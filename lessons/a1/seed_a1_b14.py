# -*- coding: utf-8 -*-
"""
Seed file Bài 14 (A1): "Ôn tập A1 (Tiếp theo) — Mạo từ, Động từ sein, Quốc gia/Ngôn ngữ & Phương hướng"
Vị trí A1: lesson_id = 28 (sau Bài 13)
Tích hợp 4 Học phần Lý thuyết (màu hóa der/die/das + Bảng chia sein + Quốc gia/Ngôn ngữ + La bàn Phương hướng SVG)
+ 18 Từ vựng mới (không trùng Bài 1->13) + Đúng 125 Bài tập độc nhất từ Đặc tả Bài 14 (Dictation, Semantic Tolerance, Cap Warning).
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


def seed_lesson_14():
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
    lesson_id = 28
    lesson_title = 'Bài 14: Ôn tập A1 (Tiếp theo) — Mạo từ, Động từ sein, Quốc gia/Ngôn ngữ & Phương hướng'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed font-sans">
        <!-- BANNER TỔNG QUAN BÀI 14 -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-br from-indigo-700 via-blue-700 to-emerald-800 text-white shadow-xl relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/20 backdrop-blur-md text-amber-200 text-xs font-black uppercase tracking-wider">
                    DeutschMeister A1 • ÔN TẬP A1 (TIẾP THEO) • Bài 14
                </span>
                <h1 class="text-2xl sm:text-4xl font-black text-white tracking-tight">
                    Ôn tập A1: Mạo từ Nominativ, Động từ „sein“, Quốc gia &amp; Phương hướng
                </h1>
                <p class="text-blue-100 text-sm sm:text-base font-normal max-w-3xl leading-relaxed">
                    Hệ thống hóa mạo từ xác định/không xác định/phủ định (der/die/das, ein/eine, kein/keine), chia động từ „sein“ ở Präsens và Präteritum, cặp Quốc gia – Ngôn ngữ, và trọng tâm đặc biệt phân biệt 2 cách diễn đạt phương hướng địa lý (im Norden vs. nördlich).
                </p>
                <div class="pt-2 flex flex-wrap gap-2 text-xs font-bold">
                    <span class="px-3 py-1.5 rounded-xl bg-blue-500/30 border border-blue-200/40 whitespace-nowrap">🟦 der (Đực)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-rose-500/30 border border-rose-200/40 whitespace-nowrap">🟥 die (Cái / Số nhiều)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-emerald-500/30 border border-emerald-200/40 whitespace-nowrap">🟩 das (Trung)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/15 border border-white/25 whitespace-nowrap">⏱️ sein (Präsens &amp; Präteritum)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/15 border border-white/25 whitespace-nowrap">🧭 Phương hướng (im + Danh từ / -lich)</span>
                </div>
            </div>
            <div class="absolute -right-6 -bottom-8 opacity-15 text-9xl select-none pointer-events-none">🧭</div>
        </div>

        <!-- HỌC PHẦN 1: MẠO TỪ Ở NOMINATIV -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm shrink-0">1</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Tổng Ôn: Mạo Từ (Artikel) ở Nominativ
                </h2>
            </div>
            <p class="text-sm text-slate-700">
                Trong tiếng Đức, danh từ luôn đi kèm mạo từ để thể hiện Giống (Đực / Cái / Trung) và Số (Ít / Nhiều):
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs sm:text-sm">
                <div class="p-3.5 rounded-2xl bg-indigo-50/70 border border-indigo-200 space-y-1">
                    <div class="font-black text-indigo-900">1. Mạo từ xác định (Bestimmter Artikel)</div>
                    <p class="text-slate-600">Dùng khi danh từ đã được xác định, đã nhắc đến trước đó, hoặc là duy nhất.</p>
                </div>
                <div class="p-3.5 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-1">
                    <div class="font-black text-amber-900">2. Mạo từ không xác định (Unbestimmter Artikel)</div>
                    <p class="text-slate-600">Dùng khi nhắc đến sự vật lần đầu tiên. <b class="text-rose-700">Lưu ý: Không có mạo từ không xác định ở dạng số nhiều.</b></p>
                </div>
                <div class="p-3.5 rounded-2xl bg-rose-50/70 border border-rose-200 space-y-1">
                    <div class="font-black text-rose-900">3. Mạo từ phủ định (Negativartikel)</div>
                    <p class="text-slate-600">Dùng để phủ định trực tiếp một danh từ bằng cách thêm chữ <b>k</b> trước mạo từ không xác định (<i>kein / keine</i>).</p>
                </div>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-xs">
                <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[640px]">
                    <thead>
                        <tr class="bg-slate-100 text-slate-900 border-b border-slate-200">
                            <th class="px-4 py-3 font-extrabold">Giống / Số</th>
                            <th class="px-4 py-3 font-extrabold">Xác định (Der/Die/Das)</th>
                            <th class="px-4 py-3 font-extrabold">Không xác định (Ein)</th>
                            <th class="px-4 py-3 font-extrabold">Phủ định (Kein)</th>
                            <th class="px-4 py-3 font-extrabold">Ví dụ minh họa</th>
                            <th class="px-3 py-3 text-center font-extrabold">Nghe</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr class="bg-blue-50/70">
                            <td class="px-4 py-3 font-black text-blue-900">🟦 Đực (Maskulinum)</td>
                            <td class="px-4 py-3 font-mono font-black text-blue-700">der</td>
                            <td class="px-4 py-3 font-mono font-bold text-blue-800">ein</td>
                            <td class="px-4 py-3 font-mono font-bold text-blue-900">kein</td>
                            <td class="px-4 py-3">
                                <div class="font-mono font-semibold text-slate-900">Das ist <b class="text-blue-700">ein</b> Tisch. <b class="text-blue-700">Der</b> Tisch ist alt.</div>
                                <div class="text-xs text-slate-600 italic">Đây là một cái bàn. Cái bàn đó cũ rồi.</div>
                            </td>
                            <td class="px-3 py-3 text-center"><button type="button" onclick="b14_speakGerman('Das ist ein Tisch. Der Tisch ist alt.')" class="p-1.5 rounded-lg bg-white hover:bg-blue-100 border border-blue-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="bg-rose-50/70">
                            <td class="px-4 py-3 font-black text-rose-900">🟥 Cái (Femininum)</td>
                            <td class="px-4 py-3 font-mono font-black text-rose-700">die</td>
                            <td class="px-4 py-3 font-mono font-bold text-rose-800">eine</td>
                            <td class="px-4 py-3 font-mono font-bold text-rose-900">keine</td>
                            <td class="px-4 py-3">
                                <div class="font-mono font-semibold text-slate-900">Ist das eine Lampe? Nein, das ist <b class="text-rose-700">keine</b> Lampe.</div>
                                <div class="text-xs text-slate-600 italic">Đó là một cái đèn à? Không, đó không phải đèn.</div>
                            </td>
                            <td class="px-3 py-3 text-center"><button type="button" onclick="b14_speakGerman('Ist das eine Lampe? Nein, das ist keine Lampe.')" class="p-1.5 rounded-lg bg-white hover:bg-rose-100 border border-rose-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="bg-emerald-50/70">
                            <td class="px-4 py-3 font-black text-emerald-900">🟩 Trung (Neutrum)</td>
                            <td class="px-4 py-3 font-mono font-black text-emerald-700">das</td>
                            <td class="px-4 py-3 font-mono font-bold text-emerald-800">ein</td>
                            <td class="px-4 py-3 font-mono font-bold text-emerald-900">kein</td>
                            <td class="px-4 py-3">
                                <div class="font-mono font-semibold text-slate-900">Das ist <b class="text-emerald-700">ein</b> Buch. <b class="text-emerald-700">Das</b> Buch ist neu.</div>
                                <div class="text-xs text-slate-600 italic">Đây là một quyển sách. Quyển sách đó mới.</div>
                            </td>
                            <td class="px-3 py-3 text-center"><button type="button" onclick="b14_speakGerman('Das ist ein Buch. Das Buch ist neu.')" class="p-1.5 rounded-lg bg-white hover:bg-emerald-100 border border-emerald-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="bg-rose-50/40">
                            <td class="px-4 py-3 font-black text-rose-900">🟥 Số nhiều (Plural)</td>
                            <td class="px-4 py-3 font-mono font-black text-rose-700">die</td>
                            <td class="px-4 py-3 italic text-slate-500">(không có)</td>
                            <td class="px-4 py-3 font-mono font-bold text-rose-900">keine</td>
                            <td class="px-4 py-3">
                                <div class="font-mono font-semibold text-slate-900">Das sind <b class="text-rose-700">keine</b> Kinder. Das sind Studenten.</div>
                                <div class="text-xs text-slate-600 italic">Đó không phải trẻ em. Đó là các sinh viên.</div>
                            </td>
                            <td class="px-3 py-3 text-center"><button type="button" onclick="b14_speakGerman('Das sind keine Kinder. Das sind Studenten.')" class="p-1.5 rounded-lg bg-white hover:bg-rose-100 border border-rose-200 cursor-pointer">🔊</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- HỌC PHẦN 2: ĐỘNG TỪ SEIN -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm shrink-0">2</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Tổng Ôn: Động Từ „sein“ (Thì, Là, Ở) — Hiện Tại &amp; Quá Khứ
                </h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs sm:text-sm">
                <div class="p-3.5 rounded-2xl bg-emerald-50 border border-emerald-200">
                    <span class="font-black text-emerald-900">⏱️ Dấu hiệu Hiện tại (Präsens):</span>
                    <span class="font-mono font-bold text-emerald-800 ml-1">heute</span> (hôm nay), <span class="font-mono font-bold text-emerald-800">jetzt</span> (bây giờ).
                </div>
                <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200">
                    <span class="font-black text-amber-900">⏪ Dấu hiệu Quá khứ (Präteritum):</span>
                    <span class="font-mono font-bold text-amber-900 ml-1">gestern</span> (hôm qua), <span class="font-mono font-bold text-amber-900">früher</span> (trước đây), <span class="font-mono font-bold text-amber-900">letztes Jahr</span> (năm ngoái), <span class="font-mono font-bold text-amber-900">schon mal</span> (đã từng).
                </div>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-xs">
                <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[580px]">
                    <thead>
                        <tr class="bg-indigo-50 text-indigo-950 border-b border-indigo-200">
                            <th class="px-4 py-3 font-extrabold">Ngôi (Chủ ngữ)</th>
                            <th class="px-4 py-3 font-extrabold">Präsens (Hiện tại)</th>
                            <th class="px-4 py-3 font-extrabold">Präteritum (Quá khứ đơn)</th>
                            <th class="px-4 py-3 font-extrabold">Ví dụ</th>
                            <th class="px-3 py-3 text-center font-extrabold">Nghe</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr>
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">ich <span class="font-sans font-normal text-slate-500">(tôi)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">bin</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-amber-700">war</td>
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900">Gestern <b>war</b> ich im Kino.</span> <span class="text-xs text-slate-500 italic block">Hôm qua tôi ở rạp chiếu phim.</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Gestern war ich im Kino.')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">du <span class="font-sans font-normal text-slate-500">(bạn)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">bist</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-amber-700">warst</td>
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900"><b>Warst</b> du gestern zu Hause?</span> <span class="text-xs text-slate-500 italic block">Hôm qua bạn có ở nhà không?</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Warst du gestern zu Hause?')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">er/sie/es <span class="font-sans font-normal text-slate-500">(anh/cô ấy/nó)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">ist</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-amber-700">war</td>
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900">Früher <b>war</b> sie Lehrerin.</span> <span class="text-xs text-slate-500 italic block">Trước đây cô ấy là giáo viên.</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Früher war sie Lehrerin.')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">wir <span class="font-sans font-normal text-slate-500">(chúng tôi)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">sind</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-amber-700">waren</td>
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900">Wir <b>waren</b> gestern in Berlin.</span> <span class="text-xs text-slate-500 italic block">Hôm qua chúng tôi ở Berlin.</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Wir waren gestern in Berlin.')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">ihr <span class="font-sans font-normal text-slate-500">(các bạn)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">seid</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-amber-700">wart</td>
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900">Wo <b>wart</b> ihr gestern?</span> <span class="text-xs text-slate-500 italic block">Hôm qua các bạn đã ở đâu?</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Wo wart ihr gestern?')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">sie/Sie <span class="font-sans font-normal text-slate-500">(họ/Ngài)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">sind</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-amber-700">waren</td>
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900"><b>Waren</b> Sie schon mal in Paris?</span> <span class="text-xs text-slate-500 italic block">Ngài đã từng ở Paris chưa?</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Waren Sie schon mal in Paris?')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- HỌC PHẦN 3: QUỐC GIA & NGÔN NGỮ -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm shrink-0">3</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Quốc Gia &amp; Ngôn Ngữ (Länder und Sprachen)
                </h2>
            </div>
            <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-200 text-xs sm:text-sm space-y-1.5">
                <p><b>Quy tắc chung:</b> Tên ngôn ngữ thường có đuôi <code class="px-1.5 py-0.5 rounded bg-white border border-indigo-200 font-bold text-indigo-700">-isch</code> / <code class="px-1.5 py-0.5 rounded bg-white border border-indigo-200 font-bold text-indigo-700">-sch</code> nhưng <b>KHÔNG có công thức cố định</b> (<i>Frankreich → Französisch, Spanien → Spanisch, Polen → Polnisch, Vietnam → Vietnamesisch, England → Englisch, Deutschland → Deutsch</i>). Hãy học theo từng cặp quốc gia – ngôn ngữ.</p>
                <p><b>Lưu ý viết hoa &amp; mạo từ quốc gia:</b> Viết hoa khi là danh từ (<i>Ich lerne Deutsch, auf Deutsch</i>). Đa số quốc gia không dùng mạo từ (<i>aus Deutschland, aus Vietnam</i>), ngoại trừ một số nước bắt buộc có mạo từ: <i>aus der Türkei, aus der Schweiz, aus den USA</i>.</p>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-xs">
                <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[540px]">
                    <thead>
                        <tr class="bg-slate-100 text-slate-900 border-b border-slate-200">
                            <th class="px-4 py-3 font-extrabold">Quốc gia</th>
                            <th class="px-4 py-3 font-extrabold">Ngôn ngữ</th>
                            <th class="px-4 py-3 font-extrabold">Quốc gia</th>
                            <th class="px-4 py-3 font-extrabold">Ngôn ngữ</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr>
                            <td class="px-4 py-2.5 font-semibold">Deutschland, Österreich <span class="text-xs text-slate-500 block">(Đức, Áo)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700 flex items-center justify-between gap-2">Deutsch <button type="button" onclick="b14_speakGerman('Deutschland, Österreich, Deutsch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></td>
                            <td class="px-4 py-2.5 font-semibold">Spanien <span class="text-xs text-slate-500 block">(Tây Ban Nha)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Spanisch</span><button type="button" onclick="b14_speakGerman('Spanien, Spanisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-semibold">Frankreich <span class="text-xs text-slate-500 block">(Pháp)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Französisch</span><button type="button" onclick="b14_speakGerman('Frankreich, Französisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                            <td class="px-4 py-2.5 font-semibold">Italien <span class="text-xs text-slate-500 block">(Ý)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Italienisch</span><button type="button" onclick="b14_speakGerman('Italien, Italienisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-semibold">Ägypten <span class="text-xs text-slate-500 block">(Ai Cập)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Arabisch</span><button type="button" onclick="b14_speakGerman('Ägypten, Arabisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                            <td class="px-4 py-2.5 font-semibold">Russland <span class="text-xs text-slate-500 block">(Nga)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Russisch</span><button type="button" onclick="b14_speakGerman('Russland, Russisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-semibold">Polen <span class="text-xs text-slate-500 block">(Ba Lan)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Polnisch</span><button type="button" onclick="b14_speakGerman('Polen, Polnisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                            <td class="px-4 py-2.5 font-semibold">Vietnam <span class="text-xs text-slate-500 block">(Việt Nam)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Vietnamesisch</span><button type="button" onclick="b14_speakGerman('Vietnam, Vietnamesisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                        </tr>
                        <tr>
                            <td class="px-4 py-2.5 font-semibold">Dänemark <span class="text-xs text-slate-500 block">(Đan Mạch)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Dänisch</span><button type="button" onclick="b14_speakGerman('Dänemark, Dänisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                            <td class="px-4 py-2.5 font-semibold">Großbritannien (England) <span class="text-xs text-slate-500 block">(Anh)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Englisch</span><button type="button" onclick="b14_speakGerman('Großbritannien, Englisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                        </tr>
                        <tr class="bg-amber-50/40">
                            <td class="px-4 py-2.5 font-semibold">die Türkei <span class="text-xs text-rose-700 block">(Thổ Nhĩ Kỳ • có mạo từ)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Türkisch</span><button type="button" onclick="b14_speakGerman('die Türkei, Türkisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer">🔊</button></div></td>
                            <td class="px-4 py-2.5 font-semibold">die Schweiz <span class="text-xs text-rose-700 block">(Thụy Sĩ • có mạo từ)</span></td>
                            <td class="px-4 py-2.5 font-mono font-bold text-indigo-700"><div class="flex items-center justify-between gap-2"><span>Deutsch / Französisch / Italienisch <span class="font-sans text-[11px] font-normal text-slate-500">(tùy vùng)</span></span><button type="button" onclick="b14_speakGerman('die Schweiz, Deutsch, Französisch, Italienisch')" class="p-1 rounded bg-slate-50 hover:bg-indigo-50 cursor-pointer shrink-0">🔊</button></div></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- HỌC PHẦN 4: PHƯƠNG HƯỚNG & VỊ TRÍ (LA BÀN TƯƠNG TÁC) -->
        <section class="space-y-4">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm shrink-0">4</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Trọng Tâm Đặc Biệt: Phương Hướng &amp; Vị Trí (Himmelsrichtungen)
                </h2>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm">
                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200">
                    <div class="font-black text-slate-900 mb-1">4 hướng chính:</div>
                    <b>Norden</b> (Bắc), <b>Süden</b> (Nam), <b>Osten</b> (Đông), <b>Westen</b> (Tây).
                </div>
                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200">
                    <div class="font-black text-slate-900 mb-1">4 hướng phụ:</div>
                    <b>Nordosten</b> (ĐB), <b>Nordwesten</b> (TB), <b>Südosten</b> (ĐN), <b>Südwesten</b> (TN).
                </div>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border-2 border-amber-300 space-y-3">
                <div class="font-black text-amber-950 text-sm">⚠️ 2 CÁCH NÓI KHÁC NGHĨA: BÊN TRONG vs BÊN NGOÀI</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs sm:text-sm">
                    <div class="p-3.5 rounded-xl bg-white border border-blue-200 space-y-1.5">
                        <div class="font-black text-blue-800">CÁCH 1: Dùng Danh từ (Bắt buộc có „im“)</div>
                        <p class="text-xs font-semibold text-blue-700">👉 Ở phía Bắc / Nam / … <b>BÊN TRONG X</b> (A thuộc X).</p>
                        <div class="font-mono text-xs bg-blue-50 p-2 rounded-lg text-blue-950 font-bold">A liegt <u>im + [Danh từ hướng viết hoa]</u> + von + B.</div>
                        <div class="flex items-center justify-between gap-2">
                            <div><i>Hanoi liegt <b>im Norden</b> von Vietnam.</i> <span class="text-slate-500 text-xs block">Hà Nội nằm ở miền Bắc của Việt Nam.</span></div>
                            <button type="button" onclick="b14_speakGerman('Hanoi liegt im Norden von Vietnam.')" class="p-1 rounded bg-blue-50 hover:bg-blue-100 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="flex items-center justify-between gap-2">
                            <div><i>München liegt <b>im Süden</b> von Deutschland.</i> <span class="text-slate-500 text-xs block">München nằm ở miền Nam của nước Đức.</span></div>
                            <button type="button" onclick="b14_speakGerman('München liegt im Süden von Deutschland.')" class="p-1 rounded bg-blue-50 hover:bg-blue-100 cursor-pointer shrink-0">🔊</button>
                        </div>
                    </div>
                    <div class="p-3.5 rounded-xl bg-white border border-emerald-200 space-y-1.5">
                        <div class="font-black text-emerald-800">CÁCH 2: Dùng Tính từ (-lich, TUYỆT ĐỐI KHÔNG dùng „im“)</div>
                        <p class="text-xs font-semibold text-emerald-700">👉 Ở phía Bắc / Nam / … <b>BÊN NGOÀI X</b> (A không thuộc X, so sánh hai nơi riêng biệt).</p>
                        <div class="font-mono text-xs bg-emerald-50 p-2 rounded-lg text-emerald-950 font-bold">A liegt <u>[Tính từ hướng viết thường]</u> + von + B.</div>
                        <div class="flex items-center justify-between gap-2">
                            <div><i>China liegt <b>nördlich</b> von Vietnam.</i> <span class="text-slate-500 text-xs block">Trung Quốc nằm ở phía Bắc Việt Nam.</span></div>
                            <button type="button" onclick="b14_speakGerman('China liegt nördlich von Vietnam.')" class="p-1 rounded bg-emerald-50 hover:bg-emerald-100 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="flex items-center justify-between gap-2">
                            <div><i>Österreich liegt <b>südlich</b> von Deutschland.</i> <span class="text-slate-500 text-xs block">Áo nằm ở phía Nam nước Đức.</span></div>
                            <button type="button" onclick="b14_speakGerman('Österreich liegt südlich von Deutschland.')" class="p-1 rounded bg-emerald-50 hover:bg-emerald-100 cursor-pointer shrink-0">🔊</button>
                        </div>
                    </div>
                </div>
                <div class="p-2.5 rounded-xl bg-white/90 border border-amber-200 text-xs text-amber-950">
                    <b>💡 Ghi chú Trung tâm / Giữa:</b> <b>Zentrum</b> = trung tâm thành phố (<i>im Zentrum von Hanoi</i>); <b>Mitte</b> = giữa của một nước/vùng (<i>in der Mitte von Vietnam</i>).
                </div>
            </div>

            <!-- CONTAINER SƠ ĐỒ LA BÀN TƯƠNG TÁC -->
            <div id="b14-compass-svg-container" class="p-4 sm:p-5 rounded-3xl bg-indigo-50/40 border border-indigo-200"></div>
        </section>
    </div>
    """

    cursor.execute("""
        INSERT OR REPLACE INTO lessons (id, level_id, title, grammar_content)
        VALUES (?, ?, ?, ?);
    """, (lesson_id, a1_id, lesson_title, grammar_html))

    # Cập nhật 18 từ vựng mới của Bài 14 (đã đối chiếu loại hoàn toàn từ trùng Bài 1 -> Bài 13)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    vocab_items = [
        ("Laptop", "der", "máy tính xách tay (Pl: die Laptops)", "„Das ist kein Fernseher, das ist ein Laptop.“ — Đó không phải tivi, đó là một chiếc laptop."),
        ("Rucksack", "der", "ba lô (Pl: die Rucksäcke)", "„Ist das ein Rucksack von Thomas?“ — Đó có phải là một chiếc ba lô của Thomas không?"),
        ("Schlüssel", "der", "chìa khóa (Pl: die Schlüssel)", "„Wo ist heute der Schlüssel?“ — Hôm nay chìa khóa ở đâu?"),
        ("Arzt", "der", "bác sĩ (nam); bác sĩ nói chung (Pl: die Ärzte)", "„Früher war mein Vater Arzt.“ — Trước đây bố tôi từng là bác sĩ."),
        ("Lehrer", "der", "giáo viên (nam); thầy giáo (Pl: die Lehrer)", "„Früher waren wir Studenten, jetzt sind wir Lehrer.“ — Trước đây chúng tôi là sinh viên, nay là giáo viên."),
        ("Film", "der", "bộ phim (Pl: die Filme)", "„Gestern war ich im Kino, der Film war fantastisch!“ — Hôm qua tôi ở rạp, bộ phim rất tuyệt vời!"),
        ("Computer", "der", "máy vi tính (Pl: die Computer)", "„Das ist kein Fernseher, das ist ein Computer.“ — Đó không phải tivi, đó là máy vi tính."),
        ("Nordwesten", "der", "hướng Tây Bắc (Pl: nur Sg.)", "„Bremen liegt im Nordwesten von Deutschland.“ — Bremen nằm ở miền Tây Bắc của nước Đức."),
        ("Südosten", "der", "hướng Đông Nam (Pl: nur Sg.)", "„Griechenland liegt im Südosten von Europa.“ — Hy Lạp nằm ở miền Đông Nam của châu Âu."),
        ("Südwesten", "der", "hướng Tây Nam (Pl: nur Sg.)", "„Spanien liegt im Südwesten von Europa.“ — Tây Ban Nha nằm ở miền Tây Nam của châu Âu."),
        ("Kamera", "die", "máy ảnh (Pl: die Kameras)", "„Das ist keine Kamera, das ist ein Handy.“ — Đó không phải máy ảnh, đó là điện thoại."),
        ("Muttersprache", "die", "tiếng mẹ đẻ (Pl: die Muttersprachen)", "„Seine Muttersprache ist Arabisch.“ — Tiếng mẹ đẻ của anh ấy là tiếng Ả Rập."),
        ("Freundin", "die", "bạn (nữ); bạn gái (Pl: die Freundinnen)", "„Meine Freundin spricht gut Deutsch und Englisch.“ — Bạn (nữ) của tôi nói tốt tiếng Đức và tiếng Anh."),
        ("Kind", "das", "đứa trẻ; con (Pl: die Kinder)", "„Das Kind lernt heute Deutsch in der Schule.“ — Đứa trẻ hôm nay học tiếng Đức ở trường."),
        ("Konzert", "das", "buổi hòa nhạc (Pl: die Konzerte)", "„Das Konzert gestern Abend war fantastisch!“ — Buổi hòa nhạc tối qua thật tuyệt vời!"),
        ("Radio", "das", "cái đài radio (Pl: die Radios)", "„Nein, das ist kein Radio.“ — Không, đó không phải là một cái đài."),
        ("Zentrum", "das", "trung tâm (thành phố) (Pl: die Zentren)", "„Das Hotel liegt im Zentrum von Hanoi.“ — Khách sạn nằm ở trung tâm Hà Nội."),
        ("Europa", "das", "châu Âu (Thường dùng KHÔNG mạo từ: in Europa, aus Europa; Pl: nur Sg.)", "„Russland liegt im Osten von Europa.“ — Nga nằm ở miền Đông của châu Âu.")
    ]

    for word, art, mean, ex_sent in vocab_items:
        cursor.execute("""
            INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
            VALUES (?, ?, ?, ?, ?);
        """, (lesson_id, word, art, mean, ex_sent))

    print(f"Đã cập nhật thành công {len(vocab_items)} từ vựng cho Bài 14.")

    # Nạp chính xác 125 câu bài tập Bài 14 theo README/readme_b_i_14.md
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    exercises_data = [
        {
            "id": 1,
            "exercise_type": "trac_nghiem",
            "question": "Câu 1: Chọn giới từ thích hợp:\n\"Berlin liegt ___ Nordosten von Deutschland.\"",
            "options": ["in", "im", "an", "bei"],
            "correct_answer": "im",
            "explanation": "\"Nordosten\" là danh từ viết hoa chỉ hướng (nằm bên trong nước Đức), bắt buộc dùng cụm \"im + [Danh từ hướng]\"\n-> Đáp án: im.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Berlin liegt im Nordosten von Deutschland.",
                "translation": "Berlin nằm ở miền Đông Bắc của nước Đức."
            }
        },
        {
            "id": 2,
            "exercise_type": "trac_nghiem",
            "question": "Câu 2: Chọn giới từ thích hợp:\n\"Hamburg liegt ___ nördlich von Hannover.\"",
            "options": ["in", "im", "(không điền giới từ)", "am"],
            "correct_answer": "(không điền giới từ)",
            "explanation": "\"nördlich\" là tính từ (có đuôi -lich, Hamburg nằm bên ngoài Hannover), tuyệt đối không dùng giới từ \"im\" hay \"in\"\n-> Đáp án: (không điền giới từ).",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Hamburg liegt nördlich von Hannover.",
                "translation": "Hamburg nằm ở phía Bắc của Hannover."
            }
        },
        {
            "id": 3,
            "exercise_type": "trac_nghiem",
            "question": "Câu 3: Chọn câu ĐÚNG NHẤT mô tả vị trí của Cần Thơ (thuộc Việt Nam):",
            "options": [
                "Can Tho liegt im südlich von Vietnam.",
                "Can Tho liegt im Süden von Vietnam.",
                "Can Tho liegt im Süden Vietnam.",
                "Can Tho liegt südlich in Vietnam."
            ],
            "correct_answer": "Can Tho liegt im Süden von Vietnam.",
            "explanation": "Cần Thơ thuộc Việt Nam và dùng danh từ chỉ hướng \"Süden\" nên phải có cụm \"im Süden von\".\nPhương án A ghép nhầm \"im\" với tính từ \"südlich\", C thiếu \"von\", D dùng \"südlich in\" sai cấu trúc.\n-> Đáp án: Can Tho liegt im Süden von Vietnam.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Can Tho liegt im Süden von Vietnam.",
                "translation": "Cần Thơ nằm ở miền Nam của Việt Nam."
            }
        },
        {
            "id": 4,
            "exercise_type": "trac_nghiem",
            "question": "Câu 4: Cụm \"im Nordwesten\" chỉ CÙNG HƯỚNG LA BÀN với tính từ nào sau đây?",
            "options": ["südwestlich", "nordöstlich", "nordwestlich", "südöstlich"],
            "correct_answer": "nordwestlich",
            "explanation": "Nord (Bắc) + Westen (Tây) = Tây Bắc.\nTính từ tương ứng chỉ hướng Tây Bắc là \"nordwestlich\"\n-> Đáp án: nordwestlich.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "im Nordwesten, nordwestlich",
                "translation": "Cùng hướng Tây Bắc: im Nordwesten (bên trong)\nnordwestlich (bên ngoài)."
            }
        },
        {
            "id": 5,
            "exercise_type": "trac_nghiem",
            "question": "Câu 5: Chọn mạo từ phủ định thích hợp:\n\"Ist das eine Brille?\" — \"Nein, das ist ___ Brille.\"",
            "options": ["kein", "keine", "eine", "nicht"],
            "correct_answer": "keine",
            "explanation": "\"die Brille\" là danh từ giống cái (die), phủ định danh từ giống cái ở Nominativ dùng \"keine\"\n-> Đáp án: keine.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Ist das eine Brille? Nein, das ist keine Brille.",
                "translation": "Đây có phải mắt kính không?\nKhông, đó không phải mắt kính."
            }
        },
        {
            "id": 6,
            "exercise_type": "trac_nghiem",
            "question": "Câu 6: Chọn cụm từ phù hợp để nói Đà Nẵng nằm ở miền Trung (giữa) của Việt Nam:\n\"Da Nang liegt ___ von Vietnam.\"",
            "options": ["im nordöstlich", "in der Mitte", "nördlich", "im westlich"],
            "correct_answer": "in der Mitte",
            "explanation": "Với phạm vi một nước/vùng, diễn đạt \"ở giữa / miền Trung của ...\" dùng cụm cố định \"in der Mitte von\"\n-> Đáp án: in der Mitte.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["in der Mitte", "im Zentrum"],
                "audio_text": "Da Nang liegt in der Mitte von Vietnam.",
                "translation": "Đà Nẵng nằm ở miền Trung của Việt Nam."
            }
        },
        {
            "id": 7,
            "exercise_type": "trac_nghiem",
            "question": "Câu 7: Chọn câu ĐÚNG mô tả vị trí giữa hai quốc gia riêng biệt (Trung Quốc nằm phía Bắc Việt Nam):",
            "options": [
                "China liegt im Norden von Vietnam.",
                "China liegt nördlich von Vietnam.",
                "China liegt im nördlich von Vietnam.",
                "China liegt Norden von Vietnam."
            ],
            "correct_answer": "China liegt nördlich von Vietnam.",
            "explanation": "Trung Quốc là quốc gia khác, nằm BÊN NGOÀI Việt Nam nên dùng tính từ \"nördlich von\" (không dùng \"im Norden von\").\n-> Đáp án: China liegt nördlich von Vietnam.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "China liegt nördlich von Vietnam.",
                "translation": "Trung Quốc nằm ở phía Bắc của Việt Nam."
            }
        },
        {
            "id": 8,
            "exercise_type": "trac_nghiem",
            "question": "Câu 8: Chọn mạo từ phủ định thích hợp (der Laptop):\n\"Das ist ___ Laptop, sondern ein Computer.\"",
            "options": ["keine", "nicht", "kein", "einen"],
            "correct_answer": "kein",
            "explanation": "\"der Laptop\" mang giống đực (der), phủ định danh từ giống đực ở Nominativ dùng \"kein\"\n-> Đáp án: kein.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Das ist kein Laptop, sondern ein Computer.",
                "translation": "Đó không phải máy tính xách tay, mà là máy vi tính."
            }
        },
        {
            "id": 9,
            "exercise_type": "trac_nghiem",
            "question": "Câu 9: Chọn dạng đúng của động từ \"sein\":\n\"___ das dein Rucksack?\" — \"Ja, danke!\"",
            "options": ["Sind", "Bist", "Ist", "Seid"],
            "correct_answer": "Ist",
            "explanation": "Chủ ngữ giả \"das\" đi với danh từ số ít \"dein Rucksack\" chia \"sein\" ở ngôi số ít thứ 3 là \"ist\"\n-> Đáp án: Ist.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Ist das dein Rucksack? Ja, danke!",
                "translation": "Đó có phải ba lô của bạn không?\nVâng, cảm ơn!"
            }
        },
        {
            "id": 10,
            "exercise_type": "trac_nghiem",
            "question": "Câu 10: Chọn dạng quá khứ (Präteritum) đúng của \"sein\":\n\"Gestern ___ wir im Konzert in Berlin.\"",
            "options": ["sind", "wart", "waren", "war"],
            "correct_answer": "waren",
            "explanation": "\"Gestern\" (hôm qua) chỉ quá khứ.\nNgôi \"wir\" chia quá khứ Präteritum của \"sein\" là \"waren\"\n-> Đáp án: waren.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Gestern waren wir im Konzert in Berlin.",
                "translation": "Hôm qua chúng tôi đã ở buổi hòa nhạc tại Berlin."
            }
        },
        {
            "id": 11,
            "exercise_type": "trac_nghiem",
            "question": "Câu 11: Chọn dạng quá khứ (Präteritum) đúng cho ngôi \"du\":\n\"___ du gestern Abend zu Hause?\"",
            "options": ["Warst", "Bist", "Wart", "Waren"],
            "correct_answer": "Warst",
            "explanation": "\"gestern Abend\" là tối hôm qua (Präteritum).\nNgôi \"du\" chia quá khứ của \"sein\" là \"warst\"\n-> Đáp án: Warst.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Warst du gestern Abend zu Hause?",
                "translation": "Tối hôm qua bạn có ở nhà không?"
            }
        },
        {
            "id": 12,
            "exercise_type": "trac_nghiem",
            "question": "Câu 12: Chọn cụm giới từ đúng với quốc gia \"die Türkei\":\n\"Mein Vater kommt ___ Türkei.\"",
            "options": ["aus", "in die", "aus der", "im"],
            "correct_answer": "aus der",
            "explanation": "\"die Türkei\" là quốc gia có mạo từ giống cái, khi đi với giới từ \"aus\" (+ Dativ) biến thành \"aus der Türkei\"\n-> Đáp án: aus der.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Mein Vater kommt aus der Türkei.",
                "translation": "Bố tôi đến từ Thổ Nhĩ Kỳ."
            }
        },
        {
            "id": 13,
            "exercise_type": "trac_nghiem",
            "question": "Câu 13: \"Welche Sprache spricht man in Ägypten?\"",
            "options": ["Ägyptisch", "Arabisch", "Türkisch", "Spanisch"],
            "correct_answer": "Arabisch",
            "explanation": "Tại Ai Cập (Ägypten) người dân nói tiếng Ả Rập (\"Arabisch\"), không dùng \"Ägyptisch\"\n-> Đáp án: Arabisch.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "In Ägypten spricht man Arabisch.",
                "translation": "Người ta nói ngôn ngữ nào ở Ai Cập?"
            }
        },
        {
            "id": 14,
            "exercise_type": "trac_nghiem",
            "question": "Câu 14: Chọn giới từ đúng với quốc gia \"die Schweiz\":\n\"Meine Eltern wohnen ___ Schweiz, in Zürich.\"",
            "options": ["in", "im", "in der", "aus der"],
            "correct_answer": "in der",
            "explanation": "\"die Schweiz\" có mạo từ giống cái\ntrả lời cho vị trí tĩnh \"Wo?\" dùng \"in + Dativ\"\n-> \"in der Schweiz\"\n-> Đáp án: in der.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Meine Eltern wohnen in der Schweiz, in Zürich.",
                "translation": "Bố mẹ tôi sống ở Thụy Sĩ, tại Zürich."
            }
        },
        {
            "id": 15,
            "exercise_type": "trac_nghiem",
            "question": "Câu 15: Chọn từ để hỏi phù hợp:\n\"___ spricht man in Griechenland?\" — \"Griechisch.\"",
            "options": ["Was für", "Wer", "Welche Sprache", "Woher"],
            "correct_answer": "Welche Sprache",
            "explanation": "Để hỏi \"người ta nói ngôn ngữ nào?\" dùng cụm \"Welche Sprache spricht man ...?\"\n-> Đáp án: Welche Sprache.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Welche Sprache spricht man in Griechenland? Griechisch.",
                "translation": "Ở Hy Lạp người ta nói tiếng gì?\nTiếng Hy Lạp."
            }
        },
        {
            "id": 16,
            "exercise_type": "dien_khuyet",
            "question": "Câu 16: Điền từ thích hợp:\n\"Hai Phong liegt im ___ von Vietnam.\" (hướng Đông Bắc)",
            "options": null,
            "correct_answer": "Nordosten",
            "explanation": "Sau \"im\" cần dùng danh từ viết hoa chỉ hướng (Hải Phòng thuộc miền Đông Bắc Việt Nam).\nĐông Bắc là \"Nordosten\"\n-> Đáp án: Nordosten.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Nordosten", "nordosten"],
                "audio_text": "Hai Phong liegt im Nordosten von Vietnam.",
                "translation": "Hải Phòng nằm ở miền Đông Bắc của Việt Nam."
            }
        },
        {
            "id": 17,
            "exercise_type": "dien_khuyet",
            "question": "Câu 17: Điền tính từ chỉ hướng:\n\"Polen liegt ___ von Deutschland.\" (phía Đông)",
            "options": null,
            "correct_answer": "östlich",
            "explanation": "Ba Lan nằm bên ngoài Đức, phía Đông khi dùng như tính từ (không có giới từ) là \"östlich\"\n-> Đáp án: östlich.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["östlich", "oestlich"],
                "audio_text": "Polen liegt östlich von Deutschland.",
                "translation": "Ba Lan nằm ở phía Đông của nước Đức."
            }
        },
        {
            "id": 18,
            "exercise_type": "dien_khuyet",
            "question": "Câu 18: Điền giới từ thích hợp:\n\"München liegt ___ Süden von Deutschland.\"",
            "options": null,
            "correct_answer": "im",
            "explanation": "München nằm bên trong nước Đức và \"Süden\" là danh từ viết hoa chỉ hướng, nên bắt buộc đi kèm giới từ \"im\"\n-> Đáp án: im.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["im", "Im"],
                "audio_text": "München liegt im Süden von Deutschland.",
                "translation": "München nằm ở miền Nam của nước Đức."
            }
        },
        {
            "id": 19,
            "exercise_type": "dien_khuyet",
            "question": "Câu 19: Điền mạo từ không xác định thích hợp (die Kamera):\n\"Das ist kein Radio, das ist ___ Kamera.\"",
            "options": null,
            "correct_answer": "eine",
            "explanation": "\"die Kamera\" là danh từ giống cái, mạo từ không xác định ở Nominativ là \"eine\"\n-> Đáp án: eine.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["eine", "Eine"],
                "audio_text": "Das ist kein Radio, das ist eine Kamera.",
                "translation": "Đó không phải là cái đài radio, đó là một chiếc máy ảnh."
            }
        },
        {
            "id": 20,
            "exercise_type": "dien_khuyet",
            "question": "Câu 20: Điền mạo từ phủ định thích hợp (der Schlüssel):\n\"Ist das ein Schlüssel?\" — \"Nein, das ist ___ Schlüssel.\"",
            "options": null,
            "correct_answer": "kein",
            "explanation": "\"der Schlüssel\" là danh từ giống đực, phủ định danh từ giống đực ở Nominativ dùng \"kein\"\n-> Đáp án: kein.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["kein", "Kein"],
                "audio_text": "Ist das ein Schlüssel? Nein, das ist kein Schlüssel.",
                "translation": "Đây có phải là chìa khóa không?\nKhông, đó không phải chìa khóa."
            }
        },
        {
            "id": 21,
            "exercise_type": "dien_khuyet",
            "question": "Câu 21: Điền danh từ chỉ hướng thích hợp:\n\"Dresden liegt im ___ von Deutschland.\" (hướng Đông)",
            "options": null,
            "correct_answer": "Osten",
            "explanation": "Dresden thuộc miền Đông nước Đức\nsau \"im\" dùng danh từ viết hoa chỉ hướng Đông là \"Osten\"\n-> Đáp án: Osten.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Osten", "osten"],
                "audio_text": "Dresden liegt im Osten von Deutschland.",
                "translation": "Dresden nằm ở miền Đông của nước Đức."
            }
        },
        {
            "id": 22,
            "exercise_type": "dien_khuyet",
            "question": "Câu 22: Điền tính từ chỉ hướng:\n\"Österreich liegt ___ von Deutschland.\" (phía Nam)",
            "options": null,
            "correct_answer": "südlich",
            "explanation": "Áo là quốc gia riêng nằm bên ngoài và ở phía Nam của Đức nên dùng tính từ \"südlich\" (không dùng \"im\").\n-> Đáp án: südlich.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["südlich", "suedlich"],
                "audio_text": "Österreich liegt südlich von Deutschland.",
                "translation": "Nước Áo nằm ở phía Nam của nước Đức."
            }
        },
        {
            "id": 23,
            "exercise_type": "dien_khuyet",
            "question": "Câu 23: Điền tên ngôn ngữ tiếng Đức thích hợp:\n\"Er kommt aus Ägypten. Seine Muttersprache ist ___.\" (tiếng Ả Rập)",
            "options": null,
            "correct_answer": "Arabisch",
            "explanation": "Tiếng mẹ đẻ ở Ai Cập là tiếng Ả Rập, danh từ tên ngôn ngữ luôn viết hoa: \"Arabisch\"\n-> Đáp án: Arabisch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Arabisch", "arabisch"],
                "audio_text": "Er kommt aus Ägypten. Seine Muttersprache ist Arabisch.",
                "translation": "Anh ấy đến từ Ai Cập.\nTiếng mẹ đẻ của anh ấy là tiếng Ả Rập."
            }
        },
        {
            "id": 24,
            "exercise_type": "dien_khuyet",
            "question": "Câu 24: Điền tên châu lục bằng tiếng Đức (không cần mạo từ):\n\"Deutschland und Frankreich liegen in ___.\" (châu Âu)",
            "options": null,
            "correct_answer": "Europa",
            "explanation": "Tên châu lục \"das Europa\" thường dùng không mạo từ sau giới từ \"in\"\n-> \"in Europa\"\n-> Đáp án: Europa.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Europa", "europa"],
                "audio_text": "Deutschland und Frankreich liegen in Europa.",
                "translation": "Đức và Pháp nằm ở châu Âu."
            }
        },
        {
            "id": 25,
            "exercise_type": "dien_khuyet",
            "question": "Câu 25: Điền mạo từ thích hợp sau giới từ \"in\" (quốc gia die Türkei):\n\"Meine Tante lebt seit zwei Jahren in ___ Türkei.\"",
            "options": null,
            "correct_answer": "der",
            "explanation": "Quốc gia giống cái \"die Türkei\" khi đứng sau \"in\" (vị trí tĩnh) chuyển sang Dativ thành \"in der Türkei\"\n-> Đáp án: der.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["der"],
                "audio_text": "Meine Tante lebt seit zwei Jahren in der Türkei.",
                "translation": "Cô/dì của tôi sống ở Thổ Nhĩ Kỳ đã hai năm rồi."
            }
        },
        {
            "id": 26,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 26: Chia động từ \"sein\":\n\"Früher ___ er sehr sportlich.\"",
            "options": null,
            "correct_answer": "war",
            "explanation": "\"Früher\" (trước đây) là dấu hiệu thì quá khứ Präteritum.\nNgôi \"er\" chia quá khứ của \"sein\" là \"war\"\n-> Đáp án: war.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["war"],
                "audio_text": "Früher war er sehr sportlich.",
                "translation": "Trước đây anh ấy rất đam mê thể thao."
            }
        },
        {
            "id": 27,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 27: Chia động từ \"sein\":\n\"Wo ___ ihr jetzt?\"",
            "options": null,
            "correct_answer": "seid",
            "explanation": "\"jetzt\" (bây giờ) là thì hiện tại (Präsens).\nNgôi \"ihr\" chia \"sein\" là \"seid\"\n-> Đáp án: seid.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["seid"],
                "audio_text": "Wo seid ihr jetzt?",
                "translation": "Bây giờ các bạn đang ở đâu?"
            }
        },
        {
            "id": 28,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 28: Chia động từ \"tragen\":\n\"Anna ___ gern ein blaues Kleid.\"",
            "options": null,
            "correct_answer": "trägt",
            "explanation": "Động từ bất quy tắc \"tragen\" (mặc) biến âm a -> ä ở ngôi er/sie/es (Anna) thành \"trägt\"\n-> Đáp án: trägt.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["trägt", "traegt"],
                "audio_text": "Anna trägt gern ein blaues Kleid.",
                "translation": "Anna thích mặc một chiếc đầm màu xanh dương."
            }
        },
        {
            "id": 29,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 29: Chia động từ \"sein\":\n\"Gestern ___ meine Eltern im Konzert.\"",
            "options": null,
            "correct_answer": "waren",
            "explanation": "\"Gestern\" là quá khứ, chủ ngữ \"meine Eltern\" (số nhiều) chia \"sein\" ở Präteritum là \"waren\"\n-> Đáp án: waren.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["waren"],
                "audio_text": "Gestern waren meine Eltern im Konzert.",
                "translation": "Hôm qua bố mẹ tôi đã ở buổi hòa nhạc."
            }
        },
        {
            "id": 30,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 30: Chia động từ \"sein\":\n\"Ich ___ letztes Jahr zum ersten Mal in Wien.\"",
            "options": null,
            "correct_answer": "war",
            "explanation": "\"letztes Jahr\" (năm ngoái) chỉ quá khứ.\nNgôi \"ich\" chia Präteritum của \"sein\" là \"war\"\n-> Đáp án: war.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["war"],
                "audio_text": "Ich war letztes Jahr zum ersten Mal in Wien.",
                "translation": "Năm ngoái tôi lần đầu tiên đến Viên."
            }
        },
        {
            "id": 31,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 31: Chia động từ \"sein\":\n\"Wann ___ du gestern zu Hause, Lisa?\"",
            "options": null,
            "correct_answer": "warst",
            "explanation": "\"gestern\" chỉ quá khứ, ngôi \"du\" chia Präteritum của \"sein\" là \"warst\"\n-> Đáp án: warst.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["warst"],
                "audio_text": "Wann warst du gestern zu Hause, Lisa?",
                "translation": "Hôm qua khi nào bạn ở nhà vậy, Lisa?"
            }
        },
        {
            "id": 32,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 32: Chia động từ \"lesen\":\n\"Mein Bruder ___ jeden Morgen die Zeitung.\"",
            "options": null,
            "correct_answer": "liest",
            "explanation": "Động từ bất quy tắc \"lesen\" (đọc) biến âm e -> ie ở ngôi er/sie/es (Mein Bruder) thành \"liest\"\n-> Đáp án: liest.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["liest"],
                "audio_text": "Mein Bruder liest jeden Morgen die Zeitung.",
                "translation": "Anh/em trai tôi mỗi sáng đều đọc báo."
            }
        },
        {
            "id": 33,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 33: Chia động từ \"sprechen\":\n\"Welche Sprachen ___ ihr zu Hause?\"",
            "options": null,
            "correct_answer": "sprecht",
            "explanation": "Ngôi \"ihr\" KHÔNG bao giờ biến âm ở các động từ bất quy tắc!\nGốc \"sprech-\" + đuôi \"-t\"\n-> Đáp án: sprecht.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["sprecht"],
                "audio_text": "Welche Sprachen sprecht ihr zu Hause?",
                "translation": "Ở nhà các bạn nói những ngôn ngữ nào?"
            }
        },
        {
            "id": 34,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 34: Chia động từ \"fahren\":\n\"Der Zug ___ direkt nach Hamburg.\"",
            "options": null,
            "correct_answer": "fährt",
            "explanation": "Động từ bất quy tắc \"fahren\" (chạy/lái) biến âm a -> ä ở ngôi er/sie/es (Der Zug) thành \"fährt\"\n-> Đáp án: fährt.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["fährt", "faehrt"],
                "audio_text": "Der Zug fährt direkt nach Hamburg.",
                "translation": "Chuyến tàu chạy thẳng tới Hamburg."
            }
        },
        {
            "id": 35,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 35: Chia động từ \"schlafen\":\n\"Das Kind ___ am Sonntag bis neun Uhr.\"",
            "options": null,
            "correct_answer": "schläft",
            "explanation": "Động từ bất quy tắc \"schlafen\" (ngủ) biến âm a -> ä ở ngôi er/sie/es (Das Kind) thành \"schläft\"\n-> Đáp án: schläft.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["schläft", "schlaeft"],
                "audio_text": "Das Kind schläft am Sonntag bis neun Uhr.",
                "translation": "Đứa trẻ ngủ đến chín giờ vào ngày Chủ nhật."
            }
        },
        {
            "id": 36,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 36: Dịch sang tiếng Đức (kèm mạo từ số ít):\n\"áo khoác mùa đông\"",
            "options": null,
            "correct_answer": "der Wintermantel",
            "explanation": "\"áo khoác mùa đông\" là danh từ giống đực ghép từ der Winter + der Mantel.\n-> Đáp án: der Wintermantel.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["der Wintermantel", "Wintermantel"],
                "audio_text": "der Wintermantel",
                "translation": "áo khoác mùa đông"
            }
        },
        {
            "id": 37,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 37: Dịch sang tiếng Đức (kèm mạo từ số ít):\n\"sương mù\"",
            "options": null,
            "correct_answer": "der Nebel",
            "explanation": "\"sương mù\" trong tiếng Đức mang giống đực \"der\"\n-> Đáp án: der Nebel.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["der Nebel", "Nebel"],
                "audio_text": "der Nebel",
                "translation": "sương mù"
            }
        },
        {
            "id": 38,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 38: Dịch sang tiếng Đức (kèm mạo từ số ít):\n\"máy tính xách tay\"",
            "options": null,
            "correct_answer": "der Laptop",
            "explanation": "\"máy tính xách tay\" trong tiếng Đức là danh từ giống đực \"der\"\n-> Đáp án: der Laptop.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["der Laptop", "Laptop"],
                "audio_text": "der Laptop",
                "translation": "máy tính xách tay"
            }
        },
        {
            "id": 39,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 39: Dịch sang tiếng Đức (kèm mạo từ số ít):\n\"chìa khóa\"",
            "options": null,
            "correct_answer": "der Schlüssel",
            "explanation": "\"chìa khóa\" là danh từ giống đực \"der\"\n-> Đáp án: der Schlüssel.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["der Schlüssel", "Schlüssel", "der Schluessel", "Schluessel"],
                "audio_text": "der Schlüssel",
                "translation": "chìa khóa"
            }
        },
        {
            "id": 40,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 40: Dịch sang tiếng Đức (kèm mạo từ số ít):\n\"tiếng mẹ đẻ\"",
            "options": null,
            "correct_answer": "die Muttersprache",
            "explanation": "\"tiếng mẹ đẻ\" là danh từ ghép mang giống của \"die Sprache\" (giống cái).\n-> Đáp án: die Muttersprache.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["die Muttersprache", "Muttersprache"],
                "audio_text": "die Muttersprache",
                "translation": "tiếng mẹ đẻ"
            }
        },
        {
            "id": 41,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 41: Dịch sang tiếng Việt:\n\"die Krawatte\"",
            "options": null,
            "correct_answer": "cà vạt",
            "explanation": "\"die Krawatte\" có nghĩa là chiếc cà vạt.\n-> Đáp án: cà vạt.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["cà vạt", "cái cà vạt", "chiếc cà vạt"],
                "audio_text": "die Krawatte",
                "translation": "cà vạt"
            }
        },
        {
            "id": 42,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 42: Dịch sang tiếng Việt:\n\"Es ist neblig.\"",
            "options": null,
            "correct_answer": "Trời có sương mù.",
            "explanation": "Tính từ \"neblig\" (từ \"der Nebel\") mang nghĩa có sương mù.\n-> Đáp án: Trời có sương mù.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Trời có sương mù.", "Trời có sương mù", "Có sương mù", "Trời sương mù"],
                "audio_text": "Es ist neblig.",
                "translation": "Trời có sương mù."
            }
        },
        {
            "id": 43,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 43: Dịch sang tiếng Việt:\n\"der Rucksack\"",
            "options": null,
            "correct_answer": "ba lô",
            "explanation": "\"der Rucksack\" là chiếc ba lô đeo lưng.\n-> Đáp án: ba lô.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["ba lô", "balo", "cái ba lô", "chiếc ba lô"],
                "audio_text": "der Rucksack",
                "translation": "ba lô"
            }
        },
        {
            "id": 44,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 44: Dịch sang tiếng Việt:\n\"die Kamera\"",
            "options": null,
            "correct_answer": "máy ảnh",
            "explanation": "\"die Kamera\" có nghĩa là máy ảnh / máy chụp hình.\n-> Đáp án: máy ảnh.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["máy ảnh", "chiếc máy ảnh", "cái máy ảnh", "máy chụp ảnh", "máy chụp hình"],
                "audio_text": "die Kamera",
                "translation": "máy ảnh"
            }
        },
        {
            "id": 45,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 45: Dịch sang tiếng Việt:\n\"das Konzert\"",
            "options": null,
            "correct_answer": "buổi hòa nhạc",
            "explanation": "\"das Konzert\" có nghĩa là buổi hòa nhạc.\n-> Đáp án: buổi hòa nhạc.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["buổi hòa nhạc", "hòa nhạc"],
                "audio_text": "das Konzert",
                "translation": "buổi hòa nhạc"
            }
        },
        {
            "id": 46,
            "exercise_type": "noi_o",
            "question": "Câu 46 (Bài nối 1): Ghép Quốc gia với Ngôn ngữ tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Quy tắc tạo tên ngôn ngữ thường thêm đuôi -sch hoặc -isch vào gốc tên quốc gia (Deutschland - Deutsch, Frankreich - Französisch, Polen - Polnisch, Italien - Italienisch).\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Deutschland", "right": "Deutsch"},
                    {"left": "Frankreich", "right": "Französisch"},
                    {"left": "Polen", "right": "Polnisch"},
                    {"left": "Italien", "right": "Italienisch"}
                ],
                "audio_text": "Deutschland, Deutsch. Frankreich, Französisch. Polen, Polnisch. Italien, Italienisch.",
                "translation": "Đức - Tiếng Đức\nPháp - Tiếng Pháp\nBa Lan - Tiếng Ba Lan\nÝ - Tiếng Ý"
            }
        },
        {
            "id": 47,
            "exercise_type": "noi_o",
            "question": "Câu 47 (Bài nối 2): Ghép từ vựng quần áo tiếng Đức với nghĩa tiếng Việt:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Nhận diện từ vựng trang phục A1: der Stiefel (bốt), der Mantel (áo măng tô), der Pullover (áo len), der Rock (chân váy).\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "der Stiefel", "right": "bốt"},
                    {"left": "der Mantel", "right": "áo măng tô"},
                    {"left": "der Pullover", "right": "áo len"},
                    {"left": "der Rock", "right": "chân váy"}
                ],
                "audio_text": "der Stiefel. der Mantel. der Pullover. der Rock.",
                "translation": "der Stiefel: bốt\nder Mantel: áo măng tô\nder Pullover: áo len\nder Rock: chân váy"
            }
        },
        {
            "id": 48,
            "exercise_type": "noi_o",
            "question": "Câu 48 (Bài nối 3): Ghép Quốc gia với Ngôn ngữ (lưu ý ngoại lệ Ägypten):",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Ai Cập (Ägypten) nói tiếng Ả Rập (Arabisch), Tây Ban Nha.\n-> Spanisch, Nhật Bản.\n-> Japanisch, Nga.\n-> Russisch.\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Ägypten", "right": "Arabisch"},
                    {"left": "Spanien", "right": "Spanisch"},
                    {"left": "Japan", "right": "Japanisch"},
                    {"left": "Russland", "right": "Russisch"}
                ],
                "audio_text": "Ägypten, Arabisch. Spanien, Spanisch. Japan, Japanisch. Russland, Russisch.",
                "translation": "Ai Cập - Tiếng Ả Rập\nTây Ban Nha - Tiếng Tây Ban Nha\nNhật Bản - Tiếng Nhật\nNga - Tiếng Nga"
            }
        },
        {
            "id": 49,
            "exercise_type": "noi_o",
            "question": "Câu 49 (Bài nối 4): Ghép cụm phương hướng bên trong (im + Danh từ) với nghĩa tiếng Việt:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Bốn hướng chính dùng danh từ viết hoa sau \"im\": im Norden (Bắc), im Süden (Nam), im Osten (Đông), im Westen (Tây).\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "im Norden", "right": "ở miền Bắc"},
                    {"left": "im Süden", "right": "ở miền Nam"},
                    {"left": "im Osten", "right": "ở miền Đông"},
                    {"left": "im Westen", "right": "ở miền Tây"}
                ],
                "audio_text": "im Norden. im Süden. im Osten. im Westen.",
                "translation": "im Norden: ở miền Bắc\nim Süden: ở miền Nam\nim Osten: ở miền Đông\nim Westen: ở miền Tây"
            }
        },
        {
            "id": 50,
            "exercise_type": "noi_o",
            "question": "Câu 50 (Bài nối 5): Ghép tính từ chỉ hướng bên ngoài (-lich von) với nghĩa tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Tính từ chỉ hướng không đi với \"im\": nordöstlich (Đông Bắc), südöstlich (Đông Nam), südwestlich (Tây Nam), nordwestlich (Tây Bắc).\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "nordöstlich von", "right": "phía Đông Bắc của"},
                    {"left": "südöstlich von", "right": "phía Đông Nam của"},
                    {"left": "südwestlich von", "right": "phía Tây Nam của"},
                    {"left": "nordwestlich von", "right": "phía Tây Bắc của"}
                ],
                "audio_text": "nordöstlich von. südöstlich von. südwestlich von. nordwestlich von.",
                "translation": "nordöstlich von: phía Đông Bắc của\nsüdöstlich von: phía Đông Nam của\nsüdwestlich von: phía Tây Nam của\nnordwestlich von: phía Tây Bắc của"
            }
        },
        {
            "id": 51,
            "exercise_type": "noi_o",
            "question": "Câu 51 (Bài nối 6): Ghép đại từ nhân xưng với dạng quá khứ (Präteritum) của động từ \"sein\":",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Chia động từ \"sein\" ở thì quá khứ Präteritum: ich war, du warst, wir waren, ihr wart.\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "war"},
                    {"left": "du", "right": "warst"},
                    {"left": "wir", "right": "waren"},
                    {"left": "ihr", "right": "wart"}
                ],
                "audio_text": "ich war. du warst. wir waren. ihr wart.",
                "translation": "ich war: tôi đã\ndu warst: bạn đã\nwir waren: chúng tôi đã\nihr wart: các bạn đã"
            }
        },
        {
            "id": 52,
            "exercise_type": "noi_o",
            "question": "Câu 52 (Bài nối 7): Ghép đại từ nhân xưng với dạng hiện tại (Präsens) của động từ \"sein\":",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Chia động từ \"sein\" ở thì hiện tại Präsens: ich bin, du bist, er ist, ihr seid.\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "ich", "right": "bin"},
                    {"left": "du", "right": "bist"},
                    {"left": "er", "right": "ist"},
                    {"left": "ihr", "right": "seid"}
                ],
                "audio_text": "ich bin. du bist. er ist. ihr seid.",
                "translation": "ich bin: tôi là\ndu bist: bạn là\ner ist: anh ấy là\nihr seid: các bạn là"
            }
        },
        {
            "id": 53,
            "exercise_type": "noi_o",
            "question": "Câu 53 (Bài nối 8): Ghép tên quốc gia với cụm chỉ vị trí \"ở tại ...\" (Wo?) tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Quốc gia không mạo từ dùng \"in + Tên nước\" (in Deutschland)\ncó mạo từ giống cái dùng \"in der ...\" (in der Schweiz / Türkei)\nsố nhiều dùng \"in den USA\"\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "die Schweiz", "right": "in der Schweiz"},
                    {"left": "die Türkei", "right": "in der Türkei"},
                    {"left": "die USA (Plural)", "right": "in den USA"},
                    {"left": "Deutschland", "right": "in Deutschland"}
                ],
                "audio_text": "die Schweiz, in der Schweiz. die Türkei, in der Türkei. die USA, in den USA. Deutschland, in Deutschland.",
                "translation": "Thụy Sĩ -> ở Thụy Sĩ\nThổ Nhĩ Kỳ -> ở Thổ Nhĩ Kỳ\nMỹ -> ở Mỹ\nĐức -> ở Đức"
            }
        },
        {
            "id": 54,
            "exercise_type": "noi_o",
            "question": "Câu 54 (Bài nối 9): Ghép tình huống thời tiết với đồ dùng/trang phục phù hợp:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Trời mưa (Es regnet) cần ô (der Regenschirm)\ntrời tuyết (Es schneit) cần áo khoác mùa đông\ntrời nắng (sonnig) cần kính râm\ntrời lạnh (kalt) cần khăn quàng.\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Es regnet.", "right": "der Regenschirm"},
                    {"left": "Es schneit.", "right": "der Wintermantel"},
                    {"left": "Es ist sonnig.", "right": "die Sonnenbrille"},
                    {"left": "Es ist kalt.", "right": "der Schal"}
                ],
                "audio_text": "Es regnet, der Regenschirm. Es schneit, der Wintermantel. Es ist sonnig, die Sonnenbrille. Es ist kalt, der Schal.",
                "translation": "Trời mưa -> ô dù\nCó tuyết -> áo khoác mùa đông\nTrời nắng -> kính râm\nTrời lạnh -> khăn quàng"
            }
        },
        {
            "id": 55,
            "exercise_type": "noi_o",
            "question": "Câu 55 (Bài nối 10): Ghép danh từ mới của Bài 14 với nghĩa tiếng Việt tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Ôn tập từ vựng Bài 14: das Zentrum (trung tâm thành phố), die Freundin (bạn nữ; bạn gái), der Arzt (bác sĩ), das Kind (đứa trẻ; con).\n-> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "das Zentrum", "right": "trung tâm (thành phố)"},
                    {"left": "die Freundin", "right": "bạn (nữ); bạn gái"},
                    {"left": "der Arzt", "right": "bác sĩ"},
                    {"left": "das Kind", "right": "đứa trẻ; con"}
                ],
                "audio_text": "das Zentrum. die Freundin. der Arzt. das Kind.",
                "translation": "das Zentrum: trung tâm (thành phố)\ndie Freundin: bạn (nữ); bạn gái\nder Arzt: bác sĩ\ndas Kind: đứa trẻ; con"
            }
        },
        {
            "id": 56,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 56: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n\"München liegt [1] [2] von Deutschland.\" (miền Nam)",
            "options": null,
            "correct_answer": "im / Süden",
            "explanation": "Có 2 ô trống và München nằm bên trong nước Đức nên dùng cấu trúc danh từ \"im Süden\"\n-> Đáp án: im / Süden.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "München liegt [1] [2] von Deutschland.",
                "accepted_answers": ["im / Süden", "im/Süden", "im Süden", "im / Sueden", "im/Sueden"],
                "audio_text": "München liegt im Süden von Deutschland.",
                "translation": "München nằm ở miền Nam của nước Đức."
            }
        },
        {
            "id": 57,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 57: Điền 2 mạo từ thích hợp vào [1] và [2] (cách nhau bởi dấu /):\n\"Das ist [1] Kuli. [2] Kuli ist blau.\" (một / cây bút đó - xác định)",
            "options": null,
            "correct_answer": "ein / Der",
            "explanation": "\"der Kuli\" giống đực: lần đầu nhắc đến dùng mạo từ không xác định \"ein\"\nlần sau đã xác định dùng \"Der\" (đầu câu viết hoa).\n-> Đáp án: ein / Der.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Das ist [1] Kuli. [2] Kuli ist blau.",
                "accepted_answers": ["ein / Der", "ein/Der", "ein Der"],
                "audio_text": "Das ist ein Kuli. Der Kuli ist blau.",
                "translation": "Đây là một cây bút bi.\nCây bút bi đó màu xanh dương."
            }
        },
        {
            "id": 58,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 58: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n\"Hue liegt [1] [2] Mitte von Vietnam.\" (ở phần giữa của đất nước)",
            "options": null,
            "correct_answer": "in / der",
            "explanation": "Cụm cố định chỉ vùng giữa của một quốc gia là \"in der Mitte von ...\"\n-> Đáp án: in / der.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Hue liegt [1] [2] Mitte von Vietnam.",
                "accepted_answers": ["in / der", "in/der", "in der"],
                "audio_text": "Hue liegt in der Mitte von Vietnam.",
                "translation": "Huế nằm ở miền Trung của Việt Nam."
            }
        },
        {
            "id": 59,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 59: Điền 2 mạo từ thích hợp vào [1] và [2] (cách nhau bởi dấu /):\n\"Das ist [1] Kamera. [2] Kamera ist neu.\" (một / chiếc máy ảnh đó)",
            "options": null,
            "correct_answer": "eine / Die",
            "explanation": "\"die Kamera\" giống cái: lần đầu dùng \"eine\"\ncâu sau đã xác định và ở đầu câu nên dùng \"Die\"\n-> Đáp án: eine / Die.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Das ist [1] Kamera. [2] Kamera ist neu.",
                "accepted_answers": ["eine / Die", "eine/Die", "eine Die"],
                "audio_text": "Das ist eine Kamera. Die Kamera ist neu.",
                "translation": "Đây là một chiếc máy ảnh.\nChiếc máy ảnh đó mới."
            }
        },
        {
            "id": 60,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 60: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n\"Mein Freund kommt [1] [2] Türkei.\" (từ nước Thổ Nhĩ Kỳ)",
            "options": null,
            "correct_answer": "aus / der",
            "explanation": "Quốc gia giống cái \"die Türkei\" đi với \"kommen aus\" chuyển thành \"aus der Türkei\"\n-> Đáp án: aus / der.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Mein Freund kommt [1] [2] Türkei.",
                "accepted_answers": ["aus / der", "aus/der", "aus der"],
                "audio_text": "Mein Freund kommt aus der Türkei.",
                "translation": "Bạn tôi đến từ Thổ Nhĩ Kỳ."
            }
        },
        {
            "id": 61,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 61: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n\"Meine Schwester wohnt [1] [2] Schweiz.\" (ở Thụy Sĩ)",
            "options": null,
            "correct_answer": "in / der",
            "explanation": "Quốc gia giống cái \"die Schweiz\" đi với \"wohnen in\" (vị trí tĩnh) chuyển sang Dativ thành \"in der Schweiz\"\n-> Đáp án: in / der.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Meine Schwester wohnt [1] [2] Schweiz.",
                "accepted_answers": ["in / der", "in/der", "in der"],
                "audio_text": "Meine Schwester wohnt in der Schweiz.",
                "translation": "Chị/em gái tôi sống ở Thụy Sĩ."
            }
        },
        {
            "id": 62,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 62: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n\"Bremen liegt [1] [2] von Deutschland.\" (miền Tây Bắc)",
            "options": null,
            "correct_answer": "im / Nordwesten",
            "explanation": "Bremen thuộc miền Tây Bắc nước Đức nên dùng \"im Nordwesten\" (viết hoa danh từ hướng).\n-> Đáp án: im / Nordwesten.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Bremen liegt [1] [2] von Deutschland.",
                "accepted_answers": ["im / Nordwesten", "im/Nordwesten", "im Nordwesten"],
                "audio_text": "Bremen liegt im Nordwesten von Deutschland.",
                "translation": "Bremen nằm ở miền Tây Bắc của nước Đức."
            }
        },
        {
            "id": 63,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 63: Điền 2 mạo từ thích hợp vào [1] và [2] (cách nhau bởi dấu /):\n\"Das ist [1] Laptop, sondern [2] Computer.\" (không phải / một)",
            "options": null,
            "correct_answer": "kein / ein",
            "explanation": "\"der Laptop\" và \"der Computer\" đều mang giống đực \"der\" ở Nominativ: phủ định dùng \"kein\", khẳng định dùng \"ein\"\n-> Đáp án: kein / ein.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Das ist [1] Laptop, sondern [2] Computer.",
                "accepted_answers": ["kein / ein", "kein/ein", "kein ein"],
                "audio_text": "Das ist kein Laptop, sondern ein Computer.",
                "translation": "Đó không phải là một chiếc laptop, mà là một máy vi tính."
            }
        },
        {
            "id": 64,
            "exercise_type": "nghe_dien",
            "question": "Câu 64: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Wo waren Sie gestern, Herr Müller?",
            "explanation": "Luyện nghe câu hỏi quá khứ lịch sự với ngôi \"Sie\": \"Wo waren Sie gestern, Herr Müller?\"\n-> Đáp án: Wo waren Sie gestern, Herr Müller?",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Wo waren Sie gestern, Herr Müller?",
                "accepted_answers": [
                    "Wo waren Sie gestern, Herr Müller?",
                    "Wo waren Sie gestern Herr Müller?",
                    "Wo waren Sie gestern, Herr Mueller?",
                    "Wo waren Sie gestern, Herr Müller"
                ],
                "audio_text": "Wo waren Sie gestern, Herr Müller?",
                "translation": "Hôm qua ngài ở đâu, ngài Müller?"
            }
        },
        {
            "id": 65,
            "exercise_type": "nghe_dien",
            "question": "Câu 65: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Paris liegt westlich von Deutschland.",
            "explanation": "Luyện nghe cấu trúc phương hướng bên ngoài dùng tính từ \"westlich\": \"Paris liegt westlich von Deutschland.\"\n-> Đáp án: Paris liegt westlich von Deutschland.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Paris liegt westlich von Deutschland.",
                "accepted_answers": ["Paris liegt westlich von Deutschland.", "Paris liegt westlich von Deutschland"],
                "audio_text": "Paris liegt westlich von Deutschland.",
                "translation": "Paris nằm ở phía Tây của nước Đức."
            }
        },
        {
            "id": 66,
            "exercise_type": "nghe_dien",
            "question": "Câu 66: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Hanoi liegt im Norden von Vietnam.",
            "explanation": "Câu mẫu phương hướng bên trong: \"Hanoi liegt im Norden von Vietnam.\"\n-> Đáp án: Hanoi liegt im Norden von Vietnam.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Hanoi liegt im Norden von Vietnam.",
                "accepted_answers": ["Hanoi liegt im Norden von Vietnam.", "Hanoi liegt im Norden von Vietnam"],
                "audio_text": "Hanoi liegt im Norden von Vietnam.",
                "translation": "Hà Nội nằm ở miền Bắc của Việt Nam."
            }
        },
        {
            "id": 67,
            "exercise_type": "nghe_dien",
            "question": "Câu 67: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Früher war mein Vater Arzt in Leipzig.",
            "explanation": "Ôn tập thì quá khứ của \"sein\" (war) và nghề nghiệp không mạo từ: \"Früher war mein Vater Arzt in Leipzig.\"\n-> Đáp án: Früher war mein Vater Arzt in Leipzig.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Früher war mein Vater Arzt in Leipzig.",
                "accepted_answers": [
                    "Früher war mein Vater Arzt in Leipzig.",
                    "Früher war mein Vater Arzt in Leipzig",
                    "Frueher war mein Vater Arzt in Leipzig."
                ],
                "audio_text": "Früher war mein Vater Arzt in Leipzig.",
                "translation": "Trước đây bố tôi từng là bác sĩ ở Leipzig."
            }
        },
        {
            "id": 68,
            "exercise_type": "nghe_dien",
            "question": "Câu 68: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Das Hotel liegt im Zentrum von Hanoi.",
            "explanation": "Phân biệt \"im Zentrum\" (trung tâm thành phố): \"Das Hotel liegt im Zentrum von Hanoi.\"\n-> Đáp án: Das Hotel liegt im Zentrum von Hanoi.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Das Hotel liegt im Zentrum von Hanoi.",
                "accepted_answers": ["Das Hotel liegt im Zentrum von Hanoi.", "Das Hotel liegt im Zentrum von Hanoi"],
                "audio_text": "Das Hotel liegt im Zentrum von Hanoi.",
                "translation": "Khách sạn nằm ở trung tâm Hà Nội."
            }
        },
        {
            "id": 69,
            "exercise_type": "nghe_dien",
            "question": "Câu 69: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Früher waren wir Studenten, jetzt sind wir Lehrer.",
            "explanation": "Đối chiếu quá khứ \"waren\" và hiện tại \"sind\" cho ngôi \"wir\": \"Früher waren wir Studenten, jetzt sind wir Lehrer.\"\n-> Đáp án: Früher waren wir Studenten, jetzt sind wir Lehrer.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Früher waren wir Studenten, jetzt sind wir Lehrer.",
                "accepted_answers": [
                    "Früher waren wir Studenten, jetzt sind wir Lehrer.",
                    "Früher waren wir Studenten jetzt sind wir Lehrer.",
                    "Frueher waren wir Studenten, jetzt sind wir Lehrer.",
                    "Früher waren wir Studenten, jetzt sind wir Lehrer"
                ],
                "audio_text": "Früher waren wir Studenten, jetzt sind wir Lehrer.",
                "translation": "Trước đây chúng tôi là sinh viên, bây giờ chúng tôi là giáo viên."
            }
        },
        {
            "id": 70,
            "exercise_type": "nghe_dien",
            "question": "Câu 70: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Seine Muttersprache ist Arabisch.",
            "explanation": "Nghe từ vựng \"die Muttersprache\" và ngôn ngữ \"Arabisch\": \"Seine Muttersprache ist Arabisch.\"\n-> Đáp án: Seine Muttersprache ist Arabisch.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Seine Muttersprache ist Arabisch.",
                "accepted_answers": ["Seine Muttersprache ist Arabisch.", "Seine Muttersprache ist Arabisch"],
                "audio_text": "Seine Muttersprache ist Arabisch.",
                "translation": "Tiếng mẹ đẻ của anh ấy là tiếng Ả Rập."
            }
        },
        {
            "id": 71,
            "exercise_type": "nghe_dien",
            "question": "Câu 71: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Griechenland liegt im Südosten von Europa.",
            "explanation": "Nghe câu hướng kép Đông Nam (\"im Südosten\") trong châu Âu (\"von Europa\"): \"Griechenland liegt im Südosten von Europa.\"\n-> Đáp án: Griechenland liegt im Südosten von Europa.",
            "exp_reward": 15,
            "extra_data": {
                "dictation_mode": true,
                "full_sentence": "Griechenland liegt im Südosten von Europa.",
                "accepted_answers": [
                    "Griechenland liegt im Südosten von Europa.",
                    "Griechenland liegt im Südosten von Europa",
                    "Griechenland liegt im Suedosten von Europa."
                ],
                "audio_text": "Griechenland liegt im Südosten von Europa.",
                "translation": "Hy Lạp nằm ở miền Đông Nam của châu Âu."
            }
        },
        {
            "id": 72,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 72: Dịch câu sau sang tiếng Đức (dùng tính từ hướng):\n\"Nước Áo nằm ở phía Nam của nước Đức.\"",
            "options": null,
            "correct_answer": "Österreich liegt südlich von Deutschland.",
            "explanation": "Nước Áo nằm BÊN NGOÀI Đức nên dùng tính từ \"südlich\" (tuyệt đối không dùng \"im\").\n-> Đáp án: Österreich liegt südlich von Deutschland.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Österreich liegt südlich von Deutschland.",
                    "Österreich liegt südlich von Deutschland",
                    "Oesterreich liegt suedlich von Deutschland."
                ],
                "audio_text": "Österreich liegt südlich von Deutschland.",
                "translation": "Nước Áo nằm ở phía Nam của nước Đức."
            }
        },
        {
            "id": 73,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 73: Dịch câu sau sang tiếng Đức (dùng danh từ hướng):\n\"Tây Ban Nha nằm ở miền Tây Nam của Châu Âu.\"",
            "options": null,
            "correct_answer": "Spanien liegt im Südwesten von Europa.",
            "explanation": "Tây Ban Nha thuộc Châu Âu, miền Tây Nam (danh từ) là \"Südwesten\" đi kèm giới từ \"im\"\n-> Đáp án: Spanien liegt im Südwesten von Europa.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Spanien liegt im Südwesten von Europa.",
                    "Spanien liegt im Südwesten von Europa",
                    "Spanien liegt im Suedwesten von Europa."
                ],
                "audio_text": "Spanien liegt im Südwesten von Europa.",
                "translation": "Tây Ban Nha nằm ở miền Tây Nam của châu Âu."
            }
        },
        {
            "id": 74,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 74: Dịch câu sau sang tiếng Đức:\n\"Đà Nẵng nằm ở miền Trung (giữa) của Việt Nam.\"",
            "options": null,
            "correct_answer": "Da Nang liegt in der Mitte von Vietnam.",
            "explanation": "Vùng giữa của một quốc gia dùng cụm \"in der Mitte von\"\n-> Đáp án: Da Nang liegt in der Mitte von Vietnam.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Da Nang liegt in der Mitte von Vietnam.",
                    "Da Nang liegt in der Mitte von Vietnam",
                    "Da Nang liegt im Zentrum von Vietnam.",
                    "Da Nang liegt im Zentrum von Vietnam"
                ],
                "audio_text": "Da Nang liegt in der Mitte von Vietnam.",
                "translation": "Đà Nẵng nằm ở miền Trung của Việt Nam."
            }
        },
        {
            "id": 75,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 75: Dịch câu sau sang tiếng Đức (ngôi du):\n\"Hôm qua bạn có ở nhà không?\"",
            "options": null,
            "correct_answer": "Warst du gestern zu Hause?",
            "explanation": "Đặt câu hỏi Yes/No thì quá khứ với \"sein\" ở ngôi \"du\" là \"Warst du ...?\"\n-> Đáp án: Warst du gestern zu Hause?",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Warst du gestern zu Hause?",
                    "Warst du gestern zu Hause",
                    "Warst du gestern zuhause?",
                    "Warst du gestern daheim?"
                ],
                "audio_text": "Warst du gestern zu Hause?",
                "translation": "Hôm qua bạn có ở nhà không?"
            }
        },
        {
            "id": 76,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 76: Dịch câu sau sang tiếng Đức:\n\"Hôm qua chúng tôi ở Berlin.\"",
            "options": null,
            "correct_answer": "Wir waren gestern in Berlin.",
            "explanation": "Chủ ngữ \"wir\" chia quá khứ của \"sein\" là \"waren\"\n-> Đáp án: Wir waren gestern in Berlin.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Wir waren gestern in Berlin.",
                    "Wir waren gestern in Berlin",
                    "Gestern waren wir in Berlin.",
                    "Gestern waren wir in Berlin"
                ],
                "audio_text": "Wir waren gestern in Berlin.",
                "translation": "Hôm qua chúng tôi ở Berlin."
            }
        },
        {
            "id": 77,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 77: Dịch câu sau sang tiếng Đức (lưu ý mạo từ phủ định):\n\"Đây không phải là một chiếc ba lô, đây là một cái túi.\" (die Tasche)",
            "options": null,
            "correct_answer": "Das ist kein Rucksack, das ist eine Tasche.",
            "explanation": "\"der Rucksack\" giống đực -> phủ định là \"kein\"\n\"die Tasche\" giống cái.\n-> khẳng định là \"eine\"\n-> Đáp án: Das ist kein Rucksack, das ist eine Tasche.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Das ist kein Rucksack, das ist eine Tasche.",
                    "Das ist kein Rucksack, sondern eine Tasche.",
                    "Das ist kein Rucksack, das ist eine Tasche"
                ],
                "audio_text": "Das ist kein Rucksack, das ist eine Tasche.",
                "translation": "Đây không phải là một chiếc ba lô, đây là một cái túi."
            }
        },
        {
            "id": 78,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 78: Dịch câu sau sang tiếng Đức:\n\"Cô ấy đến từ Thụy Sĩ và nói tiếng Pháp.\"",
            "options": null,
            "correct_answer": "Sie kommt aus der Schweiz und spricht Französisch.",
            "explanation": "\"die Schweiz\" đi với \"aus\" biến thành \"aus der Schweiz\"\nđộng từ \"sprechen\" ngôi \"sie\" biến âm thành \"spricht\"\n-> Đáp án: Sie kommt aus der Schweiz und spricht Französisch.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Sie kommt aus der Schweiz und spricht Französisch.",
                    "Sie kommt aus der Schweiz und spricht Französisch",
                    "Sie kommt aus der Schweiz und spricht Franzoesisch."
                ],
                "audio_text": "Sie kommt aus der Schweiz und spricht Französisch.",
                "translation": "Cô ấy đến từ Thụy Sĩ và nói tiếng Pháp."
            }
        },
        {
            "id": 79,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 79: Dịch câu sau sang tiếng Đức:\n\"Buổi hòa nhạc tối qua rất tuyệt vời!\"",
            "options": null,
            "correct_answer": "Das Konzert gestern Abend war fantastisch!",
            "explanation": "\"das Konzert\" là chủ ngữ số ít ở quá khứ nên dùng \"war\"\n-> Đáp án: Das Konzert gestern Abend war fantastisch!",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Das Konzert gestern Abend war fantastisch!",
                    "Das Konzert gestern Abend war fantastisch.",
                    "Das Konzert gestern Abend war fantastisch",
                    "Das Konzert gestern Abend war sehr gut!",
                    "Das Konzert gestern Abend war super!",
                    "Das Konzert gestern Abend war toll!"
                ],
                "audio_text": "Das Konzert gestern Abend war fantastisch!",
                "translation": "Buổi hòa nhạc tối qua rất tuyệt vời!"
            }
        },
        {
            "id": 80,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 80: Dịch câu sau sang tiếng Việt:\n\"Russland liegt im Osten von Europa.\"",
            "options": null,
            "correct_answer": "Nga nằm ở miền Đông của châu Âu.",
            "explanation": "\"Russland\" = Nga, \"im Osten von Europa\" = ở miền Đông của châu Âu.\n-> Đáp án: Nga nằm ở miền Đông của châu Âu.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Nga nằm ở miền Đông của châu Âu.",
                    "Nga nằm ở miền Đông của châu Âu",
                    "Nước Nga nằm ở miền Đông của châu Âu.",
                    "Nga nằm ở phía Đông châu Âu."
                ],
                "audio_text": "Russland liegt im Osten von Europa.",
                "translation": "Nga nằm ở miền Đông của châu Âu."
            }
        },
        {
            "id": 81,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 81: Dịch câu sau sang tiếng Việt:\n\"Letztes Jahr war sie in Vietnam.\"",
            "options": null,
            "correct_answer": "Năm ngoái cô ấy đã ở Việt Nam.",
            "explanation": "\"Letztes Jahr\" = Năm ngoái\nđộng từ quá khứ \"war\" diễn tả trạng thái đã ở đâu trong quá khứ.\n-> Đáp án: Năm ngoái cô ấy đã ở Việt Nam.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Năm ngoái cô ấy đã ở Việt Nam.",
                    "Năm ngoái cô ấy đã ở Việt Nam",
                    "Năm ngoái cô ấy ở Việt Nam.",
                    "Năm ngoái cô ấy ở Việt Nam"
                ],
                "audio_text": "Letztes Jahr war sie in Vietnam.",
                "translation": "Năm ngoái cô ấy đã ở Việt Nam."
            }
        },
        {
            "id": 82,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 82: Dịch câu sau sang tiếng Việt:\n\"Wo liegt Würzburg?\"",
            "options": null,
            "correct_answer": "Würzburg nằm ở đâu?",
            "explanation": "Từ để hỏi \"Wo\" = ở đâu, động từ \"liegen\" dùng để hỏi vị trí địa lý.\n-> Đáp án: Würzburg nằm ở đâu?",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Würzburg nằm ở đâu?", "Würzburg nằm ở đâu", "Würzburg ở đâu?"],
                "audio_text": "Wo liegt Würzburg?",
                "translation": "Würzburg nằm ở đâu?"
            }
        },
        {
            "id": 83,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 83: Dịch câu sau sang tiếng Việt:\n\"Die Schweiz liegt südlich von Deutschland.\"",
            "options": null,
            "correct_answer": "Thụy Sĩ nằm ở phía Nam của nước Đức.",
            "explanation": "\"die Schweiz\" = Thụy Sĩ, tính từ \"südlich von\" = ở phía Nam của (bên ngoài).\n-> Đáp án: Thụy Sĩ nằm ở phía Nam của nước Đức.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Thụy Sĩ nằm ở phía Nam của nước Đức.",
                    "Thụy Sĩ nằm ở phía Nam của nước Đức",
                    "Nước Thụy Sĩ nằm ở phía Nam của Đức."
                ],
                "audio_text": "Die Schweiz liegt südlich von Deutschland.",
                "translation": "Thụy Sĩ nằm ở phía Nam của nước Đức."
            }
        },
        {
            "id": 84,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 84: Dịch câu sau sang tiếng Việt:\n\"Köln liegt im Westen von Deutschland.\"",
            "options": null,
            "correct_answer": "Köln nằm ở miền Tây của nước Đức.",
            "explanation": "\"im Westen\" diễn tả vị trí ở miền Tây bên trong nước Đức.\n-> Đáp án: Köln nằm ở miền Tây của nước Đức.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Köln nằm ở miền Tây của nước Đức.",
                    "Köln nằm ở miền Tây của nước Đức",
                    "Köln nằm ở phía Tây nước Đức."
                ],
                "audio_text": "Köln liegt im Westen von Deutschland.",
                "translation": "Köln nằm ở miền Tây của nước Đức."
            }
        },
        {
            "id": 85,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 85: Dịch câu sau sang tiếng Việt:\n\"Früher war mein Onkel Lehrer in Dresden.\"",
            "options": null,
            "correct_answer": "Trước đây chú/bác tôi từng là giáo viên ở Dresden.",
            "explanation": "\"Früher\" = Trước đây, \"war\" = từng là, \"mein Onkel\" = chú/bác/cậu của tôi.\n-> Đáp án: Trước đây chú/bác tôi từng là giáo viên ở Dresden.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Trước đây chú tôi từng là giáo viên ở Dresden.",
                    "Trước đây bác tôi từng là giáo viên ở Dresden.",
                    "Trước đây chú của tôi là giáo viên ở Dresden.",
                    "Trước đây cậu tôi từng là giáo viên ở Dresden."
                ],
                "audio_text": "Früher war mein Onkel Lehrer in Dresden.",
                "translation": "Trước đây chú/bác tôi từng là giáo viên ở Dresden."
            }
        },
        {
            "id": 86,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 86: Dịch câu sau sang tiếng Việt:\n\"Sie spricht Arabisch und Englisch.\"",
            "options": null,
            "correct_answer": "Cô ấy nói tiếng Ả Rập và tiếng Anh.",
            "explanation": "\"spricht\" là dạng chia ngôi \"sie\" (cô ấy) của \"sprechen\", \"Arabisch\" = tiếng Ả Rập.\n-> Đáp án: Cô ấy nói tiếng Ả Rập và tiếng Anh.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Cô ấy nói tiếng Ả Rập và tiếng Anh.",
                    "Cô ấy nói tiếng Ả Rập và tiếng Anh",
                    "Cô ấy nói được tiếng Ả Rập và tiếng Anh."
                ],
                "audio_text": "Sie spricht Arabisch und Englisch.",
                "translation": "Cô ấy nói tiếng Ả Rập và tiếng Anh."
            }
        },
        {
            "id": 87,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 87: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Bonn liegt südwestlich von Rostock.",
            "explanation": "Cấu trúc phương hướng ngoài thành phố: Chủ ngữ (Bonn) + liegt + tính từ hướng (südwestlich, không có im) + von + Rostock.\n-> Đáp án: Bonn liegt südwestlich von Rostock.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["liegt", "Bonn", "südwestlich", "Rostock", "von", "."],
                "accepted_answers": ["Bonn liegt südwestlich von Rostock.", "Bonn liegt südwestlich von Rostock"],
                "audio_text": "Bonn liegt südwestlich von Rostock.",
                "translation": "Bonn nằm ở phía Tây Nam của Rostock."
            }
        },
        {
            "id": 88,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 88: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Ist das das Auto von Thomas?",
            "explanation": "Câu hỏi Yes/No luôn đảo động từ \"Ist\" lên đầu câu\nmạo từ xác định \"das\" đứng ngay trước \"Auto\"\n-> Đáp án: Ist das das Auto von Thomas?",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["das", "Ist", "Auto", "das", "von", "Thomas", "?"],
                "accepted_answers": ["Ist das das Auto von Thomas?", "Ist das das Auto von Thomas"],
                "audio_text": "Ist das das Auto von Thomas?",
                "translation": "Đó có phải là xe ô tô của Thomas không?"
            }
        },
        {
            "id": 89,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 89: Sắp xếp các từ sau thành câu hoàn chỉnh (mô tả vị trí giữa hai thành phố):",
            "options": null,
            "correct_answer": "Hannover liegt nordwestlich von Leipzig.",
            "explanation": "Hannover nằm bên ngoài, về phía Tây Bắc của Leipzig nên dùng tính từ \"nordwestlich von\"\n-> Đáp án: Hannover liegt nordwestlich von Leipzig.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["nordwestlich", "liegt", "Hannover", "von", "Leipzig", "."],
                "accepted_answers": ["Hannover liegt nordwestlich von Leipzig.", "Hannover liegt nordwestlich von Leipzig"],
                "audio_text": "Hannover liegt nordwestlich von Leipzig.",
                "translation": "Hannover nằm ở phía Tây Bắc của Leipzig."
            }
        },
        {
            "id": 90,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 90: Sắp xếp các từ sau thành câu hỏi quá khứ:",
            "options": null,
            "correct_answer": "Warst du am Wochenende in München?",
            "explanation": "Câu hỏi Yes/No quá khứ với \"sein\" đảo \"Warst\" lên đầu câu.\n-> Đáp án: Warst du am Wochenende in München?",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["am", "Warst", "du", "in", "Wochenende", "München", "?"],
                "accepted_answers": ["Warst du am Wochenende in München?", "Warst du am Wochenende in München"],
                "audio_text": "Warst du am Wochenende in München?",
                "translation": "Cuối tuần bạn có ở München không?"
            }
        },
        {
            "id": 91,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 91: Sắp xếp các từ sau thành câu phân biệt đồ vật:",
            "options": null,
            "correct_answer": "Das ist kein Fernseher, das ist ein Radio.",
            "explanation": "\"der Fernseher\" (giống đực) phủ định bằng \"kein\"\n\"das Radio\" (giống trung) dùng \"ein\"\n-> Đáp án: Das ist kein Fernseher, das ist ein Radio.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["ein", "ist", "Das", "kein", "Radio", "das", "Fernseher,", "ist", "."],
                "accepted_answers": [
                    "Das ist kein Fernseher, das ist ein Radio.",
                    "Das ist kein Fernseher, das ist ein Radio"
                ],
                "audio_text": "Das ist kein Fernseher, das ist ein Radio.",
                "translation": "Đó không phải tivi, đó là một cái đài radio."
            }
        },
        {
            "id": 92,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 92: Sắp xếp các từ sau thành câu nói về xuất xứ:",
            "options": null,
            "correct_answer": "Er kommt aus der Türkei.",
            "explanation": "Quốc gia giống cái \"die Türkei\" đi kèm giới từ \"aus\" thành \"aus der Türkei\"\n-> Đáp án: Er kommt aus der Türkei.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["Türkei", "kommt", "aus", "Er", "der", "."],
                "accepted_answers": ["Er kommt aus der Türkei.", "Er kommt aus der Türkei"],
                "audio_text": "Er kommt aus der Türkei.",
                "translation": "Anh ấy đến từ Thổ Nhĩ Kỳ."
            }
        },
        {
            "id": 93,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 93: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Das Kind lernt heute Deutsch in der Schule.",
            "explanation": "Động từ chia \"lernt\" đứng ở vị trí số 2 trong câu trần thuật.\n-> Đáp án: Das Kind lernt heute Deutsch in der Schule.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["lernt", "Das", "Kind", "Deutsch", "in der Schule", "heute", "."],
                "accepted_answers": [
                    "Das Kind lernt heute Deutsch in der Schule.",
                    "Heute lernt das Kind Deutsch in der Schule."
                ],
                "audio_text": "Das Kind lernt heute Deutsch in der Schule.",
                "translation": "Đứa trẻ hôm nay học tiếng Đức ở trường."
            }
        },
        {
            "id": 94,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 94: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Meine Freundin spricht gut Italienisch.",
            "explanation": "Chủ ngữ \"Meine Freundin\" (ngôi số ít giống cái) chia \"sprechen\" biến âm thành \"spricht\"\n-> Đáp án: Meine Freundin spricht gut Italienisch.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["spricht", "Freundin", "gut", "Meine", "Italienisch", "."],
                "accepted_answers": ["Meine Freundin spricht gut Italienisch.", "Meine Freundin spricht gut Italienisch"],
                "audio_text": "Meine Freundin spricht gut Italienisch.",
                "translation": "Bạn nữ của tôi nói tốt tiếng Ý."
            }
        },
        {
            "id": 95,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 95: Sắp xếp các từ sau thành câu mô tả vị trí địa lý:",
            "options": null,
            "correct_answer": "Stuttgart liegt südöstlich von Bonn.",
            "explanation": "Stuttgart nằm bên ngoài, ở phía Đông Nam của Bonn.\n-> dùng tính từ \"südöstlich von\"\n-> Đáp án: Stuttgart liegt südöstlich von Bonn.",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["von", "Stuttgart", "Bonn", "südöstlich", "liegt", "."],
                "accepted_answers": ["Stuttgart liegt südöstlich von Bonn.", "Stuttgart liegt südöstlich von Bonn"],
                "audio_text": "Stuttgart liegt südöstlich von Bonn.",
                "translation": "Stuttgart nằm ở phía Đông Nam của Bonn."
            }
        },
        {
            "id": 96,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 96: Sắp xếp các từ sau thành câu hỏi lịch sự:",
            "options": null,
            "correct_answer": "Woher kommen Sie, Frau Weber?",
            "explanation": "Câu hỏi W-Fragen lịch sự dùng ngôi \"Sie\": \"Woher kommen Sie, Frau Weber?\"\n-> Đáp án: Woher kommen Sie, Frau Weber?",
            "exp_reward": 15,
            "extra_data": {
                "tokens": ["kommen", "Woher", "Sie,", "Weber", "Frau", "?"],
                "accepted_answers": ["Woher kommen Sie, Frau Weber?", "Woher kommen Sie Frau Weber?"],
                "audio_text": "Woher kommen Sie, Frau Weber?",
                "translation": "Bà đến từ đâu vậy, bà Weber?"
            }
        },
        {
            "id": 97,
            "exercise_type": "phan_loai_dong_tu",
            "question": "Câu 97: Phân loại các dạng của động từ \"sein\" sau đây vào 2 nhóm Hiện tại (Präsens) / Quá khứ (Präteritum):",
            "options": null,
            "correct_answer": "Hiện tại (Präsens), Hiện tại (Präsens), Hiện tại (Präsens), Quá khứ (Präteritum), Quá khứ (Präteritum), Quá khứ (Präteritum)",
            "explanation": "Hiện tại (Präsens): bin, ist, seid.\nQuá khứ (Präteritum): war, waren, warst.\n-> Đáp án: Hiện tại (Präsens) cho 3 từ đầu, Quá khứ (Präteritum) cho 3 từ sau.",
            "exp_reward": 15,
            "extra_data": {
                "categories": ["Hiện tại (Präsens)", "Quá khứ (Präteritum)"],
                "items": [
                    {"word": "bin", "meaning_vi": "tôi là (ngôi ich)", "category": "Hiện tại (Präsens)"},
                    {"word": "ist", "meaning_vi": "anh/cô ấy là (ngôi er/sie/es)", "category": "Hiện tại (Präsens)"},
                    {"word": "seid", "meaning_vi": "các bạn là (ngôi ihr)", "category": "Hiện tại (Präsens)"},
                    {"word": "war", "meaning_vi": "tôi/anh ấy đã là (ich/er/sie/es)", "category": "Quá khứ (Präteritum)"},
                    {"word": "waren", "meaning_vi": "chúng tôi/họ đã là (wir/sie/Sie)", "category": "Quá khứ (Präteritum)"},
                    {"word": "warst", "meaning_vi": "bạn đã là (ngôi du)", "category": "Quá khứ (Präteritum)"}
                ],
                "accepted_answers": [
                    "Hiện tại (Präsens), Hiện tại (Präsens), Hiện tại (Präsens), Quá khứ (Präteritum), Quá khứ (Präteritum), Quá khứ (Präteritum)"
                ],
                "audio_text": "bin, ist, seid, war, waren, warst.",
                "translation": "Hiện tại: bin, ist, seid\nQuá khứ: war, waren, warst"
            }
        },
        {
            "id": 98,
            "exercise_type": "phan_loai_dong_tu",
            "question": "Câu 98: Phân loại 4 dạng chia của động từ \"sein\" sau đây vào 2 nhóm Hiện tại (Präsens) / Quá khứ (Präteritum):",
            "options": null,
            "correct_answer": "Hiện tại (Präsens), Quá khứ (Präteritum), Hiện tại (Präsens), Quá khứ (Präteritum)",
            "explanation": "\"bist\" (du) và \"sind\" (wir/sie/Sie) thuộc Hiện tại (Präsens)\n\"wart\" (ihr) và \"waren\" (wir/sie/Sie) thuộc Quá khứ (Präteritum).",
            "exp_reward": 15,
            "extra_data": {
                "categories": ["Hiện tại (Präsens)", "Quá khứ (Präteritum)"],
                "items": [
                    {"word": "bist", "meaning_vi": "bạn là (ngôi du)", "category": "Hiện tại (Präsens)"},
                    {"word": "wart", "meaning_vi": "các bạn đã là (ngôi ihr)", "category": "Quá khứ (Präteritum)"},
                    {"word": "sind", "meaning_vi": "chúng tôi/ngài là (wir/Sie)", "category": "Hiện tại (Präsens)"},
                    {"word": "war", "meaning_vi": "tôi/anh ấy đã ở (ich/er)", "category": "Quá khứ (Präteritum)"}
                ],
                "accepted_answers": ["Hiện tại (Präsens), Quá khứ (Präteritum), Hiện tại (Präsens), Quá khứ (Präteritum)"],
                "audio_text": "bist, wart, sind, war.",
                "translation": "Hiện tại: bist, sind\nQuá khứ: wart, war"
            }
        },
        {
            "id": 99,
            "exercise_type": "phan_loai_dong_tu",
            "question": "Câu 99: Phân loại 4 động từ sau (tragen, wohnen, lesen, kaufen) vào nhóm Bất quy tắc (biến âm ở ngôi du/er) hoặc Có quy tắc:",
            "options": null,
            "correct_answer": "Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc",
            "explanation": "\"tragen\" (a -> ä: trägt) và \"lesen\" (e -> ie: liest) biến âm ở ngôi du/er nên là Bất quy tắc\n\"wohnen\" và \"kaufen\" là Có quy tắc.\n-> Đáp án: Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc.",
            "exp_reward": 15,
            "extra_data": {
                "categories": ["Bất quy tắc", "Có quy tắc"],
                "items": [
                    {"word": "tragen", "meaning_vi": "mặc/đeo (a → ä: trägt)", "category": "Bất quy tắc"},
                    {"word": "wohnen", "meaning_vi": "sống, cư trú", "category": "Có quy tắc"},
                    {"word": "lesen", "meaning_vi": "đọc (e → ie: liest)", "category": "Bất quy tắc"},
                    {"word": "kaufen", "meaning_vi": "mua sắm", "category": "Có quy tắc"}
                ],
                "accepted_answers": [
                    "Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc",
                    "Bất quy tắc / Có quy tắc / Bất quy tắc / Có quy tắc"
                ],
                "audio_text": "tragen, wohnen, lesen, kaufen.",
                "translation": "tragen: mặc (bất quy tắc)\nwohnen: sống (có quy tắc)\nlesen: đọc (bất quy tắc)\nkaufen: mua (có quy tắc)"
            }
        },
        {
            "id": 100,
            "exercise_type": "phan_loai_tu_hoi",
            "question": "Câu 100: Chọn từ để hỏi thích hợp (Wo / Woher) cho 4 câu hỏi dưới đây:",
            "options": null,
            "correct_answer": "Woher, Wo, Wo, Woher",
            "explanation": "Động từ \"kommen\" (đến từ đâu) luôn dùng \"Woher\".\nCác câu hỏi vị trí tĩnh (\"liegen\", \"sein\") dùng \"Wo\"\n-> Đáp án: Woher, Wo, Wo, Woher.",
            "exp_reward": 15,
            "extra_data": {
                "categories": ["Wo", "Woher"],
                "items": [
                    {"word": "___ kommst du?", "meaning_vi": "Bạn đến từ đâu?", "category": "Woher"},
                    {"word": "___ liegt München?", "meaning_vi": "München nằm ở đâu?", "category": "Wo"},
                    {"word": "___ waren Sie gestern?", "meaning_vi": "Hôm qua ngài ở đâu?", "category": "Wo"},
                    {"word": "___ kommt sie?", "meaning_vi": "Cô ấy đến từ đâu?", "category": "Woher"}
                ],
                "accepted_answers": ["Woher, Wo, Wo, Woher", "Woher / Wo / Wo / Woher"],
                "audio_text": "Woher kommst du? Wo liegt München? Wo waren Sie gestern? Wo kommt sie?",
                "translation": "Bạn đến từ đâu?\nMünchen nằm ở đâu?\nHôm qua ngài ở đâu?\nCô ấy đến từ đâu?"
            }
        },
        {
            "id": 101,
            "exercise_type": "phan_loai_tu_hoi",
            "question": "Câu 101: Phân loại 4 câu trả lời sau (Aus der Türkei, In Hanoi, Maria, Ein Rucksack) tương ứng với từ để hỏi phù hợp (Woher / Wo / Wie / Was):",
            "options": null,
            "correct_answer": "Woher, Wo, Wie, Was",
            "explanation": "\"Aus der Türkei\" chỉ xuất xứ (Woher), \"In Hanoi\" chỉ vị trí (Wo), \"Maria\" trả lời câu hỏi tên (Wie), \"Ein Rucksack\" chỉ đồ vật (Was).\n-> Đáp án: Woher, Wo, Wie, Was.",
            "exp_reward": 15,
            "extra_data": {
                "categories": ["Woher", "Wo", "Wie", "Was"],
                "items": [
                    {"word": "Aus der Türkei.", "meaning_vi": "Từ Thổ Nhĩ Kỳ (xuất xứ)", "category": "Woher"},
                    {"word": "In Hanoi.", "meaning_vi": "Ở Hà Nội (vị trí)", "category": "Wo"},
                    {"word": "Maria.", "meaning_vi": "Tên riêng (hỏi tên)", "category": "Wie"},
                    {"word": "Ein Rucksack.", "meaning_vi": "Một chiếc ba lô (đồ vật)", "category": "Was"}
                ],
                "accepted_answers": ["Woher, Wo, Wie, Was", "Woher / Wo / Wie / Was"],
                "audio_text": "Aus der Türkei. In Hanoi. Maria. Ein Rucksack.",
                "translation": "Từ Thổ Nhĩ Kỳ\nỞ Hà Nội\nTên Maria\nMột chiếc ba lô"
            }
        },
        {
            "id": 102,
            "exercise_type": "phan_loai_tu_hoi",
            "question": "Câu 102: Phân loại 4 câu trả lời sau (Im Süden von Deutschland, Aus Ägypten, Eine Kamera, Ich heiße Paul) tương ứng với từ để hỏi phù hợp (Wo / Woher / Was / Wie):",
            "options": null,
            "correct_answer": "Wo, Woher, Was, Wie",
            "explanation": "\"Im Süden von Deutschland\" chỉ vị trí (Wo), \"Aus Ägypten\" chỉ xuất xứ (Woher), \"Eine Kamera\" chỉ sự vật (Was), \"Ich heiße Paul\" trả lời tên (Wie).\n-> Đáp án: Wo, Woher, Was, Wie.",
            "exp_reward": 15,
            "extra_data": {
                "categories": ["Woher", "Wo", "Wie", "Was"],
                "items": [
                    {"word": "Im Süden von Deutschland.", "meaning_vi": "Ở miền Nam nước Đức (vị trí)", "category": "Wo"},
                    {"word": "Aus Ägypten.", "meaning_vi": "Từ Ai Cập (xuất xứ)", "category": "Woher"},
                    {"word": "Eine Kamera.", "meaning_vi": "Một chiếc máy ảnh (đồ vật)", "category": "Was"},
                    {"word": "Ich heiße Paul.", "meaning_vi": "Tôi tên là Paul (hỏi tên)", "category": "Wie"}
                ],
                "accepted_answers": ["Wo, Woher, Was, Wie", "Wo / Woher / Was / Wie"],
                "audio_text": "Im Süden von Deutschland. Aus Ägypten. Eine Kamera. Ich heiße Paul.",
                "translation": "Ở miền Nam Đức\nTừ Ai Cập\nMột máy ảnh\nTôi tên là Paul"
            }
        },
        {
            "id": 103,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 103: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n\"Bremen liegt im nordwestlich von Leipzig.\"",
            "options": null,
            "correct_answer": "Bremen liegt nordwestlich von Leipzig.",
            "explanation": "\"nordwestlich\" là tính từ chỉ hướng (Bremen nằm bên ngoài Leipzig), bắt buộc bỏ giới từ \"im\"\n-> Đáp án: Bremen liegt nordwestlich von Leipzig.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Bremen liegt nordwestlich von Leipzig.", "Bremen liegt nordwestlich von Leipzig"],
                "audio_text": "Bremen liegt nordwestlich von Leipzig.",
                "translation": "Bremen nằm ở phía Tây Bắc của Leipzig."
            }
        },
        {
            "id": 104,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 104: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n\"Das ist kein Kamera. Das ist ein Handy.\"",
            "options": null,
            "correct_answer": "Das ist keine Kamera. Das ist ein Handy.",
            "explanation": "\"die Kamera\" mang giống cái nên mạo từ phủ định phải là \"keine\", không dùng \"kein\"\n-> Đáp án: Das ist keine Kamera.\nDas ist ein Handy.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Das ist keine Kamera. Das ist ein Handy.", "Das ist keine Kamera. Das ist ein Handy"],
                "audio_text": "Das ist keine Kamera. Das ist ein Handy.",
                "translation": "Đó không phải là máy ảnh.\nĐó là một chiếc điện thoại."
            }
        },
        {
            "id": 105,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 105: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n\"Frankfurt liegt im westlich von Dresden.\"",
            "options": null,
            "correct_answer": "Frankfurt liegt westlich von Dresden.",
            "explanation": "\"westlich\" là tính từ chỉ hướng (bên ngoài Dresden), phải bỏ giới từ \"im\"\n-> Đáp án: Frankfurt liegt westlich von Dresden.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Frankfurt liegt westlich von Dresden.", "Frankfurt liegt westlich von Dresden"],
                "audio_text": "Frankfurt liegt westlich von Dresden.",
                "translation": "Frankfurt nằm ở phía Tây của Dresden."
            }
        },
        {
            "id": 106,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 106: Tìm lỗi sai về thì của động từ và viết lại câu đúng hoàn chỉnh:\n\"Heute bin ich zu Hause, und gestern sind wir in Köln.\"",
            "options": null,
            "correct_answer": "Heute bin ich zu Hause, und gestern waren wir in Köln.",
            "explanation": "Vế sau có trạng từ quá khứ \"gestern\" (hôm qua) nên động từ \"sein\" ở ngôi \"wir\" phải chia quá khứ thành \"waren\"\n-> Đáp án: Heute bin ich zu Hause, und gestern waren wir in Köln.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Heute bin ich zu Hause, und gestern waren wir in Köln.",
                    "Heute bin ich zu Hause, und gestern waren wir in Köln",
                    "Heute bin ich zu Hause, und gestern waren wir in Koeln."
                ],
                "audio_text": "Heute bin ich zu Hause, und gestern waren wir in Köln.",
                "translation": "Hôm nay tôi ở nhà, còn hôm qua chúng tôi đã ở Köln."
            }
        },
        {
            "id": 107,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 107: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n\"Meine Familie kommt aus Türkei.\"",
            "options": null,
            "correct_answer": "Meine Familie kommt aus der Türkei.",
            "explanation": "\"die Türkei\" là quốc gia bắt buộc có mạo từ giống cái, đi với giới từ \"aus\" phải là \"aus der Türkei\"\n-> Đáp án: Meine Familie kommt aus der Türkei.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Meine Familie kommt aus der Türkei.",
                    "Meine Familie kommt aus der Türkei",
                    "Meine Familie kommt aus der Tuerkei."
                ],
                "audio_text": "Meine Familie kommt aus der Türkei.",
                "translation": "Gia đình tôi đến từ Thổ Nhĩ Kỳ."
            }
        },
        {
            "id": 108,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 108: Tìm lỗi sai kiến thức ngôn ngữ và viết lại câu đúng hoàn chỉnh:\n\"In Ägypten spricht man Ägyptisch.\"",
            "options": null,
            "correct_answer": "In Ägypten spricht man Arabisch.",
            "explanation": "Ngôn ngữ chính thức của Ai Cập (Ägypten) là tiếng Ả Rập (\"Arabisch\"), không phải \"Ägyptisch\"\n-> Đáp án: In Ägypten spricht man Arabisch.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "In Ägypten spricht man Arabisch.",
                    "In Ägypten spricht man Arabisch",
                    "In Aegypten spricht man Arabisch."
                ],
                "audio_text": "In Ägypten spricht man Arabisch.",
                "translation": "Ở Ai Cập người ta nói tiếng Ả Rập."
            }
        },
        {
            "id": 109,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 109: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n\"Mein Bruder wohnen jetzt in der Schweiz.\"",
            "options": null,
            "correct_answer": "Mein Bruder wohnt jetzt in der Schweiz.",
            "explanation": "Chủ ngữ \"Mein Bruder\" (số ít, ngôi er) chia động từ \"wohnen\" là \"wohnt\"\n-> Đáp án: Mein Bruder wohnt jetzt in der Schweiz.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Mein Bruder wohnt jetzt in der Schweiz.", "Mein Bruder wohnt jetzt in der Schweiz"],
                "audio_text": "Mein Bruder wohnt jetzt in der Schweiz.",
                "translation": "Anh/em trai tôi hiện đang sống ở Thụy Sĩ."
            }
        },
        {
            "id": 110,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 110: Tìm lỗi sai mạo từ sau động từ \"sein\" và viết lại câu đúng hoàn chỉnh:\n\"Ist das einen Schlüssel? Nein, das ist ein Kuli.\"",
            "options": null,
            "correct_answer": "Ist das ein Schlüssel? Nein, das ist ein Kuli.",
            "explanation": "Sau động từ \"sein\" luôn dùng Nominativ (không dùng Akkusativ \"einen\"), \"der Schlüssel\" dùng \"ein\"\n-> Đáp án: Ist das ein Schlüssel?\nNein, das ist ein Kuli.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Ist das ein Schlüssel? Nein, das ist ein Kuli.",
                    "Ist das ein Schlüssel? Nein, das ist ein Kuli",
                    "Ist das ein Schluessel? Nein, das ist ein Kuli."
                ],
                "audio_text": "Ist das ein Schlüssel? Nein, das ist ein Kuli.",
                "translation": "Đó có phải một chiếc chìa khóa không?\nKhông, đó là một cây bút bi."
            }
        },
        {
            "id": 111,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 111: Tìm lỗi sai chia động từ bất quy tắc và viết lại câu đúng hoàn chỉnh:\n\"Anna tragt heute eine schöne Jacke.\"",
            "options": null,
            "correct_answer": "Anna trägt heute eine schöne Jacke.",
            "explanation": "Động từ bất quy tắc \"tragen\" phải biến âm a -> ä ở ngôi thứ 3 số ít \"Anna\" thành \"trägt\"\n-> Đáp án: Anna trägt heute eine schöne Jacke.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Anna trägt heute eine schöne Jacke.",
                    "Anna trägt heute eine schöne Jacke",
                    "Anna traegt heute eine schoene Jacke."
                ],
                "audio_text": "Anna trägt heute eine schöne Jacke.",
                "translation": "Hôm nay Anna mặc một chiếc áo khoác đẹp."
            }
        },
        {
            "id": 112,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 112: Tìm lỗi sai giới từ và viết lại câu đúng hoàn chỉnh:\n\"Hue liegt im Zentrum in Vietnam.\"",
            "options": null,
            "correct_answer": "Hue liegt in der Mitte von Vietnam.",
            "explanation": "Khi diễn tả vị trí giữa của một quốc gia/vùng phải dùng cụm \"in der Mitte von ...\" (hoặc \"im Zentrum von ...\", không dùng \"in Vietnam\").\n-> Đáp án: Hue liegt in der Mitte von Vietnam.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Hue liegt in der Mitte von Vietnam.",
                    "Hue liegt in der Mitte von Vietnam",
                    "Hue liegt im Zentrum von Vietnam.",
                    "Hue liegt im Zentrum von Vietnam"
                ],
                "audio_text": "Hue liegt in der Mitte von Vietnam.",
                "translation": "Huế nằm ở miền Trung của Việt Nam."
            }
        },
        {
            "id": 113,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 113: Đặt câu hỏi W-Fragen về xuất xứ cho cụm từ gạch chân (hỏi ở ngôi du):",
            "options": null,
            "correct_answer": "Woher kommst du?",
            "explanation": "Cụm \"aus Russland\" chỉ xuất xứ nên dùng từ để hỏi \"Woher\", chia động từ ở ngôi \"du\" là \"kommst\"\n-> Đáp án: Woher kommst du?",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ich komme aus Russland.",
                "target_phrase": "aus Russland",
                "accepted_answers": ["Woher kommst du?", "Woher kommst du"],
                "audio_text": "Woher kommst du?",
                "translation": "Bạn đến từ đâu?\n(Tôi đến từ Nga.)"
            }
        },
        {
            "id": 114,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 114: Đặt câu hỏi W-Fragen về đồ uống cho từ gạch chân (hỏi ở ngôi ihr):",
            "options": null,
            "correct_answer": "Was trinkt ihr?",
            "explanation": "\"Kaffee\" là đồ uống (sự vật), dùng từ để hỏi \"Was\".\nNgôi \"ihr\" chia \"trinken\" là \"trinkt\" (cũng chấp nhận \"Was möchtet ihr trinken?\").\n-> Đáp án: Was trinkt ihr?",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Wir trinken Kaffee.",
                "target_phrase": "Kaffee",
                "accepted_answers": [
                    "Was trinkt ihr?",
                    "Was trinkt ihr",
                    "Was möchtet ihr trinken?",
                    "Was möchtet ihr trinken",
                    "Was moechtet ihr trinken?"
                ],
                "audio_text": "Was trinkt ihr?",
                "translation": "Các bạn uống gì?\n(Chúng tôi uống cà phê.)"
            }
        },
        {
            "id": 115,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 115: Đặt câu hỏi W-Fragen về vị trí địa lý cho cụm từ gạch chân:",
            "options": null,
            "correct_answer": "Wo liegt Hanoi?",
            "explanation": "Cụm \"im Norden von Vietnam\" chỉ vị trí địa lý tĩnh nên dùng từ để hỏi \"Wo\"\n-> Đáp án: Wo liegt Hanoi?",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Hanoi liegt im Norden von Vietnam.",
                "target_phrase": "im Norden von Vietnam",
                "accepted_answers": ["Wo liegt Hanoi?", "Wo liegt Hanoi"],
                "audio_text": "Wo liegt Hanoi?",
                "translation": "Hà Nội nằm ở đâu?\n(Hà Nội nằm ở miền Bắc Việt Nam.)"
            }
        },
        {
            "id": 116,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 116: Đặt câu hỏi W-Fragen về nơi chốn quá khứ cho cụm từ gạch chân (hỏi ở ngôi du):",
            "options": null,
            "correct_answer": "Wo warst du gestern?",
            "explanation": "Cụm \"im Kino\" chỉ nơi chốn trong quá khứ.\n-> dùng \"Wo\" và chia \"sein\" ở quá khứ ngôi \"du\" là \"warst\"\n-> Đáp án: Wo warst du gestern?",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Gestern war ich im Kino.",
                "target_phrase": "im Kino",
                "accepted_answers": ["Wo warst du gestern?", "Wo warst du gestern"],
                "audio_text": "Wo warst du gestern?",
                "translation": "Hôm qua bạn đã ở đâu?\n(Hôm qua tôi đã ở rạp chiếu phim.)"
            }
        },
        {
            "id": 117,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 117: Đặt câu hỏi W-Fragen về tiếng mẹ đẻ cho từ gạch chân (hỏi ở ngôi du):",
            "options": null,
            "correct_answer": "Was ist deine Muttersprache?",
            "explanation": "\"Arabisch\" là ngôn ngữ/sự vật, hỏi tiếng mẹ đẻ của bạn là gì dùng \"Was ist deine Muttersprache?\" (cũng chấp nhận \"Welche Sprache sprichst du?\").\n-> Đáp án: Was ist deine Muttersprache?",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Meine Muttersprache ist Arabisch.",
                "target_phrase": "Arabisch",
                "accepted_answers": [
                    "Was ist deine Muttersprache?",
                    "Was ist deine Muttersprache",
                    "Welche ist deine Muttersprache?",
                    "Welche Sprache sprichst du?"
                ],
                "audio_text": "Was ist deine Muttersprache?",
                "translation": "Tiếng mẹ đẻ của bạn là gì?\n(Tiếng mẹ đẻ của tôi là tiếng Ả Rập.)"
            }
        },
        {
            "id": 118,
            "exercise_type": "dung_sai",
            "question": "Câu 118: Đọc đoạn văn sau và chọn Đúng (Richtig) hoặc Sai (Falsch):\nNhận định: \"Hamburg liegt südlich von Deutschland.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Falsch",
            "explanation": "Đoạn văn xác nhận \"Hamburg liegt im Norden von Deutschland\" (ở miền Bắc nước Đức), nên nhận định Hamburg nằm ở phía Nam là sai.\n-> Đáp án: Falsch.",
            "exp_reward": 15,
            "extra_data": {
                "reading_text": "Hamburg liegt im Norden von Deutschland. München liegt im Süden.",
                "reading_translation_vi": "Hamburg nằm ở miền Bắc nước Đức.\nMünchen nằm ở miền Nam.",
                "accepted_answers": ["Falsch", "Falsch (Sai)"],
                "audio_text": "Hamburg liegt im Norden von Deutschland. München liegt im Süden.",
                "translation": "Hamburg nằm ở miền Bắc nước Đức.\nMünchen nằm ở miền Nam."
            }
        },
        {
            "id": 119,
            "exercise_type": "dung_sai",
            "question": "Câu 119: Đọc đoạn văn sau và chọn Đúng (Richtig) hoặc Sai (Falsch):\nNhận định: \"Die Familie wohnt jetzt in Wien.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Richtig",
            "explanation": "Trong đoạn văn có câu \"Jetzt wohnen wir in Europa, in Wien.\"\n-> trùng khớp hoàn toàn với nhận định.\n-> Đáp án: Richtig.",
            "exp_reward": 15,
            "extra_data": {
                "reading_text": "Früher war meine Familie in der Schweiz. Mein Vater war Arzt in Zürich und meine Mutter war Lehrerin. Jetzt wohnen wir in Europa, in Wien. Ich spreche Deutsch und Englisch.",
                "reading_translation_vi": "Trước đây gia đình tôi từng ở Thụy Sĩ.\nBố tôi từng là bác sĩ ở Zürich và mẹ tôi từng là giáo viên.\nBây giờ chúng tôi sống ở châu Âu, tại Viên.\nTôi nói tiếng Đức và tiếng Anh.",
                "accepted_answers": ["Richtig", "Richtig (Đúng)"],
                "audio_text": "Früher war meine Familie in der Schweiz. Mein Vater war Arzt in Zürich und meine Mutter war Lehrerin. Jetzt wohnen wir in Europa, in Wien. Ich spreche Deutsch und Englisch.",
                "translation": "Trước đây gia đình tôi từng ở Thụy Sĩ.\nHiện tại gia đình sống ở Viên."
            }
        },
        {
            "id": 120,
            "exercise_type": "dung_sai",
            "question": "Câu 120: Đọc đoạn văn sau và chọn Đúng (Richtig) hoặc Sai (Falsch):\nNhận định: \"Da Nang liegt im Westen von Vietnam.\"",
            "options": ["Richtig", "Falsch"],
            "correct_answer": "Falsch",
            "explanation": "Đoạn văn nêu rõ \"Da Nang liegt in der Mitte von Vietnam\" (nằm ở miền Trung/giữa Việt Nam), không phải miền Tây.\n-> Đáp án: Falsch.",
            "exp_reward": 15,
            "extra_data": {
                "reading_text": "Hanoi liegt im Norden von Vietnam und Can Tho liegt im Süden. Da Nang liegt in der Mitte von Vietnam. Meine Freundin kommt aus Da Nang und ihre Muttersprache ist Vietnamesisch.",
                "reading_translation_vi": "Hà Nội nằm ở miền Bắc Việt Nam và Cần Thơ nằm ở miền Nam.\nĐà Nẵng nằm ở miền Trung của Việt Nam.\nBạn nữ của tôi đến từ Đà Nẵng và tiếng mẹ đẻ của cô ấy là tiếng Việt.",
                "accepted_answers": ["Falsch", "Falsch (Sai)"],
                "audio_text": "Hanoi liegt im Norden von Vietnam und Can Tho liegt im Süden. Da Nang liegt in der Mitte von Vietnam. Meine Freundin kommt aus Da Nang und ihre Muttersprache ist Vietnamesisch.",
                "translation": "Hà Nội ở miền Bắc, Cần Thơ ở miền Nam, Đà Nẵng ở miền Trung Việt Nam."
            }
        },
        {
            "id": 121,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 121: Sắp xếp các câu thoại sau theo đúng thứ tự một đoạn hội thoại hỏi vị trí hợp lý:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi vị trí chung -> Trả lời ở nước Đức.\n-> Hỏi kỹ hơn ở vùng nào.\n-> Trả lời chi tiết bằng phương hướng (im Süden).\n-> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Gast", "text": "Entschuldigung, wo liegt München?"},
                    {"id": 2, "speaker": "Passant", "text": "München? Das liegt in Deutschland."},
                    {"id": 3, "speaker": "Gast", "text": "Ja, aber wo genau in Deutschland?"},
                    {"id": 4, "speaker": "Passant", "text": "München liegt im Süden von Deutschland."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Entschuldigung, wo liegt München? München? Das liegt in Deutschland. Ja, aber wo genau in Deutschland? München liegt im Süden von Deutschland.",
                "translation": "- Khách: Xin lỗi, München nằm ở đâu?\n- Người qua đường: München à?\nNó nằm ở Đức.\n- Khách: Vâng, nhưng chính xác ở đâu tại Đức?\n- Người qua đường: München nằm ở miền Nam nước Đức."
            }
        },
        {
            "id": 122,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 122: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại hỏi thăm quá khứ:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi hôm qua ở đâu -> Trả lời ở buổi hòa nhạc.\n-> Hỏi cảm nhận buổi hòa nhạc thế nào.\n-> Trả lời thật tuyệt vời.\n-> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Mia", "text": "Wo warst du gestern Abend, Lukas?"},
                    {"id": 2, "speaker": "Lukas", "text": "Ich war im Konzert in Dresden."},
                    {"id": 3, "speaker": "Mia", "text": "Und wie war das Konzert?"},
                    {"id": 4, "speaker": "Lukas", "text": "Es war fantastisch!"}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Wo warst du gestern Abend, Lukas? Ich war im Konzert in Dresden. Und wie war das Konzert? Es war fantastisch!",
                "translation": "- Mia: Tối hôm qua bạn ở đâu vậy, Lukas?\n- Lukas: Tôi đã ở buổi hòa nhạc tại Dresden.\n- Mia: Thế buổi hòa nhạc thế nào?\n- Lukas: Nó thật tuyệt vời!"
            }
        },
        {
            "id": 123,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 123: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại hỏi xuất xứ và ngôn ngữ:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi đến từ đâu -> Trả lời từ Thổ Nhĩ Kỳ.\n-> Hỏi về ngôn ngữ nói được.\n-> Xác nhận tiếng mẹ đẻ và đang học tiếng Đức.\n-> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Tim", "text": "Woher kommst du eigentlich, Leyla?"},
                    {"id": 2, "speaker": "Leyla", "text": "Ich komme aus der Türkei."},
                    {"id": 3, "speaker": "Tim", "text": "Sprichst du Türkisch und Deutsch?"},
                    {"id": 4, "speaker": "Leyla", "text": "Ja, Türkisch ist meine Muttersprache und ich lerne Deutsch."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Woher kommst du eigentlich, Leyla? Ich komme aus der Türkei. Sprichst du Türkisch und Deutsch? Ja, Türkisch ist meine Muttersprache und ich lerne Deutsch.",
                "translation": "- Tim: Thực ra bạn đến từ đâu vậy, Leyla?\n- Leyla: Tôi đến từ Thổ Nhĩ Kỳ.\n- Tim: Bạn nói tiếng Thổ Nhĩ Kỳ và tiếng Đức à?\n- Leyla: Vâng, tiếng Thổ Nhĩ Kỳ là tiếng mẹ đẻ của tôi và tôi đang học tiếng Đức."
            }
        },
        {
            "id": 124,
            "exercise_type": "doc_menu_cafe",
            "question": "Câu 124: Nhìn vào bản đồ dưới đây, bạn thấy Berlin ở góc trên bên phải của nước Đức. Chọn câu miêu tả đúng:",
            "options": [
                "Berlin liegt im Nordosten von Deutschland.",
                "Berlin liegt im Südwesten von Deutschland.",
                "Berlin liegt im Nordwesten von Deutschland.",
                "Berlin liegt im Südosten von Deutschland."
            ],
            "correct_answer": "Berlin liegt im Nordosten von Deutschland.",
            "explanation": "Vị trí góc trên bên phải tương ứng với hướng Đông Bắc (Nord + Ost = Nordosten), nằm bên trong Đức nên dùng \"im Nordosten von Deutschland\"\n-> Đáp án: Berlin liegt im Nordosten von Deutschland.",
            "exp_reward": 15,
            "extra_data": {
                "map_card": {
                    "country": "Deutschland",
                    "city": "Berlin",
                    "x": 182,
                    "y": 64
                },
                "accepted_answers": ["Berlin liegt im Nordosten von Deutschland."],
                "audio_text": "Berlin liegt im Nordosten von Deutschland.",
                "translation": "Berlin nằm ở miền Đông Bắc của nước Đức."
            }
        },
        {
            "id": 125,
            "exercise_type": "doc_menu_cafe",
            "question": "Câu 125: Nhìn vào bảng thực đơn sau và chọn câu trả lời phù hợp nhất của khách khi bồi bàn hỏi:\n\"Was möchten Sie bestellen?\"",
            "options": [
                "Ich nehme einen Tee und einen Kuchen, bitte.",
                "München liegt im Süden von Deutschland.",
                "Nein, ich komme aus der Schweiz.",
                "Früher waren wir Lehrer in Berlin."
            ],
            "correct_answer": "Ich nehme einen Tee und einen Kuchen, bitte.",
            "explanation": "Khi bồi bàn hỏi gọi món (\"Was möchten Sie bestellen?\"), câu phản hồi hợp lý theo thực đơn là chọn đồ uống/bánh có trong menu.\n-> Đáp án: Ich nehme einen Tee und einen Kuchen, bitte.",
            "exp_reward": 15,
            "extra_data": {
                "menu_items": [
                    {"name": "Kaffee", "price": "2,80 €"},
                    {"name": "Tee", "price": "2,20 €"},
                    {"name": "Kuchen", "price": "3,40 €"}
                ],
                "accepted_answers": ["Ich nehme einen Tee und einen Kuchen, bitte."],
                "audio_text": "Was möchten Sie bestellen? Ich nehme einen Tee und einen Kuchen, bitte.",
                "translation": "Ngài muốn gọi món gì ạ?\nCho tôi gọi một trà và một bánh ngọt, làm ơn."
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
    print(f"Đã nạp thành công {len(exercises_data)} bài tập (Bài 14) với đầy đủ 125 câu chuẩn QA.")
    conn.close()


if __name__ == "__main__":
    seed_lesson_14()
