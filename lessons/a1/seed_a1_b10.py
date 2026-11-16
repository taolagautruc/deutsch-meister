# -*- coding: utf-8 -*-
"""
Seed file Bài 10 (A1): "Essen und Trinken - Thực phẩm, So sánh hơn / So sánh nhất, Từ hỏi: Welch-"
Vị trí A1: lesson_order = 11 (sau Bài 9)
Tích hợp đầy đủ 9 Học phần Lý thuyết + 6 Container Sơ đồ SVG + 50 Từ vựng + 100 Bài tập độc nhất (16 Dạng bài)
Chuẩn CEFR A1 và tuân thủ tuyệt đối Giao thức QA Zero-Bug
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

def seed_lesson_10():
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
    lesson_id = 24
    lesson_title = 'Bài 10: Thực phẩm - So sánh hơn / So sánh nhất - Fragewort: Welch-'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed font-sans">
        <!-- BANNER TỔNG QUAN BÀI 10 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-emerald-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-400/30 text-emerald-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Essen & Trinken • Welch- • Steigerung (Bài 10)
                    </span>
                    <span class="text-xs font-semibold text-slate-400 bg-slate-800/80 px-2.5 py-1 rounded-lg border border-slate-700">
                        100 Bài tập Zero-Bug QA • 6 Sơ đồ SVG Tương tác
                    </span>
                </div>
                <h1 class="text-2xl sm:text-3xl font-black tracking-tight text-white">
                    Essen und Trinken: So sánh hơn / nhất, Từ hỏi Welch- & Mua sắm
                </h1>
                <p class="text-slate-300 text-xs sm:text-sm max-w-3xl leading-relaxed">
                    Khám phá toàn bộ từ vựng ẩm thực Đức - Việt (3 giống <code>der / die / das</code>), làm chủ từ hỏi <b>Welch-</b> biến đổi theo Giống và Cách, nắm vững 3 bậc so sánh (<code>Positiv → Komparativ → Superlativ</code>), cấu trúc <code>mehr … als</code>, và tự tin giao tiếp mua sắm: gọi món, hỏi giá, đơn vị đo lường và đọc giá tiền Euro bằng tiếng Đức.
                </p>
                <div class="pt-2 flex flex-wrap gap-2 text-xs">
                    <span class="px-2.5 py-1 rounded-md bg-emerald-500/10 border border-emerald-400/20 text-emerald-200">🧀 50 Từ vựng thực phẩm</span>
                    <span class="px-2.5 py-1 rounded-md bg-blue-500/10 border border-blue-400/20 text-blue-200">❓ Welch- (Welcher / Welchen / Welche / Welches)</span>
                    <span class="px-2.5 py-1 rounded-md bg-amber-500/10 border border-amber-400/20 text-amber-200">📈 Steigerung (viel - mehr - am meisten; gern - lieber - am liebsten)</span>
                    <span class="px-2.5 py-1 rounded-md bg-purple-500/10 border border-purple-400/20 text-purple-200">🛒 Đi mua sắm & Đọc giá tiền Euro</span>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 1: TỪ VỰNG THỰC PHẨM (LEBENSMITTEL) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 font-black text-sm flex items-center justify-center shrink-0">1</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Từ Vựng Thực Phẩm (Lebensmittel) Theo 3 Giống</h2>
                    <p class="text-xs text-slate-500">Quy tắc giống, số nhiều chuẩn hóa và các từ vựng cốt lõi</p>
                </div>
            </div>

            <!-- Bảng phân loại 3 giống -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                <!-- Giống đực -->
                <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-2">
                    <div class="flex items-center justify-between font-bold text-blue-900 border-b border-blue-200/60 pb-1.5">
                        <span class="text-sm">🔵 Giống Đực (der)</span>
                        <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 text-[11px]">Maskulinum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-800">
                        <li>• <b class="text-blue-950">der Käse</b> <i>(die Käse)</i>: phô mai <span class="text-[10px] text-amber-700 font-bold">(ngoại lệ đuôi -e)</span></li>
                        <li>• <b class="text-blue-950">der Kuchen</b> <i>(die Kuchen)</i>: bánh ngọt</li>
                        <li>• <b class="text-blue-950">der Apfel</b> <i>(die Äpfel)</i>: quả táo</li>
                        <li>• <b class="text-blue-950">der Fisch</b> <i>(die Fische)</i>: cá</li>
                        <li>• <b class="text-blue-950">der Salat</b> <i>(die Salate)</i>: xà lách; món salad</li>
                        <li>• <b class="text-blue-950">der Schinken</b> <i>(die Schinken)</i>: thịt xông khói</li>
                        <li>• <b class="text-blue-950">der Pfeffer</b> <i>(nur Sg.)</i>: tiêu</li>
                        <li>• <b class="text-blue-950">der Reis</b> <i>(nur Sg.)</i>: gạo, cơm <span class="text-[10px] text-emerald-700 font-bold">(chuẩn từ điển: der)</span></li>
                        <li>• <b class="text-blue-950">der Saft</b> <i>(die Säfte)</i>: nước ép</li>
                        <li>• <b class="text-blue-950">der Kaffee</b> <i>(die Kaffees)</i>: cà phê</li>
                        <li>• <b class="text-blue-950">der Tee</b> <i>(die Tees)</i>: trà</li>
                        <li>• <b class="text-blue-950">der Joghurt</b> <i>(die Joghurts)</i>: sữa chua</li>
                        <li>• <b class="text-blue-950">der Becher</b> <i>(die Becher)</i>: hộp/cốc (sữa chua)</li>
                    </ul>
                </div>

                <!-- Giống cái -->
                <div class="p-4 rounded-2xl bg-rose-50/60 border border-rose-200 space-y-2">
                    <div class="flex items-center justify-between font-bold text-rose-900 border-b border-rose-200/60 pb-1.5">
                        <span class="text-sm">🔴 Giống Cái (die)</span>
                        <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 text-[11px]">Femininum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-800">
                        <li>• <b class="text-rose-950">die Butter</b> <i>(nur Sg.)</i>: bơ</li>
                        <li>• <b class="text-rose-950">die Milch</b> <i>(nur Sg.)</i>: sữa</li>
                        <li>• <b class="text-rose-950">die Kartoffel</b> <i>(die Kartoffeln)</i>: khoai tây</li>
                        <li>• <b class="text-rose-950">die Tomate</b> <i>(die Tomaten)</i>: cà chua</li>
                        <li>• <b class="text-rose-950">die Möhre</b> <i>(die Möhren)</i>: cà rốt (= die Karotte)</li>
                        <li>• <b class="text-rose-950">die Erdbeere</b> <i>(die Erdbeeren)</i>: dâu tây</li>
                        <li>• <b class="text-rose-950">die Banane</b> <i>(die Bananen)</i>: quả chuối</li>
                        <li>• <b class="text-rose-950">die Orange</b> <i>(die Orangen)</i>: quả cam</li>
                        <li>• <b class="text-rose-950">die Zitrone</b> <i>(die Zitronen)</i>: quả chanh</li>
                        <li>• <b class="text-rose-950">die Wurst</b> <i>(die Würste)</i>: xúc xích</li>
                        <li>• <b class="text-rose-950">die Salami</b> <i>(die Salamis)</i>: xúc xích lên men</li>
                        <li>• <b class="text-rose-950">die Birne</b> <i>(die Birnen)</i>: quả lê</li>
                        <li>• <b class="text-rose-950">die Nudel</b> <i>(die Nudeln)</i>: sợi mì</li>
                        <li>• <b class="text-rose-950">die Paprika</b> <i>(die Paprikas)</i>: ớt chuông</li>
                        <li>• <b class="text-rose-950">die Ananas</b> <i>(die Ananas)</i>: quả dứa</li>
                        <li>• <b class="text-rose-950">die Zwiebel</b> <i>(die Zwiebeln)</i>: hành tây</li>
                        <li>• <b class="text-rose-950">die Suppe</b> <i>(die Suppen)</i>: món súp / canh</li>
                        <li>• <b class="text-rose-950">die Marmelade</b> <i>(die Marmeladen)</i>: mứt</li>
                        <li>• <b class="text-rose-950">die Schokolade</b> <i>(die Schokoladen)</i>: sô-cô-la</li>
                    </ul>
                </div>

                <!-- Giống trung -->
                <div class="p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200 space-y-2">
                    <div class="flex items-center justify-between font-bold text-emerald-900 border-b border-emerald-200/60 pb-1.5">
                        <span class="text-sm">🟢 Giống Trung (das)</span>
                        <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-[11px]">Neutrum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-800">
                        <li>• <b class="text-emerald-950">das Brot</b> <i>(die Brote)</i>: bánh mì</li>
                        <li>• <b class="text-emerald-950">das Brötchen</b> <i>(die Brötchen)</i>: bánh mì nhỏ <span class="text-[10px] text-emerald-700 font-bold">(đuôi -chen luôn das)</span></li>
                        <li>• <b class="text-emerald-950">das Hähnchen</b> <i>(die Hähnchen)</i>: thịt gà <span class="text-[10px] text-emerald-700 font-bold">(đuôi -chen luôn das)</span></li>
                        <li>• <b class="text-emerald-950">das Ei</b> <i>(die Eier)</i>: quả trứng</li>
                        <li>• <b class="text-emerald-950">das Fleisch</b> <i>(nur Sg.)</i>: thịt</li>
                        <li>• <b class="text-emerald-950">das Obst</b> <i>(nur Sg.)</i>: hoa quả, trái cây</li>
                        <li>• <b class="text-emerald-950">das Gemüse</b> <i>(nur Sg.)</i>: rau củ</li>
                        <li>• <b class="text-emerald-950">das Eis</b> <i>(nur Sg.)</i>: kem; đá</li>
                        <li>• <b class="text-emerald-950">das Salz</b> <i>(nur Sg.)</i>: muối</li>
                        <li>• <b class="text-emerald-950">das Müsli</b> <i>(die Müslis)</i>: ngũ cốc ăn sáng</li>
                        <li>• <b class="text-emerald-950">das Schnitzel</b> <i>(die Schnitzel)</i>: thịt tẩm bột chiên</li>
                        <li>• <b class="text-emerald-950">das Wasser</b> <i>(nur Sg.)</i>: nước</li>
                        <li>• <b class="text-emerald-950">das Bier</b> <i>(die Biere)</i>: bia</li>
                    </ul>
                </div>
            </div>

            <!-- Mẹo nhớ giống và từ không đếm được -->
            <div class="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs space-y-2 text-slate-800">
                <div class="font-extrabold text-amber-900 flex items-center gap-1.5">
                    <span>💡 Mẹo nhớ giống & Quy tắc số lượng quan trọng:</span>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 leading-relaxed">
                    <div>• <b>Hoa quả / rau củ đuôi -e thường là die</b>: <i>die Banane, die Orange, die Birne, die Erdbeere, die Tomate, die Möhre</i>. Ngoại lệ: <b>der Käse</b> (giống đực) và <b>das Gemüse</b> (giống trung).</div>
                    <div>• <b>Đuôi -chen luôn là das</b>: <i>das Hähnchen, das Brötchen</i>.</div>
                    <div>• <b>Nhóm danh từ không đếm được (nur Singular)</b>: <i>das Obst, das Gemüse, das Fleisch, der Reis, die Butter, die Milch, das Salz</i>. Không dùng số đếm trực tiếp, không dùng ein/eine (nói <i>Ich esse Reis</i>, không nói <i>Ich esse einen Reis</i>).</div>
                    <div>• <b>Trạng từ chỉ tần suất</b>: <i>immer</i> (luôn luôn) · <i>oft</i> (thường) · <i>manchmal</i> (thỉnh thoảng) · <i>selten</i> (hiếm khi) · <i>nie</i> (không bao giờ).</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: HƯƠNG VỊ, BỮA ĂN & SỞ THÍCH -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-amber-100 text-amber-700 font-black text-sm flex items-center justify-center shrink-0">2</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Hương Vị, Bữa Ăn & Cách Bày Tỏ Sở Thích</h2>
                    <p class="text-xs text-slate-500">Tính từ miêu tả khẩu vị, cấu trúc 'zum' và nói về món ăn yêu thích</p>
                </div>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 text-xs">
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="font-bold text-slate-900">lecker</span>: ngon
                    <p class="text-slate-500 italic mt-0.5">„Der Kuchen ist lecker.“</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="font-bold text-slate-900">süß</span>: ngọt
                    <p class="text-slate-500 italic mt-0.5 whitespace-nowrap">„Die Erdbeeren sind süß.“</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="font-bold text-slate-900">salzig</span>: mặn
                    <p class="text-slate-500 italic mt-0.5">„Die Suppe ist zu salzig.“</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="font-bold text-slate-900">sauer</span>: chua
                    <p class="text-slate-500 italic mt-0.5">„Die Zitrone ist sauer.“</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="font-bold text-slate-900">scharf</span>: cay
                    <p class="text-slate-500 italic mt-0.5">„Die Wurst ist scharf.“</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <span class="font-bold text-slate-900">frisch</span>: tươi
                    <p class="text-slate-500 italic mt-0.5">„Der Fisch ist ganz frisch.“</p>
                </div>
            </div>

            <!-- Ba bữa ăn & giới từ zum -->
            <div class="p-4 rounded-2xl bg-indigo-50/60 border border-indigo-200 text-xs space-y-2">
                <div class="font-extrabold text-indigo-900">🍽️ Ba bữa ăn chính & Cấu trúc „zum …“:</div>
                <div class="space-y-1 text-slate-700">
                    <div>• <b>das Frühstück</b> (bữa sáng) → <b>zum Frühstück</b>: <i>„Zum Frühstück esse ich Müsli mit Milch.“</i></div>
                    <div>• <b>das Mittagessen</b> (bữa trưa) → <b>zum Mittagessen</b>: <i>„Zum Mittagessen gibt es Reis mit Fisch.“</i></div>
                    <div>• <b>das Abendessen</b> (bữa tối) → <b>zum Abendessen</b>: <i>„Zum Abendessen koche ich Nudeln.“</i></div>
                    <div>• Hỏi: <i>„Was isst du zum Frühstück?“</i> (Bạn ăn gì vào bữa sáng?) · <i>„Mein Lieblingsessen ist Schnitzel mit Kartoffeln.“</i> (Món ăn yêu thích của tôi là thịt tẩm bột chiên dùng kèm khoai tây.)</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: TỪ HỎI WELCH- (TRỌNG TÂM 1) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 font-black text-sm flex items-center justify-center shrink-0">3</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">⭐ Từ Hỏi „Welch-“ (... Nào?) Trong Nominativ & Akkusativ</h2>
                    <p class="text-xs text-slate-500">Quy tắc đuôi mạo từ xác định, phân biệt Chủ ngữ / Tân ngữ và cụm 2 danh từ</p>
                </div>
            </div>

            <p class="text-xs text-slate-600">
                Từ hỏi <b>Welch-</b> dùng để chọn một trong nhiều đối tượng cùng loại. Đuôi của <b>welch-</b> giống hệt mạo từ xác định: <code>der → welcher</code>, <code>den → welchen</code>, <code>die → welche</code>, <code>das → welches</code>. <b>Chỉ giống ĐỰC mới đổi giữa Nominativ và Akkusativ!</b>
            </p>

            <!-- BẢNG ĐUÔI TƯƠNG TÁC SƠ ĐỒ V1 CONTAINER -->
            <div id="svg-v1-container" class="my-4"></div>

            <!-- LƯU ĐỒ CHỌN WELCH- SƠ ĐỒ V2 CONTAINER -->
            <div id="svg-v2-container" class="my-4"></div>

            <!-- Cụm có hai danh từ -->
            <div class="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs space-y-2 text-slate-800">
                <div class="font-extrabold text-amber-900">⚠️ Quy tắc cụm có 2 danh từ (Ví dụ: „Welche Dose Cola?“):</div>
                <p>Trong cụm <i>„một lon cô-ca“</i> có 2 danh từ: <b>die Dose</b> (lon) và <b>die Cola</b>. <b>Đuôi của welch- luôn lấy theo danh từ đứng NGAY SAU NÓ</b> (ở đây là <i>Dose</i> → <code>Welche Dose Cola?</code>). Không lấy theo danh từ phía sau.</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 font-mono text-[11px] pt-1">
                    <div class="p-2 bg-white rounded-lg border border-amber-200">• Welche Dose Cola ist billig? (die Dose)</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200">• Welche Flasche Wasser nimmst du? (die Flasche)</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200">• Welches Stück Kuchen möchten Sie? (das Stück)</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200">• Welchen Becher Joghurt nimmst du? (der Becher, Akk)</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: VIEL, VIELE, MEHR, MEHR ... ALS -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 font-black text-sm flex items-center justify-center shrink-0">4</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Số Lượng & So Sánh Số Lượng: viel, viele, mehr, mehr … als</h2>
                    <p class="text-xs text-slate-500">Phân biệt danh từ đếm được vs không đếm được và cấu trúc so sánh hơn</p>
                </div>
            </div>

            <div class="overflow-x-auto text-xs">
                <table class="w-full border-collapse border border-slate-200">
                    <thead class="bg-slate-50 text-slate-800 font-bold">
                        <tr>
                            <th class="p-2.5 border border-slate-200 text-left">Từ</th>
                            <th class="p-2.5 border border-slate-200 text-left">Nghĩa</th>
                            <th class="p-2.5 border border-slate-200 text-left">Đi với danh từ nào?</th>
                            <th class="p-2.5 border border-slate-200 text-left">Ví dụ & Dịch</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr>
                            <td class="p-2.5 font-bold text-purple-900 border border-slate-200">viel</td>
                            <td class="p-2.5 border border-slate-200">nhiều</td>
                            <td class="p-2.5 border border-slate-200">Không đếm được, số ít (Käse, Obst, Reis, Fleisch, Wasser)</td>
                            <td class="p-2.5 border border-slate-200"><i>„Wir essen viel Obst.“</i> (Chúng tôi ăn nhiều hoa quả.)</td>
                        </tr>
                        <tr>
                            <td class="p-2.5 font-bold text-purple-900 border border-slate-200">viele</td>
                            <td class="p-2.5 border border-slate-200">nhiều</td>
                            <td class="p-2.5 border border-slate-200">Đếm được, số nhiều (Äpfel, Eier, Nudeln, Kartoffeln)</td>
                            <td class="p-2.5 border border-slate-200"><i>„Ich kaufe viele Äpfel.“</i> (Tôi mua nhiều quả táo.)</td>
                        </tr>
                        <tr>
                            <td class="p-2.5 font-bold text-purple-900 border border-slate-200">mehr … als</td>
                            <td class="p-2.5 border border-slate-200">nhiều hơn …</td>
                            <td class="p-2.5 border border-slate-200">Cả đếm được và không đếm được (không đổi dạng)</td>
                            <td class="p-2.5 border border-slate-200"><i>„Er isst mehr Reis als Nudeln.“</i> (Anh ấy ăn cơm nhiều hơn mì.)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-xs flex items-center gap-2 flex-wrap">
                <span class="px-2.5 py-1 rounded-lg bg-indigo-100 text-indigo-800 font-extrabold text-xs uppercase tracking-wide">Công thức:</span>
                <code class="px-2.5 py-1 rounded-lg bg-slate-200/80 text-slate-900 font-bold text-xs">Chủ ngữ + Động từ + mehr + [Danh từ A] + als + [Danh từ B]</code>
            </div>
        </div>

        <!-- HỌC PHẦN 5: SO SÁNH HƠN & SO SÁNH NHẤT (TRỌNG TÂM 2) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-rose-100 text-rose-700 font-black text-sm flex items-center justify-center shrink-0">5</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">⭐ So Sánh Hơn (Komparativ) & So Sánh Nhất (Superlativ)</h2>
                    <p class="text-xs text-slate-500">Ba bậc so sánh, 3 cặp bất quy tắc bắt buộc thuộc và cấu trúc đảo ngữ vị trí 1-2-3</p>
                </div>
            </div>

            <!-- BẬC THANG SO SÁNH SƠ ĐỒ V3 CONTAINER -->
            <div id="svg-v3-container" class="my-4"></div>

            <!-- KHUNG CÂU ĐẢO NGỮ VỊ TRÍ 1-2-3 SƠ ĐỒ V4 CONTAINER -->
            <div id="svg-v4-container" class="my-4"></div>

            <!-- Bảng 3 cặp bất quy tắc -->
            <div class="overflow-x-auto text-xs">
                <table class="w-full border-collapse border border-slate-200 text-center">
                    <thead class="bg-rose-50 text-rose-950 font-bold">
                        <tr>
                            <th class="p-2.5 border border-slate-200">Positiv (Nguyên mức)</th>
                            <th class="p-2.5 border border-slate-200">Komparativ (So sánh hơn)</th>
                            <th class="p-2.5 border border-slate-200">Superlativ (So sánh nhất)</th>
                            <th class="p-2.5 border border-slate-200 text-left">Ý nghĩa & Dấu hiệu</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr>
                            <td class="p-2.5 font-bold border border-slate-200">viel</td>
                            <td class="p-2.5 font-bold text-rose-700 border border-slate-200">mehr</td>
                            <td class="p-2.5 font-bold text-rose-900 border border-slate-200">am meisten</td>
                            <td class="p-2.5 text-left border border-slate-200">Nói về <b>Số lượng</b> (ăn/mua bao nhiêu)</td>
                        </tr>
                        <tr>
                            <td class="p-2.5 font-bold border border-slate-200">gern</td>
                            <td class="p-2.5 font-bold text-rose-700 border border-slate-200">lieber</td>
                            <td class="p-2.5 font-bold text-rose-900 border border-slate-200">am liebsten</td>
                            <td class="p-2.5 text-left border border-slate-200">Nói về <b>Sở thích</b> (thích làm gì / thích món gì hơn)</td>
                        </tr>
                        <tr>
                            <td class="p-2.5 font-bold border border-slate-200">gut</td>
                            <td class="p-2.5 font-bold text-rose-700 border border-slate-200">besser</td>
                            <td class="p-2.5 font-bold text-rose-900 border border-slate-200">am besten</td>
                            <td class="p-2.5 text-left border border-slate-200">Nói về <b>Chất lượng / Kỹ năng</b> (ngon, tốt, nấu ăn giỏi)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Quy tắc Umlaut & biến âm tính từ -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-xs space-y-1.5 text-slate-700">
                <div class="font-bold text-slate-900">🔍 Quy tắc chính tả quan trọng của tính từ:</div>
                <div>• <b>Đuôi -er/-el bỏ e ở Komparativ</b>: <code>teuer → teurer → am teuersten</code>; <code>sauer → saurer → am sauersten</code>.</div>
                <div>• <b>Đuôi -t, -d, -s, -ß, -z, -sch thêm -esten</b>: <code>frisch → frischer → am frischesten</code>; <code>süß → süßer → am süßesten</code>; <code>heiß → heißer → am heißesten</code>.</div>
                <div>• <b>Biến âm Umlaut ở tính từ ngắn</b>: <code>alt → älter → am ältesten</code>; <code>kalt → kälter → am kältesten</code>; <code>warm → wärmer → am wärmsten</code>; <code>gesund → gesünder → am gesündesten</code>.</div>
            </div>
        </div>

        <!-- HỌC PHẦN 6: ĐI MUA SẮM (EINKAUFEN) & GIÁ TIỀN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 font-black text-sm flex items-center justify-center shrink-0">6</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Đi Mua Sắm (Einkaufen) — Hỏi Mua, Đơn Vị Đo & Đọc Giá Tiền</h2>
                    <p class="text-xs text-slate-500">Mẫu câu tại quầy hàng, đơn vị đóng gói và máy đọc tiền Euro chuẩn Đức</p>
                </div>
            </div>

            <!-- QUẦY CHỢ HỘI THOẠI TƯƠNG TÁC SƠ ĐỒ V5 CONTAINER -->
            <div id="svg-v5-container" class="my-4"></div>

            <!-- MÁY ĐỌC GIÁ TIỀN EURO SƠ ĐỒ V6 CONTAINER -->
            <div id="svg-v6-container" class="my-4"></div>

            <!-- Đơn vị đo lường sau số đếm -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div class="p-3.5 rounded-2xl bg-emerald-50/70 border border-emerald-200 space-y-1">
                    <span class="font-bold text-emerald-900">⚖️ Đơn vị đo (giữ nguyên số ít sau số đếm):</span>
                    <ul class="space-y-0.5 text-slate-700">
                        <li>• <b>das Kilo</b>: <i>zwei Kilo Äpfel</i> (hai ký táo)</li>
                        <li>• <b>das Pfund</b> (= 500g): <i>zwei Pfund Erdbeeren</i> (hai Pfund = một ký dâu tây)</li>
                        <li>• <b>das Gramm</b>: <i>zweihundert Gramm Käse</i> (200g phô mai)</li>
                        <li>• <b>der Liter</b>: <i>zwei Liter Milch</i> (hai lít sữa)</li>
                        <li>• <b>das Stück</b>: <i>drei Stück Kuchen</i> (ba miếng bánh)</li>
                    </ul>
                </div>
                <div class="p-3.5 rounded-2xl bg-blue-50/70 border border-blue-200 space-y-1">
                    <span class="font-bold text-blue-900">📦 Đơn vị đóng gói (thêm đuôi số nhiều -n/-en):</span>
                    <ul class="space-y-0.5 text-slate-700">
                        <li>• <b>die Flasche</b> → <i>zwei Flaschen Wasser</i> (hai chai nước)</li>
                        <li>• <b>die Dose</b> → <i>drei Dosen Cola</i> (ba lon cô-ca)</li>
                        <li>• <b>die Packung</b> → <i>zwei Packungen Müsli</i> (hai gói ngũ cốc)</li>
                        <li>• <b>die Tüte</b> → <i>zwei Tüten Obst</i> (hai túi hoa quả)</li>
                        <li>• <b>die Scheibe</b> → <i>vier Scheiben Schinken</i> (bốn lát giăm bông)</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 7: ĐỘNG TỪ ĂN UỐNG & ÔN PERFEKT -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-orange-100 text-orange-700 font-black text-sm flex items-center justify-center shrink-0">7</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Động Từ Ăn Uống, Mua Sắm & Ôn Tập Perfekt (Bài 9)</h2>
                    <p class="text-xs text-slate-500">Quy tắc chia Präsens, nhóm biến âm e → i / a → ä, động từ khuyết möchten / mögen / dürfen</p>
                </div>
            </div>

            <div class="overflow-x-auto text-xs">
                <table class="w-full border-collapse border border-slate-200">
                    <thead class="bg-orange-50 text-orange-950 font-bold">
                        <tr>
                            <th class="p-2 border border-slate-200 text-left">Động từ</th>
                            <th class="p-2 border border-slate-200 text-left">Nghĩa</th>
                            <th class="p-2 border border-slate-200 text-left">Präsens (du / er·sie·es)</th>
                            <th class="p-2 border border-slate-200 text-left">Perfekt (haben + P.II)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">essen</td>
                            <td class="p-2 border border-slate-200">ăn</td>
                            <td class="p-2 font-bold text-rose-700 border border-slate-200">du isst / er isst (e → i)</td>
                            <td class="p-2 border border-slate-200">hat gegessen</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">trinken</td>
                            <td class="p-2 border border-slate-200">uống</td>
                            <td class="p-2 border border-slate-200">du trinkst / er trinkt</td>
                            <td class="p-2 border border-slate-200">hat getrunken</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">nehmen</td>
                            <td class="p-2 border border-slate-200">lấy, chọn mua</td>
                            <td class="p-2 font-bold text-rose-700 border border-slate-200">du nimmst / er nimmt (e → i)</td>
                            <td class="p-2 border border-slate-200">hat genommen</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">backen</td>
                            <td class="p-2 border border-slate-200">nướng bánh</td>
                            <td class="p-2 font-bold text-rose-700 border border-slate-200">du bäckst (backst) / er bäckt (backt)</td>
                            <td class="p-2 border border-slate-200">hat gebacken</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">kaufen / einkaufen</td>
                            <td class="p-2 border border-slate-200">mua / đi mua sắm</td>
                            <td class="p-2 border border-slate-200">du kaufst (ein) / er kauft (ein)</td>
                            <td class="p-2 border border-slate-200">hat gekauft / hat eingekauft</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">kochen</td>
                            <td class="p-2 border border-slate-200">nấu ăn</td>
                            <td class="p-2 border border-slate-200">du kochst / er kocht</td>
                            <td class="p-2 border border-slate-200">hat gekocht</td>
                        </tr>
                        <tr>
                            <td class="p-2 font-bold text-slate-900 border border-slate-200">bestellen</td>
                            <td class="p-2 border border-slate-200">gọi món</td>
                            <td class="p-2 border border-slate-200">du bestellst / er bestellt</td>
                            <td class="p-2 border border-slate-200">hat bestellt (tiền tố 'be-' không thêm ge-)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Khung so sánh 3 cách nói sở thích & gọi món -->
            <div class="mt-4 p-4 rounded-2xl bg-orange-50/80 border border-orange-200 text-xs space-y-2 text-slate-800">
                <div class="font-extrabold text-orange-950 flex items-center gap-1.5">
                    <span>🍽️ Phân biệt 3 cách nói sở thích & gọi món trong ẩm thực:</span>
                </div>
                <div class="space-y-2 leading-relaxed">
                    <div class="p-2.5 rounded-xl bg-white border border-orange-100">
                        <b class="text-orange-950">1. mögen (thích + Danh từ):</b> <code class="px-1.5 py-0.5 rounded bg-orange-100 text-orange-900 font-bold">ich mag, du magst, er/sie/es mag, wir mögen, ihr mögt, sie/Sie mögen</code>.<br>
                        <span class="text-slate-600 mt-1 block">👉 <b>Ví dụ:</b> <i>„Ich mag Käse, aber ich mag keinen Fisch.“</i> (Tôi thích phô mai nhưng không thích cá.)</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-orange-100">
                        <b class="text-orange-950">2. Động từ thường + gern (thích làm gì):</b> dùng khi diễn tả hành động ăn/uống/nấu.<br>
                        <span class="text-slate-600 mt-1 block">👉 <b>Ví dụ:</b> <i>„Ich esse gern Pizza und trinke gern Apfelsaft.“</i> (Tôi thích ăn pizza và thích uống nước táo.)</span>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-orange-100">
                        <b class="text-orange-950">3. möchten (muốn / xin gọi món lịch sự):</b> <code class="px-1.5 py-0.5 rounded bg-orange-100 text-orange-900 font-bold">ich möchte, du möchtest, er/sie/es möchte, wir möchten, ihr möchtet, sie/Sie möchten</code>.<br>
                        <span class="text-slate-600 mt-1 block">👉 <b>Ví dụ:</b> <i>„Ich möchte bitte ein Kilo Tomaten.“</i> / <i>„Was möchten Sie trinken?“</i></span>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 8: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">8</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Đọc Hiểu & Phân Tích Văn Bản Ẩm Thực (Textanalyse)</h2>
                    <p class="text-xs text-slate-500">Luyện đọc hiểu có âm thanh bản xứ de-DE, phân tích ngữ pháp câu và tính toán chi tiêu</p>
                </div>
            </div>

            <!-- Bài đọc 1 -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 text-xs">
                <div class="flex items-center justify-between flex-wrap gap-2 pb-2 border-b border-slate-200">
                    <span class="font-bold text-slate-900 text-sm">📖 Đoạn 1: Die Essgewohnheiten der Familie Berger (Wien)</span>
                    <div class="flex gap-1.5">
                        <button onclick="speakGerman('Familie Berger wohnt in Wien. Zum Frühstück essen die Bergers Brot mit Butter und Marmelade. Der Vater trinkt Kaffee, die Mutter trinkt lieber Tee, und die Kinder trinken am liebsten Milch. Mittags kocht die Mutter oft Kartoffeln mit Fisch oder Gemüse. Die Kinder essen mehr Nudeln als Reis, aber der Vater isst mehr Reis als Nudeln. Am Wochenende backt der Vater einen Kuchen. Am liebsten essen alle Erdbeerkuchen.', 1.0)" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 font-bold transition">
                            🔊 Nghe đọc (1.0x)
                        </button>
                    </div>
                </div>
                <div class="text-slate-800 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200">
                    „Familie Berger wohnt in Wien. Zum Frühstück essen die Bergers Brot mit Butter und Marmelade. Der Vater trinkt Kaffee, die Mutter trinkt <b>lieber</b> Tee, und die Kinder trinken <b>am liebsten</b> Milch. Mittags kocht die Mutter oft Kartoffeln mit Fisch oder Gemüse. Die Kinder essen <b>mehr</b> Nudeln <b>als</b> Reis, aber der Vater isst <b>mehr</b> Reis <b>als</b> Nudeln. Am Wochenende backt der Vater einen Kuchen. <b>Am liebsten</b> essen alle Erdbeerkuchen.“
                </div>
                <div class="text-slate-600 italic">
                    👉 <b>Bản dịch:</b> „Gia đình Berger sống ở Wien. Vào bữa sáng nhà Berger ăn bánh mì với bơ và mứt. Người bố uống cà phê, người mẹ thích uống trà hơn, còn bọn trẻ thích uống sữa nhất. Buổi trưa mẹ thường nấu khoai tây với cá hoặc rau củ. Bọn trẻ ăn mì nhiều hơn cơm, nhưng người bố ăn cơm nhiều hơn mì. Cuối tuần người bố nướng một chiếc bánh. Mọi người thích nhất là ăn bánh dâu tây.“
                </div>
            </div>

            <!-- Bài đọc 2: Ở chợ -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 text-xs">
                <div class="flex items-center justify-between flex-wrap gap-2 pb-2 border-b border-slate-200">
                    <span class="font-bold text-slate-900 text-sm">🛒 Đoạn 2: Hội thoại mua hàng ở chợ (Frau Nguyen)</span>
                    <button onclick="speakGerman('Guten Tag! Was möchten Sie bitte? Guten Tag! Ich möchte gern zwei Kilo Tomaten und ein Kilo Möhren. Was kostet das Kilo Möhren? Ein Kilo Möhren kostet einen Euro zwanzig. Sonst noch etwas? Ja, welche Ananas ist süß? Diese Ananas hier ist sehr frisch und süß. Das Stück kostet zwei Euro dreißig. Gut, dann nehme ich die Ananas. Das ist alles. Wie viel macht das zusammen? Zwei Kilo Tomaten zu je zwei Euro fünfzig, ein Kilo Möhren für ein Euro zwanzig und eine Ananas für zwei Euro dreißig. Das macht zusammen acht Euro fünfzig. Hier sind zehn Euro. Vielen Dank! Sie bekommen einen Euro fünfzig zurück.', 1.0)" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 font-bold transition cursor-pointer">
                        🔊 Nghe hội thoại (1.0x)
                    </button>
                </div>
                <div class="text-slate-800 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-1">
                    <p><b>— Verkäufer:</b> Guten Tag! Was möchten Sie bitte?</p>
                    <p><b>— Frau Nguyen:</b> Guten Tag! Ich möchte gern zwei Kilo Tomaten und ein Kilo Möhren. Was kostet das Kilo Möhren?</p>
                    <p><b>— Verkäufer:</b> Ein Kilo Möhren kostet einen Euro zwanzig. Sonst noch etwas?</p>
                    <p><b>— Frau Nguyen:</b> Ja, welche Ananas ist süß?</p>
                    <p><b>— Verkäufer:</b> Diese Ananas hier ist sehr frisch und süß. Das Stück kostet zwei Euro dreißig.</p>
                    <p><b>— Frau Nguyen:</b> Gut, dann nehme ich die Ananas. Das ist alles. Wie viel macht das zusammen?</p>
                    <p><b>— Verkäufer:</b> Zwei Kilo Tomaten zu je 2,50 €, ein Kilo Möhren für 1,20 € und eine Ananas für 2,30 €. Das macht zusammen acht Euro fünfzig (8,50 €).</p>
                    <p><b>— Frau Nguyen:</b> Hier sind zehn Euro.</p>
                    <p><b>— Verkäufer:</b> Vielen Dank! Sie bekommen einen Euro fünfzig (1,50 €) zurück.</p>
                </div>
                <div class="text-slate-600 italic space-y-1 bg-slate-100/70 p-3 rounded-xl border border-slate-200">
                    <p class="font-bold not-italic text-slate-800">👉 Bản dịch tiếng Việt:</p>
                    <p>— Người bán: Xin chào! Quý khách muốn mua gì ạ?</p>
                    <p>— Bà Nguyen: Xin chào! Tôi muốn mua 2 ký cà chua và 1 ký cà rốt. Một ký cà rốt giá bao nhiêu?</p>
                    <p>— Người bán: Một ký cà rốt có giá 1 Euro 20. Quý khách cần gì thêm nữa không?</p>
                    <p>— Bà Nguyen: Vâng, quả dứa nào ngọt vậy?</p>
                    <p>— Người bán: Quả dứa ở đây rất tươi và ngọt. Mỗi quả có giá 2 Euro 30.</p>
                    <p>— Bà Nguyen: Tốt, vậy tôi lấy quả dứa này. Thế là đủ rồi. Tất cả hết bao nhiêu tiền?</p>
                    <p>— Người bán: 2 ký cà chua mỗi ký 2,50 €, 1 ký cà rốt 1,20 € và 1 quả dứa 2,30 €. Tổng cộng hết 8 Euro 50 (8,50 €).</p>
                    <p>— Bà Nguyen: Gửi anh 10 Euro.</p>
                    <p>— Người bán: Cảm ơn quý khách rất nhiều! Quý khách nhận lại 1 Euro 50 (1,50 €) tiền thừa.</p>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full border-collapse border border-slate-200 text-center text-xs">
                        <thead class="bg-indigo-50 text-indigo-950 font-bold">
                            <tr>
                                <th class="p-2 border border-slate-200 text-left">Mặt hàng</th>
                                <th class="p-2 border border-slate-200">Số lượng</th>
                                <th class="p-2 border border-slate-200">Đơn giá</th>
                                <th class="p-2 border border-slate-200">Thành tiền</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="p-2 border border-slate-200 text-left">Tomaten</td>
                                <td class="p-2 border border-slate-200">2 kg</td>
                                <td class="p-2 border border-slate-200">2,50 € / kg</td>
                                <td class="p-2 font-bold border border-slate-200">5,00 €</td>
                            </tr>
                            <tr>
                                <td class="p-2 border border-slate-200 text-left">Möhren</td>
                                <td class="p-2 border border-slate-200">1 kg</td>
                                <td class="p-2 border border-slate-200">1,20 € / kg</td>
                                <td class="p-2 font-bold border border-slate-200">1,20 €</td>
                            </tr>
                            <tr>
                                <td class="p-2 border border-slate-200 text-left">Ananas</td>
                                <td class="p-2 border border-slate-200">1 Stück</td>
                                <td class="p-2 border border-slate-200">2,30 €</td>
                                <td class="p-2 font-bold border border-slate-200">2,30 €</td>
                            </tr>
                            <tr class="bg-emerald-50 font-black text-emerald-950">
                                <td colspan="3" class="p-2 border border-slate-200 text-right">Tổng cộng (Das macht zusammen):</td>
                                <td class="p-2 border border-slate-200">8,50 € (acht Euro fünfzig)</td>
                            </tr>
                            <tr class="bg-slate-100 font-bold text-slate-800">
                                <td colspan="3" class="p-2 border border-slate-200 text-right">Tiền khách đưa (10,00 €) - Tiền thối lại (Wechselgeld):</td>
                                <td class="p-2 border border-slate-200 text-indigo-700">1,50 € (ein Euro fünfzig)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 9: BẢNG TỔNG HỢP KIẾN THỨC (CHEAT SHEET) -->
        <div class="p-6 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-800 pb-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-500/20 text-emerald-300 font-black text-sm flex items-center justify-center shrink-0">9</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-white">Bảng Tổng Hợp Kiến Thức (Cheat Sheet Bài 10)</h2>
                    <p class="text-xs text-slate-400">Tóm tắt các quy tắc vàng để làm bài tập đạt 100/100 điểm</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs leading-relaxed">
                <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <span class="font-bold text-emerald-400">1. Từ hỏi Welch-:</span>
                    <p class="text-slate-300">• <code>der → welcher</code> (Nom) / <code>welchen</code> (Akk)<br>• <code>die → welche</code> · <code>das → welches</code> · <code>số nhiều → welche</code>.<br>• Chỉ giống ĐỰC mới đổi giữa Nom và Akk!</p>
                </div>
                <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <span class="font-bold text-blue-400">2. Ba cặp so sánh bất quy tắc:</span>
                    <p class="text-slate-300">• <code>viel → mehr → am meisten</code> (số lượng)<br>• <code>gern → lieber → am liebsten</code> (sở thích)<br>• <code>gut → besser → am besten</code> (chất lượng)</p>
                </div>
                <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <span class="font-bold text-amber-400">3. Vị trí động từ khi đảo ngữ:</span>
                    <p class="text-slate-300">• Khi <code>Am liebsten / Am meisten / Am besten</code> đứng ở vị trí ①, động từ chia luôn ở vị trí ② rồi mới đến chủ ngữ ③: <i>„Am liebsten esse ich Nudeln.“</i></p>
                </div>
                <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <span class="font-bold text-purple-400">4. Đọc giá tiền Euro:</span>
                    <p class="text-slate-300">• <code>3,75 €</code> = <i>drei Euro fünfundsiebzig</i> (không đọc Komma, không đọc Cent).<br>• <code>0,50 €</code> = <i>fünfzig Cent</i> · <code>1,00 €</code> = <i>ein Euro</i>.</p>
                </div>
            </div>
        </div>
    </div>
    """

    raw_vocab = [
        [
                "der",
                "Käse",
                "phô mai (Pl: die Käse)",
                "Der Käse aus der Schweiz schmeckt sehr gut. (Phô mai từ Thụy Sĩ rất ngon.)"
        ],
        [
                "der",
                "Kuchen",
                "bánh ngọt (Pl: die Kuchen)",
                "Meine Oma backt am Sonntag einen Kuchen. (Bà tôi nướng bánh ngọt vào Chủ nhật.)"
        ],
        [
                "der",
                "Apfel",
                "quả táo (Pl: die Äpfel)",
                "Ein Apfel am Tag ist gesund. (Mỗi ngày một quả táo thì tốt cho sức khỏe.)"
        ],
        [
                "der",
                "Fisch",
                "cá (Pl: die Fische)",
                "Am Freitag gibt es Fisch mit Reis. (Thứ Sáu có cá với cơm.)"
        ],
        [
                "der",
                "Salat",
                "xà lách; món salad (Pl: die Salate)",
                "Zum Mittagessen esse ich einen Salat. (Vào bữa trưa tôi ăn một món salad.)"
        ],
        [
                "der",
                "Schinken",
                "thịt xông khói, giăm bông (Pl: die Schinken)",
                "Das Brötchen mit Schinken ist lecker. (Chiếc bánh mì kẹp giăm bông rất ngon.)"
        ],
        [
                "der",
                "Pfeffer",
                "tiêu (nur Singular)",
                "Bitte geben Sie mir Salz und Pfeffer. (Làm ơn đưa cho tôi muối và tiêu.)"
        ],
        [
                "die",
                "Salami",
                "xúc xích lên men (salami) (Pl: die Salamis)",
                "Ich esse gern ein Brötchen mit Salami. (Tôi thích ăn bánh mì kẹp salami.)"
        ],
        [
                "die",
                "Butter",
                "bơ (nur Singular)",
                "Zum Frühstück esse ich Brot mit Butter. (Vào bữa sáng tôi ăn bánh mì với bơ.)"
        ],
        [
                "die",
                "Kartoffel",
                "khoai tây (Pl: die Kartoffeln)",
                "Die Kartoffel ist sehr billig. (Khoai tây rất rẻ.)"
        ],
        [
                "die",
                "Tomate",
                "cà chua (Pl: die Tomaten)",
                "Die Tomate ist rot und frisch. (Quả cà chua đỏ và tươi.)"
        ],
        [
                "die",
                "Möhre",
                "cà rốt (Pl: die Möhren)",
                "Ich schneide eine Möhre für die Suppe. (Tôi thái một củ cà rốt cho món súp.)"
        ],
        [
                "die",
                "Erdbeere",
                "dâu tây (Pl: die Erdbeeren)",
                "Die Erdbeere ist süß und rot. (Quả dâu tây ngọt và đỏ.)"
        ],
        [
                "die",
                "Banane",
                "quả chuối (Pl: die Bananen)",
                "Die Banane ist gelb. (Quả chuối màu vàng.)"
        ],
        [
                "die",
                "Orange",
                "quả cam (Pl: die Orangen)",
                "Eine Orange hat viel Vitamin C. (Một quả cam có nhiều vitamin C.)"
        ],
        [
                "die",
                "Wurst",
                "xúc xích (Pl: die Würste)",
                "In Deutschland isst man gern Wurst. (Ở Đức người ta thích ăn xúc xích.)"
        ],
        [
                "die",
                "Birne",
                "quả lê (Pl: die Birnen)",
                "Die Birne schmeckt süß. (Quả lê có vị ngọt.)"
        ],
        [
                "die",
                "Nudel",
                "sợi mì, mì (Pl: die Nudeln)",
                "Zum Abendessen koche ich Nudeln. (Bữa tối tôi nấu mì.)"
        ],
        [
                "die",
                "Paprika",
                "ớt chuông (Pl: die Paprikas)",
                "Die Paprika ist heute billig. (Ớt chuông hôm nay rẻ.)"
        ],
        [
                "die",
                "Ananas",
                "quả dứa (Pl: die Ananas)",
                "Die Ananas aus Vietnam ist sehr süß. (Dứa từ Việt Nam rất ngọt.)"
        ],
        [
                "die",
                "Zwiebel",
                "hành tây (Pl: die Zwiebeln)",
                "Ich brauche eine Zwiebel für den Salat. (Tôi cần một củ hành tây cho món salad.)"
        ],
        [
                "das",
                "Brot",
                "bánh mì (Pl: die Brote)",
                "Das Brot ist noch warm. (Bánh mì vẫn còn ấm.)"
        ],
        [
                "das",
                "Hähnchen",
                "thịt gà (Pl: die Hähnchen)",
                "Wir essen heute Hähnchen mit Reis. (Hôm nay chúng tôi ăn thịt gà với cơm.)"
        ],
        [
                "das",
                "Ei",
                "quả trứng (Pl: die Eier)",
                "Zum Frühstück esse ich ein Ei. (Vào bữa sáng tôi ăn một quả trứng.)"
        ],
        [
                "das",
                "Fleisch",
                "thịt (nur Singular)",
                "Mein Bruder isst kein Fleisch. (Anh trai tôi không ăn thịt.)"
        ],
        [
                "der",
                "Reis",
                "gạo, cơm (nur Singular)",
                "In Vietnam isst man jeden Tag Reis. (Ở Việt Nam người ta ăn cơm mỗi ngày.)"
        ],
        [
                "der",
                "Preis",
                "giá cả (Pl: die Preise)",
                "Der Preis für den Käse ist hoch. (Giá của loại phô mai này cao.)"
        ],
        [
                "der",
                "Liter",
                "lít (Pl: die Liter (Sau số đếm giữ nguyên: zwei Liter))",
                "Ich kaufe zwei Liter Milch. (Tôi mua hai lít sữa.)"
        ],
        [
                "der",
                "Markt",
                "chợ (Pl: die Märkte)",
                "Auf dem Markt ist das Obst frisch. (Ở chợ hoa quả rất tươi.)"
        ],
        [
                "der",
                "Supermarkt",
                "siêu thị (Pl: die Supermärkte)",
                "Der Supermarkt ist bis zwanzig Uhr geöffnet. (Siêu thị mở cửa đến hai mươi giờ.)"
        ],
        [
                "der",
                "Saft",
                "nước ép (Pl: die Säfte)",
                "Zum Frühstück trinke ich ein Glas Saft. (Vào bữa sáng tôi uống một ly nước ép.)"
        ],
        [
                "der",
                "Kaffee",
                "cà phê (Pl: die Kaffees)",
                "Morgens trinke ich einen Kaffee. (Buổi sáng tôi uống một ly cà phê.)"
        ],
        [
                "der",
                "Joghurt",
                "sữa chua (Pl: die Joghurts)",
                "Der Joghurt mit Erdbeeren schmeckt gut. (Sữa chua vị dâu tây rất ngon.)"
        ],
        [
                "die",
                "Marmelade",
                "mứt (Pl: die Marmeladen)",
                "Ich esse gern Brot mit Marmelade. (Tôi thích ăn bánh mì với mứt.)"
        ],
        [
                "die",
                "Schokolade",
                "sô cô la (Pl: die Schokoladen)",
                "Die Schokolade ist sehr süß. (Sô cô la rất ngọt.)"
        ],
        [
                "die",
                "Milch",
                "sữa (nur Singular)",
                "Das Baby trinkt Milch. (Em bé uống sữa.)"
        ],
        [
                "die",
                "Cola",
                "nước cô-ca (Pl: die Colas)",
                "Die Cola ist schön kalt. (Cô-ca rất lạnh.)"
        ],
        [
                "die",
                "Dose",
                "lon, hộp (Pl: die Dosen)",
                "Ich kaufe drei Dosen Tomaten. (Tôi mua ba hộp cà chua.)"
        ],
        [
                "die",
                "Flasche",
                "cái chai (Pl: die Flaschen)",
                "Die Flasche Wasser kostet einen Euro. (Chai nước giá một euro.)"
        ],
        [
                "die",
                "Tüte",
                "cái túi (Pl: die Tüten)",
                "Ich brauche eine Tüte für das Obst. (Tôi cần một cái túi cho trái cây.)"
        ],
        [
                "die",
                "Bäckerei",
                "tiệm bánh mì (Pl: die Bäckereien)",
                "In der Bäckerei kaufe ich Brot und Kuchen. (Ở tiệm bánh tôi mua bánh mì và bánh ngọt.)"
        ],
        [
                "das",
                "Obst",
                "hoa quả, trái cây (nur Singular)",
                "Auf dem Markt kaufe ich frisches Obst. (Ở chợ tôi mua trái cây tươi.)"
        ],
        [
                "das",
                "Gemüse",
                "rau củ (nur Singular)",
                "Das Gemüse ist heute billig. (Rau củ hôm nay rẻ.)"
        ],
        [
                "das",
                "Eis",
                "kem; đá (nur Singular)",
                "Im Sommer esse ich gern Eis. (Mùa hè tôi thích ăn kem.)"
        ],
        [
                "das",
                "Salz",
                "muối (nur Singular)",
                "Die Suppe braucht noch Salz. (Món súp còn cần thêm muối.)"
        ],
        [
                "das",
                "Müsli",
                "ngũ cốc ăn sáng (Pl: die Müslis)",
                "Zum Frühstück esse ich Müsli mit Milch. (Vào bữa sáng tôi ăn ngũ cốc với sữa.)"
        ],
        [
                "das",
                "Schnitzel",
                "thịt tẩm bột chiên (Pl: die Schnitzel)",
                "Das Schnitzel mit Kartoffeln ist mein Lieblingsessen. (Món thịt tẩm bột chiên với khoai tây là món ăn yêu thích của tôi.)"
        ],
        [
                "das",
                "Kilo",
                "ký (kg) (Pl: die Kilos (Sau số đếm giữ nguyên: zwei Kilo))",
                "Ein Kilo Äpfel kostet zwei Euro vierzig. (Một ký táo giá hai euro bốn mươi.)"
        ],
        [
                "das",
                "Bier",
                "bia (Pl: die Biere)",
                "Mein Vater trinkt abends ein Bier. (Bố tôi uống một ly bia vào buổi tối.)"
        ],
        [
                "das",
                "Wasser",
                "nước (nur Singular)",
                "Ich trinke viel Wasser. (Tôi uống nhiều nước.)"
        ]
]

    vocabularies_data = []
    for art, word, meaning, example_str in raw_vocab:
        vocabularies_data.append((
            lesson_id,
            word,
            art if art else None,
            meaning,
            example_str
        ))

    cursor.execute("SELECT id FROM lessons WHERE id = ?;", (lesson_id,))
    existing_lesson = cursor.fetchone()

    if existing_lesson:
        cursor.execute("""
            UPDATE lessons SET title = ?, grammar_content = ? WHERE id = ?;
        """, (lesson_title, grammar_html, lesson_id))
    else:
        cursor.execute("""
            INSERT INTO lessons (id, level_id, title, grammar_content)
            VALUES (?, ?, ?, ?);
        """, (lesson_id, a1_id, lesson_title, grammar_html))

    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies_data)

    exercises_raw = [
        {
                "type": "trac_nghiem",
                "question": "Câu 1: Chọn từ hỏi đúng để hoàn thành câu: „___ Apfel kaufst du?“",
                "options": [
                        "Welcher",
                        "Welche",
                        "Welchen",
                        "Welches"
                ],
                "correct_answer": "Welchen",
                "explanation": "Trong câu này, 'du' là chủ ngữ (Nominativ), còn 'Apfel' là tân ngữ trực tiếp của động từ 'kaufst' nên ở Cách 4 (Akkusativ). Vì 'der Apfel' là danh từ giống đực (der -> den ở Akkusativ), từ hỏi 'welch-' phải nhận đuôi '-en' -> „Welchen Apfel kaufst du?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Bạn mua quả táo nào?"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 2: Chọn từ hỏi đúng để hoàn thành câu: „___ Bananen sind schon reif?“",
                "options": [
                        "Welcher",
                        "Welche",
                        "Welchen",
                        "Welches"
                ],
                "correct_answer": "Welche",
                "explanation": "'Bananen' là danh từ số nhiều (die Bananen), đóng vai trò làm chủ ngữ (Nominativ) của động từ 'sind'. Với danh từ số nhiều ở cả Nominativ và Akkusativ, từ hỏi 'welch-' luôn nhận đuôi '-e' -> „Welche Bananen sind schon reif?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Những quả chuối nào đã chín rồi?"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 3: Chọn từ hỏi đúng để hoàn thành câu: „___ Obst ist frisch?“",
                "options": [
                        "Welcher",
                        "Welche",
                        "Welchen",
                        "Welches"
                ],
                "correct_answer": "Welches",
                "explanation": "'Obst' (hoa quả/trái cây) là danh từ giống trung (das Obst), làm chủ ngữ trong câu. Với danh từ giống trung (das) ở cả Nominativ và Akkusativ, từ hỏi 'welch-' luôn nhận đuôi '-es' -> „Welches Obst ist frisch?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Loại hoa quả nào tươi?"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 4: Chọn dạng đúng của tính từ 'billig' để hoàn thành câu: „Der Apfel ist ___ als die Birne.“",
                "options": [
                        "billiger",
                        "billigere",
                        "billigster",
                        "am billigsten"
                ],
                "correct_answer": "billiger",
                "explanation": "Trong câu có liên từ 'als' (hơn) dùng để so sánh giữa hai đối tượng ('der Apfel' và 'die Birne'), nên cần dùng bậc so sánh hơn (Komparativ). Trong tiếng Đức, mọi tính từ có quy tắc đều tạo Komparativ bằng cách thêm đuôi '-er' vào gốc tính từ (billig + -er -> billiger) và giữ nguyên không chia đuôi khi đứng sau động từ 'sein' (ist).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Quả táo rẻ hơn quả lê."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 5: Chọn dạng đúng để hoàn thành câu: „Der Fisch ist ___.“",
                "options": [
                        "am teuerten",
                        "am teuersten",
                        "am teurersten",
                        "am teuerrsten"
                ],
                "correct_answer": "am teuersten",
                "explanation": "Cả 4 phương án đều ở bậc so sánh nhất (Superlativ) của tính từ 'teuer' (đắt). Lưu ý quy tắc chính tả: tính từ 'teuer' chỉ lược bỏ chữ '-e-' ở bậc so sánh hơn ('teurer'), còn ở bậc so sánh nhất vẫn giữ nguyên gốc 'teuer' + '-sten' -> 'am teuersten' (các cách viết 'am teurersten', 'am teuerrsten', 'am teuerten' đều sai chính tả).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Món cá có giá đắt nhất."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 6: Chọn từ chỉ số lượng đúng để hoàn thành câu: „Auf dem Markt kaufe ich ___ Äpfel.“",
                "options": [
                        "viel",
                        "viele",
                        "vieler",
                        "viels"
                ],
                "correct_answer": "viele",
                "explanation": "'Äpfel' (những quả táo) là danh từ đếm được ở dạng số nhiều nên bắt buộc đi với 'viele' (có đuôi '-e'). Từ 'viel' (không đuôi) chỉ đi với danh từ không đếm được số ít (như 'viel Obst', 'viel Wasser'), còn 'viels' không tồn tại.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Ở chợ tôi mua nhiều quả táo."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 7: Chọn từ đúng để hoàn thành câu: „Ich esse Reis ___ als Brot.“",
                "options": [
                        "gern",
                        "am liebsten",
                        "besser",
                        "lieber"
                ],
                "correct_answer": "lieber",
                "explanation": "Trong câu có từ 'als' (hơn) nên bắt buộc dùng bậc so sánh hơn (Komparativ) -> loại 'gern' (nguyên mức) và 'am liebsten' (so sánh nhất). Khi nói thích ăn/uống món gì hơn món gì ('essen/trinken + ... + als'), tiếng Đức dùng dạng so sánh hơn của 'gern' là 'lieber' (không dùng 'besser' vì 'besser' chỉ chất lượng hoặc kỹ năng làm việc gì giỏi hơn).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi thích ăn cơm hơn bánh mì."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 8: Chọn câu đúng ngữ pháp tiếng Đức:",
                "options": [
                        "Am liebsten ich esse Schokolade.",
                        "Am liebsten Schokolade esse ich.",
                        "Ich am liebsten esse Schokolade.",
                        "Am liebsten esse ich Schokolade."
                ],
                "correct_answer": "Am liebsten esse ich Schokolade.",
                "explanation": "Theo quy tắc vị trí động từ trong câu trần thuật tiếng Đức (Verbzweitstellung - V2), khi đưa cụm trạng từ so sánh nhất 'Am liebsten' lên đầu câu (Vị trí 1) để nhấn mạnh, động từ chia 'esse' bắt buộc phải đứng ngay ở Vị trí 2, sau đó mới đến chủ ngữ 'ich' ở Vị trí 3 -> „Am liebsten esse ich Schokolade.“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi thích ăn sô-cô-la nhất."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 9: Người bán hỏi: „Was darf es sein?“ — Câu trả lời tự nhiên và đúng ngữ pháp nhất của khách hàng là:",
                "options": [
                        "Was darf es sein?",
                        "Ich hätte gern zwei Kilo Äpfel.",
                        "Ja, bitte, Äpfel haben.",
                        "Ich bin zwei Kilo Äpfel."
                ],
                "correct_answer": "Ich hätte gern zwei Kilo Äpfel.",
                "explanation": "Câu hỏi „Was darf es sein?“ là mẫu câu lịch sự rất phổ biến của người bán hàng tại Đức. Để trả lời lịch sự, khách hàng dùng cấu trúc „Ich hätte gern / Ich möchte + [Món hàng ở Akkusativ]“ -> „Ich hätte gern zwei Kilo Äpfel.“ (đơn vị đo 'Kilo' giữ nguyên số ít sau số đếm 'zwei', danh từ đếm được 'Äpfel' ở số nhiều). Các lựa chọn còn lại đều sai: „Was darf es sein?“ hoặc „Es darf Äpfel sein.“ là lặp lại máy móc câu hỏi của người bán; „Ja, bitte, Äpfel haben.“ sai cấu trúc câu; „Ich bin zwei Kilo Äpfel.“ (Tôi là 2 ký táo) sai hoàn toàn về nghĩa.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Người bán: „Quý khách muốn mua gì ạ?“ — Khách hàng: „Cho tôi lấy hai ký táo.“"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 10: Dòng nào dưới đây ghi ĐÚNG cả mạo từ (giống) lẫn dạng số nhiều của cả 3 danh từ?",
                "options": [
                        "der Käse – die Käsen / die Wurst – die Wursten / der Fisch – die Fischs",
                        "der Apfel – die Apfels / die Birne – die Birne / das Ei – die Eis",
                        "der Apfel – die Äpfel / die Birne – die Birnen / das Ei – die Eier",
                        "die Apfel – die Äpfel / der Birne – die Birnen / das Ei – die Eier"
                ],
                "correct_answer": "der Apfel – die Äpfel / die Birne – die Birnen / das Ei – die Eier",
                "explanation": "Dòng đúng duy nhất là „der Apfel – die Äpfel / die Birne – die Birnen / das Ei – die Eier“ vì chính xác cả giống lẫn quy tắc số nhiều ở cả 3 từ: 'der Apfel -> die Äpfel' (giống đực, số nhiều thêm Umlaut ä), 'die Birne -> die Birnen' (giống cái tận cùng bằng -e, số nhiều thêm -n), 'das Ei -> die Eier' (giống trung, số nhiều thêm -er). Các dòng còn lại đều sai đuôi số nhiều (như *die Käsen, *die Wursten, *die Fischs, *die Apfels, *die Eis) hoặc sai giống của danh từ (*die Apfel, *der Birne).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "quả táo – những quả táo / quả lê – những quả lê / quả trứng – những quả trứng."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 11: Điền dạng đúng của từ hỏi 'welch-' để hoàn thành câu: „___ Salat ist gesund?“",
                "options": null,
                "correct_answer": "Welcher",
                "explanation": "Danh từ 'der Salat' (giống đực) đứng trước động từ 'ist' nên đóng vai trò làm chủ ngữ (Nominativ). Với giống đực ở Nominativ, từ hỏi 'welch-' nhận đuôi '-er' -> „Welcher Salat ist gesund?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Món salad nào tốt cho sức khỏe?",
                        "accepted_answers": [
                                "Welcher",
                                "welcher"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 12: Điền dạng đúng của từ hỏi 'welch-' để hoàn thành câu: „___ Schinken möchtest du?“",
                "options": null,
                "correct_answer": "Welchen",
                "explanation": "Trong câu này 'du' là chủ ngữ, còn 'der Schinken' (giống đực) là tân ngữ trực tiếp của động từ 'möchtest' nên ở Cách 4 (Akkusativ: der -> den). Từ hỏi 'welch-' phải nhận đuôi '-en' -> „Welchen Schinken möchtest du?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Bạn muốn loại giăm bông nào?",
                        "accepted_answers": [
                                "Welchen",
                                "welchen"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 13: Điền dạng đúng của từ hỏi 'welch-' để hoàn thành câu: „___ Brot möchtest du?“",
                "options": null,
                "correct_answer": "Welches",
                "explanation": "'das Brot' là danh từ giống trung, đóng vai trò tân ngữ (Akkusativ) của động từ 'möchtest'. Với giống trung (das), từ hỏi 'welch-' luôn giữ đuôi '-es' ở cả Nominativ và Akkusativ -> „Welches Brot möchtest du?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Bạn muốn loại bánh mì nào?",
                        "accepted_answers": [
                                "Welches",
                                "welches"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 14: Điền dạng đúng của từ hỏi 'welch-' để hoàn thành câu: „___ Kartoffeln brauchen wir?“",
                "options": null,
                "correct_answer": "Welche",
                "explanation": "'wir' là chủ ngữ, còn 'die Kartoffeln' là danh từ số nhiều ở Cách 4 (Akkusativ). Với danh từ số nhiều, từ hỏi 'welch-' luôn nhận đuôi '-e' ở cả Nominativ và Akkusativ -> „Welche Kartoffeln brauchen wir?“.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chúng ta cần những củ khoai tây nào?",
                        "accepted_answers": [
                                "Welche",
                                "welche"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 15: Điền dạng đúng của tính từ 'teuer' để hoàn thành câu: „Ein Kilo Fleisch ist ___ als ein Kilo Kartoffeln.“",
                "options": null,
                "correct_answer": "teurer",
                "explanation": "Trong câu có liên từ 'als' (hơn) dùng để so sánh giữa hai đối tượng nên cần dùng bậc so sánh hơn (Komparativ). Tính từ 'teuer' có đuôi '-er', khi thêm đuôi '-er' của Komparativ phải lược bỏ chữ '-e-' ở gốc -> 'teurer'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Một ký thịt đắt hơn một ký khoai tây.",
                        "accepted_answers": [
                                "teurer"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 16: Chọn và điền từ thích hợp ('viel', 'viele' hoặc 'mehr') vào chỗ trống: „Mein Bruder isst ___ Reis als ich.“",
                "options": null,
                "correct_answer": "mehr",
                "explanation": "Trong câu có cấu trúc so sánh hơn với 'als' ('... als ich') nên phải dùng dạng so sánh hơn của 'viel' là 'mehr' (dùng được cho cả danh từ đếm được lẫn không đếm được như 'Reis').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Anh trai tôi ăn cơm nhiều hơn tôi.",
                        "accepted_answers": [
                                "mehr"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 17: Điền dạng đúng của từ 'gern' để hoàn thành câu: „Von allen Früchten esse ich ___ Erdbeeren.“",
                "options": null,
                "correct_answer": "am liebsten",
                "explanation": "Cụm từ „Von allen Früchten“ (Trong tất cả các loại trái cây) cho thấy đây là phép so sánh nhất (Superlativ) giữa dâu tây với toàn bộ các loại quả khác. Dạng bất quy tắc của 'gern' ở Superlativ là 'am liebsten' (gern -> lieber -> am liebsten).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Trong tất cả các loại trái cây, tôi thích ăn dâu tây nhất.",
                        "accepted_answers": [
                                "am liebsten",
                                "Am liebsten"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 18: Điền dạng đúng của tính từ 'gesund' để hoàn thành câu: „Der Salat ist gesund, aber Möhren sind noch ___.“",
                "options": null,
                "correct_answer": "gesünder",
                "explanation": "Vế sau dùng 'aber ... sind noch ...' (nhưng ... còn ... hơn nữa) để so sánh mức độ tốt cho sức khỏe của cà rốt cao hơn salad -> dùng bậc so sánh hơn (Komparativ). Tính từ 'gesund' biến âm Umlaut 'u -> ü' khi thêm '-er' -> 'gesünder'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Salad tốt cho sức khỏe, nhưng cà rốt còn tốt hơn nữa.",
                        "accepted_answers": [
                                "gesünder",
                                "gesuender"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 19: Chia dạng đúng của động từ 'essen' để hoàn thành câu: „Du ___ gern Fisch.“",
                "options": null,
                "correct_answer": "isst",
                "explanation": "Chủ ngữ là ngôi thứ hai số ít 'du'. Động từ 'essen' (ăn) là động từ bất quy tắc đổi nguyên âm gốc 'e -> i' ở ngôi 'du' và 'er/sie/es' -> 'du isst'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Bạn thích ăn cá.",
                        "accepted_answers": [
                                "isst"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 20: Chia dạng đúng của động từ 'kosten' để hoàn thành câu: „Was ___ ein Kilo Birnen?“",
                "options": null,
                "correct_answer": "kostet",
                "explanation": "Danh từ trung tâm của chủ ngữ 'ein Kilo Birnen' là đơn vị đo số ít 'ein Kilo' (một ký - không chia theo từ 'Birnen' phía sau) -> chia động từ 'kosten' ở ngôi thứ ba số ít: 'kostet'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Một ký lê giá bao nhiêu?",
                        "accepted_answers": [
                                "kostet"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 21: Chia dạng đúng của động từ 'kosten' để hoàn thành câu: „Wie viel ___ drei Dosen Cola?“",
                "options": null,
                "correct_answer": "kosten",
                "explanation": "Khác với đơn vị đo lường ('Kilo', 'Liter') luôn giữ số ít, đơn vị đóng gói 'die Dose' (cái lon) có dạng số nhiều là 'die Dosen'. Chủ ngữ 'drei Dosen Cola' là số nhiều nên động từ 'kosten' chia ở dạng nguyên mẫu số nhiều -> 'kosten'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Ba lon cô-ca giá bao nhiêu?",
                        "accepted_answers": [
                                "kosten"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 22: Chia dạng đúng của động từ 'kochen' để hoàn thành câu: „Ihr ___ heute Abend Nudeln.“",
                "options": null,
                "correct_answer": "kocht",
                "explanation": "Chủ ngữ là ngôi thứ hai số nhiều 'ihr' (các bạn). Động từ có quy tắc 'kochen' lấy gốc 'koch-' cộng đuôi '-t' -> 'ihr kocht'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tối nay các bạn nấu mì.",
                        "accepted_answers": [
                                "kocht"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 23: Dịch sang tiếng Đức (kèm mạo từ số ít): \"cà rốt\"",
                "options": null,
                "correct_answer": "die Möhre",
                "explanation": "Cà rốt trong tiếng Đức là 'die Möhre' (hoặc 'die Karotte'); số nhiều là 'die Möhren'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "cà rốt = die Möhre",
                        "accepted_answers": [
                                "die Möhre",
                                "Möhre",
                                "die Karotte",
                                "Karotte",
                                "die Moehre",
                                "Moehre"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 24: Dịch sang tiếng Đức (kèm mạo từ số ít): \"hành tây\"",
                "options": null,
                "correct_answer": "die Zwiebel",
                "explanation": "Hành tây trong tiếng Đức là 'die Zwiebel' (số nhiều: 'die Zwiebeln').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "hành tây = die Zwiebel",
                        "accepted_answers": [
                                "die Zwiebel",
                                "Zwiebel"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 25: Dịch sang tiếng Đức (kèm mạo từ số ít): \"thịt gà\"",
                "options": null,
                "correct_answer": "das Hähnchen",
                "explanation": "Thịt gà là 'das Hähnchen' (đuôi '-chen' luôn mang giống trung 'das').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "thịt gà = das Hähnchen",
                        "accepted_answers": [
                                "das Hähnchen",
                                "Hähnchen",
                                "das Haehnchen",
                                "Haehnchen"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 26: Dịch sang tiếng Đức (kèm mạo từ số ít): \"gạo, cơm\"",
                "options": null,
                "correct_answer": "der Reis",
                "explanation": "Gạo, cơm trong tiếng Đức là 'der Reis' (danh từ giống đực, chỉ dùng ở số ít).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "gạo, cơm = der Reis",
                        "accepted_answers": [
                                "der Reis",
                                "Reis"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 27: Dịch sang tiếng Đức (kèm mạo từ số ít): \"ngũ cốc ăn sáng\"",
                "options": null,
                "correct_answer": "das Müsli",
                "explanation": "Ngũ cốc ăn sáng là 'das Müsli' (số nhiều: 'die Müslis').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "ngũ cốc ăn sáng = das Müsli",
                        "accepted_answers": [
                                "das Müsli",
                                "Müsli",
                                "das Muesli",
                                "Muesli"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 28: Dịch sang tiếng Đức (kèm mạo từ số ít): \"quả dứa\"",
                "options": null,
                "correct_answer": "die Ananas",
                "explanation": "Quả dứa là 'die Ananas' (số nhiều giữ nguyên: 'die Ananas').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "quả dứa = die Ananas",
                        "accepted_answers": [
                                "die Ananas",
                                "Ananas"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 29: Dịch sang tiếng Đức: \"một lon cô-ca\"",
                "options": null,
                "correct_answer": "eine Dose Cola",
                "explanation": "'die Dose' là danh từ giống cái -> 'eine Dose Cola' (không cần giới từ giữa đơn vị và danh từ).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "một lon cô-ca = eine Dose Cola",
                        "accepted_answers": [
                                "eine Dose Cola",
                                "eine Dose cola"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 30: Dịch sang tiếng Đức: \"một lít sữa\"",
                "options": null,
                "correct_answer": "ein Liter Milch",
                "explanation": "'der Liter' là giống đực, đi kèm 'die Milch' -> 'ein Liter Milch' (khi là tân ngữ: 'einen Liter Milch').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "một lít sữa = ein Liter Milch",
                        "accepted_answers": [
                                "ein Liter Milch",
                                "einen Liter Milch",
                                "ein liter milch"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 31: Dịch sang tiếng Việt: „der Schinken“",
                "options": null,
                "correct_answer": "thịt xông khói",
                "explanation": "'der Schinken' nghĩa là thịt xông khói hoặc giăm bông (số nhiều: 'die Schinken').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "thịt xông khói / giăm bông",
                        "accepted_answers": [
                                "thịt xông khói",
                                "giăm bông",
                                "thịt nguội",
                                "thịt giăm bông"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 32: Dịch sang tiếng Việt: „die Paprika“",
                "options": null,
                "correct_answer": "ớt chuông",
                "explanation": "'die Paprika' nghĩa là quả ớt chuông (số nhiều: 'die Paprikas').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "ớt chuông",
                        "accepted_answers": [
                                "ớt chuông",
                                "quả ớt chuông",
                                "ớt ngọt"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 33: Dịch sang tiếng Việt: „das Schnitzel“",
                "options": null,
                "correct_answer": "thịt tẩm bột chiên",
                "explanation": "'das Schnitzel' là món thịt tẩm bột chiên truyền thống (số nhiều: 'die Schnitzel').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "thịt tẩm bột chiên",
                        "accepted_answers": [
                                "thịt tẩm bột chiên",
                                "món thịt tẩm bột chiên",
                                "schnitzel",
                                "thịt chiên xù"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 34: Dịch sang tiếng Việt: „die Erdbeere“",
                "options": null,
                "correct_answer": "dâu tây",
                "explanation": "'die Erdbeere' nghĩa là quả dâu tây (số nhiều: 'die Erdbeeren').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "dâu tây",
                        "accepted_answers": [
                                "dâu tây",
                                "quả dâu tây"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 35: Dịch sang tiếng Việt: „Das macht zusammen vier Euro.“",
                "options": null,
                "correct_answer": "Tổng cộng là bốn euro.",
                "explanation": "'Das macht zusammen ...' = 'tổng cộng là ... / tất cả hết ...' (mẫu câu chốt tổng hóa đơn khi tính tiền); 'vier Euro' = bốn euro (4 euro).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tổng cộng là bốn euro.",
                        "accepted_answers": [
                                "Tổng cộng là bốn euro.",
                                "Tổng cộng là 4 euro.",
                                "Tổng cộng bốn euro.",
                                "Tổng cộng 4 euro.",
                                "Tất cả hết bốn euro.",
                                "Tất cả hết 4 euro.",
                                "Tất cả là bốn euro.",
                                "Tất cả là 4 euro.",
                                "Cộng lại là bốn euro.",
                                "Cộng lại là 4 euro.",
                                "Tất cả hết 4€.",
                                "Tổng cộng là 4€."
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 36: Dịch sang tiếng Việt: „Haben Sie Schokolade?“",
                "options": null,
                "correct_answer": "Ngài có sô cô la không?",
                "explanation": "'Haben Sie ...?' là mẫu câu hỏi lịch sự khi đi mua hàng để hỏi xem tiệm/người bán có mặt hàng nào đó hay không; 'Sie' = ngài / anh / chị; 'Schokolade' = sô cô la (socola).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Ngài có sô cô la không?",
                        "accepted_answers": [
                                "Ngài có sô cô la không?",
                                "Ngài có socola không?",
                                "Ngài có sô-cô-la không?",
                                "Anh có socola không?",
                                "Chị có socola không?",
                                "Bạn có socola không?",
                                "Quý khách có socola không?",
                                "Anh có sô cô la không?",
                                "Chị có sô cô la không?",
                                "Bạn có sô cô la không?",
                                "Quý khách có sô cô la không?",
                                "Quý khách có sô-cô-la không?",
                                "Cửa hàng có socola không?",
                                "Tiệm có socola không?",
                                "Ở đây có socola không?",
                                "Cửa hàng có sô cô la không?",
                                "Tiệm có sô cô la không?",
                                "Ở đây có sô cô la không?",
                                "Ông có sô cô la không?",
                                "Bà có sô cô la không?",
                                "Ông có socola không?",
                                "Bà có socola không?",
                                "Anh chị có sô cô la không?",
                                "Anh chị có socola không?"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 37: Dịch sang tiếng Việt: „Ich hätte gern einen Liter Milch.“",
                "options": null,
                "correct_answer": "Tôi muốn lấy một lít sữa.",
                "explanation": "'Ich hätte gern ...' = 'tôi muốn lấy ... / cho tôi ...' (mẫu câu lịch sự khi đi mua sắm); 'einen Liter Milch' = một lít sữa (1 lít sữa).",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi muốn lấy một lít sữa.",
                        "accepted_answers": [
                                "Tôi muốn lấy một lít sữa.",
                                "Tôi muốn lấy 1 lít sữa.",
                                "Tôi muốn một lít sữa.",
                                "Tôi muốn 1 lít sữa.",
                                "Cho tôi một lít sữa.",
                                "Cho tôi 1 lít sữa.",
                                "Tôi cần một lít sữa.",
                                "Tôi cần 1 lít sữa."
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 38: Dịch sang tiếng Việt: „Wie viel kosten die Birnen?“",
                "options": null,
                "correct_answer": "Những quả lê giá bao nhiêu?",
                "explanation": "'Wie viel kosten ...?' dùng cho chủ ngữ số nhiều ('die Birnen') = '... giá bao nhiêu? / bao nhiêu tiền?'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Những quả lê giá bao nhiêu?",
                        "accepted_answers": [
                                "Những quả lê giá bao nhiêu?",
                                "Các quả lê giá bao nhiêu?",
                                "Mấy quả lê giá bao nhiêu?",
                                "các quả lê giá bao nhiêu",
                                "mấy quả lê giá bao nhiêu",
                                "Lê giá bao nhiêu?",
                                "Những quả lê bao nhiêu tiền?",
                                "Các quả lê bao nhiêu tiền?",
                                "Mấy quả lê này giá bao nhiêu?",
                                "Những quả lê này giá bao nhiêu?"
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 39: Nối từ tiếng Đức với nghĩa tiếng Việt tương ứng:",
                "options": null,
                "correct_answer": "die Birne - quả lê | die Erdbeere - dâu tây | die Orange - quả cam | die Ananas - quả dứa",
                "explanation": "Cả 4 loại trái cây đều là danh từ giống cái ('die'): 'die Birne' = quả lê; 'die Erdbeere' = dâu tây; 'die Orange' = quả cam; 'die Ananas' = quả dứa.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "die Birne - quả lê | die Erdbeere - dâu tây | die Orange - quả cam | die Ananas - quả dứa",
                        "noi_o_pairs": [
                                {
                                        "left": "die Birne",
                                        "right": "quả lê"
                                },
                                {
                                        "left": "die Erdbeere",
                                        "right": "dâu tây"
                                },
                                {
                                        "left": "die Orange",
                                        "right": "quả cam"
                                },
                                {
                                        "left": "die Ananas",
                                        "right": "quả dứa"
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 40: Nối danh từ số ít với dạng số nhiều tương ứng:",
                "options": null,
                "correct_answer": "der Apfel - die Äpfel | das Ei - die Eier | die Kartoffel - die Kartoffeln | der Kuchen - die Kuchen",
                "explanation": "'der Apfel -> die Äpfel' (thêm Umlaut); 'das Ei -> die Eier' (thêm -er); 'die Kartoffel -> die Kartoffeln' (thêm -n); 'der Kuchen -> die Kuchen' (giữ nguyên).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "quả táo – những quả táo | quả trứng – những quả trứng | củ khoai tây – những củ khoai tây | bánh ngọt – những chiếc bánh ngọt",
                        "noi_o_pairs": [
                                {
                                        "left": "der Apfel",
                                        "right": "die Äpfel"
                                },
                                {
                                        "left": "das Ei",
                                        "right": "die Eier"
                                },
                                {
                                        "left": "die Kartoffel",
                                        "right": "die Kartoffeln"
                                },
                                {
                                        "left": "der Kuchen",
                                        "right": "die Kuchen"
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 41: Nối câu hỏi với câu trả lời tương ứng:",
                "options": null,
                "correct_answer": "Welche Orangen sind frisch? - Die Orangen aus Spanien. | Welches Brot schmeckt gut? - Das Brot vom Bäcker. | Welchen Joghurt kaufst du? - Den Joghurt mit Erdbeeren. | Welcher Fisch ist heute billig? - Der Fisch aus dem Fluss.",
                "explanation": "Câu trả lời rút gọn dùng mạo từ xác định tương ứng với Giống và Cách của từ hỏi: 'welche Orangen' (số nhiều) -> 'Die Orangen'; 'welches Brot' (giống trung) -> 'Das Brot'; 'welchen Joghurt' (giống đực, tân ngữ Akkusativ) -> 'Den Joghurt'; 'welcher Fisch' (giống đực, chủ ngữ Nominativ) -> 'Der Fisch'.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Những quả cam nào tươi? – Những quả cam từ Tây Ban Nha. | Loại bánh mì nào ngon? – Bánh mì của tiệm bánh. | Bạn mua loại sữa chua nào? – Sữa chua vị dâu tây. | Con cá nào hôm nay rẻ? – Con cá từ sông.",
                        "noi_o_pairs": [
                                {
                                        "left": "Welche Orangen sind frisch?",
                                        "right": "Die Orangen aus Spanien."
                                },
                                {
                                        "left": "Welches Brot schmeckt gut?",
                                        "right": "Das Brot vom Bäcker."
                                },
                                {
                                        "left": "Welchen Joghurt kaufst du?",
                                        "right": "Den Joghurt mit Erdbeeren."
                                },
                                {
                                        "left": "Welcher Fisch ist heute billig?",
                                        "right": "Der Fisch aus dem Fluss."
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 42: Nối động từ nguyên mẫu với dạng chia tương ứng:",
                "options": null,
                "correct_answer": "essen - isst | nehmen - nimmt | geben - gibt | empfehlen - empfiehlt",
                "explanation": "Bốn động từ bất quy tắc nhóm đổi nguyên âm 'e -> i / ie' ở ngôi thứ 3 số ít: 'essen -> isst', 'nehmen -> nimmt', 'geben -> gibt', 'empfehlen -> empfiehlt'.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "ăn – (anh ấy) ăn | lấy – (anh ấy) lấy | cho/có – (nó) cho/có | giới thiệu – (anh ấy) giới thiệu",
                        "noi_o_pairs": [
                                {
                                        "left": "essen",
                                        "right": "isst"
                                },
                                {
                                        "left": "nehmen",
                                        "right": "nimmt"
                                },
                                {
                                        "left": "geben",
                                        "right": "gibt"
                                },
                                {
                                        "left": "empfehlen",
                                        "right": "empfiehlt"
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 43: Nối động từ với dạng Partizip II (ôn tập Perfekt Bài 9):",
                "options": null,
                "correct_answer": "kaufen - gekauft | essen - gegessen | bestellen - bestellt | einkaufen - eingekauft",
                "explanation": "'kaufen -> gekauft' (ge-t); 'essen -> gegessen' (bất quy tắc); 'bestellen -> bestellt' (tiền tố be- không tách, không ge-); 'einkaufen -> eingekauft' (tiền tố tách ein- -> ein + ge + kauft).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "mua – đã mua | ăn – đã ăn | gọi món – đã gọi món | mua sắm – đã mua sắm",
                        "noi_o_pairs": [
                                {
                                        "left": "kaufen",
                                        "right": "gekauft"
                                },
                                {
                                        "left": "essen",
                                        "right": "gegessen"
                                },
                                {
                                        "left": "bestellen",
                                        "right": "bestellt"
                                },
                                {
                                        "left": "einkaufen",
                                        "right": "eingekauft"
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 44: Nối tính từ nguyên mức với dạng so sánh hơn (Komparativ):",
                "options": null,
                "correct_answer": "billig - billiger | teuer - teurer | gesund - gesünder | groß - größer",
                "explanation": "'billig -> billiger' (+ -er); 'teuer -> teurer' (bỏ âm e); 'gesund -> gesünder' (thêm Umlaut u -> ü); 'groß -> größer' (thêm Umlaut o -> ö).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "rẻ – rẻ hơn | đắt – đắt hơn | tốt cho sức khỏe – tốt hơn cho sức khỏe | to – to hơn",
                        "noi_o_pairs": [
                                {
                                        "left": "billig",
                                        "right": "billiger"
                                },
                                {
                                        "left": "teuer",
                                        "right": "teurer"
                                },
                                {
                                        "left": "gesund",
                                        "right": "gesünder"
                                },
                                {
                                        "left": "groß",
                                        "right": "größer"
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 45: Nối từ gốc với dạng so sánh nhất (Superlativ):",
                "options": null,
                "correct_answer": "gern - am liebsten | viel - am meisten | gut - am besten | billig - am billigsten",
                "explanation": "Ba cặp bất quy tắc bắt buộc thuộc: 'gern -> am liebsten', 'viel -> am meisten', 'gut -> am besten'; 'billig -> am billigsten' (theo quy tắc am + …sten).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "thích – thích nhất | nhiều – nhiều nhất | tốt – tốt nhất | rẻ – rẻ nhất",
                        "noi_o_pairs": [
                                {
                                        "left": "gern",
                                        "right": "am liebsten"
                                },
                                {
                                        "left": "viel",
                                        "right": "am meisten"
                                },
                                {
                                        "left": "gut",
                                        "right": "am besten"
                                },
                                {
                                        "left": "billig",
                                        "right": "am billigsten"
                                }
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 46: Nối đơn vị đo / đóng gói với thực phẩm đi kèm phù hợp:",
                "options": null,
                "correct_answer": "eine Dose - Cola | ein Stück - Kuchen | ein Liter - Milch | ein Kilo - Kartoffeln",
                "explanation": "Các cụm đơn vị đo lường & đóng gói thông dụng trong mua sắm: 'eine Dose Cola' (một lon cô-ca), 'ein Stück Kuchen' (một miếng bánh ngọt), 'ein Liter Milch' (một lít sữa), 'ein Kilo Kartoffeln' (một ký khoai tây).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "một lon – cô-ca | một miếng – bánh ngọt | một lít – sữa | một ký – khoai tây",
                        "noi_o_pairs": [
                                {
                                        "left": "eine Dose",
                                        "right": "Cola"
                                },
                                {
                                        "left": "ein Stück",
                                        "right": "Kuchen"
                                },
                                {
                                        "left": "ein Liter",
                                        "right": "Milch"
                                },
                                {
                                        "left": "ein Kilo",
                                        "right": "Kartoffeln"
                                }
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 47: Điền 2 từ để hoàn thành hội thoại: „Quý khách muốn món xà lách nào? — Cho tôi phần xà lách đó nhé.“ (ngăn cách bởi dấu /): [1] Salat möchten Sie? — [2] Salat, bitte.",
                "options": null,
                "correct_answer": "Welchen / Den",
                "explanation": "Danh từ 'der Salat' (giống đực) đóng vai trò là tân ngữ trực tiếp (Akkusativ) của động từ 'möchten' (và động từ lược bỏ ở câu trả lời). Do đó, ở Cách 4 (Akkusativ), từ hỏi 'welch-' nhận đuôi '-en' ('Welchen Salat...?') và mạo từ xác định trong câu trả lời cũng đổi từ 'der' sang 'den' ('Den Salat, bitte.' - hoặc dùng đại từ chỉ định 'Diesen Salat, bitte.').",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Quý khách muốn món xà lách nào? — Cho tôi phần xà lách đó nhé.",
                        "accepted_answers": [
                                "Welchen / Den",
                                "welchen / den",
                                "Welchen/Den",
                                "welchen/den",
                                "Welchen Den",
                                "welchen den",
                                "Welchen / Diesen",
                                "welchen / diesen",
                                "Welchen/Diesen",
                                "welchen/diesen",
                                "Welchen Diesen",
                                "welchen diesen"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 48: Điền 2 từ để hoàn thành câu: „Hôm nay cà rốt rẻ hơn cà chua.“ (ngăn cách bởi dấu /): Die Möhren sind heute [1] [2] die Tomaten.",
                "options": null,
                "correct_answer": "billiger / als",
                "explanation": "Để diễn tả phép so sánh hơn (Komparativ) của tính từ 'billig' (rẻ), ta thêm đuôi '-er' vào gốc tính từ -> 'billiger' và dùng liên từ 'als' (hơn) đứng trước đối tượng so sánh 'die Tomaten'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Hôm nay cà rốt rẻ hơn cà chua.",
                        "accepted_answers": [
                                "billiger / als",
                                "billiger/als",
                                "billiger als",
                                "Billiger / als",
                                "Billiger als",
                                "günstiger / als",
                                "günstiger/als",
                                "günstiger als",
                                "Günstiger / als",
                                "Günstiger als"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 49: Điền 2 từ để hoàn thành câu: „Tôi ăn cơm nhiều hơn mì.“ (ngăn cách bởi dấu /): Ich esse [1] Reis [2] Nudeln.",
                "options": null,
                "correct_answer": "mehr / als",
                "explanation": "Khi so sánh số lượng nhiều hơn giữa hai danh từ ('Reis' và 'Nudeln'), tiếng Đức dùng dạng so sánh hơn bất quy tắc của 'viel' là 'mehr' kết hợp với liên từ 'als' -> cấu trúc 'mehr ... als ...'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi ăn cơm nhiều hơn mì.",
                        "accepted_answers": [
                                "mehr / als",
                                "mehr/als",
                                "mehr als",
                                "Mehr / als",
                                "Mehr als"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 50: Điền 2 từ để hoàn thành câu: „Tôi thích ăn kem hơn bánh ngọt.“ (ngăn cách bởi dấu /): Ich esse [1] Eis [2] Kuchen.",
                "options": null,
                "correct_answer": "lieber / als",
                "explanation": "Để diễn tả sở thích ăn/uống món gì hơn món gì ('thích ... hơn'), ta dùng dạng so sánh hơn (Komparativ) của trạng từ 'gern' là 'lieber' đi kèm liên từ 'als' -> 'Ich esse lieber Eis als Kuchen.'",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi thích ăn kem hơn bánh ngọt.",
                        "accepted_answers": [
                                "lieber / als",
                                "lieber/als",
                                "lieber als",
                                "Lieber / als",
                                "Lieber als"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 51: Điền 2 từ để hoàn thành câu: „Anna nấu ăn giỏi (ngon) hơn anh trai của cô ấy.“ (ngăn cách bởi dấu /): Anna kocht [1] [2] ihr Bruder.",
                "options": null,
                "correct_answer": "besser / als",
                "explanation": "Khi nói về chất lượng hoặc kỹ năng làm việc gì tốt/giỏi hơn ('gut kochen'), ta dùng dạng so sánh hơn bất quy tắc của 'gut' là 'besser' kết hợp với liên từ 'als' -> 'besser als'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Anna nấu ăn giỏi (ngon) hơn anh trai của cô ấy.",
                        "accepted_answers": [
                                "besser / als",
                                "besser/als",
                                "besser als",
                                "Besser / als",
                                "Besser als",
                                "leckerer / als",
                                "leckerer/als",
                                "leckerer als",
                                "Leckerer / als",
                                "Leckerer als"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 52: Điền 2 từ để hoàn thành câu: „Tôi thích ăn cá nhất.“ (ngăn cách bởi dấu /): [1] [2] esse ich Fisch.",
                "options": null,
                "correct_answer": "Am / liebsten",
                "explanation": "Dạng so sánh nhất (Superlativ) của 'gern' để chỉ sở thích cao nhất là 'am liebsten'. Khi đưa cụm 'Am liebsten' lên đầu câu (Vị trí 1), động từ chia 'esse' đứng ở Vị trí 2 và chủ ngữ 'ich' đảo ra Vị trí 3 -> „Am liebsten esse ich Fisch.“",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi thích ăn cá nhất.",
                        "accepted_answers": [
                                "Am / liebsten",
                                "am / liebsten",
                                "am/liebsten",
                                "Am/liebsten",
                                "Am liebsten",
                                "am liebsten"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 53: Điền 2 từ để hoàn thành câu: „Một ký táo giá 2,40 euro. Hai ký giá 4,80 euro.“ (ngăn cách bởi dấu /): Ein Kilo Äpfel [1] 2,40 €. Zwei Kilo [2] 4,80 €.",
                "options": null,
                "correct_answer": "kostet / kosten",
                "explanation": "Động từ chỉ giá cả là 'kosten' (có giá). Ở câu đầu, chủ ngữ 'Ein Kilo Äpfel' có trung tâm là đơn vị đo số ít ('ein Kilo') nên động từ chia ngôi thứ 3 số ít là 'kostet'. Ở câu sau, dù danh từ đơn vị đo 'Kilo' giữ nguyên không thêm đuôi số nhiều sau số đếm 'zwei', nhưng cụm 'Zwei Kilo' mang nghĩa số nhiều (2 ký) nên động từ chia ở ngôi thứ 3 số nhiều là 'kosten'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Một ký táo giá 2,40 euro. Hai ký giá 4,80 euro.",
                        "accepted_answers": [
                                "kostet / kosten",
                                "kostet/kosten",
                                "kostet kosten",
                                "Kostet / kosten",
                                "Kostet kosten"
                        ]
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 54: Điền 2 từ để hoàn thành câu: „Hôm qua tôi đã mua rau củ ở chợ và đã nếm thử hoa quả.“ (ngăn cách bởi dấu /): Gestern habe ich auf dem Markt Gemüse [1] und Obst [2].",
                "options": null,
                "correct_answer": "gekauft / probiert",
                "explanation": "Trạng từ 'Gestern' (hôm qua) và trợ động từ 'habe' ở Vị trí 2 cho biết câu dùng thì quá khứ hoàn thành (Perfekt), nên vị trí [1] và [2] ở cuối câu cần điền dạng Partizip II: 'kaufen' (mua) là động từ có quy tắc -> 'gekauft' (ge- + kauf + -t); 'probieren' (nếm thử) có đuôi '-ieren' nên không thêm tiền tố 'ge-' -> 'probiert'.",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Hôm qua tôi đã mua rau củ ở chợ và đã nếm thử hoa quả.",
                        "accepted_answers": [
                                "gekauft / probiert",
                                "gekauft/probiert",
                                "gekauft probiert",
                                "Gekauft / probiert",
                                "Gekauft probiert",
                                "eingekauft / probiert",
                                "eingekauft/probiert",
                                "eingekauft probiert",
                                "Eingekauft / probiert",
                                "Eingekauft probiert"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 55: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Welches",
                "explanation": "'das Obst' (hoa quả/trái cây) là danh từ giống trung, đóng vai trò tân ngữ trực tiếp (Akkusativ) của động từ 'kaufst'. Với giống trung (das), từ hỏi 'welch-' luôn nhận đuôi '-es' -> „Welches Obst kaufst du am liebsten?“.",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Welches Obst kaufst du am liebsten?",
                        "display_sentence": "___ Obst kaufst du am liebsten?",
                        "hint_vi": "Bạn thích mua loại hoa quả nào nhất?",
                        "translation": "Bạn thích mua loại hoa quả nào nhất?",
                        "accepted_answers": [
                                "Welches",
                                "welches"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 56: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "zwei",
                "explanation": "Mức giá 2,90 € trong tiếng Đức được đọc là 'zwei Euro neunzig' (Số Euro + 'Euro' + Số Cent, không đọc dấu phẩy Komma).",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Ein Kilo Birnen kostet zwei Euro neunzig.",
                        "display_sentence": "Ein Kilo Birnen kostet ___ Euro neunzig.",
                        "hint_vi": "Một ký lê giá hai euro chín mươi (2,90 €).",
                        "translation": "Một ký lê giá hai euro chín mươi (2,90 €).",
                        "accepted_answers": [
                                "zwei",
                                "2"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 57: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "mehr",
                "explanation": "Trong câu có cấu trúc so sánh hơn với 'als ich' (hơn tôi), kết hợp với danh từ 'Gemüse' -> dùng dạng so sánh hơn (Komparativ) bất quy tắc của 'viel' là 'mehr'.",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Meine Schwester isst mehr Gemüse als ich.",
                        "display_sentence": "Meine Schwester isst ___ Gemüse als ich.",
                        "hint_vi": "Chị/em gái tôi ăn rau củ nhiều hơn tôi.",
                        "translation": "Chị/em gái tôi ăn rau củ nhiều hơn tôi.",
                        "accepted_answers": [
                                "mehr",
                                "Mehr"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 58: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "besser",
                "explanation": "Trong câu có liên từ 'als' (hơn) dùng để so sánh chất lượng bánh mì ở hai nơi -> dùng dạng so sánh hơn (Komparativ) bất quy tắc của 'gut' là 'besser'.",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Das Brot beim Bäcker ist besser als im Supermarkt.",
                        "display_sentence": "Das Brot beim Bäcker ist ___ als im Supermarkt.",
                        "hint_vi": "Bánh mì ở tiệm bánh ngon hơn ở siêu thị.",
                        "translation": "Bánh mì ở tiệm bánh ngon hơn ở siêu thị.",
                        "accepted_answers": [
                                "besser",
                                "Besser"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 59: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Müsli",
                "explanation": "'das Müsli' là món ngũ cốc ăn sáng. Khi nói chung về thực phẩm ăn trong bữa ('esse ich Müsli mit Milch'), danh từ chỉ thức ăn không cần dùng mạo từ.",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Zum Frühstück esse ich Müsli mit Milch.",
                        "display_sentence": "Zum Frühstück esse ich ___ mit Milch.",
                        "hint_vi": "Vào bữa sáng tôi ăn ngũ cốc với sữa.",
                        "translation": "Vào bữa sáng tôi ăn ngũ cốc với sữa.",
                        "accepted_answers": [
                                "Müsli",
                                "müsli",
                                "Muesli",
                                "muesli"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 60: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "hätte",
                "explanation": "Để gọi món hoặc hỏi mua hàng một cách lịch sự trong tiếng Đức, ta dùng cấu trúc cố định „Ich hätte gern + [Món hàng ở Akkusativ]“ (Tôi muốn lấy/xin mua...).",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Was darf es sein? Ich hätte gern zwei Kilo Äpfel.",
                        "display_sentence": "Was darf es sein? Ich ___ gern zwei Kilo Äpfel.",
                        "hint_vi": "Quý khách muốn mua gì ạ? — Cho tôi lấy hai ký táo.",
                        "translation": "Quý khách muốn mua gì ạ? — Cho tôi lấy hai ký táo.",
                        "accepted_answers": [
                                "hätte",
                                "haette",
                                "Hätte",
                                "Haette"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 61: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "achtzig",
                "explanation": "Khi đọc giá tiền lẻ bằng tiếng Đức, phần xu (80 Cent) được đọc ngay sau từ 'Euro' là 'achtzig' -> 9,80 € đọc là 'neun Euro achtzig'.",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Das macht zusammen neun Euro achtzig.",
                        "display_sentence": "Das macht zusammen neun Euro ___.",
                        "hint_vi": "Tổng cộng là chín euro tám mươi (9,80 €).",
                        "translation": "Tổng cộng là chín euro tám mươi (9,80 €).",
                        "accepted_answers": [
                                "achtzig",
                                "80"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 62: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "gekocht",
                "explanation": "Trạng từ 'Gestern' (hôm qua) và trợ động từ 'haben' ở Vị trí 2 cho biết câu ở thì quá khứ hoàn thành (Perfekt). Vị trí cuối câu điền Partizip II của động từ có quy tắc 'kochen' (nấu) là 'gekocht' (ge- + koch + -t).",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Gestern haben wir Nudeln gekocht.",
                        "display_sentence": "Gestern haben wir Nudeln ___.",
                        "hint_vi": "Hôm qua chúng tôi đã nấu mì.",
                        "translation": "Hôm qua chúng tôi đã nấu mì.",
                        "accepted_answers": [
                                "gekocht",
                                "Gekocht"
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 63: Dịch câu hỏi sau sang tiếng Đức: „Bạn muốn mua chiếc bánh ngọt nào?“",
                "options": null,
                "correct_answer": "Welchen Kuchen möchtest du kaufen?",
                "explanation": "'der Kuchen' là tân ngữ -> Akkusativ -> 'Welchen Kuchen'; 'möchten' ở vị trí 2, động từ nguyên mẫu 'kaufen' ở cuối câu. -> Đáp án: \"Welchen Kuchen möchtest du kaufen?\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Bạn muốn mua chiếc bánh ngọt nào?",
                        "accepted_answers": [
                                "Welchen Kuchen möchtest du kaufen?",
                                "Welchen Kuchen möchten Sie kaufen?",
                                "Welchen Kuchen möchtet ihr kaufen?"
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 64: Dịch câu sau sang tiếng Đức: „Quả cam rẻ hơn quả dứa.“",
                "options": null,
                "correct_answer": "Die Orange ist billiger als die Ananas.",
                "explanation": "'die Orange' và 'die Ananas' đều mang giống cái; so sánh hơn dùng 'billiger als'. -> Đáp án: \"Die Orange ist billiger als die Ananas.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Quả cam rẻ hơn quả dứa.",
                        "accepted_answers": [
                                "Die Orange ist billiger als die Ananas."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 65: Dịch câu sau sang tiếng Đức: „Tôi thích ăn cá hơn thịt.“",
                "options": null,
                "correct_answer": "Ich esse lieber Fisch als Fleisch.",
                "explanation": "Cấu trúc so sánh sở thích 'lieber … als' (Komparativ của 'gern'). -> Đáp án: \"Ich esse lieber Fisch als Fleisch.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Tôi thích ăn cá hơn thịt.",
                        "accepted_answers": [
                                "Ich esse lieber Fisch als Fleisch.",
                                "Ich esse Fisch lieber als Fleisch.",
                                "Lieber esse ich Fisch als Fleisch."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 66: Dịch câu sau sang tiếng Đức: „Trong gia đình tôi, bố nấu ăn ngon nhất.“",
                "options": null,
                "correct_answer": "In meiner Familie kocht mein Vater am besten.",
                "explanation": "Superlativ của 'gut' là 'am besten'; 'in meiner Familie' là trạng ngữ nơi chốn (Dativ). -> Đáp án: \"In meiner Familie kocht mein Vater am besten.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Trong gia đình tôi, bố nấu ăn ngon nhất.",
                        "accepted_answers": [
                                "In meiner Familie kocht mein Vater am besten.",
                                "Mein Vater kocht in meiner Familie am besten."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 67: Dịch câu hỏi sau sang tiếng Đức: „Hai lít sữa giá bao nhiêu?“",
                "options": null,
                "correct_answer": "Wie viel kosten zwei Liter Milch?",
                "explanation": "'zwei Liter' là số nhiều -> dùng 'kosten'; 'Liter' giữ nguyên số ít sau số đếm. -> Đáp án: \"Wie viel kosten zwei Liter Milch?\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hai lít sữa giá bao nhiêu?",
                        "accepted_answers": [
                                "Wie viel kosten zwei Liter Milch?",
                                "Was kosten zwei Liter Milch?"
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 68: Dịch câu sau sang tiếng Đức (Perfekt): „Hôm qua tôi đã nấu mì và ăn salad.“",
                "options": null,
                "correct_answer": "Gestern habe ich Nudeln gekocht und Salat gegessen.",
                "explanation": "'kochen -> gekocht', 'essen -> gegessen'; cả 2 đều dùng trợ động từ 'haben' nên 'habe' chỉ cần xuất hiện 1 lần. -> Đáp án: \"Gestern habe ich Nudeln gekocht und Salat gegessen.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hôm qua tôi đã nấu mì và ăn salad.",
                        "accepted_answers": [
                                "Gestern habe ich Nudeln gekocht und Salat gegessen.",
                                "Ich habe gestern Nudeln gekocht und Salat gegessen.",
                                "Gestern habe ich Nudeln gekocht und habe Salat gegessen."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 69: Dịch câu sau sang tiếng Việt: „Welche Äpfel sind süß? — Die Äpfel von meiner Oma.“",
                "options": null,
                "correct_answer": "Những quả táo nào ngọt? — Những quả táo của bà tôi.",
                "explanation": "'Welche Äpfel ...?' là câu hỏi số nhiều ('những quả táo nào ...?'); trả lời bằng cấu trúc sở hữu 'Die Äpfel von meiner Oma' (những quả táo của bà tôi).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Những quả táo nào ngọt? — Những quả táo của bà tôi.",
                        "accepted_answers": [
                                "Những quả táo nào ngọt? — Những quả táo của bà tôi.",
                                "Những quả táo nào ngọt? - Những quả táo của bà tôi.",
                                "Những quả táo nào ngọt vậy? — Những quả táo của bà tôi.",
                                "Những quả táo nào ngọt vậy? - Những quả táo của bà tôi.",
                                "Quả táo nào ngọt? — Táo của bà tôi.",
                                "Quả táo nào ngọt? - Táo của bà tôi."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 70: Dịch câu sau sang tiếng Việt: „In Vietnam essen die Menschen mehr Reis als Brot.“",
                "options": null,
                "correct_answer": "Ở Việt Nam mọi người ăn gạo nhiều hơn bánh mì.",
                "explanation": "Cấu trúc so sánh hơn với 'mehr ... als' (nhiều hơn so với); 'die Menschen' = mọi người / người dân; 'Reis' = cơm / gạo.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Ở Việt Nam mọi người ăn gạo nhiều hơn bánh mì.",
                        "accepted_answers": [
                                "Ở Việt Nam mọi người ăn gạo nhiều hơn bánh mì.",
                                "Ở Việt Nam mọi người ăn cơm nhiều hơn bánh mì.",
                                "Ở Việt Nam người ta ăn cơm nhiều hơn bánh mì.",
                                "Ở Việt Nam người ta ăn gạo nhiều hơn bánh mì.",
                                "Ở Việt Nam người dân ăn cơm nhiều hơn bánh mì.",
                                "Ở Việt Nam người dân ăn gạo nhiều hơn bánh mì."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 71: Dịch câu sau sang tiếng Việt: „Am meisten kaufe ich Obst und Gemüse auf dem Markt.“",
                "options": null,
                "correct_answer": "Tôi mua nhiều nhất là hoa quả và rau củ ở chợ.",
                "explanation": "'Am meisten' (nhiều nhất) đứng đầu câu tạo đảo ngữ, động từ 'kaufe' ở vị trí thứ hai; 'Obst und Gemüse' = hoa quả và rau củ (trái cây và rau củ).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Tôi mua nhiều nhất là hoa quả và rau củ ở chợ.",
                        "accepted_answers": [
                                "Tôi mua nhiều nhất là hoa quả và rau củ ở chợ.",
                                "Tôi mua hoa quả và rau củ ở chợ nhiều nhất.",
                                "Tôi mua nhiều nhất là trái cây và rau củ ở chợ.",
                                "Tôi mua trái cây và rau củ ở chợ nhiều nhất.",
                                "Tôi hay mua hoa quả và rau củ ở chợ nhất.",
                                "Tôi hay mua trái cây và rau củ ở chợ nhất."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 72: Dịch câu sau sang tiếng Việt: „Meine Schwester trinkt lieber Saft als Cola, aber am liebsten trinkt sie Wasser.“",
                "options": null,
                "correct_answer": "Chị tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước lọc nhất.",
                "explanation": "Cấu trúc so sánh hơn 'lieber ... als' (thích ... hơn) và so sánh nhất 'am liebsten' (thích nhất); 'Saft' = nước ép; 'Cola' = cô-ca (coca); 'Wasser' = nước / nước lọc.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Chị tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước lọc nhất.",
                        "accepted_answers": [
                                "Chị tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước lọc nhất.",
                                "Chị tôi thích uống nước ép hơn coca, nhưng thích uống nước lọc nhất.",
                                "Chị tôi thích uống nước ép hơn cola, nhưng thích uống nước lọc nhất.",
                                "Chị gái tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước lọc nhất.",
                                "Chị gái tôi thích uống nước ép hơn coca, nhưng thích uống nước lọc nhất.",
                                "Chị gái tôi thích uống nước ép hơn cola, nhưng thích uống nước lọc nhất.",
                                "Em gái tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước lọc nhất.",
                                "Em gái tôi thích uống nước ép hơn coca, nhưng thích uống nước lọc nhất.",
                                "Em gái tôi thích uống nước ép hơn cola, nhưng thích uống nước lọc nhất.",
                                "Chị tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước nhất.",
                                "Chị tôi thích uống nước ép hơn coca, nhưng thích uống nước nhất.",
                                "Chị tôi thích uống nước ép hơn cola, nhưng thích uống nước nhất.",
                                "Chị tôi thích nước ép hơn cola, nhưng thích nhất là uống nước.",
                                "Chị tôi thích nước ép hơn coca, nhưng thích nhất là uống nước."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 73: Dịch đoạn hội thoại sau sang tiếng Việt: „Guten Tag, ich hätte gern ein Pfund Erdbeeren. — Gern. Sonst noch etwas? — Nein, danke. Was macht das?“",
                "options": null,
                "correct_answer": "Xin chào, tôi muốn lấy nửa ký dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?",
                "explanation": "'ein Pfund' = nửa ký (500g); 'Was macht das?' = 'tổng cộng bao nhiêu? / tất cả hết bao nhiêu?'; 'Sonst noch etwas?' = 'còn gì nữa không?'.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Xin chào, tôi muốn lấy nửa ký dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?",
                        "accepted_answers": [
                                "Xin chào, tôi muốn lấy nửa ký dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Xin chào, tôi muốn lấy nửa ký dâu tây. - Vâng. Ngài cần gì nữa không? - Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Xin chào, tôi muốn lấy nửa cân dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Xin chào, tôi muốn lấy nửa cân dâu tây. - Vâng. Ngài cần gì nữa không? - Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Xin chào, tôi muốn lấy 500g dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Xin chào, tôi muốn lấy 500g dâu tây. - Vâng. Ngài cần gì nữa không? - Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Xin chào, tôi muốn lấy 500 gram dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?",
                                "Chào bạn, tôi muốn lấy nửa ký dâu tây. — Vâng. Bạn cần gì nữa không? — Không, cảm ơn. Hết bao nhiêu vậy?",
                                "Chào bạn, tôi muốn lấy nửa ký dâu tây. - Vâng. Bạn cần gì nữa không? - Không, cảm ơn. Hết bao nhiêu vậy?",
                                "Chào bạn, tôi muốn lấy nửa cân dâu tây. — Vâng. Bạn cần gì nữa không? — Không, cảm ơn. Hết bao nhiêu vậy?",
                                "Chào bạn, tôi muốn lấy 500g dâu tây. — Vâng. Bạn cần gì nữa không? — Không, cảm ơn. Hết bao nhiêu vậy?"
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 74: Dịch câu sau sang tiếng Việt: „Gestern hat Herr Bauer im Supermarkt zwei Kilo Kartoffeln und eine Flasche Milch gekauft.“",
                "options": null,
                "correct_answer": "Hôm qua ông Bauer đã mua hai ký khoai tây và một chai sữa ở siêu thị.",
                "explanation": "Thì Perfekt 'hat ... gekauft'; đơn vị đo 'Kilo' giữ nguyên số ít sau số đếm 'zwei' (hai ký / 2 ký); 'eine Flasche Milch' = một chai sữa (1 chai sữa).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hôm qua ông Bauer đã mua hai ký khoai tây và một chai sữa ở siêu thị.",
                        "accepted_answers": [
                                "Hôm qua ông Bauer đã mua hai ký khoai tây và một chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2 ký khoai tây và 1 chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2 ký khoai tây và một chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua hai ký khoai tây và 1 chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua hai cân khoai tây và một chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2 cân khoai tây và 1 chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2 cân khoai tây và một chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua hai cân khoai tây và 1 chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2kg khoai tây và 1 chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2 kg khoai tây và 1 chai sữa ở siêu thị.",
                                "Hôm qua ông Bauer đã mua 2kg khoai tây và một chai sữa ở siêu thị.",
                                "Hôm qua ở siêu thị ông Bauer đã mua hai ký khoai tây và một chai sữa.",
                                "Hôm qua ở siêu thị ông Bauer đã mua 2 ký khoai tây và 1 chai sữa.",
                                "Hôm qua ở siêu thị ông Bauer đã mua 2 cân khoai tây và 1 chai sữa."
                        ]
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 75: Sắp xếp các từ xáo trộn thành câu hoàn chỉnh:",
                "options": null,
                "correct_answer": "Welchen Fisch nimmst du?",
                "explanation": "Cụm từ hỏi 'Welchen Fisch' ở vị trí ①, động từ 'nimmst' ở vị trí ②, chủ ngữ 'du' ở vị trí ③. -> Đáp án: \"Welchen Fisch nimmst du?\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "nimmst",
                                "Welchen",
                                "du",
                                "Fisch"
                        ],
                        "translation": "Bạn lấy con cá nào?",
                        "accepted_answers": [
                                "Welchen Fisch nimmst du?"
                        ]
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 76: Sắp xếp các từ xáo trộn thành câu hoàn chỉnh:",
                "options": null,
                "correct_answer": "Ich esse lieber Reis als Nudeln.",
                "explanation": "Cấu trúc so sánh sở thích: 'Ich esse lieber Reis als Nudeln.' (hoặc đảo ngữ 'Lieber esse ich Reis als Nudeln.').",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "Reis",
                                "esse",
                                "ich",
                                "lieber",
                                "als",
                                "Nudeln"
                        ],
                        "translation": "Tôi thích ăn cơm hơn mì.",
                        "accepted_answers": [
                                "Ich esse lieber Reis als Nudeln.",
                                "Ich esse Reis lieber als Nudeln.",
                                "Lieber esse ich Reis als Nudeln."
                        ]
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 77: Sắp xếp các từ xáo trộn thành câu hoàn chỉnh:",
                "options": null,
                "correct_answer": "Am meisten kauft meine Mutter Obst.",
                "explanation": "Nếu 'Am meisten' đứng đầu câu thì động từ 'kauft' ở vị trí ②, chủ ngữ 'meine Mutter' ở vị trí ③. -> Đáp án: \"Am meisten kauft meine Mutter Obst.\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "Am meisten",
                                "kauft",
                                "meine Mutter",
                                "Obst"
                        ],
                        "translation": "Mẹ tôi mua hoa quả nhiều nhất.",
                        "accepted_answers": [
                                "Am meisten kauft meine Mutter Obst.",
                                "Meine Mutter kauft am meisten Obst."
                        ]
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 78: Sắp xếp các từ xáo trộn thành câu hoàn chỉnh:",
                "options": null,
                "correct_answer": "Wie viel kostet der Käse?",
                "explanation": "'Wie viel' ở vị trí ①, 'kostet' ở vị trí ② (chủ ngữ số ít 'der Käse'). -> Đáp án: \"Wie viel kostet der Käse?\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "kostet",
                                "Wie viel",
                                "der Käse"
                        ],
                        "translation": "Phô mai giá bao nhiêu?",
                        "accepted_answers": [
                                "Wie viel kostet der Käse?"
                        ]
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 79: Sắp xếp các từ xáo trộn thành câu hoàn chỉnh:",
                "options": null,
                "correct_answer": "Die Birnen sind billiger als die Erdbeeren.",
                "explanation": "Cấu trúc so sánh hơn: 'Die Birnen sind billiger als die Erdbeeren.'",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "billiger",
                                "die Birnen",
                                "als",
                                "sind",
                                "die Erdbeeren"
                        ],
                        "translation": "Những quả lê rẻ hơn những quả dâu tây.",
                        "accepted_answers": [
                                "Die Birnen sind billiger als die Erdbeeren."
                        ]
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 80: Bấm chọn mạo từ (der / die / das) chính xác cho 4 danh từ thực phẩm dưới đây:",
                "options": null,
                "correct_answer": "der / die / das / der",
                "explanation": "'der Käse' (giống đực, ngoại lệ đuôi -e), 'die Butter' (giống cái), 'das Brot' (giống trung), 'der Fisch' (giống đực). -> Đáp án: \"der / die / das / der\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "der Käse, die Butter, das Brot, der Fisch",
                        "items": [
                                {
                                        "noun": "Käse",
                                        "meaning_vi": "phô mai",
                                        "article": "der",
                                        "plural": "die Käse",
                                        "reason_vi": "Ngoại lệ đuôi -e nhưng mang giống đực (der)"
                                },
                                {
                                        "noun": "Butter",
                                        "meaning_vi": "bơ",
                                        "article": "die",
                                        "plural": "nur Singular",
                                        "reason_vi": "Danh từ chỉ chất béo/bơ sữa mang giống cái (die)"
                                },
                                {
                                        "noun": "Brot",
                                        "meaning_vi": "bánh mì",
                                        "article": "das",
                                        "plural": "die Brote",
                                        "reason_vi": "Danh từ chỉ lương thực mang giống trung (das)"
                                },
                                {
                                        "noun": "Fisch",
                                        "meaning_vi": "cá",
                                        "article": "der",
                                        "plural": "die Fische",
                                        "reason_vi": "Danh từ giống đực (der)"
                                }
                        ]
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 81: Bấm chọn mạo từ (der / die / das) chính xác cho 4 danh từ thực phẩm dưới đây:",
                "options": null,
                "correct_answer": "die / das / der / die",
                "explanation": "'die Banane' (đuôi -e -> giống cái), 'das Fleisch' (giống trung), 'der Apfel' (giống đực), 'die Zwiebel' (giống cái). -> Đáp án: \"die / das / der / die\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "die Banane, das Fleisch, der Apfel, die Zwiebel",
                        "items": [
                                {
                                        "noun": "Banane",
                                        "meaning_vi": "quả chuối",
                                        "article": "die",
                                        "plural": "die Bananen",
                                        "reason_vi": "Hoa quả đuôi -e mang giống cái (die)"
                                },
                                {
                                        "noun": "Fleisch",
                                        "meaning_vi": "thịt",
                                        "article": "das",
                                        "plural": "nur Singular",
                                        "reason_vi": "Danh từ không đếm được chỉ thực phẩm mang giống trung (das)"
                                },
                                {
                                        "noun": "Apfel",
                                        "meaning_vi": "quả táo",
                                        "article": "der",
                                        "plural": "die Äpfel",
                                        "reason_vi": "Danh từ giống đực (der)"
                                },
                                {
                                        "noun": "Zwiebel",
                                        "meaning_vi": "hành tây",
                                        "article": "die",
                                        "plural": "die Zwiebeln",
                                        "reason_vi": "Danh từ giống cái (die)"
                                }
                        ]
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 82: Bấm chọn mạo từ (der / die / das) chính xác cho 4 danh từ thực phẩm dưới đây:",
                "options": null,
                "correct_answer": "das / die / der / der",
                "explanation": "'das Ei' (giống trung), 'die Nudel' (giống cái), 'der Salat' (giống đực), 'der Reis' (chuẩn từ điển: giống đực). -> Đáp án: \"das / die / der / der\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "das Ei, die Nudel, der Salat, der Reis",
                        "items": [
                                {
                                        "noun": "Ei",
                                        "meaning_vi": "quả trứng",
                                        "article": "das",
                                        "plural": "die Eier",
                                        "reason_vi": "Danh từ giống trung (das)"
                                },
                                {
                                        "noun": "Nudel",
                                        "meaning_vi": "sợi mì",
                                        "article": "die",
                                        "plural": "die Nudeln",
                                        "reason_vi": "Danh từ giống cái (die)"
                                },
                                {
                                        "noun": "Salat",
                                        "meaning_vi": "xà lách, salad",
                                        "article": "der",
                                        "plural": "die Salate",
                                        "reason_vi": "Danh từ giống đực (der)"
                                },
                                {
                                        "noun": "Reis",
                                        "meaning_vi": "gạo, cơm",
                                        "article": "der",
                                        "plural": "nur Singular",
                                        "reason_vi": "Chuẩn từ điển Đức: der Reis (giống đực, chỉ số ít)"
                                }
                        ]
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 83: Bấm chọn mạo từ (der / die / das) chính xác cho 4 danh từ thực phẩm dưới đây:",
                "options": null,
                "correct_answer": "die / der / das / die",
                "explanation": "'die Möhre' (giống cái), 'der Schinken' (giống đực), 'das Gemüse' (giống trung), 'die Orange' (giống cái). -> Đáp án: \"die / der / das / die\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "die Möhre, der Schinken, das Gemüse, die Orange",
                        "items": [
                                {
                                        "noun": "Möhre",
                                        "meaning_vi": "cà rốt",
                                        "article": "die",
                                        "plural": "die Möhren",
                                        "reason_vi": "Rau củ đuôi -e mang giống cái (die)"
                                },
                                {
                                        "noun": "Schinken",
                                        "meaning_vi": "giăm bông",
                                        "article": "der",
                                        "plural": "die Schinken",
                                        "reason_vi": "Danh từ giống đực (der)"
                                },
                                {
                                        "noun": "Gemüse",
                                        "meaning_vi": "rau củ",
                                        "article": "das",
                                        "plural": "nur Singular",
                                        "reason_vi": "Ngoại lệ: das Gemüse mang giống trung (das)"
                                },
                                {
                                        "noun": "Orange",
                                        "meaning_vi": "quả cam",
                                        "article": "die",
                                        "plural": "die Orangen",
                                        "reason_vi": "Hoa quả đuôi -e mang giống cái (die)"
                                }
                        ]
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 84: Tìm lỗi sai trong câu sau và gõ lại cả câu đúng: „Welcher Käse möchten Sie kaufen?“",
                "options": null,
                "correct_answer": "Welchen Käse möchten Sie kaufen?",
                "explanation": "Lỗi cách của từ hỏi 'welch-': 'Käse' là tân ngữ của 'möchten … kaufen' -> Akkusativ -> 'Welchen', không phải 'Welcher'. -> Đáp án: \"Welchen Käse möchten Sie kaufen?\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Welcher Käse möchten Sie kaufen?",
                        "translation": "Ngài muốn mua loại phô mai nào?",
                        "accepted_answers": [
                                "Welchen Käse möchten Sie kaufen?"
                        ]
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 85: Tìm lỗi sai trong câu sau và gõ lại cả câu đúng: „Ich esse mehr Kartoffeln wie Reis.“",
                "options": null,
                "correct_answer": "Ich esse mehr Kartoffeln als Reis.",
                "explanation": "Lỗi dùng từ trong so sánh hơn: so sánh hơn dùng 'als', không dùng 'wie' -> 'mehr Kartoffeln als Reis'. -> Đáp án: \"Ich esse mehr Kartoffeln als Reis.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Ich esse mehr Kartoffeln wie Reis.",
                        "translation": "Tôi ăn khoai tây nhiều hơn cơm.",
                        "accepted_answers": [
                                "Ich esse mehr Kartoffeln als Reis."
                        ]
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 86: Tìm lỗi sai trong câu sau và gõ lại cả câu đúng: „Der Fisch ist gutter als das Fleisch.“",
                "options": null,
                "correct_answer": "Der Fisch ist besser als das Fleisch.",
                "explanation": "Lỗi biến đổi tính từ so sánh hơn bất quy tắc: Komparativ của 'gut' là 'besser', không phải 'gutter'. -> Đáp án: \"Der Fisch ist besser als das Fleisch.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Der Fisch ist gutter als das Fleisch.",
                        "translation": "Cá ngon hơn thịt.",
                        "accepted_answers": [
                                "Der Fisch ist besser als das Fleisch."
                        ]
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 87: Tìm lỗi sai trong câu sau và gõ lại cả câu đúng: „Am liebsten ich trinke Milch.“",
                "options": null,
                "correct_answer": "Am liebsten trinke ich Milch.",
                "explanation": "Lỗi vị trí động từ: khi cụm so sánh nhất 'Am liebsten' đứng đầu câu (vị trí ①), động từ chia 'trinke' bắt buộc phải ở vị trí ② rồi mới đến chủ ngữ 'ich'. -> Đáp án: \"Am liebsten trinke ich Milch.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Am liebsten ich trinke Milch.",
                        "translation": "Tôi thích uống sữa nhất.",
                        "accepted_answers": [
                                "Am liebsten trinke ich Milch."
                        ]
                }
        },
        {
                "type": "viet_lai_so_sanh",
                "question": "Câu 88: Viết lại câu sau thành so sánh hơn với đối tượng 'der Tee': „Der Kaffee ist heiß.“",
                "options": null,
                "correct_answer": "Der Kaffee ist heißer als der Tee.",
                "explanation": "'heiß' tạo Komparativ thêm '-er' (giữ nguyên 'ß') -> 'heißer', thêm 'als der Tee' -> „Der Kaffee ist heißer als der Tee.“",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Der Kaffee ist heiß.",
                        "instruction_vi": "Viết lại thành so sánh hơn với đối tượng der Tee.",
                        "translation": "Cà phê nóng hơn trà.",
                        "accepted_answers": [
                                "Der Kaffee ist heißer als der Tee."
                        ]
                }
        },
        {
                "type": "viet_lai_so_sanh",
                "question": "Câu 89: Viết lại câu sau thành so sánh hơn với đối tượng 'Obst': „Meine Schwester isst gern Gemüse.“",
                "options": null,
                "correct_answer": "Meine Schwester isst lieber Gemüse als Obst.",
                "explanation": "Komparativ của 'gern' là 'lieber', thêm 'als Obst' -> „Meine Schwester isst lieber Gemüse als Obst.“",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Meine Schwester isst gern Gemüse.",
                        "instruction_vi": "Viết lại thành so sánh hơn với đối tượng Obst.",
                        "translation": "Chị tôi thích ăn rau củ hơn hoa quả.",
                        "accepted_answers": [
                                "Meine Schwester isst lieber Gemüse als Obst.",
                                "Meine Schwester isst Gemüse lieber als Obst."
                        ]
                }
        },
        {
                "type": "viet_lai_so_sanh",
                "question": "Câu 90: Viết lại câu sau thành so sánh nhất (không thêm đối tượng): „Meine Mutter kocht gut.“",
                "options": null,
                "correct_answer": "Meine Mutter kocht am besten.",
                "explanation": "Superlativ của 'gut' là 'am besten' (bất quy tắc) -> „Meine Mutter kocht am besten.“",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Meine Mutter kocht gut.",
                        "instruction_vi": "Viết lại thành so sánh nhất (không thêm đối tượng).",
                        "translation": "Mẹ tôi nấu ăn ngon nhất.",
                        "accepted_answers": [
                                "Meine Mutter kocht am besten."
                        ]
                }
        },
        {
                "type": "viet_lai_so_sanh",
                "question": "Câu 91: Viết lại câu sau thành so sánh hơn với đối tượng 'Saft': „Wir trinken viel Wasser.“",
                "options": null,
                "correct_answer": "Wir trinken mehr Wasser als Saft.",
                "explanation": "Komparativ của 'viel' là 'mehr', thêm 'als Saft' -> „Wir trinken mehr Wasser als Saft.“",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Wir trinken viel Wasser.",
                        "instruction_vi": "Viết lại thành so sánh hơn với đối tượng Saft.",
                        "translation": "Chúng tôi uống nước lọc nhiều hơn nước ép.",
                        "accepted_answers": [
                                "Wir trinken mehr Wasser als Saft."
                        ]
                }
        },
        {
                "type": "dung_sai",
                "question": "Câu 92: Đọc đoạn văn sau và xác định mệnh đề là Richtig (Đúng) hay Falsch (Sai): „Die Möhren sind billiger als die Tomaten.“",
                "options": [
                        "Richtig",
                        "Falsch"
                ],
                "correct_answer": "Richtig",
                "explanation": "Đoạn văn viết: „Die Tomaten kosten 2,50 Euro das Kilo, die Möhren nur 1,20 Euro.“ — 1,20 € < 2,50 € nên cà rốt rẻ hơn cà chua -> ĐÚNG (Richtig).",
                "exp_reward": 15,
                "extra_data": {
                        "reading_text": "Frau Becker geht jeden Samstag auf den Markt. Sie kauft dort frisches Gemüse und Obst. Die Tomaten kosten zwei Euro fünfzig das Kilo, die Möhren nur ein Euro zwanzig. Sie nimmt zwei Kilo Tomaten und ein Kilo Möhren. Am liebsten isst sie Erdbeeren, aber im Winter gibt es keine.",
                        "reading_translation_vi": "Bà Becker đi chợ vào mỗi thứ Bảy. Bà mua ở đó rau củ và hoa quả tươi. Cà chua giá hai euro năm mươi một ký, cà rốt chỉ một euro hai mươi. Bà lấy hai ký cà chua và một ký cà rốt. Bà thích ăn dâu tây nhất, nhưng vào mùa đông không có.",
                        "statement": "Die Möhren sind billiger als die Tomaten.",
                        "statement_vi": "Cà rốt rẻ hơn cà chua.",
                        "translation": "Cà rốt rẻ hơn cà chua."
                }
        },
        {
                "type": "dung_sai",
                "question": "Câu 93: Đọc đoạn văn sau và xác định mệnh đề là Richtig (Đúng) hay Falsch (Sai): „Frau Becker kauft zwei Kilo Möhren.“",
                "options": [
                        "Richtig",
                        "Falsch"
                ],
                "correct_answer": "Falsch",
                "explanation": "Đoạn văn viết: „Sie nimmt zwei Kilo Tomaten und ein Kilo Möhren.“ — bà mua 2 ký cà chua và 1 ký cà rốt (không phải 2 ký cà rốt) -> SAI (Falsch).",
                "exp_reward": 15,
                "extra_data": {
                        "reading_text": "Frau Becker geht jeden Samstag auf den Markt. Sie kauft dort frisches Gemüse und Obst. Die Tomaten kosten zwei Euro fünfzig das Kilo, die Möhren nur ein Euro zwanzig. Sie nimmt zwei Kilo Tomaten und ein Kilo Möhren. Am liebsten isst sie Erdbeeren, aber im Winter gibt es keine.",
                        "reading_translation_vi": "Bà Becker đi chợ vào mỗi thứ Bảy. Bà mua ở đó rau củ và hoa quả tươi. Cà chua giá hai euro năm mươi một ký, cà rốt chỉ một euro hai mươi. Bà lấy hai ký cà chua và một ký cà rốt. Bà thích ăn dâu tây nhất, nhưng vào mùa đông không có.",
                        "statement": "Frau Becker kauft zwei Kilo Möhren.",
                        "statement_vi": "Bà Becker mua hai ký cà rốt.",
                        "translation": "Bà Becker mua hai ký cà rốt."
                }
        },
        {
                "type": "dung_sai",
                "question": "Câu 94: Đọc đoạn văn sau và xác định mệnh đề là Richtig (Đúng) hay Falsch (Sai): „Tom isst zu Hause mehr Salat als im Restaurant.“",
                "options": [
                        "Richtig",
                        "Falsch"
                ],
                "correct_answer": "Falsch",
                "explanation": "Đoạn văn viết: „Im Restaurant isst er mehr Salat als zu Hause.“ — ở nhà hàng Tom ăn nhiều salad hơn ở nhà (không phải ở nhà ăn nhiều hơn) -> SAI (Falsch).",
                "exp_reward": 15,
                "extra_data": {
                        "reading_text": "Tom isst am liebsten Pizza. Zu Hause kocht er oft Nudeln. Im Restaurant isst er mehr Salat als zu Hause.",
                        "reading_translation_vi": "Tom thích ăn pizza nhất. Ở nhà anh ấy thường nấu mì. Ở nhà hàng anh ấy ăn salad nhiều hơn ở nhà.",
                        "statement": "Tom isst zu Hause mehr Salat als im Restaurant.",
                        "statement_vi": "Ở nhà Tom ăn salad nhiều hơn ở nhà hàng.",
                        "translation": "Ở nhà Tom ăn salad nhiều hơn ở nhà hàng."
                }
        },
        {
                "type": "hoi_thoai_sap_xep",
                "question": "Câu 95: Sắp xếp các lượt lời sau thành hội thoại mua sắm hợp lý tại quầy hoa quả (chọn theo thứ tự từ 1 đến 6):",
                "options": null,
                "correct_answer": "1, 2, 3, 4, 5, 6",
                "explanation": "Trình tự mua sắm chuẩn: Chào hỏi -> Gọi món -> Hỏi thêm -> Hỏi giá -> Báo tổng tiền -> Thanh toán đưa tiền. -> Đáp án: \"1, 2, 3, 4, 5, 6\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hội thoại mua sắm hoàn chỉnh tại quầy trái cây",
                        "correct_order": [
                                1,
                                2,
                                3,
                                4,
                                5,
                                6
                        ],
                        "lines": [
                                {
                                        "id": 1,
                                        "speaker": "Verkäufer",
                                        "text": "Guten Tag! Bitte schön?",
                                        "translation_vi": "Xin chào! Ngài cần gì ạ?"
                                },
                                {
                                        "id": 2,
                                        "speaker": "Kundin",
                                        "text": "Ich möchte ein Pfund Erdbeeren und zwei Bananen, bitte.",
                                        "translation_vi": "Tôi muốn nửa ký dâu tây và hai quả chuối, làm ơn."
                                },
                                {
                                        "id": 3,
                                        "speaker": "Verkäufer",
                                        "text": "Gern. Sonst noch etwas?",
                                        "translation_vi": "Vâng. Ngài cần gì nữa không ạ?"
                                },
                                {
                                        "id": 4,
                                        "speaker": "Kundin",
                                        "text": "Nein, danke. Was macht das?",
                                        "translation_vi": "Không, cảm ơn. Tổng cộng bao nhiêu?"
                                },
                                {
                                        "id": 5,
                                        "speaker": "Verkäufer",
                                        "text": "Das macht zusammen vier Euro fünfzig.",
                                        "translation_vi": "Tổng cộng là bốn euro năm mươi."
                                },
                                {
                                        "id": 6,
                                        "speaker": "Kundin",
                                        "text": "Hier sind fünf Euro. Stimmt so!",
                                        "translation_vi": "Đây là năm euro. Không cần thối!"
                                }
                        ]
                }
        },
        {
                "type": "hoi_thoai_sap_xep",
                "question": "Câu 96: Sắp xếp các lượt lời sau thành hội thoại hợp lý tại siêu thị (chọn theo thứ tự từ 1 đến 6):",
                "options": null,
                "correct_answer": "1, 2, 3, 4, 5, 6",
                "explanation": "Trình tự chuẩn: Hỏi vị trí -> Chỉ vị trí -> Hỏi giá -> Báo giá -> Quyết định số lượng -> Báo tổng tiền. -> Đáp án: \"1, 2, 3, 4, 5, 6\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hội thoại hỏi mua hàng tại siêu thị",
                        "correct_order": [
                                1,
                                2,
                                3,
                                4,
                                5,
                                6
                        ],
                        "lines": [
                                {
                                        "id": 1,
                                        "speaker": "Kunde",
                                        "text": "Entschuldigung, wo finde ich den Joghurt?",
                                        "translation_vi": "Xin lỗi, tôi tìm sữa chua ở đâu ạ?"
                                },
                                {
                                        "id": 2,
                                        "speaker": "Verkäufer",
                                        "text": "Der Joghurt steht dort hinten.",
                                        "translation_vi": "Sữa chua ở phía sau kia."
                                },
                                {
                                        "id": 3,
                                        "speaker": "Kunde",
                                        "text": "Danke. Und wie viel kostet die Milch?",
                                        "translation_vi": "Cảm ơn. Còn sữa giá bao nhiêu?"
                                },
                                {
                                        "id": 4,
                                        "speaker": "Verkäufer",
                                        "text": "Ein Liter Milch kostet ein Euro zehn.",
                                        "translation_vi": "Một lít sữa giá một euro mười."
                                },
                                {
                                        "id": 5,
                                        "speaker": "Kunde",
                                        "text": "Gut, dann nehme ich zwei Liter.",
                                        "translation_vi": "Tốt, vậy tôi lấy hai lít."
                                },
                                {
                                        "id": 6,
                                        "speaker": "Verkäufer",
                                        "text": "Das macht zwei Euro zwanzig.",
                                        "translation_vi": "Tổng cộng là hai euro hai mươi."
                                }
                        ]
                }
        },
        {
                "type": "hoi_thoai_sap_xep",
                "question": "Câu 97: Sắp xếp các lượt lời sau thành hội thoại gọi món tại nhà hàng (chọn theo thứ tự từ 1 đến 5):",
                "options": null,
                "correct_answer": "1, 2, 3, 4, 5",
                "explanation": "Trình tự nhà hàng: Hỏi đã gọi món chưa -> Xin gợi ý -> Người phục vụ gợi ý món -> Chọn món -> Xác nhận. -> Đáp án: \"1, 2, 3, 4, 5\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hội thoại gọi món tại nhà hàng",
                        "correct_order": [
                                1,
                                2,
                                3,
                                4,
                                5
                        ],
                        "lines": [
                                {
                                        "id": 1,
                                        "speaker": "Kellner",
                                        "text": "Guten Tag, haben Sie schon bestellt?",
                                        "translation_vi": "Xin chào, ngài đã gọi món chưa ạ?"
                                },
                                {
                                        "id": 2,
                                        "speaker": "Gast",
                                        "text": "Nein, noch nicht. Was empfehlen Sie?",
                                        "translation_vi": "Chưa. Ngài gợi ý món gì?"
                                },
                                {
                                        "id": 3,
                                        "speaker": "Kellner",
                                        "text": "Ich empfehle den Fisch mit Reis.",
                                        "translation_vi": "Tôi gợi ý món cá với cơm."
                                },
                                {
                                        "id": 4,
                                        "speaker": "Gast",
                                        "text": "Gut, dann nehme ich den Fisch und eine Flasche Wasser.",
                                        "translation_vi": "Tốt, vậy tôi lấy món cá và một chai nước."
                                },
                                {
                                        "id": 5,
                                        "speaker": "Kellner",
                                        "text": "Gern, das kommt gleich.",
                                        "translation_vi": "Vâng, có ngay ạ."
                                }
                        ]
                }
        },
        {
                "type": "nghe_gia_tien",
                "question": "Câu 98: Nghe phát âm câu tiếng Đức và nhập số tiền (dạng ví dụ: 4,85 hoặc 4.85):",
                "options": null,
                "correct_answer": "4,85",
                "explanation": "Giá tiền 'vier Euro fünfundachtzig' tương ứng với 4,85 € (485 Cent).",
                "exp_reward": 15,
                "extra_data": {
                        "audio_text": "Das macht zusammen vier Euro fünfundachtzig.",
                        "price_cents": 485,
                        "translation": "Tổng cộng là bốn euro tám mươi lăm.",
                        "accepted_answers": [
                                "4,85",
                                "4.85",
                                "4,85 €",
                                "4,85€",
                                "4,85 Euro"
                        ]
                }
        },
        {
                "type": "nghe_gia_tien",
                "question": "Câu 99: Nghe phát âm câu tiếng Đức và nhập số tiền (dạng ví dụ: 5,80 hoặc 5.80):",
                "options": null,
                "correct_answer": "5,80",
                "explanation": "Giá tiền 'fünf Euro achtzig' tương ứng với 5,80 € (580 Cent, 2 ký lê x 2,90 €).",
                "exp_reward": 15,
                "extra_data": {
                        "audio_text": "Zwei Kilo Birnen kosten fünf Euro achtzig.",
                        "price_cents": 580,
                        "translation": "Hai ký lê giá năm euro tám mươi.",
                        "accepted_answers": [
                                "5,80",
                                "5.80",
                                "5,80 €",
                                "5,80€",
                                "5,80 Euro"
                        ]
                }
        },
        {
                "type": "nghe_gia_tien",
                "question": "Câu 100: Nghe phát âm câu tiếng Đức và nhập số tiền (dạng ví dụ: 1,29 hoặc 1.29):",
                "options": null,
                "correct_answer": "1,29",
                "explanation": "Giá tiền 'ein Euro neunundzwanzig' tương ứng với 1,29 € (129 Cent).",
                "exp_reward": 15,
                "extra_data": {
                        "audio_text": "Die Dose Cola kostet ein Euro neunundzwanzig.",
                        "price_cents": 129,
                        "translation": "Lon cô-ca giá một euro hai mươi chín.",
                        "accepted_answers": [
                                "1,29",
                                "1.29",
                                "1,29 €",
                                "1,29€",
                                "1,29 Euro"
                        ]
                }
        }
]

    exercises_data = []
    for ex in exercises_raw:
        opts_str = json.dumps(ex["options"], ensure_ascii=False) if ex.get("options") else None
        extra_str = json.dumps(ex["extra_data"], ensure_ascii=False) if ex.get("extra_data") else None
        exercises_data.append((
            lesson_id,
            ex["type"],
            ex["question"],
            opts_str,
            ex["correct_answer"],
            ex["explanation"],
            ex["exp_reward"],
            extra_str
        ))

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises_data)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công Bài 10: 'Essen und Trinken' với đầy đủ 9 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 16 dạng!")

if __name__ == "__main__":
    seed_lesson_10()
