/**
 * DeutschMeister - Module Đồ Họa Sơ Đồ & Bản Đồ Thành Phố SVG (City Map & Direction SVG Engine)
 * Dành riêng cho Bài 8 (A1): Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu
 * 
 * Cung cấp:
 * 1. Bộ 4 Sơ đồ Không gian Trực quan (an...vorbei, durch, über, entlang)
 * 2. Bộ 12 Thẻ Hình Biểu tượng Chỉ đường (a -> l)
 * 3. Bản đồ Lưới Đường Phố Tương Tác Đa Lộ Trình (Route 1 xanh dương, Route 2 xanh lá)
 * 4. Trình vẽ hình minh họa cho các câu hỏi bài tập (renderExerciseSvg)
 * 5. Bộ sinh đề & bản đồ động (Dynamic Visual Map Generator) khi người dùng đổi đề
 */

(function (global) {
    'use strict';

    // =========================================================================
    // 1. BỘ 12 BIỂU TƯỢNG SƠ ĐỒ CHỈ ĐƯỜNG (CARDS a -> l)
    // =========================================================================
    function getDirectionSvg(code, width = 160, height = 120) {
        const c = String(code || '').toLowerCase().trim();

        // Màu sắc chủ đạo: Đường sá (Slate), Vỉa hè (Slate light), Mũi tên (Indigo/Emerald/Amber)
        const streetFill = "#334155";
        const curbFill = "#cbd5e1";
        const lineStroke = "#f8fafc";
        const arrowColor = "#3b82f6";
        const arrowAccent = "#2563eb";

        switch (c) {
            case 'a':
            case 'geradeaus':
                // a) Đi thẳng ↑
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f1f5f9"/>
                    <!-- Mặt đường -->
                    <rect x="45" y="0" width="70" height="120" fill="${streetFill}"/>
                    <!-- Vỉa hè 2 bên -->
                    <rect x="35" y="0" width="10" height="120" fill="${curbFill}"/>
                    <rect x="115" y="0" width="10" height="120" fill="${curbFill}"/>
                    <!-- Vạch kẻ đường đứt nét -->
                    <line x1="80" y1="5" x2="80" y2="115" stroke="${lineStroke}" stroke-width="3" stroke-dasharray="8 6"/>
                    <!-- Mũi tên đi thẳng màu xanh dương rực rỡ -->
                    <path d="M80 105 L80 30" stroke="${arrowColor}" stroke-width="6" stroke-linecap="round"/>
                    <polygon points="80,15 68,36 92,36" fill="${arrowAccent}"/>
                    <circle cx="80" cy="105" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'b':
            case 'an_der_kirche_vorbei':
                // b) Đi ngang qua nhà thờ ⛪
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Mặt đường chạy dọc bên trái -->
                    <rect x="20" y="0" width="55" height="120" fill="${streetFill}"/>
                    <line x1="47.5" y1="5" x2="47.5" y2="115" stroke="${lineStroke}" stroke-width="2.5" stroke-dasharray="6 5"/>
                    <!-- Vỉa hè -->
                    <rect x="75" y="0" width="8" height="120" fill="${curbFill}"/>
                    <!-- Tòa Nhà Thờ bên phải -->
                    <rect x="88" y="25" width="62" height="70" rx="4" fill="#e2e8f0" stroke="#64748b" stroke-width="1.5"/>
                    <!-- Mái chóp nhà thờ -->
                    <polygon points="119,10 93,25 145,25" fill="#f43f5e"/>
                    <!-- Thánh giá trên mái -->
                    <line x1="119" y1="2" x2="119" y2="10" stroke="#be123c" stroke-width="2"/>
                    <line x1="115" y1="5" x2="123" y2="5" stroke="#be123c" stroke-width="2"/>
                    <!-- Cửa vòm và chuông -->
                    <path d="M112 95 A7 7 0 0 1 126 95 L126 95 L112 95 Z" fill="#475569"/>
                    <circle cx="119" cy="45" r="5" fill="#fbbf24"/>
                    <text x="119" y="70" font-size="9" font-weight="bold" fill="#334155" text-anchor="middle">Kirche</text>
                    <!-- Mũi tên đi lướt ngang qua -->
                    <path d="M47.5 105 L47.5 25" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="47.5,12 39,30 56,30" fill="${arrowAccent}"/>
                    <circle cx="47.5" cy="105" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'c':
            case 'bis_zur_ampel':
                // c) Đi cho đến đèn giao thông 🚦
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <rect x="35" y="0" width="60" height="120" fill="${streetFill}"/>
                    <line x1="65" y1="5" x2="65" y2="115" stroke="${lineStroke}" stroke-width="2.5" stroke-dasharray="6 5"/>
                    <!-- Vạch dừng đỗ màu trắng trước cột đèn -->
                    <rect x="35" y="45" width="60" height="5" fill="#ffffff"/>
                    <!-- Cột đèn giao thông bên lề phải -->
                    <rect x="110" y="45" width="5" height="55" fill="#475569"/>
                    <rect x="102" y="15" width="21" height="42" rx="3" fill="#1e293b" stroke="#0f172a" stroke-width="1.5"/>
                    <!-- 3 mắt đèn Đỏ - Vàng - Xanh -->
                    <circle cx="112.5" cy="23" r="4" fill="#ef4444"/>
                    <circle cx="112.5" cy="35" r="4" fill="#f59e0b"/>
                    <circle cx="112.5" cy="47" r="4" fill="#10b981"/>
                    <text x="112.5" y="72" font-size="8" font-weight="bold" fill="#0f172a" text-anchor="middle">Ampel</text>
                    <!-- Mũi tên đi thẳng và DỪNG LẠI tại vạch dừng -->
                    <path d="M65 105 L65 52" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="65,42 57,56 73,56" fill="${arrowAccent}"/>
                    <!-- Biểu tượng Dừng (STOP bar) -->
                    <rect x="53" y="38" width="24" height="4" rx="2" fill="#ef4444"/>
                    <circle cx="65" cy="105" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'd':
            case 'bis_zur_kreuzung':
                // d) Đi cho đến ngã tư ➕
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Đường ngang cắt ngang -->
                    <rect x="0" y="35" width="160" height="45" fill="${streetFill}"/>
                    <line x1="5" y1="57.5" x2="155" y2="57.5" stroke="${lineStroke}" stroke-width="2" stroke-dasharray="6 5"/>
                    <!-- Đường dọc -->
                    <rect x="55" y="0" width="50" height="120" fill="${streetFill}"/>
                    <line x1="80" y1="5" x2="80" y2="115" stroke="${lineStroke}" stroke-width="2" stroke-dasharray="6 5"/>
                    <!-- Tâm ngã tư -->
                    <rect x="55" y="35" width="50" height="45" fill="${streetFill}"/>
                    <!-- Chữ Kreuzung -->
                    <text x="25" y="25" font-size="9" font-weight="extrabold" fill="#475569">Kreuzung</text>
                    <!-- Mũi tên từ dưới đi tới vạch ngã tư và dừng lại -->
                    <path d="M80 110 L80 84" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="80,75 73,87 87,87" fill="${arrowAccent}"/>
                    <rect x="68" y="72" width="24" height="3" fill="#ef4444"/>
                    <circle cx="80" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'e':
            case 'zweite_strasse_links':
                // e) Rẽ trái ở ngã rẽ thứ 2
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Đường chính thẳng đứng -->
                    <rect x="95" y="0" width="40" height="120" fill="${streetFill}"/>
                    <line x1="115" y1="5" x2="115" y2="115" stroke="${lineStroke}" stroke-width="2" stroke-dasharray="6 5"/>
                    <!-- Ngã rẽ 1 bên trái (ở dưới) -->
                    <rect x="0" y="78" width="95" height="30" fill="${streetFill}"/>
                    <text x="20" y="96" font-size="8" font-weight="bold" fill="#cbd5e1">1. Straße</text>
                    <!-- Dấu gạch chéo đỏ bỏ qua ngã rẽ 1 -->
                    <line x1="90" y1="88" x2="105" y2="98" stroke="#ef4444" stroke-width="2.5"/>
                    <line x1="105" y1="88" x2="90" y2="98" stroke="#ef4444" stroke-width="2.5"/>
                    <!-- Ngã rẽ 2 bên trái (ở trên) -->
                    <rect x="0" y="20" width="95" height="32" fill="${streetFill}"/>
                    <text x="20" y="40" font-size="8" font-weight="bold" fill="#6ee7b7">2. Straße (links)</text>
                    <!-- Mũi tên: Đi thẳng qua ngã 1, rồi quẹo trái vào ngã 2 -->
                    <path d="M115 110 L115 36 L25 36" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                    <polygon points="15,36 30,28 30,44" fill="${arrowAccent}"/>
                    <circle cx="115" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'f':
            case 'ueber_den_platz':
                // f) Đi băng qua quảng trường ⭕
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Quảng trường tròn ở giữa -->
                    <circle cx="80" cy="60" r="46" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
                    <circle cx="80" cy="60" r="40" fill="#fef3c7" stroke="#f59e0b" stroke-dasharray="4 3"/>
                    <!-- Đài phun nước hoặc cây giữa quảng trường -->
                    <circle cx="80" cy="60" r="12" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
                    <circle cx="80" cy="60" r="4" fill="#ffffff"/>
                    <text x="80" y="42" font-size="8.5" font-weight="extrabold" fill="#92400e" text-anchor="middle">Platz</text>
                    <!-- Đường vào và đường ra -->
                    <rect x="68" y="100" width="24" height="20" fill="${streetFill}"/>
                    <rect x="68" y="0" width="24" height="20" fill="${streetFill}"/>
                    <!-- Mũi tên đâm thẳng xuyên qua toàn bộ quảng trường -->
                    <path d="M80 115 L80 10" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="80,2 72,18 88,18" fill="${arrowAccent}"/>
                    <circle cx="80" cy="115" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'g':
            case 'hier_links':
                // g) Rẽ trái ngay tại đây ↰
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Ngã rẽ chữ L hoặc T sang trái -->
                    <path d="M0 35 L85 35 L85 120 L135 120 L135 0 L0 0 Z" fill="#e2e8f0"/>
                    <path d="M0 45 L95 45 L95 120 L55 120 L55 85 L0 85 Z" fill="${streetFill}"/>
                    <text x="35" y="25" font-size="9" font-weight="extrabold" fill="#1e293b">hier links ↰</text>
                    <!-- Mũi tên từ dưới quẹo gập ngay sang trái -->
                    <path d="M75 110 L75 65 L20 65" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                    <polygon points="10,65 24,57 24,73" fill="${arrowAccent}"/>
                    <circle cx="75" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'h':
            case 'hier_rechts':
                // h) Rẽ phải ngay tại đây ↱
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Ngã rẽ chữ L sang phải -->
                    <path d="M160 45 L65 45 L65 120 L105 120 L105 85 L160 85 Z" fill="${streetFill}"/>
                    <text x="125" y="25" font-size="9" font-weight="extrabold" fill="#1e293b" text-anchor="middle">hier rechts ↱</text>
                    <!-- Mũi tên từ dưới quẹo ngay sang phải -->
                    <path d="M85 110 L85 65 L140 65" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                    <polygon points="150,65 136,57 136,73" fill="${arrowAccent}"/>
                    <circle cx="85" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'i':
            case 'strasse_entlang':
                // i) Đi dọc theo con đường 〰️
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Con đường uốn lượn chữ S -->
                    <path d="M40 120 C 50 80, 110 80, 120 40 L 145 40 C 135 90, 75 90, 65 120 Z" fill="${curbFill}"/>
                    <path d="M20 120 C 40 70, 120 70, 100 0 L 140 0 C 160 70, 80 70, 60 120 Z" fill="${streetFill}"/>
                    <path d="M40 120 C 60 70, 140 70, 120 0" fill="none" stroke="${lineStroke}" stroke-width="2" stroke-dasharray="6 4"/>
                    <text x="30" y="25" font-size="9" font-weight="extrabold" fill="#0369a1">die Straße entlang</text>
                    <!-- Mũi tên uốn lượn dọc suốt con đường -->
                    <path d="M40 110 C 60 65, 140 65, 120 15" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="119,7 110,21 126,20" fill="${arrowAccent}"/>
                    <circle cx="40" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'j':
            case 'zweite_strasse_rechts':
                // j) Rẽ phải ở con đường thứ 2
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <rect x="25" y="0" width="40" height="120" fill="${streetFill}"/>
                    <line x1="45" y1="5" x2="45" y2="115" stroke="${lineStroke}" stroke-width="2" stroke-dasharray="6 5"/>
                    <!-- Ngã 1 bên phải -->
                    <rect x="65" y="78" width="95" height="30" fill="${streetFill}"/>
                    <text x="80" y="96" font-size="8" font-weight="bold" fill="#cbd5e1">1. Straße</text>
                    <line x1="60" y1="88" x2="75" y2="98" stroke="#ef4444" stroke-width="2.5"/>
                    <line x1="75" y1="88" x2="60" y2="98" stroke="#ef4444" stroke-width="2.5"/>
                    <!-- Ngã 2 bên phải -->
                    <rect x="65" y="20" width="95" height="32" fill="${streetFill}"/>
                    <text x="75" y="40" font-size="8" font-weight="bold" fill="#6ee7b7">2. Straße (rechts)</text>
                    <!-- Mũi tên -->
                    <path d="M45 110 L45 36 L135 36" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                    <polygon points="145,36 130,28 130,44" fill="${arrowAccent}"/>
                    <circle cx="45" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'k':
            case 'durch_das_tor':
                // k) Đi xuyên qua cổng thành ⛩️
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Đường đi thẳng từ dưới lên -->
                    <rect x="50" y="0" width="60" height="120" fill="${streetFill}"/>
                    <!-- Cổng thành vòm đá (Stadttor / Brandenburger Tor) -->
                    <rect x="15" y="38" width="130" height="42" rx="4" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
                    <!-- Trụ cổng và 3 cổng vòm -->
                    <rect x="25" y="44" width="22" height="36" rx="10" fill="#94a3b8"/>
                    <rect x="113" y="44" width="22" height="36" rx="10" fill="#94a3b8"/>
                    <!-- Cổng vòm chính giữa đục thủng cho đường xuyên qua -->
                    <path d="M55 80 L55 52 A 25 25 0 0 1 105 52 L105 80 Z" fill="${streetFill}" stroke="#334155" stroke-width="1.5"/>
                    <!-- Mái ngói trên cổng -->
                    <polygon points="80,24 10,38 150,38" fill="#e11d48"/>
                    <text x="80" y="34" font-size="8.5" font-weight="extrabold" fill="#ffffff" text-anchor="middle">Stadttor / Tor</text>
                    <!-- Mũi tên đi xuyên qua chính giữa cổng vòm -->
                    <path d="M80 110 L80 12" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="80,3 72,19 88,19" fill="${arrowAccent}"/>
                    <circle cx="80" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'l':
            case 'ueber_die_bruecke':
                // l) Đi vượt qua mặt cầu 🌉
                return `
                <svg viewBox="0 0 160 120" width="${width}" height="${height}" class="rounded-xl shadow-xs border border-slate-200 bg-slate-100">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Dòng sông Spree xanh biếc chảy ngang -->
                    <rect x="0" y="35" width="160" height="50" fill="#38bdf8"/>
                    <path d="M0 45 Q 40 40 80 45 T 160 45" fill="none" stroke="#0284c7" stroke-width="2"/>
                    <path d="M0 72 Q 40 68 80 72 T 160 72" fill="none" stroke="#0284c7" stroke-width="2"/>
                    <text x="25" y="78" font-size="7.5" font-weight="bold" fill="#0369a1">Fluss Spree</text>
                    <!-- Cây cầu đá bắc qua sông -->
                    <rect x="55" y="15" width="50" height="90" rx="3" fill="${streetFill}" stroke="#64748b" stroke-width="1.5"/>
                    <!-- Lan can cầu 2 bên -->
                    <rect x="52" y="15" width="4" height="90" fill="#94a3b8"/>
                    <rect x="104" y="15" width="4" height="90" fill="#94a3b8"/>
                    <!-- Trụ vòm cầu chìm dưới nước -->
                    <ellipse cx="80" cy="60" rx="15" ry="6" fill="#1e293b" opacity="0.3"/>
                    <text x="135" y="25" font-size="8" font-weight="extrabold" fill="#334155" text-anchor="middle">Brücke</text>
                    <!-- Mũi tên đi vượt qua mặt cầu -->
                    <path d="M80 110 L80 12" fill="none" stroke="${arrowColor}" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="80,3 72,19 88,19" fill="${arrowAccent}"/>
                    <circle cx="80" cy="110" r="4" fill="${arrowAccent}"/>
                </svg>`;

            case 'c_and_d':
            case 'direction_card_c_and_d':
                // Kết hợp cả c) và d)
                return `
                <div class="grid grid-cols-2 gap-3 max-w-sm mx-auto">
                    <div class="space-y-1 text-center">
                        ${getDirectionSvg('c', 140, 105)}
                        <span class="text-xs font-bold text-slate-700">c) bis zur Ampel</span>
                    </div>
                    <div class="space-y-1 text-center">
                        ${getDirectionSvg('d', 140, 105)}
                        <span class="text-xs font-bold text-slate-700">d) bis zur Kreuzung</span>
                    </div>
                </div>`;

            default:
                return getDirectionSvg('a', width, height);
        }
    }

    // =========================================================================
    // 2. BỘ 4 SƠ ĐỒ KHÔNG GIAN TRỰC QUAN (SPATIAL PREPOSITION DIAGRAMS)
    // =========================================================================
    function getSpatialDiagramSvg(type, width = 300, height = 180) {
        const t = String(type || '').toLowerCase();
        if (t.includes('vorbei')) {
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <!-- Lề đường & vỉa hè -->
                <rect x="30" y="0" width="100" height="180" fill="#334155"/>
                <line x1="80" y1="5" x2="80" y2="175" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/>
                <rect x="130" y="0" width="15" height="180" fill="#cbd5e1"/>
                <!-- Tòa nhà Universität / Bank bên lề đường -->
                <rect x="155" y="30" width="130" height="120" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
                <rect x="165" y="42" width="24" height="24" fill="#38bdf8" rx="3"/>
                <rect x="198" y="42" width="24" height="24" fill="#38bdf8" rx="3"/>
                <rect x="231" y="42" width="24" height="24" fill="#38bdf8" rx="3"/>
                <rect x="190" y="100" width="35" height="50" fill="#475569" rx="3"/>
                <text x="220" y="85" font-size="11" font-weight="black" fill="#1e293b" text-anchor="middle">UNIVERSITÄT</text>
                <text x="220" y="98" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="middle">(die / Femininum)</text>
                <!-- Dòng ghi chú cấu trúc -->
                <rect x="20" y="12" width="170" height="26" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
                <text x="105" y="29" font-size="11" font-weight="black" fill="#1d4ed8" text-anchor="middle">an + DATIV + vorbei</text>
                <!-- Mũi tên đi lướt ngang qua mà không rẽ vào trong -->
                <path d="M80 165 L80 35" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>
                <polygon points="80,18 70,38 90,38" fill="#1d4ed8"/>
                <circle cx="80" cy="165" r="5" fill="#1d4ed8"/>
                <!-- Bong bóng giải thích -->
                <rect x="15" y="145" width="205" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="117" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 an der Universität vorbei</text>
            </svg>`;
        } else if (t.includes('durch')) {
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <rect x="90" y="0" width="120" height="180" fill="#334155"/>
                <!-- Cổng vòm lớn Brandenburger Tor -->
                <rect x="20" y="45" width="260" height="85" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="2.5"/>
                <!-- Cổng vòm đục thủng xuyên qua -->
                <path d="M105 130 L105 75 A 45 45 0 0 1 195 75 L195 130 Z" fill="#334155" stroke="#1e293b" stroke-width="2"/>
                <!-- Cột trụ và tượng Quadriga trên đỉnh -->
                <rect x="35" y="55" width="30" height="75" fill="#cbd5e1" stroke="#64748b"/>
                <rect x="235" y="55" width="30" height="75" fill="#cbd5e1" stroke="#64748b"/>
                <polygon points="150,22 80,45 220,45" fill="#be123c"/>
                <circle cx="150" cy="15" r="6" fill="#fbbf24"/>
                <text x="150" y="40" font-size="11" font-weight="black" fill="#ffffff" text-anchor="middle">Brandenburger Tor (das)</text>
                <!-- Badge ngữ pháp -->
                <rect x="20" y="12" width="170" height="26" rx="6" fill="#fdf2f8" stroke="#f472b6" stroke-width="1.5"/>
                <text x="105" y="29" font-size="11" font-weight="black" fill="#be185d" text-anchor="middle">durch + AKKUSATIV</text>
                <!-- Mũi tên đâm xuyên qua chính giữa lòng cổng -->
                <path d="M150 168 L150 25" fill="none" stroke="#e11d48" stroke-width="6" stroke-linecap="round"/>
                <polygon points="150,10 140,30 160,30" fill="#be123c"/>
                <circle cx="150" cy="168" r="5" fill="#be123c"/>
                <!-- Chú thích -->
                <rect x="50" y="145" width="200" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="150" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 durch das Tor (xuyên qua lòng cổng)</text>
            </svg>`;
        } else if (t.includes('ueber') || t.includes('über')) {
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <!-- Dòng sông bên dưới -->
                <rect x="0" y="50" width="300" height="75" fill="#38bdf8"/>
                <path d="M0 65 Q 75 55 150 65 T 300 65" fill="none" stroke="#0284c7" stroke-width="3"/>
                <path d="M0 105 Q 75 95 150 105 T 300 105" fill="none" stroke="#0284c7" stroke-width="3"/>
                <!-- Cây cầu bắc qua sông -->
                <rect x="100" y="15" width="100" height="150" rx="6" fill="#334155" stroke="#475569" stroke-width="2"/>
                <rect x="94" y="15" width="6" height="150" fill="#94a3b8"/>
                <rect x="200" y="15" width="6" height="150" fill="#94a3b8"/>
                <!-- Vạch kẻ cầu -->
                <line x1="150" y1="20" x2="150" y2="160" stroke="#ffffff" stroke-width="2" stroke-dasharray="8 6"/>
                <text x="50" y="45" font-size="10" font-weight="extrabold" fill="#0369a1">die Schlossbrücke</text>
                <!-- Badge ngữ pháp -->
                <rect x="20" y="12" width="170" height="26" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
                <text x="105" y="29" font-size="11" font-weight="black" fill="#15803d" text-anchor="middle">über + AKKUSATIV</text>
                <!-- Mũi tên đi vượt qua mặt cầu -->
                <path d="M150 168 L150 25" fill="none" stroke="#16a34a" stroke-width="6" stroke-linecap="round"/>
                <polygon points="150,10 140,30 160,30" fill="#15803d"/>
                <circle cx="150" cy="168" r="5" fill="#15803d"/>
                <!-- Chú thích -->
                <rect x="50" y="145" width="200" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="150" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 über die Brücke (băng qua mặt cầu)</text>
            </svg>`;
        } else {
            // entlang
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <!-- Con đường chạy dọc uốn khúc nhẹ -->
                <path d="M60 180 C 100 110, 200 110, 240 0 L 290 0 C 250 110, 150 110, 110 180 Z" fill="#334155"/>
                <path d="M85 180 C 125 110, 225 110, 265 0" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/>
                <!-- Badge ngữ pháp -->
                <rect x="20" y="12" width="210" height="26" rx="6" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>
                <text x="125" y="29" font-size="11" font-weight="black" fill="#a16207" text-anchor="middle">AKKUSATIV + entlang</text>
                <!-- Mũi tên chạy dọc theo con đường -->
                <path d="M85 168 C 125 105, 225 105, 265 20" fill="none" stroke="#ca8a04" stroke-width="6" stroke-linecap="round"/>
                <polygon points="268,8 253,22 271,28" fill="#a16207"/>
                <circle cx="85" cy="168" r="5" fill="#a16207"/>
                <!-- Chú thích -->
                <rect x="30" y="145" width="240" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="150" y="161" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 die Straße entlang (dọc theo con đường)</text>
            </svg>`;
        }
    }

    // Đối chiếu durch das Tor vs. über die Brücke
    function getSpatialContrastSvg() {
        return `
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-xl mx-auto">
            <div class="p-3 rounded-2xl bg-white border border-slate-200 text-center space-y-2 shadow-xs">
                <span class="text-xs font-black text-rose-700 bg-rose-50 px-2.5 py-1 rounded-full border border-rose-200">durch das Stadttor</span>
                ${getDirectionSvg('k', 220, 140)}
                <p class="text-[11px] text-slate-600 font-semibold">Đi <b>xuyên qua lòng</b> cánh cổng vòm</p>
            </div>
            <div class="p-3 rounded-2xl bg-white border border-slate-200 text-center space-y-2 shadow-xs">
                <span class="text-xs font-black text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full border border-emerald-200">über die Brücke</span>
                ${getDirectionSvg('l', 220, 140)}
                <p class="text-[11px] text-slate-600 font-semibold">Đi <b>vượt qua trên mặt</b> cây cầu</p>
            </div>
        </div>`;
    }

    // =========================================================================
    // 3. BẢN ĐỒ LƯỚI ĐƯỜNG PHỐ TƯƠNG TÁC ĐA LỘ TRÌNH (INTERACTIVE GRID MAP)
    // =========================================================================
    function getCityGridMapSvg(activeRoute = null, quizHighlight = null) {
        // activeRoute: 'route1' (xanh dương), 'route2' (xanh lá), hoặc null (bản đồ tĩnh)
        // quizHighlight: 'quiz1', 'quiz2' (cho các câu hỏi trắc nghiệm nhìn bản đồ)
        const isRoute1 = activeRoute === 'route1' || quizHighlight === 'quiz1';
        const isRoute2 = activeRoute === 'route2' || quizHighlight === 'quiz2';

        return `
        <svg viewBox="0 0 540 360" width="100%" class="w-full max-w-2xl mx-auto rounded-3xl shadow-md border-2 border-slate-300 bg-slate-900 overflow-hidden">
            <!-- Nền bản đồ phong cách tối sang trọng -->
            <rect x="0" y="0" width="540" height="360" fill="#0f172a"/>

            <!-- Khối công viên cây xanh góc dưới bên phải -->
            <rect x="360" y="220" width="150" height="110" rx="12" fill="#064e3b" stroke="#047857" stroke-width="1.5"/>
            <text x="435" y="280" font-size="11" font-weight="bold" fill="#34d399" text-anchor="middle">🌳 Stadtpark</text>

            <!-- Hệ thống đường phố Lưới 3x3 -->
            <!-- Đường dọc 1 (chính trái) -->
            <rect x="60" y="0" width="48" height="360" fill="#1e293b"/>
            <line x1="84" y1="0" x2="84" y2="360" stroke="#475569" stroke-width="2" stroke-dasharray="8 6"/>

            <!-- Đường dọc 2 (giữa) -->
            <rect x="220" y="0" width="48" height="360" fill="#1e293b"/>
            <line x1="244" y1="0" x2="244" y2="360" stroke="#475569" stroke-width="2" stroke-dasharray="8 6"/>

            <!-- Đường dọc 3 (phải) -->
            <rect x="380" y="0" width="48" height="360" fill="#1e293b"/>
            <line x1="404" y1="0" x2="404" y2="360" stroke="#475569" stroke-width="2" stroke-dasharray="8 6"/>

            <!-- Đường ngang 1 (dưới) -->
            <rect x="0" y="270" width="540" height="44" fill="#1e293b"/>
            <line x1="0" y1="292" x2="540" y2="292" stroke="#475569" stroke-width="2" stroke-dasharray="8 6"/>

            <!-- Đường ngang 2 (giữa) -->
            <rect x="0" y="150" width="540" height="44" fill="#1e293b"/>
            <line x1="0" y1="172" x2="540" y2="172" stroke="#475569" stroke-width="2" stroke-dasharray="8 6"/>

            <!-- Đường ngang 3 (trên) -->
            <rect x="0" y="40" width="540" height="44" fill="#1e293b"/>
            <line x1="0" y1="62" x2="540" y2="62" stroke="#475569" stroke-width="2" stroke-dasharray="8 6"/>

            <!-- Tên các con đường -->
            <text x="84" y="352" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Friedrichstraße</text>
            <text x="244" y="352" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Wilhelmstraße</text>
            <text x="404" y="18" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Alexanderstraße</text>
            <text x="18" y="286" font-size="8.5" font-weight="bold" fill="#94a3b8">Leipziger Str.</text>
            <text x="18" y="166" font-size="8.5" font-weight="bold" fill="#94a3b8">Behrenstraße</text>
            <text x="18" y="56" font-size="8.5" font-weight="bold" fill="#94a3b8">Unter den Linden</text>

            <!-- TÒA NHÀ & ĐỊA ĐIỂM -->
            <!-- 1. Vị trí Start (Sie sind hier) ở góc dưới đường dọc 1 -->
            <circle cx="84" cy="330" r="14" fill="#f43f5e" stroke="#ffffff" stroke-width="2.5"/>
            <circle cx="84" cy="330" r="5" fill="#ffffff"/>
            <text x="84" y="310" font-size="10" font-weight="black" fill="#f43f5e" text-anchor="middle">📍 START</text>
            <text x="84" y="298" font-size="8" font-weight="bold" fill="#fda4af" text-anchor="middle">(Sie sind hier)</text>

            <!-- 2. Ngân hàng Bank (trên đường Behrenstraße giữa ngã 1 và 2) -->
            <rect x="125" y="105" width="75" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="162.5" y="125" font-size="14" text-anchor="middle">🏦</text>
            <text x="162.5" y="138" font-size="9" font-weight="extrabold" fill="#bfdbfe" text-anchor="middle">die Bank</text>

            <!-- 3. Nhà thờ Kirche (bên trái đường dọc 1) -->
            <rect x="5" y="85" width="48" height="55" rx="6" fill="#3f3f46" stroke="#71717a" stroke-width="1.5"/>
            <text x="29" y="112" font-size="14" text-anchor="middle">⛪</text>
            <text x="29" y="126" font-size="8" font-weight="bold" fill="#e4e4e7" text-anchor="middle">Kirche</text>

            <!-- 4. Rạp chiếu phim Kino (bên trái đường dọc 2 góc trên) -->
            <rect x="135" y="5" width="75" height="32" rx="5" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
            <text x="172.5" y="24" font-size="12" text-anchor="middle">🎬 das Kino</text>

            <!-- 5. ĐÍCH ĐẾN: Bưu điện Post & Đèn giao thông Ampel (Góc trên bên phải) -->
            <rect x="440" y="5" width="90" height="45" rx="8" fill="#854d0e" stroke="#eab308" stroke-width="2"/>
            <text x="485" y="26" font-size="14" text-anchor="middle">📮</text>
            <text x="485" y="40" font-size="10" font-weight="black" fill="#fef08a" text-anchor="middle">DIE POST</text>
            <!-- Đèn giao thông Ampel ngay trước Bưu điện -->
            <rect x="408" y="22" width="12" height="24" rx="2" fill="#000000" stroke="#eab308" stroke-width="1"/>
            <circle cx="414" cy="27" r="2" fill="#ef4444"/>
            <circle cx="414" cy="34" r="2" fill="#f59e0b"/>
            <circle cx="414" cy="41" r="2" fill="#10b981"/>
            <text x="414" y="15" font-size="7.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Ampel 🚦</text>

            <!-- 6. Ga tàu Bahnhof ở góc phải dưới -->
            <rect x="440" y="110" width="90" height="40" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="485" y="130" font-size="12" text-anchor="middle">🚉 Bahnhof</text>

            <!-- ================= LỘ TRÌNH 1 (XANH DƯƠNG) ================= -->
            ${isRoute1 ? `
            <g id="route-1-layer">
                <!-- Đường đi: Start(84,330) -> thẳng lên ngã 1(84,172) -> rẽ phải qua Bank tới ngã 2(244,172) -> rẽ trái lên ngã 3(244,62) -> rẽ phải tới Ampel(404,62) -> Đến Post bên phải -->
                <path d="M 84 330 L 84 172 L 244 172 L 244 62 L 404 62" fill="none" stroke="#3b82f6" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M 84 330 L 84 172 L 244 172 L 244 62 L 404 62" fill="none" stroke="#93c5fd" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 8"/>
                <!-- Mũi tên chỉ hướng chặng 1 -->
                <polygon points="84,240 78,252 90,252" fill="#2563eb"/>
                <!-- Mũi tên rẽ phải qua Bank -->
                <polygon points="175,172 163,166 163,178" fill="#2563eb"/>
                <!-- Mũi tên rẽ trái lên ngã tư 2 -->
                <polygon points="244,110 238,122 250,122" fill="#2563eb"/>
                <!-- Mũi tên tới Ampel -->
                <polygon points="340,62 328,56 328,68" fill="#2563eb"/>
                <!-- Đích đến Post -->
                <circle cx="440" cy="40" r="12" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
                <text x="440" y="44" font-size="9" font-weight="black" fill="#ffffff" text-anchor="middle">ZIEL</text>
            </g>
            ` : ''}

            <!-- ================= LỘ TRÌNH 2 (XANH LÁ) ================= -->
            ${isRoute2 ? `
            <g id="route-2-layer">
                <!-- Lộ trình 2: Start(84,330) -> Đi thẳng qua ngã 1 -> lên ngã 2 bên phải(84,62) -> rẽ phải đi thẳng băng qua ngã tư -> tới Ampel/Post(404,62) -->
                <path d="M 84 330 L 84 62 L 404 62" fill="none" stroke="#10b981" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M 84 330 L 84 62 L 404 62" fill="none" stroke="#a7f3d0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 8"/>
                <!-- Mũi tên thẳng lên -->
                <polygon points="84,210 78,222 90,222" fill="#059669"/>
                <polygon points="84,110 78,122 90,122" fill="#059669"/>
                <!-- Mũi tên rẽ phải ngã tư 2 đi thẳng băng qua -->
                <polygon points="180,62 168,56 168,68" fill="#059669"/>
                <polygon points="310,62 298,56 298,68" fill="#059669"/>
                <!-- Đích đến -->
                <circle cx="440" cy="40" r="12" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
                <text x="440" y="44" font-size="9" font-weight="black" fill="#ffffff" text-anchor="middle">ZIEL</text>
            </g>
            ` : ''}
        </svg>`;
    }

    // =========================================================================
    // 4. TRÌNH VẼ SƠ ĐỒ / BẢN ĐỒ VÀO CÂU HỎI BÀI TẬP (renderExerciseSvg)
    // =========================================================================
    function renderExerciseSvg(extra) {
        if (!extra) return '';
        const svgKey = extra.visual_svg || extra.map_scenario || '';
        if (!svgKey) return '';

        let innerContent = '';
        let badgeLabel = 'SƠ ĐỒ CHỈ ĐƯỜNG';
        let badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';

        if (svgKey.startsWith('direction_card_')) {
            const cardCode = svgKey.replace('direction_card_', '');
            innerContent = `<div class="flex justify-center my-3">${getDirectionSvg(cardCode, 200, 140)}</div>`;
            badgeLabel = `HÌNH CHỈ ĐƯỜNG: ${cardCode.toUpperCase()}`;
        } else if (svgKey === 'spatial_diagram_vorbei') {
            innerContent = `<div class="my-3">${getSpatialDiagramSvg('vorbei', 340, 180)}</div>`;
            badgeLabel = 'SƠ ĐỒ: an + Dativ + vorbei';
            badgeColor = 'bg-indigo-100 text-indigo-800 border-indigo-300';
        } else if (svgKey === 'spatial_contrast_tor_bruecke') {
            innerContent = `<div class="my-3">${getSpatialContrastSvg()}</div>`;
            badgeLabel = 'ĐỐI CHIẾU: durch das Tor vs. über die Brücke';
            badgeColor = 'bg-purple-100 text-purple-800 border-purple-300';
        } else if (svgKey === 'city_grid_map_quiz_1') {
            innerContent = `
            <div class="my-3 space-y-2">
                <div class="p-2 rounded-xl bg-blue-50 border border-blue-200 text-blue-900 text-xs font-semibold flex items-center justify-between">
                    <span>🔵 Đang hiển thị Lộ trình 1 (màu xanh dương) trên bản đồ thành phố</span>
                    <button type="button" onclick="speakGerman('Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel.', 1.0)" class="px-2.5 py-1 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs cursor-pointer">
                        🔊 Nghe lộ trình
                    </button>
                </div>
                ${getCityGridMapSvg('route1', 'quiz1')}
            </div>`;
            badgeLabel = 'BẢN ĐỒ LƯỚI ĐƯỜNG PHỐ — LỘ TRÌNH 1';
            badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';
        } else if (svgKey === 'city_grid_map_quiz_2') {
            innerContent = `
            <div class="my-3 space-y-2">
                <div class="p-2 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs font-semibold flex items-center justify-between">
                    <span>🟢 Đang hiển thị Lộ trình 2 (màu xanh lá) trên bản đồ thành phố</span>
                    <button type="button" onclick="speakGerman('Zuerst gehen Sie geradeaus, bis zur zweiten Kreuzung rechts. Dann gehen Sie geradeaus, über die Kreuzung. Links sehen Sie die Post.', 1.0)" class="px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs cursor-pointer">
                        🔊 Nghe lộ trình
                    </button>
                </div>
                ${getCityGridMapSvg('route2', 'quiz2')}
            </div>`;
            badgeLabel = 'BẢN ĐỒ LƯỚI ĐƯỜNG PHỐ — LỘ TRÌNH 2';
            badgeColor = 'bg-emerald-100 text-emerald-800 border-emerald-300';
        } else {
            return '';
        }

        return `
        <div class="my-3 p-4 rounded-2xl bg-white border border-slate-200 shadow-xs">
            <div class="flex items-center justify-between mb-2">
                <span class="px-2.5 py-0.5 rounded-full text-xs font-extrabold border ${badgeColor}">
                    ${badgeLabel}
                </span>
                <span class="text-[11px] text-slate-500 font-medium">Quan sát hình minh họa & định hướng</span>
            </div>
            ${innerContent}
        </div>`;
    }

    // =========================================================================
    // 5. TRÌNH TƯƠNG TÁC LÝ THUYẾT: BẬT TẮT LỘ TRÌNH BẢN ĐỒ BÀI 8
    // =========================================================================
    function setInteractiveMapRoute(route) {
        const container = document.getElementById('b8-interactive-city-map-container');
        if (!container) return;

        container.innerHTML = getCityGridMapSvg(route);

        // Cập nhật trạng thái nút bấm
        const btn1 = document.getElementById('b8-btn-route-1');
        const btn2 = document.getElementById('b8-btn-route-2');
        const btnReset = document.getElementById('b8-btn-route-reset');

        if (btn1) btn1.className = route === 'route1'
            ? 'px-4 py-2 rounded-xl bg-blue-600 text-white font-bold text-xs shadow-sm ring-2 ring-blue-400 cursor-pointer'
            : 'px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs cursor-pointer';

        if (btn2) btn2.className = route === 'route2'
            ? 'px-4 py-2 rounded-xl bg-emerald-600 text-white font-bold text-xs shadow-sm ring-2 ring-emerald-400 cursor-pointer'
            : 'px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs cursor-pointer';

        if (btnReset) btnReset.className = !route
            ? 'px-4 py-2 rounded-xl bg-slate-800 text-white font-bold text-xs shadow-sm cursor-pointer'
            : 'px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs cursor-pointer';

        // Cập nhật khung mô tả lộ trình
        const descWrap = document.getElementById('b8-route-description-wrap');
        if (descWrap) {
            if (route === 'route1') {
                descWrap.innerHTML = `
                    <div class="p-4 rounded-2xl bg-blue-50 border border-blue-200 space-y-2 text-xs sm:text-sm text-blue-950">
                        <div class="flex items-center justify-between">
                            <span class="font-extrabold text-blue-800">🔵 Lộ trình 1: Đi qua Ngân hàng tới Bưu điện</span>
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel. Rechts sehen Sie die Post.', 1.0)" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus. <b>Dann</b> gehen Sie die erste Straße rechts, <b>an der Bank vorbei</b>. <b>Dann</b> gehen Sie bis zur zweiten Kreuzung links. <b>Danach</b> gehen Sie <b>bis zur Ampel</b>. Rechts sehen Sie <b>die Post</b>.“</p>
                        <p class="text-xs text-blue-800 font-medium"><b>Dịch nghĩa:</b> Đầu tiên Ngài đi thẳng. Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. Sau đó Ngài đi đến ngã tư thứ hai thì rẽ trái. Tiếp theo Ngài đi cho đến đèn giao thông. Ở bên phải Ngài sẽ nhìn thấy bưu điện.</p>
                    </div>`;
            } else if (route === 'route2') {
                descWrap.innerHTML = `
                    <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 space-y-2 text-xs sm:text-sm text-emerald-950">
                        <div class="flex items-center justify-between">
                            <span class="font-extrabold text-emerald-800">🟢 Lộ trình 2: Đi thẳng lên ngã tư thứ 2 rồi rẽ phải</span>
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus, bis zur zweiten Kreuzung rechts. Dann gehen Sie geradeaus, über die Kreuzung. Links sehen Sie die Post.', 1.0)" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus, <b>bis zur zweiten Kreuzung rechts</b>. <b>Dann</b> gehen Sie geradeaus, <b>über die Kreuzung</b>. Links sehen Sie <b>die Post</b>.“</p>
                        <p class="text-xs text-emerald-800 font-medium"><b>Dịch nghĩa:</b> Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện.</p>
                    </div>`;
            } else {
                descWrap.innerHTML = `
                    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 text-xs text-slate-600 text-center">
                        Bấm vào một trong hai lộ trình bên trên để xem đường vẽ và nghe câu chỉ đường mẫu!
                    </div>`;
            }
        }
    }

    // =========================================================================
    // 6. BỘ SINH ĐỀ & BẢN ĐỒ ĐỘNG KHI NGƯỜI DÙNG BẤM "🔄 ĐỔI ĐỀ KHÁC" (Lesson 8)
    // =========================================================================
    function generateNewCityMapData(ex, fallbackIndex = null) {
        if (!ex) return ex;
        let extra = {};
        try {
            extra = typeof ex.extra_data === 'string' ? JSON.parse(ex.extra_data) : (ex.extra_data || {});
        } catch (e) {
            return ex;
        }

        // 1. Random Thẻ Biểu tượng Chỉ đường (a -> l)
        if (extra.dynamic_direction_card) {
            const pool = [
                { code: 'a', cmd: 'Gehen Sie geradeaus.', vi: 'Ngài hãy đi thẳng.' },
                { code: 'b', cmd: 'Gehen Sie an der Kirche vorbei.', vi: 'Ngài hãy đi ngang qua nhà thờ.' },
                { code: 'c', cmd: 'Gehen Sie bis zur Ampel.', vi: 'Ngài hãy đi cho đến đèn giao thông.' },
                { code: 'd', cmd: 'Gehen Sie bis zur Kreuzung.', vi: 'Ngài hãy đi cho đến ngã tư.' },
                { code: 'e', cmd: 'Gehen Sie die zweite Straße links.', vi: 'Ngài hãy rẽ trái ở con đường thứ hai.' },
                { code: 'f', cmd: 'Gehen Sie über den Platz.', vi: 'Ngài hãy đi băng qua quảng trường.' },
                { code: 'g', cmd: 'Gehen Sie hier links.', vi: 'Ngài hãy rẽ trái ở đây.' },
                { code: 'h', cmd: 'Gehen Sie hier rechts.', vi: 'Ngài hãy rẽ phải ở đây.' },
                { code: 'i', cmd: 'Gehen Sie die Straße entlang.', vi: 'Ngài hãy đi dọc theo con đường.' },
                { code: 'j', cmd: 'Gehen Sie die zweite Straße rechts.', vi: 'Ngài hãy rẽ phải ở con đường thứ hai.' },
                { code: 'k', cmd: 'Gehen Sie durch das Tor.', vi: 'Ngài hãy đi xuyên qua cánh cổng.' },
                { code: 'l', cmd: 'Gehen Sie über die Brücke.', vi: 'Ngài hãy đi qua cây cầu.' }
            ];
            const pick = pool[Math.floor(Math.random() * pool.length)];
            extra.visual_svg = 'direction_card_' + pick.code;
            ex.question = `Câu ${fallbackIndex || 1} [Sơ đồ Chỉ đường Random]: Quan sát sơ đồ chỉ đường hình minh họa và chọn câu lệnh tiếng Đức khớp chính xác:`;
            ex.correct_answer = pick.cmd;
            ex.explanation = `Hình ${pick.code.toUpperCase()}: ${pick.vi} -> „${pick.cmd}“`;
            extra.translation = pick.vi;

            // Xáo trộn options trắc nghiệm
            const wrongOptions = pool.filter(p => p.code !== pick.code).map(p => p.cmd);
            wrongOptions.sort(() => Math.random() - 0.5);
            ex.options = [pick.cmd, wrongOptions[0], wrongOptions[1], wrongOptions[2]].sort(() => Math.random() - 0.5);
            ex.extra_data = extra;
            return ex;
        }

        // 2. Random Động từ khuyết thiếu wollen theo 9 ngôi
        if (extra.dynamic_modal_wollen) {
            const wollenPool = [
                { subj: 'ich', verb: 'will', cityAct: 'eine Stadtrundfahrt machen', vi: 'Tôi muốn làm một chuyến tham quan thành phố.' },
                { subj: 'du', verb: 'willst', cityAct: 'auf der Friedrichstraße bummeln', vi: 'Bạn muốn đi dạo phố trên đường Friedrich.' },
                { subj: 'mein Bruder', verb: 'will', cityAct: 'an der Humboldt-Universität studieren', vi: 'Anh trai tôi muốn học đại học tại Đại học Humboldt.' },
                { subj: 'wir', verb: 'wollen', cityAct: 'einen Film im Kino sehen', vi: 'Chúng tôi muốn xem một bộ phim trong rạp.' },
                { subj: 'ihr', verb: 'wollt', cityAct: 'zum Brandenburger Tor gehen', vi: 'Các bạn muốn đi đến Cổng Brandenburg.' },
                { subj: 'Paula und Alex', verb: 'wollen', cityAct: 'in den Berliner Dom gehen', vi: 'Paula và Alex muốn đi vào Nhà thờ lớn Berlin.' },
                { subj: 'Herr Müller', verb: 'will', cityAct: 'das Schloss Bellevue besichtigen', vi: 'Ông Müller muốn tham quan Cung điện Bellevue.' }
            ];
            const pick = wollenPool[Math.floor(Math.random() * wollenPool.length)];
            ex.question = `Câu ${fallbackIndex || 27} [Chia Modalverb wollen]: Điền dạng chia đúng của 'wollen' vào chỗ trống: '${pick.subj} ___ heute ${pick.cityAct}.' (Gợi ý: '${pick.vi}')`;
            ex.correct_answer = pick.verb;
            ex.explanation = `Chủ ngữ '${pick.subj}' chia với động từ khuyết thiếu 'wollen' là '${pick.verb}'.`;
            extra.accepted_answers = [pick.verb];
            extra.translation = pick.vi;
            ex.extra_data = extra;
            return ex;
        }

        // 3. Random Địa danh Berlin (zum/zur vs in den/in die/ins)
        if (extra.dynamic_berlin_route) {
            const landmarkPool = [
                { place: 'das Brandenburger Tor', prep: 'zum', full: 'zum Brandenburger Tor', vi: 'đến Cổng Brandenburg' },
                { place: 'der Reichstag', prep: 'zum', full: 'zum Reichstag', vi: 'đến Tòa nhà Quốc hội' },
                { place: 'die Museumsinsel', prep: 'zur', full: 'zur Museumsinsel', vi: 'đến Đảo Bảo tàng' },
                { place: 'die Staatsoper', prep: 'zur', full: 'zur Staatsoper', vi: 'đến Nhà hát Opera' },
                { place: 'der Berliner Dom', prep: 'in den', full: 'in den Berliner Dom', vi: 'vào trong Nhà thờ lớn Berlin' },
                { place: 'die Nationalgalerie', prep: 'in die', full: 'in die Nationalgalerie', vi: 'vào Khu triển lãm Quốc gia' },
                { place: 'das Bundeskanzleramt', prep: 'ins', full: 'ins Bundeskanzleramt', vi: 'vào Phủ Thủ tướng' },
                { place: 'das Sony Center', prep: 'ins', full: 'ins Sony Center', vi: 'vào Trung tâm Sony' }
            ];
            const pick = landmarkPool[Math.floor(Math.random() * landmarkPool.length)];
            ex.question = `Câu ${fallbackIndex || 30} [Địa danh Berlin & Giới từ]: Điền giới từ + mạo từ thích hợp vào chỗ trống: 'Paula und Alex gehen ___ ${pick.place.split(' ').slice(1).join(' ')}.'`;
            ex.correct_answer = pick.prep;
            ex.explanation = `Với '${pick.place}', đi tới/vào dùng '${pick.prep}' -> '${pick.full}' (${pick.vi}).`;
            extra.accepted_answers = [pick.prep];
            extra.translation = `Paula và Alex đi ${pick.vi}.`;
            ex.extra_data = extra;
            return ex;
        }

        return ex;
    }

    // =========================================================================
    // 7. LƯỚI 12 THẺ HÌNH MINH HỌA CHỈ ĐƯỜNG (a -> l) TRONG PHẦN LÝ THUYẾT
    // =========================================================================
    function renderAllDirectionCardsGrid() {
        const cards = [
            { code: 'a', title: 'Hình a', de: 'Gehen Sie geradeaus.', vi: 'Ngài hãy đi thẳng.' },
            { code: 'b', title: 'Hình b', de: 'Gehen Sie an der Kirche vorbei.', vi: 'Ngài hãy đi ngang qua nhà thờ.' },
            { code: 'c', title: 'Hình c', de: 'Gehen Sie bis zur Ampel.', vi: 'Ngài hãy đi cho đến đèn giao thông.' },
            { code: 'd', title: 'Hình d', de: 'Gehen Sie bis zur Kreuzung.', vi: 'Ngài hãy đi cho đến ngã tư.' },
            { code: 'e', title: 'Hình e', de: 'Gehen Sie die zweite Straße links.', vi: 'Ngài hãy rẽ trái ở con đường thứ hai.' },
            { code: 'f', title: 'Hình f', de: 'Gehen Sie über den Platz.', vi: 'Ngài hãy đi băng qua quảng trường.' },
            { code: 'g', title: 'Hình g', de: 'Gehen Sie hier links.', vi: 'Ngài hãy rẽ trái ở đây.' },
            { code: 'h', title: 'Hình h', de: 'Gehen Sie hier rechts.', vi: 'Ngài hãy rẽ phải ở đây.' },
            { code: 'i', title: 'Hình i', de: 'Gehen Sie die Straße entlang.', vi: 'Ngài hãy đi dọc theo con đường.' },
            { code: 'j', title: 'Hình j (Mở rộng)', de: 'Gehen Sie die zweite Straße rechts.', vi: 'Ngài hãy rẽ phải ở con đường thứ hai.' },
            { code: 'k', title: 'Hình k (Mở rộng)', de: 'Gehen Sie durch das Tor.', vi: 'Ngài hãy đi xuyên qua cánh cổng.' },
            { code: 'l', title: 'Hình l (Mở rộng)', de: 'Gehen Sie über die Brücke.', vi: 'Ngài hãy đi qua cây cầu.' }
        ];

        return `
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
            ${cards.map(c => `
                <div class="p-3.5 rounded-2xl bg-white border border-slate-200 shadow-2xs hover:shadow-sm transition space-y-2 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center justify-between mb-2">
                            <span class="px-2 py-0.5 rounded-md bg-slate-100 text-slate-700 font-black text-xs">${c.title}</span>
                            <button onclick="speakGerman('${c.de}', 1.0)" class="w-7 h-7 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs font-bold transition cursor-pointer" title="Nghe phát âm">
                                🔊
                            </button>
                        </div>
                        <div class="flex justify-center my-1.5">
                            ${getDirectionSvg(c.code, 150, 105)}
                        </div>
                    </div>
                    <div class="space-y-0.5 pt-1 border-t border-slate-100">
                        <div class="font-extrabold text-xs text-indigo-950">${c.de}</div>
                        <div class="text-[11px] text-slate-500 font-medium">${c.vi}</div>
                    </div>
                </div>
            `).join('')}
        </div>`;
    }

    // =========================================================================
    // 8. TỰ ĐỘNG KHỞI TẠO CÁC CONTAINER SVG CHO BÀI 8 KHI MỞ BÀI HỌC
    // =========================================================================
    function initLesson8Visuals() {
        const vorbeiEl = document.getElementById('svg-diag-vorbei');
        if (vorbeiEl && !vorbeiEl.hasChildNodes()) {
            vorbeiEl.innerHTML = getSpatialDiagramSvg('vorbei', '100%', 150);
        }
        const durchEl = document.getElementById('svg-diag-durch');
        if (durchEl && !durchEl.hasChildNodes()) {
            durchEl.innerHTML = getSpatialDiagramSvg('durch', '100%', 150);
        }
        const ueberEl = document.getElementById('svg-diag-ueber');
        if (ueberEl && !ueberEl.hasChildNodes()) {
            ueberEl.innerHTML = getSpatialDiagramSvg('ueber', '100%', 150);
        }
        const entlangEl = document.getElementById('svg-diag-entlang');
        if (entlangEl && !entlangEl.hasChildNodes()) {
            entlangEl.innerHTML = getSpatialDiagramSvg('entlang', '100%', 150);
        }
        const mapEl = document.getElementById('b8-interactive-city-map-container');
        if (mapEl && !mapEl.hasChildNodes()) {
            mapEl.innerHTML = getCityGridMapSvg('route1');
        }
        const contrastEl = document.getElementById('svg-spatial-contrast');
        if (contrastEl && !contrastEl.hasChildNodes()) {
            contrastEl.innerHTML = getSpatialContrastSvg();
        }
        const cardsGridEl = document.getElementById('b8-direction-cards-grid');
        if (cardsGridEl && !cardsGridEl.hasChildNodes()) {
            cardsGridEl.innerHTML = renderAllDirectionCardsGrid();
        }
    }

    // Export ra Window Object
    if (typeof window !== 'undefined') {
        window.getDirectionSvg = getDirectionSvg;
        window.getSpatialDiagramSvg = getSpatialDiagramSvg;
        window.getSpatialContrastSvg = getSpatialContrastSvg;
        window.getCityGridMapSvg = getCityGridMapSvg;
        window.renderExerciseSvg = renderExerciseSvg;
        window.setInteractiveMapRoute = setInteractiveMapRoute;
        window.generateNewCityMapData = generateNewCityMapData;
        window.renderAllDirectionCardsGrid = renderAllDirectionCardsGrid;
        window.initLesson8Visuals = initLesson8Visuals;
    }

    if (typeof module !== 'undefined' && module.exports) {
        module.exports = {
            getDirectionSvg,
            getSpatialDiagramSvg,
            getSpatialContrastSvg,
            getCityGridMapSvg,
            renderExerciseSvg,
            setInteractiveMapRoute,
            generateNewCityMapData,
            renderAllDirectionCardsGrid,
            initLesson8Visuals
        };
    }
})(typeof window !== 'undefined' ? window : global);
