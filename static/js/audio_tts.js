/**
 * DeutschMeister - Hệ thống phát âm chuẩn tiếng Đức (TTS Engine)
 * Tối ưu hóa đặc biệt cho Safari / macOS / iOS / Chrome
 * Tự động khóa giọng bản xứ de-DE & bảng ánh xạ từ vựng dễ phát âm nhầm
 */

const GERMAN_PRONUNCIATION_MAP = {
    // Chữ cái đơn trong bảng chữ cái
    "A": "A", "B": "Be", "C": "Ce", "D": "De", "E": "E", "F": "Ef",
    "G": "Ge", "H": "Ha", "I": "I", "J": "Jot", "K": "Ka", "L": "El",
    "M": "Em", "N": "En", "O": "O", "P": "Pe", "Q": "Ku", "R": "Er",
    "S": "Es", "T": "Te", "U": "U", "V": "Vau", "W": "We", "X": "Iks",
    "Y": "Üpsilon", "Z": "Zett", "Ä": "Ä", "Ö": "Ö", "Ü": "Ü", "ß": "Eszett",
    // Các từ ngắn dễ bị trình duyệt nhận diện nhầm sang tiếng Anh
    "die": "die.",
    "der": "der.",
    "das": "das.",
    "Tschüss": "Tschüüs!",
    "Tschüss!": "Tschüüs!",
    "Hi": "Hi!",
    "das Bier": "das Bier.",
    "das Tier": "das Tier.",
    "das Tor": "das Tor.",
    "das Rad": "das Rad.",
    "das Spiel": "das Spiel.",
    "die Tür": "die Tür.",
    "die Küche": "die Küche.",
    // Từ vựng Bài 1 (P2): Gọi đồ uống, giá tiền & chia động từ
    "Café": "Café",
    "Kakao": "Kakao.",
    "Euro": "Euro.",
    "Cent": "Cent.",
    "möchte": "möchte.",
    "möchten": "möchten.",
    "liest": "liest.",
    "nimmt": "nimmt.",
    "heißt": "heißt.",
    "zahlen": "zahlen.",
    "Kaffee": "Kaffee.",
    "Tee": "Tee.",
    "Milch": "Milch.",
    "Zucker": "Zucker.",
    "getrennt": "getrennt.",
    "zusammen": "zusammen.",
    // Từ vựng Bài 2: Đồ dùng lớp học & Giống der/die/das
    "ein": "ein.",
    "eine": "eine.",
    "kein": "kein.",
    "keine": "keine.",
    "Kuli": "Kuli.",
    "Brille": "Brille.",
    "Wörterbuch": "Wörterbuch.",
    "Handy": "Händy.",
    "Stühle": "Stühle.",
    "Bücher": "Bücher.",
    "Brötchen": "Brötchen.",
    "buchstabieren": "buchstabieren.",
    "wiederholen": "wiederholen.",
    "verstehen": "verstehen.",
    "anschreiben": "anschreiben.",
    // Từ vựng Bài 3: Địa danh, Phương hướng & Präteritum
    "Österreich": "Österreich.",
    "Griechenland": "Griechenland.",
    "Tschechien": "Tschechien.",
    "Frankreich": "Frankreich.",
    "Großbritannien": "Großbritannien.",
    "Spanien": "Spanien.",
    "Italien": "Italien.",
    "Russland": "Russland.",
    "Polen": "Polen.",
    "Schweiz": "Schweiz.",
    "Türkei": "Türkei.",
    "Slowakei": "Slowakei.",
    "Iran": "Iran.",
    "USA": "USA.",
    "Niederlande": "Niederlande.",
    "Französisch": "Französisch.",
    "Griechisch": "Griechisch.",
    "Italienisch": "Italienisch.",
    "Spanisch": "Spanisch.",
    "Russisch": "Russisch.",
    "Polnisch": "Polnisch.",
    "Tschechisch": "Tschechisch.",
    "Persisch": "Persisch.",
    "Türkisch": "Türkisch.",
    "Sehenswürdigkeiten": "Sehenswürdigkeiten.",
    "Sehenswürdigkeit": "Sehenswürdigkeit.",
    "Eiffelturm": "Eiffelturm.",
    "Akropolis": "Akropolis.",
    "Big Ben": "Big Ben.",
    "Schiefe Turm": "Schiefe Turm.",
    "Prater": "Prater.",
    "Brandenburger Tor": "Brandenburger Tor.",
    "Rote Platz": "Rote Platz.",
    "Norden": "Norden.",
    "Süden": "Süden.",
    "Osten": "Osten.",
    "Westen": "Westen.",
    "Nordosten": "Nordosten.",
    "Südosten": "Südosten.",
    "Nordwesten": "Nordwesten.",
    "Südwesten": "Südwesten.",
    "Mitte": "Mitte.",
    "nördlich": "nördlich.",
    "südlich": "südlich.",
    "östlich": "östlich.",
    "westlich": "westlich.",
    "nordöstlich": "nordöstlich.",
    "südöstlich": "südöstlich.",
    "nordwestlich": "nordwestlich.",
    "südwestlich": "südwestlich.",
    "Präteritum": "Präteritum.",
    "gestern": "gestern.",
    "vorgestern": "vorgestern.",
    "heute": "heute.",
    "war": "war.",
    "warst": "warst.",
    "waren": "waren.",
    "wart": "wart.",
    "hatte": "hatte.",
    "hattest": "hattest.",
    "hatten": "hatten.",
    "hattet": "hattet."
};

let bestGermanVoice = null;
let isVoicesLoaded = false;

function getBestGermanVoice() {
    if (!('speechSynthesis' in window)) return null;
    const voices = window.speechSynthesis.getVoices();
    if (!voices || voices.length === 0) return null;

    // Lọc các giọng có ngôn ngữ de-DE hoặc tiếng Đức
    const deVoices = voices.filter(v => {
        const lang = (v.lang || '').toLowerCase().replace('_', '-');
        return lang === 'de-de' || lang.startsWith('de');
    });

    if (deVoices.length === 0) return null;

    // Thứ tự ưu tiên các giọng Đức chất lượng cao (macOS/iOS: Anna, Helena, Petra, Markus; Google Deutsch, Katja)
    const preferredNames = [
        'Anna', 'Helena', 'Petra', 'Markus', 'Yannick',
        'Google Deutsch', 'Microsoft Katja', 'Hedda', 'Stefan', 'Martin'
    ];

    for (const name of preferredNames) {
        const found = deVoices.find(v => v.name && v.name.toLowerCase().includes(name.toLowerCase()));
        if (found) {
            bestGermanVoice = found;
            return bestGermanVoice;
        }
    }

    bestGermanVoice = deVoices[0];
    return bestGermanVoice;
}

// Khởi tạo và lắng nghe sự kiện nạp danh sách giọng của trình duyệt
if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
        bestGermanVoice = getBestGermanVoice();
        isVoicesLoaded = true;
    };
    // Gọi ngay lần đầu
    bestGermanVoice = getBestGermanVoice();
}

/**
 * Hàm phát âm chuẩn tiếng Đức với khóa giọng de-DE và cơ chế dự phòng
 * @param {string} rawText Chuỗi tiếng Đức cần phát âm
 * @param {number} rate Tốc độ đọc (mặc định 0.9 cho chuẩn âm)
 */
function speakGerman(rawText, rate = 0.9) {
    if (!rawText) return;
    const textTrimmed = String(rawText).trim();

    // 1. Chuẩn hóa qua từ điển GERMAN_PRONUNCIATION_MAP
    let textToSpeak = GERMAN_PRONUNCIATION_MAP[textTrimmed] || textTrimmed;

    // Thêm dấu câu nếu là từ ngắn để macOS Safari không nuốt âm
    if (!/[.!?]$/.test(textToSpeak) && textToSpeak.length <= 15) {
        textToSpeak += '.';
    }

    // 2. Phát âm bằng Web Speech API nếu khả dụng
    if ('speechSynthesis' in window) {
        try {
            window.speechSynthesis.cancel(); // Dừng câu trước đó nếu đang đọc

            const utterance = new SpeechSynthesisUtterance(textToSpeak);
            utterance.lang = 'de-DE';
            utterance.rate = rate || 0.9;
            utterance.pitch = 1.0;

            const voice = bestGermanVoice || getBestGermanVoice();
            if (voice) {
                utterance.voice = voice;
            }

            let played = false;
            utterance.onstart = () => { played = true; };
            utterance.onerror = (e) => {
                console.warn('SpeechSynthesis error, falling back to /api/tts:', e);
                playFallbackAudio(textTrimmed);
            };

            window.speechSynthesis.speak(utterance);
            return;
        } catch (err) {
            console.warn('SpeechSynthesis exception:', err);
        }
    }

    // 3. Fallback: Nếu trình duyệt không hỗ trợ hoặc không có giọng Đức
    playFallbackAudio(textTrimmed);
}

/**
 * Phát âm thanh dự phòng qua endpoint Google German TTS trên máy chủ Flask
 */
function playFallbackAudio(text) {
    try {
        const audio = new Audio('/api/tts?text=' + encodeURIComponent(text));
        audio.play().catch(e => {
            console.warn('Fallback audio playback was blocked or failed:', e);
        });
    } catch (e) {
        console.error('Lỗi khi phát audio dự phòng:', e);
    }
}

if (typeof window !== 'undefined') {
    window.speakGerman = speakGerman;
    window.getBestGermanVoice = getBestGermanVoice;
    window.playFallbackAudio = playFallbackAudio;
    window.GERMAN_PRONUNCIATION_MAP = GERMAN_PRONUNCIATION_MAP;
}
