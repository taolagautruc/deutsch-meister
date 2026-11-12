#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kịch bản Kiểm thử Toàn diện & Tự động Chuẩn Zero-Bug QA cho Bài 9 (A1)
"URLAUB - DU LỊCH - PERFEKT & PRÄTERITUM (QUÁ KHỨ VĂN NÓI)"
"""

import sys
import os
import json
import sqlite3
import re

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "deutsch_meister.db")

print("=" * 70)
print("🚀 BẮT ĐẦU KIỂM THỬ TOÀN DIỆN ZERO-BUG QA CHO BÀI 9 (A1)")
print("=" * 70)

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# -----------------------------------------------------------------------------
# TEST 1: Zero-Regression Check (Bảo toàn tuyệt đối Bài 1 -> Bài 8)
# -----------------------------------------------------------------------------
print("\n🔍 TEST 1: Zero-Regression Check (Bảo toàn tuyệt đối Bài 1 -> Bài 8)...")
expected_lessons = [
    (14, 'Bài 1 (P1)', 30, 50),
    (15, 'Bài 1 (P2)', 34, 50),
    (16, 'Bài 2', 36, 50),
    (17, 'Bài 3', 42, 50),
    (18, 'Bài 4', 53, 50),
    (19, 'Bài 5', 38, 50),
    (20, 'Bài 6', 45, 100),
    (21, 'Bài 7', 50, 100),
    (22, 'Bài 8', 50, 100),
]

for lid, title_sub, exp_v, exp_ex in expected_lessons:
    cur.execute("SELECT id, title FROM lessons WHERE id = ?;", (lid,))
    row = cur.fetchone()
    assert row is not None, f"Lỗi: Không tìm thấy bài học ID {lid}"
    assert title_sub in row["title"], f"Lỗi: Tiêu đề bài {lid} không khớp '{title_sub}'"

    cur.execute("SELECT COUNT(*) as c FROM vocabularies WHERE lesson_id = ?;", (lid,))
    vc = cur.fetchone()["c"]
    assert vc == exp_v, f"Lỗi: Bài {lid} có {vc} từ vựng (kỳ vọng: {exp_v})"

    cur.execute("SELECT COUNT(*) as c FROM exercises WHERE lesson_id = ?;", (lid,))
    exc = cur.fetchone()["c"]
    assert exc == exp_ex, f"Lỗi: Bài {lid} có {exc} bài tập (kỳ vọng: {exp_ex})"
    print(f"   ✅ Lesson {lid}: '{row['title'][:35]}...' -> {vc} vocab, {exc} exercises (PASSED)")

print("✅ TEST 1: Zero-Regression Check ĐẠT 100% PASS!")

# -----------------------------------------------------------------------------
# TEST 2: Bài 9 Metadata & 5 Learning Modules Check
# -----------------------------------------------------------------------------
print("\n🔍 TEST 2: Bài 9 Metadata & 5 Learning Modules Check...")
cur.execute("SELECT id, title, grammar_content FROM lessons WHERE id = 23;")
b9_row = cur.fetchone()
assert b9_row is not None, "Lỗi: Không tìm thấy Bài 9 (ID 23) trong CSDL"
assert "Bài 9: Du lịch - Perfekt & Präteritum" in b9_row["title"], f"Tiêu đề không đúng: {b9_row['title']}"

grammar = b9_row["grammar_content"] or ""
required_modules = [
    "Từ Vựng Thiên Nhiên & Du Lịch",
    "Cụm Động Từ + Danh Từ Du Lịch (Kollokationen)",
    "Nói Về Kỳ Nghỉ & Präteritum Của sein / haben",
    "Thì Quá Khứ Perfekt - Thì Quá Khứ Văn Nói (Trọng Tâm)",
    "Máy Tính Tra Cứu Partizip II Tương Tác"
]
for mod in required_modules:
    assert mod in grammar, f"Lỗi: Thiếu học phần '{mod}' trong nội dung ngữ pháp Bài 9"
    print(f"   ✅ Học phần '{mod}' hiện diện đầy đủ")

# Kiểm tra container cho 6 SVG diagram
for v in ["svg-v1-container", "svg-v2-container", "svg-v3-container", "svg-v4-container", "svg-v5-container", "svg-v6-container"]:
    assert v in grammar, f"Lỗi: Thiếu container #{v} trong HTML lý thuyết Bài 9"
    print(f"   ✅ Container sơ đồ #{v} hiện diện")

print("✅ TEST 2: Metadata & 5 Học phần Lý thuyết ĐẠT 100% PASS!")

# -----------------------------------------------------------------------------
# TEST 3: 50 Vocabulary Items & Plural Forms Check
# -----------------------------------------------------------------------------
print("\n🔍 TEST 3: Kiểm tra 50 từ vựng của Bài 9...")
cur.execute("SELECT * FROM vocabularies WHERE lesson_id = 23 ORDER BY id;")
vocab_list = cur.fetchall()
assert len(vocab_list) == 50, f"Lỗi: Bài 9 có {len(vocab_list)} từ vựng, yêu cầu đúng 50 từ!"

for v in vocab_list:
    assert v["german_word"], f"Lỗi: german_word rỗng ở ID {v['id']}"
    assert v["article"] in ["der", "die", "das", "-"], f"Lỗi: article không hợp lệ ở ID {v['id']}: {v['article']}"
    assert v["vietnamese_meaning"], f"Lỗi: vietnamese_meaning rỗng ở ID {v['id']}"
    assert v["example_sentence"], f"Lỗi: example_sentence rỗng ở ID {v['id']}"

print("   ✅ 50/50 từ vựng đầy đủ mạo từ, nghĩa tiếng Việt và câu ví dụ chuẩn.")
print("✅ TEST 3: Kiểm tra Từ vựng ĐẠT 100% PASS!")

# -----------------------------------------------------------------------------
# TEST 4: 100 Exercises Distribution across 14 Types Check
# -----------------------------------------------------------------------------
print("\n🔍 TEST 4: Kiểm tra 100 bài tập trên đúng 14 dạng...")
cur.execute("SELECT exercise_type, COUNT(*) as c FROM exercises WHERE lesson_id = 23 GROUP BY exercise_type;")
type_counts = {r["exercise_type"]: r["c"] for r in cur.fetchall()}

expected_14_types = {
    "trac_nghiem": 12,
    "dien_khuyet": 14,
    "dich_nghia_vd": 8,
    "dich_nghia_dv": 8,
    "noi_o": 8,
    "dien_tao_cau": 8,
    "nghe_dien": 8,
    "dich_cau_vd": 6,
    "dich_cau_dv": 6,
    "sap_xep_cau": 6,
    "chon_haben_sein": 4,
    "tim_loi_sai": 4,
    "viet_lai_perfekt": 4,
    "dung_sai": 4
}

total_ex = sum(type_counts.values())
assert total_ex == 100, f"Lỗi: Tổng số bài tập là {total_ex}, kỳ vọng 100!"

for t_key, exp_c in expected_14_types.items():
    actual_c = type_counts.get(t_key, 0)
    assert actual_c == exp_c, f"Lỗi dạng '{t_key}': có {actual_c} câu, kỳ vọng {exp_c} câu!"
    print(f"   ✅ Dạng '{t_key}': {actual_c}/{exp_c} câu (PASSED)")

print("✅ TEST 4: Phân bổ 14 dạng bài tập ĐẠT 100% PASS!")

# -----------------------------------------------------------------------------
# TEST 5: Pedagogical Quality & Zero-Bug Content Check
# -----------------------------------------------------------------------------
print("\n🔍 TEST 5: Kiểm tra chất lượng nội dung & Zero-Bug...")
cur.execute("SELECT * FROM exercises WHERE lesson_id = 23 ORDER BY id;")
all_exercises = cur.fetchall()

for ex in all_exercises:
    eid = ex["id"]
    q_text = ex["question"]
    ans = ex["correct_answer"]
    exp = ex["explanation"]
    extra_str = ex["extra_data"]

    # 1. Answer non-empty
    assert ans and ans.strip(), f"Lỗi Q{eid}: correct_answer rỗng!"

    # 2. Explanation non-empty
    assert exp and exp.strip(), f"Lỗi Q{eid}: explanation rỗng!"

    # 3. Extra data valid JSON and has translation
    assert extra_str, f"Lỗi Q{eid}: extra_data rỗng!"
    extra = json.loads(extra_str)
    assert extra.get("translation"), f"Lỗi Q{eid}: translation trong extra_data rỗng!"

    # 4. Zero YouTube links
    full_dump = f"{q_text} {ans} {exp} {extra_str}"
    assert "youtube.com" not in full_dump.lower() and "youtu.be" not in full_dump.lower(), f"Lỗi Q{eid}: Chứa link YouTube!"
    assert "<iframe" not in full_dump.lower(), f"Lỗi Q{eid}: Chứa thẻ iframe!"

    # 5. Audio text check
    if ex["exercise_type"] == "nghe_dien":
        audio = extra.get("audio_text")
        assert audio, f"Lỗi Q{eid}: Thiếu audio_text!"
        assert not audio.startswith("*") and not audio.startswith('"'), f"Lỗi Q{eid}: audio_text chứa ký tự markdown thừa: {audio}"

    # 6. Matching check
    if ex["exercise_type"] == "noi_o":
        pairs = extra.get("noi_o_pairs")
        assert pairs and len(pairs) == 4, f"Lỗi Q{eid}: noi_o_pairs phải có đúng 4 cặp!"

print("   ✅ 100/100 câu hỏi vượt qua toàn bộ tiêu chí chất lượng nội dung.")
print("✅ TEST 5: Chất lượng sư phạm & Zero-Bug ĐẠT 100% PASS!")

# -----------------------------------------------------------------------------
# TEST 6: JS Databases & Module Check (verbs_db, lexikon_db, perfekt_svg)
# -----------------------------------------------------------------------------
print("\n🔍 TEST 6: Kiểm tra các tệp JavaScript mở rộng...")

# 1. perfekt_svg.js
perfekt_svg_path = os.path.join(BASE_DIR, "static/js/perfekt_svg.js")
assert os.path.isfile(perfekt_svg_path), "Lỗi: Không tìm thấy static/js/perfekt_svg.js"
with open(perfekt_svg_path, "r", encoding="utf-8") as f:
    psvg_text = f.read()

for fn in ["renderSatzklammerSvg", "renderPartizipFlowchartSvg", "renderHabenSeinDecisionTreeSvg", "renderDonauRouteMapSvg", "renderTimelineSvg", "renderPartizipCalculatorSvg", "initPerfektSvgDiagrams", "renderExercisePerfektSvg"]:
    assert fn in psvg_text, f"Lỗi: Thiếu hàm {fn} trong perfekt_svg.js"
    print(f"   ✅ Hàm SVG '{fn}' hiện diện trong perfekt_svg.js")

# 2. verbs_db.js
verbs_db_path = os.path.join(BASE_DIR, "static/js/verbs_db.js")
with open(verbs_db_path, "r", encoding="utf-8") as f:
    vdb_text = f.read()
assert "Du lịch & Perfekt (Bài 9)" in vdb_text, "Lỗi: Thiếu nhóm Bài 9 trong verbs_db.js"
assert "übernachten" in vdb_text, "Lỗi: Thiếu übernachten trong verbs_db.js"
assert "fotografieren" in vdb_text, "Lỗi: Thiếu fotografieren trong verbs_db.js"

# 3. lexikon_db.js
lexikon_db_path = os.path.join(BASE_DIR, "static/js/lexikon_db.js")
with open(lexikon_db_path, "r", encoding="utf-8") as f:
    ldb_text = f.read()
assert "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)" in ldb_text, "Lỗi: Thiếu bộ lọc Thiên nhiên trong lexikon_db.js"
assert "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)" in ldb_text, "Lỗi: Thiếu bộ lọc Kỳ nghỉ trong lexikon_db.js"
assert "die Wälder" in ldb_text, "Lỗi: Thiếu die Wälder trong lexikon_db.js"
assert "die Reiseziele" in ldb_text, "Lỗi: Thiếu die Reiseziele trong lexikon_db.js"

# 4. index.html script tag
index_path = os.path.join(BASE_DIR, "templates/index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_text = f.read()
assert "perfekt_svg.js" in index_text, "Lỗi: templates/index.html chưa chèn thẻ script perfekt_svg.js"
assert "initPerfektSvgDiagrams" in index_text, "Lỗi: templates/index.html chưa gọi initPerfektSvgDiagrams khi chọn bài"
assert "sap_xep_cau" in index_text, "Lỗi: TYPE_LABELS chưa có sap_xep_cau"

print("✅ TEST 6: JavaScript & Module Khớp 100% ĐẠT PASS!")

# -----------------------------------------------------------------------------
# TEST 7: Arena Generator Integration Check
# -----------------------------------------------------------------------------
print("\n🔍 TEST 7: Kiểm tra tích hợp Đấu trường (arena_generator.py)...")
from arena_generator import LESSON_ORDER_MAP, build_arena_questions_for_user

assert 23 in LESSON_ORDER_MAP, "Lỗi: Lesson ID 23 chưa có trong LESSON_ORDER_MAP của arena_generator.py"
print("   ✅ Lesson 23 nằm trong LESSON_ORDER_MAP")

# Sinh câu hỏi đấu trường
arena_qs = build_arena_questions_for_user(user_id=1, count=15)
assert len(arena_qs) == 15, f"Lỗi sinh câu hỏi Đấu trường: có {len(arena_qs)} câu!"
print("   ✅ Sinh thành công 15 câu hỏi Đấu trường")
print("✅ TEST 7: Đấu trường ĐẠT 100% PASS!")

conn.close()

print("\n" + "=" * 70)
print("🏆 TOÀN BỘ 7/7 BÀI TEST QA BÀI 9 ĐẠT TIÊU CHUẨN 100% PASS! ZERO-BUG QUALITY ASSURED!")
print("=" * 70)
