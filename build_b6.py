import os
import sys
import json
import re
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. Đọc nội dung đặc tả Bài 6
spec_path = os.path.join(BASE_DIR, 'templates/c_t_k_thu_t_b_i_6_dativ_gi_i_t_ph_ng_ti_n_s_th_t_ng_y_th_ng_n_m_100_b_i_t_p_qa_zero_bug.md')
with open(spec_path, 'r', encoding='utf-8') as f:
    spec_text = f.read()

# 2. Lấy 45 từ vựng Bài 6 từ static/js/lexikon_db.js
node_cmd = """
const fs = require('fs');
let content = fs.readFileSync('static/js/lexikon_db.js', 'utf8');
content = content.replace('const GERMAN_LEXIKON_DB', 'global.GERMAN_LEXIKON_DB');
eval(content);
const b6 = global.GERMAN_LEXIKON_DB.filter(x => x.category && x.category.includes('Bài 6'));
console.log(JSON.stringify(b6));
"""
res = subprocess.run(['node', '-e', node_cmd], capture_output=True, text=True)
b6_vocab_list = json.loads(res.stdout)
print(f"✅ Đã trích xuất {len(b6_vocab_list)} từ vựng Bài 6 từ lexikon_db.js")

# 3. Phân tích 100 câu hỏi từ đặc tả
q_splits = list(re.finditer(r'\n(\d+)\.\s+\*\*Câu\s+(\d+)([^\*]*)\*\*:\s*(.*?)(?=\n\d+\.\s+\*\*Câu|\n## PHẦN 4|$)', spec_text, re.DOTALL))
print(f"✅ Đã tìm thấy {len(q_splits)} khối câu hỏi trong file đặc tả.")

def clean_explanation_text(exp):
    if not exp:
        return ""
    # Cắt bỏ các section header bị dính do regex greedy
    exp = re.split(r'\n\s*---\s*|\n\s*####', exp)[0].strip()
    # Chuyển đổi toàn bộ ký hiệu LaTeX sang Unicode mũi tên
    exp = exp.replace(r'$\rightarrow$', '→')
    exp = exp.replace(r'$\longleftrightarrow$', '⇄')
    exp = exp.replace(r'\rightarrow', '→')
    exp = exp.replace(r'\longleftrightarrow', '⇄')
    # Bóc tách các công thức $...$ còn sót
    exp = re.sub(r'\$([^\$]+)\$', r'\1', exp)
    exp = exp.replace('$', '')
    exp = re.sub(r'[*_`]', '', exp).strip()
    return exp

def clean_question_text(q_num, raw_p):
    clean_p = re.sub(r'\*\s*\(Gợi ý:[^\)]*\)\s*\*?', '', raw_p).strip()
    clean_p = re.sub(r'\*+', '', clean_p).strip()
    # Loại bỏ gợi ý công thức bị lộ trong ngoặc như (`zu + der`), (`von + dem`), (`bei + dem`)
    clean_p = re.sub(r'\s*\(\s*`?[a-zäöüß]+\s*\+\s*[a-zäöüß]+`?\s*\)', '', clean_p, flags=re.IGNORECASE).strip()
    # Loại bỏ bản dịch tiếng Việt bị lộ trong ngoặc đơn trên đề bài
    clean_p = re.sub(r'\s*\(của\s+cô\s+giáo\s+chúng\s+tôi\)', '', clean_p, flags=re.IGNORECASE).strip()
    clean_p = re.sub(r'\s*\(những\s+người\s+bạn\)', '', clean_p, flags=re.IGNORECASE).strip()
    clean_p = clean_p.replace('`', '')
    return f"Câu {q_num}: {clean_p}"

parsed_exercises = []
for idx, m in enumerate(q_splits):
    q_num = int(m.group(2))
    q_title = m.group(3).strip()
    body = m.group(4).strip()
    
    if 1 <= q_num <= 18:
        ex_type = "trac_nghiem"
        pts = 15
    elif 19 <= q_num <= 33:
        ex_type = "dien_khuyet"
        pts = 15
    elif 34 <= q_num <= 45:
        ex_type = "dich_nghia_vd"
        pts = 15
    elif 46 <= q_num <= 57:
        ex_type = "dich_nghia_dv"
        pts = 15
    elif 58 <= q_num <= 67:
        ex_type = "noi_o"
        pts = 25
    elif 68 <= q_num <= 77:
        ex_type = "dien_tao_cau"
        pts = 20
    elif 78 <= q_num <= 86:
        ex_type = "nghe_dien"
        pts = 20
    elif 87 <= q_num <= 93:
        ex_type = "dich_cau_vd"
        pts = 25
    else:
        ex_type = "dich_cau_dv"
        pts = 25

    if ex_type == "trac_nghiem":
        p_match = re.search(r'^(.*?)(?=\n\s*\*\s*Đáp án:)', body, re.DOTALL)
        raw_p = p_match.group(1).strip() if p_match else body.split('\n')[0].strip()
        question = clean_question_text(q_num, raw_p)
        
        opts = []
        correct = None
        opt_matches = re.findall(r'`([A-D]\.\s*[^`]+)`(?:\s*\((Đúng)\))?', body)
        for opt_str, is_c in opt_matches:
            val = re.sub(r'^[A-D]\.\s*', '', opt_str).strip()
            opts.append(val)
            if is_c == 'Đúng':
                correct = val
        options_json = json.dumps(opts, ensure_ascii=False)
        correct_answer = correct
        
        trans_m = re.search(r'Dịch nghĩa câu:\s*[\*"\']*(.*?)[\*"\']*\n', body)
        trans = trans_m.group(1).strip() if trans_m else ''
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        extra_data = {"translation": trans}
        if q_num in [1, 2]:
            extra_data["dynamic_dativ_transport_quiz"] = True
        elif q_num in [9, 10]:
            extra_data["dynamic_dativ_position_quiz"] = True
        elif q_num in [12, 13, 14, 15]:
            extra_data["dynamic_ordinal_date_quiz"] = True

    elif ex_type == "dien_khuyet":
        raw_p = body.split('\n')[0].strip()
        question = clean_question_text(q_num, raw_p)
        options_json = None
        
        ans_m = re.search(r'Đáp án chấp nhận:\s*(`\[.*?\]`|\[.*?\])', body)
        acc_ans = json.loads(ans_m.group(1).replace('`', '')) if ans_m else []
        correct_answer = acc_ans[0]
        
        trans_m = re.search(r'Dịch nghĩa câu:\s*[\*"\']*(.*?)[\*"\']*\n', body)
        trans = trans_m.group(1).strip() if trans_m else ''
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        extra_data = {"accepted_answers": acc_ans, "translation": trans}
        if q_num in [27, 28, 29, 30, 31]:
            extra_data["dynamic_ordinal_date_quiz"] = True
        elif q_num in [22, 23, 24, 32]:
            extra_data["dynamic_dativ_position_quiz"] = True

    elif ex_type == "dich_nghia_vd":
        raw_p = body.split('\n')[0].strip()
        question = clean_question_text(q_num, raw_p)
        options_json = None
        
        ans_m = re.search(r'Đáp án chấp nhận:\s*(`\[.*?\]`|\[.*?\])', body)
        acc_ans = json.loads(ans_m.group(1).replace('`', '')) if ans_m else []
        correct_answer = acc_ans[0]
        
        clean_p_trans = re.sub(r'\*+', '', raw_p).strip()
        trans_m = re.search(r'["“](.*?)["”]', clean_p_trans)
        trans = trans_m.group(1) if trans_m else clean_p_trans
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        extra_data = {"accepted_answers": acc_ans, "translation": f"{trans} = {correct_answer}"}

    elif ex_type == "dich_nghia_dv":
        raw_p = body.split('\n')[0].strip()
        question = clean_question_text(q_num, raw_p)
        options_json = None
        
        ans_m = re.search(r'Đáp án chấp nhận:\s*(`\[.*?\]`|\[.*?\])', body)
        acc_ans = json.loads(ans_m.group(1).replace('`', '')) if ans_m else []
        correct_answer = acc_ans[0]
        
        clean_p_trans = re.sub(r'\*+', '', raw_p).strip()
        trans_m = re.search(r'[„"“](.*?)[”"]', clean_p_trans)
        de_w = trans_m.group(1) if trans_m else clean_p_trans
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        extra_data = {"accepted_answers": acc_ans, "translation": f"{de_w} = {correct_answer}"}

    elif ex_type == "noi_o":
        title_topic_m = re.search(r'Bài nối ô \d+\s*—\s*([^)]+)', q_title)
        topic = title_topic_m.group(1).replace('`', '') if title_topic_m else "Nối ô"
        question = f"Câu {q_num} (Bài nối ô {q_num - 57}): Nối các ô ở cột trái với ô tương ứng ở cột phải ({topic}):"
        options_json = None
        
        pair_matches = re.findall(r'\*\s*`([^`]+)`\s*\$\\longleftrightarrow\$\s*`([^`]+)`', body)
        pairs = [{"left": l.strip(), "right": r.strip()} for l, r in pair_matches]
        correct_answer = ", ".join([f"{p['left']} - {p['right']}" for p in pairs])
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else "Nối chính xác 100% cả 4 cặp tương ứng.")
        
        trans = f"Bài tập nối 4 cặp thẻ chuẩn kiến thức {topic}."
        extra_data = {"noi_o_pairs": pairs, "translation": trans}

    elif ex_type == "dien_tao_cau":
        khung_m = re.search(r'Khung câu hiển thị:\s*`([^`]+)`', body)
        khung = khung_m.group(1) if khung_m else ''
        display_q = khung.replace('[1]', '___').replace('[2]', '___')
        
        o1_m = re.search(r'Ô 1\s*=\s*(`\[.*?\]`|\[.*?\])', body)
        o2_m = re.search(r'Ô 2\s*=\s*(`\[.*?\]`|\[.*?\])', body)
        o1_list = json.loads(o1_m.group(1).replace('`', '')) if o1_m else []
        o2_list = json.loads(o2_m.group(1).replace('`', '')) if o2_m else []
        correct_answer = f"{o1_list[0]} / {o2_list[0]}"
        
        acc = []
        for a1 in o1_list:
            for a2 in o2_list:
                acc.append(f"{a1} / {a2}")
                acc.append(f"{a1}/{a2}")
                
        line1 = body.split('\n')[0]
        trans_m = re.search(r'[\*“\"”](.*?)[\*“\"”]', line1)
        trans = trans_m.group(1) if trans_m else ''
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        question = f"Câu {q_num}: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): '{display_q}'"
        options_json = None
        extra_data = {"accepted_answers": acc, "translation": trans}

    elif ex_type == "nghe_dien":
        audio_m = re.search(r'audio_text`?:\s*[\*"]*([^"\*\n]+)[\*"]*', body)
        disp_m = re.search(r'display_sentence`?:\s*[\*"]*([^"\*\n]+)[\*"]*', body)
        hint_m = re.search(r'hint_vi`?:\s*[\*"]*([^"\*\n]+)[\*"]*', body)
        acc_m = re.search(r'accepted_answers`?:\s*(`\[.*?\]`|\[.*?\])', body)
        
        audio = audio_m.group(1).strip() if audio_m else ''
        disp = disp_m.group(1).strip() if disp_m else ''
        trans = hint_m.group(1).strip() if hint_m else ''
        acc = json.loads(acc_m.group(1).replace('`', '')) if acc_m else []
        correct_answer = acc[0]
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        question = f"Câu {q_num} [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: '{disp}'"
        options_json = None
        extra_data = {
            "audio_text": audio,
            "display_sentence": disp,
            "accepted_answers": acc,
            "translation": trans
        }

    elif ex_type == "dich_cau_vd":
        line1 = body.split('\n')[0].strip()
        question = clean_question_text(q_num, line1)
        options_json = None
        
        acc_block_m = re.search(r'accepted_answers`?:\s*(.*?)(?=\n\s*\*?\s*Giải thích:|\n\s*\*?\s*Dịch:|$)', body, re.DOTALL)
        acc = re.findall(r'["“]([^"”]+)["”]', acc_block_m.group(1)) if acc_block_m else []
        correct_answer = " / ".join(acc[:4]) if acc else ""
        
        clean_p_trans = re.sub(r'\*+', '', line1).strip()
        trans_m = re.search(r'["“](.*?)["”]', clean_p_trans)
        trans = trans_m.group(1) if trans_m else clean_p_trans
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        extra_data = {"accepted_answers": acc, "translation": trans}

    elif ex_type == "dich_cau_dv":
        line1 = body.split('\n')[0].strip()
        question = clean_question_text(q_num, line1)
        options_json = None
        
        acc_block_m = re.search(r'accepted_answers`?:\s*(.*?)(?=\n\s*\*?\s*Giải thích:|\n\s*\*?\s*Dịch:|$)', body, re.DOTALL)
        acc = re.findall(r'["“]([^"”]+)["”]', acc_block_m.group(1)) if acc_block_m else []
        correct_answer = " / ".join(acc[:4]) if acc else ""
        
        clean_p_trans = re.sub(r'\*+', '', line1).strip()
        trans_m = re.search(r'[„"“](.*?)[”"]', clean_p_trans)
        de_w = trans_m.group(1) if trans_m else clean_p_trans
        
        exp_m = re.search(r'Giải thích:\s*(.*?)(?=\n\s*\*|\n\s*Dịch|$)', body, re.DOTALL)
        explanation = clean_explanation_text(exp_m.group(1) if exp_m else '')
        
        extra_data = {"accepted_answers": acc, "translation": de_w}

    # Final safety sanitation
    explanation = clean_explanation_text(explanation)
    parsed_exercises.append({
        "q_num": q_num,
        "type": ex_type,
        "question": question,
        "options_json": options_json,
        "correct_answer": correct_answer,
        "explanation": explanation,
        "exp_reward": pts,
        "extra_data": extra_data
    })

print(f"✅ Đã parse thành công {len(parsed_exercises)} bài tập!")

# 4. Tạo Grammar HTML
grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 6 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Dativ • Giới Từ • Phương Tiện • Số Thứ Tự & Ngày Tháng (Bài 6)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 120 phút • ⚡ 1800+ EXP • 🎯 100 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Dativ - Giới Từ Trong Dativ - Phương Tiện Giao Thông - Số Thứ Tự - Ngày Tháng Năm (Orientierung)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Hệ thống toàn diện <b>Cách 3 (Dativ)</b>; làm chủ quy tắc biến đổi mạo từ xác định, không xác định, phủ định và đại ma trận mạo từ sở hữu 9 ngôi; nằm lòng quy tắc đặc biệt <i>Plural + -n</i>; ghi nhớ nhóm giới từ luôn đi với Dativ (<i>aus, bei, mit, nach, seit, von, zu</i>) và 9 giới từ chỉ vị trí trả lời câu hỏi <i>Wo?</i>; làm chủ cấu trúc phương tiện <i>mit + Dativ</i> đối chiếu với ngoại lệ <i>zu Fuß</i>; đọc viết thành thạo <b>Số thứ tự (Ordinalzahlen)</b> từ 1 đến 31 ở cả 2 cách Nominativ và Dativ; diễn đạt chuẩn xác <b>Ngày - Tháng - Năm</b> (<i>der..., am..., vom... bis zum...</i>); và làm chủ các động từ thông dụng đi với Dativ (<i>helfen, gefallen</i>).
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: CÁCH 3 TRONG TIẾNG ĐỨC (DER DATIV) & MA TRẬN MẠO TỪ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Cách 3 Trong Tiếng Đức (Der Dativ) & Hệ Thống Ma Trận Mạo Từ</h4>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>💡</span> 3 Trường Hợp Sử Dụng Cách 3 (Dativ):</p>
                <ol class="list-decimal pl-5 space-y-1 text-slate-700">
                    <li><b>Sau các giới từ bắt buộc đi với Dativ:</b> <i>mit, nach, aus, zu, von, bei, seit, ab, gegenüber</i>.</li>
                    <li><b>Sau 9 giới từ chỉ vị trí (Wechselpräpositionen) khi trả lời cho câu hỏi <i>Wo?</i> (Ở đâu? - trạng thái tĩnh):</b> <i>in, an, auf, neben, vor, hinter, über, unter, zwischen</i>.</li>
                    <li><b>Làm tân ngữ gián tiếp (người nhận hành động / Wem?) hoặc đi sau các động từ Dativ:</b> <i>helfen, gefallen, danken, gehören</i>.</li>
                </ol>
            </div>

            <!-- Bảng 1.1: Quy tắc vàng biến đổi mạo từ Dativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>👑</span> 1.1. Ma Trận Đối Chiếu 3 Cách (Nominativ – Akkusativ – Dativ)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Giống Danh Từ</th>
                                <th class="p-3">Loại Mạo Từ</th>
                                <th class="p-3 text-center">Cách 1: Nominativ<br><span class="text-xs font-normal text-slate-500">(Chủ ngữ)</span></th>
                                <th class="p-3 text-center">Cách 4: Akkusativ<br><span class="text-xs font-normal text-slate-500">(Tân ngữ trực tiếp)</span></th>
                                <th class="p-3 text-center bg-amber-100/60 text-amber-900">Cách 3: Dativ<br><span class="text-xs font-bold text-amber-700">(Wo? / Phương tiện / Wem?)</span></th>
                                <th class="p-3">Ví Dụ Chuẩn (Dativ)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-blue-600">Maskulinum (der)</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">der<br>ein<br>kein</td>
                                <td class="p-3 text-center">de<b>n</b><br>eine<b>n</b><br>keine<b>n</b></td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-50/50">de<b>m</b><br>eine<b>m</b><br>keine<b>m</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>dem</b> Bus / auf <b>einem</b> Tisch</span>
                                        <button onclick="speakGerman('mit dem Bus auf einem Tisch')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-rose-600">Femininum (die)</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">die<br>eine<br>keine</td>
                                <td class="p-3 text-center">die<br>eine<br>keine</td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-50/50">de<b>r</b><br>eine<b>r</b><br>keine<b>r</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>der</b> U-Bahn / neben <b>einer</b> Bank</span>
                                        <button onclick="speakGerman('mit der U-Bahn neben einer Bank')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-emerald-600">Neutrum (das)</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">das<br>ein<br>kein</td>
                                <td class="p-3 text-center">das<br>ein<br>kein</td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-50/50">de<b>m</b><br>eine<b>m</b><br>keine<b>m</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>dem</b> Auto / vor <b>einem</b> Haus</span>
                                        <button onclick="speakGerman('mit dem Auto vor einem Haus')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/20">
                                <td class="p-3 font-bold text-purple-600">Plural (die + -n) ⚠️</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">die<br>—<br>keine</td>
                                <td class="p-3 text-center">die<br>—<br>keine</td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-100/60">de<b>n</b> + ...<b>n</b><br>— + ...<b>n</b><br>keine<b>n</b> + ...<b>n</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>den</b> Busse<b>n</b> / mit Kinder<b>n</b></span>
                                        <button onclick="speakGerman('mit den Bussen mit Kindern')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng 1.2: Đại ma trận Mạo từ sở hữu 9 ngôi ở Dativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>👥</span> 1.2. Đại Ma Trận Mạo Từ Sở Hữu Ở Cách 3 (Dativ) Theo 9 Ngôi Nhân Xưng
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-2.5">Ngôi Nhân Xưng</th>
                                <th class="p-2.5">Gốc Sở Hữu</th>
                                <th class="p-2.5 text-blue-700">Đực (der) & Trung (das)<br><span class="text-xs font-bold text-amber-600">đuôi -em</span></th>
                                <th class="p-2.5 text-rose-700">Cái (die)<br><span class="text-xs font-bold text-amber-600">đuôi -er</span></th>
                                <th class="p-2.5 text-purple-700">Số Nhiều (Plural)<br><span class="text-xs font-bold text-amber-600">đuôi -en (+ danh từ thêm -n)</span></th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">1. ich (tôi)</td><td class="p-2.5">mein-</td><td class="p-2.5 font-semibold">mein<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">mein<b>er</b> Schwester</td><td class="p-2.5 font-semibold">mein<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">2. du (bạn)</td><td class="p-2.5">dein-</td><td class="p-2.5 font-semibold">dein<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">dein<b>er</b> Schwester</td><td class="p-2.5 font-semibold">dein<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">3. er / es (anh ấy / nó)</td><td class="p-2.5">sein-</td><td class="p-2.5 font-semibold">sein<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">sein<b>er</b> Schwester</td><td class="p-2.5 font-semibold">sein<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">4. sie (cô ấy)</td><td class="p-2.5">ihr-</td><td class="p-2.5 font-semibold">ihr<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">ihr<b>er</b> Schwester</td><td class="p-2.5 font-semibold">ihr<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">5. wir (chúng tôi)</td><td class="p-2.5">unser-</td><td class="p-2.5 font-semibold">unser<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">unser<b>er</b> Schwester</td><td class="p-2.5 font-semibold">unser<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/30"><td class="p-2.5 font-bold text-amber-800">6. ihr (các bạn) ⚠️</td><td class="p-2.5 font-bold">euer-</td><td class="p-2.5 font-semibold">eur<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">eur<b>er</b> Schwester</td><td class="p-2.5 font-semibold">eur<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">7. sie (họ)</td><td class="p-2.5">ihr-</td><td class="p-2.5 font-semibold">ihr<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">ihr<b>er</b> Schwester</td><td class="p-2.5 font-semibold">ihr<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">8. Sie (Ngài)</td><td class="p-2.5">Ihr-</td><td class="p-2.5 font-semibold">Ihr<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">Ihr<b>er</b> Schwester</td><td class="p-2.5 font-semibold">Ihr<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: CÁC GIỚI TỪ DATIV & 9 GIỚI TỪ VỊ TRÍ WO? -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Các Giới Từ Luôn Đi Với Dativ & 9 Giới Từ Vị Trí (Wo? + Dativ)</h4>
            </div>

            <!-- Bảng 2.1: Reine Dativ-Präpositionen -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🧲</span> 2.1. Nhóm Giới Từ LUÔN LUÔN Đi Với Dativ (mit, nach, aus, zu, von, bei, seit, ab)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Giới từ</th>
                                <th class="p-3">Dạng Viết Tắt Bắt Buộc</th>
                                <th class="p-3">Ý Nghĩa Cốt Lõi</th>
                                <th class="p-3">Câu Ví Dụ Thực Tế Chuẩn (Âm thanh de-DE & Bản dịch)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">mit</td>
                                <td class="p-3 text-slate-400">—</td>
                                <td class="p-3">Cùng với / Bằng phương tiện</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Mein Bruder fährt <b>mit dem Bus</b> zur Arbeit.“ <span class="text-xs text-slate-500">(Anh trai tôi đi làm bằng xe buýt.)</span></span>
                                        <button onclick="speakGerman('Mein Bruder fährt mit dem Bus zur Arbeit.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">nach</td>
                                <td class="p-3 text-slate-400">—</td>
                                <td class="p-3">Đi đến thành phố, nước / về nhà (<i>nach Hause</i>) / Sau thời gian</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„<b>Nach der Arbeit</b> gehe ich direkt <b>nach Hause</b>.“ <span class="text-xs text-slate-500">(Sau giờ làm việc tôi đi thẳng về nhà.)</span></span>
                                        <button onclick="speakGerman('Nach der Arbeit gehe ich direkt nach Hause.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">aus</td>
                                <td class="p-3 text-slate-400">—</td>
                                <td class="p-3">Đến từ quê hương / Ra khỏi phòng, nhà</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Um 17 Uhr kommen die Mitarbeiter <b>aus dem Büro</b>.“ <span class="text-xs text-slate-500">(Lúc 17 giờ các nhân viên bước ra khỏi văn phòng.)</span></span>
                                        <button onclick="speakGerman('Um 17 Uhr kommen die Mitarbeiter aus dem Büro.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">zu</td>
                                <td class="p-3 font-semibold text-amber-700">zu + dem = <b>zum</b><br>zu + der = <b>zur</b></td>
                                <td class="p-3">Đi tới địa điểm trong phố, tới chỗ ai / Đi bộ (<i>zu Fuß</i>) / Ở nhà (<i>zu Hause</i>)</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Wie komme ich <b>zum Bahnhof</b> und <b>zur Post</b>?“ <span class="text-xs text-slate-500">(Tôi đi đến nhà ga và bưu điện bằng cách nào?)</span></span>
                                        <button onclick="speakGerman('Wie komme ich zum Bahnhof und zur Post?')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">von</td>
                                <td class="p-3 font-semibold text-amber-700">von + dem = <b>vom</b></td>
                                <td class="p-3">Từ một địa điểm trở về / Của ai (sở hữu)</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Der Zug fährt um 9 Uhr <b>vom Hauptbahnhof</b> ab.“ <span class="text-xs text-slate-500">(Chuyến tàu khởi hành lúc 9 giờ từ nhà ga chính.)</span></span>
                                        <button onclick="speakGerman('Der Zug fährt um 9 Uhr vom Hauptbahnhof ab.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">bei</td>
                                <td class="p-3 font-semibold text-amber-700">bei + dem = <b>beim</b></td>
                                <td class="p-3">Ở tại chỗ ai / Làm việc tại công ty nào</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Lukas wohnt noch <b>bei seinen Eltern</b>.“ <span class="text-xs text-slate-500">(Lukas vẫn sống ở nhà bố mẹ cậu ấy.)</span></span>
                                        <button onclick="speakGerman('Lukas wohnt noch bei seinen Eltern.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng 2.2: 9 Giới từ chỉ vị trí (Wo? + Dativ) -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📍</span> 2.2. 9 Giới Từ Vị Trí Trong Không Gian Khi Trả Lời Câu Hỏi Wo? (Ở đâu? + Dativ)
                </h5>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs sm:text-sm">
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">1. in (im = in dem)</span>
                        <p class="text-slate-600">Ở trong không gian kín (phòng, nhà, túi, thành phố): <i>im Konferenzraum, im Büro</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">2. an (am = an dem)</span>
                        <p class="text-slate-600">Ở sát cạnh / tiếp xúc mặt đứng (tường, bàn, trạm xe): <i>an der Wand, am Schreibtisch</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">3. auf</span>
                        <p class="text-slate-600">Ở trên bề mặt nằm ngang có tiếp xúc: <i>auf dem Schreibtisch, auf dem Sofa</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">4. neben</span>
                        <p class="text-slate-600">Ở bên cạnh (bên trái/phải): <i>neben dem Aufzug, neben der Tastatur</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">5. vor</span>
                        <p class="text-slate-600">Ở phía trước: <i>vor dem Hotel, vor dem Eingang</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">6. hinter</span>
                        <p class="text-slate-600">Ở phía sau / đằng sau: <i>hinter dem Bahnhof, hinter dem Krankenhaus</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">7. über</span>
                        <p class="text-slate-600">Ở phía trên cao (không tiếp xúc): <i>über dem Sofa, über dem Schreibtisch</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">8. unter</span>
                        <p class="text-slate-600">Ở phía dưới / dưới gầm: <i>unter dem Schreibtisch, unter dem Stuhl</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">9. zwischen</span>
                        <p class="text-slate-600">Ở giữa 2 vật / địa điểm: <i>zwischen der Bank und dem Kino</i>.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: PHƯƠNG TIỆN GIAO THÔNG & ĐỊNH HƯỚNG TÒA NHÀ / THÀNH PHỐ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Phương Tiện Giao Thông (Verkehrsmittel) & Định Hướng</h4>
            </div>

            <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-xs sm:text-sm text-emerald-900 space-y-1">
                <p class="font-bold flex items-center gap-2"><span>🚆</span> Công thức hỏi & trả lời phương tiện giao thông:</p>
                <p>• <b>Câu hỏi:</b> <i>Wie kommst du zur Arbeit?</i> hoặc <i>Womit fährst du nach Berlin?</i></p>
                <p>• <b>Quy tắc trả lời:</b> Mọi phương tiện đều dùng <b>mit + Dativ</b> (<i>mit dem Bus / mit der U-Bahn / mit dem Fahrrad / mit den Bussen</i>). <b>Ngoại lệ duy nhất:</b> Đi bộ = <b>zu Fuß gehen</b>.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 class="font-bold text-blue-700">🔵 Giống Đực (mit dem ...)</h5>
                    <ul class="space-y-1 text-slate-600">
                        <li>• der Bus → <b>mit dem Bus</b></li>
                        <li>• der Zug → <b>mit dem Zug</b></li>
                        <li>• der Wagen → <b>mit dem Wagen</b></li>
                    </ul>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 class="font-bold text-rose-700">🔴 Giống Cái (mit der ...)</h5>
                    <ul class="space-y-1 text-slate-600">
                        <li>• die U-Bahn → <b>mit der U-Bahn</b></li>
                        <li>• die S-Bahn → <b>mit der S-Bahn</b></li>
                        <li>• die Straßenbahn → <b>mit der Straßenbahn</b></li>
                        <li>• die Fähre → <b>mit der Fähre</b></li>
                    </ul>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 class="font-bold text-emerald-700">🟢 Giống Trung (mit dem ...) & Ngoại Lệ</h5>
                    <ul class="space-y-1 text-slate-600">
                        <li>• das Auto → <b>mit dem Auto</b></li>
                        <li>• das Fahrrad → <b>mit dem Fahrrad</b></li>
                        <li>• das Flugzeug → <b>mit dem Flugzeug</b></li>
                        <li>• das Taxi → <b>mit dem Taxi</b></li>
                        <li class="font-bold text-amber-700 pt-1">⚠️ Đi bộ: <b>zu Fuß gehen</b></li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: SỐ THỨ TỰ (ORDINALZAHLEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Số Thứ Tự (Ordinalzahlen / Ordnungszahlen)</h4>
            </div>

            <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 text-xs sm:text-sm text-purple-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>🔢</span> Hai Công Thức Cấu Tạo Số Thứ Tự:</p>
                <ul class="space-y-1 text-slate-700">
                    <li>• <b>Từ 1 đến 19:</b> Số đếm + <b>-te</b> (sau <i>der/die/das</i> ở Nominativ) | Số đếm + <b>-ten</b> (sau <i>am, im, vom, bis zum</i> ở Dativ).<br>
                    ⚠️ <b>4 Bất quy tắc bắt buộc nhớ:</b> <b>1.</b> (<i>erst-</i>), <b>3.</b> (<i>dritt-</i>), <b>7.</b> (<i>siebt-</i>), <b>8.</b> (<i>acht-</i>).</li>
                    <li>• <b>Từ 20 trở đi (20. → 31., 100., 1000.):</b> Số đếm + <b>-ste</b> (ở Nominativ) | Số đếm + <b>-sten</b> (ở Dativ). Ví dụ: <i>der zwanzigste / am zwanzigsten</i>, <i>der einundzwanzigste / am einundzwanzigsten</i>.</li>
                </ul>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                            <th class="p-2.5 text-center">Ký hiệu</th>
                            <th class="p-2.5">Số Đếm</th>
                            <th class="p-2.5 text-blue-700">Số Thứ Tự ở Nominativ (der/die/das ...)</th>
                            <th class="p-2.5 text-amber-700 font-bold">Số Thứ Tự ở Dativ (am / im / vom / bis zum ...)</th>
                            <th class="p-2.5">Ứng Dụng Thực Tế (Tầng lầu & Ngày)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-800">
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">1. ⚠️</td><td>eins</td><td>der <b>erste</b></td><td class="font-bold text-amber-700">am / im <b>ersten</b></td><td>im ersten Stock (tầng 1) / am 1. Mai</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold">2.</td><td>zwei</td><td>der <b>zweite</b></td><td class="font-bold text-amber-700">am / im <b>zweiten</b></td><td>im zweiten Stock (tầng 2) / am 2. Juni</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">3. ⚠️</td><td>drei</td><td>der <b>dritte</b></td><td class="font-bold text-amber-700">am / im <b>dritten</b></td><td>im dritten Stock (tầng 3) / am 3. August</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">7. ⚠️</td><td>sieben</td><td>der <b>siebte</b></td><td class="font-bold text-amber-700">am / im <b>siebten</b></td><td>im siebten Stock (tầng 7) / am 7. Mai</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">8. ⚠️</td><td>acht</td><td>der <b>achte</b></td><td class="font-bold text-amber-700">am / im <b>achten</b></td><td>im achten Stock (tầng 8) / am 8. März</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold">15.</td><td>fünfzehn</td><td>der <b>fünfzehnte</b></td><td class="font-bold text-amber-700">am / im <b>fünfzehnten</b></td><td>am 15. August (ngày 15 tháng Tám)</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-purple-600">20.</td><td>zwanzig</td><td>der <b>zwanzigste</b></td><td class="font-bold text-amber-700">am / im <b>zwanzigsten</b></td><td>am 20. September</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-purple-600">21.</td><td>einundzwanzig</td><td>der <b>einundzwanzigste</b></td><td class="font-bold text-amber-700">am / im <b>einundzwanzigsten</b></td><td>am 21. Juni</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-purple-600">31.</td><td>einunddreißig</td><td>der <b>einunddreißigste</b></td><td class="font-bold text-amber-700">am / im <b>einunddreißigsten</b></td><td>am 31. Dezember</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- HỌC PHẦN 5: NGÀY - THÁNG - NĂM (DAS DATUM & DIE JAHRESZAHLEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Ngày – Tháng – Năm Trong Tiếng Đức (Das Datum & Jahreszahlen)</h4>
            </div>

            <!-- 3 Cấu trúc nói ngày tháng -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <span class="font-bold text-indigo-700">1. Hôm nay là ngày mấy? (Nominativ)</span>
                    <p class="text-slate-600"><i>Welcher Tag ist heute?</i></p>
                    <p class="font-semibold text-slate-900">→ Heute ist <b>der</b> dritt<b>e</b> Mai. (03.05.)</p>
                    <p class="text-xs text-slate-500">Sau <i>der</i> dùng đuôi <b>-te / -ste</b>.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <span class="font-bold text-indigo-700">2. Vào ngày nào? (Dativ với am)</span>
                    <p class="text-slate-600"><i>Wann hast du Geburtstag?</i></p>
                    <p class="font-semibold text-slate-900">→ Ich habe <b>am</b> acht<b>en</b> März Geburtstag.</p>
                    <p class="text-xs text-slate-500">Sau <i>am</i> dùng đuôi <b>-ten / -sten</b>.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <span class="font-bold text-indigo-700">3. Khoảng ngày: vom... bis zum...</span>
                    <p class="text-slate-600"><i>Von wann bis wann habt ihr Urlaub?</i></p>
                    <p class="font-semibold text-slate-900">→ <b>Vom</b> erst<b>en</b> <b>bis zum</b> vierzehn<b>ten</b> Juli.</p>
                    <p class="text-xs text-slate-500">Cả 2 số thứ tự đều chia ở <b>Dativ (-ten/-sten)</b>.</p>
                </div>
            </div>

            <!-- Quy tắc đọc Năm -->
            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>📅</span> Quy Tắc Đọc Năm (Jahreszahlen) & Giới Từ Trước Năm:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-slate-700">
                    <div class="p-3 bg-white/80 rounded-xl border border-amber-100 space-y-1">
                        <span class="font-bold text-indigo-800">1. Các năm trước năm 2000 (Đọc theo cụm trăm):</span>
                        <p>• <b>1968:</b> <i>neunzehnhundertachtundsechzig</i> (19 trăm 68)</p>
                        <p>• <b>1998:</b> <i>neunzehnhundertachtundneunzig</i></p>
                    </div>
                    <div class="p-3 bg-white/80 rounded-xl border border-amber-100 space-y-1">
                        <span class="font-bold text-indigo-800">2. Các năm từ năm 2000 trở đi (Đọc như số đếm):</span>
                        <p>• <b>2002:</b> <i>zweitausendzwei</i></p>
                        <p>• <b>2026:</b> <i>zweitausendsechsundzwanzig</i></p>
                    </div>
                </div>
                <p class="text-xs text-slate-600 pt-1">
                    ⚠️ <b>Tuyệt đối KHÔNG dùng giới từ "in" trước năm trong tiếng Đức!</b><br>
                    • Đúng: <i>Ich bin 1998 in Hai Phong geboren.</i> (hoặc <i>im Jahr 1998</i>).<br>
                    • Sai hoàn toàn: <strike class="text-rose-600">Ich bin in 1998 geboren.</strike>
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 6: HỘI THOẠI THỰC CHIẾN ĐA NGỮ CẢNH KÈM AUDIO -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center font-bold text-sm">6</span>
                <h4 class="text-lg font-bold text-slate-900">Hội Thoại Thực Chiến Đa Ngữ Cảnh (Praxis-Dialoge de-DE)</h4>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <!-- Hội thoại 1: Im Bürogebäude -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <h5 class="font-bold text-slate-800 flex items-center gap-2"><span>🏢</span> Hội Thoại 1: Trong Tòa Nhà Công Ty</h5>
                        <button onclick="speakGerman('Entschuldigung, wo ist das Büro von Frau Schneider? Das Büro liegt im dritten Stock neben dem Aufzug. Die Kantine befindet sich im Erdgeschoss.')" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-bold cursor-pointer">🔊 Nghe Hội Thoại</button>
                    </div>
                    <div class="space-y-2.5 text-xs sm:text-sm text-slate-700">
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Khách:</b> „Entschuldigung, wo ist das Büro von Frau Schneider?“<br><span class="text-xs text-slate-500">(Xin lỗi, văn phòng của bà Schneider ở đâu ạ?)</span></p>
                            <button onclick="speakGerman('Entschuldigung, wo ist das Büro von Frau Schneider?')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Lễ tân:</b> „Das Büro liegt <b>im dritten Stock</b> <b>neben dem Aufzug</b>. Die Kantine befindet sich <b>im Erdgeschoss</b>.“<br><span class="text-xs text-slate-500">(Văn phòng nằm ở tầng ba bên cạnh thang máy. Nhà ăn thì ở tầng trệt.)</span></p>
                            <button onclick="speakGerman('Das Büro liegt im dritten Stock neben dem Aufzug. Die Kantine befindet sich im Erdgeschoss.')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                    </div>
                </div>

                <!-- Hội thoại 2: In der Stadt & Verkehrsmittel -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <h5 class="font-bold text-slate-800 flex items-center gap-2"><span>🚆</span> Hội Thoại 2: Hỏi Đường & Phương Tiện</h5>
                        <button onclick="speakGerman('Entschuldigung, wie komme ich zum Bahnhof? Fahren Sie mit der Straßenbahn Linie 3 bis zum Markt. Dort steigen Sie in den Bus um.')" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-bold cursor-pointer">🔊 Nghe Hội Thoại</button>
                    </div>
                    <div class="space-y-2.5 text-xs sm:text-sm text-slate-700">
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Người đi đường:</b> „Entschuldigung, wie komme ich <b>zum Bahnhof</b>?“<br><span class="text-xs text-slate-500">(Xin lỗi, tôi đi đến nhà ga bằng cách nào ạ?)</span></p>
                            <button onclick="speakGerman('Entschuldigung, wie komme ich zum Bahnhof?')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Cư dân:</b> „Fahren Sie <b>mit der Straßenbahn</b> Linie 3 <b>bis zum Markt</b>. Dort steigen Sie in den Bus um.“<br><span class="text-xs text-slate-500">(Bạn hãy đi bằng tàu điện mặt đất tuyến số 3 đến chợ. Tại đó bạn đổi sang xe buýt.)</span></p>
                            <button onclick="speakGerman('Fahren Sie mit der Straßenbahn Linie 3 bis zum Markt. Dort steigen Sie in den Bus um.')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

# 5. Xuất file seed_a1_b6.py
seed_py_content = f'''import json
import os
import sys

true = True
false = False
null = None

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_6():
    conn = get_connection()
    cursor = conn.cursor()

    # Đảm bảo bảng exercises có cột extra_data
    cursor.execute("PRAGMA table_info(exercises);")
    columns = [col["name"] for col in cursor.fetchall()]
    if "extra_data" not in columns:
        cursor.execute("ALTER TABLE exercises ADD COLUMN extra_data TEXT;")

    cursor.execute("SELECT id FROM levels WHERE code = 'A1';")
    level_a1 = cursor.fetchone()
    if not level_a1:
        print("❌ Hãy chạy database.py trước!")
        conn.close()
        return
    a1_id = level_a1["id"]

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 6%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 20

    # Xóa dữ liệu cũ của Bài 6 nếu có để cập nhật sạch sẽ (Bảo toàn tuyệt đối Bài 1 -> Bài 5)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM lessons WHERE id = ?;", (lesson_id,))

    lesson_title = 'Bài 6: "Dativ - Giới từ trong Dativ - Phương tiện giao thông - Số thứ tự - Ngày tháng năm (Orientierung)"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (6 HỌC PHẦN CHUẨN ĐẶC TẢ - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """{grammar_html}"""

    cursor.execute("""
        INSERT INTO lessons (id, level_id, title, grammar_content)
        VALUES (?, ?, ?, ?);
    """, (lesson_id, a1_id, lesson_title, grammar_html))

    # =========================================================================
    # DANH MỤC 45 TỪ VỰNG TRỌNG TÂM BÀI 6 (KHỚP 100% VỚI LEXIKON_DB.JS)
    # =========================================================================
    vocab_raw = {json.dumps(b6_vocab_list, ensure_ascii=False, indent=8)}

    vocabularies = []
    for item in vocab_raw:
        vocabularies.append((
            lesson_id,
            item["word"],
            item["article"],
            item["meaning"],
            f"{{item['example']}} ({{item['example_vi']}})"
        ))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # KHO 100 BÀI TẬP BÀI 6 CHUẨN ĐẶC TẢ ZERO-BUG (18+15+12+12+10+10+9+7+7)
    # =========================================================================
    exercises_raw = {json.dumps(parsed_exercises, ensure_ascii=False, indent=8)}

    import random
    exercises = []
    for ex in exercises_raw:
        q_num = ex["q_num"]
        ex_type = ex["type"]
        question = ex["question"]
        opts = ex["options_json"]
        corr = ex["correct_answer"]
        exp = ex["explanation"]
        pts = ex["exp_reward"]
        extra = ex["extra_data"]

        if ex_type == "trac_nghiem" and opts:
            try:
                opt_list = json.loads(opts)
                if isinstance(opt_list, list) and len(opt_list) > 1:
                    random.shuffle(opt_list)
                    opts = json.dumps(opt_list, ensure_ascii=False)
            except Exception:
                pass

        extra_json = json.dumps(extra, ensure_ascii=False) if extra else None
        exercises.append((
            lesson_id, ex_type, question, opts, corr, exp, pts, extra_json
        ))

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công Bài 6: 'Dativ - Giới từ trong Dativ - Phương tiện giao thông - Số thứ tự - Ngày tháng năm' với đầy đủ 6 Học phần Lý thuyết + 45 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_6()
'''

target_seed_file = os.path.join(BASE_DIR, 'lessons/a1/seed_a1_b6.py')
with open(target_seed_file, 'w', encoding='utf-8') as f:
    f.write(seed_py_content)

print(f"🎉 Đã ghi thành công file: {target_seed_file} (Kích thước: {len(seed_py_content)} bytes)")
