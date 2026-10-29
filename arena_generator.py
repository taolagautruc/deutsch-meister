"""
arena_generator.py - Bộ sinh & lọc câu hỏi Đấu trường Phản xạ 2 phút (9 dạng bài tập)
Tuân thủ tuyệt đối quy tắc 'Học đến đâu - Thi đến đó' theo chuẩn CEFR A1 -> B2.
"""

import json
import random
import sqlite3
from database import get_connection

LEVEL_RANK = {
    "A1": 1,
    "A2": 2,
    "B1": 3,
    "B2": 4
}

# Điểm số chuẩn theo Ma trận đặc tả kỹ thuật
TYPE_POINTS = {
    "trac_nghiem": {"correct": 5, "wrong": -2, "label": "Trắc nghiệm"},
    "dien_khuyet": {"correct": 7, "wrong": -3, "label": "Điền khuyết"},
    "dich_nghia_vd": {"correct": 6, "wrong": -3, "label": "Dịch từ: Việt → Đức"},
    "dich_nghia_dv": {"correct": 6, "wrong": -3, "label": "Dịch từ: Đức → Việt"},
    "noi_o": {"correct": 10, "wrong": -4, "label": "Nối ô (4 cặp)"},
    "dich_cau_vd": {"correct": 15, "wrong": -6, "label": "Dịch câu: Việt → Đức"},
    "dich_cau_dv": {"correct": 15, "wrong": -6, "label": "Dịch câu: Đức → Việt"},
    "nghe_dien": {"correct": 10, "wrong": -4, "label": "Nghe & Điền"},
    "dien_tao_cau": {"correct": 5, "wrong": -2, "label": "Điền tạo câu"}
}

# Bảng ánh xạ ID bài học hiện tại sang order
LESSON_ORDER_MAP = {
    14: ("A1", 1, "Bài 1 (P1): Làm quen, Bảng chữ cái, Đếm số"),
    15: ("A1", 2, "Bài 1 (P2): Gọi đồ, Đại từ, Chia động từ, Euro"),
    16: ("A1", 3, "Bài 2: Đồ dùng, Giống der/die/das, Mạo từ, können"),
    17: ("A1", 4, "Bài 3: Địa danh, Phương hướng, Präteritum war/waren"),
    18: ("A1", 5, "Bài 4: Nhà ở, Nominativ vs Akkusativ, Mạo từ sở hữu")
}

def get_user_allowed_lessons(user_id):
    """
    Xác định danh sách các bài học hợp lệ cho người dùng theo luật:
    1. Các bài nằm trong user_studied_lessons
    2. Các bài <= highest_level_code và <= highest_lesson_order
    3. Nếu chưa học bài nào, mặc định cho phép các bài trong A1 hiện có
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Lấy thông tin user
    cursor.execute("SELECT highest_level_code, highest_lesson_order FROM users WHERE id = ?;", (user_id,))
    u_row = cursor.fetchone()
    highest_lvl = u_row["highest_level_code"] if u_row else "A1"
    highest_order = u_row["highest_lesson_order"] if u_row else 5

    # Lấy danh sách bài đã học
    cursor.execute("SELECT lesson_id, level_code, lesson_order FROM user_studied_lessons WHERE user_id = ?;", (user_id,))
    studied_rows = cursor.fetchall()
    conn.close()

    studied_set = {r["lesson_id"] for r in studied_rows}

    allowed_lesson_ids = []
    user_rank = LEVEL_RANK.get(highest_lvl, 1)

    for lid, (lvl, order, title) in LESSON_ORDER_MAP.items():
        lvl_rank = LEVEL_RANK.get(lvl, 1)
        if lid in studied_set:
            allowed_lesson_ids.append(lid)
        elif lvl_rank < user_rank:
            allowed_lesson_ids.append(lid)
        elif lvl_rank == user_rank and order <= highest_order:
            allowed_lesson_ids.append(lid)

    # Nếu vì lý do nào đó rỗng, mặc định mở tối thiểu Bài 1 P1 hoặc tất cả bài A1 hiện có
    if not allowed_lesson_ids:
        allowed_lesson_ids = list(LESSON_ORDER_MAP.keys())

    return allowed_lesson_ids

# =============================================================================
# KHO DỮ LIỆU TỰ CHẾ PROCEDURAL THEO TỪNG BÀI HỌC (LESSON 1 -> 5)
# =============================================================================

ARENA_DATA_BY_LESSON = {
    # -------------------------------------------------------------------------
    # BÀI 1 (P1): Làm quen, Phát âm, Đếm số, Chào hỏi, Giờ giấc
    # -------------------------------------------------------------------------
    1: {
        "vocab_pairs": [
            ("Hallo!", "Xin chào! (thân mật)"),
            ("Guten Morgen!", "Chào buổi sáng!"),
            ("Guten Tag!", "Chào ngày mới / Buổi trưa!"),
            ("Guten Abend!", "Chào buổi tối!"),
            ("Gute Nacht!", "Chúc ngủ ngon!"),
            ("Auf Wiedersehen!", "Hẹn gặp lại! (trang trọng)"),
            ("Tschüss!", "Tạm biệt! (thân mật)"),
            ("Bis morgen!", "Hẹn gặp lại ngày mai!"),
            ("eins", "Số 1"),
            ("sechzehn", "Số 16"),
            ("siebzehn", "Số 17"),
            ("dreißig", "Số 30"),
            ("einundzwanzig", "Số 21"),
            ("hundert", "Một trăm (100)"),
            ("tausend", "Một nghìn (1000)")
        ],
        "noi_o_sets": [
            [
                {"left": "Hallo!", "right": "Xin chào! (thân mật)"},
                {"left": "Auf Wiedersehen!", "right": "Hẹn gặp lại! (trang trọng)"},
                {"left": "Guten Morgen!", "right": "Chào buổi sáng!"},
                {"left": "Gute Nacht!", "right": "Chúc ngủ ngon!"}
            ],
            [
                {"left": "sechzehn", "right": "Số 16 (mười sáu)"},
                {"left": "siebzehn", "right": "Số 17 (mười bảy)"},
                {"left": "dreißig", "right": "Số 30 (ba mươi)"},
                {"left": "einundzwanzig", "right": "Số 21 (hai mươi mốt)"}
            ]
        ],
        "sentences_vd": [
            ("Xin chào! Tôi tên là Anna.", ["Hallo! Ich heiße Anna.", "Hallo, ich bin Anna.", "Hallo! Mein Name ist Anna."]),
            ("Tôi đến từ Việt Nam.", ["Ich komme aus Vietnam.", "Ich bin aus Vietnam."]),
            ("Tôi sống ở Hải Phòng.", ["Ich wohne in Hai Phong.", "Ich lebe in Hai Phong."]),
            ("Hẹn gặp lại ngày mai!", ["Bis morgen!", "Auf Wiedersehen bis morgen!"])
        ],
        "sentences_dv": [
            ("Guten Tag! Ich heiße Anna.", ["Xin chào tôi tên là Anna", "Chào bạn tôi là Anna", "Chào ngày mới tôi tên là Anna"]),
            ("Woher kommen Sie?", ["Ngài đến từ đâu", "Bạn đến từ đâu", "Bác đến từ đâu", "Ông đến từ đâu"]),
            ("Ich wohne in Hai Phong.", ["Tôi sống ở Hải Phòng", "Mình sống tại Hải Phòng", "Tôi cư trú ở Hải Phòng"]),
            ("Auf Wiedersehen!", ["Hẹn gặp lại", "Tạm biệt ngài", "Xin hẹn gặp lại"])
        ],
        "nghe_dien_items": [
            {
                "audio_text": "Guten Tag! Ich heiße Anna.",
                "display_sentence": "Guten Tag! Ich ___ Anna.",
                "hint_vi": "Xin chào! Tôi tên là Anna.",
                "accepted_answers": ["heiße", "heisse", "bin"]
            },
            {
                "audio_text": "Woher kommen Sie? Ich komme aus Vietnam.",
                "display_sentence": "Woher kommen Sie? Ich komme ___ Vietnam.",
                "hint_vi": "Ngài đến từ đâu? Tôi đến từ Việt Nam.",
                "accepted_answers": ["aus"]
            },
            {
                "audio_text": "Auf Wiedersehen! Bis morgen!",
                "display_sentence": "Auf Wiedersehen! Bis ___!",
                "hint_vi": "Hẹn gặp lại! Hẹn ngày mai nhé!",
                "accepted_answers": ["morgen"]
            }
        ],
        "dien_tao_cau_items": [
            {
                "question": "Điền vào 2 chỗ trống để tạo thành câu: 'Tôi tên là Anna. Tôi đến từ Việt Nam.'",
                "display_frame": "Ich ___ Anna. Ich komme ___ Vietnam.",
                "word_bank_hints": ["heiße", "aus", "wohne", "in", "bist"],
                "accepted_answers": ["heiße / aus", "heisse / aus", "bin / aus"],
                "explanation": "Động từ heißen đi với ngôi ich là 'heiße', giới từ chỉ xuất xứ là 'aus'."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # BÀI 1 (P2): Kaffee oder Tee? - Gọi đồ, Đại từ, Chia động từ, Euro
    # -------------------------------------------------------------------------
    2: {
        "vocab_pairs": [
            ("der Kaffee", "cà phê"),
            ("der Tee", "trà"),
            ("die Milch", "sữa"),
            ("der Zucker", "đường"),
            ("ohne Zucker", "không đường"),
            ("mit viel Milch", "với nhiều sữa"),
            ("zusammen oder getrennt", "thanh toán chung hay riêng"),
            ("zahlen", "thanh toán"),
            ("möchten", "muốn"),
            ("trinken", "uống"),
            ("nehmen", "lấy/dùng"),
            ("arbeiten", "làm việc")
        ],
        "noi_o_sets": [
            [
                {"left": "Kaffee mit Milch", "right": "Cà phê có sữa"},
                {"left": "Tee ohne Zucker", "right": "Trà không đường"},
                {"left": "zusammen bitte", "right": "Thanh toán chung, làm ơn"},
                {"left": "getrennt bitte", "right": "Thanh toán riêng, làm ơn"}
            ],
            [
                {"left": "ich trinke", "right": "tôi uống"},
                {"left": "du nimmst", "right": "bạn chọn món / lấy"},
                {"left": "er arbeitet", "right": "anh ấy làm việc"},
                {"left": "wir möchten", "right": "chúng tôi muốn"}
            ]
        ],
        "sentences_vd": [
            ("Tôi uống cà phê với nhiều sữa.", ["Ich trinke Kaffee mit viel Milch."]),
            ("Cho trà không đường, làm ơn.", ["Tee ohne Zucker, bitte.", "Einen Tee ohne Zucker bitte."]),
            ("Chúng tôi muốn thanh toán.", ["Wir möchten bitte zahlen.", "Wir möchten zahlen, bitte."]),
            ("Thanh toán chung hay riêng?", ["Zusammen oder getrennt?", "Zahlen wir zusammen oder getrennt?"])
        ],
        "sentences_dv": [
            ("Was möchten Sie trinken?", ["Quý khách muốn uống gì", "Ngài muốn uống gì", "Bạn muốn uống gì ạ", "Quý khách dùng đồ uống gì"]),
            ("Wir möchten bitte zahlen.", ["Chúng tôi muốn thanh toán", "Làm ơn tính tiền cho chúng tôi", "Cho chúng tôi trả tiền"]),
            ("Das macht drei Euro neunundneunzig.", ["Tổng cộng hết 3,99 Euro", "Hết 3 euro 99 cent", "Số tiền là 3,99 Euro"]),
            ("Marc arbeitet bei der Post.", ["Marc làm việc tại bưu điện", "Marc làm việc ở bưu điện"])
        ],
        "nghe_dien_items": [
            {
                "audio_text": "Was möchten Sie trinken?",
                "display_sentence": "Was ___ Sie trinken?",
                "hint_vi": "Quý khách muốn uống gì ạ?",
                "accepted_answers": ["möchten", "moechten"]
            },
            {
                "audio_text": "Ich trinke Kaffee mit viel Milch.",
                "display_sentence": "Ich trinke Kaffee ___ viel Milch.",
                "hint_vi": "Tôi uống cà phê với nhiều sữa.",
                "accepted_answers": ["mit"]
            },
            {
                "audio_text": "Zusammen oder getrennt?",
                "display_sentence": "Zusammen ___ getrennt?",
                "hint_vi": "Thanh toán chung hay riêng ạ?",
                "accepted_answers": ["oder"]
            }
        ],
        "dien_tao_cau_items": [
            {
                "question": "Điền vào 2 chỗ trống để tạo thành câu gọi món: 'Chúng tôi muốn gọi trà.'",
                "display_frame": "Wir ___ bitte einen ___.",
                "word_bank_hints": ["möchten", "Tee", "trinken", "Kaffee", "zahle"],
                "accepted_answers": ["möchten / Tee", "moechten / Tee", "nehmen / Tee"],
                "explanation": "Wir möchten + tân ngữ Tee."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # BÀI 2: Sprache im Kurs - Đồ dùng, Giống der/die/das, Mạo từ, können
    # -------------------------------------------------------------------------
    3: {
        "vocab_pairs": [
            ("der Tisch", "cái bàn"),
            ("der Stuhl", "cái ghế"),
            ("der Kuli", "cây bút bi"),
            ("das Buch", "quyển sách"),
            ("das Wörterbuch", "cuốn từ điển"),
            ("das Handy", "điện thoại di động"),
            ("das Heft", "quyển vở"),
            ("die Brille", "kính mắt"),
            ("die Tafel", "cái bảng viết"),
            ("die Landkarte", "tấm bản đồ"),
            ("die Tasche", "cái túi xách"),
            ("wiederholen", "nhắc lại"),
            ("buchstabieren", "đánh vần"),
            ("verstehen", "hiểu")
        ],
        "noi_o_sets": [
            [
                {"left": "der Tisch", "right": "cái bàn (giống đực)"},
                {"left": "die Brille", "right": "kính mắt (giống cái)"},
                {"left": "das Buch", "right": "quyển sách (giống trung)"},
                {"left": "die Tafel", "right": "bảng viết (giống cái)"}
            ],
            [
                {"left": "ein Kuli", "right": "một chiếc bút bi"},
                {"left": "eine Brille", "right": "một chiếc kính mắt"},
                {"left": "kein Tisch", "right": "không phải cái bàn"},
                {"left": "keine Landkarte", "right": "không phải tấm bản đồ"}
            ]
        ],
        "sentences_vd": [
            ("Cái này tiếng Đức gọi là gì?", ["Wie heißt das auf Deutsch?", "Wie heisst das auf Deutsch?"]),
            ("Tôi không hiểu điều đó.", ["Das verstehe ich nicht.", "Ich verstehe das nicht."]),
            ("Ngài có thể vui lòng nhắc lại được không?", ["Können Sie das bitte wiederholen?", "Koennen Sie das bitte wiederholen?"]),
            ("Đó không phải cái bàn, đó là cái ghế.", ["Das ist kein Tisch, das ist ein Stuhl.", "Das ist kein Tisch, sondern ein Stuhl."])
        ],
        "sentences_dv": [
            ("Wie heißt das auf Deutsch?", ["Cái này tiếng Đức gọi là gì", "Từ này tiếng Đức là gì", "Cái đó gọi là gì bằng tiếng Đức"]),
            ("Das verstehe ich nicht.", ["Tôi không hiểu điều đó", "Tôi không hiểu", "Điều này tôi không hiểu"]),
            ("Können Sie das bitte buchstabieren?", ["Ngài có thể đánh vần từ đó được không", "Bạn làm ơn đánh vần từ này được không", "Ngài vui lòng đánh vần giúp tôi"]),
            ("Nein, das ist keine Brille. Das ist eine Landkarte.", ["Không, đó không phải kính mắt. Đó là bản đồ", "Không đây không phải chiếc kính mà là tấm bản đồ"])
        ],
        "nghe_dien_items": [
            {
                "audio_text": "Wie heißt das auf Deutsch?",
                "display_sentence": "Wie ___ das auf Deutsch?",
                "hint_vi": "Cái này tiếng Đức gọi là gì?",
                "accepted_answers": ["heißt", "heisst"]
            },
            {
                "audio_text": "Können Sie das bitte wiederholen?",
                "display_sentence": "Können Sie das bitte ___?",
                "hint_vi": "Ngài có thể vui lòng nhắc lại được không?",
                "accepted_answers": ["wiederholen"]
            },
            {
                "audio_text": "Das ist kein Tisch, das ist ein Stuhl.",
                "display_sentence": "Das ist ___ Tisch, das ist ein Stuhl.",
                "hint_vi": "Đó không phải cái bàn, đó là một cái ghế.",
                "accepted_answers": ["kein"]
            }
        ],
        "dien_tao_cau_items": [
            {
                "question": "Điền vào 2 chỗ trống để tạo câu hỏi: 'Ngài có thể đánh vần giúp tôi được không?'",
                "display_frame": "___ Sie das bitte ___?",
                "word_bank_hints": ["Können", "buchstabieren", "wiederholen", "sprechen", "kann"],
                "accepted_answers": ["Können / buchstabieren", "Koennen / buchstabieren"],
                "explanation": "Động từ khuyết thiếu Können đứng đầu câu hỏi Ja/Nein, buchstabieren nguyên mẫu ở cuối."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # BÀI 3: Địa danh, Phương hướng, Präteritum (war/waren)
    # -------------------------------------------------------------------------
    4: {
        "vocab_pairs": [
            ("der Norden", "phía Bắc"),
            ("der Süden", "phía Nam"),
            ("der Osten", "phía Đông"),
            ("der Westen", "phía Tây"),
            ("im Norden von", "ở phía Bắc của"),
            ("in der Mitte von", "ở miền Trung của"),
            ("nördlich von", "nằm về phía Bắc của (tính từ)"),
            ("die Schweiz", "Thụy Sỹ (giống cái)"),
            ("die Türkei", "Thổ Nhĩ Kỳ (giống cái)"),
            ("die USA", "nước Mỹ (số nhiều)"),
            ("aus der Schweiz", "đến từ Thụy Sỹ"),
            ("in den USA", "ở nước Mỹ"),
            ("ich war", "tôi đã ở"),
            ("wir waren", "chúng tôi đã ở"),
            ("der Eiffelturm", "Tháp Eiffel (Paris)"),
            ("das Brandenburger Tor", "Cổng thành Brandenburger (Berlin)")
        ],
        "noi_o_sets": [
            [
                {"left": "der Eiffelturm", "right": "Paris (Frankreich)"},
                {"left": "das Brandenburger Tor", "right": "Berlin (Deutschland)"},
                {"left": "die Akropolis", "right": "Athen (Griechenland)"},
                {"left": "der Prater", "right": "Wien (Österreich)"}
            ],
            [
                {"left": "Hanoi", "right": "im Norden von Vietnam"},
                {"left": "Da Nang", "right": "in der Mitte von Vietnam"},
                {"left": "Hai Phong", "right": "im Nordosten von Vietnam"},
                {"left": "Long An", "right": "im Süden von Vietnam"}
            ]
        ],
        "sentences_vd": [
            ("Hà Nội nằm ở miền Bắc của Việt Nam.", ["Hanoi liegt im Norden von Vietnam.", "Hanoi liegt noerdlich von Vietnam."]),
            ("Đà Nẵng nằm ở miền Trung của Việt Nam.", ["Da Nang liegt in der Mitte von Vietnam."]),
            ("Hôm qua Paula và tôi đã ở Hải Phòng.", ["Gestern waren Paula und ich in Haiphong.", "Gestern waren wir in Haiphong."]),
            ("Ở Thụy Sỹ người ta nói tiếng Đức.", ["In der Schweiz spricht man Deutsch."])
        ],
        "sentences_dv": [
            ("Hai Phong liegt im Nordosten von Vietnam.", ["Hải Phòng nằm ở phía Đông Bắc của Việt Nam", "Hải Phòng ở miền Đông Bắc Việt Nam"]),
            ("Warst du schon in Athen?", ["Bạn đã từng đến Athens chưa", "Cậu đã đi Athens bao giờ chưa", "Bạn từng ở Athens chưa"]),
            ("Gestern waren wir in Haiphong. Es war super!", ["Hôm qua chúng tôi đã ở Hải Phòng, chuyến đi thật tuyệt vời", "Hôm qua chúng mình ở Hải Phòng rất tuyệt"]),
            ("Meine Tante kommt aus der Schweiz.", ["Bác của tôi đến từ Thụy Sỹ", "Cô của tôi đến từ Thụy Sĩ", "Dì tôi đến từ Thụy Sĩ"])
        ],
        "nghe_dien_items": [
            {
                "audio_text": "Hanoi liegt im Norden von Vietnam.",
                "display_sentence": "Hanoi liegt ___ Norden von Vietnam.",
                "hint_vi": "Hà Nội nằm ở phía Bắc của Việt Nam.",
                "accepted_answers": ["im", "in dem"]
            },
            {
                "audio_text": "Gestern waren Paula und ich in Haiphong.",
                "display_sentence": "Gestern ___ Paula und ich in Haiphong.",
                "hint_vi": "Hôm qua Paula và tôi đã ở Hải Phòng.",
                "accepted_answers": ["waren"]
            },
            {
                "audio_text": "Meine Tante kommt aus der Schweiz.",
                "display_sentence": "Meine Tante kommt aus ___ Schweiz.",
                "hint_vi": "Bác của tôi đến từ Thụy Sỹ.",
                "accepted_answers": ["der"]
            }
        ],
        "dien_tao_cau_items": [
            {
                "question": "Điền vào 2 chỗ trống để tạo câu miêu tả: 'Đà Nẵng nằm ở miền Trung Việt Nam.'",
                "display_frame": "Da Nang ___ in der ___ von Vietnam.",
                "word_bank_hints": ["liegt", "Mitte", "Norden", "waren", "ist"],
                "accepted_answers": ["liegt / Mitte"],
                "explanation": "Cấu trúc: liegt in der Mitte von Vietnam."
            }
        ]
    },

    # -------------------------------------------------------------------------
    # BÀI 4: Nhà ở, Nominativ vs Akkusativ, Mạo từ sở hữu
    # -------------------------------------------------------------------------
    5: {
        "vocab_pairs": [
            ("das Wohnzimmer", "phòng khách"),
            ("das Schlafzimmer", "phòng ngủ"),
            ("die Küche", "phòng bếp"),
            ("das Badezimmer", "phòng tắm"),
            ("das Arbeitszimmer", "phòng làm việc"),
            ("der Garten", "khu vườn"),
            ("der Balkon", "ban công"),
            ("der Flur", "hành lang"),
            ("der Keller", "tầng hầm"),
            ("der Fernseher", "chiếc tivi"),
            ("der Schrank", "cái tủ"),
            ("der Kühlschrank", "tủ lạnh"),
            ("hell", "sáng sủa"),
            ("dunkel", "tối tăm"),
            ("groß", "rộng lớn"),
            ("klein", "nhỏ bé"),
            ("einen Garten", "một khu vườn (Akkusativ)"),
            ("einen Fernseher", "một chiếc TV (Akkusativ)")
        ],
        "noi_o_sets": [
            [
                {"left": "das Wohnzimmer", "right": "Phòng khách (hell và modern)"},
                {"left": "die Küche", "right": "Phòng bếp (klein và schön)"},
                {"left": "das Arbeitszimmer", "right": "Phòng làm việc (mit Tisch und Stuhl)"},
                {"left": "der Garten", "right": "Khu vườn (sehr schön)"}
            ],
            [
                {"left": "haben + der Garten", "right": "einen Garten (Akkusativ đực)"},
                {"left": "haben + das Haus", "right": "ein Haus (giống trung giữ nguyên)"},
                {"left": "haben + die Küche", "right": "eine Küche (giống cái giữ nguyên)"},
                {"left": "finden + der Schrank", "right": "den Schrank (Akkusativ xác định)"}
            ],
            [
                {"left": "hell (sáng sủa)", "right": "dunkel (tối tăm)"},
                {"left": "groß (rộng lớn)", "right": "klein (nhỏ bé)"},
                {"left": "teuer (đắt đỏ)", "right": "billig (rẻ)"},
                {"left": "alt (cũ/cổ kính)", "right": "neu / modern (mới/hiện đại)"}
            ]
        ],
        "sentences_vd": [
            ("Chúng tôi có một khu vườn.", ["Wir haben einen Garten."]),
            ("Ngôi nhà có một hành lang.", ["Das Haus hat einen Flur."]),
            ("Tôi thấy khu vườn rất đẹp.", ["Ich finde den Garten sehr schön.", "Ich finde den Garten schoen."]),
            ("Phòng khách của tôi sáng và hiện đại.", ["Mein Wohnzimmer ist hell und modern."]),
            ("Đó có phải là con của các bạn không, Maria và Lukas?", ["Sind das eure Kinder, Maria und Lukas?"])
        ],
        "sentences_dv": [
            ("Das Haus hat einen Flur. Er ist lang und dunkel.", ["Ngôi nhà có một hành lang. Nó dài và tối", "Nhà có hành lang dài và tối tăm"]),
            ("Wir haben auch einen Garten. Ich finde den Garten sehr schön.", ["Chúng tôi cũng có một khu vườn. Tôi thấy khu vườn rất đẹp", "Chúng mình cũng có vườn, mình thấy vườn rất đẹp"]),
            ("Mein Arbeitszimmer ist klein, aber hell.", ["Phòng làm việc của tôi nhỏ nhưng sáng sủa", "Phòng làm việc của mình nhỏ mà sáng"]),
            ("Sind das eure Kinder, Maria und Lukas?", ["Đó có phải con của các bạn không Maria và Lukas", "Đây có phải là con các bạn không Maria và Lukas"])
        ],
        "nghe_dien_items": [
            {
                "audio_text": "Wir haben einen Garten.",
                "display_sentence": "Wir haben ___ Garten.",
                "hint_vi": "Chúng tôi có một khu vườn (der Garten ở Akkusativ).",
                "accepted_answers": ["einen"]
            },
            {
                "audio_text": "Ich finde den Garten sehr schön.",
                "display_sentence": "Ich finde ___ Garten sehr schön.",
                "hint_vi": "Tôi thấy khu vườn rất đẹp.",
                "accepted_answers": ["den"]
            },
            {
                "audio_text": "Sind das eure Kinder, Maria und Lukas?",
                "display_sentence": "Sind das ___ Kinder, Maria und Lukas?",
                "hint_vi": "Đó có phải con của các bạn không, Maria và Lukas?",
                "accepted_answers": ["eure"]
            }
        ],
        "dien_tao_cau_items": [
            {
                "question": "Điền vào 2 chỗ trống để tạo câu: 'Ngôi nhà có một ban công và một khu vườn.'",
                "display_frame": "Das Haus hat einen ___ und einen ___.",
                "word_bank_hints": ["Balkon", "Garten", "Küche", "Zimmer", "Haus"],
                "accepted_answers": ["Balkon / Garten", "Garten / Balkon"],
                "explanation": "Cả der Balkon và der Garten đều là giống đực, đi sau hat (Akkusativ) thành einen Balkon und einen Garten."
            }
        ]
    }
}


def build_arena_questions_for_user(user_id, count=70):
    """
    Sinh danh sách câu hỏi Đấu trường kết hợp 50% từ database exercises
    và 50% từ bộ sinh Procedural, bao phủ ĐỦ 9 DẠNG BÀI TẬP.
    """
    allowed_lids = get_user_allowed_lessons(user_id)
    allowed_orders = [LESSON_ORDER_MAP[lid][1] for lid in allowed_lids if lid in LESSON_ORDER_MAP]

    questions = []

    # 1. NGUỒN DATABASE EXERCISES (Chuyển đổi bài tập hiện có)
    conn = get_connection()
    cursor = conn.cursor()
    placeholders = ",".join("?" for _ in allowed_lids)
    cursor.execute(f"""
        SELECT id, lesson_id, exercise_type, question, correct_answer, explanation, extra_data, options_json
        FROM exercises
        WHERE lesson_id IN ({placeholders})
        ORDER BY RANDOM()
        LIMIT 45;
    """, allowed_lids)
    db_rows = cursor.fetchall()
    conn.close()

    for r in db_rows:
        lid = r["lesson_id"]
        order = LESSON_ORDER_MAP.get(lid, ("A1", 1))[1]
        extra = {}
        try:
            extra = json.loads(r["extra_data"]) if r["extra_data"] else {}
        except:
            extra = {}

        q_text = r["question"]
        correct_ans = r["correct_answer"]
        explanation = r["explanation"]
        trans = extra.get("translation", "")

        # Map exercise_type sang 9 dạng Đấu trường
        mapped_type = "trac_nghiem"
        raw_type = r["exercise_type"]
        opts = []
        if r["options_json"]:
            try:
                opts = json.loads(r["options_json"])
            except:
                opts = []

        if opts and len(opts) > 1:
            mapped_type = "trac_nghiem"
        elif raw_type == "dien_khuyet":
            mapped_type = "dien_khuyet"
        elif raw_type == "nghe":
            mapped_type = "nghe_dien"
        elif raw_type == "dich":
            # Phân biệt dịch Việt -> Đức hay Đức -> Việt
            if "Việt" in q_text or "sang tiếng Đức" in q_text:
                mapped_type = "dich_cau_vd"
            else:
                mapped_type = "dich_cau_dv"
        elif raw_type == "sap_xep":
            mapped_type = "dien_tao_cau"
        else:
            mapped_type = "dien_khuyet"

        pts = TYPE_POINTS[mapped_type]

        item = {
            "type": mapped_type,
            "type_label": pts["label"],
            "points_correct": pts["correct"],
            "points_wrong": pts["wrong"],
            "question": q_text,
            "correct_answer": correct_ans,
            "accepted_answers": [correct_ans],
            "explanation": explanation,
            "translation": trans
        }

        if mapped_type == "trac_nghiem":
            item["options"] = opts
        elif mapped_type == "nghe_dien":
            item["audio_text"] = extra.get("audio_text", correct_ans)
            item["display_sentence"] = q_text
            item["hint_vi"] = trans
        elif mapped_type == "dien_tao_cau":
            item["display_frame"] = q_text
            item["word_bank_hints"] = [w.strip() for w in correct_ans.replace(",", " ").split() if len(w.strip()) > 1][:5]

        questions.append(item)

    # 2. NGUỒN PROCEDURAL ĐA DẠNG HÓA 9 DẠNG BÀI
    for order in allowed_orders:
        data = ARENA_DATA_BY_LESSON.get(order)
        if not data:
            continue

        # 2.1. Dạng 3: dich_nghia_vd (Việt -> Đức)
        for de_w, vi_w in data.get("vocab_pairs", [])[:4]:
            pts = TYPE_POINTS["dich_nghia_vd"]
            # Tạo các biến thể chấp nhận được (có hoặc không có mạo từ)
            alts = [de_w]
            parts = de_w.split()
            if len(parts) == 2 and parts[0] in ["der", "die", "das", "ein", "eine"]:
                alts.append(parts[1])  # Chỉ gõ danh từ
                indef = "eine" if parts[0] == "die" else "ein"
                alts.append(f"{indef} {parts[1]}")

            questions.append({
                "type": "dich_nghia_vd",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": f"Dịch từ/cụm từ tiếng Việt sau sang tiếng Đức: „{vi_w}“",
                "prompt_vi": vi_w,
                "correct_answer": de_w,
                "accepted_answers": alts,
                "explanation": f"„{vi_w}“ trong tiếng Đức là '{de_w}'.",
                "translation": f"{de_w} = {vi_w}"
            })

        # 2.2. Dạng 4: dich_nghia_dv (Đức -> Việt)
        for de_w, vi_w in data.get("vocab_pairs", [])[2:6]:
            pts = TYPE_POINTS["dich_nghia_dv"]
            questions.append({
                "type": "dich_nghia_dv",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": f"Dịch từ/cụm từ tiếng Đức sau sang tiếng Việt: „{de_w}“",
                "prompt_de": de_w,
                "correct_answer": vi_w,
                "accepted_answers": [vi_w, vi_w.replace("!", ""), vi_w.lower()],
                "explanation": f"'{de_w}' có nghĩa tiếng Việt là: {vi_w}.",
                "translation": f"{de_w} = {vi_w}"
            })

        # 2.3. Dạng 5: noi_o (Nối 4 cặp)
        for pair_set in data.get("noi_o_sets", []):
            pts = TYPE_POINTS["noi_o"]
            # Xáo trộn cột phải
            left_items = [p["left"] for p in pair_set]
            right_items = [p["right"] for p in pair_set]
            shuffled_right = list(right_items)
            random.shuffle(shuffled_right)

            questions.append({
                "type": "noi_o",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": "Nối 4 cặp từ tương ứng ở cột trái và cột phải (Đúng cả 4 cặp: +10đ | Sai ≥1 cặp: -4đ):",
                "pairs": pair_set,
                "left_items": left_items,
                "right_items": shuffled_right,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "Kiểm tra kỹ các cặp nghĩa tương ứng giữa hai cột.",
                "translation": "Nối cặp từ vựng & ý nghĩa tương ứng"
            })

        # 2.4. Dạng 6: dich_cau_vd (Câu Việt -> Đức)
        for vi_s, de_alts in data.get("sentences_vd", []):
            pts = TYPE_POINTS["dich_cau_vd"]
            questions.append({
                "type": "dich_cau_vd",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": f"Dịch câu hoàn chỉnh sau sang tiếng Đức: „{vi_s}“",
                "prompt_vi": vi_s,
                "correct_answer": de_alts[0],
                "accepted_answers": de_alts,
                "explanation": f"Câu tiếng Đức chuẩn: '{de_alts[0]}'",
                "translation": vi_s
            })

        # 2.5. Dạng 7: dich_cau_dv (Câu Đức -> Việt)
        for de_s, vi_alts in data.get("sentences_dv", []):
            pts = TYPE_POINTS["dich_cau_dv"]
            questions.append({
                "type": "dich_cau_dv",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": f"Dịch câu tiếng Đức sau sang tiếng Việt: „{de_s}“",
                "prompt_de": de_s,
                "correct_answer": vi_alts[0],
                "accepted_answers": vi_alts,
                "explanation": f"Nghĩa tiếng Việt chuẩn: '{vi_alts[0]}'",
                "translation": f"Bản dịch: {vi_alts[0]}"
            })

        # 2.6. Dạng 8: nghe_dien
        for item in data.get("nghe_dien_items", []):
            pts = TYPE_POINTS["nghe_dien"]
            questions.append({
                "type": "nghe_dien",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": "Bấm nút nghe phát âm và điền từ còn thiếu vào chỗ trống:",
                "audio_text": item["audio_text"],
                "display_sentence": item["display_sentence"],
                "hint_vi": item["hint_vi"],
                "correct_answer": item["accepted_answers"][0],
                "accepted_answers": item["accepted_answers"],
                "explanation": f"Từ còn thiếu là: '{item['accepted_answers'][0]}'.",
                "translation": item["hint_vi"]
            })

        # 2.7. Dạng 9: dien_tao_cau
        for item in data.get("dien_tao_cau_items", []):
            pts = TYPE_POINTS["dien_tao_cau"]
            questions.append({
                "type": "dien_tao_cau",
                "type_label": pts["label"],
                "points_correct": pts["correct"],
                "points_wrong": pts["wrong"],
                "question": item["question"],
                "display_frame": item["display_frame"],
                "word_bank_hints": item["word_bank_hints"],
                "correct_answer": item["accepted_answers"][0],
                "accepted_answers": item["accepted_answers"],
                "explanation": item["explanation"],
                "translation": "Hoàn thiện câu chuẩn ngữ pháp tiếng Đức"
            })

    # Xáo trộn toàn bộ câu hỏi
    random.shuffle(questions)
    return questions[:count]
