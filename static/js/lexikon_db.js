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
        example: "Ist das ein Becher? – Nein, das ist kein Becher. Das ist ein Papier.",
        example_vi: "Đây có phải là cái cốc không? – Không, đó không phải cái cốc. Đó là một tờ giấy."
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
        meaning: "tờ giấy / giấy", category: "Đồ dùng lớp học",
        rule: "Giống trung (das), số nhiều thêm -e (die Papiere).",
        example: "Ist das ein Becher? – Nein, das ist ein Papier.",
        example_vi: "Đây có phải là cái cốc không? – Không, đó là một tờ giấy."
    },
    {
        word: "Heft", article: "das", gender: "das", plural: "die Hefte",
        indefinite: "ein Heft", negation: "kein Heft",
        meaning: "quyển vở", category: "Đồ dùng lớp học",
        rule: "Giống trung (das), số nhiều thêm -e (die Hefte).",
        example: "Können Sie 'das Heft' bitte buchstabieren? – H - E - F - T.",
        example_vi: "Ngài có thể đánh vần từ 'das Heft' được không? – H - E - F - T."
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
        example: "Er ist ein Praktikant bei der Post.",
        example_vi: "Anh ấy là một thực tập sinh tại bưu điện."
    },
    {
        word: "Student", article: "der", gender: "der", plural: "die Studenten",
        indefinite: "ein Student", negation: "kein Student",
        meaning: "nam sinh viên", category: "Quy tắc hậu tố giống",
        rule: "Hậu tố -ent luôn mang giống đực (der). Nữ sinh viên là die Studentin.",
        example: "David ist ein Student aus den USA.",
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
        example: "Die Freundschaft von Anna und Sophie ist toll.",
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
        example: "Ist das ein Dokument? – Ja, das ist das Dokument von Herr Nguyen.",
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
        example: "Hast du eine Erlaubnis von der Lehrerin?",
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
        word: "Schiefe Turm", article: "der", gender: "der", plural: "Pisa (Ý)",
        indefinite: "ein schiefer Turm", negation: "Italien",
        meaning: "Tháp nghiêng Pisa (ở Pisa, Ý)", category: "Danh lam thắng cảnh",
        rule: "Cụm danh từ có tính từ 'schief' (nghiêng) + der Turm (tháp) -> der Schiefe Turm von Pisa.",
        example: "Wo ist der Schiefe Turm? – Er ist in Pisa, Italien.",
        example_vi: "Tháp nghiêng ở đâu? – Nó nằm ở thành phố Pisa, nước Ý."
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
        meaning: "phía Bắc, miền Bắc", category: "Phương hướng & Bản đồ",
        rule: "Mọi phương hướng đều mang giống đực (der). Có 2 cách nói: 'im Norden von' hoặc 'nördlich von'.",
        example: "Wo liegt Hanoi? – Hanoi liegt im Norden von Vietnam (nördlich von Vietnam).",
        example_vi: "Hà Nội nằm ở đâu? – Hà Nội nằm ở miền Bắc Việt Nam."
    },
    {
        word: "Süden", article: "der", gender: "der", plural: "Tính từ: südlich",
        indefinite: "im Süden von", negation: "südlich von",
        meaning: "phía Nam, miền Nam", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). Hai cách diễn đạt: 'im Süden von' hoặc 'südlich von'.",
        example: "Long An liegt im Süden von Vietnam (südlich von Vietnam).",
        example_vi: "Long An nằm ở miền Nam của Việt Nam."
    },
    {
        word: "Osten", article: "der", gender: "der", plural: "Tính từ: östlich",
        indefinite: "im Osten von", negation: "östlich von",
        meaning: "phía Đông, miền Đông", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). Khi chuyển sang tính từ thêm Umlaut o -> ö: östlich.",
        example: "Berlin liegt im Osten von Deutschland (östlich von Deutschland).",
        example_vi: "Berlin nằm ở phía Đông của nước Đức."
    },
    {
        word: "Westen", article: "der", gender: "der", plural: "Tính từ: westlich",
        indefinite: "im Westen von", negation: "westlich von",
        meaning: "phía Tây, miền Tây", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). Tính từ là 'westlich' (không có Umlaut).",
        example: "Köln liegt im Westen von Deutschland (westlich von Deutschland).",
        example_vi: "Köln nằm ở phía Tây của nước Đức."
    },
    {
        word: "Nordosten", article: "der", gender: "der", plural: "Tính từ: nordöstlich",
        indefinite: "im Nordosten von", negation: "nordöstlich von",
        meaning: "phía Đông Bắc (ghép Bắc + Đông)", category: "Phương hướng & Bản đồ",
        rule: "Tiếng Đức đặt Bắc (Nord-) trước Đông (-osten). Tính từ: nordöstlich.",
        example: "Hai Phong liegt im Nordosten von Vietnam (nordöstlich von Vietnam).",
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
        rule: "Danh từ ghép (das Haus + die Aufgabe) -> lấy giống cái (die), thường dùng ở dạng số nhiều: die Hausaufgaben machen.",
        example: "Er macht die Hausaufgaben. – Was macht er? / Macht er die Hausaufgaben?",
        example_vi: "Anh ấy làm bài tập về nhà. – Anh ấy làm gì? / Anh ấy có làm bài tập về nhà không?"
    }
];

let currentLexikonFilter = "all";
let currentLexikonSearchQuery = "";

const LEXIKON_FILTERS = [
    { id: "all", label: "Tất cả" },
    { id: "der", label: "🔵 Giống đực - der (Maskulinum)" },
    { id: "die", label: "🔴 Giống cái - die (Femininum)" },
    { id: "das", label: "🟢 Giống trung - das (Neutrum)" },
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

if (typeof window !== 'undefined') {
    window.GERMAN_LEXIKON_DB = GERMAN_LEXIKON_DB;
    window.renderLexikon = renderLexikon;
    window.updateLexikonUI = updateLexikonUI;
    window.setLexikonFilter = setLexikonFilter;
    window.onLexikonSearchChange = onLexikonSearchChange;
    window.clearLexikonSearch = clearLexikonSearch;
}
