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

/**
 * So sánh đáp án tiếng Đức thông minh:
 * Chấp nhận cả eintausend... và tausend..., einhundert... và hundert...
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
 * Sinh đề ngẫu nhiên mới cho 1 câu hỏi số đếm cụ thể
 */
function generateNewNumberData(ex) {
    let extra = {};
    try {
        extra = typeof ex.extra_data === 'string' ? JSON.parse(ex.extra_data) : (ex.extra_data || {});
    } catch (e) {
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
            if (extra.dynamic_number || extra.dynamic_mode) isDynamic = true;
        } catch (e) {}

        if (isDynamic) {
            generateNewNumberData(ex);
        }
    });
}

if (typeof window !== 'undefined') {
    window.numberToGerman = numberToGerman;
    window.getRandomInt = getRandomInt;
    window.checkGermanAnswerEquivalence = checkGermanAnswerEquivalence;
    window.generateNewNumberData = generateNewNumberData;
    window.randomizeAllNumberExercises = randomizeAllNumberExercises;
}
