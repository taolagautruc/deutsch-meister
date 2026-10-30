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
 * So sánh đáp án tiếng Đức & Việt thông minh, toàn diện:
 * 1. Chấp nhận danh sách đáp án tương đương qua dấu '/', '||', '\n', 'hoặc'.
 * 2. Bỏ qua toàn bộ dấu câu (chấm, phẩy, chấm than, chấm hỏi, ngoặc kép, gạch ngang) và chuẩn hóa khoảng trắng.
 * 3. Chuẩn hóa tiếng Đức: ß <-> ss, ä <-> ae, ö <-> oe, ü <-> ue.
 * 4. Chuẩn hóa giới thiệu bản thân:
 *    "ich heiße [Tên]" <-> "ich bin [Tên]" <-> "mein name ist [Tên]"
 *    "hallo" <-> "hi" <-> "guten tag"
 * 5. Chuẩn hóa địa danh Việt Nam:
 *    "hai phong" <-> "hải phòng" <-> "haiphong"
 *    "ha noi" <-> "hà nội" <-> "hanoi"
 *    "da nang" <-> "đà nẵng" <-> "danang"
 *    "viet nam" <-> "việt nam" <-> "vietnam"
 * 6. Chuẩn hóa đại từ tiếng Việt:
 *    "ngài" <-> "bạn" <-> "anh" <-> "chị" <-> "ông" <-> "bà" <-> "bác"
 *    "chúng mình" <-> "chúng tôi" <-> "chúng ta"
 * 7. Hoán vị vế liên từ "und" / "và":
 *    "A und B" <-> "B und A"
 * 8. Đảo ngữ vị trí trạng từ:
 *    "gestern waren Paula und ich in..." <-> "Paula und ich waren gestern in..."
 *    "gestern war ich..." <-> "ich war gestern..."
 * 9. Chuẩn hóa giá tiền Euro:
 *    "4,50" <-> "4.50" <-> "4,50 €" <-> "4,50 euro"
 * 10. Chuẩn hóa số đếm:
 *    "5" <-> "fünf", "einhundert" <-> "hundert", v.v.
 */
function checkGermanAnswerEquivalence(userAns, correctAns) {
    if (!userAns || !correctAns) return false;

    // 1. Phân tách nếu có nhiều phương án đáp án chuẩn (cách nhau bởi /, ||, \n, hoặc)
    if (correctAns.includes('/') || correctAns.includes('||') || correctAns.includes('\n') || /\s+hoặc\s+/i.test(correctAns)) {
        const alts = correctAns.split(/\/|\|\||\n|\s+hoặc\s+/i).map(a => a.trim()).filter(Boolean);
        if (alts.some(alt => checkGermanAnswerEquivalence(userAns, alt))) {
            return true;
        }
    }

    // 2. Chuẩn hóa cơ bản: chữ thường, bỏ toàn bộ dấu câu
    const baseClean = (s) => String(s)
        .trim()
        .toLowerCase()
        .replace(/[.,!?;:\"\'„“”«»‘`’–—\-\(\)\[\]\{\}\/\\~]+/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();

    const u0 = baseClean(userAns);
    const c0 = baseClean(correctAns);

    if (u0 === c0) return true;

    // 3. Chuẩn hóa tiếng Đức: ß -> ss, ä -> ae, ö -> oe, ü -> ue
    const deGermanize = (s) => s
        .replace(/ß/g, 'ss')
        .replace(/ä/g, 'ae')
        .replace(/ö/g, 'oe')
        .replace(/ü/g, 'ue');

    const uDe = deGermanize(u0);
    const cDe = deGermanize(c0);
    if (uDe === cDe) return true;

    // 4. Bỏ khoảng trắng hoàn toàn (từ ghép, số đếm hoặc gõ liền)
    const uNoSpace = uDe.replace(/\s+/g, '');
    const cNoSpace = cDe.replace(/\s+/g, '');
    if (uNoSpace === cNoSpace) return true;

    // 5. Chuẩn hóa số đếm: einhundert <-> hundert, eintausend <-> tausend
    const normalizeHundredsThousands = (s) => s
        .replace(/einhundert/g, 'hundert')
        .replace(/eintausend/g, 'tausend');
    if (normalizeHundredsThousands(uNoSpace) === normalizeHundredsThousands(cNoSpace)) return true;

    // 6. Số tự nhiên <-> Chữ số tiếng Đức (0-9999 dùng numberToGerman)
    const expandAllIntegersToWords = (str) => {
        if (!str) return '';
        return str.replace(/\b(\d{1,4})\b/g, (match, d) => {
            const n = parseInt(d, 10);
            const g = (typeof numberToGerman === 'function') ? numberToGerman(n) : '';
            return g ? deGermanize(g) : match;
        });
    };

    // 7. Chuẩn hóa giá tiền Euro: Chuyển đổi số tiền thập phân sang chữ (3,99 -> drei Euro neunundneunzig)
    const expandPricesToGermanWords = (str) => {
        if (!str) return '';
        return str.replace(/(\d+)[.,](\d{1,2})(?:\s*(?:euro|€))?/gi, (match, euros, cents) => {
            const e = parseInt(euros, 10);
            let c = parseInt(cents, 10);
            if (cents.length === 1) c = c * 10;
            const pw = (typeof priceToGerman === 'function') ? priceToGerman(e, c) : '';
            return pw ? deGermanize(pw) : match;
        });
    };

    // So sánh sau khi đã mở rộng số và giá tiền sang chữ tiếng Đức
    const uFullExp = deGermanize(baseClean(expandAllIntegersToWords(expandPricesToGermanWords(userAns))));
    const cFullExp = deGermanize(baseClean(expandAllIntegersToWords(expandPricesToGermanWords(correctAns))));
    if (uFullExp === cFullExp) return true;
    if (uFullExp.replace(/\s+/g, '') === cFullExp.replace(/\s+/g, '')) return true;

    // Chuẩn hóa các cụm từ tính tiền / giá tiền tương đương:
    const normalizePricePhrases = (s) => {
        let res = s;
        res = res.replace(/\b(das macht|das kostet|es macht|es kostet|zusammen macht das|zusammen kostet das|zusammen macht|zusammen kostet|zusammen ist das|zusammen)\b/g, '__PRICE_VERB__');
        res = res.replace(/\bcent\b/g, '').replace(/\s+/g, ' ').trim();
        res = res.replace(/\beins euro\b/g, 'ein euro');
        return res;
    };
    const uP = normalizePricePhrases(uFullExp);
    const cP = normalizePricePhrases(cFullExp);
    if (uP === cP) return true;
    if (uP.replace(/\s+/g, '') === cP.replace(/\s+/g, '')) return true;

    // Chấp nhận có hoặc không có từ "euro" khi đọc giá tiền:
    const uNoEuro = uP.replace(/\beuro\b/g, '').replace(/\s+/g, ' ').trim();
    const cNoEuro = cP.replace(/\beuro\b/g, '').replace(/\s+/g, ' ').trim();
    if (uNoEuro === cNoEuro) return true;
    if (uNoEuro.replace(/\s+/g, '') === cNoEuro.replace(/\s+/g, '')) return true;

    // Chấp nhận người học chỉ nhập giá tiền (bỏ qua động từ das macht/zusammen):
    const uPNoVerb = uP.replace(/__PRICE_VERB__/g, '').replace(/\s+/g, ' ').trim();
    const cPNoVerb = cP.replace(/__PRICE_VERB__/g, '').replace(/\s+/g, ' ').trim();
    if (uPNoVerb && cPNoVerb) {
        if (uPNoVerb === cPNoVerb) return true;
        if (uPNoVerb.replace(/\s+/g, '') === cPNoVerb.replace(/\s+/g, '')) return true;
        const uPVNoEuro = uPNoVerb.replace(/\beuro\b/g, '').replace(/\s+/g, ' ').trim();
        const cPVNoEuro = cPNoVerb.replace(/\beuro\b/g, '').replace(/\s+/g, ' ').trim();
        if (uPVNoEuro && cPVNoEuro) {
            if (uPVNoEuro === cPVNoEuro) return true;
            if (uPVNoEuro.replace(/\s+/g, '') === cPVNoEuro.replace(/\s+/g, '')) return true;
        }
    }

    // Chuẩn hóa giá tiền Euro số thuần: "4,50" <-> "4.50" <-> "4,50 euro" <-> "4,50 €"
    const cleanPrice = (s) => String(s).toLowerCase()
        .replace(/euro/g, '')
        .replace(/€/g, '')
        .replace(/\./g, ',')
        .replace(/\s+/g, '')
        .trim();
    if (cleanPrice(userAns) === cleanPrice(correctAns) && cleanPrice(correctAns).includes(',')) return true;

    // Chuẩn hóa loại bỏ chữ "cent" ở cuối khi so sánh chữ đọc giá tiền
    const uNoCent = uDe.replace(/\s*cent$/g, '').replace(/eins euro/g, 'ein euro');
    const cNoCent = cDe.replace(/\s*cent$/g, '').replace(/eins euro/g, 'ein euro');
    if (uNoCent === cNoCent) return true;

    // 8. Chuẩn hóa tiếng Việt (bỏ dấu) & tên địa danh:
    const stripVnAccents = (str) => {
        return str
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/đ/g, "d")
            .replace(/Đ/g, "D");
    };

    const normalizeLocations = (s) => {
        let res = stripVnAccents(s);
        res = res.replace(/\b(hải phòng|hai phong|haiphong)\b/gi, 'haiphong');
        res = res.replace(/\b(hà nội|ha noi|hanoi)\b/gi, 'hanoi');
        res = res.replace(/\b(đà nẵng|da nang|danang)\b/gi, 'danang');
        res = res.replace(/\b(việt nam|viet nam|vietnam)\b/gi, 'vietnam');
        res = res.replace(/\b(sài gòn|sai gon|saigon|tphcm)\b/gi, 'saigon');
        res = res.replace(/\b(long an|longan)\b/gi, 'longan');
        return res;
    };

    const uLoc = normalizeLocations(uDe);
    const cLoc = normalizeLocations(cDe);
    if (uLoc === cLoc) return true;

    // 9. Giới thiệu bản thân trong tiếng Đức:
    // "ich heiße / heisse" <-> "ich bin" <-> "mein name ist"
    // Lời chào: "hallo" <-> "hi" <-> "guten tag"
    const normalizeIntro = (s) => {
        let res = s;
        res = res.replace(/^(guten tag|hallo|hi)\b/, '__GREET__');
        res = res.replace(/\b(ich heisse|ich bin|mein name ist)\b/g, '__INTRO_NAME__');
        res = res.replace(/\bund ich wohne\b/g, 'ich wohne');
        return res;
    };
    if (normalizeIntro(uLoc) === normalizeIntro(cLoc)) return true;

    // 10. Hoán vị hai vế liên kết bằng "und", "và", hoặc dấu phẩy & từ đồng nghĩa đồ nội thất:
    const normalizeFurniture = (s) => s
        .replace(/\bbuecherregal\b/g, 'regal')
        .replace(/\bfernsehgeraet\b/g, 'fernseher');

    const uFurn = normalizeFurniture(uDe);
    const cFurn = normalizeFurniture(cDe);
    if (uFurn === cFurn) return true;

    const swap1Word = (s) => s.replace(/(\b[a-z0-9äöüß]+\b)\s+(und|va|và)\s+(\b[a-z0-9äöüß]+\b)/gi, '$3 $2 $1');
    const swap2Word = (s) => s.replace(/(\b[a-z0-9äöüß]+\s+[a-z0-9äöüß]+\b)\s+(und|va|và)\s+(\b[a-z0-9äöüß]+\s+[a-z0-9äöüß]+\b)/gi, '$3 $2 $1');
    const swapNounPairs = (s) => s.replace(/\b((?:einen|ein|eine|der|die|das|den)\s+[a-z0-9äöüß]+)\s+(und|va|và)\s+((?:einen|ein|eine|der|die|das|den)\s+[a-z0-9äöüß]+)\b/gi, '$3 $2 $1');

    for (const swapper of [swap1Word, swap2Word, swapNounPairs]) {
        if (swapper(uLoc) === cLoc || uLoc === swapper(cLoc) || swapper(uLoc) === swapper(cLoc)) return true;
        if (swapper(uDe) === cDe || uDe === swapper(cDe)) return true;
        if (swapper(uFurn) === cFurn || uFurn === swapper(cFurn) || swapper(uFurn) === swapper(cFurn)) return true;
    }

    // 11. Đảo ngữ trạng từ đầu câu trong tiếng Đức:
    const normalizeAdverbInversion = (s) => {
        let res = s;
        res = res.replace(/^gestern waren paula und ich\b/, 'paula und ich waren gestern');
        res = res.replace(/^gestern war ich\b/, 'ich war gestern');
        res = res.replace(/^gestern waren wir\b/, 'wir waren gestern');
        res = res.replace(/^heute trinken wir\b/, 'wir trinken heute');
        res = res.replace(/^heute habe ich\b/, 'ich habe heute');
        return res;
    };
    if (normalizeAdverbInversion(uLoc) === normalizeAdverbInversion(cLoc)) return true;

    // 12. Gọi đồ uống / thanh toán trong tiếng Đức:
    const normalizeOrder = (s) => {
        let res = s;
        res = res.replace(/\b(ich trinke|ich nehme|ich moechte)\b/g, '__ORDER__');
        res = res.replace(/\b(wir moechten bitte zahlen|wir moechten zahlen bitte|wir moechten zahlen|wir moechten bezahlen|zahlen bitte|wir zahlen bitte|wir zahlen|bitte zahlen)\b/g, '__PAY__');
        res = res.replace(/\b(zusammen oder getrennt bitte|zusammen oder getrennt)\b/g, '__PAY_SPLIT__');
        res = res.replace(/\b(tee ohne zucker bitte|einen tee ohne zucker bitte|tee ohne zucker|einen tee ohne zucker)\b/g, '__TEA_NO_SUGAR__');
        res = res.replace(/\b(kaffee mit viel milch|einen kaffee mit viel milch|kaffee mit viel milch bitte|einen kaffee mit viel milch bitte)\b/g, '__COFFEE_MILK__');
        return res;
    };
    if (normalizeOrder(uDe) === normalizeOrder(cDe)) return true;

    // 13. Câu hỏi tương đương (Wie heißen Sie <-> Wie heißt du, v.v.):
    const normalizeQuestions = (s) => {
        let res = s;
        res = res.replace(/\bwie heissen sie\b/g, '__Q_NAME__');
        res = res.replace(/\bwie heisst du\b/g, '__Q_NAME__');
        res = res.replace(/\bwie ist ihr name\b/g, '__Q_NAME__');
        res = res.replace(/\bwie ist dein name\b/g, '__Q_NAME__');
        res = res.replace(/\bwo wohnen sie\b/g, '__Q_LIVE__');
        res = res.replace(/\bwo wohnst du\b/g, '__Q_LIVE__');
        res = res.replace(/\bwoher kommen sie\b/g, '__Q_FROM__');
        res = res.replace(/\bwoher kommst du\b/g, '__Q_FROM__');
        res = res.replace(/\bwas moechten sie trinken\b/g, '__Q_DRINK__');
        res = res.replace(/\bwas moechtest du trinken\b/g, '__Q_DRINK__');
        res = res.replace(/\bwas trinken sie\b/g, '__Q_DRINK__');
        res = res.replace(/\bwas trinkst du\b/g, '__Q_DRINK__');
        res = res.replace(/\b(entschuldigung wie bitte|wie bitte)\b/g, '__PARDON__');
        res = res.replace(/\b(koennen sie das bitte buchstabieren|koennen sie das buchstabieren bitte|koennen sie bitte das buchstabieren|koennen sie das wort bitte buchstabieren|koennen sie bitte buchstabieren|koennen sie buchstabieren bitte|buchstabieren sie das bitte)\b/g, '__SPELL__');
        res = res.replace(/\b(koennen sie das bitte anschreiben|koennen sie das anschreiben bitte|koennen sie bitte das anschreiben|koennen sie das bitte an die tafel schreiben|schreiben sie das bitte an)\b/g, '__WRITE_BOARD__');
        res = res.replace(/\b(koennen sie das bitte wiederholen|koennen sie das wiederholen bitte|koennen sie bitte das wiederholen|koennen sie bitte wiederholen|koennen sie wiederholen bitte|wiederholen sie das bitte)\b/g, '__REPEAT__');
        return res;
    };
    if (normalizeQuestions(uDe) === normalizeQuestions(cDe)) return true;

    // Linh hoạt câu nhờ vả với "Können Sie ...": chấp nhận mọi vị trí của "bitte" và "das" tùy chọn
    if (uDe.startsWith('koennen sie') && cDe.startsWith('koennen sie')) {
        const normPolite = (s) => s.replace(/\bbitte\b/g, '').replace(/\bdas\b/g, '').replace(/\s+/g, ' ').trim();
        if (normPolite(uDe) === normPolite(cDe)) return true;
    }

    // 14. Dịch sang tiếng Việt - Linh hoạt đại từ nhân xưng & từ đồng nghĩa:
    const normalizeVnPronouns = (s) => {
        const stripped = stripVnAccents(s);
        return stripped
            .replace(/€|\beuro\b/gi, '__CURR_EUR__')
            .replace(/\b(dong|vnd|d)\b/gi, '__CURR_VND__')
            .replace(/\b(tong cong het|tong cong la|tong la|het|tong cong|tat ca het|tat ca la)\b/gi, '__TOTAL_PRICE__')
            .replace(/\b(ngai|ban|anh|chi|ong|ba|bac|em|thay|co)\b/gi, '__PRON_2ND__')
            .replace(/\b(chung minh|chung toi|chung ta)\b/gi, '__PRON_1ST_PL__')
            .replace(/\b(toi|minh|ta|tui)\b/gi, '__PRON_1ST_SG__')
            .replace(/\b(cai nay|dieu nay|cai do|dieu do|do)\b/gi, '__THIS__')
            .replace(/\b(mot|1)\b/gi, '1')
            .replace(/\b(khu vuon|cai vuon|vuon)\b/gi, 'vuon')
            .replace(/\b(quyen vo|cuon vo|vo)\b/gi, 'vo')
            .replace(/\b(quyen tu dien|cuon tu dien|tu dien)\b/gi, 'tudien')
            .replace(/\b(chiec dien thoai|cai dien thoai|dien thoai)\b/gi, 'dienthoai')
            .replace(/\b(rat dep|dep)\b/gi, 'dep')
            .replace(/\b(nho qua|qua nho)\b/gi, 'quanho')
            .replace(/\b(lap lai|nhac lai)\b/gi, 'nhaclai')
            .replace(/\b(vui long|lam on)\b/gi, 'lamon')
            .replace(/\b(goi la gi|la gi|ten la gi)\b/gi, 'lagi');
    };
    if (normalizeVnPronouns(u0) === normalizeVnPronouns(c0)) return true;

    // 15. Câu đọc hiểu điền ngắn: bỏ mạo từ ở đầu câu
    const stripArticle = (s) => s.replace(/^(einen|ein|eine|der|die|das)\s+/i, '');
    if (stripArticle(uLoc) === stripArticle(cLoc)) return true;

    // 16. So sánh cặp số cách nhau dấu phẩy (ví dụ: "83, 92" <-> "83 và 92" <-> "dreiundachtzig, zweiundneunzig")
    if (c0.includes(',') || c0.includes(' und ') || c0.includes(' và ')) {
        const splitPairs = (str) => str.split(/,|\bund\b|\bvà\b|\bva\b/).map(p => baseClean(p).replace(/\s+/g, '')).filter(Boolean);
        const uParts = splitPairs(userAns);
        const cParts = splitPairs(correctAns);
        if (uParts.length === 2 && cParts.length === 2) {
            const match1 = (checkGermanAnswerEquivalence(uParts[0], cParts[0]) && checkGermanAnswerEquivalence(uParts[1], cParts[1]));
            const match2 = (checkGermanAnswerEquivalence(uParts[0], cParts[1]) && checkGermanAnswerEquivalence(uParts[1], cParts[0]));
            if (match1 || match2) return true;
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
            extra.translation = `Nhân viên phục vụ nói: Tổng cộng hết ${formattedPrice} € (${dePrice}).`;
            ex.extra_data = JSON.stringify(extra);
            ex.question = `[Luyện Nghe giá tiền Euro (Random)]: Nghe câu thông báo của nhân viên phục vụ và điền số tiền:`;
            ex.correct_answer = formattedPrice;
            ex.explanation = `Nhân viên phục vụ nói '${extra.audio_text}' → Số tiền là ${formattedPrice} € (hoặc gõ ${dePrice}).`;
        } else {
            extra.translation = `Giá tiền: ${formattedPrice} € (${dePrice})`;
            ex.extra_data = JSON.stringify(extra);
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
        extra.translation = `'${chosenSubject.label}' ${chosenVerb.meaning}: ${chosenSubject.pronoun} ${correctForm}`;
        ex.extra_data = JSON.stringify(extra);
        return ex;
    }

    // 3. Xử lý câu hỏi Mạo từ & Phủ định (dynamic_article_quiz)
    if (extra.dynamic_article_quiz) {
        const allowedCategories = ['Đồ dùng lớp học', 'Nội thất & Đồ đạc'];
        const excludedWords = ['Hausaufgabe', 'Tafel', 'verstehen', 'wiederholen', 'buchstabieren', 'anschreiben', 'können'];
        const db = (typeof GERMAN_LEXIKON_DB !== 'undefined' && GERMAN_LEXIKON_DB.length > 0)
            ? GERMAN_LEXIKON_DB.filter(x => 
                allowedCategories.includes(x.category) && 
                !excludedWords.includes(x.word) &&
                (x.gender === 'der' || x.gender === 'die' || x.gender === 'das')
              )
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
        extra.translation = `Không, đó không phải là một ${item1.meaning}. Đó là một ${item2.meaning}.`;
        ex.extra_data = JSON.stringify(extra);
        return ex;
    }

    // 4. Xử lý câu hỏi Sở hữu với Mạo từ xác định (dynamic_possessive_article)
    if (extra.dynamic_possessive_article) {
        const allowedCategories = ['Đồ dùng lớp học', 'Nội thất & Đồ đạc'];
        const excludedWords = ['Hausaufgabe', 'Tafel', 'Landkarte', 'Whiteboard', 'verstehen', 'können'];
        const db = (typeof GERMAN_LEXIKON_DB !== 'undefined' && GERMAN_LEXIKON_DB.length > 0)
            ? GERMAN_LEXIKON_DB.filter(x => 
                allowedCategories.includes(x.category) && 
                !excludedWords.includes(x.word) &&
                (x.gender === 'der' || x.gender === 'die' || x.gender === 'das')
              )
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
        extra.translation = `Vâng, đó là ${chosenItem.meaning} của ${chosenName}.`;
        ex.extra_data = JSON.stringify(extra);
        return ex;
    }

    // 5. Xử lý câu hỏi Số nhiều danh từ (dynamic_plural_quiz)
    if (extra.dynamic_plural_quiz) {
        const allowedCategories = ['Đồ dùng lớp học', 'Nội thất & Đồ đạc', 'Nhà ở & Phòng ốc'];
        const excludedWords = ['Hausaufgabe', 'verstehen', 'können'];
        const db = (typeof GERMAN_LEXIKON_DB !== 'undefined' && GERMAN_LEXIKON_DB.length > 0)
            ? GERMAN_LEXIKON_DB.filter(x => 
                allowedCategories.includes(x.category) && 
                !excludedWords.includes(x.word) &&
                x.gender !== 'verb' && x.plural && x.plural.startsWith('die ')
              )
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
        extra.translation = `'${chosenItem.plural}' = những ${chosenItem.meaning || chosenItem.word}`;
        ex.extra_data = JSON.stringify(extra);
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
        extra.translation = `${chosen.city} nằm ở ${chosen.vi} của ${chosen.country}.`;
        ex.extra_data = JSON.stringify(extra);
        return ex;
    }

    // 7. Xử lý câu hỏi Ngữ pháp Quá khứ Präteritum & Giới từ (dynamic_landmark_quiz - Bài 3)
    if (extra.dynamic_landmark_quiz) {
        const grammarItems = [
            {
                q: "Chọn dạng quá khứ (Präteritum) đúng của động từ 'sein' cho chủ ngữ 'Paula und ich': \"Gestern ___ Paula und ich in Haiphong.\"",
                ans: "waren",
                options: ["waren", "war", "warst", "wart"],
                expl: "'Paula und ich' tương đương ngôi 'wir' (chúng tôi) → dạng quá khứ của 'sein' là 'waren'."
            },
            {
                q: "Chọn dạng quá khứ (Präteritum) đúng của động từ 'sein' cho ngôi 'du': \"___ du schon einmal in Deutschland?\"",
                ans: "Warst",
                options: ["Warst", "Wart", "War", "Waren"],
                expl: "Ngôi 'du' đi với quá khứ của 'sein' là 'warst' (đảo lên đầu câu viết hoa thành 'Warst')."
            },
            {
                q: "Chọn dạng quá khứ (Präteritum) đúng của động từ 'sein' cho ngôi 'ihr': \"Gestern ___ ihr im Theater, đúng không?\"",
                ans: "wart",
                options: ["wart", "warst", "waren", "war"],
                expl: "Ngôi 'ihr' đi với quá khứ của 'sein' chia là 'wart'."
            },
            {
                q: "Điền mạo từ thích hợp ở Dativ đi sau giới từ 'aus' cho quốc gia giống cái 'die Schweiz': \"Frau Müller kommt aus ___ Schweiz.\"",
                ans: "der",
                options: ["der", "die", "den", "dem"],
                expl: "'die Schweiz' là quốc gia có mạo từ giống cái, sau giới từ 'aus' (Dativ) mạo từ 'die' chuyển thành 'der' → 'aus der Schweiz'."
            },
            {
                q: "Điền mạo từ thích hợp ở Dativ đi sau giới từ 'in' cho quốc gia giống đực 'der Iran': \"Herr Meier wohnt in ___ Iran.\"",
                ans: "dem",
                options: ["dem", "der", "den", "das"],
                expl: "'der Iran' là quốc gia giống đực, sau giới từ 'in' (Dativ) mạo từ 'der' chuyển thành 'dem' (hoặc viết tắt là 'im')."
            },
            {
                q: "Điền mạo từ thích hợp ở Dativ đi sau giới từ 'in' cho quốc gia số nhiều 'die USA': \"David lebt in ___ USA.\"",
                ans: "den",
                options: ["den", "der", "die", "dem"],
                expl: "'die USA' là danh từ số nhiều, sau giới từ 'in' (Dativ số nhiều) mạo từ đổi thành 'den' → 'in den USA'."
            },
            {
                q: "Đâu là câu hỏi Có/Không (Ja/Nein-Frage) có trật tự từ ĐÚNG ngữ pháp tiếng Đức?",
                ans: "Wohnen Sie in Hai Phong?",
                options: ["Wohnen Sie in Hai Phong?", "Sie wohnen in Hai Phong?", "Wo wohnen Sie in Hai Phong?", "In Hai Phong wohnen Sie?"],
                expl: "Trong câu hỏi Có/Không (Ja/Nein-Frage), động từ bắt buộc phải đảo lên vị trí đầu câu (vị trí 1)."
            },
            {
                q: "Khi miêu tả vị trí bằng TÍNH TỪ phương hướng (-lich), câu nào sau đây ĐÚNG ngữ pháp?",
                ans: "Köln liegt westlich von Deutschland.",
                options: ["Köln liegt westlich von Deutschland.", "Köln liegt im westlich von Deutschland.", "Köln liegt am westlich von Deutschland.", "Köln liegt westlichen von Deutschland."],
                expl: "Tính từ phương hướng có đuôi '-lich' đứng độc lập sau 'liegt' và tuyệt đối KHÔNG có giới từ 'im' phía trước."
            }
        ];

        const chosen = grammarItems[Math.floor(Math.random() * grammarItems.length)];
        const shuffled = [...chosen.options].sort(() => Math.random() - 0.5);

        ex.question = `[Ngữ pháp Trọng tâm (Random)]: ${chosen.q}`;
        ex.correct_answer = chosen.ans;
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.explanation = chosen.expl;
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

    // 11. Xử lý câu hỏi Phân biệt Nominativ vs. Akkusativ (dynamic_nom_akk_quiz - Bài 4)
    if (extra.dynamic_nom_akk_quiz) {
        const nomAkkItems = [
            { word: "Garten", gender: "der", meaning: "khu vườn" },
            { word: "Balkon", gender: "der", meaning: "ban công" },
            { word: "Flur", gender: "der", meaning: "hành lang" },
            { word: "Keller", gender: "der", meaning: "tầng hầm" },
            { word: "Schrank", gender: "der", meaning: "cái tủ" },
            { word: "Kühlschrank", gender: "der", meaning: "tủ lạnh" },
            { word: "Tisch", gender: "der", meaning: "cái bàn" },
            { word: "Stuhl", gender: "der", meaning: "cái ghế" },
            { word: "Teppich", gender: "der", meaning: "tấm thảm" },
            { word: "Spiegel", gender: "der", meaning: "cái gương" },
            { word: "Fernseher", gender: "der", meaning: "chiếc tivi" },
            { word: "Wohnung", gender: "die", meaning: "căn hộ" },
            { word: "Küche", gender: "die", meaning: "phòng bếp" },
            { word: "Garage", gender: "die", meaning: "nhà để xe" },
            { word: "Lampe", gender: "die", meaning: "cây đèn" },
            { word: "Spüle", gender: "die", meaning: "bồn rửa bát" },
            { word: "Toilette", gender: "die", meaning: "nhà vệ sinh" },
            { word: "Haus", gender: "das", meaning: "ngôi nhà" },
            { word: "Zimmer", gender: "das", meaning: "căn phòng" },
            { word: "Wohnzimmer", gender: "das", meaning: "phòng khách" },
            { word: "Schlafzimmer", gender: "das", meaning: "phòng ngủ" },
            { word: "Badezimmer", gender: "das", meaning: "phòng tắm" },
            { word: "Bett", gender: "das", meaning: "cái giường" },
            { word: "Bücherregal", gender: "das", meaning: "kệ sách" }
        ];

        const chosen = nomAkkItems[Math.floor(Math.random() * nomAkkItems.length)];
        const modeType = Math.floor(Math.random() * 4); // 0: haben (indefinite), 1: es gibt (indefinite), 2: finden (definite), 3: kein (negation)

        let answer = "";
        let qText = "";
        let ruleText = "";

        if (modeType === 0) {
            // haben + Akkusativ
            answer = chosen.gender === "der" ? "einen" : (chosen.gender === "die" ? "eine" : "ein");
            qText = `[Nominativ vs. Akkusativ (Random)]: Điền mạo từ bất định thích hợp vào chỗ trống: "Wir haben ___ ${chosen.word}." (${chosen.meaning})`;
            ruleText = `Động từ 'haben' đòi hỏi tân ngữ Akkusativ. Danh từ '${chosen.word}' mang giống '${chosen.gender}' → ${chosen.gender === 'der' ? 'chỉ giống đực đổi thành "einen"' : 'giống ' + chosen.gender + ' giữ nguyên là "' + answer + '"'}.`;
        } else if (modeType === 1) {
            // es gibt + Akkusativ
            answer = chosen.gender === "der" ? "einen" : (chosen.gender === "die" ? "eine" : "ein");
            qText = `[Nominativ vs. Akkusativ (Random)]: Điền mạo từ bất định thích hợp: "Oben gibt es ___ ${chosen.word}." (${chosen.meaning})`;
            ruleText = `Cấu trúc 'es gibt' luôn đòi hỏi Akkusativ. '${chosen.word}' mang giống '${chosen.gender}' → đáp án là '${answer}'.`;
        } else if (modeType === 2) {
            // finden + Akkusativ (definite)
            answer = chosen.gender === "der" ? "den" : (chosen.gender === "die" ? "die" : "das");
            qText = `[Nominativ vs. Akkusativ (Random)]: Điền mạo từ xác định thích hợp: "Ich finde ___ ${chosen.word} sehr schön." (${chosen.meaning})`;
            ruleText = `'finden' đòi hỏi Akkusativ xác định. '${chosen.word}' mang giống '${chosen.gender}' → ${chosen.gender === 'der' ? 'der đổi thành "den"' : 'giữ nguyên là "' + answer + '"'}.`;
        } else {
            // kein- + Akkusativ
            answer = chosen.gender === "der" ? "keinen" : (chosen.gender === "die" ? "keine" : "kein");
            qText = `[Nominativ vs. Akkusativ (Random)]: Điền từ phủ định thích hợp: "Die Wohnung hat ___ ${chosen.word}." (${chosen.meaning})`;
            ruleText = `'haben' + phủ định ở Akkusativ: '${chosen.word}' (${chosen.gender}) → '${answer}'.`;
        }

        if (ex.exercise_type === "trac_nghiem" || (ex.options && ex.options.length > 0)) {
            const allOpts = modeType === 2 ? ["den", "der", "die", "das"] : ["einen", "ein", "eine", "keinen"];
            if (!allOpts.includes(answer)) allOpts[0] = answer;
            const shuffled = Array.from(new Set(allOpts)).sort(() => Math.random() - 0.5);
            ex.options = shuffled;
            ex.options_json = JSON.stringify(shuffled);
        }

        ex.question = qText;
        ex.correct_answer = answer;
        ex.explanation = ruleText;
        return ex;
    }

    // 12. Xử lý câu hỏi Mạo từ sở hữu theo 9 Ngôi (dynamic_possessiv_quiz - Bài 4)
    if (extra.dynamic_possessiv_quiz) {
        const owners = [
            { label: "ich (tôi)", stem: "mein" },
            { label: "du (bạn)", stem: "dein" },
            { label: "er (anh ấy / Peter)", stem: "sein" },
            { label: "sie (cô ấy / Lena)", stem: "ihr" },
            { label: "wir (chúng tôi)", stem: "unser" },
            { label: "ihr (các bạn / Maria und Lukas)", stem: "euer", isEuer: true },
            { label: "sie (họ / die Eltern)", stem: "ihr" },
            { label: "Sie (Ngài / Herr Müller)", stem: "Ihr", isCapital: true }
        ];

        const nouns = [
            { word: "Garten", gender: "der", vi: "khu vườn" },
            { word: "Balkon", gender: "der", vi: "ban công" },
            { word: "Flur", gender: "der", vi: "hành lang" },
            { word: "Wohnung", gender: "die", vi: "căn hộ" },
            { word: "Küche", gender: "die", vi: "phòng bếp" },
            { word: "Tasche", gender: "die", vi: "túi xách" },
            { word: "Haus", gender: "das", vi: "ngôi nhà" },
            { word: "Zimmer", gender: "das", vi: "căn phòng" },
            { word: "Auto", gender: "das", vi: "chiếc ô tô" },
            { word: "Kinder", gender: "die_pl", vi: "những đứa con" }
        ];

        const owner = owners[Math.floor(Math.random() * owners.length)];
        const noun = nouns[Math.floor(Math.random() * nouns.length)];
        const isAkk = Math.random() > 0.5; // Nominativ vs Akkusativ

        let result = owner.stem;
        let ending = "";

        if (noun.gender === "der") {
            if (isAkk) {
                ending = "-en";
                if (owner.isEuer) {
                    result = "euren";
                } else {
                    result = owner.stem + "en";
                }
            } else {
                result = owner.stem;
            }
        } else if (noun.gender === "die" || noun.gender === "die_pl") {
            ending = "-e";
            if (owner.isEuer) {
                result = "eure";
            } else {
                result = owner.stem + "e";
            }
        } else {
            // das
            result = owner.stem;
        }

        const caseName = isAkk && noun.gender === "der" ? "Cách 4 (Akkusativ)" : (isAkk ? "Cách 4 (Akkusativ)" : "Cách 1 (Nominativ)");
        const sentenceContext = isAkk 
            ? `"Wir haben ___ ${noun.word}." hoặc "Ich mag ___ ${noun.word}."`
            : `"Das ist ___ ${noun.word}."`;

        ex.question = `[Mạo từ Sở Hữu 9 Ngôi (Random)]: Hãy chia mạo từ sở hữu của người sở hữu '${owner.label}' đứng trước danh từ '${noun.gender === 'die_pl' ? 'die (Pl.)' : noun.gender} ${noun.word}' (${noun.vi}) trong câu ${sentenceContext}:`;
        ex.correct_answer = result;
        ex.explanation = `Người sở hữu là '${owner.label}' → Gốc sở hữu '${owner.stem}'. Đi với danh từ '${noun.word}' (${noun.gender}) ở ${caseName} → dạng đúng là '${result}'${owner.isEuer && (ending === '-e' || ending === '-en') ? ' (lưu ý "euer" bị lược bỏ e ở giữa thành "' + result + '")' : ''}.`;
        return ex;
    }

    // 13. Xử lý câu hỏi Tính từ Đối lập Miêu tả Nhà cửa (dynamic_adjective_antonym_quiz - Bài 4)
    if (extra.dynamic_adjective_antonym_quiz) {
        const adjPairs = [
            { pos: "hell", neg: "dunkel", viPos: "sáng sủa", viNeg: "tối tăm", context: "Arbeitszimmer", nounVi: "phòng làm việc" },
            { pos: "groß", neg: "klein", viPos: "rộng lớn", viNeg: "nhỏ hẹp", context: "Wohnzimmer", nounVi: "phòng khách" },
            { pos: "leise", neg: "laut", viPos: "yên tĩnh", viNeg: "ồn ào", context: "Schlafzimmer", nounVi: "phòng ngủ" },
            { pos: "lang", neg: "kurz", viPos: "dài", viNeg: "ngắn", context: "Flur", nounVi: "hành lang" },
            { pos: "neu", neg: "alt", viPos: "mới", viNeg: "cũ / cổ", context: "Haus", nounVi: "ngôi nhà" },
            { pos: "billig", neg: "teuer", viPos: "rẻ", viNeg: "đắt đỏ", context: "Wohnung", nounVi: "căn hộ" },
            { pos: "schön", neg: "hässlich", viPos: "đẹp", viNeg: "xấu xí", context: "Garten", nounVi: "khu vườn" }
        ];

        const pair = adjPairs[Math.floor(Math.random() * adjPairs.length)];
        const testPos = Math.random() > 0.5;
        const sourceWord = testPos ? pair.pos : pair.neg;
        const sourceVi = testPos ? pair.viPos : pair.viNeg;
        const targetWord = testPos ? pair.neg : pair.pos;
        const targetVi = testPos ? pair.viNeg : pair.viPos;

        const subType = Math.random() > 0.5 ? "opposite" : "sentence";

        if (subType === "opposite") {
            ex.question = `[Tính từ Đối lập (Random)]: Từ trái nghĩa (Gegenteil) trong tiếng Đức của tính từ '${sourceWord}' (${sourceVi}) là gì?`;
            ex.correct_answer = targetWord;
            ex.explanation = `Tính từ '${sourceWord}' (${sourceVi}) có từ đối lập là '${targetWord}' (${targetVi}).`;
        } else {
            ex.question = `[Tính từ Miêu tả Nhà cửa (Random)]: Hoàn thành câu miêu tả sau bằng tính từ trái nghĩa với '${sourceWord}': "Das ${pair.context} ist nicht ${sourceWord}, sondern es ist ___."`;
            ex.correct_answer = targetWord;
            ex.explanation = `Từ đối lập với '${sourceWord}' (${sourceVi}) là '${targetWord}' (${targetVi}) → "Das ${pair.context} ist nicht ${sourceWord}, sondern es ist ${targetWord}."`;
        }
        return ex;
    }

    // 14. Xử lý câu hỏi Thay thế Đại từ Nhân xưng theo Giống (dynamic_pronoun_replacement_quiz - Bài 4)
    if (extra.dynamic_pronoun_replacement_quiz) {
        const pronounItems = [
            { word: "Flur", gender: "der", pronoun: "Er", sentence: "Das Haus hat einen Flur. ___ ist lang und dunkel." },
            { word: "Garten", gender: "der", pronoun: "Er", sentence: "Wir haben einen Garten. ___ ist groß und sehr schön." },
            { word: "Balkon", gender: "der", pronoun: "Er", sentence: "Oben gibt es einen Balkon. ___ ist sonnig und hell." },
            { word: "Kühlschrank", gender: "der", pronoun: "Er", sentence: "Er kauft einen Kühlschrank. ___ ist modern und neu." },
            { word: "Küche", gender: "die", pronoun: "Sie", sentence: "Die Wohnung hat eine Küche. ___ ist klein, aber gemütlich." },
            { word: "Wohnung", gender: "die", pronoun: "Sie", sentence: "Wir mieten eine Wohnung. ___ hat 4 Zimmer." },
            { word: "Garage", gender: "die", pronoun: "Sie", sentence: "Das Haus hat eine Garage. ___ ist sehr praktisch." },
            { word: "Wohnzimmer", gender: "das", pronoun: "Es", sentence: "Wir haben ein Wohnzimmer. ___ ist hell und modern." },
            { word: "Haus", gender: "das", pronoun: "Es", sentence: "Julia hat ein Haus. ___ ist sehr alt und hat 5 Zimmer." },
            { word: "Schlafzimmer", gender: "das", pronoun: "Es", sentence: "Mein Haus hat ein Schlafzimmer. ___ ist leise und warm." }
        ];

        const item = pronounItems[Math.floor(Math.random() * pronounItems.length)];
        ex.question = `[Đại từ Thay thế theo Giống (Random)]: Điền đại từ nhân xưng thích hợp ('Er' / 'Sie' / 'Es') thay thế cho danh từ giống '${item.gender}' (${item.word}): "${item.sentence}"`;
        ex.correct_answer = item.pronoun;
        ex.explanation = `'${item.word}' mang giống '${item.gender}' nên đại từ nhân xưng làm chủ ngữ thay thế ở câu sau là '${item.pronoun}' (der → er, die → sie, das → es).`;
        return ex;
    }

    // 15. Xử lý câu hỏi Dịch câu Miêu tả Phòng & Nội thất (dynamic_house_translation_quiz - Bài 4)
    if (extra.dynamic_house_translation_quiz) {
        const translationPool = [
            {
                vi: "Tôi có một ngôi nhà. Ngôi nhà của tôi có 5 phòng.",
                de: "Ich habe ein Haus. Mein Haus hat 5 Zimmer.",
                note: "das Haus đứng sau habe (Akkusativ) → ein Haus; làm chủ ngữ → Mein Haus."
            },
            {
                vi: "Phòng khách của tôi thì sáng và hiện đại.",
                de: "Mein Wohnzimmer ist hell und modern.",
                note: "das Wohnzimmer (giống trung) → Mein Wohnzimmer; tính từ sau ist giữ nguyên."
            },
            {
                vi: "Nó có 1 Tivi và 1 giá sách.",
                de: "Es hat einen Fernseher und ein Bücherregal.",
                note: "der Fernseher (giống đực) sau hat đổi thành einen Fernseher; das Bücherregal giữ nguyên ein."
            },
            {
                vi: "Phòng ngủ của tôi thì ấm cúng và có 1 giường.",
                de: "Mein Schlafzimmer ist gemütlich und hat ein Bett.",
                note: "das Schlafzimmer → Mein; das Bett sau hat → ein Bett."
            },
            {
                vi: "Phòng làm việc của tôi thì nhỏ nhưng sáng.",
                de: "Mein Arbeitszimmer ist klein, aber hell.",
                note: "Liên từ aber nối 2 tính từ trái nghĩa: klein, aber hell."
            },
            {
                vi: "Nó có 1 bàn và 1 ghế.",
                de: "Es hat einen Tisch und einen Stuhl.",
                note: "Cả der Tisch và der Stuhl đều là giống đực nên sau hat đổi thành einen Tisch und einen Stuhl."
            },
            {
                vi: "Phòng bếp của tôi thì nhỏ và đẹp.",
                de: "Meine Küche ist klein und schön.",
                note: "die Küche mang giống cái nên mạo từ sở hữu phải thêm -e: Meine Küche."
            },
            {
                vi: "Chúng mình cũng có một khu vườn. Mình thấy khu vườn rất đẹp.",
                de: "Wir haben auch einen Garten. Ich finde den Garten sehr schön.",
                note: "der Garten lần 1 sau haben → einen Garten; lần 2 đã xác định sau finden → den Garten."
            }
        ];

        const chosen = translationPool[Math.floor(Math.random() * translationPool.length)];
        ex.question = `[Dịch câu Miêu tả Nhà & Nội thất (Random)]: Hãy dịch câu sau sang tiếng Đức chuẩn xác: "${chosen.vi}"`;
        ex.correct_answer = chosen.de;
        ex.explanation = `Bản dịch chuẩn: '${chosen.de}'. (${chosen.note})`;
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
    else if (mode === 'speak_num' || mode === 'arrange_num') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        extra.audio_text = german;
        extra.translation = `Số ${num}`;
        ex.exercise_type = 'sap_xep';
        ex.extra_data = JSON.stringify(extra);
        ex.question = `[Sắp xếp chữ số tiếng Đức (Random)]: Hãy viết số ${num} bằng chữ tiếng Đức (chú ý quy tắc: Hàng đơn vị + und + Hàng chục):`;
        ex.correct_answer = german;
        ex.explanation = `Số ${num} trong tiếng Đức viết là: '${german}'.`;
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
            if (extra.dynamic_number || extra.dynamic_mode || extra.dynamic_price || extra.dynamic_conjugation || extra.dynamic_article_quiz || extra.dynamic_possessive_article || extra.dynamic_plural_quiz || extra.dynamic_direction_quiz || extra.dynamic_landmark_quiz || extra.dynamic_praeteritum_quiz || extra.dynamic_country_language_quiz || extra.dynamic_question_transform || extra.dynamic_nom_akk_quiz || extra.dynamic_possessiv_quiz || extra.dynamic_adjective_antonym_quiz || extra.dynamic_pronoun_replacement_quiz || extra.dynamic_house_translation_quiz) isDynamic = true;
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
