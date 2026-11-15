/**
 * DeutschMeister - Module Sơ Đồ Trực Quan & Tương Tác Essen & Trinken SVG (Essen SVG Engine)
 * Dành riêng cho Bài 10 (A1): "Essen und Trinken - Thực phẩm, So sánh hơn / So sánh nhất, Fragewort: Welch-"
 * 
 * Cung cấp 6 sơ đồ trực quan theo đặc tả kỹ thuật sư phạm chuẩn CEFR A1:
 * V1: Bảng đuôi Welch- tương tác (Nominativ vs Akkusativ theo 3 giống & số nhiều)
 * V2: Lưu đồ chọn dạng Welch- chuẩn xác (Lưu đồ rẽ nhánh)
 * V3: Bậc thang so sánh 3 bậc (Positiv -> Komparativ -> Superlativ)
 * V4: Khung câu vị trí 1-2-3 khi đảo ngữ với Am liebsten / Am meisten / Am besten
 * V5: Quầy chợ tương tác - hội thoại mua sắm và hỏi giá
 * V6: Máy đọc giá tiền Euro bằng tiếng Đức chuẩn hóa
 */

(function (global) {
    'use strict';

    // =========================================================================
    // DỮ LIỆU NGUỒN CHUẨN (Single Source of Truth)
    // =========================================================================
    const ONES = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",
                  "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"];
    const TENS = { 20: "zwanzig", 30: "dreißig", 40: "vierzig", 50: "fünfzig", 60: "sechzig", 70: "siebzig", 80: "achtzig", 90: "neunzig" };

    function numWords(n) {
        if (n < 20) return ONES[n];
        const t = Math.floor(n / 10) * 10;
        const u = n % 10;
        return u === 0 ? TENS[t] : (ONES[u] + "und" + TENS[t]);
    }

    function priceToGermanCents(cents) {
        cents = parseInt(cents, 10) || 0;
        const euros = Math.floor(cents / 100);
        const c = cents % 100;
        if (euros === 0) {
            return numWords(c) + " Cent";
        }
        if (c === 0) {
            return numWords(euros) + " Euro";
        }
        return numWords(euros) + " Euro " + numWords(c);
    }

    const WELCH_NOUNS = [
        { label: "der Käse (phô mai)", gender: "m", art: "der", nom: "welcher", akk: "welchen", exNom: "Welcher Käse ist lecker?", exAkk: "Welchen Käse möchten Sie?", trNom: "Loại phô mai nào ngon?", trAkk: "Ngài muốn loại phô mai nào?" },
        { label: "die Dose (lon cô-ca)", gender: "f", art: "die", nom: "welche", akk: "welche", exNom: "Welche Dose Cola ist billig?", exAkk: "Welche Dose Cola nimmst du?", trNom: "Lon cô-ca nào rẻ?", trAkk: "Bạn lấy lon cô-ca nào?" },
        { label: "das Buch (quyển sách)", gender: "n", art: "das", nom: "welches", akk: "welches", exNom: "Welches Buch ist neu?", exAkk: "Welches Buch möchten Sie lesen?", trNom: "Quyển sách nào mới?", trAkk: "Ngài muốn đọc quyển sách nào?" },
        { label: "das Brot (bánh mì)", gender: "n", art: "das", nom: "welches", akk: "welches", exNom: "Welches Brot schmeckt am besten?", exAkk: "Welches Brot kaufst du?", trNom: "Loại bánh mì nào ngon nhất?", trAkk: "Bạn mua loại bánh mì nào?" },
        { label: "die Bananen (chuối, PL)", gender: "pl", art: "die", nom: "welche", akk: "welche", exNom: "Welche Bananen sind reif?", exAkk: "Welche Bananen nehmen wir?", trNom: "Những quả chuối nào đã chín?", trAkk: "Chúng ta lấy những quả chuối nào?" },
        { label: "der Reis (gạo, cơm)", gender: "m", art: "der", nom: "welcher", akk: "welchen", exNom: "Welcher Reis schmeckt gut?", exAkk: "Welchen Reis kaufst du?", trNom: "Loại gạo nào ngon?", trAkk: "Bạn mua loại gạo nào?" }
    ];

    const ADJECTIVES_25 = [
        { pos: "billig", comp: "billiger", sup: "am billigsten", rulePos: "Nghĩa: rẻ", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "am + gốc + -sten (am billigsten)" },
        { pos: "teuer", comp: "teurer", sup: "am teuersten", rulePos: "Nghĩa: đắt • Lưu ý: bỏ -e- ở Komparativ", ruleComp: "Lược -e- ở gốc + -er (teurer)", ruleSup: "am + gốc + -sten (am teuersten)" },
        { pos: "lecker", comp: "leckerer", sup: "am leckersten", rulePos: "Nghĩa: ngon", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "am + gốc + -sten (am leckersten)" },
        { pos: "frisch", comp: "frischer", sup: "am frischesten", rulePos: "Nghĩa: tươi", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "Đuôi -sch -> thêm -esten (am frischesten)" },
        { pos: "süß", comp: "süßer", sup: "am süßesten", rulePos: "Nghĩa: ngọt", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "Đuôi -ß -> thêm -esten (am süßesten)" },
        { pos: "sauer", comp: "saurer", sup: "am sauersten", rulePos: "Nghĩa: chua • Lưu ý: bỏ -e- ở Komparativ", ruleComp: "Lược -e- ở gốc + -er (saurer)", ruleSup: "am + gốc + -sten (am sauersten)" },
        { pos: "scharf", comp: "schärfer", sup: "am schärfsten", rulePos: "Nghĩa: cay", ruleComp: "Thêm Umlaut a -> ä + -er", ruleSup: "Thêm Umlaut a -> ä + -sten (am schärfsten)" },
        { pos: "gesund", comp: "gesünder", sup: "am gesündesten", rulePos: "Nghĩa: tốt cho sức khỏe", ruleComp: "Thêm Umlaut u -> ü + -er", ruleSup: "Thêm Umlaut u -> ü + -esten (am gesündesten)" },
        { pos: "groß", comp: "größer", sup: "am größten", rulePos: "Nghĩa: to, lớn", ruleComp: "Đổi o -> ö + -er (größer)", ruleSup: "Ngoại lệ đuôi -ß chỉ thêm -ten (am größten)" },
        { pos: "klein", comp: "kleiner", sup: "am kleinsten", rulePos: "Nghĩa: nhỏ", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "am + gốc + -sten (am kleinsten)" },
        { pos: "alt", comp: "älter", sup: "am ältesten", rulePos: "Nghĩa: cũ, già", ruleComp: "Thêm Umlaut a -> ä + -er", ruleSup: "Thêm Umlaut a -> ä + -esten (am ältesten)" },
        { pos: "jung", comp: "jünger", sup: "am jüngsten", rulePos: "Nghĩa: trẻ", ruleComp: "Thêm Umlaut u -> ü + -er", ruleSup: "Thêm Umlaut u -> ü + -sten (am jüngsten)" },
        { pos: "kalt", comp: "kälter", sup: "am kältesten", rulePos: "Nghĩa: lạnh", ruleComp: "Thêm Umlaut a -> ä + -er", ruleSup: "Thêm Umlaut a -> ä + -esten (am kältesten)" },
        { pos: "warm", comp: "wärmer", sup: "am wärmsten", rulePos: "Nghĩa: ấm", ruleComp: "Thêm Umlaut a -> ä + -er", ruleSup: "Thêm Umlaut a -> ä + -sten (am wärmsten)" },
        { pos: "heiß", comp: "heißer", sup: "am heißesten", rulePos: "Nghĩa: nóng", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "Đuôi -ß -> thêm -esten (am heißesten)" },
        { pos: "hoch", comp: "höher", sup: "am höchsten", rulePos: "Nghĩa: cao", ruleComp: "Đổi o -> ö và lược chữ 'c' (höher)", ruleSup: "Đổi o -> ö + -sten (am höchsten)" },
        { pos: "nah", comp: "näher", sup: "am nächsten", rulePos: "Nghĩa: gần", ruleComp: "Đổi a -> ä + -er (näher)", ruleSup: "Đổi a -> ä và thêm -ch- (am nächsten)" },
        { pos: "schwer", comp: "schwerer", sup: "am schwersten", rulePos: "Nghĩa: nặng; khó", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "am + gốc + -sten (am schwersten)" },
        { pos: "leicht", comp: "leichter", sup: "am leichtesten", rulePos: "Nghĩa: nhẹ; dễ", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "Đuôi -t -> thêm -esten (am leichtesten)" },
        { pos: "lang", comp: "länger", sup: "am längsten", rulePos: "Nghĩa: dài", ruleComp: "Thêm Umlaut a -> ä + -er", ruleSup: "Thêm Umlaut a -> ä + -sten (am längsten)" },
        { pos: "kurz", comp: "kürzer", sup: "am kürzesten", rulePos: "Nghĩa: ngắn", ruleComp: "Thêm Umlaut u -> ü + -er", ruleSup: "Thêm Umlaut u -> ü + -esten (am kürzesten)" },
        { pos: "gut", comp: "besser", sup: "am besten", rulePos: "Nghĩa: tốt, ngon", ruleComp: "Bất quy tắc hoàn toàn (không dùng *guter)", ruleSup: "Bất quy tắc hoàn toàn (am besten)" },
        { pos: "viel", comp: "mehr", sup: "am meisten", rulePos: "Nghĩa: nhiều", ruleComp: "Bất quy tắc hoàn toàn (không đổi đuôi)", ruleSup: "Bất quy tắc hoàn toàn (am meisten)" },
        { pos: "gern", comp: "lieber", sup: "am liebsten", rulePos: "Nghĩa: thích", ruleComp: "Bất quy tắc hoàn toàn (thích ... hơn)", ruleSup: "Bất quy tắc hoàn toàn (thích ... nhất)" },
        { pos: "wenig", comp: "weniger", sup: "am wenigsten", rulePos: "Nghĩa: ít", ruleComp: "Gốc tính từ + -er (không biến âm)", ruleSup: "am + gốc + -sten (am wenigsten)" }
    ];

    let currentSelectedNounIdx = 0;
    let currentSelectedAdjIdx = 0;
    let isSentenceInverted = true; // true: Am liebsten esse ich Nudeln; false: Ich esse am liebsten Nudeln

    // =========================================================================
    // V1: BẢNG ĐUÔI WELCH- TƯƠNG TÁC
    // =========================================================================
    function renderWelchTableSvg() {
        const container = document.getElementById('svg-v1-container');
        if (!container) return;

        const noun = WELCH_NOUNS[currentSelectedNounIdx];

        container.innerHTML = `
            <div class="p-5 rounded-3xl bg-slate-900 border border-slate-800 text-white shadow-xl space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-400 font-bold flex items-center justify-center text-xs">V1</span>
                        <span class="font-black text-sm text-white">Sơ đồ V1: Bảng Đuôi Welch- Tương Tác Theo Giống & Cách</span>
                    </div>
                    <span class="text-[11px] text-amber-400 font-semibold bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">
                        ⚡ Duy nhất giống ĐỰC biến đổi giữa Nominativ & Akkusativ
                    </span>
                </div>

                <!-- Bộ chọn danh từ mẫu -->
                <div class="flex items-center gap-2 flex-wrap text-xs">
                    <span class="text-slate-400 font-semibold">Chọn danh từ thử nghiệm:</span>
                    <div class="flex gap-1.5 flex-wrap">
                        ${WELCH_NOUNS.map((n, idx) => `
                            <button onclick="window.selectWelchNoun(${idx})" class="px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${idx === currentSelectedNounIdx ? 'bg-blue-600 text-white shadow-md' : 'bg-slate-800 hover:bg-slate-700 text-slate-300'}">
                                ${n.label}
                            </button>
                        `).join('')}
                    </div>
                </div>

                <!-- Bảng SVG Trực quan -->
                <div class="overflow-x-auto">
                    <svg viewBox="0 0 760 270" class="w-full max-w-3xl mx-auto block font-sans select-none">
                        <!-- Header -->
                        <rect x="10" y="10" width="180" height="42" rx="8" fill="#1e293b" stroke="#334155" />
                        <text x="100" y="36" fill="#94a3b8" font-size="13" font-weight="bold" text-anchor="middle">Giống & Số</text>

                        <rect x="200" y="10" width="270" height="42" rx="8" fill="#1e293b" stroke="#334155" />
                        <text x="335" y="36" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">Nominativ (Chủ ngữ)</text>

                        <rect x="480" y="10" width="270" height="42" rx="8" fill="#1e293b" stroke="#334155" />
                        <text x="615" y="36" fill="#f43f5e" font-size="13" font-weight="bold" text-anchor="middle">Akkusativ (Tân ngữ)</text>

                        <!-- Row 1: Maskulinum (der) -->
                        <g class="transition-all duration-300">
                            <rect x="10" y="60" width="180" height="48" rx="8" fill="${noun.gender === 'm' ? '#1e3a8a' : '#0f172a'}" stroke="${noun.gender === 'm' ? '#3b82f6' : '#1e293b'}" stroke-width="${noun.gender === 'm' ? '2' : '1'}" />
                            <text x="100" y="89" fill="${noun.gender === 'm' ? '#60a5fa' : '#cbd5e1'}" font-size="13" font-weight="bold" text-anchor="middle">🔵 Maskulinum (der)</text>

                            <rect x="200" y="60" width="270" height="48" rx="8" fill="${noun.gender === 'm' ? '#1d4ed8' : '#1e293b'}" stroke="${noun.gender === 'm' ? '#60a5fa' : '#334155'}" stroke-width="${noun.gender === 'm' ? '2' : '1'}" />
                            <text x="335" y="89" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#fde047" font-weight="900">er</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(der)</tspan></text>

                            <rect x="480" y="60" width="270" height="48" rx="8" fill="${noun.gender === 'm' ? '#b91c1c' : '#1e293b'}" stroke="${noun.gender === 'm' ? '#f87171' : '#334155'}" stroke-width="${noun.gender === 'm' ? '2' : '1'}" />
                            <text x="615" y="89" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#4ade80" font-weight="900">en</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(den)</tspan></text>
                        </g>

                        <!-- Row 2: Femininum (die) -->
                        <g class="transition-all duration-300">
                            <rect x="10" y="114" width="180" height="48" rx="8" fill="${noun.gender === 'f' ? '#831843' : '#0f172a'}" stroke="${noun.gender === 'f' ? '#ec4899' : '#1e293b'}" stroke-width="${noun.gender === 'f' ? '2' : '1'}" />
                            <text x="100" y="143" fill="${noun.gender === 'f' ? '#f472b6' : '#cbd5e1'}" font-size="13" font-weight="bold" text-anchor="middle">🔴 Femininum (die)</text>

                            <rect x="200" y="114" width="270" height="48" rx="8" fill="${noun.gender === 'f' ? '#9d174d' : '#1e293b'}" stroke="${noun.gender === 'f' ? '#f472b6' : '#334155'}" stroke-width="${noun.gender === 'f' ? '2' : '1'}" />
                            <text x="335" y="143" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#f472b6" font-weight="900">e</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(die)</tspan></text>

                            <rect x="480" y="114" width="270" height="48" rx="8" fill="${noun.gender === 'f' ? '#9d174d' : '#1e293b'}" stroke="${noun.gender === 'f' ? '#f472b6' : '#334155'}" stroke-width="${noun.gender === 'f' ? '2' : '1'}" />
                            <text x="615" y="143" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#f472b6" font-weight="900">e</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(die)</tspan></text>
                        </g>

                        <!-- Row 3: Neutrum (das) -->
                        <g class="transition-all duration-300">
                            <rect x="10" y="168" width="180" height="48" rx="8" fill="${noun.gender === 'n' ? '#064e3b' : '#0f172a'}" stroke="${noun.gender === 'n' ? '#10b981' : '#1e293b'}" stroke-width="${noun.gender === 'n' ? '2' : '1'}" />
                            <text x="100" y="197" fill="${noun.gender === 'n' ? '#34d399' : '#cbd5e1'}" font-size="13" font-weight="bold" text-anchor="middle">🟢 Neutrum (das)</text>

                            <rect x="200" y="168" width="270" height="48" rx="8" fill="${noun.gender === 'n' ? '#047857' : '#1e293b'}" stroke="${noun.gender === 'n' ? '#34d399' : '#334155'}" stroke-width="${noun.gender === 'n' ? '2' : '1'}" />
                            <text x="335" y="197" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#34d399" font-weight="900">es</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(das)</tspan></text>

                            <rect x="480" y="168" width="270" height="48" rx="8" fill="${noun.gender === 'n' ? '#047857' : '#1e293b'}" stroke="${noun.gender === 'n' ? '#34d399' : '#334155'}" stroke-width="${noun.gender === 'n' ? '2' : '1'}" />
                            <text x="615" y="197" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#34d399" font-weight="900">es</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(das)</tspan></text>
                        </g>

                        <!-- Row 4: Plural (die) -->
                        <g class="transition-all duration-300">
                            <rect x="10" y="222" width="180" height="44" rx="8" fill="${noun.gender === 'pl' ? '#4c1d95' : '#0f172a'}" stroke="${noun.gender === 'pl' ? '#8b5cf6' : '#1e293b'}" stroke-width="${noun.gender === 'pl' ? '2' : '1'}" />
                            <text x="100" y="249" fill="${noun.gender === 'pl' ? '#c4b5fd' : '#cbd5e1'}" font-size="13" font-weight="bold" text-anchor="middle">🟣 Plural (die)</text>

                            <rect x="200" y="222" width="270" height="44" rx="8" fill="${noun.gender === 'pl' ? '#6d28d9' : '#1e293b'}" stroke="${noun.gender === 'pl' ? '#c4b5fd' : '#334155'}" stroke-width="${noun.gender === 'pl' ? '2' : '1'}" />
                            <text x="335" y="249" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#c084fc" font-weight="900">e</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(die)</tspan></text>

                            <rect x="480" y="222" width="270" height="44" rx="8" fill="${noun.gender === 'pl' ? '#6d28d9' : '#1e293b'}" stroke="${noun.gender === 'pl' ? '#c4b5fd' : '#334155'}" stroke-width="${noun.gender === 'pl' ? '2' : '1'}" />
                            <text x="615" y="249" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">Welch<tspan fill="#c084fc" font-weight="900">e</tspan> <tspan fill="#94a3b8" font-size="12" font-weight="bold">(die)</tspan></text>
                        </g>
                    </svg>
                </div>

                <!-- Thẻ ví dụ động -->
                <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-2 text-xs">
                    <div class="text-slate-400 font-semibold">Ví dụ thực tế với <b class="text-white">${noun.label}</b>:</div>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700 flex items-center justify-between gap-2">
                            <div>
                                <span class="text-sky-400 font-bold block">1. Nominativ (Chủ ngữ):</span>
                                <span class="text-white font-medium">„${noun.exNom}“</span>
                                <span class="text-slate-400 text-[11px] block italic">${noun.trNom}</span>
                            </div>
                            <button onclick="speakGerman('${noun.exNom.replace(/'/g, "\\'")}', 1.0)" class="p-2 rounded-lg bg-sky-500/20 text-sky-300 hover:bg-sky-500/30 transition cursor-pointer shrink-0">🔊</button>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-900 border border-slate-700 flex items-center justify-between gap-2">
                            <div>
                                <span class="text-rose-400 font-bold block">2. Akkusativ (Tân ngữ):</span>
                                <span class="text-white font-medium">„${noun.exAkk}“</span>
                                <span class="text-slate-400 text-[11px] block italic">${noun.trAkk}</span>
                            </div>
                            <button onclick="speakGerman('${noun.exAkk.replace(/'/g, "\\'")}', 1.0)" class="p-2 rounded-lg bg-rose-500/20 text-rose-300 hover:bg-rose-500/30 transition cursor-pointer shrink-0">🔊</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    function selectWelchNoun(idx) {
        currentSelectedNounIdx = idx;
        renderWelchTableSvg();
    }

    // =========================================================================
    // V2: LƯU ĐỒ CHỌN DẠNG WELCH-
    // =========================================================================
    function renderWelchFlowchartSvg() {
        const container = document.getElementById('svg-v2-container');
        if (!container) return;

        container.innerHTML = `
            <div class="p-5 rounded-3xl bg-slate-900 border border-slate-800 text-white shadow-xl space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-emerald-500/20 text-emerald-400 font-bold flex items-center justify-center text-xs">V2</span>
                        <span class="font-black text-sm text-white">Sơ đồ V2: Lưu Đồ Chọn Dạng Welch- Siêu Tốc</span>
                    </div>
                    <span class="text-xs text-slate-400">Chỉ 2 bước xác định 100% đáp án đúng</span>
                </div>

                <div class="overflow-x-auto">
                    <svg viewBox="0 0 760 300" class="w-full max-w-3xl mx-auto block font-sans select-none">
                        <!-- Bước 1 -->
                        <rect x="250" y="10" width="260" height="46" rx="12" fill="#0f766e" stroke="#14b8a6" stroke-width="2" />
                        <text x="380" y="38" fill="#ffffff" font-size="14" font-weight="black" text-anchor="middle">Bước 1: Giống của danh từ là gì?</text>

                        <!-- Mũi tên 4 nhánh -->
                        <path d="M 270 56 L 100 100" stroke="#64748b" stroke-width="2" fill="none" marker-end="url(#arrow)" />
                        <path d="M 340 56 L 270 100" stroke="#64748b" stroke-width="2" fill="none" />
                        <path d="M 420 56 L 470 100" stroke="#64748b" stroke-width="2" fill="none" />
                        <path d="M 490 56 L 650 100" stroke="#38bdf8" stroke-width="2.5" fill="none" />

                        <!-- Nhánh 1: die (f) -->
                        <rect x="20" y="100" width="160" height="50" rx="10" fill="#831843" stroke="#f472b6" />
                        <text x="100" y="122" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Giống Cái (die)</text>
                        <text x="100" y="140" fill="#fbcfe8" font-size="12" font-weight="black" text-anchor="middle">→ Welche</text>

                        <!-- Nhánh 2: das (n) -->
                        <rect x="195" y="100" width="160" height="50" rx="10" fill="#064e3b" stroke="#34d399" />
                        <text x="275" y="122" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Giống Trung (das)</text>
                        <text x="275" y="140" fill="#a7f3d0" font-size="12" font-weight="black" text-anchor="middle">→ Welches</text>

                        <!-- Nhánh 3: Plural -->
                        <rect x="370" y="100" width="160" height="50" rx="10" fill="#4c1d95" stroke="#c4b5fd" />
                        <text x="450" y="122" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Số Nhiều (PL)</text>
                        <text x="450" y="140" fill="#ddd6fe" font-size="12" font-weight="black" text-anchor="middle">→ Welche</text>

                        <!-- Nhánh 4: der (m) -> Rẽ nhánh bước 2 -->
                        <rect x="545" y="100" width="205" height="56" rx="10" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2" />
                        <text x="647" y="124" fill="#ffffff" font-size="12" font-weight="black" text-anchor="middle">Giống Đực (der) ⚠️</text>
                        <text x="647" y="142" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">Bước 2: Chủ ngữ hay Tân ngữ?</text>

                        <!-- 2 nhánh của der -->
                        <path d="M 605 156 L 532 210" stroke="#38bdf8" stroke-width="2" fill="none" />
                        <path d="M 685 156 L 677 210" stroke="#f43f5e" stroke-width="2" fill="none" />

                        <!-- Nominativ -->
                        <rect x="465" y="210" width="135" height="65" rx="10" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
                        <text x="532" y="231" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Chủ ngữ (Nominativ)</text>
                        <text x="532" y="250" fill="#ffffff" font-size="14" font-weight="black" text-anchor="middle">Welcher</text>
                        <text x="532" y="266" fill="#94a3b8" font-size="9.5" text-anchor="middle">(Welcher Fisch ist frisch?)</text>

                        <!-- Akkusativ -->
                        <rect x="610" y="210" width="135" height="65" rx="10" fill="#1e293b" stroke="#f43f5e" stroke-width="2" />
                        <text x="677" y="231" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">Tân ngữ (Akkusativ)</text>
                        <text x="677" y="250" fill="#ffffff" font-size="14" font-weight="black" text-anchor="middle">Welchen</text>
                        <text x="677" y="266" fill="#94a3b8" font-size="9.5" text-anchor="middle">(Welchen Fisch nimmst du?)</text>
                    </svg>
                </div>
            </div>
        `;
    }

    // =========================================================================
    // V3: BẬC THANG SO SÁNH 3 BẬC (STEIGERUNG)
    // =========================================================================
    function renderSteigerungStaircaseSvg() {
        const container = document.getElementById('svg-v3-container');
        if (!container) return;

        const adj = ADJECTIVES_25[currentSelectedAdjIdx];

        container.innerHTML = `
            <div class="p-5 rounded-3xl bg-slate-900 border border-slate-800 text-white shadow-xl space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-amber-500/20 text-amber-400 font-bold flex items-center justify-center text-xs">V3</span>
                        <span class="font-black text-sm text-white">Sơ đồ V3: Bậc Thang So Sánh (Positiv → Komparativ → Superlativ)</span>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <button onclick="window.prevSteigerungAdj()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300 cursor-pointer">◀</button>
                        <span class="text-xs font-mono text-amber-300 font-bold px-2">${currentSelectedAdjIdx + 1} / 25</span>
                        <button onclick="window.nextSteigerungAdj()" class="px-2 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300 cursor-pointer">▶</button>
                    </div>
                </div>

                <!-- 3 Bậc thang SVG -->
                <div class="overflow-x-auto">
                    <svg viewBox="0 0 760 220" class="w-full max-w-3xl mx-auto block font-sans select-none">
                        <!-- Bậc 1: Positiv -->
                        <g>
                            <rect x="20" y="130" width="220" height="80" rx="12" fill="#1e293b" stroke="#475569" stroke-width="2" />
                            <text x="130" y="156" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">BẬC 1: POSITIV</text>
                            <text x="130" y="186" fill="#ffffff" font-size="18" font-weight="black" text-anchor="middle">${adj.pos}</text>
                            <text x="130" y="202" fill="#cbd5e1" font-size="10" text-anchor="middle">${adj.rulePos}</text>
                        </g>

                        <!-- Mũi tên lên bậc 2 -->
                        <path d="M 245 150 L 275 125" stroke="#f59e0b" stroke-width="2.5" fill="none" />

                        <!-- Bậc 2: Komparativ -->
                        <g>
                            <rect x="270" y="75" width="220" height="135" rx="12" fill="#1e3a8a" stroke="#3b82f6" stroke-width="2" />
                            <text x="380" y="105" fill="#93c5fd" font-size="12" font-weight="bold" text-anchor="middle">BẬC 2: KOMPARATIV</text>
                            <text x="380" y="140" fill="#facc15" font-size="20" font-weight="900" text-anchor="middle">${adj.comp}</text>
                            <text x="380" y="165" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">hơn … (+ als)</text>
                            <text x="380" y="195" fill="#bfdbfe" font-size="10" text-anchor="middle">${adj.ruleComp}</text>
                        </g>

                        <!-- Mũi tên lên bậc 3 -->
                        <path d="M 495 100 L 525 70" stroke="#ef4444" stroke-width="2.5" fill="none" />

                        <!-- Bậc 3: Superlativ -->
                        <g>
                            <rect x="520" y="15" width="220" height="195" rx="12" fill="#831843" stroke="#f43f5e" stroke-width="2" />
                            <text x="630" y="45" fill="#fbcfe8" font-size="12" font-weight="bold" text-anchor="middle">BẬC 3: SUPERLATIV</text>
                            <text x="630" y="85" fill="#ffffff" font-size="22" font-weight="black" text-anchor="middle">${adj.sup}</text>
                            <text x="630" y="115" fill="#facc15" font-size="13" font-weight="bold" text-anchor="middle">… NHẤT</text>
                            <text x="630" y="145" fill="#fed7aa" font-size="10" text-anchor="middle">${adj.ruleSup}</text>
                        </g>
                    </svg>
                </div>

                <div class="flex items-center justify-between flex-wrap gap-2 text-xs bg-slate-800/60 p-3 rounded-2xl border border-slate-700">
                    <span class="text-slate-300">Tính từ đang hiển thị: <b class="text-amber-300">${adj.pos}</b> → <b class="text-blue-300">${adj.comp}</b> → <b class="text-rose-300">${adj.sup}</b></span>
                    <button onclick="speakGerman('${adj.pos}, ${adj.comp}, ${adj.sup}', 0.85)" class="px-3 py-1.5 rounded-xl bg-amber-500/20 text-amber-300 hover:bg-amber-500/30 font-bold transition flex items-center gap-1 cursor-pointer">
                        🔊 Nghe 3 bậc phát âm
                    </button>
                </div>
            </div>
        `;
    }

    function nextSteigerungAdj() {
        currentSelectedAdjIdx = (currentSelectedAdjIdx + 1) % ADJECTIVES_25.length;
        renderSteigerungStaircaseSvg();
    }

    function prevSteigerungAdj() {
        currentSelectedAdjIdx = (currentSelectedAdjIdx - 1 + ADJECTIVES_25.length) % ADJECTIVES_25.length;
        renderSteigerungStaircaseSvg();
    }

    // =========================================================================
    // V4: KHUNG CÂU VỊ TRÍ 1-2-3 (AM LIEBSTEN ESSE ICH NUDELN)
    // =========================================================================
    function renderSentenceOrderSvg() {
        const container = document.getElementById('svg-v4-container');
        if (!container) return;

        const sentenceText = isSentenceInverted 
            ? "Am liebsten esse ich Nudeln." 
            : "Ich esse am liebsten Nudeln.";
        const translationText = isSentenceInverted
            ? "Tôi thích ăn mì nhất. (Đảo ngữ: Cụm so sánh nhất ở vị trí ①, Động từ ở vị trí ②)"
            : "Tôi thích ăn mì nhất. (Câu xuôi: Chủ ngữ ở vị trí ①, Động từ ở vị trí ②)";

        container.innerHTML = `
            <div class="p-5 rounded-3xl bg-slate-900 border border-slate-800 text-white shadow-xl space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-rose-500/20 text-rose-400 font-bold flex items-center justify-center text-xs">V4</span>
                        <span class="font-black text-sm text-white">Sơ đồ V4: Quy Tắc Vàng Vị Trí Động Từ 1-2-3 (Đảo Ngữ)</span>
                    </div>
                    <button onclick="window.toggleSentenceOrder()" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition shadow-sm cursor-pointer flex items-center gap-1.5">
                        🔄 Đổi kiểu: ${isSentenceInverted ? 'Chuyển sang Câu Xuôi' : 'Chuyển sang Đảo Ngữ'}
                    </button>
                </div>

                <!-- 4 Khối vị trí SVG -->
                <div class="overflow-x-auto">
                    <svg viewBox="0 0 760 130" class="w-full max-w-3xl mx-auto block font-sans select-none">
                        ${isSentenceInverted ? `
                            <!-- Khối 1: Am liebsten (vị trí 1) -->
                            <rect x="20" y="20" width="180" height="90" rx="12" fill="#1d4ed8" stroke="#60a5fa" stroke-width="2" />
                            <text x="110" y="45" fill="#bfdbfe" font-size="11" font-weight="bold" text-anchor="middle">VỊ TRÍ ①</text>
                            <text x="110" y="78" fill="#ffffff" font-size="17" font-weight="900" text-anchor="middle">Am liebsten</text>
                            <text x="110" y="96" fill="#93c5fd" font-size="10" text-anchor="middle">(Cụm so sánh nhất)</text>

                            <!-- Khối 2: esse (vị trí 2) -->
                            <rect x="210" y="20" width="160" height="90" rx="12" fill="#b91c1c" stroke="#f87171" stroke-width="2.5" />
                            <text x="290" y="45" fill="#fecaca" font-size="11" font-weight="bold" text-anchor="middle">VỊ TRÍ ② (BẮT BUỘC)</text>
                            <text x="290" y="78" fill="#fef08a" font-size="20" font-weight="900" text-anchor="middle">esse</text>
                            <text x="290" y="96" fill="#fca5a5" font-size="10" text-anchor="middle">(Động từ chia)</text>

                            <!-- Khối 3: ich (vị trí 3) -->
                            <rect x="380" y="20" width="160" height="90" rx="12" fill="#047857" stroke="#34d399" stroke-width="2" />
                            <text x="460" y="45" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">VỊ TRÍ ③</text>
                            <text x="460" y="78" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">ich</text>
                            <text x="460" y="96" fill="#6ee7b7" font-size="10" text-anchor="middle">(Chủ ngữ đảo sau)</text>

                            <!-- Khối 4: Nudeln -->
                            <rect x="550" y="20" width="190" height="90" rx="12" fill="#334155" stroke="#64748b" stroke-width="2" />
                            <text x="645" y="45" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">THÀNH PHẦN KHÁC</text>
                            <text x="645" y="78" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">Nudeln.</text>
                            <text x="645" y="96" fill="#94a3b8" font-size="10" text-anchor="middle">(Tân ngữ bổ ngữ)</text>
                        ` : `
                            <!-- Câu xuôi: Ich (1) - esse (2) - am liebsten - Nudeln -->
                            <rect x="20" y="20" width="160" height="90" rx="12" fill="#047857" stroke="#34d399" stroke-width="2" />
                            <text x="100" y="45" fill="#a7f3d0" font-size="11" font-weight="bold" text-anchor="middle">VỊ TRÍ ①</text>
                            <text x="100" y="78" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">Ich</text>
                            <text x="100" y="96" fill="#6ee7b7" font-size="10" text-anchor="middle">(Chủ ngữ)</text>

                            <rect x="190" y="20" width="160" height="90" rx="12" fill="#b91c1c" stroke="#f87171" stroke-width="2.5" />
                            <text x="270" y="45" fill="#fecaca" font-size="11" font-weight="bold" text-anchor="middle">VỊ TRÍ ② (BẮT BUỘC)</text>
                            <text x="270" y="78" fill="#fef08a" font-size="20" font-weight="900" text-anchor="middle">esse</text>
                            <text x="270" y="96" fill="#fca5a5" font-size="10" text-anchor="middle">(Động từ chia)</text>

                            <rect x="360" y="20" width="190" height="90" rx="12" fill="#1d4ed8" stroke="#60a5fa" stroke-width="2" />
                            <text x="455" y="45" fill="#bfdbfe" font-size="11" font-weight="bold" text-anchor="middle">TRẠNG TỪ SO SÁNH</text>
                            <text x="455" y="78" fill="#ffffff" font-size="17" font-weight="900" text-anchor="middle">am liebsten</text>
                            <text x="455" y="96" fill="#93c5fd" font-size="10" text-anchor="middle">(Thích nhất)</text>

                            <rect x="560" y="20" width="180" height="90" rx="12" fill="#334155" stroke="#64748b" stroke-width="2" />
                            <text x="650" y="45" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">TÂN NGỮ</text>
                            <text x="650" y="78" fill="#ffffff" font-size="18" font-weight="900" text-anchor="middle">Nudeln.</text>
                            <text x="650" y="96" fill="#94a3b8" font-size="10" text-anchor="middle">(Món ăn)</text>
                        `}
                    </svg>
                </div>

                <div class="flex items-center justify-between flex-wrap gap-2 text-xs bg-slate-800/60 p-3 rounded-2xl border border-slate-700">
                    <div>
                        <span class="text-slate-400 block">${isSentenceInverted ? 'Đang hiển thị dạng ĐẢO NGỮ:' : 'Đang hiển thị dạng CÂU XUÔI:'}</span>
                        <span class="text-white font-bold text-sm">„${sentenceText}“</span>
                        <span class="text-slate-400 block italic mt-0.5">${translationText}</span>
                    </div>
                    <button onclick="speakGerman('${sentenceText.replace(/'/g, "\\'")}', 1.0)" class="px-3 py-1.5 rounded-xl bg-blue-500/20 text-blue-300 hover:bg-blue-500/30 font-bold transition flex items-center gap-1 cursor-pointer">
                        🔊 Nghe câu chuẩn
                    </button>
                </div>
            </div>
        `;
    }

    function toggleSentenceOrder() {
        isSentenceInverted = !isSentenceInverted;
        renderSentenceOrderSvg();
    }

    // =========================================================================
    // V5: QUẦY CHỢ TƯƠNG TÁC (MARKET STAND)
    // =========================================================================
    const MARKET_ITEMS = [
        { name: "Tomaten", icon: "🍅", priceStr: "2,50 € / kg", cents: 250, unit: "Kilo", question: "Wie viel kosten die Tomaten?", questionVi: "Cà chua giá bao nhiêu?", answer: "Das Kilo kostet zwei Euro fünfzig.", answerVi: "Một ký có giá 2 Euro 50 Cent." },
        { name: "Möhren", icon: "🥕", priceStr: "1,20 € / kg", cents: 120, unit: "Kilo", question: "Wie viel kosten die Möhren?", questionVi: "Cà rốt giá bao nhiêu?", answer: "Das Kilo kostet ein Euro zwanzig.", answerVi: "Một ký có giá 1 Euro 20 Cent." },
        { name: "Ananas", icon: "🍍", priceStr: "2,30 € / Stk", cents: 230, unit: "Stück", question: "Was kostet die Ananas?", questionVi: "Quả dứa giá bao nhiêu?", answer: "Die Ananas kostet zwei Euro dreißig.", answerVi: "Quả dứa có giá 2 Euro 30 Cent." },
        { name: "Käse", icon: "🧀", priceStr: "2,99 € / 100g", cents: 299, unit: "100 Gramm", question: "Was kostet der Käse?", questionVi: "Phô mai giá bao nhiêu?", answer: "Hundert Gramm kosten zwei Euro neunundneunzig.", answerVi: "Một trăm gam có giá 2 Euro 99 Cent." },
        { name: "Brot", icon: "🥖", priceStr: "2,80 € / Stk", cents: 280, unit: "Stück", question: "Was kostet das Brot?", questionVi: "Ổ bánh mì giá bao nhiêu?", answer: "Das Brot kostet zwei Euro achtzig.", answerVi: "Ổ bánh mì có giá 2 Euro 80 Cent." },
        { name: "Milch", icon: "🥛", priceStr: "1,10 € / L", cents: 110, unit: "Liter", question: "Wie viel kostet die Milch?", questionVi: "Sữa giá bao nhiêu?", answer: "Ein Liter Milch kostet ein Euro zehn.", answerVi: "Một lít sữa có giá 1 Euro 10 Cent." }
    ];

    let currentMarketItemIdx = 0;

    function renderMarketStandSvg() {
        const container = document.getElementById('svg-v5-container');
        if (!container) return;

        const it = MARKET_ITEMS[currentMarketItemIdx];

        container.innerHTML = `
            <div class="p-5 rounded-3xl bg-slate-900 border border-slate-800 text-white shadow-xl space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-teal-500/20 text-teal-400 font-bold flex items-center justify-center text-xs">V5</span>
                        <span class="font-black text-sm text-white">Sơ đồ V5: Quầy ChỢ Tương Tác — Bấm Món Để Hỏi & Trả Lời Giá</span>
                    </div>
                    <span class="text-xs text-slate-400">Bấm vào từng mặt hàng để nghe mẫu câu hỏi và báo giá theo đơn vị tương ứng</span>
                </div>

                <!-- Lưới 6 mặt hàng trên kệ chợ -->
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2.5">
                    ${MARKET_ITEMS.map((item, idx) => `
                        <button onclick="window.selectMarketItem(${idx})" class="p-3 rounded-2xl border text-center transition cursor-pointer ${idx === currentMarketItemIdx ? 'bg-teal-950 border-teal-400 ring-2 ring-teal-400/50' : 'bg-slate-800/80 hover:bg-slate-700/80 border-slate-700'}">
                            <span class="text-2xl block mb-1">${item.icon}</span>
                            <span class="text-xs font-black text-white block">${item.name}</span>
                            <span class="text-[11px] font-mono text-teal-300 font-bold block mt-0.5">${item.priceStr}</span>
                        </button>
                    `).join('')}
                </div>

                <!-- Hội thoại tương tác chi tiết cho món được chọn -->
                <div class="p-4 rounded-2xl bg-slate-800/90 border border-slate-700 space-y-3 text-xs">
                    <div class="flex items-center justify-between border-b border-slate-700 pb-2">
                        <span class="font-bold text-teal-300 text-sm flex items-center gap-1.5">
                            <span>${it.icon}</span> <span>Đang hỏi giá: ${it.name} (${it.priceStr})</span>
                        </span>
                        <span class="text-slate-400 text-[11px]">Đọc bằng chữ: ${priceToGermanCents(it.cents)}</span>
                    </div>

                    <div class="space-y-2">
                        <!-- Khách hỏi -->
                        <div class="p-3 rounded-xl bg-slate-900 border border-slate-700 flex items-center justify-between gap-3">
                            <div>
                                <span class="text-sky-400 font-bold text-[11px] block">Khách hàng hỏi:</span>
                                <span class="text-white font-bold text-sm block">„${it.question}“</span>
                                <span class="text-slate-400 text-[11px] block italic mt-0.5">${it.questionVi}</span>
                            </div>
                            <button onclick="speakGerman('${it.question.replace(/'/g, "\\'")}', 1.0)" class="px-2.5 py-1.5 rounded-lg bg-sky-500/20 text-sky-300 hover:bg-sky-500/30 font-bold transition cursor-pointer shrink-0">
                                🔊 Khách
                            </button>
                        </div>

                        <!-- Người bán trả lời -->
                        <div class="p-3 rounded-xl bg-slate-900 border border-slate-700 flex items-center justify-between gap-3">
                            <div>
                                <span class="text-emerald-400 font-bold text-[11px] block">Người bán đáp:</span>
                                <span class="text-white font-bold text-sm block">„${it.answer}“</span>
                                <span class="text-slate-400 text-[11px] block italic mt-0.5">${it.answerVi}</span>
                            </div>
                            <button onclick="speakGerman('${it.answer.replace(/'/g, "\\'")}', 1.0)" class="px-2.5 py-1.5 rounded-lg bg-emerald-500/20 text-emerald-300 hover:bg-emerald-500/30 font-bold transition cursor-pointer shrink-0">
                                🔊 Người bán
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    function selectMarketItem(idx) {
        currentMarketItemIdx = idx;
        renderMarketStandSvg();
    }

    // =========================================================================
    // V6: MÁY ĐỌC GIÁ TIỀN EURO (PREIS-LESER)
    // =========================================================================
    let currentInputCents = 375; // 3,75 €

    function renderPriceReaderSvg() {
        const container = document.getElementById('svg-v6-container');
        if (!container) return;

        const priceText = priceToGermanCents(currentInputCents);
        const euroDec = (currentInputCents / 100).toFixed(2).replace('.', ',');

        container.innerHTML = `
            <div class="p-5 rounded-3xl bg-slate-900 border border-slate-800 text-white shadow-xl space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-3">
                    <div class="flex items-center gap-2">
                        <span class="w-7 h-7 rounded-lg bg-purple-500/20 text-purple-400 font-bold flex items-center justify-center text-xs">V6</span>
                        <span class="font-black text-sm text-white">Sơ đồ V6: Máy Đọc Giá Tiền Euro Bằng Tiếng Đức (Preis-Leser)</span>
                    </div>
                    <span class="text-[11px] text-purple-300 font-mono">Quy tắc: Số Euro + 'Euro' + Số Cent (Không đọc Komma)</span>
                </div>

                <!-- Nút chọn nhanh giá tiền -->
                <div class="flex items-center gap-1.5 flex-wrap text-xs">
                    <span class="text-slate-400 font-semibold">Chọn giá mẫu:</span>
                    ${[50, 100, 120, 200, 299, 375, 640, 1250, 1999].map(cents => `
                        <button onclick="window.setPriceCents(${cents})" class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold transition cursor-pointer ${cents === currentInputCents ? 'bg-purple-600 text-white shadow-md' : 'bg-slate-800 hover:bg-slate-700 text-slate-300'}">
                            ${(cents / 100).toFixed(2).replace('.', ',')} €
                        </button>
                    `).join('')}
                </div>

                <!-- Khung hiển thị & phát âm -->
                <div class="p-4 rounded-2xl bg-slate-800/80 border border-slate-700 flex flex-col sm:flex-row items-center justify-between gap-4">
                    <div class="text-center sm:text-left space-y-1">
                        <div class="text-2xl sm:text-3xl font-black font-mono text-purple-300 tracking-wide">
                            ${euroDec} €
                        </div>
                        <div class="text-sm sm:text-base font-extrabold text-white">
                            👉 „${priceText}“
                        </div>
                    </div>

                    <button onclick="speakGerman('${priceText.replace(/'/g, "\\'")}', 0.9)" class="px-5 py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-black text-sm transition shadow-lg flex items-center gap-2 cursor-pointer shrink-0">
                        🔊 Nghe đọc giá này
                    </button>
                </div>
            </div>
        `;
    }

    function setPriceCents(cents) {
        currentInputCents = cents;
        renderPriceReaderSvg();
    }

    // =========================================================================
    // RENDER SƠ ĐỒ MINI CHO BÀI TẬP (V1 & V4)
    // =========================================================================
    function renderExerciseEssenSvg(code) {
        if (code === 'V1') {
            return `
                <div class="p-3 bg-slate-900 text-white rounded-xl text-xs space-y-2 border border-slate-700">
                    <div class="font-bold text-sky-400 text-[11px] flex items-center justify-between">
                        <span>📊 Bảng Tra Cứu Nhanh Đuôi Welch- (V1):</span>
                        <span class="text-amber-400 font-semibold">Chỉ giống đực đổi giữa Nom & Akk</span>
                    </div>
                    <div class="grid grid-cols-3 gap-1.5 text-center font-mono text-[11px]">
                        <div class="p-1.5 bg-slate-800 rounded text-slate-300 font-bold">Giống</div>
                        <div class="p-1.5 bg-sky-950 text-sky-300 rounded font-bold">Nominativ</div>
                        <div class="p-1.5 bg-rose-950 text-rose-300 rounded font-bold">Akkusativ</div>

                        <div class="p-1 bg-slate-800 rounded font-sans">🔵 der (m)</div>
                        <div class="p-1 bg-sky-900/60 rounded text-sky-200 font-bold">welcher</div>
                        <div class="p-1 bg-rose-900/60 rounded text-rose-200 font-bold">welchen</div>

                        <div class="p-1 bg-slate-800 rounded font-sans">🔴 die (f)</div>
                        <div class="p-1 bg-slate-800/80 rounded text-slate-300">welche</div>
                        <div class="p-1 bg-slate-800/80 rounded text-slate-300">welche</div>

                        <div class="p-1 bg-slate-800 rounded font-sans">🟢 das (n)</div>
                        <div class="p-1 bg-slate-800/80 rounded text-slate-300">welches</div>
                        <div class="p-1 bg-slate-800/80 rounded text-slate-300">welches</div>

                        <div class="p-1 bg-slate-800 rounded font-sans">🟣 die (PL)</div>
                        <div class="p-1 bg-slate-800/80 rounded text-slate-300">welche</div>
                        <div class="p-1 bg-slate-800/80 rounded text-slate-300">welche</div>
                    </div>
                </div>
            `;
        }
        if (code === 'V4') {
            return `
                <div class="p-3 bg-slate-900 text-white rounded-xl text-xs space-y-1.5 border border-slate-700">
                    <div class="font-bold text-amber-400 text-[11px]">
                        📐 Khung Câu Đảo Ngữ Vị Trí 1-2-3 (V4):
                    </div>
                    <div class="flex items-center gap-1.5 text-center font-bold text-[11px] overflow-x-auto py-1">
                        <div class="p-1.5 px-2 bg-blue-900 text-blue-200 rounded-lg shrink-0">① Am liebsten</div>
                        <span class="text-slate-500">→</span>
                        <div class="p-1.5 px-2 bg-rose-900 text-yellow-300 rounded-lg shrink-0 border border-yellow-400/40">② ĐỘNG TỪ (esse)</div>
                        <span class="text-slate-500">→</span>
                        <div class="p-1.5 px-2 bg-emerald-900 text-emerald-200 rounded-lg shrink-0">③ CHỦ NGỮ (ich)</div>
                        <span class="text-slate-500">→</span>
                        <div class="p-1.5 px-2 bg-slate-800 text-slate-300 rounded-lg shrink-0">Nudeln.</div>
                    </div>
                </div>
            `;
        }
        return '';
    }

    // =========================================================================
    // KHỞI TẠO TẤT CẢ SƠ ĐỒ
    // =========================================================================
    function initEssenSvgDiagrams() {
        renderWelchTableSvg();
        renderWelchFlowchartSvg();
        renderSteigerungStaircaseSvg();
        renderSentenceOrderSvg();
        renderMarketStandSvg();
        renderPriceReaderSvg();
    }

    // Export ra Window
    global.renderWelchTableSvg = renderWelchTableSvg;
    global.renderWelchFlowchartSvg = renderWelchFlowchartSvg;
    global.renderSteigerungStaircaseSvg = renderSteigerungStaircaseSvg;
    global.renderSentenceOrderSvg = renderSentenceOrderSvg;
    global.renderMarketStandSvg = renderMarketStandSvg;
    global.renderPriceReaderSvg = renderPriceReaderSvg;
    global.initEssenSvgDiagrams = initEssenSvgDiagrams;
    global.renderExerciseEssenSvg = renderExerciseEssenSvg;
    global.selectWelchNoun = selectWelchNoun;
    global.nextSteigerungAdj = nextSteigerungAdj;
    global.prevSteigerungAdj = prevSteigerungAdj;
    global.toggleSentenceOrder = toggleSentenceOrder;
    global.selectMarketItem = selectMarketItem;
    global.setPriceCents = setPriceCents;
    global.priceToGermanCents = priceToGermanCents;

})(typeof window !== 'undefined' ? window : this);
