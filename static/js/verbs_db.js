/**
 * DeutschMeister - CSDL Động từ tiếng Đức & Công cụ Tra cứu Chia động từ (Verb-Konjugator)
 * Chuẩn CEFR A1 - A2 với 35 động từ cốt lõi, phân nhóm quy tắc, highlight biến âm & giọng đọc bản xứ de-DE
 */

const GERMAN_VERBS_DB = [
    {
        infinitiv: "sein",
        meaning: "thì, là, ở",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "sei-",
        ending: "-n",
        forms: { ich: "bin", du: "bist", er_sie_es: "ist", wir: "sind", ihr: "seid", sie_Sie: "sind" },
        praeteritum: { ich: "war", du: "warst", er_sie_es: "war", wir: "waren", ihr: "wart", sie_Sie: "waren" },
        note: "Động từ bất quy tắc quan trọng nhất trong tiếng Đức, biến đổi hoàn toàn ở tất cả các ngôi ở cả Hiện tại (Präsens) và Quá khứ đơn (Präteritum).",
        example: "Ich bin im Deutschkurs. Gestern waren wir in Haiphong."
    },
    {
        infinitiv: "haben",
        meaning: "có, sở hữu",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "hab-",
        ending: "-en",
        forms: { ich: "habe", du: "hast", er_sie_es: "hat", wir: "haben", ihr: "habt", sie_Sie: "haben" },
        praeteritum: { ich: "hatte", du: "hattest", er_sie_es: "hatte", wir: "hatten", ihr: "hattet", sie_Sie: "hatten" },
        note: "Ngôi du và er/sie/es lược bỏ phụ âm -b- ở gốc (hast, hat). Quá khứ đơn dùng gốc hatt- (hatte, hattest).",
        example: "Ich habe Zeit. Gestern hatte ich keinen Deutschunterricht."
    },
    {
        infinitiv: "machen",
        meaning: "làm, thực hiện (Das macht... = Tổng cộng hết...)",
        group: "Quy tắc (Regelmäßig)",
        stem: "mach-",
        ending: "-en",
        forms: { ich: "mache", du: "machst", er_sie_es: "macht", wir: "machen", ihr: "macht", sie_Sie: "machen" },
        note: "Chia theo đúng công thức chuẩn: -e, -st, -t, -en, -t, -en.",
        example: "Das macht 3,99 Euro."
    },
    {
        infinitiv: "wohnen",
        meaning: "sống, cư trú",
        group: "Quy tắc (Regelmäßig)",
        stem: "wohn-",
        ending: "-en",
        forms: { ich: "wohne", du: "wohnst", er_sie_es: "wohnt", wir: "wohnen", ihr: "wohnt", sie_Sie: "wohnen" },
        note: "Thường đi với giới từ 'in' (wohnen in Berlin).",
        example: "Und wo wohnt ihr? Wir wohnen in Berlin."
    },
    {
        infinitiv: "kommen",
        meaning: "đến, xuất thân",
        group: "Quy tắc (Regelmäßig)",
        stem: "komm-",
        ending: "-en",
        forms: { ich: "komme", du: "kommst", er_sie_es: "kommt", wir: "kommen", ihr: "kommt", sie_Sie: "kommen" },
        note: "Thường đi với giới từ 'aus' chỉ quê quán nguồn gốc (kommen aus Vietnam).",
        example: "Mein Freund kommt aus Russland."
    },
    {
        infinitiv: "trinken",
        meaning: "uống",
        group: "Quy tắc (Regelmäßig)",
        stem: "trink-",
        ending: "-en",
        forms: { ich: "trinke", du: "trinkst", er_sie_es: "trinkt", wir: "trinken", ihr: "trinkt", sie_Sie: "trinken" },
        note: "Động từ có quy tắc thông dụng khi gọi đồ uống tại quán cà phê/nhà hàng.",
        example: "Ich trinke Kaffee mit viel Milch."
    },
    {
        infinitiv: "zahlen",
        meaning: "thanh toán, trả tiền",
        group: "Quy tắc (Regelmäßig)",
        stem: "zahl-",
        ending: "-en",
        forms: { ich: "zahle", du: "zahlst", er_sie_es: "zahlt", wir: "zahlen", ihr: "zahlt", sie_Sie: "zahlen" },
        note: "Động từ có quy tắc, thường đi cùng möchten: 'Wir möchten bitte zahlen.'",
        example: "Wir möchten bitte zahlen. Zusammen oder getrennt?"
    },
    {
        infinitiv: "lernen",
        meaning: "học, học tập",
        group: "Quy tắc (Regelmäßig)",
        stem: "lern-",
        ending: "-en",
        forms: { ich: "lerne", du: "lernst", er_sie_es: "lernt", wir: "lernen", ihr: "lernt", sie_Sie: "lernen" },
        note: "Quy tắc chuẩn hoàn toàn.",
        example: "Wir lernen Deutsch mit DeutschMeister."
    },
    {
        infinitiv: "hören",
        meaning: "nghe, lắng nghe",
        group: "Quy tắc (Regelmäßig)",
        stem: "hör-",
        ending: "-en",
        forms: { ich: "höre", du: "hörst", er_sie_es: "hört", wir: "hören", ihr: "hört", sie_Sie: "hören" },
        note: "Giữ nguyên nguyên âm Umlaut ö ở mọi ngôi khi chia.",
        example: "Ich höre gern Musik."
    },
    {
        infinitiv: "spielen",
        meaning: "chơi (thể thao, nhạc cụ, trò chơi)",
        group: "Quy tắc (Regelmäßig)",
        stem: "spiel-",
        ending: "-en",
        forms: { ich: "spiele", du: "spielst", er_sie_es: "spielt", wir: "spielen", ihr: "spielt", sie_Sie: "spielen" },
        note: "Quy tắc chuẩn hoàn toàn.",
        example: "Er spielt Fußball."
    },
    {
        infinitiv: "kaufen",
        meaning: "mua sắm",
        group: "Quy tắc (Regelmäßig)",
        stem: "kauf-",
        ending: "-en",
        forms: { ich: "kaufe", du: "kaufst", er_sie_es: "kauft", wir: "kaufen", ihr: "kauft", sie_Sie: "kaufen" },
        note: "Quy tắc chuẩn.",
        example: "Sie kauft Kaffee und Tee."
    },
    {
        infinitiv: "leben",
        meaning: "sống, sinh sống",
        group: "Quy tắc (Regelmäßig)",
        stem: "leb-",
        ending: "-en",
        forms: { ich: "lebe", du: "lebst", er_sie_es: "lebt", wir: "leben", ihr: "lebt", sie_Sie: "leben" },
        note: "Quy tắc chuẩn hoàn toàn.",
        example: "Meine Familie lebt in Vietnam."
    },
    {
        infinitiv: "fragen",
        meaning: "hỏi, đặt câu hỏi",
        group: "Quy tắc (Regelmäßig)",
        stem: "frag-",
        ending: "-en",
        forms: { ich: "frage", du: "fragst", er_sie_es: "fragt", wir: "fragen", ihr: "fragt", sie_Sie: "fragen" },
        note: "Quy tắc chuẩn.",
        example: "Der Kellner fragt: Was möchten Sie trinken?"
    },
    {
        infinitiv: "sagen",
        meaning: "nói, bảo",
        group: "Quy tắc (Regelmäßig)",
        stem: "sag-",
        ending: "-en",
        forms: { ich: "sage", du: "sagst", er_sie_es: "sagt", wir: "sagen", ihr: "sagt", sie_Sie: "sagen" },
        note: "Quy tắc chuẩn.",
        example: "Was sagt der Lehrer?"
    },
    {
        infinitiv: "heißen",
        meaning: "tên là, gọi là",
        group: "Gốc kết thúc bằng -s, -ß, -z",
        stem: "heiß-",
        ending: "-en",
        forms: { ich: "heiße", du: "heißt", er_sie_es: "heißt", wir: "heißen", ihr: "heißt", sie_Sie: "heißen" },
        note: "Gốc kết thúc bằng -ß nên ngôi 'du' chỉ thêm -t (du heißt), viết giống hệt ngôi er/sie/es và ihr.",
        example: "Guten Tag, wie heißen Sie? Ich heiße Dat."
    },
    {
        infinitiv: "tanzen",
        meaning: "khiêu vũ, nhảy múa",
        group: "Gốc kết thúc bằng -s, -ß, -z",
        stem: "tanz-",
        ending: "-en",
        forms: { ich: "tanze", du: "tanzt", er_sie_es: "tanzt", wir: "tanzen", ihr: "tanzt", sie_Sie: "tanzen" },
        note: "Gốc kết thúc bằng -z nên ngôi 'du' chỉ thêm -t (du tanzt).",
        example: "Tanzt du gern? Ja, ich tanze sehr gern."
    },
    {
        infinitiv: "reisen",
        meaning: "đi du lịch",
        group: "Gốc kết thúc bằng -s, -ß, -z",
        stem: "reis-",
        ending: "-en",
        forms: { ich: "reise", du: "reist", er_sie_es: "reist", wir: "reisen", ihr: "reist", sie_Sie: "reisen" },
        note: "Gốc kết thúc bằng -s nên ngôi 'du' chỉ thêm -t (du reist).",
        example: "Er reist nach Deutschland."
    },
    {
        infinitiv: "mieten",
        meaning: "thuê (nhà, căn hộ, xe)",
        group: "Gốc kết thúc bằng -t, -d",
        stem: "miet-",
        ending: "-en",
        forms: { ich: "miete", du: "mietest", er_sie_es: "mietet", wir: "mieten", ihr: "mietet", sie_Sie: "mieten" },
        note: "Gốc kết thúc bằng -t nên thêm -e- trước đuôi -st (du mietest) và -t (mietet) để phát âm dễ dàng.",
        example: "Er mietet eine Wohnung in München."
    },
    {
        infinitiv: "arbeiten",
        meaning: "làm việc",
        group: "Gốc kết thúc bằng -t, -d",
        stem: "arbeit-",
        ending: "-en",
        forms: { ich: "arbeite", du: "arbeitest", er_sie_es: "arbeitet", wir: "arbeiten", ihr: "arbeitet", sie_Sie: "arbeiten" },
        note: "Gốc kết thúc bằng -t nên thêm -e- ở ngôi du (arbeitest), er/sie/es (arbeitet) và ihr (arbeitet).",
        example: "Wo arbeitest du? Ich arbeite bei der Post."
    },
    {
        infinitiv: "antworten",
        meaning: "trả lời, hồi đáp",
        group: "Gốc kết thúc bằng -t, -d",
        stem: "antwort-",
        ending: "-en",
        forms: { ich: "antworte", du: "antwortest", er_sie_es: "antwortet", wir: "antworten", ihr: "antwortet", sie_Sie: "antworten" },
        note: "Gốc kết thúc bằng -t nên chèn thêm -e- ở ngôi du, er/sie/es và ihr.",
        example: "Er antwortet schnell auf die Frage."
    },
    {
        infinitiv: "finden",
        meaning: "tìm thấy; cảm thấy/đánh giá (+ Akkusativ + Tính từ)",
        group: "Gốc kết thúc bằng -t, -d",
        stem: "find-",
        ending: "-en",
        forms: { ich: "finde", du: "findest", er_sie_es: "findet", wir: "finden", ihr: "findet", sie_Sie: "finden" },
        note: "Gốc kết thúc bằng -d nên chèn thêm -e- ở ngôi du (findest) và er/sie/es (findet). Đi với tân ngữ Akkusativ (Cách 4): Ich finde den Garten sehr schön.",
        example: "Ich finde die Küche zu klein, aber den Garten sehr schön."
    },
    {
        infinitiv: "kosten",
        meaning: "có giá là, tốn bao nhiêu",
        group: "Gốc kết thúc bằng -t, -d",
        stem: "kost-",
        ending: "-en",
        forms: { ich: "koste", du: "kostest", er_sie_es: "kostet", wir: "kosten", ihr: "kostet", sie_Sie: "kosten" },
        note: "Gốc kết thúc bằng -t nên chèn thêm -e- (kostet). Thường dùng ở ngôi thứ 3 (es/das kostet).",
        example: "Wie viel kostet der Tee? Er kostet 2,99 Euro."
    },
    {
        infinitiv: "warten",
        meaning: "chờ đợi",
        group: "Gốc kết thúc bằng -t, -d",
        stem: "wart-",
        ending: "-en",
        forms: { ich: "warte", du: "wartest", er_sie_es: "wartet", wir: "warten", ihr: "wartet", sie_Sie: "warten" },
        note: "Gốc kết thúc bằng -t nên chèn thêm -e- (wartest, wartet).",
        example: "Wir warten auf den Kellner."
    },
    {
        infinitiv: "nehmen",
        meaning: "dùng, lấy, chọn (món ăn/đồ uống)",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "nehm-",
        ending: "-en",
        forms: { ich: "nehme", du: "nimmst", er_sie_es: "nimmt", wir: "nehmen", ihr: "nehmt", sie_Sie: "nehmen" },
        note: "Biến đổi gốc 'nehm-' thành 'nimm-' ở ngôi du (nimmst) và er/sie/es (nimmt). Ngôi ihr giữ nguyên (nehmt).",
        example: "Was nehmen Sie? Ich nehme Tee."
    },
    {
        infinitiv: "lesen",
        meaning: "đọc",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "les-",
        ending: "-en",
        forms: { ich: "lese", du: "liest", er_sie_es: "liest", wir: "lesen", ihr: "lest", sie_Sie: "lesen" },
        note: "Biến âm e -> ie ở ngôi du và er/sie/es. Vì gốc kết thúc bằng -s nên du và er/sie/es đều là 'liest'.",
        example: "Du liest ein Buch auf Deutsch."
    },
    {
        infinitiv: "sprechen",
        meaning: "nói chuyện, nói ngôn ngữ",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "sprech-",
        ending: "-en",
        forms: { ich: "spreche", du: "sprichst", er_sie_es: "spricht", wir: "sprechen", ihr: "sprecht", sie_Sie: "sprechen" },
        note: "Biến âm e -> i ở ngôi du (sprichst) và er/sie/es (spricht).",
        example: "Sprichst du Deutsch? Ja, ein bisschen."
    },
    {
        infinitiv: "sehen",
        meaning: "nhìn, xem",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "seh-",
        ending: "-en",
        forms: { ich: "sehe", du: "siehst", er_sie_es: "sieht", wir: "sehen", ihr: "seht", sie_Sie: "sehen" },
        note: "Biến âm e -> ie ở ngôi du (siehst) và er/sie/es (sieht).",
        example: "Siehst du das Café dort?"
    },
    {
        infinitiv: "essen",
        meaning: "ăn",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "ess-",
        ending: "-en",
        forms: { ich: "esse", du: "isst", er_sie_es: "isst", wir: "essen", ihr: "esst", sie_Sie: "essen" },
        note: "Biến âm e -> i ở ngôi du (isst) và er/sie/es (isst).",
        example: "Er isst ein Stück Kuchen."
    },
    {
        infinitiv: "geben",
        meaning: "cho, đưa (Es gibt = Có...)",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "geb-",
        ending: "-en",
        forms: { ich: "gebe", du: "gibst", er_sie_es: "gibt", wir: "geben", ihr: "gebt", sie_Sie: "geben" },
        note: "Biến âm e -> i ở ngôi du (gibst) và er/sie/es (gibt). Cụm 'Es gibt' nghĩa là 'có'.",
        example: "Es gibt hier guten Kaffee."
    },
    {
        infinitiv: "fahren",
        meaning: "lái xe, đi xe (tàu, buýt...)",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "fahr-",
        ending: "-en",
        forms: { ich: "fahre", du: "fährst", er_sie_es: "fährt", wir: "fahren", ihr: "fahrt", sie_Sie: "fahren" },
        note: "Biến âm a -> ä ở ngôi du (fährst) và er/sie/es (fährt). Ngôi ihr giữ nguyên (fahrt).",
        example: "Wir fahren nach Berlin."
    },
    {
        infinitiv: "schlafen",
        meaning: "ngủ",
        group: "Biến âm gốc (Vokalwechsel)",
        stem: "schlaf-",
        ending: "-en",
        forms: { ich: "schlafe", du: "schläfst", er_sie_es: "schläft", wir: "schlafen", ihr: "schlaft", sie_Sie: "schlafen" },
        note: "Biến âm a -> ä ở ngôi du (schläfst) và er/sie/es (schläft).",
        example: "Das Kind schläft gut."
    },
    {
        infinitiv: "möchten",
        meaning: "muốn (lịch sự, gọi món/yêu cầu)",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "möcht-",
        ending: "-en",
        forms: { ich: "möchte", du: "möchtest", er_sie_es: "möchte", wir: "möchten", ihr: "möchtet", sie_Sie: "möchten" },
        note: "Ngôi 'ich' và 'er/sie/es' chia giống hệt nhau (möchte - không có đuôi -t). Động từ chính đi kèm đẩy về cuối câu ở dạng nguyên mẫu.",
        example: "Was möchten Sie trinken? Wir möchten bitte zahlen."
    },
    {
        infinitiv: "können",
        meaning: "có thể, biết làm gì",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "könn-",
        ending: "-en",
        forms: { ich: "kann", du: "kannst", er_sie_es: "kann", wir: "können", ihr: "könnt", sie_Sie: "können" },
        note: "Động từ khuyết thiếu: ich và er/sie/es đều là 'kann' (bỏ Umlaut ö thành a, không có đuôi).",
        example: "Ich kann ein bisschen Deutsch sprechen."
    },
    {
        infinitiv: "müssen",
        meaning: "phải (bắt buộc)",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "müss-",
        ending: "-en",
        forms: { ich: "muss", du: "musst", er_sie_es: "muss", wir: "müssen", ihr: "müsst", sie_Sie: "müssen" },
        note: "Động từ khuyết thiếu: ich và er/sie/es đều là 'muss' (bỏ Umlaut ü thành u).",
        example: "Ich muss jetzt nach Hause gehen."
    },
    {
        infinitiv: "wollen",
        meaning: "muốn (ý chí chủ quan)",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "woll-",
        ending: "-en",
        forms: { ich: "will", du: "willst", er_sie_es: "will", wir: "wollen", ihr: "wollt", sie_Sie: "wollen" },
        note: "Động từ khuyết thiếu: ich và er/sie/es đều là 'will' (o đổi thành i).",
        example: "Wir wollen Deutsch lernen."
    },
    {
        infinitiv: "liegen",
        meaning: "nằm ở, tọa lạc ở (thành phố, địa danh trên bản đồ)",
        group: "Quy tắc (Regelmäßig)",
        stem: "lieg-",
        ending: "-en",
        forms: { ich: "liege", du: "liegst", er_sie_es: "liegt", wir: "liegen", ihr: "liegt", sie_Sie: "liegen" },
        praeteritum: { ich: "lag", du: "lagst", er_sie_es: "lag", wir: "lagen", ihr: "lagt", sie_Sie: "lagen" },
        note: "Đi với giới từ 'im + Phương hướng + von' hoặc 'Tính từ hướng (-lich) + von': Hanoi liegt im Norden von Vietnam.",
        example: "Hanoi liegt im Norden von Vietnam. Hai Phong liegt im Nordosten."
    },
    {
        infinitiv: "besuchen",
        meaning: "thăm, ghé thăm (địa danh, danh thắng, bạn bè)",
        group: "Quy tắc (Regelmäßig)",
        stem: "besuch-",
        ending: "-en",
        forms: { ich: "besuche", du: "besuchst", er_sie_es: "besucht", wir: "besuchen", ihr: "besucht", sie_Sie: "besuchen" },
        note: "Tiền tố không tách 'be-'. Ví dụ: Wir besuchen das Brandenburger Tor in Berlin.",
        example: "Wir besuchen das Brandenburger Tor in Berlin."
    },
    {
        infinitiv: "buchstabieren",
        meaning: "đánh vần từng chữ cái",
        group: "Quy tắc (Regelmäßig)",
        stem: "buchstabier-",
        ending: "-en",
        forms: { ich: "buchstabiere", du: "buchstabierst", er_sie_es: "buchstabiert", wir: "buchstabieren", ihr: "buchstabiert", sie_Sie: "buchstabieren" },
        note: "Đuôi -ieren nhấn trọng âm vào -ier-. Ví dụ: Können Sie das bitte buchstabieren?",
        example: "Können Sie Ihren Vornamen bitte buchstabieren?"
    },
    {
        infinitiv: "verstehen",
        meaning: "hiểu, nắm rõ ý nghĩa",
        group: "Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)",
        stem: "versteh-",
        ending: "-en",
        forms: { ich: "verstehe", du: "verstehst", er_sie_es: "versteht", wir: "verstehen", ihr: "versteht", sie_Sie: "verstehen" },
        note: "Tiền tố không tách ver-. Ví dụ: Das verstehe ich nicht.",
        example: "Entschuldigung, wie bitte? Das verstehe ich leider nicht."
    },
    {
        infinitiv: "wiederholen",
        meaning: "nhắc lại, lặp lại lời nói",
        group: "Quy tắc (Regelmäßig)",
        stem: "wiederhol-",
        ending: "-en",
        forms: { ich: "wiederhole", du: "wiederholst", er_sie_es: "wiederholt", wir: "wiederholen", ihr: "wiederholt", sie_Sie: "wiederholen" },
        note: "Không tách khi mang nghĩa lặp lại lời nói. Ví dụ: Können Sie das bitte wiederholen?",
        example: "Können Sie die Frage bitte noch einmal wiederholen?"
    },
    {
        infinitiv: "schreiben",
        meaning: "viết",
        group: "Quy tắc (Regelmäßig)",
        stem: "schreib-",
        ending: "-en",
        forms: { ich: "schreibe", du: "schreibst", er_sie_es: "schreibt", wir: "schreiben", ihr: "schreibt", sie_Sie: "schreiben" },
        note: "Chia theo công thức chuẩn: -e, -st, -t, -en, -t, -en.",
        example: "Ich schreibe eine Postkarte an Anna."
    },
    {
        infinitiv: "helfen",
        meaning: "giúp đỡ, trợ giúp",
        group: "Biến âm gốc (nehmen, lesen)",
        stem: "helf- / hilf-",
        ending: "-en",
        forms: { ich: "helfe", du: "hilfst", er_sie_es: "hilft", wir: "helfen", ihr: "helft", sie_Sie: "helfen" },
        note: "Biến âm gốc e -> i ở ngôi du (hilfst) và er/sie/es (hilft).",
        example: "Können Sie mir bitte helfen?"
    },
    {
        infinitiv: "öffnen",
        meaning: "mở (sách, cửa sổ, phòng)",
        group: "Gốc -t, -d (mieten, arbeiten)",
        stem: "öffn-",
        ending: "-en",
        forms: { ich: "öffne", du: "öffnest", er_sie_es: "öffnet", wir: "öffnen", ihr: "öffnet", sie_Sie: "öffnen" },
        note: "Gốc kết thúc bằng -fn nên thêm âm đệm -e- ở ngôi du (-est) và er/sie/es (-et).",
        example: "Bitte öffnen Sie das Buch auf Seite zwanzig."
    },
    {
        infinitiv: "schließen",
        meaning: "đóng lại, khép lại",
        group: "Gốc -s, -ß, -z (heißen, tanzen)",
        stem: "schließ-",
        ending: "-en",
        forms: { ich: "schließe", du: "schließt", er_sie_es: "schließt", wir: "schließen", ihr: "schließt", sie_Sie: "schließen" },
        note: "Gốc kết thúc bằng -ß nên ngôi du chỉ thêm -t (du schließt = er/sie/es schließt).",
        example: "Schließen Sie bitte das Fenster!"
    },
    {
        infinitiv: "zeigen",
        meaning: "chỉ, cho xem (ảnh, tài liệu)",
        group: "Quy tắc (Regelmäßig)",
        stem: "zeig-",
        ending: "-en",
        forms: { ich: "zeige", du: "zeigst", er_sie_es: "zeigt", wir: "zeigen", ihr: "zeigt", sie_Sie: "zeigen" },
        note: "Chia theo công thức chuẩn: -e, -st, -t, -en, -t, -en.",
        example: "Paula zeigt Fotos von der Reise nach Hai Phong."
    },
    {
        infinitiv: "suchen",
        meaning: "tìm kiếm (+ Akkusativ)",
        group: "Quy tắc (Regelmäßig)",
        stem: "such-",
        ending: "-en",
        forms: { ich: "suche", du: "suchst", er_sie_es: "sucht", wir: "suchen", ihr: "sucht", sie_Sie: "suchen" },
        note: "Đòi hỏi tân ngữ Cách 4 (Akkusativ): Wir suchen eine neue Wohnung mit Garten.",
        example: "Wir suchen eine Wohnung mit 3 Zimmern und Balkon."
    },
    {
        infinitiv: "brauchen",
        meaning: "cần (+ Akkusativ)",
        group: "Quy tắc (Regelmäßig)",
        stem: "brauch-",
        ending: "-en",
        forms: { ich: "brauche", du: "brauchst", er_sie_es: "braucht", wir: "brauchen", ihr: "braucht", sie_Sie: "brauchen" },
        note: "Đòi hỏi tân ngữ Cách 4 (Akkusativ): Ich brauche einen Tisch und einen Stuhl.",
        example: "Mein Arbeitszimmer braucht einen Tisch und einen Stuhl."
    }
];

let currentVerbFilterGroup = "all";
let currentVerbSearchQuery = "";

/**
 * Hàm định dạng màu sắc cho dạng chia động từ
 */
function formatConjugatedForm(verb, personKey, value) {
    const vInf = verb.infinitiv;

    // 1. Trường hợp đặc biệt sein, haben
    if (vInf === "sein") {
        return `<span class="font-black text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded-md border border-indigo-200">${value}</span>`;
    }
    if (vInf === "haben") {
        if (personKey === "du" || personKey === "er_sie_es") {
            return `<span class="font-black text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">${value}</span>`;
        }
    }
    if (vInf === "möchten") {
        if (personKey === "ich" || personKey === "er_sie_es") {
            return `<span class="font-black text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">${value}</span>`;
        }
    }

    // 2. Trường hợp biến âm gốc
    if (verb.group.includes("Biến âm")) {
        if (personKey === "du" || personKey === "er_sie_es") {
            return `<span class="font-black text-amber-700 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">${value}</span>`;
        }
    }

    // 3. Trường hợp gốc kết thúc -t, -d
    if (verb.group.includes("-t, -d")) {
        if (personKey === "du" || personKey === "er_sie_es" || personKey === "ihr") {
            return `<span class="font-black text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">${value}</span>`;
        }
    }

    // 4. Trường hợp -s, -ß, -z
    if (verb.group.includes("-s, -ß, -z")) {
        if (personKey === "du") {
            return `<span class="font-black text-purple-700 bg-purple-50 px-2 py-0.5 rounded-md border border-purple-200">${value}</span>`;
        }
    }

    // Mặc định: Highlight phần đuôi
    return `<span class="font-black text-slate-900">${value}</span>`;
}

/**
 * Đọc lần lượt 6 ngôi của động từ bằng giọng bản xứ de-DE
 */
function speakAllForms(verbInfinitiv) {
    const verb = GERMAN_VERBS_DB.find(v => v.infinitiv === verbInfinitiv);
    if (!verb) return;

    const list = [
        `ich ${verb.forms.ich}`,
        `du ${verb.forms.du}`,
        `er, sie, es ${verb.forms.er_sie_es}`,
        `wir ${verb.forms.wir}`,
        `ihr ${verb.forms.ihr}`,
        `sie und Sie ${verb.forms.sie_Sie}`
    ];

    let i = 0;
    function speakNext() {
        if (i < list.length) {
            if (typeof window.speakGerman === 'function') {
                window.speakGerman(list[i]);
            }
            i++;
            setTimeout(speakNext, 1100);
        }
    }
    speakNext();
}

/**
 * Đọc lần lượt 6 ngôi của thì Quá khứ đơn (Präteritum)
 */
function speakAllPraeteritumForms(verbInfinitiv) {
    const verb = GERMAN_VERBS_DB.find(v => v.infinitiv === verbInfinitiv);
    if (!verb || !verb.praeteritum) return;

    const list = [
        `ich ${verb.praeteritum.ich}`,
        `du ${verb.praeteritum.du}`,
        `er, sie, es ${verb.praeteritum.er_sie_es}`,
        `wir ${verb.praeteritum.wir}`,
        `ihr ${verb.praeteritum.ihr}`,
        `sie und Sie ${verb.praeteritum.sie_Sie}`
    ];

    let i = 0;
    function speakNext() {
        if (i < list.length) {
            if (typeof window.speakGerman === 'function') {
                window.speakGerman(list[i]);
            }
            i++;
            setTimeout(speakNext, 1100);
        }
    }
    speakNext();
}

const VERB_GROUPS = [
    { id: "all", label: "Tất cả" },
    { id: "Quy tắc", label: "Quy tắc (Regelmäßig)" },
    { id: "-s, -ß, -z", label: "Gốc -s, -ß, -z (heißen, tanzen)" },
    { id: "-t, -d", label: "Gốc -t, -d (mieten, arbeiten)" },
    { id: "Biến âm", label: "Biến âm gốc (nehmen, lesen)" },
    { id: "Bất quy tắc", label: "Bất quy tắc & Khuyết thiếu (sein, möchten)" }
];

function updateVerbKonjugatorUI() {
    const cardsGrid = document.getElementById('verb-cards-grid');
    const filterPills = document.getElementById('verb-filter-pills');
    const clearWrap = document.getElementById('verb-clear-btn-wrap');
    if (!cardsGrid || !filterPills || !clearWrap) return;

    const q = (currentVerbSearchQuery || "").toLowerCase().trim();
    const filteredVerbs = GERMAN_VERBS_DB.filter(v => {
        const matchGroup = (currentVerbFilterGroup === "all") || v.group.toLowerCase().includes(currentVerbFilterGroup.toLowerCase());
        const matchSearch = !q ||
            v.infinitiv.toLowerCase().includes(q) ||
            v.meaning.toLowerCase().includes(q) ||
            Object.values(v.forms).some(f => f.toLowerCase().includes(q));
        return matchGroup && matchSearch;
    });

    clearWrap.innerHTML = currentVerbSearchQuery ? `
        <button onclick="clearVerbSearch()" class="px-4 py-3 rounded-2xl bg-white/10 hover:bg-white/20 text-white text-xs font-bold border border-white/20 transition cursor-pointer">
            ✕ Xóa tìm kiếm
        </button>
    ` : '';

    filterPills.innerHTML = VERB_GROUPS.map(g => {
        const count = g.id === "all"
            ? GERMAN_VERBS_DB.length
            : GERMAN_VERBS_DB.filter(v => v.group.toLowerCase().includes(g.id.toLowerCase())).length;
        const isActive = currentVerbFilterGroup === g.id;
        return `
            <button onclick="setVerbFilterGroup('${g.id}')" class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition whitespace-nowrap shrink-0 cursor-pointer ${isActive ? 'bg-indigo-600 text-white shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'}">
                ${g.label} (${count})
            </button>
        `;
    }).join('');

    if (filteredVerbs.length === 0) {
        cardsGrid.innerHTML = `
            <div class="col-span-full p-8 rounded-3xl bg-white border border-slate-200 text-center space-y-3">
                <div class="text-3xl">🔍</div>
                <h4 class="text-base font-bold text-slate-800">Không tìm thấy động từ nào phù hợp với từ khóa "${currentVerbSearchQuery}"</h4>
                <p class="text-xs text-slate-500">Hãy thử gõ từ nguyên mẫu như 'machen', 'sein', 'wohnen' hoặc nghĩa tiếng Việt như 'uống', 'sống', 'thuê'.</p>
                <button onclick="clearVerbSearch()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs cursor-pointer">
                    Hiển thị toàn bộ ${GERMAN_VERBS_DB.length} động từ
                </button>
            </div>
        `;
        return;
    }

    cardsGrid.innerHTML = filteredVerbs.map(v => {
        let badgeColor = "bg-indigo-50 text-indigo-700 border-indigo-200";
        if (v.group.includes("Biến âm")) badgeColor = "bg-amber-50 text-amber-800 border-amber-300";
        else if (v.group.includes("-t, -d")) badgeColor = "bg-emerald-50 text-emerald-800 border-emerald-300";
        else if (v.group.includes("-s, -ß, -z")) badgeColor = "bg-purple-50 text-purple-800 border-purple-300";
        else if (v.group.includes("Bất quy tắc")) badgeColor = "bg-rose-50 text-rose-800 border-rose-300";

        const safeExample = v.example.replace(/'/g, "\\'");

        return `
            <div class="p-5 sm:p-6 rounded-3xl bg-white border border-slate-200 shadow-sm hover:shadow-lg hover:border-indigo-300 transition-all flex flex-col justify-between space-y-4">
                <!-- Tiêu đề động từ & Nhóm -->
                <div>
                    <div class="flex items-start justify-between gap-3 flex-wrap">
                        <div class="flex items-baseline gap-2.5">
                            <h3 class="text-2xl font-black text-slate-900 tracking-tight">${v.infinitiv}</h3>
                            <button onclick="speakGerman('${v.infinitiv}')" class="w-8 h-8 rounded-xl bg-slate-100 hover:bg-indigo-600 text-slate-600 hover:text-white flex items-center justify-center text-xs transition shadow-xs cursor-pointer" title="Phát âm nguyên mẫu">
                                🔊
                            </button>
                        </div>
                        <span class="px-2.5 py-1 rounded-lg text-[11px] font-bold border ${badgeColor}">
                            ${v.group.split('(')[0].trim()}
                        </span>
                    </div>
                    <p class="text-sm font-bold text-indigo-600 mt-1">${v.meaning}</p>
                    
                    <!-- Phân tích gốc + đuôi -->
                    <div class="mt-2.5 flex items-center gap-2 text-xs">
                        <span class="px-2 py-0.5 rounded-md bg-slate-100 text-slate-600 font-semibold border border-slate-200">
                            Gốc: <b class="text-slate-900">${v.stem}</b>
                        </span>
                        <span class="px-2 py-0.5 rounded-md bg-slate-100 text-slate-600 font-semibold border border-slate-200">
                            Đuôi: <b class="text-slate-900">${v.ending}</b>
                        </span>
                    </div>

                    <p class="text-xs text-slate-500 mt-2 italic bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                        💡 ${v.note}
                    </p>
                </div>

                <!-- Bảng chia 6 ngôi Hiện tại (Präsens) -->
                <div>
                    <div class="flex items-center justify-between mb-1.5 px-1">
                        <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider">Thì Hiện Tại (Präsens)</span>
                        <span class="text-[10px] text-indigo-600 font-semibold">🔊 Bấm ô để nghe</span>
                    </div>
                    <div class="grid grid-cols-2 gap-2 bg-slate-50/70 p-3 rounded-2xl border border-slate-200/80 text-xs">
                        <div onclick="speakGerman('ich ${v.forms.ich}')" class="cursor-pointer p-2 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">ich:</span>
                            <div class="flex items-center gap-1">
                                ${formatConjugatedForm(v, 'ich', v.forms.ich)}
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-indigo-600">🔊</span>
                            </div>
                        </div>
                        <div onclick="speakGerman('wir ${v.forms.wir}')" class="cursor-pointer p-2 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">wir:</span>
                            <div class="flex items-center gap-1">
                                ${formatConjugatedForm(v, 'wir', v.forms.wir)}
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-indigo-600">🔊</span>
                            </div>
                        </div>

                        <div onclick="speakGerman('du ${v.forms.du}')" class="cursor-pointer p-2 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">du:</span>
                            <div class="flex items-center gap-1">
                                ${formatConjugatedForm(v, 'du', v.forms.du)}
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-indigo-600">🔊</span>
                            </div>
                        </div>
                        <div onclick="speakGerman('ihr ${v.forms.ihr}')" class="cursor-pointer p-2 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">ihr:</span>
                            <div class="flex items-center gap-1">
                                ${formatConjugatedForm(v, 'ihr', v.forms.ihr)}
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-indigo-600">🔊</span>
                            </div>
                        </div>

                        <div onclick="speakGerman('er ${v.forms.er_sie_es}')" class="cursor-pointer p-2 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">er/sie/es:</span>
                            <div class="flex items-center gap-1">
                                ${formatConjugatedForm(v, 'er_sie_es', v.forms.er_sie_es)}
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-indigo-600">🔊</span>
                            </div>
                        </div>
                        <div onclick="speakGerman('sie ${v.forms.sie_Sie}')" class="cursor-pointer p-2 rounded-xl bg-white border border-slate-200/80 hover:border-indigo-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">sie/Sie:</span>
                            <div class="flex items-center gap-1">
                                ${formatConjugatedForm(v, 'sie_Sie', v.forms.sie_Sie)}
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-indigo-600">🔊</span>
                            </div>
                        </div>
                    </div>
                </div>

                ${v.praeteritum ? `
                <!-- Bảng chia 6 ngôi Quá khứ đơn (Präteritum) -->
                <div>
                    <div class="flex items-center justify-between mb-1.5 px-1">
                        <span class="text-[11px] font-bold text-amber-700 uppercase tracking-wider">Thì Quá Khứ Đơn (Präteritum)</span>
                        <button onclick="speakAllPraeteritumForms('${v.infinitiv}')" class="text-[10px] text-amber-800 hover:text-amber-950 font-bold hover:underline cursor-pointer">
                            🔊 Đọc 6 ngôi Präteritum
                        </button>
                    </div>
                    <div class="grid grid-cols-2 gap-2 bg-amber-50/60 p-3 rounded-2xl border border-amber-200 text-xs">
                        <div onclick="speakGerman('ich ${v.praeteritum.ich}')" class="cursor-pointer p-2 rounded-xl bg-white border border-amber-200/80 hover:border-amber-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">ich:</span>
                            <div class="flex items-center gap-1">
                                <span class="font-black text-amber-900">${v.praeteritum.ich}</span>
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-amber-600">🔊</span>
                            </div>
                        </div>
                        <div onclick="speakGerman('wir ${v.praeteritum.wir}')" class="cursor-pointer p-2 rounded-xl bg-white border border-amber-200/80 hover:border-amber-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">wir:</span>
                            <div class="flex items-center gap-1">
                                <span class="font-black text-amber-900">${v.praeteritum.wir}</span>
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-amber-600">🔊</span>
                            </div>
                        </div>

                        <div onclick="speakGerman('du ${v.praeteritum.du}')" class="cursor-pointer p-2 rounded-xl bg-white border border-amber-200/80 hover:border-amber-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">du:</span>
                            <div class="flex items-center gap-1">
                                <span class="font-black text-amber-900">${v.praeteritum.du}</span>
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-amber-600">🔊</span>
                            </div>
                        </div>
                        <div onclick="speakGerman('ihr ${v.praeteritum.ihr}')" class="cursor-pointer p-2 rounded-xl bg-white border border-amber-200/80 hover:border-amber-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">ihr:</span>
                            <div class="flex items-center gap-1">
                                <span class="font-black text-amber-900">${v.praeteritum.ihr}</span>
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-amber-600">🔊</span>
                            </div>
                        </div>

                        <div onclick="speakGerman('er ${v.praeteritum.er_sie_es}')" class="cursor-pointer p-2 rounded-xl bg-white border border-amber-200/80 hover:border-amber-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">er/sie/es:</span>
                            <div class="flex items-center gap-1">
                                <span class="font-black text-amber-900">${v.praeteritum.er_sie_es}</span>
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-amber-600">🔊</span>
                            </div>
                        </div>
                        <div onclick="speakGerman('sie ${v.praeteritum.sie_Sie}')" class="cursor-pointer p-2 rounded-xl bg-white border border-amber-200/80 hover:border-amber-400 hover:shadow-xs transition flex items-center justify-between group">
                            <span class="text-slate-500 font-medium">sie/Sie:</span>
                            <div class="flex items-center gap-1">
                                <span class="font-black text-amber-900">${v.praeteritum.sie_Sie}</span>
                                <span class="opacity-0 group-hover:opacity-100 transition text-[10px] text-amber-600">🔊</span>
                            </div>
                        </div>
                    </div>
                </div>
                ` : ''}

                <!-- Ví dụ thực tế & Nút đọc toàn bộ bảng -->
                <div class="pt-2 border-t border-slate-100 space-y-2.5">
                    <div class="flex items-center justify-between gap-2 text-xs">
                        <span class="text-slate-600 italic truncate" title="${v.example}">"${v.example}"</span>
                        <button onclick="speakGerman('${safeExample}')" class="shrink-0 px-2 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 font-bold transition cursor-pointer" title="Nghe câu ví dụ">
                            🔊 Ví dụ
                        </button>
                    </div>

                    <button onclick="speakAllForms('${v.infinitiv}')" class="w-full py-2 rounded-xl bg-slate-100 hover:bg-indigo-600 hover:text-white text-slate-700 text-xs font-bold transition flex items-center justify-center gap-1.5 shadow-2xs cursor-pointer">
                        🔊 Đọc toàn bộ bảng chia (6 ngôi)
                    </button>
                </div>
            </div>
        `;
    }).join('');
}

/**
 * Render giao diện Tra cứu & Chia động từ (Verb-Konjugator)
 */
function renderVerbKonjugator(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (!document.getElementById('verb-cards-grid')) {
        container.innerHTML = `
            <!-- Hero Banner của Tab Tra cứu động từ -->
            <div class="rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white p-6 sm:p-8 shadow-xl border border-slate-800">
                <div class="flex flex-wrap items-center justify-between gap-4">
                    <div class="space-y-2 max-w-3xl">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                            📖 DeutschMeister Verb-Konjugator • Bảng Tra Cứu Chia Động Từ A1 - A2
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-black tracking-tight text-white">
                            Tra Cứu & Luyện Phát Âm Chia Động Từ
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                            Hệ thống tự động phân tách <b>Gốc động từ (Verbstamm)</b>, tô màu <b>Đuôi chia (-e, -st, -t, -en)</b>, cảnh báo biến âm (e → i/ie, a → ä) và hỗ trợ giọng đọc bản xứ <b>de-DE</b> cho từng ngôi nhân xưng.
                        </p>
                    </div>

                    <div class="shrink-0 text-right hidden sm:block">
                        <span class="px-4 py-2 rounded-2xl bg-white/10 border border-white/20 text-amber-400 font-extrabold text-sm flex items-center gap-2">
                            ⚡ ${GERMAN_VERBS_DB.length} Động từ cốt lõi
                        </span>
                    </div>
                </div>

                <!-- Thanh tìm kiếm thông minh (Giữ nguyên DOM để tránh nhảy chữ khi gõ bàn phím) -->
                <div class="mt-6 flex flex-wrap gap-3">
                    <div class="relative flex-1 min-w-[260px]">
                        <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                            🔍
                        </span>
                        <input id="verb-search-input" value="${currentVerbSearchQuery}" oninput="onVerbSearchChange(this.value)" type="text" placeholder="Gõ động từ tiếng Đức (machen, sein, nehmen...) hoặc nghĩa tiếng Việt (làm, uống, muốn, thuê...)" class="w-full pl-10 pr-4 py-3 rounded-2xl bg-white/10 border border-white/20 text-white placeholder:text-slate-400 text-sm focus:outline-none focus:bg-white/20 focus:border-amber-400 transition" autocomplete="off" spellcheck="false">
                    </div>
                    <div id="verb-clear-btn-wrap"></div>
                </div>
            </div>

            <!-- Bộ lọc phân loại theo nhóm -->
            <div class="flex items-center gap-2 overflow-x-auto pb-1">
                <span class="text-xs font-bold text-slate-500 whitespace-nowrap">Bộ lọc:</span>
                <div id="verb-filter-pills" class="flex items-center gap-2 overflow-x-auto"></div>
            </div>

            <!-- Lưới thẻ động từ -->
            <div id="verb-cards-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5"></div>
        `;
    }

    updateVerbKonjugatorUI();
}

function setVerbFilterGroup(groupId) {
    currentVerbFilterGroup = groupId;
    updateVerbKonjugatorUI();
}

function onVerbSearchChange(val) {
    currentVerbSearchQuery = val;
    updateVerbKonjugatorUI();
}

function clearVerbSearch() {
    currentVerbSearchQuery = "";
    currentVerbFilterGroup = "all";
    const input = document.getElementById('verb-search-input');
    if (input) {
        input.value = "";
        input.focus();
    }
    updateVerbKonjugatorUI();
}

if (typeof window !== 'undefined') {
    window.GERMAN_VERBS_DB = GERMAN_VERBS_DB;
    window.renderVerbKonjugator = renderVerbKonjugator;
    window.updateVerbKonjugatorUI = updateVerbKonjugatorUI;
    window.setVerbFilterGroup = setVerbFilterGroup;
    window.onVerbSearchChange = onVerbSearchChange;
    window.clearVerbSearch = clearVerbSearch;
    window.speakAllForms = speakAllForms;
    window.speakAllPraeteritumForms = speakAllPraeteritumForms;
}
