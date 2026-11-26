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
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900"><b>Bist</b> du jetzt zu Hause?</span> <span class="text-xs text-slate-500 italic block">Bây giờ bạn có ở nhà không?</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Bist du jetzt zu Hause?')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
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
                            <td class="px-4 py-2.5"><span class="font-mono font-semibold text-slate-900">Wir <b>sind</b> heute in Berlin.</span> <span class="text-xs text-slate-500 italic block">Hôm nay chúng tôi ở Berlin.</span></td>
                            <td class="px-3 py-2.5 text-center"><button type="button" onclick="b14_speakGerman('Wir sind heute in Berlin.')" class="p-1 rounded-lg bg-slate-50 hover:bg-indigo-100 border border-slate-200 cursor-pointer">🔊</button></td>
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
        ("Schlüssel", "der", "chìa khóa (Pl: die Schlüssel)", "„Wo ist der Schlüssel heute?“ — Hôm nay chiếc chìa khóa ở đâu?"),
        ("Arzt", "der", "bác sĩ (Pl: die Ärzte)", "„Früher war mein Vater Arzt.“ — Trước đây bố tôi từng là bác sĩ."),
        ("Lehrer", "der", "giáo viên nam (Pl: die Lehrer)", "„Früher waren wir Studenten, jetzt sind wir Lehrer.“ — Trước đây chúng tôi là sinh viên, nay là giáo viên."),
        ("Film", "der", "bộ phim (Pl: die Filme)", "„Gestern war ich im Kino, der Film war fantastisch!“ — Hôm qua tôi ở rạp, bộ phim rất tuyệt vời!"),
        ("Computer", "der", "máy vi tính (Pl: die Computer)", "„Das ist kein Fernseher, das ist ein Computer.“ — Đó không phải tivi, đó là máy vi tính."),
        ("Nordwesten", "der", "hướng Tây Bắc (Pl: nur Sg.)", "„Bremen liegt im Nordwesten von Deutschland.“ — Bremen nằm ở miền Tây Bắc của nước Đức."),
        ("Südosten", "der", "hướng Đông Nam (Pl: nur Sg.)", "„Griechenland liegt im Südosten von Europa.“ — Hy Lạp nằm ở miền Đông Nam của châu Âu."),
        ("Südwesten", "der", "hướng Tây Nam (Pl: nur Sg.)", "„Spanien liegt im Südwesten von Europa.“ — Tây Ban Nha nằm ở miền Tây Nam của châu Âu."),
        ("Kamera", "die", "máy ảnh (Pl: die Kameras)", "„Das ist keine Kamera, das ist ein Handy.“ — Đó không phải máy ảnh, đó là điện thoại."),
        ("Muttersprache", "die", "tiếng mẹ đẻ (Pl: die Muttersprachen)", "„Seine Muttersprache ist Arabisch.“ — Tiếng mẹ đẻ của anh ấy là tiếng Ả Rập."),
        ("Freundin", "die", "bạn gái (Pl: die Freundinnen)", "„Meine Freundin spricht gut Deutsch und Englisch.“ — Bạn gái tôi nói tốt tiếng Đức và tiếng Anh."),
        ("Kind", "das", "đứa trẻ, con (Pl: die Kinder)", "„Das Kind lernt heute Deutsch in der Schule.“ — Đứa trẻ hôm nay học tiếng Đức ở trường."),
        ("Konzert", "das", "buổi hòa nhạc (Pl: die Konzerte)", "„Das Konzert gestern Abend war fantastisch!“ — Buổi hòa nhạc tối qua thật tuyệt vời!"),
        ("Radio", "das", "cái đài radio (Pl: die Radios)", "„Nein, das ist kein Radio.“ — Không, đó không phải là một cái đài."),
        ("Zentrum", "das", "trung tâm (Pl: die Zentren)", "„Da Nang liegt im Zentrum von Vietnam.“ — Đà Nẵng nằm ở trung tâm của Việt Nam."),
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
        # =====================================================================
        # DẠNG 1: PHƯƠNG HƯỚNG & VỊ TRÍ (CÂU 1 - 30)
        # =====================================================================
        {
            "id": 1,
            "exercise_type": "trac_nghiem",
            "question": "Câu 1: Chọn giới từ thích hợp:\n„Berlin liegt ___ Nordosten von Deutschland.“",
            "options": ["im", "in", "(để trống)"],
            "correct_answer": "im",
            "explanation": "„Nordosten“ là danh từ viết hoa chỉ hướng, bắt buộc dùng cụm „im + [Danh từ hướng]“ -> Đáp án: im.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Berlin liegt im Nordosten von Deutschland.",
                "translation": "Berlin nằm ở miền Đông Bắc của Đức."
            }
        },
        {
            "id": 2,
            "exercise_type": "trac_nghiem",
            "question": "Câu 2: Chọn giới từ thích hợp:\n„Hamburg liegt ___ nördlich von Hannover.“",
            "options": ["im", "in", "(để trống)"],
            "correct_answer": "(để trống)",
            "explanation": "„nördlich“ là tính từ (có đuôi -lich), tuyệt đối không dùng giới từ „im“ hay „in“ -> Đáp án: (để trống).",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Hamburg liegt nördlich von Hannover.",
                "translation": "Hamburg nằm ở phía Bắc của Hannover."
            }
        },
        {
            "id": 3,
            "exercise_type": "dien_khuyet",
            "question": "Câu 3: Điền danh từ chỉ hướng thích hợp vào chỗ trống:\n„Hai Phong liegt im ___ von Vietnam.“ (hướng Đông Bắc)",
            "options": null,
            "correct_answer": "Nordosten",
            "explanation": "Sau „im“ cần dùng danh từ hướng viết hoa „Nordosten“ -> Đáp án: Nordosten.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Nordosten", "nordosten"],
                "audio_text": "Hai Phong liegt im Nordosten von Vietnam.",
                "translation": "Hải Phòng nằm ở miền Đông Bắc của Việt Nam."
            }
        },
        {
            "id": 4,
            "exercise_type": "dien_khuyet",
            "question": "Câu 4: Điền cụm từ chỉ vị trí thích hợp vào chỗ trống:\n„Da Nang liegt ___ von Vietnam.“ (trung tâm)",
            "options": null,
            "correct_answer": "im Zentrum",
            "explanation": "Cụm từ cố định chỉ trung tâm ở bên trong là „im Zentrum“ (hoặc „in der Mitte“) -> Đáp án: im Zentrum.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["im Zentrum", "im zentrum", "in der Mitte", "in der mitte"],
                "audio_text": "Da Nang liegt im Zentrum von Vietnam.",
                "translation": "Đà Nẵng nằm ở trung tâm của Việt Nam."
            }
        },
        {
            "id": 5,
            "exercise_type": "trac_nghiem",
            "question": "Câu 5: Chọn câu ĐÚNG NHẤT mô tả vị trí của Cần Thơ (thuộc Việt Nam):",
            "options": [
                "Can Tho liegt im südlich von Vietnam.",
                "Can Tho liegt im Süden von Vietnam.",
                "Can Tho liegt im Süden Vietnam."
            ],
            "correct_answer": "Can Tho liegt im Süden von Vietnam.",
            "explanation": "Cần Thơ nằm bên trong Việt Nam nên phải dùng „im Süden von Vietnam“; „im südlich“ sai vì ghép „im“ với tính từ, còn phương án C thiếu giới từ „von“ -> Đáp án: Can Tho liegt im Süden von Vietnam..",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Can Tho liegt im Süden von Vietnam.",
                "translation": "Cần Thơ nằm ở miền Nam của Việt Nam."
            }
        },
        {
            "id": 6,
            "exercise_type": "trac_nghiem",
            "question": "Câu 6: Câu nào sau đây SAI ngữ pháp?",
            "options": [
                "Dresden liegt östlich von Köln.",
                "Dresden liegt im Osten von Köln.",
                "Dresden liegt im östlich von Köln."
            ],
            "correct_answer": "Dresden liegt im östlich von Köln.",
            "explanation": "Câu „Dresden liegt im östlich von Köln.“ sai vì „östlich“ là tính từ đuôi -lich, không được dùng chung với „im“ -> Đáp án: Dresden liegt im östlich von Köln..",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Dresden liegt östlich von Köln.",
                "translation": "Dresden nằm ở phía Đông của Köln."
            }
        },
        {
            "id": 7,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 7: Dịch câu sau sang tiếng Đức (dùng tính từ hướng):\n„Nước Áo nằm ở phía Nam của nước Đức.“",
            "options": null,
            "correct_answer": "Österreich liegt südlich von Deutschland.",
            "explanation": "Phía Nam (tính từ) là „südlich“, không dùng „im“ -> Đáp án: Österreich liegt südlich von Deutschland..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Österreich liegt südlich von Deutschland.",
                    "Österreich liegt südlich von Deutschland",
                    "Oesterreich liegt südlich von Deutschland.",
                    "Oesterreich liegt südlich von Deutschland",
                    "Österreich liegt suedlich von Deutschland.",
                    "Oesterreich liegt suedlich von Deutschland"
                ],
                "audio_text": "Österreich liegt südlich von Deutschland.",
                "translation": "Nước Áo nằm ở phía Nam của nước Đức."
            }
        },
        {
            "id": 8,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 8: Dịch câu sau sang tiếng Đức (dùng danh từ hướng):\n„Tây Ban Nha nằm ở miền Tây Nam của Châu Âu.“",
            "options": null,
            "correct_answer": "Spanien liegt im Südwesten von Europa.",
            "explanation": "Miền Tây Nam (danh từ) là „Südwesten“, đi kèm „im“; Châu Âu là „Europa“ -> Đáp án: Spanien liegt im Südwesten von Europa..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Spanien liegt im Südwesten von Europa.",
                    "Spanien liegt im Südwesten von Europa",
                    "Spanien liegt im Suedwesten von Europa.",
                    "Spanien liegt im Suedwesten von Europa"
                ],
                "audio_text": "Spanien liegt im Südwesten von Europa.",
                "translation": "Tây Ban Nha nằm ở miền Tây Nam của Châu Âu."
            }
        },
        {
            "id": 9,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 9: Dịch câu sau sang tiếng Việt:\n„Russland liegt im Osten von Europa.“",
            "options": null,
            "correct_answer": "Nga nằm ở miền Đông của châu Âu.",
            "explanation": "„im Osten“ mô tả vị trí ở miền Đông / phía Đông châu Âu -> Đáp án: Nga nằm ở miền Đông của châu Âu..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Nga nằm ở miền Đông của châu Âu.",
                    "Nga nằm ở miền Đông của châu Âu",
                    "Nước Nga nằm ở phía Đông của châu Âu.",
                    "Nước Nga nằm ở phía Đông của châu Âu",
                    "Nước Nga nằm ở miền Đông của châu Âu.",
                    "Nga nằm ở phía Đông của châu Âu."
                ],
                "audio_text": "Russland liegt im Osten von Europa.",
                "translation": "Nga nằm ở miền Đông của châu Âu."
            }
        },
        {
            "id": 10,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 10: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Bonn liegt südwestlich von Rostock.",
            "explanation": "Trật tự chuẩn: Chủ ngữ (Bonn) + liegt + tính từ hướng (südwestlich) + von + Rostock -> Đáp án: Bonn liegt südwestlich von Rostock..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["liegt", "Bonn", "südwestlich", "Rostock", "von", "."],
                "accepted_answers": [
                    "Bonn liegt südwestlich von Rostock.",
                    "Bonn liegt südwestlich von Rostock",
                    "Bonn liegt suedwestlich von Rostock.",
                    "Bonn liegt suedwestlich von Rostock"
                ],
                "audio_text": "Bonn liegt südwestlich von Rostock.",
                "translation": "Bonn nằm ở phía Tây Nam của Rostock."
            }
        },
        {
            "id": 11,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 11: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Bremen liegt im nordwestlich von Deutschland.“",
            "options": null,
            "correct_answer": "Bremen liegt im Nordwesten von Deutschland.",
            "explanation": "Bremen nằm BÊN TRONG nước Đức nên phải dùng danh từ „im Nordwesten“, đồng thời không ghép „im“ với tính từ „nordwestlich“ -> Đáp án: Bremen liegt im Nordwesten von Deutschland..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Bremen liegt im Nordwesten von Deutschland.",
                    "Bremen liegt im Nordwesten von Deutschland"
                ],
                "audio_text": "Bremen liegt im Nordwesten von Deutschland.",
                "translation": "Bremen nằm ở miền Tây Bắc của nước Đức."
            }
        },
        {
            "id": 12,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 12: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„München liegt [1] [2] von Deutschland.“ (miền Nam)",
            "options": null,
            "correct_answer": "im / Süden",
            "explanation": "Có 2 ô trống nên dùng cấu trúc danh từ viết hoa „im Süden“ -> Đáp án: im / Süden.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "München liegt [1] [2] von Deutschland.",
                "accepted_answers": ["im / Süden", "im/Süden", "im Süden", "im / Sueden", "im/Sueden", "im / süden", "im/süden"],
                "audio_text": "München liegt im Süden von Deutschland.",
                "translation": "München nằm ở miền Nam của nước Đức."
            }
        },
        {
            "id": 13,
            "exercise_type": "dien_khuyet",
            "question": "Câu 13: Điền tính từ hướng thích hợp vào chỗ trống:\n„Polen liegt ___ von Deutschland.“ (phía Đông - Tính từ)",
            "options": null,
            "correct_answer": "östlich",
            "explanation": "Hướng Đông dạng tính từ là „östlich“ (không dùng „im“) -> Đáp án: östlich.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["östlich", "oestlich"],
                "audio_text": "Polen liegt östlich von Deutschland.",
                "translation": "Ba Lan nằm ở phía Đông của nước Đức."
            }
        },
        {
            "id": 14,
            "exercise_type": "dien_khuyet",
            "question": "Câu 14: Điền danh từ chỉ hướng thích hợp vào chỗ trống:\n„Italien liegt im ___ von Österreich.“ (hướng Nam)",
            "options": null,
            "correct_answer": "Süden",
            "explanation": "Đã có „im“, cần điền danh từ hướng Nam viết hoa „Süden“ -> Đáp án: Süden.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Süden", "süden", "Sueden", "sueden"],
                "audio_text": "Italien liegt im Süden von Österreich.",
                "translation": "Ý nằm ở miền Nam của nước Áo."
            }
        },
        {
            "id": 15,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 15: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Hannover liegt nordwestlich von Leipzig.",
            "explanation": "Thực tế địa lý: Hannover (52.37°N, 9.73°E) nằm ở phía Tây Bắc (nordwestlich) của Leipzig (51.34°N, 12.37°E) -> Đáp án: Hannover liegt nordwestlich von Leipzig..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["nordwestlich", "liegt", "Hannover", "von", "Leipzig", "."],
                "accepted_answers": [
                    "Hannover liegt nordwestlich von Leipzig.",
                    "Hannover liegt nordwestlich von Leipzig"
                ],
                "audio_text": "Hannover liegt nordwestlich von Leipzig.",
                "translation": "Hannover nằm ở phía Tây Bắc của Leipzig."
            }
        },
        {
            "id": 16,
            "exercise_type": "trac_nghiem",
            "question": "Câu 16: Cụm „im Nordwesten“ chỉ CÙNG HƯỚNG LA BÀN (Tây Bắc) với tính từ nào sau đây? (Lưu ý: „im Nordwesten“ dùng cho vị trí bên trong, còn tính từ dùng cho vị trí bên ngoài)",
            "options": ["nordöstlich", "südwestlich", "nordwestlich"],
            "correct_answer": "nordwestlich",
            "explanation": "Nord (Bắc) + Westen (Tây) = Tây Bắc. Tuy „im Nordwesten“ (bên trong) và „nordwestlich“ (bên ngoài) khác nhau về phạm vi, cả hai đều chỉ hướng Tây Bắc -> Đáp án: nordwestlich.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "im Nordwesten, nordwestlich",
                "translation": "Cùng hướng Tây Bắc: im Nordwesten (bên trong) / nordwestlich (bên ngoài)."
            }
        },
        {
            "id": 17,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 17: Dịch câu sau sang tiếng Đức (dùng tính từ hướng):\n„Paris nằm ở phía Tây của nước Đức.“",
            "options": null,
            "correct_answer": "Paris liegt westlich von Deutschland.",
            "explanation": "Hướng Tây dạng tính từ là „westlich“ -> Đáp án: Paris liegt westlich von Deutschland..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Paris liegt westlich von Deutschland.", "Paris liegt westlich von Deutschland"],
                "audio_text": "Paris liegt westlich von Deutschland.",
                "translation": "Paris nằm ở phía Tây của nước Đức."
            }
        },
        {
            "id": 18,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 18: Dịch câu sau sang tiếng Việt:\n„Die Schweiz liegt südlich von Deutschland.“",
            "options": null,
            "correct_answer": "Thụy Sĩ nằm ở phía Nam của nước Đức.",
            "explanation": "„die Schweiz“ = Thụy Sĩ, „südlich“ = phía Nam -> Đáp án: Thụy Sĩ nằm ở phía Nam của nước Đức..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Thụy Sĩ nằm ở phía Nam của nước Đức.",
                    "Thụy Sĩ nằm ở phía Nam của nước Đức",
                    "Nước Thụy Sĩ nằm ở phía Nam của Đức.",
                    "Nước Thụy Sĩ nằm ở phía Nam của nước Đức."
                ],
                "audio_text": "Die Schweiz liegt südlich von Deutschland.",
                "translation": "Thụy Sĩ nằm ở phía Nam của nước Đức."
            }
        },
        {
            "id": 19,
            "exercise_type": "trac_nghiem",
            "question": "Câu 19: Chọn giới từ thích hợp (cấu trúc mở rộng với Genitiv):\n„Das Hotel liegt ___ Westen der Stadt.“",
            "options": ["im", "in", "(để trống)"],
            "correct_answer": "im",
            "explanation": "„Westen“ là danh từ viết hoa chỉ hướng nên luôn đi với „im“ -> Đáp án: im.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Das Hotel liegt im Westen der Stadt.",
                "translation": "Khách sạn nằm ở khu vực phía Tây của thành phố."
            }
        },
        {
            "id": 20,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 20: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Hue liegt im Zentrum in Vietnam.“",
            "options": null,
            "correct_answer": "Hue liegt im Zentrum von Vietnam.",
            "explanation": "Cấu trúc mô tả thuộc về nơi nào phải dùng giới từ „von“ (của), không dùng „in“ (chấp nhận cả „in der Mitte von Vietnam“) -> Đáp án: Hue liegt im Zentrum von Vietnam..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Hue liegt im Zentrum von Vietnam.",
                    "Hue liegt im Zentrum von Vietnam",
                    "Hue liegt in der Mitte von Vietnam.",
                    "Hue liegt in der Mitte von Vietnam"
                ],
                "audio_text": "Hue liegt im Zentrum von Vietnam.",
                "translation": "Huế nằm ở miền Trung của Việt Nam."
            }
        },
        {
            "id": 21,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 21: Đặt câu hỏi cho cụm từ in đậm trong câu sau:\n„Stuttgart liegt **im Süden von Deutschland**.“",
            "options": null,
            "correct_answer": "Wo liegt Stuttgart?",
            "explanation": "Hỏi vị trí địa lý của thành phố dùng từ để hỏi „Wo“ -> Đáp án: Wo liegt Stuttgart?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Stuttgart liegt im Süden von Deutschland.",
                "target_phrase": "im Süden von Deutschland",
                "accepted_answers": ["Wo liegt Stuttgart?", "Wo liegt Stuttgart"],
                "audio_text": "Wo liegt Stuttgart?",
                "translation": "Stuttgart nằm ở đâu?"
            }
        },
        {
            "id": 22,
            "exercise_type": "dien_khuyet",
            "question": "Câu 22: Điền tính từ hướng thích hợp vào chỗ trống:\n„Frankfurt liegt ___ von Würzburg.“ (phía Tây - tính từ)",
            "options": null,
            "correct_answer": "westlich",
            "explanation": "Hướng Tây dạng tính từ không đi kèm „im“ là „westlich“ -> Đáp án: westlich.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["westlich"],
                "audio_text": "Frankfurt liegt westlich von Würzburg.",
                "translation": "Frankfurt nằm ở phía Tây của Würzburg."
            }
        },
        {
            "id": 23,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 23: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Wien liegt im Osten von Österreich.",
            "explanation": "Chủ ngữ (Wien) + liegt + cụm hướng (im Osten) + von + Österreich -> Đáp án: Wien liegt im Osten von Österreich..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["im Osten", "liegt", "Wien", "von", "Österreich", "."],
                "accepted_answers": [
                    "Wien liegt im Osten von Österreich.",
                    "Wien liegt im Osten von Österreich",
                    "Wien liegt im Osten von Oesterreich.",
                    "Wien liegt im Osten von Oesterreich"
                ],
                "audio_text": "Wien liegt im Osten von Österreich.",
                "translation": "Viên nằm ở miền Đông của nước Áo."
            }
        },
        {
            "id": 24,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 24: Dịch câu sau sang tiếng Đức:\n„Huế nằm ở trung tâm của Việt Nam.“",
            "options": null,
            "correct_answer": "Hue liegt im Zentrum von Vietnam.",
            "explanation": "„ở trung tâm của Việt Nam“ = „im Zentrum von Vietnam“ (hoặc „in der Mitte von Vietnam“) -> Đáp án: Hue liegt im Zentrum von Vietnam..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Hue liegt im Zentrum von Vietnam.",
                    "Hue liegt im Zentrum von Vietnam",
                    "Hue liegt in der Mitte von Vietnam.",
                    "Hue liegt in der Mitte von Vietnam"
                ],
                "audio_text": "Hue liegt im Zentrum von Vietnam.",
                "translation": "Huế nằm ở trung tâm của Việt Nam."
            }
        },
        {
            "id": 25,
            "exercise_type": "trac_nghiem",
            "question": "Câu 25: Chọn giới từ thích hợp:\n„Leipzig liegt ___ Osten von Deutschland.“",
            "options": ["im", "in", "(để trống)"],
            "correct_answer": "im",
            "explanation": "„Osten“ là danh từ viết hoa chỉ hướng Đông, bắt buộc dùng „im“ -> Đáp án: im.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Leipzig liegt im Osten von Deutschland.",
                "translation": "Leipzig nằm ở miền Đông của nước Đức."
            }
        },
        {
            "id": 26,
            "exercise_type": "trac_nghiem",
            "question": "Câu 26: Chọn từ đúng:\n„Griechenland liegt im ___ von Europa.“",
            "options": ["Südosten", "südöstlich"],
            "correct_answer": "Südosten",
            "explanation": "Vì phía trước đã có „im“ nên phải dùng danh từ viết hoa „Südosten“ -> Đáp án: Südosten.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Griechenland liegt im Südosten von Europa.",
                "translation": "Hy Lạp nằm ở miền Đông Nam của châu Âu."
            }
        },
        {
            "id": 27,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 27: Dịch câu sau sang tiếng Việt:\n„Wo liegt Da Nang?“",
            "options": null,
            "correct_answer": "Đà Nẵng nằm ở đâu?",
            "explanation": "„Wo liegt...?“ = nằm ở đâu? -> Đáp án: Đà Nẵng nằm ở đâu?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Đà Nẵng nằm ở đâu?", "Đà Nẵng nằm ở đâu", "Đà Nẵng ở đâu?", "Đà Nẵng ở đâu"],
                "audio_text": "Wo liegt Da Nang?",
                "translation": "Đà Nẵng nằm ở đâu?"
            }
        },
        {
            "id": 28,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 28: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Tokio liegt östlich in Japan.“",
            "options": null,
            "correct_answer": "Tokio liegt im Osten von Japan.",
            "explanation": "Tokyo nằm BÊN TRONG Nhật Bản nên phải dùng „im Osten von Japan“ (không dùng „östlich“ hay „in Japan“) -> Đáp án: Tokio liegt im Osten von Japan..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Tokio liegt im Osten von Japan.",
                    "Tokio liegt im Osten von Japan"
                ],
                "audio_text": "Tokio liegt im Osten von Japan.",
                "translation": "Tokyo nằm ở miền Đông của Nhật Bản."
            }
        },
        {
            "id": 29,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 29: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Nha Trang [1] im [2] von Vietnam.“ (nằm ở / miền Nam)",
            "options": null,
            "correct_answer": "liegt / Süden",
            "explanation": "Động từ chỉ vị trí là „liegt“; danh từ hướng Nam viết hoa là „Süden“ -> Đáp án: liegt / Süden.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Nha Trang [1] im [2] von Vietnam.",
                "accepted_answers": ["liegt / Süden", "liegt/Süden", "liegt Süden", "liegt / Sueden", "liegt/Sueden", "liegt / süden"],
                "audio_text": "Nha Trang liegt im Süden von Vietnam.",
                "translation": "Nha Trang nằm ở miền Nam của Việt Nam."
            }
        },
        {
            "id": 30,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 30: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Stuttgart liegt südlich von Frankfurt.",
            "explanation": "Trật tự chuẩn: Chủ ngữ (Stuttgart) + liegt + südlich + von + Frankfurt -> Đáp án: Stuttgart liegt südlich von Frankfurt..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["von", "südlich", "liegt", "Stuttgart", "Frankfurt", "."],
                "accepted_answers": [
                    "Stuttgart liegt südlich von Frankfurt.",
                    "Stuttgart liegt südlich von Frankfurt",
                    "Stuttgart liegt suedlich von Frankfurt.",
                    "Stuttgart liegt suedlich von Frankfurt"
                ],
                "audio_text": "Stuttgart liegt südlich von Frankfurt.",
                "translation": "Stuttgart nằm ở phía Nam của Frankfurt."
            }
        },

        # =====================================================================
        # DẠNG 2: MẠO TỪ ARTIKEL (CÂU 31 - 45)
        # =====================================================================
        {
            "id": 31,
            "exercise_type": "trac_nghiem",
            "question": "Câu 31: Chọn mạo từ phủ định thích hợp:\n„Ist das ein Fernseher? — Nein, das ist ___ Fernseher. Das ist ein Laptop.“",
            "options": ["kein", "keine", "ein"],
            "correct_answer": "kein",
            "explanation": "„der Fernseher“ (tivi) mang giống đực, phủ định danh từ giống đực dùng „kein“ -> Đáp án: kein.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Ist das ein Fernseher? Nein, das ist kein Fernseher. Das ist ein Laptop.",
                "translation": "Đây là tivi phải không? Không, đó không phải tivi. Đó là laptop."
            }
        },
        {
            "id": 32,
            "exercise_type": "trac_nghiem",
            "question": "Câu 32: Chọn mạo từ phủ định thích hợp:\n„Ist das eine Brille? — Nein, das ist ___ Brille.“",
            "options": ["kein", "keine", "eine"],
            "correct_answer": "keine",
            "explanation": "„die Brille“ (mắt kính) mang giống cái, phủ định là „keine“ -> Đáp án: keine.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Ist das eine Brille? Nein, das ist keine Brille.",
                "translation": "Đây là mắt kính à? Không, đó không phải mắt kính."
            }
        },
        {
            "id": 33,
            "exercise_type": "dien_khuyet",
            "question": "Câu 33: Điền mạo từ phủ định thích hợp vào chỗ trống:\n„Das sind ___ Bücher. Das sind Hefte.“ (phủ định)",
            "options": null,
            "correct_answer": "keine",
            "explanation": "„Bücher“ là danh từ số nhiều (Plural), phủ định luôn dùng „keine“ -> Đáp án: keine.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["keine"],
                "audio_text": "Das sind keine Bücher. Das sind Hefte.",
                "translation": "Đó không phải là những cuốn sách. Đó là những cuốn vở."
            }
        },
        {
            "id": 34,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 34: Điền 2 mạo từ thích hợp vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Das ist [1] Kuli. [2] Kuli ist blau.“ (một / cái - xác định)",
            "options": null,
            "correct_answer": "ein / Der",
            "explanation": "Lần đầu nhắc đến dùng „ein“ (der Kuli). Lần thứ hai đã xác định dùng „Der“ (viết hoa đầu câu) -> Đáp án: ein / Der.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Das ist [1] Kuli. [2] Kuli ist blau.",
                "accepted_answers": ["ein / Der", "ein/Der", "ein / der", "ein/der", "ein, Der", "ein, der", "ein Der", "ein der"],
                "audio_text": "Das ist ein Kuli. Der Kuli ist blau.",
                "translation": "Đây là một cây bút bi. Cây bút bi màu xanh."
            }
        },
        {
            "id": 35,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 35: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Das ist kein Kamera. Das ist ein Handy.“",
            "options": null,
            "correct_answer": "Das ist keine Kamera. Das ist ein Handy.",
            "explanation": "„die Kamera“ mang giống cái nên phủ định phải là „keine Kamera“ -> Đáp án: Das ist keine Kamera. Das ist ein Handy..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Das ist keine Kamera. Das ist ein Handy.", "Das ist keine Kamera. Das ist ein Handy"],
                "audio_text": "Das ist keine Kamera. Das ist ein Handy.",
                "translation": "Đó không phải máy ảnh. Đó là một chiếc điện thoại."
            }
        },
        {
            "id": 36,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 36: Dịch câu sau sang tiếng Đức:\n„Đó không phải là một cuốn sách.“",
            "options": null,
            "correct_answer": "Das ist kein Buch.",
            "explanation": "„das Buch“ mang giống trung, phủ định là „kein Buch“ -> Đáp án: Das ist kein Buch..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Das ist kein Buch.", "Das ist kein Buch"],
                "audio_text": "Das ist kein Buch.",
                "translation": "Đó không phải là một cuốn sách."
            }
        },
        {
            "id": 37,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 37: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Ist das das Auto von Thomas?",
            "explanation": "Câu hỏi Yes/No đảo „Ist“ lên đầu; mạo từ xác định của „Auto“ là „das“ -> Đáp án: Ist das das Auto von Thomas?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["das", "Ist", "Auto", "von", "Thomas", "?"],
                "accepted_answers": ["Ist das das Auto von Thomas?", "Ist das das Auto von Thomas"],
                "audio_text": "Ist das das Auto von Thomas?",
                "translation": "Đó có phải là xe ô tô của Thomas không?"
            }
        },
        {
            "id": 38,
            "exercise_type": "trac_nghiem",
            "question": "Câu 38: Chọn từ phủ định thích hợp:\n„Wir haben ___ Kinder. Wir sind kinderlos.“",
            "options": ["keine", "kein", "nicht"],
            "correct_answer": "keine",
            "explanation": "„Kinder“ là danh từ số nhiều, phủ định danh từ số nhiều dùng „keine“ -> Đáp án: keine.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Wir haben keine Kinder. Wir sind kinderlos.",
                "translation": "Chúng tôi không có con. Chúng tôi chưa có con."
            }
        },
        {
            "id": 39,
            "exercise_type": "dien_khuyet",
            "question": "Câu 39: Điền mạo từ không xác định thích hợp vào chỗ trống:\n„Hier ist ___ Tasche. Die Tasche ist sehr schön.“ (một)",
            "options": null,
            "correct_answer": "eine",
            "explanation": "„die Tasche“ mang giống cái, nhắc đến lần đầu dùng „eine“ -> Đáp án: eine.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["eine"],
                "audio_text": "Hier ist eine Tasche. Die Tasche ist sehr schön.",
                "translation": "Đây là một chiếc túi. Chiếc túi rất đẹp."
            }
        },
        {
            "id": 40,
            "exercise_type": "dien_khuyet",
            "question": "Câu 40: Điền mạo từ xác định thích hợp vào chỗ trống:\n„Ist das der Stuhl von Anna? — Nein, das ist ___ Stuhl von David.“",
            "options": null,
            "correct_answer": "der",
            "explanation": "Có cụm xác định „von David“ nên chiếc ghế đã xác định, dùng mạo từ giống đực „der“ -> Đáp án: der.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["der"],
                "audio_text": "Ist das der Stuhl von Anna? Nein, das ist der Stuhl von David.",
                "translation": "Đây là ghế của Anna à? Không, đó là ghế của David."
            }
        },
        {
            "id": 41,
            "exercise_type": "dien_khuyet",
            "question": "Câu 41: Điền mạo từ phủ định thích hợp vào chỗ trống:\n„Ist das ein Rucksack? — Nein, das ist ___ Rucksack.“",
            "options": null,
            "correct_answer": "kein",
            "explanation": "„der Rucksack“ mang giống đực nên phủ định dùng „kein“ -> Đáp án: kein.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["kein"],
                "audio_text": "Ist das ein Rucksack? Nein, das ist kein Rucksack.",
                "translation": "Đây là một chiếc ba lô phải không? Không, đó không phải ba lô."
            }
        },
        {
            "id": 42,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 42: Điền 2 mạo từ thích hợp vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Das ist [1] Lampe. [2] Lampe ist hell.“",
            "options": null,
            "correct_answer": "eine / Die",
            "explanation": "„die Lampe“ mang giống cái: lần đầu dùng „eine“, lần sau đã xác định viết hoa đầu câu là „Die“ -> Đáp án: eine / Die.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Das ist [1] Lampe. [2] Lampe ist hell.",
                "accepted_answers": ["eine / Die", "eine/Die", "eine / die", "eine/die", "eine Die", "eine die"],
                "audio_text": "Das ist eine Lampe. Die Lampe ist hell.",
                "translation": "Đây là một chiếc đèn. Chiếc đèn rất sáng."
            }
        },
        {
            "id": 43,
            "exercise_type": "dien_khuyet",
            "question": "Câu 43: Điền mạo từ phủ định thích hợp vào chỗ trống:\n„Sind das Handys? — Nein, das sind ___ Handys.“",
            "options": null,
            "correct_answer": "keine",
            "explanation": "„Handys“ là danh từ số nhiều, phủ định số nhiều luôn dùng „keine“ -> Đáp án: keine.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["keine"],
                "audio_text": "Sind das Handys? Nein, das sind keine Handys.",
                "translation": "Đó là những chiếc điện thoại à? Không, đó không phải những chiếc điện thoại."
            }
        },
        {
            "id": 44,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 44: Dịch câu sau sang tiếng Đức:\n„Đây không phải là một cái bàn.“",
            "options": null,
            "correct_answer": "Das ist kein Tisch.",
            "explanation": "„der Tisch“ mang giống đực, phủ định là „kein Tisch“ -> Đáp án: Das ist kein Tisch..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Das ist kein Tisch.", "Das ist kein Tisch", "Hier ist kein Tisch.", "Dies ist kein Tisch."],
                "audio_text": "Das ist kein Tisch.",
                "translation": "Đây không phải là một cái bàn."
            }
        },
        {
            "id": 45,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 45: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Ist das ein Flasche?“",
            "options": null,
            "correct_answer": "Ist das eine Flasche?",
            "explanation": "„die Flasche“ mang giống cái nên mạo từ không xác định phải là „eine“ -> Đáp án: Ist das eine Flasche?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Ist das eine Flasche?", "Ist das eine Flasche"],
                "audio_text": "Ist das eine Flasche?",
                "translation": "Đó có phải là một cái chai không?"
            }
        },

        # =====================================================================
        # DẠNG 3: ĐỘNG TỪ "SEIN" HIỆN TẠI & QUÁ KHỨ (CÂU 46 - 60)
        # =====================================================================
        {
            "id": 46,
            "exercise_type": "dien_khuyet",
            "question": "Câu 46: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„Heute ___ ich in der Schule.“ (sein)",
            "options": null,
            "correct_answer": "bin",
            "explanation": "Dấu hiệu „Heute“ (hiện tại) đi với ngôi „ich“ chia là „bin“ -> Đáp án: bin.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["bin"],
                "audio_text": "Heute bin ich in der Schule.",
                "translation": "Hôm nay tôi ở trường."
            }
        },
        {
            "id": 47,
            "exercise_type": "dien_khuyet",
            "question": "Câu 47: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„Gestern ___ wir im Kino.“ (sein)",
            "options": null,
            "correct_answer": "waren",
            "explanation": "Dấu hiệu „Gestern“ (quá khứ) đi với ngôi „wir“ chia Präteritum là „waren“ -> Đáp án: waren.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["waren"],
                "audio_text": "Gestern waren wir im Kino.",
                "translation": "Hôm qua chúng tôi ở rạp chiếu phim."
            }
        },
        {
            "id": 48,
            "exercise_type": "dien_khuyet",
            "question": "Câu 48: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„___ du schon mal in Paris?“ (sein)",
            "options": null,
            "correct_answer": "Warst",
            "explanation": "„schon mal“ (đã từng) -> Quá khứ. Ngôi „du“ chia là „warst“, đứng đầu câu viết hoa „Warst“ -> Đáp án: Warst.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Warst", "warst"],
                "audio_text": "Warst du schon mal in Paris?",
                "translation": "Bạn đã từng ở Paris chưa?"
            }
        },
        {
            "id": 49,
            "exercise_type": "trac_nghiem",
            "question": "Câu 49: Chọn dạng đúng của động từ „sein“:\n„Früher ___ er sehr sportlich.“",
            "options": ["ist", "war", "warst"],
            "correct_answer": "war",
            "explanation": "„Früher“ (trước đây) là dấu hiệu quá khứ. Ngôi „er“ chia Präteritum là „war“ -> Đáp án: war.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Früher war er sehr sportlich.",
                "translation": "Trước đây anh ấy rất đam mê thể thao."
            }
        },
        {
            "id": 50,
            "exercise_type": "trac_nghiem",
            "question": "Câu 50: Chọn dạng đúng của động từ „sein“:\n„Wo ___ ihr jetzt?“",
            "options": ["wart", "sind", "seid"],
            "correct_answer": "seid",
            "explanation": "„jetzt“ (bây giờ) là hiện tại. Ngôi „ihr“ chia là „seid“ -> Đáp án: seid.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Wo seid ihr jetzt?",
                "translation": "Bây giờ các bạn đang ở đâu?"
            }
        },
        {
            "id": 51,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 51: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Meine Freunde waren am Wochenende in Italien.",
            "explanation": "Động từ „waren“ luôn đứng ở vị trí số 2; „Meine Freunde“ là số nhiều (sie) -> Đáp án: Meine Freunde waren am Wochenende in Italien..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["in Italien", "Meine Freunde", "am Wochenende", "waren", "."],
                "accepted_answers": [
                    "Meine Freunde waren am Wochenende in Italien.",
                    "Meine Freunde waren am Wochenende in Italien",
                    "Am Wochenende waren meine Freunde in Italien.",
                    "Am Wochenende waren meine Freunde in Italien"
                ],
                "audio_text": "Meine Freunde waren am Wochenende in Italien.",
                "translation": "Cuối tuần trước bạn bè tôi đã ở Ý."
            }
        },
        {
            "id": 52,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 52: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Gestern sind wir in Hamburg.“",
            "options": null,
            "correct_answer": "Gestern waren wir in Hamburg.",
            "explanation": "Có dấu hiệu quá khứ „gestern“ (hôm qua) nên động từ phải chia „waren“, không dùng hiện tại „sind“ -> Đáp án: Gestern waren wir in Hamburg..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Gestern waren wir in Hamburg.",
                    "Gestern waren wir in Hamburg",
                    "Wir waren gestern in Hamburg.",
                    "Wir waren gestern in Hamburg"
                ],
                "audio_text": "Gestern waren wir in Hamburg.",
                "translation": "Hôm qua chúng tôi đã ở Hamburg."
            }
        },
        {
            "id": 53,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 53: Chia động từ „sein“ vào 2 chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Gestern [1] ich in Berlin. Heute [2] ich in München.“ (sein / sein)",
            "options": null,
            "correct_answer": "war / bin",
            "explanation": "Vế đầu có „Gestern“ (quá khứ) -> „war“; vế sau có „Heute“ (hiện tại) -> „bin“ -> Đáp án: war / bin.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Gestern [1] ich in Berlin. Heute [2] ich in München.",
                "accepted_answers": ["war / bin", "war/bin", "war bin", "war, bin"],
                "audio_text": "Gestern war ich in Berlin. Heute bin ich in München.",
                "translation": "Hôm qua tôi ở Berlin. Hôm nay tôi ở München."
            }
        },
        {
            "id": 54,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 54: Dịch câu sau sang tiếng Đức (dùng ngôi Sie lịch sự):\n„Hôm qua ngài ở đâu, ngài Müller?“",
            "options": null,
            "correct_answer": "Wo waren Sie gestern, Herr Müller?",
            "explanation": "Hỏi quá khứ lịch sự với ngôi „Sie“ dùng „waren Sie“ -> Đáp án: Wo waren Sie gestern, Herr Müller?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Wo waren Sie gestern, Herr Müller?",
                    "Wo waren Sie gestern, Herr Müller",
                    "Wo waren Sie gestern Herr Müller?",
                    "Herr Müller, wo waren Sie gestern?",
                    "Herr Müller, wo waren Sie gestern",
                    "Wo waren Sie gestern, Herr Mueller?",
                    "Herr Mueller, wo waren Sie gestern?"
                ],
                "audio_text": "Wo waren Sie gestern, Herr Müller?",
                "translation": "Hôm qua ngài ở đâu, ngài Müller?"
            }
        },
        {
            "id": 55,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 55: Dịch câu sau sang tiếng Việt:\n„Letztes Jahr war sie in Vietnam.“",
            "options": null,
            "correct_answer": "Năm ngoái cô ấy đã ở Việt Nam.",
            "explanation": "„Letztes Jahr“ = Năm ngoái; „war“ = đã ở -> Đáp án: Năm ngoái cô ấy đã ở Việt Nam..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Năm ngoái cô ấy đã ở Việt Nam.",
                    "Năm ngoái cô ấy đã ở Việt Nam",
                    "Cô ấy đã ở Việt Nam vào năm ngoái.",
                    "Cô ấy đã ở Việt Nam năm ngoái.",
                    "Năm ngoái cô ấy ở Việt Nam."
                ],
                "audio_text": "Letztes Jahr war sie in Vietnam.",
                "translation": "Năm ngoái cô ấy đã ở Việt Nam."
            }
        },
        {
            "id": 56,
            "exercise_type": "dien_khuyet",
            "question": "Câu 56: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„Lukas und Mia ___ heute krank.“ (sein)",
            "options": null,
            "correct_answer": "sind",
            "explanation": "Chủ ngữ số nhiều „Lukas und Mia“ + „heute“ (hiện tại) -> „sind“ -> Đáp án: sind.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["sind"],
                "audio_text": "Lukas und Mia sind heute krank.",
                "translation": "Hôm nay Lukas và Mia bị ốm."
            }
        },
        {
            "id": 57,
            "exercise_type": "dien_khuyet",
            "question": "Câu 57: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„___ ihr am Sonntag zu Hause?“ (sein - quá khứ)",
            "options": null,
            "correct_answer": "Wart",
            "explanation": "Quá khứ của „sein“ ở ngôi „ihr“ đứng đầu câu hỏi viết hoa là „Wart“ -> Đáp án: Wart.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Wart", "wart"],
                "audio_text": "Wart ihr am Sonntag zu Hause?",
                "translation": "Chủ nhật vừa rồi các bạn có ở nhà không?"
            }
        },
        {
            "id": 58,
            "exercise_type": "dien_khuyet",
            "question": "Câu 58: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„Das Konzert ___ fantastisch!“ (sein - quá khứ)",
            "options": null,
            "correct_answer": "war",
            "explanation": "Chủ ngữ „Das Konzert“ (ngôi es) ở quá khứ đơn chia là „war“ -> Đáp án: war.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["war"],
                "audio_text": "Das Konzert war fantastisch!",
                "translation": "Buổi hòa nhạc thật tuyệt vời!"
            }
        },
        {
            "id": 59,
            "exercise_type": "dien_khuyet",
            "question": "Câu 59: Chia động từ „sein“ phù hợp với ngữ cảnh:\n„Wo ___ der Schlüssel?“ (sein - hiện tại)",
            "options": null,
            "correct_answer": "ist",
            "explanation": "Chủ ngữ số ít „der Schlüssel“ (ngôi er) ở hiện tại chia là „ist“ -> Đáp án: ist.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["ist"],
                "audio_text": "Wo ist der Schlüssel?",
                "translation": "Chìa khóa ở đâu vậy?"
            }
        },
        {
            "id": 60,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 60: Chia động từ „sein“ vào 2 chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„Früher [1] wir Studenten, jetzt [2] wir Lehrer.“ (sein / sein)",
            "options": null,
            "correct_answer": "waren / sind",
            "explanation": "„Früher“ (trước đây) dùng quá khứ „waren“; „jetzt“ (bây giờ) dùng hiện tại „sind“ -> Đáp án: waren / sind.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "Früher [1] wir Studenten, jetzt [2] wir Lehrer.",
                "accepted_answers": ["waren / sind", "waren/sind", "waren sind", "waren, sind"],
                "audio_text": "Früher waren wir Studenten, jetzt sind wir Lehrer.",
                "translation": "Trước đây chúng tôi là sinh viên, bây giờ chúng tôi là giáo viên."
            }
        },

        # =====================================================================
        # DẠNG 4: QUỐC GIA & NGÔN NGỮ (CÂU 61 - 70)
        # =====================================================================
        {
            "id": 61,
            "exercise_type": "dien_khuyet",
            "question": "Câu 61: Điền tên ngôn ngữ thích hợp vào chỗ trống:\n„Elena kommt aus Spanien. Sie spricht fließend ___.“",
            "options": null,
            "correct_answer": "Spanisch",
            "explanation": "Ngôn ngữ của „Spanien“ (Tây Ban Nha) là „Spanisch“ -> Đáp án: Spanisch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Spanisch", "spanisch"],
                "audio_text": "Elena kommt aus Spanien. Sie spricht fließend Spanisch.",
                "translation": "Elena đến từ Tây Ban Nha. Cô ấy nói tiếng Tây Ban Nha trôi chảy."
            }
        },
        {
            "id": 62,
            "exercise_type": "trac_nghiem",
            "question": "Câu 62: Chọn tên ngôn ngữ đúng:\n„Er wohnt in Ägypten. Seine Muttersprache ist ___.“",
            "options": ["Arabisch", "Ägypte", "Ägyptenisch"],
            "correct_answer": "Arabisch",
            "explanation": "Ngôn ngữ chính thức của Ai Cập (Ägypten) là tiếng Ả Rập: „Arabisch“ -> Đáp án: Arabisch.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Er wohnt in Ägypten. Seine Muttersprache ist Arabisch.",
                "translation": "Anh ấy sống ở Ai Cập. Tiếng mẹ đẻ của anh ấy là tiếng Ả Rập."
            }
        },
        {
            "id": 63,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 63: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Sie kommt aus Griechenland. Sie spricht Grieche.“",
            "options": null,
            "correct_answer": "Sie kommt aus Griechenland. Sie spricht Griechisch.",
            "explanation": "Ngôn ngữ của Hy Lạp là „Griechisch“, không phải „Grieche“ (danh từ chỉ người Hy Lạp) -> Đáp án: Sie kommt aus Griechenland. Sie spricht Griechisch..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Sie kommt aus Griechenland. Sie spricht Griechisch.", "Sie kommt aus Griechenland. Sie spricht Griechisch"],
                "audio_text": "Sie kommt aus Griechenland. Sie spricht Griechisch.",
                "translation": "Cô ấy đến từ Hy Lạp. Cô ấy nói tiếng Hy Lạp."
            }
        },
        {
            "id": 64,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 64: Dịch 2 câu sau sang tiếng Đức:\n„Cô ấy đến từ Thổ Nhĩ Kỳ. Cô ấy nói tiếng Thổ Nhĩ Kỳ.“",
            "options": null,
            "correct_answer": "Sie kommt aus der Türkei. Sie spricht Türkisch.",
            "explanation": "Thổ Nhĩ Kỳ bắt buộc có mạo từ: „aus der Türkei“; ngôn ngữ là „Türkisch“ -> Đáp án: Sie kommt aus der Türkei. Sie spricht Türkisch..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Sie kommt aus der Türkei. Sie spricht Türkisch.",
                    "Sie kommt aus der Türkei. Sie spricht Türkisch",
                    "Sie kommt aus der Tuerkei. Sie spricht Tuerkisch.",
                    "Sie kommt aus der Tuerkei. Sie spricht Tuerkisch"
                ],
                "audio_text": "Sie kommt aus der Türkei. Sie spricht Türkisch.",
                "translation": "Cô ấy đến từ Thổ Nhĩ Kỳ. Cô ấy nói tiếng Thổ Nhĩ Kỳ."
            }
        },
        {
            "id": 65,
            "exercise_type": "noi_o",
            "question": "Câu 65: Nối Quốc gia với Ngôn ngữ tương ứng:",
            "options": null,
            "correct_answer": "Nối đúng 4/4 cặp",
            "explanation": "Quy tắc tạo tên ngôn ngữ thường thêm đuôi -sch hoặc -isch: Deutschland-Deutsch, Frankreich-Französisch, Polen-Polnisch, Italien-Italienisch -> Đáp án: Nối đúng 4/4 cặp.",
            "exp_reward": 15,
            "extra_data": {
                "noi_o_pairs": [
                    {"left": "Deutschland", "right": "Deutsch"},
                    {"left": "Frankreich", "right": "Französisch"},
                    {"left": "Polen", "right": "Polnisch"},
                    {"left": "Italien", "right": "Italienisch"}
                ],
                "audio_text": "Deutschland, Deutsch. Frankreich, Französisch. Polen, Polnisch. Italien, Italienisch.",
                "translation": "Deutschland: Đức — Deutsch: tiếng Đức | Frankreich: Pháp — Französisch: tiếng Pháp | Polen: Ba Lan — Polnisch: tiếng Ba Lan | Italien: Ý — Italienisch: tiếng Ý"
            }
        },
        {
            "id": 66,
            "exercise_type": "dien_khuyet",
            "question": "Câu 66: Điền tên ngôn ngữ thích hợp vào chỗ trống:\n„Anna wohnt in Dänemark. Sie spricht ___.“",
            "options": null,
            "correct_answer": "Dänisch",
            "explanation": "Ngôn ngữ của „Dänemark“ (Đan Mạch) là „Dänisch“ -> Đáp án: Dänisch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Dänisch", "dänisch", "Daenisch", "daenisch"],
                "audio_text": "Anna wohnt in Dänemark. Sie spricht Dänisch.",
                "translation": "Anna sống ở Đan Mạch. Cô ấy nói tiếng Đan Mạch."
            }
        },
        {
            "id": 67,
            "exercise_type": "dien_khuyet",
            "question": "Câu 67: Điền tên ngôn ngữ thích hợp vào chỗ trống:\n„Mario wohnt in Rom, Italien. Er spricht ___.“",
            "options": null,
            "correct_answer": "Italienisch",
            "explanation": "Ngôn ngữ của „Italien“ (Ý) là „Italienisch“ -> Đáp án: Italienisch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Italienisch", "italienisch"],
                "audio_text": "Mario wohnt in Rom, Italien. Er spricht Italienisch.",
                "translation": "Mario sống ở Rome, Ý. Anh ấy nói tiếng Ý."
            }
        },
        {
            "id": 68,
            "exercise_type": "dien_khuyet",
            "question": "Câu 68: Điền tên ngôn ngữ thích hợp vào chỗ trống:\n„In Österreich spricht man ___.“",
            "options": null,
            "correct_answer": "Deutsch",
            "explanation": "Ở nước Áo (Österreich), ngôn ngữ chính thức là tiếng Đức: „Deutsch“ -> Đáp án: Deutsch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Deutsch", "deutsch"],
                "audio_text": "In Österreich spricht man Deutsch.",
                "translation": "Ở Áo người ta nói tiếng Đức."
            }
        },
        {
            "id": 69,
            "exercise_type": "dien_khuyet",
            "question": "Câu 69: Điền tên ngôn ngữ thích hợp vào chỗ trống:\n„Ich komme aus Russland. Ich spreche ___.“",
            "options": null,
            "correct_answer": "Russisch",
            "explanation": "Ngôn ngữ của „Russland“ (Nga) là „Russisch“ -> Đáp án: Russisch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Russisch", "russisch"],
                "audio_text": "Ich komme aus Russland. Ich spreche Russisch.",
                "translation": "Tôi đến từ Nga. Tôi nói tiếng Nga."
            }
        },
        {
            "id": 70,
            "exercise_type": "dien_khuyet",
            "question": "Câu 70: Điền tên ngôn ngữ thích hợp vào chỗ trống:\n„John kommt aus Großbritannien. Er spricht ___.“",
            "options": null,
            "correct_answer": "Englisch",
            "explanation": "Ngôn ngữ của „Großbritannien“ (Vương quốc Anh) là „Englisch“ -> Đáp án: Englisch.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": ["Englisch", "englisch"],
                "audio_text": "John kommt aus Großbritannien. Er spricht Englisch.",
                "translation": "John đến từ Vương quốc Anh. Anh ấy nói tiếng Anh."
            }
        },

        # =====================================================================
        # DẠNG 5: ĐẶT CÂU HỎI W-FRAGEN (CÂU 71 - 85)
        # =====================================================================
        {
            "id": 71,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 71: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi du):\n„Ich komme **aus Russland**.“",
            "options": null,
            "correct_answer": "Woher kommst du?",
            "explanation": "„aus Russland“ chỉ xuất xứ, dùng từ để hỏi „Woher“ ở ngôi du -> Đáp án: Woher kommst du?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ich komme aus Russland.",
                "target_phrase": "aus Russland",
                "accepted_answers": ["Woher kommst du?", "Woher kommst du"],
                "audio_text": "Woher kommst du?",
                "translation": "Bạn đến từ đâu? (Tôi đến từ Nga.)"
            }
        },
        {
            "id": 72,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 72: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi sie):\n„Meine Schwester wohnt **in Berlin**.“",
            "options": null,
            "correct_answer": "Wo wohnt sie?",
            "explanation": "„in Berlin“ chỉ nơi chốn tĩnh, dùng từ để hỏi „Wo“ -> Đáp án: Wo wohnt sie?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Meine Schwester wohnt in Berlin.",
                "target_phrase": "in Berlin",
                "accepted_answers": ["Wo wohnt sie?", "Wo wohnt sie", "Wo wohnt deine Schwester?", "Wo wohnt deine Schwester"],
                "audio_text": "Wo wohnt sie?",
                "translation": "Cô ấy sống ở đâu? (Chị/em gái tôi sống ở Berlin.)"
            }
        },
        {
            "id": 73,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 73: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi ihr):\n„Wir trinken **Kaffee**.“",
            "options": null,
            "correct_answer": "Was trinkt ihr?",
            "explanation": "„Kaffee“ là đồ vật, dùng từ để hỏi „Was“ ở ngôi ihr (chấp nhận cả „Was möchtet ihr trinken?“) -> Đáp án: Was trinkt ihr?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Wir trinken Kaffee.",
                "target_phrase": "Kaffee",
                "accepted_answers": [
                    "Was trinkt ihr?",
                    "Was trinkt ihr",
                    "Was möchtet ihr trinken?",
                    "Was möchtet ihr trinken",
                    "Was moechtet ihr trinken?",
                    "Was moechtet ihr trinken",
                    "Was wollt ihr trinken?",
                    "Was wollt ihr trinken"
                ],
                "audio_text": "Was trinkt ihr?",
                "translation": "Các bạn uống gì? (Chúng tôi uống cà phê.)"
            }
        },
        {
            "id": 74,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 74: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi Sie lịch sự):\n„Mein Name ist **David**.“",
            "options": null,
            "correct_answer": "Wie heißen Sie?",
            "explanation": "Hỏi tên lịch sự ngôi Sie dùng „Wie heißen Sie?“ hoặc „Wie ist Ihr Name?“ -> Đáp án: Wie heißen Sie?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Mein Name ist David.",
                "target_phrase": "David",
                "accepted_answers": ["Wie heißen Sie?", "Wie heißen Sie", "Wie heissen Sie?", "Wie heissen Sie", "Wie ist Ihr Name?", "Wie ist Ihr Name"],
                "audio_text": "Wie heißen Sie?",
                "translation": "Tên ngài là gì? (Tên tôi là David.)"
            }
        },
        {
            "id": 75,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 75: Đặt câu hỏi cho cụm từ in đậm (hỏi vị trí):\n„München liegt **im Süden von Deutschland**.“",
            "options": null,
            "correct_answer": "Wo liegt München?",
            "explanation": "Hỏi vị trí địa lý dùng từ để hỏi „Wo“ -> Đáp án: Wo liegt München?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "München liegt im Süden von Deutschland.",
                "target_phrase": "im Süden von Deutschland",
                "accepted_answers": ["Wo liegt München?", "Wo liegt München", "Wo liegt Muenchen?", "Wo liegt Muenchen"],
                "audio_text": "Wo liegt München?",
                "translation": "München nằm ở đâu?"
            }
        },
        {
            "id": 76,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 76: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi du):\n„Gestern war ich **im Kino**.“",
            "options": null,
            "correct_answer": "Wo warst du gestern?",
            "explanation": "„im Kino“ chỉ địa điểm dùng „Wo“; quá khứ của „sein“ ở ngôi du là „warst“ -> Đáp án: Wo warst du gestern?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Gestern war ich im Kino.",
                "target_phrase": "im Kino",
                "accepted_answers": ["Wo warst du gestern?", "Wo warst du gestern", "Wo warst du?", "Wo warst du"],
                "audio_text": "Wo warst du gestern?",
                "translation": "Hôm qua bạn đã ở đâu?"
            }
        },
        {
            "id": 77,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 77: Đặt câu hỏi Yes/No cho câu trả lời sau (hỏi ở ngôi du):\n„**Ja**, ich war schon mal in Spanien.“",
            "options": null,
            "correct_answer": "Warst du schon mal in Spanien?",
            "explanation": "Trả lời „Ja“ -> Đặt câu hỏi Yes/No bằng cách đảo động từ quá khứ „Warst“ lên đầu câu -> Đáp án: Warst du schon mal in Spanien?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ja, ich war schon mal in Spanien.",
                "target_phrase": "Ja",
                "accepted_answers": ["Warst du schon mal in Spanien?", "Warst du schon mal in Spanien"],
                "audio_text": "Warst du schon mal in Spanien?",
                "translation": "Bạn đã từng ở Tây Ban Nha chưa?"
            }
        },
        {
            "id": 78,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 78: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi ihr):\n„Wir treffen uns **um 15 Uhr**.“",
            "options": null,
            "correct_answer": "Wann trefft ihr euch?",
            "explanation": "„um 15 Uhr“ chỉ thời gian nên dùng „Wann“ hoặc „Um wie viel Uhr“ -> Đáp án: Wann trefft ihr euch?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Wir treffen uns um 15 Uhr.",
                "target_phrase": "um 15 Uhr",
                "accepted_answers": ["Wann trefft ihr euch?", "Wann trefft ihr euch", "Um wie viel Uhr trefft ihr euch?", "Um wie viel Uhr trefft ihr euch"],
                "audio_text": "Wann trefft ihr euch?",
                "translation": "Các bạn gặp nhau khi nào?"
            }
        },
        {
            "id": 79,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 79: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi er):\n„Er lernt **Deutsch**.“",
            "options": null,
            "correct_answer": "Was lernt er?",
            "explanation": "„Deutsch“ là đối tượng học nên hỏi bằng „Was“ -> Đáp án: Was lernt er?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Er lernt Deutsch.",
                "target_phrase": "Deutsch",
                "accepted_answers": ["Was lernt er?", "Was lernt er"],
                "audio_text": "Was lernt er?",
                "translation": "Anh ấy học gì?"
            }
        },
        {
            "id": 80,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 80: Đặt câu hỏi Yes/No cho câu trả lời sau:\n„**Nein**, das ist kein Radio.“",
            "options": null,
            "correct_answer": "Ist das ein Radio?",
            "explanation": "Câu trả lời phủ định „Nein, das ist kein Radio.“ tương ứng câu hỏi khẳng định „Ist das ein Radio?“ -> Đáp án: Ist das ein Radio?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Nein, das ist kein Radio.",
                "target_phrase": "Nein",
                "accepted_answers": ["Ist das ein Radio?", "Ist das ein Radio"],
                "audio_text": "Ist das ein Radio?",
                "translation": "Đó là một cái đài phải không?"
            }
        },
        {
            "id": 81,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 81: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi Sie lịch sự):\n„Ich spreche **Spanisch und Englisch**.“",
            "options": null,
            "correct_answer": "Welche Sprachen sprechen Sie?",
            "explanation": "Hỏi nói những ngôn ngữ nào dùng „Welche Sprachen sprechen Sie?“ -> Đáp án: Welche Sprachen sprechen Sie?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ich spreche Spanisch und Englisch.",
                "target_phrase": "Spanisch und Englisch",
                "accepted_answers": ["Welche Sprachen sprechen Sie?", "Welche Sprachen sprechen Sie", "Was sprechen Sie?", "Was sprechen Sie"],
                "audio_text": "Welche Sprachen sprechen Sie?",
                "translation": "Ngài nói những ngôn ngữ nào?"
            }
        },
        {
            "id": 82,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 82: Đặt câu hỏi Yes/No cho câu trả lời sau:\n„**Ja**, die Lampe ist neu.“",
            "options": null,
            "correct_answer": "Ist die Lampe neu?",
            "explanation": "Trả lời „Ja“ -> Đảo động từ „Ist“ lên đầu thành „Ist die Lampe neu?“ -> Đáp án: Ist die Lampe neu?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Ja, die Lampe ist neu.",
                "target_phrase": "Ja",
                "accepted_answers": ["Ist die Lampe neu?", "Ist die Lampe neu"],
                "audio_text": "Ist die Lampe neu?",
                "translation": "Chiếc đèn còn mới phải không?"
            }
        },
        {
            "id": 83,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 83: Đặt câu hỏi cho cụm từ in đậm (hỏi ở ngôi ihr):\n„Früher waren wir **in Hanoi**.“",
            "options": null,
            "correct_answer": "Wo wart ihr früher?",
            "explanation": "„in Hanoi“ chỉ địa điểm dùng „Wo“; quá khứ ngôi ihr là „wart“ -> Đáp án: Wo wart ihr früher?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Früher waren wir in Hanoi.",
                "target_phrase": "in Hanoi",
                "accepted_answers": ["Wo wart ihr früher?", "Wo wart ihr früher", "Wo wart ihr frueher?", "Wo wart ihr frueher"],
                "audio_text": "Wo wart ihr früher?",
                "translation": "Trước đây các bạn đã ở đâu?"
            }
        },
        {
            "id": 84,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 84: Đặt câu hỏi cho cụm từ in đậm:\n„Das ist **ein Füller**.“",
            "options": null,
            "correct_answer": "Was ist das?",
            "explanation": "„ein Füller“ là đồ vật nên hỏi bằng „Was ist das?“ -> Đáp án: Was ist das?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Das ist ein Füller.",
                "target_phrase": "ein Füller",
                "accepted_answers": ["Was ist das?", "Was ist das"],
                "audio_text": "Was ist das?",
                "translation": "Đây là cái gì vậy?"
            }
        },
        {
            "id": 85,
            "exercise_type": "viet_lai_cau_w",
            "question": "Câu 85: Đặt câu hỏi cho cụm từ in đậm:\n„Sie kommt **aus der Türkei**.“",
            "options": null,
            "correct_answer": "Woher kommt sie?",
            "explanation": "„aus der Türkei“ chỉ nơi xuất xứ nên hỏi bằng „Woher kommt sie?“ -> Đáp án: Woher kommt sie?.",
            "exp_reward": 15,
            "extra_data": {
                "source_sentence": "Sie kommt aus der Türkei.",
                "target_phrase": "aus der Türkei",
                "accepted_answers": ["Woher kommt sie?", "Woher kommt sie"],
                "audio_text": "Woher kommt sie?",
                "translation": "Cô ấy đến từ đâu?"
            }
        },

        # =====================================================================
        # DẠNG 6: NGHE CHÉP CHÍNH TẢ - DICTATION MODE (CÂU 86 - 95)
        # =====================================================================
        {
            "id": 86,
            "exercise_type": "nghe_dien",
            "question": "Câu 86: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Wo waren Sie gestern, Herr Müller?",
            "explanation": "Câu hỏi quá khứ trang trọng: „Wo waren Sie gestern, Herr Müller?“ -> Đáp án: Wo waren Sie gestern, Herr Müller?.",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Wo waren Sie gestern, Herr Müller?",
                "full_sentence": "Wo waren Sie gestern, Herr Müller?",
                "dictation_mode": True,
                "translation": "Hôm qua ngài ở đâu, ngài Müller?",
                "accepted_answers": [
                    "Wo waren Sie gestern, Herr Müller?",
                    "Wo waren Sie gestern, Herr Müller",
                    "Wo waren Sie gestern Herr Müller?",
                    "Wo waren Sie gestern Herr Müller",
                    "Wo waren Sie gestern, Herr Mueller?",
                    "Wo waren Sie gestern Herr Mueller"
                ]
            }
        },
        {
            "id": 87,
            "exercise_type": "nghe_dien",
            "question": "Câu 87: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Paris liegt westlich von Deutschland.",
            "explanation": "Tính từ hướng „westlich“ không đi kèm „im“: „Paris liegt westlich von Deutschland.“ -> Đáp án: Paris liegt westlich von Deutschland..",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Paris liegt westlich von Deutschland.",
                "full_sentence": "Paris liegt westlich von Deutschland.",
                "dictation_mode": True,
                "translation": "Paris nằm ở phía Tây của nước Đức.",
                "accepted_answers": ["Paris liegt westlich von Deutschland.", "Paris liegt westlich von Deutschland"]
            }
        },
        {
            "id": 88,
            "exercise_type": "nghe_dien",
            "question": "Câu 88: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Das ist keine Kamera. Das ist ein Handy.",
            "explanation": "Phủ định „die Kamera“ dùng „keine“: „Das ist keine Kamera. Das ist ein Handy.“ -> Đáp án: Das ist keine Kamera. Das ist ein Handy..",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Das ist keine Kamera. Das ist ein Handy.",
                "full_sentence": "Das ist keine Kamera. Das ist ein Handy.",
                "dictation_mode": True,
                "translation": "Đó không phải máy ảnh. Đó là một chiếc điện thoại.",
                "accepted_answers": [
                    "Das ist keine Kamera. Das ist ein Handy.",
                    "Das ist keine Kamera. Das ist ein Handy",
                    "Das ist keine Kamera Das ist ein Handy"
                ]
            }
        },
        {
            "id": 89,
            "exercise_type": "nghe_dien",
            "question": "Câu 89: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Ich war schon mal in Italien.",
            "explanation": "Quá khứ của „sein“ ngôi ich là „war“: „Ich war schon mal in Italien.“ -> Đáp án: Ich war schon mal in Italien..",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Ich war schon mal in Italien.",
                "full_sentence": "Ich war schon mal in Italien.",
                "dictation_mode": True,
                "translation": "Tôi đã từng ở Ý.",
                "accepted_answers": ["Ich war schon mal in Italien.", "Ich war schon mal in Italien"]
            }
        },
        {
            "id": 90,
            "exercise_type": "nghe_dien",
            "question": "Câu 90: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Welche Sprachen sprechen Sie?",
            "explanation": "Câu hỏi ngôn ngữ trang trọng: „Welche Sprachen sprechen Sie?“ -> Đáp án: Welche Sprachen sprechen Sie?.",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Welche Sprachen sprechen Sie?",
                "full_sentence": "Welche Sprachen sprechen Sie?",
                "dictation_mode": True,
                "translation": "Ngài nói những ngôn ngữ nào?",
                "accepted_answers": ["Welche Sprachen sprechen Sie?", "Welche Sprachen sprechen Sie"]
            }
        },
        {
            "id": 91,
            "exercise_type": "nghe_dien",
            "question": "Câu 91: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Sie kommt aus der Türkei.",
            "explanation": "Thổ Nhĩ Kỳ dùng mạo từ „aus der Türkei“: „Sie kommt aus der Türkei.“ -> Đáp án: Sie kommt aus der Türkei..",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Sie kommt aus der Türkei.",
                "full_sentence": "Sie kommt aus der Türkei.",
                "dictation_mode": True,
                "translation": "Cô ấy đến từ Thổ Nhĩ Kỳ.",
                "accepted_answers": ["Sie kommt aus der Türkei.", "Sie kommt aus der Türkei", "Sie kommt aus der Tuerkei.", "Sie kommt aus der Tuerkei"]
            }
        },
        {
            "id": 92,
            "exercise_type": "nghe_dien",
            "question": "Câu 92: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "München liegt im Süden von Deutschland.",
            "explanation": "Danh từ hướng đi với „im“: „München liegt im Süden von Deutschland.“ -> Đáp án: München liegt im Süden von Deutschland..",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "München liegt im Süden von Deutschland.",
                "full_sentence": "München liegt im Süden von Deutschland.",
                "dictation_mode": True,
                "translation": "München nằm ở miền Nam nước Đức.",
                "accepted_answers": [
                    "München liegt im Süden von Deutschland.",
                    "München liegt im Süden von Deutschland",
                    "Muenchen liegt im Sueden von Deutschland.",
                    "Muenchen liegt im Sueden von Deutschland"
                ]
            }
        },
        {
            "id": 93,
            "exercise_type": "nghe_dien",
            "question": "Câu 93: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Trinken wir zusammen Kaffee?",
            "explanation": "Câu rủ lịch sự: „Trinken wir zusammen Kaffee?“ -> Đáp án: Trinken wir zusammen Kaffee?.",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Trinken wir zusammen Kaffee?",
                "full_sentence": "Trinken wir zusammen Kaffee?",
                "dictation_mode": True,
                "translation": "Chúng ta cùng uống cà phê nhé?",
                "accepted_answers": ["Trinken wir zusammen Kaffee?", "Trinken wir zusammen Kaffee"]
            }
        },
        {
            "id": 94,
            "exercise_type": "nghe_dien",
            "question": "Câu 94: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Entschuldigung, ist hier frei?",
            "explanation": "Câu giao tiếp quen thuộc ở quán: „Entschuldigung, ist hier frei?“ -> Đáp án: Entschuldigung, ist hier frei?.",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Entschuldigung, ist hier frei?",
                "full_sentence": "Entschuldigung, ist hier frei?",
                "dictation_mode": True,
                "translation": "Xin lỗi, chỗ này còn trống không?",
                "accepted_answers": [
                    "Entschuldigung, ist hier frei?",
                    "Entschuldigung, ist hier frei",
                    "Entschuldigung ist hier frei?",
                    "Entschuldigung ist hier frei"
                ]
            }
        },
        {
            "id": 95,
            "exercise_type": "nghe_dien",
            "question": "Câu 95: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Früher war mein Vater Arzt.",
            "explanation": "„Früher“ đi với quá khứ „war“: „Früher war mein Vater Arzt.“ -> Đáp án: Früher war mein Vater Arzt..",
            "exp_reward": 15,
            "extra_data": {
                "audio_text": "Früher war mein Vater Arzt.",
                "full_sentence": "Früher war mein Vater Arzt.",
                "dictation_mode": True,
                "translation": "Trước đây bố tôi là bác sĩ.",
                "accepted_answers": ["Früher war mein Vater Arzt.", "Früher war mein Vater Arzt", "Frueher war mein Vater Arzt.", "Frueher war mein Vater Arzt"]
            }
        },

        # =====================================================================
        # DẠNG 7: DỊCH CÂU VIỆT <-> ĐỨC (CÂU 96 - 105)
        # =====================================================================
        {
            "id": 96,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 96: Dịch câu sau sang tiếng Đức:\n„Hôm qua tôi đã ở Berlin.“",
            "options": null,
            "correct_answer": "Gestern war ich in Berlin.",
            "explanation": "Trạng ngữ thời gian „Gestern“ -> Quá khứ „war“ (Gestern war ich in Berlin. hoặc Ich war gestern in Berlin.) -> Đáp án: Gestern war ich in Berlin..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Gestern war ich in Berlin.",
                    "Gestern war ich in Berlin",
                    "Ich war gestern in Berlin.",
                    "Ich war gestern in Berlin"
                ],
                "audio_text": "Gestern war ich in Berlin.",
                "translation": "Hôm qua tôi đã ở Berlin."
            }
        },
        {
            "id": 97,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 97: Dịch câu sau sang tiếng Đức:\n„Bạn đến từ đâu vậy David?“",
            "options": null,
            "correct_answer": "Woher kommst du, David?",
            "explanation": "Câu hỏi xuất xứ ngôi thân mật „du“ -> Đáp án: Woher kommst du, David?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Woher kommst du, David?", "Woher kommst du, David", "Woher kommst du David?", "Woher kommst du David"],
                "audio_text": "Woher kommst du, David?",
                "translation": "Bạn đến từ đâu vậy David?"
            }
        },
        {
            "id": 98,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 98: Dịch câu sau sang tiếng Việt:\n„Fährst du am Wochenende nach Polen?“",
            "options": null,
            "correct_answer": "Cuối tuần bạn có đi Ba Lan không?",
            "explanation": "Đi bằng phương tiện đến quốc gia dùng „fahren nach“ -> Đáp án: Cuối tuần bạn có đi Ba Lan không?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Cuối tuần bạn có đi Ba Lan không?",
                    "Cuối tuần bạn có đi Ba Lan không",
                    "Bạn có đi Ba Lan vào cuối tuần không?",
                    "Bạn có đi Ba Lan vào cuối tuần không",
                    "Cuối tuần cậu có đi Ba Lan không?",
                    "Bạn có lái xe đi Ba Lan vào cuối tuần không?"
                ],
                "audio_text": "Fährst du am Wochenende nach Polen?",
                "translation": "Cuối tuần bạn có đi Ba Lan không?"
            }
        },
        {
            "id": 99,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 99: Dịch câu sau sang tiếng Đức (dùng Danh từ hướng):\n„Cần Thơ nằm ở miền Nam của Việt Nam.“",
            "options": null,
            "correct_answer": "Can Tho liegt im Süden von Vietnam.",
            "explanation": "Miền Nam (danh từ) là „im Süden“ -> Đáp án: Can Tho liegt im Süden von Vietnam..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Can Tho liegt im Süden von Vietnam.",
                    "Can Tho liegt im Süden von Vietnam",
                    "Can Tho liegt im Sueden von Vietnam.",
                    "Can Tho liegt im Sueden von Vietnam"
                ],
                "audio_text": "Can Tho liegt im Süden von Vietnam.",
                "translation": "Cần Thơ nằm ở miền Nam của Việt Nam."
            }
        },
        {
            "id": 100,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 100: Dịch câu giao tiếp sau sang tiếng Việt:\n„Das klingt gut! Viel Spaß!“",
            "options": null,
            "correct_answer": "Nghe hay đấy! Chúc vui vẻ nhé!",
            "explanation": "Cụm từ giao tiếp phản hồi sự hào hứng -> Đáp án: Nghe hay đấy! Chúc vui vẻ nhé!.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Nghe hay đấy! Chúc vui vẻ nhé!",
                    "Nghe hay đấy! Chúc vui vẻ nhé",
                    "Nghe tuyệt đấy! Chúc vui vẻ!",
                    "Nghe tuyệt đấy! Chúc vui vẻ nhé!",
                    "Nghe hay quá! Chúc vui vẻ!"
                ],
                "audio_text": "Das klingt gut! Viel Spaß!",
                "translation": "Nghe hay đấy! Chúc vui vẻ nhé!"
            }
        },
        {
            "id": 101,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 101: Dịch câu sau sang tiếng Việt:\n„Was möchtet ihr trinken?“",
            "options": null,
            "correct_answer": "Các bạn muốn uống gì?",
            "explanation": "„ihr“ = các bạn, „möchtet ... trinken“ = muốn uống -> Đáp án: Các bạn muốn uống gì?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Các bạn muốn uống gì?", "Các bạn muốn uống gì", "Các bạn muốn uống gì ạ?", "Các cậu muốn uống gì?"],
                "audio_text": "Was möchtet ihr trinken?",
                "translation": "Các bạn muốn uống gì?"
            }
        },
        {
            "id": 102,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 102: Dịch 2 câu sau sang tiếng Đức:\n„Đó không phải là mắt kính. Đó là cái chai.“",
            "options": null,
            "correct_answer": "Das ist keine Brille. Das ist eine Flasche.",
            "explanation": "„die Brille“ (giống cái -> keine Brille) và „die Flasche“ (giống cái -> eine Flasche) -> Đáp án: Das ist keine Brille. Das ist eine Flasche..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Das ist keine Brille. Das ist eine Flasche.", "Das ist keine Brille. Das ist eine Flasche"],
                "audio_text": "Das ist keine Brille. Das ist eine Flasche.",
                "translation": "Đó không phải là mắt kính. Đó là cái chai."
            }
        },
        {
            "id": 103,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 103: Dịch câu sau sang tiếng Đức:\n„Trước đây chúng tôi là sinh viên.“",
            "options": null,
            "correct_answer": "Früher waren wir Studenten.",
            "explanation": "„Früher“ (trước đây) đi với quá khứ „waren“ ở vị trí số 2 -> Đáp án: Früher waren wir Studenten..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Früher waren wir Studenten.",
                    "Früher waren wir Studenten",
                    "Wir waren früher Studenten.",
                    "Wir waren früher Studenten",
                    "Frueher waren wir Studenten.",
                    "Wir waren frueher Studenten."
                ],
                "audio_text": "Früher waren wir Studenten.",
                "translation": "Trước đây chúng tôi là sinh viên."
            }
        },
        {
            "id": 104,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 104: Dịch câu sau sang tiếng Việt:\n„Sie spricht Französisch und Englisch.“",
            "options": null,
            "correct_answer": "Cô ấy nói tiếng Pháp và tiếng Anh.",
            "explanation": "„spricht“ chia theo ngôi „sie“ số ít (cô ấy), nói 2 ngôn ngữ Pháp và Anh -> Đáp án: Cô ấy nói tiếng Pháp và tiếng Anh..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Cô ấy nói tiếng Pháp và tiếng Anh.",
                    "Cô ấy nói tiếng Pháp và tiếng Anh",
                    "Chị ấy nói tiếng Pháp và tiếng Anh.",
                    "Cô ấy nói được tiếng Pháp và tiếng Anh."
                ],
                "audio_text": "Sie spricht Französisch und Englisch.",
                "translation": "Cô ấy nói tiếng Pháp và tiếng Anh."
            }
        },
        {
            "id": 105,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 105: Dịch câu sau sang tiếng Đức (lịch sự):\n„Tên của ngài là gì?“",
            "options": null,
            "correct_answer": "Wie ist Ihr Name?",
            "explanation": "Hỏi tên lịch sự dùng „Wie ist Ihr Name?“ hoặc „Wie heißen Sie?“ -> Đáp án: Wie ist Ihr Name?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ["Wie ist Ihr Name?", "Wie ist Ihr Name", "Wie heißen Sie?", "Wie heißen Sie", "Wie heissen Sie?", "Wie heissen Sie"],
                "audio_text": "Wie ist Ihr Name?",
                "translation": "Tên của ngài là gì?"
            }
        },

        # =====================================================================
        # DẠNG 8: SẮP XẾP TỪ THÀNH CÂU (CÂU 106 - 115)
        # =====================================================================
        {
            "id": 106,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 106: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Gestern waren wir im Theater.",
            "explanation": "Có thể đặt „Gestern“ lên đầu rồi đảo động từ „waren“ (hoặc „Wir waren gestern im Theater.“) -> Đáp án: Gestern waren wir im Theater..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["gestern", "wir", "im Theater", "waren", "."],
                "accepted_answers": [
                    "Gestern waren wir im Theater.",
                    "Gestern waren wir im Theater",
                    "Wir waren gestern im Theater.",
                    "Wir waren gestern im Theater"
                ],
                "audio_text": "Gestern waren wir im Theater.",
                "translation": "Hôm qua chúng tôi đã ở rạp hát."
            }
        },
        {
            "id": 107,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 107: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Warst du schon mal in Deutschland?",
            "explanation": "Câu hỏi Yes/No đảo động từ quá khứ „Warst“ lên vị trí 1 -> Đáp án: Warst du schon mal in Deutschland?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["du", "mal", "Warst", "schon", "in Deutschland", "?"],
                "accepted_answers": ["Warst du schon mal in Deutschland?", "Warst du schon mal in Deutschland"],
                "audio_text": "Warst du schon mal in Deutschland?",
                "translation": "Bạn đã từng ở Đức chưa?"
            }
        },
        {
            "id": 108,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 108: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Sie kommt aus der Türkei.",
            "explanation": "Thổ Nhĩ Kỳ bắt buộc có mạo từ „der“ sau „aus“ -> Đáp án: Sie kommt aus der Türkei..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["aus", "kommt", "der", "Sie", "Türkei", "."],
                "accepted_answers": [
                    "Sie kommt aus der Türkei.",
                    "Sie kommt aus der Türkei",
                    "Sie kommt aus der Tuerkei.",
                    "Sie kommt aus der Tuerkei"
                ],
                "audio_text": "Sie kommt aus der Türkei.",
                "translation": "Cô ấy đến từ Thổ Nhĩ Kỳ."
            }
        },
        {
            "id": 109,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 109: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "München liegt im Süden von Deutschland.",
            "explanation": "Chủ ngữ + liegt + im Süden + von + quốc gia -> Đáp án: München liegt im Süden von Deutschland..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["liegt", "München", "im Süden", "von", "Deutschland", "."],
                "accepted_answers": [
                    "München liegt im Süden von Deutschland.",
                    "München liegt im Süden von Deutschland",
                    "Muenchen liegt im Sueden von Deutschland.",
                    "Muenchen liegt im Sueden von Deutschland"
                ],
                "audio_text": "München liegt im Süden von Deutschland.",
                "translation": "München nằm ở miền Nam nước Đức."
            }
        },
        {
            "id": 110,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 110: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Welche Sprachen sprechen Sie?",
            "explanation": "Từ để hỏi kép „Welche Sprachen“ + động từ „sprechen“ + ngôi „Sie“ -> Đáp án: Welche Sprachen sprechen Sie?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["sprechen", "Welche", "Sie", "Sprachen", "?"],
                "accepted_answers": ["Welche Sprachen sprechen Sie?", "Welche Sprachen sprechen Sie"],
                "audio_text": "Welche Sprachen sprechen Sie?",
                "translation": "Ngài nói những ngôn ngữ nào?"
            }
        },
        {
            "id": 111,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 111: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Das ist kein Buch.",
            "explanation": "„das Buch“ giống trung dùng phủ định „kein“ -> Đáp án: Das ist kein Buch..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["ist", "Das", "kein", "Buch", "."],
                "accepted_answers": ["Das ist kein Buch.", "Das ist kein Buch"],
                "audio_text": "Das ist kein Buch.",
                "translation": "Đây không phải là một cuốn sách."
            }
        },
        {
            "id": 112,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 112: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Ist die Lampe neu?",
            "explanation": "Câu hỏi Yes/No đảo động từ „Ist“ lên đầu câu -> Đáp án: Ist die Lampe neu?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["die Lampe", "Ist", "neu", "?"],
                "accepted_answers": ["Ist die Lampe neu?", "Ist die Lampe neu"],
                "audio_text": "Ist die Lampe neu?",
                "translation": "Chiếc đèn còn mới phải không?"
            }
        },
        {
            "id": 113,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 113: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh:",
            "options": null,
            "correct_answer": "Trinken wir zusammen Kaffee?",
            "explanation": "Câu hỏi rủ rê với ngôi „wir“ đảo động từ „Trinken“ lên đầu -> Đáp án: Trinken wir zusammen Kaffee?.",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["wir", "Trinken", "Kaffee", "zusammen", "?"],
                "accepted_answers": ["Trinken wir zusammen Kaffee?", "Trinken wir zusammen Kaffee"],
                "audio_text": "Trinken wir zusammen Kaffee?",
                "translation": "Chúng ta cùng uống cà phê nhé?"
            }
        },
        {
            "id": 114,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 114: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Früher war mein Vater Arzt.",
            "explanation": "„Früher“ ở đầu câu, động từ „war“ đứng ở vị trí 2 -> Đáp án: Früher war mein Vater Arzt..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["mein Vater", "war", "Früher", "Arzt", "."],
                "accepted_answers": [
                    "Früher war mein Vater Arzt.",
                    "Früher war mein Vater Arzt",
                    "Frueher war mein Vater Arzt.",
                    "Mein Vater war früher Arzt."
                ],
                "audio_text": "Früher war mein Vater Arzt.",
                "translation": "Trước đây bố tôi là bác sĩ."
            }
        },
        {
            "id": 115,
            "exercise_type": "sap_xep_cau",
            "question": "Câu 115: Sắp xếp các từ sau thành câu hoàn chỉnh:",
            "options": null,
            "correct_answer": "Hamburg liegt nördlich von Hannover.",
            "explanation": "Thực tế địa lý: Hamburg (53.55°N) nằm ở phía Bắc của Hannover (52.37°N), tính từ „nördlich“ không có „im“ -> Đáp án: Hamburg liegt nördlich von Hannover..",
            "exp_reward": 10,
            "extra_data": {
                "tokens": ["nördlich", "liegt", "Hannover", "von", "Hamburg", "."],
                "accepted_answers": [
                    "Hamburg liegt nördlich von Hannover.",
                    "Hamburg liegt nördlich von Hannover",
                    "Hamburg liegt noerdlich von Hannover.",
                    "Hamburg liegt noerdlich von Hannover"
                ],
                "audio_text": "Hamburg liegt nördlich von Hannover.",
                "translation": "Hamburg nằm ở phía Bắc của Hannover."
            }
        },

        # =====================================================================
        # DẠNG 9: SẮP XẾP HỘI THOẠI LOGIC (CÂU 116 - 125)
        # =====================================================================
        {
            "id": 116,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 116: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Quán Cafe - Làm quen:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Xin phép ngồi -> Đồng ý -> Cảm ơn & giới thiệu bản thân -> Giới thiệu lại -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Gast", "text": "Entschuldigung, ist hier frei?"},
                    {"id": 2, "speaker": "Anna", "text": "Ja klar, bitte. Setzen Sie sich."},
                    {"id": 3, "speaker": "Gast", "text": "Danke. Ich bin John aus Frankreich, und du?"},
                    {"id": 4, "speaker": "Anna", "text": "Ich heiße Anna. Ich komme aus Polen."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Entschuldigung, ist hier frei? Ja klar, bitte. Setzen Sie sich. Danke. Ich bin John aus Frankreich, und du? Ich heiße Anna. Ich komme aus Polen.",
                "translation": "- Khách: Xin lỗi, chỗ này còn trống không?\n- Anna: Vâng tất nhiên, xin mời. Ngài hãy ngồi đi.\n- Khách: Cảm ơn. Tôi là John đến từ Pháp, còn bạn?\n- Anna: Tôi tên là Anna. Tôi đến từ Ba Lan."
            }
        },
        {
            "id": 117,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 117: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Rủ rê bạn bè:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5, 6",
            "explanation": "Trình tự logic: Hỏi giờ gặp -> Trả lời -> Hỏi làm gì -> Uống cà phê ăn bánh -> Chúc vui -> Cảm ơn -> Đáp án: 1, 2, 3, 4, 5, 6.",
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
                "audio_text": "Hallo! Wann triffst du heute deine Freunde? Hallo! Wir treffen uns um 15 Uhr im Café. Was macht ihr dort? Wir trinken Kaffee und essen Kuchen. Das klingt gut! Viel Spaß! Danke!",
                "translation": "- Lukas: Chào bạn! Hôm nay khi nào bạn gặp bạn bè?\n- Paul: Chào! Chúng tôi gặp nhau lúc 15 giờ ở quán cà phê.\n- Lukas: Các bạn làm gì ở đó?\n- Paul: Chúng tôi uống cà phê và ăn bánh ngọt.\n- Lukas: Nghe hay đấy! Chúc vui vẻ!\n- Paul: Cảm ơn!"
            }
        },
        {
            "id": 118,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 118: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Hỏi đường / Vị trí:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi vị trí chung -> Trả lời tên nước -> Hỏi kỹ hơn vị trí trong nước -> Trả lời bằng phương hướng „im Süden“ -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Anna", "text": "Entschuldigung, wo liegt München?"},
                    {"id": 2, "speaker": "Tom", "text": "München? Das liegt in Deutschland."},
                    {"id": 3, "speaker": "Anna", "text": "Ja, aber wo genau in Deutschland?"},
                    {"id": 4, "speaker": "Tom", "text": "München liegt im Süden von Deutschland."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Entschuldigung, wo liegt München? München? Das liegt in Deutschland. Ja, aber wo genau in Deutschland? München liegt im Süden von Deutschland.",
                "translation": "- Anna: Xin lỗi, München nằm ở đâu?\n- Tom: München à? Nó nằm ở nước Đức.\n- Anna: Vâng, nhưng chính xác ở đâu tại Đức vậy?\n- Tom: München nằm ở miền Nam của nước Đức."
            }
        },
        {
            "id": 119,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 119: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Làm quen lịch sự:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Chào & hỏi ai -> Trả lời tên & hỏi lại -> Trả lời & hỏi xuất xứ -> Trả lời xuất xứ -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Maria", "text": "Guten Tag! Wer sind Sie?"},
                    {"id": 2, "speaker": "David", "text": "Guten Tag, mein Name ist David. Und wie heißen Sie?"},
                    {"id": 3, "speaker": "Maria", "text": "Ich bin Maria. Woher kommen Sie, David?"},
                    {"id": 4, "speaker": "David", "text": "Ich komme aus Deutschland."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Guten Tag! Wer sind Sie? Guten Tag, mein Name ist David. Und wie heißen Sie? Ich bin Maria. Woher kommen Sie, David? Ich komme aus Deutschland.",
                "translation": "- Maria: Xin chào! Ngài là ai ạ?\n- David: Xin chào, tên tôi là David. Còn ngài tên gì?\n- Maria: Tôi là Maria. Ngài đến từ đâu vậy David?\n- David: Tôi đến từ nước Đức."
            }
        },
        {
            "id": 120,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 120: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Kể chuyện quá khứ:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi hôm qua ở đâu -> Trả lời ở rạp chiếu phim -> Hỏi cảm nhận -> Đánh giá bộ phim -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Mia", "text": "Hallo Tom, wo warst du gestern?"},
                    {"id": 2, "speaker": "Tom", "text": "Gestern war ich im Kino."},
                    {"id": 3, "speaker": "Mia", "text": "Ach so! War es gut?"},
                    {"id": 4, "speaker": "Tom", "text": "Ja, der Film war fantastisch!"}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Hallo Tom, wo warst du gestern? Gestern war ich im Kino. Ach so! War es gut? Ja, der Film war fantastisch!",
                "translation": "- Mia: Chào Tom, hôm qua bạn đã ở đâu?\n- Tom: Hôm qua tôi ở rạp chiếu phim.\n- Mia: À thế à! Có hay không?\n- Tom: Có, bộ phim rất tuyệt vời!"
            }
        },
        {
            "id": 121,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 121: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Nhận diện đồ vật:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi có phải tivi không -> Phủ định với „kein“ -> Hỏi vậy là gì -> Giải thích là máy tính -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Ben", "text": "Ist das ein Fernseher?"},
                    {"id": 2, "speaker": "Lisa", "text": "Nein, das ist kein Fernseher."},
                    {"id": 3, "speaker": "Ben", "text": "Was ist es dann?"},
                    {"id": 4, "speaker": "Lisa", "text": "Das ist ein Computer."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Ist das ein Fernseher? Nein, das ist kein Fernseher. Was ist es dann? Das ist ein Computer.",
                "translation": "- Ben: Đó có phải là một cái tivi không?\n- Lisa: Không, đó không phải tivi.\n- Ben: Vậy đó là cái gì?\n- Lisa: Đó là một chiếc máy vi tính."
            }
        },
        {
            "id": 122,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 122: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Hỏi về ngôn ngữ:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi xuất xứ -> Trả lời từ Nhật Bản -> Hỏi có nói tiếng Nhật không -> Xác nhận là tiếng mẹ đẻ -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Max", "text": "Woher kommst du?"},
                    {"id": 2, "speaker": "Kenji", "text": "Ich komme aus Japan."},
                    {"id": 3, "speaker": "Max", "text": "Sprichst du dann Japanisch?"},
                    {"id": 4, "speaker": "Kenji", "text": "Ja, Japanisch ist meine Muttersprache."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Woher kommst du? Ich komme aus Japan. Sprichst du dann Japanisch? Ja, Japanisch ist meine Muttersprache.",
                "translation": "- Max: Bạn đến từ đâu?\n- Kenji: Tôi đến từ Nhật Bản.\n- Max: Vậy bạn có nói tiếng Nhật không?\n- Kenji: Có, tiếng Nhật là tiếng mẹ đẻ của tôi."
            }
        },
        {
            "id": 123,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 123: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Kế hoạch chuyến đi cuối tuần:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi cuối tuần có đi Ba Lan không -> Phủ định -> Hỏi vậy đi đâu -> Trả lời đi Pháp -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Nina", "text": "Fährst du am Wochenende nach Polen?"},
                    {"id": 2, "speaker": "Jan", "text": "Nein, ich fahre nicht nach Polen."},
                    {"id": 3, "speaker": "Nina", "text": "Wohin fährst du dann?"},
                    {"id": 4, "speaker": "Jan", "text": "Ich fahre nach Frankreich."}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Fährst du am Wochenende nach Polen? Nein, ich fahre nicht nach Polen. Wohin fährst du dann? Ich fahre nach Frankreich.",
                "translation": "- Nina: Cuối tuần bạn có đi Ba Lan không?\n- Jan: Không, tôi không đi Ba Lan.\n- Nina: Vậy bạn đi đâu?\n- Jan: Tôi đi Pháp."
            }
        },
        {
            "id": 124,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 124: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Đặt lịch hẹn:",
            "options": null,
            "correct_answer": "1, 2, 3, 4",
            "explanation": "Trình tự logic: Hỏi hôm nay có rảnh không -> Trả lời bận -> Hỏi ngày mai thế nào -> Trả lời ngày mai có thời gian -> Đáp án: 1, 2, 3, 4.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Sara", "text": "Hast du heute Zeit?"},
                    {"id": 2, "speaker": "Leon", "text": "Nein, heute bin ich leider beschäftigt."},
                    {"id": 3, "speaker": "Sara", "text": "Und wie ist es morgen?"},
                    {"id": 4, "speaker": "Leon", "text": "Ja, morgen habe ich Zeit!"}
                ],
                "correct_order": [1, 2, 3, 4],
                "audio_text": "Hast du heute Zeit? Nein, heute bin ich leider beschäftigt. Und wie ist es morgen? Ja, morgen habe ich Zeit!",
                "translation": "- Sara: Hôm nay bạn có thời gian không?\n- Leon: Không, tiếc là hôm nay tôi bận rồi.\n- Sara: Thế ngày mai thì sao?\n- Leon: Vâng, ngày mai tôi có thời gian!"
            }
        },
        {
            "id": 125,
            "exercise_type": "hoi_thoai_sap_xep",
            "question": "Câu 125: Sắp xếp các câu thoại sau theo đúng diễn biến hội thoại Gọi món trong quán:",
            "options": null,
            "correct_answer": "1, 2, 3, 4, 5",
            "explanation": "Trình tự logic: Bồi bàn hỏi khách 1 -> Khách 1 gọi cà phê -> Hỏi tiếp khách 2 -> Khách 2 gọi trà -> Bồi bàn xác nhận mang ra ngay -> Đáp án: 1, 2, 3, 4, 5.",
            "exp_reward": 15,
            "extra_data": {
                "lines": [
                    {"id": 1, "speaker": "Kellner", "text": "Was möchten Sie trinken?"},
                    {"id": 2, "speaker": "Gast 1", "text": "Ich trinke einen Kaffee, bitte."},
                    {"id": 3, "speaker": "Kellner", "text": "Und was möchten Sie?"},
                    {"id": 4, "speaker": "Gast 2", "text": "Für mich einen Tee, bitte."},
                    {"id": 5, "speaker": "Kellner", "text": "Also ein Kaffee und ein Tee. Kommt sofort!"}
                ],
                "correct_order": [1, 2, 3, 4, 5],
                "audio_text": "Was möchten Sie trinken? Ich trinke einen Kaffee, bitte. Und was möchten Sie? Für mich einen Tee, bitte. Also ein Kaffee und ein Tee. Kommt sofort!",
                "translation": "- Bồi bàn: Ngài muốn uống gì ạ?\n- Khách 1: Cho tôi một cà phê, làm ơn.\n- Bồi bàn: Còn ngài muốn dùng gì ạ?\n- Khách 2: Cho tôi một trà nhé.\n- Bồi bàn: Vậy là một cà phê và một trà. Có ngay đây ạ!"
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
