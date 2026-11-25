/**
 * DeutschMeister - Module Sơ Đồ Trực Quan & Tương Tác Bài 13 (A1)
 * "Ôn tập tổng hợp A1: Động từ bất quy tắc, W-Fragen & Giao tiếp quán Cafe"
 * 
 * V1: Cỗ máy Vokalwechsel 7 động từ bất quy tắc (a→ä, e→i, e→ie & Bẫy ngôi ihr)
 * V2: Bản đồ tương tác W-Fragen & Giới từ (Woher -> aus, Wo -> in, Wie -> Name, Was -> Dinge, Wann -> Zeit)
 */

(function (global) {
    'use strict';

    // =========================================================================
    // V1: CỖ MÁY VOKALWECHSEL (ĐỔI NGUYÊN ÂM GỐC) 7 ĐỘNG TỪ BẤT QUY TẮC
    // =========================================================================
    const V1_VERBS = {
        "lesen": {
            infinitiv: "lesen",
            meaning: "đọc",
            type: "e → ie",
            baseVowel: "e",
            shiftedVowel: "ie",
            forms: { ich: "lese", du: "liest", er_sie_es: "liest", wir: "lesen", ihr: "lest", sie_Sie: "lesen" },
            note: "Vokalwechsel (đổi nguyên âm gốc) e → ie CHỈ ở ngôi du và er/sie/es. Gốc đã kết thúc bằng s nên du chỉ thêm -t (lies + t = liest). Ngôi ihr KHÔNG đổi (lest).",
            examples: {
                ich: { de: "Ich lese am Abend ein Buch.", vi: "Buổi tối tôi đọc một quyển sách." },
                du: { de: "Liest du gern Romane oder Zeitungen?", vi: "Bạn thích đọc tiểu thuyết hay báo?" },
                er_sie_es: { de: "Das Mädchen liest das Buch.", vi: "Cô bé đọc quyển sách." },
                wir: { de: "Wir lesen zusammen die Speisekarte.", vi: "Chúng tôi cùng nhau đọc thực đơn." },
                ihr: { de: "Lest ihr heute einen langen Brief?", vi: "Hôm nay các bạn có đọc một bức thư dài không?" },
                sie_Sie: { de: "Herr Weber, lesen Sie oft die Zeitung?", vi: "Ông Weber, ông có thường đọc báo không?" }
            }
        },
        "fahren": {
            infinitiv: "fahren",
            meaning: "lái xe, đi",
            type: "a → ä",
            baseVowel: "a",
            shiftedVowel: "ä",
            forms: { ich: "fahre", du: "fährst", er_sie_es: "fährt", wir: "fahren", ihr: "fahrt", sie_Sie: "fahren" },
            note: "Vokalwechsel a → ä CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG đổi nguyên âm (fahrt).",
            examples: {
                ich: { de: "Ich fahre mit dem Zug nach Hamburg.", vi: "Tôi đi tàu hỏa tới Hamburg." },
                du: { de: "Fährst du am Wochenende nach Berlin?", vi: "Cuối tuần bạn có đi Berlin không?" },
                er_sie_es: { de: "Mein Bruder fährt am Sonntag nach München.", vi: "Anh trai tôi đi München vào Chủ nhật." },
                wir: { de: "Wir fahren nach Polen.", vi: "Chúng tôi đi tới Ba Lan." },
                ihr: { de: "Wann fahrt ihr nach Hause?", vi: "Khi nào các bạn về nhà?" },
                sie_Sie: { de: "Fahren Sie morgen in die Schweiz?", vi: "Ngày mai ngài có đi Thụy Sĩ không?" }
            }
        },
        "schlafen": {
            infinitiv: "schlafen",
            meaning: "ngủ",
            type: "a → ä",
            baseVowel: "a",
            shiftedVowel: "ä",
            forms: { ich: "schlafe", du: "schläfst", er_sie_es: "schläft", wir: "schlafen", ihr: "schlaft", sie_Sie: "schlafen" },
            note: "Vokalwechsel a → ä CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG đổi nguyên âm (schlaft).",
            examples: {
                ich: { de: "Ich schlafe heute sehr gut.", vi: "Hôm nay tôi ngủ rất ngon." },
                du: { de: "Schläfst du im Hotel?", vi: "Bạn có ngủ ở khách sạn không?" },
                er_sie_es: { de: "Der Hund schläft gemütlich auf dem Sofa.", vi: "Chú chó ngủ thoải mái trên ghế sofa." },
                wir: { de: "Wir schlafen heute im Hotel.", vi: "Hôm nay chúng tôi ngủ ở khách sạn." },
                ihr: { de: "Ihr schlaft am Wochenende zu lange!", vi: "Các bạn ngủ quá lâu vào cuối tuần!" },
                sie_Sie: { de: "Die Kinder schlafen im Schlafzimmer.", vi: "Bọn trẻ ngủ trong phòng ngủ." }
            }
        },
        "sprechen": {
            infinitiv: "sprechen",
            meaning: "nói",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "spreche", du: "sprichst", er_sie_es: "spricht", wir: "sprechen", ihr: "sprecht", sie_Sie: "sprechen" },
            note: "Vokalwechsel e → i CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG đổi nguyên âm (sprecht).",
            examples: {
                ich: { de: "Ich spreche ein bisschen Deutsch.", vi: "Tôi nói một chút tiếng Đức." },
                du: { de: "Du sprichst zu leise.", vi: "Bạn nói quá nhỏ." },
                er_sie_es: { de: "Der Lehrer spricht zu leise.", vi: "Thầy giáo nói quá nhỏ." },
                wir: { de: "Wir sprechen im Deutschkurs viel Deutsch.", vi: "Chúng tôi nói nhiều tiếng Đức trong lớp học." },
                ihr: { de: "Sprecht ihr Englisch oder Französisch?", vi: "Các bạn nói tiếng Anh hay tiếng Pháp?" },
                sie_Sie: { de: "Die Touristen sprechen sehr deutlich.", vi: "Các du khách nói rất rõ ràng." }
            }
        },
        "treffen": {
            infinitiv: "treffen",
            meaning: "gặp gỡ",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "treffe", du: "triffst", er_sie_es: "trifft", wir: "treffen", ihr: "trefft", sie_Sie: "treffen" },
            note: "Vokalwechsel e → i CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG đổi nguyên âm (trefft).",
            examples: {
                ich: { de: "Heute treffe ich meine Freunde.", vi: "Hôm nay tôi gặp bạn bè của mình." },
                du: { de: "Wann triffst du deine Freunde im Café?", vi: "Khi nào bạn gặp bạn bè ở quán cà phê?" },
                er_sie_es: { de: "Am Nachmittag trifft Anna ihre Freunde im Café.", vi: "Vào buổi chiều, Anna gặp bạn bè ở quán cà phê." },
                wir: { de: "Wir treffen uns um 15 Uhr im Café.", vi: "Chúng tôi gặp nhau lúc 15 giờ ở quán cà phê." },
                ihr: { de: "Wann trefft ihr eure Freunde?", vi: "Khi nào các bạn gặp bạn bè của mình?" },
                sie_Sie: { de: "Sie treffen Maria am Bahnhof.", vi: "Họ gặp Maria ở nhà ga." }
            }
        },
        "essen": {
            infinitiv: "essen",
            meaning: "ăn",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "esse", du: "isst", er_sie_es: "isst", wir: "essen", ihr: "esst", sie_Sie: "essen" },
            note: "Vokalwechsel e → i CHỈ ở ngôi du và er/sie/es (du isst / er isst). Gốc kết thúc bằng s/ss nên du chỉ thêm -t. Ngôi ihr KHÔNG đổi (esst).",
            examples: {
                ich: { de: "Ich esse gern Eis.", vi: "Tôi thích ăn kem." },
                du: { de: "Was isst du heute zum Frühstück?", vi: "Hôm nay bạn ăn gì vào bữa sáng?" },
                er_sie_es: { de: "Das Kind isst ein Eis.", vi: "Đứa trẻ ăn một cây kem." },
                wir: { de: "Wir essen im Sommer gern Eis.", vi: "Vào mùa hè chúng tôi thích ăn kem." },
                ihr: { de: "Esst ihr gern frischen Käse und Salat?", vi: "Các bạn có thích ăn phô mai tươi và xà lách không?" },
                sie_Sie: { de: "Die Kinder essen Eis.", vi: "Bọn trẻ đang ăn kem." }
            }
        },
        "geben": {
            infinitiv: "geben",
            meaning: "cho, đưa",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "gebe", du: "gibst", er_sie_es: "gibt", wir: "geben", ihr: "gebt", sie_Sie: "geben" },
            note: "Vokalwechsel e → i CHỈ ở ngôi du và er/sie/es (du gibst / er gibt). Ngôi ihr KHÔNG đổi nguyên âm (gebt).",
            examples: {
                ich: { de: "Ich gebe dem Hund das Futter.", vi: "Tôi cho chú chó ăn thức ăn." },
                du: { de: "Gibst du mir bitte den Zucker?", vi: "Bạn làm ơn đưa cho tôi đường được không?" },
                er_sie_es: { de: "Hannes gibt dem Hund das Futter.", vi: "Hannes cho chú chó ăn thức ăn." },
                wir: { de: "Wir geben dir das Buch.", vi: "Chúng tôi đưa cho bạn quyển sách." },
                ihr: { de: "Gebt ihr dem Lehrer den Brief?", vi: "Các bạn đưa bức thư cho thầy giáo phải không?" },
                sie_Sie: { de: "Hannes und Julia geben dem Hund das Futter.", vi: "Hannes và Julia cho chú chó thức ăn." }
            }
        }
    };

    const PRONOUNS = [
        { key: "ich", label: "ich (tôi)", isShifted: false, note: "Giữ nguyên âm gốc + đuôi -e" },
        { key: "du", label: "du (bạn)", isShifted: true, note: "🔥 VOKALWECHSEL: Đổi nguyên âm gốc + đuôi -st (hoặc -t nếu gốc -s/-ß/-z)" },
        { key: "er_sie_es", label: "er/sie/es (anh/cô ấy/nó)", isShifted: true, note: "🔥 VOKALWECHSEL: Đổi nguyên âm gốc + đuôi -t" },
        { key: "wir", label: "wir (chúng tôi)", isShifted: false, note: "Giữ nguyên thể đuôi -en" },
        { key: "ihr", label: "ihr (các bạn)", isShifted: false, isGoldWarning: true, note: "⚠️ QUY TẮC VÀNG: KHÔNG biến âm! Giữ nguyên âm gốc + đuôi -t" },
        { key: "sie_Sie", label: "sie / Sie (họ / Ngài)", isShifted: false, note: "Giữ nguyên thể đuôi -en" }
    ];

    let currentV1Verb = "lesen";
    let currentV1Pronoun = "du";

    function b13_renderVowelShiftMachine(containerId) {
        const c = document.getElementById(containerId || "b13-svg-v1-container");
        if (!c) return;

        const verbData = V1_VERBS[currentV1Verb] || V1_VERBS["lesen"];
        const curPron = PRONOUNS.find(p => p.key === currentV1Pronoun) || PRONOUNS[1];
        const conjugatedForm = verbData.forms[currentV1Pronoun] || "";
        const isShifted = curPron.isShifted;
        const isIhr = curPron.key === "ihr";
        const curExample = (verbData.examples && verbData.examples[curPron.key])
            ? verbData.examples[curPron.key]
            : { de: "", vi: "" };

        const safeConjugationSpeak = `${curPron.key === 'er_sie_es' ? 'er' : (curPron.key === 'sie_Sie' ? 'Sie' : curPron.key)} ${conjugatedForm}`.replace(/'/g, "\\'");
        const safeExampleSpeak = curExample.de.replace(/[„“"]/g, '').replace(/'/g, "\\'");

        c.innerHTML = `
            <div class="p-4 sm:p-6 rounded-3xl bg-slate-900 border border-amber-500/40 text-white shadow-2xl space-y-5">
                <!-- Header -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 border-b border-slate-800 pb-4">
                    <div class="flex flex-wrap items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-300 font-bold text-xs uppercase tracking-wider whitespace-nowrap shrink-0">
                            ⚙️ Sơ đồ V1: Cỗ Máy Vokalwechsel
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Quy Tắc Vàng Động Từ Bất Quy Tắc (A1)</h4>
                    </div>
                    <span class="text-xs text-amber-300/90 font-medium">💡 Đổi nguyên âm CHỈ ở du & er/sie/es • Ngôi ihr KHÔNG biến âm!</span>
                </div>

                <!-- Bộ chọn 7 Động từ -->
                <div class="space-y-2">
                    <div class="text-xs font-bold text-slate-300 uppercase tracking-wider flex flex-wrap items-center justify-between gap-2">
                        <span>1. Chọn động từ bất quy tắc cần khảo sát:</span>
                        <span class="text-amber-300 font-mono text-xs px-2 py-0.5 rounded bg-amber-500/10 border border-amber-500/30">Vokalwechsel: ${verbData.type}</span>
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2">
                        ${Object.keys(V1_VERBS).map(vk => {
                            const v = V1_VERBS[vk];
                            const isSel = vk === currentV1Verb;
                            return `
                                <button type="button" onclick="b13_selectVerb('${vk}')"
                                    class="p-2.5 rounded-xl border text-center transition cursor-pointer flex flex-col items-center justify-center ${
                                        isSel
                                            ? 'bg-amber-500 text-slate-950 font-black border-amber-400 shadow-md shadow-amber-500/20 scale-[1.02]'
                                            : 'bg-slate-800/90 hover:bg-slate-800 border-slate-700 text-slate-200 font-semibold'
                                    }">
                                    <span class="text-sm font-bold font-mono">${v.infinitiv}</span>
                                    <span class="text-[11px] ${isSel ? 'text-slate-900 font-bold' : 'text-slate-400'}">(${v.meaning})</span>
                                </button>
                            `;
                        }).join('')}
                    </div>
                </div>

                <!-- 6 Bóng đèn ngôi xưng -->
                <div class="space-y-2">
                    <div class="text-xs font-bold text-slate-300 uppercase tracking-wider">
                        2. Bấm chọn ngôi nhân xưng để xem dạng chia & ví dụ tương ứng:
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
                        ${PRONOUNS.map(p => {
                            const isSel = p.key === currentV1Pronoun;
                            let bulbClass = "border-slate-700 bg-slate-800/70 text-slate-200 hover:bg-slate-800";
                            let icon = "⚪";
                            let badgeTag = "Có quy tắc";
                            let badgeTagClass = "text-slate-300";

                            if (p.isShifted) {
                                bulbClass = isSel
                                    ? "border-rose-500 bg-rose-950/80 text-rose-100 ring-2 ring-rose-500/60 shadow-lg shadow-rose-900/40"
                                    : "border-rose-900/50 bg-rose-950/25 text-rose-200 hover:bg-rose-950/45";
                                icon = "🔴";
                                badgeTag = "🔥 Đổi nguyên âm";
                                badgeTagClass = "text-rose-300 font-bold";
                            } else if (p.isGoldWarning) {
                                bulbClass = isSel
                                    ? "border-emerald-500 bg-emerald-950/80 text-emerald-100 ring-2 ring-emerald-500/60 shadow-lg shadow-emerald-900/40"
                                    : "border-emerald-900/50 bg-emerald-950/25 text-emerald-200 hover:bg-emerald-950/45";
                                icon = "🟢";
                                badgeTag = "KHÔNG biến âm";
                                badgeTagClass = "text-emerald-300 font-extrabold";
                            } else if (isSel) {
                                bulbClass = "border-sky-500 bg-sky-950/80 text-sky-100 ring-2 ring-sky-500/60";
                                icon = "🔵";
                                badgeTag = "Giữ nguyên gốc";
                                badgeTagClass = "text-sky-300 font-bold";
                            }

                            return `
                                <button type="button" onclick="b13_selectPronoun('${p.key}')"
                                    class="p-3 rounded-2xl border text-left transition cursor-pointer flex flex-col justify-between gap-1.5 min-w-0 ${bulbClass}">
                                    <div class="flex items-center justify-between gap-1">
                                        <span class="text-xs font-black">${p.label.split(' ')[0]}</span>
                                        <span class="text-xs shrink-0">${icon}</span>
                                    </div>
                                    <div class="text-sm font-black font-mono tracking-wide break-words">
                                        ${verbData.forms[p.key]}
                                    </div>
                                    <span class="text-[11px] leading-tight block ${badgeTagClass}">
                                        ${badgeTag}
                                    </span>
                                </button>
                            `;
                        }).join('')}
                    </div>
                </div>

                <!-- Bảng hiển thị kết quả Cỗ máy -->
                <div class="p-4 sm:p-5 rounded-2xl border ${
                    isShifted
                        ? 'bg-gradient-to-r from-rose-950/70 to-slate-900 border-rose-500/50 shadow-inner'
                        : (isIhr 
                            ? 'bg-gradient-to-r from-emerald-950/70 to-slate-900 border-emerald-500/50 shadow-inner'
                            : 'bg-slate-800/70 border-slate-700')
                } space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div class="space-y-1">
                            <span class="text-xs uppercase font-extrabold tracking-wider ${
                                isShifted ? 'text-rose-400' : (isIhr ? 'text-emerald-400' : 'text-sky-400')
                            }">
                                ${isShifted ? '🚨 VOKALWECHSEL: NGUYÊN ÂM ĐÃ BIẾN ĐỔI!' : (isIhr ? '🛡️ CHỐNG BẪY NGÔI IHR: KHÔNG BIẾN ÂM!' : 'ℹ️ DẠNG CHIA NGUYÊN ÂM GỐC')}
                            </span>
                            <div class="flex items-center gap-3 flex-wrap">
                                <span class="text-2xl sm:text-3xl font-black text-white font-mono">
                                    <span class="text-slate-300">${curPron.label.split(' ')[0]}</span>
                                    <span class="${isShifted ? 'text-rose-300 underline decoration-rose-500 decoration-2' : (isIhr ? 'text-emerald-300 font-black' : 'text-amber-300')}">${conjugatedForm}</span>
                                </span>
                                <button type="button" onclick="b13_speakGerman('${safeConjugationSpeak}')"
                                    class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-600 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                    🔊 Nghe
                                </button>
                            </div>
                        </div>

                        <div class="p-3 rounded-xl bg-slate-950/70 border border-slate-800 text-xs space-y-1 max-w-sm">
                            <div class="font-bold text-slate-300">Quy tắc áp dụng:</div>
                            <div class="${isShifted ? 'text-rose-200 font-semibold' : (isIhr ? 'text-emerald-200 font-bold' : 'text-slate-300')}">
                                ${curPron.note}
                            </div>
                        </div>
                    </div>

                    <!-- Ví dụ thực tế đổi theo đúng ngôi đang chọn -->
                    <div class="pt-3 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                        <div class="space-y-1">
                            <div class="text-slate-200 font-medium">
                                <span class="text-amber-400 font-bold">Ví dụ (ngôi ${curPron.label.split(' ')[0]}):</span>
                                <span class="italic font-serif text-sm text-white">„${curExample.de}“</span>
                            </div>
                            <div class="text-slate-300 italic">${curExample.vi}</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('${safeExampleSpeak}')"
                            class="px-3 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-200 border border-amber-500/40 font-bold text-xs shrink-0 transition flex items-center gap-1 cursor-pointer self-start sm:self-center">
                            🔊 Đọc cả câu
                        </button>
                    </div>
                </div>
            </div>
        `;
    }

    function b13_selectVerb(verbKey) {
        if (V1_VERBS[verbKey]) {
            currentV1Verb = verbKey;
            b13_renderVowelShiftMachine();
        }
    }

    function b13_selectPronoun(pronounKey) {
        currentV1Pronoun = pronounKey;
        b13_renderVowelShiftMachine();
    }

    // =========================================================================
    // V2: BẢN ĐỒ W-FRAGEN & GIỚI TỪ (Woher -> aus, Wo -> in, Wie, Was, Wann)
    // =========================================================================
    const V2_QUESTIONS = {
        "Woher": {
            word: "Woher",
            meaning: "Từ đâu (quê quán, xuất xứ)",
            targetPrep: "aus / aus der / aus den",
            prepMeaning: "từ (thành phố / quốc gia)",
            category: "Quê quán / Xuất xứ",
            dialogue: {
                question: "Woher kommen Sie?",
                question_vi: "Ngài đến từ đâu?",
                answer: "Ich komme aus der Türkei / aus Deutschland.",
                answer_vi: "Tôi đến từ Thổ Nhĩ Kỳ / từ nước Đức."
            },
            rule: "Thường đi với „aus“. Nước có mạo từ dùng aus der / aus den: aus der Türkei, aus der Schweiz, aus den USA. Nước không mạo từ: aus Deutschland, aus Vietnam, aus Polen.",
            colorClass: "rose"
        },
        "Wo": {
            word: "Wo",
            meaning: "Ở đâu (nơi chốn, cư trú)",
            targetPrep: "in / am / zu / bei",
            prepMeaning: "ở, tại (thành phố, địa điểm)",
            category: "Nơi sinh sống / Vị trí",
            dialogue: {
                question: "Wo wohnen Sie?",
                question_vi: "Ngài sống ở đâu?",
                answer: "Ich wohne in Berlin.",
                answer_vi: "Tôi sống ở Berlin."
            },
            rule: "Thường đi với „in“ + thành phố / nước (in Berlin). Cũng gặp am Bahnhof (ở nhà ga), zu Hause (ở nhà), bei Freunden (ở nhà bạn bè).",
            colorClass: "blue"
        },
        "Wie": {
            word: "Wie",
            meaning: "Như thế nào (Hỏi Tên / Tính chất)",
            targetPrep: "Name / Tính chất",
            prepMeaning: "Tên riêng hoặc đặc điểm",
            category: "Tên & Danh tính",
            dialogue: {
                question: "Wie heißen Sie?",
                question_vi: "Ngài tên là gì?",
                answer: "Ich heiße Anna.",
                answer_vi: "Tôi tên là Anna."
            },
            rule: "Hỏi tên dùng „Wie heißen Sie?“ / „Wie ist Ihr Name?“. KHÔNG dùng „Was ist dein Name?“.",
            colorClass: "amber"
        },
        "Was": {
            word: "Was",
            meaning: "Cái gì (Hỏi Đồ vật / Đồ uống / Hoạt động)",
            targetPrep: "Đồ ăn / Đồ uống / Sự vật",
            prepMeaning: "Kaffee, Tee, Eis, Salat...",
            category: "Giao tiếp quán Cafe",
            dialogue: {
                question: "Was möchten Sie trinken?",
                question_vi: "Ngài muốn uống gì ạ?",
                answer: "Ich möchte Kaffee trinken.",
                answer_vi: "Tôi muốn uống cà phê."
            },
            rule: "Hỏi sự vật, món ăn, thức uống hoặc hành động: „Was trinken Sie?“, „Was isst du gern?“, „Was machen Sie?“.",
            colorClass: "purple"
        },
        "Wann": {
            word: "Wann",
            meaning: "Khi nào (Thời gian)",
            targetPrep: "am / um / hôm nay...",
            prepMeaning: "am Wochenende, um 15 Uhr",
            category: "Thời gian",
            dialogue: {
                question: "Wann triffst du deine Freunde?",
                question_vi: "Khi nào bạn gặp bạn bè của mình?",
                answer: "Am Wochenende um 15 Uhr.",
                answer_vi: "Vào cuối tuần lúc 15 giờ."
            },
            rule: "Wann hỏi thời điểm: thường trả lời với „am“ (am Wochenende, am Abend) hoặc „um“ (um 15 Uhr).",
            colorClass: "emerald"
        }
    };

    let currentV2Key = "Woher";

    function b13_renderWFragenMap(containerId) {
        const c = document.getElementById(containerId || "b13-svg-v2-container");
        if (!c) return;

        const qData = V2_QUESTIONS[currentV2Key] || V2_QUESTIONS["Woher"];
        const safeQ = qData.dialogue.question.replace(/[„“"]/g, '').replace(/'/g, "\\'");
        const safeA = qData.dialogue.answer.replace(/[„“"]/g, '').replace(/'/g, "\\'");
        const safeBoth = `${qData.dialogue.question} ${qData.dialogue.answer}`.replace(/[„“"]/g, '').replace(/'/g, "\\'");

        c.innerHTML = `
            <div class="p-4 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/40 text-white shadow-2xl space-y-5">
                <!-- Header -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 border-b border-slate-800 pb-4">
                    <div class="flex flex-wrap items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/40 text-indigo-300 font-bold text-xs uppercase tracking-wider whitespace-nowrap shrink-0">
                            🗺️ Sơ đồ V2: W-Fragen &amp; Giới Từ
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Bản Đồ Đặt Câu Hỏi &amp; Giới Từ Đi Kèm (A1)</h4>
                    </div>
                    <span class="text-xs text-indigo-300/90 font-medium whitespace-nowrap">💡 Woher • Wo • Wie • Was • Wann</span>
                </div>

                <!-- 5 Nút W-Fragen -->
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2.5">
                    ${Object.keys(V2_QUESTIONS).map(qk => {
                        const q = V2_QUESTIONS[qk];
                        const isSel = qk === currentV2Key;
                        return `
                            <button type="button" onclick="b13_selectWFrage('${qk}')"
                                class="p-3 rounded-2xl border text-center transition cursor-pointer flex flex-col items-center justify-center gap-1 min-w-0 ${
                                    isSel
                                        ? 'bg-indigo-600 text-white font-black border-indigo-400 ring-2 ring-indigo-400/50 shadow-lg shadow-indigo-600/30 scale-[1.02]'
                                        : 'bg-slate-800/90 hover:bg-slate-800 border-slate-700 text-slate-200'
                                }">
                                <span class="text-base font-black font-mono">${q.word}?</span>
                                <span class="text-[11px] leading-tight ${isSel ? 'text-indigo-100' : 'text-slate-400'}">${q.category}</span>
                            </button>
                        `;
                    }).join('')}
                </div>

                <!-- Sơ đồ Luồng Trực Quan -->
                <div class="p-4 sm:p-5 rounded-2xl bg-slate-950/80 border border-slate-800 space-y-4">
                    <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                        <!-- Khối Câu Hỏi -->
                        <div class="w-full md:w-5/12 p-4 rounded-xl bg-indigo-950/60 border border-indigo-500/40 text-center space-y-1">
                            <span class="text-[10px] font-black uppercase tracking-wider text-indigo-300 block">Từ Để Hỏi (W-Frage)</span>
                            <div class="text-2xl font-black text-indigo-200 font-mono">${qData.word}?</div>
                            <div class="text-xs text-slate-300">Ý nghĩa: <b class="text-white">${qData.meaning}</b></div>
                        </div>

                        <!-- Mũi tên liên kết -->
                        <div class="flex flex-col items-center justify-center shrink-0">
                            <div class="text-xs font-bold text-amber-300 font-mono px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30 whitespace-nowrap">
                                THƯỜNG ĐI KÈM ➔
                            </div>
                        </div>

                        <!-- Khối Giới Từ / Trả Lời -->
                        <div class="w-full md:w-5/12 p-4 rounded-xl bg-emerald-950/60 border border-emerald-500/40 text-center space-y-1">
                            <span class="text-[10px] font-black uppercase tracking-wider text-emerald-300 block">Giới Từ / Thành Phần Trả Lời</span>
                            <div class="text-xl sm:text-2xl font-black text-emerald-200 font-mono">${qData.targetPrep}</div>
                            <div class="text-xs text-slate-300">Đặc điểm: <b class="text-white">${qData.prepMeaning}</b></div>
                        </div>
                    </div>

                    <!-- Khung Phân tích Logic & Quy tắc -->
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs flex items-start gap-2.5">
                        <span class="text-base shrink-0">📌</span>
                        <div class="space-y-0.5">
                            <span class="font-bold text-amber-300">Ghi nhớ trọng tâm:</span>
                            <p class="text-slate-200 leading-relaxed">${qData.rule}</p>
                        </div>
                    </div>

                    <!-- Mẫu Hội Thoại Mẫu -->
                    <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2">
                        <div class="text-xs font-bold text-indigo-300 uppercase tracking-wider flex flex-wrap items-center justify-between gap-2">
                            <span>Mẫu Hội Thoại Thực Tế:</span>
                            <button type="button" onclick="b13_speakGerman('${safeBoth}')"
                                class="px-2.5 py-1 rounded-lg bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-200 border border-indigo-500/40 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                🔊 Nghe hỏi &amp; đáp
                            </button>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                            <div class="p-3 rounded-lg bg-slate-950 border border-slate-800/80 space-y-1">
                                <div class="flex items-center justify-between gap-2">
                                    <span class="font-bold text-indigo-300">Hỏi:</span>
                                    <button type="button" onclick="b13_speakGerman('${safeQ}')" class="text-slate-300 hover:text-indigo-300 cursor-pointer" title="Nghe câu hỏi">🔊</button>
                                </div>
                                <div class="font-mono text-sm text-white">„${qData.dialogue.question}“</div>
                                <div class="text-slate-300 italic">${qData.dialogue.question_vi}</div>
                            </div>
                            <div class="p-3 rounded-lg bg-slate-950 border border-slate-800/80 space-y-1">
                                <div class="flex items-center justify-between gap-2">
                                    <span class="font-bold text-emerald-300">Đáp:</span>
                                    <button type="button" onclick="b13_speakGerman('${safeA}')" class="text-slate-300 hover:text-emerald-300 cursor-pointer" title="Nghe câu trả lời">🔊</button>
                                </div>
                                <div class="font-mono text-sm text-white">„${qData.dialogue.answer}“</div>
                                <div class="text-slate-300 italic">${qData.dialogue.answer_vi}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    function b13_selectWFrage(wKey) {
        if (V2_QUESTIONS[wKey]) {
            currentV2Key = wKey;
            b13_renderWFragenMap();
        }
    }

    // =========================================================================
    // HỘI THOẠI 7 DÒNG "KAFFEE ODER TEE" - PHÁT TUẦN TỰ TỪNG DÒNG
    // =========================================================================
    const B13_CAFE_DIALOGUE_LINES = [
        "Entschuldigung, ist hier frei?",
        "Ja klar, bitte.",
        "Ich bin John aus Frankreich, und du?",
        "Ich heiße Maria. Ich komme aus Polen.",
        "Was trinkst du: Kaffee oder Tee?",
        "Kaffee.",
        "Zwei Kaffee, bitte!"
    ];

    let cafeDlgPlaying = false;
    let cafeDlgSeqToken = 0;

    function b13_clearCafeLineHighlights() {
        for (let i = 0; i < B13_CAFE_DIALOGUE_LINES.length; i++) {
            const el = document.getElementById(`b13-cafe-line-${i}`);
            if (el) {
                el.classList.remove("ring-2", "ring-amber-500", "bg-amber-50");
            }
        }
    }

    function b13_playCafeDialogue() {
        if (typeof window === 'undefined') return;
        const token = ++cafeDlgSeqToken;
        cafeDlgPlaying = true;
        b13_clearCafeLineHighlights();

        const btn = document.getElementById("b13-cafe-play-all-btn");
        if (btn) btn.innerText = "⏸ Đang đọc hội thoại...";

        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const voice = typeof getBestGermanVoice === 'function' ? getBestGermanVoice() : null;

            const playNext = (idx) => {
                if (token !== cafeDlgSeqToken) return;
                if (idx >= B13_CAFE_DIALOGUE_LINES.length) {
                    cafeDlgPlaying = false;
                    b13_clearCafeLineHighlights();
                    if (btn) btn.innerText = "🔊 Nghe cả hội thoại";
                    return;
                }
                b13_clearCafeLineHighlights();
                const lineEl = document.getElementById(`b13-cafe-line-${idx}`);
                if (lineEl) lineEl.classList.add("ring-2", "ring-amber-500", "bg-amber-50");

                const u = new SpeechSynthesisUtterance(B13_CAFE_DIALOGUE_LINES[idx]);
                u.lang = 'de-DE';
                u.rate = 0.9;
                u.pitch = 1.0;
                if (voice) u.voice = voice;
                u.onend = () => playNext(idx + 1);
                u.onerror = () => playNext(idx + 1);
                window.speechSynthesis.speak(u);
            };
            playNext(0);
        } else if (typeof speakGerman === 'function') {
            speakGerman(B13_CAFE_DIALOGUE_LINES.join(" "));
            if (btn) btn.innerText = "🔊 Nghe cả hội thoại";
        }
    }

    // =========================================================================
    // TTS AUDIO HELPER (SẠCH TIẾNG ĐỨC)
    // =========================================================================
    function b13_speakGerman(text) {
        cafeDlgSeqToken++;
        b13_clearCafeLineHighlights();
        const btn = document.getElementById("b13-cafe-play-all-btn");
        if (btn) btn.innerText = "🔊 Nghe cả hội thoại";

        const clean = String(text || '').replace(/[„“"]/g, '').trim();
        if (!clean) return;
        if (typeof speakGerman === 'function') {
            speakGerman(clean);
        } else if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            const u = new SpeechSynthesisUtterance(clean);
            u.lang = 'de-DE';
            window.speechSynthesis.speak(u);
        }
    }

    // =========================================================================
    // INIT FUNCTION
    // =========================================================================
    function b13_initReviewSvgDiagrams() {
        b13_renderVowelShiftMachine();
        b13_renderWFragenMap();
    }

    // Export ra Window
    global.b13_renderVowelShiftMachine = b13_renderVowelShiftMachine;
    global.b13_selectVerb = b13_selectVerb;
    global.b13_selectPronoun = b13_selectPronoun;
    global.b13_renderWFragenMap = b13_renderWFragenMap;
    global.b13_selectWFrage = b13_selectWFrage;
    global.b13_playCafeDialogue = b13_playCafeDialogue;
    global.b13_speakGerman = b13_speakGerman;
    global.b13_initReviewSvgDiagrams = b13_initReviewSvgDiagrams;
    global.initReviewSvgDiagrams = b13_initReviewSvgDiagrams;

})(typeof window !== 'undefined' ? window : this);
