/**
 * DeutschMeister - Module Sơ Đồ Trực Quan & Tương Tác Bài 13 (A1)
 * "Ôn tập tổng hợp A1: Động từ bất quy tắc, W-Fragen & Giao tiếp quán Cafe"
 * 
 * V1: Cỗ máy biến âm 7 động từ (Vowel-Shift Machine: a→ä, e→i, e→ie & Bẫy ngôi ihr)
 * V2: Bản đồ tương tác W-Fragen & Giới từ (Wo -> in, Woher -> aus, Wie -> Name, Was -> Dinge)
 */

(function (global) {
    'use strict';

    // =========================================================================
    // V1: CỖ MÁY BIẾN ÂM 7 ĐỘNG TỪ BẤT QUY TẮC
    // =========================================================================
    const V1_VERBS = {
        "lesen": {
            infinitiv: "lesen",
            meaning: "đọc",
            type: "e → ie",
            baseVowel: "e",
            shiftedVowel: "ie",
            forms: { ich: "lese", du: "liest", er_sie_es: "liest", wir: "lesen", ihr: "lest", sie_Sie: "lesen" },
            note: "Biến âm e → ie CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG biến âm (lest).",
            example: "Jeden Abend liest mein Großvater die Zeitung.",
            example_vi: "Mỗi tối ông tôi đều đọc báo."
        },
        "fahren": {
            infinitiv: "fahren",
            meaning: "lái xe, đi",
            type: "a → ä",
            baseVowel: "a",
            shiftedVowel: "ä",
            forms: { ich: "fahre", du: "fährst", er_sie_es: "fährt", wir: "fahren", ihr: "fahrt", sie_Sie: "fahren" },
            note: "Biến âm a → ä CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG biến âm (fahrt).",
            example: "Fährst du am Wochenende mit dem Zug nach Berlin?",
            example_vi: "Cuối tuần bạn có đi tàu tới Berlin không?"
        },
        "schlafen": {
            infinitiv: "schlafen",
            meaning: "ngủ",
            type: "a → ä",
            baseVowel: "a",
            shiftedVowel: "ä",
            forms: { ich: "schlafe", du: "schläfst", er_sie_es: "schläft", wir: "schlafen", ihr: "schlaft", sie_Sie: "schlafen" },
            note: "Biến âm a → ä CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG biến âm (schlaft).",
            example: "Warum schläfst du heute im Hotel und nicht zu Hause?",
            example_vi: "Tại sao hôm nay bạn lại ngủ ở khách sạn mà không phải ở nhà?"
        },
        "sprechen": {
            infinitiv: "sprechen",
            meaning: "nói",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "spreche", du: "sprichst", er_sie_es: "spricht", wir: "sprechen", ihr: "sprecht", sie_Sie: "sprechen" },
            note: "Biến âm e → i CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG biến âm (sprecht).",
            example: "Die Lehrerin spricht sehr laut und deutlich.",
            example_vi: "Cô giáo nói rất to và rõ ràng."
        },
        "treffen": {
            infinitiv: "treffen",
            meaning: "gặp gỡ",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "treffe", du: "triffst", er_sie_es: "trifft", wir: "treffen", ihr: "trefft", sie_Sie: "treffen" },
            note: "Biến âm e → i CHỈ ở ngôi du và er/sie/es. Ngôi ihr KHÔNG biến âm (trefft).",
            example: "Am Nachmittag trifft Anna ihre Freunde im Café.",
            example_vi: "Vào buổi chiều, Anna gặp bạn bè ở quán cà phê."
        },
        "essen": {
            infinitiv: "essen",
            meaning: "ăn",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "esse", du: "isst", er_sie_es: "isst", wir: "essen", ihr: "esst", sie_Sie: "essen" },
            note: "Biến âm e → i CHỈ ở ngôi du và er/sie/es (du isst / er isst). Ngôi ihr KHÔNG biến âm (esst).",
            example: "Im Sommer essen die Kinder sehr gern Schokoladeneis.",
            example_vi: "Vào mùa hè bọn trẻ rất thích ăn kem sô-cô-la."
        },
        "geben": {
            infinitiv: "geben",
            meaning: "cho, đưa",
            type: "e → i",
            baseVowel: "e",
            shiftedVowel: "i",
            forms: { ich: "gebe", du: "gibst", er_sie_es: "gibt", wir: "geben", ihr: "gebt", sie_Sie: "geben" },
            note: "Biến âm e → i CHỈ ở ngôi du và er/sie/es (du gibst / er gibt). Ngôi ihr KHÔNG biến âm (gebt).",
            example: "Hannes und Julia geben dem kleinen Hund das Futter.",
            example_vi: "Hannes và Julia cho chú chó nhỏ ăn thức ăn."
        }
    };

    const PRONOUNS = [
        { key: "ich", label: "ich (tôi)", isShifted: false, note: "Giữ nguyên âm gốc + đuôi -e" },
        { key: "du", label: "du (bạn)", isShifted: true, note: "🔥 BIẾN ĐỔI NGUYÊN ÂM + đuôi -st" },
        { key: "er_sie_es", label: "er/sie/es (anh/cô ấy/nó)", isShifted: true, note: "🔥 BIẾN ĐỔI NGUYÊN ÂM + đuôi -t" },
        { key: "wir", label: "wir (chúng tôi)", isShifted: false, note: "Giữ nguyên thể đuôi -en" },
        { key: "ihr", label: "ihr (các bạn)", isShifted: false, isGoldWarning: true, note: "⚠️ QUY TẮC VÀNG: KHÔNG BIẾN ÂM! Giữ nguyên âm gốc + đuôi -t" },
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

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-amber-500/30 text-white shadow-2xl space-y-6">
                <!-- Header -->
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-300 font-bold text-xs uppercase tracking-wider">
                            ⚙️ Sơ đồ V1: Cỗ Máy Biến Âm
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Quy Tắc Vàng Chia Động Từ Bất Quy Tắc (A1)</h4>
                    </div>
                    <span class="text-xs text-amber-300/80 font-medium">💡 Biến âm CHỈ xảy ra ở ngôi du & er/sie/es! Ngôi ihr KHÔNG biến âm!</span>
                </div>

                <!-- Bộ chọn 7 Động từ -->
                <div class="space-y-2">
                    <div class="text-xs font-bold text-slate-400 uppercase tracking-wider flex items-center justify-between">
                        <span>1. Chọn động từ bất quy tắc cần khảo sát:</span>
                        <span class="text-amber-400 font-mono text-xs">Loại: ${verbData.type}</span>
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
                                            : 'bg-slate-800/80 hover:bg-slate-800 border-slate-700 text-slate-200 font-semibold'
                                    }">
                                    <span class="text-sm font-bold font-mono">${v.infinitiv}</span>
                                    <span class="text-[11px] ${isSel ? 'text-slate-900' : 'text-slate-400'}">(${v.meaning})</span>
                                </button>
                            `;
                        }).join('')}
                    </div>
                </div>

                <!-- 6 Bóng đèn ngôi xưng -->
                <div class="space-y-2">
                    <div class="text-xs font-bold text-slate-400 uppercase tracking-wider">
                        2. Chọn ngôi nhân xưng để xem đèn kích hoạt biến âm:
                    </div>
                    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
                        ${PRONOUNS.map(p => {
                            const isSel = p.key === currentV1Pronoun;
                            let bulbClass = "border-slate-700 bg-slate-800/60 text-slate-300";
                            let icon = "⚪";
                            if (p.isShifted) {
                                bulbClass = isSel
                                    ? "border-rose-500 bg-rose-950/70 text-rose-200 ring-2 ring-rose-500/50 shadow-lg shadow-rose-900/40"
                                    : "border-rose-900/40 bg-rose-950/20 text-rose-300/80 hover:bg-rose-950/40";
                                icon = "🔴";
                            } else if (p.isGoldWarning) {
                                bulbClass = isSel
                                    ? "border-emerald-500 bg-emerald-950/70 text-emerald-200 ring-2 ring-emerald-500/50 shadow-lg shadow-emerald-900/40"
                                    : "border-emerald-900/40 bg-emerald-950/20 text-emerald-300/80 hover:bg-emerald-950/40";
                                icon = "🟢";
                            } else if (isSel) {
                                bulbClass = "border-sky-500 bg-sky-950/70 text-sky-200 ring-2 ring-sky-500/50";
                                icon = "🔵";
                            }
                            return `
                                <button type="button" onclick="b13_selectPronoun('${p.key}')"
                                    class="p-3 rounded-2xl border text-left transition cursor-pointer flex flex-col justify-between gap-1.5 ${bulbClass}">
                                    <div class="flex items-center justify-between">
                                        <span class="text-xs font-black">${p.label.split(' ')[0]}</span>
                                        <span class="text-xs">${icon}</span>
                                    </div>
                                    <div class="text-sm font-black font-mono tracking-wide">
                                        ${verbData.forms[p.key]}
                                    </div>
                                    <span class="text-[10px] text-slate-400 block truncate">
                                        ${p.isShifted ? '🔥 Biến âm' : (p.isGoldWarning ? '⭐ Không đổi' : 'Quy tắc')}
                                    </span>
                                </button>
                            `;
                        }).join('')}
                    </div>
                </div>

                <!-- Bảng hiển thị kết quả Cỗ máy (Visual Display Panel) -->
                <div class="p-4 sm:p-5 rounded-2xl border ${
                    isShifted
                        ? 'bg-gradient-to-r from-rose-950/60 to-slate-900 border-rose-500/40 shadow-inner'
                        : (isIhr 
                            ? 'bg-gradient-to-r from-emerald-950/60 to-slate-900 border-emerald-500/40 shadow-inner'
                            : 'bg-slate-800/60 border-slate-700')
                } space-y-4">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                        <div class="space-y-1">
                            <span class="text-xs uppercase font-extrabold tracking-wider ${
                                isShifted ? 'text-rose-400' : (isIhr ? 'text-emerald-400' : 'text-sky-400')
                            }">
                                ${isShifted ? '🚨 TRẠNG THÁI: NGUYÊN ÂM ĐÃ BIẾN ĐỔI!' : (isIhr ? '🛡️ TRẠNG THÁI: CHỐNG BẪY NGÔI IHR!' : 'ℹ️ TRẠNG THÁI: CHIA QUY TẮC')}
                            </span>
                            <div class="flex items-baseline gap-3 flex-wrap">
                                <span class="text-2xl sm:text-3xl font-black text-white font-mono">
                                    <span class="text-slate-400">${curPron.label.split(' ')[0]}</span>
                                    <span class="${isShifted ? 'text-rose-300 underline decoration-rose-500 decoration-2' : (isIhr ? 'text-emerald-300 font-black' : 'text-amber-300')}">${conjugatedForm}</span>
                                </span>
                                <button type="button" onclick="b13_speakGerman('${curPron.label.split(' ')[0]} ${conjugatedForm}')"
                                    class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-600 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                    🔊 Nghe
                                </button>
                            </div>
                        </div>

                        <div class="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-xs space-y-1 max-w-sm">
                            <div class="font-bold text-slate-300">Quy tắc áp dụng:</div>
                            <div class="${isShifted ? 'text-rose-300 font-semibold' : (isIhr ? 'text-emerald-300 font-bold' : 'text-slate-400')}">
                                ${curPron.note}
                            </div>
                        </div>
                    </div>

                    <!-- Ví dụ thực tế -->
                    <div class="pt-3 border-t border-slate-800/80 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                        <div class="space-y-0.5">
                            <div class="text-slate-300 font-medium">
                                <span class="text-amber-400 font-bold">Ví dụ thực tế:</span>
                                <span class="italic font-serif text-sm text-white">„${verbData.example}“</span>
                            </div>
                            <div class="text-slate-400 italic">${verbData.example_vi}</div>
                        </div>
                        <button type="button" onclick="b13_speakGerman('${verbData.example.replace(/"/g, '')}')"
                            class="px-3 py-1.5 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 font-bold text-xs shrink-0 transition flex items-center gap-1 cursor-pointer">
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
    // V2: BẢN ĐỒ W-FRAGEN & GIỚI TỪ (Wo -> in, Woher -> aus, Wie -> Name, Was -> Dinge)
    // =========================================================================
    const V2_QUESTIONS = {
        "Woher": {
            word: "Woher",
            meaning: "Từ đâu (quê quán, xuất xứ)",
            targetPrep: "aus",
            prepMeaning: "từ (quốc gia, thành phố)",
            category: "Herkunft / Quê quán",
            dialogue: {
                question: "Woher kommen Sie?",
                question_vi: "Ngài đến từ đâu?",
                answer: "Ich komme aus Vietnam / aus Deutschland.",
                answer_vi: "Tôi đến từ Việt Nam / từ nước Đức."
            },
            rule: "Woher LUÔN LUÔN đi cùng động từ kommen và giới từ xuất xứ 'aus'.",
            colorClass: "rose"
        },
        "Wo": {
            word: "Wo",
            meaning: "Ở đâu (nơi chốn, cư trú)",
            targetPrep: "in",
            prepMeaning: "ở, tại (thành phố, đất nước)",
            category: "Wohnort / Nơi sinh sống",
            dialogue: {
                question: "Wo wohnen Sie jetzt?",
                question_vi: "Hiện tại ngài sống ở đâu?",
                answer: "Ich wohne in Berlin / in Ha Noi.",
                answer_vi: "Tôi sống ở Berlin / ở Hà Nội."
            },
            rule: "Wo hỏi địa điểm cư trú/vị trí cố định, LUÔN đi cùng động từ wohnen/leben/sein và giới từ 'in'.",
            colorClass: "blue"
        },
        "Wie": {
            word: "Wie",
            meaning: "Như thế nào (Hỏi Tên / Tính chất)",
            targetPrep: "Name",
            prepMeaning: "Tên riêng hoặc danh tính",
            category: "Name & Identität / Danh tính",
            dialogue: {
                question: "Wie heißen Sie? / Wie ist Ihr Name?",
                question_vi: "Ngài tên là gì? / Tên của ngài là gì?",
                answer: "Ich heiße Anna. / Mein Name ist David.",
                answer_vi: "Tôi tên là Anna. / Tên tôi là David."
            },
            rule: "Trong tiếng Đức KHÔNG dùng 'Was ist dein Name' mà BẮT BUỘC dùng 'Wie heißen Sie?' hoặc 'Wie ist Ihr Name?'.",
            colorClass: "amber"
        },
        "Was": {
            word: "Was",
            meaning: "Cái gì (Hỏi Đồ vật / Đồ uống / Hoạt động)",
            targetPrep: "Dinge / Speisen",
            prepMeaning: "Sự vật, món ăn, đồ uống",
            category: "Giao tiếp quán Cafe",
            dialogue: {
                question: "Was möchten Sie trinken?",
                question_vi: "Ngài muốn dùng thức uống gì?",
                answer: "Zwei Kaffee mit Zucker, bitte!",
                answer_vi: "Xin cho hai cà phê có đường!"
            },
            rule: "Was hỏi sự vật, đồ uống hoặc hành động: Was trinken Sie? Was essen wir? Was machen Sie?",
            colorClass: "purple"
        },
        "Wann": {
            word: "Wann",
            meaning: "Khi nào (Thời gian)",
            targetPrep: "Zeit / am, um",
            prepMeaning: "thời gian: am Wochenende, um 15 Uhr",
            category: "Zeitpunkt / Thời gian",
            dialogue: {
                question: "Wann triffst du deine Freunde im Café?",
                question_vi: "Khi nào bạn gặp bạn bè ở quán cà phê?",
                answer: "Am Wochenende um 15 Uhr.",
                answer_vi: "Vào cuối tuần lúc 15 giờ."
            },
            rule: "Wann hỏi thời gian cụ thể: am (thứ/buổi trong ngày/cuối tuần), um (giờ cụ thể).",
            colorClass: "emerald"
        }
    };

    let currentV2Key = "Woher";

    function b13_renderWFragenMap(containerId) {
        const c = document.getElementById(containerId || "b13-svg-v2-container");
        if (!c) return;

        const qData = V2_QUESTIONS[currentV2Key] || V2_QUESTIONS["Woher"];

        c.innerHTML = `
            <div class="p-5 sm:p-6 rounded-3xl bg-slate-900 border border-indigo-500/30 text-white shadow-2xl space-y-6">
                <!-- Header -->
                <div class="flex items-center justify-between flex-wrap gap-2 border-b border-slate-800 pb-4">
                    <div class="flex items-center gap-2">
                        <span class="px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/40 text-indigo-300 font-bold text-xs uppercase tracking-wider">
                            🗺️ Sơ đồ V2: Bản Đồ W-Fragen & Giới Từ
                        </span>
                        <h4 class="text-base sm:text-lg font-black text-white">Nghệ Thuật Đặt Câu Hỏi & Giới Từ Đi Kèm (A1)</h4>
                    </div>
                    <span class="text-xs text-indigo-300/80 font-medium">💡 Woher + aus • Wo + in • Wie + Name • Was + Cafe</span>
                </div>

                <!-- 5 Nút W-Fragen -->
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-2.5">
                    ${Object.keys(V2_QUESTIONS).map(qk => {
                        const q = V2_QUESTIONS[qk];
                        const isSel = qk === currentV2Key;
                        return `
                            <button type="button" onclick="b13_selectWFrage('${qk}')"
                                class="p-3 rounded-2xl border text-center transition cursor-pointer flex flex-col items-center justify-center gap-1 ${
                                    isSel
                                        ? 'bg-indigo-600 text-white font-black border-indigo-400 ring-2 ring-indigo-400/50 shadow-lg shadow-indigo-600/30 scale-[1.02]'
                                        : 'bg-slate-800/80 hover:bg-slate-800 border-slate-700 text-slate-200'
                                }">
                                <span class="text-base font-black font-mono">${q.word}?</span>
                                <span class="text-[11px] ${isSel ? 'text-indigo-100' : 'text-slate-400'}">${q.category}</span>
                            </button>
                        `;
                    }).join('')}
                </div>

                <!-- Sơ đồ Luồng Kéo Mũi Tên Trực Quan (SVG Interactive Flow) -->
                <div class="p-5 rounded-2xl bg-slate-950/80 border border-slate-800 space-y-4">
                    <div class="flex flex-col md:flex-row items-center justify-between gap-4">
                        <!-- Khối Câu Hỏi -->
                        <div class="w-full md:w-5/12 p-4 rounded-xl bg-indigo-950/50 border border-indigo-500/40 text-center space-y-1">
                            <span class="text-[10px] font-black uppercase tracking-wider text-indigo-400 block">Từ Để Hỏi (W-Frage)</span>
                            <div class="text-2xl font-black text-indigo-200 font-mono">${qData.word}?</div>
                            <div class="text-xs text-slate-300">Ý nghĩa: <b class="text-white">${qData.meaning}</b></div>
                        </div>

                        <!-- Mũi tên liên kết SVG -->
                        <div class="flex flex-col items-center justify-center shrink-0">
                            <div class="text-xs font-bold text-amber-400 font-mono px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/30">
                                LUÔN ĐI KÈM ➔
                            </div>
                        </div>

                        <!-- Khối Giới Từ / Trả Lời -->
                        <div class="w-full md:w-5/12 p-4 rounded-xl bg-emerald-950/50 border border-emerald-500/40 text-center space-y-1">
                            <span class="text-[10px] font-black uppercase tracking-wider text-emerald-400 block">Giới Từ / Thành Phần Chuẩn</span>
                            <div class="text-2xl font-black text-emerald-200 font-mono">${qData.targetPrep}</div>
                            <div class="text-xs text-slate-300">Đặc điểm: <b class="text-white">${qData.prepMeaning}</b></div>
                        </div>
                    </div>

                    <!-- Khung Phân tích Logic & Quy tắc -->
                    <div class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs flex items-start gap-2.5">
                        <span class="text-base">📌</span>
                        <div class="space-y-0.5">
                            <span class="font-bold text-amber-300">Ghi nhớ trọng tâm:</span>
                            <p class="text-slate-300 leading-relaxed">${qData.rule}</p>
                        </div>
                    </div>

                    <!-- Mẫu Hội Thoại Mẫu -->
                    <div class="p-4 rounded-xl bg-slate-900/90 border border-slate-800 space-y-2">
                        <div class="text-xs font-bold text-indigo-400 uppercase tracking-wider flex items-center justify-between">
                            <span>Mẫu Hội Thoại Thực Tế:</span>
                            <button type="button" onclick="b13_speakGerman('${qData.dialogue.question} ${qData.dialogue.answer}')"
                                class="px-2.5 py-1 rounded-lg bg-indigo-500/20 hover:bg-indigo-500/30 text-indigo-300 border border-indigo-500/40 text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                                🔊 Nghe hội thoại
                            </button>
                        </div>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                            <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800/80 space-y-1">
                                <span class="font-bold text-indigo-300">Hỏi:</span>
                                <div class="font-mono text-sm text-white">${qData.dialogue.question}</div>
                                <div class="text-slate-400 italic">${qData.dialogue.question_vi}</div>
                            </div>
                            <div class="p-2.5 rounded-lg bg-slate-950 border border-slate-800/80 space-y-1">
                                <span class="font-bold text-emerald-300">Đáp:</span>
                                <div class="font-mono text-sm text-white">${qData.dialogue.answer}</div>
                                <div class="text-slate-400 italic">${qData.dialogue.answer_vi}</div>
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
    // TTS AUDIO HELPER
    // =========================================================================
    function b13_speakGerman(text) {
        if (typeof speakGerman === 'function') {
            speakGerman(text);
        } else if ('speechSynthesis' in window) {
            const u = new SpeechSynthesisUtterance(text);
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
    global.b13_speakGerman = b13_speakGerman;
    global.b13_initReviewSvgDiagrams = b13_initReviewSvgDiagrams;
    global.initReviewSvgDiagrams = b13_initReviewSvgDiagrams;

})(typeof window !== 'undefined' ? window : this);
