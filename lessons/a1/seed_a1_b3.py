import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_3():
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

    # Xóa dữ liệu cũ của Bài 3 nếu đã có để cập nhật sạch sẽ
    cursor.execute("DELETE FROM lessons WHERE level_id = ? AND title LIKE 'Bài 3%';", (a1_id,))

    lesson_title = 'Bài 3: "Städte – Länder – Sprachen: Địa Danh, Phương Hướng & Thì Quá Khứ Đơn (Präteritum)"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (7 HỌC PHẦN CHUẨN ĐẶC TẢ - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 3 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Địa Danh, Phương Hướng & Quá Khứ Đơn Präteritum (Bài 3)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 75 phút • ⚡ 750+ EXP
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Städte – Länder – Sprachen • Địa Danh, Phương Hướng & Thì Quá Khứ Đơn (Präteritum)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Làm chủ quy tắc mạo từ địa lý (phân biệt rõ nhóm 85% quốc gia không dùng mạo từ vs. nhóm quốc gia đặc biệt bắt buộc đi kèm mạo từ <i>die Schweiz, die Türkei, die Slowakei, der Iran, die USA</i>); ghi nhớ 7 danh lam thắng cảnh biểu tượng của Châu Âu cùng 3 mẫu câu hỏi – đáp địa danh kinh điển; định hướng bản đồ với hệ thống 8 phương hướng (danh từ <i>der Norden...</i> vs. tính từ <i>nördlich...</i>, vị trí trung tâm <i>in der Mitte</i>); làm chủ 3 cấu trúc câu cốt lõi và hệ thống 9 từ để hỏi <i>W-Fragen</i>; sử dụng thành thạo thì Quá khứ đơn (<b>Präteritum</b>) của động từ <b>sein</b> (<i>war / warst / waren / wart</i>) và <b>haben</b> (<i>hatte / hattest</i>) để tự tin kể lại trải nghiệm chuyến du lịch.
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: QUỐC GIA (DIE LÄNDER), NGÔN NGỮ (DIE SPRACHEN) & QUY TẮC MẠO TỪ ĐỊA LÝ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">1</span>
                <div>
                    <h4 class="text-lg font-black text-slate-900 tracking-tight">Quốc Gia (Die Länder), Ngôn Ngữ (Die Sprachen) & Mạo Từ Địa Lý</h4>
                    <p class="text-xs text-slate-500">Phân biệt nhóm quốc gia không dùng mạo từ và nhóm quốc gia bắt buộc dùng mạo từ</p>
                </div>
            </div>

            <p class="text-sm text-slate-600">
                Trong tiếng Đức, các quốc gia được chia thành <b>2 nhóm ngữ pháp cực kỳ quan trọng</b>: Nhóm <b>không có mạo từ</b> (chiếm khoảng 85% các nước trên thế giới) và Nhóm <b>bắt buộc phải đi kèm mạo từ</b> (<i>die</i>, <i>der</i>, hoặc <i>die</i> số nhiều).
            </p>

            <!-- 1.1 Bảng 13 Quốc gia không mạo từ -->
            <div class="space-y-3">
                <h5 class="text-xs font-bold uppercase tracking-wider text-slate-500">1.1. Bảng 13 Quốc gia Không dùng Mạo từ & Ngôn ngữ tương ứng</h5>
                <p class="text-xs text-slate-600">
                    Khi nói <i>"đến từ"</i> dùng giới từ <b>aus</b>, khi nói <i>"ở tại"</i> dùng giới từ <b>in</b>, và khi nói <i>"đi đến"</i> dùng giới từ <b>nach</b> (không cần mạo từ ở giữa):
                </p>
                <div class="overflow-x-auto rounded-2xl border border-slate-200">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                            <tr>
                                <th class="p-3">Quốc gia (Land)</th>
                                <th class="p-3">Nghĩa tiếng Việt</th>
                                <th class="p-3">Ngôn ngữ chính (Sprache)</th>
                                <th class="p-3">Nghĩa tiếng Việt</th>
                                <th class="p-3">Câu ví dụ chuẩn & Phát âm</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Deutschland</td>
                                <td class="p-3">Nước Đức</td>
                                <td class="p-3 font-semibold text-purple-700">Deutsch</td>
                                <td class="p-3">Tiếng Đức</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Ich komme aus Deutschland und spreche Deutsch."</span>
                                    <button onclick="speakGerman('Ich komme aus Deutschland und spreche Deutsch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Österreich</td>
                                <td class="p-3">Nước Áo</td>
                                <td class="p-3 font-semibold text-purple-700">Deutsch</td>
                                <td class="p-3">Tiếng Đức</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Wien liegt in Österreich. Man spricht dort Deutsch."</span>
                                    <button onclick="speakGerman('Wien liegt in Österreich. Man spricht dort Deutsch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Italien</td>
                                <td class="p-3">Nước Ý</td>
                                <td class="p-3 font-semibold text-purple-700">Italienisch</td>
                                <td class="p-3">Tiếng Ý</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Pisa ist in Italien. Sie spricht gut Italienisch."</span>
                                    <button onclick="speakGerman('Pisa ist in Italien. Sie spricht gut Italienisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Spanien</td>
                                <td class="p-3">Tây Ban Nha</td>
                                <td class="p-3 font-semibold text-purple-700">Spanisch</td>
                                <td class="p-3">Tiếng Tây Ban Nha</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Carlos kommt aus Spanien und spricht Spanisch."</span>
                                    <button onclick="speakGerman('Carlos kommt aus Spanien und spricht Spanisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Griechenland</td>
                                <td class="p-3">Hy Lạp</td>
                                <td class="p-3 font-semibold text-purple-700">Griechisch</td>
                                <td class="p-3">Tiếng Hy Lạp</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Athen ist in Griechenland. Er lernt Griechisch."</span>
                                    <button onclick="speakGerman('Athen ist in Griechenland. Er lernt Griechisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Frankreich</td>
                                <td class="p-3">Nước Pháp</td>
                                <td class="p-3 font-semibold text-purple-700">Französisch</td>
                                <td class="p-3">Tiếng Pháp</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Der Eiffelturm ist in Frankreich. Wir sprechen Französisch."</span>
                                    <button onclick="speakGerman('Der Eiffelturm ist in Frankreich. Wir sprechen Französisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Großbritannien / England</td>
                                <td class="p-3">Nước Anh</td>
                                <td class="p-3 font-semibold text-purple-700">Englisch</td>
                                <td class="p-3">Tiếng Anh</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Big Ben ist in England. Sprichst du Englisch?"</span>
                                    <button onclick="speakGerman('Big Ben ist in England. Sprichst du Englisch?')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Polen</td>
                                <td class="p-3">Ba Lan</td>
                                <td class="p-3 font-semibold text-purple-700">Polnisch</td>
                                <td class="p-3">Tiếng Ba Lan</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Mein Freund kommt aus Polen und spricht Polnisch."</span>
                                    <button onclick="speakGerman('Mein Freund kommt aus Polen und spricht Polnisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Tschechien</td>
                                <td class="p-3">Cộng hòa Séc</td>
                                <td class="p-3 font-semibold text-purple-700">Tschechisch</td>
                                <td class="p-3">Tiếng Séc</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Prag liegt in Tschechien. Dort spricht man Tschechisch."</span>
                                    <button onclick="speakGerman('Prag liegt in Tschechien. Dort spricht man Tschechisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Russland</td>
                                <td class="p-3">Nước Nga</td>
                                <td class="p-3 font-semibold text-purple-700">Russisch</td>
                                <td class="p-3">Tiếng Nga</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Moskau ist in Russland. Anna spricht Russisch."</span>
                                    <button onclick="speakGerman('Moskau ist in Russland. Anna spricht Russisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">China</td>
                                <td class="p-3">Trung Quốc</td>
                                <td class="p-3 font-semibold text-purple-700">Chinesisch</td>
                                <td class="p-3">Tiếng Trung Quốc</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Frau Wang kommt aus China und spricht Chinesisch."</span>
                                    <button onclick="speakGerman('Frau Wang kommt aus China und spricht Chinesisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 transition">
                                <td class="p-3 font-bold text-indigo-700">Vietnam</td>
                                <td class="p-3">Việt Nam</td>
                                <td class="p-3 font-semibold text-purple-700">Vietnamesisch</td>
                                <td class="p-3">Tiếng Việt</td>
                                <td class="p-3 flex items-center justify-between gap-2">
                                    <span class="italic text-slate-700">"Ich komme aus Vietnam und spreche Vietnamesisch."</span>
                                    <button onclick="speakGerman('Ich komme aus Vietnam und spreche Vietnamesisch.')" class="px-2 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-slate-700 space-y-1.5">
                    <p class="font-bold text-amber-900">💡 Ghi chú Ngữ pháp về Tên Ngôn ngữ & Động từ sprechen:</p>
                    <p>• Hầu hết tên ngôn ngữ đều kết thúc bằng hậu tố <b>-isch</b> (đọc là <code>[ɪʃ]</code>).</p>
                    <p>• Động từ đi kèm ngôn ngữ là <b>sprechen</b> (nói) — biến âm <code>e -> i</code> ở ngôi <code>du</code> và <code>er/sie/es</code>: <i>ich spreche, <b>du sprichst</b>, <b>er spricht</b>, wir sprechen, ihr sprecht, sie/Sie sprechen</i>.</p>
                </div>
            </div>

            <!-- 1.2 Nhóm Quốc gia Bắt buộc có Mạo từ -->
            <div class="space-y-3 pt-3 border-t border-slate-100">
                <h5 class="text-xs font-bold uppercase tracking-wider text-slate-500">1.2. Nhóm Quốc gia ĐẶC BIỆT Bắt buộc có Mạo từ (Länder mit Artikel)</h5>
                <p class="text-xs text-slate-600">
                    Khi đi kèm với giới từ <b>aus</b> (<i>đến từ</i>) hoặc <b>in</b> (<i>ở tại</i>), mạo từ của các nước này sẽ <b>biến đổi theo Cách 3 (Dativ)</b>:
                </p>
                <div class="overflow-x-auto rounded-2xl border border-rose-200 bg-rose-50/20">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-rose-100/70 text-rose-900 font-bold border-b border-rose-200">
                            <tr>
                                <th class="p-3">Phân nhóm Giống</th>
                                <th class="p-3">Quốc gia gốc (Nominativ)</th>
                                <th class="p-3">Nghĩa tiếng Việt</th>
                                <th class="p-3">Ngôn ngữ</th>
                                <th class="p-3">Đến từ (aus + Dativ)</th>
                                <th class="p-3">Ở tại (in + Dativ)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-rose-100">
                            <tr class="hover:bg-white/60 transition">
                                <td class="p-3 font-bold text-rose-700">1. Giống cái (die)</td>
                                <td class="p-3 font-black text-slate-900">die Schweiz</td>
                                <td class="p-3">Thụy Sỹ</td>
                                <td class="p-3">Deutsch, Französisch, Italienisch</td>
                                <td class="p-3 font-bold text-indigo-700">aus der Schweiz</td>
                                <td class="p-3 font-bold text-emerald-700">in der Schweiz</td>
                            </tr>
                            <tr class="hover:bg-white/60 transition">
                                <td class="p-3 font-bold text-rose-700">1. Giống cái (die)</td>
                                <td class="p-3 font-black text-slate-900">die Türkei</td>
                                <td class="p-3">Thổ Nhĩ Kỳ</td>
                                <td class="p-3">Türkisch</td>
                                <td class="p-3 font-bold text-indigo-700">aus der Türkei</td>
                                <td class="p-3 font-bold text-emerald-700">in der Türkei</td>
                            </tr>
                            <tr class="hover:bg-white/60 transition">
                                <td class="p-3 font-bold text-rose-700">1. Giống cái (die)</td>
                                <td class="p-3 font-black text-slate-900">die Slowakei</td>
                                <td class="p-3">Slovakia</td>
                                <td class="p-3">Slowakisch</td>
                                <td class="p-3 font-bold text-indigo-700">aus der Slowakei</td>
                                <td class="p-3 font-bold text-emerald-700">in der Slowakei</td>
                            </tr>
                            <tr class="hover:bg-white/60 transition">
                                <td class="p-3 font-bold text-blue-700">2. Giống đực (der)</td>
                                <td class="p-3 font-black text-slate-900">der Iran</td>
                                <td class="p-3">Iran</td>
                                <td class="p-3">Persisch (tiếng Ba Tư)</td>
                                <td class="p-3 font-bold text-indigo-700">aus dem Iran</td>
                                <td class="p-3 font-bold text-emerald-700">im (in dem) Iran</td>
                            </tr>
                            <tr class="hover:bg-white/60 transition">
                                <td class="p-3 font-bold text-purple-700">3. Số nhiều (die Pl.)</td>
                                <td class="p-3 font-black text-slate-900">die USA</td>
                                <td class="p-3">Nước Mỹ</td>
                                <td class="p-3">Englisch</td>
                                <td class="p-3 font-bold text-indigo-700">aus den USA</td>
                                <td class="p-3 font-bold text-emerald-700">in den USA</td>
                            </tr>
                            <tr class="hover:bg-white/60 transition">
                                <td class="p-3 font-bold text-purple-700">3. Số nhiều (die Pl.)</td>
                                <td class="p-3 font-black text-slate-900">die Niederlande</td>
                                <td class="p-3">Hà Lan</td>
                                <td class="p-3">Niederländisch</td>
                                <td class="p-3 font-bold text-indigo-700">aus den Niederlanden</td>
                                <td class="p-3 font-bold text-emerald-700">in den Niederlanden</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="p-4 rounded-2xl bg-indigo-50 border border-indigo-200 text-xs text-indigo-950 space-y-1">
                    <p class="font-bold text-indigo-900">🔥 Mẹo Vàng Ghi Nhớ:</p>
                    <p>• Mọi quốc gia tận cùng bằng hậu tố <b>-ei</b> (<i>die Türkei, die Slowakei, die Mongolei</i>) luôn luôn mang giống cái (<b>die</b>).</p>
                    <p>• Thụy Sỹ (<b>die Schweiz</b>) có 3 ngôn ngữ chính trong bài: <i>Deutsch, Französisch, Italienisch</i>.</p>
                    <p>• Với <b>der Iran</b>, ngôn ngữ chính thức là <b>Persisch</b> (tiếng Ba Tư), không phải "Iranisch".</p>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: DANH LAM THẮNG CẢNH CHÂU ÂU (SEHENSWÜRDIGKEITEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">2</span>
                <div>
                    <h4 class="text-lg font-black text-slate-900 tracking-tight">Danh Lam Thắng Cảnh Châu Âu (Sehenswürdigkeiten in Europa)</h4>
                    <p class="text-xs text-slate-500">7 Công trình kiến trúc biểu tượng & 3 mẫu câu hỏi – đáp kinh điển</p>
                </div>
            </div>

            <p class="text-sm text-slate-600">
                Danh từ <b>die Sehenswürdigkeit</b> (số nhiều: <i>die Sehenswürdigkeiten</i>) có nghĩa là <i>danh lam thắng cảnh / điểm tham quan đáng xem</i> (ghép từ <code>sehen</code> = nhìn/xem + <code>würdig</code> = xứng đáng + hậu tố <code>-keit</code> mang giống cái).
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-rose-100 text-rose-800 font-bold">die (Giống cái)</span>
                        <button onclick="speakGerman('die Akropolis in Athen, Griechenland')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">die Akropolis</h5>
                    <p class="text-slate-600">Thành cổ Akropolis</p>
                    <p class="text-indigo-700 font-semibold">📍 Athen, Griechenland (Hy Lạp)</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-blue-100 text-blue-800 font-bold">der (Giống đực)</span>
                        <button onclick="speakGerman('der Big Ben in London, England')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">der Big Ben</h5>
                    <p class="text-slate-600">Tháp đồng hồ Big Ben (theo <i>der Turm</i>)</p>
                    <p class="text-indigo-700 font-semibold">📍 London, England (Anh)</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-blue-100 text-blue-800 font-bold">der (Giống đực)</span>
                        <button onclick="speakGerman('der Eiffelturm in Paris, Frankreich')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">der Eiffelturm</h5>
                    <p class="text-slate-600">Tháp Eiffel (ghép với <i>der Turm</i>)</p>
                    <p class="text-indigo-700 font-semibold">📍 Paris, Frankreich (Pháp)</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-blue-100 text-blue-800 font-bold">der (Giống đực)</span>
                        <button onclick="speakGerman('der Schiefe Turm in Pisa, Italien')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">der Schiefe Turm</h5>
                    <p class="text-slate-600">Tháp nghiêng Pisa (<i>schief</i> = nghiêng)</p>
                    <p class="text-indigo-700 font-semibold">📍 Pisa, Italien (Ý)</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-blue-100 text-blue-800 font-bold">der (Giống đực)</span>
                        <button onclick="speakGerman('der Prater in Wien, Österreich')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">der Prater</h5>
                    <p class="text-slate-600">Công viên giải trí Prater</p>
                    <p class="text-indigo-700 font-semibold">📍 Wien, Österreich (Áo)</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-emerald-100 text-emerald-800 font-bold">das (Giống trung)</span>
                        <button onclick="speakGerman('das Brandenburger Tor in Berlin, Deutschland')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">das Brandenburger Tor</h5>
                    <p class="text-slate-600">Cổng Brandenburg (theo <i>das Tor</i> = cái cổng)</p>
                    <p class="text-indigo-700 font-semibold">📍 Berlin, Deutschland (Đức)</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="px-2 py-0.5 rounded-md bg-blue-100 text-blue-800 font-bold">der (Giống đực)</span>
                        <button onclick="speakGerman('der Rote Platz in Moskau, Russland')" class="text-indigo-600 font-bold hover:underline">🔊</button>
                    </div>
                    <h5 class="text-base font-black text-slate-900">der Rote Platz</h5>
                    <p class="text-slate-600">Quảng trường Đỏ (theo <i>der Platz</i>)</p>
                    <p class="text-indigo-700 font-semibold">📍 Moskau, Russland (Nga)</p>
                </div>
            </div>

            <!-- 2.2 Ba mẫu câu hỏi đáp kinh điển -->
            <div class="p-5 rounded-2xl bg-slate-900 text-white space-y-3 text-xs">
                <p class="text-amber-400 font-bold text-sm">💬 Ba Mẫu Câu Hỏi – Đáp Kinh Điển Về Địa Danh:</p>
                <div class="space-y-2 text-slate-300">
                    <div class="flex items-baseline justify-between border-b border-slate-800 pb-2">
                        <div>
                            <b class="text-white">1. Hỏi tên công trình:</b> <i>Was ist das?</i>
                            <span class="block text-slate-400">→ Trả lời: <b>Das ist die Akropolis. / Das ist das Brandenburger Tor.</b> (giữ nguyên mạo từ ở Nominativ).</span>
                        </div>
                        <button onclick="speakGerman('Was ist das? Das ist die Akropolis.')" class="text-amber-400 font-bold">🔊</button>
                    </div>
                    <div class="flex items-baseline justify-between border-b border-slate-800 pb-2">
                        <div>
                            <b class="text-white">2. Hỏi vị trí thành phố (kèm tiểu từ ngữ khí 'denn'):</b> <i>Wo ist denn das?</i>
                            <span class="block text-slate-400">→ Trả lời: <b>Das ist in Athen. / Das ist in Paris.</b> (Tiểu từ <i>denn</i> thể hiện sự tò mò, thân thiện: "Thế nó ở đâu vậy?").</span>
                        </div>
                        <button onclick="speakGerman('Wo ist denn das? Das ist in Athen.')" class="text-amber-400 font-bold">🔊</button>
                    </div>
                    <div class="flex items-baseline justify-between">
                        <div>
                            <b class="text-white">3. Hỏi quốc gia:</b> <i>In welchem Land ist das?</i>
                            <span class="block text-slate-400">→ Trả lời: <b>Athen ist in Griechenland. / Wien ist in Österreich.</b></span>
                        </div>
                        <button onclick="speakGerman('In welchem Land ist das? Athen ist in Griechenland.')" class="text-amber-400 font-bold">🔊</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: ĐỊNH HƯỚNG BẢN ĐỒ & 8 PHƯƠNG HƯỚNG (HIMMELSRICHTUNGEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">3</span>
                <div>
                    <h4 class="text-lg font-black text-slate-900 tracking-tight">Định Hướng Bản Đồ & Hệ Thống 8 Phương Hướng</h4>
                    <p class="text-xs text-slate-500">Danh từ (der) vs. Tính từ (-lich), quy tắc ghép Bắc/Nam trước Đông/Tây & 2 cách trả lời vị trí</p>
                </div>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-slate-700 space-y-2">
                <p class="font-bold text-amber-900">⚠️ 3 Quy Tắc Vàng Về Phương Hướng Trong Tiếng Đức:</p>
                <p>1. <b>Mọi danh từ chỉ phương hướng đều mang giống đực (der)</b>: <i>der Norden, der Süden, der Osten, der Westen</i>. Khi nói <i>"ở phía..."</i> dùng <b>im (= in dem)</b> + Danh từ phương hướng + <b>von</b>.</p>
                <p>2. <b>Khi chuyển sang Tính từ/Trạng từ chỉ hướng (-lich)</b>: Thêm hậu tố <b>-lich</b>, viết thường và thêm <b>Umlaut (¨)</b>: <i>Norden → <b>nördlich</b></i>, <i>Süden → <b>südlich</b></i>, <i>Osten → <b>östlich</b></i>, <i>Westen → <b>westlich</b></i> (không Umlaut). Khi dùng tính từ <b>tuyệt đối KHÔNG có "im"</b>!</p>
                <p>3. <b>Thứ tự ghép 4 hướng phụ (Đông Bắc, Đông Nam...)</b>: Ngược lại với tiếng Việt, <b>tiếng Đức đặt Bắc (Nord-) / Nam (Süd-) lên trước</b>, sau đó mới ghép với Đông (-osten) / Tây (-westen): <i>Đông Bắc = <b>der Nordosten / nordöstlich</b></i>.</p>
            </div>

            <!-- Bảng 8 phương hướng và vị trí trung tâm -->
            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-left text-xs">
                    <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3">Hướng</th>
                            <th class="p-3">Danh từ (der)</th>
                            <th class="p-3">Cụm Danh từ (im ... von)</th>
                            <th class="p-3">Tính từ (...lich von)</th>
                            <th class="p-3">Ví dụ mẫu chuẩn</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Bắc (North)</td>
                            <td class="p-3 font-bold text-blue-700">der Norden</td>
                            <td class="p-3 font-semibold text-indigo-700">im Norden von</td>
                            <td class="p-3 font-semibold text-purple-700">nördlich von</td>
                            <td class="p-3">Hanoi liegt <b>im Norden von</b> Vietnam (<b>nördlich von</b> Vietnam).</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Nam (South)</td>
                            <td class="p-3 font-bold text-blue-700">der Süden</td>
                            <td class="p-3 font-semibold text-indigo-700">im Süden von</td>
                            <td class="p-3 font-semibold text-purple-700">südlich von</td>
                            <td class="p-3">Long An liegt <b>im Süden von</b> Vietnam (<b>südlich von</b> Vietnam).</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Đông (East)</td>
                            <td class="p-3 font-bold text-blue-700">der Osten</td>
                            <td class="p-3 font-semibold text-indigo-700">im Osten von</td>
                            <td class="p-3 font-semibold text-purple-700">östlich von</td>
                            <td class="p-3">Berlin liegt <b>im Osten von</b> Deutschland.</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Tây (West)</td>
                            <td class="p-3 font-bold text-blue-700">der Westen</td>
                            <td class="p-3 font-semibold text-indigo-700">im Westen von</td>
                            <td class="p-3 font-semibold text-purple-700">westlich von</td>
                            <td class="p-3">Köln liegt <b>im Westen von</b> Deutschland.</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Đông Bắc (Northeast)</td>
                            <td class="p-3 font-bold text-blue-700">der Nordosten</td>
                            <td class="p-3 font-semibold text-indigo-700">im Nordosten von</td>
                            <td class="p-3 font-semibold text-purple-700">nordöstlich von</td>
                            <td class="p-3">Hai Phong liegt <b>im Nordosten von</b> Vietnam.</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Đông Nam (Southeast)</td>
                            <td class="p-3 font-bold text-blue-700">der Südosten</td>
                            <td class="p-3 font-semibold text-indigo-700">im Südosten von</td>
                            <td class="p-3 font-semibold text-purple-700">südöstlich von</td>
                            <td class="p-3">Dresden liegt <b>im Südosten von</b> Deutschland.</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Tây Bắc (Northwest)</td>
                            <td class="p-3 font-bold text-blue-700">der Nordwesten</td>
                            <td class="p-3 font-semibold text-indigo-700">im Nordwesten von</td>
                            <td class="p-3 font-semibold text-purple-700">nordwestlich von</td>
                            <td class="p-3">Dien Bien liegt <b>im Nordwesten von</b> Vietnam.</td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">Tây Nam (Southwest)</td>
                            <td class="p-3 font-bold text-blue-700">der Südwesten</td>
                            <td class="p-3 font-semibold text-indigo-700">im Südwesten von</td>
                            <td class="p-3 font-semibold text-purple-700">südwestlich von</td>
                            <td class="p-3">Can Tho liegt <b>im Südwesten von</b> Vietnam.</td>
                        </tr>
                        <tr class="hover:bg-rose-50/50 transition">
                            <td class="p-3 font-bold text-rose-700">Miền Trung / Ở giữa</td>
                            <td class="p-3 font-bold text-rose-700">die Mitte (Giống cái!)</td>
                            <td class="p-3 font-semibold text-rose-700">in der Mitte von</td>
                            <td class="p-3 italic text-slate-400">— (Không có dạng -lich)</td>
                            <td class="p-3 font-bold text-rose-900">Da Nang liegt <b>in der Mitte von</b> Vietnam.</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Hai cách trả lời câu hỏi Wo liegt...? -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-indigo-50 border border-indigo-200 space-y-1.5">
                    <span class="px-2.5 py-1 rounded-md bg-indigo-600 text-white font-bold">Cách 1: Dùng Cụm Danh Từ (im ... von)</span>
                    <p class="text-slate-800 font-semibold mt-2">Công thức: <code>[Thành phố] + liegt + im [Danh từ hướng] + von + [Quốc gia].</code></p>
                    <p class="text-slate-600 italic">👉 "Hai Phong liegt <b>im Nordosten von</b> Vietnam."</p>
                    <p class="text-slate-600 italic">👉 "München liegt <b>im Süden von</b> Deutschland."</p>
                </div>

                <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 space-y-1.5">
                    <span class="px-2.5 py-1 rounded-md bg-purple-600 text-white font-bold">Cách 2: Dùng Tính Từ (-lich von)</span>
                    <p class="text-slate-800 font-semibold mt-2">Công thức: <code>[Thành phố] + liegt + [Tính từ -lich] + von + [Quốc gia].</code></p>
                    <p class="text-slate-600 italic">👉 "Hai Phong liegt <b>nordöstlich von</b> Vietnam." (Tuyệt đối KHÔNG có "im")</p>
                    <p class="text-slate-600 italic">👉 "München liegt <b>südlich von</b> Deutschland."</p>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: BA CẤU TRÚC CÂU TRỌNG TÂM & 9 TỪ ĐỂ HỎI (W-FRAGEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">4</span>
                <div>
                    <h4 class="text-lg font-black text-slate-900 tracking-tight">Ba Cấu Trúc Câu Cốt Lõi & Bảng 9 Từ Để Hỏi (W-Fragen)</h4>
                    <p class="text-xs text-slate-500">Vị trí động từ chia (Position 1 vs. Position 2) và cách chuyển đổi câu trần thuật sang câu hỏi</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-md bg-blue-100 text-blue-800 font-bold">1. Câu Trần Thuật (Aussagesatz)</span>
                    <p class="font-bold text-slate-900">S + V (Pos 2) + O...</p>
                    <p class="text-slate-600">Động từ chia luôn đứng ở <b>Vị trí thứ 2</b>:</p>
                    <p class="italic text-indigo-700 font-semibold">"Ich (1) <b>komme</b> (2) aus Vietnam (3)."</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-md bg-amber-100 text-amber-800 font-bold">2. Câu Hỏi W-Frage</span>
                    <p class="font-bold text-slate-900">W-Wort (1) + V (Pos 2) + S (3)...?</p>
                    <p class="text-slate-600">Từ để hỏi đứng số 1, động từ giữ <b>Vị trí thứ 2</b>:</p>
                    <p class="italic text-amber-800 font-semibold">"Woher (1) <b>kommen</b> (2) Sie (3)?"</p>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-md bg-emerald-100 text-emerald-800 font-bold">3. Câu Hỏi Ja/Nein-Frage</span>
                    <p class="font-bold text-slate-900">V (Pos 1) + S (2) + O...?</p>
                    <p class="text-slate-600">Đẩy động từ chia lên thẳng <b>Vị trí số 1</b>:</p>
                    <p class="italic text-emerald-800 font-semibold">"<b>Kommen</b> (1) Sie (2) aus Vietnam?"</p>
                </div>
            </div>

            <!-- Bảng 9 từ để hỏi -->
            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-left text-xs">
                    <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3">Từ để hỏi (W-Wort)</th>
                            <th class="p-3">Nghĩa tiếng Việt</th>
                            <th class="p-3">Chức năng & Câu ví dụ chuẩn A1</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Wer</td>
                            <td class="p-3 font-semibold">Ai? (Chủ ngữ)</td>
                            <td class="p-3">Hỏi người: <i>Wer ist das? – Das ist Frau Schiller. / Wer ist sie? – Sie ist Lehrerin.</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Wo</td>
                            <td class="p-3 font-semibold">Ở đâu? (Vị trí tĩnh)</td>
                            <td class="p-3">Hỏi nơi ở: <i>Wo wohnen Sie? – Ich wohne in Hai Phong. / Wo liegt Hanoi?</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Woher</td>
                            <td class="p-3 font-semibold">Từ đâu đến? (Nguồn gốc)</td>
                            <td class="p-3">Hỏi quê quán (đi với <code>aus</code>): <i>Woher kommst du? – Ich komme aus Vietnam.</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Wohin</td>
                            <td class="p-3 font-semibold">Đến đâu? (Hướng di chuyển)</td>
                            <td class="p-3">Hỏi điểm đến (đi với <code>nach / in</code>): <i>Wohin fahren Sie? – Ich fahre nach Berlin.</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Was</td>
                            <td class="p-3 font-semibold">Cái gì? / Làm nghề gì?</td>
                            <td class="p-3">Hỏi sự vật: <i>Was ist das? / Was macht er? – Er macht die Hausaufgaben.</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Wie</td>
                            <td class="p-3 font-semibold">Như thế nào? / Bao nhiêu?</td>
                            <td class="p-3">Hỏi tên, sức khỏe: <i>Wie heißen Sie? / Wie geht es dir? / Wie bitte?</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Wann</td>
                            <td class="p-3 font-semibold">Khi nào?</td>
                            <td class="p-3">Hỏi thời gian: <i>Wann beginnt der Kurs? – Am Montag um 8 Uhr.</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">Warum</td>
                            <td class="p-3 font-semibold">Tại sao?</td>
                            <td class="p-3">Hỏi lý do: <i>Warum lernst du Deutsch? – Für das Studium in Deutschland.</i></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-black text-indigo-700">In welchem / Welche</td>
                            <td class="p-3 font-semibold">... nào?</td>
                            <td class="p-3">Hỏi lựa chọn: <i>In welchem Land ist das? / Welche Sprache sprichst du?</i></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 4 bài mẫu chuyển đổi trên bảng -->
            <div class="space-y-2 text-xs">
                <p class="font-bold text-slate-800">📝 4 Tình Huống Thực Hành Chuyển Đổi Trên Bảng Viết:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <p class="font-bold text-slate-900">1. "Ich heiße Anna." (Tôi tên là Anna)</p>
                        <p class="text-indigo-700 font-medium">→ W-Frage: <b>Wie heißen Sie?</b> (hoặc <i>Wie heißt du?</i>)</p>
                        <p class="text-emerald-700 font-medium">→ Ja/Nein: <b>Heißen Sie Anna?</b> (hoặc <i>Heißt du Anna?</i>)</p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <p class="font-bold text-slate-900">2. "Ich wohne in Hai Phong." (Tôi sống ở Hải Phòng)</p>
                        <p class="text-indigo-700 font-medium">→ W-Frage: <b>Wo wohnen Sie?</b> (hoặc <i>Wo wohnst du?</i>)</p>
                        <p class="text-emerald-700 font-medium">→ Ja/Nein: <b>Wohnen Sie in Hai Phong?</b></p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <p class="font-bold text-slate-900">3. "Er macht die Hausaufgaben." (Anh ấy làm bài tập)</p>
                        <p class="text-indigo-700 font-medium">→ W-Frage: <b>Was macht er?</b></p>
                        <p class="text-emerald-700 font-medium">→ Ja/Nein: <b>Macht er die Hausaufgaben?</b></p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <p class="font-bold text-slate-900">4. "Sie ist Lehrerin." (Cô ấy là giáo viên)</p>
                        <p class="text-indigo-700 font-medium">→ W-Frage: <b>Wer ist sie?</b> (hoặc <i>Was ist sie von Beruf?</i>)</p>
                        <p class="text-emerald-700 font-medium">→ Ja/Nein: <b>Ist sie Lehrerin?</b></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 5: THÌ QUÁ KHỨ ĐƠN (PRÄTERITUM) CỦA SEIN VÀ HABEN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">5</span>
                <div>
                    <h4 class="text-lg font-black text-slate-900 tracking-tight">Thì Quá Khứ Đơn (Präteritum) Của Động Từ "sein" & "haben"</h4>
                    <p class="text-xs text-slate-500">Quy tắc chia gốc war- và hatt-, trạng từ thời gian quá khứ & mẫu hội thoại hỏi trải nghiệm</p>
                </div>
            </div>

            <p class="text-sm text-slate-600">
                Trong tiếng Đức, khi nói về quá khứ, riêng động từ <b>sein</b> (thì, là, ở) và <b>haben</b> (có) thì người Đức <b>luôn luôn ưu tiên dùng thì Quá khứ đơn (Präteritum)</b> trong cả văn nói giao tiếp hàng ngày lẫn văn viết vì câu văn ngắn gọn, thanh thoát và tự nhiên hơn rất nhiều.
            </p>

            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-left text-xs">
                    <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3">Ngôi nhân xưng</th>
                            <th class="p-3">sein ở Hiện tại (Präsens)</th>
                            <th class="p-3 bg-amber-100/60 text-amber-900 font-black">sein ở Quá khứ đơn (Präteritum)</th>
                            <th class="p-3">haben ở Hiện tại (Präsens)</th>
                            <th class="p-3 bg-indigo-100/60 text-indigo-900 font-black">haben ở Quá khứ đơn (Präteritum)</th>
                            <th class="p-3">Phát âm Präteritum</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">ich (tôi)</td>
                            <td class="p-3">bin</td>
                            <td class="p-3 font-black text-amber-900 bg-amber-50/50">war</td>
                            <td class="p-3">habe</td>
                            <td class="p-3 font-black text-indigo-900 bg-indigo-50/50">hatte</td>
                            <td class="p-3"><button onclick="speakGerman('ich war, ich hatte')" class="px-2 py-1 rounded bg-slate-100 text-indigo-600 font-bold hover:bg-indigo-600 hover:text-white transition cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">du (bạn)</td>
                            <td class="p-3">bist</td>
                            <td class="p-3 font-black text-amber-900 bg-amber-50/50">warst</td>
                            <td class="p-3">hast</td>
                            <td class="p-3 font-black text-indigo-900 bg-indigo-50/50">hattest</td>
                            <td class="p-3"><button onclick="speakGerman('du warst, du hattest')" class="px-2 py-1 rounded bg-slate-100 text-indigo-600 font-bold hover:bg-indigo-600 hover:text-white transition cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-amber-100/30 transition">
                            <td class="p-3 font-bold text-slate-900">er / sie / es (anh/cô ấy/nó)</td>
                            <td class="p-3">ist</td>
                            <td class="p-3 font-black text-amber-900 bg-amber-100/60">war <span class="text-[10px] text-amber-700 font-semibold">(giống hệt ich!)</span></td>
                            <td class="p-3">hat</td>
                            <td class="p-3 font-black text-indigo-900 bg-indigo-100/60">hatte <span class="text-[10px] text-indigo-700 font-semibold">(giống hệt ich!)</span></td>
                            <td class="p-3"><button onclick="speakGerman('er war, er hatte')" class="px-2 py-1 rounded bg-slate-100 text-indigo-600 font-bold hover:bg-indigo-600 hover:text-white transition cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">wir (chúng tôi)</td>
                            <td class="p-3">sind</td>
                            <td class="p-3 font-black text-amber-900 bg-amber-50/50">waren</td>
                            <td class="p-3">haben</td>
                            <td class="p-3 font-black text-indigo-900 bg-indigo-50/50">hatten</td>
                            <td class="p-3"><button onclick="speakGerman('wir waren, wir hatten')" class="px-2 py-1 rounded bg-slate-100 text-indigo-600 font-bold hover:bg-indigo-600 hover:text-white transition cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">ihr (các bạn)</td>
                            <td class="p-3">seid</td>
                            <td class="p-3 font-black text-amber-900 bg-amber-50/50">wart</td>
                            <td class="p-3">habt</td>
                            <td class="p-3 font-black text-indigo-900 bg-indigo-50/50">hattet</td>
                            <td class="p-3"><button onclick="speakGerman('ihr wart, ihr hattet')" class="px-2 py-1 rounded bg-slate-100 text-indigo-600 font-bold hover:bg-indigo-600 hover:text-white transition cursor-pointer">🔊</button></td>
                        </tr>
                        <tr class="hover:bg-slate-50 transition">
                            <td class="p-3 font-bold text-slate-900">sie / Sie (họ / Ngài)</td>
                            <td class="p-3">sind</td>
                            <td class="p-3 font-black text-amber-900 bg-amber-50/50">waren</td>
                            <td class="p-3">haben</td>
                            <td class="p-3 font-black text-indigo-900 bg-indigo-50/50">hatten</td>
                            <td class="p-3"><button onclick="speakGerman('sie waren, Sie waren')" class="px-2 py-1 rounded bg-slate-100 text-indigo-600 font-bold hover:bg-indigo-600 hover:text-white transition cursor-pointer">🔊</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 space-y-1.5">
                    <p class="font-bold text-amber-900">⏰ Dấu hiệu nhận biết thì Quá khứ (Präteritum):</p>
                    <p>• <b>gestern</b>: hôm qua (<i>Gestern waren wir in Haiphong.</i>)</p>
                    <p>• <b>vorgestern</b>: hôm kia</p>
                    <p>• <b>früher</b>: trước đây, ngày xưa</p>
                    <p>• <b>letzte Woche / letztes Jahr</b>: tuần trước / năm ngoái</p>
                    <p>• <b>schon</b>: đã từng (<i>Warst du schon in Hanoi?</i>)</p>
                </div>

                <div class="p-4 rounded-2xl bg-indigo-50 border border-indigo-200 space-y-1.5">
                    <p class="font-bold text-indigo-900">✈️ Mẫu Hội Thoại Hỏi Trải Nghiệm Du Lịch:</p>
                    <p class="italic">A: <b>"Warst du schon in Hanoi?"</b> (Bạn đã từng ở Hà Nội chưa?)</p>
                    <p class="italic text-emerald-800">B: <b>"Ja, ich war schon in Hanoi."</b> (Rồi, mình đã từng ở Hà Nội.)</p>
                    <p class="italic text-rose-800">C: <b>"Nein, wo ist denn das?"</b> (Chưa, thế nó ở đâu vậy?)</p>
                    <p class="italic text-indigo-800">A: <b>"Hanoi liegt im Norden von Vietnam."</b></p>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 6: PHÂN TÍCH HỘI THOẠI ĐIỀN TỪ & BƯU THIẾP DU LỊCH HẢI PHÒNG -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-600 text-white font-extrabold flex items-center justify-center text-sm shadow-sm">6</span>
                <div>
                    <h4 class="text-lg font-black text-slate-900 tracking-tight">Phân Tích Hội Thoại Carlos & Bưu Thiếp Du Lịch Hải Phòng</h4>
                    <p class="text-xs text-slate-500">Phân tích văn bản gốc bưu thiếp của Paula & Peter, đảo ngữ khi trạng từ đứng đầu và 4 cụm giới từ Dativ</p>
                </div>
            </div>

            <!-- Đoạn hội thoại Carlos -->
            <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-xs space-y-2">
                <div class="flex items-center justify-between">
                    <h5 class="font-bold text-slate-900">💬 Đoạn Hội Thoại Carlos & Người Bạn (Athen / Wien):</h5>
                    <button onclick="speakGerman('Carlos, woher kommst du? Ich komme aus Wien. Das ist in Österreich.')" class="px-2 py-1 rounded bg-indigo-50 text-indigo-700 font-bold hover:bg-indigo-100 transition cursor-pointer">🔊 Nghe hội thoại</button>
                </div>
                <div class="space-y-1 text-slate-700 leading-relaxed">
                    <p><b>A:</b> Carlos, woher <b>kommst</b> du?</p>
                    <p><b>Carlos:</b> Ich <b>komme</b> aus Wien. Das <b>ist</b> in Österreich. Und du, woher <b>kommst</b> du?</p>
                    <p><b>A:</b> Ich <b>komme</b> aus Athen. <b>Warst</b> du schon in Athen?</p>
                    <p><b>Carlos:</b> Nein, wo <b>ist</b> denn das?</p>
                    <p><b>A:</b> Das <b>ist</b> in Griechenland.</p>
                </div>
            </div>

            <!-- Bưu thiếp Hải Phòng -->
            <div class="p-6 rounded-3xl bg-gradient-to-br from-amber-50 to-orange-50 border border-amber-200 text-slate-800 space-y-3 relative shadow-xs">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="px-3 py-1 rounded-full bg-amber-200 text-amber-900 font-bold text-xs">✉️ Bưu Thiếp Du Lịch Hải Phòng Gửi Anna</span>
                    <button onclick="speakGerman('Liebe Anna, gestern waren Paula und ich in Haiphong. Ich war im BigC Supermarkt und Paula im Theater. Wart ihr schon auf dem Cat Bi Markt? Der Cat Bi Markt war sehr interessant. Hier sind ein paar Fotos. Es war super! Heute sind wir am Do Son Meer. Viele Grüße, Paula und Peter')" class="px-3 py-1.5 rounded-xl bg-amber-600 text-white font-bold text-xs hover:bg-amber-700 transition flex items-center gap-1.5 cursor-pointer">
                        🔊 Nghe toàn bộ bức thư
                    </button>
                </div>

                <div class="p-5 rounded-2xl bg-white/90 border border-amber-200/80 font-serif text-xs leading-relaxed space-y-2 text-slate-900">
                    <p class="font-bold text-amber-950 text-sm">Liebe Anna,</p>
                    <p>
                        <b>gestern</b> <b>waren</b> Paula und ich in Haiphong. <b>Ich</b> <b>war</b> im BigC Supermarkt und <b>Paula</b> [war] im Theater. <b>Wart</b> <b>ihr</b> schon auf dem Cat Bi Markt? Der Cat Bi Markt <b>war</b> sehr interessant. Hier <b>sind</b> ein paar Fotos. Es <b>war</b> super! <b>Heute</b> <b>sind</b> wir am Do Son Meer.
                    </p>
                    <p class="pt-2">Viele Grüße<br><b>Paula und Peter</b></p>
                </div>

                <div class="text-xs text-slate-700 space-y-1.5 pt-2">
                    <p class="font-bold text-amber-950">🔍 Phân tích Ngữ pháp Đắt giá:</p>
                    <p>1. <b>gestern waren Paula und ich...</b>: Khi trạng ngữ thời gian <code>gestern</code> đứng Vị trí 1, động từ chia ở quá khứ <b>waren</b> giữ vững ở Vị trí 2, chủ ngữ <b>Paula und ich</b> (= <i>wir</i>) lùi về Vị trí 3!</p>
                    <p>2. <b>4 Cụm Giới từ Chỉ Địa Điểm (Cách 3 - Dativ) cần thuộc lòng:</b></p>
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1 font-mono text-[11px]">
                        <span class="p-2 rounded-lg bg-white border border-amber-200 text-slate-800"><b>im Supermarkt</b><br><span class="text-slate-500 font-sans">(in dem)</span></span>
                        <span class="p-2 rounded-lg bg-white border border-amber-200 text-slate-800"><b>im Theater</b><br><span class="text-slate-500 font-sans">(in dem)</span></span>
                        <span class="p-2 rounded-lg bg-white border border-amber-200 text-slate-800"><b>auf dem Markt</b><br><span class="text-slate-500 font-sans">(trên chợ)</span></span>
                        <span class="p-2 rounded-lg bg-white border border-amber-200 text-slate-800"><b>am Do Son Meer</b><br><span class="text-slate-500 font-sans">(an dem)</span></span>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 7: TỔNG KẾT NGỮ PHÁP VÀ MẪU CÂU CỐT LÕI BÀI 3 -->
        <div class="p-6 rounded-3xl bg-indigo-950 text-white shadow-xl border border-indigo-900 space-y-4">
            <h4 class="text-lg font-black tracking-tight text-white flex items-center gap-2">
                <span>🎯</span> Tổng Kết Ngữ Pháp Cốt Lõi Bài 3 (A1 Checklist)
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-white/10 border border-white/10 space-y-2">
                    <p class="text-amber-400 font-bold">1. Địa danh & Phương hướng:</p>
                    <p>• Quốc gia có mạo từ: <i>aus/in der Schweiz, aus/in der Türkei, aus dem / im Iran, aus/in den USA</i>.</p>
                    <p>• 7 Danh thắng: <i>die Akropolis, der Big Ben, der Eiffelturm, der Schiefe Turm, der Prater, das Brandenburger Tor, der Rote Platz</i>.</p>
                    <p>• 2 cách viết vị trí: <i>liegt im Norden von...</i> (danh từ) = <i>liegt nördlich von...</i> (tính từ).</p>
                </div>
                <div class="p-4 rounded-2xl bg-white/10 border border-white/10 space-y-2">
                    <p class="text-emerald-400 font-bold">2. Quá khứ Präteritum & Cấu trúc câu:</p>
                    <p>• Động từ <b>sein</b> ở Quá khứ: <i>ich war, du warst, er/sie/es war, wir waren, ihr wart, sie/Sie waren</i>.</p>
                    <p>• Động từ <b>haben</b> ở Quá khứ: <i>ich hatte, du hattest, er hatte, wir hatten, ihr hattet, sie hatten</i>.</p>
                    <p>• Đảo ngữ: <i>Gestern waren wir in Haiphong.</i> (Động từ luôn đứng vị trí 2 trong câu trần thuật).</p>
                </div>
            </div>
        </div>
    </div>
    """

    cursor.execute("""
        INSERT INTO lessons (level_id, title, grammar_content)
        VALUES (?, ?, ?);
    """, (a1_id, lesson_title, grammar_html))
    lesson_id = cursor.lastrowid

    # =========================================================================
    # NẠP TỪ VỰNG BÀI 3 (35+ TỪ VỰNG CHUẨN ĐẶC TẢ)
    # =========================================================================
    vocabularies = [
        # Quốc gia & Ngôn ngữ
        (lesson_id, "Deutschland", "das", "nước Đức", "Ich komme aus Deutschland und spreche Deutsch."),
        (lesson_id, "Österreich", "das", "nước Áo", "Wien liegt in Österreich. Man spricht dort Deutsch."),
        (lesson_id, "Italien", "das", "nước Ý", "Pisa ist in Italien. Sie spricht gut Italienisch."),
        (lesson_id, "Spanien", "das", "Tây Ban Nha", "Carlos kommt aus Spanien und spricht Spanisch."),
        (lesson_id, "Griechenland", "das", "Hy Lạp", "Athen ist in Griechenland. Er lernt Griechisch."),
        (lesson_id, "Frankreich", "das", "nước Pháp", "Der Eiffelturm ist in Frankreich. Wir sprechen Französisch."),
        (lesson_id, "England", "das", "nước Anh (Großbritannien)", "Big Ben ist in England. Sprichst du Englisch?"),
        (lesson_id, "Polen", "das", "Ba Lan", "Mein Freund kommt aus Polen und spricht Polnisch."),
        (lesson_id, "Tschechien", "das", "Cộng hòa Séc", "Prag liegt in Tschechien. Dort spricht man Tschechisch."),
        (lesson_id, "Russland", "das", "nước Nga", "Moskau ist in Russland. Anna spricht Russisch."),
        (lesson_id, "China", "das", "Trung Quốc", "Frau Wang kommt aus China und spricht Chinesisch."),
        (lesson_id, "Vietnam", "das", "Việt Nam", "Ich komme aus Vietnam und spreche Vietnamesisch."),
        # Quốc gia có mạo từ
        (lesson_id, "Schweiz", "die", "Thụy Sỹ (aus der / in der Schweiz)", "Meine Tante wohnt in der Schweiz. Dort spricht man Deutsch, Französisch und Italienisch."),
        (lesson_id, "Türkei", "die", "Thổ Nhĩ Kỳ (aus der / in der Türkei)", "Er kommt aus der Türkei und spricht Türkisch."),
        (lesson_id, "Slowakei", "die", "Slovakia (aus der / in der Slowakei)", "Bratislava liegt in der Slowakei. Man spricht dort Slowakisch."),
        (lesson_id, "Iran", "der", "Iran (aus dem / im Iran)", "Mein Kollege kommt aus dem Iran. Er spricht Persisch."),
        (lesson_id, "USA", "die (Pl.)", "Hợp chủng quốc Hoa Kỳ - Mỹ (aus den / in den USA)", "Die Lehrerin kommt aus den USA."),
        (lesson_id, "Niederlande", "die (Pl.)", "Hà Lan (aus den / in den Niederlanden)", "Amsterdam ist in den Niederlanden."),
        # 7 Danh lam thắng cảnh
        (lesson_id, "Sehenswürdigkeit", "die", "danh lam thắng cảnh, điểm tham quan", "Der Eiffelturm ist eine berühmte Sehenswürdigkeit in Europa."),
        (lesson_id, "Akropolis", "die", "Thành cổ Akropolis (ở Athen, Griechenland)", "Was ist das? – Das ist die Akropolis. Sie liegt in Athen."),
        (lesson_id, "Big Ben", "der", "Tháp đồng hồ Big Ben (ở London, England)", "Wo ist der Big Ben? – Er ist in London, England."),
        (lesson_id, "Eiffelturm", "der", "Tháp Eiffel (ở Paris, Frankreich)", "Der Eiffelturm steht in Paris. Paris liegt in Frankreich."),
        (lesson_id, "Schiefe Turm", "der", "Tháp nghiêng Pisa (ở Pisa, Italien)", "Wo ist der Schiefe Turm? – Er ist in Pisa, Italien."),
        (lesson_id, "Prater", "der", "Công viên giải trí Prater (ở Wien, Österreich)", "Der Prater ist in Wien. Wien liegt im Osten von Österreich."),
        (lesson_id, "Brandenburger Tor", "das", "Cổng Brandenburg (ở Berlin, Deutschland)", "Das Brandenburger Tor ist in Berlin, Deutschland."),
        (lesson_id, "Rote Platz", "der", "Quảng trường Đỏ (ở Moskau, Russland)", "Der Rote Platz ist in Moskau. Moskau liegt in Russland."),
        # Phương hướng
        (lesson_id, "Norden", "der", "phía Bắc, miền Bắc (im Norden von / nördlich von)", "Hanoi liegt im Norden von Vietnam."),
        (lesson_id, "Süden", "der", "phía Nam, miền Nam (im Süden von / südlich von)", "Long An liegt im Süden von Vietnam."),
        (lesson_id, "Osten", "der", "phía Đông, miền Đông (im Osten von / östlich von)", "Berlin liegt im Osten von Deutschland."),
        (lesson_id, "Westen", "der", "phía Tây, miền Tây (im Westen von / westlich von)", "Köln liegt im Westen von Deutschland."),
        (lesson_id, "Nordosten", "der", "phía Đông Bắc (im Nordosten von / nordöstlich von)", "Hai Phong liegt im Nordosten von Vietnam."),
        (lesson_id, "Mitte", "die", "miền Trung, trung tâm (in der Mitte von)", "Da Nang liegt in der Mitte von Vietnam."),
        (lesson_id, "Landkarte", "die", "bản đồ địa lý", "Wir sehen die Städte auf der Landkarte."),
        # Du lịch & Bưu thiếp
        (lesson_id, "Supermarkt", "der", "siêu thị (im BigC Supermarkt)", "Ich war gestern im BigC Supermarkt."),
        (lesson_id, "Theater", "das", "nhà hát (im Theater)", "Paula war im Theater in Haiphong."),
        (lesson_id, "Markt", "der", "chợ (auf dem Cat Bi Markt)", "Wart ihr schon auf dem Cat Bi Markt?"),
        (lesson_id, "Meer", "das", "biển (am Do Son Meer)", "Heute sind wir am Do Son Meer."),
        (lesson_id, "Hausaufgabe", "die", "bài tập về nhà", "Er macht die Hausaufgaben.")
    ]

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # NẠP KHO 50 CÂU HỎI BÀI 3 (ĐỦ 7 DẠNG KỸ NĂNG: 10 + 10 + 8 + 6 + 5 + 4 + 7)
    # =========================================================================
    exercises = [
        # --- DẠNG 1: TRẮC NGHIỆM (10 CÂU) ---
        (
            lesson_id, "trac_nghiem",
            "Câu 1: Quốc gia nào dưới đây bắt buộc phải đi kèm mạo từ 'die' ở Nominativ?",
            json.dumps(["Deutschland", "Österreich", "die Schweiz", "Spanien"]),
            "die Schweiz",
            "'die Schweiz' (Thụy Sỹ) là quốc gia mang giống cái, bắt buộc đi kèm mạo từ.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 2: Tại nước Áo (Österreich), ngôn ngữ chính thức được người dân sử dụng là gì?",
            json.dumps(["Österreichisch", "Deutsch", "Englisch", "Französisch"]),
            "Deutsch",
            "Nước Áo (Österreich) sử dụng tiếng Đức (Deutsch) là ngôn ngữ chính thức.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 3: Ngôn ngữ chính thức của đất nước Iran (der Iran) là gì?",
            json.dumps(["Iranisch", "Arabisch", "Persisch", "Türkisch"]),
            "Persisch",
            "Tại Iran (der Iran), ngôn ngữ chính thức là tiếng Ba Tư (Persisch).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 4: Danh thắng tháp Eiffel ('der Eiffelturm') nằm ở thành phố và quốc gia nào?",
            json.dumps(["Berlin, Deutschland", "Paris, Frankreich", "London, England", "Rom, Italien"]),
            "Paris, Frankreich",
            "Tháp Eiffel ('der Eiffelturm') tọa lạc tại thủ đô Paris, nước Pháp (Frankreich).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 5: Công trình Cổng Brandenburg ('das Brandenburger Tor') đi kèm mạo từ gì ở Nominativ?",
            json.dumps(["der", "die", "das", "die (Plural)"]),
            "das",
            "'das Brandenburger Tor' mang giống trung (das) theo danh từ chính 'das Tor' (cái cổng).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 6: Theo quy tắc phương hướng tiếng Đức, phía 'Đông Bắc' được ghép như thế nào?",
            json.dumps(["der Ostennorden", "der Nordosten", "der Ostnord", "der Nordost"]),
            "der Nordosten",
            "Tiếng Đức lấy Bắc (Nord-) ghép trước Đông (-osten) tạo thành 'der Nordosten'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 7: Điền dạng quá khứ Präteritum của 'sein': 'Gestern ___ Paula und ich in Haiphong.'",
            json.dumps(["war", "warst", "waren", "wart"]),
            "waren",
            "Chủ ngữ 'Paula und ich' tương đương với ngôi 'wir' (chúng tôi) → chia là 'waren'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 8: Ở thì Quá khứ đơn (Präteritum) của 'sein', ngôi 'er/sie/es' được chia như thế nào?",
            json.dumps(["wart", "ware", "war", "warst"]),
            "war",
            "Quy tắc vàng: Ngôi thứ 3 số ít (er/sie/es) và ngôi thứ nhất (ich) chia giống hệt nhau: 'war'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 9: Trong bức thư Hải Phòng, giới từ nào đi với chợ ngoài trời Cát Bi Markt? '___ dem Cat Bi Markt'",
            json.dumps(["im", "auf", "an", "bei"]),
            "auf",
            "Chợ ngoài trời hoặc quảng trường dùng giới từ 'auf dem': 'auf dem Cat Bi Markt'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 10 [Dynamic Thắng cảnh]: Công trình 'die Akropolis' nằm ở thành phố nào?",
            json.dumps(["Athen", "London", "Paris", "Wien"]),
            "Athen",
            "'die Akropolis' là thành cổ nổi tiếng tọa lạc tại thủ đô Athen (Athens), Hy Lạp.",
            15,
            json.dumps({"dynamic_landmark_quiz": True})
        ),

        # --- DẠNG 2: ĐIỀN KHUYẾT (10 CÂU) ---
        (
            lesson_id, "dien_khuyet",
            "Câu 11: Điền cụm giới từ thích hợp: 'Hanoi liegt ___ Norden von Vietnam.'",
            None,
            "im",
            "Dùng cụm danh từ phương hướng: 'im Norden von Vietnam' (ở miền Bắc Việt Nam).",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 12: Điền tính từ phương hướng tận cùng bằng đuôi -lich: 'Hai Phong liegt ___ von Vietnam.'",
            None,
            "nordöstlich",
            "Tính từ chỉ hướng Đông Bắc là 'nordöstlich' (không có 'im' phía trước).",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 13: Điền cụm từ chỉ miền Trung: 'Da Nang liegt ___ Mitte von Vietnam.'",
            None,
            "in der",
            "Vì 'die Mitte' mang giống cái nên ở Dativ phải dùng 'in der Mitte von Vietnam'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 14: Điền dạng quá khứ của 'sein' cho ngôi 'du': '___ du schon in Athen?'",
            None,
            "Warst",
            "Câu hỏi quá khứ với chủ ngữ 'du' đảo 'Warst' lên đầu câu.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 15: Điền dạng quá khứ của 'sein' cho ngôi 'ich': 'Gestern ___ ich im BigC Supermarkt.'",
            None,
            "war",
            "Chủ ngữ 'ich' đi với thì Präteritum của 'sein' là 'war'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 16: Điền dạng quá khứ của 'sein' cho ngôi 'ihr': '___ ihr schon auf dem Cat Bi Markt?'",
            None,
            "Wart",
            "Chủ ngữ 'ihr' đi với thì Präteritum của 'sein' là 'wart' (viết hoa đầu câu: Wart).",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 17: Điền 2 động từ chia thích hợp (cách nhau bởi dấu phẩy): 'Carlos, woher ___ du? – Ich ___ aus Wien.'",
            None,
            "kommst, komme",
            "Chủ ngữ 'du' chia là 'kommst'; chủ ngữ 'ich' chia là 'komme'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 18: Điền mạo từ ở Dativ sau giới từ 'aus': 'Meine Tante kommt aus ___ Schweiz.'",
            None,
            "der",
            "'die Schweiz' mang giống cái, sau giới từ 'aus' đổi thành 'der' ('aus der Schweiz').",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 19: Điền mạo từ ở Dativ sau giới từ 'in': 'New York liegt in ___ USA.'",
            None,
            "den",
            "'die USA' là danh từ số nhiều, sau giới từ 'in' đổi thành 'den' ('in den USA').",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 20 [Dynamic Präteritum]: Điền dạng quá khứ của động từ 'sein' cho chủ ngữ trong ngoặc: 'Gestern ___ Paula in Haiphong.'",
            None,
            "war",
            "Paula (ngôi thứ 3 số ít = sie) chia ở Präteritum là 'war'.",
            15,
            json.dumps({"dynamic_praeteritum_quiz": True})
        ),

        # --- DẠNG 3: DỊCH 2 CHIỀU VIỆT ⇄ ĐỨC (8 CÂU) ---
        (
            lesson_id, "dich",
            "Câu 21: Dịch câu sau sang tiếng Đức (dùng cụm danh từ 'im ... von'): 'Hải Phòng nằm ở phía Đông Bắc của Việt Nam.'",
            None,
            "Hai Phong liegt im Nordosten von Vietnam. / Hai Phong liegt nordöstlich von Vietnam.",
            "Dùng cụm danh từ: 'Hai Phong liegt im Nordosten von Vietnam.' hoặc tính từ 'Hai Phong liegt nordöstlich von Vietnam.'",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 22: Dịch câu sau sang tiếng Đức: 'Đà Nẵng nằm ở miền Trung của Việt Nam.'",
            None,
            "Da Nang liegt in der Mitte von Vietnam.",
            "Miền Trung dùng cụm cố định: 'Da Nang liegt in der Mitte von Vietnam.'",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 23: Dịch câu sau sang tiếng Đức: 'Long An nằm ở miền Nam của Việt Nam.'",
            None,
            "Long An liegt im Süden von Vietnam. / Long An liegt südlich von Vietnam.",
            "Long An nằm ở miền Nam: 'Long An liegt im Süden von Vietnam.' hoặc 'Long An liegt südlich von Vietnam.'",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 24: Dịch câu sau sang tiếng Đức (câu hỏi trải nghiệm quá khứ thân mật 'du'): 'Bạn đã từng đến Hà Nội chưa?'",
            None,
            "Warst du schon in Hanoi?",
            "Câu hỏi trải nghiệm với 'schon' và 'sein' ở quá khứ: 'Warst du schon in Hanoi?'",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 25: Dịch câu sau sang tiếng Đức: 'Hôm qua Paula và tôi đã ở Hải Phòng.'",
            None,
            "Gestern waren Paula und ich in Haiphong. / Paula und ich waren gestern in Haiphong.",
            "Đưa trạng từ 'gestern' lên đầu: 'Gestern waren Paula und ich in Haiphong.'",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 26: Dịch câu sau sang tiếng Đức: 'Tháp Eiffel nằm ở Paris, nước Pháp.'",
            None,
            "Der Eiffelturm ist in Paris, Frankreich. / Der Eiffelturm liegt in Paris, Frankreich.",
            "Tháp Eiffel: 'Der Eiffelturm ist in Paris, Frankreich.' (hoặc 'liegt in').",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 27: Dịch câu sau sang tiếng Đức: 'Ở Thụy Sỹ người ta nói tiếng Đức, tiếng Pháp và tiếng Ý.'",
            None,
            "In der Schweiz spricht man Deutsch, Französisch und Italienisch.",
            "Ở Thụy Sỹ: 'In der Schweiz spricht man Deutsch, Französisch und Italienisch.'",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 28 [Dynamic Phương hướng]: Viết câu miêu tả vị trí địa lý của thành phố: 'Hanoi liegt im Norden von Vietnam.'",
            None,
            "Hanoi liegt im Norden von Vietnam. / Hanoi liegt nördlich von Vietnam.",
            "Vị trí địa lý chuẩn: 'Hanoi liegt im Norden von Vietnam.' (hoặc 'nördlich von Vietnam').",
            20,
            json.dumps({"dynamic_direction_quiz": True})
        ),

        # --- DẠNG 4: LUYỆN NGHE (6 CÂU) ---
        (
            lesson_id, "nghe",
            "Câu 29: Nghe âm thanh chuẩn 1.0x / 0.65x và nhập lại câu nói tiếng Đức:",
            None,
            "Das Brandenburger Tor ist in Berlin.",
            "Âm thanh phát âm: 'Das Brandenburger Tor ist in Berlin.' (Cổng Brandenburg ở Berlin).",
            20,
            json.dumps({"audio_text": "Das Brandenburger Tor ist in Berlin."})
        ),
        (
            lesson_id, "nghe",
            "Câu 30: Nghe âm thanh chuẩn 1.0x / 0.65x và nhập lại câu nói tiếng Đức:",
            None,
            "Gestern waren wir in Haiphong. Es war super!",
            "Âm thanh phát âm: 'Gestern waren wir in Haiphong. Es war super!'",
            20,
            json.dumps({"audio_text": "Gestern waren wir in Haiphong. Es war super!"})
        ),
        (
            lesson_id, "nghe",
            "Câu 31: Nghe âm thanh chuẩn 1.0x / 0.65x và nhập lại câu nói tiếng Đức:",
            None,
            "Athen ist in Griechenland.",
            "Âm thanh phát âm: 'Athen ist in Griechenland.' (Athens nằm ở Hy Lạp).",
            20,
            json.dumps({"audio_text": "Athen ist in Griechenland."})
        ),
        (
            lesson_id, "nghe",
            "Câu 32: Nghe âm thanh chuẩn 1.0x / 0.65x và nhập lại câu nói tiếng Đức:",
            None,
            "Der Cat Bi Markt war sehr interessant.",
            "Âm thanh phát âm: 'Der Cat Bi Markt war sehr interessant.'",
            20,
            json.dumps({"audio_text": "Der Cat Bi Markt war sehr interessant."})
        ),
        (
            lesson_id, "nghe",
            "Câu 33: Nghe âm thanh chuẩn 1.0x / 0.65x và nhập lại câu nói tiếng Đức:",
            None,
            "Er kommt aus der Türkei und spricht Türkisch.",
            "Âm thanh phát âm: 'Er kommt aus der Türkei und spricht Türkisch.'",
            20,
            json.dumps({"audio_text": "Er kommt aus der Türkei und spricht Türkisch."})
        ),
        (
            lesson_id, "nghe",
            "Câu 34: Nghe âm thanh chuẩn 1.0x / 0.65x và nhập lại câu nói tiếng Đức:",
            None,
            "Wien liegt in Österreich. Man spricht dort Deutsch.",
            "Âm thanh phát âm: 'Wien liegt in Österreich. Man spricht dort Deutsch.'",
            20,
            json.dumps({"audio_text": "Wien liegt in Österreich. Man spricht dort Deutsch."})
        ),

        # --- DẠNG 5: LUYỆN NÓI & PHÁT ÂM (5 CÂU) ---
        (
            lesson_id, "noi",
            "Câu 35: Luyện phát âm câu vị trí địa lý của Hải Phòng:",
            None,
            "Hai Phong liegt im Nordosten von Vietnam.",
            "Bấm vào biểu tượng loa để nghe giọng đọc bản xứ de-DE và luyện đọc to thành tiếng.",
            20,
            json.dumps({"audio_text": "Hai Phong liegt im Nordosten von Vietnam."})
        ),
        (
            lesson_id, "noi",
            "Câu 36: Luyện phát âm câu vị trí địa lý của Đà Nẵng:",
            None,
            "Da Nang liegt in der Mitte von Vietnam.",
            "Luyện phát âm chuẩn: 'Da Nang liegt in der Mitte von Vietnam.'",
            20,
            json.dumps({"audio_text": "Da Nang liegt in der Mitte von Vietnam."})
        ),
        (
            lesson_id, "noi",
            "Câu 37: Luyện phát âm câu hội thoại hỏi thăm vị trí:",
            None,
            "Warst du schon in Athen? – Nein, wo ist denn das?",
            "Luyện phát âm ngữ điệu tự nhiên của tiểu từ 'denn': 'Warst du schon in Athen? – Nein, wo ist denn das?'",
            20,
            json.dumps({"audio_text": "Warst du schon in Athen? Nein, wo ist denn das?"})
        ),
        (
            lesson_id, "noi",
            "Câu 38: Luyện phát âm đoạn thư quá khứ du lịch Hải Phòng:",
            None,
            "Gestern waren Paula und ich in Haiphong. Es war super!",
            "Luyện phát âm chuẩn đuôi 'waren' và 'war': 'Gestern waren Paula und ich in Haiphong. Es war super!'",
            20,
            json.dumps({"audio_text": "Gestern waren Paula und ich in Haiphong. Es war super!"})
        ),
        (
            lesson_id, "noi",
            "Câu 39: Luyện phát âm câu về các ngôn ngữ của Thụy Sỹ:",
            None,
            "In der Schweiz spricht man Deutsch, Französisch und Italienisch.",
            "Luyện phát âm chuẩn các ngôn ngữ: 'In der Schweiz spricht man Deutsch, Französisch und Italienisch.'",
            20,
            json.dumps({"audio_text": "In der Schweiz spricht man Deutsch, Französisch und Italienisch."})
        ),

        # --- DẠNG 6: ĐỌC HIỂU BƯU THIẾP HẢI PHÒNG (4 CÂU) ---
        (
            lesson_id, "doc",
            "Câu 40 [Đọc hiểu Bưu thiếp]: Dựa vào bức thư của Paula & Peter, ai là người nhận bức thư bưu thiếp này?",
            json.dumps(["Anna", "Paula", "Peter", "Carlos"]),
            "Anna",
            "Bức thư mở đầu bằng 'Liebe Anna,' → Người nhận thư là Anna.",
            20, None
        ),
        (
            lesson_id, "doc",
            "Câu 41 [Đọc hiểu Bưu thiếp]: Ngày hôm qua ('gestern'), Paula đã ở địa điểm nào?",
            json.dumps(["im BigC Supermarkt", "im Theater", "am Do Son Meer", "in Hanoi"]),
            "im Theater",
            "Bức thư nêu rõ: 'Ich war im BigC Supermarkt und Paula [war] im Theater.' → Paula đã ở trong nhà hát.",
            20, None
        ),
        (
            lesson_id, "doc",
            "Câu 42 [Đọc hiểu Bưu thiếp]: Chợ Cát Bi ('der Cat Bi Markt') được nhận xét như thế nào?",
            json.dumps(["sehr groß", "sehr interessant", "sehr teuer", "nicht schön"]),
            "sehr interessant",
            "Bức thư viết: 'Der Cat Bi Markt war sehr interessant.' (Chợ Cát Bi đã rất thú vị).",
            20, None
        ),
        (
            lesson_id, "doc",
            "Câu 43 [Đọc hiểu Bưu thiếp]: Ngày hôm nay ('heute'), Paula và Peter đang ở địa điểm nào?",
            json.dumps(["im Supermarkt", "im Theater", "auf dem Markt", "am Do Son Meer"]),
            "am Do Son Meer",
            "Bức thư viết: 'Heute sind wir am Do Son Meer.' (Hôm nay chúng mình đang ở biển Đồ Sơn).",
            20, None
        ),

        # --- DẠNG 7: VIẾT CÂU & CHUYỂN ĐỔI CÂU HỎI (7 CÂU) ---
        (
            lesson_id, "viet",
            "Câu 44: Hãy chuyển câu trần thuật 'Ich heiße Anna.' sang câu hỏi có từ để hỏi (W-Frage):",
            None,
            "Wie heißen Sie? / Wie heißt du?",
            "Khi hỏi tên với động từ 'heißen', dùng từ để hỏi 'Wie': 'Wie heißen Sie?' (hoặc 'Wie heißt du?').",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 45: Hãy chuyển câu trần thuật 'Ich wohne in Hai Phong.' sang câu hỏi Có/Không (Ja/Nein-Frage):",
            None,
            "Wohnen Sie in Hai Phong? / Wohnst du in Hai Phong?",
            "Đẩy động từ lên đầu câu để tạo Ja/Nein-Frage: 'Wohnen Sie in Hai Phong?' (hoặc 'Wohnst du in Hai Phong?').",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 46: Hãy chuyển câu trần thuật 'Er macht die Hausaufgaben.' sang câu hỏi có từ để hỏi (W-Frage):",
            None,
            "Was macht er?",
            "Hỏi cho hành động làm bài tập dùng từ để hỏi 'Was': 'Was macht er?' (Anh ấy đang làm gì?).",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 47: Hãy chuyển câu trần thuật 'Sie ist Lehrerin.' sang câu hỏi Có/Không (Ja/Nein-Frage):",
            None,
            "Ist sie Lehrerin?",
            "Đảo động từ 'ist' lên đầu câu: 'Ist sie Lehrerin?' (Cô ấy có phải là giáo viên không?).",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 48: Hãy chuyển câu trần thuật 'Carlos kommt aus Wien.' sang câu hỏi có từ để hỏi (W-Frage):",
            None,
            "Woher kommt Carlos? / Woher kommt er?",
            "Hỏi quê quán, nguồn gốc dùng 'Woher': 'Woher kommt Carlos?'",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 49: Viết lại câu sau sang dạng dùng TÍNH TỪ phương hướng (-lich): 'Köln liegt im Westen von Deutschland.'",
            None,
            "Köln liegt westlich von Deutschland.",
            "Chuyển cụm danh từ 'im Westen von' sang tính từ 'westlich von' (không có 'im').",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 50 [Dynamic Chuyển đổi Câu]: Hãy chuyển câu trần thuật sang câu hỏi tương ứng:",
            None,
            "Wie heißen Sie? / Wie heißt du?",
            "Chuyển đổi câu chuẩn ngữ pháp tiếng Đức.",
            25,
            json.dumps({"dynamic_question_transform": True})
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
    print("✅ Đã khởi tạo thành công Bài 3: 'Städte – Länder – Sprachen' với đầy đủ 7 Học phần Lý thuyết (Không link YouTube) + 38 Từ vựng + ĐÚNG 50 Bài tập (10+10+8+6+5+4+7) có 5 Bộ Random Đổi đề!")

if __name__ == "__main__":
    seed_lesson_3()

