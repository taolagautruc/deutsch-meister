import json
import urllib.parse
import urllib.request
from flask import Flask, jsonify, request, render_template, Response
from database import get_connection

app = Flask(__name__)
app.json.ensure_ascii = False

def ensure_db_initialized():
    """Tự động kiểm tra và khởi tạo dữ liệu nếu chạy trên máy chủ mới (Render/Cloud)"""
    try:
        from database import init_db, get_connection
        init_db()
        conn = get_connection()
        cursor = conn.cursor()
        
        # Đảm bảo bảng exercises có cột extra_data
        cursor.execute("PRAGMA table_info(exercises);")
        columns = [col["name"] for col in cursor.fetchall()]
        if "extra_data" not in columns:
            cursor.execute("ALTER TABLE exercises ADD COLUMN extra_data TEXT;")
            conn.commit()

        cursor.execute("SELECT COUNT(*) as cnt FROM lessons WHERE title LIKE 'Bài 1 (P1)%';")
        if cursor.fetchone()["cnt"] == 0:
            from lessons.a1.seed_a1_b1_p1 import seed_lesson_1_part_1
            seed_lesson_1_part_1()
            
        cursor.execute("SELECT COUNT(*) as cnt FROM lessons WHERE title LIKE 'Bài 1 (P2)%';")
        if cursor.fetchone()["cnt"] == 0:
            from lessons.a1.seed_a1_b1_p2 import seed_lesson_1_part_2
            seed_lesson_1_part_2()
            
        cursor.execute("SELECT COUNT(*) as cnt FROM lessons WHERE title LIKE 'Bài 2%';")
        if cursor.fetchone()["cnt"] == 0:
            from lessons.a1.seed_a1_b2 import seed_lesson_2
            seed_lesson_2()
            
        conn.close()
    except Exception as e:
        print("ensure_db_initialized:", e)

ensure_db_initialized()

@app.route("/")
def index():
    return render_template("index.html")

# Cổng âm thanh phát âm chuẩn giọng Đức bản xứ (Google German TTS)
@app.route("/api/tts")
def tts_german():
    text = request.args.get("text", "").strip()
    if not text:
        return "Missing text", 400
    encoded = urllib.parse.quote(text)
    tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&tl=de&client=tw-ob&q={encoded}"
    req = urllib.request.Request(tts_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            audio_data = resp.read()
        return Response(audio_data, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 502

@app.route("/api/overview", methods=["GET"])
def get_overview():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM levels ORDER BY id;")
    levels = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT * FROM user_progress WHERE user_id = 1;")
    user = dict(cursor.fetchone())
    conn.close()
    return jsonify({"levels": levels, "user": user})

@app.route("/api/levels/<level_code>", methods=["GET"])
def get_level_data(level_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM levels WHERE code = ?;", (level_code.upper(),))
    level = cursor.fetchone()
    if not level:
        conn.close()
        return jsonify({"error": "Không tìm thấy trình độ này"}), 404

    cursor.execute("SELECT * FROM lessons WHERE level_id = ? ORDER BY id;", (level["id"],))
    lessons = [dict(row) for row in cursor.fetchall()]

    for lesson in lessons:
        cursor.execute("SELECT * FROM vocabularies WHERE lesson_id = ?;", (lesson["id"],))
        lesson["vocabularies"] = [dict(row) for row in cursor.fetchall()]

        cursor.execute("SELECT * FROM exercises WHERE lesson_id = ? ORDER BY id;", (lesson["id"],))
        exercises = []
        for ex in cursor.fetchall():
            ex_dict = dict(ex)
            ex_dict["options"] = json.loads(ex_dict["options_json"]) if ex_dict["options_json"] else []
            exercises.append(ex_dict)
        lesson["exercises"] = exercises

    conn.close()
    return jsonify({"level": dict(level), "lessons": lessons})

@app.route("/api/exp/add", methods=["POST"])
def add_exp():
    data = request.get_json()
    exp_gained = int(data.get("exp", 10))
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user_progress
        SET total_exp = total_exp + ?, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = 1;
    """, (exp_gained,))
    conn.commit()
    cursor.execute("SELECT * FROM user_progress WHERE user_id = 1;")
    updated_user = dict(cursor.fetchone())
    conn.close()
    return jsonify({"message": f"Đã cộng thêm {exp_gained} EXP!", "user": updated_user})

if __name__ == "__main__":
    import os
    import socket

    def is_port_in_use(p):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('127.0.0.1', p)) == 0

    port = int(os.environ.get("PORT", 5000))
    if port == 5000 and is_port_in_use(5000):
        print("⚠️ Cổng 5000 đang được macOS AirPlay Receiver sử dụng. Tự động chuyển sang cổng 5001...")
        port = 5001

    print(f"🚀 DeutschMeister đang chạy tại: http://127.0.0.1:{port}")
    app.run(debug=True, host="0.0.0.0", port=port)