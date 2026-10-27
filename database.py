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

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công cơ sở dữ liệu 'deutsch_meister.db' và 4 cấp độ A1 - B2!")

if __name__ == "__main__":
    init_db()