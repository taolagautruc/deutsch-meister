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
                <!-- Lề đường & vỉa hè bên trái -->
                <rect x="25" y="0" width="90" height="180" fill="#334155"/>
                <line x1="70" y1="5" x2="70" y2="175" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/>
                <rect x="115" y="0" width="12" height="180" fill="#cbd5e1"/>
                <!-- Badge ngữ pháp góc trên bên phải (hoàn toàn tách biệt khỏi đường đi) -->
                <rect x="135" y="8" width="155" height="25" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
                <text x="212.5" y="25" font-size="10.5" font-weight="black" fill="#1d4ed8" text-anchor="middle">an + DATIV + vorbei</text>
                <!-- Tòa nhà Universität bên lề đường -->
                <rect x="135" y="37" width="155" height="102" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
                <rect x="145" y="46" width="22" height="22" fill="#38bdf8" rx="3"/>
                <rect x="175" y="46" width="22" height="22" fill="#38bdf8" rx="3"/>
                <rect x="205" y="46" width="22" height="22" fill="#38bdf8" rx="3"/>
                <rect x="235" y="46" width="22" height="22" fill="#38bdf8" rx="3"/>
                <text x="212.5" y="85" font-size="11" font-weight="black" fill="#1e293b" text-anchor="middle">UNIVERSITÄT</text>
                <text x="212.5" y="98" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="middle">(die / Femininum)</text>
                <rect x="195" y="103" width="35" height="36" fill="#475569" rx="3"/>
                <!-- Mũi tên đi lướt ngang qua trên đường chạy dọc mà không rẽ vào trong -->
                <path d="M70 165 L70 35" fill="none" stroke="#2563eb" stroke-width="6" stroke-linecap="round"/>
                <polygon points="70,18 60,38 80,38" fill="#1d4ed8"/>
                <circle cx="70" cy="165" r="5" fill="#1d4ed8"/>
                <!-- Bong bóng giải thích phía dưới -->
                <rect x="15" y="147" width="220" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="125" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 an der Universität vorbei</text>
            </svg>`;
        } else if (t.includes('durch')) {
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <rect x="95" y="0" width="110" height="180" fill="#334155"/>
                <!-- Cổng vòm lớn Brandenburger Tor -->
                <rect x="20" y="48" width="260" height="85" rx="6" fill="#e2e8f0" stroke="#475569" stroke-width="2.5"/>
                <!-- Cổng vòm đục thủng xuyên qua -->
                <path d="M105 133 L105 78 A 45 45 0 0 1 195 78 L195 133 Z" fill="#334155" stroke="#1e293b" stroke-width="2"/>
                <!-- Cột trụ và tượng Quadriga trên đỉnh -->
                <rect x="35" y="58" width="28" height="75" fill="#cbd5e1" stroke="#64748b"/>
                <rect x="237" y="58" width="28" height="75" fill="#cbd5e1" stroke="#64748b"/>
                <polygon points="150,26 80,48 220,48" fill="#be123c"/>
                <circle cx="150" cy="18" r="5" fill="#fbbf24"/>
                <!-- Badge ngữ pháp góc trên bên trái -->
                <rect x="10" y="8" width="126" height="26" rx="6" fill="#fdf2f8" stroke="#f472b6" stroke-width="1.5"/>
                <text x="73" y="25" font-size="10.5" font-weight="black" fill="#be185d" text-anchor="middle">durch + AKKUSATIV</text>
                <!-- Nhãn tên địa danh góc trên bên phải -->
                <rect x="164" y="8" width="126" height="26" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="227" y="25" font-size="9.5" font-weight="black" fill="#1e293b" text-anchor="middle">Brandenburger Tor (das)</text>
                <!-- Mũi tên đâm xuyên qua chính giữa lòng cổng -->
                <path d="M150 168 L150 25" fill="none" stroke="#e11d48" stroke-width="6" stroke-linecap="round"/>
                <polygon points="150,10 140,28 160,28" fill="#be123c"/>
                <circle cx="150" cy="168" r="5" fill="#be123c"/>
                <!-- Chú thích phía dưới -->
                <rect x="45" y="147" width="210" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="150" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 durch das Tor (xuyên qua lòng cổng)</text>
            </svg>`;
        } else if (t.includes('ueber') || t.includes('über')) {
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <!-- Dòng sông bên dưới -->
                <rect x="0" y="52" width="300" height="74" fill="#38bdf8"/>
                <path d="M0 68 Q 75 58 150 68 T 300 68" fill="none" stroke="#0284c7" stroke-width="3"/>
                <path d="M0 108 Q 75 98 150 108 T 300 108" fill="none" stroke="#0284c7" stroke-width="3"/>
                <text x="48" y="116" font-size="8.5" font-weight="extrabold" fill="#0284c7" text-anchor="middle">Fluss Spree</text>
                <!-- Cây cầu bắc qua sông -->
                <rect x="100" y="15" width="100" height="150" rx="6" fill="#334155" stroke="#475569" stroke-width="2"/>
                <rect x="94" y="15" width="6" height="150" fill="#94a3b8"/>
                <rect x="200" y="15" width="6" height="150" fill="#94a3b8"/>
                <!-- Vạch kẻ cầu -->
                <line x1="150" y1="20" x2="150" y2="160" stroke="#ffffff" stroke-width="2" stroke-dasharray="8 6"/>
                <!-- Badge ngữ pháp góc trên bờ trái -->
                <rect x="8" y="10" width="82" height="26" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
                <text x="49" y="27" font-size="9" font-weight="black" fill="#15803d" text-anchor="middle">über + AKKUSATIV</text>
                <!-- Nhãn tên cây cầu góc trên bờ phải -->
                <rect x="208" y="10" width="84" height="26" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="250" y="27" font-size="8.5" font-weight="extrabold" fill="#1e293b" text-anchor="middle">Schlossbrücke</text>
                <!-- Mũi tên đi vượt qua mặt cầu -->
                <path d="M150 168 L150 25" fill="none" stroke="#16a34a" stroke-width="6" stroke-linecap="round"/>
                <polygon points="150,10 140,30 160,30" fill="#15803d"/>
                <circle cx="150" cy="168" r="5" fill="#15803d"/>
                <!-- Chú thích phía dưới -->
                <rect x="45" y="147" width="210" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="150" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 über die Brücke (băng qua mặt cầu)</text>
            </svg>`;
        } else {
            // entlang
            return `
            <svg viewBox="0 0 300 180" width="${width}" height="${height}" class="w-full max-w-md mx-auto rounded-2xl shadow-sm border border-slate-200 bg-white">
                <rect x="0" y="0" width="300" height="180" fill="#f8fafc"/>
                <!-- Con đường chạy dọc uốn khúc nhẹ -->
                <path d="M60 180 C 100 110, 200 110, 240 0 L 290 0 C 250 110, 150 110, 110 180 Z" fill="#334155"/>
                <path d="M85 180 C 125 110, 225 110, 265 0" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/>
                <!-- Badge ngữ pháp góc trên bên trái -->
                <rect x="10" y="10" width="145" height="25" rx="6" fill="#fefce8" stroke="#fde047" stroke-width="1.5"/>
                <text x="82.5" y="26.5" font-size="10.5" font-weight="black" fill="#a16207" text-anchor="middle">AKKUSATIV + entlang</text>
                <!-- Nhãn tên đường đặt phía dưới badge ngữ pháp bên trái, hoàn toàn tách biệt khỏi mũi tên -->
                <rect x="10" y="40" width="125" height="24" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
                <text x="72.5" y="56" font-size="9" font-weight="extrabold" fill="#1e293b" text-anchor="middle">die Friedrichstraße</text>
                <!-- Mũi tên chạy dọc theo con đường -->
                <path d="M85 168 C 125 105, 225 105, 265 20" fill="none" stroke="#ca8a04" stroke-width="6" stroke-linecap="round"/>
                <polygon points="268,8 253,22 271,28" fill="#a16207"/>
                <circle cx="85" cy="168" r="5" fill="#a16207"/>
                <!-- Chú thích -->
                <rect x="30" y="147" width="240" height="24" rx="6" fill="#fef3c7" stroke="#f59e0b"/>
                <text x="150" y="163" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">👉 die Straße entlang (dọc theo con đường)</text>
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
            <text x="404" y="352" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Alexanderstraße</text>
            <text x="18" y="286" font-size="8.5" font-weight="bold" fill="#94a3b8">Leipziger Str.</text>
            <text x="18" y="166" font-size="8.5" font-weight="bold" fill="#94a3b8">Behrenstraße</text>
            <text x="18" y="56" font-size="8.5" font-weight="bold" fill="#94a3b8">Unter den Linden</text>

            <!-- TÒA NHÀ & ĐỊA ĐIỂM -->
            <!-- 1. Vị trí Start (Sie sind hier) trên Friedrichstraße giữa Leipziger Str. và Behrenstraße -->
            <circle cx="84" cy="235" r="13" fill="#f43f5e" stroke="#ffffff" stroke-width="2.5"/>
            <circle cx="84" cy="235" r="4.5" fill="#ffffff"/>
            <text x="104" y="232" font-size="10" font-weight="black" fill="#f43f5e" text-anchor="start">📍 START</text>
            <text x="104" y="244" font-size="8" font-weight="bold" fill="#fda4af" text-anchor="start">(Sie sind hier)</text>

            <!-- 2. Ngân hàng Bank (trên đường Behrenstraße giữa ngã 1 và 2) -->
            <rect x="125" y="105" width="75" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="162.5" y="125" font-size="14" text-anchor="middle">🏦</text>
            <text x="162.5" y="138" font-size="9" font-weight="extrabold" fill="#bfdbfe" text-anchor="middle">Bank</text>

            <!-- 3. Nhà thờ Kirche (bên trái đường dọc 1) -->
            <rect x="5" y="85" width="48" height="55" rx="6" fill="#3f3f46" stroke="#71717a" stroke-width="1.5"/>
            <text x="29" y="112" font-size="14" text-anchor="middle">⛪</text>
            <text x="29" y="126" font-size="8" font-weight="bold" fill="#e4e4e7" text-anchor="middle">Kirche</text>

            <!-- 4. Rạp chiếu phim Kino (bên trái đường dọc 2 góc trên) -->
            <rect x="135" y="5" width="75" height="32" rx="5" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
            <text x="172.5" y="24" font-size="12" text-anchor="middle">🎬 Kino</text>

            <!-- 5. ĐÍCH ĐẾN: Bưu điện Post & Đèn giao thông Ampel (Góc trên bên phải) -->
            <rect x="440" y="5" width="90" height="45" rx="8" fill="#854d0e" stroke="#eab308" stroke-width="2"/>
            <text x="485" y="26" font-size="14" text-anchor="middle">📮</text>
            <text x="485" y="40" font-size="10" font-weight="black" fill="#fef08a" text-anchor="middle">Post</text>
            <!-- Đèn giao thông Ampel ngay trước Bưu điện -->
            <rect x="408" y="20" width="12" height="24" rx="2" fill="#000000" stroke="#eab308" stroke-width="1"/>
            <circle cx="414" cy="25" r="2" fill="#ef4444"/>
            <circle cx="414" cy="32" r="2" fill="#f59e0b"/>
            <circle cx="414" cy="39" r="2" fill="#10b981"/>
            <text x="414" y="14" font-size="7.5" font-weight="bold" fill="#fbbf24" text-anchor="middle">Ampel 🚦</text>

            <!-- 6. Ga tàu Bahnhof ở góc phải dưới -->
            <rect x="440" y="110" width="90" height="40" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="485" y="130" font-size="12" text-anchor="middle">🚉 Bahnhof</text>

            <!-- ================= LỘ TRÌNH 1 (XANH DƯƠNG) ================= -->
            ${isRoute1 ? `
            <g id="route-1-layer">
                <!-- Đường đi: Start(84,235) -> thẳng lên ngã 1(84,172) -> rẽ phải qua Bank tới ngã 2(244,172) -> rẽ trái lên ngã 3(244,62) -> rẽ phải đường Unter den Linden tới Ampel(414,62) -> Post ngay trước mắt -->
                <path d="M 84 235 L 84 172 L 244 172 L 244 62 L 414 62" fill="none" stroke="#3b82f6" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M 84 235 L 84 172 L 244 172 L 244 62 L 414 62" fill="none" stroke="#93c5fd" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 8"/>
                <!-- Mũi tên chỉ hướng chặng 1 (đi thẳng lên ngã 1) -->
                <polygon points="84,198 78,210 90,210" fill="#2563eb"/>
                <!-- Mũi tên rẽ phải qua Bank -->
                <polygon points="175,172 163,166 163,178" fill="#2563eb"/>
                <!-- Mũi tên rẽ trái lên ngã tư 2 -->
                <polygon points="244,110 238,122 250,122" fill="#2563eb"/>
                <!-- Mũi tên rẽ phải đường Unter den Linden tới Ampel -->
                <polygon points="340,62 328,56 328,68" fill="#2563eb"/>
                <!-- Đích đến Post -->
                <circle cx="414" cy="62" r="11" fill="#3b82f6" stroke="#ffffff" stroke-width="2"/>
                <text x="414" y="65" font-size="8.5" font-weight="black" fill="#ffffff" text-anchor="middle">ZIEL</text>
            </g>
            ` : ''}

            <!-- ================= LỘ TRÌNH 2 (XANH LÁ) ================= -->
            ${isRoute2 ? `
            <g id="route-2-layer">
                <!-- Lộ trình 2: Start(84,235) -> Đi thẳng qua ngã 1 -> lên ngã 2 bên phải(84,62) -> rẽ phải đi thẳng băng qua ngã tư -> tới Ampel/Post(414,62) -->
                <path d="M 84 235 L 84 62 L 414 62" fill="none" stroke="#10b981" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M 84 235 L 84 62 L 414 62" fill="none" stroke="#a7f3d0" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 8"/>
                <!-- Mũi tên thẳng lên -->
                <polygon points="84,198 78,210 90,210" fill="#059669"/>
                <polygon points="84,110 78,122 90,122" fill="#059669"/>
                <!-- Mũi tên rẽ phải ngã tư 2 đi thẳng băng qua -->
                <polygon points="180,62 168,56 168,68" fill="#059669"/>
                <polygon points="310,62 298,56 298,68" fill="#059669"/>
                <!-- Đích đến tại Ampel sát Post -->
                <circle cx="414" cy="62" r="11" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
                <text x="414" y="65" font-size="8.5" font-weight="black" fill="#ffffff" text-anchor="middle">ZIEL</text>
            </g>
            ` : ''}
        </svg>`;
    }


    // =========================================================================
    // 3B. CÁC HÀM VẼ SVG CHO BÀI TẬP BÀI 8 (ZERO SPOILERS - KHÔNG LỘ ĐÁP ÁN)
    // =========================================================================

    // Thẻ chỉ hướng sạch cho Quiz (loại bỏ chữ text chỉ hướng tiếng Đức)
    function getCleanDirectionSvg(code, width = 160, height = 120) {
        let svg = getDirectionSvg(code, width, height);
        // Loại bỏ các thẻ <text> chứa gợi ý trực tiếp như hier links, 2. Straße (links), v.v.
        svg = svg.replace(/<text[^>]*>.*?<\/text>/gi, '');
        return svg;
    }

    // 1. map_route_finder_1 (Câu 1: START -> ngã 1 qua thẳng -> ngã 2 rẽ phải -> qua Krankenhaus bên trái -> tới Ampel ở ngã tư -> Kino bên trái ngay sau Ampel)
    function getMapRouteFinder1Svg() {
        return `
        <svg viewBox="0 0 520 320" width="100%" class="w-full max-w-xl mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="520" height="320" fill="#0f172a"/>
            <!-- Lưới đường phố 3x3 -->
            <rect x="60" y="0" width="44" height="320" fill="#1e293b"/>
            <line x1="82" y1="0" x2="82" y2="320" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <rect x="220" y="0" width="44" height="320" fill="#1e293b"/>
            <line x1="242" y1="0" x2="242" y2="320" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <rect x="380" y="0" width="44" height="320" fill="#1e293b"/>
            <line x1="402" y1="0" x2="402" y2="320" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <rect x="0" y="240" width="520" height="40" fill="#1e293b"/>
            <line x1="0" y1="260" x2="520" y2="260" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <rect x="0" y="140" width="520" height="40" fill="#1e293b"/>
            <line x1="0" y1="160" x2="520" y2="160" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <rect x="0" y="40" width="520" height="40" fill="#1e293b"/>
            <line x1="0" y1="60" x2="520" y2="60" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Tên các con đường -->
            <text x="82" y="312" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Friedrichstr.</text>
            <text x="242" y="312" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Wilhelmstr.</text>
            <text x="402" y="312" font-size="8.5" font-weight="bold" fill="#94a3b8" text-anchor="middle">Alexanderstr.</text>
            <text x="12" y="255" font-size="8.5" font-weight="bold" fill="#94a3b8">Leipziger Str.</text>
            <text x="12" y="155" font-size="8.5" font-weight="bold" fill="#94a3b8">Behrenstr.</text>
            <text x="12" y="55" font-size="8.5" font-weight="bold" fill="#94a3b8">Unter den Linden</text>

            <!-- Điểm START: vòng tròn bán kính 16 đủ lớn chứa trọn vẹn chữ START không bị clip -->
            <circle cx="82" cy="290" r="16" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>
            <text x="82" y="290" font-size="7.5" font-weight="black" fill="#ffffff" text-anchor="middle" dominant-baseline="central">START</text>

            <!-- Tòa nhà Krankenhaus (nằm bên trái của đường Behrenstraße, trước khi tới ngã tư Ampel) -->
            <rect x="120" y="92" width="85" height="40" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="162.5" y="112" font-size="12" text-anchor="middle">🏥</text>
            <text x="162.5" y="125" font-size="8.5" font-weight="bold" fill="#bfdbfe" text-anchor="middle">Krankenhaus</text>

            <!-- Cột đèn giao thông Ampel tại đúng ngã tư Behrenstr. x Wilhelmstr. -->
            <rect x="236" y="142" width="12" height="24" rx="2" fill="#020617" stroke="#eab308" stroke-width="1"/>
            <circle cx="242" cy="147" r="2.5" fill="#ef4444"/>
            <circle cx="242" cy="154" r="2.5" fill="#f59e0b"/>
            <circle cx="242" cy="161" r="2.5" fill="#10b981"/>
            <text x="242" y="136" font-size="7.5" font-weight="bold" fill="#fde047" text-anchor="middle">Ampel 🚦</text>

            <!-- Tòa nhà Kino (nằm bên trái ngay sau Ampel trên Behrenstraße) -->
            <rect x="275" y="92" width="85" height="40" rx="6" fill="#581c87" stroke="#a855f7" stroke-width="1.5"/>
            <text x="317.5" y="112" font-size="12" text-anchor="middle">🎬</text>
            <text x="317.5" y="125" font-size="8.5" font-weight="bold" fill="#e9d5ff" text-anchor="middle">Kino</text>

            <!-- Tòa nhà khác: Schloss, Post, Bahnhof -->
            <rect x="120" y="5" width="85" height="30" rx="5" fill="#3f3f46" stroke="#71717a" stroke-width="1.5"/>
            <text x="162.5" y="24" font-size="8" font-weight="bold" fill="#e4e4e7" text-anchor="middle">🏰 Schloss</text>

            <rect x="435" y="92" width="75" height="40" rx="6" fill="#854d0e" stroke="#eab308" stroke-width="1.5"/>
            <text x="472.5" y="112" font-size="12" text-anchor="middle">📮</text>
            <text x="472.5" y="125" font-size="8.5" font-weight="bold" fill="#fef08a" text-anchor="middle">Post</text>

            <rect x="435" y="242" width="75" height="35" rx="5" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="472.5" y="264" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">🚉 Bahnhof</text>
        </svg>`;
    }

    // 2. map_route_line_2 (Câu 2: START -> thẳng -> ngã tư 3 rẽ trái -> qua Brücke trước -> xuyên Park sau -> Einkaufszentrum bên phải)
    function getMapRouteLine2Svg() {
        return `
        <svg viewBox="0 0 520 320" width="100%" class="w-full max-w-xl mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <!-- Lớp 1: Nền bản đồ -->
            <rect x="0" y="0" width="520" height="320" fill="#0f172a"/>

            <!-- Lớp 2: Hệ thống đường xá & Dòng sông Spree -->
            <rect x="200" y="0" width="40" height="320" fill="#1e293b"/>
            <line x1="220" y1="0" x2="220" y2="320" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <rect x="360" y="0" width="40" height="320" fill="#1e293b"/>

            <rect x="0" y="250" width="520" height="36" fill="#1e293b"/>
            <rect x="0" y="160" width="520" height="36" fill="#1e293b"/>
            <!-- Đường ngang số 3 chạy qua toàn bộ bản đồ -->
            <rect x="0" y="60" width="520" height="40" fill="#1e293b"/>
            <line x1="0" y1="80" x2="520" y2="80" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Dòng sông Spree màu xanh chảy dọc -->
            <rect x="145" y="0" width="30" height="320" fill="#0284c7"/>
            <text x="160" y="30" font-size="8.5" font-weight="bold" fill="#bae6fd" text-anchor="middle">Spree</text>
            <text x="160" y="295" font-size="8.5" font-weight="bold" fill="#bae6fd" text-anchor="middle">Spree</text>

            <!-- Lớp 3: Tòa nhà Einkaufszentrum (ở phía bắc đường số 3, không có viền thừa) -->
            <rect x="10" y="10" width="115" height="42" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
            <text x="67.5" y="27" font-size="11" text-anchor="middle">🛍️</text>
            <text x="67.5" y="41" font-size="8.5" font-weight="bold" fill="#a7f3d0" text-anchor="middle">Einkaufszentrum</text>

            <!-- Lớp 4: Khung Park (nằm TRÊN đường, phần xanh liền mạch không bị cắt ngang, không viền thừa) -->
            <rect x="45" y="60" width="85" height="85" rx="8" fill="#065f46" stroke="#059669" stroke-width="2"/>
            <!-- Lối đi mờ nội bộ công viên -->
            <line x1="45" y1="80" x2="130" y2="80" stroke="#047857" stroke-width="3" stroke-dasharray="4 4"/>
            <!-- Nhãn Park ở phía dưới, hoàn toàn không bị đường xanh che -->
            <text x="87.5" y="132" font-size="9" font-weight="bold" fill="#6ee7b7" text-anchor="middle">🌳 Park</text>

            <!-- Lớp 5: Cầu bắc qua sông Spree trên đường số 3 (gọn gàng, hai lan can bên) -->
            <rect x="143" y="58" width="34" height="44" rx="2" fill="#334155" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="143" y1="60" x2="177" y2="60" stroke="#cbd5e1" stroke-width="2.5"/>
            <line x1="143" y1="100" x2="177" y2="100" stroke="#cbd5e1" stroke-width="2.5"/>
            <text x="160" y="52" font-size="8" font-weight="bold" fill="#cbd5e1" text-anchor="middle">🌉 Brücke</text>

            <!-- Điểm START: bán kính 16 đủ lớn chứa trọn vẹn chữ START không bị clip -->
            <circle cx="220" cy="295" r="16" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>
            <text x="220" y="295" font-size="7.5" font-weight="black" fill="#ffffff" text-anchor="middle" dominant-baseline="central">START</text>

            <!-- Lớp 6: ĐƯỜNG VẼ MÀU XANH DƯƠNG TRÊN CÙNG: Đi thẳng -> ngã 3 rẽ trái -> qua cầu -> xuyên BÊN TRONG công viên Park -> Einkaufszentrum bên phải -->
            <path d="M 220 295 L 220 80 L 35 80 L 35 55" fill="none" stroke="#3b82f6" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M 220 295 L 220 80 L 35 80 L 35 55" fill="none" stroke="#93c5fd" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="6 4"/>
            <polygon points="220,185 214,197 226,197" fill="#1d4ed8"/>
            <polygon points="160,80 172,74 172,86" fill="#1d4ed8"/>
            <polygon points="85,80 97,74 97,86" fill="#1d4ed8"/>
            <circle cx="35" cy="55" r="6" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5"/>
        </svg>`;
    }

    // 3. quiz_spatial_3_steps (Câu 3: Sơ đồ 3 hình 1 -> 2 -> 3: Staatsoper, Stadttor, Fluss)
    function getQuizSpatial3StepsSvg() {
        return `
        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 my-2">
            <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1.5">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-600 text-white font-black text-xs">1</span>
                <svg viewBox="0 0 160 120" width="100%" class="rounded-xl border border-slate-200 bg-white mx-auto">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <rect x="15" y="0" width="50" height="120" fill="#334155"/>
                    <rect x="80" y="25" width="70" height="70" rx="6" fill="#e2e8f0" stroke="#64748b" stroke-width="1.5"/>
                    <text x="115" y="55" font-size="16" text-anchor="middle">🎭</text>
                    <text x="115" y="75" font-size="8.5" font-weight="bold" fill="#334155" text-anchor="middle">Staatsoper</text>
                    <path d="M 40 110 L 40 18" fill="none" stroke="#2563eb" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="40,10 32,25 48,25" fill="#1d4ed8"/>
                    <circle cx="40" cy="110" r="4" fill="#1d4ed8"/>
                </svg>
            </div>

            <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1.5">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-rose-600 text-white font-black text-xs">2</span>
                <svg viewBox="0 0 160 120" width="100%" class="rounded-xl border border-slate-200 bg-white mx-auto">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <rect x="55" y="0" width="50" height="120" fill="#334155"/>
                    <rect x="15" y="44" width="130" height="42" rx="4" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
                    <path d="M 60 86 L 60 60 A 20 20 0 0 1 100 60 L 100 86 Z" fill="#334155"/>
                    <!-- Mũi tên đâm xuyên qua cổng -->
                    <path d="M 80 112 L 80 34" fill="none" stroke="#e11d48" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="80,24 72,39 88,39" fill="#be123c"/>
                    <circle cx="80" cy="112" r="4" fill="#be123c"/>
                    <!-- Nhãn Stadttor đặt lớp trên cùng ở phía trên đỉnh cổng, đọc trọn vẹn chữ không bị che -->
                    <rect x="42" y="8" width="76" height="18" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
                    <text x="80" y="20" font-size="8.5" font-weight="black" fill="#1e293b" text-anchor="middle" dominant-baseline="central">🏰 Stadttor</text>
                </svg>
            </div>

            <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1.5">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-emerald-600 text-white font-black text-xs">3</span>
                <svg viewBox="0 0 160 120" width="100%" class="rounded-xl border border-slate-200 bg-white mx-auto">
                    <rect x="0" y="0" width="160" height="120" fill="#f8fafc"/>
                    <!-- Bờ sông -->
                    <rect x="110" y="0" width="50" height="120" fill="#38bdf8"/>
                    <text x="135" y="65" font-size="8.5" font-weight="bold" fill="#0369a1" text-anchor="middle" transform="rotate(-90 135 65)">Fluss</text>
                    <!-- Con đường song song -->
                    <rect x="30" y="0" width="60" height="120" fill="#334155"/>
                    <path d="M 60 110 L 60 15" fill="none" stroke="#16a34a" stroke-width="5" stroke-linecap="round"/>
                    <polygon points="60,8 52,22 68,22" fill="#15803d"/>
                    <circle cx="60" cy="110" r="4" fill="#15803d"/>
                    <!-- Icon cây bên đường (thay cho các chấm tròn) -->
                    <text x="16" y="38" font-size="13" text-anchor="middle">🌳</text>
                    <text x="16" y="88" font-size="13" text-anchor="middle">🌳</text>
                </svg>
            </div>
        </div>`;
    }

    // 4. map_route_line_3 (Câu 5: Lộ trình ĐI THẲNG từ dưới lên: START -> Humboldt-Universität -> Berliner Dom -> Ampel -> Marktplatz -> Rathaus)
    function getMapRouteLine3Svg() {
        return `
        <svg viewBox="0 0 520 380" width="100%" class="w-full max-w-xl mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="520" height="380" fill="#0f172a"/>

            <!-- Đại lộ thẳng đứng ở giữa bản đồ -->
            <rect x="145" y="0" width="50" height="380" fill="#1e293b"/>
            <line x1="170" y1="0" x2="170" y2="380" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Điểm START ở dưới cùng của đại lộ (bán kính 16 chứa trọn vẹn chữ START) -->
            <circle cx="170" cy="350" r="16" fill="#3b82f6" stroke="#ffffff" stroke-width="2.5"/>
            <text x="170" y="350" font-size="7.5" font-weight="black" fill="#ffffff" text-anchor="middle" dominant-baseline="central">START</text>

            <!-- Tòa nhà 1: Humboldt-Universität nằm bên PHẢI đại lộ -->
            <rect x="210" y="270" width="180" height="42" rx="5" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="300" y="295" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">🏛️ Humboldt-Universität</text>

            <!-- Tòa nhà 2: Berliner Dom nằm bên PHẢI đại lộ -->
            <rect x="210" y="195" width="180" height="42" rx="5" fill="#3f3f46" stroke="#71717a" stroke-width="1.5"/>
            <text x="300" y="220" font-size="9" font-weight="bold" fill="#fef08a" text-anchor="middle">⛪ Berliner Dom</text>

            <!-- Vạch dừng và Cột đèn giao thông Ampel nằm ngay trên đại lộ -->
            <rect x="145" y="152" width="50" height="4" fill="#ffffff"/>
            <rect x="125" y="132" width="12" height="24" rx="2" fill="#000" stroke="#f59e0b" stroke-width="1"/>
            <circle cx="131" cy="137" r="2" fill="#ef4444"/>
            <circle cx="131" cy="144" r="2" fill="#f59e0b"/>
            <circle cx="131" cy="151" r="2" fill="#10b981"/>
            <text x="110" y="146" font-size="8" font-weight="bold" fill="#fde047" text-anchor="end">Ampel 🚦</text>

            <!-- Vùng quảng trường Marktplatz (nằm trên đường, có nhãn tiếng Đức đọc rõ bên phải, không bị đường xanh che) -->
            <rect x="85" y="65" width="310" height="58" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
            <text x="300" y="99" font-size="11" font-weight="black" fill="#92400e" text-anchor="middle">⭕ Marktplatz</text>

            <!-- Tòa thị chính Rathaus (ZIEL) ở cuối đường phía trên cùng -->
            <rect x="105" y="8" width="130" height="42" rx="6" fill="#854d0e" stroke="#eab308" stroke-width="2"/>
            <text x="170" y="26" font-size="11" text-anchor="middle">🏛️</text>
            <text x="170" y="39" font-size="8.5" font-weight="black" fill="#fef08a" text-anchor="middle">Rathaus (ZIEL)</text>

            <!-- Tuyến đường màu xanh dương ĐI THẲNG MỘT MẠCH từ START -> qua Universität -> qua Dom -> tới Ampel -> qua Marktplatz -> Rathaus -->
            <path d="M 170 350 L 170 50" fill="none" stroke="#3b82f6" stroke-width="6" stroke-linecap="round"/>
            <path d="M 170 350 L 170 50" fill="none" stroke="#93c5fd" stroke-width="2" stroke-linecap="round" stroke-dasharray="6 4"/>
            <polygon points="170,285 164,297 176,297" fill="#1d4ed8"/>
            <polygon points="170,210 164,222 176,222" fill="#1d4ed8"/>
            <polygon points="170,105 164,117 176,117" fill="#1d4ed8"/>
            <circle cx="170" cy="50" r="5" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5"/>
        </svg>`;
    }

    // 5. map_error_check_1 (Câu 12: Hauptbahnhof -> thẳng ngã 1 -> rẽ trái ngã 2 -> qua Kirche bên phải -> rẽ phải tới Theater)
    function getMapErrorCheck1Svg() {
        return `
        <svg viewBox="0 0 500 300" width="100%" class="w-full max-w-xl mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="500" height="300" fill="#0f172a"/>
            <rect x="250" y="0" width="44" height="300" fill="#1e293b"/>
            <rect x="0" y="200" width="500" height="40" fill="#1e293b"/>
            <rect x="0" y="80" width="500" height="40" fill="#1e293b"/>

            <!-- Hauptbahnhof (START) - Khung nới rộng 170px chứa trọn vẹn nhãn không bị tràn -->
            <rect x="187" y="250" width="170" height="38" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="272" y="274" font-size="8.5" font-weight="bold" fill="#e2e8f0" text-anchor="middle">🚉 Hauptbahnhof (START)</text>

            <!-- Kirche ở phía trên đường ngang thứ 2 (nằm bên PHẢI người đi khi đi về hướng tây) -->
            <rect x="130" y="35" width="70" height="38" rx="5" fill="#3f3f46" stroke="#71717a" stroke-width="1.5"/>
            <text x="165" y="59" font-size="8" font-weight="bold" fill="#e4e4e7" text-anchor="middle">⛪ Kirche</text>

            <!-- Theater ở cuối đường rẽ trái -->
            <rect x="20" y="35" width="75" height="38" rx="5" fill="#831843" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="57.5" y="59" font-size="8.5" font-weight="bold" fill="#fbcfe8" text-anchor="middle">🎭 Theater (ZIEL)</text>

            <!-- Tuyến đường mũi tên vàng -->
            <path d="M 272 250 L 272 100 L 58 100 L 58 75" fill="none" stroke="#eab308" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
            <polygon points="272,160 266,172 278,172" fill="#ca8a04"/>
            <polygon points="170,100 182,94 182,106" fill="#ca8a04"/>
            <polygon points="58,74 52,86 64,86" fill="#ca8a04"/>
        </svg>`;
    }

    // 6. map_fill_1 (Câu 19: START -> an der Bank vorbei -> links abbiegen -> Krankenhaus)
    function getMapFill1Svg() {
        return `
        <svg viewBox="0 0 480 260" width="100%" class="w-full max-w-lg mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="480" height="260" fill="#0f172a"/>

            <!-- Địa điểm phụ ở xa lộ trình: Supermarkt (phía trên bên trái), Post (phía dưới bên phải) -->
            <rect x="40" y="25" width="85" height="38" rx="6" fill="#065f46" stroke="#10b981" stroke-width="1.5"/>
            <text x="82.5" y="49" font-size="8.5" font-weight="bold" fill="#a7f3d0" text-anchor="middle">🛒 Supermarkt</text>

            <rect x="360" y="200" width="75" height="38" rx="6" fill="#854d0e" stroke="#eab308" stroke-width="1.5"/>
            <text x="397.5" y="224" font-size="8.5" font-weight="bold" fill="#fef08a" text-anchor="middle">📮 Post</text>

            <!-- Đường chính nằm ngang ở phía dưới: từ x=20 đến x=460, y=140 đến 184 (rộng 44, tâm y=162) -->
            <rect x="20" y="140" width="440" height="44" fill="#1e293b"/>
            <line x1="20" y1="162" x2="460" y2="162" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Ngã rẽ lên trên (đường dọc đi lên phía bắc): từ y=20 đến y=140, x=270 đến 314 (rộng 44, tâm x=292) -->
            <rect x="270" y="20" width="44" height="120" fill="#1e293b"/>
            <line x1="292" y1="20" x2="292" y2="140" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Khối Bank: nằm sát đường, phía bên PHẢI người đi (phía dưới đường nằm ngang: y=192..236), TRƯỚC ngã rẽ (x=140..240) -->
            <rect x="140" y="192" width="100" height="44" rx="6" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
            <text x="190" y="212" font-size="12" text-anchor="middle">🏦</text>
            <text x="190" y="226" font-size="8.5" font-weight="bold" fill="#e2e8f0" text-anchor="middle">Bank</text>

            <!-- Khối Krankenhaus: ở đích đến (đỉnh đường rẽ lên phía trên: y=15..57, x=240..344) -->
            <rect x="240" y="15" width="104" height="42" rx="6" fill="#1e3a8a" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="292" y="34" font-size="12" text-anchor="middle">🏥</text>
            <text x="292" y="48" font-size="8.5" font-weight="bold" fill="#bfdbfe" text-anchor="middle">Krankenhaus (ZIEL)</text>

            <!-- Lộ trình mũi tên xanh dương: bắt đầu từ mép vòng tròn START (x=76, y=162) đi thẳng qua Bank -> tới ngã rẽ x=292 -> rẽ TRÁI đi thẳng lên Krankenhaus y=65 -->
            <path d="M 76 162 L 292 162 L 292 65" fill="none" stroke="#3b82f6" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
            <polygon points="292,57 284,72 300,72" fill="#1d4ed8"/>
            <polygon points="220,162 208,156 208,168" fill="#1d4ed8"/>

            <!-- Điểm START ở dưới bên trái: cx=60, cy=162. Vòng tròn r=16 nằm trên cùng, chữ START trọn vẹn không bị mũi tên đè -->
            <circle cx="60" cy="162" r="16" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>
            <text x="60" y="162" font-size="7.5" font-weight="black" fill="#ffffff" text-anchor="middle" dominant-baseline="central">START</text>
        </svg>`;
    }

    // 7. map_fill_2 (Câu 20: Friedrichstraße dọc -> rechts in die Blumenstraße -> am Schloss vorbei -> Kunstmuseum)
    function getMapFill2Svg() {
        return `
        <svg viewBox="0 0 480 240" width="100%" class="w-full max-w-lg mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="480" height="240" fill="#0f172a"/>

            <!-- Friedrichstraße dọc -->
            <rect x="80" y="0" width="46" height="240" fill="#1e293b"/>
            <line x1="103" y1="0" x2="103" y2="240" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <text x="65" y="120" font-size="8" font-weight="bold" fill="#94a3b8" transform="rotate(-90 65 120)">Friedrichstraße</text>

            <!-- Blumenstraße ngang -->
            <rect x="126" y="60" width="334" height="42" fill="#1e293b"/>
            <line x1="126" y1="81" x2="460" y2="81" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>
            <text x="210" y="52" font-size="8.5" font-weight="bold" fill="#94a3b8">Blumenstraße</text>

            <!-- Khối Schloss: nằm sát đường trên lộ trình Blumenstraße (y=110..152, x=180..265) -->
            <rect x="180" y="110" width="90" height="42" rx="6" fill="#3f3f46" stroke="#71717a" stroke-width="1.5"/>
            <text x="225" y="128" font-size="11" text-anchor="middle">🏰</text>
            <text x="225" y="142" font-size="8.5" font-weight="bold" fill="#fef08a" text-anchor="middle">Schloss</text>

            <!-- Khối Kunstmuseum: ở cuối lộ trình sau Schloss (x=335..450, y=60..102) -->
            <rect x="335" y="60" width="115" height="42" rx="6" fill="#831843" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="392.5" y="78" font-size="11" text-anchor="middle">🏛️</text>
            <text x="392.5" y="92" font-size="8.5" font-weight="bold" fill="#fbcfe8" text-anchor="middle">Kunstmuseum (ZIEL)</text>

            <!-- Lộ trình mũi tên vàng: từ mép trên START (x=103, y=179) đi lên Friedrichstraße -> rẽ phải vào Blumenstraße -> qua Schloss -> dừng trước Kunstmuseum (x=330, y=81) -->
            <path d="M 103 179 L 103 81 L 330 81" fill="none" stroke="#eab308" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
            <polygon points="330,81 318,75 318,87" fill="#ca8a04"/>
            <polygon points="103,130 97,142 109,142" fill="#ca8a04"/>
            <polygon points="230,81 218,75 218,87" fill="#ca8a04"/>

            <!-- Điểm START ở dưới cùng Friedrichstraße: cx=103, cy=195. r=16 vẽ trên cùng, chữ START trọn vẹn không bị đè -->
            <circle cx="103" cy="195" r="16" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>
            <text x="103" y="195" font-size="7.5" font-weight="black" fill="#ffffff" text-anchor="middle" dominant-baseline="central">START</text>
        </svg>`;
    }

    // 8. quiz_icon_bridge (Câu 21: Icon cầu qua sông sạch sẽ)
    function getQuizIconBridgeSvg() {
        return `
        <svg viewBox="0 0 200 130" width="200" height="130" class="mx-auto rounded-2xl border border-slate-200 bg-slate-50">
            <rect x="0" y="0" width="200" height="130" fill="#f8fafc"/>
            <rect x="0" y="40" width="200" height="50" fill="#38bdf8"/>
            <path d="M 0 55 Q 50 50 100 55 T 200 55" fill="none" stroke="#0284c7" stroke-width="2"/>
            <!-- Cây cầu -->
            <rect x="75" y="15" width="50" height="100" rx="3" fill="#334155" stroke="#475569" stroke-width="1.5"/>
            <rect x="71" y="15" width="4" height="100" fill="#94a3b8"/>
            <rect x="125" y="15" width="4" height="100" fill="#94a3b8"/>
            <!-- Mũi tên vượt qua cầu -->
            <path d="M 100 115 L 100 15" fill="none" stroke="#16a34a" stroke-width="5" stroke-linecap="round"/>
            <polygon points="100,8 92,23 108,23" fill="#15803d"/>
            <circle cx="100" cy="115" r="4" fill="#15803d"/>
        </svg>`;
    }

    // 9. quiz_icon_gate (Câu 22: Icon cổng vòm đục thủng xuyên qua sạch sẽ)
    function getQuizIconGateSvg() {
        return `
        <svg viewBox="0 0 200 130" width="200" height="130" class="mx-auto rounded-2xl border border-slate-200 bg-slate-50">
            <rect x="0" y="0" width="200" height="130" fill="#f8fafc"/>
            <rect x="70" y="0" width="60" height="130" fill="#334155"/>
            <!-- Tòa cổng vòm -->
            <rect x="25" y="45" width="150" height="45" rx="4" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
            <path d="M 75 90 L 75 60 A 25 25 0 0 1 125 60 L 125 90 Z" fill="#334155"/>
            <polygon points="100,28 20,45 180,45" fill="#e11d48"/>
            <!-- Mũi tên đâm xuyên qua cổng -->
            <path d="M 100 120 L 100 12" fill="none" stroke="#e11d48" stroke-width="5" stroke-linecap="round"/>
            <polygon points="100,5 92,20 108,20" fill="#be123c"/>
            <circle cx="100" cy="120" r="4" fill="#be123c"/>
        </svg>`;
    }

    // 10. quiz_icon_along (Câu 23: Icon mũi tên đi dọc theo con đường rộng breite Straße / hàng cây / Zoo)
    function getQuizIconAlongSvg() {
        return `
        <svg viewBox="0 0 200 130" width="200" height="130" class="mx-auto rounded-2xl border border-slate-200 bg-slate-50">
            <rect x="0" y="0" width="200" height="130" fill="#f8fafc"/>
            <!-- Con đường rộng hơn một chút để khớp 'breite Straße' -->
            <path d="M 30 130 C 52 70, 132 70, 112 0 L 175 0 C 195 70, 115 70, 93 130 Z" fill="#334155"/>
            <path d="M 62 130 C 82 70, 162 70, 142 0" fill="none" stroke="#f8fafc" stroke-width="2" stroke-dasharray="6 4"/>

            <!-- Hàng cây bên lề đường (icon cây 🌳 không chữ thay cho chấm tròn) -->
            <text x="18" y="105" font-size="12" text-anchor="middle">🌳</text>
            <text x="36" y="60" font-size="12" text-anchor="middle">🌳</text>
            <text x="68" y="28" font-size="12" text-anchor="middle">🌳</text>

            <!-- Khối Zoo ở phía cuối đường, bên TRÁI mũi tên -->
            <rect x="76" y="6" width="46" height="24" rx="4" fill="#065f46" stroke="#10b981" stroke-width="1.2"/>
            <text x="99" y="21" font-size="8.5" font-weight="bold" fill="#a7f3d0" text-anchor="middle">🦁 Zoo</text>

            <!-- Mũi tên uốn lượn chạy dọc con đường -->
            <path d="M 62 120 C 82 65, 162 65, 142 15" fill="none" stroke="#ca8a04" stroke-width="5" stroke-linecap="round"/>
            <polygon points="142,8 133,22 149,21" fill="#a16207"/>
            <circle cx="62" cy="120" r="4" fill="#a16207"/>
        </svg>`;
    }

    // 11. map_build_1 (Câu 68: START -> durch den Park -> an der Kirche vorbei -> bis zum Bahnhof)
    function getMapBuild1Svg() {
        return `
        <svg viewBox="0 0 460 220" width="100%" class="w-full max-w-lg mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="460" height="220" fill="#0f172a"/>

            <!-- Con đường chạy ngang -->
            <rect x="30" y="88" width="400" height="44" fill="#1e293b"/>
            <line x1="30" y1="110" x2="430" y2="110" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Khối Park: vùng xanh, đường đi & mũi tên chạy xuyên qua giữa -->
            <rect x="115" y="66" width="115" height="88" rx="8" fill="#064e3b" stroke="#10b981" stroke-width="2" fill-opacity="0.9"/>
            <text x="172.5" y="85" font-size="11" font-weight="extrabold" fill="#a7f3d0" text-anchor="middle">🌳 Park</text>

            <!-- Khối Kirche: nằm sát mép đường phía trên, mũi tên đi ngang qua -->
            <rect x="250" y="26" width="90" height="46" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="295" y="54" font-size="10.5" font-weight="bold" fill="#bae6fd" text-anchor="middle">⛪ Kirche</text>

            <!-- Điểm đích: Bahnhof (ZIEL) ở cuối đường bên phải -->
            <rect x="360" y="82" width="85" height="56" rx="6" fill="#581c87" stroke="#c084fc" stroke-width="2"/>
            <text x="402.5" y="105" font-size="10" font-weight="bold" fill="#f5d0fe" text-anchor="middle">🚉 Bahnhof</text>
            <text x="402.5" y="122" font-size="10" font-weight="black" fill="#facc15" text-anchor="middle">(ZIEL)</text>

            <!-- Lộ trình mũi tên: xuất phát từ mép START, đi xuyên qua Park, đi ngang qua Kirche, kết thúc tại Bahnhof -->
            <path d="M 68 110 L 358 110" fill="none" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>
            <polygon points="358,110 346,104 346,116" fill="#0284c7"/>

            <!-- START: vòng tròn đỏ trên cùng, không bị che -->
            <circle cx="50" cy="110" r="16" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>
            <text x="50" y="114" font-size="8.5" font-weight="black" fill="#ffffff" text-anchor="middle">START</text>
        </svg>`;
    }

    // 12. map_build_2 (Câu 69: START -> über die Brücke -> Goethestraße entlang -> Post ZIEL)
    function getMapBuild2Svg() {
        return `
        <svg viewBox="0 0 460 220" width="100%" class="w-full max-w-lg mx-auto rounded-2xl shadow-sm border border-slate-300 bg-slate-900 overflow-hidden">
            <rect x="0" y="0" width="460" height="220" fill="#0f172a"/>

            <!-- Dòng sông (Fluss) nằm ngang -->
            <rect x="0" y="95" width="460" height="48" fill="#0369a1"/>
            <path d="M 0 110 Q 30 115 60 110 T 120 110 T 180 110 T 240 110 T 300 110 T 360 110 T 420 110 T 460 110" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.6"/>
            <path d="M 0 128 Q 30 133 60 128 T 120 128 T 180 128 T 240 128 T 300 128 T 360 128 T 420 128 T 460 128" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
            <text x="410" y="125" font-size="9" font-style="italic" fill="#bae6fd" text-anchor="middle">Fluss</text>

            <!-- Con đường dọc từ START đi lên -->
            <rect x="80" y="38" width="44" height="182" fill="#1e293b"/>
            <line x1="102" y1="145" x2="102" y2="220" stroke="#334155" stroke-width="2" stroke-dasharray="6 5"/>

            <!-- Khối cây cầu (Brücke) bắc ngang qua sông -->
            <rect x="74" y="93" width="56" height="52" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
            <line x1="80" y1="119" x2="124" y2="119" stroke="#64748b" stroke-width="2" stroke-dasharray="4 3"/>
            <text x="102" y="86" font-size="9.5" font-weight="extrabold" fill="#f8fafc" text-anchor="middle">🌉 Brücke</text>

            <!-- Con đường ngang Goethestraße sau khi qua cầu rẽ sang phải -->
            <rect x="80" y="18" width="276" height="44" fill="#1e293b"/>
            <line x1="124" y1="40" x2="355" y2="40" stroke="#475569" stroke-width="2" stroke-dasharray="6 5"/>
            <text x="220" y="33" font-size="9.5" font-weight="bold" fill="#cbd5e1" text-anchor="middle">Goethestraße</text>

            <!-- Điểm đích: Bưu điện Post (ZIEL) ở cuối đường Goethestraße -->
            <rect x="355" y="14" width="85" height="52" rx="6" fill="#854d0e" stroke="#facc15" stroke-width="2"/>
            <text x="397.5" y="36" font-size="10.5" font-weight="extrabold" fill="#fef9c3" text-anchor="middle">🏣 Post</text>
            <text x="397.5" y="52" font-size="10" font-weight="black" fill="#fde047" text-anchor="middle">(ZIEL)</text>

            <!-- Mũi tên lộ trình: đi từ START qua cầu (über die Brücke) rồi chạy dọc Goethestraße (entlang) đến Post -->
            <path d="M 102 178 L 102 40 L 354 40" fill="none" stroke="#10b981" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
            <polygon points="354,40 342,34 342,46" fill="#059669"/>

            <!-- START: ở dưới cùng của đường dọc, vẽ trên cùng hiển thị rõ ràng -->
            <circle cx="102" cy="195" r="16" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>
            <text x="102" y="199" font-size="8.5" font-weight="black" fill="#ffffff" text-anchor="middle">START</text>
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
        let badgeLabel = 'BẢN ĐỒ';
        let badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';

        switch (svgKey) {
            case 'map_route_finder_1':
                innerContent = getMapRouteFinder1Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';
                break;
            case 'map_route_line_2':
                innerContent = getMapRouteLine2Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';
                break;
            case 'quiz_spatial_3_steps':
                innerContent = getQuizSpatial3StepsSvg();
                badgeLabel = 'HÌNH MINH HỌA';
                badgeColor = 'bg-indigo-100 text-indigo-800 border-indigo-300';
                break;
            case 'map_route_line_3':
                innerContent = getMapRouteLine3Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';
                break;
            case 'map_error_check_1':
                innerContent = getMapErrorCheck1Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-amber-100 text-amber-800 border-amber-300';
                break;
            case 'map_fill_1':
                innerContent = getMapFill1Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-emerald-100 text-emerald-800 border-emerald-300';
                break;
            case 'map_fill_2':
                innerContent = getMapFill2Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-emerald-100 text-emerald-800 border-emerald-300';
                break;
            case 'quiz_icon_bridge':
                innerContent = getQuizIconBridgeSvg();
                badgeLabel = 'HÌNH MINH HỌA';
                badgeColor = 'bg-slate-100 text-slate-700 border-slate-300';
                break;
            case 'quiz_icon_gate':
                innerContent = getQuizIconGateSvg();
                badgeLabel = 'HÌNH MINH HỌA';
                badgeColor = 'bg-slate-100 text-slate-700 border-slate-300';
                break;
            case 'quiz_icon_along':
                innerContent = getQuizIconAlongSvg();
                badgeLabel = 'HÌNH MINH HỌA';
                badgeColor = 'bg-slate-100 text-slate-700 border-slate-300';
                break;
            case 'map_build_1':
                innerContent = getMapBuild1Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-indigo-100 text-indigo-800 border-indigo-300';
                break;
            case 'map_build_2':
                innerContent = getMapBuild2Svg();
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-purple-100 text-purple-800 border-purple-300';
                break;
            case 'city_grid_map_quiz_1':
                innerContent = getCityGridMapSvg('route1', 'quiz1');
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-blue-100 text-blue-800 border-blue-300';
                break;
            case 'city_grid_map_quiz_2':
                innerContent = getCityGridMapSvg('route2', 'quiz2');
                badgeLabel = 'BẢN ĐỒ';
                badgeColor = 'bg-emerald-100 text-emerald-800 border-emerald-300';
                break;
            default:
                if (svgKey.startsWith('direction_card_')) {
                    const cardCode = svgKey.replace('direction_card_', '');
                    innerContent = `<div class="flex justify-center my-3">${getCleanDirectionSvg(cardCode, 200, 140)}</div>`;
                    badgeLabel = 'HÌNH MINH HỌA';
                } else if (svgKey === 'spatial_diagram_vorbei') {
                    innerContent = `<div class="my-3">${getSpatialDiagramSvg('vorbei', 340, 180)}</div>`;
                    badgeLabel = 'HÌNH MINH HỌA';
                    badgeColor = 'bg-indigo-100 text-indigo-800 border-indigo-300';
                } else if (svgKey === 'spatial_contrast_tor_bruecke') {
                    innerContent = `<div class="my-3">${getSpatialContrastSvg()}</div>`;
                    badgeLabel = 'HÌNH MINH HỌA';
                    badgeColor = 'bg-purple-100 text-purple-800 border-purple-300';
                } else {
                    return '';
                }
        }

        return `
        <div class="my-3 p-4 rounded-2xl bg-white border border-slate-200 shadow-xs">
            <div class="flex items-center justify-between mb-2">
                <span class="px-2.5 py-0.5 rounded-full text-xs font-extrabold border ${badgeColor}">
                    ${badgeLabel}
                </span>
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
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur nächsten Kreuzung und dort links. Danach gehen Sie rechts und die Straße Unter den Linden entlang bis zur Ampel. Die Post sehen Sie dann direkt vor sich.', 1.0)" class="px-3 py-1 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus. <b>Dann</b> gehen Sie die erste Straße rechts, <b>an der Bank vorbei</b>. <b>Dann</b> gehen Sie bis zur nächsten Kreuzung und dort links. <b>Danach</b> gehen Sie rechts und die Straße Unter den Linden entlang <b>bis zur Ampel</b>. <b>Die Post</b> sehen Sie dann <b>direkt vor sich</b>.“</p>
                        <p class="text-xs text-blue-800 font-medium"><b>Dịch nghĩa:</b> Đầu tiên Ngài đi thẳng. Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. Sau đó Ngài đi đến ngã tư tiếp theo và rẽ trái ở đó. Tiếp theo Ngài rẽ phải và đi dọc theo đường Unter den Linden cho đến đèn giao thông. Ngài sẽ thấy bưu điện ngay phía trước.</p>
                    </div>`;
            } else if (route === 'route2') {
                descWrap.innerHTML = `
                    <div class="p-4 rounded-2xl bg-emerald-50 border border-emerald-200 space-y-2 text-xs sm:text-sm text-emerald-950">
                        <div class="flex items-center justify-between">
                            <span class="font-extrabold text-emerald-800">🟢 Lộ trình 2: Đi thẳng lên ngã tư thứ 2 rồi rẽ phải</span>
                            <button onclick="speakGerman('Zuerst gehen Sie geradeaus, bis zur zweiten Kreuzung rechts. Dann gehen Sie geradeaus, über die Kreuzung, bis zur Ampel. Links sehen Sie die Post.', 1.0)" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs cursor-pointer flex items-center gap-1">
                                🔊 Nghe phát âm chuẩn de-DE
                            </button>
                        </div>
                        <p class="italic font-serif">„<b>Zuerst</b> gehen Sie geradeaus, <b>bis zur zweiten Kreuzung rechts</b>. <b>Dann</b> gehen Sie geradeaus, <b>über die Kreuzung</b>, <b>bis zur Ampel</b>. Links sehen Sie <b>die Post</b>.“</p>
                        <p class="text-xs text-emerald-800 font-medium"><b>Dịch nghĩa:</b> Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư, cho đến đèn giao thông. Ở bên trái Ngài sẽ nhìn thấy bưu điện.</p>
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
            ex.question = `Câu ${fallbackIndex || 27} [Chia Modalverb wollen]: Điền dạng chia đúng của 'wollen' vào chỗ trống: '${pick.subj} ___ heute ${pick.cityAct}.'`;
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
        if (vorbeiEl && !vorbeiEl.querySelector('svg')) {
            vorbeiEl.innerHTML = getSpatialDiagramSvg('vorbei', '100%', 150);
        }
        const durchEl = document.getElementById('svg-diag-durch');
        if (durchEl && !durchEl.querySelector('svg')) {
            durchEl.innerHTML = getSpatialDiagramSvg('durch', '100%', 150);
        }
        const ueberEl = document.getElementById('svg-diag-ueber');
        if (ueberEl && !ueberEl.querySelector('svg')) {
            ueberEl.innerHTML = getSpatialDiagramSvg('ueber', '100%', 150);
        }
        const entlangEl = document.getElementById('svg-diag-entlang');
        if (entlangEl && !entlangEl.querySelector('svg')) {
            entlangEl.innerHTML = getSpatialDiagramSvg('entlang', '100%', 150);
        }
        const mapEl = document.getElementById('b8-interactive-city-map-container');
        if (mapEl && !mapEl.querySelector('svg')) {
            mapEl.innerHTML = getCityGridMapSvg('route1');
        }
        const contrastEl = document.getElementById('svg-spatial-contrast');
        if (contrastEl && !contrastEl.querySelector('svg')) {
            contrastEl.innerHTML = getSpatialContrastSvg();
        }
        const cardsGridEl = document.getElementById('b8-direction-cards-grid');
        if (cardsGridEl && !cardsGridEl.querySelector('.grid')) {
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
        window.getMapRouteFinder1Svg = getMapRouteFinder1Svg;
        window.getMapRouteLine2Svg = getMapRouteLine2Svg;
        window.getQuizSpatial3StepsSvg = getQuizSpatial3StepsSvg;
        window.getMapRouteLine3Svg = getMapRouteLine3Svg;
        window.getMapErrorCheck1Svg = getMapErrorCheck1Svg;
        window.getMapFill1Svg = getMapFill1Svg;
        window.getMapFill2Svg = getMapFill2Svg;
        window.getQuizIconBridgeSvg = getQuizIconBridgeSvg;
        window.getQuizIconGateSvg = getQuizIconGateSvg;
        window.getQuizIconAlongSvg = getQuizIconAlongSvg;
        window.getMapBuild1Svg = getMapBuild1Svg;
        window.getMapBuild2Svg = getMapBuild2Svg;
        window.getCleanDirectionSvg = getCleanDirectionSvg;
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
