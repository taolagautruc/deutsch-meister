/**
 * DeutschMeister - Module Sơ Đồ Trực Quan & Tương Tác Perfekt SVG (Perfekt SVG Engine)
 * Dành riêng cho Bài 9 (A1): "Urlaub - Du lịch - Perfekt Präteritum (Quá khứ văn nói)"
 * 
 * Cung cấp 6 sơ đồ trực quan theo đặc tả kỹ thuật sư phạm chuẩn CEFR A1:
 * V1: Khung kẹp câu Perfekt (Satzklammer) với 4 ví dụ chuyển đổi linh hoạt & logic từng slide
 * V2: Sơ đồ 5 nhánh hình thành Partizip II (chuẩn công thức không ge- và ge- chèn giữa)
 * V3: Cây quyết định Trợ động từ HABEN hay SEIN (Quy tắc phân loại chuẩn xác)
 * V4: Trục thời gian Perfekt vs Präteritum (Văn nói vs Văn viết)
 * V5: Bản đồ hành trình sông Donau (Passau -> Linz -> Wien -> Budapest) tương tác
 * V6: Máy tính chẩn đoán Partizip II tương tác tra cứu từ nguồn chuẩn
 */

(function (global) {
    'use strict';

    // =========================================================================
    // DỮ LIỆU ĐỘNG TỪ BẢNG NGUỒN CHUẨN PERFEKT (Single Source of Truth)
    // =========================================================================
    const PERFEKT_VERBS = [
        { verb: "machen", type: "Quy tắc ge-t", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "gemacht", ex: "Wir haben gestern eine Radtour gemacht.", tr: "Hôm qua chúng tôi đã đi một chuyến đạp xe.", group: 1, step: "Không tiền tố, không đuôi -ieren -> ge + mach + t" },
        { verb: "besichtigen", type: "Tiền tố be- không tách", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "besichtigt", ex: "Im Urlaub haben wir ein altes Schloss besichtigt.", tr: "Trong kỳ nghỉ chúng tôi đã tham quan một lâu đài cổ.", group: 4, step: "Tiền tố không tách be- -> không ge- -> gốc + t" },
        { verb: "übernachten", type: "Tiền tố über- không tách + gốc -t", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "übernachtet", ex: "Die Familie hat in einer kleinen Pension übernachtet.", tr: "Gia đình đã ngủ lại trong một nhà nghỉ nhỏ.", group: 4, step: "Tiền tố über- không tách + đuôi gốc -t -> thêm -et" },
        { verb: "besuchen", type: "Tiền tố be- không tách", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "besucht", ex: "Im Sommer habe ich meine Großeltern besucht.", tr: "Vào mùa hè tôi đã đi thăm ông bà.", group: 4, step: "Tiền tố be- không tách -> không ge- -> gốc + t" },
        { verb: "einkaufen", type: "Động từ tách ein-", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "eingekauft", ex: "Am zweiten Tag haben wir auf dem Markt eingekauft.", tr: "Vào ngày thứ hai chúng tôi đã đi mua sắm ở chợ.", group: 5, step: "Tiền tố tách ein- -> ein + ge + kauf + t" },
        { verb: "fotografieren", type: "Đuôi -ieren (không ge-)", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "fotografiert", ex: "Er hat den Sonnenuntergang am Meer fotografiert.", tr: "Anh ấy đã chụp ảnh hoàng hôn bên bờ biển.", group: 3, step: "Đuôi -ieren -> không ge- -> gốc + t" },
        { verb: "erreichen", type: "Tiền tố er- không tách", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "erreicht", ex: "Wir haben das Reiseziel am Abend erreicht.", tr: "Chúng tôi đã đến được điểm đến vào buổi tối.", group: 4, step: "Tiền tố er- không tách -> không ge- -> gốc + t" },
        { verb: "wandern", type: "Quy tắc di chuyển (dùng sein)", aux: "ist", auxFull: "sein (chia ngôi thứ 3 số ít: ist)", p2: "gewandert", ex: "Mein Vater ist früher oft in den Bergen gewandert.", tr: "Ngày trước bố tôi thường đi bộ đường dài trên núi.", group: 1, step: "Di chuyển đổi vị trí -> trợ động từ sein -> ge + wander + t" },
        { verb: "zelten", type: "Gốc -t -> ge-et", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "gezeltet", ex: "Die Kinder haben im Garten gezeltet.", tr: "Những đứa trẻ đã cắm trại trong vườn.", group: 2, step: "Gốc zelt kết thúc bằng -t -> thêm -e- -> ge + zelt + et" },
        { verb: "probieren", type: "Đuôi -ieren", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "probiert", ex: "Hast du schon die Nudelsuppe probiert?", tr: "Bạn đã thử món súp mì chưa?", group: 3, step: "Đuôi -ieren -> không ge- -> probier + t" },
        { verb: "passieren", type: "Đuôi -ieren (đổi trạng thái, sein)", aux: "ist", auxFull: "sein (chia ngôi thứ 3 số ít: ist)", p2: "passiert", ex: "Im Urlaub ist etwas Lustiges passiert.", tr: "Trong kỳ nghỉ đã xảy ra một chuyện vui.", group: 3, step: "Đổi trạng thái/sự việc xảy ra -> trợ động từ sein -> passier + t" },
        { verb: "anschauen", type: "Động từ tách an-", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "angeschaut", ex: "Die Touristen haben die Altstadt angeschaut.", tr: "Các du khách đã ngắm phố cổ.", group: 5, step: "Tiền tố tách an- -> an + ge + schau + t" },
        { verb: "planen", type: "Quy tắc ge-t", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "geplant", ex: "Mein Onkel hat die Reise im Januar geplant.", tr: "Chú tôi đã lên kế hoạch cho chuyến đi vào tháng Giêng.", group: 1, step: "Quy tắc thông thường -> ge + plan + t" },
        { verb: "regnen", type: "Thời tiết, gốc -gn -> ge-et", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "geregnet", ex: "In den Alpen hat es drei Tage geregnet.", tr: "Ở dãy Alps trời đã mưa ba ngày.", group: 2, step: "Thời tiết (ngôi es hat) + gốc regn- -> ge + regn + et" },
        { verb: "bleiben", type: "Bất quy tắc (dùng sein)", aux: "ist", auxFull: "sein (chia ngôi thứ 3 số ít: ist)", p2: "geblieben", ex: "Meine Freunde sind nur einen Tag in der Stadt geblieben.", tr: "Các bạn tôi chỉ ở lại thành phố một ngày.", group: 6, step: "Thuộc nhóm đặc biệt sein/bleiben/werden -> dùng sein -> geblieben" },
        { verb: "fliegen", type: "Bất quy tắc chuyển động (sein)", aux: "ist", auxFull: "sein (chia ngôi thứ 3 số ít: ist)", p2: "geflogen", ex: "Sie sind von Frankfurt nach Hanoi geflogen.", tr: "Họ đã bay từ Frankfurt đến Hà Nội.", group: 6, step: "Chuyển động đổi vị trí bằng đường hàng không -> dùng sein -> geflogen" },
        { verb: "schwimmen", type: "Bất quy tắc chuyển động (sein)", aux: "ist", auxFull: "sein (chia ngôi thứ 3 số ít: ist)", p2: "geschwommen", ex: "Die Kinder sind zur Insel geschwommen.", tr: "Những đứa trẻ đã bơi tới hòn đảo.", group: 6, step: "Bơi lội di chuyển vị trí -> dùng sein -> geschwommen" },
        { verb: "treffen", type: "Bất quy tắc e -> i", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "getroffen", ex: "Am Strand habe ich eine Freundin getroffen.", tr: "Ở bãi biển tôi đã gặp một người bạn gái.", group: 6, step: "Bất quy tắc -> đổi nguyên âm e -> o -> hat getroffen" },
        { verb: "schlafen", type: "Bất quy tắc (trạng thái tại chỗ)", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "geschlafen", ex: "Wir haben im Zug gut geschlafen.", tr: "Chúng tôi đã ngủ ngon trên tàu.", group: 6, step: "Trạng thái kéo dài tại chỗ -> dùng haben -> hat geschlafen" },
        { verb: "anrufen", type: "Động từ tách an- + bất quy tắc", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "angerufen", ex: "Meine Mutter hat mich aus dem Urlaub angerufen.", tr: "Mẹ tôi đã gọi điện cho tôi từ kỳ nghỉ.", group: 5, step: "Tiền tố tách an- + bất quy tắc rufen -> an + ge + rufen" },
        { verb: "reisen", type: "Quy tắc di chuyển (sein)", aux: "ist", auxFull: "sein (chia ngôi thứ 3 số ít: ist)", p2: "gereist", ex: "Sie sind mit dem Zug durch Europa gereist.", tr: "Họ đã đi du lịch khắp châu Âu bằng tàu hỏa.", group: 1, step: "Đi du lịch/di chuyển -> dùng sein -> ist gereist" },
        { verb: "buchen", type: "Quy tắc ge-t", aux: "hat", auxFull: "haben (chia ngôi thứ 3 số ít: hat)", p2: "gebucht", ex: "Wir haben zwei Zimmer für drei Nächte gebucht.", tr: "Chúng tôi đã đặt hai phòng cho ba đêm.", group: 1, step: "Có tân ngữ đặt phòng -> dùng haben -> hat gebucht" }
    ];

    // =========================================================================
    // V1: SƠ ĐỒ KHUNG CÂU PERFEKT (SATZKLAMMER)
    // =========================================================================
    const SATZKLAMMER_EXAMPLES = [
        {
            title: "1. Câu khẳng định chuẩn (S ở vị trí 1)",
            isOpenPos1: false,
            pos1: "Wir",
            pos1Label: "VỊ TRÍ 1",
            pos1Sub: "Chủ ngữ (S)",
            pos2: "haben",
            pos2Label: "VỊ TRÍ 2 (NGOẶC MỞ)",
            pos2Sub: "Trợ động từ (chia theo S)",
            mid: "einen Ausflug ans Meer",
            midLabel: "MITTELFELD (Ở GIỮA)",
            midSub: "Tân ngữ & Nơi chốn",
            end: "gemacht.",
            endLabel: "CUỐI CÂU (NGOẶC ĐÓNG)",
            endSub: "ge + mach + t",
            explanation: "💡 Trợ động từ 'haben' đứng ở Vị trí 2 mở đầu khung kẹp, ôm trọn trạng ngữ/tân ngữ ở giữa (Mittelfeld) và đóng khung bằng Partizip II 'gemacht.' ở cuối câu.",
            fullDe: "Wir haben einen Ausflug ans Meer gemacht.",
            fullVi: "Chúng tôi đã đi dã ngoại ra biển."
        },
        {
            title: "2. Đảo ngữ với Trạng từ Thời gian (Vị trí 1)",
            isOpenPos1: false,
            pos1: "Gestern",
            pos1Label: "VỊ TRÍ 1",
            pos1Sub: "Thời gian (Position 1)",
            pos2: "bin",
            pos2Label: "VỊ TRÍ 2 (NGOẶC MỞ)",
            pos2Sub: "Trợ động từ (chia theo S)",
            mid: "ich mit dem Zug nach Berlin",
            midLabel: "MITTELFELD (Ở GIỮA)",
            midSub: "Chủ ngữ + Phương tiện + Nơi đến",
            end: "gefahren.",
            endLabel: "CUỐI CÂU (NGOẶC ĐÓNG)",
            endSub: "ge + fahr + en",
            explanation: "💡 Khi trạng từ thời gian 'Gestern' đứng ở vị trí 1, trợ động từ 'bin' vẫn bắt buộc đứng ở vị trí 2 (mở ngoặc), chủ ngữ 'ich' lùi vào trong Mittelfeld, và đóng khung bằng 'gefahren.' ở cuối câu.",
            fullDe: "Gestern bin ich mit dem Zug nach Berlin gefahren.",
            fullVi: "Hôm qua tôi đã đi tàu hỏa đến Berlin."
        },
        {
            title: "3. Câu hỏi Yes/No (Ja/Nein-Frage - Trợ động từ mở khung ở đầu câu)",
            isOpenPos1: true,
            pos1: "Hast",
            pos1Label: "ĐẦU CÂU (NGOẶC MỞ)",
            pos1Sub: "Trợ động từ (chia theo S)",
            pos2: "du",
            pos2Label: "VỊ TRÍ 2 (TRONG KHUNG)",
            pos2Sub: "Chủ ngữ (S)",
            mid: "viele Fotos im Urlaub",
            midLabel: "MITTELFELD (Ở GIỮA)",
            midSub: "Tân ngữ & Nơi chốn",
            end: "gemacht?",
            endLabel: "CUỐI CÂU (NGOẶC ĐÓNG)",
            endSub: "ge + mach + t?",
            explanation: "💡 Trong câu hỏi Yes/No (Ja/Nein-Frage), trợ động từ 'Hast' đảo lên vị trí 1 mở đầu khung kẹp, chủ ngữ 'du' và thông tin ở giữa và đóng khung bằng 'gemacht?' ở cuối câu.",
            fullDe: "Hast du viele Fotos im Urlaub gemacht?",
            fullVi: "Bạn đã chụp nhiều ảnh trong kỳ nghỉ chứ?"
        },
        {
            title: "4. Động từ tách (Tiền tố gắn liền trong Partizip II)",
            isOpenPos1: false,
            pos1: "Wir",
            pos1Label: "VỊ TRÍ 1",
            pos1Sub: "Chủ ngữ (S)",
            pos2: "haben",
            pos2Label: "VỊ TRÍ 2 (NGOẶC MỞ)",
            pos2Sub: "Trợ động từ (chia theo S)",
            mid: "auf dem Markt",
            midLabel: "MITTELFELD (Ở GIỮA)",
            midSub: "Trạng ngữ chỉ nơi chốn",
            end: "eingekauft.",
            endLabel: "CUỐI CÂU (NGOẶC ĐÓNG)",
            endSub: "Tiền tố (ein) + ge + gốc (kauft)",
            explanation: "💡 Khác với thì hiện tại ('Wir kaufen ... ein'), ở thì Perfekt tiền tố tách 'ein-' không đứng rời nữa mà gắn liền vào Partizip II với '-ge-' chèn ở giữa ('eingekauft').",
            fullDe: "Wir haben auf dem Markt eingekauft.",
            fullVi: "Chúng tôi đã mua sắm ở chợ."
        }
    ];

    let currentSatzklammerIdx = 0;

    function renderSatzklammerSvg(index = 0) {
        currentSatzklammerIdx = (index + SATZKLAMMER_EXAMPLES.length) % SATZKLAMMER_EXAMPLES.length;
        const ex = SATZKLAMMER_EXAMPLES[currentSatzklammerIdx];

        // Slide 3: Box 1 is Open (blue), Box 2 is inner (gray)
        const box1Fill = ex.isOpenPos1 ? "#0369a1" : "#1e293b";
        const box1Stroke = ex.isOpenPos1 ? "#38bdf8" : "#475569";
        const box1TitleColor = ex.isOpenPos1 ? "#bae6fd" : "#94a3b8";
        const box1SubColor = ex.isOpenPos1 ? "#e0f2fe" : "#64748b";

        const box2Fill = ex.isOpenPos1 ? "#1e293b" : "#0369a1";
        const box2Stroke = ex.isOpenPos1 ? "#475569" : "#38bdf8";
        const box2TitleColor = ex.isOpenPos1 ? "#94a3b8" : "#bae6fd";
        const box2SubColor = ex.isOpenPos1 ? "#64748b" : "#e0f2fe";

        // Arch start coordinates: if isOpenPos1 is true, start at x=90, else x=260
        const archStartX = ex.isOpenPos1 ? 90 : 260;
        const archLabelX = ex.isOpenPos1 ? 320 : 410;

        return `
        <div class="perfekt-visual-card p-4 rounded-2xl bg-slate-900 border border-slate-700/80 shadow-xl text-slate-100 my-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-blue-500/20 text-blue-400 border border-blue-500/30">V1</span>
                    <span class="font-extrabold text-sm text-slate-200">Sơ đồ Khung câu Perfekt (Satzklammer)</span>
                </div>
                <div class="flex items-center gap-1.5 text-xs">
                    <button onclick="window.switchSatzklammerExample(-1)" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold border border-slate-700 transition">◀ Trước</button>
                    <span class="px-2 py-1 font-mono text-slate-400 font-bold">${currentSatzklammerIdx + 1}/4</span>
                    <button onclick="window.switchSatzklammerExample(1)" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold border border-slate-700 transition">Sau ▶</button>
                </div>
            </div>

            <div class="mt-2 mb-3 text-xs text-amber-400 font-semibold flex items-center justify-between">
                <span>📌 ${ex.title}</span>
                <button onclick="speakGerman('${ex.fullDe.replace(/'/g, "\\'")}', 1.0)" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 border border-indigo-500/30 font-bold transition">
                    🔊 Nghe phát âm câu
                </button>
            </div>

            <div class="overflow-x-auto py-2">
                <svg viewBox="0 0 760 210" width="100%" height="210" class="min-w-[620px] font-sans">
                    <defs>
                        <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8" />
                        </marker>
                        <linearGradient id="bracket-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#38bdf8" />
                            <stop offset="100%" stop-color="#f43f5e" />
                        </linearGradient>
                    </defs>

                    <!-- Background Base -->
                    <rect x="0" y="0" width="760" height="210" rx="16" fill="#0f172a" />

                    <!-- Box 1 -->
                    <g transform="translate(20, 75)">
                        <rect width="140" height="85" rx="12" fill="${box1Fill}" stroke="${box1Stroke}" stroke-width="${ex.isOpenPos1 ? '2.5' : '2'}"/>
                        <text x="70" y="22" text-anchor="middle" fill="${box1TitleColor}" font-size="11" font-weight="800">${ex.pos1Label}</text>
                        <text x="70" y="52" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="900">${ex.pos1}</text>
                        <text x="70" y="74" text-anchor="middle" fill="${box1SubColor}" font-size="9" font-weight="600">${ex.pos1Sub}</text>
                    </g>

                    <!-- Box 2 -->
                    <g transform="translate(180, 75)">
                        <rect width="160" height="85" rx="12" fill="${box2Fill}" stroke="${box2Stroke}" stroke-width="${ex.isOpenPos1 ? '2' : '2.5'}"/>
                        <text x="80" y="22" text-anchor="middle" fill="${box2TitleColor}" font-size="11" font-weight="800">${ex.pos2Label}</text>
                        <text x="80" y="52" text-anchor="middle" fill="#ffffff" font-size="20" font-weight="900">${ex.pos2}</text>
                        <text x="80" y="74" text-anchor="middle" fill="${box2SubColor}" font-size="9" font-weight="600">${ex.pos2Sub}</text>
                    </g>

                    <!-- Box 3: Mittelfeld -->
                    <g transform="translate(360, 75)">
                        <rect width="200" height="85" rx="12" fill="#1e293b" stroke="#64748b" stroke-dasharray="4 3" stroke-width="1.8"/>
                        <text x="100" y="22" text-anchor="middle" fill="#94a3b8" font-size="11" font-weight="700">${ex.midLabel}</text>
                        <text x="100" y="52" text-anchor="middle" fill="#f1f5f9" font-size="14" font-weight="700">${ex.mid}</text>
                        <text x="100" y="74" text-anchor="middle" fill="#64748b" font-size="9">${ex.midSub}</text>
                    </g>

                    <!-- Box 4: Satzende -->
                    <g transform="translate(580, 75)">
                        <rect width="160" height="85" rx="12" fill="#be123c" stroke="#f43f5e" stroke-width="2.5"/>
                        <text x="80" y="22" text-anchor="middle" fill="#fecdd3" font-size="11" font-weight="800">${ex.endLabel}</text>
                        <text x="80" y="52" text-anchor="middle" fill="#ffffff" font-size="19" font-weight="900">${ex.end}</text>
                        <text x="80" y="74" text-anchor="middle" fill="#ffe4e6" font-size="9" font-weight="600">${ex.endSub}</text>
                    </g>

                    <!-- Satzklammer Curved Arch -->
                    <path d="M ${archStartX} 70 C ${archStartX} 20, 660 20, 660 70" fill="none" stroke="url(#bracket-grad)" stroke-width="3.5" stroke-dasharray="6 4" marker-end="url(#arrow-blue)"/>
                    <rect x="${archLabelX}" y="14" width="130" height="22" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="${archLabelX + 65}" y="29" text-anchor="middle" fill="#38bdf8" font-size="10.5" font-weight="800">KHUNG KẸP CÂU</text>
                </svg>
            </div>

            <div class="mt-2 p-3 rounded-xl bg-slate-800/80 border border-slate-700 text-xs flex flex-col gap-1.5">
                <div>
                    <span class="text-slate-400 font-medium">Bản dịch tiếng Việt:</span>
                    <span class="text-emerald-400 font-bold ml-1">„${ex.fullVi}“</span>
                </div>
                <div class="text-[11.5px] text-amber-200/90 leading-relaxed">
                    ${ex.explanation}
                </div>
            </div>
        </div>`;
    }

    // =========================================================================
    // V2: SƠ ĐỒ 5 NHÁNH HÌNH THÀNH PARTIZIP II
    // =========================================================================
    function renderPartizipFlowchartSvg() {
        return `
        <div class="perfekt-visual-card p-4 rounded-2xl bg-slate-900 border border-slate-700/80 shadow-xl text-slate-100 my-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">V2</span>
                    <span class="font-extrabold text-sm text-slate-200">Sơ đồ 5 nhánh hình thành Partizip II (Kèm Âm thanh Mẫu)</span>
                </div>
                <span class="text-xs text-slate-400">Chẩn đoán nhanh mọi động từ</span>
            </div>

            <p class="text-xs text-slate-300 mt-2">Bấm vào nút 🔊 ở từng nhóm để nghe phát âm chính xác cặp động từ nguyên mẫu và dạng Partizip II:</p>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 mt-3">
                <!-- Nhóm 1 -->
                <div class="p-3 rounded-xl bg-slate-800 border border-blue-500/40 shadow-xs">
                    <div class="flex items-center justify-between mb-1">
                        <span class="px-2 py-0.5 rounded-md text-[10px] font-black bg-blue-500/20 text-blue-400 border border-blue-500/30">NHÓM 1</span>
                        <button onclick="speakGerman('machen, gemacht; kaufen, gekauft; hören, gehört.', 1.0)" class="text-xs text-blue-300 hover:text-white px-2 py-0.5 rounded bg-blue-600/30 font-bold">🔊 Nghe</button>
                    </div>
                    <div class="text-xs font-bold text-slate-200">Động từ có quy tắc</div>
                    <div class="font-mono text-sm text-blue-400 font-extrabold mt-1">ge + gốc + t</div>
                    <div class="text-[11px] text-slate-300 mt-1">Ví dụ: machen → <b class="text-white">gemacht</b></div>
                    <div class="text-[10px] text-slate-400 mt-0.5">kaufen → gekauft, hören → gehört</div>
                </div>

                <!-- Nhóm 2 -->
                <div class="p-3 rounded-xl bg-slate-800 border border-emerald-500/40 shadow-xs">
                    <div class="flex items-center justify-between mb-1">
                        <span class="px-2 py-0.5 rounded-md text-[10px] font-black bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">NHÓM 2</span>
                        <button onclick="speakGerman('zelten, gezeltet; arbeiten, gearbeitet; regnen, geregnet.', 1.0)" class="text-xs text-emerald-300 hover:text-white px-2 py-0.5 rounded bg-emerald-600/30 font-bold">🔊 Nghe</button>
                    </div>
                    <div class="text-xs font-bold text-slate-200">Gốc kết thúc -t, -d, -gn</div>
                    <div class="font-mono text-sm text-emerald-400 font-extrabold mt-1">ge + gốc + et</div>
                    <div class="text-[11px] text-slate-300 mt-1">Ví dụ: zelten → <b class="text-white">gezeltet</b></div>
                    <div class="text-[10px] text-slate-400 mt-0.5">arbeiten → gearbeitet, regnen → geregnet</div>
                </div>

                <!-- Nhóm 3 -->
                <div class="p-3 rounded-xl bg-slate-800 border border-amber-500/40 shadow-xs">
                    <div class="flex items-center justify-between mb-1">
                        <span class="px-2 py-0.5 rounded-md text-[10px] font-black bg-amber-500/20 text-amber-400 border border-amber-500/30">NHÓM 3</span>
                        <button onclick="speakGerman('fotografieren, fotografiert; probieren, probiert; studieren, studiert.', 1.0)" class="text-xs text-amber-300 hover:text-white px-2 py-0.5 rounded bg-amber-600/30 font-bold">🔊 Nghe</button>
                    </div>
                    <div class="text-xs font-bold text-slate-200">Đuôi -ieren (KHÔNG có ge-)</div>
                    <div class="font-mono text-sm text-amber-400 font-extrabold mt-1">gốc + t</div>
                    <div class="text-[11px] text-slate-300 mt-1">Ví dụ: fotografieren → <b class="text-white">fotografiert</b></div>
                    <div class="text-[10px] text-slate-400 mt-0.5">probieren → probiert, studieren → studiert</div>
                </div>

                <!-- Nhóm 4 -->
                <div class="p-3 rounded-xl bg-slate-800 border border-purple-500/40 shadow-xs">
                    <div class="flex items-center justify-between mb-1">
                        <span class="px-2 py-0.5 rounded-md text-[10px] font-black bg-purple-500/20 text-purple-400 border border-purple-500/30">NHÓM 4</span>
                        <button onclick="speakGerman('besuchen, besucht; bezahlen, bezahlt; bekommen, bekommen; verstehen, verstanden.', 1.0)" class="text-xs text-purple-300 hover:text-white px-2 py-0.5 rounded bg-purple-600/30 font-bold">🔊 Nghe</button>
                    </div>
                    <div class="text-xs font-bold text-slate-200">Tiền tố KHÔNG tách (be-, ver-, er...)</div>
                    <div class="font-mono text-sm text-purple-400 font-extrabold mt-1">tiền tố + gốc + (e)t / en (KHÔNG có ge-)</div>
                    <div class="text-[11px] text-slate-300 mt-1">Có quy tắc: besuchen → <b class="text-white">besucht</b>, bezahlt</div>
                    <div class="text-[10px] text-slate-400 mt-0.5">Bất quy tắc: bekommen → bekommen, verstanden</div>
                </div>

                <!-- Nhóm 5 -->
                <div class="p-3 rounded-xl bg-slate-800 border border-cyan-500/40 shadow-xs">
                    <div class="flex items-center justify-between mb-1">
                        <span class="px-2 py-0.5 rounded-md text-[10px] font-black bg-cyan-500/20 text-cyan-400 border border-cyan-500/30">NHÓM 5</span>
                        <button onclick="speakGerman('einkaufen, eingekauft; abholen, abgeholt; mitnehmen, mitgenommen; aufstehen, aufgestanden.', 1.0)" class="text-xs text-cyan-300 hover:text-white px-2 py-0.5 rounded bg-cyan-600/30 font-bold">🔊 Nghe</button>
                    </div>
                    <div class="text-xs font-bold text-slate-200">Động từ TÁCH (ge chèn giữa)</div>
                    <div class="font-mono text-sm text-cyan-400 font-extrabold mt-1">tiền tố + ge + gốc + (e)t / en</div>
                    <div class="text-[11px] text-slate-300 mt-1">Có quy tắc: einkaufen → <b class="text-white">eingekauft</b>, abgeholt</div>
                    <div class="text-[10px] text-slate-400 mt-0.5">Bất quy tắc: mitgenommen, aufgestanden</div>
                </div>

                <!-- Nhóm 6 -->
                <div class="p-3 rounded-xl bg-slate-800 border border-rose-500/40 shadow-xs">
                    <div class="flex items-center justify-between mb-1">
                        <span class="px-2 py-0.5 rounded-md text-[10px] font-black bg-rose-500/20 text-rose-400 border border-rose-500/30">NHÓM 6</span>
                        <button onclick="speakGerman('fliegen, geflogen; gehen, gegangen; trinken, getrunken.', 1.0)" class="text-xs text-rose-300 hover:text-white px-2 py-0.5 rounded bg-rose-600/30 font-bold">🔊 Nghe</button>
                    </div>
                    <div class="text-xs font-bold text-slate-200">Bất quy tắc & Hỗn hợp</div>
                    <div class="font-mono text-sm text-rose-400 font-extrabold mt-1">ge + gốc đổi + en / t</div>
                    <div class="text-[11px] text-slate-300 mt-1">Ví dụ: fliegen → <b class="text-white">geflogen</b></div>
                    <div class="text-[10px] text-slate-400 mt-0.5">gehen → gegangen, trinken → getrunken</div>
                </div>
            </div>
        </div>`;
    }

    // =========================================================================
    // V3: CÂY QUYẾT ĐỊNH HABEN / SEIN (QUY TẮC PHÂN LOẠI CHUẨN XÁC)
    // =========================================================================
    function renderHabenSeinDecisionTreeSvg() {
        return `
        <div class="perfekt-visual-card p-4 rounded-2xl bg-slate-900 border border-slate-700/80 shadow-xl text-slate-100 my-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-amber-500/20 text-amber-400 border border-amber-500/30">V3</span>
                    <span class="font-extrabold text-sm text-slate-200">Cây quyết định: Chọn trợ động từ HABEN hay SEIN?</span>
                </div>
                <span class="text-xs text-amber-300 font-bold">Quy tắc phân loại chuẩn xác</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-3">
                <!-- Nhánh SEIN (Màu Cam) -->
                <div class="p-3.5 rounded-xl bg-amber-950/30 border border-amber-500/40 text-xs">
                    <div class="flex items-center justify-between mb-2 pb-2 border-b border-amber-500/30">
                        <div class="flex items-center gap-2">
                            <span class="w-6 h-6 rounded-full bg-amber-500 text-slate-950 font-black flex items-center justify-center text-xs">1</span>
                            <span class="font-extrabold text-amber-300 text-sm">CHỌN SEIN (bin, bist, ist, sind, seid) KHI:</span>
                        </div>
                    </div>
                    <ul class="space-y-2 text-slate-200">
                        <li class="flex items-start gap-1.5">
                            <span class="text-amber-400 font-bold">✓</span>
                            <div>
                                <b class="text-white">1. Chuyển động thay đổi vị trí từ A đến B:</b>
                                <div class="text-slate-300 text-[11px] font-mono mt-0.5">fahren, fliegen, gehen, kommen, reisen, wandern, schwimmen, laufen</div>
                                <button onclick="speakGerman('fahren, fliegen, gehen, kommen, reisen, wandern, schwimmen, laufen', 1.0)" class="mt-1 px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold border border-amber-500/30">🔊 Nghe nhóm chuyển động</button>
                            </div>
                        </li>
                        <li class="flex items-start gap-1.5">
                            <span class="text-amber-400 font-bold">✓</span>
                            <div>
                                <b class="text-white">2. Thay đổi trạng thái:</b>
                                <div class="text-slate-300 text-[11px] font-mono mt-0.5">aufstehen (thức dậy), einschlafen (ngủ thiếp đi), aufwachen (tỉnh giấc), schmelzen (tan chảy), gefrieren (đông đá)</div>
                                <button onclick="speakGerman('aufstehen, einschlafen, aufwachen, schmelzen, gefrieren', 1.0)" class="mt-1 px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold border border-amber-500/30">🔊 Nghe nhóm đổi trạng thái</button>
                            </div>
                        </li>
                        <li class="flex items-start gap-1.5">
                            <span class="text-amber-400 font-bold">✓</span>
                            <div>
                                <b class="text-white">3. Động từ cố định đi với sein:</b>
                                <div class="text-slate-300 text-[11px] font-mono mt-0.5">sein (ist gewesen), bleiben (ist geblieben), werden (ist geworden), passieren (ist passiert)</div>
                                <button onclick="speakGerman('sein, ist gewesen; bleiben, ist geblieben; werden, ist geworden; passieren, ist passiert', 1.0)" class="mt-1 px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold border border-amber-500/30">🔊 Nghe nhóm cố định sein</button>
                            </div>
                        </li>
                    </ul>
                </div>

                <!-- Nhánh HABEN (Màu Xanh lá) -->
                <div class="p-3.5 rounded-xl bg-emerald-950/30 border border-emerald-500/40 text-xs">
                    <div class="flex items-center justify-between mb-2 pb-2 border-b border-emerald-500/30">
                        <div class="flex items-center gap-2">
                            <span class="w-6 h-6 rounded-full bg-emerald-500 text-slate-950 font-black flex items-center justify-center text-xs">2</span>
                            <span class="font-extrabold text-emerald-300 text-sm">CHỌN HABEN (habe, hast, hat, haben, habt) KHI:</span>
                        </div>
                    </div>
                    <ul class="space-y-2 text-slate-200">
                        <li class="flex items-start gap-1.5">
                            <span class="text-emerald-400 font-bold">✓</span>
                            <div>
                                <b class="text-white">1. Động từ có tân ngữ Akkusativ:</b>
                                <div class="text-slate-300 text-[11px] font-mono mt-0.5">machen, besichtigen, kaufen, essen, trinken, fotografieren, planen</div>
                                <button onclick="speakGerman('machen, besichtigen, kaufen, essen, trinken, fotografieren, planen', 1.0)" class="mt-1 px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold border border-emerald-500/30">🔊 Nghe nhóm tân ngữ</button>
                            </div>
                        </li>
                        <li class="flex items-start gap-1.5">
                            <span class="text-emerald-400 font-bold">✓</span>
                            <div>
                                <b class="text-white">2. Hoạt động hoặc trạng thái tại chỗ:</b>
                                <div class="text-slate-300 text-[11px] font-mono mt-0.5">schlafen (ngủ), wohnen (ở), arbeiten (làm việc), übernachten (ngủ lại), warten (chờ)</div>
                                <button onclick="speakGerman('schlafen, wohnen, arbeiten, übernachten, warten', 1.0)" class="mt-1 px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold border border-emerald-500/30">🔊 Nghe nhóm tại chỗ</button>
                            </div>
                        </li>
                        <li class="flex items-start gap-1.5">
                            <span class="text-emerald-400 font-bold">✓</span>
                            <div>
                                <b class="text-white">3. Hiện tượng thời tiết (ngôi es):</b>
                                <div class="text-slate-300 text-[11px] font-mono mt-0.5">es hat geregnet (mưa), es hat geschneit (tuyết rơi)</div>
                                <button onclick="speakGerman('es hat geregnet, es hat geschneit', 1.0)" class="mt-1 px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold border border-emerald-500/30">🔊 Nghe nhóm thời tiết</button>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>`;
    }

    // =========================================================================
    // V4: TRỤC THỜI GIAN PERFEKT / PRÄTERITUM (Mục 4)
    // =========================================================================
    function renderTimelineSvg() {
        return `
        <div class="perfekt-visual-card p-4 rounded-2xl bg-slate-900 border border-slate-700/80 shadow-xl text-slate-100 my-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-indigo-500/20 text-indigo-400 border border-indigo-500/30">V4</span>
                    <span class="font-extrabold text-sm text-slate-200">Trục thời gian: Perfekt (Văn nói) vs Präteritum (Văn viết)</span>
                </div>
            </div>

            <div class="overflow-x-auto py-3">
                <svg viewBox="0 0 760 170" width="100%" height="170" class="min-w-[620px]">
                    <rect width="760" height="170" rx="14" fill="#0f172a" />

                    <!-- Trục thời gian chính -->
                    <line x1="50" y1="100" x2="710" y2="100" stroke="#475569" stroke-width="4" stroke-linecap="round"/>
                    <polygon points="718,100 706,94 706,106" fill="#475569" />

                    <!-- Điểm JETZT (Hiện tại) -->
                    <line x1="540" y1="50" x2="540" y2="150" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4 3"/>
                    <circle cx="540" cy="100" r="7" fill="#38bdf8" />
                    <text x="540" y="40" text-anchor="middle" fill="#38bdf8" font-size="12" font-weight="900">JETZT (HIỆN TẠI)</text>
                    <text x="540" y="130" text-anchor="middle" fill="#94a3b8" font-size="10">Präsens</text>
                    <text x="540" y="148" text-anchor="middle" fill="#f1f5f9" font-size="11" font-weight="700">„Ich mache Fotos.“</text>

                    <!-- Vùng QUÁ KHỨ (Vergangenheit) -->
                    <text x="260" y="28" text-anchor="middle" fill="#f43f5e" font-size="12" font-weight="900">VERGANGENHEIT (QUÁ KHỨ)</text>

                    <!-- Tầng 1: PERFEKT (Văn nói) -->
                    <rect x="70" y="42" width="400" height="24" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="80" y="58" fill="#38bdf8" font-size="10" font-weight="800">PERFEKT (Văn nói hằng ngày):</text>
                    <text x="265" y="58" fill="#ffffff" font-size="11" font-weight="700">„Ich habe Fotos gemacht.“</text>

                    <!-- Tầng 2: PRÄTERITUM (Văn viết) -->
                    <rect x="70" y="70" width="400" height="24" rx="6" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
                    <text x="80" y="86" fill="#c084fc" font-size="10" font-weight="800">PRÄTERITUM (Sách báo / Văn viết):</text>
                    <text x="265" y="86" fill="#e2e8f0" font-size="11">„Ich machte Fotos.“</text>

                    <!-- Điểm đặc biệt: sein & haben -->
                    <rect x="70" y="112" width="400" height="34" rx="8" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
                    <text x="270" y="126" text-anchor="middle" fill="#fbbf24" font-size="10.5" font-weight="800">⭐ ĐẶC BIỆT KHI NÓI: sein & haben DÙNG PRÄTERITUM</text>
                    <text x="270" y="140" text-anchor="middle" fill="#fef3c7" font-size="11" font-weight="700">„Ich war am Meer.“ • „Wir hatten viel Spaß.“</text>

                    <!-- Tương lai -->
                    <text x="650" y="80" text-anchor="middle" fill="#64748b" font-size="11" font-weight="700">ZUKUNFT</text>
                    <text x="650" y="96" text-anchor="middle" fill="#475569" font-size="10">(Tương lai)</text>
                </svg>
            </div>
        </div>`;
    }

    // =========================================================================
    // V5: BẢN ĐỒ HÀNH TRÌNH SÔNG DONAU (Mục 5)
    // =========================================================================
    const DONAU_STOPS = [
        {
            id: "passau",
            city: "Passau (Đức)",
            icon: "🚴",
            title: "Khởi hành chuyến đạp xe",
            de: "Familie Müller hat eine Radtour von Passau nach Linz gemacht. Sie sind mit dem Rad gefahren.",
            vi: "Gia đình Müller đã bắt đầu chuyến đi xe đạp từ Passau đến Linz. Họ đã đạp xe đi."
        },
        {
            id: "linz",
            city: "Linz (Áo)",
            icon: "🏨 ⛪",
            title: "Nghỉ ngơi & Tham quan",
            de: "In Linz haben sie in einer Pension übernachtet und ein altes Kloster besichtigt.",
            vi: "Ở Linz họ đã ngủ lại trong một nhà nghỉ và đã tham quan một tu viện cổ."
        },
        {
            id: "wien",
            city: "Wien (Thủ đô Áo)",
            icon: "🏛️ 📷",
            title: "Khám phá thủ đô",
            de: "In Wien haben sie das Rathaus besucht und fotografiert. Das Wetter war prima.",
            vi: "Ở Wien họ đã thăm tòa thị chính và chụp ảnh. Thời tiết đã rất đẹp."
        },
        {
            id: "budapest",
            city: "Budapest (Hungary)",
            icon: "🏁 🏆",
            title: "Về đích hoàn thành chuyến đi",
            de: "In Budapest hat die Familie ihr Ziel erreicht. Die Radtour war wunderbar!",
            vi: "Tại Budapest gia đình đã đến được đích. Chuyến đạp xe thật tuyệt vời!"
        }
    ];

    let currentDonauStopIdx = 0;

    function renderDonauRouteMapSvg(activeIdx = 0) {
        currentDonauStopIdx = activeIdx;
        const currentStop = DONAU_STOPS[currentDonauStopIdx];

        return `
        <div class="perfekt-visual-card p-4 rounded-2xl bg-slate-900 border border-slate-700/80 shadow-xl text-slate-100 my-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-cyan-500/20 text-cyan-400 border border-cyan-500/30">V5</span>
                    <span class="font-extrabold text-sm text-slate-200">Bản đồ tương tác Hành trình sông Donau (Passau → Linz → Wien → Budapest)</span>
                </div>
                <button onclick="window.readFullDonauRoute()" class="px-3 py-1 rounded-xl bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
                    ▶ Đọc cả hành trình
                </button>
            </div>

            <!-- SVG Sông Donau -->
            <div class="overflow-x-auto py-2">
                <svg viewBox="0 0 760 170" width="100%" height="170" class="min-w-[620px]">
                    <rect width="760" height="170" rx="14" fill="#0f172a" />

                    <!-- Dòng sông Donau uốn lượn màu xanh dương -->
                    <path d="M 40 105 Q 160 55, 270 95 T 510 85 T 720 110" fill="none" stroke="#0284c7" stroke-width="26" stroke-linecap="round"/>
                    <path d="M 40 105 Q 160 55, 270 95 T 510 85 T 720 110" fill="none" stroke="#38bdf8" stroke-width="5" stroke-dasharray="8 6"/>

                    <!-- 4 Điểm dừng -->
                    <!-- 1. Passau -->
                    <g onclick="window.selectDonauStop(0)" class="cursor-pointer">
                        <circle cx="90" cy="95" r="16" fill="${currentDonauStopIdx === 0 ? '#38bdf8' : '#1e293b'}" stroke="#38bdf8" stroke-width="3"/>
                        <text x="90" y="100" text-anchor="middle" font-size="13">🚴</text>
                        <text x="90" y="135" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">1. Passau</text>
                        <text x="90" y="150" text-anchor="middle" fill="#94a3b8" font-size="10">Đức</text>
                    </g>

                    <!-- 2. Linz -->
                    <g onclick="window.selectDonauStop(1)" class="cursor-pointer">
                        <circle cx="270" cy="95" r="16" fill="${currentDonauStopIdx === 1 ? '#38bdf8' : '#1e293b'}" stroke="#38bdf8" stroke-width="3"/>
                        <text x="270" y="100" text-anchor="middle" font-size="13">🏨</text>
                        <text x="270" y="135" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">2. Linz</text>
                        <text x="270" y="150" text-anchor="middle" fill="#94a3b8" font-size="10">Áo</text>
                    </g>

                    <!-- 3. Wien -->
                    <g onclick="window.selectDonauStop(2)" class="cursor-pointer">
                        <circle cx="490" cy="85" r="16" fill="${currentDonauStopIdx === 2 ? '#38bdf8' : '#1e293b'}" stroke="#38bdf8" stroke-width="3"/>
                        <text x="490" y="90" text-anchor="middle" font-size="13">🏛️</text>
                        <text x="490" y="125" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">3. Wien</text>
                        <text x="490" y="140" text-anchor="middle" fill="#94a3b8" font-size="10">Thủ đô Áo</text>
                    </g>

                    <!-- 4. Budapest -->
                    <g onclick="window.selectDonauStop(3)" class="cursor-pointer">
                        <circle cx="670" cy="110" r="16" fill="${currentDonauStopIdx === 3 ? '#10b981' : '#1e293b'}" stroke="#10b981" stroke-width="3"/>
                        <text x="670" y="115" text-anchor="middle" font-size="13">🏁</text>
                        <text x="670" y="145" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="800">4. Budapest</text>
                        <text x="670" y="160" text-anchor="middle" fill="#94a3b8" font-size="10">Hungary (Đích)</text>
                    </g>
                </svg>
            </div>

            <!-- Thẻ hiển thị chặng được chọn -->
            <div id="donau-detail-card" class="mt-2 p-3.5 rounded-xl bg-slate-800/90 border border-slate-700 text-xs">
                <div class="flex items-center justify-between pb-2 border-b border-slate-700">
                    <span class="font-extrabold text-sm text-cyan-300">${currentStop.icon} ${currentStop.city}: ${currentStop.title}</span>
                    <button onclick="speakGerman('${currentStop.de.replace(/'/g, "\\'")}', 1.0)" class="px-2.5 py-1 rounded-lg bg-cyan-600/30 hover:bg-cyan-600/50 text-cyan-200 border border-cyan-500/30 font-bold transition">
                        🔊 Nghe chặng này
                    </button>
                </div>
                <div class="mt-2 text-slate-100 font-semibold text-xs leading-relaxed">
                    „${currentStop.de}“
                </div>
                <div class="mt-1 text-slate-400 text-xs">
                    👉 ${currentStop.vi}
                </div>
            </div>
        </div>`;
    }

    // =========================================================================
    // V6: MÁY TÍNH PARTIZIP II TƯƠNG TÁC TRA CỨU (Mục 6)
    // =========================================================================
    function renderPartizipCalculatorSvg() {
        return `
        <div class="perfekt-visual-card p-4 rounded-2xl bg-slate-900 border border-slate-700/80 shadow-xl text-slate-100 my-4">
            <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-rose-500/20 text-rose-400 border border-rose-500/30">V6</span>
                    <span class="font-extrabold text-sm text-slate-200">Máy tính chẩn đoán Partizip II tương tác</span>
                </div>
                <span class="text-xs text-slate-400">Tra cứu 22 động từ trọng tâm</span>
            </div>

            <div class="mt-3 flex flex-wrap items-center gap-2">
                <label class="text-xs text-slate-300 font-bold">Chọn động từ cần tra cứu:</label>
                <select id="v6-verb-select" onchange="window.calculatePartizipV6()" class="px-3 py-1.5 rounded-xl bg-slate-800 border border-slate-700 text-slate-100 font-bold text-xs focus:ring-2 focus:ring-rose-500">
                    ${PERFEKT_VERBS.map(v => `<option value="${v.verb}">${v.verb} (${v.type})</option>`).join('')}
                </select>
            </div>

            <div id="v6-result-box" class="mt-3 p-3.5 rounded-xl bg-slate-800/90 border border-slate-700 text-xs">
                <!-- Nội dung chẩn đoán do calculatePartizipV6() render -->
            </div>
        </div>`;
    }

    // =========================================================================
    // HÀM ĐIỀU HƯỚNG TƯƠNG TÁC
    // =========================================================================
    global.switchSatzklammerExample = function (delta) {
        const container = document.getElementById('svg-v1-container');
        if (container) {
            container.innerHTML = renderSatzklammerSvg(currentSatzklammerIdx + delta);
        }
    };

    global.selectDonauStop = function (idx) {
        currentDonauStopIdx = idx;
        const container = document.getElementById('svg-v5-container');
        if (container) {
            container.innerHTML = renderDonauRouteMapSvg(idx);
        }
    };

    global.readFullDonauRoute = function () {
        let fullSpeech = DONAU_STOPS.map(s => s.de).join(' ');
        speakGerman(fullSpeech, 0.95);
    };

    global.calculatePartizipV6 = function () {
        const select = document.getElementById('v6-verb-select');
        const box = document.getElementById('v6-result-box');
        if (!select || !box) return;

        const verbName = select.value;
        const item = PERFEKT_VERBS.find(v => v.verb === verbName) || PERFEKT_VERBS[0];

        box.innerHTML = `
            <div class="flex items-center justify-between pb-2 border-b border-slate-700">
                <div class="flex items-center gap-2">
                    <span class="text-rose-400 font-mono font-black text-sm">${item.verb}</span>
                    <span class="text-slate-400 text-xs">→</span>
                    <span class="text-emerald-400 font-mono font-black text-sm">${item.aux} ${item.p2}</span>
                </div>
                <div class="flex items-center gap-1.5">
                    <button onclick="speakGerman('${item.verb}, ${item.aux} ${item.p2}', 1.0)" class="px-2 py-1 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-300 border border-emerald-500/30 font-bold text-[11px] transition">
                        🔊 Phát âm dạng động từ
                    </button>
                    <button onclick="speakGerman('${item.ex.replace(/'/g, "\\'")}', 1.0)" class="px-2.5 py-1 rounded-lg bg-indigo-600/30 hover:bg-indigo-600/50 text-indigo-300 border border-indigo-500/30 font-bold text-[11px] transition">
                        🔊 Nghe câu ví dụ
                    </button>
                </div>
            </div>
            <div class="mt-2 grid grid-cols-1 md:grid-cols-2 gap-2 text-slate-300">
                <div><b>Phân loại:</b> <span class="text-amber-300">${item.type} (Nhóm ${item.group})</span></div>
                <div><b>Trợ động từ:</b> <span class="${item.aux === 'ist' ? 'text-amber-400' : 'text-emerald-400'} font-black">${item.auxFull || item.aux}</span></div>
            </div>
            <div class="mt-2 text-slate-400 text-xs"><b>Quy trình chẩn đoán:</b> ${item.step}</div>
            <div class="mt-2 p-2 rounded-lg bg-slate-900 border border-slate-800 text-slate-200">
                <div>💬 <b>Ví dụ:</b> <span class="text-white font-semibold">„${item.ex}“</span></div>
                <div class="text-slate-400 mt-0.5">👉 ${item.tr}</div>
            </div>
        `;
    };

    // Hàm gắn các sơ đồ vào container khi mở Bài 9
    global.initPerfektSvgDiagrams = function () {
        const c1 = document.getElementById('svg-v1-container');
        if (c1) c1.innerHTML = renderSatzklammerSvg(0);

        const c2 = document.getElementById('svg-v2-container');
        if (c2) c2.innerHTML = renderPartizipFlowchartSvg();

        const c3 = document.getElementById('svg-v3-container');
        if (c3) c3.innerHTML = renderHabenSeinDecisionTreeSvg();

        const c4 = document.getElementById('svg-v4-container');
        if (c4) c4.innerHTML = renderTimelineSvg();

        const c5 = document.getElementById('svg-v5-container');
        if (c5) c5.innerHTML = renderDonauRouteMapSvg(0);

        const c6 = document.getElementById('svg-v6-container');
        if (c6) {
            c6.innerHTML = renderPartizipCalculatorSvg();
            global.calculatePartizipV6();
        }
    };

    // Render sơ đồ khi bài tập có visual
    global.renderExercisePerfektSvg = function (visualCode) {
        if (!visualCode) return '';
        const code = String(visualCode).toUpperCase();
        if (code === 'V1') return renderSatzklammerSvg(0);
        if (code === 'V2') return renderPartizipFlowchartSvg();
        if (code === 'V3') return renderHabenSeinDecisionTreeSvg();
        if (code === 'V4') return renderTimelineSvg();
        if (code === 'V5' || code === 'ROUTE_DONAU') return renderDonauRouteMapSvg(0);
        if (code === 'V6') return renderPartizipCalculatorSvg();
        return '';
    };

    // Export ra global scope
    global.renderSatzklammerSvg = renderSatzklammerSvg;
    global.renderPartizipFlowchartSvg = renderPartizipFlowchartSvg;
    global.renderHabenSeinDecisionTreeSvg = renderHabenSeinDecisionTreeSvg;
    global.renderTimelineSvg = renderTimelineSvg;
    global.renderDonauRouteMapSvg = renderDonauRouteMapSvg;
    global.renderPartizipCalculatorSvg = renderPartizipCalculatorSvg;
    global.PERFEKT_VERBS = PERFEKT_VERBS;

})(typeof window !== 'undefined' ? window : global);
