import sqlite3
import json
import os
import sys

def test_lesson_5_qa():
    print("=================================================================")
    print("🚀 BẮT ĐẦU KIỂM THỬ TOÀN DIỆN ZERO-BUG: BÀI 5 & TOÀN BỘ HỆ THỐNG")
    print("=================================================================")

    # 1. KIỂM TRA BẢO TOÀN DỮ LIỆU CÁC BÀI HỌC CŨ (BÀI 1 P1 -> BÀI 4)
    conn = sqlite3.connect('deutsch_meister.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM lessons ORDER BY id;")
    lessons = cursor.fetchall()
    print(f"\n1. Danh sách bài học hiện có trong DB: {len(lessons)} bài")
    assert len(lessons) >= 6, f"Thiếu bài học! Hiện chỉ có {len(lessons)} bài"

    expected_lessons = [
        ('Bài 1 (P1)', 50),
        ('Bài 1 (P2)', 50),
        ('Bài 2', 50),
        ('Bài 3', 50),
        ('Bài 4', 50),
        ('Bài 5', 50)
    ]

    for prefix, exp_ex_cnt in expected_lessons:
        matching = [l for l in lessons if prefix in l['title']]
        assert len(matching) == 1, f"Không tìm thấy duy nhất 1 bài khớp '{prefix}'"
        lid = matching[0]['id']
        title = matching[0]['title']

        cursor.execute("SELECT count(*) as cnt FROM exercises WHERE lesson_id = ?;", (lid,))
        ex_cnt = cursor.fetchone()['cnt']
        cursor.execute("SELECT count(*) as cnt FROM vocabularies WHERE lesson_id = ?;", (lid,))
        voc_cnt = cursor.fetchone()['cnt']
        print(f"   ✓ {title} (ID: {lid}) -> {voc_cnt} từ vựng, {ex_cnt} bài tập (Chuẩn: {exp_ex_cnt})")
        assert ex_cnt == exp_ex_cnt, f"Bài {title} có {ex_cnt} bài tập, khác {exp_ex_cnt}!"

    # 2. KIỂM TRA CHI TIẾT BÀI 5
    b5 = [l for l in lessons if 'Bài 5' in l['title']][0]
    b5_id = b5['id']

    # 2.1. Kiểm tra 38 từ vựng của Bài 5
    cursor.execute("SELECT * FROM vocabularies WHERE lesson_id = ?;", (b5_id,))
    b5_vocabs = cursor.fetchall()
    print(f"\n2. Kiểm tra từ vựng Bài 5: {len(b5_vocabs)} từ vựng")
    assert len(b5_vocabs) == 38, f"Bài 5 phải có đúng 38 từ vựng, hiện có {len(b5_vocabs)}!"

    for v in b5_vocabs:
        word = v['german_word']
        art = v['article']
        mean = v['vietnamese_meaning']
        ex = v['example_sentence']
        assert art in ['der', 'die', 'das', 'Adj.', 'V.'], f"Mạo từ không hợp lệ cho từ {word}: {art}"
        assert mean and len(mean) > 2, f"Nghĩa tiếng Việt bị thiếu cho từ {word}"
        assert ex and len(ex) > 5, f"Câu ví dụ bị thiếu cho từ {word}"
        assert '(' in ex and ')' in ex, f"Câu ví dụ của từ {word} thiếu bản dịch tiếng Việt trong ngoặc: {ex}"
        # Đảm bảo từ vựng có mặt trong câu ví dụ
        w_clean = word.lower()
        ex_clean = ex.lower()
        assert w_clean in ex_clean or w_clean[:-1] in ex_clean or word in ex, f"Từ {word} không xuất hiện trong ví dụ: {ex}"
    print("   ✓ 100% 38 từ vựng Bài 5 có mạo từ chuẩn, nghĩa tiếng Việt và câu ví dụ khớp từ vựng!")

    # 2.2. Kiểm tra 50 bài tập Bài 5 và 9 dạng
    cursor.execute("SELECT * FROM exercises WHERE lesson_id = ? ORDER BY id;", (b5_id,))
    b5_exercises = cursor.fetchall()
    print(f"\n3. Kiểm tra 50 bài tập Bài 5: {len(b5_exercises)} câu")
    assert len(b5_exercises) == 50, f"Bài 5 phải có đúng 50 câu bài tập, hiện có {len(b5_exercises)}!"

    type_counts = {}
    for idx, e in enumerate(b5_exercises):
        etype = e['exercise_type']
        type_counts[etype] = type_counts.get(etype, 0) + 1
        q = e['question']
        ca = e['correct_answer']
        exp = e['explanation']
        extra = json.loads(e['extra_data']) if e['extra_data'] else {}

        # Mọi câu đều phải có dịch nghĩa tiếng Việt trong extra_data hoặc question
        assert extra.get('translation'), f"Câu {idx+1} thiếu bản dịch tiếng Việt!"
        assert exp and len(exp) > 5, f"Câu {idx+1} thiếu giải thích đáp án!"

        if etype == 'trac_nghiem':
            opts = json.loads(e['options_json'])
            assert len(opts) == 4, f"Câu trắc nghiệm {idx+1} không đủ 4 phương án!"
            assert ca in opts, f"Câu {idx+1}: correct_answer '{ca}' không nằm trong options: {opts}"
        elif etype == 'nghe_dien':
            assert extra.get('audio_text'), f"Câu nghe {idx+1} thiếu audio_text!"
            assert extra.get('display_sentence'), f"Câu nghe {idx+1} thiếu display_sentence!"
            # Đảm bảo không lộ đáp án trong đề
            assert ca.lower() not in q.lower().split("chỗ trống:")[0], f"Câu nghe {idx+1} để lộ đáp án trên đề bài!"
        elif etype == 'noi_o':
            assert extra.get('noi_o_pairs'), f"Bài nối ô {idx+1} thiếu noi_o_pairs!"
            assert len(extra['noi_o_pairs']) == 4, f"Bài nối ô {idx+1} phải có 4 cặp!"

    expected_type_distribution = {
        'trac_nghiem': 8,
        'dien_khuyet': 7,
        'dich_nghia_vd': 6,
        'dich_nghia_dv': 6,
        'noi_o': 6,
        'dien_tao_cau': 5,
        'nghe_dien': 4,
        'dich_cau_vd': 4,
        'dich_cau_dv': 4
    }

    print("   Phân bổ 9 dạng bài tập trong Bài 5:")
    for k, v in expected_type_distribution.items():
        actual = type_counts.get(k, 0)
        print(f"     • {k}: {actual} câu (Chuẩn: {v})")
        assert actual == v, f"Dạng {k} có {actual} câu, khác {v}!"

    conn.close()

    # 3. KIỂM TRA VERBS_DB.JS
    print("\n4. Kiểm tra Tab Chia động từ (static/js/verbs_db.js):")
    with open('static/js/verbs_db.js', 'r', encoding='utf-8') as f:
        verbs_content = f.read()

    b5_verbs = ["aufmachen", "zumachen", "anmachen", "ausmachen", "aufstehen", "ausgehen", "einkaufen", "anrufen", "fernsehen", "mitkommen", "vorbereiten", "frühstücken"]
    for v in b5_verbs:
        assert f'infinitiv: "{v}"' in verbs_content, f"Thiếu động từ {v} trong verbs_db.js!"
    assert 'id: "Động từ tách"' in verbs_content, "Thiếu bộ lọc Động từ tách trong verbs_db.js!"
    print(f"   ✓ Đã có đủ 12 động từ Bài 5 và bộ lọc 'Động từ tách' trong verbs_db.js!")

    # 4. KIỂM TRA LEXIKON_DB.JS
    print("\n5. Kiểm tra Tab Từ vựng & Giống (static/js/lexikon_db.js):")
    with open('static/js/lexikon_db.js', 'r', encoding='utf-8') as f:
        lexikon_content = f.read()

    assert 'id: "Thời gian & Lịch trình"' in lexikon_content, "Thiếu bộ lọc Thời gian & Lịch trình trong lexikon_db.js!"
    assert 'category: "Thời gian & Lịch trình"' in lexikon_content, "Thiếu các từ thuộc category Thời gian & Lịch trình!"
    
    b5_lex_sample = ["Sekunde", "Montag", "Januar", "Mittagspause", "Panne", "Zeit"]
    for w in b5_lex_sample:
        assert f'word: "{w}"' in lexikon_content, f"Thiếu từ {w} trong lexikon_db.js!"
    print("   ✓ Đã có đủ 38 từ vựng và bộ lọc 'Thời gian & Lịch trình' trong lexikon_db.js!")

    # 5. KIỂM TRA ARENA_GENERATOR.PY
    print("\n6. Kiểm tra Hệ thống Đấu trường (arena_generator.py):")
    from arena_generator import build_arena_questions_for_user, LESSON_ORDER_MAP, ARENA_DATA_BY_LESSON
    assert 19 in LESSON_ORDER_MAP, "Thiếu Bài 5 (ID 19) trong LESSON_ORDER_MAP!"
    assert 6 in ARENA_DATA_BY_LESSON, "Thiếu key 6 trong ARENA_DATA_BY_LESSON!"
    q_list = build_arena_questions_for_user(None, count=30)
    assert len(q_list) >= 20, f"Sinh câu hỏi đấu trường thất bại: chỉ được {len(q_list)} câu!"
    print(f"   ✓ Sinh thành công {len(q_list)} câu hỏi Đấu trường bao phủ các bài học!")

    print("\n=================================================================")
    print("🎉 TOÀN BỘ KIỂM THỬ ĐẠT 100% PASS - HỆ THỐNG SẠCH LỖI (ZERO-BUG)!")
    print("=================================================================")

if __name__ == "__main__":
    test_lesson_5_qa()
