/**
 * DeutschMeister - CSDL Giống danh từ & Từ vựng theo chủ đề (Genus- & Wortschatz-Lexikon)
 * Tích hợp đầy đủ danh từ lớp học, quy tắc hậu tố der/die/das, số nhiều, mạo từ bất định, phủ định và động từ giao tiếp.
 */

const GERMAN_LEXIKON_DB = [
    // --- 1. ĐỒ DÙNG LỚP HỌC (GIỐNG ĐỰC - DER) ---
    {
        word: "Tisch", article: "der", gender: "der", plural: "die Tische",
        indefinite: "ein Tisch", negation: "kein Tisch",
        meaning: "cái bàn", category: "Đồ dùng lớp học",
        rule: "Danh từ đơn âm tiết chỉ đồ nội thất, số nhiều thêm -e.",
        example: "Ist das ein Tisch? – Ja, das ist der Tisch im Kursraum.",
        example_vi: "Đây có phải là một cái bàn không? – Đúng, đó là cái bàn trong phòng học."
    },
    {
        word: "Stuhl", article: "der", gender: "der", plural: "die Stühle",
        indefinite: "ein Stuhl", negation: "kein Stuhl",
        meaning: "cái ghế", category: "Đồ dùng lớp học",
        rule: "Số nhiều biến âm u -> ü và thêm đuôi -e (die Stühle).",
        example: "Das ist kein Tisch, das ist ein Stuhl.",
        example_vi: "Đó không phải là cái bàn, đó là một cái ghế."
    },
    {
        word: "Füller", article: "der", gender: "der", plural: "die Füller",
        indefinite: "ein Füller", negation: "kein Füller",
        meaning: "bút mực / bút máy", category: "Đồ dùng lớp học",
        rule: "Danh từ kết thúc bằng -er thường mang giống đực (der) và giữ nguyên ở số nhiều.",
        example: "Ist das ein Füller? – Ja, das ist der Füller von Marc.",
        example_vi: "Đây có phải là bút mực không? – Đúng, đó là cây bút mực của Marc."
    },
    {
        word: "Kuli", article: "der", gender: "der", plural: "die Kulis",
        indefinite: "ein Kuli", negation: "kein Kuli",
        meaning: "bút bi (Kugelschreiber)", category: "Đồ dùng lớp học",
        rule: "Viết tắt của der Kugelschreiber, số nhiều thêm -s (die Kulis).",
        example: "Ist das ein Kuli? – Ja, das ist der Kuli von Anna.",
        example_vi: "Đây có phải là một cây bút bi không? – Đúng, đó là bút bi của Anna."
    },
    {
        word: "Bleistift", article: "der", gender: "der", plural: "die Bleistifte",
        indefinite: "ein Bleistift", negation: "kein Bleistift",
        meaning: "bút chì", category: "Đồ dùng lớp học",
        rule: "Ghép từ das Blei (chì) + der Stift (cây bút) -> lấy giống theo từ cuối (der). Số nhiều thêm -e.",
        example: "Ich habe keinen Kuli, aber ich habe einen Bleistift.",
        example_vi: "Tôi không có bút bi, nhưng tôi có một cây bút chì."
    },
    {
        word: "Radiergummi", article: "der", gender: "der", plural: "die Radiergummis",
        indefinite: "ein Radiergummi", negation: "kein Radiergummi",
        meaning: "cục tẩy / cục gôm", category: "Đồ dùng lớp học",
        rule: "Số nhiều thêm đuôi -s (die Radiergummis).",
        example: "Wie heißt das auf Deutsch? – Das ist ein Radiergummi.",
        example_vi: "Cái này tiếng Đức gọi là gì? – Đó là một cục tẩy."
    },
    {
        word: "Becher", article: "der", gender: "der", plural: "die Becher",
        indefinite: "ein Becher", negation: "kein Becher",
        meaning: "cái cốc / cái ly (không quai)", category: "Đồ dùng lớp học",
        rule: "Đuôi -er mang giống đực (der), số nhiều giữ nguyên (die Becher).",
        example: "Ist das ein Becher? – Nein, das ist kein Becher. Das ist ein Heft.",
        example_vi: "Đây có phải là cái cốc không? – Không, đó không phải là cái cốc. Đó là một quyển vở."
    },

    // --- 2. ĐỒ DÙNG LỚP HỌC (GIỐNG CÁI - DIE) ---
    {
        word: "Tafel", article: "die", gender: "die", plural: "die Tafeln",
        indefinite: "eine Tafel", negation: "keine Tafel",
        meaning: "cái bảng đen", category: "Đồ dùng lớp học",
        rule: "Danh từ giống cái kết thúc bằng -el khi sang số nhiều thêm -n (die Tafeln).",
        example: "Die Lehrerin schreibt an die Tafel. Das ist eine Tafel.",
        example_vi: "Cô giáo viết lên bảng. Đó là một cái bảng đen."
    },
    {
        word: "Brille", article: "die", gender: "die", plural: "die Brillen",
        indefinite: "eine Brille", negation: "keine Brille",
        meaning: "cái kính mắt", category: "Đồ dùng lớp học",
        rule: "Đa số danh từ tận cùng bằng -e mang giống cái (die) và thêm -n ở số nhiều.",
        example: "Ist das eine Brille? – Nein, das ist keine Brille. Das ist eine Landkarte.",
        example_vi: "Đây có phải là kính mắt không? – Không, đó không phải kính mắt. Đó là một tấm bản đồ."
    },
    {
        word: "Tasche", article: "die", gender: "die", plural: "die Taschen",
        indefinite: "eine Tasche", negation: "keine Tasche",
        meaning: "túi xách / cặp sách", category: "Đồ dùng lớp học",
        rule: "Tận cùng bằng -e -> giống cái (die), số nhiều thêm -n (die Taschen).",
        example: "Ja, das ist die Tasche von Anna.",
        example_vi: "Đúng vậy, đó là chiếc túi xách của Anna."
    },
    {
        word: "Landkarte", article: "die", gender: "die", plural: "die Landkarten",
        indefinite: "eine Landkarte", negation: "keine Landkarte",
        meaning: "bản đồ", category: "Đồ dùng lớp học",
        rule: "Danh từ ghép (das Land + die Karte) -> lấy giống cái (die) theo từ cuối die Karte.",
        example: "Das ist keine Brille, das ist eine Landkarte.",
        example_vi: "Đó không phải là kính mắt, đó là một tấm bản đồ."
    },

    // --- 3. ĐỒ DÙNG LỚP HỌC (GIỐNG TRUNG - DAS) ---
    {
        word: "Papier", article: "das", gender: "das", plural: "die Papiere",
        indefinite: "ein Papier", negation: "kein Papier",
        meaning: "giấy / tờ giấy (ein Blatt Papier)", category: "Đồ dùng lớp học",
        rule: "Giống trung (das); là danh từ chất liệu không đếm được (một tờ giấy: ein Blatt Papier). Số nhiều die Papiere: giấy tờ tùy thân.",
        example: "Brauchst du Papier? – Ja, ich brauche ein Blatt Papier.",
        example_vi: "Bạn có cần giấy không? – Vâng, tôi cần một tờ giấy."
    },
    {
        word: "Heft", article: "das", gender: "das", plural: "die Hefte",
        indefinite: "ein Heft", negation: "kein Heft",
        meaning: "quyển vở", category: "Đồ dùng lớp học",
        rule: "Giống trung (das), số nhiều thêm -e (die Hefte).",
        example: "Können Sie 'Heft' bitte buchstabieren? – H - E - F - T.",
        example_vi: "Ngài có thể vui lòng đánh vần từ 'Heft' được không? – H - E - F - T."
    },
    {
        word: "Mäppchen", article: "das", gender: "das", plural: "die Mäppchen",
        indefinite: "ein Mäppchen", negation: "kein Mäppchen",
        meaning: "hộp bút / túi đựng bút", category: "Đồ dùng lớp học",
        rule: "Đuôi thu nhỏ -chen luôn mang giống trung (das) 100%, số nhiều giữ nguyên dạng.",
        example: "Ist das dein Mäppchen? – Ja, im Mäppchen sind ein Kuli und ein Bleistift.",
        example_vi: "Đây là hộp bút của bạn à? – Vâng, trong hộp bút có một cây bút bi và một cây bút chì."
    },

    {
        word: "Buch", article: "das", gender: "das", plural: "die Bücher",
        indefinite: "ein Buch", negation: "kein Buch",
        meaning: "quyển sách", category: "Đồ dùng lớp học",
        rule: "Giống trung (das), số nhiều biến âm u -> ü và thêm -er (die Bücher).",
        example: "Ist das ein Buch? – Ja, das ist das Buch von Frau Schiller.",
        example_vi: "Đây có phải là một quyển sách không? – Đúng, đó là quyển sách của bà Schiller."
    },
    {
        word: "Wörterbuch", article: "das", gender: "das", plural: "die Wörterbücher",
        indefinite: "ein Wörterbuch", negation: "kein Wörterbuch",
        meaning: "quyển từ điển", category: "Đồ dùng lớp học",
        rule: "Danh từ ghép (die Wörter + das Buch) -> lấy giống das và số nhiều theo Buch.",
        example: "Das ist kein Heft, das ist ein Wörterbuch.",
        example_vi: "Đó không phải là quyển vở, đó là một quyển từ điển."
    },
    {
        word: "Handy", article: "das", gender: "das", plural: "die Handys",
        indefinite: "ein Handy", negation: "kein Handy",
        meaning: "điện thoại di động", category: "Đồ dùng lớp học",
        rule: "Giống trung (das), số nhiều thêm -s (die Handys - không biến đổi y thành ie).",
        example: "Ist das ein Handy? – Ja, das ist das Handy von David.",
        example_vi: "Đây có phải là điện thoại không? – Đúng, đó là chiếc điện thoại của David."
    },
    {
        word: "Whiteboard", article: "das", gender: "das", plural: "die Whiteboards",
        indefinite: "ein Whiteboard", negation: "kein Whiteboard",
        meaning: "bảng trắng", category: "Đồ dùng lớp học",
        rule: "Từ mượn tiếng Anh đi với das Board -> das Whiteboard, số nhiều thêm -s.",
        example: "Im Deutschkurs haben wir eine Tafel und ein Whiteboard.",
        example_vi: "Trong lớp học tiếng Đức chúng tôi có một bảng đen và một bảng trắng."
    },
    {
        word: "Brötchen", article: "das", gender: "das", plural: "die Brötchen",
        indefinite: "ein Brötchen", negation: "kein Brötchen",
        meaning: "bánh mì nhỏ", category: "Quy tắc hậu tố giống",
        rule: "Mọi danh từ có hậu tố giảm nhẹ -chen luôn mang giống trung (das) 100% và giữ nguyên ở số nhiều.",
        example: "Ich esse ein Brötchen und trinke einen Kaffee.",
        example_vi: "Tôi ăn một chiếc bánh mì nhỏ và uống một ly cà phê."
    },

    // --- 4. ĐỘNG TỪ LỚP HỌC & GIAO TIẾP (VERBEN IM KURS) ---
    {
        word: "verstehen", article: "Verb", gender: "verb", plural: "ich verstehe / Sie verstehen",
        indefinite: "Gốc: versteh-", negation: "Phủ định: verstehe ... nicht",
        meaning: "hiểu, nắm bắt được", category: "Động từ lớp học",
        rule: "Động từ có tiền tố không tách 'ver-'. Khi phủ định cả câu dùng 'nicht': Das verstehe ich nicht.",
        example: "Das verstehe ich nicht. Können Sie das bitte erklären?",
        example_vi: "Điều đó tôi không hiểu. Ngài có thể giải thích điều đó được không?"
    },
    {
        word: "wiederholen", article: "Verb", gender: "verb", plural: "ich wiederhole / Sie wiederholen",
        indefinite: "Gốc: wiederhol-", negation: "Đi với: Können Sie ...?",
        meaning: "lặp lại, nhắc lại", category: "Động từ lớp học",
        rule: "Thường đứng cuối câu ở dạng nguyên mẫu khi đi với động từ khuyết thiếu 'können'.",
        example: "Das verstehe ich nicht. Können Sie das bitte wiederholen?",
        example_vi: "Điều đó tôi không hiểu. Ngài có thể vui lòng lặp lại được không ạ?"
    },
    {
        word: "buchstabieren", article: "Verb", gender: "verb", plural: "ich buchstabiere / Sie buchstabieren",
        indefinite: "Gốc: buchstabier-", negation: "Đuôi: -ieren",
        meaning: "đánh vần từng chữ cái", category: "Động từ lớp học",
        rule: "Động từ đuôi -ieren dùng để yêu cầu đánh vần tên người, thành phố hoặc từ mới.",
        example: "Das verstehe ich nicht. Können Sie das bitte buchstabieren?",
        example_vi: "Điều đó tôi không hiểu. Ngài có thể vui lòng đánh vần từ đó được không ạ?"
    },
    {
        word: "anschreiben", article: "Verb", gender: "verb", plural: "ich schreibe an / Sie schreiben an",
        indefinite: "Tiền tố tách: an-", negation: "Nguyên mẫu cuối câu",
        meaning: "viết lên bảng", category: "Động từ lớp học",
        rule: "Khi đi với 'Können Sie...?', động từ giữ nguyên mẫu 'anschreiben' ở cuối câu.",
        example: "Das verstehe ich nicht. Können Sie das bitte anschreiben?",
        example_vi: "Điều đó tôi không hiểu. Ngài có thể vui lòng viết từ đó lên bảng được không ạ?"
    },
    {
        word: "können", article: "Modalverb", gender: "verb", plural: "ich kann / du kannst / Sie können",
        indefinite: "Khuyết thiếu", negation: "Cấu trúc khung câu",
        meaning: "có thể (nhờ vả lịch sự / khả năng)", category: "Động từ lớp học",
        rule: "Đứng ở vị trí thứ 2 (hoặc đầu câu hỏi Yes/No), đẩy động từ chính về cuối câu ở dạng nguyên mẫu.",
        example: "Können Sie das bitte langsam wiederholen?",
        example_vi: "Ngài có thể vui lòng lặp lại điều đó chậm một chút được không?"
    },

    // --- 5. CÁC DANH TỪ MẪU THEO QUY TẮC HẬU TỐ NHẬN BIẾT GIỐNG ---
    {
        word: "Praktikant", article: "der", gender: "der", plural: "die Praktikanten",
        indefinite: "ein Praktikant", negation: "kein Praktikant",
        meaning: "nam thực tập sinh", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ant luôn mang giống đực (der).",
        example: "Er ist Praktikant bei der Post.",
        example_vi: "Anh ấy là một thực tập sinh tại bưu điện."
    },
    {
        word: "Student", article: "der", gender: "der", plural: "die Studenten",
        indefinite: "ein Student", negation: "kein Student",
        meaning: "nam sinh viên", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ent luôn mang giống đực (der). Nữ sinh viên là die Studentin.",
        example: "David ist Student aus den USA.",
        example_vi: "David là một sinh viên đến từ Mỹ."
    },
    {
        word: "Teppich", article: "der", gender: "der", plural: "die Teppiche",
        indefinite: "ein Teppich", negation: "kein Teppich",
        meaning: "tấm thảm", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ich luôn mang giống đực (der).",
        example: "Ist das ein Teppich? – Ja, der Teppich ist sehr schön.",
        example_vi: "Đây có phải là một tấm thảm không? – Đúng, tấm thảm rất đẹp."
    },
    {
        word: "Polizist", article: "der", gender: "der", plural: "die Polizisten",
        indefinite: "ein Polizist", negation: "kein Polizist",
        meaning: "nam cảnh sát", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ist luôn mang giống đực (der).",
        example: "Mein Freund arbeitet als Polizist in Berlin.",
        example_vi: "Bạn tôi làm cảnh sát ở Berlin."
    },
    {
        word: "Zwilling", article: "der", gender: "der", plural: "die Zwillinge",
        indefinite: "ein Zwilling", negation: "kein Zwilling",
        meaning: "anh/em sinh đôi", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ling luôn mang giống đực (der).",
        example: "Peter und Paul sind Zwillinge.",
        example_vi: "Peter và Paul là hai anh em sinh đôi."
    },
    {
        word: "Krankheit", article: "die", gender: "die", plural: "die Krankheiten",
        indefinite: "eine Krankheit", negation: "keine Krankheit",
        meaning: "căn bệnh", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -heit luôn mang giống cái (die) 100%, số nhiều thêm -en.",
        example: "Das ist keine schlimme Krankheit.",
        example_vi: "Đó không phải là một căn bệnh nghiêm trọng."
    },
    {
        word: "Möglichkeit", article: "die", gender: "die", plural: "die Möglichkeiten",
        indefinite: "eine Möglichkeit", negation: "keine Möglichkeit",
        meaning: "khả năng, cơ hội", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -keit luôn mang giống cái (die) 100%, số nhiều thêm -en.",
        example: "Das ist eine gute Möglichkeit für uns.",
        example_vi: "Đó là một cơ hội tốt cho chúng tôi."
    },
    {
        word: "Freundschaft", article: "die", gender: "die", plural: "die Freundschaften",
        indefinite: "eine Freundschaft", negation: "keine Freundschaft",
        meaning: "tình bạn", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -schaft luôn mang giống cái (die) 100%.",
        example: "Die Freundschaft zwischen Anna und Sophie ist toll.",
        example_vi: "Tình bạn của Anna và Sophie thật tuyệt vời."
    },
    {
        word: "Kleidung", article: "die", gender: "die", plural: "die Kleidungen",
        indefinite: "eine Kleidung", negation: "keine Kleidung",
        meaning: "quần áo, trang phục", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ung luôn mang giống cái (die) 100%.",
        example: "Die Kleidung aus Italien ist sehr modern.",
        example_vi: "Trang phục từ Ý rất hiện đại."
    },
    {
        word: "Sekretärin", article: "die", gender: "die", plural: "die Sekretärinnen",
        indefinite: "eine Sekretärin", negation: "keine Sekretärin",
        meaning: "nữ thư ký", category: "Quy tắc hậu tố giống",
        rule: "Danh từ nghề nghiệp nữ giới có đuôi -in luôn mang giống cái (die), số nhiều thêm -nen.",
        example: "Frau Bui arbeitet als Sekretärin in Hamburg.",
        example_vi: "Bà Bùi làm nữ thư ký tại Hamburg."
    },
    {
        word: "Dokument", article: "das", gender: "das", plural: "die Dokumente",
        indefinite: "ein Dokument", negation: "kein Dokument",
        meaning: "tài liệu, văn kiện", category: "Quy tắc hậu tố giống",
        rule: "Đa số đuôi -ment mang giống trung (das), NGOẠI TRỪ: der Moment (khoảnh khắc)!",
        example: "Ist das ein Dokument? – Ja, das ist das Dokument von Herrn Nguyen.",
        example_vi: "Đây có phải là tài liệu không? – Đúng, đó là tài liệu của ông Nguyễn."
    },
    {
        word: "Moment", article: "der", gender: "der", plural: "die Momente",
        indefinite: "ein Moment", negation: "kein Moment",
        meaning: "khoảnh khắc, giây lát (NGOẠI LỆ)", category: "Quy tắc hậu tố giống",
        rule: "⚠️ NGOẠI LỆ QUAN TRỌNG: Dù kết thúc bằng -ment nhưng 'der Moment' mang giống đực!",
        example: "Einen Moment, bitte! Ich schreibe das Wort an.",
        example_vi: "Xin chờ một lát! Tôi sẽ viết từ đó lên bảng."
    },
    {
        word: "Ergebnis", article: "das", gender: "das", plural: "die Ergebnisse",
        indefinite: "ein Ergebnis", negation: "kein Ergebnis",
        meaning: "kết quả", category: "Quy tắc hậu tố giống",
        rule: "Đa số đuôi -nis mang giống trung (das), NGOẠI TRỪ: die Erlaubnis (sự cho phép)!",
        example: "Das Ergebnis im Deutschkurs ist super.",
        example_vi: "Kết quả trong khóa học tiếng Đức rất tuyệt."
    },
    {
        word: "Erlaubnis", article: "die", gender: "die", plural: "die Erlaubnisse",
        indefinite: "eine Erlaubnis", negation: "keine Erlaubnis",
        meaning: "sự cho phép, giấy phép (NGOẠI LỆ)", category: "Quy tắc hậu tố giống",
        rule: "⚠️ NGOẠI LỆ QUAN TRỌNG: Dù kết thúc bằng -nis nhưng 'die Erlaubnis' mang giống cái!",
        example: "Hast du die Erlaubnis von der Lehrerin?",
        example_vi: "Bạn có sự cho phép của cô giáo chưa?"
    },
    // --- 4. BÀI 3: DANH LAM THẮNG CẢNH CHÂU ÂU (SEHENSWÜRDIGKEITEN) ---
    {
        word: "Sehenswürdigkeit", article: "die", gender: "die", plural: "die Sehenswürdigkeiten",
        indefinite: "eine Sehenswürdigkeit", negation: "keine Sehenswürdigkeit",
        meaning: "danh lam thắng cảnh, điểm tham quan", category: "Danh lam thắng cảnh",
        rule: "Hậu tố -keit luôn mang giống cái (die) 100%, số nhiều thêm -en.",
        example: "Der Eiffelturm ist eine berühmte Sehenswürdigkeit in Europa.",
        example_vi: "Tháp Eiffel là một danh lam thắng cảnh nổi tiếng ở châu Âu."
    },
    {
        word: "Akropolis", article: "die", gender: "die", plural: "— (Danh từ riêng)",
        indefinite: "Athen (Hy Lạp)", negation: "Griechenland",
        meaning: "Thành cổ Akropolis (ở Athens, Hy Lạp)", category: "Danh lam thắng cảnh",
        rule: "Danh thắng nổi tiếng ở Athen (Griechenland), luôn đi kèm mạo từ xác định 'die'.",
        example: "Was ist das? – Das ist die Akropolis. Sie liegt in Athen, Griechenland.",
        example_vi: "Đây là gì? – Đó là thành cổ Akropolis. Nó nằm ở Athens, Hy Lạp."
    },
    {
        word: "Big Ben", article: "der", gender: "der", plural: "— (Danh từ riêng)",
        indefinite: "London (Anh)", negation: "England / Großbritannien",
        meaning: "Tháp đồng hồ Big Ben (ở London, Anh)", category: "Danh lam thắng cảnh",
        rule: "Mang giống đực (der) theo danh từ der Turm (ngọn tháp).",
        example: "Wo ist der Big Ben? – Der Big Ben ist in London, England.",
        example_vi: "Tháp Big Ben ở đâu? – Tháp Big Ben ở London, nước Anh."
    },
    {
        word: "Eiffelturm", article: "der", gender: "der", plural: "die Eiffeltürme",
        indefinite: "Paris (Pháp)", negation: "Frankreich",
        meaning: "Tháp Eiffel (ở Paris, Pháp)", category: "Danh lam thắng cảnh",
        rule: "Danh từ ghép lấy giống theo từ cuối: der Turm (ngọn tháp) -> der Eiffelturm.",
        example: "Der Eiffelturm steht in Paris. Paris liegt in Frankreich.",
        example_vi: "Tháp Eiffel nằm ở Paris. Paris thuộc nước Pháp."
    },
    {
        word: "Schiefe Turm (von Pisa)", article: "der", gender: "der", plural: "Pisa (Ý)",
        indefinite: "ein schiefer Turm", negation: "Italien",
        meaning: "Tháp nghiêng Pisa (ở Pisa, Ý)", category: "Danh lam thắng cảnh",
        rule: "Cụm danh từ có tính từ 'schief' (nghiêng) + der Turm (tháp) -> der Schiefe Turm von Pisa.",
        example: "Wo ist der Schiefe Turm von Pisa? – Er ist in Pisa, Italien.",
        example_vi: "Tháp nghiêng Pisa ở đâu? – Nó nằm ở thành phố Pisa, nước Ý."
    },
    {
        word: "Prater", article: "der", gender: "der", plural: "— (Danh từ riêng)",
        indefinite: "Wien (Áo)", negation: "Österreich",
        meaning: "Công viên giải trí Prater (ở Viên, Áo)", category: "Danh lam thắng cảnh",
        rule: "Mang giống đực (der), tọa lạc tại thủ đô Wien của nước Áo (Österreich).",
        example: "Der Prater ist in Wien. Wien liegt im Osten von Österreich.",
        example_vi: "Công viên Prater ở Viên. Viên nằm ở phía Đông của nước Áo."
    },
    {
        word: "Brandenburger Tor", article: "das", gender: "das", plural: "Berlin (Đức)",
        indefinite: "ein Tor", negation: "Deutschland",
        meaning: "Cổng Brandenburg (ở Berlin, Đức)", category: "Danh lam thắng cảnh",
        rule: "Lấy giống trung (das) theo danh từ chính das Tor (cái cổng).",
        example: "Was ist das? – Das ist das Brandenburger Tor in Berlin, Deutschland.",
        example_vi: "Đây là gì? – Đó là Cổng Brandenburg ở Berlin, CHLB Đức."
    },
    {
        word: "Rote Platz", article: "der", gender: "der", plural: "Moskau (Nga)",
        indefinite: "ein Platz", negation: "Russland",
        meaning: "Quảng trường Đỏ (ở Mát-xcơ-va, Nga)", category: "Danh lam thắng cảnh",
        rule: "Lấy giống đực (der) theo danh từ der Platz (quảng trường).",
        example: "Der Rote Platz ist in Moskau. Moskau liegt in Russland.",
        example_vi: "Quảng trường Đỏ nằm ở Mát-xcơ-va. Mát-xcơ-va thuộc nước Nga."
    },

    // --- 5. BÀI 3: QUỐC GIA CÓ MẠO TỪ & ĐỊA LÝ (LÄNDER MIT ARTIKEL) ---
    {
        word: "Schweiz", article: "die", gender: "die", plural: "Ngôn ngữ: Deutsch, Französisch, Italienisch",
        indefinite: "in der Schweiz", negation: "aus der Schweiz",
        meaning: "Thụy Sỹ (Quốc gia có mạo từ die)", category: "Quốc gia & Ngôn ngữ",
        rule: "Quốc gia mang giống cái (die). Khi đi với 'aus' hoặc 'in' ở Dativ phải đổi thành 'aus der Schweiz' / 'in der Schweiz'.",
        example: "Meine Tante wohnt in der Schweiz. Dort spricht man Deutsch, Französisch und Italienisch.",
        example_vi: "Cô của tôi sống ở Thụy Sỹ. Ở đó người ta nói tiếng Đức, tiếng Pháp và tiếng Ý."
    },
    {
        word: "Türkei", article: "die", gender: "die", plural: "Ngôn ngữ: Türkisch",
        indefinite: "in der Türkei", negation: "aus der Türkei",
        meaning: "Thổ Nhĩ Kỳ (Quốc gia có mạo từ die)", category: "Quốc gia & Ngôn ngữ",
        rule: "Mọi quốc gia tận cùng bằng đuôi -ei đều mang giống cái (die). Dativ: aus/in der Türkei.",
        example: "Er kommt aus der Türkei und spricht Türkisch.",
        example_vi: "Anh ấy đến từ Thổ Nhĩ Kỳ và nói tiếng Thổ Nhĩ Kỳ."
    },
    {
        word: "Slowakei", article: "die", gender: "die", plural: "Ngôn ngữ: Slowakisch",
        indefinite: "in der Slowakei", negation: "aus der Slowakei",
        meaning: "Slovakia (Quốc gia có mạo từ die)", category: "Quốc gia & Ngôn ngữ",
        rule: "Đuôi -ei mang giống cái (die). Dativ: aus/in der Slowakei.",
        example: "Bratislava liegt in der Slowakei. Man spricht dort Slowakisch.",
        example_vi: "Bratislava nằm ở Slovakia. Ở đó người ta nói tiếng Slovakia."
    },
    {
        word: "Iran", article: "der", gender: "der", plural: "Ngôn ngữ: Persisch (Tiếng Ba Tư)",
        indefinite: "im (in dem) Iran", negation: "aus dem Iran",
        meaning: "Iran (Quốc gia có mạo từ der)", category: "Quốc gia & Ngôn ngữ",
        rule: "Quốc gia mang giống đực (der). Ở Dativ đổi thành 'aus dem Iran' và 'im Iran'. Ngôn ngữ là Persisch!",
        example: "Mein Kollege kommt aus dem Iran. Er spricht Persisch.",
        example_vi: "Đồng nghiệp của tôi đến từ Iran. Anh ấy nói tiếng Ba Tư."
    },
    {
        word: "USA", article: "die (Pl.)", gender: "die", plural: "Ngôn ngữ: Englisch",
        indefinite: "in den USA", negation: "aus den USA",
        meaning: "Hợp chủng quốc Hoa Kỳ - Mỹ (Số nhiều)", category: "Quốc gia & Ngôn ngữ",
        rule: "Danh từ số nhiều (Plural). Khi đi với 'aus' hoặc 'in' ở Dativ đổi thành 'aus den USA' / 'in den USA'.",
        example: "Die Lehrerin ist nett, sie kommt aus den USA.",
        example_vi: "Cô giáo rất tốt bụng, cô ấy đến từ nước Mỹ."
    },
    {
        word: "Niederlande", article: "die (Pl.)", gender: "die", plural: "Ngôn ngữ: Niederländisch",
        indefinite: "in den Niederlanden", negation: "aus den Niederlanden",
        meaning: "Hà Lan (Số nhiều)", category: "Quốc gia & Ngôn ngữ",
        rule: "Danh từ số nhiều (Plural). Dativ: in den Niederlanden / aus den Niederlanden.",
        example: "Amsterdam ist in den Niederlanden. Man spricht dort Niederländisch.",
        example_vi: "Amsterdam ở Hà Lan. Ở đó người ta nói tiếng Hà Lan."
    },

    // --- 6. BÀI 3: PHƯƠNG HƯỚNG & ĐỊNH HƯỚNG BẢN ĐỒ (HIMMELSRICHTUNGEN) ---
    {
        word: "Norden", article: "der", gender: "der", plural: "Tính từ: nördlich",
        indefinite: "im Norden von", negation: "nördlich von",
        meaning: "phía Bắc, miền Bắc (im Norden von + (nằm trong) / nördlich von + (nằm ngoài, phía bắc của))", category: "Phương hướng & Bản đồ",
        rule: "Mọi phương hướng đều mang giống đực (der). 'im Norden von' (nằm trong) vs. 'nördlich von' (nằm ngoài, phía bắc của).",
        example: "Wo liegt Hamburg? – Hamburg liegt im Norden von Deutschland (nördlich von Berlin).",
        example_vi: "Hamburg nằm ở đâu? – Hamburg nằm ở miền Bắc nước Đức (về phía Bắc của Berlin)."
    },
    {
        word: "Süden", article: "der", gender: "der", plural: "Tính từ: südlich",
        indefinite: "im Süden von", negation: "südlich von",
        meaning: "phía Nam, miền Nam (im Süden von + (nằm trong) / südlich von + (nằm ngoài, phía nam của))", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). 'im Süden von' (nằm trong) vs. 'südlich von' (nằm ngoài, phía nam của).",
        example: "Long An liegt im Süden von Vietnam (südwestlich von Ho-Chi-Minh-Stadt).",
        example_vi: "Long An nằm ở miền Nam của Việt Nam."
    },
    {
        word: "Osten", article: "der", gender: "der", plural: "Tính từ: östlich",
        indefinite: "im Osten von", negation: "östlich von",
        meaning: "phía Đông, miền Đông (im Osten von + (nằm trong) / östlich von + (nằm ngoài, phía đông của))", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). 'im Osten von' (nằm trong) vs. 'östlich von' (nằm ngoài, phía đông của). Tính từ: östlich.",
        example: "Berlin liegt im Osten von Deutschland (östlich von Magdeburg).",
        example_vi: "Berlin nằm ở phía Đông của nước Đức."
    },
    {
        word: "Westen", article: "der", gender: "der", plural: "Tính từ: westlich",
        indefinite: "im Westen von", negation: "westlich von",
        meaning: "phía Tây, miền Tây (im Westen von + (nằm trong) / westlich von + (nằm ngoài, phía tây của))", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). 'im Westen von' (nằm trong) vs. 'westlich von' (nằm ngoài, phía tây của). Tính từ: westlich.",
        example: "Köln liegt im Westen von Deutschland (westlich von Frankfurt).",
        example_vi: "Köln nằm ở phía Tây của nước Đức."
    },
    {
        word: "Nordosten", article: "der", gender: "der", plural: "Tính từ: nordöstlich",
        indefinite: "im Nordosten von", negation: "nordöstlich von",
        meaning: "phía Đông Bắc (im Nordosten von + (nằm trong) / nordöstlich von + (nằm ngoài, phía đông bắc của))", category: "Phương hướng & Bản đồ",
        rule: "Tiếng Đức đặt Bắc (Nord-) trước Đông (-osten). 'im Nordosten von' (nằm trong) vs. 'nordöstlich von' (nằm ngoài, phía đông bắc của).",
        example: "Hai Phong liegt im Nordosten von Vietnam (nordöstlich von Hanoi).",
        example_vi: "Hải Phòng nằm ở phía Đông Bắc của Việt Nam."
    },
    {
        word: "Südosten", article: "der", gender: "der", plural: "Tính từ: südöstlich",
        indefinite: "im Südosten von", negation: "südöstlich von",
        meaning: "phía Đông Nam (ghép Nam + Đông)", category: "Phương hướng & Bản đồ",
        rule: "Tiếng Đức đặt Nam (Süd-) trước Đông (-osten). Tính từ: südöstlich.",
        example: "Dresden liegt im Südosten von Deutschland.",
        example_vi: "Dresden nằm ở phía Đông Nam của nước Đức."
    },
    {
        word: "Nordwesten", article: "der", gender: "der", plural: "Tính từ: nordwestlich",
        indefinite: "im Nordwesten von", negation: "nordwestlich von",
        meaning: "phía Tây Bắc (ghép Bắc + Tây)", category: "Phương hướng & Bản đồ",
        rule: "Tiếng Đức đặt Bắc (Nord-) trước Tây (-westen). Tính từ: nordwestlich.",
        example: "Dien Bien liegt im Nordwesten von Vietnam.",
        example_vi: "Điện Biên nằm ở phía Tây Bắc của Việt Nam."
    },
    {
        word: "Südwesten", article: "der", gender: "der", plural: "Tính từ: südwestlich",
        indefinite: "im Südwesten von", negation: "südwestlich von",
        meaning: "phía Tây Nam (ghép Nam + Tây)", category: "Phương hướng & Bản đồ",
        rule: "Tiếng Đức đặt Nam (Süd-) trước Tây (-westen). Tính từ: südwestlich.",
        example: "Can Tho liegt im Südwesten von Vietnam.",
        example_vi: "Cần Thơ nằm ở phía Tây Nam của Việt Nam."
    },
    {
        word: "Mitte", article: "die", gender: "die", plural: "Cụm cố định: in der Mitte von",
        indefinite: "in der Mitte", negation: "Không có dạng -lich",
        meaning: "trung tâm, ở giữa, miền Trung", category: "Phương hướng & Bản đồ",
        rule: "Mang giống cái (die) nên khi đi với giới từ 'in' ở Dativ phải đổi thành 'in der Mitte von'.",
        example: "Wo liegt Da Nang? – Da Nang liegt in der Mitte von Vietnam.",
        example_vi: "Đà Nẵng nằm ở đâu? – Đà Nẵng nằm ở miền Trung của Việt Nam."
    },
    {
        word: "Landkarte", article: "die", gender: "die", plural: "die Landkarten",
        indefinite: "eine Landkarte", negation: "keine Landkarte",
        meaning: "bản đồ địa lý", category: "Phương hướng & Bản đồ",
        rule: "Danh từ ghép (das Land + die Karte) -> lấy giống cái theo từ cuối (die Karte).",
        example: "Wir sehen die Städte auf der Landkarte.",
        example_vi: "Chúng tôi xem các thành phố trên bản đồ địa lý."
    },
    {
        word: "Hausaufgabe", article: "die", gender: "die", plural: "die Hausaufgaben (thường dùng số nhiều)",
        indefinite: "eine Hausaufgabe", negation: "keine Hausaufgaben",
        meaning: "bài tập về nhà", category: "Đồ dùng lớp học",
        rule: "Danh từ ghép (das Haus + die Aufgabe) -> lấy giống cái (die), thường dùng ở dạng số nhiều không mạo từ: Hausaufgaben machen.",
        example: "Er macht Hausaufgaben. – Was macht er? / Macht er Hausaufgaben?",
        example_vi: "Anh ấy làm bài tập về nhà. – Anh ấy làm gì? / Anh ấy có làm bài tập về nhà không?"
    },

    // --- 7. BÀI 4: NHÀ Ở & CÁC PHÒNG (MENSCHEN UND HÄUSER) ---
    {
        word: "Garten", article: "der", gender: "der", plural: "die Gärten",
        indefinite: "ein Garten", negation: "kein Garten", akkusativ: "den / einen / keinen Garten",
        meaning: "khu vườn", category: "Nhà ở & Phòng ốc",
        rule: "Biến âm a -> ä ở số nhiều (die Gärten). Giống đực ở Akkusativ đổi thành den/einen/keinen Garten.",
        example: "Wir haben einen großen Garten. Ich finde den Garten sehr schön.",
        example_vi: "Chúng mình có một khu vườn lớn. Mình thấy khu vườn rất đẹp."
    },
    {
        word: "Balkon", article: "der", gender: "der", plural: "die Balkone",
        indefinite: "ein Balkon", negation: "kein Balkon", akkusativ: "den / einen / keinen Balkon",
        meaning: "ban công", category: "Nhà ở & Phòng ốc",
        rule: "Số nhiều thêm -e. Sau cấu trúc 'es gibt' (Akkusativ) đổi thành 'einen Balkon'.",
        example: "Oben gibt es einen Balkon.",
        example_vi: "Ở tầng trên có một cái ban công."
    },
    {
        word: "Flur", article: "der", gender: "der", plural: "die Flure",
        indefinite: "ein Flur", negation: "kein Flur", akkusativ: "den / einen / keinen Flur",
        meaning: "hành lang", category: "Nhà ở & Phòng ốc • Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Số nhiều thêm -e. Đại từ nhân xưng thay thế ở Nominativ là 'Er' (Er ist lang und dunkel).",
        example: "Das Haus hat einen Flur. Er ist lang und dunkel.",
        example_vi: "Ngôi nhà có một hành lang. Nó dài và tối."
    },
    {
        word: "Keller", article: "der", gender: "der", plural: "die Keller",
        indefinite: "ein Keller", negation: "kein Keller", akkusativ: "den / einen / keinen Keller",
        meaning: "tầng hầm", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -er giữ nguyên ở số nhiều. Akkusativ đổi thành: einen Keller / keinen Keller.",
        example: "Die Wohnung hat einen Keller.",
        example_vi: "Căn hộ có một tầng hầm."
    },
    {
        word: "Stock", article: "der", gender: "der", plural: "die Stockwerke",
        indefinite: "ein Stock", negation: "kein Stock", akkusativ: "den / einen / keinen Stock",
        meaning: "tầng lầu", category: "Nhà ở & Phòng ốc • Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Số nhiều dùng die Stockwerke (với nghĩa tầng lầu). Ghi chú: der erste Stock = lầu 1 (tầng 2 theo cách đếm Việt Nam); die Stöcke = những cây gậy (nghĩa khác).",
        example: "Meine Wohnung liegt im zweiten Stock.",
        example_vi: "Căn hộ của tôi nằm ở tầng hai."
    },
    {
        word: "Wohnung", article: "die", gender: "die", plural: "die Wohnungen",
        indefinite: "eine Wohnung", negation: "keine Wohnung", akkusativ: "die / eine / keine Wohnung",
        meaning: "căn hộ", category: "Nhà ở & Phòng ốc",
        rule: "Hậu tố -ung luôn mang giống cái (die) 100%, số nhiều thêm -en. Akkusativ giữ nguyên.",
        example: "Wir suchen eine neue Wohnung in Berlin.",
        example_vi: "Chúng mình đang tìm một căn hộ mới ở Berlin."
    },
    {
        word: "Garage", article: "die", gender: "die", plural: "die Garagen",
        indefinite: "eine Garage", negation: "keine Garage", akkusativ: "die / eine / keine Garage",
        meaning: "ga-ra ô tô, nhà để xe", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -e mang giống cái (die), số nhiều thêm -n. Mạo từ Akkusativ giữ nguyên.",
        example: "Das Haus hat eine große Garage.",
        example_vi: "Ngôi nhà có một ga-ra để xe rộng rãi."
    },
    {
        word: "Terrasse", article: "die", gender: "die", plural: "die Terrassen",
        indefinite: "eine Terrasse", negation: "keine Terrasse", akkusativ: "die / eine / keine Terrasse",
        meaning: "sân hiên, hiên nhà", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -e mang giống cái (die), số nhiều thêm -n.",
        example: "Im Sommer sitzen wir oft auf der Terrasse.",
        example_vi: "Vào mùa hè chúng tôi hay ngồi ngoài sân hiên."
    },
    {
        word: "Küche", article: "die", gender: "die", plural: "die Küchen",
        indefinite: "eine Küche", negation: "keine Küche", akkusativ: "die / eine / keine Küche",
        meaning: "nhà bếp, phòng bếp", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -e mang giống cái (die). Mạo từ sở hữu thêm đuôi -e: Meine Küche ist klein und schön.",
        example: "Ich finde die Küche zu klein.",
        example_vi: "Mình thấy căn bếp hơi quá nhỏ."
    },
    {
        word: "Toilette", article: "die", gender: "die", plural: "die Toiletten",
        indefinite: "eine Toilette", negation: "keine Toilette", akkusativ: "die / eine / keine Toilette",
        meaning: "nhà vệ sinh", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -e mang giống cái (die), số nhiều thêm -n (die Toiletten).",
        example: "Wo ist die Toilette, bitte?",
        example_vi: "Xin hỏi nhà vệ sinh ở đâu ạ?"
    },
    {
        word: "Haus", article: "das", gender: "das", plural: "die Häuser",
        indefinite: "ein Haus", negation: "kein Haus", akkusativ: "das / ein / kein Haus",
        meaning: "ngôi nhà", category: "Nhà ở & Phòng ốc",
        rule: "Số nhiều biến âm au -> äu và thêm đuôi -er (die Häuser). Giống trung ở Akkusativ giữ nguyên.",
        example: "Wir haben ein Haus. Unser Haus ist sehr alt.",
        example_vi: "Chúng mình có một ngôi nhà. Nhà của chúng mình rất cũ."
    },
    {
        word: "Wohnheim", article: "das", gender: "das", plural: "die Wohnheime",
        indefinite: "ein Wohnheim", negation: "kein Wohnheim", akkusativ: "das / ein / kein Wohnheim",
        meaning: "ký túc xá", category: "Nhà ở & Phòng ốc",
        rule: "Ghép wohnen + das Heim -> mang giống trung (das), số nhiều thêm -e.",
        example: "Lukas wohnt im Studentenwohnheim.",
        example_vi: "Lukas sống trong ký túc xá sinh viên."
    },
    {
        word: "Fenster", article: "das", gender: "das", plural: "die Fenster",
        indefinite: "ein Fenster", negation: "kein Fenster", akkusativ: "das / ein / kein Fenster",
        meaning: "cửa sổ", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -er giống trung, số nhiều giữ nguyên (die Fenster).",
        example: "Das Zimmer hat ein großes Fenster.",
        example_vi: "Căn phòng có một cửa sổ lớn."
    },
    {
        word: "Zimmer", article: "das", gender: "das", plural: "die Zimmer",
        indefinite: "ein Zimmer", negation: "kein Zimmer", akkusativ: "das / ein / kein Zimmer",
        meaning: "căn phòng", category: "Nhà ở & Phòng ốc",
        rule: "Đuôi -er giống trung, số nhiều giữ nguyên. Mọi phòng ghép với -zimmer đều là das!",
        example: "Unser Haus hat 5 Zimmer.",
        example_vi: "Ngôi nhà của chúng tôi có 5 phòng."
    },
    {
        word: "Wohnzimmer", article: "das", gender: "das", plural: "die Wohnzimmer",
        indefinite: "ein Wohnzimmer", negation: "kein Wohnzimmer", akkusativ: "das / ein / kein Wohnzimmer",
        meaning: "phòng khách", category: "Nhà ở & Phòng ốc",
        rule: "Ghép với das Zimmer -> luôn mang giống trung (das), số nhiều giữ nguyên. Đại từ thay thế là Es.",
        example: "Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher.",
        example_vi: "Phòng khách của tôi sáng và hiện đại. Nó có 1 Tivi."
    },
    {
        word: "Badezimmer", article: "das", gender: "das", plural: "die Badezimmer",
        indefinite: "ein Badezimmer", negation: "kein Badezimmer", akkusativ: "das / ein / kein Badezimmer",
        meaning: "phòng tắm (das Bad)", category: "Nhà ở & Phòng ốc",
        rule: "Ghép baden + das Zimmer -> giống trung (das). Viết gọn là das Bad (die Bäder).",
        example: "Das Badezimmer ist sehr sauber.",
        example_vi: "Phòng tắm rất sạch sẽ."
    },
    {
        word: "Schlafzimmer", article: "das", gender: "das", plural: "die Schlafzimmer",
        indefinite: "ein Schlafzimmer", negation: "kein Schlafzimmer", akkusativ: "das / ein / kein Schlafzimmer",
        meaning: "phòng ngủ", category: "Nhà ở & Phòng ốc",
        rule: "Ghép schlafen + das Zimmer -> giống trung (das), số nhiều giữ nguyên.",
        example: "Mein Schlafzimmer ist gemütlich und hat ein Bett.",
        example_vi: "Phòng ngủ của tôi thì ấm cúng và có 1 giường."
    },
    {
        word: "Esszimmer", article: "das", gender: "das", plural: "die Esszimmer",
        indefinite: "ein Esszimmer", negation: "kein Esszimmer", akkusativ: "das / ein / kein Esszimmer",
        meaning: "phòng ăn", category: "Nhà ở & Phòng ốc",
        rule: "Ghép essen + das Zimmer -> giống trung (das).",
        example: "Wir essen zusammen im Esszimmer.",
        example_vi: "Chúng tôi ăn cùng nhau trong phòng ăn."
    },
    {
        word: "Arbeitszimmer", article: "das", gender: "das", plural: "die Arbeitszimmer",
        indefinite: "ein Arbeitszimmer", negation: "kein Arbeitszimmer", akkusativ: "das / ein / kein Arbeitszimmer",
        meaning: "phòng làm việc", category: "Nhà ở & Phòng ốc",
        rule: "Ghép die Arbeit + s + das Zimmer -> giống trung (das). Đại từ thay thế là Es.",
        example: "Mein Arbeitszimmer ist klein, aber hell. Es hat einen Tisch und einen Stuhl.",
        example_vi: "Phòng làm việc của tôi nhỏ nhưng sáng. Nó có 1 bàn và 1 ghế."
    },
    {
        word: "Kinderzimmer", article: "das", gender: "das", plural: "die Kinderzimmer",
        indefinite: "ein Kinderzimmer", negation: "kein Kinderzimmer", akkusativ: "das / ein / kein Kinderzimmer",
        meaning: "phòng trẻ em", category: "Nhà ở & Phòng ốc",
        rule: "Ghép die Kinder + das Zimmer -> giống trung (das).",
        example: "Das Kinderzimmer ist bunt und schön.",
        example_vi: "Phòng trẻ em rực rỡ và đẹp."
    },

    // --- 8. BÀI 4: NỘI THẤT & ĐỒ ĐẠC (MÖBEL & EINRICHTUNG) ---
    {
        word: "Schrank", article: "der", gender: "der", plural: "die Schränke",
        indefinite: "ein Schrank", negation: "kein Schrank", akkusativ: "den / einen / keinen Schrank",
        meaning: "cái tủ (tủ quần áo)", category: "Nội thất & Đồ đạc",
        rule: "Số nhiều thêm Umlaut a -> ä và -e. Sau động từ haben/kaufen (Akkusativ) đổi thành: einen Schrank.",
        example: "Er kauft einen neuen Schrank für das Schlafzimmer.",
        example_vi: "Anh ấy mua một cái tủ mới cho phòng ngủ."
    },
    {
        word: "Kühlschrank", article: "der", gender: "der", plural: "die Kühlschränke",
        indefinite: "ein Kühlschrank", negation: "kein Kühlschrank", akkusativ: "den / einen / keinen Kühlschrank",
        meaning: "tủ lạnh", category: "Nội thất & Đồ đạc",
        rule: "Ghép kühl + der Schrank -> giống đực (der). Akkusativ: einen Kühlschrank.",
        example: "Die Küche hat einen modernen Kühlschrank.",
        example_vi: "Nhà bếp có một chiếc tủ lạnh hiện đại."
    },
    {
        word: "Teppich", article: "der", gender: "der", plural: "die Teppiche",
        indefinite: "ein Teppich", negation: "kein Teppich", akkusativ: "den / einen / keinen Teppich",
        meaning: "tấm thảm", category: "Nội thất & Đồ đạc",
        rule: "Hậu tố -ich luôn mang giống đực (der). Số nhiều thêm -e. Akkusativ: einen Teppich.",
        example: "Im Wohnzimmer liegt ein schöner Teppich.",
        example_vi: "Trong phòng khách có trải một tấm thảm đẹp."
    },
    {
        word: "Spiegel", article: "der", gender: "der", plural: "die Spiegel",
        indefinite: "ein Spiegel", negation: "kein Spiegel", akkusativ: "den / einen / keinen Spiegel",
        meaning: "cái gương", category: "Nội thất & Đồ đạc",
        rule: "Tận cùng -el, số nhiều giữ nguyên. Akkusativ: einen Spiegel.",
        example: "Das Bad hat einen großen Spiegel.",
        example_vi: "Phòng tắm có một chiếc gương lớn."
    },
    {
        word: "Fernseher", article: "der", gender: "der", plural: "die Fernseher",
        indefinite: "ein Fernseher", negation: "kein Fernseher", akkusativ: "den / einen / keinen Fernseher",
        meaning: "Tivi (máy truyền hình)", category: "Nội thất & Đồ đạc",
        rule: "Tận cùng -er chỉ thiết bị mang giống đực (der). Akkusativ đổi thành: einen Fernseher.",
        example: "Mein Wohnzimmer hat einen Fernseher und ein Bücherregal.",
        example_vi: "Phòng khách của tôi có 1 chiếc Tivi và 1 giá sách."
    },
    {
        word: "Lampe", article: "die", gender: "die", plural: "die Lampen",
        indefinite: "eine Lampe", negation: "keine Lampe", akkusativ: "die / eine / keine Lampe",
        meaning: "cái đèn", category: "Nội thất & Đồ đạc",
        rule: "Tận cùng -e mang giống cái (die), số nhiều thêm -n. Akkusativ giữ nguyên.",
        example: "Auf dem Schreibtisch steht eine Lampe.",
        example_vi: "Trên bàn làm việc có một cái đèn."
    },
    {
        word: "Spüle", article: "die", gender: "die", plural: "die Spülen",
        indefinite: "eine Spüle", negation: "keine Spüle", akkusativ: "die / eine / keine Spüle",
        meaning: "bồn rửa bát", category: "Nội thất & Đồ đạc",
        rule: "Đuôi -e mang giống cái (die), số nhiều thêm -n.",
        example: "Die Küche hat eine Spüle und einen Herd.",
        example_vi: "Nhà bếp có một bồn rửa bát và một cái bếp."
    },
    {
        word: "Bett", article: "das", gender: "das", plural: "die Betten",
        indefinite: "ein Bett", negation: "kein Bett", akkusativ: "das / ein / kein Bett",
        meaning: "cái giường", category: "Nội thất & Đồ đạc",
        rule: "Ngoại lệ số nhiều của giống trung thêm -en: die Betten. Akkusativ giữ nguyên ein Bett.",
        example: "Mein Schlafzimmer hat ein bequemes Bett.",
        example_vi: "Phòng ngủ của tôi có một chiếc giường êm ái."
    },
    {
        word: "Regal", article: "das", gender: "das", plural: "die Regale",
        indefinite: "ein Regal", negation: "kein Regal", akkusativ: "das / ein / kein Regal",
        meaning: "cái giá, cái kệ", category: "Nội thất & Đồ đạc",
        rule: "Giống trung (das), số nhiều thêm -e (die Regale).",
        example: "Das Arbeitszimmer hat ein weißes Regal.",
        example_vi: "Phòng làm việc có một cái kệ màu trắng."
    },
    {
        word: "Bücherregal", article: "das", gender: "das", plural: "die Bücherregale",
        indefinite: "ein Bücherregal", negation: "kein Bücherregal", akkusativ: "das / ein / kein Bücherregal",
        meaning: "giá sách, kệ sách", category: "Nội thất & Đồ đạc",
        rule: "Ghép die Bücher + das Regal -> lấy giống theo das Regal. Akkusativ giữ nguyên ein Bücherregal.",
        example: "Das Wohnzimmer hat einen Fernseher und ein Bücherregal.",
        example_vi: "Phòng khách có 1 Tivi và 1 giá sách."
    },
    // --- 11. THỜI GIAN, THỨ, THÁNG & LỊCH TRÌNH (BÀI 5) ---
    {
        word: "Sekunde", article: "die", gender: "die", plural: "die Sekunden",
        indefinite: "eine Sekunde", negation: "keine Sekunde",
        meaning: "giây", category: "Thời gian & Lịch trình",
        rule: "Đơn vị thời gian nhỏ mang giống cái (die), số nhiều thêm -n.",
        example: "Eine Minute hat sechzig Sekunden.",
        example_vi: "Một phút có sáu mươi giây."
    },
    {
        word: "Minute", article: "die", gender: "die", plural: "die Minuten",
        indefinite: "eine Minute", negation: "keine Minute",
        meaning: "phút", category: "Thời gian & Lịch trình",
        rule: "Đơn vị thời gian kết thúc đuôi -e mang giống cái (die), số nhiều thêm -n.",
        example: "Der Bus kommt in fünf Minuten.",
        example_vi: "Xe buýt sẽ đến trong năm phút nữa."
    },
    {
        word: "Stunde", article: "die", gender: "die", plural: "die Stunden",
        indefinite: "eine Stunde", negation: "keine Stunde",
        meaning: "tiếng, giờ đồng hồ (thời lượng)", category: "Thời gian & Lịch trình",
        rule: "Chỉ thời lượng/khoảng thời gian. Số nhiều thêm -n (die Stunden).",
        example: "Heute arbeite ich acht Stunden.",
        example_vi: "Hôm nay tôi làm việc tám tiếng đồng hồ."
    },
    {
        word: "Tag", article: "der", gender: "der", plural: "die Tage",
        indefinite: "ein Tag", negation: "kein Tag",
        meaning: "ngày", category: "Thời gian & Lịch trình",
        rule: "Danh từ giống đực (der Tag), số nhiều thêm -e (die Tage).",
        example: "Ein Tag hat vierundzwanzig Stunden.",
        example_vi: "Một ngày có hai mươi tư tiếng đồng hồ."
    },
    {
        word: "Woche", article: "die", gender: "die", plural: "die Wochen",
        indefinite: "eine Woche", negation: "keine Woche",
        meaning: "tuần", category: "Thời gian & Lịch trình",
        rule: "Danh từ kết thúc đuôi -e mang giống cái (die), số nhiều thêm -n.",
        example: "Eine Woche hat sieben Tage.",
        example_vi: "Một tuần có bảy ngày."
    },
    {
        word: "Wochenende", article: "das", gender: "das", plural: "die Wochenenden",
        indefinite: "ein Wochenende", negation: "kein Wochenende",
        meaning: "cuối tuần", category: "Thời gian & Lịch trình",
        rule: "Ghép die Woche + das Ende -> lấy giống theo das Ende. Đi với am Wochenende.",
        example: "Am Wochenende arbeite ich nicht.",
        example_vi: "Vào cuối tuần tôi không làm việc."
    },
    {
        word: "Monat", article: "der", gender: "der", plural: "die Monate",
        indefinite: "ein Monat", negation: "kein Monat",
        meaning: "tháng", category: "Thời gian & Lịch trình",
        rule: "Danh từ giống đực (der Monat), số nhiều thêm -e (die Monate).",
        example: "Ein Monat hat dreißig oder einunddreißig Tage.",
        example_vi: "Một tháng có ba mươi hoặc ba mươi mốt ngày."
    },
    {
        word: "Jahr", article: "das", gender: "das", plural: "die Jahre",
        indefinite: "ein Jahr", negation: "kein Jahr",
        meaning: "năm", category: "Thời gian & Lịch trình",
        rule: "Danh từ giống trung (das Jahr), số nhiều thêm -e (die Jahre).",
        example: "Ein Jahr hat zwölf Monate.",
        example_vi: "Một năm có mười hai tháng."
    },
    {
        word: "Uhr", article: "die", gender: "die", plural: "die Uhren",
        indefinite: "eine Uhr", negation: "keine Uhr",
        meaning: "đồng hồ / giờ (mốc thời gian)", category: "Thời gian & Lịch trình",
        rule: "Dùng để nói mốc giờ trên đồng hồ (Es ist 8 Uhr) hoặc cái đồng hồ. Số nhiều thêm -en.",
        example: "Es ist acht Uhr.",
        example_vi: "Bây giờ là tám giờ đúng."
    },
    {
        word: "Montag", article: "der", gender: "der", plural: "die Montage",
        indefinite: "ein Montag", negation: "kein Montag",
        meaning: "thứ Hai", category: "Thời gian & Lịch trình",
        rule: "Tất cả các thứ trong tuần đều mang giống đực (der) và đi với am.",
        example: "Am Montag beginnt meine Arbeitswoche.",
        example_vi: "Vào thứ Hai tuần làm việc của tôi bắt đầu."
    },
    {
        word: "Dienstag", article: "der", gender: "der", plural: "die Dienstage",
        indefinite: "ein Dienstag", negation: "kein Dienstag",
        meaning: "thứ Ba", category: "Thời gian & Lịch trình",
        rule: "Thứ trong tuần mang giống đực (der), đi với am Dienstag.",
        example: "Am Dienstag habe ich einen Deutschkurs.",
        example_vi: "Vào thứ Ba tôi có một khóa học tiếng Đức."
    },
    {
        word: "Mittwoch", article: "der", gender: "der", plural: "die Mittwoche",
        indefinite: "ein Mittwoch", negation: "kein Mittwoch",
        meaning: "thứ Tư", category: "Thời gian & Lịch trình",
        rule: "Thứ trong tuần mang giống đực (der), đi với am Mittwoch.",
        example: "Am Mittwoch mache ich um 17 Uhr Sport.",
        example_vi: "Vào thứ Tư tôi tập thể thao lúc 17 giờ."
    },
    {
        word: "Donnerstag", article: "der", gender: "der", plural: "die Donnerstage",
        indefinite: "ein Donnerstag", negation: "kein Donnerstag",
        meaning: "thứ Năm", category: "Thời gian & Lịch trình",
        rule: "Thứ trong tuần mang giống đực (der), đi với am Donnerstag.",
        example: "Am Donnerstag kauft Anna im Supermarkt ein.",
        example_vi: "Vào thứ Năm Anna đi mua sắm ở siêu thị."
    },
    {
        word: "Freitag", article: "der", gender: "der", plural: "die Freitage",
        indefinite: "ein Freitag", negation: "kein Freitag",
        meaning: "thứ Sáu", category: "Thời gian & Lịch trình",
        rule: "Thứ trong tuần mang giống đực (der), đi với am Freitag.",
        example: "Am Freitag um 20 Uhr gehe ich aus.",
        example_vi: "Vào thứ Sáu lúc 20 giờ tôi đi chơi."
    },
    {
        word: "Samstag", article: "der", gender: "der", plural: "die Samstage",
        indefinite: "ein Samstag", negation: "kein Samstag",
        meaning: "thứ Bảy", category: "Thời gian & Lịch trình",
        rule: "Thứ trong tuần mang giống đực (der), đi với am Samstag.",
        example: "Am Samstag treffen wir unsere Freunde.",
        example_vi: "Vào thứ Bảy chúng tôi gặp gỡ bạn bè của mình."
    },
    {
        word: "Sonntag", article: "der", gender: "der", plural: "die Sonntage",
        indefinite: "ein Sonntag", negation: "kein Sonntag",
        meaning: "Chủ nhật", category: "Thời gian & Lịch trình",
        rule: "Thứ trong tuần mang giống đực (der), đi với am Sonntag.",
        example: "Am Sonntag stehe ich um 8 Uhr auf.",
        example_vi: "Vào Chủ nhật tôi thức dậy lúc 8 giờ."
    },
    {
        word: "Morgen", article: "der", gender: "der", plural: "die Morgen",
        indefinite: "ein Morgen", negation: "kein Morgen",
        meaning: "buổi sáng sớm (06:00 – 10:00)", category: "Thời gian & Lịch trình",
        rule: "Buổi trong ngày mang giống đực (der), đi với am Morgen.",
        example: "Am Morgen trinke ich gern eine Tasse Kaffee.",
        example_vi: "Vào buổi sáng tôi thích uống một tách cà phê."
    },
    {
        word: "Vormittag", article: "der", gender: "der", plural: "die Vormittage",
        indefinite: "ein Vormittag", negation: "kein Vormittag",
        meaning: "buổi sáng trước trưa (10:00 – 12:00)", category: "Thời gian & Lịch trình",
        rule: "Buổi trong ngày mang giống đực (der), đi với am Vormittag.",
        example: "Am Vormittag arbeite ich im Büro.",
        example_vi: "Vào buổi sáng trước trưa tôi làm việc ở văn phòng."
    },
    {
        word: "Mittag", article: "der", gender: "der", plural: "die Mittage",
        indefinite: "ein Mittag", negation: "kein Mittag",
        meaning: "buổi trưa (12:00 – 14:00)", category: "Thời gian & Lịch trình",
        rule: "Buổi trong ngày mang giống đực (der), đi với am Mittag.",
        example: "Am Mittag mache ich um 12 Uhr Mittagspause.",
        example_vi: "Vào buổi trưa tôi nghỉ trưa lúc 12 giờ."
    },
    {
        word: "Nachmittag", article: "der", gender: "der", plural: "die Nachmittage",
        indefinite: "ein Nachmittag", negation: "kein Nachmittag",
        meaning: "buổi chiều (14:00 – 18:00)", category: "Thời gian & Lịch trình",
        rule: "Buổi trong ngày mang giống đực (der), đi với am Nachmittag.",
        example: "Am Nachmittag trinken wir Tee und lesen ein Buch.",
        example_vi: "Vào buổi chiều chúng tôi uống trà và đọc một quyển sách."
    },
    {
        word: "Abend", article: "der", gender: "der", plural: "die Abende",
        indefinite: "ein Abend", negation: "kein Abend",
        meaning: "buổi tối (18:00 – 22:00)", category: "Thời gian & Lịch trình",
        rule: "Buổi trong ngày mang giống đực (der), đi với am Abend.",
        example: "Am Abend sehe ich mit meiner Familie fern.",
        example_vi: "Vào buổi tối tôi xem tivi cùng gia đình mình."
    },
    {
        word: "Nacht", article: "die", gender: "die", plural: "die Nächte",
        indefinite: "eine Nacht", negation: "keine Nacht",
        meaning: "ban đêm (22:00 – 06:00)", category: "Thời gian & Lịch trình",
        rule: "Ngoại lệ: mang giống cái (die Nacht) nên bắt buộc đi với in der Nacht (không dùng am Nacht).",
        example: "In der Nacht schlafe ich acht Stunden.",
        example_vi: "Vào ban đêm tôi ngủ tám tiếng đồng hồ."
    },
    {
        word: "Januar", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Januar", negation: "kein Januar",
        meaning: "tháng Một", category: "Thời gian & Lịch trình",
        rule: "Tất cả 12 tháng đều mang giống đực (der) và đi với giới từ im.",
        example: "Im Januar ist es in Deutschland sehr kalt.",
        example_vi: "Vào tháng Một trời ở Đức rất lạnh."
    },
    {
        word: "Februar", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Februar", negation: "kein Februar",
        meaning: "tháng Hai", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im Februar.",
        example: "Im Februar hat der Monat nur 28 oder 29 Tage.",
        example_vi: "Vào tháng Hai tháng chỉ có 28 hoặc 29 ngày."
    },
    {
        word: "März", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein März", negation: "kein März",
        meaning: "tháng Ba", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im März.",
        example: "Im März beginnt der Frühling.",
        example_vi: "Vào tháng Ba mùa xuân bắt đầu."
    },
    {
        word: "April", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein April", negation: "kein April",
        meaning: "tháng Tư", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im April.",
        example: "Mein Bruder hat im April Geburtstag.",
        example_vi: "Anh trai tôi có sinh nhật vào tháng Tư."
    },
    {
        word: "Mai", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Mai", negation: "kein Mai",
        meaning: "tháng Năm", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im Mai.",
        example: "Im Mai ist das Wetter in Berlin sehr schön.",
        example_vi: "Vào tháng Năm thời tiết ở Berlin rất đẹp."
    },
    {
        word: "Juni", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Juni", negation: "kein Juni",
        meaning: "tháng Sáu", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im Juni.",
        example: "Im Juni fahren wir nach Italien.",
        example_vi: "Vào tháng Sáu chúng tôi đi sang Ý."
    },
    {
        word: "Juli", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Juli", negation: "kein Juli",
        meaning: "tháng Bảy", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im Juli.",
        example: "Im Juli haben die Studenten Sommerferien.",
        example_vi: "Vào tháng Bảy các sinh viên có kỳ nghỉ hè."
    },
    {
        word: "August", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein August", negation: "kein August",
        meaning: "tháng Tám", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im August.",
        example: "Im August ist es in Vietnam oft heiß.",
        example_vi: "Vào tháng Tám trời ở Việt Nam thường nóng."
    },
    {
        word: "September", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein September", negation: "kein September",
        meaning: "tháng Chín", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im September.",
        example: "Im September beginnt mein Studium.",
        example_vi: "Vào tháng Chín việc học đại học của tôi bắt đầu."
    },
    {
        word: "Oktober", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Oktober", negation: "kein Oktober",
        meaning: "tháng Mười", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im Oktober.",
        example: "Im Oktober ist der Herbst rất đẹp.",
        example_vi: "Vào tháng Mười mùa thu rất đẹp."
    },
    {
        word: "November", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein November", negation: "kein November",
        meaning: "tháng Mười Một", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im November.",
        example: "Im November arbeite ich viel.",
        example_vi: "Vào tháng Mười Một tôi làm việc nhiều."
    },
    {
        word: "Dezember", article: "der", gender: "der", plural: "kein Plural (Plural selten)",
        indefinite: "ein Dezember", negation: "kein Dezember",
        meaning: "tháng Mười Hai", category: "Thời gian & Lịch trình",
        rule: "Tháng trong năm mang giống đực (der), đi với im Dezember.",
        example: "Im Dezember ist Weihnachten.",
        example_vi: "Vào tháng Mười Hai là lễ Giáng sinh."
    },
    {
        word: "Termin", article: "der", gender: "der", plural: "die Termine",
        indefinite: "ein Termin", negation: "kein Termin", akkusativ: "den / einen / keinen Termin",
        meaning: "cuộc hẹn, lịch hẹn", category: "Thời gian & Lịch trình",
        rule: "Danh từ giống đực (der Termin), số nhiều thêm -e. Sau haben đổi sang Akkusativ: einen Termin.",
        example: "Ich habe einen Termin um zehn Uhr.",
        example_vi: "Tôi có một cuộc hẹn vào lúc mười giờ."
    },
    {
        word: "Mittagspause", article: "die", gender: "die", plural: "die Mittagspausen",
        indefinite: "eine Mittagspause", negation: "keine Mittagspause",
        meaning: "giờ nghỉ trưa", category: "Thời gian & Lịch trình",
        rule: "Ghép der Mittag + die Pause -> mang giống cái (die). Đi với cụm Mittagspause machen.",
        example: "Um zwölf Uhr mache ich Mittagspause.",
        example_vi: "Vào lúc mười hai giờ tôi nghỉ trưa."
    },
    {
        word: "Panne", article: "die", gender: "die", plural: "die Pannen",
        indefinite: "eine Panne", negation: "keine Panne",
        meaning: "sự cố hỏng xe dọc đường", category: "Thời gian & Lịch trình",
        rule: "Danh từ giống cái (die Panne). Cụm cố định: eine Panne haben (gặp sự cố).",
        example: "Wir hatten gestern eine Panne.",
        example_vi: "Hôm qua chúng tôi đã gặp một sự cố hỏng xe."
    },
    {
        word: "Zeit", article: "die", gender: "die", plural: "die Zeiten",
        indefinite: "eine Zeit", negation: "keine Zeit",
        meaning: "thời gian", category: "Thời gian & Lịch trình",
        rule: "Danh từ giống cái (die Zeit). Thường dùng: keine Zeit haben (không có thời gian).",
        example: "Gestern hatte ich keine Zeit.",
        example_vi: "Hôm qua tôi đã không có thời gian."
    },
    {
        word: "Bus", article: "der", gender: "der", plural: "die Busse",
        indefinite: "ein Bus", negation: "kein Bus",
        meaning: "xe buýt", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Bus), số nhiều die Busse. Đi bằng xe buýt dùng mit dem Bus.",
        example: "Mein Bruder fährt jeden Tag mit dem Bus zur Arbeit.",
        example_vi: "Anh trai tôi đi làm mỗi ngày bằng xe buýt."
    },
    {
        word: "Zug", article: "der", gender: "der", plural: "die Züge",
        indefinite: "ein Zug", negation: "kein Zug",
        meaning: "tàu hỏa", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Zug), số nhiều biến âm u -> ü (die Züge). Đi bằng tàu hỏa dùng mit dem Zug.",
        example: "Der Zug fährt um acht Uhr am Bahnhof ab.",
        example_vi: "Chuyến tàu khởi hành lúc 8 giờ tại nhà ga."
    },
    {
        word: "Wagen", article: "der", gender: "der", plural: "die Wagen",
        indefinite: "ein Wagen", negation: "kein Wagen",
        meaning: "xe hơi, ô tô cá nhân", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Wagen). Đi bằng xe hơi dùng mit seinem Wagen.",
        example: "Herr Müller fährt mit seinem Wagen ins Büro.",
        example_vi: "Ông Müller lái chiếc xe hơi của ông ấy đến văn phòng."
    },
    {
        word: "U-Bahn", article: "die", gender: "die", plural: "die U-Bahnen",
        indefinite: "eine U-Bahn", negation: "keine U-Bahn",
        meaning: "tàu điện ngầm", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die U-Bahn). Đi bằng tàu điện ngầm dùng mit der U-Bahn.",
        example: "In Berlin fahren wir immer mit der U-Bahn.",
        example_vi: "Ở Berlin chúng tôi luôn đi bằng tàu điện ngầm."
    },
    {
        word: "S-Bahn", article: "die", gender: "die", plural: "die S-Bahnen",
        indefinite: "eine S-Bahn", negation: "keine S-Bahn",
        meaning: "tàu điện nhanh đô thị", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die S-Bahn). Đi bằng tàu điện đô thị dùng mit der S-Bahn.",
        example: "Vom Flughafen fährt der Tourist mit der S-Bahn ins Stadtzentrum.",
        example_vi: "Từ sân bay vị khách du lịch đi bằng tàu điện đô thị vào trung tâm thành phố."
    },
    {
        word: "Straßenbahn", article: "die", gender: "die", plural: "die Straßenbahnen",
        indefinite: "eine Straßenbahn", negation: "keine Straßenbahn",
        meaning: "tàu điện mặt đất", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Straßenbahn). Đi bằng tàu điện mặt đất dùng mit der Straßenbahn.",
        example: "Am Wochenende fahren unsere Großeltern mit der Straßenbahn zum Markt.",
        example_vi: "Vào cuối tuần ông bà của chúng tôi đi bằng tàu điện mặt đất ra chợ."
    },
    {
        word: "Fähre", article: "die", gender: "die", plural: "die Fähren",
        indefinite: "eine Fähre", negation: "keine Fähre",
        meaning: "phà", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Fähre). Đi bằng phà dùng mit der Fähre.",
        example: "Wir fahren mit der Fähre auf die Insel.",
        example_vi: "Chúng tôi đi bằng phà ra đảo."
    },
    {
        word: "Auto", article: "das", gender: "das", plural: "die Autos",
        indefinite: "ein Auto", negation: "kein Auto",
        meaning: "ô tô, xe hơi", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Auto). Đi bằng ô tô dùng mit dem Auto.",
        example: "Am Sonntag fahren unsere Nachbarn mit dem Auto ans Meer.",
        example_vi: "Vào Chủ nhật những người hàng xóm của chúng tôi đi bằng ô tô ra biển."
    },
    {
        word: "Fahrrad", article: "das", gender: "das", plural: "die Fahrräder",
        indefinite: "ein Fahrrad", negation: "kein Fahrrad",
        meaning: "xe đạp", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Fahrrad), số nhiều die Fahrräder. Đi bằng xe đạp dùng mit dem Fahrrad.",
        example: "Bei schönem Wetter fährt sie mit dem Fahrrad zur Schule.",
        example_vi: "Khi thời tiết đẹp cô ấy đi xe đạp tới trường."
    },
    {
        word: "Motorrad", article: "das", gender: "das", plural: "die Motorräder",
        indefinite: "ein Motorrad", negation: "kein Motorrad",
        meaning: "xe mô tô", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Motorrad). Đi bằng xe máy/mô tô dùng mit dem Motorrad.",
        example: "In Vietnam fahren viele Menschen mit dem Motorrad zur Arbeit.",
        example_vi: "Ở Việt Nam nhiều người đi làm bằng xe mô tô."
    },
    {
        word: "Taxi", article: "das", gender: "das", plural: "die Taxis",
        indefinite: "ein Taxi", negation: "kein Taxi",
        meaning: "xe taxi", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Taxi). Đi bằng taxi dùng mit dem Taxi.",
        example: "Wir fahren mit dem Taxi nach Hause.",
        example_vi: "Chúng tôi đi bằng taxi về nhà."
    },
    {
        word: "Flugzeug", article: "das", gender: "das", plural: "die Flugzeuge",
        indefinite: "ein Flugzeug", negation: "kein Flugzeug",
        meaning: "máy bay", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Flugzeug). Bay bằng máy bay dùng mit dem Flugzeug fliegen.",
        example: "Im August fliegen wir mit dem Flugzeug nach Deutschland.",
        example_vi: "Vào tháng Tám chúng tôi bay bằng máy bay sang Đức."
    },
    {
        word: "Schiff", article: "das", gender: "das", plural: "die Schiffe",
        indefinite: "ein Schiff", negation: "kein Schiff",
        meaning: "tàu thủy lớn", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Schiff). Đi bằng tàu thủy dùng mit dem Schiff fahren.",
        example: "Die Touristen machen eine Reise mit dem Schiff.",
        example_vi: "Những du khách thực hiện một chuyến du hành bằng tàu thủy."
    },
    {
        word: "Fuß", article: "der", gender: "der", plural: "die Füße",
        indefinite: "ein Fuß", negation: "kein Fuß",
        meaning: "bàn chân (đi bộ)", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Ngoại lệ đi bộ trong tiếng Đức dùng cụm cố định zu Fuß gehen.",
        example: "Die Schule ist gleich neben meinem Haus, deshalb gehe ich immer zu Fuß.",
        example_vi: "Ngôi trường ở ngay cạnh nhà tôi, vì vậy tôi luôn đi bộ."
    },
    {
        word: "Bahnhof", article: "der", gender: "der", plural: "die Bahnhöfe",
        indefinite: "ein Bahnhof", negation: "kein Bahnhof",
        meaning: "nhà ga xe lửa", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Bahnhof). Đến nhà ga dùng zum Bahnhof, tại nhà ga dùng am Bahnhof.",
        example: "Wie komme ich vom Hauptbahnhof zum Stadtmuseum?",
        example_vi: "Tôi đi từ nhà ga trung tâm đến bảo tàng thành phố bằng cách nào?"
    },
    {
        word: "Flughafen", article: "der", gender: "der", plural: "die Flughäfen",
        indefinite: "ein Flughafen", negation: "kein Flughafen",
        meaning: "sân bay", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Flughafen). Đến sân bay dùng zum Flughafen, từ sân bay về dùng vom Flughafen.",
        example: "Wann kommt deine Schwester heute Abend vom Flughafen zurück?",
        example_vi: "Tối nay khi nào chị gái của bạn từ sân bay trở về?"
    },
    {
        word: "Haltestelle", article: "die", gender: "die", plural: "die Haltestellen",
        indefinite: "eine Haltestelle", negation: "keine Haltestelle",
        meaning: "trạm dừng (xe buýt/tàu)", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Haltestelle). Tại trạm dừng dùng an der Haltestelle.",
        example: "Wann kommt der Bus an der Haltestelle an?",
        example_vi: "Khi nào xe buýt đến trạm dừng?"
    },
    {
        word: "Parkplatz", article: "der", gender: "der", plural: "die Parkplätze",
        indefinite: "ein Parkplatz", negation: "kein Parkplatz",
        meaning: "bãi đỗ xe", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Parkplatz). Phía sau bệnh viện dùng hinter dem Krankenhaus.",
        example: "Der große Parkplatz liegt direkt hinter dem Krankenhaus.",
        example_vi: "Bãi đỗ xe lớn nằm ngay phía sau bệnh viện."
    },
    {
        word: "Markt", article: "der", gender: "der", plural: "die Märkte",
        indefinite: "ein Markt", negation: "kein Markt",
        meaning: "khu chợ", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Markt). Ra chợ dùng zum Markt hoặc auf dem Markt.",
        example: "Meine Großeltern fahren gern mit der Straßenbahn zum Markt.",
        example_vi: "Ông bà tôi thích đi bằng tàu điện mặt đất ra chợ."
    },
    {
        word: "Park", article: "der", gender: "der", plural: "die Parks",
        indefinite: "ein Park", negation: "kein Park",
        meaning: "công viên", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống đực (der Park). Ở trong công viên dùng im Park.",
        example: "Am Sonntag spielen die Kinder im Park mit ihren Freunden.",
        example_vi: "Vào Chủ nhật bọn trẻ chơi ở trong công viên với những người bạn của chúng."
    },
    {
        word: "Bank", article: "die", gender: "die", plural: "die Banken",
        indefinite: "eine Bank", negation: "keine Bank",
        meaning: "ngân hàng", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Bank). Đến ngân hàng dùng zur Bank, làm việc ở ngân hàng dùng bei einer Bank.",
        example: "Frau Bui arbeitet bei einer Bank in Berlin.",
        example_vi: "Bà Bùi làm việc tại một ngân hàng ở Berlin."
    },
    {
        word: "Post", article: "die", gender: "die", plural: "kein Plural (die Postämter = các bưu điện)",
        indefinite: "eine Post", negation: "keine Post",
        meaning: "bưu điện", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Post). Không dùng số nhiều (hoặc dùng die Postämter = các bưu điện). Đến bưu điện dùng zur Post, bên cạnh bưu điện dùng neben der Post.",
        example: "Wie komme ich zum Bahnhof und zur Post?",
        example_vi: "Tôi đi đến nhà ga và bưu điện bằng cách nào?"
    },
    {
        word: "Bibliothek", article: "die", gender: "die", plural: "die Bibliotheken",
        indefinite: "eine Bibliothek", negation: "keine Bibliothek",
        meaning: "thư viện", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Bibliothek). Đi bộ đến thư viện dùng zu Fuß zur Bibliothek.",
        example: "Morgen gehen wir zu Fuß zur Bibliothek.",
        example_vi: "Ngày mai chúng tôi đi bộ đến thư viện."
    },
    {
        word: "Buchhandlung", article: "die", gender: "die", plural: "die Buchhandlungen",
        indefinite: "eine Buchhandlung", negation: "keine Buchhandlung",
        meaning: "hiệu sách", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Buchhandlung). Giữa hiệu sách và rạp phim dùng zwischen der Buchhandlung und dem Kino.",
        example: "Das Café liegt direkt zwischen der Buchhandlung und dem Kino.",
        example_vi: "Quán cà phê nằm ngay giữa hiệu sách và rạp chiếu phim."
    },
    {
        word: "Apotheke", article: "die", gender: "die", plural: "die Apotheken",
        indefinite: "eine Apotheke", negation: "keine Apotheke",
        meaning: "hiệu thuốc tây", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Apotheke). Đối diện nhà ga dùng gegenüber vom Bahnhof.",
        example: "Die Apotheke liegt direkt gegenüber vom Bahnhof.",
        example_vi: "Hiệu thuốc nằm ngay đối diện nhà ga."
    },
    {
        word: "Kirche", article: "die", gender: "die", plural: "die Kirchen",
        indefinite: "eine Kirche", negation: "keine Kirche",
        meaning: "nhà thờ", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống cái (die Kirche). Bên cạnh nhà thờ cổ dùng neben einer alten Kirche.",
        example: "Das Museum liegt direkt vor dem Park und neben einer alten Kirche.",
        example_vi: "Bảo tàng nằm ngay phía trước công viên và bên cạnh một nhà thờ cổ."
    },
    {
        word: "Krankenhaus", article: "das", gender: "das", plural: "die Krankenhäuser",
        indefinite: "ein Krankenhaus", negation: "kein Krankenhaus",
        meaning: "bệnh viện", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Krankenhaus). Phía sau bệnh viện dùng hinter dem Krankenhaus.",
        example: "Der Parkplatz liegt direkt hinter dem Krankenhaus.",
        example_vi: "Bãi đỗ xe nằm ngay phía sau bệnh viện."
    },
    {
        word: "Hotel", article: "das", gender: "das", plural: "die Hotels",
        indefinite: "ein Hotel", negation: "kein Hotel",
        meaning: "khách sạn", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Hotel). Phía trước khách sạn dùng vor dem Hotel.",
        example: "Das Taxi wartet vor dem Hotel auf die Gäste.",
        example_vi: "Chiếc taxi đang đợi khách phía trước khách sạn."
    },
    {
        word: "Café", article: "das", gender: "das", plural: "die Cafés",
        indefinite: "ein Café", negation: "kein Café",
        meaning: "quán cà phê", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Café). Trong quán cà phê dùng im Café.",
        example: "Die Studenten sitzen im Café vor der Universität.",
        example_vi: "Các sinh viên đang ngồi trong quán cà phê phía trước trường đại học."
    },
    {
        word: "Kino", article: "das", gender: "das", plural: "die Kinos",
        indefinite: "ein Kino", negation: "kein Kino",
        meaning: "rạp chiếu phim", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Kino). Giữa hiệu sách và rạp phim dùng zwischen der Buchhandlung und dem Kino.",
        example: "Am Samstag gehen wir mit unseren Freunden ins Kino.",
        example_vi: "Vào thứ Bảy chúng tôi đi xem phim cùng với những người bạn của chúng tôi."
    },
    {
        word: "Museum", article: "das", gender: "das", plural: "die Museen",
        indefinite: "ein Museum", negation: "kein Museum",
        meaning: "bảo tàng", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Museum). Đến bảo tàng thành phố dùng zum Stadtmuseum.",
        example: "Wie komme ich vom Hauptbahnhof zum Stadtmuseum?",
        example_vi: "Tôi đi từ nhà ga trung tâm đến bảo tàng thành phố bằng cách nào?"
    },
    {
        word: "Stadtzentrum", article: "das", gender: "das", plural: "die Stadtzentren",
        indefinite: "ein Stadtzentrum", negation: "kein Stadtzentrum",
        meaning: "trung tâm thành phố", category: "Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)",
        rule: "Danh từ giống trung (das Stadtzentrum). Vào trung tâm thành phố dùng ins Stadtzentrum.",
        example: "Vom Flughafen fährt der Tourist mit der S-Bahn ins Stadtzentrum.",
        example_vi: "Từ sân bay vị khách du lịch đi bằng tàu điện đô thị vào trung tâm thành phố."
    },
    {
        word: "Aufzug", article: "der", gender: "der", plural: "die Aufzüge",
        indefinite: "ein Aufzug", negation: "kein Aufzug",
        meaning: "thang máy", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống đực (der Aufzug). Bên cạnh thang máy dùng neben dem Aufzug.",
        example: "Unser Büro liegt im zweiten Stock neben dem Aufzug.",
        example_vi: "Văn phòng của chúng tôi nằm ở tầng hai bên cạnh thang máy."
    },
    {
        word: "Eingang", article: "der", gender: "der", plural: "die Eingänge",
        indefinite: "ein Eingang", negation: "kein Eingang",
        meaning: "lối vào, cổng vào", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống đực (der Eingang). Bên cạnh lối vào dùng neben dem Eingang.",
        example: "Die Rezeption befindet sich im Erdgeschoss neben dem Eingang.",
        example_vi: "Quầy lễ tân nằm ở tầng trệt bên cạnh lối vào."
    },
    {
        word: "Schreibtisch", article: "der", gender: "der", plural: "die Schreibtische",
        indefinite: "ein Schreibtisch", negation: "kein Schreibtisch",
        meaning: "bàn làm việc", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống đực (der Schreibtisch). Trên bàn làm việc dùng auf dem Schreibtisch.",
        example: "Der Drucker steht auf dem Schreibtisch neben dem Computer.",
        example_vi: "Chiếc máy in nằm trên bàn làm việc bên cạnh máy tính."
    },
    {
        word: "Drucker", article: "der", gender: "der", plural: "die Drucker",
        indefinite: "ein Drucker", negation: "kein Drucker",
        meaning: "máy in", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống đực (der Drucker). Đặt trên mặt bàn làm việc dùng auf dem Schreibtisch.",
        example: "Der schwere Drucker steht auf dem Schreibtisch.",
        example_vi: "Chiếc máy in nặng đặt ở trên mặt bàn làm việc."
    },
    {
        word: "Kalender", article: "der", gender: "der", plural: "die Kalender",
        indefinite: "ein Kalender", negation: "kein Kalender",
        meaning: "cuốn lịch", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống đực (der Kalender). Treo trên tường dùng an der Wand.",
        example: "Der Kalender hängt an der Wand über dem Schreibtisch.",
        example_vi: "Cuốn lịch treo trên tường phía trên bàn làm việc."
    },
    {
        word: "Konferenzraum", article: "der", gender: "der", plural: "die Konferenzräume",
        indefinite: "ein Konferenzraum", negation: "kein Konferenzraum",
        meaning: "phòng họp, phòng hội nghị", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống đực (der Konferenzraum). Ở trong phòng họp dùng im Konferenzraum.",
        example: "Die Mitarbeiter sitzen im Konferenzraum.",
        example_vi: "Các nhân viên đang ngồi ở trong phòng họp."
    },
    {
        word: "Treppe", article: "die", gender: "die", plural: "die Treppen",
        indefinite: "eine Treppe", negation: "keine Treppe",
        meaning: "cầu thang bộ", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống cái (die Treppe). Đi bằng cầu thang bộ dùng über die Treppe.",
        example: "Sie müssen über die Treppe in den dritten Stock gehen.",
        example_vi: "Ngài phải đi bằng cầu thang bộ lên tầng ba."
    },
    {
        word: "Rezeption", article: "die", gender: "die", plural: "die Rezeptionen",
        indefinite: "eine Rezeption", negation: "keine Rezeption",
        meaning: "quầy lễ tân, quầy tiếp tân", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống cái (die Rezeption). Ở quầy lễ tân dùng an der Rezeption.",
        example: "Die Rezeption befindet sich im Erdgeschoss neben dem Eingang.",
        example_vi: "Quầy lễ tân nằm ở tầng trệt bên cạnh lối vào."
    },
    {
        word: "Kantine", article: "die", gender: "die", plural: "die Kantinen",
        indefinite: "eine Kantine", negation: "keine Kantine",
        meaning: "nhà ăn, căng tin cơ quan", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống cái (die Kantine). Trong nhà ăn ở tầng trệt dùng in der Kantine im Erdgeschoss.",
        example: "Die Kantine befindet sich im Erdgeschoss.",
        example_vi: "Nhà ăn nằm ở tầng trệt."
    },
    {
        word: "Erdgeschoss", article: "das", gender: "das", plural: "die Erdgeschosse",
        indefinite: "ein Erdgeschoss", negation: "kein Erdgeschoss",
        meaning: "tầng trệt", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống trung (das Erdgeschoss). Ở tầng trệt luôn dùng im Erdgeschoss.",
        example: "Die Kantine befindet sich im Erdgeschoss und der Konferenzraum ist im siebten Stock.",
        example_vi: "Nhà ăn nằm ở tầng trệt và phòng họp ở tầng bảy."
    },
    {
        word: "Büro", article: "das", gender: "das", plural: "die Büros",
        indefinite: "ein Büro", negation: "kein Büro",
        meaning: "văn phòng làm việc", category: "Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)",
        rule: "Danh từ giống trung (das Büro). Ở văn phòng dùng im Büro.",
        example: "Das Büro von Frau Schneider liegt im dritten Stock neben dem Aufzug.",
        example_vi: "Văn phòng của bà Schneider nằm ở tầng ba bên cạnh thang máy."
    },
    {
        word: "Programmierer", article: "der", gender: "der", plural: "die Programmierer",
        indefinite: "ein Programmierer", negation: "kein Programmierer",
        meaning: "nam lập trình viên", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Programmierer). Số nhiều giữ nguyên die Programmierer.",
        example: "Paula Rausch arbeitet mit einem Programmierer im Büro zusammen.",
        example_vi: "Paula Rausch làm việc cùng một nam lập trình viên ở văn phòng."
    },
    {
        word: "Programmiererin", article: "die", gender: "die", plural: "die Programmiererinnen",
        indefinite: "eine Programmiererin", negation: "keine Programmiererin",
        meaning: "nữ lập trình viên", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái kết thúc bằng -in. Số nhiều gấp đôi -nn thành die Programmiererinnen.",
        example: "Paula Rausch ist 35 Jahre alt und arbeitet als Programmiererin.",
        example_vi: "Paula Rausch 35 tuổi và làm nghề nữ lập trình viên."
    },
    {
        word: "Taxifahrer", article: "der", gender: "der", plural: "die Taxifahrer",
        indefinite: "ein Taxifahrer", negation: "kein Taxifahrer",
        meaning: "nam tài xế taxi", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Taxifahrer). Nghề nghiệp nói sein + Taxifahrer hoặc arbeiten als Taxifahrer.",
        example: "Mein Onkel arbeitet seit fünf Jahren als Taxifahrer in Hamburg.",
        example_vi: "Chú tôi làm nghề tài xế taxi ở Hamburg từ 5 năm nay."
    },
    {
        word: "Taxifahrerin", article: "die", gender: "die", plural: "die Taxifahrerinnen",
        indefinite: "eine Taxifahrerin", negation: "keine Taxifahrerin",
        meaning: "nữ tài xế taxi", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái. Số nhiều thêm -nen: die Taxifahrerinnen.",
        example: "Frau Becker ist eine erfahrene Taxifahrerin in Berlin.",
        example_vi: "Bà Becker là một nữ tài xế taxi giàu kinh nghiệm ở Berlin."
    },
    {
        word: "Krankenpfleger", article: "der", gender: "der", plural: "die Krankenpfleger",
        indefinite: "ein Krankenpfleger", negation: "kein Krankenpfleger",
        meaning: "nam điều dưỡng / y tá", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực chỉ nam y tá, chăm sóc bệnh nhân trong bệnh viện.",
        example: "Der Krankenpfleger hilft dem Arzt jeden Tag im Krankenhaus.",
        example_vi: "Người nam điều dưỡng giúp đỡ bác sĩ mỗi ngày ở bệnh viện."
    },
    {
        word: "Krankenpflegerin", article: "die", gender: "die", plural: "die Krankenpflegerinnen",
        indefinite: "eine Krankenpflegerin", negation: "keine Krankenpflegerin",
        meaning: "nữ điều dưỡng / y tá", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái chỉ nữ y tá (hoặc die Krankenschwester).",
        example: "Meine Tante arbeitet als Krankenpflegerin auf der Station.",
        example_vi: "Dì tôi làm nghề nữ điều dưỡng ở khoa điều trị."
    },
    {
        word: "Florist", article: "der", gender: "der", plural: "die Floristen",
        indefinite: "ein Florist", negation: "kein Florist",
        meaning: "nam nhân viên bán hoa / cắm hoa", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực thuộc nhóm N-Deklination: số nhiều die Floristen.",
        example: "Der Florist bindet wunderschöne Blumen für die Hochzeit.",
        example_vi: "Người nam thợ hoa bó những bông hoa tuyệt đẹp cho đám cưới."
    },
    {
        word: "Floristin", article: "die", gender: "die", plural: "die Floristinnen",
        indefinite: "eine Floristin", negation: "keine Floristin",
        meaning: "nữ nhân viên bán hoa", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Floristin). Nơi làm việc im Blumengeschäft.",
        example: "Die Floristin verkauft schöne Blumen im Blumengeschäft.",
        example_vi: "Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa."
    },
    {
        word: "Verkäufer", article: "der", gender: "der", plural: "die Verkäufer",
        indefinite: "ein Verkäufer", negation: "kein Verkäufer",
        meaning: "nam nhân viên bán hàng", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực. Bán hàng trong siêu thị hoặc cửa hàng.",
        example: "Der Verkäufer berät die Kunden freundlich im Supermarkt.",
        example_vi: "Nam nhân viên bán hàng tư vấn khách hàng thân thiện ở siêu thị."
    },
    {
        word: "Verkäuferin", article: "die", gender: "die", plural: "die Verkäuferinnen",
        indefinite: "eine Verkäuferin", negation: "keine Verkäuferin",
        meaning: "nữ nhân viên bán hàng", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Verkäuferin). Số nhiều die Verkäuferinnen.",
        example: "Die Verkäuferin verkauft moderne Schuhe im Schuhgeschäft.",
        example_vi: "Nữ nhân viên bán hàng bán những đôi giày hiện đại ở trong cửa hàng giày."
    },
    {
        word: "Mechatroniker", article: "der", gender: "der", plural: "die Mechatroniker",
        indefinite: "ein Mechatroniker", negation: "kein Mechatroniker",
        meaning: "nam thợ cơ khí ô tô", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Thợ cơ khí điện tử ô tô (KFZ-Mechatroniker), làm việc in einer Werkstatt.",
        example: "Der Mechatroniker repariert das Auto in einer Werkstatt.",
        example_vi: "Người thợ cơ khí sửa chiếc ô tô ở trong một xưởng sửa chữa."
    },
    {
        word: "Mechatronikerin", article: "die", gender: "die", plural: "die Mechatronikerinnen",
        indefinite: "eine Mechatronikerin", negation: "keine Mechatronikerin",
        meaning: "nữ thợ cơ khí ô tô", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Nữ thợ cơ khí ô tô (KFZ-Mechatronikerin).",
        example: "Sie lernt fleißig und möchte Mechatronikerin werden.",
        example_vi: "Cô ấy học tập chăm chỉ và muốn trở thành nữ thợ cơ khí."
    },
    {
        word: "Trainer", article: "der", gender: "der", plural: "die Trainer",
        indefinite: "ein Trainer", negation: "kein Trainer",
        meaning: "nam huấn luyện viên", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Trainer), làm việc im Fitnessstudio hoặc im Stadion.",
        example: "Der Trainer leitet das Training im Fitnessstudio.",
        example_vi: "Huấn luyện viên phụ trách buổi tập ở phòng gym."
    },
    {
        word: "Trainerin", article: "die", gender: "die", plural: "die Trainerinnen",
        indefinite: "eine Trainerin", negation: "keine Trainerin",
        meaning: "nữ huấn luyện viên", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Trainerin), số nhiều die Trainerinnen.",
        example: "Unsere Trainerin hilft den Sportlern jeden Tag im Stadion.",
        example_vi: "Nữ huấn luyện viên của chúng tôi giúp đỡ các vận động viên mỗi ngày ở sân vận động."
    },
    {
        word: "Lehrer", article: "der", gender: "der", plural: "die Lehrer",
        indefinite: "ein Lehrer", negation: "kein Lehrer",
        meaning: "nam giáo viên", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Lehrer). Cấu trúc Er ist Lehrer von Beruf không dùng mạo từ.",
        example: "Frank Müller ist Lehrer von Beruf und hat jetzt Ferien.",
        example_vi: "Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ."
    },
    {
        word: "Lehrerin", article: "die", gender: "die", plural: "die Lehrerinnen",
        indefinite: "eine Lehrerin", negation: "keine Lehrerin",
        meaning: "nữ giáo viên", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Lehrerin). Giảng dạy ở trường: an einer Schule unterrichten.",
        example: "Die Lehrerin unterrichtet Schüler an einer Schule in Berlin.",
        example_vi: "Nữ giáo viên giảng dạy học sinh tại một trường học ở Berlin."
    },
    {
        word: "Schüler", article: "der", gender: "der", plural: "die Schüler",
        indefinite: "ein Schüler", negation: "kein Schüler",
        meaning: "nam học sinh (phổ thông)", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Schüler), học sinh cấp 1 đến cấp 3.",
        example: "Der Schüler lernt viele Fächer in der Schule.",
        example_vi: "Cậu học sinh học nhiều môn học ở trường."
    },
    {
        word: "Schülerin", article: "die", gender: "die", plural: "die Schülerinnen",
        indefinite: "eine Schülerin", negation: "keine Schülerin",
        meaning: "nữ học sinh (phổ thông)", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Schülerin), số nhiều die Schülerinnen.",
        example: "Anna ist eine fleißige Schülerin am Gymnasium.",
        example_vi: "Anna là một nữ học sinh chăm chỉ tại trường THPT (Gymnasium)."
    },
    {
        word: "Student", article: "der", gender: "der", plural: "die Studenten",
        indefinite: "ein Student", negation: "kein Student",
        meaning: "nam sinh viên (đại học)", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực nhóm N-Deklination: der Student, des Studenten, die Studenten.",
        example: "Der Student studiert Informatik an der Universität.",
        example_vi: "Nam sinh viên học ngành công nghệ thông tin tại trường đại học."
    },
    {
        word: "Studentin", article: "die", gender: "die", plural: "die Studentinnen",
        indefinite: "eine Studentin", negation: "keine Studentin",
        meaning: "nữ sinh viên (đại học)", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Studentin). Học đại học: an der Universität studieren.",
        example: "Die Studentin liest viele deutsche Fachbücher in der Bibliothek.",
        example_vi: "Nữ sinh viên đọc nhiều sách chuyên ngành tiếng Đức trong thư viện."
    },
    {
        word: "Sekretär", article: "der", gender: "der", plural: "die Sekretäre",
        indefinite: "ein Sekretär", negation: "kein Sekretär",
        meaning: "nam thư ký", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Sekretär), số nhiều die Sekretäre.",
        example: "Der Sekretär vereinbart wichtige Termine mit Kunden.",
        example_vi: "Nam thư ký sắp xếp các cuộc hẹn quan trọng với khách hàng."
    },
    {
        word: "Sekretärin", article: "die", gender: "die", plural: "die Sekretärinnen",
        indefinite: "eine Sekretärin", negation: "keine Sekretärin",
        meaning: "nữ thư ký", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Sekretärin). Viết email và gọi điện: E-Mails schreiben und Kunden anrufen.",
        example: "Die Sekretärin schreibt E-Mails und ruft Kunden im Büro an.",
        example_vi: "Nữ thư ký viết email và gọi điện cho khách hàng ở văn phòng."
    },
    {
        word: "Friseur", article: "der", gender: "der", plural: "die Friseure",
        indefinite: "ein Friseur", negation: "kein Friseur",
        meaning: "nam thợ cắt tóc", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Friseur). Nơi làm việc im Friseursalon.",
        example: "Der Friseur schneidet meinem Bruder im Friseursalon die Haare.",
        example_vi: "Người thợ làm tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc."
    },
    {
        word: "Friseurin", article: "die", gender: "die", plural: "die Friseurinnen",
        indefinite: "eine Friseurin", negation: "keine Friseurin",
        meaning: "nữ thợ làm tóc", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Friseurin), số nhiều die Friseurinnen.",
        example: "Die Friseurin macht eine sehr schöne moderne Frisur.",
        example_vi: "Nữ thợ làm tóc làm một kiểu tóc hiện đại rất đẹp."
    },
    {
        word: "Kellner", article: "der", gender: "der", plural: "die Kellner",
        indefinite: "ein Kellner", negation: "kein Kellner",
        meaning: "nam nhân viên phục vụ bàn", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Kellner). Phục vụ thực khách im Restaurant.",
        example: "Der Kellner bringt den Gästen das Essen im Restaurant.",
        example_vi: "Người bồi bàn mang thức ăn cho thực khách ở nhà hàng."
    },
    {
        word: "Kellnerin", article: "die", gender: "die", plural: "die Kellnerinnen",
        indefinite: "eine Kellnerin", negation: "keine Kellnerin",
        meaning: "nữ nhân viên phục vụ bàn", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái (die Kellnerin), số nhiều die Kellnerinnen.",
        example: "Die Kellnerin bedient Gäste freundlich im Café.",
        example_vi: "Nữ phục vụ bàn phục vụ thực khách thân thiện ở quán cà phê."
    },
    {
        word: "Koch", article: "der", gender: "der", plural: "die Köche",
        indefinite: "ein Koch", negation: "kein Koch",
        meaning: "nam đầu bếp", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực đặc biệt: số nhiều đổi biến âm die Köche.",
        example: "Der Koch bereitet köstliche Gerichte in der Küche zu.",
        example_vi: "Người đầu bếp chuẩn bị những món ăn ngon tuyệt trong nhà bếp."
    },
    {
        word: "Köchin", article: "die", gender: "die", plural: "die Köchinnen",
        indefinite: "eine Köchin", negation: "keine Köchin",
        meaning: "nữ đầu bếp", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái đặc biệt: thêm Umlaut ö và đuôi -in thành die Köchin.",
        example: "Frau Bui ist eine talentierte Köchin in einem Restaurant.",
        example_vi: "Bà Bùi là một nữ đầu bếp tài năng trong một nhà hàng."
    },
    {
        word: "Arzt", article: "der", gender: "der", plural: "die Ärzte",
        indefinite: "ein Arzt", negation: "kein Arzt",
        meaning: "nam bác sĩ", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực đặc biệt: số nhiều thêm Umlaut die Ärzte.",
        example: "Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus.",
        example_vi: "Bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện."
    },
    {
        word: "Ärztin", article: "die", gender: "die", plural: "die Ärztinnen",
        indefinite: "eine Ärztin", negation: "keine Ärztin",
        meaning: "nữ bác sĩ", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái đặc biệt: thêm Umlaut ä và đuôi -in thành die Ärztin.",
        example: "Die Ärztin hilft kranken Menschen mit großer Geduld.",
        example_vi: "Nữ bác sĩ giúp đỡ những người bệnh bằng sự kiên nhẫn to lớn."
    },
    {
        word: "Hausmann", article: "der", gender: "der", plural: "die Hausmänner",
        indefinite: "ein Hausmann", negation: "kein Hausmann",
        meaning: "người đàn ông nội trợ", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống đực (der Hausmann), số nhiều die Hausmänner.",
        example: "Mein Onkel ist Hausmann und kümmert sich um die Kinder.",
        example_vi: "Chú tôi là người nội trợ và chăm sóc con cái."
    },
    {
        word: "Hausfrau", article: "die", gender: "die", plural: "die Hausfrauen",
        indefinite: "eine Hausfrau", negation: "keine Hausfrau",
        meaning: "người phụ nữ nội trợ", category: "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
        rule: "Danh từ giống cái chuyển từ gốc -mann sang -frau: die Hausfrau.",
        example: "Meine Großmutter war viele Jahre Hausfrau und kochte gern.",
        example_vi: "Bà tôi đã làm nội trợ nhiều năm và rất thích nấu ăn."
    },
    {
        word: "Friseursalon", article: "der", gender: "der", plural: "die Friseursalons",
        indefinite: "ein Friseursalon", negation: "kein Friseursalon",
        meaning: "tiệm làm tóc, salon tóc", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống đực (der Friseursalon). Trả lời Wo? dùng im Friseursalon (in + dem).",
        example: "Der Friseur arbeitet jeden Tag im Friseursalon.",
        example_vi: "Người thợ làm tóc làm việc mỗi ngày ở trong tiệm làm tóc."
    },
    {
        word: "Supermarkt", article: "der", gender: "der", plural: "die Supermärkte",
        indefinite: "ein Supermarkt", negation: "kein Supermarkt",
        meaning: "siêu thị", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống đực (der Supermarkt). Trả lời Wo? dùng im Supermarkt.",
        example: "Frau Lindner kauft frische Lebensmittel im Supermarkt ein.",
        example_vi: "Bà Lindner mua thực phẩm tươi ở trong siêu thị."
    },
    {
        word: "Kindergarten", article: "der", gender: "der", plural: "die Kindergärten",
        indefinite: "ein Kindergarten", negation: "kein Kindergarten",
        meaning: "trường mẫu giáo, nhà trẻ", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống đực. Di chuyển Wohin? -> in den Kindergarten; ở lại Wo? -> im Kindergarten.",
        example: "Um 8.30 Uhr bringt Frank seine Tochter in den Kindergarten.",
        example_vi: "Lúc 8 giờ 30 phút Frank đưa con gái vào trường mẫu giáo."
    },
    {
        word: "Schule", article: "die", gender: "die", plural: "die Schulen",
        indefinite: "eine Schule", negation: "keine Schule",
        meaning: "trường học (phổ thông)", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống cái (die Schule). Trả lời Wo? dùng an einer Schule hoặc in der Schule.",
        example: "Frau Weber unterrichtet viele Schüler an einer Schule in Berlin.",
        example_vi: "Bà Weber giảng dạy nhiều học sinh tại một trường học ở Berlin."
    },
    {
        word: "Universität", article: "die", gender: "die", plural: "die Universitäten",
        indefinite: "eine Universität", negation: "keine Universität",
        meaning: "trường đại học", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống cái đuôi -tät. Trả lời Wo? dùng an der Universität / an einer Hochschule.",
        example: "Mein Bruder studiert Informatik an der Universität.",
        example_vi: "Anh trai tôi học ngành tin học tại trường đại học."
    },
    {
        word: "Werkstatt", article: "die", gender: "die", plural: "die Werkstätten",
        indefinite: "eine Werkstatt", negation: "keine Werkstatt",
        meaning: "xưởng sửa chữa", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống cái (die Werkstatt). Di chuyển Wohin? -> in die Werkstatt; ở tại Wo? -> in der Werkstatt.",
        example: "Der KFZ-Mechatroniker repariert das Auto in einer Werkstatt.",
        example_vi: "Người thợ cơ khí ô tô sửa chiếc xe trong một xưởng sửa chữa."
    },
    {
        word: "Baustelle", article: "die", gender: "die", plural: "die Baustellen",
        indefinite: "eine Baustelle", negation: "keine Baustelle",
        meaning: "công trường xây dựng", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống cái (die Baustelle). Trả lời Wo? dùng auf der Baustelle / auf einer Baustelle.",
        example: "Die Arbeiter tragen Helme auf der Baustelle.",
        example_vi: "Các công nhân đội mũ bảo hộ trên công trường xây dựng."
    },
    {
        word: "Firma", article: "die", gender: "die", plural: "die Firmen",
        indefinite: "eine Firma", negation: "keine Firma",
        meaning: "công ty, doanh nghiệp", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống cái (die Firma). Trả lời Wo? dùng in einer Firma hoặc bei einer IT-Firma.",
        example: "Paula Rausch arbeitet als Programmiererin bei einer IT-Firma.",
        example_vi: "Paula Rausch làm nghề lập trình viên tại một công ty công nghệ thông tin."
    },
    {
        word: "Krankenhaus", article: "das", gender: "das", plural: "die Krankenhäuser",
        indefinite: "ein Krankenhaus", negation: "kein Krankenhaus",
        meaning: "bệnh viện", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống trung (das Krankenhaus). Trả lời Wo? dùng im Krankenhaus (in + dem).",
        example: "Der Arzt untersucht die Patienten im Krankenhaus.",
        example_vi: "Bác sĩ khám cho các bệnh nhân ở trong bệnh viện."
    },
    {
        word: "Restaurant", article: "das", gender: "das", plural: "die Restaurants",
        indefinite: "ein Restaurant", negation: "kein Restaurant",
        meaning: "nhà hàng", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống trung gốc Pháp (das Restaurant). Trả lời Wo? dùng im Restaurant.",
        example: "Die Köchin kocht leckere Spezialitäten im Restaurant.",
        example_vi: "Nữ đầu bếp nấu các món đặc sản ngon miệng ở trong nhà hàng."
    },
    {
        word: "Blumengeschäft", article: "das", gender: "das", plural: "die Blumengeschäfte",
        indefinite: "ein Blumengeschäft", negation: "kein Blumengeschäft",
        meaning: "cửa hàng hoa tươi", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ ghép giống trung (das Blumengeschäft). Trả lời Wo? dùng im Blumengeschäft.",
        example: "Die Floristin verkauft bunte Rosen im Blumengeschäft.",
        example_vi: "Người nữ bán hoa bán hoa hồng nhiều màu sắc ở trong cửa hàng hoa."
    },
    {
        word: "Schuhgeschäft", article: "das", gender: "das", plural: "die Schuhgeschäfte",
        indefinite: "ein Schuhgeschäft", negation: "kein Schuhgeschäft",
        meaning: "cửa hàng giày dép", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ ghép giống trung (das Schuhgeschäft). Trả lời Wo? dùng im Schuhgeschäft.",
        example: "Die Verkäuferin verkauft modische Schuhe im Schuhgeschäft.",
        example_vi: "Nữ nhân viên bán hàng bán giày thời trang ở trong cửa hàng giày."
    },
    {
        word: "Sprachzentrum", article: "das", gender: "das", plural: "die Sprachzentren",
        indefinite: "ein Sprachzentrum", negation: "kein Sprachzentrum",
        meaning: "trung tâm ngoại ngữ", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống trung đuôi -um đổi số nhiều sang -en: die Sprachzentren. Dùng im Sprachzentrum.",
        example: "Wir lernen jeden Tag Deutsch im Sprachzentrum.",
        example_vi: "Chúng tôi học tiếng Đức mỗi ngày ở trong trung tâm ngoại ngữ."
    },
    {
        word: "Bett", article: "das", gender: "das", plural: "die Betten",
        indefinite: "ein Bett", negation: "kein Bett",
        meaning: "chiếc giường ngủ", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống trung (das Bett). Hướng di chuyển Wohin? -> ins Bett; Vị trí tĩnh Wo? -> im Bett.",
        example: "Um neunzehn Uhr bringt Frank seine Tochter ins Bett.",
        example_vi: "Lúc 19 giờ Frank đưa con gái của mình lên giường đi ngủ."
    },
    {
        word: "Fitnessstudio", article: "das", gender: "das", plural: "die Fitnessstudios",
        indefinite: "ein Fitnessstudio", negation: "kein Fitnessstudio",
        meaning: "phòng tập thể hình, gym", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống trung (das Fitnessstudio). Trả lời Wo? dùng im Fitnessstudio.",
        example: "Der Trainer trainiert fleißig Sportler im Fitnessstudio.",
        example_vi: "Huấn luyện viên rèn luyện chăm chỉ cho vận động viên ở phòng gym."
    },
    {
        word: "Stadion", article: "das", gender: "das", plural: "die Stadien",
        indefinite: "ein Stadion", negation: "kein Stadion",
        meaning: "sân vận động", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống trung (das Stadion), số nhiều die Stadien. Trả lời Wo? dùng im Stadion.",
        example: "Am Wochenende spielen Fußballer im großen Stadion.",
        example_vi: "Vào cuối tuần các cầu thủ thi đấu ở trong sân vận động lớn."
    },
    {
        word: "Computer", article: "der", gender: "der", plural: "die Computer",
        indefinite: "ein Computer", negation: "kein Computer",
        meaning: "máy vi tính", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống đực (der Computer). Tân ngữ Akkusativ sau brauchen: einen Computer brauchen.",
        example: "Bei ihrer Arbeit braucht Petra May einen schnellen Computer.",
        example_vi: "Trong công việc của mình, Petra May cần một chiếc máy tính nhanh."
    },
    {
        word: "Patient", article: "der", gender: "der", plural: "die Patienten",
        indefinite: "ein Patient", negation: "kein Patient", akkusativ: "den / einen / keinen Patienten",
        meaning: "bệnh nhân", category: "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
        rule: "Danh từ giống đực N-Deklination (der Patient). Tân ngữ Akkusativ sau untersuchen: den Patienten untersuchen.",
        example: "Der Arzt untersucht den kranken Patienten im Behandlungszimmer.",
        example_vi: "Bác sĩ khám cho bệnh nhân bị ốm ở trong phòng khám bệnh."
    }
];

let currentLexikonFilter = "all";
let currentLexikonSearchQuery = "";

const LEXIKON_FILTERS = [
    { id: "all", label: "Tất cả" },
    { id: "Berufe", label: "👨‍💼 Nghề nghiệp Nam & Nữ (Bài 7)" },
    { id: "Arbeitsorte", label: "🏢 Nơi làm việc & Đời sống (Bài 7)" },
    { id: "Phương tiện Giao thông", label: "🚆 Phương tiện Giao thông & Điểm đến (Bài 6)" },
    { id: "Tòa nhà, Văn phòng", label: "🏢 Tòa nhà, Văn phòng & Bàn làm việc (Bài 6)" },
    { id: "der", label: "🔵 Giống đực - der (Maskulinum)" },
    { id: "die", label: "🔴 Giống cái - die (Femininum)" },
    { id: "das", label: "🟢 Giống trung - das (Neutrum)" },
    { id: "Thời gian & Lịch trình", label: "⏰ Thời gian, Thứ, Tháng & Lịch trình (Bài 5)" },
    { id: "Nhà ở & Phòng ốc", label: "🏠 Nhà ở & Phòng ốc (Menschen & Häuser)" },
    { id: "Nội thất & Đồ đạc", label: "🛋️ Nội thất & Đồ đạc (Möbel & Einrichtung)" },
    { id: "Quốc gia & Ngôn ngữ", label: "🌍 Quốc gia & Ngôn ngữ (Länder & Sprachen)" },
    { id: "Danh lam thắng cảnh", label: "🏛️ Danh lam thắng cảnh (Sehenswürdigkeiten)" },
    { id: "Phương hướng & Bản đồ", label: "🧭 Phương hướng & Bản đồ (Himmelsrichtungen)" },
    { id: "Đồ dùng lớp học", label: "🏫 Đồ dùng & Ngôn ngữ lớp học" },
    { id: "Động từ lớp học", label: "🗣️ Động từ lớp học & Giao tiếp" },
    { id: "Quy tắc hậu tố giống", label: "🧩 Quy tắc hậu tố nhận biết giống" }
];

function updateLexikonUI() {
    const cardsGrid = document.getElementById('lexikon-cards-grid');
    const filterPills = document.getElementById('lexikon-filter-pills');
    const clearWrap = document.getElementById('lexikon-clear-btn-wrap');
    if (!cardsGrid || !filterPills || !clearWrap) return;

    const q = (currentLexikonSearchQuery || "").toLowerCase().trim();
    const filteredList = GERMAN_LEXIKON_DB.filter(item => {
        let matchFilter = true;
        if (currentLexikonFilter === "der" || currentLexikonFilter === "die" || currentLexikonFilter === "das") {
            matchFilter = item.gender === currentLexikonFilter;
        } else if (currentLexikonFilter !== "all") {
            matchFilter = item.category === currentLexikonFilter;
        }

        const matchSearch = !q ||
            item.word.toLowerCase().includes(q) ||
            item.article.toLowerCase().includes(q) ||
            item.meaning.toLowerCase().includes(q) ||
            item.rule.toLowerCase().includes(q) ||
            item.plural.toLowerCase().includes(q);

        return matchFilter && matchSearch;
    });

    // Cập nhật nút xóa tìm kiếm
    clearWrap.innerHTML = currentLexikonSearchQuery ? `
        <button onclick="clearLexikonSearch()" class="px-4 py-3 rounded-2xl bg-white/10 hover:bg-white/20 text-white text-xs font-bold border border-white/20 transition cursor-pointer">
            ✕ Xóa tìm kiếm
        </button>
    ` : '';

    // Cập nhật bộ lọc Pills
    filterPills.innerHTML = LEXIKON_FILTERS.map(f => {
        let count = 0;
        if (f.id === "all") {
            count = GERMAN_LEXIKON_DB.length;
        } else if (f.id === "der" || f.id === "die" || f.id === "das") {
            count = GERMAN_LEXIKON_DB.filter(x => x.gender === f.id).length;
        } else {
            count = GERMAN_LEXIKON_DB.filter(x => x.category === f.id).length;
        }

        const isActive = currentLexikonFilter === f.id;
        return `
            <button onclick="setLexikonFilter('${f.id}')" class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition whitespace-nowrap shrink-0 cursor-pointer ${isActive ? 'bg-indigo-600 text-white shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'}">
                ${f.label} (${count})
            </button>
        `;
    }).join('');

    // Cập nhật danh sách thẻ từ vựng
    if (filteredList.length === 0) {
        cardsGrid.innerHTML = `
            <div class="col-span-full p-8 rounded-3xl bg-white border border-slate-200 text-center space-y-3">
                <div class="text-3xl">🔍</div>
                <h4 class="text-base font-bold text-slate-800">Không tìm thấy từ vựng nào phù hợp với từ khóa "${currentLexikonSearchQuery}"</h4>
                <p class="text-xs text-slate-500">Hãy thử gõ tên đồ vật như 'Kuli', 'Brille', 'Buch' hoặc nghĩa tiếng Việt như 'bút', 'kính', 'sách'.</p>
                <button onclick="clearLexikonSearch()" class="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs cursor-pointer">
                    Hiển thị toàn bộ ${GERMAN_LEXIKON_DB.length} mục tra cứu
                </button>
            </div>
        `;
        return;
    }

    cardsGrid.innerHTML = filteredList.map(item => {
        let badgeStyle = "bg-purple-50 text-purple-700 border-purple-300";
        let displayFullWord = item.word;

        if (item.gender === "der") {
            badgeStyle = "bg-blue-50 text-blue-700 border-blue-300";
            displayFullWord = `der ${item.word}`;
        } else if (item.gender === "die") {
            badgeStyle = "bg-rose-50 text-rose-700 border-rose-300";
            displayFullWord = `die ${item.word}`;
        } else if (item.gender === "das") {
            badgeStyle = "bg-emerald-50 text-emerald-700 border-emerald-300";
            displayFullWord = `das ${item.word}`;
        }

        const safeSpeakWord = displayFullWord.replace(/'/g, "\\'");
        const safeSpeakExample = item.example.replace(/'/g, "\\'");

        let grammarPillsHtml = "";
        if (item.gender === "verb") {
            grammarPillsHtml = `
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200 font-semibold text-slate-700">
                        <span class="text-slate-400 block text-[10px]">Dạng chia:</span>
                        <span class="font-bold text-slate-900">${item.plural}</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200 font-semibold text-slate-700">
                        <span class="text-slate-400 block text-[10px]">Đặc điểm:</span>
                        <span class="font-bold text-purple-700">${item.indefinite}</span>
                    </div>
                </div>
            `;
        } else {
            grammarPillsHtml = `
                <div class="grid grid-cols-2 gap-2 text-xs">
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200 font-semibold text-slate-700">
                        <span class="text-slate-400 block text-[10px]">Số nhiều (Plural):</span>
                        <span class="font-bold text-indigo-700">${item.plural}</span>
                    </div>
                    <div class="p-2 rounded-xl bg-slate-50 border border-slate-200 font-semibold text-slate-700">
                        <span class="text-slate-400 block text-[10px]">Bất định / Phủ định:</span>
                        <span class="font-bold text-slate-900">${item.indefinite}</span> / <span class="text-rose-600 font-bold">${item.negation}</span>
                    </div>
                </div>
                ${item.akkusativ ? `
                <div class="p-2 rounded-xl bg-indigo-50/70 border border-indigo-200 text-xs flex items-center justify-between">
                    <span class="text-indigo-900 font-bold text-[10px]">Cách 4 (Akkusativ):</span>
                    <span class="font-mono font-bold text-indigo-700 text-[11px]">${item.akkusativ}</span>
                </div>
                ` : ''}
            `;
        }

        return `
            <div class="p-5 sm:p-6 rounded-3xl bg-white border border-slate-200 shadow-sm hover:shadow-lg hover:border-indigo-300 transition-all flex flex-col justify-between space-y-4">
                <div>
                    <div class="flex items-start justify-between gap-3 flex-wrap">
                        <div class="flex items-baseline gap-2.5">
                            <h3 class="text-2xl font-black text-slate-900 tracking-tight">${displayFullWord}</h3>
                            <button onclick="speakGerman('${safeSpeakWord}')" class="w-8 h-8 rounded-xl bg-slate-100 hover:bg-indigo-600 text-slate-600 hover:text-white flex items-center justify-center text-xs transition shadow-xs cursor-pointer" title="Phát âm chuẩn de-DE">
                                🔊
                            </button>
                        </div>
                        <span class="px-2.5 py-1 rounded-lg text-[11px] font-bold border ${badgeStyle}">
                            ${item.article} (${item.category})
                        </span>
                    </div>
                    <p class="text-sm font-bold text-indigo-600 mt-1">${item.meaning}</p>
                </div>

                ${grammarPillsHtml}

                <div class="p-3 rounded-2xl bg-amber-50/70 border border-amber-200/80 text-xs text-slate-700">
                    💡 <span class="font-semibold text-slate-800">${item.rule}</span>
                </div>

                <div class="pt-2 border-t border-slate-100 space-y-1 text-xs">
                    <div class="flex items-center justify-between gap-2">
                        <span class="text-slate-700 font-medium italic">"${item.example}"</span>
                        <button onclick="speakGerman('${safeSpeakExample}')" class="shrink-0 px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 font-bold transition flex items-center gap-1 cursor-pointer">
                            🔊 Nghe câu
                        </button>
                    </div>
                    <p class="text-[11px] text-slate-500">${item.example_vi}</p>
                </div>
            </div>
        `;
    }).join('');
}

function renderLexikon(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Nếu cấu trúc DOM chưa có (lần đầu mở tab), khởi tạo khung tĩnh một lần duy nhất
    if (!document.getElementById('lexikon-cards-grid')) {
        container.innerHTML = `
            <!-- Hero Banner của Tab Từ vựng & Giống -->
            <div class="rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white p-6 sm:p-8 shadow-xl border border-slate-800">
                <div class="flex flex-wrap items-center justify-between gap-4">
                    <div class="space-y-2 max-w-3xl">
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                            🏷️ DeutschMeister Genus- & Wortschatz-Lexikon • Tra Cứu Giống & Từ Vựng A1 - A2
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-black tracking-tight text-white">
                            Tra Cứu Giống (der / die / das), Số Nhiều & Từ Vựng Theo Chủ Đề
                        </h2>
                        <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                            Hệ thống phân loại tự động Giống đực (<b>der</b>), Giống cái (<b>die</b>), Giống trung (<b>das</b>), Dạng số nhiều (<b>Plural</b>), Mạo từ bất định (<b>ein/eine</b>), Phủ định (<b>kein/keine</b>) và Động từ theo chủ đề kèm câu ví dụ thực tế và giọng đọc bản xứ <b>de-DE</b>.
                        </p>
                    </div>

                    <div class="shrink-0 text-right hidden sm:block">
                        <span class="px-4 py-2 rounded-2xl bg-white/10 border border-white/20 text-amber-400 font-extrabold text-sm flex items-center gap-2">
                            ⚡ ${GERMAN_LEXIKON_DB.length}+ Từ vựng & Quy tắc cốt lõi
                        </span>
                    </div>
                </div>

                <!-- Thanh tìm kiếm thông minh (Giữ nguyên DOM để không bị nhảy chữ khi gõ bàn phím Telex) -->
                <div class="mt-6 flex flex-wrap gap-3">
                    <div class="relative flex-1 min-w-[260px]">
                        <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-slate-400">
                            🔍
                        </span>
                        <input id="lexikon-search-input" value="${currentLexikonSearchQuery}" oninput="onLexikonSearchChange(this.value)" type="text" placeholder="Gõ từ tiếng Đức (Kuli, Brille, Handy, verstehen...) hoặc nghĩa tiếng Việt (bút bi, kính mắt, bảng đen, đánh vần...)" class="w-full pl-10 pr-4 py-3 rounded-2xl bg-white/10 border border-white/20 text-white placeholder:text-slate-400 text-sm focus:outline-none focus:bg-white/20 focus:border-amber-400 transition" autocomplete="off" spellcheck="false">
                    </div>
                    <div id="lexikon-clear-btn-wrap"></div>
                </div>
            </div>

            <!-- Nút bật/tắt Bảng Ma Trận Mạo Từ & Sở Hữu -->
            <div class="flex items-center justify-between flex-wrap gap-2 pt-1">
                <button onclick="toggleMatrixTable()" id="btn-toggle-matrix" class="px-4 py-2.5 rounded-2xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white font-bold text-xs shadow-md transition flex items-center gap-1.5 cursor-pointer">
                    📊 Bảng Tra Cứu Nhanh Mạo Từ & Sở Hữu (Nominativ vs. Akkusativ)
                </button>
                <span class="text-xs text-slate-500 italic">💡 Bấm để đối chiếu nhanh quy tắc biến đổi Cách 1 (Nominativ) sang Cách 4 (Akkusativ)</span>
            </div>

            <!-- Khung Ma Trận Tra Cứu Nhanh (Collapsible) -->
            <div id="lexikon-matrix-table-wrap" class="hidden rounded-3xl bg-white border border-indigo-200 p-5 sm:p-6 shadow-sm space-y-4">
                <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                    <h3 class="text-base font-extrabold text-slate-900 flex items-center gap-2">
                        <span>📋</span> Ma Trận 3 Loại Mạo Từ: Nominativ (Cách 1) vs. Akkusativ (Cách 4)
                    </h3>
                    <button onclick="toggleMatrixTable()" class="text-slate-400 hover:text-slate-700 text-sm font-bold cursor-pointer">✕ Đóng</button>
                </div>

                <div class="overflow-x-auto rounded-2xl border border-slate-200">
                    <table class="w-full text-left text-xs">
                        <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                            <tr>
                                <th class="p-3">Giống / Số</th>
                                <th class="p-3">Xác định (C1 → C4)</th>
                                <th class="p-3">Bất định (C1 → C4)</th>
                                <th class="p-3">Phủ định (C1 → C4)</th>
                                <th class="p-3">Sở hữu ich / du / er / wir (C1 → C4)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            <tr class="bg-blue-50/40">
                                <td class="p-3 font-bold text-blue-800">🔵 Giống Đực (m)</td>
                                <td class="p-3"><b>der</b> → <span class="font-bold text-rose-600">den</span></td>
                                <td class="p-3"><b>ein</b> → <span class="font-bold text-rose-600">einen</span></td>
                                <td class="p-3"><b>kein</b> → <span class="font-bold text-rose-600">keinen</span></td>
                                <td class="p-3">mein → <span class="font-bold text-rose-600">meinen</span> / dein → <span class="font-bold text-rose-600">deinen</span></td>
                            </tr>
                            <tr class="bg-rose-50/40">
                                <td class="p-3 font-bold text-rose-800">🔴 Giống Cái (f)</td>
                                <td class="p-3"><b>die</b> → <b>die</b> (giữ nguyên)</td>
                                <td class="p-3"><b>eine</b> → <b>eine</b> (giữ nguyên)</td>
                                <td class="p-3"><b>keine</b> → <b>keine</b> (giữ nguyên)</td>
                                <td class="p-3">meine / deine / seine / unsere (giữ nguyên)</td>
                            </tr>
                            <tr class="bg-emerald-50/40">
                                <td class="p-3 font-bold text-emerald-800">🟢 Giống Trung (n)</td>
                                <td class="p-3"><b>das</b> → <b>das</b> (giữ nguyên)</td>
                                <td class="p-3"><b>ein</b> → <b>ein</b> (giữ nguyên)</td>
                                <td class="p-3"><b>kein</b> → <b>kein</b> (giữ nguyên)</td>
                                <td class="p-3">mein / dein / sein / unser (giữ nguyên)</td>
                            </tr>
                            <tr class="bg-purple-50/40">
                                <td class="p-3 font-bold text-purple-800">🟣 Số Nhiều (Pl)</td>
                                <td class="p-3"><b>die</b> → <b>die</b> (giữ nguyên)</td>
                                <td class="p-3"><i>— (không có ein)</i></td>
                                <td class="p-3"><b>keine</b> → <b>keine</b> (giữ nguyên)</td>
                                <td class="p-3">meine / deine / eure (bỏ e) / Ihre (giữ nguyên)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-slate-700">
                    💡 <b>Quy luật cốt lõi cần nhớ:</b> Chỉ duy nhất <b>Giống đực (der)</b> khi chuyển sang Akkusativ mới đổi đuôi sang <b>-en</b> (<i>den, einen, keinen, meinen, deinen, seinen, ihren, unseren, euren, Ihren</i>). Tất cả các giống còn lại (die, das, Plural) <b>giữ nguyên 100%</b>!
                </div>
            </div>

            <!-- Bộ lọc phân loại theo giống & chủ đề -->
            <div class="flex items-center gap-2 overflow-x-auto pb-1">
                <span class="text-xs font-bold text-slate-500 whitespace-nowrap">Bộ lọc:</span>
                <div id="lexikon-filter-pills" class="flex items-center gap-2 overflow-x-auto"></div>
            </div>

            <!-- Lưới thẻ từ vựng & giống (Cập nhật động nội dung thẻ mà không ảnh hưởng tới ô input) -->
            <div id="lexikon-cards-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5"></div>
        `;
    }

    updateLexikonUI();
}

function setLexikonFilter(filterId) {
    currentLexikonFilter = filterId;
    updateLexikonUI();
}

function onLexikonSearchChange(val) {
    currentLexikonSearchQuery = val;
    updateLexikonUI();
}

function clearLexikonSearch() {
    currentLexikonSearchQuery = "";
    currentLexikonFilter = "all";
    const input = document.getElementById('lexikon-search-input');
    if (input) {
        input.value = "";
        input.focus();
    }
    updateLexikonUI();
}

function toggleMatrixTable() {
    const wrap = document.getElementById('lexikon-matrix-table-wrap');
    const btn = document.getElementById('btn-toggle-matrix');
    if (!wrap || !btn) return;
    const isHidden = wrap.classList.contains('hidden');
    if (isHidden) {
        wrap.classList.remove('hidden');
        btn.innerHTML = '✕ Đóng Bảng Ma Trận Mạo Từ & Sở Hữu';
    } else {
        wrap.classList.add('hidden');
        btn.innerHTML = '📊 Bảng Tra Cứu Nhanh Mạo Từ & Sở Hữu (Nominativ vs. Akkusativ)';
    }
}

if (typeof window !== 'undefined') {
    window.GERMAN_LEXIKON_DB = GERMAN_LEXIKON_DB;
    window.renderLexikon = renderLexikon;
    window.updateLexikonUI = updateLexikonUI;
    window.setLexikonFilter = setLexikonFilter;
    window.onLexikonSearchChange = onLexikonSearchChange;
    window.clearLexikonSearch = clearLexikonSearch;
    window.toggleMatrixTable = toggleMatrixTable;
}
