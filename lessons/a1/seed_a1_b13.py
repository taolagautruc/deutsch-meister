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
                    DeutschMeister A1 • ÔN TẬP A1 • Verben &amp; W-Fragen (Bài 13)
                </span>
                <h1 class="text-2xl sm:text-4xl font-black text-white tracking-tight">
                    Ôn tập A1: Động từ bất quy tắc, W-Fragen &amp; Giao tiếp quán Cafe
                </h1>
                <p class="text-amber-100 text-sm sm:text-base font-normal max-w-3xl leading-relaxed">
                    Hệ thống hóa toàn bộ quy tắc chia động từ có quy tắc và động từ bất quy tắc (Vokalwechsel: a→ä, e→i, e→ie), phân biệt đại từ nhân xưng. Nắm vững nghệ thuật đặt câu hỏi W-Fragen, động từ khuyết thiếu „möchten“ và thực hành hội thoại gọi món tại quán Cafe.
                </p>
                <div class="pt-2 flex flex-wrap gap-2 text-xs font-bold">
                    <span class="px-3 py-1.5 rounded-xl bg-white/15 backdrop-blur-sm border border-white/25 whitespace-nowrap">🔥 Động từ bất quy tắc (a→ä, e→i, e→ie)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/15 backdrop-blur-sm border border-white/25 whitespace-nowrap">📝 Động từ có quy tắc</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/15 backdrop-blur-sm border border-white/25 whitespace-nowrap">❓ W-Fragen (Wie, Wo, Woher, Was, Wann)</span>
                    <span class="px-3 py-1.5 rounded-xl bg-white/15 backdrop-blur-sm border border-white/25 whitespace-nowrap">☕ Hội thoại Cafe</span>
                </div>
            </div>
            <div class="absolute -right-8 -bottom-8 opacity-15 text-9xl select-none pointer-events-none">☕</div>
        </div>

        <!-- HỌC PHẦN 1: BẢNG ĐẠI TỪ NHÂN XƯNG & BẢNG CHIA 4 ĐỘNG TỪ CỐT LÕI -->
        <section class="space-y-5">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm shrink-0">1</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Bảng Đại Từ Nhân Xưng &amp; 4 Động Từ Nền Tảng (wohnen, lesen, sein, haben)
                </h2>
            </div>
            <p class="text-sm text-slate-700">
                Bảng đầy đủ đại từ nhân xưng theo từng ngôi (số ít / số nhiều / lịch sự) và đuôi chia chuẩn:
            </p>

            <!-- B1: BẢNG ĐẠI TỪ NHÂN XƯNG CÓ GHI NGÔI -->
            <div class="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-xs">
                <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[540px]">
                    <thead>
                        <tr class="bg-indigo-50 text-indigo-950 border-b border-indigo-200">
                            <th class="px-4 py-3 font-extrabold">Đại từ</th>
                            <th class="px-4 py-3 font-extrabold">Nghĩa tiếng Việt</th>
                            <th class="px-4 py-3 font-extrabold">Ngôi &amp; Số</th>
                            <th class="px-4 py-3 font-extrabold">Đuôi chuẩn</th>
                            <th class="px-4 py-3 font-extrabold text-center">Nghe</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-800 bg-white">
                        <tr class="hover:bg-slate-50">
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">ich</td>
                            <td class="px-4 py-2.5 font-semibold">tôi</td>
                            <td class="px-4 py-2.5 text-slate-600">ngôi I, số ít</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-e</td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('ich')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">du</td>
                            <td class="px-4 py-2.5 font-semibold">bạn</td>
                            <td class="px-4 py-2.5 text-slate-600">ngôi II, số ít</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-st <span class="text-[11px] font-normal text-slate-600">(-t nếu gốc -s/-ß/-z; -est nếu gốc -t/-d)</span></td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('du')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">er / sie / es</td>
                            <td class="px-4 py-2.5 font-semibold">anh ấy / cô ấy / nó</td>
                            <td class="px-4 py-2.5 text-slate-600">ngôi III, số ít</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-t</td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('er, sie, es')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">wir</td>
                            <td class="px-4 py-2.5 font-semibold">chúng tôi / chúng ta</td>
                            <td class="px-4 py-2.5 text-slate-600">ngôi I, số nhiều</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-en</td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('wir')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50 bg-emerald-50/40">
                            <td class="px-4 py-2.5 font-mono font-black text-emerald-800">ihr</td>
                            <td class="px-4 py-2.5 font-semibold">các bạn</td>
                            <td class="px-4 py-2.5 text-slate-600">ngôi II, số nhiều</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-t <span class="text-[11px] font-bold text-emerald-800">(KHÔNG đổi nguyên âm!)</span></td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('ihr')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">sie</td>
                            <td class="px-4 py-2.5 font-semibold">họ</td>
                            <td class="px-4 py-2.5 text-slate-600">ngôi III, số nhiều</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-en <span class="text-[11px] font-normal text-rose-700">(ngoại lệ: sie sind)</span></td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('sie')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="px-4 py-2.5 font-mono font-black text-indigo-700">Sie</td>
                            <td class="px-4 py-2.5 font-semibold">ngài / các ngài</td>
                            <td class="px-4 py-2.5 text-slate-600">lịch sự (luôn viết hoa S)</td>
                            <td class="px-4 py-2.5 font-mono font-bold text-emerald-700">-en <span class="text-[11px] font-normal text-rose-700">(ngoại lệ: Sie sind)</span></td>
                            <td class="px-4 py-2.5 text-center"><button type="button" onclick="b13_speakGerman('Sie')" class="px-2 py-0.5 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Khung Vàng Cảnh Báo Phân Biệt 3 Chữ sie (A4) -->
            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-300 space-y-2 text-xs">
                <div class="flex items-center gap-2 font-black text-amber-900">
                    <span>⚠️ KHUNG VÀNG CẢNH BÁO: PHÂN BIỆT 3 CHỮ „SIE“ TRONG TIẾNG ĐỨC</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                    <div class="p-3 rounded-xl bg-white border border-amber-200 text-slate-800 space-y-1">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-slate-900 font-mono">1. sie (cô ấy)</span>
                            <button type="button" onclick="b13_speakGerman('sie kommt, sie liest, sie ist')" class="text-xs px-1.5 py-0.5 rounded bg-amber-50 hover:bg-amber-100 cursor-pointer">🔊</button>
                        </div>
                        <p class="text-slate-600 text-[11px]">Ngôi III số ít, động từ chia đuôi <b>-t</b>: <i class="font-mono text-slate-900">sie kommt, sie liest, sie ist</i>.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-amber-200 text-slate-800 space-y-1">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-slate-900 font-mono">2. sie (họ)</span>
                            <button type="button" onclick="b13_speakGerman('sie kommen, sie lesen, sie sind')" class="text-xs px-1.5 py-0.5 rounded bg-amber-50 hover:bg-amber-100 cursor-pointer">🔊</button>
                        </div>
                        <p class="text-slate-600 text-[11px]">Ngôi III số nhiều, động từ chia đuôi <b>-en</b>: <i class="font-mono text-slate-900">sie kommen, sie lesen</i>. <b>Ngoại lệ:</b> <b class="text-rose-700 font-mono">„sie sind“</b> (không phải <i class="line-through text-slate-500">„sien“</i>).</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-amber-200 text-slate-800 space-y-1">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-slate-900 font-mono">3. Sie (ngài / các ngài)</span>
                            <button type="button" onclick="b13_speakGerman('Sie kommen, Sie sind')" class="text-xs px-1.5 py-0.5 rounded bg-amber-50 hover:bg-amber-100 cursor-pointer">🔊</button>
                        </div>
                        <p class="text-slate-600 text-[11px]">Ngôi lịch sự: <b>LUÔN VIẾT HOA chữ S</b> ở mọi vị trí câu; động từ đuôi <b>-en</b>: <i class="font-mono text-slate-900">Sie kommen, Sie sind</i>.</p>
                    </div>
                </div>
            </div>

            <!-- B2: BẢNG CHIA 4 ĐỘNG TỪ (CỘT GỐC | ĐUÔI): wohnen, lesen, sein, haben -->
            <div class="space-y-2 pt-2">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <h3 class="text-sm sm:text-base font-black text-slate-900">
                        Bảng Chia 4 Động Từ Trọng Tâm (Tách Gốc | Đuôi)
                    </h3>
                    <span class="text-xs font-bold text-rose-700 bg-rose-50 px-2.5 py-1 rounded-lg border border-rose-200">
                        🔥 Lưu ý: lesen đổi nguyên âm e → ie ở du &amp; er/sie/es; ngôi ihr KHÔNG đổi (lest)!
                    </span>
                </div>
                <div class="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-xs">
                    <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[680px]">
                        <thead>
                            <tr class="bg-slate-100 text-slate-900 border-b border-slate-200">
                                <th class="px-3 py-3 font-extrabold">Ngôi</th>
                                <th class="px-3 py-3 font-extrabold text-blue-800">wohnen (sống)<br><span class="text-[11px] font-normal text-slate-500">Gốc + Đuôi</span></th>
                                <th class="px-3 py-3 font-extrabold text-amber-800">lesen (đọc)<br><span class="text-[11px] font-normal text-slate-500">Gốc + Đuôi (e → ie)</span></th>
                                <th class="px-3 py-3 font-extrabold text-purple-800">sein (thì, là, ở)<br><span class="text-[11px] font-normal text-slate-500">Bất quy tắc hoàn toàn</span></th>
                                <th class="px-3 py-3 font-extrabold text-emerald-800">haben (có)<br><span class="text-[11px] font-normal text-slate-500">Bất quy tắc ở du, er/sie/es</span></th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800 bg-white">
                            <tr class="hover:bg-slate-50">
                                <td class="px-3 py-2.5 font-mono font-bold text-slate-900">ich <span class="text-[11px] font-normal text-slate-500">(I, ít)</span></td>
                                <td class="px-3 py-2.5 font-mono">wohn<b class="text-blue-600">-e</b> <span class="text-xs text-slate-500">(wohne)</span></td>
                                <td class="px-3 py-2.5 font-mono">les<b class="text-amber-700">-e</b> <span class="text-xs text-slate-500">(lese)</span></td>
                                <td class="px-3 py-2.5 font-mono font-bold text-purple-700">bin</td>
                                <td class="px-3 py-2.5 font-mono font-bold text-emerald-700">habe</td>
                            </tr>
                            <tr class="bg-rose-50/50 hover:bg-rose-50">
                                <td class="px-3 py-2.5 font-mono font-bold text-rose-900">du <span class="text-[11px] font-normal text-rose-700">(II, ít)</span></td>
                                <td class="px-3 py-2.5 font-mono">wohn<b class="text-blue-600">-st</b> <span class="text-xs text-slate-500">(wohnst)</span></td>
                                <td class="px-3 py-2.5 font-mono"><span class="px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 font-black">lies<b class="text-rose-600">-t</b> (liest) 🔥</span></td>
                                <td class="px-3 py-2.5 font-mono font-bold text-purple-700">bist</td>
                                <td class="px-3 py-2.5 font-mono font-bold text-rose-700">hast</td>
                            </tr>
                            <tr class="bg-rose-50/50 hover:bg-rose-50">
                                <td class="px-3 py-2.5 font-mono font-bold text-rose-900">er/sie/es <span class="text-[11px] font-normal text-rose-700">(III, ít)</span></td>
                                <td class="px-3 py-2.5 font-mono">wohn<b class="text-blue-600">-t</b> <span class="text-xs text-slate-500">(wohnt)</span></td>
                                <td class="px-3 py-2.5 font-mono"><span class="px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 font-black">lies<b class="text-rose-600">-t</b> (liest) 🔥</span></td>
                                <td class="px-3 py-2.5 font-mono font-bold text-purple-700">ist</td>
                                <td class="px-3 py-2.5 font-mono font-bold text-rose-700">hat</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="px-3 py-2.5 font-mono font-bold text-slate-900">wir <span class="text-[11px] font-normal text-slate-500">(I, nhiều)</span></td>
                                <td class="px-3 py-2.5 font-mono">wohn<b class="text-blue-600">-en</b> <span class="text-xs text-slate-500">(wohnen)</span></td>
                                <td class="px-3 py-2.5 font-mono">les<b class="text-amber-700">-en</b> <span class="text-xs text-slate-500">(lesen)</span></td>
                                <td class="px-3 py-2.5 font-mono font-bold text-purple-700">sind</td>
                                <td class="px-3 py-2.5 font-mono font-bold text-emerald-700">haben</td>
                            </tr>
                            <tr class="bg-emerald-50/60 hover:bg-emerald-50">
                                <td class="px-3 py-2.5 font-mono font-bold text-emerald-900">ihr <span class="text-[11px] font-normal text-emerald-700">(II, nhiều)</span></td>
                                <td class="px-3 py-2.5 font-mono">wohn<b class="text-blue-600">-t</b> <span class="text-xs text-slate-500">(wohnt)</span></td>
                                <td class="px-3 py-2.5 font-mono"><span class="px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-900 font-black">les<b class="text-emerald-700">-t</b> (lest) ✅ KHÔNG đổi!</span></td>
                                <td class="px-3 py-2.5 font-mono font-bold text-purple-700">seid</td>
                                <td class="px-3 py-2.5 font-mono font-bold text-emerald-700">habt</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="px-3 py-2.5 font-mono font-bold text-slate-900">sie / Sie <span class="text-[11px] font-normal text-slate-500">(III, nhiều / lịch sự)</span></td>
                                <td class="px-3 py-2.5 font-mono">wohn<b class="text-blue-600">-en</b> <span class="text-xs text-slate-500">(wohnen)</span></td>
                                <td class="px-3 py-2.5 font-mono">les<b class="text-amber-700">-en</b> <span class="text-xs text-slate-500">(lesen)</span></td>
                                <td class="px-3 py-2.5 font-mono font-bold text-purple-700">sind</td>
                                <td class="px-3 py-2.5 font-mono font-bold text-emerald-700">haben</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="flex flex-wrap gap-2 pt-1 text-xs">
                    <button type="button" onclick="b13_speakGerman('ich wohne, du wohnst, er wohnt, wir wohnen, ihr wohnt, sie wohnen')" class="px-3 py-1.5 rounded-xl bg-blue-50 hover:bg-blue-100 text-blue-800 border border-blue-200 font-bold cursor-pointer">🔊 Nghe wohnen</button>
                    <button type="button" onclick="b13_speakGerman('ich lese, du liest, er liest, wir lesen, ihr lest, sie lesen')" class="px-3 py-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer">🔊 Nghe lesen</button>
                    <button type="button" onclick="b13_speakGerman('ich bin, du bist, er ist, wir sind, ihr seid, sie sind')" class="px-3 py-1.5 rounded-xl bg-purple-50 hover:bg-purple-100 text-purple-800 border border-purple-200 font-bold cursor-pointer">🔊 Nghe sein</button>
                    <button type="button" onclick="b13_speakGerman('ich habe, du hast, er hat, wir haben, ihr habt, sie haben')" class="px-3 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-200 font-bold cursor-pointer">🔊 Nghe haben</button>
                </div>
            </div>
        </section>

        <!-- HỌC PHẦN 2: ĐỘNG TỪ CÓ QUY TẮC, NGOẠI LỆ ĐUÔI DU & ĐỘNG TỪ BẤT QUY TẮC (VOKALWECHSEL) -->
        <section class="space-y-5">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-amber-600 text-white font-black flex items-center justify-center text-sm shrink-0">2</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Động Từ Có Quy Tắc, Ngoại Lệ Đuôi &amp; Động Từ Bất Quy Tắc (Vokalwechsel)
                </h2>
            </div>

            <!-- A3: QUY TẮC ĐUÔI NGÔI DU & NGOẠI LỆ GỐC -s/-ß/-z VÀ -t/-d -->
            <div class="p-4 rounded-2xl bg-sky-50 border border-sky-200 space-y-3 text-xs">
                <div class="font-black text-sky-950 text-sm">📌 Quy tắc đuôi ngôi „du“ và các trường hợp gốc đặc biệt (Bắt buộc nhớ!):</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="p-3.5 rounded-xl bg-white border border-sky-200 space-y-1.5 text-slate-800">
                        <div class="font-extrabold text-indigo-800">1. Gốc kết thúc bằng <code>-s / -ß / -z</code> → ngôi <code>du</code> chỉ thêm <code>-t</code>:</div>
                        <p class="text-slate-600">Gốc đã kết thúc bằng s/ß/z thì <b>du chỉ thêm -t</b> (ví dụ: <code>lies + t = liest</code>):</p>
                        <div class="space-y-1 pt-1">
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-indigo-700">„du heißt“</b> — bạn tên là <span class="text-slate-500">(heißen)</span></span>
                                <button type="button" onclick="b13_speakGerman('du heißt')" class="text-slate-500 hover:text-indigo-600 cursor-pointer">🔊</button>
                            </div>
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-indigo-700">„du tanzt“</b> — bạn nhảy <span class="text-slate-500">(tanzen)</span></span>
                                <button type="button" onclick="b13_speakGerman('du tanzt')" class="text-slate-500 hover:text-indigo-600 cursor-pointer">🔊</button>
                            </div>
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-indigo-700">„du reist“</b> — bạn đi du lịch <span class="text-slate-500">(reisen)</span></span>
                                <button type="button" onclick="b13_speakGerman('du reist')" class="text-slate-500 hover:text-indigo-600 cursor-pointer">🔊</button>
                            </div>
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-indigo-700">„du liest“</b> — bạn đọc <span class="text-slate-500">(lesen: lies + t)</span></span>
                                <button type="button" onclick="b13_speakGerman('du liest')" class="text-slate-500 hover:text-indigo-600 cursor-pointer">🔊</button>
                            </div>
                        </div>
                    </div>
                    <div class="p-3.5 rounded-xl bg-white border border-sky-200 space-y-1.5 text-slate-800">
                        <div class="font-extrabold text-amber-800">2. Gốc kết thúc bằng <code>-t / -d</code> → chèn thêm <code>-e-</code> ở ngôi <code>du, er/sie/es, ihr</code>:</div>
                        <p class="text-slate-600">Chèn <code>-e-</code> để dễ phát âm (<code>-est</code>, <code>-et</code>):</p>
                        <div class="space-y-1 pt-1">
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-amber-700">„du arbeitest“</b> — bạn làm việc <span class="text-slate-500">(arbeiten)</span></span>
                                <button type="button" onclick="b13_speakGerman('du arbeitest')" class="text-slate-500 hover:text-amber-600 cursor-pointer">🔊</button>
                            </div>
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-amber-700">„er arbeitet“</b> — anh ấy làm việc</span>
                                <button type="button" onclick="b13_speakGerman('er arbeitet')" class="text-slate-500 hover:text-amber-600 cursor-pointer">🔊</button>
                            </div>
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-amber-700">„ihr arbeitet“</b> — các bạn làm việc</span>
                                <button type="button" onclick="b13_speakGerman('ihr arbeitet')" class="text-slate-500 hover:text-amber-600 cursor-pointer">🔊</button>
                            </div>
                            <div class="flex items-center justify-between gap-2 bg-slate-50 px-2.5 py-1.5 rounded-lg">
                                <span><b class="font-mono text-amber-700">„du wartest“</b> — bạn chờ đợi <span class="text-slate-500">(warten)</span></span>
                                <button type="button" onclick="b13_speakGerman('du wartest')" class="text-slate-500 hover:text-amber-600 cursor-pointer">🔊</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- B7 PHẦN 1: ÔN CHIA ĐỘNG TỪ CÓ QUY TẮC (15 CÂU MẪU) -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 text-xs">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <h3 class="text-sm sm:text-base font-black text-slate-900">
                        📝 Ôn Chia Động Từ Có Quy Tắc (Công thức: Gốc động từ + Đuôi ngôi) — 15 Câu Mẫu
                    </h3>
                    <span class="font-mono text-[11px] px-2.5 py-1 rounded-lg bg-white border border-slate-200 text-slate-700 font-bold">
                        ich -e | du -st | er/sie/es -t | wir -en | ihr -t | sie/Sie -en
                    </span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2.5">
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">kaufen:</span> „Wir kaufen den Käse.“</div>
                            <div class="text-slate-500 italic">Chúng tôi mua phô mai.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Wir kaufen den Käse.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">gehen:</span> „Hannes geht spazieren.“</div>
                            <div class="text-slate-500 italic">Hannes đi dạo.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Hannes geht spazieren.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">reisen:</span> „Julia und Lara reisen nach Italien.“</div>
                            <div class="text-slate-500 italic">Julia và Lara du lịch tới Ý.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Julia und Lara reisen nach Italien.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">trinken:</span> „Trinkst du gern Kaffee?“</div>
                            <div class="text-slate-500 italic">Bạn có thích uống cà phê không?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Trinkst du gern Kaffee?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">machen:</span> „Ich mache meine Hausaufgaben.“</div>
                            <div class="text-slate-500 italic">Tôi làm bài tập về nhà.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Ich mache meine Hausaufgaben.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">schreiben:</span> „Schreibt ihr einen Brief?“</div>
                            <div class="text-slate-500 italic">Các bạn đang viết một bức thư à?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Schreibt ihr einen Brief?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">hören:</span> „Karin hört Musik.“</div>
                            <div class="text-slate-500 italic">Karin nghe nhạc.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Karin hört Musik.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">kommen:</span> „Woher kommen Sie?“</div>
                            <div class="text-slate-500 italic">Ngài đến từ đâu ạ?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Woher kommen Sie?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">liegen:</span> „Das Handy liegt in der Küche.“</div>
                            <div class="text-slate-500 italic">Chiếc điện thoại nằm trong bếp.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Das Handy liegt in der Küche.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">spielen:</span> „Die Kinder spielen Fußball.“</div>
                            <div class="text-slate-500 italic">Bọn trẻ chơi bóng đá.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Die Kinder spielen Fußball.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">singen:</span> „Singst du gern?“</div>
                            <div class="text-slate-500 italic">Bạn có thích hát không?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Singst du gern?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">grillen:</span> „Der Vater grillt das Gemüse.“</div>
                            <div class="text-slate-500 italic">Bố nướng rau củ.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Der Vater grillt das Gemüse.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">spielen:</span> „Spielt ihr Tennis?“</div>
                            <div class="text-slate-500 italic">Các bạn có chơi quần vợt không?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Spielt ihr Tennis?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">besuchen:</span> „Die Touristen besuchen das Rathaus.“</div>
                            <div class="text-slate-500 italic">Khách du lịch tham quan tòa thị chính.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Die Touristen besuchen das Rathaus.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-slate-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-indigo-600">arbeiten:</span> „Du arbeitest heute sehr viel.“</div>
                            <div class="text-slate-500 italic">Hôm nay bạn làm việc rất nhiều.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Du arbeitest heute sehr viel.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-amber-50/90 border border-amber-200 text-amber-950 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                    <div class="leading-relaxed">
                        <b>Lưu ý:</b> gốc <code>-t/-d</code> thì chèn <code>-e-</code>: <span class="font-mono font-bold">du arbeitest, er arbeitet, ihr arbeitet</span>. Gốc <code>-s/-ß/-z</code> thì <code>du</code> chỉ thêm <code>-t</code>: <span class="font-mono font-bold">du heißt, du reist</span>.
                    </div>
                    <button type="button" onclick="b13_speakGerman('du arbeitest, er arbeitet, ihr arbeitet, du heißt, du reist')" class="px-2.5 py-1 rounded-lg bg-white border border-amber-200 text-amber-800 font-bold cursor-pointer shrink-0 self-start sm:self-center">🔊 Nghe</button>
                </div>
            </div>

            <!-- ĐỘNG TỪ BẤT QUY TẮC (VOKALWECHSEL) -->
            <div class="p-4 rounded-2xl bg-rose-50 border border-rose-300 text-xs space-y-2">
                <div class="font-black text-rose-900 text-sm flex items-center gap-2">
                    <span>🔥 QUY TẮC VÀNG ĐỘNG TỪ BẤT QUY TẮC (VOKALWECHSEL):</span>
                </div>
                <p class="text-rose-950 leading-relaxed font-semibold">
                    Hiện tượng <b>Vokalwechsel (đổi nguyên âm gốc)</b> <b>CHỈ XẢY RA</b> ở 2 ngôi: <code>du</code> và <code>er/sie/es</code>.
                    <br>
                    <span class="text-rose-800 font-extrabold underline">Tuyệt đối cấm kỵ:</span> Ngôi <code>ihr</code> (các bạn) <b>KHÔNG BAO GIỜ</b> biến âm! (<i>ihr fahrt, ihr schlaft, ihr lest, ihr sprecht</i>).
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5 text-slate-800">
                    <div class="font-bold font-mono text-sm text-indigo-700">Nhóm a → ä:</div>
                    <div>• <b>fahren</b>: du fährst, er fährt (ihr fahrt)</div>
                    <div>• <b>schlafen</b>: du schläfst, er schläft (ihr schlaft)</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5 text-slate-800">
                    <div class="font-bold font-mono text-sm text-amber-700">Nhóm e → i:</div>
                    <div>• <b>sprechen</b>: du sprichst, er spricht (ihr sprecht)</div>
                    <div>• <b>treffen</b>: du triffst, er trifft (ihr trefft)</div>
                    <div>• <b>essen</b>: du isst, er isst (ihr esst)</div>
                    <div>• <b>geben</b>: du gibst, er gibt (ihr gebt)</div>
                </div>
                <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5 text-slate-800">
                    <div class="font-bold font-mono text-sm text-emerald-700">Nhóm e → ie:</div>
                    <div>• <b>lesen</b>: du liest, er liest (ihr lest)</div>
                    <div class="text-[11px] text-slate-600 italic mt-1">*Gốc đã kết thúc bằng s thì du chỉ thêm -t (lies + t = liest).</div>
                </div>
            </div>

            <!-- B7 PHẦN 2: 7 CÂU MẪU ĐỘNG TỪ BẤT QUY TẮC -->
            <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-3 text-xs">
                <div class="font-black text-amber-950 text-sm">🔥 7 Câu Mẫu Động Từ Bất Quy Tắc Trọng Tâm:</div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-rose-700">lesen (e→ie):</span> „Das Mädchen liest das Buch.“</div>
                            <div class="text-slate-500 italic">Cô bé đọc quyển sách.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Das Mädchen liest das Buch.')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-rose-700">fahren (a→ä):</span> „Wir fahren nach Polen.“</div>
                            <div class="text-slate-500 italic">Chúng tôi đi tới Ba Lan. (ngôi wir không đổi; du fährst)</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Wir fahren nach Polen.')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-rose-700">sprechen (e→i):</span> „Der Lehrer spricht zu leise.“</div>
                            <div class="text-slate-500 italic">Thầy giáo nói quá nhỏ.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Der Lehrer spricht zu leise.')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-emerald-700">treffen (ngôi ihr KHÔNG đổi):</span> „Wann trefft ihr eure Freunde?“</div>
                            <div class="text-slate-500 italic">Khi nào các bạn gặp bạn bè của mình?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Wann trefft ihr eure Freunde?')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-rose-700">essen (e→i):</span> „Ich esse gern Eis.“</div>
                            <div class="text-slate-500 italic">Tôi thích ăn kem. (ngôi du/er: du isst, er isst)</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Ich esse gern Eis.')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-rose-700">geben (e→i):</span> „Hannes und Julia geben dem Hund das Futter.“</div>
                            <div class="text-slate-500 italic">Hannes và Julia cho chú chó thức ăn.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Hannes und Julia geben dem Hund das Futter.')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200 flex items-start justify-between gap-2 md:col-span-2">
                        <div>
                            <div class="font-bold text-slate-900"><span class="text-rose-700">schlafen (a→ä):</span> „Schläfst du im Hotel?“</div>
                            <div class="text-slate-500 italic">Bạn có ngủ ở khách sạn không?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Schläfst du im Hotel?')" class="text-slate-400 hover:text-amber-600 cursor-pointer shrink-0">🔊</button>
                    </div>
                </div>
            </div>

            <!-- CONTAINER SƠ ĐỒ V1 -->
            <div id="b13-svg-v1-container" class="my-4"></div>
        </section>

        <!-- HỌC PHẦN 3: TỪ ĐỂ HỎI (W-FRAGEN), 3 CÁCH HỎI TÊN & MÖCHTEN -->
        <section class="space-y-5">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-indigo-600 text-white font-black flex items-center justify-center text-sm shrink-0">3</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Từ Để Hỏi (W-Fragen), Ba Cách Hỏi Tên &amp; Động Từ Khuyết „möchten“
                </h2>
            </div>

            <!-- A1 + A2 + D2 + D3 + #4: 5 THẺ W-FRAGEN RESPONSIVE (1 CỘT MOBILE / 2 TABLET / TỐI ĐA 3 DESKTOP), ĐỒNG NHẤT CẤU TRÚC -->
            <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 text-xs">
                <!-- 1. Wie -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between gap-3 text-slate-800 min-w-[230px]">
                    <div class="space-y-1.5 flex-1">
                        <span class="font-mono text-sm font-black text-amber-700 block">Wie (Như thế nào)</span>
                        <p class="text-slate-600 leading-relaxed">Dùng để hỏi tên gọi, tính chất hoặc trạng thái. Lưu ý: KHÔNG dùng „Was ist dein Name?“.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-2">
                        <div class="space-y-0.5">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-slate-900 inline-block">„Wie heißen Sie?“</span>
                                <button type="button" onclick="b13_speakGerman('Wie heißen Sie?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Ngài tên là gì?</div>
                        </div>
                        <div class="space-y-0.5 pt-2 border-t border-slate-100">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-emerald-700 inline-block">„Ich heiße Anna.“</span>
                                <button type="button" onclick="b13_speakGerman('Ich heiße Anna.')" class="text-slate-400 hover:text-emerald-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Tôi tên là Anna.</div>
                        </div>
                    </div>
                </div>

                <!-- 2. Woher (A2) -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between gap-3 text-slate-800 min-w-[230px]">
                    <div class="space-y-1.5 flex-1">
                        <span class="font-mono text-sm font-black text-rose-700 block">Woher (Từ đâu)</span>
                        <p class="text-slate-600 leading-relaxed">Thường đi với <b>aus</b>. Nước có mạo từ dùng <b>aus der / aus den</b> (<i>aus der Türkei, aus der Schweiz, aus den USA</i>); nước không mạo từ dùng <b>aus</b> (<i>aus Deutschland, aus Vietnam, aus Polen</i>).</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-2">
                        <div class="space-y-0.5">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-slate-900 inline-block">„Woher kommst du?“</span>
                                <button type="button" onclick="b13_speakGerman('Woher kommst du?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Bạn đến từ đâu?</div>
                        </div>
                        <div class="space-y-0.5 pt-2 border-t border-slate-100">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-emerald-700 inline-block">„Aus Vietnam.“</span>
                                <button type="button" onclick="b13_speakGerman('Aus Vietnam.')" class="text-slate-400 hover:text-emerald-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Từ Việt Nam.</div>
                        </div>
                    </div>
                </div>

                <!-- 3. Wo (A1) -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between gap-3 text-slate-800 min-w-[230px]">
                    <div class="space-y-1.5 flex-1">
                        <span class="font-mono text-sm font-black text-blue-700 block">Wo (Ở đâu)</span>
                        <p class="text-slate-600 leading-relaxed">Thường đi với <b>in</b> + thành phố / nước (<i>in Berlin</i>). Cũng gặp <i>am Bahnhof, zu Hause, bei Freunden</i>.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-2">
                        <div class="space-y-0.5">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-slate-900 inline-block">„Wo wohnen Sie?“</span>
                                <button type="button" onclick="b13_speakGerman('Wo wohnen Sie?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Ngài sống ở đâu?</div>
                        </div>
                        <div class="space-y-0.5 pt-2 border-t border-slate-100">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-emerald-700 inline-block">„In Berlin.“</span>
                                <button type="button" onclick="b13_speakGerman('In Berlin.')" class="text-slate-400 hover:text-emerald-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Ở Berlin.</div>
                        </div>
                    </div>
                </div>

                <!-- 4. Was -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between gap-3 text-slate-800 min-w-[230px]">
                    <div class="space-y-1.5 flex-1">
                        <span class="font-mono text-sm font-black text-purple-700 block">Was (Cái gì)</span>
                        <p class="text-slate-600 leading-relaxed">Hỏi đồ vật, đồ ăn, thức uống hoặc hoạt động đang làm.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-2">
                        <div class="space-y-0.5">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-slate-900 inline-block">„Was trinken Sie?“</span>
                                <button type="button" onclick="b13_speakGerman('Was trinken Sie?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Ngài uống gì ạ?</div>
                        </div>
                        <div class="space-y-0.5 pt-2 border-t border-slate-100">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-emerald-700 inline-block">„Kaffee mit Zucker.“</span>
                                <button type="button" onclick="b13_speakGerman('Kaffee mit Zucker.')" class="text-slate-400 hover:text-emerald-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Cà phê có đường.</div>
                        </div>
                    </div>
                </div>

                <!-- 5. Wann (D3) -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between gap-3 text-slate-800 min-w-[230px]">
                    <div class="space-y-1.5 flex-1">
                        <span class="font-mono text-sm font-black text-emerald-700 block">Wann (Khi nào)</span>
                        <p class="text-slate-600 leading-relaxed">Hỏi thời điểm, thứ trong tuần hoặc giờ giấc (<i>am Wochenende, um 15 Uhr</i>).</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-2">
                        <div class="space-y-0.5">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-slate-900 inline-block">„Wann fahrt ihr?“</span>
                                <button type="button" onclick="b13_speakGerman('Wann fahrt ihr?')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Khi nào các bạn đi?</div>
                        </div>
                        <div class="space-y-0.5 pt-2 border-t border-slate-100">
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono font-bold text-emerald-700 inline-block">„Am Wochenende.“</span>
                                <button type="button" onclick="b13_speakGerman('Am Wochenende.')" class="text-slate-400 hover:text-emerald-600 cursor-pointer shrink-0">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-500 italic">Vào cuối tuần.</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- CONTAINER SƠ ĐỒ V2 -->
            <div id="b13-svg-v2-container" class="my-4"></div>

            <!-- B3: BA CÁCH HỎI TÊN (NGÔI SIE VÀ NGÔI DU) -->
            <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-200 space-y-3 text-xs">
                <div class="font-black text-indigo-950 text-sm">🪪 Ba Cách Hỏi Tên Chuẩn Trong Tiếng Đức (Cả ngôi lịch sự „Sie“ &amp; thân mật „du“):</div>
                <div class="overflow-x-auto rounded-xl border border-indigo-200 bg-white">
                    <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[580px]">
                        <thead>
                            <tr class="bg-indigo-100/70 text-indigo-950 border-b border-indigo-200">
                                <th class="px-3.5 py-2.5 font-extrabold">Cách</th>
                                <th class="px-3.5 py-2.5 font-extrabold">Ngôi lịch sự (Sie)</th>
                                <th class="px-3.5 py-2.5 font-extrabold">Ngôi thân mật (du)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800 bg-white">
                            <tr>
                                <td class="px-3.5 py-2.5 font-bold text-indigo-700">1. Dùng heißen</td>
                                <td class="px-3.5 py-2.5">
                                    <div class="flex items-center justify-between gap-2">
                                        <span class="font-mono font-bold">„Wie heißen Sie?“ → „Ich heiße Anna.“</span>
                                        <button type="button" onclick="b13_speakGerman('Wie heißen Sie? Ich heiße Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                                    </div>
                                    <div class="text-[11px] text-slate-500 italic">Ngài tên là gì? → Tôi tên là Anna.</div>
                                </td>
                                <td class="px-3.5 py-2.5">
                                    <div class="flex items-center justify-between gap-2">
                                        <span class="font-mono font-bold">„Wie heißt du?“ → „Ich heiße Anna.“</span>
                                        <button type="button" onclick="b13_speakGerman('Wie heißt du? Ich heiße Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                                    </div>
                                    <div class="text-[11px] text-slate-500 italic">Bạn tên là gì? → Tôi tên là Anna.</div>
                                </td>
                            </tr>
                            <tr>
                                <td class="px-3.5 py-2.5 font-bold text-indigo-700">2. Dùng sein (Wer)</td>
                                <td class="px-3.5 py-2.5">
                                    <div class="flex items-center justify-between gap-2">
                                        <span class="font-mono font-bold">„Wer sind Sie?“ → „Ich bin Anna.“</span>
                                        <button type="button" onclick="b13_speakGerman('Wer sind Sie? Ich bin Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                                    </div>
                                    <div class="text-[11px] text-slate-500 italic">Ngài là ai ạ? → Tôi là Anna.</div>
                                </td>
                                <td class="px-3.5 py-2.5">
                                    <div class="flex items-center justify-between gap-2">
                                        <span class="font-mono font-bold">„Wer bist du?“ → „Ich bin Anna.“</span>
                                        <button type="button" onclick="b13_speakGerman('Wer bist du? Ich bin Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                                    </div>
                                    <div class="text-[11px] text-slate-500 italic">Bạn là ai? → Tôi là Anna.</div>
                                </td>
                            </tr>
                            <tr>
                                <td class="px-3.5 py-2.5 font-bold text-indigo-700">3. Dùng der Name</td>
                                <td class="px-3.5 py-2.5">
                                    <div class="flex items-center justify-between gap-2">
                                        <span class="font-mono font-bold">„Wie ist Ihr Name?“ → „Mein Name ist Anna.“</span>
                                        <button type="button" onclick="b13_speakGerman('Wie ist Ihr Name? Mein Name ist Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                                    </div>
                                    <div class="text-[11px] text-slate-500 italic">Tên của ngài là gì? → Tên tôi là Anna.</div>
                                </td>
                                <td class="px-3.5 py-2.5">
                                    <div class="flex items-center justify-between gap-2">
                                        <span class="font-mono font-bold">„Wie ist dein Name?“ → „Mein Name ist Anna.“</span>
                                        <button type="button" onclick="b13_speakGerman('Wie ist dein Name? Mein Name ist Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                                    </div>
                                    <div class="text-[11px] text-slate-500 italic">Tên của bạn là gì? → Tên tôi là Anna.</div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- B4: ĐỘNG TỪ KHUYẾT MÖCHTEN (MUỐN) -->
            <div class="p-4 rounded-2xl bg-purple-50/70 border border-purple-200 space-y-3 text-xs">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <h3 class="text-sm sm:text-base font-black text-purple-950">
                        ✨ Động Từ Khuyết Thiếu „möchten“ (Muốn — Diễn đạt lịch sự)
                    </h3>
                    <button type="button" onclick="b13_speakGerman('ich möchte, du möchtest, er möchte, wir möchten, ihr möchtet, sie möchten')" class="px-2.5 py-1 rounded-lg bg-white border border-purple-200 text-purple-700 font-bold cursor-pointer">🔊 Nghe bảng chia</button>
                </div>
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2 text-center">
                    <div class="p-2.5 rounded-xl bg-white border border-purple-200 text-slate-800"><span class="text-slate-500 block text-[11px]">ich</span><b class="font-mono text-purple-800">möchte</b></div>
                    <div class="p-2.5 rounded-xl bg-white border border-purple-200 text-slate-800"><span class="text-slate-500 block text-[11px]">du</span><b class="font-mono text-purple-800">möchtest</b></div>
                    <div class="p-2.5 rounded-xl bg-white border border-purple-200 text-slate-800"><span class="text-slate-500 block text-[11px]">er/sie/es</span><b class="font-mono text-purple-800">möchte</b></div>
                    <div class="p-2.5 rounded-xl bg-white border border-purple-200 text-slate-800"><span class="text-slate-500 block text-[11px]">wir</span><b class="font-mono text-purple-800">möchten</b></div>
                    <div class="p-2.5 rounded-xl bg-white border border-purple-200 text-slate-800"><span class="text-slate-500 block text-[11px]">ihr</span><b class="font-mono text-purple-800">möchtet</b></div>
                    <div class="p-2.5 rounded-xl bg-white border border-purple-200 text-slate-800"><span class="text-slate-500 block text-[11px]">sie / Sie</span><b class="font-mono text-purple-800">möchten</b></div>
                </div>
                <div class="p-3.5 rounded-xl bg-white border border-purple-200 space-y-2 text-slate-800">
                    <div><b>📐 Cấu trúc khung câu (Satzklammer):</b> Động từ khuyết <b>möchten</b> đứng ở <b>vị trí 2</b>, động từ chính ở dạng <b>nguyên mẫu (Infinitiv)</b> đứng ở <b>CUỐI câu</b>.</div>
                    <div class="flex flex-wrap items-center justify-between gap-2 bg-purple-50/80 p-2.5 rounded-lg border border-purple-100">
                        <div>
                            <div class="font-mono font-bold text-slate-900">„Was möchten Sie trinken?“ → „Ich möchte Kaffee trinken.“</div>
                            <div class="text-slate-600 italic">Ngài muốn uống gì ạ? → Tôi muốn uống cà phê. <span class="not-italic text-purple-800 font-semibold">(= „Ich trinke Kaffee.“ nhưng lịch sự hơn)</span></div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Was möchten Sie trinken? Ich möchte Kaffee trinken.')" class="px-2.5 py-1 rounded-lg bg-white border border-purple-200 text-purple-700 font-bold cursor-pointer shrink-0">🔊 Nghe</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- HỌC PHẦN 4: HỘI THOẠI THỰC TẾ „KAFFEE ODER TEE“ & HỎI - ĐÁP THEO NGÔI -->
        <section class="space-y-5">
            <div class="flex items-center gap-2 border-b border-slate-200 pb-2">
                <span class="w-8 h-8 rounded-lg bg-orange-600 text-white font-black flex items-center justify-center text-sm shrink-0">4</span>
                <h2 class="text-lg sm:text-xl font-black text-slate-900">
                    Hội Thoại Thực Tế „Kaffee oder Tee“ &amp; Quy Tắc Hỏi - Đáp Theo Ngôi
                </h2>
            </div>

            <!-- B5: HỘI THOẠI 7 DÒNG KAFFEE ODER TEE -->
            <div class="p-4 sm:p-5 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-3 text-xs">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <h3 class="text-sm sm:text-base font-black text-amber-950">
                        ☕ Hội Thoại Chuẩn 7 Dòng Tại Quán Cafe: „Kaffee oder Tee“
                    </h3>
                    <button id="b13-cafe-play-all-btn" type="button" onclick="b13_playCafeDialogue()"
                        class="px-3.5 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs shadow-sm transition cursor-pointer flex items-center gap-1.5">
                        🔊 Nghe cả hội thoại
                    </button>
                </div>
                <div class="space-y-2">
                    <div id="b13-cafe-line-0" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">1.</span> „Entschuldigung, ist hier frei?“</div>
                            <div class="text-slate-600 italic">Xin lỗi, chỗ này còn trống không?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Entschuldigung, ist hier frei?')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div id="b13-cafe-line-1" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">2.</span> „Ja klar, bitte.“</div>
                            <div class="text-slate-600 italic">Vâng tất nhiên, xin mời.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Ja klar, bitte.')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div id="b13-cafe-line-2" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">3.</span> „Ich bin John aus Frankreich, und du?“</div>
                            <div class="text-slate-600 italic">Tôi là John đến từ Pháp, còn bạn?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Ich bin John aus Frankreich, und du?')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div id="b13-cafe-line-3" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">4.</span> „Ich heiße Maria. Ich komme aus Polen.“</div>
                            <div class="text-slate-600 italic">Tôi tên là Maria. Tôi đến từ Ba Lan.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Ich heiße Maria. Ich komme aus Polen.')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div id="b13-cafe-line-4" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">5.</span> „Was trinkst du: Kaffee oder Tee?“</div>
                            <div class="text-slate-600 italic">Bạn uống gì: cà phê hay trà?</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Was trinkst du: Kaffee oder Tee?')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div id="b13-cafe-line-5" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">6.</span> „Kaffee.“</div>
                            <div class="text-slate-600 italic">Cà phê.</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Kaffee.')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                    <div id="b13-cafe-line-6" class="p-3 rounded-xl bg-white border border-amber-200 flex items-center justify-between gap-3 transition">
                        <div>
                            <div class="font-mono font-bold text-slate-900 text-sm"><span class="text-amber-700">7.</span> „Zwei Kaffee, bitte!“</div>
                            <div class="text-slate-600 italic">Xin cho hai cà phê!</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('Zwei Kaffee, bitte!')" class="px-2.5 py-1 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 font-bold cursor-pointer shrink-0">🔊</button>
                    </div>
                </div>
            </div>

            <!-- B6: HỎI - ĐÁP THEO NGÔI -->
            <div class="p-4 sm:p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 text-xs">
                <div class="flex flex-wrap items-center justify-between gap-2">
                    <h3 class="text-sm sm:text-base font-black text-slate-900">
                        🔄 Quy Tắc Hỏi - Đáp Đổi Ngôi Chuẩn Giao Tiếp
                    </h3>
                    <span class="px-2.5 py-1 rounded-lg bg-indigo-100 text-indigo-900 font-extrabold text-[11px] border border-indigo-200">
                        💡 Hỏi „ihr“ → trả lời „wir“ • Hỏi „Sie“ / „du“ → trả lời „ich“
                    </span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5">
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <div class="flex items-center justify-between gap-2">
                            <span class="font-mono font-bold text-slate-900">„Was trinken Sie?“ → „Tee, bitte.“</span>
                            <button type="button" onclick="b13_speakGerman('Was trinken Sie? Tee, bitte.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="text-slate-600 italic">Ngài uống gì ạ? → Cho trà, xin cảm ơn.</div>
                    </div>
                    <div class="p-3 rounded-xl bg-emerald-50/60 border border-emerald-200 space-y-1">
                        <div class="flex items-center justify-between gap-2">
                            <span class="font-mono font-bold text-slate-900">„Was trinkt ihr?“ → „Wir trinken Kaffee.“</span>
                            <button type="button" onclick="b13_speakGerman('Was trinkt ihr? Wir trinken Kaffee.')" class="text-slate-400 hover:text-emerald-600 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="text-slate-600 italic">Các bạn uống gì? → Chúng tôi uống cà phê. <b class="text-emerald-800 not-italic">(ihr → wir)</b></div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <div class="flex items-center justify-between gap-2">
                            <span class="font-mono font-bold text-slate-900">„Wo wohnen Sie?“ → „Ich wohne in Hanoi.“</span>
                            <button type="button" onclick="b13_speakGerman('Wo wohnen Sie? Ich wohne in Hanoi.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="text-slate-600 italic">Ngài sống ở đâu? → Tôi sống ở Hà Nội. <b class="text-indigo-700 not-italic">(Sie → ich)</b></div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <div class="flex items-center justify-between gap-2">
                            <span class="font-mono font-bold text-slate-900">„Woher kommen Sie?“ → „Aus der Türkei.“</span>
                            <button type="button" onclick="b13_speakGerman('Woher kommen Sie? Aus der Türkei.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="text-slate-600 italic">Ngài đến từ đâu? → Từ Thổ Nhĩ Kỳ.</div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <div class="flex items-center justify-between gap-2">
                            <span class="font-mono font-bold text-slate-900">„Wie heißen Sie?“ → „Julia Müller.“</span>
                            <button type="button" onclick="b13_speakGerman('Wie heißen Sie? Julia Müller.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="text-slate-600 italic">Ngài tên là gì? → Julia Müller.</div>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200 space-y-1">
                        <div class="flex items-center justify-between gap-2">
                            <span class="font-mono font-bold text-slate-900">„Wie heißt du?“ → „Mein Name ist Anna.“</span>
                            <button type="button" onclick="b13_speakGerman('Wie heißt du? Mein Name ist Anna.')" class="text-slate-400 hover:text-indigo-600 cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="text-slate-600 italic">Bạn tên là gì? → Tên tôi là Anna.</div>
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

    # Cập nhật danh sách từ vựng Bài 13 (12 thẻ gốc sửa chuẩn C1-C5 + 6 thẻ B8 chưa có ở Bài 1->12)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    
    vocab_items = [
        ("Kaffee", "der", "cà phê (Pl: die Kaffees)", "„Ich trinke meinen Kaffee immer mit viel Zucker.“ — Tôi luôn uống cà phê của mình với nhiều đường."),
        ("Tee", "der", "trà (Pl: die Tees)", "„Möchtest du eine Tasse schwarzen Tee?“ — Bạn có muốn một tách trà đen không?"),
        ("Zucker", "der", "đường (Pl: nur Sg.)", "„Zwei Kaffee mit Zucker, bitte!“ — Xin cho hai cà phê có đường!"),
        ("Käse", "der", "phô mai (Pl: die Käse)", "„Wir kaufen frischen Käse im Supermarkt.“ — Chúng tôi mua phô mai tươi ở siêu thị."),
        ("Salat", "der", "rau xà lách, món salad (Pl: die Salate)", "„Ich mache heute Abend einen Salat.“ — Tối nay tôi làm một món xà lách."),
        ("Hund", "der", "con chó (Pl: die Hunde)", "„Der Hund schläft gemütlich auf dem Sofa.“ — Chú chó đang ngủ thoải mái trên ghế sofa."),
        ("Brief", "der", "bức thư (Pl: die Briefe)", "„Anna schreibt einen langen Brief an ihre Oma.“ — Anna viết một bức thư dài cho bà của cô ấy."),
        ("Eis", "das", "kem, đá (Pl: nur Sg.)", "„Ich esse gern Eis.“ — Tôi thích ăn kem."),
        ("Futter", "das", "thức ăn thú cưng (Pl: nur Sg.)", "„Hannes gibt der Katze das Futter.“ — Hannes cho mèo ăn thức ăn."),
        ("Hotel", "das", "khách sạn (Pl: die Hotels)", "„Schläfst du im Hotel?“ — Bạn có ngủ ở khách sạn không?"),
        ("Rathaus", "das", "tòa thị chính (Pl: die Rathäuser)", "„Die Touristen besuchen das alte Rathaus.“ — Du khách tham quan tòa thị chính cũ."),
        ("Gemüse", "das", "rau củ (Pl: nur Sg.)", "„Gemüse ist sehr gesund für den Körper.“ — Rau củ rất tốt cho sức khỏe cơ thể."),
        # 6 thẻ mới từ B8 (đã loại 6 từ trùng: das Buch, der Lehrer, das Handy, die Küche, die Hausaufgabe, die Türkei)
        ("Mädchen", "das", "cô bé (Pl: die Mädchen)", "„Das Mädchen liest ein Buch.“ — Cô bé đang đọc một quyển sách."),
        ("Freund", "der", "bạn (Pl: die Freunde)", "„Wann triffst du deine Freunde?“ — Khi nào bạn gặp bạn bè của mình?"),
        ("Fußball", "der", "bóng đá (Pl: die Fußbälle)", "„Die Kinder spielen Fußball.“ — Bọn trẻ đang chơi bóng đá."),
        ("Musik", "die", "âm nhạc (Pl: nur Sg.)", "„Karin hört Musik.“ — Karin đang nghe nhạc."),
        ("Tennis", "das", "quần vợt (Pl: nur Sg.)", "„Spielt ihr Tennis?“ — Các bạn có chơi quần vợt không?"),
        ("Tourist", "der", "khách du lịch (Pl: die Touristen)", "„Die Touristen besuchen das Rathaus.“ — Khách du lịch tham quan tòa thị chính."),
        ("Speisekarte", "die", "thực đơn (Pl: die Speisekarten)", "„Wir lesen zusammen die Speisekarte.“ — Chúng tôi cùng nhau đọc thực đơn.")
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
            "extra_data": {
                "audio_text": "Meine Schwester liest am Abend oft einen Roman.",
                "translation": "Chị/em gái tôi buổi tối thường đọc một cuốn tiểu thuyết."
            }
        },
        {
            "id": 2,
            "exercise_type": "trac_nghiem",
            "question": "Câu 2: Chọn dạng đúng của động từ trong ngoặc:\n„Wann ___ ihr am Wochenende nach Berlin?“ (fahren)",
            "options": ["fährst", "fahrt", "fährt", "fahren"],
            "correct_answer": "fahrt",
            "explanation": "LƯU Ý: Ngôi ihr (các bạn) KHÔNG biến âm. Động từ „fahren“ bỏ đuôi -en thêm -t thành „fahrt“ -> Đáp án: fahrt.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wann fahrt ihr am Wochenende nach Berlin?", "translation": "Cuối tuần khi nào các bạn đi Berlin?"}
        },
        {
            "id": 3,
            "exercise_type": "trac_nghiem",
            "question": "Câu 3: Chọn từ để hỏi thích hợp:\n„___ kommst du, Maria?“ — „Aus Spanien.“",
            "options": ["Wo", "Wie", "Was", "Woher"],
            "correct_answer": "Woher",
            "explanation": "Câu trả lời dùng giới từ „Aus“ (từ) chỉ quê quán/xuất xứ, nên câu hỏi phải dùng từ để hỏi „Woher“ (từ đâu) -> Đáp án: Woher.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Woher kommst du, Maria? Aus Spanien.", "translation": "Maria, bạn đến từ đâu? — Từ Tây Ban Nha."}
        },
        {
            "id": 4,
            "exercise_type": "trac_nghiem",
            "question": "Câu 4: Chọn dạng đúng của động từ trong ngoặc:\n„Der Lehrer ___ heute sehr laut.“ (sprechen)",
            "options": ["sprechet", "sprech", "spricht", "spracht"],
            "correct_answer": "spricht",
            "explanation": "Chủ ngữ „Der Lehrer“ (er - anh ấy), động từ bất quy tắc „sprechen“ đổi e → i thành „spricht“ -> Đáp án: spricht.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Der Lehrer spricht heute sehr laut.", "translation": "Hôm nay thầy giáo nói rất to."}
        },
        {
            "id": 5,
            "exercise_type": "trac_nghiem",
            "question": "Câu 5: Chọn dạng đúng của động từ trong ngoặc:\n„Was ___ Hannes und Julia dem kleinen Hund?“ (geben)",
            "options": ["gibt", "gebt", "gibst", "geben"],
            "correct_answer": "geben",
            "explanation": "Chủ ngữ là „Hannes und Julia“ (họ - sie số nhiều), động từ giữ nguyên thể „geben“ -> Đáp án: geben.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Was geben Hannes und Julia dem kleinen Hund?", "translation": "Hannes và Julia cho chú chó nhỏ ăn gì?"}
        },
        {
            "id": 6,
            "exercise_type": "trac_nghiem",
            "question": "Câu 6: Chọn dạng đúng của động từ trong ngoặc:\n„Das Handy ___ in der Küche auf dem Tisch.“ (liegen)",
            "options": ["liegst", "lege", "liegt", "liegen"],
            "correct_answer": "liegt",
            "explanation": "Chủ ngữ „Das Handy“ (ngôi es) đi với động từ có quy tắc „liegen“ thêm đuôi -t thành „liegt“ -> Đáp án: liegt.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Das Handy liegt in der Küche auf dem Tisch.", "translation": "Chiếc điện thoại nằm ở trong bếp trên bàn."}
        },
        {
            "id": 7,
            "exercise_type": "trac_nghiem",
            "question": "Câu 7: Chọn dạng đúng của động từ trong ngoặc:\n„___ du heute Nacht bei mir?“ (schlafen)",
            "options": ["Schlafst", "Schläfst", "Schläft", "Schlafen"],
            "correct_answer": "Schläfst",
            "explanation": "Chủ ngữ ngôi „du“, động từ „schlafen“ đổi a → ä và thêm đuôi -st thành „Schläfst“ -> Đáp án: Schläfst.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Schläfst du heute Nacht bei mir?", "translation": "Tối nay bạn có ngủ ở chỗ tôi không?"}
        },
        {
            "id": 8,
            "exercise_type": "trac_nghiem",
            "question": "Câu 8: Chọn đại từ nhân xưng thích hợp:\n„Der Vater grillt am Sonntag Fleisch. ___ macht auch einen Salat.“",
            "options": ["Er", "Sie", "Es", "Ihr"],
            "correct_answer": "Er",
            "explanation": "Đại từ thay thế cho danh từ giống đực „Der Vater“ là „Er“ (anh ấy/ông ấy) -> Đáp án: Er.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Der Vater grillt am Sonntag Fleisch. Er macht auch einen Salat.",
                "translation": "Người bố nướng thịt vào Chủ nhật. Ông ấy cũng làm một món salad."
            }
        },
        {
            "id": 9,
            "exercise_type": "trac_nghiem",
            "question": "Câu 9: Chọn câu hỏi ĐÚNG cho câu trả lời sau:\n„Ich trinke Kaffee mit Zucker.“",
            "options": ["Wo wohnst du?", "Was trinken Sie?", "Wie heißt du?", "Wer trinkt Tee?"],
            "correct_answer": "Was trinken Sie?",
            "explanation": "Câu trả lời nói về loại đồ uống („Kaffee“), nên câu hỏi phù hợp nhất là „Was trinken Sie?“ (Ngài uống gì?) -> Đáp án: Was trinken Sie?.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Was trinken Sie? Ich trinke Kaffee mit Zucker.", "translation": "Ngài uống gì? Tôi uống cà phê với đường."}
        },
        {
            "id": 10,
            "exercise_type": "trac_nghiem",
            "question": "Câu 10: Chọn dạng động từ tobe đúng cho câu giao tiếp:\n„Entschuldigung, ___ hier frei?“",
            "options": ["ist", "sind", "bin", "bist"],
            "correct_answer": "ist",
            "explanation": "Chủ ngữ giả định cho chỗ ngồi/nơi chốn là es, đi với động từ tobe „ist“ (Ist hier frei? = Chỗ này còn trống không?) -> Đáp án: ist.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Entschuldigung, ist hier frei?", "translation": "Xin lỗi, chỗ này còn trống không?"}
        },
        {
            "id": 11,
            "exercise_type": "trac_nghiem",
            "question": "Câu 11: Chọn dạng đúng của động từ trong ngoặc:\n„Wann ___ du deine Freunde im Café?“ (treffen)",
            "options": ["treffst", "triffst", "trifft", "treffen"],
            "correct_answer": "triffst",
            "explanation": "Ngôi „du“, động từ bất quy tắc „treffen“ đổi e → i thành „triffst“ -> Đáp án: triffst.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wann triffst du deine Freunde im Café?", "translation": "Khi nào bạn gặp bạn bè ở quán cà phê?"}
        },
        {
            "id": 12,
            "exercise_type": "trac_nghiem",
            "question": "Câu 12: Chọn dạng đúng của động từ trong ngoặc:\n„Wir ___ im Sommer gern Vanilleeis.“ (essen)",
            "options": ["isst", "esse", "essen", "esst"],
            "correct_answer": "essen",
            "explanation": "Chủ ngữ ngôi „wir“ (chúng tôi) luôn dùng động từ nguyên thể „essen“ -> Đáp án: essen.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wir essen im Sommer gern Vanilleeis.", "translation": "Mùa hè chúng tôi thích ăn kem vani."}
        },
        {
            "id": 13,
            "exercise_type": "trac_nghiem",
            "question": "Câu 13: Chọn dạng đúng của động từ trong ngoặc:\n„Julia und Lara ___ nach Italien.“ (reisen)",
            "options": ["reist", "reisen", "reisst", "reise"],
            "correct_answer": "reisen",
            "explanation": "Chủ ngữ số nhiều „Julia und Lara“ (họ - sie số nhiều), động từ giữ nguyên thể „reisen“ -> Đáp án: reisen.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Julia und Lara reisen nach Italien.", "translation": "Julia và Lara đi du lịch đến Ý."}
        },
        {
            "id": 14,
            "exercise_type": "trac_nghiem",
            "question": "Câu 14: Chọn từ để hỏi thích hợp:\n„___ wohnen Sie jetzt?“ — „In München.“",
            "options": ["Woher", "Was", "Wie", "Wo"],
            "correct_answer": "Wo",
            "explanation": "Câu trả lời dùng giới từ „In“ chỉ địa điểm cư trú, câu hỏi về nơi ở dùng „Wo“ (ở đâu) -> Đáp án: Wo.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Wo wohnen Sie jetzt? In München.", "translation": "Hiện tại ngài sống ở đâu? — Ở München."}
        },
        {
            "id": 15,
            "exercise_type": "trac_nghiem",
            "question": "Câu 15: Chọn dạng đúng của động từ trong ngoặc:\n„Die Touristen ___ das alte Rathaus.“ (besuchen)",
            "options": ["besucht", "besuche", "besuchen", "besuchst"],
            "correct_answer": "besuchen",
            "explanation": "Chủ ngữ „Die Touristen“ (số nhiều - họ) đi với động từ nguyên thể „besuchen“ -> Đáp án: besuchen.",
            "exp_reward": 10,
            "extra_data": {"audio_text": "Die Touristen besuchen das alte Rathaus.", "translation": "Khách du lịch tham quan tòa thị chính cũ."}
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
            "extra_data": {
                "accepted_answers": [
                    "Wie",
                    "wie"
                ],
                "audio_text": "Wie heißt du? Ich heiße David.",
                "translation": "Bạn tên là gì? — Tôi tên là David."
            }
        },
        {
            "id": 17,
            "exercise_type": "dien_khuyet",
            "question": "Câu 17: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Wir ___ den Käse im Supermarkt.“ (kaufen)",
            "options": null,
            "correct_answer": "kaufen",
            "explanation": "Chủ ngữ „wir“ đi với động từ nguyên thể „kaufen“ -> Đáp án: kaufen.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "kaufen"
                ],
                "audio_text": "Wir kaufen den Käse im Supermarkt.",
                "translation": "Chúng tôi mua phô mai ở siêu thị."
            }
        },
        {
            "id": 18,
            "exercise_type": "dien_khuyet",
            "question": "Câu 18: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Mein Onkel ___ gern schwarzen Tee.“ (trinken)",
            "options": null,
            "correct_answer": "trinkt",
            "explanation": "Chủ ngữ „Mein Onkel“ (er - anh ấy), động từ có quy tắc „trinken“ thêm đuôi -t thành „trinkt“ -> Đáp án: trinkt.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "trinkt"
                ],
                "audio_text": "Mein Onkel trinkt gern schwarzen Tee.",
                "translation": "Chú của tôi thích uống trà đen."
            }
        },
        {
            "id": 19,
            "exercise_type": "dien_khuyet",
            "question": "Câu 19: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Ich ___ meine Hausaufgaben.“ (machen)",
            "options": null,
            "correct_answer": "mache",
            "explanation": "Chủ ngữ „ich“ đi với động từ có quy tắc thêm đuôi -e thành „mache“ -> Đáp án: mache.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["mache"], "audio_text": "Ich mache meine Hausaufgaben.", "translation": "Tôi làm bài tập về nhà của mình."}
        },
        {
            "id": 20,
            "exercise_type": "dien_khuyet",
            "question": "Câu 20: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Die Kinder ___ Fußball auf dem Hof.“ (spielen)",
            "options": null,
            "correct_answer": "spielen",
            "explanation": "Chủ ngữ số nhiều „Die Kinder“ (bọn trẻ - sie Plural), động từ giữ nguyên thể „spielen“ -> Đáp án: spielen.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "spielen"
                ],
                "audio_text": "Die Kinder spielen Fußball auf dem Hof.",
                "translation": "Bọn trẻ đang chơi bóng đá ngoài sân."
            }
        },
        {
            "id": 21,
            "exercise_type": "dien_khuyet",
            "question": "Câu 21: Điền động từ khuyết thiếu thể hiện mong muốn lịch sự:\n„Herr Müller, was ___ Sie trinken?“ (muốn)",
            "options": null,
            "correct_answer": "möchten",
            "explanation": "Động từ khuyết thiếu chỉ sự mong muốn lịch sự đi với ngôi Ngài (Sie) là „möchten“ -> Đáp án: möchten.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "möchten",
                    "moechten"
                ],
                "audio_text": "Herr Müller, was möchten Sie trinken?",
                "translation": "Ông Müller, ngài muốn uống gì ạ?"
            }
        },
        {
            "id": 22,
            "exercise_type": "dien_khuyet",
            "question": "Câu 22: Điền giới từ chỉ xuất xứ vào chỗ trống:\n„Ich komme ___ Frankreich.“ (từ)",
            "options": null,
            "correct_answer": "aus",
            "explanation": "Giới từ chỉ nơi xuất xứ đi với động từ kommen là „aus“ -> Đáp án: aus.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["aus"], "audio_text": "Ich komme aus Frankreich.", "translation": "Tôi đến từ nước Pháp."}
        },
        {
            "id": 23,
            "exercise_type": "dien_khuyet",
            "question": "Câu 23: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„___ ihr einen Brief an die Großmutter?“ (schreiben)",
            "options": null,
            "correct_answer": "Schreibt",
            "explanation": "Ngôi „ihr“ (các bạn), động từ „schreiben“ thêm đuôi -t và đứng đầu câu hỏi đảo là „Schreibt“ -> Đáp án: Schreibt.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Schreibt",
                    "schreibt"
                ],
                "audio_text": "Schreibt ihr einen Brief an die Großmutter?",
                "translation": "Các bạn đang viết một bức thư gửi cho bà phải không?"
            }
        },
        {
            "id": 24,
            "exercise_type": "dien_khuyet",
            "question": "Câu 24: Điền dạng đúng của động từ trong ngoặc vào chỗ trống:\n„Karin ___ sehr gern klassische Musik.“ (hören)",
            "options": null,
            "correct_answer": "hört",
            "explanation": "Chủ ngữ Karin (ngôi sie số ít), động từ „hören“ thêm đuôi -t thành „hört“ -> Đáp án: hört.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "hört",
                    "hoert"
                ],
                "audio_text": "Karin hört sehr gern klassische Musik.",
                "translation": "Karin rất thích nghe nhạc cổ điển."
            }
        },
        {
            "id": 25,
            "exercise_type": "dien_khuyet",
            "question": "Câu 25: Điền từ để hỏi thích hợp vào chỗ trống:\n„___ singst du so gern?“ — „Weil ich Musik liebe.“",
            "options": null,
            "correct_answer": "Warum",
            "explanation": "Câu trả lời bắt đầu bằng „Weil“ (bởi vì), câu hỏi nguyên nhân phải dùng „Warum“ (tại sao) -> Đáp án: Warum.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Warum",
                    "warum"
                ],
                "audio_text": "Warum singst du so gern? Weil ich Musik liebe.",
                "translation": "Tại sao bạn thích hát thế? — Bởi vì tôi yêu âm nhạc."
            }
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
            "extra_data": {
                "accepted_answers": [
                    "liest"
                ],
                "audio_text": "Das Mädchen liest im Wohnzimmer ein Buch.",
                "translation": "Cô bé đang đọc một quyển sách trong phòng khách."
            }
        },
        {
            "id": 27,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 27: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Er ___ am Sonntag nach Hamburg.“ (fahren)",
            "options": null,
            "correct_answer": "fährt",
            "explanation": "Ngôi „er“, động từ bất quy tắc „fahren“ đổi a → ä thành „fährt“ -> Đáp án: fährt.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "fährt",
                    "faehrt"
                ],
                "audio_text": "Er fährt am Sonntag nach Hamburg.",
                "translation": "Anh ấy đi Hamburg vào Chủ nhật."
            }
        },
        {
            "id": 28,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 28: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Was ___ du heute zum Frühstück?“ (essen)",
            "options": null,
            "correct_answer": "isst",
            "explanation": "Ngôi „du“, động từ bất quy tắc „essen“ đổi e → i thành „isst“ -> Đáp án: isst.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "isst"
                ],
                "audio_text": "Was isst du heute zum Frühstück?",
                "translation": "Hôm nay bạn ăn gì cho bữa sáng?"
            }
        },
        {
            "id": 29,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 29: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Der Tourist ___ fließend Deutsch.“ (sprechen)",
            "options": null,
            "correct_answer": "spricht",
            "explanation": "Chủ ngữ „Der Tourist“ (ngôi er), động từ „sprechen“ đổi e → i thành „spricht“ -> Đáp án: spricht.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "spricht"
                ],
                "audio_text": "Der Tourist spricht fließend Deutsch.",
                "translation": "Người khách du lịch nói tiếng Đức trôi chảy."
            }
        },
        {
            "id": 30,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 30: Chia động từ mệnh lệnh ngôi du của động từ trong ngoặc:\n„Bitte ___ mir den Zucker!“ (geben - ngôi du)",
            "options": null,
            "correct_answer": "gib",
            "explanation": "Mệnh lệnh ngôi du của động từ bất quy tắc „geben“ (e → i) lược bỏ đuôi -st thành „gib“ -> Đáp án: gib.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["gib", "Gib"], "audio_text": "Bitte gib mir den Zucker!", "translation": "Làm ơn đưa cho tôi lọ đường!"}
        },
        {
            "id": 31,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 31: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Wann ___ er seine neue Freundin?“ (treffen)",
            "options": null,
            "correct_answer": "trifft",
            "explanation": "Ngôi „er“, động từ bất quy tắc „treffen“ đổi e → i thành „trifft“ -> Đáp án: trifft.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "trifft"
                ],
                "audio_text": "Wann trifft er seine neue Freundin?",
                "translation": "Khi nào anh ấy gặp người bạn gái mới của mình?"
            }
        },
        {
            "id": 32,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 32: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Der Hund ___ gemütlich auf dem Sofa.“ (schlafen)",
            "options": null,
            "correct_answer": "schläft",
            "explanation": "Chủ ngữ „Der Hund“ (ngôi er), động từ „schlafen“ đổi a → ä thành „schläft“ -> Đáp án: schläft.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "schläft",
                    "schlaeft"
                ],
                "audio_text": "Der Hund schläft gemütlich auf dem Sofa.",
                "translation": "Chú chó ngủ thoải mái trên ghế sofa."
            }
        },
        {
            "id": 33,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 33: Chia động từ trong ngoặc theo đúng chủ ngữ:\n„Ihr ___ am Wochenende zu lange!“ (schlafen)",
            "options": null,
            "correct_answer": "schlaft",
            "explanation": "LƯU Ý QUAN TRỌNG: Ngôi ihr (các bạn) KHÔNG BAO GIỜ biến âm. „schlafen“ chỉ thêm đuôi -t thành „schlaft“ -> Đáp án: schlaft.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "schlaft"
                ],
                "audio_text": "Ihr schlaft am Wochenende zu lange!",
                "translation": "Cuối tuần các bạn ngủ quá lâu đấy!"
            }
        },
        {
            "id": 34,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 34: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„___ du gern Romane oder Zeitungen?“ (lesen)",
            "options": null,
            "correct_answer": "Liest",
            "explanation": "Ngôi „du“, động từ bất quy tắc „lesen“ đổi e → ie đứng đầu câu hỏi là „Liest“ -> Đáp án: Liest.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Liest",
                    "liest"
                ],
                "audio_text": "Liest du gern Romane oder Zeitungen?",
                "translation": "Bạn thích đọc tiểu thuyết hay báo?"
            }
        },
        {
            "id": 35,
            "exercise_type": "dien_chia_dong_tu",
            "question": "Câu 35: Chia động từ bất quy tắc trong ngoặc theo đúng chủ ngữ:\n„Die Chefin ___ gerade mit einem Kunden.“ (sprechen)",
            "options": null,
            "correct_answer": "spricht",
            "explanation": "Chủ ngữ „Die Chefin“ (ngôi sie số ít), động từ „sprechen“ đổi e → i thành „spricht“ -> Đáp án: spricht.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "spricht"
                ],
                "audio_text": "Die Chefin spricht gerade mit einem Kunden.",
                "translation": "Nữ sếp đang nói chuyện với một khách hàng."
            }
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
            "extra_data": {"accepted_answers": ["der Kaffee", "Kaffee", "der kaffee", "kaffee"], "audio_text": "der Kaffee", "translation": "cà phê"}
        },
        {
            "id": 37,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 37: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„trà“",
            "options": null,
            "correct_answer": "der Tee",
            "explanation": "Trà trong tiếng Đức là danh từ giống đực: „der Tee“ -> Đáp án: der Tee.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["der Tee", "Tee", "der tee", "tee"], "audio_text": "der Tee", "translation": "trà"}
        },
        {
            "id": 38,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 38: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„rau củ“",
            "options": null,
            "correct_answer": "das Gemüse",
            "explanation": "Rau củ trong tiếng Đức là danh từ giống trung: „das Gemüse“ -> Đáp án: das Gemüse.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "das Gemüse",
                    "Gemüse",
                    "das Gemuese",
                    "Gemuese",
                    "das gemüse",
                    "gemüse"
                ],
                "audio_text": "das Gemüse",
                "translation": "rau củ"
            }
        },
        {
            "id": 39,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 39: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„bức thư“",
            "options": null,
            "correct_answer": "der Brief",
            "explanation": "Bức thư trong tiếng Đức là danh từ giống đực: „der Brief“ -> Đáp án: der Brief.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["der Brief", "Brief", "der brief", "brief"], "audio_text": "der Brief", "translation": "bức thư"}
        },
        {
            "id": 40,
            "exercise_type": "dich_nghia_vd",
            "question": "Câu 40: Dịch từ sau sang tiếng Đức (kèm mạo từ xác định):\n„tòa thị chính“",
            "options": null,
            "correct_answer": "das Rathaus",
            "explanation": "Tòa thị chính là danh từ ghép giống trung (der Rat + das Haus) -> „das Rathaus“ -> Đáp án: das Rathaus.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "das Rathaus",
                    "Rathaus",
                    "das rathaus",
                    "rathaus"
                ],
                "audio_text": "das Rathaus",
                "translation": "tòa thị chính"
            }
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
            "extra_data": {
                "accepted_answers": [
                    "Xin lỗi, chỗ này còn trống không?",
                    "Xin lỗi chỗ này còn trống không?",
                    "Xin lỗi, ở đây còn trống không?",
                    "Xin lỗi ở đây còn trống không?",
                    "Xin lỗi, chỗ này trống không?",
                    "Xin lỗi chỗ này trống không?"
                ],
                "audio_text": "Entschuldigung, ist hier frei?",
                "translation": "Xin lỗi, chỗ này còn trống không?"
            }
        },
        {
            "id": 42,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 42: Dịch câu đáp lại sau sang tiếng Việt:\n„Ja klar, bitte.“",
            "options": null,
            "correct_answer": "Vâng tất nhiên, xin mời.",
            "explanation": "Câu trả lời đồng ý nhiệt tình cho người khác ngồi cùng bàn: „Vâng tất nhiên, xin mời.“ -> Đáp án: Vâng tất nhiên, xin mời..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Vâng tất nhiên, xin mời.",
                    "Vâng, xin mời.",
                    "Tất nhiên rồi, xin mời.",
                    "Vâng tất nhiên xin mời.",
                    "Được chứ, xin mời.",
                    "Tất nhiên, xin mời."
                ],
                "audio_text": "Ja klar, bitte.",
                "translation": "Vâng tất nhiên, xin mời."
            }
        },
        {
            "id": 43,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 43: Dịch câu gọi món sau sang tiếng Việt:\n„Zwei Kaffee, bitte!“",
            "options": null,
            "correct_answer": "Xin cho hai cà phê!",
            "explanation": "Cách gọi món nhanh và lịch sự trong quán cà phê: „Xin cho hai cà phê!“ -> Đáp án: Xin cho hai cà phê!.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Xin cho hai cà phê!",
                    "Hai cà phê, làm ơn!",
                    "Cho hai cà phê!",
                    "Làm ơn cho hai cà phê!",
                    "Hai ly cà phê, làm ơn!",
                    "Hai cốc cà phê, làm ơn!"
                ],
                "audio_text": "Zwei Kaffee, bitte!",
                "translation": "Xin cho hai cà phê!"
            }
        },
        {
            "id": 44,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 44: Dịch danh từ sau sang tiếng Việt:\n„das Futter“",
            "options": null,
            "correct_answer": "thức ăn thú cưng",
            "explanation": "Danh từ „das Futter“ dùng riêng để chỉ thức ăn dành cho thú cưng / động vật -> Đáp án: thức ăn thú cưng.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "thức ăn thú cưng",
                    "thức ăn cho thú",
                    "thức ăn động vật",
                    "thức ăn gia súc",
                    "thức ăn cho động vật",
                    "thức ăn"
                ],
                "audio_text": "das Futter",
                "translation": "thức ăn thú cưng"
            }
        },
        {
            "id": 45,
            "exercise_type": "dich_nghia_dv",
            "question": "Câu 45: Dịch danh từ sau sang tiếng Việt:\n„der Käse“",
            "options": null,
            "correct_answer": "phô mai",
            "explanation": "Danh từ „der Käse“ trong tiếng Đức nghĩa là „phô mai“ -> Đáp án: phô mai.",
            "exp_reward": 10,
            "extra_data": {"accepted_answers": ["phô mai", "pho mát", "pho mai", "phomai"], "audio_text": "der Käse", "translation": "phô mai"}
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
                    {
                        "left": "ich",
                        "right": "spreche"
                    },
                    {
                        "left": "du",
                        "right": "sprichst"
                    },
                    {
                        "left": "er",
                        "right": "spricht"
                    },
                    {
                        "left": "ihr",
                        "right": "sprecht"
                    }
                ],
                "audio_text": "ich spreche. du sprichst. er spricht. ihr sprecht.",
                "translation": "ich spreche: tôi nói | du sprichst: bạn nói | er spricht: anh ấy nói | ihr sprecht: các bạn nói"
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
                    {
                        "left": "wir",
                        "right": "fahren"
                    },
                    {
                        "left": "du",
                        "right": "fährst"
                    },
                    {
                        "left": "sie (cô ấy)",
                        "right": "fährt"
                    },
                    {
                        "left": "ihr",
                        "right": "fahrt"
                    }
                ],
                "audio_text": "wir fahren. du fährst. sie fährt. ihr fahrt.",
                "translation": "wir fahren: chúng tôi đi | du fährst: bạn đi | sie fährt: cô ấy đi | ihr fahrt: các bạn đi"
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
                    {
                        "left": "ich",
                        "right": "schlafe"
                    },
                    {
                        "left": "du",
                        "right": "schläfst"
                    },
                    {
                        "left": "es",
                        "right": "schläft"
                    },
                    {
                        "left": "ihr",
                        "right": "schlaft"
                    }
                ],
                "audio_text": "ich schlafe. du schläfst. es schläft. ihr schlaft.",
                "translation": "ich schlafe: tôi ngủ | du schläfst: bạn ngủ | es schläft: nó ngủ | ihr schlaft: các bạn ngủ"
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
                    {
                        "left": "Woher kommen Sie?",
                        "right": "Aus Vietnam."
                    },
                    {
                        "left": "Wo wohnen Sie?",
                        "right": "In Berlin."
                    },
                    {
                        "left": "Wie heißen Sie?",
                        "right": "Ich bin Anna."
                    },
                    {
                        "left": "Was trinken Sie?",
                        "right": "Kaffee, bitte."
                    }
                ],
                "audio_text": "Woher kommen Sie? Aus Vietnam. Wo wohnen Sie? In Berlin. Wie heißen Sie? Ich bin Anna. Was trinken Sie? Kaffee, bitte.",
                "translation": "Woher kommen Sie? — Aus Vietnam (Từ Việt Nam) | Wo wohnen Sie? — In Berlin (Ở Berlin) | Wie heißen Sie? — Ich bin Anna (Tôi là Anna) | Was trinken Sie? — Kaffee, bitte (Cho cà phê ạ)"
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
                    {
                        "left": "der Zucker",
                        "right": "đường"
                    },
                    {
                        "left": "das Rathaus",
                        "right": "tòa thị chính"
                    },
                    {
                        "left": "der Brief",
                        "right": "bức thư"
                    },
                    {
                        "left": "der Hund",
                        "right": "con chó"
                    }
                ],
                "audio_text": "der Zucker. das Rathaus. der Brief. der Hund.",
                "translation": "der Zucker: đường | das Rathaus: tòa thị chính | der Brief: bức thư | der Hund: con chó"
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
                    {
                        "left": "Ist hier frei?",
                        "right": "Ja klar, bitte."
                    },
                    {
                        "left": "Was möchten Sie trinken?",
                        "right": "Einen Tee, bitte."
                    },
                    {
                        "left": "Ich bin John.",
                        "right": "Ich heiße Maria."
                    },
                    {
                        "left": "Trinkst du Kaffee oder Tee?",
                        "right": "Kaffee mit Zucker."
                    }
                ],
                "audio_text": "Ist hier frei? Ja klar, bitte. Was möchten Sie trinken? Einen Tee, bitte. Ich bin John. Ich heiße Maria. Trinkst du Kaffee oder Tee? Kaffee mit Zucker.",
                "translation": "Ist hier frei? — Ja klar, bitte. | Was möchten Sie trinken? — Einen Tee, bitte. | Ich bin John. — Ich heiße Maria. | Trinkst du Kaffee oder Tee? — Kaffee mit Zucker."
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
                    {
                        "left": "ich",
                        "right": "lese"
                    },
                    {
                        "left": "du",
                        "right": "liest"
                    },
                    {
                        "left": "er",
                        "right": "liest"
                    },
                    {
                        "left": "ihr",
                        "right": "lest"
                    }
                ],
                "audio_text": "ich lese. du liest. er liest. ihr lest.",
                "translation": "ich lese: tôi đọc | du liest: bạn đọc | er liest: anh ấy đọc | ihr lest: các bạn đọc"
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
                    {
                        "left": "geben",
                        "right": "cho, đưa"
                    },
                    {
                        "left": "treffen",
                        "right": "gặp gỡ"
                    },
                    {
                        "left": "reisen",
                        "right": "du lịch"
                    },
                    {
                        "left": "grillen",
                        "right": "nướng BBQ"
                    }
                ],
                "audio_text": "geben. treffen. reisen. grillen.",
                "translation": "geben: cho, đưa | treffen: gặp gỡ | reisen: du lịch | grillen: nướng BBQ"
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
                    {
                        "left": "ich",
                        "right": "bin"
                    },
                    {
                        "left": "du",
                        "right": "bist"
                    },
                    {
                        "left": "wir",
                        "right": "haben"
                    },
                    {
                        "left": "er",
                        "right": "hat"
                    }
                ],
                "audio_text": "ich bin. du bist. wir haben. er hat.",
                "translation": "ich bin: tôi là | du bist: bạn là | wir haben: chúng tôi có | er hat: anh ấy có"
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
                    {
                        "left": "Das Mädchen",
                        "right": "isst Eis."
                    },
                    {
                        "left": "Die Kinder",
                        "right": "essen Eis."
                    },
                    {
                        "left": "Ich",
                        "right": "esse Eis."
                    },
                    {
                        "left": "Ihr",
                        "right": "esst Eis."
                    }
                ],
                "audio_text": "Das Mädchen isst Eis. Die Kinder essen Eis. Ich esse Eis. Ihr esst Eis.",
                "translation": "Das Mädchen isst Eis: Cô bé ăn kem | Die Kinder essen Eis: Bọn trẻ ăn kem | Ich esse Eis: Tôi ăn kem | Ihr esst Eis: Các bạn ăn kem"
            }
        },

        # --- 3.7. ĐIỀN 2 CHỖ TRỐNG TẠO CÂU (8 CÂU) ---
        {
            "id": 56,
            "exercise_type": "dien_tao_cau",
            "question": "Câu 56: Điền 2 từ vào chỗ trống [1] và [2] (cách nhau bởi dấu /):\n„[1] heißt du und woher [2] du?“",
            "options": null,
            "correct_answer": "Wie / kommst",
            "explanation": "Hỏi tên dùng từ để hỏi „Wie“; chủ ngữ ngôi du đi với kommen thành „kommst“ -> Đáp án: Wie / kommst.",
            "exp_reward": 15,
            "extra_data": {
                "display_frame": "[1] heißt du und woher [2] du?",
                "accepted_answers": [
                    "Wie / kommst",
                    "Wie/kommst",
                    "Wie kommst",
                    "wie / kommst",
                    "wie/kommst"
                ],
                "audio_text": "Wie heißt du und woher kommst du?",
                "translation": "Bạn tên là gì và bạn đến từ đâu?"
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
                "accepted_answers": [
                    "besuchen / machen",
                    "besuchen/machen",
                    "besuchen machen"
                ],
                "audio_text": "Die Touristen besuchen das Rathaus und machen Fotos.",
                "translation": "Khách du lịch tham quan tòa thị chính và chụp ảnh."
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
                "accepted_answers": [
                    "fährt / trifft",
                    "fährt/trifft",
                    "faehrt / trifft",
                    "faehrt/trifft",
                    "fährt trifft"
                ],
                "audio_text": "Mein Bruder fährt am Wochenende nach München. Er trifft dort Freunde.",
                "translation": "Anh trai tôi đi München vào cuối tuần. Anh ấy gặp bạn bè ở đó."
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
                "accepted_answers": [
                    "Wo / schläft",
                    "Wo/schläft",
                    "Wo / schlaeft",
                    "Wo/schlaeft",
                    "Wo schläft",
                    "wo / schläft"
                ],
                "audio_text": "Wo schläft das Baby? Es schläft im Schlafzimmer.",
                "translation": "Em bé ngủ ở đâu? — Em bé ngủ trong phòng ngủ."
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
                "accepted_answers": [
                    "grillen / grillt",
                    "grillen/grillt",
                    "grillen grillt"
                ],
                "audio_text": "Wir grillen gern Fleisch, aber Anna grillt lieber Gemüse.",
                "translation": "Chúng tôi thích nướng thịt, nhưng Anna thích nướng rau củ hơn."
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
                "accepted_answers": [
                    "trinkt / trinken",
                    "trinkt/trinken",
                    "trinkt trinken"
                ],
                "audio_text": "Was trinkt ihr? Kaffee oder Tee? Wir trinken Tee.",
                "translation": "Các bạn uống gì? Cà phê hay trà? — Chúng tôi uống trà."
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
                "accepted_answers": [
                    "Woher / Aus",
                    "Woher/Aus",
                    "Woher Aus",
                    "woher / aus",
                    "woher/aus"
                ],
                "audio_text": "Woher kommen Sie? Aus der Türkei.",
                "translation": "Ngài đến từ đâu? — Từ Thổ Nhĩ Kỳ."
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
                "accepted_answers": [
                    "Was / esse",
                    "Was/esse",
                    "Was esse",
                    "was / esse",
                    "was/esse"
                ],
                "audio_text": "Was isst du gern? Ich esse gern Käse.",
                "translation": "Bạn thích ăn gì? — Tôi thích ăn phô mai."
            }
        },

        # --- 3.8. NGHE CHÉP CHÍNH TẢ - DICTATION (8 CÂU) ---
        {
            "id": 64,
            "exercise_type": "nghe_dien",
            "question": "Câu 64: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Der Vater liest die Zeitung.",
            "explanation": "Động từ bất quy tắc lesen ngôi er đổi e → ie là „liest“. Câu hoàn chỉnh: „Der Vater liest die Zeitung.“ -> Đáp án: Der Vater liest die Zeitung.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Der Vater liest die Zeitung.",
                "full_sentence": "Der Vater liest die Zeitung.",
                "dictation_mode": True,
                "translation": "Người bố đọc báo.",
                "accepted_answers": [
                    "Der Vater liest die Zeitung.",
                    "Der Vater liest die Zeitung"
                ]
            }
        },
        {
            "id": 65,
            "exercise_type": "nghe_dien",
            "question": "Câu 65: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Wann fahrt ihr nach Hause?",
            "explanation": "Ngôi ihr không biến âm, phát âm âm a ngắn trong „fahrt“. Câu hoàn chỉnh: „Wann fahrt ihr nach Hause?“ -> Đáp án: Wann fahrt ihr nach Hause?",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Wann fahrt ihr nach Hause?",
                "full_sentence": "Wann fahrt ihr nach Hause?",
                "dictation_mode": True,
                "translation": "Khi nào các bạn về nhà?",
                "accepted_answers": [
                    "Wann fahrt ihr nach Hause?",
                    "Wann fahrt ihr nach Hause"
                ]
            }
        },
        {
            "id": 66,
            "exercise_type": "nghe_dien",
            "question": "Câu 66: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Ich komme aus Vietnam.",
            "explanation": "Giới từ chỉ nơi xuất xứ đi với kommen là „aus“. Câu hoàn chỉnh: „Ich komme aus Vietnam.“ -> Đáp án: Ich komme aus Vietnam.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Ich komme aus Vietnam.",
                "full_sentence": "Ich komme aus Vietnam.",
                "dictation_mode": True,
                "translation": "Tôi đến từ Việt Nam.",
                "accepted_answers": [
                    "Ich komme aus Vietnam.",
                    "Ich komme aus Vietnam"
                ]
            }
        },
        {
            "id": 67,
            "exercise_type": "nghe_dien",
            "question": "Câu 67: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Das Kind isst ein Eis.",
            "explanation": "Chủ ngữ Das Kind (ngôi es), động từ essen đổi e → i thành „isst“. Câu hoàn chỉnh: „Das Kind isst ein Eis.“ -> Đáp án: Das Kind isst ein Eis.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Das Kind isst ein Eis.",
                "full_sentence": "Das Kind isst ein Eis.",
                "dictation_mode": True,
                "translation": "Đứa trẻ ăn một cây kem.",
                "accepted_answers": [
                    "Das Kind isst ein Eis.",
                    "Das Kind isst ein Eis"
                ]
            }
        },
        {
            "id": 68,
            "exercise_type": "nghe_dien",
            "question": "Câu 68: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Sprichst du Deutsch?",
            "explanation": "Động từ sprechen đổi e → i ở ngôi du đứng đầu câu hỏi Yes/No: „Sprichst“. Câu hoàn chỉnh: „Sprichst du Deutsch?“ -> Đáp án: Sprichst du Deutsch?",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Sprichst du Deutsch?",
                "full_sentence": "Sprichst du Deutsch?",
                "dictation_mode": True,
                "translation": "Bạn có nói tiếng Đức không?",
                "accepted_answers": [
                    "Sprichst du Deutsch?",
                    "Sprichst du Deutsch"
                ]
            }
        },
        {
            "id": 69,
            "exercise_type": "nghe_dien",
            "question": "Câu 69: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Wir wohnen in Berlin.",
            "explanation": "Giới từ chỉ địa điểm cư trú trong thành phố là „in“. Câu hoàn chỉnh: „Wir wohnen in Berlin.“ -> Đáp án: Wir wohnen in Berlin.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Wir wohnen in Berlin.",
                "full_sentence": "Wir wohnen in Berlin.",
                "dictation_mode": True,
                "translation": "Chúng tôi sống ở Berlin.",
                "accepted_answers": [
                    "Wir wohnen in Berlin.",
                    "Wir wohnen in Berlin"
                ]
            }
        },
        {
            "id": 70,
            "exercise_type": "nghe_dien",
            "question": "Câu 70: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Zwei Kaffee, bitte!",
            "explanation": "Cụm gọi đồ uống lịch sự: „Zwei Kaffee, bitte!“. Danh từ Kaffee và từ đứng đầu câu cần viết hoa -> Đáp án: Zwei Kaffee, bitte!",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Zwei Kaffee, bitte!",
                "full_sentence": "Zwei Kaffee, bitte!",
                "dictation_mode": True,
                "translation": "Xin cho hai cà phê!",
                "accepted_answers": [
                    "Zwei Kaffee, bitte!",
                    "Zwei Kaffee, bitte"
                ]
            }
        },
        {
            "id": 71,
            "exercise_type": "nghe_dien",
            "question": "Câu 71: Nghe Audio và gõ lại trọn vẹn câu tiếng Đức bạn nghe được:",
            "options": null,
            "correct_answer": "Der Hund schläft auf dem Sofa.",
            "explanation": "Chủ ngữ Der Hund (er), động từ schlafen đổi a → ä thành „schläft“. Câu hoàn chỉnh: „Der Hund schläft auf dem Sofa.“ -> Đáp án: Der Hund schläft auf dem Sofa.",
            "exp_reward": 10,
            "extra_data": {
                "audio_text": "Der Hund schläft auf dem Sofa.",
                "full_sentence": "Der Hund schläft auf dem Sofa.",
                "dictation_mode": True,
                "translation": "Chú chó ngủ trên ghế sofa.",
                "accepted_answers": [
                    "Der Hund schläft auf dem Sofa.",
                    "Der Hund schläft auf dem Sofa",
                    "Der Hund schlaeft auf dem Sofa.",
                    "Der Hund schlaeft auf dem Sofa"
                ]
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
            "extra_data": {
                "accepted_answers": [
                    "Ich komme aus Deutschland.",
                    "Ich komme aus Deutschland"
                ],
                "audio_text": "Ich komme aus Deutschland.",
                "translation": "Tôi đến từ nước Đức."
            }
        },
        {
            "id": 73,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 73: Dịch câu sau sang tiếng Đức:\n„Bạn sống ở đâu?“",
            "options": null,
            "correct_answer": "Wo wohnst du?",
            "explanation": "Từ để hỏi Wo + động từ wohnen chia theo ngôi du là „Wo wohnst du?“ (hoặc ngôi Sie: „Wo wohnen Sie?“) -> Đáp án: Wo wohnst du?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Wo wohnst du?",
                    "Wo wohnst du",
                    "Wo wohnen Sie?",
                    "Wo wohnen Sie"
                ],
                "audio_text": "Wo wohnst du?",
                "translation": "Bạn sống ở đâu?"
            }
        },
        {
            "id": 74,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 74: Dịch câu sau sang tiếng Đức:\n„Ông nội tôi đọc báo.“",
            "options": null,
            "correct_answer": "Mein Großvater liest die Zeitung.",
            "explanation": "Chủ ngữ Mein Großvater / Mein Opa (ngôi er), động từ lesen đổi e → ie thành „liest“ + die Zeitung -> Đáp án: Mein Großvater liest die Zeitung..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Mein Großvater liest die Zeitung.",
                    "Mein Großvater liest die Zeitung",
                    "Mein Opa liest die Zeitung.",
                    "Mein Opa liest die Zeitung",
                    "Mein Opa liest eine Zeitung.",
                    "Mein Opa liest Zeitung.",
                    "Mein Großvater liest eine Zeitung.",
                    "Mein Großvater liest Zeitung."
                ],
                "audio_text": "Mein Großvater liest die Zeitung.",
                "translation": "Ông nội tôi đọc báo."
            }
        },
        {
            "id": 75,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 75: Dịch câu sau sang tiếng Đức:\n„Cô ấy đi Berlin.“",
            "options": null,
            "correct_answer": "Sie fährt nach Berlin.",
            "explanation": "Chủ ngữ Sie (cô ấy) đi với fahren đổi a → ä thành „fährt“ + giới từ nach Berlin -> Đáp án: Sie fährt nach Berlin..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Sie fährt nach Berlin.",
                    "Sie fährt nach Berlin",
                    "Sie faehrt nach Berlin.",
                    "Sie faehrt nach Berlin"
                ],
                "audio_text": "Sie fährt nach Berlin.",
                "translation": "Cô ấy đi Berlin."
            }
        },
        {
            "id": 76,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 76: Dịch câu sau sang tiếng Đức:\n„Anh ấy gặp bạn bè của anh ấy.“",
            "options": null,
            "correct_answer": "Er trifft seine Freunde.",
            "explanation": "Chủ ngữ Er đi với động từ treffen đổi e → i thành „trifft“ + tân ngữ seine Freunde -> Đáp án: Er trifft seine Freunde..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Er trifft seine Freunde.",
                    "Er trifft seine Freunde"
                ],
                "audio_text": "Er trifft seine Freunde.",
                "translation": "Anh ấy gặp bạn bè của anh ấy."
            }
        },
        {
            "id": 77,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 77: Dịch câu sau sang tiếng Đức:\n„Chúng tôi ăn kem.“",
            "options": null,
            "correct_answer": "Wir essen Eis.",
            "explanation": "Chủ ngữ Wir đi với động từ nguyên thể „essen“ + Eis -> Đáp án: Wir essen Eis..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Wir essen Eis.",
                    "Wir essen Eis",
                    "Wir essen ein Eis.",
                    "Wir essen ein Eis"
                ],
                "audio_text": "Wir essen Eis.",
                "translation": "Chúng tôi ăn kem."
            }
        },
        {
            "id": 78,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 78: Dịch câu sau sang tiếng Đức:\n„Các bạn ngủ ở khách sạn phải không?“",
            "options": null,
            "correct_answer": "Schlaft ihr im Hotel?",
            "explanation": "Câu hỏi Yes/No đảo động từ lên đầu; ngôi ihr KHÔNG biến âm nên chia là „Schlaft ihr im Hotel?“ -> Đáp án: Schlaft ihr im Hotel?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Schlaft ihr im Hotel?",
                    "Schlaft ihr im Hotel"
                ],
                "audio_text": "Schlaft ihr im Hotel?",
                "translation": "Các bạn ngủ ở khách sạn phải không?"
            }
        },
        {
            "id": 79,
            "exercise_type": "dich_cau_vd",
            "question": "Câu 79: Dịch câu sau sang tiếng Đức:\n„Ngài muốn uống gì ạ?“",
            "options": null,
            "correct_answer": "Was möchten Sie trinken?",
            "explanation": "Câu hỏi lịch sự trong quán dùng động từ khuyết thiếu: „Was möchten Sie trinken?“ -> Đáp án: Was möchten Sie trinken?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Was möchten Sie trinken?",
                    "Was möchten Sie trinken",
                    "Was moechten Sie trinken?",
                    "Was moechten Sie trinken"
                ],
                "audio_text": "Was möchten Sie trinken?",
                "translation": "Ngài muốn uống gì ạ?"
            }
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
            "extra_data": {
                "accepted_answers": [
                    "Tên của ngài là gì?",
                    "Tên của ngài là gì",
                    "Tên ngài là gì?",
                    "Tên ngài là gì",
                    "Tên của ngài gì?",
                    "Ngài tên là gì?",
                    "Ngài tên là gì",
                    "Ngài tên gì?",
                    "ngài tên gì",
                    "Tên của ông là gì?",
                    "Tên của ông là gì",
                    "Tên ông là gì?",
                    "Ông tên là gì?",
                    "Ông tên gì?",
                    "Tên của bà là gì?",
                    "Tên bà là gì?",
                    "Bà tên là gì?",
                    "Bà tên gì?"
                ],
                "audio_text": "Wie ist Ihr Name?",
                "translation": "Tên của ngài là gì?"
            }
        },
        {
            "id": 81,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 81: Dịch câu sau sang tiếng Việt:\n„Entschuldigung, ist hier frei?“",
            "options": null,
            "correct_answer": "Xin lỗi, chỗ này còn trống không?",
            "explanation": "Câu hỏi xin phép ngồi ghế trống trong quán: „Xin lỗi, chỗ này còn trống không?“ -> Đáp án: Xin lỗi, chỗ này còn trống không?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Xin lỗi, chỗ này còn trống không?",
                    "Xin lỗi, chỗ này còn trống không",
                    "Xin lỗi chỗ này còn trống không?",
                    "Xin lỗi chỗ này còn trống không",
                    "Xin lỗi, chỗ này có trống không?",
                    "Xin lỗi chỗ này có trống không",
                    "Chỗ này có trống không?",
                    "chỗ này có trống không",
                    "Chỗ này còn trống không?",
                    "Xin lỗi, ở đây còn trống không?",
                    "Xin lỗi ở đây còn trống không?",
                    "Xin lỗi, ở đây có trống không?",
                    "Ở đây có trống không?",
                    "Ở đây còn trống không?"
                ],
                "audio_text": "Entschuldigung, ist hier frei?",
                "translation": "Xin lỗi, chỗ này còn trống không?"
            }
        },
        {
            "id": 82,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 82: Dịch câu sau sang tiếng Việt:\n„Ich trinke Tee mit Zucker.“",
            "options": null,
            "correct_answer": "Tôi uống trà với đường.",
            "explanation": "mit Zucker = với đường / có đường: „Tôi uống trà với đường.“ -> Đáp án: Tôi uống trà với đường..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Tôi uống trà với đường.",
                    "Tôi uống trà với đường",
                    "Tôi uống trà có đường.",
                    "Tôi uống trà có đường",
                    "Tôi uống trà cùng đường.",
                    "Tôi uống trà thêm đường.",
                    "Tôi uống trà pha đường.",
                    "Tôi uống trà đường.",
                    "Tôi uống trà đường",
                    "Mình uống trà với đường.",
                    "Mình uống trà có đường."
                ],
                "audio_text": "Ich trinke Tee mit Zucker.",
                "translation": "Tôi uống trà với đường."
            }
        },
        {
            "id": 83,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 83: Dịch câu sau sang tiếng Việt:\n„Der Lehrer spricht zu leise.“",
            "options": null,
            "correct_answer": "Thầy giáo nói quá nhỏ.",
            "explanation": "spricht = nói, zu leise = quá nhỏ/quá khẽ: „Thầy giáo nói quá nhỏ.“ -> Đáp án: Thầy giáo nói quá nhỏ..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Thầy giáo nói quá nhỏ.",
                    "Thầy giáo nói quá nhỏ",
                    "Thầy giáo nói nhỏ quá.",
                    "Thầy giáo nói quá bé.",
                    "Thầy giáo nói quá bé",
                    "Thầy giáo nói bé quá.",
                    "Giáo viên nói quá nhỏ.",
                    "Giáo viên nói quá nhỏ",
                    "Giáo viên nói quá bé.",
                    "Giáo viên nói bé quá.",
                    "Thầy giáo nói quá khẽ.",
                    "Thầy giáo nói quá khẽ",
                    "Giáo viên nói quá khẽ.",
                    "Thầy nói quá nhỏ.",
                    "Thầy nói quá bé."
                ],
                "audio_text": "Der Lehrer spricht zu leise.",
                "translation": "Thầy giáo nói quá nhỏ."
            }
        },
        {
            "id": 84,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 84: Dịch câu sau sang tiếng Việt:\n„Hannes gibt dem Hund das Futter.“",
            "options": null,
            "correct_answer": "Hannes cho chú chó thức ăn.",
            "explanation": "gibt dem Hund = cho chú chó, das Futter = thức ăn: „Hannes cho chú chó thức ăn.“ -> Đáp án: Hannes cho chú chó thức ăn..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Hannes cho chú chó thức ăn.",
                    "Hannes cho chú chó thức ăn",
                    "Hannes cho con chó thức ăn.",
                    "Hannes cho con chó thức ăn",
                    "Hannes cho chó thức ăn.",
                    "Hannes cho chú chó ăn.",
                    "Hannes cho con chó ăn.",
                    "Hannes cho chó ăn.",
                    "Hannes cho chú chó ăn thức ăn.",
                    "Hannes cho con chó ăn thức ăn.",
                    "Hannes cho chó ăn thức ăn.",
                    "Hannes cho chó ăn thức ăn",
                    "Hannes đưa thức ăn cho chú chó.",
                    "Hannes đưa thức ăn cho con chó.",
                    "Hannes đưa thức ăn cho chó.",
                    "Hannes đưa đồ ăn cho con chó.",
                    "Hannes cho con chó đồ ăn."
                ],
                "audio_text": "Hannes gibt dem Hund das Futter.",
                "translation": "Hannes cho chú chó thức ăn."
            }
        },
        {
            "id": 85,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 85: Dịch câu sau sang tiếng Việt:\n„Fährst du am Wochenende nach Polen?“",
            "options": null,
            "correct_answer": "Cuối tuần bạn có đi Ba Lan không?",
            "explanation": "Fährst du = bạn có đi/lái xe..., am Wochenende = vào cuối tuần: „Cuối tuần bạn có đi Ba Lan không?“ -> Đáp án: Cuối tuần bạn có đi Ba Lan không?.",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Cuối tuần bạn có đi Ba Lan không?",
                    "Cuối tuần bạn có đi Ba Lan không",
                    "Vào cuối tuần bạn có đi Ba Lan không?",
                    "Bạn có đi Ba Lan vào cuối tuần không?",
                    "Bạn có đi Ba Lan vào cuối tuần không",
                    "Bạn có đi Ba Lan cuối tuần không?",
                    "Cuối tuần cậu có đi Ba Lan không?",
                    "Cậu có đi Ba Lan vào cuối tuần không?",
                    "Cuối tuần mày có đi Ba Lan không?",
                    "Mày có đi Ba Lan vào cuối tuần không?",
                    "Cuối tuần bạn có lái xe tới Ba Lan không?",
                    "Cuối tuần bạn có lái xe đi Ba Lan không?",
                    "Bạn có lái xe đi Ba Lan vào cuối tuần không?",
                    "Bạn có lái xe tới Ba Lan vào cuối tuần không?",
                    "Cuối tuần cậu có lái xe đi Ba Lan không?",
                    "Cuối tuần mày có lái xe tới Ba Lan không?"
                ],
                "audio_text": "Fährst du am Wochenende nach Polen?",
                "translation": "Cuối tuần bạn có đi Ba Lan không?"
            }
        },
        {
            "id": 86,
            "exercise_type": "dich_cau_dv",
            "question": "Câu 86: Dịch câu sau sang tiếng Việt:\n„Karin wohnt in München.“",
            "options": null,
            "correct_answer": "Karin sống ở München.",
            "explanation": "wohnt in München = sống ở München: „Karin sống ở München.“ -> Đáp án: Karin sống ở München..",
            "exp_reward": 10,
            "extra_data": {
                "accepted_answers": [
                    "Karin sống ở München.",
                    "Karin sống ở München",
                    "Karin sống tại München.",
                    "Karin sống tại München",
                    "Karin sống ở Munich.",
                    "Karin sống tại Munich.",
                    "Karin ở München.",
                    "Karin ở tại München.",
                    "Karin đang sống ở München."
                ],
                "audio_text": "Karin wohnt in München.",
                "translation": "Karin sống ở München."
            }
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
                "tokens": [
                    "die Kinder",
                    "essen",
                    "Eis",
                    "Im Sommer",
                    "gern"
                ],
                "accepted_answers": [
                    "Im Sommer essen die Kinder gern Eis.",
                    "Die Kinder essen im Sommer gern Eis."
                ],
                "audio_text": "Im Sommer essen die Kinder gern Eis.",
                "translation": "Vào mùa hè bọn trẻ thích ăn kem."
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
                "tokens": [
                    "ihr",
                    "nach",
                    "Reist",
                    "Italien",
                    "?"
                ],
                "accepted_answers": [
                    "Reist ihr nach Italien?"
                ],
                "audio_text": "Reist ihr nach Italien?",
                "translation": "Các bạn có đi du lịch đến Ý không?"
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
                "tokens": [
                    "wohnen",
                    "Sie",
                    "in Berlin",
                    "Wo",
                    "?"
                ],
                "accepted_answers": [
                    "Wo wohnen Sie in Berlin?"
                ],
                "audio_text": "Wo wohnen Sie in Berlin?",
                "translation": "Ngài sống ở đâu tại Berlin?"
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
                "tokens": [
                    "trinkt",
                    "Was",
                    "am Morgen",
                    "der Opa",
                    "?"
                ],
                "accepted_answers": [
                    "Was trinkt der Opa am Morgen?"
                ],
                "audio_text": "Was trinkt der Opa am Morgen?",
                "translation": "Ông nội uống gì vào buổi sáng?"
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
                "tokens": [
                    "die Zeitung",
                    "Der Großvater",
                    "am Morgen",
                    "liest"
                ],
                "accepted_answers": [
                    "Der Großvater liest am Morgen die Zeitung.",
                    "Am Morgen liest der Großvater die Zeitung."
                ],
                "audio_text": "Der Großvater liest am Morgen die Zeitung.",
                "translation": "Ông nội đọc báo vào buổi sáng."
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
                "tokens": [
                    "dem Hund",
                    "Hannes",
                    "das Futter",
                    "gibt"
                ],
                "accepted_answers": [
                    "Hannes gibt dem Hund das Futter.",
                    "Dem Hund gibt Hannes das Futter."
                ],
                "audio_text": "Hannes gibt dem Hund das Futter.",
                "translation": "Hannes cho chú chó thức ăn."
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
                "tokens": [
                    "im Hotel",
                    "schlafen",
                    "Wir",
                    "heute"
                ],
                "accepted_answers": [
                    "Wir schlafen heute im Hotel.",
                    "Heute schlafen wir im Hotel."
                ],
                "audio_text": "Wir schlafen heute im Hotel.",
                "translation": "Hôm nay chúng tôi ngủ ở khách sạn."
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
                "tokens": [
                    "spricht",
                    "Der Lehrer",
                    "Deutsch",
                    "fließend"
                ],
                "accepted_answers": [
                    "Der Lehrer spricht fließend Deutsch.",
                    "Fließend Deutsch spricht der Lehrer."
                ],
                "audio_text": "Der Lehrer spricht fließend Deutsch.",
                "translation": "Thầy giáo nói tiếng Đức trôi chảy."
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
                "tokens": [
                    "treffe",
                    "ich",
                    "Heute",
                    "meine Freunde"
                ],
                "accepted_answers": [
                    "Heute treffe ich meine Freunde.",
                    "Ich treffe heute meine Freunde."
                ],
                "audio_text": "Heute treffe ich meine Freunde.",
                "translation": "Hôm nay tôi gặp bạn bè của mình."
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
                "tokens": [
                    "kommst",
                    "Woher",
                    "du",
                    "?"
                ],
                "accepted_answers": [
                    "Woher kommst du?"
                ],
                "audio_text": "Woher kommst du?",
                "translation": "Bạn đến từ đâu?"
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
                    {
                        "word": "lesen",
                        "meaning_vi": "đọc (e → ie)",
                        "category": "Bất quy tắc"
                    },
                    {
                        "word": "kaufen",
                        "meaning_vi": "mua",
                        "category": "Có quy tắc"
                    },
                    {
                        "word": "fahren",
                        "meaning_vi": "lái xe (a → ä)",
                        "category": "Bất quy tắc"
                    },
                    {
                        "word": "machen",
                        "meaning_vi": "làm",
                        "category": "Có quy tắc"
                    }
                ],
                "categories": [
                    "Bất quy tắc",
                    "Có quy tắc"
                ],
                "accepted_answers": [
                    "Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc",
                    "Bất quy tắc / Có quy tắc / Bất quy tắc / Có quy tắc"
                ],
                "audio_text": "lesen. kaufen. fahren. machen.",
                "translation": "lesen: đọc | kaufen: mua | fahren: lái xe | machen: làm"
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
                    {
                        "word": "sprechen",
                        "meaning_vi": "nói (e → i)",
                        "category": "Bất quy tắc"
                    },
                    {
                        "word": "hören",
                        "meaning_vi": "nghe",
                        "category": "Có quy tắc"
                    },
                    {
                        "word": "spielen",
                        "meaning_vi": "chơi",
                        "category": "Có quy tắc"
                    },
                    {
                        "word": "treffen",
                        "meaning_vi": "gặp gỡ (e → i)",
                        "category": "Bất quy tắc"
                    }
                ],
                "categories": [
                    "Bất quy tắc",
                    "Có quy tắc"
                ],
                "accepted_answers": [
                    "Bất quy tắc, Có quy tắc, Có quy tắc, Bất quy tắc",
                    "Bất quy tắc / Có quy tắc / Có quy tắc / Bất quy tắc"
                ],
                "audio_text": "sprechen. hören. spielen. treffen.",
                "translation": "sprechen: nói | hören: nghe | spielen: chơi | treffen: gặp gỡ"
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
                    {
                        "word": "schlafen",
                        "meaning_vi": "ngủ (a → ä)",
                        "category": "Bất quy tắc"
                    },
                    {
                        "word": "reisen",
                        "meaning_vi": "du lịch",
                        "category": "Có quy tắc"
                    },
                    {
                        "word": "geben",
                        "meaning_vi": "cho, đưa (e → i)",
                        "category": "Bất quy tắc"
                    },
                    {
                        "word": "grillen",
                        "meaning_vi": "nướng BBQ",
                        "category": "Có quy tắc"
                    }
                ],
                "categories": [
                    "Bất quy tắc",
                    "Có quy tắc"
                ],
                "accepted_answers": [
                    "Bất quy tắc, Có quy tắc, Bất quy tắc, Có quy tắc",
                    "Bất quy tắc / Có quy tắc / Bất quy tắc / Có quy tắc"
                ],
                "audio_text": "schlafen. reisen. geben. grillen.",
                "translation": "schlafen: ngủ | reisen: du lịch | geben: cho, đưa | grillen: nướng BBQ"
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
                    {
                        "word": "Aus Vietnam.",
                        "meaning_vi": "Từ Việt Nam (xuất xứ)",
                        "category": "Woher"
                    },
                    {
                        "word": "In Berlin.",
                        "meaning_vi": "Ở Berlin (địa điểm)",
                        "category": "Wo"
                    },
                    {
                        "word": "Anna.",
                        "meaning_vi": "Tên riêng",
                        "category": "Wie"
                    },
                    {
                        "word": "Kaffee.",
                        "meaning_vi": "Đồ uống",
                        "category": "Was"
                    }
                ],
                "categories": [
                    "Woher",
                    "Wo",
                    "Wie",
                    "Was"
                ],
                "accepted_answers": [
                    "Woher, Wo, Wie, Was",
                    "Woher / Wo / Wie / Was"
                ],
                "audio_text": "Aus Vietnam. In Berlin. Anna. Kaffee.",
                "translation": "Aus Vietnam: Từ Việt Nam | In Berlin: Ở Berlin | Anna: Tên riêng | Kaffee: Cà phê"
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
                    {
                        "word": "Mein Name ist John.",
                        "meaning_vi": "Tên tôi là John (hỏi tên)",
                        "category": "Wie"
                    },
                    {
                        "word": "Aus Frankreich.",
                        "meaning_vi": "Từ nước Pháp (xuất xứ)",
                        "category": "Woher"
                    },
                    {
                        "word": "In München.",
                        "meaning_vi": "Ở München (địa điểm)",
                        "category": "Wo"
                    },
                    {
                        "word": "Ein Eis.",
                        "meaning_vi": "Một cây kem (món ăn)",
                        "category": "Was"
                    }
                ],
                "categories": [
                    "Wie",
                    "Woher",
                    "Wo",
                    "Was"
                ],
                "accepted_answers": [
                    "Wie, Woher, Wo, Was",
                    "Wie / Woher / Wo / Was"
                ],
                "audio_text": "Mein Name ist John. Aus Frankreich. In München. Ein Eis.",
                "translation": "Mein Name ist John: Tên tôi là John | Aus Frankreich: Từ nước Pháp | In München: Ở München | Ein Eis: Một cây kem"
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
                    {
                        "word": "Aus der Türkei.",
                        "meaning_vi": "Từ Thổ Nhĩ Kỳ (xuất xứ)",
                        "category": "Woher"
                    },
                    {
                        "word": "Ich heiße Julia.",
                        "meaning_vi": "Tôi tên là Julia (hỏi tên)",
                        "category": "Wie"
                    },
                    {
                        "word": "In Hamburg.",
                        "meaning_vi": "Ở Hamburg (địa điểm)",
                        "category": "Wo"
                    },
                    {
                        "word": "Einen Tomatensalat.",
                        "meaning_vi": "Món salad cà chua (món ăn)",
                        "category": "Was"
                    }
                ],
                "categories": [
                    "Woher",
                    "Wie",
                    "Wo",
                    "Was"
                ],
                "accepted_answers": [
                    "Woher, Wie, Wo, Was",
                    "Woher / Wie / Wo / Was"
                ],
                "audio_text": "Aus der Türkei. Ich heiße Julia. In Hamburg. Einen Tomatensalat.",
                "translation": "Aus der Türkei: Từ Thổ Nhĩ Kỳ | Ich heiße Julia: Tôi tên là Julia | In Hamburg: Ở Hamburg | Einen Tomatensalat: Món salad cà chua"
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
            "extra_data": {
                "accepted_answers": [
                    "Ihr schlaft heute Nacht im Hotel, oder?",
                    "Ihr schlaft heute Nacht im Hotel, oder?",
                    "Ihr schlaft heute Nacht im Hotel, oder"
                ],
                "audio_text": "Ihr schlaft heute Nacht im Hotel, oder?",
                "translation": "Đêm nay các bạn ngủ ở khách sạn phải không?"
            }
        },
        {
            "id": 104,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 104: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Wann treffst du heute deine Freunde?“",
            "options": null,
            "correct_answer": "Wann triffst du heute deine Freunde?",
            "explanation": "Động từ bất quy tắc treffen biến âm e → i ở ngôi du thành „triffst“ -> Đáp án: Wann triffst du heute deine Freunde?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Wann triffst du heute deine Freunde?",
                    "Wann triffst du heute deine Freunde"
                ],
                "audio_text": "Wann triffst du heute deine Freunde?",
                "translation": "Hôm nay khi nào bạn gặp bạn bè của mình?"
            }
        },
        {
            "id": 105,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 105: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Woher wohnst du in Berlin?“",
            "options": null,
            "correct_answer": "Wo wohnst du in Berlin?",
            "explanation": "Hỏi nơi ở (với giới từ in) phải dùng từ để hỏi „Wo“, không dùng Woher -> Đáp án: Wo wohnst du in Berlin?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Wo wohnst du in Berlin?",
                    "Wo wohnst du in Berlin"
                ],
                "audio_text": "Wo wohnst du in Berlin?",
                "translation": "Bạn sống ở đâu tại Berlin?"
            }
        },
        {
            "id": 106,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 106: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Das Mädchen lest im Wohnzimmer ein Buch.“",
            "options": null,
            "correct_answer": "Das Mädchen liest im Wohnzimmer ein Buch.",
            "explanation": "Chủ ngữ Das Mädchen mang giống trung (ngôi es). Động từ bất quy tắc lesen đổi e → ie thành „liest“ -> Đáp án: Das Mädchen liest im Wohnzimmer ein Buch..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Das Mädchen liest im Wohnzimmer ein Buch.",
                    "Das Mädchen liest im Wohnzimmer ein Buch"
                ],
                "audio_text": "Das Mädchen liest im Wohnzimmer ein Buch.",
                "translation": "Cô bé đang đọc một quyển sách trong phòng khách."
            }
        },
        {
            "id": 107,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 107: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Ich fahrt am Wochenende ans Meer.“",
            "options": null,
            "correct_answer": "Ich fahre am Wochenende ans Meer.",
            "explanation": "Chủ ngữ ngôi ich đi với động từ thêm đuôi -e bình thường thành „fahre“ -> Đáp án: Ich fahre am Wochenende ans Meer..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Ich fahre am Wochenende ans Meer.",
                    "Ich fahre am Wochenende ans Meer"
                ],
                "audio_text": "Ich fahre am Wochenende ans Meer.",
                "translation": "Cuối tuần tôi đi ra biển."
            }
        },
        {
            "id": 108,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 108: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Der Lehrer sprechen zu leise.“",
            "options": null,
            "correct_answer": "Der Lehrer spricht zu leise.",
            "explanation": "Chủ ngữ Der Lehrer (ngôi er), động từ sprechen đổi e → i thành „spricht“ -> Đáp án: Der Lehrer spricht zu leise..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Der Lehrer spricht zu leise.",
                    "Der Lehrer spricht zu leise"
                ],
                "audio_text": "Der Lehrer spricht zu leise.",
                "translation": "Thầy giáo nói quá nhỏ."
            }
        },
        {
            "id": 109,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 109: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Ich komme in Deutschland.“",
            "options": null,
            "correct_answer": "Ich komme aus Deutschland.",
            "explanation": "Động từ kommen diễn tả xuất xứ từ quốc gia nào phải đi kèm giới từ „aus“ -> Đáp án: Ich komme aus Deutschland..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Ich komme aus Deutschland.",
                    "Ich komme aus Deutschland"
                ],
                "audio_text": "Ich komme aus Deutschland.",
                "translation": "Tôi đến từ nước Đức."
            }
        },
        {
            "id": 110,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 110: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Was esst er gern?“",
            "options": null,
            "correct_answer": "Was isst er gern?",
            "explanation": "Chủ ngữ ngôi er, động từ bất quy tắc essen đổi e → i thành „isst“ -> Đáp án: Was isst er gern?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Was isst er gern?",
                    "Was isst er gern"
                ],
                "audio_text": "Was isst er gern?",
                "translation": "Anh ấy thích ăn gì?"
            }
        },
        {
            "id": 111,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 111: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Entschuldigung, ist hier frei sein?“",
            "options": null,
            "correct_answer": "Entschuldigung, ist hier frei?",
            "explanation": "Câu đã có động từ tobe ist đứng trước, không để động từ nguyên thể sein ở cuối câu -> Đáp án: Entschuldigung, ist hier frei?.",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Entschuldigung, ist hier frei?",
                    "Entschuldigung, ist hier frei"
                ],
                "audio_text": "Entschuldigung, ist hier frei?",
                "translation": "Xin lỗi, chỗ này còn trống không?"
            }
        },
        {
            "id": 112,
            "exercise_type": "tim_loi_sai",
            "question": "Câu 112: Tìm lỗi sai trong câu sau và viết lại câu đúng hoàn chỉnh:\n„Hannes und Julia gibt dem Hund das Futter.“",
            "options": null,
            "correct_answer": "Hannes und Julia geben dem Hund das Futter.",
            "explanation": "Chủ ngữ số nhiều (Hannes und Julia - sie số nhiều), động từ giữ nguyên thể „geben“ -> Đáp án: Hannes und Julia geben dem Hund das Futter..",
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": [
                    "Hannes und Julia geben dem Hund das Futter.",
                    "Hannes und Julia geben dem Hund das Futter"
                ],
                "audio_text": "Hannes und Julia geben dem Hund das Futter.",
                "translation": "Hannes và Julia cho chú chó thức ăn."
            }
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
                "accepted_answers": [
                    "Woher kommst du?",
                    "Woher kommst du"
                ],
                "audio_text": "Woher kommst du?",
                "translation": "Bạn đến từ đâu? (Tôi đến từ Ba Lan.)"
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
                "accepted_answers": [
                    "Wie ist Ihr Name?",
                    "Wie ist Ihr Name",
                    "Wie heißen Sie?",
                    "Wie heißen Sie"
                ],
                "audio_text": "Wie ist Ihr Name?",
                "translation": "Tên của ngài là gì? (Tên tôi là Anna.)"
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
                "accepted_answers": [
                    "Wo wohnst du?",
                    "Wo wohnst du"
                ],
                "audio_text": "Wo wohnst du?",
                "translation": "Bạn sống ở đâu? (Tôi sống ở Hà Nội.)"
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
                "accepted_answers": [
                    "Was trinkt ihr?",
                    "Was trinkt ihr"
                ],
                "audio_text": "Was trinkt ihr?",
                "translation": "Các bạn uống gì? (Chúng tôi uống cà phê.)"
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
                "accepted_answers": [
                    "Woher kommt sie?",
                    "Woher kommt sie"
                ],
                "audio_text": "Woher kommt sie?",
                "translation": "Cô ấy đến từ đâu? (Cô ấy đến từ Thổ Nhĩ Kỳ.)"
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
                "accepted_answers": [
                    "Falsch"
                ],
                "audio_text": "Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker.",
                "translation": "Đây là David. Anh ấy đến từ Tây Ban Nha, nhưng hiện tại anh ấy sống ở Berlin. Vào cuối tuần, anh ấy thường đi xe đạp vào công viên. Anh ấy thích đọc sách và ăn pizza. Hôm nay anh ấy gặp Maria ở quán cà phê. Họ cùng nhau uống cà phê với nhiều đường."
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
                "accepted_answers": [
                    "Richtig"
                ],
                "audio_text": "Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker.",
                "translation": "Đây là David. Anh ấy đến từ Tây Ban Nha, nhưng hiện tại anh ấy sống ở Berlin. Vào cuối tuần, anh ấy thường đi xe đạp vào công viên. Anh ấy thích đọc sách và ăn pizza. Hôm nay anh ấy gặp Maria ở quán cà phê. Họ cùng nhau uống cà phê với nhiều đường."
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
                "accepted_answers": [
                    "Richtig"
                ],
                "audio_text": "Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker.",
                "translation": "Đây là David. Anh ấy đến từ Tây Ban Nha, nhưng hiện tại anh ấy sống ở Berlin. Vào cuối tuần, anh ấy thường đi xe đạp vào công viên. Anh ấy thích đọc sách và ăn pizza. Hôm nay anh ấy gặp Maria ở quán cà phê. Họ cùng nhau uống cà phê với nhiều đường."
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
                    {
                        "id": 1,
                        "speaker": "Gast",
                        "text": "Entschuldigung, ist hier frei?"
                    },
                    {
                        "id": 2,
                        "speaker": "Anna",
                        "text": "Ja klar, bitte. Setzen Sie sich."
                    },
                    {
                        "id": 3,
                        "speaker": "Gast",
                        "text": "Danke. Ich bin John aus Frankreich, und du?"
                    },
                    {
                        "id": 4,
                        "speaker": "Anna",
                        "text": "Ich heiße Anna. Ich komme aus Polen."
                    },
                    {
                        "id": 5,
                        "speaker": "Kellner",
                        "text": "Was möchtet ihr trinken: Kaffee oder Tee?"
                    },
                    {
                        "id": 6,
                        "speaker": "Gast",
                        "text": "Zwei Kaffee mit Zucker, bitte!"
                    }
                ],
                "correct_order": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "translation": "- Khách: Xin lỗi, chỗ này còn trống không?\n- Anna: Vâng tất nhiên, xin mời. Ngài hãy ngồi xuống đi.\n- Khách: Cảm ơn bạn. Tôi là John đến từ Pháp, còn bạn?\n- Anna: Tôi tên là Anna. Tôi đến từ Ba Lan.\n- Bồi bàn: Các bạn muốn uống gì: cà phê hay trà?\n- Khách: Cho hai cà phê có đường, xin cảm ơn!",
                "audio_text": "Entschuldigung, ist hier frei? Ja klar, bitte. Setzen Sie sich. Danke. Ich bin John aus Frankreich, und du? Ich heiße Anna. Ich komme aus Polen. Was möchtet ihr trinken: Kaffee oder Tee? Zwei Kaffee mit Zucker, bitte!"
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
                    {
                        "id": 1,
                        "speaker": "Maria",
                        "text": "Guten Tag! Wer sind Sie?"
                    },
                    {
                        "id": 2,
                        "speaker": "David",
                        "text": "Guten Tag, mein Name ist David. Und wie heißen Sie?"
                    },
                    {
                        "id": 3,
                        "speaker": "Maria",
                        "text": "Ich bin Maria. Woher kommen Sie, David?"
                    },
                    {
                        "id": 4,
                        "speaker": "David",
                        "text": "Ich komme aus Deutschland."
                    },
                    {
                        "id": 5,
                        "speaker": "Maria",
                        "text": "Und wo wohnen Sie jetzt?"
                    },
                    {
                        "id": 6,
                        "speaker": "David",
                        "text": "Ich wohne in Berlin."
                    }
                ],
                "correct_order": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "translation": "- Maria: Xin chào! Ngài là ai ạ?\n- David: Xin chào, tên tôi là David. Còn ngài tên là gì?\n- Maria: Tôi là Maria. Ngài đến từ đâu vậy David?\n- David: Tôi đến từ nước Đức.\n- Maria: Và hiện tại ngài sống ở đâu?\n- David: Tôi sống ở Berlin.",
                "audio_text": "Guten Tag! Wer sind Sie? Guten Tag, mein Name ist David. Und wie heißen Sie? Ich bin Maria. Woher kommen Sie, David? Ich komme aus Deutschland. Und wo wohnen Sie jetzt? Ich wohne in Berlin."
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
                    {
                        "id": 1,
                        "speaker": "Lukas",
                        "text": "Hallo! Wann triffst du heute deine Freunde?"
                    },
                    {
                        "id": 2,
                        "speaker": "Paul",
                        "text": "Hallo! Wir treffen uns um 15 Uhr im Café."
                    },
                    {
                        "id": 3,
                        "speaker": "Lukas",
                        "text": "Was macht ihr dort?"
                    },
                    {
                        "id": 4,
                        "speaker": "Paul",
                        "text": "Wir trinken Kaffee und essen Kuchen."
                    },
                    {
                        "id": 5,
                        "speaker": "Lukas",
                        "text": "Das klingt gut! Viel Spaß!"
                    },
                    {
                        "id": 6,
                        "speaker": "Paul",
                        "text": "Danke!"
                    }
                ],
                "correct_order": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "translation": "- Lukas: Xin chào! Hôm nay khi nào bạn gặp bạn bè thế?\n- Paul: Chào bạn! Chúng tôi gặp nhau lúc 15 giờ ở quán cà phê.\n- Lukas: Các bạn làm gì ở đó?\n- Paul: Chúng tôi uống cà phê và ăn bánh ngọt.\n- Lukas: Nghe hay đấy! Chúc vui vẻ nhé!\n- Paul: Cảm ơn bạn!",
                "audio_text": "Hallo! Wann triffst du heute deine Freunde? Hallo! Wir treffen uns um 15 Uhr im Café. Was macht ihr dort? Wir trinken Kaffee und essen Kuchen. Das klingt gut! Viel Spaß! Danke!"
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
                    {
                        "name": "Kaffee",
                        "price": "2,50 €"
                    },
                    {
                        "name": "Tee",
                        "price": "2,00 €"
                    },
                    {
                        "name": "Kuchen",
                        "price": "3,00 €"
                    }
                ],
                "accepted_answers": [
                    "Ich trinke einen Kaffee."
                ],
                "audio_text": "Was möchten Sie trinken? Ich trinke einen Kaffee.",
                "translation": "Ngài muốn uống gì ạ? — Tôi uống một ly cà phê."
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
                    {
                        "name": "Pizza",
                        "price": "6,50 €"
                    },
                    {
                        "name": "Tomatensalat",
                        "price": "4,00 €"
                    },
                    {
                        "name": "Eis",
                        "price": "2,00 €"
                    }
                ],
                "accepted_answers": [
                    "Wir essen ein Eis."
                ],
                "audio_text": "Was essen wir jetzt? Wir essen ein Eis.",
                "translation": "Bây giờ chúng ta ăn gì đây? — Chúng ta ăn một cây kem."
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
