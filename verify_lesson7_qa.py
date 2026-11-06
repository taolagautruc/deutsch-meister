"""
verify_lesson7_qa.py - Kịch bản kiểm thử tự động toàn diện Zero-Bug QA cho Bài 7 (A1)
Kiểm tra 6 tiêu chí bắt buộc theo Ma trận đặc tả kỹ thuật Bài 7 DeutschMeister.
"""

import sys
import os
import re
import json
import sqlite3
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def run_tests():
    print("=" * 70)
    print("🚀 BẮT ĐẦU CHẠY KIỂM THỬ TỰ ĐỘNG ZERO-BUG QA CHO BÀI 7 (A1)")
    print("=" * 70)

    conn = get_connection()
    c = conn.cursor()

    # -------------------------------------------------------------------------
    # TEST 1: ZERO-REGRESSION CHECK (BẢO TOÀN TUYỆT ĐỐI BÀI 1 -> BÀI 6 & BÀI 7)
    # -------------------------------------------------------------------------
    print("\n🔍 TEST 1: Zero-Regression Check (Bảo toàn tuyệt đối Bài 1 -> Bài 6 & Bài 7)...")
    expected_lessons = [
        (14, 'Bài 1 (P1): "Làm Quen Với Tiếng Đức, Bảng Chữ Cái và Đếm Số"', 30, 50),
        (15, 'Bài 1 (P2): "Kaffee oder Tee - Cà Phê Hoặc Trà"', 34, 50),
        (16, 'Bài 2: "Sprache im Kurs - Động Từ và Giống (der, die, das & Mạo Từ)"', 36, 50),
        (17, 'Bài 3: "Städte – Länder – Sprachen: Địa Danh, Phương Hướng & Thì Quá Khứ Đơn (Präteritum)"', 42, 50),
        (18, 'Bài 4: "Menschen und Häuser - Nhà Ở, Cách 1 Nominativ / Cách 4 Akkusativ & Mạo Từ Sở Hữu"', 53, 50),
        (19, 'Bài 5: "Thời gian - Động từ tách - Haben in Präteritum (Termine)"', 38, 50),
        (20, 'Bài 6: "Dativ - Giới từ trong Dativ - Phương tiện giao thông - Số thứ tự - Ngày tháng năm (Orientierung)"', 45, 100),
        (21, 'Bài 7: "Beruf - Modalverben - Artikelwörter in Akkusativ (Nghề nghiệp - Động từ khuyết thiếu - Từ hạn định Cách 4 & Phân biệt Akkusativ / Dativ)"', 50, 100)
    ]

    for lid, expected_title, exp_v, exp_e in expected_lessons:
        c.execute("SELECT id, title, grammar_content FROM lessons WHERE id = ?;", (lid,))
        row = c.fetchone()
        assert row is not None, f"❌ LỖI: Bài học ID {lid} không tồn tại!"
        assert row["title"] == expected_title, f"❌ LỖI: Tiêu đề Bài {lid} bị sai lệch! Nhận được: '{row['title']}'"
        assert len(row["grammar_content"] or "") > 500, f"❌ LỖI: Lý thuyết Bài {lid} bị trống!"

        c.execute("SELECT count(*) as cnt FROM vocabularies WHERE lesson_id = ?;", (lid,))
        vcnt = c.fetchone()["cnt"]
        assert vcnt == exp_v, f"❌ LỖI: Từ vựng Bài {lid} có {vcnt} từ, kỳ vọng {exp_v} từ!"

        c.execute("SELECT count(*) as cnt FROM exercises WHERE lesson_id = ?;", (lid,))
        ecnt = c.fetchone()["cnt"]
        assert ecnt == exp_e, f"❌ LỖI: Bài tập Bài {lid} có {ecnt} câu, kỳ vọng {exp_e} câu!"
        print(f"   ✅ Lesson {lid}: '{row['title'][:40]}...' -> {vcnt} vocab, {ecnt} exercises (PASSED)")

    print("✅ TEST 1: Zero-Regression Check ĐẠT 100%!")

    # -------------------------------------------------------------------------
    # TEST 2: 100-QUESTION & 9-TYPE VERIFICATION (BÀI 7)
    # -------------------------------------------------------------------------
    print("\n🔍 TEST 2: 100-Question & 9-Type Verification (Bài 7)...")
    expected_type_counts = {
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

    c.execute("SELECT exercise_type, count(*) as cnt FROM exercises WHERE lesson_id = 21 GROUP BY exercise_type;")
    actual_counts = {r["exercise_type"]: r["cnt"] for r in c.fetchall()}
    total_q = sum(actual_counts.values())
    assert total_q == 100, f"❌ LỖI: Tổng số câu hỏi Bài 7 là {total_q}, kỳ vọng 100!"

    for etype, exp_c in expected_type_counts.items():
        act_c = actual_counts.get(etype, 0)
        assert act_c == exp_c, f"❌ LỖI dạng '{etype}': có {act_c} câu, kỳ vọng {exp_c} câu!"
        print(f"   ✅ Dạng '{etype}': {act_c}/{exp_c} câu (PASSED)")

    c.execute("SELECT question FROM exercises WHERE lesson_id = 21;")
    all_questions = [r["question"] for r in c.fetchall()]
    assert len(set(all_questions)) == 100, f"❌ LỖI: Phát hiện câu hỏi trùng lặp! Chỉ có {len(set(all_questions))} câu độc nhất."
    print("   ✅ Kiểm tra chống trùng lặp: Đủ 100/100 câu hỏi hoàn toàn độc nhất (PASSED)")
    print("✅ TEST 2: 100-Question & 9-Type Verification ĐẠT 100%!")

    # -------------------------------------------------------------------------
    # TEST 3: ATOMIC ALIGNMENT & ZERO LEAKAGE CHECK
    # -------------------------------------------------------------------------
    print("\n🔍 TEST 3: Atomic Alignment & Zero Leakage Check...")
    c.execute("SELECT id, exercise_type, question, options_json, correct_answer, explanation, extra_data FROM exercises WHERE lesson_id = 21 ORDER BY id;")
    b7_exercises = c.fetchall()

    for idx, ex in enumerate(b7_exercises):
        q_num = idx + 1
        q_text = ex["question"]
        etype = ex["exercise_type"]
        corr = ex["correct_answer"]
        exp = ex["explanation"]
        extra = json.loads(ex["extra_data"]) if ex["extra_data"] else {}

        # 3.1. Đề bài, giải thích, dịch nghĩa không được để trống
        assert q_text and len(q_text.strip()) > 5, f"❌ LỖI: Câu {q_num} có đề bài trống!"
        assert exp and len(exp.strip()) > 5, f"❌ LỖI: Câu {q_num} có giải thích trống!"
        assert extra.get("translation"), f"❌ LỖI: Câu {q_num} thiếu bản dịch tiếng Việt (translation)!"

        # 3.2. Kiểm tra trắc nghiệm
        if etype == "trac_nghiem":
            opts = json.loads(ex["options_json"])
            assert len(opts) == 4, f"❌ LỖI: Câu {q_num} trắc nghiệm có {len(opts)} lựa chọn, kỳ vọng 4!"
            assert corr in opts, f"❌ LỖI: Đáp án đúng '{corr}' không nằm trong options câu {q_num}!"

        # 3.3. Kiểm tra tự luận / điền khuyết
        if etype in ["dien_khuyet", "dich_nghia_vd", "dich_nghia_dv", "dien_tao_cau", "dich_cau_vd", "dich_cau_dv"]:
            accepted = extra.get("accepted_answers", [])
            assert len(accepted) > 0, f"❌ LỖI: Câu {q_num} ({etype}) thiếu accepted_answers!"
            assert corr in accepted, f"❌ LỖI: Đáp án chuẩn '{corr}' không có trong accepted_answers câu {q_num}!"

        # 3.4. Kiểm tra nối ô
        if etype == "noi_o":
            pairs = extra.get("noi_o_pairs", [])
            assert len(pairs) == 4, f"❌ LỖI: Bài nối ô câu {q_num} có {len(pairs)} cặp, kỳ vọng 4!"
            for p in pairs:
                assert p.get("left") and p.get("right"), f"❌ LỖI: Cặp nối ô câu {q_num} thiếu left/right!"

        # 3.5. Kiểm tra nghe điền
        if etype == "nghe_dien":
            audio = extra.get("audio_text")
            assert audio and len(audio.strip()) > 5, f"❌ LỖI: Câu {q_num} nghe điền thiếu audio_text!"
            # Kiểm tra âm thanh không chứa tiếng Việt
            assert not any(ord(char) > 255 for char in audio if char not in "äöüÄÖÜß"), \
                f"❌ LỖI: audio_text chứa ký tự lạ/tiếng Việt: '{audio}'"

    print("   ✅ Toàn bộ 100 câu hỏi đều có bản dịch, giải thích và khớp nguyên tử (PASSED)")
    print("✅ TEST 3: Atomic Alignment & Zero Leakage Check ĐẠT 100%!")

    # -------------------------------------------------------------------------
    # TEST 4: VOCABULARY CARD MATCH CHECK
    # -------------------------------------------------------------------------
    print("\n🔍 TEST 4: Vocabulary Card Match Check (50 từ vựng)...")
    c.execute("SELECT german_word, article, vietnamese_meaning, example_sentence FROM vocabularies WHERE lesson_id = 21;")
    vocab_rows = c.fetchall()
    assert len(vocab_rows) == 50, f"❌ LỖI: Số từ vựng Bài 7 trong DB là {len(vocab_rows)}, kỳ vọng 50!"

    for v in vocab_rows:
        w = v["german_word"].split()[-1]
        ex = v["example_sentence"]
        has_match = (w.lower() in ex.lower())
        assert has_match, f"❌ LỖI: Câu ví dụ '{ex}' không chứa từ vựng '{w}'!"
        assert "(Pl:" in v["vietnamese_meaning"], f"❌ LỖI: Thẻ từ vựng '{v['german_word']}' thiếu dạng số nhiều (Pl: ...)!"

    print("   ✅ 50/50 từ vựng có ví dụ chứa danh từ mục tiêu và dạng số nhiều (Pl: ...) đầy đủ (PASSED)")
    print("✅ TEST 4: Vocabulary Card Match Check ĐẠT 100%!")

    # -------------------------------------------------------------------------
    # TEST 5: JAVASCRIPT & FRONTEND COMPATIBILITY CHECK
    # -------------------------------------------------------------------------
    print("\n🔍 TEST 5: JavaScript & Frontend Compatibility Check...")
    node_test = """
    const fs = require('fs');
    let lexContent = fs.readFileSync('static/js/lexikon_db.js', 'utf8');
    lexContent = lexContent.replace('const GERMAN_LEXIKON_DB', 'global.GERMAN_LEXIKON_DB');
    eval(lexContent);
    const b7 = global.GERMAN_LEXIKON_DB.filter(x => x.category && x.category.includes('Bài 7'));
    if (b7.length !== 50) {
        console.error('Lỗi: lexikon_db.js có ' + b7.length + ' từ Bài 7, kỳ vọng 50');
        process.exit(1);
    }

    let verbsContent = fs.readFileSync('static/js/verbs_db.js', 'utf8');
    verbsContent = verbsContent.replace('const GERMAN_VERBS_DB', 'global.GERMAN_VERBS_DB');
    eval(verbsContent);
    const b7Verbs = ['müssen', 'können', 'wollen', 'dürfen', 'sollen', 'unterrichten', 'untersuchen', 'reparieren', 'verkaufen', 'schneiden', 'brauchen', 'bringen', 'abholen', 'schlafen'];
    for (const v of b7Verbs) {
        const found = global.GERMAN_VERBS_DB.find(x => x.infinitiv === v);
        if (!found) {
            console.error('Lỗi: verbs_db.js thiếu động từ: ' + v);
            process.exit(1);
        }
    }

    let trainerContent = fs.readFileSync('static/js/number_trainer.js', 'utf8');
    trainerContent = trainerContent.replace(/window\\./g, 'global.');
    trainerContent = trainerContent.replace(/function finalize\\(ex\\)/g, 'global.finalize = function(ex)');
    eval(trainerContent);

    const testEngines = [
        { extra_data: JSON.stringify({ dynamic_profession_quiz: true }) },
        { extra_data: JSON.stringify({ dynamic_modalverb_schedule_quiz: true }) },
        { extra_data: JSON.stringify({ dynamic_akkdativ_kontrast_quiz: true }) },
        { extra_data: JSON.stringify({ dynamic_possessivartikel_akkusativ_quiz: true }) }
    ];
    for (const t of testEngines) {
        const res = global.generateNewNumberData(t);
        if (!res.question || !res.correct_answer) {
            console.error('Lỗi: dynamic engine thất bại', t);
            process.exit(1);
        }
    }

    console.log('✅ Frontend JS Databases: 50 danh từ, 14 động từ và 4 Randomizer Engines Bài 7 hợp lệ 100%');
    """
    import shutil
    node_bin = shutil.which('node') or (
        '/usr/local/bin/node' if os.path.exists('/usr/local/bin/node') else (
            '/opt/homebrew/bin/node' if os.path.exists('/opt/homebrew/bin/node') else 'node'
        )
    )
    res = subprocess.run([node_bin, '-e', node_test], capture_output=True, text=True)
    assert res.returncode == 0, f"❌ LỖI Node.js check: {res.stderr}"
    print("   " + res.stdout.strip())
    print("✅ TEST 5: JavaScript & Frontend Compatibility Check ĐẠT 100%!")

    # -------------------------------------------------------------------------
    # TEST 6: ARENA GENERATOR MULTI-LEVEL CHECK
    # -------------------------------------------------------------------------
    print("\n🔍 TEST 6: Arena Generator Check (Học đến đâu - Thi đến đó)...")
    import arena_generator
    assert 21 in arena_generator.LESSON_ORDER_MAP, "❌ LỖI: Bài 7 (ID 21) chưa có trong LESSON_ORDER_MAP!"
    assert 8 in arena_generator.ARENA_DATA_BY_LESSON, "❌ LỖI: Thứ tự 8 chưa có trong ARENA_DATA_BY_LESSON!"

    # Test sinh câu hỏi cho user có level Bài 7
    arena_qs = arena_generator.build_arena_questions_for_user(user_id=1, count=20)
    assert len(arena_qs) >= 15, f"❌ LỖI: Đấu trường sinh quá ít câu hỏi: {len(arena_qs)}"
    print(f"   ✅ Đấu trường sinh thành công {len(arena_qs)} câu hỏi đa dạng tới Bài 7 (PASSED)")
    print("✅ TEST 6: Arena Generator Check ĐẠT 100%!")

    conn.close()
    print("\n" + "=" * 70)
    print("🏆 TẤT CẢ 6/6 BÀI KIỂM THỬ ĐỀU ĐẠT 100% PASS! ZERO-BUG QUALITY ASSURED!")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()

