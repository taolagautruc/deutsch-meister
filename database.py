import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "deutsch_meister.db")

def get_connection():
    """Hàm tạo kết nối tới cơ sở dữ liệu SQLite"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Giúp trả về dữ liệu dạng từ điển (dict) dễ đọc
    conn.execute("PRAGMA foreign_keys = ON;")  # Bật kiểm tra khóa ngoại
    return conn

def init_db():
    """Hàm khởi tạo các bảng SQL và dữ liệu cấp độ ban đầu"""
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Bảng Trình độ (Levels)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS levels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code VARCHAR(10) UNIQUE NOT NULL,
        title VARCHAR(100) NOT NULL,
        description TEXT
    );
    """)

    # 2. Bảng Bài học (Lessons)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level_id INT REFERENCES levels(id) ON DELETE CASCADE,
        title VARCHAR(255) NOT NULL,
        grammar_content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. Bảng Từ vựng (Vocabularies)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vocabularies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
        german_word VARCHAR(100) NOT NULL,
        article VARCHAR(10),
        vietnamese_meaning VARCHAR(255) NOT NULL,
        example_sentence TEXT
    );
    """)

    # 4. Bảng Theo dõi tiến độ & EXP người dùng (User Progress)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_progress (
        user_id INT PRIMARY KEY,
        username VARCHAR(100) DEFAULT 'Học viên',
        total_exp INT DEFAULT 0,
        current_streak INT DEFAULT 0,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 5. Bảng Tài khoản người chơi cạnh tranh (Users - UNIQUE COLLATE NOCASE)
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

    # 6. Bảng Tiến độ bài học của từng tài khoản (user_studied_lessons)
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

    # 7. Bảng Phiên chơi Đấu trường (arena_daily_attempts - tối đa 2 lần/ngày)
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

    # Thêm sẵn 4 cấp độ A1, A2, B1, B2 nếu chưa có
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

    # Tạo sẵn 1 hồ sơ người dùng mặc định để lưu điểm EXP
    cursor.execute("""
    INSERT OR IGNORE INTO user_progress (user_id, username, total_exp, current_streak)
    VALUES (1, 'Bạn (Học viên)', 0, 1);
    """)

    # Khởi tạo các tài khoản thi đua mẫu cho Bảng xếp hạng nếu bảng users trống
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
    print("✅ Đã khởi tạo thành công cơ sở dữ liệu 'deutsch_meister.db' và 4 cấp độ A1 - B2!")

if __name__ == "__main__":
    init_db()