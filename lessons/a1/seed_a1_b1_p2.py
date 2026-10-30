import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_1_part_2():
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

    # Xóa dữ liệu cũ của Bài 1 (P2) nếu đã có để cập nhật sạch sẽ, bảo toàn lesson_id
    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 1 (P2)%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    fixed_lesson_id = existing_lesson["id"] if existing_lesson else None
    if fixed_lesson_id:
        cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (fixed_lesson_id,))
        cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (fixed_lesson_id,))
        cursor.execute("DELETE FROM lessons WHERE id = ?;", (fixed_lesson_id,))

    lesson_title = 'Bài 1 (P2): "Kaffee oder Tee - Cà Phê Hoặc Trà"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (6 MỤC CHUẨN ĐẶC TẢ KỸ THUẬT - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 1 (P2) DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Bài Học Giao Tiếp & Ngữ Pháp Cốt Lõi (P2)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 50 phút • ⚡ 600+ EXP
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Kaffee oder Tee? • Đại Từ Nhân Xưng, Chia Động Từ, Gọi Đồ Uống & Thanh Toán Euro (€)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Làm chủ hệ thống Đại từ nhân xưng ở cách 1 (Nominativ), phân biệt 3 chữ <i>sie/Sie</i>; nắm vững quy tắc chia động từ thì Hiện tại (Quy tắc, Gốc <i>-s/-ß/-z</i>, Gốc <i>-t/-d</i>, Biến âm <i>e → i/ie</i>, Bất quy tắc <i>sein/haben</i> và khuyết thiếu <i>möchten</i>); tự tin gọi đồ uống, tùy chọn thành phần đi kèm như đường, sữa, đá (<i>mit/ohne, viel/wenig</i>) và hỏi giá, thanh toán tiền Euro (€) tại quán cà phê/nhà hàng.
                </p>
            </div>
        </div>

        <!-- MỤC 1: HỆ THỐNG ĐẠI TỪ NHÂN XƯNG Ở CÁCH 1 (NOMINATIV) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">1</span>
                <div>
                    <h3 class="text-lg font-black text-slate-900">Hệ Thống Đại Từ Nhân Xưng (Personalpronomen) ở Cách 1 (Nominativ)</h3>
                    <p class="text-xs text-slate-500">Chủ ngữ đóng vai trò thực hiện hành động chính trong câu</p>
                </div>
            </div>

            <p class="text-sm text-slate-600 leading-relaxed">
                Trong tiếng Đức, đại từ nhân xưng là nền tảng để quyết định <b>đuôi chia của động từ</b>. Hãy bấm vào từng đại từ để nghe phát âm chuẩn bản xứ:
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
                <div onclick="speakGerman('ich')" class="cursor-pointer p-4 rounded-2xl bg-slate-50 hover:bg-indigo-50/80 border border-slate-200 hover:border-indigo-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-indigo-700">ich</span>
                        <span class="text-xs text-indigo-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">tôi (ngôi 1 số ít)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Động từ chia đuôi: <b class="text-indigo-600">-e</b> (ich trinke, wohne)</p>
                </div>

                <div onclick="speakGerman('du')" class="cursor-pointer p-4 rounded-2xl bg-slate-50 hover:bg-indigo-50/80 border border-slate-200 hover:border-indigo-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-indigo-700">du</span>
                        <span class="text-xs text-indigo-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">bạn, cậu, em (ngôi 2 số ít thân mật)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Dùng cho bạn bè, người thân, trẻ em. Đuôi: <b class="text-indigo-600">-st</b></p>
                </div>

                <div onclick="speakGerman('er')" class="cursor-pointer p-4 rounded-2xl bg-slate-50 hover:bg-indigo-50/80 border border-slate-200 hover:border-indigo-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-indigo-700">er</span>
                        <span class="text-xs text-indigo-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">anh ấy, ông ấy, nó (giống đực der)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Ngôi 3 số ít giống đực. Đuôi: <b class="text-indigo-600">-t</b></p>
                </div>

                <div onclick="speakGerman('sie')" class="cursor-pointer p-4 rounded-2xl bg-rose-50/80 hover:bg-rose-100/80 border border-rose-200 hover:border-rose-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-rose-700">sie <span class="text-xs font-medium text-rose-600">(số ít)</span></span>
                        <span class="text-xs text-rose-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">cô ấy, bà ấy, nó (giống cái die)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Ngôi 3 số ít giống cái. Đuôi: <b class="text-indigo-600">-t</b></p>
                </div>

                <div onclick="speakGerman('es')" class="cursor-pointer p-4 rounded-2xl bg-slate-50 hover:bg-indigo-50/80 border border-slate-200 hover:border-indigo-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-indigo-700">es</span>
                        <span class="text-xs text-indigo-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">nó (danh từ giống trung das)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Ngôi 3 số ít giống trung. Đuôi: <b class="text-indigo-600">-t</b></p>
                </div>

                <div onclick="speakGerman('wir')" class="cursor-pointer p-4 rounded-2xl bg-slate-50 hover:bg-indigo-50/80 border border-slate-200 hover:border-indigo-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-indigo-700">wir</span>
                        <span class="text-xs text-indigo-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">chúng tôi, chúng ta (ngôi 1 số nhiều)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5"><b>Anna und ich = wir</b>. Đuôi: <b class="text-indigo-600">-en</b></p>
                </div>

                <div onclick="speakGerman('ihr')" class="cursor-pointer p-4 rounded-2xl bg-slate-50 hover:bg-indigo-50/80 border border-slate-200 hover:border-indigo-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-indigo-700">ihr</span>
                        <span class="text-xs text-indigo-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">các bạn (ngôi 2 số nhiều thân mật)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Hỏi trực tiếp <b>Anna und Peter = ihr</b>. Đuôi: <b class="text-indigo-600">-t</b></p>
                </div>

                <div onclick="speakGerman('sie')" class="cursor-pointer p-4 rounded-2xl bg-purple-50/80 hover:bg-purple-100/80 border border-purple-200 hover:border-purple-400 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-purple-700">sie <span class="text-xs font-medium text-purple-600">(số nhiều)</span></span>
                        <span class="text-xs text-purple-600 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">họ, chúng nó (ngôi 3 số nhiều)</p>
                    <p class="text-[11px] text-slate-500 mt-0.5">Ngôi 3 số nhiều. Đuôi: <b class="text-indigo-600">-en</b></p>
                </div>

                <div onclick="speakGerman('Sie')" class="cursor-pointer p-4 rounded-2xl bg-amber-50/90 hover:bg-amber-100/90 border border-amber-300 hover:border-amber-500 transition group flex flex-col justify-between">
                    <div class="flex items-center justify-between">
                        <span class="text-xl font-black text-amber-800">Sie <span class="text-xs font-medium text-amber-700">(Viết hoa S)</span></span>
                        <span class="text-xs text-amber-700 group-hover:scale-110 transition">🔊</span>
                    </div>
                    <p class="text-xs font-bold text-slate-800 mt-1">Ngài / các Ngài / Ông / Bà (ngôi 2 lịch sự)</p>
                    <p class="text-[11px] text-amber-800 mt-0.5 font-semibold">Luôn viết hoa <b>S</b> ở mọi vị trí! Đuôi: <b>-en</b></p>
                </div>
            </div>

            <!-- Khung phân biệt 3 chữ sie/Sie -->
            <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-200/90 text-xs sm:text-sm text-slate-700 space-y-2">
                <p class="font-extrabold text-amber-900 flex items-center gap-1.5">
                    ⚠️ Mẹo Phân Biệt Tuyệt Đối 3 Chữ "sie / Sie" Trong Đề Thi:
                </p>
                <ul class="list-disc pl-5 space-y-1 text-slate-700">
                    <li><b>sie (cô ấy)</b>: Đi với động từ chia đuôi <b>-t</b> (ví dụ: <i>sie kommt, sie trinkt, sie ist</i>).</li>
                    <li><b>sie (họ)</b>: Đi với động từ chia đuôi <b>-en</b> (ví dụ: <i>sie kommen, sie trinken, sie sind</i>).</li>
                    <li><b>Sie (Ngài - lịch sự)</b>: Luôn viết hoa chữ <b>S</b> ở mọi vị trí (đầu, giữa hay cuối câu), động từ chia đuôi <b>-en</b> (ví dụ: <i>Was trinken Sie?</i>).</li>
                </ul>
            </div>
        </div>

        <!-- MỤC 2: CẤU TẠO ĐỘNG TỪ & QUY TẮC CHIA CÓ QUY TẮC -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">2</span>
                <div>
                    <h3 class="text-lg font-black text-slate-900">Cấu Tạo Động Từ & Quy Tắc Chia Đuôi Chuẩn Ở Thì Hiện Tại (Präsens)</h3>
                    <p class="text-xs text-slate-500">Công thức chia đuôi tiêu chuẩn ở thì Hiện tại (Präsens) và Quy tắc Vị trí số 2 (Position 2)</p>
                </div>
            </div>

            <div class="p-4 rounded-2xl bg-indigo-50/60 border border-indigo-200 text-xs sm:text-sm text-slate-800 space-y-2">
                <p class="font-bold text-indigo-900">1. Động từ nguyên mẫu (Infinitiv) = Gốc động từ (Verbstamm) + Đuôi nguyên mẫu (-en / -n):</p>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-center font-mono font-bold text-xs">
                    <div class="p-2 bg-white rounded-xl border border-indigo-200">mach|en → <span class="text-indigo-600">mach-</span></div>
                    <div class="p-2 bg-white rounded-xl border border-indigo-200">wohn|en → <span class="text-indigo-600">wohn-</span></div>
                    <div class="p-2 bg-white rounded-xl border border-indigo-200">komm|en → <span class="text-indigo-600">komm-</span></div>
                    <div class="p-2 bg-white rounded-xl border border-indigo-200">trink|en → <span class="text-indigo-600">trink-</span></div>
                </div>
            </div>

            <!-- Bảng công thức chia chuẩn -->
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 border-b border-slate-200">
                            <th class="p-3 font-extrabold">Đại từ (Chủ ngữ)</th>
                            <th class="p-3 font-extrabold">Đuôi chia</th>
                            <th class="p-3 font-extrabold">machen (làm)</th>
                            <th class="p-3 font-extrabold">wohnen (sống)</th>
                            <th class="p-3 font-extrabold">kommen (đến)</th>
                            <th class="p-3 font-extrabold">trinken (uống)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">ich</td>
                            <td class="p-3 font-mono font-extrabold text-amber-700 bg-amber-50/60">-e</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ich mache')">mach<b class="text-amber-700">e</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ich wohne')">wohn<b class="text-amber-700">e</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ich komme')">komm<b class="text-amber-700">e</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ich trinke')">trink<b class="text-amber-700">e</b> 🔊</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">du</td>
                            <td class="p-3 font-mono font-extrabold text-amber-700 bg-amber-50/60">-st</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('du machst')">mach<b class="text-amber-700">st</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('du wohnst')">wohn<b class="text-amber-700">st</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('du kommst')">komm<b class="text-amber-700">st</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('du trinkst')">trink<b class="text-amber-700">st</b> 🔊</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">er / sie / es</td>
                            <td class="p-3 font-mono font-extrabold text-amber-700 bg-amber-50/60">-t</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('er macht')">mach<b class="text-amber-700">t</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('er wohnt')">wohn<b class="text-amber-700">t</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('er kommt')">komm<b class="text-amber-700">t</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('er trinkt')">trink<b class="text-amber-700">t</b> 🔊</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">wir</td>
                            <td class="p-3 font-mono font-extrabold text-amber-700 bg-amber-50/60">-en</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('wir machen')">mach<b class="text-amber-700">en</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('wir wohnen')">wohn<b class="text-amber-700">en</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('wir kommen')">komm<b class="text-amber-700">en</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('wir trinken')">trink<b class="text-amber-700">en</b> 🔊</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">ihr</td>
                            <td class="p-3 font-mono font-extrabold text-amber-700 bg-amber-50/60">-t</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ihr macht')">mach<b class="text-amber-700">t</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ihr wohnt')">wohn<b class="text-amber-700">t</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ihr kommt')">komm<b class="text-amber-700">t</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('ihr trinkt')">trink<b class="text-amber-700">t</b> 🔊</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">sie / Sie</td>
                            <td class="p-3 font-mono font-extrabold text-amber-700 bg-amber-50/60">-en</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('sie machen')">mach<b class="text-amber-700">en</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('sie wohnen')">wohn<b class="text-amber-700">en</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('sie kommen')">komm<b class="text-amber-700">en</b> 🔊</td>
                            <td class="p-3 font-semibold cursor-pointer" onclick="speakGerman('sie trinken')">trink<b class="text-amber-700">en</b> 🔊</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Quy tắc vị trí động từ Position 2 -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-xs sm:text-sm text-slate-700 space-y-1.5">
                <p class="font-extrabold text-slate-900">📌 Quy tắc Vị trí số 2 (Position 2):</p>
                <p>Trong câu trần thuật và câu hỏi có từ để hỏi (W-Frage), động từ đã chia theo chủ ngữ <b>luôn luôn đứng ở vị trí thành phần thứ 2 trong câu</b> (tính theo cụm thành phần câu, không đếm theo từng từ đơn lẻ):</p>
                <div class="flex flex-wrap gap-2 pt-1 font-mono text-xs font-bold">
                    <span class="px-2.5 py-1 rounded-lg bg-white border border-slate-200">Ich [1] <b class="text-indigo-600">komme [2]</b> aus Vietnam.</span>
                    <span class="px-2.5 py-1 rounded-lg bg-white border border-slate-200">Wo [1] <b class="text-indigo-600">wohnen [2]</b> Sie?</span>
                </div>
            </div>
        </div>

        <!-- MỤC 3: HAI TRƯỜNG HỢP ĐẶC BIỆT KHI CHIA (-s/-ß/-z & -t/-d) KÈM HỘI THOẠI -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">3</span>
                <div>
                    <h3 class="text-lg font-black text-slate-900">Hai Trường Hợp Đặc Biệt Về Phát Âm Khi Chia Động Từ (-s, -ß, -z & -t, -d)</h3>
                    <p class="text-xs text-slate-500">Tránh líu lưỡi và giữ ngữ điệu chuẩn xác của người Đức</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Nhóm 1: -s, -ß, -z -->
                <div class="p-5 rounded-2xl bg-purple-50/60 border border-purple-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="font-black text-sm text-purple-900">1. Gốc kết thúc -s, -ß, -z, -x</span>
                        <span class="text-xs font-mono px-2 py-0.5 rounded bg-purple-200 text-purple-900 font-bold">heißen, tanzen</span>
                    </div>
                    <p class="text-xs text-slate-700 leading-relaxed">
                        Vì gốc động từ đã kết thúc bằng nhóm âm xuýt (/s/, /z/, /ts/, /ks/), ở ngôi <b>du</b> ta <b>chỉ thêm -t</b> (không thêm -st). Do đó, ngôi <b>du, er/sie/es và ihr</b> có cách viết giống hệt nhau:
                    </p>
                    <div class="bg-white p-3 rounded-xl border border-purple-200 text-xs font-mono space-y-1">
                        <div>ich <b>heiße</b> | <b>tanze</b></div>
                        <div>du <b class="text-purple-700">heißt</b> | <b class="text-purple-700">tanzt</b> <span class="text-slate-400 font-sans">(chỉ thêm -t!)</span></div>
                        <div>er/sie/es <b class="text-purple-700">heißt</b> | <b class="text-purple-700">tanzt</b></div>
                        <div>wir <b>heißen</b> | <b>tanzen</b></div>
                        <div>ihr <b class="text-purple-700">heißt</b> | <b class="text-purple-700">tanzt</b></div>
                        <div>sie/Sie <b>heißen</b> | <b>tanzen</b></div>
                    </div>
                </div>

                <!-- Nhóm 2: -t, -d -->
                <div class="p-5 rounded-2xl bg-emerald-50/60 border border-emerald-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="font-black text-sm text-emerald-900">2. Gốc kết thúc -t, -d</span>
                        <span class="text-xs font-mono px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 font-bold">mieten, arbeiten</span>
                    </div>
                    <p class="text-xs text-slate-700 leading-relaxed">
                        Để đọc rõ âm đuôi, ta <b>chèn thêm nguyên âm -e-</b> ở ngôi <b>du (-est)</b>, <b>er/sie/es (-et)</b> và <b>ihr (-et)</b>:
                    </p>
                    <div class="bg-white p-3 rounded-xl border border-emerald-200 text-xs font-mono space-y-1">
                        <div>ich <b>miete</b> | <b>arbeite</b></div>
                        <div>du <b class="text-emerald-700">mietest</b> | <b class="text-emerald-700">arbeitest</b> <span class="text-slate-400 font-sans">(thêm -e-)</span></div>
                        <div>er/sie/es <b class="text-emerald-700">mietet</b> | <b class="text-emerald-700">arbeitet</b></div>
                        <div>wir <b>mieten</b> | <b>arbeiten</b></div>
                        <div>ihr <b class="text-emerald-700">mietet</b> | <b class="text-emerald-700">arbeitet</b> <span class="text-slate-400 font-sans">(thêm -e-)</span></div>
                        <div>sie/Sie <b>mieten</b> | <b>arbeiten</b></div>
                    </div>
                </div>
            </div>

            <!-- 2 Bài hội thoại mẫu tương tác có audio -->
            <div class="space-y-3 pt-2">
                <h4 class="text-sm font-extrabold text-slate-900 flex items-center gap-2">
                    🗣️ Hội Thoại Mẫu Thực Tế (Bấm để nghe phát âm từng câu):
                </h4>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Hội thoại 1: Marc, Anna, Peter -->
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs">
                        <div class="font-bold text-slate-900 pb-1 border-b border-slate-200 flex items-center justify-between">
                            <span>Hội thoại 1: Quê quán, nơi ở & làm việc</span>
                            <span class="text-[11px] text-indigo-600 font-semibold">Marc, Anna, Peter</span>
                        </div>
                        <div onclick="speakGerman('Woher kommst du?')" class="cursor-pointer p-2 rounded-lg hover:bg-indigo-50 transition flex justify-between items-center">
                            <span><b>Marc:</b> Woher kommst du? <i>(Bạn đến từ đâu?)</i></span>
                            <span class="text-indigo-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Ich komme aus Brasilien. Das ist mein Freund Peter, er kommt aus Russland.')" class="cursor-pointer p-2 rounded-lg hover:bg-indigo-50 transition flex justify-between items-center">
                            <span><b>Anna:</b> Ich komme aus Brasilien. Das ist mein Freund Peter, er kommt aus Russland. <i>(Mình đến từ Brazil. Đây là bạn trai mình, Peter, anh ấy đến từ Nga.)</i></span>
                            <span class="text-indigo-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Und wo wohnt ihr?')" class="cursor-pointer p-2 rounded-lg hover:bg-indigo-50 transition flex justify-between items-center">
                            <span><b>Marc:</b> Und wo wohnt ihr? <i>(Và hai bạn sống ở đâu?)</i></span>
                            <span class="text-indigo-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Wir wohnen in Berlin. Wo arbeitest du?')" class="cursor-pointer p-2 rounded-lg hover:bg-indigo-50 transition flex justify-between items-center">
                            <span><b>Anna:</b> Wir wohnen in Berlin. Wo arbeitest du? <i>(Chúng mình sống ở Berlin. Còn bạn làm việc ở đâu?)</i></span>
                            <span class="text-indigo-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Ich arbeite bei der Post.')" class="cursor-pointer p-2 rounded-lg hover:bg-indigo-50 transition flex justify-between items-center">
                            <span><b>Marc:</b> Ich arbeite bei der Post. <i>(Mình làm việc tại bưu điện.)</i></span>
                            <span class="text-indigo-600">🔊</span>
                        </div>
                    </div>

                    <!-- Hội thoại 2: Lịch sự với Frau / Herr -->
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs">
                        <div class="font-bold text-slate-900 pb-1 border-b border-slate-200 flex items-center justify-between">
                            <span>Hội thoại 2: Giao tiếp lịch sự (ngôi Sie)</span>
                            <span class="text-[11px] text-amber-700 font-semibold">Frau Bui & Herr Nguyen</span>
                        </div>
                        <div onclick="speakGerman('Guten Tag, wie heißen Sie?')" class="cursor-pointer p-2 rounded-lg hover:bg-amber-50 transition flex justify-between items-center">
                            <span><b>Frau Bui:</b> Guten Tag, wie heißen Sie? <i>(Xin chào, tên Ngài là gì ạ?)</i></span>
                            <span class="text-amber-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Ich heiße Dat Nguyen.')" class="cursor-pointer p-2 rounded-lg hover:bg-amber-50 transition flex justify-between items-center">
                            <span><b>Herr Nguyen:</b> Ich heiße Dat Nguyen. <i>(Tôi tên là Đạt Nguyễn.)</i></span>
                            <span class="text-amber-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Woher kommen Sie?')" class="cursor-pointer p-2 rounded-lg hover:bg-amber-50 transition flex justify-between items-center">
                            <span><b>Frau Bui:</b> Woher kommen Sie? <i>(Ngài đến từ đâu ạ?)</i></span>
                            <span class="text-amber-600">🔊</span>
                        </div>
                        <div onclick="speakGerman('Ich komme aus Vietnam.')" class="cursor-pointer p-2 rounded-lg hover:bg-amber-50 transition flex justify-between items-center">
                            <span><b>Herr Nguyen:</b> Ich komme aus Vietnam. <i>(Tôi đến từ Việt Nam.)</i></span>
                            <span class="text-amber-600">🔊</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- MỤC 4: BẤT QUY TẮC CỐT LÕI (SEIN, HABEN) & BIẾN ÂM (LESEN, NEHMEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">4</span>
                <div>
                    <h3 class="text-lg font-black text-slate-900">Động Từ Bất Quy Tắc Cốt Lõi (sein, haben) & Động Từ Biến Âm (lesen, nehmen)</h3>
                    <p class="text-xs text-slate-500">Các động từ tần suất xuất hiện cao nhất trong kỳ thi Goethe / TELC A1</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <!-- Bảng sein & haben -->
                <div class="p-5 rounded-2xl bg-indigo-50/60 border border-indigo-200 space-y-3">
                    <h4 class="font-extrabold text-sm text-indigo-900">1. sein (thì, là, ở) & haben (có)</h4>
                    <div class="overflow-x-auto">
                        <table class="w-full text-xs font-mono text-left">
                            <thead>
                                <tr class="text-slate-500 border-b border-indigo-200">
                                    <th class="pb-1.5 font-bold">Ngôi</th>
                                    <th class="pb-1.5 font-bold text-indigo-700">sein</th>
                                    <th class="pb-1.5 font-bold text-amber-700">haben</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-indigo-100 font-bold">
                                <tr><td class="py-1">ich</td><td class="text-indigo-700">bin</td><td class="text-amber-700">habe</td></tr>
                                <tr><td class="py-1">du</td><td class="text-indigo-700">bist</td><td class="text-amber-700">hast <span class="text-[10px] text-slate-400 font-sans">(bỏ b)</span></td></tr>
                                <tr><td class="py-1">er/sie/es</td><td class="text-indigo-700">ist</td><td class="text-amber-700">hat <span class="text-[10px] text-slate-400 font-sans">(bỏ b)</span></td></tr>
                                <tr><td class="py-1">wir</td><td class="text-indigo-700">sind</td><td class="text-amber-700">haben</td></tr>
                                <tr><td class="py-1">ihr</td><td class="text-indigo-700">seid</td><td class="text-amber-700">habt</td></tr>
                                <tr><td class="py-1">sie/Sie</td><td class="text-indigo-700">sind</td><td class="text-amber-700">haben</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Bảng lesen & nehmen -->
                <div class="p-5 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-3">
                    <h4 class="font-extrabold text-sm text-amber-900">2. Biến âm e → ie / i (lesen, nehmen)</h4>
                    <p class="text-[11px] text-slate-600">
                        ⚡ <b>Lưu ý cốt lõi:</b> Chỉ biến âm ở ngôi thứ 2 và thứ 3 số ít (<b>du, er/sie/es</b>)!
                    </p>
                    <div class="overflow-x-auto">
                        <table class="w-full text-xs font-mono text-left">
                            <thead>
                                <tr class="text-slate-500 border-b border-amber-200">
                                    <th class="pb-1.5 font-bold">Ngôi</th>
                                    <th class="pb-1.5 font-bold text-amber-800">lesen (đọc)</th>
                                    <th class="pb-1.5 font-bold text-amber-800">nehmen (chọn/dùng)</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-amber-100 font-bold">
                                <tr><td class="py-1">ich</td><td>lese</td><td>nehme</td></tr>
                                <tr><td class="py-1">du</td><td class="text-rose-600">liest <span class="text-[10px] text-slate-400 font-sans">(chỉ +t)</span></td><td class="text-rose-600">nimmst <span class="text-[10px] text-slate-400 font-sans">(bỏ h, gấp đôi m)</span></td></tr>
                                <tr><td class="py-1">er/sie/es</td><td class="text-rose-600">liest</td><td class="text-rose-600">nimmt <span class="text-[10px] text-slate-400 font-sans">(bỏ h, gấp đôi m)</span></td></tr>
                                <tr><td class="py-1">wir</td><td>lesen</td><td>nehmen</td></tr>
                                <tr><td class="py-1">ihr</td><td>lest</td><td>nehmt</td></tr>
                                <tr><td class="py-1">sie/Sie</td><td>lesen</td><td>nehmen</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Đoạn văn mẫu thực hành Café Kafka & Deutschkurs -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-xs sm:text-sm text-slate-700 space-y-2">
                <p class="font-bold text-slate-900">☕ Đoạn tin nhắn thực tế tại Café Kafka (Luyện phản xạ 'sein'):</p>
                <div onclick="speakGerman('Hi, Anna und ich sind im Café Kafka. Wo bist du? Maria ist auch da. Kommst du auch?')" class="cursor-pointer p-3 rounded-xl bg-white border border-slate-200 hover:border-indigo-400 transition flex justify-between items-start">
                    <span>
                        <i>"Hi, Anna und ich <b>sind</b> im Café Kafka. Wo <b>bist</b> du? Maria <b>ist</b> auch da. Kommst du auch?"</i><br>
                        <span class="text-slate-500 text-xs">Chào, Anna và tôi đang ở quán Café Kafka. Bạn đang ở đâu? Maria cũng ở đây. Bạn cũng đến chứ?</span>
                    </span>
                    <span class="text-indigo-600 ml-2">🔊</span>
                </div>
                <div onclick="speakGerman('Ach, ihr seid im Café Kafka! Ich bin im Deutschkurs. Die Lehrerin ist nett, sie ist aus den USA.')" class="cursor-pointer p-3 rounded-xl bg-white border border-slate-200 hover:border-indigo-400 transition flex justify-between items-start">
                    <span>
                        <i>"Ach, ihr <b>seid</b> im Café Kafka! Ich <b>bin</b> im Deutschkurs. Die Lehrerin <b>ist</b> nett, sie <b>ist</b> aus den USA."</i><br>
                        <span class="text-slate-500 text-xs">A, các bạn đang ở quán Café Kafka à! Tôi đang ở lớp học tiếng Đức. Cô giáo rất thân thiện, cô ấy đến từ Mỹ.</span>
                    </span>
                    <span class="text-indigo-600 ml-2">🔊</span>
                </div>
            </div>
        </div>

        <!-- MỤC 5: ĐỘNG TỪ KHUYẾT THIẾU MÖCHTEN & CẤU TRÚC KHUNG CÂU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">5</span>
                <div>
                    <h3 class="text-lg font-black text-slate-900">Động Từ Khuyết Thiếu möchten (Muốn Lịch Sự) & Khung Câu (Satzklammer)</h3>
                    <p class="text-xs text-slate-500">Mẫu câu tiêu chuẩn khi gọi đồ uống và thanh toán</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h4 class="font-extrabold text-sm text-slate-900">Bảng chia 'möchten'</h4>
                    <ul class="text-xs font-mono space-y-1 divide-y divide-slate-100">
                        <li class="py-1">ich <b class="text-indigo-600">möchte</b> <span class="text-[11px] text-slate-400 font-sans">(không có -t)</span></li>
                        <li class="py-1">du <b class="text-indigo-600">möchtest</b></li>
                        <li class="py-1">er/sie/es <b class="text-rose-600">möchte</b> <span class="text-[11px] text-rose-500 font-sans font-bold">(KHÔNG có -t!)</span></li>
                        <li class="py-1">wir <b class="text-indigo-600">möchten</b></li>
                        <li class="py-1">ihr <b class="text-indigo-600">möchtet</b></li>
                        <li class="py-1">sie/Sie <b class="text-indigo-600">möchten</b></li>
                    </ul>
                    <p class="text-[11px] text-slate-500 pt-1">💡 <b>Bản chất:</b> <i>'möchten'</i> là dạng giả định lịch sự (Konjunktiv II) của động từ <i>'mögen'</i>, được sử dụng với cấu trúc giống hệt động từ khuyết thiếu. Khi ngữ cảnh gọi món đã rõ, có thể lược bỏ động từ thường ở cuối câu (VD: <i>Möchten Sie Kaffee mit Milch?</i>).</p>
                </div>

                <div class="p-5 rounded-2xl bg-indigo-50/60 border border-indigo-200 space-y-3 text-xs sm:text-sm">
                    <h4 class="font-extrabold text-indigo-900">Cấu trúc khung câu (Satzklammer):</h4>
                    <p class="text-slate-700 leading-relaxed">
                        Khi có <b>möchten</b> đi kèm động từ hành động khác, <b>möchten đứng ở vị trí số 2</b>, động từ chính <b>đẩy về CUỐI CÂU và giữ nguyên mẫu (-en)</b>:
                    </p>
                    <div class="space-y-1.5 font-mono text-xs">
                        <div class="p-2 rounded-lg bg-white border border-indigo-200">
                            Was <b class="text-indigo-700">möchten</b> Sie <b class="text-amber-700">trinken</b>?
                        </div>
                        <div class="p-2 rounded-lg bg-white border border-indigo-200">
                            Ich <b class="text-indigo-700">möchte</b> Kakao <b class="text-amber-700">trinken</b>.
                        </div>
                        <div class="p-2 rounded-lg bg-white border border-indigo-200">
                            Wir <b class="text-indigo-700">möchten</b> bitte <b class="text-amber-700">zahlen</b>.
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- MỤC 6: TỪ VỰNG ĐỒ UỐNG, THÀNH PHẦN ĐI KÈM, CÁCH HỎI GIÁ & THANH TOÁN TIỀN EURO -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">6</span>
                <div>
                    <h3 class="text-lg font-black text-slate-900">Từ Vựng Đồ Uống, Thành Phần Đi Kèm, Cách Gọi Món & Thanh Toán Euro (€)</h3>
                    <p class="text-xs text-slate-500">Kỹ năng thực chiến tại quán cà phê ở Đức, Áo và Thụy Sĩ</p>
                </div>
            </div>

            <!-- Lưới đồ uống & mạo từ -->
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                <div onclick="speakGerman('der Kaffee')" class="cursor-pointer p-3 rounded-2xl bg-blue-50/60 border border-blue-200 hover:border-blue-400 transition">
                    <span class="px-2 py-0.5 rounded bg-blue-600 text-white font-black text-[10px]">der</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">der Kaffee</p>
                    <p class="text-slate-500 text-[11px]">cà phê 🔊</p>
                </div>
                <div onclick="speakGerman('der Tee')" class="cursor-pointer p-3 rounded-2xl bg-blue-50/60 border border-blue-200 hover:border-blue-400 transition">
                    <span class="px-2 py-0.5 rounded bg-blue-600 text-white font-black text-[10px]">der</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">der Tee</p>
                    <p class="text-slate-500 text-[11px]">trà 🔊</p>
                </div>
                <div onclick="speakGerman('die Milch')" class="cursor-pointer p-3 rounded-2xl bg-rose-50/60 border border-rose-200 hover:border-rose-400 transition">
                    <span class="px-2 py-0.5 rounded bg-rose-600 text-white font-black text-[10px]">die</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">die Milch</p>
                    <p class="text-slate-500 text-[11px]">sữa 🔊</p>
                </div>
                <div onclick="speakGerman('der Zucker')" class="cursor-pointer p-3 rounded-2xl bg-blue-50/60 border border-blue-200 hover:border-blue-400 transition">
                    <span class="px-2 py-0.5 rounded bg-blue-600 text-white font-black text-[10px]">der</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">der Zucker</p>
                    <p class="text-slate-500 text-[11px]">đường 🔊</p>
                </div>
                <div onclick="speakGerman('das Wasser')" class="cursor-pointer p-3 rounded-2xl bg-emerald-50/60 border border-emerald-200 hover:border-emerald-400 transition">
                    <span class="px-2 py-0.5 rounded bg-emerald-600 text-white font-black text-[10px]">das</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">das Wasser</p>
                    <p class="text-slate-500 text-[11px]">nước lọc 🔊</p>
                </div>
                <div onclick="speakGerman('die Cola')" class="cursor-pointer p-3 rounded-2xl bg-rose-50/60 border border-rose-200 hover:border-rose-400 transition">
                    <span class="px-2 py-0.5 rounded bg-rose-600 text-white font-black text-[10px]">die</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">die Cola</p>
                    <p class="text-slate-500 text-[11px]">nước ngọt Cola 🔊</p>
                </div>
                <div onclick="speakGerman('der Wein')" class="cursor-pointer p-3 rounded-2xl bg-blue-50/60 border border-blue-200 hover:border-blue-400 transition">
                    <span class="px-2 py-0.5 rounded bg-blue-600 text-white font-black text-[10px]">der</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">der Wein</p>
                    <p class="text-slate-500 text-[11px]">rượu vang 🔊</p>
                </div>
                <div onclick="speakGerman('der Kakao')" class="cursor-pointer p-3 rounded-2xl bg-blue-50/60 border border-blue-200 hover:border-blue-400 transition">
                    <span class="px-2 py-0.5 rounded bg-blue-600 text-white font-black text-[10px]">der</span>
                    <p class="font-extrabold text-slate-900 text-sm mt-1">der Kakao</p>
                    <p class="text-slate-500 text-[11px]">ca cao 🔊</p>
                </div>
            </div>

            <!-- Giới từ & Cách đọc tiền Euro -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2 text-xs sm:text-sm">
                    <h4 class="font-extrabold text-slate-900">Cặp từ đối lập khi gọi món:</h4>
                    <div class="space-y-1">
                        <div>• <b class="text-indigo-600">mit</b> (với/có) ↔ <b class="text-rose-600">ohne</b> (không có/không kèm)</div>
                        <div>• <b class="text-indigo-600">viel</b> (nhiều) ↔ <b class="text-slate-600">wenig</b> (ít)</div>
                        <div class="italic text-slate-500 pt-1">Ví dụ: "Kaffee mit viel Milch" / "Tee ohne Zucker, bitte."</div>
                    </div>
                </div>

                <div class="p-4 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-2 text-xs sm:text-sm">
                    <h4 class="font-extrabold text-amber-900">Quy tắc đọc giá tiền Euro (1 € = 100 Cent):</h4>
                    <p class="text-slate-700">Dấu phẩy (<b>,</b>) đọc là <b>"Euro"</b>, phần số lẻ phía sau đọc như số đếm bình thường:</p>
                    <div class="space-y-1 font-mono text-xs">
                        <div onclick="speakGerman('ein Euro neunundzwanzig')" class="cursor-pointer hover:text-indigo-600">1,29 € → <b>ein Euro neunundzwanzig</b> 🔊</div>
                        <div onclick="speakGerman('drei Euro neunundneunzig')" class="cursor-pointer hover:text-indigo-600">3,99 € → <b>drei Euro neunundneunzig</b> 🔊</div>
                        <div onclick="speakGerman('neun Euro sechsundachtzig')" class="cursor-pointer hover:text-indigo-600">9,86 € → <b>neun Euro sechsundachtzig</b> 🔊</div>
                    </div>
                </div>
            </div>

            <!-- Hội thoại hoàn chỉnh tại Quán Cà Phê -->
            <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2.5 text-xs sm:text-sm">
                <div class="font-extrabold text-slate-900 pb-1.5 border-b border-slate-200 flex items-center justify-between">
                    <span>☕ Hội thoại gọi món & Thanh toán tại Quán Cà Phê</span>
                    <span class="text-xs text-indigo-600 font-semibold">Kellner, Anna, Sophie</span>
                </div>
                <div onclick="speakGerman('Was möchten Sie trinken?')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Kellner:</b> Was möchten Sie trinken? <i>(Quý khách muốn uống gì ạ?)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
                <div onclick="speakGerman('Ich trinke Kaffee mit viel Milch.')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Anna:</b> Ich trinke Kaffee mit viel Milch. <i>(Tôi uống cà phê với nhiều sữa.)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
                <div onclick="speakGerman('Ich nehme Tee, bitte.')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Sophie:</b> Ich nehme Tee, bitte. <i>(Cho tôi dùng trà ạ.)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
                <div class="py-1 text-slate-400 text-center italic text-xs">--- Sau khi uống xong - Gọi tính tiền ---</div>
                <div onclick="speakGerman('Wir möchten bitte zahlen.')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Anna & Sophie:</b> Wir möchten bitte zahlen. <i>(Chúng tôi muốn thanh toán ạ.)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
                <div onclick="speakGerman('Zusammen oder getrennt?')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Kellner:</b> Zusammen oder getrennt? <i>(Thanh toán chung hay riêng ạ?)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
                <div onclick="speakGerman('Zusammen, bitte.')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Anna:</b> Zusammen, bitte. <i>(Thanh toán chung ạ.)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
                <div onclick="speakGerman('Das macht sechs Euro achtzig.')" class="cursor-pointer p-2.5 rounded-xl hover:bg-white transition flex justify-between items-center">
                    <span><b>Kellner:</b> Das macht 6,80 Euro. <i>(Tổng cộng hết 6,80 Euro ạ.)</i></span>
                    <span class="text-indigo-600">🔊</span>
                </div>
            </div>
        </div>
    </div>
    """

    if fixed_lesson_id:
        cursor.execute("INSERT INTO lessons (id, level_id, title, grammar_content) VALUES (?, ?, ?, ?);", (fixed_lesson_id, a1_id, lesson_title, grammar_html))
        lesson_id = fixed_lesson_id
    else:
        cursor.execute("INSERT INTO lessons (level_id, title, grammar_content) VALUES (?, ?, ?);", (a1_id, lesson_title, grammar_html))
        lesson_id = cursor.lastrowid

    # =========================================================================
    # DANH SÁCH TỪ VỰNG BÀI 1 (P2)
    # =========================================================================
    vocabs = [
        (lesson_id, "Kaffee", "der", "Cà phê", "Ich trinke Kaffee mit viel Milch. (Tôi uống cà phê với nhiều sữa.)"),
        (lesson_id, "Tee", "der", "Trà", "Ich nehme Tee ohne Zucker, bitte. (Cho tôi dùng trà không đường ạ.)"),
        (lesson_id, "Milch", "die", "Sữa", "Möchten Sie Kaffee mit Milch? (Ngài muốn dùng cà phê có sữa không?)"),
        (lesson_id, "Zucker", "der", "Đường", "Tee ohne Zucker, bitte. (Làm ơn cho một ly trà không đường.)"),
        (lesson_id, "Cola", "die", "Nước ngọt Cola", "Er trinkt eine Cola. (Anh ấy uống một ly/chai nước ngọt Cola.)"),
        (lesson_id, "Wasser", "das", "Nước lọc", "Ein Glas Wasser, bitte. (Làm ơn cho một ly nước lọc.)"),
        (lesson_id, "Mineralwasser", "das", "Nước khoáng", "Ich trinke gern Mineralwasser. (Tôi thích uống nước khoáng.)"),
        (lesson_id, "Wein", "der", "Rượu vang", "Wir trinken Wein im Restaurant. (Chúng tôi uống rượu vang trong nhà hàng.)"),
        (lesson_id, "Kakao", "der", "Ca cao", "Ich möchte Kakao trinken. (Tôi muốn uống ca cao.)"),
        (lesson_id, "Saft", "der", "Nước ép hoa quả", "Der Saft ist sehr lecker. (Nước ép hoa quả rất ngon.)"),
        (lesson_id, "Eis", "das", "Đá lạnh / Kem", "Cola mit Eis, bitte. (Làm ơn cho một ly Cola có đá.)"),
        (lesson_id, "Café", "das", "Quán cà phê", "Wir sind im Café Kafka. (Chúng tôi đang ở quán cà phê Kafka.)"),
        (lesson_id, "Kellner", "der", "Nam bồi bàn / Nam nhân viên phục vụ (nữ: die Kellnerin)", "Der Kellner fragt: Was möchten Sie trinken? (Người bồi bàn hỏi: Ngài muốn uống gì?)"),
        (lesson_id, "Euro", "der", "Đồng tiền Euro (€)", "Das macht 6,80 Euro. (Tổng cộng hết 6,80 Euro.)"),
        (lesson_id, "Cent", "der", "Đơn vị xu Cent (1 € = 100 Cent)", "Ein Euro hat hundert Cent. (Một Euro có một trăm Cent.)"),
        (lesson_id, "trinken", "Động từ", "Uống", "Was trinken Sie? Ich trinke Tee. (Ngài uống gì? - Tôi uống trà.)"),
        (lesson_id, "nehmen", "Động từ", "Dùng, lấy, chọn (món)", "Was nehmen Sie? Ich nehme Kaffee. (Ngài dùng món gì? - Tôi dùng cà phê.)"),
        (lesson_id, "möchten", "Động từ", "Muốn (lịch sự)", "Was möchten Sie trinken? (Ngài muốn uống gì?)"),
        (lesson_id, "zahlen", "Động từ", "Thanh toán, trả tiền", "Wir möchten bitte zahlen. (Làm ơn cho chúng tôi thanh toán.)"),
        (lesson_id, "kosten", "Động từ", "Có giá là, trị giá, tốn", "Wie viel kostet der Kaffee? (Cà phê này giá bao nhiêu?)"),
        (lesson_id, "mieten", "Động từ", "Thuê (nhà, căn hộ)", "Er mietet eine Wohnung in Berlin. (Anh ấy thuê một căn hộ ở Berlin.)"),
        (lesson_id, "arbeiten", "Động từ", "Làm việc", "Wo arbeitest du? Ich arbeite bei der Post. (Bạn làm việc ở đâu? - Tôi làm việc ở bưu điện.)"),
        (lesson_id, "wohnen", "Động từ", "Sống, cư trú", "Wir wohnen in Frankfurt. (Chúng tôi sống ở Frankfurt.)"),
        (lesson_id, "kommen", "Động từ", "Đến, tới (kommen aus: đến từ)", "Ich komme aus Vietnam. (Tôi đến từ Việt Nam.)"),
        (lesson_id, "heißen", "Động từ", "Tên là, gọi là", "Wie heißen Sie? Ich heiße Dat Nguyen. (Ngài tên là gì? - Tôi tên là Đạt Nguyễn.)"),
        (lesson_id, "sein", "Động từ", "Thì, là, ở", "Ich bin im Deutschkurs. (Tôi đang ở lớp học tiếng Đức.)"),
        (lesson_id, "haben", "Động từ", "Có, sở hữu", "Hast du heute Zeit? (Hôm nay bạn có thời gian không?)"),
        (lesson_id, "lesen", "Động từ", "Đọc", "Du liest ein deutsches Buch. (Bạn đang đọc một cuốn sách tiếng Đức.)"),
        (lesson_id, "mit", "Giới từ", "Với, có kèm", "Kaffee mit Milch und Zucker. (Cà phê có sữa và đường.)"),
        (lesson_id, "ohne", "Giới từ", "Không có, không kèm", "Tee ohne Zucker. (Trà không có đường.)"),
        (lesson_id, "viel", "Trạng từ", "Nhiều", "Ich trinke Kaffee mit viel Milch. (Tôi uống cà phê với nhiều sữa.)"),
        (lesson_id, "wenig", "Trạng từ", "Ít", "Nur wenig Zucker, bitte. (Chỉ một ít đường thôi ạ.)"),
        (lesson_id, "zusammen", "Trạng từ", "Cùng nhau, tính chung", "Zusammen, bitte. (Làm ơn tính chung.)"),
        (lesson_id, "getrennt", "Trạng từ", "Riêng biệt, tính riêng", "Wir zahlen getrennt, bitte. (Làm ơn cho chúng tôi tính riêng.)")
    ]

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabs)

    # Đoạn văn đọc hiểu dùng chung cho dạng Đọc hiểu
    passage_doc_1 = (
        "Marc: Woher kommst du?\n"
        "Anna: Ich komme aus Brasilien. Das ist mein Freund, er kommt aus Russland.\n"
        "Marc: Und wo wohnt ihr?\n"
        "Anna: Wir wohnen in Berlin. Wo arbeitest du?\n"
        "Marc: Ich arbeite bei der Post."
    )

    passage_doc_2 = (
        "Anna: Hi, Anna und ich sind im Café Kafka. Wo bist du? Maria ist auch da. Kommst du auch?\n"
        "Peter: Wo seid ihr? Ich bin im Deutschkurs. Die Lehrerin ist nett, sie ist aus den USA."
    )

    passage_doc_3 = (
        "Kellner: Was möchten Sie trinken?\n"
        "Anna: Ich trinke Kaffee mit viel Milch.\n"
        "Sophie: Ich nehme Tee, bitte.\n"
        "...\n"
        "Anna und Sophie: Wir möchten bitte zahlen.\n"
        "Kellner: Zusammen oder getrennt?\n"
        "Anna: Zusammen, bitte.\n"
        "Kellner: Das macht 6,80 Euro."
    )

    # =========================================================================
    # KHO ĐÚNG 50 BÀI TẬP BÀI 1 (P2) THEO 7 DẠNG KỸ NĂNG & RANDOM ĐỔI ĐỀ
    # =========================================================================
    exercises = [
        # ---------------------------------------------------------------------
        # DẠNG 1: TRẮC NGHIỆM (trac_nghiem) - ĐÚNG 10 CÂU (Câu 1 -> 10)
        # ---------------------------------------------------------------------
        (
            lesson_id, "trac_nghiem",
            "Câu 1 [Đại từ nhân xưng]: Đại từ nào thay thế chính xác cho cụm chủ ngữ 'Anna und ich'?",
            json.dumps(["wir", "ihr", "sie", "Sie"]),
            "wir",
            "Khi có 'ich' kết hợp với một người khác (Anna und ich), chủ ngữ tương đương với ngôi 'wir' (chúng tôi).", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 2 [Đại từ nhân xưng]: Khi hỏi trực tiếp hai người bạn 'Anna und Peter', bạn dùng đại từ nào?",
            json.dumps(["ihr", "wir", "sie", "Sie"]),
            "ihr",
            "Khi hỏi trực tiếp nhiều người thân mật (nhiều ngôi 'du'), ta dùng đại từ số nhiều 'ihr' (các bạn).", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 3 [Giao tiếp lịch sự]: Khi xưng hô trang trọng với 'Herr Nguyen' hoặc 'Frau Bui', ta dùng đại từ nào?",
            json.dumps(["Sie", "er", "du", "ihr"]),
            "Sie",
            "Ngôi 'Sie' (viết hoa chữ S) dùng để xưng hô lịch sự với người lớn tuổi, đối tác hoặc người lạ.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 4 [Chia động từ gốc -ß]: Ngôi 'du' của động từ 'heißen' (tên là) được chia chính xác là gì?",
            json.dumps(["heißt", "heißest", "heißen", "heißst"]),
            "heißt",
            "Vì gốc 'heiß-' đã có âm gió -ß nên ngôi 'du' chỉ thêm đuôi -t: du heißt.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 5 [Chia động từ gốc -t]: Ngôi 'du' của động từ 'arbeiten' (làm việc) được chia như thế nào?",
            json.dumps(["arbeitest", "arbeits", "arbeitet", "arbeitst"]),
            "arbeitest",
            "Gốc 'arbeit-' kết thúc bằng -t nên phải chèn thêm nguyên âm -e- trước đuôi -st: du arbeitest.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 6 [Chia động từ gốc -t]: Ngôi 'ihr' của động từ 'mieten' (thuê) được chia là gì?",
            json.dumps(["mietet", "mietest", "mieten", "miet"]),
            "mietet",
            "Gốc 'miet-' kết thúc bằng -t nên thêm -e- trước đuôi -t: ihr mietet.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 7 [Động từ biến âm]: Ngôi 'du' của động từ 'lesen' (đọc) chia dạng nào dưới đây?",
            json.dumps(["liest", "lesest", "leist", "lest"]),
            "liest",
            "Động từ 'lesen' biến âm e → ie ở ngôi du và er/sie/es: du liest.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 8 [Động từ biến âm]: Ngôi 'er' của động từ 'nehmen' (chọn món/lấy) chia là gì?",
            json.dumps(["nimmt", "nehmt", "nimmst", "nahmt"]),
            "nimmt",
            "Động từ 'nehmen' biến âm 'nehm-' thành 'nimm-' ở ngôi du (nimmst) và er/sie/es (nimmt).", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 9 [Khuyết thiếu möchten]: Dạng chia nào của 'möchten' đi đúng với chủ ngữ 'er'?",
            json.dumps(["möchte", "möchtet", "möchtest", "möchten"]),
            "möchte",
            "Ngôi 'ich' và 'er/sie/es' của động từ khuyết thiếu chia giống nhau và KHÔNG có đuôi -t: er möchte.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 10 [Từ vựng thanh toán]: Khi bồi bàn hỏi 'Zusammen oder getrennt?', từ 'getrennt' có nghĩa là gì?",
            json.dumps(["Thanh toán riêng", "Thanh toán chung", "Thanh toán bằng thẻ", "Gói mang về"]),
            "Thanh toán riêng",
            "'zusammen' là thanh toán chung gộp lại, 'getrennt' là thanh toán riêng phần của từng người.", 15, None
        ),

        # ---------------------------------------------------------------------
        # DẠNG 2: ĐIỀN KHUYẾT CHIA ĐỘNG TỪ (dien_khuyet) - ĐÚNG 10 CÂU (Câu 11 -> 20)
        # ---------------------------------------------------------------------
        (
            lesson_id, "dien_khuyet",
            "Câu 11 [Điền khuyết sein]: Điền dạng đúng của 'sein': 'Hi, Anna und ich ___ im Café Kafka.'",
            None, "sind",
            "'Anna und ich' tương đương với ngôi số nhiều 'wir' nên động từ sein chia là 'sind'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 12 [Điền khuyết sein]: Điền dạng đúng của 'sein': 'Wo ___ du? Maria ist auch da.'",
            None, "bist",
            "Ngôi 'du' của động từ bất quy tắc sein là 'bist' (Wo bist du?).", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 13 [Điền khuyết haben]: Điền dạng đúng của 'haben': 'Er ___ heute keine Zeit.'",
            None, "hat",
            "Ngôi 'er' của động từ haben lược bỏ phụ âm -b- thành 'hat'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 14 [Điền khuyết wohnen]: Điền dạng đúng của 'wohnen': 'Und wo ___ ihr? - Wir wohnen in Berlin.'",
            None, "wohnt",
            "Chủ ngữ 'ihr' đi với động từ wohnen thêm đuôi -t: 'wohnt'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 15 [Điền khuyết kommen]: Điền dạng đúng của 'kommen': 'Das ist mein Freund, er ___ aus Russland.'",
            None, "kommt",
            "Chủ ngữ 'er' đi với động từ kommen thêm đuôi -t: 'kommt'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 16 [Điền khuyết arbeiten]: Điền dạng đúng của 'arbeiten': 'Wo arbeitest du? - Ich ___ bei der Post.'",
            None, "arbeite",
            "Chủ ngữ 'ich' đi với động từ arbeiten có đuôi -e: 'arbeite'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 17 [Điền khuyết trinken]: Điền dạng đúng của 'trinken': 'Was ___ Sie? - Ich trinke Kaffee mit Milch.'",
            None, "trinken",
            "Ngôi lịch sự 'Sie' đi với động từ nguyên mẫu có đuôi -en: 'trinken'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 18 [Điền khuyết nehmen]: Điền dạng đúng của 'nehmen': 'Was ___ du? - Ich nehme Tee.'",
            None, "nimmst",
            "Động từ biến âm 'nehmen' ở ngôi 'du' biến đổi thành 'nimmst'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 19 [Điền khuyết möchten]: Điền dạng đúng của 'möchten': 'Wir ___ bitte zahlen.'",
            None, "möchten",
            "Ngôi 'wir' đi với möchten chia là 'möchten'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 20 [Điền khuyết machen]: Điền dạng đúng của 'machen': 'Das ___ 3,99 Euro.'",
            None, "macht",
            "Cấu trúc báo tổng giá tiền: 'Das macht + [Số tiền] + Euro'.", 15, None
        ),

        # ---------------------------------------------------------------------
        # DẠNG 3: DỊCH 2 CHIỀU & GIÁ TIỀN EURO (dich) - ĐÚNG 8 CÂU (Câu 21 -> 28)
        # ---------------------------------------------------------------------
        (
            lesson_id, "dich",
            "Câu 21 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Tôi uống cà phê với nhiều sữa.'",
            None, "Ich trinke Kaffee mit viel Milch. / Ich nehme Kaffee mit viel Milch. / Ich möchte Kaffee mit viel Milch. / Ich trinke einen Kaffee mit viel Milch.",
            "Cấu trúc: Ich trinke (Tôi uống) + Kaffee (cà phê) + mit viel Milch (với nhiều sữa).", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 22 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Cho trà không đường, làm ơn.'",
            None, "Tee ohne Zucker, bitte. / Einen Tee ohne Zucker, bitte. / Tee ohne Zucker bitte. / Ich möchte Tee ohne Zucker, bitte.",
            "Cấu trúc: Tee (trà) + ohne Zucker (không đường) + bitte (làm ơn/ạ).", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 23 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Chúng tôi muốn thanh toán.'",
            None, "Wir möchten bitte zahlen. / Wir möchten zahlen, bitte. / Wir möchten zahlen. / Wir möchten bitte bezahlen. / Zahlen, bitte! / Zahlen bitte!",
            "Cấu trúc khung câu: Wir möchten (Chúng tôi muốn) + bitte + zahlen (thanh toán).", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 24 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Thanh toán chung hay riêng?'",
            None, "Zusammen oder getrennt? / Zusammen hoặc getrennt, bitte? / Zusammen oder getrennt",
            "Câu hỏi quen thuộc của nhân viên phục vụ: Zusammen (chung) + oder (hay/hoặc) + getrennt (riêng)?", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 25 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Tổng cộng hết 3,99 Euro.'",
            None, "Das macht 3,99 Euro. / Das macht 3,99 €. / Das macht 3.99 Euro. / Das kostet 3,99 Euro. / Das macht 3,99. / Das macht drei Euro neunundneunzig. / Das macht drei Euro neunundneunzig Cent. / Das kostet drei Euro neunundneunzig. / Das macht drei neunundneunzig.",
            "Cấu trúc chuẩn: 'Das macht 3,99 Euro.'", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 26 [Đổi giá tiền Euro (Random)]: Hãy viết giá tiền 1,29 € bằng chữ tiếng Đức (chấp nhận có hoặc không có chữ Cent):",
            None, "ein Euro neunundzwanzig / 1,29 / 1,29 € / ein Euro 29",
            "1,29 € đọc là: 'ein Euro neunundzwanzig' (chú ý dùng 'ein Euro' thay vì 'eins Euro').", 20,
            json.dumps({"dynamic_price": True, "dynamic_mode": "price_to_de", "euros": 1, "cents": 29})
        ),
        (
            lesson_id, "dich",
            "Câu 27 [Đổi giá tiền Euro (Random)]: Hãy viết giá tiền 2,99 € bằng chữ tiếng Đức:",
            None, "zwei Euro neunundneunzig / 2,99 / 2,99 € / 2 Euro 99",
            "2,99 € viết bằng chữ tiếng Đức là: 'zwei Euro neunundneunzig'.", 20,
            json.dumps({"dynamic_price": True, "dynamic_mode": "price_to_de", "euros": 2, "cents": 99})
        ),
        (
            lesson_id, "dich",
            "Câu 28 [Đổi giá tiền Euro (Random)]: Hãy viết giá tiền 9,86 € bằng chữ tiếng Đức:",
            None, "neun Euro sechsundachtzig / 9,86 / 9,86 € / 9 Euro 86",
            "9,86 € viết bằng chữ tiếng Đức là: 'neun Euro sechsundachtzig'.", 20,
            json.dumps({"dynamic_price": True, "dynamic_mode": "price_to_de", "euros": 9, "cents": 86})
        ),

        # ---------------------------------------------------------------------
        # DẠNG 4: LUYỆN NGHE 1.0x & 0.65x (nghe) - ĐÚNG 6 CÂU (Câu 29 -> 34)
        # ---------------------------------------------------------------------
        (
            lesson_id, "nghe",
            "Câu 29 [Luyện Nghe]: Nghe câu hỏi của nhân viên bồi bàn và viết lại chính xác:",
            None, "Was möchten Sie trinken? / Was möchten Sie trinken",
            "Câu nghe được là: 'Was möchten Sie trinken?' (Quý khách muốn uống gì ạ?)", 20,
            json.dumps({"audio_text": "Was möchten Sie trinken?"})
        ),
        (
            lesson_id, "nghe",
            "Câu 30 [Luyện Nghe điền từ]: Nghe và điền động từ biến âm còn thiếu vào câu: 'Du ___ ein deutsches Buch.'",
            None, "liest",
            "Âm thanh phát câu: 'Du liest ein deutsches Buch.' → Động từ còn thiếu là 'liest'.", 20,
            json.dumps({"audio_text": "Du liest ein deutsches Buch."})
        ),
        (
            lesson_id, "nghe",
            "Câu 31 [Luyện Nghe điền từ]: Nghe và điền động từ biến âm còn thiếu vào câu: 'Er ___ einen Tee mit Zitrone.'",
            None, "nimmt",
            "Âm thanh phát câu: 'Er nimmt einen Tee mit Zitrone.' → Động từ là 'nimmt'.", 20,
            json.dumps({"audio_text": "Er nimmt einen Tee mit Zitrone."})
        ),
        (
            lesson_id, "nghe",
            "Câu 32 [Luyện Nghe giá tiền (Random)]: Nghe câu thông báo của bồi bàn và điền số tiền dạng số (ví dụ: 4,50):",
            None, "4,50",
            "Bồi bàn thông báo 'Das macht vier Euro fünfzig.' → Số tiền là 4,50 (hoặc 4.50).", 20,
            json.dumps({"audio_text": "Das macht vier Euro fünfzig.", "dynamic_price": True, "dynamic_mode": "listen_price", "euros": 4, "cents": 50})
        ),
        (
            lesson_id, "nghe",
            "Câu 33 [Luyện Nghe giá tiền (Random)]: Nghe câu thông báo của bồi bàn và điền số tiền dạng số (ví dụ: 12,89):",
            None, "12,89",
            "Bồi bàn thông báo 'Das macht zwölf Euro neunundachtzig.' → Số tiền là 12,89.", 20,
            json.dumps({"audio_text": "Das macht zwölf Euro neunundachtzig.", "dynamic_price": True, "dynamic_mode": "listen_price", "euros": 12, "cents": 89})
        ),
        (
            lesson_id, "nghe",
            "Câu 34 [Luyện Nghe]: Nghe và viết lại câu trả lời thanh toán:",
            None, "Zusammen, bitte. / Zusammen bitte. / Zusammen, bitte / Zusammen bitte",
            "Âm thanh phát: 'Zusammen, bitte.' (Thanh toán chung ạ.)", 20,
            json.dumps({"audio_text": "Zusammen, bitte."})
        ),

        # ---------------------------------------------------------------------
        # DẠNG 5: SẮP XẾP TỪ THÀNH CÂU (sap_xep) - ĐÚNG 5 CÂU (Câu 35 -> 39)
        # ---------------------------------------------------------------------
        (
            lesson_id, "sap_xep",
            "Câu 35 [Sắp xếp từ thành câu]: Sắp xếp các từ sau thành câu hỏi gọi đồ uống lịch sự: [trinken / möchten / Was / Sie / ?]",
            None, "Was möchten Sie trinken?",
            "Câu hỏi W-Frage với động từ khuyết thiếu möchten: Từ để hỏi (Was) đứng vị trí 1, động từ khuyết thiếu chia theo Sie (möchten) đứng vị trí 2, động từ nguyên thể trinken về cuối câu.", 25,
            json.dumps({"audio_text": "Was möchten Sie trinken?", "translation": "Quý khách muốn uống gì ạ?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 36 [Sắp xếp từ thành câu]: Sắp xếp các từ sau thành câu gọi cà phê nhiều sữa: [Kaffee / trinke / Ich / viel / Milch / mit / .]",
            None, "Ich trinke Kaffee mit viel Milch.",
            "Chủ ngữ Ich đứng vị trí 1, động từ trinke đứng vị trí 2, tân ngữ Kaffee và cụm giới từ mit viel Milch ở sau.", 25,
            json.dumps({"audio_text": "Ich trinke Kaffee mit viel Milch.", "translation": "Tôi uống cà phê với nhiều sữa."}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 37 [Sắp xếp từ thành câu]: Sắp xếp câu hỏi bồi bàn hỏi khách trả chung hay riêng: [getrennt / oder / Zusammen / ?]",
            None, "Zusammen oder getrennt?",
            "Mẫu câu hỏi kinh điển khi thanh toán tại quán ăn/cafe ở Đức: Zusammen (chung) oder (hay) getrennt (riêng)?", 25,
            json.dumps({"audio_text": "Zusammen hoặc getrennt?", "translation": "Thanh toán chung hay thanh toán riêng?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 38 [Sắp xếp từ thành câu]: Sắp xếp các từ sau thành câu ghép miêu tả cô giáo: [nett / ist / Die Lehrerin / sie / , / aus den USA / ist / .]",
            None, "Die Lehrerin ist nett, sie ist aus den USA.",
            "Mệnh đề 1: Die Lehrerin ist nett. Mệnh đề 2: sie ist aus den USA (Đại từ sie thay thế cho Die Lehrerin).", 25,
            json.dumps({"audio_text": "Die Lehrerin ist nett, sie ist aus den USA.", "translation": "Cô giáo rất tốt bụng, cô ấy đến từ nước Mỹ."}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 39 [Sắp xếp hội thoại]: Sắp xếp câu hỏi và trả lời về nơi làm việc: [bei der Post / arbeitest / Wo / ? / Ich / du / arbeite / .]",
            None, "Wo arbeitest du? Ich arbeite bei der Post.",
            "Câu hỏi: Wo arbeitest du? Trả lời: Ich arbeite bei der Post.", 25,
            json.dumps({"audio_text": "Wo arbeitest du? Ich arbeite bei der Post.", "translation": "Bạn làm việc ở đâu? Tôi làm việc ở bưu điện."}, ensure_ascii=False)
        ),

        # ---------------------------------------------------------------------
        # DẠNG 6: ĐỌC HIỂU HỘI THOẠI (doc) - ĐÚNG 4 CÂU (Câu 40 -> 43)
        # ---------------------------------------------------------------------
        (
            lesson_id, "doc",
            "Câu 40 [Đọc hiểu 1]: Dựa vào đoạn hội thoại giữa Marc, Anna và Peter, Marc làm việc ở đâu?",
            json.dumps(["Tại bưu điện", "Tại quán cà phê", "Tại trường học", "Tại ngân hàng"]),
            "Tại bưu điện",
            "Trong đoạn hội thoại, Marc nói: 'Ich arbeite bei der Post.' (tại bưu điện).", 20,
            json.dumps({"passage": passage_doc_1})
        ),
        (
            lesson_id, "doc",
            "Câu 41 [Đọc hiểu 2]: Dựa vào đoạn tin nhắn Café Kafka, Peter hiện đang ở đâu?",
            json.dumps(["Trong khóa học tiếng Đức", "Ở quán Café Kafka", "Ở bưu điện", "Ở ga tàu"]),
            "Trong khóa học tiếng Đức",
            "Peter trả lời: 'Ich bin im Deutschkurs.' (trong khóa học tiếng Đức).", 20,
            json.dumps({"passage": passage_doc_2})
        ),
        (
            lesson_id, "doc",
            "Câu 42 [Đọc hiểu 3]: Theo lời của Peter, cô giáo dạy tiếng Đức đến từ quốc gia nào?",
            json.dumps(["Mỹ", "Nga", "Brazil", "Đức"]),
            "Mỹ",
            "Peter nói: 'Die Lehrerin ist nett, sie ist aus den USA.' (cô giáo đến từ Mỹ).", 20,
            json.dumps({"passage": passage_doc_2})
        ),
        (
            lesson_id, "doc",
            "Câu 43 [Đọc hiểu 4]: Dựa vào hội thoại tại quán cà phê, Sophie uống gì và tổng số tiền thanh toán là bao nhiêu?",
            json.dumps([
                "Sophie uống trà và tổng tiền là 6,80 Euro",
                "Sophie uống cà phê và tổng tiền là 6,80 Euro",
                "Anna uống trà và tổng tiền là 4,50 Euro",
                "Cả hai đều uống cà phê"
            ]),
            "Sophie uống trà và tổng tiền là 6,80 Euro",
            "Sophie nói 'Ich nehme Tee, bitte.' và người bồi bàn báo 'Das macht 6,80 Euro.'", 20,
            json.dumps({"passage": passage_doc_3})
        ),

        # ---------------------------------------------------------------------
        # DẠNG 7: VIẾT CÂU, CHIA ĐỘNG TỪ & GIÁ TIỀN (viet) - ĐÚNG 7 CÂU (Câu 44 -> 50)
        # ---------------------------------------------------------------------
        (
            lesson_id, "viet",
            "Câu 44 [Sắp xếp khung câu Satzklammer]: Sắp xếp các từ sau thành câu hỏi hoàn chỉnh: 'trinken / Sie / Was / möchten / ?'",
            None, "Was möchten Sie trinken? / Was möchten Sie trinken",
            "Cấu trúc câu hỏi: Từ để hỏi (Was) + möchten chia theo Sie + Sie + động từ nguyên mẫu trinken cuối câu.", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 45 [Sắp xếp khung câu Satzklammer]: Sắp xếp các từ sau thành câu hoàn chỉnh: 'zahlen / möchten / Wir / bitte / .'",
            None, "Wir möchten bitte zahlen. / Wir möchten zahlen, bitte. / Wir möchten bitte zahlen",
            "Cấu trúc: Chủ ngữ (Wir) + möchten + bitte + zahlen nguyên mẫu ở cuối câu.", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 46 [Viết dạng chia động từ]: Hãy viết dạng chia của động từ 'sein' cho ngôi 'ihr':",
            None, "seid",
            "Ngôi 'ihr' của động từ sein là: 'seid' (Wo seid ihr?).", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 47 [Viết dạng chia động từ]: Hãy viết dạng chia của động từ 'haben' cho ngôi 'du':",
            None, "hast",
            "Ngôi 'du' của động từ haben là: 'hast' (Du hast Zeit).", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 48 [Viết dạng chia động từ]: Hãy viết dạng chia của động từ 'mieten' cho ngôi 'er':",
            None, "mietet",
            "Gốc 'miet-' kết thúc bằng -t nên thêm -et ở ngôi er: 'mietet'.", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 49 [Rèn phản xạ Chia Động Từ (Random)]: Hãy chia động từ 'arbeiten' cho chủ ngữ 'du': 'du ___'",
            None, "arbeitest",
            "Động từ 'arbeiten' ở ngôi 'du' được chia là 'arbeitest'.", 25,
            json.dumps({"dynamic_conjugation": True, "verb": "arbeiten", "subject": "du"})
        ),
        (
            lesson_id, "viet",
            "Câu 50 [Viết giá tiền Euro (Random)]: Hãy viết cách đọc giá tiền 3,99 € bằng chữ tiếng Đức (chấp nhận có hoặc không có chữ Cent):",
            None, "drei Euro neunundneunzig / 3,99 / 3,99 € / 3.99 / drei Euro neunundneunzig Cent",
            "3,99 € được viết là: 'drei Euro neunundneunzig'.", 30,
            json.dumps({"dynamic_price": True, "dynamic_mode": "price_to_de", "euros": 3, "cents": 99})
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
    print("✅ Đã khởi tạo thành công Bài 1 (P2): 'Kaffee oder Tee - Cà Phê Hoặc Trà' với đầy đủ Lý thuyết (Không link YouTube) + 34 Từ vựng + ĐÚNG 50 Bài tập (10+10+8+6+5+4+7) có Random Đổi đề!")

if __name__ == "__main__":
    seed_lesson_1_part_2()
