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

    // Chấp nhận nhiều đáp án tương đương cách nhau bởi dấu '/' hoặc '||'
    if (correctAns.includes('/') || correctAns.includes('||')) {
        const alts = correctAns.split(/\/|\|\|/).map(a => a.trim());
        if (alts.some(alt => checkGermanAnswerEquivalence(userAns, alt))) {
            return true;
        }
    }

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

    // 3. Xử lý câu hỏi Mạo từ & Phủ định (dynamic_article_quiz)
    if (extra.dynamic_article_quiz) {
        const db = (typeof GERMAN_LEXIKON_DB !== 'undefined' && GERMAN_LEXIKON_DB.length > 0)
            ? GERMAN_LEXIKON_DB.filter(x => x.gender !== 'verb')
            : [
                { word: "Tisch", article: "der", gender: "der", negation: "kein Tisch", indefinite: "ein Tisch", meaning: "cái bàn" },
                { word: "Brille", article: "die", gender: "die", negation: "keine Brille", indefinite: "eine Brille", meaning: "cái kính" },
                { word: "Handy", article: "das", gender: "das", negation: "kein Handy", indefinite: "ein Handy", meaning: "điện thoại" },
                { word: "Tasche", article: "die", gender: "die", negation: "keine Tasche", indefinite: "eine Tasche", meaning: "túi xách" },
                { word: "Buch", article: "das", gender: "das", negation: "kein Buch", indefinite: "ein Buch", meaning: "quyển sách" },
                { word: "Kuli", article: "der", gender: "der", negation: "kein Kuli", indefinite: "ein Kuli", meaning: "bút bi" }
            ];

        const idx1 = Math.floor(Math.random() * db.length);
        let idx2 = Math.floor(Math.random() * db.length);
        while (idx2 === idx1 && db.length > 1) {
            idx2 = Math.floor(Math.random() * db.length);
        }
        const item1 = db[idx1];
        const item2 = db[idx2];

        const negWord = item1.gender === 'die' ? 'keine' : 'kein';
        const indWord = item2.gender === 'die' ? 'eine' : 'ein';
        const qIndefinite = item1.gender === 'die' ? 'eine' : 'ein';

        ex.question = `[Mạo từ & Phủ định (Random)]: Hoàn thành câu trả lời phủ định: "Ist das ${qIndefinite} ${item1.word}?" → "Nein, das ist ___ ${item1.word}. Das ist ___ ${item2.word}." (Điền 2 từ mạo từ cách nhau bởi dấu phẩy):`;
        ex.correct_answer = `${negWord}, ${indWord}`;
        ex.explanation = `'${item1.word}' mang giống ${item1.article} nên phủ định dùng '${negWord}'; '${item2.word}' mang giống ${item2.article} nên dùng '${indWord}'.`;
        return ex;
    }

    // 4. Xử lý câu hỏi Sở hữu với Mạo từ xác định (dynamic_possessive_article)
    if (extra.dynamic_possessive_article) {
        const db = (typeof GERMAN_LEXIKON_DB !== 'undefined' && GERMAN_LEXIKON_DB.length > 0)
            ? GERMAN_LEXIKON_DB.filter(x => x.gender !== 'verb')
            : [
                { word: "Kuli", article: "der", gender: "der", meaning: "bút bi" },
                { word: "Handy", article: "das", gender: "das", meaning: "điện thoại" },
                { word: "Brille", article: "die", gender: "die", meaning: "kính mắt" },
                { word: "Buch", article: "das", gender: "das", meaning: "quyển sách" },
                { word: "Tasche", article: "die", gender: "die", meaning: "túi xách" },
                { word: "Füller", article: "der", gender: "der", meaning: "bút mực" }
            ];
        const names = ["Anna", "David", "Marc", "Frau Schiller", "Herr Nguyen", "Sophie", "Peter"];
        const chosenItem = db[Math.floor(Math.random() * db.length)];
        const chosenName = names[Math.floor(Math.random() * names.length)];

        const indWord = chosenItem.gender === 'die' ? 'eine' : 'ein';
        const defWord = chosenItem.article; // der / die / das

        ex.question = `[Mạo từ Sở Hữu (Random)]: Hoàn thành câu xác nhận đồ vật của ${chosenName}: "Ist das ___ ${chosenItem.word}?" → "Ja, das ist ___ ${chosenItem.word} von ${chosenName}." (Điền 2 từ mạo từ cách nhau bởi dấu phẩy):`;
        ex.correct_answer = `${indWord}, ${defWord}`;
        ex.explanation = `'${chosenItem.word}' (${chosenItem.meaning}) mang giống ${defWord} → Mạo từ bất định là '${indWord}' và mạo từ xác định sở hữu là '${defWord} ${chosenItem.word} von ${chosenName}'.`;
        return ex;
    }

    // 5. Xử lý câu hỏi Số nhiều danh từ (dynamic_plural_quiz)
    if (extra.dynamic_plural_quiz) {
        const db = (typeof GERMAN_LEXIKON_DB !== 'undefined' && GERMAN_LEXIKON_DB.length > 0)
            ? GERMAN_LEXIKON_DB.filter(x => x.gender !== 'verb' && x.plural && x.plural.startsWith('die '))
            : [
                { word: "Tisch", article: "der", plural: "die Tische", rule: "Thêm -e" },
                { word: "Stuhl", article: "der", plural: "die Stühle", rule: "Biến âm u -> ü và thêm -e" },
                { word: "Brille", article: "die", plural: "die Brillen", rule: "Thêm -n" },
                { word: "Buch", article: "das", plural: "die Bücher", rule: "Biến âm u -> ü và thêm -er" },
                { word: "Heft", article: "das", plural: "die Hefte", rule: "Thêm -e" },
                { word: "Wörterbuch", article: "das", plural: "die Wörterbücher", rule: "Số nhiều theo Buch (die Wörterbücher)" },
                { word: "Handy", article: "das", plural: "die Handys", rule: "Thêm -s" }
            ];
        const chosenItem = db[Math.floor(Math.random() * db.length)];

        ex.question = `[Số Nhiều Danh Từ (Random)]: Hãy viết dạng số nhiều (kèm mạo từ 'die') của danh từ '${chosenItem.article} ${chosenItem.word}':`;
        ex.correct_answer = chosenItem.plural;
        ex.explanation = `'${chosenItem.article} ${chosenItem.word}' khi chuyển sang số nhiều là '${chosenItem.plural}'. ${chosenItem.rule || ''}`;
        return ex;
    }

    // 6. Xử lý câu hỏi Phương hướng & Bản đồ (dynamic_direction_quiz - Bài 3)
    if (extra.dynamic_direction_quiz) {
        const cities = [
            { city: "Hanoi", country: "Vietnam", noun: "im Norden", adj: "nördlich", vi: "miền Bắc", isCenter: false },
            { city: "Hai Phong", country: "Vietnam", noun: "im Nordosten", adj: "nordöstlich", vi: "phía Đông Bắc", isCenter: false },
            { city: "Da Nang", country: "Vietnam", noun: "in der Mitte", adj: "in der Mitte", vi: "miền Trung", isCenter: true },
            { city: "Long An", country: "Vietnam", noun: "im Süden", adj: "südlich", vi: "miền Nam", isCenter: false },
            { city: "Dien Bien", country: "Vietnam", noun: "im Nordwesten", adj: "nordwestlich", vi: "phía Tây Bắc", isCenter: false },
            { city: "Can Tho", country: "Vietnam", noun: "im Südwesten", adj: "südwestlich", vi: "phía Tây Nam", isCenter: false },
            { city: "Berlin", country: "Deutschland", noun: "im Osten", adj: "östlich", vi: "phía Đông", isCenter: false },
            { city: "München", country: "Deutschland", noun: "im Süden", adj: "südlich", vi: "phía Nam", isCenter: false },
            { city: "Hamburg", country: "Deutschland", noun: "im Norden", adj: "nördlich", vi: "phía Bắc", isCenter: false },
            { city: "Köln", country: "Deutschland", noun: "im Westen", adj: "westlich", vi: "phía Tây", isCenter: false },
            { city: "Frankfurt", country: "Deutschland", noun: "im Westen", adj: "westlich", vi: "phía Tây", isCenter: false },
            { city: "Dresden", country: "Deutschland", noun: "im Südosten", adj: "südöstlich", vi: "phía Đông Nam", isCenter: false }
        ];
        const chosen = cities[Math.floor(Math.random() * cities.length)];
        const useAdj = !chosen.isCenter && (Math.random() > 0.5);

        if (useAdj) {
            ex.question = `[Phương hướng Tính từ -lich (Random)]: Hãy viết câu miêu tả vị trí của ${chosen.city} bằng TÍNH TỪ chỉ phương hướng (-lich) theo mẫu '${chosen.city} liegt ... von ${chosen.country}':`;
            ex.correct_answer = `${chosen.city} liegt ${chosen.adj} von ${chosen.country}.`;
            ex.explanation = `Dùng tính từ chỉ phương hướng (-lich): '${chosen.city} liegt ${chosen.adj} von ${chosen.country}' (${chosen.city} nằm ở ${chosen.vi} ${chosen.country}). Tuyệt đối không dùng 'im' trước tính từ.`;
        } else {
            ex.question = `[Phương hướng Cụm Danh từ (Random)]: Hãy hoàn thành vị trí của ${chosen.city} (${chosen.vi} ${chosen.country}): '${chosen.city} liegt ___ von ${chosen.country}.'`;
            ex.correct_answer = chosen.noun;
            ex.explanation = `'${chosen.city}' nằm ở ${chosen.vi} của ${chosen.country} → Cụm giới từ là '${chosen.noun} von ${chosen.country}'.`;
        }
        return ex;
    }

    // 7. Xử lý câu hỏi Danh lam Thắng cảnh Châu Âu (dynamic_landmark_quiz - Bài 3)
    if (extra.dynamic_landmark_quiz) {
        const landmarks = [
            { name: "Akropolis", article: "die", city: "Athen", country: "Griechenland", vi: "Thành cổ Akropolis" },
            { name: "Big Ben", article: "der", city: "London", country: "England", vi: "Tháp đồng hồ Big Ben" },
            { name: "Eiffelturm", article: "der", city: "Paris", country: "Frankreich", vi: "Tháp Eiffel" },
            { name: "Schiefe Turm", article: "der", city: "Pisa", country: "Italien", vi: "Tháp nghiêng Pisa" },
            { name: "Prater", article: "der", city: "Wien", country: "Österreich", vi: "Công viên giải trí Prater" },
            { name: "Brandenburger Tor", article: "das", city: "Berlin", country: "Deutschland", vi: "Cổng Brandenburg" },
            { name: "Rote Platz", article: "der", city: "Moskau", country: "Russland", vi: "Quảng trường Đỏ" }
        ];
        const chosen = landmarks[Math.floor(Math.random() * landmarks.length)];
        const quizType = Math.floor(Math.random() * 3);

        if (quizType === 0) {
            ex.question = `[Danh lam thắng cảnh Châu Âu (Random)]: Công trình '${chosen.name}' (${chosen.vi}) đi kèm mạo từ nào ở Nominativ? "Was ist das? – Das ist ___ ${chosen.name}."`;
            ex.correct_answer = chosen.article;
            ex.explanation = `'${chosen.name}' đi kèm mạo từ '${chosen.article}' → "Das ist ${chosen.article} ${chosen.name}".`;
        } else if (quizType === 1) {
            ex.question = `[Địa danh & Thành phố (Random)]: Công trình '${chosen.article} ${chosen.name}' (${chosen.vi}) nằm ở thành phố nào? "Wo ist denn das? – Das ist in ___."`;
            ex.correct_answer = chosen.city;
            ex.explanation = `'${chosen.article} ${chosen.name}' tọa lạc tại thành phố '${chosen.city}'.`;
        } else {
            ex.question = `[Địa danh & Quốc gia (Random)]: Thành phố ${chosen.city} ('${chosen.article} ${chosen.name}') nằm ở quốc gia nào? "In welchem Land ist das? – ${chosen.city} ist in ___."`;
            ex.correct_answer = chosen.country;
            ex.explanation = `'${chosen.city}' nằm ở đất nước '${chosen.country}'.`;
        }
        return ex;
    }

    // 8. Xử lý câu hỏi Chia 'sein' ở Thì Präteritum (dynamic_praeteritum_quiz - Bài 3)
    if (extra.dynamic_praeteritum_quiz) {
        const subjects = [
            { label: "ich", pronoun: "ich", form: "war" },
            { label: "du", pronoun: "du", form: "warst" },
            { label: "er (anh ấy)", pronoun: "er", form: "war" },
            { label: "sie (cô ấy)", pronoun: "sie", form: "war" },
            { label: "wir", pronoun: "wir", form: "waren" },
            { label: "ihr", pronoun: "ihr", form: "wart" },
            { label: "Sie (Ngài)", pronoun: "Sie", form: "waren" },
            { label: "Paula und ich", pronoun: "Paula und ich", form: "waren" },
            { label: "du und Peter (ihr)", pronoun: "du und Peter", form: "wart" },
            { label: "Paula", pronoun: "Paula", form: "war" },
            { label: "Der Cat Bi Markt", pronoun: "Der Cat Bi Markt", form: "war" }
        ];
        const times = ["Gestern", "Vorgestern", "Letzte Woche", "Früher"];
        const places = ["in Haiphong", "in Hanoi", "im BigC Supermarkt", "im Theater", "auf dem Cat Bi Markt", "in Wien", "in Athen"];

        const chosenSub = subjects[Math.floor(Math.random() * subjects.length)];
        const chosenTime = times[Math.floor(Math.random() * times.length)];
        const chosenPlace = places[Math.floor(Math.random() * places.length)];

        ex.question = `[Chia 'sein' ở Thì Präteritum (Random)]: Điền dạng quá khứ đúng của động từ 'sein' cho chủ ngữ '${chosenSub.label}': "${chosenTime} ___ ${chosenSub.pronoun} ${chosenPlace}."`;
        ex.correct_answer = chosenSub.form;
        ex.explanation = `Chủ ngữ '${chosenSub.pronoun}' đi với thì Quá khứ đơn (Präteritum) của 'sein' là '${chosenSub.form}'. (${chosenTime} ${chosenSub.form} ${chosenSub.pronoun} ${chosenPlace}).`;
        return ex;
    }

    // 9. Xử lý câu hỏi Quốc gia & Ngôn ngữ (dynamic_country_language_quiz - Bài 3)
    if (extra.dynamic_country_language_quiz) {
        const countries = [
            { country: "die Schweiz", article: "die", lang: "Deutsch, Französisch, Italienisch", aus: "aus der Schweiz", in: "in der Schweiz", isSpecial: true },
            { country: "die Türkei", article: "die", lang: "Türkisch", aus: "aus der Türkei", in: "in der Türkei", isSpecial: true },
            { country: "die Slowakei", article: "die", lang: "Slowakisch", aus: "aus der Slowakei", in: "in der Slowakei", isSpecial: true },
            { country: "der Iran", article: "der", lang: "Persisch", aus: "aus dem Iran", in: "im Iran", isSpecial: true },
            { country: "die USA", article: "die (Pl.)", lang: "Englisch", aus: "aus den USA", in: "in den USA", isSpecial: true },
            { country: "Deutschland", article: "—", lang: "Deutsch", aus: "aus Deutschland", in: "in Deutschland", isSpecial: false },
            { country: "Österreich", article: "—", lang: "Deutsch", aus: "aus Österreich", in: "in Österreich", isSpecial: false },
            { country: "Italien", article: "—", lang: "Italienisch", aus: "aus Italien", in: "in Italien", isSpecial: false },
            { country: "Spanien", article: "—", lang: "Spanisch", aus: "aus Spanien", in: "in Spanien", isSpecial: false },
            { country: "Griechenland", article: "—", lang: "Griechisch", aus: "aus Griechenland", in: "in Griechenland", isSpecial: false },
            { country: "Frankreich", article: "—", lang: "Französisch", aus: "aus Frankreich", in: "in Frankreich", isSpecial: false },
            { country: "Russland", article: "—", lang: "Russisch", aus: "aus Russland", in: "in Russland", isSpecial: false },
            { country: "Polen", article: "—", lang: "Polnisch", aus: "aus Polen", in: "in Polen", isSpecial: false },
            { country: "Vietnam", article: "—", lang: "Vietnamesisch", aus: "aus Vietnam", in: "in Vietnam", isSpecial: false }
        ];

        const chosen = countries[Math.floor(Math.random() * countries.length)];
        const quizType = chosen.isSpecial ? (Math.random() > 0.5 ? 'preposition' : 'language') : 'language';

        if (quizType === 'preposition') {
            const useAus = Math.random() > 0.5;
            if (useAus) {
                ex.question = `[Giới từ 'aus' với Quốc gia có mạo từ (Random)]: Điền cụm giới từ 'đến từ' cho quốc gia '${chosen.country}': "Frau Müller kommt ___."`;
                ex.correct_answer = chosen.aus;
                ex.explanation = `'${chosen.country}' là quốc gia có mạo từ, khi kết hợp với 'aus' ở Dativ phải đổi thành '${chosen.aus}'.`;
            } else {
                ex.question = `[Giới từ 'in' với Quốc gia có mạo từ (Random)]: Điền cụm giới từ 'ở tại' cho quốc gia '${chosen.country}': "Herr Meier wohnt ___."`;
                ex.correct_answer = chosen.in;
                ex.explanation = `'${chosen.country}' ở Dativ khi đi với giới từ 'in' là '${chosen.in}'.`;
            }
        } else {
            ex.question = `[Ngôn ngữ Quốc gia (Random)]: Ngôn ngữ chính được nói tại '${chosen.country}' là gì? (Ví dụ: Deutsch, Französisch, Spanisch...):`;
            ex.correct_answer = chosen.lang;
            ex.explanation = `Tại '${chosen.country}', ngôn ngữ chính là: '${chosen.lang}'.`;
        }
        return ex;
    }

    // 10. Xử lý câu hỏi Chuyển đổi Câu hỏi W-Frage & Ja/Nein-Frage (dynamic_question_transform - Bài 3)
    if (extra.dynamic_question_transform) {
        const sentencePool = [
            {
                statement: "Ich heiße Anna.",
                wQuestion: "Wie heißen Sie?",
                wAlt: "Wie heißt du?",
                jnQuestion: "Heißen Sie Anna?",
                jnAlt: "Heißt du Anna?",
                meaning: "Tôi tên là Anna."
            },
            {
                statement: "Ich wohne in Hai Phong.",
                wQuestion: "Wo wohnen Sie?",
                wAlt: "Wo wohnst du?",
                jnQuestion: "Wohnen Sie in Hai Phong?",
                jnAlt: "Wohnst du in Hai Phong?",
                meaning: "Tôi sống ở Hải Phòng."
            },
            {
                statement: "Er macht die Hausaufgaben.",
                wQuestion: "Was macht er?",
                wAlt: "Was macht er?",
                jnQuestion: "Macht er die Hausaufgaben?",
                jnAlt: "Macht er die Hausaufgaben?",
                meaning: "Anh ấy làm bài tập về nhà."
            },
            {
                statement: "Sie ist Lehrerin.",
                wQuestion: "Wer ist sie?",
                wAlt: "Was ist sie von Beruf?",
                jnQuestion: "Ist sie Lehrerin?",
                jnAlt: "Ist sie Lehrerin?",
                meaning: "Cô ấy là giáo viên."
            },
            {
                statement: "Carlos kommt aus Wien.",
                wQuestion: "Woher kommt Carlos?",
                wAlt: "Woher kommt er?",
                jnQuestion: "Kommt Carlos aus Wien?",
                jnAlt: "Kommt er aus Wien?",
                meaning: "Carlos đến từ Viên."
            },
            {
                statement: "Hanoi liegt im Norden von Vietnam.",
                wQuestion: "Wo liegt Hanoi?",
                wAlt: "Wo liegt Hanoi?",
                jnQuestion: "Liegt Hanoi im Norden von Vietnam?",
                jnAlt: "Liegt Hanoi im Norden von Vietnam?",
                meaning: "Hà Nội nằm ở miền Bắc Việt Nam."
            }
        ];

        const chosen = sentencePool[Math.floor(Math.random() * sentencePool.length)];
        const askW = Math.random() > 0.5;

        if (askW) {
            ex.question = `[Chuyển sang W-Frage (Random)]: Hãy chuyển câu trần thuật "${chosen.statement}" (${chosen.meaning}) sang câu hỏi có từ để hỏi (W-Frage):`;
            ex.correct_answer = `${chosen.wQuestion} / ${chosen.wAlt}`;
            ex.explanation = `Câu hỏi W-Frage tương ứng là: '${chosen.wQuestion}' (hoặc thân mật: '${chosen.wAlt}').`;
        } else {
            ex.question = `[Chuyển sang Ja/Nein-Frage (Random)]: Hãy chuyển câu trần thuật "${chosen.statement}" (${chosen.meaning}) sang câu hỏi Có/Không (Ja/Nein-Frage):`;
            ex.correct_answer = `${chosen.jnQuestion} / ${chosen.jnAlt}`;
            ex.explanation = `Đẩy động từ lên đầu câu để tạo Ja/Nein-Frage: '${chosen.jnQuestion}' (hoặc: '${chosen.jnAlt}').`;
        }
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
            if (extra.dynamic_number || extra.dynamic_mode || extra.dynamic_price || extra.dynamic_conjugation || extra.dynamic_article_quiz || extra.dynamic_possessive_article || extra.dynamic_plural_quiz || extra.dynamic_direction_quiz || extra.dynamic_landmark_quiz || extra.dynamic_praeteritum_quiz || extra.dynamic_country_language_quiz || extra.dynamic_question_transform) isDynamic = true;
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
