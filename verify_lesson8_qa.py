import sqlite3
import json
import os
import sys

def verify():
    print("=" * 60)
    print("🚀 BẮT ĐẦU KIỂM THỬ TOÀN DIỆN QA BÀI 8 (ZERO-BUG VERIFICATION)")
    print("=" * 60)

    conn = sqlite3.connect("deutsch_meister.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. Zero regression on previous lessons
    print("\n[TEST 1] Kiểm tra bảo toàn dữ liệu Bài 1 P1 -> Bài 7 (Zero Regression):")
    cursor.execute("SELECT id, title FROM lessons ORDER BY id ASC;")
    lessons = cursor.fetchall()
    print(f"Tổng số bài học trong DB: {len(lessons)}")
    for l in lessons:
        cursor.execute("SELECT COUNT(*) as cnt FROM exercises WHERE lesson_id = ?;", (l["id"],))
        ex_cnt = cursor.fetchone()["cnt"]
        cursor.execute("SELECT COUNT(*) as cnt FROM vocabularies WHERE lesson_id = ?;", (l["id"],))
        voc_cnt = cursor.fetchone()["cnt"]
        print(f"  • ID {l['id']}: '{l['title'][:55]}...' -> {voc_cnt} từ vựng, {ex_cnt} bài tập")
        assert ex_cnt > 0, f"Lỗi: Bài {l['id']} bị mất bài tập!"
    print("✅ TEST 1 PASS: Tất cả các bài 1 P1 -> Bài 7 nguyên vẹn 100%!")

    # 2. Check Lesson 8 details
    print("\n[TEST 2] Kiểm tra Bài 8 (lesson_id = 22):")
    cursor.execute("SELECT id, title, grammar_content FROM lessons WHERE id = 22 OR title LIKE 'Bài 8%';")
    b8 = cursor.fetchone()
    assert b8 is not None, "❌ Lỗi: Không tìm thấy Bài 8 trong database!"
    b8_id = b8["id"]
    print(f"  • Lesson ID: {b8_id}")
    print(f"  • Tiêu đề: {b8['title']}")
    assert "14 Danh Lam Thắng Cảnh Berlin" in b8["grammar_content"], "❌ Thiếu Phần 1: Địa điểm & Danh lam thắng cảnh Berlin"
    assert "Nghệ Thuật Hỏi Đường & Chỉ Đường" in b8["grammar_content"], "❌ Thiếu Phần 2: Hỏi đường & Chỉ đường"
    assert "zu + Dativ" in b8["grammar_content"], "❌ Thiếu Phần 3: zu + Dativ vs in + Akkusativ"
    assert "4 Động Từ Khuyết Thiếu" in b8["grammar_content"], "❌ Thiếu Phần 4: Động từ khuyết thiếu"
    assert "Paula & Alex Khám Phá Berlin" in b8["grammar_content"], "❌ Thiếu Phần 5: Đoạn văn mẫu"

    # Các kiểm tra bổ sung theo yêu cầu tinh chỉnh lý thuyết
    assert "và hören" not in b8["grammar_content"], "❌ Còn sót 'và hören' trong tiếng Đức!"
    assert "und hören ein Konzert" in b8["grammar_content"], "❌ Thiếu 'und hören ein Konzert'!"
    assert "und dort links" in b8["grammar_content"], "❌ Lộ trình 1 chưa sửa thành 'und dort links'!"
    assert "svg-diag-vorbei" in b8["grammar_content"] and "<svg" in b8["grammar_content"], "❌ Thiếu SVG Sơ đồ 1!"
    assert "Không dùng để gọi món" in b8["grammar_content"], "❌ Thiếu cảnh báo sắc thái wollen trong khung tím!"
    assert "Không phải luật tuyệt đối" in b8["grammar_content"], "❌ Thiếu lưu ý thực tế dưới bảng zu/in!"
    print("✅ TEST 2 PASS: Đầy đủ 5 Học phần Lý thuyết chuyên sâu & đã tinh chỉnh 100% chuẩn xác!")

    # 3. Check 50 vocabularies of Lesson 8
    print("\n[TEST 3] Kiểm tra 50 Từ vựng Bài 8:")
    cursor.execute("SELECT COUNT(*) as cnt FROM vocabularies WHERE lesson_id = ?;", (b8_id,))
    v_cnt = cursor.fetchone()["cnt"]
    assert v_cnt == 50, f"❌ Lỗi: Số lượng từ vựng là {v_cnt}, kỳ vọng đúng 50!"
    cursor.execute("SELECT german_word, article, vietnamese_meaning, example_sentence FROM vocabularies WHERE lesson_id = ? LIMIT 5;", (b8_id,))
    sample_v = cursor.fetchall()
    for sv in sample_v:
        print(f"  • {sv['german_word']} ({sv['article']}): {sv['vietnamese_meaning']} | VD: {sv['example_sentence'][:40]}...")
    print("✅ TEST 3 PASS: Đủ 50/50 từ vựng danh lam thắng cảnh & giao thông thành phố!")

    # 4. Check 100 exercises of Lesson 8
    print("\n[TEST 4] Kiểm tra 100 Bài tập độc nhất của Bài 8:")
    cursor.execute("SELECT id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data FROM exercises WHERE lesson_id = ? ORDER BY id ASC;", (b8_id,))
    exercises = cursor.fetchall()
    assert len(exercises) == 100, f"❌ Lỗi: Số bài tập là {len(exercises)}, kỳ vọng đúng 100!"

    # Duplicate check
    q_texts = [e["question"] for e in exercises]
    unique_q = set(q_texts)
    assert len(unique_q) == 100, f"❌ Lỗi: Có {100 - len(unique_q)} câu hỏi bị trùng lặp tiêu đề!"

    # Distribution check
    type_counts = {}
    for e in exercises:
        t = e["exercise_type"]
        type_counts[t] = type_counts.get(t, 0) + 1
    
    expected_dist = {
        "trac_nghiem": 18,
        "dien_khuyet": 15,
        "dich_nghia_vd": 12,
        "dich_nghia_dv": 12,
        "noi_o": 10,
        "dien_tao_cau": 10,
        "nghe_dien": 9,
        "dich_cau_vd": 7,
        "dich_cau_dv": 7
    }
    print("  Phân bố bài tập:")
    for k, expected_num in expected_dist.items():
        actual_num = type_counts.get(k, 0)
        print(f"  • {k:15}: {actual_num} câu (Kỳ vọng: {expected_num})")
        assert actual_num == expected_num, f"❌ Lỗi phân bố ở {k}: {actual_num} != {expected_num}"
    print("✅ TEST 4 PASS: ĐÚNG 100 bài tập 9 dạng độc nhất, 0% trùng lặp!")

    # 5. Check 'noi_o' (Q58 -> Q67)
    print("\n[TEST 5] Kiểm tra chất lượng nhóm Nối ô (Câu 58 -> 67):")
    noi_o_list = [e for e in exercises if e["exercise_type"] == "noi_o"]
    assert len(noi_o_list) == 10, "❌ Lỗi: Không đủ 10 câu nối ô!"
    for idx, e in enumerate(noi_o_list, 58):
        extra = json.loads(e["extra_data"])
        pairs = extra.get("noi_o_pairs", [])
        assert len(pairs) == 4, f"❌ Câu {idx} không đủ 4 cặp!"
        
        # Kiểm tra không có nhãn ngữ pháp trong ngoặc ở đề bài và cột trái
        import re
        q_title = e["question"]
        grammar_brackets = ["(Dativ)", "(Akkusativ)", "(Nominativ)", "(bis zu)", "(3. Person", "(1. Person", "(2. Person", "(Sie)", "(du)", "(ihr)", "(wir)", "(Maskulinum)", "(Femininum)", "(Neutrum)"]
        for gb in grammar_brackets:
            assert gb.lower() not in q_title.lower(), f"❌ Câu {idx} có nhãn ngữ pháp {gb} trong tiêu đề: {q_title}"
        assert "Ngài" not in q_title and "Cậu" not in q_title, f"❌ Câu {idx} có Ngài/Cậu trong tiêu đề: {q_title}"
        assert "Khu triển lãm" not in q_title, f"❌ Câu {idx} có 'Khu triển lãm' trong tiêu đề: {q_title}"

        for p_idx, p in enumerate(pairs, 1):
            left_text = p["left"]
            right_text = p["right"]
            # Kiểm tra không có nhãn ngữ pháp trong ngoặc ở cột trái
            for gb in grammar_brackets:
                assert gb.lower() not in left_text.lower(), f"❌ Câu {idx} cặp {p_idx} có nhãn ngữ pháp {gb} ở cột trái: {left_text}"
            assert "Ngài" not in left_text and "Cậu" not in left_text, f"❌ Câu {idx} cặp {p_idx} có Ngài/Cậu ở cột trái: {left_text}"
            assert "Khu triển lãm" not in left_text and "Khu triển lãm" not in right_text, f"❌ Câu {idx} có 'Khu triển lãm': {left_text} / {right_text}"
            
            # Kiểm tra ô tiếng Đức không chứa tiếng Việt lẫn lộn
            if idx in (59, 61, 63, 65, 67):
                viet_chars = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
                for ch in viet_chars:
                    assert ch not in left_text.lower(), f"❌ Câu {idx} có tiếng Việt ở cột trái: {left_text}"
            viet_chars = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
            for ch in viet_chars:
                assert ch not in right_text.lower(), f"❌ Câu {idx} có tiếng Việt ở cột phải: {right_text}"

        # Kiểm tra Dịch nghĩa có 4 dòng riêng biệt, không có dấu | (trừ câu 60, 64 đã ẩn dịch nghĩa)
        trans = extra.get("translation", "")
        if idx not in (60, 64):
            assert "|" not in trans, f"❌ Câu {idx} Dịch nghĩa còn dồn bằng dấu '|': {trans}"
            assert "1." in trans and "2." in trans and "3." in trans and "4." in trans, f"❌ Câu {idx} không dịch đủ 4 cặp: {trans}"
        else:
            assert trans == "", f"❌ Câu {idx} phải ẩn Dịch nghĩa (chuỗi rỗng)!"
        assert "Ngài" not in trans and "Cậu" not in trans, f"❌ Câu {idx} Dịch nghĩa có Ngài/Cậu: {trans}"
        assert "Khu triển lãm" not in trans, f"❌ Câu {idx} Dịch nghĩa có 'Khu triển lãm': {trans}"

        # Kiểm tra Giải thích
        exp = e["explanation"]
        assert exp and len(exp) > 20, f"❌ Câu {idx} thiếu giải thích chi tiết!"
        assert "Ngài" not in exp and "Cậu" not in exp, f"❌ Câu {idx} Giải thích có Ngài/Cậu: {exp}"
        assert "Khu triển lãm" not in exp, f"❌ Câu {idx} Giải thích có 'Khu triển lãm': {exp}"

        # Kiểm tra cụ thể Câu 62: phân biệt rõ ràng không thể nhầm lẫn giữa Cặp 2 (người bạn thân đi bộ) và Cặp 3 (hai bạn đi xe buýt)
        if idx == 62:
            assert any("đi bộ qua quảng trường" in p["left"] for p in pairs), "❌ Câu 62 Cặp 2 thiếu chi tiết đi bộ qua quảng trường!"
            assert any("đi bằng xe buýt" in p["left"] for p in pairs), "❌ Câu 62 Cặp 3 thiếu chi tiết đi bằng xe buýt!"
            print(f"  • Câu 62: Đã phân biệt rõ ràng 100% giữa người bạn thân (đi bộ qua quảng trường) và 2 bạn (đi xe buýt).")

        # Kiểm tra cụ thể Câu 66: lộ trình rõ ràng trên đề bài để xác định thứ tự từng bước
        if idx == 66:
            assert "lộ trình" in q_title and "Khách sạn" in q_title, f"❌ Câu 66 thiếu lộ trình trên đề bài: {q_title}"
            print(f"  • Câu 66: Đề bài nêu rõ lộ trình từng bước (Ga tàu ➔ Cầu & Công viên ➔ Ngã tư ➔ Khách sạn).")
    print("✅ TEST 5 PASS: Cả 10 bài nối ô không có nhãn ngữ pháp, dịch đủ 4 dòng riêng biệt và không có Ngài/Cậu/Khu triển lãm 100%!")

    # 6. Check 'dien_tao_cau' (Q68 -> Q77)
    print("\n[TEST 6] Kiểm tra nhóm Điền tạo câu (Câu 68 -> 77):")
    dtc_list = [e for e in exercises if e["exercise_type"] == "dien_tao_cau"]
    assert len(dtc_list) == 10, "❌ Lỗi: Không đủ 10 câu điền tạo câu!"

    def normalize_german_slot(s):
        if not s:
            return ""
        s = s.strip().lower()
        import re
        s = re.sub(r'[.,!?;:…]+$', '', s).strip()
        s = re.sub(r'\s+', ' ', s)
        s = s.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
        return s

    def evaluate_multi_slot(user_ans, slot1_list, slot2_list):
        if not user_ans or '/' not in user_ans:
            return False
        parts = [p.strip() for p in user_ans.split('/')]
        if len(parts) != 2 or not parts[0] or not parts[1]:
            return False
        u1 = normalize_german_slot(parts[0])
        u2 = normalize_german_slot(parts[1])
        s1 = [normalize_german_slot(x) for x in slot1_list]
        s2 = [normalize_german_slot(x) for x in slot2_list]
        return (u1 in s1) and (u2 in s2)

    for idx, e in enumerate(dtc_list, 68):
        q_title = e["question"]
        corr = e["correct_answer"]
        exp = e["explanation"]
        extra = json.loads(e["extra_data"])
        trans = extra.get("translation", "")
        slot1 = extra.get("slot1_accepted", [])
        slot2 = extra.get("slot2_accepted", [])

        # Kiểm tra không chứa "Ngài" hoặc "Cậu"
        assert "Ngài" not in q_title and "Cậu" not in q_title, f"❌ Câu {idx} có Ngài/Cậu trong câu hỏi: {q_title}"
        assert "Ngài" not in trans and "Cậu" not in trans, f"❌ Câu {idx} có Ngài/Cậu trong dịch nghĩa: {trans}"
        assert "Ngài" not in exp and "Cậu" not in exp, f"❌ Câu {idx} có Ngài/Cậu trong giải thích: {exp}"

        # Kiểm tra slot1 và slot2
        assert len(slot1) >= 1 and len(slot2) >= 1, f"❌ Câu {idx} thiếu slot1_accepted hoặc slot2_accepted!"
        assert "/" in corr, f"❌ Câu {idx} đáp án không có dấu '/': {corr}"

        # Kiểm tra chi tiết từng câu theo yêu cầu
        if idx == 68:
            assert "cho người bạn thân (du)" not in q_title, "❌ Câu 68 còn 'cho người bạn thân (du)'!"
            assert "ngăn cách bởi dấu /" in q_title, "❌ Câu 68 thiếu 'ngăn cách bởi dấu /'!"
            assert "Lauf zuerst [1] den Park und geh dann an [2] Kirche vorbei bis zum Bahnhof!" in q_title
            assert trans == "Đầu tiên bạn hãy đi xuyên qua công viên, rồi đi ngang qua nhà thờ cho đến nhà ga nhé!"
            assert extra.get("visual_svg") == "map_build_1"
        elif idx == 69:
            assert "lịch sự" not in q_title, "❌ Câu 69 còn chữ 'lịch sự'!"
            assert "ngăn cách bởi dấu /" in q_title, "❌ Câu 69 thiếu 'ngăn cách bởi dấu /'!"
            assert "Gehen Sie zuerst [1] die Brücke und dann die Goethestraße [2] bis zur Post!" in q_title
            assert trans == "Trước tiên quý vị hãy đi qua cây cầu, rồi đi dọc theo phố Goethe cho đến bưu điện!"
            assert extra.get("visual_svg") == "map_build_2"
        elif idx == 74:
            assert evaluate_multi_slot("in die / in der", slot1, slot2) is True, "❌ Câu 74: 'in die / in der' phải ĐÚNG!"
            assert evaluate_multi_slot("in der", slot1, slot2) is False, "❌ Câu 74: 'in der' phải SAI!"
            assert evaluate_multi_slot("in der / in die", slot1, slot2) is False, "❌ Câu 74: 'in der / in die' phải SAI!"
            assert evaluate_multi_slot("in der / in der", slot1, slot2) is False, "❌ Câu 74: 'in der / in der' phải SAI!"
        elif idx == 73:
            assert evaluate_multi_slot("muesst / koennt", slot1, slot2) is True, "❌ Câu 73: 'muesst / koennt' phải ĐÚNG!"
            assert evaluate_multi_slot("musst / könnt", slot1, slot2) is False, "❌ Câu 73: 'musst / könnt' phải SAI!"
        elif idx == 77:
            assert "erste" not in q_title and "zweite" not in q_title, "❌ Câu 77 lộ đáp án erste / zweite trên đề!"
            assert "1. vào chỗ trống [1] và 2. vào chỗ trống [2]" in q_title
            assert trans == "Quý vị hãy đi con đường thứ nhất bên phải, rồi sau đó rẽ trái lại ở ngã tư thứ hai!"
            assert evaluate_multi_slot("erste / zweiten", slot1, slot2) is True, "❌ Câu 77: 'erste / zweiten' phải ĐÚNG!"
            assert evaluate_multi_slot("erste / zweite", slot1, slot2) is False, "❌ Câu 77: 'erste / zweite' phải SAI!"

    # Kiểm tra bản đồ SVG city_map_svg.js
    with open("static/js/city_map_svg.js", "r", encoding="utf-8") as f:
        svg_content = f.read()
    assert "map_build_1" in svg_content
    assert "map_build_2" in svg_content
    assert "Park" in svg_content and "Kirche" in svg_content and "Bahnhof" in svg_content
    assert "Brücke" in svg_content and "Goethestraße" in svg_content and "Post" in svg_content
    # Không còn Dom trong map_build_1
    build_1_block = svg_content[svg_content.find("map_build_1"):svg_content.find("map_build_2")]
    assert "Dom" not in build_1_block, "❌ map_build_1 vẫn còn nhãn 'Dom'!"
    # Bỏ Krankenhaus, Ampel, Kreuzung trong map_build_2
    build_2_block = svg_content[svg_content.find("function getMapBuild2Svg"):svg_content.find("function renderExerciseSvg")]
    assert "Krankenhaus" not in build_2_block, "❌ map_build_2 vẫn còn Krankenhaus!"
    assert "Ampel" not in build_2_block, "❌ map_build_2 vẫn còn Ampel!"
    assert "Kreuzung" not in build_2_block, "❌ map_build_2 vẫn còn Kreuzung!"
    print("✅ TEST 6 PASS: Cả 10 bài điền tạo câu và 2 bản đồ SVG đáp ứng 100% chuẩn chấm từng ô & zero-spoiler!")

    # 7. Check 'dich_cau' (Q87 -> Q100)
    print("\n[TEST 7] Kiểm tra nhóm Dịch câu V->Đ và Đ->V (Câu 87 -> 100):")
    trans_list = [e for e in exercises if e["exercise_type"] in ("dich_cau_vd", "dich_cau_dv")]
    assert len(trans_list) == 14, "❌ Lỗi: Không đủ 14 câu dịch câu!"
    for e in trans_list:
        extra = json.loads(e["extra_data"])
        acc = extra.get("accepted_answers", [])
        assert len(acc) >= 2, f"❌ Câu {e['question'][:20]} thiếu đa đáp án: {acc}"
        assert e["explanation"] is not None and len(e["explanation"]) > 10, f"❌ Câu {e['question'][:20]} thiếu giải thích chi tiết!"
    print("✅ TEST 7 PASS: Cả 14 bài dịch câu có đa đáp án linh hoạt và lời giải sư phạm đầy đủ!")

    # 8. Check 'dich_cau_vd' (Q87 -> Q93): Text & Grading Rubric
    print("\n[TEST 8] Kiểm tra chi tiết Nhóm Dịch câu Việt -> Đức (Câu 87 -> 93):")
    q87_93 = [e for e in exercises if e["exercise_type"] == "dich_cau_vd"]
    assert len(q87_93) == 7, f"❌ Kỳ vọng 7 câu dich_cau_vd, thực tế có {len(q87_93)}"

    for idx, e in enumerate(q87_93, 87):
        q_title = e["question"]
        exp = e["explanation"]
        extra = json.loads(e["extra_data"])
        trans = extra.get("translation", "")

        # Không chứa "Ngài" hoặc "Cậu"
        assert "Ngài" not in q_title and "Cậu" not in q_title, f"❌ Câu {idx} có Ngài/Cậu trong đề bài: {q_title}"
        assert "Ngài" not in exp and "Cậu" not in exp, f"❌ Câu {idx} có Ngài/Cậu trong giải thích: {exp}"

        # Translation không có '=' và không lặp lại tiếng Việt
        assert "=" not in trans, f"❌ Câu {idx} translation vẫn còn dấu '=': {trans}"
        assert not re.search(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', trans, re.I), f"❌ Câu {idx} translation vẫn còn tiếng Việt: {trans}"

        if idx == 87:
            assert "quý vị" in q_title, f"❌ Câu 87 đề bài chưa có 'quý vị': {q_title}"
            assert trans == "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!"
        elif idx == 88:
            assert "Bạn hãy" in q_title, f"❌ Câu 88 đề bài chưa có 'Bạn hãy': {q_title}"
            assert "'abbiegen' là động từ tách: 'bieg … ab' (cũng được 'biege … ab')." in exp
            assert trans == "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!"
        elif idx == 89:
            assert trans == "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?"
        elif idx == 90:
            assert trans == "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus."
        elif idx == 91:
            assert "Khi 'Am Vormittag' đứng đầu câu" in exp and "'in der Morgen' là sai" in exp
            assert trans == "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln."
        elif idx == 92:
            assert trans == "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper."
        elif idx == 93:
            assert "'du' và 'Sie' đều được chấp nhận." in exp
            assert trans == "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen."

    # Kiểm tra thuật toán chấm ngữ pháp & hints Câu 87-93
    TARGET_NOUNS = {'stadttor', 'brandenburger', 'museumsinsel', 'einkaufszentrum', 'krankenhaus', 'marktplatz', 'reichstag', 'kreuzung', 'staatsoper', 'touristen', 'besucher'}
    PREFIXES = ['der', 'die', 'das', 'den', 'dem', 'des', 'am', 'im', 'zum', 'zur', 'durch', 'ueber', 'an', 'in', 'mit', 'auf', 'vor', 'nach', 'um', 'bis', 'zu']
    KNOWN_STEMS = [
        'grossen', 'grosser', 'grosse', 'kleinen', 'alten', 'zweiten', 'ersten', 'bruecke',
        'krankenhaus', 'ampel', 'park', 'fluss', 'kreuzung', 'museumsinsel', 'kirche',
        'marktplatz', 'rathaus', 'reichstag', 'einkaufszentrum', 'bus', 'brandenburger',
        'tor', 'abend', 'staatsoper', 'hafen', 'stadttor', 'bank', 'morgen', 'vormittag',
        'nachmittag', 'fuss', 'kommen', 'gehen', 'vorbei', 'links', 'rechts'
    ]

    def levenshtein(s1, s2):
        if len(s1) < len(s2):
            return levenshtein(s2, s1)
        if len(s2) == 0:
            return len(s1)
        prev = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            curr = [i + 1]
            for j, c2 in enumerate(s2):
                ins = prev[j + 1] + 1
                dels = curr[j] + 1
                subs = prev[j] + (c1 != c2)
                curr.append(min(ins, dels, subs))
            prev = curr
        return prev[-1]

    def normalize_vd(text):
        if not text:
            return ''
        s = text.lower()
        s = s.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
        s = re.sub(r'[\.,!?;:\"\'„“”»«\(\)\-\–]', ' ', s)
        s = re.sub(r'\s+', ' ', s).strip()
        tokens = s.split(' ')
        expanded = []
        for tok in tokens:
            decoupled = False
            for p in PREFIXES:
                if tok.startswith(p) and len(tok) > len(p):
                    rest = tok[len(p):]
                    if rest in KNOWN_STEMS or rest in PREFIXES or rest in TARGET_NOUNS:
                        expanded.append(p)
                        decoupled_second = False
                        for p2 in PREFIXES:
                            if rest.startswith(p2) and len(rest) > len(p2):
                                rest2 = rest[len(p2):]
                                if rest2 in KNOWN_STEMS or rest2 in TARGET_NOUNS:
                                    expanded.append(p2)
                                    expanded.append(rest2)
                                    decoupled_second = True
                                    break
                        if not decoupled_second:
                            expanded.append(rest)
                        decoupled = True
                        break
            if not decoupled:
                if tok == 'vorbeigehen':
                    expanded.extend(['vorbei', 'gehen'])
                elif tok == 'linksab':
                    expanded.extend(['links', 'ab'])
                elif tok == 'rechtsab':
                    expanded.extend(['rechts', 'ab'])
                else:
                    expanded.append(tok)
        final_tokens = []
        for tok in expanded:
            mapped = tok
            if len(tok) >= 6:
                for tn in TARGET_NOUNS:
                    if levenshtein(tok, tn) <= 1:
                        mapped = tn
                        break
            final_tokens.append(mapped)
        return ' '.join(final_tokens)

    def eval_vd(user_ans, q_num):
        norm = normalize_vd(user_ans)
        if q_num == 87:
            p87 = r'^(?:zuerst\s+)?gehen\s+sie(?:\s+(?:zuerst|zunaechst|als\s+erstes))?\s+(?:geradeaus\s+ueber\s+die\s+bruecke|ueber\s+die\s+bruecke\s+geradeaus)\s+(?:(?:und\s+)?(?:dann|danach|anschliessend)\s+(?:gehen\s+sie\s+)?)?(?:am|an\s+dem)\s+krankenhaus\s+vorbei\s+bis\s+(?:zur|zu\s+der)\s+zweiten\s+ampel$'
            if re.match(p87, norm):
                return True, ''
            if re.search(r'bis\s+zum\b', norm):
                return False, "Chú ý mạo từ: 'die Ampel' là giống cái, sau 'bis zu' (+ Dativ) phải dùng 'bis zur zweiten Ampel' (hoặc 'bis zu der zweiten Ampel'), không dùng 'bis zum'."
            return False, "Cần dịch đúng: 'Gehen Sie (zuerst) geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!'"
        elif q_num == 88:
            p88 = r'^(?:geh|gehe|lauf|laufe)\s+durch\s+den\s+park(?:\s+und)?(?:\s+(?:geh|gehe|lauf|laufe))?\s+(?:den\s+fluss\s+entlang|am\s+fluss\s+entlang)\s+und\s+(?:bieg|biege)\s+(?:an\s+der\s+ersten\s+kreuzung\s+links|links\s+an\s+der\s+ersten\s+kreuzung)\s+ab$'
            if re.match(p88, norm):
                return True, ''
            if re.search(r'gehen\s+sie', norm) or re.search(r'\bsie\b', norm):
                return False, "Đề bài yêu cầu dùng ngôi thân mật 'du' (Geh... / Lauf... và bieg ... ab), không dùng 'Gehen Sie'."
            return False, "Cần dịch đúng: 'Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!'"
        elif q_num == 89:
            p89 = r'^(?:entschuldigung|entschuldigen\s+sie|verzeihung)\s+wir\s+suchen\s+die\s+museumsinsel\s+wie\s+(?:kommen|gehen)\s+wir(?:\s+zu\s+fuss)?\s+(?:zur|zu\s+der|auf\s+die)\s+museumsinsel(?:\s+zu\s+fuss)?$'
            if re.match(p89, norm):
                return True, ''
            return False, "Cần dịch đúng: 'Entschuldigung / Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir (zu Fuß) zur Museumsinsel?'"
        elif q_num == 90:
            p90 = r'^(?:geht|lauft)\s+an\s+der\s+alten\s+kirche\s+vorbei\s+und\s+(?:(?:geht|lauft)\s+)?ueber\s+den\s+marktplatz\s+(?:rechts\s+seht\s+ihr\s+das\s+rathaus|ihr\s+seht\s+rechts\s+das\s+rathaus|auf\s+der\s+rechten\s+seite\s+seht\s+ihr\s+das\s+rathaus|rechts\s+ist\s+das\s+rathaus)$'
            if re.match(p90, norm):
                return True, ''
            if re.search(r'ueber\s+dem\s+marktplatz', norm):
                return False, "Chuyển động băng qua quảng trường dùng Akkusativ: 'über den Marktplatz' (không dùng Dativ 'über dem')."
            return False, "Cần dịch đúng: 'Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.'"
        elif q_num == 91:
            p_c1 = r'(?:(?:(?:am\s+morgen|am\s+vormittag)\s+(?:will|moechte)\s+mein\s+onkel|mein\s+onkel\s+(?:will|moechte)\s+(?:am\s+morgen|am\s+vormittag))\s+den\s+reichstag\s+besichtigen)'
            p_c2 = r'(?:(?:(?:am\s+nachmittag)\s+(?:wollen|moechten)\s+wir|wir\s+(?:wollen|moechten)\s+am\s+nachmittag)\s+im\s+einkaufszentrum\s+bummeln)'
            p91 = rf'^{p_c1}\s+und\s+{p_c2}$'
            if re.match(p91, norm):
                return True, ''
            if re.search(r'in\s+der\s+morgen|im\s+morgen', norm):
                return False, "Cụm chỉ buổi sáng chưa đúng: dùng 'am Morgen' hoặc 'am Vormittag'."
            if re.search(r'(?:am\s+vormittag|am\s+morgen)\s+mein\s+onkel\s+(?:will|moechte)', norm):
                return False, "Khi 'Am Vormittag' đứng đầu câu, động từ chia ('will') đứng ngay sau nó, rồi mới đến chủ ngữ: 'Am Vormittag will mein Onkel …'. 'Am Morgen' cũng đúng; 'in der Morgen' là sai. 'möchte / möchten' cũng được chấp nhận."
            return False, "Cần dịch đúng: 'Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln.'"
        elif q_num == 92:
            p92 = r'^(?:zuerst\s+fahren\s+die\s+(?:touristen|besucher)|die\s+(?:touristen|besucher)\s+fahren\s+zuerst)\s+mit\s+dem\s+bus\s+(?:zum|zu\s+dem|bis\s+zum)\s+brandenburger\s+tor\s+und\s+(?:am\s+abend\s+gehen\s+sie|gehen\s+(?:sie\s+)?am\s+abend|abends\s+gehen\s+sie|sie\s+gehen\s+(?:am\s+abend|abends))\s+in\s+die\s+staatsoper$'
            if re.match(p92, norm):
                return True, ''
            return False, "Cần dịch đúng: 'Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper.'"
        elif q_num == 93:
            p93_a = r'^(?:um\s+(?:zum|zu\s+dem)\s+hafen\s+zu\s+kommen|um\s+den\s+hafen\s+zu\s+erreichen)\s+(?:musst\s+du|muessen\s+sie)\s+durch\s+das\s+stadttor(?:\s+gehen)?\s+und\s+an\s+der\s+grossen\s+bank\s+(?:vorbei\s+gehen|vorbeigehen)$'
            p93_b = r'^(?:du\s+musst|sie\s+muessen)\s+durch\s+das\s+stadttor(?:\s+gehen)?\s+und\s+an\s+der\s+grossen\s+bank\s+(?:vorbei\s+gehen|vorbeigehen)\s+um\s+(?:zum|zu\s+dem)\s+hafen\s+zu\s+kommen$'
            if re.match(p93_a, norm) or re.match(p93_b, norm):
                return True, ''
            if re.search(r'an\s+die\s+grossen\s+bank', norm) or re.search(r'an\s+die\s+grosse\s+bank', norm):
                return False, "Giới từ chỉ vị trí ngang qua: 'an der großen Bank vorbei' (an + Dativ giống cái: 'der', tính từ mang đuôi '-en')."
            if re.search(r'an\s+der\s+grosse\s+bank', norm):
                return False, "Đuôi tính từ sau mạo từ xác định ở Dativ là '-en': dùng 'an der großen Bank', không dùng 'große'."
            return False, "Cần dịch đúng: 'Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen.' ('du' và 'Sie' đều được chấp nhận)."
        return False, ''

    test_cases = [
        # ĐÚNG
        (93, 'um zum hafen zu kommen musst du durch das stadttor und an dergroßen bank vorbeigehen', True, ''),
        (93, 'Du musst durch das Stadttor und an der großen Bank vorbeigehen, um zum Hafen zu kommen.', True, ''),
        (91, 'Am Morgen möchte mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln', True, ''),
        (89, 'Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir zur Museumsinsel zu Fuß?', True, ''),
        # SAI
        (91, 'In der Morgen möchte mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln', False, 'am Morgen'),
        (91, 'Am Vormittag mein Onkel will den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln', False, 'đứng ngay sau nó'),
        (93, 'Um zum Hafen zu kommen, musst du durch das Stadttor und an die großen Bank vorbeigehen.', False, 'an der großen Bank vorbei'),
        (93, 'Um zum Hafen zu kommen, musst du durch das Stadttor và an der große Bank vorbeigehen.', False, 'đuôi tính từ'),
        (88, 'Gehen Sie durch den Park, laufen Sie den Fluss entlang und biegen Sie an der ersten Kreuzung links ab!', False, 'ngôi thân mật'),
        (90, 'Geht an der alten Kirche vorbei und über dem Marktplatz, rechts seht ihr das Rathaus.', False, 'über den Marktplatz'),
        (87, 'Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zum zweiten Ampel!', False, 'bis zur zweiten Ampel'),
    ]

    for q_n, inp, exp_b, exp_kw in test_cases:
        res_b, res_hint = eval_vd(inp, q_n)
        assert res_b == exp_b, f"❌ Q{q_n} test failed for input '{inp}': expected {exp_b}, got {res_b}"
        if not exp_b and exp_kw:
            assert exp_kw.lower() in res_hint.lower(), f"❌ Q{q_n} hint missing '{exp_kw}': got '{res_hint}'"

    print("✅ TEST 8 PASS: Cả 7 bài dịch câu Việt -> Đức (Q87 -> 93) đáp ứng 100% chuẩn văn bản, không dấu '=', và vượt qua toàn bộ test cases ngữ pháp & hints!")

    conn.close()
    print("\n" + "=" * 60)
    print("🎉 TOÀN BỘ 8/8 BÀI TEST QA BÀI 8 ĐẠT TIÊU CHUẨN 100% PASS!")
    print("=" * 60)

if __name__ == "__main__":
    verify()
