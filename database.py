import os
import re
import sqlite3
import urllib.parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "deutsch_meister.db")
DATABASE_URL = os.environ.get("DATABASE_URL")

def is_postgres():
    """Kiểm tra hệ thống có đang cấu hình Cloud PostgreSQL (DATABASE_URL) hay không"""
    return bool(DATABASE_URL and ("postgres" in DATABASE_URL.lower()))

class PGCursorWrapper:
    """Wrapper cho cursor PostgreSQL để tương thích 100% với cú pháp SQLite của mã nguồn"""
    def __init__(self, raw_cursor, conn):
        self.cursor = raw_cursor
        self.conn = conn
        self.lastrowid = None

    def _adapt_sql(self, sql):
        clean_sql = sql.strip()

        # 1. PRAGMA table_info emulation
        m = re.match(r"PRAGMA\s+table_info\((\w+)\);?", clean_sql, re.IGNORECASE)
        if m:
            tbl = m.group(1).lower()
            return f"SELECT 0 as cid, column_name as name, data_type as type, 0 as notnull, NULL as dflt_value, 0 as pk FROM information_schema.columns WHERE lower(table_name) = '{tbl}';", False

        # 2. PRAGMA foreign_keys hoặc pragma khác
        if clean_sql.upper().startswith("PRAGMA"):
            return "SELECT 1;", False

        # 3. Chuyển đổi '?' thành '%s' cho psycopg2
        adapted = re.sub(r"\?", "%s", clean_sql)

        # 4. INSERT OR IGNORE -> ON CONFLICT DO NOTHING
        if re.search(r"INSERT\s+OR\s+IGNORE\s+INTO", adapted, re.IGNORECASE):
            adapted = re.sub(r"INSERT\s+OR\s+IGNORE\s+INTO", "INSERT INTO", adapted, flags=re.IGNORECASE)
            adapted = adapted.rstrip("; \t\n") + " ON CONFLICT DO NOTHING;"

        # 5. Tự động thêm RETURNING id cho câu lệnh INSERT đơn lẻ nếu cần lastrowid
        is_insert = bool(re.match(r"INSERT\s+INTO", adapted, re.IGNORECASE))
        needs_returning = is_insert and ("RETURNING" not in adapted.upper()) and ("ON CONFLICT DO NOTHING" not in adapted.upper())
        if needs_returning:
            adapted = adapted.rstrip("; \t\n") + " RETURNING id;"

        return adapted, needs_returning

    def execute(self, sql, params=None):
        adapted_sql, had_returning = self._adapt_sql(sql)
        try:
            if params is not None:
                self.cursor.execute(adapted_sql, params)
            else:
                self.cursor.execute(adapted_sql)

            if had_returning:
                try:
                    res = self.cursor.fetchone()
                    if res:
                        self.lastrowid = res[0] if isinstance(res, (tuple, list)) else res.get("id", res[0])
                except Exception:
                    self.lastrowid = None
            return self
        except Exception as e:
            try:
                self.conn.rollback()
            except Exception:
                pass
            raise e

    def executemany(self, sql, params_seq):
        adapted_sql, _ = self._adapt_sql(sql)
        adapted_sql = re.sub(r"\s+RETURNING\s+id;?$", ";", adapted_sql, flags=re.IGNORECASE)
        try:
            return self.cursor.executemany(adapted_sql, params_seq)
        except Exception as e:
            try:
                self.conn.rollback()
            except Exception:
                pass
            raise e

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchmany(self, size=None):
        return self.cursor.fetchmany(size) if size else self.cursor.fetchmany()

    @property
    def rowcount(self):
        return self.cursor.rowcount

    def close(self):
        return self.cursor.close()

class PGConnectionWrapper:
    """Wrapper cho kết nối PostgreSQL để tương thích với giao diện sqlite3"""
    def __init__(self, raw_conn):
        self.raw_conn = raw_conn

    def cursor(self):
        import psycopg2.extras
        raw_cur = self.raw_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return PGCursorWrapper(raw_cur, self.raw_conn)

    def commit(self):
        return self.raw_conn.commit()

    def rollback(self):
        return self.raw_conn.rollback()

    def close(self):
        return self.raw_conn.close()

    def execute(self, sql, params=None):
        cur = self.cursor()
        cur.execute(sql, params)
        return cur

def get_connection():
    """
    Hàm tạo kết nối cơ sở dữ liệu:
    - Nếu có cấu hình biến môi trường DATABASE_URL (Cloud PostgreSQL trên Render/Neon/Supabase) -> Kết nối PostgreSQL vĩnh viễn.
    - Nếu không có (môi trường máy cá nhân Mac) -> Kết nối file SQLite deutsch_meister.db.
    """
    if is_postgres():
        try:
            import psycopg2
            import psycopg2.extras
            url = DATABASE_URL
            if url.startswith("postgres://"):
                url = url.replace("postgres://", "postgresql://", 1)
            raw_conn = psycopg2.connect(url)
            return PGConnectionWrapper(raw_conn)
        except Exception as err:
            print(f"⚠️ [DATABASE] Không thể kết nối Cloud PostgreSQL qua DATABASE_URL: {err}")
            print("🔄 [DATABASE] Đang tự động chuyển về chế độ dự phòng SQLite cục bộ...")

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Hàm khởi tạo cấu trúc bảng và dữ liệu cấp độ ban đầu cho cả SQLite và PostgreSQL"""
    conn = get_connection()
    cursor = conn.cursor()

    if is_postgres():
        # Khởi tạo bảng cho Cloud PostgreSQL (dữ liệu lưu vĩnh viễn trên Cloud Server)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS levels (
            id SERIAL PRIMARY KEY,
            code VARCHAR(10) UNIQUE NOT NULL,
            title VARCHAR(100) NOT NULL,
            description TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lessons (
            id SERIAL PRIMARY KEY,
            level_id INT REFERENCES levels(id) ON DELETE CASCADE,
            title VARCHAR(255) NOT NULL,
            grammar_content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS vocabularies (
            id SERIAL PRIMARY KEY,
            lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
            german_word VARCHAR(100) NOT NULL,
            article VARCHAR(10),
            vietnamese_meaning VARCHAR(255) NOT NULL,
            example_sentence TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id SERIAL PRIMARY KEY,
            lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
            exercise_type VARCHAR(50) NOT NULL,
            question_prompt TEXT NOT NULL,
            options_json TEXT,
            correct_answer TEXT NOT NULL,
            explanation TEXT,
            vietnamese_translation TEXT,
            extra_data TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_progress (
            user_id INT PRIMARY KEY,
            username VARCHAR(100) DEFAULT 'Học viên',
            total_exp INT DEFAULT 0,
            current_streak INT DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            token TEXT,
            highest_level_code TEXT DEFAULT 'A1',
            highest_lesson_order INTEGER DEFAULT 1,
            total_exp INTEGER DEFAULT 0,
            arena_best_score INTEGER DEFAULT 0,
            arena_total_games INTEGER DEFAULT 0,
            streak_days INTEGER DEFAULT 1,
            last_active_date TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username_lower ON users(LOWER(username));")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_studied_lessons (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            lesson_id INTEGER NOT NULL,
            level_code TEXT NOT NULL,
            lesson_order INTEGER NOT NULL,
            studied_theory INTEGER DEFAULT 1,
            practice_completed INTEGER DEFAULT 0,
            best_practice_score INTEGER DEFAULT 0,
            correct_exercises TEXT DEFAULT '[]',
            last_studied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, lesson_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS arena_daily_attempts (
            id SERIAL PRIMARY KEY,
            session_token TEXT NOT NULL UNIQUE,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            play_date TEXT NOT NULL,
            attempt_number INTEGER NOT NULL,
            status TEXT DEFAULT 'in_progress',
            final_score INTEGER DEFAULT 0,
            correct_count INTEGER DEFAULT 0,
            wrong_count INTEGER DEFAULT 0,
            scope_summary TEXT,
            breakdown_json TEXT,
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            finished_at TIMESTAMP
        );
        """)

        cursor.execute("CREATE INDEX IF NOT EXISTS idx_arena_user_date ON arena_daily_attempts(user_id, play_date);")

        default_levels = [
            ("A1", "Trình độ A1 - Khởi đầu", "Làm quen phát âm, giao tiếp cơ bản và ngữ pháp nền tảng."),
            ("A2", "Trình độ A2 - Sơ cấp", "Giao tiếp hàng ngày, mở rộng từ vựng theo chủ đề quen thuộc."),
            ("B1", "Trình độ B1 - Trung cấp", "Sử dụng tiếng Đức độc lập trong công việc, học tập và du lịch."),
            ("B2", "Trình độ B2 - Trung cao cấp", "Diễn đạt trôi chảy, thảo luận các chủ đề phức tạp và học thuật.")
        ]
        cursor.executemany("""
        INSERT INTO levels (code, title, description)
        VALUES (%s, %s, %s)
        ON CONFLICT (code) DO NOTHING;
        """, default_levels)

        cursor.execute("""
        INSERT INTO user_progress (user_id, username, total_exp, current_streak)
        VALUES (1, 'Bạn (Học viên)', 0, 1)
        ON CONFLICT (user_id) DO NOTHING;
        """)

        cursor.execute("SELECT COUNT(*) FROM users;")
        cnt_row = cursor.fetchone()
        u_count = cnt_row[0] if cnt_row else 0
        if u_count == 0:
            from werkzeug.security import generate_password_hash
            sample_users = [
                ("lukas_de", generate_password_hash("LukasPass123!", method="pbkdf2:sha256"), "B2", 10, 1890, 185, 12, 7),
                ("Minh_Anh", generate_password_hash("MinhAnhPass123!", method="pbkdf2:sha256"), "B1", 8, 1620, 160, 9, 5),
                ("HoangNam", generate_password_hash("HoangNamPass123!", method="pbkdf2:sha256"), "A2", 5, 1510, 140, 8, 4),
                ("Thao_Vy", generate_password_hash("ThaoVyPass123!", method="pbkdf2:sha256"), "A1", 4, 1120, 110, 5, 3)
            ]
            cursor.executemany("""
            INSERT INTO users (username, password_hash, highest_level_code, highest_lesson_order, total_exp, arena_best_score, arena_total_games, streak_days)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """, sample_users)

        conn.commit()
        conn.close()
        print("✅ [DATABASE] Đã kết nối và khởi tạo thành công Cloud PostgreSQL Database!")
        return

    # Chế độ SQLite cho môi trường máy cá nhân
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code VARCHAR(10) UNIQUE NOT NULL,
        title VARCHAR(100) NOT NULL,
        description TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_id INT REFERENCES levels(id) ON DELETE CASCADE,
        title VARCHAR(255) NOT NULL,
        grammar_content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vocabularies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id INT REFERENCES levels(id) ON DELETE CASCADE,
        german_word VARCHAR(100) NOT NULL,
        article VARCHAR(10),
        vietnamese_meaning VARCHAR(255) NOT NULL,
        example_sentence TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
        exercise_type VARCHAR(50) NOT NULL,
        question_prompt TEXT NOT NULL,
        options_json TEXT,
        correct_answer TEXT NOT NULL,
        explanation TEXT,
        vietnamese_translation TEXT,
        extra_data TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        user_id INT PRIMARY KEY,
        username VARCHAR(100) DEFAULT 'Học viên',
        total_exp INT DEFAULT 0,
        current_streak INT DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE COLLATE NOCASE,
        password_hash TEXT NOT NULL,
        token TEXT,
        highest_level_code TEXT DEFAULT 'A1',
        highest_lesson_order INTEGER DEFAULT 1,
        total_exp INTEGER DEFAULT 0,
        arena_best_score INTEGER DEFAULT 0,
        arena_total_games INTEGER DEFAULT 0,
        streak_days INTEGER DEFAULT 1,
        last_active_date TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username_lower ON users(LOWER(username));")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_studied_lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        lesson_id INTEGER NOT NULL,
        level_code TEXT NOT NULL,
        lesson_order INTEGER NOT NULL,
        studied_theory INTEGER DEFAULT 1,
        practice_completed INTEGER DEFAULT 0,
        best_practice_score INTEGER DEFAULT 0,
        correct_exercises TEXT DEFAULT '[]',
        last_studied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(user_id, lesson_id),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS arena_daily_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_token TEXT NOT NULL UNIQUE,
        user_id INTEGER NOT NULL,
        play_date TEXT NOT NULL,
        attempt_number INTEGER NOT NULL,
        status TEXT DEFAULT 'in_progress',
        final_score INTEGER DEFAULT 0,
        correct_count INTEGER DEFAULT 0,
        wrong_count INTEGER DEFAULT 0,
        scope_summary TEXT,
        breakdown_json TEXT,
        started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        finished_at TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_arena_user_date ON arena_daily_attempts(user_id, play_date);")

    default_levels = [
        ("A1", "Trình độ A1 - Khởi đầu", "Làm quen phát âm, giao tiếp cơ bản và ngữ pháp nền tảng."),
        ("A2", "Trình độ A2 - Sơ cấp", "Giao tiếp hàng ngày, mở rộng từ vựng theo chủ đề quen thuộc."),
        ("B1", "Trình độ B1 - Trung cấp", "Sử dụng tiếng Đức độc lập trong công việc, học tập và du lịch."),
        ("B2", "Trình độ B2 - Trung cao cấp", "Diễn đạt trôi chảy, thảo luận các chủ đề phức tạp và học thuật.")
    ]
    cursor.executemany("""
    INSERT OR IGNORE INTO levels (code, title, description)
    VALUES (?, ?, ?);
    """, default_levels)

    cursor.execute("""
    INSERT OR IGNORE INTO user_progress (user_id, username, total_exp, current_streak)
    VALUES (1, 'Bạn (Học viên)', 0, 1);
    """)

    cursor.execute("SELECT COUNT(*) FROM users;")
    if cursor.fetchone()[0] == 0:
        from werkzeug.security import generate_password_hash
        sample_users = [
            ("lukas_de", generate_password_hash("LukasPass123!", method="pbkdf2:sha256"), "B2", 10, 1890, 185, 12, 7),
            ("Minh_Anh", generate_password_hash("MinhAnhPass123!", method="pbkdf2:sha256"), "B1", 8, 1620, 160, 9, 5),
            ("HoangNam", generate_password_hash("HoangNamPass123!", method="pbkdf2:sha256"), "A2", 5, 1510, 140, 8, 4),
            ("Thao_Vy", generate_password_hash("ThaoVyPass123!", method="pbkdf2:sha256"), "A1", 4, 1120, 110, 5, 3)
        ]
        cursor.executemany("""
        INSERT INTO users (username, password_hash, highest_level_code, highest_lesson_order, total_exp, arena_best_score, arena_total_games, streak_days)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, sample_users)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công cơ sở dữ liệu SQLite 'deutsch_meister.db' và 4 cấp độ A1 - B2!")

if __name__ == "__main__":
    init_db()
