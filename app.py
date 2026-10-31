import json
import os
import re
import uuid
import urllib.parse
import urllib.request
from datetime import datetime, timezone, timedelta
from flask import Flask, jsonify, request, render_template, Response, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_connection, init_db
from arena_generator import build_arena_questions_for_user, get_user_allowed_lessons

VN_TZ = timezone(timedelta(hours=7))

def get_vn_today_str():
    """Trả về ngày hiện tại theo chuẩn YYYY-MM-DD theo múi giờ Việt Nam (UTC+7)"""
    return datetime.now(VN_TZ).strftime("%Y-%m-%d")

def ensure_question_number(orig_question: str, new_question_body: str = None, fallback_index: int = None) -> str:
    """
    Bảo toàn và chuẩn hóa tiền tố 'Câu <số> ' cho mọi câu hỏi bài tập.
    """
    target = new_question_body if new_question_body is not None else orig_question
    if not target:
        return target or ""
    src = orig_question.strip() if orig_question else ""
    match = re.match(r"^(Câu\s+\d+\s*)", src, re.IGNORECASE)
    prefix = match.group(1) if match else (f"Câu {fallback_index} " if fallback_index else "")
    
    if prefix and not re.match(r"^Câu\s+\d+", target.strip(), re.IGNORECASE):
        return f"{prefix.strip()} {target.strip()}"
    return target

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "deutsch-meister-arena-2026-super-secret-key-120s")
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)
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

        # Đảm bảo bảng users có cột token và updated_at
        cursor.execute("PRAGMA table_info(users);")
        u_cols = [col["name"] for col in cursor.fetchall()]
        if "token" not in u_cols:
            cursor.execute("ALTER TABLE users ADD COLUMN token TEXT;")
            conn.commit()
        if "updated_at" not in u_cols:
            cursor.execute("ALTER TABLE users ADD COLUMN updated_at TIMESTAMP;")
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

        cursor.execute("SELECT COUNT(*) as cnt FROM lessons WHERE title LIKE 'Bài 3%';")
        if cursor.fetchone()["cnt"] == 0:
            from lessons.a1.seed_a1_b3 import seed_lesson_3
            seed_lesson_3()

        cursor.execute("SELECT COUNT(*) as cnt FROM lessons WHERE title LIKE 'Bài 4%';")
        if cursor.fetchone()["cnt"] == 0:
            from lessons.a1.seed_a1_b4 import seed_lesson_4
            seed_lesson_4()
            
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
    
    uid = session.get("user_id")
    user = None
    if uid:
        cursor.execute("SELECT id as user_id, username, total_exp, streak_days as current_streak FROM users WHERE id = ?;", (uid,))
        row = cursor.fetchone()
        if row:
            user = dict(row)
            
    if not user:
        cursor.execute("SELECT * FROM user_progress WHERE user_id = 1;")
        row = cursor.fetchone()
        user = dict(row) if row else {"user_id": 1, "username": "Học viên", "total_exp": 0, "current_streak": 1}
        
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
        import random
        for idx, ex in enumerate(cursor.fetchall()):
            ex_dict = dict(ex)
            opts = json.loads(ex_dict["options_json"]) if ex_dict["options_json"] else []
            if opts and isinstance(opts, list) and len(opts) > 1:
                opts = list(opts)
                random.shuffle(opts)
            ex_dict["options"] = opts
            ex_dict["question"] = ensure_question_number(ex_dict.get("question", ""), fallback_index=idx + 1)
            exercises.append(ex_dict)
        lesson["exercises"] = exercises

    conn.close()
    return jsonify({"level": dict(level), "lessons": lessons})

@app.route("/api/exp/add", methods=["POST"])
def add_exp():
    data = request.get_json() or {}
    exp_gained = int(data.get("exp", 10))
    uid = session.get("user_id")
    conn = get_connection()
    cursor = conn.cursor()
    if uid:
        cursor.execute("""
            UPDATE users
            SET total_exp = total_exp + ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?;
        """, (exp_gained, uid))
        conn.commit()
        cursor.execute("SELECT id, username, total_exp FROM users WHERE id = ?;", (uid,))
        user_row = cursor.fetchone()
        updated_user = dict(user_row) if user_row else {"total_exp": exp_gained}
    else:
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

# =============================================================================
# HỆ THỐNG ĐĂNG KÝ / ĐĂNG NHẬP / TIẾN ĐỘ & ĐẤU TRƯỜNG PHẢN XẠ 2 PHÚT (API)
# =============================================================================

@app.route("/api/auth/check-username", methods=["GET"])
def check_username():
    """Kiểm tra tính hợp lệ & kiểm tra trùng tên không phân biệt hoa thường"""
    raw = request.args.get("username", "").strip()
    if len(raw) < 4:
        return jsonify({"available": False, "message": "Tên tài khoản phải có tối thiểu 4 ký tự."})
    if len(raw) > 24:
        return jsonify({"available": False, "message": "Tên tài khoản không được vượt quá 24 ký tự."})
    if not re.match(r"^[a-zA-Z0-9_]{4,24}$", raw):
        return jsonify({"available": False, "message": "Chỉ chấp nhận chữ cái không dấu, chữ số và gạch dưới (_)."})

    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE LOWER(username) = LOWER(?);", (raw,))
    row = c.fetchone()
    conn.close()
    if row:
        return jsonify({
            "available": False,
            "message": f"Tên tài khoản '{raw}' đã tồn tại trên hệ thống! Vui lòng chọn một tên khác để thi đua."
        })
    return jsonify({"available": True, "message": "Tên tài khoản hợp lệ và có thể sử dụng!"})

@app.route("/api/auth/register", methods=["POST"])
def register():
    """Đăng ký tài khoản cạnh tranh mới"""
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")

    if len(username) < 4 or len(username) > 24:
        return jsonify({"error": "Tên tài khoản phải từ 4 đến 24 ký tự!"}), 400
    if not re.match(r"^[a-zA-Z0-9_]{4,24}$", username):
        return jsonify({"error": "Tên tài khoản chỉ được chứa chữ cái không dấu, chữ số và dấu gạch dưới (_)."}), 400
    if len(password) < 8:
        return jsonify({"error": "Mật khẩu phải có tối thiểu 8 ký tự!"}), 400

    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT 1 FROM users WHERE LOWER(username) = LOWER(?);", (username,))
    if c.fetchone():
        conn.close()
        return jsonify({
            "error": f"Tên tài khoản '{username}' đã tồn tại trên hệ thống! Vui lòng chọn một tên khác để thi đua."
        }), 409

    pwd_hash = generate_password_hash(password, method="pbkdf2:sha256")
    today = get_vn_today_str()
    auth_token = str(uuid.uuid4())
    c.execute("""
        INSERT INTO users (username, password_hash, token, highest_level_code, highest_lesson_order, total_exp, arena_best_score, arena_total_games, streak_days, last_active_date)
        VALUES (?, ?, ?, 'A1', 1, 0, 0, 0, 1, ?);
    """, (username, pwd_hash, auth_token, today))
    user_id = c.lastrowid

    # Đánh dấu mặc định bài đầu tiên đã học
    c.execute("""
        INSERT OR IGNORE INTO user_studied_lessons (user_id, lesson_id, level_code, lesson_order, studied_theory)
        VALUES (?, 14, 'A1', 1, 1);
    """, (user_id,))
    conn.commit()

    c.execute("SELECT id, username, highest_level_code, highest_lesson_order, total_exp, arena_best_score, arena_total_games, streak_days FROM users WHERE id = ?;", (user_id,))
    user_dict = dict(c.fetchone())
    conn.close()

    session.permanent = True
    session["user_id"] = user_id
    user_dict["token"] = auth_token
    user_dict["studied_lessons"] = [14]
    user_dict["arena_attempts_today"] = 0
    user_dict["arena_remaining_today"] = 2

    return jsonify({"message": f"Chào mừng {username}! Đăng ký thành công.", "user": user_dict, "token": auth_token})

@app.route("/api/auth/login", methods=["POST"])
def login():
    """Đăng nhập tài khoản thi đua"""
    data = request.get_json() or {}
    username = data.get("username", "").strip()
    password = data.get("password", "")

    if not username or not password:
        return jsonify({"error": "Vui lòng nhập đầy đủ tên tài khoản và mật khẩu!"}), 400

    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(?);", (username,))
    row = c.fetchone()
    if not row or not check_password_hash(row["password_hash"], password):
        conn.close()
        return jsonify({"error": "Tên tài khoản hoặc mật khẩu không chính xác!"}), 401

    user_dict = dict(row)
    user_dict.pop("password_hash", None)
    
    auth_token = user_dict.get("token") or str(uuid.uuid4())
    today = get_vn_today_str()
    c.execute("UPDATE users SET token = ?, last_active_date = ? WHERE id = ?;", (auth_token, today, user_dict["id"]))
    conn.commit()

    session.permanent = True
    session["user_id"] = user_dict["id"]
    user_dict["token"] = auth_token

    # Lấy danh sách bài đã học
    c.execute("SELECT lesson_id FROM user_studied_lessons WHERE user_id = ?;", (user_dict["id"],))
    user_dict["studied_lessons"] = [r["lesson_id"] for r in c.fetchall()]

    # Lấy số lượt đấu trường hôm nay
    c.execute("SELECT COUNT(*) AS cnt FROM arena_daily_attempts WHERE user_id = ? AND play_date = ?;", (user_dict["id"], today))
    used = c.fetchone()["cnt"]
    conn.close()

    user_dict["arena_attempts_today"] = used
    user_dict["arena_remaining_today"] = max(0, 2 - used)

    return jsonify({"message": f"Đăng nhập thành công! Chào {user_dict['username']}.", "user": user_dict, "token": auth_token})

@app.route("/api/auth/restore-session", methods=["POST"])
def restore_session():
    """Khôi phục phiên đăng nhập từ localStorage token khi người dùng tải lại web"""
    data = request.get_json() or {}
    token = data.get("token", "").strip()
    if not token:
        return jsonify({"logged_in": False, "user": None}), 400

    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, username, token, highest_level_code, highest_lesson_order, total_exp, arena_best_score, arena_total_games, streak_days, last_active_date FROM users WHERE token = ?;", (token,))
    row = c.fetchone()
    if not row:
        conn.close()
        return jsonify({"logged_in": False, "user": None}), 404

    user_dict = dict(row)
    session.permanent = True
    session["user_id"] = user_dict["id"]

    today = get_vn_today_str()
    c.execute("UPDATE users SET last_active_date = ? WHERE id = ?;", (today, user_dict["id"]))
    conn.commit()

    c.execute("SELECT lesson_id FROM user_studied_lessons WHERE user_id = ?;", (user_dict["id"],))
    user_dict["studied_lessons"] = [r["lesson_id"] for r in c.fetchall()]

    c.execute("SELECT COUNT(*) AS cnt FROM arena_daily_attempts WHERE user_id = ? AND play_date = ?;", (user_dict["id"], today))
    used = c.fetchone()["cnt"]
    conn.close()

    user_dict["arena_attempts_today"] = used
    user_dict["arena_remaining_today"] = max(0, 2 - used)

    return jsonify({"logged_in": True, "user": user_dict, "token": token})

@app.route("/api/auth/logout", methods=["POST"])
def logout():
    """Đăng xuất phiên hiện tại"""
    session.pop("user_id", None)
    return jsonify({"message": "Đã đăng xuất thành công!"})

@app.route("/api/auth/me", methods=["GET"])
def get_me():
    """Lấy thông tin người dùng hiện tại"""
    uid = session.get("user_id")
    if not uid:
        return jsonify({"logged_in": False, "user": None})

    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, username, highest_level_code, highest_lesson_order, total_exp, arena_best_score, arena_total_games, streak_days, last_active_date FROM users WHERE id = ?;", (uid,))
    row = c.fetchone()
    if not row:
        conn.close()
        session.pop("user_id", None)
        return jsonify({"logged_in": False, "user": None})

    user_dict = dict(row)
    c.execute("SELECT lesson_id FROM user_studied_lessons WHERE user_id = ?;", (uid,))
    user_dict["studied_lessons"] = [r["lesson_id"] for r in c.fetchall()]

    today = get_vn_today_str()
    c.execute("SELECT COUNT(*) AS cnt FROM arena_daily_attempts WHERE user_id = ? AND play_date = ?;", (uid, today))
    used = c.fetchone()["cnt"]
    conn.close()

    user_dict["arena_attempts_today"] = used
    user_dict["arena_remaining_today"] = max(0, 2 - used)

    return jsonify({"logged_in": True, "user": user_dict})

@app.route("/api/progress/mark-studied", methods=["POST"])
def mark_studied():
    """Lưu bài học người dùng vừa xem để mở rộng phạm vi câu hỏi Đấu trường"""
    data = request.get_json() or {}
    lesson_id = int(data.get("lesson_id", 14))
    level_code = data.get("level_code", "A1")
    lesson_order = int(data.get("lesson_order", 1))

    uid = session.get("user_id")
    if uid:
        conn = get_connection()
        c = conn.cursor()
        c.execute("""
            INSERT INTO user_studied_lessons (user_id, lesson_id, level_code, lesson_order, studied_theory, last_studied_at)
            VALUES (?, ?, ?, ?, 1, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id, lesson_id) DO UPDATE SET last_studied_at = CURRENT_TIMESTAMP;
        """, (uid, lesson_id, level_code, lesson_order))

        c.execute("""
            UPDATE users
            SET highest_lesson_order = MAX(highest_lesson_order, ?),
                highest_level_code = ?
            WHERE id = ?;
        """, (lesson_order, level_code, uid))
        conn.commit()
        conn.close()

    return jsonify({"success": True, "lesson_id": lesson_id, "lesson_order": lesson_order})

@app.route("/api/arena/start", methods=["POST"])
def arena_start():
    """Bắt đầu ván Đấu trường 2 phút (chặn nếu đã chơi >= 2 lần/ngày)"""
    uid = session.get("user_id")
    if not uid:
        return jsonify({"error": "Vui lòng đăng nhập hoặc đăng ký tài khoản để tham gia Đấu trường Đua Top!"}), 401

    today = get_vn_today_str()
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) AS cnt FROM arena_daily_attempts WHERE user_id = ? AND play_date = ?;", (uid, today))
    used = c.fetchone()["cnt"]

    if used >= 2:
        conn.close()
        return jsonify({
            "error": "Mỗi tài khoản chỉ được tham gia Đấu trường tối đa 2 lần mỗi ngày! Hãy quay lại vào ngày mai (00:00) nhé.",
            "remaining": 0,
            "attempts_today": used
        }), 403

    attempt_num = used + 1
    session_token = str(uuid.uuid4())

    # Khởi tạo bản ghi attempt in_progress chống gian lận F5
    c.execute("""
        INSERT INTO arena_daily_attempts (session_token, user_id, play_date, attempt_number, status)
        VALUES (?, ?, ?, ?, 'in_progress');
    """, (session_token, uid, today, attempt_num))
    conn.commit()
    conn.close()

    # Sinh danh sách câu hỏi theo đúng tiến độ người chơi
    questions = build_arena_questions_for_user(uid, count=80)

    return jsonify({
        "session_token": session_token,
        "attempt_number": attempt_num,
        "remaining_today": 2 - attempt_num,
        "duration_seconds": 120,
        "questions": questions
    })

@app.route("/api/arena/finish", methods=["POST"])
def arena_finish():
    """Tổng kết ván Đấu trường và cộng điểm"""
    uid = session.get("user_id")
    if not uid:
        return jsonify({"error": "Chưa đăng nhập!"}), 401

    data = request.get_json() or {}
    session_token = data.get("session_token")
    final_score = int(data.get("final_score", 0))
    correct_count = int(data.get("correct_count", 0))
    wrong_count = int(data.get("wrong_count", 0))
    breakdown = data.get("breakdown", {})
    scope_summary = data.get("scope_summary", "A1")

    conn = get_connection()
    c = conn.cursor()

    if session_token:
        c.execute("""
            UPDATE arena_daily_attempts
            SET status = 'completed',
                final_score = ?,
                correct_count = ?,
                wrong_count = ?,
                scope_summary = ?,
                breakdown_json = ?,
                finished_at = CURRENT_TIMESTAMP
            WHERE session_token = ? AND user_id = ?;
        """, (final_score, correct_count, wrong_count, scope_summary, json.dumps(breakdown), session_token, uid))

    # Cập nhật điểm cho user
    c.execute("""
        UPDATE users
        SET total_exp = total_exp + MAX(0, ?),
            arena_best_score = MAX(arena_best_score, ?),
            arena_total_games = arena_total_games + 1
        WHERE id = ?;
    """, (final_score, final_score, uid))

    if uid == 1:
        c.execute("UPDATE user_progress SET total_exp = total_exp + MAX(0, ?) WHERE user_id = 1;", (final_score,))

    conn.commit()

    c.execute("SELECT id, username, total_exp, arena_best_score, arena_total_games FROM users WHERE id = ?;", (uid,))
    user_updated = dict(c.fetchone())
    conn.close()

    return jsonify({
        "success": True,
        "final_score": final_score,
        "correct_count": correct_count,
        "wrong_count": wrong_count,
        "user": user_updated
    })

@app.route("/api/arena/leaderboard", methods=["GET"])
def get_leaderboard():
    """Lấy Bảng Xếp Hạng Thực Tế từ Database: Hôm nay & Kỷ lục Mọi thời đại"""
    today = get_vn_today_str()
    conn = get_connection()
    c = conn.cursor()

    # 1. Bảng xếp hạng trong ngày hôm nay
    c.execute("""
        SELECT a.user_id, u.username, u.highest_level_code, MAX(a.final_score) as best_today_score,
               u.total_exp
        FROM arena_daily_attempts a
        JOIN users u ON a.user_id = u.id
        WHERE a.play_date = ? AND a.status = 'completed'
        GROUP BY a.user_id
        ORDER BY best_today_score DESC, u.total_exp DESC
        LIMIT 10;
    """, (today,))
    daily_rows = [dict(r) for r in c.fetchall()]

    # 2. Bảng xếp hạng All-Time
    c.execute("""
        SELECT id as user_id, username, highest_level_code, arena_best_score, total_exp, arena_total_games
        FROM users
        ORDER BY arena_best_score DESC, total_exp DESC
        LIMIT 10;
    """, ())
    all_time_rows = [dict(r) for r in c.fetchall()]
    conn.close()

    return jsonify({
        "today_date": today,
        "daily_top": daily_rows,
        "all_time_top": all_time_rows
    })

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