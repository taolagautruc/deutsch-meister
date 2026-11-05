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

def seed_lesson_6():
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
        conn.close()
        return
    a1_id = level_a1["id"]

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 6%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 20

    # Xóa dữ liệu cũ của Bài 6 nếu có để cập nhật sạch sẽ (Bảo toàn tuyệt đối Bài 1 -> Bài 5)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    lesson_title = 'Bài 6: "Dativ - Giới từ trong Dativ - Phương tiện giao thông - Số thứ tự - Ngày tháng năm (Orientierung)"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (6 HỌC PHẦN CHUẨN ĐẶC TẢ - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 6 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Dativ • Giới Từ • Phương Tiện • Số Thứ Tự & Ngày Tháng (Bài 6)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 120 phút • ⚡ 1800+ EXP • 🎯 100 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Dativ - Giới Từ Trong Dativ - Phương Tiện Giao Thông - Số Thứ Tự - Ngày Tháng Năm (Orientierung)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Hệ thống toàn diện <b>Cách 3 (Dativ)</b>; làm chủ quy tắc biến đổi mạo từ xác định, không xác định, phủ định và đại ma trận mạo từ sở hữu 9 ngôi; nằm lòng quy tắc đặc biệt <i>Plural + -n</i>; ghi nhớ nhóm giới từ luôn đi với Dativ (<i>aus, bei, mit, nach, seit, von, zu</i>) và 9 giới từ chỉ vị trí trả lời câu hỏi <i>Wo?</i>; làm chủ cấu trúc phương tiện <i>mit + Dativ</i> đối chiếu với ngoại lệ <i>zu Fuß</i>; đọc viết thành thạo <b>Số thứ tự (Ordinalzahlen)</b> từ 1 đến 31 ở cả 2 cách Nominativ và Dativ; diễn đạt chuẩn xác <b>Ngày - Tháng - Năm</b> (<i>der..., am..., vom... bis zum...</i>); và làm chủ các động từ thông dụng đi với Dativ (<i>helfen, gefallen</i>).
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: CÁCH 3 TRONG TIẾNG ĐỨC (DER DATIV) & MA TRẬN MẠO TỪ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Cách 3 Trong Tiếng Đức (Der Dativ) & Hệ Thống Ma Trận Mạo Từ</h4>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>💡</span> 3 Trường Hợp Sử Dụng Cách 3 (Dativ):</p>
                <ol class="list-decimal pl-5 space-y-1 text-slate-700">
                    <li><b>Sau các giới từ bắt buộc đi với Dativ:</b> <i>mit, nach, aus, zu, von, bei, seit, ab, gegenüber</i>.</li>
                    <li><b>Sau 9 giới từ chỉ vị trí (Wechselpräpositionen) khi trả lời cho câu hỏi <i>Wo?</i> (Ở đâu? - trạng thái tĩnh):</b> <i>in, an, auf, neben, vor, hinter, über, unter, zwischen</i>.</li>
                    <li><b>Làm tân ngữ gián tiếp (người nhận hành động / Wem?) hoặc đi sau các động từ Dativ:</b> <i>helfen, gefallen, danken, gehören</i>.</li>
                </ol>
            </div>

            <!-- Bảng 1.1: Quy tắc vàng biến đổi mạo từ Dativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>👑</span> 1.1. Ma Trận Đối Chiếu 3 Cách (Nominativ – Akkusativ – Dativ)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Giống Danh Từ</th>
                                <th class="p-3">Loại Mạo Từ</th>
                                <th class="p-3 text-center">Cách 1: Nominativ<br><span class="text-xs font-normal text-slate-500">(Chủ ngữ)</span></th>
                                <th class="p-3 text-center">Cách 4: Akkusativ<br><span class="text-xs font-normal text-slate-500">(Tân ngữ trực tiếp)</span></th>
                                <th class="p-3 text-center bg-amber-100/60 text-amber-900">Cách 3: Dativ<br><span class="text-xs font-bold text-amber-700">(Wo? / Phương tiện / Wem?)</span></th>
                                <th class="p-3">Ví Dụ Chuẩn (Dativ)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-blue-600">Maskulinum (der)</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">der<br>ein<br>kein</td>
                                <td class="p-3 text-center">de<b>n</b><br>eine<b>n</b><br>keine<b>n</b></td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-50/50">de<b>m</b><br>eine<b>m</b><br>keine<b>m</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>dem</b> Bus / auf <b>einem</b> Tisch</span>
                                        <button onclick="speakGerman('mit dem Bus auf einem Tisch')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-rose-600">Femininum (die)</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">die<br>eine<br>keine</td>
                                <td class="p-3 text-center">die<br>eine<br>keine</td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-50/50">de<b>r</b><br>eine<b>r</b><br>keine<b>r</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>der</b> U-Bahn / neben <b>einer</b> Bank</span>
                                        <button onclick="speakGerman('mit der U-Bahn neben einer Bank')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-emerald-600">Neutrum (das)</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">das<br>ein<br>kein</td>
                                <td class="p-3 text-center">das<br>ein<br>kein</td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-50/50">de<b>m</b><br>eine<b>m</b><br>keine<b>m</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>dem</b> Auto / vor <b>einem</b> Haus</span>
                                        <button onclick="speakGerman('mit dem Auto vor einem Haus')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/20">
                                <td class="p-3 font-bold text-purple-600">Plural (die + -n) ⚠️</td>
                                <td class="p-3">Xác định<br>Không xác định<br>Phủ định</td>
                                <td class="p-3 text-center">die<br>—<br>keine</td>
                                <td class="p-3 text-center">die<br>—<br>keine</td>
                                <td class="p-3 text-center font-bold text-amber-700 bg-amber-100/60">de<b>n</b> + ...<b>n</b><br>— + ...<b>n</b><br>keine<b>n</b> + ...<b>n</b></td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>mit <b>den</b> Busse<b>n</b> / mit Kinder<b>n</b></span>
                                        <button onclick="speakGerman('mit den Bussen mit Kindern')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng 1.2: Đại ma trận Mạo từ sở hữu 9 ngôi ở Dativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>👥</span> 1.2. Đại Ma Trận Mạo Từ Sở Hữu Ở Cách 3 (Dativ) Theo 9 Ngôi Nhân Xưng
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-2.5">Ngôi Nhân Xưng</th>
                                <th class="p-2.5">Gốc Sở Hữu</th>
                                <th class="p-2.5 text-blue-700">Đực (der) & Trung (das)<br><span class="text-xs font-bold text-amber-600">đuôi -em</span></th>
                                <th class="p-2.5 text-rose-700">Cái (die)<br><span class="text-xs font-bold text-amber-600">đuôi -er</span></th>
                                <th class="p-2.5 text-purple-700">Số Nhiều (Plural)<br><span class="text-xs font-bold text-amber-600">đuôi -en (+ danh từ thêm -n)</span></th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">1. ich (tôi)</td><td class="p-2.5">mein-</td><td class="p-2.5 font-semibold">mein<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">mein<b>er</b> Schwester</td><td class="p-2.5 font-semibold">mein<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">2. du (bạn)</td><td class="p-2.5">dein-</td><td class="p-2.5 font-semibold">dein<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">dein<b>er</b> Schwester</td><td class="p-2.5 font-semibold">dein<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">3. er / es (anh ấy / nó)</td><td class="p-2.5">sein-</td><td class="p-2.5 font-semibold">sein<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">sein<b>er</b> Schwester</td><td class="p-2.5 font-semibold">sein<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">4. sie (cô ấy)</td><td class="p-2.5">ihr-</td><td class="p-2.5 font-semibold">ihr<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">ihr<b>er</b> Schwester</td><td class="p-2.5 font-semibold">ihr<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">5. wir (chúng tôi)</td><td class="p-2.5">unser-</td><td class="p-2.5 font-semibold">unser<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">unser<b>er</b> Schwester</td><td class="p-2.5 font-semibold">unser<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/30"><td class="p-2.5 font-bold text-amber-800">6. ihr (các bạn) ⚠️</td><td class="p-2.5 font-bold">euer-</td><td class="p-2.5 font-semibold">eur<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">eur<b>er</b> Schwester</td><td class="p-2.5 font-semibold">eur<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">7. sie (họ)</td><td class="p-2.5">ihr-</td><td class="p-2.5 font-semibold">ihr<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">ihr<b>er</b> Schwester</td><td class="p-2.5 font-semibold">ihr<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-2.5 font-bold">8. Sie (Ngài)</td><td class="p-2.5">Ihr-</td><td class="p-2.5 font-semibold">Ihr<b>em</b> Bruder / Kind</td><td class="p-2.5 font-semibold">Ihr<b>er</b> Schwester</td><td class="p-2.5 font-semibold">Ihr<b>en</b> Eltern / Freunde<b>n</b></td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: CÁC GIỚI TỪ DATIV & 9 GIỚI TỪ VỊ TRÍ WO? -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Các Giới Từ Luôn Đi Với Dativ & 9 Giới Từ Vị Trí (Wo? + Dativ)</h4>
            </div>

            <!-- Bảng 2.1: Reine Dativ-Präpositionen -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🧲</span> 2.1. Nhóm Giới Từ LUÔN LUÔN Đi Với Dativ (mit, nach, aus, zu, von, bei, seit, ab)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Giới từ</th>
                                <th class="p-3">Dạng Viết Tắt Bắt Buộc</th>
                                <th class="p-3">Ý Nghĩa Cốt Lõi</th>
                                <th class="p-3">Câu Ví Dụ Thực Tế Chuẩn (Âm thanh de-DE & Bản dịch)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">mit</td>
                                <td class="p-3 text-slate-400">—</td>
                                <td class="p-3">Cùng với / Bằng phương tiện</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Mein Bruder fährt <b>mit dem Bus</b> zur Arbeit.“ <span class="text-xs text-slate-500">(Anh trai tôi đi làm bằng xe buýt.)</span></span>
                                        <button onclick="speakGerman('Mein Bruder fährt mit dem Bus zur Arbeit.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">nach</td>
                                <td class="p-3 text-slate-400">—</td>
                                <td class="p-3">Đi đến thành phố, nước / về nhà (<i>nach Hause</i>) / Sau thời gian</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„<b>Nach der Arbeit</b> gehe ich direkt <b>nach Hause</b>.“ <span class="text-xs text-slate-500">(Sau giờ làm việc tôi đi thẳng về nhà.)</span></span>
                                        <button onclick="speakGerman('Nach der Arbeit gehe ich direkt nach Hause.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">aus</td>
                                <td class="p-3 text-slate-400">—</td>
                                <td class="p-3">Đến từ quê hương / Ra khỏi phòng, nhà</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Um 17 Uhr kommen die Mitarbeiter <b>aus dem Büro</b>.“ <span class="text-xs text-slate-500">(Lúc 17 giờ các nhân viên bước ra khỏi văn phòng.)</span></span>
                                        <button onclick="speakGerman('Um 17 Uhr kommen die Mitarbeiter aus dem Büro.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">zu</td>
                                <td class="p-3 font-semibold text-amber-700">zu + dem = <b>zum</b><br>zu + der = <b>zur</b></td>
                                <td class="p-3">Đi tới địa điểm trong phố, tới chỗ ai / Đi bộ (<i>zu Fuß</i>) / Ở nhà (<i>zu Hause</i>)</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Wie komme ich <b>zum Bahnhof</b> und <b>zur Post</b>?“ <span class="text-xs text-slate-500">(Tôi đi đến nhà ga và bưu điện bằng cách nào?)</span></span>
                                        <button onclick="speakGerman('Wie komme ich zum Bahnhof und zur Post?')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">von</td>
                                <td class="p-3 font-semibold text-amber-700">von + dem = <b>vom</b></td>
                                <td class="p-3">Từ một địa điểm trở về / Của ai (sở hữu)</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Der Zug fährt um 9 Uhr <b>vom Hauptbahnhof</b> ab.“ <span class="text-xs text-slate-500">(Chuyến tàu khởi hành lúc 9 giờ từ nhà ga chính.)</span></span>
                                        <button onclick="speakGerman('Der Zug fährt um 9 Uhr vom Hauptbahnhof ab.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-indigo-700">bei</td>
                                <td class="p-3 font-semibold text-amber-700">bei + dem = <b>beim</b></td>
                                <td class="p-3">Ở tại chỗ ai / Làm việc tại công ty nào</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-1">
                                        <span>„Lukas wohnt noch <b>bei seinen Eltern</b>.“ <span class="text-xs text-slate-500">(Lukas vẫn sống ở nhà bố mẹ cậu ấy.)</span></span>
                                        <button onclick="speakGerman('Lukas wohnt noch bei seinen Eltern.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng 2.2: 9 Giới từ chỉ vị trí (Wo? + Dativ) -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📍</span> 2.2. 9 Giới Từ Vị Trí Trong Không Gian Khi Trả Lời Câu Hỏi Wo? (Ở đâu? + Dativ)
                </h5>
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs sm:text-sm">
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">1. in (im = in dem)</span>
                        <p class="text-slate-600">Ở trong không gian kín (phòng, nhà, túi, thành phố): <i>im Konferenzraum, im Büro</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">2. an (am = an dem)</span>
                        <p class="text-slate-600">Ở sát cạnh / tiếp xúc mặt đứng (tường, bàn, trạm xe): <i>an der Wand, am Schreibtisch</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">3. auf</span>
                        <p class="text-slate-600">Ở trên bề mặt nằm ngang có tiếp xúc: <i>auf dem Schreibtisch, auf dem Sofa</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">4. neben</span>
                        <p class="text-slate-600">Ở bên cạnh (bên trái/phải): <i>neben dem Aufzug, neben der Tastatur</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">5. vor</span>
                        <p class="text-slate-600">Ở phía trước: <i>vor dem Hotel, vor dem Eingang</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">6. hinter</span>
                        <p class="text-slate-600">Ở phía sau / đằng sau: <i>hinter dem Bahnhof, hinter dem Krankenhaus</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">7. über</span>
                        <p class="text-slate-600">Ở phía trên cao (không tiếp xúc): <i>über dem Sofa, über dem Schreibtisch</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">8. unter</span>
                        <p class="text-slate-600">Ở phía dưới / dưới gầm: <i>unter dem Schreibtisch, unter dem Stuhl</i>.</p>
                    </div>
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">9. zwischen</span>
                        <p class="text-slate-600">Ở giữa 2 vật / địa điểm: <i>zwischen der Bank und dem Kino</i>.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: PHƯƠNG TIỆN GIAO THÔNG & ĐỊNH HƯỚNG TÒA NHÀ / THÀNH PHỐ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Phương Tiện Giao Thông (Verkehrsmittel) & Định Hướng</h4>
            </div>

            <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 text-xs sm:text-sm text-emerald-900 space-y-1">
                <p class="font-bold flex items-center gap-2"><span>🚆</span> Công thức hỏi & trả lời phương tiện giao thông:</p>
                <p>• <b>Câu hỏi:</b> <i>Wie kommst du zur Arbeit?</i> hoặc <i>Womit fährst du nach Berlin?</i></p>
                <p>• <b>Quy tắc trả lời:</b> Mọi phương tiện đều dùng <b>mit + Dativ</b> (<i>mit dem Bus / mit der U-Bahn / mit dem Fahrrad / mit den Bussen</i>). <b>Ngoại lệ duy nhất:</b> Đi bộ = <b>zu Fuß gehen</b>.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 class="font-bold text-blue-700">🔵 Giống Đực (mit dem ...)</h5>
                    <ul class="space-y-1 text-slate-600">
                        <li>• der Bus → <b>mit dem Bus</b></li>
                        <li>• der Zug → <b>mit dem Zug</b></li>
                        <li>• der Wagen → <b>mit dem Wagen</b></li>
                    </ul>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 class="font-bold text-rose-700">🔴 Giống Cái (mit der ...)</h5>
                    <ul class="space-y-1 text-slate-600">
                        <li>• die U-Bahn → <b>mit der U-Bahn</b></li>
                        <li>• die S-Bahn → <b>mit der S-Bahn</b></li>
                        <li>• die Straßenbahn → <b>mit der Straßenbahn</b></li>
                        <li>• die Fähre → <b>mit der Fähre</b></li>
                    </ul>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <h5 class="font-bold text-emerald-700">🟢 Giống Trung (mit dem ...) & Ngoại Lệ</h5>
                    <ul class="space-y-1 text-slate-600">
                        <li>• das Auto → <b>mit dem Auto</b></li>
                        <li>• das Fahrrad → <b>mit dem Fahrrad</b></li>
                        <li>• das Flugzeug → <b>mit dem Flugzeug</b></li>
                        <li>• das Taxi → <b>mit dem Taxi</b></li>
                        <li class="font-bold text-amber-700 pt-1">⚠️ Đi bộ: <b>zu Fuß gehen</b></li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: SỐ THỨ TỰ (ORDINALZAHLEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Số Thứ Tự (Ordinalzahlen / Ordnungszahlen)</h4>
            </div>

            <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 text-xs sm:text-sm text-purple-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>🔢</span> Hai Công Thức Cấu Tạo Số Thứ Tự:</p>
                <ul class="space-y-1 text-slate-700">
                    <li>• <b>Từ 1 đến 19:</b> Số đếm + <b>-te</b> (sau <i>der/die/das</i> ở Nominativ) | Số đếm + <b>-ten</b> (sau <i>am, im, vom, bis zum</i> ở Dativ).<br>
                    ⚠️ <b>4 Bất quy tắc bắt buộc nhớ:</b> <b>1.</b> (<i>erst-</i>), <b>3.</b> (<i>dritt-</i>), <b>7.</b> (<i>siebt-</i>), <b>8.</b> (<i>acht-</i>).</li>
                    <li>• <b>Từ 20 trở đi (20. → 31., 100., 1000.):</b> Số đếm + <b>-ste</b> (ở Nominativ) | Số đếm + <b>-sten</b> (ở Dativ). Ví dụ: <i>der zwanzigste / am zwanzigsten</i>, <i>der einundzwanzigste / am einundzwanzigsten</i>.</li>
                </ul>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                            <th class="p-2.5 text-center">Ký hiệu</th>
                            <th class="p-2.5">Số Đếm</th>
                            <th class="p-2.5 text-blue-700">Số Thứ Tự ở Nominativ (der/die/das ...)</th>
                            <th class="p-2.5 text-amber-700 font-bold">Số Thứ Tự ở Dativ (am / im / vom / bis zum ...)</th>
                            <th class="p-2.5">Ứng Dụng Thực Tế (Tầng lầu & Ngày)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-800">
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">1. ⚠️</td><td>eins</td><td>der <b>erste</b></td><td class="font-bold text-amber-700">am / im <b>ersten</b></td><td>im ersten Stock (tầng 1) / am 1. Mai</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold">2.</td><td>zwei</td><td>der <b>zweite</b></td><td class="font-bold text-amber-700">am / im <b>zweiten</b></td><td>im zweiten Stock (tầng 2) / am 2. Juni</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">3. ⚠️</td><td>drei</td><td>der <b>dritte</b></td><td class="font-bold text-amber-700">am / im <b>dritten</b></td><td>im dritten Stock (tầng 3) / am 3. August</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">7. ⚠️</td><td>sieben</td><td>der <b>siebte</b></td><td class="font-bold text-amber-700">am / im <b>siebten</b></td><td>im siebten Stock (tầng 7) / am 7. Mai</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-rose-600">8. ⚠️</td><td>acht</td><td>der <b>achte</b></td><td class="font-bold text-amber-700">am / im <b>achten</b></td><td>im achten Stock (tầng 8) / am 8. März</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold">15.</td><td>fünfzehn</td><td>der <b>fünfzehnte</b></td><td class="font-bold text-amber-700">am / im <b>fünfzehnten</b></td><td>am 15. August (ngày 15 tháng Tám)</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-purple-600">20.</td><td>zwanzig</td><td>der <b>zwanzigste</b></td><td class="font-bold text-amber-700">am / im <b>zwanzigsten</b></td><td>am 20. September</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-purple-600">21.</td><td>einundzwanzig</td><td>der <b>einundzwanzigste</b></td><td class="font-bold text-amber-700">am / im <b>einundzwanzigsten</b></td><td>am 21. Juni</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-2 text-center font-bold text-purple-600">31.</td><td>einunddreißig</td><td>der <b>einunddreißigste</b></td><td class="font-bold text-amber-700">am / im <b>einunddreißigsten</b></td><td>am 31. Dezember</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- HỌC PHẦN 5: NGÀY - THÁNG - NĂM (DAS DATUM & DIE JAHRESZAHLEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Ngày – Tháng – Năm Trong Tiếng Đức (Das Datum & Jahreszahlen)</h4>
            </div>

            <!-- 3 Cấu trúc nói ngày tháng -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <span class="font-bold text-indigo-700">1. Hôm nay là ngày mấy? (Nominativ)</span>
                    <p class="text-slate-600"><i>Welcher Tag ist heute?</i></p>
                    <p class="font-semibold text-slate-900">→ Heute ist <b>der</b> dritt<b>e</b> Mai. (03.05.)</p>
                    <p class="text-xs text-slate-500">Sau <i>der</i> dùng đuôi <b>-te / -ste</b>.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <span class="font-bold text-indigo-700">2. Vào ngày nào? (Dativ với am)</span>
                    <p class="text-slate-600"><i>Wann hast du Geburtstag?</i></p>
                    <p class="font-semibold text-slate-900">→ Ich habe <b>am</b> acht<b>en</b> März Geburtstag.</p>
                    <p class="text-xs text-slate-500">Sau <i>am</i> dùng đuôi <b>-ten / -sten</b>.</p>
                </div>
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <span class="font-bold text-indigo-700">3. Khoảng ngày: vom... bis zum...</span>
                    <p class="text-slate-600"><i>Von wann bis wann habt ihr Urlaub?</i></p>
                    <p class="font-semibold text-slate-900">→ <b>Vom</b> erst<b>en</b> <b>bis zum</b> vierzehn<b>ten</b> Juli.</p>
                    <p class="text-xs text-slate-500">Cả 2 số thứ tự đều chia ở <b>Dativ (-ten/-sten)</b>.</p>
                </div>
            </div>

            <!-- Quy tắc đọc Năm -->
            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>📅</span> Quy Tắc Đọc Năm (Jahreszahlen) & Giới Từ Trước Năm:</p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-slate-700">
                    <div class="p-3 bg-white/80 rounded-xl border border-amber-100 space-y-1">
                        <span class="font-bold text-indigo-800">1. Các năm trước năm 2000 (Đọc theo cụm trăm):</span>
                        <p>• <b>1968:</b> <i>neunzehnhundertachtundsechzig</i> (19 trăm 68)</p>
                        <p>• <b>1998:</b> <i>neunzehnhundertachtundneunzig</i></p>
                    </div>
                    <div class="p-3 bg-white/80 rounded-xl border border-amber-100 space-y-1">
                        <span class="font-bold text-indigo-800">2. Các năm từ năm 2000 trở đi (Đọc như số đếm):</span>
                        <p>• <b>2002:</b> <i>zweitausendzwei</i></p>
                        <p>• <b>2026:</b> <i>zweitausendsechsundzwanzig</i></p>
                    </div>
                </div>
                <p class="text-xs text-slate-600 pt-1">
                    ⚠️ <b>Tuyệt đối KHÔNG dùng giới từ "in" trước năm trong tiếng Đức!</b><br>
                    • Đúng: <i>Ich bin 1998 in Hai Phong geboren.</i> (hoặc <i>im Jahr 1998</i>).<br>
                    • Sai hoàn toàn: <strike class="text-rose-600">Ich bin in 1998 geboren.</strike>
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 6: HỘI THOẠI THỰC CHIẾN ĐA NGỮ CẢNH KÈM AUDIO -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center font-bold text-sm">6</span>
                <h4 class="text-lg font-bold text-slate-900">Hội Thoại Thực Chiến Đa Ngữ Cảnh (Praxis-Dialoge de-DE)</h4>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <!-- Hội thoại 1: Im Bürogebäude -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <h5 class="font-bold text-slate-800 flex items-center gap-2"><span>🏢</span> Hội Thoại 1: Trong Tòa Nhà Công Ty</h5>
                        <button onclick="speakGerman('Entschuldigung, wo ist das Büro von Frau Schneider? Das Büro liegt im dritten Stock neben dem Aufzug. Die Kantine befindet sich im Erdgeschoss.')" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-bold cursor-pointer">🔊 Nghe Hội Thoại</button>
                    </div>
                    <div class="space-y-2.5 text-xs sm:text-sm text-slate-700">
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Khách:</b> „Entschuldigung, wo ist das Büro von Frau Schneider?“<br><span class="text-xs text-slate-500">(Xin lỗi, văn phòng của bà Schneider ở đâu ạ?)</span></p>
                            <button onclick="speakGerman('Entschuldigung, wo ist das Büro von Frau Schneider?')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Lễ tân:</b> „Das Büro liegt <b>im dritten Stock</b> <b>neben dem Aufzug</b>. Die Kantine befindet sich <b>im Erdgeschoss</b>.“<br><span class="text-xs text-slate-500">(Văn phòng nằm ở tầng ba bên cạnh thang máy. Nhà ăn thì ở tầng trệt.)</span></p>
                            <button onclick="speakGerman('Das Büro liegt im dritten Stock neben dem Aufzug. Die Kantine befindet sich im Erdgeschoss.')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                    </div>
                </div>

                <!-- Hội thoại 2: In der Stadt & Verkehrsmittel -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <h5 class="font-bold text-slate-800 flex items-center gap-2"><span>🚆</span> Hội Thoại 2: Hỏi Đường & Phương Tiện</h5>
                        <button onclick="speakGerman('Entschuldigung, wie komme ich zum Bahnhof? Fahren Sie mit der Straßenbahn Linie 3 bis zum Markt. Dort steigen Sie in den Bus um.')" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs font-bold cursor-pointer">🔊 Nghe Hội Thoại</button>
                    </div>
                    <div class="space-y-2.5 text-xs sm:text-sm text-slate-700">
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Người đi đường:</b> „Entschuldigung, wie komme ich <b>zum Bahnhof</b>?“<br><span class="text-xs text-slate-500">(Xin lỗi, tôi đi đến nhà ga bằng cách nào ạ?)</span></p>
                            <button onclick="speakGerman('Entschuldigung, wie komme ich zum Bahnhof?')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                        <div class="flex items-start justify-between gap-2 p-2 rounded-xl bg-white border border-slate-200/60 shadow-xs">
                            <p><b>Cư dân:</b> „Fahren Sie <b>mit der Straßenbahn</b> Linie 3 <b>bis zum Markt</b>. Dort steigen Sie in den Bus um.“<br><span class="text-xs text-slate-500">(Bạn hãy đi bằng tàu điện mặt đất tuyến số 3 đến chợ. Tại đó bạn đổi sang xe buýt.)</span></p>
                            <button onclick="speakGerman('Fahren Sie mit der Straßenbahn Linie 3 bis zum Markt. Dort steigen Sie in den Bus um.')" title="Nghe câu này" class="shrink-0 p-1.5 rounded-lg bg-slate-100 hover:bg-indigo-100 text-indigo-600 cursor-pointer text-xs">🔊</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""

    if existing_lesson:
        cursor.execute("""
            UPDATE lessons SET title = ?, grammar_content = ? WHERE id = ?;
        """, (lesson_title, grammar_html, lesson_id))
    else:
        cursor.execute("""
            INSERT INTO lessons (id, level_id, title, grammar_content)
            VALUES (?, ?, ?, ?);
        """, (lesson_id, a1_id, lesson_title, grammar_html))

    # =========================================================================
    # DANH MỤC 45 TỪ VỰNG TRỌNG TÂM BÀI 6 (KHỚP 100% VỚI LEXIKON_DB.JS)
    # =========================================================================
    vocab_raw = [
        {
                "word": "Flur",
                "article": "der",
                "gender": "der",
                "plural": "die Flure",
                "indefinite": "ein Flur",
                "negation": "kein Flur",
                "akkusativ": "den / einen / keinen Flur",
                "meaning": "hành lang",
                "category": "Nhà ở & Phòng ốc • Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Số nhiều thêm -e. Đại từ nhân xưng thay thế ở Nominativ là 'Er' (Er ist lang und dunkel).",
                "example": "Das Haus hat einen Flur. Er ist lang und dunkel.",
                "example_vi": "Ngôi nhà có một hành lang. Nó dài và tối."
        },
        {
                "word": "Stock",
                "article": "der",
                "gender": "der",
                "plural": "die Stöcke",
                "indefinite": "ein Stock",
                "negation": "kein Stock",
                "akkusativ": "den / einen / keinen Stock",
                "meaning": "tầng lầu",
                "category": "Nhà ở & Phòng ốc • Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Số nhiều biến âm o -> ö và thêm -e (die Stöcke). Thường đi với số thứ tự: im 1. Stock.",
                "example": "Meine Wohnung liegt im zweiten Stock.",
                "example_vi": "Căn hộ của tôi nằm ở tầng hai."
        },
        {
                "word": "Bus",
                "article": "der",
                "gender": "der",
                "plural": "die Busse",
                "indefinite": "ein Bus",
                "negation": "kein Bus",
                "meaning": "xe buýt",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Bus), số nhiều die Busse. Đi bằng xe buýt dùng mit dem Bus.",
                "example": "Mein Bruder fährt jeden Tag mit dem Bus zur Arbeit.",
                "example_vi": "Anh trai tôi đi làm mỗi ngày bằng xe buýt."
        },
        {
                "word": "Zug",
                "article": "der",
                "gender": "der",
                "plural": "die Züge",
                "indefinite": "ein Zug",
                "negation": "kein Zug",
                "meaning": "tàu hỏa",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Zug), số nhiều biến âm u -> ü (die Züge). Đi bằng tàu hỏa dùng mit dem Zug.",
                "example": "Der Zug fährt um acht Uhr am Bahnhof ab.",
                "example_vi": "Chuyến tàu khởi hành lúc 8 giờ tại nhà ga."
        },
        {
                "word": "Wagen",
                "article": "der",
                "gender": "der",
                "plural": "die Wagen",
                "indefinite": "ein Wagen",
                "negation": "kein Wagen",
                "meaning": "xe hơi, ô tô cá nhân",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Wagen). Đi bằng xe hơi dùng mit seinem Wagen.",
                "example": "Herr Müller fährt mit seinem Wagen ins Büro.",
                "example_vi": "Ông Müller lái chiếc xe hơi của ông ấy đến văn phòng."
        },
        {
                "word": "U-Bahn",
                "article": "die",
                "gender": "die",
                "plural": "die U-Bahnen",
                "indefinite": "eine U-Bahn",
                "negation": "keine U-Bahn",
                "meaning": "tàu điện ngầm",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die U-Bahn). Đi bằng tàu điện ngầm dùng mit der U-Bahn.",
                "example": "In Berlin fahren wir immer mit der U-Bahn.",
                "example_vi": "Ở Berlin chúng tôi luôn đi bằng tàu điện ngầm."
        },
        {
                "word": "S-Bahn",
                "article": "die",
                "gender": "die",
                "plural": "die S-Bahnen",
                "indefinite": "eine S-Bahn",
                "negation": "keine S-Bahn",
                "meaning": "tàu điện nhanh đô thị",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die S-Bahn). Đi bằng tàu điện đô thị dùng mit der S-Bahn.",
                "example": "Vom Flughafen fährt der Tourist mit der S-Bahn ins Stadtzentrum.",
                "example_vi": "Từ sân bay vị khách du lịch đi bằng tàu điện đô thị vào trung tâm thành phố."
        },
        {
                "word": "Straßenbahn",
                "article": "die",
                "gender": "die",
                "plural": "die Straßenbahnen",
                "indefinite": "eine Straßenbahn",
                "negation": "keine Straßenbahn",
                "meaning": "tàu điện mặt đất",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Straßenbahn). Đi bằng tàu điện mặt đất dùng mit der Straßenbahn.",
                "example": "Am Wochenende fahren unsere Großeltern mit der Straßenbahn zum Markt.",
                "example_vi": "Vào cuối tuần ông bà của chúng tôi đi bằng tàu điện mặt đất ra chợ."
        },
        {
                "word": "Fähre",
                "article": "die",
                "gender": "die",
                "plural": "die Fähren",
                "indefinite": "eine Fähre",
                "negation": "keine Fähre",
                "meaning": "phà",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Fähre). Đi bằng phà dùng mit der Fähre.",
                "example": "Wir fahren mit der Fähre auf die Insel.",
                "example_vi": "Chúng tôi đi bằng phà ra đảo."
        },
        {
                "word": "Auto",
                "article": "das",
                "gender": "das",
                "plural": "die Autos",
                "indefinite": "ein Auto",
                "negation": "kein Auto",
                "meaning": "ô tô, xe hơi",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Auto). Đi bằng ô tô dùng mit dem Auto.",
                "example": "Am Sonntag fahren unsere Nachbarn mit dem Auto ans Meer.",
                "example_vi": "Vào Chủ nhật những người hàng xóm của chúng tôi đi bằng ô tô ra biển."
        },
        {
                "word": "Fahrrad",
                "article": "das",
                "gender": "das",
                "plural": "die Fahrräder",
                "indefinite": "ein Fahrrad",
                "negation": "kein Fahrrad",
                "meaning": "xe đạp",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Fahrrad), số nhiều die Fahrräder. Đi bằng xe đạp dùng mit dem Fahrrad.",
                "example": "Bei schönem Wetter fährt sie mit dem Fahrrad zur Schule.",
                "example_vi": "Khi thời tiết đẹp cô ấy đi xe đạp tới trường."
        },
        {
                "word": "Motorrad",
                "article": "das",
                "gender": "das",
                "plural": "die Motorräder",
                "indefinite": "ein Motorrad",
                "negation": "kein Motorrad",
                "meaning": "xe mô tô",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Motorrad). Đi bằng xe máy/mô tô dùng mit dem Motorrad.",
                "example": "In Vietnam fahren viele Menschen mit dem Motorrad zur Arbeit.",
                "example_vi": "Ở Việt Nam nhiều người đi làm bằng xe mô tô."
        },
        {
                "word": "Taxi",
                "article": "das",
                "gender": "das",
                "plural": "die Taxis",
                "indefinite": "ein Taxi",
                "negation": "kein Taxi",
                "meaning": "xe taxi",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Taxi). Đi bằng taxi dùng mit dem Taxi.",
                "example": "Wir fahren mit dem Taxi nach Hause.",
                "example_vi": "Chúng tôi đi bằng taxi về nhà."
        },
        {
                "word": "Flugzeug",
                "article": "das",
                "gender": "das",
                "plural": "die Flugzeuge",
                "indefinite": "ein Flugzeug",
                "negation": "kein Flugzeug",
                "meaning": "máy bay",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Flugzeug). Bay bằng máy bay dùng mit dem Flugzeug fliegen.",
                "example": "Im August fliegen wir mit dem Flugzeug nach Deutschland.",
                "example_vi": "Vào tháng Tám chúng tôi bay bằng máy bay sang Đức."
        },
        {
                "word": "Schiff",
                "article": "das",
                "gender": "das",
                "plural": "die Schiffe",
                "indefinite": "ein Schiff",
                "negation": "kein Schiff",
                "meaning": "tàu thủy lớn",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Schiff). Đi bằng tàu thủy dùng mit dem Schiff fahren.",
                "example": "Die Touristen machen eine Reise mit dem Schiff.",
                "example_vi": "Những du khách thực hiện một chuyến du hành bằng tàu thủy."
        },
        {
                "word": "Fuß",
                "article": "der",
                "gender": "der",
                "plural": "die Füße",
                "indefinite": "ein Fuß",
                "negation": "kein Fuß",
                "meaning": "bàn chân (đi bộ)",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Ngoại lệ đi bộ trong tiếng Đức dùng cụm cố định zu Fuß gehen.",
                "example": "Die Schule ist gleich neben meinem Haus, deshalb gehe ich immer zu Fuß.",
                "example_vi": "Ngôi trường ở ngay cạnh nhà tôi, vì vậy tôi luôn đi bộ."
        },
        {
                "word": "Bahnhof",
                "article": "der",
                "gender": "der",
                "plural": "die Bahnhöfe",
                "indefinite": "ein Bahnhof",
                "negation": "kein Bahnhof",
                "meaning": "nhà ga xe lửa",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Bahnhof). Đến nhà ga dùng zum Bahnhof, tại nhà ga dùng am Bahnhof.",
                "example": "Wie komme ich vom Hauptbahnhof zum Stadtmuseum?",
                "example_vi": "Tôi đi từ nhà ga trung tâm đến bảo tàng thành phố bằng cách nào?"
        },
        {
                "word": "Flughafen",
                "article": "der",
                "gender": "der",
                "plural": "die Flughäfen",
                "indefinite": "ein Flughafen",
                "negation": "kein Flughafen",
                "meaning": "sân bay",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Flughafen). Đến sân bay dùng zum Flughafen, từ sân bay về dùng vom Flughafen.",
                "example": "Wann kommt deine Schwester heute Abend vom Flughafen zurück?",
                "example_vi": "Tối nay khi nào chị gái của bạn từ sân bay trở về?"
        },
        {
                "word": "Haltestelle",
                "article": "die",
                "gender": "die",
                "plural": "die Haltestellen",
                "indefinite": "eine Haltestelle",
                "negation": "keine Haltestelle",
                "meaning": "trạm dừng (xe buýt/tàu)",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Haltestelle). Tại trạm dừng dùng an der Haltestelle.",
                "example": "Wann kommt der Bus an der Haltestelle an?",
                "example_vi": "Khi nào xe buýt đến trạm dừng?"
        },
        {
                "word": "Parkplatz",
                "article": "der",
                "gender": "der",
                "plural": "die Parkplätze",
                "indefinite": "ein Parkplatz",
                "negation": "kein Parkplatz",
                "meaning": "bãi đỗ xe",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Parkplatz). Phía sau bệnh viện dùng hinter dem Krankenhaus.",
                "example": "Der große Parkplatz liegt direkt hinter dem Krankenhaus.",
                "example_vi": "Bãi đỗ xe lớn nằm ngay phía sau bệnh viện."
        },
        {
                "word": "Markt",
                "article": "der",
                "gender": "der",
                "plural": "die Märkte",
                "indefinite": "ein Markt",
                "negation": "kein Markt",
                "meaning": "khu chợ",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Markt). Ra chợ dùng zum Markt hoặc auf dem Markt.",
                "example": "Meine Großeltern fahren gern mit der Straßenbahn zum Markt.",
                "example_vi": "Ông bà tôi thích đi bằng tàu điện mặt đất ra chợ."
        },
        {
                "word": "Park",
                "article": "der",
                "gender": "der",
                "plural": "die Parks",
                "indefinite": "ein Park",
                "negation": "kein Park",
                "meaning": "công viên",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống đực (der Park). Ở trong công viên dùng im Park.",
                "example": "Am Sonntag spielen die Kinder im Park mit ihren Freunden.",
                "example_vi": "Vào Chủ nhật bọn trẻ chơi ở trong công viên với những người bạn của chúng."
        },
        {
                "word": "Bank",
                "article": "die",
                "gender": "die",
                "plural": "die Banken",
                "indefinite": "eine Bank",
                "negation": "keine Bank",
                "meaning": "ngân hàng",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Bank). Đến ngân hàng dùng zur Bank, làm việc ở ngân hàng dùng bei einer Bank.",
                "example": "Frau Bui arbeitet bei einer Bank in Berlin.",
                "example_vi": "Bà Bùi làm việc tại một ngân hàng ở Berlin."
        },
        {
                "word": "Post",
                "article": "die",
                "gender": "die",
                "plural": "die Post",
                "indefinite": "eine Post",
                "negation": "keine Post",
                "meaning": "bưu điện",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Post). Đến bưu điện dùng zur Post, bên cạnh bưu điện dùng neben der Post.",
                "example": "Wie komme ich zum Bahnhof und zur Post?",
                "example_vi": "Tôi đi đến nhà ga và bưu điện bằng cách nào?"
        },
        {
                "word": "Bibliothek",
                "article": "die",
                "gender": "die",
                "plural": "die Bibliotheken",
                "indefinite": "eine Bibliothek",
                "negation": "keine Bibliothek",
                "meaning": "thư viện",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Bibliothek). Đi bộ đến thư viện dùng zu Fuß zur Bibliothek.",
                "example": "Morgen gehen wir zu Fuß zur Bibliothek.",
                "example_vi": "Ngày mai chúng tôi đi bộ đến thư viện."
        },
        {
                "word": "Buchhandlung",
                "article": "die",
                "gender": "die",
                "plural": "die Buchhandlungen",
                "indefinite": "eine Buchhandlung",
                "negation": "keine Buchhandlung",
                "meaning": "hiệu sách",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Buchhandlung). Giữa hiệu sách và rạp phim dùng zwischen der Buchhandlung und dem Kino.",
                "example": "Das Café liegt direkt zwischen der Buchhandlung und dem Kino.",
                "example_vi": "Quán cà phê nằm ngay giữa hiệu sách và rạp chiếu phim."
        },
        {
                "word": "Apotheke",
                "article": "die",
                "gender": "die",
                "plural": "die Apotheken",
                "indefinite": "eine Apotheke",
                "negation": "keine Apotheke",
                "meaning": "hiệu thuốc tây",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Apotheke). Đối diện nhà ga dùng gegenüber vom Bahnhof.",
                "example": "Die Apotheke liegt direkt gegenüber vom Bahnhof.",
                "example_vi": "Hiệu thuốc nằm ngay đối diện nhà ga."
        },
        {
                "word": "Kirche",
                "article": "die",
                "gender": "die",
                "plural": "die Kirchen",
                "indefinite": "eine Kirche",
                "negation": "keine Kirche",
                "meaning": "nhà thờ",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống cái (die Kirche). Bên cạnh nhà thờ cổ dùng neben einer alten Kirche.",
                "example": "Das Museum liegt direkt vor dem Park und neben einer alten Kirche.",
                "example_vi": "Bảo tàng nằm ngay phía trước công viên và bên cạnh một nhà thờ cổ."
        },
        {
                "word": "Krankenhaus",
                "article": "das",
                "gender": "das",
                "plural": "die Krankenhäuser",
                "indefinite": "ein Krankenhaus",
                "negation": "kein Krankenhaus",
                "meaning": "bệnh viện",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Krankenhaus). Phía sau bệnh viện dùng hinter dem Krankenhaus.",
                "example": "Der Parkplatz liegt direkt hinter dem Krankenhaus.",
                "example_vi": "Bãi đỗ xe nằm ngay phía sau bệnh viện."
        },
        {
                "word": "Hotel",
                "article": "das",
                "gender": "das",
                "plural": "die Hotels",
                "indefinite": "ein Hotel",
                "negation": "kein Hotel",
                "meaning": "khách sạn",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Hotel). Phía trước khách sạn dùng vor dem Hotel.",
                "example": "Das Taxi wartet vor dem Hotel auf die Gäste.",
                "example_vi": "Chiếc taxi đang đợi khách phía trước khách sạn."
        },
        {
                "word": "Café",
                "article": "das",
                "gender": "das",
                "plural": "die Cafés",
                "indefinite": "ein Café",
                "negation": "kein Café",
                "meaning": "quán cà phê",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Café). Trong quán cà phê dùng im Café.",
                "example": "Die Studenten sitzen im Café vor der Universität.",
                "example_vi": "Các sinh viên đang ngồi trong quán cà phê phía trước trường đại học."
        },
        {
                "word": "Kino",
                "article": "das",
                "gender": "das",
                "plural": "die Kinos",
                "indefinite": "ein Kino",
                "negation": "kein Kino",
                "meaning": "rạp chiếu phim",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Kino). Giữa hiệu sách và rạp phim dùng zwischen der Buchhandlung und dem Kino.",
                "example": "Am Samstag gehen wir mit unseren Freunden ins Kino.",
                "example_vi": "Vào thứ Bảy chúng tôi đi xem phim cùng với những người bạn của chúng tôi."
        },
        {
                "word": "Museum",
                "article": "das",
                "gender": "das",
                "plural": "die Museen",
                "indefinite": "ein Museum",
                "negation": "kein Museum",
                "meaning": "bảo tàng",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Museum). Đến bảo tàng thành phố dùng zum Stadtmuseum.",
                "example": "Wie komme ich vom Hauptbahnhof zum Stadtmuseum?",
                "example_vi": "Tôi đi từ nhà ga trung tâm đến bảo tàng thành phố bằng cách nào?"
        },
        {
                "word": "Stadtzentrum",
                "article": "das",
                "gender": "das",
                "plural": "die Stadtzentren",
                "indefinite": "ein Stadtzentrum",
                "negation": "kein Stadtzentrum",
                "meaning": "trung tâm thành phố",
                "category": "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
                "rule": "Danh từ giống trung (das Stadtzentrum). Vào trung tâm thành phố dùng ins Stadtzentrum.",
                "example": "Vom Flughafen fährt der Tourist mit der S-Bahn ins Stadtzentrum.",
                "example_vi": "Từ sân bay vị khách du lịch đi bằng tàu điện đô thị vào trung tâm thành phố."
        },
        {
                "word": "Aufzug",
                "article": "der",
                "gender": "der",
                "plural": "die Aufzüge",
                "indefinite": "ein Aufzug",
                "negation": "kein Aufzug",
                "meaning": "thang máy",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống đực (der Aufzug). Bên cạnh thang máy dùng neben dem Aufzug.",
                "example": "Unser Büro liegt im zweiten Stock neben dem Aufzug.",
                "example_vi": "Văn phòng của chúng tôi nằm ở tầng hai bên cạnh thang máy."
        },
        {
                "word": "Eingang",
                "article": "der",
                "gender": "der",
                "plural": "die Eingänge",
                "indefinite": "ein Eingang",
                "negation": "kein Eingang",
                "meaning": "lối vào, cổng vào",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống đực (der Eingang). Bên cạnh lối vào dùng neben dem Eingang.",
                "example": "Die Rezeption befindet sich im Erdgeschoss neben dem Eingang.",
                "example_vi": "Quầy lễ tân nằm ở tầng trệt bên cạnh lối vào."
        },
        {
                "word": "Schreibtisch",
                "article": "der",
                "gender": "der",
                "plural": "die Schreibtische",
                "indefinite": "ein Schreibtisch",
                "negation": "kein Schreibtisch",
                "meaning": "bàn làm việc",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống đực (der Schreibtisch). Trên bàn làm việc dùng auf dem Schreibtisch.",
                "example": "Der Drucker steht auf dem Schreibtisch neben dem Computer.",
                "example_vi": "Chiếc máy in nằm trên bàn làm việc bên cạnh máy tính."
        },
        {
                "word": "Drucker",
                "article": "der",
                "gender": "der",
                "plural": "die Drucker",
                "indefinite": "ein Drucker",
                "negation": "kein Drucker",
                "meaning": "máy in",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống đực (der Drucker). Đặt trên mặt bàn làm việc dùng auf dem Schreibtisch.",
                "example": "Der schwere Drucker steht auf dem Schreibtisch.",
                "example_vi": "Chiếc máy in nặng đặt ở trên mặt bàn làm việc."
        },
        {
                "word": "Kalender",
                "article": "der",
                "gender": "der",
                "plural": "die Kalender",
                "indefinite": "ein Kalender",
                "negation": "kein Kalender",
                "meaning": "cuốn lịch",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống đực (der Kalender). Treo trên tường dùng an der Wand.",
                "example": "Der Kalender hängt an der Wand über dem Schreibtisch.",
                "example_vi": "Cuốn lịch treo trên tường phía trên bàn làm việc."
        },
        {
                "word": "Konferenzraum",
                "article": "der",
                "gender": "der",
                "plural": "die Konferenzräume",
                "indefinite": "ein Konferenzraum",
                "negation": "kein Konferenzraum",
                "meaning": "phòng họp, phòng hội nghị",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống đực (der Konferenzraum). Ở trong phòng họp dùng im Konferenzraum.",
                "example": "Die Mitarbeiter sitzen im Konferenzraum.",
                "example_vi": "Các nhân viên đang ngồi ở trong phòng họp."
        },
        {
                "word": "Treppe",
                "article": "die",
                "gender": "die",
                "plural": "die Treppen",
                "indefinite": "eine Treppe",
                "negation": "keine Treppe",
                "meaning": "cầu thang bộ",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống cái (die Treppe). Đi bằng cầu thang bộ dùng über die Treppe.",
                "example": "Sie müssen über die Treppe in den dritten Stock gehen.",
                "example_vi": "Ngài phải đi bằng cầu thang bộ lên tầng ba."
        },
        {
                "word": "Rezeption",
                "article": "die",
                "gender": "die",
                "plural": "die Rezeptionen",
                "indefinite": "eine Rezeption",
                "negation": "keine Rezeption",
                "meaning": "quầy lễ tân, quầy tiếp tân",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống cái (die Rezeption). Ở quầy lễ tân dùng an der Rezeption.",
                "example": "Die Rezeption befindet sich im Erdgeschoss neben dem Eingang.",
                "example_vi": "Quầy lễ tân nằm ở tầng trệt bên cạnh lối vào."
        },
        {
                "word": "Kantine",
                "article": "die",
                "gender": "die",
                "plural": "die Kantinen",
                "indefinite": "eine Kantine",
                "negation": "keine Kantine",
                "meaning": "nhà ăn, căng tin cơ quan",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống cái (die Kantine). Trong nhà ăn ở tầng trệt dùng in der Kantine im Erdgeschoss.",
                "example": "Die Kantine befindet sich im Erdgeschoss.",
                "example_vi": "Nhà ăn nằm ở tầng trệt."
        },
        {
                "word": "Erdgeschoss",
                "article": "das",
                "gender": "das",
                "plural": "die Erdgeschosse",
                "indefinite": "ein Erdgeschoss",
                "negation": "kein Erdgeschoss",
                "meaning": "tầng trệt",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống trung (das Erdgeschoss). Ở tầng trệt luôn dùng im Erdgeschoss.",
                "example": "Die Kantine befindet sich im Erdgeschoss und der Konferenzraum ist im siebten Stock.",
                "example_vi": "Nhà ăn nằm ở tầng trệt và phòng họp ở tầng bảy."
        },
        {
                "word": "Büro",
                "article": "das",
                "gender": "das",
                "plural": "die Büros",
                "indefinite": "ein Büro",
                "negation": "kein Büro",
                "meaning": "văn phòng làm việc",
                "category": "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
                "rule": "Danh từ giống trung (das Büro). Ở văn phòng dùng im Büro.",
                "example": "Das Büro von Frau Schneider liegt im dritten Stock neben dem Aufzug.",
                "example_vi": "Văn phòng của bà Schneider nằm ở tầng ba bên cạnh thang máy."
        }
]

    vocabularies = []
    for item in vocab_raw:
        meaning = f"{item['meaning']} (Pl: {item['plural']})" if item.get("plural") else item["meaning"]
        vocabularies.append((
            lesson_id,
            item["word"],
            item["article"],
            meaning,
            f"{item['example']} ({item['example_vi']})"
        ))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # KHO 100 BÀI TẬP BÀI 6 CHUẨN ĐẶC TẢ ZERO-BUG (18+15+12+12+10+10+9+7+7)
    # =========================================================================
    exercises_raw = [
        {
                "q_num": 1,
                "type": "trac_nghiem",
                "question": "Câu 1: Chọn cụm từ đúng để hoàn thành câu: „Meine Mutter fährt jeden Morgen ___ zur Arbeit.“",
                "options_json": "[\"mit die Straßenbahn\", \"mit der Straßenbahn\", \"mit dem Straßenbahn\", \"mit den Straßenbahn\"]",
                "correct_answer": "mit der Straßenbahn",
                "explanation": "Giới từ mit luôn đi với Cách 3 (Dativ). Danh từ die Straßenbahn mang giống cái (Femininum), nên ở Dativ mạo từ die biến đổi thành der → mit der Straßenbahn.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Mẹ tôi đi làm mỗi buổi sáng bằng tàu điện mặt đất."
                }
        },
        {
                "q_num": 2,
                "type": "trac_nghiem",
                "question": "Câu 2: Chọn phương án đúng điền vào 2 chỗ trống: „Womit ___ dein Bruder zur Universität? — Er ___ ___ Fahrrad.“",
                "options_json": "[\"fährt / fährt mit dem\", \"fahrst / fährt mit das\", \"fährt / fahrt mit einem\", \"fahren / fährt zu dem\"]",
                "correct_answer": "fährt / fährt mit dem",
                "explanation": "Chủ ngữ dein Bruder (= ngôi er) nên động từ fahren biến âm a -> ä thành fährt. Danh từ das Fahrrad mang giống trung nên sau mit (Dativ) biến đổi thành mit dem Fahrrad.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Anh trai của bạn đi đến trường đại học bằng phương tiện gì? — Anh ấy đi bằng xe đạp."
                }
        },
        {
                "q_num": 3,
                "type": "trac_nghiem",
                "question": "Câu 3: Chọn cách diễn đạt đúng nhất: „Die Schule liegt direkt neben unserem Haus. Deshalb gehen die Kinder immer ___.“",
                "options_json": "[\"mit dem Fuß\", \"mit den Füßen\", \"zu Fuß\", \"auf dem Fuß\"]",
                "correct_answer": "zu Fuß",
                "explanation": "Khác với các phương tiện dùng mit + Dativ, cụm từ cố định chỉ việc \"đi bộ\" trong tiếng Đức là zu Fuß gehen.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Ngôi trường nằm ngay bên cạnh nhà chúng tôi. Vì vậy bọn trẻ luôn đi bộ."
                }
        },
        {
                "q_num": 4,
                "type": "trac_nghiem",
                "question": "Câu 4: Chọn đáp án đúng ngữ pháp Cách 3 (Dativ): „Am Wochenende macht Herr Wagner einen Ausflug mit ___.“",
                "options_json": "[\"seine Kinder\", \"seinen Kinder\", \"seinen Kindern\", \"seinem Kindern\"]",
                "correct_answer": "seinen Kindern",
                "explanation": "Sau giới từ mit là Cách 3 (Dativ). Ở dạng số nhiều (Plural), mạo từ sở hữu seine đổi thành seinen và danh từ số nhiều Kinder bắt buộc phải cộng thêm đuôi -n thành seinen Kindern.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Vào cuối tuần ông Wagner đi dã ngoại cùng với các con của ông ấy."
                }
        },
        {
                "q_num": 5,
                "type": "trac_nghiem",
                "question": "Câu 5: Chọn dạng mạo từ sở hữu đúng: „Kinder, wohnt ihr noch bei ___ Eltern oder habt ihr schon eine eigene Wohnung?“",
                "options_json": "[\"eure\", \"eurem\", \"eurer\", \"euren\"]",
                "correct_answer": "euren",
                "explanation": "Chủ ngữ đang được hỏi là ihr (các bạn/các con) → gốc sở hữu là euer. Đi sau giới từ bei (+ Dativ) và trước danh từ số nhiều Eltern, euer thêm đuôi -en và lược chữ e ở giữa thành euren Eltern.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Các con ơi, các con vẫn còn sống ở nhà bố mẹ của các con hay là đã có một căn hộ riêng rồi?"
                }
        },
        {
                "q_num": 6,
                "type": "trac_nghiem",
                "question": "Câu 6: Chọn đáp án đúng: „Das Geschenk auf dem Tisch ist von ___ Lehrerin.“",
                "options_json": "[\"unsere\", \"unserer\", \"unserem\", \"unseren\"]",
                "correct_answer": "unserer",
                "explanation": "Sau giới từ von là Cách 3 (Dativ). Danh từ die Lehrerin mang giống cái (Femininum), nên gốc sở hữu unser (của chúng tôi) nhận đuôi -er thành unserer Lehrerin.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Món quà ở trên bàn là của cô giáo chúng tôi."
                }
        },
        {
                "q_num": 7,
                "type": "trac_nghiem",
                "question": "Câu 7: Chọn giới từ đúng: „Nach dem Frühstück fährt Frau Weber zuerst ___ Bahnhof und dann mit dem ICE ___ Frankfurt.“",
                "options_json": "[\"nach / zu\", \"zum / nach\", \"zur / in\", \"im / nach\"]",
                "correct_answer": "zum / nach",
                "explanation": "Đi tới một địa điểm cụ thể trong thành phố (der Bahnhof) dùng zu + dem = zum Bahnhof. Đi tới một thành phố không có mạo từ (Frankfurt) dùng giới từ nach (nach Frankfurt).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Sau bữa sáng bà Weber trước tiên đi đến nhà ga rồi sau đó đi bằng tàu cao tốc ICE tới Frankfurt."
                }
        },
        {
                "q_num": 8,
                "type": "trac_nghiem",
                "question": "Câu 8: Chọn cặp từ đúng điền vào câu: „Am Sonntag bleibe ich den ganzen Tag ___, aber am Montag gehe ich um 18 Uhr von der Arbeit ___.“",
                "options_json": "[\"nach Hause / zu Hause\", \"zu Hause / nach Hause\", \"im Haus / zum Haus\", \"bei Hause / nach Hause\"]",
                "correct_answer": "zu Hause / nach Hause",
                "explanation": "zu Hause chỉ trạng thái tĩnh (đang ở nhà - Wo?), còn nach Hause chỉ sự di chuyển (đi về nhà - Wohin?).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Vào Chủ nhật tôi ở nhà cả ngày, nhưng vào thứ Hai tôi đi từ chỗ làm về nhà lúc 18 giờ."
                }
        },
        {
                "q_num": 9,
                "type": "trac_nghiem",
                "question": "Câu 9: Chọn phương án đúng: „Wo liegt die neue Buchhandlung? — Sie liegt direkt zwischen ___ Supermarkt und ___ Post.“",
                "options_json": "[\"den / die\", \"dem / der\", \"der / dem\", \"einem / eine\"]",
                "correct_answer": "dem / der",
                "explanation": "Câu hỏi Wo? với giới từ zwischen đòi hỏi cả 2 danh từ phía sau đều phải chia ở Cách 3 (Dativ): der Supermarkt (giống đực) → dem Supermarkt; die Post (giống cái) → der Post.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hiệu sách mới nằm ở đâu? — Nó nằm ngay giữa siêu thị và bưu điện."
                }
        },
        {
                "q_num": 10,
                "type": "trac_nghiem",
                "question": "Câu 10: Chọn giới từ vị trí đúng: „Der schwere Drucker steht ___ dem Schreibtisch, und das schöne Familienfoto hängt ___ der Wand.“",
                "options_json": "[\"über / auf\", \"auf / an\", \"an / in\", \"unter / neben\"]",
                "correct_answer": "auf / an",
                "explanation": "Đặt tiếp xúc trên bề mặt nằm ngang (der Schreibtisch) dùng auf dem Schreibtisch; treo tiếp xúc trên bề mặt thẳng đứng (die Wand - giống cái) dùng an der Wand.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Chiếc máy in nặng đặt ở trên mặt bàn làm việc, và bức ảnh gia đình đẹp đẽ treo ở trên tường."
                }
        },
        {
                "q_num": 11,
                "type": "trac_nghiem",
                "question": "Câu 11: Chọn câu trả lời đúng ngữ pháp: „Wo befindet sich die Kantine in Ihrer Firma? — Sie liegt ___ Erdgeschoss, und mein Büro ist ___ dritten Stock.“",
                "options_json": "[\"im / im\", \"am / am\", \"in der / im\", \"auf dem / in der\"]",
                "correct_answer": "im / im",
                "explanation": "Cả das Erdgeschoss (giống trung) và der Stock (giống đực) khi chỉ vị trí Wo? đều dùng in + dem = im: im Erdgeschoss và im dritten Stock.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Nhà ăn trong công ty của Ngài nằm ở đâu? — Nó nằm ở tầng trệt, còn văn phòng của tôi ở tầng ba."
                }
        },
        {
                "q_num": 12,
                "type": "trac_nghiem",
                "question": "Câu 12: Dãy số thứ tự nào sau đây được viết ĐÚNG HOÀN TOÀN cho các mốc 1. — 3. — 7. — 8. ở Cách 1 (Nominativ)?",
                "options_json": "[\"der einsigste — der dreite — der siebente — der achtte\", \"der erste — der dritte — der siebte — der achte\", \"der erste — der dreite — der siebte — der achte\", \"der ersten — der dritten — der siebten — der achten\"]",
                "correct_answer": "der erste — der dritte — der siebte — der achte",
                "explanation": "Bốn số thứ tự bất quy tắc từ 1 đến 19 ở Nominativ là: 1. -> erste, 3. -> dritte, 7. -> siebte (bỏ -en), 8. -> achte (chỉ có một chữ t).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Thứ nhất — Thứ ba — Thứ bảy — Thứ tám."
                }
        },
        {
                "q_num": 13,
                "type": "trac_nghiem",
                "question": "Câu 13: Số thứ tự của 23. sau mạo từ der ở Cách 1 (Nominativ) được viết như thế nào?",
                "options_json": "[\"derdreiundzwanzigste\", \"der dritteundzwanzigste\", \"der dreiundzwanzigste\", \"der dreiundzwanzigsten\"]",
                "correct_answer": "der dreiundzwanzigste",
                "explanation": "Từ 20 trở đi, số thứ tự được tạo bằng cách thêm đuôi -ste vào cuối số đếm: dreiundzwanzig + -ste → der dreiundzwanzigste (phần hàng đơn vị drei ở đầu giữ nguyên, không đổi thành dritte).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Thứ hai mươi ba (ngày 23)."
                }
        },
        {
                "q_num": 14,
                "type": "trac_nghiem",
                "question": "Câu 14: Chọn cặp từ đúng cho cuộc hội thoại: „Welcher Tag ist heute? — Heute ist der ___ Oktober (20.10.). Und wann fliegt ihr nach Wien? — Wir fliegen am ___ Oktober (25.10.).“",
                "options_json": "[\"zwanzigsten / fünfundzwanzigste\", \"zwanzigste / fünfundzwanzigsten\", \"zwanzig / fünfundzwanzig\", \"zwanzigster / fünfundzwanzigster\"]",
                "correct_answer": "zwanzigste / fünfundzwanzigsten",
                "explanation": "Sau Heute ist der ... (Nominativ) dùng đuôi -ste (der zwanzigste Oktober). Sau giới từ am (Dativ) bắt buộc phải thêm -n thành đuôi -sten (am fünfundzwanzigsten Oktober).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Hôm nay là ngày mấy? — Hôm nay là ngày 20 tháng Mười. Và khi nào các bạn bay đi Viên? — Chúng tôi bay vào ngày 25 tháng Mười."
                }
        },
        {
                "q_num": 15,
                "type": "trac_nghiem",
                "question": "Câu 15: Chọn phương án đúng để diễn đạt \"từ ngày 01/07 đến ngày 14/07\": „Unsere Kollegen haben ___ Juli Sommerurlaub.“",
                "options_json": "[\"von ersten bis vierzehnte\", \"vom erste bis zum vierzehnte\", \"vom ersten bis zum vierzehnten\", \"am ersten bis am vierzehnten\"]",
                "correct_answer": "vom ersten bis zum vierzehnten",
                "explanation": "Trong cấu trúc vom ... bis zum ..., cả vom (von + dem) và zum (zu + dem) đều ở Cách 3 (Dativ), nên cả hai số thứ tự đều phải chia đuôi -ten (vom ersten bis zum vierzehnten Juli).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Các đồng nghiệp của chúng tôi có kỳ nghỉ hè từ ngày mùng 1 đến ngày 14 tháng Bảy."
                }
        },
        {
                "q_num": 16,
                "type": "trac_nghiem",
                "question": "Câu 16: Câu nào dưới đây viết và đọc ĐÚNG nghĩa \"Bố tôi sinh năm 1968 tại Hải Phòng\"?",
                "options_json": "[\"Mein Vater ist in 1968 (neunzehnhundertachtundsechzig) in Hai Phong geboren.\", \"Mein Vater ist 1968 (neunzehnhundertachtundsechzig) in Hai Phong geboren.\", \"Mein Vater ist am 1968 (tausendneunhundertachtundsechzig) in Hai Phong geboren.\", \"Mein Vater war im 1968 in Hai Phong geboren.\"]",
                "correct_answer": "Mein Vater ist 1968 (neunzehnhundertachtundsechzig) in Hai Phong geboren.",
                "explanation": "Trong tiếng Đức, khi chỉ năm đơn lẻ, ta viết trực tiếp số năm (1968) hoặc dùng im Jahr 1968 (tuyệt đối không dùng in 1968 hay am 1968). Năm 1968 đọc theo hàng trăm là neunzehnhundertachtundsechzig.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Bố tôi sinh năm 1968 tại Hải Phòng."
                }
        },
        {
                "q_num": 17,
                "type": "trac_nghiem",
                "question": "Câu 17: Chọn phương án đúng hoàn thành câu: „Paula, ___ du bitte ___ Großmutter in der Küche?“",
                "options_json": "[\"helfst / die\", \"hilfst / deiner\", \"hilft / deine\", \"helfe / deinem\"]",
                "correct_answer": "hilfst / deiner",
                "explanation": "Động từ helfen biến âm e -> i ở ngôi du thành hilfst, và đòi hỏi tân ngữ ở Cách 3 (Dativ). Vì die Großmutter mang giống cái nên deine đổi thành deiner Großmutter.",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Paula ơi, bạn làm ơn giúp bà của bạn ở trong bếp nhé?"
                }
        },
        {
                "q_num": 18,
                "type": "trac_nghiem",
                "question": "Câu 18: Chọn câu hoàn chỉnh đúng ngữ pháp 100%:",
                "options_json": "[\"Am drittem Mai fahren wir mit den Zug zu unseren Freunden.\", \"Am dritten Mai fahren wir mit dem Zug zu unseren Freunden.\", \"Im dritten Mai fahren wir mit dem Zug nach unseren Freunden.\", \"Am dritte Mai fährt wir mit der Zug bei unseren Freunde.\"]",
                "correct_answer": "Am dritten Mai fahren wir mit dem Zug zu unseren Freunden.",
                "explanation": "Ngày cụ thể dùng Am dritten Mai; phương tiện der Zug dùng mit dem Zug; đi tới chỗ người dùng zu + Dativ số nhiều là zu unseren Freunden (danh từ Freunde thêm -n).",
                "exp_reward": 15,
                "extra_data": {
                        "translation": "Vào ngày mùng 3 tháng Năm, chúng tôi đi bằng tàu hỏa tới chỗ những người bạn của chúng tôi."
                }
        },
        {
                "q_num": 19,
                "type": "dien_khuyet",
                "question": "Câu 19: Điền giới từ thu gọn thích hợp vào chỗ trống: „Jeden Morgen geht mein Sohn um 7 Uhr zu Fuß ___ Schule.“",
                "options_json": null,
                "correct_answer": "zur",
                "explanation": "die Schule mang giống cái; đi đến trường dùng zu + der Schule viết tắt bắt buộc thành zur Schule.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "zur"
                        ],
                        "translation": "Mỗi buổi sáng con trai tôi đi bộ đến trường lúc 7 giờ."
                }
        },
        {
                "q_num": 20,
                "type": "dien_khuyet",
                "question": "Câu 20: Điền giới từ thu gọn thích hợp vào chỗ trống: „Wann kommt deine Schwester heute Abend ___ Flughafen zurück?“",
                "options_json": null,
                "correct_answer": "vom",
                "explanation": "Từ một địa điểm trở về dùng giới từ von + Dativ; der Flughafen mang giống đực nên von + dem viết tắt thành vom Flughafen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "vom"
                        ],
                        "translation": "Tối nay khi nào chị gái của bạn từ sân bay trở về?"
                }
        },
        {
                "q_num": 21,
                "type": "dien_khuyet",
                "question": "Câu 21: Điền giới từ thu gọn thích hợp vào chỗ trống: „Gestern war mein Großvater zwei Stunden ___ Arzt.“",
                "options_json": null,
                "correct_answer": "beim",
                "explanation": "Ở chỗ bác sĩ (der Arzt) dùng bei + dem Arzt viết tắt thành beim Arzt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "beim"
                        ],
                        "translation": "Hôm qua ông của tôi đã ở chỗ bác sĩ hai tiếng đồng hồ."
                }
        },
        {
                "q_num": 22,
                "type": "dien_khuyet",
                "question": "Câu 22: Điền mạo từ xác định đúng ở Cách 3 (Dativ) vào chỗ trống: „Viele Fahrgäste warten am Morgen an ___ Haltestelle (die Haltestelle).“",
                "options_json": null,
                "correct_answer": "der",
                "explanation": "Danh từ die Haltestelle mang giống cái (Femininum). Sau giới từ chỉ vị trí an (trả lời câu hỏi Wo? - Ở đâu?) thuộc Cách 3 (Dativ), mạo từ xác định đổi từ die thành der (an der Haltestelle).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der"
                        ],
                        "translation": "Nhiều hành khách đứng đợi ở trạm dừng vào buổi sáng."
                }
        },
        {
                "q_num": 23,
                "type": "dien_khuyet",
                "question": "Câu 23: Điền mạo từ sở hữu đúng của ngôi er (sein-) ở Cách 3 (Dativ) vào chỗ trống: „Thomas fährt jeden Sonntag mit ___ Fahrrad (das Fahrrad) durch den Park.“",
                "options_json": null,
                "correct_answer": "seinem",
                "explanation": "Sau giới từ mit bắt buộc dùng Cách 3 (Dativ). Danh từ das Fahrrad mang giống trung (Neutrum), nên gốc mạo từ sở hữu sein- của Thomas (ngôi er) nhận đuôi -em thành seinem Fahrrad.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "seinem"
                        ],
                        "translation": "Thomas đạp xe đạp của anh ấy qua công viên vào mỗi Chủ nhật."
                }
        },
        {
                "q_num": 24,
                "type": "dien_khuyet",
                "question": "Câu 24: Điền mạo từ sở hữu đúng của ngôi Sie (Ihr- viết hoa) ở Cách 3 (Dativ) vào chỗ trống: „Herr Direktor, der Brief liegt auf ___ Schreibtisch neben dem Laptop.“",
                "options_json": null,
                "correct_answer": "Ihrem",
                "explanation": "der Schreibtisch mang giống đực, ở Dativ sau giới từ auf thì mạo từ sở hữu của ngôi Sie là Ihrem Schreibtisch.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Ihrem"
                        ],
                        "translation": "Thưa Ngài Giám đốc, bức thư nằm ở trên bàn làm việc của Ngài bên cạnh chiếc máy tính xách tay."
                }
        },
        {
                "q_num": 25,
                "type": "dien_khuyet",
                "question": "Câu 25: Điền dạng đúng của danh từ số nhiều die Freunde ở Cách 3 (Dativ) vào chỗ trống: „Am Samstag gehen wir mit unseren ___ ins Kino.“",
                "options_json": null,
                "correct_answer": "Freunden",
                "explanation": "Ở Cách 3 (Dativ) số nhiều, danh từ die Freunde bắt buộc phải thêm đuôi -n thành Freunden.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Freunden"
                        ],
                        "translation": "Vào thứ Bảy chúng tôi đi xem phim cùng với những người bạn của chúng tôi."
                }
        },
        {
                "q_num": 26,
                "type": "dien_khuyet",
                "question": "Câu 26: Điền dạng chia đúng của động từ fahren theo chủ ngữ vào chỗ trống: „Frau Kien, wann ___ der nächste Bus zum Hauptbahnhof?“",
                "options_json": null,
                "correct_answer": "fährt",
                "explanation": "Chủ ngữ của câu hỏi là der nächste Bus (ngôi thứ 3 số ít er), nên động từ fahren biến âm a -> ä thành fährt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "fährt",
                                "faehrt"
                        ],
                        "translation": "Bà Kiên ơi, khi nào chuyến xe buýt tiếp theo chạy tới nhà ga trung tâm vậy?"
                }
        },
        {
                "q_num": 27,
                "type": "dien_khuyet",
                "question": "Câu 27: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: „Die Personalabteilung befindet sich im ___ (1.) Stock.“",
                "options_json": null,
                "correct_answer": "ersten",
                "explanation": "Đi sau giới từ im (in + dem — Dativ), số thứ tự 1. (erste) phải thêm đuôi -n thành im ersten Stock.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ersten"
                        ],
                        "translation": "Phòng nhân sự nằm ở tầng một."
                }
        },
        {
                "q_num": 28,
                "type": "dien_khuyet",
                "question": "Câu 28: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: „Unsere neue Wohnung liegt im ___ (7.) Stock.“",
                "options_json": null,
                "correct_answer": "siebten",
                "explanation": "Số thứ tự của 7 là bất quy tắc (siebte), đi sau im (Dativ) thêm -n thành im siebten Stock.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "siebten"
                        ],
                        "translation": "Căn hộ mới của chúng tôi nằm ở tầng bảy."
                }
        },
        {
                "q_num": 29,
                "type": "dien_khuyet",
                "question": "Câu 29: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: „Welcher Tag ist heute? — Heute ist der ___ (3.) April.“",
                "options_json": null,
                "correct_answer": "dritte",
                "explanation": "Sau Heute ist der ... là Cách 1 (Nominativ), nên số thứ tự 3. chia là der dritte April (không có -n).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "dritte"
                        ],
                        "translation": "Hôm nay là ngày mấy? — Hôm nay là ngày mùng 3 tháng Tư."
                }
        },
        {
                "q_num": 30,
                "type": "dien_khuyet",
                "question": "Câu 30: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: „Wann feiert deine Schwester ihren Geburtstag? — Sie feiert am ___ (8.) März ihren Geburtstag.“",
                "options_json": null,
                "correct_answer": "achten",
                "explanation": "Số thứ tự của mốc 8 là achte (chỉ viết một chữ t). Đứng sau giới từ am (Dativ chỉ thời điểm ngày), số thứ tự bắt buộc thêm đuôi -n thành am achten März.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "achten"
                        ],
                        "translation": "Khi nào chị gái của bạn tổ chức sinh nhật? — Chị ấy tổ chức sinh nhật vào ngày mùng 8 tháng Ba."
                }
        },
        {
                "q_num": 31,
                "type": "dien_khuyet",
                "question": "Câu 31: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: „Der Deutschkurs beginnt am ___ (20.) September.“",
                "options_json": null,
                "correct_answer": "zwanzigsten",
                "explanation": "Từ số 20 trở đi, số thứ tự dùng đuôi -ste (Nominativ) và -sten (Dativ sau am) → am zwanzigsten September.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "zwanzigsten"
                        ],
                        "translation": "Khóa học tiếng Đức bắt đầu vào ngày 20 tháng Chín."
                }
        },
        {
                "q_num": 32,
                "type": "dien_khuyet",
                "question": "Câu 32: Điền giới từ chỉ vị trí thích hợp vào chỗ trống: „In unserem neuen Wohnzimmer hängt eine moderne Uhr ___ der Wand.“",
                "options_json": null,
                "correct_answer": "an",
                "explanation": "Khi miêu tả đồ vật treo áp sát tiếp xúc trên bề mặt thẳng đứng như bức tường (die Wand), trong tiếng Đức bắt buộc dùng giới từ an (an der Wand).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "an"
                        ],
                        "translation": "Trong phòng khách mới của chúng tôi có một chiếc đồng hồ hiện đại treo trên tường."
                }
        },
        {
                "q_num": 33,
                "type": "dien_khuyet",
                "question": "Câu 33: Điền dạng chia đúng của động từ gefallen vào chỗ trống: „Wie ___ dir das neue Fahrrad von deinem Bruder?“",
                "options_json": null,
                "correct_answer": "gefällt",
                "explanation": "Chủ ngữ của câu là das neue Fahrrad (ngôi es), nên động từ gefallen biến âm a -> ä thành gefällt (đi với tân ngữ Dativ là dir).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "gefällt",
                                "gefaellt"
                        ],
                        "translation": "Bạn thấy thích chiếc xe đạp mới của anh trai bạn như thế nào?"
                }
        },
        {
                "q_num": 34,
                "type": "dich_nghia_vd",
                "question": "Câu 34: Dịch sang tiếng Đức: \"bằng tàu điện ngầm\"",
                "options_json": null,
                "correct_answer": "mit der U-Bahn",
                "explanation": "die U-Bahn (giống cái) đi sau giới từ mit (Dativ) biến đổi thành mit der U-Bahn.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "mit der U-Bahn",
                                "mit der U Bahn"
                        ],
                        "translation": "bằng tàu điện ngầm = mit der U-Bahn"
                }
        },
        {
                "q_num": 35,
                "type": "dich_nghia_vd",
                "question": "Câu 35: Dịch sang tiếng Đức: \"bằng máy bay\"",
                "options_json": null,
                "correct_answer": "mit dem Flugzeug",
                "explanation": "das Flugzeug (giống trung) đi sau giới từ mit (Dativ) biến đổi thành mit dem Flugzeug.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "mit dem Flugzeug"
                        ],
                        "translation": "bằng máy bay = mit dem Flugzeug"
                }
        },
        {
                "q_num": 36,
                "type": "dich_nghia_vd",
                "question": "Câu 36: Dịch sang tiếng Đức: \"đi bộ\"",
                "options_json": null,
                "correct_answer": "zu Fuß",
                "explanation": "Cụm cố định chỉ việc đi bộ trong tiếng Đức là zu Fuß (hoặc zu Fuß gehen).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "zu Fuß",
                                "zu Fuß gehen",
                                "zu Fuss",
                                "zu Fuss gehen"
                        ],
                        "translation": "đi bộ = zu Fuß"
                }
        },
        {
                "q_num": 37,
                "type": "dich_nghia_vd",
                "question": "Câu 37: Dịch sang tiếng Đức: \"ở tầng trệt\"",
                "options_json": null,
                "correct_answer": "im Erdgeschoss",
                "explanation": "Tầng trệt là danh từ giống trung das Erdgeschoss → ở tầng trệt là im Erdgeschoss.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "im Erdgeschoss",
                                "in dem Erdgeschoss"
                        ],
                        "translation": "ở tầng trệt = im Erdgeschoss"
                }
        },
        {
                "q_num": 38,
                "type": "dich_nghia_vd",
                "question": "Câu 38: Dịch sang tiếng Đức: \"ở tầng ba\"",
                "options_json": null,
                "correct_answer": "im dritten Stock",
                "explanation": "Tầng lầu là der Stock (hoặc die Etage), số thứ tự 3 ở Dativ là dritten → im dritten Stock.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "im dritten Stock",
                                "im 3. Stock",
                                "in der dritten Etage",
                                "in der 3. Etage"
                        ],
                        "translation": "ở tầng ba = im dritten Stock"
                }
        },
        {
                "q_num": 39,
                "type": "dich_nghia_vd",
                "question": "Câu 39: Dịch sang tiếng Đức (kèm mạo từ): \"trạm dừng (xe buýt / tàu điện)\"",
                "options_json": null,
                "correct_answer": "die Haltestelle",
                "explanation": "Trạm dừng phương tiện công cộng là danh từ giống cái die Haltestelle (số nhiều: die Haltestellen).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "die Haltestelle",
                                "Haltestelle",
                                "die Bushaltestelle"
                        ],
                        "translation": "trạm dừng (xe buýt / tàu điện) = die Haltestelle"
                }
        },
        {
                "q_num": 40,
                "type": "dich_nghia_vd",
                "question": "Câu 40: Dịch sang tiếng Đức (kèm mạo từ): \"thang máy\"",
                "options_json": null,
                "correct_answer": "der Aufzug",
                "explanation": "Thang máy trong tiếng Đức là danh từ giống đực der Aufzug hoặc der Fahrstuhl.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der Aufzug",
                                "Aufzug",
                                "der Fahrstuhl",
                                "Fahrstuhl"
                        ],
                        "translation": "thang máy = der Aufzug"
                }
        },
        {
                "q_num": 41,
                "type": "dich_nghia_vd",
                "question": "Câu 41: Dịch sang tiếng Đức (kèm mạo từ): \"bàn làm việc\"",
                "options_json": null,
                "correct_answer": "der Schreibtisch",
                "explanation": "Bàn làm việc / bàn viết là danh từ ghép giống đực der Schreibtisch (số nhiều: die Schreibtische).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der Schreibtisch",
                                "Schreibtisch"
                        ],
                        "translation": "bàn làm việc = der Schreibtisch"
                }
        },
        {
                "q_num": 42,
                "type": "dich_nghia_vd",
                "question": "Câu 42: Dịch sang tiếng Đức (kèm mạo từ): \"máy in\"",
                "options_json": null,
                "correct_answer": "der Drucker",
                "explanation": "Máy in là danh từ giống đực der Drucker.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der Drucker",
                                "Drucker"
                        ],
                        "translation": "máy in = der Drucker"
                }
        },
        {
                "q_num": 43,
                "type": "dich_nghia_vd",
                "question": "Câu 43: Dịch cụm vị trí sau sang tiếng Đức: \"phía trước khách sạn\"",
                "options_json": null,
                "correct_answer": "vor dem Hotel",
                "explanation": "Giới từ \"phía trước\" là vor; das Hotel (giống trung) ở Cách 3 (Dativ) đổi thành dem Hotel → vor dem Hotel.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "vor dem Hotel"
                        ],
                        "translation": "phía trước khách sạn = vor dem Hotel"
                }
        },
        {
                "q_num": 44,
                "type": "dich_nghia_vd",
                "question": "Câu 44: Dịch cụm ngày tháng sau sang tiếng Đức: \"vào ngày mùng 1 tháng Năm\"",
                "options_json": null,
                "correct_answer": "am ersten Mai",
                "explanation": "Giới từ am + số thứ tự 1. ở Dativ (ersten) + Mai → am ersten Mai.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "am ersten Mai",
                                "am 1. Mai",
                                "am ersten Fünften",
                                "am 1.5."
                        ],
                        "translation": "vào ngày mùng 1 tháng Năm = am ersten Mai"
                }
        },
        {
                "q_num": 45,
                "type": "dich_nghia_vd",
                "question": "Câu 45: Dịch cụm vị trí sau sang tiếng Đức: \"đang ở nhà / đi về nhà\" (Ghi theo thứ tự: ở nhà / về nhà)",
                "options_json": null,
                "correct_answer": "zu Hause / nach Hause",
                "explanation": "zu Hause dùng cho trạng thái tĩnh (đang ở nhà - Wo?), còn nach Hause dùng cho hành động di chuyển (đi về nhà - Wohin?).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "zu Hause / nach Hause",
                                "zu Hause, nach Hause",
                                "zuhause / nachhause"
                        ],
                        "translation": "đang ở nhà / đi về nhà = zu Hause / nach Hause"
                }
        },
        {
                "q_num": 46,
                "type": "dich_nghia_dv",
                "question": "Câu 46: Dịch sang tiếng Việt: „mit der S-Bahn“",
                "options_json": null,
                "correct_answer": "bằng tàu điện nhanh / bằng tàu điện / bằng tàu S-Bahn / bằng tàu điện đô thị / đi bằng tàu điện nhanh",
                "explanation": "die S-Bahn (Stadtschnellbahn) là tàu điện nhanh đô thị; mit der S-Bahn = bằng tàu điện nhanh / tàu điện đô thị.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "bằng tàu điện nhanh",
                                "bằng tàu điện đô thị",
                                "bằng tàu S-Bahn",
                                "bằng tàu điện",
                                "với tàu điện đô thị",
                                "đi bằng tàu điện nhanh",
                                "bằng tàu nhanh S-Bahn"
                        ],
                        "translation": "Dịch sang tiếng Việt: „mit der S-Bahn“ = bằng tàu điện nhanh"
                }
        },
        {
                "q_num": 47,
                "type": "dich_nghia_dv",
                "question": "Câu 47: Dịch sang tiếng Việt: „die Straßenbahn“",
                "options_json": null,
                "correct_answer": "tàu điện / xe điện / tàu điện mặt đất / tàu điện trên mặt đất / xe điện mặt đất",
                "explanation": "die Straßenbahn là tàu điện chạy trên đường phố (tàu điện mặt đất / xe điện).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "tàu điện",
                                "tàu điện mặt đất",
                                "xe điện",
                                "tàu điện trên mặt đất",
                                "xe điện mặt đất"
                        ],
                        "translation": "Dịch sang tiếng Việt: „die Straßenbahn“ = tàu điện"
                }
        },
        {
                "q_num": 48,
                "type": "dich_nghia_dv",
                "question": "Câu 48: Dịch sang tiếng Việt: „der Konferenzraum“",
                "options_json": null,
                "correct_answer": "phòng họp / phòng hội nghị / phòng họp hội nghị",
                "explanation": "der Konferenzraum (die Konferenz + der Raum) có nghĩa là phòng họp / phòng hội nghị.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "phòng họp",
                                "phòng hội nghị",
                                "phòng họp hội nghị"
                        ],
                        "translation": "Dịch sang tiếng Việt: „der Konferenzraum“ = phòng họp"
                }
        },
        {
                "q_num": 49,
                "type": "dich_nghia_dv",
                "question": "Câu 49: Dịch sang tiếng Việt: „an der Rezeption“",
                "options_json": null,
                "correct_answer": "ở quầy lễ tân / tại quầy lễ tân / ở lễ tân / tại lễ tân / ở bàn tiếp tân / tại bàn lễ tân",
                "explanation": "die Rezeption là quầy lễ tân; ở tại quầy lễ tân dùng giới từ an + Dativ → an der Rezeption.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ở quầy lễ tân",
                                "tại quầy lễ tân",
                                "ở lễ tân",
                                "tại lễ tân",
                                "ở bàn tiếp tân",
                                "tại bàn tiếp tân",
                                "tại bàn lễ tân"
                        ],
                        "translation": "Dịch sang tiếng Việt: „an der Rezeption“ = ở quầy lễ tân"
                }
        },
        {
                "q_num": 50,
                "type": "dich_nghia_dv",
                "question": "Câu 50: Dịch sang tiếng Việt: „zwischen dem Stuhl und dem Schreibtisch“",
                "options_json": null,
                "correct_answer": "ở giữa cái ghế và bàn làm việc / giữa cái ghế và bàn làm việc / ở giữa ghế và bàn làm việc / giữa ghế và bàn làm việc / giữa cái ghế và cái bàn làm việc / ở giữa cái ghế và cái bàn làm việc",
                "explanation": "zwischen = ở giữa; der Stuhl = cái ghế; der Schreibtisch = bàn làm việc.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ở giữa cái ghế và bàn làm việc",
                                "giữa cái ghế và bàn làm việc",
                                "ở giữa ghế và bàn làm việc",
                                "giữa ghế và bàn làm việc",
                                "giữa cái ghế và cái bàn làm việc",
                                "ở giữa cái ghế và cái bàn làm việc",
                                "nằm giữa chiếc ghế và cái bàn làm việc",
                                "ở giữa ghế và bàn viết"
                        ],
                        "translation": "Dịch sang tiếng Việt: „zwischen dem Stuhl und dem Schreibtisch“ = ở giữa cái ghế và bàn làm việc"
                }
        },
        {
                "q_num": 51,
                "type": "dich_nghia_dv",
                "question": "Câu 51: Dịch sang tiếng Việt: „hinter dem Bahnhof“",
                "options_json": null,
                "correct_answer": "ở phía sau nhà ga / phía sau nhà ga / ở đằng sau nhà ga / đằng sau nhà ga / sau nhà ga / ở sau nhà ga",
                "explanation": "Giới từ hinter có nghĩa là ở phía sau / đằng sau; der Bahnhof = nhà ga.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ở phía sau nhà ga",
                                "phía sau nhà ga",
                                "ở đằng sau nhà ga",
                                "đằng sau nhà ga",
                                "sau nhà ga",
                                "ở sau nhà ga",
                                "phía sau ga tàu",
                                "sau ga tàu"
                        ],
                        "translation": "Dịch sang tiếng Việt: „hinter dem Bahnhof“ = ở phía sau nhà ga"
                }
        },
        {
                "q_num": 52,
                "type": "dich_nghia_dv",
                "question": "Câu 52: Dịch sang tiếng Việt: „unter dem Tisch“",
                "options_json": null,
                "correct_answer": "dưới bàn / ở dưới bàn / dưới cái bàn / ở dưới cái bàn / phía dưới bàn / dưới gầm bàn / ở dưới gầm bàn",
                "explanation": "Giới từ unter có nghĩa là ở phía dưới / dưới gầm.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "dưới bàn",
                                "ở dưới bàn",
                                "dưới cái bàn",
                                "ở dưới cái bàn",
                                "phía dưới bàn",
                                "dưới gầm bàn",
                                "ở dưới gầm bàn",
                                "phía dưới cái bàn"
                        ],
                        "translation": "Dịch sang tiếng Việt: „unter dem Tisch“ = dưới bàn"
                }
        },
        {
                "q_num": 53,
                "type": "dich_nghia_dv",
                "question": "Câu 53: Dịch sang tiếng Việt: „über dem Sofa“",
                "options_json": null,
                "correct_answer": "phía trên ghế sofa / ở phía trên ghế sofa / trên ghế sofa / ở trên ghế sofa / phía trên ghế sô pha / trên ghế sô pha",
                "explanation": "Giới từ über chỉ vị trí ở phía trên cao hơn vật mốc (không tiếp xúc trực tiếp với bề mặt sofa).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "phía trên ghế sofa",
                                "ở phía trên ghế sofa",
                                "trên ghế sofa",
                                "ở trên ghế sofa",
                                "phía trên ghế sô pha",
                                "trên ghế sô pha",
                                "ở phía trên ghế sô pha",
                                "treo phía trên ghế sô pha"
                        ],
                        "translation": "Dịch sang tiếng Việt: „über dem Sofa“ = phía trên ghế sofa"
                }
        },
        {
                "q_num": 54,
                "type": "dich_nghia_dv",
                "question": "Câu 54: Dịch sang tiếng Việt: „bei meinen Eltern“",
                "options_json": null,
                "correct_answer": "ở chỗ bố mẹ tôi / ở nhà bố mẹ tôi / ở với bố mẹ tôi / với bố mẹ tôi / ở chỗ cha mẹ tôi / ở chỗ ba mẹ tôi / ở cùng bố mẹ tôi",
                "explanation": "Giới từ bei + người có nghĩa là ở tại nhà / chỗ của người đó (bei meinen Eltern = ở nhà bố mẹ tôi).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ở chỗ bố mẹ tôi",
                                "ở nhà bố mẹ tôi",
                                "tại nhà bố mẹ tôi",
                                "với bố mẹ tôi",
                                "ở cùng bố mẹ tôi",
                                "ở chỗ cha mẹ tôi",
                                "ở nhà ba mẹ tôi",
                                "ở chỗ ba mẹ tôi"
                        ],
                        "translation": "Dịch sang tiếng Việt: „bei meinen Eltern“ = ở chỗ bố mẹ tôi"
                }
        },
        {
                "q_num": 55,
                "type": "dich_nghia_dv",
                "question": "Câu 55: Dịch sang tiếng Việt: „am einundzwanzigsten Juni“",
                "options_json": null,
                "correct_answer": "vào ngày 21 tháng 6 / ngày 21 tháng 6 / vào ngày 21 tháng Sáu / ngày 21 tháng Sáu / ngày 21/6 / vào ngày 21/6 / 21/6",
                "explanation": "einundzwanzigsten là số thứ tự 21. ở Cách 3 (Dativ) sau giới từ am; Juni = tháng Sáu.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "vào ngày 21 tháng 6",
                                "vào ngày 21 tháng Sáu",
                                "ngày 21 tháng 6",
                                "ngày 21 tháng Sáu",
                                "ngày 21/6",
                                "21/6",
                                "vào ngày 21/6",
                                "vào ngày hai mươi mốt tháng Sáu"
                        ],
                        "translation": "Dịch sang tiếng Việt: „am einundzwanzigsten Juni“ = vào ngày 21 tháng 6"
                }
        },
        {
                "q_num": 56,
                "type": "dich_nghia_dv",
                "question": "Câu 56: Dịch sang tiếng Việt: „vom dritten bis zum zehnten August“",
                "options_json": null,
                "correct_answer": "từ ngày 3 đến ngày 10 tháng 8 / từ ngày mùng 3 đến ngày 10 tháng 8 / từ ngày 3 đến 10 tháng 8 / từ 3 đến 10 tháng 8 / từ ngày 3 đến ngày 10 tháng Tám / từ 3/8 đến 10/8",
                "explanation": "vom ... bis zum ... = từ ngày ... đến ngày ...; dritten = ngày 3; zehnten = ngày 10; August = tháng Tám.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "từ ngày 3 đến ngày 10 tháng 8",
                                "từ ngày mùng 3 đến ngày 10 tháng 8",
                                "từ ngày mùng 3 đến ngày 10 tháng Tám",
                                "từ ngày 3 đến 10 tháng 8",
                                "từ 3 đến 10 tháng 8",
                                "từ 3/8 đến 10/8",
                                "từ ngày 3/8 đến 10/8"
                        ],
                        "translation": "Dịch sang tiếng Việt: „vom dritten bis zum zehnten August“ = từ ngày 3 đến ngày 10 tháng 8"
                }
        },
        {
                "q_num": 57,
                "type": "dich_nghia_dv",
                "question": "Câu 57: Dịch sang tiếng Việt: „die Tastatur und die Maus“",
                "options_json": null,
                "correct_answer": "bàn phím và chuột / bàn phím và con chuột / chuột và bàn phím / con chuột và bàn phím / bàn phím và chuột máy tính",
                "explanation": "die Tastatur = bàn phím máy tính; die Maus = con chuột máy tính.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "bàn phím và chuột",
                                "bàn phím và con chuột",
                                "chuột và bàn phím",
                                "con chuột và bàn phím",
                                "bàn phím và con chuột máy tính",
                                "bàn phím và chuột máy tính"
                        ],
                        "translation": "Dịch sang tiếng Việt: „die Tastatur und die Maus“ = bàn phím và chuột"
                }
        },
        {
                "q_num": 58,
                "type": "noi_o",
                "question": "Câu 58 (Bài nối ô 1): Nối các ô ở cột trái với ô tương ứng ở cột phải (Biến đổi mạo từ sang Cách 3 Dativ):",
                "options_json": null,
                "correct_answer": "Đi bằng tàu điện ngầm (danh từ giống Cái: die U-Bahn) - mit der U-Bahn (die biến đổi thành der), Gặp nhau ở nhà ga (danh từ giống Đực: der Bahnhof) - am Bahnhof (an + dem gộp thành am), Đỗ xe phía trước khách sạn (danh từ giống Trung: das Hotel) - vor dem Hotel (das biến đổi thành dem), Đi dã ngoại cùng bọn trẻ (danh từ Số nhiều: die Kinder) - mit den Kindern (die biến đổi thành den + thêm đuôi -n)",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Đi bằng tàu điện ngầm (danh từ giống Cái: die U-Bahn)",
                                        "right": "mit der U-Bahn (die biến đổi thành der)"
                                },
                                {
                                        "left": "Gặp nhau ở nhà ga (danh từ giống Đực: der Bahnhof)",
                                        "right": "am Bahnhof (an + dem gộp thành am)"
                                },
                                {
                                        "left": "Đỗ xe phía trước khách sạn (danh từ giống Trung: das Hotel)",
                                        "right": "vor dem Hotel (das biến đổi thành dem)"
                                },
                                {
                                        "left": "Đi dã ngoại cùng bọn trẻ (danh từ Số nhiều: die Kinder)",
                                        "right": "mit den Kindern (die biến đổi thành den + thêm đuôi -n)"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Biến đổi mạo từ sang Cách 3 Dativ."
                }
        },
        {
                "q_num": 59,
                "type": "noi_o",
                "question": "Câu 59 (Bài nối ô 2): Nối các ô ở cột trái với ô tương ứng ở cột phải (Các dạng gộp giới từ + mạo từ ở Dativ):",
                "options_json": null,
                "correct_answer": "Đi bộ đến trường học (địa điểm giống Cái) - zur Schule (viết gọn bắt buộc của zu + der Schule), Đi tàu ra ga chính (địa điểm giống Đực) - zum Hauptbahnhof (viết gọn bắt buộc của zu + dem Hauptbahnhof), Đang ở chỗ bác sĩ khám bệnh (người / chuyên gia) - beim Arzt (viết gọn bắt buộc của bei + dem Arzt), Đón người thân trở về từ sân bay (địa điểm xuất phát) - vom Flughafen (viết gọn bắt buộc của von + dem Flughafen)",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Đi bộ đến trường học (địa điểm giống Cái)",
                                        "right": "zur Schule (viết gọn bắt buộc của zu + der Schule)"
                                },
                                {
                                        "left": "Đi tàu ra ga chính (địa điểm giống Đực)",
                                        "right": "zum Hauptbahnhof (viết gọn bắt buộc của zu + dem Hauptbahnhof)"
                                },
                                {
                                        "left": "Đang ở chỗ bác sĩ khám bệnh (người / chuyên gia)",
                                        "right": "beim Arzt (viết gọn bắt buộc của bei + dem Arzt)"
                                },
                                {
                                        "left": "Đón người thân trở về từ sân bay (địa điểm xuất phát)",
                                        "right": "vom Flughafen (viết gọn bắt buộc của von + dem Flughafen)"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Các dạng gộp giới từ + mạo từ ở Dativ."
                }
        },
        {
                "q_num": 60,
                "type": "noi_o",
                "question": "Câu 60 (Bài nối ô 3): Nối các ô ở cột trái với ô tương ứng ở cột phải (Phương tiện giao thông & Cách diễn đạt chuẩn):",
                "options_json": null,
                "correct_answer": "die U-Bahn (tàu điện ngầm) - mit der U-Bahn fahren, das Flugzeug (máy bay) - mit dem Flugzeug fliegen, das Fahrrad (xe đạp) - mit dem Fahrrad fahren, der Fuß (đi bộ - ngoại lệ) - zu Fuß gehen",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "die U-Bahn (tàu điện ngầm)",
                                        "right": "mit der U-Bahn fahren"
                                },
                                {
                                        "left": "das Flugzeug (máy bay)",
                                        "right": "mit dem Flugzeug fliegen"
                                },
                                {
                                        "left": "das Fahrrad (xe đạp)",
                                        "right": "mit dem Fahrrad fahren"
                                },
                                {
                                        "left": "der Fuß (đi bộ - ngoại lệ)",
                                        "right": "zu Fuß gehen"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Phương tiện giao thông & Cách diễn đạt chuẩn."
                }
        },
        {
                "q_num": 61,
                "type": "noi_o",
                "question": "Câu 61 (Bài nối ô 4): Nối các ô ở cột trái với ô tương ứng ở cột phải (Giới từ vị trí Wo? trên bàn làm việc):",
                "options_json": null,
                "correct_answer": "auf dem Schreibtisch - nằm ở trên mặt bàn làm việc (có tiếp xúc), unter dem Schreibtisch - đặt ở dưới gầm bàn làm việc, neben der Tastatur - nằm ở bên cạnh bàn phím, an der Wand über dem Tisch - treo trên tường phía trên cái bàn",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "auf dem Schreibtisch",
                                        "right": "nằm ở trên mặt bàn làm việc (có tiếp xúc)"
                                },
                                {
                                        "left": "unter dem Schreibtisch",
                                        "right": "đặt ở dưới gầm bàn làm việc"
                                },
                                {
                                        "left": "neben der Tastatur",
                                        "right": "nằm ở bên cạnh bàn phím"
                                },
                                {
                                        "left": "an der Wand über dem Tisch",
                                        "right": "treo trên tường phía trên cái bàn"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Giới từ vị trí Wo? trên bàn làm việc."
                }
        },
        {
                "q_num": 62,
                "type": "noi_o",
                "question": "Câu 62 (Bài nối ô 5): Nối các ô ở cột trái với ô tương ứng ở cột phải (Số đếm sang Số thứ tự bất quy tắc & từ 20):",
                "options_json": null,
                "correct_answer": "1 (eins) - der erste / am ersten, 3 (drei) - der dritte / am dritten, 7 (sieben) - der siebte / am siebten, 20 (zwanzig) - der zwanzigste / am zwanzigsten",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "1 (eins)",
                                        "right": "der erste / am ersten"
                                },
                                {
                                        "left": "3 (drei)",
                                        "right": "der dritte / am dritten"
                                },
                                {
                                        "left": "7 (sieben)",
                                        "right": "der siebte / am siebten"
                                },
                                {
                                        "left": "20 (zwanzig)",
                                        "right": "der zwanzigste / am zwanzigsten"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Số đếm sang Số thứ tự bất quy tắc & từ 20."
                }
        },
        {
                "q_num": 63,
                "type": "noi_o",
                "question": "Câu 63 (Bài nối ô 6): Nối các ô ở cột trái với ô tương ứng ở cột phải (Ngày tháng bằng số sang Cách đọc sau giới từ am):",
                "options_json": null,
                "correct_answer": "am 01.01. - am ersten Januar, am 08.03. - am achten März, am 15.08. - am fünfzehnten August, am 24.12. - am vierundzwanzigsten Dezember",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "am 01.01.",
                                        "right": "am ersten Januar"
                                },
                                {
                                        "left": "am 08.03.",
                                        "right": "am achten März"
                                },
                                {
                                        "left": "am 15.08.",
                                        "right": "am fünfzehnten August"
                                },
                                {
                                        "left": "am 24.12.",
                                        "right": "am vierundzwanzigsten Dezember"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Ngày tháng bằng số sang Cách đọc sau giới từ am."
                }
        },
        {
                "q_num": 64,
                "type": "noi_o",
                "question": "Câu 64 (Bài nối ô 7): Nối các ô ở cột trái với ô tương ứng ở cột phải (Năm bằng số sang Cách đọc chữ tiếng Đức):",
                "options_json": null,
                "correct_answer": "1945 - neunzehnhundertfünfundvierzig, 1989 - neunzehnhundertneunundachtzig, 1998 - neunzehnhundertachtundneunzig, 2026 - zweitausendsechsundzwanzig",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "1945",
                                        "right": "neunzehnhundertfünfundvierzig"
                                },
                                {
                                        "left": "1989",
                                        "right": "neunzehnhundertneunundachtzig"
                                },
                                {
                                        "left": "1998",
                                        "right": "neunzehnhundertachtundneunzig"
                                },
                                {
                                        "left": "2026",
                                        "right": "zweitausendsechsundzwanzig"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Năm bằng số sang Cách đọc chữ tiếng Đức."
                }
        },
        {
                "q_num": 65,
                "type": "noi_o",
                "question": "Câu 65 (Bài nối ô 8): Nối các ô ở cột trái với ô tương ứng ở cột phải (Đại từ nhân xưng sang Mạo từ sở hữu ở Dativ):",
                "options_json": null,
                "correct_answer": "ich (tôi) - mit meinem Bruder / mit meiner Schwester, sie (cô ấy) - mit ihrem Bruder / mit ihrer Schwester, wir (chúng tôi) - mit unserem Bruder / mit unserer Schwester, ihr (các bạn) - mit eurem Bruder / mit eurer Schwester",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "ich (tôi)",
                                        "right": "mit meinem Bruder / mit meiner Schwester"
                                },
                                {
                                        "left": "sie (cô ấy)",
                                        "right": "mit ihrem Bruder / mit ihrer Schwester"
                                },
                                {
                                        "left": "wir (chúng tôi)",
                                        "right": "mit unserem Bruder / mit unserer Schwester"
                                },
                                {
                                        "left": "ihr (các bạn)",
                                        "right": "mit eurem Bruder / mit eurer Schwester"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Đại từ nhân xưng sang Mạo từ sở hữu ở Dativ."
                }
        },
        {
                "q_num": 66,
                "type": "noi_o",
                "question": "Câu 66 (Bài nối ô 9): Nối các ô ở cột trái với ô tương ứng ở cột phải (Câu hỏi định hướng & Thời gian sang Câu trả lời):",
                "options_json": null,
                "correct_answer": "Womit fährt Herr Müller nach Berlin? - Er fährt mit dem Zug., Wo ist das Büro von Frau Schneider? - Es liegt im dritten Stock neben dem Aufzug., Welcher Tag ist heute? - Heute ist der zwölfte Oktober., Wann hast du Geburtstag? - Ich habe am siebten Mai Geburtstag.",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Womit fährt Herr Müller nach Berlin?",
                                        "right": "Er fährt mit dem Zug."
                                },
                                {
                                        "left": "Wo ist das Büro von Frau Schneider?",
                                        "right": "Es liegt im dritten Stock neben dem Aufzug."
                                },
                                {
                                        "left": "Welcher Tag ist heute?",
                                        "right": "Heute ist der zwölfte Oktober."
                                },
                                {
                                        "left": "Wann hast du Geburtstag?",
                                        "right": "Ich habe am siebten Mai Geburtstag."
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Câu hỏi định hướng & Thời gian sang Câu trả lời."
                }
        },
        {
                "q_num": 67,
                "type": "noi_o",
                "question": "Câu 67 (Bài nối ô 10): Nối các ô ở cột trái với ô tương ứng ở cột phải (Động từ Bài 6 sang Nghĩa & Quy tắc biến âm):",
                "options_json": null,
                "correct_answer": "fahren (du fährst, er fährt) - đi bằng xe/tàu (biến âm a -> ä), umsteigen (steigt ... um) - đổi tàu / chuyển tuyến xe (động từ tách), helfen (du hilfst, er hilft + Dativ) - giúp đỡ ai đó (biến âm e -> i), hängen (hängt + Wo? Dativ) - treo ở đâu đó (vị trí tĩnh)",
                "explanation": "Nối chính xác 100% cả 4 cặp tương ứng.",
                "exp_reward": 25,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "fahren (du fährst, er fährt)",
                                        "right": "đi bằng xe/tàu (biến âm a -> ä)"
                                },
                                {
                                        "left": "umsteigen (steigt ... um)",
                                        "right": "đổi tàu / chuyển tuyến xe (động từ tách)"
                                },
                                {
                                        "left": "helfen (du hilfst, er hilft + Dativ)",
                                        "right": "giúp đỡ ai đó (biến âm e -> i)"
                                },
                                {
                                        "left": "hängen (hängt + Wo? Dativ)",
                                        "right": "treo ở đâu đó (vị trí tĩnh)"
                                }
                        ],
                        "translation": "Bài tập nối 4 cặp thẻ chuẩn kiến thức Động từ Bài 6 sang Nghĩa & Quy tắc biến âm."
                }
        },
        {
                "q_num": 68,
                "type": "dien_tao_cau",
                "question": "Câu 68: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Jeden Morgen ___ mein Bruder mit ___ U-Bahn zur Arbeit.'",
                "options_json": null,
                "correct_answer": "fährt / der",
                "explanation": "Chủ ngữ mein Bruder (er) chia động từ fahren là fährt; die U-Bahn (giống cái) sau mit (Dativ) đổi thành mit der U-Bahn.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "fährt / der",
                                "fährt/der",
                                "faehrt / der",
                                "faehrt/der"
                        ],
                        "translation": "„Mỗi buổi sáng anh trai tôi đi làm bằng tàu điện ngầm."
                }
        },
        {
                "q_num": 69,
                "type": "dien_tao_cau",
                "question": "Câu 69: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Unser Büro liegt ___ zweiten Stock neben ___ Aufzug.'",
                "options_json": null,
                "correct_answer": "im / dem",
                "explanation": "Ở tầng hai dùng im zweiten Stock; der Aufzug (giống đực) sau giới từ neben (Wo? + Dativ) đổi thành neben dem Aufzug.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "im / dem",
                                "im/dem"
                        ],
                        "translation": "„Văn phòng của chúng tôi nằm ở tầng hai bên cạnh thang máy."
                }
        },
        {
                "q_num": 70,
                "type": "dien_tao_cau",
                "question": "Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Das Café liegt zwischen ___ Bank und ___ Kino.'",
                "options_json": null,
                "correct_answer": "der / dem",
                "explanation": "Sau zwischen (Wo? + Dativ), danh từ giống cái die Bank đổi thành der Bank, danh từ giống trung das Kino đổi thành dem Kino.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der / dem",
                                "der/dem"
                        ],
                        "translation": "„Quán cà phê nằm giữa ngân hàng và rạp chiếu phim."
                }
        },
        {
                "q_num": 71,
                "type": "dien_tao_cau",
                "question": "Câu 71: Điền dạng chữ của số thứ tự cho ngày 1. và ngày 2. vào các chỗ trống (ngăn cách bởi dấu /): 'Heute ist der ___ (1.) Mai, und morgen am ___ (2.) Mai fliegen wir nach Italien.'",
                "options_json": null,
                "correct_answer": "erste / zweiten",
                "explanation": "Sau Heute ist der ... (Nominativ) dùng đuôi -te (erste); sau am (Dativ) dùng đuôi -ten (zweiten).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "erste / zweiten",
                                "erste/zweiten",
                                "Erste / Zweiten",
                                "erste / zweite",
                                "erste/zweite",
                                "1. / 2.",
                                "1./2.",
                                "1 / 2",
                                "1/2",
                                "erste / 2.",
                                "1. / zweiten"
                        ],
                        "translation": "„Hôm nay là ngày mùng 1 tháng Năm, và ngày mai vào ngày mùng 2 tháng Năm chúng tôi bay sang Ý."
                }
        },
        {
                "q_num": 72,
                "type": "dien_tao_cau",
                "question": "Câu 72: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Am Sonntag spielen die Kinder ___ Park mit ihren ___ (Freunde).'",
                "options_json": null,
                "correct_answer": "im / Freunden",
                "explanation": "Trong công viên (der Park) là im Park; danh từ số nhiều Freunde ở Cách 3 (Dativ) sau mit ihren bắt buộc thêm -n thành Freunden.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "im / Freunden",
                                "im/Freunden",
                                "Im / Freunden",
                                "im / freunden"
                        ],
                        "translation": "„Vào Chủ nhật bọn trẻ chơi ở trong công viên với những người bạn của chúng."
                }
        },
        {
                "q_num": 73,
                "type": "dien_tao_cau",
                "question": "Câu 73: Điền dạng chữ của số thứ tự cho ngày 7. và ngày 20. vào các chỗ trống (ngăn cách bởi dấu /): 'Habt ihr vom ___ (7.) bis zum ___ (20.) August Urlaub?'",
                "options_json": null,
                "correct_answer": "siebten / zwanzigsten",
                "explanation": "Cả hai vị trí sau vom và bis zum đều chia ở Dativ: 7. -> siebten, 20. -> zwanzigsten.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "siebten / zwanzigsten",
                                "siebten/zwanzigsten",
                                "Siebten / Zwanzigsten",
                                "siebte / zwanzigste",
                                "siebte/zwanzigste",
                                "7. / 20.",
                                "7./20.",
                                "7 / 20",
                                "7/20",
                                "siebten / 20.",
                                "7. / zwanzigsten"
                        ],
                        "translation": "„Các bạn có kỳ nghỉ từ ngày mùng 7 đến ngày 20 tháng Tám phải không?"
                }
        },
        {
                "q_num": 74,
                "type": "dien_tao_cau",
                "question": "Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Zug ___ um 9 Uhr vom Hauptbahnhof ___.'",
                "options_json": null,
                "correct_answer": "fährt / ab",
                "explanation": "Động từ tách abfahren chia cho ngôi thứ 3 số ít (der Zug) biến âm thành fährt ở vị trí số 2 và tách tiền tố ab xuống cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "fährt / ab",
                                "fährt/ab",
                                "faehrt / ab",
                                "faehrt/ab"
                        ],
                        "translation": "„Chuyến tàu khởi hành lúc 9 giờ từ nhà ga trung tâm."
                }
        },
        {
                "q_num": 75,
                "type": "dien_tao_cau",
                "question": "Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Die Katze schläft ___ dem Stuhl von ___ Vater.'",
                "options_json": null,
                "correct_answer": "unter / meinem",
                "explanation": "Giới từ \"dưới gầm\" là unter; sau giới từ von (+ Dativ), mein Vater (giống đực) đổi thành von meinem Vater.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "unter / meinem",
                                "unter/meinem"
                        ],
                        "translation": "„Con mèo đang ngủ dưới gầm ghế của bố tôi."
                }
        },
        {
                "q_num": 76,
                "type": "dien_tao_cau",
                "question": "Câu 76: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Heute Abend bleiben wir ___ Hause, aber morgen gehen wir zu ___ zur Bibliothek.'",
                "options_json": null,
                "correct_answer": "zu / Fuß",
                "explanation": "Cụm cố định \"ở nhà\" là zu Hause và \"đi bộ\" là zu Fuß.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zu / Fuß",
                                "zu/Fuß",
                                "zu / Fuss",
                                "zu/Fuss"
                        ],
                        "translation": "„Tối nay chúng tôi ở nhà, nhưng ngày mai chúng tôi đi bộ đến thư viện."
                }
        },
        {
                "q_num": 77,
                "type": "dien_tao_cau",
                "question": "Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Das schöne Bild hängt an ___ Wand über ___ Sofa.'",
                "options_json": null,
                "correct_answer": "der / dem",
                "explanation": "die Wand (giống cái) ở Dativ là an der Wand; das Sofa (giống trung) ở Dativ là über dem Sofa.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der / dem",
                                "der/dem"
                        ],
                        "translation": "„Bức tranh đẹp treo trên tường phía trên ghế sofa."
                }
        },
        {
                "q_num": 78,
                "type": "nghe_dien",
                "question": "Câu 78 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Meine Kollegin fährt jeden Tag mit der ___ ins Büro.'",
                "options_json": null,
                "correct_answer": "Straßenbahn",
                "explanation": "Danh từ giống cái die Straßenbahn (tàu điện mặt đất) sau giới từ mit là mit der Straßenbahn.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Meine Kollegin fährt jeden Tag mit der Straßenbahn ins Büro.",
                        "display_sentence": "Meine Kollegin fährt jeden Tag mit der ___ ins Büro.",
                        "accepted_answers": [
                                "Straßenbahn",
                                "Strassenbahn"
                        ],
                        "translation": "Nữ đồng nghiệp của tôi mỗi ngày đều đi bằng tàu điện mặt đất đến văn phòng."
                }
        },
        {
                "q_num": 79,
                "type": "nghe_dien",
                "question": "Câu 79 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Die Rezeption befindet sich im ___ neben dem Eingang.'",
                "options_json": null,
                "correct_answer": "Erdgeschoss",
                "explanation": "Danh từ das Erdgeschoss có nghĩa là tầng trệt (im Erdgeschoss).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Die Rezeption befindet sich im Erdgeschoss neben dem Eingang.",
                        "display_sentence": "Die Rezeption befindet sich im ___ neben dem Eingang.",
                        "accepted_answers": [
                                "Erdgeschoss"
                        ],
                        "translation": "Quầy lễ tân nằm ở tầng trệt bên cạnh lối vào."
                }
        },
        {
                "q_num": 80,
                "type": "nghe_dien",
                "question": "Câu 80 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Das Büro von Herrn Müller liegt im ___ Stock.'",
                "options_json": null,
                "correct_answer": "dritten",
                "explanation": "Số thứ tự 3. ở Cách 3 (Dativ) sau giới từ im đọc và viết là dritten.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Das Büro von Herrn Müller liegt im dritten Stock.",
                        "display_sentence": "Das Büro von Herrn Müller liegt im ___ Stock.",
                        "accepted_answers": [
                                "dritten",
                                "3."
                        ],
                        "translation": "Văn phòng của ông Müller nằm ở tầng ba."
                }
        },
        {
                "q_num": 81,
                "type": "nghe_dien",
                "question": "Câu 81 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Der Drucker steht auf dem Schreibtisch ___ dem Computer und dem Telefon.'",
                "options_json": null,
                "correct_answer": "zwischen",
                "explanation": "Giới từ zwischen có nghĩa là ở giữa hai vật.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der Drucker steht auf dem Schreibtisch zwischen dem Computer und dem Telefon.",
                        "display_sentence": "Der Drucker steht auf dem Schreibtisch ___ dem Computer und dem Telefon.",
                        "accepted_answers": [
                                "zwischen"
                        ],
                        "translation": "Chiếc máy in đặt trên bàn làm việc ở giữa máy tính và điện thoại bàn."
                }
        },
        {
                "q_num": 82,
                "type": "nghe_dien",
                "question": "Câu 82 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Im Sommer fliegen unsere Eltern mit dem ___ nach Spanien.'",
                "options_json": null,
                "correct_answer": "Flugzeug",
                "explanation": "Danh từ das Flugzeug có nghĩa là máy bay (mit dem Flugzeug).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Im Sommer fliegen unsere Eltern mit dem Flugzeug nach Spanien.",
                        "display_sentence": "Im Sommer fliegen unsere Eltern mit dem ___ nach Spanien.",
                        "accepted_answers": [
                                "Flugzeug"
                        ],
                        "translation": "Vào mùa hè bố mẹ chúng tôi bay bằng máy bay sang Tây Ban Nha."
                }
        },
        {
                "q_num": 83,
                "type": "nghe_dien",
                "question": "Câu 83 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Mein Bruder hat am ___ August Geburtstag.'",
                "options_json": null,
                "correct_answer": "fünfzehnten",
                "explanation": "Ngày 15 đi sau giới từ am (Dativ) là fünfzehnten.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Mein Bruder hat am fünfzehnten August Geburtstag.",
                        "display_sentence": "Mein Bruder hat am ___ August Geburtstag.",
                        "accepted_answers": [
                                "fünfzehnten",
                                "fuenfzehnten",
                                "15."
                        ],
                        "translation": "Anh trai tôi có sinh nhật vào ngày 15 tháng Tám."
                }
        },
        {
                "q_num": 84,
                "type": "nghe_dien",
                "question": "Câu 84 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Heute ist der ___ Oktober.'",
                "options_json": null,
                "correct_answer": "zwanzigste",
                "explanation": "Sau Heute ist der ... (Nominativ), số thứ tự 20 có đuôi -ste là zwanzigste.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Heute ist der zwanzigste Oktober.",
                        "display_sentence": "Heute ist der ___ Oktober.",
                        "accepted_answers": [
                                "zwanzigste",
                                "20."
                        ],
                        "translation": "Hôm nay là ngày 20 tháng Mười."
                }
        },
        {
                "q_num": 85,
                "type": "nghe_dien",
                "question": "Câu 85 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Am Wochenende fährt Lukas mit seinen ___ in den Zoo.'",
                "options_json": null,
                "correct_answer": "Kindern",
                "explanation": "Danh từ số nhiều die Kinder khi chia ở Cách 3 (Dativ) phải thêm đuôi -n thành Kindern.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Am Wochenende fährt Lukas mit seinen Kindern in den Zoo.",
                        "display_sentence": "Am Wochenende fährt Lukas mit seinen ___ in den Zoo.",
                        "accepted_answers": [
                                "Kindern"
                        ],
                        "translation": "Vào cuối tuần Lukas đi sở thú cùng với các con của anh ấy."
                }
        },
        {
                "q_num": 86,
                "type": "nghe_dien",
                "question": "Câu 86 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Der große Parkplatz liegt direkt ___ dem Krankenhaus.'",
                "options_json": null,
                "correct_answer": "hinter",
                "explanation": "Giới từ chỉ vị trí hinter có nghĩa là ở phía sau.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der große Parkplatz liegt direkt hinter dem Krankenhaus.",
                        "display_sentence": "Der große Parkplatz liegt direkt ___ dem Krankenhaus.",
                        "accepted_answers": [
                                "hinter"
                        ],
                        "translation": "Bãi đỗ xe lớn nằm ngay phía sau bệnh viện."
                }
        },
        {
                "q_num": 87,
                "type": "dich_cau_vd",
                "question": "Câu 87: Dịch câu sau sang tiếng Đức: \"Anh trai tôi đi làm mỗi ngày bằng xe buýt.\"",
                "options_json": null,
                "correct_answer": "Mein Bruder fährt jeden Tag mit dem Bus zur Arbeit. / Jeden Tag fährt mein Bruder mit dem Bus zur Arbeit. / Mein Bruder fährt täglich mit dem Bus zur Arbeit. / Mit dem Bus fährt mein Bruder jeden Tag zur Arbeit.",
                "explanation": "Chủ ngữ Mein Bruder chia động từ fahren thành fährt; phương tiện der Bus ở Dativ là mit dem Bus; đi làm là zur Arbeit.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Mein Bruder fährt jeden Tag mit dem Bus zur Arbeit.",
                                "Jeden Tag fährt mein Bruder mit dem Bus zur Arbeit.",
                                "Mein Bruder fährt täglich mit dem Bus zur Arbeit.",
                                "Mit dem Bus fährt mein Bruder jeden Tag zur Arbeit."
                        ],
                        "translation": "Anh trai tôi đi làm mỗi ngày bằng xe buýt."
                }
        },
        {
                "q_num": 88,
                "type": "dich_cau_vd",
                "question": "Câu 88: Dịch câu sau sang tiếng Đức: \"Văn phòng của bà Schneider nằm ở tầng ba bên cạnh thang máy.\"",
                "options_json": null,
                "correct_answer": "Das Büro von Frau Schneider liegt im dritten Stock neben dem Aufzug. / Das Büro von Frau Schneider ist im dritten Stock neben dem Aufzug. / Das Büro von Frau Schneider liegt im 3. Stock neben dem Aufzug. / Das Büro von Frau Schneider ist im 3. Stock neben dem Fahrstuhl.",
                "explanation": "Ở tầng ba là im dritten Stock; bên cạnh thang máy (der Aufzug / der Fahrstuhl) ở Dativ là neben dem Aufzug.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Das Büro von Frau Schneider liegt im dritten Stock neben dem Aufzug.",
                                "Das Büro von Frau Schneider ist im dritten Stock neben dem Aufzug.",
                                "Das Büro von Frau Schneider liegt im 3. Stock neben dem Aufzug.",
                                "Das Büro von Frau Schneider ist im 3. Stock neben dem Fahrstuhl.",
                                "Frau Schneiders Büro liegt im dritten Stock neben dem Aufzug."
                        ],
                        "translation": "Văn phòng của bà Schneider nằm ở tầng ba bên cạnh thang máy."
                }
        },
        {
                "q_num": 89,
                "type": "dich_cau_vd",
                "question": "Câu 89: Dịch câu sau sang tiếng Đức: \"Hôm nay là ngày mùng 8 tháng Ba.\"",
                "options_json": null,
                "correct_answer": "Heute ist der achte März. / Heute ist der 8. März. / Heute ist der achte Dritte.",
                "explanation": "Cấu trúc nói ngày hiện tại với động từ sein dùng Cách 1 (Nominativ): Heute ist der achte März.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Heute ist der achte März.",
                                "Heute ist der 8. März.",
                                "Heute ist der achte Dritte."
                        ],
                        "translation": "Hôm nay là ngày mùng 8 tháng Ba."
                }
        },
        {
                "q_num": 90,
                "type": "dich_cau_vd",
                "question": "Câu 90: Dịch câu sau sang tiếng Đức: \"Em gái tôi có sinh nhật vào ngày 21 tháng Sáu.\"",
                "options_json": null,
                "correct_answer": "Meine Schwester hat am einundzwanzigsten Juni Geburtstag. / Meine Schwester hat am 21. Juni Geburtstag. / Am einundzwanzigsten Juni hat meine Schwester Geburtstag. / Am 21. Juni hat meine Schwester Geburtstag.",
                "explanation": "Sự kiện diễn ra vào ngày nào dùng giới từ am + số thứ tự đuôi -sten (am einundzwanzigsten Juni).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Meine Schwester hat am einundzwanzigsten Juni Geburtstag.",
                                "Meine Schwester hat am 21. Juni Geburtstag.",
                                "Am einundzwanzigsten Juni hat meine Schwester Geburtstag.",
                                "Am 21. Juni hat meine Schwester Geburtstag."
                        ],
                        "translation": "Em gái tôi có sinh nhật vào ngày 21 tháng Sáu."
                }
        },
        {
                "q_num": 91,
                "type": "dich_cau_vd",
                "question": "Câu 91: Dịch câu sau sang tiếng Đức: \"Chiếc máy tính xách tay nằm trên bàn làm việc giữa cái đèn và điện thoại.\"",
                "options_json": null,
                "correct_answer": "Der Laptop liegt auf dem Schreibtisch zwischen der Lampe und dem Telefon. / Der Laptop steht auf dem Schreibtisch zwischen der Lampe und dem Telefon. / Der Laptop ist auf dem Schreibtisch zwischen der Lampe und dem Telefon. / Der Laptop liegt auf dem Schreibtisch zwischen dem Telefon und der Lampe.",
                "explanation": "Trên bàn làm việc (der Schreibtisch) là auf dem Schreibtisch; giữa cái đèn (die Lampe -> der Lampe) và điện thoại (das Telefon -> dem Telefon).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Der Laptop liegt auf dem Schreibtisch zwischen der Lampe und dem Telefon.",
                                "Der Laptop steht auf dem Schreibtisch zwischen der Lampe und dem Telefon.",
                                "Der Laptop ist auf dem Schreibtisch zwischen der Lampe und dem Telefon.",
                                "Der Laptop liegt auf dem Schreibtisch zwischen dem Telefon und der Lampe."
                        ],
                        "translation": "Chiếc máy tính xách tay nằm trên bàn làm việc giữa cái đèn và điện thoại."
                }
        },
        {
                "q_num": 92,
                "type": "dich_cau_vd",
                "question": "Câu 92: Dịch câu sau sang tiếng Đức: \"Chúng tôi có kỳ nghỉ từ ngày mùng 3 đến ngày 15 tháng Tám.\"",
                "options_json": null,
                "correct_answer": "Wir haben vom dritten bis zum fünfzehnten August Urlaub. / Wir haben vom 3. bis zum 15. August Urlaub. / Vom dritten bis zum fünfzehnten August haben wir Urlaub. / Wir haben Urlaub vom dritten bis zum fünfzehnten August.",
                "explanation": "Khoảng từ ngày ... đến ngày ... dùng vom + [-ten] + bis zum + [-ten] (vom dritten bis zum fünfzehnten August).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Wir haben vom dritten bis zum fünfzehnten August Urlaub.",
                                "Wir haben vom 3. bis zum 15. August Urlaub.",
                                "Vom dritten bis zum fünfzehnten August haben wir Urlaub.",
                                "Wir haben Urlaub vom dritten bis zum fünfzehnten August."
                        ],
                        "translation": "Chúng tôi có kỳ nghỉ từ ngày mùng 3 đến ngày 15 tháng Tám."
                }
        },
        {
                "q_num": 93,
                "type": "dich_cau_vd",
                "question": "Câu 93: Dịch câu sau sang tiếng Đức: \"Trường học ở ngay cạnh nhà tôi nên tôi luôn đi bộ.\"",
                "options_json": null,
                "correct_answer": "Die Schule liegt direkt neben meinem Haus, deshalb gehe ich immer zu Fuß. / Die Schule ist neben meinem Haus, also gehe ich immer zu Fuß. / Die Schule ist gleich neben meinem Haus. Ich gehe immer zu Fuß. / Die Schule liegt neben meinem Haus. Ich gehe immer zu Fuß.",
                "explanation": "Bên cạnh nhà tôi (das Haus) ở Dativ là neben meinem Haus; đi bộ là zu Fuß gehen.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Die Schule liegt direkt neben meinem Haus, deshalb gehe ich immer zu Fuß.",
                                "Die Schule ist neben meinem Haus, also gehe ich immer zu Fuß.",
                                "Die Schule ist gleich neben meinem Haus. Ich gehe immer zu Fuß.",
                                "Die Schule liegt neben meinem Haus. Ich gehe immer zu Fuß."
                        ],
                        "translation": "Trường học ở ngay cạnh nhà tôi nên tôi luôn đi bộ."
                }
        },
        {
                "q_num": 94,
                "type": "dich_cau_dv",
                "question": "Câu 94: Dịch câu sau sang tiếng Việt: „Am Wochenende fahren unsere Großeltern mit der Straßenbahn zum Markt.“",
                "options_json": null,
                "correct_answer": "Vào cuối tuần ông bà của chúng tôi đi bằng tàu điện ra chợ / Cuối tuần ông bà chúng tôi đi chợ bằng tàu điện mặt đất / Vào cuối tuần ông bà tôi đi bằng tàu điện mặt đất đến chợ / Cuối tuần ông bà của chúng mình đi tàu điện ra chợ / Cuối tuần ông bà tôi đi tàu điện ra chợ / Cuối tuần ông bà của chúng tôi đi xe điện ra chợ / Vào cuối tuần ông bà của tôi đi xe điện đến chợ",
                "explanation": "unsere Großeltern = ông bà của chúng tôi; mit der Straßenbahn = bằng tàu điện mặt đất / xe điện; zum Markt = ra chợ / đến chợ.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Vào cuối tuần ông bà của chúng tôi đi bằng tàu điện ra chợ",
                                "Cuối tuần ông bà chúng tôi đi chợ bằng tàu điện mặt đất",
                                "Vào cuối tuần ông bà tôi đi bằng tàu điện mặt đất đến chợ",
                                "Cuối tuần ông bà của chúng mình đi tàu điện ra chợ",
                                "Cuối tuần ông bà tôi đi tàu điện ra chợ",
                                "Cuối tuần ông bà của chúng tôi đi xe điện ra chợ",
                                "Vào cuối tuần ông bà của tôi đi xe điện đến chợ",
                                "Cuối tuần ông bà chúng tôi đi xe điện ra chợ"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Am Wochenende fahren unsere Großeltern mit der Straßenbahn zum Markt.“"
                }
        },
        {
                "q_num": 95,
                "type": "dich_cau_dv",
                "question": "Câu 95: Dịch câu sau sang tiếng Việt: „Das Café liegt direkt zwischen der Buchhandlung und dem Kino.“",
                "options_json": null,
                "correct_answer": "Quán cà phê nằm ngay giữa hiệu sách và rạp chiếu phim / Quán cà phê ở ngay giữa tiệm sách và rạp chiếu phim / Quán cà phê nằm ở giữa hiệu sách và rạp phim / Quán cà phê ở giữa hiệu sách và rạp chiếu phim / Tiệm cà phê nằm ở giữa hiệu sách và rạp phim / Quán cafe nằm ngay giữa nhà sách và rạp phim / Quán cà phê nằm giữa tiệm sách và rạp phim",
                "explanation": "zwischen der Buchhandlung und dem Kino = ở giữa hiệu sách và rạp chiếu phim.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Quán cà phê nằm ngay giữa hiệu sách và rạp chiếu phim",
                                "Quán cà phê ở ngay giữa tiệm sách và rạp chiếu phim",
                                "Quán cà phê nằm ở giữa hiệu sách và rạp phim",
                                "Quán cà phê ở giữa hiệu sách và rạp chiếu phim",
                                "Tiệm cà phê nằm ở giữa hiệu sách và rạp phim",
                                "Quán cafe nằm ngay giữa nhà sách và rạp phim",
                                "Quán cà phê nằm giữa tiệm sách và rạp phim",
                                "Quán cafe ở giữa hiệu sách và rạp phim"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Das Café liegt direkt zwischen der Buchhandlung und dem Kino.“"
                }
        },
        {
                "q_num": 96,
                "type": "dich_cau_dv",
                "question": "Câu 96: Dịch câu sau sang tiếng Việt: „Die Kantine befindet sich im Erdgeschoss und der Konferenzraum ist im siebten Stock.“",
                "options_json": null,
                "correct_answer": "Căn tin ở tầng trệt và phòng họp nằm ở tầng 7 / Nhà ăn nằm ở tầng trệt và phòng họp ở tầng bảy / Căn tin ở tầng trệt còn phòng họp nằm ở tầng 7 / Nhà ăn ở tầng trệt và phòng hội nghị nằm ở tầng bảy / Căn tin nằm ở tầng trệt và phòng họp ở tầng 7 / Căng tin ở tầng trệt và phòng họp ở tầng 7 / Nhà ăn ở tầng trệt và phòng họp nằm ở tầng 7",
                "explanation": "die Kantine = nhà ăn / căng tin / căn tin; im Erdgeschoss = ở tầng trệt; im siebten Stock = ở tầng bảy / tầng 7.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Căn tin ở tầng trệt và phòng họp nằm ở tầng 7",
                                "Nhà ăn nằm ở tầng trệt và phòng họp ở tầng bảy",
                                "Căn tin ở tầng trệt còn phòng họp nằm ở tầng 7",
                                "Nhà ăn ở tầng trệt và phòng hội nghị nằm ở tầng bảy",
                                "Căn tin nằm ở tầng trệt và phòng họp ở tầng 7",
                                "Căng tin ở tầng trệt và phòng họp ở tầng 7",
                                "Nhà ăn ở tầng trệt và phòng họp nằm ở tầng 7",
                                "Căn tin ở tầng trệt và phòng họp ở tầng 7"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Die Kantine befindet sich im Erdgeschoss und der Konferenzraum ist im siebten Stock.“"
                }
        },
        {
                "q_num": 97,
                "type": "dich_cau_dv",
                "question": "Câu 97: Dịch câu sau sang tiếng Việt: „Meine Tochter ist am dritten Oktober zweitausendzwei in Berlin geboren.“",
                "options_json": null,
                "correct_answer": "Con gái tôi sinh vào ngày 3 tháng 10 năm 2002 ở Berlin / Con gái tôi sinh vào ngày mùng 3 tháng 10 năm 2002 tại Berlin / Con gái của tôi sinh ngày 3 tháng 10 năm 2002 ở Berlin / Con gái tôi sinh ngày 3/10/2002 ở Berlin / Con gái tôi sinh ngày 3 tháng 10 năm 2002 ở Berlin / Con gái tôi sinh vào ngày 3 tháng 10 năm 2002 tại Berlin / Con gái tôi sinh vào ngày ba tháng Mười năm 2002 tại Berlin / Con gái tôi sinh ngày 3 tháng 10 năm 2002 tại Berlin",
                "explanation": "am dritten Oktober zweitausendzwei = vào ngày 3 tháng 10 năm 2002; ist ... geboren = sinh ra.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Con gái tôi sinh vào ngày 3 tháng 10 năm 2002 ở Berlin",
                                "Con gái tôi sinh vào ngày mùng 3 tháng 10 năm 2002 tại Berlin",
                                "Con gái của tôi sinh ngày 3 tháng 10 năm 2002 ở Berlin",
                                "Con gái tôi sinh ngày 3/10/2002 ở Berlin",
                                "Con gái tôi sinh ngày 3 tháng 10 năm 2002 ở Berlin",
                                "Con gái tôi sinh vào ngày 3 tháng 10 năm 2002 tại Berlin",
                                "Con gái tôi sinh vào ngày ba tháng Mười năm 2002 tại Berlin",
                                "Con gái tôi sinh ngày 3 tháng 10 năm 2002 tại Berlin",
                                "con gái tôi sinh vào ngày 3 tháng 10 năm 2002 ở berlin"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Meine Tochter ist am dritten Oktober zweitausendzwei in Berlin geboren.“"
                }
        },
        {
                "q_num": 98,
                "type": "dich_cau_dv",
                "question": "Câu 98: Dịch câu sau sang tiếng Việt: „Nach der Arbeit gehe ich nicht sofort nach Hause, sondern ich treffe mich mit meinen Freunden im Park.“",
                "options_json": null,
                "correct_answer": "Sau giờ làm việc tôi không về nhà ngay mà tôi gặp gỡ những người bạn của tôi ở công viên / Sau giờ làm việc tôi không đi về nhà ngay mà tôi gặp gỡ những người bạn của tôi ở trong công viên / Sau khi tan làm tôi không về nhà ngay mà hẹn gặp bạn bè của mình trong công viên / Sau giờ làm tôi không về nhà liền mà gặp những người bạn của tôi ở công viên / Sau giờ làm việc tôi không về nhà ngay mà gặp bạn bè ở công viên / Sau giờ làm tôi không về nhà ngay mà gặp gỡ bạn bè của tôi ở công viên",
                "explanation": "Nach der Arbeit = sau giờ làm việc / sau giờ làm; nach Hause gehen = đi về nhà; mit meinen Freunden = với những người bạn của tôi (Dativ số nhiều); im Park = ở công viên / trong công viên.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Sau giờ làm việc tôi không về nhà ngay mà tôi gặp gỡ những người bạn của tôi ở công viên",
                                "Sau giờ làm việc tôi không đi về nhà ngay mà tôi gặp gỡ những người bạn của tôi ở trong công viên",
                                "Sau khi tan làm tôi không về nhà ngay mà hẹn gặp bạn bè của mình trong công viên",
                                "Sau giờ làm tôi không về nhà liền mà gặp những người bạn của tôi ở công viên",
                                "Sau giờ làm việc tôi không về nhà ngay mà gặp bạn bè ở công viên",
                                "Sau giờ làm tôi không về nhà ngay mà gặp gỡ bạn bè của tôi ở công viên",
                                "sau giờ làm việc tôi không về nhà ngay mà tôi gặp gỡ những người bạn của tôi ở công viên"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Nach der Arbeit gehe ich không sofort nach Hause, sondern ich treffe mich mit meinen Freunden im Park.“"
                }
        },
        {
                "q_num": 99,
                "type": "dich_cau_dv",
                "question": "Câu 99: Dịch câu sau sang tiếng Việt: „Das große Familienfoto hängt an der Wand über dem Sofa.“",
                "options_json": null,
                "correct_answer": "Bức ảnh gia đình lớn treo trên tường phía trên ghế sofa / Tấm ảnh gia đình lớn được treo ở trên tường phía trên ghế sô pha / Bức ảnh gia đình to treo trên bức tường phía trên ghế sofa / Bức ảnh gia đình lớn treo ở trên tường phía trên ghế sofa / Tấm hình gia đình lớn treo trên tường phía trên ghế sofa / Bức ảnh gia đình to treo trên tường phía trên ghế sofa",
                "explanation": "an der Wand = trên tường (tiếp xúc mặt đứng); über dem Sofa = phía trên ghế sofa (không tiếp xúc).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Bức ảnh gia đình lớn treo trên tường phía trên ghế sofa",
                                "Tấm ảnh gia đình lớn được treo ở trên tường phía trên ghế sô pha",
                                "Bức ảnh gia đình to treo trên bức tường phía trên ghế sofa",
                                "Bức ảnh gia đình lớn treo ở trên tường phía trên ghế sofa",
                                "Tấm hình gia đình lớn treo trên tường phía trên ghế sofa",
                                "Bức ảnh gia đình to treo trên tường phía trên ghế sofa"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Das große Familienfoto hängt an der Wand über dem Sofa.“"
                }
        },
        {
                "q_num": 100,
                "type": "dich_cau_dv",
                "question": "Câu 100: Dịch câu sau sang tiếng Việt: „Vom ersten bis zum vierzehnten Juli bleibt unsere Arztpraxis geschlossen.“",
                "options_json": null,
                "correct_answer": "Từ ngày 1 đến ngày 14 tháng 7 phòng khám của chúng tôi đóng cửa / Từ ngày mùng 1 đến ngày 14 tháng 7 phòng khám bác sĩ của chúng tôi đóng cửa / Từ ngày 1 đến ngày 14 tháng Bảy phòng khám của chúng tôi đóng cửa / Từ ngày 1 đến ngày 14 tháng 7 phòng khám chúng tôi đóng cửa / Từ 1/7 đến 14/7 phòng mạch của chúng tôi nghỉ đóng cửa / Từ ngày 1 đến 14 tháng 7 phòng khám của chúng tôi đóng cửa / Từ ngày mùng 1 đến ngày 14 tháng 7 phòng khám của chúng tôi đóng cửa",
                "explanation": "Vom ersten bis zum vierzehnten Juli = từ ngày 1 đến ngày 14 tháng 7; die Arztpraxis = phòng khám bác sĩ / phòng khám.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Từ ngày 1 đến ngày 14 tháng 7 phòng khám của chúng tôi đóng cửa",
                                "Từ ngày mùng 1 đến ngày 14 tháng 7 phòng khám bác sĩ của chúng tôi đóng cửa",
                                "Từ ngày 1 đến ngày 14 tháng Bảy phòng khám của chúng tôi đóng cửa",
                                "Từ ngày 1 đến ngày 14 tháng 7 phòng khám chúng tôi đóng cửa",
                                "Từ 1/7 đến 14/7 phòng mạch của chúng tôi nghỉ đóng cửa",
                                "Từ ngày 1 đến 14 tháng 7 phòng khám của chúng tôi đóng cửa",
                                "Từ ngày mùng 1 đến ngày 14 tháng 7 phòng khám của chúng tôi đóng cửa"
                        ],
                        "translation": "Dịch câu sau sang tiếng Việt: „Vom ersten bis zum vierzehnten Juli bleibt unsere Arztpraxis geschlossen.“"
                }
        }
]

    import random
    exercises = []
    for ex in exercises_raw:
        q_num = ex["q_num"]
        ex_type = ex["type"]
        question = ex["question"]
        opts = ex["options_json"]
        corr = ex["correct_answer"]
        exp = ex["explanation"]
        pts = ex["exp_reward"]
        extra = ex["extra_data"]

        if ex_type == "trac_nghiem" and opts:
            try:
                opt_list = json.loads(opts)
                if isinstance(opt_list, list) and len(opt_list) > 1:
                    random.shuffle(opt_list)
                    opts = json.dumps(opt_list, ensure_ascii=False)
            except Exception:
                pass

        extra_json = json.dumps(extra, ensure_ascii=False) if extra else None
        exercises.append((
            lesson_id, ex_type, question, opts, corr, exp, pts, extra_json
        ))

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công Bài 6: 'Dativ - Giới từ trong Dativ - Phương tiện giao thông - Số thứ tự - Ngày tháng năm' với đầy đủ 6 Học phần Lý thuyết + 45 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_6()
