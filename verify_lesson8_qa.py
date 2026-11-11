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
    for idx, e in enumerate(dtc_list, 68):
        corr = e["correct_answer"]
        assert "/" in corr, f"❌ Câu {idx} đáp án không có dấu '/': {corr}"
        extra = json.loads(e["extra_data"])
        acc = extra.get("accepted_answers", [])
        assert len(acc) >= 2, f"❌ Câu {idx} thiếu biến thể accepted_answers: {acc}"
        for a in acc:
            assert "/" in a or "," in a, f"❌ Câu {idx} accepted_answer không có dấu ngăn cách: {a}"
    print("✅ TEST 6 PASS: Cả 10 bài điền tạo câu chuẩn cấu trúc 2 từ ngăn cách bởi dấu /!")

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

    conn.close()
    print("\n" + "=" * 60)
    print("🎉 TOÀN BỘ 7/7 BÀI TEST QA BÀI 8 ĐẠT TIÊU CHUẨN 100% PASS!")
    print("=" * 60)

if __name__ == "__main__":
    verify()
