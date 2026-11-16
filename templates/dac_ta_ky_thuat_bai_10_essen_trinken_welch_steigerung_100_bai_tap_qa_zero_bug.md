# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 10 (A1) "ESSEN UND TRINKEN - THỰC PHẨM, SO SÁNH HƠN / SO SÁNH NHẤT, TỪ HỎI WELCH-" — TÍCH HỢP SƠ ĐỒ TƯƠNG TÁC, BỘ DỮ LIỆU NGUỒN CHUẨN & 100 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**, **Bài 4**, **Bài 5**, **Bài 6**, **Bài 7**, **Bài 8**, **Bài 9**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này chỉ gồm: **(1)** tạo mới hoàn toàn **Bài 10 (`lessons/a1/seed_a1_b10.py`)** ở vị trí **`lesson_order = 11`** của cấp độ **A1** (vì Bài 1 gồm 2 phần P1, P2 nên số thứ tự hiển thị lệch 1 so với `lesson_order`); **(2)** *cộng dồn thêm* động từ và từ vựng mới của Bài 10 vào 2 chuyên mục tra cứu; **(3)** *mở rộng thêm* (không thay thế) kiến thức Đấu trường tới Bài 10; **(4)** viết và chạy kịch bản kiểm thử toàn diện.
> * **Quy tắc chống ghi đè khi cộng dồn dữ liệu**: Nếu một động từ / danh từ của Bài 10 **đã tồn tại** trong `verbs_db.js` / `lexikon_db.js` từ bài trước (rất có thể đã có `essen`, `trinken`, `kaufen`, `nehmen`, `möchten`, `das Obst`, `das Essen`, `der Salat`...), thì **GIỮ NGUYÊN thẻ cũ, KHÔNG tạo thẻ trùng, KHÔNG sửa thẻ cũ**. Chỉ thêm các mục chưa có (so khớp theo `lemma` + `article`). Báo cáo ở cuối quá trình: *"đã thêm N thẻ mới, bỏ qua M thẻ trùng"*.
> * **Quy tắc chống phá vỡ giao diện cũ (`Zero-Regression for UI`)**: Các dạng bài mới của Bài 10 (xem mục 3.2) phải được làm bằng cách **thêm component mới hoặc tổng quát hóa component có sẵn một cách tương thích ngược** (ví dụ: `chon_haben_sein` của Bài 9 vẫn phải chạy y như cũ). Sau khi code xong, mở lại **Bài 9 và Bài 8** để kiểm tra các dạng bài cũ vẫn hoạt động.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu. Video bài giảng chỉ là tài liệu tham khảo để soạn nội dung.
>
> ---
>
> ### 🎯 2. PHẠM VI KIẾN THỨC & ĐỘ KHÓ (`A1+ SCOPE CONTROL`)
> * **Ba trọng tâm ngữ pháp của Bài 10**: **(1)** Từ hỏi **`Welch-`** (*"... nào?"*) biến đổi theo giống - số - cách (`Nominativ` / `Akkusativ`); **(2)** **So sánh hơn (`Komparativ`) và so sánh nhất (`Superlativ`)** của `viel – mehr – am meisten`, `gern – lieber – am liebsten`, `gut – besser – am besten` cùng cấu trúc `mehr … als`, `viel`, `viele`; **(3)** **Đi mua sắm (`Einkaufen`)**: hỏi - nói món cần mua, hỏi giá, đơn vị đo lường, đọc giá tiền bằng tiếng Đức.
> * **Từ vựng**: 34 danh từ thực phẩm trên bảng giảng (`der / die / das`) + mở rộng thêm nhiều nhóm thực phẩm, đồ uống, đơn vị, cửa hàng.
> * **Ôn tập có chủ đích**: Vì người học đang cần nắm vững **cách chia động từ có quy tắc**, Bài 10 đưa vào lý thuyết và bài tập: chia **Präsens** của động từ có quy tắc và bất quy tắc nhóm `e → i(e)` / `a → ä` (`essen, nehmen, geben, empfehlen, backen, braten`), động từ khuyết `möchten / mögen / dürfen`, và **ôn Perfekt của Bài 9** (`gekauft, gekocht, gegessen, getrunken, gebacken, bestellt, bezahlt, probiert, eingekauft`). Phần ôn Perfekt chỉ chiếm số lượng nhỏ.
> * **Độ khó**: ở mức **bằng Bài 9 hoặc nhỉnh hơn một chút** (có câu so sánh, câu đảo ngữ với `Am meisten / Am liebsten`, câu hỏi `Welch-`, hội thoại mua hàng, đọc giá tiền). **Không** đưa vào bài tập: biến đổi đuôi tính từ trước danh từ (`der billigste Käse`), `Dativ` của `welch-` (chỉ *nhận biết* ⭐), `Konjunktiv II` ngoài cụm cố định `ich hätte gern`, câu phụ `weil / dass / wenn`.
> * **Tên gọi chuẩn**: bảng giảng ghi nhầm tiêu đề cột là *"Imperativ"* — đúng phải là **`Komparativ`** (so sánh hơn). Web **phải dùng đúng thuật ngữ `Komparativ`** và ghi chú *"Imperativ" là thể mệnh lệnh, không liên quan*.
>
> ---
>
> ### 🗺️ 3. YÊU CẦU HÌNH ẢNH MINH HỌA (`VISUAL DIAGRAMS`) CHO BÀI 10
> Antigravity IDE **BẮT BUỘC** xây dựng module **`static/js/essen_svg.js`** (SVG nội tuyến, tương thích Dark/Light mode) gồm **6 sơ đồ** (đặc tả chi tiết ở **mục 2.9**): `V1` Bảng đuôi `Welch-` tương tác; `V2` Lưu đồ chọn `welcher / welchen / welche / welches`; `V3` Bậc thang so sánh `Positiv → Komparativ → Superlativ`; `V4` Khung câu `Am liebsten esse ich …` (vị trí 1-2-3); `V5` Quầy chợ - hội thoại mua hàng tương tác; `V6` Máy đọc giá tiền Euro. Một số câu hỏi bài tập có trường `visual` để hiển thị sơ đồ ngay trên khung câu hỏi.
>
> ---
>
> ### 🔍 4. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI & CHỐNG TRÙNG LẶP (`ZERO-BUG & ZERO-DUPLICATE QA PROTOCOL`)
> Các lỗi sau đã từng xuất hiện trên web và **KHÔNG ĐƯỢC LẶP LẠI**. Mỗi lỗi có một quy tắc kiểm tra cụ thể:
> 1. **Dịch sai nghĩa** → Mọi bản dịch tiếng Việt phải dịch **đúng câu tiếng Đức đã hoàn chỉnh** (đã điền đáp án), đúng thì, đúng ngôi, đúng mức độ so sánh (*"hơn"* ≠ *"nhất"*).
> 2. **Thiếu phần dịch nghĩa** → 100% từ vựng, ví dụ, đoạn văn, bảng lý thuyết và **100 câu hỏi** đều phải có `translation_vi` không rỗng.
> 3. **Dịch / đáp án không liên quan đến đề bài** → Đề bài, hình minh họa, đáp án, dịch nghĩa và giải thích phải cùng sinh ra từ **một đối tượng dữ liệu duy nhất** (`single source of truth`). Mục `Giải thích` bắt buộc **chứa chính chuỗi đáp án đúng**.
> 4. **Voice thiếu / voice sai** → Mọi nút `🔊` phải có và chỉ truyền **chuỗi tiếng Đức sạch** (`de-DE`) vào `speakGerman()`. Không đọc lẫn tiếng Việt, không đọc ký hiệu `___`, `→`, `[1]`, `€`, `/`. **Giá tiền phải được chuyển thành chữ trước khi đọc** (`3,75 €` → *"drei Euro fünfundsiebzig"*), tuyệt đối không để trình đọc tự đọc ký hiệu `€` hoặc dấu phẩy.
> 5. **Ví dụ không khớp thẻ từ vựng** → Thẻ từ nào thì `example_de` phải chứa **đúng dạng từ đó** (số ít hoặc số nhiều của chính thẻ), và `example_vi` phải dịch đúng câu đó.
> 6. **Giải thích sai đáp án** → Giải thích phải khớp đáp án đúng và quy tắc ngữ pháp thật sự (ví dụ: không giải thích `welchen Käse` bằng "vì Käse là giống cái").
> 7. **Chống trùng lặp câu hỏi 100%** → `len(set(normalized_questions)) == 100`. Toàn bộ 100 câu trong Bài 10 là câu **mới sáng tác**, chỉ *tham khảo* ý tưởng từ bảng giảng, **không sao chép** nguyên câu của giáo trình, của Bài 9 hay Bài 8.
> 8. **Đa dạng ngôi & ngữ cảnh** → Câu hỏi dùng đủ `ich, du, er, sie, es, wir, ihr, sie (số nhiều), Sie`, tên riêng, gia đình, nghề nghiệp; bối cảnh Việt Nam (chợ, phở, cơm, trái cây nhiệt đới) lẫn Đức - Áo - Thụy Sĩ.
> 9. **Số liệu giá cả phải nhất quán** → Giá của từng mặt hàng trong bài tập và hội thoại phải lấy từ **bảng giá nguồn `PRICE_TABLE`** (Phần 4); mọi **giỏ hàng có nêu mặt hàng cụ thể** phải có **tổng tiền khớp phép cộng**, tính bằng **số nguyên cent** để không sai số. (Các câu chỉ nghe *"tổng cộng là …"* mà không nêu mặt hàng thì không bị ràng buộc bởi bảng giá.)
> 10. **Không sửa bài cũ** → chạy `Zero-Regression Check` (xem Phần 5).
>
> ---
>
> ### ⚠️ 5. NHỮNG ĐIỂM CẦN CHUẨN HÓA SO VỚI BẢNG VIẾT TRÊN LỚP (ĐỌC KỸ TRƯỚC KHI CODE)
> Bảng giảng được viết tay nên có vài chỗ cần kiểm chứng. Khi đưa lên web cần xử lý như sau để người học **không học sai**:
> 1. **`das Bund` → `das Buch`**: Trong bảng chia `Nominativ / Akkusativ`, ví dụ giống trung được viết giống chữ *"Bund"*. Các câu ví dụ bên cạnh (*"Welches Buch möchten Sie lesen?"*, *"Welches Buch ist neu?"*) cho thấy đó là **`das Buch`** (quyển sách). Web dùng **`das Buch`**. (Lưu ý: `das Bund` là một từ khác — *bó rau*, ví dụ `ein Bund Petersilie` — chỉ giới thiệu ở mục mở rộng, không nhầm với `Buch`.)
> 2. **`der Reis`, không phải `das Reis`**: Bảng từ vựng ghi `s. Reis` (*gạo*). Theo từ điển, **`der Reis`** (giống đực, chỉ số ít). Web dùng **`der Reis`** và có bài tập củng cố giống này. Nếu thẻ cũ nào đó đã có `das Reis` thì **chỉ báo cáo cho người dùng, không tự sửa bài cũ**.
> 3. **`Salami`**: Bảng ghi `r. Salami (s)`. Dạng thông dụng nhất trong từ điển là **`die Salami`** (số nhiều `die Salamis`); một số vùng có thể dùng `der`. Web hiển thị **`die Salami`** kèm ghi chú *"bảng giảng ghi `r.`"*. **Không dùng `Salami` trong bất kỳ bài tập nào kiểm tra giống** (để tránh gây nhầm lẫn).
> 4. **Tiêu đề cột `Imperativ` → `Komparativ`**, và **`Superlativ` = so sánh *nhất*** (bảng ghi dấu viết tắt dễ nhầm với *"hơn"*). Cặp thuật ngữ chuẩn: `Komparativ = so sánh hơn`, `Superlativ = so sánh nhất`.
> 5. **`Welche Dose Cola …?` — danh từ nào quyết định đuôi?** Cụm `Dose Cola` có hai danh từ; đuôi `welch-` luôn theo danh từ **đứng ngay sau nó** (`die Dose` → `welche`), không theo `Cola`. Web phải có ví dụ này kèm giải thích.
> 6. **Bài điền `viel / mehr / mehr … als` trên bảng**: ở câu về *Wurst / Käse*, cô giáo ghi cả `viel` lẫn `mehr` ở cùng một ô (cả hai đều chấp nhận được). Web trình bày: `viel` = *nhiều* (nói chung), `mehr` = *nhiều hơn* (ngầm so sánh). Bài tập **chỉ dùng các câu chỉ có một đáp án đúng rõ ràng**.
> 7. **Đơn vị đo sau số đếm**: `Kilo, Liter, Gramm, Pfund, Stück` **giữ nguyên** (`zwei Kilo Äpfel`, `zwei Liter Milch`); còn `Flasche, Dose, Tüte, Packung` **thêm `-n`** (`zwei Flaschen Bier`, `zwei Dosen Cola`).
> 8. **`kosten` chia theo vật được hỏi giá**: `Was kostet der Salat?` (số ít) nhưng `Wie viel kosten 100 g Käse?` (đại lượng / số nhiều). Web giải thích rõ điều này.
> 9. **`Möhre` = `Karotte`**: hai từ đồng nghĩa; bài tập dịch *"cà rốt"* chấp nhận cả hai, nhưng thẻ chính dùng `die Möhre` theo bảng giảng.

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 → Bài 9 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 10** theo quy tắc chống ghi đè ở mục 1.

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung **20 động từ trọng tâm của Bài 10** (liên quan ăn uống - mua sắm). Với mỗi thẻ: bảng chia **Präsens** 6 ngôi, dòng **Perfekt** (với động từ khuyết thiếu ghi *"—"*), loại động từ, phát âm `de-DE`, và 1 câu ví dụ **chứa đúng động từ đó** kèm dịch nghĩa. Đây cũng là dữ liệu mẫu cho Engine sinh đề.

| # | Động từ (nghĩa) | Loại | Präsens: ich / du / er·sie·es / wir / ihr / sie·Sie | Perfekt | Ví dụ (`🔊 de-DE`) & Dịch |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **essen** *(ăn)* | Bất quy tắc `e → i` | esse / **isst** / **isst** / essen / esst / essen | hat gegessen | *„Zum Frühstück esse ich Brot mit Butter.“* — Vào bữa sáng tôi ăn bánh mì với bơ. |
| 2 | **trinken** *(uống)* | Có quy tắc (Präsens), Partizip bất quy tắc | trinke / trinkst / trinkt / trinken / trinkt / trinken | hat getrunken | *„Meine Kinder trinken jeden Tag Milch.“* — Các con tôi ngày nào cũng uống sữa. |
| 3 | **kaufen** *(mua)* | Có quy tắc | kaufe / kaufst / kauft / kaufen / kauft / kaufen | hat gekauft | *„Wir kaufen Obst und Gemüse auf dem Markt.“* — Chúng tôi mua hoa quả và rau củ ở chợ. |
| 4 | **nehmen** *(lấy, chọn mua)* | Bất quy tắc `e → i`, gốc đổi | nehme / **nimmst** / **nimmt** / nehmen / nehmt / nehmen | hat genommen | *„Heute nehme ich zwei Kilo Kartoffeln.“* — Hôm nay tôi lấy hai ký khoai tây. |
| 5 | **kosten** *(có giá)* | Có quy tắc, chỉ dùng ngôi `es` / `sie` (số nhiều) | es kostet / sie kosten | hat gekostet | *„Wie viel kosten die Erdbeeren?“* — Dâu tây giá bao nhiêu? |
| 6 | **möchten** *(muốn, ước muốn lịch sự)* | Động từ khuyết | möchte / möchtest / möchte / möchten / möchtet / möchten | — | *„Ich möchte ein Stück Kuchen.“* — Tôi muốn một miếng bánh ngọt. |
| 7 | **mögen** *(thích)* | Động từ khuyết, đổi `ö → a` ở số ít | **mag** / **magst** / **mag** / mögen / mögt / mögen | — | *„Magst du Fisch?“* — Bạn có thích cá không? |
| 8 | **dürfen** *(được phép)* | Động từ khuyết, đổi `ü → a` ở số ít | **darf** / **darfst** / **darf** / dürfen / dürft / dürfen | — | *„Darf ich ein Stück probieren?“* — Tôi có được thử một miếng không? |
| 9 | **brauchen** *(cần)* | Có quy tắc | brauche / brauchst / braucht / brauchen / braucht / brauchen | hat gebraucht | *„Ich brauche Zwiebeln und Tomaten.“* — Tôi cần hành tây và cà chua. |
| 10 | **wünschen** *(mong muốn, cần)* | Có quy tắc (gốc `-sch`: `du wünschst`) | wünsche / wünschst / wünscht / wünschen / wünscht / wünschen | hat gewünscht | *„Was wünschen Sie, bitte?“* — Ngài cần gì ạ? |
| 11 | **kochen** *(nấu ăn)* | Có quy tắc | koche / kochst / kocht / kochen / kocht / kochen | hat gekocht | *„Mein Vater kocht gern Fisch.“* — Bố tôi thích nấu cá. |
| 12 | **backen** *(nướng bánh)* | Bất quy tắc `a → ä` ở `du, er` | backe / **bäckst** (cũng `backst`) / **bäckt** (cũng `backt`) / backen / backt / backen | hat gebacken | *„Am Sonntag backe ich einen Kuchen.“* — Chủ nhật tôi nướng một cái bánh. |
| 13 | **braten** *(chiên, rán)* | Bất quy tắc `a → ä` | brate / **brätst** / **brät** / braten / bratet / braten | hat gebraten | *„Er brät Fisch mit Zwiebeln.“* — Anh ấy chiên cá với hành tây. |
| 14 | **schneiden** *(cắt, thái)* | Gốc `-d` → thêm `-e-` ở `du, er, ihr` | schneide / **schneidest** / **schneidet** / schneiden / **schneidet** / schneiden | hat geschnitten | *„Sie schneidet die Tomaten für den Salat.“* — Cô ấy thái cà chua để làm salad. |
| 15 | **schmecken** *(có vị, ngon)* | Có quy tắc | schmecke / schmeckst / schmeckt / schmecken / schmeckt / schmecken | hat geschmeckt | *„Die Suppe schmeckt sehr gut.“* — Món súp rất ngon. |
| 16 | **bestellen** *(gọi món, đặt hàng)* | Có quy tắc, tiền tố `be-` (không `ge-` ở Partizip) | bestelle / bestellst / bestellt / bestellen / bestellt / bestellen | hat bestellt | *„Ich bestelle einen Salat und ein Wasser.“* — Tôi gọi một salad và một nước lọc. |
| 17 | **bezahlen** *(trả tiền)* | Có quy tắc, tiền tố `be-` | bezahle / bezahlst / bezahlt / bezahlen / bezahlt / bezahlen | hat bezahlt | *„Wir bezahlen zusammen.“* — Chúng tôi trả tiền chung. |
| 18 | **geben** *(cho; `es gibt` = có)* | Bất quy tắc `e → i` | gebe / **gibst** / **gibt** / geben / gebt / geben | hat gegeben | *„Heute gibt es Fisch mit Reis.“* — Hôm nay có cá với cơm. |
| 19 | **vergleichen** *(so sánh)* | Có quy tắc ở Präsens, Partizip bất quy tắc, tiền tố `ver-` | vergleiche / vergleichst / vergleicht / vergleichen / vergleicht / vergleichen | hat verglichen | *„Wir vergleichen die Preise.“* — Chúng tôi so sánh giá cả. |
| 20 | **empfehlen** *(giới thiệu, gợi ý)* | Bất quy tắc `e → ie` | empfehle / **empfiehlst** / **empfiehlt** / empfehlen / empfehlt / empfehlen | hat empfohlen | *„Ich empfehle den Fisch.“* — Tôi gợi ý món cá. |

> 📌 **Lưu ý hiển thị**: Các động từ đã có thẻ từ bài trước (`essen, trinken, kaufen, nehmen, möchten, probieren, einkaufen...`) **không tạo thẻ trùng**. Thẻ `möchten / mögen / dürfen` ghi rõ *"Động từ khuyết — Perfekt sẽ học ở A2"*. Phát âm `🔊` luôn đọc **một câu hoàn chỉnh**, không đọc bảng chia.

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung **2 chủ đề lọc mới** với đầy đủ **50 danh từ có mạo từ `der/die/das`, dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng thẻ** (danh từ nào đã có ở bài trước thì **giữ thẻ cũ, không tạo trùng**):

#### Chủ đề A: `Lebensmittel: Rau củ, Trái cây, Thịt & Cá (Bài 10)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **der Käse** | die Käse | phô mai | Der Käse aus der Schweiz schmeckt sehr gut. | Phô mai từ Thụy Sĩ rất ngon. |
| 2 | **der Kuchen** | die Kuchen | bánh ngọt | Meine Oma backt am Sonntag einen Kuchen. | Bà tôi nướng bánh ngọt vào Chủ nhật. |
| 3 | **der Apfel** | die Äpfel | quả táo | Ein Apfel am Tag ist gesund. | Mỗi ngày một quả táo thì tốt cho sức khỏe. |
| 4 | **der Fisch** | die Fische | cá | Am Freitag gibt es Fisch mit Reis. | Thứ Sáu có cá với cơm. |
| 5 | **der Salat** | die Salate | xà lách; món salad | Zum Mittagessen esse ich einen Salat. | Vào bữa trưa tôi ăn một món salad. |
| 6 | **der Schinken** | die Schinken | thịt xông khói, giăm bông | Das Brötchen mit Schinken ist lecker. | Chiếc bánh mì kẹp giăm bông rất ngon. |
| 7 | **der Pfeffer** | *(nur Singular)* | tiêu | Bitte geben Sie mir Salz und Pfeffer. | Làm ơn đưa cho tôi muối và tiêu. |
| 8 | **die Salami** | die Salamis | xúc xích lên men (salami) | Ich esse gern ein Brötchen mit Salami. | Tôi thích ăn bánh mì kẹp salami. |
| 9 | **die Butter** | *(nur Singular)* | bơ | Zum Frühstück esse ich Brot mit Butter. | Vào bữa sáng tôi ăn bánh mì với bơ. |
| 10 | **die Kartoffel** | die Kartoffeln | khoai tây | Die Kartoffel ist sehr billig. | Khoai tây rất rẻ. |
| 11 | **die Tomate** | die Tomaten | cà chua | Die Tomate ist rot und frisch. | Quả cà chua đỏ và tươi. |
| 12 | **die Möhre** | die Möhren | cà rốt | Ich schneide eine Möhre für die Suppe. | Tôi thái một củ cà rốt cho món súp. |
| 13 | **die Erdbeere** | die Erdbeeren | dâu tây | Die Erdbeere ist süß und rot. | Quả dâu tây ngọt và đỏ. |
| 14 | **die Banane** | die Bananen | quả chuối | Die Banane ist gelb. | Quả chuối màu vàng. |
| 15 | **die Orange** | die Orangen | quả cam | Eine Orange hat viel Vitamin C. | Một quả cam có nhiều vitamin C. |
| 16 | **die Wurst** | die Würste | xúc xích | In Deutschland isst man gern Wurst. | Ở Đức người ta thích ăn xúc xích. |
| 17 | **die Birne** | die Birnen | quả lê | Die Birne schmeckt süß. | Quả lê có vị ngọt. |
| 18 | **die Nudel** | die Nudeln | sợi mì, mì | Zum Abendessen koche ich Nudeln. | Bữa tối tôi nấu mì. |
| 19 | **die Paprika** | die Paprikas | ớt chuông | Die Paprika ist heute billig. | Ớt chuông hôm nay rẻ. |
| 20 | **die Ananas** | die Ananas | quả dứa | Die Ananas aus Vietnam ist sehr süß. | Dứa từ Việt Nam rất ngọt. |
| 21 | **die Zwiebel** | die Zwiebeln | hành tây | Ich brauche eine Zwiebel für den Salat. | Tôi cần một củ hành tây cho món salad. |
| 22 | **das Brot** | die Brote | bánh mì | Das Brot ist noch warm. | Bánh mì vẫn còn ấm. |
| 23 | **das Hähnchen** | die Hähnchen | thịt gà | Wir essen heute Hähnchen mit Reis. | Hôm nay chúng tôi ăn thịt gà với cơm. |
| 24 | **das Ei** | die Eier | quả trứng | Zum Frühstück esse ich ein Ei. | Vào bữa sáng tôi ăn một quả trứng. |
| 25 | **das Fleisch** | *(nur Singular)* | thịt | Mein Bruder isst kein Fleisch. | Anh trai tôi không ăn thịt. |

#### Chủ đề B: `Einkaufen: Đồ uống, Đơn vị, Cửa hàng & Món ăn (Bài 10)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 26 | **der Reis** | *(nur Singular)* | gạo, cơm | In Vietnam isst man jeden Tag Reis. | Ở Việt Nam người ta ăn cơm mỗi ngày. |
| 27 | **der Preis** | die Preise | giá cả | Der Preis für den Käse ist hoch. | Giá của loại phô mai này cao. |
| 28 | **der Liter** | die Liter | lít | Ich kaufe zwei Liter Milch. | Tôi mua hai lít sữa. |
| 29 | **der Markt** | die Märkte | chợ | Auf dem Markt ist das Obst frisch. | Ở chợ hoa quả rất tươi. |
| 30 | **der Supermarkt** | die Supermärkte | siêu thị | Der Supermarkt ist bis zwanzig Uhr geöffnet. | Siêu thị mở cửa đến hai mươi giờ. |
| 31 | **der Saft** | die Säfte | nước ép | Zum Frühstück trinke ich ein Glas Saft. | Vào bữa sáng tôi uống một ly nước ép. |
| 32 | **der Kaffee** | die Kaffees | cà phê | Morgens trinke ich einen Kaffee. | Buổi sáng tôi uống một ly cà phê. |
| 33 | **der Joghurt** | die Joghurts | sữa chua | Der Joghurt mit Erdbeeren schmeckt gut. | Sữa chua vị dâu tây rất ngon. |
| 34 | **die Marmelade** | die Marmeladen | mứt | Ich esse gern Brot mit Marmelade. | Tôi thích ăn bánh mì với mứt. |
| 35 | **die Schokolade** | die Schokoladen | sô cô la | Die Schokolade ist sehr süß. | Sô cô la rất ngọt. |
| 36 | **die Milch** | *(nur Singular)* | sữa | Das Baby trinkt Milch. | Em bé uống sữa. |
| 37 | **die Cola** | die Colas | nước cô-ca | Die Cola ist schön kalt. | Cô-ca rất lạnh. |
| 38 | **die Dose** | die Dosen | lon, hộp | Ich kaufe drei Dosen Tomaten. | Tôi mua ba hộp cà chua. |
| 39 | **die Flasche** | die Flaschen | cái chai | Die Flasche Wasser kostet einen Euro. | Chai nước giá một euro. |
| 40 | **die Tüte** | die Tüten | cái túi | Ich brauche eine Tüte für das Obst. | Tôi cần một cái túi cho trái cây. |
| 41 | **die Bäckerei** | die Bäckereien | tiệm bánh mì | In der Bäckerei kaufe ich Brot und Kuchen. | Ở tiệm bánh tôi mua bánh mì và bánh ngọt. |
| 42 | **das Obst** | *(nur Singular)* | hoa quả, trái cây | Auf dem Markt kaufe ich frisches Obst. | Ở chợ tôi mua trái cây tươi. |
| 43 | **das Gemüse** | *(nur Singular)* | rau củ | Das Gemüse ist heute billig. | Rau củ hôm nay rẻ. |
| 44 | **das Eis** | *(nur Singular)* | kem; đá | Im Sommer esse ich gern Eis. | Mùa hè tôi thích ăn kem. |
| 45 | **das Salz** | *(nur Singular)* | muối | Die Suppe braucht noch Salz. | Món súp còn cần thêm muối. |
| 46 | **das Müsli** | die Müslis | ngũ cốc ăn sáng | Zum Frühstück esse ich Müsli mit Milch. | Vào bữa sáng tôi ăn ngũ cốc với sữa. |
| 47 | **das Schnitzel** | die Schnitzel | thịt tẩm bột chiên | Das Schnitzel mit Kartoffeln ist mein Lieblingsessen. | Món thịt tẩm bột chiên với khoai tây là món ăn yêu thích của tôi. |
| 48 | **das Kilo** | die Kilos | ký (kg) | Ein Kilo Äpfel kostet zwei Euro vierzig. | Một ký táo giá hai euro bốn mươi. |
| 49 | **das Bier** | die Biere | bia | Mein Vater trinkt abends ein Bier. | Bố tôi uống một ly bia vào buổi tối. |
| 50 | **das Wasser** | *(nur Singular)* | nước | Ich trinke viel Wasser. | Tôi uống nhiều nước. |

> ✅ **Mẹo quy tắc giống hiển thị trên thẻ**: Danh từ ghép lấy giống của từ cuối (`der Super` + `der Markt` = `der Supermarkt`). Rất nhiều **hoa quả đuôi `-e` là `die`** (`die Banane, die Orange, die Birne, die Erdbeere, die Tomate, die Möhre, die Zwiebel`) — nhưng `der Käse` là ngoại lệ (giống đực). **Nhóm không đếm được, chỉ số ít**: `das Obst, das Gemüse, das Fleisch, der Reis, die Butter, die Milch, das Salz, der Pfeffer, das Wasser`. `der Joghurt` cũng có thể gặp là `das Joghurt`; web dạy **`der Joghurt`** và không dùng nó trong bài tập kiểm tra giống.

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 10: "ESSEN UND TRINKEN — THỰC PHẨM, SO SÁNH, WELCH-"

Bài học thứ 11 trong danh sách Cấp độ A1 (`lesson_order = 11`):
* **Tiêu đề bài học**: `Bài 10: Thực phẩm - So sánh hơn / So sánh nhất - Fragewort: Welch-` *(chủ đề trên bảng: "Essen und Trinken")*
* **Mô tả ngắn**: `Học từ vựng thực phẩm (der Käse, die Banane, das Obst, der Reis...), cách hỏi "... nào?" với Welch- (Welcher Käse? Welchen Käse? Welche Dose? Welches Brot?), so sánh hơn và so sánh nhất (viel – mehr – am meisten; gern – lieber – am liebsten; gut – besser – am besten; billig – billiger – am billigsten), cấu trúc mehr ... als, và kỹ năng đi mua sắm: gọi món, hỏi giá, đơn vị đo, đọc giá tiền Euro, hội thoại ở chợ - siêu thị - tiệm bánh.`
* **Cấu trúc bài**: Học phần 1 (Từ vựng thực phẩm) → 2 (Hương vị, bữa ăn, sở thích) → **3 (Welch- — phần trọng tâm thứ nhất)** → 4 (viel / viele / mehr / mehr … als) → **5 (Komparativ & Superlativ — phần trọng tâm thứ hai)** → 6 (Einkaufen: mua sắm, giá cả) → 7 (Động từ ăn uống - mua sắm & ôn Perfekt) → 8 (Đọc hiểu & phân tích văn bản) → 9 (Bảng tổng hợp & đặc tả sơ đồ SVG).

---

### HỌC PHẦN 1: TỪ VỰNG THỰC PHẨM (`LEBENSMITTEL`)

> 💡 **Cách đọc ký hiệu trên bảng giảng**: `r.` = **der**, `e.` = **die**, `s.` = **das**; trong ngoặc là **số nhiều**; `(-)` = số nhiều **giữ nguyên** hình thức; `(s)`, `(n)`, `(e)`, `(er)`, `(se)` = thêm đuôi đó; `(Sg.)` = chỉ có số ít.

#### 1.1. Bảng từ vựng chính (khớp bảng giảng, đã chuẩn hóa giống) — phân theo 3 giống
| Giống Đực (<span style="color:#3b82f6">**`der`**</span>) | Giống Cái (<span style="color:#f43f5e">**`die`**</span>) | Giống Trung (<span style="color:#10b981">**`das`**</span>) |
| :--- | :--- | :--- |
| • **der Käse** *(Pl: die Käse)*: phô mai<br>• **der Kuchen** *(Pl: die Kuchen)*: bánh ngọt<br>• **der Apfel** *(Pl: die Äpfel)*: quả táo<br>• **der Fisch** *(Pl: die Fische)*: cá<br>• **der Salat** *(Pl: die Salate)*: xà lách; món salad<br>• **der Schinken** *(Pl: die Schinken)*: thịt xông khói<br>• **der Pfeffer** *(nur Sg.)*: tiêu<br>• **der Reis** *(nur Sg.)*: gạo, cơm ⚠️ *bảng giảng ghi `s.` — chuẩn là **der***<br>• **der Joghurt**, **der Saft**, **der Kaffee**... *(mở rộng, xem 1.3)* | • **die Butter** *(nur Sg.)*: bơ<br>• **die Kartoffel** *(Pl: die Kartoffeln)*: khoai tây<br>• **die Tomate** *(Pl: die Tomaten)*: cà chua<br>• **die Möhre** *(Pl: die Möhren)*: cà rốt<br>• **die Erdbeere** *(Pl: die Erdbeeren)*: dâu tây<br>• **die Banane** *(Pl: die Bananen)*: chuối<br>• **die Orange** *(Pl: die Orangen)*: cam<br>• **die Wurst** *(Pl: die W<u>ü</u>rste)*: xúc xích<br>• **die Birne** *(Pl: die Birnen)*: lê<br>• **die Nudel** *(Pl: die Nudeln)*: mì<br>• **die Paprika** *(Pl: die Paprikas)*: ớt chuông<br>• **die Ananas** *(Pl: die Ananas / Ananasse)*: dứa<br>• **die Zwiebel** *(Pl: die Zwiebeln)*: hành tây<br>• **die Marmelade** *(Pl: die Marmeladen)*: mứt<br>• **die Schokolade** *(Pl: die Schokoladen)*: sô cô la<br>• **die Salami** *(Pl: die Salamis)*: xúc xích lên men ⚠️ *bảng ghi `r.`* | • **das Brot** *(Pl: die Brote)*: bánh mì<br>• **das Hähnchen** *(Pl: die Hähnchen)*: thịt gà<br>• **das Ei** *(Pl: die Eier)*: trứng<br>• **das Fleisch** *(nur Sg.)*: thịt<br>• **das Obst** *(nur Sg.)*: hoa quả<br>• **das Gemüse** *(nur Sg.)*: rau củ<br>• **das Eis** *(nur Sg.)*: kem; đá<br>• **das Salz** *(nur Sg.)*: muối<br>• **das Müsli** *(Pl: die Müslis)*: ngũ cốc<br>• **das Schnitzel** *(Pl: die Schnitzel)*: thịt tẩm bột chiên |

> 🔎 **Mẹo nhớ giống (không học vẹt)**:
> * **Hoa quả và rau củ đuôi `-e` thường là `die`**: `die Banane, die Orange, die Birne, die Erdbeere, die Tomate, die Möhre`. Ngoại lệ cần nhớ: **`der Käse`** (đuôi `-e` nhưng giống đực) và **`das Gemüse`** (giống trung).
> * **Đuôi `-chen` luôn là `das`**: `das Hähnchen`, `das Brötchen` (từ chỉ "nhỏ, bé"). **Đuôi `-lein` cũng `das`**.
> * **Đuôi `-ung`, `-heit`, `-keit` luôn là `die`**; đuôi `-er` chỉ người hoặc vật thường `der`.
> * **Nhóm không đếm được** (`das Obst, das Gemüse, das Fleisch, der Reis, das Salz`) **không dùng số nhiều** và **không dùng `ein/eine`**: nói `Ich esse Reis.` chứ không nói `Ich esse einen Reis.`
> * **Quy tắc số nhiều gợi ý**: đuôi `-e` → thêm `-n` (`die Banane → die Bananen`); đuôi `-el`, `-er`, `-en`, `-chen` → giữ nguyên (`die Kuchen`, `das Hähnchen`, `die Schnitzel`); từ nước ngoài thường thêm `-s` (`die Müslis, die Paprikas, die Salamis`).

#### 1.2. Từ khóa "Lebensmittel" và cách nói tần suất (⭐ mở rộng)
* **das Lebensmittel** *(Pl: die Lebensmittel)*: thực phẩm — thường dùng ở **số nhiều** (`Welche Lebensmittel kaufen Sie oft?`).
* **Trạng từ chỉ tần suất** (đứng sau động từ chia): `immer` (luôn luôn) · `oft` (thường) · `manchmal` (thỉnh thoảng) · `selten` (hiếm khi) · `nie` (không bao giờ). Ví dụ (`🔊 de-DE`): *„Ich kaufe oft Obst auf dem Markt.“* — Tôi thường mua hoa quả ở chợ. *„Wir essen selten Fleisch.“* — Chúng tôi hiếm khi ăn thịt.

#### 1.3. Mở rộng ⭐: 40 từ thực phẩm - đồ uống - bữa ăn bổ sung (mỗi từ có `🔊`)
| Nhóm | Từ vựng (mạo từ, số nhiều) & Nghĩa |
| :--- | :--- |
| **Trái cây** | **die Zitrone** *(Zitronen)*: chanh vàng · **die Traube** *(Trauben)*: nho · **die Mango** *(Mangos)*: xoài · **die Kirsche** *(Kirschen)*: anh đào · **die Wassermelone** *(Wassermelonen)*: dưa hấu |
| **Rau củ** | **die Gurke** *(Gurken)*: dưa chuột · **der Knoblauch** *(nur Sg.)*: tỏi · **der Pilz** *(Pilze)*: nấm · **die Bohne** *(Bohnen)*: đậu · **der Mais** *(nur Sg.)*: ngô |
| **Thịt - Cá** | **das Schweinefleisch** *(nur Sg.)*: thịt lợn · **das Rindfleisch** *(nur Sg.)*: thịt bò · **das Hackfleisch** *(nur Sg.)*: thịt băm · **der Lachs** *(Lachse)*: cá hồi · **die Garnele** *(Garnelen)*: tôm |
| **Sữa - Bánh - Gia vị** | **die Sahne** *(nur Sg.)*: kem tươi · **der Quark** *(nur Sg.)*: phô mai tươi (Quark) · **das Brötchen** *(die Brötchen)*: bánh mì nhỏ · **der Zucker** *(nur Sg.)*: đường · **das Mehl** *(nur Sg.)*: bột mì · **das Öl** *(Öle)*: dầu ăn · **der Essig** *(nur Sg.)*: giấm |
| **Đồ uống** | **der Tee** *(Tees)*: trà · **das Mineralwasser** *(nur Sg.)*: nước khoáng · **der Orangensaft** *(Orangensäfte)*: nước cam ép · **die Limonade** *(Limonaden)*: nước chanh có ga · **der Wein** *(Weine)*: rượu vang |
| **Bữa ăn & món** | **das Frühstück** *(Frühstücke)*: bữa sáng · **das Mittagessen** *(Mittagessen)*: bữa trưa · **das Abendessen** *(Abendessen)*: bữa tối · **die Suppe** *(Suppen)*: món súp · **der Nachtisch** *(Nachtische)*: món tráng miệng · **das Lieblingsessen** *(Lieblingsessen)*: món ăn yêu thích |
| **Đơn vị & Đóng gói** | **das Pfund** *(Pfunde)*: nửa ký (500 g) · **das Gramm** *(die Gramm)*: gam · **die Packung** *(Packungen)*: gói, hộp · **das Stück** *(Stücke)*: miếng, cái · **das Glas** *(Gläser)*: ly, lọ · **die Scheibe** *(Scheiben)*: lát · **das Bund** *(Bunde)*: bó (rau) ⚠️ *khác với `das Buch`* |
| **Mua sắm** | **die Kasse** *(Kassen)*: quầy thu ngân · **das Wechselgeld** *(nur Sg.)*: tiền thối · **das Angebot** *(Angebote)*: hàng khuyến mãi · **der Euro** / **der Cent**: đồng euro / xu |

> ⚠️ Với các từ mở rộng, **bài tập chỉ dùng những từ đã có đầy đủ nghĩa - giống - số nhiều trong bảng này** (hoặc bảng 1.1 và Phụ lục A).

---

### HỌC PHẦN 2: HƯƠNG VỊ, BỮA ĂN & SỞ THÍCH (`GESCHMACK, MAHLZEITEN, VORLIEBEN`)

#### 2.1. Tính từ miêu tả đồ ăn (⭐ mở rộng, mỗi từ có `🔊`)
| Tính từ | Nghĩa | Ví dụ (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- | :--- |
| **lecker** | ngon | *„Der Kuchen ist lecker.“* | Chiếc bánh ngọt rất ngon. |
| **süß** | ngọt | *„Die Erdbeeren sind süß.“* | Dâu tây ngọt. |
| **salzig** | mặn | *„Die Suppe ist zu salzig.“* | Món súp quá mặn. |
| **sauer** | chua | *„Die Zitrone ist sauer.“* | Quả chanh vàng chua. |
| **scharf** | cay | *„Die Wurst ist scharf.“* | Cây xúc xích cay. |
| **bitter** | đắng | *„Der Kaffee ist bitter.“* | Cà phê đắng. |
| **frisch** | tươi | *„Der Fisch ist ganz frisch.“* | Con cá còn rất tươi. |
| **gesund** | tốt cho sức khỏe | *„Gemüse ist gesund.“* | Rau củ tốt cho sức khỏe. |
| **billig** / **teuer** | rẻ / đắt | *„Die Tomaten sind billig, aber der Fisch ist teuer.“* | Cà chua rẻ nhưng cá đắt. |
| **kalt** / **warm** / **heiß** | lạnh / ấm / nóng | *„Die Suppe ist heiß.“* | Món súp nóng. |

#### 2.2. Ba bữa ăn chính & cách dùng giới từ `zu` (⭐)
* **das Frühstück** (bữa sáng), **das Mittagessen** (bữa trưa), **das Abendessen** (bữa tối).
* Dùng **`zum`** (= `zu` + `dem`) để nói *"vào bữa …"*: *„**Zum** Frühstück esse ich Müsli.“* — Vào bữa sáng tôi ăn ngũ cốc. *„**Zum** Mittagessen gibt es Reis mit Fisch.“* — Vào bữa trưa có cơm với cá. *„**Zum** Abendessen koche ich Nudeln.“*
* Hỏi: *„Was isst du **zum** Frühstück?“* — Bạn ăn gì vào bữa sáng?

#### 2.3. Nói về món ăn yêu thích và khẩu vị
| Mẫu câu (`🔊 de-DE`) | Dịch |
| :--- | :--- |
| *„Ich esse gern Fisch.“* | Tôi thích ăn cá. |
| *„Ich esse nicht gern Fleisch.“* | Tôi không thích ăn thịt. |
| *„Mein Lieblingsessen ist Schnitzel mit Kartoffeln.“* | Món ăn yêu thích của tôi là thịt tẩm bột chiên với khoai tây. |
| *„Das schmeckt gut / sehr gut / nicht so gut.“* | Món này ngon / rất ngon / không ngon lắm. |
| *„Magst du Käse?“* — *„Ja, sehr. / Nein, nicht so.“* | Bạn có thích phô mai không? — Có, rất thích. / Không, không thích lắm. |
| *„Guten Appetit!“* · *„Mahlzeit!“* | Chúc ngon miệng! · (lời chào / chúc vào giờ ăn) |

---

### HỌC PHẦN 3: ⭐ TỪ HỎI `WELCH-` — "... NÀO?" (TRỌNG TÂM THỨ NHẤT) ⭐

> 🧭 **Bản đồ phần này**: 3.1 Khái niệm → 3.2 Bảng đuôi `Nominativ / Akkusativ` → 3.3 Cách chọn `Nominativ` hay `Akkusativ` → 3.4 Ví dụ & câu trả lời → 3.5 Cụm có hai danh từ (`Welche Dose Cola`) → 3.6 Mẹo - lỗi thường gặp → 3.7 Mở rộng ⭐.

#### 3.1. `Welch-` là gì? (`Das Fragewort "welch-"`)
* **`Welch-` + danh từ = "danh từ đó NÀO?"** — dùng để hỏi **chọn một trong nhiều thứ** cùng loại mà cả hai bên đều biết. *Ví dụ*: trước quầy phô mai có 5 loại, bạn hỏi *„**Welchen** Käse möchten Sie?“* — Ngài muốn loại phô mai **nào**?
* **Đuôi của `welch-` giống hệt đuôi của mạo từ xác định `der / den / die / das`** nên rất dễ nhớ:

| Mạo từ xác định | → | Dạng `welch-` | Quy luật |
| :--- | :-: | :--- | :--- |
| **der** | → | **welcher** | `-er` |
| **den** | → | **welchen** | `-en` |
| **die** (số ít) | → | **welche** | `-e` |
| **das** | → | **welches** | `-es` |
| **die** (số nhiều) | → | **welche** | `-e` |

#### 3.2. Bảng đuôi `Welch-` theo giống - số - cách *(khớp bảng giảng; sơ đồ `V1`)*
| Giống | `Nominativ` (Cách 1) | `Akkusativ` (Cách 4) |
| :--- | :--- | :--- |
| **m** (giống đực) | der Käse → **Welcher** Käse | den Käse → **Welchen** Käse |
| **f** (giống cái) | die Dose → **Welche** Dose | die Dose → **Welche** Dose |
| **n** (giống trung) | das Buch → **Welches** Buch | das Buch → **Welches** Buch |
| **PL** (số nhiều) | die Bananen → **Welche** Bananen | die Bananen → **Welche** Bananen |

> 🔑 **Chỉ giống ĐỰC mới đổi giữa hai cách** (`welcher` ↔ `welchen`). Giống cái, giống trung và số nhiều **giữ nguyên** ở cả hai cách. Đây là điểm quan trọng nhất của bảng.
> 📚 *Lưu ý ví dụ giống trung*: bảng giảng viết `das Buch` (quyển sách) — xem mục chuẩn hóa số 1.

#### 3.3. Chọn `Nominativ` hay `Akkusativ`? (lưu đồ `V2`)
Đuôi `welch-` phụ thuộc **vai trò của cụm danh từ trong câu**:
| Vai trò | Dùng cách | Dấu hiệu nhận biết | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :-: | :--- | :--- |
| **Chủ ngữ** (người / vật *thực hiện* hành động hoặc *được nói đến*) | **Nominativ** | Đi với `sein`, `werden`, `bleiben`; hoặc làm chủ ngữ của `schmecken`, `kosten`, `aussehen`... | *„**Welcher** Fisch ist heute frisch?“* — Con cá nào hôm nay tươi?<br>*„**Welches** Brot schmeckt am besten?“* — Loại bánh mì nào ngon nhất? |
| **Tân ngữ trực tiếp** (cái bị mua, ăn, uống, chọn...) | **Akkusativ** | Đi với `kaufen, nehmen, essen, trinken, möchten, brauchen, probieren, bestellen, empfehlen, mögen, kochen, backen, haben` và `es gibt` | *„**Welchen** Fisch empfehlen Sie?“* — Ngài gợi ý con cá nào?<br>*„**Welches** Brot kaufst du?“* — Bạn mua loại bánh mì nào?<br>*„**Welchen** Salat gibt es heute?“* — Hôm nay có loại salad nào? |

* 🧪 **Mẹo kiểm tra nhanh "thay thế bằng mạo từ"**: Thay `welch-` bằng `der / den` rồi tự đặt câu trả lời.
  * *„Welcher Käse ist lecker?“* → *„**Der** Käse ist lecker.“* → `der` → **Nominativ** → `welcher`.
  * *„Welchen Käse kaufst du?“* → *„Ich kaufe **den** Käse.“* → `den` → **Akkusativ** → `welchen`.
* ⚠️ **Chỉ giống đực mới cần cân nhắc**: nếu danh từ là `die / das / số nhiều`, bạn không cần xác định cách — dùng `welche / welches / welche`.

#### 3.4. Ví dụ đầy đủ — câu hỏi & câu trả lời (mỗi dòng có `🔊`)
| Câu hỏi (`🔊 de-DE`) | Giống · Cách | Dịch | Câu trả lời mẫu |
| :--- | :-: | :--- | :--- |
| *„**Welcher** Kuchen schmeckt am besten?“* | m · Nom | Chiếc bánh nào ngon nhất? | *„Der Kuchen mit Erdbeeren.“* |
| *„**Welchen** Kuchen nimmst du?“* | m · Akk | Bạn lấy chiếc bánh nào? | *„Den Kuchen mit Schokolade.“* |
| *„**Welche** Tomate ist reif?“* | f · Nom | Quả cà chua nào chín? | *„Die Tomate hier.“* |
| *„**Welche** Orange möchtest du?“* | f · Akk | Bạn muốn quả cam nào? | *„Die Orange links.“* |
| *„**Welches** Obst kaufen Sie heute?“* | n · Akk | Hôm nay ngài mua loại hoa quả nào? | *„Das Obst vom Markt.“* |
| *„**Welches** Eis ist am besten?“* | n · Nom | Loại kem nào ngon nhất? | *„Das Eis mit Schokolade.“* |
| *„**Welche** Äpfel sind süß?“* | PL · Nom | Những quả táo nào ngọt? | *„Die Äpfel aus dem Garten.“* |
| *„**Welche** Eier brauchen wir?“* | PL · Akk | Chúng ta cần những quả trứng nào? | *„Die Eier vom Markt.“* |
| *„**Welche** Lebensmittel kaufen Sie oft?“* | PL · Akk | Ngài thường mua những thực phẩm nào? | *„Reis, Obst und Fleisch.“* |

> 💡 **Quy tắc câu trả lời**: Khi trả lời, dùng **mạo từ xác định đúng giống - cách**: `Den Käse, bitte.` (m, Akk), `Die Dose hier.` (f), `Das Brot da.` (n). Có thể trả lời ngắn bằng danh từ không mạo từ: *„Frischkäse, bitte.“*

#### 3.5. ⚠️ Cụm có hai danh từ: `Welche Dose Cola …?` — danh từ nào quyết định đuôi?
Trong cụm *"một lon cô-ca"* có hai danh từ: **`die Dose`** (lon) và **`die Cola`**. **Đuôi `welch-` luôn theo danh từ ĐỨNG NGAY SAU NÓ** — ở đây là `Dose` (giống cái) → **`welche`**.
* *„**Welche** Dose Cola ist billig?“* — Lon cô-ca nào rẻ? *(`die Dose`, Nominativ, giống cái → `welche`)*
* *„**Welche** Flasche Wasser nimmst du?“* — Bạn lấy chai nước nào? *(`die Flasche`, giống cái → `welche`)*
* *„**Welches** Stück Kuchen möchten Sie?“* — Ngài muốn miếng bánh nào? *(`das Stück`, giống trung → `welches`)*
* *„**Welchen** Liter Milch kaufst du?“* — hiếm gặp, nhưng đúng: `der Liter`, Akkusativ → `welchen`.
* ❌ Sai thường gặp: ~~*Welches Dose Cola?*~~ (lấy giống của `Cola`) → ✔ *Welche Dose Cola?*

#### 3.6. 🧰 Mẹo nhớ & MƯỜI lỗi thường gặp (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Dùng `welcher` cho tân ngữ giống đực | ✘ *Welcher Käse möchten Sie?* | ✔ *Welchen Käse möchten Sie?* | `möchten` + tân ngữ → Akkusativ → `den` → `welchen`. |
| 2 | Dùng `welchen` cho chủ ngữ giống đực | ✘ *Welchen Fisch ist frisch?* | ✔ *Welcher Fisch ist frisch?* | Chủ ngữ của `sein` → Nominativ → `welcher`. |
| 3 | Đổi đuôi giống cái theo cách | ✘ *Welchen Dose nimmst du?* | ✔ *Welche Dose nimmst du?* | Giống cái **không đổi**. |
| 4 | Dùng `welche` cho giống trung | ✘ *Welche Obst kaufst du?* | ✔ *Welches Obst kaufst du?* | `das Obst` → `welches`. |
| 5 | Dùng `welches` cho số nhiều | ✘ *Welches Bananen sind billig?* | ✔ *Welche Bananen sind billig?* | Số nhiều luôn `welche`. |
| 6 | Quên danh từ sau `welch-` | ✘ *Welchen möchten Sie?* *(khi chưa nêu danh từ)* | ✔ *Welchen Käse möchten Sie?* | `welch-` thường đi kèm danh từ (trừ khi đã nhắc ngay trước đó). |
| 7 | Lấy giống của danh từ thứ hai | ✘ *Welches Dose Cola?* | ✔ *Welche Dose Cola?* | Theo `Dose`, không theo `Cola`. |
| 8 | Nhầm `welch-` với `wie` | ✘ *Wie Käse möchten Sie?* | ✔ *Welchen Käse möchten Sie?* | `wie` hỏi *như thế nào*, không đi trực tiếp với danh từ. |
| 9 | Dùng sai vị trí động từ | ✘ *Welchen Käse Sie möchten?* | ✔ *Welchen Käse möchten Sie?* | Động từ ở **vị trí thứ 2**; cụm `Welchen Käse` chiếm vị trí 1. |
| 10 | Nhầm giống khi dùng `Reis` | ✘ *Welches Reis kaufst du?* | ✔ *Welchen Reis kaufst du?* | `der Reis` (giống đực, Akk) → `welchen`. |

#### 3.7. Mở rộng ⭐ (chỉ cần nhận biết, không có trong bài tập)
* **`Welch-` sau giới từ — Dativ**: giống đực & trung → **`welchem`**; giống cái → **`welcher`**; số nhiều → **`welchen`**. *„In **welchem** Supermarkt kaufst du ein?“* — Bạn mua sắm ở siêu thị nào? *„Bei **welcher** Bäckerei kaufst du Brot?“* — Bạn mua bánh mì ở tiệm bánh nào? (Dativ sẽ học kỹ ở bài sau.)
* **`Welch-` và `Was für ein-`**: `Welch-` hỏi *"cái nào trong số đã biết"*; `Was für ein-` hỏi *"loại gì, thuộc kiểu nào"*. *„Was für einen Käse möchten Sie?“* — Ngài muốn loại phô mai kiểu gì (mềm, cứng, mặn...)? *(Chỉ nhận biết.)*
* **Dùng độc lập (không danh từ) khi đã rõ**: *„Ich möchte einen Apfel. — **Welchen**?“* — Tôi muốn một quả táo. — Quả nào?

---

### HỌC PHẦN 4: `VIEL`, `VIELE`, `MEHR`, `MEHR … ALS` — NÓI VỀ SỐ LƯỢNG VÀ SO SÁNH SỐ LƯỢNG

#### 4.1. Bảng phân biệt các từ chỉ số lượng
| Từ | Nghĩa | Đi với | Biến đổi? | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- | :---: | :--- |
| **viel** | nhiều | Danh từ **không đếm được**, số ít (`Käse, Obst, Reis, Fleisch, Wasser, Salz`) | Không đổi | *„Wir essen viel Obst.“* — Chúng tôi ăn nhiều hoa quả. |
| **viele** | nhiều | Danh từ **đếm được, số nhiều** (`Äpfel, Eier, Nudeln, Kartoffeln`) | Thêm `-e` | *„Ich kaufe viele Äpfel.“* — Tôi mua nhiều quả táo. |
| **mehr** | nhiều hơn | Cả hai loại danh từ | **Không bao giờ đổi** | *„Er trinkt mehr Wasser.“* / *„Sie isst mehr Eier.“* |
| **wenig** | ít | Danh từ không đếm được | Không đổi | *„Ich esse wenig Fleisch.“* — Tôi ăn ít thịt. |
| **weniger** | ít hơn | Cả hai loại danh từ | Không đổi | *„Wir kaufen weniger Süßigkeiten.“* ⭐ |
| **genug** | đủ | Cả hai loại | Không đổi | *„Wir haben genug Brot.“* ⭐ — Chúng ta có đủ bánh mì. |
| **zu viel** | quá nhiều | Cả hai loại | Không đổi | *„In der Suppe ist zu viel Salz.“* ⭐ — Trong món súp có quá nhiều muối. |

> 🔑 **Mẹo phân biệt `viel` và `viele`**: Thử *đếm* bằng số. Đếm được → `viele` (`zwei Äpfel` → `viele Äpfel`). Không đếm được → `viel` (không nói `zwei Käse` theo nghĩa "khối lượng" → `viel Käse`).

#### 4.2. Cấu trúc `mehr … als` (so sánh số lượng: "nhiều hơn …")
> ### 📐 CÔNG THỨC: &nbsp; **`S + V + mehr + [danh từ A] + als + [danh từ B]`**
* *„In Berlin gibt es mehr Döner-Lokale als in Istanbul.“* — Ở Berlin có nhiều quán Döner hơn ở Istanbul.
* **`als`** = *"hơn so với"* (không dùng `wie` trong so sánh hơn). Danh từ B có thể là cả cụm (`als in Istanbul`, `als die Menschen in Südeuropa`).

#### 4.3. Phân tích bài điền `viel / mehr / mehr … als` trên bảng giảng *(đọc để hiểu cách dùng)*
| # | Câu hoàn chỉnh (`🔊 de-DE`) | Dịch nghĩa | Đáp án trên bảng | Vì sao? |
| :-: | :--- | :--- | :--- | :--- |
| 1 | *„Die Deutschen essen gern Döner. In Berlin gibt es **mehr** Döner-Lokale **als** in Istanbul.“* | Người Đức thích ăn Döner. Ở Berlin có nhiều quán Döner hơn ở Istanbul. | **mehr … als** | So sánh số lượng giữa hai thành phố. |
| 2 | *„In Deutschland und Österreich isst man **viel** Wurst, in der Schweiz **viel** Käse.“* | Ở Đức và Áo người ta ăn nhiều xúc xích, ở Thụy Sĩ ăn nhiều phô mai. | **viel** *(cô giáo ghi thêm `mehr` ở cả hai ô)* | `viel` = nhiều (tuyệt đối); `mehr` cũng chấp nhận được nếu ngầm so sánh với nước khác. |
| 3 | *„Die Menschen in Deutschland, Österreich und in der Schweiz essen **mehr** Kartoffeln **als** die Menschen in Südeuropa.“* | Người dân ở Đức, Áo và Thụy Sĩ ăn khoai tây nhiều hơn người dân Nam Âu. | **mehr … als** | Có đối tượng so sánh (`die Menschen in Südeuropa`). |
| 4 | *„In Deutschland, Österreich und in der Schweiz kocht man **viel** zu Hause.“* | Ở Đức, Áo và Thụy Sĩ người ta nấu ăn nhiều ở nhà. | **viel** | Không có đối tượng so sánh → `viel`. |

> 📘 **Từ mới trong phần này**: **`man`** = *"người ta"* (đại từ chung, chia động từ như `er/sie/es`: *man isst, man kocht, man trinkt*); **`das Lokal`** *(Pl: die Lokale)* = quán, nhà hàng nhỏ; **`gern`** = *"thích"*.

#### 4.4. Mở rộng ⭐: kết hợp `viel` với so sánh
* **`viel` + Komparativ** = *"… hơn rất nhiều"*: *„Fisch ist viel teurer als Reis.“* — Cá đắt hơn gạo rất nhiều. *„Ich esse viel mehr Obst als früher.“* — Tôi ăn nhiều hoa quả hơn trước rất nhiều.
* **`nicht viel` / `nicht so viel`**: *„Ich esse nicht viel Fleisch.“* — Tôi không ăn nhiều thịt.
* **`ein bisschen` / `ein wenig`** = *"một chút"*: *„Ich möchte ein bisschen Salz.“*

---

### HỌC PHẦN 5: ⭐ SO SÁNH HƠN (`KOMPARATIV`) & SO SÁNH NHẤT (`SUPERLATIV`) (TRỌNG TÂM THỨ HAI) ⭐

> 🧭 **Bản đồ phần này**: 5.1 Ba bậc so sánh → 5.2 Ba cặp quan trọng trên bảng (`viel / gern / gut`) → 5.3 Cách tạo Komparativ - Superlativ của tính từ → 5.4 Cấu trúc câu → 5.5 Vị trí động từ `1-2-3` → 5.6 Khi nào dùng cặp nào → 5.7 Mười lỗi thường gặp → 5.8 Mở rộng ⭐.
> ⚠️ **Thuật ngữ**: bảng giảng ghi tiêu đề cột đầu là *"Imperativ"*. **Đúng là `Komparativ`** (so sánh hơn). Cột sau là **`Superlativ`** (so sánh **nhất**).

#### 5.1. Ba bậc so sánh (`Steigerung`) — sơ đồ `V3`
| Bậc | Tên | Nghĩa | Ví dụ với `billig` |
| :-: | :--- | :--- | :--- |
| 1 | **Positiv** | nguyên mức | billig *(rẻ)* |
| 2 | **Komparativ** | **hơn** | billig**er** *(rẻ hơn)* |
| 3 | **Superlativ** | **nhất** | am billig**sten** *(rẻ nhất)* |

#### 5.2. Ba cặp bất quy tắc trên bảng giảng — HỌC THUỘC
| Positiv | Nghĩa | Komparativ | Nghĩa | Superlativ | Nghĩa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **viel** | nhiều | **mehr** | nhiều hơn | **am meisten** | nhiều nhất |
| **gern** | thích | **lieber** | thích hơn | **am liebsten** | thích nhất |
| **gut** | tốt | **besser** | tốt hơn | **am besten** | tốt nhất |

##### Phân tích các câu ví dụ trên bảng giảng (mỗi câu có `🔊`; số `①②③` là **vị trí trong câu**)
| Komparativ (so sánh hơn) | Superlativ (so sánh nhất) | Dịch |
| :--- | :--- | :--- |
| *„Ich esse **mehr** Reis **als** Nudeln.“* | *„**Am meisten**① esse② ich③ Kartoffeln.“* | Tôi ăn gạo nhiều hơn mì. / Tôi ăn khoai tây nhiều nhất. |
| *„Ich esse **lieber** Eis **als** Wurst.“* | *„**Am liebsten**① lese② ich③ Harry Potter.“* | Tôi thích ăn kem hơn xúc xích. / Tôi thích đọc Harry Potter nhất. |
| *„Ich spreche **besser** Deutsch **als** Englisch.“* | *„**Am besten**① spreche② ich③ Vietnamesisch.“* | Tôi nói tiếng Đức tốt hơn tiếng Anh. / Tôi nói tiếng Việt tốt nhất. |

> 🔑 **Điểm mấu chốt**: Khi cụm so sánh nhất `Am meisten / Am liebsten / Am besten` đứng **đầu câu (vị trí ①)**, **động từ chia luôn ở vị trí ②** rồi mới đến chủ ngữ ③ — tức là **đảo ngữ** (sơ đồ `V4`).

#### 5.3. Cách tạo `Komparativ` & `Superlativ` của tính từ (⭐ mở rộng quan trọng)
> ### 📐 CÔNG THỨC CƠ BẢN
> * **Komparativ** = tính từ + **`-er`** &nbsp;&nbsp; (`billig → billiger`)
> * **Superlativ** = **`am`** + tính từ + **`-sten`** &nbsp;&nbsp; (`billig → am billigsten`)

| Quy tắc | Ví dụ (Positiv → Komparativ → Superlativ) |
| :--- | :--- |
| **① Thông thường** (thêm `-er` / `am -sten`) | `billig → billiger → am billigsten` *(rẻ)* · `lecker → leckerer → am leckersten` *(ngon)* · `klein → kleiner → am kleinsten` *(nhỏ)* · `schwer → schwerer → am schwersten` *(nặng)* |
| **② Tính từ kết thúc `-t, -d, -s, -ß, -x, -z, -sch`** → Superlativ thêm **`-esten`** | `frisch → frischer → am frischesten` *(tươi)* · `süß → süßer → am süßesten` *(ngọt)* · `heiß → heißer → am heißesten` *(nóng)* · `leicht → leichter → am leichtesten` *(nhẹ)* · `gesund → gesünder → am gesündesten` |
| **③ Tính từ đuôi `-er` / `-el`** → Komparativ **bỏ `e`** | `teuer → **teurer** → am teuersten` *(đắt)* · `sauer → **saurer** → am sauersten` *(chua)* |
| **④ Thêm dấu hai chấm (Umlaut) `a → ä, o → ö, u → ü`** (một số tính từ ngắn) | `alt → älter → am ältesten` · `jung → jünger → am jüngsten` · `kalt → kälter → am kältesten` · `warm → wärmer → am wärmsten` · `scharf → schärfer → am schärfsten` · `lang → länger → am längsten` · `kurz → kürzer → am kürzesten` · `gesund → gesünder → am gesündesten` |
| **⑤ Ngoại lệ về chính tả** | `groß → größer → am größten` *(lớn)* — **không** thêm `e` dù đuôi `-ß` |
| **⑥ Bất quy tắc phải học thuộc** | `gut → besser → am besten` · `viel → mehr → am meisten` · `gern → lieber → am liebsten` · `hoch → höher → am höchsten` · `nah → näher → am nächsten` · `wenig → weniger → am wenigsten` |

> 🔎 **Cách nhớ Umlaut**: Không có quy tắc 100%. Quy ước thực hành: các tính từ **ngắn, một âm tiết, có `a / o / u`** hay có Umlaut (`alt, jung, kalt, warm, scharf, lang, kurz, groß, hoch, gesund`). Các tính từ khác (`billig, lecker, frisch, süß, klein, teuer, schwer, leicht, heiß`) **không** có Umlaut. Bảng nguồn ở Phụ lục A là **dữ liệu chuẩn — không tự suy diễn bằng thuật toán**.

##### Bảng 25 tính từ so sánh (`ADJECTIVES` — chép nguyên vào Phụ lục A)
| Positiv | Nghĩa | Komparativ | Superlativ |
| :--- | :--- | :--- | :--- |
| billig | rẻ | billiger | am billigsten |
| teuer | đắt | teurer | am teuersten |
| lecker | ngon | leckerer | am leckersten |
| frisch | tươi | frischer | am frischesten |
| süß | ngọt | süßer | am süßesten |
| sauer | chua | saurer | am sauersten |
| scharf | cay | schärfer | am schärfsten |
| gesund | tốt cho sức khỏe | gesünder | am gesündesten |
| groß | lớn, to | größer | am größten |
| klein | nhỏ | kleiner | am kleinsten |
| alt | cũ, già | älter | am ältesten |
| jung | trẻ | jünger | am jüngsten |
| kalt | lạnh | kälter | am kältesten |
| warm | ấm | wärmer | am wärmsten |
| heiß | nóng | heißer | am heißesten |
| hoch | cao | höher | am höchsten |
| nah | gần | näher | am nächsten |
| schwer | nặng; khó | schwerer | am schwersten |
| leicht | nhẹ; dễ | leichter | am leichtesten |
| lang | dài | länger | am längsten |
| kurz | ngắn | kürzer | am kürzesten |
| gut | tốt | besser | am besten |
| viel | nhiều | mehr | am meisten |
| gern | thích | lieber | am liebsten |
| wenig | ít | weniger | am wenigsten |

#### 5.4. Cấu trúc câu so sánh
| Loại | Công thức | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **So sánh hơn với tính từ** | `A + ist + Komparativ + als + B` | *„Die Birne ist **billiger als** die Erdbeere.“* — Quả lê rẻ hơn quả dâu tây. |
| **So sánh hơn với động từ (`gern`, `gut`, `viel`)** | `S + V + lieber / besser / mehr (+ tân ngữ) + als + B` | *„Ich trinke **lieber** Tee **als** Kaffee.“* — Tôi thích uống trà hơn cà phê.<br>*„Er kocht **besser als** ich.“* — Anh ấy nấu ăn giỏi hơn tôi. |
| **So sánh nhất với tính từ** | `A + ist + am + …sten` | *„Der Fisch ist **am teuersten**.“* — Cá đắt nhất. |
| **So sánh nhất — đảo ngữ** | `Am …sten + ist + A` | *„**Am teuersten** ist der Fisch.“* |
| **So sánh nhất với động từ** | `S + V + am liebsten / am besten / am meisten + …` | *„Ich esse **am liebsten** Nudeln.“* — Tôi thích ăn mì nhất. |
| **Đảo ngữ khi đặt cụm nhất đứng đầu** | `Am liebsten + V + S + …` | *„**Am liebsten** esse ich Nudeln.“* |

> 🔑 **`als` hay `wie`?** — So sánh **hơn** dùng **`als`** (*"hơn"*). Từ `wie` chỉ dùng cho so sánh **bằng** (xem 5.8).
> 🔑 **Danh từ đứng sau `als`** giữ **cùng cách** với danh từ ở vế trước: *„Der Apfel ist billiger als **die Birne**.“* (đều Nominativ); *„Ich kaufe mehr Äpfel als **Birnen**.“* (đều tân ngữ).

#### 5.5. Vị trí động từ `1-2-3` khi cụm so sánh nhất đứng đầu (sơ đồ `V4`)
| ① Vị trí 1 | ② Vị trí 2 (động từ chia) | ③ Vị trí 3 (chủ ngữ) | Phần còn lại |
| :--- | :--- | :--- | :--- |
| **Am liebsten** | esse | ich | Nudeln. |
| **Am meisten** | kauft | meine Mutter | Obst. |
| **Am besten** | kocht | mein Vater | Fisch. |
| **Am teuersten** | ist | der Fisch. | |

* Nếu **không đảo ngữ**: *„Ich esse **am liebsten** Nudeln.“* — Chủ ngữ ở vị trí 1, động từ ở vị trí 2, `am liebsten` đứng **sau động từ**.
* Cả hai cách đều **đúng**; khi chấm bài sắp xếp câu, phải chấp nhận **mọi trật tự hợp lệ**.

#### 5.6. Khi nào dùng cặp nào? (`viel/mehr` – `gern/lieber` – `gut/besser`)
| Cặp | Dùng để nói về | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **viel – mehr – am meisten** | **Số lượng** (ăn, mua, uống bao nhiêu) | *„Ich trinke **mehr** Wasser als Saft.“* — Tôi uống nước lọc nhiều hơn nước ép. |
| **gern – lieber – am liebsten** | **Sở thích** (thích làm gì / thích gì hơn) | *„Ich esse **gern** Obst, **lieber** Eis, **am liebsten** Schokolade.“* — Tôi thích ăn hoa quả, thích kem hơn, thích sô cô la nhất. |
| **gut – besser – am besten** | **Chất lượng / khả năng** (ngon, giỏi, tốt) | *„Das Brot hier schmeckt **am besten**.“* — Bánh mì ở đây ngon nhất. |

> ⚠️ `gern` luôn đi với **động từ** (`ich esse gern …`), không đi với `sein`. Không nói *~~Ich bin gern müde~~*. Câu nghĩa "*thích*" nhưng dùng động từ `mögen` thì không thêm `gern`: *„Ich mag Käse.“* (không nói *~~Ich mag gern Käse~~*).

#### 5.7. ⚠️ MƯỜI LỖI THƯỜNG GẶP (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Dùng `wie` thay `als` | ✘ *Ich esse mehr Reis wie Nudeln.* | ✔ *Ich esse mehr Reis als Nudeln.* | So sánh hơn → `als`. |
| 2 | Thêm `-er` cho `gut` | ✘ *gutter* | ✔ *besser* | Bất quy tắc. |
| 3 | Gấp đôi mức độ | ✘ *mehr besser* | ✔ *besser* / *viel besser* | Không cộng hai Komparativ. |
| 4 | Viết sai `teuer` | ✘ *teuerer* | ✔ *teurer* | Đuôi `-er` → bỏ `e`. |
| 5 | Quên `am` ở Superlativ | ✘ *Der Fisch ist teuersten.* | ✔ *Der Fisch ist am teuersten.* | Superlativ vị ngữ cần `am`. |
| 6 | Sai vị trí động từ | ✘ *Am liebsten ich esse Nudeln.* | ✔ *Am liebsten esse ich Nudeln.* | Động từ **vị trí 2**. |
| 7 | Thiếu `-e-` ở `-esten` | ✘ *am frischsten* | ✔ *am frischesten* | Đuôi `-sch` → `-esten`. |
| 8 | Nhầm `lieber` và `besser` | ✘ *Ich esse besser Eis als Kuchen.* *(nghĩa "giỏi ăn hơn")* | ✔ *Ich esse lieber Eis als Kuchen.* | `lieber` = thích hơn. |
| 9 | Dùng `viel` với danh từ đếm được số nhiều | ✘ *Ich kaufe viel Äpfel.* | ✔ *Ich kaufe viele Äpfel.* | `viele` + số nhiều. |
| 10 | Nhầm `mehr` với `meist` | ✘ *Ich esse am mehrsten Reis.* | ✔ *Ich esse am meisten Reis.* | Superlativ của `viel` là `am meisten`. |

#### 5.8. Mở rộng ⭐ (nhận biết, chỉ dùng rất ít trong bài tập)
* **So sánh bằng**: `so + Positiv + wie` / `genauso + Positiv + wie`. *„Die Birne ist **so** teuer **wie** der Apfel.“* — Quả lê đắt bằng quả táo. *„Fisch ist **nicht so** billig **wie** Reis.“* — Cá không rẻ bằng gạo. *(So sánh bằng dùng `wie`, so sánh hơn dùng `als`.)*
* **`weniger … als`** = *"ít hơn …"*: *„Ich esse weniger Fleisch als früher.“*
* **`immer + Komparativ`** = *"ngày càng …"*: *„Das Obst wird immer teurer.“* — Hoa quả ngày càng đắt.
* **Tính từ so sánh đứng trước danh từ** (`der billigste Käse`, `ein besseres Brot`) có thêm đuôi tính từ — thuộc A2, chỉ nhận biết.

---

### HỌC PHẦN 6: MUA SẮM (`EINKAUFEN`) — HỎI, NÓI, HỎI GIÁ, ĐỌC GIÁ TIỀN

#### 6.1. Người bán hỏi gì? Người mua nói gì? *(khớp bảng giảng, có mở rộng; sơ đồ `V5`)*
| a) Người bán **hỏi** khách muốn gì (`🔊 de-DE`) | Dịch | b) Khách **nói** muốn gì (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- | :--- |
| *„Bitte schön?“* | Xin mời (ngài cần gì ạ)? | *„Ein Kilo Kartoffeln, bitte!“* | Làm ơn một ký khoai tây! |
| *„Sie wünschen, bitte?“* | Ngài cần gì ạ? | *„Einen Liter Milch, bitte!“* | Làm ơn một lít sữa! |
| *„Was darf es sein?“* | Ngài cần gì ạ? | *„Ich nehme einen Kuchen.“* | Tôi lấy một chiếc bánh ngọt. |
| *„Welchen Käse möchten Sie?“* | Ngài muốn loại phô mai nào? | *„Ich möchte eine Dose Cola.“* | Tôi muốn một lon cô-ca. |
| *„Sonst noch etwas?“* / *„Darf es sonst noch etwas sein?“* | Ngài cần gì nữa không ạ? | *„Ich hätte gern eine Flasche Bier.“* | Tôi muốn lấy một chai bia. |
| *„Möchten Sie eine Tüte?“* | Ngài có cần túi không? | *„Haben Sie Schokolade?“* | Ngài có sô cô la không? |
| *„Das macht zusammen …“* | Tổng cộng là … | *„Gibt es heute Salat?“* | Hôm nay có salad không? |
| *„Hier ist Ihr Wechselgeld.“* ⭐ | Đây là tiền thối của ngài. | *„Danke, das ist alles.“* · *„Ja, bitte.“* / *„Nein, danke.“* | Cảm ơn, hết rồi. · Vâng, làm ơn. / Không, cảm ơn. |

> 🔑 **Ba cách nói "tôi muốn lấy…" (đều lịch sự)**:
> * **`Ich möchte + Akk.`** — *„Ich möchte einen Apfel.“*
> * **`Ich hätte gern + Akk.`** — *„Ich hätte gern einen Apfel.“* (rất lịch sự, thường dùng ở cửa hàng) — `hätte` là dạng đặc biệt của `haben`; **chỉ cần học nguyên cụm `ich hätte gern`** (các ngôi: `ich hätte, du hättest, er/sie/es hätte, wir hätten, ihr hättet, sie/Sie hätten`).
> * **`Ich nehme + Akk.`** — *„Ich nehme einen Apfel.“* (đã chọn xong).
> * Sau cả ba cụm, vật cần mua ở **Akkusativ**: `einen Apfel` (m), `eine Birne` (f), `ein Brot` (n), `Äpfel` (số nhiều).

#### 6.2. Hỏi giá & đáp giá (`nach dem Preis fragen`)
| Câu hỏi (`🔊 de-DE`) | Dịch | Cách trả lời (`🔊 de-DE`) |
| :--- | :--- | :--- |
| *„Was **kostet** eine Dose Cola?“* | Một lon cô-ca giá bao nhiêu? | *„Zwei Euro, bitte.“* / *„Eine Dose kostet zwei Euro.“* |
| *„Wie viel **kosten** hundert Gramm Käse?“* | Một trăm gam phô mai giá bao nhiêu? | *„Hundert Gramm kosten zwei Euro neunundneunzig.“* |
| *„Was macht das?“* / *„Wie viel macht das zusammen?“* | Tất cả là bao nhiêu? | *„Das macht zusammen neunzehn Euro neunundneunzig.“* |

> 🔑 **`kosten` chia theo vật được hỏi giá**: `Was kostet **der Salat**?` (số ít → `kostet`); `Wie viel kosten **die Birnen**?` (số nhiều → `kosten`); `Wie viel kosten **hundert Gramm** Käse?` (đại lượng được tính như số nhiều → `kosten`).

#### 6.3. Đơn vị đo lường & đóng gói (`Mengenangaben`)
| Đơn vị | Nghĩa | Sau số đếm | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :---: | :--- |
| **das Kilo (Kilogramm)** | ký (1 000 g) | **giữ nguyên** | *„Zwei Kilo Äpfel, bitte.“* — Làm ơn hai ký táo. |
| **das Pfund** | nửa ký (500 g) | giữ nguyên | *„Ein Pfund Erdbeeren, bitte.“* — Làm ơn nửa ký dâu tây. |
| **das Gramm** | gam | giữ nguyên | *„Hundert Gramm Schinken, bitte.“* — Làm ơn một trăm gam giăm bông. |
| **der Liter** | lít | giữ nguyên | *„Zwei Liter Milch, bitte.“* — Làm ơn hai lít sữa. |
| **das Stück** | miếng, cái | giữ nguyên | *„Zwei Stück Kuchen, bitte.“* — Làm ơn hai miếng bánh. |
| **die Flasche** | chai | thêm **`-n`** | *„Zwei Flaschen Wasser, bitte.“* — Làm ơn hai chai nước. |
| **die Dose** | lon, hộp | thêm **`-n`** | *„Drei Dosen Tomaten, bitte.“* — Làm ơn ba hộp cà chua. |
| **die Packung** | gói | thêm **`-en`** | *„Zwei Packungen Müsli, bitte.“* — Làm ơn hai gói ngũ cốc. |
| **die Tüte** | túi | thêm **`-n`** | *„Zwei Tüten Obst.“* — Hai túi hoa quả. |
| **die Scheibe** | lát | thêm **`-n`** | *„Drei Scheiben Schinken.“* — Ba lát giăm bông. |

> 🔑 **Quy tắc ghi nhớ**: Đơn vị **đo lường** giống đực/trung (`Kilo, Pfund, Gramm, Liter, Stück`) **giữ nguyên số ít** sau số đếm; đơn vị **đóng gói** giống cái (`Flasche, Dose, Packung, Tüte, Scheibe`) **thêm đuôi số nhiều**. Danh từ chỉ thứ được đo đứng **ngay sau**, không cần giới từ: `eine Dose Cola`, `ein Kilo Äpfel` (không có `von`).

#### 6.4. ĐỌC GIÁ TIỀN BẰNG TIẾNG ĐỨC (`Preise lesen`) — sơ đồ `V6`
> 🔑 **Quy tắc đọc**: `Số euro` + `Euro` + `số cent`. **Không đọc chữ "Komma"** và **không đọc chữ "Cent"** khi có cả euro lẫn cent; `Euro` và `Cent` **không thêm `-s`** ở số nhiều. Số `1` ở euro đọc là **`ein`** (*ein Euro*).

| Giá viết | Cách đọc (`🔊 de-DE`) | Ghi chú |
| :--- | :--- | :--- |
| 0,50 € | **fünfzig Cent** | Chỉ có cent: đọc `Cent` |
| 0,99 € | **neunundneunzig Cent** | |
| 1,00 € | **ein Euro** | Tròn euro: không đọc cent |
| 1,20 € | **ein Euro zwanzig** | Khớp bảng giảng (*„Nur 1,20 Euro.“*) |
| 2,00 € | **zwei Euro** | |
| 2,99 € | **zwei Euro neunundneunzig** | Khớp bảng giảng |
| 3,75 € | **drei Euro fünfundsiebzig** | Khớp bảng giảng |
| 6,40 € | **sechs Euro vierzig** | |
| 12,50 € | **zwölf Euro fünfzig** | |
| 19,99 € | **neunzehn Euro neunundneunzig** | Khớp bảng giảng |

* **Nhắc lại số 1–99**: `eins, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn, elf, zwölf, dreizehn … sechzehn, siebzehn … neunzehn, zwanzig`; từ 21 trở đi **đơn vị đọc trước**: `einundzwanzig, zweiundzwanzig, … fünfundsiebzig, neunundneunzig`; hàng chục: `dreißig, vierzig, fünfzig, sechzig, siebzig, achtzig, neunzig`. Lưu ý chính tả: **`sechzehn`** (không `sechszehn`), **`siebzehn`** (không `siebenzehn`), **`sechzig`**, **`siebzig`**, **`dreißig`** (có `ß`).
* **Thuật toán chuyển giá thành chữ** để đọc `🔊` được đặc tả ở Phần 4 (Engine E3), kèm bộ test bắt buộc.

#### 6.5. Hội thoại mua sắm mẫu — bốn tình huống (`🔊 de-DE` từng dòng, có dịch)
##### Hội thoại 1: Ở chợ — thứ tự đúng của bài sắp xếp trên bảng giảng
| # | Người nói | Câu (`🔊 de-DE`) | Dịch |
| :-: | :-: | :--- | :--- |
| 1 | Verkäufer | *„Guten Tag, was darf es sein?“* | Xin chào, ngài cần gì ạ? |
| 2 | Kunde | *„Ich hätte gern ein Kilo Kartoffeln.“* | Tôi muốn lấy một ký khoai tây. |
| 3 | Verkäufer | *„Gern, sonst noch etwas?“* | Vâng, ngài còn cần gì nữa không ạ? |
| 4 | Kunde | *„Wie viel kostet der Salat?“* | Salad giá bao nhiêu ạ? |
| 5 | Verkäufer | *„Nur 1,20 Euro.“* | Chỉ một euro hai mươi. |
| 6 | Kunde | *„Dann nehme ich noch einen Salat und zwei Orangen. Das ist alles.“* | Vậy tôi lấy thêm một salad và hai quả cam. Hết rồi ạ. |
| 7 | Verkäufer | *„Das macht zusammen 3,75 €.“* | Tổng cộng là ba euro bảy mươi lăm. |
| 8 | Kunde | *„Bitte.“* | Của bạn đây (khi đưa tiền). |

##### Hội thoại 2: Ở quầy tiệm bánh
* *Verkäuferin*: *„Guten Morgen! Was darf es sein?“* — Chào buổi sáng! Ngài cần gì ạ?
* *Kunde*: *„Ich hätte gern ein Brot und ein Stück Kuchen.“* — Tôi muốn một ổ bánh mì và một miếng bánh ngọt.
* *Verkäuferin*: *„Gern. Sonst noch etwas?“* — Vâng. Ngài cần gì nữa không ạ?
* *Kunde*: *„Nein, danke. Was macht das zusammen?“* — Không, cảm ơn. Tất cả là bao nhiêu?
* *Verkäuferin*: *„Das macht sechs Euro vierzig.“* — Tất cả là sáu euro bốn mươi. *(Bảng giá: `Brot` 2,80 € + `Stück Kuchen` 3,60 € = 6,40 €)*
* *Kunde*: *„Hier, bitte. Stimmt so.“* — Đây ạ. Không cần thối.

##### Hội thoại 3: Ở siêu thị — hỏi tìm hàng và giá
* *Kundin*: *„Entschuldigung, haben Sie Müsli?“* — Xin lỗi, bạn có ngũ cốc không?
* *Verkäufer*: *„Ja, das Müsli steht dort links.“* — Có, ngũ cốc ở kia, bên trái.
* *Kundin*: *„Danke. Wie viel kostet die Packung?“* — Cảm ơn. Một gói giá bao nhiêu?
* *Verkäufer*: *„Die Packung kostet drei Euro neunundneunzig.“* — Một gói giá ba euro chín mươi chín.
* *Kundin*: *„Gut, dann nehme ich zwei Packungen.“* — Tốt, vậy tôi lấy hai gói. *(2 × 3,99 € = 7,98 € = `sieben Euro achtundneunzig`)*

##### Hội thoại 4: Trong nhà hàng
* *Kellner*: *„Guten Abend, was möchten Sie trinken?“* — Chào buổi tối, ngài muốn uống gì ạ?
* *Gast*: *„Ein Wasser, bitte.“* — Làm ơn cho một nước lọc.
* *Kellner*: *„Und was möchten Sie essen?“* — Và ngài muốn ăn gì ạ?
* *Gast*: *„Ich nehme das Schnitzel mit Kartoffeln.“* — Tôi lấy món thịt tẩm bột chiên với khoai tây.
* *Kellner*: *„Gern, das kommt gleich.“* — Vâng, có ngay ạ.

#### 6.6. Các nơi mua sắm (⭐ mở rộng)
**der Markt** (chợ) · **der Supermarkt** (siêu thị) · **die Bäckerei** (tiệm bánh mì) · **die Metzgerei** (cửa hàng thịt) · **der Obststand** (quầy hoa quả) · **der Kiosk** (ki-ốt). *Mẫu câu*: *„Ich kaufe Brot **in der Bäckerei** und Gemüse **auf dem Markt**.“* — Tôi mua bánh mì ở tiệm bánh và rau củ ở chợ. *(Giới từ chỉ nơi chốn ở Dativ: `in der Bäckerei`, `auf dem Markt`, `im Supermarkt` — ôn từ Bài 8, 9.)*

---

### HỌC PHẦN 7: ĐỘNG TỪ ĂN UỐNG - MUA SẮM & ÔN PERFEKT (CHIA ĐỘNG TỪ CÓ QUY TẮC)

#### 7.1. Ôn công thức chia Präsens của động từ **có quy tắc**
> ### 📐 CÔNG THỨC: &nbsp; **`gốc động từ` + đuôi** &nbsp;(`ich -e · du -st · er/sie/es -t · wir -en · ihr -t · sie/Sie -en`)
> *Gốc động từ* = nguyên mẫu **bỏ `-en`** (`kaufen → kauf-`, `kochen → koch-`).

| Ngôi | **kaufen** (mua) | **kochen** (nấu) | **bestellen** (gọi món) | **brauchen** (cần) | **schmecken** (có vị) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ich** | kaufe | koche | bestelle | brauche | schmecke |
| **du** | kaufst | kochst | bestellst | brauchst | schmeckst |
| **er / sie / es** | kauft | kocht | bestellt | braucht | schmeckt |
| **wir** | kaufen | kochen | bestellen | brauchen | schmecken |
| **ihr** | kauft | kocht | bestellt | braucht | schmeckt |
| **sie / Sie** | kaufen | kochen | bestellen | brauchen | schmecken |

* 🔸 **Gốc kết thúc `-d`, `-t`** → thêm **`-e-`** ở `du / er·sie·es / ihr`: `schneiden → du schneid**est**, er schneid**et**, ihr schneid**et**`; `arbeiten → du arbeit**est**`; `warten → er wart**et**`.
* 🔸 **Gốc kết thúc `-s, -ß, -z, -x`** → ngôi `du` chỉ thêm **`-t`** (không `-st`): `heißen → du heiß**t**`; `reisen → du reis**t**`; `tanzen → du tanz**t**`.
* 🔸 **Gốc kết thúc `-sch` thì vẫn thêm `-st`** (không rút gọn): `wünschen → du wünsch**st**`; `waschen → du wäsch**st**`; `tauschen → du tausch**st**`.
* 🔸 **Cách "đóng gói" câu hỏi**: `Was kochst du heute?` — `Wohin kaufst du ein?` (động từ tách: `einkaufen → ich kaufe … ein`).

#### 7.2. Động từ **bất quy tắc ở Präsens** (đổi nguyên âm ở `du` và `er/sie/es`)
| Nhóm | Động từ | `ich` | `du` | `er / sie / es` | `wir` | `ihr` | `sie / Sie` |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `e → i` | **essen** | esse | **isst** | **isst** | essen | esst | essen |
| `e → i` | **geben** | gebe | **gibst** | **gibt** | geben | gebt | geben |
| `e → i` *(+ gốc đổi phụ âm)* | **nehmen** | nehme | **nimmst** | **nimmt** | nehmen | nehmt | nehmen |
| `e → ie` | **empfehlen** | empfehle | **empfiehlst** | **empfiehlt** | empfehlen | empfehlt | empfehlen |
| `a → ä` | **backen** | backe | **bäckst** | **bäckt** | backen | backt | backen |
| `a → ä` | **braten** | brate | **brätst** | **brät** | braten | bratet | braten |

> 🔑 **Nhắc nhớ**: Đổi nguyên âm **chỉ xảy ra ở `du` và `er/sie/es`**; `ich, wir, ihr, sie/Sie` giữ nguyên gốc. Ví dụ: *„Du **isst** gern Fisch.“* — *„Er **nimmt** zwei Brötchen.“* — *„Es **gibt** heute Reis.“*

#### 7.3. Động từ khuyết thiếu cho việc gọi món: `möchten`, `mögen`, `dürfen`
| Ngôi | **möchten** (muốn) | **mögen** (thích) | **dürfen** (được phép) |
| :--- | :--- | :--- | :--- |
| **ich** | möchte | mag | darf |
| **du** | möchtest | magst | darfst |
| **er / sie / es** | möchte | mag | darf |
| **wir** | möchten | mögen | dürfen |
| **ihr** | möchtet | mögt | dürft |
| **sie / Sie** | möchten | mögen | dürfen |

* **Cấu trúc**: động từ khuyết ở **vị trí 2**, động từ chính nguyên mẫu ở **cuối câu**: *„Ich möchte einen Kuchen **kaufen**.“* — Tôi muốn mua một chiếc bánh. *„Darf ich ein Stück **probieren**?“* — Tôi có thể thử một miếng không? *„Was möchten Sie **trinken**?“* — Ngài muốn uống gì?
* **`mögen`** = *thích* (một thứ cụ thể): *„Ich mag Käse.“* **`gern` + động từ** = *thích làm gì*: *„Ich esse gern Käse.“* — hai cách nói gần nghĩa, **không dùng cùng lúc**.
* **`es gibt` + Akkusativ** = *"có"*: *„Gibt es heute Fisch?“* — Hôm nay có cá không? *„Es gibt keinen Salat.“* — Không có salad.

#### 7.4. ⭐ ÔN PERFEKT (Bài 9) VỚI ĐỘNG TỪ ĂN UỐNG - MUA SẮM
Công thức: **`haben + … + Partizip II`** (tất cả động từ dưới đây dùng **`haben`**).
| Infinitiv | Nghĩa | Nhóm Partizip II (Bài 9) | Partizip II | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :-: | :--- | :--- |
| **kaufen** | mua | ① `ge-t` | gekauft | *„Gestern habe ich Obst gekauft.“* — Hôm qua tôi đã mua hoa quả. |
| **einkaufen** | mua sắm | ⑤ tiền tố tách | eingekauft | *„Wir haben auf dem Markt eingekauft.“* — Chúng tôi đã đi mua sắm ở chợ. |
| **kochen** | nấu | ① | gekocht | *„Meine Mutter hat Reis gekocht.“* — Mẹ tôi đã nấu cơm. |
| **schmecken** | có vị, ngon | ① | geschmeckt | *„Das Essen hat gut geschmeckt.“* — Món ăn đã rất ngon. |
| **bestellen** | gọi món | ④ tiền tố `be-` | bestellt | *„Ihr habt einen Salat bestellt.“* — Các bạn đã gọi một salad. |
| **bezahlen** | trả tiền | ④ | bezahlt | *„Er hat die Rechnung bezahlt.“* — Anh ấy đã trả hóa đơn. |
| **probieren** | thử | ③ `-ieren` | probiert | *„Sie hat den Käse probiert.“* — Cô ấy đã thử phô mai. |
| **essen** | ăn | ⑥ bất quy tắc | gegessen | *„Wir haben Fisch gegessen.“* — Chúng tôi đã ăn cá. |
| **trinken** | uống | ⑥ | getrunken | *„Du hast viel Wasser getrunken.“* — Bạn đã uống nhiều nước. |
| **nehmen** | lấy | ⑥ | genommen | *„Ich habe zwei Kilo Äpfel genommen.“* — Tôi đã lấy hai ký táo. |
| **backen** | nướng bánh | ⑥ | gebacken | *„Am Samstag haben sie einen Kuchen gebacken.“* — Thứ Bảy họ đã nướng một chiếc bánh. |
| **braten** | chiên | ⑥ | gebraten | *„Er hat das Schnitzel gebraten.“* — Anh ấy đã chiên miếng thịt tẩm bột. |
| **schneiden** | cắt | ⑥ | geschnitten | *„Wir haben die Zwiebeln geschnitten.“* — Chúng tôi đã thái hành tây. |
| **empfehlen** | giới thiệu | ⑥ + tiền tố `emp-` | empfohlen | *„Der Kellner hat den Fisch empfohlen.“* — Người phục vụ đã gợi ý món cá. |

---

### HỌC PHẦN 8: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN (`TEXTANALYSE: ESSEN UND TRINKEN` — KÈM AUDIO `de-DE`)

#### 8.1. Đoạn văn 1: *"Die Essgewohnheiten der Familie Berger"* (thói quen ăn uống — so sánh hơn / nhất)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Familie Berger wohnt in Wien. Zum Frühstück essen die Bergers Brot mit Butter und Marmelade. Der Vater trinkt Kaffee, die Mutter trinkt **lieber** Tee, und die Kinder trinken **am liebsten** Milch. Mittags kocht die Mutter oft Kartoffeln mit Fisch oder Gemüse. Die Kinder essen **mehr** Nudeln **als** Reis, aber der Vater isst **mehr** Reis **als** Nudeln. Am Wochenende backt der Vater einen Kuchen. **Am liebsten** essen alle Erdbeerkuchen.“*
* **Dịch nghĩa tiếng Việt**:
  > *„Gia đình Berger sống ở Wien. Vào bữa sáng nhà Berger ăn bánh mì với bơ và mứt. Người bố uống cà phê, người mẹ thích uống trà hơn, còn bọn trẻ thích uống sữa nhất. Buổi trưa mẹ thường nấu khoai tây với cá hoặc rau củ. Bọn trẻ ăn mì nhiều hơn cơm, nhưng người bố ăn cơm nhiều hơn mì. Cuối tuần người bố nướng một chiếc bánh. Mọi người thích nhất là ăn bánh dâu tây.“*
* **Bảng phân tích bắt buộc kèm theo (hiển thị khi bấm "🔍 Phân tích")**:

| Cụm trong đoạn văn | Loại | Giải thích |
| :--- | :-: | :--- |
| *die Mutter trinkt **lieber** Tee* | Komparativ của `gern` | Mẹ thích trà **hơn** (so với cà phê của bố). |
| *die Kinder trinken **am liebsten** Milch* | Superlativ của `gern` | Bọn trẻ thích sữa **nhất**. |
| *essen **mehr** Nudeln **als** Reis* | Komparativ của `viel` + `als` | Ăn mì **nhiều hơn** cơm. |
| *der Vater isst **mehr** Reis **als** Nudeln* | Komparativ của `viel` + `als` | Bố ăn cơm **nhiều hơn** mì. |
| ***Am liebsten** essen alle Erdbeerkuchen* | Superlativ đảo ngữ | `Am liebsten`① `essen`② `alle`③ — động từ ở vị trí 2. |
| *backt der Vater einen Kuchen* | `backen` (`er backt`) | Ngôi `er` — Akkusativ `einen Kuchen`. |

#### 8.2. Đoạn văn 2: *Ở chợ — bà Nguyen mua rau củ* (`Welch-`, hỏi giá, tính tiền)
* **Hội thoại (`🔊 de-DE`, mỗi dòng một nút)**:
  > **Verkäufer**: *„Guten Morgen, was darf es sein?“*
  > **Frau Nguyen**: *„Welche Tomaten sind heute frisch?“*
  > **Verkäufer**: *„Die Tomaten hier. Das Kilo kostet zwei Euro fünfzig.“*
  > **Frau Nguyen**: *„Dann nehme ich zwei Kilo Tomaten.“*
  > **Verkäufer**: *„Gern. Sonst noch etwas?“*
  > **Frau Nguyen**: *„Ja, ein Kilo Möhren. Wie viel kosten die Möhren?“*
  > **Verkäufer**: *„Ein Kilo Möhren kostet ein Euro zwanzig.“*
  > **Frau Nguyen**: *„Gut. Und was kostet die Ananas?“*
  > **Verkäufer**: *„Die Ananas kostet zwei Euro dreißig.“*
  > **Frau Nguyen**: *„Die Ananas nehme ich auch. Das ist alles.“*
  > **Verkäufer**: *„Das macht zusammen acht Euro fünfzig.“*
  > **Frau Nguyen**: *„Hier sind zehn Euro.“*
  > **Verkäufer**: *„Und ein Euro fünfzig zurück. Danke schön!“*
* **Dịch nghĩa**:
  > **Người bán**: *„Chào buổi sáng, bà cần gì ạ?“* — **Bà Nguyen**: *„Những quả cà chua nào hôm nay tươi?“* — **Người bán**: *„Cà chua ở đây ạ. Một ký giá hai euro năm mươi.“* — **Bà Nguyen**: *„Vậy tôi lấy hai ký cà chua.“* — **Người bán**: *„Vâng. Bà cần gì nữa không ạ?“* — **Bà Nguyen**: *„Có, một ký cà rốt. Cà rốt giá bao nhiêu?“* — **Người bán**: *„Một ký cà rốt giá một euro hai mươi.“* — **Bà Nguyen**: *„Tốt. Còn quả dứa giá bao nhiêu?“* — **Người bán**: *„Quả dứa giá hai euro ba mươi.“* — **Bà Nguyen**: *„Tôi lấy cả quả dứa. Hết rồi ạ.“* — **Người bán**: *„Tổng cộng là tám euro năm mươi.“* — **Bà Nguyen**: *„Đây là mười euro.“* — **Người bán**: *„Và thối lại một euro năm mươi. Cảm ơn bà!“*
* **Bảng tính tiền (hiển thị cùng hội thoại, tính bằng số nguyên cent)**:

| Mặt hàng | Số lượng | Đơn giá | Thành tiền |
| :--- | :-: | :--- | :--- |
| Tomaten | 2 kg | 2,50 € / kg | 5,00 € |
| Möhren | 1 kg | 1,20 € / kg | 1,20 € |
| Ananas | 1 Stück | 2,30 € | 2,30 € |
| **Tổng cộng** | | | **8,50 €** *(`acht Euro fünfzig`)* |
| Khách đưa | | | 10,00 € |
| **Tiền thối** | | | **1,50 €** *(`ein Euro fünfzig`)* |

#### 8.3. Đoạn văn 3: *E-Mail von Minh* (`am liebsten`, `mehr … als`, so sánh tính từ)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Hallo Lena, du fragst, was ich in Deutschland **am liebsten** esse. Ich esse **am liebsten** Reis mit Fisch, so wie zu Hause in Vietnam! Brot mag ich auch, aber ich esse **mehr** Reis **als** Brot. Auf dem Markt kaufe ich viel Gemüse. Gemüse ist gesund und billig. Obst ist **teurer als** Gemüse, aber Mangos schmecken **am besten**. Was isst du **am liebsten**? Dein Minh“*
* **Dịch nghĩa**:
  > *„Chào Lena, bạn hỏi ở Đức mình thích ăn gì nhất. Mình thích nhất là ăn cơm với cá, giống như ở nhà ở Việt Nam! Mình cũng thích bánh mì, nhưng mình ăn cơm nhiều hơn bánh mì. Ở chợ mình mua nhiều rau củ. Rau củ tốt cho sức khỏe và rẻ. Hoa quả đắt hơn rau củ, nhưng xoài thì ngon nhất. Còn bạn thích ăn gì nhất? Minh của bạn“*
* **Bảng phân tích**:

| Cụm trong thư | Loại | Giải thích |
| :--- | :-: | :--- |
| *am liebsten esse* | Superlativ của `gern` | **Thích nhất**; động từ chia ở vị trí 2 khi đứng sau chủ ngữ (`ich esse am liebsten`). |
| *mehr Reis als Brot* | Komparativ của `viel` | Ăn cơm nhiều **hơn** bánh mì. |
| *viel Gemüse* | `viel` + danh từ không đếm được | `das Gemüse` không có số nhiều → `viel`. |
| *teurer als Gemüse* | Komparativ của `teuer` | `teuer → teurer` (bỏ `e`). |
| *schmecken am besten* | Superlativ của `gut` | Mangos **ngon nhất**. |

---

### HỌC PHẦN 9 (MỤC 2.9): BẢNG TỔNG HỢP & ĐẶC TẢ 6 SƠ ĐỒ SVG (`static/js/essen_svg.js`)

#### 9.1. Bảng tổng hợp kiến thức (`CHEAT SHEET` — in được trên 1 trang)
| Mục | Ghi nhớ nhanh |
| :--- | :--- |
| **Đuôi `welch-`** | `der → welcher` · `den → welchen` · `die → welche` · `das → welches` · số nhiều `→ welche`. **Chỉ giống đực đổi giữa Nominativ và Akkusativ.** |
| **Chọn cách** | Chủ ngữ → Nominativ; tân ngữ (`kaufen, nehmen, essen, trinken, möchten, brauchen…`) → Akkusativ |
| **Hai danh từ** | `Welche Dose Cola?` — theo danh từ **đứng ngay sau** `welch-` (`Dose`) |
| **Số lượng** | `viel` + không đếm được · `viele` + số nhiều đếm được · `mehr` (không đổi) · `mehr … als` |
| **3 cặp bất quy tắc** | `viel – mehr – am meisten` · `gern – lieber – am liebsten` · `gut – besser – am besten` |
| **Tính từ** | Komparativ `+ -er`; Superlativ `am + … + -sten` (`-esten` sau `-t/-d/-s/-ß/-z/-sch`); `teuer → teurer`; Umlaut: `alt, jung, kalt, warm, scharf, gesund…` |
| **Câu so sánh** | `A ist + Komparativ + als + B` · `Am …sten + động từ + chủ ngữ` |
| **Mua sắm** | `Ich möchte / Ich hätte gern / Ich nehme + Akk.` · `Was kostet …? / Wie viel kosten …?` · `Das macht zusammen …` |
| **Đơn vị** | `Kilo, Pfund, Gramm, Liter, Stück` giữ nguyên · `Flasche, Dose, Packung, Tüte` thêm `-n/-en` |
| **Giá tiền** | `3,75 € = drei Euro fünfundsiebzig` · `1,20 € = ein Euro zwanzig` |
| **Giống dễ nhầm** | `der Käse` · `der Reis` · `das Obst` · `das Gemüse` · `die Butter` · `die Wurst` |

#### 9.2. Đặc tả 6 sơ đồ SVG trực quan
Mỗi sơ đồ phải có **tiêu đề tiếng Việt + nhãn tiếng Đức**, hoạt động đúng ở chế độ Dark/Light, và mọi câu tiếng Đức hiển thị trong sơ đồ có nút **`🔊`** (chỉ đọc chuỗi tiếng Đức sạch).

| Mã | Tên sơ đồ | Hình vẽ & hành vi bắt buộc |
| :-: | :--- | :--- |
| **V1** | **Bảng đuôi `Welch-` tương tác** | Bảng 4 hàng (`m / f / n / PL`) × 2 cột (`Nominativ / Akkusativ`) như mục 3.2. Phía trên có **danh sách chọn danh từ** (`der Käse, die Dose, das Buch, die Bananen, der Reis, das Brot…` lấy từ Phụ lục A). Khi chọn một danh từ → tô sáng đúng ô, hiện câu mẫu (`Welchen Käse möchten Sie?`) + dịch + `🔊`. Các ô giống đực dùng màu khác biệt nổi bật vì là ô duy nhất đổi đuôi. |
| **V2** | **Lưu đồ chọn `welch-`** | Sơ đồ khối: `Danh từ giống gì?` → (cái / trung / số nhiều → `welche / welches / welche`) hoặc (đực → `Danh từ là chủ ngữ hay tân ngữ?` → `Chủ ngữ → welcher` / `Tân ngữ → welchen`). Mỗi nhánh kết thúc bằng ví dụ có `🔊`. |
| **V3** | **Bậc thang so sánh** | Ba bậc thang đi lên: `Positiv → Komparativ → Superlativ`. Có 3 hàng ví dụ: `billig → billiger → am billigsten`, `gern → lieber → am liebsten`, `gut → besser → am besten`; nút chuyển hàng `◀ ▶` hoặc chọn tính từ từ bảng 25 tính từ (Phụ lục A). **Chỉ dùng dữ liệu bảng nguồn**, không tự suy diễn. |
| **V4** | **Khung câu `Am liebsten esse ich …` (vị trí 1-2-3)** | Hàng 4 ô: **①** cụm so sánh nhất (xanh dương) · **②** động từ chia (đỏ) · **③** chủ ngữ (xanh lá) · phần còn lại (xám). Bấm nút "đảo ngữ" → các ô hoán đổi mượt giữa `Ich esse am liebsten Nudeln.` và `Am liebsten esse ich Nudeln.` Mỗi trạng thái có dịch + `🔊`. |
| **V5** | **Quầy chợ — hội thoại tương tác** | Quầy hàng với các bảng giá và hình biểu tượng (🍅 🥕 🍍 🧀 🥖 🥛). Bấm vào một món → hiện câu hỏi `Was kostet …?` / `Wie viel kosten …?` và câu trả lời có **giá tiền được đọc bằng chữ**. Nút **▶ "Mua sắm"** chạy hội thoại 1 hoặc 2 ở mục 6.5, mỗi lượt lời phát `🔊` tuần tự. |
| **V6** | **Máy đọc giá tiền Euro** | Ô nhập số tiền (`0,01`–`99,99`) hoặc nút chọn nhanh; hiển thị **giá viết** `3,75 €` → **cách đọc bằng chữ** `drei Euro fünfundsiebzig` → nút `🔊`. Phải dùng **cùng hàm `price_to_german()` của Engine E3** (không viết lại logic) và pass toàn bộ test ở Phần 4. |

---

## PHẦN 3: KHO 100 BÀI TẬP ĐỘC NHẤT CỦA BÀI 10 (`lessons/a1/seed_a1_b10.py`) — 16 DẠNG BÀI

Toàn bộ **100 câu hỏi** dưới đây là **câu mới sáng tác**, chỉ tham khảo ý tưởng từ bảng giảng; không trùng với giáo trình, Bài 9 hay Bài 8. Chủ ngữ được **xoay vòng đủ 9 ngôi** (`ich, du, er, sie, es, wir, ihr, sie, Sie`) cùng tên riêng, gia đình, khách hàng - người bán; ngữ cảnh đa dạng (chợ, siêu thị, tiệm bánh, nhà hàng, bữa sáng, Wien, Berlin, Việt Nam). Độ khó ngang Bài 9, thỉnh thoảng nhỉnh hơn một chút (đảo ngữ `Am liebsten …`, đọc giá tiền, sắp xếp hội thoại).

### 3.1. Bảng Phân Bổ 100 Câu Hỏi Theo 16 Dạng Bài Tập
| STT | Mã dạng (`type`) | Tên dạng bài hiển thị | Số lượng | Mã câu | Trọng tâm |
| :-: | :--- | :--- | :-: | :-: | :--- |
| 1 | `trac_nghiem` | Trắc nghiệm | **10** | 1–10 | Đuôi `welch-`, Komparativ / Superlativ, `viel / viele`, `lieber`, vị trí động từ, câu mua hàng, giống & số nhiều |
| 2 | `dien_khuyet` | Điền khuyết | **12** | 11–22 | Điền `welch-`, `mehr`, `am liebsten`, `teurer`, chia động từ `isst / kostet / kocht` |
| 3 | `dich_nghia_vd` | Dịch từ / cụm: Việt → Đức | **8** | 23–30 | Danh từ thực phẩm (kèm mạo từ) + cụm đơn vị |
| 4 | `dich_nghia_dv` | Dịch từ / câu ngắn: Đức → Việt | **8** | 31–38 | Danh từ + mẫu câu mua sắm |
| 5 | `noi_o` | Nối ô (Matching) | **8** | 39–46 | Từ ↔ nghĩa, số ít ↔ số nhiều, hỏi ↔ đáp, chia động từ, Partizip II, Komparativ, Superlativ, đơn vị ↔ thực phẩm |
| 6 | `dien_tao_cau` | Điền 2 chỗ trống tạo câu | **8** | 47–54 | `welchen … den`, `billiger … als`, `mehr … als`, `kostet … kosten`, Perfekt |
| 7 | `nghe_dien` | Nghe `de-DE` và điền từ | **8** | 55–62 | Nghe câu hỏi `Welch-`, câu so sánh, giá tiền, Perfekt |
| 8 | `dich_cau_vd` | Dịch câu: Việt → Đức | **6** | 63–68 | Dịch câu hỏi / so sánh / Perfekt (đa đáp án) |
| 9 | `dich_cau_dv` | Dịch câu: Đức → Việt | **6** | 69–74 | Dịch câu / hội thoại ngắn |
| 10 | `sap_xep_cau` | Sắp xếp từ thành câu | **5** | 75–79 | Câu hỏi `Welch-`, `lieber … als`, `Am meisten …` (đảo ngữ) |
| 11 | `phan_loai_giong` 🆕 | **Phân loại `der / die / das`** | **4** | 80–83 | Mỗi câu 4 danh từ thực phẩm → xếp vào đúng giống |
| 12 | `tim_loi_sai` | Tìm lỗi và sửa câu | **4** | 84–87 | Sai đuôi `welch-` / `als - wie` / Komparativ / vị trí động từ |
| 13 | `viet_lai_so_sanh` 🆕 | **Viết lại câu thành so sánh** | **4** | 88–91 | Positiv → Komparativ / Superlativ |
| 14 | `dung_sai` | Đọc hiểu Đúng / Sai (Richtig / Falsch) | **3** | 92–94 | 2 đoạn văn ngắn về chợ và thói quen ăn uống |
| 15 | `hoi_thoai_sap_xep` 🆕 | **Sắp xếp hội thoại mua sắm** | **3** | 95–97 | Xếp các lượt lời thành hội thoại hợp lý |
| 16 | `nghe_gia_tien` 🆕 | **Nghe giá tiền và nhập số** | **3** | 98–100 | Nghe giá bằng chữ → gõ số `4,85` |
| | | **TỔNG CỘNG BÀI 10** | **100** | 1–100 | **100% độc nhất + QA Zero-Bug** |

> 📌 Phân bổ trọng tâm: khoảng **30 câu** về `Welch-` và từ vựng giống - số nhiều, **30 câu** về so sánh / số lượng, **15 câu** về mua sắm - giá tiền, **15 câu** về chia động từ và ôn Perfekt, phần còn lại là đọc hiểu - tổng hợp.

### 3.2. Đặc tả giao diện & chấm điểm cho 4 dạng bài MỚI (🆕) — *làm thêm, không phá component cũ*
Ba dạng `sap_xep_cau`, `tim_loi_sai`, `dung_sai` **dùng lại nguyên component của Bài 9**. Bốn dạng mới dưới đây nên được làm bằng cách **tổng quát hóa tương thích ngược** component cũ (xem mục 1) hoặc tạo component mới.

| Dạng | Giao diện người học | Dữ liệu câu hỏi (`question object`) | Quy tắc chấm điểm |
| :--- | :--- | :--- | :--- |
| `phan_loai_giong` | Bảng 4 hàng; mỗi hàng 1 danh từ (**không kèm mạo từ**) + nghĩa tiếng Việt + 3 nút **`der`** / **`die`** / **`das`** | `items` = 4 × {`noun`, `meaning_vi`, `article`, `plural`, `reason_vi`} | Đúng khi **cả 4 hàng** đúng; hàng sai tô đỏ và hiện `reason_vi` + dạng đầy đủ (`der Käse`). Voice đọc `article + noun`. *(Tương tự `chon_haben_sein` của Bài 9, chỉ khác số nút.)* |
| `viet_lai_so_sanh` | Hiển thị câu gốc ở Positiv + yêu cầu (so sánh hơn / nhất, kèm đối tượng); người học **gõ lại cả câu** | `source_sentence`, `instruction_vi`, `accepted_answers`, `translation_vi` (dịch câu đáp án) | So khớp như `dich_cau_vd` (không phân biệt hoa/thường, bỏ dấu câu cuối). |
| `hoi_thoai_sap_xep` | Các **lượt lời xáo trộn** (mỗi ô là 1 lượt, kèm nhãn người nói); người học bấm theo thứ tự đúng; nút `↩ Xóa`, `🔊 Nghe cả hội thoại` | `lines` (danh sách đã xáo), `correct_order` (danh sách chỉ số đúng), `translation_vi` (dịch từng lượt) | Đúng khi thứ tự trùng `correct_order` hoặc trùng một thứ tự khác được liệt kê trong `accepted_orders`. |
| `nghe_gia_tien` | Nút `🔊` phát câu có giá tiền (đã đọc thành chữ); ô nhập số | `audio_text` (giá **viết bằng chữ**), `price_cents` (số nguyên), `accepted_answers`, `translation_vi` | Chuẩn hóa đáp án: bỏ khoảng trắng và ký hiệu `€`, chấp nhận dấu `,` hoặc `.` (`4,85` = `4.85`), chấp nhận có hoặc không có `Euro`. So sánh **bằng số nguyên cent** (`485`). |

> 🔊 **Quy tắc voice cho mọi dạng**: sau khi người học trả lời xong, nút `🔊` đọc **câu tiếng Đức đúng đầy đủ** (đã điền chỗ trống / đã sắp xếp / đã sửa lỗi). Dạng `dich_nghia_dv`, `dich_cau_dv`: đọc câu tiếng Đức ở đề bài. Không bao giờ đọc ký hiệu `___`, `[1]`, `→`, `€`. Mọi giá tiền hiển thị bằng số phải được **chuyển thành chữ bằng `price_to_german()`** trước khi đọc.
> 🈯 **Quy tắc `translation_vi` cho các dạng đề bài là tiếng Việt hoặc chỉ có cặp từ**: với `dich_nghia_vd` (Câu 23–30) đề bài **chính là tiếng Việt**, nên sau khi trả lời web hiển thị `Dịch nghĩa: <đề tiếng Việt> = <đáp án tiếng Đức>`; với `dich_nghia_dv` (Câu 31–38) bản dịch **chính là đáp án**; với `noi_o` hiển thị dòng *"Dịch nghĩa các cặp"* (có sẵn cho từng bài nối). Với `dich_cau_vd` (Câu 63–68) và `dien_tao_cau` (Câu 47–54) `translation_vi` = **đề tiếng Việt**; với `dich_cau_dv` (Câu 69–74) = **đáp án tiếng Việt**; với `nghe_dien` = `hint_vi`; với `hoi_thoai_sap_xep` = dịch **từng lượt lời** có sẵn. Không được để trống phần dịch ở bất kỳ dạng nào.
> 🧮 **Quy tắc `dien_tao_cau` khi có 2 ô trống**: chấm từng ô; ô nào đúng thì tô xanh, ô sai tô đỏ; điểm EXP chỉ cộng khi **cả hai ô** đúng.
> 🔠 **Quy tắc chữ hoa**: so khớp **không phân biệt hoa/thường** cho mọi dạng; chấp nhận `ä/ö/ü/ß` được gõ thành `ae/oe/ue/ss` (ví dụ `hätte` = `haette`, `süß` = `suess`).

---

### 3.3. Danh Sách Chi Tiết 100 Câu Hỏi (Để Seed Vào `lessons/a1/seed_a1_b10.py`)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 10 Câu: Câu 1 → Câu 10)
1. **Câu 1** *(kèm sơ đồ `visual: V1`)*
   * `question`: Quan sát **bảng đuôi `welch-` (V1)** bên trên. Chọn dạng đúng: *„___ Apfel kaufst du?“* (`der Apfel`, tân ngữ)
   * Đáp án: `A. Welcher` | `B. Welchen` (Đúng) | `C. Welche` | `D. Welches`
   * Dịch nghĩa câu: *„Bạn mua quả táo nào?“*
   * Giải thích: `der Apfel` là giống **đực**, làm **tân ngữ** của `kaufen` → **Akkusativ** → `den` → **`Welchen Apfel kaufst du?`**
2. **Câu 2**
   * `question`: Chọn dạng đúng: *„___ Bananen sind schon reif?“*
   * Đáp án: `A. Welcher` | `B. Welchen` | `C. Welche` (Đúng) | `D. Welches`
   * Dịch nghĩa câu: *„Những quả chuối nào đã chín rồi?“*
   * Giải thích: `die Bananen` là **số nhiều**, làm chủ ngữ → **`Welche Bananen sind schon reif?`** (số nhiều luôn dùng `welche`).
3. **Câu 3**
   * `question`: Chọn dạng đúng: *„___ Obst ist frisch?“*
   * Đáp án: `A. Welcher` | `B. Welchen` | `C. Welche` | `D. Welches` (Đúng)
   * Dịch nghĩa câu: *„Loại hoa quả nào tươi?“*
   * Giải thích: `das Obst` là giống **trung** → **`Welches Obst ist frisch?`**
4. **Câu 4**
   * `question`: Chọn dạng so sánh hơn đúng của `billig`: *„Der Apfel ist ___ als die Birne.“*
   * Đáp án: `A. billigere` | `B. billiger` (Đúng) | `C. billigster` | `D. am billigsten`
   * Dịch nghĩa câu: *„Quả táo rẻ hơn quả lê.“*
   * Giải thích: Komparativ = tính từ + `-er` → **`billiger`**, đi với `als` ở sau.
5. **Câu 5**
   * `question`: Chọn dạng so sánh **nhất** đúng của `teuer`: *„Der Fisch ist ___.“*
   * Đáp án: `A. am teuerten` | `B. am teuersten` (Đúng) | `C. am teurersten` | `D. am teuerrsten`
   * Dịch nghĩa câu: *„Con cá đắt nhất.“*
   * Giải thích: `teuer → teurer → am teuersten`. Chỉ Komparativ bỏ `e` (`teurer`); Superlativ giữ nguyên gốc `teuer` + `-sten`.
6. **Câu 6**
   * `question`: Chọn từ đúng: *„Auf dem Markt kaufe ich ___ Äpfel.“*
   * Đáp án: `A. viel` | `B. viele` (Đúng) | `C. vieler` | `D. viels`
   * Dịch nghĩa câu: *„Ở chợ tôi mua nhiều quả táo.“*
   * Giải thích: `Äpfel` là danh từ **số nhiều đếm được** → **`viele`** (còn `viel` đi với danh từ không đếm được như `Obst`).
7. **Câu 7**
   * `question`: Chọn từ đúng nghĩa *"thích hơn"*: *„Ich esse Reis ___ als Brot.“*
   * Đáp án: `A. gern` | `B. lieber` (Đúng) | `C. am liebsten` | `D. besser`
   * Dịch nghĩa câu: *„Tôi thích ăn cơm hơn bánh mì.“*
   * Giải thích: Komparativ của `gern` là **`lieber`**; cấu trúc `lieber … als`.
8. **Câu 8** *(kèm sơ đồ `visual: V4`)*
   * `question`: Quan sát **khung câu V4**. Chọn câu đúng vị trí động từ:
   * Đáp án: `A. Am liebsten ich esse Schokolade.` | `B. Am liebsten esse ich Schokolade.` (Đúng) | `C. Am liebsten Schokolade esse ich.` | `D. Ich am liebsten esse Schokolade.`
   * Dịch nghĩa câu: *„Tôi thích ăn sô cô la nhất.“*
   * Giải thích: Cụm `Am liebsten` ở vị trí ①, **động từ `esse` phải ở vị trí ②**, rồi mới đến chủ ngữ `ich` ③ → **`Am liebsten esse ich Schokolade.`**
9. **Câu 9**
   * `question`: Người bán hỏi: *„Was darf es sein?“* Câu trả lời **tự nhiên và đúng ngữ pháp** nhất là:
   * Đáp án: `A. Ich hätte gern zwei Kilo Äpfel.` (Đúng) | `B. Ich bin zwei Kilo Äpfel.` | `C. Ja, bitte, Äpfel haben.` | `D. Es darf Äpfel sein.`
   * Dịch nghĩa câu: *„Tôi muốn lấy hai ký táo.“*
   * Giải thích: Khi mua hàng dùng `Ich hätte gern / Ich möchte / Ich nehme + Akkusativ` → **`Ich hätte gern zwei Kilo Äpfel.`** (sau `Kilo` giữ nguyên số ít).
10. **Câu 10**
    * `question`: Dòng nào ghi **ĐÚNG cả mạo từ lẫn số nhiều**?
    * Đáp án: `A. der Apfel – die Äpfel / die Birne – die Birnen / das Ei – die Eier` (Đúng) | `B. der Apfel – die Apfels / die Birne – die Birne / das Ei – die Eis` | `C. die Apfel – die Äpfel / der Birne – die Birnen / das Ei – die Eier` | `D. der Käse – die Käsen / die Wurst – die Wursten / der Fisch – die Fischs`
    * Dịch nghĩa câu: *„quả táo – các quả táo / quả lê – các quả lê / quả trứng – các quả trứng.“*
    * Giải thích: `der Apfel → die Äpfel` (thêm Umlaut), `die Birne → die Birnen`, `das Ei → die Eier`. Các dòng còn lại sai giống hoặc số nhiều (`die Käse`, `die Würste`, `die Fische`).

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 12 Câu: Câu 11 → Câu 22)
11. **Câu 11**: Điền dạng `welch-` đúng (Nominativ): *„___ Salat ist gesund?“* (`der Salat`)
    * Đáp án chấp nhận: `["welcher"]`
    * Dịch nghĩa câu: *„Món salad nào tốt cho sức khỏe?“*
    * Giải thích: `der Salat` là **chủ ngữ** của `ist` → Nominativ giống đực → **`Welcher`**.
12. **Câu 12**: Điền dạng `welch-` đúng (Akkusativ): *„___ Schinken möchtest du?“* (`der Schinken`)
    * Đáp án chấp nhận: `["welchen"]`
    * Dịch nghĩa câu: *„Bạn muốn loại giăm bông nào?“*
    * Giải thích: `der Schinken` là **tân ngữ** của `möchten` → Akkusativ giống đực → **`Welchen`**.
13. **Câu 13**: Điền dạng `welch-` đúng (Akkusativ): *„___ Brot möchtest du?“* (`das Brot`)
    * Đáp án chấp nhận: `["welches"]`
    * Dịch nghĩa câu: *„Bạn muốn loại bánh mì nào?“*
    * Giải thích: `das Brot` giống trung, Akkusativ không đổi → **`Welches`**.
14. **Câu 14**: Điền dạng `welch-` đúng: *„___ Kartoffeln brauchen wir?“*
    * Đáp án chấp nhận: `["welche"]`
    * Dịch nghĩa câu: *„Chúng ta cần những củ khoai tây nào?“*
    * Giải thích: `die Kartoffeln` là số nhiều (Akkusativ) → **`Welche`**.
15. **Câu 15**: Điền dạng so sánh hơn của `teuer`: *„Ein Kilo Fleisch ist ___ als ein Kilo Kartoffeln.“*
    * Đáp án chấp nhận: `["teurer"]`
    * Dịch nghĩa câu: *„Một ký thịt đắt hơn một ký khoai tây.“*
    * Giải thích: `teuer → teurer` (bỏ `e`) rồi + `als`.
16. **Câu 16**: Điền `viel / viele / mehr` phù hợp (so sánh hơn): *„Mein Bruder isst ___ Reis als ich.“*
    * Đáp án chấp nhận: `["mehr"]`
    * Dịch nghĩa câu: *„Anh trai tôi ăn cơm nhiều hơn tôi.“*
    * Giải thích: Có `als ich` (đối tượng so sánh) → Komparativ của `viel` là **`mehr`**.
17. **Câu 17**: Điền cụm so sánh nhất của `gern`: *„Von allen Früchten esse ich ___ Erdbeeren.“*
    * Đáp án chấp nhận: `["am liebsten"]`
    * Dịch nghĩa câu: *„Trong tất cả các loại trái cây, tôi thích ăn dâu tây nhất.“*
    * Giải thích: Superlativ của `gern` = **`am liebsten`**.
18. **Câu 18**: Điền dạng so sánh hơn của `gesund`: *„Der Salat ist gesund, aber Möhren sind noch ___.“*
    * Đáp án chấp nhận: `["gesünder", "gesuender"]`
    * Dịch nghĩa câu: *„Salad tốt cho sức khỏe, nhưng cà rốt còn tốt hơn nữa.“*
    * Giải thích: `gesund → gesünder` (thêm Umlaut `u → ü`).
19. **Câu 19**: Chia động từ `essen` ở ngôi `du`: *„Du ___ gern Fisch.“*
    * Đáp án chấp nhận: `["isst"]`
    * Dịch nghĩa câu: *„Bạn thích ăn cá.“*
    * Giải thích: `essen` đổi `e → i` ở `du` → **`isst`**.
20. **Câu 20**: Chia động từ `kosten`: *„Was ___ ein Kilo Birnen?“*
    * Đáp án chấp nhận: `["kostet"]`
    * Dịch nghĩa câu: *„Một ký lê giá bao nhiêu?“*
    * Giải thích: Chủ ngữ `ein Kilo Birnen` là **số ít** → **`kostet`**.
21. **Câu 21**: Chia động từ `kosten`: *„Wie viel ___ drei Dosen Cola?“*
    * Đáp án chấp nhận: `["kosten"]`
    * Dịch nghĩa câu: *„Ba lon cô-ca giá bao nhiêu?“*
    * Giải thích: `drei Dosen` là **số nhiều** → **`kosten`**.
22. **Câu 22**: Chia động từ `kochen` ở ngôi `ihr`: *„Ihr ___ heute Abend Nudeln.“*
    * Đáp án chấp nhận: `["kocht"]`
    * Dịch nghĩa câu: *„Tối nay các bạn nấu mì.“*
    * Giải thích: `kochen`: gốc `koch-` + `-t` ở `ihr` → **`kocht`**.

---

#### NHÓM 3: DỊCH TỪ / CỤM TỪ VIỆT → ĐỨC (`dich_nghia_vd` — 8 Câu: Câu 23 → Câu 30)
23. **Câu 23**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"cà rốt"***
    * Đáp án chấp nhận: `["die Möhre", "Möhre", "die Karotte", "Karotte"]`
    * Giải thích: Cà rốt là **`die Möhre`** (cũng gọi `die Karotte`); số nhiều `die Möhren`.
24. **Câu 24**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"hành tây"***
    * Đáp án chấp nhận: `["die Zwiebel", "Zwiebel"]`
    * Giải thích: Hành tây là **`die Zwiebel`** (số nhiều: `die Zwiebeln`).
25. **Câu 25**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"thịt gà"***
    * Đáp án chấp nhận: `["das Hähnchen", "Hähnchen", "das Haehnchen"]`
    * Giải thích: Thịt gà là **`das Hähnchen`** (đuôi `-chen` luôn là `das`).
26. **Câu 26**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"gạo, cơm"***
    * Đáp án chấp nhận: `["der Reis", "Reis"]`
    * Giải thích: Gạo là **`der Reis`** (giống đực, chỉ số ít).
27. **Câu 27**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"ngũ cốc ăn sáng"***
    * Đáp án chấp nhận: `["das Müsli", "Müsli", "das Muesli"]`
    * Giải thích: Ngũ cốc ăn sáng là **`das Müsli`** (số nhiều: `die Müslis`).
28. **Câu 28**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"quả dứa"***
    * Đáp án chấp nhận: `["die Ananas", "Ananas"]`
    * Giải thích: Quả dứa là **`die Ananas`** (số nhiều giữ nguyên: `die Ananas`).
29. **Câu 29**: Dịch sang tiếng Đức: ***"một lon cô-ca"***
    * Đáp án chấp nhận: `["eine Dose Cola", "eine Dose cola"]`
    * Giải thích: `die Dose` là giống cái → **`eine Dose Cola`** (không cần giới từ giữa đơn vị và vật).
30. **Câu 30**: Dịch sang tiếng Đức: ***"một lít sữa"***
    * Đáp án chấp nhận: `["ein Liter Milch", "einen Liter Milch"]`
    * Giải thích: `der Liter` + `die Milch` → **`ein Liter Milch`** (khi là tân ngữ: `einen Liter Milch`).

---

#### NHÓM 4: DỊCH TỪ / CÂU NGẮN ĐỨC → VIỆT (`dich_nghia_dv` — 8 Câu: Câu 31 → Câu 38)
31. **Câu 31**: Dịch sang tiếng Việt: ***„der Schinken“***
    * Đáp án chấp nhận: `["thịt xông khói", "giăm bông", "thịt nguội", "thịt giăm bông"]`
    * Giải thích: `der Schinken` là thịt xông khói / giăm bông (số nhiều: `die Schinken`).
32. **Câu 32**: Dịch sang tiếng Việt: ***„die Paprika“***
    * Đáp án chấp nhận: `["ớt chuông", "quả ớt chuông", "ớt ngọt"]`
    * Giải thích: `die Paprika` là ớt chuông (số nhiều: `die Paprikas`).
33. **Câu 33**: Dịch sang tiếng Việt: ***„das Schnitzel“***
    * Đáp án chấp nhận: `["thịt tẩm bột chiên", "món thịt tẩm bột chiên", "schnitzel", "thịt chiên xù"]`
    * Giải thích: `das Schnitzel` là miếng thịt tẩm bột chiên (số nhiều: `die Schnitzel`).
34. **Câu 34**: Dịch sang tiếng Việt: ***„die Erdbeere“***
    * Đáp án chấp nhận: `["dâu tây", "quả dâu tây"]`
    * Giải thích: `die Erdbeere` là dâu tây (số nhiều: `die Erdbeeren`).
35. **Câu 35**: Dịch sang tiếng Việt: ***„Das macht zusammen vier Euro.“***
    * Đáp án chấp nhận: `["Tổng cộng là bốn euro.", "Tất cả là bốn euro.", "Cộng lại là bốn euro.", "Tổng cộng bốn euro."]`
    * Giải thích: `Das macht zusammen …` = *"tổng cộng là …"*; `vier Euro` = bốn euro.
36. **Câu 36**: Dịch sang tiếng Việt: ***„Haben Sie Schokolade?“***
    * Đáp án chấp nhận: `["Ngài có sô cô la không?", "Bạn có sô cô la không?", "Bà có sô cô la không?", "Ông có sô cô la không?", "Anh chị có sô cô la không?"]`
    * Giải thích: `Haben Sie …?` là câu hỏi lịch sự xem cửa hàng có món gì không; `Sie` = ngài / bạn (lịch sự).
37. **Câu 37**: Dịch sang tiếng Việt: ***„Ich hätte gern einen Liter Milch.“***
    * Đáp án chấp nhận: `["Tôi muốn lấy một lít sữa.", "Tôi muốn một lít sữa.", "Cho tôi một lít sữa."]`
    * Giải thích: `Ich hätte gern …` = *"tôi muốn lấy …"* (lịch sự); `einen Liter Milch` là tân ngữ Akkusativ.
38. **Câu 38**: Dịch sang tiếng Việt: ***„Wie viel kosten die Birnen?“***
    * Đáp án chấp nhận: `["Những quả lê giá bao nhiêu?", "Lê giá bao nhiêu?", "Những quả lê bao nhiêu tiền?", "Mấy quả lê này giá bao nhiêu?"]`
    * Giải thích: `Wie viel kosten …?` dùng cho **số nhiều** (`die Birnen`) = *"… giá bao nhiêu?"*.

---

#### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 8 Bài: Câu 39 → Câu 46, mỗi bài 4 cặp độc nhất)
39. **Câu 39 (Bài nối 1 — Từ Đức ↔ nghĩa Việt, trái cây)**:
    * `die Birne` ↔ `quả lê`
    * `die Erdbeere` ↔ `dâu tây`
    * `die Orange` ↔ `quả cam`
    * `die Ananas` ↔ `quả dứa`
    * Giải thích: Bốn loại trái cây đều là giống cái (`die`).
40. **Câu 40 (Bài nối 2 — Số ít ↔ Số nhiều)**:
    * `der Apfel` ↔ `die Äpfel`
    * `das Ei` ↔ `die Eier`
    * `die Kartoffel` ↔ `die Kartoffeln`
    * `der Kuchen` ↔ `die Kuchen`
    * Dịch nghĩa các cặp: *quả táo – những quả táo; quả trứng – những quả trứng; củ khoai tây – những củ khoai tây; bánh ngọt – những chiếc bánh ngọt.*
    * Giải thích: `Apfel` thêm Umlaut, `Ei` thêm `-er`, `Kartoffel` thêm `-n`, `Kuchen` giữ nguyên.
41. **Câu 41 (Bài nối 3 — Câu hỏi `Welch-` ↔ Câu trả lời phù hợp)**:
    * `Welche Orangen sind frisch?` ↔ `Die Orangen aus Spanien.`
    * `Welches Brot schmeckt gut?` ↔ `Das Brot vom Bäcker.`
    * `Welchen Joghurt kaufst du?` ↔ `Den Joghurt mit Erdbeeren.`
    * `Welcher Fisch ist heute billig?` ↔ `Der Fisch aus dem Fluss.`
    * Dịch nghĩa các cặp: *Những quả cam nào tươi? – Những quả cam từ Tây Ban Nha. | Loại bánh mì nào ngon? – Bánh mì của tiệm bánh. | Bạn mua loại sữa chua nào? – Sữa chua vị dâu tây. | Con cá nào hôm nay rẻ? – Con cá từ sông.*
    * Giải thích: Câu trả lời dùng mạo từ xác định cùng giống - cách với `welch-` (`welche → die`, `welches → das`, `welchen → den`, `welcher → der`).
42. **Câu 42 (Bài nối 4 — Nguyên mẫu ↔ Ngôi `er` ở Präsens)**:
    * `essen` ↔ `isst`
    * `nehmen` ↔ `nimmt`
    * `geben` ↔ `gibt`
    * `empfehlen` ↔ `empfiehlt`
    * Dịch nghĩa các cặp: *ăn – (anh ấy) ăn; lấy – (anh ấy) lấy; cho / có – (nó) cho / có; giới thiệu – (anh ấy) giới thiệu.*
    * Giải thích: Bốn động từ bất quy tắc đổi nguyên âm `e → i / ie` ở `er/sie/es`.
43. **Câu 43 (Bài nối 5 — Nguyên mẫu ↔ Partizip II, ôn Bài 9)**:
    * `kaufen` ↔ `gekauft`
    * `essen` ↔ `gegessen`
    * `bestellen` ↔ `bestellt`
    * `einkaufen` ↔ `eingekauft`
    * Dịch nghĩa các cặp: *mua – đã mua; ăn – đã ăn; gọi món – đã gọi món; mua sắm – đã mua sắm.*
    * Giải thích: `kaufen` (`ge-t`), `essen` (bất quy tắc), `bestellen` (tiền tố `be-`, không `ge-`), `einkaufen` (tiền tố tách: `ein` + `ge` + `kauft`).
44. **Câu 44 (Bài nối 6 — Tính từ ↔ Komparativ)**:
    * `billig` ↔ `billiger`
    * `teuer` ↔ `teurer`
    * `gesund` ↔ `gesünder`
    * `groß` ↔ `größer`
    * Dịch nghĩa các cặp: *rẻ – rẻ hơn; đắt – đắt hơn; tốt cho sức khỏe – tốt cho sức khỏe hơn; to – to hơn.*
    * Giải thích: `teuer` bỏ `e`; `gesund` và `groß` thêm Umlaut.
45. **Câu 45 (Bài nối 7 — Từ gốc ↔ Superlativ)**:
    * `gern` ↔ `am liebsten`
    * `viel` ↔ `am meisten`
    * `gut` ↔ `am besten`
    * `billig` ↔ `am billigsten`
    * Dịch nghĩa các cặp: *thích – thích nhất; nhiều – nhiều nhất; tốt – tốt nhất; rẻ – rẻ nhất.*
    * Giải thích: Ba cặp đầu là bất quy tắc; `billig` theo quy tắc `am + …sten`.
46. **Câu 46 (Bài nối 8 — Đơn vị ↔ Thực phẩm đi cặp)**:
    * `eine Dose` ↔ `Cola`
    * `eine Flasche` ↔ `Wasser`
    * `ein Liter` ↔ `Milch`
    * `ein Kilo` ↔ `Kartoffeln`
    * Dịch nghĩa các cặp: *một lon – cô-ca; một chai – nước; một lít – sữa; một ký – khoai tây.*
    * Giải thích: `eine Dose Cola`, `eine Flasche Wasser`, `ein Liter Milch`, `ein Kilo Kartoffeln` là các cụm đơn vị thông dụng.

---

#### NHÓM 6: ĐIỀN VÀO 2 CHỖ TRỐNG TẠO CÂU (`dien_tao_cau` — 8 Câu: Câu 47 → Câu 54)
47. **Câu 47**: Điền 2 từ để hoàn thành hội thoại: *„Bạn muốn xà lách nào? — Xin cho xà lách này.“*
    * Khung câu hiển thị: `[1] Salat möchten Sie? — [2] Salat, bitte.`
    * Đáp án từng ô: Ô 1 = `["welchen"]`, Ô 2 = `["den"]`.
    * Giải thích: `der Salat` là tân ngữ → Akkusativ → câu hỏi **`Welchen`**, câu trả lời **`Den`**.
48. **Câu 48**: Điền 2 từ để hoàn thành câu: *„Hôm nay cà rốt rẻ hơn cà chua.“*
    * Khung câu hiển thị: `Die Möhren sind heute [1] [2] die Tomaten.`
    * Đáp án từng ô: Ô 1 = `["billiger"]`, Ô 2 = `["als"]`.
    * Giải thích: Komparativ của `billig` là **`billiger`**, nối với vế sau bằng **`als`**.
49. **Câu 49**: Điền 2 từ để hoàn thành câu: *„Tôi ăn gạo nhiều hơn mì.“*
    * Khung câu hiển thị: `Ich esse [1] Reis [2] Nudeln.`
    * Đáp án từng ô: Ô 1 = `["mehr"]`, Ô 2 = `["als"]`.
    * Giải thích: Cấu trúc **`mehr … als`**.
50. **Câu 50**: Điền 2 từ để hoàn thành câu: *„Tôi thích ăn kem hơn bánh ngọt.“*
    * Khung câu hiển thị: `Ich esse [1] Eis [2] Kuchen.`
    * Đáp án từng ô: Ô 1 = `["lieber"]`, Ô 2 = `["als"]`.
    * Giải thích: Cấu trúc **`lieber … als`** (Komparativ của `gern`).
51. **Câu 51**: Điền 2 từ để hoàn thành câu: *„Anna nấu ăn ngon hơn anh trai của cô ấy.“*
    * Khung câu hiển thị: `Anna kocht [1] [2] ihr Bruder.`
    * Đáp án từng ô: Ô 1 = `["besser"]`, Ô 2 = `["als"]`.
    * Giải thích: Komparativ của `gut` là **`besser`**; so sánh hơn dùng **`als`**.
52. **Câu 52**: Điền 2 từ để hoàn thành câu (chú ý chữ hoa đầu câu): *„Tôi thích ăn cá nhất.“*
    * Khung câu hiển thị: `[1] [2] esse ich Fisch.`
    * Đáp án từng ô: Ô 1 = `["am"]`, Ô 2 = `["liebsten"]`.
    * Giải thích: Superlativ của `gern` = **`am liebsten`**, đứng đầu câu nên động từ `esse` ở vị trí ②: **`Am liebsten esse ich Fisch.`**
53. **Câu 53**: Điền 2 dạng của `kosten`: *„Một ký táo giá 2,40 euro. Hai ký giá 4,80 euro.“*
    * Khung câu hiển thị: `Ein Kilo Äpfel [1] 2,40 €. Zwei Kilo [2] 4,80 €.`
    * Đáp án từng ô: Ô 1 = `["kostet"]`, Ô 2 = `["kosten"]`.
    * Giải thích: `ein Kilo Äpfel` là số ít → **`kostet`**; `zwei Kilo` là số nhiều → **`kosten`**. *(Voice đọc: „Ein Kilo Äpfel kostet zwei Euro vierzig. Zwei Kilo kosten vier Euro achtzig.“)*
54. **Câu 54**: Điền 2 Partizip II (ôn Bài 9) để hoàn thành câu: *„Hôm qua tôi đã mua rau củ ở chợ và đã thử hoa quả.“*
    * Khung câu hiển thị: `Gestern habe ich auf dem Markt Gemüse [1] und Obst [2].`
    * Đáp án từng ô: Ô 1 = `["gekauft"]`, Ô 2 = `["probiert"]`.
    * Giải thích: `kaufen → gekauft` (`ge-t`); `probieren → probiert` (đuôi `-ieren`, không `ge-`).

---

#### NHÓM 7: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 8 Câu: Câu 55 → Câu 62)
55. **Câu 55**:
    * `audio_text`: *"Welches Obst kaufst du am liebsten?"*
    * `display_sentence`: *"___ Obst kaufst du am liebsten?"*
    * `hint_vi`: *"Bạn thích mua loại hoa quả nào nhất?"*
    * `accepted_answers`: `["welches"]`
    * Giải thích: `das Obst` (giống trung) → **`Welches`**.
56. **Câu 56**:
    * `audio_text`: *"Ein Kilo Birnen kostet zwei Euro neunzig."*
    * `display_sentence`: *"Ein Kilo Birnen kostet ___ Euro neunzig."*
    * `hint_vi`: *"Một ký lê giá hai euro chín mươi."*
    * `accepted_answers`: `["zwei", "2"]`
    * Giải thích: Giá `2,90 €` đọc là **`zwei Euro neunzig`**.
57. **Câu 57**:
    * `audio_text`: *"Meine Schwester isst mehr Gemüse als ich."*
    * `display_sentence`: *"Meine Schwester isst ___ Gemüse als ich."*
    * `hint_vi`: *"Chị tôi ăn rau củ nhiều hơn tôi."*
    * `accepted_answers`: `["mehr"]`
    * Giải thích: Có `als ich` → Komparativ của `viel` là **`mehr`**.
58. **Câu 58**:
    * `audio_text`: *"Das Brot beim Bäcker ist besser als im Supermarkt."*
    * `display_sentence`: *"Das Brot beim Bäcker ist ___ als im Supermarkt."*
    * `hint_vi`: *"Bánh mì ở tiệm bánh ngon hơn ở siêu thị."*
    * `accepted_answers`: `["besser"]`
    * Giải thích: Komparativ của `gut` là **`besser`**.
59. **Câu 59**:
    * `audio_text`: *"Zum Frühstück esse ich Müsli mit Milch."*
    * `display_sentence`: *"Zum Frühstück esse ich ___ mit Milch."*
    * `hint_vi`: *"Vào bữa sáng tôi ăn ngũ cốc với sữa."*
    * `accepted_answers`: `["müsli", "muesli"]`
    * Giải thích: `das Müsli` là ngũ cốc ăn sáng.
60. **Câu 60**:
    * `audio_text`: *"Was darf es sein? Ich hätte gern zwei Kilo Äpfel."*
    * `display_sentence`: *"Was darf es sein? Ich ___ gern zwei Kilo Äpfel."*
    * `hint_vi`: *"Ngài cần gì ạ? Tôi muốn lấy hai ký táo."*
    * `accepted_answers`: `["hätte", "haette"]`
    * Giải thích: Cụm lịch sự cố định **`ich hätte gern`**.
61. **Câu 61**:
    * `audio_text`: *"Das macht zusammen neun Euro achtzig."*
    * `display_sentence`: *"Das macht zusammen neun Euro ___."*
    * `hint_vi`: *"Tổng cộng là chín euro tám mươi."*
    * `accepted_answers`: `["achtzig", "80"]`
    * Giải thích: `9,80 €` đọc là **`neun Euro achtzig`**.
62. **Câu 62**:
    * `audio_text`: *"Gestern haben wir Nudeln gekocht."*
    * `display_sentence`: *"Gestern haben wir Nudeln ___."*
    * `hint_vi`: *"Hôm qua chúng tôi đã nấu mì."*
    * `accepted_answers`: `["gekocht"]`
    * Giải thích: `kochen → gekocht` (`ge-t`), dùng với `haben`.

---

#### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (`dich_cau_vd` — 6 Câu: Câu 63 → Câu 68, chấm đa đáp án)
63. **Câu 63**: Dịch câu hỏi sau sang tiếng Đức: ***"Bạn muốn mua chiếc bánh ngọt nào?"***
    * `accepted_answers`:
      * `"Welchen Kuchen möchtest du kaufen?"`
      * `"Welchen Kuchen möchten Sie kaufen?"`
      * `"Welchen Kuchen möchtet ihr kaufen?"`
    * Giải thích: `der Kuchen` là tân ngữ → Akkusativ → **`Welchen Kuchen`**; `möchten` ở vị trí 2, động từ `kaufen` ở cuối câu.
64. **Câu 64**: Dịch câu sau sang tiếng Đức: ***"Quả cam rẻ hơn quả dứa."***
    * `accepted_answers`:
      * `"Die Orange ist billiger als die Ananas."`
    * Giải thích: `die Orange`, `die Ananas` đều giống cái; Komparativ **`billiger`** + `als`.
65. **Câu 65**: Dịch câu sau sang tiếng Đức: ***"Tôi thích ăn cá hơn thịt."***
    * `accepted_answers`:
      * `"Ich esse lieber Fisch als Fleisch."`
      * `"Ich esse Fisch lieber als Fleisch."`
      * `"Lieber esse ich Fisch als Fleisch."`
    * Giải thích: Cấu trúc **`lieber … als`** (Komparativ của `gern`).
66. **Câu 66**: Dịch câu sau sang tiếng Đức: ***"Trong gia đình tôi, bố nấu ăn ngon nhất."***
    * `accepted_answers`:
      * `"In meiner Familie kocht mein Vater am besten."`
      * `"Mein Vater kocht in meiner Familie am besten."`
    * Giải thích: Superlativ của `gut` là **`am besten`**; `in meiner Familie` (Wo? + Dativ).
67. **Câu 67**: Dịch câu hỏi sau sang tiếng Đức: ***"Hai lít sữa giá bao nhiêu?"***
    * `accepted_answers`:
      * `"Wie viel kosten zwei Liter Milch?"`
      * `"Was kosten zwei Liter Milch?"`
    * Giải thích: `zwei Liter` là số nhiều → **`kosten`**; `Liter` giữ nguyên số ít sau số đếm.
68. **Câu 68**: Dịch câu sau sang tiếng Đức (Perfekt): ***"Hôm qua tôi đã nấu mì và ăn salad."***
    * `accepted_answers`:
      * `"Gestern habe ich Nudeln gekocht und Salat gegessen."`
      * `"Ich habe gestern Nudeln gekocht und Salat gegessen."`
      * `"Gestern habe ich Nudeln gekocht und habe Salat gegessen."`
    * Giải thích: `kochen → gekocht`, `essen → gegessen`; cả hai dùng `haben`, nên `habe` chỉ cần xuất hiện một lần.

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (`dich_cau_dv` — 6 Câu: Câu 69 → Câu 74, chấm đa đáp án)
69. **Câu 69**: Dịch câu sau sang tiếng Việt: ***„Welche Äpfel sind süß? — Die Äpfel von meiner Oma.“***
    * `accepted_answers`:
      * `"Những quả táo nào ngọt? — Những quả táo của bà tôi."`
      * `"Những quả táo nào ngọt vậy? — Những quả táo của bà tôi."`
    * Giải thích: `Welche Äpfel` (số nhiều, chủ ngữ); trả lời bằng `Die Äpfel von …`.
70. **Câu 70**: Dịch câu sau sang tiếng Việt: ***„In Vietnam essen die Menschen mehr Reis als Brot.“***
    * `accepted_answers`:
      * `"Ở Việt Nam mọi người ăn gạo nhiều hơn bánh mì."`
      * `"Ở Việt Nam người ta ăn cơm nhiều hơn bánh mì."`
      * `"Ở Việt Nam người dân ăn cơm nhiều hơn bánh mì."`
    * Giải thích: Cấu trúc `mehr … als` (nhiều hơn).
71. **Câu 71**: Dịch câu sau sang tiếng Việt: ***„Am meisten kaufe ich Obst und Gemüse auf dem Markt.“***
    * `accepted_answers`:
      * `"Tôi mua nhiều nhất là hoa quả và rau củ ở chợ."`
      * `"Tôi mua hoa quả và rau củ ở chợ nhiều nhất."`
    * Giải thích: `Am meisten` (nhiều nhất) đứng đầu câu nên động từ `kaufe` ở vị trí ②.
72. **Câu 72**: Dịch câu sau sang tiếng Việt: ***„Meine Schwester trinkt lieber Saft als Cola, aber am liebsten trinkt sie Wasser.“***
    * `accepted_answers`:
      * `"Chị tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước lọc nhất."`
      * `"Chị tôi thích nước ép hơn cola, nhưng thích nhất là uống nước."`
      * `"Chị gái tôi thích uống nước ép hơn cô-ca, nhưng thích uống nước nhất."`
    * Giải thích: `lieber … als` (thích hơn); `am liebsten` (thích nhất).
73. **Câu 73**: Dịch đoạn hội thoại sau sang tiếng Việt: ***„Guten Tag, ich hätte gern ein Pfund Erdbeeren. — Gern. Sonst noch etwas? — Nein, danke. Was macht das?“***
    * `accepted_answers`:
      * `"Xin chào, tôi muốn lấy nửa ký dâu tây. — Vâng. Ngài cần gì nữa không? — Không, cảm ơn. Tổng cộng bao nhiêu?"`
      * `"Chào bạn, tôi muốn lấy nửa ký dâu tây. — Vâng. Bạn cần gì nữa không? — Không, cảm ơn. Hết bao nhiêu vậy?"`
    * Giải thích: `ein Pfund` = nửa ký (500 g); `Was macht das?` = *"tất cả là bao nhiêu?"*
74. **Câu 74**: Dịch câu sau sang tiếng Việt: ***„Gestern hat Herr Bauer im Supermarkt zwei Kilo Kartoffeln und eine Flasche Milch gekauft.“***
    * `accepted_answers`:
      * `"Hôm qua ông Bauer đã mua hai ký khoai tây và một chai sữa ở siêu thị."`
      * `"Hôm qua ở siêu thị ông Bauer đã mua hai ký khoai tây và một chai sữa."`
    * Giải thích: Perfekt `hat … gekauft`; `Kilo` giữ nguyên số ít, `Flasche` là giống cái.

---

#### NHÓM 10: SẮP XẾP TỪ THÀNH CÂU (`sap_xep_cau` — 5 Câu: Câu 75 → Câu 79)
75. **Câu 75**
    * `tokens` (đã xáo trộn): `[nimmst, Welchen, du, Fisch]`
    * `accepted_answers`: `["Welchen Fisch nimmst du?"]`
    * Dịch nghĩa câu: *„Bạn lấy con cá nào?“*
    * Giải thích: Cụm `Welchen Fisch` ở vị trí ①, động từ `nimmst` ở vị trí ②, chủ ngữ `du` ở ③.
76. **Câu 76**
    * `tokens`: `[Reis, esse, ich, lieber, als, Nudeln]`
    * `accepted_answers`: `["Ich esse lieber Reis als Nudeln.", "Ich esse Reis lieber als Nudeln.", "Lieber esse ich Reis als Nudeln."]`
    * Dịch nghĩa câu: *„Tôi thích ăn cơm hơn mì.“*
    * Giải thích: Cấu trúc `lieber … als`; nếu `Lieber` đứng đầu câu thì `esse` ở vị trí ② rồi đến `ich`.
77. **Câu 77**
    * `tokens`: `[Am meisten, kauft, meine Mutter, Obst]`
    * `accepted_answers`: `["Am meisten kauft meine Mutter Obst.", "Meine Mutter kauft am meisten Obst."]`
    * Dịch nghĩa câu: *„Mẹ tôi mua hoa quả nhiều nhất.“*
    * Giải thích: Nếu `Am meisten` đứng đầu câu thì động từ `kauft` ở vị trí ②, chủ ngữ `meine Mutter` ở vị trí ③.
78. **Câu 78**
    * `tokens`: `[kostet, Wie viel, der Käse]`
    * `accepted_answers`: `["Wie viel kostet der Käse?"]`
    * Dịch nghĩa câu: *„Phô mai giá bao nhiêu?“*
    * Giải thích: `Wie viel` ở vị trí ①, `kostet` ở vị trí ② (chủ ngữ số ít `der Käse`).
79. **Câu 79**
    * `tokens`: `[billiger, die Birnen, als, sind, die Erdbeeren]`
    * `accepted_answers`: `["Die Birnen sind billiger als die Erdbeeren."]`
    * Dịch nghĩa câu: *„Những quả lê rẻ hơn những quả dâu tây.“*
    * Giải thích: Cấu trúc `A + sind + Komparativ + als + B`.

---

#### NHÓM 11: 🆕 PHÂN LOẠI `DER / DIE / DAS` (`phan_loai_giong` — 4 Câu: Câu 80 → Câu 83, kèm bảng nhắc giống ở đầu mỗi câu)
Mỗi câu: xếp **4 danh từ** vào đúng mạo từ. Đúng khi cả 4 đều đúng.
80. **Câu 80**: Xếp các danh từ sau:
    * `Käse` (phô mai) → **der** (`der Käse`)
    * `Butter` (bơ) → **die** (`die Butter`)
    * `Brot` (bánh mì) → **das** (`das Brot`)
    * `Fisch` (cá) → **der** (`der Fisch`)
    * Giải thích: `Käse` và `Fisch` giống đực; `Butter` giống cái; `Brot` giống trung.
81. **Câu 81**: Xếp các danh từ sau:
    * `Banane` (quả chuối) → **die** (`die Banane`)
    * `Fleisch` (thịt) → **das** (`das Fleisch`)
    * `Apfel` (quả táo) → **der** (`der Apfel`)
    * `Zwiebel` (hành tây) → **die** (`die Zwiebel`)
    * Giải thích: `Banane` và `Zwiebel` giống cái; `Fleisch` giống trung; `Apfel` giống đực.
82. **Câu 82**: Xếp các danh từ sau:
    * `Ei` (quả trứng) → **das** (`das Ei`)
    * `Nudel` (sợi mì) → **die** (`die Nudel`)
    * `Salat` (xà lách) → **der** (`der Salat`)
    * `Reis` (gạo) → **der** (`der Reis`)
    * Giải thích: **`der Reis`** giống đực (bảng giảng ghi `s.` là chưa chuẩn); `der Salat` giống đực; `das Ei`; `die Nudel`.
83. **Câu 83**: Xếp các danh từ sau:
    * `Möhre` (cà rốt) → **die** (`die Möhre`)
    * `Schinken` (giăm bông) → **der** (`der Schinken`)
    * `Gemüse` (rau củ) → **das** (`das Gemüse`)
    * `Orange` (quả cam) → **die** (`die Orange`)
    * Giải thích: `Möhre`, `Orange` giống cái; `Schinken` giống đực; `Gemüse` giống trung.

---

#### NHÓM 12: TÌM LỖI VÀ SỬA CÂU (`tim_loi_sai` — 4 Câu: Câu 84 → Câu 87)
Mỗi câu có **đúng 1 lỗi**. Người học gõ lại **cả câu đúng**.
84. **Câu 84** *(lỗi `welch-` cách)*
    * `wrong_sentence`: *„Welcher Käse möchten Sie kaufen?“*
    * `accepted_answers`: `["Welchen Käse möchten Sie kaufen?"]`
    * Dịch nghĩa câu đúng: *„Ngài muốn mua loại phô mai nào?“*
    * Giải thích: Lỗi cách của từ hỏi 'welch-': danh từ 'der Käse' (giống đực) đóng vai trò tân ngữ trực tiếp (Akkusativ) của động từ 'kaufen' nên từ hỏi biến đổi thành 'Welchen', không phải 'Welcher'. -> Đáp án: "Welchen Käse möchten Sie kaufen?"
85. **Câu 85** *(lỗi `als / wie`)*
    * `wrong_sentence`: *„Ich esse mehr Kartoffeln wie Reis.“*
    * `accepted_answers`: `["Ich esse mehr Kartoffeln als Reis."]`
    * Dịch nghĩa câu đúng: *„Tôi ăn khoai tây nhiều hơn cơm.“*
    * Giải thích: Lỗi dùng từ nối trong phép so sánh hơn: trong tiếng Đức chuẩn, so sánh hơn (Komparativ) bắt buộc dùng liên từ 'als', không dùng 'wie' ('wie' chỉ dùng cho so sánh ngang bằng 'so ... wie'). -> Đáp án: "Ich esse mehr Kartoffeln als Reis."
86. **Câu 86** *(lỗi Komparativ bất quy tắc)*
    * `wrong_sentence`: *„Der Fisch ist gutter als das Fleisch.“*
    * `accepted_answers`: `["Der Fisch ist besser als das Fleisch."]`
    * Dịch nghĩa câu đúng: *„Cá ngon hơn thịt.“*
    * Giải thích: Komparativ của `gut` là **`besser`** (bất quy tắc), không phải `gutter`.
87. **Câu 87** *(lỗi vị trí động từ)*
    * `wrong_sentence`: *„Am liebsten ich trinke Milch.“*
    * `accepted_answers`: `["Am liebsten trinke ich Milch.", "Ich trinke am liebsten Milch."]`
    * Dịch nghĩa câu đúng: *„Tôi thích uống sữa nhất.“*
    * Giải thích: Lỗi vị trí động từ (Verbzweitstellung - V2): khi đưa cụm so sánh nhất 'Am liebsten' lên đầu câu (Vị trí 1), động từ chia 'trinke' bắt buộc phải đứng ở Vị trí 2 rồi mới đến chủ ngữ 'ich'. -> Đáp án: "Am liebsten trinke ich Milch." (hoặc "Ich trinke am liebsten Milch.").

---

#### NHÓM 13: 🆕 VIẾT LẠI CÂU THÀNH SO SÁNH (`viet_lai_so_sanh` — 4 Câu: Câu 88 → Câu 91)
88. **Câu 88**
    * `source_sentence`: *„Der Kaffee ist heiß.“*
    * `instruction_vi`: *Viết lại thành so sánh hơn với đối tượng `der Tee`.*
    * `accepted_answers`: `["Der Kaffee ist heißer als der Tee."]`
    * Dịch nghĩa câu đáp án: *„Cà phê nóng hơn trà.“*
    * Giải thích: `heiß → heißer` (giữ nguyên `ß`), thêm `als der Tee`.
89. **Câu 89**
    * `source_sentence`: *„Meine Schwester isst gern Gemüse.“*
    * `instruction_vi`: *Viết lại thành so sánh hơn với đối tượng `Obst`.*
    * `accepted_answers`: `["Meine Schwester isst lieber Gemüse als Obst.", "Meine Schwester isst Gemüse lieber als Obst."]`
    * Dịch nghĩa câu đáp án: *„Chị tôi thích ăn rau củ hơn hoa quả.“*
    * Giải thích: `gern → lieber`, thêm `als Obst`.
90. **Câu 90**
    * `source_sentence`: *„Meine Mutter kocht gut.“*
    * `instruction_vi`: *Viết lại thành so sánh nhất (không thêm đối tượng).*
    * `accepted_answers`: `["Meine Mutter kocht am besten."]`
    * Dịch nghĩa câu đáp án: *„Mẹ tôi nấu ăn ngon nhất.“*
    * Giải thích: `gut → am besten` (bất quy tắc).
91. **Câu 91**
    * `source_sentence`: *„Wir trinken viel Wasser.“*
    * `instruction_vi`: *Viết lại thành so sánh hơn với đối tượng `Saft`.*
    * `accepted_answers`: `["Wir trinken mehr Wasser als Saft."]`
    * Dịch nghĩa câu đáp án: *„Chúng tôi uống nước lọc nhiều hơn nước ép.“*
    * Giải thích: `viel → mehr`, thêm `als Saft`.

---

#### NHÓM 14: ĐỌC HIỂU ĐÚNG / SAI — RICHTIG / FALSCH (`dung_sai` — 3 Câu: Câu 92 → Câu 94)
**Đoạn văn A** *(dùng cho Câu 92 và 93; khi đọc `🔊`, giá `2,50` đọc là `zwei Euro fünfzig`, `1,20` đọc là `ein Euro zwanzig`)*:
> *„Frau Becker geht jeden Samstag auf den Markt. Sie kauft dort frisches Gemüse und Obst. Die Tomaten kosten 2,50 Euro das Kilo, die Möhren nur 1,20 Euro. Sie nimmt zwei Kilo Tomaten und ein Kilo Möhren. Am liebsten isst sie Erdbeeren, aber im Winter gibt es keine.“*
> **Dịch**: *„Bà Becker đi chợ vào mỗi thứ Bảy. Bà mua ở đó rau củ và hoa quả tươi. Cà chua giá 2,50 euro một ký, cà rốt chỉ 1,20 euro. Bà lấy hai ký cà chua và một ký cà rốt. Bà thích ăn dâu tây nhất, nhưng vào mùa đông không có.“*

92. **Câu 92**: Mệnh đề: *„Die Möhren sind billiger als die Tomaten.“*
    * Đáp án: **Richtig (Đúng)**
    * Dịch nghĩa mệnh đề: *„Cà rốt rẻ hơn cà chua.“*
    * Giải thích: Đoạn văn viết *„Die Tomaten kosten 2,50 Euro das Kilo, die Möhren nur 1,20 Euro.“* — 1,20 € < 2,50 € nên cà rốt rẻ hơn.
93. **Câu 93**: Mệnh đề: *„Frau Becker kauft zwei Kilo Möhren.“*
    * Đáp án: **Falsch (Sai)**
    * Dịch nghĩa mệnh đề: *„Bà Becker mua hai ký cà rốt.“*
    * Giải thích: Đoạn văn viết *„Sie nimmt zwei Kilo Tomaten und ein Kilo Möhren.“* — bà mua **hai ký cà chua** và **một ký cà rốt**.

**Đoạn văn B**:
> *„Tom isst am liebsten Pizza. Zu Hause kocht er oft Nudeln. Im Restaurant isst er mehr Salat als zu Hause.“*
> **Dịch**: *„Tom thích ăn pizza nhất. Ở nhà anh ấy thường nấu mì. Ở nhà hàng anh ấy ăn salad nhiều hơn ở nhà.“*

94. **Câu 94**: Mệnh đề: *„Tom isst zu Hause mehr Salat als im Restaurant.“*
    * Đáp án: **Falsch (Sai)**
    * Dịch nghĩa mệnh đề: *„Ở nhà Tom ăn salad nhiều hơn ở nhà hàng.“*
    * Giải thích: Đoạn văn viết *„Im Restaurant isst er mehr Salat als zu Hause.“* — **ở nhà hàng** anh ấy ăn salad nhiều hơn, không phải ở nhà.

---

#### NHÓM 15: 🆕 SẮP XẾP HỘI THOẠI MUA SẮM (`hoi_thoai_sap_xep` — 3 Câu: Câu 95 → Câu 97)
Mỗi ô là **một lượt lời** (kèm vai nói và câu tiếng Đức, không hiển thị tiếng Việt trước khi làm). Danh sách lượt lời được xáo trộn ngẫu nhiên khi render giao diện. Sau khi nộp bài, toàn bộ bản dịch tiếng Việt của hội thoại hiển thị trong khung **`📖 Dịch nghĩa:`**.
95. **Câu 95** *(tình huống: quầy trái cây)*
    * `lines` (thứ tự đúng 1 -> 6, web xáo trộn khi hiển thị):
      1. **Verkäufer**: *„Guten Tag! Bitte schön?“*
      2. **Kundin**: *„Ich möchte ein Pfund Erdbeeren und zwei Bananen, bitte.“*
      3. **Verkäufer**: *„Gern. Sonst noch etwas?“*
      4. **Kundin**: *„Nein, danke. Was macht das?“*
      5. **Verkäufer**: *„Das macht zusammen vier Euro fünfzig.“*
      6. **Kundin**: *„Hier sind fünf Euro. Stimmt so!“*
    * `correct_order`: `[1, 2, 3, 4, 5, 6]`
    * `translation` (hiển thị trong khung `📖 Dịch nghĩa:`): `Người bán: Xin chào! Ngài cần gì ạ? — Khách nữ: Tôi muốn mua nửa ký dâu tây và hai quả chuối, làm ơn. — Người bán: Vâng. Ngài cần gì thêm nữa không ạ? — Khách nữ: Không, cảm ơn. Tổng cộng hết bao nhiêu? — Người bán: Tổng cộng là bốn euro năm mươi (4,50 €). — Khách nữ: Đây là năm euro. Không cần thối lại đâu!`
    * Giải thích: Hội thoại đi theo trình tự **chào hỏi → gọi món → hỏi thêm → hỏi giá → báo giá → thanh toán**. *(Kiểm tra số: 1 Pfund Erdbeeren = 3,90 € + 2 × 0,30 € = 4,50 € = `vier Euro fünfzig`.)*
96. **Câu 96** *(tình huống: siêu thị)*
    * `lines` (thứ tự đúng 1 -> 6, web xáo trộn khi hiển thị):
      1. **Kunde**: *„Entschuldigung, wo finde ich den Joghurt?“*
      2. **Verkäufer**: *„Der Joghurt steht dort hinten.“*
      3. **Kunde**: *„Danke. Und wie viel kostet die Milch?“*
      4. **Verkäufer**: *„Ein Liter Milch kostet ein Euro zehn.“*
      5. **Kunde**: *„Gut, dann nehme ich zwei Liter.“*
      6. **Verkäufer**: *„Das macht zwei Euro zwanzig.“*
    * `correct_order`: `[1, 2, 3, 4, 5, 6]`
    * `translation` (hiển thị trong khung `📖 Dịch nghĩa:`): `Khách nam: Xin lỗi, tôi tìm sữa chua ở đâu ạ? — Người bán: Sữa chua ở phía sau kia. — Khách nam: Cảm ơn. Còn sữa giá bao nhiêu? — Người bán: Một lít sữa giá một euro mười (1,10 €). — Khách nam: Tốt, vậy tôi lấy hai lít. — Người bán: Tổng cộng là hai euro hai mươi (2,20 €).`
    * Giải thích: Hỏi vị trí → trả lời → hỏi giá → báo giá → quyết định mua → tính tiền. *(2 × 1,10 € = 2,20 € = `zwei Euro zwanzig`.)*
97. **Câu 97** *(tình huống: nhà hàng)*
    * `lines` (thứ tự đúng 1 -> 5, web xáo trộn khi hiển thị):
      1. **Kellner**: *„Guten Tag, haben Sie schon bestellt?“*
      2. **Gast**: *„Nein, noch nicht. Was empfehlen Sie?“*
      3. **Kellner**: *„Ich empfehle den Fisch mit Reis.“*
      4. **Gast**: *„Gut, dann nehme ich den Fisch und eine Flasche Wasser.“*
      5. **Kellner**: *„Gern, das kommt gleich.“*
    * `correct_order`: `[1, 2, 3, 4, 5]`
    * `translation` (hiển thị trong khung `📖 Dịch nghĩa:`): `Phục vụ: Xin chào, ngài đã gọi món chưa ạ? — Khách: Chưa. Ngài gợi ý món gì? — Phục vụ: Tôi gợi ý món cá ăn với cơm. — Khách: Tốt, vậy tôi lấy món cá và một chai nước. — Phục vụ: Vâng, có ngay ạ.`
    * Giải thích: Hỏi đã gọi món chưa → xin gợi ý → gợi ý → chọn món → xác nhận.

---

#### NHÓM 16: 🆕 NGHE GIÁ TIỀN VÀ NHẬP SỐ (`nghe_gia_tien` — 3 Câu: Câu 98 → Câu 100)
Người học nghe câu (giá **đã được đọc thành chữ**) và gõ giá bằng số. Đề bài thống nhất: `Nghe phát âm câu tiếng Đức và nhập số tiền bằng chữ số:` (không chứa ví dụ số để tránh lộ đáp án).
98. **Câu 98**: *Câu 98: Nghe phát âm câu tiếng Đức và nhập số tiền bằng chữ số:*
    * `audio_text`: *"Das macht zusammen vier Euro fünfundachtzig."*
    * `price_cents`: `485`
    * `accepted_answers`: `["4,85", "4.85", "4,85 €", "4.85 €", "4,85€", "4.85€", "4,85 Euro", "4.85 Euro"]`
    * Dịch nghĩa câu: *„Tổng cộng là bốn euro tám mươi lăm.“*
    * Giải thích: **`vier Euro fünfundachtzig` = 4,85 €**.
99. **Câu 99**: *Câu 99: Nghe phát âm câu tiếng Đức và nhập số tiền bằng chữ số:*
    * `audio_text`: *"Zwei Kilo Birnen kosten fünf Euro achtzig."*
    * `price_cents`: `580`
    * `accepted_answers`: `["5,80", "5.80", "5,8", "5.8", "5,80 €", "5.80 €", "5,80€", "5.80€", "5,80 Euro", "5.80 Euro"]`
    * Dịch nghĩa câu: *„Hai ký lê giá năm euro tám mươi.“*
    * Giải thích: **`fünf Euro achtzig` = 5,80 €** *(đúng với 2 × 2,90 €)*.
100. **Câu 100**: *Câu 100: Nghe phát âm câu tiếng Đức và nhập số tiền bằng chữ số:*
     * `audio_text`: *"Die Dose Cola kostet ein Euro neunundzwanzig."*
     * `price_cents`: `129`
     * `accepted_answers`: `["1,29", "1.29", "1,29 €", "1.29 €", "1,29€", "1.29€", "1,29 Euro", "1.29 Euro"]`
     * Dịch nghĩa câu: *„Lon cô-ca giá một euro hai mươi chín.“*
     * Giải thích: **`ein Euro neunundzwanzig` = 1,29 €**.

---

## PHẦN 4: HỆ THỐNG SINH ĐỀ NGẪU NHIÊN VÔ HẠN & DỮ LIỆU NGUỒN CHUẨN (`SINGLE SOURCE OF TRUTH`)

### 4.1. Mục tiêu & nguyên tắc
Màn hình bài tập của Bài 9 có khu vực **"Luyện Phản Xạ Ngẫu Nhiên Không Giới Hạn"** với nút **"Đổi bộ đề ngẫu nhiên mới"**. Bài 10 phải có **đúng cơ chế tương tự** (giữ nguyên cách hoạt động, cách tính EXP và bộ lọc 16 dạng bài như cơ chế hiện có của Bài 8 / Bài 9), nhưng **nội dung ngẫu nhiên được sinh bằng các Engine dưới đây**, theo các nguyên tắc:
1. **Một nguồn dữ liệu duy nhất**: mọi câu sinh ra đều lấy từ các bảng ở mục 4.2 (và bảng tính từ ở mục 5.3, bảng động từ ở mục 1.1 / 7.4). **Cấm** sinh dạng từ bằng quy tắc suy diễn (ví dụ tự cộng `-er`), vì sẽ tạo ra dạng sai như `teuerer`.
2. **Đề, đáp án, dịch nghĩa, giải thích và voice cùng sinh ra từ MỘT đối tượng** (`question object`) — không ghép riêng từng phần.
3. **Mỗi bộ đề ngẫu nhiên** gồm 100 câu theo **cùng phân bổ 16 dạng** của mục 3.1; **không có hai câu trùng nhau** trong cùng bộ (so khớp sau khi chuẩn hóa chữ hoa/thường, dấu câu, khoảng trắng); **không trùng với 100 câu cố định** của Bài 10; khi lỡ trùng phải bốc lại tối đa 20 lần, nếu vẫn trùng thì đổi dạng mẫu câu.
4. **Hạt giống (`seed`)** được lưu cùng bộ đề để tái hiện lỗi khi cần.
5. **Mọi Engine đều phải có test tự động** (xem Phần 5) và **không sinh ra câu gây mơ hồ** (câu có hai đáp án đúng mà `accepted_answers` không liệt kê hết).

### 4.2. DỮ LIỆU NGUỒN CHUẨN (Phụ lục A)
#### A1. `FOOD_POOL` — danh từ thực phẩm dùng cho Engine E1, E2, E7 (38 danh từ)
Cột `cnt`: `Y` = đếm được (dùng `viele` + số nhiều); `N` = không đếm được (dùng `viel` + số ít); `B` = dùng được cả hai nên **không dùng trong Engine `viel/viele`**. **Không đưa `Salami` và `Joghurt` vào pool** (xem mục chuẩn hóa).
| Mạo từ | Danh từ | Số nhiều | `cnt` | Nghĩa | Mạo từ | Danh từ | Số nhiều | `cnt` | Nghĩa |
| :-: | :--- | :--- | :-: | :--- | :-: | :--- | :--- | :-: | :--- |
| der | Käse | Käse | N | phô mai | die | Zwiebel | Zwiebeln | Y | hành tây |
| der | Kuchen | Kuchen | Y | bánh ngọt | die | Marmelade | Marmeladen | N | mứt |
| der | Apfel | Äpfel | Y | quả táo | die | Schokolade | Schokoladen | N | sô cô la |
| der | Fisch | Fische | B | cá | die | Milch | — | N | sữa |
| der | Salat | Salate | Y | xà lách, salad | das | Brot | Brote | B | bánh mì |
| der | Schinken | Schinken | N | giăm bông | das | Hähnchen | Hähnchen | Y | thịt gà |
| der | Pfeffer | — | N | tiêu | das | Ei | Eier | Y | quả trứng |
| der | Reis | — | N | gạo, cơm | das | Fleisch | — | N | thịt |
| der | Saft | Säfte | N | nước ép | das | Obst | — | N | hoa quả |
| der | Kaffee | Kaffees | N | cà phê | das | Gemüse | — | N | rau củ |
| die | Butter | — | N | bơ | das | Eis | — | N | kem |
| die | Kartoffel | Kartoffeln | Y | khoai tây | das | Salz | — | N | muối |
| die | Tomate | Tomaten | Y | cà chua | das | Müsli | Müslis | N | ngũ cốc |
| die | Möhre | Möhren | Y | cà rốt | das | Schnitzel | Schnitzel | Y | thịt tẩm bột chiên |
| die | Erdbeere | Erdbeeren | Y | dâu tây | das | Bier | Biere | N | bia |
| die | Banane | Bananen | Y | quả chuối | das | Wasser | — | N | nước |
| die | Orange | Orangen | Y | quả cam | die | Wurst | Würste | B | xúc xích |
| die | Birne | Birnen | Y | quả lê | die | Nudel | Nudeln | Y | sợi mì |
| die | Paprika | Paprikas | Y | ớt chuông | die | Ananas | Ananas | Y | quả dứa |

#### A2. `WELCH_ENDINGS` — bảng đuôi `welch-`
| Giống / số | Nominativ | Akkusativ |
| :--- | :--- | :--- |
| der (m, số ít) | welcher | welchen |
| die (f, số ít) | welche | welche |
| das (n, số ít) | welches | welches |
| die (số nhiều) | welche | welche |

#### A3. `PRICE_TABLE` — bảng giá nguồn (đơn vị: **cent**, tính theo đơn vị ở cột 3)
| Mặt hàng (dạng dùng trong câu) | Giống / số | Đơn vị tính giá | Giá (cent) |
| :--- | :--- | :--- | :-: |
| Äpfel | số nhiều | Kilo | 240 |
| Birnen | số nhiều | Kilo | 290 |
| Bananen | số nhiều | Kilo | 160 |
| Banane | số ít | Stück (1 quả) | 30 |
| Orangen | số nhiều | Kilo | 220 |
| Erdbeeren | số nhiều | Kilo | 780 *(1 Pfund = 390)* |
| Tomaten | số nhiều | Kilo | 250 |
| Möhren | số nhiều | Kilo | 120 |
| Kartoffeln | số nhiều | Kilo | 110 |
| Zwiebeln | số nhiều | Kilo | 140 |
| Paprika | số nhiều | Kilo | 360 |
| Hähnchen | das, số ít | Kilo | 690 |
| Fisch | der, số ít | Kilo | 1250 |
| Salat | der, số ít | Stück | 130 |
| Ananas | die, số ít | Stück | 230 |
| Käse | der, số ít | 100 Gramm | 299 |
| Schinken | der, số ít | 100 Gramm | 189 |
| Wurst | die, số ít | 100 Gramm | 149 |
| Milch | die, số ít | Liter | 110 |
| Cola | die, số ít | Dose | 129 |
| Wasser | das, số ít | Flasche | 60 |
| Brot | das, số ít | Stück | 280 |
| Kuchen | der, số ít | Stück | 360 |
| Müsli | das, số ít | Packung | 399 |

> 🔒 **Ràng buộc bảng giá**: mọi câu "A rẻ hơn / đắt hơn B" sinh ra phải **đúng theo bảng** và chỉ so sánh hai mặt hàng **cùng đơn vị tính giá**; chênh lệch tối thiểu **10 cent** để không có câu gây tranh cãi.

#### A4. `QUANTITY_PHRASES` — cụm số lượng + vật (Akkusativ) dùng cho Engine E4
| Mặt hàng | Đơn vị | n = 1 | n = 2 | n = 3 |
| :--- | :--- | :--- | :--- | :--- |
| Tomaten / Möhren / Äpfel / Birnen / Kartoffeln | Kilo | ein Kilo X | zwei Kilo X | drei Kilo X |
| Milch | Liter | ein Liter Milch | zwei Liter Milch | drei Liter Milch |
| Ananas | Stück | eine Ananas | zwei Ananas | drei Ananas |
| Salat | Stück | einen Salat | zwei Salate | drei Salate |
| Brot | Stück | ein Brot | zwei Brote | drei Brote |
| Kuchen | Stück | ein Stück Kuchen | zwei Stück Kuchen | drei Stück Kuchen |
| Müsli | Packung | eine Packung Müsli | zwei Packungen Müsli | drei Packungen Müsli |
| Wasser | Flasche | eine Flasche Wasser | zwei Flaschen Wasser | drei Flaschen Wasser |
| Cola | Dose | eine Dose Cola | zwei Dosen Cola | drei Dosen Cola |

> Quy tắc đã đặc tả ở mục 6.3: đơn vị đo giữ nguyên số ít (`zwei Kilo`, `zwei Liter`, `zwei Stück`); đơn vị đóng gói thêm `-n/-en` (`zwei Flaschen`, `zwei Dosen`, `zwei Packungen`).

#### A5. `NUMBER_WORDS` — bảng số cho hàm đọc giá
`ONES = [null, ein, zwei, drei, vier, fünf, sechs, sieben, acht, neun, zehn, elf, zwölf, dreizehn, vierzehn, fünfzehn, sechzehn, siebzehn, achtzehn, neunzehn]` (chỉ số 0–19; phần tử `1` là **`ein`**, dùng được cho cả `ein Euro` lẫn `einundzwanzig`).
`TENS = {20: zwanzig, 30: dreißig, 40: vierzig, 50: fünfzig, 60: sechzig, 70: siebzig, 80: achtzig, 90: neunzig}`.

### 4.3. CÁC ENGINE SINH ĐỀ
| Mã | Tên | Sinh ra dạng bài | Đặc tả & ràng buộc (BẮT BUỘC) |
| :-: | :--- | :--- | :--- |
| **E1** | **Welch- Generator** | `trac_nghiem`, `dien_khuyet`, `dien_tao_cau`, `nghe_dien`, `tim_loi_sai` | Chọn 1 danh từ từ **A1** + 1 vai trò. **Vai trò Nominativ** → khung câu `Welch- N ist/schmeckt + {frisch, billig, teuer, lecker, gesund}?` (ví dụ `Welcher Fisch ist heute frisch?`). **Vai trò Akkusativ** → khung `Welch- N + {möchtest du, kaufst du, nimmst du, brauchen wir, empfehlen Sie, probierst du}?`. Đuôi lấy từ **A2** theo (giống, số, cách). Danh từ **không có số nhiều** (`Obst, Gemüse, Reis, Milch…`) chỉ được dùng ở số ít. Động từ chia **đúng ngôi** từ bảng 1.1. 3 phương án sai của trắc nghiệm = 3 dạng đuôi còn lại. Bản dịch lấy từ mẫu dịch cố định theo khung câu: `Welch- N ...?` → *"… N nào …?"*. Câu trả lời mẫu (nếu có) dùng mạo từ xác định tương ứng. |
| **E2** | **Steigerung Generator** | `trac_nghiem`, `dien_khuyet`, `dien_tao_cau`, `noi_o`, `viet_lai_so_sanh`, `sap_xep_cau`, `dich_cau_vd/dv` | **E2a (so sánh giá)**: chọn 2 mặt hàng cùng đơn vị từ **A3**; sinh `X ist/sind billiger/teurer als Y` **đúng theo giá**. Chủ ngữ số ít → `ist`, số nhiều → `sind`; mạo từ lấy từ **A1**. **E2b (tính từ)**: dạng so sánh **chỉ lấy từ bảng 25 tính từ (mục 5.3)**. **E2c (sở thích / số lượng)**: khung `S + esse/trinke/kaufe + {lieber, mehr, am liebsten, am meisten} + N1 (+ als N2)` — chỉ dùng cặp `lieber/mehr + als` khi có N2; đối với `am liebsten / am meisten` có thể đảo ngữ. Chủ ngữ xoay đủ 9 ngôi, động từ chia đúng. **Không** sinh câu khẳng định sự thật mơ hồ (ví dụ "cá ngon hơn thịt") ở dạng `dung_sai`; chỉ dùng ở dạng dịch / điền từ. |
| **E3** | **Price Reader** | `nghe_gia_tien`, `nghe_dien`, mọi nút `🔊` có giá | Hàm **`price_to_german(cents)`** theo thuật toán 4.4. **Bắt buộc** dùng cho mọi nơi hiển thị / đọc giá tiền. Giá sinh ngẫu nhiên: `cents` từ 10 đến 9999 và **`cents % 100 ≠ 1`**. |
| **E4** | **Einkauf Generator** | `hoi_thoai_sap_xep`, `dich_cau`, `dung_sai` (đọc hiểu) | Chọn 2–3 mặt hàng từ **A3 + A4**, số lượng 1–3 mỗi loại; **tổng tiền = Σ (đơn giá × số lượng)** bằng số nguyên cent (với đơn vị `100 Gramm` mỗi lần lấy 100/200/300 g). Khách đưa tờ tiền nhỏ nhất trong `{5, 10, 20, 50}` € đủ trả; **tiền thối = đưa − tổng ≥ 0**. Sinh hội thoại theo trình tự **chào → gọi → hỏi thêm → hỏi giá → báo tổng → trả tiền → thối** (các lượt lời lấy từ mục 6.1/6.5). Bản dịch từng lượt lời lấy từ ngân hàng câu cố định, giá tiền được dịch bằng số. |
| **E5** | **Verb Conjugation Generator** | `dien_khuyet`, `noi_o`, `trac_nghiem`, `tim_loi_sai` | Chọn động từ và ngôi; dạng chia **lấy từ bảng 1.1 và 7.1 / 7.2 / 7.3** (không tự chia). Loại trừ các ngôi vô nghĩa: `kosten` chỉ ngôi `es/sie (số nhiều)`; `möchten/mögen/dürfen` không có Perfekt. **Ôn Perfekt**: chỉ dùng 14 động từ của bảng 7.4, kèm trợ động từ `haben`. |
| **E6** | **Satzstellung Builder** | `sap_xep_cau`, `tim_loi_sai` (lỗi vị trí) | Khung: `[Superlativ ①] [V ②] [S ③] [phần còn lại]` và biến thể không đảo ngữ. **`accepted_answers` phải gồm cả hai trật tự hợp lệ.** Token được xáo trộn sao cho **khác** trật tự đúng. Với `Welch-`: `[Welch- N ①] [V ②] [S ③]`. |
| **E7** | **Gender Classifier** | `phan_loai_giong`, `trac_nghiem`, `noi_o` | Chọn 4 danh từ từ **A1** sao cho có **ít nhất 2 giống khác nhau**; nhãn `reason_vi` lấy từ mẹo đuôi (mục 1.1) hoặc ghi *"học thuộc"*. **Không** dùng `Salami`, `Joghurt`. |
| **E8** | **Dialogue Orderer** | `hoi_thoai_sap_xep` | Lấy hội thoại từ E4 hoặc 4 hội thoại ở mục 6.5; xáo trộn các lượt lời; kiểm tra thứ tự xáo trộn **khác** thứ tự gốc. |
| **E9** | **Arena Extension** | Đấu trường | **Thêm** (không thay thế) một nhóm 15 câu hỏi hỗn hợp của Bài 10 (5 `Welch-`, 4 so sánh, 3 mua sắm, 3 từ vựng giống) vào kho Đấu trường, giữ nguyên toàn bộ câu cũ. |

### 4.4. THUẬT TOÁN `price_to_german(cents)` & BỘ TEST BẮT BUỘC
```python
ONES = ["null","ein","zwei","drei","vier","fünf","sechs","sieben","acht","neun","zehn",
        "elf","zwölf","dreizehn","vierzehn","fünfzehn","sechzehn","siebzehn","achtzehn","neunzehn"]
TENS = {20:"zwanzig",30:"dreißig",40:"vierzig",50:"fünfzig",60:"sechzig",70:"siebzig",80:"achtzig",90:"neunzig"}

def num_words(n):                       # 1 <= n <= 99
    if n < 20:
        return ONES[n]
    t, u = (n // 10) * 10, n % 10
    return TENS[t] if u == 0 else ONES[u] + "und" + TENS[t]

def price_to_german(cents):             # cents: số nguyên, 0 < cents < 10000, cents % 100 != 1
    euros, c = divmod(cents, 100)
    if euros == 0:
        return f"{num_words(c)} Cent"
    if c == 0:
        return f"{num_words(euros)} Euro"
    return f"{num_words(euros)} Euro {num_words(c)}"
```
| `cents` | Kết quả bắt buộc | `cents` | Kết quả bắt buộc |
| :-: | :--- | :-: | :--- |
| 50 | fünfzig Cent | 1250 | zwölf Euro fünfzig |
| 99 | neunundneunzig Cent | 1999 | neunzehn Euro neunundneunzig |
| 100 | ein Euro | 1100 | elf Euro |
| 120 | ein Euro zwanzig | 1600 | sechzehn Euro |
| 129 | ein Euro neunundzwanzig | 1700 | siebzehn Euro |
| 200 | zwei Euro | 2100 | einundzwanzig Euro |
| 299 | zwei Euro neunundneunzig | 2130 | einundzwanzig Euro dreißig |
| 375 | drei Euro fünfundsiebzig | 3000 | dreißig Euro |
| 485 | vier Euro fünfundachtzig | 640 | sechs Euro vierzig |
| 580 | fünf Euro achtzig | 850 | acht Euro fünfzig |

**Hàm chuẩn hóa đáp án giá (`parse_price_input`)**: bỏ khoảng trắng, bỏ `€` và chữ `Euro` (không phân biệt hoa/thường), đổi `.` thành `,`, tách phần euro và cent, **bù thành 2 chữ số cent** (`4,5` → `4,50`), rồi quy ra số nguyên cent. Đáp án `4,85`, `4.85`, `4,85 €`, `4,85€`, `4,85 Euro` phải cùng cho `485`.

---

## PHẦN 5: KIỂM THỬ TOÀN DIỆN & QA ZERO-BUG (`verify_lesson10_qa.py`)

> **Yêu cầu bắt buộc**: Sau khi code xong, Antigravity IDE phải **viết và chạy** `verify_lesson10_qa.py` (hoặc `pytest` tương đương), **sửa mọi lỗi** cho đến khi toàn bộ test đạt, rồi **dán báo cáo kết quả** theo mẫu mục 5.5. Không được báo "xong" khi chưa chạy.

### 5.1. Bảng đối chiếu: lỗi cũ → kiểm tra tự động
| # | Lỗi đã từng gặp | Kiểm tra tự động (phải đạt) |
| :-: | :--- | :--- |
| 1 | Dịch sai nghĩa | Với 100% câu: `translation_vi` không rỗng; bản dịch **chứa các từ khóa nghĩa** của đáp án (từ điển `KEYWORDS_VI`); câu so sánh hơn phải chứa *"hơn"*, so sánh nhất phải chứa *"nhất"*; câu Perfekt phải chứa *"đã"*. Rà soát thủ công thêm 30 câu ngẫu nhiên. |
| 2 | Thiếu phần dịch | Quét toàn bộ `lexikon`, `verbs`, đoạn văn, bảng lý thuyết, 100 câu: không còn trường `*_vi` rỗng hoặc `None`. |
| 3 | Dịch / đáp án không liên quan đề | Mỗi câu: ghép `display_sentence` + đáp án → so sánh với `audio_text`/câu chuẩn; `explanation` **chứa chuỗi đáp án đúng** (chuẩn hóa). |
| 4 | Voice thiếu / sai | Mọi phần tử có `🔊` phải có `speak_text` không rỗng; `speak_text` **không chứa** ký tự trong `[_→€\[\]/]` và **không chứa** ký tự tiếng Việt có dấu đặc trưng (`ă â đ ê ô ơ ư`); mọi giá tiền đã qua `price_to_german`. Với câu điền khuyết: `speak_text` = câu đã điền đầy đủ. |
| 5 | Ví dụ không khớp thẻ từ | Mỗi thẻ từ vựng: `example_de` chứa **lemma hoặc dạng số nhiều** của thẻ (không phân biệt hoa/thường); thẻ động từ: ví dụ chứa một dạng chia của động từ đó. |
| 6 | Giải thích sai đáp án | Tự động: giải thích chứa đáp án; kiểm tra chéo quy tắc: đuôi `welch-` đúng theo A2; mọi Komparativ / Superlativ đúng theo bảng 5.3; mọi Partizip II đúng theo bảng 7.4 và Bài 9. |
| 7 | Câu hỏi trùng nhau | `len(set(normalize(q.prompt + q.display))) == 100`; không có hai câu cùng `accepted_answers` **và** cùng nội dung đề. So sánh thêm với toàn bộ câu của **Bài 8 và Bài 9** (không được trùng). |
| 8 | Giá tiền sai | Mọi hội thoại / câu có giỏ hàng: `sum(price × qty) == total`; `price_to_german` pass 20 test ở 4.4. |
| 9 | Làm hỏng bài cũ | `Zero-Regression Check` mục 5.2. |
| 10 | Số lượng sai | Đúng 100 câu; đúng phân bổ 16 dạng như mục 3.1 (`10,12,8,8,8,8,8,6,6,5,4,4,4,3,3,3`); đúng 50 thẻ từ vựng (trừ thẻ trùng bài cũ) và 20 thẻ động từ (trừ thẻ trùng). |

### 5.2. Kiểm tra không phá bài cũ (`Zero-Regression Check`)
1. **Trước khi code**: tạo nhánh `lesson-10`; chạy `git stash`/`git status` để chắc chắn working tree sạch; lưu **băm SHA-256** của toàn bộ file bài cũ (`lessons/a1/seed_a1_b*.py`, `verbs_db.js`, `lexikon_db.js`, `arena_generator.py`) vào `baseline_hashes.json`.
2. **Sau khi code**: so sánh băm. Với `lessons/a1/seed_a1_b1*…b9.py`: **phải giữ nguyên 100%**. Với `verbs_db.js`, `lexikon_db.js`, `arena_generator.py`: chỉ được **thêm** dòng (kiểm tra bằng `git diff --numstat`: số dòng xóa = 0).
3. **Kiểm tra giao diện cũ**: mở **Bài 8 và Bài 9**, chạy thử mỗi dạng bài (đặc biệt `chon_haben_sein`, `viet_lai_perfekt`, `sap_xep_cau`, `tim_loi_sai`, `dung_sai`) → kết quả y như trước; **không có lỗi trong Console**.
4. **Tiến độ người dùng**: tiến độ, EXP, chuỗi ngày, huy hiệu của người dùng ở các bài cũ **không bị thay đổi**.

### 5.3. Danh sách test tự động bắt buộc trong `verify_lesson10_qa.py`
| Nhóm | Test | Mô tả |
| :--- | :--- | :--- |
| **Dữ liệu** | `test_lexikon_counts` | 50 thẻ mới (trừ trùng); mỗi thẻ có `article ∈ {der,die,das}`, `plural` (hoặc `nur Singular/Plural`), `meaning_vi`, `example_de`, `example_vi`. |
| | `test_lexikon_example_matches` | `example_de` chứa lemma hoặc số nhiều của chính thẻ. |
| | `test_lexikon_gender_whitelist` | Giống của 50 danh từ khớp bảng chuẩn (đặc biệt: `der Reis`, `der Käse`, `die Wurst`, `das Gemüse`, `das Hähnchen`, `die Möhre`). |
| | `test_verbs_present_forms` | 20 động từ: bảng chia 6 ngôi khớp bảng 1.1; ví dụ chứa dạng chia của động từ. |
| | `test_adjective_table` | 25 tính từ: Komparativ / Superlativ **khớp** bảng 5.3 (chép từ nguồn, không tự tính). Quy tắc kiểm tra chéo: Superlativ kết thúc `-sten`/`-esten`; Superlativ `-esten` khi Positiv kết thúc `t, d, s, ß, z, sch`. |
| **Engine** | `test_price_to_german` | 20 test ở 4.4 + 200 giá ngẫu nhiên: kết quả không rỗng, đúng định dạng, không chứa chữ số. |
| | `test_parse_price_input` | `4,85 / 4.85 / 4,85 € / 4,85€ / 4,85 Euro → 485`; `4,5 → 450`. |
| | `test_welch_engine` | Sinh 500 câu: đuôi `welch-` luôn khớp A2; không có số nhiều của danh từ `nur Singular`; mọi câu có `translation_vi`. |
| | `test_steigerung_engine` | Sinh 500 câu E2a: phát biểu **đúng theo PRICE_TABLE**; chủ ngữ `ist/sind` khớp số; Komparativ lấy từ bảng. |
| | `test_einkauf_engine` | Sinh 300 giỏ hàng: tổng và tiền thối đúng; cụm số lượng theo A4; dịch giá bằng số. |
| | `test_no_duplicates_in_random_set` | 200 bộ đề ngẫu nhiên × 100 câu: không trùng trong bộ, không trùng 100 câu cố định, không trùng Bài 8/9. |
| **Bài tập cố định** | `test_100_questions` | Đúng 100 câu; phân bổ 16 dạng đúng; mã câu 1–100 liên tục. |
| | `test_unique_questions` | Không trùng sau chuẩn hóa. |
| | `test_every_question_has_translation_and_explanation` | Không rỗng; giải thích chứa đáp án. |
| | `test_answers_in_accepted_list` | Đáp án hiển thị nằm trong `accepted_answers`; trắc nghiệm có **đúng 1** đáp án đúng; nối ô có đúng 4 cặp, mỗi trái ↔ 1 phải. |
| | `test_tts_clean` | Mọi `speak_text` sạch (xem 5.1 mục 4). |
| | `test_sentences_german_checks` | Kiểm tra cơ học: câu tiếng Đức bắt đầu bằng chữ hoa; có dấu câu cuối; không có ký tự lạ; `welch-` ở đầu câu hỏi `Welch-` được đối chiếu với A2 theo giống của danh từ đi sau. |
| **Quy tắc ngữ pháp cứng** | `test_komparativ_in_questions` | Mọi dạng so sánh xuất hiện trong 100 câu đều có trong bảng 5.3. |
| | `test_partizip_review` | Mọi Partizip II (ôn Bài 9) khớp bảng 7.4 hoặc bảng nguồn Bài 9. |
| | `test_verb_second_position` | Với câu `sap_xep_cau` và `tim_loi_sai` loại vị trí động từ: `accepted_answers` có động từ chia ở vị trí 2. |
| **Giao diện** | `test_ui_16_types_visible` | Bộ lọc hiển thị đủ 16 dạng với số lượng đúng; nút "Tất cả (100)". |
| | `test_ui_all_audio_buttons` | Click toàn bộ nút `🔊` không lỗi; âm lượng bật. |
| **Hồi quy** | `test_zero_regression` | Theo mục 5.2. |

### 5.4. Danh sách kiểm tra thủ công cuối cùng (người thật rà soát)
1. Mở Bài 10, đọc **toàn bộ lý thuyết**: không còn ô trống, không còn bản dịch thiếu, không bảng vỡ cột (chú ý các ô có ký tự `|`).
2. Đối chiếu **giống `der Reis`**, `die Salami` (kèm ghi chú), `das Buch` (không phải `das Bund`) với mục chuẩn hóa.
3. Bấm `🔊` ở **mọi** bảng: từ vựng, mẫu câu, hội thoại, đoạn văn, sơ đồ. Nghe thử các câu có giá tiền: phải đọc *"drei Euro fünfundsiebzig"*, **không** đọc "Komma" hay "Euro-Zeichen".
4. Làm thử **một câu mỗi dạng** (16 dạng) ở chế độ đúng và chế độ sai: kiểm tra phần *Dịch nghĩa* và *Giải thích* hiển thị đúng và khớp đáp án.
5. Làm đủ **100/100** để kiểm tra thanh tiến độ, EXP, huy hiệu, lưu tiến độ sau khi tải lại trang.
6. Bấm **"Đổi bộ đề ngẫu nhiên mới"** ít nhất 10 lần: không câu nào lặp trong cùng bộ; mọi giá tiền / tổng tiền đều đúng phép tính; không có câu vô nghĩa.
7. Chuyển sang **Bài 8, Bài 9**: các bài vẫn hoạt động; không đổi nội dung.
8. Thử trên **điện thoại** (màn hình hẹp): bảng có thanh cuộn ngang, nút `🔊` bấm được, sơ đồ SVG co giãn đúng.
9. Thử **Dark / Light mode** cho 6 sơ đồ.

### 5.5. Mẫu báo cáo cuối cùng (bắt buộc dán vào phản hồi sau khi làm xong)
```
BÁO CÁO QA BÀI 10
- Số câu hỏi: 100 / 100 (phân bổ 16 dạng: 10,12,8,8,8,8,8,6,6,5,4,4,4,3,3,3)  [ĐẠT/KHÔNG ĐẠT]
- Câu trùng nhau: 0                                                          [ĐẠT/KHÔNG ĐẠT]
- Thẻ từ vựng thêm mới / bỏ qua vì trùng: X / Y
- Thẻ động từ thêm mới / bỏ qua vì trùng: X / Y
- Test price_to_german: 20/20 + 200 ngẫu nhiên                               [ĐẠT/KHÔNG ĐẠT]
- Test bảng so sánh (25 tính từ): 25/25                                       [ĐẠT/KHÔNG ĐẠT]
- Test 500 câu Welch- / 500 câu Steigerung / 300 giỏ hàng                    [ĐẠT/KHÔNG ĐẠT]
- Test TTS sạch (100% nút 🔊)                                                 [ĐẠT/KHÔNG ĐẠT]
- Zero-Regression (băm file Bài 1–9, git diff không xóa dòng nào)             [ĐẠT/KHÔNG ĐẠT]
- Giao diện Bài 8, Bài 9 vẫn chạy đúng                                       [ĐẠT/KHÔNG ĐẠT]
- Các lỗi đã phát hiện và đã sửa: (liệt kê)
- Các điểm cần người dùng quyết định: (liệt kê, nếu có)
```

### 5.6. Lưu ý giao diện đã quan sát được ở Bài 9 (khuyến nghị xử lý, KHÔNG làm hỏng bài cũ)
* Nhãn tab **"Phần 2: Bài tập (Đủ 7 Dạng)"** đang **viết cố định số 7**, trong khi Bài 9 có **14 dạng** (và Bài 10 có **16 dạng**). Khuyến nghị: tính số dạng **động** từ dữ liệu của từng bài (`len(set(question.type))`) cho **Bài 9 và Bài 10**; các bài cũ hơn **giữ nguyên hành vi hiện có** nếu việc đổi nhãn có nguy cơ gây lỗi, và chỉ báo lại cho người dùng để quyết định.
* Thanh bộ lọc dạng bài phải **tự mở rộng đúng 16 chip** của Bài 10 (kèm số lượng trong ngoặc) và không bị tràn trên điện thoại (cho phép xuống dòng).
* Tên hiển thị của dạng bài mới theo bảng 3.1; không dùng mã kỹ thuật (`phan_loai_giong`) làm nhãn.

---

*Hết đặc tả Bài 10. Nhắc lại ba nguyên tắc cuối cùng cho Antigravity IDE: **(1)** không động chạm bài cũ; **(2)** mọi dữ liệu - đề - đáp án - dịch - giải thích - voice phải sinh từ một nguồn; **(3)** chạy kiểm thử và dán báo cáo trước khi báo hoàn thành.*
