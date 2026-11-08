import os
import sys
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def build_full_lesson8_seed_script():
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
                            <script>
                                document.addEventListener("DOMContentLoaded", function() {
                                    if (typeof getSpatialDiagramSvg === 'function') {
                                        document.getElementById('svg-diag-vorbei').innerHTML = getSpatialDiagramSvg('vorbei', '100%', 150);
                                    }
                                });
                            </script>
                        </div>
                        <p class="text-xs text-slate-600">Đi ngang qua bên cạnh tòa nhà mà không rẽ vào trong: <i>an der Universität vorbei / am Dom vorbei</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-rose-100 text-rose-800">SƠ ĐỒ 2: durch + AKKUSATIV</span>
                        <div id="svg-diag-durch">
                            <script>
                                document.addEventListener("DOMContentLoaded", function() {
                                    if (typeof getSpatialDiagramSvg === 'function') {
                                        document.getElementById('svg-diag-durch').innerHTML = getSpatialDiagramSvg('durch', '100%', 150);
                                    }
                                });
                            </script>
                        </div>
                        <p class="text-xs text-slate-600">Đi xuyên qua chính giữa lòng cổng vòm hoặc công viên: <i>durch das Tor / durch den Park</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800">SƠ ĐỒ 3: über + AKKUSATIV</span>
                        <div id="svg-diag-ueber">
                            <script>
                                document.addEventListener("DOMContentLoaded", function() {
                                    if (typeof getSpatialDiagramSvg === 'function') {
                                        document.getElementById('svg-diag-ueber').innerHTML = getSpatialDiagramSvg('ueber', '100%', 150);
                                    }
                                });
                            </script>
                        </div>
                        <p class="text-xs text-slate-600">Đi vượt qua trên mặt cầu, mặt quảng trường: <i>über die Brücke / über den Platz</i>.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="text-xs font-black px-2.5 py-1 rounded-full bg-amber-100 text-amber-800">SƠ ĐỒ 4: AKKUSATIV + entlang</span>
                        <div id="svg-diag-entlang"></div>
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
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel. Rechts sehen Sie die Post.', 1.0)" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus. <b>Dann</b> gehen Sie die erste Straße rechts, <b>an der Bank vorbei</b>. <b>Dann</b> gehen Sie bis zur zweiten Kreuzung links. <b>Danach</b> gehen Sie <b>bis zur Ampel</b>. Rechts sehen Sie <b>die Post</b>.“</p>
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
        </div>

        <!-- HỌC PHẦN 4: MA TRẬN 4 ĐỘNG TỪ KHUYẾT THIẾU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Hệ Thống Ma Trận 4 Động Từ Khuyết Thiếu (möchten - können - müssen - wollen)</h4>
            </div>

            <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 text-xs sm:text-sm text-purple-950 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>⭐</span> Điểm Mới Trọng Tâm: Động từ khuyết thiếu 'wollen' (muốn — ý định/kế hoạch mạnh mẽ):</p>
                <p>Khác với <i>möchten</i> (muốn lịch sự khi gọi món hoặc mong ước), <b>wollen</b> diễn đạt kế hoạch hoặc quyết tâm chắc chắn. Biến âm: <b>o -> i</b> ở số ít: <i>ich will, du willst, er/sie/es will</i>. Lưu ý: ngôi <b>ich</b> bằng ngôi <b>er/sie/es</b> và không có đuôi <b>-t</b>!</p>
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
                    <p class="italic font-serif text-slate-800 leading-relaxed">„Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin. Sie gehen <b>zum Brandenburger Tor</b> und machen viele Fotos. Sie fahren mit dem Bus <b>am Bundeskanzleramt vorbei</b> und laufen <b>über die Schlossbrücke</b>. Am Nachmittag gehen sie <b>in den Berliner Dom</b> và hören ein Konzert. Am Abend essen sie Pizza und gehen danach <b>in die Disko</b> ‚Von Euch‘.“</p>
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
    return grammar_html

if __name__ == "__main__":
    print("Testing grammar HTML length:", len(build_full_lesson8_seed_script()))
