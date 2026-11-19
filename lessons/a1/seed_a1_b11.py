# -*- coding: utf-8 -*-
"""
Seed file Bài 11 (A1): "Kleidung und Wetter - Trang phục, Màu sắc ở Akkusativ, Đại từ chỉ định dies-, Thời tiết"
Vị trí A1: lesson_order = 12 (sau Bài 10)
Tích hợp đầy đủ 9 Học phần Lý thuyết + 6 Container Sơ đồ SVG + 50 Từ vựng + 100 Bài tập độc nhất (18 Dạng bài)
Chuẩn CEFR A1 và tuân thủ tuyệt đối Giao thức QA Zero-Bug & Quy tắc Color-Dativ separation
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

def seed_lesson_11():
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
    lesson_id = 25
    lesson_title = 'Bài 11: Kleidung - Die Farbe in Akkusativ - dies- (Đại từ chỉ định) - Wetter'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed font-sans">
        <!-- BANNER TỔNG QUAN BÀI 11 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Kleidung & Wetter • Akkusativ • dies- (Bài 11)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 120 phút • ⚡ 1800+ EXP • 🎯 100 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Bài 11: Kleidung - Die Farbe in Akkusativ - dies- (Đại từ chỉ định) - Wetter
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Chinh phục trọn bộ từ vựng trang phục (<code>der Mantel, die Jacke, das Kleid, die Schuhe...</code>) và 17 màu sắc; ghép tính từ chỉ màu vào trang phục ở Cách 4 <b>Akkusativ</b> theo công thức thần chú <b>„en – e – es – e“</b>; làm chủ đại từ chỉ định <b>dies- (dieser / diesen / diese / dieses)</b>; phân biệt rành mạch Akkusativ và Dativ với các động từ thời trang (<code>tragen, anziehen, gefallen, passen, stehen, gehören</code>); tự tin mô tả thời tiết (<code>Es regnet, Es ist sonnig / windig, Wie ist das Wetter bei dir?</code>) và giao tiếp mua sắm quần áo tại cửa hàng Đức.
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: TỪ VỰNG TRANG PHỤC (DIE KLEIDUNG) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">1</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Từ Vựng Trang Phục (Die Kleidung) Theo 3 Giống</h2>
                    <p class="text-xs text-slate-500">Quy tắc mạo từ der / die / das, dạng số nhiều chuẩn hóa và mẹo ghi nhớ</p>
                </div>
            </div>

            <!-- Bảng phân loại 3 giống -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                <!-- Giống đực (der) -->
                <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-2">
                    <div class="flex items-center justify-between font-bold text-blue-900 border-b border-blue-200/60 pb-1.5">
                        <span class="text-sm">🔵 Giống Đực (der)</span>
                        <span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 text-[11px]">Maskulinum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-800">
                        <li>• <b class="text-blue-950">der Stiefel</b> <i>(die Stiefel)</i>: bốt, ủng</li>
                        <li>• <b class="text-blue-950">der Mantel</b> <i>(die Mäntel)</i>: áo măng tô</li>
                        <li>• <b class="text-blue-950">der Pullover</b> <i>(die Pullover)</i>: áo len chui đầu</li>
                        <li>• <b class="text-blue-950">der Rock</b> <i>(die Röcke)</i>: chân váy</li>
                        <li>• <b class="text-blue-950">der Anzug</b> <i>(die Anzüge)</i>: bộ com lê</li>
                        <li>• <b class="text-blue-950">der Schuh</b> <i>(die Schuhe)</i>: giày</li>
                        <li>• <b class="text-blue-950">der Gürtel</b> <i>(die Gürtel)</i>: thắt lưng</li>
                        <li>• <b class="text-blue-950">der Hut</b> <i>(die Hüte)</i>: mũ có vành</li>
                        <li>• <b class="text-blue-950">der Handschuh</b> <i>(die Handschuhe)</i>: găng tay</li>
                        <li>• <b class="text-blue-950">der Schal</b> <i>(die Schals)</i>: khăn quàng</li>
                    </ul>
                </div>

                <!-- Giống cái (die) -->
                <div class="p-4 rounded-2xl bg-rose-50/60 border border-rose-200 space-y-2">
                    <div class="flex items-center justify-between font-bold text-rose-900 border-b border-rose-200/60 pb-1.5">
                        <span class="text-sm">🔴 Giống Cái (die)</span>
                        <span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 text-[11px]">Femininum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-800">
                        <li>• <b class="text-rose-950">die Jeans</b> <i>(die Jeans)</i>: quần bò</li>
                        <li>• <b class="text-rose-950">die Jacke</b> <i>(die Jacken)</i>: áo khoác</li>
                        <li>• <b class="text-rose-950">die Hose</b> <i>(die Hosen)</i>: quần</li>
                        <li>• <b class="text-rose-950">die Bluse</b> <i>(die Blusen)</i>: áo sơ mi nữ</li>
                        <li>• <b class="text-rose-950">die Socke</b> <i>(die Socken)</i>: tất</li>
                        <li>• <b class="text-rose-950">die Krawatte</b> <i>(die Krawatten)</i>: cà vạt</li>
                        <li>• <b class="text-rose-950">die Mütze</b> <i>(die Mützen)</i>: mũ len, mũ lưỡi trai</li>
                        <li>• <b class="text-rose-950">die Sonnenbrille</b> <i>(die Sonnenbrillen)</i>: kính râm</li>
                    </ul>
                </div>

                <!-- Giống trung (das) -->
                <div class="p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200 space-y-2">
                    <div class="flex items-center justify-between font-bold text-emerald-900 border-b border-emerald-200/60 pb-1.5">
                        <span class="text-sm">🟢 Giống Trung (das)</span>
                        <span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 text-[11px]">Neutrum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-800">
                        <li>• <b class="text-emerald-950">das T-Shirt</b> <i>(die T-Shirts)</i>: áo phông</li>
                        <li>• <b class="text-emerald-950">das Hemd</b> <i>(die Hemden)</i>: áo sơ mi nam</li>
                        <li>• <b class="text-emerald-950">das Kleid</b> <i>(die Kleider)</i>: đầm, váy liền</li>
                        <li>• <b class="text-emerald-950">das Sweatshirt</b> <i>(die Sweatshirts)</i>: áo nỉ</li>
                        <li>• <b class="text-emerald-950">das Paar</b>: đôi (<i>ein Paar Schuhe</i> = 1 đôi giày)</li>
                    </ul>
                </div>
            </div>

            <!-- Khung mẹo ghi nhớ -->
            <div class="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs text-amber-950 space-y-2">
                <div class="font-bold flex items-center gap-1.5 text-amber-900">
                    <span>💡</span> Mẹo nhớ giống và số nhiều trang phục:
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-700">
                    <div>• <b>Đuôi -e đa phần là die:</b> <i>die Jacke, die Hose, die Bluse, die Socke, die Krawatte, die Mütze</i>.</div>
                    <div>• <b>Đồ vật đi theo đôi thường dùng số nhiều:</b> <i>Schuhe, Socken, Stiefel, Handschuhe, Jeans</i>.</div>
                    <div>• <b>Đuôi -el, -er giữ nguyên số nhiều:</b> <i>der Stiefel → die Stiefel, der Gürtel → die Gürtel, der Pullover → die Pullover</i>.</div>
                    <div>• <b>Thêm Umlaut khi sang số nhiều:</b> <i>der Mantel → die Mäntel, der Rock → die Röcke, der Anzug → die Anzüge, der Hut → die Hüte</i>.</div>
                </div>
            </div>

            <!-- SƠ ĐỒ V4 NHÚNG VÀO ĐÂY -->
            <div id="svg-v4-container"></div>
        </div>

        <!-- HỌC PHẦN 2: 17 MÀU SẮC (DIE FARBE) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">2</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">17 Màu Sắc Tiếng Đức & Phân Loại Biến Đổi Đuôi</h2>
                    <p class="text-xs text-slate-500">Màu có chia đuôi, màu bất biến, màu ghép hell- / dunkel-</p>
                </div>
            </div>

            <!-- Bảng màu sắc đầy đủ -->
            <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2 text-xs text-center font-bold">
                <div class="p-2.5 rounded-xl border border-red-200 bg-red-50 text-red-900">rot (đỏ)</div>
                <div class="p-2.5 rounded-xl border border-orange-200 bg-orange-50 text-orange-900">orange (cam) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-yellow-200 bg-yellow-50 text-yellow-900">gelb (vàng)</div>
                <div class="p-2.5 rounded-xl border border-emerald-200 bg-emerald-50 text-emerald-900">grün (xanh lá)</div>
                <div class="p-2.5 rounded-xl border border-blue-200 bg-blue-50 text-blue-900">blau (xanh da trời)</div>
                <div class="p-2.5 rounded-xl border border-purple-200 bg-purple-50 text-purple-900">lila (tím hồng) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-indigo-200 bg-indigo-50 text-indigo-900">violett (tím xanh)</div>
                <div class="p-2.5 rounded-xl border border-pink-200 bg-pink-50 text-pink-900">rosa (hồng nhạt) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-pink-300 bg-pink-100 text-pink-950">pink (hồng đậm) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-slate-800 bg-slate-900 text-white">schwarz (đen)</div>
                <div class="p-2.5 rounded-xl border border-slate-300 bg-white text-slate-900 shadow-xs">weiß (trắng)</div>
                <div class="p-2.5 rounded-xl border border-slate-400 bg-slate-100 text-slate-800">grau (xám/ghi)</div>
                <div class="p-2.5 rounded-xl border border-amber-800 bg-amber-50 text-amber-950">braun (nâu)</div>
                <div class="p-2.5 rounded-xl border border-teal-200 bg-teal-50 text-teal-900">mint (xanh bạc hà) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-cyan-200 bg-cyan-50 text-cyan-900">türkis (xanh ngọc) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-amber-200 bg-amber-100/60 text-amber-900">beige (màu be) ⚠️</div>
                <div class="p-2.5 rounded-xl border border-indigo-200 bg-gradient-to-r from-red-100 via-green-100 to-blue-100 text-indigo-950">bunt (sặc sỡ)</div>
            </div>

            <!-- Bảng phân loại tính từ màu -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs pt-2">
                <div class="p-4 rounded-2xl bg-emerald-50/70 border border-emerald-200 space-y-2">
                    <div class="font-bold text-emerald-900 flex items-center gap-1.5">
                        <span>✅</span> 1. Nhóm Màu Có Chia Đuôi Bình Thường:
                    </div>
                    <p class="text-slate-700 leading-relaxed">
                        Gồm: <code>rot, gelb, grün, blau, schwarz, weiß, grau, braun, bunt, violett</code> và các màu ghép với <code>hell-</code> (sáng/nhạt) hoặc <code>dunkel-</code> (tối/đậm).<br>
                        Ví dụ: <i>Ich kaufe einen <b>roten</b> Schal.</i> · <i>Sie trägt ein <b>weißes</b> T-Shirt.</i>
                    </p>
                </div>

                <div class="p-4 rounded-2xl bg-rose-50/70 border border-rose-200 space-y-2">
                    <div class="font-bold text-rose-900 flex items-center gap-1.5">
                        <span>⚠️</span> 2. Nhóm Màu Bất Biến (Không Bao Giờ Thêm Đuôi):
                    </div>
                    <p class="text-slate-700 leading-relaxed">
                        Gồm các từ mượn tiếng nước ngoài: <code>orange, lila, rosa, pink, beige, türkis, mint</code>.<br>
                        Ví dụ: <i>Sie trägt eine <b>rosa</b> Bluse</i> (không bao giờ nói <s>rosane</s>). · <i>Ich suche ein <b>lila</b> Kleid.</i>
                    </p>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: MÀU SẮC & TRANG PHỤC Ở AKKUSATIV (TRỌNG TÂM 1) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">3</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Màu Sắc & Trang Phục ở Akkusativ — Đuôi Tính Từ „en – e – es – e“</h2>
                    <p class="text-xs text-slate-500">Công thức gắn đuôi màu sau mạo từ bất định (ein-) và danh từ số nhiều</p>
                </div>
            </div>

            <!-- Công thức vàng -->
            <div class="p-4 rounded-2xl bg-indigo-50/80 border border-indigo-200 text-xs text-indigo-950 space-y-2">
                <div class="text-sm font-black text-indigo-900">📐 CÔNG THỨC VÀNG VỀ ĐUÔI TÍNH TỪ MÀU Ở AKKUSATIV:</div>
                <div class="p-3 rounded-xl bg-white border border-indigo-200 font-mono text-center text-sm font-bold text-indigo-900 shadow-xs">
                    m: einen [Màu]-en &nbsp;|&nbsp; f: eine [Màu]-e &nbsp;|&nbsp; n: ein [Màu]-es &nbsp;|&nbsp; PL: [Màu]-e
                </div>
                <div class="text-[11px] text-slate-600 space-y-1">
                    <div>💡 <b>Ghi chú số nhiều (Plural):</b> PL: <code>-e</code> khi không có mạo từ (<i>rote Schuhe</i>); nếu đi sau <i>die / diese / welche / keine / meine</i> thì dùng đuôi <code>-en</code> (<i>diese roten Schuhe</i>).</div>
                    <div>💡 <b>Giải thích bản chất:</b> Ở giống trung (das Kleid), mạo từ <code>ein</code> không có đuôi nên tính từ phải gánh đuôi đặc trưng <code>-es</code> (giống đuôi das). Còn ở giống đực, mạo từ <code>einen</code> đã mang đuôi <code>-en</code> nên tính từ nhận tiếp đuôi <code>-en</code>.</div>
                </div>
            </div>

            <!-- SƠ ĐỒ V2 NHÚNG VÀO ĐÂY -->
            <div id="svg-v2-container"></div>

            <!-- Bảng phân tích câu Familie Müller -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs">
                <div class="font-bold text-slate-800">📖 Phân tích ví dụ thực tế trên bảng giảng:</div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-700">
                    <div class="p-2 rounded-xl bg-white border border-slate-200">
                        • <i>Frau Müller trägt <b>eine grüne Hose</b> (f → -e), <b>ein schwarzes T-Shirt</b> (n → -es) und <b>weiße Schuhe</b> (PL → -e).</i>
                    </div>
                    <div class="p-2 rounded-xl bg-white border border-slate-200">
                        • <i>Herr Müller zieht <b>einen blauen Trainingsanzug</b> (m → -en) an.</i>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: ÔN LẠI AKKUSATIV & DATIV VỚI TRANG PHỤC -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">4</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Ôn Lại Akkusativ & Dativ Với Trang Phục: Wen/Was? — Wem?</h2>
                    <p class="text-xs text-slate-500">Phân biệt động từ đi với Akkusativ, Dativ và cả hai; đại từ nhân xưng ở Dativ</p>
                </div>
            </div>

            <!-- SƠ ĐỒ V3 NHÚNG VÀO ĐÂY -->
            <div id="svg-v3-container"></div>

            <!-- Quy tắc vàng Dativ & 4 động từ thời trang -->
            <div class="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs text-amber-950 space-y-2">
                <div class="font-bold text-amber-900">💡 Quy tắc vàng phân biệt Akkusativ vs Dativ:</div>
                <div class="text-slate-700 leading-relaxed">
                    Với nhóm động từ Dativ (<code>gefallen, passen, stehen, gehören</code>), món đồ trang phục đóng vai trò làm <b>Chủ ngữ (Nominativ)</b>, còn người mặc/thích luôn chia ở <b>Cách 3 (Dativ: mir, dir, ihm, ihr...)</b>.
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1 text-slate-800">
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        • <b>passen (+ Dativ):</b> vừa vặn về kích cỡ (Größe) / size.<br>
                        <i>Ví dụ: Die Hose passt mir. (Chiếc quần vừa với tôi).</i>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        • <b>stehen (+ Dativ):</b> hợp/đẹp với vẻ ngoài, màu sắc, phong cách.<br>
                        <i>Ví dụ: Das Kleid steht dir gut. (Chiếc đầm rất hợp với bạn).</i>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        • <b>gefallen (+ Dativ):</b> thích, ưng mắt về thẩm mỹ nói chung.<br>
                        <i>Ví dụ: Der Mantel gefällt ihm. (Anh ấy thích chiếc áo măng tô này).</i>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-amber-200">
                        • <b>gehören (+ Dativ):</b> thuộc về ai (quyền sở hữu).<br>
                        <i>Ví dụ: Die Jacke gehört mir. (Chiếc áo khoác thuộc về tôi / của tôi).</i>
                    </div>
                </div>
            </div>

            <!-- Bảng đại từ Dativ tra cứu nhanh -->
            <div class="p-4 rounded-2xl bg-purple-50/70 border border-purple-200 text-xs space-y-2">
                <div class="font-bold text-purple-900">Bảng Tra Cứu Đại Từ Nhân Xưng ở Dativ (Ôn tập):</div>
                <div class="grid grid-cols-3 sm:grid-cols-9 gap-1 text-center font-mono">
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">ich</span><b class="text-purple-700">mir</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">du</span><b class="text-purple-700">dir</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">er</span><b class="text-purple-700">ihm</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">sie</span><b class="text-purple-700">ihr</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">es</span><b class="text-purple-700">ihm</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">wir</span><b class="text-purple-700">uns</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">ihr</span><b class="text-purple-700">euch</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">sie</span><b class="text-purple-700">ihnen</b></div>
                    <div class="p-2 rounded-lg bg-white border border-purple-200"><span class="text-[10px] text-slate-400 block">Sie</span><b class="text-purple-700">Ihnen</b></div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 5: ĐẠI TỪ CHỈ ĐỊNH DIES- (TRỌNG TÂM 2) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">5</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Đại Từ Chỉ Định dies- (dieser / diesen / diese / dieses)</h2>
                    <p class="text-xs text-slate-500">Cách dùng đi kèm danh từ hoặc đứng độc lập, kết hợp cặp câu hỏi welch- ↔ dies-</p>
                </div>
            </div>

            <!-- SƠ ĐỒ V1 NHÚNG VÀO ĐÂY -->
            <div id="svg-v1-container"></div>

            <div class="p-4 rounded-2xl bg-blue-50/70 border border-blue-200 text-xs text-blue-950 space-y-2">
                <div class="font-bold text-blue-900">💡 Quy tắc vàng:</div>
                <div class="text-slate-800 font-medium">
                    Chỉ giống Đực (der) mới biến đổi ở Akkusativ (-en: <b>welchen / diesen</b>). Giống cái (-e), giống trung (-es) và số nhiều (-e) giữ nguyên hình thái như ở Nominativ!
                </div>
                <div class="font-bold text-blue-900 pt-1">📌 Hai cách dùng của dies-:</div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-700">
                    <div class="p-2.5 rounded-xl bg-white border border-blue-200">
                        <b>1. Đi kèm danh từ:</b> <i>Ich kaufe <b>diesen Rock</b>.</i> (Tôi mua chiếc chân váy này).
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-blue-200">
                        <b>2. Đứng một mình:</b> <i>Welchen Gürtel nimmst du? — <b>Diesen hier</b>.</i> (thay thế cho der Gürtel).
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 6: THỜI TIẾT (DAS WETTER) (TRỌNG TÂM 3) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">6</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Thời Tiết (Das Wetter): Mẫu Câu, Hỏi Đáp, Nhiệt Độ & Mùa</h2>
                    <p class="text-xs text-slate-500">Cách dùng chủ ngữ giả es, 4 cấu trúc câu thời tiết và cách đọc nhiệt độ chuẩn bằng chữ</p>
                </div>
            </div>

            <!-- 4 Mẫu câu thời tiết -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5 text-xs">
                <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                    <div class="font-bold text-slate-900">① Es + Động từ</div>
                    <div class="font-mono text-indigo-700 font-bold">Es regnet.</div>
                    <div class="text-[11px] text-slate-500">Trời mưa (hoặc Es schneit = tuyết rơi).</div>
                </div>
                <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                    <div class="font-bold text-slate-900">② Es ist + Tính từ</div>
                    <div class="font-mono text-indigo-700 font-bold">Es ist windig.</div>
                    <div class="text-[11px] text-slate-500">Trời có gió (sonnig, windig, neblig, kalt, heiß, warm, kühl, bewölkt).</div>
                </div>
                <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                    <div class="font-bold text-slate-900">③ Die Sonne scheint</div>
                    <div class="font-mono text-indigo-700 font-bold">Die Sonne scheint.</div>
                    <div class="text-[11px] text-slate-500">Mặt trời chiếu sáng (trời nắng).</div>
                </div>
                <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                    <div class="font-bold text-slate-900">④ Es gibt + Akkusativ</div>
                    <div class="font-mono text-indigo-700 font-bold">Es gibt Regen.</div>
                    <div class="text-[11px] text-slate-500">Có mưa / có sương mù (Nebel).</div>
                </div>
            </div>

            <!-- SƠ ĐỒ V5 NHÚNG VÀO ĐÂY -->
            <div id="svg-v5-container"></div>
        </div>

        <!-- HỌC PHẦN 7: MUA QUẦN ÁO — HỘI THOẠI Ở CỬA HÀNG -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">7</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Mua Quần Áo — Hội Thoại ở Cửa Hàng & Phòng Thử Đồ</h2>
                    <p class="text-xs text-slate-500">8 Cặp giao tiếp chuẩn giữa người bán và khách, hỏi kích cỡ và phòng thử đồ</p>
                </div>
            </div>

            <!-- SƠ ĐỒ V6 NHÚNG VÀO ĐÂY -->
            <div id="svg-v6-container"></div>
        </div>

        <!-- HỌC PHẦN 8: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">8</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Đọc Hiểu & Phân Tích Văn Bản Thực Tế (Textanalyse)</h2>
                    <p class="text-xs text-slate-500">3 Đoạn văn hoàn chỉnh có phát âm chuẩn de-DE và phân tích cấu trúc ngữ pháp</p>
                </div>
            </div>

            <div class="space-y-4 text-xs">
                <!-- Đoạn 1 -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-slate-900 text-sm">Đoạn 1: Familie Müller macht viel Sport</span>
                        <button onclick="speakGerman('Familie Müller macht viel Sport. Frau Müller spielt Fußball. Sie trägt eine grüne Hose, ein schwarzes T-Shirt und weiße Schuhe. Ihr Mann spielt Tennis. Heute hat er einen blauen Trainingsanzug und gelbe Schuhe angezogen.', 0.9)" class="text-indigo-600 font-bold hover:underline cursor-pointer">🔊 Nghe đoạn văn</button>
                    </div>
                    <p class="text-slate-700 leading-relaxed italic">
                        „Familie Müller macht viel Sport. Frau Müller spielt Fußball. Sie trägt <b>eine grüne Hose</b>, <b>ein schwarzes T-Shirt</b> und <b>weiße Schuhe</b>. Ihr Mann spielt Tennis. Heute hat er <b>einen blauen Trainingsanzug</b> und <b>gelbe Schuhe</b> angezogen.“
                    </p>
                    <div class="text-slate-500 text-[11px]">
                        📖 <b>Dịch:</b> Gia đình Müller tập thể thao nhiều. Bà Müller chơi bóng đá. Bà mặc quần xanh lá, áo phông đen và giày trắng. Chồng bà chơi quần vợt. Hôm nay ông ấy mặc bộ đồ thể thao xanh và đi giày vàng.
                    </div>
                </div>

                <!-- Đoạn 2 -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-slate-900 text-sm">Đoạn 2: Das Wetter in Vietnam</span>
                        <button onclick="speakGerman('Wie ist das Wetter in Vietnam? Im Norden ist es im Winter kalt, und oft ist es neblig. Im Sommer ist es dort sehr heiß, und es regnet viel. In Đà Lạt ist es das ganze Jahr kühl. In Sài Gòn ist es immer warm.', 0.9)" class="text-indigo-600 font-bold hover:underline cursor-pointer">🔊 Nghe đoạn văn</button>
                    </div>
                    <p class="text-slate-700 leading-relaxed italic">
                        „Wie ist das Wetter in Vietnam? Im Norden ist es im Winter kalt, und oft ist es neblig. Im Sommer ist es dort sehr heiß, und es regnet viel. In Đà Lạt ist es das ganze Jahr kühl. Dort gibt es am Morgen oft Nebel. In Sài Gòn ist es immer warm.“
                    </p>
                    <div class="text-slate-500 text-[11px]">
                        📖 <b>Dịch:</b> Thời tiết ở Việt Nam thế nào? Ở miền Bắc mùa đông trời lạnh và thường có sương mù. Mùa hè rất nóng và mưa nhiều. Ở Đà Lạt trời mát quanh năm. Buổi sáng hay có sương mù. Ở Sài Gòn trời luôn ấm.
                    </div>
                </div>

                <!-- Đoạn 3: Im Kaufhaus -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-bold text-slate-900 text-sm">Đoạn 3: Im Kaufhaus (Mua sắm tại trung tâm thương mại)</span>
                        <button onclick="speakGerman('Im Kaufhaus sucht Herr Schmidt einen Pullover. Die Verkäuferin fragt: Welchen Pullover möchten Sie? Herr Schmidt zeigt auf das Regal: Diesen hier. Er probiert ihn an. Der Pullover passt ihm perfekt und die grüne Farbe steht ihm sehr gut.', 0.9)" class="text-indigo-600 font-bold hover:underline cursor-pointer">🔊 Nghe đoạn văn</button>
                    </div>
                    <p class="text-slate-700 leading-relaxed italic">
                        „Im Kaufhaus sucht Herr Schmidt <b>einen Pullover</b>. Die Verkäuferin fragt: <i>„<b>Welchen Pullover</b> möchten Sie?“</i> Herr Schmidt zeigt auf das Regal: <i>„<b>Diesen hier</b>.“</i> Er probiert ihn an. Der Pullover <b>passt ihm</b> perfekt und die grüne Farbe <b>steht ihm</b> sehr gut.“
                    </p>
                    <div class="text-slate-500 text-[11px]">
                        📖 <b>Dịch:</b> Tại trung tâm bách hóa, ông Schmidt tìm một chiếc áo len. Cô bán hàng hỏi: „Ngài muốn mua chiếc áo len nào ạ?“ Ông Schmidt chỉ vào giá để đồ: „Chiếc này đây ạ.“ Ông ấy thử áo. Chiếc áo len vừa khít với ông ấy và màu xanh lá rất hợp với ông ấy.
                    </div>
                    <div class="mt-2 pt-2 border-t border-slate-200 grid grid-cols-1 sm:grid-cols-2 gap-1.5 text-[11px] text-slate-600">
                        <div>• <code>einen Pullover / Welchen Pullover / Diesen hier</code>: giống đực (der) biến cách ở Akkusativ (-en).</div>
                        <div>• <code>anprobieren (thử đồ)</code>: động từ tách <i>(Er probiert ihn an)</i>.</div>
                        <div>• <code>passen + Dativ (ihm)</code>: vừa vặn về kích cỡ.</div>
                        <div>• <code>stehen + Dativ (ihm)</code>: hợp về diện mạo và màu sắc.</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 9: BẢNG TỔNG HỢP KIẾN THỨC (CHEAT SHEET) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3 border-b border-slate-100 pb-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm flex items-center justify-center shrink-0">9</span>
                <div>
                    <h2 class="text-base sm:text-lg font-black text-slate-900">Bảng Tổng Hợp Kiến Thức Cốt Lõi (Cheat Sheet Bài 11)</h2>
                    <p class="text-xs text-slate-500">Ôn tập siêu tốc toàn bộ điểm ngữ pháp trọng tâm trước khi làm 100 câu bài tập</p>
                </div>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-left text-xs divide-y divide-slate-200">
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <tr class="p-3 bg-slate-50 font-bold"><td class="p-3 w-1/3 text-indigo-900">Màu ở Akkusativ</td><td class="p-3">m <code>-en</code> (einen roten Rock) · f <code>-e</code> (eine rote Bluse) · n <code>-es</code> (ein rotes Kleid) · PL <code>-e</code> khi không có mạo từ (rote Schuhe); nếu đi sau <i>die / diese / welche / keine / meine</i> thì dùng đuôi <code>-en</code> (diese roten Schuhe) → <b>„en – e – es – e“</b></td></tr>
                        <tr class="p-3"><td class="p-3 font-bold text-indigo-900">Màu bất biến</td><td class="p-3"><code>rosa, lila, orange, beige, türkis, mint, pink</code> (không bao giờ chia đuôi: <i>eine rosa Bluse</i>)</td></tr>
                        <tr class="p-3 bg-slate-50 font-bold"><td class="p-3 text-indigo-900">dies- (Đại từ chỉ định)</td><td class="p-3">Chỉ giống đực biến đổi: <b>dieser → diesen</b> (Akkusativ). f: diese · n: dieses · PL: diese</td></tr>
                        <tr class="p-3"><td class="p-3 font-bold text-indigo-900">Akkusativ vs. Dativ</td><td class="p-3">Akkusativ: <code>tragen, anziehen, anprobieren, kaufen, suchen</code> · Dativ: <code>gefallen, passen, stehen, gehören</code></td></tr>
                        <tr class="p-3 bg-slate-50 font-bold"><td class="p-3 text-indigo-900">Thời tiết</td><td class="p-3"><code>Es regnet / Es schneit</code> (động từ) · <code>Es ist sonnig / windig / neblig / kalt / heiß</code> (tính từ)</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- THẺ HOÀN THÀNH LÝ THUYẾT VÀ NÚT CHUYỂN SANG BÀI TẬP -->
        <div class="p-6 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 text-center space-y-4">
            <div class="text-sm sm:text-base font-black text-indigo-300">
                🎉 Bạn Đã Nắm Vững Toàn Bộ Lý Thuyết Bài 11?
            </div>
            <p class="text-xs sm:text-sm text-slate-300 max-w-xl mx-auto">
                Bắt đầu chinh phục kho <b>100 Bài tập Độc nhất (Đủ 18 Dạng)</b> với phản hồi âm thanh chuẩn bản xứ và hệ thống chấm điểm Zero-Bug!
            </p>
            <div class="pt-2">
                <button onclick="switchTab('exercises')" class="px-6 py-3 rounded-2xl bg-indigo-600 hover:bg-indigo-500 text-white font-black text-sm shadow-lg hover:shadow-indigo-500/30 transition-all cursor-pointer inline-flex items-center gap-2">
                    Lý thuyết đã xong • Tiếp tục làm bài tập ➜
                </button>
            </div>
        </div>
    </div>
    """

    vocabularies_raw = [('Stiefel', 'der', 'bốt (số nhiều: die Stiefel)', 'Im Schnee trage ich gern Stiefel.'), ('Mantel', 'der', 'áo măng tô (số nhiều: die Mäntel)', 'Bei Kälte trage ich einen Mantel.'), ('Pullover', 'der', 'áo len chui đầu (số nhiều: die Pullover)', 'Heute trage ich einen Pullover.'), ('Rock', 'der', 'chân váy (số nhiều: die Röcke)', 'Meine Schwester trägt gern einen Rock.'), ('Anzug', 'der', 'bộ com lê (số nhiều: die Anzüge)', 'Mein Vater trägt einen Anzug und eine Krawatte.'), ('Schuh', 'der', 'giày (số nhiều: die Schuhe)', 'Die Schuhe sind Größe neununddreißig.'), ('Gürtel', 'der', 'thắt lưng (số nhiều: die Gürtel)', 'Ich brauche einen Gürtel für die Hose.'), ('Hut', 'der', 'mũ có vành (số nhiều: die Hüte)', 'In der Sonne trägt er einen Hut.'), ('Handschuh', 'der', 'găng tay (số nhiều: die Handschuhe)', 'Bei Kälte trage ich Handschuhe.'), ('Jeans', 'die', 'quần bò (số nhiều: die Jeans)', 'Ich trage gern Jeans und ein T-Shirt.'), ('Jacke', 'die', 'áo khoác (số nhiều: die Jacken)', 'Im Herbst trage ich eine Jacke.'), ('Hose', 'die', 'quần (số nhiều: die Hosen)', 'Die Hose ist mir zu lang.'), ('Bluse', 'die', 'áo sơ mi nữ (số nhiều: die Blusen)', 'Sie trägt eine Bluse und einen Rock.'), ('Socke', 'die', 'tất (số nhiều: die Socken)', 'Ich brauche warme Socken.'), ('Krawatte', 'die', 'cà vạt (số nhiều: die Krawatten)', 'Mein Onkel trägt eine Krawatte.'), ('T-Shirt', 'das', 'áo phông (số nhiều: die T-Shirts)', 'Im Sommer trage ich ein T-Shirt.'), ('Hemd', 'das', 'áo sơ mi nam (số nhiều: die Hemden)', 'Er trägt ein Hemd und eine Krawatte.'), ('Kleid', 'das', 'đầm, váy liền (số nhiều: die Kleider)', 'Sie trägt ein Kleid zur Party.'), ('Schal', 'der', 'khăn quàng (số nhiều: die Schals)', 'Im Winter brauche ich einen Schal.'), ('Mütze', 'die', 'mũ len, mũ lưỡi trai (số nhiều: die Mützen)', 'Bei Kälte trage ich eine Mütze.'), ('Regenmantel', 'der', 'áo mưa (số nhiều: die Regenmäntel)', 'Bei Regen trage ich einen Regenmantel.'), ('Regenschirm', 'der', 'cái ô (số nhiều: die Regenschirme)', 'Ich nehme heute einen Regenschirm mit.'), ('Sonnenbrille', 'die', 'kính râm (số nhiều: die Sonnenbrillen)', 'Bei Sonne trage ich eine Sonnenbrille.'), ('Größe', 'die', 'kích cỡ (số nhiều: die Größen)', 'Welche Größe haben Sie?'), ('Umkleidekabine', 'die', 'phòng thử đồ (số nhiều: die Umkleidekabinen)', 'Die Umkleidekabine ist dort hinten.'), ('Regen', 'der', 'mưa (chỉ có số ít)', 'Bei Regen bleibe ich zu Hause.'), ('Schnee', 'der', 'tuyết (chỉ có số ít)', 'Im Winter liegt viel Schnee in den Bergen.'), ('Wind', 'der', 'gió (số nhiều: die Winde)', 'Der Wind ist heute kalt.'), ('Nebel', 'der', 'sương mù (chỉ có số ít)', 'Im Herbst gibt es oft Nebel.'), ('Sturm', 'der', 'cơn bão (số nhiều: die Stürme)', 'Der Sturm kommt heute Abend.'), ('Himmel', 'der', 'bầu trời (số nhiều: die Himmel)', 'Der Himmel ist heute bewölkt.'), ('Frühling', 'der', 'mùa xuân (số nhiều: die Frühlinge)', 'Im Frühling ist es warm.'), ('Sommer', 'der', 'mùa hè (số nhiều: die Sommer)', 'Im Sommer ist es heiß.'), ('Herbst', 'der', 'mùa thu (số nhiều: die Herbste)', 'Im Herbst regnet es oft.'), ('Winter', 'der', 'mùa đông (số nhiều: die Winter)', 'Im Winter schneit es in Deutschland.'), ('Wetterbericht', 'der', 'bản tin thời tiết (số nhiều: die Wetterberichte)', 'Der Wetterbericht meldet Regen.'), ('Kleiderschrank', 'der', 'tủ quần áo (số nhiều: die Kleiderschränke)', 'Mein Kleiderschrank ist voll.'), ('Sonne', 'die', 'mặt trời (số nhiều: die Sonnen)', 'Heute scheint die Sonne.'), ('Wolke', 'die', 'đám mây (số nhiều: die Wolken)', 'Am Himmel sind viele Wolken.'), ('Kälte', 'die', 'khí lạnh, cái lạnh (chỉ có số ít)', 'Bei Kälte friere ich schnell.'), ('Hitze', 'die', 'khí nóng, cái nóng (chỉ có số ít)', 'Bei Hitze schwitze ich viel.'), ('Temperatur', 'die', 'nhiệt độ (số nhiều: die Temperaturen)', 'Die Temperatur ist heute sehr hoch.'), ('Jahreszeit', 'die', 'mùa trong năm (số nhiều: die Jahreszeiten)', 'Welche Jahreszeit magst du am liebsten?'), ('Farbe', 'die', 'màu sắc (số nhiều: die Farben)', 'Welche Farbe hat dein Hemd?'), ('Mode', 'die', 'thời trang (chỉ có số ít)', 'Meine Schwester mag Mode.'), ('Wetter', 'das', 'thời tiết (chỉ có số ít)', 'Wie ist das Wetter heute?'), ('Gewitter', 'das', 'cơn dông (số nhiều: die Gewitter)', 'Am Abend gibt es ein Gewitter.'), ('Grad', 'das', 'độ nhiệt độ (sau số đếm giữ nguyên: zwanzig Grad)', 'Heute sind es zwanzig Grad.'), ('Kaufhaus', 'das', 'trung tâm bách hóa (số nhiều: die Kaufhäuser)', 'Im Kaufhaus gibt es viele Mäntel.'), ('Geschäft', 'das', 'cửa hàng (số nhiều: die Geschäfte)', 'Das Geschäft öffnet um neun Uhr.')]

    vocabularies_data = [
        (lesson_id, word, article, meaning, example)
        for (word, article, meaning, example) in vocabularies_raw
    ]

    exercises_raw = [
        {
                "type": "trac_nghiem",
                "question": "Câu 1: Chọn dạng đúng: „Wir nehmen ___ Hut hier.“",
                "options": [
                        "dieser",
                        "diesen",
                        "diese",
                        "dieses"
                ],
                "correct_answer": "diesen",
                "explanation": "der Hut là danh từ giống đực, đóng vai trò tân ngữ trực tiếp (Akkusativ) của động từ 'nehmen' nên đại từ chỉ định dies- nhận đuôi -en thành diesen → „Wir nehmen diesen Hut hier.“ → Đáp án: \"diesen\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chúng tôi lấy chiếc mũ này đây.",
                        "accepted_answers": [
                                "diesen",
                                "B"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 2: Chọn dạng đúng: „___ Schuhe sind mir zu groß.“",
                "options": [
                        "Dieser",
                        "Diesen",
                        "Diese",
                        "Dieses"
                ],
                "correct_answer": "Diese",
                "explanation": "die Schuhe là danh từ số nhiều làm chủ ngữ (Nominativ); dạng chỉ định số nhiều luôn là Diese -> „Diese Schuhe sind mir zu groß.“ -> Đáp án: \"Diese\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Đôi giày này rộng quá đối với tôi.",
                        "accepted_answers": [
                                "Diese",
                                "C"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 3: Chọn đuôi đúng: „Heute trage ich einen ___ Pullover.“",
                "options": [
                        "roter",
                        "roten",
                        "rote",
                        "rotes"
                ],
                "correct_answer": "roten",
                "explanation": "der Pullover là danh từ giống đực ở Akkusativ sau mạo từ bất định einen; tính từ nhận đuôi -en -> „einen roten Pullover“. -> Đáp án: \"roten\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Hôm nay tôi mặc một chiếc áo len đỏ.",
                        "accepted_answers": [
                                "roten",
                                "B"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 4: Chọn đuôi đúng: „Sie kauft eine ___ Hose.“",
                "options": [
                        "schwarzen",
                        "schwarze",
                        "schwarzes",
                        "schwarzer"
                ],
                "correct_answer": "schwarze",
                "explanation": "die Hose là danh từ giống cái ở Akkusativ sau mạo từ eine; tính từ nhận đuôi -e -> „eine schwarze Hose“. -> Đáp án: \"schwarze\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Cô ấy mua một chiếc quần đen.",
                        "accepted_answers": [
                                "schwarze",
                                "B"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 5: Chọn đuôi đúng: „Er sucht ein ___ Hemd.“",
                "options": [
                        "weißer",
                        "weißen",
                        "weiße",
                        "weißes"
                ],
                "correct_answer": "weißes",
                "explanation": "das Hemd là danh từ giống trung ở Akkusativ; mạo từ ein không có đuôi nên tính từ phải mang đuôi -es -> „ein weißes Hemd“. -> Đáp án: \"weißes\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Anh ấy tìm một chiếc áo sơ mi trắng.",
                        "accepted_answers": [
                                "weißes",
                                "D"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 6: Chọn đại từ đúng: „Die Jacke passt ___ gut.“ (ngôi: du)",
                "options": [
                        "dich",
                        "dir",
                        "du",
                        "dein"
                ],
                "correct_answer": "dir",
                "explanation": "Động từ passen (vừa vặn) bắt buộc đi với Dativ; dạng Dativ của đại từ du là dir -> „Die Jacke passt dir gut.“ -> Đáp án: \"dir\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chiếc áo khoác rất vừa với bạn.",
                        "accepted_answers": [
                                "dir",
                                "B"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 7: Chọn câu đúng nghĩa \"Trời đang mưa\":",
                "options": [
                        "Es ist regnet.",
                        "Es regnet.",
                        "Der Regen ist.",
                        "Es hat regnen."
                ],
                "correct_answer": "Es regnet.",
                "explanation": "regnen là động từ thời tiết, dùng với chủ ngữ giả es -> „Es regnet.“ (tuyệt đối không dùng kèm ist). -> Đáp án: \"Es regnet.\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Trời đang mưa.",
                        "accepted_answers": [
                                "Es regnet.",
                                "B"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 8: Chọn dạng đúng: „Ich kaufe gern ___ Schuhe.“",
                "options": [
                        "braune",
                        "braunen",
                        "braunes",
                        "brauner"
                ],
                "correct_answer": "braune",
                "explanation": "Danh từ số nhiều không có mạo từ ở Akkusativ nhận đuôi -e -> „braune Schuhe“. -> Đáp án: \"braune\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi thích mua giày nâu.",
                        "accepted_answers": [
                                "braune",
                                "A"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 9: Chọn từ đúng: „Welchen Gürtel nimmst du? — ___ hier.“",
                "options": [
                        "Dieser",
                        "Diesen",
                        "Diese",
                        "Dieses"
                ],
                "correct_answer": "Diesen",
                "explanation": "Welchen Gürtel là der Gürtel ở Akkusativ (giống đực); khi đứng độc lập thay thế cho tân ngữ giống đực thì dùng Diesen hier. -> Đáp án: \"Diesen\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Bạn lấy chiếc thắt lưng nào? — Chiếc này đây.",
                        "accepted_answers": [
                                "Diesen",
                                "B"
                        ]
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 10: Dòng nào ghi ĐÚNG cả mạo từ lẫn số nhiều?",
                "options": [
                        "der Mantel – die Mäntel / die Jacke – die Jacken / das Kleid – die Kleider",
                        "der Mantel – die Mantels / die Jacke – die Jacke / das Kleid – die Kleids",
                        "die Mantel – die Mäntel / der Jacke – die Jacken / das Kleid – die Kleider",
                        "der Rock – die Rocks / die Hose – die Hose / das Hemd – die Hemde"
                ],
                "correct_answer": "der Mantel – die Mäntel / die Jacke – die Jacken / das Kleid – die Kleider",
                "explanation": "der Mantel -> die Mäntel (thêm Umlaut), die Jacke -> die Jacken, das Kleid -> die Kleider. Các dòng còn lại sai giống hoặc sai dạng số nhiều. -> Đáp án: \"der Mantel – die Mäntel / die Jacke – die Jacken / das Kleid – die Kleider\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "áo măng tô – các áo măng tô / áo khoác – các áo khoác / đầm – các đầm.",
                        "accepted_answers": [
                                "der Mantel – die Mäntel / die Jacke – die Jacken / das Kleid – die Kleider",
                                "A"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 11: Điền vào chỗ trống: „Der Hut steht ___ gut.“ (ngôi: ich)",
                "options": null,
                "correct_answer": "mir",
                "explanation": "Động từ stehen (hợp với ai) đi với Dativ; đại từ Dativ của ich là mir -> „Der Hut steht mir gut.“ -> Đáp án: \"mir\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chiếc mũ rất hợp với tôi.",
                        "accepted_answers": [
                                "mir"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 12: Điền vào chỗ trống: „Die Stiefel passen ___ nicht.“ (ngôi: sie - họ)",
                "options": null,
                "correct_answer": "ihnen",
                "explanation": "Động từ passen đi với Dativ; đại từ Dativ của sie (họ) là ihnen -> „Die Stiefel passen ihnen nicht.“ -> Đáp án: \"ihnen\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Đôi bốt không vừa với họ.",
                        "accepted_answers": [
                                "ihnen"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 13: Điền vào chỗ trống: „Der Pullover gefällt ___ sehr.“ (ngôi: er)",
                "options": null,
                "correct_answer": "ihm",
                "explanation": "Động từ gefallen đi với Dativ; đại từ Dativ của er là ihm -> „Der Pullover gefällt ihm sehr.“ -> Đáp án: \"ihm\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chiếc áo len làm anh ấy rất thích.",
                        "accepted_answers": [
                                "ihm"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 14: Điền đại từ chỉ định thích hợp (dạng của dies-): „Ich möchte ___ Jacke hier.“",
                "options": null,
                "correct_answer": "diese",
                "explanation": "die Jacke là danh từ giống cái; ở Akkusativ vẫn giữ nguyên đuôi diese -> „Ich möchte diese Jacke hier.“ -> Đáp án: \"diese\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Tôi muốn chiếc áo khoác này đây.",
                        "accepted_answers": [
                                "diese"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 15: Điền đại từ chỉ định thích hợp (dạng của dies-): „___ Kleid ist sehr schön.“",
                "options": null,
                "correct_answer": "Dieses",
                "explanation": "das Kleid là danh từ giống trung làm chủ ngữ (Nominativ) -> Dieses Kleid ist sehr schön. -> Đáp án: \"Dieses\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chiếc đầm này rất đẹp.",
                        "accepted_answers": [
                                "Dieses",
                                "dieses"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 16: Điền vào chỗ trống (động từ schneien): „Im Winter ___ es in Deutschland oft.“",
                "options": null,
                "correct_answer": "schneit",
                "explanation": "Động từ thời tiết schneien chia ở ngôi es là schneit -> „Im Winter schneit es in Deutschland oft.“ -> Đáp án: \"schneit\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Vào mùa đông ở Đức tuyết thường rơi.",
                        "accepted_answers": [
                                "schneit"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 17: Điền tính từ thời tiết thích hợp: „Im Sommer ist es in Sài Gòn oft sehr ___.“",
                "options": null,
                "correct_answer": "heiß",
                "explanation": "Sau cụm 'ist es' dùng tính từ: die Hitze -> heiß -> „Im Sommer ist es in Sài Gòn oft sehr heiß.“ -> Đáp án: \"heiß\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Vào mùa hè ở Sài Gòn trời thường rất nóng.",
                        "accepted_answers": [
                                "heiß",
                                "heiss"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 18: Chia động từ tragen: „Du ___ heute eine Hose und einen Pullover.“",
                "options": null,
                "correct_answer": "trägst",
                "explanation": "tragen là động từ biến âm a -> ä ở ngôi du: du trägst -> „Du trägst heute eine Hose und einen Pullover.“ -> Đáp án: \"trägst\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Hôm nay bạn mặc một chiếc quần và một chiếc áo len.",
                        "accepted_answers": [
                                "trägst",
                                "traegst"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 19: Chia động từ tragen: „Ihr ___ im Sommer gern T-Shirts.“",
                "options": null,
                "correct_answer": "tragt",
                "explanation": "Ngôi ihr không đổi nguyên âm: ihr tragt (không có Umlaut) -> „Ihr tragt im Sommer gern T-Shirts.“ -> Đáp án: \"tragt\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Vào mùa hè các bạn thích mặc áo phông.",
                        "accepted_answers": [
                                "tragt"
                        ]
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 20: Điền tiền tố tách thích hợp (nghĩa: mặc vào): „Anna zieht heute einen Mantel ___.“",
                "options": null,
                "correct_answer": "an",
                "explanation": "anziehen là động từ tách, tiền tố an- đứng ở vị trí cuối câu đơn -> „Anna zieht heute einen Mantel an.“ -> Đáp án: \"an\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Hôm nay Anna mặc áo măng tô vào.",
                        "accepted_answers": [
                                "an"
                        ]
                }
        },
        {
                "type": "dien_duoi_tinh_tu",
                "question": "Câu 21: Điền đuôi tính từ vào chỗ trống: „Er kauft einen blau__ Anzug.“",
                "options": null,
                "correct_answer": "en",
                "explanation": "der Anzug là giống đực ở Akkusativ sau mạo từ einen; tính từ nhận đuôi -en -> einen blauen Anzug. -> Đáp án: \"en\"",
                "exp_reward": 10,
                "extra_data": {
                        "display_sentence": "Er kauft einen blau__ Anzug.",
                        "stem": "blau",
                        "noun": "der Anzug",
                        "gender": "m",
                        "full_sentence": "Er kauft einen blauen Anzug.",
                        "translation": "Anh ấy mua một bộ com lê xanh.",
                        "accepted_answers": [
                                "en",
                                "-en"
                        ]
                }
        },
        {
                "type": "dien_duoi_tinh_tu",
                "question": "Câu 22: Điền đuôi tính từ vào chỗ trống: „Sie trägt ein gelb__ Kleid.“",
                "options": null,
                "correct_answer": "es",
                "explanation": "das Kleid là giống trung ở Akkusativ; sau mạo từ ein tính từ nhận đuôi -es -> ein gelbes Kleid. -> Đáp án: \"es\"",
                "exp_reward": 10,
                "extra_data": {
                        "display_sentence": "Sie trägt ein gelb__ Kleid.",
                        "stem": "gelb",
                        "noun": "das Kleid",
                        "gender": "n",
                        "full_sentence": "Sie trägt ein gelbes Kleid.",
                        "translation": "Cô ấy mặc một chiếc đầm vàng.",
                        "accepted_answers": [
                                "es",
                                "-es"
                        ]
                }
        },
        {
                "type": "dien_duoi_tinh_tu",
                "question": "Câu 23: Điền đuôi tính từ vào chỗ trống: „Wir suchen eine grau__ Hose.“",
                "options": null,
                "correct_answer": "e",
                "explanation": "die Hose là giống cái ở Akkusativ; sau mạo từ eine tính từ nhận đuôi -e -> eine graue Hose. -> Đáp án: \"e\"",
                "exp_reward": 10,
                "extra_data": {
                        "display_sentence": "Wir suchen eine grau__ Hose.",
                        "stem": "grau",
                        "noun": "die Hose",
                        "gender": "f",
                        "full_sentence": "Wir suchen eine graue Hose.",
                        "translation": "Chúng tôi tìm một chiếc quần xám.",
                        "accepted_answers": [
                                "e",
                                "-e"
                        ]
                }
        },
        {
                "type": "dien_duoi_tinh_tu",
                "question": "Câu 24: Điền đuôi tính từ vào chỗ trống: „Die Kinder brauchen dunkelblau__ Schuhe.“",
                "options": null,
                "correct_answer": "e",
                "explanation": "Danh từ số nhiều không mạo từ ở Akkusativ nhận đuôi -e -> dunkelblaue Schuhe. -> Đáp án: \"e\"",
                "exp_reward": 10,
                "extra_data": {
                        "display_sentence": "Die Kinder brauchen dunkelblau__ Schuhe.",
                        "stem": "dunkelblau",
                        "noun": "die Schuhe",
                        "gender": "pl",
                        "full_sentence": "Die Kinder brauchen dunkelblaue Schuhe.",
                        "translation": "Bọn trẻ cần đôi giày xanh đậm.",
                        "accepted_answers": [
                                "e",
                                "-e"
                        ]
                }
        },
        {
                "type": "dien_duoi_tinh_tu",
                "question": "Câu 25: Điền đuôi tính từ vào chỗ trống: „Ich nehme einen schwarz__ Gürtel.“",
                "options": null,
                "correct_answer": "en",
                "explanation": "der Gürtel là giống đực ở Akkusativ sau einen; tính từ nhận đuôi -en -> einen schwarzen Gürtel. -> Đáp án: \"en\"",
                "exp_reward": 10,
                "extra_data": {
                        "display_sentence": "Ich nehme einen schwarz__ Gürtel.",
                        "stem": "schwarz",
                        "noun": "der Gürtel",
                        "gender": "m",
                        "full_sentence": "Ich nehme einen schwarzen Gürtel.",
                        "translation": "Tôi lấy một chiếc thắt lưng đen.",
                        "accepted_answers": [
                                "en",
                                "-en"
                        ]
                }
        },
        {
                "type": "dien_duoi_tinh_tu",
                "question": "Câu 26: Điền đuôi tính từ vào chỗ trống: „Sie probiert ein braun__ T-Shirt an.“",
                "options": null,
                "correct_answer": "es",
                "explanation": "das T-Shirt là giống trung ở Akkusativ sau ein; tính từ nhận đuôi -es -> ein braunes T-Shirt. -> Đáp án: \"es\"",
                "exp_reward": 10,
                "extra_data": {
                        "display_sentence": "Sie probiert ein braun__ T-Shirt an.",
                        "stem": "braun",
                        "noun": "das T-Shirt",
                        "gender": "n",
                        "full_sentence": "Sie probiert ein braunes T-Shirt an.",
                        "translation": "Cô ấy thử một chiếc áo phông nâu.",
                        "accepted_answers": [
                                "es",
                                "-es"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 27: Dịch sang tiếng Đức (kèm mạo từ số ít): \"áo khoác\"",
                "options": null,
                "correct_answer": "die Jacke",
                "explanation": "Áo khoác trong tiếng Đức là die Jacke (số nhiều: die Jacken). -> Đáp án: \"die Jacke\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "áo khoác = die Jacke",
                        "accepted_answers": [
                                "die Jacke",
                                "Jacke"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 28: Dịch sang tiếng Đức (kèm mạo từ số ít): \"chân váy\"",
                "options": null,
                "correct_answer": "der Rock",
                "explanation": "Chân váy trong tiếng Đức là der Rock (số nhiều: die Röcke). -> Đáp án: \"der Rock\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "chân váy = der Rock",
                        "accepted_answers": [
                                "der Rock",
                                "Rock"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 29: Dịch sang tiếng Đức (kèm mạo từ số ít): \"áo sơ mi nam\"",
                "options": null,
                "correct_answer": "das Hemd",
                "explanation": "Áo sơ mi nam trong tiếng Đức là das Hemd (số nhiều: die Hemden). -> Đáp án: \"das Hemd\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "áo sơ mi nam = das Hemd",
                        "accepted_answers": [
                                "das Hemd",
                                "Hemd"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 30: Dịch sang tiếng Đức (kèm mạo từ số ít): \"thắt lưng\"",
                "options": null,
                "correct_answer": "der Gürtel",
                "explanation": "Thắt lưng trong tiếng Đức là der Gürtel (số nhiều: die Gürtel). -> Đáp án: \"der Gürtel\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "thắt lưng = der Gürtel",
                        "accepted_answers": [
                                "der Gürtel",
                                "Gürtel",
                                "der Guertel",
                                "Guertel"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 31: Dịch sang tiếng Đức (kèm mạo từ số ít): \"sương mù\"",
                "options": null,
                "correct_answer": "der Nebel",
                "explanation": "Sương mù là danh từ giống đực der Nebel; tính từ tương ứng là neblig. -> Đáp án: \"der Nebel\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "sương mù = der Nebel",
                        "accepted_answers": [
                                "der Nebel",
                                "Nebel"
                        ]
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 32: Dịch sang tiếng Đức (kèm mạo từ số ít): \"tuyết\"",
                "options": null,
                "correct_answer": "der Schnee",
                "explanation": "Tuyết là danh từ giống đực der Schnee (chỉ có số ít); động từ tương ứng là schneien. -> Đáp án: \"der Schnee\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "tuyết = der Schnee",
                        "accepted_answers": [
                                "der Schnee",
                                "Schnee"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 33: Dịch sang tiếng Việt: „die Krawatte“",
                "options": null,
                "correct_answer": "cà vạt",
                "explanation": "die Krawatte có nghĩa là cà vạt (số nhiều: die Krawatten). -> Đáp án: \"cà vạt\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "cà vạt",
                        "accepted_answers": [
                                "cà vạt",
                                "chiếc cà vạt",
                                "ca vat",
                                "ca vạt"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 34: Dịch sang tiếng Việt: „der Handschuh“",
                "options": null,
                "correct_answer": "găng tay",
                "explanation": "der Handschuh có nghĩa là găng tay (số nhiều: die Handschuhe). -> Đáp án: \"găng tay\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "găng tay",
                        "accepted_answers": [
                                "găng tay",
                                "chiếc găng tay",
                                "một chiếc găng tay",
                                "gang tay"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 35: Dịch sang tiếng Việt: „bewölkt“",
                "options": null,
                "correct_answer": "nhiều mây",
                "explanation": "bewölkt là tính từ chỉ thời tiết có nghĩa là nhiều mây / có mây. -> Đáp án: \"nhiều mây\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "nhiều mây",
                        "accepted_answers": [
                                "nhiều mây",
                                "có mây",
                                "trời nhiều mây",
                                "nhieu may"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 36: Dịch sang tiếng Việt: „Es ist neblig.“",
                "options": null,
                "correct_answer": "Trời có sương mù.",
                "explanation": "Es ist neblig. có nghĩa là Trời có sương mù. (es là chủ ngữ giả không dịch). -> Đáp án: \"Trời có sương mù.\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Trời có sương mù.",
                        "accepted_answers": [
                                "Trời có sương mù.",
                                "Trời có sương mù",
                                "Có sương mù.",
                                "Có sương mù",
                                "Trời nhiều sương mù.",
                                "Trời sương mù."
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 37: Dịch sang tiếng Việt: „Das steht mir nicht.“",
                "options": null,
                "correct_answer": "Cái này không hợp với tôi.",
                "explanation": "stehen (hợp dáng/phong cách) + Dativ mir; không hợp là Das steht mir nicht. -> Đáp án: \"Cái này không hợp với tôi.\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Cái này không hợp với tôi.",
                        "accepted_answers": [
                                "Cái này không hợp với tôi.",
                                "Cái này không hợp với tôi",
                                "Cái này không hợp tôi.",
                                "Cái này không hợp tôi",
                                "Cái đó không hợp với tôi.",
                                "Cái đó không hợp với tôi"
                        ]
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 38: Dịch sang tiếng Việt: „Die Hose ist mir zu lang.“",
                "options": null,
                "correct_answer": "Chiếc quần này dài quá đối với tôi.",
                "explanation": "zu lang = dài quá; mir (Dativ) = đối với tôi -> Chiếc quần này dài quá đối với tôi. -> Đáp án: \"Chiếc quần này dài quá đối với tôi.\"",
                "exp_reward": 10,
                "extra_data": {
                        "translation": "Chiếc quần này dài quá đối với tôi.",
                        "accepted_answers": [
                                "Chiếc quần này dài quá đối với tôi.",
                                "Chiếc quần này dài quá đối với tôi",
                                "Chiếc quần dài quá đối với tôi.",
                                "Chiếc quần dài quá đối với tôi",
                                "Cái quần dài quá với tôi.",
                                "Quần dài quá đối với tôi."
                        ]
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 39: Nối từ tiếng Đức với nghĩa tiếng Việt tương ứng (Trang phục):",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "der Mantel: áo măng tô | die Socke: tất | der Hut: mũ có vành | die Bluse: áo sơ mi nữ. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Mantel",
                                        "right": "áo măng tô"
                                },
                                {
                                        "left": "die Socke",
                                        "right": "tất"
                                },
                                {
                                        "left": "der Hut",
                                        "right": "mũ"
                                },
                                {
                                        "left": "die Bluse",
                                        "right": "áo sơ mi nữ"
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: der Mantel = áo măng tô; die Socke = tất; der Hut = mũ; die Bluse = áo sơ mi nữ."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 40: Nối danh từ số ít với dạng số nhiều tương ứng:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "der Rock -> die Röcke | die Hose -> die Hosen | das Kleid -> die Kleider | der Schuh -> die Schuhe. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Rock",
                                        "right": "die Röcke"
                                },
                                {
                                        "left": "die Hose",
                                        "right": "die Hosen"
                                },
                                {
                                        "left": "das Kleid",
                                        "right": "die Kleider"
                                },
                                {
                                        "left": "der Schuh",
                                        "right": "die Schuhe"
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: chân váy – những chân váy; quần – những chiếc quần; đầm – những chiếc đầm; giày – những đôi giày."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 41: Nối từ chỉ màu sắc với nghĩa tiếng Việt tương ứng:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "schwarz: đen | grau: ghi / xám | braun: nâu | gelb: vàng. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "schwarz",
                                        "right": "đen"
                                },
                                {
                                        "left": "grau",
                                        "right": "ghi / xám"
                                },
                                {
                                        "left": "braun",
                                        "right": "nâu"
                                },
                                {
                                        "left": "gelb",
                                        "right": "vàng"
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: schwarz = đen; grau = ghi / xám; braun = nâu; gelb = vàng."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 42: Nối danh từ thời tiết với tính từ tương ứng:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "der Nebel -> neblig | der Wind -> windig | die Sonne -> sonnig | die Hitze -> heiß. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Nebel",
                                        "right": "neblig"
                                },
                                {
                                        "left": "der Wind",
                                        "right": "windig"
                                },
                                {
                                        "left": "die Sonne",
                                        "right": "sonnig"
                                },
                                {
                                        "left": "die Hitze",
                                        "right": "heiß"
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: sương mù – có sương mù; gió – có gió; mặt trời – nắng; khí nóng – nóng."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 43: Nối câu tiếng Việt với câu thời tiết tiếng Đức tương ứng:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "Trời mưa -> Es regnet. | Tuyết rơi -> Es schneit. | Trời nhiều mây -> Es ist bewölkt. | Trời nóng -> Es ist heiß. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Trời mưa.",
                                        "right": "Es regnet."
                                },
                                {
                                        "left": "Tuyết rơi.",
                                        "right": "Es schneit."
                                },
                                {
                                        "left": "Trời nhiều mây.",
                                        "right": "Es ist bewölkt."
                                },
                                {
                                        "left": "Trời nóng.",
                                        "right": "Es ist heiß."
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: Trời mưa = Es regnet; Tuyết rơi = Es schneit; Trời nhiều mây = Es ist bewölkt; Trời nóng = Es ist heiß."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 44: Nối danh từ với cụm dies- ở Akkusativ tương ứng:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "der Gürtel -> diesen Gürtel | die Hose -> diese Hose | das Hemd -> dieses Hemd | die Stiefel -> diese Stiefel. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Gürtel",
                                        "right": "diesen Gürtel"
                                },
                                {
                                        "left": "die Hose",
                                        "right": "diese Hose"
                                },
                                {
                                        "left": "das Hemd",
                                        "right": "dieses Hemd"
                                },
                                {
                                        "left": "die Stiefel",
                                        "right": "diese Stiefel"
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: thắt lưng – chiếc thắt lưng này; quần – chiếc quần này; áo sơ mi – chiếc áo sơ mi này; bốt – những đôi bốt này."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 45: Nối ngôi đại từ với dạng đại từ Dativ tương ứng:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "ich -> mir | du -> dir | wir -> uns | sie (họ) -> ihnen. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "ich",
                                        "right": "mir"
                                },
                                {
                                        "left": "du",
                                        "right": "dir"
                                },
                                {
                                        "left": "wir",
                                        "right": "uns"
                                },
                                {
                                        "left": "sie (họ)",
                                        "right": "ihnen"
                                }
                        ],
                        "translation": "Dịch nghĩa các cặp: ich = mir; du = dir; wir = uns; sie (họ) = ihnen."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 46: Nối câu hỏi ở cửa hàng với câu trả lời phù hợp:",
                "options": null,
                "correct_answer": "Nối đúng 4/4 cặp",
                "explanation": "Kann ich Ihnen helfen? ↔ Ich suche einen Pullover. | Passt Ihnen die Hose? ↔ Ja, sie passt gut. | Wie gefällt dir das Hemd? ↔ Es gefällt mir sehr. | Wie viel kostet der Mantel? ↔ Er kostet neunzig Euro. -> Đáp án: \"Nối đúng 4/4 cặp\"",
                "exp_reward": 15,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Kann ich Ihnen helfen?",
                                        "right": "Ich suche einen Pullover."
                                },
                                {
                                        "left": "Passt Ihnen die Hose?",
                                        "right": "Ja, sie passt gut."
                                },
                                {
                                        "left": "Wie gefällt dir das Hemd?",
                                        "right": "Es gefällt mir sehr."
                                },
                                {
                                        "left": "Wie viel kostet der Mantel?",
                                        "right": "Er kostet neunzig Euro."
                                }
                        ],
                        "translation": "Dịch nghĩa: Tôi có thể giúp gì? – Tôi tìm áo len | Quần vừa không? – Có, nó vừa | Bạn thích áo sơ mi không? – Tôi rất thích | Áo măng tô bao nhiêu tiền? – 90 euro."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 47: Điền từ và đuôi tính từ vào chỗ trống: „Heute ___ ich ein rot___ Kleid.“ (Hôm nay tôi mặc một chiếc đầm đỏ.)",
                "options": null,
                "correct_answer": "trage / es",
                "explanation": "Động từ tragen đi với ngôi ich là trage; das Kleid là giống trung nên tính từ nhận đuôi -es -> ein rotes Kleid -> Đáp án: \"trage / es\"",
                "exp_reward": 15,
                "extra_data": {
                        "display_frame": "Heute ___ ich ein rot___ Kleid.",
                        "word_bank_hints": [
                                "trage",
                                "es",
                                "trägst",
                                "en",
                                "tragt"
                        ],
                        "accepted_answers": [
                                "trage / es",
                                "trage/es",
                                "trage / -es",
                                "trage/-es",
                                "trage es"
                        ],
                        "translation": "Hôm nay tôi mặc một chiếc đầm đỏ."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 48: Điền từ và đuôi tính từ vào chỗ trống: „Du ___ einen grün___ Mantel.“ (Bạn mặc một chiếc áo măng tô xanh lá.)",
                "options": null,
                "correct_answer": "trägst / en",
                "explanation": "tragen đi với ngôi du là trägst; der Mantel là giống đực ở Akkusativ nên tính từ nhận đuôi -en -> einen grünen Mantel -> Đáp án: \"trägst / en\"",
                "exp_reward": 15,
                "extra_data": {
                        "display_frame": "Du ___ einen grün___ Mantel.",
                        "word_bank_hints": [
                                "trägst",
                                "en",
                                "trage",
                                "es",
                                "traegst"
                        ],
                        "accepted_answers": [
                                "trägst / en",
                                "trägst/en",
                                "trägst / -en",
                                "trägst/-en",
                                "traegst / en",
                                "traegst/en",
                                "trägst en",
                                "traegst en"
                        ],
                        "translation": "Bạn mặc một chiếc áo măng tô xanh lá."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 49: Điền 2 đại từ vào chỗ trống: „___ Hose hier ist zu lang, aber ___ Hose da passt.“ (Chiếc quần này đây dài quá, nhưng chiếc quần kia thì vừa.)",
                "options": null,
                "correct_answer": "diese / diese",
                "explanation": "die Hose là danh từ giống cái nên đại từ chỉ định ở cả hai vị trí đều là diese -> Diese Hose hier ist zu lang, aber diese Hose da passt. -> Đáp án: \"diese / diese\"",
                "exp_reward": 15,
                "extra_data": {
                        "display_frame": "___ Hose hier ist zu lang, aber ___ Hose da passt.",
                        "word_bank_hints": [
                                "diese",
                                "dieser",
                                "dieses",
                                "diesen"
                        ],
                        "accepted_answers": [
                                "diese / diese",
                                "diese/diese",
                                "Diese / diese",
                                "Diese/diese",
                                "diese diese",
                                "Diese diese"
                        ],
                        "translation": "Chiếc quần này đây dài quá, nhưng chiếc quần kia thì vừa."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 50: Điền 2 từ vào chỗ trống: „Der Pullover ___ mir gut, und die Schuhe ___ mir auch.“ (Chiếc áo len hợp với tôi, và đôi giày cũng hợp với tôi.)",
                "options": null,
                "correct_answer": "steht / stehen",
                "explanation": "der Pullover là danh từ số ít nên chia steht; die Schuhe là danh từ số nhiều nên chia stehen -> Der Pullover steht mir gut, und die Schuhe stehen mir auch. -> Đáp án: \"steht / stehen\"",
                "exp_reward": 15,
                "extra_data": {
                        "display_frame": "Der Pullover ___ mir gut, und die Schuhe ___ mir auch.",
                        "word_bank_hints": [
                                "steht",
                                "stehen",
                                "passt",
                                "passen"
                        ],
                        "accepted_answers": [
                                "steht / stehen",
                                "steht/stehen",
                                "steht stehen"
                        ],
                        "translation": "Chiếc áo len hợp với tôi, và đôi giày cũng hợp với tôi."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 51: Điền 2 từ vào chỗ trống: „Heute ___ es in Hamburg, und es ist ___.“ (Hôm nay ở Hamburg trời mưa và lạnh.)",
                "options": null,
                "correct_answer": "regnet / kalt",
                "explanation": "Động từ thời tiết regnet (ngôi es); sau ist dùng tính từ kalt -> Heute regnet es in Hamburg, und es ist kalt. -> Đáp án: \"regnet / kalt\"",
                "exp_reward": 15,
                "extra_data": {
                        "display_frame": "Heute ___ es in Hamburg, und es ist ___.",
                        "word_bank_hints": [
                                "regnet",
                                "kalt",
                                "schneit",
                                "Kälte",
                                "Regen"
                        ],
                        "accepted_answers": [
                                "regnet / kalt",
                                "regnet/kalt",
                                "regnet kalt"
                        ],
                        "translation": "Hôm nay ở Hamburg trời mưa và lạnh."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 52: Điền 2 từ vào chỗ trống: „Gestern hat es ___ und ich habe einen Mantel ___.“ (Hôm qua trời có tuyết và tôi đã mặc áo măng tô.)",
                "options": null,
                "correct_answer": "geschneit / angezogen",
                "explanation": "schneien ở thì Perfekt là hat geschneit; anziehen ở thì Perfekt là habe angezogen -> Gestern hat es geschneit und ich habe einen Mantel angezogen. -> Đáp án: \"geschneit / angezogen\"",
                "exp_reward": 15,
                "extra_data": {
                        "display_frame": "Gestern hat es ___ und ich habe einen Mantel ___.",
                        "word_bank_hints": [
                                "geschneit",
                                "angezogen",
                                "schneit",
                                "zieht an",
                                "geregnet"
                        ],
                        "accepted_answers": [
                                "geschneit / angezogen",
                                "geschneit/angezogen",
                                "geschneit angezogen"
                        ],
                        "translation": "Hôm qua trời có tuyết và tôi đã mặc áo măng tô."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 53: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "blauen",
                "explanation": "Từ còn thiếu trong audio là 'blauen' (der Pullover giống đực, Akkusativ: einen blauen Pullover). -> Đáp án: \"blauen\"",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Ich trage heute einen blauen Pullover.",
                        "display_sentence": "Ich trage heute einen ___ Pullover.",
                        "hint_vi": "Hôm nay tôi mặc một chiếc áo len xanh.",
                        "accepted_answers": [
                                "blauen"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 54: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "neununddreißig",
                "explanation": "Số 39 đọc là 'neununddreißig' (hoặc nhập chữ số 39). -> Đáp án: \"neununddreißig\"",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Diese Schuhe sind Größe neununddreißig.",
                        "display_sentence": "Diese Schuhe sind Größe ___.",
                        "hint_vi": "Đôi giày này cỡ ba mươi chín.",
                        "accepted_answers": [
                                "neununddreißig",
                                "neununddreissig",
                                "39"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 55: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "neblig",
                "explanation": "Từ còn thiếu là tính từ 'neblig' (có sương mù). -> Đáp án: \"neblig\"",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Es ist heute neblig und kalt.",
                        "display_sentence": "Es ist heute ___ und kalt.",
                        "hint_vi": "Hôm nay trời có sương mù và lạnh.",
                        "accepted_answers": [
                                "neblig"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 56: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "mir",
                "explanation": "Từ còn thiếu là đại từ Dativ 'mir' sau động từ passen -> „Der Mantel passt mir leider nicht.“ -> Đáp án: \"mir\"",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Der Mantel passt mir leider nicht.",
                        "display_sentence": "Der Mantel passt ___ leider nicht.",
                        "hint_vi": "Tiếc là chiếc áo măng tô không vừa với tôi.",
                        "accepted_answers": [
                                "mir"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 57: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Diesen",
                "explanation": "Từ còn thiếu là đại từ chỉ định 'Diesen' thay thế cho Welchen Hut (giống đực, Akkusativ). -> Đáp án: \"Diesen\"",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Welchen Hut möchten Sie? Diesen hier.",
                        "display_sentence": "Welchen Hut möchten Sie? ___ hier.",
                        "hint_vi": "Ngài muốn chiếc mũ nào? Chiếc này đây.",
                        "accepted_answers": [
                                "Diesen",
                                "diesen"
                        ]
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 58: Nghe phát âm câu tiếng Đức và điền từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "heiß",
                "explanation": "Từ còn thiếu trong audio là tính từ 'heiß' (nóng). -> Đáp án: \"heiß\"",
                "exp_reward": 10,
                "extra_data": {
                        "audio_text": "Im Sommer ist es in Vietnam oft sehr heiß.",
                        "display_sentence": "Im Sommer ist es in Vietnam oft sehr ___.",
                        "hint_vi": "Vào mùa hè ở Việt Nam trời thường rất nóng.",
                        "accepted_answers": [
                                "heiß",
                                "heiss"
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 59: Dịch câu sau sang tiếng Đức: \"Hôm nay tôi mặc một chiếc quần màu đen.\"",
                "options": null,
                "correct_answer": "Heute trage ich eine schwarze Hose.",
                "explanation": "die Hose là giống cái, ở Akkusativ tính từ nhận đuôi -e -> một chiếc quần đen là eine schwarze Hose -> Đáp án: \"Heute trage ich eine schwarze Hose.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hôm nay tôi mặc một chiếc quần màu đen.",
                        "accepted_answers": [
                                "Heute trage ich eine schwarze Hose.",
                                "Ich trage heute eine schwarze Hose."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 60: Dịch câu sau sang tiếng Đức: \"Cô ấy mua một chiếc áo sơ mi trắng.\"",
                "options": null,
                "correct_answer": "Sie kauft ein weißes Hemd.",
                "explanation": "das Hemd là giống trung, ở Akkusativ sau ein tính từ nhận đuôi -es -> ein weißes Hemd -> Đáp án: \"Sie kauft ein weißes Hemd.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Cô ấy mua một chiếc áo sơ mi trắng.",
                        "accepted_answers": [
                                "Sie kauft ein weißes Hemd.",
                                "Sie kauft ein weisses Hemd."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 61: Dịch câu sau sang tiếng Đức: \"Tôi lấy chiếc mũ này.\"",
                "options": null,
                "correct_answer": "Ich nehme diesen Hut.",
                "explanation": "der Hut là giống đực, làm tân ngữ trực tiếp của nehmen ở Akkusativ -> diesen Hut -> Đáp án: \"Ich nehme diesen Hut.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Tôi lấy chiếc mũ này.",
                        "accepted_answers": [
                                "Ich nehme diesen Hut.",
                                "Diesen Hut nehme ich."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 62: Dịch câu sau sang tiếng Đức: \"Chiếc áo khoác này rất hợp với bạn.\"",
                "options": null,
                "correct_answer": "Diese Jacke steht dir sehr gut.",
                "explanation": "die Jacke -> Diese Jacke; hợp với bạn dùng động từ stehen + Dativ dir -> Diese Jacke steht dir sehr gut. -> Đáp án: \"Diese Jacke steht dir sehr gut.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Chiếc áo khoác này rất hợp với bạn.",
                        "accepted_answers": [
                                "Diese Jacke steht dir sehr gut.",
                                "Diese Jacke steht dir gut."
                        ]
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 63: Dịch câu sau sang tiếng Đức: \"Hôm nay ở chỗ tôi trời nắng, nhưng ở chỗ bạn trời mưa.\"",
                "options": null,
                "correct_answer": "Bei mir ist es heute sonnig, aber bei dir regnet es.",
                "explanation": "bei đi với Dativ: bei mir / bei dir; trời nắng dùng tính từ sonnig (Es ist sonnig), trời mưa dùng động từ regnen (Es regnet) -> Đáp án: \"Bei mir ist es heute sonnig, aber bei dir regnet es.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hôm nay ở chỗ tôi trời nắng, nhưng ở chỗ bạn trời mưa.",
                        "accepted_answers": [
                                "Bei mir ist es heute sonnig, aber bei dir regnet es.",
                                "Heute ist es bei mir sonnig, aber bei dir regnet es."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 64: Dịch câu sau sang tiếng Việt: „Welche Größe haben Sie? — Ich trage Größe vierzig.“",
                "options": null,
                "correct_answer": "Ngài mặc cỡ nào? — Tôi mặc cỡ bốn mươi.",
                "explanation": "Welche Größe haben Sie? = Ngài mặc kích cỡ nào?; Ich trage Größe 40 = Tôi mặc cỡ 40. -> Đáp án: \"Ngài mặc cỡ nào? — Tôi mặc cỡ bốn mươi.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Ngài mặc cỡ nào? — Tôi mặc cỡ bốn mươi.",
                        "accepted_answers": [
                                "Ngài mặc cỡ nào? — Tôi mặc cỡ bốn mươi.",
                                "Bạn mặc cỡ nào? — Tôi mặc cỡ bốn mươi.",
                                "Ngài mặc cỡ nào? Tôi mặc cỡ bốn mươi.",
                                "Bạn mặc cỡ nào? Tôi mặc cỡ bốn mươi."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 65: Dịch câu sau sang tiếng Việt: „Dieser Mantel ist mir zu groß, aber dieser hier passt mir gut.“",
                "options": null,
                "correct_answer": "Chiếc áo măng tô này rộng quá đối với tôi, nhưng chiếc này đây thì vừa với tôi.",
                "explanation": "Dieser Mantel (chủ ngữ giống đực); zu groß = quá rộng; dieser hier = chiếc này đây; passt mir gut = rất vừa với tôi. -> Đáp án: \"Chiếc áo măng tô này rộng quá đối với tôi, nhưng chiếc này đây thì vừa với tôi.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Chiếc áo măng tô này rộng quá đối với tôi, nhưng chiếc này đây thì vừa với tôi.",
                        "accepted_answers": [
                                "Chiếc áo măng tô này rộng quá đối với tôi, nhưng chiếc này đây thì vừa với tôi.",
                                "Chiếc áo măng tô này tôi mặc rộng quá, nhưng chiếc này đây vừa với tôi.",
                                "Chiếc áo măng tô này rộng quá với tôi, nhưng chiếc này đây vừa với tôi."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 66: Dịch câu sau sang tiếng Việt: „Im Winter trägt mein Vater immer einen Mantel, einen Hut und Handschuhe.“",
                "options": null,
                "correct_answer": "Vào mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay.",
                "explanation": "Động từ tragen dùng chung cho mặc áo, đội mũ và đeo găng tay; immer = luôn luôn. -> Đáp án: \"Vào mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Vào mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay.",
                        "accepted_answers": [
                                "Vào mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay.",
                                "Mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 67: Dịch câu sau sang tiếng Việt: „Heute ist es in Hamburg windig und bewölkt, aber morgen scheint die Sonne.“",
                "options": null,
                "correct_answer": "Hôm nay ở Hamburg trời có gió và nhiều mây, nhưng ngày mai trời sẽ nắng.",
                "explanation": "windig = có gió; bewölkt = nhiều mây; die Sonne scheint = mặt trời chiếu sáng / trời nắng. -> Đáp án: \"Hôm nay ở Hamburg trời có gió và nhiều mây, nhưng ngày mai trời sẽ nắng.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hôm nay ở Hamburg trời có gió và nhiều mây, nhưng ngày mai trời sẽ nắng.",
                        "accepted_answers": [
                                "Hôm nay ở Hamburg trời có gió và nhiều mây, nhưng ngày mai trời sẽ nắng.",
                                "Hôm nay ở Hamburg có gió và nhiều mây, nhưng ngày mai mặt trời sẽ chiếu sáng.",
                                "Hôm nay ở Hamburg trời có gió và nhiều mây, nhưng ngày mai trời nắng."
                        ]
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 68: Dịch câu sau sang tiếng Việt: „Welche Jacke gefällt dir besser? — Diese hier gefällt mir besser.“",
                "options": null,
                "correct_answer": "Chiếc áo khoác nào bạn thích hơn? — Chiếc này đây tôi thích hơn.",
                "explanation": "gefallen + Dativ (dir, mir) có nghĩa là làm ai đó thích; besser là so sánh hơn của gut -> Bạn thích chiếc nào hơn? Chiếc này đây tôi thích hơn. -> Đáp án: \"Chiếc áo khoác nào bạn thích hơn? — Chiếc này đây tôi thích hơn.\"",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Chiếc áo khoác nào bạn thích hơn? — Chiếc này đây tôi thích hơn.",
                        "accepted_answers": [
                                "Chiếc áo khoác nào bạn thích hơn? — Chiếc này đây tôi thích hơn.",
                                "Bạn thích chiếc áo khoác nào hơn? — Tôi thích chiếc này đây hơn.",
                                "Chiếc áo khoác nào bạn thích hơn? Chiếc này đây tôi thích hơn."
                        ]
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 69: Sắp xếp các từ sau thành câu tiếng Đức hoàn chỉnh:",
                "options": null,
                "correct_answer": "Heute trägt er einen blauen Anzug.",
                "explanation": "Động từ chia 'trägt' bắt buộc đứng ở vị trí 2; trạng từ 'Heute' ở vị trí 1 -> đảo chủ ngữ 'er' ra sau động từ -> „Heute trägt er einen blauen Anzug.“. -> Đáp án: \"Heute trägt er einen blauen Anzug.\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "trägt",
                                "Heute",
                                "einen blauen Anzug",
                                "er"
                        ],
                        "accepted_answers": [
                                "Heute trägt er einen blauen Anzug.",
                                "Er trägt heute einen blauen Anzug."
                        ],
                        "translation": "Hôm nay anh ấy mặc một bộ com lê xanh."
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 70: Sắp xếp các từ sau thành câu hỏi tiếng Đức hoàn chỉnh:",
                "options": null,
                "correct_answer": "Welchen Pullover nimmst du?",
                "explanation": "Cụm từ hỏi 'Welchen Pullover' ở vị trí 1, động từ 'nimmst' ở vị trí 2, chủ ngữ 'du' đứng sau động từ -> „Welchen Pullover nimmst du?“. -> Đáp án: \"Welchen Pullover nimmst du?\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "nimmst",
                                "Welchen Pullover",
                                "du"
                        ],
                        "accepted_answers": [
                                "Welchen Pullover nimmst du?"
                        ],
                        "translation": "Bạn lấy chiếc áo len nào?"
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 71: Sắp xếp các từ sau thành câu tiếng Đức hoàn chỉnh:",
                "options": null,
                "correct_answer": "Ich kaufe diesen Gürtel.",
                "explanation": "Chủ ngữ 'Ich' ở vị trí 1, động từ 'kaufe' ở vị trí 2, tân ngữ Akkusativ 'diesen Gürtel' ở vị trí 3 -> „Ich kaufe diesen Gürtel.“. -> Đáp án: \"Ich kaufe diesen Gürtel.\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "kaufe",
                                "Ich",
                                "diesen Gürtel"
                        ],
                        "accepted_answers": [
                                "Ich kaufe diesen Gürtel.",
                                "Diesen Gürtel kaufe ich."
                        ],
                        "translation": "Tôi mua chiếc thắt lưng này."
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 72: Sắp xếp các từ sau thành câu tiếng Đức hoàn chỉnh:",
                "options": null,
                "correct_answer": "Die Schuhe passen mir leider nicht.",
                "explanation": "Chủ ngữ 'Die Schuhe' (số nhiều) đi với động từ 'passen' ở vị trí 2; đại từ Dativ 'mir' đứng trước trạng từ 'leider' và từ phủ định 'nicht' đứng cuối -> „Die Schuhe passen mir leider không.“ -> Đáp án: \"Die Schuhe passen mir leider nicht.\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "passen",
                                "Die Schuhe",
                                "mir",
                                "leider",
                                "nicht"
                        ],
                        "accepted_answers": [
                                "Die Schuhe passen mir leider nicht.",
                                "Leider passen mir die Schuhe nicht."
                        ],
                        "translation": "Tiếc là đôi giày không vừa với tôi."
                }
        },
        {
                "type": "sap_xep_cau",
                "question": "Câu 73: Sắp xếp các từ sau thành câu tiếng Đức hoàn chỉnh:",
                "options": null,
                "correct_answer": "Heute schneit es in Berlin.",
                "explanation": "Trạng từ 'Heute' ở vị trí 1, động từ 'schneit' ở vị trí 2, chủ ngữ giả 'es' đứng ngay sau động từ -> „Heute schneit es in Berlin.“. -> Đáp án: \"Heute schneit es in Berlin.\"",
                "exp_reward": 15,
                "extra_data": {
                        "tokens": [
                                "schneit",
                                "es",
                                "in Berlin",
                                "heute"
                        ],
                        "accepted_answers": [
                                "Heute schneit es in Berlin.",
                                "In Berlin schneit es heute.",
                                "Es schneit heute in Berlin."
                        ],
                        "translation": "Hôm nay ở Berlin tuyết rơi."
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 74: Phân loại mạo từ der / die / das cho 4 danh từ trang phục sau:",
                "options": null,
                "correct_answer": "Mantel: der, Hose: die, Kleid: das, Gürtel: der",
                "explanation": "Mantel và Gürtel là giống đực (der); Hose là giống cái (die Hose đuôi -e); Kleid là giống trung (das Kleid). -> Đáp án: \"Mantel: der, Hose: die, Kleid: das, Gürtel: der\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "word": "Mantel",
                                        "article": "der",
                                        "meaning": "áo măng tô"
                                },
                                {
                                        "word": "Hose",
                                        "article": "die",
                                        "meaning": "quần"
                                },
                                {
                                        "word": "Kleid",
                                        "article": "das",
                                        "meaning": "đầm"
                                },
                                {
                                        "word": "Gürtel",
                                        "article": "der",
                                        "meaning": "thắt lưng"
                                }
                        ],
                        "translation": "Phân loại giống: der Mantel (áo măng tô), die Hose (quần), das Kleid (đầm), der Gürtel (thắt lưng)."
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 75: Phân loại mạo từ der / die / das cho 4 danh từ trang phục sau:",
                "options": null,
                "correct_answer": "Bluse: die, Hemd: das, Schuh: der, Krawatte: die",
                "explanation": "Bluse và Krawatte là giống cái (đuôi -e); Hemd là giống trung (das Hemd); Schuh là giống đực (der Schuh). -> Đáp án: \"Bluse: die, Hemd: das, Schuh: der, Krawatte: die\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "word": "Bluse",
                                        "article": "die",
                                        "meaning": "áo sơ mi nữ"
                                },
                                {
                                        "word": "Hemd",
                                        "article": "das",
                                        "meaning": "áo sơ mi nam"
                                },
                                {
                                        "word": "Schuh",
                                        "article": "der",
                                        "meaning": "giày"
                                },
                                {
                                        "word": "Krawatte",
                                        "article": "die",
                                        "meaning": "cà vạt"
                                }
                        ],
                        "translation": "Phân loại giống: die Bluse (áo sơ mi nữ), das Hemd (áo sơ mi nam), der Schuh (giày), die Krawatte (cà vạt)."
                }
        },
        {
                "type": "phan_loai_giong",
                "question": "Câu 76: Phân loại mạo từ der / die / das cho 4 danh từ thời tiết sau:",
                "options": null,
                "correct_answer": "Regen: der, Sonne: die, Wetter: das, Nebel: der",
                "explanation": "Regen và Nebel là giống đực (der); Sonne là giống cái (die Sonne); Wetter là giống trung (das Wetter). -> Đáp án: \"Regen: der, Sonne: die, Wetter: das, Nebel: der\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "word": "Regen",
                                        "article": "der",
                                        "meaning": "mưa"
                                },
                                {
                                        "word": "Sonne",
                                        "article": "die",
                                        "meaning": "mặt trời"
                                },
                                {
                                        "word": "Wetter",
                                        "article": "das",
                                        "meaning": "thời tiết"
                                },
                                {
                                        "word": "Nebel",
                                        "article": "der",
                                        "meaning": "sương mù"
                                }
                        ],
                        "translation": "Phân loại giống: der Regen (mưa), die Sonne (mặt trời), das Wetter (thời tiết), der Nebel (sương mù)."
                }
        },
        {
                "type": "phan_loai_cach",
                "question": "Câu 77: Xác định cụm in đậm trong mỗi câu sau thuộc Akkusativ hay Dativ:",
                "options": null,
                "correct_answer": "Akkusativ, Dativ, Akkusativ, Dativ",
                "explanation": "Tân ngữ trực tiếp của tragen / suchen là Akkusativ; người sau passen / gefallen là Dativ. -> Đáp án: \"Akkusativ, Dativ, Akkusativ, Dativ\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "sentence": "Ich trage einen Mantel.",
                                        "target_phrase": "einen Mantel",
                                        "case": "Akkusativ",
                                        "reason_vi": "tragen + tân ngữ trực tiếp (giống đực m -> einen)",
                                        "translation_vi": "Tôi mặc một chiếc áo măng tô."
                                },
                                {
                                        "sentence": "Der Hut passt dir.",
                                        "target_phrase": "dir",
                                        "case": "Dativ",
                                        "reason_vi": "passen + Dativ (dir)",
                                        "translation_vi": "Chiếc mũ vừa với bạn."
                                },
                                {
                                        "sentence": "Sie sucht eine Hose.",
                                        "target_phrase": "eine Hose",
                                        "case": "Akkusativ",
                                        "reason_vi": "suchen + tân ngữ trực tiếp Akkusativ (giống cái f -> eine)",
                                        "translation_vi": "Cô ấy tìm một chiếc quần."
                                },
                                {
                                        "sentence": "Die Jacke gefällt ihm.",
                                        "target_phrase": "ihm",
                                        "case": "Dativ",
                                        "reason_vi": "gefallen + Dativ (ihm)",
                                        "translation_vi": "Chiếc áo khoác làm anh ấy thích."
                                }
                        ],
                        "translation": "Hàng 1: Akkusativ | Hàng 2: Dativ | Hàng 3: Akkusativ | Hàng 4: Dativ."
                }
        },
        {
                "type": "phan_loai_cach",
                "question": "Câu 78: Xác định cụm in đậm trong mỗi câu sau thuộc Akkusativ hay Dativ:",
                "options": null,
                "correct_answer": "Akkusativ, Dativ, Akkusativ, Dativ",
                "explanation": "kaufen / anziehen đi với Akkusativ; stehen / gehören đi với Dativ. -> Đáp án: \"Akkusativ, Dativ, Akkusativ, Dativ\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "sentence": "Wir kaufen diesen Pullover.",
                                        "target_phrase": "diesen Pullover",
                                        "case": "Akkusativ",
                                        "reason_vi": "kaufen + Akkusativ (m -> diesen)",
                                        "translation_vi": "Chúng tôi mua chiếc áo len này."
                                },
                                {
                                        "sentence": "Die Stiefel stehen mir gut.",
                                        "target_phrase": "mir",
                                        "case": "Dativ",
                                        "reason_vi": "stehen (hợp dáng) + Dativ (mir)",
                                        "translation_vi": "Đôi bốt rất hợp với tôi."
                                },
                                {
                                        "sentence": "Er zieht einen Anzug an.",
                                        "target_phrase": "einen Anzug",
                                        "case": "Akkusativ",
                                        "reason_vi": "anziehen + Akkusativ (m -> einen)",
                                        "translation_vi": "Anh ấy mặc một bộ com lê vào."
                                },
                                {
                                        "sentence": "Das Kleid gehört meiner Schwester.",
                                        "target_phrase": "meiner Schwester",
                                        "case": "Dativ",
                                        "reason_vi": "gehören + Dativ (giống cái f -> meiner)",
                                        "translation_vi": "Chiếc đầm này là của chị tôi."
                                }
                        ],
                        "translation": "Hàng 1: Akkusativ | Hàng 2: Dativ | Hàng 3: Akkusativ | Hàng 4: Dativ."
                }
        },
        {
                "type": "phan_loai_cach",
                "question": "Câu 79: Xác định cụm in đậm trong mỗi câu sau thuộc Akkusativ hay Dativ:",
                "options": null,
                "correct_answer": "Akkusativ, Akkusativ, Dativ, Dativ",
                "explanation": "Hai hàng chứa màu sắc thuộc cụm tân ngữ Akkusativ (tragen, nehmen); hai hàng Dativ (passen, gehören) không chứa màu sắc. -> Đáp án: \"Akkusativ, Akkusativ, Dativ, Dativ\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "sentence": "Ich trage einen schwarzen Rock.",
                                        "target_phrase": "einen schwarzen Rock",
                                        "case": "Akkusativ",
                                        "reason_vi": "tragen + Akkusativ cụm màu sắc (m -> einen ... -en)",
                                        "translation_vi": "Tôi mặc một chiếc chân váy đen."
                                },
                                {
                                        "sentence": "Du nimmst ein blaues Hemd.",
                                        "target_phrase": "ein blaues Hemd",
                                        "case": "Akkusativ",
                                        "reason_vi": "nehmen + Akkusativ cụm màu sắc (n -> ein ... -es)",
                                        "translation_vi": "Bạn lấy một chiếc áo sơ mi xanh."
                                },
                                {
                                        "sentence": "Der Gürtel passt uns nicht.",
                                        "target_phrase": "uns",
                                        "case": "Dativ",
                                        "reason_vi": "passen + Dativ (uns)",
                                        "translation_vi": "Chiếc thắt lưng không vừa với chúng tôi."
                                },
                                {
                                        "sentence": "Der Schal gehört ihr.",
                                        "target_phrase": "ihr",
                                        "case": "Dativ",
                                        "reason_vi": "gehören + Dativ (ihr)",
                                        "translation_vi": "Chiếc khăn quàng là của cô ấy."
                                }
                        ],
                        "translation": "Hàng 1: Akkusativ | Hàng 2: Akkusativ | Hàng 3: Dativ | Hàng 4: Dativ."
                }
        },
        {
                "type": "phan_loai_cach",
                "question": "Câu 80: Xác định cụm in đậm trong mỗi câu sau thuộc Akkusativ hay Dativ:",
                "options": null,
                "correct_answer": "Dativ, Akkusativ, Dativ, Akkusativ",
                "explanation": "Với động từ schenken: người nhận là Dativ (meinem Bruder), món quà là Akkusativ (einen Gürtel). gefallen đi với Dativ (euch), anprobieren đi với Akkusativ (eine Jacke). -> Đáp án: \"Dativ, Akkusativ, Dativ, Akkusativ\"",
                "exp_reward": 15,
                "extra_data": {
                        "items": [
                                {
                                        "sentence": "Ich schenke meinem Bruder einen Gürtel.",
                                        "target_phrase": "meinem Bruder",
                                        "case": "Dativ",
                                        "reason_vi": "schenken + người nhận ở Dativ (m -> meinem)",
                                        "translation_vi": "Tôi tặng anh trai tôi một chiếc thắt lưng."
                                },
                                {
                                        "sentence": "Ich schenke meinem Bruder einen Gürtel.",
                                        "target_phrase": "einen Gürtel",
                                        "case": "Akkusativ",
                                        "reason_vi": "schenken + món quà ở Akkusativ (m -> einen)",
                                        "translation_vi": "Tôi tặng anh trai tôi một chiếc thắt lưng."
                                },
                                {
                                        "sentence": "Wie gefällt euch der Hut?",
                                        "target_phrase": "euch",
                                        "case": "Dativ",
                                        "reason_vi": "gefallen + Dativ (euch)",
                                        "translation_vi": "Các bạn thấy chiếc mũ này thế nào (có thích không)?"
                                },
                                {
                                        "sentence": "Sie probiert eine Jacke an.",
                                        "target_phrase": "eine Jacke",
                                        "case": "Akkusativ",
                                        "reason_vi": "anprobieren + Akkusativ (f -> eine)",
                                        "translation_vi": "Cô ấy thử một chiếc áo khoác."
                                }
                        ],
                        "translation": "Hàng 1: Dativ | Hàng 2: Akkusativ | Hàng 3: Dativ | Hàng 4: Akkusativ."
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 81: Tìm 1 lỗi sai và gõ lại câu đúng ngữ pháp: „Ich trage einen rote Pullover.“",
                "options": null,
                "correct_answer": "Ich trage einen roten Pullover.",
                "explanation": "Lỗi sai đuôi tính từ: der Pullover là danh từ giống đực ở Akkusativ sau einen, tính từ phải có đuôi -en (roten), không phải rote -> „Ich trage einen roten Pullover.“. -> Đáp án: \"Ich trage einen roten Pullover.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Ich trage einen rote Pullover.",
                        "accepted_answers": [
                                "Ich trage einen roten Pullover."
                        ],
                        "translation": "Tôi mặc một chiếc áo len đỏ."
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 82: Tìm 1 lỗi sai và gõ lại câu đúng ngữ pháp: „Sie trägt eine rosane Bluse.“",
                "options": null,
                "correct_answer": "Sie trägt eine rosa Bluse.",
                "explanation": "Lỗi thêm đuôi cho màu bất biến: màu rosa là từ mượn bất biến, tuyệt đối không thêm đuôi -ne -> „Sie trägt eine rosa Bluse.“. -> Đáp án: \"Sie trägt eine rosa Bluse.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Sie trägt eine rosane Bluse.",
                        "accepted_answers": [
                                "Sie trägt eine rosa Bluse."
                        ],
                        "translation": "Cô ấy mặc một chiếc áo sơ mi nữ màu hồng."
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 83: Tìm 1 lỗi sai và gõ lại câu đúng ngữ pháp: „Ich kaufe dieser Hose.“",
                "options": null,
                "correct_answer": "Ich kaufe diese Hose.",
                "explanation": "Lỗi dạng dies-: die Hose là danh từ giống cái, ở Akkusativ dạng chỉ định là diese, không phải dieser -> „Ich kaufe diese Hose.“. -> Đáp án: \"Ich kaufe diese Hose.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Ich kaufe dieser Hose.",
                        "accepted_answers": [
                                "Ich kaufe diese Hose."
                        ],
                        "translation": "Tôi mua chiếc quần này."
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 84: Tìm 1 lỗi sai và gõ lại câu đúng ngữ pháp: „Die Jacke gefällt ich sehr.“",
                "options": null,
                "correct_answer": "Die Jacke gefällt mir sehr.",
                "explanation": "Lỗi cách của đại từ: động từ gefallen bắt buộc đi với Dativ, Dativ của ich là mir, không dùng ich -> „Die Jacke gefällt mir sehr.“. -> Đáp án: \"Die Jacke gefällt mir rất.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Die Jacke gefällt ich sehr.",
                        "accepted_answers": [
                                "Die Jacke gefällt mir sehr."
                        ],
                        "translation": "Chiếc áo khoác này tôi rất thích."
                }
        },
        {
                "type": "tim_loi_sai",
                "question": "Câu 85: Tìm 1 lỗi sai và gõ lại câu đúng ngữ pháp: „Es ist regnet heute.“",
                "options": null,
                "correct_answer": "Es regnet heute.",
                "explanation": "Lỗi động từ thời tiết: regnen là động từ, không dùng kèm trợ động từ ist -> „Es regnet heute.“ (hoặc Heute regnet es). -> Đáp án: \"Es regnet heute.\"",
                "exp_reward": 15,
                "extra_data": {
                        "wrong_sentence": "Es ist regnet heute.",
                        "accepted_answers": [
                                "Es regnet heute.",
                                "Heute regnet es."
                        ],
                        "translation": "Hôm nay trời mưa."
                }
        },
        {
                "type": "viet_lai_dies",
                "question": "Câu 86: Thay „den Rock“ bằng „dies-“ kèm danh từ: „Ich nehme den Rock.“",
                "options": null,
                "correct_answer": "Ich nehme diesen Rock.",
                "explanation": "den Rock (giống đực m ở Akkusativ) thay bằng diesen Rock -> „Ich nehme diesen Rock.“. -> Đáp án: \"Ich nehme diesen Rock.\"",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Ich nehme den Rock.",
                        "instruction_vi": "Thay „den Rock“ bằng „dies-“ kèm danh từ.",
                        "accepted_answers": [
                                "Ich nehme diesen Rock."
                        ],
                        "translation": "Tôi lấy chiếc chân váy này."
                }
        },
        {
                "type": "viet_lai_dies",
                "question": "Câu 87: Thay „die Bluse“ bằng „dies-“ kèm danh từ: „Sie kauft die Bluse.“",
                "options": null,
                "correct_answer": "Sie kauft diese Bluse.",
                "explanation": "die Bluse (giống cái f ở Akkusativ) thay bằng diese Bluse -> „Sie kauft diese Bluse.“. -> Đáp án: \"Sie kauft diese Bluse.\"",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Sie kauft die Bluse.",
                        "instruction_vi": "Thay „die Bluse“ bằng „dies-“ kèm danh từ.",
                        "accepted_answers": [
                                "Sie kauft diese Bluse."
                        ],
                        "translation": "Cô ấy mua chiếc áo sơ mi nữ này."
                }
        },
        {
                "type": "viet_lai_dies",
                "question": "Câu 88: Thay „das Hemd“ bằng „dies-“ kèm danh từ: „Wir suchen das Hemd.“",
                "options": null,
                "correct_answer": "Wir suchen dieses Hemd.",
                "explanation": "das Hemd (giống trung n ở Akkusativ) thay bằng dieses Hemd -> „Wir suchen dieses Hemd.“. -> Đáp án: \"Wir suchen dieses Hemd.\"",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Wir suchen das Hemd.",
                        "instruction_vi": "Thay „das Hemd“ bằng „dies-“ kèm danh từ.",
                        "accepted_answers": [
                                "Wir suchen dieses Hemd."
                        ],
                        "translation": "Chúng tôi tìm chiếc áo sơ mi nam này."
                }
        },
        {
                "type": "viet_lai_dies",
                "question": "Câu 89: Viết lại câu dùng „dies-“ đứng một mình (bỏ danh từ): „Ich kaufe den Gürtel.“",
                "options": null,
                "correct_answer": "Ich kaufe diesen.",
                "explanation": "den Gürtel là giống đực ở Akkusativ; khi đứng một mình thay thế cho danh từ giống đực thì dùng diesen -> „Ich kaufe diesen.“. -> Đáp án: \"Ich kaufe diesen.\"",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Ich kaufe den Gürtel.",
                        "instruction_vi": "Dùng „dies-“ đứng một mình (bỏ danh từ).",
                        "accepted_answers": [
                                "Ich kaufe diesen."
                        ],
                        "translation": "Tôi mua cái này."
                }
        },
        {
                "type": "viet_lai_dies",
                "question": "Câu 90: Viết lại câu dùng „dies-“ đứng một mình (bỏ danh từ), giữ động từ tách: „Du probierst die Schuhe an.“",
                "options": null,
                "correct_answer": "Du probierst diese an.",
                "explanation": "die Schuhe là số nhiều; đứng một mình là diese; động từ tách probierst ... an giữ nguyên tiền tố an ở cuối câu -> „Du probierst diese an.“. -> Đáp án: \"Du probierst diese an.\"",
                "exp_reward": 15,
                "extra_data": {
                        "source_sentence": "Du probierst die Schuhe an.",
                        "instruction_vi": "Dùng „dies-“ đứng một mình (bỏ danh từ), giữ động từ tách.",
                        "accepted_answers": [
                                "Du probierst diese an."
                        ],
                        "translation": "Bạn thử đôi này."
                }
        },
        {
                "type": "dung_sai",
                "question": "Câu 91: Đọc đoạn văn sau và xác định Đúng (Richtig) hay Sai (Falsch):\n„Lena trägt rote Schuhe.“",
                "options": [
                        "Richtig",
                        "Falsch"
                ],
                "correct_answer": "Richtig",
                "explanation": "Đoạn văn viết: „Sie trägt ein schwarzes Kleid, eine graue Jacke und rote Schuhe.“ -> Lena đi giày đỏ là Đúng (Richtig). -> Đáp án: \"Richtig\"",
                "exp_reward": 10,
                "extra_data": {
                        "reading_text": "Lena geht heute auf eine Party. Sie trägt ein schwarzes Kleid, eine graue Jacke und rote Schuhe. Lenas Bruder Tom trägt einen dunkelblauen Anzug und eine gelbe Krawatte.",
                        "reading_translation": "Hôm nay Lena đi dự một bữa tiệc. Cô ấy mặc một chiếc đầm đen, một chiếc áo khoác xám và đi giày đỏ. Tom, anh trai của Lena, mặc một bộ com lê xanh đậm và thắt một chiếc cà vạt vàng.",
                        "statement": "Lena trägt rote Schuhe.",
                        "translation": "Lena đi giày đỏ. (Đúng)",
                        "accepted_answers": [
                                "Richtig",
                                "Đúng",
                                "dung"
                        ]
                }
        },
        {
                "type": "dung_sai",
                "question": "Câu 92: Đọc đoạn văn sau và xác định Đúng (Richtig) hay Sai (Falsch):\n„Tom trägt eine blaue Krawatte.“",
                "options": [
                        "Richtig",
                        "Falsch"
                ],
                "correct_answer": "Falsch",
                "explanation": "Đoạn văn viết: „Lenas Bruder Tom trägt einen dunkelblauen Anzug und eine gelbe Krawatte.“ -> Tom mặc com lê xanh đậm, còn cà vạt là màu vàng (gelbe Krawatte), không phải cà vạt xanh -> Sai (Falsch). -> Đáp án: \"Falsch\"",
                "exp_reward": 10,
                "extra_data": {
                        "reading_text": "Lena geht heute auf eine Party. Sie trägt ein schwarzes Kleid, eine graue Jacke und rote Schuhe. Lenas Bruder Tom trägt einen dunkelblauen Anzug und eine gelbe Krawatte.",
                        "reading_translation": "Hôm nay Lena đi dự một bữa tiệc. Cô ấy mặc một chiếc đầm đen, một chiếc áo khoác xám và đi giày đỏ. Tom, anh trai của Lena, mặc một bộ com lê xanh đậm và thắt một chiếc cà vạt vàng.",
                        "statement": "Tom trägt eine blaue Krawatte.",
                        "translation": "Tom thắt một chiếc cà vạt xanh. (Sai)",
                        "accepted_answers": [
                                "Falsch",
                                "Sai",
                                "sai"
                        ]
                }
        },
        {
                "type": "dung_sai",
                "question": "Câu 93: Đọc bản tin thời tiết sau và xác định Đúng (Richtig) hay Sai (Falsch):\n„Morgen regnet es in Wien.“",
                "options": [
                        "Richtig",
                        "Falsch"
                ],
                "correct_answer": "Falsch",
                "explanation": "Bản tin thời tiết nêu rõ: „Morgen scheint die Sonne, aber es bleibt kalt.“ -> Ngày mai trời nắng chứ không mưa -> Mệnh đề trời mưa là Sai (Falsch). -> Đáp án: \"Falsch\"",
                "exp_reward": 10,
                "extra_data": {
                        "reading_text": "In Wien ist es heute kalt und neblig. Es sind nur zwei Grad. Morgen scheint die Sonne, aber es bleibt kalt.",
                        "reading_translation": "Hôm nay ở Wien trời lạnh và có sương mù. Chỉ có hai độ. Ngày mai trời nắng, nhưng vẫn lạnh.",
                        "statement": "Morgen regnet es in Wien.",
                        "translation": "Ngày mai ở Wien trời mưa. (Sai)",
                        "accepted_answers": [
                                "Falsch",
                                "Sai",
                                "sai"
                        ]
                }
        },
        {
                "type": "hoi_thoai_sap_xep",
                "question": "Câu 94: Sắp xếp các lượt lời sau thành hội thoại mua sắm áo len hợp lý (chọn theo thứ tự từ 1 đến 6):",
                "options": null,
                "correct_answer": "1, 2, 3, 4, 5, 6",
                "explanation": "Trình tự mua sắm chuẩn: Chào hỏi gợi ý -> Nêu nhu cầu tìm áo len -> Hỏi cỡ -> Báo cỡ 48 -> Cho xem áo và gợi ý thử -> Hỏi phòng thử đồ. -> Đáp án: \"1, 2, 3, 4, 5, 6\"",
                "exp_reward": 15,
                "extra_data": {
                        "correct_order": [
                                1,
                                2,
                                3,
                                4,
                                5,
                                6
                        ],
                        "translation": "Người bán: Xin chào! Ngài tìm món nào cụ thể không ạ? — Khách: Có, tôi tìm một chiếc áo len. — Người bán: Ngài mặc cỡ nào? — Khách: Tôi mặc cỡ bốn mươi tám. — Người bán: Chiếc này đây chúng tôi có cỡ bốn mươi tám. Ngài có muốn thử không? — Khách: Vâng, rất sẵn lòng. Phòng thử đồ ở đâu?",
                        "lines": [
                                {
                                        "id": 1,
                                        "speaker": "Verkäuferin",
                                        "text": "Guten Tag! Suchen Sie etwas Bestimmtes?"
                                },
                                {
                                        "id": 2,
                                        "speaker": "Kunde",
                                        "text": "Ja, ich suche einen Pullover."
                                },
                                {
                                        "id": 3,
                                        "speaker": "Verkäuferin",
                                        "text": "Welche Größe haben Sie?"
                                },
                                {
                                        "id": 4,
                                        "speaker": "Kunde",
                                        "text": "Ich trage Größe achtundvierzig."
                                },
                                {
                                        "id": 5,
                                        "speaker": "Verkäuferin",
                                        "text": "Diesen hier haben wir in achtundvierzig. Wollen Sie ihn anprobieren?"
                                },
                                {
                                        "id": 6,
                                        "speaker": "Kunde",
                                        "text": "Ja, gern. Wo ist die Umkleidekabine?"
                                }
                        ]
                }
        },
        {
                "type": "hoi_thoai_sap_xep",
                "question": "Câu 95: Sắp xếp các lượt lời sau thành hội thoại đổi quần tại cửa hàng (chọn theo thứ tự từ 1 đến 6):",
                "options": null,
                "correct_answer": "1, 2, 3, 4, 5, 6",
                "explanation": "Trình tự: Báo quần không vừa -> Hỏi có phải chật quá -> Báo quần quá dài -> Đề nghị chiếc ngắn hơn -> Thử ưng ý và quyết định lấy -> Báo tổng tiền 49 Euro. -> Đáp án: \"1, 2, 3, 4, 5, 6\"",
                "exp_reward": 15,
                "extra_data": {
                        "correct_order": [
                                1,
                                2,
                                3,
                                4,
                                5,
                                6
                        ],
                        "translation": "Khách nữ: Xin lỗi, tôi đã thử chiếc quần này. Nó không vừa với tôi. — Người bán: Nó chật quá phải không ạ? — Khách nữ: Không, nó dài quá. — Người bán: Vậy bạn lấy chiếc này đây. Nó ngắn hơn. — Khách nữ: Cảm ơn, chiếc này vừa với tôi. Tôi lấy chiếc này. — Người bán: Tổng cộng là bốn mươi chín euro.",
                        "lines": [
                                {
                                        "id": 1,
                                        "speaker": "Kundin",
                                        "text": "Entschuldigung, ich habe diese Hose anprobiert. Sie passt mir nicht."
                                },
                                {
                                        "id": 2,
                                        "speaker": "Verkäufer",
                                        "text": "Ist sie zu klein?"
                                },
                                {
                                        "id": 3,
                                        "speaker": "Kundin",
                                        "text": "Nein, sie ist zu lang."
                                },
                                {
                                        "id": 4,
                                        "speaker": "Verkäufer",
                                        "text": "Dann nehmen Sie diese hier. Sie ist kürzer."
                                },
                                {
                                        "id": 5,
                                        "speaker": "Kundin",
                                        "text": "Danke, die passt mir gut. Die nehme ich."
                                },
                                {
                                        "id": 6,
                                        "speaker": "Verkäufer",
                                        "text": "Das macht neunundvierzig Euro."
                                }
                        ]
                }
        },
        {
                "type": "hoi_thoai_sap_xep",
                "question": "Câu 96: Sắp xếp các lượt lời sau thành cuộc trò chuyện về thời tiết (chọn theo thứ tự từ 1 đến 5):",
                "options": null,
                "correct_answer": "1, 2, 3, 4, 5",
                "explanation": "Trình tự: Chào và hỏi thời tiết chỗ bạn -> Trả lời trời mưa và hỏi lại -> Báo chỗ mình nắng nhưng lạnh -> Gợi ý cần áo măng tô -> Đồng ý và cho biết đeo cả găng tay. -> Đáp án: \"1, 2, 3, 4, 5\"",
                "exp_reward": 15,
                "extra_data": {
                        "correct_order": [
                                1,
                                2,
                                3,
                                4,
                                5
                        ],
                        "translation": "A: Chào Mai, thời tiết chỗ bạn thế nào? — B: Chào Tim! Chỗ mình trời mưa. Còn chỗ bạn? — A: Chỗ bọn mình trời nắng nhưng lạnh. — B: Vậy bạn cần một chiếc áo măng tô. — A: Ừ, mình cũng đeo găng tay.",
                        "lines": [
                                {
                                        "id": 1,
                                        "speaker": "A",
                                        "text": "Hallo Mai, wie ist das Wetter bei dir?"
                                },
                                {
                                        "id": 2,
                                        "speaker": "B",
                                        "text": "Hallo Tim! Bei mir regnet es. Und bei dir?"
                                },
                                {
                                        "id": 3,
                                        "speaker": "A",
                                        "text": "Bei uns scheint die Sonne, aber es ist kalt."
                                },
                                {
                                        "id": 4,
                                        "speaker": "B",
                                        "text": "Dann brauchst du einen Mantel."
                                },
                                {
                                        "id": 5,
                                        "speaker": "A",
                                        "text": "Ja, ich trage auch Handschuhe."
                                }
                        ]
                }
        },
        {
                "type": "bieu_tuong_thoi_tiet",
                "question": "Câu 97: Nhìn biểu tượng thời tiết sau và chọn câu tiếng Đức đúng:",
                "options": [
                        "Es regnet.",
                        "Es schneit.",
                        "Es ist neblig.",
                        "Es ist heiß."
                ],
                "correct_answer": "Es regnet.",
                "explanation": "Biểu tượng đám mây và mưa 🌧️ tương ứng với câu: „Es regnet.“ (Trời mưa). -> Đáp án: \"Es regnet.\"",
                "exp_reward": 10,
                "extra_data": {
                        "weather_icon": "🌧️",
                        "icon_alt_vi": "Mây và mưa",
                        "translation": "Trời mưa.",
                        "accepted_answers": [
                                "Es regnet.",
                                "A"
                        ]
                }
        },
        {
                "type": "bieu_tuong_thoi_tiet",
                "question": "Câu 98: Nhìn biểu tượng thời tiết sau và chọn câu tiếng Đức đúng:",
                "options": [
                        "Es regnet.",
                        "Es ist sonnig.",
                        "Es schneit.",
                        "Es ist windig."
                ],
                "correct_answer": "Es schneit.",
                "explanation": "Biểu tượng bông tuyết ❄️ tương ứng với câu: „Es schneit.“ (Tuyết rơi). -> Đáp án: \"Es schneit.\"",
                "exp_reward": 10,
                "extra_data": {
                        "weather_icon": "❄️",
                        "icon_alt_vi": "Bông tuyết",
                        "translation": "Tuyết rơi.",
                        "accepted_answers": [
                                "Es schneit.",
                                "C"
                        ]
                }
        },
        {
                "type": "bieu_tuong_thoi_tiet",
                "question": "Câu 99: Nhìn biểu tượng thời tiết sau và chọn câu tiếng Đức đúng:",
                "options": [
                        "Es ist bewölkt.",
                        "Es ist windig.",
                        "Es gewittert.",
                        "Es ist kalt."
                ],
                "correct_answer": "Es ist windig.",
                "explanation": "Biểu tượng gió thổi 🌬️ tương ứng với câu: „Es ist windig.“ (Trời có gió). -> Đáp án: \"Es ist windig.\"",
                "exp_reward": 10,
                "extra_data": {
                        "weather_icon": "🌬️",
                        "icon_alt_vi": "Gió thổi",
                        "translation": "Trời có gió.",
                        "accepted_answers": [
                                "Es ist windig.",
                                "B"
                        ]
                }
        },
        {
                "type": "bieu_tuong_thoi_tiet",
                "question": "Câu 100: Nhìn biểu tượng thời tiết sau và chọn câu tiếng Đức đúng:",
                "options": [
                        "Es ist neblig.",
                        "Es ist heiß.",
                        "Es schneit.",
                        "Es ist bewölkt."
                ],
                "correct_answer": "Es ist bewölkt.",
                "explanation": "Biểu tượng đám mây ☁️ tương ứng với câu: „Es ist bewölkt.“ (Trời nhiều mây). -> Đáp án: \"Es ist bewölkt.\"",
                "exp_reward": 10,
                "extra_data": {
                        "weather_icon": "☁️",
                        "icon_alt_vi": "Đám mây",
                        "translation": "Trời nhiều mây.",
                        "accepted_answers": [
                                "Es ist bewölkt.",
                                "D"
                        ]
                }
        }
]

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
    print("✅ Đã khởi tạo thành công Bài 11: 'Kleidung und Wetter' với đầy đủ 9 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 18 dạng!")

if __name__ == "__main__":
    seed_lesson_11()
