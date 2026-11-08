# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 8 (A1) "STADT - HỎI ĐƯỜNG / CHỈ ĐƯỜNG - ĐỘNG TỪ KHUYẾT THIẾU" — TÍCH HỢP SƠ ĐỒ & BẢN ĐỒ TƯƠNG TÁC SVG TRONG LÝ THUYẾT & 100 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa làm hỏng, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**, **Bài 4**, **Bài 5**, **Bài 6**, **Bài 7**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này là **tạo mới hoàn toàn Bài 8 (`lessons/a1/seed_a1_b8.py`)** ở vị trí `lesson_order = 9` của cấp độ **A1** với **hệ thống hình ảnh sơ đồ chỉ đường & bản đồ thành phố trực quan (SVG)** trong cả phần lý thuyết và phần bài tập, kho **100 câu hỏi bài tập độc nhất**, cộng dồn động từ và từ vựng của Bài 8 vào 2 chuyên mục tra cứu, mở rộng trần kiến thức Đấu trường tới Bài 8, và chạy kịch bản kiểm thử toàn diện.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu.
>
> ---
>
> ### 🗺️ 2. YÊU CẦU ĐẶC BIỆT CỦA BÀI 8: BẮT BUỘC CÓ HÌNH ẢNH MINH HỌA SƠ ĐỒ & BẢN ĐỒ TRONG CẢ LÝ THUYẾT LẪN BÀI TẬP (`VISUAL SVG DIAGRAMS & INTERACTIVE CITY MAPS`)
> Vì Bài 8 dạy về **Hỏi đường, Chỉ đường và Định hướng trong thành phố**, nếu chỉ có chữ thuần túy người học sẽ không thể hình dung được sự khác biệt giữa các giới từ không gian và lộ trình rẽ. Do đó, Antigravity IDE **BẮT BUỘC** phải xây dựng module đồ họa **`static/js/city_map_svg.js`** (kết hợp SVG nội tuyến sắc nét, tương thích Dark/Light mode) để hiển thị:
> 1. **Trong phần Lý thuyết**:
>    * **Bộ 4 Sơ đồ Không gian Trực quan (`Spatial Preposition Diagrams`)**: Minh họa bằng hình vẽ mũi tên chuyển động cho 4 cấu trúc dễ nhầm nhất:
>      1. `an + Dativ + vorbei` *(đi ngang qua bên cạnh tòa nhà `Universität / Kirche / Bank`)*,
>      2. `durch + Akkusativ` *(đi xuyên qua lòng cổng `das Tor / der Park`)*,
>      3. `über + Akkusativ` *(đi vượt qua trên mặt `die Brücke / der Platz / die Kreuzung`)*,
>      4. `Akkusativ + entlang` *(đi dọc theo chiều dài `die Straße / der Fluss`)*.
>    * **Bộ 12 Thẻ Hình Biểu Tượng Chỉ Đường (`Visual Direction Flashcards a -> l`)**: Tái hiện đầy đủ và sắc nét 9 hình vẽ trên bảng giảng (`a` đến `i`: *đi thẳng, đi ngang qua nhà thờ, đi tới đèn giao thông, đi tới ngã tư, rẽ trái ở ngã rẽ thứ 2, đi băng qua quảng trường, rẽ trái ở đây, rẽ phải ở đây, đi dọc theo con đường*) và mở rộng thêm 3 hình (*rẽ phải ở ngã rẽ thứ 2, đi xuyên qua cổng thành, đi qua cầu*). Mỗi thẻ có hình vẽ SVG rõ ràng + câu lệnh tiếng Đức + nút `🔊` phát âm + dịch nghĩa tiếng Việt.
>    * **Bản đồ Lưới Đường Phố Tương Tác Đa Lộ Trình (`Interactive Multi-Route City Grid Map`)**: Vẽ bản đồ lưới đường phố gồm vị trí xuất phát (`📍 Start: Sie sind hier`), các ngã tư (`1. Kreuzung`, `2. Kreuzung`), các tòa nhà (`🏦 Bank`, `⛪ Kirche`, `🏫 Universität`, `📮 Post`, `🚦 Ampel`, `🎬 Kino`, `🚉 Bahnhof`), cho phép người học bấm nút bật/tắt đường đi màu xanh dương (**Lộ trình 1**) và màu xanh lá (**Lộ trình 2**) kèm thuyết minh từng bước bằng giọng đọc `de-DE`.
> 2. **Trong phần Bài tập (100 Câu hỏi & Bộ Random Đổi Đề)**:
>    * Hỗ trợ trường dữ liệu `visual_svg` / `map_scenario` trong các câu hỏi bài tập để hiển thị **biểu tượng mũi tên chỉ đường** hoặc **bản đồ lộ trình đường phố trực quan ngay trên khung câu hỏi** (áp dụng cho cả Trắc nghiệm nhìn bản đồ, Điền khuyết lộ trình trên bản đồ, Nối hình chỉ đường, Điền từ tạo câu chỉ đường và Dịch câu theo bản đồ).
>    * Khi người dùng bấm **`🔄 Đổi đề khác`**, **Bộ Sinh Bản Đồ Động (`Dynamic Visual Map Generator`)** tự động vẽ lại lộ trình mới trên bản đồ SVG (đổi điểm xuất phát, đổi tòa nhà đi ngang qua, đổi ngã rẽ thứ 1/2/3 trái/phải, đổi điểm đích) và cập nhật đồng bộ 100% Đề bài – Hình bản đồ – Đáp án – Dịch nghĩa – Giải thích!
>
> ---
>
> ### 🔍 3. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI & CHỐNG TRÙNG LẶP CÂU HỎI (`ZERO-BUG & ZERO-DUPLICATE QA PROTOCOL`)
> 1. **Chống trùng lặp câu hỏi 100% (`Strict Deduplication Check`)**: Toàn bộ **100 câu hỏi** trong Bài 8 (`seed_a1_b8.py`) phải hoàn toàn độc nhất (`len(set(questions)) == 100`), sáng tạo mở rộng đa ngữ cảnh, đa chủ ngữ (`ich, du, er, sie, es, wir, ihr, sie, Sie`, du khách, cảnh sát, tài xế, sinh viên...), tuyệt đối không bê nguyên xi hay lặp lại câu hỏi.
> 2. **Cấm dịch sai nghĩa hoặc thiếu phần dịch nghĩa**: 100% từ vựng, ví dụ, bảng lý thuyết, chú thích bản đồ và 100% câu hỏi bài tập phải có bản dịch tiếng Việt chuẩn xác.
> 3. **Cấm lệch Đề bài – Hình minh họa – Đáp án – Giải thích (`Strict Atomic Visual-Text Alignment`)**: Nếu hình SVG vẽ mũi tên rẽ trái ở ngã rẽ thứ hai (`die zweite Straße links`) hoặc đi ngang qua ngân hàng (`an der Bank vorbei`), thì đề bài, đáp án đúng và lời giải thích phải khớp tuyệt đối với hình vẽ đó.
> 4. **Cấm thiếu Voice hoặc Voice đọc sai ngôn ngữ (`100% Clean German TTS Voice`)**: Mọi nút `🔊` chỉ truyền chuỗi tiếng Đức sạch (`de-DE`) vào `speakGerman()`, tuyệt đối không đọc lẫn tiếng Việt hay ký hiệu `___`, `->`.
> 5. **Cấm đưa ví dụ không khớp với thẻ từ vựng**: Thẻ từ vựng dạy từ nào (ví dụ `das Stadttor`, `die Museumsinsel`, `das Bundeskanzleramt`, `die Kreuzung`) thì câu ví dụ `example_de` và `example_vi` bắt buộc chứa đúng từ đó.

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 $\rightarrow$ Bài 7 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 8**:

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung/cập nhật **12 động từ trọng tâm của Bài 8** (nhấn mạnh động từ khuyết thiếu `wollen` đặt cạnh `möchten, können, müssen` và nhóm động từ di chuyển/tham quan thành phố), kèm phát âm `de-DE` và ví dụ chuẩn:
1. **`wollen`** (*muốn [ý định mạnh mẽ, kế hoạch chắc chắn]* — **Modalverb**, đổi `o -> i` ở số ít, ngôi `ich` và `er/sie/es` không có đuôi):
   * Chia theo ngôi: `ich will`, `du willst`, `er/sie/es will`, `wir wollen`, `ihr wollt`, `sie/Sie wollen`.
   * Ví dụ: *„In Deutschland will ich an der Humboldt-Universität studieren.“ (Ở Đức tôi muốn học đại học tại trường Đại học Humboldt.)*
2. **`bummeln`** (*đi dạo phố, tản bộ ngắm cảnh/mua sắm* — Động từ đuôi `-eln`, ngôi `ich` lược `e` thành `ich bummle` hoặc `ich bummele`):
   * Chia theo ngôi: `ich bummle (bummele)`, `du bummelst`, `er/sie/es bummelt`, `wir bummeln`, `ihr bummelt`, `sie/Sie bummeln`.
   * Ví dụ: *„Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.“ (Tiếp sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.)*
3. **`vorbeigehen`** (*đi ngang qua [đi bộ]* — **Động từ tách** `vorbei-` + `gehen`, đi với cụm `an + Dativ + vorbei`):
   * Chia theo ngôi: `ich gehe ... vorbei`, `du gehst ... vorbei`, `er/sie/es geht ... vorbei`, `wir gehen ... vorbei`, `ihr geht ... vorbei`, `sie/Sie gehen ... vorbei`.
   * Ví dụ: *„Gehen Sie zuerst an der Bank und an der Kirche vorbei!“ (Đầu tiên Ngài hãy đi ngang qua ngân hàng và nhà thờ!)*
4. **`vorbeifahren`** (*lái xe / đi xe ngang qua* — **Động từ tách** `vorbei-` + `fahren`, biến âm `a -> ä` ở `du, er/sie/es`, đi với `an + Dativ + vorbei`):
   * Chia theo ngôi: `ich fahre ... vorbei`, `du fährst ... vorbei`, `er/sie/es fährt ... vorbei`, `wir fahren ... vorbei`, `ihr fahrt ... vorbei`, `sie/Sie fahren ... vorbei`.
   * Ví dụ: *„Der Bus fährt am Bundeskanzleramt vorbei.“ (Chiếc xe buýt chạy ngang qua Phủ Thủ tướng.)*
5. **`laufen`** (*chạy bộ / đi bộ* — **Biến âm `au -> äu`** ở ngôi `du läufst, er/sie/es läuft`):
   * Chia theo ngôi: `ich laufe`, `du läufst`, `er/sie/es läuft`, `wir laufen`, `ihr lauft`, `sie/Sie laufen`.
   * Ví dụ: *„Paula und Alex laufen über die Schlossbrücke.“ (Paula và Alex đi bộ qua cầu Schlossbrücke.)*
6. **`sehen`** (*nhìn thấy, xem* — **Biến âm `e -> ie`** ở ngôi `du siehst, er/sie/es sieht`):
   * Chia theo ngôi: `ich sehe`, `du siehst`, `er/sie/es sieht`, `wir sehen`, `ihr seht`, `sie/Sie sehen`.
   * Ví dụ: *„Rechts neben der Ampel sehen Sie die Post.“ (Ở bên phải cạnh đèn giao thông, Ngài sẽ nhìn thấy bưu điện.)*
7. **`abbiegen`** (*rẽ, quẹo [trái/phải]* — **Động từ tách** `ab-` + `biegen`):
   * Chia theo ngôi: `ich biege ... ab`, `du biegst ... ab`, `er/sie/es biegt ... ab`, `wir biegen ... ab`, `ihr biegt ... ab`, `sie/Sie biegen ... ab`.
   * Ví dụ: *„An der zweiten Kreuzung müssen Sie links abbiegen.“ (Ở ngã tư thứ hai Ngài phải rẽ trái.)*
8. **`überqueren`** (*băng qua [đường, cầu, quảng trường]* — Tiền tố `über-` không tách, đi với `Akkusativ`):
   * Chia theo ngôi: `ich überquere`, `du überquerst`, `er/sie/es überquert`, `wir überqueren`, `ihr überquert`, `sie/Sie überqueren`.
   * Ví dụ: *„Bitte überqueren Sie die Straße an der Ampel!“ (Xin Ngài hãy băng qua đường tại chỗ đèn giao thông!)*
9. **`besichtigen`** (*tham quan, vãn cảnh [danh lam thắng cảnh, bảo tàng]* — Tiền tố `be-` không tách, đi với `Akkusativ`):
   * Chia theo ngôi: `ich besichtige`, `du besichtigst`, `er/sie/es besichtigt`, `wir besichtigen`, `ihr besichtigt`, `sie/Sie besichtigen`.
   * Ví dụ: *„Die Touristen wollen heute den Reichstag und das Schloss Bellevue besichtigen.“ (Các du khách hôm nay muốn tham quan tòa nhà Quốc hội và cung điện Bellevue.)*
10. **`studieren`** (*học đại học, nghiên cứu* — Động từ đuôi `-ieren`):
    * Chia theo ngôi: `ich studiere`, `du studierst`, `er/sie/es studiert`, `wir studieren`, `ihr studiert`, `sie/Sie studieren`.
    * Ví dụ: *„Mein Cousin will nächstes Jahr in Berlin Architektur studieren.“ (Anh họ tôi muốn năm sau học ngành Kiến trúc ở Berlin.)*
11. **`hören`** (*nghe* — Động từ quy tắc):
    * Chia theo ngôi: `ich höre`, `du hörst`, `er/sie/es hört`, `wir hören`, `ihr hört`, `sie/Sie hören`.
    * Ví dụ: *„Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.“ (Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc.)*
12. **`wenden`** (*quay đầu lại* — Gốc `-d` thêm `-e-`):
    * Chia theo ngôi: `ich wende`, `du wendest`, `er/sie/es wendet`, `wir wenden`, `ihr wendet`, `sie/Sie wenden`.
    * Ví dụ: *„Sie fahren in die falsche Richtung, bitte wenden Sie an der nächsten Kreuzung!“ (Ngài đang lái xe sai hướng rồi, xin hãy quay đầu ở ngã tư tiếp theo!)*

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung 2 chủ đề lọc mới của Bài 8 với đầy đủ **50 danh từ có mạo từ (`der/die/das`), dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng thẻ từ vựng**:
1. **`Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)`**
2. **`Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)`**

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 8: "STADT - HỎI ĐƯỜNG / CHỈ ĐƯỜNG - ĐỘNG TỪ KHUYẾT THIẾU" (KÈM HỆ THỐNG SƠ ĐỒ & BẢN ĐỒ SVG TRỰC QUAN)

Bài học thứ 9 trong danh sách Cấp độ A1 (`lesson_order = 9`):
* **Tiêu đề bài học**: `Bài 8: Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu (Thành phố Berlin - Định hướng Bản đồ & Modalverben)`
* **Mô tả ngắn**: `Khám phá từ vựng các địa điểm trong thành phố (In der Stadt) và 14 danh lam thắng cảnh nổi tiếng tại Berlin; nắm vững nghệ thuật Hỏi đường & Chỉ đường với hệ thống Sơ đồ Không gian và Bản đồ Đường phố SVG trực quan (an...vorbei, durch, über, entlang, bis zur...); phân biệt cách đi vào trong (in + Akkusativ) với đi tới địa điểm (zu + Dativ) và làm chủ bộ 4 Động từ khuyết thiếu (möchten, können, müssen, wollen).`

---

### HỌC PHẦN 1: TỪ VỰNG ĐỊA ĐIỂM TRONG THÀNH PHỐ (`IN DER STADT`) & DANH LAM THẮNG CẢNH BERLIN (`SEHENSWÜRDIGKEITEN IN BERLIN`)

#### 1.1. Bảng 1: Hệ Thống Địa Điểm Trong Thành Phố (`In der Stadt`) Phân Theo 3 Giống (`der / die / das`)
> 💡 **Mẹo Ngữ pháp & Từ vựng Cực Quan Trọng**:
> 1. **Danh từ ghép (`Komposita`)**: Giống của danh từ ghép luôn do **từ đứng cuối cùng (`Grundwort`)** quyết định:
>    * `der Hafen` *(cảng biển)* $\longrightarrow$ `der Flug` + **`der Hafen`** = **`der Flughafen`** *(sân bay — số nhiều: `die Flughäfen`)*.
>    * `der Markt` *(chợ)* $\longrightarrow$ `super` + **`der Markt`** = **`der Supermarkt`** *(siêu thị — số nhiều: `die Supermärkte`)*.
>    * `das Tor` *(cổng)* $\longrightarrow$ `die Stadt` + **`das Tor`** = **`das Stadttor`** *(cổng thành)* & **`das Brandenburger Tor`** *(Cổng Brandenburg)*.
>    * `das Haus` *(ngôi nhà)* $\longrightarrow$ **`das Krankenhaus`** *(bệnh viện — số nhiều: `die Krankenhäuser`)*.
>    * `das Zentrum` *(trung tâm)* $\longrightarrow$ **`das Einkaufszentrum`** *(trung tâm thương mại — số nhiều đổi `-um` thành `-en`: `die Einkaufszentren`)*.
> 2. **Phân biệt 2 nghĩa và 2 dạng số nhiều của danh từ `die Bank`**:
>    * **`die Bank`** *(ngân hàng — nơi giao dịch tiền)* $\longrightarrow$ Số nhiều: **`die Banken`**.
>    * **`die Bank`** *(ghế băng dài trong công viên)* $\longrightarrow$ Số nhiều: **`die Bänke`** *(như ghi chú trên bảng)*.
> 3. **Danh từ chỉ dùng ở số ít (`nur Singular`)**: **`die Post`** *(bưu điện / ngành bưu chính)* thường chỉ dùng ở số ít (`die Post`). Khi muốn đếm nhiều bưu cục cụ thể, người Đức dùng `das Postamt` $\rightarrow$ `die Postämter`.

| Giống Đực (<span style="color:#3b82f6">**`der` — Maskulinum**</span>) | Giống Cái (<span style="color:#f43f5e">**`die` — Femininum**</span>) | Giống Trung (<span style="color:#10b981">**`das` — Neutrum**</span>) |
| :--- | :--- | :--- |
| • **der Bahnhof** *(Pl: die Bahnh<u>ö</u>fe)*: nhà ga tàu hỏa<br>  $\rightarrow$ **der Hauptbahnhof**: nhà ga trung tâm<br>• **der Hafen** *(Pl: die H<u>ä</u>fen)*: cảng biển<br>  $\rightarrow$ **der Flughafen** *(Pl: die Flugh<u>ä</u>fen)*: sân bay<br>• **der Markt** *(Pl: die M<u>ä</u>rkte)*: chợ<br>  $\rightarrow$ **der Supermarkt** *(Pl: die Superm<u>ä</u>rkte)*: siêu thị<br>• **der Platz** *(Pl: die Pl<u>ä</u>tze)*: quảng trường, sân<br>• **der Park** *(Pl: die Parks)*: công viên<br>• **der Zoo** *(Pl: die Zoos)*: sở thú, vườn bách thú<br>• **der Turm** *(Pl: die T<u>ü</u>rme)*: tòa tháp<br>• **der Dom** *(Pl: die Dome)*: nhà thờ lớn | • **die Stadt** *(Pl: die St<u>ä</u>dte)*: thành phố<br>• **die Kirche** *(Pl: die Kirchen)*: nhà thờ<br>• **die Schule** *(Pl: die Schulen)*: trường học<br>• **die Brücke** *(Pl: die Brücken)*: cây cầu<br>• **die Bank** *(Pl: die Banken [ngân hàng] / die B<u>ä</u>nke [ghế dài])*<br>• **die Post** *(nur Sg.)*: bưu điện<br>• **die Straße** *(Pl: die Straßen)*: con đường, phố<br>• **die Ampel** *(Pl: die Ampeln)*: đèn giao thông<br>• **die Kreuzung** *(Pl: die Kreuzungen)*: ngã tư, giao lộ<br>• **die Disko** *(Pl: die Diskos)*: vũ trường, quán bar nhạc | • **das Schloss** *(Pl: die Schl<u>ö</u>sser)*: lâu đài, cung điện<br>• **das Stadttor** *(Pl: die Stadttore)*: cổng thành<br>• **das Kino** *(Pl: die Kinos)*: rạp chiếu phim<br>• **das Krankenhaus** *(Pl: die Krankenh<u>ä</u>user)*: bệnh viện<br>• **das Einkaufszentrum** *(Pl: die Einkaufszentr<u>en</u>)*: trung tâm thương mại<br>• **das Hotel** *(Pl: die Hotels)*: khách sạn<br>• **das Museum** *(Pl: die Muse<u>en</u>)*: viện bảo tàng<br>• **das Rathaus** *(Pl: die Rath<u>ä</u>user)*: tòa thị chính<br>• **das Theater** *(Pl: die Theater)*: nhà hát kịch |

---

#### 1.2. Bảng 2: 14 Danh Lam Thắng Cảnh Nổi Tiếng Tại Thủ Đô Berlin (`Sehenswürdigkeiten in Berlin`)
*(Phân loại chuẩn theo 3 giống `der / die / das` kèm giải thích từ gốc giúp nhớ ngay lập tức)*

| Giống Đực (<span style="color:#3b82f6">**`der`**</span>) | Giống Cái (<span style="color:#f43f5e">**`die`**</span>) | Giống Trung (<span style="color:#10b981">**`das`**</span>) |
| :--- | :--- | :--- |
| 1. **der Reichstag**: Tòa nhà Quốc hội Đức *(vì `der Tag`)*<br>2. **der Alexanderplatz**: Quảng trường Alexander *(vì `der Platz`)*<br>3. **der Potsdamer Platz**: Quảng trường Potsdam *(vì `der Platz`)*<br>4. **der Berliner Dom**: Nhà thờ lớn Berlin *(vì `der Dom`)*<br>5. **der Fernsehturm**: Tháp truyền hình Berlin *(vì `der Turm`)* | 6. **die Humboldt-Universität**: Đại học Humboldt *(vì `-tät` luôn là `die`)*<br>7. **die Staatsoper**: Nhà hát Opera Quốc gia *(vì `die Oper`)*<br>8. **die Friedrichstraße**: Phố mua sắm Friedrich *(vì `die Straße`)*<br>9. **die Museumsinsel**: Đảo Bảo tàng *(vì `die Insel` - hòn đảo)*<br>10. **die Alte Nationalgalerie**: Khu triển lãm Quốc gia Cũ *(vì `-ie` luôn là `die`)* | 11. **das Bundeskanzleramt**: Phủ Thủ tướng Liên bang *(vì `das Amt` - cơ quan/phủ)*<br>12. **das Brandenburger Tor**: Cổng thành Brandenburg *(vì `das Tor` - cánh cổng)*<br>13. **das Schloss Bellevue**: Cung điện Bellevue *(vì `das Schloss` - cung điện)*<br>14. **das Sony Center**: Trung tâm phức hợp Sony *(vì `das Center`)* |

---

### HỌC PHẦN 2: NGHỆ THUẬT HỎI ĐƯỜNG (`NACH DEM WEG FRAGEN`) & CHỈ ĐƯỜNG (`DEN WEG BESCHREIBEN`) KÈM SƠ ĐỒ MINH HỌA TRỰC QUAN

#### 2.1. Bốn Cấu Trúc Hỏi Đường Lịch Sự Trong Tiếng Đức (`Nach dem Weg fragen`)
Khi muốn hỏi đường một người trên phố ở Đức, luôn bắt đầu bằng **`Entschuldigung, ...`** *(Xin lỗi cho tôi hỏi...)* hoặc **`Entschuldigen Sie bitte, ...`**:

| Mẫu Câu Hỏi Đường (`🔊 de-DE`) | Quy Tắc Ngữ Pháp Đi Kèm | Ví Dụ Cụ Thể Đa Địa Điểm (`🔊 de-DE`) |
| :--- | :--- | :--- |
| **1. `Entschuldigung, ich suche + [Akkusativ].`**<br>*(Xin lỗi, tôi đang tìm...)* | Động từ **`suchen`** *(tìm kiếm)* luôn đòi hỏi **Cách 4 (`Akkusativ`)**:<br>• `den Bahnhof` (`m`)<br>• `die Post` (`f`)<br>• `das Kino` (`n`) | • *„Entschuldigung, ich suche **das Kino**.“*<br>• *„Entschuldigung, ich suche **den Berliner Dom**.“*<br>• *„Entschuldigung, ich suche **die Humboldt-Universität**.“* |
| **2. `Entschuldigung, wo ist + [Nominativ]?`**<br>*(Xin lỗi, ... ở đâu vậy?)* | Động từ **`sein` (`ist/sind`)** luôn đi với **Cách 1 (`Nominativ`)**:<br>• `der Bahnhof` (`m`)<br>• `die Bank` (`f`)<br>• `das Kino` (`n`) | • *„Entschuldigung, wo ist **das Kino**?“*<br>• *„Entschuldigung, wo ist hier **eine Bank**?“*<br>• *„Entschuldigung, wo ist **der Alexanderplatz**?“* |
| **3. `Entschuldigung, wo geht es + [Hướng đích]?`**<br>*(Xin lỗi, đi lối nào để tới...?)* | Dùng **`ins` (`in + das`)** / **`in die`** hoặc phổ biến nhất là **`zum` (`zu + dem`)** / **`zur` (`zu + der`)**: | • *„Entschuldigung, wo geht es **ins Kino**?“*<br>• *„Entschuldigung, wo geht es **zum Bahnhof**?“*<br>• *„Entschuldigung, wo geht es **zur Museumsinsel**?“* |
| **4. `Entschuldigung, wie komme ich + [Hướng đích]?`**<br>*(Xin lỗi, làm thế nào tôi đi đến được...?)* | Đi với **`ins / in den / in die`** hoặc **`zum / zur`**: | • *„Entschuldigung, wie komme ich **ins Kino**?“*<br>• *„Entschuldigung, wie komme ich **zum Brandenburger Tor**?“*<br>• *„Entschuldigung, wie komme ich **zur Post**?“* |

---

#### 2.2. Khung Cấu Trúc Chỉ Đường Theo Trình Tự Thời Gian (`Zuerst -> Dann -> Danach -> Zum Schluss`)
Khi chỉ đường cho người khác (dùng ngôi trang trọng **`Sie`** với câu mệnh lệnh **`Gehen Sie ...!`** *Ngài hãy đi bộ...* hoặc **`Fahren Sie ...!`** *Ngài hãy đi xe...*), ta nối các chặng bằng các trạng từ chỉ trình tự (đứng đầu câu $\rightarrow$ động từ đứng ngay vị trí số 2):
1. **`Zuerst`** `gehen Sie ...` *(Đầu tiên Ngài hãy đi...)*
2. **`Dann`** `gehen Sie ...` *(Sau đó Ngài hãy đi...)*
3. **`Danach`** `gehen Sie ...` *(Tiếp theo đó Ngài hãy đi...)*
4. **`Anschließend`** / **`Zum Schluss`** `gehen Sie ...` *(Tiếp nối theo / Cuối cùng Ngài hãy đi...)*
5. **`Links / Rechts sehen Sie ...`** *(Ở bên trái / bên phải Ngài sẽ nhìn thấy...)*

---

#### 2.3. BỘ 4 SƠ ĐỒ KHÔNG GIAN TRỰC QUAN (`SVG SPATIAL PREPOSITION DIAGRAMS` — BẮT BUỘC VẼ TRÊN GIAO DIỆN LÝ THUYẾT)
Antigravity IDE phải render **4 thẻ sơ đồ SVG lớn, có hiệu ứng mũi tên chuyển động** giải thích 4 cụm giới từ chỉ đường quan trọng nhất trong ảnh chụp bảng viết:

| Sơ Đồ Minh Họa SVG (Bắt buộc hiển thị trực quan trên Web) | Công Thức Ngữ Pháp | Giải Thích & Ví Dụ Thực Chiến (`🔊 de-DE`) |
| :--- | :--- | :--- |
| **Sơ đồ 1: `an ... vorbei` *(Đi ngang qua bên cạnh)***<br>*(Vẽ tòa nhà `Universität` / `Kirche` / `Bank` nằm bên lề đường, mũi tên đi thẳng dọc theo vỉa hè lướt ngang qua mặt tiền tòa nhà mà không rẽ vào trong)* | **`an` + CÁCH 3 (`DATIV`) + `vorbei`**<br>• Giống đực (`der`) & trung (`das`): **`am ... vorbei`** *(an + dem)*<br>• Giống cái (`die`): **`an der ... vorbei`** | • *„Gehen Sie **an <u>der</u> Universität vorbei**!“* *(Hãy đi ngang qua trường đại học!)*<br>• *„Gehen Sie **an <u>der</u> Kirche vorbei**!“* *(Hãy đi ngang qua nhà thờ!)*<br>• *„Sie fahren mit dem Bus **<u>am</u> Bundeskanzleramt vorbei**.“* *(Họ đi xe buýt ngang qua Phủ Thủ tướng.)* |
| **Sơ đồ 2: `durch ...` *(Đi xuyên qua lòng không gian)***<br>*(Vẽ chiếc cổng vòm `das Tor` / `Brandenburger Tor` hoặc công viên `der Park`, mũi tên đâm xuyên từ bên này qua chính giữa lòng cổng sang bên kia)* | **`durch` + CÁCH 4 (`AKKUSATIV`)**<br>• Giống đực: **`durch den`**<br>• Giống cái: **`durch die`**<br>• Giống trung: **`durch das`** *(hoặc `durchs`)* | • *„Gehen Sie **durch <u>das</u> Tor**!“* *(Hãy đi xuyên qua cánh cổng!)*<br>• *„Wir laufen **durch <u>den</u> Park**.“* *(Chúng tôi chạy bộ xuyên qua công viên.)* |
| **Sơ đồ 3: `über ...` *(Đi vượt qua / băng qua bề mặt)***<br>*(Vẽ cây cầu vòm `die Brücke`, quảng trường tròn `der Platz` hoặc ngã tư `die Kreuzung`, mũi tên đi băng từ đầu bên này vượt qua bề mặt sang đầu bên kia)* | **`über` + CÁCH 4 (`AKKUSATIV`)**<br>*(Vì có sự di chuyển `Wohin?`)*<br>• Giống đực: **`über den`**<br>• Giống cái: **`über die`**<br>• Giống trung: **`über das`** | • *„Gehen Sie **über <u>die</u> Brücke**!“* *(Hãy đi qua cây cầu!)*<br>• *„Gehen Sie **über <u>den</u> Platz**!“* *(Hãy đi băng qua quảng trường!)*<br>• *„Gehen Sie geradeaus, **über <u>die</u> Kreuzung**!“* *(Hãy đi thẳng, băng qua ngã tư!)* |
| **Sơ đồ 4: `... entlang` *(Đi dọc theo chiều dài)***<br>*(Vẽ con đường uốn lượn `die Straße` hoặc bờ sông `der Fluss`, mũi tên chạy song song dọc suốt chiều dài con đường; lưu ý từ `entlang` đứng **SAU** danh từ!)* | **CÁCH 4 (`AKKUSATIV`) + `entlang`**<br>*(Từ `entlang` đặt **sau** danh từ ở Akkusativ)*<br>• **`die Straße entlang`**<br>• **`den Fluss entlang`** | • *„Gehen Sie **<u>die</u> Straße entlang**!“* *(Hãy đi dọc theo con đường!)*<br>• *„Gehen Sie **<u>die</u> Lạch-Tray-Straße entlang**!“* *(Hãy đi dọc theo đường Lạch Tray!)*<br>• *„Wir spazieren **<u>den</u> Fluss entlang**.“* *(Chúng tôi đi dạo dọc theo bờ sông.)* |

---

#### 2.4. BỘ 12 THẺ HÌNH MINH HỌA CHỈ ĐƯỜNG (`VISUAL DIRECTION CARDS a -> l` — KHỚP 100% BÀI GIẢNG TRÊN BẢNG & MỞ RỘNG)
Antigravity IDE phải hiển thị **Lưới 12 Thẻ Hình Chỉ Đường bằng SVG (`Direction Icon Grid`)** để người học nhìn hình là thuộc ngay câu lệnh tiếng Đức:

| Mã Hình | Mô Tả Hình Vẽ SVG Cần Render Chính Xác (`static/js/city_map_svg.js`) | Câu Lệnh Tiếng Đức Chuẩn (`🔊 de-DE`) | Giải Thích Ngữ Pháp & Nghĩa Tiếng Việt |
| :---: | :--- | :--- | :--- |
| **`Hình a)`** | Con đường thẳng nhìn từ dưới lên, hai bên có vỉa hè gạch chéo, **mũi tên đi thẳng về phía trước (`↑`)**. | ***„Gehen Sie geradeaus.“***<br>*(Câu số 3 trên bảng)* | **Ngài hãy đi thẳng.** (`geradeaus` = thẳng tiến về phía trước). |
| **`Hình b)`** | Con đường chạy chéo, bên phải đường là **tòa nhà thờ có thánh giá trên mái (`⛪ Kirche`)**, mũi tên đi thẳng lướt ngang qua mặt nhà thờ. | ***„Gehen Sie an der Kirche vorbei.“***<br>*(Câu số 8 trên bảng)* | **Ngài hãy đi ngang qua nhà thờ.** (`an + der Kirche [Dativ] + vorbei`). |
| **`Hình c)`** | Khúc đường có **cột đèn giao thông 3 màu (`🚦 Ampel`)** ở phía trước, mũi tên đi tới ngay chân cột đèn thì dừng lại. | ***„Gehen Sie bis zur Ampel.“***<br>*(Câu số 5 trên bảng)* | **Ngài hãy đi cho đến đèn giao thông.** (`bis zu + der Ampel [Dativ] = bis zur Ampel`). |
| **`Hình d)`** | Giao lộ **ngã tư chữ thập (`➕ Kreuzung`)**, mũi tên từ dưới đi thẳng tới sát tâm ngã tư thì dừng lại. | ***„Gehen Sie bis zur Kreuzung.“***<br>*(Câu số 6 trên bảng)* | **Ngài hãy đi cho đến ngã tư.** (`bis zu + der Kreuzung [Dativ] = bis zur Kreuzung`). |
| **`Hình e)`** | Con đường chính có **2 ngã rẽ bên tay trái**; mũi tên đi thẳng qua ngã rẽ trái thứ nhất và **quẹo trái ở ngã rẽ thứ hai**. | ***„Gehen Sie die zweite Straße links.“***<br>*(Câu số 7 trên bảng)* | **Ngài hãy rẽ trái ở con đường thứ hai.** (Số thứ tự `zweite` đứng trước danh từ giống cái `die Straße`). |
| **`Hình f)`** | Một **quảng trường hình tròn (`⭕ Platz`)** ở giữa có bồn cây/đài phun nước, mũi tên đi xuyên từ mép dưới băng qua quảng trường lên mép trên. | ***„Gehen Sie über den Platz.“***<br>*(Câu số 9 trên bảng)* | **Ngài hãy đi băng qua quảng trường.** (`über + den Platz [Akkusativ]`). |
| **`Hình g)`** | Ngã rẽ chữ T/ngã tư, **mũi tên quẹo sang bên tay trái (`↰`)** ngay tại ngã rẽ hiện tại. | ***„Gehen Sie hier links.“***<br>*(Câu số 2 trên bảng)* | **Ngài hãy rẽ trái ở đây.** (`links` = bên trái). |
| **`Hình h)`** | Ngã rẽ chữ T/ngã tư, **mũi tên quẹo sang bên tay phải (`↱`)** ngay tại ngã rẽ hiện tại. | ***„Gehen Sie hier rechts.“***<br>*(Câu số 1 trên bảng)* | **Ngài hãy rẽ phải ở đây.** (`rechts` = bên phải). |
| **`Hình i)`** | Con đường uốn cong chữ S, **mũi tên uốn lượn chạy dọc suốt theo chiều dài con đường**. | ***„Gehen Sie die Straße entlang.“***<br>*(Câu số 4 trên bảng)* | **Ngài hãy đi dọc theo con đường.** (`die Straße [Akkusativ] + entlang`). |
| **`Hình j)`**<br>*(Mở rộng)* | Con đường chính có **2 ngã rẽ bên tay phải**; mũi tên bỏ qua ngã rẽ phải thứ nhất và **quẹo phải ở ngã rẽ thứ hai**. | ***„Gehen Sie die zweite Straße rechts.“*** | **Ngài hãy rẽ phải ở con đường thứ hai.** |
| **`Hình k)`**<br>*(Mở rộng)* | **Cổng thành hình vòm (`⛩️ das Stadttor / Brandenburger Tor`)**, mũi tên đi xuyên qua chính giữa cổng vòm. | ***„Gehen Sie durch das Tor.“*** | **Ngài hãy đi xuyên qua cánh cổng.** (`durch + das Tor [Akkusativ]`). |
| **`Hình l)`**<br>*(Mở rộng)* | **Cây cầu bắc qua sông (`🌉 die Brücke`)**, mũi tên đi vòng qua mặt cầu từ bờ này sang bờ kia. | ***„Gehen Sie über die Brücke.“*** | **Ngài hãy đi qua cây cầu.** (`über + die Brücke [Akkusativ]`). |

---

#### 2.5. BẢN ĐỒ LƯỚI ĐƯỜNG PHỐ TƯƠNG TÁC (`INTERACTIVE MULTI-ROUTE GRID MAP` — TÁI HIỆN BẢN ĐỒ TRÊN BẢNG VIẾT)
Antigravity IDE phải vẽ một **Bản đồ Đường phố Tương tác bằng SVG** tái hiện chính xác sơ đồ trên bảng viết (với người đứng ở góc dưới bên trái `📍 Start`, tòa nhà **`🏦 Bank`** nằm ở đường ngang thứ 2, và **`📮 Post` + `🚦 Ampel`** nằm ở góc trên bên phải), cho phép người dùng bấm xem 2 lộ trình thực tế:

* **Lộ trình 1 (Đường màu xanh dương — Đi qua Ngân hàng)**:
  > **Tiếng Đức (`🔊 de-DE`)**: *„**Zuerst** gehen Sie geradeaus. **Dann** gehen Sie die erste Straße rechts, **an der Bank vorbei**. **Dann** gehen Sie bis zur zweiten Kreuzung links. **Danach** gehen Sie **bis zur Ampel**. Rechts sehen Sie **die Post**.“*
  > **Dịch nghĩa**: *„Đầu tiên Ngài đi thẳng. Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. Sau đó Ngài đi đến ngã tư thứ hai thì rẽ trái. Tiếp theo Ngài đi cho đến đèn giao thông. Ở bên phải Ngài sẽ nhìn thấy bưu điện.“*
* **Lộ trình 2 (Đường màu xanh lá — Đi thẳng lên ngã tư thứ 2 rồi rẽ phải)**:
  > **Tiếng Đức (`🔊 de-DE`)**: *„**Zuerst** gehen Sie geradeaus, **bis zur zweiten Kreuzung rechts**. **Dann** gehen Sie geradeaus, **über die Kreuzung**. Links sehen Sie **die Post**.“*
  > **Dịch nghĩa**: *„Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện.“*

---

### HỌC PHẦN 3: CHUYÊN ĐỀ PHÂN BIỆT CẤU TRÚC ĐI ĐẾN ĐỊA ĐIỂM: `ZU + DATIV` (`ZUM / ZUR`) VS. `IN + AKKUSATIV` (`IN DEN / IN DIE / INS`)

Trong đoạn văn về **Paula và Alex ở Berlin** trên bảng viết, có hai cách nói *"đi đến một địa điểm"* mà người học rất hay thắc mắc: tại sao lúc thì dùng **`gehen zum Brandenburger Tor`**, lúc lại dùng **`gehen in den Berliner Dom`** hay **`gehen in die Disko`**?

| Tiêu Chí Phân Biệt | 1. **`zu` + CÁCH 3 (`DATIV`)**<br>(`zum` = `zu dem` / `zur` = `zu der`) | 2. **`in` + CÁCH 4 (`AKKUSATIV`)**<br>(`in den` / `in die` / `ins` = `in das`) |
| :--- | :--- | :--- |
| **Ý nghĩa không gian** | Nhấn mạnh **hướng di chuyển tới địa điểm / công trình đó** (đến trước cổng, đến khu vực đó, hoặc đến làm việc/giao dịch mà không nhấn mạnh việc bước vào bên trong lòng kiến trúc kín). | Nhấn mạnh hành động **bước hẳn vào BÊN TRONG lòng tòa nhà / không gian khép kín** để xem phim, nghe nhạc, nhảy múa, ăn uống, tham quan triển lãm... |
| **Biến đổi mạo từ theo giống** | • Giống đực (`der`): **`zum`** (*zum Bahnhof, zum Flughafen, zum Reichstag, zum Alexanderplatz*)<br>• Giống trung (`das`): **`zum`** (*zum Brandenburger Tor, zum Schloss Bellevue*)<br>• Giống cái (`die`): **`zur`** (*zur Post, zur Bank, zur Kirche, zur Schule, zur Ampel, zur Kreuzung*) | • Giống đực (`der`): **`in den`** (*in den Berliner Dom, in den Supermarkt, in den Park, in den Zoo*)<br>• Giống trung (`das`): **`ins`** (*ins Kino, ins Theater, ins Museum, ins Einkaufszentrum, ins Hotel*)<br>• Giống cái (`die`): **`in die`** (*in die Disko, in die Nationalgalerie, in die Staatsoper, in die Kirche*) |
| **Ví dụ đối chiếu từ bài giảng (`🔊 de-DE`)** | • *„Paula und Alex gehen **<u>zum</u> Brandenburger Tor** und machen viele Fotos.“* *(Paula và Alex đi **đến Cổng Brandenburg** và chụp nhiều bức ảnh — đứng ở khu vực cổng chụp ảnh).*<br>• *„Gehen Sie **bis <u>zur</u> Ampel** / **bis <u>zur</u> Kreuzung**!“* *(Hãy đi **đến chỗ đèn giao thông / ngã tư**!)* | • *„Am Nachmittag gehen sie **<u>in den</u> Berliner Dom** und hören ein Konzert.“* *(Buổi chiều họ đi **vào trong Nhà thờ lớn Berlin** và nghe hòa nhạc).*<br>• *„Am Abend gehen sie **<u>in die</u> Disko** ‚Von Euch‘.“* *(Buổi tối họ đi **vào vũ trường** 'Von Euch'.)*<br>• *„Danach will ich **<u>in die</u> Nationalgalerie** gehen.“* *(Tiếp theo tôi muốn đi **vào Khu triển lãm Quốc gia**.)* |

---

### HỌC PHẦN 4: HỆ THỐNG BẢNG MA TRẬN 4 ĐỘNG TỪ KHUYẾT THIẾU (`MÖCHTEN - KÖNNEN - MÜSSEN - WOLLEN`) & TRẠNG TỪ TRÌNH TỰ

#### 4.1. Bảng Ma Trận Đối Chiếu 4 Động Từ Khuyết Thiếu Trọng Tâm Trên Bảng Viết (`Berlin sehen`)
> **Điểm mới trọng tâm của Bài 8**: Bổ sung động từ khuyết thiếu **`wollen` *(muốn — thể hiện ý định mạnh mẽ, quyết tâm hoặc kế hoạch rõ ràng)*** và đặt cạnh **`möchten` *(muốn — lịch sự, nhã nhặn khi gọi món hoặc đề xuất)***.
> * Lưu ý biến âm của **`wollen`**: Đổi nguyên âm gốc **`o -> i`** ở cả 3 ngôi số ít (`ich will`, `du willst`, `er/sie/es will`), và ngôi `ich` bằng ngôi `er/sie/es` (`will` — không có đuôi `-e` hay `-t`!).

| Ngôi Nhân Xưng | 1. **`möchten`**<br>*(muốn — lịch sự, ước muốn)* | 2. **`können`**<br>*(có thể, có khả năng)* | 3. **`müssen`**<br>*(phải, bắt buộc)* | 4. **`wollen`** ⭐<br>*(muốn — ý định/kế hoạch mạnh)* |
| :--- | :---: | :---: | :---: | :---: |
| **`ich`** *(tôi)* | **möchte** | **kann** | **muss** | <span style="color:#ec4899">**will**</span> ⚠️ |
| **`du`** *(bạn)* | **möchtest** | **kannst** | **musst** | <span style="color:#ec4899">**willst**</span> ⚠️ |
| **`er / sie / es`** *(anh/cô ấy/nó)* | **möchte** | **kann** | **muss** | <span style="color:#ec4899">**will**</span> ⚠️ |
| **`wir`** *(chúng tôi)* | **möchten** | **können** | **müssen** | **wollen** |
| **`ihr`** *(các bạn)* | **möchtet** | **könnt** | **müsst** | **wollt** |
| **`Sie / sie`** *(Ngài / họ)* | **möchten** | **können** | **müssen** | **wollen** |

* **4 Câu Ví Dụ Kinh Điển Trên Bảng Viết (`🔊 de-DE`)**:
  1. *„Ich **möchte** Kaffee **trinken**.“* *(Tôi muốn uống cà phê — lời gọi đồ lịch sự).*
  2. *„Ich **kann** gut **kochen**.“* *(Tôi có thể nấu ăn ngon — chỉ kỹ năng).*
  3. *„Am Wochenende **muss** ich **arbeiten**.“* *(Vào cuối tuần tôi phải làm việc — sự bắt buộc).*
  4. *„In Deutschland **will** ich **studieren**.“* *(Ở Đức tôi muốn học đại học — kế hoạch/mục tiêu quyết tâm).*

---

### HỌC PHẦN 5: PHÂN TÍCH 2 ĐOẠN VĂN MẪU TRONG BÀI GIẢNG (`TEXTANALYSE: BERLIN SEHEN` — KÈM AUDIO `de-DE`)

#### 5.1. Đoạn văn 1: Hành trình khám phá Berlin của Paula và Alex (`Giới từ chỉ hướng & địa điểm`)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin. Sie gehen **zum Brandenburger Tor** (`zu + dem`) und machen viele Fotos. Sie fahren mit dem Bus **am Bundeskanzleramt vorbei** (`an + dem ... vorbei`) und laufen **über die Schlossbrücke** (`über + Akkusativ`). Am Nachmittag gehen sie **in den Berliner Dom** (`in + Akkusativ`) und hören ein Konzert. Am Abend essen sie Pizza und gehen danach **in die Disko** ‚Von Euch‘ (`in + Akkusativ`).“*
* **Dịch nghĩa tiếng Việt**:
  > *„Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin. Họ đi đến Cổng Brandenburg và chụp nhiều bức ảnh. Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke. Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ ăn bánh Pizza và sau đó đi vào vũ trường 'Von Euch'.“*

#### 5.2. Đoạn văn 2: Tin nhắn kể kế hoạch du lịch Berlin gửi Julia (`Động từ khuyết thiếu wollen + Trạng từ trình tự`)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Hi Julia! Berlin ist super! Wir **wollen** noch eine Stadtrundfahrt **machen**. **Danach will** ich in die Nationalgalerie **gehen**. **Anschließend wollen** Maria und ich auf der Friedrichstraße **bummeln**. Und heute Abend **wollen** wir noch einen Film im Kino **sehen**.“*
* **Dịch nghĩa tiếng Việt & Từ vựng trọng tâm**:
  > *„Chào Julia! Berlin tuyệt vời lắm! Chúng mình còn muốn thực hiện một chuyến tham quan vòng quanh thành phố (`eine Stadtrundfahrt machen`). Sau đó (`Danach`) mình muốn đi vào Khu triển lãm Quốc gia. Tiếp ngay sau đó (`Anschließend`) Maria và mình muốn đi dạo phố (`bummeln`) trên đường Friedrich. Và tối nay chúng mình còn muốn xem một bộ phim ở trong rạp chiếu phim.“*

---

## PHẦN 3: KHO 100 BÀI TẬP ĐỘC NHẤT CỦA BÀI 8 (`lessons/a1/seed_a1_b8.py`) — TÍCH HỢP SƠ ĐỒ / BẢN ĐỒ SVG & BỘ RANDOM ĐỔI ĐỀ ĐA CHIỀU

Toàn bộ **100 câu hỏi (`100 Unique Exercises`)** dưới đây đã được thiết kế sáng tạo, **tích hợp hình ảnh sơ đồ mũi tên & bản đồ đường phố SVG ngay trong câu hỏi**, bao phủ trọn vẹn 9 dạng bài tập, đa dạng hóa chủ ngữ (`ich, du, er, sie, es, wir, ihr, sie, Sie`, tên riêng, khách du lịch...) và kiểm tra chéo để đảm bảo **0% trùng lặp**.

### 3.1. Bảng Phân Bổ 100 Câu Hỏi Bài 8 Theo 9 Dạng Bài Tập
| STT | Mã Dạng (`type`) | Tên Dạng Bài Tập Hiển Thị | Số Lượng | Nội Dung Trọng Tâm & Tích Hợp Hình Minh Họa SVG Trong Bài 8 |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **`trac_nghiem`** | **Trắc nghiệm (Có Sơ đồ & Bản đồ SVG)** | **18 câu** | • **8 câu nhìn Sơ đồ / Bản đồ SVG** chọn câu chỉ đường hoặc đích đến đúng (`an...vorbei`, `durch...`, `über...`, `...entlang`, `bis zur Ampel/Kreuzung`, `zweite Straße links/rechts`)<br>• **10 câu ngữ pháp & từ vựng chuyên sâu**: Giống & số nhiều của địa điểm (`der Bahnhof -> die Bahnhöfe`, `das Schloss -> die Schlösser`, `die Bank -> die Banken/Bänke`, `die Post` chỉ số ít), 14 danh lam thắng cảnh Berlin, phân biệt `zum/zur` vs. `in den/in die/ins`, và chia động từ khuyết thiếu `wollen, möchten, können, müssen`. |
| **2** | **`dien_khuyet`** | **Điền khuyết (Có Sơ đồ & Bản đồ SVG)** | **15 câu** | • Điền dạng chia đúng của `wollen` (`will, willst, wollen, wollt`) và các động từ chỉ đường<br>• Nhìn bản đồ/sơ đồ SVG điền giới từ và mạo từ đúng (`am ... vorbei`, `an der ... vorbei`, `über die`, `über den`, `durch das`, `entlang`, `bis zur`, `in den`, `zum`). |
| **3** | **`dich_nghia_vd`** | **Dịch từ/cụm từ: Việt $\rightarrow$ Đức** | **12 câu** | Dịch các địa điểm trong thành phố, danh lam thắng cảnh Berlin và các cụm khẩu lệnh chỉ đường từ tiếng Việt sang tiếng Đức. |
| **4** | **`dich_nghia_dv`** | **Dịch từ/cụm từ: Đức $\rightarrow$ Việt** | **12 câu** | Dịch các danh lam thắng cảnh Berlin, địa điểm thành phố và các cụm chỉ đường từ tiếng Đức sang tiếng Việt. |
| **5** | **`noi_o`** | **Nối ô từ trái qua phải (Matching Pairs)** | **10 bài** | 10 bài ghép cặp (mỗi bài 4 cặp = 40 mệnh đề độc nhất):<br>• Bài 1 & 2: Nối Mô tả Biểu tượng Chỉ đường (`Hình a -> i`) $\leftrightarrow$ Khẩu lệnh tiếng Đức tương ứng<br>• Bài 3: Nối Địa điểm trong thành phố $\leftrightarrow$ Dạng số nhiều & Nghĩa<br>• Bài 4 & 5: Nối 14 Danh lam thắng cảnh Berlin $\leftrightarrow$ Mạo từ (`der/die/das`) & Ý nghĩa<br>• Bài 6: Nối Câu hỏi đường $\leftrightarrow$ Cấu trúc ngữ pháp tương ứng<br>• Bài 7: Nối Giới từ không gian (`an...vorbei`, `durch`, `über`, `entlang`) $\leftrightarrow$ Cách ngữ pháp & Sơ đồ<br>• Bài 8: Nối Ngôi nhân xưng $\leftrightarrow$ Dạng chia của `wollen` và `möchten`<br>• Bài 9: Nối Chặng hành trình của Paula & Alex ở Berlin $\leftrightarrow$ Cụm giới từ đích<br>• Bài 10: Nối Thứ tự các bước trên Bản đồ thành phố (`Zuerst -> Dann -> Danach -> Rechts`) $\leftrightarrow$ Hành động tương ứng. |
| **6** | **`dien_tao_cau`** | **Điền vào chỗ trống tạo câu (Kèm Bản đồ)** | **10 câu** | Nhìn sơ đồ/bản đồ SVG hoặc ngữ cảnh du lịch, điền 2 từ còn thiếu để tạo thành câu chỉ đường hoặc câu kế hoạch với `wollen`. |
| **7** | **`nghe_dien`** | **Nghe giọng đọc `de-DE` và điền từ** | **9 câu** | Nghe câu chỉ đường / thuyết minh du lịch Berlin bằng giọng bản xứ `de-DE` (kèm sơ đồ minh họa) và điền từ chính xác. |
| **8** | **`dich_cau_vd`** | **Dịch câu: Việt $\rightarrow$ Đức (Kèm Bản đồ)** | **7 câu** | Dịch các câu hỏi đường, chỉ đường theo sơ đồ và kế hoạch tham quan với `wollen` từ tiếng Việt sang tiếng Đức (chấm đa đáp án). |
| **9** | **`dich_cau_dv`** | **Dịch câu: Đức $\rightarrow$ Việt (Kèm Bản đồ)** | **7 câu** | Dịch các câu lộ trình trên bản đồ và hành trình khám phá Berlin từ tiếng Đức sang tiếng Việt (chấm đa đáp án). |
| | | **TỔNG CỘNG BÀI 8** | **100 CÂU** | **100% Câu hỏi Độc nhất + Có Hình Sơ đồ/Bản đồ SVG + QA Zero-Bug** |

---

### 3.2. Danh Sách Chi Tiết 100 Câu Hỏi Chuẩn Xác & Độc Nhất Của Bài 8 (Để Seed Vào `lessons/a1/seed_a1_b8.py`)

#### NHÓM 1: TRẮC NGHIỆM KÈM SƠ ĐỒ & BẢN ĐỒ SVG (`trac_nghiem` — 18 Câu: Câu 1 $\rightarrow$ Câu 18)
1. **Câu 1 (Nhìn Sơ đồ SVG `Hình e` — Ngã rẽ thứ 2 bên trái)**:
   * `visual_svg`: Render **`direction_card_e`** *(Con đường có 2 ngã rẽ bên trái, mũi tên bỏ qua ngã rẽ thứ nhất và quẹo trái ở ngã rẽ thứ hai)*.
   * `question`: Quan sát **Sơ đồ chỉ đường `e)`** bên trên và chọn câu lệnh tiếng Đức khớp chính xác với mũi tên:
   * Đáp án: `A. Gehen Sie hier links.` | `B. Gehen Sie die erste Straße links.` | `C. Gehen Sie die zweite Straße links.` (Đúng) | `D. Gehen Sie die zweite Straße rechts.`
   * Dịch nghĩa câu: *"Ngài hãy rẽ trái ở con đường thứ hai."*
   * Giải thích: Trên sơ đồ `e)`, mũi tên đi qua ngã rẽ trái thứ nhất và quẹo vào ngã rẽ trái thứ hai $\rightarrow$ **`Gehen Sie die zweite Straße links.`**
2. **Câu 2 (Nhìn Sơ đồ SVG `Hình b` — Đi ngang qua Nhà thờ)**:
   * `visual_svg`: Render **`direction_card_b`** *(Con đường có tòa nhà thờ có thánh giá `⛪ Kirche`, mũi tên đi thẳng ngang qua mặt tiền nhà thờ)*.
   * `question`: Quan sát **Sơ đồ chỉ đường `b)`** bên trên: Mũi tên chỉ hành động đi ngang qua nhà thờ (`die Kirche`). Câu nào dưới đây đúng ngữ pháp 100%?
   * Đáp án: `A. Gehen Sie an die Kirche vorbei.` | `B. Gehen Sie an der Kirche vorbei.` (Đúng) | `C. Gehen Sie durch die Kirche.` | `D. Gehen Sie über der Kirche.`
   * Dịch nghĩa câu: *"Ngài hãy đi ngang qua nhà thờ."*
   * Giải thích: Cấu trúc *"đi ngang qua bên cạnh một địa điểm"* luôn dùng **`an + Dativ + vorbei`**. Vì `die Kirche` mang giống cái (`Femininum`), ở `Dativ` mạo từ `die` đổi thành **`der`** $\rightarrow$ **`an der Kirche vorbei`**.
3. **Câu 3 (Nhìn Sơ đồ SVG `Hình f` — Đi băng qua Quảng trường)**:
   * `visual_svg`: Render **`direction_card_f`** *(Quảng trường hình tròn có bồn cây ở giữa, mũi tên đi băng xuyên qua bề mặt quảng trường)*.
   * `question`: Quan sát **Sơ đồ chỉ đường `f)`** bên trên: Để chỉ đường *"Ngài hãy đi băng qua quảng trường (`der Platz`)"*, ta nói như thế nào?
   * Đáp án: `A. Gehen Sie über dem Platz.` | `B. Gehen Sie über den Platz.` (Đúng) | `C. Gehen Sie an dem Platz vorbei.` | `D. Gehen Sie bis zum Platz.`
   * Dịch nghĩa câu: *"Ngài hãy đi băng qua quảng trường."*
   * Giải thích: Đi băng qua một bề mặt không gian (`Wohin?` — có sự di chuyển) dùng giới từ **`über + Akkusativ`**. Danh từ `der Platz` (giống đực) sang `Akkusativ` đổi thành **`über den Platz`**.
4. **Câu 4 (Nhìn Sơ đồ SVG `Hình c` & `Hình d` — Đi cho đến Đèn giao thông / Ngã tư)**:
   * `visual_svg`: Render **`direction_card_c_and_d`** *(Hình `c`: mũi tên dừng tại cột đèn giao thông `🚦 Ampel`; Hình `d`: mũi tên dừng tại ngã tư `➕ Kreuzung`)*.
   * `question`: Quan sát hai sơ đồ **`c)`** và **`d)`**: Vì cả `die Ampel` (đèn giao thông) và `die Kreuzung` (ngã tư) đều mang giống cái (`Femininum`), cụm giới từ *"đi cho đến..."* nào dưới đây là đúng?
   * Đáp án: `A. bis zu die Ampel / bis zu die Kreuzung` | `B. bis zum Ampel / bis zum Kreuzung` | `C. bis zur Ampel / bis zur Kreuzung` (Đúng) | `D. bis an die Ampel / bis in die Kreuzung`
   * Dịch nghĩa câu: *"Đi cho đến đèn giao thông / Đi cho đến ngã tư."*
   * Giải thích: Giới từ kép `bis zu` luôn đi với **Cách 3 (`Dativ`)**. Với danh từ giống cái (`die Ampel`, `die Kreuzung`), `zu + der` viết tắt thành **`zur`** $\rightarrow$ **`bis zur Ampel`** và **`bis zur Kreuzung`**.
5. **Câu 5 (Nhìn Sơ đồ SVG `Hình i` — Đi dọc theo con đường `... entlang`)**:
   * `visual_svg`: Render **`direction_card_i`** *(Con đường uốn lượn với mũi tên đi dọc suốt theo chiều dài con đường)*.
   * `question`: Quan sát **Sơ đồ `i)`**: Chọn câu đúng ngữ pháp để diễn tả *"Ngài hãy đi dọc theo con đường Friedrich (`die Friedrichstraße`)"*:
   * Đáp án: `A. Gehen Sie entlang der Friedrichstraße.` | `B. Gehen Sie die Friedrichstraße entlang.` (Đúng) | `C. Gehen Sie an der Friedrichstraße entlang vorbei.` | `D. Gehen Sie durch die Friedrichstraße entlang.`
   * Dịch nghĩa câu: *"Ngài hãy đi dọc theo đường Friedrich."*
   * Giải thích: Khi dùng từ **`entlang`** *(dọc theo)* đứng **SAU** danh từ, danh từ phía trước được chia ở **Cách 4 (`Akkusativ`)**: **`Gehen Sie die Friedrichstraße entlang.`**
6. **Câu 6 (Nhìn Sơ đồ SVG Đối chiếu `durch das Tor` vs. `über die Brücke`)**:
   * `visual_svg`: Render **`spatial_contrast_tor_bruecke`** *(Bên trái: mũi tên đi xuyên qua lòng cổng vòm `das Stadttor`; Bên phải: mũi tên đi vượt qua cây cầu `die Brücke`)*.
   * `question`: Quan sát 2 hình minh họa bên trên và chọn cặp giới từ + mạo từ điền đúng vào câu: *„Zuerst gehen die Touristen ___ Stadttor (`das Stadttor`), und danach laufen sie ___ Brücke (`die Brücke`).“*
   * Đáp án: `A. über das / durch die` | `B. durch das / über die` (Đúng) | `C. durch dem / über der` | `D. am / an der`
   * Dịch nghĩa câu: *"Đầu tiên các du khách đi xuyên qua cổng thành, và tiếp theo họ đi bộ qua cây cầu."*
   * Giải thích: Đi xuyên qua lòng cổng vòm dùng **`durch + Akkusativ`** (`durch das Stadttor`); đi vượt qua mặt cầu dùng **`über + Akkusativ`** (`über die Brücke`).
7. **Câu 7 (Nhìn Bản đồ Lưới Đường Phố SVG — Đọc lộ trình tìm Điểm Đích)**:
   * `visual_svg`: Render **`city_grid_map_quiz_1`** *(Bản đồ hiển thị vạch đường đi từ `📍 Start`: đi thẳng $\rightarrow$ rẽ phải ở đường thứ nhất $\rightarrow$ đi ngang qua `🏦 Bank` $\rightarrow$ rẽ trái ở ngã tư thứ hai $\rightarrow$ đi tới `🚦 Ampel` $\rightarrow$ nhìn sang bên phải là tòa nhà **`📮 Post`**, bên trái là **`🎬 Kino`**)*.
   * `question`: Hãy theo dõi lộ trình sau trên **Bản đồ thành phố** bên trên: *„Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel.“* — Tòa nhà nằm ở **bên tay phải (`rechts`)** của bạn tại điểm cuối là gì?
   * Đáp án: `A. das Kino` | `B. die Bank` | `C. die Post` (Đúng) | `D. der Bahnhof`
   * Dịch nghĩa câu: *"Đầu tiên Ngài đi thẳng. Sau đó rẽ phải ở đường thứ nhất, đi ngang qua ngân hàng. Sau đó đi đến ngã tư thứ hai rẽ trái. Tiếp theo đi đến đèn giao thông. Ở bên phải Ngài nhìn thấy bưu điện."*
   * Giải thích: Theo đúng hướng di chuyển từ dưới lên tới đèn giao thông (`Ampel`) trên bản đồ, phía bên tay phải (`rechts`) chính là **`die Post`** (Bưu điện).
8. **Câu 8 (Nhìn Bản đồ Lưới Đường Phố SVG — Lộ trình 2 đến Bưu điện)**:
   * `visual_svg`: Render **`city_grid_map_quiz_2`** *(Bản đồ hiển thị Lộ trình 2 màu xanh lá: Từ `📍 Start` đi thẳng qua ngã tư thứ 1, đến ngã tư thứ 2 thì rẽ phải, đi thẳng băng qua ngã tư tiếp theo, nhìn bên tay trái là `📮 Post`)*.
   * `question`: Quan sát **Lộ trình số 2 (màu xanh lá)** trên bản đồ bên trên và chọn từ đúng điền vào chỗ trống: *„Zuerst gehen Sie geradeaus, bis zur ___ Kreuzung rechts. Dann gehen Sie geradeaus, ___ die Kreuzung. Links sehen Sie die Post.“*
   * Đáp án: `A. ersten / durch` | `B. zweiten / über` (Đúng) | `C. zweiten / an` | `D. dritten / um`
   * Dịch nghĩa câu: *"Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ thấy bưu điện."*
   * Giải thích: Đường màu xanh lá đi thẳng tới ngã tư thứ hai (`bis zur zweiten Kreuzung rechts`), sau đó đi băng qua ngã tư tiếp theo (`über die Kreuzung`).
9. **Câu 9 (Giống & Dạng số nhiều của các địa điểm trong thành phố `In der Stadt`)**: Dòng nào dưới đây liệt kê **ĐÚNG 100%** cả mạo từ số ít và dạng số nhiều của các danh từ địa điểm?
   * Đáp án:
     * `A. der Bahnhof (die Bahnhofen) / das Schloss (die Schlosse) / das Einkaufszentrum (die Einkaufszentrums)`
     * `B. der Bahnhof (die Bahnhöfe) / das Schloss (die Schlösser) / das Einkaufszentrum (die Einkaufszentren)` (Đúng)
     * `C. das Bahnhof (die Bahnhöfe) / der Schloss (die Schlösser) / die Einkaufszentrum (die Einkaufszentren)`
     * `D. der Hafen (die Hafen) / der Markt (die Markte) / der Platz (die Platze)`
   * Dịch nghĩa câu: *"Nhà ga (các nhà ga) / Lâu đài (các lâu đài) / Trung tâm thương mại (các trung tâm thương mại)."*
   * Giải thích: `der Bahnhof` $\rightarrow$ `die Bahnhöfe` (thêm Umlaut + `-e`); `das Schloss` $\rightarrow$ `die Schlösser` (thêm Umlaut + `-er`); `das Einkaufszentrum` $\rightarrow$ `die Einkaufszentren` (đuôi `-um` đổi thành `-en`).
10. **Câu 10 (Phân biệt 2 nghĩa & 2 số nhiều của `die Bank` và đặc điểm của `die Post`)**: Phát biểu ngữ pháp nào dưới đây là **CHÍNH XÁC NHẤT**?
    * Đáp án:
      * `A. Danh từ "die Post" có dạng số nhiều thông dụng là "die Posten", còn "die Bank" không có số nhiều.`
      * `B. Danh từ "die Post" (bưu điện) chỉ dùng ở số ít (nur Singular), còn "die Bank" có số nhiều là "die Banken" (các ngân hàng) hoặc "die Bänke" (các ghế băng dài).` (Đúng)
      * `C. Cả "die Post" và "die Bank" đều mang giống trung (das).`
      * `D. Danh từ "der Flughafen" mang giống trung vì chỉ địa điểm lớn.`
    * Dịch nghĩa câu: *"Danh từ die Post chỉ dùng ở số ít, còn die Bank có 2 dạng số nhiều tùy theo nghĩa."*
    * Giải thích: `die Post` (bưu điện) là danh từ chỉ dùng ở số ít (`nur Singular`). `die Bank` khi mang nghĩa *ngân hàng* có số nhiều là `die Banken`, còn khi mang nghĩa *ghế băng dài* có số nhiều là `die Bänke`.
11. **Câu 11 (Giống của các Danh lam thắng cảnh tại Berlin `Sehenswürdigkeiten in Berlin`)**: Nhóm danh lam thắng cảnh Berlin nào dưới đây có **cả 3 địa danh đều mang GIỐNG TRUNG (`das`)**?
    * Đáp án:
      * `A. der Reichstag, der Berliner Dom, der Fernsehturm`
      * `B. die Humboldt-Universität, die Staatsoper, die Museumsinsel`
      * `C. das Bundeskanzleramt, das Brandenburger Tor, das Schloss Bellevue` (Đúng)
      * `D. das Alexanderplatz, das Friedrichstraße, das Sony Center`
    * Dịch nghĩa câu: *"Phủ Thủ tướng, Cổng Brandenburg, Cung điện Bellevue."*
    * Giải thích: Cả 3 địa danh này đều có danh từ gốc ở cuối mang giống trung: `das Amt` $\rightarrow$ **`das Bundeskanzleramt`**, `das Tor` $\rightarrow$ **`das Brandenburger Tor`**, `das Schloss` $\rightarrow$ **`das Schloss Bellevue`** (cùng với **`das Sony Center`**).
12. **Câu 12 (Giống Đực `der` và Giống Cái `die` của các địa danh Berlin)**: Chọn cặp mạo từ đúng cho 2 địa danh nổi tiếng ở Berlin: *„1. ___ Fernsehturm steht am Alexanderplatz. — 2. ___ Museumsinsel liegt im Zentrum von Berlin.“*
    * Đáp án: `A. Das / Die` | `B. Der / Die` (Đúng) | `C. Der / Das` | `D. Die / Der`
    * Dịch nghĩa câu: *"1. Tháp truyền hình nằm ở quảng trường Alexander. — 2. Đảo Bảo tàng nằm ở trung tâm Berlin."*
    * Giải thích: `der Turm` (ngọn tháp) $\rightarrow$ **`der Fernsehturm`** (giống đực); `die Insel` (hòn đảo) $\rightarrow$ **`die Museumsinsel`** (giống cái).
13. **Câu 13 (Phân biệt `zum` [`zu + Dativ`] vs. `in den` [`in + Akkusativ`] trong đoạn văn Berlin)**: Chọn phương án đúng điền vào câu: *„Paula und Alex gehen zuerst ___ Brandenburger Tor (`das Tor`) und machen Fotos. Am Nachmittag gehen sie ___ Berliner Dom (`der Dom`) und hören ein Konzert.“*
    * Đáp án: `A. ins / zum` | `B. zum / in den` (Đúng) | `C. in das / im` | `D. zur / in der`
    * Dịch nghĩa câu: *"Paula và Alex đầu tiên đi đến Cổng Brandenburg và chụp ảnh. Buổi chiều họ đi vào trong Nhà thờ lớn Berlin và nghe một buổi hòa nhạc."*
    * Giải thích: Đi tới khu vực Cổng Brandenburg để chụp ảnh bên ngoài dùng `zu + dem` = **`zum Brandenburger Tor`**. Đi hẳn vào bên trong Nhà thờ lớn Berlin (`der Dom`) để nghe hòa nhạc dùng `in + Akkusativ` = **`in den Berliner Dom`**.
14. **Câu 14 (Phối hợp `am ... vorbei` và `über die ...` khi tham quan Berlin)**: Chọn cặp từ đúng hoàn thành câu: *„Die Touristen fahren mit dem Bus ___ Bundeskanzleramt (`das Amt`) vorbei und laufen dann ___ Schlossbrücke (`die Brücke`).“*
    * Đáp án: `A. ans / über der` | `B. am / über die` (Đúng) | `C. durch das / an der` | `D. beim / durch die`
    * Dịch nghĩa câu: *"Các du khách đi xe buýt ngang qua Phủ Thủ tướng và sau đó đi bộ qua cầu Schlossbrücke."*
    * Giải thích: Đi ngang qua `das Bundeskanzleramt` dùng `an + dem ... vorbei` = **`am Bundeskanzleramt vorbei`**. Đi bộ qua cầu `die Schlossbrücke` (`Wohin? + Akkusativ`) dùng **`über die Schlossbrücke`**.
15. **Câu 15 (Chia động từ khuyết thiếu `wollen` ở ngôi `ich` và `wir`)**: Chọn cặp dạng chia đúng của động từ `wollen`: *„Wir ___ heute eine Stadtrundfahrt in Berlin machen, und danach ___ ich in die Alte Nationalgalerie gehen.“*
    * Đáp án: `A. wollt / will` | `B. wollen / will` (Đúng) | `C. wollen / wolle` | `D. will / wollen`
    * Dịch nghĩa câu: *"Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố Berlin, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia Cũ."*
    * Giải thích: Với động từ khuyết thiếu `wollen`, ngôi `wir` chia là **`wollen`**, còn ngôi `ich` (và `er/sie/es`) biến đổi nguyên âm `o -> i` và không có đuôi thành **`will`**.
16. **Câu 16 (Chia động từ khuyết thiếu `wollen` với chủ ngữ ghép `Maria und ich` và ngôi `ihr`)**: Chọn phương án đúng: *„Was ___ ihr heute Nachmittag machen? — Maria und ich ___ auf der Friedrichstraße bummeln.“*
    * Đáp án: `A. wollt / wollen` (Đúng) | `B. willst / wollen` | `C. wollen / wollt` | `D. wollt / will`
    * Dịch nghĩa câu: *"Chiều nay các bạn muốn làm gì? — Maria và tôi muốn đi dạo phố trên đường Friedrich."*
    * Giải thích: Ngôi `ihr` (các bạn) chia là **`wollt`**. Chủ ngữ ghép `Maria und ich` tương đương với ngôi `wir` (chúng tôi) nên chia là **`wollen`**.
17. **Câu 17 (Đối chiếu sắc thái & cách chia của 4 động từ khuyết thiếu `möchten, können, müssen, wollen`)**: Chọn câu có cách chia động từ khuyết thiếu **ĐÚNG NGỮ PHÁP 100%**:
    * Đáp án:
      * `A. Mein Bruder willt nächstes Jahr in Deutschland studieren.`
      * `B. Am Wochenende musst meine Schwester im Krankenhaus arbeiten.`
      * `C. Lukas kann sehr gut kochen und will in Berlin ein Restaurant aufmachen.` (Đúng)
      * `D. Wir möchten heute Abend einen Film im Kino seht.`
    * Dịch nghĩa câu: *"Lukas có thể nấu ăn rất giỏi và muốn mở một nhà hàng ở Berlin."*
    * Giải thích: Ở ngôi thứ 3 số ít (`Lukas` = `er`), động từ `können` chia là **`kann`** và `wollen` chia là **`will`** (tuyệt đối không thêm `-t`), động từ chính `kochen` và `aufmachen` đứng nguyên mẫu ở cuối câu.
18. **Câu 18 (Hỏi đường với `Wie komme ich ...?` và `Wo geht es ...?`)**: Một du khách đứng ở nhà ga và muốn hỏi đường đi đến Nhà hát Opera Quốc gia (`die Staatsoper`). Câu hỏi nào dưới đây là **ĐÚNG NGỮ PHÁP**?
    * Đáp án:
      * `A. Entschuldigung, wie komme ich zum Staatsoper?`
      * `B. Entschuldigung, wie komme ich zur Staatsoper?` (Đúng)
      * `C. Entschuldigung, wo geht es in der Staatsoper?`
      * `D. Entschuldigung, ich suche der Staatsoper.`
    * Dịch nghĩa câu: *"Xin lỗi, làm thế nào tôi đi đến được Nhà hát Opera Quốc gia?"*
    * Giải thích: Danh từ `die Staatsoper` mang giống cái (`Femininum`), nên khi đi với giới từ `zu + Dativ` phải dùng `zu + der` = **`zur Staatsoper`** (hoặc nếu dùng `in + Akkusativ` thì là `in die Staatsoper`).

---

#### NHÓM 2: ĐIỀN KHUYẾT KÈM SƠ ĐỒ & BẢN ĐỒ SVG (`dien_khuyet` — 15 Câu: Câu 19 $\rightarrow$ Câu 33)
19. **Câu 19 (Nhìn Sơ đồ SVG `Hình a`)**:
    * `visual_svg`: Render **`direction_card_a`** *(Mũi tên đi thẳng)*.
    * Điền từ chỉ hướng thích hợp vào chỗ trống: *„Gehen Sie zuerst 200 Meter ___!“* *(Ngài hãy đi thẳng 200 mét trước tiên!)*
    * Đáp án chấp nhận: `["geradeaus"]`
    * Giải thích: *"Đi thẳng về phía trước"* trong tiếng Đức là **`geradeaus`**.
20. **Câu 20 (Nhìn Sơ đồ SVG `Hình g` & `Hình h`)**:
    * `visual_svg`: Render **`direction_card_h`** *(Mũi tên rẽ sang bên phải)*.
    * Điền từ chỉ hướng thích hợp vào chỗ trống: *„An der Ampel gehen Sie bitte hier ___, nicht links!“* *(Tại đèn giao thông xin Ngài hãy rẽ phải ở đây, đừng rẽ trái!)*
    * Đáp án chấp nhận: `["rechts"]`
    * Giải thích: Đối lập với `links` (bên trái) là **`rechts`** (bên phải).
21. **Câu 21 (Nhìn Sơ đồ SVG `an ... vorbei`)**:
    * `visual_svg`: Render **`spatial_diagram_vorbei`** *(Mũi tên đi ngang qua tòa nhà `Universität`)*.
    * Điền từ còn thiếu để hoàn thành cấu trúc *"đi ngang qua"*: *„Gehen Sie an der Humboldt-Universität ___ und dann die erste Straße links.“*
    * Đáp án chấp nhận: `["vorbei"]`
    * Giải thích: Cấu trúc *"đi ngang qua địa điểm nào"* là **`an + Dativ + vorbei`**.
22. **Câu 22**: Điền giới từ thu gọn (`an + dem`) thích hợp vào chỗ trống: *„Der Sightseeing-Bus fährt ___ Bundeskanzleramt und ___ Reichstag vorbei.“* *(Gợi ý: `das Bundeskanzleramt`, `der Reichstag`)*
    * Đáp án chấp nhận: `["am"]`
    * Dịch nghĩa câu: *"Chiếc xe buýt tham quan chạy ngang qua Phủ Thủ tướng và tòa nhà Quốc hội."*
    * Giải thích: Cả `das Bundeskanzleramt` (giống trung) và `der Reichstag` (giống đực) khi đi với `an + Dativ + vorbei` đều gộp `an + dem` thành **`am`**.
23. **Câu 23 (Nhìn Sơ đồ SVG `durch das Tor`)**:
    * `visual_svg`: Render **`direction_card_k`** *(Mũi tên đi xuyên qua lòng cổng vòm `Tor`)*.
    * Điền giới từ chỉ sự xuyên qua (`+ Akkusativ`) vào chỗ trống: *„Die Besucher gehen ___ das Brandenburger Tor.“*
    * Đáp án chấp nhận: `["durch", "durchs"]`
    * Dịch nghĩa câu: *"Những người khách tham quan đi xuyên qua Cổng Brandenburg."*
    * Giải thích: Đi xuyên qua lòng cánh cổng dùng giới từ **`durch`** + Cách 4 (`Akkusativ`).
24. **Câu 24 (Nhìn Sơ đồ SVG `über die Brücke`)**:
    * `visual_svg`: Render **`direction_card_l`** *(Mũi tên đi qua cây cầu `Brücke`)*.
    * Điền giới từ chỉ hành động đi vượt qua mặt cầu vào chỗ trống: *„Paula und Alex laufen ___ die Schlossbrücke.“*
    * Đáp án chấp nhận: `["über", "ueber"]`
    * Dịch nghĩa câu: *"Paula và Alex đi bộ qua cầu Schlossbrücke."*
    * Giải thích: Đi qua cầu, qua đường, qua quảng trường dùng **`über + Akkusativ`**.
25. **Câu 25**: Điền hậu tố giới từ chỉ đường *"dọc theo"* đứng sau danh từ ở `Akkusativ`: *„Gehen Sie bitte den Fluss Spree ___ bis zur Museumsinsel!“*
    * Đáp án chấp nhận: `["entlang"]`
    * Dịch nghĩa câu: *"Xin Ngài hãy đi dọc theo sông Spree cho đến Đảo Bảo tàng!"*
    * Giải thích: Cấu trúc `[Danh từ ở Akkusativ] + entlang` có nghĩa là đi dọc theo (`den Fluss entlang`, `die Straße entlang`).
26. **Câu 26**: Điền cụm từ thu gọn (`zu + der`) vào chỗ trống: *„Gehen Sie immer geradeaus bis ___ zweiten Kreuzung!“* *(Gợi ý: `die Kreuzung`)*
    * Đáp án chấp nhận: `["zur"]`
    * Dịch nghĩa câu: *"Ngài cứ đi thẳng mãi cho đến ngã tư thứ hai!"*
    * Giải thích: `bis zu` luôn đi với Cách 3 (`Dativ`). `die Kreuzung` mang giống cái nên `zu + der` viết tắt là **`zur`** (`bis zur zweiten Kreuzung`).
27. **Câu 27**: Điền dạng chia đúng của động từ khuyết thiếu `wollen` vào chỗ trống: *„In den Sommerferien ___ mein Sohn allein nach Berlin reisen.“*
    * Đáp án chấp nhận: `["will"]`
    * Dịch nghĩa câu: *"Trong kỳ nghỉ hè, con trai tôi muốn đi du lịch một mình đến Berlin."*
    * Giải thích: Chủ ngữ `mein Sohn` là ngôi thứ 3 số ít (`er`), động từ `wollen` chia thành **`will`**.
28. **Câu 28**: Điền dạng chia đúng của động từ khuyết thiếu `wollen` vào chỗ trống: *„Wohin ___ du heute Abend mit deinen Freunden gehen, Sofia?“*
    * Đáp án chấp nhận: `["willst"]`
    * Dịch nghĩa câu: *"Tối nay bạn muốn đi đâu cùng với những người bạn của mình thế, Sofia?"*
    * Giải thích: Ngôi thứ 2 số ít (`du`) của động từ `wollen` là **`willst`**.
29. **Câu 29**: Điền dạng chia đúng của động từ khuyết thiếu `wollen` vào chỗ trống: *„Heute Abend ___ wir noch einen spannenden Film im Kino sehen.“*
    * Đáp án chấp nhận: `["wollen"]`
    * Dịch nghĩa câu: *"Tối nay chúng tôi còn muốn xem một bộ phim hấp dẫn ở trong rạp chiếu phim."*
    * Giải thích: Ngôi thứ nhất số nhiều (`wir`) của động từ `wollen` giữ nguyên là **`wollen`**.
30. **Câu 30**: Điền cụm giới từ + mạo từ (`in + den`) thích hợp vào chỗ trống: *„Am Nachmittag gehen die Touristen ___ Berliner Dom und hören ein Orgelkonzert.“* *(Gợi ý: `der Berliner Dom`)*
    * Đáp án chấp nhận: `["in den"]`
    * Dịch nghĩa câu: *"Vào buổi chiều các du khách đi vào trong Nhà thờ lớn Berlin và nghe một buổi hòa nhạc đàn đại phong cầm."*
    * Giải thích: Đi vào bên trong tòa nhà (`Wohin? + Akkusativ`) với danh từ giống đực `der Berliner Dom` dùng **`in den`**.
31. **Câu 31**: Điền cụm giới từ + mạo từ (`in + die`) thích hợp vào chỗ trống: *„Nach dem Abendessen gehen Paula und Alex ___ Disko ‚Von Euch‘.“* *(Gợi ý: `die Disko`)*
    * Đáp án chấp nhận: `["in die"]`
    * Dịch nghĩa câu: *"Sau bữa tối, Paula và Alex đi vào vũ trường 'Von Euch'."*
    * Giải thích: `die Disko` mang giống cái, đi vào trong vũ trường (`Wohin? + Akkusativ`) dùng **`in die Disko`**.
32. **Câu 32**: Điền giới từ thu gọn (`zu + dem`) thích hợp vào chỗ trống: *„Entschuldigung, wie komme ich am schnellsten ___ Hauptbahnhof?“* *(Gợi ý: `der Hauptbahnhof`)*
    * Đáp án chấp nhận: `["zum"]`
    * Dịch nghĩa câu: *"Xin lỗi, làm thế nào tôi đi đến được nhà ga trung tâm nhanh nhất?"*
    * Giải thích: `der Hauptbahnhof` mang giống đực, đi sau `zu + Dativ` gộp `zu + dem` thành **`zum Hauptbahnhof`**.
33. **Câu 33**: Điền dạng số nhiều đúng của danh từ `das Schloss` (lâu đài, cung điện) vào chỗ trống: *„In Deutschland und Österreich gibt es viele alte ___.“*
    * Đáp án chấp nhận: `["Schlösser", "Schloesser"]`
    * Dịch nghĩa câu: *"Ở Đức và Áo có rất nhiều lâu đài cổ."*
    * Giải thích: Danh từ giống trung `das Schloss` khi chuyển sang số nhiều phải thêm Umlaut `o -> ö` và đuôi `-er` thành **`die Schlösser`**.

---

#### NHÓM 3: DỊCH NGHĨA TỪ / CỤM TỪ VIỆT $\rightarrow$ ĐỨC (`dich_nghia_vd` — 12 Câu: Câu 34 $\rightarrow$ Câu 45)
34. **Câu 34**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"cảng biển"***
    * Đáp án chấp nhận: `["der Hafen", "Hafen"]`
    * Giải thích: Cảng biển là danh từ giống đực **`der Hafen`** (số nhiều: `die Häfen`).
35. **Câu 35**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"cây cầu"***
    * Đáp án chấp nhận: `["die Brücke", "Brücke", "die Bruecke"]`
    * Giải thích: Cây cầu là danh từ giống cái **`die Brücke`** (số nhiều: `die Brücken`).
36. **Câu 36**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"lâu đài / cung điện"***
    * Đáp án chấp nhận: `["das Schloss", "Schloss"]`
    * Giải thích: Lâu đài / cung điện là danh từ giống trung **`das Schloss`** (số nhiều: `die Schlösser`).
37. **Câu 37**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"trung tâm thương mại"***
    * Đáp án chấp nhận: `["das Einkaufszentrum", "Einkaufszentrum"]`
    * Giải thích: Trung tâm thương mại là danh từ giống trung **`das Einkaufszentrum`** (số nhiều: `die Einkaufszentren`).
38. **Câu 38**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"cổng thành"***
    * Đáp án chấp nhận: `["das Stadttor", "Stadttor"]`
    * Giải thích: Cổng thành là danh từ ghép giống trung **`das Stadttor`** (số nhiều: `die Stadttore`).
39. **Câu 39**: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): ***"Tòa nhà Quốc hội Đức"***
    * Đáp án chấp nhận: `["der Reichstag", "Reichstag"]`
    * Giải thích: Tòa nhà Quốc hội ở Berlin là **`der Reichstag`**.
40. **Câu 40**: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): ***"Phủ Thủ tướng Đức"***
    * Đáp án chấp nhận: `["das Bundeskanzleramt", "Bundeskanzleramt"]`
    * Giải thích: Phủ Thủ tướng Liên bang Đức là danh từ giống trung **`das Bundeskanzleramt`**.
41. **Câu 41**: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): ***"Đảo Bảo tàng"***
    * Đáp án chấp nhận: `["die Museumsinsel", "Museumsinsel"]`
    * Giải thích: Đảo Bảo tàng ở Berlin là danh từ giống cái **`die Museumsinsel`**.
42. **Câu 42**: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): ***"Tháp truyền hình"***
    * Đáp án chấp nhận: `["der Fernsehturm", "Fernsehturm"]`
    * Giải thích: Tháp truyền hình là danh từ giống đực **`der Fernsehturm`**.
43. **Câu 43**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi cho đến đèn giao thông"***
    * Đáp án chấp nhận: `["bis zur Ampel gehen", "bis zur Ampel", "Gehen Sie bis zur Ampel"]`
    * Giải thích: Đèn giao thông là `die Ampel` $\rightarrow$ *"cho đến đèn giao thông"* là **`bis zur Ampel`**.
44. **Câu 44**: Dịch cụm chỉ đường sau sang tiếng Đức: ***"đi ngang qua ngân hàng"***
    * Đáp án chấp nhận: `["an der Bank vorbei", "an der Bank vorbeigehen", "Gehen Sie an der Bank vorbei"]`
    * Giải thích: Ngân hàng là `die Bank` $\rightarrow$ cấu trúc `an + Dativ + vorbei` là **`an der Bank vorbei`**.
45. **Câu 45**: Dịch cụm từ chỉ hoạt động du lịch sau sang tiếng Đức: ***"thực hiện một chuyến tham quan vòng quanh thành phố"***
    * Đáp án chấp nhận: `["eine Stadtrundfahrt machen", "Stadtrundfahrt machen"]`
    * Giải thích: Chuyến tham quan vòng quanh thành phố (bằng xe buýt/tàu) là `die Stadtrundfahrt` $\rightarrow$ **`eine Stadtrundfahrt machen`**.

---

#### NHÓM 4: DỊCH NGHĨA TỪ / CỤM TỪ ĐỨC $\rightarrow$ VIỆT (`dich_nghia_dv` — 12 Câu: Câu 46 $\rightarrow$ Câu 57)
46. **Câu 46**: Dịch sang tiếng Việt: ***„die Staatsoper“***
    * Đáp án chấp nhận: `["nhà hát Opera quốc gia", "nhà hát nhạc kịch quốc gia", "nhà hát opera nhà nước"]`
    * Giải thích: `die Staatsoper` là Nhà hát Opera Quốc gia tại Berlin.
47. **Câu 47**: Dịch sang tiếng Việt: ***„der Berliner Dom“***
    * Đáp án chấp nhận: `["nhà thờ lớn Berlin", "nhà thờ chính tòa Berlin", "thánh đường Berlin"]`
    * Giải thích: `der Berliner Dom` là Nhà thờ lớn Berlin.
48. **Câu 48**: Dịch sang tiếng Việt: ***„die Alte Nationalgalerie“***
    * Đáp án chấp nhận: `["khu triển lãm quốc gia cũ", "khu trưng bày nghệ thuật quốc gia", "phòng triển lãm quốc gia cổ", "khu triển lãm quốc gia"]`
    * Giải thích: `die Alte Nationalgalerie` là Khu triển lãm Quốc gia (Cũ) nằm trên Đảo Bảo tàng ở Berlin.
49. **Câu 49**: Dịch sang tiếng Việt: ***„das Schloss Bellevue“***
    * Đáp án chấp nhận: `["cung điện Bellevue", "lâu đài Bellevue"]`
    * Giải thích: `das Schloss Bellevue` là Cung điện Bellevue (nơi làm việc chính thức của Tổng thống Đức ở Berlin).
50. **Câu 50**: Dịch sang tiếng Việt: ***„Gehen Sie die erste Straße rechts!“***
    * Đáp án chấp nhận: `["Ngài hãy rẽ phải ở con đường thứ nhất", "Hãy đi con đường đầu tiên bên phải", "Rẽ phải ở đường đầu tiên", "Ngài hãy đi đường thứ nhất bên tay phải"]`
    * Giải thích: `die erste Straße rechts` = rẽ phải ở con đường thứ nhất / đầu tiên.
51. **Câu 51**: Dịch sang tiếng Việt: ***„Gehen Sie bis zur zweiten Kreuzung links!“***
    * Đáp án chấp nhận: `["Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái", "Hãy đi tới ngã tư thứ hai bên trái", "Đi đến ngã tư thứ hai rồi rẽ trái"]`
    * Giải thích: `bis zur zweiten Kreuzung links` = đi đến ngã tư thứ hai rồi rẽ trái.
52. **Câu 52**: Dịch sang tiếng Việt: ***„Gehen Sie über den Platz und durch das Stadttor!“***
    * Đáp án chấp nhận: `["Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành", "Hãy đi qua quảng trường và đi xuyên qua cổng thành"]`
    * Giải thích: `über den Platz` = băng qua quảng trường; `durch das Stadttor` = xuyên qua cổng thành.
53. **Câu 53**: Dịch sang tiếng Việt: ***„auf der Friedrichstraße bummeln“***
    * Đáp án chấp nhận: `["đi dạo phố trên đường Friedrich", "dạo chơi mua sắm trên phố Friedrich", "tản bộ trên đường Friedrich"]`
    * Giải thích: Động từ `bummeln` có nghĩa là đi dạo phố, tản bộ ngắm cảnh/cửa hàng.
54. **Câu 54**: Dịch sang tiếng Việt: ***„Entschuldigung, wie komme ich ins Kino?“***
    * Đáp án chấp nhận: `["Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?", "Xin lỗi, tôi đi tới rạp chiếu phim bằng cách nào?", "Xin lỗi, đi đến rạp chiếu phim như thế nào?"]`
    * Giải thích: `Wie komme ich ins Kino?` là câu hỏi đường lịch sự để đi tới rạp chiếu phim.
55. **Câu 55**: Dịch sang tiếng Việt: ***„Zuerst — Dann — Danach — Anschließend“***
    * Đáp án chấp nhận: `["Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó", "Trước tiên, sau đó, tiếp theo, tiếp nối sau đó", "Đầu tiên, sau đó, tiếp đó, sau cùng"]`
    * Giải thích: Bộ 4 trạng từ liên kết trình tự hành động khi chỉ đường và kể lịch trình.
56. **Câu 56**: Dịch sang tiếng Việt: ***„mit dem Bus am Bundeskanzleramt vorbeifahren“***
    * Đáp án chấp nhận: `["đi xe buýt ngang qua Phủ Thủ tướng", "chạy xe buýt ngang qua Phủ Thủ tướng"]`
    * Giải thích: `mit dem Bus` = bằng xe buýt; `am Bundeskanzleramt vorbeifahren` = đi/chạy xe ngang qua Phủ Thủ tướng.
57. **Câu 57**: Dịch sang tiếng Việt: ***„die Straße entlanggehen“***
    * Đáp án chấp nhận: `["đi bộ dọc theo con đường", "đi dọc theo con đường", "đi dọc phố"]`
    * Giải thích: `die Straße entlanggehen` = đi bộ dọc theo chiều dài con đường.

---

#### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 10 Bài: Câu 58 $\rightarrow$ Câu 67, mỗi bài 4 cặp độc nhất)
58. **Câu 58 (Bài nối ô 1 — Nối Biểu tượng Sơ đồ Chỉ đường với Câu lệnh tiếng Đức - Phần 1)**:
    * `[Hình a: Mũi tên đi thẳng ↑]` $\longleftrightarrow$ `Gehen Sie geradeaus.`
    * `[Hình h: Mũi tên quẹo phải ngay tại đây ↱]` $\longleftrightarrow$ `Gehen Sie hier rechts.`
    * `[Hình g: Mũi tên quẹo trái ngay tại đây ↰]` $\longleftrightarrow$ `Gehen Sie hier links.`
    * `[Hình i: Mũi tên chạy dọc theo đường uốn lượn 〰️]` $\longleftrightarrow$ `Gehen Sie die Straße entlang.`
59. **Câu 59 (Bài nối ô 2 — Nối Biểu tượng Sơ đồ Chỉ đường với Câu lệnh tiếng Đức - Phần 2)**:
    * `[Hình c: Mũi tên đi tới đèn giao thông 🚦 dừng lại]` $\longleftrightarrow$ `Gehen Sie bis zur Ampel.`
    * `[Hình d: Mũi tên đi tới ngã tư ➕ dừng lại]` $\longleftrightarrow$ `Gehen Sie bis zur Kreuzung.`
    * `[Hình b: Mũi tên đi lướt ngang qua mặt nhà thờ ⛪]` $\longleftrightarrow$ `Gehen Sie an der Kirche vorbei.`
    * `[Hình f: Mũi tên đi băng xuyên qua quảng trường tròn ⭕]` $\longleftrightarrow$ `Gehen Sie über den Platz.`
60. **Câu 60 (Bài nối ô 3 — Nối Danh từ Địa điểm Thành phố với Dạng Số Nhiều chuẩn)**:
    * `der Bahnhof & der Flughafen` $\longleftrightarrow$ `die Bahnhöfe & die Flughäfen (thêm Umlaut)`
    * `das Schloss & das Krankenhaus` $\longleftrightarrow$ `die Schlösser & die Krankenhäuser (thêm Umlaut + -er)`
    * `das Einkaufszentrum & das Museum` $\longleftrightarrow$ `die Einkaufszentren & die Museen (đổi đuôi sang -en)`
    * `die Post (bưu điện)` $\longleftrightarrow$ `nur Singular (chỉ dùng ở dạng số ít)`
61. **Câu 61 (Bài nối ô 4 — Nối Danh lam Thắng cảnh Berlin với Mạo từ & Nghĩa - Phần 1)**:
    * `der Reichstag & der Fernsehturm` $\longleftrightarrow$ `Giống đực (der): Tòa nhà Quốc hội & Tháp truyền hình`
    * `der Berliner Dom & der Alexanderplatz` $\longleftrightarrow$ `Giống đực (der): Nhà thờ lớn Berlin & Quảng trường Alexander`
    * `die Humboldt-Universität & die Staatsoper` $\longleftrightarrow$ `Giống cái (die): Đại học Humboldt & Nhà hát Opera Quốc gia`
    * `die Museumsinsel & die Friedrichstraße` $\longleftrightarrow$ `Giống cái (die): Đảo Bảo tàng & Phố Friedrich`
62. **Câu 62 (Bài nối ô 5 — Nối Danh lam Thắng cảnh Berlin với Mạo từ & Nghĩa - Phần 2)**:
    * `das Brandenburger Tor` $\longleftrightarrow$ `Giống trung (das): Cổng thành Brandenburg`
    * `das Bundeskanzleramt` $\longleftrightarrow$ `Giống trung (das): Phủ Thủ tướng Liên bang`
    * `das Schloss Bellevue` $\longleftrightarrow$ `Giống trung (das): Cung điện Bellevue`
    * `die Alte Nationalgalerie` $\longleftrightarrow$ `Giống cái (die): Khu triển lãm Quốc gia Cũ`
63. **Câu 63 (Bài nối ô 6 — Nối 4 Mẫu Câu Hỏi Đường với Cấu trúc Ngữ pháp đi kèm)**:
    * `Entschuldigung, ich suche ...` $\longleftrightarrow$ `+ Cách 4 (Akkusativ): den Bahnhof / das Kino`
    * `Entschuldigung, wo ist ...?` $\longleftrightarrow$ `+ Cách 1 (Nominativ): der Bahnhof / das Kino`
    * `Entschuldigung, wie komme ich ...?` $\longleftrightarrow$ `+ zum Bahnhof / zur Post / ins Kino`
    * `Entschuldigung, wo geht es ...?` $\longleftrightarrow$ `+ zum Reichstag / zur Museumsinsel / ins Zentrum`
64. **Câu 64 (Bài nối ô 7 — Nối 4 Cấu trúc Giới từ Không gian với Cách Ngữ pháp)**:
    * `an ... vorbei (đi ngang qua bên cạnh)` $\longleftrightarrow$ `luôn đi với Cách 3 (Dativ): an der Bank vorbei / am Dom vorbei`
    * `durch ... (đi xuyên qua lòng cổng/công viên)` $\longleftrightarrow$ `luôn đi với Cách 4 (Akkusativ): durch das Tor / durch den Park`
    * `über ... (đi băng qua mặt cầu/quảng trường)` $\longleftrightarrow$ `đi với Cách 4 (Akkusativ): über die Brücke / über den Platz`
    * `... entlang (đi dọc theo đường/sông)` $\longleftrightarrow$ `đứng SAU danh từ ở Cách 4 (Akkusativ): die Straße entlang`
65. **Câu 65 (Bài nối ô 8 — Nối Chủ ngữ với Dạng chia của 4 Động từ Khuyết thiếu)**:
    * `ich / er / sie / es (với wollen)` $\longleftrightarrow$ `will (đổi nguyên âm o -> i, không có đuôi)`
    * `du (với wollen & müssen)` $\longleftrightarrow$ `willst / musst (thêm đuôi -st)`
    * `wir / sie / Sie (với wollen & möchten)` $\longleftrightarrow$ `wollen / möchten (nguyên mẫu đuôi -en)`
    * `ihr (với wollen & können)` $\longleftrightarrow$ `wollt / könnt (thêm đuôi -t)`
66. **Câu 66 (Bài nối ô 9 — Nối Các Chặng Tham Quan Berlin của Paula & Alex)**:
    * `1. Sie gehen zum Brandenburger Tor` $\longleftrightarrow$ `und machen dort viele Fotos.`
    * `2. Sie fahren mit dem Bus am Bundeskanzleramt vorbei` $\longleftrightarrow$ `und laufen über die Schlossbrücke.`
    * `3. Am Nachmittag gehen sie in den Berliner Dom` $\longleftrightarrow$ `und hören ein Konzert.`
    * `4. Am Abend essen sie Pizza` $\longleftrightarrow$ `und gehen danach in die Disko „Von Euch“.`
67. **Câu 67 (Bài nối ô 10 — Sắp xếp 4 Bước Chỉ Đường Từ Điểm Xuất Phát Tới Bưu Điện)**:
    * `Bước 1 (Zuerst)` $\longleftrightarrow$ `gehen Sie geradeaus.`
    * `Bước 2 (Dann)` $\longleftrightarrow$ `gehen Sie die erste Straße rechts, an der Bank vorbei.`
    * `Bước 3 (Danach)` $\longleftrightarrow$ `gehen Sie bis zur zweiten Kreuzung links und bis zur Ampel.`
    * `Bước 4 (Am Ziel)` $\longleftrightarrow$ `Rechts sehen Sie die Post.`

---

#### NHÓM 6: ĐIỀN VÀO CHỖ TRỐNG ĐỂ TẠO THÀNH CÂU KÈM BẢN ĐỒ SVG (`dien_tao_cau` — 10 Câu: Câu 68 $\rightarrow$ Câu 77)
68. **Câu 68 (Kèm Sơ đồ Bản đồ Lộ trình 1)**: Điền 2 từ còn thiếu để hoàn thành câu chỉ đường: *„Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.“*
    * Khung câu hiển thị: `Dann gehen Sie die erste Straße [1], an der Bank [2].`
    * Đáp án từng ô: Ô 1 = `["rechts"]`, Ô 2 = `["vorbei"]`.
    * Giải thích: Rẽ phải là `rechts`; đi ngang qua ngân hàng là `an der Bank vorbei`.
69. **Câu 69 (Kèm Sơ đồ Bản đồ Lộ trình 2)**: Điền 2 từ còn thiếu để hoàn thành câu chỉ đường: *„Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai bên phải, sau đó đi băng qua ngã tư.“*
    * Khung câu hiển thị: `Zuerst gehen Sie geradeaus, bis [1] zweiten Kreuzung rechts. Dann gehen Sie [2] die Kreuzung.`
    * Đáp án từng ô: Ô 1 = `["zur"]`, Ô 2 = `["über", "ueber"]`.
    * Giải thích: *"Cho đến ngã tư thứ hai"* là `bis zur zweiten Kreuzung`; *"băng qua ngã tư"* là `über die Kreuzung`.
70. **Câu 70**: Điền 2 từ còn thiếu để hoàn thành câu: *„Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.“*
    * Khung câu hiển thị: `Sie fahren mit dem Bus [1] Bundeskanzleramt vorbei und laufen [2] die Schlossbrücke.`
    * Đáp án từng ô: Ô 1 = `["am"]`, Ô 2 = `["über", "ueber"]`.
    * Giải thích: `das Bundeskanzleramt` đi với `an + Dativ + vorbei` là `am Bundeskanzleramt vorbei`; đi bộ qua cầu `die Schlossbrücke` là `über die Schlossbrücke`.
71. **Câu 71**: Điền 2 từ còn thiếu để hoàn thành câu: *„Đầu tiên các bạn hãy đi xuyên qua Cổng Brandenburg rồi đi dọc theo con đường.“*
    * Khung câu hiển thị: `Geht zuerst [1] das Brandenburger Tor und dann die Straße [2]!`
    * Đáp án từng ô: Ô 1 = `["durch"]`, Ô 2 = `["entlang"]`.
    * Giải thích: Đi xuyên qua cổng là `durch das Brandenburger Tor`; đi dọc theo con đường là `die Straße entlang`.
72. **Câu 72**: Điền 2 dạng chia đúng của động từ `wollen` để hoàn thành đoạn tin nhắn: *„Chúng mình còn muốn làm một chuyến tham quan thành phố, và sau đó mình muốn đi vào Khu triển lãm Quốc gia.“*
    * Khung câu hiển thị: `Wir [1] noch eine Stadtrundfahrt machen, und danach [2] ich in die Nationalgalerie gehen.`
    * Đáp án từng ô: Ô 1 = `["wollen"]`, Ô 2 = `["will"]`.
    * Giải thích: Ngôi `wir` chia là `wollen`, ngôi `ich` chia là `will`.
73. **Câu 73**: Điền 2 từ còn thiếu (phân biệt `zum` và `in den`) để hoàn thành câu: *„Buổi sáng chúng tôi đi đến Quảng trường Alexander, và buổi chiều chúng tôi đi vào trong Nhà thờ lớn Berlin.“*
    * Khung câu hiển thị: `Am Vormittag gehen wir [1] Alexanderplatz, und am Nachmittag gehen wir [2] Berliner Dom.`
    * Đáp án từng ô: Ô 1 = `["zum"]`, Ô 2 = `["in den"]`.
    * Giải thích: Đi đến quảng trường dùng `zum Alexanderplatz` (`zu + dem`); đi vào bên trong nhà thờ lớn dùng `in den Berliner Dom` (`in + Akkusativ`).
74. **Câu 74**: Điền 2 từ còn thiếu để hoàn thành câu: *„Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.“*
    * Khung câu hiển thị: `Anschließend [1] Maria und ich auf der Friedrichstraße [2].` (Gợi ý: `wollen`, `đi dạo phố`)
    * Đáp án từng ô: Ô 1 = `["wollen"]`, Ô 2 = `["bummeln"]`.
    * Giải thích: Chủ ngữ `Maria und ich` (`wir`) chia `wollen` ở vị trí số 2, động từ nguyên mẫu `bummeln` đứng cuối câu.
75. **Câu 75**: Điền 2 từ còn thiếu để hoàn thành câu hỏi đường: *„Xin lỗi, tôi đang tìm rạp chiếu phim. Làm thế nào tôi đi đến được rạp chiếu phim?“*
    * Khung câu hiển thị: `Entschuldigung, ich [1] das Kino. Wie komme ich [2] Kino?`
    * Đáp án từng ô: Ô 1 = `["suche"]`, Ô 2 = `["ins", "zum"]`.
    * Giải thích: *"Tôi đang tìm"* là `ich suche`; *"đến rạp chiếu phim"* là `ins Kino` (`in + das`) hoặc `zum Kino`.
76. **Câu 76**: Điền 2 động từ khuyết thiếu (`müssen` và `wollen`) chia theo ngôi `ich` vào chỗ trống: *„Vào cuối tuần tôi phải làm việc, nhưng sang năm ở Đức tôi muốn học đại học.“*
    * Khung câu hiển thị: `Am Wochenende [1] ich arbeiten, aber nächstes Jahr in Deutschland [2] ich studieren.`
    * Đáp án từng ô: Ô 1 = `["muss"]`, Ô 2 = `["will"]`.
    * Giải thích: Ngôi `ich` của `müssen` là `muss`, của `wollen` là `will`.
77. **Câu 77**: Điền 2 từ còn thiếu để hoàn thành câu chỉ đường: *„Ngài hãy đi cho đến đèn giao thông, ở bên phải Ngài sẽ nhìn thấy bưu điện.“*
    * Khung câu hiển thị: `Gehen Sie bis zur [1]. Rechts [2] Sie die Post.`
    * Đáp án từng ô: Ô 1 = `["Ampel"]`, Ô 2 = `["sehen"]`.
    * Giải thích: Đèn giao thông là `die Ampel` (`bis zur Ampel`); nhìn thấy là `sehen Sie`.

---

#### NHÓM 7: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 9 Câu: Câu 78 $\rightarrow$ Câu 86)
78. **Câu 78**:
    * `audio_text`: *"Zuerst gehen Sie geradeaus und dann die erste Straße rechts, an der Bank vorbei."*
    * `display_sentence`: *"Zuerst gehen Sie ___ und dann die erste Straße rechts, an der Bank vorbei."*
    * `hint_vi`: *"Đầu tiên Ngài đi thẳng và sau đó rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."*
    * `accepted_answers`: `["geradeaus"]`
    * Giải thích: Từ chỉ hướng *"đi thẳng"* là `geradeaus`.
79. **Câu 79**:
    * `audio_text`: *"Gehen Sie bitte bis zur zweiten Kreuzung links und danach bis zur Ampel."*
    * `display_sentence`: *"Gehen Sie bitte bis zur zweiten ___ links und danach bis zur Ampel."*
    * `hint_vi`: *"Xin Ngài hãy đi cho đến ngã tư thứ hai bên trái và tiếp theo đi cho đến đèn giao thông."*
    * `accepted_answers`: `["Kreuzung"]`
    * Giải thích: Danh từ `die Kreuzung` có nghĩa là ngã tư, giao lộ.
80. **Câu 80**:
    * `audio_text`: *"Paula und Alex gehen zum Brandenburger Tor und machen viele Fotos."*
    * `display_sentence`: *"Paula und Alex gehen ___ Brandenburger Tor und machen viele Fotos."*
    * `hint_vi`: *"Paula và Alex đi đến Cổng Brandenburg và chụp nhiều bức ảnh."*
    * `accepted_answers`: `["zum"]`
    * Giải thích: `zu + dem Brandenburger Tor` viết tắt là `zum Brandenburger Tor`.
81. **Câu 81**:
    * `audio_text`: *"Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke."*
    * `display_sentence`: *"Sie fahren mit dem Bus am ___ vorbei und laufen über die Schlossbrücke."*
    * `hint_vi`: *"Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."*
    * `accepted_answers`: `["Bundeskanzleramt"]`
    * Giải thích: Phủ Thủ tướng Liên bang Đức là `das Bundeskanzleramt`.
82. **Câu 82**:
    * `audio_text`: *"Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert."*
    * `display_sentence`: *"Am Nachmittag gehen sie in den Berliner ___ und hören ein Konzert."*
    * `hint_vi`: *"Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc."*
    * `accepted_answers`: `["Dom"]`
    * Giải thích: Nhà thờ lớn Berlin là `der Berliner Dom`.
83. **Câu 83**:
    * `audio_text`: *"Wir wollen heute eine Stadtrundfahrt in Berlin machen."*
    * `display_sentence`: *"Wir wollen heute eine ___ in Berlin machen."*
    * `hint_vi`: *"Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố ở Berlin."*
    * `accepted_answers`: `["Stadtrundfahrt"]`
    * Giải thích: Danh từ `die Stadtrundfahrt` có nghĩa là chuyến tham quan vòng quanh thành phố.
84. **Câu 84**:
    * `audio_text`: *"Anschließend wollen Maria und ich auf der Friedrichstraße bummeln."*
    * `display_sentence`: *"Anschließend wollen Maria und ich auf der Friedrichstraße ___."*
    * `hint_vi`: *"Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."*
    * `accepted_answers`: `["bummeln"]`
    * Giải thích: Động từ nguyên mẫu `bummeln` có nghĩa là đi dạo phố, tản bộ ngắm cảnh.
85. **Câu 85**:
    * `audio_text`: *"Gehen Sie bitte an der Kirche vorbei und dann über den Platz."*
    * `display_sentence`: *"Gehen Sie bitte an der ___ vorbei und dann über den Platz."*
    * `hint_vi`: *"Xin Ngài hãy đi ngang qua nhà thờ và sau đó đi băng qua quảng trường."*
    * `accepted_answers`: `["Kirche"]`
    * Giải thích: Danh từ `die Kirche` có nghĩa là nhà thờ (`an der Kirche vorbei`).
86. **Câu 86**:
    * `audio_text`: *"In Deutschland will mein Bruder an der Humboldt-Universität studieren."*
    * `display_sentence`: *"In Deutschland ___ mein Bruder an der Humboldt-Universität studieren."*
    * `hint_vi`: *"Ở Đức anh trai tôi muốn học đại học tại trường Đại học Humboldt."*
    * `accepted_answers`: `["will"]`
    * Giải thích: Động từ khuyết thiếu `wollen` chia ở ngôi thứ 3 số ít (`mein Bruder`) là `will`.

---

#### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT $\rightarrow$ ĐỨC (`dich_cau_vd` — 7 Câu: Câu 87 $\rightarrow$ Câu 93, chấm đa đáp án linh hoạt)
87. **Câu 87**: Dịch câu hỏi đường sau sang tiếng Đức: ***"Xin lỗi, tôi đang tìm bưu điện. Làm thế nào tôi đi đến được bưu điện?"***
    * `accepted_answers`:
      * `"Entschuldigung, ich suche die Post. Wie komme ich zur Post?"`
      * `"Entschuldigung, ich suche die Post. Wo geht es zur Post?"`
      * `"Entschuldigen Sie, ich suche die Post. Wie komme ich zur Post?"`
    * Giải thích: `die Post` mang giống cái; sau `ich suche` (`Akkusativ`) là `die Post`, còn sau `Wie komme ich ...?` (`zu + Dativ`) là `zur Post`.
88. **Câu 88**: Dịch câu chỉ đường sau sang tiếng Đức: ***"Đầu tiên Ngài đi thẳng, sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."***
    * `accepted_answers`:
      * `"Zuerst gehen Sie geradeaus, dann gehen Sie die erste Straße rechts, an der Bank vorbei."`
      * `"Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei."`
      * `"Gehen Sie zuerst geradeaus und dann die erste Straße rechts, an der Bank vorbei."`
    * Giải thích: `Zuerst gehen Sie geradeaus`, `die erste Straße rechts`, và `an der Bank vorbei` (`an + Dativ + vorbei`).
89. **Câu 89**: Dịch câu chỉ đường sau sang tiếng Đức: ***"Ngài hãy đi cho đến ngã tư thứ hai bên trái, tiếp theo đi cho đến đèn giao thông."***
    * `accepted_answers`:
      * `"Gehen Sie bis zur zweiten Kreuzung links, danach gehen Sie bis zur Ampel."`
      * `"Gehen Sie bis zur zweiten Kreuzung links und danach bis zur Ampel."`
      * `"Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel."`
    * Giải thích: Cả `die Kreuzung` và `die Ampel` đều đi với `bis zur` (`bis zu + der`).
90. **Câu 90**: Dịch câu sau sang tiếng Đức: ***"Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."***
    * `accepted_answers`:
      * `"Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke."`
      * `"Sie fahren mit dem Bus am Bundeskanzleramt vorbei und gehen über die Schlossbrücke."`
    * Giải thích: `am Bundeskanzleramt vorbei` (`an + dem ... vorbei`) và `über die Schlossbrücke` (`über + Akkusativ`).
91. **Câu 91**: Dịch câu sau sang tiếng Đức: ***"Chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia."***
    * `accepted_answers`:
      * `"Wir wollen eine Stadtrundfahrt machen, und danach will ich in die Nationalgalerie gehen."`
      * `"Wir wollen noch eine Stadtrundfahrt machen. Danach will ich in die Nationalgalerie gehen."`
      * `"Wir wollen eine Stadtrundfahrt machen. Danach will ich in die Alte Nationalgalerie gehen."`
    * Giải thích: `Wir wollen ... machen` (ngôi `wir`) và `Danach will ich ... gehen` (ngôi `ich`).
92. **Câu 92**: Dịch câu sau sang tiếng Đức: ***"Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."***
    * `accepted_answers`:
      * `"Anschließend wollen Maria und ich auf der Friedrichstraße bummeln."`
      * `"Danach wollen Maria und ich auf der Friedrichstraße bummeln."`
      * `"Maria und ich wollen anschließend auf der Friedrichstraße bummeln."`
    * Giải thích: `Anschließend` đứng đầu câu đảo `wollen` lên vị trí số 2, động từ nguyên mẫu `bummeln` đứng ở cuối câu.
93. **Câu 93**: Dịch câu sau sang tiếng Đức: ***"Ngài hãy đi xuyên qua Cổng Brandenburg và đi băng qua quảng trường."***
    * `accepted_answers`:
      * `"Gehen Sie durch das Brandenburger Tor und über den Platz."`
      * `"Gehen Sie durch das Brandenburger Tor und gehen Sie über den Platz."`
      * `"Bitte gehen Sie durch das Brandenburger Tor und über den Platz."`
    * Giải thích: `durch das Brandenburger Tor` (`durch + Akkusativ`) và `über den Platz` (`über + Akkusativ`).

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC $\rightarrow$ VIỆT (`dich_cau_dv` — 7 Câu: Câu 94 $\rightarrow$ Câu 100, chấm đa đáp án linh hoạt)
94. **Câu 94**: Dịch câu sau sang tiếng Việt: ***„Zuerst gehen Sie geradeaus, bis zur zweiten Kreuzung rechts. Dann gehen Sie geradeaus, über die Kreuzung. Links sehen Sie die Post.“***
    * `accepted_answers`:
      * `"Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện."`
      * `"Trước tiên hãy đi thẳng đến ngã tư thứ hai bên phải. Sau đó đi thẳng băng qua ngã tư. Bên trái bạn sẽ thấy bưu điện."`
      * `"Đầu tiên Ngài đi thẳng tới ngã tư thứ hai bên tay phải, sau đó đi thẳng qua ngã tư, bên trái Ngài thấy bưu điện."`
    * Giải thích: Đây là toàn bộ Lộ trình số 2 trên bản đồ chỉ đường tới Bưu điện (`die Post`).
95. **Câu 95**: Dịch câu sau sang tiếng Việt: ***„Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin und gehen zuerst zum Brandenburger Tor.“***
    * `accepted_answers`:
      * `"Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg."`
      * `"Paula và Alex tới từ Madrid, họ đến thăm bạn bè tại Berlin và trước tiên đi tới Cổng Brandenburg."`
    * Giải thích: `besuchen Freunde` = thăm bạn bè; `gehen zum Brandenburger Tor` = đi đến Cổng Brandenburg.
96. **Câu 96**: Dịch câu sau sang tiếng Việt: ***„Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert. Am Abend gehen sie in die Disko.“***
    * `accepted_answers`:
      * `"Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường."`
      * `"Buổi chiều họ vào trong Nhà thờ lớn Berlin nghe hòa nhạc, buổi tối họ đi tới quán bar vũ trường."`
    * Giải thích: `in den Berliner Dom` = vào trong Nhà thờ lớn Berlin; `in die Disko` = vào trong vũ trường.
97. **Câu 97**: Dịch câu sau sang tiếng Việt: ***„Gehen Sie bitte an der Kirche vorbei, dann die Lạch-Tray-Straße entlang bis zur Ampel!“***
    * `accepted_answers`:
      * `"Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!"`
      * `"Hãy đi ngang qua nhà thờ rồi đi dọc đường Lạch Tray tới chỗ đèn giao thông!"`
    * Giải thích: `an der Kirche vorbei` = đi ngang qua nhà thờ; `die Lạch-Tray-Straße entlang` = đi dọc theo đường Lạch Tray; `bis zur Ampel` = cho đến đèn giao thông.
98. **Câu 98**: Dịch câu sau sang tiếng Việt: ***„Heute Abend wollen wir noch einen Film im Kino sehen, aber am Wochenende muss ich arbeiten.“***
    * `accepted_answers`:
      * `"Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc."`
      * `"Tối nay chúng mình còn muốn xem phim ở rạp nhưng cuối tuần mình phải đi làm."`
    * Giải thích: Kết hợp hai động từ khuyết thiếu `wollen` (muốn) và `müssen` (phải).
99. **Câu 99**: Dịch câu sau sang tiếng Việt: ***„Entschuldigung, wie komme ich zur Museumsinsel und zur Humboldt-Universität?“***
    * `accepted_answers`:
      * `"Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?"`
      * `"Xin lỗi cho hỏi tôi đi tới Đảo Bảo tàng và Đại học Humboldt bằng cách nào?"`
    * Giải thích: Cả `die Museumsinsel` và `die Humboldt-Universität` đều mang giống cái nên đi với `zur` (`zu + der`).
100. **Câu 100**: Dịch câu sau sang tiếng Việt: ***„Die Touristen gehen durch das alte Stadttor, laufen über den Marktplatz und besichtigen das schöne Schloss.“***
     * `accepted_answers`:
       * `"Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ."`
       * `"Những người khách du lịch đi qua cổng thành cũ, băng qua quảng trường chợ và tham quan lâu đài tuyệt đẹp."`
     * Giải thích: `durch das alte Stadttor` = xuyên qua cổng thành cổ; `über den Marktplatz` = băng qua quảng trường chợ; `besichtigen das schöne Schloss` = tham quan lâu đài/cung điện đẹp.

---

## PHẦN 4: KIẾN TRÚC BỘ SINH ĐỀ & BẢN ĐỒ ĐỘNG (`DYNAMIC VISUAL MAP & MULTI-VARIABLE RANDOMIZER`) CHO BÀI 8

Khi người học bấm nút **`🔄 Đổi đề khác`** hoặc thoát ra vào lại, Antigravity IDE phải kích hoạt **4 Engine Sinh Đề Động (`Atomic Visual & Grammar Generators`)**:

### 4.1. Engine 1: Bộ Sinh Bản Đồ Đường Phố SVG Động (`Dynamic SVG Street Grid Map Generator`)
* Tự động vẽ một bản đồ lưới $3 \times 3$ bằng SVG và sinh ngẫu nhiên một lộ trình mới từ **`📍 Start`**:
  * **Biến thiên ngã rẽ**: `die erste / zweite / dritte Straße links / rechts` hoặc `bis zur ersten / zweiten / dritten Kreuzung links / rechts`.
  * **Biến thiên tòa nhà đi ngang qua (`an + Dativ + vorbei`)**:
    * Giống cái (`an der ... vorbei`): `an der Bank vorbei`, `an der Kirche vorbei`, `an der Schule vorbei`, `an der Post vorbei`, `an der Universität vorbei`.
    * Giống đực & trung (`am ... vorbei`): `am Supermarkt vorbei`, `am Bahnhof vorbei`, `am Krankenhaus vorbei`, `am Kino vorbei`, `am Hotel vorbei`, `am Bundeskanzleramt vorbei`.
  * **Biến thiên chướng ngại vật đi qua (`durch / über / entlang`)**: `durch das Stadttor`, `durch den Park`, `über die Brücke`, `über den Platz`, `über die Kreuzung`, `die Friedrichstraße entlang`.
  * **Biến thiên Điểm Đích (`Rechts / Links sehen Sie ...`)**: `die Post`, `das Kino`, `das Einkaufszentrum`, `das Schloss`, `den Bahnhof`, `den Zoo`.
  * Toàn bộ hình vẽ SVG trên màn hình, câu hỏi tiếng Đức, đáp án đúng, bản dịch tiếng Việt và lời giải thích được sinh từ cùng một đối tượng dữ liệu duy nhất!

### 4.2. Engine 2: Bộ Sinh Thẻ Hình Chỉ Đường Tương Tác (`Visual Direction Card Generator a -> l`)
* Hoán vị ngẫu nhiên 12 biểu tượng SVG chỉ đường (`a` đến `l`) với đa dạng chủ ngữ mệnh lệnh (`Gehen Sie ...!`, `Fahren Sie ...!`, `Geh bitte ...!`, `Geht bitte ...!`) và tên đường phố khác nhau.

### 4.3. Engine 3: Bộ Sinh Hành Trình Khám Phá Thành Phố Với 14 Địa Danh Berlin (`Berlin Sightseeing Route Generator`)
* Tự động kết hợp đa chủ ngữ (`Ich, Du, Paula und Alex, Mijn Bruder, Unsere Klasse, Die Touristen aus Japan, Herr und Frau Weber, Ihr...`) với 14 địa danh Berlin, tự động phân biệt chính xác khi nào dùng **`zum / zur`** (`zum Brandenburger Tor`, `zum Reichstag`, `zur Museumsinsel`, `zur Staatsoper`) và khi nào dùng **`in den / in die / ins`** (`in den Berliner Dom`, `in die Alte Nationalgalerie`, `ins Bundeskanzleramt`, `ins Sony Center`).

### 4.4. Engine 4: Ma Trận 4 Động Từ Khuyết Thiếu (`möchten, können, müssen, wollen`) Đa Chủ Ngữ
* Tự động xoay vòng 9 ngôi nhân xưng (`ich, du, er, sie, es, wir, ihr, sie, Sie`) kết hợp với chuỗi liên từ trình tự (`Zuerst -> Dann -> Danach -> Anschließend -> Heute Abend`) và các hoạt động trong thành phố (`eine Stadtrundfahrt machen`, `auf der Friedrichstraße bummeln`, `einen Film im Kino sehen`, `Fotos am Brandenburger Tor machen`, `in Deutschland studieren`).

---

## PHẦN 5: DANH SÁCH KIỂM THỬ BẮT BUỘC SAU KHI CODE (`POST-CODING QA & VISUAL VERIFICATION CHECKLIST`)

Sau khi code xong Bài 8, Antigravity IDE **BẮT BUỘC** phải viết và chạy kịch bản kiểm thử tự động (`verify_lesson8_qa.py`) để kiểm tra 7 tiêu chí sau trước khi hoàn tất:

1. **Kiểm tra Bảo toàn Tuyệt đối Bài 1 $\rightarrow$ Bài 7 (`Zero-Regression Check`)**:
   * Xác nhận trong cơ sở dữ liệu `deutsch_meister.db`: **Bài 1 (P1), Bài 1 (P2), Bài 2, Bài 3, Bài 4, Bài 5, Bài 6, Bài 7** vẫn giữ nguyên 100% nội dung lý thuyết, từ vựng và số lượng câu hỏi bài tập, không bị xóa hay ghi đè.
2. **Kiểm tra Hiển thị Hình ảnh Sơ đồ & Bản đồ SVG (`Visual SVG Rendering Verification`)**:
   * Xác nhận trong phần Lý thuyết Bài 8 có đầy đủ: **4 Sơ đồ giới từ không gian (`an...vorbei`, `durch`, `über`, `entlang`)**, **12 Thẻ hình chỉ đường (`a` đến `l`)** và **Bản đồ lưới đường phố 2 lộ trình (`Route 1` & `Route 2`)**.
   * Xác nhận trong phần Bài tập Bài 8: Các câu hỏi có gắn `visual_svg` hiển thị đúng hình vẽ sơ đồ/bản đồ SVG ngay phía trên câu hỏi và tự động vẽ lại bản đồ mới khi bấm `🔄 Đổi đề khác`.
3. **Kiểm tra Quy mô 100 Câu hỏi & Chống Trùng Lặp Tuyệt Đối (`100-Question & Zero-Duplicate Verification`)**:
   * Xác nhận **Bài 8** có đúng **100 câu hỏi** (`trac_nghiem`: 18, `dien_khuyet`: 15, `dich_nghia_vd`: 12, `dich_nghia_dv`: 12, `noi_o`: 10, `dien_tao_cau`: 10, `nghe_dien`: 9, `dich_cau_vd`: 7, `dich_cau_dv`: 7) và **0 câu trùng lặp** (`len(unique_questions) == 100`).
4. **Kiểm tra Khớp Nguyên Tử Đề Bài – Hình Bản Đồ – Đáp Án – Dịch Nghĩa – Giải Thích (`Atomic Alignment Check`)**:
   * Chạy vòng lặp giả lập 20 lần gọi API lấy đề bài tập Bài 8: Đảm bảo 100% câu hỏi đều có đáp án đúng khớp với hình SVG, bản dịch tiếng Việt đầy đủ và lời giải thích ngữ pháp chuẩn xác.
5. **Kiểm tra 100% Thẻ Từ Vựng & Câu Ví Dụ (`Vocabulary Card Match Check`)**:
   * Quét toàn bộ từ vựng của Bài 8 trong `seed_a1_b8.py` và `lexikon_db.js`: Đảm bảo 100% câu ví dụ tiếng Đức (`example_de`) chứa chính xác từ vựng trên thẻ đó và bản dịch tiếng Việt (`example_vi`) dịch đúng nghĩa.
6. **Kiểm tra Giọng Đọc TTS `de-DE` (`Voice Check`)**:
   * Đảm bảo mọi nút `🔊` trong Bài 8, trên các thẻ sơ đồ chỉ đường và trong câu hỏi `nghe_dien` chỉ truyền văn bản tiếng Đức chuẩn vào `speakGerman()`.
7. **Đồng bộ lên GitHub (`Git Commit & Push`)**:
   * Sau khi toàn bộ bài kiểm thử đạt `100% PASS`, đẩy code lên repository `taolagautruc/deutsch-meister`:
     ```bash
     git add .
     git commit -m "Add Lesson 8 (Stadt, Wegbeschreibung with interactive SVG maps & diagrams, Modalverben wollen) with 100 unique exercises and Zero-Bug QA"
     git push origin main
     ```