# -*- coding: utf-8 -*-
"""
Seed file Bài 12 (A1): "Körper und Gesundheit - dürfen - Pronomen im Akkusativ - Imperativ"
Vị trí A1: lesson_order = 13 (sau Bài 11)
Tích hợp đầy đủ 8 Học phần Lý thuyết + 6 Container Sơ đồ SVG + 50 Từ vựng + 125 Bài tập độc nhất (18 Dạng bài)
Chuẩn CEFR A1 và tuân thủ tuyệt đối Giao thức QA Zero-Bug & Quy tắc Imperativ-Pronoun Rules
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

def seed_lesson_12():
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
    lesson_id = 26
    lesson_title = 'Bài 12: Körper - Gesundheit - dürfen - Pronomen im Akkusativ - Imperativ'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed font-sans">
        <!-- BANNER TỔNG QUAN BÀI 12 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Körper & Gesundheit • dürfen • Imperativ (Bài 12)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 150 phút • ⚡ 2200+ EXP • 🎯 125 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Bài 12: Körper - Gesundheit - dürfen - Pronomen im Akkusativ - Imperativ
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Làm chủ từ vựng 30+ bộ phận cơ thể và các triệu chứng bệnh tật. Học cách dùng Modalverb <b>'dürfen'</b> (được phép/cấm). Phân biệt cực kỳ chi tiết Đại từ nhân xưng ở <b>Akkusativ</b> so với <b>Dativ</b>. Đặc biệt, nắm vững nghệ thuật ra lệnh và khuyên bảo qua câu mệnh lệnh (<b>Imperativ</b>) ở 3 ngôi: <code>du, ihr, Sie</code>.
                </p>
                <div class="pt-2 flex flex-wrap gap-2 text-xs">
                    <span class="px-3 py-1 rounded-xl bg-slate-800/80 border border-slate-700 text-slate-300 font-medium">🏥 50 Từ vựng Cơ thể & Bệnh tật</span>
                    <span class="px-3 py-1 rounded-xl bg-sky-950/80 border border-sky-500/30 text-sky-300 font-medium">🧍 Đại từ Akkusativ (mich, dich...)</span>
                    <span class="px-3 py-1 rounded-xl bg-rose-950/80 border border-rose-500/30 text-rose-300 font-medium">🛑 Modalverb: dürfen</span>
                    <span class="px-3 py-1 rounded-xl bg-amber-950/80 border border-amber-500/30 text-amber-300 font-medium">❗️ Câu mệnh lệnh (Imperativ)</span>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 1: TỪ VỰNG CƠ THỂ VÀ BỆNH LÝ (KÖRPER & KRANKHEIT) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-black text-sm flex items-center justify-center shrink-0">1</span>
                <h4 class="text-lg font-black text-slate-900">Từ Vựng Bộ Phận Cơ Thể & Triệu Chứng Bệnh</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-600">
                Học bộ phận cơ thể người theo 3 giống (<b>der / die / das</b>) và cách tạo từ ghép chỉ triệu chứng đau (<b>Komposita</b>) cùng cấu trúc <b>wehtun + Dativ</b>.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3 rounded-2xl bg-sky-50/70 border border-sky-200 space-y-1">
                    <div class="font-black text-sky-900 uppercase">Giống Đực (der)</div>
                    <ul class="space-y-0.5 text-slate-700">
                        <li>• <b>der Kopf</b> (die Köpfe): đầu</li>
                        <li>• <b>der Hals</b> (die Hälse): cổ, họng</li>
                        <li>• <b>der Rücken</b> (die Rücken): lưng</li>
                        <li>• <b>der Bauch</b> (die Bäuche): bụng</li>
                        <li>• <b>der Arm</b> (die Arme): cánh tay</li>
                        <li>• <b>der Finger</b> (die Finger): ngón tay</li>
                        <li>• <b>der Fuß</b> (die Füße): bàn chân</li>
                        <li>• <b>der Zahn</b> (die Zähne): răng</li>
                    </ul>
                </div>
                <div class="p-3 rounded-2xl bg-rose-50/70 border border-rose-200 space-y-1">
                    <div class="font-black text-rose-900 uppercase">Giống Cái (die)</div>
                    <ul class="space-y-0.5 text-slate-700">
                        <li>• <b>die Hand</b> (die Hände): bàn tay</li>
                        <li>• <b>die Nase</b> (die Nasen): mũi</li>
                        <li>• <b>die Schulter</b> (die Schultern): vai</li>
                        <li>• <b>die Brust</b> (die Brüste): ngực</li>
                        <li>• <b>die Zunge</b> (die Zungen): lưỡi</li>
                        <li>• <b>die Lippe</b> (die Lippen): môi</li>
                    </ul>
                </div>
                <div class="p-3 rounded-2xl bg-emerald-50/70 border border-emerald-200 space-y-1">
                    <div class="font-black text-emerald-900 uppercase">Giống Trung (das)</div>
                    <ul class="space-y-0.5 text-slate-700">
                        <li>• <b>das Auge</b> (die Augen): mắt</li>
                        <li>• <b>das Ohr</b> (die Ohren): tai</li>
                        <li>• <b>das Bein</b> (die Beine): chân (cả cẳng)</li>
                        <li>• <b>das Herz</b> (die Herzen): trái tim</li>
                        <li>• <b>das Knie</b> (die Knie): đầu gối</li>
                        <li>• <b>das Haar</b> (die Haare): tóc</li>
                        <li>• <b>das Gesicht</b> (die Gesichter): khuôn mặt</li>
                    </ul>
                </div>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-amber-950 space-y-1.5">
                <div class="font-bold text-amber-900">💡 Cấu trúc diễn đạt đau: wehtun + Dativ</div>
                <div>👉 <b>[Bộ phận cơ thể ở Nominativ] + tut / tun + [Đại từ Dativ] + weh.</b></div>
                <div class="italic">Ví dụ: „Mein Kopf <b>tut mir</b> weh.“ (Đầu tôi làm tôi đau ➔ Tôi bị đau đầu).</div>
                <div class="italic">Ví dụ: „Ihre Füße <b>tun ihr</b> weh.“ (Bàn chân cô ấy làm cô ấy đau ➔ Cô ấy bị đau chân).</div>
            </div>

            <!-- SƠ ĐỒ V1 CONTAINER -->
            <div id="b12-svg-v1-container" class="mt-4"></div>
        </div>

        <!-- HỌC PHẦN 2: ĐẠI TỪ NHÂN XƯNG CÁCH 4 (PERSONALPRONOMEN IM AKKUSATIV) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-sky-600 text-white font-black text-sm flex items-center justify-center shrink-0">2</span>
                <h4 class="text-lg font-black text-slate-900">Đại Từ Nhân Xưng ở Akkusativ & Phân Biệt với Dativ</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-600">
                Đại từ nhân xưng ở Cách 4 (Akkusativ) đóng vai trò tân ngữ trực tiếp chịu tác động của hành động. Xem bảng so sánh 3 cách để nắm chắc:
            </p>

            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-xs text-left border-collapse">
                    <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-2.5">Nominativ (Chủ ngữ)</th>
                            <th class="p-2.5 text-sky-700 bg-sky-50/50">Akkusativ (Tân ngữ Trực tiếp)</th>
                            <th class="p-2.5 text-amber-700 bg-amber-50/50">Dativ (Tân ngữ Gián tiếp)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 font-mono text-slate-700">
                        <tr><td class="p-2">ich (tôi)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">mich</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">mir</td></tr>
                        <tr><td class="p-2">du (bạn)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">dich</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">dir</td></tr>
                        <tr><td class="p-2">er (anh ấy)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">ihn (biến đổi!)</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">ihm</td></tr>
                        <tr><td class="p-2">sie (cô ấy)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">sie</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">ihr</td></tr>
                        <tr><td class="p-2">es (nó)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">es</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">ihm</td></tr>
                        <tr><td class="p-2">wir (chúng tôi)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">uns</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">uns</td></tr>
                        <tr><td class="p-2">ihr (các bạn)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">euch</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">euch</td></tr>
                        <tr><td class="p-2">sie / Sie (họ / Ngài)</td><td class="p-2 text-sky-700 font-bold bg-sky-50/30">sie / Sie</td><td class="p-2 text-amber-700 font-bold bg-amber-50/30">ihnen / Ihnen</td></tr>
                    </tbody>
                </table>
            </div>

            <div class="p-3 rounded-xl bg-sky-50 border border-sky-200 text-xs text-slate-700 space-y-1">
                <div>• <b>Động từ + Akkusativ:</b> <i>lieben</i> (yêu), <i>vermissen</i> (nhớ): <i>„Ich liebe dich.“</i> (Anh yêu em.), <i>„Ich vermisse dich jeden Tag.“</i> (Anh nhớ em mỗi ngày.)</div>
                <div>• <b>Động từ + Dativ + Akkusativ (như geben):</b> Đại từ nhân xưng Dativ (người nhận: <i>mir</i>) luôn đứng trước cụm danh từ Akkusativ (vật: <i>eine Salbe</i>). Ví dụ: <i>„Die Hausärztin gibt mir eine Salbe.“</i></div>
            </div>

            <!-- SƠ ĐỒ V2 CONTAINER -->
            <div id="b12-svg-v2-container" class="mt-4"></div>
        </div>

        <!-- HỌC PHẦN 3: ĐỘNG TỪ KHUYẾT THIẾU DÜRFEN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-rose-600 text-white font-black text-sm flex items-center justify-center shrink-0">3</span>
                <h4 class="text-lg font-black text-slate-900">Modalverb dürfen: Sự Cho Phép & Cấm Đoán</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-600">
                Động từ <b>dürfen</b> diễn đạt sự cho phép (Erlaubnis) hoặc cấm đoán (Verbot khi đi với <code>nicht / kein</code>). Chú ý hiện tượng biến âm <b>ü ➔ a</b> ở 3 ngôi số ít:
            </p>

            <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 text-xs font-mono">
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200"><span class="text-slate-500">ich:</span> <b class="text-rose-700">darf</b></div>
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200"><span class="text-slate-500">du:</span> <b class="text-rose-700">darfst</b></div>
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200"><span class="text-slate-500">er/sie/es/man:</span> <b class="text-rose-700">darf</b></div>
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200"><span class="text-slate-500">wir:</span> <b class="text-slate-800">dürfen</b></div>
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200"><span class="text-slate-500">ihr:</span> <b class="text-slate-800">dürft</b></div>
                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200"><span class="text-slate-500">sie/Sie:</span> <b class="text-slate-800">dürfen</b></div>
            </div>

            <!-- SƠ ĐỒ V5 CONTAINER -->
            <div id="b12-svg-v5-container" class="mt-4"></div>
        </div>

        <!-- HỌC PHẦN 4: CÂU MỆNH LỆNH (IMPERATIV) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-amber-600 text-white font-black text-sm flex items-center justify-center shrink-0">4</span>
                <h4 class="text-lg font-black text-slate-900">Câu Mệnh Lệnh (Imperativ) ở 3 Ngôi: du, ihr, Sie</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-600">
                Câu mệnh lệnh dùng để ra lệnh, yêu cầu hoặc đưa ra lời khuyên. Nắm chắc 3 ngôi và các quy tắc biến âm:
            </p>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 space-y-1.5">
                    <div class="font-bold text-amber-900 uppercase">1. Ngôi du (Thân mật 1 người)</div>
                    <div class="text-slate-700">• Bỏ chủ ngữ <code>du</code>, bỏ đuôi <code>-st</code>: <i>Komm!</i>, <i>Trink!</i></div>
                    <div class="text-slate-700">• Biến âm <code>e ➔ i/ie</code>: <b>GIỮ</b> (<i>Iss!</i>, <i>Lies!</i>, <i>Nimm!</i>)</div>
                    <div class="text-slate-700">• Đổi <code>a ➔ ä</code> (hoặc <code>au ➔ äu</code>): về nguyên âm gốc (<i>Fahr!</i>, <i>Schlaf!</i>, <i>Lauf!</i>)</div>
                    <div class="text-slate-700">• Gốc kết thúc bằng <code>-t/-d</code> hoặc phụ âm + <code>m/n</code>: thêm <b>-e</b> (<i>Arbeite!</i>, <i>Warte!</i>, <i>Atme!</i>, <i>Öffne!</i>, <i>Zeichne!</i>)</div>
                </div>

                <div class="p-3.5 rounded-2xl bg-indigo-50 border border-indigo-200 space-y-1.5">
                    <div class="font-bold text-indigo-900 uppercase">2. Ngôi ihr (Nhóm bạn bè)</div>
                    <div class="text-slate-700">• Chia như ngôi <code>ihr</code> ở Hiện tại, rồi <b>thông thường lược bỏ chủ ngữ ihr</b> (chỉ thêm khi muốn nhấn mạnh đối tượng).</div>
                    <div class="text-slate-700">• Ví dụ: ihr kommt ➔ <b>Kommt!</b></div>
                    <div class="text-slate-700">• Ví dụ: ihr esst ➔ <b>Esst!</b> (không biến âm 'i')</div>
                    <div class="text-slate-700">• Ví dụ: ihr wartet ➔ <b>Wartet!</b></div>
                    <div class="text-slate-700">• Động từ tách (như <i>aufräumen</i>, <i>ausruhen</i>): Tiền tố tách chuyển xuống cuối câu. Ví dụ: <b>Räumt eure Zimmer auf!</b></div>
                </div>

                <div class="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-200 space-y-1.5">
                    <div class="font-bold text-emerald-900 uppercase">3. Ngôi Sie (Trang trọng lịch sự)</div>
                    <div class="text-slate-700">• Đảo ngữ: <b>Động từ nguyên mẫu + Sie</b> (bắt buộc có chữ Sie!).</div>
                    <div class="text-slate-700">• Ví dụ: <b>Kommen Sie bitte!</b></div>
                    <div class="text-slate-700">• Ví dụ: <b>Nehmen Sie diese Tablette!</b></div>
                    <div class="text-slate-700">• Ngoại lệ sein: <b>Seien Sie ruhig!</b></div>
                </div>
            </div>

            <!-- MỤC MỞ RỘNG: ĐỘNG TỪ PHẢN THÂN TÁCH "SICH AUSRUHEN" -->
            <div class="p-5 rounded-2xl bg-cyan-50/90 border-2 border-cyan-300 text-xs text-cyan-950 space-y-3 shadow-xs">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-cyan-600 text-white font-extrabold text-xs shadow-xs">
                        💡 Mục 4.1 Mở rộng lời khuyên sức khỏe: Động từ phản thân tách (sich ausruhen)
                    </span>
                    <span class="text-[11px] font-bold text-cyan-800 bg-cyan-100/80 px-2 py-0.5 rounded-md border border-cyan-200">
                        Phổ biến trong giao tiếp phòng khám
                    </span>
                </div>
                <p class="text-slate-700 leading-relaxed text-xs sm:text-sm">
                    Trong bối cảnh y tế và sức khỏe, các bác sĩ rất thường dùng động từ <b>sich ausruhen</b> (nghỉ ngơi). Đây là động từ phản thân đi kèm tiền tố tách <b>aus-</b>:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-white border border-cyan-200 space-y-1.5 shadow-2xs">
                        <div class="font-bold text-cyan-900 text-xs uppercase tracking-wide">📌 Bảng đại từ phản thân (Reflexivpronomen):</div>
                        <div class="text-slate-700">• ich ➔ <b>mich</b> | du ➔ <b>dich</b></div>
                        <div class="text-slate-700">• er / sie / es / man ➔ <b>sich</b></div>
                        <div class="text-slate-700">• wir ➔ <b>uns</b> | ihr ➔ <b>euch</b> | sie / Sie ➔ <b>sich</b></div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-cyan-200 space-y-1.5 shadow-2xs">
                        <div class="font-bold text-cyan-900 text-xs uppercase tracking-wide">⚡ Câu mệnh lệnh (Imperativ) với sich ausruhen:</div>
                        <div class="text-slate-700">• <b>ngôi du:</b> <code>Ruh dich aus!</code> — <i>Hãy nghỉ ngơi đi!</i></div>
                        <div class="text-slate-700">• <b>ngôi ihr:</b> <code>Ruht euch aus!</code> — <i>Các bạn hãy nghỉ ngơi đi!</i></div>
                        <div class="text-slate-700">• <b>ngôi Sie:</b> <code>Ruhen Sie sich aus!</code> — <i>Xin ngài hãy nghỉ ngơi đi!</i></div>
                    </div>
                </div>
            </div>

            <!-- SƠ ĐỒ V3 & V4 CONTAINER -->
            <div id="b12-svg-v3-container" class="mt-4"></div>
            <div id="b12-svg-v4-container" class="mt-4"></div>
        </div>

        <!-- HỌC PHẦN 5: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN (TEXTANALYSE) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-cyan-600 text-white font-black text-sm flex items-center justify-center shrink-0">5</span>
                <h4 class="text-lg font-black text-slate-900">Đọc Hiểu & Giao Tiếp Phòng Khám (Beim Hausarzt)</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-600">
                Thực hành đọc hiểu các đoạn văn và đoạn hội thoại thực tế tại phòng mạch bác sĩ gia đình và hiệu thuốc Đức.
            </p>

            <!-- SƠ ĐỒ V6 CONTAINER -->
            <div id="b12-svg-v6-container" class="mt-4"></div>
        </div>
    </div>
"""

    cursor.execute("SELECT id FROM lessons WHERE id = ?;", (lesson_id,))
    existing_lesson = cursor.fetchone()

    if existing_lesson:
        cursor.execute("""
            UPDATE lessons 
            SET title = ?, grammar_content = ?, level_id = ?
            WHERE id = ?;
        """, (lesson_title, grammar_html, a1_id, lesson_id))
        print(f"Đã cập nhật Lý thuyết Bài 12 (ID: {lesson_id}).")
    else:
        cursor.execute("""
            INSERT INTO lessons (id, level_id, title, grammar_content)
            VALUES (?, ?, ?, ?);
        """, (lesson_id, a1_id, lesson_title, grammar_html))
        print(f"Đã tạo mới Bài 12 (ID: {lesson_id}).")

    # 1. SEED 50 TỪ VỰNG BÀI 12
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    vocab_list = [
        {
                "article": "der",
                "german_word": "der Kopf",
                "vietnamese_meaning": "cái đầu (PL: die Köpfe)",
                "example_sentence": "„Mein Kopf tut sehr weh.“ — Đầu tôi rất đau."
        },
        {
                "article": "der",
                "german_word": "der Hals",
                "vietnamese_meaning": "cổ, họng (PL: die Hälse)",
                "example_sentence": "„Ich habe Schmerzen im Hals.“ — Tôi bị đau ở họng."
        },
        {
                "article": "der",
                "german_word": "der Arm",
                "vietnamese_meaning": "cánh tay (PL: die Arme)",
                "example_sentence": "„Sein linker Arm ist gebrochen.“ — Cánh tay trái của anh ấy bị gãy."
        },
        {
                "article": "der",
                "german_word": "der Bauch",
                "vietnamese_meaning": "bụng (PL: die Bäuche)",
                "example_sentence": "„Nach dem Essen tut mein Bauch weh.“ — Sau khi ăn bụng tôi bị đau."
        },
        {
                "article": "der",
                "german_word": "der Rücken",
                "vietnamese_meaning": "lưng (PL: die Rücken)",
                "example_sentence": "„Er hat Probleme mit dem Rücken.“ — Anh ấy có vấn đề với cái lưng."
        },
        {
                "article": "der",
                "german_word": "der Fuß",
                "vietnamese_meaning": "bàn chân (PL: die Füße)",
                "example_sentence": "„Meine Füße sind sehr kalt.“ — Hai bàn chân tôi rất lạnh."
        },
        {
                "article": "der",
                "german_word": "der Finger",
                "vietnamese_meaning": "ngón tay (PL: die Finger)",
                "example_sentence": "„Zeig mir deine Finger!“ — Hãy cho tôi xem ngón tay của bạn!"
        },
        {
                "article": "der",
                "german_word": "der Zahn",
                "vietnamese_meaning": "răng (PL: die Zähne)",
                "example_sentence": "„Du musst deine Zähne putzen.“ — Bạn phải đánh răng."
        },
        {
                "article": "der",
                "german_word": "der Muskel",
                "vietnamese_meaning": "cơ bắp (PL: die Muskeln)",
                "example_sentence": "„Er trainiert seine Muskeln.“ — Anh ấy tập luyện cơ bắp."
        },
        {
                "article": "der",
                "german_word": "der Mund",
                "vietnamese_meaning": "miệng (PL: die Münder)",
                "example_sentence": "„Mach bitte den Mund auf!“ — Xin hãy há miệng ra!"
        },
        {
                "article": "der",
                "german_word": "der Zeh",
                "vietnamese_meaning": "ngón chân (PL: die Zehen)",
                "example_sentence": "„Ein Zeh tut mir weh.“ — Một ngón chân làm tôi đau."
        },
        {
                "article": "der",
                "german_word": "der Magen",
                "vietnamese_meaning": "dạ dày (PL: die Mägen)",
                "example_sentence": "„Der Magen ist leer.“ — Dạ dày đang trống rỗng."
        },
        {
                "article": "die",
                "german_word": "die Hand",
                "vietnamese_meaning": "bàn tay (PL: die Hände)",
                "example_sentence": "„Bitte waschen Sie Ihre Hände!“ — Xin ngài hãy rửa tay!"
        },
        {
                "article": "die",
                "german_word": "die Nase",
                "vietnamese_meaning": "mũi (PL: die Nasen)",
                "example_sentence": "„Meine Nase läuft.“ — Mũi tôi đang chảy nước."
        },
        {
                "article": "die",
                "german_word": "die Lunge",
                "vietnamese_meaning": "phổi (PL: die Lungen)",
                "example_sentence": "„Rauchen ist schlecht für die Lunge.“ — Hút thuốc thì tồi tệ cho phổi."
        },
        {
                "article": "die",
                "german_word": "die Schulter",
                "vietnamese_meaning": "vai (PL: die Schultern)",
                "example_sentence": "„Sie hat Schmerzen in der Schulter.“ — Cô ấy bị đau ở vai."
        },
        {
                "article": "die",
                "german_word": "die Brust",
                "vietnamese_meaning": "ngực (PL: die Brüste)",
                "example_sentence": "„Der Arzt hört meine Brust ab.“ — Bác sĩ nghe lồng ngực của tôi."
        },
        {
                "article": "die",
                "german_word": "die Zunge",
                "vietnamese_meaning": "lưỡi (PL: die Zungen)",
                "example_sentence": "„Zeigen Sie mir Ihre Zunge!“ — Hãy cho tôi xem lưỡi của ngài!"
        },
        {
                "article": "das",
                "german_word": "das Auge",
                "vietnamese_meaning": "mắt (PL: die Augen)",
                "example_sentence": "„Deine Augen sind sehr schön.“ — Đôi mắt của bạn rất đẹp."
        },
        {
                "article": "das",
                "german_word": "das Ohr",
                "vietnamese_meaning": "tai (PL: die Ohren)",
                "example_sentence": "„Ein Ohr tut ihm weh.“ — Một bên tai làm anh ấy đau."
        },
        {
                "article": "das",
                "german_word": "das Bein",
                "vietnamese_meaning": "chân (cả cẳng) (PL: die Beine)",
                "example_sentence": "„Sie hat lange Beine.“ — Cô ấy có đôi chân dài."
        },
        {
                "article": "das",
                "german_word": "das Herz",
                "vietnamese_meaning": "tim (PL: die Herzen)",
                "example_sentence": "„Mein Herz schlägt schnell.“ — Tim tôi đập nhanh."
        },
        {
                "article": "das",
                "german_word": "das Knie",
                "vietnamese_meaning": "đầu gối (PL: die Knie)",
                "example_sentence": "„Mein Knie tut beim Laufen weh.“ — Đầu gối tôi đau khi chạy."
        },
        {
                "article": "das",
                "german_word": "das Haar",
                "vietnamese_meaning": "tóc (PL: die Haare)",
                "example_sentence": "„Sie wäscht ihre Haare jeden Tag.“ — Cô ấy gội đầu mỗi ngày."
        },
        {
                "article": "das",
                "german_word": "das Gesicht",
                "vietnamese_meaning": "khuôn mặt (PL: die Gesichter)",
                "example_sentence": "„Wasch dir das Gesicht!“ — Hãy rửa mặt đi!"
        },
        {
                "article": "der",
                "german_word": "der Hausarzt",
                "vietnamese_meaning": "bác sĩ gia đình (nam) (PL: die Hausärzte)",
                "example_sentence": "„Ich muss zum Hausarzt gehen.“ — Tôi phải đi bác sĩ gia đình."
        },
        {
                "article": "der",
                "german_word": "der Schmerz",
                "vietnamese_meaning": "cơn đau (PL: die Schmerzen)",
                "example_sentence": "„Ich habe starke Schmerzen.“ — Tôi bị đau dữ dội."
        },
        {
                "article": "der",
                "german_word": "der Hustensaft",
                "vietnamese_meaning": "siro ho (PL: die Hustensäfte)",
                "example_sentence": "„Nehmen Sie diesen Hustensaft!“ — Ngài hãy uống siro ho này!"
        },
        {
                "article": "der",
                "german_word": "der Schnupfen",
                "vietnamese_meaning": "bệnh sổ mũi",
                "example_sentence": "„Bei Schnupfen brauche ich Taschentücher.“ — Khi sổ mũi tôi cần khăn giấy."
        },
        {
                "article": "der",
                "german_word": "der Husten",
                "vietnamese_meaning": "bệnh ho",
                "example_sentence": "„Dein Husten klingt schlimm.“ — Tiếng ho của bạn nghe tệ đấy."
        },
        {
                "article": "der",
                "german_word": "der Ratschlag",
                "vietnamese_meaning": "lời khuyên (PL: die Ratschläge)",
                "example_sentence": "„Der Arzt gibt mir einen guten Ratschlag.“ — Bác sĩ cho tôi một lời khuyên tốt."
        },
        {
                "article": "der",
                "german_word": "der Termin",
                "vietnamese_meaning": "cuộc hẹn (PL: die Termine)",
                "example_sentence": "„Haben Sie einen Termin?“ — Ngài có lịch hẹn không?"
        },
        {
                "article": "der",
                "german_word": "der Patient",
                "vietnamese_meaning": "bệnh nhân (nam) (PL: die Patienten)",
                "example_sentence": "„Der Patient muss im Bett bleiben.“ — Bệnh nhân phải nằm lại trên giường."
        },
        {
                "article": "die",
                "german_word": "die Hausärztin",
                "vietnamese_meaning": "bác sĩ gia đình (nữ) (PL: die Hausärztinnen)",
                "example_sentence": "„Ich habe einen Termin bei der Hausärztin.“ — Tôi có lịch hẹn với bác sĩ nữ."
        },
        {
                "article": "die",
                "german_word": "die Patientin",
                "vietnamese_meaning": "bệnh nhân (nữ) (PL: die Patientinnen)",
                "example_sentence": "„Die Patientin wartet schon lange.“ — Bệnh nhân nữ đã đợi lâu rồi."
        },
        {
                "article": "die",
                "german_word": "die Entspannung",
                "vietnamese_meaning": "sự thư giãn",
                "example_sentence": "„Yoga ist gut für die Entspannung.“ — Yoga tốt cho sự thư giãn."
        },
        {
                "article": "die",
                "german_word": "die Konzentration",
                "vietnamese_meaning": "sự tập trung",
                "example_sentence": "„Die Konzentration fällt mir schwer.“ — Sự tập trung thật khó với tôi."
        },
        {
                "article": "die",
                "german_word": "die Bewegung",
                "vietnamese_meaning": "sự vận động",
                "example_sentence": "„Bewegung ist wichtig für die Gesundheit.“ — Vận động rất quan trọng cho sức khỏe."
        },
        {
                "article": "die",
                "german_word": "die Versichertenkarte",
                "vietnamese_meaning": "thẻ BHYT (PL: die Versichertenkarten)",
                "example_sentence": "„Ich brauche Ihre Versichertenkarte.“ — Tôi cần thẻ BHYT của ngài."
        },
        {
                "article": "die",
                "german_word": "die Arztkosten",
                "vietnamese_meaning": "chi phí y tế",
                "example_sentence": "„Die Versicherung bezahlt die Arztkosten.“ — Bảo hiểm chi trả chi phí y tế."
        },
        {
                "article": "die",
                "german_word": "die Apotheke",
                "vietnamese_meaning": "hiệu thuốc (PL: die Apotheken)",
                "example_sentence": "„Die Apotheke ist gleich um die Ecke.“ — Hiệu thuốc ở ngay góc phố."
        },
        {
                "article": "die",
                "german_word": "die Entzündung",
                "vietnamese_meaning": "chứng viêm (PL: die Entzündungen)",
                "example_sentence": "„Er hat eine Entzündung im Hals.“ — Anh ấy bị viêm ở họng."
        },
        {
                "article": "die",
                "german_word": "die Zigarette",
                "vietnamese_meaning": "điếu thuốc lá (PL: die Zigaretten)",
                "example_sentence": "„Zigaretten sind ungesund.“ — Thuốc lá thì không tốt cho sức khỏe."
        },
        {
                "article": "die",
                "german_word": "die Salbe",
                "vietnamese_meaning": "thuốc mỡ (PL: die Salben)",
                "example_sentence": "„Diese Salbe hilft gegen Rückenschmerzen.“ — Thuốc mỡ này giúp trị đau lưng."
        },
        {
                "article": "die",
                "german_word": "die Erkältung",
                "vietnamese_meaning": "chứng cảm lạnh (PL: die Erkältungen)",
                "example_sentence": "„Mit einer Erkältung soll man im Bett bleiben.“ — Khi bị cảm lạnh nên nằm nghỉ."
        },
        {
                "article": "die",
                "german_word": "die Gesundheit",
                "vietnamese_meaning": "sức khỏe",
                "example_sentence": "„Gesundheit ist das Wichtigste im Leben.“ — Sức khỏe là điều quan trọng nhất."
        },
        {
                "article": "die",
                "german_word": "die Krankheit",
                "vietnamese_meaning": "bệnh tật (PL: die Krankheiten)",
                "example_sentence": "„Das ist eine schwere Krankheit.“ — Đó là một căn bệnh nặng."
        },
        {
                "article": "die",
                "german_word": "die Tablette",
                "vietnamese_meaning": "thuốc viên (PL: die Tabletten)",
                "example_sentence": "„Nehmen Sie täglich zwei Tabletten!“ — Mỗi ngày uống hai viên thuốc!"
        },
        {
                "article": "das",
                "german_word": "das Fieber",
                "vietnamese_meaning": "cơn sốt",
                "example_sentence": "„Das Kind hat hohes Fieber.“ — Đứa trẻ bị sốt cao."
        },
        {
                "article": "das",
                "german_word": "das Medikament",
                "vietnamese_meaning": "thuốc men (PL: die Medikamente)",
                "example_sentence": "„Nehmen Sie das Medikament nach dem Essen.“ — Hãy uống thuốc sau bữa ăn."
        },
        {
                "article": "das",
                "german_word": "das Rezept",
                "vietnamese_meaning": "đơn thuốc (PL: die Rezepte)",
                "example_sentence": "„Der Arzt schreibt mir ein Rezept.“ — Bác sĩ viết cho tôi một đơn thuốc."
        }
]

    for v in vocab_list:
        cursor.execute("""
            INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
            VALUES (?, ?, ?, ?, ?);
        """, (lesson_id, v["german_word"], v["article"], v["vietnamese_meaning"], v["example_sentence"]))
    print(f"Đã nạp thành công {len(vocab_list)} từ vựng cho Bài 12.")

    # 2. SEED 125 BÀI TẬP BÀI 12
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))
    exercises_data = [
        {
            "id": 1,
            "exercise_type": "trac_nghiem",
            "question": "Câu 1: Chọn đại từ đúng: \"Ich liebe ___.\"",
            "options": ["dir", "dich", "du", "mich"],
            "correct_answer": "dich",
            "explanation": "Động từ lieben tác động trực tiếp lên đối tượng nên đi kèm với Akkusativ (Cách 4).\nĐại từ Akkusativ của du là dich.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Tôi yêu bạn.",
                "audio_text": "dich"
            }
        },
        {
            "id": 2,
            "exercise_type": "trac_nghiem",
            "question": "Câu 2: Chọn đại từ đúng: \"Der Arzt untersucht ___ heute.\" (ông ấy)",
            "options": ["er", "ihm", "ihn", "es"],
            "correct_answer": "ihn",
            "explanation": "Động từ untersuchen (khám bệnh) + Akkusativ.\nAkkusativ của er là ihn.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Bác sĩ khám cho ông ấy hôm nay.",
                "audio_text": "ihn"
            }
        },
        {
            "id": 3,
            "exercise_type": "trac_nghiem",
            "question": "Câu 3: Chọn hình thức đúng của Modalverb: \"Die Kinder ___ nicht so viel Schokolade essen.\"",
            "options": ["dürft", "darfst", "darf", "dürfen"],
            "correct_answer": "dürfen",
            "explanation": "Die Kinder là chủ ngữ số nhiều (sie - họ).\nĐộng từ dürfen chia ở số nhiều là dürfen.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Bọn trẻ không được phép ăn quá nhiều sô cô la.",
                "audio_text": "dürfen"
            }
        },
        {
            "id": 4,
            "exercise_type": "trac_nghiem",
            "question": "Câu 4: Chọn câu Mệnh lệnh (Imperativ) đúng cho ngôi du:",
            "options": [
                "Trinkt viel Wasser!",
                "Trinken Sie viel Wasser!",
                "Trink viel Wasser!",
                "Trinkst du viel Wasser!"
            ],
            "correct_answer": "Trink viel Wasser!",
            "explanation": "Đối với ngôi du, ta bỏ đuôi -st và thông thường lược bỏ chủ ngữ du (chỉ thêm khi muốn nhấn mạnh đối tượng): du trinkst.\n-> Trink!\n-> Đáp án đúng: \"Trink viel Wasser!\"",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Hãy uống nhiều nước!",
                "audio_text": "du"
            }
        },
        {
            "id": 5,
            "exercise_type": "trac_nghiem",
            "question": "Câu 5: Tìm từ khác loại (về Giống - Artikel):",
            "options": ["Rücken", "Nase", "Bauch", "Finger"],
            "correct_answer": "Nase",
            "explanation": "der Rücken, der Bauch, der Finger đều là giống Đực (der).\nChỉ có die Nase là giống Cái (die).",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Rücken (lưng), Nase (mũi), Bauch (bụng), Finger (ngón tay).",
                "audio_text": "Nase"
            }
        },
        {
            "id": 6,
            "exercise_type": "trac_nghiem",
            "question": "Câu 6: \"Guten Tag, Herr Müller. Was fehlt ___?\"",
            "options": ["Ihnen", "Sie", "dich", "dir"],
            "correct_answer": "Ihnen",
            "explanation": "Động từ fehlen trong y tế đi với Dativ.\nHerr Müller đòi hỏi sự trang trọng (Sie), Dativ của Sie là Ihnen.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Chào ngài Müller.\nNgài bị làm sao vậy?",
                "audio_text": "Ihnen"
            }
        },
        {
            "id": 7,
            "exercise_type": "trac_nghiem",
            "question": "Câu 7: Chọn đại từ đúng: \"Wir haben ein Problem. Kannst du ___ helfen?\"",
            "options": ["uns", "wir", "euch", "mich"],
            "correct_answer": "uns",
            "explanation": "Động từ helfen đi với Dativ.\nDativ của wir (chúng tôi) là uns.\n(Bẫy: uns ở Akk và Dat giống nhau, nhưng bản chất ở đây là Dat).",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Chúng tôi có một vấn đề.\nBạn có thể giúp chúng tôi không?",
                "audio_text": "uns"
            }
        },
        {
            "id": 8,
            "exercise_type": "trac_nghiem",
            "question": "Câu 8: \"Das ist Maria. Kennst du ___?\"",
            "options": ["ihr", "sie", "ihn", "es"],
            "correct_answer": "sie",
            "explanation": "Động từ kennen + Akkusativ.\nAkkusativ của sie (cô ấy) vẫn là sie.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Kia là Maria.\nBạn có biết cô ấy không?",
                "audio_text": "sie"
            }
        },
        {
            "id": 9,
            "exercise_type": "trac_nghiem",
            "question": "Câu 9: Chọn câu Mệnh lệnh đúng cho ngôi ihr: (Động từ essen)",
            "options": ["Isst mehr Gemüse!", "Esst mehr Gemüse!", "Essen Sie mehr Gemüse!", "Iss mehr Gemüse!"],
            "correct_answer": "Esst mehr Gemüse!",
            "explanation": "Mệnh lệnh ngôi ihr: chia động từ như bình thường (ihr esst) rồi thông thường lược bỏ chủ ngữ ihr (chỉ thêm khi muốn nhấn mạnh đối tượng).\n-> Esst!\nKhông có biến âm 'i' như ngôi du.\n-> Đáp án đúng: \"Esst mehr Gemüse!\"",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Các bạn hãy ăn nhiều rau hơn!",
                "audio_text": "ihr"
            }
        },
        {
            "id": 10,
            "exercise_type": "trac_nghiem",
            "question": "Câu 10: Biển báo ghi: \"Hier darf man nicht parken.\" Nghĩa là gì?",
            "options": [
                "Người ta được phép đỗ xe ở đây.",
                "Cấm đỗ xe ở đây.",
                "Bãi đỗ xe miễn phí.",
                "Bạn phải đỗ xe ở đây."
            ],
            "correct_answer": "Cấm đỗ xe ở đây.",
            "explanation": "nicht dürfen mang ý nghĩa cấm đoán (Verbot). parken = đỗ xe.\n-> Đáp án đúng: \"Cấm đỗ xe ở đây.\"",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Ở đây người ta không được đỗ xe.",
                "audio_text": "Cấm đỗ xe ở đây"
            }
        },
        {
            "id": 11,
            "exercise_type": "trac_nghiem",
            "question": "Câu 11: Điền vào chỗ trống: \"Mein rechter ___ tut weh. Ich kann nicht gut laufen.\"",
            "options": ["Fuß", "Kopf", "Hand", "Bauch"],
            "correct_answer": "Fuß",
            "explanation": "laufen (đi/chạy) liên quan đến chân (der Fuß). rechter cho thấy danh từ giống đực (der).",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Bàn chân phải của tôi bị đau.\nTôi không thể đi lại tốt được.",
                "audio_text": "Fuß"
            }
        },
        {
            "id": 12,
            "exercise_type": "trac_nghiem",
            "question": "Câu 12: Chọn đại từ đúng: \"Ruf ___ bitte heute Abend an!\" (tôi)",
            "options": ["mir", "mich", "ich", "mein"],
            "correct_answer": "mich",
            "explanation": "Động từ anrufen (gọi điện) + Akkusativ.\nAkkusativ của ich là mich.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Hãy gọi cho tôi vào tối nay nhé!",
                "audio_text": "mich"
            }
        },
        {
            "id": 13,
            "exercise_type": "trac_nghiem",
            "question": "Câu 13: Chọn hình thức Mệnh lệnh đúng của động từ arbeiten cho ngôi du:",
            "options": ["Arbeit!", "Arbeitest!", "Arbeite!", "Arbeitet!"],
            "correct_answer": "Arbeite!",
            "explanation": "Gốc động từ kết thúc bằng -t (arbeit-en ➔ arbeit-), khi chuyển sang Imperativ ngôi du phải thêm đuôi -e để dễ phát âm.\n-> Arbeite!",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Hãy làm việc đi!",
                "audio_text": "arbeiten"
            }
        },
        {
            "id": 14,
            "exercise_type": "trac_nghiem",
            "question": "Câu 14: \"Wie oft muss ich die Tabletten nehmen?\" – \"Nehmen ___ die Tabletten zweimal täglich.\"",
            "options": ["Sie", "ihr", "du", "man"],
            "correct_answer": "Sie",
            "explanation": "Động từ nguyên mẫu Nehmen đứng đầu câu + đại từ nhân xưng.\n-> Câu mệnh lệnh ngôi lịch sự Sie.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Ngài hãy uống thuốc hai lần mỗi ngày.",
                "audio_text": "Sie"
            }
        },
        {
            "id": 15,
            "exercise_type": "trac_nghiem",
            "question": "Câu 15: Chọn hình thức đúng của Modalverb: \"___ ich einen Kaffee trinken?\"",
            "options": ["Darfst", "Dürfen", "Darf", "Dürft"],
            "correct_answer": "Darf",
            "explanation": "Chủ ngữ là ich ➔ động từ dürfen chia là darf.",
            "exp_reward": 15,
            "extra_data": {
                "translation": "Tôi có được phép uống một ly cà phê không?",
                "audio_text": "Darf"
            }
        },
        {
            "id": 16,
            "exercise_type": "dien_khuyet",
            "question": "Câu 16: Điền Modalverb dürfen: \"Mama, ___ ich jetzt fernsehen?\"",
            "options": null,
            "correct_answer": "darf",
            "explanation": "Chủ ngữ ich ➔ darf.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["darf"],
                "translation": "Mẹ ơi, con có được phép xem TV bây giờ không?",
                "audio_text": "darf"
            }
        },
        {
            "id": 17,
            "exercise_type": "dien_khuyet",
            "question": "Câu 17: Điền Modalverb dürfen: \"Ihr ___ nicht so laut sprechen! Das Baby schläft.\"",
            "options": null,
            "correct_answer": "dürft",
            "explanation": "Chủ ngữ ihr ➔ dürft.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["dürft", "duerft"],
                "translation": "Các con không được nói chuyện lớn tiếng như vậy!\nEm bé đang ngủ.",
                "audio_text": "dürft"
            }
        },
        {
            "id": 18,
            "exercise_type": "dien_khuyet",
            "question": "Câu 18: Điền Modalverb dürfen: \"Entschuldigung, ___ man hier fotografieren?\"",
            "options": null,
            "correct_answer": "darf",
            "explanation": "Chủ ngữ man (người ta - ngôi thứ 3 số ít).\n-> darf.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["darf"],
                "translation": "Xin lỗi, người ta có được phép chụp ảnh ở đây không?",
                "audio_text": "darf"
            }
        },
        {
            "id": 19,
            "exercise_type": "dien_khuyet",
            "question": "Câu 19: Điền Modalverb dürfen: \"Lukas ___ heute Abend nicht ins Kino gehen.\"",
            "options": null,
            "correct_answer": "darf",
            "explanation": "Chủ ngữ Lukas (er) ➔ darf.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["darf"],
                "translation": "Lukas không được phép đi xem phim tối nay.",
                "audio_text": "darf"
            }
        },
        {
            "id": 20,
            "exercise_type": "dien_khuyet",
            "question": "Câu 20: Điền động từ chia ở Imperativ (ngôi du): \"___ bitte einen Moment!\" (warten)",
            "options": null,
            "correct_answer": "Warte",
            "explanation": "Gốc động từ warten (bỏ -en) là wart-, kết thúc bằng -t nên Imperativ ngôi du phải thêm đuôi -e: Warte!\n(Quy tắc chung: gốc kết thúc bằng -t, -d hoặc phụ âm + m/n thì thêm đuôi -e).",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Warte"],
                "translation": "Xin hãy đợi một lát!",
                "audio_text": "Warte"
            }
        },
        {
            "id": 21,
            "exercise_type": "dien_khuyet",
            "question": "Câu 21: Điền động từ chia ở Imperativ (ngôi ihr): \"Kinder, ___ eure Hausaufgaben!\" (machen)",
            "options": null,
            "correct_answer": "Macht",
            "explanation": "Ngôi ihr chia bình thường macht rồi thông thường lược bỏ chữ ihr (chỉ thêm khi muốn nhấn mạnh đối tượng).\n-> Macht!",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Macht"],
                "translation": "Các con, hãy làm bài tập về nhà của các con đi!",
                "audio_text": "Macht"
            }
        },
        {
            "id": 22,
            "exercise_type": "dien_khuyet",
            "question": "Câu 22: Điền động từ chia ở Imperativ (ngôi du): \"___ nicht so viel Cola!\" (trinken)",
            "options": null,
            "correct_answer": "Trink",
            "explanation": "Ngôi du của trinken là trinkst, bỏ st.\n-> Trink!",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Trink", "Trinke"],
                "translation": "Đừng uống nhiều nước ngọt Cola quá!",
                "audio_text": "Trink"
            }
        },
        {
            "id": 23,
            "exercise_type": "dien_khuyet",
            "question": "Câu 23: Điền động từ chia ở Imperativ (ngôi Sie): \"___ Sie bitte Platz im Wartezimmer!\" (nehmen)",
            "options": null,
            "correct_answer": "Nehmen",
            "explanation": "Cấu trúc mệnh lệnh lịch sự: Nguyên thể Nehmen + Sie.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Nehmen"],
                "translation": "Xin ngài hãy ngồi chờ ở phòng đợi!",
                "audio_text": "Nehmen"
            }
        },
        {
            "id": 24,
            "exercise_type": "dien_khuyet",
            "question": "Câu 24: Điền đại từ Akkusativ: \"Das ist mein neuer Pullover. Findest du ___ schön?\" (er)",
            "options": null,
            "correct_answer": "ihn",
            "explanation": "der Pullover được thay thế bằng đại từ er.\nĐứng làm tân ngữ cho finden.\n-> Akkusativ là ihn.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["ihn"],
                "translation": "Đó là chiếc áo len mới của tôi.\nBạn thấy nó đẹp không?",
                "audio_text": "ihn"
            }
        },
        {
            "id": 25,
            "exercise_type": "dien_khuyet",
            "question": "Câu 25: Điền đại từ Dativ: \"Wir suchen den Bahnhof. Können Sie ___ bitte helfen?\" (wir)",
            "options": null,
            "correct_answer": "uns",
            "explanation": "LƯU Ý!\nĐộng từ helfen đi với Dativ.\nDativ của wir là uns.\n(Câu này rèn luyện sự tỉnh táo).",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["uns"],
                "translation": "Chúng tôi đang tìm nhà ga.\nNgài có thể giúp chúng tôi được không?",
                "audio_text": "uns"
            }
        },
        {
            "id": 26,
            "exercise_type": "dien_khuyet",
            "question": "Câu 26: Điền đại từ Akkusativ: \"Ich habe dich gestern angerufen, aber du hast ___ nicht gehört.\" (ich)",
            "options": null,
            "correct_answer": "mich",
            "explanation": "Động từ hören + Akkusativ.\nAkkusativ của ich là mich.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["mich"],
                "translation": "Hôm qua tôi đã gọi điện cho bạn, nhưng bạn không nghe thấy tôi.",
                "audio_text": "mich"
            }
        },
        {
            "id": 27,
            "exercise_type": "dien_khuyet",
            "question": "Câu 27: Điền bộ phận cơ thể: \"Ich kann nicht essen. Ich habe Zahn___.\"",
            "options": null,
            "correct_answer": "schmerzen",
            "explanation": "Ghép từ Zahn + schmerzen = Zahnschmerzen.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["schmerzen"],
                "translation": "Tôi không thể ăn.\nTôi bị đau răng.",
                "audio_text": "schmerzen"
            }
        },
        {
            "id": 28,
            "exercise_type": "dien_khuyet",
            "question": "Câu 28: Điền bộ phận cơ thể: \"Er hat den ganzen Tag am Computer gearbeitet. Jetzt tun ihm die ___ weh.\" (đôi mắt)",
            "options": null,
            "correct_answer": "Augen",
            "explanation": "Đôi mắt (số nhiều) = die Augen.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Augen"],
                "translation": "Anh ấy đã làm việc cả ngày trên máy tính.\nBây giờ đôi mắt của anh ấy bị đau.",
                "audio_text": "Augen"
            }
        },
        {
            "id": 29,
            "exercise_type": "dien_khuyet",
            "question": "Câu 29: Điền dạng đúng của động từ: \"Der Arzt ___ mir Hustensaft.\" (verschreiben)",
            "options": null,
            "correct_answer": "verschreibt",
            "explanation": "Chủ ngữ Der Arzt (er) ➔ verschreibt.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["verschreibt"],
                "translation": "Bác sĩ kê cho tôi siro ho.",
                "audio_text": "verschreibt"
            }
        },
        {
            "id": 30,
            "exercise_type": "dien_khuyet",
            "question": "Câu 30: Điền dạng đúng của động từ: \"Bitte ___ Sie tief ein und aus!\" (atmen)",
            "options": null,
            "correct_answer": "atmen",
            "explanation": "Câu mệnh lệnh ngôi Sie ➔ động từ nguyên thể atmen.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["atmen"],
                "translation": "Xin ngài hãy hít vào và thở ra thật sâu!",
                "audio_text": "atmen"
            }
        },
        {
            "id": 31,
            "exercise_type": "chia_imperativ",
            "question": "Câu 31: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Du isst mehr Obst.\"",
            "options": null,
            "correct_answer": "Iss mehr Obst!",
            "explanation": "Du isst ➔ bỏ du và đuôi -t ➔ Iss!\n(động từ đổi e ➔ i nên giữ i).\n-> Đáp án: \"Iss mehr Obst!\"",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Du isst mehr Obst.",
                "accepted_answers": ["Iss mehr Obst!", "Iss mehr Obst"],
                "translation": "Hãy ăn nhiều trái cây hơn!",
                "audio_text": "Iss mehr Obst"
            }
        },
        {
            "id": 32,
            "exercise_type": "chia_imperativ",
            "question": "Câu 32: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Ihr lest den Text.\"",
            "options": null,
            "correct_answer": "Lest den Text!",
            "explanation": "Ngôi ihr chia là lest, thông thường lược bỏ chữ ihr đi.\n-> Lest den Text!\n(chỉ thêm khi muốn nhấn mạnh đối tượng).",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ihr lest den Text.",
                "accepted_answers": ["Lest den Text!", "Lest den Text"],
                "translation": "Các bạn hãy đọc đoạn văn!",
                "audio_text": "Lest den Text"
            }
        },
        {
            "id": 33,
            "exercise_type": "chia_imperativ",
            "question": "Câu 33: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Sie (trang trọng) kommen bitte pünktlich.\"",
            "options": null,
            "correct_answer": "Kommen Sie bitte pünktlich!",
            "explanation": "Đảo động từ nguyên thể lên trước Sie.\n-> Kommen Sie.\n-> Đáp án: \"Kommen Sie bitte pünktlich!\"",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Sie (trang trọng) kommen bitte pünktlich.",
                "accepted_answers": [
                    "Kommen Sie bitte pünktlich!",
                    "Kommen Sie bitte pünktlich",
                    "Bitte kommen Sie pünktlich!",
                    "Bitte kommen Sie pünktlich"
                ],
                "translation": "Xin ngài hãy đến đúng giờ!",
                "audio_text": "Kommen Sie bitte pünktlich"
            }
        },
        {
            "id": 34,
            "exercise_type": "chia_imperativ",
            "question": "Câu 34: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Du bist leise.\"",
            "options": null,
            "correct_answer": "Sei leise!",
            "explanation": "sein là động từ bất quy tắc đặc biệt.\nỞ ngôi du, mệnh lệnh của nó là Sei.\n-> Đáp án: \"Sei leise!\"",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Du bist leise.",
                "accepted_answers": ["Sei leise!", "Sei leise"],
                "translation": "Hãy trật tự!",
                "audio_text": "Sei leise"
            }
        },
        {
            "id": 35,
            "exercise_type": "chia_imperativ",
            "question": "Câu 35: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Ihr geht jetzt schlafen.\"",
            "options": null,
            "correct_answer": "Geht jetzt schlafen!",
            "explanation": "Ngôi ihr chia là geht, thông thường lược bỏ ihr.\n-> Geht jetzt schlafen!\n(chỉ thêm ihr khi muốn nhấn mạnh).",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ihr geht jetzt schlafen.",
                "accepted_answers": ["Geht jetzt schlafen!", "Geht jetzt schlafen"],
                "translation": "Các con hãy đi ngủ ngay bây giờ!",
                "audio_text": "Geht jetzt schlafen"
            }
        },
        {
            "id": 36,
            "exercise_type": "chia_imperativ",
            "question": "Câu 36: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Du machst die Tür zu.\"",
            "options": null,
            "correct_answer": "Mach die Tür zu!",
            "explanation": "Động từ tách zumachen.\nNgôi du là du machst... zu.\n-> Bỏ st và du.\n-> Mach die Tür zu!",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Du machst die Tür zu.",
                "accepted_answers": ["Mach die Tür zu!", "Mach die Tuer zu!", "Mach die Tür zu"],
                "translation": "Hãy đóng cửa lại!",
                "audio_text": "Mach die Tür zu"
            }
        },
        {
            "id": 37,
            "exercise_type": "chia_imperativ",
            "question": "Câu 37: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Sie (trang trọng) rufen mich morgen an.\"",
            "options": null,
            "correct_answer": "Rufen Sie mich morgen an!",
            "explanation": "Đảo Rufen lên đầu, tiền tố tách an vẫn ở cuối câu.\n-> Rufen Sie... an!\n-> Đáp án: \"Rufen Sie mich morgen an!\"",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Sie (trang trọng) rufen mich morgen an.",
                "accepted_answers": ["Rufen Sie mich morgen an!", "Rufen Sie mich morgen an"],
                "translation": "Xin ngài hãy gọi cho tôi vào ngày mai!",
                "audio_text": "Rufen Sie mich morgen an"
            }
        },
        {
            "id": 38,
            "exercise_type": "chia_imperativ",
            "question": "Câu 38: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Du fährst langsamer.\"",
            "options": null,
            "correct_answer": "Fahr langsamer!",
            "explanation": "Động từ đổi a ➔ ä (hoặc au ➔ äu) ở ngôi du thì Imperativ ngôi du trở về nguyên âm gốc: fährst.\n-> Fahr!, schläfst.\n-> Schlaf!, läufst.\n-> Lauf!\n-> Đáp án: \"Fahr langsamer!\"",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Du fährst langsamer.",
                "accepted_answers": ["Fahr langsamer!", "Fahr langsamer"],
                "translation": "Hãy lái xe chậm lại!",
                "audio_text": "Fahr langsamer"
            }
        },
        {
            "id": 39,
            "exercise_type": "chia_imperativ",
            "question": "Câu 39: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Du zeichnest ein Bild.\"",
            "options": null,
            "correct_answer": "Zeichne ein Bild!",
            "explanation": "Gốc động từ (bỏ -en) là zeichn-, kết thúc bằng phụ âm + n nên phải thêm -e để đọc được.\n-> Zeichne!\n(Quy tắc chung: gốc kết thúc bằng -t, -d hoặc phụ âm + m/n thì thêm -e).\n-> Đáp án: \"Zeichne ein Bild!\"",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Du zeichnest ein Bild.",
                "accepted_answers": ["Zeichne ein Bild!", "Zeichne ein Bild"],
                "translation": "Hãy vẽ một bức tranh!",
                "audio_text": "Zeichne ein Bild"
            }
        },
        {
            "id": 40,
            "exercise_type": "chia_imperativ",
            "question": "Câu 40: Chuyển câu trần thuật sau sang câu Mệnh lệnh (Imperativ): \"Ihr nehmt die Tabletten.\"",
            "options": null,
            "correct_answer": "Nehmt die Tabletten!",
            "explanation": "Ngôi ihr của nehmen là nehmt.\nBỏ ihr.\n-> Nehmt die Tabletten!",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ihr nehmt die Tabletten.",
                "accepted_answers": ["Nehmt die Tabletten!", "Nehmt die Tabletten"],
                "translation": "Các bạn hãy uống thuốc viên đi!",
                "audio_text": "Nehmt die Tabletten"
            }
        },
        {
            "id": 41,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 41: \"Ich liebe meine Eltern. Ich besuche ___ jedes Wochenende.\"",
            "options": null,
            "correct_answer": "sie",
            "explanation": "meine Eltern (số nhiều) ➔ đại từ sie (họ). besuchen + Akkusativ.\n-> vẫn là sie.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["sie"],
                "translation": "Tôi yêu bố mẹ tôi.\nTôi đến thăm họ mỗi cuối tuần.",
                "audio_text": "sie"
            }
        },
        {
            "id": 42,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 42: \"Das ist mein neuer Computer. Ich brauche ___ für die Arbeit.\"",
            "options": null,
            "correct_answer": "ihn",
            "explanation": "der Computer (giống đực) ➔ đại từ er. brauchen + Akkusativ.\n-> Akkusativ của er là ihn.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["ihn"],
                "translation": "Đó là chiếc máy tính mới của tôi.\nTôi cần nó cho công việc.",
                "audio_text": "ihn"
            }
        },
        {
            "id": 43,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 43: \"Wo ist Anna? Ich kann ___ nicht finden.\"",
            "options": null,
            "correct_answer": "sie",
            "explanation": "Anna (giống cái) ➔ đại từ sie (cô ấy). finden + Akkusativ.\n-> sie.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["sie"],
                "translation": "Anna đâu rồi?\nTôi không thể tìm thấy cô ấy.",
                "audio_text": "sie"
            }
        },
        {
            "id": 44,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 44: \"Wir haben ein neues Auto. Ich kaufe ___ morgen.\"",
            "options": null,
            "correct_answer": "es",
            "explanation": "das Auto (giống trung) ➔ đại từ es. kaufen + Akkusativ.\n-> es.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["es"],
                "translation": "Chúng tôi có một chiếc ô tô mới.\nTôi mua nó vào ngày mai.",
                "audio_text": "es"
            }
        },
        {
            "id": 45,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 45: \"Ihr seid meine besten Freunde. Ich vergesse ___ nie.\"",
            "options": null,
            "correct_answer": "euch",
            "explanation": "ihr (các bạn). vergessen + Akkusativ.\n-> Akkusativ của ihr là euch.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["euch"],
                "translation": "Các bạn là những người bạn tốt nhất của tôi.\nTôi sẽ không bao giờ quên các bạn.",
                "audio_text": "euch"
            }
        },
        {
            "id": 46,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 46: \"Herr Schmidt, der Chef möchte ___ sprechen.\"",
            "options": null,
            "correct_answer": "Sie",
            "explanation": "Herr Schmidt ➔ xưng hô trang trọng (Sie). sprechen + Akkusativ.\n-> Sie (viết hoa).",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Sie"],
                "translation": "Ngài Schmidt, sếp muốn nói chuyện với ngài.",
                "audio_text": "Sie"
            }
        },
        {
            "id": 47,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 47: \"Der Salat ist lecker. Ich esse ___ gern.\"",
            "options": null,
            "correct_answer": "ihn",
            "explanation": "der Salat (giống đực) ➔ er. essen + Akkusativ.\n-> ihn.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["ihn"],
                "translation": "Món salad ngon.\nTôi thích ăn nó.",
                "audio_text": "ihn"
            }
        },
        {
            "id": 48,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 48: \"Das Buch ist interessant. Ich lese ___ jeden Abend.\"",
            "options": null,
            "correct_answer": "es",
            "explanation": "das Buch (giống trung) ➔ es. lesen + Akkusativ.\n-> es.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["es"],
                "translation": "Cuốn sách thật thú vị.\nTôi đọc nó mỗi tối.",
                "audio_text": "es"
            }
        },
        {
            "id": 49,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 49: \"Mein Bruder und ich spielen oft Fußball. Manchmal besucht unser Vater ___ beim Training.\"",
            "options": null,
            "correct_answer": "uns",
            "explanation": "Mein Bruder und ich = wir (chúng tôi). besuchen + Akkusativ.\n-> Akkusativ của wir là uns.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["uns"],
                "translation": "Anh trai tôi và tôi thường chơi bóng đá.\nĐôi khi bố chúng tôi đến thăm chúng tôi lúc tập luyện.",
                "audio_text": "uns"
            }
        },
        {
            "id": 50,
            "exercise_type": "dien_dai_tu_akk",
            "question": "Câu 50: \"Hast du den Schlüssel? – Nein, ich habe ___ nicht gesehen.\"",
            "options": null,
            "correct_answer": "ihn",
            "explanation": "der Schlüssel (giống đực) ➔ er. sehen + Akkusativ.\n-> ihn.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["ihn"],
                "translation": "Bạn có chìa khóa không? – Không, tôi chưa nhìn thấy nó.",
                "audio_text": "ihn"
            }
        },
        {
            "id": 51,
            "exercise_type": "phan_loai_cach",
            "question": "Câu 51: Xác định từ được gạch chân trong mỗi câu sau thuộc Akkusativ hay Dativ:",
            "options": null,
            "correct_answer": "Akkusativ, Dativ, Akkusativ, Dativ",
            "explanation": "1. sehen + Akkusativ ➔ dich · 2. helfen + Dativ.\n-> mir · 3. treffen + Akkusativ.\n-> ihn · 4. gehören + Dativ.\n-> uns.\n-> Đáp án: \"Akkusativ, Dativ, Akkusativ, Dativ\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "sentence": "\"Ich sehe dich jeden Tag.\"",
                        "target_phrase": "dich",
                        "case": "Akkusativ",
                        "reason_vi": "sehen + Akk"
                    },
                    {
                        "sentence": "\"Der Arzt hilft mir.\"",
                        "target_phrase": "mir",
                        "case": "Dativ",
                        "reason_vi": "helfen + Dat"
                    },
                    {
                        "sentence": "\"Wir treffen ihn morgen.\"",
                        "target_phrase": "ihn",
                        "case": "Akkusativ",
                        "reason_vi": "treffen + Akk"
                    },
                    {
                        "sentence": "\"Das Auto gehört uns.\"",
                        "target_phrase": "uns",
                        "case": "Dativ",
                        "reason_vi": "gehören + Dat"
                    }
                ],
                "translation": "Hàng 1: \"Ich sehe dich jeden Tag.\" (Akkusativ)\nHàng 2: \"Der Arzt hilft mir.\" (Dativ)\nHàng 3: \"Wir treffen ihn morgen.\" (Akkusativ)\nHàng 4: \"Das Auto gehört uns.\" (Dativ)"
            }
        },
        {
            "id": 52,
            "exercise_type": "phan_loai_cach",
            "question": "Câu 52: Xác định từ được gạch chân trong mỗi câu sau thuộc Akkusativ hay Dativ:",
            "options": null,
            "correct_answer": "Dativ, Akkusativ, Dativ, Akkusativ",
            "explanation": "1. wehtun + Dativ ➔ ihm · 2. lieben + Akkusativ.\n-> mich · 3. passen + Dativ.\n-> dir · 4. brauchen + Akkusativ.\n-> es.\n-> Đáp án: \"Dativ, Akkusativ, Dativ, Akkusativ\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "sentence": "\"Der Kopf tut ihm weh.\"",
                        "target_phrase": "ihm",
                        "case": "Dativ",
                        "reason_vi": "wehtun + Dat"
                    },
                    {
                        "sentence": "\"Sie liebt mich.\"",
                        "target_phrase": "mich",
                        "case": "Akkusativ",
                        "reason_vi": "lieben + Akk"
                    },
                    {
                        "sentence": "\"Passt dir die Hose?\"",
                        "target_phrase": "dir",
                        "case": "Dativ",
                        "reason_vi": "passen + Dat"
                    },
                    {
                        "sentence": "\"Ich brauche es nicht.\"",
                        "target_phrase": "es",
                        "case": "Akkusativ",
                        "reason_vi": "brauchen + Akk"
                    }
                ],
                "translation": "Hàng 1: \"Der Kopf tut ihm weh.\" (Dativ)\nHàng 2: \"Sie liebt mich.\" (Akkusativ)\nHàng 3: \"Passt dir die Hose?\" (Dativ)\nHàng 4: \"Ich brauche es nicht.\" (Akkusativ)"
            }
        },
        {
            "id": 53,
            "exercise_type": "phan_loai_cach",
            "question": "Câu 53: Xác định từ được gạch chân trong mỗi câu sau thuộc Akkusativ hay Dativ:",
            "options": null,
            "correct_answer": "Dativ, Akkusativ, Akkusativ, Dativ",
            "explanation": "1. gefallen + Dativ ➔ Ihnen · 2. hören + Akkusativ.\n-> euch · 3. besuchen + Akkusativ.\n-> uns · 4. danken + Dativ.\n-> dir.\n-> Đáp án: \"Dativ, Akkusativ, Akkusativ, Dativ\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "sentence": "\"Wie gefällt Ihnen das Hotel?\"",
                        "target_phrase": "Ihnen",
                        "case": "Dativ",
                        "reason_vi": "gefallen + Dat"
                    },
                    {
                        "sentence": "\"Ich höre euch nicht.\"",
                        "target_phrase": "euch",
                        "case": "Akkusativ",
                        "reason_vi": "hören + Akk"
                    },
                    {
                        "sentence": "\"Er besucht uns am Sonntag.\"",
                        "target_phrase": "uns",
                        "case": "Akkusativ",
                        "reason_vi": "besuchen + Akk"
                    },
                    {
                        "sentence": "\"Ich danke dir für die Hilfe.\"",
                        "target_phrase": "dir",
                        "case": "Dativ",
                        "reason_vi": "danken + Dat"
                    }
                ],
                "translation": "Hàng 1: \"Wie gefällt Ihnen das Hotel?\" (Dativ)\nHàng 2: \"Ich höre euch nicht.\" (Akkusativ)\nHàng 3: \"Er besucht uns am Sonntag.\" (Akkusativ)\nHàng 4: \"Ich danke dir für die Hilfe.\" (Dativ)"
            }
        },
        {
            "id": 54,
            "exercise_type": "phan_loai_cach",
            "question": "Câu 54: Xác định từ được gạch chân trong mỗi câu sau thuộc Akkusativ hay Dativ:",
            "options": null,
            "correct_answer": "Dativ, Akkusativ, Dativ, Akkusativ",
            "explanation": "1. helfen + Dativ ➔ ihr · 2. sehen + Akkusativ.\n-> sie · 3. stehen + Dativ.\n-> mir · 4. kennen + Akkusativ.\n-> Sie.\n-> Đáp án: \"Dativ, Akkusativ, Dativ, Akkusativ\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "sentence": "\"Die Salbe hilft ihr sehr.\"",
                        "target_phrase": "ihr",
                        "case": "Dativ",
                        "reason_vi": "helfen + Dat"
                    },
                    {
                        "sentence": "\"Manchmal sehe ich sie im Café.\" (cô ấy)",
                        "target_phrase": "sie",
                        "case": "Akkusativ",
                        "reason_vi": "sehen + Akk"
                    },
                    {
                        "sentence": "\"Steht mir das Kleid?\"",
                        "target_phrase": "mir",
                        "case": "Dativ",
                        "reason_vi": "stehen + Dat"
                    },
                    {
                        "sentence": "\"Ich kenne Sie nicht.\" (Ngài)",
                        "target_phrase": "Sie",
                        "case": "Akkusativ",
                        "reason_vi": "kennen + Akk"
                    }
                ],
                "translation": "Hàng 1: \"Die Salbe hilft ihr sehr.\" (Dativ)\nHàng 2: \"Manchmal sehe ich sie im Café.\" (cô ấy) (Akkusativ)\nHàng 3: \"Steht mir das Kleid?\" (Dativ)\nHàng 4: \"Ich kenne Sie nicht.\" (Ngài) (Akkusativ)"
            }
        },
        {
            "id": 55,
            "exercise_type": "phan_loai_cach",
            "question": "Câu 55: Xác định từ được gạch chân trong mỗi câu sau thuộc Akkusativ hay Dativ:",
            "options": null,
            "correct_answer": "Akkusativ, Dativ, Dativ, Akkusativ",
            "explanation": "1. giới từ für + Akkusativ ➔ sie · 2. gefallen + Dativ.\n-> ihr · 3. geben + Dativ (người nhận).\n-> ihr · 4. lesen + Akkusativ.\n-> es.\n-> Đáp án: \"Akkusativ, Dativ, Dativ, Akkusativ\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "sentence": "\"Ich kaufe das Buch für sie.\" (cô ấy)",
                        "target_phrase": "sie",
                        "case": "Akkusativ",
                        "reason_vi": "giới từ für + Akk"
                    },
                    {
                        "sentence": "\"Das Buch gefällt ihr.\"",
                        "target_phrase": "ihr",
                        "case": "Dativ",
                        "reason_vi": "gefallen + Dat"
                    },
                    {
                        "sentence": "\"Ich gebe ihr das Buch.\"",
                        "target_phrase": "ihr",
                        "case": "Dativ",
                        "reason_vi": "geben + Dat người nhận"
                    },
                    {
                        "sentence": "\"Ich lese es jeden Tag.\" (cuốn sách)",
                        "target_phrase": "es",
                        "case": "Akkusativ",
                        "reason_vi": "lesen + Akk"
                    }
                ],
                "translation": "Hàng 1: \"Ich kaufe das Buch für sie.\" (cô ấy) (Akkusativ)\nHàng 2: \"Das Buch gefällt ihr.\" (Dativ)\nHàng 3: \"Ich gebe ihr das Buch.\" (Dativ)\nHàng 4: \"Ich lese es jeden Tag.\" (cuốn sách) (Akkusativ)"
            }
        },
        {
            "id": 56,
            "exercise_type": "phan_loai_giong",
            "question": "Câu 56: Phân loại mạo từ (der / die / das) cho 4 danh từ sau:",
            "options": null,
            "correct_answer": "Kopf: der, Hand: die, Auge: das, Zahn: der",
            "explanation": "Kopf, Hand, Zahn: học thuộc giống (der Kopf, die Hand, der Zahn).\nLưu ý: Auge tận cùng -e nhưng là das (ngoại lệ, giống das Ohr).\n-> Đáp án: \"Kopf: der, Hand: die, Auge: das, Zahn: der\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "noun": "Kopf",
                        "word": "Kopf",
                        "article": "der",
                        "meaning_vi": "đầu",
                        "meaning": "đầu"
                    },
                    {
                        "noun": "Hand",
                        "word": "Hand",
                        "article": "die",
                        "meaning_vi": "bàn tay",
                        "meaning": "bàn tay"
                    },
                    {
                        "noun": "Auge",
                        "word": "Auge",
                        "article": "das",
                        "meaning_vi": "mắt",
                        "meaning": "mắt"
                    },
                    {
                        "noun": "Zahn",
                        "word": "Zahn",
                        "article": "der",
                        "meaning_vi": "răng",
                        "meaning": "răng"
                    }
                ],
                "translation": "Kopf (der): đầu\nHand (die): bàn tay\nAuge (das): mắt\nZahn (der): răng"
            }
        },
        {
            "id": 57,
            "exercise_type": "phan_loai_giong",
            "question": "Câu 57: Phân loại mạo từ (der / die / das) cho 4 danh từ sau:",
            "options": null,
            "correct_answer": "Bauch: der, Schulter: die, Knie: das, Finger: der",
            "explanation": "Bauch, Finger: giống đực (der Bauch, der Finger - học thuộc).\nSchulter: giống cái (die Schulter - học thuộc).\nKnie: giống trung (das Knie - học thuộc).\n-> Đáp án: \"Bauch: der, Schulter: die, Knie: das, Finger: der\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "noun": "Bauch",
                        "word": "Bauch",
                        "article": "der",
                        "meaning_vi": "bụng",
                        "meaning": "bụng"
                    },
                    {
                        "noun": "Schulter",
                        "word": "Schulter",
                        "article": "die",
                        "meaning_vi": "vai",
                        "meaning": "vai"
                    },
                    {
                        "noun": "Knie",
                        "word": "Knie",
                        "article": "das",
                        "meaning_vi": "đầu gối",
                        "meaning": "đầu gối"
                    },
                    {
                        "noun": "Finger",
                        "word": "Finger",
                        "article": "der",
                        "meaning_vi": "ngón tay",
                        "meaning": "ngón tay"
                    }
                ],
                "translation": "Bauch (der): bụng\nSchulter (die): vai\nKnie (das): đầu gối\nFinger (der): ngón tay"
            }
        },
        {
            "id": 58,
            "exercise_type": "phan_loai_giong",
            "question": "Câu 58: Phân loại mạo từ (der / die / das) cho 4 danh từ sau:",
            "options": null,
            "correct_answer": "Fieber: das, Erkältung: die, Husten: der, Medikament: das",
            "explanation": "Mẹo: đuôi -ung luôn là die (die Erkältung)\nđuôi -ment là das (das Medikament).\nTừ không có quy tắc cần học thuộc: das Fieber, der Husten.\n-> Đáp án: \"Fieber: das, Erkältung: die, Husten: der, Medikament: das\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "noun": "Fieber",
                        "word": "Fieber",
                        "article": "das",
                        "meaning_vi": "sốt",
                        "meaning": "sốt"
                    },
                    {
                        "noun": "Erkältung",
                        "word": "Erkältung",
                        "article": "die",
                        "meaning_vi": "cảm lạnh",
                        "meaning": "cảm lạnh"
                    },
                    {
                        "noun": "Husten",
                        "word": "Husten",
                        "article": "der",
                        "meaning_vi": "ho",
                        "meaning": "ho"
                    },
                    {
                        "noun": "Medikament",
                        "word": "Medikament",
                        "article": "das",
                        "meaning_vi": "thuốc men",
                        "meaning": "thuốc men"
                    }
                ],
                "translation": "Fieber (das): sốt\nErkältung (die): cảm lạnh\nHusten (der): ho\nMedikament (das): thuốc men"
            }
        },
        {
            "id": 59,
            "exercise_type": "phan_loai_giong",
            "question": "Câu 59: Phân loại mạo từ (der / die / das) cho 4 danh từ sau:",
            "options": null,
            "correct_answer": "Apotheke: die, Rezept: das, Schmerz: der, Tablette: die",
            "explanation": "Mẹo: đuôi -e thường là die (die Apotheke, die Tablette).\nTừ không có quy tắc cần học thuộc: das Rezept, der Schmerz.\n-> Đáp án: \"Apotheke: die, Rezept: das, Schmerz: der, Tablette: die\"",
            "exp_reward": 15,
            "extra_data": {
                "items": [
                    {
                        "noun": "Apotheke",
                        "word": "Apotheke",
                        "article": "die",
                        "meaning_vi": "nhà thuốc",
                        "meaning": "nhà thuốc"
                    },
                    {
                        "noun": "Rezept",
                        "word": "Rezept",
                        "article": "das",
                        "meaning_vi": "đơn thuốc",
                        "meaning": "đơn thuốc"
                    },
                    {
                        "noun": "Schmerz",
                        "word": "Schmerz",
                        "article": "der",
                        "meaning_vi": "cơn đau",
                        "meaning": "cơn đau"
                    },
                    {
                        "noun": "Tablette",
                        "word": "Tablette",
                        "article": "die",
                        "meaning_vi": "thuốc viên",
                        "meaning": "thuốc viên"
                    }
                ],
                "translation": "Apotheke (die): nhà thuốc\nRezept (das): đơn thuốc\nSchmerz (der): cơn đau\nTablette (die): thuốc viên"
            }
        },
        {
            "id": 60,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 60: Nối từ tiếng Đức với nghĩa tiếng Việt:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Các bộ phận phần thân trên.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "der Bauch", "right": "bụng"},
                    {"left": "der Rücken", "right": "lưng"},
                    {"left": "die Schulter", "right": "vai"},
                    {"left": "die Brust", "right": "ngực"}
                ],
                "translation": "der Bauch = bụng\nder Rücken = lưng\ndie Schulter = vai\ndie Brust = ngực"
            }
        },
        {
            "id": 61,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 61: Nối từ tiếng Đức với nghĩa tiếng Việt:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Các bộ phận chi.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "der Fuß", "right": "bàn chân"},
                    {"left": "das Bein", "right": "chân (cả cẳng)"},
                    {"left": "der Arm", "right": "cánh tay"},
                    {"left": "die Hand", "right": "bàn tay"}
                ],
                "translation": "der Fuß = bàn chân\ndas Bein = chân (cả cẳng)\nder Arm = cánh tay\ndie Hand = bàn tay"
            }
        },
        {
            "id": 62,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 62: Nối danh từ số ít với dạng số nhiều:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Auge + n; Ohr + en; Finger giữ nguyên\nZahn thêm Umlaut + e.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "das Auge", "right": "die Augen"},
                    {"left": "das Ohr", "right": "die Ohren"},
                    {"left": "der Finger", "right": "die Finger"},
                    {"left": "der Zahn", "right": "die Zähne"}
                ],
                "translation": "das Auge (mắt) = die Augen (đôi mắt)\ndas Ohr (tai) = die Ohren (đôi tai)\nder Finger (ngón tay) = die Finger (những ngón tay)\nder Zahn (răng) = die Zähne (những chiếc răng)"
            }
        },
        {
            "id": 63,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 63: Nối từ tiếng Đức với nghĩa tiếng Việt:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Các vật dụng/thuốc tại nhà thuốc.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "die Salbe", "right": "thuốc mỡ"},
                    {"left": "die Tablette", "right": "thuốc viên"},
                    {"left": "das Rezept", "right": "đơn thuốc"},
                    {"left": "das Medikament", "right": "thuốc men"}
                ],
                "translation": "die Salbe = thuốc mỡ\ndie Tablette = thuốc viên\ndas Rezept = đơn thuốc\ndas Medikament = thuốc men"
            }
        },
        {
            "id": 64,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 64: Nối từ tiếng Đức với nghĩa tiếng Việt:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Các từ về bệnh và triệu chứng.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "das Fieber", "right": "cơn sốt"},
                    {"left": "der Schnupfen", "right": "sổ mũi"},
                    {"left": "der Husten", "right": "bệnh ho"},
                    {"left": "die Entzündung", "right": "chứng viêm"}
                ],
                "translation": "das Fieber = cơn sốt\nder Schnupfen = sổ mũi\nder Husten = bệnh ho\ndie Entzündung = chứng viêm"
            }
        },
        {
            "id": 65,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 65: Nối đại từ Nominativ với dạng Akkusativ:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Bảng biến đổi đại từ nhân xưng từ cách 1 sang cách 4.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "mich"},
                    {"left": "du", "right": "dich"},
                    {"left": "wir", "right": "uns"},
                    {"left": "ihr", "right": "euch"}
                ],
                "translation": "ich (tôi - Nom) = mich (tôi - Akk)\ndu (bạn - Nom) = dich (bạn - Akk)\nwir (chúng tôi - Nom) = uns (chúng tôi - Akk)\nihr (các bạn - Nom) = euch (các bạn - Akk)"
            }
        },
        {
            "id": 66,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 66: Nối đại từ Nominativ với dạng Akkusativ:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Chỉ có giống đực (er) biến đổi thành ihn.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "er", "right": "ihn"},
                    {"left": "sie (cô ấy)", "right": "sie"},
                    {"left": "es", "right": "es"},
                    {"left": "Sie (trang trọng)", "right": "Sie"}
                ],
                "translation": "er (anh ấy - Nom) = ihn (anh ấy - Akk)\nsie (cô ấy - Nom) = sie (cô ấy - Akk)\nes (nó - Nom) = es (nó - Akk)\nSie (Ngài - Nom) = Sie (Ngài - Akk)"
            }
        },
        {
            "id": 67,
            "exercise_type": "noi_o_tu_vung",
            "question": "Câu 67: Nối câu hỏi với câu trả lời phù hợp:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Logic hội thoại đăng ký tại phòng khám: Hỏi hẹn trước.\n-> Hỏi đã từng đến chưa.\n-> Hỏi thời gian chờ.\n-> Hướng dẫn chỗ ngồi đợi.\n-> Đáp án: \"Nối đúng 4/4 cặp\"",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Haben Sie einen Termin?", "right": "Nein, leider nicht."},
                    {"left": "Waren Sie schon einmal bei uns?", "right": "Nein, ich bin neu hier."},
                    {"left": "Muss ich lange warten?", "right": "Nein, nur ein paar Minuten."},
                    {"left": "Wo soll ich warten?", "right": "Nehmen Sie bitte im Wartezimmer Platz."}
                ],
                "translation": "1. Haben Sie einen Termin?\n(Ngài có hẹn trước không?) = Nein, leider nicht.\n(Không, tiếc là không.)\n2. Waren Sie schon einmal bei uns?\n(Ngài đã từng đến khám ở chỗ chúng tôi chưa?) = Nein, ich bin neu hier.\n(Chưa, tôi là bệnh nhân mới.)\n3. Muss ich lange warten?\n(Tôi có phải đợi lâu không?) = Nein, nur ein paar Minuten.\n(Không, chỉ vài phút thôi.)\n4. Wo soll ich warten?\n(Tôi nên chờ ở đâu?) = Nehmen Sie bitte im Wartezimmer Platz.\n(Xin ngài hãy ngồi chờ ở phòng đợi.)"
            }
        },
        {
            "id": 68,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 68: Điền 2 từ để hoàn thành câu (ở đây người ta không được phép hút thuốc): \"Hier ___ man nicht ___.\" (dürfen)",
            "options": null,
            "correct_answer": "darf / rauchen",
            "explanation": "Chủ ngữ man dùng với dürfen chia là darf.\nĐộng từ chính rauchen đứng cuối câu ở dạng nguyên thể.\n-> \"Hier darf man nicht rauchen.\"\n-> Đáp án: \"darf / rauchen\"",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Hier ___ man nicht ___.",
                "hints": "(dürfen)",
                "instruction": "Điền từ vào các chỗ trống theo thứ tự, ngăn cách bằng dấu /",
                "accepted_answers": ["darf / rauchen", "darf/rauchen", "darf rauchen"],
                "translation": "Ở đây người ta không được phép hút thuốc.",
                "audio_text": "Hier darf man nicht rauchen"
            }
        },
        {
            "id": 69,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 69: Điền 2 từ để hoàn thành câu (thưa bác sĩ, tôi có được phép tập thể thao không): \"Herr Doktor, ___ ich Sport ___?\" (dürfen)",
            "options": null,
            "correct_answer": "darf / machen",
            "explanation": "Chủ ngữ ich → dürfen chia là darf.\nĐộng từ chính machen ở cuối câu.\n-> \"Herr Doktor, darf ich Sport machen?\"\n-> Đáp án: \"darf / machen\"",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Herr Doktor, ___ ich Sport ___?",
                "hints": "(dürfen)",
                "instruction": "Điền từ vào các chỗ trống theo thứ tự, ngăn cách bằng dấu /",
                "accepted_answers": ["darf / machen", "darf/machen", "darf machen"],
                "translation": "Thưa bác sĩ, tôi có được phép tập thể thao không?",
                "audio_text": "Herr Doktor darf ich Sport machen"
            }
        },
        {
            "id": 70,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 70: Điền 2 từ để hoàn thành câu (nói với nhiều bạn nhỏ, các con hãy trật tự nhé): \"Das Kind schläft. ___ bitte ___!\" (sein)",
            "options": null,
            "correct_answer": "seid / leise",
            "explanation": "Imperativ ngôi ihr của sein là seid, không dùng chủ ngữ ihr.\n-> \"Seid bitte leise!\"\n-> Đáp án: \"seid / leise\"",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Das Kind schläft. ___ bitte ___!",
                "hints": "(sein)",
                "instruction": "Điền từ vào các chỗ trống theo thứ tự, ngăn cách bằng dấu /",
                "accepted_answers": ["seid / leise", "seid/leise", "seid leise", "Seid / leise", "Seid/leise", "Seid leise"],
                "translation": "Đứa trẻ đang ngủ.\nCác con hãy trật tự nhé!",
                "audio_text": "Das Kind schläft Seid leise"
            }
        },
        {
            "id": 71,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 71: Điền 2 đại từ Akkusativ (người bố nói với con): \"Ich liebe ___. Liebst du ___?\" (du / ich)",
            "options": null,
            "correct_answer": "dich / mich",
            "explanation": "lieben + Akkusativ.\nAkkusativ của du là dich, của ich là mich.\n-> \"Ich liebe dich. Liebst du mich?\"\n-> Đáp án: \"dich / mich\"",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Ich liebe ___. Liebst du ___?",
                "hints": "(du / ich)",
                "instruction": "Điền từ vào các chỗ trống theo thứ tự, ngăn cách bằng dấu /",
                "accepted_answers": ["dich / mich", "dich/mich", "dich mich"],
                "translation": "Bố yêu con.\nCon có yêu bố không?",
                "audio_text": "Ich liebe dich Liebst du mich"
            }
        },
        {
            "id": 72,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 72: Điền 2 từ để hoàn thành câu (cánh tay tôi đau, tôi cần một loại thuốc mỡ): \"Mein Arm tut ___ weh. Ich brauche eine ___.\" (ich)",
            "options": null,
            "correct_answer": "mir / Salbe",
            "explanation": "Cấu trúc tut + Dativ + weh, Dativ của ich là mir. die Salbe.\n-> eine Salbe.\n-> Đáp án: \"mir / Salbe\"",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Mein Arm tut ___ weh. Ich brauche eine ___.",
                "hints": "(ich)",
                "instruction": "Điền từ vào các chỗ trống theo thứ tự, ngăn cách bằng dấu /",
                "accepted_answers": ["mir / Salbe", "mir/Salbe", "mir Salbe", "mir / salbe", "mir/salbe", "mir salbe"],
                "translation": "Cánh tay tôi đau.\nTôi cần một loại thuốc mỡ.",
                "audio_text": "Mein Arm tut mir weh Ich brauche eine Salbe"
            }
        },
        {
            "id": 73,
            "exercise_type": "nghe_dien",
            "question": "Câu 73: Nghe và điền 1 từ vào chỗ trống: \"___ jeden Tag spazieren!\"",
            "options": null,
            "correct_answer": "Geh",
            "explanation": "gehen → Imperativ ngôi du: Geh!\n→ \"Geh jeden Tag spazieren!\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"___ jeden Tag spazieren!\"",
                "full_sentence": "\"Geh jeden Tag spazieren!\"",
                "audio_text": "Geh jeden Tag spazieren",
                "hints": "Động từ nguyên mẫu: gehen (ngôi du)",
                "hint_vi": "Hãy đi dạo mỗi ngày!",
                "translation": "Hãy đi dạo mỗi ngày!",
                "accepted_answers": ["Geh", "geh", "Gehe", "gehe", "Geh jeden Tag spazieren!", "Geh jeden Tag spazieren"]
            }
        },
        {
            "id": 74,
            "exercise_type": "nghe_dien",
            "question": "Câu 74: Nghe và điền 1 từ vào chỗ trống: \"Gute Besserung! ___ Sie sich aus!\"",
            "options": null,
            "correct_answer": "Ruhen",
            "explanation": "sich ausruhen → Imperativ ngôi Sie: Ruhen Sie sich aus!\n-> \"Gute Besserung! Ruhen Sie sich aus!\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"Gute Besserung! ___ Sie sich aus!\"",
                "full_sentence": "\"Gute Besserung! Ruhen Sie sich aus!\"",
                "audio_text": "Gute Besserung Ruhen Sie sich aus",
                "hints": "Động từ phản thân: sich ausruhen (ngôi Sie)",
                "hint_vi": "Chúc mau khỏe! Ngài hãy nghỉ ngơi đi.",
                "translation": "Chúc mau khỏe!\nNgài hãy nghỉ ngơi đi.",
                "accepted_answers": ["Ruhen", "ruhen", "Gute Besserung! Ruhen Sie sich aus!", "Ruhen Sie sich aus!"]
            }
        },
        {
            "id": 75,
            "exercise_type": "nghe_dien",
            "question": "Câu 75: Nghe và điền 1 từ vào chỗ trống: \"Was ___ Ihnen?\"",
            "options": null,
            "correct_answer": "fehlt",
            "explanation": "fehlen + Dativ dùng để hỏi thăm bệnh tình, chủ ngữ ngôi 3 số ít: fehlt.\n-> \"Was fehlt Ihnen?\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"Was ___ Ihnen?\"",
                "full_sentence": "\"Was fehlt Ihnen?\"",
                "audio_text": "Was fehlt Ihnen",
                "hints": "Động từ nguyên mẫu: fehlen (chủ ngữ Was)",
                "hint_vi": "Ngài bị làm sao vậy?",
                "translation": "Ngài bị làm sao vậy?",
                "accepted_answers": ["fehlt", "Fehlt", "Was fehlt Ihnen?", "Was fehlt Ihnen"]
            }
        },
        {
            "id": 76,
            "exercise_type": "nghe_dien",
            "question": "Câu 76: Nghe và điền 1 từ vào chỗ trống: \"Der Arzt schreibt mir ein ___.\"",
            "options": null,
            "correct_answer": "Rezept",
            "explanation": "ein + danh từ giống trung (das Rezept) ở Akkusativ: ein Rezept.\n-> \"Der Arzt schreibt mir ein Rezept.\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"Der Arzt schreibt mir ein ___.\"",
                "full_sentence": "\"Der Arzt schreibt mir ein Rezept.\"",
                "audio_text": "Der Arzt schreibt mir ein Rezept",
                "hints": "Danh từ giống trung: das Rezept (đơn thuốc)",
                "hint_vi": "Bác sĩ viết cho tôi một đơn thuốc.",
                "translation": "Bác sĩ viết cho tôi một đơn thuốc.",
                "accepted_answers": ["Rezept", "rezept", "Der Arzt schreibt mir ein Rezept.", "ein Rezept"]
            }
        },
        {
            "id": 77,
            "exercise_type": "nghe_dien",
            "question": "Câu 77: Nghe và điền 1 từ vào chỗ trống: \"Wir ___ hier nicht parken.\"",
            "options": null,
            "correct_answer": "dürfen",
            "explanation": "dürfen chia với chủ ngữ wir: dürfen → \"Wir dürfen hier nicht parken.\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"Wir ___ hier nicht parken.\"",
                "full_sentence": "\"Wir dürfen hier nicht parken.\"",
                "audio_text": "Wir dürfen hier nicht parken",
                "hints": "Modalverb: dürfen (chia với ngôi wir)",
                "hint_vi": "Chúng tôi không được phép đỗ xe ở đây.",
                "translation": "Chúng tôi không được phép đỗ xe ở đây.",
                "accepted_answers": [
                    "dürfen",
                    "duerfen",
                    "Dürfen",
                    "Duerfen",
                    "Wir dürfen hier nicht parken.",
                    "Wir duerfen hier nicht parken."
                ]
            }
        },
        {
            "id": 78,
            "exercise_type": "nghe_dien",
            "question": "Câu 78: Nghe và điền 1 từ vào chỗ trống: \"Du bist meine Traumfrau. Ich liebe ___.\"",
            "options": null,
            "correct_answer": "dich",
            "explanation": "Động từ lieben đi với tân ngữ Akkusativ, đại từ du chuyển thành dich.\n-> \"Du bist meine Traumfrau. Ich liebe dich.\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"Du bist meine Traumfrau. Ich liebe ___.\"",
                "full_sentence": "\"Du bist meine Traumfrau. Ich liebe dich.\"",
                "audio_text": "Du bist meine Traumfrau Ich liebe dich",
                "hints": "Đại từ nhân xưng: du (chia ở Akkusativ sau lieben)",
                "hint_vi": "Em là người phụ nữ trong mơ của anh. Anh yêu em.",
                "translation": "Em là người phụ nữ trong mơ của anh.\nAnh yêu em.",
                "accepted_answers": ["dich", "Dich", "Ich liebe dich.", "Ich liebe dich"]
            }
        },
        {
            "id": 79,
            "exercise_type": "nghe_dien",
            "question": "Câu 79: Nghe và điền 1 từ vào chỗ trống: \"Mein ___ tut mir furchtbar weh.\"",
            "options": null,
            "correct_answer": "Bauch",
            "explanation": "Danh từ giống đực der Bauch, đứng làm chủ ngữ sau mein: Mein Bauch tut mir furchtbar weh.\n-> \"Mein Bauch tut mir furchtbar weh.\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"Mein ___ tut mir furchtbar weh.\"",
                "full_sentence": "\"Mein Bauch tut mir furchtbar weh.\"",
                "audio_text": "Mein Bauch tut mir furchtbar weh",
                "hints": "Danh từ chỉ bộ phận cơ thể: der Bauch (bụng)",
                "hint_vi": "Bụng tôi đau kinh khủng.",
                "translation": "Bụng tôi đau kinh khủng.",
                "accepted_answers": ["Bauch", "bauch", "Mein Bauch tut mir furchtbar weh.", "Mein Bauch tut mir furchtbar weh"]
            }
        },
        {
            "id": 80,
            "exercise_type": "nghe_dien",
            "question": "Câu 80: Nghe và điền 1 từ vào chỗ trống: \"___ jeden Tag eine Tablette!\"",
            "options": null,
            "correct_answer": "Nehmt",
            "explanation": "nehmen → Imperativ ngôi ihr: Nehmt!\n(thông thường lược bỏ chủ ngữ ihr, giữ nguyên gốc nehm- + -t).\n-> \"Nehmt jeden Tag eine Tablette!\"",
            "exp_reward": 15,
            "extra_data": {
                "display_sentence": "\"___ jeden Tag eine Tablette!\"",
                "full_sentence": "\"Nehmt jeden Tag eine Tablette!\"",
                "audio_text": "Nehmt jeden Tag eine Tablette",
                "hints": "Động từ nguyên mẫu: nehmen (Imperativ ngôi ihr)",
                "hint_vi": "Các bạn hãy uống mỗi ngày một viên thuốc!",
                "translation": "Các bạn hãy uống mỗi ngày một viên thuốc!",
                "accepted_answers": [
                    "Nehmt",
                    "nehmt",
                    "Nimm",
                    "nimm",
                    "Nehmt jeden Tag eine Tablette!",
                    "Nehmt jeden Tag eine Tablette",
                    "Nimm jeden Tag eine Tablette!"
                ]
            }
        },
        {
            "id": 81,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 81: Dịch câu sau sang tiếng Đức: \"Ngài hãy uống nhiều nước!\"",
            "options": null,
            "correct_answer": "Trinken Sie viel Wasser!",
            "explanation": "Mệnh lệnh lịch sự: Trinken Sie + viel Wasser.\n-> Đáp án chuẩn: \"Trinken Sie viel Wasser!\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Trinken Sie viel Wasser!",
                    "Trinken Sie viel Wasser",
                    "Trinken Sie bitte viel Wasser!",
                    "Trinken Sie bitte viel Wasser",
                    "Trinken Sie viel Wasser, bitte!",
                    "Trinken Sie viel Wasser, bitte",
                    "Bitte trinken Sie viel Wasser!",
                    "Bitte trinken Sie viel Wasser"
                ],
                "translation": "Ngài hãy uống nhiều nước!",
                "audio_text": "Trinken Sie viel Wasser"
            }
        },
        {
            "id": 82,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 82: Dịch câu sau sang tiếng Đức: \"Ở đây người ta không được phép hút thuốc.\"",
            "options": null,
            "correct_answer": "Hier darf man nicht rauchen.",
            "explanation": "man darf nicht = không được phép\nrauchen (hút thuốc) để cuối câu.\n-> Đáp án chuẩn: \"Hier darf man nicht rauchen.\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Hier darf man nicht rauchen.",
                    "Hier darf man nicht rauchen",
                    "Man darf hier nicht rauchen.",
                    "Man darf hier nicht rauchen"
                ],
                "translation": "Ở đây người ta không được phép hút thuốc.",
                "audio_text": "Hier darf man nicht rauchen"
            }
        },
        {
            "id": 83,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 83: Dịch câu sau sang tiếng Đức (ngôi du): \"Hãy làm bài tập về nhà của bạn!\"",
            "options": null,
            "correct_answer": "Mach deine Hausaufgaben!",
            "explanation": "Imperativ ngôi du của machen là Mach.\nTính từ sở hữu tương ứng ngôi du là deine.\n-> Đáp án chuẩn: \"Mach deine Hausaufgaben!\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Mach deine Hausaufgaben!",
                    "Mach deine Hausaufgaben",
                    "Mach bitte deine Hausaufgaben!",
                    "Mach bitte deine Hausaufgaben",
                    "Mach deine Hausaufgaben, bitte!",
                    "Mach deine Hausaufgaben, bitte",
                    "Bitte mach deine Hausaufgaben!",
                    "Bitte mach deine Hausaufgaben",
                    "Macht eure Hausaufgaben!",
                    "Macht eure Hausaufgaben",
                    "Machen Sie Ihre Hausaufgaben!",
                    "Machen Sie Ihre Hausaufgaben"
                ],
                "translation": "Hãy làm bài tập về nhà của bạn!",
                "audio_text": "Mach deine Hausaufgaben"
            }
        },
        {
            "id": 84,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 84: Dịch câu sau sang tiếng Đức: \"Tôi bị đau đầu dữ dội.\"",
            "options": null,
            "correct_answer": "Ich habe starke Kopfschmerzen.",
            "explanation": "Có hai cách nói: haben + Schmerzen (Ich habe starke Kopfschmerzen) hoặc wehtun + Dativ (Mein Kopf tut mir sehr weh).\n-> Đáp án chuẩn: \"Ich habe starke Kopfschmerzen.\" hoặc \"Mein Kopf tut mir sehr weh.\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Ich habe starke Kopfschmerzen.",
                    "Ich habe starke Kopfschmerzen",
                    "Ich habe sehr starke Kopfschmerzen.",
                    "Ich habe sehr starke Kopfschmerzen",
                    "Mein Kopf tut mir sehr weh.",
                    "Mein Kopf tut mir sehr weh",
                    "Mein Kopf tut mir weh.",
                    "Mein Kopf tut mir weh",
                    "Ich habe Kopfschmerzen.",
                    "Ich habe Kopfschmerzen"
                ],
                "translation": "Tôi bị đau đầu dữ dội.",
                "audio_text": "Ich habe starke Kopfschmerzen"
            }
        },
        {
            "id": 85,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 85: Dịch câu sau sang tiếng Đức: \"Các bạn hãy ăn nhiều rau hơn!\"",
            "options": null,
            "correct_answer": "Esst mehr Gemüse!",
            "explanation": "Imperativ ngôi ihr của essen là Esst.\n-> Đáp án chuẩn: \"Esst mehr Gemüse!\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Esst mehr Gemüse!",
                    "Esst mehr Gemüse",
                    "Esst bitte mehr Gemüse!",
                    "Esst bitte mehr Gemüse",
                    "Esst mehr Gemüse, bitte!",
                    "Esst mehr Gemüse, bitte",
                    "Bitte esst mehr Gemüse!",
                    "Bitte esst mehr Gemüse",
                    "Esst mehr Gemuese!",
                    "Esst mehr Gemuese",
                    "Esst bitte mehr Gemuese!",
                    "Esst bitte mehr Gemuese"
                ],
                "translation": "Các bạn hãy ăn nhiều rau hơn!",
                "audio_text": "Esst mehr Gemüse"
            }
        },
        {
            "id": 86,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 86: Dịch câu sau sang tiếng Đức (ngôi du): \"Hãy nghỉ ngơi đi!\"",
            "options": null,
            "correct_answer": "Ruh dich aus!",
            "explanation": "Mệnh lệnh ngôi du của động từ phản thân tách sich ausruhen là Ruh dich aus!\n-> Đáp án chuẩn: \"Ruh dich aus!\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Ruh dich aus!",
                    "Ruh dich aus",
                    "Ruh dich bitte aus!",
                    "Ruh dich bitte aus",
                    "Ruh dich aus, bitte!",
                    "Ruh dich aus, bitte",
                    "Bitte ruh dich aus!",
                    "Bitte ruh dich aus",
                    "Ruhe dich aus!",
                    "Ruhe dich aus",
                    "Ruht euch aus!",
                    "Ruht euch aus",
                    "Ruhen Sie sich aus!",
                    "Ruhen Sie sich aus"
                ],
                "translation": "Hãy nghỉ ngơi đi!",
                "audio_text": "Ruh dich aus"
            }
        },
        {
            "id": 87,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 87: Dịch câu sau sang tiếng Việt: \"Atmen Sie bitte tief ein und aus!\"",
            "options": null,
            "correct_answer": "Xin ngài hãy hít vào và thở ra thật sâu!",
            "explanation": "tief ein- und ausatmen = hít sâu và thở ra.\n-> Nghĩa tiếng Việt chuẩn: \"Xin ngài hãy hít vào và thở ra thật sâu!\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Xin ngài hãy hít vào và thở ra thật sâu!",
                    "Xin hãy hít vào và thở ra thật sâu!",
                    "Hãy hít vào và thở ra thật sâu!",
                    "Hãy hít vào và thở ra sâu!",
                    "Xin ngài hãy hít sâu và thở ra!",
                    "Làm ơn hãy hít vào và thở ra thật sâu!",
                    "Vui lòng hít vào và thở ra thật sâu!",
                    "Hít vào và thở ra thật sâu!"
                ],
                "translation": "Xin ngài hãy hít vào và thở ra thật sâu!",
                "audio_text": "Atmen Sie bitte tief ein und aus"
            }
        },
        {
            "id": 88,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 88: Dịch câu sau sang tiếng Việt: \"Der Rücken tut ihm weh.\"",
            "options": null,
            "correct_answer": "Lưng của anh ấy bị đau.",
            "explanation": "Cấu trúc wehtun + Dativ (ihm).\n-> Nghĩa tiếng Việt chuẩn: \"Lưng của anh ấy bị đau.\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Lưng của anh ấy bị đau.",
                    "Lưng anh ấy bị đau.",
                    "Lưng anh ấy đau.",
                    "Anh ấy bị đau lưng.",
                    "Anh ấy đau lưng.",
                    "Lưng của ông ấy bị đau.",
                    "Lưng ông ấy bị đau.",
                    "Ông ấy bị đau lưng.",
                    "Lưng cậu ấy bị đau.",
                    "Cậu ấy bị đau lưng."
                ],
                "translation": "Lưng của anh ấy bị đau.",
                "audio_text": "Der Rücken tut ihm weh"
            }
        },
        {
            "id": 89,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 89: Dịch câu sau sang tiếng Việt: \"Darf ich hier fotografieren?\"",
            "options": null,
            "correct_answer": "Tôi có được phép chụp ảnh ở đây không?",
            "explanation": "fotografieren = chụp ảnh. darf ich = xin phép.\n-> Nghĩa tiếng Việt chuẩn: \"Tôi có được phép chụp ảnh ở đây không?\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Tôi có được phép chụp ảnh ở đây không?",
                    "Tôi có được chụp ảnh ở đây không?",
                    "Tôi có thể chụp ảnh ở đây không?",
                    "Tôi chụp ảnh ở đây được không?",
                    "Tôi có được phép chụp hình ở đây không?",
                    "Ở đây tôi có được chụp ảnh không?",
                    "Ở đây tôi có được phép chụp ảnh không?",
                    "Mình có được chụp ảnh ở đây không?"
                ],
                "translation": "Tôi có được phép chụp ảnh ở đây không?",
                "audio_text": "Darf ich hier fotografieren"
            }
        },
        {
            "id": 90,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 90: Dịch câu sau sang tiếng Việt: \"Bleib heute im Bett!\"",
            "options": null,
            "correct_answer": "Hôm nay hãy nằm nghỉ trên giường!",
            "explanation": "Bleib là mệnh lệnh ngôi du của bleiben. im Bett = trên giường.\n-> Nghĩa tiếng Việt chuẩn: \"Hôm nay hãy nằm nghỉ trên giường!\" (hoặc: Hôm nay hãy ở lại trên giường!).",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Hôm nay hãy nằm nghỉ trên giường!",
                    "Hôm nay hãy ở lại trên giường!",
                    "Hôm nay hãy nằm lại trên giường!",
                    "Hãy nằm nghỉ trên giường hôm nay!",
                    "Hãy ở lại trên giường hôm nay!",
                    "Hôm nay hãy nghỉ trên giường!",
                    "Hôm nay hãy ở trên giường nhé!",
                    "Hôm nay hãy nằm trên giường!"
                ],
                "translation": "Hôm nay hãy nằm nghỉ trên giường!",
                "audio_text": "Bleib heute im Bett"
            }
        },
        {
            "id": 91,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 91: Dịch câu sau sang tiếng Việt: \"Wir sehen uns jeden Morgen im Bus.\"",
            "options": null,
            "correct_answer": "Chúng ta gặp nhau mỗi sáng trên xe buýt.",
            "explanation": "sich sehen = gặp nhau, uns chỉ hai bên gặp nhau (chúng ta).\n-> Nghĩa tiếng Việt chuẩn: \"Chúng ta gặp nhau mỗi sáng trên xe buýt.\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Chúng ta gặp nhau mỗi sáng trên xe buýt.",
                    "Chúng tôi gặp nhau mỗi sáng trên xe buýt.",
                    "Chúng mình gặp nhau mỗi sáng trên xe buýt.",
                    "Chúng ta gặp nhau mỗi buổi sáng trên xe buýt.",
                    "Chúng tôi gặp nhau mỗi buổi sáng ở xe buýt.",
                    "Chúng ta gặp nhau mỗi sáng trên xe bus.",
                    "Chúng tôi gặp nhau mỗi sáng trên xe bus."
                ],
                "translation": "Chúng ta gặp nhau mỗi sáng trên xe buýt.",
                "audio_text": "Wir sehen uns jeden Morgen im Bus"
            }
        },
        {
            "id": 92,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 92: Dịch câu sau sang tiếng Việt: \"Zeigen Sie mir bitte Ihre Zunge!\"",
            "options": null,
            "correct_answer": "Xin ngài hãy cho tôi xem lưỡi của ngài!",
            "explanation": "zeigen = chỉ/cho xem. die Zunge = lưỡi.\n-> Nghĩa tiếng Việt chuẩn: \"Xin ngài hãy cho tôi xem lưỡi của ngài!\"",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Xin ngài hãy cho tôi xem lưỡi của ngài!",
                    "Xin hãy cho tôi xem lưỡi của ngài!",
                    "Hãy cho tôi xem lưỡi của ngài!",
                    "Hãy cho tôi xem lưỡi của bạn!",
                    "Làm ơn cho tôi xem lưỡi của ngài!",
                    "Vui lòng cho tôi xem lưỡi của ngài!",
                    "Xin hãy thè lưỡi ra!",
                    "Hãy thè lưỡi ra!",
                    "Cho tôi xem lưỡi của bạn!"
                ],
                "translation": "Xin ngài hãy cho tôi xem lưỡi của ngài!",
                "audio_text": "Zeigen Sie mir bitte Ihre Zunge"
            }
        },
        {
            "id": 93,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 93: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Nehmen Sie bitte die Tabletten nach dem Essen!",
            "explanation": "Quy tắc câu Mệnh lệnh (Imperativ) ngôi Sie: Động từ nguyên mẫu đứng đầu câu (V1), chủ ngữ Sie đứng ngay sau động từ (V2), từ lịch sự 'bitte' đứng sau Sie.\nTrạng ngữ thời gian 'nach dem Essen' đứng sau tân ngữ 'die Tabletten' (hoặc ngược lại).\n-> \"Nehmen Sie bitte die Tabletten nach dem Essen!\" (hoặc \"Bitte nehmen Sie die Tabletten nach dem Essen!\").",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["bitte", "die Tabletten", "Sie", "nehmen", "nach dem Essen", "!"],
                "accepted_answers": [
                    "Nehmen Sie bitte die Tabletten nach dem Essen!",
                    "Bitte nehmen Sie die Tabletten nach dem Essen!",
                    "Nehmen Sie die Tabletten bitte nach dem Essen!",
                    "Nehmen Sie nach dem Essen bitte die Tabletten!",
                    "Bitte nehmen Sie nach dem Essen die Tabletten!"
                ],
                "translation": "Xin ngài hãy uống thuốc sau bữa ăn!",
                "audio_text": "Nehmen Sie bitte die Tabletten nach dem Essen"
            }
        },
        {
            "id": 94,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 94: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Räumt eure Zimmer auf!",
            "explanation": "Quy tắc câu Mệnh lệnh (Imperativ) ngôi ihr: Động từ chia như ngôi ihr ở thì Hiện tại (gốc räum- + -t thành Räumt) và thông thường lược bỏ chủ ngữ ihr (chỉ thêm khi muốn nhấn mạnh).\nVới động từ tách aufräumen, tiền tố tách 'auf' bắt buộc phải chuyển xuống đứng ở cuối câu.\n-> \"Räumt eure Zimmer auf!\" Khối từ 'eure Zimmer' đóng vai trò tân ngữ Akkusativ.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["auf", "eure Zimmer", "räumt", "!"],
                "accepted_answers": ["Räumt eure Zimmer auf!"],
                "translation": "Các con hãy dọn dẹp phòng của mình đi!",
                "audio_text": "Räumt eure Zimmer auf"
            }
        },
        {
            "id": 95,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 95: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Iss weniger Schokolade!",
            "explanation": "Quy tắc câu Mệnh lệnh (Imperativ) ngôi du với động từ bất quy tắc: essen đổi nguyên âm e → i thành 'Iss!' (bỏ chủ ngữ du và bỏ đuôi -st).\nCụm tân ngữ 'weniger Schokolade' (ít sô cô la hơn) đứng sau động từ mệnh lệnh.\n-> \"Iss weniger Schokolade!\" (Quy tắc chung ngôi du: bỏ du, bỏ đuôi -st, giữ nguyên âm đổi e ➔ i).",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["weniger", "Schokolade", "iss", "!"],
                "accepted_answers": ["Iss weniger Schokolade!"],
                "translation": "Hãy ăn ít sô cô la lại!",
                "audio_text": "Iss weniger Schokolade"
            }
        },
        {
            "id": 96,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 96: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Im Wartezimmer darf man nicht telefonieren.",
            "explanation": "Quy tắc câu trần thuật với Động từ khuyết (Modalverb): Động từ chia 'darf' (chủ ngữ man) bắt buộc đứng ở Vị trí 2 sau trạng từ nơi chốn 'Im Wartezimmer'.\nĐộng từ chính 'telefonieren' ở dạng nguyên mẫu đứng ở cuối câu (khung câu Satzklammer), từ phủ định 'nicht' đứng ngay trước động từ chính.\n-> \"Im Wartezimmer darf man nicht telefonieren.\" (hoặc \"Man darf im Wartezimmer nicht telefonieren.\").",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["telefonieren", "darf", "im Wartezimmer", "nicht", "man", "."],
                "accepted_answers": [
                    "Im Wartezimmer darf man nicht telefonieren.",
                    "Man darf im Wartezimmer nicht telefonieren.",
                    "Man darf nicht im Wartezimmer telefonieren."
                ],
                "translation": "Trong phòng đợi người ta không được phép gọi điện thoại.",
                "audio_text": "Im Wartezimmer darf man nicht telefonieren"
            }
        },
        {
            "id": 97,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 97: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Ich vermisse dich jeden Tag.",
            "explanation": "Quy tắc vị trí tân ngữ Akkusativ: Động từ vermissen đi với tân ngữ trực tiếp chỉ người ở cách Akkusativ (đại từ 'dich').\nĐại từ nhân xưng 'dich' đứng ngay sau động từ chia 'vermisse', trạng ngữ thời gian 'jeden Tag' đứng sau (hoặc đưa lên đầu câu thì động từ đảo lên V2).\n-> \"Ich vermisse dich jeden Tag.\" (hoặc \"Jeden Tag vermisse ich dich.\" / \"Dich vermisse ich jeden Tag.\").",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["dich", "jeden Tag", "vermisse", "Ich", "."],
                "accepted_answers": [
                    "Ich vermisse dich jeden Tag.",
                    "Jeden Tag vermisse ich dich.",
                    "Dich vermisse ich jeden Tag."
                ],
                "translation": "Anh nhớ em mỗi ngày.",
                "audio_text": "Ich vermisse dich jeden Tag"
            }
        },
        {
            "id": 98,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 98: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Die Hausärztin gibt mir eine Salbe.",
            "explanation": "Quy tắc trật tự tân ngữ Dativ và Akkusativ: Khi động từ đi kèm cả tân ngữ chỉ người và tân ngữ chỉ vật (như geben), đại từ nhân xưng ở Dativ ('mir' - người nhận) bắt buộc phải đứng trước cụm danh từ ở Akkusativ ('eine Salbe' - vật được cho).\nChủ ngữ 'Die Hausärztin' đứng đầu câu, động từ 'gibt' ở Vị trí 2.\n-> \"Die Hausärztin gibt mir eine Salbe.\" (hoặc \"Mir gibt die Hausärztin eine Salbe.\").",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["eine Salbe", "gibt", "die Hausärztin", "mir", "."],
                "accepted_answers": [
                    "Die Hausärztin gibt mir eine Salbe.",
                    "Mir gibt die Hausärztin eine Salbe.",
                    "Eine Salbe gibt mir die Hausärztin."
                ],
                "translation": "Bác sĩ gia đình đưa cho tôi một tuýp thuốc mỡ.",
                "audio_text": "Die Hausärztin gibt mir eine Salbe"
            }
        },
        {
            "id": 99,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 99: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Mein Bruder hat Bauchschmerzen.",
            "explanation": "Quy tắc diễn đạt triệu chứng sức khỏe: Dùng cấu trúc haben + tên bệnh/cơn đau (Bauchschmerzen).\nChủ ngữ ngôi thứ 3 số ít 'Mein Bruder' đi với động từ chia 'hat' ở Vị trí 2, danh từ bệnh đứng cuối câu.\n-> \"Mein Bruder hat Bauchschmerzen.\" (hoặc đảo ngữ nhấn mạnh \"Bauchschmerzen hat mein Bruder.\").",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["Bauchschmerzen", "hat", "mein Bruder", "."],
                "accepted_answers": ["Mein Bruder hat Bauchschmerzen.", "Bauchschmerzen hat mein Bruder."],
                "translation": "Em trai tôi bị đau bụng.",
                "audio_text": "Mein Bruder hat Bauchschmerzen"
            }
        },
        {
            "id": 100,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 100: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Darf ich im Bett frühstücken?",
            "explanation": "Quy tắc câu hỏi Yes/No (Ja/Nein-Frage) với Động từ khuyết: Động từ khuyết chia theo chủ ngữ ich ('Darf') bắt buộc phải đảo lên Vị trí 1 (đầu câu), chủ ngữ 'ich' đứng ở Vị trí 2. Động từ chính 'frühstücken' ở dạng nguyên thể đứng ở cuối câu, trạng ngữ nơi chốn 'im Bett' nằm ở giữa khung câu.\n-> \"Darf ich im Bett frühstücken?\" Khung câu: Darf (V1) ... im Bett ... frühstücken (cuối)?",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["im Bett", "frühstücken", "darf", "ich", "?"],
                "accepted_answers": ["Darf ich im Bett frühstücken?", "Darf ich frühstücken im Bett?"],
                "translation": "Tôi có được ăn sáng trên giường không?",
                "audio_text": "Darf ich im Bett frühstücken"
            }
        },
        {
            "id": 101,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 101: Tìm và sửa lỗi sai trong câu sau: \"Arbeit nicht so viel!\"",
            "options": null,
            "correct_answer": "Arbeite nicht so viel!",
            "explanation": "Gốc arbeit- kết thúc bằng -t nên Imperativ ngôi du bắt buộc phải thêm đuôi -e.\n-> Arbeite!\n(Quy tắc chung: gốc động từ kết thúc bằng -t, -d, hoặc phụ âm + m/n như zeichn-, öffn-, atm- đều phải thêm -e ở ngôi du).\n-> Đáp án đúng: \"Arbeite nicht so viel!\"",
            "exp_reward": 15,
            "extra_data": {
                "wrong_sentence": "Arbeit nicht so viel!",
                "accepted_answers": ["Arbeite nicht so viel!", "Arbeite nicht so viel"],
                "translation": "Đừng làm việc nhiều quá!",
                "audio_text": "Arbeite nicht so viel"
            }
        },
        {
            "id": 102,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 102: Tìm và sửa lỗi sai trong câu sau: \"Du darf nicht so laut sprechen.\"",
            "options": null,
            "correct_answer": "Du darfst nicht so laut sprechen.",
            "explanation": "Động từ khuyết thiếu dürfen khi chia ở ngôi du thì hiện tại phải đổi nguyên âm ü.\n-> a và thêm đuôi -st thành darfst (không giữ nguyên dạng darf của ngôi ich/er/sie/es).\n-> Đáp án đúng: \"Du darfst nicht so laut sprechen!\"",
            "exp_reward": 15,
            "extra_data": {
                "wrong_sentence": "Du darf nicht so laut sprechen.",
                "accepted_answers": ["Du darfst nicht so laut sprechen.", "Du darfst nicht so laut sprechen"],
                "translation": "Bạn không được phép nói to như vậy.",
                "audio_text": "Du darfst nicht so laut sprechen"
            }
        },
        {
            "id": 103,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 103: Tìm và sửa lỗi sai trong câu sau: \"Ich besuche ihm morgen.\"",
            "options": null,
            "correct_answer": "Ich besuche ihn morgen.",
            "explanation": "Động từ besuchen đòi hỏi tân ngữ trực tiếp ở cách Akkusativ (besuchen + Akkusativ).\nĐại từ nhân xưng giống đực er chuyển sang Akkusativ là ihn (không dùng đại từ Dativ ihm).\n-> Đáp án đúng: \"Ich besuche ihn morgen.\".",
            "exp_reward": 15,
            "extra_data": {
                "wrong_sentence": "Ich besuche ihm morgen.",
                "accepted_answers": [
                    "Ich besuche ihn morgen.",
                    "Ich besuche ihn morgen",
                    "Morgen besuche ich ihn.",
                    "Morgen besuche ich ihn"
                ],
                "translation": "Ngày mai tôi sẽ đến thăm anh ấy.",
                "audio_text": "Ich besuche ihn morgen"
            }
        },
        {
            "id": 104,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 104: Tìm và sửa lỗi sai trong câu sau: \"Sprech bitte langsamer!\"",
            "options": null,
            "correct_answer": "Sprich bitte langsamer!",
            "explanation": "Động từ sprechen là động từ mạnh biến đổi nguyên âm e ➔ i ở các ngôi số ít (du sprichst).\nKhi chuyển sang câu Mệnh lệnh (Imperativ) ở ngôi du, quy tắc bắt buộc là phải GIỮ nguyên âm biến đổi i (và thông thường lược bỏ chủ ngữ du cùng đuôi -st): Sprech.\n-> Sprich!\n-> Đáp án đúng: \"Sprich bitte langsamer!\"",
            "exp_reward": 15,
            "extra_data": {
                "wrong_sentence": "Sprech bitte langsamer!",
                "accepted_answers": [
                    "Sprich bitte langsamer!",
                    "Sprich bitte langsamer",
                    "Bitte sprich langsamer!",
                    "Bitte sprich langsamer"
                ],
                "translation": "Xin hãy nói chậm hơn!",
                "audio_text": "Sprich bitte langsamer"
            }
        },
        {
            "id": 105,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 105: Tìm và sửa lỗi sai trong câu sau: \"Er darft heute nicht Fußball spielen.\"",
            "options": null,
            "correct_answer": "Er darf heute nicht Fußball spielen.",
            "explanation": "Động từ khuyết thiếu dürfen khi chia ở ngôi thứ ba số ít (er/sie/es/man) ở thì Hiện tại KHÔNG có đuôi -t (dạng chia là darf, giống hệt ngôi ich, không phải darft).\n-> Đáp án đúng: \"Er darf heute nicht Fußball spielen.\".",
            "exp_reward": 15,
            "extra_data": {
                "wrong_sentence": "Er darft heute nicht Fußball spielen.",
                "accepted_answers": [
                    "Er darf heute nicht Fußball spielen.",
                    "Er darf heute nicht Fußball spielen",
                    "Heute darf er nicht Fußball spielen.",
                    "Heute darf er nicht Fußball spielen"
                ],
                "translation": "Hôm nay anh ấy không được phép chơi bóng đá.",
                "audio_text": "Er darf heute nicht Fußball spielen"
            }
        },
        {
            "id": 106,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 106: Tìm và sửa lỗi sai trong câu sau: \"Ruhen aus Sie sich!\"",
            "options": null,
            "correct_answer": "Ruhen Sie sich aus!",
            "explanation": "Quy tắc câu Mệnh lệnh (Imperativ) ngôi Sie với động từ phản thân tách (sich ausruhen): Động từ chia đứng đầu câu (Ruhen), đại từ nhân xưng Sie đứng ngay sau động từ, đại từ phản thân sich đứng sau Sie, và tiền tố tách aus bắt buộc phải đứng ở cuối câu.\n-> Ruhen Sie sich aus!\n-> Đáp án đúng: \"Ruhen Sie sich aus!\"",
            "exp_reward": 15,
            "extra_data": {
                "wrong_sentence": "Ruhen aus Sie sich!",
                "accepted_answers": ["Ruhen Sie sich aus!", "Ruhen Sie sich aus"],
                "translation": "Xin ngài hãy nghỉ ngơi đi!",
                "audio_text": "Ruhen Sie sich aus"
            }
        },
        {
            "id": 107,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 107: Dịch từ sau sang tiếng Đức (kèm mạo từ der / die / das): \"cái mũi\"",
            "options": null,
            "correct_answer": "die Nase",
            "explanation": "die Nase (giống cái, số nhiều: die Nasen) · Ví dụ: \"Meine Nase läuft.\" (Mũi tôi đang chảy nước).\n-> Nghĩa tiếng Đức chuẩn kèm mạo từ là: \"die Nase\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["die Nase", "die nase", "Nase", "nase"],
                "translation": "cái mũi",
                "audio_text": "die Nase"
            }
        },
        {
            "id": 108,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 108: Dịch từ sau sang tiếng Đức (kèm mạo từ der / die / das): \"bác sĩ gia đình (nam)\"",
            "options": null,
            "correct_answer": "der Hausarzt",
            "explanation": "der Hausarzt (giống đực, số nhiều: die Hausärzte) · Ví dụ: \"Ich muss zum Hausarzt gehen.\" (Tôi phải đi bác sĩ gia đình).\n-> Nghĩa tiếng Đức chuẩn kèm mạo từ là: \"der Hausarzt\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["der Hausarzt", "der hausarzt", "Hausarzt", "hausarzt"],
                "translation": "bác sĩ gia đình (nam)",
                "audio_text": "der Hausarzt"
            }
        },
        {
            "id": 109,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 109: Dịch từ sau sang tiếng Đức (kèm mạo từ der / die / das): \"đơn thuốc\"",
            "options": null,
            "correct_answer": "das Rezept",
            "explanation": "das Rezept (giống trung, số nhiều: die Rezepte) · Ví dụ: \"Der Arzt schreibt mir ein Rezept.\" (Bác sĩ viết cho tôi một đơn thuốc).\n-> Nghĩa tiếng Đức chuẩn kèm mạo từ là: \"das Rezept\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["das Rezept", "das rezept", "Rezept", "rezept"],
                "translation": "đơn thuốc",
                "audio_text": "das Rezept"
            }
        },
        {
            "id": 110,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 110: Dịch từ sau sang tiếng Đức (kèm mạo từ der / die / das): \"trái tim\"",
            "options": null,
            "correct_answer": "das Herz",
            "explanation": "das Herz (giống trung, số nhiều: die Herzen) · Ví dụ: \"Mein Herz schlägt schnell.\" (Tim tôi đập nhanh).\n-> Nghĩa tiếng Đức chuẩn kèm mạo từ là: \"das Herz\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["das Herz", "das herz", "Herz", "herz"],
                "translation": "trái tim",
                "audio_text": "das Herz"
            }
        },
        {
            "id": 111,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 111: Dịch từ sau sang tiếng Việt: \"die Schulter\"",
            "options": null,
            "correct_answer": "vai",
            "explanation": "die Schulter (giống cái, số nhiều: die Schultern) · Ví dụ: \"Sie hat Schmerzen in der Schulter.\" (Cô ấy bị đau ở vai).\n-> Đáp án: \"vai\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["vai", "bả vai", "cái vai", "vai (bả vai)"],
                "translation": "vai",
                "audio_text": "die Schulter"
            }
        },
        {
            "id": 112,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 112: Dịch từ sau sang tiếng Việt: \"die Apotheke\"",
            "options": null,
            "correct_answer": "hiệu thuốc",
            "explanation": "die Apotheke (giống cái, số nhiều: die Apotheken) · Ví dụ: \"Die Apotheke ist gleich um die Ecke.\" (Hiệu thuốc ở ngay góc phố).\n-> Đáp án: \"hiệu thuốc\" (hoặc nhà thuốc, tiệm thuốc).",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["hiệu thuốc", "nhà thuốc", "tiệm thuốc", "quầy thuốc"],
                "translation": "hiệu thuốc\nnhà thuốc",
                "audio_text": "die Apotheke"
            }
        },
        {
            "id": 113,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 113: Dịch từ sau sang tiếng Việt: \"das Bein\"",
            "options": null,
            "correct_answer": "chân",
            "explanation": "das Bein (giống trung, số nhiều: die Beine) · Ví dụ: \"Sie hat lange Beine.\" (Cô ấy có đôi chân dài).\nLưu ý: das Bein chỉ cẳng chân/chân nói chung, đừng nhầm với der Fuß (bàn chân).\n-> Đáp án: \"chân\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["chân", "cẳng chân", "chân (cả cẳng)", "cái chân", "đôi chân"],
                "translation": "chân (cả cẳng)",
                "audio_text": "das Bein"
            }
        },
        {
            "id": 114,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 114: Dịch từ sau sang tiếng Việt: \"der Schnupfen\"",
            "options": null,
            "correct_answer": "sổ mũi",
            "explanation": "der Schnupfen (giống đực, danh từ thường ở số ít) · Ví dụ: \"Bei Schnupfen brauche ich Taschentücher.\" (Khi sổ mũi tôi cần khăn giấy).\n-> Đáp án: \"sổ mũi\".",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["sổ mũi", "nghẹt mũi", "ngạt mũi", "cảm lạnh nhẹ", "bệnh sổ mũi", "chảy nước mũi"],
                "translation": "sổ mũi",
                "audio_text": "der Schnupfen"
            }
        },
        {
            "id": 115,
            "exercise_type": "dung_sai",
            "question": "Câu 115: Đọc đoạn văn 'Tipps für die Gesundheit' và chọn Đúng (Richtig) hoặc Sai (Falsch) cho nhận định: \"Man soll sich jeden Tag bewegen.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Richtig",
            "explanation": "Đoạn văn có câu: \"Und vergessen Sie nicht: Bewegen Sie sich jeden Tag!\" (Và đừng quên: Hãy vận động mỗi ngày!).\n-> Nhận định \"Man soll sich jeden Tag bewegen.\" là Đúng (Richtig).\n-> Đáp án: \"Richtig\"",
            "exp_reward": 15,
            "extra_data": {
                "passage": "Um gesund zu bleiben, müssen Sie auf Ihren Körper achten. Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine. Trinken Sie täglich mindestens zwei Liter Wasser. Trinken Sie nicht zu viel Kaffee oder Alkohol. Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge. Wenn Sie am Computer arbeiten, machen Sie oft Pausen für Ihre Augen. Und vergessen Sie nicht: Bewegen Sie sich jeden Tag!",
                "statement": "Man soll sich jeden Tag bewegen.",
                "translation": "Người ta nên vận động mỗi ngày.",
                "audio_text": "Man soll sich jeden Tag bewegen"
            }
        },
        {
            "id": 116,
            "exercise_type": "dung_sai",
            "question": "Câu 116: Đọc đoạn văn 'Tipps für die Gesundheit' và chọn Đúng (Richtig) hoặc Sai (Falsch) cho nhận định: \"Rauchen ist gut für die Lunge.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Falsch",
            "explanation": "Đoạn văn ghi rõ: \"Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge.\" (Bạn cũng không được phép hút thuốc, điều đó rất có hại cho phổi, chứ không phải tốt cho phổi).\n-> Nhận định \"Rauchen ist gut für die Lunge.\" là Sai (Falsch).\n-> Đáp án: \"Falsch\"",
            "exp_reward": 15,
            "extra_data": {
                "passage": "Um gesund zu bleiben, müssen Sie auf Ihren Körper achten. Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine. Trinken Sie täglich mindestens zwei Liter Wasser. Trinken Sie nicht zu viel Kaffee oder Alkohol. Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge. Wenn Sie am Computer arbeiten, machen Sie oft Pausen für Ihre Augen. Und vergessen Sie nicht: Bewegen Sie sich jeden Tag!",
                "statement": "Rauchen ist gut für die Lunge.",
                "translation": "Hút thuốc thì tốt cho phổi.",
                "audio_text": "Rauchen ist gut für die Lunge"
            }
        },
        {
            "id": 117,
            "exercise_type": "dung_sai",
            "question": "Câu 117: Đọc đoạn văn 'Tipps für die Gesundheit' và chọn Đúng (Richtig) hoặc Sai (Falsch) cho nhận định: \"Obst und Gemüse sind gut für die Gesundheit.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Richtig",
            "explanation": "Đoạn văn có câu: \"Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine.\" (Hãy ăn nhiều trái cây và rau củ vì chúng có nhiều vitamin để giữ gìn sức khỏe).\n-> Nhận định \"Obst und Gemüse sind gut für die Gesundheit.\" là Đúng (Richtig).\n-> Đáp án: \"Richtig\"",
            "exp_reward": 15,
            "extra_data": {
                "passage": "Um gesund zu bleiben, müssen Sie auf Ihren Körper achten. Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine. Trinken Sie täglich mindestens zwei Liter Wasser. Trinken Sie nicht zu viel Kaffee oder Alkohol. Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge. Wenn Sie am Computer arbeiten, machen Sie oft Pausen für Ihre Augen. Und vergessen Sie nicht: Bewegen Sie sich jeden Tag!",
                "statement": "Obst und Gemüse sind gut für die Gesundheit.",
                "translation": "Trái cây và rau củ tốt cho sức khỏe.",
                "audio_text": "Obst und Gemüse sind gut für die Gesundheit"
            }
        },
        {
            "id": 118,
            "exercise_type": "dung_sai",
            "question": "Câu 118: Đọc đoạn văn 'Tipps für die Gesundheit' và chọn Đúng (Richtig) hoặc Sai (Falsch) cho nhận định: \"Am Computer soll man oft Pausen machen.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Richtig",
            "explanation": "Đoạn văn có câu: \"Wenn Sie am Computer arbeiten, machen Sie oft Pausen für Ihre Augen.\" (Khi làm việc bên máy tính, hãy thường xuyên nghỉ ngơi cho mắt).\n-> Nhận định \"Am Computer soll man oft Pausen machen.\" là Đúng (Richtig).\n-> Đáp án: \"Richtig\"",
            "exp_reward": 15,
            "extra_data": {
                "passage": "Um gesund zu bleiben, müssen Sie auf Ihren Körper achten. Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine. Trinken Sie täglich mindestens zwei Liter Wasser. Trinken Sie nicht zu viel Kaffee oder Alkohol. Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge. Wenn Sie am Computer arbeiten, machen Sie oft Pausen für Ihre Augen. Und vergessen Sie nicht: Bewegen Sie sich jeden Tag!",
                "statement": "Am Computer soll man oft Pausen machen.",
                "translation": "Khi dùng máy tính nên thường xuyên nghỉ ngơi.",
                "audio_text": "Am Computer soll man oft Pausen machen"
            }
        },
        {
            "id": 119,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 119: Sắp xếp các câu thoại sau theo đúng thứ tự diễn biến hội thoại hợp lý:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5",
            "explanation": "Nhân viên phòng khám chào hỏi và hỏi lý do gọi đến.\n-> Bệnh nhân báo bị ốm và cần đặt lịch hẹn hôm nay.\n-> Phòng khám hỏi triệu chứng và hỏi có sốt không.\n-> Bệnh nhân mô tả đau đầu và bị sốt từ hôm qua.\n-> Phòng khám hẹn giờ đến khám vào lúc 11 giờ hôm nay (Imperativ: Kommen Sie bitte...!).",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Praxis", "text": "Praxis Dr. Weber, guten Tag! Was kann ich für Sie tun?"},
                    {"id": 2, "speaker": "Herr Klein", "text": "Guten Tag. Ich bin krank und brauche heute einen Termin."},
                    {"id": 3, "speaker": "Praxis", "text": "Was fehlt Ihnen denn? Haben Sie Fieber?"},
                    {"id": 4, "speaker": "Herr Klein", "text": "Ja, mein Kopf tut sehr weh und ich habe seit gestern Fieber."},
                    {"id": 5, "speaker": "Praxis", "text": "Kommen Sie bitte heute um 11 Uhr in die Praxis!"}
                ],
                "correct_order": [1, 2, 3, 4, 5],
                "translation": "- Phòng khám: Phòng khám Bác sĩ Weber xin chào!\nTôi có thể giúp gì cho ngài?\n- Ông Klein: Xin chào.\nTôi bị ốm và hôm nay tôi cần một lịch hẹn khám.\n- Phòng khám: Ngài bị làm sao vậy?\nNgài có sốt không?\n- Ông Klein: Vâng, đầu tôi đau dữ dội và tôi bị sốt từ hôm qua.\n- Phòng khám: Xin ngài hãy đến phòng khám vào lúc 11 giờ hôm nay!"
            }
        },
        {
            "id": 120,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 120: Sắp xếp các câu thoại sau theo đúng thứ tự diễn biến hội thoại hợp lý:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5, 6",
            "explanation": "Dược sĩ chào hỏi và hỏi nhu cầu của khách.\n-> Khách kể con trai bị ho nặng và hỏi mua siro ho.\n-> Dược sĩ xác nhận có và hỏi cháu có sốt không.\n-> Khách xác nhận không sốt chỉ bị ho.\n-> Dược sĩ đưa siro ho và dặn cách dùng (Imperativ: Geben Sie ihm...).\n-> Khách cảm ơn sự giúp đỡ và chào tạm biệt.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Apothekerin", "text": "Guten Tag! Was kann ich für Sie tun?"},
                    {"id": 2, "speaker": "Kunde", "text": "Guten Tag! Mein Sohn hat starken Husten. Haben Sie einen Hustensaft?"},
                    {"id": 3, "speaker": "Apothekerin", "text": "Ja, natürlich. Hat Ihr Sohn auch Fieber?"},
                    {"id": 4, "speaker": "Kunde", "text": "Nein, er hat kein Fieber, nur Husten."},
                    {"id": 5, "speaker": "Apothekerin", "text": "Hier ist der Hustensaft. Geben Sie ihm zweimal täglich einen Löffel!"},
                    {"id": 6, "speaker": "Kunde", "text": "Vielen Dank für Ihre Hilfe. Auf Wiedersehen!"}
                ],
                "correct_order": [1, 2, 3, 4, 5, 6],
                "translation": "- Dược sĩ: Xin chào!\nTôi có thể giúp gì cho quý khách?\n- Khách: Xin chào!\nCon trai tôi bị ho nặng.\nHiệu thuốc có siro ho không ạ?\n- Dược sĩ: Vâng, có chứ.\nCháu có bị sốt không?\n- Khách: Không, cháu không sốt, chỉ bị ho thôi.\n- Dược sĩ: Siro ho đây ạ.\nHãy cho cháu uống mỗi ngày hai lần, mỗi lần một thìa!\n- Khách: Cảm ơn nhiều vì sự giúp đỡ của cô.\nTạm biệt!"
            }
        },
        {
            "id": 121,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 121: Sắp xếp các câu thoại sau theo đúng thứ tự diễn biến hội thoại hợp lý:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5",
            "explanation": "Con xin phép ra ngoài chơi (Darf ich jetzt draußen spielen?).\n-> Mẹ hỏi thời tiết (Regnet es draußen?).\n-> Con trả lời trời không mưa, trời nắng.\n-> Mẹ cho phép chơi ở sân chơi nhưng dặn mặc áo khoác (Imperativ: zieh eine Jacke an!).\n-> Con cảm ơn và đồng ý làm ngay.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Sohn", "text": "Mama, ich bin fertig mit den Hausaufgaben. Darf ich jetzt draußen spielen?"},
                    {"id": 2, "speaker": "Mutter", "text": "Regnet es draußen?"},
                    {"id": 3, "speaker": "Sohn", "text": "Nein, es regnet nicht. Die Sonne scheint."},
                    {"id": 4, "speaker": "Mutter", "text": "Gut, du darfst eine Stunde auf dem Spielplatz spielen. Aber zieh eine Jacke an! Es ist kalt."},
                    {"id": 5, "speaker": "Sohn", "text": "Danke, Mama! Mach ich."}
                ],
                "correct_order": [1, 2, 3, 4, 5],
                "translation": "- Con trai: Mẹ ơi, con làm xong bài tập về nhà rồi.\nBây giờ con ra ngoài chơi được không ạ?\n- Mẹ: Bên ngoài trời có mưa không?\n- Con trai: Không ạ, trời không mưa.\nTrời nắng.\n- Mẹ: Được, con được chơi một tiếng ở sân chơi.\nNhưng hãy mặc áo khoác vào!\nTrời lạnh.\n- Con trai: Cảm ơn mẹ!\nVâng, con làm ngay!"
            }
        },
        {
            "id": 122,
            "exercise_type": "bieu_tuong_benh",
            "question": "Câu 122: Nhìn biểu tượng bệnh và chọn câu tiếng Đức diễn đạt đúng nhất:",
            "options": ["Ich habe Fieber.", "Ich habe Zahnschmerzen.", "Mein Knie tut weh.", "Ich habe Schnupfen."],
            "correct_answer": "Ich habe Fieber.",
            "explanation": "Biểu tượng ngậm nhiệt kế biểu thị bệnh Sốt (Fieber).\n-> Đáp án đúng: \"Ich habe Fieber.\"",
            "exp_reward": 15,
            "extra_data": {
                "emoji_icon": "🤒",
                "weather_icon": "🤒",
                "icon_alt_vi": "Mặt ngậm nhiệt kế",
                "translation": "Tôi bị sốt.",
                "audio_text": "Ich habe Fieber"
            }
        },
        {
            "id": 123,
            "exercise_type": "bieu_tuong_benh",
            "question": "Câu 123: Nhìn biểu tượng bệnh và chọn câu tiếng Đức diễn đạt đúng nhất:",
            "options": ["Mein Bauch tut weh.", "Ich habe Husten.", "Ich habe Schnupfen.", "Ich bin gesund."],
            "correct_answer": "Ich habe Schnupfen.",
            "explanation": "Biểu tượng xì mũi bằng khăn giấy biểu thị bệnh Sổ mũi (Schnupfen).\n-> Đáp án đúng: \"Ich habe Schnupfen.\"",
            "exp_reward": 15,
            "extra_data": {
                "emoji_icon": "🤧",
                "weather_icon": "🤧",
                "icon_alt_vi": "Mặt xì mũi",
                "translation": "Tôi bị sổ mũi.",
                "audio_text": "Ich habe Schnupfen"
            }
        },
        {
            "id": 124,
            "exercise_type": "bieu_tuong_benh",
            "question": "Câu 124: Nhìn biểu tượng bệnh và chọn câu tiếng Đức diễn đạt đúng nhất:",
            "options": ["Ich habe Kopfschmerzen.", "Mein Bein tut weh.", "Ich habe Husten.", "Ich bin müde."],
            "correct_answer": "Ich habe Kopfschmerzen.",
            "explanation": "Biểu tượng đầu quấn băng biểu thị chứng Đau đầu (Kopfschmerzen).\n-> Đáp án đúng: \"Ich habe Kopfschmerzen.\"",
            "exp_reward": 15,
            "extra_data": {
                "emoji_icon": "🤕",
                "weather_icon": "🤕",
                "icon_alt_vi": "Đầu quấn băng",
                "translation": "Tôi bị đau đầu.",
                "audio_text": "Ich habe Kopfschmerzen"
            }
        },
        {
            "id": 125,
            "exercise_type": "bieu_tuong_benh",
            "question": "Câu 125: Nhìn biểu tượng bệnh và chọn câu tiếng Đức diễn đạt đúng nhất:",
            "options": [
                "Ich habe Zahnschmerzen.",
                "Mein Bauch tut weh.",
                "Ich habe Schnupfen.",
                "Mein Fuß tut weh."
            ],
            "correct_answer": "Mein Bauch tut weh.",
            "explanation": "Biểu tượng buồn nôn liên quan đến bệnh Đau dạ dày/Đau bụng (Bauchschmerzen / Bauch tut weh).\n-> Đáp án đúng: \"Mein Bauch tut weh.\"",
            "exp_reward": 15,
            "extra_data": {
                "emoji_icon": "🤢",
                "weather_icon": "🤢",
                "icon_alt_vi": "Mặt xanh xao buồn nôn",
                "translation": "Bụng tôi bị đau.",
                "audio_text": "Mein Bauch tut weh"
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
    print(f"Đã nạp thành công {len(exercises_data)} bài tập (18 dạng bài) cho Bài 12.")
    conn.close()

if __name__ == "__main__":
    seed_lesson_12()
