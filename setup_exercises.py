import json
from database import get_connection

def init_exercises_and_sample_data():
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Tạo bảng Bài tập (Exercises) hỗ trợ 7 dạng bài & Game EXP
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
        exercise_type VARCHAR(50) NOT NULL, -- 'trac_nghiem', 'dien_khuyet', 'dich', 'nghe', 'noi', 'doc', 'viet'
        question TEXT NOT NULL,             -- Nội dung câu hỏi / câu cần dịch / đoạn văn
        options_json TEXT,                  -- Các lựa chọn đáp án (dạng JSON cho bài trắc nghiệm)
        correct_answer TEXT NOT NULL,       -- Đáp án chính xác
        explanation TEXT,                   -- Giải thích chi tiết sau khi làm bài
        exp_reward INT DEFAULT 10           -- Điểm EXP thưởng khi làm đúng
    );
    """)

    # 2. Lấy ID của trình độ A1
    cursor.execute("SELECT id FROM levels WHERE code = 'A1';")
    level_a1 = cursor.fetchone()

    if level_a1:
        a1_id = level_a1["id"]

        # Kiểm tra xem đã có bài học mẫu nào chưa để tránh tạo trùng
        cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 1:%';", (a1_id,))
        existing_lesson = cursor.fetchone()

        if not existing_lesson:
            # Thêm 1 Bài học mẫu cho A1
            cursor.execute("""
            INSERT INTO lessons (level_id, title, grammar_content)
            VALUES (?, ?, ?);
            """, (
                a1_id,
                "Bài 1: Chào hỏi và Làm quen (Begrüßung)",
                "Trong tiếng Đức, danh từ luôn viết hoa chữ cái đầu và đi kèm mạo từ xác định: der (giống đực), die (giống cái), das (giống trung)."
            ))
            lesson_id = cursor.lastrowid

            # Thêm 3 Từ vựng mẫu đủ 3 giống der, die, das
            sample_vocabs = [
                (lesson_id, "Tisch", "der", "Cái bàn", "Der Tisch ist neu. (Cái bàn này mới.)"),
                (lesson_id, "Lampe", "die", "Cái đèn", "Die Lampe ist schön. (Cái đèn này đẹp.)"),
                (lesson_id, "Buch", "das", "Quyển sách", "Das Buch ist interessant. (Quyển sách rất thú vị.)")
            ]
            cursor.executemany("""
            INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
            VALUES (?, ?, ?, ?, ?);
            """, sample_vocabs)

            # Thêm thử các dạng bài tập mẫu cho Bài 1
            sample_exercises = [
                (
                    lesson_id,
                    "trac_nghiem",
                    "Mạo từ đúng của danh từ 'Buch' (Quyển sách) là gì?",
                    json.dumps(["der", "die", "das", "den"]),
                    "das",
                    "'Buch' là danh từ giống trung trong tiếng Đức nên đi với mạo từ 'das'.",
                    15
                ),
                (
                    lesson_id,
                    "dien_khuyet",
                    "Điền từ còn thiếu vào chỗ trống: 'Guten ___! (Chào buổi sáng!)'",
                    None,
                    "Morgen",
                    "'Guten Morgen' là câu chào buổi sáng thông dụng trong tiếng Đức.",
                    15
                ),
                (
                    lesson_id,
                    "dich",
                    "Dịch câu sau sang tiếng Đức: 'Quyển sách rất thú vị.'",
                    None,
                    "Das Buch ist interessant.",
                    "Cấu trúc: Das Buch (Quyển sách) + ist (thì/là) + interessant (thú vị).",
                    20
                )
            ]
            cursor.executemany("""
            INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, sample_exercises)

    conn.commit()

    # 3. Kiểm tra và in kết quả ra màn hình
    cursor.execute("SELECT COUNT(*) AS total FROM lessons;")
    total_lessons = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM vocabularies;")
    total_vocabs = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM exercises;")
    total_exercises = cursor.fetchone()["total"]

    conn.close()
    print("✅ Đã tạo xong bảng 'exercises' (hỗ trợ 7 dạng bài tập & EXP)!")
    print(f"📚 Dữ liệu hiện có trong Database: {total_lessons} Bài học | {total_vocabs} Từ vựng | {total_exercises} Bài tập mẫu.")

if __name__ == "__main__":
    init_exercises_and_sample_data()