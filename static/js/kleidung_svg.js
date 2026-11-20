/**
 * DeutschMeister - Module Sơ Đồ Trực Quan & Tương Tác Kleidung, Farbe, dies- & Wetter SVG
 * Dành riêng cho Bài 11 (A1): "Kleidung und Wetter - Trang phục, Màu sắc ở Akkusativ, Đại từ chỉ định dies-, Thời tiết"
 * 
 * Cung cấp 6 sơ đồ trực quan theo đặc tả kỹ thuật sư phạm chuẩn CEFR A1:
 * V1: Bảng dies- / welch- tương tác (Nominativ vs Akkusativ theo 3 giống & số nhiều)
 * V2: Bảng đuôi tính từ màu ở Akkusativ + Hộp chọn trang phục & màu sắc
 * V3: Lưu đồ phân biệt Akkusativ / Dativ (Tuân thủ nghiêm ngặt quy tắc Color-Dativ separation)
 * V4: Tủ quần áo tương tác (Kleiderschrank - 18 món đồ kèm chọn màu)
 * V5: Bản đồ thời tiết Việt Nam - Đức & Áo (Wetterkarte kèm phát thanh bản tin)
 * V6: Cuộc hội thoại ở phòng thử đồ (Umkleidekabine - tương tác mua sắm)
 */

(function (global) {
    'use strict';

    // =========================================================================
    // DỮ LIỆU NGUỒN CHUẨN (Single Source of Truth)
    // =========================================================================
    const ONES = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",
                  "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"];
    const TENS = { 20: "zwanzig", 30: "dreißig", 40: "vierzig", 50: "fünfzig", 60: "sechzig", 70: "siebzig", 80: "achtzig", 90: "neunzig" };

    function b11_b11_numWords(n) {
        if (n < 20) return ONES[n];
        const t = Math.floor(n / 10) * 10;
        const u = n % 10;
        return u === 0 ? TENS[t] : (ONES[u] + "und" + TENS[t]);
    }

    function b11_b11_tempToGerman(t) {
        if (t === 0) return "null Grad";
        if (t < 0) return "minus " + b11_numWords(-t) + " Grad";
        return b11_numWords(t) + " Grad";
    }

    // Danh từ trang phục cho V1
    const V1_NOUNS = [
        { label: "der Rock (chân váy)", gender: "m", art: "der", nomDies: "dieser", akkDies: "diesen", nomWelch: "welcher", akkWelch: "welchen", exNom: "Welcher Rock gefällt dir? — Dieser hier.", exAkk: "Welchen Rock nimmst du? — Diesen hier.", trNom: "Chiếc chân váy nào làm bạn thích? — Chiếc này đây.", trAkk: "Bạn lấy chiếc chân váy nào? — Chiếc này đây." },
        { label: "der Hut (chiếc mũ)", gender: "m", art: "der", nomDies: "dieser", akkDies: "diesen", nomWelch: "welcher", akkWelch: "welchen", exNom: "Welcher Hut passt mir? — Dieser hier.", exAkk: "Welchen Hut möchten Sie kaufen? — Diesen hier.", trNom: "Chiếc mũ nào vừa với tôi? — Chiếc này đây.", trAkk: "Ngài muốn mua chiếc mũ nào? — Chiếc này đây." },
        { label: "die Hose (chiếc quần)", gender: "f", art: "die", nomDies: "diese", akkDies: "diese", nomWelch: "welche", akkWelch: "welche", exNom: "Welche Hose passt dir? — Diese hier.", exAkk: "Welche Hose kaufst du? — Diese hier.", trNom: "Chiếc quần nào vừa với bạn? — Chiếc này đây.", trAkk: "Bạn mua chiếc quần nào? — Chiếc này đây." },
        { label: "die Jacke (áo khoác)", gender: "f", art: "die", nomDies: "diese", akkDies: "diese", nomWelch: "welche", akkWelch: "welche", exNom: "Welche Jacke gefällt Ihnen? — Diese hier.", exAkk: "Welche Jacke tragen Sie gern? — Diese hier.", trNom: "Chiếc áo khoác nào làm Ngài thích? — Chiếc này đây.", trAkk: "Ngài thích mặc chiếc áo khoác nào? — Chiếc này đây." },
        { label: "das Kleid (chiếc đầm)", gender: "n", art: "das", nomDies: "dieses", akkDies: "dieses", nomWelch: "welches", akkWelch: "welches", exNom: "Welches Kleid gefällt dir? — Dieses hier.", exAkk: "Welches Kleid kaufst du? — Dieses hier.", trNom: "Chiếc đầm nào làm bạn thích? — Chiếc này đây.", trAkk: "Bạn mua chiếc đầm nào? — Chiếc này đây." },
        { label: "das Hemd (áo sơ mi nam)", gender: "n", art: "das", nomDies: "dieses", akkDies: "dieses", nomWelch: "welches", akkWelch: "welches", exNom: "Welches Hemd passt ihm? — Dieses hier.", exAkk: "Welches Hemd nimmst du? — Dieses hier.", trNom: "Chiếc áo sơ mi nào vừa với anh ấy? — Chiếc này đây.", trAkk: "Bạn lấy chiếc áo sơ mi nào? — Chiếc này đây." },
        { label: "die Schuhe (đôi giày, PL)", gender: "pl", art: "die", nomDies: "diese", akkDies: "diese", nomWelch: "welche", akkWelch: "welche", exNom: "Welche Schuhe passen dir? — Diese hier.", exAkk: "Welche Schuhe nehmen Sie? — Diese hier.", trNom: "Đôi giày nào vừa với bạn? — Đôi này đây.", trAkk: "Ngài lấy đôi giày nào? — Đôi này đây." },
        { label: "die Stiefel (đôi bốt, PL)", gender: "pl", art: "die", nomDies: "diese", akkDies: "diese", nomWelch: "welche", akkWelch: "welche", exNom: "Welche Stiefel gefallen dir? — Diese hier.", exAkk: "Welche Stiefel kaufst du? — Diese hier.", trNom: "Đôi bốt nào làm bạn thích? — Đôi này đây.", trAkk: "Bạn mua đôi bốt nào? — Đôi này đây." }
    ];

    let b11_b11_currentV1NounIndex = 0;
    let b11_currentV1Case = "akk"; // "nom" hoặc "akk"

    // =========================================================================
    // SƠ ĐỒ V1: BẢNG DIES- / WELCH- TƯƠNG TÁC
    // =========================================================================
    function b11_b11_renderDiesTableSvg() {
        const container = document.getElementById('b11-svg-v1-container');
        if (!container) return;

        const noun = V1_NOUNS[b11_currentV1NounIndex];
        const isNom = b11_currentV1Case === "nom";
        const sentence = isNom ? noun.exNom : noun.exAkk;
        const translation = isNom ? noun.trNom : noun.trAkk;
        const audioSentence = sentence.replace("39", "neununddreißig");

        const rows = [
            { g: "m", label: "Giống Đực (der)", nomWelch: "welcher", nomDies: "dieser", akkWelch: "welchen", akkDies: "diesen", isHighlight: noun.gender === "m" },
            { g: "f", label: "Giống Cái (die)", nomWelch: "welche", nomDies: "diese", akkWelch: "welche", akkDies: "diese", isHighlight: noun.gender === "f" },
            { g: "n", label: "Giống Trung (das)", nomWelch: "welches", nomDies: "dieses", akkWelch: "welches", akkDies: "dieses", isHighlight: noun.gender === "n" },
            { g: "pl", label: "Số Nhiều (die)", nomWelch: "welche", nomDies: "diese", akkWelch: "welche", akkDies: "diese", isHighlight: noun.gender === "pl" }
        ];

        container.innerHTML = `
            <div class="p-5 sm:p-7 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-indigo-500/20 text-indigo-400 font-black text-xs">Sơ đồ V1</span>
                        <h3 class="text-base sm:text-lg font-black text-white">Bảng Đại Từ Chỉ Định dies- & Từ Hỏi welch- Tương Tác</h3>
                    </div>
                    <div class="flex items-center gap-2 text-xs">
                        <span class="text-slate-400">Chọn vai trò:</span>
                        <button type="button" onclick="b11_setV1Case('nom')" class="px-3 py-1.5 rounded-lg font-bold transition cursor-pointer ${isNom ? 'bg-amber-500 text-slate-950 shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
                            Nominativ (Chủ ngữ)
                        </button>
                        <button type="button" onclick="b11_setV1Case('akk')" class="px-3 py-1.5 rounded-lg font-bold transition cursor-pointer ${!isNom ? 'bg-emerald-500 text-slate-950 shadow' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}">
                            Akkusativ (Tân ngữ)
                        </button>
                    </div>
                </div>

                <div class="flex flex-wrap items-center justify-between gap-3 text-xs">
                    <div class="flex items-center gap-2">
                        <span class="text-slate-400 font-bold">Chọn danh từ:</span>
                        <select onchange="b11_selectV1Noun(this.value)" class="bg-slate-800 border border-slate-700 rounded-xl px-3 py-1.5 text-white font-bold focus:outline-none focus:border-indigo-400 cursor-pointer">
                            ${V1_NOUNS.map((item, idx) => `
                                <option value="${idx}" ${idx === b11_currentV1NounIndex ? 'selected' : ''}>${item.label}</option>
                            `).join('')}
                        </select>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <button type="button" onclick="b11_prevV1Noun()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">◀</button>
                        <span class="text-xs text-slate-400 font-mono">${b11_currentV1NounIndex + 1} / ${V1_NOUNS.length}</span>
                        <button type="button" onclick="b11_nextV1Noun()" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold transition">▶</button>
                    </div>
                </div>

                <!-- Bảng 4 hàng x 4 cột -->
                <div class="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-950/60">
                    <table class="w-full text-left text-xs">
                        <thead>
                            <tr class="border-b border-slate-800 bg-slate-900/90 text-slate-400">
                                <th class="p-3">Giống & Số</th>
                                <th class="p-3 text-center ${isNom ? 'bg-amber-950/40 text-amber-300 font-extrabold' : ''}">Nominativ (welch-)</th>
                                <th class="p-3 text-center ${isNom ? 'bg-amber-950/40 text-amber-300 font-extrabold' : ''}">Nominativ (dies-)</th>
                                <th class="p-3 text-center ${!isNom ? 'bg-emerald-950/40 text-emerald-300 font-extrabold' : ''}">Akkusativ (welch-)</th>
                                <th class="p-3 text-center ${!isNom ? 'bg-emerald-950/40 text-emerald-300 font-extrabold' : ''}">Akkusativ (dies-)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/80">
                            ${rows.map(r => {
                                const rowHighlight = r.isHighlight;
                                const isMascAkk = r.g === "m" && !isNom;
                                return `
                                    <tr class="${rowHighlight ? 'bg-indigo-950/40 border-l-4 border-indigo-400' : 'hover:bg-slate-900/40'} transition">
                                        <td class="p-3 font-bold ${rowHighlight ? 'text-indigo-300 font-black' : 'text-slate-300'}">${r.label}</td>
                                        <td class="p-3 text-center font-mono ${isNom && rowHighlight ? 'bg-amber-500/20 text-amber-300 font-black rounded-lg scale-105' : 'text-slate-300'}">${r.nomWelch}</td>
                                        <td class="p-3 text-center font-mono ${isNom && rowHighlight ? 'bg-amber-500/20 text-amber-300 font-black rounded-lg scale-105' : 'text-slate-300'}">${r.nomDies}</td>
                                        <td class="p-3 text-center font-mono ${!isNom && rowHighlight ? (isMascAkk ? 'bg-rose-500/30 text-rose-300 font-black border border-rose-400/50 rounded-lg animate-pulse' : 'bg-emerald-500/20 text-emerald-300 font-black rounded-lg') : 'text-slate-300'}">
                                            ${r.akkWelch}
                                        </td>
                                        <td class="p-3 text-center font-mono ${!isNom && rowHighlight ? (isMascAkk ? 'bg-rose-500/30 text-rose-300 font-black border border-rose-400/50 rounded-lg animate-pulse' : 'bg-emerald-500/20 text-emerald-300 font-black rounded-lg') : 'text-slate-300'}">
                                            ${r.akkDies}
                                        </td>
                                    </tr>
                                `;
                            }).join('')}
                        </tbody>
                    </table>
                </div>

                <div class="p-3 rounded-xl bg-slate-800/60 border border-slate-700/60 text-[11px] text-slate-300 flex items-center justify-between gap-2">
                    <span>💡 <b>Quy tắc vàng:</b> Chỉ giống <b>Đực (der)</b> mới biến đổi ở Akkusativ (<code>-en</code>: <b>welchen / diesen</b>). Giống cái (<code>-e</code>), giống trung (<code>-es</code>) và số nhiều (<code>-e</code>) giữ nguyên hình thái như ở Nominativ!</span>
                </div>

                <!-- Khung câu ví dụ & phát âm -->
                <div class="p-4 rounded-2xl bg-gradient-to-r from-indigo-950/80 to-slate-900 border border-indigo-500/30 flex flex-wrap items-center justify-between gap-3">
                    <div class="space-y-1">
                        <div class="text-xs text-indigo-400 font-bold uppercase tracking-wider">Hội thoại mẫu minh họa:</div>
                        <div class="text-sm sm:text-base font-black text-white">👉 „${sentence}“</div>
                        <div class="text-xs text-slate-400">📖 Dịch: ${translation}</div>
                    </div>
                    <button type="button" onclick="speakGerman('${audioSentence.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                        🔊 Nghe câu mẫu
                    </button>
                </div>
            </div>
        `;
    }

    function b11_b11_selectV1Noun(idx) {
        b11_currentV1NounIndex = parseInt(idx, 10) || 0;
        b11_renderDiesTableSvg();
    }
    function b11_b11_prevV1Noun() {
        b11_currentV1NounIndex = (b11_currentV1NounIndex - 1 + V1_NOUNS.length) % V1_NOUNS.length;
        b11_renderDiesTableSvg();
    }
    function b11_b11_nextV1Noun() {
        b11_currentV1NounIndex = (b11_currentV1NounIndex + 1) % V1_NOUNS.length;
        b11_renderDiesTableSvg();
    }
    function b11_b11_setV1Case(c) {
        b11_currentV1Case = c;
        b11_renderDiesTableSvg();
    }

    // =========================================================================
    // SƠ ĐỒ V2: BẢNG ĐUÔI TÍNH TỪ MÀU Ở AKKUSATIV + HỘP CHỌN
    // =========================================================================
    const V2_ITEMS = [
        { label: "der Rock (chân váy)", g: "m", art: "einen", ending: "en", noun: "Rock", tr: "chân váy" },
        { label: "der Mantel (áo măng tô)", g: "m", art: "einen", ending: "en", noun: "Mantel", tr: "áo măng tô" },
        { label: "der Pullover (áo len)", g: "m", art: "einen", ending: "en", noun: "Pullover", tr: "áo len" },
        { label: "der Anzug (bộ com lê)", g: "m", art: "einen", ending: "en", noun: "Anzug", tr: "bộ com lê" },
        { label: "der Gürtel (thắt lưng)", g: "m", art: "einen", ending: "en", noun: "Gürtel", tr: "thắt lưng" },
        { label: "der Hut (chiếc mũ)", g: "m", art: "einen", ending: "en", noun: "Hut", tr: "mũ" },
        { label: "die Hose (chiếc quần)", g: "f", art: "eine", ending: "e", noun: "Hose", tr: "quần" },
        { label: "die Jacke (áo khoác)", g: "f", art: "eine", ending: "e", noun: "Jacke", tr: "áo khoác" },
        { label: "die Bluse (áo sơ mi nữ)", g: "f", art: "eine", ending: "e", noun: "Bluse", tr: "áo sơ mi nữ" },
        { label: "das Kleid (chiếc đầm)", g: "n", art: "ein", ending: "es", noun: "Kleid", tr: "đầm" },
        { label: "das Hemd (áo sơ mi nam)", g: "n", art: "ein", ending: "es", noun: "Hemd", tr: "áo sơ mi nam" },
        { label: "das T-Shirt (áo phông)", g: "n", art: "ein", ending: "es", noun: "T-Shirt", tr: "áo phông" },
        { label: "die Schuhe (đôi giày, PL)", g: "pl", art: "", ending: "e", noun: "Schuhe", tr: "đôi giày" },
        { label: "die Stiefel (đôi bốt, PL)", g: "pl", art: "", ending: "e", noun: "Stiefel", tr: "đôi bốt" },
        { label: "die Socken (đôi tất, PL)", g: "pl", art: "", ending: "e", noun: "Socken", tr: "đôi tất" }
    ];

    const V2_COLORS = [
        { color: "schwarz", nameVi: "đen", isInvariant: false },
        { color: "rot", nameVi: "đỏ", isInvariant: false },
        { color: "blau", nameVi: "xanh da trời", isInvariant: false },
        { color: "grün", nameVi: "xanh lá", isInvariant: false },
        { color: "weiß", nameVi: "trắng", isInvariant: false },
        { color: "grau", nameVi: "xám/ghi", isInvariant: false },
        { color: "braun", nameVi: "nâu", isInvariant: false },
        { color: "gelb", nameVi: "vàng", isInvariant: false },
        { color: "bunt", nameVi: "sặc sỡ", isInvariant: false },
        { color: "dunkelblau", nameVi: "xanh đậm", isInvariant: false },
        { color: "hellblau", nameVi: "xanh nhạt", isInvariant: false },
        { color: "dunkelgrün", nameVi: "xanh lá đậm", isInvariant: false },
        { color: "hellgrün", nameVi: "xanh lá nhạt", isInvariant: false },
        { color: "violett", nameVi: "tím", isInvariant: false },
        { color: "rosa", nameVi: "hồng nhạt (bất biến)", isInvariant: true },
        { color: "lila", nameVi: "tím hồng (bất biến)", isInvariant: true },
        { color: "beige", nameVi: "be (bất biến)", isInvariant: true },
        { color: "orange", nameVi: "cam (bất biến)", isInvariant: true }
    ];

    let b11_b11_currentV2ItemIndex = 0;
    let b11_b11_currentV2ColorIndex = 0;

    function b11_b11_renderFarbeAkkusativSvg() {
        const container = document.getElementById('b11-svg-v2-container');
        if (!container) return;

        const it = V2_ITEMS[b11_currentV2ItemIndex];
        const cl = V2_COLORS[b11_currentV2ColorIndex];

        let phraseDe = "";
        let colorWord = "";
        if (cl.isInvariant) {
            colorWord = cl.color;
            phraseDe = it.art ? `${it.art} ${colorWord} ${it.noun}` : `${colorWord} ${it.noun}`;
        } else {
            colorWord = cl.color + it.ending;
            phraseDe = it.art ? `${it.art} ${colorWord} ${it.noun}` : `${colorWord} ${it.noun}`;
        }

        const sentenceDe = `Ich trage gern ${phraseDe}.`;
        const sentenceVi = `Tôi thích mặc một chiếc ${it.tr} màu ${cl.nameVi.replace(" (bất biến)", "")}.`;

        container.innerHTML = `
            <div class="p-5 sm:p-7 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-emerald-500/20 text-emerald-400 font-black text-xs">Sơ đồ V2</span>
                        <h3 class="text-base sm:text-lg font-black text-white">Bảng Đuôi Tính Từ Màu ở Akkusativ: „en – e – es – e“</h3>
                    </div>
                    <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-400 text-xs font-semibold">Tự động ghép đuôi chuẩn xác</span>
                </div>

                <!-- 4 Cột quy tắc đuôi -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-center text-xs">
                    <div class="p-3 rounded-2xl bg-blue-950/50 border border-blue-500/40 space-y-1 ${it.g === 'm' ? 'ring-2 ring-blue-400 scale-105' : ''} transition">
                        <div class="font-bold text-blue-300">Giống Đực (m)</div>
                        <div class="text-2xl font-black text-blue-400 font-mono">-en</div>
                        <div class="text-[11px] text-slate-300">einen schwarz<b class="text-amber-300">en</b> Rock</div>
                    </div>
                    <div class="p-3 rounded-2xl bg-rose-950/50 border border-rose-500/40 space-y-1 ${it.g === 'f' ? 'ring-2 ring-rose-400 scale-105' : ''} transition">
                        <div class="font-bold text-rose-300">Giống Cái (f)</div>
                        <div class="text-2xl font-black text-rose-400 font-mono">-e</div>
                        <div class="text-[11px] text-slate-300">eine rot<b class="text-amber-300">e</b> Bluse</div>
                    </div>
                    <div class="p-3 rounded-2xl bg-emerald-950/50 border border-emerald-500/40 space-y-1 ${it.g === 'n' ? 'ring-2 ring-emerald-400 scale-105' : ''} transition">
                        <div class="font-bold text-emerald-300">Giống Trung (n)</div>
                        <div class="text-2xl font-black text-emerald-400 font-mono">-es</div>
                        <div class="text-[11px] text-slate-300">ein grün<b class="text-amber-300">es</b> Kleid</div>
                    </div>
                    <div class="p-3 rounded-2xl bg-purple-950/50 border border-purple-500/40 space-y-1 ${it.g === 'pl' ? 'ring-2 ring-purple-400 scale-105' : ''} transition">
                        <div class="font-bold text-purple-300">Số Nhiều (Plural)</div>
                        <div class="text-2xl font-black text-purple-400 font-mono">-e</div>
                        <div class="text-[11px] text-slate-300">PL -e khi không có mạo từ (rote Schuhe); nếu đi sau die / diese / welche / keine / meine thì dùng đuôi -en (diese roten Schuhe)</div>
                    </div>
                </div>

                <!-- Hộp chọn tương tác -->
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-1.5">
                        <label class="text-slate-400 font-bold">1. Chọn món đồ trang phục:</label>
                        <select onchange="b11_selectV2Item(this.value)" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white font-bold focus:outline-none focus:border-emerald-400 cursor-pointer">
                            ${V2_ITEMS.map((item, idx) => `
                                <option value="${idx}" ${idx === b11_currentV2ItemIndex ? 'selected' : ''}>${item.label}</option>
                            `).join('')}
                        </select>
                    </div>
                    <div class="p-3.5 rounded-2xl bg-slate-800/80 border border-slate-700 space-y-1.5">
                        <label class="text-slate-400 font-bold">2. Chọn màu sắc:</label>
                        <select onchange="b11_selectV2Color(this.value)" class="w-full bg-slate-900 border border-slate-700 rounded-xl px-3 py-2 text-white font-bold focus:outline-none focus:border-emerald-400 cursor-pointer">
                            ${V2_COLORS.map((item, idx) => `
                                <option value="${idx}" ${idx === b11_currentV2ColorIndex ? 'selected' : ''}>${item.color} (${item.nameVi})</option>
                            `).join('')}
                        </select>
                    </div>
                </div>

                <!-- Cụm từ sinh ra -->
                <div class="p-4 rounded-2xl bg-slate-950 border border-emerald-500/30 flex flex-wrap items-center justify-between gap-3">
                    <div class="space-y-1">
                        <div class="text-xs text-slate-400 font-bold">Cụm từ Akkusativ hoàn chỉnh:</div>
                        <div class="text-lg sm:text-xl font-black text-emerald-300">
                            👉 ${it.art ? `<span class="text-slate-300">${it.art}</span> ` : ''}<span class="text-amber-300 underline font-mono">${colorWord}</span> <span class="text-white">${it.noun}</span>
                            ${cl.isInvariant ? '<span class="text-[11px] text-rose-400 font-normal ml-2">(Màu bất biến: không chia đuôi)</span>' : ''}
                        </div>
                        <div class="text-xs text-slate-300">Câu đầy đủ: <i>„${sentenceDe}“</i> — ${sentenceVi}</div>
                    </div>
                    <button type="button" onclick="speakGerman('${sentenceDe.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                        🔊 Nghe câu này
                    </button>
                </div>
            </div>
        `;
    }

    function b11_b11_selectV2Item(idx) {
        b11_currentV2ItemIndex = parseInt(idx, 10) || 0;
        b11_renderFarbeAkkusativSvg();
    }
    function b11_b11_selectV2Color(idx) {
        b11_currentV2ColorIndex = parseInt(idx, 10) || 0;
        b11_renderFarbeAkkusativSvg();
    }

    // =========================================================================
    // SƠ ĐỒ V3: LƯU ĐỒ PHÂN BIỆT AKKUSATIV / DATIV
    // =========================================================================
    function b11_b11_renderAkkDativFlowchartSvg() {
        const container = document.getElementById('b11-svg-v3-container');
        if (!container) return;

        container.innerHTML = `
            <div class="p-5 sm:p-7 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-purple-500/20 text-purple-400 font-black text-xs">Sơ đồ V3</span>
                        <h3 class="text-base sm:text-lg font-black text-white">Lưu Đồ Quyết Định Phân Biệt Akkusativ vs. Dativ</h3>
                    </div>
                    <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-400 text-xs font-semibold">Chuẩn ngữ pháp CEFR A1</span>
                </div>

                <!-- Bảng so sánh 2 nhánh rẽ -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                    <!-- Nhánh Akkusativ (Cách 4) -->
                    <div class="p-4 rounded-2xl bg-emerald-950/40 border border-emerald-500/40 space-y-3">
                        <div class="flex items-center justify-between font-black text-emerald-300 border-b border-emerald-500/30 pb-2">
                            <span class="text-sm">🟢 NHÁNH AKKUSATIV (CÁCH 4)</span>
                            <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-200 text-[11px]">Wen / Was?</span>
                        </div>
                        <ul class="space-y-1.5 text-slate-300">
                            <li>• <b>Động từ tác động:</b> <code>tragen, anziehen, anprobieren, kaufen, suchen, nehmen, brauchen</code>.</li>
                            <li>• <b>Vai trò:</b> Tân ngữ trực tiếp (đồ vật bị mặc, bị mua, bị tìm).</li>
                            <li>• <b>Mẹo nhớ:</b> Chỉ giống đực đổi <b>der → den, ein → einen, dies- → diesen</b>.</li>
                            <li>• <b>Gắn màu sắc:</b> Đuôi <code>-en / -e / -es / -e</code> (đúng quy tắc Học phần 3).</li>
                        </ul>
                        <div class="p-3 rounded-xl bg-slate-900/90 border border-emerald-500/30 space-y-1">
                            <div class="text-[11px] text-emerald-400 font-bold">Ví dụ chuẩn (Bấm để nghe):</div>
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono text-white">„Ich trage einen blauen Anzug.“</span>
                                <button type="button" onclick="speakGerman('Ich trage einen blauen Anzug.', 0.9)" class="text-emerald-400 hover:text-emerald-300 font-bold cursor-pointer">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-400">Dịch: Tôi mặc một bộ com lê xanh.</div>
                        </div>
                    </div>

                    <!-- Nhánh Dativ (Cách 3) -->
                    <div class="p-4 rounded-2xl bg-purple-950/40 border border-purple-500/40 space-y-3">
                        <div class="flex items-center justify-between font-black text-purple-300 border-b border-purple-500/30 pb-2">
                            <span class="text-sm">🟣 NHÁNH DATIV (CÁCH 3)</span>
                            <span class="px-2 py-0.5 rounded bg-purple-500/20 text-purple-200 text-[11px]">Wem? (Cho ai)</span>
                        </div>
                        <ul class="space-y-1.5 text-slate-300">
                            <li>• <b>Động từ cảm nhận/sở hữu:</b> <code>gefallen, passen, stehen, gehören, helfen</code>.</li>
                            <li>• <b>Món đồ là chủ ngữ:</b> <i>Der Mantel passt <b>mir</b></i> (Chiếc áo vừa với tôi).</li>
                            <li>• <b>Đại từ Dativ:</b> <code>mir, dir, ihm, ihr, uns, euch, ihnen, Ihnen</code>.</li>
                            <li>• <b>Quy tắc vàng:</b> Với nhóm động từ Dativ (<code>gefallen, passen, stehen, gehören</code>), món đồ trang phục đóng vai trò làm <b>Chủ ngữ (Nominativ)</b>, còn người mặc/thích luôn chia ở <b>Cách 3 (Dativ: mir, dir, ihm, ihr...)</b>.</li>
                        </ul>
                        <div class="p-2.5 rounded-xl bg-purple-900/40 border border-purple-500/30 text-[11px] text-purple-200 space-y-1">
                            <div class="font-bold text-white">🔍 Phân biệt 4 động từ thời trang đi với Dativ:</div>
                            <div>• <b>passen (+ Dativ)</b>: vừa vặn (về kích cỡ / size) — <i>„Die Hose passt mir.“</i></div>
                            <div>• <b>stehen (+ Dativ)</b>: hợp (về màu sắc, kiểu dáng) — <i>„Das Kleid steht dir gut.“</i></div>
                            <div>• <b>gefallen (+ Dativ)</b>: thích / ưng mắt (về thẩm mỹ) — <i>„Der Rock gefällt ihr.“</i></div>
                            <div>• <b>gehören (+ Dativ)</b>: thuộc về ai (sở hữu) — <i>„Der Hut gehört ihm.“</i></div>
                        </div>
                        <div class="p-3 rounded-xl bg-slate-900/90 border border-purple-500/30 space-y-1">
                            <div class="text-[11px] text-purple-400 font-bold">Ví dụ chuẩn (Bấm để nghe):</div>
                            <div class="flex items-center justify-between gap-2">
                                <span class="font-mono text-white">„Der Pullover gefällt mir sehr gut.“</span>
                                <button type="button" onclick="speakGerman('Der Pullover gefällt mir sehr gut.', 0.9)" class="text-purple-400 hover:text-purple-300 font-bold cursor-pointer">🔊</button>
                            </div>
                            <div class="text-[11px] text-slate-400">Dịch: Chiếc áo len làm tôi rất thích.</div>
                        </div>
                    </div>
                </div>

                <!-- Trường hợp cả hai: schenken, zeigen -->
                <div class="p-3.5 rounded-2xl bg-slate-800/70 border border-slate-700 text-xs text-slate-300 space-y-1">
                    <div class="font-bold text-amber-300">⚡ Động từ đi với cả hai tân ngữ (schenken, zeigen):</div>
                    <div>Công thức: <code>S + V + Người (Dativ) + Vật (Akkusativ)</code> — <i>„Ich schenke <b>meinem Vater</b> (Dativ) <b>eine Krawatte</b> (Akkusativ).“</i></div>
                </div>
            </div>
        `;
    }

    // =========================================================================
    // SƠ ĐỒ V4: TỦ QUẦN ÁO TƯƠNG TÁC (KLEIDERSCHRANK)
    // =========================================================================
    const V4_ITEMS = [
        { icon: "🧥", word: "der Mantel", pl: "PL: die Mäntel", vi: "áo măng tô", sentenceDe: "Ich trage einen Mantel.", sentenceVi: "Tôi mặc một chiếc áo măng tô." },
        { icon: "👔", word: "das Hemd", pl: "PL: die Hemden", vi: "áo sơ mi nam", sentenceDe: "Ich trage ein Hemd.", sentenceVi: "Tôi mặc một chiếc áo sơ mi nam." },
        { icon: "👗", word: "das Kleid", pl: "PL: die Kleider", vi: "váy đầm", sentenceDe: "Ich trage ein Kleid.", sentenceVi: "Tôi mặc một chiếc váy đầm." },
        { icon: "👖", word: "die Hose", pl: "PL: die Hosen", vi: "quần dài", sentenceDe: "Ich trage eine Hose.", sentenceVi: "Tôi mặc một chiếc quần dài." },
        { icon: "👚", word: "die Bluse", pl: "PL: die Blusen", vi: "áo sơ mi nữ", sentenceDe: "Ich trage eine Bluse.", sentenceVi: "Tôi mặc một chiếc áo sơ mi nữ." },
        { icon: "🥾", word: "der Stiefel", pl: "PL: die Stiefel", vi: "bốt, ủng (đôi bốt)", sentenceDe: "Ich trage Stiefel.", sentenceVi: "Tôi đi bốt." },
        { icon: "👞", word: "der Schuh", pl: "PL: die Schuhe", vi: "giày (đôi giày)", sentenceDe: "Ich trage Schuhe.", sentenceVi: "Tôi đi giày." },
        { icon: "🧣", word: "der Schal", pl: "PL: die Schals", vi: "khăn quàng", sentenceDe: "Ich trage einen Schal.", sentenceVi: "Tôi quàng một chiếc khăn." },
        { icon: "🧤", word: "der Handschuh", pl: "PL: die Handschuhe", vi: "găng tay (đôi găng tay)", sentenceDe: "Ich trage Handschuhe.", sentenceVi: "Tôi đeo găng tay." },
        { icon: "🎩", word: "der Hut", pl: "PL: die Hüte", vi: "mũ rộng vành", sentenceDe: "Ich trage einen Hut.", sentenceVi: "Tôi đội một chiếc mũ rộng vành." },
        { icon: "🧢", word: "die Mütze", pl: "PL: die Mützen", vi: "mũ len (mũ lưỡi trai)", sentenceDe: "Ich trage eine Mütze.", sentenceVi: "Tôi đội một chiếc mũ len (mũ lưỡi trai)." },
        { icon: "👔", word: "die Krawatte", pl: "PL: die Krawatten", vi: "cà vạt", sentenceDe: "Ich trage eine Krawatte.", sentenceVi: "Tôi đeo một chiếc cà vạt." },
        { icon: "🧦", word: "die Socke", pl: "PL: die Socken", vi: "tất, vớ (đôi tất)", sentenceDe: "Ich trage Socken.", sentenceVi: "Tôi đi tất." },
        { icon: "👕", word: "das T-Shirt", pl: "PL: die T-Shirts", vi: "áo phông", sentenceDe: "Ich trage ein T-Shirt.", sentenceVi: "Tôi mặc một chiếc áo phông." },
        { icon: "🤵", word: "der Anzug", pl: "PL: die Anzüge", vi: "bộ com lê", sentenceDe: "Ich trage einen Anzug.", sentenceVi: "Tôi mặc một bộ com lê." },
        { icon: "🧥", word: "der Pullover", pl: "PL: die Pullover", vi: "áo len", sentenceDe: "Ich trage einen Pullover.", sentenceVi: "Tôi mặc một chiếc áo len." },
        { icon: "🧥", word: "die Jacke", pl: "PL: die Jacken", vi: "áo khoác", sentenceDe: "Ich trage eine Jacke.", sentenceVi: "Tôi mặc một chiếc áo khoác." },
        { icon: "👖", word: "die Jeans", pl: "PL: die Jeans", vi: "quần bò (jeans)", sentenceDe: "Ich trage eine Jeans.", sentenceVi: "Tôi mặc quần bò (jeans)." }
    ];

    let b11_b11_currentV4Index = 0;

    function b11_b11_renderKleiderschrankSvg() {
        const container = document.getElementById('b11-svg-v4-container');
        if (!container) return;

        const it = V4_ITEMS[b11_currentV4Index];
        const sentenceDe = it.sentenceDe;
        const sentenceVi = it.sentenceVi;
        const jeansExtra = it.word === 'die Jeans' ? ' (hoặc <i>„Ich trage Jeans.“</i>)' : '';

        container.innerHTML = `
            <div class="p-5 sm:p-7 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-blue-500/20 text-blue-400 font-black text-xs">Sơ đồ V4</span>
                        <h3 class="text-base sm:text-lg font-black text-white">Tủ Quần Áo Tương Tác (Kleiderschrank)</h3>
                    </div>
                    <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-400 text-xs font-semibold">18 Món đồ trang phục chuẩn</span>
                </div>

                <!-- Lưới 18 món đồ trong tủ -->
                <div class="grid grid-cols-3 sm:grid-cols-6 gap-2 text-xs">
                    ${V4_ITEMS.map((item, idx) => `
                        <button type="button" onclick="b11_selectV4Item(${idx})" class="p-2.5 rounded-2xl flex flex-col items-center justify-center gap-1 transition cursor-pointer ${idx === b11_currentV4Index ? 'bg-indigo-600 text-white shadow-lg ring-2 ring-indigo-400 scale-105' : 'bg-slate-800/80 hover:bg-slate-700/80 text-slate-300'}">
                            <span class="text-2xl">${item.icon}</span>
                            <span class="font-bold text-[11px] text-center truncate w-full">${item.word}</span>
                        </button>
                    `).join('')}
                </div>

                <!-- Khung chi tiết món đồ được chọn -->
                <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 flex flex-wrap items-center justify-between gap-4">
                    <div class="flex items-center gap-3">
                        <span class="text-4xl p-2 rounded-2xl bg-slate-800">${it.icon}</span>
                        <div>
                            <div class="text-base font-black text-white">${it.word} <span class="text-xs text-slate-400 font-normal">(${it.pl})</span></div>
                            <div class="text-xs text-indigo-400 font-bold">Nghĩa: ${it.vi}</div>
                            <div class="text-xs text-slate-300 mt-1">Câu mẫu: <b>„${sentenceDe}“</b>${jeansExtra} — <i>${sentenceVi}</i></div>
                        </div>
                    </div>
                    <button type="button" onclick="speakGerman('${sentenceDe.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                        🔊 Nghe phát âm
                    </button>
                </div>
            </div>
        `;
    }

    function b11_b11_selectV4Item(idx) {
        b11_currentV4Index = parseInt(idx, 10) || 0;
        b11_renderKleiderschrankSvg();
    }

    // =========================================================================
    // SƠ ĐỒ V5: BẢN ĐỒ THỜI TIẾT VIỆT NAM - ĐỨC (WETTERKARTE)
    // =========================================================================
    const CITIES_WEATHER = [
        { city: "Berlin", country: "Đức", icon: "⛅", desc: "bewölkt", temp: 8, tempWord: "acht Grad", de: "In Berlin ist es bewölkt. Es sind acht Grad.", vi: "Ở Berlin trời nhiều mây, nhiệt độ tám độ." },
        { city: "Hamburg", country: "Đức", icon: "🌧️", desc: "regnet und windig", temp: 7, tempWord: "sieben Grad", de: "In Hamburg regnet es und es ist windig. Es sind sieben Grad.", vi: "Ở Hamburg trời mưa và có gió, nhiệt độ bảy độ." },
        { city: "München", country: "Đức", icon: "☀️", desc: "sonnig", temp: 12, tempWord: "zwölf Grad", de: "In München scheint die Sonne. Es sind zwölf Grad.", vi: "Ở München trời có nắng, nhiệt độ mười hai độ." },
        { city: "Wien", country: "Áo", icon: "🌫️", desc: "neblig", temp: 4, tempWord: "vier Grad", de: "In Wien ist es neblig. Es sind vier Grad.", vi: "Ở Wien trời có sương mù, nhiệt độ bốn độ." },
        { city: "Hà Nội", country: "Việt Nam", icon: "🌫️", desc: "neblig", temp: 24, tempWord: "vierundzwanzig Grad", de: "In Hà Nội ist es neblig. Es sind vierundzwanzig Grad.", vi: "Ở Hà Nội trời có sương mù, nhiệt độ hai mươi tư độ." },
        { city: "Hải Phòng", country: "Việt Nam", icon: "🌬️", desc: "windig", temp: 22, tempWord: "zweiundzwanzig Grad", de: "In Hải Phòng ist es windig. Es sind zweiundzwanzig Grad.", vi: "Ở Hải Phòng trời có gió, nhiệt độ hai mươi hai độ." },
        { city: "Đà Lạt", country: "Việt Nam", icon: "🌫️", desc: "kühl und neblig", temp: 17, tempWord: "siebzehn Grad", de: "In Đà Lạt ist es kühl und oft neblig. Es sind siebzehn Grad.", vi: "Ở Đà Lạt trời mát và hay có sương mù, nhiệt độ mười bảy độ." },
        { city: "Sài Gòn", country: "Việt Nam", icon: "☀️", desc: "sonnig und heiß", temp: 33, tempWord: "dreiunddreißig Grad", de: "In Sài Gòn ist es sonnig und heiß. Es sind dreiunddreißig Grad.", vi: "Ở Sài Gòn trời có nắng và nóng, nhiệt độ ba mươi ba độ." }
    ];

    let b11_b11_currentCityIndex = 0;

    function b11_b11_renderWetterMapSvg() {
        const container = document.getElementById('b11-svg-v5-container');
        if (!container) return;

        const c = CITIES_WEATHER[b11_currentCityIndex];

        container.innerHTML = `
            <div class="p-5 sm:p-7 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-amber-500/20 text-amber-400 font-black text-xs">Sơ đồ V5</span>
                        <h3 class="text-base sm:text-lg font-black text-white">Bản Đồ Thời Tiết Việt Nam - Đức & Áo (Wetterkarte)</h3>
                    </div>
                    <button type="button" onclick="b11_readFullWeatherReport()" class="px-3.5 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs transition shadow flex items-center gap-1.5 cursor-pointer">
                        📻 Đọc toàn bộ Bản tin thời tiết
                    </button>
                </div>

                <!-- Danh sách các thành phố -->
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5 text-xs">
                    ${CITIES_WEATHER.map((city, idx) => `
                        <button type="button" onclick="b11_selectCity(${idx})" class="p-3 rounded-2xl flex items-center justify-between gap-2 transition cursor-pointer ${idx === b11_currentCityIndex ? 'bg-amber-500/20 border-2 border-amber-400 text-white' : 'bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 text-slate-300'}">
                            <div class="text-left">
                                <div class="font-black text-sm">${city.city}</div>
                                <div class="text-[10px] text-slate-400">${city.country}</div>
                            </div>
                            <div class="text-right">
                                <div class="text-xl">${city.icon}</div>
                                <div class="font-mono font-bold text-amber-300">${city.temp}°C</div>
                            </div>
                        </button>
                    `).join('')}
                </div>

                <!-- Chi tiết thành phố chọn -->
                <div class="p-4 rounded-2xl bg-slate-950 border border-amber-500/30 flex flex-wrap items-center justify-between gap-3">
                    <div class="space-y-1">
                        <div class="text-xs text-amber-400 font-bold uppercase tracking-wider">Thời tiết tại ${c.city} (${c.country}):</div>
                        <div class="text-sm sm:text-base font-black text-white">👉 „${c.de}“</div>
                        <div class="text-xs text-slate-400">📖 Dịch: ${c.vi} (Nhiệt độ đọc: <i>${c.tempWord}</i>)</div>
                    </div>
                    <button type="button" onclick="speakGerman('${c.de.replace(/'/g, "\\'")}', 0.9)" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs transition shadow-md flex items-center gap-1.5 cursor-pointer shrink-0">
                        🔊 Nghe phát âm
                    </button>
                </div>
            </div>
        `;
    }

    function b11_b11_selectCity(idx) {
        b11_currentCityIndex = parseInt(idx, 10) || 0;
        b11_renderWetterMapSvg();
    }

    function b11_b11_readFullWeatherReport() {
        const fullReport = "Guten Morgen! Hier ist der Wetterbericht für heute. In Berlin ist es bewölkt, es sind acht Grad. In Hamburg regnet es und es ist windig, es sind sieben Grad. In München scheint die Sonne, es sind zwölf Grad. In Wien ist es neblig, es sind vier Grad. In Vietnam: In Hà Nội ist es neblig, es sind vierundzwanzig Grad. In Hải Phòng ist es windig, zweiundzwanzig Grad. In Đà Lạt ist es kühl und neblig, siebzehn Grad. In Sài Gòn ist es sonnig und heiß, dreiunddreißig Grad.";
        if (typeof speakGerman === 'function') {
            speakGerman(fullReport, 0.9);
        }
    }

    // =========================================================================
    // SƠ ĐỒ V6: HỘI THOẠI PHÒNG THỬ ĐỒ (UMKLEIDEKABINE)
    // =========================================================================
    const DIALOGUES_V6 = [
        {
            title: "Hội thoại 1: Mua áo len (Suchen & Anprobieren)",
            lines: [
                { spk: "Verkäuferin", de: "Guten Tag! Suchen Sie etwas Bestimmtes?", vi: "Xin chào! Ngài tìm món nào cụ thể không ạ?" },
                { spk: "Kunde", de: "Ja, ich suche einen Pullover.", vi: "Có, tôi tìm một chiếc áo len." },
                { spk: "Verkäuferin", de: "Welche Größe haben Sie?", vi: "Ngài mặc cỡ nào?" },
                { spk: "Kunde", de: "Ich trage Größe achtundvierzig.", vi: "Tôi mặc cỡ bốn mươi tám." },
                { spk: "Verkäuferin", de: "Diesen hier haben wir in achtundvierzig. Wollen Sie ihn anprobieren?", vi: "Chiếc này đây chúng tôi có cỡ bốn mươi tám. Ngài có muốn thử không?" },
                { spk: "Kunde", de: "Ja, gern. Wo ist die Umkleidekabine?", vi: "Vâng, rất sẵn lòng. Phòng thử đồ ở đâu?" },
                { spk: "Verkäuferin", de: "Die Umkleidekabine ist dort hinten links.", vi: "Phòng thử đồ ở phía sau bên trái đằng kia ạ." }
            ]
        },
        {
            title: "Hội thoại 2: Đổi quần vì dài quá (Passen & Zu lang)",
            lines: [
                { spk: "Kundin", de: "Entschuldigung, ich habe diese Hose anprobiert. Sie passt mir nicht.", vi: "Xin lỗi, tôi đã thử chiếc quần này. Nó không vừa với tôi." },
                { spk: "Verkäufer", de: "Ist sie zu klein?", vi: "Nó chật quá phải không ạ?" },
                { spk: "Kundin", de: "Nein, sie ist zu lang.", vi: "Không, nó dài quá." },
                { spk: "Verkäufer", de: "Dann nehmen Sie diese hier. Sie ist kürzer.", vi: "Vậy bạn lấy chiếc này đây. Nó ngắn hơn." },
                { spk: "Kundin", de: "Danke, die passt mir gut. Die nehme ich.", vi: "Cảm ơn, chiếc này vừa với tôi. Tôi lấy chiếc này." },
                { spk: "Verkäufer", de: "Das macht neunundvierzig Euro.", vi: "Tổng cộng là bốn mươi chín euro." }
            ]
        }
    ];

    let b11_b11_currentV6DiagIndex = 0;
    let b11_b11_currentV6LineIndex = 0;

    function b11_b11_renderFittingRoomSvg() {
        const container = document.getElementById('b11-svg-v6-container');
        if (!container) return;

        const diag = DIALOGUES_V6[b11_currentV6DiagIndex];
        const line = diag.lines[b11_currentV6LineIndex];

        container.innerHTML = `
            <div class="p-5 sm:p-7 rounded-3xl bg-slate-900 text-white shadow-xl border border-slate-800 space-y-5">
                <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-1 rounded-lg bg-pink-500/20 text-pink-400 font-black text-xs">Sơ đồ V6</span>
                        <h3 class="text-base sm:text-lg font-black text-white">Hội Thoại Mua Quần Áo & Phòng Thử Đồ (Umkleidekabine)</h3>
                    </div>
                    <div class="flex items-center gap-2 text-xs">
                        <button type="button" onclick="b11_switchV6Diag(0)" class="px-3 py-1.5 rounded-lg font-bold transition cursor-pointer ${b11_currentV6DiagIndex === 0 ? 'bg-pink-600 text-white' : 'bg-slate-800 text-slate-300'}">
                            Hội thoại 1: Áo len
                        </button>
                        <button type="button" onclick="b11_switchV6Diag(1)" class="px-3 py-1.5 rounded-lg font-bold transition cursor-pointer ${b11_currentV6DiagIndex === 1 ? 'bg-pink-600 text-white' : 'bg-slate-800 text-slate-300'}">
                            Hội thoại 2: Đổi quần
                        </button>
                    </div>
                </div>

                <!-- Diễn biến hội thoại theo lượt -->
                <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-3">
                    <div class="flex items-center justify-between text-xs text-slate-400 border-b border-slate-800/80 pb-2">
                        <span class="font-bold text-pink-300">${diag.title}</span>
                        <span class="font-mono">Lượt ${b11_currentV6LineIndex + 1} / ${diag.lines.length}</span>
                    </div>

                    <div class="p-4 rounded-xl ${line.spk.includes('Verk') ? 'bg-indigo-950/40 border border-indigo-500/30' : 'bg-emerald-950/40 border border-emerald-500/30'} space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="px-2.5 py-0.5 rounded-md text-[11px] font-black uppercase ${line.spk.includes('Verk') ? 'bg-indigo-500/30 text-indigo-300' : 'bg-emerald-500/30 text-emerald-300'}">
                                ${line.spk}
                            </span>
                            <button type="button" onclick="speakGerman('${line.de.replace(/'/g, "\\'")}', 0.9)" class="text-white hover:text-pink-300 font-bold text-xs flex items-center gap-1 cursor-pointer">
                                🔊 Nghe lượt này
                            </button>
                        </div>
                        <div class="text-base sm:text-lg font-black text-white">„${line.de}“</div>
                        <div class="text-xs text-slate-300">📖 Dịch: ${line.vi}</div>
                    </div>

                    <!-- Nút bấm chuyển lượt -->
                    <div class="flex items-center justify-between pt-2">
                        <button type="button" onclick="b11_prevV6Line()" ${b11_currentV6LineIndex === 0 ? 'disabled class=\"opacity-40 cursor-not-allowed\"' : 'class=\"cursor-pointer hover:bg-slate-700\"'} class="px-3 py-1.5 rounded-xl bg-slate-800 text-xs font-bold text-slate-200 transition">
                            ◀ Lượt trước
                        </button>
                        <button type="button" onclick="b11_nextV6Line()" ${b11_currentV6LineIndex === diag.lines.length - 1 ? 'disabled class=\"opacity-40 cursor-not-allowed\"' : 'class=\"cursor-pointer hover:bg-slate-700\"'} class="px-3 py-1.5 rounded-xl bg-slate-800 text-xs font-bold text-slate-200 transition">
                            Lượt tiếp ▶
                        </button>
                    </div>
                </div>
            </div>
        `;
    }

    function b11_b11_switchV6Diag(idx) {
        b11_currentV6DiagIndex = idx;
        b11_currentV6LineIndex = 0;
        b11_renderFittingRoomSvg();
    }
    function b11_b11_prevV6Line() {
        if (b11_currentV6LineIndex > 0) {
            b11_currentV6LineIndex--;
            b11_renderFittingRoomSvg();
        }
    }
    function b11_b11_nextV6Line() {
        const diag = DIALOGUES_V6[b11_currentV6DiagIndex];
        if (b11_currentV6LineIndex < diag.lines.length - 1) {
            b11_currentV6LineIndex++;
            b11_renderFittingRoomSvg();
        }
    }

    // =========================================================================
    // KHỞI TẠO TẤT CẢ SƠ ĐỒ
    // =========================================================================
    function b11_initKleidungSvgDiagrams() {
        if (typeof currentLesson !== 'undefined' && currentLesson && currentLesson.id !== 25) {
            return;
        }
        b11_renderDiesTableSvg();
        b11_renderFarbeAkkusativSvg();
        b11_renderAkkDativFlowchartSvg();
        b11_renderKleiderschrankSvg();
        b11_renderWetterMapSvg();
        b11_renderFittingRoomSvg();
    }

    // Export ra Window (Toàn bộ hàm Bài 11 mang tiền tố b11_ để chống đụng độ)
    global.b11_renderDiesTableSvg = b11_renderDiesTableSvg;
    global.b11_renderFarbeAkkusativSvg = b11_renderFarbeAkkusativSvg;
    global.b11_renderAkkDativFlowchartSvg = b11_renderAkkDativFlowchartSvg;
    global.b11_renderKleiderschrankSvg = b11_renderKleiderschrankSvg;
    global.b11_renderWetterMapSvg = b11_renderWetterMapSvg;
    global.b11_renderFittingRoomSvg = b11_renderFittingRoomSvg;
    global.b11_initKleidungSvgDiagrams = b11_initKleidungSvgDiagrams;
    global.initKleidungSvgDiagrams = b11_initKleidungSvgDiagrams; // Alias cho index.html
    global.b11_selectV1Noun = b11_selectV1Noun;
    global.b11_prevV1Noun = b11_prevV1Noun;
    global.b11_nextV1Noun = b11_nextV1Noun;
    global.b11_setV1Case = b11_setV1Case;
    global.b11_selectV2Item = b11_selectV2Item;
    global.b11_selectV2Color = b11_selectV2Color;
    global.b11_selectV4Item = b11_selectV4Item;
    global.b11_selectCity = b11_selectCity;
    global.b11_readFullWeatherReport = b11_readFullWeatherReport;
    global.b11_switchV6Diag = b11_switchV6Diag;
    global.b11_prevV6Line = b11_prevV6Line;
    global.b11_nextV6Line = b11_nextV6Line;

})(typeof window !== 'undefined' ? window : this);
