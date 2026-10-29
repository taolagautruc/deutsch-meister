import json
import os
import sys

# Đảm bảo đường dẫn import hoạt động dù chạy từ thư mục con hay thư mục gốc
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_1_part_1():
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
        return
    a1_id = level_a1["id"]

    # Xóa dữ liệu cũ của Bài 1 (P1) để nạp lại sạch sẽ
    cursor.execute("DELETE FROM lessons WHERE level_id = ? AND title LIKE 'Bài 1 (P1)%';", (a1_id,))

    lesson_title = 'Bài 1 (P1): "Làm Quen Với Tiếng Đức, Bảng Chữ Cái và Đếm Số"'

    # 1. DANH SÁCH 30 CHỮ CÁI: 26 CHỮ LATINH + 4 KÝ TỰ ĐẶC BIỆT
    # Chuẩn hóa theo tài liệu: Chữ hoa/thường, phiên âm IPA, cách đọc tiếng Việt, từ phát âm TTS
    alphabet_data = [
        ("A a", "/aː/", "đọc như a", "A"),
        ("B b", "/beː/", "đọc như bê", "B"),
        ("C c", "/tseː/", "đọc như tsê", "C"),
        ("D d", "/deː/", "đọc như đê", "D"),
        ("E e", "/eː/", "đọc như ê", "E"),
        ("F f", "/ɛf/", "đọc như ép-phờ", "F"),
        ("G g", "/geː/", "đọc như ghê", "G"),
        ("H h", "/haː/", "đọc như ha", "H"),
        ("I i", "/iː/", "đọc như i", "I"),
        ("J j", "/jɔt/", "đọc như dốt", "J"),
        ("K k", "/kaː/", "đọc như ca", "K"),
        ("L l", "/ɛl/", "đọc như en-lờ", "L"),
        ("M m", "/ɛm/", "đọc như em-mờ", "M"),
        ("N n", "/ɛn/", "đọc như en-nờ", "N"),
        ("O o", "/oː/", "đọc như ô", "O"),
        ("P p", "/peː/", "đọc như pê", "P"),
        ("Q q", "/kuː/", "đọc như cu", "Q"),
        ("R r", "/ɛɐ̯/", "đọc như e-rờ rung cuống họng", "R"),
        ("S s", "/ɛs/", "đọc như ét-sờ", "S"),
        ("T t", "/teː/", "đọc như thê bật hơi", "T"),
        ("U u", "/uː/", "đọc như u", "U"),
        ("V v", "/faʊ̯/", "đọc là phao (vào từ: ph)", "V"),
        ("W w", "/veː/", "đọc là vê (vào từ: v)", "W"),
        ("X x", "/ɪks/", "đọc như ích-xờ", "X"),
        ("Y y", "/ˈʏpsilɔn/", "đọc như uýp-xi-lon", "Y"),
        ("Z z", "/tsɛt/", "đọc như tsét", "Z"),
        # 4 chữ cái đặc biệt (Umlaut & Eszett)
        ("Ä ä", "/ɛː/", "a-Umlaut (mở miệng đọc ê)", "Ä"),
        ("Ö ö", "/øː/", "o-Umlaut (tròn môi chữ ô đọc ê)", "Ö"),
        ("Ü ü", "/yː/", "u-Umlaut (tròn môi chữ u đọc uy)", "Ü"),
        ("ß", "/ɛsˈtsɛt/", "Eszett (đọc như s kéo dài)", "ß")
    ]

    alpha_cards = "".join([
        f"""<div onclick="speakGerman('{tts}')" class="cursor-pointer p-3 rounded-2xl bg-slate-50/90 hover:bg-indigo-50/80 border border-slate-200/90 hover:border-indigo-400 hover:shadow-md transition-all duration-200 group flex flex-col justify-between">
            <div class="flex items-center justify-between">
                <span class="font-black text-base text-slate-900 group-hover:text-indigo-600 transition">{char}</span>
                <span class="w-6 h-6 rounded-lg bg-white group-hover:bg-indigo-600 text-indigo-600 group-hover:text-white flex items-center justify-center text-xs shadow-xs transition">🔊</span>
            </div>
            <div class="mt-2 font-mono text-xs font-bold text-amber-700 bg-amber-50/80 px-2 py-0.5 rounded-md inline-block border border-amber-200/60">{ipa}</div>
            <div class="text-[11px] text-slate-500 font-medium mt-1 leading-snug">{vi}</div>
        </div>"""
        for char, ipa, vi, tts in alphabet_data
    ])

    # Giao diện lý thuyết không có link YouTube, mang thương hiệu DeutschMeister
    grammar_html = f"""
    <div class="space-y-6 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI HỌC DEUTSCHMEISTER (ĐÃ BỎ LINK YOUTUBE) -->
        <div class="p-6 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Bài Học Khởi Đầu (P1)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 45 phút • ⚡ 500+ EXP
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Khám Phá Nền Tảng Tiếng Đức: Bảng Chữ Cái, Ghép Âm & Số Đếm (0 - 9999)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Nắm vững 26 chữ cái Latinh, 4 ký tự đặc biệt (Ä, Ö, Ü, ß), quy tắc ghép âm chuẩn bản xứ, mẫu câu chào hỏi - giới thiệu bản thân và hệ thống số đếm từ 0 đến 9999.
                </p>
                <div class="flex flex-wrap items-center gap-3 pt-2 text-xs">
                    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/10 text-slate-200 border border-white/10">
                        <span class="text-emerald-400">✓</span> 30 Thẻ chữ cái tương tác & Audio
                    </div>
                    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/10 text-slate-200 border border-white/10">
                        <span class="text-emerald-400">✓</span> 30 Thẻ từ vựng có mạo từ der/die/das
                    </div>
                    <div class="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/10 text-slate-200 border border-white/10">
                        <span class="text-emerald-400">✓</span> 50 Câu bài tập kèm Random số đếm
                    </div>
                </div>
            </div>
        </div>

        <!-- PHẦN 1: BẢNG CHỮ CÁI CÓ PHIÊN ÂM & VOICE TỪNG CHỮ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-3">
                <div>
                    <h4 class="text-base font-extrabold text-indigo-700 uppercase tracking-wide flex items-center gap-2">
                        <span>1. Bảng Chữ Cái Tiếng Đức (Das Alphabet) & 4 Ký Tự Đặc Biệt</span>
                    </h4>
                    <p class="text-xs text-slate-500 mt-1">💡 Bấm trực tiếp vào từng ô chữ cái để nghe phát âm chuẩn tiếng Đức kèm phiên âm quốc tế (IPA).</p>
                </div>
                <button onclick="speakGerman('A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Ä, Ö, Ü, Eszett', 0.85)" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-sm hover:shadow transition flex items-center gap-2">
                    <span>🔊</span> Đọc mẫu toàn bộ Bảng chữ cái
                </button>
            </div>

            <!-- Lưới 30 thẻ chữ cái tương tác -->
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 lg:grid-cols-6 gap-3">
                {alpha_cards}
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs pt-3">
                <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-1.5">
                    <p class="font-bold text-amber-900 text-sm flex items-center gap-1.5">
                        <span>✨</span> Khẩu hình 4 chữ cái đặc biệt (Umlaut & Eszett):
                    </p>
                    <p>• <b>Ä / ä /ɛː/</b>: <i>a-Umlaut</i> — miệng mở rộng đọc âm <b>ê</b> (<i>Qualität, Universität</i>)</p>
                    <p>• <b>Ö / ö /øː/</b>: <i>o-Umlaut</i> — giữ tròn môi chữ <b>ô</b> nhưng phát âm chữ <b>ê</b> (<i>mögen, hören</i>)</p>
                    <p>• <b>Ü / ü /yː/</b>: <i>u-Umlaut</i> — giữ tròn môi chữ <b>u</b> nhưng phát âm chữ <b>uy</b> (<i>müde, Küche</i>)</p>
                    <p>• <b>ß /ɛsˈtsɛt/</b>: <i>Eszett</i> — đọc như âm <b>s</b> kéo dài (<i>heißen, dreißig</i>)</p>
                </div>
                <div class="p-4 rounded-2xl bg-emerald-50/70 border border-emerald-200 space-y-2">
                    <p class="font-bold text-emerald-900 text-sm flex items-center gap-1.5">
                        <span>🏙️</span> Luyện đánh vần 4 thành phố Đức (Bấm để nghe):
                    </p>
                    <div class="space-y-1.5 font-mono text-emerald-950">
                        <div class="flex items-center justify-between bg-white/70 p-1.5 rounded-lg border border-emerald-200/60">
                            <span>1) <b>HAMBURG</b>: ha - a - em - be - u - er - ge</span>
                            <div class="flex gap-1">
                                <button onclick="speakGerman('Hamburg')" class="px-2 py-0.5 rounded bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-bold">🔊 Từ</button>
                                <button onclick="speakGerman('H, A, M, B, U, R, G')" class="px-2 py-0.5 rounded bg-white hover:bg-emerald-50 text-emerald-700 border border-emerald-300 text-[11px]">🔤 Từng chữ</button>
                            </div>
                        </div>
                        <div class="flex items-center justify-between bg-white/70 p-1.5 rounded-lg border border-emerald-200/60">
                            <span>2) <b>FRANKFURT</b>: ef - er - a - en - ka - ef - u - er - te</span>
                            <div class="flex gap-1">
                                <button onclick="speakGerman('Frankfurt')" class="px-2 py-0.5 rounded bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-bold">🔊 Từ</button>
                                <button onclick="speakGerman('F, R, A, N, K, F, U, R, T')" class="px-2 py-0.5 rounded bg-white hover:bg-emerald-50 text-emerald-700 border border-emerald-300 text-[11px]">🔤 Từng chữ</button>
                            </div>
                        </div>
                        <div class="flex items-center justify-between bg-white/70 p-1.5 rounded-lg border border-emerald-200/60">
                            <span>3) <b>BERLIN</b>: be - e - er - el - i - en</span>
                            <div class="flex gap-1">
                                <button onclick="speakGerman('Berlin')" class="px-2 py-0.5 rounded bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-bold">🔊 Từ</button>
                                <button onclick="speakGerman('B, E, R, L, I, N')" class="px-2 py-0.5 rounded bg-white hover:bg-emerald-50 text-emerald-700 border border-emerald-300 text-[11px]">🔤 Từng chữ</button>
                            </div>
                        </div>
                        <div class="flex items-center justify-between bg-white/70 p-1.5 rounded-lg border border-emerald-200/60">
                            <span>4) <b>MÜNCHEN</b>: em - ü - en - ce - ha - e - en</span>
                            <div class="flex gap-1">
                                <button onclick="speakGerman('München')" class="px-2 py-0.5 rounded bg-emerald-600 hover:bg-emerald-700 text-white text-[11px] font-bold">🔊 Từ</button>
                                <button onclick="speakGerman('M, Ü, N, C, H, E, N')" class="px-2 py-0.5 rounded bg-white hover:bg-emerald-50 text-emerald-700 border border-emerald-300 text-[11px]">🔤 Từng chữ</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PHẦN 2: QUY TẮC ĐÁNH VẦN & PHÁT ÂM -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-3">
            <h4 class="text-base font-extrabold text-indigo-700 uppercase tracking-wide">2. Quy Tắc Đánh Vần Nguyên Âm Ghép & Phụ Âm</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <p class="font-extrabold text-slate-900 text-sm">🅰️ Nguyên âm đôi & Tổ hợp có -r:</p>
                    <p>• <b>ei [aɪ̯]</b> → đọc là <b>ai</b>: <button onclick="speakGerman('mein, dein, eins, zwei, drei')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 mein, dein, eins, zwei, drei</button></p>
                    <p>• <b>ie [iː]</b> → đọc là <b>i kéo dài</b> (tuyệt đối không đọc "đai"): <button onclick="speakGerman('die, Sie, vier, sieben')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 die, Sie, vier, sieben</button></p>
                    <p>• <b>eu / äu [ɔʏ̯]</b> → đọc là <b>oi</b>: <button onclick="speakGerman('Deutsch, Verkäufer, neun')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Deutsch, Verkäufer, neun</button></p>
                    <p>• <b>ir</b> (i-ơ ngắn): <i>mir, dir</i> | <b>ier</b> (i-ơ dài): <button onclick="speakGerman('hier, das Bier, das Tier')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 hier, Bier, Tier</button></p>
                    <p>• <b>ur</b> (u-ơ): <i>Kurs, Burg</i> | <b>ür</b> (uy-ơ): <button onclick="speakGerman('die Tür, für')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Tür, für</button></p>
                    <p>• <b>or</b> (o): <i>Tor, sorgen</i> | <b>er</b> (e): <i>der, wer, woher</i></p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <p class="font-extrabold text-slate-900 text-sm">🅱️ Phụ âm & Tổ hợp phụ âm đặc trưng:</p>
                    <p>• <b>s</b> (trước nguyên âm) → đọc như <b>z/d</b>: <button onclick="speakGerman('Sie, sorgen, sieben')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Sie, sorgen, sieben</button></p>
                    <p>• <b>v</b> → đọc như <b>ph (f)</b>: <button onclick="speakGerman('der Vater, vier')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Vater, vier</button> | <b>w</b> → đọc như <b>v</b>: <i>was, wer</i></p>
                    <p>• <b>z [ts]</b> → siết hai hàm răng đọc <b>ts</b>: <button onclick="speakGerman('der Zahn, der Zoo, zehn, zwei')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Zahn, Zoo, zehn</button></p>
                    <p>• <b>ch</b>: sau <b>a, o, u, au</b> đọc như <b>kh</b> (<button onclick="speakGerman('auch, der Koch')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 auch, Koch</button>); còn lại đọc nhẹ (<button onclick="speakGerman('mich, dich, ich')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 mich, dich, ich</button>)</p>
                    <p>• <b>sch [ʃ]</b> (chu môi s nặng): <button onclick="speakGerman('die Schule, die Schuhe')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Schule, Schuhe</button></p>
                    <p>• <b>sp / st</b> (đầu từ) → đọc s như <b>sch</b>: <button onclick="speakGerman('der Sport, das Spiel, die Stadt, der Stuhl')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Sport, Spiel, Stadt, Stuhl</button></p>
                    <p>• <b>tsch [tʃ]</b> (ch nặng): <button onclick="speakGerman('Tschüss, Deutsch')" class="text-indigo-600 font-bold underline hover:text-indigo-800">🔊 Tschüss, Deutsch</button></p>
                </div>
            </div>
        </div>

        <!-- PHẦN 3 & 4: CHÀO HỎI & GIỚI THIỆU -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-2 text-xs sm:text-sm">
                <h4 class="text-base font-extrabold text-indigo-700 uppercase tracking-wide">3. Chào Hỏi & Tạm Biệt</h4>
                <p>• <b>Hallo!</b>: Xin chào (lịch sự) | <b>Hi! / Grüß dich! / Hallöchen!</b>: Chào thân mật</p>
                <p>• <b>Guten Morgen</b>: Chào buổi sáng | <b>Guten Tag</b>: Chào buổi trưa/chiều</p>
                <p>• <b>Guten Abend</b>: Chào buổi tối | <b>Gute Nacht</b>: Chúc ngủ ngon</p>
                <p>• <b>Tschüss!</b> [tʃʏs]: Tạm biệt | <b>Auf Wiedersehen!</b>: Hẹn gặp lại (trang trọng)</p>
                <p>• <b>Bis dann / Bis morgen / Bis später</b>: Hẹn gặp sau / Hẹn ngày mai / Hẹn lát gặp</p>
            </div>
            <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-2 text-xs sm:text-sm">
                <h4 class="text-base font-extrabold text-indigo-700 uppercase tracking-wide">4. 5 Mẫu Câu Giới Thiệu Bản Thân</h4>
                <p>1) <b>Wer sind Sie?</b> → <i>Ich bin Anna.</i></p>
                <p>2) <b>Wie ist Ihr Name?</b> → <i>Mein Name ist Anna.</i></p>
                <p>3) <b>Wie heißen Sie?</b> → <i>Ich heiße Anna.</i></p>
                <p>4) <b>Woher kommen Sie?</b> → <i>Ich komme <b>aus</b> Vietnam.</i></p>
                <p>5) <b>Wo wohnen Sie?</b> → <i>Ich wohne <b>in</b> Hai Phong.</i></p>
            </div>
        </div>

        <!-- PHẦN 5: HỆ THỐNG SỐ ĐẾM (0 – 9999) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-3 text-xs sm:text-sm">
            <h4 class="text-base font-extrabold text-indigo-700 uppercase tracking-wide">5. Hệ Thống Số Đếm (0 – 9999)</h4>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-slate-900 mb-1">Số 0 – 12:</p>
                    <p>0: <b>null</b> | 1: <b>eins</b> | 2: <b>zwei</b> | 3: <b>drei</b> | 4: <b>vier</b> | 5: <b>fünf</b> | 6: <b>sechs</b> | 7: <b>sieben</b> | 8: <b>acht</b> | 9: <b>neun</b> | 10: <b>zehn</b> | 11: <b>elf</b> | 12: <b>zwölf</b></p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-slate-900 mb-1">Số 13 – 19 (Đơn vị + zehn):</p>
                    <p>13: <b>dreizehn</b> | 14: <b>vierzehn</b> | 15: <b>fünfzehn</b> | <span class="text-red-600 font-bold">16: sechzehn (bỏ s)</span> | <span class="text-red-600 font-bold">17: siebzehn (bỏ en)</span> | 18: <b>achtzehn</b> | 19: <b>neunzehn</b></p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-slate-900 mb-1">Số tròn chục, trăm, nghìn:</p>
                    <p>20: <b>zwanzig</b> | <span class="text-red-600 font-bold">30: dreißig (ß)</span> | 40: <b>vierzig</b> | 50: <b>fünfzig</b> | <span class="text-red-600 font-bold">60: sechzig</span> | <span class="text-red-600 font-bold">70: siebzig</span> | 80: <b>achtzig</b> | 90: <b>neunzig</b> | 100: <b>(ein)hundert</b> | 1000: <b>(ein)tausend</b></p>
                </div>
            </div>
            <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-200 space-y-1.5">
                <p class="font-extrabold text-indigo-950">🔢 Quy tắc ghép số (Viết liền một từ duy nhất):</p>
                <p>• <b>21–99</b>: <b>[Đơn vị] + und + [Chục]</b> (Số 1 bỏ <i>s</i> thành <b>ein</b>: 21 = <i>einundzwanzig</i>, 34 = <i>vierunddreißig</i>).</p>
                <p>• <b>100–9999</b>: <b>[Nghìn] + [Trăm] + [2 số cuối]</b> (Không có <i>und</i> sau hundert/tausend: 707 = <i>siebenhundertsieben</i>, 912 = <i>neunhundertzwölf</i>).</p>
            </div>
        </div>
    </div>
    """

    cursor.execute("INSERT INTO lessons (level_id, title, grammar_content) VALUES (?, ?, ?);", (a1_id, lesson_title, grammar_html))
    lesson_id = cursor.lastrowid

    # 2. 30 THẺ TỪ VỰNG (Chuẩn mạo từ der/die/das và câu ví dụ)
    vocabs = [
        (lesson_id, "Verkäufer", "der", "Người bán hàng (nam)", "Der Verkäufer ist freundlich. (Người bán hàng rất thân thiện.)"),
        (lesson_id, "Kurs", "der", "Khóa học", "Der Deutschkurs beginnt heute. (Khóa học tiếng Đức bắt đầu hôm nay.)"),
        (lesson_id, "Stuhl", "der", "Cái ghế", "Der Stuhl ist neu. (Cái ghế này mới.)"),
        (lesson_id, "Vater", "der", "Người cha / Bố", "Mein Vater wohnt in Berlin. (Bố tôi sống ở Berlin.)"),
        (lesson_id, "Zahn", "der", "Cái răng", "Der Zahn ist weiß. (Cái răng màu trắng.)"),
        (lesson_id, "Zoo", "der", "Sở thú", "Wir gehen in den Zoo. (Chúng tôi đi sở thú.)"),
        (lesson_id, "Koch", "der", "Đầu bếp (nam)", "Der Koch kocht rất gut. (Người đầu bếp nấu ăn rất ngon.)"),
        (lesson_id, "Sport", "der", "Thể thao", "Sport ist gesund. (Thể thao tốt cho sức khỏe.)"),
        (lesson_id, "Tag", "der", "Ngày / Buổi trưa chiều", "Guten Tag! Wie geht es Ihnen? (Xin chào! Ngài có khỏe không?)"),
        (lesson_id, "Morgen", "der", "Buổi sáng", "Guten Morgen! (Chào buổi sáng!)"),
        (lesson_id, "Abend", "der", "Buổi tối", "Guten Abend! (Chào buổi tối!)"),
        (lesson_id, "Name", "der", "Tên", "Mein Name ist Anna. (Tên của tôi là Anna.)"),
        (lesson_id, "Qualität", "die", "Chất lượng", "Die Qualität ist sehr gut. (Chất lượng rất tốt.)"),
        (lesson_id, "Universität", "die", "Trường đại học", "Die Universität ist in Berlin. (Trường đại học ở Berlin.)"),
        (lesson_id, "Küche", "die", "Nhà bếp", "Die Küche ist sauber. (Nhà bếp sạch sẽ.)"),
        (lesson_id, "Burg", "die", "Lâu đài / Thành cổ", "Die Burg in Hamburg ist alt. (Lâu đài ở Hamburg đã cổ.)"),
        (lesson_id, "Tür", "die", "Cánh cửa", "Die Tür ist offen. (Cánh cửa đang mở.)"),
        (lesson_id, "Ruhe", "die", "Sự yên tĩnh", "Bitte Ruhe! (Xin hãy giữ yên lặng!)"),
        (lesson_id, "Schule", "die", "Trường học", "Die Schule ist groß. (Trường học rất lớn.)"),
        (lesson_id, "Stadt", "die", "Thành phố", "Berlin ist eine schöne Stadt. (Berlin là một thành phố đẹp.)"),
        (lesson_id, "Nacht", "die", "Ban đêm", "Gute Nacht! (Chúc ngủ ngon!)"),
        (lesson_id, "Bier", "das", "Bia", "Das Bier aus Deutschland ist gut. (Bia từ nước Đức rất ngon.)"),
        (lesson_id, "Tier", "das", "Con vật / Động vật", "Das Tier ist im Zoo. (Con vật ở trong sở thú.)"),
        (lesson_id, "Tor", "das", "Cái cổng / Khung thành", "Das Brandenburger Tor ist in Berlin. (Cổng Brandenburg ở Berlin.)"),
        (lesson_id, "Rad", "das", "Bánh xe / Xe đạp", "Ich fahre mit dem Rad. (Tôi đi bằng xe đạp.)"),
        (lesson_id, "Spiel", "das", "Trò chơi / Trận đấu", "Das Spiel ist super. (Trận đấu rất tuyệt vời.)"),
        (lesson_id, "Auf Wiedersehen!", "Mẫu câu", "Hẹn gặp lại (Trang trọng)", "Auf Wiedersehen! Bis morgen! (Hẹn gặp lại! Hẹn ngày mai!)"),
        (lesson_id, "Tschüss!", "Mẫu câu", "Tạm biệt (Thân mật)", "Tschüss! Bis später! (Tạm biệt! Hẹn lát nữa gặp!)"),
        (lesson_id, "Woher kommen Sie?", "Mẫu câu", "Ngài đến từ đâu?", "Woher kommen Sie? Ich komme aus Vietnam. (Ngài đến từ đâu?)"),
        (lesson_id, "Wo wohnen Sie?", "Mẫu câu", "Ngài sống ở đâu?", "Wo wohnen Sie? Ich wohne in Hai Phong. (Ngài sống ở đâu?)")
    ]
    cursor.executemany("INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence) VALUES (?, ?, ?, ?, ?);", vocabs)

    # 3. ĐỦ 50 BÀI TẬP PHÂN BỔ ĐÚNG THEO ĐẶC TẢ:
    # 10 trắc nghiệm + 8 điền khuyết + 8 dịch + 7 nghe + 5 nói + 4 đọc + 8 viết = 50 câu!
    passage_text = "Hội thoại tại lớp học tiếng Đức:\n- Lehrerin: Guten Morgen! Wie heißen Sie?\n- Anna: Guten Morgen! Ich heiße Anna.\n- Lehrerin: Woher kommen Sie, Anna?\n- Anna: Ich komme aus Vietnam.\n- Lehrerin: Und wo wohnen Sie?\n- Anna: Ich wohne in Hai Phong. Meine Hausnummer ist vierunddreißig."

    exercises = [
        # =========================================================================
        # DẠNG 1: TRẮC NGHIỆM (trac_nghiem) - ĐÚNG 10 CÂU (Câu 1 - 10)
        # =========================================================================
        (
            lesson_id, "trac_nghiem",
            "Câu 1: Trong bảng chữ cái tiếng Đức, chữ cái 'J' có phiên âm và cách đọc tên là gì?",
            json.dumps(["/jɔt/ - đọc là dốt", "/ja/ - đọc là gia", "/dʒeɪ/ - đọc là dây", "/ji/ - đọc là gi"]),
            "/jɔt/ - đọc là dốt",
            "Chữ J trong bảng chữ cái tiếng Đức được đọc tên là /jɔt/ (dốt).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 2: Hai chữ cái 'V' và 'W' có tên gọi trong bảng chữ cái lần lượt là:",
            json.dumps(["V /faʊ̯/ (phao) và W /veː/ (vê)", "V /veː/ và W /faʊ̯/", "V /vi/ và W /double-u/", "V /va/ và W /wa/"]),
            "V /faʊ̯/ (phao) và W /veː/ (vê)",
            "Chữ V tên là /faʊ̯/ (vào từ phát âm như ph/f); chữ W tên là /veː/ (vào từ phát âm như v).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 3: Mạo từ 'die' (giống cái) và đại từ 'Sie' (Ngài) chứa nguyên âm đôi 'ie' được phát âm chuẩn là:",
            json.dumps(["Âm 'i' kéo dài /diː/ và /ziː/", "Âm 'ai' /daɪ̯/ như tiếng Anh", "Âm 'ê' /deː/", "Âm 'i-ơ' /diːɐ̯/"]),
            "Âm 'i' kéo dài /diː/ và /ziː/",
            "Trong tiếng Đức, 'ie' luôn đọc là âm 'i kéo dài' (/diː/, /ziː/), tuyệt đối không đọc là 'đai' như tiếng Anh.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 4: Tổ hợp nguyên âm 'eu' và 'äu' (trong 'Deutsch', 'neun', 'Verkäufer') phát âm là:",
            json.dumps(["Âm 'oi' /ɔʏ̯/", "Âm 'ai' /aɪ̯/", "Âm 'êu'", "Âm 'au'"]),
            "Âm 'oi' /ɔʏ̯/",
            "Cả 'eu' và 'äu' đều phát âm là 'oi' /ɔʏ̯/.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 5: Khi tổ hợp 'ch' đứng sau các nguyên âm a, o, u, au (ví dụ: 'auch', 'Koch', 'Buch'), ta phát âm như thế nào?",
            json.dumps(["Đọc như âm 'kh' ở cuống họng /x/", "Đọc như âm 'ch' nhẹ /ç/ (như ich, mich)", "Đọc như âm 'k'", "Đọc như âm 'sch'"]),
            "Đọc như âm 'kh' ở cuống họng /x/",
            "Sau a, o, u, au thì 'ch' đọc như 'kh' (auch, Koch, acht); sau các nguyên âm khác đọc nhẹ (ich, mich, dich).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 6: Khi đứng ở đầu từ, hai tổ hợp 'sp' (Sport, Spiel) và 'st' (Stadt, Stuhl) được phát âm thế nào?",
            json.dumps(["Chữ s được đọc tròn môi như 'sch' (/ʃp/ và /ʃt/)", "Đọc s nhẹ bình thường", "Câm chữ s", "Đọc như chữ z"]),
            "Chữ s được đọc tròn môi như 'sch' (/ʃp/ và /ʃt/)",
            "Quy tắc phát âm: 'sp' và 'st' ở đầu từ luôn đọc chữ s thành âm 'sch' nặng (Sport, Spiel, Stadt, Stuhl).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 7: Khi mới gặp một người lạ hoặc cần chào hỏi lịch sự, bạn nên dùng câu nào?",
            json.dumps(["Hallo! hoặc Guten Tag!", "Hi!", "Hallöchen!", "Grüß dich!"]),
            "Hallo! hoặc Guten Tag!",
            "'Hi', 'Hallöchen', 'Grüß dich' chỉ dùng cho bạn bè thân thiết; với người mới quen ta dùng 'Hallo' hoặc 'Guten Tag'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 8: Đâu là cách viết ĐÚNG của hai số 16 và 17 trong tiếng Đức?",
            json.dumps(["sechzehn và siebzehn", "sechszehn và siebenzehn", "sechzig và siebzig", "sechszig và siebzehn"]),
            "sechzehn và siebzehn",
            "Số 16 (sechzehn) lược bỏ chữ 's' ở sechs; số 17 (siebzehn) lược bỏ đuôi 'en' ở sieben.",
            20, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 9: Đâu là cách viết ĐÚNG của bộ 3 số tròn chục 30, 60 và 70?",
            json.dumps(["dreißig, sechzig, siebzig", "dreizig, sechszig, siebenzig", "dreißig, sechszig, siebzig", "dreizig, sechzig, siebzig"]),
            "dreißig, sechzig, siebzig",
            "30 dùng chữ ß (dreißig), 60 bỏ 's' (sechzig), 70 bỏ 'en' (siebzig).",
            20, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 10 [Random Đọc Số]: Cách viết tiếng Đức chính xác của số 21 là gì?",
            json.dumps(["einundzwanzig", "einsundzwanzig", "zwanzigundeins", "einzwanzig"]),
            "einundzwanzig",
            "Hàng đơn vị đọc trước + und + hàng chục (số 1 bỏ s thành ein): einundzwanzig.",
            20,
            json.dumps({"dynamic_number": True, "dynamic_mode": "mcq_num_to_de", "min": 21, "max": 99})
        ),

        # =========================================================================
        # DẠNG 2: ĐIỀN KHUYẾT (dien_khuyet) - ĐÚNG 8 CÂU (Câu 11 - 18)
        # =========================================================================
        (
            lesson_id, "dien_khuyet",
            "Câu 11: Điền từ để hỏi còn thiếu: '___ sind Sie? -> Ich bin Anna.' (Ngài là ai?)",
            None, "Wer", "'Wer sind Sie?' = Ngài là ai?", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 12: Điền động từ còn thiếu (chú ý chữ ß): 'Wie ___ Sie? -> Ich heiße Anna.'",
            None, "heißen", "'Wie heißen Sie?' = Ngài tên là gì?", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 13: Điền tính từ sở hữu: 'Wie ist ___ Name? -> Mein Name ist Anna.'",
            None, "Ihr", "'Wie ist Ihr Name?' = Tên của Ngài là gì?", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 14: Điền giới từ chỉ quê hương/xuất xứ: 'Woher kommen Sie? -> Ich komme ___ Vietnam.'",
            None, "aus", "Đi với động từ kommen chỉ xuất xứ, ta luôn dùng giới từ 'aus'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 15: Điền giới từ chỉ nơi cư trú: 'Wo wohnen Sie? -> Ich wohne ___ Hai Phong.'",
            None, "in", "Đi với động từ wohnen (sống ở đâu), ta dùng giới từ 'in'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 16: Điền từ còn thiếu vào lời chào buổi sáng: 'Guten ___!'",
            None, "Morgen", "'Guten Morgen!' = Chào buổi sáng!", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 17: Điền từ còn thiếu để tạo câu chúc ngủ ngon: 'Gute ___!'",
            None, "Nacht", "'Gute Nacht!' = Chúc ngủ ngon!", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 18: Điền từ nối giữa hàng đơn vị và hàng chục trong số 34: 'vier___dreißig'",
            None, "und", "Quy tắc ghép số 21-99: [Đơn vị] + und + [Chục] -> vierunddreißig.", 20, None
        ),

        # =========================================================================
        # DẠNG 3: DỊCH 2 CHIỀU & ĐỔI SỐ (dich) - ĐÚNG 8 CÂU (Câu 19 - 26)
        # =========================================================================
        (
            lesson_id, "dich",
            "Câu 19 [Việt → Đức]: Dịch sang tiếng Đức: 'Chào buổi sáng!'",
            None, "Guten Morgen! / Guten Morgen", "'Chào buổi sáng!' = 'Guten Morgen!'.", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 20 [Việt → Đức]: Dịch sang tiếng Đức: 'Hẹn gặp lại!' (Trang trọng)",
            None, "Auf Wiedersehen! / Auf Wiedersehen", "'Hẹn gặp lại!' (trang trọng) = 'Auf Wiedersehen!'.", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 21 [Việt → Đức]: Dịch sang tiếng Đức: 'Tôi đến từ Việt Nam.'",
            None, "Ich komme aus Vietnam. / Ich komme aus Viet Nam. / Ich komme aus Việt Nam.", "Mẫu câu chuẩn: 'Ich komme aus Vietnam.'", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 22 [Đức → Việt]: Dịch câu hỏi sau sang tiếng Việt: 'Wo wohnen Sie?'",
            None, "Ngài sống ở đâu? / Bạn sống ở đâu? / Anh sống ở đâu? / Chị sống ở đâu? / Bác sống ở đâu? / Ông sống ở đâu? / Bà sống ở đâu?", "'Wo wohnen Sie?' = 'Ngài sống ở đâu?' (chấp nhận cả các đại từ xưng hô tương đương như bạn, anh, chị).", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 23 [Đức → Số (Random)]: Chuyển chữ số tiếng Đức sau thành số tự nhiên: 'vierunddreißig'",
            None, "34", "vier (4) + und + dreißig (30) = 34.", 20,
            json.dumps({"dynamic_number": True, "dynamic_mode": "de_to_num", "min": 21, "max": 99})
        ),
        (
            lesson_id, "dich",
            "Câu 24 [Đức → Số (Random 2 chữ số)]: Chuyển chữ số tiếng Đức sau thành số tự nhiên: 'siebenundvierzig'",
            None, "47", "sieben (7) + und + vierzig (40) = 47.", 20,
            json.dumps({"dynamic_number": True, "dynamic_mode": "de_to_num", "min": 21, "max": 99})
        ),
        (
            lesson_id, "dich",
            "Câu 25 [Đức → Số (Random 3 chữ số)]: Chuyển chữ số tiếng Đức sau thành số tự nhiên: 'zweihundertachtunddreißig'",
            None, "238", "zweihundert (200) + acht (8) + und + dreißig (30) = 238.", 25,
            json.dumps({"dynamic_number": True, "dynamic_mode": "de_to_num", "min": 101, "max": 999})
        ),
        (
            lesson_id, "dich",
            "Câu 26 [Đức → Số (Random 4 chữ số)]: Chuyển chữ số tiếng Đức sau thành số tự nhiên: 'eintausendzweihundertvierunddreißig'",
            None, "1234", "eintausend (1000) + zweihundert (200) + vierunddreißig (34) = 1234.", 30,
            json.dumps({"dynamic_number": True, "dynamic_mode": "de_to_num", "min": 1001, "max": 9999})
        ),

        # =========================================================================
        # DẠNG 4: LUYỆN NGHE 1.0x & 0.65x (nghe) - ĐÚNG 7 CÂU (Câu 27 - 33)
        # =========================================================================
        (
            lesson_id, "nghe",
            "Câu 27 [Nghe từ vựng có Umlaut]: Bấm nút Nghe và gõ lại chính xác danh từ tiếng Đức bạn nghe được (Gợi ý: Trường đại học):",
            None, "Universität / Universitaet", "Từ phát âm là 'Universität'.", 20,
            json.dumps({"audio_text": "Universität"})
        ),
        (
            lesson_id, "nghe",
            "Câu 28 [Nghe từ vựng]: Bấm nút Nghe và gõ lại lời chào tạm biệt thân mật trong tiếng Đức:",
            None, "Tschüss / Tschuess", "Từ phát âm là 'Tschüss' [tʃʏs] (Tạm biệt).", 20,
            json.dumps({"audio_text": "Tschüss"})
        ),
        (
            lesson_id, "nghe",
            "Câu 29 [Nghe câu giao tiếp]: Nghe câu hỏi và gõ lại chính xác bằng tiếng Đức:",
            None, "Woher kommen Sie? / Woher kommen Sie", "Câu hỏi: 'Woher kommen Sie?' (Ngài đến từ đâu?).", 20,
            json.dumps({"audio_text": "Woher kommen Sie?"})
        ),
        (
            lesson_id, "nghe",
            "Câu 30 [Nghe câu giới thiệu]: Nghe câu tự giới thiệu và gõ lại chính xác bằng tiếng Đức:",
            None, "Mein Name ist Anna. / Mein Name ist Anna / Ich heiße Anna. / Ich bin Anna.", "Câu nói: 'Mein Name ist Anna.' (Tên tôi là Anna.)", 20,
            json.dumps({"audio_text": "Mein Name ist Anna."})
        ),
        (
            lesson_id, "nghe",
            "Câu 31 [Nghe Số 2 chữ số (Random)]: Bấm nút Nghe phát âm số đếm và nhập con số tự nhiên tương ứng (ví dụ: 47):",
            None, "47", "Âm thanh đọc là 'siebenundvierzig' -> Số 47.", 25,
            json.dumps({"audio_text": "siebenundvierzig", "dynamic_number": True, "dynamic_mode": "listen_num", "min": 21, "max": 99})
        ),
        (
            lesson_id, "nghe",
            "Câu 32 [Nghe Số 3 chữ số (Random)]: Bấm nút Nghe phát âm số đếm và nhập con số tự nhiên tương ứng:",
            None, "677", "Âm thanh đọc là 'sechshundertsiebenundsiebzig' -> Số 677.", 25,
            json.dumps({"audio_text": "sechshundertsiebenundsiebzig", "dynamic_number": True, "dynamic_mode": "listen_num", "min": 101, "max": 999})
        ),
        (
            lesson_id, "nghe",
            "Câu 33 [Nghe Số 4 chữ số (Random)]: Bấm nút Nghe phát âm số đếm và nhập con số tự nhiên tương ứng:",
            None, "1234", "Âm thanh đọc là 'eintausendzweihundertvierunddreißig' -> Số 1234.", 30,
            json.dumps({"audio_text": "eintausendzweihundertvierunddreißig", "dynamic_number": True, "dynamic_mode": "listen_num", "min": 1001, "max": 4999})
        ),

        # =========================================================================
        # DẠNG 5: LUYỆN NÓI & PHÁT ÂM (noi) - ĐÚNG 5 CÂU (Câu 34 - 38)
        # =========================================================================
        (
            lesson_id, "noi",
            "Câu 34 [Luyện Nói âm ie & ü]: Bấm '🔊 Nghe chuẩn', đọc to cụm từ sau rồi bấm '🎙️ Thu âm' hoặc gõ lại:",
            None, "Die Küche, das Bier und das Tier",
            "Chú ý âm 'ie' kéo dài trong die, Bier, Tier và âm tròn môi 'ü' trong Küche.", 25,
            json.dumps({"audio_text": "Die Küche, das Bier und das Tier"})
        ),
        (
            lesson_id, "noi",
            "Câu 35 [Luyện Nói âm sch, tsch, ß]: Nghe mẫu và luyện đọc to câu sau:",
            None, "Tschüss! Wir heißen Anna und Ben.",
            "Phát âm rõ [tʃʏs] (Tschüss) và [s] kéo dài (heißen).", 25,
            json.dumps({"audio_text": "Tschüss! Wir heißen Anna und Ben."})
        ),
        (
            lesson_id, "noi",
            "Câu 36 [Luyện Nói Tự giới thiệu]: Nghe mẫu và luyện đọc trôi chảy 4 câu tự giới thiệu bản thân:",
            None, "Guten Tag! Ich heiße Anna. Ich komme aus Vietnam. Ich wohne in Hai Phong.",
            "Chuỗi 4 câu giao tiếp nền tảng trong bài 1.", 30,
            json.dumps({"audio_text": "Guten Tag! Ich heiße Anna. Ich komme aus Vietnam. Ich wohne in Hai Phong."})
        ),
        (
            lesson_id, "noi",
            "Câu 37 [Luyện Nói Tạm biệt]: Nghe mẫu và đọc chuẩn 2 câu tạm biệt trang trọng & thân mật:",
            None, "Auf Wiedersehen! Tschüss! Bis morgen!",
            "Phát âm rõ âm [v] trong Wiedersehen và [tʃʏs] trong Tschüss.", 25,
            json.dumps({"audio_text": "Auf Wiedersehen! Tschüss! Bis morgen!"})
        ),
        (
            lesson_id, "noi",
            "Câu 38 [Luyện Nói số đếm (Random)]: Nghe mẫu và luyện phát âm số sau bằng tiếng Đức:",
            None, "einundzwanzig",
            "21 đọc là einundzwanzig.", 25,
            json.dumps({"audio_text": "einundzwanzig", "dynamic_number": True, "dynamic_mode": "speak_num", "min": 21, "max": 99})
        ),

        # =========================================================================
        # DẠNG 6: ĐỌC HIỂU HỘI THOẠI (doc) - ĐÚNG 4 CÂU (Câu 39 - 42)
        # =========================================================================
        (
            lesson_id, "doc",
            "Câu 39 [Đọc hiểu 1]: Đọc đoạn hội thoại sau và cho biết Anna đến từ quốc gia nào?",
            json.dumps(["Vietnam", "Deutschland", "Österreich", "Schweiz"]),
            "Vietnam",
            "Trong hội thoại: 'Ich komme aus Vietnam.'", 20,
            json.dumps({"passage": passage_text})
        ),
        (
            lesson_id, "doc",
            "Câu 40 [Đọc hiểu 2]: Dựa vào đoạn hội thoại trên, Anna hiện đang cư trú ở thành phố nào?",
            json.dumps(["Hai Phong", "Hanoi", "Berlin", "München"]),
            "Hai Phong",
            "Anna trả lời: 'Ich wohne in Hai Phong.'", 20,
            json.dumps({"passage": passage_text})
        ),
        (
            lesson_id, "doc",
            "Câu 41 [Đọc hiểu 3]: Số nhà (Hausnummer) của Anna trong đoạn hội thoại là số mấy?",
            json.dumps(["34", "43", "24", "47"]),
            "34",
            "'vierunddreißig' = 4 (vier) + 30 (dreißig) = 34.", 20,
            json.dumps({"passage": passage_text})
        ),
        (
            lesson_id, "doc",
            "Câu 42 [Đọc hiểu 4]: Lời chào cô giáo dùng khi bắt đầu buổi học trong hội thoại là gì?",
            json.dumps(["Guten Morgen!", "Gute Nacht!", "Tschüss!", "Auf Wiedersehen!"]),
            "Guten Morgen!",
            "Cô giáo mở đầu: 'Lehrerin: Guten Morgen! Wie heißen Sie?'", 20,
            json.dumps({"passage": passage_text})
        ),

        # =========================================================================
        # DẠNG 7: VIẾT SỐ & VIẾT CÂU TIẾNG ĐỨC (viet) - ĐÚNG 8 CÂU (Câu 43 - 50)
        # =========================================================================
        (
            lesson_id, "viet",
            "Câu 43 [Viết số 13–19 (Random)]: Hãy viết số 16 bằng chữ tiếng Đức:",
            None, "sechzehn", "Số 16 lược bỏ chữ 's' ở sechs -> sechzehn.", 25,
            json.dumps({"dynamic_number": True, "dynamic_mode": "num_to_de", "min": 11, "max": 19})
        ),
        (
            lesson_id, "viet",
            "Câu 44 [Viết số tròn chục (Random)]: Hãy viết số 30 bằng chữ tiếng Đức:",
            None, "dreißig", "Số 30 viết với chữ ß -> dreißig.", 25,
            json.dumps({"dynamic_number": True, "dynamic_mode": "tens_to_de"})
        ),
        (
            lesson_id, "viet",
            "Câu 45 [Viết số 2 chữ số (Random)]: Hãy viết số 69 bằng chữ tiếng Đức (viết liền không dấu cách):",
            None, "neunundsechzig", "9 (neun) + und + 60 (sechzig) = neunundsechzig.", 25,
            json.dumps({"dynamic_number": True, "dynamic_mode": "num_to_de", "min": 21, "max": 99})
        ),
        (
            lesson_id, "viet",
            "Câu 46 [Viết cặp 2 số (Random)]: Hãy viết số 83 và số 92 bằng chữ tiếng Đức (cách nhau bởi dấu phẩy):",
            None, "dreiundachtzig, zweiundneunzig", "83 = dreiundachtzig; 92 = zweiundneunzig.", 30,
            json.dumps({"dynamic_number": True, "dynamic_mode": "pair_num_to_de", "min": 21, "max": 99})
        ),
        (
            lesson_id, "viet",
            "Câu 47 [Viết số 3 chữ số (Random)]: Hãy viết số 677 bằng chữ tiếng Đức (viết liền không dấu cách):",
            None, "sechshundertsiebenundsiebzig", "600 (sechshundert) + 77 (siebenundsiebzig) = sechshundertsiebenundsiebzig.", 30,
            json.dumps({"dynamic_number": True, "dynamic_mode": "num_to_de", "min": 101, "max": 999})
        ),
        (
            lesson_id, "viet",
            "Câu 48 [Viết số 3 chữ số đặc biệt (Random)]: Hãy viết số 912 bằng chữ tiếng Đức (viết liền không dấu cách):",
            None, "neunhundertzwölf", "900 (neunhundert) + 12 (zwölf) = neunhundertzwölf.", 30,
            json.dumps({"dynamic_number": True, "dynamic_mode": "special_3digit_to_de"})
        ),
        (
            lesson_id, "viet",
            "Câu 49 [Viết số 4 chữ số (Random)]: Hãy viết số 1234 bằng chữ tiếng Đức (bắt đầu bằng eintausend...):",
            None, "eintausendzweihundertvierunddreißig", "1000 (eintausend) + 200 (zweihundert) + 34 (vierunddreißig).", 35,
            json.dumps({"dynamic_number": True, "dynamic_mode": "num_to_de", "min": 1001, "max": 9999})
        ),
        (
            lesson_id, "viet",
            "Câu 50 [Viết câu giao tiếp]: Hãy viết câu tiếng Đức có nghĩa là: 'Xin chào! Tôi tên là Anna. Tôi sống ở Hải Phòng.'",
            None, "Hallo! Ich heiße Anna. Ich wohne in Hai Phong. / Hallo, ich bin Anna. Ich wohne in Hai Phong. / Hallo, ich heiße Anna. Ich wohne in Hai Phong. / Hallo! Ich bin Anna. Ich wohne in Hai Phong. / Hallo! Mein Name ist Anna. Ich wohne in Hai Phong. / Guten Tag! Ich heiße Anna. Ich wohne in Hai Phong. / Guten Tag, ich bin Anna. Ich wohne in Hai Phong. / Hallo! Ich bin Anna und wohne in Hai Phong.", "Kết hợp lời chào Hallo/Guten Tag + giới thiệu tên (Ich heiße / Ich bin / Mein Name ist) + nơi ở (Ich wohne in Hai Phong). Chấp nhận nhiều cách diễn đạt tương đương.", 35, None
        )
    ]

    import random
    shuffled_exercises = []
    for ex in exercises:
        ex_list = list(ex)
        if ex_list[1] == "trac_nghiem" and ex_list[3]:
            try:
                opts = json.loads(ex_list[3])
                if isinstance(opts, list) and len(opts) > 1:
                    random.shuffle(opts)
                    ex_list[3] = json.dumps(opts, ensure_ascii=False)
            except Exception:
                pass
        shuffled_exercises.append(tuple(ex_list))
    exercises = shuffled_exercises

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises)

    conn.commit()
    conn.close()
    print("✅ Đã cập nhật Bài 1 (P1): Không YouTube + Bảng chữ cái tương tác IPA + ĐỦ 50 BÀI TẬP (10+8+8+7+5+4+8) có Random Số đếm!")

if __name__ == "__main__":
    seed_lesson_1_part_1()
