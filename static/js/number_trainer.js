/**
 * DeutschMeister - Bộ sinh và chuyển đổi số tiếng Đức (Dynamic Number Generator)
 * Hỗ trợ chuyển đổi từ 0 đến 9999 sang chữ tiếng Đức chuẩn ngữ pháp
 * Tự động đổi đề số đếm ngẫu nhiên khi hoàn thành câu hoặc bấm Đổi đề
 */

function numberToGerman(n) {
    n = parseInt(n, 10);
    if (isNaN(n) || n < 0 || n > 9999) return "";
    if (n === 0) return "null";

    const ones = ["", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"];
    const teens = {
        10: "zehn", 11: "elf", 12: "zwölf", 13: "dreizehn", 14: "vierzehn",
        15: "fünfzehn", 16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn"
    };
    const tens = {
        2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig",
        6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"
    };

    function convertUnder100(num) {
        if (num === 0) return "";
        if (num === 1) return "eins";
        if (num < 10) return ones[num];
        if (num < 20) return teens[num];
        const t = Math.floor(num / 10);
        const o = num % 10;
        if (o === 0) return tens[t];
        return `${ones[o]}und${tens[t]}`;
    }

    let result = "";
    if (n >= 1000) {
        const th = Math.floor(n / 1000);
        result += (th === 1 ? "eintausend" : `${ones[th]}tausend`);
        n %= 1000;
    }
    if (n >= 100) {
        const h = Math.floor(n / 100);
        result += (h === 1 ? "einhundert" : `${ones[h]}hundert`);
        n %= 100;
    }
    if (n > 0) {
        result += convertUnder100(n);
    }
    return result;
}

/**
 * Tạo số ngẫu nhiên trong khoảng [min, max]
 */
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function priceToGerman(euros, cents) {
    euros = parseInt(euros, 10) || 0;
    cents = parseInt(cents, 10) || 0;

    let euroStr = "";
    if (euros === 1) {
        euroStr = "ein Euro";
    } else {
        euroStr = `${numberToGerman(euros)} Euro`;
    }

    if (cents <= 0) {
        return euroStr;
    }

    const centStr = numberToGerman(cents);
    return `${euroStr} ${centStr}`;
}

/**
 * So sánh đáp án tiếng Đức thông minh:
 * Chấp nhận cả eintausend... và tausend..., einhundert... và hundert...
 * Chấp nhận định dạng giá tiền (4,50 <-> 4.50 <-> 4,50 Euro <-> ein Euro neunundzwanzig Cent...)
 */
function checkGermanAnswerEquivalence(userAns, correctAns) {
    if (!userAns || !correctAns) return false;

    const clean = (s) => String(s)
        .trim()
        .toLowerCase()
        .replace(/[.,!?;:]+$/g, '')
        .replace(/\s+/g, ' ');

    const u = clean(userAns);
    const c = clean(correctAns);

    if (u === c) return true;

    // Chuẩn hóa so sánh giá tiền Euro (ví dụ: "4,50" <-> "4.50" <-> "4,50 euro" <-> "4,50 €")
    const cleanPrice = (s) => s.replace(/euro/g, '').replace(/€/g, '').replace(/\./g, ',').replace(/\s+/g, '').trim();
    if (cleanPrice(u) === cleanPrice(c) && cleanPrice(c).includes(',')) return true;

    // Chuẩn hóa loại bỏ chữ "cent" ở cuối khi so sánh chữ đọc giá tiền
    const uNoCent = u.replace(/\s*cent$/g, '').replace(/eins euro/g, 'ein euro');
    const cNoCent = c.replace(/\s*cent$/g, '').replace(/eins euro/g, 'ein euro');
    if (uNoCent === cNoCent) return true;

    // Chuẩn hóa loại bỏ khoảng trắng hoàn toàn nếu câu trả lời là 1 từ ghép
    const uNoSpace = u.replace(/\s+/g, '');
    const cNoSpace = c.replace(/\s+/g, '');

    if (uNoSpace === cNoSpace) return true;

    // So sánh chấp nhận cả einhundert <-> hundert
    const normalizeHundreds = (str) => str.replace(/einhundert/g, 'hundert');
    if (normalizeHundreds(uNoSpace) === normalizeHundreds(cNoSpace)) return true;

    // So sánh chấp nhận cả eintausend <-> tausend
    const normalizeThousands = (str) => str.replace(/eintausend/g, 'tausend');
    if (normalizeThousands(uNoSpace) === normalizeThousands(cNoSpace)) return true;

    // So sánh cho cặp số cách nhau dấu phẩy (ví dụ: "83, 92" hoặc "dreiundachtzig, zweiundneunzig")
    if (c.includes(',')) {
        const uParts = u.split(',').map(p => clean(p).replace(/\s+/g, ''));
        const cParts = c.split(',').map(p => clean(p).replace(/\s+/g, ''));
        if (uParts.length === cParts.length) {
            const allMatch = uParts.every((part, idx) => {
                const target = cParts[idx];
                return part === target ||
                    normalizeHundreds(part) === normalizeHundreds(target) ||
                    normalizeThousands(part) === normalizeThousands(target);
            });
            if (allMatch) return true;
        }
    }

    return false;
}

/**
 * Sinh đề ngẫu nhiên mới cho 1 câu hỏi cụ thể (Số đếm, Giá tiền Euro hoặc Chia động từ)
 */
function generateNewNumberData(ex) {
    let extra = {};
    try {
        extra = typeof ex.extra_data === 'string' ? JSON.parse(ex.extra_data) : (ex.extra_data || {});
    } catch (e) {
        return ex;
    }

    // 1. Xử lý câu hỏi Giá tiền Euro (dynamic_price)
    if (extra.dynamic_price) {
        const centsList = [0, 10, 15, 20, 25, 30, 45, 50, 60, 75, 80, 85, 89, 90, 95, 99];
        const euros = getRandomInt(1, 25);
        const cents = centsList[Math.floor(Math.random() * centsList.length)];
        const formattedPrice = `${euros},${cents < 10 ? '0' + cents : cents}`;
        const dePrice = priceToGerman(euros, cents);

        if (extra.dynamic_mode === 'listen_price') {
            extra.audio_text = `Das macht ${dePrice}.`;
            ex.extra_data = JSON.stringify(extra);
            ex.question = `[Luyện Nghe giá tiền Euro (Random)]: Nghe câu thông báo của nhân viên phục vụ và điền số tiền:`;
            ex.correct_answer = formattedPrice;
            ex.explanation = `Nhân viên phục vụ nói '${extra.audio_text}' → Số tiền là ${formattedPrice} € (hoặc gõ ${dePrice}).`;
        } else {
            ex.question = `[Viết giá tiền Euro (Random)]: Hãy viết giá tiền ${formattedPrice} € bằng chữ tiếng Đức (chấp nhận có hoặc không có chữ Cent):`;
            ex.correct_answer = dePrice;
            ex.explanation = `Giá tiền ${formattedPrice} € viết bằng chữ tiếng Đức là: '${dePrice}' (hoặc kèm 'Cent').`;
        }
        return ex;
    }

    // 2. Xử lý câu hỏi Chia động từ theo ngôi (dynamic_conjugation)
    if (extra.dynamic_conjugation) {
        const verbsDb = (typeof GERMAN_VERBS_DB !== 'undefined') ? GERMAN_VERBS_DB : [
            { infinitiv: "machen", meaning: "làm", forms: { ich: "mache", du: "machst", er_sie_es: "macht", wir: "machen", ihr: "macht", sie_Sie: "machen" } },
            { infinitiv: "wohnen", meaning: "sống", forms: { ich: "wohne", du: "wohnst", er_sie_es: "wohnt", wir: "wohnen", ihr: "wohnt", sie_Sie: "wohnen" } },
            { infinitiv: "kommen", meaning: "đến", forms: { ich: "komme", du: "kommst", er_sie_es: "kommt", wir: "kommen", ihr: "kommt", sie_Sie: "kommen" } },
            { infinitiv: "heißen", meaning: "tên là", forms: { ich: "heiße", du: "heißt", er_sie_es: "heißt", wir: "heißen", ihr: "heißt", sie_Sie: "heißen" } },
            { infinitiv: "mieten", meaning: "thuê", forms: { ich: "miete", du: "mietest", er_sie_es: "mietet", wir: "mieten", ihr: "mietet", sie_Sie: "mieten" } },
            { infinitiv: "arbeiten", meaning: "làm việc", forms: { ich: "arbeite", du: "arbeitest", er_sie_es: "arbeitet", wir: "arbeiten", ihr: "arbeitet", sie_Sie: "arbeiten" } },
            { infinitiv: "trinken", meaning: "uống", forms: { ich: "trinke", du: "trinkst", er_sie_es: "trinkt", wir: "trinken", ihr: "trinkt", sie_Sie: "trinken" } },
            { infinitiv: "nehmen", meaning: "chọn món", forms: { ich: "nehme", du: "nimmst", er_sie_es: "nimmt", wir: "nehmen", ihr: "nehmt", sie_Sie: "nehmen" } },
            { infinitiv: "lesen", meaning: "đọc", forms: { ich: "lese", du: "liest", er_sie_es: "liest", wir: "lesen", ihr: "lest", sie_Sie: "lesen" } },
            { infinitiv: "sein", meaning: "thì, là, ở", forms: { ich: "bin", du: "bist", er_sie_es: "ist", wir: "sind", ihr: "seid", sie_Sie: "sind" } },
            { infinitiv: "haben", meaning: "có", forms: { ich: "habe", du: "hast", er_sie_es: "hat", wir: "haben", ihr: "habt", sie_Sie: "haben" } },
            { infinitiv: "möchten", meaning: "muốn", forms: { ich: "möchte", du: "möchtest", er_sie_es: "möchte", wir: "möchten", ihr: "möchtet", sie_Sie: "möchten" } },
            { infinitiv: "zahlen", meaning: "thanh toán", forms: { ich: "zahle", du: "zahlst", er_sie_es: "zahlt", wir: "zahlen", ihr: "zahlt", sie_Sie: "zahlen" } }
        ];

        const targetVerbs = ["machen", "wohnen", "kommen", "heißen", "mieten", "arbeiten", "trinken", "nehmen", "lesen", "sein", "haben", "möchten", "zahlen"];
        const pool = verbsDb.filter(v => targetVerbs.includes(v.infinitiv));
        const chosenVerb = pool[Math.floor(Math.random() * pool.length)];

        const subjects = [
            { label: "ich", personKey: "ich", pronoun: "ich" },
            { label: "du", personKey: "du", pronoun: "du" },
            { label: "er", personKey: "er_sie_es", pronoun: "er" },
            { label: "sie (cô ấy)", personKey: "er_sie_es", pronoun: "sie" },
            { label: "es", personKey: "er_sie_es", pronoun: "es" },
            { label: "wir", personKey: "wir", pronoun: "wir" },
            { label: "ihr", personKey: "ihr", pronoun: "ihr" },
            { label: "sie (họ)", personKey: "sie_Sie", pronoun: "sie" },
            { label: "Sie (Ngài)", personKey: "sie_Sie", pronoun: "Sie" },
            { label: "Anna und ich", personKey: "wir", pronoun: "Anna und ich" },
            { label: "Du und Peter", personKey: "ihr", pronoun: "Du und Peter" },
            { label: "Die Lehrerin", personKey: "er_sie_es", pronoun: "Die Lehrerin" },
            { label: "Mein Freund", personKey: "er_sie_es", pronoun: "Mein Freund" }
        ];

        const chosenSubject = subjects[Math.floor(Math.random() * subjects.length)];
        const correctForm = chosenVerb.forms[chosenSubject.personKey];

        ex.question = `[Rèn phản xạ Chia Động Từ (Random)]: Hãy chia động từ '${chosenVerb.infinitiv}' (${chosenVerb.meaning}) cho chủ ngữ '${chosenSubject.label}': '${chosenSubject.pronoun} ___'`;
        ex.correct_answer = correctForm;
        ex.explanation = `Động từ '${chosenVerb.infinitiv}' đi với chủ ngữ '${chosenSubject.label}' được chia là: '${correctForm}'.`;
        return ex;
    }

    if (!extra.dynamic_number && !extra.dynamic_mode) return ex;

    const mode = extra.dynamic_mode;
    const min = extra.min || 21;
    const max = extra.max || 99;

    if (mode === 'mcq_num_to_de') {
        const num = getRandomInt(min, max);
        const correct = numberToGerman(num);
        // Tạo các phương án gây nhiễu
        const distractors = new Set();
        distractors.add(correct);

        while (distractors.size < 4) {
            const fakeNum = getRandomInt(Math.max(10, num - 15), Math.min(99, num + 15));
            if (fakeNum !== num) {
                distractors.add(numberToGerman(fakeNum));
            }
        }

        const options = Array.from(distractors).sort(() => Math.random() - 0.5);
        ex.question = `Câu 10 [Random Đọc Số]: Cách viết tiếng Đức chính xác của số ${num} là gì?`;
        ex.options = options;
        ex.options_json = JSON.stringify(options);
        ex.correct_answer = correct;
        ex.explanation = `Số ${num} được ghép từ hàng đơn vị + und + hàng chục: ${correct}.`;
    }
    else if (mode === 'de_to_num') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        ex.question = `[Đức → Số (Random)]: Chuyển chữ số tiếng Đức sau thành số tự nhiên: '${german}'`;
        ex.correct_answer = String(num);
        ex.explanation = `'${german}' biểu thị con số tự nhiên ${num}.`;
    }
    else if (mode === 'listen_num') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        extra.audio_text = german;
        ex.extra_data = JSON.stringify(extra);
        ex.correct_answer = String(num);
        ex.explanation = `Âm thanh phát âm: '${german}' → Đáp án là số ${num}.`;
    }
    else if (mode === 'num_to_de') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        let prefix = '';
        if (num >= 1000) {
            prefix = ' (bắt đầu bằng eintausend... hoặc tausend...)';
        } else if (num >= 100) {
            prefix = ' (viết liền không dấu cách)';
        } else {
            prefix = ' (viết liền không dấu cách)';
        }
        ex.question = `Hãy viết số ${num} bằng chữ tiếng Đức${prefix}:`;
        ex.correct_answer = german;
        ex.explanation = `Số ${num} viết bằng chữ tiếng Đức chuẩn là: ${german}.`;
    }
    else if (mode === 'tens_to_de') {
        const tensList = [20, 30, 40, 50, 60, 70, 80, 90];
        const num = tensList[Math.floor(Math.random() * tensList.length)];
        const german = numberToGerman(num);
        ex.question = `[Viết số tròn chục (Random)]: Hãy viết số ${num} bằng chữ tiếng Đức:`;
        ex.correct_answer = german;
        ex.explanation = `Số tròn chục ${num} được viết là: ${german}${num === 30 ? ' (chú ý chữ ß)' : ''}.`;
    }
    else if (mode === 'special_3digit_to_de') {
        const specials = [912, 815, 716, 617, 511, 418, 319, 212, 116, 707, 808, 909];
        const num = specials[Math.floor(Math.random() * specials.length)];
        const german = numberToGerman(num);
        ex.question = `[Viết số 3 chữ số đặc biệt (Random)]: Hãy viết số ${num} bằng chữ tiếng Đức (viết liền không dấu cách):`;
        ex.correct_answer = german;
        ex.explanation = `Số ${num} viết bằng chữ tiếng Đức là: ${german}.`;
    }
    else if (mode === 'pair_num_to_de') {
        const n1 = getRandomInt(21, 99);
        let n2 = getRandomInt(21, 99);
        while (n2 === n1) n2 = getRandomInt(21, 99);

        const de1 = numberToGerman(n1);
        const de2 = numberToGerman(n2);
        ex.question = `[Viết cặp 2 số (Random)]: Hãy viết số ${n1} và số ${n2} bằng chữ tiếng Đức (cách nhau bởi dấu phẩy):`;
        ex.correct_answer = `${de1}, ${de2}`;
        ex.explanation = `${n1} = ${de1}; ${n2} = ${de2}.`;
    }
    else if (mode === 'speak_num') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        extra.audio_text = german;
        ex.extra_data = JSON.stringify(extra);
        ex.question = `[Luyện Nói số đếm (Random)]: Nghe mẫu và luyện phát âm số ${num} bằng tiếng Đức:`;
        ex.correct_answer = german;
        ex.explanation = `Số ${num} phát âm là: ${german}.`;
    }

    return ex;
}

/**
 * Đổi toàn bộ các câu hỏi số đếm trong danh sách bài tập hiện tại
 */
function randomizeAllNumberExercises(exercisesList) {
    if (!exercisesList || !Array.isArray(exercisesList)) return;
    exercisesList.forEach(ex => {
        let isDynamic = false;
        try {
            const extra = typeof ex.extra_data === 'string' ? JSON.parse(ex.extra_data) : (ex.extra_data || {});
            if (extra.dynamic_number || extra.dynamic_mode || extra.dynamic_price || extra.dynamic_conjugation) isDynamic = true;
        } catch (e) {}

        if (isDynamic) {
            generateNewNumberData(ex);
        }
    });
}

if (typeof window !== 'undefined') {
    window.numberToGerman = numberToGerman;
    window.priceToGerman = priceToGerman;
    window.getRandomInt = getRandomInt;
    window.checkGermanAnswerEquivalence = checkGermanAnswerEquivalence;
    window.generateNewNumberData = generateNewNumberData;
    window.randomizeAllNumberExercises = randomizeAllNumberExercises;
}
