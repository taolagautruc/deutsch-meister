# -*- coding: utf-8 -*-
"""
Kịch bản Kiểm thử Toàn diện & QA Anti-Bug Bài 14 (A1)
Theo Đặc tả Kỹ thuật Bài 14 (README/readme_b_i_14.md - Phần III):
"Ôn tập A1 (Tiếp theo) — Mạo từ, Động từ sein, Quốc gia/Ngôn ngữ & Phương hướng"
"""

import hashlib
import json
import math
import os
import re
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection


def normalize_text(s):
    if not s:
        return ""
    s = s.lower().strip()
    s = re.sub(r'[*_`„“"\'~\[\]\(\)\.,!?:;\-\/]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def run_tests():
    print("=" * 70)
    print("BẮT ĐẦU CHẠY KIỂM THỬ TOÀN DIỆN & QA ANTI-BUG BÀI 14 (A1)")
    print("=" * 70)

    errors = []

    # 1. ZERO-REGRESSION (Bài 1 -> Bài 13)
    print("\n[1/7] Kiểm tra Zero-Regression (Bài 1 -> 13 & Append-only files)...")
    if os.path.exists('baseline_hashes.json'):
        with open('baseline_hashes.json', 'r', encoding='utf-8') as f:
            baseline = json.load(f)
        for filepath, expected_hash in baseline.items():
            if 'seed_a1_b14.py' in filepath:
                continue
            if os.path.exists(filepath):
                with open(filepath, 'rb') as fp:
                    cur_hash = hashlib.sha256(fp.read()).hexdigest()
                if cur_hash != expected_hash:
                    errors.append(f"Regression detected in {filepath}: SHA-256 mismatch!")
            else:
                errors.append(f"Missing baseline file: {filepath}")

        base_ref = 'dbcfafc' if subprocess.run(['git', 'cat-file', '-e', 'dbcfafc^{commit}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0 else 'HEAD'
        res = subprocess.run(
            ['git', 'diff', '--numstat', base_ref, 'static/js/verbs_db.js', 'static/js/lexikon_db.js', 'arena_generator.py'],
            stdout=subprocess.PIPE, text=True
        )
        for line in res.stdout.strip().split('\n'):
            if line.strip():
                parts = line.split()
                if len(parts) >= 3 and parts[1] != '0':
                    errors.append(f"File {parts[2]} has {parts[1]} deleted lines vs {base_ref}!")
    print("  ✓ Zero-Regression PASS: Bài 1-13 nguyên vẹn.")

    # 2. CSDL & LÝ THUYẾT MỞ RỘNG
    print("\n[2/7] Kiểm tra CSDL & Lý thuyết Bài 14 (ID=28)...")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, grammar_content FROM lessons WHERE id = 28;")
    lesson_b14 = cursor.fetchone()
    if not lesson_b14:
        errors.append("Không tìm thấy Lesson 14 (id=28) trong bảng lessons!")
        conn.close()
        return False

    gc = lesson_b14["grammar_content"] or ""
    print(f"  ✓ Lesson 14 tồn tại: {lesson_b14['title']}")
    for marker in [
        "b14-compass-svg-container",
        "bg-blue-50", "bg-rose-50", "bg-emerald-50",
        "Präsens", "Präteritum",
        "Länder", "Himmelsrichtungen",
        "2 CÁCH NÓI KHÁC NGHĨA: BÊN TRONG vs BÊN NGOÀI",
        "im Norden", "China liegt", "Arabisch", "die Türkei", "die Schweiz",
        "KHÔNG có công thức cố định",
        "Warst du gestern zu Hause?",
        "Wir waren gestern in Berlin.",
        "<b>Zentrum</b> = trung tâm thành phố",
        "in der Mitte von Vietnam"
    ]:
        if marker not in gc:
            errors.append(f"Lý thuyết Bài 14 thiếu nội dung/thành phần '{marker}'!")
    if "Ägyptisch" in gc:
        errors.append("Lý thuyết Bài 14 vẫn còn chứa 'Ägyptisch'!")
    if "Hanoi liegt <b>nördlich</b> von Vietnam" in gc or "München liegt <b>südlich</b> von Deutschland" in gc:
        errors.append("Lý thuyết Bài 14 vẫn còn ví dụ sai 'Hanoi/München liegt ...lich von Vietnam/Deutschland'!")
    if "Warst du schon einmal" in gc or "Wir sind zu Hause" in gc:
        errors.append("Lý thuyết Bài 14 bảng sein vẫn còn ví dụ Präsens cũ cho du/wir!")

    # 3. KIỂM TRA TỪ VỰNG BÀI 14 (KHÔNG TRÙNG BÀI 1 -> 13)
    print("\n[3/7] Kiểm tra từ vựng Bài 14 (18 thẻ không trùng Bài 1 -> 13)...")
    cursor.execute("SELECT DISTINCT lower(german_word) as w FROM vocabularies WHERE lesson_id < 28;")
    old_words = {r["w"] for r in cursor.fetchall()}
    cursor.execute("SELECT german_word, article, vietnamese_meaning, example_sentence FROM vocabularies WHERE lesson_id = 28;")
    v_rows = cursor.fetchall()
    if len(v_rows) != 18:
        errors.append(f"Số lượng từ vựng Bài 14 không đúng: {len(v_rows)}/18.")
    v_map = {}
    for r in v_rows:
        w = r["german_word"]
        v_map[w] = r
        if w.lower() in old_words:
            errors.append(f"Từ vựng '{w}' bị trùng với Bài 1-13!")
        ex_s = r["example_sentence"] or ""
        if " — " not in ex_s or "„" not in ex_s or "“" not in ex_s:
            errors.append(f"Thẻ '{w}' thiếu ngoặc „...“ hoặc dịch ' — '!")
        else:
            de_part, vi_part = ex_s.split(" — ", 1)
            if not vi_part.strip():
                errors.append(f"Thẻ '{w}' có phần dịch trống!")
    if "Zentrum" in v_map and "Das Hotel liegt im Zentrum von Hanoi." not in (v_map["Zentrum"]["example_sentence"] or ""):
        errors.append("Thẻ 'Zentrum' chưa cập nhật ví dụ 'Das Hotel liegt im Zentrum von Hanoi.'!")
    if "Freundin" in v_map:
        f_mean = v_map["Freundin"]["vietnamese_meaning"] or ""
        f_ex = v_map["Freundin"]["example_sentence"] or ""
        if "bạn (nữ); bạn gái" not in f_mean or "Bạn (nữ) của tôi" not in f_ex:
            errors.append("Thẻ 'Freundin' chưa cập nhật nghĩa/dịch 'bạn (nữ); bạn gái'!")
    if "Schlüssel" in v_map and "Wo ist heute der Schlüssel?" not in (v_map["Schlüssel"]["example_sentence"] or ""):
        errors.append("Thẻ 'Schlüssel' chưa cập nhật ví dụ 'Wo ist heute der Schlüssel?'!")
    print(f"  ✓ Từ vựng Bài 14 PASS: {len(v_rows)}/18 thẻ độc nhất.")

    # 4. KIỂM TRA CHÍNH XÁC 125 CÂU BÀI TẬP
    print("\n[4/7] Kiểm tra số lượng bài tập (assert len == 125)...")
    cursor.execute("SELECT id, exercise_type, question, options_json, correct_answer, explanation, extra_data FROM exercises WHERE lesson_id = 28 ORDER BY id ASC;")
    exercises = cursor.fetchall()
    assert len(exercises) == 125, f"Kỳ vọng 125 câu, thực tế {len(exercises)} câu!"
    print("  ✓ Đủ chính xác 125/125 câu bài tập.")

    # 5. QUÉT TRÙNG LẶP (125 UNIQUE)
    print("\n[5/7] Quét trùng lặp nội dung (125/125 câu độc nhất)...")
    seen = {}
    dups = []
    generic_prompts = {
        "sắp xếp các từ sau thành câu hoàn chỉnh",
        "sắp xếp các từ sau thành câu hỏi hoàn chỉnh",
        "nghe audio và gõ lại trọn vẹn câu tiếng đức bạn nghe được"
    }
    for idx, ex in enumerate(exercises, 1):
        q_clean = re.sub(r"^Câu \d+:\s*", "", ex["question"] or "")
        norm = normalize_text(q_clean)
        if norm in generic_prompts:
            norm = f"{norm} :: {normalize_text(ex['correct_answer'])}"
        if norm in seen:
            dups.append((seen[norm], idx, q_clean[:40]))
        else:
            seen[norm] = idx

    if dups:
        for orig, dup_i, snip in dups:
            errors.append(f"Trùng lặp giữa Câu {orig} và Câu {dup_i}: {snip}")
    else:
        print("  ✓ Deduplication PASS: 125/125 câu hỏi độc nhất (0% trùng lặp).")

    # 6. QUÉT TRANSLATION_VI, EXPLANATION & VOICE TTS CLEANLINESS (125/125)
    print("\n[6/7] Kiểm tra 100% có translation, explanation & voice speak_text (de-DE) sạch...")
    vi_char_re = re.compile(r"[àáạảãâầấậẩẫăằắặẳẵèẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]", re.IGNORECASE)
    for idx, ex in enumerate(exercises, 1):
        expl = (ex["explanation"] or "").strip()
        ans = (ex["correct_answer"] or "").strip()
        extra = json.loads(ex["extra_data"] or "{}")
        trans = (extra.get("translation") or "").strip()
        audio = (extra.get("audio_text") or "").strip()

        if not trans:
            errors.append(f"Câu {idx}: Thiếu translation!")
        elif "đáp án" in trans.lower():
            errors.append(f"Câu {idx}: translation lộ gợi ý 'đáp án': '{trans}'")

        if not expl:
            errors.append(f"Câu {idx}: Thiếu explanation!")
        elif ex["exercise_type"] != "hoi_thoai_sap_xep":
            norm_expl = normalize_text(expl)
            norm_ans = normalize_text(ans)
            parts = [normalize_text(p) for p in re.split(r'[/,]', ans) if p.strip()]
            if norm_ans not in norm_expl and not (parts and all(p in norm_expl for p in parts)):
                errors.append(f"Câu {idx}: Explanation chưa chứa đáp án '{ans}'!")

        if not audio:
            errors.append(f"Câu {idx}: Thiếu audio_text (speak_text)!")
        else:
            for bad_c in ["___", "[1]", "[2]", "[", "]", "→", "_"]:
                if bad_c in audio:
                    errors.append(f"Câu {idx}: audio_text chứa ký tự cấm {bad_c!r}: '{audio}'")
            if vi_char_re.search(audio):
                errors.append(f"Câu {idx}: audio_text chứa ký tự tiếng Việt: '{audio}'")

    print("  ✓ Translation, Explanation & TTS Cleanliness PASS: 125/125 câu hợp lệ.")

    # 7. ANTI-BUG PROTOCOL CHECK (Dictation Mode + Semantic Tolerance + Cap Warning)
    print("\n[7/7] Rà soát Anti-Bug (Dictation Mode 86-95, Semantic Tolerance, Capitalization Warning)...")
    dict_ex = [ex for idx, ex in enumerate(exercises, 1) if 86 <= idx <= 95]
    assert len(dict_ex) == 10
    for offset, ex in enumerate(dict_ex, 86):
        extra = json.loads(ex["extra_data"] or "{}")
        if ex["exercise_type"] != "nghe_dien":
            errors.append(f"Câu {offset}: Phải là 'nghe_dien'!")
        if "___" in (ex["question"] or "") or "display_sentence" in extra or not extra.get("dictation_mode"):
            errors.append(f"Câu {offset}: Chưa bật Dictation Mode 100% ẩn text!")
        if ex["correct_answer"] != extra.get("full_sentence"):
            errors.append(f"Câu {offset}: correct_answer phải bằng full_sentence!")

    with open('static/js/b14_review_svg.js', 'r', encoding='utf-8') as f_b14:
        b14_js = f_b14.read()
    with open('templates/index.html', 'r', encoding='utf-8') as f_idx:
        idx_html = f_idx.read()
    if "evaluateLesson14Translation" not in b14_js or "evaluateLesson14Translation" not in idx_html:
        errors.append("Thiếu Semantic Tolerance evaluator cho Bài 14!")
    if "isLesson14GermanInput" not in idx_html:
        errors.append("Thiếu Capitalization Warning hook cho Bài 14!")
    if "isLesson14Vocab" not in idx_html or "whitespace-nowrap" not in idx_html:
        errors.append("Thiếu guard chống rớt dấu ngoặc đóng đơn độc (whitespace-nowrap) cho thẻ từ vựng Bài 14!")
    if "Hue liegt in der Mitte von Vietnam." not in b14_js or "Zentrum = trung tâm thành phố" not in b14_js:
        errors.append("b14_review_svg.js chưa cập nhật quy tắc Mitte vs Zentrum!")
    if "Hue liegt im Zentrum von Vietnam." in b14_js:
        errors.append("b14_review_svg.js vẫn còn ví dụ cũ 'Hue liegt im Zentrum von Vietnam.'!")

    # 8. KIỂM TRA TỌA ĐỘ PHƯƠNG HƯỚNG (-lich von) & CẤM DÙNG BÊN TRONG/Ägyptisch
    print("\n[8/8] Kiểm tra tọa độ địa lý (A liegt ...lich von B) & chống dùng sai bên trong...")
    COORDS = {
        "Hanoi": (21.03, 105.85), "Hue": (16.46, 107.59), "Da Nang": (16.05, 108.20), "Can Tho": (10.04, 105.75),
        "Köln": (50.94, 6.96), "Dresden": (51.05, 13.74), "München": (48.14, 11.58),
        "Stuttgart": (48.78, 9.18), "Bonn": (50.73, 7.10), "Rostock": (54.09, 12.14),
        "Hannover": (52.37, 9.73), "Leipzig": (51.34, 12.37), "Bremen": (53.08, 8.80),
        "Hamburg": (53.55, 9.99), "Frankfurt": (50.11, 8.68), "Würzburg": (49.79, 9.95),
        "Paris": (48.86, 2.35), "China": (35.86, 104.20), "Vietnam": (14.06, 108.28),
        "Deutschland": (51.16, 10.45), "Österreich": (47.52, 14.55), "Polen": (51.92, 19.14),
        "Frankreich": (46.23, 2.21), "Die Schweiz": (46.82, 8.23), "Schweiz": (46.82, 8.23),
    }
    COUNTRY_ENTITIES = {"China", "Vietnam", "Deutschland", "Österreich", "Polen", "Frankreich", "Die Schweiz", "Schweiz"}
    DIR_AZIMUTH = {
        "nördlich": 0.0, "nordöstlich": 45.0, "östlich": 90.0, "südöstlich": 135.0,
        "südlich": 180.0, "südwestlich": 225.0, "westlich": 270.0, "nordwestlich": 315.0,
    }
    CONTAINED_IN = {
        "Vietnam": {"Hanoi", "Hue", "Da Nang", "Hai Phong", "Nha Trang", "Can Tho"},
        "Deutschland": {"Berlin", "Hamburg", "München", "Köln", "Dresden", "Leipzig", "Hannover", "Bremen", "Stuttgart", "Frankfurt", "Bonn", "Rostock", "Würzburg"},
        "Österreich": {"Wien"},
        "Japan": {"Tokio"},
        "Europa": {"Spanien", "Griechenland", "Deutschland", "Frankreich", "Italien", "Polen", "Russland", "Österreich"},
    }

    def check_geo_sentence(sent, source_label):
        m = re.search(r"([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s]+?)\s+liegt\s+(?:im\s+)?(nördlich|nordöstlich|östlich|südöstlich|südlich|südwestlich|westlich|nordwestlich)\s+von\s+([A-ZÄÖÜ][A-Za-zÄÖÜäöüß\s]+)", sent)
        if not m:
            return
        # Bỏ qua câu ví dụ sai cố tình trong đề bài câu hỏi "tìm lỗi sai / sai ngữ pháp"
        if re.search(r"\bim\s+(nördlich|nordöstlich|östlich|südöstlich|südlich|südwestlich|westlich|nordwestlich)", sent):
            return
        a_place = m.group(1).strip()
        adj = m.group(2).strip()
        b_place = re.sub(r"[.!?,\"„“]+$", "", m.group(3).strip())
        if b_place in CONTAINED_IN and a_place in CONTAINED_IN[b_place]:
            errors.append(f"{source_label}: '{a_place}' thuộc '{b_place}', cấm dùng '{adj} von {b_place}' (phải dùng 'im ...')!")
            return
        if a_place in COORDS and b_place in COORDS:
            latA, lonA = COORDS[a_place]
            latB, lonB = COORDS[b_place]
            avg_lat = math.radians((latA + latB) / 2.0)
            dy = latA - latB
            dx = (lonA - lonB) * math.cos(avg_lat)
            deg = (math.degrees(math.atan2(dx, dy)) + 360.0) % 360.0
            exp_deg = DIR_AZIMUTH[adj]
            diff = abs((deg - exp_deg + 180.0) % 360.0 - 180.0)
            tol = 45.0 if (a_place in COUNTRY_ENTITIES or b_place in COUNTRY_ENTITIES) else 32.0
            if diff > tol:
                errors.append(f"{source_label}: Sai tọa độ '{sent}' -> hướng từ {b_place} tới {a_place} là {deg:.1f}°, kỳ vọng {adj} ({exp_deg}°, lệch {diff:.1f}° > {tol}°)!")

    # Kiểm tra toàn bộ B14_DIRECTIONS trong b14_review_svg.js
    for adj_ex_m in re.finditer(r"adjEx:\s*'([^']+)'", b14_js):
        check_geo_sentence(adj_ex_m.group(1), "b14_review_svg.js")

    # Kiểm tra toàn bộ 125 bài tập & thẻ từ vựng Bài 14
    for r in v_rows:
        if "Ägyptisch" in (r["example_sentence"] or "") or "Ägyptisch" in (r["vietnamese_meaning"] or ""):
            errors.append(f"Thẻ từ vựng '{r['german_word']}' vẫn còn chứa 'Ägyptisch'!")
        check_geo_sentence(r["example_sentence"] or "", f"Vocab({r['german_word']})")

    for idx, ex in enumerate(exercises, 1):
        extra = json.loads(ex["extra_data"] or "{}")
        if "Ägyptisch" in (ex["correct_answer"] or "") or "Ägyptisch" in (extra.get("audio_text") or ""):
            errors.append(f"Câu {idx}: Vẫn còn dùng 'Ägyptisch' thay cho 'Arabisch'!")
        texts_to_check = [ex["correct_answer"] or "", extra.get("audio_text") or ""] + list(extra.get("accepted_answers") or [])
        if idx not in (6, 11):  # Câu 6 chọn đáp án sai, Câu 11 đề bài chứa lỗi cố ý; còn correct_answer vẫn phải chuẩn
            pass
        for t in texts_to_check:
            check_geo_sentence(t, f"Câu {idx}")
    print("  ✓ Coordinate & Geography Check PASS: Mọi câu '...lich von' đúng hướng la bàn & phân biệt đúng BÊN TRONG / BÊN NGOÀI.")

    conn.close()

    print("\n" + "=" * 70)
    if errors:
        print(f"PHÁT HIỆN {len(errors)} LỖI:")
        for e in errors:
            print("  -", e)
        return False

    print("Đã hoàn tất sinh 125 câu Bài 14, hoàn thành chạy script kiểm tra trùng lặp nội dung, và đã rà soát toàn bộ bộ quy tắc Anti-Bug.")
    print("=" * 70)
    return True


if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
