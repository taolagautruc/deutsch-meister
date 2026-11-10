# ĐẶC TẢ KỸ THUẬT CẢI TIẾN TRIỆT ĐỂ BÀI TẬP BÀI 8 (A1): THỰC CHIẾN CHỈ ĐƯỜNG TRÊN BẢN ĐỒ, CHUYÊN SÂU TỪ VỰNG & GIỚI TỪ AKKUSATIV / DATIV, CẤM LẶP LÝ THUYẾT & CẤM LỘ GỢI Ý (`DEUTSCHMEISTER`)

> **CHỈ THỊ BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT (ƯU TIÊN TỐIượng):**
>
> ### 🚨 1. XÓA BỎ NGAY LẬP TỨC MỌI "GỢI Ý LÀM LỘ ĐÁP ÁN" TRÊN ĐỀ BÀI & TRÊN HÌNH VẼ SVG (`STRICT NO-SPOILER & BLIND-TEST POLICY`)
> Hiện tại phần bài tập Bài 8 đang mắc lỗi nghiêm trọng là **làm lộ đáp án và gợi ý ngay trên đề bài hoặc trên hình minh họa**. Antigravity IDE phải thực hiện cuộc tổng rà soát và **XÓA SẠCH 100%** các yếu tố sau khỏi trường `question`, `display_sentence` và hình vẽ `city_map_svg.js`:
> 1. **CẤM gợi ý giống của danh từ trong đề bài**:
>    * ❌ **SAI (Đang bị lộ)**: `... gehen ___ Berliner Dom (der Dom)` hoặc `... laufen ___ Schlossbrücke (die Brücke)` hoặc `... am Bundeskanzleramt (das Amt) vorbei`.
>    * ✅ **ĐÚNG (Chuẩn kiểm tra thực lực)**: `... gehen ___ Berliner Dom` hoặc `... laufen ___ Schlossbrücke`. Người học **bắt buộc phải tự nhớ** `Dom` là `der`, `Brücke` là `die`, `Amt` là `das`!
> 2. **CẤM gợi ý Cách ngữ pháp (`Akkusativ / Dativ`) hoặc công thức ghép từ trong đề bài**:
>    * ❌ **SAI (Đang bị lộ)**: `Điền giới từ (+ Akkusativ)...`, `Điền cụm từ thu gọn (zu + der)...`, `Điền giới từ (an + dem)...`, `Điền mạo từ ở Dativ...`.
>    * ✅ **ĐÚNG**: Chỉ nêu yêu cầu trung lập hoặc hiển thị câu tiếng Đức có ô trống `___`. Người học phải tự phân tích động từ/giới từ để quyết định dùng `Akkusativ` hay `Dativ`.
> 3. **CẤM chèn tiếng Việt dịch nghĩa hoặc gợi ý tiếng Việt vào trong câu hỏi Ngữ pháp / Trắc nghiệm / Điền khuyết tiếng Đức**:
>    * ❌ **SAI (Đang bị lộ)**: *„An der Ampel gehen Sie bitte hier ___, nicht links! (Tại đèn giao thông xin Ngài hãy rẽ phải ở đây, đừng rẽ trái!)“* $\rightarrow$ Dịch ra tiếng Việt ngay trong đề bài như vậy làm người học biết ngay đáp án là `rechts` mà không cần đọc hiểu câu tiếng Đức!
>    * ✅ **ĐÚNG**: Trong các dạng `trac_nghiem`, `dien_khuyet`, `dien_tao_cau`, `nghe_dien`, đề bài (`question`) **CHỈ hiển thị ngữ cảnh/câu tiếng Đức thuần túy** (kèm bản đồ SVG). Bản dịch tiếng Việt (`translation_vi`) và lời giải thích (`explanation`) **CHỈ ĐƯỢC HIỂN THỊ SAU KHI NGƯỜI HỌC ĐÃ BẤM NỘP ĐÁP ÁN**! (Chỉ riêng các dạng bài *Dịch Việt $\rightarrow$ Đức* và *Dịch Đức $\rightarrow$ Việt* mới hiển thị câu gốc cần dịch).
> 4. **CẤM làm lộ đáp án trên Hình vẽ Sơ đồ & Bản đồ SVG (`Clean Unspoiled SVG Maps`)**:
>    * ❌ **SAI (Đang bị lộ trên hình)**: Trên hình vẽ cổng vòm lại ghi sẵn chữ `durch` hoặc `das Tor`; trên hình vẽ cây cầu lại ghi chữ `über die Brücke`; trên bản đồ lại ghi sẵn `die Post`, `der Bahnhof`, `an der Bank vorbei`.
>    * ✅ **ĐÚNG**:
>      * Trên **Bản đồ đường phố (`Street Grid Map`)**: Các tòa nhà chỉ được hiển thị **Biểu tượng Icon + Tên danh từ gốc KHÔNG KÈM MẠO TỪ** (ví dụ: `🏦 Bank`, `📮 Post`, `⛪ Kirche`, `🚉 Bahnhof`, `🏰 Schloss`, `🎬 Kino`, `🏥 Krankenhaus`, `🛍️ Einkaufszentrum`, `🏫 Universität`, `🏛️ Rathaus`, `🚦 Ampel`). Tuyệt đối không ghi `die Bank`, `der Bahnhof`, `das Kino` lên bản đồ!
>      * Trên **Sơ đồ mũi tên chỉ hướng (`Direction Diagram`)**: Chỉ vẽ hình học không gian (con đường, ngã tư, tòa nhà, cây cầu, cổng vòm, quảng trường) và **đường mũi tên chuyển động màu nổi bật**, tuyệt đối **KHÔNG viết bất kỳ chữ tiếng Đức nào (`vorbei`, `durch`, `über`, `entlang`, `links`, `rechts`) lên hình SVG**!

---

### 🧠 2. CẤM LẶP LẠI CÂU CỦA PHẦN LÝ THUYẾT — SÁNG TẠO 100% NGỮ CẢNH MỚI (`ZERO THEORY REPETITION`)
* **CẤM bê nguyên xi** đoạn văn *„Paula und Alex kommen aus Madrid...“*, tin nhắn *„Hi Julia! Berlin ist super!...“*, hay 2 câu lộ trình mẫu trên bảng viết vào phần bài tập. Tài liệu lý thuyết chỉ là khung kiến thức để AI tham khảo từ vựng và cấu trúc ngữ pháp.
* **Trọng tâm của 100 bài tập Bài 8 mới**:
  1. **Tình huống thực chiến Nhìn Bản Đồ Chỉ Đường (`Real-life Map Navigation Roleplay`)**: Đặt người học vào vai một người dân địa phương đang nhìn bản đồ để chỉ đường cho:
     * **Một vị khách du lịch nước ngoài / người lớn tuổi trên phố** $\rightarrow$ Dùng ngôi trang trọng **`Sie`** (*„Gehen Sie...“, „Fahren Sie...“, „Nehmen Sie...“, „Sie müssen...“, „Sie sehen...“*).
     * **Một người bạn thân hoặc em ruột mới đến thành phố** $\rightarrow$ Dùng ngôi thân mật số ít **`du`** (*„Geh zuerst...“, „Fahr...“, „Du musst...“, „Dann siehst du...“*).
     * **Một nhóm bạn bè hoặc hai người thân trong gia đình** $\rightarrow$ Dùng ngôi thân mật số nhiều **`ihr`** (*„Geht zuerst...“, „Fahrt...“, „Ihr müsst...“, „Rechts seht ihr...“*).
     * **Miêu tả lộ trình di chuyển của ngôi thứ 3** (`der Tourist`, `meine Tante`, `Herr Weber`, `die Reisegruppe`, `der Taxifahrer`, `wir`) kết hợp cả 6 động từ khuyết thiếu (`wollen, müssen, können, möchten, dürfen, sollen`).
  2. **Xoay trục Từ vựng Địa điểm + Phân biệt Giới từ `Akkusativ` vs. `Dativ`**:
     * Bắt buộc người học phân biệt rõ:
       * **`an + Dativ + vorbei`** (`am Bahnhof vorbei`, `am Schloss vorbei`, `an der Kirche vorbei`, `an der Post vorbei`)
       * **`bis zu + Dativ`** (`bis zum Markt`, `bis zum Stadttor`, `bis zur Ampel`, `bis zur dritten Kreuzung`)
       * **`zu + Dativ` (`zum / zur`)** vs. **`in + Akkusativ` (`in den / in die / ins`)** vs. **`in + Dativ` (`im / in der` — khi hỏi vị trí tĩnh `Wo?`)**
       * **`durch + Akkusativ`** (`durch den Park`, `durch das Stadttor`, `durch die Fußgängerzone`)
       * **`über + Akkusativ`** (`über den Alexanderplatz`, `über die Brücke`, `über die Kreuzung`)
       * **`[Akkusativ] + entlang`** (`den Fluss entlang`, `die Friedrichstraße entlang`, `den Kanal entlang`).

---

## PHẦN 1: THIẾT KẾ MODULE BẢN ĐỒ & SƠ ĐỒ SVG KHÔNG LỘ ĐÁP ÁN (`static/js/city_map_svg.js`)

Antigravity IDE cần cập nhật tệp `static/js/city_map_svg.js` để cung cấp **2 chế độ hiển thị khác nhau**:
1. **Chế độ Lý thuyết (`mode: "theory"`)**: Có chú thích đầy đủ để người học tiếp thu kiến thức mới.
2. **Chế độ Bài tập & Đấu trường (`mode: "quiz_blind"`)**: **Tắt toàn bộ chữ gợi ý và mạo từ trên hình SVG**. Cụ thể:

### 1.1. Quy Chuẩn Bản Đồ Lưới Thành Phố Trong Bài Tập (`Quiz Street Grid Map SVG`)
Bản đồ thành phố trong phần Bài tập là một lưới đường phố trực quan (gồm 3 đường dọc giao với 3 đường ngang tạo thành các ngã tư đánh số tự động theo hướng đi từ vị trí **`📍 START`** kèm mũi tên chỉ hướng mặt ban đầu của người đi):
* **Các nhãn hiển thị hợp lệ trên Bản đồ Bài tập**:
  * Điểm bắt đầu: **`📍 START`** (có mũi tên định hướng ban đầu $\uparrow$).
  * Các công trình kiến trúc trên bản đồ **chỉ ghi Danh từ gốc (Không có `der/die/das`)**:
    * `🏦 Bank`, `⛪ Kirche`, `📮 Post`, `🚉 Bahnhof`, `✈️ Flughafen`, `🛒 Supermarkt`, `🌳 Park`, `🦁 Zoo`, `🏰 Schloss`, `⛩️ Stadttor`, `🎬 Kino`, `🏥 Krankenhaus`, `🛍️ Einkaufszentrum`, `🏫 Schule`, `🎓 Universität`, `🏛️ Rathaus`, `🏨 Hotel`, `🎭 Staatsoper`, `🗼 Fernsehturm`, `⛪ Berliner Dom`, `🏛️ Reichstag`, `🏢 Bundeskanzleramt`.
  * Khi câu hỏi yêu cầu tìm điểm đích (`Ziel`), tòa nhà đích được đánh dấu bằng **`❓ [A]`**, **`❓ [B]`**, **`❓ [C]`**, **`❓ [D]`** ở 4 vị trí khác nhau trên bản đồ để người học tự dò theo lời chỉ đường bằng tiếng Đức và xác định xem người đó sẽ đến tòa nhà nào, hoặc nhìn vạch lộ trình từ `📍 START` đến `🏁 ZIEL` để tự điền câu chỉ đường!

### 1.2. Quy Chuẩn 12 Sơ Đồ Mũi Tên Không Gian Trong Bài Tập (`Quiz Spatial Arrow Icons`)
Trong chế độ bài tập (`quiz_blind`), 12 sơ đồ (`quiz_icon_1` $\rightarrow$ `quiz_icon_12`) chỉ hiển thị hình vẽ đường phố, biểu tượng vật thể (cây cầu, cổng vòm, quảng trường tròn, cột đèn 3 màu, nhà thờ, ngã tư) và **mũi tên chuyển động màu vàng/xanh**, tuyệt đối không hiển thị bất kỳ chữ cái tiếng Đức nào trên hình.

---

## PHẦN 2: KHO 100 CÂU HỎI BÀI TẬP BÀI 8 MỚI HOÀN TOÀN (`lessons/a1/seed_a1_b8.py`) — SÁNG TẠO, THỰC CHIẾN BẢN ĐỒ & KHÔNG LỘ GỢI Ý

Dưới đây là đặc tả chi tiết **100 câu hỏi hoàn toàn mới** (không lặp lại bất kỳ câu nào của phần Lý thuyết, không chứa gợi ý giống/cách hay tiếng Việt làm lộ đáp án trong đề bài):

### NHÓM 1: TRẮC NGHIỆM THỰC CHIẾN BẢN ĐỒ, TỪ VỰNG & GIỚI TỪ AKKUSATIV / DATIV (`trac_nghiem` — 18 Câu: Câu 1 $\rightarrow$ Câu 18)

1. **Câu 1 (Nhìn Bản đồ SVG — Dò lộ trình của khách du lịch để tìm Điểm Đích)**:
   * `visual_svg`: Render **`map_route_finder_1`** *(Vị trí `📍 START` ở góc dưới bên trái nhìn lên hướng Bắc. Trên bản đồ có các tòa nhà ghi tên không mạo từ: `🏥 Krankenhaus`, `🏦 Bank`, `🎬 Kino`, `📮 Post`, `🚉 Bahnhof`, `🏰 Schloss`. Không vẽ vạch sẵn để người học tự dò theo lời chỉ đường trong câu hỏi)*.
   * `question`: *„Ein Tourist steht am Punkt START und fragt nach dem Weg. Sie sagen: ‚Gehen Sie zuerst geradeaus über die erste Kreuzung! An der zweiten Kreuzung biegen Sie rechts ab. Gehen Sie dann am Krankenhaus vorbei bis zur Ampel. Direkt links neben der Ampel liegt das Gebäude.‘ — Welches Ziel sucht der Tourist?“*
   * `options`: `["A. Das Kino", "B. Den Bahnhof", "C. Das Schloss", "D. Die Post"]`
   * `answer`: `"A. Das Kino"`
   * `translation_vi` *(Chỉ hiện sau khi nộp bài)*: *"Một vị khách du lịch đứng ở điểm START và hỏi đường. Bạn nói: 'Đầu tiên Ngài hãy đi thẳng băng qua ngã tư thứ nhất! Ở ngã tư thứ hai Ngài rẽ phải. Sau đó Ngài đi ngang qua bệnh viện cho đến đèn giao thông. Ngay bên trái cạnh đèn giao thông là tòa nhà đó.' — Vị khách du lịch đang tìm đích đến nào?"*
   * `explanation` *(Chỉ hiện sau khi nộp bài)*: *"Dò trên bản đồ từ START: đi thẳng qua ngã tư 1 $\rightarrow$ đến ngã tư 2 rẽ phải $\rightarrow$ đi ngang qua Bệnh viện (`am Krankenhaus vorbei`) tới đèn giao thông (`bis zur Ampel`), nhìn sang bên trái (`links`) chính là Rạp chiếu phim (`das Kino`)."*

2. **Câu 2 (Nhìn Bản đồ SVG — Chỉ đường cho bạn thân ở ngôi `du`)**:
   * `visual_svg`: Render **`map_route_line_2`** *(Bản đồ vẽ sẵn vạch lộ trình màu xanh từ `📍 START`: đi thẳng $\rightarrow$ rẽ trái ở con đường thứ ba $\rightarrow$ đi xuyên qua công viên `🌳 Park` $\rightarrow$ đi qua cầu `🌉 Brücke` $\rightarrow$ đích đến bên phải là `🛍️ Einkaufszentrum`)*.
   * `question`: *„Dein Freund Jonas möchte zum Einkaufszentrum gehen. Welche Wegbeschreibung passt genau zur blauen Route auf der Karte?“*
   * `options`:
     * `"A. Geh zuerst geradeaus, dann die dritte Straße links! Lauf durch den Park und über die Brücke! Rechts siehst du das Einkaufszentrum."`
     * `"B. Geh zuerst geradeaus, dann die zweite Straße rechts! Lauf am Park vorbei und durch die Brücke! Links siehst du das Einkaufszentrum."`
     * `"C. Geh zuerst die erste Straße links, dann durch dem Park und über der Brücke bis zum Einkaufszentrum!"`
     * `"D. Geh geradeaus bis zur dritten Kreuzung rechts, dann den Park entlang und an der Brücke vorbei!"`
   * `answer`: `"A. Geh zuerst geradeaus, dann die dritte Straße links! Lauf durch den Park und über die Brücke! Rechts siehst du das Einkaufszentrum."`
   * `translation_vi`: *"Người bạn Jonas của bạn muốn đi đến trung tâm thương mại. Lời chỉ đường nào khớp chính xác với lộ trình màu xanh trên bản đồ?"*
   * `explanation`: *"Lộ trình trên bản đồ: đi thẳng (`geradeaus`) $\rightarrow$ rẽ trái ở đường thứ 3 (`die dritte Straße links`) $\rightarrow$ đi xuyên qua công viên (`durch den Park` — `durch + Akkusativ` với `der Park`) $\rightarrow$ đi qua cầu (`über die Brücke` — `über + Akkusativ` với `die Brücke`)."*

3. **Câu 3 (Nhìn Sơ đồ SVG không chữ — Phân biệt giới từ không gian)**:
   * `visual_svg`: Render **`quiz_spatial_3_steps`** *(Vẽ 3 hình liên tiếp không có chữ: Hình 1: Mũi tên đi lướt ngang qua mặt tiền Nhà hát Opera `🎭`; Hình 2: Mũi tên đi dọc theo bờ sông `🌊`; Hình 3: Mũi tên đi xuyên qua Cổng thành `⛩️`)*.
   * `question`: *„Welche Satzkette beschreibt die drei Bilder (1 -> 2 -> 3) grammatikalisch völlig korrekt?“*
   * `options`:
     * `"A. Zuerst gehen wir an der Staatsoper vorbei, dann den Fluss entlang und danach durch das Stadttor."`
     * `"B. Zuerst gehen wir an die Staatsoper vorbei, dann entlang dem Fluss und danach über das Stadttor."`
     * `"C. Zuerst gehen wir am Staatsoper vorbei, dann durch den Fluss und danach am Stadttor vorbei."`
     * `"D. Zuerst gehen wir durch die Staatsoper, dann über den Fluss und danach das Stadttor entlang."`
   * `answer`: `"A. Zuerst gehen wir an der Staatsoper vorbei, dann den Fluss entlang und danach durch das Stadttor."`
   * `translation_vi`: *"Chuỗi câu nào miêu tả cả 3 bức hình (1 -> 2 -> 3) hoàn toàn đúng ngữ pháp?"*
   * `explanation`: *"1. Đi ngang qua `die Staatsoper` (giống cái) dùng `an + Dativ + vorbei` $\rightarrow$ **`an der Staatsoper vorbei`**. 2. Đi dọc theo `der Fluss` (giống đực) dùng `Akkusativ + entlang` $\rightarrow$ **`den Fluss entlang`**. 3. Đi xuyên qua `das Stadttor` (giống trung) dùng `durch + Akkusativ` $\rightarrow$ **`durch das Stadttor`**."*

4. **Câu 4 (Tình huống Khách du lịch hỏi đường trên phố — Phân biệt 4 mẫu câu hỏi đường)**:
   * `question`: *„Eine ältere Dame spricht Sie auf der Straße in Berlin an. Welcher Fragesatz ist grammatikalisch FALSCH?“*
   * `options`:
     * `"A. Entschuldigung, ich suche das Bundeskanzleramt."`
     * `"B. Entschuldigung, wie komme ich zum Museumsinsel?"`
     * `"C. Entschuldigung, wo geht es hier zum Hauptbahnhof?"`
     * `"D. Entschuldigung, wo ist hier eine Bank?"`
   * `answer`: `"B. Entschuldigung, wie komme ich zum Museumsinsel?"`
   * `translation_vi`: *"Một bà lão hỏi chuyện bạn trên đường phố ở Berlin. Câu hỏi đường nào dưới đây bị SAI ngữ pháp?"*
   * `explanation`: *"Danh từ `die Museumsinsel` (Đảo Bảo tàng) mang giống cái (`die` — vì `die Insel`), nên khi đi với giới từ `zu + Dativ` bắt buộc phải dùng **`zur Museumsinsel`** (`zu + der`), không được dùng `zum`."*

5. **Câu 5 (Chỉ đường cho 2 người bạn bằng ngôi `ihr` kèm giới từ `an ... vorbei` & `bis zu`)**:
   * `visual_svg`: Render **`map_route_line_3`** *(Bản đồ vẽ lộ trình từ `📍 START`: đi ngang qua `🎓 Universität` và `⛪ Dom` $\rightarrow$ đi tới `🚦 Ampel` $\rightarrow$ rẽ trái $\rightarrow$ băng qua `⭕ Marktplatz`)*.
   * `question`: *„Deine Freunde Clara und Tim suchen das historische Rathaus. Du erklärst ihnen den Weg auf der Karte: ‚Geht zuerst ___ Humboldt-Universität und ___ Berliner Dom vorbei, dann geradeaus bis ___ Ampel und über ___ Marktplatz!‘“*
   * `options`:
     * `"A. an der / am / zur / den"`
     * `"B. an die / an den / zu der / dem"`
     * `"C. am / an der / zum / das"`
     * `"D. an der / am / zum / den"`
   * `answer`: `"A. an der / am / zur / den"`
   * `translation_vi`: *"Hai người bạn Clara và Tim của bạn đang tìm tòa thị chính cổ. Bạn giải thích đường đi trên bản đồ cho họ: 'Đầu tiên các bạn hãy đi ngang qua Đại học Humboldt và Nhà thờ lớn Berlin, sau đó đi thẳng cho đến đèn giao thông và băng qua quảng trường chợ!'"*
   * `explanation`: *"`die Humboldt-Universität` (`f`) $\rightarrow$ **`an der ... vorbei`**; `der Berliner Dom` (`m`) $\rightarrow$ **`am ... vorbei`**; `die Ampel` (`f`) $\rightarrow$ **`bis zur Ampel`**; `der Marktplatz` (`m`) sau `über + Akkusativ` $\rightarrow$ **`über den Marktplatz`**."*

6. **Câu 6 (Kiểm tra chuyên sâu Giống `der/die/das` của 14 Danh lam thắng cảnh Berlin & Địa điểm thành phố)**:
   * `question`: *„In welcher Reihe haben ALLE vier Substantive denselben Artikel im Singular?“*
   * `options`:
     * `"A. der Reichstag — der Hafen — der Fernsehturm — der Potsdamer Platz"`
     * `"B. die Staatsoper — die Brücke — die Stadttor — die Friedrichstraße"`
     * `"C. das Schloss — das Einkaufszentrum — das Bank — das Bundeskanzleramt"`
     * `"D. der Bahnhof — der Markt — der Museumsinsel — der Zoo"`
   * `answer`: `"A. der Reichstag — der Hafen — der Fernsehturm — der Potsdamer Platz"`
   * `translation_vi`: *"Ở dòng nào TẤT CẢ 4 danh từ đều có cùng một mạo từ ở dạng số ít?"*
   * `explanation`: *"Ở câu A, cả 4 danh từ đều mang giống đực (`der`): `der Reichstag`, `der Hafen`, `der Fernsehturm`, `der Potsdamer Platz`. (Câu B sai vì `das Stadttor`; Câu C sai vì `die Bank`; Câu D sai vì `die Museumsinsel`)."*

7. **Câu 7 (Kiểm tra chuyên sâu dạng Số Nhiều của danh từ địa điểm trong thành phố)**:
   * `question`: *„Großstädte in Europa: Welcher Satz verwendet ALLE Pluralformen korrekt?“*
   * `options`:
     * `"A. In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks."`
     * `"B. In dieser Metropole gibt es drei Flughافen, vier alte Schlosse, zwei große Einkaufszentrums und viele grüne Parke."`
     * `"C. In dieser Metropole gibt es drei Flughäfe, vier alte Schlösse, zwei große Einkaufszentren und viele grüne Parks."`
     * `"D. In dieser Metropole gibt es zwei Hauptposten, fünf Bahnhofen und zehn Krankenhauser."`
   * `answer`: `"A. In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks."`
   * `translation_vi`: *"Các đại đô thị ở châu Âu: Câu nào sử dụng TẤT CẢ các dạng số nhiều chính xác?"*
   * `explanation`: *"`der Flughafen` $\rightarrow$ **`die Flughäfen`**; `das Schloss` $\rightarrow$ **`die Schlösser`**; `das Einkaufszentrum` $\rightarrow$ **`die Einkaufszentren`**; `der Park` $\rightarrow$ **`die Parks`**. (Lưu ý: `die Post` chỉ dùng ở số ít, `Bahnhof` $\rightarrow$ `Bahnhöfe`, `Krankenhaus` $\rightarrow$ `Krankenhäuser`)."*

8. **Câu 8 (Phân biệt 2 dạng số nhiều của `die Bank`: `die Banken` vs. `die Bänke`)**:
   * `question`: *„Ergänzen Sie die passenden Pluralformen: ‚In der Innenstadt arbeiten viele Menschen in den internationalen ___, und im Stadtpark sitzen die Rentner gern auf den sonnigen ___.‘“*
   * `options`:
     * `"A. Banken / Bänken"`
     * `"B. Bänken / Banken"`
     * `"C. Banken / Banken"`
     * `"D. Bänke / Bänke"`
   * `answer`: `"A. Banken / Bänken"`
   * `translation_vi`: *"Điền dạng số nhiều phù hợp: 'Ở khu trung tâm thành phố nhiều người làm việc trong các ngân hàng quốc tế, và trong công viên thành phố những người hưu trí thích ngồi trên những chiếc ghế băng dài đầy nắng.'"*
   * `explanation`: *"`die Bank` nghĩa là *ngân hàng* có số nhiều là `die Banken` (ở `Dativ Plural` sau `in den` là **`Banken`**). `die Bank` nghĩa là *ghế băng dài* có số nhiều là `die Bänke` (ở `Dativ Plural` sau `auf den` thêm `-n` thành **`Bänken`**)."*

9. **Câu 9 (Phân biệt `in + Akkusativ` [Wohin?] vs. `in + Dativ` [Wo?] vs. `zu + Dativ`)**:
   * `question`: *„Am Samstagabend möchten meine Cousine und ich ___ Staatsoper gehen, denn heute singt ein berühmter Tenor ___ Staatsoper. Davor fahren wir noch kurz ___ Alexanderplatz.“*
   * `options`:
     * `"A. in die / in der / zum"`
     * `"B. in der / in die / in den"`
     * `"C. zur / in die / am"`
     * `"D. ins / im / zum"`
   * `answer`: `"A. in die / in der / zum"`
   * `translation_vi`: *"Tối thứ Bảy chị họ tôi và tôi muốn đi vào Nhà hát Opera Quốc gia, vì hôm nay một giọng nam cao nổi tiếng hát ở trong Nhà hát Opera. Trước đó chúng tôi còn đi qua Quảng trường Alexander một lát."*
   * `explanation`: *"1. `gehen` (di chuyển vào trong `Wohin?` + `Akkusativ`) với `die Staatsoper` $\rightarrow$ **`in die Staatsoper`**. 2. `singen` (hành động diễn ra ở vị trí tĩnh `Wo?` + `Dativ`) với `die Staatsoper` $\rightarrow$ **`in der Staatsoper`**. 3. Đi tới quảng trường `der Alexanderplatz` (`zu + Dativ`) $\rightarrow$ **`zum Alexanderplatz`**."*

10. **Câu 10 (Phân biệt `durch` vs. `über` vs. `entlang` trong tình huống dẫn đoàn du lịch)**:
    * `question`: *„Der Reiseleiter sagt zu den Gästen: ‚Wir spazieren jetzt zuerst die Spree ___, gehen dann ___ die alte Holzbrücke und laufen schließlich ___ den dunklen Tunnel zum Schloss.‘“*
    * `options`:
      * `"A. entlang / über / durch"`
      * `"B. über / durch / entlang"`
      * `"C. durch / entlang / über"`
      * `"D. vorbei / über / in"`
    * `answer`: `"A. entlang / über / durch"`
    * `translation_vi`: *"Người hướng dẫn viên du lịch nói với các vị khách: 'Bây giờ đầu tiên chúng ta đi dạo dọc theo sông Spree, sau đó đi qua cây cầu gỗ cổ và cuối cùng đi bộ xuyên qua đường hầm tối để tới cung điện.'"*
    * `explanation`: *"Đi dọc theo sông Spree (đứng sau danh từ) dùng **`entlang`** (`die Spree entlang`); đi vượt qua trên mặt cầu dùng **`über`** (`über die alte Holzbrücke`); đi xuyên qua lòng đường hầm (`der Tunnel`) dùng **`durch`** (`durch den dunklen Tunnel`)."*

11. **Câu 11 (Kết hợp Động từ khuyết thiếu `wollen`, `müssen`, `können`, `möchten` trong tình huống hỏi đường)**:
    * `question`: *„Familie Schneider ist neu in München. Herr Schneider ___ unbedingt das Deutsche Museum besichtigen, aber seine Kinder sind müde und ___ nicht mehr weit laufen. Deshalb ___ sie jetzt ein Taxi zum Hotel nehmen.“*
    * `options`:
      * `"A. will / können / müssen"`
      * `"B. wollen / kann / muss"`
      * `"C. willst / könnt / möchten"`
      * `"D. möchte / müssen / will"`
    * `answer`: `"A. will / können / müssen"`
    * `translation_vi`: *"Gia đình ông Schneider mới đến München. Ông Schneider nhất định muốn tham quan Bảo tàng Đức, nhưng các con của ông đã mỏi chân và không thể đi bộ xa thêm nữa. Vì vậy bây giờ họ phải bắt một chiếc taxi về khách sạn."*
    * `explanation`: *"`Herr Schneider` (`er`) $\rightarrow$ **`will`**; `seine Kinder` (`sie` - số nhiều) $\rightarrow$ **`können`**; `sie` (họ) $\rightarrow$ **`müssen`**."*

12. **Câu 12 (Nhìn Bản đồ SVG — Tìm lỗi sai trong lời chỉ đường)**:
    * `visual_svg`: Render **`map_error_check_1`** *(Bản đồ hiển thị lộ trình từ `📍 START` tới `🏰 Schloss Bellevue`: đi thẳng $\rightarrow$ rẽ trái ở ngã tư thứ nhất $\rightarrow$ đi ngang qua `🏫 Schule` $\rightarrow$ đi qua `🌉 Brücke` $\rightarrow$ bên phải là `🏰 Schloss Bellevue`)*.
    * `question`: *„Ein Passant erklärt Ihnen den Weg zum Schloss Bellevue nach der Karte oben. In welchem Satz hat er einen Richtungsfehler im Vergleich zur eingezeichneten Route gemacht?“*
    * `options`:
      * `"A. Zuerst gehen Sie vom Startpunkt aus geradeaus bis zur ersten Kreuzung."`
      * `"B. An der ersten Kreuzung biegen Sie bitte rechts ab."`
      * `"C. Danach gehen Sie geradeaus an der Schule vorbei."`
      * `"D. Zum Schluss laufen Sie über die Brücke, und rechts sehen Sie das Schloss Bellevue."`
    * `answer`: `"B. An der ersten Kreuzung biegen Sie bitte rechts ab."`
    * `translation_vi`: *"Một người đi đường giải thích cho bạn đường tới Cung điện Bellevue theo bản đồ trên. Ở câu nào người đó đã chỉ SAI hướng so với lộ trình vẽ trên bản đồ?"*
    * `explanation`: *"Trên bản đồ, tại ngã tư thứ nhất (`an der ersten Kreuzung`), mũi tên quẹo sang bên trái (**`links`**), nhưng câu B lại nói `rechts` (bên phải)."*

13. **Câu 13 (Phân biệt `suchen + Akkusativ` vs. `sein + Nominativ` vs. `vorbeigehen an + Dativ`)**:
    * `question`: *„Touristen im Stadtzentrum: ‚Entschuldigung, wir suchen ___ neuen Hauptbahnhof.‘ — ‚Gehen Sie einfach an ___ alten Kirche vorbei, dann steht ___ Hauptbahnhof direkt vor Ihnen!‘“*
    * `options`:
      * `"A. den / der / der"`
      * `"B. der / die / den"`
      * `"C. dem / der / der"`
      * `"D. den / die / dem"`
    * `answer`: `"A. den / der / der"`
    * `translation_vi`: *"Du khách ở trung tâm thành phố: 'Xin lỗi, chúng tôi đang tìm nhà ga trung tâm mới.' — 'Các ngài cứ đi ngang qua nhà thờ cổ, sau đó nhà ga trung tâm nằm ngay trước mặt các ngài!'"*
    * `explanation`: *"1. Sau động từ `suchen` cần `Akkusativ` (`der Hauptbahnhof` $\rightarrow$ **`den`**). 2. Trong cụm `an ... vorbei` cần `Dativ` (`die Kirche` $\rightarrow$ **`der`**). 3. Chủ ngữ của động từ `steht` ở `Nominativ` (`der Hauptbahnhof` $\rightarrow$ **`der`**)."*

14. **Câu 14 (Số thứ tự đứng trước danh từ chỉ đường ở `Akkusativ` vs. `Dativ`)**:
    * `question`: *„Taxifahrer in Wien: ‚Muss ich hier schon abbiegen?‘ — ‚Nein, fahren Sie bitte erst die ___ Straße links und halten Sie dann an der ___ Ampel vor dem Theater!‘“*
    * `options`:
      * `"A. dritte / zweiten"`
      * `"B. dritten / zweite"`
      * `"C. dritter / zweiter"`
      * `"D.em dritten / der zweite"`
    * `answer`: `"A. dritte / zweiten"`
    * `translation_vi`: *"Tài xế taxi ở Viên: 'Tôi phải rẽ ngay ở đây rồi à?' — 'Không, xin anh hãy chạy tới con đường thứ ba mới rẽ trái rồi dừng lại ở chỗ đèn giao thông thứ hai trước nhà hát!'"*
    * `explanation`: *"Trong cụm `die ___ Straße links` (`Akkusativ` giống cái sau `die`), số thứ tự có đuôi **`-e`** (`die dritte Straße`). Trong cụm `an der ___ Ampel` (`Dativ` giống cái sau `an der`), số thứ tự bắt buộc thêm đuôi **`-en`** (`an der zweiten Ampel` — tương tự như `bis zur zweiten Kreuzung`)."*

15. **Câu 15 (Đảo ngữ khi đứng đầu câu bằng các trạng từ liên kết `Zuerst, Dann, Danach, Anschließend`)**:
    * `question`: *„Welcher Satz über den Familienausflug in Hamburg hat die einzig richtige Wortstellung (Verb auf Position 2)?“*
    * `options`:
      * `"A. Zuerst wir wollen den großen Hafen besichtigen, und danach wir gehen ins Fischrestaurant."`
      * `"B. Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder eine Hafenrundfahrt machen."`
      * `"C. Zuerst wollen besichtigen wir den großen Hafen, und danach die Kinder möchten Eis essen."`
      * `"D. Wir zuerst wollen den großen Hafen besichtigen, und anschließend wollen gehen wir in den Zoo."`
    * `answer`: `"B. Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder eine Hafenrundfahrt machen."`
    * `translation_vi`: *"Câu nào kể về chuyến dã ngoại gia đình ở Hamburg có trật tự từ đúng duy nhất (Động từ chia ở vị trí số 2)?"*
    * `explanation`: *"Khi trạng từ `Zuerst` hoặc `danach` đứng đầu mệnh đề (vị trí số 1), động từ khuyết thiếu đã chia (`wollen`, `möchten`) bắt buộc phải đứng ngay vị trí số 2 trước chủ ngữ (`Zuerst wollen wir...`, `danach möchten die Kinder...`), còn động từ nguyên mẫu (`besichtigen`, `machen`) đứng ở cuối câu."*

16. **Câu 16 (Giới từ đi với phương tiện giao thông `mit + Dativ` kết hợp giới từ chỉ đường)**:
    * `question`: *„Wie kommen deine Großeltern morgen vom Hotel zum Schloss Sanssouci? — Sie fahren zuerst mit ___ U-Bahn bis ___ Hauptbahnhof und nehmen dort ___ Bus direkt ___ Schloss.“*
    * `options`:
      * `"A. der / zum / den / zum"`
      * `"B. die / zur / der / ins"`
      * `"C. dem / am / den / nach"`
      * `"D. der / in den / dem / zum"`
    * `answer`: `"A. der / zum / den / zum"`
    * `translation_vi`: *"Ngày mai ông bà của bạn đi từ khách sạn đến Cung điện Sanssouci bằng cách nào? — Đầu tiên ông bà đi bằng tàu điện ngầm cho đến nhà ga trung tâm và ở đó bắt chiếc xe buýt đi thẳng tới cung điện."*
    * `explanation`: *"1. `mit + Dativ`: `die U-Bahn` $\rightarrow$ **`mit der U-Bahn`**. 2. `bis zu + Dativ`: `der Hauptbahnhof` $\rightarrow$ **`bis zum Hauptbahnhof`**. 3. `nehmen + Akkusativ`: `der Bus` $\rightarrow$ **`nehmen den Bus`**. 4. `zu + Dativ`: `das Schloss` $\rightarrow$ **`zum Schloss`**."*

17. **Câu 17 (Chọn lời chỉ đường hợp lý khi người hỏi đang lái xe ô tô `Fahren Sie...` vs. đi bộ)**:
    * `question`: *„Ein Autofahrer fragt Sie nach dem Weg zum Flughafen. Welche Antwort ist logisch und grammatikalisch richtig?“*
    * `options`:
      * `"A. Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts auf die Autobahn zum Flughafen!"`
      * `"B. Gehen Sie zu Fuß durch das Wohnzimmer und über den kleinen Supermarkt bis in den Flughafen!"`
      * `"C. Fahren Sie am Flughafen vorbei, durch die Post und dann unter der Bank entlang!"`
      * `"D. Laufen Sie mit dem Auto an die Kreuzung vorbei und biegen Sie auf der Ampel ab!"`
    * `answer`: `"A. Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts auf die Autobahn zum Flughafen!"`
    * `translation_vi`: *"Một tài xế ô tô hỏi bạn đường ra sân bay. Câu trả lời nào vừa hợp logic thực tế vừa đúng ngữ pháp?"*
    * `explanation`: *"Tài xế đang lái xe nên dùng mệnh lệnh `Fahren Sie...`: chạy dọc theo đường chính (`diese Hauptstraße entlang`), qua cây cầu lớn (`über die große Brücke`) và sau đèn giao thông thứ hai rẽ phải lên đường cao tốc ra sân bay (`zum Flughafen`)."*

18. **Câu 18 (Tổng hợp đọc hiểu bảng chỉ dẫn du lịch trong thành phố)**:
    * `question`: *„Lesen Sie die Informationstafel am Bahnhof: ‚Vom Hauptbahnhof erreichen Sie die Museumsinsel in 15 Minuten zu Fuß: Gehen Sie durch den Bahnhofspark, über die Friedrichbrücke und an der Staatsoper vorbei.‘ — Was müssen die Besucher auf diesem Weg tun?“*
    * `options`:
      * `"A. Sie müssen eine Brücke überqueren und einen Park durchqueren."`
      * `"B. Sie müssen mit dem Bus in die Staatsoper hineingehen."`
      * `"C. Sie müssen vor der Brücke links zum Flughafen abbiegen."`
      * `"D. Sie dürfen den Bahnhofspark nicht betreten."`
    * `answer`: `"A. Sie müssen eine Brücke überqueren und einen Park durchqueren."`
    * `translation_vi`: *"Hãy đọc bảng thông tin tại nhà ga: 'Từ nhà ga trung tâm, quý khách đi bộ 15 phút là tới Đảo Bảo tàng: Hãy đi xuyên qua công viên nhà ga, đi qua cầu Friedrich và đi ngang qua Nhà hát Opera Quốc gia.' — Khách tham quan phải làm gì trên quãng đường này?"*
    * `explanation`: *"`durch den Bahnhofspark gehen` = đi xuyên qua một công viên (`einen Park durchqueren`); `über die Friedrichbrücke gehen` = băng qua một cây cầu (`eine Brücke überqueren`)."*

---

### NHÓM 2: ĐIỀN KHUYẾT CHUYÊN SÂU — KHÔNG GỢI Ý GIỐNG / CÁCH / TIẾNG VIỆT (`dien_khuyet` — 15 Câu: Câu 19 $\rightarrow$ Câu 33)
*(Lưu ý: Trong giao diện làm bài, học viên chỉ nhìn thấy câu tiếng Đức và bản đồ SVG nếu có; tuyệt đối không hiển thị gợi ý trong ngoặc. Sau khi nộp bài mới hiện bản dịch tiếng Việt và giải thích).*

19. **Câu 19 (Nhìn Bản đồ SVG `map_fill_1` — Đi ngang qua Ngân hàng & Bệnh viện)**:
    * `visual_svg`: Render **`map_fill_1`** *(Vạch lộ trình đi ngang qua `🏦 Bank` rồi rẽ trái tới `🏥 Krankenhaus`)*.
    * `question`: *„Entschuldigung, wie komme ich zum Krankenhaus? — Gehen Sie zuerst geradeaus an ___ Bank vorbei und biegen Sie dann links ab!“*
    * `accepted_answers`: `["der"]`
    * `translation_vi`: *"Xin lỗi, làm thế nào tôi đi đến được bệnh viện? — Đầu tiên Ngài hãy đi thẳng ngang qua ngân hàng rồi sau đó rẽ trái!"*
    * `explanation`: *"Danh từ `Bank` mang giống cái (`die Bank`). Trong cấu trúc `an + Dativ + vorbei`, mạo từ `die` đổi thành **`der`** (`an der Bank vorbei`)."*

20. **Câu 20 (Nhìn Bản đồ SVG `map_fill_2` — Đi ngang qua Cung điện)**:
    * `visual_svg`: Render **`map_fill_2`** *(Vạch lộ trình xe buýt chạy ngang qua `🏰 Schloss` rồi dừng trước `🏛️ Museum`)*.
    * `question`: *„Fährt dieser Bus zum Kunstmuseum? — Ja, er fährt direkt ___ alten Schloss vorbei und hält dann vor dem Museum.“*
    * `accepted_answers`: `["am", "an dem"]`
    * `translation_vi`: *"Chuyến xe buýt này có chạy tới bảo tàng nghệ thuật không? — Có, nó chạy ngang qua ngay cung điện cổ rồi dừng trước bảo tàng."*
    * `explanation`: *"Danh từ `Schloss` mang giống trung (`das Schloss`). Đi với cấu trúc `an + Dativ + vorbei`, `an + dem` gộp thành **`am`** (`am alten Schloss vorbei`)."*

21. **Câu 21 (Nhìn Sơ đồ SVG `quiz_icon_bridge` — Đi qua cây cầu)**:
    * `visual_svg`: Render **`quiz_icon_bridge`** *(Hình vẽ cây cầu bắc qua sông và mũi tên đi vượt qua mặt cầu, không có chữ trên hình)*.
    * `question`: *„Um zur Museumsinsel zu kommen, müsst ihr zuerst ___ die große Brücke laufen.“*
    * `accepted_answers`: `["über", "ueber"]`
    * `translation_vi`: *"Để đi đến được Đảo Bảo tàng, đầu tiên các bạn phải đi bộ qua cây cầu lớn."*
    * `explanation`: *"Đi vượt qua / băng qua mặt cầu (`die Brücke`) dùng giới từ **`über`** (+ `Akkusativ`)."*

22. **Câu 22 (Nhìn Sơ đồ SVG `quiz_icon_gate` — Đi xuyên qua cổng thành)**:
    * `visual_svg`: Render **`quiz_icon_gate`** *(Hình vẽ cổng thành cổ hình vòm và mũi tên đi xuyên qua chính giữa cổng, không có chữ trên hình)*.
    * `question`: *„Wenn du in die Altstadt willst, musst du zu Fuß ___ das historische Stadttor gehen.“*
    * `accepted_answers`: `["durch", "durchs"]`
    * `translation_vi`: *"Nếu bạn muốn vào khu phố cổ, bạn phải đi bộ xuyên qua cổng thành lịch sử."*
    * `explanation`: *"Đi xuyên qua lòng cổng thành (`das Stadttor`) dùng giới từ **`durch`** (+ `Akkusativ`)."*

23. **Câu 23 (Nhìn Sơ đồ SVG `quiz_icon_along` — Đi dọc theo con phố)**:
    * `visual_svg`: Render **`quiz_icon_along`** *(Hình vẽ con đường dài với hàng cây và mũi tên đi dọc suốt chiều dài con đường, không có chữ trên hình)*.
    * `question`: *„Gehen Sie einfach diese breite Straße ___! Nach etwa dreihundert Metern sehen Sie links den Zoo.“*
    * `accepted_answers`: `["entlang"]`
    * `translation_vi`: *"Ngài cứ đi dọc theo con đường rộng này! Sau khoảng ba trăm mét Ngài sẽ nhìn thấy sở thú ở bên trái."*
    * `explanation`: *"Từ chỉ hướng đi dọc theo đứng **sau** danh từ ở `Akkusativ` (`diese breite Straße`) là **`entlang`**."*

24. **Câu 24 (Đi cho đến ngã tư thứ ba — Giới từ kép `bis zu + Dativ`)**:
    * `question`: *„Fahren Sie mit dem Fahrrad immer geradeaus bis ___ dritten Kreuzung und biegen Sie dort rechts ab!“*
    * `accepted_answers`: `["zur", "zu der"]`
    * `translation_vi`: *"Ngài cứ đạp xe thẳng mãi cho đến ngã tư thứ ba và rẽ phải ở đó!"*
    * `explanation`: *"Danh từ `Kreuzung` mang giống cái (`die Kreuzung`). Sau giới từ `bis zu + Dativ`, `zu + der` viết tắt thành **`zur`** (`bis zur dritten Kreuzung`)."*

25. **Câu 25 (Đi cho đến cảng biển — Giới từ kép `bis zu + Dativ` với danh từ giống đực)**:
    * `question`: *„Wie weit fährt die Straßenbahn Linie 4? — Sie fährt vom Rathaus durch das Zentrum bis ___ Hafen.“*
    * `accepted_answers`: `["zum", "zu dem"]`
    * `translation_vi`: *"Tuyến tàu điện mặt đất số 4 chạy bao xa? — Nó chạy từ tòa thị chính xuyên qua trung tâm cho đến cảng biển."*
    * `explanation`: *"Danh từ `Hafen` (cảng biển) mang giống đực (`der Hafen`). Sau `bis zu + Dativ`, `zu + dem` viết tắt thành **`zum`** (`bis zum Hafen`)."*

26. **Câu 26 (Phân biệt `in + Akkusativ` khi bước vào bên trong Trung tâm thương mại)**:
    * `question`: *„Es regnet stark! Komm, wir gehen schnell ___ Einkaufszentrum dort drüben und trinken einen heißen Kakao!“*
    * `accepted_answers`: `["ins", "in das"]`
    * `translation_vi`: *"Trời mưa to quá! Nào, chúng mình đi nhanh vào trong trung tâm thương mại ở đằng kia và uống một cốc ca cao nóng đi!"*
    * `explanation`: *"Danh từ `Einkaufszentrum` mang giống trung (`das Einkaufszentrum`). Đi bước vào bên trong (`Wohin?` + `Akkusativ`) dùng `in + das` = **`ins`**."*

27. **Câu 27 (Phân biệt `in + Akkusativ` khi đi vào bên trong Nhà thờ hoặc Khu triển lãm)**:
    * `question`: *„Meine Tante interessiert sich sehr für Kunst, deshalb geht sie heute Nachmittag ___ Alte Nationalgalerie.“*
    * `accepted_answers`: `["in die"]`
    * `translation_vi`: *"Cô của tôi rất quan tâm đến nghệ thuật, vì vậy chiều nay cô ấy đi vào Khu triển lãm Quốc gia Cũ."*
    * `explanation`: *"`Alte Nationalgalerie` mang giống cái (`die`). Đi vào bên trong (`Wohin?` + `Akkusativ`) dùng **`in die`**."*

28. **Câu 28 (Đi vào bên trong Công viên / Sở thú — Danh từ giống đực ở `Akkusativ`)**:
    * `question`: *„Das Wetter ist heute wunderbar. Gehen wir am Nachmittag mit den Kindern ___ großen Stadtpark oder lieber in den Zoo?“*
    * `accepted_answers`: `["in den"]`
    * `translation_vi`: *"Thời tiết hôm nay tuyệt đẹp. Chiều nay chúng ta đi cùng bọn trẻ vào công viên lớn của thành phố hay đi vào sở thú hơn?"*
    * `explanation`: *"Danh từ `Stadtpark` (`der Park`) mang giống đực. Khi chỉ hướng đi vào (`Wohin?` + `Akkusativ`), `der` đổi thành `den` $\rightarrow$ **`in den`**."*

29. **Câu 29 (Chia động từ khuyết thiếu `wollen` ở ngôi thứ 3 số ít trong ngữ cảnh du lịch)**:
    * `question`: *„Mein Onkel fotografiert sehr gern. In Berlin ___ er unbedingt auf den Fernsehturm fahren und die Stadt von oben fotografieren.“*
    * `accepted_answers`: `["will"]`
    * `translation_vi`: *"Chú của tôi rất thích chụp ảnh. Ở Berlin chú ấy nhất định muốn đi lên Tháp truyền hình và chụp ảnh thành phố từ trên cao."*
    * `explanation`: *"Chủ ngữ `er` (`mein Onkel`) là ngôi thứ 3 số ít; động từ khuyết thiếu `wollen` biến âm `o -> i` và không có đuôi thành **`will`**."*

30. **Câu 30 (Chia động từ khuyết thiếu `wollen` ở ngôi `ihr`)**:
    * `question`: *„Hallo Leon, hallo Mia! Ihr seid schon am Alexanderplatz. Was ___ ihr denn danach noch in der Innenstadt unternehmen?“*
    * `accepted_answers`: `["wollt"]`
    * `translation_vi`: *"Chào Leon, chào Mia! Hai bạn đã ở Quảng trường Alexander rồi. Thế sau đó hai bạn còn muốn làm gì ở khu trung tâm thành phố nữa?"*
    * `explanation`: *"Với chủ ngữ ngôi thứ 2 số nhiều `ihr` (các bạn), động từ `wollen` chia thành **`wollt`**."*

31. **Câu 31 (Chia động từ `sehen` biến âm `e -> ie` ở ngôi `du` khi chỉ đường cho bạn)**:
    * `question`: *„Geh einfach über die kleine Brücke und dann 100 Meter geradeaus! Direkt auf der linken Seite ___ du schon die gelbe Post.“*
    * `accepted_answers`: `["siehst"]`
    * `translation_vi`: *"Cậu cứ đi qua cây cầu nhỏ rồi đi thẳng 100 mét! Ngay ở phía bên tay trái cậu sẽ nhìn thấy bưu điện màu vàng."*
    * `explanation`: *"Động từ `sehen` (nhìn thấy) là động từ mạnh biến âm `e -> ie` ở ngôi `du` (`du siehst`) và `er/sie/es` (`er sieht`). Vì chỉ đường cho bạn ở ngôi `du`, đáp án đúng là **`siehst`**."*

32. **Câu 32 (Chia động từ `fahren` biến âm `a -> ä` trong cấu trúc động từ tách `vorbeifahren`)**:
    * `question`: *„Nimm am besten die Buslinie 100! Dieser Bus ___ am Reichstag, am Brandenburger Tor und am Schloss Bellevue vorbei.“*
    * `accepted_answers`: `["fährt", "faehrt"]`
    * `translation_vi`: *"Tốt nhất bạn hãy đi tuyến xe buýt số 100! Chuyến xe buýt này chạy ngang qua Tòa nhà Quốc hội, Cổng Brandenburg và Cung điện Bellevue."*
    * `explanation`: *"Chủ ngữ `Dieser Bus` là ngôi thứ 3 số ít (`er`). Động từ tách `vorbeifahren` tách tiền tố `vorbei` xuống cuối câu, phần gốc `fahren` biến âm `a -> ä` thành **`fährt`**."*

33. **Câu 33 (Điền động từ nguyên mẫu chỉ việc đi dạo phố mua sắm ở cuối câu với `Modalverb`)**:
    * `question`: *„Das Wetter in Berlin ist sonnig. Nach dem Mittagessen wollen meine Schwester und ich zwei Stunden auf dem Kurfürstendamm ___.“* *(Điền động từ có nghĩa đi dạo phố/tản bộ ngắm cửa hàng bắt đầu bằng chữ `b...`)*
    * `accepted_answers`: `["bummeln"]`
    * `translation_vi`: *"Thời tiết ở Berlin nắng đẹp. Sau bữa trưa, chị gái tôi và tôi muốn đi dạo phố hai tiếng đồng hồ trên đại lộ Kurfürstendamm."*
    * `explanation`: *"Sau động từ khuyết thiếu `wollen`, động từ chính đứng ở cuối câu ở dạng nguyên mẫu: **`bummeln`** (đi dạo phố, tản bộ ngắm cảnh/mua sắm)."*

---

### NHÓM 3: DỊCH TỪ / CỤM TỪ CHỈ ĐƯỜNG & ĐỊA ĐIỂM VIỆT $\rightarrow$ ĐỨC (`dich_nghia_vd` — 12 Câu: Câu 34 $\rightarrow$ Câu 45)
*(Yêu cầu người học tự nhớ đúng mạo từ `der/die/das` và giới từ `Akkusativ/Dativ` mà không có gợi ý).*

34. **Câu 34**: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): ***"nhà ga trung tâm"***
    * `accepted_answers`: `["der Hauptbahnhof", "der Bahnhof"]`
    * `explanation`: *"Nhà ga trung tâm là danh từ giống đực **`der Hauptbahnhof`** (vì `der Bahnhof`)."*
35. **Câu 35**: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): ***"sân bay"***
    * `accepted_answers`: `["der Flughafen"]`
    * `explanation`: *"Sân bay là danh từ ghép giống đực **`der Flughafen`** (số nhiều: `die Flughäfen`)."*
36. **Câu 36**: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): ***"ngã tư / giao lộ"***
    * `accepted_answers`: `["die Kreuzung"]`
    * `explanation`: *"Ngã tư / giao lộ là danh từ giống cái **`die Kreuzung`** (đuôi `-ung` luôn mang mạo từ `die`)."*
37. **Câu 37**: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): ***"đèn giao thông"***
    * `accepted_answers`: `["die Ampel"]`
    * `explanation`: *"Đèn giao thông là danh từ giống cái **`die Ampel`** (số nhiều: `die Ampeln`)."*
38. **Câu 38**: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định): ***"Nhà thờ lớn Berlin"***
    * `accepted_answers`: `["der Berliner Dom"]`
    * `explanation`: *"Nhà thờ lớn Berlin là danh từ giống đực **`der Berliner Dom`**."*
39. **Câu 39**: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định): ***"Cổng thành Brandenburg"***
    * `accepted_answers`: `["das Brandenburger Tor"]`
    * `explanation`: *"Cổng Brandenburg mang giống trung **`das Brandenburger Tor`** (vì `das Tor`)."*
40. **Câu 40**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi ngang qua bệnh viện"***
    * `accepted_answers`: `["am Krankenhaus vorbei", "am Krankenhaus vorbeigehen", "an dem Krankenhaus vorbei", "Gehen Sie am Krankenhaus vorbei"]`
    * `explanation`: *"Bệnh viện là `das Krankenhaus` (giống trung). Khi đi với cấu trúc `an + Dativ + vorbei`, `an + dem` gộp thành **`am Krankenhaus vorbei`**."*
41. **Câu 41**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi ngang qua trường đại học"***
    * `accepted_answers`: `["an der Universität vorbei", "an der Universitaet vorbei", "an der Universität vorbeigehen", "Gehen Sie an der Universität vorbei"]`
    * `explanation`: *"Trường đại học là `die Universität` (giống cái). Đi với `an + Dativ + vorbei` đổi `die` thành `der`: **`an der Universität vorbei`**."*
42. **Câu 42**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi xuyên qua công viên"***
    * `accepted_answers`: `["durch den Park", "durch den Park gehen", "durch den Park laufen", "Gehen Sie durch den Park"]`
    * `explanation`: *"Công viên là `der Park` (giống đực). Đi xuyên qua dùng `durch + Akkusativ` $\rightarrow$ **`durch den Park`**."*
43. **Câu 43**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi băng qua ngã tư"***
    * `accepted_answers`: `["über die Kreuzung", "ueber die Kreuzung", "über die Kreuzung gehen", "Gehen Sie über die Kreuzung"]`
    * `explanation`: *"Ngã tư là `die Kreuzung` (giống cái). Đi băng qua dùng `über + Akkusativ` $\rightarrow$ **`über die Kreuzung`**."*
44. **Câu 44**: Dịch cụm chỉ đường sau sang tiếng Đức (dùng ngôi trang trọng `Sie`): ***"Ngài hãy rẽ trái ở con đường thứ ba!"***
    * `accepted_answers`: `["Gehen Sie die dritte Straße links!", "Gehen Sie die dritte Straße links", "Fahren Sie die dritte Straße links!", "Biegen Sie die dritte Straße links ab!"]`
    * `explanation`: *"Con đường thứ ba bên trái là **`die dritte Straße links`**."*
45. **Câu 45**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi cho đến nhà ga"***
    * `accepted_answers`: `["bis zum Bahnhof", "bis zum Bahnhof gehen", "Gehen Sie bis zum Bahnhof"]`
    * `explanation`: *"Nhà ga là `der Bahnhof` (giống đực). Đi cho đến nhà ga dùng `bis zu + Dativ` $\rightarrow$ **`bis zum Bahnhof`**."*

---

### NHÓM 4: DỊCH TỪ / CỤM TỪ CHỈ ĐƯỜNG & ĐỊA ĐIỂM ĐỨC $\rightarrow$ VIỆT (`dich_nghia_dv` — 12 Câu: Câu 46 $\rightarrow$ Câu 57)

46. **Câu 46**: Dịch sang tiếng Việt: ***„die Bahnhöfe und die Flughäfen“***
    * `accepted_answers`: `["các nhà ga và các sân bay", "những nhà ga và những sân bay", "nhà ga và sân bay"]`
    * `explanation`: *"Dạng số nhiều của `der Bahnhof` (`die Bahnhöfe`) và `der Flughafen` (`die Flughäfen`)."*
47. **Câu 47**: Dịch sang tiếng Việt: ***„die alten Schlösser und die modernen Einkaufszentren“***
    * `accepted_answers`: `["những lâu đài cổ và những trung tâm thương mại hiện đại", "các cung điện cổ và các trung tâm thương mại hiện đại", "các lâu đài cũ và các trung tâm mua sắm hiện đại"]`
    * `explanation`: *"`die Schlösser` = những lâu đài/cung điện; `die Einkaufszentren` = những trung tâm thương mại."*
48. **Câu 48**: Dịch sang tiếng Việt: ***„am Supermarkt und an der Post vorbeigehen“***
    * `accepted_answers`: `["đi ngang qua siêu thị và bưu điện", "đi bộ ngang qua siêu thị và bưu điện"]`
    * `explanation`: *"Cấu trúc `an + Dativ + vorbeigehen` với `der Supermarkt` (`am`) và `die Post` (`an der`)."*
49. **Câu 49**: Dịch sang tiếng Việt: ***„durch das mittelalterliche Stadttor laufen“***
    * `accepted_answers`: `["đi bộ xuyên qua cổng thành thời trung cổ", "chạy xuyên qua cổng thành trung cổ", "đi xuyên qua cổng thành cổ"]`
    * `explanation`: *"`durch das Stadttor` = xuyên qua cổng thành."*
50. **Câu 50**: Dịch sang tiếng Việt: ***„den malerischen Fluss entlangspazieren“***
    * `accepted_answers`: `["đi dạo dọc theo dòng sông thơ mộng", "tản bộ dọc theo con sông đẹp như tranh", "đi dạo dọc bờ sông"]`
    * `explanation`: *"`den Fluss entlangspazieren` = đi dạo dọc theo con sông."*
51. **Câu 51**: Dịch sang tiếng Việt: ***„bis zur dritten Ampel geradeaus fahren“***
    * `accepted_answers`: `["lái xe đi thẳng cho đến đèn giao thông thứ ba", "chạy thẳng tới cột đèn giao thông thứ ba", "đi xe thẳng đến đèn giao thông thứ 3"]`
    * `explanation`: *"`bis zur dritten Ampel` = cho đến đèn giao thông thứ ba."*
52. **Câu 52**: Dịch sang tiếng Việt: ***„über die breite Brücke in die Neustadt gehen“***
    * `accepted_answers`: `["đi qua cây cầu rộng để vào khu phố mới", "đi bộ qua cây cầu rộng vào khu đô thị mới"]`
    * `explanation`: *"`über die breite Brücke` = qua cây cầu rộng; `in die Neustadt` = vào khu phố mới."*
53. **Câu 53**: Dịch sang tiếng Việt: ***„eine zweistündige Stadtrundfahrt mit dem Doppeldeckerbus machen“***
    * `accepted_answers`: `["thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng", "đi tham quan thành phố 2 tiếng bằng xe buýt 2 tầng"]`
    * `explanation`: *"`eine Stadtrundfahrt machen` = thực hiện chuyến tham quan vòng quanh thành phố; `der Doppeldeckerbus` = xe buýt 2 tầng."*
54. **Câu 54**: Dịch sang tiếng Việt: ***„an der nächsten Kreuzung links abbiegen“***
    * `accepted_answers`: `["rẽ trái ở ngã tư tiếp theo", "quẹo trái tại giao lộ kế tiếp"]`
    * `explanation`: *"`an der nächsten Kreuzung` = tại ngã tư tiếp theo; `links abbiegen` = rẽ trái."*
55. **Câu 55**: Dịch sang tiếng Việt: ***„den Fernsehturm am Alexanderplatz besichtigen wollen“***
    * `accepted_answers`: `["muốn tham quan Tháp truyền hình ở quảng trường Alexander", "muốn đi xem Tháp truyền hình tại quảng trường Alexander"]`
    * `explanation`: *"`besichtigen` = tham quan; `wollen` = muốn."*
56. **Câu 56**: Dịch sang tiếng Việt: ***„Entschuldigen Sie bitte, wo geht es hier zum Reichstag?“***
    * `accepted_answers`: `["Xin lỗi Ngài, ở đây đi lối nào để tới Tòa nhà Quốc hội vậy?", "Cho tôi xin lỗi, đường nào đi đến Tòa nhà Quốc hội thế ạ?", "Xin lỗi, đi đến Tòa nhà Quốc hội theo hướng nào?"]`
    * `explanation`: *"Câu hỏi đường lịch sự với `Wo geht es hier zum ...?`."*
57. **Câu 57**: Dịch sang tiếng Việt: ***„Gegenüber vom Bahnhof sehen Sie das große Hotel.“***
    * `accepted_answers`: `["Đối diện với nhà ga Ngài sẽ nhìn thấy khách sạn lớn.", "Ở phía đối diện nhà ga bạn sẽ thấy khách sạn lớn."] `
    * `explanation`: *"`gegenüber von + Dativ` = đối diện với..."*

---

### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI — TƯ DUY NGỮ PHÁP & ĐỊNH HƯỚNG (`noi_o` — 10 Bài: Câu 58 $\rightarrow$ Câu 67)
*(Tuyệt đối không lộ đáp án ở vế trái, bắt buộc người học phải suy luận giống của danh từ và cách của giới từ để nối đúng).*

58. **Câu 58 (Bài nối ô 1 — Nối Tình huống của Khách du lịch với Câu Hỏi Đường phù hợp)**:
    * `1. Du suchst ein Medikament und fragst nach dem Ort (Wo? + Nominativ)` $\longleftrightarrow$ `Entschuldigung, wo ist hier eine Apotheke?`
    * `2. Du stehst auf der Straße und suchst direkt den Ort (suchen + Akkusativ)` $\longleftrightarrow$ `Entschuldigung, ich suche den Hauptbahnhof.`
    * `3. Du möchtest den Weg zu einer Sehenswürdigkeit wissen (zu + Dativ)` $\longleftrightarrow$ `Entschuldigung, wie komme ich zum Brandenburger Tor?`
    * `4. Du möchtest in ein Gebäude hineingehen (in + Akkusativ)` $\longleftrightarrow$ `Entschuldigung, wo geht es hier ins Stadtmuseum?`
59. **Câu 59 (Bài nối ô 2 — Nối Động từ Chỉ đường với Cụm Giới từ Không gian đúng ngữ pháp)**:
    * `1. Bitte gehen Sie an ...` $\longleftrightarrow$ `der alten Kirche und am Rathaus vorbei!`
    * `2. Bitte laufen Sie durch ...` $\longleftrightarrow$ `den grünen Stadtpark und das große Stadttor!`
    * `3. Bitte fahren Sie über ...` $\longleftrightarrow$ `die neue Brücke und den Marktplatz!`
    * `4. Bitte spazieren Sie ...` $\longleftrightarrow$ `die Friedrichstraße und den Kanal entlang!`
60. **Câu 60 (Bài nối ô 3 — Nối 4 Địa điểm có Giống khác nhau với Cụm `bis zu + Dativ` chuẩn xác)**:
    * `1. der Flughafen & der Hafen` $\longleftrightarrow$ `Fahren Sie geradeaus bis zum Flughafen / bis zum Hafen!`
    * `2. die Kreuzung & die Ampel` $\longleftrightarrow$ `Gehen Sie geradeaus bis zur Kreuzung / bis zur Ampel!`
    * `3. das Stadttor & das Einkaufszentrum` $\longleftrightarrow$ `Laufen Sie geradeaus bis zum Stadttor / bis zum Einkaufszentrum!`
    * `4. die zweite Straße & die Staatsoper` $\longleftrightarrow$ `Gehen Sie geradeaus bis zur zweiten Straße / bis zur Staatsoper!`
61. **Câu 61 (Bài nối ô 4 — Phân biệt Đích đến `in + Akkusativ` [vào trong] theo 3 Giống & Số nhiều)**:
    * `1. Danh từ giống đực (Berliner Dom, Zoo, Supermarkt)` $\longleftrightarrow$ `Wir gehen am Nachmittag in den Berliner Dom / in den Zoo.`
    * `2. Danh từ giống cái (Disko, Staatsoper, Nationalgalerie)` $\longleftrightarrow$ `Wir gehen heute Abend in die Disko / in die Staatsoper.`
    * `3. Danh từ giống trung (Kino, Einkaufszentrum, Theater)` $\longleftrightarrow$ `Wir gehen am Wochenende ins Kino / ins Einkaufszentrum.`
    * `4. Danh từ ở vị trí tĩnh (Wo? -> in + Dativ)` $\longleftrightarrow$ `Wir hören ein Konzert im Berliner Dom / sehen einen Film im Kino.`
62. **Câu 62 (Bài nối ô 5 — Nối Chỉ dẫn cho 3 Đối tượng khác nhau: Khách lạ `Sie`, Bạn thân `du`, Nhóm bạn `ihr`)**:
    * `1. Chỉ đường cho một vị khách lớn tuổi (Sie)` $\longleftrightarrow$ `Gehen Sie bitte die erste Straße rechts und dann bis zur Ampel!`
    * `2. Chỉ đường cho một người bạn thân (du)` $\longleftrightarrow$ `Geh bitte die erste Straße rechts und lauf dann über den Platz!`
    * `3. Chỉ đường cho hai người bạn cùng lớp (ihr)` $\longleftrightarrow$ `Geht bitte die erste Straße rechts und fahrt dann mit dem Bus!`
    * `4. Đề xuất cả nhóm cùng đi với nhau (wir)` $\longleftrightarrow$ `Gehen wir zuerst durch den Park und danach ins Café!`
63. **Câu 63 (Bài nối ô 6 — Nối Chủ ngữ với Câu có Động từ Khuyết thiếu `wollen, müssen, können, möchten`)**:
    * `1. Meine Cousine Lena (3. Person Singular)` $\longleftrightarrow$ `will nächstes Jahr an der Humboldt-Universität Medizin studieren.`
    * `2. Mein Bruder und ich (1. Person Plural)` $\longleftrightarrow$ `wollen morgen Vormittag eine Schifffahrt auf der Spree machen.`
    * `3. Du (2. Person Singular)` $\longleftrightarrow$ `musst an der dritten Kreuzung links abbiegen und vor der Bank halten.`
    * `4. Ihr (2. Person Plural)` $\longleftrightarrow$ `könnt vom Alexanderplatz zu Fuß bis zur Museumsinsel gehen.`
64. **Câu 64 (Bài nối ô 7 — Nối Danh từ Số Ít với Dạng Số Nhiều đúng trong Thành phố)**:
    * `1. der Bahnhof / der Hafen / der Markt` $\longleftrightarrow$ `die Bahnhöfe / die Häfen / die Märkte`
    * `2. das Schloss / das Krankenhaus / das Rathaus` $\longleftrightarrow$ `die Schlösser / die Krankenhäuser / die Rathäuser`
    * `3. das Einkaufszentrum / das Museum` $\longleftrightarrow$ `die Einkaufszentren / die Museen`
    * `4. die Brücke / die Kreuzung / die Ampel` $\longleftrightarrow$ `die Brücken / die Kreuzungen / die Ampeln`
65. **Câu 65 (Bài nối ô 8 — Nối 4 Danh lam thắng cảnh Berlin với Hoạt động thực tế phù hợp)**:
    * `1. Auf dem Fernsehturm am Alexanderplatz` $\longleftrightarrow$ `kann man ganz Berlin von oben sehen.`
    * `2. Auf der Museumsinsel und in der Alten Nationalgalerie` $\longleftrightarrow$ `wollen die Touristen berühmte Kunstwerke besichtigen.`
    * `3. Auf der langen Friedrichstraße` $\longleftrightarrow$ `möchten viele Besucher am Nachmittag bummeln und einkaufen.`
    * `4. Vor dem Brandenburger Tor und dem Reichstag` $\longleftrightarrow$ `machen die Reisegruppen immer viele Erinnerungsfotos.`
66. **Câu 66 (Bài nối ô 9 — Sắp xếp Trình tự Chỉ đường từ Nhà ga đến Khách sạn cho Du khách)**:
    * `1. Bước mở đầu (Zuerst)` $\longleftrightarrow$ `gehen Sie vom Bahnhofsvorplatz geradeaus die Kaiserstraße entlang.`
    * `2. Bước thứ hai (Dann)` $\longleftrightarrow$ `biegen Sie an der zweiten Kreuzung vor der Bank links ab.`
    * `3. Bước thứ ba (Danach)` $\longleftrightarrow$ `laufen Sie über die kleine Brücke und am Stadtpark vorbei.`
    * `4. Bước cuối cùng (Zum Schluss)` $\longleftrightarrow$ `sehen Sie direkt rechts nach der Ampel Ihr Hotel.`
67. **Câu 67 (Bài nối ô 10 — Phân biệt Cặp Câu Vị Trí Tĩnh `Wo?` vs. Chuyển Động `Wohin?`)**:
    * `1. Wo wartet dein Freund auf dich? (Vị trí tĩnh - Dativ)` $\longleftrightarrow$ `Er steht direkt vor dem Kino / an der zweiten Ampel.`
    * `2. Wohin läufst du so schnell? (Hướng đích - Akkusativ)` $\longleftrightarrow$ `Ich laufe schnell in das Kino / über die Straße.`
    * `3. Wo fährt der Sightseeing-Bus entlang? (Đi ngang qua - Dativ)` $\longleftrightarrow$ `Er fährt am Schloss Bellevue und an der Universität vorbei.`
    * `4. Wohin fährt der Sightseeing-Bus jetzt? (Đi xuyên qua - Akkusativ)` $\longleftrightarrow$ `Er fährt jetzt durch das Stadttor auf den großen Platz.`

---

### NHÓM 6: ĐIỀN VÀO CHỖ TRỐNG ĐỂ TẠO THÀNH CÂU — KHÔNG GỢI Ý GIỐNG / CÁCH (`dien_tao_cau` — 10 Câu: Câu 68 $\rightarrow$ Câu 77)
*(Chỉ hiển thị câu tiếng Đức có 2 chỗ trống `[1]`, `[2]` và bản đồ/ngữ cảnh tiếng Đức. Học viên phải tự suy luận cả giới từ, mạo từ lẫn dạng chia động từ).*

68. **Câu 68 (Nhìn Bản đồ SVG `map_build_1` — Chỉ đường cho bạn thân `du` đi qua công viên và nhà thờ)**:
    * `visual_svg`: Render **`map_build_1`** *(Lộ trình từ `📍 START` đi xuyên qua `🌳 Park` rồi đi ngang qua `⛪ Kirche` tới `🚉 Bahnhof`)*.
    * `question`: Hoàn thành lời chỉ đường cho người bạn thân (`du`) khớp với lộ trình trên bản đồ:
    * `display_sentence`: `Lauf zuerst [1] den Park und geh dann an [2] Kirche vorbei bis zum Bahnhof!`
    * `accepted_answers`: Ô 1 = `["durch"]`, Ô 2 = `["der"]`.
    * `translation_vi`: *"Đầu tiên cậu hãy chạy xuyên qua công viên và sau đó đi ngang qua nhà thờ cho đến nhà ga!"*
    * `explanation`: *"Đi xuyên qua `der Park` dùng **`durch`** (`durch den Park`). Đi ngang qua `die Kirche` dùng `an + Dativ + vorbei` $\rightarrow$ **`an der Kirche vorbei`**."*

69. **Câu 69 (Nhìn Bản đồ SVG `map_build_2` — Chỉ đường cho khách du lịch đi qua cầu và dọc theo phố)**:
    * `visual_svg`: Render **`map_build_2`** *(Lộ trình từ `📍 START` đi qua `🌉 Brücke` rồi đi dọc theo `🛣️ Goethestraße` tới `📮 Post`)*.
    * `question`: Hoàn thành lời chỉ đường lịch sự cho vị khách du lịch khớp với bản đồ:
    * `display_sentence`: `Gehen Sie zuerst [1] die Brücke und dann die Goethestraße [2] bis zur Post!`
    * `accepted_answers`: Ô 1 = `["über", "ueber"]`, Ô 2 = `["entlang"]`.
    * `translation_vi`: *"Đầu tiên Ngài hãy đi qua cây cầu và sau đó đi dọc theo đường Goethe cho đến bưu điện!"*
    * `explanation`: *"Đi vượt qua mặt cầu dùng **`über`** (`über die Brücke`); đi dọc theo con đường đặt **`entlang`** ở sau danh từ (`die Goethestraße entlang`)."*

70. **Câu 70 (Phân biệt `zum` [`zu + Dativ`] và `in den` [`in + Akkusativ`])**:
    * `question`: Hoàn thành câu kể về lịch trình ngày Chủ nhật của gia đình:
    * `display_sentence`: `Am Sonntagvormittag fahren wir zuerst [1] Flughafen, um Oma abzuholen, und am Nachmittag gehen wir zusammen [2] Zoo.`
    * `accepted_answers`: Ô 1 = `["zum"]`, Ô 2 = `["in den", "zum"]`.
    * `translation_vi`: *"Sáng Chủ nhật đầu tiên chúng tôi lái xe ra sân bay để đón bà, và buổi chiều chúng tôi cùng nhau đi vào sở thú."*
    * `explanation`: *"`der Flughafen` sau `zu + Dativ` là **`zum Flughafen`**; đi vào bên trong sở thú (`der Zoo`) dùng **`in den Zoo`**."*

71. **Câu 71 (Phân biệt `am ... vorbei` và `bis zur ...`)**:
    * `question`: Hoàn thành lời hướng dẫn của tài xế xe buýt:
    * `display_sentence`: `Sie müssen hier aussteigen, dann [1] großen Supermarkt vorbeigehen und geradeaus bis [2] zweiten Ampel laufen.`
    * `accepted_answers`: Ô 1 = `["am", "an dem"]`, Ô 2 = `["zur", "zu der"]`.
    * `translation_vi`: *"Ngài phải xuống xe ở đây, sau đó đi ngang qua siêu thị lớn và đi bộ thẳng cho đến đèn giao thông thứ hai."*
    * `explanation`: *"`der Supermarkt` đi với `an + Dativ + vorbei` là **`am großen Supermarkt vorbei`**; `die Ampel` đi với `bis zu + Dativ` là **`bis zur zweiten Ampel`**."*

72. **Câu 72 (Chia động từ khuyết thiếu `wollen` ở ngôi `er` và `wir`)**:
    * `question`: Hoàn thành câu với dạng chia đúng của động từ khuyết thiếu **`wollen`**:
    * `display_sentence`: `Mein Freund Lukas [1] heute unbedingt das Bundeskanzleramt fotografieren, aber wir [2] lieber zuerst auf der Museumsinsel spazieren gehen.`
    * `accepted_answers`: Ô 1 = `["will"]`, Ô 2 = `["wollen"]`.
    * `translation_vi`: *"Người bạn Lukas của tôi hôm nay nhất định muốn chụp ảnh Phủ Thủ tướng, nhưng chúng tôi lại muốn đi dạo trên Đảo Bảo tàng trước hơn."*
    * `explanation`: *"Ngôi thứ 3 số ít (`Lukas` = `er`) chia là **`will`**; ngôi thứ nhất số nhiều (`wir`) chia là **`wollen`**."*

73. **Câu 73 (Chia động từ khuyết thiếu `müssen` và `können` trong câu chỉ đường)**:
    * `question`: Hoàn thành câu hướng dẫn giao thông với dạng chia đúng của **`müssen`** (ô 1) và **`können`** (ô 2):
    * `display_sentence`: `An dieser Kreuzung [1] du leider nicht links abbiegen, aber du [2] an der nächsten Ampel wenden.`
    * `accepted_answers`: Ô 1 = `["darfst", "kannst", "musst"]`, Ô 2 = `["kannst"]`. *(Chỉnh câu rõ nghĩa bắt buộc với `müssen` ở ô 1)*:
    * *Chuẩn hóa `display_sentence`*: `Vor der Baustelle [1] ihr leider rechts abbiegen, aber danach [2] ihr wieder geradeaus bis zum Hafen fahren.` *(Điền dạng chia của `müssen` vào ô 1 và `können` vào ô 2)*.
    * `accepted_answers`: Ô 1 = `["müsst", "muesst"]`, Ô 2 = `["könnt", "koennt"]`.
    * `translation_vi`: *"Trước công trường rất tiếc các bạn phải rẽ phải, nhưng sau đó các bạn có thể lại chạy thẳng cho đến cảng biển."*
    * `explanation`: *"Với chủ ngữ `ihr` (các bạn), `müssen` chia là **`müsst`** và `können` chia là **`könnt`**."*

74. **Câu 74 (Phân biệt `in die` [Akkusativ] và `in der` [Dativ] với danh từ giống cái)**:
    * `question`: Hoàn thành câu với cụm giới từ `in` + mạo từ phù hợp:
    * `display_sentence`: `Wohin gehst du? — Ich gehe jetzt [1] Staatsoper, weil meine Freundin heute Abend [2] Staatsoper Geige spielt.`
    * `accepted_answers`: Ô 1 = `["in die"]`, Ô 2 = `["in der"]`.
    * `translation_vi`: *"Bạn đang đi đâu thế? — Bây giờ tôi đi vào Nhà hát Opera Quốc gia, bởi vì tối nay bạn gái tôi chơi đàn vĩ cầm ở trong Nhà hát Opera Quốc gia."*
    * `explanation`: *"Ô 1 trả lời cho `Wohin?` (di chuyển vào trong) $\rightarrow$ `in + Akkusativ` = **`in die Staatsoper`**. Ô 2 trả lời cho `Wo?` (chơi đàn ở đâu - vị trí tĩnh) $\rightarrow$ `in + Dativ` = **`in der Staatsoper`**."*

75. **Câu 75 (Phân biệt `ins` [Akkusativ] và `im` [Dativ] với danh từ giống trung)**:
    * `question`: Hoàn thành câu với dạng rút gọn đúng của giới từ `in`:
    * `display_sentence`: `Mein kleiner Bruder muss leider [1] Krankenhaus gebracht werden, aber unser Nachbar arbeitet als Arzt [2] Krankenhaus.`
    * `accepted_answers`: Ô 1 = `["ins", "in das"]`, Ô 2 = `["im", "in dem"]`.
    * `translation_vi`: *"Em trai nhỏ của tôi rất tiếc phải được đưa vào bệnh viện, nhưng người hàng xóm của chúng tôi làm bác sĩ ở trong bệnh viện đó."*
    * `explanation`: *"Đưa vào bệnh viện (`Wohin?` + `Akkusativ`) với `das Krankenhaus` dùng **`ins`** (`in das`). Làm việc ở trong bệnh viện (`Wo?` + `Dativ`) dùng **`im`** (`in dem`)."*

76. **Câu 76 (Hỏi đường với `suchen + Akkusativ` và `komme ich + zur/zum`)**:
    * `question`: Hoàn thành đoạn hội thoại hỏi đường ngắn trên phố:
    * `display_sentence`: `Entschuldigung, ich suche [1] alten Marktplatz. Wie komme ich am besten [2] Marktplatz?`
    * `accepted_answers`: Ô 1 = `["den"]`, Ô 2 = `["zum", "zu dem"]`.
    * `translation_vi`: *"Xin lỗi, tôi đang tìm quảng trường chợ cổ. Làm thế nào tôi đi đến được quảng trường chợ một cách tốt nhất?"*
    * `explanation`: *"`der Marktplatz` (giống đực) đứng sau động từ `suchen` (`Akkusativ`) dùng mạo từ **`den`** (`den alten Marktplatz`); đứng sau `Wie komme ich ...?` (`zu + Dativ`) dùng **`zum`** (`zum Marktplatz`)."*

77. **Câu 77 (Số thứ tự trong câu chỉ đường ở `Akkusativ` và `Dativ`)**:
    * `question`: Hoàn thành câu chỉ đường với dạng đúng của số thứ tự `erste` (1.) và `zweite` (2.):
    * `display_sentence`: `Nehmen Sie bitte die [1] Straße rechts und biegen Sie dann an der [2] Kreuzung wieder links ab!`
    * `accepted_answers`: Ô 1 = `["erste"]`, Ô 2 = `["zweiten"]`.
    * `translation_vi`: *"Xin Ngài hãy đi con đường thứ nhất bên phải và sau đó tại ngã tư thứ hai lại rẽ trái!"*
    * `explanation`: *"Sau `die` ở `Akkusativ` giống cái dùng **`erste`** (`die erste Straße`); sau `an der` ở `Dativ` giống cái bắt buộc thêm đuôi `-n` thành **`zweiten`** (`an der zweiten Kreuzung`)."*

---

### NHÓM 7: NGHE GIỌNG ĐỌC `de-DE` VÀ ĐIỀN TỪ — TÌNH HUỐNG MỚI (`nghe_dien` — 9 Câu: Câu 78 $\rightarrow$ Câu 86)
*(Trong lúc làm bài, chỉ phát âm thanh `audio_text` và hiển thị `display_sentence` tiếng Đức, KHÔNG hiện `hint_vi` trước khi nộp bài để rèn kỹ năng nghe thực tế).*

78. **Câu 78**:
    * `audio_text`: *"Entschuldigung, wie komme ich vom Hauptbahnhof am schnellsten zum Flughafen?"*
    * `display_sentence`: *"Entschuldigung, wie komme ich vom Hauptbahnhof am schnellsten zum ___?"*
    * `accepted_answers`: `["Flughafen"]`
    * `translation_vi`: *"Xin lỗi, làm thế nào tôi đi từ nhà ga trung tâm ra sân bay nhanh nhất?"*
    * `explanation`: *"Danh từ ghép `der Flughafen` có nghĩa là sân bay."*
79. **Câu 79**:
    * `audio_text`: *"Gehen Sie zuerst über die lange Brücke und dann dreihundert Meter den Fluss entlang."*
    * `display_sentence`: *"Gehen Sie zuerst über die lange ___ und dann dreihundert Meter den Fluss entlang."*
    * `accepted_answers`: `["Brücke", "Bruecke"]`
    * `translation_vi`: *"Đầu tiên Ngài hãy đi qua cây cầu dài và sau đó đi dọc theo con sông ba trăm mét."*
    * `explanation`: *"Danh từ `die Brücke` có nghĩa là cây cầu."*
80. **Câu 80**:
    * `audio_text`: *"Der Sightseeing-Bus fährt am historischen Rathaus und an der Staatsoper vorbei."*
    * `display_sentence`: *"Der Sightseeing-Bus fährt am historischen Rathaus und an der ___ vorbei."*
    * `accepted_answers`: `["Staatsoper"]`
    * `translation_vi`: *"Chiếc xe buýt tham quan chạy ngang qua tòa thị chính lịch sử và Nhà hát Opera Quốc gia."*
    * `explanation`: *"`die Staatsoper` là Nhà hát Opera Quốc gia."*
81. **Câu 81**:
    * `audio_text`: *"An der dritten Kreuzung vor dem Krankenhaus musst du links abbiegen."*
    * `display_sentence`: *"An der dritten ___ vor dem Krankenhaus musst du links abbiegen."*
    * `accepted_answers`: `["Kreuzung"]`
    * `translation_vi`: *"Tại ngã tư thứ ba trước bệnh viện, bạn phải rẽ trái."*
    * `explanation`: *"`die Kreuzung` là ngã tư / giao lộ."*
82. **Câu 82**:
    * `audio_text`: *"Meine Großeltern wollen morgen Nachmittag das schöne Schloss Bellevue besichtigen."*
    * `display_sentence`: *"Meine Großeltern ___ morgen Nachmittag das schöne Schloss Bellevue besichtigen."*
    * `accepted_answers`: `["wollen"]`
    * `translation_vi`: *"Ông bà của tôi muốn tham quan Cung điện Bellevue tuyệt đẹp vào chiều mai."*
    * `explanation`: *"Động từ khuyết thiếu `wollen` chia với chủ ngữ số nhiều `Meine Großeltern` (`sie`)."*
83. **Câu 83**:
    * `audio_text`: *"Laufen Sie einfach durch das alte Stadttor, dann stehen Sie direkt auf dem Marktplatz."*
    * `display_sentence`: *"Laufen Sie einfach ___ das alte Stadttor, dann stehen Sie direkt auf dem Marktplatz."*
    * `accepted_answers`: `["durch"]`
    * `translation_vi`: *"Ngài cứ đi bộ xuyên qua cổng thành cổ, sau đó Ngài sẽ đứng ngay trên quảng trường chợ."*
    * `explanation`: *"Giới từ `durch` (+ `Akkusativ`) diễn tả sự đi xuyên qua lòng cổng thành."*
84. **Câu 84**:
    * `audio_text`: *"Am Samstag möchten wir im neuen Einkaufszentrum Kleider kaufen und danach ins Kino gehen."*
    * `display_sentence`: *"Am Samstag möchten wir im neuen ___ Kleider kaufen und danach ins Kino gehen."*
    * `accepted_answers`: `["Einkaufszentrum"]`
    * `translation_vi`: *"Vào thứ Bảy chúng tôi muốn mua quần áo ở trong trung tâm thương mại mới và sau đó đi vào rạp chiếu phim."*
    * `explanation`: *"`das Einkaufszentrum` là trung tâm thương mại."*
85. **Câu 85**:
    * `audio_text`: *"Fahren Sie bitte immer geradeaus bis zur zweiten Ampel vor der Universität!"*
    * `display_sentence`: *"Fahren Sie bitte immer ___ bis zur zweiten Ampel vor der Universität!"*
    * `accepted_answers`: `["geradeaus"]`
    * `translation_vi`: *"Xin Ngài cứ lái xe đi thẳng mãi cho đến đèn giao thông thứ hai trước trường đại học!"*
    * `explanation`: *"Trạng từ chỉ hướng `geradeaus` có nghĩa là đi thẳng."*
86. **Câu 86**:
    * `audio_text`: *"Nach der Stadtrundfahrt will mein Cousin noch eine Stunde am Hafen bummeln."*
    * `display_sentence`: *"Nach der ___ will mein Cousin noch eine Stunde am Hafen bummeln."*
    * `accepted_answers`: `["Stadtrundfahrt"]`
    * `translation_vi`: *"Sau chuyến tham quan vòng quanh thành phố, anh họ tôi còn muốn đi dạo một tiếng ở cảng biển."*
    * `explanation`: *"`die Stadtrundfahrt` là chuyến tham quan vòng quanh thành phố."*

---

### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT $\rightarrow$ ĐỨC — TÌNH HUỐNG CHỈ ĐƯỜNG CHO KHÁCH / BẠN BÈ / NGƯỜI THÂN (`dich_cau_vd` — 7 Câu: Câu 87 $\rightarrow$ Câu 93)

87. **Câu 87 (Chỉ đường cho vị khách du lịch nước ngoài bằng ngôi `Sie`)**:
    * `question`: Dịch câu chỉ đường sau sang tiếng Đức (dùng ngôi trang trọng `Sie`): ***"Đầu tiên Ngài hãy đi thẳng qua cây cầu, sau đó đi ngang qua bệnh viện cho đến đèn giao thông thứ hai!"***
    * `accepted_answers`:
      * `"Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!"`
      * `"Zuerst gehen Sie geradeaus über die Brücke, danach gehen Sie am Krankenhaus vorbei bis zur zweiten Ampel."`
      * `"Gehen Sie zuerst über die Brücke geradeaus und dann am Krankenhaus vorbei bis zur zweiten Ampel!"`
    * `explanation`: *"Qua cầu: `über die Brücke` (`Akkusativ`); đi ngang qua bệnh viện (`das Krankenhaus`): `am Krankenhaus vorbei` (`Dativ`); cho đến đèn giao thông thứ hai (`die Ampel`): `bis zur zweiten Ampel` (`Dativ`)."*

88. **Câu 88 (Chỉ đường cho bạn thân bằng ngôi `du`)**:
    * `question`: Dịch câu chỉ đường cho bạn thân sau sang tiếng Đức (dùng ngôi `du`): ***"Cậu hãy đi xuyên qua công viên, đi dọc theo con sông và rẽ trái ở ngã tư thứ nhất!"***
    * `accepted_answers`:
      * `"Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!"`
      * `"Geh durch den Park, geh den Fluss entlang und geh die erste Straße links!"`
      * `"Lauf durch den Park, den Fluss entlang und an der ersten Kreuzung links!"`
    * `explanation`: *"Ngôi `du` mệnh lệnh: `Geh / Lauf`; xuyên qua công viên: `durch den Park`; dọc theo con sông: `den Fluss entlang`; ở ngã tư thứ nhất bên trái: `an der ersten Kreuzung links`."*

89. **Câu 89 (Hỏi đường thực tế của khách du lịch tại Berlin)**:
    * `question`: Dịch câu hỏi đường sau sang tiếng Đức: ***"Xin lỗi, chúng tôi đang tìm Đảo Bảo tàng. Làm thế nào chúng tôi đi bộ đến được Đảo Bảo tàng?"***
    * `accepted_answers`:
      * `"Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?"`
      * `"Entschuldigung, wir suchen die Museumsinsel. Wie gehen wir zur Museumsinsel?"`
      * `"Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir zur Museumsinsel?"`
    * `explanation`: *"`die Museumsinsel` mang giống cái (`die`): sau `suchen` (`Akkusativ`) là `die Museumsinsel`, sau `Wie kommen wir ...?` (`zu + Dativ`) là `zur Museumsinsel`."*

90. **Câu 90 (Chỉ đường cho hai người bạn bằng ngôi `ihr`)**:
    * `question`: Dịch câu sau sang tiếng Đức (dùng ngôi `ihr`): ***"Các bạn hãy đi ngang qua nhà thờ cổ và băng qua quảng trường chợ, ở bên phải các bạn sẽ nhìn thấy tòa thị chính."***
    * `accepted_answers`:
      * `"Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus."`
      * `"Geht an der alten Kirche vorbei und lauft über den Marktplatz! Rechts seht ihr das Rathaus."`
      * `"Lauft an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus."`
    * `explanation`: *"Mệnh lệnh ngôi `ihr`: `Geht / Lauft`; ngang qua nhà thờ cổ: `an der alten Kirche vorbei`; băng qua quảng trường chợ: `über den Marktplatz`; các bạn nhìn thấy: `seht ihr`."*

91. **Câu 91 (Kể kế hoạch tham quan với động từ khuyết thiếu `wollen` và `möchten`)**:
    * `question`: Dịch câu sau sang tiếng Đức: ***"Buổi sáng chú của tôi muốn tham quan Tòa nhà Quốc hội, và buổi chiều chúng tôi muốn đi dạo phố ở trung tâm thương mại."***
    * `accepted_answers`:
      * `"Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln."`
      * `"Am Morgen will mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln."`
      * `"Vormittags möchte mein Onkel den Reichstag besichtigen, und nachmittags wollen wir im Einkaufszentrum bummeln."`
    * `explanation`: *"`mein Onkel` (`er`) $\rightarrow$ `will ... besichtigen`; `der Reichstag` ở `Akkusativ` là `den Reichstag`; ở trong trung tâm thương mại (`Wo?` + `Dativ`) là `im Einkaufszentrum`."*

92. **Câu 92 (Phân biệt `zum` và `in das / ins` trong cùng một câu)**:
    * `question`: Dịch câu sau sang tiếng Đức: ***"Đầu tiên các du khách đi xe buýt đến Cổng Brandenburg, và buổi tối họ đi vào trong Nhà hát Opera Quốc gia."***
    * `accepted_answers`:
      * `"Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper."`
      * `"Die Touristen fahren zuerst mit dem Bus zum Brandenburger Tor, und abends gehen sie in die Staatsoper."`
    * `explanation`: *"Đi bằng xe buýt: `mit dem Bus`; đến Cổng Brandenburg: `zum Brandenburger Tor` (`zu + dem`); đi vào trong Nhà hát Opera Quốc gia: `in die Staatsoper` (`in + Akkusativ`)."*

93. **Câu 93 (Kết hợp `durch`, `vorbei` và động từ khuyết thiếu `müssen`)**:
    * `question`: Dịch câu sau sang tiếng Đức: ***"Để đến được cảng biển, bạn phải đi xuyên qua cổng thành và đi ngang qua ngân hàng lớn."***
    * `accepted_answers`:
      * `"Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen."`
      * `"Du musst durch das Stadttor gehen und an der großen Bank vorbeigehen, um zum Hafen zu kommen."`
      * `"Wenn du zum Hafen willst, musst du durch das Stadttor und an der großen Bank vorbeigehen."`
    * `explanation`: *"Đến cảng biển: `zum Hafen`; xuyên qua cổng thành: `durch das Stadttor`; ngang qua ngân hàng lớn: `an der großen Bank vorbei`."*

---

### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC $\rightarrow$ VIỆT — LỘ TRÌNH THỰC TẾ (`dich_cau_dv` — 7 Câu: Câu 94 $\rightarrow$ Câu 100)

94. **Câu 94**: Dịch câu chỉ đường sau sang tiếng Việt: ***„Gehen Sie vom Bahnhof aus zuerst dreihundert Meter geradeaus, dann an der Hauptpost vorbei und an der zweiten Ampel rechts!“***
    * `accepted_answers`:
      * `"Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!"`
      * `"Từ phía nhà ga trước tiên bạn đi thẳng 300 mét, rồi đi qua bưu điện chính và tại đèn giao thông thứ hai thì rẽ phải!"`
    * `explanation`: *"`vom Bahnhof aus` = từ nhà ga; `an der Hauptpost vorbei` = ngang qua bưu điện chính; `an der zweiten Ampel rechts` = rẽ phải ở đèn giao thông thứ hai."*
95. **Câu 95**: Dịch câu sau sang tiếng Việt: ***„Wenn ihr zum alten Schloss wollt, müsst ihr zuerst durch den Stadtpark laufen und danach die steinerne Brücke überqueren.“***
    * `accepted_answers`:
      * `"Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá."`
      * `"Nếu các cậu muốn tới cung điện cổ thì trước tiên phải chạy xuyên qua công viên thành phố rồi đi qua cây cầu bằng đá."`
    * `explanation`: *"`durch den Stadtpark laufen` = đi bộ/chạy xuyên qua công viên thành phố; `die steinerne Brücke überqueren` = băng qua cây cầu đá."*
96. **Câu 96**: Dịch câu sau sang tiếng Việt: ***„Der Bus Linie 200 fährt am Alexanderplatz, am Berliner Dom und an der Humboldt-Universität vorbei bis zum Zoologischen Garten.“***
    * `accepted_answers`:
      * `"Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú."`
      * `"Xe buýt tuyến 200 đi ngang qua quảng trường Alexander, Nhà thờ lớn Berlin và trường Đại học Humboldt tới tận Sở thú."`
    * `explanation`: *"Cấu trúc `an + Dativ + vorbeifahren` với cả danh từ giống đực (`am`) và giống cái (`an der`)."*
97. **Câu 97**: Dịch câu sau sang tiếng Việt: ***„Entschuldigen Sie bitte, können Sie mir auf dem Stadtplan zeigen, wie ich zu Fuß zum Bundeskanzleramt komme?“***
    * `accepted_answers`:
      * `"Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?"`
      * `"Cho tôi xin lỗi, bạn có thể chỉ giúp tôi trên bản đồ thành phố đường đi bộ tới Phủ Thủ tướng được không?"`
    * `explanation`: *"`auf dem Stadtplan zeigen` = chỉ trên bản đồ thành phố; `zu Fuß zum Bundeskanzleramt kommen` = đi bộ đến Phủ Thủ tướng."*
98. **Câu 98**: Dịch câu sau sang tiếng Việt: ***„Spaziert einfach zwanzig Minuten das Flussufer entlang, dann seht ihr auf der linken Seite die berühmte Museumsinsel!“***
    * `accepted_answers`:
      * `"Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!"`
      * `"Các cậu hãy tản bộ dọc bờ sông 20 phút rồi sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái!"`
    * `explanation`: *"`das Flussufer entlang` = dọc theo bờ sông; `auf der linken Seite` = ở phía bên tay trái."*
99. **Câu 99**: Dịch câu sau sang tiếng Việt: ***„Am Vormittag wollen die Studenten in die Alte Nationalgalerie gehen, aber am Abend möchten sie lieber einen Film im Kino sehen.“***
    * `accepted_answers`:
      * `"Vào buổi sáng các sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn."`
      * `"Buổi sáng những người sinh viên muốn vào Khu triển lãm Quốc gia Cũ, nhưng buổi tối họ muốn xem phim trong rạp hơn."`
    * `explanation`: *"Đối chiếu `in die Alte Nationalgalerie gehen` (`Wohin?` + `Akkusativ`) và `im Kino sehen` (`Wo?` + `Dativ`)."*
100. **Câu 100**: Dịch câu sau sang tiếng Việt: ***„Biegen Sie bitte vor dem großen Einkaufszentrum links ab, fahren Sie durch den kurzen Tunnel und halten Sie direkt neben der Bank!“***
     * `accepted_answers`:
       * `"Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!"`
       * `"Hãy quẹo trái ở phía trước trung tâm mua sắm lớn, chạy xuyên qua hầm ngắn và đỗ ngay cạnh ngân hàng!"`
     * `explanation`: *"`vor dem großen Einkaufszentrum` = trước trung tâm thương mại lớn; `durch den kurzen Tunnel` = xuyên qua đường hầm ngắn; `neben der Bank` = bên cạnh ngân hàng."*

---

## PHẦN 3: NÂNG CẤP BỘ SINH ĐỀ ĐỘNG (`DYNAMIC ROLEPLAY MAP & GRAMMAR GENERATOR`) CHO BÀI 8

Khi học viên bấm nút **`🔄 Đổi đề khác`** trong Bài 8, hệ thống tuyệt đối không được chỉ xáo trộn thứ tự các câu tĩnh, mà phải kích hoạt **Bộ Sinh Tình Huống Chỉ Đường Thực Chiến (`Real-life Navigation Roleplay Engine`)** tuân thủ nghiêm ngặt quy tắc **Không Lộ Gợi Ý**:

1. **Sinh ngẫu nhiên Người Hỏi & Ngôi Giao Tiếp**:
   * **Ngôi `Sie` (Khách du lịch / Người lạ trên phố)**: *„Ein Tourist aus Japan / Eine Dame / Ein Autofahrer fragt Sie nach dem Weg...“* $\rightarrow$ Động từ chia ở `Gehen Sie / Fahren Sie / Nehmen Sie / Biegen Sie ... ab / Rechts sehen Sie...`
   * **Ngôi `du` (Bạn thân / Anh chị em)**: *„Dein Freund Max / Deine Schwester Lisa / Dein Cousin fragt dich...“* $\rightarrow$ Động từ chia ở `Geh / Fahr / Nimm / Bieg ... ab / Rechts siehst du...`
   * **Ngôi `ihr` (Nhóm bạn / Người thân)**: *„Deine Freunde / Eure Eltern fragen euch...“* $\rightarrow$ Động từ chia ở `Geht / Fahrt / Nehmt / Biegt ... ab / Rechts seht ihr...`
2. **Sinh ngẫu nhiên Bản đồ Lưới Đường Phố SVG Không Mạo Từ (`Unspoiled SVG Map`)**:
   * Vẽ ngẫu nhiên vị trí của 6–8 tòa nhà trên lưới đường phố (chỉ hiển thị icon + danh từ gốc không mạo từ như `🏦 Bank`, `⛪ Kirche`, `🏥 Krankenhaus`, `🏰 Schloss`, `🚉 Bahnhof`, `🛍️ Einkaufszentrum`, `📮 Post`, `🎬 Kino`, `⛩️ Stadttor`).
   * Tự động tính toán lộ trình từ `📍 START` tới `🏁 ZIEL` và kiểm tra kiến thức tổng hợp của người học:
     * Tự nhớ giống của tòa nhà đi ngang qua để chia `am [Mask/Neut] vorbei` hay `an der [Fem] vorbei`.
     * Tự nhớ giống của chướng ngại vật để chia `durch den Park / durch das Stadttor` hay `über die Brücke / über den Platz / über die Kreuzung`.
     * Tự nhớ số thứ tự ở `Akkusativ` (`die erste/zweite/dritte Straße`) hay ở `Dativ` (`an der ersten/zweiten/dritten Kreuzung`, `bis zur ersten/zweiten/dritten Ampel`).
     * Tự phân biệt đích đến `zum/zur` (`zu + Dativ`) và `in den/in die/ins` (`in + Akkusativ`).

---

## PHẦN 4: KỊCH BẢN KIỂM THỬ TỰ ĐỘNG BẮT BUỘC (`verify_lesson8_no_spoilers_qa.py`)

Sau khi cập nhật `lessons/a1/seed_a1_b8.py` và `static/js/city_map_svg.js`, Antigravity IDE **BẮT BUỘC** phải chạy script kiểm thử tự động để xác nhận 6 tiêu chí sau đạt **100% PASS**:

1. **Kiểm tra Không Lộ Gợi Ý Giống & Cách Trong Đề Bài (`Zero-Hint Regex Check`)**:
   * Quét toàn bộ 100 câu hỏi của Bài 8: Đảm bảo trong trường `question` và `display_sentence` **KHÔNG TỒN TẠI** bất kỳ chuỗi gợi ý nào như `(der `, `(die `, `(das `, `(Akkusativ)`, `(Dativ)`, `(zu +`, `(an +`, `(in +`, `(Gợi ý:`.
2. **Kiểm tra Không Rò Rỉ Tiếng Việt Trong Đề Bài Ngữ Pháp Tiếng Đức (`Zero-Vietnamese-Leak Check`)**:
   * Đảm bảo trong các dạng `trac_nghiem`, `dien_khuyet`, `dien_tao_cau`, `nghe_dien`, câu tiếng Đức cần điền từ không kèm theo bản dịch tiếng Việt nằm lộ thiên trong trường `question` (bản dịch tiếng Việt chỉ nằm trong trường `translation_vi` / `explanation` để hiển thị sau khi người học đã trả lời).
3. **Kiểm tra Bản Đồ & Sơ Đồ SVG Không Lộ Đáp Án (`Clean SVG Map Check`)**:
   * Đảm bảo trên các hình vẽ SVG của chế độ bài tập (`quiz_blind`) không chứa các từ khóa đáp án (`vorbei`, `durch`, `über`, `entlang`, `geradeaus`, `links`, `rechts`) và các nhãn tòa nhà trên bản đồ không chứa mạo từ `der`, `die`, `das`.
4. **Kiểm tra 0% Lặp Lại Câu Trong Lý Thuyết & 0% Trùng Lặp Câu Hỏi (`100% Originality & Deduplication Check`)**:
   * Xác nhận không có câu nào sao chép lại đoạn văn *Paula und Alex* hay *Hi Julia* của phần lý thuyết, và `len(set(questions)) == 100`.
5. **Kiểm tra Bảo Toàn Dữ Liệu Bài 1 $\rightarrow$ Bài 7 (`Zero-Regression Check`)**:
   * Xác nhận toàn bộ Bài 1 (P1, P2) đến Bài 7 vẫn nguyên vẹn 100%.
6. **Đồng bộ lên GitHub (`Git Commit & Push`)**:
   ```bash
   git add .
   git commit -m "Overhaul Lesson 8 exercises: 100 original map-navigation roleplay questions, deep Akkusativ/Dativ focus, zero spoilers/hints on prompts and SVG maps"
   git push origin main
   ```