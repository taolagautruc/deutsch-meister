# -*- coding: utf-8 -*-
"""
Seed file Bài 13 (A1): "Ôn tập tổng hợp A1 — Động từ bất quy tắc, W-Fragen & Giao tiếp quán Cafe"
Vị trí A1: lesson_order = 14 (sau Bài 12)
Tích hợp đầy đủ 4 Học phần Lý thuyết + 2 Container Sơ đồ SVG + 12 Từ vựng + 125 Bài tập độc nhất (18 Dạng bài)
Chuẩn CEFR A1 và tuân thủ tuyệt đối Giao thức QA Zero-Bug & Quy tắc chống bẫy ngôi ihr
"""

import json
import os
import sys

true = True
false = False
null = None

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_13():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("PRAGMA table_info(exercises);")
    columns = [col["name"] for col in cursor.fetchall()]
    if "extra_data" not in columns:
        cursor.execute("ALTER TABLE exercises ADD COLUMN extra_data TEXT;")

    cursor.execute("SELECT id FROM levels WHERE code = 'A1';")
    level_a1 = cursor.fetchone()
    if not level_a1:
        print("Không tìm thấy cấp độ A1 trong database!")
        conn.close()
        return

    a1_id = level_a1["id"]
    lesson_id = 27
    lesson_title = 'Bài 13: Ôn tập tổng hợp A1 — Động từ bất quy tắc, W-Fragen & Giao tiếp quán Cafe'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed font-sans">
        <!-- BANNER TỔNG QUAN BÀI 13 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-amber-600 via-orange-600 to-indigo-900 text-white shadow-xl relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/20 backdrop-blur-md text-amber-200 text-xs font-black uppercase tracking-wider">
                    DeutschMeister A1 • ÖK A1 • Verben & W-Fragen (Bài 13)
                </span>
                <h1 class="text-2xl sm:text-4xl font-black text-white tracking-tight">
                    Ôn tập A1: Động từ bất quy tắc, W-Fragen & Giao tiếp quán Cafe
                </h1>
                <p class="text-amber-100 text-sm sm:text-base font-normal max-w-3xl leading-relaxed">
                    Hệ thống hóa toàn bộ quy tắc chia động từ mạnh (biến đổi nguyên âm a→ä, e→i, e→ie), phân biệt đại từ nhân xưng. Nắm vững nghệ thuật đặt câu hỏi W-Fragen và thực hành hội thoại gọi món tại quán Cafe.
                </p>
                <div class="pt-2 flex flex-wrap gap-2 text-xs font-bold">
                    <span class="px-3 py-1.5 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20">🔥 Bất quy tắc (a→ä, e→i, e→ie)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20">📝 Động từ Có quy tắc</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20">❓ W-Fragen (Wie, Wo, Woher)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20">☕ Hội thoại Cafe</span>
                </div>
            </div>
            <div class="absolute -right-8 -bottom-8 opacity-15 text-9xl select-none pointer-events-none">☕</div>
        </div>

        <!-- HỌC PHẦN 1: HỆ THỐNG ĐẠI TỪ NHÂN XƯNG & TRỢ ĐỘNG TỪ SEIN / HABEN -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm">1</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Hệ Thống Đại Từ Nhân Xưng & Trợ Động Từ sein / haben
                </h2>
            </div>
            <p class="text-sm">
                Để chia động từ chính xác trong tiếng Đức, bạn cần nắm vững hai nhóm đại từ nhân xưng:
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="font-extrabold text-indigo-900 text-sm">Số ít (Singular):</div>
                    <ul class="space-y-1.5 text-slate-700">
                        <li>• <b class="font-mono text-indigo-600">ich</b> (tôi): đuôi <code>-e</code> • sein: <b>bin</b>, haben: <b>habe</b></li>
                        <li>• <b class="font-mono text-indigo-600">du</b> (bạn - thân mật 1 người): đuôi <code>-st</code> • sein: <b>bist</b>, haben: <b>hast</b></li>
                        <li>• <b class="font-mono text-indigo-600">er / sie / es</b> (anh ấy / cô ấy / nó): đuôi <code>-t</code> • sein: <b>ist</b>, haben: <b>hat</b></li>
                    </ul>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="font-extrabold text-indigo-900 text-sm">Số nhiều (Plural) & Trang trọng:</div>
                    <ul class="space-y-1.5 text-slate-700">
                        <li>• <b class="font-mono text-indigo-600">wir</b> (chúng tôi/chúng ta): đuôi <code>-en</code> • sein: <b>sind</b>, haben: <b>haben</b></li>
                        <li>• <b class="font-mono text-indigo-600">ihr</b> (các bạn - thân mật số nhiều): đuôi <code>-t</code> • sein: <b>seid</b>, haben: <b>habt</b></li>
                        <li>• <b class="font-mono text-indigo-600">sie</b> (họ) / <b class="font-mono text-indigo-600">Sie</b> (Ngài/Các ngài): đuôi <code>-en</code> • sein: <b>sind</b>, haben: <b>haben</b></li>
                    </ul>
                </div>
            </div>

            <!-- Khung Vàng Cảnh Báo Phân Biệt 3 Chữ sie -->
            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-300 space-y-2 text-xs">
                <div class="flex items-center gap-2 font-black text-amber-900">
                    <span>⚠️ KHUNG VÀNG CẢNH BÁO: PHÂN BIỆT 3 CHỮ "SIE" TRONG TIẾNG ĐỨC</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        <span class="font-bold text-slate-900 block font-mono">1. sie (cô ấy)</span>
                        <span class="text-slate-600 text-[11px]">Động từ chia số ít ngôi thứ 3 (đuôi <b>-t</b>): <i>sie kommt, sie liest</i>.</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        <span class="font-bold text-slate-900 block font-mono">2. sie (họ)</span>
                        <span class="text-slate-600 text-[11px]">Động từ chia số nhiều ở dạng nguyên thể (đuôi <b>-en</b>): <i>sie kommen, sie lesen</i>.</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        <span class="font-bold text-slate-900 block font-mono">3. Sie (Ngài / Các ngài)</span>
                        <span class="text-slate-600 text-[11px]">LUÔN VIẾT HOA chữ <b>S</b> ở mọi vị trí câu; động từ giữ nguyên thể (đuôi <b>-en</b>): <i>Sie kommen</i>.</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- HỌC PHẦN 2: ĐỘNG TỪ BẤT QUY TẮC & SƠ ĐỒ V1 CỖ MÁY BIẾN ÂM -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-amber-600 text-white font-black flex items-center justify-center text-sm">2</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Động Từ Bất Quy Tắc (Biến Âm Vowel-Shift) & Quy Tắc Vàng
                </h2>
            </div>
            
            <div class="p-4 rounded-2xl bg-rose-50 border border-rose-300 text-xs space-y-2">
                <div class="font-black text-rose-900 text-sm flex items-center gap-2">
                    <span>🔥 QUY TẮC VÀNG BẤT HỦ:</span>
                </div>
                <p class="text-rose-950 leading-relaxed font-semibold">
                    Hiện tượng biến đổi nguyên âm gốc (Vowel-Shift) <b>CHỈ XẢY RA</b> ở 2 ngôi: <code>du</code> và <code>er/sie/es</code>.
                    <br>
                    <span class="text-rose-800 font-extrabold underline">Tuyệt đối cấm kỵ:</span> Ngôi <code>ihr</code> (các bạn) <b>KHÔNG BAO GIỜ</b> biến âm! (<i>ihr fahrt, ihr schlaft, ihr lest, ihr sprecht</i>).
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900 font-mono text-sm text-indigo-600">Nhóm a → ä:</div>
                    <div>• <b>fahren</b>: du fährst, er fährt (ihr fahrt)</div>
                    <div>• <b>schlafen</b>: du schläfst, er schläft (ihr schlaft)</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900 font-mono text-sm text-amber-600">Nhóm e → i:</div>
                    <div>• <b>sprechen</b>: du sprichst, er spricht</div>
                    <div>• <b>treffen</b>: du triffst, er trifft</div>
                    <div>• <b>essen</b>: du isst, er isst</div>
                    <div>• <b>geben</b>: du gibst, er gibt</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900 font-mono text-sm text-emerald-600">Nhóm e → ie:</div>
                    <div>• <b>lesen</b>: du liest, er liest (ihr lest)</div>
                    <div class="text-[11px] text-slate-500 italic mt-1">*Ngôi du đuôi -st gộp với s gốc thành -t: du liest, du isst.</div>
                </div>
            </div>

            <!-- CONTAINER SƠ ĐỒ V1 -->
            <div id="b13-svg-v1-container" class="my-4"></div>
        </section>

        <!-- HỌC PHẦN 3: TỪ ĐỂ HỎI (W-FRAGEN) & QUY TẮC GIỚI TỪ -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm">3</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Từ Để Hỏi (W-Fragen) & Quy Tắc Giới Từ Đi Kèm
                </h2>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                    <span class="font-mono text-sm font-black text-indigo-600">Wie (Như thế nào)</span>
                    <p class="text-slate-600">Dùng để hỏi tên hoặc tính chất:</p>
                    <div class="font-mono text-[11px] text-slate-900">Wie heißen Sie?</div>
                    <div class="text-slate-500 italic">Tôi tên là Anna.</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                    <span class="font-mono text-sm font-black text-rose-600">Woher (Từ đâu)</span>
                    <p class="text-slate-600">Hỏi quê quán, xuất xứ. Luôn đi với <b>aus</b>:</p>
                    <div class="font-mono text-[11px] text-slate-900">Woher kommst du?</div>
                    <div class="text-slate-500 italic">Aus Vietnam.</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                    <span class="font-mono text-sm font-black text-blue-600">Wo (Ở đâu)</span>
                    <p class="text-slate-600">Hỏi nơi ở, vị trí cố định. Luôn đi với <b>in</b>:</p>
                    <div class="font-mono text-[11px] text-slate-900">Wo wohnen Sie?</div>
                    <div class="text-slate-500 italic">In Berlin.</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                    <span class="font-mono text-sm font-black text-purple-600">Was (Cái gì)</span>
                    <p class="text-slate-600">Hỏi đồ vật, đồ ăn, thức uống:</p>
                    <div class="font-mono text-[11px] text-slate-900">Was trinken Sie?</div>
                    <div class="text-slate-500 italic">Kaffee mit Zucker.</div>
                </div>
            </div>

            <!-- CONTAINER SƠ ĐỒ V2 -->
            <div id="b13-svg-v2-container" class="my-4"></div>
        </section>

        <!-- HỌC PHẦN 4: HỘI THOẠI THỰC TẾ: KAFFEE ODER TEE -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-orange-600 text-white font-black flex items-center justify-center text-sm">4</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Hội Thoại Thực Tế Quán Cafe: Kaffee oder Tee
                </h2>
            </div>
            
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 text-xs">
                <div class="font-extrabold text-slate-900 text-sm">3 Tình huống giao tiếp cốt lõi tại quán Cafe:</div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <span class="font-bold text-amber-700">1. Tìm chỗ ngồi:</span>
                        <div class="font-mono text-slate-900">„Entschuldigung, ist hier frei?“</div>
                        <div class="text-slate-500 italic">Xin lỗi, chỗ này còn trống không?</div>
                        <div class="font-mono text-emerald-700 mt-1">„Ja klar, bitte.“</div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <span class="font-bold text-amber-700">2. Làm quen cơ bản:</span>
                        <div class="font-mono text-slate-900">„Ich bin John aus Frankreich, und du?“</div>
                        <div class="text-slate-500 italic">Tôi là John đến từ Pháp, còn bạn?</div>
                        <div class="font-mono text-emerald-700 mt-1">„Ich heiße Anna. Ich komme aus Polen.“</div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <span class="font-bold text-amber-700">3. Gọi đồ uống:</span>
                        <div class="font-mono text-slate-900">„Was möchtet ihr trinken?“</div>
                        <div class="text-slate-500 italic">Các bạn muốn uống gì?</div>
                        <div class="font-mono text-emerald-700 mt-1">„Zwei Kaffee mit Zucker, bitte!“</div>
                    </div>
                </div>
            </div>
        </section>
    </div>
    """

    cursor.execute("""
        INSERT OR REPLACE INTO lessons (id, level_id, title, grammar_content)
        VALUES (?, ?, ?, ?);
    """, (lesson_id, a1_id, lesson_title, grammar_html))

    # Cập nhật danh sách từ vựng Bài 13
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    
    vocab_items = [
        ("Kaffee", "der", "cà phê", "Ich trinke meinen Kaffee immer mit viel Zucker."),
        ("Tee", "der", "trà", "Möchtest du eine Tasse schwarzen Tee?"),
        ("Zucker", "der", "đường (nur Sg.)", "Zwei Kaffee mit Zucker, bitte!"),
        ("Käse", "der", "phô mai", "Wir kaufen frischen Käse im Supermarkt."),
        ("Salat", "der", "rau xà lách, món salad", "Ich mache heute Abend einen Tomatensalat."),
        ("Hund", "der", "con chó", "Der Hund schläft gemütlich auf dem Sofa."),
        ("Brief", "der", "bức thư", "Anna schreibt einen langen Brief an ihre Oma."),
        ("Eis", "das", "kem, đá (nur Sg.)", "Ich esse gern Erdbeereis."),
        ("Futter", "das", "thức ăn thú cưng (nur Sg.)", "Hannes gibt der Katze das Futter."),
        ("Hotel", "das", "khách sạn", "Das Hotelzimmer ist groß und sehr sauber."),
        ("Rathaus", "das", "tòa thị chính", "Die Touristen besuchen das alte Rathaus."),
        ("Gemüse", "das", "rau củ (nur Sg.)", "Gemüse ist sehr gesund für den Körper.")
    ]

    for word, art, mean, ex_sent in vocab_items:
        cursor.execute("""
            INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
            VALUES (?, ?, ?, ?, ?);
        """, (lesson_id, word, art, mean, ex_sent))

    print(f"Đã cập nhật thành công {len(vocab_items)} từ vựng cho Bài 13.")

    # Cập nhật 125 bài tập Bài 13
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    exercises_data = [
        # --- 3.1. TRẮC NGHIỆM (15 CÂU) ---
        {
            "id": 1,
            "exercise_type": "trac_nghiem",
            "question": "Câu 1: Chọn dạng đúng của động từ trong ngoặc:\n„Meine Schwester ___ am Abend oft einen Roman.“ (lesen)",
            "options": ["lest", "lese", "liest", "liesst"],
            "correct_answer": "liest",
            "explanation": "Chủ ngữ „Meine Schwester“ tương đương ngôi cô ấy (sie), động từ bất quy tắc „lesen“ đổi e → ie thành „liest“ -> Đáp án: liest.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Meine Schwester liest am Abend oft einen Roman."}
        },
        {
            "id": 2,
            "exercise_type": "trac_nghiem",
            "question": "Câu 2: Chọn dạng đúng của động từ trong ngoặc:\n„Wann ___ ihr am Wochenende nach Berlin?“ (fahren)",
            "options": ["fährst", "fahrt", "fährt", "fahren"],
            "correct_answer": "fahrt",
            "explanation": "LƯU Ý: Ngôi ihr (các bạn) KHÔNG biến âm. Động từ „fahren“ bỏ đuôi -en thêm -t thành „fahrt“ -> Đáp án: fahrt.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wann fahrt ihr am Wochenende nach Berlin?"}
        },
        {
            "id": 3,
            "exercise_type": "trac_nghiem",
            "question": "Câu 3: Chọn từ để hỏi thích hợp:\n„___ kommst du, Maria?“ — „Aus Spanien.“",
            "options": ["Wo", "Wie", "Was", "Woher"],
            "correct_answer": "Woher",
            "explanation": "Câu trả lời dùng giới từ „Aus“ (từ) chỉ quê quán/xuất xứ, nên câu hỏi phải dùng từ để hỏi „Woher“ (từ đâu) -> Đáp án: Woher.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Woher kommst du, Maria? Aus Spanien."}
        },
        {
            "id": 4,
            "exercise_type": "trac_nghiem",
            "question": "Câu 4: Chọn dạng đúng của động từ trong ngoặc:\n„Der Lehrer ___ heute sehr laut.“ (sprechen)",
            "options": ["sprechet", "sprech", "spricht", "spracht"],
            "correct_answer": "spricht",
            "explanation": "Chủ ngữ „Der Lehrer“ (er - anh ấy), động từ bất quy tắc „sprechen“ đổi e → i thành „spricht“ -> Đáp án: spricht.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Der Lehrer spricht heute sehr laut."}
        },
        {
            "id": 5,
            "exercise_type": "trac_nghiem",
            "question": "Câu 5: Chọn dạng đúng của động từ trong ngoặc:\n„Was ___ Hannes und Julia dem kleinen Hund?“ (geben)",
            "options": ["gibt", "gebt", "gibst", "geben"],
            "correct_answer": "geben",
            "explanation": "Chủ ngữ là „Hannes und Julia“ (họ - sie số nhiều), động từ giữ nguyên thể „geben“ -> Đáp án: geben.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Was geben Hannes und Julia dem kleinen Hund?"}
        },
        {
            "id": 6,
            "exercise_type": "trac_nghiem",
            "question": "Câu 6: Chọn dạng đúng của động từ trong ngoặc:\n„Das Handy ___ in der Küche auf dem Tisch.“ (liegen)",
            "options": ["liegst", "lege", "liegt", "liegen"],
            "correct_answer": "liegt",
            "explanation": "Chủ ngữ „Das Handy“ (ngôi es) đi với động từ có quy tắc „liegen“ thêm đuôi -t thành „liegt“ -> Đáp án: liegt.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Das Handy liegt in der Küche auf dem Tisch."}
        },
        {
            "id": 7,
            "exercise_type": "trac_nghiem",
            "question": "Câu 7: Chọn dạng đúng của động từ trong ngoặc:\n„___ du heute Nacht bei mir?“ (schlafen)",
            "options": ["Schlafst", "Schläfst", "Schläft", "Schlafen"],
            "correct_answer": "Schläfst",
            "explanation": "Chủ ngữ ngôi „du“, động từ „schlafen“ đổi a → ä và thêm đuôi -st thành „Schläfst“ -> Đáp án: Schläfst.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Schläfst du heute Nacht bei mir?"}
        },
        {
            "id": 8,
            "exercise_type": "trac_nghiem",
            "question": "Câu 8: Chọn đại từ nhân xưng thích hợp:\n„Der Vater grillt am Sonntag Fleisch. ___ macht auch einen Salat.“",
            "options": ["Er", "Sie", "Es", "Ihr"],
            "correct_answer": "Er",
            "explanation": "Đại từ thay thế cho danh từ giống đực „Der Vater“ là „Er“ (anh ấy/ông ấy) -> Đáp án: Er.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Der Vater grillt am Sonntag Fleisch. Er macht auch einen Salat."}
        },
        {
            "id": 9,
            "exercise_type": "trac_nghiem",
            "question": "Câu 9: Chọn câu hỏi ĐÚNG cho câu trả lời sau:\n„Ich trinke Kaffee mit Zucker.“",
            "options": ["Wo wohnst du?", "Was trinken Sie?", "Wie heißt du?", "Wer trinkt Tee?"],
            "correct_answer": "Was trinken Sie?",
            "explanation": "Câu trả lời nói về loại đồ uống („Kaffee“), nên câu hỏi phù hợp nhất là „Was trinken Sie?“ (Ngài uống gì?) -> Đáp án: Was trinken Sie?.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Was trinken Sie? Ich trinke Kaffee mit Zucker."}
        },
        {
            "id": 10,
            "exercise_type": "trac_nghiem",
            "question": "Câu 10: Chọn dạng động từ tobe đúng cho câu giao tiếp:\n„Entschuldigung, ___ hier frei?“",
            "options": ["ist", "sind", "bin", "bist"],
            "correct_answer": "ist",
            "explanation": "Chủ ngữ giả định cho chỗ ngồi/nơi chốn là es, đi với động từ tobe „ist“ (Ist hier frei? = Chỗ này còn trống không?) -> Đáp án: ist.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Entschuldigung, ist hier frei?"}
        },
        {
            "id": 11,
            "exercise_type": "trac_nghiem",
            "question": "Câu 11: Chọn dạng đúng của động từ trong ngoặc:\n„Wann ___ du deine Freunde im Café?“ (treffen)",
            "options": ["treffst", "triffst", "trifft", "treffen"],
            "correct_answer": "triffst",
            "explanation": "Ngôi „du“, động từ bất quy tắc „treffen“ đổi e → i thành „triffst“ -> Đáp án: triffst.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wann triffst du deine Freunde im Café?"}
        },
        {
            "id": 12,
            "exercise_type": "trac_nghiem",
            "question": "Câu 12: Chọn dạng đúng của động từ trong ngoặc:\n„Wir ___ im Sommer gern Vanilleeis.“ (essen)",
            "options": ["isst", "esse", "essen", "esst"],
            "correct_answer": "essen",
            "explanation": "Chủ ngữ ngôi „wir“ (chúng tôi) luôn dùng động từ nguyên thể „essen“ -> Đáp án: essen.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wir essen im Sommer gern Vanilleeis."}
        },
        {
            "id": 13,
            "exercise_type": "trac_nghiem",
            "question": "Câu 13: Chọn dạng đúng của động từ trong ngoặc:\n„Julia und Lara ___ nach Italien.“ (reisen)",
            "options": ["reist", "reisen", "reisst", "reise"],
            "correct_answer": "reisen",
            "explanation": "Chủ ngữ số nhiều „Julia und Lara“ (họ - sie số nhiều), động từ giữ nguyên thể „reisen“ -> Đáp án: reisen.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Julia und Lara reisen nach Italien."}
        },
        {
            "id": 14,
            "exercise_type": "trac_nghiem",
            "question": "Câu 14: Chọn từ để hỏi thích hợp:\n„___ wohnen Sie jetzt?“ — „In München.“",
            "options": ["Woher", "Was", "Wie", "Wo"],
            "correct_answer": "Wo",
            "explanation": "Câu trả lời dùng giới từ „In“ chỉ địa điểm cư trú, câu hỏi về nơi ở dùng „Wo“ (ở đâu) -> Đáp án: Wo.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wo wohnen Sie jetzt? In München."}
        },
        {
            "id": 15,
            "exercise_type": "trac_nghiem",
            "question": "Câu 15: Chọn dạng đúng của động từ trong ngoặc:\n„Die Touristen ___ das alte Rathaus.“ (besuchen)",
            "options": ["besucht", "besuche", "besuchen", "besuchst"],
            "correct_answer": "besuchen",
            "explanation": "Chủ ngữ „Die Touristen“ (số nhiều - họ) đi với động từ nguyên thể „besuchen“ -> Đáp án: besuchen.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Die Touristen besuchen das alte Rathaus."}
        },

        # --- 3.2. ĐIỀN KHUYẾT (10 CÂU) ---
        {
            "id": 16,
            "exercise_type": "dien_khuyet",
            "question": "Câu 16: Điền từ để hỏi thích hợp vào chỗ trống:\n„___ heißt du?“ — „Ich heiße David.“",
            "options": null,
            "correct_answer": "Wie",
            "explanation": "Hỏi tên trong tiếng Đức luôn dùng từ để hỏi „Wie“ (Wie heißt du?) -> Đáp án: Wie.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Wie", "wie"]}
        },
        {
            "id": 17,
            "exercise_type": "dien_khuyet",
            "question": "Câu 17: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Wir ___ den Käse im Supermarkt.“ (kaufen)",
            "options": null,
            "correct_answer": "kaufen",
            "explanation": "Chủ ngữ „wir“ đi với động từ nguyên thể „kaufen“ -> Đáp án: kaufen.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["kaufen"]}
        },
        {
            "id": 18,
            "exercise_type": "dien_khuyet",
            "question": "Câu 18: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Mein Onkel ___ gern schwarzen Tee.“ (trinken)",
            "options": null,
            "correct_answer": "trinkt",
            "explanation": "Chủ ngữ „Mein Onkel“ (er - anh ấy), động từ có quy tắc „trinken“ thêm đuôi -t thành „trinkt“ -> Đáp án: trinkt.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["trinkt"]}
        },
        {
            "id": 19,
            "exercise_type": "dien_khuyet",
            "question": "Câu 19: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Ich ___ meine Hausaufgaben.“ (machen)",
            "options": null,
            "correct_answer": "mache",
            "explanation": "Chủ ngữ „ich“ đi với động từ có quy tắc thêm đuôi -e thành „mache“ -> Đáp án: mache.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["mache"]}
        },
        {
            "id": 20,
            "exercise_type": "dien_khuyet",
            "question": "Câu 20: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Die Kinder ___ Fußball auf dem Hof.“ (spielen)",
            "options": null,
            "correct_answer": "spielen",
            "explanation": "Chủ ngữ số nhiều „Die Kinder“ (bọn trẻ - sie Plural), động từ giữ nguyên thể „spielen“ -> Đáp án: spielen.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["spielen"]}
        },
        {
            "id": 21,
            "exercise_type": "dien_khuyet",
            "question": "Câu 21: Điền động từ khuyết thiếu thể hiện mong muốn lịch sự:\n„Herr Müller, was ___ Sie trinken?“ (muốn)",
            "options": null,
            "correct_answer": "möchten",
            "explanation": "Động từ khuyết thiếu chỉ sự mong muốn lịch sự đi với ngôi Ngài (Sie) là „möchten“ -> Đáp án: möchten.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["möchten", "moechten"]}
        },
        {
            "id": 22,
            "exercise_type": "dien_khuyet",
            "question": "Câu 22: Điền giới từ chỉ xuất xứ vào chỗ trống:\n„Ich komme ___ Frankreich.“ (từ)",
            "options": null,
            "correct_answer": "aus",
            "explanation": "Giới từ chỉ nơi xuất xứ đi với động từ kommen là „aus“ -> Đáp án: aus.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["aus"]}
        },
        {
            "id": 23,
            "exercise_type": "dien_khuyet",
            "question": "Câu 23: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„___ ihr einen Brief an die Großmutter?“ (schreiben)",
            "options": null,
            "correct_answer": "Schreibt",
            "explanation": "Ngôi „ihr“ (các bạn), động từ „schreiben“ thêm đuôi -t và đứng đầu câu hỏi đảo là „Schreibt“ -> Đáp án: Schreibt.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Schreibt", "schreibt"]}
        },
        {
            "id": 24,
            "exercise_type": "dien_khuyet",
            "question": "Câu 24: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Karin ___ rất thích nghe nhạc cổ điển.“ (hören)",
            "options": null,
            "correct_answer": "hört",
            "explanation": "Chủ ngữ Karin (ngôi sie số ít), động từ „hören“ thêm đuôi -t thành „hört“ -> Đáp án: hört.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["hört", "hoert"]}
        },
        {
            "id": 25,
            "exercise_type": "dien_khuyet",
            "question": "Câu 25: Điền từ để hỏi thích hợp vào chỗ trống:\n„___ singst du so gern?“ — „Weil ich Musik liebe.“",
            "options": null,
            "correct_answer": "Warum",
            "explanation": "Câu trả lời bắt đầu bằng „Weil“ (bởi vì), câu hỏi nguyên nhân phải dùng „Warum“ (tại sao) -> Đáp án: Warum.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Warum", "warum"]}
        },

        # --- 3.3. CHIA ĐỘNG TỪ BẤT QUY TẮC (10 CÂU) ---
        {
            "id": 26,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 26: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Das Mädchen ___ im Wohnzimmer ein Buch.“ (lesen)",
            "options": null,
            "correct_answer": "liest",
            "explanation": "Chủ ngữ „Das Mädchen“ (ngôi es), động từ bất quy tắc „lesen“ đổi e → ie thành „liest“ -> Đáp án: liest.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["liest"]}
        },
        {
            "id": 27,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 27: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Er ___ am Sonntag nach Hamburg.“ (fahren)",
            "options": null,
            "correct_answer": "fährt",
            "explanation": "Ngôi „er“, động từ bất quy tắc „fahren“ đổi a → ä thành „fährt“ -> Đáp án: fährt.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["fährt", "faehrt"]}
        },
        {
            "id": 28,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 28: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Was ___ du heute zum Frühstück?“ (essen)",
            "options": null,
            "correct_answer": "isst",
            "explanation": "Ngôi „du“, động từ bất quy tắc „essen“ đổi e → i thành „isst“ -> Đáp án: isst.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["isst"]}
        },
        {
            "id": 29,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 29: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Der Tourist ___ fließend Deutsch.“ (sprechen)",
            "options": null,
            "correct_answer": "spricht",
            "explanation": "Chủ ngữ „Der Tourist“ (ngôi er), động từ „sprechen“ đổi e → i thành „spricht“ -> Đáp án: spricht.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["spricht"]}
        },
        {
            "id": 30,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 30: Chia động từ mệnh lệnh ngôi du của động từ trong ngoặc:\n„Bitte ___ mir den Zucker!“ (geben - ngôi du)",
            "options": null,
            "correct_answer": "gib",
            "explanation": "Mệnh lệnh ngôi du của động từ bất quy tắc „geben“ (e → i) lược bỏ đuôi -st thành „gib“ -> Đáp án: gib.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["gib", "Gib"]}
        },
        {
            "id": 31,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 31: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Wann ___ er seine neue Freundin?“ (treffen)",
            "options": null,
            "correct_answer": "trifft",
            "explanation": "Ngôi „er“, động từ bất quy tắc „treffen“ đổi e → i thành „trifft“ -> Đáp án: trifft.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["trifft"]}
        },
        {
            "id": 32,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 32: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Der Hund ___ gemütlich auf dem Sofa.“ (schlafen)",
            "options": null,
            "correct_answer": "schläft",
            "explanation": "Chủ ngữ „Der Hund“ (ngôi er), động từ „schlafen“ đổi a → ä thành „schläft“ -> Đáp án: schläft.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["schläft", "schlaeft"]}
        },
        {
            "id": 33,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 33: Chia động từ trong ngoặc theo đúng chủ ngữ:\n„Ihr ___ am Wochenende zu lange!“ (schlafen)",
            "options": null,
            "correct_answer": "schlaft",
            "explanation": "LƯU Ý QUAN TRỌNG: Ngôi ihr (các bạn) KHÔNG BAO GIỜ biến âm. „schlafen“ chỉ thêm đuôi -t thành „schlaft“ -> Đáp án: schlaft.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["schlaft"]}
        },
        {
            "id": 34,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 34: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„___ du gern Romane oder Zeitungen?“ (lesen)",
            "options": null,
            "correct_answer": "Liest",
            "explanation": "Ngôi „du“, động từ bất quy tắc „lesen“ đổi e → ie đứng đầu câu hỏi là „Liest“ -> Đáp án: Liest.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Liest", "liest"]}
        },
        {
            "id": 35,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 35: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Die Chefin ___ gerade mit einem Kunden.“ (sprechen)",
            "options": null,
            "correct_answer": "spricht",
            "explanation": "Chủ ngữ „Die Chefin“ (ngôi sie số ít), động từ „sprechen“ đổi e → i thành „spricht“ -> Đáp án: spricht.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["spricht"]}
        },

        # --- 3.4. DỊCH TỪ VIỆT → ĐỨC (5 CÂU) ---
        {
            "id": 36,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 36: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„cà phê“",
            "options": null,
            "correct_answer": "der Kaffee",
            "explanation": "Cà phê trong tiếng Đức là danh từ giống đực: „der Kaffee“ -> Đáp án: der Kaffee.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["der Kaffee", "Kaffee", "der kaffee", "kaffee"]}
        },
        {
            "id": 37,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 37: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„trà“",
            "options": null,
            "correct_answer": "der Tee",
            "explanation": "Trà trong tiếng Đức là danh từ giống đực: „der Tee“ -> Đáp án: der Tee.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["der Tee", "Tee", "der tee", "tee"]}
        },
        {
            "id": 38,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 38: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„rau củ“",
            "options": null,
            "correct_answer": "das Gemüse",
            "explanation": "Rau củ trong tiếng Đức là danh từ giống trung: „das Gemüse“ -> Đáp án: das Gemüse.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["das Gemüse", "Gemüse", "das Gemuese", "Gemuese", "das gemüse", "gemüse"]}
        },
        {
            "id": 39,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 39: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„bức thư“",
            "options": null,
            "correct_answer": "der Brief",
            "explanation": "Bức thư trong tiếng Đức là danh từ giống đực: „der Brief“ -> Đáp án: der Brief.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["der Brief", "Brief", "der brief", "brief"]}
        },
        {
            "id": 40,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 40: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„tòa thị chính“",
            "options": null,
            "correct_answer": "das Rathaus",
            "explanation": "Tòa thị chính là danh từ ghép giống trung (der Rat + das Haus) -> „das Rathaus“ -> Đáp án: das Rathaus.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["das Rathaus", "Rathaus", "das rathaus", "rathaus"]}
        },

        # --- 3.5. DỊCH TỪ / CÂU NGẮN ĐỨC → VIỆT (5 CÂU) ---
        {
            "id": 41,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 41: Dịch câu giao tiếp sau sang tiếng Việt:\n„Entschuldigung, ist hier frei?“",
            "options": null,
            "correct_answer": "Xin lỗi, chỗ này còn trống không?",
            "explanation": "Câu hỏi lịch sự phổ biến khi muốn ngồi vào bàn còn trống ở quán: „Xin lỗi, chỗ này còn trống không?“ -> Đáp án: Xin lỗi, chỗ này còn trống không?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Xin lỗi, chỗ này còn trống không?", "Xin lỗi chỗ này còn trống không?", "Xin lỗi, ở đây còn trống không?", "Xin lỗi ở đây còn trống không?", "Xin lỗi, chỗ này trống không?", "Xin lỗi chỗ này trống không?"]}
        },
        {
            "id": 42,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 42: Dịch câu đáp lại sau sang tiếng Việt:\n„Ja klar, bitte.“",
            "options": null,
            "correct_answer": "Vâng tất nhiên, xin mời.",
            "explanation": "Câu trả lời đồng ý nhiệt tình cho người khác ngồi cùng bàn: „Vâng tất nhiên, xin mời.“ -> Đáp án: Vâng tất nhiên, xin mời..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Vâng tất nhiên, xin mời.", "Vâng, xin mời.", "Tất nhiên rồi, xin mời.", "Vâng tất nhiên xin mời.", "Được chứ, xin mời.", "Tất nhiên, xin mời."]}
        },
        {
            "id": 43,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 43: Dịch câu gọi món sau sang tiếng Việt:\n„Zwei Kaffee, bitte!“",
            "options": null,
            "correct_answer": "Xin cho hai cà phê!",
            "explanation": "Cách gọi món nhanh và lịch sự trong quán cà phê: „Xin cho hai cà phê!“ -> Đáp án: Xin cho hai cà phê!.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Xin cho hai cà phê!", "Hai cà phê, làm ơn!", "Cho hai cà phê!", "Làm ơn cho hai cà phê!", "Hai ly cà phê, làm ơn!", "Hai cốc cà phê, làm ơn!"]}
        },
        {
            "id": 44,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 44: Dịch danh từ sau sang tiếng Việt:\n„das Futter“",
            "options": null,
            "correct_answer": "thức ăn thú cưng",
            "explanation": "Danh từ „das Futter“ dùng riêng để chỉ thức ăn dành cho thú cưng / động vật -> Đáp án: thức ăn thú cưng.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["thức ăn thú cưng", "thức ăn cho thú", "thức ăn động vật", "thức ăn gia súc", "thức ăn cho động vật", "thức ăn"]}
        },
        {
            "id": 45,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 45: Dịch danh từ sau sang tiếng Việt:\n„der Käse“",
            "options": null,
            "correct_answer": "phô mai",
            "explanation": "Danh từ „der Käse“ trong tiếng Đức nghĩa là „phô mai“ -> Đáp án: phô mai.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["phô mai", "pho mát", "pho mai", "phomai"]}
        },

        # --- 3.6. NỐI Ô TƯƠNG ỨNG (10 BÀI) ---
        {
            "id": 46,
            "exercise_type": "noi_o",
            "question": "Câu 46: Nối đại từ nhân xưng với dạng chia tương ứng của động từ sprechen (e → i):",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Ngôi ich/ihr giữ nguyên nguyên âm e (spreche, sprecht), ngôi du/er biến âm e thành i (sprichst, spricht) -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "spreche"},
                    {"left": "du", "right": "sprichst"},
                    {"left": "er", "right": "spricht"},
                    {"left": "ihr", "right": "sprecht"}
                ]
            }
        },
        {
            "id": 47,
            "exercise_type": "noi_o",
            "question": "Câu 47: Nối đại từ nhân xưng với dạng chia tương ứng của động từ fahren (a → ä):",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Ngôi du và cô ấy biến âm a thành ä (fährst, fährt); ngôi ihr và wir không biến âm (fahrt, fahren) -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "wir", "right": "fahren"},
                    {"left": "du", "right": "fährst"},
                    {"left": "sie (cô ấy)", "right": "fährt"},
                    {"left": "ihr", "right": "fahrt"}
                ]
            }
        },
        {
            "id": 48,
            "exercise_type": "noi_o",
            "question": "Câu 48: Nối đại từ nhân xưng với dạng chia tương ứng của động từ schlafen (a → ä):",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Động từ schlafen biến âm a thành ä ở ngôi du (schläfst) và es (schläft); ngôi ihr giữ nguyên a (schlaft) -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "schlafe"},
                    {"left": "du", "right": "schläfst"},
                    {"left": "es", "right": "schläft"},
                    {"left": "ihr", "right": "schlaft"}
                ]
            }
        },
        {
            "id": 49,
            "exercise_type": "noi_o",
            "question": "Câu 49: Nối câu hỏi W-Fragen với câu trả lời tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Woher đi với giới từ Aus; Wo đi với giới từ In; Wie hỏi tên; Was hỏi đồ uống -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Woher kommen Sie?", "right": "Aus Vietnam."},
                    {"left": "Wo wohnen Sie?", "right": "In Berlin."},
                    {"left": "Wie heißen Sie?", "right": "Ich bin Anna."},
                    {"left": "Was trinken Sie?", "right": "Kaffee, bitte."}
                ]
            }
        },
        {
            "id": 50,
            "exercise_type": "noi_o",
            "question": "Câu 50: Nối danh từ tiếng Đức với nghĩa tiếng Việt tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "der Zucker: đường, das Rathaus: tòa thị chính, der Brief: bức thư, der Hund: con chó -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "der Zucker", "right": "đường"},
                    {"left": "das Rathaus", "right": "tòa thị chính"},
                    {"left": "der Brief", "right": "bức thư"},
                    {"left": "der Hund", "right": "con chó"}
                ]
            }
        },
        {
            "id": 51,
            "exercise_type": "noi_o",
            "question": "Câu 51: Nối câu thoại trong quán cà phê với câu phản hồi phù hợp:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Khớp các phản hồi chuẩn trong giao tiếp quán Cafe -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Ist hier frei?", "right": "Ja klar, bitte."},
                    {"left": "Was möchten Sie trinken?", "right": "Einen Tee, bitte."},
                    {"left": "Ich bin John.", "right": "Ich heiße Maria."},
                    {"left": "Trinkst du Kaffee oder Tee?", "right": "Kaffee mit Zucker."}
                ]
            }
        },
        {
            "id": 52,
            "exercise_type": "noi_o",
            "question": "Câu 52: Nối đại từ nhân xưng với dạng chia tương ứng của động từ lesen (e → ie):",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Động từ lesen biến âm e thành ie ở ngôi du (liest) và er (liest); ngôi ihr giữ nguyên e (lest) -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "lese"},
                    {"left": "du", "right": "liest"},
                    {"left": "er", "right": "liest"},
                    {"left": "ihr", "right": "lest"}
                ]
            }
        },
        {
            "id": 53,
            "exercise_type": "noi_o",
            "question": "Câu 53: Nối động từ nguyên thể với nghĩa tiếng Việt tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "geben: cho/đưa; treffen: gặp gỡ; reisen: du lịch; grillen: nướng BBQ -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "geben", "right": "cho, đưa"},
                    {"left": "treffen", "right": "gặp gỡ"},
                    {"left": "reisen", "right": "du lịch"},
                    {"left": "grillen", "right": "nướng BBQ"}
                ]
            }
        },
        {
            "id": 54,
            "exercise_type": "noi_o",
            "question": "Câu 54: Nối đại từ nhân xưng với dạng chia đúng của động từ sein và haben:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "ich đi với bin; du đi với bist; wir đi với haben; er đi với hat -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "bin"},
                    {"left": "du", "right": "bist"},
                    {"left": "wir", "right": "haben"},
                    {"left": "er", "right": "hat"}
                ]
            }
        },
        {
            "id": 55,
            "exercise_type": "noi_o",
            "question": "Câu 55: Nối chủ ngữ với vị ngữ chứa động từ essen (e → i):",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Das Mädchen (es) -> isst Eis; Die Kinder (Plural) -> essen Eis; Ich -> esse Eis; Ihr -> esst Eis -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Das Mädchen", "right": "isst Eis."},
                    {"left": "Die Kinder", "right": "essen Eis."},
                    {"left": "Ich", "right": "esse Eis."},
                    {"left": "Ihr", "right": "esst Eis."}
                ]
            }
        },

        # --- 3.7. ĐIỀN 2 CHỖ TRỐNG TẠO CÂU (8 CÂU) ---
        {
            "id": 56,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 56: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„[1] heißt du và woher [2] du?“",
            "options": null,
            "correct_answer": "Wie / kommst",
            "explanation": "Hỏi tên dùng từ để hỏi „Wie“; chủ ngữ ngôi du đi với kommen thành „kommst“ -> Đáp án: Wie / kommst.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "[1] heißt du und woher [2] du?",
                "accepted_answers": ["Wie / kommst", "Wie/kommst", "Wie kommst", "wie / kommst", "wie/kommst"]
            }
        },
        {
            "id": 57,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 57: Điền 2 dạng động từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Die Touristen [1] das Rathaus und [2] Fotos.“ (besuchen / machen)",
            "options": null,
            "correct_answer": "besuchen / machen",
            "explanation": "Chủ ngữ „Die Touristen“ (số nhiều) đi với động từ nguyên thể „besuchen“ và „machen“ -> Đáp án: besuchen / machen.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Die Touristen [1] das Rathaus und [2] Fotos.",
                "accepted_answers": ["besuchen / machen", "besuchen/machen", "besuchen machen"]
            }
        },
        {
            "id": 58,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 58: Điền 2 dạng động từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Mein Bruder [1] am Wochenende nach München. Er [2] dort Freunde.“ (fahren / treffen)",
            "options": null,
            "correct_answer": "fährt / trifft",
            "explanation": "Chủ ngữ „Mein Bruder“ (er) đi với fahren biến âm thành „fährt“ và treffen biến âm thành „trifft“ -> Đáp án: fährt / trifft.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Mein Bruder [1] am Wochenende nach München. Er [2] dort Freunde.",
                "accepted_answers": ["fährt / trifft", "fährt/trifft", "faehrt / trifft", "faehrt/trifft", "fährt trifft"]
            }
        },
        {
            "id": 59,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 59: Điền từ để hỏi và động từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„[1] schläft das Baby? — Es [2] im Schlafzimmer.“ (Wo / schlafen)",
            "options": null,
            "correct_answer": "Wo / schläft",
            "explanation": "Hỏi nơi chốn dùng từ để hỏi „Wo“; chủ ngữ „Es“ đi với schlafen đổi a → ä thành „schläft“ -> Đáp án: Wo / schläft.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "[1] schläft das Baby? — Es [2] im Schlafzimmer.",
                "accepted_answers": ["Wo / schläft", "Wo/schläft", "Wo / schlaeft", "Wo/schlaeft", "Wo schläft", "wo / schläft"]
            }
        },
        {
            "id": 60,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 60: Điền 2 dạng động từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Wir [1] gern Fleisch, aber Anna [2] lieber Gemüse.“ (grillen)",
            "options": null,
            "correct_answer": "grillen / grillt",
            "explanation": "Chủ ngữ „Wir“ đi với nguyên thể „grillen“; chủ ngữ „Anna“ (ngôi sie số ít) thêm đuôi -t thành „grillt“ -> Đáp án: grillen / grillt.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Wir [1] gern Fleisch, aber Anna [2] lieber Gemüse.",
                "accepted_answers": ["grillen / grillt", "grillen/grillt", "grillen grillt"]
            }
        },
        {
            "id": 61,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 61: Điền 2 dạng động từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Was [1] ihr? Kaffee oder Tee? — Wir [2] Tee.“ (trinken)",
            "options": null,
            "correct_answer": "trinkt / trinken",
            "explanation": "Ngôi „ihr“ đi với „trinkt“; ngôi „wir“ đi với động từ nguyên thể „trinken“ -> Đáp án: trinkt / trinken.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Was [1] ihr? Kaffee oder Tee? — Wir [2] Tee.",
                "accepted_answers": ["trinkt / trinken", "trinkt/trinken", "trinkt trinken"]
            }
        },
        {
            "id": 62,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 62: Điền từ để hỏi và giới từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„[1] kommen Sie? — [2] der Türkei.“",
            "options": null,
            "correct_answer": "Woher / Aus",
            "explanation": "Hỏi quê quán/xuất xứ dùng từ để hỏi „Woher“ và câu trả lời dùng giới từ „Aus“ -> Đáp án: Woher / Aus.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "[1] kommen Sie? — [2] der Türkei.",
                "accepted_answers": ["Woher / Aus", "Woher/Aus", "Woher Aus", "woher / aus", "woher/aus"]
            }
        },
        {
            "id": 63,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 63: Điền từ để hỏi và dạng động từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„[1] isst du gern? — Ich [2] gern Käse.“ (essen)",
            "options": null,
            "correct_answer": "Was / esse",
            "explanation": "Hỏi ăn món gì dùng từ để hỏi „Was“; chủ ngữ ngôi „ich“ đi với động từ thêm -e thành „esse“ -> Đáp án: Was / esse.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "[1] isst du gern? — Ich [2] gern Käse.",
                "accepted_answers": ["Was / esse", "Was/esse", "Was esse", "was / esse", "was/esse"]
            }
        },

        # --- 3.8. NGHE GIỌNG BẢN XỨ VÀ ĐIỀN TỪ (8 CÂU) ---
        {
            "id": 64,
            "exercise_type": "nghe_dien",
            "question": "Câu 64: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nDer Vater ___ die Zeitung.",
            "options": null,
            "correct_answer": "liest",
            "explanation": "Động từ bất quy tắc lesen ngôi er đổi e → ie là „liest“ -> Đáp án: liest.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Der Vater liest die Zeitung.",
                "display_sentence": "Der Vater ___ die Zeitung.",
                "full_sentence": "Der Vater liest die Zeitung.",
                "translation": "Người bố đọc báo.",
                "accepted_answers": ["liest"]
            }
        },
        {
            "id": 65,
            "exercise_type": "nghe_dien",
            "question": "Câu 65: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nWann ___ ihr nach Hause?",
            "options": null,
            "correct_answer": "fahrt",
            "explanation": "Ngôi ihr không biến âm, phát âm âm a ngắn trong „fahrt“ -> Đáp án: fahrt.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Wann fahrt ihr nach Hause?",
                "display_sentence": "Wann ___ ihr nach Hause?",
                "full_sentence": "Wann fahrt ihr nach Hause?",
                "translation": "Khi nào các bạn về nhà?",
                "accepted_answers": ["fahrt"]
            }
        },
        {
            "id": 66,
            "exercise_type": "nghe_dien",
            "question": "Câu 66: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nIch komme ___ Vietnam.",
            "options": null,
            "correct_answer": "aus",
            "explanation": "Giới từ chỉ nơi xuất xứ đi với kommen là „aus“ -> Đáp án: aus.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Ich komme aus Vietnam.",
                "display_sentence": "Ich komme ___ Vietnam.",
                "full_sentence": "Ich komme aus Vietnam.",
                "translation": "Tôi đến từ Việt Nam.",
                "accepted_answers": ["aus"]
            }
        },
        {
            "id": 67,
            "exercise_type": "nghe_dien",
            "question": "Câu 67: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nDas Kind ___ ein Eis.",
            "options": null,
            "correct_answer": "isst",
            "explanation": "Chủ ngữ Das Kind (ngôi es), động từ essen đổi e → i thành „isst“ -> Đáp án: isst.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Das Kind isst ein Eis.",
                "display_sentence": "Das Kind ___ ein Eis.",
                "full_sentence": "Das Kind isst ein Eis.",
                "translation": "Đứa trẻ ăn một cây kem.",
                "accepted_answers": ["isst"]
            }
        },
        {
            "id": 68,
            "exercise_type": "nghe_dien",
            "question": "Câu 68: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\n___ du Deutsch?",
            "options": null,
            "correct_answer": "Sprichst",
            "explanation": "Động từ sprechen đổi e → i ở ngôi du đứng đầu câu hỏi Yes/No viết hoa: „Sprichst“ -> Đáp án: Sprichst.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Sprichst du Deutsch?",
                "display_sentence": "___ du Deutsch?",
                "full_sentence": "Sprichst du Deutsch?",
                "translation": "Bạn có nói tiếng Đức không?",
                "accepted_answers": ["Sprichst", "sprichst"]
            }
        },
        {
            "id": 69,
            "exercise_type": "nghe_dien",
            "question": "Câu 69: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nWir wohnen ___ Berlin.",
            "options": null,
            "correct_answer": "in",
            "explanation": "Giới từ chỉ địa điểm cư trú trong thành phố là „in“ -> Đáp án: in.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Wir wohnen in Berlin.",
                "display_sentence": "Wir wohnen ___ Berlin.",
                "full_sentence": "Wir wohnen in Berlin.",
                "translation": "Chúng tôi sống ở Berlin.",
                "accepted_answers": ["in"]
            }
        },
        {
            "id": 70,
            "exercise_type": "nghe_dien",
            "question": "Câu 70: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nZwei ___, bitte!",
            "options": null,
            "correct_answer": "Kaffee",
            "explanation": "Từ cần điền là danh từ đồ uống „Kaffee“ -> Đáp án: Kaffee.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Zwei Kaffee, bitte!",
                "display_sentence": "Zwei ___, bitte!",
                "full_sentence": "Zwei Kaffee, bitte!",
                "translation": "Xin cho hai cà phê!",
                "accepted_answers": ["Kaffee", "kaffee"]
            }
        },
        {
            "id": 71,
            "exercise_type": "nghe_dien",
            "question": "Câu 71: Nghe phát âm và điền 1 từ còn thiếu vào chỗ trống:\nDer Hund ___ auf dem Sofa.",
            "options": null,
            "correct_answer": "schläft",
            "explanation": "Chủ ngữ Der Hund (er), động từ schlafen đổi a → ä thành „schläft“ -> Đáp án: schläft.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Der Hund schläft auf dem Sofa.",
                "display_sentence": "Der Hund ___ auf dem Sofa.",
                "full_sentence": "Der Hund schläft auf dem Sofa.",
                "translation": "Chú chó ngủ trên ghế sofa.",
                "accepted_answers": ["schläft", "schlaeft"]
            }
        },

        # --- 3.9. DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (8 CÂU) ---
        {
            "id": 72,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 72: Dịch câu sau sang tiếng Đức:\n„Tôi đến từ nước Đức.“",
            "options": null,
            "correct_answer": "Ich komme aus Deutschland.",
            "explanation": "Chủ ngữ Ich + động từ komme + giới từ xuất xứ aus + tên quốc gia Deutschland -> Đáp án: Ich komme aus Deutschland..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Ich komme aus Deutschland.", "Ich komme aus Deutschland"]}
        },
        {
            "id": 73,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 73: Dịch câu sau sang tiếng Đức:\n„Bạn sống ở đâu?“",
            "options": null,
            "correct_answer": "Wo wohnst du?",
            "explanation": "Từ để hỏi Wo + động từ wohnen chia theo ngôi du là „Wo wohnst du?“ (hoặc ngôi Sie: „Wo wohnen Sie?“) -> Đáp án: Wo wohnst du?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Wo wohnst du?", "Wo wohnst du", "Wo wohnen Sie?", "Wo wohnen Sie"]}
        },
        {
            "id": 74,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 74: Dịch câu sau sang tiếng Đức:\n„Ông nội tôi đọc báo.“",
            "options": null,
            "correct_answer": "Mein Großvater liest die Zeitung.",
            "explanation": "Chủ ngữ Mein Großvater / Mein Opa (ngôi er), động từ lesen đổi e → ie thành „liest“ + die Zeitung -> Đáp án: Mein Großvater liest die Zeitung..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Mein Großvater liest die Zeitung.", "Mein Großvater liest die Zeitung", "Mein Opa liest die Zeitung.", "Mein Opa liest die Zeitung", "Mein Opa liest eine Zeitung.", "Mein Opa liest Zeitung.", "Mein Großvater liest eine Zeitung.", "Mein Großvater liest Zeitung."]}
        },
        {
            "id": 75,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 75: Dịch câu sau sang tiếng Đức:\n„Cô ấy đi Berlin.“",
            "options": null,
            "correct_answer": "Sie fährt nach Berlin.",
            "explanation": "Chủ ngữ Sie (cô ấy) đi với fahren đổi a → ä thành „fährt“ + giới từ nach Berlin -> Đáp án: Sie fährt nach Berlin..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Sie fährt nach Berlin.", "Sie fährt nach Berlin", "Sie faehrt nach Berlin.", "Sie faehrt nach Berlin"]}
        },
        {
            "id": 76,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 76: Dịch câu sau sang tiếng Đức:\n„Anh ấy gặp bạn bè của anh ấy.“",
            "options": null,
            "correct_answer": "Er trifft seine Freunde.",
            "explanation": "Chủ ngữ Er đi với động từ treffen đổi e → i thành „trifft“ + tân ngữ seine Freunde -> Đáp án: Er trifft seine Freunde..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Er trifft seine Freunde.", "Er trifft seine Freunde"]}
        },
        {
            "id": 77,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 77: Dịch câu sau sang tiếng Đức:\n„Chúng tôi ăn kem.“",
            "options": null,
            "correct_answer": "Wir essen Eis.",
            "explanation": "Chủ ngữ Wir đi với động từ nguyên thể „essen“ + Eis -> Đáp án: Wir essen Eis..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Wir essen Eis.", "Wir essen Eis", "Wir essen ein Eis.", "Wir essen ein Eis"]}
        },
        {
            "id": 78,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 78: Dịch câu sau sang tiếng Đức:\n„Các bạn ngủ ở khách sạn phải không?“",
            "options": null,
            "correct_answer": "Schlaft ihr im Hotel?",
            "explanation": "Câu hỏi Yes/No đảo động từ lên đầu; ngôi ihr KHÔNG biến âm nên chia là „Schlaft ihr im Hotel?“ -> Đáp án: Schlaft ihr im Hotel?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Schlaft ihr im Hotel?", "Schlaft ihr im Hotel"]}
        },
        {
            "id": 79,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 79: Dịch câu sau sang tiếng Đức:\n„Ngài muốn uống gì ạ?“",
            "options": null,
            "correct_answer": "Was möchten Sie trinken?",
            "explanation": "Câu hỏi lịch sự trong quán dùng động từ khuyết thiếu: „Was möchten Sie trinken?“ -> Đáp án: Was möchten Sie trinken?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Was möchten Sie trinken?", "Was möchten Sie trinken", "Was moechten Sie trinken?", "Was moechten Sie trinken"]}
        },

        # --- 3.10. DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (7 CÂU) ---
        {
            "id": 80,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 80: Dịch câu sau sang tiếng Việt:\n„Wie ist Ihr Name?“",
            "options": null,
            "correct_answer": "Tên của ngài là gì?",
            "explanation": "Câu hỏi tên trang trọng trong tiếng Đức: „Tên của ngài là gì?“ -> Đáp án: Tên của ngài là gì?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Tên của ngài là gì?", "Tên của ngài là gì", "Tên ngài là gì?", "Tên ngài là gì", "Ngài tên là gì?", "Ngài tên là gì", "Tên của ông là gì?", "Tên của bà là gì?"]}
        },
        {
            "id": 81,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 81: Dịch câu sau sang tiếng Việt:\n„Entschuldigung, ist hier frei?“",
            "options": null,
            "correct_answer": "Xin lỗi, chỗ này còn trống không?",
            "explanation": "Câu hỏi xin phép ngồi ghế trống trong quán: „Xin lỗi, chỗ này còn trống không?“ -> Đáp án: Xin lỗi, chỗ này còn trống không?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Xin lỗi, chỗ này còn trống không?", "Xin lỗi, chỗ này còn trống không", "Xin lỗi chỗ này còn trống không?", "Xin lỗi chỗ này còn trống không", "Xin lỗi, ở đây còn trống không?", "Xin lỗi ở đây còn trống không?"]}
        },
        {
            "id": 82,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 82: Dịch câu sau sang tiếng Việt:\n„Ich trinke Tee mit Zucker.“",
            "options": null,
            "correct_answer": "Tôi uống trà với đường.",
            "explanation": "mit Zucker = với đường / có đường: „Tôi uống trà với đường.“ -> Đáp án: Tôi uống trà với đường..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Tôi uống trà với đường.", "Tôi uống trà với đường", "Tôi uống trà có đường.", "Tôi uống trà có đường", "Tôi uống trà đường."]}
        },
        {
            "id": 83,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 83: Dịch câu sau sang tiếng Việt:\n„Der Lehrer spricht zu leise.“",
            "options": null,
            "correct_answer": "Thầy giáo nói quá nhỏ.",
            "explanation": "spricht = nói, zu leise = quá nhỏ/quá khẽ: „Thầy giáo nói quá nhỏ.“ -> Đáp án: Thầy giáo nói quá nhỏ..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Thầy giáo nói quá nhỏ.", "Thầy giáo nói quá nhỏ", "Giáo viên nói quá nhỏ.", "Giáo viên nói quá nhỏ", "Thầy giáo nói quá khẽ.", "Thầy giáo nói quá khẽ"]}
        },
        {
            "id": 84,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 84: Dịch câu sau sang tiếng Việt:\n„Hannes gibt dem Hund das Futter.“",
            "options": null,
            "correct_answer": "Hannes cho chú chó thức ăn.",
            "explanation": "gibt dem Hund = cho chú chó, das Futter = thức ăn: „Hannes cho chú chó thức ăn.“ -> Đáp án: Hannes cho chú chó thức ăn..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Hannes cho chú chó thức ăn.", "Hannes cho chú chó thức ăn", "Hannes cho chó ăn thức ăn.", "Hannes cho chó ăn thức ăn", "Hannes đưa thức ăn cho chú chó.", "Hannes đưa thức ăn cho chó."]}
        },
        {
            "id": 85,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 85: Dịch câu sau sang tiếng Việt:\n„Fährst du am Wochenende nach Polen?“",
            "options": null,
            "correct_answer": "Cuối tuần bạn có đi Ba Lan không?",
            "explanation": "Fährst du = bạn có đi/lái xe..., am Wochenende = vào cuối tuần: „Cuối tuần bạn có đi Ba Lan không?“ -> Đáp án: Cuối tuần bạn có đi Ba Lan không?.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Cuối tuần bạn có đi Ba Lan không?", "Cuối tuần bạn có đi Ba Lan không", "Bạn có đi Ba Lan vào cuối tuần không?", "Bạn có đi Ba Lan vào cuối tuần không"]}
        },
        {
            "id": 86,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 86: Dịch câu sau sang tiếng Việt:\n„Karin wohnt in München.“",
            "options": null,
            "correct_answer": "Karin sống ở München.",
            "explanation": "wohnt in München = sống ở München: „Karin sống ở München.“ -> Đáp án: Karin sống ở München..",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["Karin sống ở München.", "Karin sống ở München", "Karin sống tại München.", "Karin sống tại München"]}
        },

        # --- 3.11. SẮP XẾP TỪ THÀNH CÂU (10 CÂU) ---
        {
            "id": 87,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 87: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Im Sommer essen die Kinder gern Eis.",
            "explanation": "Trạng ngữ „Im Sommer“ đứng đầu thì động từ „essen“ đứng ở vị trí 2, tiếp theo là chủ ngữ „die Kinder“ -> Đáp án: Im Sommer essen die Kinder gern Eis..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["die Kinder", "essen", "Eis", "Im Sommer", "gern"],
                "accepted_answers": ["Im Sommer essen die Kinder gern Eis.", "Die Kinder essen im Sommer gern Eis."]
            }
        },
        {
            "id": 88,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 88: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Reist ihr nach Italien?",
            "explanation": "Câu hỏi Yes/No đảo động từ „Reist“ lên đầu câu, sau đó đến chủ ngữ „ihr“ -> Đáp án: Reist ihr nach Italien?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["ihr", "nach", "Reist", "Italien", "?"],
                "accepted_answers": ["Reist ihr nach Italien?"]
            }
        },
        {
            "id": 89,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 89: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Wo wohnen Sie in Berlin?",
            "explanation": "Từ để hỏi „Wo“ đứng đầu, động từ „wohnen“ ở vị trí 2, tiếp đến chủ ngữ „Sie“ -> Đáp án: Wo wohnen Sie in Berlin?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["wohnen", "Sie", "in Berlin", "Wo", "?"],
                "accepted_answers": ["Wo wohnen Sie in Berlin?"]
            }
        },
        {
            "id": 90,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 90: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Was trinkt der Opa am Morgen?",
            "explanation": "Từ để hỏi „Was“ đứng đầu, động từ „trinkt“ ở vị trí 2, chủ ngữ „der Opa“ -> Đáp án: Was trinkt der Opa am Morgen?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["trinkt", "Was", "am Morgen", "der Opa", "?"],
                "accepted_answers": ["Was trinkt der Opa am Morgen?"]
            }
        },
        {
            "id": 91,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 91: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Der Großvater liest am Morgen die Zeitung.",
            "explanation": "Chủ ngữ „Der Großvater“, động từ „liest“ vị trí 2, trạng ngữ „am Morgen“, tân ngữ „die Zeitung“ -> Đáp án: Der Großvater liest am Morgen die Zeitung..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["die Zeitung", "Der Großvater", "am Morgen", "liest"],
                "accepted_answers": ["Der Großvater liest am Morgen die Zeitung.", "Am Morgen liest der Großvater die Zeitung."]
            }
        },
        {
            "id": 92,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 92: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Hannes gibt dem Hund das Futter.",
            "explanation": "Chủ ngữ „Hannes“, động từ „gibt“ ở vị trí 2, tân ngữ Dativ „dem Hund“, tân ngữ Akkusativ „das Futter“ -> Đáp án: Hannes gibt dem Hund das Futter..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["dem Hund", "Hannes", "das Futter", "gibt"],
                "accepted_answers": ["Hannes gibt dem Hund das Futter.", "Dem Hund gibt Hannes das Futter."]
            }
        },
        {
            "id": 93,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 93: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Wir schlafen heute im Hotel.",
            "explanation": "Chủ ngữ „Wir“, động từ „schlafen“ ở vị trí 2, thời gian „heute“, địa điểm „im Hotel“ -> Đáp án: Wir schlafen heute im Hotel..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["im Hotel", "schlafen", "Wir", "heute"],
                "accepted_answers": ["Wir schlafen heute im Hotel.", "Heute schlafen wir im Hotel."]
            }
        },
        {
            "id": 94,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 94: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Der Lehrer spricht fließend Deutsch.",
            "explanation": "Chủ ngữ „Der Lehrer“, động từ „spricht“ ở vị trí 2, bổ ngữ „fließend Deutsch“ -> Đáp án: Der Lehrer spricht fließend Deutsch..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["spricht", "Der Lehrer", "Deutsch", "fließend"],
                "accepted_answers": ["Der Lehrer spricht fließend Deutsch.", "Fließend Deutsch spricht der Lehrer."]
            }
        },
        {
            "id": 95,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 95: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Heute treffe ich meine Freunde.",
            "explanation": "Trạng từ thời gian „Heute“ đứng đầu câu, động từ „treffe“ ở vị trí 2, chủ ngữ „ich“ -> Đáp án: Heute treffe ich meine Freunde..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["treffe", "ich", "Heute", "meine Freunde"],
                "accepted_answers": ["Heute treffe ich meine Freunde.", "Ich treffe heute meine Freunde."]
            }
        },
        {
            "id": 96,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 96: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Woher kommst du?",
            "explanation": "Từ để hỏi „Woher“ đứng đầu, động từ „kommst“ ở vị trí 2, chủ ngữ „du“ -> Đáp án: Woher kommst du?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["kommst", "Woher", "du", "?"],
                "accepted_answers": ["Woher kommst du?"]
            }
        },

        # --- 3.12. PHÂN LOẠI ĐỘNG TỪ (3 BÀI) ---
        {
            "id": 97,
            "exercise_type": "phan_loai_dong_tu",
            "question": "Câu 97: Phân loại 4 động từ sau (lesen, kaufen, fahren, machen) vào nhóm Bất quy tắc (biến âm) hoặc Có quy tắc:",
            "options": null,
            "correct_answer": "Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc",
            "explanation": "lesen (e → ie) và fahren (a → ä) là động từ bất quy tắc; kaufen và machen là động từ có quy tắc -> Đáp án: Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc.",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {"word": "lesen", "meaning_vi": "đọc (e → ie)", "category": "Bất quy tắc"},
                    {"word": "kaufen", "meaning_vi": "mua", "category": "Có quy tắc"},
                    {"word": "fahren", "meaning_vi": "lái xe (a → ä)", "category": "Bất quy tắc"},
                    {"word": "machen", "meaning_vi": "làm", "category": "Có quy tắc"}
                ],
                "categories": ["Bất quy tắc", "Có quy tắc"],
                "accepted_answers": ["Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc", "Bất quy tắc / Có quy tắc / Bất quy tắc / Có quy tắc"]
            }
        },
        {
            "id": 98,
            "exercise_type": "phan_loai_dong_tu",
            "question": "Câu 98: Phân loại 4 động từ sau (sprechen, hören, spielen, treffen) vào nhóm Bất quy tắc (biến âm) hoặc Có quy tắc:",
            "options": null,
            "correct_answer": "Bất quy tắc, Có quy tắc, Có quy tắc, Bất quy tắc",
            "explanation": "sprechen (e → i) và treffen (e → i) là động từ bất quy tắc; hören và spielen là động từ có quy tắc -> Đáp án: Bất quy tắc, Có quy tắc, Có quy tắc, Bất quy tắc.",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {"word": "sprechen", "meaning_vi": "nói (e → i)", "category": "Bất quy tắc"},
                    {"word": "hören", "meaning_vi": "nghe", "category": "Có quy tắc"},
                    {"word": "spielen", "meaning_vi": "chơi", "category": "Có quy tắc"},
                    {"word": "treffen", "meaning_vi": "gặp gỡ (e → i)", "category": "Bất quy tắc"}
                ],
                "categories": ["Bất quy tắc", "Có quy tắc"],
                "accepted_answers": ["Bất quy tắc, Có quy tắc, Có quy tắc, Bất quy tắc", "Bất quy tắc / Có quy tắc / Có quy tắc / Bất quy tắc"]
            }
        },
        {
            "id": 99,
            "exercise_type": "phan_loai_dong_tu",
            "question": "Câu 99: Phân loại 4 động từ sau (schlafen, reisen, geben, grillen) vào nhóm Bất quy tắc (biến âm) hoặc Có quy tắc:",
            "options": null,
            "correct_answer": "Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc",
            "explanation": "schlafen (a → ä) và geben (e → i) là động từ bất quy tắc; reisen và grillen là động từ có quy tắc -> Đáp án: Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc.",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {"word": "schlafen", "meaning_vi": "ngủ (a → ä)", "category": "Bất quy tắc"},
                    {"word": "reisen", "meaning_vi": "du lịch", "category": "Có quy tắc"},
                    {"word": "geben", "meaning_vi": "cho, đưa (e → i)", "category": "Bất quy tắc"},
                    {"word": "grillen", "meaning_vi": "nướng BBQ", "category": "Có quy tắc"}
                ],
                "categories": ["Bất quy tắc", "Có quy tắc"],
                "accepted_answers": ["Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc", "Bất quy tắc / Có quy tắc / Bất quy tắc / Có quy tắc"]
            }
        },

        # --- 3.13. PHÂN LOẠI TỪ ĐỂ HỎI (3 BÀI) ---
        {
            "id": 100,
            "exercise_type": "phan_loai_tu_hoi",
            "question": "Câu 100: Phân loại 4 câu trả lời sau (Aus Vietnam, In Berlin, Anna, Kaffee) tương ứng với từ để hỏi phù hợp (Woher, Wo, Wie, Was):",
            "options": null,
            "correct_answer": "Woher, Wo, Wie, Was",
            "explanation": "Aus đi với Woher, In đi với Wo, Tên người đi với Wie, Đồ uống đi với Was -> Đáp án: Woher, Wo, Wie, Was.",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {"word": "Aus Vietnam.", "meaning_vi": "Từ Việt Nam (xuất xứ)", "category": "Woher"},
                    {"word": "In Berlin.", "meaning_vi": "Ở Berlin (địa điểm)", "category": "Wo"},
                    {"word": "Anna.", "meaning_vi": "Tên riêng", "category": "Wie"},
                    {"word": "Kaffee.", "meaning_vi": "Đồ uống", "category": "Was"}
                ],
                "categories": ["Woher", "Wo", "Wie", "Was"],
                "accepted_answers": ["Woher, Wo, Wie, Was", "Woher / Wo / Wie / Was"]
            }
        },
        {
            "id": 101,
            "exercise_type": "phan_loai_tu_hoi",
            "question": "Câu 101: Phân loại 4 câu trả lời sau (Mein Name ist John, Aus Frankreich, In München, Ein Eis) tương ứng với từ để hỏi phù hợp (Wie, Woher, Wo, Was):",
            "options": null,
            "correct_answer": "Wie, Woher, Wo, Was",
            "explanation": "Mein Name ist... đi với Wie (Wie ist Ihr Name?); Aus đi với Woher; In đi với Wo; Ein Eis đi với Was -> Đáp án: Wie, Woher, Wo, Was.",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {"word": "Mein Name ist John.", "meaning_vi": "Tên tôi là John (hỏi tên)", "category": "Wie"},
                    {"word": "Aus Frankreich.", "meaning_vi": "Từ nước Pháp (xuất xứ)", "category": "Woher"},
                    {"word": "In München.", "meaning_vi": "Ở München (địa điểm)", "category": "Wo"},
                    {"word": "Ein Eis.", "meaning_vi": "Một cây kem (món ăn)", "category": "Was"}
                ],
                "categories": ["Wie", "Woher", "Wo", "Was"],
                "accepted_answers": ["Wie, Woher, Wo, Was", "Wie / Woher / Wo / Was"]
            }
        },
        {
            "id": 102,
            "exercise_type": "phan_loai_tu_hoi",
            "question": "Câu 102: Phân loại 4 câu trả lời sau (Aus der Türkei, Ich heiße Julia, In Hamburg, Einen Tomatensalat) tương ứng với từ để hỏi phù hợp (Woher, Wie, Wo, Was):",
            "options": null,
            "correct_answer": "Woher, Wie, Wo, Was",
            "explanation": "Aus der Türkei đi với Woher; Ich heiße... đi với Wie; In Hamburg đi với Wo; Einen Tomatensalat đi với Was -> Đáp án: Woher, Wie, Wo, Was.",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {"word": "Aus der Türkei.", "meaning_vi": "Từ Thổ Nhĩ Kỳ (xuất xứ)", "category": "Woher"},
                    {"word": "Ich heiße Julia.", "meaning_vi": "Tôi tên là Julia (hỏi tên)", "category": "Wie"},
                    {"word": "In Hamburg.", "meaning_vi": "Ở Hamburg (địa điểm)", "category": "Wo"},
                    {"word": "Einen Tomatensalat.", "meaning_vi": "Món salad cà chua (món ăn)", "category": "Was"}
                ],
                "categories": ["Woher", "Wie", "Wo", "Was"],
                "accepted_answers": ["Woher, Wie, Wo, Was", "Woher / Wie / Wo / Was"]
            }
        },

        # --- 3.14. TÌM LỖI SAI VÀ SỬA LẠI (10 CÂU) ---
        {
            "id": 103,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 103: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Ihr schläft heute Nacht im Hotel, oder?“",
            "options": null,
            "correct_answer": "Ihr schlaft heute Nacht im Hotel, oder?",
            "explanation": "BẪY QUAN TRỌNG: Ngôi ihr (các bạn) KHÔNG BAO GIỜ biến âm. Động từ schlafen đi với ihr là „schlaft“ (không có Umlaut ä) -> Đáp án: Ihr schlaft heute Nacht im Hotel, oder?.",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Ihr schlaft heute Nacht im Hotel, hoặc?", "Ihr schlaft heute Nacht im Hotel, oder?", "Ihr schlaft heute Nacht im Hotel, oder"]}
        },
        {
            "id": 104,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 104: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Wann treffst du heute deine Freunde?“",
            "options": null,
            "correct_answer": "Wann triffst du heute deine Freunde?",
            "explanation": "Động từ bất quy tắc treffen biến âm e → i ở ngôi du thành „triffst“ -> Đáp án: Wann triffst du heute deine Freunde?.",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Wann triffst du heute deine Freunde?", "Wann triffst du heute deine Freunde"]}
        },
        {
            "id": 105,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 105: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Woher wohnst du in Berlin?“",
            "options": null,
            "correct_answer": "Wo wohnst du in Berlin?",
            "explanation": "Hỏi nơi ở (với giới từ in) phải dùng từ để hỏi „Wo“, không dùng Woher -> Đáp án: Wo wohnst du in Berlin?.",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Wo wohnst du in Berlin?", "Wo wohnst du in Berlin"]}
        },
        {
            "id": 106,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 106: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Das Mädchen lest im Wohnzimmer ein Buch.“",
            "options": null,
            "correct_answer": "Das Mädchen liest im Wohnzimmer ein Buch.",
            "explanation": "Chủ ngữ Das Mädchen mang giống trung (ngôi es). Động từ bất quy tắc lesen đổi e → ie thành „liest“ -> Đáp án: Das Mädchen liest im Wohnzimmer ein Buch..",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Das Mädchen liest im Wohnzimmer ein Buch.", "Das Mädchen liest im Wohnzimmer ein Buch"]}
        },
        {
            "id": 107,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 107: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Ich fahrt am Wochenende ans Meer.“",
            "options": null,
            "correct_answer": "Ich fahre am Wochenende ans Meer.",
            "explanation": "Chủ ngữ ngôi ich đi với động từ thêm đuôi -e bình thường thành „fahre“ -> Đáp án: Ich fahre am Wochenende ans Meer..",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Ich fahre am Wochenende ans Meer.", "Ich fahre am Wochenende ans Meer"]}
        },
        {
            "id": 108,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 108: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Der Lehrer sprechen zu leise.“",
            "options": null,
            "correct_answer": "Der Lehrer spricht zu leise.",
            "explanation": "Chủ ngữ Der Lehrer (ngôi er), động từ sprechen đổi e → i thành „spricht“ -> Đáp án: Der Lehrer spricht zu leise..",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Der Lehrer spricht zu leise.", "Der Lehrer spricht zu leise"]}
        },
        {
            "id": 109,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 109: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Ich komme in Deutschland.“",
            "options": null,
            "correct_answer": "Ich komme aus Deutschland.",
            "explanation": "Động từ kommen diễn tả xuất xứ từ quốc gia nào phải đi kèm giới từ „aus“ -> Đáp án: Ich komme aus Deutschland..",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Ich komme aus Deutschland.", "Ich komme aus Deutschland"]}
        },
        {
            "id": 110,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 110: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Was esst er gern?“",
            "options": null,
            "correct_answer": "Was isst er gern?",
            "explanation": "Chủ ngữ ngôi er, động từ bất quy tắc essen đổi e → i thành „isst“ -> Đáp án: Was isst er gern?.",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Was isst er gern?", "Was isst er gern"]}
        },
        {
            "id": 111,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 111: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Entschuldigung, ist hier frei sein?“",
            "options": null,
            "correct_answer": "Entschuldigung, ist hier frei?",
            "explanation": "Câu đã có động từ tobe ist đứng trước, không để động từ nguyên thể sein ở cuối câu -> Đáp án: Entschuldigung, ist hier frei?.",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Entschuldigung, ist hier frei?", "Entschuldigung, ist hier frei"]}
        },
        {
            "id": 112,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 112: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Hannes und Julia gibt dem Hund das Futter.“",
            "options": null,
            "correct_answer": "Hannes und Julia geben dem Hund das Futter.",
            "explanation": "Chủ ngữ số nhiều (Hannes und Julia - sie số nhiều), động từ giữ nguyên thể „geben“ -> Đáp án: Hannes und Julia geben dem Hund das Futter..",
            "exp_reward": 15,
            "extra_data": {"accepted_answers": ["Hannes und Julia geben dem Hund das Futter.", "Hannes und Julia geben dem Hund das Futter"]}
        },

        # --- 3.15. ĐẶT CÂU HỎI CHO TỪ GẠCH CHÂN (5 CÂU) ---
        {
            "id": 113,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 113: Đặt câu hỏi cho cụm từ in đậm trong câu sau (hỏi ở ngôi du):\n„Ich komme **aus Polen**.“",
            "options": null,
            "correct_answer": "Woher kommst du?",
            "explanation": "Cụm „aus Polen“ chỉ nơi xuất xứ nên hỏi bằng từ để hỏi „Woher“; đổi ngôi ich thành du đi với động từ kommst -> Đáp án: Woher kommst du?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ich komme aus Polen.",
                "target_phrase": "aus Polen",
                "accepted_answers": ["Woher kommst du?", "Woher kommst du"]
            }
        },
        {
            "id": 114,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 114: Đặt câu hỏi cho cụm từ in đậm trong câu sau (hỏi ở ngôi Sie lịch sự):\n„Mein Name ist **Anna**.“",
            "options": null,
            "correct_answer": "Wie ist Ihr Name?",
            "explanation": "Hỏi tên lịch sự ở ngôi Sie dùng cấu trúc „Wie ist Ihr Name?“ hoặc „Wie heißen Sie?“ -> Đáp án: Wie ist Ihr Name?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Mein Name ist Anna.",
                "target_phrase": "Anna",
                "accepted_answers": ["Wie ist Ihr Name?", "Wie ist Ihr Name", "Wie heißen Sie?", "Wie heißen Sie"]
            }
        },
        {
            "id": 115,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 115: Đặt câu hỏi cho cụm từ in đậm trong câu sau (hỏi ở ngôi du):\n„Ich wohne **in Ha Noi**.“",
            "options": null,
            "correct_answer": "Wo wohnst du?",
            "explanation": "Cụm „in Ha Noi“ chỉ địa điểm cư trú nên hỏi bằng từ để hỏi „Wo“; đổi ngôi ich thành du đi với wohnst -> Đáp án: Wo wohnst du?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ich wohne in Ha Noi.",
                "target_phrase": "in Ha Noi",
                "accepted_answers": ["Wo wohnst du?", "Wo wohnst du"]
            }
        },
        {
            "id": 116,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 116: Đặt câu hỏi cho cụm từ in đậm trong câu sau (hỏi ở ngôi ihr):\n„Wir trinken **Kaffee**.“",
            "options": null,
            "correct_answer": "Was trinkt ihr?",
            "explanation": "Từ „Kaffee“ chỉ đồ vật/đồ uống nên hỏi bằng „Was“; đổi ngôi wir thành ihr đi với động từ „trinkt“ -> Đáp án: Was trinkt ihr?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Wir trinken Kaffee.",
                "target_phrase": "Kaffee",
                "accepted_answers": ["Was trinkt ihr?", "Was trinkt ihr"]
            }
        },
        {
            "id": 117,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 117: Đặt câu hỏi cho cụm từ in đậm trong câu sau (hỏi ở ngôi sie - cô ấy):\n„Sie kommt **aus der Türkei**.“",
            "options": null,
            "correct_answer": "Woher kommt sie?",
            "explanation": "Cụm „aus der Türkei“ chỉ xuất xứ nên hỏi bằng „Woher“; giữ nguyên chủ ngữ ngôi 3 số ít sie và động từ kommt -> Đáp án: Woher kommt sie?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Sie kommt aus der Türkei.",
                "target_phrase": "aus der Türkei",
                "accepted_answers": ["Woher kommt sie?", "Woher kommt sie"]
            }
        },

        # --- 3.16. ĐÚNG HAY SAI (3 CÂU) ---
        {
            "id": 118,
            "exercise_type": "dung_sai",
            "question": "Câu 118: Đọc đoạn văn sau và chọn Đúng (Richtig) hoặc Sai (Falsch):\nNhận định: „David kommt aus Deutschland.“",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Falsch",
            "explanation": "Nhận định này là SAI (Falsch) vì trong bài đọc nói rõ David đến từ Tây Ban Nha („Er kommt aus Spanien“), không phải từ nước Đức -> Đáp án: Falsch.",
            "exp_reward": 10,
            "extra_data": {
                "reading_text": "Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker.",
                "reading_translation_vi": "Đây là David. Anh ấy đến từ Tây Ban Nha, nhưng hiện tại anh ấy sống ở Berlin. Vào cuối tuần, anh ấy thường đi xe đạp vào công viên. Anh ấy thích đọc sách và ăn pizza. Hôm nay anh ấy gặp Maria ở quán cà phê. Họ cùng nhau uống cà phê với nhiều đường.",
                "accepted_answers": ["Falsch"]
            }
        },
        {
            "id": 119,
            "exercise_type": "dung_sai",
            "question": "Câu 119: Đọc đoạn văn sau và chọn Đúng (Richtig) hoặc Sai (Falsch):\nNhận định: „Maria und David trinken Kaffee.“",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Richtig",
            "explanation": "Nhận định này là ĐÚNG (Richtig) vì đoạn văn viết: „Sie trinken zusammen Kaffee mit viel Zucker“ -> Đáp án: Richtig.",
            "exp_reward": 10,
            "extra_data": {
                "reading_text": "Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker.",
                "reading_translation_vi": "Đây là David. Anh ấy đến từ Tây Ban Nha, nhưng hiện tại anh ấy sống ở Berlin. Vào cuối tuần, anh ấy thường đi xe đạp vào công viên. Anh ấy thích đọc sách và ăn pizza. Hôm nay anh ấy gặp Maria ở quán cà phê. Họ cùng nhau uống cà phê với nhiều đường.",
                "accepted_answers": ["Richtig"]
            }
        },
        {
            "id": 120,
            "exercise_type": "dung_sai",
            "question": "Câu 120: Đọc đoạn văn sau và chọn Đúng (Richtig) hoặc Sai (Falsch):\nNhận định: „David isst gern Pizza und liest Bücher.“",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Richtig",
            "explanation": "Nhận định này là ĐÚNG (Richtig) vì đoạn văn viết: „Er liest gern Bücher und isst Pizza“ -> Đáp án: Richtig.",
            "exp_reward": 10,
            "extra_data": {
                "reading_text": "Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker.",
                "reading_translation_vi": "Đây là David. Anh ấy đến từ Tây Ban Nha, nhưng hiện tại anh ấy sống ở Berlin. Vào cuối tuần, anh ấy thường đi xe đạp vào công viên. Anh ấy thích đọc sách và ăn pizza. Hôm nay anh ấy gặp Maria ở quán cà phê. Họ cùng nhau uống cà phê với nhiều đường.",
                "accepted_answers": ["Richtig"]
            }
        },

        # --- 3.17. SẮP XẾP HỘI THOẠI (3 CÂU) ---
        {
            "id": 121,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 121: Sắp xếp các câu thoại sau theo đúng diễn biến một cuộc hội thoại tại quán cà phê:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5, 6",
            "explanation": "Thứ tự logic: Khách hỏi chỗ trống -> Anna mời ngồi -> Khách cảm ơn & tự giới thiệu -> Anna giới thiệu lại -> Bồi bàn hỏi món -> Khách gọi 2 cà phê -> Đáp án: 1, 2, 3, 4, 5, 6.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Gast", "text": "Entschuldigung, ist hier frei?"},
                    {"id": 2, "speaker": "Anna", "text": "Ja klar, bitte. Setzen Sie sich."},
                    {"id": 3, "speaker": "Gast", "text": "Danke. Ich bin John aus Frankreich, und du?"},
                    {"id": 4, "speaker": "Anna", "text": "Ich heiße Anna. Ich komme aus Polen."},
                    {"id": 5, "speaker": "Kellner", "text": "Was möchtet ihr trinken: Kaffee oder Tee?"},
                    {"id": 6, "speaker": "Gast", "text": "Zwei Kaffee mit Zucker, bitte!"}
                ],
                "correct_order": [1, 2, 3, 4, 5, 6],
                "translation": "- Khách: Xin lỗi, chỗ này còn trống không?\n- Anna: Vâng tất nhiên, xin mời. Ngài hãy ngồi xuống đi.\n- Khách: Cảm ơn bạn. Tôi là John đến từ Pháp, còn bạn?\n- Anna: Tôi tên là Anna. Tôi đến từ Ba Lan.\n- Bồi bàn: Các bạn muốn uống gì: cà phê hay trà?\n- Khách: Cho hai cà phê có đường, xin cảm ơn!"
            }
        },
        {
            "id": 122,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 122: Sắp xếp các câu thoại sau theo đúng diễn biến một cuộc làm quen lịch sự:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5, 6",
            "explanation": "Thứ tự logic: Chào hỏi ban đầu -> Giới thiệu tên và hỏi lại -> Giới thiệu tên và hỏi xuất xứ -> Trả lời xuất xứ -> Hỏi nơi ở hiện tại -> Trả lời nơi ở -> Đáp án: 1, 2, 3, 4, 5, 6.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Maria", "text": "Guten Tag! Wer sind Sie?"},
                    {"id": 2, "speaker": "David", "text": "Guten Tag, mein Name ist David. Und wie heißen Sie?"},
                    {"id": 3, "speaker": "Maria", "text": "Ich bin Maria. Woher kommen Sie, David?"},
                    {"id": 4, "speaker": "David", "text": "Ich komme aus Deutschland."},
                    {"id": 5, "speaker": "Maria", "text": "Und wo wohnen Sie jetzt?"},
                    {"id": 6, "speaker": "David", "text": "Ich wohne in Berlin."}
                ],
                "correct_order": [1, 2, 3, 4, 5, 6],
                "translation": "- Maria: Xin chào! Ngài là ai ạ?\n- David: Xin chào, tên tôi là David. Còn ngài tên là gì?\n- Maria: Tôi là Maria. Ngài đến từ đâu vậy David?\n- David: Tôi đến từ nước Đức.\n- Maria: Và hiện tại ngài sống ở đâu?\n- David: Tôi sống ở Berlin."
            }
        },
        {
            "id": 123,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 123: Sắp xếp các câu thoại sau theo đúng diễn biến cuộc đối thoại rủ rê bạn bè:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5, 6",
            "explanation": "Thứ tự logic: Hỏi thời gian gặp bạn -> Trả lời thời gian & địa điểm -> Hỏi hoạt động dự định -> Trả lời hoạt động -> Chúc vui vẻ -> Cảm ơn -> Đáp án: 1, 2, 3, 4, 5, 6.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Lukas", "text": "Hallo! Wann triffst du heute deine Freunde?"},
                    {"id": 2, "speaker": "Paul", "text": "Hallo! Wir treffen uns um 15 Uhr im Café."},
                    {"id": 3, "speaker": "Lukas", "text": "Was macht ihr dort?"},
                    {"id": 4, "speaker": "Paul", "text": "Wir trinken Kaffee und essen Kuchen."},
                    {"id": 5, "speaker": "Lukas", "text": "Das klingt gut! Viel Spaß!"},
                    {"id": 6, "speaker": "Paul", "text": "Danke!"}
                ],
                "correct_order": [1, 2, 3, 4, 5, 6],
                "translation": "- Lukas: Xin chào! Hôm nay khi nào bạn gặp bạn bè thế?\n- Paul: Chào bạn! Chúng tôi gặp nhau lúc 15 giờ ở quán cà phê.\n- Lukas: Các bạn làm gì ở đó?\n- Paul: Chúng tôi uống cà phê và ăn bánh ngọt.\n- Lukas: Nghe hay đấy! Chúc vui vẻ nhé!\n- Paul: Cảm ơn bạn!"
            }
        },

        # --- 3.18. ĐỌC MENU CHỌN PHẢN HỒI (2 CÂU) ---
        {
            "id": 124,
            "exercise_type": "doc_menu_cafe",
            "question": "Câu 124: Nhìn vào bảng thực đơn sau và chọn câu trả lời đúng của khách khi bồi bàn hỏi:\n📋 Thực đơn: Kaffee (2,50 €), Tee (2,00 €), Kuchen (3,00 €)\nBồi bàn hỏi: „Was möchten Sie trinken?“",
            "options": [
                "Ich trinke einen Kaffee.",
                "Ich esse Kuchen.",
                "Ich heiße Anna.",
                "Ich komme aus Vietnam."
            ],
            "correct_answer": "Ich trinke einen Kaffee.",
            "explanation": "Bồi bàn hỏi khách muốn uống gì („Was möchten Sie trinken?“), câu trả lời phù hợp trong thực đơn đồ uống là „Ich trinke einen Kaffee.“ -> Đáp án: Ich trinke einen Kaffee..",
            "exp_reward": 10,
            "extra_data": {
                "menu_items": [
                    {"name": "Kaffee", "price": "2,50 €"},
                    {"name": "Tee", "price": "2,00 €"},
                    {"name": "Kuchen", "price": "3,00 €"}
                ],
                "accepted_answers": ["Ich trinke einen Kaffee."]
            }
        },
        {
            "id": 125,
            "exercise_type": "doc_menu_cafe",
            "question": "Câu 125: Nhìn vào bảng thực đơn sau và chọn câu trả lời đúng khi bạn của bạn hỏi:\n📋 Thực đơn: Pizza (6,50 €), Tomatensalat (4,00 €), Eis (2,00 €)\nBạn hỏi: „Was essen wir jetzt?“",
            "options": [
                "Wir essen ein Eis.",
                "Wir trinken Kaffee.",
                "Wir schlafen.",
                "Wir fahren."
            ],
            "correct_answer": "Wir essen ein Eis.",
            "explanation": "Câu hỏi về món ăn („Was essen wir jetzt?“), trong các phương án chỉ có món ăn phù hợp với thực đơn là „Wir essen ein Eis.“ -> Đáp án: Wir essen ein Eis..",
            "exp_reward": 10,
            "extra_data": {
                "menu_items": [
                    {"name": "Pizza", "price": "6,50 €"},
                    {"name": "Tomatensalat", "price": "4,00 €"},
                    {"name": "Eis", "price": "2,00 €"}
                ],
                "accepted_answers": ["Wir essen ein Eis."]
            }
        }
    ]

    for ex in exercises_data:
        options_json = json.dumps(ex["options"], ensure_ascii=False) if ex["options"] else None
        extra_data_json = json.dumps(ex["extra_data"], ensure_ascii=False) if ex["extra_data"] else None
        
        cursor.execute("""
            INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (lesson_id, ex["exercise_type"], ex["question"], options_json, ex["correct_answer"], ex["explanation"], ex["exp_reward"], extra_data_json))

    conn.commit()
    print(f"Đã nạp thành công {len(exercises_data)} bài tập (18 dạng bài) cho Bài 13.")
    conn.close()

if __name__ == "__main__":
    seed_lesson_13()
