# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 11 (A1) "KLEIDUNG UND WETTER — TRANG PHỤC, MÀU SẮC Ở AKKUSATIV, ĐẠI TỪ CHỈ ĐỊNH DIES-, THỜI TIẾT" — TÍCH HỢP SƠ ĐỒ TƯƠNG TÁC, BỘ DỮ LIỆU NGUỒN CHUẨN & 100 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2** → **Bài 10**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này chỉ gồm: **(1)** tạo mới hoàn toàn **Bài 11 (`lessons/a1/seed_a1_b11.py`)** ở vị trí **`lesson_order = 12`** của cấp độ **A1** (vì Bài 1 gồm 2 phần P1, P2 nên số thứ tự hiển thị lệch 1 so với `lesson_order`); **(2)** *cộng dồn thêm* động từ và từ vựng mới của Bài 11 vào 2 chuyên mục tra cứu; **(3)** *mở rộng thêm* (không thay thế) kiến thức Đấu trường tới Bài 11; **(4)** viết và chạy kịch bản kiểm thử toàn diện.
> * **Quy tắc chống ghi đè khi cộng dồn dữ liệu**: Nếu một động từ / danh từ của Bài 11 **đã tồn tại** trong `verbs_db.js` / `lexikon_db.js` từ bài trước (rất có thể đã có `das Wetter` từ Bài 10, `regnen` từ Bài 9...), thì **GIỮ NGUYÊN thẻ cũ, KHÔNG tạo thẻ trùng, KHÔNG sửa thẻ cũ**. Chỉ thêm các mục chưa có (so khớp theo `lemma` + `article`). Báo cáo ở cuối quá trình: *"đã thêm N thẻ mới, bỏ qua M thẻ trùng"*.
> * **Quy tắc chống phá vỡ giao diện cũ (`Zero-Regression for UI`)**: Các dạng bài mới của Bài 11 (xem mục 3.2) phải được làm bằng cách **thêm component mới hoặc tổng quát hóa component có sẵn một cách tương thích ngược** (ví dụ: `chon_haben_sein` của Bài 9 và `phan_loai_giong` của Bài 10 vẫn phải chạy y như cũ). Sau khi code xong, mở lại **Bài 8, Bài 9, Bài 10** để kiểm tra các dạng bài cũ vẫn hoạt động.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu. Video bài giảng chỉ là tài liệu tham khảo để soạn nội dung.
>
> ---
>
> ### 🎯 2. PHẠM VI KIẾN THỨC & ĐỘ KHÓ (`A1+ SCOPE CONTROL`)
> * **Ba trọng tâm của Bài 11** *(đúng theo yêu cầu của người dùng)*:
>   1. **Trang phục & màu sắc ở `Akkusativ`**: tính từ chỉ màu đứng trước danh từ chỉ trang phục, đuôi tính từ ở Akkusativ sau `ein- / eine / ein / (không mạo từ số nhiều)` (`einen schwarzen Rock · eine grüne Hose · ein blaues Kleid · rote Schuhe`) — **kết hợp ôn lại `Akkusativ` và `Dativ`** với đồ dùng quần áo (`tragen, anziehen, kaufen, suchen` → Akkusativ; `gefallen, passen, stehen, gehören` → Dativ).
>   2. **Đại từ chỉ định `dies-`** (`dieser, diesen, diese, dieses`): dùng kèm danh từ hoặc đứng một mình; luyện nhiều dạng bài trong bối cảnh trang phục, màu sắc và mẫu câu mua sắm đời thường.
>   3. **Thời tiết (`Wetter`)**: `Es regnet / schneit / ist windig / neblig / sonnig / bewölkt / kalt / heiß`, hỏi đáp về thời tiết (`Wie ist das Wetter in …? / bei dir? / bei euch?`), mùa, nhiệt độ, mặc gì theo thời tiết.
> * **Ôn tập có chủ đích**: `Komparativ` (Bài 10: `schöner, wärmer, kälter`), `Welch-` (Bài 10), `Perfekt` (Bài 9: `angezogen, geschneit, geregnet`), chia động từ có quy tắc (`tragen: trägst/trägt`, `anziehen`), đọc số/giá tiền (Bài 10) cho bài mua quần áo. Phần ôn chỉ chiếm số lượng nhỏ.
> * **Độ khó**: ở mức **bằng Bài 10 hoặc nhỉnh hơn một chút**. **Không** đưa vào bài tập: tính từ sau mạo từ xác định (`den roten Pullover` — chỉ nhận biết ⭐), tính từ ở `Nominativ` (cô giáo gạch bỏ cột này trên bảng — chỉ nhận biết ⭐), `Dativ` số nhiều có đuôi `-n` của danh từ, `Imperativ`, `Konjunktiv II` ngoài cụm cố định, câu phụ `weil / dass / wenn`.
>
> ---
>
> ### 🎨 3. QUY TẮC VÀNG VỀ MÀU SẮC & DATIV TRONG BÀI TẬP (`COLOR–DATIV SEPARATION RULES`) — **BẮT BUỘC TUYỆT ĐỐI**
> Người dùng yêu cầu: *"màu sắc chỉ nên dính tới Akkusativ; nếu có vế dính tới Dativ thì không được dính tới màu sắc"*. Do đó, trong **toàn bộ 100 câu bài tập và mọi bộ đề ngẫu nhiên**:
> * **R1 — Màu chỉ ở Akkusativ**: Từ chỉ màu (và tính từ chỉ màu có đuôi) **chỉ được xuất hiện** (a) trong **cụm tân ngữ Akkusativ** của câu (`… trägt einen schwarzen Rock`, `… kauft ein weißes Hemd`), hoặc (b) trong bài tập **từ vựng thuần túy** (dịch từ, nối từ - nghĩa) không nằm trong câu có chia cách.
> * **R2 — Câu có màu KHÔNG được chứa dấu hiệu Dativ**: đại từ Dativ (`mir, dir, ihm, ihnen, Ihnen, uns, euch`, `ihr`), mạo từ / sở hữu Dativ (`dem, einem, einer, meinem, meiner, deinem, deiner…`), giới từ đi với Dativ (`mit, bei, von, aus, nach, zu, zum, zur, im, am, beim, vom`), **động từ đi với Dativ** (`gefallen, passen, stehen, gehören, helfen, schenken, zeigen`).
> * **R3 — Câu Dativ không có màu**: mọi câu dùng `gefallen / passen / stehen / gehören` hoặc cấu trúc `Dativ + Akkusativ` (`schenken, kaufen für, zeigen`) **không được có từ chỉ màu**, kể cả khi màu nằm ở phần Akkusativ của cùng câu.
> * **R4 — Không dùng màu ở `Nominativ` / vị ngữ** trong bài tập (không có câu kiểu *„Der Mantel ist blau.“*).
> * **R5 — Màu bất biến** (`rosa, lila, pink, beige, orange, türkis, mint`) chỉ dùng trong 1 câu `tim_loi_sai` (Akkusativ) và trong bài từ vựng.
> * **R6 — Kiểm tra tự động**: `test_color_dativ_separation` (Phần 5) quét **toàn bộ** câu đề, đáp án, ví dụ, hội thoại, đoạn văn của 100 câu và của mọi bộ đề ngẫu nhiên. Vi phạm = **không đạt**.
> * Các câu trên bảng giảng có **cả màu lẫn Dativ** (*„Die blaue Jacke gefällt mir nicht.“*, *„Grün steht Ihnen sehr gut.“*) **chỉ được đặt ở phần lý thuyết** với nhãn `⚠️ chỉ để đọc hiểu — không dùng trong bài tập`, **không đưa vào bài tập**.
>
> ---
>
> ### 🗺️ 4. YÊU CẦU HÌNH ẢNH MINH HỌA (`VISUAL DIAGRAMS`) CHO BÀI 11
> Antigravity IDE **BẮT BUỘC** xây dựng module **`static/js/kleidung_svg.js`** (SVG nội tuyến, tương thích Dark/Light mode) gồm **6 sơ đồ** (đặc tả chi tiết ở **mục 2.9**): `V1` Bảng `dies- / welch-` tương tác; `V2` Bảng đuôi tính từ màu ở Akkusativ + tủ quần áo; `V3` Lưu đồ phân biệt Akkusativ / Dativ; `V4` Tủ quần áo tương tác (bấm món đồ → nghe câu `Ich trage …`); `V5` Bản đồ thời tiết Việt Nam - Đức; `V6` Cuộc hội thoại ở phòng thử đồ. Một số câu hỏi bài tập có trường `visual` (hoặc `weather_icon`).
>
> ---
>
> ### 🔍 5. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI & CHỐNG TRÙNG LẶP (`ZERO-BUG & ZERO-DUPLICATE QA PROTOCOL`)
> Các lỗi sau đã từng xuất hiện trên web và **KHÔNG ĐƯỢC LẶP LẠI**:
> 1. **Dịch sai nghĩa** → Mọi bản dịch tiếng Việt phải dịch **đúng câu tiếng Đức đã hoàn chỉnh** (đã điền đáp án), đúng thì, đúng ngôi, đúng màu sắc và đúng loại quần áo (không dịch `Rock` thành *"quần"*, `Hose` thành *"váy"*).
> 2. **Thiếu phần dịch nghĩa** → 100% từ vựng, ví dụ, đoạn văn, bảng lý thuyết và **100 câu hỏi** đều phải có phần dịch không rỗng (quy tắc từng dạng ở mục 3.2).
> 3. **Dịch / đáp án không liên quan đến đề bài** → Đề bài, hình minh họa, đáp án, dịch nghĩa và giải thích phải cùng sinh ra từ **một đối tượng dữ liệu duy nhất** (`single source of truth`). Mục `Giải thích` bắt buộc **chứa chính chuỗi đáp án đúng**.
> 4. **Voice thiếu / voice sai** → Mọi nút `🔊` phải có và chỉ truyền **chuỗi tiếng Đức sạch** (`de-DE`). Không đọc ký hiệu `___`, `[1]`, `→`, `°C`, `€`, emoji. **Nhiệt độ phải chuyển thành chữ** (`15 °C` → *„fünfzehn Grad“*, `-3 °C` → *„minus drei Grad“*); **kích cỡ** `Größe 38` → *„Größe achtunddreißig“*; **giá tiền** dùng `price_to_german()` của Bài 10.
> 5. **Ví dụ không khớp thẻ từ vựng** → Thẻ từ nào thì `example_de` phải chứa **đúng dạng từ đó** (số ít hoặc số nhiều của chính thẻ), và `example_vi` phải dịch đúng câu đó.
> 6. **Giải thích sai đáp án** → Giải thích phải khớp đáp án đúng và quy tắc ngữ pháp thật sự (ví dụ: không giải thích `einen roten Pullover` bằng "vì Pullover là giống cái").
> 7. **Chống trùng lặp câu hỏi 100%** → `len(set(normalized_questions)) == 100`. Toàn bộ 100 câu trong Bài 11 là câu **mới sáng tác**, chỉ *tham khảo* ý tưởng từ bảng giảng, **không sao chép** nguyên câu của giáo trình, của Bài 8, 9 hay 10.
> 8. **Đa dạng ngôi & ngữ cảnh** → Câu hỏi dùng đủ `ich, du, er, sie, es, wir, ihr, sie (số nhiều), Sie`, tên riêng, gia đình, nghề nghiệp; bối cảnh Việt Nam (Hà Nội, Huế, Đà Lạt, Sài Gòn, Hải Phòng) lẫn Đức - Áo (Berlin, Wien, Hamburg, München).
> 9. **Đúng giống & đúng đuôi** → Mọi cụm `mạo từ + tính từ màu + danh từ` phải đúng đuôi theo bảng ở Phụ lục A (giống - số của **danh từ quần áo** lấy từ bảng nguồn). Mọi dạng `dies-` phải đúng theo bảng A2.
> 10. **Không sửa bài cũ** → chạy `Zero-Regression Check` (xem Phần 5).
>
> ---
>
> ### ⚠️ 6. NHỮNG ĐIỂM CẦN CHUẨN HÓA SO VỚI BẢNG VIẾT TRÊN LỚP (ĐỌC KỸ TRƯỚC KHI CODE)
> Bảng giảng được viết tay nên có vài chỗ cần xử lý khi đưa lên web để người học **không học sai / không bối rối**:
> 1. **Bảng đuôi tính từ — cột `Nominativ` bị gạch chéo**: bảng ghi `m: er / en · f: e / e · n: es / es · PL: e (DT) / e (DT)`, trong đó cột `Nom/C1` bị **gạch bỏ**. Hiểu là cô giáo chỉ dạy **đuôi ở `Akkusativ`** (tiêu đề *"TT đi kèm DT có mạo từ …"* bị cắt dở — nội dung là *tính từ đi kèm danh từ có mạo từ bất định / không mạo từ*). Web: **phần chính = cột `Akkusativ` (`-en / -e / -es / -e`)**; cột `Nominativ` chỉ hiển thị mờ ở mục mở rộng ⭐ *"chỉ nhận biết"* và **không có trong bài tập**.
> 2. **Ký hiệu `e (DT)` ở số nhiều**: hiểu là *"đuôi `-e`, danh từ **không có mạo từ**"* (`braune Schuhe`, `weiße Schuhe`). Sau **mạo từ không đổi nguyên mẫu số nhiều** (`die`) quy tắc khác (`die braunen Schuhe`) — chỉ nhận biết ⭐.
> 3. **Màu bất biến** (không thêm đuôi): `orange, lila, rosa, pink, beige, türkis, mint` (bảng giảng liệt kê nhưng không nói rõ). Web thêm ghi chú và ví dụ: *eine rosa Jacke*, *ein beige Hemd*. Riêng `bunt` và `violett` **có thể chia đuôi** (`bunte Socken`, `ein violettes Kleid`).
> 4. **Nghĩa màu theo bảng**: `lila = tím hồng`, `violett = tím xanh`, `rosa = hồng nhạt`, `pink = hồng đậm`, `grau = ghi / xám`, `mint = xanh bạc hà`, `türkis = xanh ngọc`, `bunt = sặc sỡ`. Web giữ nguyên nghĩa theo bảng.
> 5. **`e. Wolken` → `die Wolke` (số nhiều `die Wolken`)**: bảng viết dạng số nhiều. Web hiển thị thẻ chuẩn `die Wolke (Pl. die Wolken)`.
> 6. **`die Kälte` / `die Hitze` là danh từ**, còn **`kalt` / `heiß` là tính từ**: nói *„Es ist kalt.“* / *„Es ist heiß.“* — **không** nói ~~*Es ist Kälte*~~.
> 7. **`VN` và `HP` trong câu hỏi thời tiết** là **Việt Nam** và **Hải Phòng**. Web hiển thị đầy đủ: *„Wie ist das Wetter in Vietnam? / in Hải Phòng? / bei dir? / bei euch?“*.
> 8. **`anziehen` và `tragen`**: bảng ghi `anziehen = tragen`. Thực tế: `tragen` = *mặc / đang mặc* (trạng thái); `anziehen` = *mặc vào* (hành động, động từ tách). Web giải thích rõ; Perfekt `hat angezogen` (ôn Bài 9).
> 9. **`ihr tragt`** (không `trägt`): ngôi `ihr` **không đổi nguyên âm**; chỉ `du trägst` và `er/sie/es trägt` đổi `a → ä`.
> 10. **Các câu trên bảng vừa có màu vừa có Dativ** (`Die blaue Jacke gefällt mir nicht.`, `Grün steht Ihnen sehr gut.`): xem R3 — **chỉ để đọc hiểu trong lý thuyết, không đưa vào bài tập**.
> 11. **`diesen … oder diesen`** trong câu hỏi trên bảng chỉ hai vật khác nhau (cô giáo chỉ vào từng vật). Web giải thích: *"hai lần `diesen` là hai cái áo khác nhau, người nói chỉ tay vào từng cái"*.
> 12. **`Größe 39 / 38 / 40`** là **cỡ giày / áo**; đọc số bằng chữ khi dùng `🔊` (`neununddreißig, achtunddreißig, vierzig`).
> 13. **`Wintermantel`** là danh từ ghép (`der Winter` + `der Mantel` = **`der Wintermantel`**, áo khoác mùa đông); `Trainingsanzug` = `der Trainingsanzug` (bộ đồ thể thao).
> 14. **`Beide sind warm`**: `beide` = *cả hai* (từ mới, thêm vào lý thuyết ⭐).

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 → Bài 10 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 11** theo quy tắc chống ghi đè ở mục 1.

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung **20 động từ trọng tâm của Bài 11** (trang phục - thời tiết - mua sắm). Với mỗi thẻ: bảng chia **Präsens** 6 ngôi, dòng **Perfekt**, loại động từ (**kèm cách đi cùng: Akk / Dativ**), phát âm `de-DE`, và 1 câu ví dụ **chứa đúng động từ đó** kèm dịch nghĩa. *(Các ví dụ dưới đây không dùng màu sắc; nếu có Dativ thì không có màu.)*

| # | Động từ (nghĩa) | Loại / Cách | Präsens: ich / du / er·sie·es / wir / ihr / sie·Sie | Perfekt | Ví dụ (`🔊 de-DE`) & Dịch |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **tragen** *(mặc, mang, đeo)* | Bất quy tắc `a → ä` · **+ Akk** | trage / **trägst** / **trägt** / tragen / tragt / tragen | hat getragen | *„Meine Schwester trägt gern Röcke.“* — Chị tôi thích mặc váy. |
| 2 | **anziehen** *(mặc vào)* | Động từ tách `an-` · **+ Akk** | ich ziehe … an / du ziehst … an / er zieht … an / wir ziehen … an / ihr zieht … an / sie ziehen … an | hat angezogen | *„Zuerst ziehe ich die Hose an.“* — Trước tiên tôi mặc quần vào. |
| 3 | **ausziehen** *(cởi ra)* | Động từ tách `aus-` · **+ Akk** | ich ziehe … aus / du ziehst … aus / er zieht … aus / wir ziehen … aus / ihr zieht … aus / sie ziehen … aus | hat ausgezogen | *„Am Abend ziehe ich die Schuhe aus.“* — Buổi tối tôi cởi giày ra. |
| 4 | **anprobieren** *(thử [quần áo])* | Tách `an-` + `-ieren` · **+ Akk** | ich probiere … an / du probierst … an / er probiert … an / wir probieren … an / ihr probiert … an / sie probieren … an | hat anprobiert | *„Ich probiere die Hose an.“* — Tôi thử chiếc quần. |
| 5 | **passen** *(vừa với)* | Có quy tắc · **+ Dativ** | passe / **passt** / passt / passen / passt / passen | hat gepasst | *„Die Schuhe passen mir sehr gut.“* — Đôi giày rất vừa với tôi. |
| 6 | **stehen** *(hợp, đứng)* | Bất quy tắc ở Partizip · **+ Dativ** (nghĩa "hợp") | stehe / stehst / steht / stehen / steht / stehen | hat gestanden | *„Der Hut steht dir gut.“* — Chiếc mũ hợp với bạn. |
| 7 | **gefallen** *(làm hài lòng, được thích)* | Bất quy tắc `a → ä` · **+ Dativ** | gefalle / **gefällst** / **gefällt** / gefallen / gefallt / gefallen | hat gefallen | *„Wie gefällt dir die Jacke?“* — Bạn thấy cái áo khoác thế nào (có thích không)? |
| 8 | **gehören** *(thuộc về)* | Có quy tắc, tiền tố `ge-` · **+ Dativ** | gehöre / gehörst / gehört / gehören / gehört / gehören | hat gehört | *„Der Schal gehört meiner Mutter.“* — Chiếc khăn này là của mẹ tôi. |
| 9 | **suchen** *(tìm)* | Có quy tắc · **+ Akk** | suche / suchst / sucht / suchen / sucht / suchen | hat gesucht | *„Ich suche eine Hose.“* — Tôi đang tìm một chiếc quần. |
| 10 | **finden** *(thấy, tìm thấy)* | Gốc `-d` → thêm `-e-` · **+ Akk** | finde / **findest** / **findet** / finden / **findet** / finden | hat gefunden | *„Wo finde ich Handschuhe?“* — Tôi tìm găng tay ở đâu? |
| 11 | **schenken** *(tặng)* | Có quy tắc · **+ Dativ + Akk** | schenke / schenkst / schenkt / schenken / schenkt / schenken | hat geschenkt | *„Ich schenke meinem Vater eine Krawatte.“* — Tôi tặng bố tôi một chiếc cà vạt. |
| 12 | **zeigen** *(cho xem)* | Có quy tắc · **+ Dativ + Akk** | zeige / zeigst / zeigt / zeigen / zeigt / zeigen | hat gezeigt | *„Die Verkäuferin zeigt mir einen Anzug.“* — Nhân viên bán hàng cho tôi xem một bộ com lê. |
| 13 | **helfen** *(giúp đỡ)* | Bất quy tắc `e → i` · **+ Dativ** | helfe / **hilfst** / **hilft** / helfen / helft / helfen | hat geholfen | *„Kann ich Ihnen helfen?“* — Tôi có thể giúp gì cho ngài ạ? |
| 14 | **mitnehmen** *(mang theo)* | Động từ tách `mit-`, bất quy tắc · **+ Akk** | ich nehme … mit / du nimmst … mit / er nimmt … mit / wir nehmen … mit / ihr nehmt … mit / sie nehmen … mit | hat mitgenommen | *„Bei Regen nehme ich einen Regenschirm mit.“* — Khi trời mưa tôi mang theo một chiếc ô. |
| 15 | **aussehen** *(trông có vẻ)* | Tách `aus-`, bất quy tắc `e → ie` | ich sehe … aus / du siehst … aus / er sieht … aus / wir sehen … aus / ihr seht … aus / sie sehen … aus | hat ausgesehen | *„Du siehst in dem Anzug gut aus.“* — Bạn trông rất đẹp trong bộ com lê. |
| 16 | **schneien** *(tuyết rơi)* | Có quy tắc, chỉ ngôi `es` | es schneit | hat geschneit | *„Im Januar schneit es in den Alpen.“* — Vào tháng Giêng tuyết rơi ở dãy Alps. |
| 17 | **scheinen** *(chiếu sáng)* | Bất quy tắc ở Partizip | scheine / scheinst / scheint / scheinen / scheint / scheinen | hat geschienen | *„Heute scheint die Sonne.“* — Hôm nay mặt trời chiếu sáng (trời nắng). |
| 18 | **gewittern** *(có dông)* | Có quy tắc, chỉ ngôi `es` | es gewittert | hat gewittert | *„Heute Nacht gewittert es.“* — Đêm nay có dông. |
| 19 | **frieren** *(thấy lạnh, rét)* | Bất quy tắc ở Partizip | friere / frierst / friert / frieren / friert / frieren | hat gefroren | *„Ich friere ohne Handschuhe.“* — Tôi thấy lạnh khi không có găng tay. |
| 20 | **schwitzen** *(đổ mồ hôi)* | Gốc `-z` → `du schwitzt` | schwitze / **schwitzt** / schwitzt / schwitzen / schwitzt / schwitzen | hat geschwitzt | *„Bei Hitze schwitze ich viel.“* — Khi trời nóng tôi đổ nhiều mồ hôi. |

> 📌 **Lưu ý hiển thị**: Mỗi thẻ động từ phải có nhãn **cách đi cùng** (`+ Akk` / `+ Dativ` / `+ Dativ + Akk`) in nổi bật — đây là kiến thức ôn **Akkusativ / Dativ** trọng tâm của bài. Các động từ đã có thẻ từ bài trước (`regnen`, `probieren`, `einkaufen`...) **không tạo thẻ trùng**. Phát âm `🔊` luôn đọc **một câu hoàn chỉnh**.

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung **2 chủ đề lọc mới** với đầy đủ **50 danh từ có mạo từ `der/die/das`, dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng thẻ** (danh từ nào đã có ở bài trước — ví dụ `das Wetter` — thì **giữ thẻ cũ, không tạo trùng**). *Các câu ví dụ trong bảng dưới đây không có màu sắc.*

#### Chủ đề A: `Kleidung: Trang phục & Phụ kiện (Bài 11)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **der Stiefel** | die Stiefel | bốt | Im Schnee trage ich gern Stiefel. | Trong tuyết tôi thích đi bốt. |
| 2 | **der Mantel** | die Mäntel | áo măng tô | Bei Kälte trage ich einen Mantel. | Khi trời lạnh tôi mặc áo măng tô. |
| 3 | **der Pullover** | die Pullover | áo len chui đầu | Heute trage ich einen Pullover. | Hôm nay tôi mặc một chiếc áo len. |
| 4 | **der Rock** | die Röcke | chân váy | Meine Schwester trägt gern einen Rock. | Chị tôi thích mặc chân váy. |
| 5 | **der Anzug** | die Anzüge | bộ com lê | Mein Vater trägt einen Anzug und eine Krawatte. | Bố tôi mặc bộ com lê và thắt cà vạt. |
| 6 | **der Schuh** | die Schuhe | giày | Die Schuhe sind Größe neununddreißig. | Đôi giày này cỡ ba mươi chín. |
| 7 | **der Gürtel** | die Gürtel | thắt lưng | Ich brauche einen Gürtel für die Hose. | Tôi cần một chiếc thắt lưng cho cái quần. |
| 8 | **der Hut** | die Hüte | mũ (có vành) | In der Sonne trägt er einen Hut. | Dưới nắng anh ấy đội một chiếc mũ. |
| 9 | **der Handschuh** | die Handschuhe | găng tay | Bei Kälte trage ich Handschuhe. | Khi trời lạnh tôi đeo găng tay. |
| 10 | **die Jeans** | die Jeans | quần bò | Ich trage gern Jeans und ein T-Shirt. | Tôi thích mặc quần bò và áo phông. |
| 11 | **die Jacke** | die Jacken | áo khoác | Im Herbst trage ich eine Jacke. | Vào mùa thu tôi mặc áo khoác. |
| 12 | **die Hose** | die Hosen | quần | Die Hose ist mir zu lang. | Chiếc quần này dài quá đối với tôi. |
| 13 | **die Bluse** | die Blusen | áo sơ mi nữ | Sie trägt eine Bluse und einen Rock. | Cô ấy mặc áo sơ mi nữ và chân váy. |
| 14 | **die Socke** | die Socken | tất | Ich brauche warme Socken. | Tôi cần những đôi tất ấm. |
| 15 | **die Krawatte** | die Krawatten | cà vạt | Mein Onkel trägt eine Krawatte. | Chú tôi thắt cà vạt. |
| 16 | **das T-Shirt** | die T-Shirts | áo phông | Im Sommer trage ich ein T-Shirt. | Mùa hè tôi mặc áo phông. |
| 17 | **das Hemd** | die Hemden | áo sơ mi nam | Er trägt ein Hemd und eine Krawatte. | Anh ấy mặc áo sơ mi và thắt cà vạt. |
| 18 | **das Kleid** | die Kleider | đầm, váy liền | Sie trägt ein Kleid zur Party. | Cô ấy mặc một chiếc đầm đi dự tiệc. |
| 19 | **der Schal** | die Schals | khăn quàng | Im Winter brauche ich einen Schal. | Mùa đông tôi cần một chiếc khăn quàng. |
| 20 | **die Mütze** | die Mützen | mũ len, mũ lưỡi trai | Bei Kälte trage ich eine Mütze. | Khi trời lạnh tôi đội mũ len. |
| 21 | **der Regenmantel** | die Regenmäntel | áo mưa | Bei Regen trage ich einen Regenmantel. | Khi trời mưa tôi mặc áo mưa. |
| 22 | **der Regenschirm** | die Regenschirme | cái ô | Ich nehme heute einen Regenschirm mit. | Hôm nay tôi mang theo một chiếc ô. |
| 23 | **die Sonnenbrille** | die Sonnenbrillen | kính râm | Bei Sonne trage ich eine Sonnenbrille. | Khi trời nắng tôi đeo kính râm. |
| 24 | **die Größe** | die Größen | cỡ, kích cỡ | Welche Größe haben Sie? | Ngài mặc cỡ nào ạ? |
| 25 | **die Umkleidekabine** | die Umkleidekabinen | phòng thử đồ | Die Umkleidekabine ist dort hinten. | Phòng thử đồ ở phía sau kia. |

#### Chủ đề B: `Wetter & Jahreszeiten & Einkaufen: Thời tiết, Mùa, Mua sắm (Bài 11)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 26 | **der Regen** | *(nur Singular)* | mưa | Bei Regen bleibe ich zu Hause. | Khi trời mưa tôi ở nhà. |
| 27 | **der Schnee** | *(nur Singular)* | tuyết | Im Winter liegt viel Schnee in den Bergen. | Vào mùa đông có nhiều tuyết trên núi. |
| 28 | **der Wind** | die Winde | gió | Der Wind ist heute kalt. | Hôm nay gió lạnh. |
| 29 | **der Nebel** | die Nebel | sương mù | Im Herbst gibt es oft Nebel. | Vào mùa thu thường có sương mù. |
| 30 | **der Sturm** | die Stürme | bão, cơn bão | Der Sturm kommt heute Abend. | Tối nay bão đến. |
| 31 | **der Himmel** | die Himmel | bầu trời | Der Himmel ist heute bewölkt. | Hôm nay bầu trời nhiều mây. |
| 32 | **der Frühling** | die Frühlinge | mùa xuân | Im Frühling ist es warm. | Vào mùa xuân trời ấm. |
| 33 | **der Sommer** | die Sommer | mùa hè | Im Sommer ist es heiß. | Vào mùa hè trời nóng. |
| 34 | **der Herbst** | die Herbste | mùa thu | Im Herbst regnet es oft. | Vào mùa thu trời hay mưa. |
| 35 | **der Winter** | die Winter | mùa đông | Im Winter schneit es in Deutschland. | Vào mùa đông ở Đức có tuyết rơi. |
| 36 | **der Wetterbericht** | die Wetterberichte | bản tin thời tiết | Der Wetterbericht sagt Regen. | Bản tin thời tiết báo có mưa. |
| 37 | **der Kleiderschrank** | die Kleiderschränke | tủ quần áo | Mein Kleiderschrank ist voll. | Tủ quần áo của tôi đầy ắp. |
| 38 | **die Sonne** | die Sonnen | mặt trời | Heute scheint die Sonne. | Hôm nay mặt trời chiếu sáng. |
| 39 | **die Wolke** | die Wolken | đám mây | Am Himmel sind viele Wolken. | Trên bầu trời có nhiều mây. |
| 40 | **die Kälte** | *(nur Singular)* | cái lạnh, khí lạnh | Bei Kälte friere ich schnell. | Khi trời lạnh tôi dễ bị rét. |
| 41 | **die Hitze** | *(nur Singular)* | cái nóng, khí nóng | Bei Hitze schwitze ich viel. | Khi trời nóng tôi đổ nhiều mồ hôi. |
| 42 | **die Temperatur** | die Temperaturen | nhiệt độ | Die Temperatur ist heute sehr hoch. | Hôm nay nhiệt độ rất cao. |
| 43 | **die Jahreszeit** | die Jahreszeiten | mùa (trong năm) | Welche Jahreszeit magst du am liebsten? | Bạn thích mùa nào nhất? |
| 44 | **die Farbe** | die Farben | màu sắc | Welche Farbe hat dein Hemd? | Chiếc áo sơ mi của bạn màu gì? |
| 45 | **die Mode** | *(nur Singular)* | thời trang | Meine Schwester mag Mode. | Chị tôi thích thời trang. |
| 46 | **das Wetter** | *(nur Singular)* | thời tiết | Wie ist das Wetter heute? | Hôm nay thời tiết thế nào? |
| 47 | **das Gewitter** | die Gewitter | cơn dông | Am Abend gibt es ein Gewitter. | Buổi tối có một cơn dông. |
| 48 | **das Grad** | die Grad | độ (nhiệt độ) | Heute sind es zwanzig Grad. | Hôm nay là hai mươi độ. |
| 49 | **das Kaufhaus** | die Kaufhäuser | trung tâm bách hóa | Im Kaufhaus gibt es viele Mäntel. | Ở trung tâm bách hóa có nhiều áo măng tô. |
| 50 | **das Geschäft** | die Geschäfte | cửa hàng | Das Geschäft öffnet um neun Uhr. | Cửa hàng mở cửa lúc chín giờ. |

> ✅ **Mẹo quy tắc giống hiển thị trên thẻ**: **Nhiều thứ trang phục dài / ngoài là `der`** (`der Mantel, der Rock, der Anzug, der Hut, der Gürtel`); **đuôi `-e` thường là `die`** (`die Jacke, die Hose, die Bluse, die Socke, die Krawatte, die Mütze`); **`das Hemd, das Kleid, das T-Shirt`** là giống trung. Danh từ **chỉ số ít**: `der Regen, der Schnee, die Kälte, die Hitze, die Mode, das Wetter`. Danh từ **số nhiều về hình thức**: `die Jeans` (cũng dùng số ít nghĩa "một chiếc quần bò" → vẫn `die Jeans`). Bốn mùa **đều là `der`**: `der Frühling, der Sommer, der Herbst, der Winter` (nói `im Winter` = `in dem Winter`). Danh từ **nhiệt độ sau số đếm không đổi**: `zwanzig Grad`.

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 11: "KLEIDUNG UND WETTER — TRANG PHỤC, MÀU SẮC Ở AKKUSATIV, DIES-, THỜI TIẾT"

Bài học thứ 12 trong danh sách Cấp độ A1 (`lesson_order = 12`):
* **Tiêu đề bài học (hiển thị ở danh mục bên trái, nên giữ ngắn)**: `Bài 11: Kleidung - Farbe - dies- - Wetter` · **Tiêu đề đầy đủ ở khung bài**: `Bài 11: Kleidung - Die Farbe in Akkusativ - dies- (Đại từ chỉ định) - Wetter`.
* **Mô tả ngắn**: `Học từ vựng trang phục (der Mantel, die Jacke, das Kleid...) và 17 màu sắc; gắn màu vào trang phục ở Akkusativ (einen schwarzen Rock, eine rote Bluse, ein grünes Kleid, braune Schuhe); ôn Akkusativ - Dativ với tragen / anziehen / gefallen / passen / stehen; làm chủ đại từ chỉ định dies- (dieser / diesen / diese / dieses) và nói về thời tiết (Es regnet, Es ist windig, Wie ist das Wetter bei dir?); đi mua quần áo và thử đồ.`

### 2.0. CẤU TRÚC HIỂN THỊ TRANG LÝ THUYẾT (khớp giao diện thực tế của Bài 10)
Quan sát giao diện Bài 10 trên web (ảnh chụp và video quay màn hình), trang lý thuyết gồm các thành phần sau — **Bài 11 phải dùng đúng bố cục này** để người học thấy nhất quán:
| Thành phần | Nội dung cho Bài 11 |
| :--- | :--- |
| **Huy hiệu đầu khung** (viên thuốc xanh) | `DeutschMeister A1 • Kleidung & Wetter • Akkusativ • dies- (Bài 11)` |
| **Huy hiệu thứ hai** | `100 Bài tập Zero-Bug QA • 6 Sơ đồ SVG Tương tác` |
| **Tiêu đề lớn** | `Kleidung und Wetter: Trang phục, Màu sắc ở Akkusativ, dies- & Thời tiết` |
| **Đoạn mô tả** | Dùng "Mô tả ngắn" ở trên |
| **4 viên thuốc chủ đề** | `👗 50 Từ vựng trang phục & thời tiết` · `🎨 Farbe + Akkusativ (-en / -e / -es / -e)` · `👉 dies- (dieser / diesen / diese / dieses)` · `🌦️ Wetter & Akkusativ vs Dativ` |
| **Các thẻ mục đánh số 1 → 9** (vòng tròn số xanh + tiêu đề + phụ đề) | Học phần 1 → 9 bên dưới; mỗi thẻ có tiêu đề (`Từ Vựng Trang Phục (Kleidung) Theo 3 Giống`…) và **một dòng phụ đề** mô tả |
| **Lưới thẻ từ vựng** | Mỗi danh từ một thẻ: mạo từ (nhãn màu `der` xanh dương / `die` đỏ / `das` xanh lá), từ, số nhiều, nghĩa, câu ví dụ nghiêng kèm biểu tượng loa; nút **Phát âm** |
| **Khung nhấn mạnh (vàng)** | Dùng cho quy tắc quan trọng (ví dụ *"Mẹo nhớ giống"*, *"Quy tắc màu sắc chỉ dùng với Akkusativ"*) |
| **Sơ đồ SVG nhúng trong thẻ mục** | `V1` ở mục 5 · `V2` ở mục 3 · `V3` ở mục 4 · `V4` ở mục 1 · `V5` ở mục 6 · `V6` ở mục 7 (có tiêu đề `Sơ đồ V#: …` và nút chuyển ví dụ `◀ 1 / n ▶`) |
| **Thẻ cuối trang** | `Nắm Vững Toàn Bộ Lý Thuyết Bài Học?` + nút **`Đã hoàn thành`** + nút **`Lý thuyết đã xong • Tiếp tục làm bài tập ➜`** (nhảy sang `Phần 2: Bài tập`) |
| **Tab bài tập** | Nhãn **`Phần 2: Bài tập (Đủ 18 Dạng)`** (số dạng tính **động** từ dữ liệu của bài) |

#### 2.0.1. Lỗi giao diện đã quan sát được ở Bài 10 — **KHÔNG được lặp lại ở Bài 11**
* **Thanh bộ lọc dạng bài hiển thị sai thứ tự và sai đánh số**: ở Bài 10 các chip hiện ra theo thứ tự `… 10. Sắp xếp câu → 12. Tìm lỗi sai → 14. Đúng / Sai → 11. Phân loại der / die / das → 13. Viết lại so sánh → 15 → 16`, trong khi bảng phân bổ (mục 3.1 của Bài 10) quy định `11 = Phân loại, 12 = Tìm lỗi sai, 13 = Viết lại so sánh, 14 = Đúng / Sai`. **Yêu cầu cho Bài 11**: các chip phải **sắp tăng dần theo STT ở bảng 3.1** (1 → 18) và **số hiển thị trên chip = STT trong bảng 3.1**; nếu hai thứ này khác nhau thì **không đạt**. (Việc sửa thứ tự chip của **Bài 10** là một sửa lỗi hiển thị riêng — chỉ thực hiện khi người dùng đồng ý, không được làm ảnh hưởng nội dung bài.)
* **Số lượng dạng bài**: nhãn tab của Bài 11 phải ghi **`Đủ 18 Dạng`** (tính từ dữ liệu), không để số cố định.
* **Giải thích**: văn bản giải thích hiển thị trên web (ví dụ ở Bài 10) có dạng *"… nên từ hỏi biến đổi thành … → Đáp án: …"* — **giữ phong cách này** và luôn kết thúc bằng *"→ Đáp án: …"* chứa đáp án đúng.

---

### HỌC PHẦN 1: TỪ VỰNG TRANG PHỤC (`DIE KLEIDUNG`)
> 💡 **Cách đọc ký hiệu trên bảng giảng**: `r.` = **der**, `e.` = **die**, `s.` = **das**; trong ngoặc là **số nhiều**; `(-)` = số nhiều **giữ nguyên**; `(Sg.)` = chỉ có số ít.

#### 1.1. Bảng từ vựng chính (khớp bảng giảng) — phân theo 3 giống *(sơ đồ `V4` đi kèm)*
| Giống Đực (<span style="color:#3b82f6">**`der`**</span>) | Giống Cái (<span style="color:#f43f5e">**`die`**</span>) | Giống Trung (<span style="color:#10b981">**`das`**</span>) |
| :--- | :--- | :--- |
| • **der Stiefel** *(Pl: die Stiefel)*: bốt<br>• **der Mantel** *(Pl: die M<u>ä</u>ntel)*: áo măng tô<br>• **der Pullover** *(Pl: die Pullover)*: áo chui đầu, áo len<br>• **der Rock** *(Pl: die R<u>ö</u>cke)*: chân váy<br>• **der Anzug** *(Pl: die Anz<u>ü</u>ge)*: bộ com lê<br>• **der Schuh** *(Pl: die Schuhe)*: giày<br>• **der Gürtel** *(Pl: die Gürtel)*: thắt lưng<br>• **der Hut** *(Pl: die H<u>ü</u>te)*: mũ<br>• **der Handschuh** *(Pl: die Handschuhe)*: găng tay | • **die Jeans** *(Pl: die Jeans)*: quần bò<br>• **die Jacke** *(Pl: die Jacken)*: áo khoác<br>• **die Hose** *(Pl: die Hosen)*: quần<br>• **die Bluse** *(Pl: die Blusen)*: áo sơ mi nữ<br>• **die Socke** *(Pl: die Socken)*: tất<br>• **die Krawatte** *(Pl: die Krawatten)*: cà vạt | • **das T-Shirt** *(Pl: die T-Shirts)*: áo phông<br>• **das Hemd** *(Pl: die Hemden)*: áo sơ mi nam<br>• **das Kleid** *(Pl: die Kleider)*: đầm, váy liền |

> 🔎 **Mẹo nhớ giống & số nhiều (không học vẹt)**:
> * **Đuôi `-e` thường là `die`**: `die Jacke, die Hose, die Bluse, die Socke, die Krawatte`. Cặp **`der Schuh` ↔ `die Schuhe`**: nhiều khi đồ **đi theo đôi** nên hay dùng **số nhiều** (`Schuhe, Socken, Stiefel, Handschuhe, Jeans`).
> * **Danh từ đuôi `-el`, `-er` giữ nguyên số nhiều**: `der Stiefel → die Stiefel`, `der Gürtel → die Gürtel`, `der Pullover → die Pullover`.
> * **Thêm Umlaut khi số nhiều**: `der Mantel → die Mäntel`, `der Rock → die Röcke`, `der Anzug → die Anzüge`, `der Hut → die Hüte`.
> * **`die Jeans`** có hình thức số nhiều nhưng vẫn dùng cho *"một chiếc quần bò"*: *„Ich kaufe eine Jeans.“* hoặc *„Ich kaufe Jeans.“* — vẫn là `die Jeans`.
> * **`das Paar`** (*đôi*): *„ein Paar Schuhe“*, *„zwei Paar Socken“* (sau số đếm `Paar` giữ nguyên).

#### 1.2. Mở rộng ⭐: 16 trang phục - phụ kiện bổ sung (mỗi từ có `🔊`)
| Nhóm | Từ vựng (mạo từ, số nhiều) & Nghĩa |
| :--- | :--- |
| **Mặc ngoài / theo thời tiết** | **der Wintermantel** *(die Wintermäntel)*: áo khoác mùa đông · **der Regenmantel** *(die Regenmäntel)*: áo mưa · **die Weste** *(Westen)*: áo gi-lê · **der Trainingsanzug** *(die Trainingsanzüge)*: bộ đồ thể thao · **das Sweatshirt** *(Sweatshirts)*: áo nỉ |
| **Phụ kiện** | **der Schal** *(Schals)*: khăn quàng · **die Mütze** *(Mützen)*: mũ len, mũ lưỡi trai · **die Sonnenbrille** *(Sonnenbrillen)*: kính râm · **der Regenschirm** *(Regenschirme)*: cái ô · **die Tasche** *(Taschen)*: túi xách |
| **Đồ mặc nhà - đi biển** | **der Schlafanzug** *(Schlafanzüge)*: đồ ngủ · **der Badeanzug** *(Badeanzüge)*: đồ bơi nữ · **die Shorts** *(nur Pl.)*: quần short |
| **Mua sắm** | **die Größe** *(Größen)*: cỡ · **die Umkleidekabine** *(Umkleidekabinen)*: phòng thử đồ · **das Kaufhaus** *(Kaufhäuser)*: trung tâm bách hóa · **das Geschäft** *(Geschäfte)*: cửa hàng |

#### 1.3. Tính từ nói về quần áo (⭐ mở rộng, mỗi từ có `🔊`)
| Tính từ | Nghĩa | Ví dụ (`🔊 de-DE`) — *không có màu, có thể có Dativ* | Dịch |
| :--- | :--- | :--- | :--- |
| **groß / klein** | to, rộng / nhỏ, chật | *„Der Pullover ist mir zu groß.“* | Chiếc áo len này rộng quá đối với tôi. |
| **lang / kurz** | dài / ngắn | *„Die Hose ist mir zu lang.“* | Chiếc quần dài quá đối với tôi. |
| **eng / weit** | chật, bó / rộng | *„Die Schuhe sind mir zu eng.“* | Đôi giày chật quá đối với tôi. |
| **warm / kalt** | ấm / lạnh | *„Der Mantel ist sehr warm.“* | Chiếc áo măng tô rất ấm. |
| **schön / hässlich** | đẹp / xấu | *„Das Kleid ist schön.“* | Chiếc đầm này đẹp. |
| **bequem** | thoải mái, dễ chịu | *„Die Jeans ist bequem.“* | Chiếc quần bò này thoải mái. |
| **elegant / sportlich** | thanh lịch / thể thao | *„Der Anzug sieht elegant aus.“* | Bộ com lê trông thanh lịch. |
| **teuer / billig** | đắt / rẻ | *„Der Mantel ist teuer.“* | Chiếc áo măng tô đắt. |

---

### HỌC PHẦN 2: 17 MÀU SẮC (`DIE FARBE`)

#### 2.1. Bảng màu sắc (khớp bảng giảng)
| Màu | Nghĩa (theo bảng giảng) | Màu | Nghĩa | Màu | Nghĩa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **rot** | đỏ | **grau** | ghi / xám | **hellrot** | đỏ nhạt (sáng) |
| **orange** | cam | **braun** | nâu | **hellblau** | xanh nhạt (sáng) |
| **gelb** | vàng | **mint** | xanh bạc hà | **dunkelbraun** | nâu đậm (tối) |
| **grün** | xanh lá | **beige** | be | | |
| **blau** | xanh da trời | **türkis** | màu xanh ngọc | **hell-** | sáng |
| **lila** | tím hồng | **bunt** | sặc sỡ | **dunkel-** | tối |
| **violett** | tím xanh | | | | |
| **rosa** | hồng nhạt | | | | |
| **pink** | hồng đậm | | | | |
| **schwarz** | đen | | | | |
| **weiß** | trắng | | | | |

> 🔑 **Cách ghép màu đậm - nhạt**: `hell-` hoặc `dunkel-` + màu, **viết liền một từ**: `hellrot, hellblau, hellgrün, dunkelbraun, dunkelblau, dunkelgrün`. Từ ghép này **chia đuôi như màu gốc** (`einen hellblauen Pullover`).
> 🔑 **Màu viết thường khi làm tính từ**: `rot, blau, grün`. Khi là danh từ (tên màu) **viết hoa**: *„das Rot“*, *„in Grün“* (cụm cố định ở cửa hàng; xem mục 7).

#### 2.2. Màu có chia đuôi và màu bất biến (quan trọng, bảng giảng không nêu)
| Loại | Các màu | Ví dụ (`🔊 de-DE`) — *Akkusativ, không có Dativ* | Dịch |
| :--- | :--- | :--- | :--- |
| **Có chia đuôi** (như mọi tính từ) | `rot, gelb, grün, blau, schwarz, weiß, grau, braun, bunt, violett`, mọi từ ghép `hell-/dunkel-` | *„Ich kaufe einen **roten** Schal.“* · *„Sie trägt eine **graue** Hose.“* · *„Er kauft ein **violettes** Hemd.“* · *„Wir brauchen **bunte** Socken.“* | Tôi mua một chiếc khăn đỏ. · Cô ấy mặc một chiếc quần xám. · Anh ấy mua một chiếc áo sơ mi tím. · Chúng tôi cần những đôi tất sặc sỡ. |
| **Bất biến** (không thêm đuôi) | `orange, lila, rosa, beige, türkis, mint` *(và `pink` thường dùng không đuôi)* | *„Sie trägt eine **rosa** Bluse.“* · *„Ich kaufe ein **lila** Kleid.“* · *„Er sucht ein **beige** Hemd.“* | Cô ấy mặc một chiếc áo sơ mi nữ màu hồng. · Tôi mua một chiếc đầm màu tím hồng. · Anh ấy tìm một chiếc áo sơ mi màu be. |

> ⚠️ **Mẹo ghi nhớ màu bất biến**: Đa số là **từ mượn nước ngoài hoặc tên vật** (`orange` = quả cam, `rosa` = hoa hồng, `lila` = hoa tử đinh hương, `beige`, `türkis`, `mint` từ tiếng Pháp / Thổ). **Không** nói ~~*eine rosane Bluse*~~, ~~*ein lilanes Kleid*~~.

#### 2.3. Hỏi về màu sắc ⭐ (mở rộng — *chỉ để hiểu; không có trong bài tập*, vì ở dạng vị ngữ `Nominativ`)
* *„Welche Farbe hat dein Mantel?“* — Chiếc áo măng tô của bạn màu gì? · *„Mein Mantel ist grau.“* — Áo măng tô của tôi màu xám. *(Ở dạng **vị ngữ** — sau `sein` — màu **không có đuôi**.)*
* **`die Lieblingsfarbe`** *(Pl: die Lieblingsfarben)*: màu yêu thích — *„Meine Lieblingsfarbe ist Blau.“*

---

### HỌC PHẦN 3: ⭐ MÀU SẮC & TRANG PHỤC Ở `AKKUSATIV` — TÍNH TỪ CÓ ĐUÔI (TRỌNG TÂM THỨ NHẤT) ⭐

> 🧭 **Bản đồ phần này**: 3.1 Nhắc lại Akkusativ → 3.2 `tragen` và `anziehen` → 3.3 Bảng đuôi tính từ màu ở Akkusativ → 3.4 Cách tạo cụm `mạo từ + màu + danh từ` (3 bước) → 3.5 Màu bất biến - ghép `hell-/dunkel-` → 3.6 Phân tích câu trên bảng → 3.7 Mười lỗi thường gặp → 3.8 Mở rộng ⭐.

#### 3.1. Nhắc lại `Akkusativ` (cách 4) — tân ngữ trực tiếp
* **`Akkusativ`** trả lời cho câu hỏi **`Wen?` / `Was?`** (*"ai?" / "cái gì?"*): vật hoặc người **chịu tác động trực tiếp** của động từ. *„Ich trage **einen Mantel**.“* → *Was trage ich?* — *einen Mantel*.
* **Chỉ giống ĐỰC mới đổi mạo từ ở Akkusativ**; giống cái, giống trung, số nhiều **giữ nguyên** như Nominativ:
| | Giống đực (m) | Giống cái (f) | Giống trung (n) | Số nhiều (PL) |
| :--- | :--- | :--- | :--- | :--- |
| **Mạo từ xác định** | der → **den** | die → die | das → das | die → die |
| **Mạo từ bất định** | ein → **einen** | eine → eine | ein → ein | *(không có)* |

* **Động từ đi với `Akkusativ` trong bài này** *(sơ đồ `V3`)*: `tragen, anziehen, ausziehen, anprobieren, kaufen, suchen, finden, nehmen, brauchen, mitnehmen, haben, möchten`.

#### 3.2. `tragen` (mặc) và `anziehen` (mặc vào) *(khớp bảng giảng)*
| Ngôi | **tragen** (mặc, mang) | **anziehen** (mặc vào) |
| :--- | :--- | :--- |
| **ich** | trage | ziehe … an |
| **du** | **trägst** | ziehst … an |
| **er / sie / es** | **trägt** | zieht … an |
| **wir** | tragen | ziehen … an |
| **ihr** | **tragt** *(không đổi nguyên âm)* | zieht … an |
| **sie / Sie** | tragen | ziehen … an |

* **Hỏi - đáp** *(bảng giảng)*: *„Was tragen Sie heute?“* — Hôm nay ngài mặc gì? · *„Heute trage ich ein Kleid.“* — Hôm nay tôi mặc một chiếc đầm. · *„Was tragen Sie gern?“* — Ngài thích mặc gì? · *„Ich trage gern Jeans.“* — Tôi thích mặc quần bò.
* **`tragen` ≠ `anziehen`**: `tragen` = **đang mặc / thường mặc** (trạng thái). `anziehen` = **hành động mặc vào** (động từ tách; Perfekt `hat angezogen`). *„Ich trage heute einen Pullover.“* — Hôm nay tôi mặc áo len. *„Ich ziehe den Pullover an.“* — Tôi mặc cái áo len vào. *„Er hat einen Mantel angezogen.“* — Anh ấy đã mặc áo măng tô vào. *(Bảng giảng ghi `anziehen = tragen` vì trong nhiều câu hai từ có thể thay nhau.)*
* **Quy tắc mạo từ (bảng giảng)**: lần đầu **nhắc đến** một món đồ (tân ngữ Akkusativ) → dùng **mạo từ bất định** (`ein / eine / einen`): *„Heute trage ich **ein** Kleid.“* · *„Heute trage ich **eine** Jacke und **einen** Rock.“* — Hôm nay tôi mặc một chiếc áo khoác và một chiếc chân váy. Khi nói đến món đồ **đã biết**, dùng mạo từ xác định (`den, die, das`).

#### 3.3. BẢNG ĐUÔI TÍNH TỪ Ở AKKUSATIV *(khớp bảng giảng; sơ đồ `V2`)*
> ### 📐 CÔNG THỨC: &nbsp; **`mạo từ bất định (ein-) + màu + ĐUÔI + danh từ`** — đuôi ở Akkusativ: **m `-en` · f `-e` · n `-es` · PL `-e`**

| Giống / số | Mạo từ bất định | Đuôi tính từ (Akkusativ) | Ví dụ (`🔊 de-DE`) | Dịch |
| :--- | :--- | :---: | :--- | :--- |
| **m** (giống đực) | **einen** | **-en** | *„Ich trage gern **einen schwarzen** Rock.“* | Tôi thích mặc một chiếc chân váy đen. |
| **f** (giống cái) | **eine** | **-e** | *„Ich trage gern **eine rote** Bluse.“* | Tôi thích mặc một chiếc áo sơ mi nữ đỏ. |
| **n** (giống trung) | **ein** | **-es** | *„Ich trage gern **ein grünes** Kleid.“* | Tôi thích mặc một chiếc đầm xanh lá. |
| **PL** (số nhiều, **không mạo từ**) | *(không có — bảng ghi `X`)* | **-e** | *„Ich trage gern braune Schuhe.“* | Tôi thích đi giày nâu. |

> 🔑 **Vì sao giống trung lại là `-es` còn giống đực là `-en`?** Tính từ **phải mang dấu hiệu giống - cách** mà mạo từ không mang. `einen` (m, Akk) **đã có** `-en` nên tính từ chỉ cần `-en`. `ein` (n, Akk) **không có đuôi** nên tính từ **phải mang `-es`** (giống như `das`). `eine` (f) và số nhiều dùng `-e`.
> 🧠 **Ghi nhớ dạng thơ**: **"en – e – es – e"** *(m – f – n – PL)* — thứ tự **đực, cái, trung, số nhiều**.

#### 3.4. Ba bước tạo cụm `mạo từ + màu + danh từ` (và ví dụ thật)
**Bước 1**: Tìm **giống & số** của danh từ (tra bảng 1.1). **Bước 2**: Chọn **mạo từ bất định** đúng (`einen / eine / ein / không mạo từ`). **Bước 3**: Gắn đuôi `-en / -e / -es / -e` vào **màu**.
| Danh từ | Giống | Màu | Cụm hoàn chỉnh (Akk) | Ví dụ câu (`🔊 de-DE`) & Dịch |
| :--- | :-: | :--- | :--- | :--- |
| der Anzug | m | blau | **einen blauen** Anzug | *„Er trägt einen blauen Anzug.“* — Anh ấy mặc một bộ com lê xanh. |
| der Hut | m | gelb | **einen gelben** Hut | *„Sie kauft einen gelben Hut.“* — Cô ấy mua một chiếc mũ vàng. |
| die Hose | f | grau | **eine graue** Hose | *„Wir suchen eine graue Hose.“* — Chúng tôi tìm một chiếc quần xám. |
| die Jacke | f | braun | **eine braune** Jacke | *„Du probierst eine braune Jacke an.“* — Bạn thử một chiếc áo khoác nâu. |
| das T-Shirt | n | weiß | **ein weißes** T-Shirt | *„Ich nehme ein weißes T-Shirt.“* — Tôi lấy một chiếc áo phông trắng. |
| das Hemd | n | blau | **ein blaues** Hemd | *„Er braucht ein blaues Hemd.“* — Anh ấy cần một chiếc áo sơ mi xanh. |
| die Stiefel | PL | schwarz | schwarze Stiefel | *„Die Kinder brauchen schwarze Stiefel.“* — Bọn trẻ cần đôi bốt đen. |
| die Socken | PL | bunt | bunte Socken | *„Ihr kauft bunte Socken.“* — Các bạn mua những đôi tất sặc sỡ. |

#### 3.5. Màu bất biến - ghép `hell-/dunkel-` - màu phụ (⭐ ví dụ thêm)
* **Bất biến (không đuôi)**: *„Sie trägt eine **rosa** Jacke.“* — Cô ấy mặc một chiếc áo khoác màu hồng nhạt. *„Ich suche ein **lila** Kleid.“* — Tôi tìm một chiếc đầm màu tím hồng.
* **Ghép màu**: *„Ich nehme einen **hellblauen** Pullover.“* — Tôi lấy một chiếc áo len xanh nhạt. *„Sie sucht eine **dunkelgrüne** Jacke.“* — Cô ấy tìm một chiếc áo khoác xanh đậm. *„Er kauft einen **dunkelbraunen** Gürtel.“* — Anh ấy mua một chiếc thắt lưng nâu đậm.
* ⭐ **Cụm cố định ở cửa hàng `in + Màu`** (tên màu viết hoa): *„Haben Sie das T-Shirt in Orange?“* — Ngài có chiếc áo phông này màu cam không? ⚠️ *chỉ để đọc hiểu — không dùng trong bài tập (xem mục 7).*

#### 3.6. Phân tích các câu trên bảng giảng — *"Familie Müller macht viel Sport"* (mỗi câu có `🔊`)
| # | Câu trên bảng (`🔊 de-DE`) | Dịch nghĩa | Cụm có màu — phân tích đuôi |
| :-: | :--- | :--- | :--- |
| 1 | *„Frau Müller spielt Fußball. Sie trägt eine grüne Hose, ein schwarzes T-Shirt und weiße Schuhe.“* | Bà Müller chơi bóng đá. Bà mặc một chiếc quần xanh lá, một áo phông đen và đi giày trắng. | `eine grüne Hose` (f → `-e`) · `ein schwarzes T-Shirt` (n → `-es`) · `weiße Schuhe` (PL → `-e`) |
| 2 | *„Ihr Mann spielt Tennis. Heute hat er einen blauen Trainingsanzug und gelbe Schuhe angezogen.“* | Chồng bà chơi quần vợt. Hôm nay ông ấy đã mặc một bộ đồ thể thao xanh và đi giày vàng. | `einen blauen Trainingsanzug` (m → `-en`) · `gelbe Schuhe` (PL → `-e`) · Perfekt `hat … angezogen` (Bài 9) |
| 3 | *„Ihr Sohn geht joggen. Er zieht eine schwarze Hose und einen roten Pullover an.“* | Con trai họ đi chạy bộ. Cậu ấy mặc một chiếc quần đen và một chiếc áo len đỏ. | `eine schwarze Hose` (f → `-e`) · `einen roten Pullover` (m → `-en`) · động từ tách `zieht … an` |
| 4 | *„Ihre Tochter tanzt. Sie trägt ein blaues Kleid und schwarze Schuhe.“* | Con gái họ nhảy. Cô bé mặc một chiếc đầm xanh và đi giày đen. | `ein blaues Kleid` (n → `-es`) · `schwarze Schuhe` (PL → `-e`) |

> 📘 **Từ mới**: `Sport machen` = tập thể thao · `Fußball spielen` = chơi bóng đá · `Tennis spielen` = chơi quần vợt · `joggen gehen` = đi chạy bộ · `tanzen` = nhảy múa. `ihr` / `ihre` ở đây là **sở hữu** (*của bà ấy*), **không phải** đại từ `ihr` (*các bạn*).

#### 3.7. ⚠️ MƯỜI LỖI THƯỜNG GẶP VỚI MÀU SẮC Ở AKKUSATIV (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Thiếu đuôi tính từ | ✘ *Ich trage einen rot Pullover.* | ✔ *Ich trage einen roten Pullover.* | Tính từ trước danh từ **phải có đuôi**. |
| 2 | Dùng đuôi `-e` cho giống đực | ✘ *Er kauft einen blaue Anzug.* | ✔ *Er kauft einen blauen Anzug.* | m + Akk → **`-en`**. |
| 3 | Dùng đuôi `-en` cho giống cái | ✘ *Sie trägt eine grünen Hose.* | ✔ *Sie trägt eine grüne Hose.* | f → **`-e`**. |
| 4 | Dùng đuôi `-e` cho giống trung | ✘ *Ich nehme ein weiße T-Shirt.* | ✔ *Ich nehme ein weißes T-Shirt.* | n → **`-es`**. |
| 5 | Dùng `ein` cho số nhiều | ✘ *Wir kaufen eine braune Schuhe.* | ✔ *Wir kaufen braune Schuhe.* | Số nhiều **không có** mạo từ bất định. |
| 6 | Dùng `-en` cho số nhiều | ✘ *Sie braucht schwarzen Socken.* | ✔ *Sie braucht schwarze Socken.* | PL → **`-e`**. |
| 7 | Thêm đuôi cho màu bất biến | ✘ *Sie trägt eine rosane Bluse.* | ✔ *Sie trägt eine rosa Bluse.* | `rosa` không biến đổi. |
| 8 | Dùng `einer`/`einem` | ✘ *Ich kaufe einem Rock.* | ✔ *Ich kaufe einen Rock.* | `kaufen` + **Akkusativ** → `einen`. |
| 9 | Sai giống danh từ | ✘ *Ich trage ein schwarzes Hose.* | ✔ *Ich trage eine schwarze Hose.* | `die Hose` là giống cái. |
| 10 | Quên đuôi ở từ ghép màu | ✘ *Er trägt einen dunkelblau Mantel.* | ✔ *Er trägt einen dunkelblauen Mantel.* | Từ ghép `dunkel-` + màu vẫn chia đuôi. |

#### 3.8. Mở rộng ⭐ (chỉ nhận biết, **không có trong bài tập**)
* **Đuôi tính từ ở `Nominativ` sau `ein-`** *(cô giáo gạch bỏ cột này trên bảng)*: m **`-er`**, f **`-e`**, n **`-es`**, PL **`-e`**. *„Ein **roter** Mantel ist teuer.“* — Một chiếc áo măng tô đỏ thì đắt. Chỉ khác Akkusativ ở **giống đực** (`-er` thay vì `-en`).
* **Tính từ sau mạo từ xác định ở `Akkusativ`**: m `den -en` · f `die -e` · n `das -e` · PL `die -en`. *„Ich nehme den roten Pullover.“* — Tôi lấy chiếc áo len đỏ kia. *„Wir kaufen die schwarzen Schuhe.“* — Chúng tôi mua đôi giày đen đó. *(Quy tắc này khác bảng chính; sẽ học kỹ ở A2.)*
* **Tính từ sau `kein-`, `mein-`, `dein-`** (cùng quy tắc với `ein-`): *„Ich habe keinen roten Pullover.“* — Tôi không có chiếc áo len đỏ nào. *„Er trägt meinen grauen Schal.“* — Anh ấy quàng chiếc khăn xám của tôi.

---

### HỌC PHẦN 4: ÔN LẠI `AKKUSATIV` & `DATIV` VỚI TRANG PHỤC (`WEN / WAS?` — `WEM?`)

> 🧭 **Bản đồ phần này**: 4.1 Hai câu hỏi `Wen/Was?` và `Wem?` → 4.2 Bảng mạo từ & đại từ → 4.3 Động từ + `Akkusativ` / + `Dativ` / + cả hai → 4.4 `gefallen - passen - stehen - gehören` → 4.5 `Dativ + Akkusativ` (`schenken, zeigen`) → 4.6 `Dativ` trong cách nói về thời tiết → 4.7 Lưu đồ `V3` → 4.8 Mười lỗi thường gặp.
> 🎨 **Lưu ý của bài**: để người học tập trung vào đúng điểm ngữ pháp, **các ví dụ `Dativ` ở phần này KHÔNG có màu sắc**; màu sắc chỉ xuất hiện cùng `Akkusativ` (Học phần 3).

#### 4.1. Hai câu hỏi phân biệt `Akkusativ` và `Dativ`
| Cách | Câu hỏi | Vai trò | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- | :--- |
| **Akkusativ** (cách 4) | **`Wen?` / `Was?`** — *ai / cái gì?* | **Tân ngữ trực tiếp** (vật bị mặc, mua, tìm…) | *„Ich trage **einen Mantel**.“* — Was trage ich? Einen Mantel. — Tôi mặc một chiếc áo măng tô. |
| **Dativ** (cách 3) | **`Wem?`** — *cho ai? đối với ai?* | **Tân ngữ gián tiếp** (người nhận / người cảm nhận) | *„Der Mantel gefällt **mir**.“* — Wem gefällt der Mantel? Mir. — Chiếc áo măng tô làm tôi hài lòng (tôi thích). |

#### 4.2. Bảng mạo từ & đại từ nhân xưng ở 3 cách (ôn)
##### Mạo từ
| Cách | m | f | n | PL |
| :--- | :--- | :--- | :--- | :--- |
| **Nominativ** (xác định) | der | die | das | die |
| **Akkusativ** (xác định) | **den** | die | das | die |
| **Dativ** (xác định) | **dem** | **der** | **dem** | **den** *(danh từ thêm `-n`)* |
| **Nominativ** (bất định) | ein | eine | ein | — |
| **Akkusativ** (bất định) | **einen** | eine | ein | — |
| **Dativ** (bất định) | **einem** | **einer** | **einem** | — |
| **Dativ với sở hữu** (`mein-`) | **meinem** | **meiner** | **meinem** | **meinen** |

##### Đại từ nhân xưng
| Nominativ | ich | du | er | sie | es | wir | ihr | sie | Sie |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Akkusativ** | mich | dich | ihn | sie | es | uns | euch | sie | Sie |
| **Dativ** | **mir** | **dir** | **ihm** | **ihr** | **ihm** | **uns** | **euch** | **ihnen** | **Ihnen** |

> 🔑 Dativ `ihr` (*cho cô ấy*) **trùng hình thức** với Nominativ `ihr` (*các bạn*); ngữ cảnh quyết định: *„Das Kleid gefällt **ihr**.“* (cô ấy) ≠ *„**Ihr** habt Hunger.“* (các bạn).

#### 4.3. Động từ đi với `Akkusativ` / `Dativ` trong bài
| Nhóm | Động từ | Ví dụ (`🔊 de-DE`) & Dịch *(không có màu)* |
| :--- | :--- | :--- |
| **+ Akkusativ** | `tragen, anziehen, ausziehen, anprobieren, kaufen, suchen, finden, nehmen, brauchen, mitnehmen` | *„Wir kaufen einen Gürtel.“* — Chúng tôi mua một chiếc thắt lưng. · *„Du suchst eine Jacke.“* — Bạn tìm một chiếc áo khoác. |
| **+ Dativ** (người cảm nhận / người sở hữu) | **`gefallen, passen, stehen, gehören, helfen`** | *„Der Pullover gefällt mir.“* · *„Die Stiefel passen ihm.“* · *„Der Hut steht dir.“* · *„Der Schal gehört ihr.“* · *„Ich helfe dir.“* |
| **+ Dativ + Akkusativ** | **`schenken, zeigen, geben, kaufen (cho ai)`** | *„Ich schenke meinem Vater eine Krawatte.“* — Tôi tặng bố tôi một chiếc cà vạt. |

> 🧠 **Mẹo "đảo ngược" quan trọng**: Ở tiếng Việt ta nói *"**tôi** thích cái áo"* (chủ ngữ là người). Với `gefallen / passen / stehen`, tiếng Đức coi **món đồ là chủ ngữ** (`Nominativ`) còn **người là tân ngữ `Dativ`**: *„**Der Pullover** (Nom) gefällt **mir** (Dativ).“* — *"Cái áo len làm tôi hài lòng."* Không nói ~~*Ich gefalle den Pullover*~~.

#### 4.4. `gefallen – passen – stehen – gehören`: dùng khi nào? *(khớp mẫu câu bảng giảng)*
| Động từ | Nghĩa dùng | Ví dụ (`🔊 de-DE`) & Dịch | Câu hỏi thường gặp |
| :--- | :--- | :--- | :--- |
| **gefallen** | *thích* (cảm nhận chủ quan) | *„Das Kleid gefällt mir gut.“* — Tôi thích cái đầm này. · *„Der Hut gefällt mir nicht.“* | *„Wie gefällt Ihnen dieses Kleid?“* |
| **passen** | *vừa kích cỡ / hợp* | *„Die Hose passt mir nicht.“* — Cái quần không vừa với tôi. · *„Der Anzug passt ihm gut.“* | *„Passt Ihnen die Jacke?“* |
| **stehen** | *hợp với dáng người / phong cách* | *„Der Mantel steht dir sehr gut.“* — Chiếc áo măng tô rất hợp với bạn. · *„Das steht mir nicht.“* — Cái này không hợp với tôi. | *„Wie steht mir das?“* |
| **gehören** | *thuộc về, của ai* | *„Der Gürtel gehört meinem Bruder.“* — Chiếc thắt lưng là của anh trai tôi. | *„Wem gehört der Schal?“* — Mir. / Ihr. |
| **`zu + tính từ`** | *quá …* (với `sein`) | *„Das ist mir zu klein.“* · *„Die Schuhe sind uns zu eng.“* | — |

> ❓ **`Wem gehört …?`**: *„Wem gehört der Regenschirm?“* — Cái ô này của ai? — *„Er gehört mir.“* / *„Er gehört meiner Mutter.“*

#### 4.5. `Dativ + Akkusativ`: thứ tự hai tân ngữ
> ### 📐 CÔNG THỨC: &nbsp; **`S + V + (người: Dativ) + (vật: Akkusativ)`** — với **danh từ**: Dativ trước, Akkusativ sau; với **đại từ nhân xưng** đứng trước danh từ.
| Trường hợp | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- |
| Dativ **danh từ** + Akkusativ **danh từ** | *„Ich schenke **meiner Schwester** einen Schal.“* — Tôi tặng chị tôi một chiếc khăn. |
| Dativ **đại từ** + Akkusativ **danh từ** | *„Ich schenke **ihr** einen Schal.“* — Tôi tặng cô ấy một chiếc khăn. *(đại từ đứng trước)* |
| `zeigen` | *„Die Verkäuferin zeigt **mir** einen Mantel.“* — Người bán hàng cho tôi xem một chiếc áo măng tô. |
| `kaufen` (mua cho ai) | *„Er kauft **seiner Mutter** eine Bluse.“* — Anh ấy mua cho mẹ một chiếc áo sơ mi nữ. |
* ⭐ **Cả hai đều là đại từ**: **Akkusativ trước Dativ** — *„Ich schenke **ihn ihm**.“* (nhận biết).

#### 4.6. `Dativ` trong cách nói về thời tiết & mùa (ôn giới từ)
| Mẫu | Ví dụ (`🔊 de-DE`) & Dịch | Giải thích |
| :--- | :--- | :--- |
| **`bei` + Dativ** = *ở chỗ …* | *„**Bei mir** ist es sonnig.“* — Ở chỗ tôi trời nắng. · *„**Bei uns** ist es heiß.“* — Ở chỗ chúng tôi trời nóng. · *„Wie ist das Wetter **bei dir**? Und **bei euch**?“* | `mir, uns, dir, euch` đều là **Dativ** (bảng 4.2). |
| **`im` + mùa** (`in` + `dem`) | *„**Im** Winter schneit es.“* — Vào mùa đông tuyết rơi. · *„**Im** Sommer ist es heiß.“* | `im Winter / im Sommer / im Frühling / im Herbst`. |
| **`in` + địa điểm** (hỏi `Wo?`) | *„In Hà Nội ist es kalt.“* · *„In den Alpen schneit es.“* | `in + Dativ`; tên thành phố không mạo từ. |
| **`bei` + hiện tượng thời tiết** | *„**Bei** Regen nehme ich einen Regenschirm mit.“* — Khi trời mưa tôi mang theo ô. | `bei Regen / Kälte / Hitze / Wind / Nebel` = *"khi trời …"*. |

#### 4.7. Lưu đồ quyết định `Akkusativ` hay `Dativ`? (sơ đồ `V3`)
1. Động từ là **`gefallen / passen / stehen / gehören / helfen`**? → **người = `Dativ`**; món đồ = chủ ngữ (`Nominativ`).
2. Động từ là **`schenken / zeigen / geben`**? → **người = `Dativ`**, **vật = `Akkusativ`**.
3. Động từ là **`tragen / anziehen / kaufen / suchen / nehmen / anprobieren / brauchen`**? → vật = **`Akkusativ`** (chỉ giống đực đổi: `den / einen`).
4. Sau giới từ **`bei, mit, von, aus, nach, zu`** → luôn **`Dativ`**. Sau **`in, an, auf`** hỏi *`Wo?`* (ở đâu) → `Dativ`.

#### 4.8. ⚠️ MƯỜI LỖI THƯỜNG GẶP VỚI `AKKUSATIV` & `DATIV` (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Dùng Akkusativ sau `gefallen` | ✘ *Der Hut gefällt mich.* | ✔ *Der Hut gefällt mir.* | `gefallen` + **Dativ**. |
| 2 | Dùng Dativ sau `tragen` | ✘ *Ich trage dem Mantel.* | ✔ *Ich trage den Mantel.* | `tragen` + **Akkusativ**; m → `den`. |
| 3 | Dùng Akkusativ sau `passen` | ✘ *Die Schuhe passen mich nicht.* | ✔ *Die Schuhe passen mir nicht.* | `passen` + **Dativ**. |
| 4 | Thiếu đuôi Dativ ở sở hữu | ✘ *Ich schenke mein Vater einen Gürtel.* | ✔ *Ich schenke meinem Vater einen Gürtel.* | Người nhận ở **Dativ** (`meinem`). |
| 5 | Dùng `sie` thay `ihr` (Dativ) | ✘ *Das Kleid gefällt sie.* | ✔ *Das Kleid gefällt ihr.* | Dativ của `sie` (số ít) là `ihr`. |
| 6 | Dùng Akkusativ sau `helfen` | ✘ *Ich helfe dich.* | ✔ *Ich helfe dir.* | `helfen` + **Dativ**. |
| 7 | Dùng Akkusativ sau `stehen` | ✘ *Der Pullover steht mich gut.* | ✔ *Der Pullover steht mir gut.* | `stehen` (hợp) + **Dativ**. |
| 8 | Dùng sai mạo từ giống cái | ✘ *Wir kaufen der Hose.* | ✔ *Wir kaufen die Hose.* | `kaufen` + Akkusativ; f → `die`. |
| 9 | Dùng Nominativ thay Dativ | ✘ *Der Mantel gehört ich.* | ✔ *Der Mantel gehört mir.* | `gehören` + **Dativ**. |
| 10 | Thiếu đuôi giống cái ở Akkusativ | ✘ *Ich schenke ihm ein Krawatte.* | ✔ *Ich schenke ihm eine Krawatte.* | `die Krawatte` → `eine`. |

---

### HỌC PHẦN 5: ⭐ ĐẠI TỪ CHỈ ĐỊNH `DIES-` (`DEMONSTRATIVA`) (TRỌNG TÂM THỨ HAI) ⭐

> 🧭 **Bản đồ phần này**: 5.1 `dies-` là gì? → 5.2 Bảng dạng `dies-` *(sơ đồ `V1`)* → 5.3 Hai cách dùng (kèm danh từ / đứng một mình) → 5.4 Kết hợp `welch-` + `dies-` → 5.5 Phân tích hội thoại trên bảng giảng → 5.6 `hier` / `da` → 5.7 `dies-` trong câu đời thường → 5.8 `dies` và `das` → 5.9 Mười lỗi thường gặp → 5.10 Mở rộng ⭐.

#### 5.1. `Dies-` là gì? *(theo bảng giảng)*
* **`Demonstrativa`** (đại từ / từ chỉ định) **`dies-`** = *"này / ấy / đó"*.
* **Dùng để chỉ** **sự vật hoặc đối tượng đang ở trước mắt** (người nói *chỉ tay vào*).
* **Hoạt động giống đại từ nhân xưng ngôi thứ 3** (`er / sie / es / sie`): **thay đổi theo giống, số lượng và cách** của danh từ được nói đến.
* **Có thể đi kèm danh từ** (*dieser Rock* — chiếc chân váy này) **hoặc đứng độc lập** (*diesen* — cái này, khi danh từ đã rõ).

#### 5.2. Bảng dạng `dies-` ở `Nominativ` và `Akkusativ` *(khớp bảng giảng; sơ đồ `V1`)*
| Giống | `Nominativ` (Cách 1) | `Akkusativ` (Cách 4) |
| :--- | :--- | :--- |
| **m** (giống đực) | der → **dieser** | den → **diesen** |
| **f** (giống cái) | die → **diese** | die → **diese** |
| **n** (giống trung) | das → **dieses** | das → **dieses** |
| **PL** (số nhiều) | die → **diese** | die → **diese** |

> 🔑 **Chỉ giống ĐỰC mới đổi giữa hai cách** (`dieser` ↔ `diesen`) — **giống hệt `welch-` ở Bài 10** (`welcher` ↔ `welchen`). Hai từ này (và `jed-`) dùng **cùng một bộ đuôi `-er / -en / -e / -es / -e`**.
> 🧠 **Cách ghi nhớ**: lấy mạo từ xác định `der / den / die / das` rồi đổi thành **`dieser / diesen / diese / dieses`**: đuôi mạo từ là đuôi `dies-`.
> ⭐ **Dạng `Dativ` (chỉ nhận biết)**: m **`diesem`** · f **`dieser`** · n **`diesem`** · PL **`diesen`**. *„Diesem Mantel gefällt …“* hiếm gặp; thường gặp trong cụm *„mit diesem Hut“*.

#### 5.3. Hai cách dùng `dies-` *(khớp ví dụ trên bảng giảng)*
| Cách dùng | Công thức | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **Kèm danh từ** | `dies- + Danh từ` | *„Ich kaufe **diesen Rock**.“* — Tôi mua chiếc chân váy này. · *„Ich möchte **diese Jacke**.“* — Tôi muốn chiếc áo khoác này. |
| **Đứng một mình** (danh từ đã rõ) | `dies-` | *„Ich kaufe **diesen**.“* — Tôi mua cái này. *(= diesen Rock)* · *„Ich möchte **diese**.“* — Tôi muốn cái này. *(= diese Jacke)* |
| **Câu hỏi `welch-` ↔ trả lời `dies-`** | `Welch- …? — Dies- (hier).` | *„Welche Jacke möchten Sie? — **Diese** hier.“* — Ngài muốn chiếc áo khoác nào? — Chiếc này đây. |

> 🔑 **Khi đứng một mình**, `dies-` **vẫn phải đúng giống - số - cách của danh từ đã nhắc**: nếu nói về `der Rock` (Akkusativ) → **`diesen`**; về `die Jacke` → **`diese`**; về `das Kleid` → **`dieses`**; về `die Schuhe` → **`diese`**. Vì vậy ~~*Ich kaufe diese.*~~ chỉ đúng khi nói về giống cái hoặc số nhiều, **không** đúng khi nói về `der Rock`.

#### 5.4. Kết hợp `welch-` + `dies-` (hỏi - đáp khi chọn đồ) *(sơ đồ `V1`)*
| Hỏi (`🔊 de-DE`) | Trả lời (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- |
| *„**Welchen** Gürtel nimmst du?“* *(m, Akk)* | *„**Diesen** hier.“* | Bạn lấy chiếc thắt lưng nào? — Chiếc này đây. |
| *„**Welche** Bluse gefällt Ihnen?“* *(f, Nom)* | *„**Diese** da.“* | Chiếc áo sơ mi nữ nào làm ngài thích? — Chiếc kia. |
| *„**Welches** Hemd probierst du an?“* *(n, Akk)* | *„**Dieses** hier.“* | Bạn thử chiếc áo sơ mi nam nào? — Chiếc này đây. |
| *„**Welche** Stiefel passen dir?“* *(PL, Nom)* | *„**Diese** passen mir.“* | Đôi bốt nào vừa với bạn? — Đôi này vừa với tôi. |

#### 5.5. Phân tích hai hội thoại trên bảng giảng *(mỗi câu có `🔊`)*
##### Hội thoại 1 — chọn áo khoác mùa đông *(`der Wintermantel`)*
| # | Câu (`🔊 de-DE`) | Dịch nghĩa | Ghi chú ngữ pháp |
| :-: | :--- | :--- | :--- |
| 1 | *„**Welchen** Wintermantel findest du **schöner**? **Diesen** oder **diesen**?“* | Bạn thấy chiếc áo khoác mùa đông nào đẹp hơn? Chiếc này hay chiếc này? | `der Wintermantel` (m) làm tân ngữ của `finden` → Akkusativ → `welchen / diesen`; **`schöner`** là Komparativ (Bài 10). *Hai lần `diesen` chỉ hai chiếc khác nhau (người nói chỉ tay).* |
| 2 | *„Ich finde **diesen** hier **schöner**. Aber **welcher** ist **wärmer**?“* | Tôi thấy chiếc này đây đẹp hơn. Nhưng chiếc nào ấm hơn? | `welcher` là **Nominativ** (chủ ngữ của `ist`); `wärmer` = Komparativ của `warm` (thêm Umlaut). |
| 3 | *„**Beide** sind warm. Ich nehme **diesen** hier.“* | Cả hai đều ấm. Tôi lấy chiếc này đây. | `beide` = cả hai (số nhiều); `nehmen` + Akkusativ → `diesen`. |

##### Hội thoại 2 — chọn đôi bốt theo cỡ giày
| # | Câu (`🔊 de-DE`) | Dịch nghĩa | Ghi chú ngữ pháp |
| :-: | :--- | :--- | :--- |
| 1 | *„**Welche** Stiefel sind Größe neununddreißig?“* | Những đôi bốt nào cỡ ba mươi chín? | `die Stiefel` (PL, Nominativ) → `welche`. `Größe 39` đọc bằng chữ khi dùng `🔊`. |
| 2 | *„**Diese** hier.“* | Những đôi này đây. | `diese` đứng một mình, số nhiều. |
| 3 | *„Und **diese** hier nicht?“* | Còn những đôi này đây thì không phải ạ? | Hỏi lại để xác nhận. |
| 4 | *„Nein, **diese** sind Größe achtunddreißig.“* | Không, những đôi này là cỡ ba mươi tám. | `diese` số nhiều Nominativ. |

#### 5.6. `hier` và `da` — chỉ gần, chỉ xa
* **`dieser hier`** = *cái này đây* (gần người nói) · **`dieser da`** = *cái kia* (xa hơn). *„Der Hut hier gefällt mir, aber **diesen da** nehme ich nicht.“* → câu mẫu đơn giản hơn: *„**Diesen hier** nehme ich, **diesen da** nicht.“* — Tôi lấy cái này đây, cái kia thì không.
* **Vị trí**: `hier / da` đứng **sau** cụm `dies- (+ danh từ)`: *„Ich nehme diesen Pullover **hier**.“* (không nói ~~*Ich nehme hier diesen Pullover*~~ khi muốn chỉ rõ vật).

#### 5.7. `Dies-` trong các câu đời thường
| Tình huống | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- |
| **Nhận xét đồ** (`Nominativ` + Dativ) | *„**Dieser** Pullover gefällt mir.“* — Chiếc áo len này tôi thích. · *„**Diese** Hose passt mir nicht.“* — Chiếc quần này không vừa với tôi. · *„**Dieses** Kleid steht dir gut.“* — Chiếc đầm này hợp với bạn. · *„**Diese** Schuhe sind mir zu eng.“* — Đôi giày này chật quá đối với tôi. |
| **Chọn mua** (`Akkusativ`) | *„Ich nehme **diesen** Schal.“* — Tôi lấy chiếc khăn này. · *„Wir kaufen **diese** Mütze.“* — Chúng tôi mua chiếc mũ len này. · *„Er probiert **dieses** Hemd an.“* — Anh ấy thử chiếc áo sơ mi này. |
| **Hỏi giá** | *„Wie viel kostet **dieser** Mantel?“* — Chiếc áo măng tô này giá bao nhiêu? · *„Was kosten **diese** Handschuhe?“* — Đôi găng tay này giá bao nhiêu? |
| **Chỉ thời gian** (`Akkusativ` — trạng ngữ) | *„**Diese Woche** ist es kalt.“* — Tuần này trời lạnh. · *„**Dieses Jahr** schneit es viel.“* — Năm nay tuyết rơi nhiều. · *„**Diesen Winter** brauche ich einen neuen Mantel.“* — Mùa đông này tôi cần một chiếc áo măng tô mới. · *„**Dieses Wochenende** regnet es.“* — Cuối tuần này trời mưa. |

> 📘 **Từ chỉ thời gian với `dies-` (Akkusativ)**: `diese Woche` (tuần này) · `diesen Monat` (tháng này) · `dieses Jahr` (năm nay) · `dieses Wochenende` (cuối tuần này) · `diesen Sommer / Winter / Herbst` · `diesen Frühling` (mùa … này). Nói *„Diesen Morgen“* hiếm; thường nói **`heute Morgen`**.

#### 5.8. `Dies-` và `das` — phân biệt khi chỉ vật
* **`Das ist ein Mantel.`** — Đây là một chiếc áo măng tô. *(`das` chung chung, nói thường ngày)* · **`Was ist das?`** — Đây là cái gì?
* **`Dieser Mantel ist teuer.`** — **Chiếc áo măng tô này** đắt. *(`dies-` **chỉ một vật cụ thể**, phải hợp giống)*
* ⭐ **`Dies ist …`** *(trang trọng, hiếm)* = `Das ist …`.

#### 5.9. ⚠️ MƯỜI LỖI THƯỜNG GẶP VỚI `DIES-` (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Dùng `dieser` cho tân ngữ giống đực | ✘ *Ich kaufe dieser Rock.* | ✔ *Ich kaufe diesen Rock.* | m + Akk → `diesen`. |
| 2 | Dùng `diesen` cho chủ ngữ giống đực | ✘ *Diesen Mantel ist warm.* | ✔ *Dieser Mantel ist warm.* | Chủ ngữ → Nominativ → `dieser`. |
| 3 | Dùng `dieser` cho giống cái ở Akk | ✘ *Ich nehme dieser Hose.* | ✔ *Ich nehme diese Hose.* | f → `diese` ở cả hai cách. |
| 4 | Dùng `diese` cho giống trung | ✘ *Diese Hemd gefällt mir.* | ✔ *Dieses Hemd gefällt mir.* | n → `dieses`. |
| 5 | Dùng `dieses` cho số nhiều | ✘ *Dieses Schuhe sind klein.* | ✔ *Diese Schuhe sind klein.* | PL → `diese`. |
| 6 | Quên đổi khi đứng một mình | ✘ *Ich kaufe diese.* (nói về `der Rock`) | ✔ *Ich kaufe diesen.* | Theo giống của danh từ đã nhắc (`Rock` m). |
| 7 | Đặt `hier` sai chỗ | ✘ *Ich nehme hier diesen Pullover.* | ✔ *Ich nehme diesen Pullover hier.* | `hier` đứng sau cụm `dies- + Nomen`. |
| 8 | Nhầm `dies` với `das` | ✘ *Dieses ist ein Mantel.* | ✔ *Das ist ein Mantel.* | Giới thiệu chung → `das`. |
| 9 | Dùng đuôi giống đực `-es` | ✘ *Dieses Gürtel ist neu.* | ✔ *Dieser Gürtel ist neu.* | `der Gürtel` → Nom `dieser`. |
| 10 | Bỏ đuôi hoàn toàn | ✘ *Ich kaufe dies Hose.* | ✔ *Ich kaufe diese Hose.* | `dies-` luôn có đuôi (trừ `dies ist` trang trọng). |

#### 5.10. Mở rộng ⭐ (chỉ nhận biết, **không có trong bài tập**)
* **`jen-`** = *"kia, ấy"* (xa hơn, văn viết): *„dieser Mantel hier, jener dort“*. Dùng cùng bộ đuôi `dies-`.
* **`diese(r/s) … hier`** có thể rút thành **`der / die / das hier`** khi nói: *„**Den** hier nehme ich.“* — Cái này đây tôi lấy. *(`den` ở đây là đại từ chỉ định nhấn mạnh.)*

---

### HỌC PHẦN 6: ⭐ THỜI TIẾT (`DAS WETTER`) (TRỌNG TÂM THỨ BA) ⭐

> 🧭 **Bản đồ phần này**: 6.1 Từ vựng thời tiết *(bảng giảng)* → 6.2 Bốn mẫu câu → 6.3 Hỏi - đáp về thời tiết → 6.4 Nhiệt độ → 6.5 Bốn mùa & tháng → 6.6 Thời tiết & trang phục → 6.7 So sánh thời tiết (ôn Bài 10) → 6.8 Thời tiết ở quá khứ (ôn Bài 9) → 6.9 Bản tin thời tiết → 6.10 Lỗi thường gặp.

#### 6.1. Từ vựng thời tiết (khớp bảng giảng; sơ đồ `V5`)
| Danh từ | Nghĩa | Động từ / Tính từ | Câu hoàn chỉnh (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- | :--- | :--- |
| **der Regen** | mưa | **regnen** *(v)* | *„Es regnet.“* | Trời mưa. |
| **der Schnee** | tuyết | **schneien** *(v)* | *„Es schneit.“* | Tuyết rơi. |
| **der Wind** | gió | **windig** *(adj)* | *„Es ist windig.“* | Trời có gió. |
| **der Nebel** | sương mù | **neblig** *(adj)* | *„Es ist neblig.“* | Trời có sương mù. |
| **die Sonne** | mặt trời | **sonnig** *(adj)* | *„Es ist sonnig.“* | Trời nắng. |
| **die Wolke** *(Pl: die Wolken)* | mây | **bewölkt** *(adj)* | *„Es ist bewölkt.“* | Trời nhiều mây. |
| **die Kälte** | khí lạnh | **kalt** *(adj)* | *„Es ist kalt.“* | Trời lạnh. |
| **die Hitze** | khí nóng | **heiß** *(adj)* | *„Es ist heiß.“* | Trời nóng. |

> ⚠️ **Phân biệt danh từ - động từ - tính từ**: `der Regen` (danh từ) → `regnen` (động từ: *Es regnet*). `die Kälte` (danh từ) → `kalt` (tính từ: *Es ist kalt*). **Không** nói ~~*Es ist Kälte*~~, ~~*Es ist Regen*~~.

##### Mở rộng ⭐: 12 từ thời tiết bổ sung (mỗi từ có `🔊`)
| Từ | Nghĩa | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **das Gewitter** / **gewittern** | cơn dông / có dông | *„Heute Nacht gewittert es.“* — Đêm nay có dông. · *„Am Abend gibt es ein Gewitter.“* |
| **der Sturm** / **stürmisch** | bão / có bão | *„Es ist stürmisch.“* — Trời giông bão. |
| **wolkig** | nhiều mây (đồng nghĩa với `bewölkt`) | *„Es ist wolkig.“* |
| **die Sonne scheint** | trời nắng (mặt trời chiếu) | *„Heute scheint die Sonne.“* — Hôm nay mặt trời chiếu sáng. |
| **warm / kühl** | ấm / mát | *„Es ist warm.“* · *„Im Herbst ist es kühl.“* — Mùa thu trời mát. |
| **schwül** | oi bức | *„Im Sommer ist es oft schwül.“* — Mùa hè thường oi bức. |
| **trocken / nass** | khô / ướt | *„Der Boden ist nass.“* — Mặt đất ướt. |
| **regnerisch** | nhiều mưa | *„Der Herbst ist regnerisch.“* — Mùa thu nhiều mưa. |
| **schön / schlecht** | đẹp / xấu (thời tiết) | *„Das Wetter ist schön.“* · *„Das Wetter ist schlecht.“* |
| **die Temperatur** | nhiệt độ | *„Die Temperatur ist heute hoch.“* |
| **das Grad** | độ | *„Es sind zwanzig Grad.“* |
| **der Wetterbericht** | bản tin thời tiết | *„Der Wetterbericht sagt Regen.“* |

#### 6.2. Bốn mẫu câu nói về thời tiết (chủ ngữ giả `es`)
| Mẫu | Công thức | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **① Es + động từ** | `Es regnet / schneit / gewittert.` | *„Es regnet.“* — Trời mưa. · *„Es schneit in den Alpen.“* — Tuyết rơi ở dãy Alps. |
| **② Es ist + tính từ** | `Es ist sonnig / windig / neblig / bewölkt / kalt / heiß / warm.` | *„Es ist heute neblig.“* — Hôm nay có sương mù. · *„Es ist sehr heiß.“* |
| **③ Die Sonne scheint** | `Die Sonne scheint.` | *„Morgen scheint die Sonne.“* — Ngày mai trời nắng. |
| **④ Es gibt + Akkusativ** | `Es gibt Regen / Nebel / ein Gewitter.` | *„Heute gibt es Nebel.“* — Hôm nay có sương mù. · *„Es gibt viel Wind.“* — Có nhiều gió. |

> 🔑 `es` ở đây **không có nghĩa** (chỉ để đủ chủ ngữ) nên **không dịch**. Có thể đặt trạng từ ở đầu câu: *„**Heute** regnet es.“* (động từ vẫn ở vị trí ②).

#### 6.3. Hỏi - đáp về thời tiết *(khớp bảng giảng)*
| Câu hỏi (`🔊 de-DE`) | Dịch | Trả lời mẫu (`🔊 de-DE`) |
| :--- | :--- | :--- |
| *„Wie ist das Wetter in Vietnam?“* | Thời tiết ở Việt Nam thế nào? | *„In Vietnam ist es heiß.“* |
| *„Wie ist das Wetter in Hải Phòng?“* | Thời tiết ở Hải Phòng thế nào? | *„In Hải Phòng ist es windig.“* |
| *„Wie ist das Wetter **bei dir**?“* | Thời tiết chỗ bạn thế nào? | *„**Bei mir** ist es sonnig.“* — Chỗ tôi trời nắng. |
| *„Wie ist das Wetter **bei euch**?“* | Thời tiết chỗ các bạn thế nào? | *„**Bei uns** ist es heiß.“* — Chỗ chúng tôi trời nóng. |
| *„Wie ist das Wetter heute / morgen?“* | Hôm nay / ngày mai thời tiết thế nào? | *„Heute ist es bewölkt, morgen regnet es.“* |
| *„Wie warm / kalt ist es?“* · *„Wie viel Grad sind es?“* | Trời ấm / lạnh bao nhiêu? · Bao nhiêu độ? | *„Es sind fünfzehn Grad.“* |

> 📘 **`VN` = Vietnam, `HP` = Hải Phòng** trong ví dụ của bảng giảng. Khi trả lời, **không** thêm `ist es` hai lần: *„Bei mir **ist es** sonnig.“* (đúng).

#### 6.4. Nhiệt độ & cách đọc (`Grad`)
| Viết | Cách đọc (`🔊 de-DE`) | Câu ví dụ |
| :--- | :--- | :--- |
| 0 °C | **null Grad** | *„Es sind null Grad.“* |
| 15 °C | **fünfzehn Grad** | *„Es sind fünfzehn Grad.“* |
| 28 °C | **achtundzwanzig Grad** | *„In Hà Nội sind es achtundzwanzig Grad.“* |
| 36 °C | **sechsunddreißig Grad** | *„Es sind sechsunddreißig Grad — sehr heiß!“* |
| −5 °C | **minus fünf Grad** | *„Es sind minus fünf Grad.“* |

> 🔑 **`das Grad` không đổi số nhiều sau số đếm** (`zwanzig Grad`, không `Grade`). Dấu `°C` **không đọc**; số âm đọc **`minus + số`**. Dùng hàm đọc số 0–99 của Bài 10 (có thêm `null`).

#### 6.5. Bốn mùa & tháng *(`die Jahreszeiten`)*
| Mùa (tất cả là `der`) | Tháng ở Đức (nửa bắc) | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **der Frühling** | März, April, Mai | *„Im Frühling ist es warm.“* — Vào mùa xuân trời ấm. |
| **der Sommer** | Juni, Juli, August | *„Im Sommer ist es heiß.“* |
| **der Herbst** | September, Oktober, November | *„Im Herbst regnet es oft.“* |
| **der Winter** | Dezember, Januar, Februar | *„Im Winter schneit es.“* |

* **`im` + tháng / mùa**: *„**Im** Januar ist es kalt.“* — Vào tháng Giêng trời lạnh.
* ⭐ **Việt Nam**: `die Regenzeit` (mùa mưa) · `die Trockenzeit` (mùa khô): *„In Vietnam gibt es die Regenzeit und die Trockenzeit.“* — Ở Việt Nam có mùa mưa và mùa khô.

#### 6.5.1. Thời tiết & thời gian: các trạng ngữ thường gặp
`heute` (hôm nay) · `morgen` (ngày mai) · `gestern` (hôm qua) · `diese Woche` (tuần này) · `am Wochenende` (vào cuối tuần) · `am Morgen / am Nachmittag / am Abend` (sáng / chiều / tối) · `in der Nacht` (ban đêm) · `oft / manchmal / selten / nie` (thường / thỉnh thoảng / hiếm / không bao giờ). *„Am Nachmittag scheint die Sonne.“* — Buổi chiều trời nắng.

#### 6.6. Thời tiết & trang phục — **`Bei + thời tiết + mặc gì`** *(ôn Akkusativ; ví dụ không dùng màu vì có `bei` = Dativ)*
| Thời tiết | Ví dụ (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- |
| **bei Kälte** | *„Bei Kälte trage ich einen Mantel, einen Schal und Handschuhe.“* | Khi trời lạnh tôi mặc áo măng tô, quàng khăn và đeo găng tay. |
| **bei Hitze** | *„Bei Hitze trage ich ein T-Shirt und kurze Hosen.“* | Khi trời nóng tôi mặc áo phông và quần short. |
| **bei Regen** | *„Bei Regen nehme ich einen Regenschirm mit.“* | Khi trời mưa tôi mang theo ô. |
| **bei Schnee** | *„Bei Schnee brauche ich Stiefel.“* | Khi có tuyết tôi cần bốt. |
| **bei Wind** | *„Bei Wind ziehe ich eine Jacke an.“* | Khi có gió tôi mặc áo khoác vào. |
| **bei Sonne** | *„Bei Sonne trage ich eine Sonnenbrille und einen Hut.“* | Khi trời nắng tôi đeo kính râm và đội mũ. |

#### 6.7. So sánh thời tiết (ôn `Komparativ` & `Superlativ` Bài 10)
* *„Im Sommer ist es **wärmer als** im Frühling.“* — Mùa hè ấm hơn mùa xuân. · *„In Hà Nội ist es im Winter **kälter als** in Sài Gòn.“* · *„Im Januar ist es **am kältesten**.“* — Tháng Giêng lạnh nhất. · *„In Đà Lạt ist es **kühler als** in Sài Gòn.“*
* `warm → wärmer → am wärmsten` · `kalt → kälter → am kältesten` · `heiß → heißer → am heißesten` · `gut → besser → am besten` (*Das Wetter ist heute **besser** als gestern.*)

#### 6.8. Thời tiết ở quá khứ (ôn `Perfekt` Bài 9)
* Động từ thời tiết dùng **`haben`**: *„Gestern **hat** es **geregnet**.“* — Hôm qua trời đã mưa. · *„Letzte Woche **hat** es **geschneit**.“* — Tuần trước tuyết đã rơi. · *„Es **hat** den ganzen Tag **gewittert**.“* — Cả ngày đã có dông.
* Với `sein` (Präteritum): *„Gestern **war** es neblig.“* — Hôm qua trời đã có sương mù. · *„Das Wetter **war** schlecht.“*
* Nhắc lại `anziehen` ở Perfekt: *„Ich **habe** einen Mantel **angezogen**.“* — Tôi đã mặc áo măng tô vào.

#### 6.9. Bản tin thời tiết (`der Wetterbericht`) — đoạn nghe - đọc mẫu *(sơ đồ `V5`)*
* **Đoạn bản tin (`🔊 de-DE`)**:
  > *„Guten Morgen! Hier ist der Wetterbericht für heute. In Berlin ist es bewölkt, es sind acht Grad. In Hamburg regnet es, es ist windig, und es sind nur sieben Grad. In München scheint die Sonne, es sind zwölf Grad. In Wien ist es neblig, es sind vier Grad. Morgen wird es überall kälter.“*
* **Dịch nghĩa**:
  > *„Chào buổi sáng! Đây là bản tin thời tiết hôm nay. Ở Berlin trời nhiều mây, nhiệt độ tám độ. Ở Hamburg trời mưa, có gió và chỉ bảy độ. Ở München trời nắng, mười hai độ. Ở Wien có sương mù, bốn độ. Ngày mai khắp nơi sẽ lạnh hơn.“*
* **Từ mới**: `überall` = khắp nơi · `wird es kälter` = trời sẽ lạnh hơn (⭐ `werden`: *es wird* = nó trở nên).

#### 6.10. ⚠️ LỖI THƯỜNG GẶP KHI NÓI VỀ THỜI TIẾT (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Thêm `ist` trước động từ | ✘ *Es ist regnet.* | ✔ *Es regnet.* | `regnen` là động từ; không cần `sein`. |
| 2 | Dùng danh từ thay tính từ | ✘ *Es ist Kälte.* | ✔ *Es ist kalt.* | Sau `ist` dùng **tính từ**. |
| 3 | Sai mạo từ `Wetter` | ✘ *Die Wetter ist schön.* | ✔ *Das Wetter ist schön.* | `das Wetter` (giống trung, chỉ số ít). |
| 4 | Dùng `haben` với tính từ | ✘ *Es hat sonnig.* | ✔ *Es ist sonnig.* | Tính từ đi với `sein`. |
| 5 | Dùng Nominativ sau `bei` | ✘ *Bei ich ist es heiß.* | ✔ *Bei mir ist es heiß.* | `bei` + **Dativ** → `mir`. |
| 6 | Sai đại từ Dativ | ✘ *Wie ist das Wetter bei du?* | ✔ *Wie ist das Wetter bei dir?* | `du` → Dativ `dir`. |
| 7 | Thêm số nhiều cho `Grad` | ✘ *Es sind zwanzig Grade.* | ✔ *Es sind zwanzig Grad.* | Sau số đếm `Grad` giữ nguyên. |
| 8 | Dùng danh từ thay tính từ (nắng) | ✘ *Es ist Sonne.* | ✔ *Es ist sonnig.* | `die Sonne` → `sonnig`. |
| 9 | Quên đảo ngữ khi đặt trạng từ đầu câu | ✘ *Heute es regnet.* | ✔ *Heute regnet es.* | Động từ ở **vị trí ②**. |
| 10 | Dùng `sein` ở Perfekt thời tiết | ✘ *Gestern ist es geregnet.* | ✔ *Gestern hat es geregnet.* | Động từ thời tiết dùng **`haben`**. |

---

### HỌC PHẦN 7: MUA QUẦN ÁO — HỘI THOẠI Ở CỬA HÀNG (`EINKAUFEN IM KLEIDUNGSGESCHÄFT`)

#### 7.1. Người bán nói gì? Khách nói gì? *(khớp 8 cặp hỏi - đáp trên bảng giảng; sơ đồ `V6`)*
| # | **Verkäufer** (người bán) (`🔊 de-DE`) | Dịch | **Kunde** (khách) (`🔊 de-DE`) | Dịch |
| :-: | :--- | :--- | :--- | :--- |
| 1 | *„Guten Tag, kann ich Ihnen helfen?“* | Xin chào, tôi có thể giúp gì cho ngài ạ? | *„Ich suche ein Kleid.“* · *„Wo finde ich Kleider?“* | Tôi tìm một chiếc đầm. · Tôi tìm đầm ở đâu? |
| 2 | *„Welche Größe denn?“* | Ngài mặc cỡ nào ạ? | *„Vierzig.“* | Cỡ bốn mươi. |
| 3 | *„Die Größe haben wir leider nicht.“* | Tiếc là chúng tôi không có cỡ đó. | *„Haben Sie das Kleid in Größe vierzig?“* | Ngài có chiếc đầm này cỡ bốn mươi không? |
| 4 | *„Wollen Sie das anprobieren?“* | Ngài có muốn thử cái này không? | *„Kann ich das anprobieren?“* | Tôi có thể thử cái này không? |
| 5 | *„Die Umkleidekabine ist hier rechts.“* | Phòng thử đồ ở bên phải đây. | *„Wo ist die Umkleidekabine?“* | Phòng thử đồ ở đâu? |
| 6 | *„Wie gefällt Ihnen dieses Kleid?“* | Ngài thấy chiếc đầm này thế nào (có thích không)? | *„Das gefällt mir gut.“* · *„Das gefällt mir nicht.“* | Tôi thích cái này. · Tôi không thích cái này. |
| 7 | *„Das Kleid passt, oder?“* | Chiếc đầm vừa, đúng không ạ? | *„Das Kleid passt nicht.“* · *„Das ist mir zu klein.“* · *„Das ist mir zu groß.“* | Chiếc đầm không vừa. · Cái này nhỏ / chật quá đối với tôi. · Cái này rộng quá đối với tôi. |
| 8 | *„Wie steht Ihnen das?“* *(hỏi nhận xét)* | Cái này trông hợp với ngài chứ? | *„Das steht mir nicht.“* · *„Ja, sehr gut. Das nehme ich.“* | Cái này không hợp với tôi. · Vâng, rất hợp. Tôi lấy cái này. |

> ⚠️ **Hai câu trên bảng giảng có cả màu và Dativ** (*„Grün steht Ihnen sehr gut / nicht so gut.“*; *„Haben Sie das Kleid in Grün?“* — cụm cố định `in + Màu`). **Chỉ để đọc hiểu**: màu sắc **không** được ghép với Dativ trong bài tập (xem Quy tắc R3). Nghĩa: *„Màu xanh lá rất hợp / không hợp lắm với ngài.“* · *„Ngài có chiếc đầm này màu xanh lá không?“*

> 🔑 **Điểm ngữ pháp trong 8 cặp**: `Ihnen` / `mir` là **Dativ** (`helfen, gefallen, passen, stehen`); `Kleid / Hose / das` là **Akkusativ** với `suchen / anprobieren / nehmen`; **`wollen Sie …?`** = *ngài có muốn …?* (từ `wollen`, sẽ học kỹ ở bài sau — chỉ cần hiểu mẫu câu).

#### 7.2. Các mẫu câu nói về kích cỡ - vừa vặn - giá (⭐ mở rộng)
| Tình huống | Mẫu câu (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- |
| **Hỏi cỡ** | *„Welche Größe haben Sie?“* · *„Ich trage Größe achtundvierzig.“* | Ngài mặc cỡ nào? · Tôi mặc cỡ bốn mươi tám. |
| **Hỏi có cỡ khác không** | *„Haben Sie das in Größe zweiundvierzig?“* | Ngài có cái này cỡ bốn mươi hai không? |
| **Hỏi vừa không** | *„Passt Ihnen die Hose?“* · *„Passt dir der Pullover?“* | Quần có vừa với ngài không? · Áo len có vừa với bạn không? |
| **Nói không vừa** | *„Die Hose ist mir zu lang.“* · *„Die Schuhe sind mir zu eng.“* | Quần dài quá đối với tôi. · Giày chật quá đối với tôi. |
| **Hỏi giá** | *„Wie viel kostet dieser Mantel?“* · *„Was kosten diese Handschuhe?“* | Chiếc áo măng tô này giá bao nhiêu? · Đôi găng tay này giá bao nhiêu? |
| **Quyết định mua** | *„Den nehme ich.“* · *„Ich nehme diesen.“* | Cái này tôi lấy. |
| **Từ chối** | *„Danke, ich schaue nur.“* | Cảm ơn, tôi chỉ xem thôi. |

#### 7.3. Bảng giá quần áo mẫu (dùng để luyện đọc giá — số liệu nguồn ở Phụ lục A)
| Món | Giá | Cách đọc (`🔊 de-DE`) | Món | Giá | Cách đọc |
| :--- | :-: | :--- | :--- | :-: | :--- |
| der Mantel | 90 € | neunzig Euro | das Hemd | 35 € | fünfunddreißig Euro |
| die Jacke | 65 € | fünfundsechzig Euro | der Rock | 32 € | zweiunddreißig Euro |
| der Pullover | 39 € | neununddreißig Euro | der Gürtel | 25 € | fünfundzwanzig Euro |
| die Hose | 49 € | neunundvierzig Euro | der Schal | 19 € | neunzehn Euro |
| das Kleid | 59 € | neunundfünfzig Euro | das T-Shirt | 15 € | fünfzehn Euro |

#### 7.4. Hội thoại trên bảng giảng — thứ tự đúng *(bài sắp xếp trên bảng)* ⚠️ chỉ để đọc hiểu
> ⚠️ Hội thoại này **có cả màu sắc và Dativ** (`Die blaue Jacke gefällt mir nicht`). Hiển thị ở lý thuyết với nhãn *"chỉ để đọc hiểu"*; **không đưa vào bài tập**.
| # | Người nói | Câu (`🔊 de-DE`) | Dịch |
| :-: | :-: | :--- | :--- |
| 1 | A | *„Guten Tag! Kann ich Ihnen helfen?“* | Xin chào! Tôi có thể giúp gì cho ngài? |
| 2 | B | *„Ja, ich suche eine Jacke.“* | Vâng, tôi tìm một chiếc áo khoác. |
| 3 | A | *„Welche Größe haben Sie denn?“* | Ngài mặc cỡ nào ạ? |
| 4 | B | *„Sechsunddreißig oder achtunddreißig.“* | Ba mươi sáu hoặc ba mươi tám. |
| 5 | A | *„Wir haben hier eine braune Jacke in achtunddreißig und eine blaue in Größe sechsunddreißig.“* | Ở đây chúng tôi có một chiếc áo khoác nâu cỡ ba mươi tám và một chiếc xanh cỡ ba mươi sáu. |
| 6 | B | *„Die blaue Jacke gefällt mir nicht. Ich probiere die braune an. Wo ist die Umkleidekabine?“* | Chiếc áo khoác xanh tôi không thích. Tôi thử chiếc nâu. Phòng thử đồ ở đâu? |
| 7 | A | *„Hinten rechts. Und passt Ihnen die Jacke?“* | Ở phía sau bên phải. Và chiếc áo khoác có vừa với ngài không? |
| 8 | B | *„Nein, die Ärmel sind zu lang. Sie steht mir nicht.“* | Không, tay áo dài quá. Nó không hợp với tôi. |

> 📘 **Từ mới**: `der Ärmel` *(Pl: die Ärmel)* = tay áo · `hinten rechts` = phía sau bên phải · `denn` (trong câu hỏi) = *"vậy"* (làm câu hỏi thân thiện hơn).

#### 7.5. Bốn hội thoại mới (mỗi dòng có `🔊` và dịch) — **màu chỉ nằm ở dòng Akkusativ, dòng Dativ không có màu**
##### Hội thoại 1 — Mua áo len (không có màu)
* *Verkäuferin*: *„Guten Tag! Suchen Sie etwas Bestimmtes?“* — Xin chào! Ngài tìm món nào cụ thể không ạ?
* *Kunde*: *„Ja, ich suche einen Pullover.“* — Có, tôi tìm một chiếc áo len.
* *Verkäuferin*: *„Welche Größe haben Sie?“* — Ngài mặc cỡ nào?
* *Kunde*: *„Ich trage Größe achtundvierzig.“* — Tôi mặc cỡ bốn mươi tám.
* *Verkäuferin*: *„Diesen hier haben wir in achtundvierzig. Wollen Sie ihn anprobieren?“* — Chiếc này đây chúng tôi có cỡ bốn mươi tám. Ngài có muốn thử không?
* *Kunde*: *„Ja, gern. Wo ist die Umkleidekabine?“* — Vâng, rất sẵn lòng. Phòng thử đồ ở đâu?

##### Hội thoại 2 — Mua áo khoác mùa đông (màu ở dòng Akkusativ)
* *Verkäuferin*: *„Guten Tag! Kann ich Ihnen helfen?“* — Xin chào! Tôi có thể giúp gì cho ngài?
* *Kunde*: *„Ja, ich suche einen Wintermantel.“* — Vâng, tôi tìm một chiếc áo khoác mùa đông.
* *Verkäuferin*: *„Wir haben hier einen schwarzen Mantel und einen grauen Mantel.“* — Ở đây chúng tôi có một chiếc áo măng tô đen và một chiếc xám. *(màu + Akkusativ, không có Dativ)*
* *Kunde*: *„Welchen Mantel finden Sie wärmer?“* — Ngài thấy chiếc áo nào ấm hơn?
* *Verkäuferin*: *„Beide sind sehr warm.“* — Cả hai đều rất ấm.
* *Kunde*: *„Dann probiere ich diesen hier an.“* — Vậy tôi thử chiếc này đây.
* *Verkäuferin*: *„Passt er Ihnen?“* — Nó có vừa với ngài không? *(Dativ, không có màu)*
* *Kunde*: *„Ja, er passt mir sehr gut, und er gefällt mir auch. Ich nehme ihn.“* — Vâng, nó rất vừa với tôi, và tôi cũng thích. Tôi lấy nó.
* *Verkäuferin*: *„Das macht neunzig Euro.“* — Tổng cộng là chín mươi euro.

##### Hội thoại 3 — Đổi quần vì dài quá
* *Kundin*: *„Guten Tag. Diese Hose ist mir zu lang.“* — Xin chào. Chiếc quần này dài quá đối với tôi.
* *Verkäufer*: *„Haben Sie die Hose schon getragen?“* — Bạn đã mặc chiếc quần này chưa? *(Perfekt, Bài 9)*
* *Kundin*: *„Nein, ich habe sie nur anprobiert.“* — Chưa, tôi chỉ mới thử thôi.
* *Verkäufer*: *„Dann nehmen Sie diese Hose hier. Sie ist kürzer.“* — Vậy bạn lấy chiếc quần này đây. Nó ngắn hơn. *(Komparativ, Bài 10)*
* *Kundin*: *„Danke, die passt mir gut.“* — Cảm ơn, chiếc này vừa với tôi.

##### Hội thoại 4 — Chọn quà sinh nhật (`Dativ + Akkusativ`, không có màu)
* *Tom*: *„Ich suche ein Geschenk für meinen Vater. Er hat bald Geburtstag.“* — Tôi tìm một món quà cho bố. Sắp đến sinh nhật ông.
* *Verkäufer*: *„Wie gefällt ihm dieser Gürtel?“* — Ông ấy có thích chiếc thắt lưng này không?
* *Tom*: *„Der Gürtel ist schön, aber mein Vater hat schon einen. Ich schenke ihm eine Krawatte.“* — Thắt lưng đẹp, nhưng bố tôi đã có rồi. Tôi tặng ông một chiếc cà vạt.
* *Verkäufer*: *„Dann zeige ich Ihnen unsere Krawatten.“* — Vậy tôi cho ngài xem những chiếc cà vạt của chúng tôi.

---

### HỌC PHẦN 8: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN (`TEXTANALYSE: KLEIDUNG UND WETTER` — KÈM AUDIO `de-DE`)

#### 8.1. Đoạn văn 1: *"Familie Müller macht viel Sport"* (màu ở Akkusativ — khớp bảng giảng)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Familie Müller macht viel Sport. Frau Müller spielt Fußball. Sie trägt **eine grüne** Hose, **ein schwarzes** T-Shirt und **weiße** Schuhe. Ihr Mann spielt Tennis. Heute hat er **einen blauen** Trainingsanzug und **gelbe** Schuhe angezogen. Ihr Sohn geht joggen. Er zieht **eine schwarze** Hose und **einen roten** Pullover an. Ihre Tochter tanzt. Sie trägt **ein blaues** Kleid und **schwarze** Schuhe.“*
* **Dịch nghĩa tiếng Việt**:
  > *„Gia đình Müller tập thể thao nhiều. Bà Müller chơi bóng đá. Bà mặc một chiếc quần xanh lá, một chiếc áo phông đen và đi giày trắng. Chồng bà chơi quần vợt. Hôm nay ông ấy đã mặc một bộ đồ thể thao xanh và đi giày vàng. Con trai họ đi chạy bộ. Cậu ấy mặc một chiếc quần đen và một chiếc áo len đỏ. Con gái họ nhảy múa. Cô bé mặc một chiếc đầm xanh và đi giày đen.“*
* **Bảng phân tích** (hiển thị khi bấm "🔍 Phân tích"): xem bảng 3.6 — mỗi cụm `mạo từ + màu + danh từ` kèm **giống, đuôi, lý do**.

#### 8.2. Đoạn văn 2 (mới): *"Ein Tag im Kaufhaus"* (`Dativ + Akkusativ`, `dies-`, `Komparativ`, **không có màu**)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Heute gehe ich mit meiner Oma ins Kaufhaus. Sie braucht einen Mantel für den Winter. Die Verkäuferin zeigt ihr zwei Mäntel. „Welchen Mantel finden Sie schöner? **Diesen** oder **diesen**?“, fragt sie. Oma probiert beide an. „**Dieser** hier ist mir zu eng, aber **dieser** passt mir sehr gut“, sagt sie. „Er gefällt mir auch.“ Ich sage: „Er steht dir wirklich gut, Oma!“ Dann nehmen wir **diesen**. Er kostet neunzig Euro. Zum Geburtstag schenke ich ihr noch einen Schal.“*
* **Dịch nghĩa**:
  > *„Hôm nay tôi đi trung tâm bách hóa cùng bà. Bà cần một chiếc áo khoác cho mùa đông. Cô bán hàng cho bà xem hai chiếc áo măng tô. „Bà thấy chiếc nào đẹp hơn? Chiếc này hay chiếc này?“, cô hỏi. Bà thử cả hai chiếc. „Chiếc này đây chật quá đối với tôi, nhưng chiếc này thì rất vừa với tôi“, bà nói. „Tôi cũng thích nó.“ Tôi nói: „Nó thật sự hợp với bà đấy, bà ơi!“ Rồi chúng tôi lấy chiếc này. Nó giá chín mươi euro. Nhân dịp sinh nhật tôi tặng bà thêm một chiếc khăn quàng.“*
* **Bảng phân tích**:

| Cụm trong đoạn văn | Loại | Giải thích |
| :--- | :-: | :--- |
| *Welchen Mantel … Diesen oder diesen?* | `welch-` + `dies-` (m, Akk) | `der Mantel` là tân ngữ của `finden` → `welchen / diesen`; hai `diesen` chỉ hai chiếc khác nhau. |
| *mit meiner Oma* | Dativ | `mit` + Dativ; `die Oma` (f) → `meiner`. |
| *zeigt ihr zwei Mäntel* | Dativ + Akkusativ | `ihr` (Dativ) đứng trước `zwei Mäntel` (Akk). |
| *Dieser hier ist mir zu eng* | `dies-` Nominativ + Dativ | `dieser` là chủ ngữ (m); `mir` là Dativ; `zu eng` = chật quá. |
| *dieser passt mir sehr gut* | `dies-` Nom + `passen` + Dativ | `passen` + Dativ `mir`. |
| *Er gefällt mir auch* / *Er steht dir wirklich gut* | `gefallen` / `stehen` + Dativ | `mir`, `dir` là Dativ. |
| *schenke ich ihr noch einen Schal* | Dativ + Akkusativ | `ihr` (Dativ) + `einen Schal` (Akk, m). |

#### 8.3. Đoạn văn 3 (mới): *"Das Wetter in Vietnam"* (thời tiết)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Wie ist das Wetter in Vietnam? Im Norden ist es im Winter kalt, und oft ist es neblig. Im Sommer ist es dort sehr heiß, und es regnet viel. In Đà Lạt ist es das ganze Jahr kühl. Dort gibt es am Morgen oft Nebel. In Sài Gòn ist es immer warm, und im Sommer gibt es am Nachmittag oft ein Gewitter. In Deutschland schneit es im Winter, aber in Vietnam schneit es fast nie.“*
* **Dịch nghĩa**:
  > *„Thời tiết ở Việt Nam thế nào? Ở miền Bắc vào mùa đông trời lạnh và thường có sương mù. Vào mùa hè ở đó rất nóng và mưa nhiều. Ở Đà Lạt trời mát quanh năm. Ở đó buổi sáng thường có sương mù. Ở Sài Gòn trời luôn ấm, và vào mùa hè buổi chiều thường có một cơn dông. Ở Đức mùa đông tuyết rơi, nhưng ở Việt Nam hầu như không bao giờ có tuyết.“*
* **Bảng phân tích**:

| Cụm trong đoạn văn | Loại | Giải thích |
| :--- | :-: | :--- |
| *Im Norden ist es im Winter kalt* | `im` + Dativ | `im` = `in dem`; `der Norden`, `der Winter`. `Es ist kalt` (tính từ). |
| *es regnet viel* | Động từ thời tiết | `regnen`, `viel` (nhiều, bổ nghĩa động từ). |
| *Dort gibt es … Nebel* | `es gibt` + Akk | `der Nebel` (m) → `Nebel` không mạo từ. |
| *gibt es … ein Gewitter* | `es gibt` + Akk | `das Gewitter` → `ein Gewitter` (n, Akk). |
| *das ganze Jahr* | Trạng ngữ Akk | *"quanh năm"*. |
| *fast nie* | Trạng từ | `fast nie` = hầu như không bao giờ. |

#### 8.4. Bản tin thời tiết (`der Wetterbericht`) — xem mục 6.9; đoạn này cũng là dữ liệu đọc hiểu cho bài `dung_sai` và nghe điền từ.

---

### HỌC PHẦN 9 (MỤC 2.9): BẢNG TỔNG HỢP & ĐẶC TẢ 6 SƠ ĐỒ SVG (`static/js/kleidung_svg.js`)

#### 9.1. Bảng tổng hợp kiến thức (`CHEAT SHEET` — in được trên 1 trang)
| Mục | Ghi nhớ nhanh |
| :--- | :--- |
| **Màu ở Akkusativ** | `mạo từ ein- + màu + đuôi + danh từ`: m **`-en`** (einen roten Pullover) · f **`-e`** (eine rote Bluse) · n **`-es`** (ein rotes Kleid) · PL **`-e`**, không mạo từ (rote Schuhe) → **"en – e – es – e"** |
| **Màu bất biến** | `orange, lila, rosa, beige, türkis, mint` (pink thường không đuôi): *eine rosa Bluse* |
| **Màu ghép** | `hell- / dunkel- + màu` viết liền, vẫn chia đuôi: *einen hellblauen Pullover* |
| **Akkusativ** | `tragen, anziehen, anprobieren, kaufen, suchen, nehmen, brauchen` → hỏi `Wen/Was?`; chỉ giống đực đổi `den / einen` |
| **Dativ** | `gefallen, passen, stehen, gehören, helfen` → hỏi `Wem?`: *Der Hut steht mir.* · đại từ Dativ: `mir, dir, ihm, ihr, ihm, uns, euch, ihnen, Ihnen` |
| **Dativ + Akk** | `schenken, zeigen, geben`: *Ich schenke ihm einen Gürtel.* (Dativ trước, Akk sau) |
| **dies-** | m `dieser / diesen` · f `diese / diese` · n `dieses / dieses` · PL `diese / diese`; kèm danh từ hoặc đứng một mình; `hier / da` |
| **welch- ↔ dies-** | `Welchen Gürtel nimmst du? — Diesen hier.` (cùng bộ đuôi) |
| **Thời tiết** | `Es regnet / schneit / gewittert` · `Es ist windig / neblig / sonnig / bewölkt / kalt / heiß` · `Die Sonne scheint` · `Es gibt Nebel` |
| **Hỏi thời tiết** | `Wie ist das Wetter in …? / bei dir? / bei euch?` → `Bei mir ist es sonnig.` · `Wie viel Grad sind es?` → `Es sind fünfzehn Grad.` |
| **Mặc theo thời tiết** | `Bei Kälte trage ich einen Mantel.` · `Bei Regen nehme ich einen Regenschirm mit.` |
| **Cửa hàng** | `Ich suche …` · `Welche Größe haben Sie?` · `Kann ich das anprobieren?` · `Das passt mir nicht.` · `Das nehme ich.` |

#### 9.2. Đặc tả 6 sơ đồ SVG trực quan
Mỗi sơ đồ phải có **tiêu đề tiếng Việt + nhãn tiếng Đức**, hoạt động đúng ở chế độ Dark/Light, **hiển thị tiêu đề `Sơ đồ V#: …`** và nút chuyển ví dụ (`◀ 1 / n ▶`) như các sơ đồ của Bài 10; mọi câu tiếng Đức hiển thị trong sơ đồ có nút **`🔊`** (chỉ đọc chuỗi tiếng Đức sạch). **Mọi ví dụ trong sơ đồ tuân thủ R1–R4.**

| Mã | Đặt ở mục | Tên sơ đồ | Hình vẽ & hành vi bắt buộc |
| :-: | :-: | :--- | :--- |
| **V1** | 5 | **Bảng `dies- / welch-` tương tác** | Bảng 4 hàng (`m / f / n / PL`) × 2 cột (`Nominativ / Akkusativ`) cho **cả `welch-` và `dies-`** cạnh nhau (4 cột con). Có **danh sách chọn danh từ trang phục** (`der Rock, die Hose, das Kleid, die Schuhe, der Hut…` lấy từ Phụ lục A). Chọn danh từ + chọn vai trò (chủ ngữ / tân ngữ) → tô sáng ô tương ứng, hiện câu mẫu *„Welchen Rock nimmst du? — Diesen hier.“* + dịch + `🔊`. Ô giống đực dùng màu khác vì là ô duy nhất đổi đuôi. |
| **V2** | 3 | **Bảng đuôi tính từ màu ở Akkusativ + hộp chọn** | Bảng `m -en / f -e / n -es / PL -e`. Bên dưới: chọn **danh từ trang phục** (Phụ lục A1) và **màu có chia đuôi** (Phụ lục A2) → hiển thị cụm **`einen schwarzen Rock`** với đuôi tô màu nổi bật, dịch và `🔊`; chọn màu bất biến → hiển thị *"không đuôi"*. **Chỉ dùng hàm tạo đuôi của Phụ lục A** và **tất cả câu mẫu dùng động từ Akkusativ** (`trage, kaufe, suche, nehme`). |
| **V3** | 4 | **Lưu đồ Akkusativ / Dativ** | Sơ đồ khối theo mục 4.7. Nhánh `Akkusativ` và nhánh `Dativ` có màu khác nhau; mỗi nhánh có **ví dụ không có màu sắc** (nhánh Dativ) và **ví dụ có màu chỉ ở nhánh Akkusativ**. Bấm vào một ví dụ → `🔊`. |
| **V4** | 1 | **Tủ quần áo tương tác (`Kleiderschrank`)** | Hình tủ quần áo với **18 món đồ** (biểu tượng + từ). Bấm món đồ → hiện thẻ *„der Mantel · die Mäntel“* và nghe câu *„Ich trage einen Mantel.“* (mạo từ bất định đúng giống). Có ô chọn màu: chọn màu → câu đổi thành *„Ich trage einen grauen Mantel.“* (đuôi đúng theo bảng). **Không có nút Dativ trong sơ đồ này.** |
| **V5** | 6 | **Bản đồ thời tiết Việt Nam - Đức (`Wetterkarte`)** | Bản đồ đơn giản 2 vùng: **Việt Nam** (Hà Nội, Hải Phòng, Huế, Đà Lạt, Sài Gòn) và **Đức - Áo** (Berlin, Hamburg, München, Wien). Mỗi thành phố có biểu tượng thời tiết (☀️ 🌧️ ❄️ 🌫️ ☁️ 🌬️ ⛈️), nhiệt độ. Bấm thành phố → hiện câu *„In Hamburg regnet es. Es sind sieben Grad.“* + dịch + `🔊` (nhiệt độ đọc bằng chữ). Nút **▶ "Đọc bản tin"** đọc lần lượt các thành phố (nội dung bản tin 6.9). Dữ liệu thời tiết là **dữ liệu mẫu cố định** trong Phụ lục A5, không phải dữ liệu thật. |
| **V6** | 7 | **Phòng thử đồ (`Umkleidekabine`) — hội thoại tương tác** | Khung cảnh cửa hàng: người bán và khách (hai bóng nói). Bấm **▶ "Thử đồ"** → chạy lần lượt Hội thoại 1 → 4 ở mục 7.5, mỗi lượt phát `🔊`. Có nút chọn lượt `◀ ▶` và nút ẩn / hiện bản dịch. |

---

## PHẦN 3: KHO 100 BÀI TẬP ĐỘC NHẤT CỦA BÀI 11 (`lessons/a1/seed_a1_b11.py`) — 18 DẠNG BÀI

Toàn bộ **100 câu hỏi** dưới đây là **câu mới sáng tác**, chỉ tham khảo ý tưởng từ bảng giảng; không trùng với giáo trình, Bài 8, 9 hay 10. Chủ ngữ được **xoay vòng đủ 9 ngôi** (`ich, du, er, sie, es, wir, ihr, sie, Sie`) cùng tên riêng, gia đình, người bán - khách hàng; ngữ cảnh đa dạng (cửa hàng, nhà, chợ, đi học, đi dự tiệc, Hà Nội, Hamburg, Wien…). **Mọi câu có màu sắc đều tuân thủ Quy tắc vàng R1–R4 (màu chỉ ở Akkusativ; câu có màu không có dấu hiệu Dativ).**

### 3.1. Bảng Phân Bổ 100 Câu Hỏi Theo 18 Dạng Bài Tập
| STT | Mã dạng (`type`) | Tên dạng bài hiển thị | Số lượng | Mã câu | Trọng tâm |
| :-: | :--- | :--- | :-: | :-: | :--- |
| 1 | `trac_nghiem` | Trắc nghiệm | **10** | 1–10 | `dies-`, đuôi tính từ màu, Dativ `dir`, câu thời tiết, giống - số nhiều trang phục |
| 2 | `dien_khuyet` | Điền khuyết | **10** | 11–20 | Đại từ Dativ `mir / ihnen / ihm`, `dies-`, `schneit`, `heiß`, `trägst / tragt`, `an` |
| 3 | `dien_duoi_tinh_tu` 🆕 | **Điền đuôi tính từ màu** | **6** | 21–26 | Điền `-en / -e / -es` cho màu ở Akkusativ |
| 4 | `dich_nghia_vd` | Dịch từ: Việt → Đức | **6** | 27–32 | Trang phục (kèm mạo từ) + thời tiết |
| 5 | `dich_nghia_dv` | Dịch từ / câu ngắn: Đức → Việt | **6** | 33–38 | Trang phục, thời tiết, câu Dativ ngắn |
| 6 | `noi_o` | Nối ô (Matching) | **8** | 39–46 | Từ ↔ nghĩa, số ít ↔ số nhiều, màu, thời tiết, `dies-`, đại từ Dativ, hỏi ↔ đáp |
| 7 | `dien_tao_cau` | Điền 2 chỗ trống tạo câu | **6** | 47–52 | Động từ + đuôi màu, `dies-`, `steht / stehen`, thời tiết, Perfekt |
| 8 | `nghe_dien` | Nghe `de-DE` và điền từ | **6** | 53–58 | Nghe câu về trang phục, cỡ giày, thời tiết, Dativ |
| 9 | `dich_cau_vd` | Dịch câu: Việt → Đức | **5** | 59–63 | Màu + Akkusativ, `dies-`, `steht dir`, thời tiết `bei mir / bei dir` |
| 10 | `dich_cau_dv` | Dịch câu: Đức → Việt | **5** | 64–68 | Cửa hàng, thời tiết, Dativ + so sánh |
| 11 | `sap_xep_cau` | Sắp xếp từ thành câu | **5** | 69–73 | Vị trí động từ: Akkusativ, `welch-`, `dies-`, Dativ, thời tiết |
| 12 | `phan_loai_giong` | Phân loại `der / die / das` | **3** | 74–76 | Trang phục và danh từ thời tiết |
| 13 | `phan_loai_cach` 🆕 | **Phân loại Akkusativ / Dativ** | **4** | 77–80 | Mỗi câu 4 hàng: cụm được in đậm là **Akkusativ** hay **Dativ**? |
| 14 | `tim_loi_sai` | Tìm lỗi và sửa câu | **5** | 81–85 | Sai đuôi màu, màu bất biến, `dies-`, đại từ Dativ, động từ thời tiết |
| 15 | `viet_lai_dies` 🆕 | **Viết lại với `dies-`** | **5** | 86–90 | Thay `der/die/das` bằng `dies-`, có / không kèm danh từ |
| 16 | `dung_sai` | Đọc hiểu Đúng / Sai | **3** | 91–93 | Một đoạn về trang phục (có màu) + một bản tin thời tiết |
| 17 | `hoi_thoai_sap_xep` | Sắp xếp hội thoại | **3** | 94–96 | Cửa hàng, đổi đồ, trò chuyện thời tiết |
| 18 | `bieu_tuong_thoi_tiet` 🆕 | **Nhìn biểu tượng chọn câu thời tiết** | **4** | 97–100 | Biểu tượng thời tiết → chọn câu tiếng Đức đúng |
| | | **TỔNG CỘNG BÀI 11** | **100** | 1–100 | **100% độc nhất + QA Zero-Bug** |

> 📌 Phân bổ trọng tâm (ước lượng): **khoảng một phần ba số câu** về trang phục - màu sắc - `Akkusativ` / `Dativ`, **khoảng một phần ba** về `dies-` (kết hợp `welch-`), **khoảng một phần tư** về thời tiết; phần còn lại là từ vựng - mua sắm - tổng hợp. Câu hỏi nào cũng có thể chạm nhiều nội dung cùng lúc (ví dụ vừa `dies-` vừa Dativ).

### 3.2. Đặc tả giao diện & chấm điểm cho 4 dạng bài MỚI (🆕) — *làm thêm, không phá component cũ*
Các dạng `sap_xep_cau`, `tim_loi_sai`, `dung_sai`, `phan_loai_giong`, `hoi_thoai_sap_xep` **dùng lại nguyên component của Bài 9 / Bài 10**. Bốn dạng mới:
| Dạng | Giao diện người học | Dữ liệu câu hỏi (`question object`) | Quy tắc chấm điểm |
| :--- | :--- | :--- | :--- |
| `dien_duoi_tinh_tu` | Câu tiếng Đức có **một chỗ trống ngay sau thân tính từ** (ví dụ `Er kauft einen blau__ Anzug.`); ô nhập nhỏ (1–3 ký tự); kèm bảng nhắc **"en – e – es – e"** thu gọn | `display_sentence`, `stem` (thân màu), `noun`, `gender` (`m/f/n/pl`), `accepted_answers` (đuôi, ví dụ `["en"]`), `translation_vi` | So khớp đuôi **không phân biệt hoa thường**. Sau khi trả lời, hiển thị cụm đầy đủ (`einen blauen Anzug`) và voice đọc **cả câu đã điền**. |
| `phan_loai_cach` | Bảng 4 hàng; mỗi hàng 1 câu tiếng Đức, **cụm cần xét được in đậm**, 2 nút **`Akkusativ`** / **`Dativ`** | `items` = 4 × {`sentence`, `target_phrase`, `case` (`Akk`/`Dativ`), `reason_vi`, `translation_vi`} | Đúng khi **cả 4 hàng** đúng; hàng sai tô đỏ và hiện `reason_vi` (nêu rõ động từ / giới từ quyết định cách). Mỗi `sentence` **tuân thủ R1–R4 riêng**. |
| `viet_lai_dies` | Hiển thị câu gốc dùng `der/die/das`; yêu cầu (*"thay bằng `dies-` kèm danh từ"* hoặc *"dùng `dies-` đứng một mình"*); người học **gõ lại cả câu** | `source_sentence`, `instruction_vi`, `accepted_answers`, `translation_vi` (dịch câu đáp án) | So khớp như `dich_cau_vd` (không phân biệt hoa thường, bỏ dấu câu cuối). |
| `bieu_tuong_thoi_tiet` | Hiển thị **biểu tượng thời tiết lớn** (emoji, có `alt` bằng tiếng Việt) + 4 lựa chọn là câu tiếng Đức | `weather_icon` (emoji), `icon_alt_vi`, `options` (4 câu), `correct_option_id`, `translation_vi`, `explanation` | Trắc nghiệm một đáp án. Voice đọc **câu đúng**; không bao giờ đọc tên emoji. |

> 🔊 **Quy tắc voice cho mọi dạng**: sau khi người học trả lời xong, nút `🔊` đọc **câu tiếng Đức đúng đầy đủ**. Không bao giờ đọc ký hiệu `___`, `__`, `[1]`, `→`, `°C`, `€`, emoji. **Nhiệt độ, cỡ và giá phải chuyển thành chữ trước khi đọc** (xem mục 5.2).
> 🈯 **Quy tắc `translation_vi` theo dạng**: `dich_nghia_vd` (Câu 27–32) = **đề tiếng Việt** (hiển thị `Dịch nghĩa: <đề> = <đáp án Đức>`); `dich_nghia_dv`, `dich_cau_dv` = **đáp án tiếng Việt**; `dien_tao_cau`, `dich_cau_vd` = **đề tiếng Việt**; `nghe_dien` = `hint_vi`; `noi_o` = dòng *"Dịch nghĩa các cặp"*; `phan_loai_giong`, `phan_loai_cach` = nghĩa / dịch từng hàng; `hoi_thoai_sap_xep` = dịch **từng lượt lời**. Không được để trống phần dịch ở bất kỳ dạng nào.
> 🔠 **Quy tắc chữ hoa**: so khớp **không phân biệt hoa/thường**; chấp nhận `ä/ö/ü/ß` được gõ thành `ae/oe/ue/ss`.
> 🎨 **Nhắc lại**: không câu nào được **vừa có màu vừa có Dativ** (R2, R3) và **không câu nào dùng màu ở Nominativ / vị ngữ** (R4).

---

### 3.3. Danh Sách Chi Tiết 100 Câu Hỏi (Để Seed Vào `lessons/a1/seed_a1_b11.py`)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 10 Câu: Câu 1 → Câu 10)
1. **Câu 1** *(kèm sơ đồ `visual: V1`)*
   * `question`: Quan sát **bảng `dies- / welch-` (V1)**. Chọn dạng đúng: *„Wir nehmen ___ Hut hier.“* (`der Hut`, tân ngữ)
   * Đáp án: `A. dieser` | `B. diesen` (Đúng) | `C. diese` | `D. dieses`
   * Dịch nghĩa câu: *„Chúng tôi lấy chiếc mũ này đây.“*
   * Giải thích: `der Hut` là giống **đực**, làm **tân ngữ** của `nehmen` → **Akkusativ** → `den` → `diesen` → **`Wir nehmen diesen Hut hier.`**
2. **Câu 2**
   * `question`: Chọn dạng đúng: *„___ Schuhe sind mir zu groß.“*
   * Đáp án: `A. Dieser` | `B. Diesen` | `C. Diese` (Đúng) | `D. Dieses`
   * Dịch nghĩa câu: *„Đôi giày này rộng quá đối với tôi.“*
   * Giải thích: `die Schuhe` là **số nhiều**, làm chủ ngữ → **`Diese Schuhe sind mir zu groß.`** (số nhiều luôn dùng `diese`).
3. **Câu 3**
   * `question`: Chọn đuôi đúng: *„Heute trage ich einen ___ Pullover.“*
   * Đáp án: `A. roter` | `B. roten` (Đúng) | `C. rote` | `D. rotes`
   * Dịch nghĩa câu: *„Hôm nay tôi mặc một chiếc áo len đỏ.“*
   * Giải thích: `der Pullover` giống **đực**, Akkusativ, mạo từ `einen` → tính từ đuôi **`-en`** → **`einen roten Pullover`**.
4. **Câu 4**
   * `question`: Chọn đuôi đúng: *„Sie kauft eine ___ Hose.“*
   * Đáp án: `A. schwarzen` | `B. schwarze` (Đúng) | `C. schwarzes` | `D. schwarzer`
   * Dịch nghĩa câu: *„Cô ấy mua một chiếc quần đen.“*
   * Giải thích: `die Hose` giống **cái** → đuôi **`-e`** → **`eine schwarze Hose`**.
5. **Câu 5**
   * `question`: Chọn đuôi đúng: *„Er sucht ein ___ Hemd.“*
   * Đáp án: `A. weißer` | `B. weißen` | `C. weiße` | `D. weißes` (Đúng)
   * Dịch nghĩa câu: *„Anh ấy tìm một chiếc áo sơ mi trắng.“*
   * Giải thích: `das Hemd` giống **trung**; `ein` không có đuôi nên tính từ mang **`-es`** → **`ein weißes Hemd`**.
6. **Câu 6**
   * `question`: Chọn đại từ đúng: *„Die Jacke passt ___ gut.“* (người nói với `du`)
   * Đáp án: `A. dich` | `B. dir` (Đúng) | `C. du` | `D. dein`
   * Dịch nghĩa câu: *„Chiếc áo khoác rất vừa với bạn.“*
   * Giải thích: `passen` đi với **Dativ**; Dativ của `du` là **`dir`** → **`Die Jacke passt dir gut.`**
7. **Câu 7**
   * `question`: Chọn câu đúng nghĩa *"Trời đang mưa"*:
   * Đáp án: `A. Es ist regnet.` | `B. Es regnet.` (Đúng) | `C. Der Regen ist.` | `D. Es hat regnen.`
   * Dịch nghĩa câu: *„Trời đang mưa.“*
   * Giải thích: `regnen` là **động từ** nên nói **`Es regnet.`** (không dùng `ist`).
8. **Câu 8**
   * `question`: Chọn dạng đúng: *„Ich kaufe gern ___ Schuhe.“* (số nhiều, không có mạo từ)
   * Đáp án: `A. braune` (Đúng) | `B. braunen` | `C. braunes` | `D. brauner`
   * Dịch nghĩa câu: *„Tôi thích mua giày nâu.“*
   * Giải thích: Số nhiều không mạo từ ở Akkusativ → đuôi **`-e`** → **`braune Schuhe`**.
9. **Câu 9**
   * `question`: Chọn từ đúng: *„Welchen Gürtel nimmst du? — ___ hier.“*
   * Đáp án: `A. Dieser` | `B. Diesen` (Đúng) | `C. Diese` | `D. Dieses`
   * Dịch nghĩa câu: *„Bạn lấy chiếc thắt lưng nào? — Chiếc này đây.“*
   * Giải thích: `Welchen Gürtel` là `der Gürtel` (m, Akk) nên trả lời bằng **`Diesen hier.`**
10. **Câu 10**
    * `question`: Dòng nào ghi **ĐÚNG cả mạo từ lẫn số nhiều**?
    * Đáp án: `A. der Mantel – die Mäntel / die Jacke – die Jacken / das Kleid – die Kleider` (Đúng) | `B. der Mantel – die Mantels / die Jacke – die Jacke / das Kleid – die Kleids` | `C. die Mantel – die Mäntel / der Jacke – die Jacken / das Kleid – die Kleider` | `D. der Rock – die Rocks / die Hose – die Hose / das Hemd – die Hemde`
    * Dịch nghĩa câu: *„áo măng tô – các áo măng tô / áo khoác – các áo khoác / đầm – các đầm.“*
    * Giải thích: `der Mantel → die Mäntel` (thêm Umlaut), `die Jacke → die Jacken`, `das Kleid → die Kleider`. Các dòng khác sai giống hoặc số nhiều (`die Röcke`, `die Hosen`, `die Hemden`).

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 10 Câu: Câu 11 → Câu 20)
11. **Câu 11**: Điền đại từ Dativ: *„Der Hut steht ___ gut.“* (`ich`)
    * Đáp án chấp nhận: `["mir"]`
    * Dịch nghĩa câu: *„Chiếc mũ rất hợp với tôi.“*
    * Giải thích: `stehen` (hợp) đi với **Dativ**; Dativ của `ich` là **`mir`**.
12. **Câu 12**: Điền đại từ Dativ: *„Die Stiefel passen ___ nicht.“* (`sie`, số nhiều — *họ*)
    * Đáp án chấp nhận: `["ihnen"]`
    * Dịch nghĩa câu: *„Đôi bốt không vừa với họ.“*
    * Giải thích: `passen` + **Dativ**; Dativ của `sie` (số nhiều) là **`ihnen`**.
13. **Câu 13**: Điền đại từ Dativ: *„Der Pullover gefällt ___ sehr.“* (`er`)
    * Đáp án chấp nhận: `["ihm"]`
    * Dịch nghĩa câu: *„Chiếc áo len làm anh ấy rất thích.“*
    * Giải thích: `gefallen` + **Dativ**; Dativ của `er` là **`ihm`**.
14. **Câu 14**: Điền dạng `dies-` đúng (Akkusativ): *„Ich möchte ___ Jacke hier.“* (`die Jacke`)
    * Đáp án chấp nhận: `["diese"]`
    * Dịch nghĩa câu: *„Tôi muốn chiếc áo khoác này đây.“*
    * Giải thích: `die Jacke` giống cái; Akkusativ không đổi → **`diese`**.
15. **Câu 15**: Điền dạng `dies-` đúng (Nominativ): *„___ Kleid ist sehr schön.“* (`das Kleid`)
    * Đáp án chấp nhận: `["dieses"]`
    * Dịch nghĩa câu: *„Chiếc đầm này rất đẹp.“*
    * Giải thích: `das Kleid` giống trung → **`Dieses`**.
16. **Câu 16**: Chia động từ `schneien`: *„Im Winter ___ es in Deutschland oft.“*
    * Đáp án chấp nhận: `["schneit"]`
    * Dịch nghĩa câu: *„Vào mùa đông ở Đức tuyết thường rơi.“*
    * Giải thích: Động từ thời tiết dùng ngôi `es` → **`schneit`**.
17. **Câu 17**: Điền tính từ của `die Hitze`: *„Im Sommer ist es in Sài Gòn oft sehr ___.“*
    * Đáp án chấp nhận: `["heiß", "heiss"]`
    * Dịch nghĩa câu: *„Vào mùa hè ở Sài Gòn trời thường rất nóng.“*
    * Giải thích: Sau `ist es` dùng **tính từ**: `die Hitze → heiß` → **`Es ist heiß.`**
18. **Câu 18**: Chia động từ `tragen` ở ngôi `du`: *„Du ___ heute eine Hose und einen Pullover.“*
    * Đáp án chấp nhận: `["trägst", "traegst"]`
    * Dịch nghĩa câu: *„Hôm nay bạn mặc một chiếc quần và một chiếc áo len.“*
    * Giải thích: `tragen` đổi `a → ä` ở `du` → **`trägst`**.
19. **Câu 19**: Chia động từ `tragen` ở ngôi `ihr`: *„Ihr ___ im Sommer gern T-Shirts.“*
    * Đáp án chấp nhận: `["tragt"]`
    * Dịch nghĩa câu: *„Vào mùa hè các bạn thích mặc áo phông.“*
    * Giải thích: Ngôi `ihr` **không đổi nguyên âm**: gốc `trag-` + `-t` = **`tragt`**.
20. **Câu 20**: Điền tiền tố tách: *„Anna zieht heute einen Mantel ___.“* (`anziehen`)
    * Đáp án chấp nhận: `["an"]`
    * Dịch nghĩa câu: *„Hôm nay Anna mặc áo măng tô vào.“*
    * Giải thích: `anziehen` là **động từ tách**: `zieht … an` → tiền tố **`an`** đứng cuối câu.

---

#### NHÓM 3: 🆕 ĐIỀN ĐUÔI TÍNH TỪ MÀU (`dien_duoi_tinh_tu` — 6 Câu: Câu 21 → Câu 26)
Điền **đuôi** vào chỗ trống `__` (ví dụ `blau__` → `en`).
21. **Câu 21**: *„Er kauft einen blau__ Anzug.“* (`der Anzug`, m)
    * Đáp án chấp nhận: `["en"]`
    * Dịch nghĩa câu: *„Anh ấy mua một bộ com lê xanh.“*
    * Giải thích: `der Anzug` giống đực, Akkusativ, `einen` → đuôi **`-en`** → **`einen blauen Anzug`**.
22. **Câu 22**: *„Sie trägt ein gelb__ Kleid.“* (`das Kleid`, n)
    * Đáp án chấp nhận: `["es"]`
    * Dịch nghĩa câu: *„Cô ấy mặc một chiếc đầm vàng.“*
    * Giải thích: `das Kleid` giống trung → đuôi **`-es`** → **`ein gelbes Kleid`**.
23. **Câu 23**: *„Wir suchen eine grau__ Hose.“* (`die Hose`, f)
    * Đáp án chấp nhận: `["e"]`
    * Dịch nghĩa câu: *„Chúng tôi tìm một chiếc quần xám.“*
    * Giải thích: `die Hose` giống cái → đuôi **`-e`** → **`eine graue Hose`**.
24. **Câu 24**: *„Die Kinder brauchen dunkelblau__ Schuhe.“* (`die Schuhe`, số nhiều, không mạo từ)
    * Đáp án chấp nhận: `["e"]`
    * Dịch nghĩa câu: *„Bọn trẻ cần đôi giày xanh đậm.“*
    * Giải thích: Số nhiều không mạo từ ở Akkusativ → đuôi **`-e`** → **`dunkelblaue Schuhe`**.
25. **Câu 25**: *„Ich nehme einen schwarz__ Gürtel.“* (`der Gürtel`, m)
    * Đáp án chấp nhận: `["en"]`
    * Dịch nghĩa câu: *„Tôi lấy một chiếc thắt lưng đen.“*
    * Giải thích: `der Gürtel` giống đực, Akkusativ → **`-en`** → **`einen schwarzen Gürtel`**.
26. **Câu 26**: *„Sie probiert ein braun__ T-Shirt an.“* (`das T-Shirt`, n)
    * Đáp án chấp nhận: `["es"]`
    * Dịch nghĩa câu: *„Cô ấy thử một chiếc áo phông nâu.“*
    * Giải thích: `das T-Shirt` giống trung → **`-es`** → **`ein braunes T-Shirt`**.

---

#### NHÓM 4: DỊCH TỪ VIỆT → ĐỨC (`dich_nghia_vd` — 6 Câu: Câu 27 → Câu 32)
27. **Câu 27**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"áo khoác"***
    * Đáp án chấp nhận: `["die Jacke", "Jacke"]`
    * Giải thích: Áo khoác là **`die Jacke`** (số nhiều: `die Jacken`).
28. **Câu 28**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"chân váy"***
    * Đáp án chấp nhận: `["der Rock", "Rock"]`
    * Giải thích: Chân váy là **`der Rock`** (số nhiều: `die Röcke`).
29. **Câu 29**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"áo sơ mi nam"***
    * Đáp án chấp nhận: `["das Hemd", "Hemd"]`
    * Giải thích: Áo sơ mi nam là **`das Hemd`** (số nhiều: `die Hemden`).
30. **Câu 30**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"thắt lưng"***
    * Đáp án chấp nhận: `["der Gürtel", "Gürtel", "der Guertel"]`
    * Giải thích: Thắt lưng là **`der Gürtel`** (số nhiều: `die Gürtel`).
31. **Câu 31**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"sương mù"***
    * Đáp án chấp nhận: `["der Nebel", "Nebel"]`
    * Giải thích: Sương mù là **`der Nebel`**; tính từ tương ứng là `neblig`.
32. **Câu 32**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"tuyết"***
    * Đáp án chấp nhận: `["der Schnee", "Schnee"]`
    * Giải thích: Tuyết là **`der Schnee`** (chỉ số ít); động từ tương ứng là `schneien`.

---

#### NHÓM 5: DỊCH TỪ / CÂU NGẮN ĐỨC → VIỆT (`dich_nghia_dv` — 6 Câu: Câu 33 → Câu 38)
33. **Câu 33**: Dịch sang tiếng Việt: ***„die Krawatte“***
    * Đáp án chấp nhận: `["cà vạt", "chiếc cà vạt", "ca vạt"]`
    * Giải thích: `die Krawatte` là cà vạt (số nhiều: `die Krawatten`).
34. **Câu 34**: Dịch sang tiếng Việt: ***„der Handschuh“***
    * Đáp án chấp nhận: `["găng tay", "chiếc găng tay", "một chiếc găng tay"]`
    * Giải thích: `der Handschuh` là găng tay (số nhiều: `die Handschuhe`).
35. **Câu 35**: Dịch sang tiếng Việt: ***„bewölkt“***
    * Đáp án chấp nhận: `["nhiều mây", "có mây", "trời nhiều mây", "u ám nhiều mây"]`
    * Giải thích: `bewölkt` là tính từ chỉ trời nhiều mây (từ `die Wolke`); *„Es ist bewölkt.“*
36. **Câu 36**: Dịch sang tiếng Việt: ***„Es ist neblig.“***
    * Đáp án chấp nhận: `["Trời có sương mù.", "Có sương mù.", "Trời nhiều sương mù.", "Trời sương mù."]`
    * Giải thích: `Es ist neblig.` = *"Trời có sương mù."* (`es` không dịch).
37. **Câu 37**: Dịch sang tiếng Việt: ***„Das steht mir nicht.“***
    * Đáp án chấp nhận: `["Cái này không hợp với tôi.", "Cái này không hợp tôi.", "Cái đó không hợp với tôi."]`
    * Giải thích: `stehen` (hợp) + Dativ `mir`; `nicht` = không → *"không hợp với tôi"*.
38. **Câu 38**: Dịch sang tiếng Việt: ***„Die Hose ist mir zu lang.“***
    * Đáp án chấp nhận: `["Chiếc quần này dài quá đối với tôi.", "Chiếc quần dài quá đối với tôi.", "Cái quần dài quá với tôi.", "Quần dài quá đối với tôi."]`
    * Giải thích: `zu lang` = *dài quá*; `mir` (Dativ) = *đối với tôi*.

---

#### NHÓM 6: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 8 Bài: Câu 39 → Câu 46, mỗi bài 4 cặp độc nhất)
39. **Câu 39 (Bài nối 1 — Từ Đức ↔ nghĩa Việt, trang phục)**:
    * `der Mantel` ↔ `áo măng tô`
    * `die Socke` ↔ `tất`
    * `der Hut` ↔ `mũ`
    * `die Bluse` ↔ `áo sơ mi nữ`
    * Giải thích: Bốn món trang phục thông dụng: `der Mantel`, `die Socke`, `der Hut`, `die Bluse`.
40. **Câu 40 (Bài nối 2 — Số ít ↔ Số nhiều)**:
    * `der Rock` ↔ `die Röcke`
    * `die Hose` ↔ `die Hosen`
    * `das Kleid` ↔ `die Kleider`
    * `der Schuh` ↔ `die Schuhe`
    * Dịch nghĩa các cặp: *chân váy – những chân váy; quần – những chiếc quần; đầm – những chiếc đầm; giày – những đôi giày.*
    * Giải thích: `Rock` thêm Umlaut, `Hose` thêm `-n`, `Kleid` thêm `-er`, `Schuh` thêm `-e`.
41. **Câu 41 (Bài nối 3 — Màu ↔ Nghĩa Việt)**:
    * `schwarz` ↔ `đen`
    * `grau` ↔ `ghi / xám`
    * `braun` ↔ `nâu`
    * `gelb` ↔ `vàng`
    * Giải thích: Bốn màu cơ bản `schwarz, grau, braun, gelb`.
42. **Câu 42 (Bài nối 4 — Danh từ thời tiết ↔ Tính từ)**:
    * `der Nebel` ↔ `neblig`
    * `der Wind` ↔ `windig`
    * `die Sonne` ↔ `sonnig`
    * `die Hitze` ↔ `heiß`
    * Dịch nghĩa các cặp: *sương mù – có sương mù; gió – có gió; mặt trời – nắng; khí nóng – nóng.*
    * Giải thích: Danh từ + tính từ đi với `Es ist …` (`Es ist neblig / windig / sonnig / heiß`).
43. **Câu 43 (Bài nối 5 — Tiếng Việt ↔ Câu thời tiết tiếng Đức)**:
    * `Trời mưa.` ↔ `Es regnet.`
    * `Tuyết rơi.` ↔ `Es schneit.`
    * `Trời nhiều mây.` ↔ `Es ist bewölkt.`
    * `Trời nóng.` ↔ `Es ist heiß.`
    * Giải thích: Hai câu đầu dùng **động từ** (`regnet`, `schneit`); hai câu sau dùng **`ist` + tính từ**.
44. **Câu 44 (Bài nối 6 — Danh từ ↔ Cụm `dies-` ở Akkusativ)**:
    * `der Gürtel` ↔ `diesen Gürtel`
    * `die Hose` ↔ `diese Hose`
    * `das Hemd` ↔ `dieses Hemd`
    * `die Stiefel` ↔ `diese Stiefel`
    * Dịch nghĩa các cặp: *thắt lưng – chiếc thắt lưng này; quần – chiếc quần này; áo sơ mi – chiếc áo sơ mi này; bốt – những đôi bốt này.*
    * Giải thích: Chỉ giống đực đổi (`den → diesen`); `die → diese`, `das → dieses`.
45. **Câu 45 (Bài nối 7 — Ngôi ↔ Đại từ Dativ)**:
    * `ich` ↔ `mir`
    * `du` ↔ `dir`
    * `wir` ↔ `uns`
    * `sie (họ)` ↔ `ihnen`
    * Dịch nghĩa các cặp: *tôi – cho tôi; bạn – cho bạn; chúng tôi – cho chúng tôi; họ – cho họ.*
    * Giải thích: Dativ của `ich` là `mir`, `du` là `dir`, `wir` là `uns`, `sie` (số nhiều) là `ihnen`.
46. **Câu 46 (Bài nối 8 — Câu hỏi ở cửa hàng ↔ Câu trả lời)**:
    * `Kann ich Ihnen helfen?` ↔ `Ich suche einen Pullover.`
    * `Passt Ihnen die Hose?` ↔ `Ja, sie passt gut.`
    * `Wie gefällt dir das Hemd?` ↔ `Es gefällt mir sehr.`
    * `Wie viel kostet der Mantel?` ↔ `Er kostet neunzig Euro.`
    * Dịch nghĩa các cặp: *Tôi có thể giúp gì ạ? – Tôi tìm một chiếc áo len. | Quần có vừa với ngài không? – Có, nó vừa. | Bạn thấy chiếc áo sơ mi này thế nào? – Tôi rất thích nó. | Áo măng tô giá bao nhiêu? – Nó giá chín mươi euro.*
    * Giải thích: Mỗi câu trả lời khớp loại thông tin được hỏi (nhu cầu, vừa vặn, sở thích, giá).

---

#### NHÓM 7: ĐIỀN VÀO 2 CHỖ TRỐNG TẠO CÂU (`dien_tao_cau` — 6 Câu: Câu 47 → Câu 52)
47. **Câu 47**: Điền 2 từ để hoàn thành câu: *„Hôm nay tôi mặc một chiếc đầm đỏ.“*
    * Khung câu hiển thị: `Heute [1] ich ein rot[2] Kleid.`
    * Đáp án từng ô: Ô 1 = `["trage"]`, Ô 2 = `["es"]`.
    * Giải thích: `ich` + `tragen` → **`trage`**; `das Kleid` (n) → đuôi **`-es`** → **`ein rotes Kleid`**.
48. **Câu 48**: Điền 2 từ để hoàn thành câu: *„Bạn mặc một chiếc áo măng tô xanh lá.“*
    * Khung câu hiển thị: `Du [1] einen grün[2] Mantel.`
    * Đáp án từng ô: Ô 1 = `["trägst", "traegst"]`, Ô 2 = `["en"]`.
    * Giải thích: `du` + `tragen` → **`trägst`**; `der Mantel` (m, Akk) → **`-en`** → **`einen grünen Mantel`**.
49. **Câu 49**: Điền 2 từ để hoàn thành câu: *„Chiếc quần này đây dài quá, nhưng chiếc quần kia thì vừa.“*
    * Khung câu hiển thị: `[1] Hose hier ist zu lang, aber [2] Hose da passt.`
    * Đáp án từng ô: Ô 1 = `["diese"]`, Ô 2 = `["diese"]`.
    * Giải thích: `die Hose` giống cái → ở cả hai cách đều là **`diese`**; `hier` chỉ gần, `da` chỉ xa.
50. **Câu 50**: Điền 2 từ để hoàn thành câu: *„Chiếc áo len hợp với tôi, và đôi giày cũng hợp với tôi.“*
    * Khung câu hiển thị: `Der Pullover [1] mir gut, und die Schuhe [2] mir auch.`
    * Đáp án từng ô: Ô 1 = `["steht"]`, Ô 2 = `["stehen"]`.
    * Giải thích: `der Pullover` (số ít) → **`steht`**; `die Schuhe` (số nhiều) → **`stehen`**; `stehen` + Dativ `mir`.
51. **Câu 51**: Điền 2 từ để hoàn thành câu: *„Hôm nay ở Hamburg trời mưa và lạnh.“*
    * Khung câu hiển thị: `Heute [1] es in Hamburg, und es ist [2].`
    * Đáp án từng ô: Ô 1 = `["regnet"]`, Ô 2 = `["kalt"]`.
    * Giải thích: `regnen` → **`regnet`** (ngôi `es`); `die Kälte` → tính từ **`kalt`**.
52. **Câu 52**: Điền 2 từ để hoàn thành câu (ôn Perfekt): *„Hôm qua trời có tuyết và tôi đã mặc áo măng tô.“*
    * Khung câu hiển thị: `Gestern hat es [1] und ich habe einen Mantel [2].`
    * Đáp án từng ô: Ô 1 = `["geschneit"]`, Ô 2 = `["angezogen"]`.
    * Giải thích: `schneien → geschneit` (động từ thời tiết dùng `haben`); `anziehen → angezogen` (tách: `an` + `ge` + `zogen`).

---

#### NHÓM 8: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 6 Câu: Câu 53 → Câu 58)
53. **Câu 53**:
    * `audio_text`: *"Ich trage heute einen blauen Pullover."*
    * `display_sentence`: *"Ich trage heute einen ___ Pullover."*
    * `hint_vi`: *"Hôm nay tôi mặc một chiếc áo len xanh."*
    * `accepted_answers`: `["blauen"]`
    * Giải thích: `der Pullover` (m, Akk) → tính từ **`blauen`**.
54. **Câu 54**:
    * `audio_text`: *"Diese Schuhe sind Größe neununddreißig."*
    * `display_sentence`: *"Diese Schuhe sind Größe ___."*
    * `hint_vi`: *"Đôi giày này cỡ ba mươi chín."*
    * `accepted_answers`: `["neununddreißig", "neununddreissig", "39"]`
    * Giải thích: Cỡ `39` đọc là **`neununddreißig`** (đơn vị trước, hàng chục sau).
55. **Câu 55**:
    * `audio_text`: *"Es ist heute neblig und kalt."*
    * `display_sentence`: *"Es ist heute ___ und kalt."*
    * `hint_vi`: *"Hôm nay trời có sương mù và lạnh."*
    * `accepted_answers`: `["neblig"]`
    * Giải thích: `der Nebel` → tính từ **`neblig`**.
56. **Câu 56**:
    * `audio_text`: *"Der Mantel passt mir leider nicht."*
    * `display_sentence`: *"Der Mantel passt ___ leider nicht."*
    * `hint_vi`: *"Tiếc là chiếc áo măng tô không vừa với tôi."*
    * `accepted_answers`: `["mir"]`
    * Giải thích: `passen` + Dativ → **`mir`**.
57. **Câu 57**:
    * `audio_text`: *"Welchen Hut möchten Sie? Diesen hier."*
    * `display_sentence`: *"Welchen Hut möchten Sie? ___ hier."*
    * `hint_vi`: *"Ngài muốn chiếc mũ nào? Chiếc này đây."*
    * `accepted_answers`: `["diesen"]`
    * Giải thích: `der Hut` (m, Akk) → **`Diesen`**.
58. **Câu 58**:
    * `audio_text`: *"Im Sommer ist es in Vietnam oft sehr heiß."*
    * `display_sentence`: *"Im Sommer ist es in Vietnam oft sehr ___."*
    * `hint_vi`: *"Vào mùa hè ở Việt Nam trời thường rất nóng."*
    * `accepted_answers`: `["heiß", "heiss"]`
    * Giải thích: `die Hitze` → tính từ **`heiß`**.

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (`dich_cau_vd` — 5 Câu: Câu 59 → Câu 63, chấm đa đáp án)
59. **Câu 59**: Dịch câu sau sang tiếng Đức: ***"Hôm nay tôi mặc một chiếc quần màu đen."***
    * `accepted_answers`:
      * `"Heute trage ich eine schwarze Hose."`
      * `"Ich trage heute eine schwarze Hose."`
    * Giải thích: `die Hose` giống cái → **`eine schwarze Hose`**; `heute` đứng đầu câu thì `trage` ở vị trí ②.
60. **Câu 60**: Dịch câu sau sang tiếng Đức: ***"Cô ấy mua một chiếc áo sơ mi trắng."***
    * `accepted_answers`:
      * `"Sie kauft ein weißes Hemd."`
      * `"Sie kauft ein weisses Hemd."`
    * Giải thích: `das Hemd` giống trung → **`ein weißes Hemd`**.
61. **Câu 61**: Dịch câu sau sang tiếng Đức: ***"Tôi lấy chiếc mũ này."***
    * `accepted_answers`:
      * `"Ich nehme diesen Hut."`
      * `"Diesen Hut nehme ich."`
    * Giải thích: `der Hut` (m, Akk) → **`diesen Hut`**.
62. **Câu 62**: Dịch câu sau sang tiếng Đức: ***"Chiếc áo khoác này rất hợp với bạn."***
    * `accepted_answers`:
      * `"Diese Jacke steht dir sehr gut."`
      * `"Diese Jacke steht dir gut."`
    * Giải thích: `die Jacke` → **`Diese Jacke`**; *"hợp"* = `stehen` + Dativ **`dir`**.
63. **Câu 63**: Dịch câu sau sang tiếng Đức: ***"Hôm nay ở chỗ tôi trời nắng, nhưng ở chỗ bạn trời mưa."***
    * `accepted_answers`:
      * `"Bei mir ist es heute sonnig, aber bei dir regnet es."`
      * `"Heute ist es bei mir sonnig, aber bei dir regnet es."`
    * Giải thích: `bei mir / bei dir` (`bei` + Dativ); `Es ist sonnig` (tính từ) và `Es regnet` (động từ).

---

#### NHÓM 10: DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (`dich_cau_dv` — 5 Câu: Câu 64 → Câu 68, chấm đa đáp án)
64. **Câu 64**: Dịch câu sau sang tiếng Việt: ***„Welche Größe haben Sie? — Ich trage Größe vierzig.“***
    * `accepted_answers`:
      * `"Ngài mặc cỡ nào? — Tôi mặc cỡ bốn mươi."`
      * `"Bạn mặc cỡ nào? — Tôi mặc cỡ bốn mươi."`
    * Giải thích: `Welche Größe` (f, Akk); `tragen` ở đây nghĩa *"mặc (cỡ)"*.
65. **Câu 65**: Dịch câu sau sang tiếng Việt: ***„Dieser Mantel ist mir zu groß, aber dieser hier passt mir gut.“***
    * `accepted_answers`:
      * `"Chiếc áo măng tô này rộng quá đối với tôi, nhưng chiếc này đây thì vừa với tôi."`
      * `"Chiếc áo măng tô này tôi mặc rộng quá, nhưng chiếc này đây vừa với tôi."`
    * Giải thích: `dieser` (Nominativ, m); `zu groß` = rộng quá; `passen` + Dativ `mir`.
66. **Câu 66**: Dịch câu sau sang tiếng Việt: ***„Im Winter trägt mein Vater immer einen Mantel, einen Hut und Handschuhe.“***
    * `accepted_answers`:
      * `"Vào mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay."`
      * `"Mùa đông bố tôi luôn mặc áo măng tô, đội mũ và đeo găng tay."`
    * Giải thích: `tragen` dùng cho *mặc, đội, đeo*; `immer` = luôn luôn.
67. **Câu 67**: Dịch câu sau sang tiếng Việt: ***„Heute ist es in Hamburg windig und bewölkt, aber morgen scheint die Sonne.“***
    * `accepted_answers`:
      * `"Hôm nay ở Hamburg trời có gió và nhiều mây, nhưng ngày mai trời sẽ nắng."`
      * `"Hôm nay ở Hamburg có gió và nhiều mây, nhưng ngày mai mặt trời sẽ chiếu sáng."`
    * Giải thích: `windig`, `bewölkt` (tính từ); `scheint die Sonne` = trời nắng.
68. **Câu 68**: Dịch câu sau sang tiếng Việt: ***„Welche Jacke gefällt dir besser? — Diese hier gefällt mir besser.“***
    * `accepted_answers`:
      * `"Chiếc áo khoác nào bạn thích hơn? — Chiếc này đây tôi thích hơn."`
      * `"Bạn thích chiếc áo khoác nào hơn? — Tôi thích chiếc này đây hơn."`
    * Giải thích: `gefallen` + Dativ (`dir`, `mir`); `besser` = Komparativ của `gut`; `Diese hier` đứng một mình.

---

#### NHÓM 11: SẮP XẾP TỪ THÀNH CÂU (`sap_xep_cau` — 5 Câu: Câu 69 → Câu 73)
69. **Câu 69**
    * `tokens` (đã xáo trộn): `[trägt, Heute, einen blauen Anzug, er]`
    * `accepted_answers`: `["Heute trägt er einen blauen Anzug.", "Er trägt heute einen blauen Anzug."]`
    * Dịch nghĩa câu: *„Hôm nay anh ấy mặc một bộ com lê xanh.“*
    * Giải thích: Động từ `trägt` ở vị trí ②; nếu `Heute` đứng đầu thì chủ ngữ `er` đứng sau động từ.
70. **Câu 70**
    * `tokens`: `[nimmst, Welchen Pullover, du]`
    * `accepted_answers`: `["Welchen Pullover nimmst du?"]`
    * Dịch nghĩa câu: *„Bạn lấy chiếc áo len nào?“*
    * Giải thích: `Welchen Pullover` ở vị trí ① (`der Pullover`, m, Akk), động từ `nimmst` ở vị trí ②.
71. **Câu 71**
    * `tokens`: `[kaufe, Ich, diesen Gürtel]`
    * `accepted_answers`: `["Ich kaufe diesen Gürtel.", "Diesen Gürtel kaufe ich."]`
    * Dịch nghĩa câu: *„Tôi mua chiếc thắt lưng này.“*
    * Giải thích: `diesen Gürtel` (m, Akk); nếu đứng đầu câu thì `kaufe` vẫn ở vị trí ② rồi mới đến `ich`.
72. **Câu 72** *(Dativ — không có màu)*
    * `tokens`: `[passen, Die Schuhe, mir, leider, nicht]`
    * `accepted_answers`: `["Die Schuhe passen mir leider nicht.", "Leider passen mir die Schuhe nicht."]`
    * Dịch nghĩa câu: *„Tiếc là đôi giày không vừa với tôi.“*
    * Giải thích: `passen` + Dativ `mir`; `nicht` đứng cuối câu.
73. **Câu 73** *(thời tiết)*
    * `tokens`: `[schneit, es, in Berlin, heute]`
    * `accepted_answers`: `["Heute schneit es in Berlin.", "In Berlin schneit es heute.", "Es schneit heute in Berlin."]`
    * Dịch nghĩa câu: *„Hôm nay ở Berlin tuyết rơi.“*
    * Giải thích: Động từ thời tiết `schneit` + `es`; trạng ngữ đứng đầu thì `schneit` vẫn ở vị trí ②.

---

#### NHÓM 12: PHÂN LOẠI `DER / DIE / DAS` (`phan_loai_giong` — 3 Câu: Câu 74 → Câu 76)
Mỗi câu: xếp **4 danh từ** vào đúng mạo từ. Đúng khi cả 4 đều đúng.
74. **Câu 74**: Xếp các danh từ sau:
    * `Mantel` (áo măng tô) → **der** (`der Mantel`)
    * `Hose` (quần) → **die** (`die Hose`)
    * `Kleid` (đầm) → **das** (`das Kleid`)
    * `Gürtel` (thắt lưng) → **der** (`der Gürtel`)
    * Giải thích: `Mantel`, `Gürtel` giống đực; `Hose` giống cái (đuôi `-e`); `Kleid` giống trung.
75. **Câu 75**: Xếp các danh từ sau:
    * `Bluse` (áo sơ mi nữ) → **die** (`die Bluse`)
    * `Hemd` (áo sơ mi nam) → **das** (`das Hemd`)
    * `Schuh` (giày) → **der** (`der Schuh`)
    * `Krawatte` (cà vạt) → **die** (`die Krawatte`)
    * Giải thích: `Bluse`, `Krawatte` giống cái (đuôi `-e`); `Hemd` giống trung; `Schuh` giống đực.
76. **Câu 76**: Xếp các danh từ sau (thời tiết):
    * `Regen` (mưa) → **der** (`der Regen`)
    * `Sonne` (mặt trời) → **die** (`die Sonne`)
    * `Wetter` (thời tiết) → **das** (`das Wetter`)
    * `Nebel` (sương mù) → **der** (`der Nebel`)
    * Giải thích: `Regen`, `Nebel` giống đực; `Sonne` giống cái; `Wetter` giống trung.

---

#### NHÓM 13: 🆕 PHÂN LOẠI AKKUSATIV / DATIV (`phan_loai_cach` — 4 Câu: Câu 77 → Câu 80)
Mỗi hàng là **một câu**; xác định cụm **in đậm** thuộc **Akkusativ** hay **Dativ**. Đúng khi cả 4 hàng đúng. *(Mỗi câu tuân thủ R1–R4: câu có màu chỉ có Akkusativ.)*
77. **Câu 77**
    * Hàng 1: *„Ich trage **einen Mantel**.“* → **Akkusativ** *(`tragen` + tân ngữ trực tiếp; m → `einen`)* — Dịch: *Tôi mặc một chiếc áo măng tô.*
    * Hàng 2: *„Der Hut passt **dir**.“* → **Dativ** *(`passen` + Dativ)* — Dịch: *Chiếc mũ vừa với bạn.*
    * Hàng 3: *„Sie sucht **eine Hose**.“* → **Akkusativ** *(`suchen` + Akk; f → `eine`)* — Dịch: *Cô ấy tìm một chiếc quần.*
    * Hàng 4: *„Die Jacke gefällt **ihm**.“* → **Dativ** *(`gefallen` + Dativ)* — Dịch: *Chiếc áo khoác làm anh ấy thích.*
    * Giải thích: Tân ngữ của `tragen / suchen` là **Akkusativ**; người sau `passen / gefallen` là **Dativ**.
78. **Câu 78**
    * Hàng 1: *„Wir kaufen **diesen Pullover**.“* → **Akkusativ** *(`kaufen` + Akk; m → `diesen`)* — Dịch: *Chúng tôi mua chiếc áo len này.*
    * Hàng 2: *„Die Stiefel stehen **mir** gut.“* → **Dativ** *(`stehen` + Dativ)* — Dịch: *Đôi bốt rất hợp với tôi.*
    * Hàng 3: *„Er zieht **einen Anzug** an.“* → **Akkusativ** *(`anziehen` + Akk)* — Dịch: *Anh ấy mặc một bộ com lê vào.*
    * Hàng 4: *„Das Kleid gehört **meiner Schwester**.“* → **Dativ** *(`gehören` + Dativ; f → `meiner`)* — Dịch: *Chiếc đầm này là của chị tôi.*
    * Giải thích: `kaufen / anziehen` + Akkusativ; `stehen / gehören` + Dativ.
79. **Câu 79** *(màu chỉ nằm ở hàng Akkusativ)*
    * Hàng 1: *„Ich trage **einen schwarzen Rock**.“* → **Akkusativ** *(m → `einen … -en`)* — Dịch: *Tôi mặc một chiếc chân váy đen.*
    * Hàng 2: *„Du nimmst **ein blaues Hemd**.“* → **Akkusativ** *(`nehmen` + Akk; n → `ein … -es`)* — Dịch: *Bạn lấy một chiếc áo sơ mi xanh.*
    * Hàng 3: *„Der Gürtel passt **uns** nicht.“* → **Dativ** *(`passen` + Dativ)* — Dịch: *Chiếc thắt lưng không vừa với chúng tôi.*
    * Hàng 4: *„Der Schal gehört **ihr**.“* → **Dativ** *(`gehören` + Dativ)* — Dịch: *Chiếc khăn quàng là của cô ấy.*
    * Giải thích: Hai hàng có màu là **Akkusativ** (tân ngữ của `tragen / nehmen`); hai hàng **Dativ** (`passen / gehören`) không có màu.
80. **Câu 80**
    * Hàng 1: *„Ich schenke **meinem Bruder** einen Gürtel.“* → **Dativ** *(người nhận; m → `meinem`)* — Dịch: *Tôi tặng anh trai tôi một chiếc thắt lưng.*
    * Hàng 2: *„Ich schenke meinem Bruder **einen Gürtel**.“* → **Akkusativ** *(vật được tặng; m → `einen`)* — Dịch: *Tôi tặng anh trai tôi một chiếc thắt lưng.*
    * Hàng 3: *„Wie gefällt **euch** der Hut?“* → **Dativ** *(`gefallen` + Dativ)* — Dịch: *Các bạn thấy chiếc mũ này thế nào (có thích không)?*
    * Hàng 4: *„Sie probiert **eine Jacke** an.“* → **Akkusativ** *(`anprobieren` + Akk; f → `eine`)* — Dịch: *Cô ấy thử một chiếc áo khoác.*
    * Giải thích: Với `schenken` — **người nhận = Dativ**, **vật = Akkusativ**.

---

#### NHÓM 14: TÌM LỖI VÀ SỬA CÂU (`tim_loi_sai` — 5 Câu: Câu 81 → Câu 85)
Mỗi câu có **đúng 1 lỗi**. Người học gõ lại **cả câu đúng**.
81. **Câu 81** *(lỗi đuôi tính từ màu)*
    * `wrong_sentence`: *„Ich trage einen rote Pullover.“*
    * `accepted_answers`: `["Ich trage einen roten Pullover."]`
    * Dịch nghĩa câu đúng: *„Tôi mặc một chiếc áo len đỏ.“*
    * Giải thích: Lỗi **đuôi tính từ**: `der Pullover` giống đực, Akkusativ → **`roten`** (đuôi `-en`), không phải `rote`.
82. **Câu 82** *(lỗi màu bất biến)*
    * `wrong_sentence`: *„Sie trägt eine rosane Bluse.“*
    * `accepted_answers`: `["Sie trägt eine rosa Bluse."]`
    * Dịch nghĩa câu đúng: *„Cô ấy mặc một chiếc áo sơ mi nữ màu hồng.“*
    * Giải thích: Màu **`rosa` bất biến**, không thêm đuôi → **`eine rosa Bluse`**.
83. **Câu 83** *(lỗi `dies-`)*
    * `wrong_sentence`: *„Ich kaufe dieser Hose.“*
    * `accepted_answers`: `["Ich kaufe diese Hose."]`
    * Dịch nghĩa câu đúng: *„Tôi mua chiếc quần này.“*
    * Giải thích: `die Hose` giống cái, Akkusativ → **`diese`** (không phải `dieser`).
84. **Câu 84** *(lỗi đại từ Dativ)*
    * `wrong_sentence`: *„Die Jacke gefällt ich sehr.“*
    * `accepted_answers`: `["Die Jacke gefällt mir sehr."]`
    * Dịch nghĩa câu đúng: *„Chiếc áo khoác này tôi rất thích.“*
    * Giải thích: `gefallen` + **Dativ** → **`mir`**, không phải `ich`.
85. **Câu 85** *(lỗi động từ thời tiết)*
    * `wrong_sentence`: *„Es ist regnet heute.“*
    * `accepted_answers`: `["Es regnet heute."]`
    * Dịch nghĩa câu đúng: *„Hôm nay trời mưa.“*
    * Giải thích: `regnen` là động từ nên nói **`Es regnet`** (không có `ist`).

---

#### NHÓM 15: 🆕 VIẾT LẠI VỚI `DIES-` (`viet_lai_dies` — 5 Câu: Câu 86 → Câu 90)
86. **Câu 86**
    * `source_sentence`: *„Ich nehme den Rock.“*
    * `instruction_vi`: *Thay `den Rock` bằng `dies-` kèm danh từ.*
    * `accepted_answers`: `["Ich nehme diesen Rock."]`
    * Dịch nghĩa câu đáp án: *„Tôi lấy chiếc chân váy này.“*
    * Giải thích: `den Rock` (m, Akk) → **`diesen Rock`**.
87. **Câu 87**
    * `source_sentence`: *„Sie kauft die Bluse.“*
    * `instruction_vi`: *Thay `die Bluse` bằng `dies-` kèm danh từ.*
    * `accepted_answers`: `["Sie kauft diese Bluse."]`
    * Dịch nghĩa câu đáp án: *„Cô ấy mua chiếc áo sơ mi nữ này.“*
    * Giải thích: `die Bluse` (f) → **`diese Bluse`**.
88. **Câu 88**
    * `source_sentence`: *„Wir suchen das Hemd.“*
    * `instruction_vi`: *Thay `das Hemd` bằng `dies-` kèm danh từ.*
    * `accepted_answers`: `["Wir suchen dieses Hemd."]`
    * Dịch nghĩa câu đáp án: *„Chúng tôi tìm chiếc áo sơ mi nam này.“*
    * Giải thích: `das Hemd` (n) → **`dieses Hemd`**.
89. **Câu 89**
    * `source_sentence`: *„Ich kaufe den Gürtel.“*
    * `instruction_vi`: *Dùng `dies-` đứng một mình (bỏ danh từ).*
    * `accepted_answers`: `["Ich kaufe diesen."]`
    * Dịch nghĩa câu đáp án: *„Tôi mua cái này.“*
    * Giải thích: `den Gürtel` (m, Akk) → đứng một mình là **`diesen`**.
90. **Câu 90**
    * `source_sentence`: *„Du probierst die Schuhe an.“*
    * `instruction_vi`: *Dùng `dies-` đứng một mình (bỏ danh từ), giữ động từ tách.*
    * `accepted_answers`: `["Du probierst diese an."]`
    * Dịch nghĩa câu đáp án: *„Bạn thử đôi này.“*
    * Giải thích: `die Schuhe` (số nhiều) → **`diese`**; động từ tách `probierst … an` đưa tiền tố `an` về cuối câu.

---

#### NHÓM 16: ĐỌC HIỂU ĐÚNG / SAI — RICHTIG / FALSCH (`dung_sai` — 3 Câu: Câu 91 → Câu 93)
**Đoạn văn A** *(trang phục có màu — chỉ ở Akkusativ)*:
> *„Lena geht heute auf eine Party. Sie trägt ein schwarzes Kleid, eine graue Jacke und rote Schuhe. Lenas Bruder Tom trägt einen dunkelblauen Anzug und eine gelbe Krawatte.“*
> **Dịch**: *„Hôm nay Lena đi dự một bữa tiệc. Cô ấy mặc một chiếc đầm đen, một chiếc áo khoác xám và đi giày đỏ. Tom, anh trai của Lena, mặc một bộ com lê xanh đậm và thắt một chiếc cà vạt vàng.“*

91. **Câu 91**: Mệnh đề: *„Lena trägt rote Schuhe.“*
    * Đáp án: **Richtig (Đúng)**
    * Dịch nghĩa mệnh đề: *„Lena đi giày đỏ.“*
    * Giải thích: Đoạn văn viết *„Sie trägt ein schwarzes Kleid, eine graue Jacke und rote Schuhe.“* — Lena đi **giày đỏ**.
92. **Câu 92**: Mệnh đề: *„Tom trägt eine blaue Krawatte.“*
    * Đáp án: **Falsch (Sai)**
    * Dịch nghĩa mệnh đề: *„Tom thắt một chiếc cà vạt xanh.“*
    * Giải thích: Đoạn văn viết *„… einen dunkelblauen Anzug und eine gelbe Krawatte.“* — **bộ com lê** xanh đậm, còn **cà vạt màu vàng**, không phải xanh.

**Đoạn văn B** *(bản tin thời tiết)*:
> *„In Wien ist es heute kalt und neblig. Es sind nur zwei Grad. Morgen scheint die Sonne, aber es bleibt kalt.“*
> **Dịch**: *„Hôm nay ở Wien trời lạnh và có sương mù. Chỉ có hai độ. Ngày mai trời nắng, nhưng vẫn lạnh.“*  *(Khi đọc `🔊`, `2` được đọc là `zwei Grad`.)*

93. **Câu 93**: Mệnh đề: *„Morgen regnet es in Wien.“*
    * Đáp án: **Falsch (Sai)**
    * Dịch nghĩa mệnh đề: *„Ngày mai ở Wien trời mưa.“*
    * Giải thích: Đoạn văn viết *„Morgen scheint die Sonne, aber es bleibt kalt.“* — ngày mai **trời nắng**, không mưa.

---

#### NHÓM 17: SẮP XẾP HỘI THOẠI (`hoi_thoai_sap_xep` — 3 Câu: Câu 94 → Câu 96)
Mỗi ô là **một lượt lời** (kèm nhãn người nói). Người học bấm theo đúng thứ tự.
94. **Câu 94** *(tình huống: tìm áo len)*
    * `lines` (thứ tự đúng — web phải xáo trộn khi hiển thị):
      1. **Verkäuferin**: *„Guten Tag! Suchen Sie etwas Bestimmtes?“* — Xin chào! Ngài tìm món nào cụ thể không ạ?
      2. **Kunde**: *„Ja, ich suche einen Pullover.“* — Có, tôi tìm một chiếc áo len.
      3. **Verkäuferin**: *„Welche Größe haben Sie?“* — Ngài mặc cỡ nào?
      4. **Kunde**: *„Ich trage Größe achtundvierzig.“* — Tôi mặc cỡ bốn mươi tám.
      5. **Verkäuferin**: *„Diesen hier haben wir in achtundvierzig. Wollen Sie ihn anprobieren?“* — Chiếc này đây chúng tôi có cỡ bốn mươi tám. Ngài có muốn thử không?
      6. **Kunde**: *„Ja, gern. Wo ist die Umkleidekabine?“* — Vâng, rất sẵn lòng. Phòng thử đồ ở đâu?
    * `correct_order`: `[1, 2, 3, 4, 5, 6]`
    * Giải thích: Chào hỏi → nêu nhu cầu → hỏi cỡ → nói cỡ → đề nghị thử → hỏi phòng thử đồ.
95. **Câu 95** *(tình huống: đổi quần dài quá)*
    * `lines` (thứ tự đúng):
      1. **Kundin**: *„Entschuldigung, ich habe diese Hose anprobiert. Sie passt mir nicht.“* — Xin lỗi, tôi đã thử chiếc quần này. Nó không vừa với tôi.
      2. **Verkäufer**: *„Ist sie zu klein?“* — Nó chật quá phải không ạ?
      3. **Kundin**: *„Nein, sie ist zu lang.“* — Không, nó dài quá.
      4. **Verkäufer**: *„Dann nehmen Sie diese hier. Sie ist kürzer.“* — Vậy bạn lấy chiếc này đây. Nó ngắn hơn.
      5. **Kundin**: *„Danke, die passt mir gut. Die nehme ich.“* — Cảm ơn, chiếc này vừa với tôi. Tôi lấy chiếc này.
      6. **Verkäufer**: *„Das macht neunundvierzig Euro.“* — Tổng cộng là bốn mươi chín euro.
    * `correct_order`: `[1, 2, 3, 4, 5, 6]`
    * Giải thích: Nêu vấn đề → hỏi lý do → trả lời → đề nghị phương án → chấp nhận mua → báo giá. *(Giá `Hose` = 49 € theo bảng giá nguồn.)*
96. **Câu 96** *(tình huống: trò chuyện về thời tiết)*
    * `lines` (thứ tự đúng):
      1. **A**: *„Hallo Mai, wie ist das Wetter bei dir?“* — Chào Mai, thời tiết chỗ bạn thế nào?
      2. **B**: *„Hallo Tim! Bei mir regnet es. Und bei dir?“* — Chào Tim! Chỗ mình trời mưa. Còn chỗ bạn?
      3. **A**: *„Bei uns scheint die Sonne, aber es ist kalt.“* — Chỗ bọn mình trời nắng nhưng lạnh.
      4. **B**: *„Dann brauchst du einen Mantel.“* — Vậy bạn cần một chiếc áo măng tô.
      5. **A**: *„Ja, ich trage auch Handschuhe.“* — Ừ, mình cũng đeo găng tay.
    * `correct_order`: `[1, 2, 3, 4, 5]`
    * Giải thích: Hỏi thời tiết → trả lời và hỏi lại → trả lời → gợi ý trang phục → phản hồi.

---

#### NHÓM 18: 🆕 NHÌN BIỂU TƯỢNG CHỌN CÂU THỜI TIẾT (`bieu_tuong_thoi_tiet` — 4 Câu: Câu 97 → Câu 100)
Hiển thị **biểu tượng lớn** (emoji, có `alt` tiếng Việt); chọn **câu tiếng Đức** đúng. Voice đọc **câu đúng**, không đọc tên emoji.
97. **Câu 97**
    * `weather_icon`: `🌧️` · `icon_alt_vi`: *Mây và mưa*
    * Đáp án: `A. Es regnet.` (Đúng) | `B. Es schneit.` | `C. Es ist neblig.` | `D. Es ist heiß.`
    * Dịch nghĩa câu đúng: *„Trời mưa.“*
    * Giải thích: Biểu tượng mưa ↔ **`Es regnet.`**
98. **Câu 98**
    * `weather_icon`: `❄️` · `icon_alt_vi`: *Bông tuyết*
    * Đáp án: `A. Es regnet.` | `B. Es ist sonnig.` | `C. Es schneit.` (Đúng) | `D. Es ist windig.`
    * Dịch nghĩa câu đúng: *„Tuyết rơi.“*
    * Giải thích: Biểu tượng tuyết ↔ **`Es schneit.`**
99. **Câu 99**
    * `weather_icon`: `🌬️` · `icon_alt_vi`: *Gió thổi*
    * Đáp án: `A. Es ist bewölkt.` | `B. Es ist windig.` (Đúng) | `C. Es gewittert.` | `D. Es ist kalt.`
    * Dịch nghĩa câu đúng: *„Trời có gió.“*
    * Giải thích: Biểu tượng gió ↔ **`Es ist windig.`** (`der Wind → windig`).
100. **Câu 100**
     * `weather_icon`: `☁️` · `icon_alt_vi`: *Mây*
     * Đáp án: `A. Es ist neblig.` | `B. Es ist heiß.` | `C. Es schneit.` | `D. Es ist bewölkt.` (Đúng)
     * Dịch nghĩa câu đúng: *„Trời nhiều mây.“*
     * Giải thích: Biểu tượng mây ↔ **`Es ist bewölkt.`** (`die Wolke → bewölkt`).

---

## PHẦN 4: HỆ THỐNG SINH ĐỀ NGẪU NHIÊN VÔ HẠN & DỮ LIỆU NGUỒN CHUẨN (`SINGLE SOURCE OF TRUTH`)

### 4.1. Mục tiêu & nguyên tắc
Màn hình bài tập (như Bài 9 và Bài 10) có khu vực **"Luyện Phản Xạ Ngẫu Nhiên Không Giới Hạn"** với nút **"Đổi bộ đề ngẫu nhiên mới"**. Bài 11 phải có **đúng cơ chế tương tự** (giữ nguyên cách hoạt động, cách tính EXP và bộ lọc dạng bài như cơ chế hiện có), nhưng **nội dung ngẫu nhiên được sinh bằng các Engine dưới đây**, theo các nguyên tắc:
1. **Một nguồn dữ liệu duy nhất**: mọi câu sinh ra đều lấy từ các bảng ở mục 4.2 (và bảng động từ ở mục 1.1, bảng tính từ so sánh ở Bài 10 khi cần). **Cấm** sinh dạng từ bằng quy tắc suy diễn ngoài các hàm đã đặc tả (ví dụ chỉ được tạo đuôi màu bằng hàm `akk_ending()` của Phụ lục A2).
2. **Đề, đáp án, dịch nghĩa, giải thích và voice cùng sinh ra từ MỘT đối tượng** (`question object`) — không ghép riêng từng phần.
3. **Mỗi bộ đề ngẫu nhiên** gồm 100 câu theo **cùng phân bổ 18 dạng** của mục 3.1; **không có hai câu trùng nhau** trong cùng bộ (so khớp sau khi chuẩn hóa chữ hoa/thường, dấu câu, khoảng trắng); **không trùng với 100 câu cố định** của Bài 11 và **không trùng câu của Bài 8, 9, 10**; khi lỡ trùng phải bốc lại tối đa 20 lần, nếu vẫn trùng thì đổi dạng mẫu câu.
4. **Hạt giống (`seed`)** được lưu cùng bộ đề để tái hiện lỗi.
5. **Mọi câu sinh ra đều phải đi qua `check_color_rules()` (mục 4.4)** — vi phạm R1–R4 thì **bỏ câu và sinh lại**, không bao giờ được hiển thị cho người học.
6. **Mọi Engine đều có test tự động** (Phần 5) và **không sinh câu mơ hồ** (câu có hai đáp án đúng mà `accepted_answers` không liệt kê hết).

### 4.2. DỮ LIỆU NGUỒN CHUẨN (Phụ lục A)
#### A1. `CLOTHES_POOL` — danh từ trang phục (22 danh từ)
Cột `pl_pref`: `Y` = thường dùng ở **số nhiều không mạo từ** khi nói *"mặc / mua / tìm"* (ví dụ `schwarze Schuhe`); `N` = dùng số ít với `ein-`.
| Mạo từ | Danh từ | Số nhiều | `pl_pref` | Nghĩa | Mạo từ | Danh từ | Số nhiều | `pl_pref` | Nghĩa |
| :-: | :--- | :--- | :-: | :--- | :-: | :--- | :--- | :-: | :--- |
| der | Stiefel | Stiefel | Y | bốt | die | Krawatte | Krawatten | N | cà vạt |
| der | Mantel | Mäntel | N | áo măng tô | das | T-Shirt | T-Shirts | N | áo phông |
| der | Pullover | Pullover | N | áo len | das | Hemd | Hemden | N | áo sơ mi nam |
| der | Rock | Röcke | N | chân váy | das | Kleid | Kleider | N | đầm |
| der | Anzug | Anzüge | N | bộ com lê | der | Schal | Schals | N | khăn quàng |
| der | Schuh | Schuhe | Y | giày | die | Mütze | Mützen | N | mũ len |
| der | Gürtel | Gürtel | N | thắt lưng | der | Regenmantel | Regenmäntel | N | áo mưa |
| der | Hut | Hüte | N | mũ | die | Sonnenbrille | Sonnenbrillen | N | kính râm |
| der | Handschuh | Handschuhe | Y | găng tay | die | Jeans | Jeans | Y | quần bò |
| die | Jacke | Jacken | N | áo khoác | die | Socke | Socken | Y | tất |
| die | Hose | Hosen | N | quần | die | Bluse | Blusen | N | áo sơ mi nữ |

> 🔒 **Ràng buộc**: Khi dùng dạng số nhiều với màu (`Y`), **không có mạo từ** và đuôi là **`-e`**; khi dùng `die Jeans` với màu thì dùng số nhiều (`blaue Jeans`).

#### A2. `COLORS` & hàm `akk_ending()`
* **Màu có chia đuôi (`DECLINABLE`)**: `rot, gelb, grün, blau, schwarz, weiß, grau, braun, bunt, violett, hellrot, hellblau, hellgrün, dunkelbraun, dunkelblau, dunkelgrün`.
* **Màu bất biến (`INVARIANT`)**: `orange, lila, rosa, beige, türkis, mint` *(chỉ dùng trong 1 dạng `tim_loi_sai` và bài từ vựng — R5)*.
* **Bảng đuôi Akkusativ sau `ein-`**:
| Giống / số | Mạo từ bất định | Đuôi |
| :--- | :--- | :-: |
| m | einen | `en` |
| f | eine | `e` |
| n | ein | `es` |
| pl | *(không mạo từ)* | `e` |
```python
AKK_ENDING = {"m": "en", "f": "e", "n": "es", "pl": "e"}
INDEF_AKK  = {"m": "einen", "f": "eine", "n": "ein", "pl": ""}

def akk_np(gender, color, noun_form):          # color phải thuộc DECLINABLE
    art = INDEF_AKK[gender]
    return " ".join(x for x in (art, color + AKK_ENDING[gender], noun_form) if x)
# akk_np("m","schwarz","Rock") -> "einen schwarzen Rock"
# akk_np("n","blau","Kleid")   -> "ein blaues Kleid"
# akk_np("pl","braun","Schuhe")-> "braune Schuhe"
```

#### A3. `DIES_ENDINGS` (và `WELCH_ENDINGS` của Bài 10 — cùng bộ đuôi)
| Giống / số | Nominativ | Akkusativ |
| :--- | :--- | :--- |
| der (m) | dieser | diesen |
| die (f) | diese | diese |
| das (n) | dieses | dieses |
| die (PL) | diese | diese |

#### A4. `PRONOUNS` — đại từ nhân xưng
| Nominativ | ich | du | er | sie | es | wir | ihr | sie (PL) | Sie |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Akkusativ | mich | dich | ihn | sie | es | uns | euch | sie | Sie |
| Dativ | mir | dir | ihm | ihr | ihm | uns | euch | ihnen | Ihnen |

#### A5. `DATIV_PATTERNS` — mẫu câu Dativ về trang phục (**không có màu**)
| Mẫu | Công thức | Ví dụ |
| :--- | :--- | :--- |
| `gefallen` | `[Sache Nom] + gefällt/gefallen + [Dativ] + (sehr gut / nicht)` | *Der Pullover gefällt mir sehr.* |
| `passen` | `[Sache Nom] + passt/passen + [Dativ] + (gut / nicht)` | *Die Stiefel passen ihm nicht.* |
| `stehen` | `[Sache Nom] + steht/stehen + [Dativ] + (gut / nicht)` | *Der Hut steht dir gut.* |
| `gehören` | `[Sache Nom] + gehört/gehören + [Dativ]` | *Der Schal gehört meiner Mutter.* |
| `zu + tính từ` | `[Sache Nom] + ist/sind + [Dativ] + zu + {groß, klein, lang, kurz, eng, weit}` | *Die Hose ist mir zu lang.* |
| `schenken/zeigen` | `[Subj] + schenkt/zeigt + [Dativ] + [Akk]` | *Ich schenke ihm einen Gürtel.* |
> Động từ chia theo **chủ ngữ là Sache** (`gefällt` số ít / `gefallen` số nhiều). Tất cả các mẫu Dativ **cấm từ chỉ màu**.

#### A6. `WEATHER` — bảng thời tiết nguồn
| Biểu tượng | Danh từ | Động từ / Tính từ | Câu chuẩn | Dịch |
| :-: | :--- | :--- | :--- | :--- |
| 🌧️ | der Regen | regnen | Es regnet. | Trời mưa. |
| ❄️ | der Schnee | schneien | Es schneit. | Tuyết rơi. |
| 🌬️ | der Wind | windig | Es ist windig. | Trời có gió. |
| 🌫️ | der Nebel | neblig | Es ist neblig. | Trời có sương mù. |
| ☀️ | die Sonne | sonnig | Es ist sonnig. | Trời nắng. |
| ☁️ | die Wolke | bewölkt | Es ist bewölkt. | Trời nhiều mây. |
| 🥶 | die Kälte | kalt | Es ist kalt. | Trời lạnh. |
| 🥵 | die Hitze | heiß | Es ist heiß. | Trời nóng. |
| ⛈️ | das Gewitter | gewittern | Es gewittert. | Có dông. |

#### A7. `CITY_WEATHER` — dữ liệu thời tiết mẫu **cố định** (cho `V5` và Engine E4; *không phải số liệu thật*)
| Thành phố | Thời tiết | Nhiệt độ (°C) | Thành phố | Thời tiết | Nhiệt độ (°C) |
| :--- | :--- | :-: | :--- | :--- | :-: |
| Berlin | bewölkt | 8 | Hà Nội | neblig | 16 |
| Hamburg | regnet + windig | 7 | Hải Phòng | windig | 20 |
| München | sonnig | 12 | Đà Lạt | neblig | 15 |
| Wien | neblig | 4 | Sài Gòn | heiß | 34 |
> Khi sinh câu "thành phố X ấm / lạnh hơn thành phố Y" phải **so sánh đúng theo nhiệt độ ở bảng** (chênh tối thiểu 3 độ).

#### A8. `CLOTHES_PRICE` — bảng giá quần áo mẫu (đơn vị: **cent**)
| Món | Giá | Món | Giá | Món | Giá |
| :--- | :-: | :--- | :-: | :--- | :-: |
| Mantel | 9000 | Hemd | 3500 | Schal | 1900 |
| Jacke | 6500 | Rock | 3200 | Mütze | 1500 |
| Pullover | 3900 | Gürtel | 2500 | Regenschirm | 1200 |
| Hose | 4900 | Hut | 2800 | T-Shirt | 1500 |
| Kleid | 5900 | Krawatte | 2200 | Socken (1 đôi) | 600 |
| Schuhe (1 đôi) | 7900 | Stiefel (1 đôi) | 9900 | Handschuhe (1 đôi) | 1800 |
> Giá mua sắm trong bài tập phải lấy từ bảng; đọc giá bằng `price_to_german()` của Bài 10.

#### A9. Hàm đọc nhiệt độ & cỡ (dùng chung cho `🔊`)
```python
ONES = ["null","ein","zwei","drei","vier","fünf","sechs","sieben","acht","neun","zehn",
        "elf","zwölf","dreizehn","vierzehn","fünfzehn","sechzehn","siebzehn","achtzehn","neunzehn"]
TENS = {20:"zwanzig",30:"dreißig",40:"vierzig",50:"fünfzig",60:"sechzig",70:"siebzig",80:"achtzig",90:"neunzig"}

def num_words(n):                       # 1 <= n <= 99
    if n < 20: return ONES[n]
    t, u = (n // 10) * 10, n % 10
    return TENS[t] if u == 0 else ONES[u] + "und" + TENS[t]

def temp_to_german(t):                  # -50 <= t <= 50
    if t == 0:  return "null Grad"
    if t < 0:   return "minus " + num_words(-t) + " Grad"
    return num_words(t) + " Grad"

def size_to_german(n):                  # cỡ 30..60
    return num_words(n)
```
| Giá trị | Kết quả bắt buộc | Giá trị | Kết quả bắt buộc |
| :-: | :--- | :-: | :--- |
| 0 °C | null Grad | −3 °C | minus drei Grad |
| 1 °C | ein Grad | −15 °C | minus fünfzehn Grad |
| 8 °C | acht Grad | 36 °C | sechsunddreißig Grad |
| 15 °C | fünfzehn Grad | cỡ 38 | achtunddreißig |
| 21 °C | einundzwanzig Grad | cỡ 39 | neununddreißig |
| 28 °C | achtundzwanzig Grad | cỡ 48 | achtundvierzig |

### 4.3. CÁC ENGINE SINH ĐỀ
| Mã | Tên | Sinh ra dạng bài | Đặc tả & ràng buộc (BẮT BUỘC) |
| :-: | :--- | :--- | :--- |
| **E1** | **Farbe-Akkusativ Generator** | `trac_nghiem`, `dien_khuyet`, `dien_duoi_tinh_tu`, `dien_tao_cau`, `nghe_dien`, `dich_cau_vd`, `sap_xep_cau`, `tim_loi_sai` | Chọn 1 trang phục từ **A1** + 1 màu **`DECLINABLE`** từ **A2** (màu `INVARIANT` chỉ dùng cho `tim_loi_sai`). Khung câu **chỉ dùng động từ Akkusativ**: `{trage, trägst, trägt, tragen, tragt} + NP`, `kaufe/kaufst/…`, `suche…`, `nehme/nimmst…`, `brauche…`, `probiere … an`, `zieht … an`, và trạng từ `heute/oft/gern/gestern`. NP tạo bằng **`akk_np()`**. Động từ chia **đúng ngôi** từ bảng 1.1. **Cấm** mọi dấu hiệu Dativ trong câu (xem 4.4). Bản dịch lấy từ mẫu dịch cố định theo khung: *"… mặc / mua / tìm … + <trang phục> + <màu>"* (màu dịch theo bảng 2.1; **không** dịch `Rock` thành *"quần"*). |
| **E2** | **Dativ Generator** | `dien_khuyet`, `trac_nghiem`, `noi_o`, `dien_tao_cau`, `nghe_dien`, `sap_xep_cau`, `tim_loi_sai`, `dich_cau` | Dùng mẫu **A5** với danh từ trang phục từ **A1** (**không màu**), đại từ từ **A4**. Chủ ngữ số ít → `gefällt/passt/steht/gehört`, số nhiều → `gefallen/passen/stehen/gehören`. Người cảm nhận xoay đủ `mir, dir, ihm, ihr, uns, euch, ihnen, Ihnen`. Có thể dùng `dies-` làm chủ ngữ. **Cấm tuyệt đối từ chỉ màu.** |
| **E3** | **Dies- Generator** | `trac_nghiem`, `dien_khuyet`, `viet_lai_dies`, `noi_o`, `dien_tao_cau`, `sap_xep_cau`, `tim_loi_sai` | Chọn 1 trang phục từ **A1** + vai trò (chủ ngữ / tân ngữ) + kiểu dùng (kèm danh từ / đứng một mình / có `hier` hoặc `da`). Dạng `dies-` lấy từ **A3**. Khi **đứng một mình**, đảm bảo danh từ đã được nhắc trong câu trước hoặc đề bài (`Welchen Gürtel nimmst du? — Diesen hier.`). `viet_lai_dies`: nguồn dùng `der/die/das`, đáp án dùng `dies-` (nếu động từ tách thì đặt tiền tố cuối câu). **Không dùng màu trong câu có `dies-` khi câu có Dativ** (R2). |
| **E4** | **Wetter Generator** | `trac_nghiem`, `dien_khuyet`, `nghe_dien`, `dich_cau`, `noi_o`, `bieu_tuong_thoi_tiet`, `dung_sai`, `sap_xep_cau` | Lấy từ **A6** và **A7**. Mẫu: `Es regnet.`, `Es ist {adj}.`, `In {Stadt} ist es {adj}.`, `Es sind {temp_to_german} …`, `Bei {mir/dir/uns/euch} ist es {adj}.`, `Heute scheint die Sonne.`, `Gestern hat es geregnet/geschneit.`, `Bei {Regen/Kälte/Hitze/…} trage ich {NP không màu}.`. So sánh nhiệt độ **đúng theo A7**. `bieu_tuong_thoi_tiet`: 1 đáp án đúng + 3 câu của các hàng khác trong A6 (không trùng nhau). **Không dùng màu trong câu có `bei` / `im`** (R2). |
| **E5** | **Case Classifier** | `phan_loai_cach` | Mỗi hàng sinh từ **một mẫu có siêu dữ liệu** (E1 → cụm Akkusativ; E2 → cụm Dativ; `schenken` → cả hai). Xác định `target_phrase` và `case` từ siêu dữ liệu của mẫu, **không đoán**. Mỗi bộ 4 hàng có **ít nhất 1 Akkusativ và 1 Dativ**. Câu có màu → **chỉ** là câu Akkusativ (không Dativ). |
| **E6** | **Satzstellung Builder** | `sap_xep_cau`, `tim_loi_sai` (lỗi vị trí) | Khung: `[Trạng từ/NP ①] [V ②] [S ③] [phần còn lại]` và biến thể không đảo ngữ; thời tiết: `Heute schneit es in {Stadt}.` / `In {Stadt} schneit es heute.` **`accepted_answers` phải có mọi trật tự hợp lệ.** Token được xáo trộn sao cho **khác** trật tự đúng. |
| **E7** | **Dialogue Orderer** | `hoi_thoai_sap_xep` | Lấy 4 hội thoại ở mục 7.5 (**chỉ dòng Akkusativ mới có màu**) hoặc hội thoại cửa hàng - thời tiết dựng sẵn; xáo trộn lượt lời, đảm bảo thứ tự xáo **khác** thứ tự gốc. Giá lấy từ **A8**. |
| **E8** | **Arena Extension** | Đấu trường | **Thêm** (không thay thế) 15 câu hỏi hỗn hợp của Bài 11 (5 `Farbe + Akkusativ`, 4 `dies-`, 3 Dativ, 3 thời tiết) vào kho Đấu trường, giữ nguyên toàn bộ câu cũ. |

### 4.4. HÀM `check_color_rules()` — BẮT BUỘC CHẠY CHO MỌI CÂU
```python
import re
COLOR_RE = re.compile(r"^(hell|dunkel)?(rot|gelb|grün|gruen|blau|schwarz|weiß|weiss|grau|braun|bunt|violett"
                      r"|orange|lila|rosa|pink|beige|türkis|tuerkis|mint)(e|en|es|er|em)?$", re.I)
DATIV_TOKENS = {"mir","dir","ihm","ihnen","uns","euch","ihr","dem","einem","einer","meinem","meiner",
                "deinem","deiner","seinem","seiner","ihrem","im","am","zum","zur","beim","vom",
                "bei","mit","von","aus","nach","zu"}
DATIV_VERBS  = {"gefällt","gefallen","gefallt","passt","passen","steht","stehen","gehört","gehören",
                "hilft","helfen","helfe","schenke","schenkt","schenken","zeigt","zeigen","zeige"}
BE_FORMS     = {"ist","sind","war","waren","bin","bist","seid"}

def check_color_rules(sentence, is_vocab_only=False):
    toks = re.findall(r"[A-Za-zÄÖÜäöüß\-]+", sentence)
    low  = [t.lower() for t in toks]
    colors = [i for i, t in enumerate(low) if COLOR_RE.match(t)]
    if not colors or is_vocab_only or len(toks) <= 2:
        return []                                   # không có màu → OK; từ vựng thuần túy → OK
    errs = []
    if any(t in DATIV_TOKENS for t in low):  errs.append("R2: có dấu hiệu Dativ (đại từ/mạo từ/giới từ)")
    if any(t in DATIV_VERBS for t in low):   errs.append("R3: có động từ Dativ")
    for i in colors:                                   # R4: màu làm vị ngữ / Nominativ
        if i > 0 and low[i-1] in BE_FORMS:   errs.append("R4: màu làm vị ngữ sau 'sein'")
        if i == len(low) - 1:                errs.append("R4: màu đứng cuối câu (vị ngữ)")
    return errs
```
* **Quy ước**: hàm được gọi cho **từng câu tiếng Đức** (đề bài, đáp án, lựa chọn, lượt lời hội thoại, câu trong đoạn văn của bài tập). Câu có `errs` ≠ `[]` → **không đạt**. Bài từ vựng thuần túy (dịch từ, nối từ - nghĩa) gọi với `is_vocab_only=True`.
* **Ngoại lệ duy nhất**: các câu ở phần **lý thuyết** có nhãn `⚠️ chỉ để đọc hiểu` (câu trên bảng giảng có cả màu và Dativ) **không** đi vào bài tập nên không bị quét.

---

## PHẦN 5: KIỂM THỬ TOÀN DIỆN & QA ZERO-BUG (`verify_lesson11_qa.py`)

> **Yêu cầu bắt buộc**: Sau khi code xong, Antigravity IDE phải **viết và chạy** `verify_lesson11_qa.py` (hoặc `pytest` tương đương), **sửa mọi lỗi** cho đến khi toàn bộ test đạt, rồi **dán báo cáo kết quả** theo mẫu mục 5.5. Không được báo "xong" khi chưa chạy.

### 5.1. Bảng đối chiếu: lỗi cũ → kiểm tra tự động
| # | Lỗi đã từng gặp | Kiểm tra tự động (phải đạt) |
| :-: | :--- | :--- |
| 1 | Dịch sai nghĩa | Với 100% câu: phần dịch không rỗng; bản dịch **chứa từ khóa nghĩa** của loại quần áo / màu / hiện tượng thời tiết (từ điển `KEYWORDS_VI`: `Rock → chân váy`, `Hose → quần`, `Jacke → áo khoác`, `rot → đỏ`, `regnet → mưa` …); câu quá khứ chứa *"đã"*; câu so sánh chứa *"hơn / nhất"*. Rà soát thủ công thêm 30 câu ngẫu nhiên. |
| 2 | Thiếu phần dịch | Quét `lexikon`, `verbs`, đoạn văn, bảng lý thuyết, 100 câu: không còn trường `*_vi` rỗng hoặc `None`. |
| 3 | Dịch / đáp án không liên quan đề | Mỗi câu: `explanation` **chứa chuỗi đáp án đúng** (chuẩn hóa); ghép đáp án vào `display_sentence` → khớp `audio_text` (với `nghe_dien`). |
| 4 | Voice thiếu / sai | Mọi nút `🔊` có `speak_text` không rỗng; `speak_text` **không chứa** `[_→€°\[\]/]`, emoji, ký tự Việt có dấu đặc trưng; nhiệt độ qua `temp_to_german`, cỡ qua `size_to_german`, giá qua `price_to_german`; câu điền khuyết đọc **câu đã điền đủ**. |
| 5 | Ví dụ không khớp thẻ từ | Mỗi thẻ từ vựng: `example_de` chứa **lemma hoặc số nhiều** của thẻ; thẻ động từ: ví dụ chứa một dạng chia của động từ đó. |
| 6 | Giải thích sai đáp án | Kiểm tra chéo: đuôi màu theo A2, `dies-` theo A3, đại từ Dativ theo A4, giống - số nhiều theo A1, bảng chia động từ theo 1.1. |
| 7 | Câu hỏi trùng nhau | `len(set(normalize(q))) == 100`; so sánh thêm với toàn bộ câu của **Bài 8, 9, 10**. |
| 8 | **Màu sắc trong câu Dativ / Nominativ** *(yêu cầu riêng của Bài 11)* | **`test_color_dativ_separation`**: chạy `check_color_rules()` trên **mọi câu tiếng Đức** của 100 câu và **mọi câu của 200 bộ đề ngẫu nhiên** → **0 vi phạm**. |
| 9 | Sai đuôi tính từ màu | **`test_color_endings`**: mọi cụm `ein- + màu + danh từ` / `màu + danh từ số nhiều` trong bài tập khớp hàm `akk_np()` và giống của danh từ theo A1. |
| 10 | Làm hỏng bài cũ | `Zero-Regression Check` mục 5.2. |
| 11 | Số lượng sai | Đúng 100 câu; đúng phân bổ 18 dạng (`10,10,6,6,6,8,6,6,5,5,5,3,4,5,5,3,3,4`); đúng 50 thẻ từ vựng (trừ thẻ trùng) và 20 thẻ động từ (trừ thẻ trùng). |
| 12 | Chip bộ lọc sai thứ tự / sai số | `test_ui_chips_sorted`: 18 chip hiển thị **tăng dần theo STT bảng 3.1**, số trên chip = STT, số lượng trong ngoặc đúng. |

### 5.2. Kiểm tra không phá bài cũ (`Zero-Regression Check`)
1. **Trước khi code**: tạo nhánh `lesson-11`; làm sạch working tree; lưu **băm SHA-256** của toàn bộ file bài cũ (`lessons/a1/seed_a1_b*.py`, `verbs_db.js`, `lexikon_db.js`, `arena_generator.py`) vào `baseline_hashes.json`.
2. **Sau khi code**: so sánh băm. Với `seed_a1_b1…b10.py`: **giữ nguyên 100%**. Với `verbs_db.js`, `lexikon_db.js`, `arena_generator.py`: chỉ được **thêm** dòng (`git diff --numstat`: số dòng xóa = 0).
3. **Kiểm tra giao diện cũ**: mở **Bài 8, 9, 10**, chạy thử mỗi dạng bài (đặc biệt `chon_haben_sein`, `phan_loai_giong`, `hoi_thoai_sap_xep`, `nghe_gia_tien`, `sap_xep_cau`, `tim_loi_sai`, `dung_sai`) → kết quả y như trước; **không có lỗi trong Console**.
4. **Tiến độ người dùng**: tiến độ, EXP, chuỗi ngày, huy hiệu ở các bài cũ **không đổi**.

### 5.3. Danh sách test tự động bắt buộc trong `verify_lesson11_qa.py`
| Nhóm | Test | Mô tả |
| :--- | :--- | :--- |
| **Dữ liệu** | `test_lexikon_counts` | 50 thẻ mới (trừ trùng); mỗi thẻ có `article ∈ {der,die,das}`, `plural` hoặc `nur Singular`, `meaning_vi`, `example_de`, `example_vi`. |
| | `test_lexikon_example_matches` | `example_de` chứa lemma hoặc số nhiều của chính thẻ. |
| | `test_lexikon_gender_whitelist` | Giống của 50 danh từ khớp bảng chuẩn (`der Mantel`, `der Rock`, `die Jacke`, `die Hose`, `das Kleid`, `das Hemd`, `der Regen`, `die Sonne`, `das Gewitter`…). |
| | `test_verbs_present_forms` | 20 động từ: bảng chia 6 ngôi khớp công thức hoặc ngoại lệ đã ghi (`trägst/trägt`, `gefällst/gefällt`, `hilfst/hilft`, `passt`, `schwitzt`); ví dụ chứa dạng chia; nhãn cách (`+ Akk / + Dativ`) đúng. |
| **Engine** | `test_akk_np` | 300 cụm sinh ngẫu nhiên: đuôi khớp bảng A2; màu bất biến không có đuôi. |
| | `test_color_dativ_separation` | Xem 5.1 mục 8 (**0 vi phạm**). |
| | `test_dies_engine` | 500 câu: dạng `dies-` khớp A3; khi đứng một mình có danh từ được nhắc trước; động từ tách đặt tiền tố cuối câu. |
| | `test_dativ_engine` | 500 câu: đại từ Dativ khớp A4; động từ chia theo chủ ngữ `Sache`; **không có từ màu**. |
| | `test_wetter_engine` | 500 câu: khớp A6/A7; so sánh nhiệt độ đúng; nhiệt độ đọc bằng chữ (kết quả không chứa chữ số). |
| | `test_temp_and_size_reader` | Bảng test ở A9 (12 test) + 200 giá trị ngẫu nhiên. |
| | `test_no_duplicates_in_random_set` | 200 bộ đề × 100 câu: không trùng trong bộ, không trùng 100 câu cố định, không trùng Bài 8/9/10. |
| **Bài tập cố định** | `test_100_questions` | Đúng 100 câu; phân bổ 18 dạng đúng; mã câu 1–100 liên tục. |
| | `test_unique_questions` | Không trùng sau chuẩn hóa. |
| | `test_every_question_has_translation_and_explanation` | Không rỗng; giải thích chứa đáp án. |
| | `test_answers_in_accepted_list` | Đáp án hiển thị nằm trong `accepted_answers`; trắc nghiệm có **đúng 1** đáp án đúng; nối ô có đúng 4 cặp. |
| | `test_tts_clean` | Mọi `speak_text` sạch (xem 5.1 mục 4). |
| | `test_color_endings` | Xem 5.1 mục 9. |
| | `test_case_labels` | Với 16 hàng của 4 câu `phan_loai_cach`: nhãn `Akk / Dativ` khớp động từ / giới từ trong câu (`tragen/suchen/kaufen/nehmen/anziehen/anprobieren/schenken(vật)` → Akk; `passen/gefallen/stehen/gehören/schenken(người)` → Dativ). |
| | `test_weather_icon_questions` | 4 câu `bieu_tuong_thoi_tiet`: đúng 1 đáp án đúng, khớp bảng A6; ba đáp án sai khác nhau và khác đáp án đúng. |
| **Giao diện** | `test_ui_18_types_visible` | Bộ lọc hiển thị đủ 18 dạng; nút "Tất cả (100)"; nhãn tab **`Đủ 18 Dạng`**. |
| | `test_ui_chips_sorted` | Chip tăng dần theo STT, số trên chip đúng. |
| | `test_ui_all_audio_buttons` | Click toàn bộ nút `🔊` không lỗi. |
| | `test_ui_lesson_layout` | Trang lý thuyết có đủ thẻ mục 1–9, 6 sơ đồ `V1–V6`, thẻ cuối trang *"Nắm Vững Toàn Bộ Lý Thuyết Bài Học?"* và nút chuyển sang bài tập. |
| **Hồi quy** | `test_zero_regression` | Theo mục 5.2. |

### 5.4. Danh sách kiểm tra thủ công cuối cùng (người thật rà soát)
1. Mở Bài 11, đọc **toàn bộ lý thuyết**: không ô trống, không bản dịch thiếu, không bảng vỡ cột (chú ý các ô có ký tự `|`).
2. Đối chiếu các điểm chuẩn hóa ở mục 6 của "Chỉ thị tối cao": bảng đuôi tính từ **chỉ cột Akkusativ**, màu bất biến, `die Wolke`, `ihr tragt`, hai câu bảng giảng có màu + Dativ **chỉ nằm ở lý thuyết**.
3. Bấm `🔊` ở **mọi** bảng: từ vựng, mẫu câu, hội thoại, đoạn văn, sơ đồ. Nghe thử các câu có nhiệt độ / cỡ / giá: phải đọc *„fünfzehn Grad“*, *„Größe achtunddreißig“*, *„neunzig Euro“*, **không** đọc ký hiệu.
4. **Đọc 100 câu bài tập và kiểm tra bằng mắt quy tắc màu - Dativ**: không câu nào vừa có màu vừa có `mir / dir / ihm / ihnen / Ihnen / bei / im / mit…`; không câu nào có màu ở vị ngữ.
5. Làm thử **một câu mỗi dạng** (18 dạng) ở chế độ đúng và chế độ sai: kiểm tra *Dịch nghĩa* và *Giải thích* khớp đáp án.
6. Làm đủ **100/100**: thanh tiến độ, EXP, huy hiệu, lưu tiến độ sau khi tải lại trang.
7. Bấm **"Đổi bộ đề ngẫu nhiên mới"** ít nhất 10 lần: không câu nào lặp trong cùng bộ; không câu nào vi phạm quy tắc màu - Dativ; thời tiết và nhiệt độ hợp lý.
8. Chuyển sang **Bài 8, 9, 10**: các bài vẫn hoạt động; không đổi nội dung.
9. Thử trên **điện thoại**: bảng cuộn ngang, nút `🔊` bấm được, 6 sơ đồ co giãn đúng, 18 chip bộ lọc xuống dòng gọn.
10. Thử **Dark / Light mode** cho 6 sơ đồ.

### 5.5. Mẫu báo cáo cuối cùng (bắt buộc dán vào phản hồi sau khi làm xong)
```
BÁO CÁO QA BÀI 11
- Số câu hỏi: 100 / 100 (18 dạng: 10,10,6,6,6,8,6,6,5,5,5,3,4,5,5,3,3,4)   [ĐẠT/KHÔNG ĐẠT]
- Câu trùng nhau: 0                                                         [ĐẠT/KHÔNG ĐẠT]
- Thẻ từ vựng thêm mới / bỏ qua vì trùng: X / Y
- Thẻ động từ thêm mới / bỏ qua vì trùng: X / Y
- test_color_dativ_separation: 0 vi phạm (100 câu + 200 bộ ngẫu nhiên)       [ĐẠT/KHÔNG ĐẠT]
- test_color_endings / test_akk_np / test_dies_engine / test_dativ_engine    [ĐẠT/KHÔNG ĐẠT]
- test_wetter_engine / test_temp_and_size_reader                             [ĐẠT/KHÔNG ĐẠT]
- Test TTS sạch (100% nút 🔊)                                                [ĐẠT/KHÔNG ĐẠT]
- Chip bộ lọc tăng dần theo STT, nhãn "Đủ 18 Dạng"                           [ĐẠT/KHÔNG ĐẠT]
- Zero-Regression (băm Bài 1–10, git diff không xóa dòng nào)                [ĐẠT/KHÔNG ĐẠT]
- Giao diện Bài 8, 9, 10 vẫn chạy đúng                                      [ĐẠT/KHÔNG ĐẠT]
- Các lỗi đã phát hiện và đã sửa: (liệt kê)
- Các điểm cần người dùng quyết định: (liệt kê, nếu có)
```

### 5.6. Lưu ý giao diện đã quan sát được ở Bài 10 (khuyến nghị xử lý, KHÔNG làm hỏng bài cũ)
* **Chip bộ lọc ở Bài 10 đang hiển thị sai thứ tự** (`… 10, 12, 14, 11, 13, 15, 16`) và **đánh số không khớp bảng phân bổ**. Bài 11 phải sửa đúng (mục 2.0.1). Với Bài 10: chỉ báo lại và sửa khi người dùng đồng ý.
* **Trang chủ** vẫn ghi cứng *"7 dạng Bài tập"* ở phần giới thiệu chung (đó là câu mô tả chung của hệ thống). Khuyến nghị đổi thành *"nhiều dạng Bài tập"* hoặc tính động — chỉ làm khi người dùng đồng ý, không bắt buộc cho Bài 11.
* **Tên hiển thị của dạng bài mới** theo bảng 3.1; không dùng mã kỹ thuật (`phan_loai_cach`, `viet_lai_dies`) làm nhãn.

---

*Hết đặc tả Bài 11. Nhắc lại ba nguyên tắc cuối cùng cho Antigravity IDE: **(1)** không động chạm bài cũ; **(2)** mọi dữ liệu - đề - đáp án - dịch - giải thích - voice phải sinh từ một nguồn, và **màu sắc chỉ ở Akkusativ, không bao giờ cùng câu với Dativ**; **(3)** chạy kiểm thử và dán báo cáo trước khi báo hoàn thành.*
