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

def seed_lesson_8():
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

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 8%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 22

    # Xóa dữ liệu cũ của Bài 8 nếu có để cập nhật sạch sẽ (Bảo toàn tuyệt đối Bài 1 -> Bài 7)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    lesson_title = 'Bài 8: "Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu (Thành phố Berlin - Định hướng Bản đồ & Modalverben)"'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 8 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-sky-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/20 border border-sky-400/30 text-sky-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Stadt • Wegbeschreibung • Modalverben (Bài 8)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 120 phút • ⚡ 1800+ EXP • 🎯 100 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Bài 8: Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu (Thành phố Berlin - Định hướng Bản đồ & Modalverben)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Khám phá toàn diện hệ thống từ vựng <b>Địa điểm trong Thành phố (In der Stadt)</b> và <b>14 Danh lam thắng cảnh nổi tiếng tại Thủ đô Berlin</b>; làm chủ nghệ thuật <b>Hỏi đường (Nach dem Weg fragen)</b> và <b>Chỉ đường (Den Weg beschreiben)</b> với hệ thống Sơ đồ Không gian và Bản đồ Lưới đường phố SVG trực quan (<i>an...vorbei, durch, über, entlang, bis zur...</i>); phân biệt sự khác biệt bản chất giữa đi vào trong (<i>in + Akkusativ</i>) vs. đi đến địa điểm (<i>zu + Dativ</i>); và chinh phục trọn vẹn ma trận 4 <b>Động từ khuyết thiếu (möchten, können, müssen, wollen)</b> kèm chuỗi liên từ chỉ trình tự thời gian (<i>Zuerst -> Dann -> Danach -> Anschließend</i>).
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: TỪ VỰNG ĐỊA ĐIỂM TRONG THÀNH PHỐ & DANH LAM THẮNG CẢNH BERLIN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-sky-100 text-sky-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Địa Điểm Trong Thành Phố (In der Stadt) & 14 Danh Lam Thắng Cảnh Berlin</h4>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>💡</span> Mẹo Ngữ pháp & Từ vựng Cực Quan Trọng Cần Nhớ:</p>
                <ol class="list-decimal pl-5 space-y-1 text-slate-700">
                    <li><b>Danh từ ghép (Komposita):</b> Giống luôn do từ đứng cuối (Grundwort) quyết định: <i>der Flughafen</i> (vì <i>der Hafen</i>), <i>der Supermarkt</i> (vì <i>der Markt</i>), <i>das Stadttor</i> & <i>das Brandenburger Tor</i> (vì <i>das Tor</i>), <i>das Krankenhaus</i> (vì <i>das Haus</i>), <i>das Einkaufszentrum</i> (vì <i>das Zentrum</i>).</li>
                    <li><b>Phân biệt 2 nghĩa của 'die Bank':</b> Ngân hàng tiền số nhiều là <b>die Banken</b>; ghế băng dài công viên số nhiều là <b>die Bänke</b>.</li>
                    <li><b>Danh từ chỉ dùng số ít (nur Singular):</b> <b>die Post</b> (bưu điện/bưu chính) thường chỉ dùng ở số ít. Nếu đếm bưu cục cụ thể dùng <i>das Postamt -> die Postämter</i>.</li>
                </ol>
            </div>

            <!-- Bảng 1: Địa điểm trong thành phố theo 3 giống -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🏙️</span> Bảng 1: Địa Điểm Thành Phố Phân Theo 3 Giống (der / die / das)
                </h5>
                <div class="overflow-x-auto rounded-2xl border border-slate-200">
                    <table class="w-full text-left text-xs sm:text-sm">
                        <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                            <tr>
                                <th class="p-3 text-blue-700">Giống Đực (der — Maskulinum)</th>
                                <th class="p-3 text-rose-700">Giống Cái (die — Femininum)</th>
                                <th class="p-3 text-emerald-700">Giống Trung (das — Neutrum)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="p-3">
                                    • <b>der Bahnhof</b> (Pl: <i>die Bahnhöfe</i>): nhà ga<br>
                                    • <b>der Hauptbahnhof</b>: ga trung tâm<br>
                                    • <b>der Hafen</b> (Pl: <i>die Häfen</i>): cảng biển<br>
                                    • <b>der Flughafen</b> (Pl: <i>die Flughäfen</i>): sân bay<br>
                                    • <b>der Markt</b> (Pl: <i>die Märkte</i>): chợ<br>
                                    • <b>der Supermarkt</b> (Pl: <i>die Supermärkte</i>): siêu thị<br>
                                    • <b>der Platz</b> (Pl: <i>die Plätze</i>): quảng trường<br>
                                    • <b>der Park</b> (Pl: <i>die Parks</i>): công viên<br>
                                    • <b>der Zoo</b> (Pl: <i>die Zoos</i>): vườn bách thú<br>
                                    • <b>der Turm</b> (Pl: <i>die Türme</i>): tòa tháp<br>
                                    • <b>der Dom</b> (Pl: <i>die Dome</i>): nhà thờ lớn
                                </td>
                                <td class="p-3">
                                    • <b>die Stadt</b> (Pl: <i>die Städte</i>): thành phố<br>
                                    • <b>die Kirche</b> (Pl: <i>die Kirchen</i>): nhà thờ<br>
                                    • <b>die Schule</b> (Pl: <i>die Schulen</i>): trường học<br>
                                    • <b>die Brücke</b> (Pl: <i>die Brücken</i>): cây cầu<br>
                                    • <b>die Bank</b> (Pl: <i>die Banken / Bänke</i>): ngân hàng / ghế băng<br>
                                    • <b>die Post</b> (nur Sg.): bưu điện<br>
                                    • <b>die Straße</b> (Pl: <i>die Straßen</i>): con đường, phố<br>
                                    • <b>die Ampel</b> (Pl: <i>die Ampeln</i>): đèn giao thông<br>
                                    • <b>die Kreuzung</b> (Pl: <i>die Kreuzungen</i>): ngã tư<br>
                                    • <b>die Disko</b> (Pl: <i>die Diskos</i>): vũ trường, bar
                                </td>
                                <td class="p-3">
                                    • <b>das Schloss</b> (Pl: <i>die Schlösser</i>): lâu đài<br>
                                    • <b>das Stadttor</b> (Pl: <i>die Stadttore</i>): cổng thành<br>
                                    • <b>das Kino</b> (Pl: <i>die Kinos</i>): rạp chiếu phim<br>
                                    • <b>das Krankenhaus</b> (Pl: <i>die Krankenhäuser</i>): bệnh viện<br>
                                    • <b>das Einkaufszentrum</b> (Pl: <i>die Einkaufszentren</i>): trung tâm thương mại<br>
                                    • <b>das Hotel</b> (Pl: <i>die Hotels</i>): khách sạn<br>
                                    • <b>das Museum</b> (Pl: <i>die Museen</i>): bảo tàng<br>
                                    • <b>das Rathaus</b> (Pl: <i>die Rathäuser</i>): tòa thị chính<br>
                                    • <b>das Theater</b> (Pl: <i>die Theater</i>): nhà hát kịch
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng 2: 14 Danh lam thắng cảnh Berlin -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🏛️</span> Bảng 2: 14 Danh Lam Thắng Cảnh Nổi Tiếng Tại Thủ Đô Berlin
                </h5>
                <div class="overflow-x-auto rounded-2xl border border-slate-200">
                    <table class="w-full text-left text-xs sm:text-sm">
                        <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                            <tr>
                                <th class="p-3 text-blue-700">Giống Đực (der)</th>
                                <th class="p-3 text-rose-700">Giống Cái (die)</th>
                                <th class="p-3 text-emerald-700">Giống Trung (das)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="p-3">
                                    1. <b>der Reichstag</b>: Tòa nhà Quốc hội Đức (<i>der Tag</i>)<br>
                                    2. <b>der Alexanderplatz</b>: Quảng trường Alex (<i>der Platz</i>)<br>
                                    3. <b>der Potsdamer Platz</b>: Quảng trường Potsdam<br>
                                    4. <b>der Berliner Dom</b>: Nhà thờ lớn Berlin (<i>der Dom</i>)<br>
                                    5. <b>der Fernsehturm</b>: Tháp truyền hình (<i>der Turm</i>)
                                </td>
                                <td class="p-3">
                                    6. <b>die Humboldt-Universität</b>: ĐH Humboldt (<i>-tät</i>)<br>
                                    7. <b>die Staatsoper</b>: Nhà hát Opera Quốc gia (<i>die Oper</i>)<br>
                                    8. <b>die Friedrichstraße</b>: Phố Friedrich (<i>die Straße</i>)<br>
                                    9. <b>die Museumsinsel</b>: Đảo Bảo tàng (<i>die Insel</i>)<br>
                                    10. <b>die Alte Nationalgalerie</b>: Triển lãm QG Cũ (<i>-ie</i>)
                                </td>
                                <td class="p-3">
                                    11. <b>das Bundeskanzleramt</b>: Phủ Thủ tướng (<i>das Amt</i>)<br>
                                    12. <b>das Brandenburger Tor</b>: Cổng Brandenburg (<i>das Tor</i>)<br>
                                    13. <b>das Schloss Bellevue</b>: Cung điện Bellevue (<i>das Schloss</i>)<br>
                                    14. <b>das Sony Center</b>: Trung tâm Sony (<i>das Center</i>)
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: NGHỆ THUẬT HỎI ĐƯỜNG & CHỈ ĐƯỜNG KÈM SƠ ĐỒ SVG & BẢN ĐỒ TƯƠNG TÁC -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Nghệ Thuật Hỏi Đường & Chỉ Đường Kèm Sơ Đồ & Bản Đồ Lưới Trực Quan</h4>
            </div>

            <!-- 4 Mẫu câu hỏi đường -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800">2.1. Bốn Mẫu Câu Hỏi Đường Lịch Sự (Nach dem Weg fragen):</h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs sm:text-sm">
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">1. Entschuldigung, ich suche + [Akkusativ].</div>
                        <p class="text-slate-600">Động từ <i>suchen</i> luôn đòi hỏi Cách 4: <i>den Bahnhof / die Post / das Kino</i>.</p>
                        <p class="text-slate-500 italic">„Entschuldigung, ich suche das Kino.“ <span class="not-italic text-slate-500 text-xs">(Xin lỗi, tôi đang tìm rạp chiếu phim.)</span></p>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">2. Entschuldigung, wo ist + [Nominativ]?</div>
                        <p class="text-slate-600">Động từ <i>sein (ist)</i> luôn đi với Cách 1: <i>der Bahnhof / eine Bank / das Kino</i>.</p>
                        <p class="text-slate-500 italic">„Entschuldigung, wo ist hier eine Bank?“ <span class="not-italic text-slate-500 text-xs">(Xin lỗi, ở đây có ngân hàng nào không?)</span></p>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">3. Entschuldigung, wo geht es + [Hướng đích]?</div>
                        <p class="text-slate-600">Dùng <i>zum / zur</i> hoặc <i>ins / in die</i>: Đi lối nào để tới...</p>
                        <p class="text-slate-500 italic">„Entschuldigung, wo geht es zum Bahnhof?“ <span class="not-italic text-slate-500 text-xs">(Xin lỗi, đi lối nào để tới nhà ga?)</span></p>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">4. Entschuldigung, wie komme ich + [Hướng đích]?</div>
                        <p class="text-slate-600">Mẫu câu hỏi đường phổ biến nhất: Làm thế nào tôi đến được...</p>
                        <p class="text-slate-500 italic">„Entschuldigung, wie komme ich zur Post?“ <span class="not-italic text-slate-500 text-xs">(Xin lỗi, làm thế nào tôi đến được bưu điện?)</span></p>
                    </div>
                </div>
            </div>

            <!-- BỘ 4 SƠ ĐỒ KHÔNG GIAN SVG -->
            <div class="space-y-3 pt-2">
                <h5 class="text-sm font-bold text-slate-800">2.2. Bộ 4 Sơ Đồ Giới Từ Không Gian Trực Quan (SVG Spatial Diagrams):</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-blue-100 text-blue-800">SƠ ĐỒ 1: an + DATIV + vorbei</span>
                        <div id="svg-diag-vorbei">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><rect x="25" y="0" width="90" height="180" fill="#334155"/><line x1="70" y1="5" x2="70" y2="175" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/><rect x="115" y="0" width="12" height="180" fill="#cbd5e1"/><rect x="135" y="8" width="155" height="25" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/><text x="212.5" y="25" font-size="10.5" font-weight="black" fill="#1d4ed8" text-anchor="middle">an + DATIV + vorbei</text><rect x="135" y="37" width="155" height="102" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="2"/><rect x="145" y="46" width="22" height="22" fill="#38bdf8" rx="3"/><rect x="175" y="46" width="22" height="22" fill="#38bdf8" rx="3"/><rect x="205" y="46" width="22" height="22" fill="#38bdf8" rx="3"/><rect x="235" y="46" width="22" height="22" fill="#38bdf8" rx="3"/><text x="212.5" y="85" font-size="11" font-weight="black" fill="#1e293b" text-anchor="middle">UNIVERSITÄT</text><text x="212.5" y="98" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="middle">(die / Femininum)</text><rect x="195" y="103" width="35" height="36" fill="#475569" rx="3"/><path d="M70 165 L70 35" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/><polygon points="70,18 60,38 80,38" fill="#1d4ed8"/><circle cx="70" cy="165" r="5" fill="#1d4ed8"/><rect x="15" y="147" width="220" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="125" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 an der Universität vorbei</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi ngang qua bên cạnh tòa nhà mà không rẽ vào trong: <i>an der Universität vorbei / am Dom vorbei</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-rose-100 text-rose-800">SƠ ĐỒ 2: durch + AKKUSATIV</span>
                        <div id="svg-diag-durch">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><rect x="95" y="0" width="110" height="180" fill="#334155"/><rect x="20" y="48" width="260" height="85" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="2.5"/><path d="M105 133 L105 78 A 45 45 0 0 1 195 78 L195 133 Z" fill="#334155" stroke="#1e293b" stroke-width="2"/><rect x="35" y="58" width="28" height="75" fill="#cbd5e1" stroke="#64748b"/><rect x="237" y="58" width="28" height="75" fill="#cbd5e1" stroke="#64748b"/><polygon points="150,26 80,48 220,48" fill="#be123c"/><circle cx="150" cy="18" r="5" fill="#fbbf24"/><rect x="10" y="8" width="126" height="26" rx="6" fill="#fdf2f8" stroke="#f472b6" stroke-width="1.5"/><text x="73" y="25" font-size="10.5" font-weight="black" fill="#be185d" text-anchor="middle">durch + AKKUSATIV</text><rect x="164" y="8" width="126" height="26" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/><text x="227" y="25" font-size="9.5" font-weight="black" fill="#1e293b" text-anchor="middle">Brandenburger Tor (das)</text><path d="M150 168 L150 25" fill="none" stroke="#e11d48" stroke-width="6" stroke-linecap="round"/><polygon points="150,10 140,28 160,28" fill="#be123c"/><circle cx="150" cy="168" r="5" fill="#be123c"/><rect x="45" y="147" width="210" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="150" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 durch das Tor (xuyên qua lòng cổng)</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi xuyên qua chính giữa lòng cổng vòm hoặc công viên: <i>durch das Tor / durch den Park</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800">SƠ ĐỒ 3: über + AKKUSATIV</span>
                        <div id="svg-diag-ueber">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><rect x="0" y="52" width="300" height="74" fill="#38bdf8"/><path d="M0 68 Q 75 58 150 68 T 300 68" fill="none" stroke="#0284c7" stroke-width="3"/><path d="M0 108 Q 75 98 150 108 T 300 108" fill="none" stroke="#0284c7" stroke-width="3"/><text x="48" y="116" font-size="8.5" font-weight="extrabold" fill="#0284c7" text-anchor="middle">Fluss Spree</text><rect x="100" y="15" width="100" height="150" rx="6" fill="#334155" stroke="#475569" stroke-width="2"/><rect x="94" y="15" width="6" height="150" fill="#94a3b8"/><rect x="200" y="15" width="6" height="150" fill="#94a3b8"/><line x1="150" y1="20" x2="150" y2="160" stroke="#ffffff" stroke-width="2" stroke-dasharray="8 6"/><rect x="8" y="10" width="82" height="26" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/><text x="49" y="27" font-size="9" font-weight="black" fill="#15803d" text-anchor="middle">über + AKKUSATIV</text><rect x="208" y="10" width="84" height="26" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/><text x="250" y="27" font-size="8.5" font-weight="extrabold" fill="#1e293b" text-anchor="middle">die Schlossbrücke</text><path d="M150 168 L150 25" fill="none" stroke="#16a34a" stroke-width="6" stroke-linecap="round"/><polygon points="150,10 140,30 160,30" fill="#15803d"/><circle cx="150" cy="168" r="5" fill="#15803d"/><rect x="45" y="147" width="210" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="150" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 über die Brücke (băng qua mặt cầu)</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi vượt qua trên mặt cầu, mặt quảng trường: <i>über die Brücke / über den Platz</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-amber-100 text-amber-800">SƠ ĐỒ 4: AKKUSATIV + entlang</span>
                        <div id="svg-diag-entlang">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><path d="M60 180 C 100 110, 200 110, 240 0 L 290 0 C 250 110, 150 110, 110 180 Z" fill="#334155"/><path d="M85 180 C 125 110, 225 110, 265 0" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/><rect x="10" y="10" width="145" height="25" rx="6" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/><text x="82.5" y="26.5" font-size="10.5" font-weight="black" fill="#a16207" text-anchor="middle">AKKUSATIV + entlang</text><rect x="10" y="40" width="125" height="24" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/><text x="72.5" y="56" font-size="9" font-weight="extrabold" fill="#1e293b" text-anchor="middle">die Friedrichstraße</text><path d="M85 168 C 125 105, 225 105, 265 20" fill="none" stroke="#ca8a04" stroke-width="6" stroke-linecap="round"/><polygon points="268,8 253,22 271,28" fill="#a16207"/><circle cx="85" cy="168" r="5" fill="#a16207"/><rect x="30" y="147" width="240" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="150" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 die Straße entlang (dọc theo con đường)</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi dọc theo chiều dài con đường (từ <i>entlang</i> đứng SAU danh từ): <i>die Straße entlang</i>.</p>
                    </div>
                </div>
            </div>

            <!-- ĐỐI CHIẾU DURCH DAS TOR VS ÜBER DIE BRÜCKE -->
            <div class="space-y-3 pt-2">
                <h5 class="text-sm font-bold text-slate-800">2.3. Đối Chiếu: Đi Xuyên Qua (durch) vs. Đi Băng Qua Trên Mặt (über):</h5>
                <div id="svg-spatial-contrast"></div>
            </div>

            <!-- LƯỚI 12 THẺ HÌNH CHỈ ĐƯỜNG a -> l -->
            <div class="space-y-3 pt-2">
                <h5 class="text-sm font-bold text-slate-800 flex items-center justify-between">
                    <span>🧭 2.4. Bộ 12 Thẻ Hình Minh Họa Chỉ Đường (Visual Direction Cards a &rarr; l):</span>
                    <span class="text-xs text-slate-500 font-normal">Bấm 🔊 để nghe khẩu lệnh tiếng Đức</span>
                </h5>
                <div id="b8-direction-cards-grid"></div>
            </div>

            <!-- BẢN ĐỒ LƯỚI ĐƯỜNG PHỐ TƯƠNG TÁC -->
            <div class="space-y-3 pt-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                        <span>🗺️</span> Bản Đồ Lưới Đường Phố Tương Tác Đa Lộ Trình (Berlin City Map)
                    </h5>
                    <div class="flex items-center gap-2">
                        <button id="b8-btn-route-1" onclick="setInteractiveMapRoute('route1')" class="px-3.5 py-1.5 rounded-xl bg-blue-600 text-white font-bold text-xs shadow-sm cursor-pointer">
                            🔵 Lộ trình 1 (Qua Ngân hàng)
                        </button>
                        <button id="b8-btn-route-2" onclick="setInteractiveMapRoute('route2')" class="px-3.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs cursor-pointer">
                            🟢 Lộ trình 2 (Qua Ngã tư 2)
                        </button>
                        <button id="b8-btn-route-reset" onclick="setInteractiveMapRoute(null)" class="px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs cursor-pointer">
                            🔄 Bản đồ trống
                        </button>
                    </div>
                </div>

                <div id="b8-interactive-city-map-container" class="rounded-3xl overflow-hidden shadow-sm">
                    <script>
                        document.addEventListener("DOMContentLoaded", function() {
                            if (typeof getCityGridMapSvg === 'function') {
                                document.getElementById('b8-interactive-city-map-container').innerHTML = getCityGridMapSvg('route1');
                            }
                        });
                    </script>
                </div>

                <div id="b8-route-description-wrap">
                    <div class="p-4 rounded-2xl bg-blue-50 border border-blue-200 space-y-2 text-xs sm:text-sm text-blue-950">
                        <div class="flex items-center justify-between">
                            <span class="font-extrabold text-blue-800">🔵 Lộ trình 1: Đi qua Ngân hàng tới Bưu điện</span>
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur nächsten Kreuzung und dort links. Danach gehen Sie rechts und die Straße Unter den Linden entlang bis zur Ampel. Die Post sehen Sie dann direkt vor sich.', 1.0)" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus. <b>Dann</b> gehen Sie die erste Straße rechts, <b>an der Bank vorbei</b>. <b>Dann</b> gehen Sie bis zur nächsten Kreuzung und dort links. <b>Danach</b> gehen Sie rechts und die Straße Unter den Linden entlang <b>bis zur Ampel</b>. <b>Die Post</b> sehen Sie dann <b>direkt vor sich</b>.“</p>
                        <p class="text-xs text-blue-800 font-medium"><b>Dịch nghĩa:</b> Đầu tiên Ngài đi thẳng. Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. Sau đó Ngài đi đến ngã tư tiếp theo và rẽ trái ở đó. Tiếp theo Ngài rẽ phải và đi dọc theo đường Unter den Linden cho đến đèn giao thông. Ngài sẽ thấy bưu điện ngay phía trước.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: PHÂN BIỆT ZU + DATIV VS. IN + AKKUSATIV -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Phân Biệt Cấu Trúc Đến Địa Điểm: zu + Dativ (zum/zur) vs. in + Akkusativ (in den/in die/ins)</h4>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3 w-1/4">Tiêu Chí Phân Biệt</th>
                            <th class="p-3 text-indigo-700 w-3/8">1. zu + CÁCH 3 (DATIV) • zum / zur</th>
                            <th class="p-3 text-rose-700 w-3/8">2. in + CÁCH 4 (AKKUSATIV) • in den / in die / ins</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <tr>
                            <td class="p-3 font-bold bg-slate-50/50">Ý nghĩa không gian</td>
                            <td class="p-3">Nhấn mạnh <b>hướng di chuyển tới khu vực/địa điểm đó</b> (đứng trước cổng chụp ảnh, đến làm việc mà không nhấn mạnh việc bước vào bên trong lòng kiến trúc kín).</td>
                            <td class="p-3">Nhấn mạnh hành động <b>bước hẳn vào BÊN TRONG lòng tòa nhà khép kín</b> (vào nghe nhạc, xem phim, nhảy múa, tham quan triển lãm).</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold bg-slate-50/50">Biến đổi mạo từ</td>
                            <td class="p-3">
                                • der -> <b>zum</b> (<i>zum Bahnhof, zum Reichstag</i>)<br>
                                • das -> <b>zum</b> (<i>zum Brandenburger Tor</i>)<br>
                                • die -> <b>zur</b> (<i>zur Post, zur Bank, zur Ampel</i>)
                            </td>
                            <td class="p-3">
                                • der -> <b>in den</b> (<i>in den Berliner Dom</i>)<br>
                                • das -> <b>ins</b> (<i>ins Kino, ins Museum</i>)<br>
                                • die -> <b>in die</b> (<i>in die Disko, in die Galerie</i>)
                            </td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold bg-slate-50/50">Ví dụ từ bài giảng</td>
                            <td class="p-3 italic">
                                „Paula und Alex gehen <b>zum Brandenburger Tor</b> und machen viele Fotos.“ (đến khu vực Cổng chụp ảnh).
                            </td>
                            <td class="p-3 italic">
                                „Am Nachmittag gehen sie <b>in den Berliner Dom</b> und hören ein Konzert.“ (vào bên trong nghe hòa nhạc).
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- LƯU Ý THỰC TẾ ZU VS IN -->
            <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-200 text-xs sm:text-sm text-amber-950 space-y-2 leading-relaxed">
                <div class="font-bold flex items-center gap-1.5 text-amber-900">
                    <span>💡</span> Hướng Dẫn Sử Dụng Thực Tế (Không phải luật tuyệt đối):
                </div>
                <ul class="list-disc list-inside space-y-1 text-slate-700">
                    <li><b>zu</b> thường dùng cho <b>người, cơ quan, nơi làm việc/học tập, ga, bưu điện</b>: <i>zum Arzt, zur Schule, zur Arbeit, zum Bahnhof, zur Post</i>.</li>
                    <li><b>in</b> thường dùng cho <b>nơi giải trí, mua sắm, tham quan</b>: <i>ins Kino, ins Museum, in den Supermarkt, in die Disko</i>.</li>
                    <li>Một số nơi dùng được cả hai (<i>zum Supermarkt</i> hoặc <i>in den Supermarkt</i>), nên bảng chỉ là hướng dẫn phân biệt sắc thái, không phải luật tuyệt đối.</li>
                </ul>
            </div>
        </div>

        <!-- HỌC PHẦN 4: MA TRẬN 4 ĐỘNG TỪ KHUYẾT THIẾU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Hệ Thống Ma Trận 4 Động Từ Khuyết Thiếu (möchten - können - müssen - wollen)</h4>
            </div>

            <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 text-xs sm:text-sm text-purple-950 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>⭐</span> Điểm Mới Trọng Tâm: Động từ khuyết thiếu 'wollen' (muốn / định làm):</p>
                <p><b>wollen = muốn/định làm</b> (trực tiếp, mạnh hơn <i>möchten</i>). <b>Không dùng để gọi món hoặc nhờ người lạ</b>, hãy nói <i>Ich möchte einen Kaffee</i>. Biến âm: <b>o -> i</b> ở số ít: <i>ich will, du willst, er/sie/es will</i>. Lưu ý: ngôi <b>ich</b> bằng ngôi <b>er/sie/es</b> và không có đuôi <b>-t</b>!</p>
            </div>

            <div class="overflow-x-auto rounded-2xl border border-slate-200">
                <table class="w-full text-center text-xs sm:text-sm">
                    <thead class="bg-slate-50 text-slate-700 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3 text-left">Ngôi Nhân Xưng</th>
                            <th class="p-3">1. möchten</th>
                            <th class="p-3">2. können</th>
                            <th class="p-3">3. müssen</th>
                            <th class="p-3 text-purple-700 font-extrabold">4. wollen ⭐</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <tr>
                            <td class="p-3 text-left font-bold">ich</td>
                            <td class="p-3">möchte</td>
                            <td class="p-3">kann</td>
                            <td class="p-3">muss</td>
                            <td class="p-3 font-extrabold text-purple-700 bg-purple-50/50">will</td>
                        </tr>
                        <tr>
                            <td class="p-3 text-left font-bold">du</td>
                            <td class="p-3">möchtest</td>
                            <td class="p-3">kannst</td>
                            <td class="p-3">musst</td>
                            <td class="p-3 font-extrabold text-purple-700 bg-purple-50/50">willst</td>
                        </tr>
                        <tr>
                            <td class="p-3 text-left font-bold">er / sie / es</td>
                            <td class="p-3">möchte</td>
                            <td class="p-3">kann</td>
                            <td class="p-3">muss</td>
                            <td class="p-3 font-extrabold text-purple-700 bg-purple-50/50">will</td>
                        </tr>
                        <tr>
                            <td class="p-3 text-left font-bold">wir</td>
                            <td class="p-3">möchten</td>
                            <td class="p-3">können</td>
                            <td class="p-3">müssen</td>
                            <td class="p-3 font-bold">wollen</td>
                        </tr>
                        <tr>
                            <td class="p-3 text-left font-bold">ihr</td>
                            <td class="p-3">möchtet</td>
                            <td class="p-3">könnt</td>
                            <td class="p-3">müsst</td>
                            <td class="p-3 font-bold">wollt</td>
                        </tr>
                        <tr>
                            <td class="p-3 text-left font-bold">sie / Sie</td>
                            <td class="p-3">möchten</td>
                            <td class="p-3">können</td>
                            <td class="p-3">müssen</td>
                            <td class="p-3 font-bold">wollen</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- HỌC PHẦN 5: PHÂN TÍCH 2 ĐOẠN VĂN MẪU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-rose-100 text-rose-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Phân Tích 2 Đoạn Văn Mẫu: Paula & Alex Khám Phá Berlin</h4>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                <!-- Đoạn 1 -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-extrabold text-slate-900">📖 Đoạn 1: Hành trình tại Berlin</span>
                        <button onclick="speakGerman('Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin. Sie gehen zum Brandenburger Tor und machen viele Fotos. Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke. Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert. Am Abend essen sie Pizza und gehen danach in die Disko.', 1.0)" class="px-2.5 py-1 rounded-lg bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs cursor-pointer">
                            🔊 Nghe de-DE
                        </button>
                    </div>
                    <p class="italic font-serif text-slate-800 leading-relaxed">„Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin. Sie gehen <b>zum Brandenburger Tor</b> und machen viele Fotos. Sie fahren mit dem Bus <b>am Bundeskanzleramt vorbei</b> und laufen <b>über die Schlossbrücke</b>. Am Nachmittag gehen sie <b>in den Berliner Dom</b> und hören ein Konzert. Am Abend essen sie Pizza und gehen danach <b>in die Disko</b> ‚Von Euch‘.“</p>
                    <p class="text-slate-600 text-xs"><b>Dịch nghĩa:</b> Paula và Alex đến từ Madrid. Họ thăm bạn bè ở Berlin. Họ đi đến Cổng Brandenburg chụp ảnh. Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke. Buổi chiều họ vào Nhà thờ lớn Berlin nghe hòa nhạc. Buổi tối họ ăn pizza và vào vũ trường 'Von Euch'.</p>
                </div>

                <!-- Đoạn 2 -->
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <div class="flex items-center justify-between">
                        <span class="font-extrabold text-slate-900">📱 Đoạn 2: Tin nhắn gửi Julia</span>
                        <button onclick="speakGerman('Hi Julia! Berlin ist super! Wir wollen noch eine Stadtrundfahrt machen. Danach will ich in die Nationalgalerie gehen. Anschließend wollen Maria und ich auf der Friedrichstraße bummeln. Und heute Abend wollen wir noch einen Film im Kino sehen.', 1.0)" class="px-2.5 py-1 rounded-lg bg-sky-600 hover:bg-sky-700 text-white font-bold text-xs cursor-pointer">
                            🔊 Nghe de-DE
                        </button>
                    </div>
                    <p class="italic font-serif text-slate-800 leading-relaxed">„Hi Julia! Berlin ist super! Wir <b>wollen</b> noch eine Stadtrundfahrt <b>machen</b>. <b>Danach will</b> ich in die Nationalgalerie <b>gehen</b>. <b>Anschließend wollen</b> Maria und ich auf der Friedrichstraße <b>bummeln</b>. Und heute Abend <b>wollen</b> wir noch einen Film im Kino <b>sehen</b>.“</p>
                    <p class="text-slate-600 text-xs"><b>Dịch nghĩa:</b> Chào Julia! Berlin tuyệt vời lắm! Chúng mình còn muốn làm một chuyến tham quan thành phố. Sau đó mình muốn đi vào Khu triển lãm Quốc gia. Tiếp ngay sau đó Maria và mình muốn đi dạo phố trên đường Friedrich. Và tối nay chúng mình còn muốn xem một bộ phim trong rạp.</p>
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
    # DANH MỤC 50 TỪ VỰNG TRỌNG TÂM BÀI 8 (KHỚP 100% VỚI LEXIKON_DB.JS)
    # =========================================================================
    vocab_raw = [
        {
                "word": "Bahnhof",
                "article": "der",
                "gender": "der",
                "plural": "die Bahnhöfe",
                "indefinite": "ein Bahnhof",
                "negation": "kein Bahnhof",
                "akkusativ": "den Bahnhof",
                "meaning": "nhà ga tàu hỏa",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm đuôi -e (die Bahnhöfe).",
                "example": "Entschuldigung, wie komme ich zum Bahnhof?",
                "example_vi": "Xin lỗi, làm thế nào tôi đi đến được nhà ga?"
        },
        {
                "word": "Hauptbahnhof",
                "article": "der",
                "gender": "der",
                "plural": "die Hauptbahnhöfe",
                "indefinite": "ein Hauptbahnhof",
                "negation": "kein Hauptbahnhof",
                "akkusativ": "den Hauptbahnhof",
                "meaning": "nhà ga trung tâm",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ ghép với der Bahnhof (Haupt + Bahnhof), số nhiều: die Hauptbahnhöfe.",
                "example": "Der Zug nach München fährt vom Hauptbahnhof ab.",
                "example_vi": "Chuyến tàu đi München khởi hành từ nhà ga trung tâm."
        },
        {
                "word": "Hafen",
                "article": "der",
                "gender": "der",
                "plural": "die Häfen",
                "indefinite": "ein Hafen",
                "negation": "kein Hafen",
                "akkusativ": "den Hafen",
                "meaning": "cảng biển",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều biến âm a -> ä (die Häfen).",
                "example": "In Hamburg besichtigen wir den großen Hafen.",
                "example_vi": "Ở Hamburg chúng tôi tham quan cảng biển lớn."
        },
        {
                "word": "Flughafen",
                "article": "der",
                "gender": "der",
                "plural": "die Flughäfen",
                "indefinite": "ein Flughafen",
                "negation": "kein Flughafen",
                "akkusativ": "den Flughafen",
                "meaning": "sân bay",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ ghép (Flug + der Hafen), số nhiều: die Flughäfen.",
                "example": "Der Taxifahrer fährt schnell zum Flughafen.",
                "example_vi": "Người tài xế taxi lái xe nhanh đến sân bay."
        },
        {
                "word": "Markt",
                "article": "der",
                "gender": "der",
                "plural": "die Märkte",
                "indefinite": "ein Markt",
                "negation": "kein Markt",
                "akkusativ": "den Markt",
                "meaning": "chợ, khu chợ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm đuôi -e (die Märkte).",
                "example": "Am Samstag kaufe ich frisches Obst auf dem Markt.",
                "example_vi": "Vào thứ Bảy tôi mua hoa quả tươi ở chợ."
        },
        {
                "word": "Supermarkt",
                "article": "der",
                "gender": "der",
                "plural": "die Supermärkte",
                "indefinite": "ein Supermarkt",
                "negation": "kein Supermarkt",
                "akkusativ": "den Supermarkt",
                "meaning": "siêu thị",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ ghép (Super + der Markt), số nhiều: die Supermärkte.",
                "example": "Er geht nach der Arbeit in den Supermarkt einkaufen.",
                "example_vi": "Anh ấy đi vào siêu thị mua sắm sau giờ làm việc."
        },
        {
                "word": "Platz",
                "article": "der",
                "gender": "der",
                "plural": "die Plätze",
                "indefinite": "ein Platz",
                "negation": "kein Platz",
                "akkusativ": "den Platz",
                "meaning": "quảng trường, chỗ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm -e (die Plätze). Băng qua quảng trường: über den Platz.",
                "example": "Gehen Sie geradeaus über den Platz!",
                "example_vi": "Ngài hãy đi thẳng băng qua quảng trường!"
        },
        {
                "word": "Park",
                "article": "der",
                "gender": "der",
                "plural": "die Parks",
                "indefinite": "ein Park",
                "negation": "kein Park",
                "akkusativ": "den Park",
                "meaning": "công viên",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều thêm -s (die Parks). Đi xuyên qua công viên: durch den Park.",
                "example": "Am Nachmittag spazieren wir gern durch den Park.",
                "example_vi": "Vào buổi chiều chúng tôi thích đi dạo xuyên qua công viên."
        },
        {
                "word": "Zoo",
                "article": "der",
                "gender": "der",
                "plural": "die Zoos",
                "indefinite": "ein Zoo",
                "negation": "kein Zoo",
                "akkusativ": "den Zoo",
                "meaning": "vườn bách thú, sở thú",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực vay mượn, số nhiều thêm -s (die Zoos).",
                "example": "Am Wochenende besuchen viele Familien den Zoo.",
                "example_vi": "Vào cuối tuần nhiều gia đình đi tham quan sở thú."
        },
        {
                "word": "Turm",
                "article": "der",
                "gender": "der",
                "plural": "die Türme",
                "indefinite": "ein Turm",
                "negation": "kein Turm",
                "akkusativ": "den Turm",
                "meaning": "tòa tháp, ngọn tháp",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều biến âm u -> ü và thêm -e (die Türme).",
                "example": "Von diesem Turm hat man eine schöne Aussicht.",
                "example_vi": "Từ ngọn tháp này người ta có một tầm nhìn rất đẹp."
        },
        {
                "word": "Dom",
                "article": "der",
                "gender": "der",
                "plural": "die Dome",
                "indefinite": "ein Dom",
                "negation": "kein Dom",
                "akkusativ": "den Dom",
                "meaning": "nhà thờ lớn, thánh đường",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống đực (der), số nhiều thêm đuôi -e (die Dome).",
                "example": "Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.",
                "example_vi": "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc."
        },
        {
                "word": "Stadt",
                "article": "die",
                "gender": "die",
                "plural": "die Städte",
                "indefinite": "eine Stadt",
                "negation": "keine Stadt",
                "akkusativ": "die Stadt",
                "meaning": "thành phố",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều biến âm a -> ä và thêm -e (die Städte).",
                "example": "Berlin ist eine sehr interessante Stadt.",
                "example_vi": "Berlin là một thành phố rất thú vị."
        },
        {
                "word": "Kirche",
                "article": "die",
                "gender": "die",
                "plural": "die Kirchen",
                "indefinite": "eine Kirche",
                "negation": "keine Kirche",
                "akkusativ": "die Kirche",
                "meaning": "nhà thờ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều thêm -n (die Kirchen). Đi ngang qua nhà thờ: an der Kirche vorbei.",
                "example": "Gehen Sie an der Kirche vorbei und dann links!",
                "example_vi": "Ngài hãy đi ngang qua nhà thờ rồi sau đó rẽ trái!"
        },
        {
                "word": "Schule",
                "article": "die",
                "gender": "die",
                "plural": "die Schulen",
                "indefinite": "eine Schule",
                "negation": "keine Schule",
                "akkusativ": "die Schule",
                "meaning": "trường học",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều thêm -n (die Schulen).",
                "example": "Die Kinder gehen jeden Morgen zur Schule.",
                "example_vi": "Bọn trẻ đi đến trường vào mỗi buổi sáng."
        },
        {
                "word": "Brücke",
                "article": "die",
                "gender": "die",
                "plural": "die Brücken",
                "indefinite": "eine Brücke",
                "negation": "keine Brücke",
                "akkusativ": "die Brücke",
                "meaning": "cây cầu",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều thêm -n (die Brücken). Đi qua cầu: über die Brücke.",
                "example": "Wir laufen über die Brücke zum Museum.",
                "example_vi": "Chúng tôi đi bộ qua cây cầu đến viện bảo tàng."
        },
        {
                "word": "Bank",
                "article": "die",
                "gender": "die",
                "plural": "die Banken",
                "indefinite": "eine Bank",
                "negation": "keine Bank",
                "akkusativ": "die Bank",
                "meaning": "ngân hàng (tài chính)",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Phân biệt 2 nghĩa: Ngân hàng tiền số nhiều là die Banken; ghế băng dài số nhiều là die Bänke.",
                "example": "Vor der Reise muss ich noch zur Bank gehen.",
                "example_vi": "Trước chuyến đi tôi còn phải ra ngân hàng."
        },
        {
                "word": "Post",
                "article": "die",
                "gender": "die",
                "plural": "nur Singular",
                "indefinite": "eine Post",
                "negation": "keine Post",
                "akkusativ": "die Post",
                "meaning": "bưu điện, ngành bưu chính",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái chỉ dùng ở số ít (nur Singular). Khi muốn đếm nhiều bưu cục cụ thể dùng das Postamt -> die Postämter.",
                "example": "Ich bringe diesen Brief schnell zur Post.",
                "example_vi": "Tôi mang lá thư này nhanh ra bưu điện."
        },
        {
                "word": "Straße",
                "article": "die",
                "gender": "die",
                "plural": "die Straßen",
                "indefinite": "eine Straße",
                "negation": "keine Straße",
                "akkusativ": "die Straße",
                "meaning": "con đường, con phố",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều thêm -n (die Straßen). Đi dọc phố: die Straße entlang.",
                "example": "In dieser Straße gibt es viele kleine Cafés.",
                "example_vi": "Trên con phố này có rất nhiều quán cà phê nhỏ."
        },
        {
                "word": "Ampel",
                "article": "die",
                "gender": "die",
                "plural": "die Ampeln",
                "indefinite": "eine Ampel",
                "negation": "keine Ampel",
                "akkusativ": "die Ampel",
                "meaning": "đèn giao thông",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều thêm -n (die Ampeln). Cho đến đèn giao thông: bis zur Ampel.",
                "example": "An der Ampel biegen Sie bitte rechts ab!",
                "example_vi": "Tại đèn giao thông xin Ngài hãy rẽ phải!"
        },
        {
                "word": "Kreuzung",
                "article": "die",
                "gender": "die",
                "plural": "die Kreuzungen",
                "indefinite": "eine Kreuzung",
                "negation": "keine Kreuzung",
                "akkusativ": "die Kreuzung",
                "meaning": "ngã tư, giao lộ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Hậu tố -ung luôn là giống cái (die), số nhiều: die Kreuzungen. Băng qua ngã tư: über die Kreuzung.",
                "example": "An der nächsten Kreuzung fahren wir geradeaus.",
                "example_vi": "Tại ngã tư tiếp theo chúng ta đi thẳng."
        },
        {
                "word": "Disko",
                "article": "die",
                "gender": "die",
                "plural": "die Diskos",
                "indefinite": "eine Disko",
                "negation": "keine Disko",
                "akkusativ": "die Disko",
                "meaning": "vũ trường, quán bar nhảy",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống cái (die), số nhiều thêm -s (die Diskos). Vào vũ trường: in die Disko.",
                "example": "Am Freitagabend gehen die Jugendlichen in die Disko.",
                "example_vi": "Vào tối thứ Sáu các bạn trẻ đi vào vũ trường."
        },
        {
                "word": "Schloss",
                "article": "das",
                "gender": "das",
                "plural": "die Schlösser",
                "indefinite": "ein Schloss",
                "negation": "kein Schloss",
                "akkusativ": "das Schloss",
                "meaning": "lâu đài, cung điện",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống trung (das), số nhiều biến âm o -> ö và thêm -er (die Schlösser).",
                "example": "Das alte Schloss liegt direkt am Fluss.",
                "example_vi": "Tòa lâu đài cổ nằm ngay bên cạnh dòng sông."
        },
        {
                "word": "Stadttor",
                "article": "das",
                "gender": "das",
                "plural": "die Stadttore",
                "indefinite": "ein Stadttor",
                "negation": "kein Stadttor",
                "akkusativ": "das Stadttor",
                "meaning": "cổng thành",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ ghép giống trung (die Stadt + das Tor), số nhiều: die Stadttore. Đi xuyên qua cổng: durch das Stadttor.",
                "example": "Die Touristen gehen durch das historische Stadttor.",
                "example_vi": "Các du khách đi xuyên qua cổng thành lịch sử."
        },
        {
                "word": "Kino",
                "article": "das",
                "gender": "das",
                "plural": "die Kinos",
                "indefinite": "ein Kino",
                "negation": "kein Kino",
                "akkusativ": "das Kino",
                "meaning": "rạp chiếu phim",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống trung (das), số nhiều thêm -s (die Kinos). Đi vào rạp: ins Kino (in das Kino).",
                "example": "Heute Abend gehen wir zusammen ins Kino.",
                "example_vi": "Tối nay chúng tôi cùng nhau đi xem phim ở rạp."
        },
        {
                "word": "Krankenhaus",
                "article": "das",
                "gender": "das",
                "plural": "die Krankenhäuser",
                "indefinite": "ein Krankenhaus",
                "negation": "kein Krankenhaus",
                "akkusativ": "das Krankenhaus",
                "meaning": "bệnh viện",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ ghép giống trung (der Kranke + das Haus), số nhiều: die Krankenhäuser. Đi ngang qua: am Krankenhaus vorbei.",
                "example": "Der Arzt arbeitet jeden Tag im Krankenhaus.",
                "example_vi": "Bác sĩ làm việc mỗi ngày ở trong bệnh viện."
        },
        {
                "word": "Einkaufszentrum",
                "article": "das",
                "gender": "das",
                "plural": "die Einkaufszentren",
                "indefinite": "ein Einkaufszentrum",
                "negation": "kein Einkaufszentrum",
                "akkusativ": "das Einkaufszentrum",
                "meaning": "trung tâm thương mại",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Đuôi -um đổi thành -en ở số nhiều: die Einkaufszentren. Giống trung (das).",
                "example": "Am Samstag gehen viele Leute ins Einkaufszentrum.",
                "example_vi": "Vào thứ Bảy nhiều người đi vào trung tâm thương mại."
        },
        {
                "word": "Hotel",
                "article": "das",
                "gender": "das",
                "plural": "die Hotels",
                "indefinite": "ein Hotel",
                "negation": "kein Hotel",
                "akkusativ": "das Hotel",
                "meaning": "khách sạn",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống trung (das), số nhiều thêm -s (die Hotels).",
                "example": "Die Touristen übernachten in einem modernen Hotel.",
                "example_vi": "Các du khách nghỉ qua đêm trong một khách sạn hiện đại."
        },
        {
                "word": "Museum",
                "article": "das",
                "gender": "das",
                "plural": "die Museen",
                "indefinite": "ein Museum",
                "negation": "kein Museum",
                "akkusativ": "das Museum",
                "meaning": "viện bảo tàng",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Đuôi -um đổi thành -en ở số nhiều: die Museen. Giống trung (das).",
                "example": "Morgen wollen wir das historische Museum besuchen.",
                "example_vi": "Ngày mai chúng tôi muốn đi tham quan viện bảo tàng lịch sử."
        },
        {
                "word": "Rathaus",
                "article": "das",
                "gender": "das",
                "plural": "die Rathäuser",
                "indefinite": "ein Rathaus",
                "negation": "kein Rathaus",
                "akkusativ": "das Rathaus",
                "meaning": "tòa thị chính",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ ghép giống trung (der Rat + das Haus), số nhiều: die Rathäuser.",
                "example": "Vor dem Rathaus gibt es einen schönen Marktplatz.",
                "example_vi": "Ở phía trước tòa thị chính có một quảng trường chợ đẹp."
        },
        {
                "word": "Theater",
                "article": "das",
                "gender": "das",
                "plural": "die Theater",
                "indefinite": "ein Theater",
                "negation": "kein Theater",
                "akkusativ": "das Theater",
                "meaning": "nhà hát kịch",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Danh từ giống trung (das), giữ nguyên dạng ở số nhiều (die Theater).",
                "example": "Am Wochenende gehen wir ins Theater.",
                "example_vi": "Vào cuối tuần chúng tôi đi xem kịch ở nhà hát."
        },
        {
                "word": "Reichstag",
                "article": "der",
                "gender": "der",
                "plural": "die Reichstage",
                "indefinite": "ein Reichstag",
                "negation": "kein Reichstag",
                "akkusativ": "den Reichstag",
                "meaning": "Tòa nhà Quốc hội Đức",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Danh lam thắng cảnh Berlin giống đực (vì der Tag). Đi tới: zum Reichstag.",
                "example": "Die Touristen stehen vor dem Reichstag und fotografieren die Glaskuppel.",
                "example_vi": "Các du khách đứng trước Tòa nhà Quốc hội và chụp ảnh mái vòm kính."
        },
        {
                "word": "Alexanderplatz",
                "article": "der",
                "gender": "der",
                "plural": "nur Singular",
                "indefinite": "ein Alexanderplatz",
                "negation": "kein Alexanderplatz",
                "akkusativ": "den Alexanderplatz",
                "meaning": "Quảng trường Alexander",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Quảng trường nổi tiếng ở Berlin mang giống đực (vì der Platz). Đi tới: zum Alexanderplatz.",
                "example": "Wir treffen uns heute Nachmittag am Alexanderplatz.",
                "example_vi": "Chúng ta hẹn gặp nhau vào chiều nay ở Quảng trường Alexander."
        },
        {
                "word": "Potsdamer Platz",
                "article": "der",
                "gender": "der",
                "plural": "nur Singular",
                "indefinite": "ein Potsdamer Platz",
                "negation": "kein Potsdamer Platz",
                "akkusativ": "den Potsdamer Platz",
                "meaning": "Quảng trường Potsdam",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Quảng trường hiện đại tại Berlin mang giống đực (vì der Platz).",
                "example": "Am Potsdamer Platz gibt es viele moderne Hochhäuser und Kinos.",
                "example_vi": "Ở Quảng trường Potsdam có rất nhiều tòa nhà cao tầng hiện đại và rạp chiếu phim."
        },
        {
                "word": "Berliner Dom",
                "article": "der",
                "gender": "der",
                "plural": "nur Singular",
                "indefinite": "ein Berliner Dom",
                "negation": "kein Berliner Dom",
                "akkusativ": "den Berliner Dom",
                "meaning": "Nhà thờ lớn Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Thánh đường lớn ở Berlin mang giống đực (vì der Dom). Đi vào trong: in den Berliner Dom.",
                "example": "Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.",
                "example_vi": "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc."
        },
        {
                "word": "Fernsehturm",
                "article": "der",
                "gender": "der",
                "plural": "die Fernsehtürme",
                "indefinite": "ein Fernsehturm",
                "negation": "kein Fernsehturm",
                "akkusativ": "den Fernsehturm",
                "meaning": "Tháp truyền hình Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Tòa tháp cao nhất nước Đức tại Berlin mang giống đực (vì der Turm).",
                "example": "Der Fernsehturm ist das höchste Bauwerk in ganz Deutschland.",
                "example_vi": "Tháp truyền hình là công trình kiến trúc cao nhất trên toàn nước Đức."
        },
        {
                "word": "Humboldt-Universität",
                "article": "die",
                "gender": "die",
                "plural": "die Humboldt-Universitäten",
                "indefinite": "eine Humboldt-Universität",
                "negation": "keine Humboldt-Universität",
                "akkusativ": "die Humboldt-Universität",
                "meaning": "Trường Đại học Humboldt",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Hậu tố -tät luôn mang giống cái (die). Đi tới: zur Humboldt-Universität.",
                "example": "In Deutschland will mein Bruder an der Humboldt-Universität studieren.",
                "example_vi": "Ở Đức anh trai tôi muốn học đại học tại trường Đại học Humboldt."
        },
        {
                "word": "Staatsoper",
                "article": "die",
                "gender": "die",
                "plural": "die Staatsopern",
                "indefinite": "eine Staatsoper",
                "negation": "keine Staatsoper",
                "akkusativ": "die Staatsoper",
                "meaning": "Nhà hát Opera Quốc gia Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Danh lam thắng cảnh mang giống cái (vì die Oper). Đi tới: zur Staatsoper.",
                "example": "Heute Abend besuchen wir eine berühmte Oper in der Staatsoper.",
                "example_vi": "Tối nay chúng tôi đi xem một vở nhạc kịch nổi tiếng ở Nhà hát Opera Quốc gia."
        },
        {
                "word": "Friedrichstraße",
                "article": "die",
                "gender": "die",
                "plural": "nur Singular",
                "indefinite": "eine Friedrichstraße",
                "negation": "keine Friedrichstraße",
                "akkusativ": "die Friedrichstraße",
                "meaning": "Phố mua sắm Friedrich",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Con phố thương mại sầm uất tại Berlin mang giống cái (vì die Straße). Đi dọc phố: die Friedrichstraße entlang.",
                "example": "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
                "example_vi": "Tiếp sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."
        },
        {
                "word": "Museumsinsel",
                "article": "die",
                "gender": "die",
                "plural": "nur Singular",
                "indefinite": "eine Museumsinsel",
                "negation": "keine Museumsinsel",
                "akkusativ": "die Museumsinsel",
                "meaning": "Đảo Bảo tàng Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Quần thể viện bảo tàng nổi tiếng thế giới mang giống cái (vì die Insel - hòn đảo).",
                "example": "Auf der Museumsinsel besichtigen wir berühmte Kunstwerke.",
                "example_vi": "Trên Đảo Bảo tàng chúng tôi tham quan các tác phẩm nghệ thuật nổi tiếng."
        },
        {
                "word": "Alte Nationalgalerie",
                "article": "die",
                "gender": "die",
                "plural": "die Alten Nationalgalerien",
                "indefinite": "eine Alte Nationalgalerie",
                "negation": "keine Alte Nationalgalerie",
                "akkusativ": "die Alte Nationalgalerie",
                "meaning": "Phòng trưng bày Quốc gia Cũ",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Hậu tố -ie luôn mang giống cái (die Galerie). Đi vào: in die Alte Nationalgalerie.",
                "example": "Danach will ich in die Alte Nationalgalerie gehen.",
                "example_vi": "Sau đó tôi muốn đi vào Phòng trưng bày Quốc gia Cũ."
        },
        {
                "word": "Bundeskanzleramt",
                "article": "das",
                "gender": "das",
                "plural": "die Bundeskanzlerämter",
                "indefinite": "ein Bundeskanzleramt",
                "negation": "kein Bundeskanzleramt",
                "akkusativ": "das Bundeskanzleramt",
                "meaning": "Phủ Thủ tướng Liên bang",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Danh lam thắng cảnh mang giống trung (vì das Amt - cơ quan).",
                "example": "Sie fahren mit dem Bus am Bundeskanzleramt vorbei.",
                "example_vi": "Họ đi xe buýt ngang qua Phủ Thủ tướng Liên bang."
        },
        {
                "word": "Brandenburger Tor",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Brandenburger Tor",
                "negation": "kein Brandenburger Tor",
                "akkusativ": "das Brandenburger Tor",
                "meaning": "Cổng thành Brandenburg",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Biểu tượng lịch sử nước Đức mang giống trung (vì das Tor). Đi tới: zum Brandenburger Tor.",
                "example": "Sie gehen zum Brandenburger Tor und machen viele Fotos.",
                "example_vi": "Họ đi đến Cổng Brandenburg và chụp nhiều bức ảnh."
        },
        {
                "word": "Schloss Bellevue",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Schloss Bellevue",
                "negation": "kein Schloss Bellevue",
                "akkusativ": "das Schloss Bellevue",
                "meaning": "Cung điện Bellevue",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Dinh thự Tổng thống Đức mang giống trung (vì das Schloss).",
                "example": "Das Schloss Bellevue liegt mitten im Tiergarten an der Spree.",
                "example_vi": "Cung điện Bellevue nằm giữa công viên Tiergarten bên bờ sông Spree."
        },
        {
                "word": "Sony Center",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Sony Center",
                "negation": "kein Sony Center",
                "akkusativ": "das Sony Center",
                "meaning": "Trung tâm phức hợp Sony Center",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "notes": "Khu phức hợp hiện đại tại Potsdamer Platz mang giống trung (vì das Center).",
                "example": "Im Sony Center gibt es viele Restaurants, Kinos und Geschäfte.",
                "example_vi": "Trong Sony Center có rất nhiều nhà hàng, rạp chiếu phim và cửa hàng."
        },
        {
                "word": "geradeaus",
                "article": null,
                "gender": null,
                "plural": null,
                "indefinite": null,
                "negation": null,
                "akkusativ": "geradeaus",
                "meaning": "đi thẳng",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Trạng từ chỉ hướng: geradeaus gehen (đi thẳng).",
                "example": "Gehen Sie bitte 200 Meter geradeaus!",
                "example_vi": "Xin Ngài hãy đi thẳng 200 mét!"
        },
        {
                "word": "vorbei",
                "article": null,
                "gender": null,
                "plural": null,
                "indefinite": null,
                "negation": null,
                "akkusativ": "vorbei",
                "meaning": "ngang qua",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Giới từ phối hợp: an + Dativ + vorbei (đi ngang qua bên cạnh tòa nhà).",
                "example": "Er geht an der Bank vorbei.",
                "example_vi": "Anh ấy đi ngang qua ngân hàng."
        },
        {
                "word": "entlang",
                "article": null,
                "gender": null,
                "plural": null,
                "indefinite": null,
                "negation": null,
                "akkusativ": "entlang",
                "meaning": "dọc theo",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Đứng SAU danh từ ở Akkusativ: die Straße entlang (dọc theo con đường).",
                "example": "Laufen Sie den Fluss entlang!",
                "example_vi": "Ngài hãy đi dọc theo con sông!"
        },
        {
                "word": "über",
                "article": null,
                "gender": null,
                "plural": null,
                "indefinite": null,
                "negation": null,
                "akkusativ": "über",
                "meaning": "băng qua, vượt qua trên mặt",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Giới từ đi với Akkusativ khi có chuyển động: über die Brücke (qua cầu), über den Platz (qua quảng trường).",
                "example": "Wir gehen über die Brücke.",
                "example_vi": "Chúng tôi đi qua cây cầu."
        },
        {
                "word": "durch",
                "article": null,
                "gender": null,
                "plural": null,
                "indefinite": null,
                "negation": null,
                "akkusativ": "durch",
                "meaning": "xuyên qua",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Giới từ luôn đi với Akkusativ: durch das Tor (qua cổng), durch den Park (qua công viên).",
                "example": "Die Touristen gehen durch das Tor.",
                "example_vi": "Các du khách đi xuyên qua cánh cổng."
        },
        {
                "word": "bummeln",
                "article": null,
                "gender": null,
                "plural": null,
                "indefinite": null,
                "negation": null,
                "akkusativ": "bummeln",
                "meaning": "đi dạo phố, tản bộ ngắm cảnh",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "notes": "Động từ thường đi với auf / durch: auf der Straße bummeln.",
                "example": "Am Nachmittag wollen wir im Zentrum bummeln.",
                "example_vi": "Buổi chiều chúng tôi muốn đi dạo phố ở trung tâm."
        }
]

    vocabularies = []
    for v in vocab_raw:
        art = v.get("article") or ""
        w = v.get("word") or ""
        full_w = (art + " " + w).strip() if art else w
        pl = v.get("plural")
        meaning = (v["meaning"] + " (Pl: " + pl + ")") if pl else v["meaning"]
        ex_vi = v.get("example_vi")
        example_str = (v["example"] + " (" + ex_vi + ")") if ex_vi else v.get("example")
        vocabularies.append((
            lesson_id,
            full_w,
            art if art else None,
            meaning,
            example_str
        ))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # 100 BÀI TẬP ĐỘC NHẤT BÀI 8 (CHUẨN 9 DẠNG BÀI - ZERO BUG & KHÔNG LỘ GỢI Ý)
    # =========================================================================
    exercises_raw = [
        {
                "type": "trac_nghiem",
                "question": "Câu 1: Một du khách đứng ở điểm START và hỏi đường. Hãy đọc lời chỉ đường, đối chiếu với bản đồ và chọn nơi du khách đang tìm.\n„Gehen Sie zuerst geradeaus über die erste Kreuzung! An der zweiten Kreuzung biegen Sie rechts ab. Gehen Sie dann am Krankenhaus vorbei bis zur Ampel. Direkt hinter der Ampel liegt das Gebäude links.“",
                "options": [
                        "Das Schloss",
                        "Das Kino",
                        "Die Post",
                        "Der Bahnhof"
                ],
                "correct_answer": "Das Kino",
                "explanation": "Từ START đi thẳng qua ngã tư 1 → ngã tư 2 rẽ phải (vào Behrenstr.) → đi qua Krankenhaus ('am Krankenhaus vorbei') tới Ampel ('bis zur Ampel') → ngay sau Ampel, bên trái là Kino.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Das Kino"
                        ],
                        "translation": "Đầu tiên bạn hãy đi thẳng qua ngã tư thứ nhất! Ở ngã tư thứ hai bạn hãy rẽ phải. Sau đó bạn đi qua bệnh viện cho đến đèn giao thông. Ngay phía sau đèn giao thông là tòa nhà ở bên trái.",
                        "visual_svg": "map_route_finder_1"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 2: Bạn của bạn là Jonas muốn đến Einkaufszentrum. Lời chỉ đường nào khớp chính xác với lộ trình màu xanh trên bản đồ?",
                "options": [
                        "Geh geradeaus und nimm die zweite Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                        "Geh geradeaus und nimm die dritte Straße rechts. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                        "Geh geradeaus und nimm die dritte Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                        "Geh geradeaus und nimm die dritte Straße links. Geh durch den Park und dann über die Brücke. Das Einkaufszentrum liegt rechts."
                ],
                "correct_answer": "Geh geradeaus und nimm die dritte Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                "explanation": "Thứ tự trên bản đồ là đi thẳng → ngã tư thứ 3 rẽ trái → qua cầu ('über die Brücke') → xuyên công viên ('durch den Park') → Einkaufszentrum bên phải. Câu 'nimm die zweite Straße links' sai vì ngã rẽ thực tế là đường thứ ba. Câu 'dritte Straße rechts' sai vì đường rẽ sang bên trái. Câu 'durch den Park und dann über die Brücke' sai thứ tự vì trên lộ trình bạn đi qua cầu trước rồi mới đi xuyên qua công viên.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Geh geradeaus und nimm die dritte Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts."
                        ],
                        "translation": "Bạn hãy đi thẳng và đi vào con đường thứ ba bên trái. Hãy đi qua cầu và sau đó đi xuyên qua công viên. Trung tâm thương mại nằm ở bên phải.",
                        "visual_svg": "map_route_line_2"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 3: Chọn chuỗi câu tiếng Đức mô tả đúng ba hình (1 → 2 → 3) và hoàn toàn đúng ngữ pháp.",
                "options": [
                        "Zuerst gehen wir an die Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                        "Zuerst gehen wir am Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                        "Zuerst gehen wir an der Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                        "Zuerst gehen wir durch das Stadttor, dann an der Staatsoper vorbei und danach den Fluss entlang."
                ],
                "correct_answer": "Zuerst gehen wir an der Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                "explanation": "(1) die Staatsoper (giống cái) → 'an der Staatsoper vorbei' (an + Dativ). (2) das Stadttor (giống trung) → 'durch das Stadttor' (durch + Akkusativ). (3) der Fluss (giống đực) → 'den Fluss entlang' (entlang đặt sau danh từ + Akkusativ). Thứ tự khớp hình 1 → 2 → 3. Đáp án 'Zuerst gehen wir durch das Stadttor, dann an der Staatsoper vorbei und danach den Fluss entlang' tuy đúng ngữ pháp nhưng sai thứ tự so với các hình (hình 1 là Staatsoper, hình 2 là Stadttor).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Zuerst gehen wir an der Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang."
                        ],
                        "translation": "Đầu tiên chúng ta đi ngang qua Nhà hát Opera, sau đó đi xuyên qua cổng thành và tiếp theo đi dọc theo dòng sông.",
                        "visual_svg": "quiz_spatial_3_steps"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 4: Một bà cụ hỏi bạn đường trên phố ở Berlin. Câu hỏi nào dưới đây SAI ngữ pháp?",
                "options": [
                        "Entschuldigung, wo finde ich das Bundeskanzleramt?",
                        "Entschuldigung, wie komme ich zum Museumsinsel?",
                        "Entschuldigung, wo ist hier eine Bank?",
                        "Entschuldigung, wo geht es hier zum Hauptbahnhof?"
                ],
                "correct_answer": "Entschuldigung, wie komme ich zum Museumsinsel?",
                "explanation": "die Museumsinsel là danh từ giống cái (vì die Insel) → khi hỏi đường dùng cấu trúc zu + Dativ, zu + der biến thành 'zur Museumsinsel', không thể dùng 'zum' (câu đúng phải là: 'Entschuldigung, wie komme ich zur Museumsinsel?'). Câu hỏi 'wo geht es hier zum Hauptbahnhof?' là đúng ngữ pháp vì der Hauptbahnhof là danh từ giống đực → zu + dem = zum.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Entschuldigung, wie komme ich zum Museumsinsel?"
                        ],
                        "translation": "Xin lỗi, làm thế nào tôi đến được Đảo Bảo tàng?"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 5: Bạn chỉ đường cho Clara và Tim trên bản đồ. Chọn đáp án điền đúng vào các chỗ trống.\n„Clara und Tim suchen das historische Rathaus. Du erklärst ihnen den Weg: ‚Geht zuerst ___ Humboldt-Universität und ___ Berliner Dom vorbei, dann geradeaus bis ___ Ampel und über ___ Marktplatz!‘“",
                "options": [
                        "an der / am / zum / den",
                        "an der / am / zur / dem",
                        "an der / am / zur / den",
                        "am / an der / zur / den"
                ],
                "correct_answer": "an der / am / zur / den",
                "explanation": "die Humboldt-Universität (giống cái) → 'an der Humboldt-Universität vorbei' (an + Dativ); der Berliner Dom (giống đực) → 'am Berliner Dom vorbei' (an + dem = am); die Ampel (giống cái) → 'bis zur Ampel' (zu + der = zur); der Marktplatz (giống đực) đi với 'über + Akkusativ' khi chỉ hướng di chuyển → 'über den Marktplatz'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "an der / am / zur / den"
                        ],
                        "translation": "Clara và Tim đang tìm tòa thị chính lịch sử. Bạn giải thích đường đi cho họ: 'Đầu tiên các bạn hãy đi qua Đại học Humboldt và đi qua Nhà thờ lớn Berlin, sau đó đi thẳng cho đến đèn giao thông và đi băng qua quảng trường chợ!'",
                        "visual_svg": "map_route_line_3"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 6: Hàng nào có cả 4 danh từ cùng một mạo từ xác định ở số ít?",
                "options": [
                        "Staatsoper – Brücke – Stadttor – Friedrichstraße",
                        "Schloss – Einkaufszentrum – Bank – Bundeskanzleramt",
                        "Reichstag – Hafen – Fernsehturm – Potsdamer Platz",
                        "Bahnhof – Markt – Museumsinsel – Zoo"
                ],
                "correct_answer": "Reichstag – Hafen – Fernsehturm – Potsdamer Platz",
                "explanation": "Hàng 'Reichstag – Hafen – Fernsehturm – Potsdamer Platz' đều là danh từ giống đực mang mạo từ 'der' (der Reichstag, der Hafen, der Fernsehturm, der Potsdamer Platz). Hàng có Staatsoper lẫn 'das Stadttor' (còn lại là die). Hàng có Schloss lẫn 'die Bank' (còn lại là das). Hàng có Bahnhof lẫn 'die Museumsinsel' (còn lại là der).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Reichstag – Hafen – Fernsehturm – Potsdamer Platz"
                        ],
                        "translation": "Tòa nhà Quốc hội – cảng – tháp truyền hình – Quảng trường Potsdam."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 7: Câu nào dưới đây mô tả một đại đô thị châu Âu và dùng ĐÚNG tất cả các dạng số nhiều?",
                "options": [
                        "In dieser Metropole gibt es drei Flughäfe, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks.",
                        "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks.",
                        "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentrums und viele grüne Parks.",
                        "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parken."
                ],
                "correct_answer": "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks.",
                "explanation": "der Flughafen → die Flughäfen (chỉ biến âm a → ä, không thêm đuôi vì Flughafen đã kết thúc bằng -en); das Schloss → die Schlösser (biến âm + đuôi -er); das Einkaufszentrum → die Einkaufszentren (đuôi -um đổi thành -en); der Park → die Parks (từ vay mượn nước ngoài, số nhiều thêm -s).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks."
                        ],
                        "translation": "Ở đại đô thị này có ba sân bay, bốn lâu đài cổ, hai trung tâm thương mại lớn và nhiều công viên xanh mát."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 8: Chọn đáp án điền đúng vào hai chỗ trống.\n‚In der Innenstadt arbeiten viele Menschen in den internationalen ___, und im Stadtpark sitzen die Rentner gern auf den sonnigen ___.‘",
                "options": [
                        "Banken / Banken",
                        "Banken / Bänken",
                        "Bänken / Bänken",
                        "Banken / Bänke"
                ],
                "correct_answer": "Banken / Bänken",
                "explanation": "Cùng một từ 'die Bank' nhưng hai nghĩa có hai số nhiều khác nhau: ngân hàng → 'die Banken'; ghế băng → 'die Bänke' (có Umlaut). Sau 'in den' và 'auf den' (Dativ số nhiều) danh từ phải có đuôi -n: 'in den Banken' (đã có sẵn -n), 'auf den Bänken'. Đáp án 'Banken' cho ghế băng thiếu Umlaut; 'Bänken' cho ngân hàng dùng sai dạng; 'Bänke' thiếu đuôi -n ở Dativ số nhiều.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Banken / Bänken"
                        ],
                        "translation": "Ở khu trung tâm thành phố, nhiều người làm việc trong các ngân hàng quốc tế, còn trong công viên thành phố, những người về hưu thích ngồi trên những chiếc ghế băng đầy nắng."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 9: Chọn đáp án điền đúng vào ba chỗ trống.\nAm Samstagabend möchten meine Cousine und ich ___ Staatsoper gehen, denn dann singt ein berühmter Tenor ___ Staatsoper. Davor fahren wir noch kurz ___ Alexanderplatz.",
                "options": [
                        "in die / in der / zum",
                        "in der / in der / zum",
                        "in die / in die / zum",
                        "in die / in der / zur"
                ],
                "correct_answer": "in die / in der / zum",
                "explanation": "Động từ 'gehen' chỉ hướng di chuyển vào trong (Wohin?) với 'die Staatsoper' đi với in + Akkusativ → 'in die Staatsoper'; 'singen' chỉ hành động diễn ra tại chỗ (Wo?) đi với in + Dativ → 'in der Staatsoper'; 'der Alexanderplatz' đi với zu + Dativ → 'zu + dem = zum'. Các đáp án có 'in der' sau 'gehen' hoặc 'in die' sau 'singt' sai vì nhầm hướng di chuyển với vị trí; 'zur' sai vì Alexanderplatz là danh từ giống đực.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "in die / in der / zum"
                        ],
                        "translation": "Tối thứ Bảy, chị (em) họ của tôi và tôi muốn đi vào Nhà hát Opera Quốc gia, vì lúc đó một giọng nam cao nổi tiếng sẽ hát trong nhà hát. Trước đó chúng tôi còn ghé nhanh tới Quảng trường Alexander."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 10: Một hướng dẫn viên du lịch nói với đoàn khách. Chọn đáp án điền đúng vào ba chỗ trống.\n‚Wir spazieren jetzt zuerst die Spree ___, gehen dann ___ die alte Holzbrücke und laufen schließlich ___ den dunklen Tunnel zum Schloss.‘",
                "options": [
                        "vorbei / über / in",
                        "über / durch / entlang",
                        "entlang / über / durch",
                        "durch / entlang / über"
                ],
                "correct_answer": "entlang / über / durch",
                "explanation": "Đi dọc theo dòng sông Spree (đặt sau danh từ) dùng 'entlang' ('die Spree entlang'); đi vượt qua trên mặt cầu dùng 'über' ('über die alte Holzbrücke'); đi xuyên qua lòng đường hầm tối ('der Tunnel') dùng 'durch' ('durch den dunklen Tunnel'). Các đáp án khác sai vì giới từ không khớp với từng chặng: đi dọc sông dùng 'entlang', đi qua cầu dùng 'über', đi xuyên đường hầm dùng 'durch'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "entlang / über / durch"
                        ],
                        "translation": "Hướng dẫn viên du lịch nói với các vị khách: 'Bây giờ đầu tiên chúng ta đi dạo dọc theo sông Spree, sau đó đi qua cây cầu gỗ cổ và cuối cùng đi bộ xuyên qua đường hầm tối để tới cung điện.'"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 11: Một gia đình đang du lịch ở München. Chọn đáp án điền đúng vào ba chỗ trống.\nFamilie Schneider ist neu in München. Herr Schneider ___ unbedingt das Deutsche Museum besichtigen, aber seine Kinder sind müde und ___ nicht mehr weit laufen. Deshalb ___ alle jetzt ein Taxi zum Hotel nehmen.",
                "options": [
                        "will / können / müssen",
                        "wollen / können / müssen",
                        "will / kann / müssen",
                        "will / können / muss"
                ],
                "correct_answer": "will / können / müssen",
                "explanation": "Chủ ngữ 'Herr Schneider' (ngôi er số ít) → 'will'; 'seine Kinder' (ngôi sie số nhiều) → 'können'; 'alle' (đại từ làm chủ ngữ số nhiều) → 'müssen'. Các đáp án khác sai vì chia động từ không khớp chủ ngữ: 'wollen' với 'Herr Schneider', 'kann' với 'seine Kinder', 'muss' với 'alle'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "will / können / müssen"
                        ],
                        "translation": "Gia đình Schneider mới đến München. Ông Schneider nhất định muốn tham quan Bảo tàng Đức, nhưng các con của ông đã mỏi chân và không thể đi bộ xa thêm nữa. Vì vậy bây giờ tất cả họ phải bắt một chiếc taxi về khách sạn."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 12: Một người qua đường chỉ đường tới Theater cho bạn, dựa theo bản đồ. Trong câu nào người đó nói SAI hướng so với lộ trình vẽ trên bản đồ?",
                "options": [
                        "Gehen Sie zuerst geradeaus über die erste Kreuzung.",
                        "An der zweiten Kreuzung biegen Sie links ab.",
                        "Danach gehen Sie an der Kirche vorbei, die links von Ihnen liegt.",
                        "Dann biegen Sie noch einmal rechts ab, und das Theater liegt direkt vor Ihnen."
                ],
                "correct_answer": "Danach gehen Sie an der Kirche vorbei, die links von Ihnen liegt.",
                "explanation": "Trên bản đồ, đường đi thẳng qua ngã tư thứ nhất, rẽ trái ở ngã tư thứ hai rồi đi dọc theo đường ngang. Nhà thờ (Kirche) nằm phía trên đường, tức bên PHẢI người đi ('rechts'), nhưng câu này lại nói 'links'. Ba câu còn lại khớp với lộ trình.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Danach gehen Sie an der Kirche vorbei, die links von Ihnen liegt."
                        ],
                        "translation": "Sau đó bạn đi ngang qua nhà thờ, nhà thờ nằm bên trái bạn.",
                        "visual_svg": "map_error_check_1"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 13: Du khách hỏi đường ở trung tâm thành phố. Chọn đáp án điền đúng vào ba chỗ trống.\n‚Entschuldigung, wir suchen ___ neuen Hauptbahnhof.‘ — ‚Gehen Sie einfach an ___ alten Kirche vorbei, dann steht ___ Hauptbahnhof direkt vor Ihnen!‘",
                "options": [
                        "den / der / der",
                        "dem / der / der",
                        "den / die / der",
                        "den / der / den"
                ],
                "correct_answer": "den / der / der",
                "explanation": "1. Động từ 'suchen' đòi hỏi tân ngữ trực tiếp ở Akkusativ; 'der Hauptbahnhof' (giống đực) đổi thành 'den neuen Hauptbahnhof'. 2. Cụm giới từ 'an … vorbei' luôn đi với Dativ; 'die Kirche' (giống cái) đổi thành 'an der alten Kirche vorbei'. 3. Trong mệnh đề 'dann steht ___ Hauptbahnhof', danh từ làm chủ ngữ ở Nominativ nên giữ nguyên mạo từ 'der Hauptbahnhof'. Các đáp án khác sai vì: 'dem' sai vì sau 'suchen' cần Akkusativ; 'die' sai vì 'an … vorbei' cần Dativ; 'den' ở chỗ thứ ba sai vì chủ ngữ của 'steht' ở Nominativ.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "den / der / der"
                        ],
                        "translation": "'Xin lỗi, chúng tôi đang tìm nhà ga trung tâm mới.' — 'Quý vị cứ đi ngang qua nhà thờ cổ, sau đó nhà ga trung tâm sẽ nằm ngay trước mặt quý vị!'"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 14: Một hành khách và một tài xế taxi ở Viên trò chuyện. Chọn đáp án điền đúng vào hai chỗ trống.\nTaxifahrer: Muss ich hier schon abbiegen?\nFahrgast: Nein, nehmen Sie bitte erst die ___ Straße links und halten Sie dann an der ___ Ampel vor dem Theater!",
                "options": [
                        "dritten / zweiten",
                        "dritte / zweiten",
                        "dritte / zweite",
                        "dritter / zweiten"
                ],
                "correct_answer": "dritte / zweiten",
                "explanation": "Số thứ tự đứng sau 'die' (giống cái ở Akkusativ, sau 'nehmen') nhận đuôi -e: 'die dritte Straße'. Đứng sau 'an der' (giống cái ở Dativ) nhận đuôi -en: 'an der zweiten Ampel'. Các đáp án khác sai vì: 'dritten' dùng đuôi -en sau 'die'; 'zweite' dùng đuôi -e sau 'an der'; 'dritter' dùng đuôi -er, không dùng cho danh từ giống cái sau 'die'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "dritte / zweiten"
                        ],
                        "translation": "Tài xế taxi: 'Tôi phải rẽ ngay ở đây à?' — Hành khách: 'Không, trước tiên xin hãy đi vào con đường thứ ba bên trái, rồi dừng lại ở đèn giao thông thứ hai trước nhà hát!'"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 15: Chọn câu có trật tự từ đúng duy nhất.",
                "options": [
                        "Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder Eis essen.",
                        "Zuerst wir wollen den großen Hafen besichtigen, und danach möchten die Kinder Eis essen.",
                        "Zuerst wollen wir den großen Hafen besichtigen, und danach die Kinder möchten Eis essen.",
                        "Zuerst wollen besichtigen wir den großen Hafen, und danach möchten die Kinder Eis essen."
                ],
                "correct_answer": "Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder Eis essen.",
                "explanation": "Khi trạng từ thời gian ('Zuerst', 'danach') đứng đầu câu hoặc đầu mệnh đề, động từ đã chia ('wollen', 'möchten') phải đứng ngay sau nó, còn động từ nguyên mẫu ('besichtigen', 'essen') đứng ở cuối câu. Liên từ 'und' kết nối hai mệnh đề độc lập mà không thay đổi trật tự từ. Các đáp án sai vì: 'Zuerst wir wollen…' đặt 'wir' trước động từ chia; '…und danach die Kinder möchten…' đặt 'die Kinder' trước động từ chia ở mệnh đề sau 'und'; 'Zuerst wollen besichtigen wir…' đặt 'besichtigen' sai chỗ, động từ nguyên mẫu phải đứng ở cuối mệnh đề.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder Eis essen."
                        ],
                        "translation": "Đầu tiên chúng tôi muốn tham quan cảng lớn, và sau đó bọn trẻ muốn ăn kem."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 16: Ông bà của bạn cần đi từ khách sạn tới cung điện Sanssouci vào ngày mai. Chọn đáp án điền đúng vào bốn chỗ trống.\nWie kommen deine Großeltern morgen vom Hotel zum Schloss Sanssouci? — Sie fahren zuerst mit ___ S-Bahn bis ___ Hauptbahnhof und nehmen dort ___ Bus direkt ___ Schloss.",
                "options": [
                        "die / zum / den / zum",
                        "der / zur / den / zum",
                        "der / zum / den / zum",
                        "der / zum / dem / zum"
                ],
                "correct_answer": "der / zum / den / zum",
                "explanation": "1. 'mit' luôn đi với Dativ: 'die S-Bahn' → 'mit der S-Bahn'. 2. 'bis zu' đi với Dativ: 'der Hauptbahnhof' → 'bis zum Hauptbahnhof'. 3. 'nehmen' cần tân ngữ Akkusativ: 'der Bus' → 'nehmen den Bus'. 4. 'zu + Dativ': 'das Schloss' → 'zum Schloss'. Các đáp án khác sai vì: 'die' sau 'mit' sai do 'mit' luôn đi với Dativ; 'zur Hauptbahnhof' sai vì der Hauptbahnhof giống đực; 'dem Bus' sai vì 'nehmen' cần Akkusativ.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der / zum / den / zum"
                        ],
                        "translation": "Ông bà của bạn ngày mai đi từ khách sạn đến Cung điện Sanssouci bằng cách nào? — Đầu tiên ông bà đi bằng tàu điện S-Bahn cho đến nhà ga trung tâm và ở đó bắt xe buýt đi thẳng tới cung điện."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 17: Một tài xế ô tô hỏi bạn cách đi ra sân bay. Chọn câu trả lời vừa hợp logic vừa đúng ngữ pháp.",
                "options": [
                        "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!",
                        "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Hauptbahnhof!",
                        "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach die zweite Ampel rechts zum Flughafen!",
                        "Gehen Sie zu Fuß diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!"
                ],
                "correct_answer": "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!",
                "explanation": "Tài xế đang điều khiển ô tô nên dùng động từ 'Fahren Sie...', đi dọc đường chính ('diese Hauptstraße entlang'), qua trên cây cầu ('über die große Brücke'), sau đèn giao thông thứ hai ('nach der zweiten Ampel' vì nach + Dativ) và đích đến đúng câu hỏi là sân bay ('zum Flughafen'). Các câu còn lại sai vì: một câu chỉ nhầm đích đến là nhà ga trung tâm; một câu sai ngữ pháp 'nach die zweite Ampel'; một câu sai logic thực tế vì bảo người đang lái xe hãy đi bộ ('Gehen Sie zu Fuß').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!"
                        ],
                        "translation": "Hãy lái xe dọc theo con đường chính này, sau đó qua cây cầu lớn, và sau đèn giao thông thứ hai rẽ phải để tới sân bay!"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 18: Đọc bảng thông tin tại nhà ga rồi trả lời câu hỏi.\n‚Vom Hauptbahnhof erreichen Sie die Museumsinsel in 15 Minuten zu Fuß: Gehen Sie durch den Bahnhofspark, über die Friedrichsbrücke und an der Staatsoper vorbei.‘\nKhách tham quan phải làm gì trên quãng đường này?",
                "options": [
                        "Sie müssen vor der Brücke links zum großen Flughafen abbiegen.",
                        "Sie müssen einen Park durchqueren und eine Brücke überqueren.",
                        "Sie müssen mit dem Linienbus direkt in die Staatsoper hineingehen.",
                        "Sie dürfen den schönen Bahnhofspark auf keinen Fall betreten."
                ],
                "correct_answer": "Sie müssen einen Park durchqueren und eine Brücke überqueren.",
                "explanation": "'durch den Bahnhofspark gehen' tương đương với 'einen Park durchqueren' (đi xuyên qua công viên); 'über die Friedrichsbrücke gehen' tương đương với 'eine Brücke überqueren' (băng qua cầu). Các đáp án khác sai vì bảng thông tin không hề yêu cầu rẽ trái ra sân bay, không bảo đi xe buýt vào nhà hát, và cũng không cấm khách bước vào công viên.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Sie müssen einen Park durchqueren und eine Brücke überqueren."
                        ],
                        "translation": "Đọc bảng thông tin tại nhà ga: 'Từ nhà ga trung tâm, quý vị đi bộ 15 phút là tới Đảo Bảo tàng: Hãy đi xuyên qua công viên nhà ga, đi qua cầu Friedrichs và đi ngang qua Nhà hát Opera Quốc gia.' — Khách tham quan phải làm gì trên quãng đường này?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 19: Điền một từ thích hợp vào chỗ trống.\nTourist: Entschuldigung, wie komme ich zum Krankenhaus?\nPassant: Gehen Sie zuerst geradeaus an ___ Bank vorbei und biegen Sie dann links ab!",
                "options": null,
                "correct_answer": "der",
                "explanation": "Danh từ Bank mang giống cái ('die Bank'). Trong cấu trúc 'an + Dativ + vorbei', mạo từ die đổi thành 'der' ('an der Bank vorbei').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der",
                                "dieser",
                                "einer",
                                "jener"
                        ],
                        "translation": "Đầu tiên bạn hãy đi thẳng ngang qua ngân hàng rồi sau đó rẽ trái!",
                        "visual_svg": "map_fill_1"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 20: Điền một từ thích hợp vào chỗ trống.\nFahrgast: Fährt dieser Bus zum Kunstmuseum?\nBusfahrer: Ja, er fährt direkt ___ alten Schloss vorbei und hält dann vor dem Museum.",
                "options": null,
                "correct_answer": "am",
                "explanation": "Danh từ Schloss mang giống trung ('das Schloss'). Đi với cấu trúc 'an + Dativ + vorbei', an + dem gộp thành 'am' ('am alten Schloss vorbei').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "am",
                                "an dem",
                                "an diesem",
                                "an einem"
                        ],
                        "translation": "Chuyến xe buýt này có chạy tới bảo tàng nghệ thuật không? — Có, nó chạy ngang qua ngay cung điện cổ rồi dừng trước bảo tàng.",
                        "visual_svg": "map_fill_2"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 21: Điền một từ thích hợp vào chỗ trống.\nUm zur Museumsinsel zu kommen, müsst ihr zuerst ___ die große Brücke laufen.",
                "options": null,
                "correct_answer": "über",
                "explanation": "Đi vượt qua / băng qua mặt cầu ('die Brücke') dùng giới từ 'über' (+ Akkusativ).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "über",
                                "ueber"
                        ],
                        "translation": "Để đi đến được Đảo Bảo tàng, đầu tiên các bạn phải đi bộ qua cây cầu lớn.",
                        "visual_svg": "quiz_icon_bridge"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 22: Điền một từ thích hợp vào chỗ trống.\nWenn du in die Altstadt willst, musst du zu Fuß ___ das historische Stadttor gehen.",
                "options": null,
                "correct_answer": "durch",
                "explanation": "Đi xuyên qua lòng cổng thành ('das Stadttor') dùng giới từ 'durch' (+ Akkusativ).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "durch"
                        ],
                        "translation": "Nếu bạn muốn vào khu phố cổ, bạn phải đi bộ xuyên qua cổng thành lịch sử.",
                        "visual_svg": "quiz_icon_gate"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 23: Điền một từ thích hợp vào chỗ trống.\nGehen Sie einfach diese breite Straße ___! Nach etwa dreihundert Metern sehen Sie links den Zoo.",
                "options": null,
                "correct_answer": "entlang",
                "explanation": "Từ chỉ hướng đi dọc theo đứng sau danh từ ở Akkusativ ('diese breite Straße') là 'entlang'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "entlang"
                        ],
                        "translation": "Bạn cứ đi dọc theo con đường rộng này! Sau khoảng ba trăm mét bạn sẽ nhìn thấy sở thú ở bên trái.",
                        "visual_svg": "quiz_icon_along"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 24: Điền một từ thích hợp vào chỗ trống.\nFahren Sie mit dem Fahrrad immer geradeaus bis ___ dritten Kreuzung und biegen Sie dort rechts ab!",
                "options": null,
                "correct_answer": "zur",
                "explanation": "Danh từ Kreuzung mang giống cái ('die Kreuzung'). Sau giới từ kép 'bis zu + Dativ', zu + der viết tắt thành 'zur' ('bis zur dritten Kreuzung').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zur",
                                "zu der"
                        ],
                        "translation": "Bạn cứ đạp xe thẳng mãi cho đến ngã tư thứ ba và rẽ phải ở đó!"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 25: Điền một từ thích hợp vào chỗ trống.\nFahrgast: Wie weit fährt die Straßenbahn Linie 4?\nPassant: Sie fährt vom Rathaus durch das Zentrum bis ___ Hafen.",
                "options": null,
                "correct_answer": "zum",
                "explanation": "Danh từ Hafen (cảng biển) mang giống đực ('der Hafen'). Sau 'bis zu + Dativ', zu + dem viết tắt thành 'zum' ('bis zum Hafen').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zum",
                                "zu dem"
                        ],
                        "translation": "Tuyến tàu điện mặt đất số 4 chạy bao xa? — Nó chạy từ tòa thị chính xuyên qua trung tâm cho đến cảng biển."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 26: „Es regnet stark! Komm, wir gehen schnell ___ Einkaufszentrum dort drüben und trinken einen heißen Kakao!“",
                "options": null,
                "correct_answer": "ins",
                "explanation": "Danh từ Einkaufszentrum mang giống trung ('das Einkaufszentrum'). Đi bước vào bên trong ('Wohin?' + Akkusativ) dùng in + das = 'ins'. Cách nói 'zum Einkaufszentrum' (đi tới trung tâm thương mại) cũng đúng ngữ pháp và được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "ins",
                                "in das",
                                "zum",
                                "zu dem"
                        ],
                        "translation": "Trời mưa to quá! Nào, chúng mình đi nhanh vào trong trung tâm thương mại ở đằng kia và uống một cốc ca cao nóng đi!"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 27: „Meine Tante interessiert sich sehr für Kunst, deshalb geht sie heute Nachmittag ___ Alte Nationalgalerie.“",
                "options": null,
                "correct_answer": "in die",
                "explanation": "'Alte Nationalgalerie' mang giống cái ('die'). Đi vào bên trong ('Wohin?' + Akkusativ) dùng 'in die'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "in die"
                        ],
                        "translation": "Cô của tôi rất quan tâm đến nghệ thuật, vì vậy chiều nay cô ấy đi vào Phòng trưng bày Quốc gia Cũ."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 28: „Das Wetter ist heute wunderbar. Gehen wir am Nachmittag mit den Kindern ___ großen Stadtpark oder lieber an den See?“",
                "options": null,
                "correct_answer": "in den",
                "explanation": "Danh từ der Stadtpark mang giống đực. Khi chỉ hướng đi vào bên trong ('Wohin?' + Akkusativ), der đổi thành den → 'in den'. Các cách nói như 'zum großen Stadtpark' hay 'durch den großen Stadtpark' cũng đúng ngữ pháp nên được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "in den",
                                "zum",
                                "zu dem",
                                "durch den"
                        ],
                        "translation": "Thời tiết hôm nay tuyệt đẹp. Chiều nay chúng ta đi cùng bọn trẻ vào công viên lớn của thành phố, hay đi ra hồ thì hơn?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 29: „Mein Onkel fotografiert sehr gern. In Berlin ___ er unbedingt auf den Fernsehturm fahren und die Stadt von oben fotografieren.“",
                "options": null,
                "correct_answer": "will",
                "explanation": "Chủ ngữ 'er' ('mein Onkel') là ngôi thứ 3 số ít; động từ khuyết thiếu wollen biến âm o -> i và không có đuôi thành 'will'. 'möchte' và 'muss' cũng phù hợp với câu này nên được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "will",
                                "möchte",
                                "muss"
                        ],
                        "translation": "Chú của tôi rất thích chụp ảnh. Ở Berlin chú ấy nhất định muốn đi lên Tháp truyền hình và chụp ảnh thành phố từ trên cao."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 30: „Hallo Leon, hallo Mia! Ihr seid schon am Alexanderplatz. Was ___ ihr denn danach noch in der Innenstadt unternehmen?“",
                "options": null,
                "correct_answer": "wollt",
                "explanation": "Với chủ ngữ ngôi thứ 2 số nhiều 'ihr' (các bạn), động từ wollen chia thành 'wollt'. 'möchtet' cũng đúng và được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "wollt",
                                "möchtet"
                        ],
                        "translation": "Chào Leon, chào Mia! Hai bạn đã ở Quảng trường Alexander rồi. Thế sau đó hai bạn còn muốn làm gì ở khu trung tâm thành phố nữa?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 31: „Geh einfach über die kleine Brücke und dann 100 Meter geradeaus! Direkt auf der linken Seite ___ du schon die gelbe Post.“",
                "options": null,
                "correct_answer": "siehst",
                "explanation": "Động từ sehen (nhìn thấy) là động từ mạnh biến âm e -> ie ở ngôi du ('du siehst') và er/sie/es ('er sieht'). Vì chỉ đường cho bạn ở ngôi du, đáp án đúng là 'siehst'. 'findest', 'entdeckst', 'erkennst' cũng hợp nghĩa và được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "siehst",
                                "findest",
                                "entdeckst",
                                "erkennst"
                        ],
                        "translation": "Bạn cứ đi qua cây cầu nhỏ rồi đi thẳng 100 mét! Ngay ở phía bên tay trái bạn sẽ nhìn thấy bưu điện màu vàng."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 32: „Nimm am besten die Buslinie 100! Dieser Bus ___ am Reichstag, am Brandenburger Tor und am Schloss Bellevue vorbei.“",
                "options": null,
                "correct_answer": "fährt",
                "explanation": "Chủ ngữ 'Dieser Bus' là ngôi thứ 3 số ít (er). Động từ tách vorbeifahren tách tiền tố vorbei xuống cuối câu, phần gốc fahren biến âm a -> ä thành 'fährt'. 'kommt' ('kommt … vorbei') cũng đúng và được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "fährt",
                                "faehrt",
                                "kommt"
                        ],
                        "translation": "Tốt nhất bạn hãy đi tuyến xe buýt số 100! Chuyến xe buýt này chạy ngang qua Tòa nhà Quốc hội, Cổng Brandenburg và Cung điện Bellevue."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 33: „Das Wetter in Berlin ist sonnig. Nach dem Mittagessen wollen meine Schwester und ich zwei Stunden auf dem Kurfürstendamm ___.“",
                "options": null,
                "correct_answer": "bummeln",
                "explanation": "Sau động từ khuyết thiếu wollen, động từ chính đứng ở cuối câu ở dạng nguyên mẫu: 'bummeln' (đi dạo phố, tản bộ ngắm cảnh/mua sắm). Các động từ như spazieren, flanieren, schlendern, laufen, gehen, shoppen, einkaufen cũng hợp nghĩa nên được chấp nhận.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "bummeln",
                                "spazieren",
                                "flanieren",
                                "schlendern",
                                "laufen",
                                "gehen",
                                "shoppen",
                                "einkaufen",
                                "spazieren gehen"
                        ],
                        "translation": "Thời tiết ở Berlin nắng đẹp. Sau bữa trưa, chị gái tôi và tôi muốn đi dạo phố hai tiếng đồng hồ trên đại lộ Kurfürstendamm."
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 34: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'nhà ga trung tâm'",
                "options": null,
                "correct_answer": "der Hauptbahnhof",
                "explanation": "Nhà ga trung tâm là danh từ giống đực der Hauptbahnhof (vì der Bahnhof). Hauptbahnhof = Haupt (chính) + Bahnhof (nhà ga), thường viết tắt là Hbf.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "der Hauptbahnhof"
                        ],
                        "translation": "nhà ga trung tâm = der Hauptbahnhof (Hbf)"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 35: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'sân bay'",
                "options": null,
                "correct_answer": "der Flughafen",
                "explanation": "Sân bay là danh từ ghép giống đực der Flughafen (số nhiều: die Flughäfen).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "der Flughafen"
                        ],
                        "translation": "sân bay: der Flughafen"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 36: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'ngã tư / giao lộ'",
                "options": null,
                "correct_answer": "die Kreuzung",
                "explanation": "Ngã tư / giao lộ là danh từ giống cái die Kreuzung (đuôi -ung luôn mang mạo từ die).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "die Kreuzung"
                        ],
                        "translation": "ngã tư / giao lộ: die Kreuzung"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 37: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'đèn giao thông'",
                "options": null,
                "correct_answer": "die Ampel",
                "explanation": "Đèn giao thông là danh từ giống cái die Ampel (số nhiều: die Ampeln).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "die Ampel"
                        ],
                        "translation": "đèn giao thông: die Ampel"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 38: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định): 'Nhà thờ lớn Berlin'",
                "options": null,
                "correct_answer": "der Berliner Dom",
                "explanation": "Nhà thờ lớn Berlin là danh từ giống đực der Berliner Dom.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "der Berliner Dom"
                        ],
                        "translation": "Nhà thờ lớn Berlin: der Berliner Dom"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 39: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định): 'Cổng thành Brandenburg'",
                "options": null,
                "correct_answer": "das Brandenburger Tor",
                "explanation": "Cổng Brandenburg mang giống trung das Brandenburger Tor (vì das Tor).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "das Brandenburger Tor"
                        ],
                        "translation": "Cổng thành Brandenburg: das Brandenburger Tor"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 40: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi ngang qua bệnh viện'",
                "options": null,
                "correct_answer": "am Krankenhaus vorbei",
                "explanation": "Bệnh viện là das Krankenhaus (giống trung). Khi đi với cấu trúc an + Dativ + vorbei, an + dem gộp thành 'am Krankenhaus vorbei'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "am Krankenhaus vorbei",
                                "am Krankenhaus vorbeigehen",
                                "an dem Krankenhaus vorbei",
                                "Gehen Sie am Krankenhaus vorbei"
                        ],
                        "translation": "đi ngang qua bệnh viện: am Krankenhaus vorbei"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 41: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi ngang qua trường đại học'",
                "options": null,
                "correct_answer": "an der Universität vorbei",
                "explanation": "Trường đại học là die Universität (giống cái). Đi với an + Dativ + vorbei đổi die thành der: 'an der Universität vorbei'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "an der Universität vorbei",
                                "an der Universitaet vorbei",
                                "an der Universität vorbeigehen",
                                "Gehen Sie an der Universität vorbei"
                        ],
                        "translation": "đi ngang qua trường đại học: an der Universität vorbei"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 42: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi xuyên qua công viên'",
                "options": null,
                "correct_answer": "durch den Park",
                "explanation": "Công viên là der Park (giống đực). Đi xuyên qua dùng durch + Akkusativ -> 'durch den Park'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "durch den Park",
                                "durch den Park gehen",
                                "durch den Park laufen",
                                "Gehen Sie durch den Park"
                        ],
                        "translation": "đi xuyên qua công viên: durch den Park"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 43: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi băng qua ngã tư'",
                "options": null,
                "correct_answer": "über die Kreuzung",
                "explanation": "Ngã tư là die Kreuzung (giống cái). Đi băng qua dùng über + Akkusativ -> 'über die Kreuzung'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "über die Kreuzung",
                                "ueber die Kreuzung",
                                "über die Kreuzung gehen",
                                "Gehen Sie über die Kreuzung"
                        ],
                        "translation": "đi băng qua ngã tư: über die Kreuzung"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 44: Dịch cụm chỉ đường sau sang tiếng Đức (dùng ngôi trang trọng Sie): 'Ngài hãy rẽ trái ở con đường thứ ba!'",
                "options": null,
                "correct_answer": "Gehen Sie die dritte Straße links!",
                "explanation": "Con đường thứ ba bên trái là 'die dritte Straße links'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie die dritte Straße links!",
                                "Gehen Sie die dritte Straße links",
                                "Gehen Sie die 3. Straße links!",
                                "Gehen Sie die 3. Straße links",
                                "Fahren Sie die dritte Straße links!",
                                "Fahren Sie die dritte Straße links",
                                "Biegen Sie die dritte Straße links ab!",
                                "Biegen Sie die dritte Straße links ab"
                        ],
                        "translation": "Ngài hãy rẽ trái ở con đường thứ ba: Gehen Sie die dritte Straße links!"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 45: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi cho đến nhà ga'",
                "options": null,
                "correct_answer": "bis zum Bahnhof",
                "explanation": "Nhà ga là der Bahnhof (giống đực). Đi cho đến nhà ga dùng bis zu + Dativ -> 'bis zum Bahnhof'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "bis zum Bahnhof",
                                "bis zum Bahnhof gehen",
                                "Gehen Sie bis zum Bahnhof"
                        ],
                        "translation": "đi cho đến nhà ga: bis zum Bahnhof"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 46: Dịch sang tiếng Việt: „die Bahnhöfe und die Flughäfen“",
                "options": null,
                "correct_answer": "các nhà ga và các sân bay",
                "explanation": "Dạng số nhiều của der Bahnhof (die Bahnhöfe) và der Flughafen (die Flughäfen).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "các nhà ga và các sân bay",
                                "những nhà ga và những sân bay",
                                "nhà ga và sân bay",
                                "các nhà ga và sân bay"
                        ],
                        "translation": "các nhà ga và các sân bay"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 47: Dịch sang tiếng Việt: „die alten Schlösser und die modernen Einkaufszentren“",
                "options": null,
                "correct_answer": "những lâu đài cổ và những trung tâm thương mại hiện đại",
                "explanation": "die Schlösser = những lâu đài/cung điện; die Einkaufszentren = những trung tâm thương mại.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "những lâu đài cổ và những trung tâm thương mại hiện đại",
                                "các lâu đài cổ và các trung tâm thương mại hiện đại",
                                "các cung điện cổ và các trung tâm thương mại hiện đại",
                                "những lâu đài cổ và trung tâm thương mại hiện đại"
                        ],
                        "translation": "những lâu đài cổ và những trung tâm thương mại hiện đại"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 48: Dịch sang tiếng Việt: „am Supermarkt und an der Post vorbeigehen“",
                "options": null,
                "correct_answer": "đi ngang qua siêu thị và bưu điện",
                "explanation": "Cấu trúc an + Dativ + vorbeigehen với der Supermarkt (am) và die Post (an der).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "đi ngang qua siêu thị và bưu điện",
                                "đi bộ ngang qua siêu thị và bưu điện",
                                "đi ngang qua siêu thị và qua bưu điện"
                        ],
                        "translation": "đi ngang qua siêu thị và bưu điện"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 49: Dịch sang tiếng Việt: „durch das mittelalterliche Stadttor laufen“",
                "options": null,
                "correct_answer": "đi bộ xuyên qua cổng thành thời trung cổ",
                "explanation": "durch das Stadttor = xuyên qua cổng thành (durch + Akkusativ); mittelalterlich = thuộc thời Trung cổ; laufen = đi bộ.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "đi bộ xuyên qua cổng thành thời trung cổ",
                                "chạy xuyên qua cổng thành trung cổ",
                                "đi xuyên qua cổng thành cổ",
                                "đi xuyên qua cổng thành thời trung cổ",
                                "chạy qua cổng thành thời trung cổ"
                        ],
                        "translation": "đi bộ xuyên qua cổng thành thời trung cổ"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 50: Dịch sang tiếng Việt: „den malerischen Fluss entlangspazieren“",
                "options": null,
                "correct_answer": "đi dạo dọc theo dòng sông thơ mộng",
                "explanation": "den Fluss entlangspazieren = đi dạo dọc theo con sông (entlang đứng sau danh từ + Akkusativ); malerisch = đẹp như tranh, thơ mộng.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "đi dạo dọc theo dòng sông thơ mộng",
                                "tản bộ dọc theo con sông đẹp như tranh",
                                "đi dạo dọc bờ sông thơ mộng",
                                "tản bộ dọc theo dòng sông thơ mộng",
                                "đi dạo dọc theo con sông thơ mộng"
                        ],
                        "translation": "đi dạo dọc theo dòng sông thơ mộng"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 51: Dịch sang tiếng Việt: „bis zur dritten Ampel geradeaus fahren“",
                "options": null,
                "correct_answer": "lái xe đi thẳng cho đến đèn giao thông thứ ba",
                "explanation": "bis zur dritten Ampel = cho đến đèn giao thông thứ ba. 'bis zu' đi với Dativ: zu + der = zur (die Ampel giống cái); số thứ tự sau 'zur' có đuôi -en: 'dritten'.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "lái xe đi thẳng cho đến đèn giao thông thứ ba",
                                "chạy thẳng tới cột đèn giao thông thứ ba",
                                "đi xe thẳng đến đèn giao thông thứ 3",
                                "chạy thẳng cho đến đèn giao thông thứ ba",
                                "đi thẳng cho đến đèn giao thông thứ ba"
                        ],
                        "translation": "lái xe đi thẳng cho đến đèn giao thông thứ ba"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 52: Dịch sang tiếng Việt: „über die breite Brücke in die Neustadt gehen“",
                "options": null,
                "correct_answer": "đi qua cây cầu rộng vào khu phố mới",
                "explanation": "über die breite Brücke = qua cây cầu rộng (über + Akkusativ); in die Neustadt = vào khu phố mới. 'in die' + Akkusativ trả lời 'Wohin?' nên chỉ hướng đi vào, không phải vị trí 'ở trong' (vị trí là 'in der Neustadt').",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "đi qua cây cầu rộng vào khu phố mới",
                                "đi bộ qua cây cầu rộng vào khu đô thị mới",
                                "băng qua cây cầu rộng vào khu phố mới"
                        ],
                        "translation": "đi qua cây cầu rộng vào khu phố mới"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 53: Dịch sang tiếng Việt: „eine zweistündige Stadtrundfahrt mit dem Doppeldeckerbus machen“",
                "options": null,
                "correct_answer": "thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng",
                "explanation": "eine Stadtrundfahrt machen = thực hiện chuyến tham quan vòng quanh thành phố; der Doppeldeckerbus = xe buýt 2 tầng.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng",
                                "đi tham quan thành phố 2 tiếng bằng xe buýt 2 tầng",
                                "đi tham quan vòng quanh thành phố 2 tiếng bằng xe buýt hai tầng",
                                "thực hiện chuyến tham quan thành phố hai tiếng bằng xe buýt hai tầng"
                        ],
                        "translation": "thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 54: Dịch sang tiếng Việt: „an der nächsten Kreuzung links abbiegen“",
                "options": null,
                "correct_answer": "rẽ trái ở ngã tư tiếp theo",
                "explanation": "an der nächsten Kreuzung = tại ngã tư tiếp theo (nächst- = gần nhất, tiếp theo; die Kreuzung giống cái, Dativ nên 'an der' + đuôi -en); links abbiegen = rẽ trái.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "rẽ trái ở ngã tư tiếp theo",
                                "quẹo trái tại giao lộ kế tiếp",
                                "rẽ trái ở ngã tư kế tiếp",
                                "quẹo trái ở ngã tư tiếp theo"
                        ],
                        "translation": "rẽ trái ở ngã tư tiếp theo"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 55: Dịch sang tiếng Việt: „den Fernsehturm am Alexanderplatz besichtigen wollen“",
                "options": null,
                "correct_answer": "muốn tham quan Tháp truyền hình ở quảng trường Alexander",
                "explanation": "besichtigen = tham quan; wollen = muốn.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "muốn tham quan Tháp truyền hình ở quảng trường Alexander",
                                "muốn đi xem Tháp truyền hình tại quảng trường Alexander",
                                "muốn tham quan tháp truyền hình ở quảng trường Alexander"
                        ],
                        "translation": "muốn tham quan Tháp truyền hình ở quảng trường Alexander"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 56: Dịch sang tiếng Việt: „Entschuldigen Sie bitte, wo geht es hier zum Reichstag?“",
                "options": null,
                "correct_answer": "Xin lỗi quý vị, từ đây đi lối nào để tới Tòa nhà Quốc hội ạ?",
                "explanation": "Entschuldigen Sie bitte = xin lỗi, làm ơn (trang trọng với Sie); 'Wo geht es hier zum ...?' = từ đây đi lối nào đến ...?; zum = zu + dem (der Reichstag); Reichstag = tòa nhà Quốc hội Đức.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Xin lỗi quý vị, từ đây đi lối nào để tới Tòa nhà Quốc hội ạ?",
                                "Xin lỗi Ngài, ở đây đi lối nào để tới Tòa nhà Quốc hội vậy?",
                                "Cho tôi xin lỗi, đường nào đi đến Tòa nhà Quốc hội thế ạ?",
                                "Xin lỗi, đi đến Tòa nhà Quốc hội theo hướng nào?",
                                "Xin lỗi, đi lối nào để tới Tòa nhà Quốc hội?"
                        ],
                        "translation": "Xin lỗi quý vị, từ đây đi lối nào để tới Tòa nhà Quốc hội ạ?"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 57: Dịch sang tiếng Việt: „Gegenüber vom Bahnhof sehen Sie das große Hotel.“",
                "options": null,
                "correct_answer": "Đối diện nhà ga, quý vị sẽ nhìn thấy khách sạn lớn.",
                "explanation": "gegenüber von + Dativ = đối diện với...; vom = von dem (der Bahnhof); sehen Sie = quý vị thấy (Sie trang trọng); das große Hotel = khách sạn lớn.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Đối diện nhà ga, quý vị sẽ nhìn thấy khách sạn lớn.",
                                "Đối diện với nhà ga Ngài sẽ nhìn thấy khách sạn lớn.",
                                "Ở phía đối diện nhà ga bạn sẽ thấy khách sạn lớn.",
                                "Đối diện với nhà ga bạn sẽ nhìn thấy khách sạn lớn."
                        ],
                        "translation": "Đối diện nhà ga, quý vị sẽ nhìn thấy khách sạn lớn."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 58: Nối tình huống (cột trái) với câu hỏi đường phù hợp (cột phải).",
                "options": null,
                "correct_answer": "Bạn cần mua thuốc và hỏi xem quanh đây có hiệu thuốc nào không. = Entschuldigung, wo ist hier eine Apotheke? | Bạn nói với người qua đường rằng bạn đang tìm nhà ga trung tâm. = Entschuldigung, ich suche den Hauptbahnhof. | Bạn hỏi cách đi đến Cổng Brandenburg. = Entschuldigung, wie komme ich zum Brandenburger Tor? | Bạn hỏi lối vào bảo tàng thành phố. = Entschuldigung, wo geht es hier ins Stadtmuseum?",
                "explanation": "1. 'Wo ist …?' hỏi vị trí; 'sein' đi với Nominativ nên 'eine Apotheke'. 2. 'suchen' đòi Akkusativ: der Hauptbahnhof → 'den Hauptbahnhof'. 3. 'wie komme ich' đi với zu + Dativ: zu + dem = 'zum Brandenburger Tor'. 4. 'Wo geht es hier ins …?' dùng in + Akkusativ khi vào bên trong một tòa nhà: in + das = 'ins Stadtmuseum'.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Bạn cần mua thuốc và hỏi xem quanh đây có hiệu thuốc nào không.",
                                        "right": "Entschuldigung, wo ist hier eine Apotheke?"
                                },
                                {
                                        "left": "Bạn nói với người qua đường rằng bạn đang tìm nhà ga trung tâm.",
                                        "right": "Entschuldigung, ich suche den Hauptbahnhof."
                                },
                                {
                                        "left": "Bạn hỏi cách đi đến Cổng Brandenburg.",
                                        "right": "Entschuldigung, wie komme ich zum Brandenburger Tor?"
                                },
                                {
                                        "left": "Bạn hỏi lối vào bảo tàng thành phố.",
                                        "right": "Entschuldigung, wo geht es hier ins Stadtmuseum?"
                                }
                        ],
                        "translation": "1. Xin lỗi, quanh đây có hiệu thuốc nào không?\n2. Xin lỗi, tôi đang tìm nhà ga trung tâm.\n3. Xin lỗi, làm thế nào tôi đến được Cổng Brandenburg?\n4. Xin lỗi, lối nào ở đây dẫn vào bảo tàng thành phố?"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 59: Nối phần đầu câu (cột trái) với phần còn lại (cột phải) để được câu chỉ đường đúng ngữ pháp.",
                "options": null,
                "correct_answer": "Bitte gehen Sie an ... = der alten Kirche und am Rathaus vorbei! | Bitte laufen Sie durch ... = den grünen Stadtpark und das große Stadttor! | Bitte fahren Sie über ... = die neue Brücke und den Marktplatz! | Bitte spazieren Sie ... = die Friedrichstraße und den Kanal entlang!",
                "explanation": "Quy tắc giới từ không gian: 1. an + Dativ + vorbei (an der alten Kirche, am Rathaus vorbei). 2. durch + Akkusativ (durch den Stadtpark, durch das Stadttor). 3. über + Akkusativ (über die Brücke, über den Marktplatz). 4. Danh từ ở Akkusativ + entlang (die Friedrichstraße entlang, den Kanal entlang).",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Bitte gehen Sie an ...",
                                        "right": "der alten Kirche und am Rathaus vorbei!"
                                },
                                {
                                        "left": "Bitte laufen Sie durch ...",
                                        "right": "den grünen Stadtpark und das große Stadttor!"
                                },
                                {
                                        "left": "Bitte fahren Sie über ...",
                                        "right": "die neue Brücke und den Marktplatz!"
                                },
                                {
                                        "left": "Bitte spazieren Sie ...",
                                        "right": "die Friedrichstraße und den Kanal entlang!"
                                }
                        ],
                        "translation": "1. Xin quý vị hãy đi ngang qua nhà thờ cổ và tòa thị chính!\n2. Xin quý vị hãy đi bộ xuyên qua công viên thành phố xanh tươi và cổng thành lớn!\n3. Xin quý vị hãy lái xe qua cây cầu mới và quảng trường chợ!\n4. Xin quý vị hãy đi dạo dọc theo phố Friedrich và dọc theo con kênh!"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 60: Nối câu chỉ đường tiếng Việt (cột trái) với câu tiếng Đức tương ứng (cột phải).",
                "options": null,
                "correct_answer": "Lái xe đi thẳng cho đến sân bay. = Fahren Sie geradeaus bis zum Flughafen! | Đi thẳng cho đến ngã tư. = Gehen Sie geradeaus bis zur Kreuzung! | Đi bộ thẳng cho đến cổng thành. = Laufen Sie geradeaus bis zum Stadttor! | Đi thẳng cho đến Nhà hát Opera. = Gehen Sie geradeaus bis zur Staatsoper!",
                "explanation": "'bis' đi với zu + Dativ. der Flughafen → zu + dem = 'zum Flughafen'; die Kreuzung → zu + der = 'zur Kreuzung'; das Stadttor → 'zum Stadttor'; die Staatsoper → 'zur Staatsoper'.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Lái xe đi thẳng cho đến sân bay.",
                                        "right": "Fahren Sie geradeaus bis zum Flughafen!"
                                },
                                {
                                        "left": "Đi thẳng cho đến ngã tư.",
                                        "right": "Gehen Sie geradeaus bis zur Kreuzung!"
                                },
                                {
                                        "left": "Đi bộ thẳng cho đến cổng thành.",
                                        "right": "Laufen Sie geradeaus bis zum Stadttor!"
                                },
                                {
                                        "left": "Đi thẳng cho đến Nhà hát Opera.",
                                        "right": "Gehen Sie geradeaus bis zur Staatsoper!"
                                }
                        ],
                        "translation": ""
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 61: Nối câu có chỗ trống (cột trái) với từ cần điền (cột phải).",
                "options": null,
                "correct_answer": "Am Nachmittag gehen wir ___ Zoo. = in den | Heute Abend gehen wir ___ Disko. = in die | Am Wochenende gehen wir ___ Einkaufszentrum. = ins | Wir hören ein Konzert ___ Berliner Dom. = im",
                "explanation": "Hỏi 'Wohin?' (di chuyển vào trong) dùng in + Akkusativ: der Zoo → 'in den Zoo'; die Disko → 'in die Disko'; das Einkaufszentrum → in + das = 'ins'. Hỏi 'Wo?' (hành động diễn ra bên trong) dùng in + Dativ: der Berliner Dom → in + dem = 'im Berliner Dom'.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Am Nachmittag gehen wir ___ Zoo.",
                                        "right": "in den"
                                },
                                {
                                        "left": "Heute Abend gehen wir ___ Disko.",
                                        "right": "in die"
                                },
                                {
                                        "left": "Am Wochenende gehen wir ___ Einkaufszentrum.",
                                        "right": "ins"
                                },
                                {
                                        "left": "Wir hören ein Konzert ___ Berliner Dom.",
                                        "right": "im"
                                }
                        ],
                        "translation": "1. Buổi chiều chúng tôi đi đến sở thú.\n2. Tối nay chúng tôi đi đến vũ trường.\n3. Cuối tuần chúng tôi đi đến trung tâm thương mại.\n4. Chúng tôi nghe hòa nhạc trong Nhà thờ lớn Berlin."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 62: Nối đối tượng giao tiếp (cột trái) với lời chỉ đường phù hợp (cột phải).",
                "options": null,
                "correct_answer": "Bạn chỉ đường lịch sự cho một bà cụ lớn tuổi đi đến cột đèn giao thông. = Gehen Sie bitte die erste Straße rechts und dann bis zur Ampel! | Bạn chỉ đường cho một người bạn thân đi bộ qua quảng trường. = Geh bitte die erste Straße rechts und lauf dann über den Platz! | Bạn chỉ đường cho hai bạn cùng lớp đi bằng xe buýt. = Geht bitte die erste Straße rechts und fahrt dann mit dem Bus! | Bạn rủ cả nhóm, gồm cả bạn, cùng đi vào nhà hàng. = Gehen wir zuerst durch den Park und danach ins Restaurant!",
                "explanation": "Với 'Sie' (bà cụ lớn tuổi): động từ đứng đầu câu, theo sau là Sie ('Gehen Sie…'). Với 'du' (1 người bạn thân): bỏ đuôi -st và bỏ đại từ ('Geh…', 'Lauf…'). Với 'ihr' (2 bạn cùng lớp): giữ đuôi -t và bỏ đại từ ('Geht…', 'Fahrt…'). Với 'wir' (cả nhóm gồm bạn): động từ đứng đầu, theo sau là wir ('Gehen wir…'), dùng để rủ cùng làm.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Bạn chỉ đường lịch sự cho một bà cụ lớn tuổi đi đến cột đèn giao thông.",
                                        "right": "Gehen Sie bitte die erste Straße rechts und dann bis zur Ampel!"
                                },
                                {
                                        "left": "Bạn chỉ đường cho một người bạn thân đi bộ qua quảng trường.",
                                        "right": "Geh bitte die erste Straße rechts und lauf dann über den Platz!"
                                },
                                {
                                        "left": "Bạn chỉ đường cho hai bạn cùng lớp đi bằng xe buýt.",
                                        "right": "Geht bitte die erste Straße rechts und fahrt dann mit dem Bus!"
                                },
                                {
                                        "left": "Bạn rủ cả nhóm, gồm cả bạn, cùng đi vào nhà hàng.",
                                        "right": "Gehen wir zuerst durch den Park und danach ins Restaurant!"
                                }
                        ],
                        "translation": "1. Xin quý vị hãy đi con đường thứ nhất bên phải rồi đi tiếp đến đèn giao thông!\n2. Bạn hãy đi con đường thứ nhất bên phải rồi đi bộ qua quảng trường nhé!\n3. Các bạn hãy đi con đường thứ nhất bên phải rồi đi tiếp bằng xe buýt!\n4. Đầu tiên chúng ta hãy đi xuyên qua công viên rồi vào nhà hàng nhé!"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 63: Nối chủ ngữ (cột trái) với phần còn lại của câu (cột phải).",
                "options": null,
                "correct_answer": "Meine Cousine Lena = will nächstes Jahr an der Humboldt-Universität Medizin studieren. | Mein Bruder und ich = wollen morgen Vormittag eine Schifffahrt auf der Spree machen. | Du = musst an der dritten Kreuzung links abbiegen und vor der Bank halten. | Ihr = könnt vom Alexanderplatz zu Fuß bis zur Museumsinsel gehen.",
                "explanation": "Chia Modalverben theo các ngôi: 1. Ngôi thứ 3 số ít (sie = Lena) của wollen chia là 'will'. 2. Chủ ngữ ghép 'Mein Bruder und ich' = wir chia wollen là 'wollen'. 3. Ngôi du chia müssen là 'musst'. 4. Ngôi ihr chia können là 'könnt'.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Meine Cousine Lena",
                                        "right": "will nächstes Jahr an der Humboldt-Universität Medizin studieren."
                                },
                                {
                                        "left": "Mein Bruder und ich",
                                        "right": "wollen morgen Vormittag eine Schifffahrt auf der Spree machen."
                                },
                                {
                                        "left": "Du",
                                        "right": "musst an der dritten Kreuzung links abbiegen und vor der Bank halten."
                                },
                                {
                                        "left": "Ihr",
                                        "right": "könnt vom Alexanderplatz zu Fuß bis zur Museumsinsel gehen."
                                }
                        ],
                        "translation": "1. Chị (em) họ Lena của tôi muốn học ngành y tại Đại học Humboldt vào năm tới.\n2. Anh (em) trai tôi và tôi muốn đi du thuyền trên sông Spree vào sáng mai.\n3. Bạn phải rẽ trái ở ngã tư thứ ba và dừng lại trước ngân hàng.\n4. Các bạn có thể đi bộ từ Quảng trường Alexander đến Đảo Bảo tàng."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 64: Nối cụm danh từ địa điểm ở số nhiều (cột trái) với cách viết tiếng Đức chuẩn (cột phải).",
                "options": null,
                "correct_answer": "các nhà ga / các cảng biển / các khu chợ = die Bahnhöfe / die Häfen / die Märkte | các lâu đài / các bệnh viện / các tòa thị chính = die Schlösser / die Krankenhäuser / die Rathäuser | các trung tâm thương mại / các viện bảo tàng = die Einkaufszentren / die Museen | những cây cầu / những ngã tư / những cột đèn giao thông = die Brücken / die Kreuzungen / die Ampeln",
                "explanation": "Quy tắc chuyển đổi từ số ít sang số nhiều của danh từ chỉ địa điểm: 1. Nhóm danh từ giống đực thêm Umlaut và đuôi -e: der Bahnhof -> die Bahnhöfe, der Hafen -> die Häfen, der Markt -> die Märkte. 2. Nhóm danh từ giống trung tận cùng bằng -haus/-schloss thêm Umlaut và đuôi -er: das Schloss -> die Schlösser, das Krankenhaus -> die Krankenhäuser, das Rathaus -> die Rathäuser. 3. Nhóm danh từ tận cùng bằng đuôi -um đổi -um thành -en: das Einkaufszentrum -> die Einkaufszentren, das Museum -> die Museen. 4. Nhóm danh từ giống cái thêm đuôi -n hoặc -en: die Brücke -> die Brücken, die Kreuzung -> die Kreuzungen, die Ampel -> die Ampeln.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "các nhà ga / các cảng biển / các khu chợ",
                                        "right": "die Bahnhöfe / die Häfen / die Märkte"
                                },
                                {
                                        "left": "các lâu đài / các bệnh viện / các tòa thị chính",
                                        "right": "die Schlösser / die Krankenhäuser / die Rathäuser"
                                },
                                {
                                        "left": "các trung tâm thương mại / các viện bảo tàng",
                                        "right": "die Einkaufszentren / die Museen"
                                },
                                {
                                        "left": "những cây cầu / những ngã tư / những cột đèn giao thông",
                                        "right": "die Brücken / die Kreuzungen / die Ampeln"
                                }
                        ],
                        "translation": ""
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 65: Ghép địa danh tại Berlin (cột trái) với hoạt động đặc trưng phù hợp ngữ cảnh (cột phải).",
                "options": null,
                "correct_answer": "Auf dem Fernsehturm am Alexanderplatz = kann man ganz Berlin von oben sehen. | Auf der Museumsinsel und in der Alten Nationalgalerie = wollen die Touristen berühmte Kunstwerke besichtigen. | Auf der langen Friedrichstraße = möchten viele Besucher am Nachmittag bummeln und einkaufen. | Vor dem Brandenburger Tor und dem Reichstag = machen die Reisegruppen immer viele Erinnerungsfotos.",
                "explanation": "Phân tích ngữ cảnh địa danh Berlin và cấu trúc ngữ pháp: 1. 'Auf dem Fernsehturm' (trên Tháp truyền hình - der Fernsehturm ở Dativ) -> ngắm toàn cảnh Berlin từ trên cao ('kann man ganz Berlin von oben sehen'). 2. 'Auf der Museumsinsel und in der Alten Nationalgalerie' (die Insel & die Galerie ở Dativ) -> trung tâm bảo tàng nghệ thuật nên du khách muốn tham quan tác phẩm nổi tiếng ('berühmte Kunstwerke besichtigen'). 3. 'Auf der langen Friedrichstraße' (die Straße ở Dativ) -> đại lộ thương mại sầm uất nên khách muốn đi dạo và mua sắm ('bummeln und einkaufen'). 4. 'Vor dem Brandenburger Tor und dem Reichstag' (das Tor & der Reichstag ở Dativ) -> biểu tượng lịch sử ngoài trời để chụp ảnh kỷ niệm ('Erinnerungsfotos machen'). Lưu ý: Khi cụm giới từ chỉ nơi chốn đứng đầu câu (vị trí số 1), động từ chia theo ngôi đứng ngay ở vị trí số 2.",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Auf dem Fernsehturm am Alexanderplatz",
                                        "right": "kann man ganz Berlin von oben sehen."
                                },
                                {
                                        "left": "Auf der Museumsinsel und in der Alten Nationalgalerie",
                                        "right": "wollen die Touristen berühmte Kunstwerke besichtigen."
                                },
                                {
                                        "left": "Auf der langen Friedrichstraße",
                                        "right": "möchten viele Besucher am Nachmittag bummeln und einkaufen."
                                },
                                {
                                        "left": "Vor dem Brandenburger Tor und dem Reichstag",
                                        "right": "machen die Reisegruppen immer viele Erinnerungsfotos."
                                }
                        ],
                        "translation": "1. Trên Tháp truyền hình ở Quảng trường Alexander, người ta có thể nhìn thấy toàn cảnh Berlin từ trên cao.\n2. Trên Đảo Bảo tàng và trong Phòng trưng bày Quốc gia Cũ, du khách muốn tham quan các tác phẩm nghệ thuật nổi tiếng.\n3. Trên phố Friedrich dài, nhiều khách tham quan muốn đi dạo và mua sắm vào buổi chiều.\n4. Trước Cổng Brandenburg và Tòa nhà Quốc hội, các đoàn du lịch luôn chụp rất nhiều ảnh kỷ niệm."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 66: Nối thứ tự các bước (cột trái) với chỉ dẫn tương ứng (cột phải) để tạo thành lộ trình hợp lý từ Quảng trường nhà ga (Bahnhofsvorplatz) đến Khách sạn (Hotel):",
                "options": null,
                "correct_answer": "Schritt 1: Zuerst = gehen Sie vom Bahnhofsvorplatz geradeaus die Kaiserstraße entlang. | Schritt 2: Dann = laufen Sie über die kleine Brücke und am Stadtpark vorbei. | Schritt 3: Danach = biegen Sie nach dem Stadtpark an der zweiten Kreuzung links ab. | Schritt 4: Zum Schluss = sehen Sie direkt rechts nach der Ampel Ihr Hotel.",
                "explanation": "Cách suy luận thứ tự lộ trình dựa vào từ khóa liên kết (Domino-Logik): Bước 1 (Zuerst) phải bắt đầu từ điểm xuất phát 'vom Bahnhofsvorplatz' (từ quảng trường nhà ga) đi dọc theo phố Kaiserstraße. Bước 2 (Dann) đi qua cầu nhỏ và đi ngang qua công viên 'am Stadtpark vorbei' (giới thiệu mốc công viên). Bước 3 (Danach) nối tiếp mốc vừa đi qua bằng cụm 'nach dem Stadtpark' (sau khi qua công viên) thì rẽ trái ở ngã tư thứ hai. Bước 4 (Zum Schluss) kết thúc tại điểm đích 'sehen Sie ... Ihr Hotel' (nhìn thấy khách sạn của quý vị ngay bên phải sau đèn giao thông).",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Schritt 1: Zuerst",
                                        "right": "gehen Sie vom Bahnhofsvorplatz geradeaus die Kaiserstraße entlang."
                                },
                                {
                                        "left": "Schritt 2: Dann",
                                        "right": "laufen Sie über die kleine Brücke und am Stadtpark vorbei."
                                },
                                {
                                        "left": "Schritt 3: Danach",
                                        "right": "biegen Sie nach dem Stadtpark an der zweiten Kreuzung links ab."
                                },
                                {
                                        "left": "Schritt 4: Zum Schluss",
                                        "right": "sehen Sie direkt rechts nach der Ampel Ihr Hotel."
                                }
                        ],
                        "translation": "1. Trước tiên, quý vị đi thẳng từ quảng trường trước nhà ga dọc theo phố Kaiser.\n2. Sau đó, quý vị đi bộ qua cây cầu nhỏ và đi ngang qua công viên thành phố.\n3. Tiếp theo, sau công viên, quý vị rẽ trái ở ngã tư thứ hai.\n4. Cuối cùng, ngay bên phải sau đèn giao thông, quý vị sẽ thấy khách sạn của mình."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 67: Nối câu hỏi (cột trái) với câu trả lời đúng ngữ pháp (cột phải).",
                "options": null,
                "correct_answer": "Wo wartet der Reiseleiter auf die Gruppe? = Direkt vor dem Brandenburger Tor neben der Information. | Wohin geht die Reisegruppe jetzt? = In das Berliner Stadtmuseum und über die Schlossbrücke. | Wo hält der Sightseeing-Bus für eine Pause? = Auf dem großen Parkplatz hinter der Staatsoper. | Wohin fährt der Sightseeing-Bus danach? = Durch das alte Stadttor in den grünen Tiergarten.",
                "explanation": "Quy tắc phân biệt vị trí tĩnh 'Wo?' (+ Cách 3 Dativ) và hướng di chuyển 'Wohin?' (+ Cách 4 Akkusativ): 1. Câu 1 & Câu 3 hỏi 'Wo?' (đợi ở đâu / dừng ở đâu -> không di chuyển): bắt buộc dùng giới từ đi với Dativ ('vor dem Brandenburger Tor', 'neben der Information', 'auf dem großen Parkplatz', 'hinter der Staatsoper'). 2. Câu 2 & Câu 4 hỏi 'Wohin?' (đi đâu / chạy đi đâu -> có sự di chuyển đổi vị trí): bắt buộc dùng giới từ đi với Akkusativ ('in das Stadtmuseum', 'über die Schlossbrücke', 'durch das alte Stadttor', 'in den grünen Tiergarten' - der Tiergarten đổi thành den).",
                "exp_reward": 30,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Wo wartet der Reiseleiter auf die Gruppe?",
                                        "right": "Direkt vor dem Brandenburger Tor neben der Information."
                                },
                                {
                                        "left": "Wohin geht die Reisegruppe jetzt?",
                                        "right": "In das Berliner Stadtmuseum und über die Schlossbrücke."
                                },
                                {
                                        "left": "Wo hält der Sightseeing-Bus für eine Pause?",
                                        "right": "Auf dem großen Parkplatz hinter der Staatsoper."
                                },
                                {
                                        "left": "Wohin fährt der Sightseeing-Bus danach?",
                                        "right": "Durch das alte Stadttor in den grünen Tiergarten."
                                }
                        ],
                        "translation": "1. 'Hướng dẫn viên du lịch đợi đoàn ở đâu?' — 'Ngay phía trước Cổng Brandenburg bên cạnh quầy thông tin.'\n2. 'Bây giờ đoàn du lịch đi đâu?' — 'Đi vào Bảo tàng thành phố Berlin và đi qua cầu Schlossbrücke.'\n3. 'Xe buýt tham quan dừng nghỉ giải lao ở đâu?' — 'Ở trên bãi đỗ xe lớn phía sau Nhà hát Opera Quốc gia.'\n4. 'Sau đó xe buýt tham quan chạy đi đâu?' — 'Chạy xuyên qua cổng thành cổ đi vào công viên Tiergarten xanh mát.'"
                }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 68: Hoàn thành lời chỉ đường khớp với lộ trình trên bản đồ bằng cách điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Lauf zuerst [1] den Park und geh dann an [2] Kirche vorbei bis zum Bahnhof!'",
            "options": null,
            "correct_answer": "durch / der",
            "explanation": "Đi xuyên qua 'der Park' dùng 'durch' ('durch den Park'). Đi ngang qua 'die Kirche' dùng 'an + Dativ + vorbei' -> 'an der Kirche vorbei'. Các từ khác cũng đúng ngữ pháp như 'dieser', 'jener', 'einer' được chấp nhận ở ô 2.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "durch"
                ],
                "slot2_accepted": [
                    "der",
                    "dieser",
                    "jener",
                    "einer"
                ],
                "accepted_answers": [
                    "durch / der",
                    "durch/der",
                    "durch / dieser",
                    "durch/dieser",
                    "durch / jener",
                    "durch/jener",
                    "durch / einer",
                    "durch/einer"
                ],
                "translation": "Đầu tiên bạn hãy đi xuyên qua công viên, rồi đi ngang qua nhà thờ cho đến nhà ga nhé!",
                "visual_svg": "map_build_1"
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 69: Hoàn thành lời chỉ đường cho vị khách du lịch khớp với bản đồ bằng cách điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Gehen Sie zuerst [1] die Brücke und dann die Goethestraße [2] bis zur Post!'",
            "options": null,
            "correct_answer": "über / entlang",
            "explanation": "Đi vượt qua mặt cầu dùng 'über' ('über die Brücke'); đi dọc theo con đường đặt 'entlang' ở sau danh từ ('die Goethestraße entlang').",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "über",
                    "ueber"
                ],
                "slot2_accepted": [
                    "entlang"
                ],
                "accepted_answers": [
                    "über / entlang",
                    "über/entlang",
                    "ueber / entlang",
                    "ueber/entlang"
                ],
                "translation": "Trước tiên quý vị hãy đi qua cây cầu, rồi đi dọc theo phố Goethe cho đến bưu điện!",
                "visual_svg": "map_build_2"
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 70: Hoàn thành câu kể về lịch trình ngày Chủ nhật của gia đình bằng cách điền 2 cụm từ vào các chỗ trống (ngăn cách bởi dấu /): 'Am Sonntagvormittag fahren wir zuerst [1] Flughafen, um Oma abzuholen, und am Nachmittag gehen wir zusammen [2] Zoo.'",
            "options": null,
            "correct_answer": "zum / in den",
            "explanation": "'der Flughafen' sau 'zu + Dativ' là 'zum Flughafen'; đi vào bên trong sở thú ('der Zoo') dùng 'in den Zoo'. 'zum Zoo' (đi tới sở thú) và 'an den Flughafen' cũng đúng ngữ pháp và được chấp nhận.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "zum",
                    "zu dem",
                    "an den",
                    "bis zum"
                ],
                "slot2_accepted": [
                    "in den",
                    "zum",
                    "zu dem"
                ],
                "accepted_answers": [
                    "zum / in den",
                    "zum/in den",
                    "zum / zum",
                    "zum/zum",
                    "zum / zu dem",
                    "zum/zu dem",
                    "zu dem / in den",
                    "zu dem/in den",
                    "zu dem / zum",
                    "zu dem/zu dem",
                    "zu dem / zu dem",
                    "an den / in den",
                    "an den/in den",
                    "an den / zum",
                    "an den/zum",
                    "an den / zu dem",
                    "an den/zu dem",
                    "bis zum / in den",
                    "bis zum/in den",
                    "bis zum / zum",
                    "bis zum/zum",
                    "bis zum / zu dem",
                    "bis zum/zu dem"
                ],
                "translation": "Sáng Chủ nhật, trước tiên chúng tôi lái xe ra sân bay để đón bà, và buổi chiều chúng tôi cùng nhau đi vào sở thú."
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 71: Hoàn thành lời hướng dẫn của tài xế xe buýt bằng cách điền 2 từ vào các chỗ trống (ngăn cách bởi dấu /): 'Sie müssen hier aussteigen, dann [1] großen Supermarkt vorbeigehen und geradeaus bis [2] zweiten Ampel laufen.'",
            "options": null,
            "correct_answer": "am / zur",
            "explanation": "'der Supermarkt' đi với 'an + Dativ + vorbei' là 'am großen Supermarkt vorbei'; 'die Ampel' đi với 'bis zu + Dativ' là 'bis zur zweiten Ampel'. 'an dem' (thay cho 'am') cũng đúng và được chấp nhận.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "am",
                    "an dem",
                    "an diesem",
                    "an einem"
                ],
                "slot2_accepted": [
                    "zur",
                    "zu der"
                ],
                "accepted_answers": [
                    "am / zur",
                    "am/zur",
                    "am / zu der",
                    "am/zu der",
                    "an dem / zur",
                    "an dem/zur",
                    "an dem / zu der",
                    "an dem/zu der",
                    "an diesem / zur",
                    "an diesem/zur",
                    "an diesem / zu der",
                    "an diesem/zu der",
                    "an một/zur",
                    "an einem / zur",
                    "an einem/zur",
                    "an einem / zu der",
                    "an einem/zu der"
                ],
                "translation": "Quý vị phải xuống xe ở đây, rồi đi ngang qua siêu thị lớn và đi bộ thẳng cho đến đèn giao thông thứ hai."
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 72: Hoàn thành câu với dạng chia đúng của động từ khuyết thiếu 'wollen' vào các chỗ trống (ngăn cách bởi dấu /): 'Mein Freund Lukas [1] heute unbedingt das Bundeskanzleramt fotografieren, aber wir [2] lieber zuerst auf der Museumsinsel spazieren gehen.'",
            "options": null,
            "correct_answer": "will / wollen",
            "explanation": "Ngôi thứ 3 số ít ('Lukas' = 'er') chia là 'will'; ngôi thứ nhất số nhiều ('wir') chia là 'wollen'.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "will"
                ],
                "slot2_accepted": [
                    "wollen"
                ],
                "accepted_answers": [
                    "will / wollen",
                    "will/wollen"
                ],
                "translation": "Bạn Lukas của tôi hôm nay nhất định muốn chụp ảnh Phủ Thủ tướng Liên bang, nhưng chúng tôi thích đi dạo trên Đảo Bảo tàng trước hơn."
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 73: Hoàn thành câu hướng dẫn giao thông với dạng chia đúng của 'müssen' vào chỗ trống [1] và 'können' vào chỗ trống [2] (ngăn cách bởi dấu /): 'Vor der Baustelle [1] ihr leider rechts abbiegen, aber danach [2] ihr wieder geradeaus bis zum Hafen fahren.'",
            "options": null,
            "correct_answer": "müsst / könnt",
            "explanation": "Với chủ ngữ 'ihr' (các bạn), 'müssen' chia là 'müsst' và 'können' chia là 'könnt'.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "müsst",
                    "muesst"
                ],
                "slot2_accepted": [
                    "könnt",
                    "koennt"
                ],
                "accepted_answers": [
                    "müsst / könnt",
                    "müsst/könnt",
                    "muesst / koennt",
                    "muesst/koennt"
                ],
                "translation": "Trước công trường, rất tiếc các bạn phải rẽ phải, nhưng sau đó các bạn lại có thể đi thẳng đến cảng."
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 74: Hoàn thành câu với cụm giới từ 'in' kèm mạo từ thích hợp vào các chỗ trống (ngăn cách bởi dấu /): 'Wohin gehst du? — Ich gehe jetzt [1] Staatsoper, weil meine Freundin heute Abend [2] Staatsoper Geige spielt.'",
            "options": null,
            "correct_answer": "in die / in der",
            "explanation": "Ô 1 trả lời cho 'Wohin?' (di chuyển vào trong) -> in + Akkusativ = 'in die Staatsoper'. Ô 2 trả lời cho 'Wo?' (chơi đàn ở đâu - vị trí tĩnh) -> in + Dativ = 'in der Staatsoper'.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "in die"
                ],
                "slot2_accepted": [
                    "in der"
                ],
                "accepted_answers": [
                    "in die / in der",
                    "in die/in der"
                ],
                "translation": "Bạn đang đi đâu thế? — Bây giờ tôi đi vào Nhà hát Opera Quốc gia, bởi vì tối nay bạn gái tôi chơi đàn vĩ cầm ở trong Nhà hát Opera Quốc gia."
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 75: Hoàn thành câu bằng cách điền giới từ 'in' kèm mạo từ thích hợp vào các chỗ trống (ngăn cách bởi dấu /): 'Mein kleiner Bruder muss leider [1] Krankenhaus gebracht werden, aber unser Nachbar arbeitet als Arzt [2] Krankenhaus.'",
            "options": null,
            "correct_answer": "ins / im",
            "explanation": "Đưa vào bệnh viện ('Wohin?' + Akkusativ) với 'das Krankenhaus' dùng 'ins' (in das). Làm việc ở trong bệnh viện ('Wo?' + Dativ) dùng 'im' (in dem). Dạng không rút gọn 'in das / in dem' cũng đúng và được chấp nhận.",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "ins",
                    "in das"
                ],
                "slot2_accepted": [
                    "im",
                    "in dem"
                ],
                "accepted_answers": [
                    "ins / im",
                    "ins/im",
                    "in das / in dem",
                    "in das/in dem",
                    "ins / in dem",
                    "ins/in dem",
                    "in das / im",
                    "in das/im"
                ],
                "translation": "Thật không may, em trai tôi phải được đưa vào bệnh viện, còn người hàng xóm của chúng tôi thì làm bác sĩ ở bệnh viện."
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 76: Hoàn thành đoạn hội thoại hỏi đường ngắn trên phố bằng cách điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Entschuldigung, ich suche [1] alten Marktplatz. Wie komme ich am besten [2] Marktplatz?'",
            "options": null,
            "correct_answer": "den / zum",
            "explanation": "'der Marktplatz' (giống đực) đứng sau động từ 'suchen' (Akkusativ) dùng mạo từ 'den' ('den alten Marktplatz'); đứng sau 'Wie komme ich ...?' (zu + Dativ) dùng 'zum' ('zum Marktplatz').",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "den",
                    "diesen",
                    "einen"
                ],
                "slot2_accepted": [
                    "zum",
                    "zu dem"
                ],
                "accepted_answers": [
                    "den / zum",
                    "den/zum",
                    "den / zu dem",
                    "den/zu dem",
                    "diesen / zum",
                    "diesen/zum",
                    "diesen / zu dem",
                    "diesen/zu dem",
                    "einen / zum",
                    "einen/zum",
                    "einen / zu dem",
                    "einen/zu dem"
                ],
                "translation": "Xin lỗi, tôi đang tìm quảng trường chợ cổ. Tốt nhất thì tôi đi đến quảng trường chợ bằng cách nào?"
            }
        },
        {
            "type": "dien_tao_cau",
            "question": "Câu 77: Hoàn thành câu chỉ đường bằng cách điền dạng đúng của số thứ tự 1. vào chỗ trống [1] và 2. vào chỗ trống [2] (ngăn cách bởi dấu /): 'Nehmen Sie bitte die [1] Straße rechts und biegen Sie dann an der [2] Kreuzung wieder links ab!'",
            "options": null,
            "correct_answer": "erste / zweiten",
            "explanation": "Sau 'die' ở Akkusativ giống cái dùng 'erste' ('die erste Straße'); sau 'an der' ở Dativ giống cái bắt buộc thêm đuôi -n thành 'zweiten' ('an der zweiten Kreuzung').",
            "exp_reward": 25,
            "extra_data": {
                "slot1_accepted": [
                    "erste"
                ],
                "slot2_accepted": [
                    "zweiten"
                ],
                "accepted_answers": [
                    "erste / zweiten",
                    "erste/zweiten"
                ],
                "translation": "Quý vị hãy đi con đường thứ nhất bên phải, rồi sau đó rẽ trái lại ở ngã tư thứ hai!"
            }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 78: „Entschuldigung, wie komme ich vom Hauptbahnhof am schnellsten zum ___?“",
                "options": null,
                "correct_answer": "Flughafen",
                "explanation": "Danh từ ghép der Flughafen có nghĩa là sân bay.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Flughafen"
                        ],
                        "audio_text": "Entschuldigung, wie komme ich vom Hauptbahnhof am schnellsten zum Flughafen?",
                        "translation": "Xin lỗi, làm thế nào tôi đi từ nhà ga trung tâm ra sân bay nhanh nhất?"
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 79: „Gehen Sie zuerst über die lange ___ und dann dreihundert Meter den Fluss entlang.“",
                "options": null,
                "correct_answer": "Brücke",
                "explanation": "Danh từ die Brücke có nghĩa là cây cầu.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Brücke",
                                "Bruecke"
                        ],
                        "audio_text": "Gehen Sie zuerst über die lange Brücke und dann dreihundert Meter den Fluss entlang.",
                        "translation": "Đầu tiên Ngài hãy đi qua cây cầu dài và sau đó đi dọc theo con sông ba trăm mét."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 80: „Der Sightseeing-Bus fährt am historischen Rathaus und an der ___ vorbei.“",
                "options": null,
                "correct_answer": "Staatsoper",
                "explanation": "die Staatsoper là Nhà hát Opera Quốc gia.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Staatsoper"
                        ],
                        "audio_text": "Der Sightseeing-Bus fährt am historischen Rathaus und an der Staatsoper vorbei.",
                        "translation": "Chiếc xe buýt tham quan chạy ngang qua tòa thị chính lịch sử và Nhà hát Opera Quốc gia."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 81: „An der dritten ___ vor dem Krankenhaus musst du links abbiegen.“",
                "options": null,
                "correct_answer": "Kreuzung",
                "explanation": "die Kreuzung là ngã tư / giao lộ.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Kreuzung"
                        ],
                        "audio_text": "An der dritten Kreuzung vor dem Krankenhaus musst du links abbiegen.",
                        "translation": "Tại ngã tư thứ ba trước bệnh viện, bạn phải rẽ trái."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 82: „Meine Großeltern ___ morgen Nachmittag das schöne Schloss Bellevue besichtigen.“",
                "options": null,
                "correct_answer": "wollen",
                "explanation": "Động từ khuyết thiếu wollen chia với chủ ngữ số nhiều Meine Großeltern (sie).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "wollen"
                        ],
                        "audio_text": "Meine Großeltern wollen morgen Nachmittag das schöne Schloss Bellevue besichtigen.",
                        "translation": "Ông bà của tôi muốn tham quan Cung điện Bellevue tuyệt đẹp vào chiều mai."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 83: „Laufen Sie einfach ___ das alte Stadttor, dann stehen Sie direkt auf dem Marktplatz.“",
                "options": null,
                "correct_answer": "durch",
                "explanation": "Giới từ durch (+ Akkusativ) diễn tả sự đi xuyên qua lòng cổng thành.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "durch"
                        ],
                        "audio_text": "Laufen Sie einfach durch das alte Stadttor, dann stehen Sie direkt auf dem Marktplatz.",
                        "translation": "Ngài cứ đi bộ xuyên qua cổng thành cổ, sau đó Ngài sẽ đứng ngay trên quảng trường chợ."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 84: „Am Samstag möchten wir im neuen ___ Kleider kaufen und danach ins Kino gehen.“",
                "options": null,
                "correct_answer": "Einkaufszentrum",
                "explanation": "das Einkaufszentrum là trung tâm thương mại.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Einkaufszentrum"
                        ],
                        "audio_text": "Am Samstag möchten wir im neuen Einkaufszentrum Kleider kaufen und danach ins Kino gehen.",
                        "translation": "Vào thứ Bảy chúng tôi muốn mua quần áo ở trong trung tâm thương mại mới và sau đó đi vào rạp chiếu phim."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 85: „Fahren Sie bitte immer ___ bis zur zweiten Ampel vor der Universität!“",
                "options": null,
                "correct_answer": "geradeaus",
                "explanation": "Trạng từ chỉ hướng geradeaus có nghĩa là đi thẳng.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "geradeaus"
                        ],
                        "audio_text": "Fahren Sie bitte immer geradeaus bis zur zweiten Ampel vor der Universität!",
                        "translation": "Xin Ngài cứ lái xe đi thẳng mãi cho đến đèn giao thông thứ hai trước trường đại học!"
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 86: „Nach der ___ will mein Cousin noch eine Stunde am Hafen bummeln.“",
                "options": null,
                "correct_answer": "Stadtrundfahrt",
                "explanation": "die Stadtrundfahrt là chuyến tham quan vòng quanh thành phố.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Stadtrundfahrt"
                        ],
                        "audio_text": "Nach der Stadtrundfahrt will mein Cousin noch eine Stunde am Hafen bummeln.",
                        "translation": "Sau chuyến tham quan vòng quanh thành phố, anh họ tôi còn muốn đi dạo một tiếng ở cảng biển."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 87: Dịch câu chỉ đường sau sang tiếng Đức (dùng ngôi trang trọng Sie): 'Đầu tiên Ngài hãy đi thẳng qua cây cầu, sau đó đi ngang qua bệnh viện cho đến đèn giao thông thứ hai!'",
                "options": null,
                "correct_answer": "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!",
                "explanation": "Qua cầu: 'über die Brücke' (Akkusativ); đi ngang qua bệnh viện ('das Krankenhaus'): 'am Krankenhaus vorbei' (Dativ); cho đến đèn giao thông thứ hai ('die Ampel'): 'bis zur zweiten Ampel' (Dativ).",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!",
                                "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel",
                                "Zuerst gehen Sie geradeaus über die Brücke, danach gehen Sie am Krankenhaus vorbei bis zur zweiten Ampel.",
                                "Zuerst gehen Sie geradeaus über die Brücke, danach gehen Sie am Krankenhaus vorbei bis zur zweiten Ampel",
                                "Gehen Sie zuerst über die Brücke geradeaus und dann am Krankenhaus vorbei bis zur zweiten Ampel!",
                                "Gehen Sie zuerst über die Brücke geradeaus und dann am Krankenhaus vorbei bis zur zweiten Ampel!"
                        ],
                        "translation": "Đầu tiên Ngài hãy đi thẳng qua cây cầu, sau đó đi ngang qua bệnh viện cho đến đèn giao thông thứ hai: Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!"
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 88: Dịch câu chỉ đường cho bạn thân sau sang tiếng Đức (dùng ngôi du): 'Cậu hãy đi xuyên qua công viên, đi dọc theo con sông và rẽ trái ở ngã tư thứ nhất!'",
                "options": null,
                "correct_answer": "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!",
                "explanation": "Ngôi du mệnh lệnh: 'Geh / Lauf'; xuyên qua công viên: 'durch den Park'; dọc theo con sông: 'den Fluss entlang'; ở ngã tư thứ nhất bên trái: 'an der ersten Kreuzung links'.",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!",
                                "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab",
                                "Geh durch den Park, geh den Fluss entlang und geh die erste Straße links!",
                                "Geh durch den Park, geh den Fluss entlang und geh die erste Straße links",
                                "Lauf durch den Park, den Fluss entlang und an der ersten Kreuzung links!",
                                "Lauf durch den Park, den Fluss entlang und an der ersten Kreuzung links"
                        ],
                        "translation": "Cậu hãy đi xuyên qua công viên, đi dọc theo con sông và rẽ trái ở ngã tư thứ nhất: Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!"
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 89: Dịch câu hỏi đường sau sang tiếng Đức: 'Xin lỗi, chúng tôi đang tìm Đảo Bảo tàng. Làm thế nào chúng tôi đi bộ đến được Đảo Bảo tàng?'",
                "options": null,
                "correct_answer": "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?",
                "explanation": "'die Museumsinsel' mang giống cái (die): sau 'suchen' (Akkusativ) là 'die Museumsinsel', sau 'Wie kommen wir ...?' (zu + Dativ) là 'zur Museumsinsel'.",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?",
                                "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel",
                                "Entschuldigung, wir suchen die Museumsinsel. Wie gehen wir zur Museumsinsel?",
                                "Entschuldigung, wir suchen die Museumsinsel. Wie gehen wir zur Museumsinsel",
                                "Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir zur Museumsinsel?",
                                "Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir zur Museumsinsel"
                        ],
                        "translation": "Xin lỗi, chúng tôi đang tìm Đảo Bảo tàng. Làm thế nào chúng tôi đi bộ đến được Đảo Bảo tàng? = Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?"
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 90: Dịch câu sau sang tiếng Đức (dùng ngôi ihr): 'Các bạn hãy đi ngang qua nhà thờ cổ và băng qua quảng trường chợ, ở bên phải các bạn sẽ nhìn thấy tòa thị chính.'",
                "options": null,
                "correct_answer": "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.",
                "explanation": "Mệnh lệnh ngôi ihr: 'Geht / Lauft'; ngang qua nhà thờ cổ: 'an der alten Kirche vorbei'; băng qua quảng trường chợ: 'über den Marktplatz'; các bạn nhìn thấy: 'seht ihr'.",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.",
                                "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus",
                                "Geht an der alten Kirche vorbei und lauft über den Marktplatz! Rechts seht ihr das Rathaus.",
                                "Geht an der alten Kirche vorbei und lauft über den Marktplatz! Rechts seht ihr das Rathaus",
                                "Lauft an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.",
                                "Lauft an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus"
                        ],
                        "translation": "Các bạn hãy đi ngang qua nhà thờ cổ và băng qua quảng trường chợ, ở bên phải các bạn sẽ nhìn thấy tòa thị chính = Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 91: Dịch câu sau sang tiếng Đức: 'Buổi sáng chú của tôi muốn tham quan Tòa nhà Quốc hội, và buổi chiều chúng tôi muốn đi dạo phố ở trung tâm thương mại.'",
                "options": null,
                "correct_answer": "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln.",
                "explanation": "'mein Onkel' (er) -> 'will ... besichtigen'; 'der Reichstag' ở Akkusativ là 'den Reichstag'; ở trong trung tâm thương mại (Wo? + Dativ) là 'im Einkaufszentrum'.",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln.",
                                "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln",
                                "Am Morgen will mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln.",
                                "Am Morgen will mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln",
                                "Vormittags möchte mein Onkel den Reichstag besichtigen, und nachmittags wollen wir im Einkaufszentrum bummeln.",
                                "Vormittags möchte mein Onkel den Reichstag besichtigen, und nachmittags wollen wir im Einkaufszentrum bummeln"
                        ],
                        "translation": "Buổi sáng chú của tôi muốn tham quan Tòa nhà Quốc hội, và buổi chiều chúng tôi muốn đi dạo phố ở trung tâm thương mại = Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 92: Dịch câu sau sang tiếng Đức: 'Đầu tiên các du khách đi xe buýt đến Cổng Brandenburg, và buổi tối họ đi vào trong Nhà hát Opera Quốc gia.'",
                "options": null,
                "correct_answer": "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper.",
                "explanation": "Đi bằng xe buýt: 'mit dem Bus'; đến Cổng Brandenburg: 'zum Brandenburger Tor' (zu + dem); đi vào trong Nhà hát Opera Quốc gia: 'in die Staatsoper' (in + Akkusativ).",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper.",
                                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper",
                                "Die Touristen fahren zuerst mit dem Bus zum Brandenburger Tor, und abends gehen sie in die Staatsoper.",
                                "Die Touristen fahren zuerst mit dem Bus zum Brandenburger Tor, und abends gehen sie in die Staatsoper",
                                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor und gehen am Abend in die Staatsoper.",
                                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor und gehen am Abend in die Staatsoper"
                        ],
                        "translation": "Đầu tiên các du khách đi xe buýt đến Cổng Brandenburg, và buổi tối họ đi vào trong Nhà hát Opera Quốc gia = Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 93: Dịch câu sau sang tiếng Đức: 'Để đến được cảng biển, bạn phải đi xuyên qua cổng thành và đi ngang qua ngân hàng lớn.'",
                "options": null,
                "correct_answer": "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen.",
                "explanation": "Đến cảng biển: 'zum Hafen'; xuyên qua cổng thành: 'durch das Stadttor'; ngang qua ngân hàng lớn: 'an der großen Bank vorbei'.",
                "exp_reward": 30,
                "extra_data": {
                        "accepted_answers": [
                                "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen.",
                                "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen",
                                "Du musst durch das Stadttor gehen und an der großen Bank vorbeigehen, um zum Hafen zu kommen.",
                                "Du musst durch das Stadttor gehen und an der großen Bank vorbeigehen, um zum Hafen zu kommen",
                                "Wenn du zum Hafen willst, musst du durch das Stadttor und an der großen Bank vorbeigehen.",
                                "Wenn du zum Hafen willst, musst du durch das Stadttor und an der großen Bank vorbeigehen"
                        ],
                        "translation": "Để đến được cảng biển, bạn phải đi xuyên qua cổng thành và đi ngang qua ngân hàng lớn = Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 94: Dịch câu chỉ đường sau sang tiếng Việt: „Gehen Sie vom Bahnhof aus zuerst dreihundert Meter geradeaus, dann an der Hauptpost vorbei und an der zweiten Ampel rechts!“",
                "options": null,
                "correct_answer": "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!",
                "explanation": "'vom Bahnhof aus' = từ nhà ga; 'an der Hauptpost vorbei' = ngang qua bưu điện chính; 'an der zweiten Ampel rechts' = rẽ phải ở đèn giao thông thứ hai.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!",
                                "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai",
                                "Từ phía nhà ga trước tiên bạn đi thẳng 300 mét, rồi đi qua bưu điện chính và tại đèn giao thông thứ hai thì rẽ phải!",
                                "Từ phía nhà ga trước tiên bạn đi thẳng 300 mét, rồi đi qua bưu điện chính và tại đèn giao thông thứ hai thì rẽ phải",
                                "Từ nhà ga đầu tiên bạn đi thẳng 300m, sau đó đi qua bưu điện chính và rẽ phải ở đèn giao thông thứ 2!",
                                "Từ nhà ga đầu tiên bạn đi thẳng 300m, sau đó đi qua bưu điện chính và rẽ phải ở đèn giao thông thứ 2"
                        ],
                        "translation": "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 95: Dịch câu sau sang tiếng Việt: „Wenn ihr zum alten Schloss wollt, müsst ihr zuerst durch den Stadtpark laufen und danach die steinerne Brücke überqueren.“",
                "options": null,
                "correct_answer": "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá.",
                "explanation": "'durch den Stadtpark laufen' = đi bộ/chạy xuyên qua công viên thành phố; 'die steinerne Brücke überqueren' = băng qua cây cầu đá.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá.",
                                "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá",
                                "Nếu các cậu muốn tới cung điện cổ thì trước tiên phải chạy xuyên qua công viên thành phố rồi đi qua cây cầu bằng đá.",
                                "Nếu các cậu muốn tới cung điện cổ thì trước tiên phải chạy xuyên qua công viên thành phố rồi đi qua cây cầu bằng đá",
                                "Nếu các bạn muốn đến lâu đài cổ, các bạn phải đi xuyên qua công viên thành phố và sau đó đi qua cây cầu đá.",
                                "Nếu các bạn muốn đến lâu đài cổ, các bạn phải đi xuyên qua công viên thành phố và sau đó đi qua cây cầu đá"
                        ],
                        "translation": "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 96: Dịch câu sau sang tiếng Việt: „Der Bus Linie 200 fährt am Alexanderplatz, am Berliner Dom und an der Humboldt-Universität vorbei bis zum Zoologischen Garten.“",
                "options": null,
                "correct_answer": "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú.",
                "explanation": "Cấu trúc 'an + Dativ + vorbeifahren' với cả danh từ giống đực ('am') và giống cái ('an der').",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú.",
                                "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú",
                                "Xe buýt tuyến 200 đi ngang qua quảng trường Alexander, Nhà thờ lớn Berlin và trường Đại học Humboldt tới tận Sở thú.",
                                "Xe buýt tuyến 200 đi ngang qua quảng trường Alexander, Nhà thờ lớn Berlin và trường Đại học Humboldt tới tận Sở thú",
                                "Tuyến xe buýt 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt đến tận Vườn bách thú.",
                                "Tuyến xe buýt 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt đến tận Vườn bách thú"
                        ],
                        "translation": "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 97: Dịch câu sau sang tiếng Việt: „Entschuldigen Sie bitte, können Sie mir auf dem Stadtplan zeigen, wie ich zu Fuß zum Bundeskanzleramt komme?“",
                "options": null,
                "correct_answer": "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?",
                "explanation": "'auf dem Stadtplan zeigen' = chỉ trên bản đồ thành phố; 'zu Fuß zum Bundeskanzleramt kommen' = đi bộ đến Phủ Thủ tướng.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?",
                                "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không",
                                "Cho tôi xin lỗi, bạn có thể chỉ giúp tôi trên bản đồ thành phố đường đi bộ tới Phủ Thủ tướng được không?",
                                "Cho tôi xin lỗi, bạn có thể chỉ giúp tôi trên bản đồ thành phố đường đi bộ tới Phủ Thủ tướng được không",
                                "Xin lỗi, bạn có thể chỉ cho tôi trên bản đồ làm thế nào tôi đi bộ đến Phủ Thủ tướng được không?",
                                "Xin lỗi, bạn có thể chỉ cho tôi trên bản đồ làm thế nào tôi đi bộ đến Phủ Thủ tướng được không"
                        ],
                        "translation": "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 98: Dịch câu sau sang tiếng Việt: „Spaziert einfach zwanzig Minuten das Flussufer entlang, dann seht ihr auf der linken Seite die berühmte Museumsinsel!“",
                "options": null,
                "correct_answer": "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!",
                "explanation": "'das Flussufer entlang' = dọc theo bờ sông; 'auf der linken Seite' = ở phía bên tay trái.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!",
                                "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái",
                                "Các cậu hãy tản bộ dọc bờ sông 20 phút rồi sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái!",
                                "Các cậu hãy tản bộ dọc bờ sông 20 phút rồi sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái",
                                "Các bạn cứ đi dạo 20 phút dọc bờ sông, sau đó các bạn sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái!",
                                "Các bạn cứ đi dạo 20 phút dọc bờ sông, sau đó các bạn sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái"
                        ],
                        "translation": "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 99: Dịch câu sau sang tiếng Việt: „Am Vormittag wollen die Studenten in die Alte Nationalgalerie gehen, aber am Abend möchten sie lieber einen Film im Kino sehen.“",
                "options": null,
                "correct_answer": "Vào buổi sáng các sinh viên muốn đi vào Phòng trưng bày Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn.",
                "explanation": "Đối chiếu 'in die Alte Nationalgalerie gehen' (Wohin? + Akkusativ) và 'im Kino sehen' (Wo? + Dativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Vào buổi sáng các sinh viên muốn đi vào Phòng trưng bày Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn.",
                                "Vào buổi sáng các sinh viên muốn đi vào Phòng trưng bày Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn",
                                "Buổi sáng những người sinh viên muốn vào Phòng trưng bày Quốc gia Cũ, nhưng buổi tối họ muốn xem phim trong rạp hơn.",
                                "Buổi sáng những người sinh viên muốn vào Phòng trưng bày Quốc gia Cũ, nhưng buổi tối họ muốn xem phim trong rạp hơn",
                                "Buổi sáng sinh viên muốn đi vào Phòng trưng bày Quốc gia Cũ, nhưng buổi tối họ thích xem một bộ phim trong rạp chiếu phim hơn.",
                                "Buổi sáng sinh viên muốn đi vào Phòng trưng bày Quốc gia Cũ, nhưng buổi tối họ thích xem một bộ phim trong rạp chiếu phim hơn"
                        ],
                        "translation": "Vào buổi sáng các sinh viên muốn đi vào Phòng trưng bày Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 100: Dịch câu sau sang tiếng Việt: „Biegen Sie bitte vor dem großen Einkaufszentrum links ab, fahren Sie durch den kurzen Tunnel und halten Sie direkt neben der Bank!“",
                "options": null,
                "correct_answer": "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!",
                "explanation": "'vor dem großen Einkaufszentrum' = trước trung tâm thương mại lớn; 'durch den kurzen Tunnel' = xuyên qua đường hầm ngắn; 'neben der Bank' = bên cạnh ngân hàng.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!",
                                "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng",
                                "Hãy quẹo trái ở phía trước trung tâm mua sắm lớn, chạy xuyên qua hầm ngắn và đỗ ngay cạnh ngân hàng!",
                                "Hãy quẹo trái ở phía trước trung tâm mua sắm lớn, chạy xuyên qua hầm ngắn và đỗ ngay cạnh ngân hàng",
                                "Xin bạn hãy rẽ trái trước trung tâm thương mại lớn, lái xe qua đường hầm ngắn và dừng ngay bên cạnh ngân hàng!",
                                "Xin bạn hãy rẽ trái trước trung tâm thương mại lớn, lái xe qua đường hầm ngắn và dừng ngay bên cạnh ngân hàng"
                        ],
                        "translation": "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!"
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
    print("✅ Đã khởi tạo thành công Bài 8: 'Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng (Zero Spoilers)!")

if __name__ == "__main__":
    seed_lesson_8()
