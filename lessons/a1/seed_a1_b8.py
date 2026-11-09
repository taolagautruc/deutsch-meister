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
                                    • <b>die Bank</b> (Pl: <i>die Banken / Bänke</i>)<br>
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
                                    • <b>das Krankenhaus</b> (Pl: <i>die Krankenhäuser</i>)<br>
                                    • <b>das Einkaufszentrum</b> (Pl: <i>die Einkaufszentren</i>)<br>
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
                        <p class="text-slate-500 italic">„Entschuldigung, ich suche das Kino.“</p>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">2. Entschuldigung, wo ist + [Nominativ]?</div>
                        <p class="text-slate-600">Động từ <i>sein (ist)</i> luôn đi với Cách 1: <i>der Bahnhof / eine Bank / das Kino</i>.</p>
                        <p class="text-slate-500 italic">„Entschuldigung, wo ist hier eine Bank?“</p>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">3. Entschuldigung, wo geht es + [Hướng đích]?</div>
                        <p class="text-slate-600">Dùng <i>zum / zur</i> hoặc <i>ins / in die</i>: Đi lối nào để tới...</p>
                        <p class="text-slate-500 italic">„Entschuldigung, wo geht es zum Bahnhof?“</p>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 space-y-1">
                        <div class="font-bold text-indigo-700">4. Entschuldigung, wie komme ich + [Hướng đích]?</div>
                        <p class="text-slate-600">Mẫu câu hỏi đường phổ biến nhất: Làm thế nào tôi đến được...</p>
                        <p class="text-slate-500 italic">„Entschuldigung, wie komme ich zur Post?“</p>
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
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><rect x="30" y="0" width="100" height="180" fill="#334155"/><line x1="80" y1="5" x2="80" y2="175" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/><rect x="130" y="0" width="15" height="180" fill="#cbd5e1"/><rect x="155" y="30" width="130" height="120" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="2"/><rect x="165" y="42" width="24" height="24" fill="#38bdf8" rx="3"/><rect x="198" y="42" width="24" height="24" fill="#38bdf8" rx="3"/><rect x="231" y="42" width="24" height="24" fill="#38bdf8" rx="3"/><rect x="190" y="100" width="35" height="50" fill="#475569" rx="3"/><text x="220" y="85" font-size="11" font-weight="black" fill="#1e293b" text-anchor="middle">UNIVERSITÄT</text><text x="220" y="98" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="middle">(die / Femininum)</text><rect x="20" y="12" width="170" height="26" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/><text x="105" y="29" font-size="11" font-weight="black" fill="#1d4ed8" text-anchor="middle">an + DATIV + vorbei</text><path d="M80 165 L80 35" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/><polygon points="80,18 70,38 90,38" fill="#1d4ed8"/><circle cx="80" cy="165" r="5" fill="#1d4ed8"/><rect x="15" y="145" width="205" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="117" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 an der Universität vorbei</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi ngang qua bên cạnh tòa nhà mà không rẽ vào trong: <i>an der Universität vorbei / am Dom vorbei</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-rose-100 text-rose-800">SƠ ĐỒ 2: durch + AKKUSATIV</span>
                        <div id="svg-diag-durch">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><rect x="90" y="0" width="120" height="180" fill="#334155"/><rect x="20" y="45" width="260" height="85" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="2.5"/><path d="M105 130 L105 75 A 45 45 0 0 1 195 75 L195 130 Z" fill="#334155" stroke="#1e293b" stroke-width="2"/><rect x="35" y="55" width="30" height="75" fill="#cbd5e1" stroke="#64748b"/><rect x="235" y="55" width="30" height="75" fill="#cbd5e1" stroke="#64748b"/><polygon points="150,22 80,45 220,45" fill="#be123c"/><circle cx="150" cy="15" r="6" fill="#fbbf24"/><text x="150" y="40" font-size="11" font-weight="black" fill="#ffffff" text-anchor="middle">Brandenburger Tor (das)</text><rect x="20" y="12" width="170" height="26" rx="6" fill="#fdf2f8" stroke="#f472b6" stroke-width="1.5"/><text x="105" y="29" font-size="11" font-weight="black" fill="#be185d" text-anchor="middle">durch + AKKUSATIV</text><path d="M150 168 L150 25" fill="none" stroke="#e11d48" stroke-width="6" stroke-linecap="round"/><polygon points="150,10 140,30 160,30" fill="#be123c"/><circle cx="150" cy="168" r="5" fill="#be123c"/><rect x="50" y="145" width="200" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="150" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 durch das Tor (xuyên qua lòng cổng)</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi xuyên qua chính giữa lòng cổng vòm hoặc công viên: <i>durch das Tor / durch den Park</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800">SƠ ĐỒ 3: über + AKKUSATIV</span>
                        <div id="svg-diag-ueber">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><rect x="0" y="50" width="300" height="75" fill="#38bdf8"/><path d="M0 65 Q 75 55 150 65 T 300 65" fill="none" stroke="#0284c7" stroke-width="3"/><path d="M0 105 Q 75 95 150 105 T 300 105" fill="none" stroke="#0284c7" stroke-width="3"/><rect x="100" y="15" width="100" height="150" rx="6" fill="#334155" stroke="#475569" stroke-width="2"/><rect x="94" y="15" width="6" height="150" fill="#94a3b8"/><rect x="200" y="15" width="6" height="150" fill="#94a3b8"/><line x1="150" y1="20" x2="150" y2="160" stroke="#ffffff" stroke-width="2" stroke-dasharray="8 6"/><text x="50" y="45" font-size="10" font-weight="extrabold" fill="#0369a1">die Schlossbrücke</text><rect x="20" y="12" width="170" height="26" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/><text x="105" y="29" font-size="11" font-weight="black" fill="#15803d" text-anchor="middle">über + AKKUSATIV</text><path d="M150 168 L150 25" fill="none" stroke="#16a34a" stroke-width="6" stroke-linecap="round"/><polygon points="150,10 140,30 160,30" fill="#15803d"/><circle cx="150" cy="168" r="5" fill="#15803d"/><rect x="50" y="145" width="200" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="150" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 über die Brücke (băng qua mặt cầu)</text></svg>
                        </div>
                        <p class="text-xs text-slate-600">Đi vượt qua trên mặt cầu, mặt quảng trường: <i>über die Brücke / über den Platz</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-amber-100 text-amber-800">SƠ ĐỒ 4: AKKUSATIV + entlang</span>
                        <div id="svg-diag-entlang">
                            <svg viewBox="0 0 300 180" width="100%" height="150" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white"><rect x="0" y="0" width="300" height="180" fill="#f8fafc"/><path d="M60 180 C 100 110, 200 110, 240 0 L 290 0 C 250 110, 150 110, 110 180 Z" fill="#334155"/><path d="M85 180 C 125 110, 225 110, 265 0" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/><rect x="20" y="12" width="210" height="26" rx="6" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/><text x="125" y="29" font-size="11" font-weight="black" fill="#a16207" text-anchor="middle">AKKUSATIV + entlang</text><path d="M85 168 C 125 105, 225 105, 265 20" fill="none" stroke="#ca8a04" stroke-width="6" stroke-linecap="round"/><polygon points="268,8 253,22 271,28" fill="#a16207"/><circle cx="85" cy="168" r="5" fill="#a16207"/><rect x="30" y="145" width="240" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/><text x="150" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 die Straße entlang (dọc theo con đường)</text></svg>
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
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung und dort links. Danach gehen Sie bis zur Ampel. Rechts sehen Sie die Post.', 1.0)" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus. <b>Dann</b> gehen Sie die erste Straße rechts, <b>an der Bank vorbei</b>. <b>Dann</b> gehen Sie bis zur zweiten Kreuzung und dort links. <b>Danach</b> gehen Sie <b>bis zur Ampel</b>. Rechts sehen Sie <b>die Post</b>.“</p>
                        <p class="text-xs text-blue-800 font-medium"><b>Dịch nghĩa:</b> Đầu tiên Ngài đi thẳng. Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. Sau đó Ngài đi đến ngã tư thứ hai thì rẽ trái. Tiếp theo Ngài đi cho đến đèn giao thông. Ở bên phải Ngài sẽ nhìn thấy bưu điện.</p>
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
                "akkusativ": "den / einen / keinen Bahnhof",
                "meaning": "nhà ga tàu hỏa",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm đuôi -e (die Bahnhöfe).",
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
                "akkusativ": "den / einen / keinen Hauptbahnhof",
                "meaning": "nhà ga trung tâm",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép với der Bahnhof (Haupt + Bahnhof), số nhiều: die Hauptbahnhöfe.",
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
                "akkusativ": "den / einen / keinen Hafen",
                "meaning": "cảng biển",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều biến âm a -> ä (die Häfen).",
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
                "akkusativ": "den / einen / keinen Flughafen",
                "meaning": "sân bay",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép (Flug + der Hafen), số nhiều: die Flughäfen.",
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
                "akkusativ": "den / einen / keinen Markt",
                "meaning": "chợ, khu chợ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm đuôi -e (die Märkte).",
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
                "akkusativ": "den / einen / keinen Supermarkt",
                "meaning": "siêu thị",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép (Super + der Markt), số nhiều: die Supermärkte.",
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
                "akkusativ": "den / einen / keinen Platz",
                "meaning": "quảng trường, chỗ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm -e (die Plätze). Băng qua quảng trường: über den Platz.",
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
                "akkusativ": "den / einen / keinen Park",
                "meaning": "công viên",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều thêm -s (die Parks). Đi xuyên qua công viên: durch den Park.",
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
                "akkusativ": "den / einen / keinen Zoo",
                "meaning": "vườn bách thú, sở thú",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực vay mượn, số nhiều thêm -s (die Zoos).",
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
                "akkusativ": "den / einen / keinen Turm",
                "meaning": "tòa tháp, ngọn tháp",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều biến âm u -> ü và thêm -e (die Türme).",
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
                "akkusativ": "den / einen / keinen Dom",
                "meaning": "nhà thờ lớn, thánh đường",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều thêm đuôi -e (die Dome).",
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
                "akkusativ": "die / eine / keine Stadt",
                "meaning": "thành phố",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều biến âm a -> ä và thêm -e (die Städte).",
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
                "akkusativ": "die / eine / keine Kirche",
                "meaning": "nhà thờ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều thêm -n (die Kirchen). Đi ngang qua nhà thờ: an der Kirche vorbei.",
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
                "akkusativ": "die / eine / keine Schule",
                "meaning": "trường học",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều thêm -n (die Schulen).",
                "example": "Die Kinder gehen jeden Morgen zur Schule.",
                "example_vi": "Những đứa trẻ đi đến trường học mỗi buổi sáng."
        },
        {
                "word": "Brücke",
                "article": "die",
                "gender": "die",
                "plural": "die Brücken",
                "indefinite": "eine Brücke",
                "negation": "keine Brücke",
                "akkusativ": "die / eine / keine Brücke",
                "meaning": "cây cầu",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều thêm -n (die Brücken). Đi qua cầu: über die Brücke.",
                "example": "Paula und Alex laufen über die Schlossbrücke.",
                "example_vi": "Paula và Alex đi bộ qua cầu Schlossbrücke."
        },
        {
                "word": "Bank",
                "article": "die",
                "gender": "die",
                "plural": "die Banken / die Bänke",
                "indefinite": "eine Bank",
                "negation": "keine Bank",
                "akkusativ": "die / eine / keine Bank",
                "meaning": "ngân hàng / ghế băng dài",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Phân biệt 2 nghĩa: Ngân hàng có số nhiều là die Banken; Ghế băng dài có số nhiều là die Bänke. Đi ngang qua: an der Bank vorbei.",
                "example": "Dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
                "example_vi": "Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."
        },
        {
                "word": "Post",
                "article": "die",
                "gender": "die",
                "plural": "nur Singular",
                "indefinite": "eine Post",
                "negation": "keine Post",
                "akkusativ": "die / eine / keine Post",
                "meaning": "bưu điện, ngành bưu chính",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), thường chỉ dùng ở số ít (nur Singular). Đi tới bưu điện: zur Post.",
                "example": "Rechts neben der Ampel sehen Sie die Post.",
                "example_vi": "Ở bên phải cạnh đèn giao thông, Ngài sẽ nhìn thấy bưu điện."
        },
        {
                "word": "Straße",
                "article": "die",
                "gender": "die",
                "plural": "die Straßen",
                "indefinite": "eine Straße",
                "negation": "keine Straße",
                "akkusativ": "die / eine / keine Straße",
                "meaning": "con đường, phố",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều thêm -n (die Straßen). Đi dọc theo con đường: die Straße entlang.",
                "example": "Gehen Sie bitte diese Straße entlang bis zur Kreuzung!",
                "example_vi": "Xin Ngài hãy đi dọc theo con đường này cho đến ngã tư!"
        },
        {
                "word": "Ampel",
                "article": "die",
                "gender": "die",
                "plural": "die Ampeln",
                "indefinite": "eine Ampel",
                "negation": "keine Ampel",
                "akkusativ": "die / eine / keine Ampel",
                "meaning": "đèn giao thông",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều thêm -n (die Ampeln). Cho đến đèn giao thông: bis zur Ampel.",
                "example": "Gehen Sie geradeaus bis zur Ampel!",
                "example_vi": "Ngài hãy đi thẳng cho đến đèn giao thông!"
        },
        {
                "word": "Kreuzung",
                "article": "die",
                "gender": "die",
                "plural": "die Kreuzungen",
                "indefinite": "eine Kreuzung",
                "negation": "keine Kreuzung",
                "akkusativ": "die / eine / keine Kreuzung",
                "meaning": "ngã tư, giao lộ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Hậu tố -ung luôn mang giống cái (die), số nhiều thêm -en (die Kreuzungen). Cho đến ngã tư: bis zur Kreuzung.",
                "example": "An der zweiten Kreuzung biegen Sie bitte rechts ab!",
                "example_vi": "Tại ngã tư thứ hai xin Ngài hãy rẽ phải!"
        },
        {
                "word": "Disko",
                "article": "die",
                "gender": "die",
                "plural": "die Diskos",
                "indefinite": "eine Disko",
                "negation": "keine Disko",
                "akkusativ": "die / eine / keine Disko",
                "meaning": "vũ trường, quán bar nhạc",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống cái (die), số nhiều thêm -s (die Diskos). Đi vào vũ trường: in die Disko.",
                "example": "Am Abend gehen die Jugendlichen in die Disko.",
                "example_vi": "Vào buổi tối các bạn thanh thiếu niên đi vào vũ trường."
        },
        {
                "word": "Schloss",
                "article": "das",
                "gender": "das",
                "plural": "die Schlösser",
                "indefinite": "ein Schloss",
                "negation": "kein Schloss",
                "akkusativ": "das / ein / kein Schloss",
                "meaning": "lâu đài, cung điện",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống trung (das), số nhiều biến âm o -> ö và thêm -er (die Schlösser).",
                "example": "In Deutschland gibt es viele alte Schlösser.",
                "example_vi": "Ở nước Đức có rất nhiều lâu đài cổ kính."
        },
        {
                "word": "Stadttor",
                "article": "das",
                "gender": "das",
                "plural": "die Stadttore",
                "indefinite": "ein Stadttor",
                "negation": "kein Stadttor",
                "akkusativ": "das / ein / kein Stadttor",
                "meaning": "cổng thành",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép giống trung (die Stadt + das Tor), số nhiều: die Stadttore. Đi xuyên qua cổng: durch das Stadttor.",
                "example": "Die Touristen gehen durch das alte Stadttor.",
                "example_vi": "Các du khách đi xuyên qua cổng thành cổ."
        },
        {
                "word": "Kino",
                "article": "das",
                "gender": "das",
                "plural": "die Kinos",
                "indefinite": "ein Kino",
                "negation": "kein Kino",
                "akkusativ": "das / ein / kein Kino",
                "meaning": "rạp chiếu phim",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống trung (das), số nhiều thêm -s (die Kinos). Đi vào rạp chiếu phim: ins Kino (in + das).",
                "example": "Heute Abend wollen wir noch einen Film im Kino sehen.",
                "example_vi": "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim."
        },
        {
                "word": "Krankenhaus",
                "article": "das",
                "gender": "das",
                "plural": "die Krankenhäuser",
                "indefinite": "ein Krankenhaus",
                "negation": "kein Krankenhaus",
                "akkusativ": "das / ein / kein Krankenhaus",
                "meaning": "bệnh viện",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép giống trung (krank + das Haus), số nhiều: die Krankenhäuser.",
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
                "akkusativ": "das / ein / kein Einkaufszentrum",
                "meaning": "trung tâm thương mại",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Đuôi -um đổi thành -en ở số nhiều: die Einkaufszentren. Giống trung (das).",
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
                "akkusativ": "das / ein / kein Hotel",
                "meaning": "khách sạn",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống trung (das), số nhiều thêm -s (die Hotels).",
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
                "akkusativ": "das / ein / kein Museum",
                "meaning": "viện bảo tàng",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Đuôi -um đổi thành -en ở số nhiều: die Museen. Giống trung (das).",
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
                "akkusativ": "das / ein / kein Rathaus",
                "meaning": "tòa thị chính",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép giống trung (der Rat + das Haus), số nhiều: die Rathäuser.",
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
                "akkusativ": "das / ein / kein Theater",
                "meaning": "nhà hát kịch",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống trung (das), giữ nguyên dạng ở số nhiều (die Theater).",
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
                "akkusativ": "den / einen / keinen Reichstag",
                "meaning": "Tòa nhà Quốc hội Đức",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Danh lam thắng cảnh Berlin giống đực (vì der Tag). Đi tới: zum Reichstag.",
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
                "akkusativ": "den / einen / keinen Alexanderplatz",
                "meaning": "Quảng trường Alexander",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Quảng trường nổi tiếng ở Berlin mang giống đực (vì der Platz). Đi tới: zum Alexanderplatz.",
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
                "akkusativ": "den / einen / keinen Potsdamer Platz",
                "meaning": "Quảng trường Potsdam",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Quảng trường hiện đại tại Berlin mang giống đực (vì der Platz).",
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
                "akkusativ": "den / einen / keinen Berliner Dom",
                "meaning": "Nhà thờ lớn Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Thánh đường lớn ở Berlin mang giống đực (vì der Dom). Đi vào trong: in den Berliner Dom.",
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
                "akkusativ": "den / einen / keinen Fernsehturm",
                "meaning": "Tháp truyền hình Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Tòa tháp cao nhất nước Đức tại Berlin mang giống đực (vì der Turm).",
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
                "akkusativ": "die / eine / keine Humboldt-Universität",
                "meaning": "Trường Đại học Humboldt",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Hậu tố -tät luôn mang giống cái (die). Đi tới: zur Humboldt-Universität.",
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
                "akkusativ": "die / eine / keine Staatsoper",
                "meaning": "Nhà hát Opera Quốc gia Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Danh lam thắng cảnh mang giống cái (vì die Oper). Đi tới: zur Staatsoper.",
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
                "akkusativ": "die / eine / keine Friedrichstraße",
                "meaning": "Phố mua sắm Friedrich",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Con phố thương mại sầm uất tại Berlin mang giống cái (vì die Straße). Đi dọc phố: die Friedrichstraße entlang.",
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
                "akkusativ": "die / eine / keine Museumsinsel",
                "meaning": "Đảo Bảo tàng Berlin",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Quần thể bảo tàng di sản UNESCO mang giống cái (vì die Insel - hòn đảo). Đi tới: zur Museumsinsel.",
                "example": "Auf der Museumsinsel liegen fünf weltberühmte Museen.",
                "example_vi": "Trên Đảo Bảo tàng có năm viện bảo tàng nổi tiếng khắp thế giới."
        },
        {
                "word": "Alte Nationalgalerie",
                "article": "die",
                "gender": "die",
                "plural": "nur Singular",
                "indefinite": "eine Alte Nationalgalerie",
                "negation": "keine Alte Nationalgalerie",
                "akkusativ": "die / eine / keine Alte Nationalgalerie",
                "meaning": "Khu triển lãm Quốc gia Cũ",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Hậu tố -ie luôn mang giống cái (die). Đi vào trong: in die Alte Nationalgalerie.",
                "example": "Danach will ich in die Alte Nationalgalerie gehen.",
                "example_vi": "Tiếp theo tôi muốn đi vào Khu triển lãm Quốc gia Cũ."
        },
        {
                "word": "Bundeskanzleramt",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Bundeskanzleramt",
                "negation": "kein Bundeskanzleramt",
                "akkusativ": "das / ein / kein Bundeskanzleramt",
                "meaning": "Phủ Thủ tướng Liên bang Đức",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Trụ sở làm việc của Thủ tướng Đức mang giống trung (vì das Amt - cơ quan/phủ). Chạy xe ngang qua: am Bundeskanzleramt vorbei.",
                "example": "Sie fahren mit dem Bus am Bundeskanzleramt vorbei.",
                "example_vi": "Họ đi xe buýt ngang qua Phủ Thủ tướng."
        },
        {
                "word": "Brandenburger Tor",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Brandenburger Tor",
                "negation": "kein Brandenburger Tor",
                "akkusativ": "das / ein / kein Brandenburger Tor",
                "meaning": "Cổng thành Brandenburg",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Biểu tượng lịch sử của Berlin và nước Đức mang giống trung (vì das Tor). Đi tới: zum Brandenburger Tor.",
                "example": "Paula und Alex gehen zum Brandenburger Tor und machen viele Fotos.",
                "example_vi": "Paula và Alex đi đến Cổng Brandenburg và chụp nhiều bức ảnh."
        },
        {
                "word": "Schloss Bellevue",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Schloss Bellevue",
                "negation": "kein Schloss Bellevue",
                "akkusativ": "das / ein / kein Schloss Bellevue",
                "meaning": "Cung điện Bellevue",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Nơi làm việc của Tổng thống Đức mang giống trung (vì das Schloss).",
                "example": "Das Schloss Bellevue liegt direkt an der Spree in Berlin.",
                "example_vi": "Cung điện Bellevue nằm ngay bên bờ sông Spree ở Berlin."
        },
        {
                "word": "Sony Center",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Sony Center",
                "negation": "kein Sony Center",
                "akkusativ": "das / ein / kein Sony Center",
                "meaning": "Trung tâm phức hợp Sony",
                "category": "Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)",
                "rule": "Trung tâm thương mại & rạp chiếu phim hiện đại mang giống trung (vì das Center).",
                "example": "Wir schauen uns das moderne Dach im Sony Center an.",
                "example_vi": "Chúng tôi ngắm nhìn mái vòm hiện đại ở Trung tâm Sony."
        },
        {
                "word": "Stadtrundfahrt",
                "article": "die",
                "gender": "die",
                "plural": "die Stadtrundfahrten",
                "indefinite": "eine Stadtrundfahrt",
                "negation": "keine Stadtrundfahrt",
                "akkusativ": "die / eine / keine Stadtrundfahrt",
                "meaning": "chuyến tham quan thành phố",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép giống cái (die Stadt + die Fahrt), số nhiều: die Stadtrundfahrten.",
                "example": "Wir wollen heute eine Stadtrundfahrt in Berlin machen.",
                "example_vi": "Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố ở Berlin."
        },
        {
                "word": "Fluss",
                "article": "der",
                "gender": "der",
                "plural": "die Flüsse",
                "indefinite": "ein Fluss",
                "negation": "kein Fluss",
                "akkusativ": "den / einen / keinen Fluss",
                "meaning": "dòng sông",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ giống đực (der), số nhiều biến âm u -> ü và thêm -e (die Flüsse).",
                "example": "Die Spree ist ein bekannter Fluss in Berlin.",
                "example_vi": "Spree là một dòng sông nổi tiếng ở Berlin."
        },
        {
                "word": "Fußgänger",
                "article": "der",
                "gender": "der",
                "plural": "die Fußgänger",
                "indefinite": "ein Fußgänger",
                "negation": "kein Fußgänger",
                "akkusativ": "den / einen / keinen Fußgänger",
                "meaning": "người đi bộ",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Hậu tố -er chỉ người mang giống đực (der), giữ nguyên ở số nhiều (die Fußgänger).",
                "example": "An der Kreuzung müssen Fußgänger auf die Ampel achten.",
                "example_vi": "Tại ngã tư người đi bộ phải chú ý đến đèn giao thông."
        },
        {
                "word": "Haltestelle",
                "article": "die",
                "gender": "die",
                "plural": "die Haltestellen",
                "indefinite": "eine Haltestelle",
                "negation": "keine Haltestelle",
                "akkusativ": "die / eine / keine Haltestelle",
                "meaning": "trạm dừng, điểm đỗ xe buýt / tàu",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Danh từ ghép giống cái (die Stelle), số nhiều thêm -n (die Haltestellen).",
                "example": "Der Bus hält an der nächsten Haltestelle.",
                "example_vi": "Chiếc xe buýt dừng lại ở trạm dừng tiếp theo."
        },
        {
                "word": "Ticket",
                "article": "das",
                "gender": "das",
                "plural": "die Tickets",
                "indefinite": "ein Ticket",
                "negation": "kein Ticket",
                "akkusativ": "das / ein / kein Ticket",
                "meaning": "vé (xe buýt, tàu hỏa, tham quan)",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Từ vay mượn giống trung (das), số nhiều thêm -s (die Tickets).",
                "example": "Sie kauft ein Ticket für die Stadtrundfahrt.",
                "example_vi": "Cô ấy mua một chiếc vé cho chuyến tham quan thành phố."
        },
        {
                "word": "Zentrum",
                "article": "das",
                "gender": "das",
                "plural": "die Zentren",
                "indefinite": "ein Zentrum",
                "negation": "kein Zentrum",
                "akkusativ": "das / ein / kein Zentrum",
                "meaning": "trung tâm thành phố",
                "category": "Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)",
                "rule": "Hậu tố -um đổi thành -en ở số nhiều: die Zentren. Giống trung (das). Đi tới trung tâm: ins Zentrum.",
                "example": "Die Museumsinsel liegt direkt im Zentrum von Berlin.",
                "example_vi": "Đảo Bảo tàng nằm ngay tại trung tâm của Berlin."
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
            art,
            meaning,
            example_str
        ))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # KHO 100 CÂU HỎI BÀI TẬP ĐỘC NHẤT BÀI 8 (9 NHÓM DẠNG CHUẨN)
    # =========================================================================
    raw_exercises = [
        {
                "type": "trac_nghiem",
                "question": "Câu 1: Quan sát Sơ đồ chỉ đường e) bên trên và chọn câu lệnh tiếng Đức khớp chính xác với mũi tên:",
                "options": [
                        "Gehen Sie hier links.",
                        "Gehen Sie die erste Straße links.",
                        "Gehen Sie die zweite Straße links.",
                        "Gehen Sie die zweite Straße rechts."
                ],
                "correct_answer": "Gehen Sie die zweite Straße links.",
                "explanation": "Trên sơ đồ e), con đường chính có hai ngã rẽ bên trái, mũi tên đi thẳng bỏ qua ngã rẽ thứ nhất và quẹo vào ngã rẽ thứ hai bên tay trái -> 'Gehen Sie die zweite Straße links.'",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie die zweite Straße links."
                        ],
                        "translation": "Ngài hãy rẽ trái ở con đường thứ hai.",
                        "visual_svg": "direction_card_e"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 2: Quan sát Sơ đồ chỉ đường b) bên trên: Mũi tên chỉ hành động đi ngang qua nhà thờ (die Kirche). Câu nào dưới đây đúng ngữ pháp 100%?",
                "options": [
                        "Gehen Sie an die Kirche vorbei.",
                        "Gehen Sie an der Kirche vorbei.",
                        "Gehen Sie durch die Kirche.",
                        "Gehen Sie über der Kirche."
                ],
                "correct_answer": "Gehen Sie an der Kirche vorbei.",
                "explanation": "Cấu trúc 'đi ngang qua bên cạnh một địa điểm' luôn dùng an + Dativ + vorbei. Vì die Kirche mang giống cái (Femininum), ở Dativ mạo từ die đổi thành der -> 'an der Kirche vorbei'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie an der Kirche vorbei."
                        ],
                        "translation": "Ngài hãy đi ngang qua nhà thờ.",
                        "visual_svg": "direction_card_b"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 3: Quan sát Sơ đồ chỉ đường f) bên trên: Để chỉ đường 'Ngài hãy đi băng qua quảng trường (der Platz)', ta nói như thế nào?",
                "options": [
                        "Gehen Sie über dem Platz.",
                        "Gehen Sie über den Platz.",
                        "Gehen Sie an dem Platz vorbei.",
                        "Gehen Sie bis zum Platz."
                ],
                "correct_answer": "Gehen Sie über den Platz.",
                "explanation": "Đi băng qua một bề mặt không gian (Wohin? - có sự di chuyển) dùng giới từ über + Akkusativ. Danh từ giống đực der Platz sang Akkusativ đổi thành 'über den Platz'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie über den Platz."
                        ],
                        "translation": "Ngài hãy đi băng qua quảng trường.",
                        "visual_svg": "direction_card_f"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 4: Quan sát hai sơ đồ c) và d) bên trên: Vì cả 'die Ampel' (đèn giao thông) và 'die Kreuzung' (ngã tư) đều mang giống cái (Femininum), cụm giới từ 'đi cho đến...' nào dưới đây là đúng?",
                "options": [
                        "bis zu die Ampel / bis zu die Kreuzung",
                        "bis zum Ampel / bis zum Kreuzung",
                        "bis zur Ampel / bis zur Kreuzung",
                        "bis an die Ampel / bis in die Kreuzung"
                ],
                "correct_answer": "bis zur Ampel / bis zur Kreuzung",
                "explanation": "Giới từ kép 'bis zu' luôn đi với Cách 3 (Dativ). Với danh từ giống cái (die Ampel, die Kreuzung), zu + der viết tắt thành zur -> 'bis zur Ampel' và 'bis zur Kreuzung'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "bis zur Ampel / bis zur Kreuzung"
                        ],
                        "translation": "Đi cho đến đèn giao thông / Đi cho đến ngã tư.",
                        "visual_svg": "direction_card_c_and_d"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 5: Quan sát Sơ đồ i) bên trên: Chọn câu đúng ngữ pháp để diễn tả 'Ngài hãy đi dọc theo con đường Friedrich (die Friedrichstraße)':",
                "options": [
                        "Gehen Sie entlang der Friedrichstraße.",
                        "Gehen Sie die Friedrichstraße entlang.",
                        "Gehen Sie an der Friedrichstraße entlang vorbei.",
                        "Gehen Sie durch die Friedrichstraße entlang."
                ],
                "correct_answer": "Gehen Sie die Friedrichstraße entlang.",
                "explanation": "Khi dùng từ 'entlang' (dọc theo) đứng SAU danh từ, danh từ phía trước được chia ở Cách 4 (Akkusativ): 'Gehen Sie die Friedrichstraße entlang.'",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie die Friedrichstraße entlang."
                        ],
                        "translation": "Ngài hãy đi dọc theo đường Friedrich.",
                        "visual_svg": "direction_card_i"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 6: Quan sát 2 hình minh họa đối chiếu bên trên và chọn cặp giới từ + mạo từ điền đúng vào câu: 'Zuerst gehen die Touristen ___ Stadttor (das Stadttor), und danach laufen sie ___ Brücke (die Brücke).'",
                "options": [
                        "über das / durch die",
                        "durch das / über die",
                        "durch dem / über der",
                        "am / an der"
                ],
                "correct_answer": "durch das / über die",
                "explanation": "Đi xuyên qua lòng cổng vòm dùng 'durch + Akkusativ' (durch das Stadttor); đi vượt qua mặt cầu dùng 'über + Akkusativ' (über die Brücke).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "durch das / über die"
                        ],
                        "translation": "Đầu tiên các du khách đi xuyên qua cổng thành, và tiếp theo họ đi bộ qua cây cầu.",
                        "visual_svg": "spatial_contrast_tor_bruecke"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 7: Hãy theo dõi lộ trình sau trên Bản đồ thành phố bên trên: 'Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung und dort links. Danach gehen Sie bis zur Ampel.' — Tòa nhà nằm ở bên tay phải (rechts) của bạn tại điểm cuối là gì?",
                "options": [
                        "das Kino",
                        "die Bank",
                        "die Post",
                        "der Bahnhof"
                ],
                "correct_answer": "die Post",
                "explanation": "Theo đúng hướng di chuyển từ dưới lên tới đèn giao thông (Ampel) trên bản đồ thành phố, phía bên tay phải (rechts) chính là 'die Post' (Bưu điện).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "die Post"
                        ],
                        "translation": "Ở bên phải Ngài nhìn thấy bưu điện (die Post).",
                        "visual_svg": "city_grid_map_quiz_1"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 8: Quan sát Lộ trình số 2 (màu xanh lá) trên bản đồ bên trên và chọn từ đúng điền vào chỗ trống: 'Zuerst gehen Sie geradeaus, bis zur ___ Kreuzung rechts. Dann gehen Sie geradeaus, ___ die Kreuzung. Links sehen Sie die Post.'",
                "options": [
                        "ersten / durch",
                        "zweiten / über",
                        "zweiten / an",
                        "dritten / um"
                ],
                "correct_answer": "zweiten / über",
                "explanation": "Đường màu xanh lá đi thẳng tới ngã tư thứ hai ('bis zur zweiten Kreuzung rechts'), sau đó đi thẳng băng qua ngã tư tiếp theo ('über die Kreuzung').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zweiten / über"
                        ],
                        "translation": "Đầu tiên Ngài đi thẳng đến ngã tư thứ hai rẽ phải, sau đó đi thẳng băng qua ngã tư.",
                        "visual_svg": "city_grid_map_quiz_2"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 9: Dòng nào dưới đây liệt kê ĐÚNG 100% cả mạo từ số ít và dạng số nhiều của các danh từ địa điểm trong thành phố?",
                "options": [
                        "der Bahnhof (die Bahnhofen) / das Schloss (die Schlosse) / das Einkaufszentrum (die Einkaufszentrums)",
                        "der Bahnhof (die Bahnhöfe) / das Schloss (die Schlösser) / das Einkaufszentrum (die Einkaufszentren)",
                        "das Bahnhof (die Bahnhöfe) / der Schloss (die Schlösser) / die Einkaufszentrum (die Einkaufszentren)",
                        "der Hafen (die Hafen) / der Markt (die Markte) / der Platz (die Platze)"
                ],
                "correct_answer": "der Bahnhof (die Bahnhöfe) / das Schloss (die Schlösser) / das Einkaufszentrum (die Einkaufszentren)",
                "explanation": "der Bahnhof -> die Bahnhöfe (thêm Umlaut + -e); das Schloss -> die Schlösser (thêm Umlaut + -er); das Einkaufszentrum -> die Einkaufszentren (đuôi -um đổi thành -en).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der Bahnhof (die Bahnhöfe) / das Schloss (die Schlösser) / das Einkaufszentrum (die Einkaufszentren)"
                        ],
                        "translation": "Nhà ga (các nhà ga) / Lâu đài (các lâu đài) / Trung tâm thương mại (các trung tâm thương mại)."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 10: Phát biểu ngữ pháp nào dưới đây về danh từ 'die Bank' và 'die Post' là CHÍNH XÁC NHẤT?",
                "options": [
                        "Danh từ 'die Post' có dạng số nhiều thông dụng là 'die Posten', còn 'die Bank' không có số nhiều.",
                        "Danh từ 'die Post' (bưu điện) chỉ dùng ở số ít (nur Singular), còn 'die Bank' có số nhiều là 'die Banken' (các ngân hàng) hoặc 'die Bänke' (các ghế băng dài).",
                        "Cả 'die Post' và 'die Bank' đều mang giống trung (das).",
                        "Danh từ 'der Flughafen' mang giống trung vì chỉ địa điểm lớn."
                ],
                "correct_answer": "Danh từ 'die Post' (bưu điện) chỉ dùng ở số ít (nur Singular), còn 'die Bank' có số nhiều là 'die Banken' (các ngân hàng) hoặc 'die Bänke' (các ghế băng dài).",
                "explanation": "'die Post' (bưu điện) là danh từ chỉ dùng ở số ít (nur Singular). 'die Bank' khi mang nghĩa ngân hàng có số nhiều là die Banken, còn khi mang nghĩa ghế băng dài có số nhiều là die Bänke.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Danh từ 'die Post' (bưu điện) chỉ dùng ở số ít (nur Singular), còn 'die Bank' có số nhiều là 'die Banken' (các ngân hàng) hoặc 'die Bänke' (các ghế băng dài)."
                        ],
                        "translation": "die Post chỉ dùng ở số ít; die Bank có 2 dạng số nhiều: die Banken (ngân hàng) và die Bänke (ghế dài)."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 11: Nhóm danh lam thắng cảnh Berlin nào dưới đây có cả 3 địa danh đều mang GIỐNG TRUNG (das)?",
                "options": [
                        "der Reichstag, der Berliner Dom, der Fernsehturm",
                        "die Humboldt-Universität, die Staatsoper, die Museumsinsel",
                        "das Bundeskanzleramt, das Brandenburger Tor, das Schloss Bellevue",
                        "das Alexanderplatz, das Friedrichstraße, das Sony Center"
                ],
                "correct_answer": "das Bundeskanzleramt, das Brandenburger Tor, das Schloss Bellevue",
                "explanation": "Cả 3 địa danh này đều có danh từ gốc ở cuối mang giống trung: das Amt -> das Bundeskanzleramt, das Tor -> das Brandenburger Tor, das Schloss -> das Schloss Bellevue (và das Sony Center).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "das Bundeskanzleramt, das Brandenburger Tor, das Schloss Bellevue"
                        ],
                        "translation": "Phủ Thủ tướng Liên bang, Cổng Brandenburg, Cung điện Bellevue."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 12: Chọn cặp mạo từ đúng cho 2 địa danh nổi tiếng ở Berlin: '1. ___ Fernsehturm steht am Alexanderplatz. — 2. ___ Museumsinsel liegt im Zentrum von Berlin.'",
                "options": [
                        "Das / Die",
                        "Der / Die",
                        "Der / Das",
                        "Die / Der"
                ],
                "correct_answer": "Der / Die",
                "explanation": "der Turm (ngọn tháp) -> 'der Fernsehturm' (giống đực); die Insel (hòn đảo) -> 'die Museumsinsel' (giống cái).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Der / Die"
                        ],
                        "translation": "1. Tháp truyền hình nằm ở quảng trường Alexander. — 2. Đảo Bảo tàng nằm ở trung tâm Berlin."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 13: Chọn phương án đúng điền vào câu phân biệt 'zum' vs 'in den': 'Paula und Alex gehen zuerst ___ Brandenburger Tor (das Tor) und machen Fotos. Am Nachmittag gehen sie ___ Berliner Dom (der Dom) und hören ein Konzert.'",
                "options": [
                        "ins / zum",
                        "zum / in den",
                        "in das / im",
                        "zur / in der"
                ],
                "correct_answer": "zum / in den",
                "explanation": "Đi tới khu vực Cổng Brandenburg để chụp ảnh bên ngoài dùng zu + dem = 'zum Brandenburger Tor'. Đi hẳn vào bên trong Nhà thờ lớn Berlin (der Dom) nghe hòa nhạc dùng in + Akkusativ = 'in den Berliner Dom'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zum / in den"
                        ],
                        "translation": "Paula và Alex đầu tiên đi đến Cổng Brandenburg chụp ảnh. Buổi chiều họ đi vào Nhà thờ lớn Berlin nghe hòa nhạc."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 14: Chọn cặp từ đúng hoàn thành câu miêu tả chuyến tham quan Berlin: 'Die Touristen fahren mit dem Bus ___ Bundeskanzleramt (das Amt) vorbei und laufen dann ___ Schlossbrücke (die Brücke).'",
                "options": [
                        "ans / über der",
                        "am / über die",
                        "durch das / an der",
                        "beim / durch die"
                ],
                "correct_answer": "am / über die",
                "explanation": "Đi ngang qua das Bundeskanzleramt dùng an + dem ... vorbei = 'am Bundeskanzleramt vorbei'. Đi bộ qua cầu die Schlossbrücke (Wohin? + Akkusativ) dùng 'über die Schlossbrücke'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "am / über die"
                        ],
                        "translation": "Các du khách đi xe buýt ngang qua Phủ Thủ tướng và sau đó đi bộ qua cầu Schlossbrücke."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 15: Chọn cặp dạng chia đúng của động từ khuyết thiếu 'wollen': 'Wir ___ heute eine Stadtrundfahrt in Berlin machen, und danach ___ ich in die Alte Nationalgalerie gehen.'",
                "options": [
                        "wollt / will",
                        "wollen / will",
                        "wollen / wolle",
                        "will / wollen"
                ],
                "correct_answer": "wollen / will",
                "explanation": "Với động từ khuyết thiếu wollen, ngôi wir chia là 'wollen', còn ngôi ich biến đổi nguyên âm o -> i và không có đuôi thành 'will'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "wollen / will"
                        ],
                        "translation": "Hôm nay chúng tôi muốn đi tham quan thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia Cũ."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 16: Chọn phương án đúng hoàn thành câu đối thoại: 'Was ___ ihr heute Nachmittag machen? — Maria und ich ___ auf der Friedrichstraße bummeln.'",
                "options": [
                        "wollt / wollen",
                        "willst / wollen",
                        "wollen / wollt",
                        "wollt / will"
                ],
                "correct_answer": "wollt / wollen",
                "explanation": "Ngôi ihr (các bạn) chia là 'wollt'. Chủ ngữ ghép 'Maria und ich' tương đương với ngôi wir (chúng tôi) nên chia là 'wollen'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "wollt / wollen"
                        ],
                        "translation": "Chiều nay các bạn muốn làm gì? — Maria và tôi muốn đi dạo phố trên đường Friedrich."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 17: Chọn câu có cách chia động từ khuyết thiếu ĐÚNG NGỮ PHÁP 100%:",
                "options": [
                        "Mein Bruder willt nächstes Jahr in Deutschland studieren.",
                        "Am Wochenende musst meine Schwester im Krankenhaus arbeiten.",
                        "Lukas kann sehr gut kochen und will in Berlin ein Restaurant aufmachen.",
                        "Wir möchten heute Abend einen Film im Kino seht."
                ],
                "correct_answer": "Lukas kann sehr gut kochen und will in Berlin ein Restaurant aufmachen.",
                "explanation": "Ở ngôi thứ 3 số ít (Lukas = er), động từ können chia là 'kann' và wollen chia là 'will' (tuyệt đối không thêm -t), động từ chính kochen và aufmachen đứng nguyên mẫu ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Lukas kann sehr gut kochen und will in Berlin ein Restaurant aufmachen."
                        ],
                        "translation": "Lukas có thể nấu ăn rất giỏi và muốn mở một nhà hàng ở Berlin."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 18: Một du khách đứng ở nhà ga và muốn hỏi đường đi đến Nhà hát Opera Quốc gia (die Staatsoper). Câu hỏi nào dưới đây là ĐÚNG NGỮ PHÁP?",
                "options": [
                        "Entschuldigung, wie komme ich zum Staatsoper?",
                        "Entschuldigung, wie komme ich zur Staatsoper?",
                        "Entschuldigung, wo geht es in der Staatsoper?",
                        "Entschuldigung, ich suche der Staatsoper."
                ],
                "correct_answer": "Entschuldigung, wie komme ich zur Staatsoper?",
                "explanation": "Danh từ die Staatsoper mang giống cái (Femininum), nên khi đi với giới từ zu + Dativ phải dùng zu + der = 'zur Staatsoper' (hoặc nếu dùng in + Akkusativ thì là 'in die Staatsoper').",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Entschuldigung, wie komme ich zur Staatsoper?"
                        ],
                        "translation": "Xin lỗi, làm thế nào tôi đi đến được Nhà hát Opera Quốc gia?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 19: Quan sát Sơ đồ chỉ đường a) bên trên và điền từ chỉ hướng thích hợp vào chỗ trống: 'Gehen Sie zuerst 200 Meter ___!'",
                "options": null,
                "correct_answer": "geradeaus",
                "explanation": "Đi thẳng về phía trước trong tiếng Đức là 'geradeaus'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "geradeaus"
                        ],
                        "translation": "Ngài hãy đi thẳng 200 mét trước tiên!",
                        "visual_svg": "direction_card_a"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 20: Quan sát Sơ đồ chỉ đường h) bên trên và điền từ chỉ hướng thích hợp vào chỗ trống: 'An der Ampel gehen Sie bitte hier ___, nicht links!'",
                "options": null,
                "correct_answer": "rechts",
                "explanation": "Đối lập với links (bên trái) là 'rechts' (bên phải).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "rechts"
                        ],
                        "translation": "Tại đèn giao thông xin Ngài hãy rẽ phải ở đây, đừng rẽ trái!",
                        "visual_svg": "direction_card_h"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 21: Quan sát Sơ đồ chỉ đường bên trên và điền từ còn thiếu để hoàn thành cấu trúc 'đi ngang qua': 'Gehen Sie an der Humboldt-Universität ___ und dann die erste Straße links.'",
                "options": null,
                "correct_answer": "vorbei",
                "explanation": "Cấu trúc đi ngang qua một địa điểm là an + Dativ + 'vorbei'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "vorbei"
                        ],
                        "translation": "Ngài hãy đi ngang qua trường Đại học Humboldt rồi rẽ vào đường thứ nhất bên trái.",
                        "visual_svg": "spatial_diagram_vorbei"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 22: Điền giới từ thu gọn (an + dem) thích hợp vào chỗ trống: 'Der Sightseeing-Bus fährt ___ Bundeskanzleramt und ___ Reichstag vorbei.' (Gợi ý: das Bundeskanzleramt, der Reichstag)",
                "options": null,
                "correct_answer": "am",
                "explanation": "Cả das Bundeskanzleramt (giống trung) và der Reichstag (giống đực) khi đi với an + Dativ + vorbei đều gộp an + dem thành 'am'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "am"
                        ],
                        "translation": "Chiếc xe buýt tham quan chạy ngang qua Phủ Thủ tướng và tòa nhà Quốc hội."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 23: Quan sát Sơ đồ k) bên trên và điền giới từ chỉ sự xuyên qua (+ Akkusativ) vào chỗ trống: 'Die Besucher gehen ___ das Brandenburger Tor.'",
                "options": null,
                "correct_answer": "durch",
                "explanation": "Đi xuyên qua lòng cánh cổng vòm dùng giới từ 'durch' + Cách 4 (Akkusativ).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "durch",
                                "durchs"
                        ],
                        "translation": "Những người khách tham quan đi xuyên qua Cổng Brandenburg.",
                        "visual_svg": "direction_card_k"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 24: Quan sát Sơ đồ l) bên trên và điền giới từ chỉ hành động đi vượt qua mặt cầu vào chỗ trống: 'Paula und Alex laufen ___ die Schlossbrücke.'",
                "options": null,
                "correct_answer": "über",
                "explanation": "Đi qua cầu, qua đường, qua quảng trường dùng 'über + Akkusativ'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "über",
                                "ueber"
                        ],
                        "translation": "Paula và Alex đi bộ qua cầu Schlossbrücke.",
                        "visual_svg": "direction_card_l"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 25: Điền hậu tố giới từ chỉ đường 'dọc theo' đứng sau danh từ ở Akkusativ: 'Gehen Sie bitte den Fluss Spree ___ bis zur Museumsinsel!'",
                "options": null,
                "correct_answer": "entlang",
                "explanation": "Cấu trúc [Danh từ ở Akkusativ] + 'entlang' có nghĩa là đi dọc theo (den Fluss entlang, die Straße entlang).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "entlang"
                        ],
                        "translation": "Xin Ngài hãy đi dọc theo sông Spree cho đến Đảo Bảo tàng!"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 26: Điền cụm từ thu gọn (zu + der) vào chỗ trống: 'Gehen Sie immer geradeaus bis ___ zweiten Kreuzung!' (Gợi ý: die Kreuzung)",
                "options": null,
                "correct_answer": "zur",
                "explanation": "'bis zu' luôn đi với Cách 3 (Dativ). die Kreuzung mang giống cái nên zu + der viết tắt là 'zur' (bis zur zweiten Kreuzung).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zur"
                        ],
                        "translation": "Ngài cứ đi thẳng mãi cho đến ngã tư thứ hai!"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 27: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'In den Sommerferien ___ mein Sohn allein nach Berlin reisen.'",
                "options": null,
                "correct_answer": "will",
                "explanation": "Chủ ngữ 'mein Sohn' là ngôi thứ 3 số ít (er), động từ wollen chia thành 'will'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "will"
                        ],
                        "translation": "Trong kỳ nghỉ hè, con trai tôi muốn đi du lịch một mình đến Berlin.",
                        "dynamic_modal_wollen": true
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 28: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'Wohin ___ du heute Abend mit deinen Freunden gehen, Sofia?'",
                "options": null,
                "correct_answer": "willst",
                "explanation": "Ngôi thứ 2 số ít (du) của động từ wollen là 'willst'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "willst"
                        ],
                        "translation": "Tối nay bạn muốn đi đâu cùng với những người bạn của mình thế, Sofia?",
                        "dynamic_modal_wollen": true
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 29: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'Heute Abend ___ wir noch einen spannenden Film im Kino sehen.'",
                "options": null,
                "correct_answer": "wollen",
                "explanation": "Ngôi thứ nhất số nhiều (wir) của động từ wollen giữ nguyên là 'wollen'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "wollen"
                        ],
                        "translation": "Tối nay chúng tôi còn muốn xem một bộ phim hấp dẫn ở trong rạp chiếu phim.",
                        "dynamic_modal_wollen": true
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 30: Điền cụm giới từ + mạo từ (in + den) thích hợp vào chỗ trống: 'Am Nachmittag gehen die Touristen ___ Berliner Dom und hören ein Orgelkonzert.' (Gợi ý: der Berliner Dom)",
                "options": null,
                "correct_answer": "in den",
                "explanation": "Đi vào bên trong tòa nhà (Wohin? + Akkusativ) với danh từ giống đực der Berliner Dom dùng 'in den'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "in den"
                        ],
                        "translation": "Vào buổi chiều các du khách đi vào trong Nhà thờ lớn Berlin và nghe một buổi hòa nhạc đàn đại phong cầm.",
                        "dynamic_berlin_route": true
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 31: Điền cụm giới từ + mạo từ (in + die) thích hợp vào chỗ trống: 'Nach dem Abendessen gehen Paula und Alex ___ Disko ‚Von Euch‘.' (Gợi ý: die Disko)",
                "options": null,
                "correct_answer": "in die",
                "explanation": "die Disko mang giống cái, đi vào trong vũ trường (Wohin? + Akkusativ) dùng 'in die Disko'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "in die"
                        ],
                        "translation": "Sau bữa tối, Paula và Alex đi vào vũ trường 'Von Euch'."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 32: Điền giới từ thu gọn (zu + dem) thích hợp vào chỗ trống: 'Entschuldigung, wie komme ich am schnellsten ___ Hauptbahnhof?' (Gợi ý: der Hauptbahnhof)",
                "options": null,
                "correct_answer": "zum",
                "explanation": "der Hauptbahnhof mang giống đực, đi sau zu + Dativ gộp zu + dem thành 'zum Hauptbahnhof'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zum"
                        ],
                        "translation": "Xin lỗi, làm thế nào tôi đi đến được nhà ga trung tâm nhanh nhất?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 33: Điền dạng số nhiều đúng của danh từ 'das Schloss' (lâu đài, cung điện) vào chỗ trống: 'In Deutschland und Österreich gibt es viele alte ___.'",
                "options": null,
                "correct_answer": "Schlösser",
                "explanation": "Danh từ giống trung das Schloss khi chuyển sang số nhiều phải thêm Umlaut o -> ö và đuôi -er thành 'die Schlösser'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Schlösser",
                                "Schloesser"
                        ],
                        "translation": "Ở Đức và Áo có rất nhiều lâu đài cổ."
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 34: Dịch sang tiếng Đức (kèm mạo từ số ít): 'cảng biển'",
                "options": null,
                "correct_answer": "der Hafen",
                "explanation": "Cảng biển là danh từ giống đực der Hafen (số nhiều: die Häfen).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der Hafen",
                                "Hafen"
                        ],
                        "translation": "cảng biển: der Hafen"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 35: Dịch sang tiếng Đức (kèm mạo từ số ít): 'cây cầu'",
                "options": null,
                "correct_answer": "die Brücke",
                "explanation": "Cây cầu là danh từ giống cái die Brücke (số nhiều: die Brücken).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "die Brücke",
                                "die Bruecke",
                                "Brücke",
                                "Bruecke"
                        ],
                        "translation": "cây cầu: die Brücke"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 36: Dịch sang tiếng Đức (kèm mạo từ số ít): 'lâu đài / cung điện'",
                "options": null,
                "correct_answer": "das Schloss",
                "explanation": "Lâu đài / cung điện là danh từ giống trung das Schloss (số nhiều: die Schlösser).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "das Schloss",
                                "Schloss"
                        ],
                        "translation": "lâu đài, cung điện: das Schloss"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 37: Dịch sang tiếng Đức (kèm mạo từ số ít): 'trung tâm thương mại'",
                "options": null,
                "correct_answer": "das Einkaufszentrum",
                "explanation": "Trung tâm thương mại là danh từ giống trung das Einkaufszentrum (số nhiều: die Einkaufszentren).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "das Einkaufszentrum",
                                "Einkaufszentrum"
                        ],
                        "translation": "trung tâm thương mại: das Einkaufszentrum"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 38: Dịch sang tiếng Đức (kèm mạo từ số ít): 'cổng thành'",
                "options": null,
                "correct_answer": "das Stadttor",
                "explanation": "Cổng thành là danh từ ghép giống trung das Stadttor (số nhiều: die Stadttore).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "das Stadttor",
                                "Stadttor"
                        ],
                        "translation": "cổng thành: das Stadttor"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 39: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Tòa nhà Quốc hội Đức'",
                "options": null,
                "correct_answer": "der Reichstag",
                "explanation": "Tòa nhà Quốc hội ở Berlin là der Reichstag.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der Reichstag",
                                "Reichstag"
                        ],
                        "translation": "Tòa nhà Quốc hội Đức: der Reichstag"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 40: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Phủ Thủ tướng Đức'",
                "options": null,
                "correct_answer": "das Bundeskanzleramt",
                "explanation": "Phủ Thủ tướng Liên bang Đức là danh từ giống trung das Bundeskanzleramt.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "das Bundeskanzleramt",
                                "Bundeskanzleramt"
                        ],
                        "translation": "Phủ Thủ tướng Đức: das Bundeskanzleramt"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 41: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Đảo Bảo tàng'",
                "options": null,
                "correct_answer": "die Museumsinsel",
                "explanation": "Đảo Bảo tàng ở Berlin là danh từ giống cái die Museumsinsel.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "die Museumsinsel",
                                "Museumsinsel"
                        ],
                        "translation": "Đảo Bảo tàng: die Museumsinsel"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 42: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Tháp truyền hình'",
                "options": null,
                "correct_answer": "der Fernsehturm",
                "explanation": "Tháp truyền hình là danh từ giống đực der Fernsehturm.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "der Fernsehturm",
                                "Fernsehturm"
                        ],
                        "translation": "Tháp truyền hình: der Fernsehturm"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 43: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi cho đến đèn giao thông'",
                "options": null,
                "correct_answer": "bis zur Ampel gehen",
                "explanation": "Đèn giao thông là die Ampel -> 'cho đến đèn giao thông' là bis zur Ampel.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "bis zur Ampel gehen",
                                "bis zur Ampel",
                                "Gehen Sie bis zur Ampel"
                        ],
                        "translation": "đi cho đến đèn giao thông: bis zur Ampel gehen"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 44: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi ngang qua ngân hàng'",
                "options": null,
                "correct_answer": "an der Bank vorbei",
                "explanation": "Ngân hàng là die Bank -> cấu trúc an + Dativ + vorbei là an der Bank vorbei.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "an der Bank vorbei",
                                "an der Bank vorbeigehen",
                                "Gehen Sie an der Bank vorbei"
                        ],
                        "translation": "đi ngang qua ngân hàng: an der Bank vorbei"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 45: Dịch cụm từ chỉ hoạt động du lịch sau sang tiếng Đức: 'thực hiện một chuyến tham quan vòng quanh thành phố'",
                "options": null,
                "correct_answer": "eine Stadtrundfahrt machen",
                "explanation": "Chuyến tham quan thành phố là die Stadtrundfahrt -> eine Stadtrundfahrt machen.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "eine Stadtrundfahrt machen",
                                "Stadtrundfahrt machen"
                        ],
                        "translation": "thực hiện chuyến tham quan thành phố: eine Stadtrundfahrt machen"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 46: Dịch sang tiếng Việt: 'die Staatsoper'",
                "options": null,
                "correct_answer": "nhà hát Opera quốc gia",
                "explanation": "die Staatsoper là Nhà hát Opera Quốc gia tại Berlin.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "nhà hát Opera quốc gia",
                                "nhà hát nhạc kịch quốc gia",
                                "nhà hát opera nhà nước",
                                "nhà hát opera"
                        ],
                        "translation": "die Staatsoper: nhà hát Opera quốc gia"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 47: Dịch sang tiếng Việt: 'der Berliner Dom'",
                "options": null,
                "correct_answer": "nhà thờ lớn Berlin",
                "explanation": "der Berliner Dom là Nhà thờ lớn Berlin.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "nhà thờ lớn Berlin",
                                "nhà thờ chính tòa Berlin",
                                "thánh đường Berlin"
                        ],
                        "translation": "der Berliner Dom: nhà thờ lớn Berlin"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 48: Dịch sang tiếng Việt: 'die Alte Nationalgalerie'",
                "options": null,
                "correct_answer": "khu triển lãm quốc gia cũ",
                "explanation": "die Alte Nationalgalerie là Khu triển lãm Quốc gia (Cũ) nằm trên Đảo Bảo tàng ở Berlin.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "khu triển lãm quốc gia cũ",
                                "khu trưng bày nghệ thuật quốc gia",
                                "phòng triển lãm quốc gia cổ",
                                "khu triển lãm quốc gia"
                        ],
                        "translation": "die Alte Nationalgalerie: khu triển lãm quốc gia cũ"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 49: Dịch sang tiếng Việt: 'das Schloss Bellevue'",
                "options": null,
                "correct_answer": "cung điện Bellevue",
                "explanation": "das Schloss Bellevue là Cung điện Bellevue (nơi làm việc chính thức của Tổng thống Đức ở Berlin).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "cung điện Bellevue",
                                "lâu đài Bellevue"
                        ],
                        "translation": "das Schloss Bellevue: cung điện Bellevue"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 50: Dịch sang tiếng Việt: 'Gehen Sie die erste Straße rechts!'",
                "options": null,
                "correct_answer": "Ngài hãy rẽ phải ở con đường thứ nhất",
                "explanation": "die erste Straße rechts = rẽ phải ở con đường thứ nhất / đầu tiên.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Ngài hãy rẽ phải ở con đường thứ nhất",
                                "Hãy đi con đường đầu tiên bên phải",
                                "Rẽ phải ở đường đầu tiên",
                                "Ngài hãy đi đường thứ nhất bên tay phải"
                        ],
                        "translation": "Gehen Sie die erste Straße rechts!: Ngài hãy rẽ phải ở con đường thứ nhất"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 51: Dịch sang tiếng Việt: 'Gehen Sie bis zur zweiten Kreuzung und dort links!'",
                "options": null,
                "correct_answer": "Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái",
                "explanation": "bis zur zweiten Kreuzung und dort links = đi đến ngã tư thứ hai và rẽ trái ở đó (thì rẽ trái).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái",
                                "Ngài hãy đi tới ngã tư thứ hai thì rẽ trái",
                                "Ngài hãy đi cho đến ngã tư thứ hai và rẽ trái ở đó",
                                "Ngài hãy đi đến ngã tư thứ hai và rẽ trái ở đó",
                                "Đi đến ngã tư thứ hai rồi rẽ trái",
                                "Hãy đi tới ngã tư thứ hai bên trái",
                                "Đi đến ngã tư thứ hai rẽ trái"
                        ],
                        "translation": "Gehen Sie bis zur zweiten Kreuzung und dort links!: Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 52: Dịch sang tiếng Việt: 'Gehen Sie über den Platz und durch das Stadttor!'",
                "options": null,
                "correct_answer": "Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành",
                "explanation": "über den Platz = băng qua quảng trường; durch das Stadttor = xuyên qua cổng thành.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành",
                                "Hãy đi qua quảng trường và đi xuyên qua cổng thành",
                                "Đi qua quảng trường và xuyên qua cổng thành"
                        ],
                        "translation": "Gehen Sie über den Platz und durch das Stadttor!: Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 53: Dịch sang tiếng Việt: 'auf der Friedrichstraße bummeln'",
                "options": null,
                "correct_answer": "đi dạo phố trên đường Friedrich",
                "explanation": "Động từ bummeln có nghĩa là đi dạo phố, tản bộ ngắm cảnh/cửa hàng.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "đi dạo phố trên đường Friedrich",
                                "dạo chơi mua sắm trên phố Friedrich",
                                "tản bộ trên đường Friedrich",
                                "đi dạo trên đường Friedrich"
                        ],
                        "translation": "auf der Friedrichstraße bummeln: đi dạo phố trên đường Friedrich"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 54: Dịch sang tiếng Việt: 'Entschuldigung, wie komme ich ins Kino?'",
                "options": null,
                "correct_answer": "Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?",
                "explanation": "Wie komme ich ins Kino? là câu hỏi đường lịch sự để đi tới rạp chiếu phim.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?",
                                "Xin lỗi, tôi đi tới rạp chiếu phim bằng cách nào?",
                                "Xin lỗi, đi đến rạp chiếu phim như thế nào?",
                                "Xin lỗi làm sao tôi đến rạp chiếu phim?"
                        ],
                        "translation": "Entschuldigung, wie komme ich ins Kino?: Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 55: Dịch sang tiếng Việt: 'Zuerst — Dann — Danach — Anschließend'",
                "options": null,
                "correct_answer": "Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó",
                "explanation": "Bộ 4 trạng từ liên kết trình tự hành động khi chỉ đường và kể lịch trình.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó",
                                "Trước tiên, sau đó, tiếp theo, tiếp nối sau đó",
                                "Đầu tiên, sau đó, tiếp đó, sau cùng",
                                "Đầu tiên - Sau đó - Tiếp theo - Tiếp đó"
                        ],
                        "translation": "Zuerst - Dann - Danach - Anschließend: Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 56: Dịch sang tiếng Việt: 'mit dem Bus am Bundeskanzleramt vorbeifahren'",
                "options": null,
                "correct_answer": "đi xe buýt ngang qua Phủ Thủ tướng",
                "explanation": "mit dem Bus = bằng xe buýt; am Bundeskanzleramt vorbeifahren = đi/chạy xe ngang qua Phủ Thủ tướng.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "đi xe buýt ngang qua Phủ Thủ tướng",
                                "chạy xe buýt ngang qua Phủ Thủ tướng",
                                "đi xe bus ngang qua Phủ Thủ tướng"
                        ],
                        "translation": "mit dem Bus am Bundeskanzleramt vorbeifahren: đi xe buýt ngang qua Phủ Thủ tướng"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 57: Dịch sang tiếng Việt: 'die Straße entlanggehen'",
                "options": null,
                "correct_answer": "đi bộ dọc theo con đường",
                "explanation": "die Straße entlanggehen = đi bộ dọc theo chiều dài con đường.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "đi bộ dọc theo con đường",
                                "đi dọc theo con đường",
                                "đi dọc phố"
                        ],
                        "translation": "die Straße entlanggehen: đi bộ dọc theo con đường"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 58: Nối Sơ đồ Chỉ đường (Cột Trái) với Khẩu lệnh tiếng Đức tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "Symbol a (↑) = Gehen Sie geradeaus. | Symbol h (↱) = Gehen Sie hier rechts. | Symbol g (↰) = Gehen Sie hier links. | Symbol i (〰️) = Gehen Sie die Straße entlang.",
                "explanation": "Phân tích 4 biểu tượng sơ đồ: 1. Symbol a chỉ mũi tên đi thẳng (geradeaus). 2. Symbol h quẹo phải ngay tại ngã rẽ hiện tại (hier rechts). 3. Symbol g quẹo trái ngay tại ngã rẽ hiện tại (hier links). 4. Symbol i uốn lượn chạy dọc theo chiều dài con đường (die Straße entlang).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Symbol a (↑)",
                                        "right": "Gehen Sie geradeaus."
                                },
                                {
                                        "left": "Symbol h (↱)",
                                        "right": "Gehen Sie hier rechts."
                                },
                                {
                                        "left": "Symbol g (↰)",
                                        "right": "Gehen Sie hier links."
                                },
                                {
                                        "left": "Symbol i (〰️)",
                                        "right": "Gehen Sie die Straße entlang."
                                }
                        ],
                        "translation": "1. Symbol a (↑): Ngài hãy đi thẳng. | 2. Symbol h (↱): Ngài hãy rẽ phải ở đây. | 3. Symbol g (↰): Ngài hãy rẽ trái ở đây. | 4. Symbol i (〰️): Ngài hãy đi dọc theo con đường."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 59: Nối Sơ đồ Chỉ đường (Cột Trái) với Khẩu lệnh tiếng Đức tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "Symbol c (Ampel) = Gehen Sie bis zur Ampel. | Symbol d (Kreuzung) = Gehen Sie bis zur Kreuzung. | Symbol b (Kirche) = Gehen Sie an der Kirche vorbei. | Symbol f (Platz) = Gehen Sie über den Platz.",
                "explanation": "Phân tích 4 biểu tượng sơ đồ: 1. Symbol c dừng lại trước cột đèn giao thông (bis zur Ampel). 2. Symbol d dừng lại trước ngã tư (bis zur Kreuzung). 3. Symbol b đi lướt ngang qua mặt nhà thờ (an der Kirche vorbei). 4. Symbol f đi băng xuyên qua quảng trường tròn (über den Platz).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Symbol c (Ampel)",
                                        "right": "Gehen Sie bis zur Ampel."
                                },
                                {
                                        "left": "Symbol d (Kreuzung)",
                                        "right": "Gehen Sie bis zur Kreuzung."
                                },
                                {
                                        "left": "Symbol b (Kirche)",
                                        "right": "Gehen Sie an der Kirche vorbei."
                                },
                                {
                                        "left": "Symbol f (Platz)",
                                        "right": "Gehen Sie über den Platz."
                                }
                        ],
                        "translation": "1. Symbol c (Ampel): Ngài hãy đi cho đến đèn giao thông. | 2. Symbol d (Kreuzung): Ngài hãy đi cho đến ngã tư. | 3. Symbol b (Kirche): Ngài hãy đi ngang qua nhà thờ. | 4. Symbol f (Platz): Ngài hãy đi băng qua quảng trường."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 60: Nối Cặp Danh từ Địa điểm (Cột Trái) với Dạng Số nhiều tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "der Bahnhof & der Flughafen = die Bahnhöfe & die Flughäfen | das Schloss & das Krankenhaus = die Schlösser & die Krankenhäuser | das Einkaufszentrum & das Museum = die Einkaufszentren & die Museen | die Post = nur Singular (kein Plural)",
                "explanation": "Quy tắc số nhiều danh từ địa điểm: 1. der Bahnhof/Flughafen biến âm a -> ä và thêm đuôi -e (die Bahnhöfe, die Flughäfen). 2. das Schloss/Krankenhaus thêm Umlaut và đuôi -er (die Schlösser, die Krankenhäuser). 3. das Einkaufszentrum/Museum có đuôi -um đổi thành -en (die Einkaufszentren, die Museen). 4. die Post chỉ dùng ở số ít (nur Singular).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Bahnhof & der Flughafen",
                                        "right": "die Bahnhöfe & die Flughäfen"
                                },
                                {
                                        "left": "das Schloss & das Krankenhaus",
                                        "right": "die Schlösser & die Krankenhäuser"
                                },
                                {
                                        "left": "das Einkaufszentrum & das Museum",
                                        "right": "die Einkaufszentren & die Museen"
                                },
                                {
                                        "left": "die Post",
                                        "right": "nur Singular (kein Plural)"
                                }
                        ],
                        "translation": "1. der Bahnhof & der Flughafen: các nhà ga & các sân bay. | 2. das Schloss & das Krankenhaus: các lâu đài & các bệnh viện. | 3. das Einkaufszentrum & das Museum: các trung tâm thương mại & các viện bảo tàng. | 4. die Post: bưu điện (chỉ dùng ở số ít)."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 61: Nối Danh lam Thắng cảnh Berlin (Cột Trái) với Giống & Nhóm kiến trúc tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "der Reichstag & der Fernsehturm = Maskulinum: das Parlament & der Turm | der Berliner Dom & der Alexanderplatz = Maskulinum: die Kirche & der Platz | die Humboldt-Universität & die Staatsoper = Femininum: die Universität & die Oper | die Museumsinsel & die Friedrichstraße = Femininum: die Insel & die Straße",
                "explanation": "Quy tắc giống danh lam thắng cảnh: 1. der Tag -> der Reichstag, der Turm -> der Fernsehturm (đều giống đực). 2. der Dom -> der Berliner Dom, der Platz -> der Alexanderplatz (đều giống đực). 3. Đuôi -tät -> die Humboldt-Universität, die Oper -> die Staatsoper (đều giống cái). 4. die Insel -> die Museumsinsel, die Straße -> die Friedrichstraße (đều giống cái).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Reichstag & der Fernsehturm",
                                        "right": "Maskulinum: das Parlament & der Turm"
                                },
                                {
                                        "left": "der Berliner Dom & der Alexanderplatz",
                                        "right": "Maskulinum: die Kirche & der Platz"
                                },
                                {
                                        "left": "die Humboldt-Universität & die Staatsoper",
                                        "right": "Femininum: die Universität & die Oper"
                                },
                                {
                                        "left": "die Museumsinsel & die Friedrichstraße",
                                        "right": "Femininum: die Insel & die Straße"
                                }
                        ],
                        "translation": "1. der Reichstag & der Fernsehturm: Giống đực - Tòa nhà Quốc hội & Tháp truyền hình. | 2. der Berliner Dom & der Alexanderplatz: Giống đực - Nhà thờ lớn Berlin & Quảng trường Alexander. | 3. die Humboldt-Universität & die Staatsoper: Giống cái - Trường Đại học Humboldt & Nhà hát Opera Quốc gia. | 4. die Museumsinsel & die Friedrichstraße: Giống cái - Đảo Bảo tàng & Phố mua sắm Friedrich."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 62: Nối Danh lam Thắng cảnh Berlin (Cột Trái) với Giống & Chức năng tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "das Brandenburger Tor = Neutrum: das Tor im Zentrum | das Bundeskanzleramt = Neutrum: das moderne Regierungsamt | das Schloss Bellevue = Neutrum: das weiße Schloss an der Spree | die Alte Nationalgalerie = Femininum: die Galerie für Kunst",
                "explanation": "Quy tắc giống danh lam thắng cảnh: 1. das Tor -> das Brandenburger Tor (giống trung). 2. das Amt -> das Bundeskanzleramt (giống trung). 3. das Schloss -> das Schloss Bellevue (giống trung). 4. Hậu tố -ie luôn mang giống cái -> die Alte Nationalgalerie.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "das Brandenburger Tor",
                                        "right": "Neutrum: das Tor im Zentrum"
                                },
                                {
                                        "left": "das Bundeskanzleramt",
                                        "right": "Neutrum: das moderne Regierungsamt"
                                },
                                {
                                        "left": "das Schloss Bellevue",
                                        "right": "Neutrum: das weiße Schloss an der Spree"
                                },
                                {
                                        "left": "die Alte Nationalgalerie",
                                        "right": "Femininum: die Galerie für Kunst"
                                }
                        ],
                        "translation": "1. das Brandenburger Tor: Giống trung - Cổng thành ở trung tâm. | 2. das Bundeskanzleramt: Giống trung - Phủ Thủ tướng Liên bang. | 3. das Schloss Bellevue: Giống trung - Cung điện của Tổng thống Liên bang. | 4. die Alte Nationalgalerie: Giống cái - Khu triển lãm nghệ thuật."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 63: Nối Mẫu Câu Hỏi Đường (Cột Trái) với Cấu trúc Ngữ pháp tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "Entschuldigung, ich suche ... = + Akkusativ: den Bahnhof / das Kino | Entschuldigung, wo ist ...? = + Nominativ: der Bahnhof / das Kino | Entschuldigung, wie komme ich ...? = + zum Bahnhof / zur Post / ins Kino | Entschuldigung, wo geht es ...? = + zum Reichstag / zur Museumsinsel / ins Zentrum",
                "explanation": "Cấu trúc câu hỏi đường: 1. suchen đòi hỏi tân ngữ Cách 4 Akkusativ. 2. sein (ist) đi với chủ ngữ Cách 1 Nominativ. 3. wie komme ich hỏi phương hướng tới địa điểm (zu + Dativ hoặc in + Akkusativ). 4. wo geht es hỏi lối đi tới địa điểm (zum/zur/ins).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Entschuldigung, ich suche ...",
                                        "right": "+ Akkusativ: den Bahnhof / das Kino"
                                },
                                {
                                        "left": "Entschuldigung, wo ist ...?",
                                        "right": "+ Nominativ: der Bahnhof / das Kino"
                                },
                                {
                                        "left": "Entschuldigung, wie komme ich ...?",
                                        "right": "+ zum Bahnhof / zur Post / ins Kino"
                                },
                                {
                                        "left": "Entschuldigung, wo geht es ...?",
                                        "right": "+ zum Reichstag / zur Museumsinsel / ins Zentrum"
                                }
                        ],
                        "translation": "1. Entschuldigung, ich suche ...: Xin lỗi, tôi đang tìm + Cách 4 (Akkusativ). | 2. Entschuldigung, wo ist ...?: Xin lỗi, ở đâu vậy + Cách 1 (Nominativ). | 3. Entschuldigung, wie komme ich ...?: Làm thế nào tôi đến được + zum/zur/ins. | 4. Entschuldigung, wo geht es ...?: Đi lối nào để tới + zum/zur/ins."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 64: Nối Giới từ Không gian (Cột Trái) với Cách Ngữ pháp & Ví dụ tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "an ... vorbei = Dativ: an der Bank vorbei / am Dom vorbei | durch ... = Akkusativ: durch das Tor / durch den Park | über ... = Akkusativ: über die Brücke / über den Platz | ... entlang = Akkusativ: die Straße entlang / den Fluss entlang",
                "explanation": "Ngữ pháp giới từ chỉ đường: 1. an + Dativ + vorbei chỉ hành động đi ngang qua địa điểm. 2. durch luôn đi với Akkusativ chỉ việc đi xuyên qua. 3. über đi với Akkusativ khi có chuyển động băng qua bề mặt. 4. entlang đặt sau danh từ ở Akkusativ chỉ việc đi dọc theo chiều dài.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "an ... vorbei",
                                        "right": "Dativ: an der Bank vorbei / am Dom vorbei"
                                },
                                {
                                        "left": "durch ...",
                                        "right": "Akkusativ: durch das Tor / durch den Park"
                                },
                                {
                                        "left": "über ...",
                                        "right": "Akkusativ: über die Brücke / über den Platz"
                                },
                                {
                                        "left": "... entlang",
                                        "right": "Akkusativ: die Straße entlang / den Fluss entlang"
                                }
                        ],
                        "translation": "1. an ... vorbei: đi ngang qua bên cạnh + Cách 3 (Dativ). | 2. durch ...: đi xuyên qua lòng + Cách 4 (Akkusativ). | 3. über ...: đi băng qua mặt + Cách 4 (Akkusativ). | 4. ... entlang: đi dọc theo chiều dài (đứng sau danh từ ở Cách 4 Akkusativ)."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 65: Nối Chủ ngữ (Cột Trái) với Dạng chia đúng của Modalverb 'wollen' (Cột Phải):",
                "options": null,
                "correct_answer": "ich / er / sie / es (wollen) = will | du (wollen & müssen) = willst / musst | wir / sie / Sie (wollen & möchten) = wollen / möchten | ihr (wollen & können) = wollt / könnt",
                "explanation": "Quy tắc chia Modalverb: 1. Ngôi ich và er/sie/es luôn giống hệt nhau và không có đuôi -t (ich will, er will). 2. Ngôi du luôn có đuôi -st (du willst, du musst). 3. Ngôi wir và sie/Sie luôn giữ nguyên đuôi -en giống nguyên mẫu (wir wollen, sie möchten). 4. Ngôi ihr luôn có đuôi -t (ihr wollt, ihr könnt).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "ich / er / sie / es (wollen)",
                                        "right": "will"
                                },
                                {
                                        "left": "du (wollen & müssen)",
                                        "right": "willst / musst"
                                },
                                {
                                        "left": "wir / sie / Sie (wollen & möchten)",
                                        "right": "wollen / möchten"
                                },
                                {
                                        "left": "ihr (wollen & können)",
                                        "right": "wollt / könnt"
                                }
                        ],
                        "translation": "1. ich / er / sie / es (wollen): muốn (ngôi ich và er/sie/es bằng nhau: will). | 2. du (wollen & müssen): bạn muốn/phải (thêm đuôi -st: willst, musst). | 3. wir / sie / Sie (wollen & möchten): chúng tôi/họ/Ngài muốn (dạng nguyên mẫu: wollen, möchten). | 4. ihr (wollen & können): các bạn muốn/có thể (thêm đuôi -t: wollt, könnt)."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 66: Nối Vế đầu Chặng Khám Phá Berlin của Paula & Alex (Cột Trái) với Vế sau tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "Sie gehen zum Brandenburger Tor = und machen dort viele Fotos. | Sie fahren mit dem Bus am Bundeskanzleramt vorbei = und laufen über die Schlossbrücke. | Am Nachmittag gehen sie in den Berliner Dom = und hören ein Orgelkonzert. | Am Abend essen sie Pizza = und gehen danach in die Disko „Von Euch“.",
                "explanation": "Theo bài đọc Berlin sehen: 1. Paula và Alex đến Cổng Brandenburg chụp ảnh bên ngoài cổng (zum Brandenburger Tor). 2. Đi xe buýt ngang qua Phủ Thủ tướng (am Bundeskanzleramt vorbei) và qua cầu (über die Schlossbrücke). 3. Buổi chiều vào bên trong Nhà thờ lớn Berlin (in den Berliner Dom) nghe hòa nhạc. 4. Buổi tối ăn pizza và đi vào vũ trường (in die Disko).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Sie gehen zum Brandenburger Tor",
                                        "right": "und machen dort viele Fotos."
                                },
                                {
                                        "left": "Sie fahren mit dem Bus am Bundeskanzleramt vorbei",
                                        "right": "und laufen über die Schlossbrücke."
                                },
                                {
                                        "left": "Am Nachmittag gehen sie in den Berliner Dom",
                                        "right": "und hören ein Orgelkonzert."
                                },
                                {
                                        "left": "Am Abend essen sie Pizza",
                                        "right": "und gehen danach in die Disko „Von Euch“."
                                }
                        ],
                        "translation": "1. Họ đi đến Cổng Brandenburg: và chụp nhiều bức ảnh ở đó. | 2. Họ đi xe buýt ngang qua Phủ Thủ tướng: và đi bộ qua cầu Schlossbrücke. | 3. Vào buổi chiều họ đi vào Nhà thờ lớn Berlin: và nghe một buổi hòa nhạc đàn đại phong cầm. | 4. Vào buổi tối họ ăn pizza: và sau đó đi vào vũ trường 'Von Euch'."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 67: Nối Trạng từ Trình tự Thời gian (Cột Trái) với Hành động Chỉ đường trên Bản đồ (Cột Phải):",
                "options": null,
                "correct_answer": "Zuerst = gehen Sie geradeaus. | Dann = gehen Sie die erste Straße rechts, an der Bank vorbei. | Danach = gehen Sie bis zur zweiten Kreuzung und dort links, bis zur Ampel. | Rechts = sehen Sie die Post.",
                "explanation": "Khung trình tự chỉ đường Lộ trình 1: 1. Zuerst mở đầu hành trình đi thẳng từ điểm xuất phát. 2. Dann chỉ bước tiếp theo rẽ phải qua ngân hàng. 3. Danach chỉ chặng kế tiếp đi đến ngã tư thứ hai rẽ trái ở đó và đến đèn giao thông. 4. Rechts chỉ vị trí đích đến của tòa nhà bưu điện nằm bên tay phải.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Zuerst",
                                        "right": "gehen Sie geradeaus."
                                },
                                {
                                        "left": "Dann",
                                        "right": "gehen Sie die erste Straße rechts, an der Bank vorbei."
                                },
                                {
                                        "left": "Danach",
                                        "right": "gehen Sie bis zur zweiten Kreuzung und dort links, bis zur Ampel."
                                },
                                {
                                        "left": "Rechts",
                                        "right": "sehen Sie die Post."
                                }
                        ],
                        "translation": "1. Zuerst: Đầu tiên Ngài đi thẳng. | 2. Dann: Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. | 3. Danach: Tiếp theo Ngài đi đến ngã tư thứ hai và rẽ trái ở đó, đi cho đến đèn giao thông. | 4. Rechts: Ở bên phải Ngài sẽ nhìn thấy bưu điện."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 68: Quan sát Bản đồ Lộ trình 1 bên trên và điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Dann gehen Sie die erste Straße [1], an der Bank [2].' (Gợi ý: 'Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.')",
                "options": null,
                "correct_answer": "rechts / vorbei",
                "explanation": "Rẽ phải là 'rechts'; đi ngang qua ngân hàng là 'an der Bank vorbei'. Bạn cần điền đủ cả 2 từ ngăn cách bởi dấu /.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "rechts / vorbei",
                                "rechts/vorbei",
                                "rechts, vorbei"
                        ],
                        "translation": "Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.",
                        "visual_svg": "city_grid_map_quiz_1"
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 69: Quan sát Bản đồ Lộ trình 2 bên trên và điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Zuerst gehen Sie geradeaus, bis [1] zweiten Kreuzung rechts. Dann gehen Sie [2] die Kreuzung.' (Gợi ý: 'Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai bên phải, sau đó đi băng qua ngã tư.')",
                "options": null,
                "correct_answer": "zur / über",
                "explanation": "'Cho đến ngã tư thứ hai' là bis zur zweiten Kreuzung; 'băng qua ngã tư' là über die Kreuzung. Bạn cần điền đủ cả 2 từ ngăn cách bởi dấu /.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zur / über",
                                "zur/über",
                                "zur / ueber",
                                "zur/ueber"
                        ],
                        "translation": "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai bên phải, sau đó đi băng qua ngã tư.",
                        "visual_svg": "city_grid_map_quiz_2"
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Sie fahren mit dem Bus [1] Bundeskanzleramt vorbei und laufen [2] die Schlossbrücke.' (Gợi ý: 'Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.')",
                "options": null,
                "correct_answer": "am / über",
                "explanation": "das Bundeskanzleramt đi với an + Dativ + vorbei là 'am Bundeskanzleramt vorbei'; đi bộ qua cầu die Schlossbrücke là 'über die Schlossbrücke'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "am / über",
                                "am/über",
                                "am / ueber",
                                "am/ueber"
                        ],
                        "translation": "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 71: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Geht zuerst [1] das Brandenburger Tor und dann die Straße [2]!' (Gợi ý: 'Đầu tiên các bạn hãy đi xuyên qua Cổng Brandenburg rồi đi dọc theo con đường.')",
                "options": null,
                "correct_answer": "durch / entlang",
                "explanation": "Đi xuyên qua lòng cổng vòm là 'durch das Brandenburger Tor'; đi dọc theo con đường là 'die Straße entlang'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "durch / entlang",
                                "durch/entlang"
                        ],
                        "translation": "Đầu tiên các bạn hãy đi xuyên qua Cổng Brandenburg rồi đi dọc theo con đường!"
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 72: Điền 2 dạng chia đúng của động từ 'wollen' vào các chỗ trống (ngăn cách bởi dấu /): 'Wir [1] noch eine Stadtrundfahrt machen, und danach [2] ich in die Nationalgalerie gehen.'",
                "options": null,
                "correct_answer": "wollen / will",
                "explanation": "Ngôi wir chia là 'wollen', ngôi ich chia là 'will'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "wollen / will",
                                "wollen/will"
                        ],
                        "translation": "Chúng mình còn muốn làm một chuyến tham quan thành phố, và sau đó mình muốn đi vào Khu triển lãm Quốc gia."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 73: Điền 2 cụm từ thích hợp vào các chỗ trống (phân biệt 'zum' và 'in den', ngăn cách bởi dấu /): 'Am Vormittag gehen wir [1] Alexanderplatz, und am Nachmittag gehen wir [2] Berliner Dom.'",
                "options": null,
                "correct_answer": "zum / in den",
                "explanation": "Đi đến quảng trường dùng 'zum Alexanderplatz' (zu + dem); đi vào bên trong lòng nhà thờ lớn dùng 'in den Berliner Dom' (in + Akkusativ).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "zum / in den",
                                "zum/in den"
                        ],
                        "translation": "Buổi sáng chúng tôi đi đến Quảng trường Alexander, và buổi chiều chúng tôi đi vào trong Nhà thờ lớn Berlin."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Anschließend [1] Maria und ich auf der Friedrichstraße [2].' (Gợi ý: 'wollen', 'đi dạo phố')",
                "options": null,
                "correct_answer": "wollen / bummeln",
                "explanation": "Chủ ngữ 'Maria und ich' (wir) chia wollen ở vị trí số 2 là 'wollen', động từ nguyên mẫu 'bummeln' đứng cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "wollen / bummeln",
                                "wollen/bummeln"
                        ],
                        "translation": "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Entschuldigung, ich [1] das Kino. Wie komme ich [2] Kino?' (Gợi ý: 'tìm kiếm', 'đến rạp')",
                "options": null,
                "correct_answer": "suche / ins",
                "explanation": "'Tôi đang tìm' là ich suche; 'đến rạp chiếu phim' là ins Kino (in + das) hoặc zum Kino.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "suche / ins",
                                "suche/ins",
                                "suche / zum",
                                "suche/zum"
                        ],
                        "translation": "Xin lỗi, tôi đang tìm rạp chiếu phim. Làm thế nào tôi đi đến được rạp chiếu phim?"
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 76: Điền 2 động từ khuyết thiếu (müssen và wollen) chia theo ngôi 'ich' vào các chỗ trống (ngăn cách bởi dấu /): 'Am Wochenende [1] ich arbeiten, aber nächstes Jahr in Deutschland [2] ich studieren.'",
                "options": null,
                "correct_answer": "muss / will",
                "explanation": "Ngôi ich của müssen là 'muss', của wollen là 'will'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "muss / will",
                                "muss/will"
                        ],
                        "translation": "Vào cuối tuần tôi phải làm việc, nhưng sang năm ở Đức tôi muốn học đại học."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Gehen Sie bis zur [1]. Rechts [2] Sie die Post.' (Gợi ý: 'đèn giao thông', 'nhìn thấy')",
                "options": null,
                "correct_answer": "Ampel / sehen",
                "explanation": "Đèn giao thông là 'die Ampel' (bis zur Ampel); nhìn thấy là 'sehen Sie'.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Ampel / sehen",
                                "Ampel/sehen"
                        ],
                        "translation": "Ngài hãy đi cho đến đèn giao thông, ở bên phải Ngài sẽ nhìn thấy bưu điện."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 78: Nghe phát âm chuẩn de-DE và điền từ chỉ hướng còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "geradeaus",
                "explanation": "Từ chỉ hướng 'đi thẳng' trong tiếng Đức là 'geradeaus'.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Zuerst gehen Sie geradeaus und dann die erste Straße rechts, an der Bank vorbei.",
                        "display_sentence": "Zuerst gehen Sie ___ und dann die erste Straße rechts, an der Bank vorbei.",
                        "hint_vi": "Đầu tiên Ngài đi thẳng và sau đó rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.",
                        "accepted_answers": [
                                "geradeaus"
                        ],
                        "translation": "Đầu tiên Ngài đi thẳng và sau đó rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 79: Nghe phát âm chuẩn de-DE và điền danh từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Kreuzung",
                "explanation": "Danh từ 'die Kreuzung' có nghĩa là ngã tư, giao lộ (bis zur zweiten Kreuzung).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Gehen Sie bitte bis zur zweiten Kreuzung und dort links, danach bis zur Ampel.",
                        "display_sentence": "Gehen Sie bitte bis zur zweiten ___ und dort links, danach bis zur Ampel.",
                        "hint_vi": "Xin Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông.",
                        "accepted_answers": [
                                "Kreuzung"
                        ],
                        "translation": "Xin Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 80: Nghe phát âm chuẩn de-DE và điền giới từ thu gọn còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "zum",
                "explanation": "zu + dem Brandenburger Tor viết tắt là 'zum Brandenburger Tor'.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Paula und Alex gehen zum Brandenburger Tor und machen viele Fotos.",
                        "display_sentence": "Paula und Alex gehen ___ Brandenburger Tor und machen viele Fotos.",
                        "hint_vi": "Paula và Alex đi đến Cổng Brandenburg và chụp nhiều bức ảnh.",
                        "accepted_answers": [
                                "zum"
                        ],
                        "translation": "Paula và Alex đi đến Cổng Brandenburg và chụp nhiều bức ảnh."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 81: Nghe phát âm chuẩn de-DE và điền danh từ địa danh còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Bundeskanzleramt",
                "explanation": "Phủ Thủ tướng Liên bang Đức là 'das Bundeskanzleramt' (am Bundeskanzleramt vorbei).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke.",
                        "display_sentence": "Sie fahren mit dem Bus am ___ vorbei und laufen über die Schlossbrücke.",
                        "hint_vi": "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.",
                        "accepted_answers": [
                                "Bundeskanzleramt"
                        ],
                        "translation": "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 82: Nghe phát âm chuẩn de-DE và điền danh từ địa danh còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Dom",
                "explanation": "Nhà thờ lớn Berlin là 'der Berliner Dom' (in den Berliner Dom).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.",
                        "display_sentence": "Am Nachmittag gehen sie in den Berliner ___ und hören ein Konzert.",
                        "hint_vi": "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc.",
                        "accepted_answers": [
                                "Dom"
                        ],
                        "translation": "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 83: Nghe phát âm chuẩn de-DE và điền danh từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Stadtrundfahrt",
                "explanation": "Danh từ 'die Stadtrundfahrt' có nghĩa là chuyến tham quan vòng quanh thành phố.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Wir wollen heute eine Stadtrundfahrt in Berlin machen.",
                        "display_sentence": "Wir wollen heute eine ___ in Berlin machen.",
                        "hint_vi": "Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố ở Berlin.",
                        "accepted_answers": [
                                "Stadtrundfahrt"
                        ],
                        "translation": "Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố ở Berlin."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 84: Nghe phát âm chuẩn de-DE và điền động từ nguyên mẫu còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "bummeln",
                "explanation": "Động từ nguyên mẫu 'bummeln' có nghĩa là đi dạo phố, tản bộ ngắm cảnh.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
                        "display_sentence": "Anschließend wollen Maria und ich auf der Friedrichstraße ___.",
                        "hint_vi": "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.",
                        "accepted_answers": [
                                "bummeln"
                        ],
                        "translation": "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 85: Nghe phát âm chuẩn de-DE và điền danh từ còn thiếu vào chỗ trống:",
                "options": null,
                "correct_answer": "Kirche",
                "explanation": "Danh từ 'die Kirche' có nghĩa là nhà thờ (an der Kirche vorbei).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Gehen Sie bitte an der Kirche vorbei und dann über den Platz.",
                        "display_sentence": "Gehen Sie bitte an der ___ vorbei und dann über den Platz.",
                        "hint_vi": "Xin Ngài hãy đi ngang qua nhà thờ và sau đó đi băng qua quảng trường.",
                        "accepted_answers": [
                                "Kirche"
                        ],
                        "translation": "Xin Ngài hãy đi ngang qua nhà thờ và sau đó đi băng qua quảng trường."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 86: Nghe phát âm chuẩn de-DE và điền dạng chia của động từ 'wollen' vào chỗ trống:",
                "options": null,
                "correct_answer": "will",
                "explanation": "Động từ khuyết thiếu wollen chia ở ngôi thứ 3 số ít (mein Bruder) là 'will'.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "In Deutschland will mein Bruder an der Humboldt-Universität studieren.",
                        "display_sentence": "In Deutschland ___ mein Bruder an der Humboldt-Universität studieren.",
                        "hint_vi": "Ở Đức anh trai tôi muốn học đại học tại trường Đại học Humboldt.",
                        "accepted_answers": [
                                "will"
                        ],
                        "translation": "Ở Đức anh trai tôi muốn học đại học tại trường Đại học Humboldt."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 87: Dịch câu hỏi đường sau sang tiếng Đức: 'Xin lỗi, tôi đang tìm bưu điện. Làm thế nào tôi đi đến được bưu điện?'",
                "options": null,
                "correct_answer": "Entschuldigung, ich suche die Post. Wie komme ich zur Post?",
                "explanation": "die Post mang giống cái; sau ich suche (Akkusativ) là die Post, còn sau Wie komme ich ...? (zu + Dativ) là zur Post.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Entschuldigung, ich suche die Post. Wie komme ich zur Post?",
                                "Entschuldigung, ich suche die Post. Wo geht es zur Post?",
                                "Entschuldigen Sie, ich suche die Post. Wie komme ich zur Post?",
                                "Entschuldigung, ich suche die Post! Wie komme ich zur Post?",
                                "Entschuldigen Sie bitte, ich suche die Post. Wie komme ich zur Post?"
                        ],
                        "translation": "Xin lỗi, tôi đang tìm bưu điện. Làm thế nào tôi đi đến được bưu điện?"
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 88: Dịch câu chỉ đường sau sang tiếng Đức: 'Đầu tiên Ngài đi thẳng, sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.'",
                "options": null,
                "correct_answer": "Zuerst gehen Sie geradeaus, dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
                "explanation": "Zuerst gehen Sie geradeaus, die erste Straße rechts, và an der Bank vorbei (an + Dativ + vorbei).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Zuerst gehen Sie geradeaus, dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
                                "Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
                                "Gehen Sie zuerst geradeaus und dann die erste Straße rechts, an der Bank vorbei.",
                                "Zuerst gehen Sie geradeaus, dann die erste Straße rechts, an der Bank vorbei."
                        ],
                        "translation": "Đầu tiên Ngài đi thẳng, sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 89: Dịch câu chỉ đường sau sang tiếng Đức: 'Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông.'",
                "options": null,
                "correct_answer": "Gehen Sie bis zur zweiten Kreuzung und dort links, danach gehen Sie bis zur Ampel.",
                "explanation": "Đi đến ngã tư thứ hai và rẽ trái ở đó: 'bis zur zweiten Kreuzung und dort links'; cho đến đèn giao thông: 'bis zur Ampel' (bis zu + der Dativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie bis zur zweiten Kreuzung und dort links, danach gehen Sie bis zur Ampel.",
                                "Gehen Sie bis zur zweiten Kreuzung und dort links und danach bis zur Ampel.",
                                "Dann gehen Sie bis zur zweiten Kreuzung und dort links. Danach gehen Sie bis zur Ampel.",
                                "Gehen Sie bitte bis zur zweiten Kreuzung und dort links und danach bis zur Ampel.",
                                "Gehen Sie bitte bis zur zweiten Kreuzung und dort links, danach gehen Sie bis zur Ampel.",
                                "Gehen Sie bis zur zweiten Kreuzung links, danach gehen Sie bis zur Ampel.",
                                "Gehen Sie bis zur zweiten Kreuzung links und danach bis zur Ampel.",
                                "Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel."
                        ],
                        "translation": "Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 90: Dịch câu sau sang tiếng Đức: 'Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.'",
                "options": null,
                "correct_answer": "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke.",
                "explanation": "am Bundeskanzleramt vorbei (an + dem ... vorbei) và über die Schlossbrücke (über + Akkusativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke.",
                                "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und gehen über die Schlossbrücke.",
                                "Sie fahren mit dem Bus am Bundeskanzleramt vorbei, und laufen über die Schlossbrücke."
                        ],
                        "translation": "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 91: Dịch câu sau sang tiếng Đức: 'Chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia.'",
                "options": null,
                "correct_answer": "Wir wollen eine Stadtrundfahrt machen, und danach will ich in die Nationalgalerie gehen.",
                "explanation": "Wir wollen ... machen (ngôi wir) và Danach will ich ... gehen (ngôi ich đảo động từ lên vị trí số 2).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Wir wollen eine Stadtrundfahrt machen, und danach will ich in die Nationalgalerie gehen.",
                                "Wir wollen noch eine Stadtrundfahrt machen. Danach will ich in die Nationalgalerie gehen.",
                                "Wir wollen eine Stadtrundfahrt machen. Danach will ich in die Alte Nationalgalerie gehen.",
                                "Wir wollen eine Stadtrundfahrt machen und danach will ich in die Alte Nationalgalerie gehen."
                        ],
                        "translation": "Chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 92: Dịch câu sau sang tiếng Đức: 'Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.'",
                "options": null,
                "correct_answer": "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
                "explanation": "Anschließend đứng đầu câu đảo wollen lên vị trí số 2, động từ nguyên mẫu bummeln đứng ở cuối câu.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
                                "Danach wollen Maria und ich auf der Friedrichstraße bummeln.",
                                "Maria und ich wollen anschließend auf der Friedrichstraße bummeln.",
                                "Anschließend möchten Maria und ich auf der Friedrichstraße bummeln."
                        ],
                        "translation": "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 93: Dịch câu sau sang tiếng Đức: 'Ngài hãy đi xuyên qua Cổng Brandenburg và đi băng qua quảng trường.'",
                "options": null,
                "correct_answer": "Gehen Sie durch das Brandenburger Tor und über den Platz.",
                "explanation": "durch das Brandenburger Tor (durch + Akkusativ) và über den Platz (über + Akkusativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Gehen Sie durch das Brandenburger Tor und über den Platz.",
                                "Gehen Sie durch das Brandenburger Tor und gehen Sie über den Platz.",
                                "Bitte gehen Sie durch das Brandenburger Tor und über den Platz.",
                                "Gehen Sie durch das Brandenburger Tor, und über den Platz."
                        ],
                        "translation": "Ngài hãy đi xuyên qua Cổng Brandenburg và đi băng qua quảng trường."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 94: Dịch câu sau sang tiếng Việt: 'Zuerst gehen Sie geradeaus, bis zur zweiten Kreuzung rechts. Dann gehen Sie geradeaus, über die Kreuzung. Links sehen Sie die Post.'",
                "options": null,
                "correct_answer": "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện.",
                "explanation": "Đây là toàn bộ câu miêu tả Lộ trình số 2 trên bản đồ chỉ đường tới Bưu điện (die Post).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện.",
                                "Trước tiên hãy đi thẳng đến ngã tư thứ hai bên phải. Sau đó đi thẳng băng qua ngã tư. Bên trái bạn sẽ thấy bưu điện.",
                                "Đầu tiên Ngài đi thẳng tới ngã tư thứ hai bên tay phải, sau đó đi thẳng qua ngã tư, bên trái Ngài thấy bưu điện.",
                                "Đầu tiên bạn đi thẳng đến ngã tư thứ hai bên phải. Sau đó bạn đi thẳng qua ngã tư. Bên trái bạn sẽ thấy bưu điện."
                        ],
                        "translation": "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 95: Dịch câu sau sang tiếng Việt: 'Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin und gehen zuerst zum Brandenburger Tor.'",
                "options": null,
                "correct_answer": "Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg.",
                "explanation": "besuchen Freunde = thăm bạn bè; gehen zum Brandenburger Tor = đi đến Cổng Brandenburg.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg.",
                                "Paula và Alex tới từ Madrid, họ đến thăm bạn bè tại Berlin và trước tiên đi tới Cổng Brandenburg.",
                                "Paula và Alex đến từ Madrid. Họ đến thăm bạn bè ở Berlin và trước hết đi đến Cổng Brandenburg.",
                                "Paula và Alex đến từ Madrid. Họ thăm bạn bè ở Berlin và đầu tiên đi tới Cổng Brandenburg."
                        ],
                        "translation": "Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 96: Dịch câu sau sang tiếng Việt: 'Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert. Am Abend gehen sie in die Disko.'",
                "options": null,
                "correct_answer": "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường.",
                "explanation": "in den Berliner Dom = vào trong Nhà thờ lớn Berlin; in die Disko = vào trong vũ trường.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường.",
                                "Buổi chiều họ vào trong Nhà thờ lớn Berlin nghe hòa nhạc, buổi tối họ đi tới quán bar vũ trường.",
                                "Vào buổi chiều họ vào Nhà thờ lớn Berlin và nghe hòa nhạc. Vào buổi tối họ đi vào vũ trường.",
                                "Buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe hòa nhạc. Buổi tối họ đi vũ trường."
                        ],
                        "translation": "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 97: Dịch câu sau sang tiếng Việt: 'Gehen Sie bitte an der Kirche vorbei, dann die Lạch-Tray-Straße entlang bis zur Ampel!'",
                "options": null,
                "correct_answer": "Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!",
                "explanation": "an der Kirche vorbei = đi ngang qua nhà thờ; die Lạch-Tray-Straße entlang = đi dọc theo đường Lạch Tray; bis zur Ampel = cho đến đèn giao thông.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!",
                                "Hãy đi ngang qua nhà thờ rồi đi dọc đường Lạch Tray tới chỗ đèn giao thông!",
                                "Xin hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray đến đèn giao thông!",
                                "Xin bạn hãy đi ngang qua nhà thờ, sau đó đi dọc đường Lạch Tray cho đến đèn giao thông!"
                        ],
                        "translation": "Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 98: Dịch câu sau sang tiếng Việt: 'Heute Abend wollen wir noch einen Film im Kino sehen, aber am Wochenende muss ich arbeiten.'",
                "options": null,
                "correct_answer": "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc.",
                "explanation": "Kết hợp hai động từ khuyết thiếu: wollen (muốn - kế hoạch) và müssen (phải - nghĩa vụ công việc).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc.",
                                "Tối nay chúng mình còn muốn xem phim ở rạp nhưng cuối tuần mình phải đi làm.",
                                "Tối nay chúng tôi muốn xem một bộ phim trong rạp chiếu phim, nhưng cuối tuần tôi phải làm việc.",
                                "Tối nay chúng tôi còn muốn xem một bộ phim ở rạp chiếu phim, nhưng cuối tuần tôi phải làm việc."
                        ],
                        "translation": "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 99: Dịch câu sau sang tiếng Việt: 'Entschuldigung, wie komme ich zur Museumsinsel und zur Humboldt-Universität?'",
                "options": null,
                "correct_answer": "Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?",
                "explanation": "Cả die Museumsinsel và die Humboldt-Universität đều mang giống cái nên đi với zur (zu + der).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?",
                                "Xin lỗi cho hỏi tôi đi tới Đảo Bảo tàng và Đại học Humboldt bằng cách nào?",
                                "Xin lỗi, tôi đi đến Đảo Bảo tàng và trường Đại học Humboldt như thế nào?",
                                "Xin lỗi, làm sao để tôi đi đến Đảo Bảo tàng và trường Đại học Humboldt?"
                        ],
                        "translation": "Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 100: Dịch câu sau sang tiếng Việt: 'Die Touristen gehen durch das alte Stadttor, laufen über den Marktplatz und besichtigen das schöne Schloss.'",
                "options": null,
                "correct_answer": "Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ.",
                "explanation": "durch das alte Stadttor = xuyên qua cổng thành cổ; über den Marktplatz = băng qua quảng trường chợ; besichtigen das schöne Schloss = tham quan lâu đài/cung điện đẹp.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ.",
                                "Những người khách du lịch đi qua cổng thành cũ, băng qua quảng trường chợ và tham quan lâu đài tuyệt đẹp.",
                                "Các khách du lịch đi xuyên qua cổng thành cổ, đi bộ qua quảng trường chợ và tham quan lâu đài đẹp.",
                                "Du khách đi xuyên qua cổng thành cổ, đi bộ qua quảng trường chợ và tham quan cung điện đẹp."
                        ],
                        "translation": "Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ."
                }
        }
]

    exercises = []
    for ex in raw_exercises:
        ex_type = ex["type"]
        question = ex["question"]
        corr = ex["correct_answer"]
        exp = ex["explanation"]
        pts = ex["exp_reward"]
        opts = json.dumps(ex["options"], ensure_ascii=False) if ex["options"] else None
        extra = ex.get("extra_data")
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
    print("✅ Đã khởi tạo thành công Bài 8: 'Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_8()
