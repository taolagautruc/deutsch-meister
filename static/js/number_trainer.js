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

// =============================================================================
// RUBRIC CHẤM ĐIỂM DỊCH ĐỨC -> VIỆT BÀI 8 (CÂU 46 -> CÂU 57)
// =============================================================================

function stripVnAccentsGlobal(str) {
    const protectedStr = String(str || "")
        .replace(/ä/g, '__ae__').replace(/Ä/g, '__Ae__')
        .replace(/ö/g, '__oe__').replace(/Ö/g, '__Oe__')
        .replace(/ü/g, '__ue__').replace(/Ü/g, '__Ue__')
        .replace(/ß/g, '__ss__');
    return protectedStr
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/đ/g, "d")
        .replace(/Đ/g, "D")
        .replace(/__ae__/g, 'ä').replace(/__Ae__/g, 'Ä')
        .replace(/__oe__/g, 'ö').replace(/__Oe__/g, 'Ö')
        .replace(/__ue__/g, 'ü').replace(/__Ue__/g, 'Ü')
        .replace(/__ss__/g, 'ß');
}

function hasVietnameseDiacritics(str) {
    return /[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]/i.test(str || '');
}

function levenshteinDistance(a, b) {
    if (a === b) return 0;
    const la = a.length, lb = b.length;
    if (Math.abs(la - lb) > 1) return 999;
    let matrix = [];
    for (let i = 0; i <= la; i++) matrix[i] = [i];
    for (let j = 0; j <= lb; j++) matrix[0][j] = j;
    for (let i = 1; i <= la; i++) {
        for (let j = 1; j <= lb; j++) {
            const cost = a[i - 1] === b[j - 1] ? 0 : 1;
            matrix[i][j] = Math.min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost
            );
        }
    }
    return matrix[la][lb];
}

function isLesson8WordMatch(userWord, stdWord) {
    if (userWord === stdWord) return true;
    if (stdWord.length < 5) return false;
    return levenshteinDistance(userWord, stdWord) <= 1;
}

const L8_NUMBER_MAP = {
    '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm',
    '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín', '10': 'mười'
};

const L8_STOPWORDS_ACCENTED = ['các', 'những', 'cái', 'chiếc', 'cây', 'con', 'việc', 'vậy', 'ạ', 'nhé', 'nhỉ', 'thì', 'là', 'một'];
const L8_STOPWORDS_UNACCENTED = L8_STOPWORDS_ACCENTED.map(w => stripVnAccentsGlobal(w));

const L8_PRONOUNS_ACCENTED = ['ngài', 'quý vị', 'bạn', 'anh', 'chị', 'ông', 'bà', 'cô', 'chú', 'quý khách'];
const L8_PRONOUNS_UNACCENTED = L8_PRONOUNS_ACCENTED.map(w => stripVnAccentsGlobal(w));

function normalizeLesson8String(str, isUnaccented) {
    let s = String(str || "").normalize("NFC").toLowerCase();
    s = s.replace(/[.,!?;:"'„“”‚‘\/\\\-\(\)\[\]\{\}«»`~^]+/g, ' ');
    s = s.replace(/\b(\d+)\b/g, (match, d) => L8_NUMBER_MAP[d] || match);
    s = s.replace(/\s+/g, ' ').trim();

    if (isUnaccented) {
        s = stripVnAccentsGlobal(s);
    }

    const pronouns = isUnaccented ? L8_PRONOUNS_UNACCENTED : L8_PRONOUNS_ACCENTED;
    const sortedPronouns = [...pronouns].sort((a, b) => b.length - a.length);
    for (const p of sortedPronouns) {
        const re = new RegExp(`(^|\\s)${p}(?=\\s|$)`, 'gi');
        s = s.replace(re, ' ');
    }

    const stopwords = isUnaccented ? L8_STOPWORDS_UNACCENTED : L8_STOPWORDS_ACCENTED;
    const sortedStopwords = [...stopwords].sort((a, b) => b.length - a.length);
    for (const sw of sortedStopwords) {
        const re = new RegExp(`(^|\\s)${sw}(?=\\s|$)`, 'gi');
        s = s.replace(re, ' ');
    }

    return s.replace(/\s+/g, ' ').trim();
}

const LESSON_8_RUBRICS = {
    46: {
        concepts: [
            ["nhà ga", "ga", "trạm xe lửa"],
            ["sân bay", "phi trường", "cảng hàng không"]
        ],
        standardAnswer: "các nhà ga và các sân bay"
    },
    47: {
        concepts: [
            [
                "lâu đài cổ", "lâu đài cũ", "lâu đài xưa", "lâu đài cổ xưa", "lâu đài cổ kính",
                "cung điện cổ", "cung điện cũ", "cung điện xưa", "cung điện cổ xưa", "cung điện cổ kính",
                "dinh thự cổ", "dinh thự cũ", "dinh thự xưa", "dinh thự cổ xưa", "dinh thự cổ kính"
            ],
            [
                "trung tâm thương mại hiện đại", "trung tâm thương mại mới", "trung tâm thương mại tân tiến",
                "trung tâm mua sắm hiện đại", "trung tâm mua sắm mới", "trung tâm mua sắm tân tiến",
                "khu mua sắm hiện đại", "khu mua sắm mới", "khu mua sắm tân tiến",
                "khu thương mại hiện đại", "khu thương mại mới", "khu thương mại tân tiến"
            ]
        ],
        standardAnswer: "những lâu đài cổ và những trung tâm thương mại hiện đại"
    },
    48: {
        concepts: [
            ["đi ngang qua", "đi ngang", "đi qua", "ngang qua", "đi lướt qua"],
            ["siêu thị"],
            ["bưu điện"]
        ],
        standardAnswer: "đi ngang qua siêu thị và bưu điện"
    },
    49: {
        concepts: [
            ["đi bộ", "đi", "chạy", "bước"],
            ["xuyên qua", "băng qua", "qua", "xuyên"],
            ["cổng thành"],
            ["trung cổ", "trung đại"]
        ],
        standardAnswer: "đi bộ xuyên qua cổng thành thời trung cổ"
    },
    50: {
        concepts: [
            ["đi dạo", "dạo bước", "tản bộ", "đi bộ", "dạo"],
            ["dọc theo", "men theo", "dọc"],
            [
                "sông thơ mộng", "sông đẹp như tranh vẽ", "sông đẹp như tranh", "sông nên thơ",
                "dòng sông thơ mộng", "dòng sông đẹp như tranh vẽ", "dòng sông đẹp như tranh", "dòng sông nên thơ",
                "con sông thơ mộng", "con sông đẹp như tranh vẽ", "con sông đẹp như tranh", "con sông nên thơ"
            ]
        ],
        standardAnswer: "đi dạo dọc theo dòng sông thơ mộng"
    },
    51: {
        concepts: [
            ["thẳng"],
            ["đèn tín hiệu giao thông", "đèn giao thông", "đèn tín hiệu", "đèn xanh đèn đỏ"],
            ["thứ ba"]
        ],
        standardAnswer: "lái xe đi thẳng cho đến đèn giao thông thứ ba"
    },
    52: {
        concepts: [
            ["băng qua", "vượt qua", "đi trên", "qua", "sang"],
            ["cầu rộng"],
            ["đi vào", "vào", "tới", "đến", "sang"],
            ["khu đô thị mới", "khu phố mới", "thành phố mới", "phố mới", "khu mới", "tân thành", "neustadt"]
        ],
        negativePatterns: [
            /\b(?:ở\s+trong|o\s+trong)\b/i
        ],
        standardAnswer: "đi qua cây cầu rộng vào khu phố mới"
    },
    53: {
        concepts: [
            [
                "tham quan vòng quanh thành phố", "đi vòng quanh thành phố", "đi tham quan thành phố",
                "du lịch vòng quanh thành phố", "tham quan thành phố", "dạo quanh thành phố",
                "vòng quanh thành phố", "tour thành phố", "city tour"
            ],
            ["hai tiếng", "hai giờ"],
            [
                "xe buýt hai tầng", "xe buýt tầng đôi",
                "xe bus hai tầng", "xe bus tầng đôi"
            ]
        ],
        standardAnswer: "thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng"
    },
    54: {
        concepts: [
            ["rẽ sang trái", "rẽ về bên trái", "rẽ bên trái", "rẽ qua trái", "quẹo trái", "rẽ trái"],
            ["ngã tư", "giao lộ"],
            ["tiếp theo", "kế tiếp", "gần nhất", "sắp tới", "kế"]
        ],
        standardAnswer: "rẽ trái ở ngã tư tiếp theo"
    },
    55: {
        concepts: [
            ["mong muốn", "có ý định", "ước muốn", "muốn", "định", "dự định"],
            ["ghé thăm", "đến thăm", "đi tham quan", "tham quan", "đi thăm", "đi xem", "thăm", "xem"],
            ["tháp truyền hình", "tháp tivi", "fernsehturm"],
            ["quảng trường alexander", "quảng trường alex", "alexanderplatz", "alexander platz", "alexander"]
        ],
        standardAnswer: "muốn tham quan Tháp truyền hình ở quảng trường Alexander"
    },
    56: {
        concepts: [
            ["cho tôi hỏi", "xin lỗi", "làm phiền", "cho hỏi", "xin hỏi", "xin phép"],
            [
                "đi như thế nào", "đi đường nào", "đi lối nào", "làm thế nào",
                "hướng nào", "chỉ đường", "hỏi đường", "đi thế nào", "lối nào", "đường nào", "làm sao", "ở đâu"
            ],
            ["tòa nhà quốc hội", "toà nhà quốc hội", "nhà quốc hội", "quốc hội", "reichstag"]
        ],
        standardAnswer: "Xin lỗi quý vị, từ đây đi lối nào để tới Tòa nhà Quốc hội ạ?"
    },
    57: {
        concepts: [
            ["đối diện"],
            ["nhà ga", "ga"],
            ["nhìn thấy", "trông thấy", "thấy được", "thấy"],
            ["khách sạn lớn", "khách sạn đồ sộ", "khách sạn to"]
        ],
        standardAnswer: "Đối diện nhà ga, quý vị sẽ nhìn thấy khách sạn lớn."
    }
};

function matchLesson8Concepts(userTokens, concepts, conceptIndex, usedTokenMask) {
    if (conceptIndex >= concepts.length) {
        return true;
    }
    const currentConceptVariants = concepts[conceptIndex];
    for (const variantWords of currentConceptVariants) {
        const vLen = variantWords.length;
        for (let i = 0; i <= userTokens.length - vLen; i++) {
            let clash = false;
            for (let k = 0; k < vLen; k++) {
                if (usedTokenMask[i + k]) {
                    clash = true;
                    break;
                }
            }
            if (clash) continue;

            let matches = true;
            for (let k = 0; k < vLen; k++) {
                if (!isLesson8WordMatch(userTokens[i + k], variantWords[k])) {
                    matches = false;
                    break;
                }
            }

            if (matches) {
                for (let k = 0; k < vLen; k++) usedTokenMask[i + k] = true;
                if (matchLesson8Concepts(userTokens, concepts, conceptIndex + 1, usedTokenMask)) {
                    return true;
                }
                for (let k = 0; k < vLen; k++) usedTokenMask[i + k] = false;
            }
        }
    }
    return false;
}

function evaluateLesson8Translation(userAns, qNum) {
    const rubric = LESSON_8_RUBRICS[qNum];
    if (!rubric) return false;

    const rawUser = String(userAns || "").trim();
    if (!rawUser) return false;

    const userWordsCount = rawUser.split(/\s+/).filter(Boolean).length;
    const stdWordsCount = rubric.standardAnswer.split(/\s+/).filter(Boolean).length;
    if (userWordsCount > 2 * stdWordsCount + 4) {
        return false;
    }

    const isUnaccented = !hasVietnameseDiacritics(rawUser);

    if (rubric.negativePatterns) {
        const cleanForNeg = normalizeLesson8String(rawUser, isUnaccented);
        for (const neg of rubric.negativePatterns) {
            if (neg.test(cleanForNeg) || neg.test(rawUser.toLowerCase())) {
                return false;
            }
        }
    }

    const normUserStr = normalizeLesson8String(rawUser, isUnaccented);
    const userTokens = normUserStr.split(/\s+/).filter(Boolean);

    const normalizedConcepts = rubric.concepts.map(varList => {
        return varList.map(v => {
            const normV = normalizeLesson8String(v, isUnaccented);
            return normV.split(/\s+/).filter(Boolean);
        }).filter(words => words.length > 0);
    });

    const usedMask = new Array(userTokens.length).fill(false);
    return matchLesson8Concepts(userTokens, normalizedConcepts, 0, usedMask);
}

const L8_TARGET_NOUNS = ['stadttor', 'brandenburger', 'museumsinsel', 'einkaufszentrum', 'krankenhaus', 'marktplatz', 'reichstag', 'kreuzung', 'staatsoper', 'touristen', 'besucher'];
const L8_PREFIXES = ['der', 'die', 'das', 'den', 'dem', 'des', 'am', 'im', 'zum', 'zur', 'durch', 'ueber', 'an', 'in', 'mit', 'auf', 'vor', 'nach', 'um', 'bis', 'zu'];
const L8_KNOWN_STEMS = [
    'grossen', 'grosser', 'grosse', 'kleinen', 'alten', 'zweiten', 'ersten', 'bruecke',
    'krankenhaus', 'ampel', 'park', 'fluss', 'kreuzung', 'museumsinsel', 'kirche',
    'marktplatz', 'rathaus', 'reichstag', 'einkaufszentrum', 'bus', 'brandenburger',
    'tor', 'abend', 'staatsoper', 'hafen', 'stadttor', 'bank', 'morgen', 'vormittag',
    'nachmittag', 'fuss', 'kommen', 'gehen', 'vorbei', 'links', 'rechts'
];

function l8Levenshtein(s1, s2) {
    if (s1 === s2) return 0;
    if (!s1.length) return s2.length;
    if (!s2.length) return s1.length;
    const matrix = [];
    for (let i = 0; i <= s2.length; i++) matrix[i] = [i];
    for (let j = 0; j <= s1.length; j++) matrix[0][j] = j;
    for (let i = 1; i <= s2.length; i++) {
        for (let j = 1; j <= s1.length; j++) {
            if (s2.charAt(i - 1) === s1.charAt(j - 1)) {
                matrix[i][j] = matrix[i - 1][j - 1];
            } else {
                matrix[i][j] = Math.min(
                    matrix[i - 1][j - 1] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j] + 1
                );
            }
        }
    }
    return matrix[s2.length][s1.length];
}

function normalizeLesson8VD(text) {
    if (!text) return '';
    let s = String(text).toLowerCase();
    s = s.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss');
    s = s.replace(/[\.,!?;:\"\'„“”»«\(\)\-\–]/g, ' ');
    s = s.replace(/\s+/g, ' ').trim();

    const rawTokens = s.split(' ').filter(Boolean);
    const expandedTokens = [];
    for (const tok of rawTokens) {
        let decoupled = false;
        for (const p of L8_PREFIXES) {
            if (tok.startsWith(p) && tok.length > p.length) {
                const rest = tok.slice(p.length);
                if (L8_KNOWN_STEMS.includes(rest) || L8_PREFIXES.includes(rest) || L8_TARGET_NOUNS.includes(rest)) {
                    expandedTokens.push(p);
                    let decoupledSecond = false;
                    for (const p2 of L8_PREFIXES) {
                        if (rest.startsWith(p2) && rest.length > p2.length) {
                            const rest2 = rest.slice(p2.length);
                            if (L8_KNOWN_STEMS.includes(rest2) || L8_TARGET_NOUNS.includes(rest2)) {
                                expandedTokens.push(p2);
                                expandedTokens.push(rest2);
                                decoupledSecond = true;
                                break;
                            }
                        }
                    }
                    if (!decoupledSecond) {
                        expandedTokens.push(rest);
                    }
                    decoupled = true;
                    break;
                }
            }
        }
        if (!decoupled) {
            if (tok === 'vorbeigehen') {
                expandedTokens.push('vorbei', 'gehen');
            } else if (tok === 'linksab') {
                expandedTokens.push('links', 'ab');
            } else if (tok === 'rechtsab') {
                expandedTokens.push('rechts', 'ab');
            } else {
                expandedTokens.push(tok);
            }
        }
    }

    // 1-typo tolerance for nouns >= 6 chars
    const finalTokens = [];
    for (const tok of expandedTokens) {
        let mapped = tok;
        if (tok.length >= 6) {
            for (const tn of L8_TARGET_NOUNS) {
                if (l8Levenshtein(tok, tn) <= 1) {
                    mapped = tn;
                    break;
                }
            }
        }
        finalTokens.push(mapped);
    }

    return finalTokens.join(' ');
}

function evaluateLesson8VDTranslation(userAns, qNum) {
    const norm = normalizeLesson8VD(userAns);
    if (!norm) return { isCorrect: false, hint: '' };

    if (qNum === 87) {
        const p87 = /^(?:zuerst\s+)?gehen\s+sie(?:\s+(?:zuerst|zunaechst|als\s+erstes))?\s+(?:geradeaus\s+ueber\s+die\s+bruecke|ueber\s+die\s+bruecke\s+geradeaus)\s+(?:(?:und\s+)?(?:dann|danach|anschliessend)\s+(?:gehen\s+sie\s+)?)?(?:am|an\s+dem)\s+krankenhaus\s+vorbei\s+bis\s+(?:zur|zu\s+der)\s+zweiten\s+ampel$/;
        if (p87.test(norm)) return { isCorrect: true, hint: '' };

        if (/bis\s+zum\b/.test(norm)) {
            return { isCorrect: false, hint: "Chú ý mạo từ: 'die Ampel' là giống cái, sau 'bis zu' (+ Dativ) phải dùng 'bis zur zweiten Ampel' (hoặc 'bis zu der zweiten Ampel'), không dùng 'bis zum'." };
        }
        if (/ueber\s+(?:dem|der|den)\b/.test(norm)) {
            return { isCorrect: false, hint: "Chuyển động qua cầu dùng Akkusativ giống cái: 'über die Brücke'." };
        }
        if (/\b(?:geh|geht)\b/.test(norm) && !/gehen\s+sie/.test(norm)) {
            return { isCorrect: false, hint: "Đề bài yêu cầu dùng ngôi trang trọng 'Sie': 'Gehen Sie ...'." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Gehen Sie (zuerst) geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!'" };
    }

    if (qNum === 88) {
        const p88 = /^(?:geh|gehe|lauf|laufe)\s+durch\s+den\s+park(?:\s+und)?(?:\s+(?:geh|gehe|lauf|laufe))?\s+(?:den\s+fluss\s+entlang|am\s+fluss\s+entlang)\s+und\s+(?:bieg|biege)\s+(?:an\s+der\s+ersten\s+kreuzung\s+links|links\s+an\s+der\s+ersten\s+kreuzung)\s+ab$/;
        if (p88.test(norm)) return { isCorrect: true, hint: '' };

        if (/gehen\s+sie/.test(norm) || /\bsie\b/.test(norm)) {
            return { isCorrect: false, hint: "Đề bài yêu cầu dùng ngôi thân mật 'du' (Geh... / Lauf... và bieg ... ab), không dùng 'Gehen Sie'." };
        }
        if (/durch\s+(?:dem|der|das)\b/.test(norm)) {
            return { isCorrect: false, hint: "Giới từ 'durch' luôn đi với Akkusativ: 'durch den Park' (der Park -> den Park)." };
        }
        if (!/\bab$/.test(norm)) {
            return { isCorrect: false, hint: "'abbiegen' là động từ tách: bắt buộc phải có tiền tố 'ab' ở cuối mệnh đề ('bieg ... ab' hoặc 'biege ... ab')." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!'" };
    }

    if (qNum === 89) {
        const p89 = /^(?:entschuldigung|entschuldigen\s+sie|verzeihung)\s+wir\s+suchen\s+die\s+museumsinsel\s+wie\s+(?:kommen|gehen)\s+wir(?:\s+zu\s+fuss)?\s+(?:zur|zu\s+der|auf\s+die)\s+museumsinsel(?:\s+zu\s+fuss)?$/;
        if (p89.test(norm)) return { isCorrect: true, hint: '' };

        if (/wir\s+suchen\s+(?:der|den|dem)\s+museumsinsel/.test(norm)) {
            return { isCorrect: false, hint: "'die Museumsinsel' mang giống cái, sau động từ 'suchen' ở Akkusativ vẫn là 'die Museumsinsel'." };
        }
        if (/\bzum\s+museumsinsel/.test(norm)) {
            return { isCorrect: false, hint: "'die Museumsinsel' mang giống cái, sau 'zu' (+ Dativ) phải dùng 'zur Museumsinsel' (zu + der), không dùng 'zum'." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Entschuldigung / Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir (zu Fuß) zur Museumsinsel?'" };
    }

    if (qNum === 90) {
        const p90 = /^(?:geht|lauft)\s+an\s+der\s+alten\s+kirche\s+vorbei\s+und\s+(?:(?:geht|lauft)\s+)?ueber\s+den\s+marktplatz\s+(?:rechts\s+seht\s+ihr\s+das\s+rathaus|ihr\s+seht\s+rechts\s+das\s+rathaus|auf\s+der\s+rechten\s+seite\s+seht\s+ihr\s+das\s+rathaus|rechts\s+ist\s+das\s+rathaus)$/;
        if (p90.test(norm)) return { isCorrect: true, hint: '' };

        if (/ueber\s+dem\s+marktplatz/.test(norm)) {
            return { isCorrect: false, hint: "Chuyển động băng qua quảng trường dùng Akkusativ: 'über den Marktplatz' (không dùng Dativ 'über dem')." };
        }
        if (/an\s+die\s+alte/.test(norm)) {
            return { isCorrect: false, hint: "Giới từ 'an ... vorbei' đi với Dativ: 'an der alten Kirche vorbei'." };
        }
        if (/an\s+der\s+alte\s+kirche/.test(norm)) {
            return { isCorrect: false, hint: "Đuôi tính từ sau mạo từ xác định ở Dativ là '-en': dùng 'an der alten Kirche', không dùng 'alte'." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.'" };
    }

    if (qNum === 91) {
        const p_c1 = '(?:(?:(?:am\\s+morgen|am\\s+vormittag)\\s+(?:will|moechte)\\s+mein\\s+onkel|mein\\s+onkel\\s+(?:will|moechte)\\s+(?:am\\s+morgen|am\\s+vormittag))\\s+den\\s+reichstag\\s+besichtigen)';
        const p_c2 = '(?:(?:(?:am\\s+nachmittag)\\s+(?:wollen|moechten)\\s+wir|wir\\s+(?:wollen|moechten)\\s+am\\s+nachmittag)\\s+im\\s+einkaufszentrum\\s+bummeln)';
        const p91 = new RegExp('^' + p_c1 + '\\s+und\\s+' + p_c2 + '$');
        if (p91.test(norm)) return { isCorrect: true, hint: '' };

        if (/in\s+der\s+morgen|im\s+morgen/.test(norm)) {
            return { isCorrect: false, hint: "Cụm chỉ buổi sáng chưa đúng: dùng 'am Morgen' hoặc 'am Vormittag'." };
        }
        if (/(?:am\s+vormittag|am\s+morgen)\s+mein\s+onkel\s+(?:will|moechte)/.test(norm)) {
            return { isCorrect: false, hint: "Khi 'Am Vormittag' đứng đầu câu, động từ chia ('will') đứng ngay sau nó, rồi mới đến chủ ngữ: 'Am Vormittag will mein Onkel …'. 'Am Morgen' cũng đúng; 'in der Morgen' là sai. 'möchte / möchten' cũng được chấp nhận." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln.'" };
    }

    if (qNum === 92) {
        const p92 = /^(?:zuerst\s+fahren\s+die\s+(?:touristen|besucher)|die\s+(?:touristen|besucher)\s+fahren\s+zuerst)\s+mit\s+dem\s+bus\s+(?:zum|zu\s+dem|bis\s+zum)\s+brandenburger\s+tor\s+und\s+(?:am\s+abend\s+gehen\s+sie|gehen\s+(?:sie\s+)?am\s+abend|abends\s+gehen\s+sie|sie\s+gehen\s+(?:am\s+abend|abends))\s+in\s+die\s+staatsoper$/;
        if (p92.test(norm)) return { isCorrect: true, hint: '' };

        if (/in\s+der\s+staatsoper/.test(norm)) {
            return { isCorrect: false, hint: "Đi vào nhà hát (chuyển động Wohin? + Akkusativ): dùng 'in die Staatsoper', không dùng Dativ 'in der'." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper.'" };
    }

    if (qNum === 93) {
        const p93_a = /^(?:um\s+(?:zum|zu\s+dem)\s+hafen\s+zu\s+kommen|um\s+den\s+hafen\s+zu\s+erreichen)\s+(?:musst\s+du|muessen\s+sie)\s+durch\s+das\s+stadttor(?:\s+gehen)?\s+und\s+an\s+der\s+grossen\s+bank\s+(?:vorbei\s+gehen|vorbeigehen)$/;
        const p93_b = /^(?:du\s+musst|sie\s+muessen)\s+durch\s+das\s+stadttor(?:\s+gehen)?\s+und\s+an\s+der\s+grossen\s+bank\s+(?:vorbei\s+gehen|vorbeigehen)\s+um\s+(?:zum|zu\s+dem)\s+hafen\s+zu\s+kommen$/;
        if (p93_a.test(norm) || p93_b.test(norm)) return { isCorrect: true, hint: '' };

        if (/an\s+die\s+grossen\s+bank/.test(norm) || /an\s+die\s+grosse\s+bank/.test(norm)) {
            return { isCorrect: false, hint: "Giới từ chỉ vị trí ngang qua: 'an der großen Bank vorbei' (an + Dativ giống cái: 'der', tính từ mang đuôi '-en')." };
        }
        if (/an\s+der\s+grosse\s+bank/.test(norm)) {
            return { isCorrect: false, hint: "Đuôi tính từ sau mạo từ xác định ở Dativ là '-en': dùng 'an der großen Bank', không dùng 'große'." };
        }
        return { isCorrect: false, hint: "Cần dịch đúng: 'Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen.' ('du' và 'Sie' đều được chấp nhận)." };
    }

    return { isCorrect: false, hint: '' };
}

function checkGermanAnswerEquivalence(userAns, correctAns, options = {}) {
    if (!userAns || !correctAns) return false;

    // Kiểm tra nhanh theo Rubric Bài 8 (Câu 46 -> 57 dạng Dịch Đức -> Việt, Câu 87 -> 93 dạng Dịch Việt -> Đức)
    if (options && options.question) {
        const isL8 = (options.lesson_id === 22) ||
                     (options.lesson_title && /bài 8\b/i.test(options.lesson_title)) ||
                     (options.isLesson8 === true) ||
                     (typeof currentLesson !== 'undefined' && currentLesson && (
                         currentLesson.id === 22 ||
                         (currentLesson.title && /bài 8\b/i.test(currentLesson.title))
                     ));
        if (isL8) {
            const l8Match = String(options.question).match(/Câu\s+(4[6-9]|5[0-7])\b/i);
            if (l8Match) {
                const qNum = parseInt(l8Match[1], 10);
                return evaluateLesson8Translation(userAns, qNum);
            }
            const l8VDMatch = String(options.question).match(/Câu\s+(8[7-9]|9[0-3])\b/i);
            if (l8VDMatch) {
                const qNum = parseInt(l8VDMatch[1], 10);
                const res = evaluateLesson8VDTranslation(userAns, qNum);
                return res.isCorrect;
            }
        }
    }

    const isMultiSlot = (typeof options === 'boolean' ? options : Boolean(options && options.isMultiSlot));

    // 0. Nếu cả userAns và correctAns đều chứa dấu / (dạng điền nhiều chỗ trống: den / dem, seinen / seinen)
    if (userAns.includes('/') && correctAns.includes('/')) {
        const uParts = userAns.split('/').map(p => p.trim());
        const cParts = correctAns.split('/').map(p => p.trim());
        if (uParts.length === cParts.length && uParts.length > 1) {
            if (uParts.every((u, idx) => checkGermanAnswerEquivalence(u, cParts[idx]))) {
                return true;
            }
            return false;
        }
    }

    // 0b. Dạng điền nhiều chỗ trống (CHỈ kích hoạt khi isMultiSlot rõ ràng hoặc câu hỏi có dạng [1] ... [2] hoặc ghi chú ngăn cách):
    // Tuyệt đối không tự suy đoán chỉ vì correctAns chứa dấu / vì dấu / thường là dấu phân cách các phương án tương đương (ví dụ die Stühle / Stühle, câu dịch / câu dịch...)
    const isMultiSlotPattern = isMultiSlot || 
        (Boolean(options && options.question) && (
            options.question.includes('[1]') || 
            options.question.includes('ngăn cách bởi dấu /') ||
            options.question.includes('cách nhau bởi dấu /') ||
            options.question.includes('ngăn cách bởi dấu phẩy') ||
            options.question.includes('cách nhau bởi dấu phẩy') ||
            /điền\s+[2-9]\s+từ/i.test(options.question)
        ));

    if (isMultiSlotPattern) {
        let cParts = [];
        if (correctAns.includes('/')) {
            cParts = correctAns.split('/').map(p => p.trim()).filter(Boolean);
        } else if (correctAns.includes(',') || correctAns.includes(';')) {
            cParts = correctAns.split(/[,;]/).map(p => p.trim()).filter(Boolean);
        } else {
            cParts = correctAns.trim().split(/\s+/).map(p => p.trim()).filter(Boolean);
        }

        if (cParts.length > 1) {
            let uParts = [];
            if (userAns.includes('/')) {
                uParts = userAns.split('/').map(p => p.trim()).filter(Boolean);
            } else if (userAns.includes(',') || userAns.includes(';')) {
                uParts = userAns.split(/[,;]/).map(p => p.trim()).filter(Boolean);
            } else {
                uParts = userAns.trim().split(/\s+/).map(p => p.trim()).filter(Boolean);
            }

            if (uParts.length === cParts.length) {
                return uParts.every((u, idx) => checkGermanAnswerEquivalence(u, cParts[idx], { isMultiSlot: false }));
            }
            // Người dùng thiếu slot (ví dụ chỉ điền 1 từ [1]): KHÔNG chấp nhận!
            return false;
        }
    }

    // 1. Phân tách nếu có nhiều phương án đáp án chuẩn (cách nhau bởi /, ||, \n, hoặc)
    // LƯU Ý: Với dạng điền nhiều chỗ trống (isMultiSlotPattern), tuyệt đối không phân tách dấu / thành các phương án độc lập
    if (!isMultiSlotPattern && (correctAns.includes('/') || correctAns.includes('||') || correctAns.includes('\n') || /\s+hoặc\s+/i.test(correctAns))) {
        const alts = correctAns.split(/\/|\|\||\n|\s+hoặc\s+/i).map(a => a.trim()).filter(Boolean);
        if (alts.some(alt => checkGermanAnswerEquivalence(userAns, alt, { isMultiSlot: false }))) {
            return true;
        }
    }

    // 2. Chuẩn hóa cơ bản: chữ thường, bỏ toàn bộ dấu câu
    const baseClean = (s) => String(s)
        .trim()
        .toLowerCase()
        .normalize("NFC")
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
        // Bảo vệ các ký tự Umlaut & Eszett tiếng Đức không bị tách dấu bởi NFD Unicode
        const protectedStr = String(str || "")
            .replace(/ä/g, '__ae__').replace(/Ä/g, '__Ae__')
            .replace(/ö/g, '__oe__').replace(/Ö/g, '__Oe__')
            .replace(/ü/g, '__ue__').replace(/Ü/g, '__Ue__')
            .replace(/ß/g, '__ss__');
        return protectedStr
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "")
            .replace(/đ/g, "d")
            .replace(/Đ/g, "D")
            .replace(/__ae__/g, 'ä').replace(/__Ae__/g, 'Ä')
            .replace(/__oe__/g, 'ö').replace(/__Oe__/g, 'Ö')
            .replace(/__ue__/g, 'ü').replace(/__Ue__/g, 'Ü')
            .replace(/__ss__/g, 'ß');
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

    // 14. Dịch sang tiếng Việt - Linh hoạt ngữ nghĩa, cấu trúc câu, ngày tháng, vị trí & từ đồng nghĩa:
    const replaceVnPhrases = (text, phraseList, replacement) => {
        let res = " " + text + " ";
        const sorted = [...phraseList].sort((a,b) => b.length - a.length);
        for (const p of sorted) {
            const escaped = p.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
            const re = new RegExp(`(^|\\s)${escaped}(?=\\s|$)`, "gi");
            res = res.replace(re, ` ${replacement}`);
        }
        return res.trim().replace(/\s+/g, " ");
    };

    const normalizeVietnameseAnswer = (s) => {
        let str = baseClean(s);

        // Chuẩn hóa ngày tháng & số thứ tự tiếng Việt
        str = replaceVnPhrases(str, ['tháng mười hai', 'tháng 12'], 'tháng 12');
        str = replaceVnPhrases(str, ['tháng mười một', 'tháng 11'], 'tháng 11');
        str = replaceVnPhrases(str, ['tháng mười', 'tháng 10'], 'tháng 10');
        str = replaceVnPhrases(str, ['tháng chín', 'tháng 9'], 'tháng 9');
        str = replaceVnPhrases(str, ['tháng tám', 'tháng 8'], 'tháng 8');
        str = replaceVnPhrases(str, ['tháng bảy', 'tháng bẩy', 'tháng 7'], 'tháng 7');
        str = replaceVnPhrases(str, ['tháng sáu', 'tháng 6'], 'tháng 6');
        str = replaceVnPhrases(str, ['tháng năm', 'tháng 5'], 'tháng 5');
        str = replaceVnPhrases(str, ['tháng tư', 'tháng bốn', 'tháng 4'], 'tháng 4');
        str = replaceVnPhrases(str, ['tháng ba', 'tháng 3'], 'tháng 3');
        str = replaceVnPhrases(str, ['tháng hai', 'tháng 2'], 'tháng 2');
        str = replaceVnPhrases(str, ['tháng một', 'tháng giêng', 'tháng 1'], 'tháng 1');

        // Chuẩn hóa số tầng
        str = replaceVnPhrases(str, ['tầng bảy', 'tầng bẩy', 'tầng 7'], 'tầng 7');
        str = replaceVnPhrases(str, ['tầng ba', 'tầng 3'], 'tầng 3');
        str = replaceVnPhrases(str, ['tầng hai', 'tầng 2'], 'tầng 2');
        str = replaceVnPhrases(str, ['tầng một', 'tầng 1'], 'tầng 1');

        // Chuẩn hóa năm 2002
        str = str.replace(/năm\s+hai\s+(nghìn|ngàn)\s+(không\s+trăm\s+)?(lẻ|linh)?\s*hai/gi, 'năm 2002');

        // Định dạng ngày tháng
        str = str.replace(/vào\s+ngày\s+mùng\s+(\d+)/gi, 'ngày $1');
        str = str.replace(/vào\s+ngày\s+(\d+)/gi, 'ngày $1');
        str = str.replace(/ngày\s+mùng\s+(\d+)/gi, 'ngày $1');
        str = str.replace(/(\d{1,2})\s*\/\s*(\d{1,2})(?:\s*\/\s*(\d{4}))?/g, (m, d, mo, y) => {
            return y ? `${d} tháng ${mo} năm ${y}` : `${d} tháng ${mo}`;
        });
        str = str.replace(/từ\s+ngày\s+(mùng\s+)?(\d+)\s+đến\s+(ngày\s+)?(\d+)/gi, 'từ $2 đến $4');
        str = str.replace(/từ\s+(\d+)\s+đến\s+(\d+)/gi, 'từ $1 đến $2');
        str = str.replace(/ngày\s+(\d+)/gi, '$1');
        str = str.replace(/mùng\s+(\d+)/gi, '$1');

        // Giới từ vị trí
        str = replaceVnPhrases(str, ['nằm ở', 'tọa lạc ở', 'tọa lạc tại', 'ở tại', 'ở trong', 'được đặt ở', 'được đặt tại'], 'ở');
        str = replaceVnPhrases(str, ['ở tại', 'tại'], 'ở');
        str = replaceVnPhrases(str, ['ở phía sau', 'phía sau', 'ở đằng sau', 'đằng sau', 'ở sau'], 'sau');
        str = replaceVnPhrases(str, ['ở phía trước', 'phía trước', 'ở đằng trước', 'đằng trước', 'ở trước'], 'trước');
        str = replaceVnPhrases(str, ['ở phía trên', 'phía trên', 'ở trên'], 'trên');
        str = replaceVnPhrases(str, ['ở phía dưới', 'phía dưới', 'ở dưới', 'dưới gầm', 'ở dưới gầm'], 'dưới');
        str = replaceVnPhrases(str, ['ngay ở giữa', 'ngay giữa', 'ở ngay giữa', 'nằm ngay giữa', 'ở giữa'], 'giữa');
        str = replaceVnPhrases(str, ['ở ngay cạnh'], 'ngay cạnh');

        // Từ vựng & cụm từ đồng nghĩa
        str = replaceVnPhrases(str, ['căn tin', 'căng tin', 'canteen', 'quán ăn'], 'nhà ăn');
        str = replaceVnPhrases(str, ['phòng hội nghị', 'phòng họp hội nghị'], 'phòng họp');
        str = replaceVnPhrases(str, ['con gái của tôi', 'đứa con gái của tôi', 'đứa con gái tôi'], 'con gái tôi');
        str = replaceVnPhrases(str, ['ông bà của chúng tôi', 'ông bà chúng tôi', 'ông bà của tôi', 'ông bà của chúng mình', 'ông bà chúng mình'], 'ông bà tôi');
        str = replaceVnPhrases(str, ['bố mẹ của tôi', 'ba mẹ tôi', 'ba mẹ của tôi', 'cha mẹ tôi', 'cha mẹ của tôi'], 'bố mẹ tôi');
        str = replaceVnPhrases(str, ['sinh vào ngày', 'sinh ngày', 'được sinh ra vào ngày', 'được sinh vào ngày', 'được sinh ngày', 'chào đời ngày', 'chào đời vào ngày', 'được sinh ra ngày', 'sinh ra', 'được sinh ra', 'được sinh', 'chào đời'], 'sinh');
        str = replaceVnPhrases(str, ['sau giờ làm việc', 'sau khi tan làm', 'sau khi làm việc', 'sau ca làm', 'sau khi tan sở', 'sau tan làm', 'sau tan sở'], 'sau giờ làm');
        str = replaceVnPhrases(str, ['không đi về nhà ngay', 'không về nhà liền', 'không đi về nhà liền', 'không về nhà lập tức', 'không lập tức về nhà'], 'không về nhà ngay');
        str = replaceVnPhrases(str, ['gặp gỡ', 'hẹn gặp'], 'gặp');
        str = replaceVnPhrases(str, ['những người bạn của tôi', 'bạn bè của mình', 'những người bạn tôi', 'bạn bè của tôi', 'bạn bè tôi', 'bạn của tôi'], 'bạn tôi');
        str = replaceVnPhrases(str, ['phòng khám bác sĩ của chúng tôi', 'phòng khám của chúng tôi', 'phòng mạch của chúng tôi', 'phòng khám bác sĩ chúng tôi', 'phòng mạch chúng tôi', 'phòng khám chúng tôi'], 'phòng khám');
        str = replaceVnPhrases(str, ['nghỉ đóng cửa', 'nghỉ làm việc', 'tạm đóng cửa', 'ngừng mở cửa', 'sẽ đóng cửa'], 'đóng cửa');
        str = replaceVnPhrases(str, ['ở trong công viên', 'trong công viên'], 'ở công viên');
        str = replaceVnPhrases(str, ['còn'], 'và');
        str = replaceVnPhrases(str, ['bức ảnh', 'tấm ảnh', 'tấm hình', 'bức hình'], 'bức ảnh');
        str = replaceVnPhrases(str, ['gia đình to'], 'gia đình lớn');
        str = replaceVnPhrases(str, ['được treo trên tường', 'treo ở trên tường', 'treo trên bức tường', 'được treo trên bức tường'], 'treo trên tường');
        str = replaceVnPhrases(str, ['ghế sô pha', 'sô pha', 'sofa'], 'ghế sofa');
        str = replaceVnPhrases(str, ['chiếc ghế', 'cái ghế'], 'ghế');
        str = replaceVnPhrases(str, ['chiếc bàn làm việc', 'cái bàn làm việc', 'bàn viết'], 'bàn làm việc');
        str = replaceVnPhrases(str, ['chiếc bàn', 'cái bàn'], 'bàn');
        str = replaceVnPhrases(str, ['con chuột máy tính', 'chuột máy tính', 'con chuột'], 'chuột');
        str = replaceVnPhrases(str, ['tàu điện mặt đất', 'tàu điện trên mặt đất', 'xe điện mặt đất', 'xe điện', 'tàu điện'], 'tàu điện');
        str = replaceVnPhrases(str, ['tàu điện đô thị', 'tàu s-bahn', 'tàu nhanh s-bahn', 'tàu s bahn', 's-bahn', 's bahn'], 'tàu điện nhanh');
        str = replaceVnPhrases(str, ['tiệm cà phê', 'quán cafe', 'tiệm cafe'], 'quán cà phê');
        str = replaceVnPhrases(str, ['tiệm sách', 'nhà sách'], 'hiệu sách');
        str = replaceVnPhrases(str, ['rạp phim'], 'rạp chiếu phim');
        str = replaceVnPhrases(str, ['ở quầy lễ tân', 'tại quầy lễ tân', 'ở lễ tân', 'tại lễ tân', 'ở bàn lễ tân', 'tại bàn tiếp tân'], 'ở quầy lễ tân');
        str = replaceVnPhrases(str, ['ở chỗ bố mẹ tôi', 'ở nhà bố mẹ tôi', 'ở với bố mẹ tôi', 'với bố mẹ tôi', 'ở cùng bố mẹ tôi', 'tại nhà bố mẹ tôi'], 'ở nhà bố mẹ tôi');
        str = replaceVnPhrases(str, ['đến chợ', 'đi chợ bằng', 'ra chợ bằng'], 'ra chợ');
        str = replaceVnPhrases(str, ['đi bằng', 'đi'], 'đi');
        str = replaceVnPhrases(str, ['vào cuối tuần'], 'cuối tuần');

        // Chuẩn hóa linh hoạt Dịch Đức -> Việt (Bài 7 & toàn hệ thống):
        // 1. Thời gian & buổi
        str = replaceVnPhrases(str, ['16 giờ 30 phút', '16 giờ 30', '16h30 phút', '16h30', '4 giờ rưỡi chiều'], '16 giờ 30');
        str = replaceVnPhrases(str, ['vào lúc 16 giờ 30', 'vào 16 giờ 30', 'lúc 16 giờ 30'], 'lúc 16 giờ 30');
        str = replaceVnPhrases(str, ['vào buổi sáng', 'buổi sáng'], 'buổi sáng');
        str = replaceVnPhrases(str, ['vào buổi chiều', 'buổi chiều'], 'buổi chiều');
        str = replaceVnPhrases(str, ['ngủ đến 7 giờ', 'ngủ tới 7 giờ', 'ngủ đến 7h', 'ngủ tới 7h'], 'ngủ đến 7 giờ');
        str = replaceVnPhrases(str, ['từ 20 đến 22 giờ', 'từ 20h đến 22h', 'từ 20 giờ đến 22 giờ', 'từ 8 giờ đến 10 giờ tối', 'từ 8h đến 10h tối'], 'từ 20 đến 22 giờ');

        // 2. Nghề nghiệp & hoạt động
        str = replaceVnPhrases(str, ['làm nghề giáo viên', 'làm giáo viên', 'là một giáo viên', 'nghề của frank müller là giáo viên', 'nghề của frank muller là giáo viên', 'là giáo viên'], 'là giáo viên');
        str = replaceVnPhrases(str, ['có kỳ nghỉ', 'có kì nghỉ', 'được nghỉ lễ', 'được nghỉ phép', 'được nghỉ', 'có ngày nghỉ'], 'có kỳ nghỉ');
        str = replaceVnPhrases(str, ['cho nên có thể', 'nên có thể', 'và có thể'], 'và có thể');
        str = replaceVnPhrases(str, ['cô giáo', 'nữ giáo viên'], 'cô giáo');
        str = replaceVnPhrases(str, ['giảng dạy học sinh', 'dạy học sinh', 'giảng dạy', 'dạy học', 'dạy'], 'dạy');
        str = replaceVnPhrases(str, ['người thợ cắt tóc', 'người thợ làm tóc', 'thợ làm tóc', 'thợ cắt tóc'], 'thợ cắt tóc');
        str = replaceVnPhrases(str, ['đang cắt tóc cho', 'cắt tóc cho'], 'cắt tóc cho');

        // 3. Gia đình & nhân xưng
        str = replaceVnPhrases(str, ['con gái của mình', 'con gái của cô ấy', 'con gái mình', 'con gái cô ấy', 'con gái'], 'con gái');
        str = replaceVnPhrases(str, ['anh trai của tôi', 'em trai của tôi', 'anh trai tôi', 'em trai tôi', 'anh tôi', 'em tôi'], 'anh trai tôi');

        // 4. Địa điểm
        str = replaceVnPhrases(str, ['từ trường mẫu giáo về', 'từ trường mầm non về', 'từ nhà trẻ về', 'từ trường mẫu giáo', 'từ trường mầm non', 'từ nhà trẻ', 'ở trường mẫu giáo', 'tại trường mẫu giáo', 'ở trường mầm non', 'tại trường mầm non', 'ở nhà trẻ', 'tại nhà trẻ', 'trường mầm non', 'nhà trẻ', 'trường mẫu giáo'], 'trường mẫu giáo');
        str = replaceVnPhrases(str, ['tại một trường học', 'ở một trường học', 'tại trường học', 'ở trường học', 'ở một ngôi trường', 'tại một ngôi trường', 'ở trường', 'tại trường', 'trường học'], 'trường');
        str = replaceVnPhrases(str, ['ở trường đại học', 'tại trường đại học', 'ở một trường đại học', 'tại một trường đại học', 'ở đại học', 'tại đại học', 'trường đại học'], 'đại học');
        str = replaceVnPhrases(str, ['ở trong phòng khách', 'trong phòng khách', 'ở phòng khách', 'phòng khách'], 'phòng khách');
        str = replaceVnPhrases(str, ['ở trong tiệm làm tóc', 'trong tiệm làm tóc', 'ở tiệm làm tóc', 'tại tiệm làm tóc', 'ở trong tiệm cắt tóc', 'trong tiệm cắt tóc', 'ở tiệm cắt tóc', 'tại tiệm cắt tóc', 'ở trong quán cắt tóc', 'trong quán cắt tóc', 'ở quán cắt tóc', 'ở trong hiệu cắt tóc', 'trong hiệu cắt tóc', 'ở hiệu cắt tóc', 'ở trong salon tóc', 'trong salon tóc', 'ở salon tóc', 'tại salon tóc', 'tiệm cắt tóc', 'tiệm làm tóc', 'salon tóc'], 'tiệm cắt tóc');
        str = replaceVnPhrases(str, ['vào xưởng sửa chữa', 'đến xưởng sửa chữa', 'tới xưởng sửa chữa', 'vào xưởng sửa xe', 'đến xưởng sửa xe', 'tới xưởng sửa xe', 'vào gara', 'đến gara', 'tới gara', 'gara ô tô', 'xưởng sửa chữa', 'xưởng sửa xe', 'tiệm sửa xe', 'gara'], 'xưởng sửa chữa');

        // 5. Xe cộ & đi lại
        str = replaceVnPhrases(str, ['chiếc xe hơi của mình', 'xe hơi của mình', 'chiếc ô tô của mình', 'ô tô của mình', 'chiếc xe của mình', 'xe của mình', 'chiếc xe hơi', 'xe hơi', 'chiếc ô tô', 'ô tô', 'chiếc xe', 'xe'], 'ô tô');
        str = replaceVnPhrases(str, ['đi đến buổi tập bóng đá', 'đi tới buổi tập bóng đá', 'đi đến buổi tập đá bóng', 'đi tới buổi tập đá bóng', 'đi tập bóng đá', 'đi tập đá bóng', 'buổi tập đá bóng', 'buổi tập bóng đá', 'tập đá bóng', 'tập bóng đá'], 'tập bóng đá');
        str = replaceVnPhrases(str, ['rồi sau đó', 'và sau đó', 'sau đó rồi', 'sau đó'], 'sau đó');
        str = replaceVnPhrases(str, ['đem', 'đưa', 'mang'], 'mang');

        // 6. Điện thoại & khách hàng
        str = replaceVnPhrases(str, ['chiếc điện thoại đó', 'chiếc điện thoại này', 'cái điện thoại đó', 'cái điện thoại này', 'chiếc điện thoại', 'cái điện thoại', 'điện thoại'], 'điện thoại');
        str = replaceVnPhrases(str, ['rất quan trọng đối với cô ấy', 'rất quan trọng với cô ấy', 'rất quan trọng cho cô ấy', 'quan trọng đối với cô ấy', 'quan trọng với cô ấy'], 'rất quan trọng với cô ấy');
        str = replaceVnPhrases(str, ['đối với cô ấy', 'với cô ấy'], 'với cô ấy');
        str = replaceVnPhrases(str, ['bởi vì', 'vì thế vì', 'vì'], 'vì');
        str = replaceVnPhrases(str, ['gọi điện thoại cho', 'gọi điện cho', 'gọi cho'], 'gọi điện cho');
        str = replaceVnPhrases(str, ['thường xuyên phải gọi điện', 'phải thường xuyên gọi điện', 'thường phải gọi điện', 'thường xuyên gọi điện', 'thường gọi điện', 'phải gọi điện thường xuyên'], 'thường xuyên phải gọi điện');
        str = replaceVnPhrases(str, ['các khách hàng của mình', 'khách hàng của mình', 'các khách hàng của cô ấy', 'khách hàng của cô ấy', 'những khách hàng của mình', 'các khách hàng', 'những khách hàng', 'khách hàng'], 'khách hàng');

        // 7. Giải trí & bữa tối
        str = replaceVnPhrases(str, ['xem truyền hình', 'xem tv', 'xem tivi', 'xem ti vi'], 'xem tivi');
        str = replaceVnPhrases(str, ['sau khi cô ấy đã làm', 'sau khi cô ấy làm', 'sau khi cô ấy đã nấu', 'sau khi cô ấy nấu', 'sau khi đã làm', 'sau khi làm', 'sau khi đã nấu', 'sau khi nấu', 'sau khi làm xong', 'sau khi nấu xong', 'sau đó cô ấy đã làm', 'sau đó cô ấy làm'], 'sau khi làm');
        str = replaceVnPhrases(str, ['bữa tối', 'bữa ăn tối', 'cơm tối'], 'bữa tối');

        return str.trim().replace(/\s+/g, ' ');
    };

    const uVn = normalizeVietnameseAnswer(userAns);
    const cVn = normalizeVietnameseAnswer(correctAns);
    if (uVn === cVn) return true;

    // Không phân biệt có dấu / không dấu tiếng Việt
    const uVnNoAcc = stripVnAccents(uVn);
    const cVnNoAcc = stripVnAccents(cVn);
    if (uVnNoAcc === cVnNoAcc) return true;

    // Bỏ từ phụ "ở", "bằng", "với", "đi" ở đầu câu dịch cụm từ ngắn
    const stripLeadingPrep = (s) => s.replace(/^(ở|tại|trong|bằng|với|đi)\s+/i, '');
    if (stripLeadingPrep(uVn) === stripLeadingPrep(cVn)) return true;
    if (stripLeadingPrep(uVnNoAcc) === stripLeadingPrep(cVnNoAcc)) return true;

    // Hoán vị cặp danh từ nối bằng "và" (ví dụ: chuột và bàn phím <-> bàn phím và chuột)
    if (uVn.includes(' và ') && cVn.includes(' và ')) {
        const uParts = uVn.split(' và ').map(s => s.trim());
        const cParts = cVn.split(' và ').map(s => s.trim());
        if (uParts.length === 2 && cParts.length === 2) {
            if (uParts[0] === cParts[1] && uParts[1] === cParts[0]) return true;
        }
    }
    if (uVnNoAcc.includes(' va ') && cVnNoAcc.includes(' va ')) {
        const uParts = uVnNoAcc.split(' va ').map(s => s.trim());
        const cParts = cVnNoAcc.split(' va ').map(s => s.trim());
        if (uParts.length === 2 && cParts.length === 2) {
            if (uParts[0] === cParts[1] && uParts[1] === cParts[0]) return true;
        }
    }

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
 * Đảm bảo câu hỏi luôn bảo toàn tiền tố "Câu <số> "
 * Nếu newQuestionBody chưa có tiền tố "Câu <số> ", trích xuất từ origQuestion hoặc dùng fallbackIndex
 */
function ensureQuestionNumber(origQuestion, newQuestionBody, fallbackIndex = null) {
    const target = (newQuestionBody !== undefined && newQuestionBody !== null) ? newQuestionBody : origQuestion;
    if (!target) return target || '';
    const src = (origQuestion || '').trim();
    const match = src.match(/^(Câu\s+\d+)[:.]?\s*/i);
    const prefix = match ? `${match[1]}: ` : (fallbackIndex != null ? `Câu ${fallbackIndex}: ` : '');

    const cleanTarget = target.trim();
    if (cleanTarget.match(/^Câu\s+\d+[:.]?\s*/i)) {
        // Chuẩn hóa tiền tố có dấu hai chấm nếu đang thiếu
        return cleanTarget.replace(/^(Câu\s+\d+)[:.]?\s*/i, '$1: ');
    }
    if (prefix) {
        return `${prefix}${cleanTarget}`;
    }
    return cleanTarget;
}

/**
 * Sinh đề ngẫu nhiên mới cho 1 câu hỏi cụ thể (Số đếm, Giá tiền Euro hoặc Chia động từ)
 */
function generateNewNumberData(ex, fallbackIndex = null) {
    let extra = {};
    try {
        extra = typeof ex.extra_data === 'string' ? JSON.parse(ex.extra_data) : (ex.extra_data || {});
    } catch (e) {
        return ex;
    }

    const origQuestion = ex.question || '';
    const finalize = (item) => {
        if (item && item.question) {
            item.question = ensureQuestionNumber(origQuestion, item.question, fallbackIndex);
        }
        return item;
    };

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
            ex.translation = extra.translation;
            ex.question = `[Luyện Nghe giá tiền Euro (Random)]: Nghe câu thông báo của nhân viên phục vụ và điền số tiền:`;
            ex.correct_answer = formattedPrice;
            ex.explanation = `Nhân viên phục vụ nói '${extra.audio_text}' → Số tiền là ${formattedPrice} € (hoặc gõ ${dePrice}).`;
        } else {
            extra.translation = `Giá tiền: ${formattedPrice} € (${dePrice})`;
            ex.extra_data = JSON.stringify(extra);
            ex.translation = extra.translation;
            ex.question = `[Viết giá tiền Euro (Random)]: Hãy viết giá tiền ${formattedPrice} € bằng chữ tiếng Đức (chấp nhận có hoặc không có chữ Cent):`;
            ex.correct_answer = dePrice;
            ex.explanation = `Giá tiền ${formattedPrice} € viết bằng chữ tiếng Đức là: '${dePrice}' (hoặc kèm 'Cent').`;
        }
        return finalize(ex);
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
            { label: "ich", personKey: "ich", pronoun: "ich", vi: "Tôi" },
            { label: "du", personKey: "du", pronoun: "du", vi: "Bạn" },
            { label: "er", personKey: "er_sie_es", pronoun: "er", vi: "Anh ấy" },
            { label: "sie (cô ấy)", personKey: "er_sie_es", pronoun: "sie", vi: "Cô ấy" },
            { label: "es", personKey: "er_sie_es", pronoun: "es", vi: "Nó" },
            { label: "wir", personKey: "wir", pronoun: "wir", vi: "Chúng tôi" },
            { label: "ihr", personKey: "ihr", pronoun: "ihr", vi: "Các bạn" },
            { label: "sie (họ)", personKey: "sie_Sie", pronoun: "sie", vi: "Họ" },
            { label: "Sie (Ngài)", personKey: "sie_Sie", pronoun: "Sie", vi: "Ngài" },
            { label: "Anna und ich", personKey: "wir", pronoun: "Anna und ich", vi: "Anna và tôi" },
            { label: "Du und Peter", personKey: "ihr", pronoun: "Du und Peter", vi: "Bạn và Peter" },
            { label: "Die Lehrerin", personKey: "er_sie_es", pronoun: "Die Lehrerin", vi: "Cô giáo" },
            { label: "Mein Freund", personKey: "er_sie_es", pronoun: "Mein Freund", vi: "Bạn của tôi" }
        ];

        const chosenSubject = subjects[Math.floor(Math.random() * subjects.length)];
        const correctForm = chosenVerb.forms[chosenSubject.personKey];

        ex.question = `[Rèn phản xạ Chia Động Từ (Random)]: Hãy chia động từ '${chosenVerb.infinitiv}' (${chosenVerb.meaning}) cho chủ ngữ '${chosenSubject.label}': '${chosenSubject.pronoun} ___'`;
        ex.correct_answer = correctForm;
        ex.explanation = `Động từ '${chosenVerb.infinitiv}' đi với chủ ngữ '${chosenSubject.label}' được chia là: '${correctForm}'.`;
        extra.translation = `${chosenSubject.vi} ${chosenVerb.meaning}.`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
        extra.translation = `Ist das ${qIndefinite} ${item1.word}? → Nein, das ist ${negWord} ${item1.word}. Das ist ${indWord} ${item2.word}. = Đây có phải là ${item1.meaning} không? → Không, đó không phải là ${item1.meaning}. Đó là một ${item2.meaning}.`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
        const personName = chosenName === "Herr Nguyen" ? "Herrn Nguyen" : chosenName;

        const indWord = chosenItem.gender === 'die' ? 'eine' : 'ein';
        const defWord = chosenItem.article; // der / die / das

        ex.question = `[Mạo từ Sở Hữu (Random)]: Hoàn thành câu xác nhận đồ vật của ${chosenName}: "Ist das ___ ${chosenItem.word}?" → "Ja, das ist ___ ${chosenItem.word} von ${personName}." (Điền 2 từ mạo từ cách nhau bởi dấu phẩy):`;
        ex.correct_answer = `${indWord}, ${defWord}`;
        ex.explanation = `'${chosenItem.word}' (${chosenItem.meaning}) mang giống ${defWord} → Mạo từ bất định là '${indWord}' và mạo từ xác định sở hữu là '${defWord} ${chosenItem.word} von ${personName}'.`;
        extra.translation = `Ist das ${indWord} ${chosenItem.word}? → Ja, das ist ${defWord} ${chosenItem.word} von ${personName}. = Đây có phải là ${chosenItem.meaning} không? → Vâng, đó là ${chosenItem.meaning} của ${chosenName}.`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
                { word: "Tisch", article: "der", plural: "die Tische", rule: "Thêm -e", meaning: "chiếc bàn" },
                { word: "Stuhl", article: "der", plural: "die Stühle", rule: "Biến âm u -> ü và thêm -e", meaning: "chiếc ghế" },
                { word: "Brille", article: "die", plural: "die Brillen", rule: "Thêm -n", meaning: "kính mắt" },
                { word: "Buch", article: "das", plural: "die Bücher", rule: "Biến âm u -> ü và thêm -er", meaning: "quyển sách" },
                { word: "Heft", article: "das", plural: "die Hefte", rule: "Thêm -e", meaning: "quyển vở" },
                { word: "Wörterbuch", article: "das", plural: "die Wörterbücher", rule: "Số nhiều theo Buch (die Wörterbücher)", meaning: "cuốn từ điển" },
                { word: "Handy", article: "das", plural: "die Handys", rule: "Thêm -s", meaning: "điện thoại" }
            ];
        const chosenItem = db[Math.floor(Math.random() * db.length)];

        ex.question = `[Số Nhiều Danh Từ (Random)]: Hãy viết dạng số nhiều (kèm mạo từ 'die') của danh từ '${chosenItem.article} ${chosenItem.word}':`;
        ex.correct_answer = chosenItem.plural;
        ex.explanation = `'${chosenItem.article} ${chosenItem.word}' khi chuyển sang số nhiều là '${chosenItem.plural}'. ${chosenItem.rule || ''}`;
        extra.translation = `${chosenItem.article} ${chosenItem.word} (${chosenItem.meaning || ''}) → ${chosenItem.plural} (những ${chosenItem.meaning || chosenItem.word})`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
            const pairsAdj = [
                { a: "Hai Phong", b: "Hanoi", adj: "östlich", viA: "Hải Phòng", viB: "Hà Nội", viDir: "phía Đông" },
                { a: "Hanoi", b: "Hue", adj: "nördlich", viA: "Hà Nội", viB: "Huế", viDir: "phía Bắc" },
                { a: "Long An", b: "Ho-Chi-Minh-Stadt", adj: "südwestlich", viA: "Long An", viB: "TP. Hồ Chí Minh", viDir: "phía Tây Nam" },
                { a: "Österreich", b: "Deutschland", adj: "südlich", viA: "Nước Áo", viB: "nước Đức", viDir: "phía Nam" },
                { a: "Hamburg", b: "Hannover", adj: "nördlich", viA: "Hamburg", viB: "Hannover", viDir: "phía Bắc" },
                { a: "München", b: "Nürnberg", adj: "südlich", viA: "München", viB: "Nürnberg", viDir: "phía Nam" },
                { a: "Köln", b: "Frankfurt", adj: "nordwestlich", viA: "Köln", viB: "Frankfurt", viDir: "phía Tây Bắc" },
                { a: "Dresden", b: "Leipzig", adj: "östlich", viA: "Dresden", viB: "Leipzig", viDir: "phía Đông" }
            ];
            const pair = pairsAdj[Math.floor(Math.random() * pairsAdj.length)];
            ex.question = `[Phương hướng Tính từ -lich (Random)]: Hãy dịch câu sau sang tiếng Đức (dùng TÍNH TỪ chỉ phương hướng -lich): '${pair.viA} nằm ở ${pair.viDir} của ${pair.viB}.'`;
            const alts = [
                `${pair.a} liegt ${pair.adj} von ${pair.b}.`,
                `${pair.a} liegt ${pair.adj} von ${pair.b}`
            ];
            if (pair.a === "Hai Phong") {
                alts.push(`Haiphong liegt ${pair.adj} von ${pair.b}.`);
                alts.push(`Hai Phong liegt ${pair.adj} von Ha Noi.`);
            } else if (pair.a === "Hanoi") {
                alts.push(`Ha Noi liegt ${pair.adj} von ${pair.b}.`);
            }
            ex.correct_answer = alts.join(" / ");
            ex.explanation = `Dùng tính từ chỉ phương hướng (-lich) so sánh 2 địa điểm riêng biệt: '${pair.a} liegt ${pair.adj} von ${pair.b}' (${pair.viA} nằm ở ${pair.viDir} của ${pair.viB}). Tuyệt đối không dùng 'im' trước tính từ.`;
            extra.translation = `${pair.viA} nằm ở ${pair.viDir} của ${pair.viB}.`;
        } else {
            const countryVi = chosen.country === "Vietnam" ? "Việt Nam" : "nước Đức";
            ex.question = `[Phương hướng Cụm Danh từ (Random)]: Hãy dịch câu sau sang tiếng Đức (dùng CỤM DANH TỪ chỉ phương hướng 'im ... von'): '${chosen.city} nằm ở ${chosen.vi} của ${countryVi}.'`;
            const nounAlts = [
                `${chosen.city} liegt ${chosen.noun} von ${chosen.country}.`,
                `${chosen.city} liegt ${chosen.noun} von ${chosen.country}`
            ];
            if (chosen.city === "Hanoi") {
                nounAlts.push(`Ha Noi liegt ${chosen.noun} von ${chosen.country}.`);
            } else if (chosen.city === "Hai Phong") {
                nounAlts.push(`Haiphong liegt ${chosen.noun} von ${chosen.country}.`);
                nounAlts.push(`Hai Phong liegt ${chosen.noun} von Viet Nam.`);
            } else if (chosen.city === "Da Nang") {
                nounAlts.push(`Đà Nẵng liegt ${chosen.noun} von ${chosen.country}.`);
                nounAlts.push(`Da Nang liegt ${chosen.noun} von Viet Nam.`);
            }
            ex.correct_answer = nounAlts.join(" / ");
            ex.explanation = `'${chosen.city}' nằm ở ${chosen.vi} của ${chosen.country} → Cụm giới từ là '${chosen.city} liegt ${chosen.noun} von ${chosen.country}' (nằm bên trong lãnh thổ).`;
            extra.translation = `${chosen.city} nằm ở ${chosen.vi} của ${countryVi}.`;
        }
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 7. Xử lý câu hỏi Ngữ pháp Quá khứ Präteritum & Giới từ (dynamic_landmark_quiz - Bài 3)
    if (extra.dynamic_landmark_quiz) {
        const grammarItems = [
            {
                q: "Chọn dạng quá khứ (Präteritum) đúng của động từ 'sein' cho chủ ngữ 'Paula und ich': \"Gestern ___ Paula und ich in Haiphong.\"",
                ans: "waren",
                options: ["waren", "war", "warst", "wart"],
                expl: "'Paula und ich' tương đương ngôi 'wir' (chúng tôi) → dạng quá khứ của 'sein' là 'waren'.",
                vi: "Hôm qua Paula và tôi đã ở Hải Phòng."
            },
            {
                q: "Chọn dạng quá khứ (Präteritum) đúng của động từ 'sein' cho ngôi 'du': \"___ du schon einmal in Deutschland?\"",
                ans: "Warst",
                options: ["Warst", "Wart", "War", "Waren"],
                expl: "Ngôi 'du' đi với quá khứ của 'sein' là 'warst' (đảo lên đầu câu viết hoa thành 'Warst').",
                vi: "Bạn đã từng ở Đức lần nào chưa?"
            },
            {
                q: "Chọn dạng quá khứ (Präteritum) đúng của động từ 'sein' cho ngôi 'ihr': \"Gestern ___ ihr im Theater, oder?\"",
                ans: "wart",
                options: ["wart", "warst", "waren", "war"],
                expl: "Ngôi 'ihr' đi với quá khứ của 'sein' chia là 'wart'.",
                vi: "Hôm qua các bạn đã ở rạp hát, đúng không?"
            },
            {
                q: "Điền mạo từ thích hợp ở Dativ đi sau giới từ 'aus' cho quốc gia giống cái 'die Schweiz': \"Frau Müller kommt aus ___ Schweiz.\"",
                ans: "der",
                options: ["der", "die", "den", "dem"],
                expl: "'die Schweiz' là quốc gia có mạo từ giống cái, sau giới từ 'aus' (Dativ) mạo từ 'die' chuyển thành 'der' → 'aus der Schweiz'.",
                vi: "Bà Müller đến từ Thụy Sỹ."
            },
            {
                q: "Điền mạo từ thích hợp ở Dativ đi sau giới từ 'in' cho quốc gia giống đực 'der Iran': \"Herr Meier wohnt in ___ Iran.\"",
                ans: "dem",
                options: ["dem", "der", "den", "das"],
                expl: "'der Iran' là quốc gia giống đực, sau giới từ 'in' (Dativ) mạo từ 'der' chuyển thành 'dem' (hoặc viết tắt là 'im').",
                vi: "Ông Meier sống ở Iran."
            },
            {
                q: "Điền mạo từ thích hợp ở Dativ đi sau giới từ 'in' cho quốc gia số nhiều 'die USA': \"David lebt in ___ USA.\"",
                ans: "den",
                options: ["den", "der", "die", "dem"],
                expl: "'die USA' là danh từ số nhiều, sau giới từ 'in' (Dativ số nhiều) mạo từ đổi thành 'den' → 'in den USA'.",
                vi: "David sống ở Mỹ."
            },
            {
                q: "Đâu là câu hỏi Có/Không (Ja/Nein-Frage) có trật tự từ ĐÚNG ngữ pháp tiếng Đức?",
                ans: "Wohnen Sie in Hai Phong?",
                options: ["Wohnen Sie in Hai Phong?", "Sie wohnen in Hai Phong?", "Wo wohnen Sie in Hai Phong?", "In Hai Phong wohnen Sie?"],
                expl: "Trong câu hỏi Có/Không (Ja/Nein-Frage), động từ bắt buộc phải đảo lên vị trí đầu câu (vị trí 1).",
                vi: "Ngài sống ở Hải Phòng phải không?"
            },
            {
                q: "Khi miêu tả vị trí bằng TÍNH TỪ phương hướng (-lich), câu nào sau đây ĐÚNG ngữ pháp?",
                ans: "Köln liegt westlich von Deutschland.",
                options: ["Köln liegt westlich von Deutschland.", "Köln liegt im westlich von Deutschland.", "Köln liegt am westlich von Deutschland.", "Köln liegt westlichen von Deutschland."],
                expl: "Tính từ phương hướng có đuôi '-lich' đứng độc lập sau 'liegt' và tuyệt đối KHÔNG có giới từ 'im' phía trước.",
                vi: "Köln nằm ở phía Tây của nước Đức."
            }
        ];

        const chosen = grammarItems[Math.floor(Math.random() * grammarItems.length)];
        const shuffled = [...chosen.options].sort(() => Math.random() - 0.5);

        ex.question = `[Ngữ pháp Trọng tâm (Random)]: ${chosen.q}`;
        ex.correct_answer = chosen.ans;
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.explanation = chosen.expl;
        extra.translation = chosen.vi || chosen.expl;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 8. Xử lý câu hỏi Chia 'sein' ở Thì Präteritum (dynamic_praeteritum_quiz - Bài 3)
    if (extra.dynamic_praeteritum_quiz) {
        const subjects = [
            { label: "ich", pronoun: "ich", form: "war", vi: "tôi" },
            { label: "du", pronoun: "du", form: "warst", vi: "bạn" },
            { label: "er (anh ấy)", pronoun: "er", form: "war", vi: "anh ấy" },
            { label: "sie (cô ấy)", pronoun: "sie", form: "war", vi: "cô ấy" },
            { label: "wir", pronoun: "wir", form: "waren", vi: "chúng tôi" },
            { label: "ihr", pronoun: "ihr", form: "wart", vi: "các bạn" },
            { label: "Sie (Ngài)", pronoun: "Sie", form: "waren", vi: "Ngài" },
            { label: "Paula und ich", pronoun: "Paula und ich", form: "waren", vi: "Paula và tôi" },
            { label: "du und Peter (ihr)", pronoun: "du und Peter", form: "wart", vi: "bạn và Peter" },
            { label: "Paula", pronoun: "Paula", form: "war", vi: "Paula" },
            { label: "Der Cat-Bi-Markt", pronoun: "Der Cat-Bi-Markt", form: "war", vi: "Chợ Cát Bi" }
        ];
        const times = [
            { de: "Gestern", vi: "Hôm qua" },
            { de: "Vorgestern", vi: "Hôm kia" },
            { de: "Letzte Woche", vi: "Tuần trước" },
            { de: "Früher", vi: "Trước đây" }
        ];
        const places = [
            { de: "in Haiphong", vi: "ở Hải Phòng" },
            { de: "in Hanoi", vi: "ở Hà Nội" },
            { de: "im Big-C-Supermarkt", vi: "ở siêu thị Big C" },
            { de: "im Theater", vi: "ở nhà hát" },
            { de: "auf dem Cat-Bi-Markt", vi: "ở chợ Cát Bi" },
            { de: "in Do Son am Meer", vi: "ở biển tại Đồ Sơn" },
            { de: "in Wien", vi: "ở Viên" },
            { de: "in Athen", vi: "ở Athens" }
        ];

        const chosenSub = subjects[Math.floor(Math.random() * subjects.length)];
        const chosenTime = times[Math.floor(Math.random() * times.length)];
        const chosenPlace = places[Math.floor(Math.random() * places.length)];

        ex.question = `[Chia 'sein' ở Thì Präteritum (Random)]: Điền dạng quá khứ đúng của động từ 'sein' cho chủ ngữ '${chosenSub.label}': "${chosenTime.de} ___ ${chosenSub.pronoun} ${chosenPlace.de}."`;
        ex.correct_answer = chosenSub.form;
        ex.explanation = `Chủ ngữ '${chosenSub.pronoun}' đi với thì Quá khứ đơn (Präteritum) của 'sein' là '${chosenSub.form}'. (${chosenTime.de} ${chosenSub.form} ${chosenSub.pronoun} ${chosenPlace.de}).`;
        extra.translation = `${chosenTime.vi}, ${chosenSub.vi} đã ${chosenPlace.vi}.`;
        const forms = ["war", "warst", "waren", "wart"];
        const shuffledOpts = [...forms].sort(() => Math.random() - 0.5);
        ex.options = shuffledOpts;
        ex.options_json = JSON.stringify(shuffledOpts);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 9. Xử lý câu hỏi Quốc gia & Ngôn ngữ (dynamic_country_language_quiz - Bài 3)
    if (extra.dynamic_country_language_quiz) {
        const countries = [
            { country: "die Schweiz", article: "die", lang: "Deutsch, Französisch, Italienisch", aus: "aus der Schweiz", in: "in der Schweiz", isSpecial: true, vi: "Thụy Sỹ" },
            { country: "die Türkei", article: "die", lang: "Türkisch", aus: "aus der Türkei", in: "in der Türkei", isSpecial: true, vi: "Thổ Nhĩ Kỳ" },
            { country: "die Slowakei", article: "die", lang: "Slowakisch", aus: "aus der Slowakei", in: "in der Slowakei", isSpecial: true, vi: "Slovakia" },
            { country: "der Iran", article: "der", lang: "Persisch", aus: "aus dem Iran", in: "im Iran", isSpecial: true, vi: "Iran" },
            { country: "die USA", article: "die (Pl.)", lang: "Englisch", aus: "aus den USA", in: "in den USA", isSpecial: true, vi: "Mỹ" },
            { country: "Deutschland", article: "—", lang: "Deutsch", aus: "aus Deutschland", in: "in Deutschland", isSpecial: false, vi: "Đức" },
            { country: "Österreich", article: "—", lang: "Deutsch", aus: "aus Österreich", in: "in Österreich", isSpecial: false, vi: "Áo" },
            { country: "Italien", article: "—", lang: "Italienisch", aus: "aus Italien", in: "in Italien", isSpecial: false, vi: "Ý" },
            { country: "Spanien", article: "—", lang: "Spanisch", aus: "aus Spanien", in: "in Spanien", isSpecial: false, vi: "Tây Ban Nha" },
            { country: "Griechenland", article: "—", lang: "Griechisch", aus: "aus Griechenland", in: "in Griechenland", isSpecial: false, vi: "Hy Lạp" },
            { country: "Frankreich", article: "—", lang: "Französisch", aus: "aus Frankreich", in: "in Frankreich", isSpecial: false, vi: "Pháp" },
            { country: "Russland", article: "—", lang: "Russisch", aus: "aus Russland", in: "in Russland", isSpecial: false, vi: "Nga" },
            { country: "Polen", article: "—", lang: "Polnisch", aus: "aus Polen", in: "in Polen", isSpecial: false, vi: "Ba Lan" },
            { country: "Vietnam", article: "—", lang: "Vietnamesisch", aus: "aus Vietnam", in: "in Vietnam", isSpecial: false, vi: "Việt Nam" }
        ];

        const chosen = countries[Math.floor(Math.random() * countries.length)];
        const quizType = chosen.isSpecial ? (Math.random() > 0.5 ? 'preposition' : 'language') : 'language';

        if (quizType === 'preposition') {
            const useAus = Math.random() > 0.5;
            if (useAus) {
                ex.question = `[Giới từ 'aus' với Quốc gia có mạo từ (Random)]: Điền cụm giới từ 'đến từ' cho quốc gia '${chosen.country}': "Frau Müller kommt ___."`;
                ex.correct_answer = chosen.aus;
                ex.explanation = `'${chosen.country}' là quốc gia có mạo từ, khi kết hợp với 'aus' ở Dativ phải đổi thành '${chosen.aus}'.`;
                extra.translation = `Bà Müller đến từ ${chosen.vi}.`;
            } else {
                ex.question = `[Giới từ 'in' với Quốc gia có mạo từ (Random)]: Điền cụm giới từ 'ở tại' cho quốc gia '${chosen.country}': "Herr Meier wohnt ___."`;
                ex.correct_answer = chosen.in;
                ex.explanation = `'${chosen.country}' ở Dativ khi đi với giới từ 'in' là '${chosen.in}'.`;
                extra.translation = `Ông Meier sống ở ${chosen.vi}.`;
            }
        } else {
            ex.question = `[Ngôn ngữ Quốc gia (Random)]: Ngôn ngữ chính được nói tại '${chosen.country}' là gì? (Ví dụ: Deutsch, Französisch, Spanisch...):`;
            ex.correct_answer = chosen.lang;
            ex.explanation = `Tại '${chosen.country}', ngôn ngữ chính là: '${chosen.lang}'.`;
            extra.translation = `Tại ${chosen.vi}, ngôn ngữ chính là tiếng ${chosen.lang}.`;
        }
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
                meaning: "Tôi tên là Anna.",
                wMeaning: "Ngài tên là gì? (hoặc: Bạn tên là gì?)",
                jnMeaning: "Ngài tên là Anna phải không? (hoặc: Bạn tên là Anna phải không?)"
            },
            {
                statement: "Ich wohne in Hai Phong.",
                wQuestion: "Wo wohnen Sie?",
                wAlt: "Wo wohnst du?",
                jnQuestion: "Wohnen Sie in Hai Phong?",
                jnAlt: "Wohnst du in Hai Phong?",
                meaning: "Tôi sống ở Hải Phòng.",
                wMeaning: "Ngài sống ở đâu? (hoặc: Bạn sống ở đâu?)",
                jnMeaning: "Ngài sống ở Hải Phòng phải không?"
            },
            {
                statement: "Er macht die Hausaufgaben.",
                wQuestion: "Was macht er?",
                wAlt: "Was macht er?",
                jnQuestion: "Macht er die Hausaufgaben?",
                jnAlt: "Macht er die Hausaufgaben?",
                meaning: "Anh ấy làm bài tập về nhà.",
                wMeaning: "Anh ấy đang làm gì?",
                jnMeaning: "Anh ấy đang làm bài tập về nhà phải không?"
            },
            {
                statement: "Sie ist Lehrerin.",
                wQuestion: "Wer ist sie?",
                wAlt: "Was ist sie von Beruf?",
                jnQuestion: "Ist sie Lehrerin?",
                jnAlt: "Ist sie Lehrerin?",
                meaning: "Cô ấy là giáo viên.",
                wMeaning: "Cô ấy là ai? (hoặc: Cô ấy làm nghề gì?)",
                jnMeaning: "Cô ấy là giáo viên phải không?"
            },
            {
                statement: "Carlos kommt aus Wien.",
                wQuestion: "Woher kommt Carlos?",
                wAlt: "Woher kommt er?",
                jnQuestion: "Kommt Carlos aus Wien?",
                jnAlt: "Kommt er aus Wien?",
                meaning: "Carlos đến từ Viên.",
                wMeaning: "Carlos đến từ đâu?",
                jnMeaning: "Carlos đến từ Viên phải không?"
            },
            {
                statement: "Hanoi liegt im Norden von Vietnam.",
                wQuestion: "Wo liegt Hanoi?",
                wAlt: "Wo liegt Hanoi?",
                jnQuestion: "Liegt Hanoi im Norden von Vietnam?",
                jnAlt: "Liegt Hanoi im Norden von Vietnam?",
                meaning: "Hà Nội nằm ở miền Bắc Việt Nam.",
                wMeaning: "Hà Nội nằm ở đâu?",
                jnMeaning: "Hà Nội nằm ở miền Bắc Việt Nam phải không?"
            }
        ];

        const chosen = sentencePool[Math.floor(Math.random() * sentencePool.length)];
        const askW = Math.random() > 0.5;

        if (askW) {
            ex.question = `[Chuyển sang W-Frage (Random)]: Hãy chuyển câu trần thuật "${chosen.statement}" (${chosen.meaning}) sang câu hỏi có từ để hỏi (W-Frage):`;
            ex.correct_answer = `${chosen.wQuestion} / ${chosen.wAlt}`;
            ex.explanation = `Câu hỏi W-Frage tương ứng là: '${chosen.wQuestion}' (hoặc thân mật: '${chosen.wAlt}').`;
            extra.translation = chosen.wMeaning;
        } else {
            ex.question = `[Chuyển sang Ja/Nein-Frage (Random)]: Hãy chuyển câu trần thuật "${chosen.statement}" (${chosen.meaning}) sang câu hỏi Có/Không (Ja/Nein-Frage):`;
            ex.correct_answer = `${chosen.jnQuestion} / ${chosen.jnAlt}`;
            ex.explanation = `Đẩy động từ lên đầu câu để tạo Ja/Nein-Frage: '${chosen.jnQuestion}' (hoặc: '${chosen.jnAlt}').`;
            extra.translation = chosen.jnMeaning;
        }
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
        let sentenceVi = "";
        if (modeType === 0) sentenceVi = `Chúng tôi có một ${chosen.meaning}.`;
        else if (modeType === 1) sentenceVi = `Ở phía trên có một ${chosen.meaning}.`;
        else if (modeType === 2) sentenceVi = `Tôi thấy ${chosen.meaning} rất đẹp.`;
        else sentenceVi = `Căn hộ không có ${chosen.meaning}.`;
        extra.translation = sentenceVi;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 12. Xử lý câu hỏi Mạo từ sở hữu theo 9 Ngôi (dynamic_possessiv_quiz - Bài 4)
    if (extra.dynamic_possessiv_quiz) {
        const owners = [
            { label: "ich (tôi)", stem: "mein", vi: "tôi" },
            { label: "du (bạn)", stem: "dein", vi: "bạn" },
            { label: "er (anh ấy / Peter)", stem: "sein", vi: "anh ấy" },
            { label: "sie (cô ấy / Lena)", stem: "ihr", vi: "cô ấy" },
            { label: "wir (chúng tôi)", stem: "unser", vi: "chúng tôi" },
            { label: "ihr (các bạn / Maria und Lukas)", stem: "euer", isEuer: true, vi: "các bạn" },
            { label: "sie (họ / die Eltern)", stem: "ihr", vi: "họ" },
            { label: "Sie (Ngài / Herr Müller)", stem: "Ihr", isCapital: true, vi: "Ngài" }
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
        extra.translation = isAkk ? `Chúng tôi có ${noun.vi} của ${owner.vi}.` : `Đó là ${noun.vi} của ${owner.vi}.`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 13. Xử lý câu hỏi Tính từ Đối lập Miêu tả Nhà cửa (dynamic_adjective_antonym_quiz - Bài 4)
    if (extra.dynamic_adjective_antonym_quiz) {
        const adjPairs = [
            { pos: "hell", neg: "dunkel", viPos: "sáng sủa", viNeg: "tối tăm", context: "Arbeitszimmer", nounVi: "phòng làm việc", art: "Das" },
            { pos: "groß", neg: "klein", viPos: "rộng lớn", viNeg: "nhỏ hẹp", context: "Wohnzimmer", nounVi: "phòng khách", art: "Das" },
            { pos: "ruhig", neg: "laut", viPos: "yên tĩnh", viNeg: "ồn ào", context: "Schlafzimmer", nounVi: "phòng ngủ", art: "Das" },
            { pos: "lang", neg: "kurz", viPos: "dài", viNeg: "ngắn", context: "Flur", nounVi: "hành lang", art: "Der" },
            { pos: "neu", neg: "alt", viPos: "mới", viNeg: "cũ / lâu năm", context: "Haus", nounVi: "ngôi nhà", art: "Das" },
            { pos: "billig", neg: "teuer", viPos: "rẻ", viNeg: "đắt đỏ", context: "Wohnung", nounVi: "căn hộ", art: "Die" },
            { pos: "schön", neg: "hässlich", viPos: "đẹp", viNeg: "xấu xí", context: "Garten", nounVi: "khu vườn", art: "Der" },
            { pos: "modern", neg: "altmodisch", viPos: "hiện đại", viNeg: "lỗi thời / kiểu cũ", context: "Wohnzimmer", nounVi: "phòng khách", art: "Das" },
            { pos: "gemütlich", neg: "ungemütlich", viPos: "ấm cúng", viNeg: "không ấm cúng, khó chịu", context: "Schlafzimmer", nounVi: "phòng ngủ", art: "Das" }
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
            extra.translation = `Từ trái nghĩa của '${sourceVi}' là '${targetVi}'.`;
        } else {
            ex.question = `[Tính từ Miêu tả Nhà cửa (Random)]: Hoàn thành câu miêu tả sau bằng tính từ trái nghĩa với '${sourceWord}': "${pair.art} ${pair.context} ist nicht ${sourceWord}, sondern es ist ___."`;
            ex.correct_answer = targetWord;
            ex.explanation = `Từ đối lập với '${sourceWord}' (${sourceVi}) là '${targetWord}' (${targetVi}) → "${pair.art} ${pair.context} ist nicht ${sourceWord}, sondern es ist ${targetWord}."`;
            extra.translation = `${pair.nounVi.charAt(0).toUpperCase() + pair.nounVi.slice(1)} không ${sourceVi}, mà nó ${targetVi}.`;
        }
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 14. Xử lý câu hỏi Thay thế Đại từ Nhân xưng theo Giống (dynamic_pronoun_replacement_quiz - Bài 4)
    if (extra.dynamic_pronoun_replacement_quiz) {
        const pronounItems = [
            { word: "Flur", gender: "der", pronoun: "Er", sentence: "Das Haus hat einen Flur. ___ ist lang und dunkel.", sentenceVi: "Ngôi nhà có một hành lang. Nó dài và tối." },
            { word: "Garten", gender: "der", pronoun: "Er", sentence: "Wir haben einen Garten. ___ ist groß und sehr schön.", sentenceVi: "Chúng tôi có một khu vườn. Nó rộng và rất đẹp." },
            { word: "Balkon", gender: "der", pronoun: "Er", sentence: "Oben gibt es einen Balkon. ___ ist sonnig und hell.", sentenceVi: "Ở phía trên có một ban công. Nó nhiều nắng và sáng sủa." },
            { word: "Kühlschrank", gender: "der", pronoun: "Er", sentence: "Er kauft einen Kühlschrank. ___ ist modern und neu.", sentenceVi: "Anh ấy mua một chiếc tủ lạnh. Nó hiện đại và mới." },
            { word: "Küche", gender: "die", pronoun: "Sie", sentence: "Die Wohnung hat eine Küche. ___ ist klein, aber gemütlich.", sentenceVi: "Căn hộ có một phòng bếp. Nó nhỏ nhưng ấm cúng." },
            { word: "Wohnung", gender: "die", pronoun: "Sie", sentence: "Wir mieten eine Wohnung. ___ hat 4 Zimmer.", sentenceVi: "Chúng tôi thuê một căn hộ. Nó có 4 phòng." },
            { word: "Garage", gender: "die", pronoun: "Sie", sentence: "Das Haus hat eine Garage. ___ ist sehr praktisch.", sentenceVi: "Ngôi nhà có một nhà để xe. Nó rất tiện lợi." },
            { word: "Wohnzimmer", gender: "das", pronoun: "Es", sentence: "Wir haben ein Wohnzimmer. ___ ist hell und modern.", sentenceVi: "Chúng tôi có một phòng khách. Nó sáng sủa và hiện đại." },
            { word: "Haus", gender: "das", pronoun: "Es", sentence: "Julia hat ein Haus. ___ ist sehr alt und hat 5 Zimmer.", sentenceVi: "Julia có một ngôi nhà. Nó rất cũ và có 5 phòng." },
            { word: "Schlafzimmer", gender: "das", pronoun: "Es", sentence: "Mein Haus hat ein Schlafzimmer. ___ ist leise und warm.", sentenceVi: "Nhà của tôi có một phòng ngủ. Nó yên tĩnh và ấm áp." }
        ];

        const item = pronounItems[Math.floor(Math.random() * pronounItems.length)];
        ex.question = `[Đại từ Thay thế theo Giống (Random)]: Điền đại từ nhân xưng thích hợp ('Er' / 'Sie' / 'Es') thay thế cho danh từ giống '${item.gender}' (${item.word}): "${item.sentence}"`;
        ex.correct_answer = item.pronoun;
        ex.explanation = `'${item.word}' mang giống '${item.gender}' nên đại từ nhân xưng làm chủ ngữ thay thế ở câu sau là '${item.pronoun}' (der → er, die → sie, das → es).`;
        extra.translation = item.sentenceVi;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
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
        extra.translation = chosen.vi;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 16. Xử lý câu hỏi Đổi giờ Đời thường (dynamic_time_quiz - Bài 5)
    if (extra.dynamic_time_quiz) {
        const timeItems = [
            { time: "08:15", off: "acht Uhr fünfzehn", inoff: "Viertel nach acht", wrong: ["Viertel vor acht", "halb acht", "acht nach Viertel"], exp: "Hơn 15 phút (1/4 giờ) qua mốc 8 giờ → 'Viertel nach acht'.", vi: "8 giờ 15 phút (8 giờ hơn 15)" },
            { time: "09:30", off: "neun Uhr dreißig", inoff: "halb zehn", wrong: ["halb neun", "Viertel nach neun", "dreißig nach neun"], exp: "9h30 = còn nửa tiếng nữa đến 10 giờ → 'halb zehn'.", vi: "9 giờ 30 phút (9 rưỡi)" },
            { time: "09:05", off: "neun Uhr fünf", inoff: "fünf nach neun", wrong: ["fünf vor neun", "halb zehn", "zehn nach neun"], exp: "9 giờ hơn 5 phút → 'fünf nach neun'.", vi: "9 giờ 5 phút" },
            { time: "07:50", off: "sieben Uhr fünfzig", inoff: "zehn vor acht", wrong: ["zehn nach sieben", "fünfzig nach sieben", "Viertel vor acht"], exp: "7h50 = 8 giờ kém 10 phút → 'zehn vor acht'.", vi: "7 giờ 50 phút (8 giờ kém 10)" },
            { time: "20:10", off: "zwanzig Uhr zehn", inoff: "zehn nach acht", wrong: ["zehn nach zwanzig", "zehn vor acht", "Viertel nach acht"], exp: "20h10 đổi sang hệ 12 tiếng là 8h10 tối → 'zehn nach acht'.", vi: "20 giờ 10 phút (8 giờ 10 tối)" },
            { time: "03:15", off: "drei Uhr fünfzehn", inoff: "Viertel nach drei", wrong: ["Viertel vor drei", "halb vier", "fünfzehn vor drei"], exp: "3 giờ hơn 15 phút → 'Viertel nach drei'.", vi: "3 giờ 15 phút (3 giờ hơn 15)" },
            { time: "05:45", off: "fünf Uhr fünfundvierzig", inoff: "Viertel vor sechs", wrong: ["Viertel nach fünf", "fünfundvierzig nach fünf", "halb sechs"], exp: "5h45 = 6 giờ kém 15 phút → 'Viertel vor sechs'.", vi: "5 giờ 45 phút (6 giờ kém 15)" },
            { time: "08:30", off: "acht Uhr dreißig", inoff: "halb neun", wrong: ["halb acht", "Viertel vor neun", "dreißig nach acht"], exp: "8 giờ rưỡi → 'halb neun' (nửa tiếng trước 9h).", vi: "8 giờ 30 phút (8 rưỡi)" },
            { time: "02:30", off: "zwei Uhr dreißig", inoff: "halb drei", wrong: ["halb zwei", "Viertel nach zwei", "dreißig nach zwei"], exp: "2 giờ rưỡi → 'halb drei' (nửa tiếng trước 3h).", vi: "2 giờ 30 phút (2 rưỡi)" },
            { time: "05:50", off: "fünf Uhr fünfzig", inoff: "zehn vor sechs", wrong: ["zehn nach fünf", "fünfzig nach fünf", "Viertel vor sechs"], exp: "5h50 = 6 giờ kém 10 phút → 'zehn vor sechs'.", vi: "5 giờ 50 phút (6 giờ kém 10)" },
            { time: "06:05", off: "sechs Uhr fünf", inoff: "fünf nach sechs", wrong: ["fünf vor sechs", "halb sieben", "zehn nach sechs"], exp: "6 giờ hơn 5 phút → 'fünf nach sechs'.", vi: "6 giờ 5 phút" },
            { time: "10:30", off: "zehn Uhr dreißig", inoff: "halb elf", wrong: ["halb zehn", "Viertel nach zehn", "dreißig nach zehn"], exp: "10 giờ rưỡi = còn nửa tiếng đến 11 giờ → 'halb elf'.", vi: "10 giờ 30 phút (10 rưỡi)" },
            { time: "11:15", off: "elf Uhr fünfzehn", inoff: "Viertel nach elf", wrong: ["Viertel vor elf", "halb zwölf", "fünfzehn nach elf"], exp: "11 giờ hơn 15 phút → 'Viertel nach elf'.", vi: "11 giờ 15 phút (11 giờ hơn 15)" },
            { time: "04:45", off: "vier Uhr fünfundvierzig", inoff: "Viertel vor fünf", wrong: ["Viertel nach vier", "halb fünf", "fünfzehn vor fünf"], exp: "4h45 = 5 giờ kém 15 phút → 'Viertel vor fünf'.", vi: "4 giờ 45 phút (5 giờ kém 15)" },
            { time: "01:30", off: "ein Uhr dreißig", inoff: "halb zwei", wrong: ["halb eins", "Viertel nach eins", "dreißig nach eins"], exp: "1 giờ rưỡi = còn nửa tiếng đến 2 giờ → 'halb zwei'.", vi: "1 giờ 30 phút (1 rưỡi)" }
        ];
        const chosen = timeItems[Math.floor(Math.random() * timeItems.length)];
        ex.question = `[Đổi cách nói giờ (Random)]: Cách đọc giờ đời thường (Inoffiziell) nào sau đây tương ứng với ${chosen.time} (${chosen.off})?`;
        ex.correct_answer = chosen.inoff;
        ex.explanation = chosen.exp;
        extra.translation = `Mốc giờ ${chosen.time} (${chosen.off}) = ${chosen.inoff}: ${chosen.vi}`;
        const opts = [chosen.inoff, ...chosen.wrong];
        const shuffled = opts.sort(() => Math.random() - 0.5);
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 17. Xử lý câu hỏi Giới từ thời gian (dynamic_prep_quiz - Bài 5)
    if (extra.dynamic_prep_quiz) {
        const prepItems = [
            { question: "___ Sonntag steht er ___ 8 Uhr auf.", correct: "Am / um", wrong: ["Im / um", "Um / am", "Am / im"], exp: "Thứ trong tuần ('Sonntag') đi với 'am'; giờ giấc cụ thể ('8 Uhr') đi với 'um'.", trans: "Vào Chủ nhật anh ấy thức dậy vào lúc 8 giờ." },
            { question: "___ Montag beginnt meine Arbeit ___ 9 Uhr.", correct: "Am / um", wrong: ["Im / um", "Um / am", "In der / um"], exp: "Thứ trong tuần ('Montag') đi với 'am'; giờ cụ thể ('9 Uhr') đi với 'um'.", trans: "Vào thứ Hai công việc của tôi bắt đầu vào lúc 9 giờ." },
            { question: "Mein Deutschkurs ist ___ Dienstag ___ 18 Uhr.", correct: "am / um", wrong: ["im / um", "um / am", "am / im"], exp: "Thứ trong tuần đi với 'am'; mốc giờ đi với 'um'.", trans: "Khóa học tiếng Đức của tôi diễn ra vào thứ Ba lúc 18 giờ." },
            { question: "___ Juni fahren wir nach Berlin, ___ Sommer ist das Wetter super.", correct: "Im / im", wrong: ["Am / am", "Um / im", "Im / am"], exp: "Tháng trong năm ('Juni') và mùa ('Sommer') đều đi với giới từ 'im'.", trans: "Vào tháng Sáu chúng tôi đi tới Berlin, vào mùa hè thời tiết rất tuyệt." },
            { question: "___ Freitag ___ 20 Uhr geht ihr mit Freunden aus.", correct: "Am / um", wrong: ["Im / um", "Um / am", "In / um"], exp: "Thứ Sáu đi với 'am'; 20 Uhr đi với 'um'.", trans: "Vào thứ Sáu lúc 20 giờ các bạn đi chơi với bạn bè." },
            { question: "___ Morgen trinken sie Kaffee, aber ___ Nacht schlafen sie viel.", correct: "Am / in der", wrong: ["Im / am", "Am / am", "In der / am"], exp: "'der Morgen' đi với 'am'; ngoại lệ 'die Nacht' (giống cái) bắt buộc đi với 'in der Nacht'.", trans: "Vào buổi sáng họ uống cà phê, nhưng vào ban đêm họ ngủ nhiều." }
        ];
        const chosen = prepItems[Math.floor(Math.random() * prepItems.length)];
        ex.question = `[Giới từ thời gian (Random)]: Chọn giới từ thích hợp điền vào câu: '${chosen.question}'`;
        ex.correct_answer = chosen.correct;
        ex.explanation = chosen.exp;
        extra.translation = chosen.trans;
        const opts = [chosen.correct, ...chosen.wrong];
        const shuffled = opts.sort(() => Math.random() - 0.5);
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 18. Xử lý câu hỏi Động từ tách (dynamic_trennbare_quiz - Bài 5)
    if (extra.dynamic_trennbare_quiz) {
        const trennbareItems = [
            { verb: "aufmachen", subject: "Wir", object: "das Fenster", stem: "machen", prefix: "auf", wrong: ["aufmachen / —", "macht / auf", "auf / machen"], exp: "Động từ tách 'aufmachen': gốc 'machen' đứng ở V2 theo ngôi 'wir', tiền tố 'auf' đứng cuối câu.", trans: "Chúng tôi mở cửa sổ ra." },
            { verb: "zumachen", subject: "Er", object: "die Tür", stem: "macht", prefix: "zu", wrong: ["zumacht / —", "mache / zu", "macht / auf"], exp: "Động từ tách 'zumachen': gốc 'macht' đứng ở V2 theo ngôi 'er', tiền tố 'zu' đứng cuối câu.", trans: "Anh ấy đóng cánh cửa lại." },
            { verb: "aufstehen", subject: "Wir", object: "am Sonntag um 8 Uhr", stem: "stehen", prefix: "auf", wrong: ["aufstehen / —", "steht / auf", "stehen / aus"], exp: "Động từ tách 'aufstehen': gốc 'stehen' chia theo 'wir', tiền tố 'auf' đứng cuối câu.", trans: "Vào Chủ nhật chúng tôi thức dậy lúc 8 giờ." },
            { verb: "ausgehen", subject: "Du", object: "am Freitag um 20 Uhr", stem: "gehst", prefix: "aus", wrong: ["ausgehst / —", "gehe / aus", "geht / aus"], exp: "Động từ tách 'ausgehen': gốc 'gehst' chia theo 'du', tiền tố 'aus' đứng cuối câu.", trans: "Vào thứ Sáu lúc 20 giờ bạn đi chơi." },
            { verb: "einkaufen", subject: "Anna", object: "im Supermarkt", stem: "kauft", prefix: "ein", wrong: ["einkauft / —", "kaufe / ein", "kaufen / ein"], exp: "Động từ tách 'einkaufen': gốc 'kauft' chia theo 'Anna' (sie), tiền tố 'ein' đứng cuối câu.", trans: "Anna đi mua sắm ở siêu thị." },
            { verb: "anmachen", subject: "Ihr", object: "die Lampe am Abend", stem: "macht", prefix: "an", wrong: ["anmacht / —", "mache / an", "macht / aus"], exp: "Động từ tách 'anmachen': gốc 'macht' chia theo ngôi 'ihr', tiền tố 'an' đứng cuối câu.", trans: "Các bạn bật đèn vào buổi tối." },
            { verb: "fernsehen", subject: "Mein Vater", object: "am Abend gern", stem: "sieht", prefix: "fern", wrong: ["siehst / fern", "seht / fern", "fernsehen / —"], exp: "Động từ tách 'fernsehen': biến âm 'e -> ie' ở ngôi thứ 3 số ít là 'sieht', tiền tố 'fern' đứng cuối câu.", trans: "Vào buổi tối bố tôi thích xem tivi." }
        ];
        const chosen = trennbareItems[Math.floor(Math.random() * trennbareItems.length)];
        ex.question = `[Động từ tách (Random)]: Chọn dạng đúng của '${chosen.verb}' cho câu: '${chosen.subject} ___ ${chosen.object} ___.'`;
        ex.correct_answer = `${chosen.stem} / ${chosen.prefix}`;
        ex.explanation = chosen.exp;
        extra.translation = chosen.trans;
        const opts = [`${chosen.stem} / ${chosen.prefix}`, ...chosen.wrong];
        const shuffled = opts.sort(() => Math.random() - 0.5);
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 19. Xử lý câu hỏi Phương tiện giao thông & Chủ ngữ đa dạng (dynamic_dativ_transport_quiz - Bài 6)
    if (extra.dynamic_dativ_transport_quiz) {
        const subjects = [
            { name: "Mein Bruder", pronoun: "er", verbForm: "fährt", vi: "Anh trai tôi" },
            { name: "Meine Mutter", pronoun: "sie", verbForm: "fährt", vi: "Mẹ tôi" },
            { name: "Herr Schneider", pronoun: "er", verbForm: "fährt", vi: "Ông Schneider" },
            { name: "Frau Wagner", pronoun: "sie", verbForm: "fährt", vi: "Bà Wagner" },
            { name: "Wir", pronoun: "wir", verbForm: "fahren", vi: "Chúng tôi" },
            { name: "Ihr", pronoun: "ihr", verbForm: "fahrt", vi: "Các bạn" },
            { name: "Meine Eltern", pronoun: "sie_pl", verbForm: "fahren", vi: "Bố mẹ tôi" },
            { name: "Die Studenten", pronoun: "sie_pl", verbForm: "fahren", vi: "Các sinh viên" }
        ];
        const vehicles = [
            { prep: "mit der Straßenbahn", wrong: ["mit die Straßenbahn", "mit dem Straßenbahn", "mit den Straßenbahn"], noun: "die Straßenbahn", vi: "bằng tàu điện mặt đất" },
            { prep: "mit dem Bus", wrong: ["mit der Bus", "mit den Bus", "mit das Bus"], noun: "der Bus", vi: "bằng xe buýt" },
            { prep: "mit dem Zug", wrong: ["mit der Zug", "mit den Zug", "mit das Zug"], noun: "der Zug", vi: "bằng tàu hỏa" },
            { prep: "mit der U-Bahn", wrong: ["mit die U-Bahn", "mit dem U-Bahn", "mit den U-Bahn"], noun: "die U-Bahn", vi: "bằng tàu điện ngầm" },
            { prep: "mit dem Fahrrad", wrong: ["mit das Fahrrad", "mit der Fahrrad", "mit den Fahrrad"], noun: "das Fahrrad", vi: "bằng xe đạp" },
            { prep: "mit dem Auto", wrong: ["mit das Auto", "mit der Auto", "mit den Auto"], noun: "das Auto", vi: "bằng ô tô" }
        ];
        const destinations = [
            { text: "zur Arbeit", vi: "đi làm" },
            { text: "zur Universität", vi: "đến trường đại học" },
            { text: "zum Bahnhof", vi: "đến nhà ga" },
            { text: "in die Stadt", vi: "vào thành phố" }
        ];

        const s = subjects[Math.floor(Math.random() * subjects.length)];
        const v = vehicles[Math.floor(Math.random() * vehicles.length)];
        const d = destinations[Math.floor(Math.random() * destinations.length)];

        ex.question = `[Phương tiện Dativ (Random)]: Chọn cụm từ đúng để hoàn thành câu: '${s.name} ${s.verbForm} jeden Morgen ___ ${d.text}.'`;
        ex.correct_answer = v.prep;
        ex.explanation = `Giới từ 'mit' luôn đi với Cách 3 (Dativ). Danh từ '${v.noun}' ở Dativ chuyển thành '${v.prep}'.`;
        extra.translation = `${s.vi} ${d.vi} mỗi buổi sáng ${v.vi}. (${s.name} ${s.verbForm} jeden Morgen ${v.prep} ${d.text}.)`;
        const opts = [v.prep, ...v.wrong];
        const shuffled = opts.sort(() => Math.random() - 0.5);
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 20. Xử lý câu hỏi Số thứ tự & Ngày tháng (dynamic_ordinal_date_quiz - Bài 6)
    if (extra.dynamic_ordinal_date_quiz) {
        const dateItems = [
            { day: "1.", nom: "erste", dat: "ersten", month: "Mai", viMonth: "tháng Năm" },
            { day: "3.", nom: "dritte", dat: "dritten", month: "März", viMonth: "tháng Ba" },
            { day: "7.", nom: "siebte", dat: "siebten", month: "August", viMonth: "tháng Tám" },
            { day: "8.", nom: "achte", dat: "achten", month: "März", viMonth: "tháng Ba" },
            { day: "15.", nom: "fünfzehnte", dat: "fünfzehnten", month: "Oktober", viMonth: "tháng Mười" },
            { day: "20.", nom: "zwanzigste", dat: "zwanzigsten", month: "September", viMonth: "tháng Chín" },
            { day: "21.", nom: "einundzwanzigste", dat: "einundzwanzigsten", month: "Juni", viMonth: "tháng Sáu" }
        ];
        const item = dateItems[Math.floor(Math.random() * dateItems.length)];
        const isDatMode = (Math.random() > 0.5);

        if (isDatMode) {
            ex.question = `[Ngày tháng Dativ (Random)]: Điền dạng chữ của số thứ tự (${item.day}) sau giới từ 'am' vào chỗ trống: 'Meine Schwester hat am ___ ${item.month} Geburtstag.'`;
            ex.correct_answer = item.dat;
            ex.explanation = `Sau giới từ 'am' (Dativ), số thứ tự '${item.day}' mang đuôi '-ten/-sten' là '${item.dat}'.`;
            extra.translation = `Em gái tôi có sinh nhật vào ngày ${item.day.replace('.', '')} ${item.viMonth}.`;
            extra.accepted_answers = [item.dat];
        } else {
            ex.question = `[Ngày tháng Nominativ (Random)]: Điền dạng chữ của số thứ tự (${item.day}) sau mạo từ 'der' vào chỗ trống: 'Heute ist der ___ ${item.month}.'`;
            ex.correct_answer = item.nom;
            ex.explanation = `Sau 'Heute ist der ...' (Nominativ), số thứ tự '${item.day}' mang đuôi '-te/-ste' là '${item.nom}'.`;
            extra.translation = `Hôm nay là ngày ${item.day.replace('.', '')} ${item.viMonth}.`;
            extra.accepted_answers = [item.nom];
        }
        ex.options = null;
        ex.options_json = null;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 21. Xử lý câu hỏi Giới từ vị trí Dativ (dynamic_dativ_position_quiz - Bài 6)
    if (extra.dynamic_dativ_position_quiz) {
        const posItems = [
            { item: "Der schwere Drucker", verb: "steht", prep: "auf", target: "dem Schreibtisch", wrong: ["auf den Schreibtisch", "über dem Schreibtisch", "an der Schreibtisch"], exp: "'der Schreibtisch' ở bề mặt ngang có tiếp xúc dùng 'auf dem Schreibtisch'.", trans: "Chiếc máy in nặng đặt trên bàn làm việc." },
            { item: "Das schöne Bild", verb: "hängt", prep: "an", target: "der Wand", wrong: ["an die Wand", "auf der Wand", "in der Wand"], exp: "'die Wand' (mặt thẳng đứng) dùng 'an der Wand'.", trans: "Bức tranh đẹp treo trên tường." },
            { item: "Das Café", verb: "liegt", prep: "zwischen", target: "der Bank und dem Kino", wrong: ["zwischen die Bank und das Kino", "neben der Bank und der Kino", "in der Bank und dem Kino"], exp: "Giới từ 'zwischen' đi với Dativ của cả 2 danh từ: 'der Bank und dem Kino'.", trans: "Quán cà phê nằm giữa ngân hàng và rạp chiếu phim." },
            { item: "Der große Parkplatz", verb: "liegt", prep: "hinter", target: "dem Krankenhaus", wrong: ["hinter das Krankenhaus", "vor der Krankenhaus", "neben den Krankenhaus"], exp: "'das Krankenhaus' ở Dativ đổi thành 'dem Krankenhaus'.", trans: "Bãi đỗ xe lớn nằm phía sau bệnh viện." },
            { item: "Das Taxi", verb: "wartet", prep: "vor", target: "dem Hotel", wrong: ["vor das Hotel", "an dem Hotel", "in das Hotel"], exp: "'das Hotel' ở Dativ sau giới từ 'vor' đổi thành 'vor dem Hotel'.", trans: "Chiếc taxi đợi phía trước khách sạn." }
        ];
        const p = posItems[Math.floor(Math.random() * posItems.length)];
        ex.question = `[Vị trí Dativ (Random)]: Chọn đáp án đúng chỉ vị trí: '${p.item} ${p.verb} ___.'`;
        ex.correct_answer = `${p.prep} ${p.target}`;
        ex.explanation = p.exp;
        extra.translation = p.trans;
        const opts = [`${p.prep} ${p.target}`, ...p.wrong];
        const shuffled = opts.sort(() => Math.random() - 0.5);
        ex.options = shuffled;
        ex.options_json = JSON.stringify(shuffled);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 22. Xử lý câu hỏi Nghề nghiệp, Hoạt động & Nơi làm việc (dynamic_profession_quiz - Bài 7)
    if (extra.dynamic_profession_quiz) {
        const subjects = [
            { name: "Herr Weber", gender: "m", vi: "Ông Weber", pronoun: "er" },
            { name: "Frau Lindner", gender: "f", vi: "Bà Lindner", pronoun: "sie" },
            { name: "Mein Bruder", gender: "m", vi: "Anh trai tôi", pronoun: "er" },
            { name: "Meine Schwester", gender: "f", vi: "Chị gái tôi", pronoun: "sie" },
            { name: "Lukas", gender: "m", vi: "Lukas", pronoun: "er" },
            { name: "Anna", gender: "f", vi: "Anna", pronoun: "sie" },
            { name: "Herr Schmidt", gender: "m", vi: "Ông Schmidt", pronoun: "er" },
            { name: "Frau Wagner", gender: "f", vi: "Bà Wagner", pronoun: "sie" }
        ];
        const professionData = [
            { m: "KFZ-Mechatroniker", f: "KFZ-Mechatronikerin", verb: "repariert Autos", workplace: "in einer Werkstatt", wrongWorkplaces: ["im Friseursalon", "im Krankenhaus", "im Supermarkt"], viProfM: "thợ cơ khí ô tô", viProfF: "nữ thợ cơ khí ô tô", viAct: "sửa xe hơi", viWp: "trong xưởng sửa chữa" },
            { m: "Arzt", f: "Ärztin", verb: "untersucht Patienten", workplace: "im Krankenhaus", wrongWorkplaces: ["in einer Werkstatt", "im Blumengeschäft", "an einer Schule"], viProfM: "bác sĩ nam", viProfF: "nữ bác sĩ", viAct: "khám cho bệnh nhân", viWp: "trong bệnh viện" },
            { m: "Florist", f: "Floristin", verb: "verkauft schöne Blumen", workplace: "im Blumengeschäft", wrongWorkplaces: ["im Friseursalon", "im Krankenhaus", "in einer Werkstatt"], viProfM: "người bán hoa", viProfF: "nữ người bán hoa", viAct: "bán những bông hoa đẹp", viWp: "trong cửa hàng hoa" },
            { m: "Friseur", f: "Friseurin", verb: "schneidet Haare", workplace: "im Friseursalon", wrongWorkplaces: ["in einer IT-Firma", "im Supermarkt", "im Krankenhaus"], viProfM: "thợ làm tóc", viProfF: "nữ thợ làm tóc", viAct: "cắt tóc", viWp: "trong tiệm làm tóc" },
            { m: "Programmierer", f: "Programmiererin", verb: "schreibt Computerprogramme", workplace: "im Büro", wrongWorkplaces: ["im Restaurant", "in einer Werkstatt", "im Blumengeschäft"], viProfM: "lập trình viên nam", viProfF: "nữ lập trình viên", viAct: "viết chương trình máy tính", viWp: "trong văn phòng" },
            { m: "Lehrer", f: "Lehrerin", verb: "unterrichtet Schüler", workplace: "an einer Schule", wrongWorkplaces: ["im Friseursalon", "in einer Werkstatt", "im Schuhgeschäft"], viProfM: "thầy giáo", viProfF: "cô giáo", viAct: "giảng dạy học sinh", viWp: "tại một trường học" },
            { m: "Koch", f: "Köchin", verb: "kocht leckere Speisen", workplace: "im Restaurant", wrongWorkplaces: ["im Büro", "an einer Schule", "im Blumengeschäft"], viProfM: "đầu bếp nam", viProfF: "nữ đầu bếp", viAct: "nấu những món ăn ngon", viWp: "trong nhà hàng" },
            { m: "Verkäufer", f: "Verkäuferin", verb: "verkauft Schuhe", workplace: "im Schuhgeschäft", wrongWorkplaces: ["im Krankenhaus", "in einer Werkstatt", "an einer Schule"], viProfM: "nam nhân viên bán hàng", viProfF: "nữ nhân viên bán hàng", viAct: "bán giày", viWp: "trong tiệm giày" }
        ];

        const s = subjects[Math.floor(Math.random() * subjects.length)];
        const p = professionData[Math.floor(Math.random() * professionData.length)];
        const targetProf = (s.gender === "m") ? p.m : p.f;
        const viProf = (s.gender === "m") ? p.viProfM : p.viProfF;

        const isWorkplaceQuestion = Math.random() > 0.5;
        if (isWorkplaceQuestion) {
            ex.question = `[Nghề nghiệp & Nơi làm việc (Random)]: Chọn cụm nơi làm việc đúng ở Dativ: '${s.name} arbeitet als ${targetProf} ___.'`;
            ex.correct_answer = p.workplace;
            ex.explanation = `Nghề nghiệp '${targetProf}' làm việc ở '${p.workplace}' (câu hỏi Wo? + Cách 3 Dativ).`;
            extra.translation = `${s.vi} làm việc với tư cách là ${viProf} ${p.viWp}.`;
            const opts = [p.workplace, ...p.wrongWorkplaces].sort(() => Math.random() - 0.5);
            ex.options = opts;
            ex.options_json = JSON.stringify(opts);
        } else {
            ex.question = `[Nghề nghiệp & Hoạt động (Random)]: Chọn hoạt động đúng với nghề nghiệp: 'Als ${targetProf} ___ ${s.name} jeden Tag.'`;
            ex.correct_answer = p.verb;
            ex.explanation = `Hoạt động đặc trưng của '${targetProf}' là '${p.verb}'.`;
            extra.translation = `Với tư cách là ${viProf}, ${s.vi} ${p.viAct} mỗi ngày.`;
            const otherVerbs = professionData.filter(x => x !== p).map(x => x.verb).slice(0, 3);
            const opts = [p.verb, ...otherVerbs].sort(() => Math.random() - 0.5);
            ex.options = opts;
            ex.options_json = JSON.stringify(opts);
        }
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 23. Xử lý câu hỏi Lịch trình & Modalverben Satzklammer (dynamic_modalverb_schedule_quiz - Bài 7)
    if (extra.dynamic_modalverb_schedule_quiz) {
        const characters = [
            { name: "Paula", pronoun: "sie", verbMuss: "muss", verbKann: "kann", vi: "Paula" },
            { name: "Frank", pronoun: "er", verbMuss: "muss", verbKann: "kann", vi: "Frank" },
            { name: "Mein Bruder", pronoun: "er", verbMuss: "muss", verbKann: "kann", vi: "Anh trai tôi" },
            { name: "Meine Schwester", pronoun: "sie", verbMuss: "muss", verbKann: "kann", vi: "Chị gái tôi" },
            { name: "Wir", pronoun: "wir", verbMuss: "müssen", verbKann: "können", vi: "Chúng tôi" },
            { name: "Ihr", pronoun: "ihr", verbMuss: "müsst", verbKann: "könnt", vi: "Các bạn" }
        ];
        const scheduleTasks = [
            { time: "Um 6.15 Uhr", modal: "müssen", infinitive: "aufstehen", viAction: "thức dậy", exp: "Động từ tách 'aufstehen' giữ nguyên mẫu ở cuối câu khi đi với Modalverb." },
            { time: "Um 7.15 Uhr", modal: "müssen", infinitive: "mit dem Bus zur Arbeit fahren", viAction: "đi xe buýt đến chỗ làm", exp: "Động từ 'fahren' đứng nguyên mẫu ở cuối khung câu Satzklammer." },
            { time: "Um 8.30 Uhr", modal: "müssen", infinitive: "die Tochter in den Kindergarten bringen", viAction: "đưa con gái vào trường mẫu giáo", exp: "Động từ 'bringen' (Wohin? in den Kindergarten) đứng nguyên mẫu ở cuối câu." },
            { time: "Um 16.30 Uhr", modal: "müssen", infinitive: "die Tochter vom Kindergarten abholen", viAction: "đón con gái từ trường mẫu giáo", exp: "Động từ tách 'abholen' không tách mà giữ nguyên mẫu ở cuối câu khi có Modalverb." },
            { time: "Von 20 bis 22 Uhr", modal: "können", infinitive: "im Wohnzimmer fernsehen", viAction: "xem tivi trong phòng khách", exp: "Động từ tách 'fernsehen' đứng nguyên mẫu ở cuối câu." },
            { time: "Am Sonntag", modal: "können", infinitive: "bis 8 Uhr schlafen", viAction: "ngủ đến 8 giờ", exp: "Động từ 'schlafen' đứng nguyên mẫu ở cuối câu sau Modalverb können." }
        ];

        const char = characters[Math.floor(Math.random() * characters.length)];
        const task = scheduleTasks[Math.floor(Math.random() * scheduleTasks.length)];
        const modalForm = (task.modal === "müssen") ? char.verbMuss : char.verbKann;

        ex.question = `[Lịch trình & Modalverben (Random)]: Chọn dạng chia đúng của Modalverb '${task.modal}': '${task.time} ___ ${char.name} ${task.infinitive}.'`;
        ex.correct_answer = modalForm;
        ex.explanation = `Chủ ngữ '${char.name}' (${char.pronoun}) đi với dạng chia '${modalForm}'. ${task.exp}`;
        extra.translation = `${task.time} ${char.vi} ${(task.modal === "müssen") ? "phải" : "có thể"} ${task.viAction}.`;

        const wrongModals = (task.modal === "müssen") 
            ? ["musst", "müsst", "müssen", "muss"].filter(x => x !== modalForm).slice(0, 3)
            : ["kannst", "könnt", "können", "kann"].filter(x => x !== modalForm).slice(0, 3);

        const opts = [modalForm, ...wrongModals].sort(() => Math.random() - 0.5);
        ex.options = opts;
        ex.options_json = JSON.stringify(opts);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 24. Xử lý câu hỏi Phân biệt Akkusativ vs. Dativ (dynamic_akkdativ_kontrast_quiz - Bài 7)
    if (extra.dynamic_akkdativ_kontrast_quiz) {
        const contrastItems = [
            {
                type: "verb",
                sentence: "Die Ärztin untersucht ___ Patienten im Behandlungszimmer.",
                correct: "den",
                wrong: ["dem", "der", "des"],
                exp: "Động từ 'untersuchen' (khám bệnh) đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ): der Patient -> den Patienten.",
                trans: "Nữ bác sĩ khám cho người bệnh nhân ở trong phòng điều trị."
            },
            {
                type: "verb",
                sentence: "Der Krankenpfleger hilft ___ Arzt bei der Untersuchung.",
                correct: "dem",
                wrong: ["den", "der", "das"],
                exp: "Động từ 'helfen' (giúp đỡ) luôn đi với Cách 3 (Dativ): der Arzt -> dem Arzt.",
                trans: "Người nam điều dưỡng giúp đỡ bác sĩ trong ca khám bệnh."
            },
            {
                type: "verb",
                sentence: "Bei ihrer Arbeit braucht Petra ___ Computer und einen Schreibtisch.",
                correct: "einen",
                wrong: ["einem", "ein", "einer"],
                exp: "Động từ 'brauchen' đi với Cách 4 (Akkusativ): der Computer -> einen Computer.",
                trans: "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc."
            },
            {
                type: "wohin_wo",
                sentence: "Um 8.30 Uhr bringt Frank seine Tochter in ___ Kindergarten.",
                correct: "den",
                wrong: ["dem", "der", "das"],
                exp: "Hành động đưa con đến trường mẫu giáo trả lời câu hỏi Wohin? (hướng di chuyển) -> Cách 4 Akkusativ: in den Kindergarten.",
                trans: "Lúc 8 giờ 30 phút Frank đưa con gái mình vào trường mẫu giáo."
            },
            {
                type: "wohin_wo",
                sentence: "Von 9 bis 15 Uhr spielt das Kind ___ Kindergarten.",
                correct: "im",
                wrong: ["in den", "ins", "an dem"],
                exp: "Chơi ở trong trường mẫu giáo trả lời câu hỏi Wo? (vị trí tĩnh) -> Cách 3 Dativ: in + dem = im Kindergarten.",
                trans: "Từ 9 đến 15 giờ đứa bé chơi ở trong trường mẫu giáo."
            },
            {
                type: "wohin_wo",
                sentence: "Herr Müller bringt das Auto in ___ Werkstatt.",
                correct: "die",
                wrong: ["der", "dem", "den"],
                exp: "Mang xe vào xưởng (Wohin? di chuyển) -> Cách 4 Akkusativ với giống cái 'die Werkstatt': in die Werkstatt.",
                trans: "Ông Müller mang chiếc xe vào xưởng sửa chữa."
            },
            {
                type: "wohin_wo",
                sentence: "Der Mechaniker repariert das Auto in ___ Werkstatt.",
                correct: "der",
                wrong: ["die", "dem", "den"],
                exp: "Sửa xe trong xưởng (Wo? vị trí tĩnh) -> Cách 3 Dativ với giống cái 'die Werkstatt': in der Werkstatt.",
                trans: "Người thợ sửa xe ở trong xưởng sửa chữa."
            },
            {
                type: "prep",
                sentence: "Das moderne Smartphone ist sehr wichtig für ___ Chef.",
                correct: "den",
                wrong: ["dem", "der", "des"],
                exp: "Giới từ 'für' luôn đi với Cách 4 (Akkusativ): der Chef -> den Chef.",
                trans: "Chiếc điện thoại thông minh hiện đại rất quan trọng đối với ông sếp."
            },
            {
                type: "prep",
                sentence: "Paula fährt jeden Morgen mit ___ Bus zur Arbeit.",
                correct: "dem",
                wrong: ["den", "der", "das"],
                exp: "Giới từ 'mit' luôn đi với Cách 3 (Dativ): der Bus -> dem Bus.",
                trans: "Paula đi làm mỗi buổi sáng bằng xe buýt."
            }
        ];

        const item = contrastItems[Math.floor(Math.random() * contrastItems.length)];
        ex.question = `[Akkusativ vs. Dativ (Random)]: Chọn từ thích hợp điền vào chỗ trống: '${item.sentence}'`;
        ex.correct_answer = item.correct;
        ex.explanation = item.exp;
        extra.translation = item.trans;

        const opts = [item.correct, ...item.wrong].sort(() => Math.random() - 0.5);
        ex.options = opts;
        ex.options_json = JSON.stringify(opts);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    // 25. Xử lý câu hỏi Mạo từ sở hữu Akkusativ 9 ngôi (dynamic_possessivartikel_akkusativ_quiz - Bài 7)
    if (extra.dynamic_possessivartikel_akkusativ_quiz) {
        const persons = [
            { pronoun: "ich", stem: "mein", vi: "tôi" },
            { pronoun: "du", stem: "dein", vi: "bạn" },
            { pronoun: "er", stem: "sein", vi: "anh ấy" },
            { pronoun: "sie", stem: "ihr", vi: "cô ấy" },
            { pronoun: "wir", stem: "unser", vi: "chúng tôi" },
            { pronoun: "ihr", stem: "euer", vi: "các bạn" },
            { pronoun: "Sie", stem: "Ihr", vi: "Ngài" }
        ];
        const objects = [
            { word: "Computer", gender: "m", ending: "en", vi: "chiếc máy tính" },
            { word: "Laptop", gender: "m", ending: "en", vi: "chiếc laptop" },
            { word: "Chef", gender: "m", ending: "en", vi: "ông sếp" },
            { word: "Tochter", gender: "f", ending: "e", vi: "con gái" },
            { word: "Kunden", gender: "pl", ending: "e", vi: "các khách hàng" },
            { word: "Auto", gender: "n", ending: "", vi: "chiếc ô tô" }
        ];

        const p = persons[Math.floor(Math.random() * persons.length)];
        const o = objects[Math.floor(Math.random() * objects.length)];

        let correct = "";
        if (p.pronoun === "ihr") {
            if (o.ending === "en") correct = "euren";
            else if (o.ending === "e") correct = "eure";
            else correct = "euer";
        } else {
            correct = p.stem + o.ending;
        }

        ex.question = `[Sở hữu Akkusativ (Random)]: Điền mạo từ sở hữu của ngôi '${p.pronoun}' ở Cách 4 (Akkusativ) trước danh từ '${o.word}': 'Brauchst du ___ ${o.word}?'`;
        ex.correct_answer = correct;
        ex.explanation = `Ngôi '${p.pronoun}' có gốc '${p.stem}-'. Với danh từ '${o.word}' ở Akkusativ, đuôi biến đổi tương ứng là '${correct}'.`;
        extra.translation = `Bạn có cần ${o.vi} của ${p.vi} không?`;

        const wrongVariants = [p.stem, p.stem + "em", p.stem + "er", p.stem + "es"].filter(x => x !== correct);
        const opts = [correct, ...wrongVariants].slice(0, 4).sort(() => Math.random() - 0.5);
        ex.options = opts;
        ex.options_json = JSON.stringify(opts);
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
        return finalize(ex);
    }

    if (!extra.dynamic_number && !extra.dynamic_mode) return finalize(ex);

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
        ex.question = `[Random Đọc Số]: Cách viết tiếng Đức chính xác của số ${num} là gì?`;
        ex.options = options;
        ex.options_json = JSON.stringify(options);
        ex.correct_answer = correct;
        ex.explanation = `Số ${num} được ghép từ hàng đơn vị + und + hàng chục: ${correct}.`;
        extra.translation = `Số ${num}: ${correct}`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
    }
    else if (mode === 'de_to_num') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        ex.question = `[Đức → Số (Random)]: Chuyển chữ số tiếng Đức sau thành số tự nhiên: '${german}'`;
        ex.correct_answer = String(num);
        ex.explanation = `'${german}' biểu thị con số tự nhiên ${num}.`;
        extra.translation = `Số ${num}: ${german}`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
    }
    else if (mode === 'listen_num') {
        const num = getRandomInt(min, max);
        const german = numberToGerman(num);
        extra.audio_text = german;
        extra.translation = `Số ${num}: ${german}`;
        ex.extra_data = JSON.stringify(extra);
        ex.correct_answer = String(num);
        ex.explanation = `Âm thanh phát âm: '${german}' → Đáp án là số ${num}.`;
        ex.translation = extra.translation;
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
        extra.translation = `Số ${num}: ${german}`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
    }
    else if (mode === 'tens_to_de') {
        const tensList = [20, 30, 40, 50, 60, 70, 80, 90];
        const num = tensList[Math.floor(Math.random() * tensList.length)];
        const german = numberToGerman(num);
        ex.question = `[Viết số tròn chục (Random)]: Hãy viết số ${num} bằng chữ tiếng Đức:`;
        ex.correct_answer = german;
        ex.explanation = `Số tròn chục ${num} được viết là: ${german}${num === 30 ? ' (chú ý chữ ß)' : ''}.`;
        extra.translation = `Số ${num}: ${german}`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
    }
    else if (mode === 'special_3digit_to_de') {
        const specials = [912, 815, 716, 617, 511, 418, 319, 212, 116, 707, 808, 909];
        const num = specials[Math.floor(Math.random() * specials.length)];
        const german = numberToGerman(num);
        ex.question = `[Viết số 3 chữ số đặc biệt (Random)]: Hãy viết số ${num} bằng chữ tiếng Đức (viết liền không dấu cách):`;
        ex.correct_answer = german;
        ex.explanation = `Số ${num} viết bằng chữ tiếng Đức là: ${german}.`;
        extra.translation = `Số ${num}: ${german}`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
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
        extra.translation = `Số ${n1} (${de1}) và số ${n2} (${de2})`;
        ex.extra_data = JSON.stringify(extra);
        ex.translation = extra.translation;
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

    return finalize(ex);
}

/**
 * Đổi toàn bộ các câu hỏi số đếm trong danh sách bài tập hiện tại
 */
function randomizeAllNumberExercises(exercisesList) {
    if (!exercisesList || !Array.isArray(exercisesList)) return;
    exercisesList.forEach((ex, idx) => {
        let isDynamic = false;
        try {
            const extra = typeof ex.extra_data === 'string' ? JSON.parse(ex.extra_data) : (ex.extra_data || {});
            if (extra.dynamic_number || extra.dynamic_mode || extra.dynamic_price || extra.dynamic_conjugation || extra.dynamic_article_quiz || extra.dynamic_possessive_article || extra.dynamic_plural_quiz || extra.dynamic_direction_quiz || extra.dynamic_landmark_quiz || extra.dynamic_praeteritum_quiz || extra.dynamic_country_language_quiz || extra.dynamic_question_transform || extra.dynamic_nom_akk_quiz || extra.dynamic_possessiv_quiz || extra.dynamic_adjective_antonym_quiz || extra.dynamic_pronoun_replacement_quiz || extra.dynamic_house_translation_quiz || extra.dynamic_prep_quiz || extra.dynamic_time_quiz || extra.dynamic_trennbare_quiz || extra.dynamic_dativ_transport_quiz || extra.dynamic_ordinal_date_quiz || extra.dynamic_dativ_position_quiz) isDynamic = true;
        } catch (e) {}

        if (isDynamic) {
            generateNewNumberData(ex, idx + 1);
        }
    });
}

if (typeof window !== 'undefined') {
    window.ensureQuestionNumber = ensureQuestionNumber;
    window.numberToGerman = numberToGerman;
    window.priceToGerman = priceToGerman;
    window.getRandomInt = getRandomInt;
    window.checkGermanAnswerEquivalence = checkGermanAnswerEquivalence;
    window.evaluateLesson8Translation = evaluateLesson8Translation;
    window.evaluateLesson8VDTranslation = evaluateLesson8VDTranslation;
    window.generateNewNumberData = generateNewNumberData;
    window.randomizeAllNumberExercises = randomizeAllNumberExercises;
}
