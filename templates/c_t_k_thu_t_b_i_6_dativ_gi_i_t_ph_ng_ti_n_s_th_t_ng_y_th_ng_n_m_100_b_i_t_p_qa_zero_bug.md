# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 6 (A1) "DATIV - GIỚI TỪ TRONG DATIV - PHƯƠNG TIỆN GIAO THÔNG - SỐ THỨ TỰ - NGÀY THÁNG NĂM" (`ORIENTIERUNG`) & KHO 100 BÀI TẬP ĐA CHIỀU (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa làm hỏng, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**, **Bài 4**, **Bài 5**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này là **tạo mới hoàn toàn Bài 6 (`lessons/a1/seed_a1_b6.py`)** với quy mô **100 câu hỏi bài tập**, nối tiếp vào danh sách bài học cấp độ **A1** (`lesson_order = 7`), cộng dồn động từ và từ vựng của Bài 6 vào 2 chuyên mục tra cứu, mở rộng trần kiến thức Đấu trường tới Bài 6, và chạy kịch bản kiểm thử toàn diện.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu.
>
> ---
>
> ### 🔍 2. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI (`ZERO-BUG QA PROTOCOL` — CẤM LẶP LẠI CÁC LỖI CŨ)
> Antigravity IDE **BẮT BUỘC TUYỆT ĐỐI KHÔNG ĐƯỢC MẮC LẠI** bất kỳ lỗi nào từng xuất hiện trước đây:
>
> 1. **Cấm dịch sai nghĩa hoặc thiếu phần dịch nghĩa (`No Missing/Wrong Translations`)**:
>    * 100% từ vựng, câu ví dụ trên thẻ từ vựng, bảng biểu lý thuyết, câu hội thoại mẫu và 100% câu hỏi trong phần bài tập phải có bản dịch tiếng Việt chuẩn xác, tự nhiên. Tuyệt đối không để trống hoặc hiện `undefined` / `null`.
> 2. **Cấm dịch đáp án hoặc giải thích không liên quan đến đề bài (`Strict Atomic Alignment`)**:
>    * Khi tạo câu hỏi tĩnh cũng như khi chạy bộ sinh đề ngẫu nhiên (`Dynamic Randomizer`), **Đề bài (`question`) – Đáp án đúng (`correct_answer` / `accepted_answers`) – Bản dịch tiếng Việt của câu hỏi (`translation_vi`) – Lời giải thích (`explanation`)** phải được đóng gói trong cùng một hàm sinh nguyên tử (`Atomic Question Generator`).
>    * **Cấm tuyệt đối** việc đề bài hỏi về ngôi `wir` hoặc ngày `15.08.` nhưng đáp án hoặc lời giải thích lại nói về ngôi `ich` hoặc ngày `03.05.`!
> 3. **Cấm thiếu Voice hoặc Voice đọc sai ngôn ngữ (`100% Clean German TTS Voice`)**:
>    * Mọi thẻ từ vựng, mọi dòng chia động từ, mọi mốc ngày tháng/số thứ tự và mọi câu hỏi nghe (`nghe_dien`) phải có nút `🔊` hoạt động 100%.
>    * Hàm `speakGerman(text, rate)` chỉ được truyền chuỗi tiếng Đức sạch (`de-DE`), tuyệt đối không đọc lẫn nghĩa tiếng Việt, không đọc dấu gạch dưới `___`, mũi tên `->` hay ký hiệu `(m)/(f)/(n)/(Pl)`.
>    * *Lưu ý đặc biệt với Số thứ tự & Ngày tháng*: Khi truyền vào TTS để đọc ngày tháng (ví dụ hiển thị `am 3. Mai`), chuỗi truyền vào `speakGerman()` phải được viết rõ thành chữ tiếng Đức **`"am dritten Mai"`** để máy đọc đúng ngữ pháp số thứ tự thay vì đọc số đếm!
> 4. **Cấm đưa câu ví dụ không khớp với thẻ từ vựng đang học (`Exact Vocabulary-Example Matching`)**:
>    * Thẻ từ vựng đang dạy từ nào (ví dụ `die Straßenbahn`, `der Aufzug`, `die Haltestelle`, `der Kalender`) thì câu ví dụ tiếng Đức (`example_de`) và dịch nghĩa (`example_vi`) **bắt buộc phải chứa chính xác từ vựng đó**.
> 5. **Đa dạng hóa Chủ ngữ, Ngữ cảnh & Biến thiên Số liệu (`Multi-Subject & Multi-Context Diversity`)**:
>    * Tuyệt đối không chỉ dùng mỗi ngôi `ich` hay chép y nguyên vài câu trong giáo trình. Phải luân phiên đủ 9 đại từ nhân xưng (`ich, du, er, sie, es, wir, ihr, sie, Sie`) và các danh từ làm chủ ngữ (`Herr Schneider, Frau Wagner, mein Vater, deine Schwester, der Tourist, unsere Kollegen, die Studenten...`) trong nhiều ngữ cảnh mới mẻ (đi làm, đi du lịch, hỏi đường, tìm phòng làm việc trong tòa nhà, sắp xếp bàn làm việc, hỏi ngày sinh nhật, lịch nghỉ phép, lịch tàu xe...).

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 → Bài 5 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 6**:

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung **12 động từ trọng tâm của Bài 6** (nhóm di chuyển, định hướng vị trí và hoạt động giao thông), kèm phát âm `de-DE` cho từng ngôi và câu ví dụ chuẩn:
1. **`fahren`** (*đi bằng phương tiện có bánh xe / tàu thủy; lái xe* — **Động từ bất quy tắc biến âm `a -> ä`** ở ngôi `du, er/sie/es`):
   * Chia theo ngôi: `ich fahre`, `du fährst`, `er/sie/es fährt`, `wir fahren`, `ihr fahrt`, `sie/Sie fahren`.
   * Ví dụ: *„Mein Bruder fährt jeden Tag mit dem Bus zur Arbeit.“ (Anh trai tôi đi làm mỗi ngày bằng xe buýt.)*
2. **`fliegen`** (*bay, đi bằng máy bay* — Quy tắc ở Hiện tại):
   * Chia theo ngôi: `ich fliege`, `du fliegst`, `er/sie/es fliegt`, `wir fliegen`, `ihr fliegt`, `sie/Sie fliegen`.
   * Ví dụ: *„Im August fliegen wir mit dem Flugzeug nach Deutschland.“ (Vào tháng Tám chúng tôi bay bằng máy bay sang Đức.)*
3. **`abfahren`** (*khởi hành, xuất bến [tàu/xe]* — **Động từ tách** `ab-` + gốc biến âm `fahren` `a -> ä`):
   * Chia theo ngôi: `ich fahre ... ab`, `du fährst ... ab`, `er/sie/es fährt ... ab`, `wir fahren ... ab`, `ihr fahrt ... ab`, `sie/Sie fahren ... ab`.
   * Ví dụ: *„Der Zug fährt um acht Uhr am Bahnhof ab.“ (Chuyến tàu khởi hành lúc 8 giờ tại nhà ga.)*
4. **`ankommen`** (*đến nơi [tàu/xe/người]* — **Động từ tách** `an-` + gốc `kommen`):
   * Chia theo ngôi: `ich komme ... an`, `du kommst ... an`, `er/sie/es kommt ... an`, `wir kommen ... an`, `ihr kommt ... an`, `sie/Sie kommen ... an`.
   * Ví dụ: *„Wann kommt der Bus an der Haltestelle an?“ (Khi nào xe buýt đến trạm dừng?)*
5. **`umsteigen`** (*đổi tàu, chuyển tuyến xe* — **Động từ tách** `um-` + gốc `steigen`):
   * Chia theo ngôi: `ich steige ... um`, `du steigst ... um`, `er/sie/es steigt ... um`, `wir steigen ... um`, `ihr steigt ... um`, `sie/Sie steigen ... um`.
   * Ví dụ: *„Am Hauptbahnhof müssen die Fahrgäste umsteigen.“ (Tại nhà ga trung tâm các hành khách phải đổi tàu.)*
6. **`einsteigen`** (*lên tàu/xe* — **Động từ tách** `ein-` + gốc `steigen`):
   * Chia theo ngôi: `ich steige ... ein`, `du steigst ... ein`, `er/sie/es steigt ... ein`...
   * Ví dụ: *„Bitte steigen Sie schnell in den Bus ein!“ (Xin Ngài vui lòng bước nhanh lên xe buýt!)*
7. **`aussteigen`** (*xuống tàu/xe* — **Động từ tách** `aus-` + gốc `steigen`):
   * Chia theo ngôi: `ich steige ... aus`, `du steigst ... aus`, `er/sie/es steigt ... aus`...
   * Ví dụ: *„An der nächsten Haltestelle steige ich aus.“ (Ở trạm dừng tiếp theo tôi sẽ xuống xe.)*
8. **`stehen`** (*đứng [chỉ vị trí tĩnh + Dativ]*):
   * Chia theo ngôi: `ich stehe`, `du stehst`, `er/sie/es steht`, `wir stehen`, `ihr steht`, `sie/Sie stehen`.
   * Ví dụ: *„Der Drucker steht auf dem Schreibtisch neben dem Computer.“ (Chiếc máy in nằm/đứng trên bàn làm việc bên cạnh máy tính.)*
9. **`sitzen`** (*ngồi [chỉ vị trí tĩnh + Dativ, gốc `-z`]*):
   * Chia theo ngôi: `ich sitze`, `du sitzt`, `er/sie/es sitzt`, `wir sitzen`, `ihr sitzt`, `sie/Sie sitzen`.
   * Ví dụ: *„Die Studenten sitzen im Café vor der Universität.“ (Các sinh viên đang ngồi trong quán cà phê phía trước trường đại học.)*
10. **`hängen`** (*treo [chỉ vị trí tĩnh + Dativ]*):
    * Chia theo ngôi: `ich hänge`, `du hängst`, `er/sie/es hängt`, `wir hängen`, `ihr hängt`, `sie/Sie hängen`.
    * Ví dụ: *„Das Bild hängt an der Wand über dem Sofa.“ (Bức tranh treo trên tường phía trên ghế sofa.)*
11. **`helfen`** (*giúp đỡ [+ Cách 3 Dativ]* — **Biến âm `e -> i`** ở `du hilfst, er/sie/es hilft`):
    * Chia theo ngôi: `ich helfe`, `du hilfst`, `er/sie/es hilft`, `wir helfen`, `ihr helft`, `sie/Sie helfen`.
    * Ví dụ: *„Der Kollege hilft der neuen Mitarbeiterin im Büro.“ (Người đồng nghiệp giúp đỡ nữ nhân viên mới ở trong văn phòng.)*
12. **`gefallen`** (*làm hài lòng / thích [+ Cách 3 Dativ]* — **Biến âm `a -> ä`** ở `du gefällst, er/sie/es gefällt`):
    * Chia theo ngôi: `ich gefalle`, `du gefällst`, `er/sie/es gefällt`, `wir gefallen`, `ihr gefallt`, `sie/Sie gefallen`.
    * Ví dụ: *„Die neue Wohnung im dritten Stock gefällt meinem Vater sehr.“ (Căn hộ mới ở tầng ba làm bố tôi rất thích.)*

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung 2 chủ đề lọc mới của Bài 6 với đầy đủ **45 danh từ có mạo từ (`der/die/das`), dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng thẻ từ vựng**:
1. **`Phương tiện Giao thông & Địa điểm Thành phố (Bài 6)`**
2. **`Tòa nhà, Văn phòng & Đồ vật Bàn làm việc (Bài 6)`**

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 6: "DATIV - GIỚI TỪ TRONG DATIV - PHƯƠNG TIỆN GIAO THÔNG - SỐ THỨ TỰ - NGÀY THÁNG NĂM" (`ORIENTIERUNG`)

Bài học thứ 7 trong danh sách Cấp độ A1 (`lesson_order = 7`):
* **Tiêu đề bài học**: `Bài 6: Dativ - Giới từ trong Dativ - Phương tiện giao thông - Số thứ tự - Ngày tháng năm (Orientierung)`
* **Mô tả ngắn**: `Làm chủ hoàn toàn Cách 3 (Dativ) với hệ thống bảng ma trận đối chiếu Nominativ - Akkusativ - Dativ theo từng giống và 9 ngôi sở hữu; nắm vững nhóm giới từ luôn đi với Dativ (mit, nach, aus, zu, von, bei) và 9 giới từ chỉ vị trí tĩnh (Wo? + Dativ); từ vựng phương tiện giao thông, tòa nhà văn phòng; quy tắc Số thứ tự (Ordinalzahlen) và cách đọc/viết Ngày - Tháng - Năm chuẩn xác.`

---

### HỌC PHẦN 1: CÁCH 3 TRONG TIẾNG ĐỨC (`DER DATIV`) & HỆ THỐNG BẢNG MA TRẬN MẠO TỪ TOÀN DIỆN

#### 1.1. Bản chất của Cách 3 (`Dativ`) & Khi nào sử dụng `Dativ`?
Ở Bài 2 và Bài 4, chúng ta đã học **Cách 1 (`Nominativ` — Chủ ngữ cách)** và **Cách 4 (`Akkusativ` — Tân ngữ trực tiếp)**. Sang Bài 6, chúng ta bước vào **Cách 3 (`Dativ` — Tân ngữ gián tiếp & Cách chỉ vị trí/phương tiện/thời gian)**. Một danh từ được chia ở **Cách 3 (`Dativ`)** trong 3 trường hợp chính sau:
1. **Đứng sau các giới từ bắt buộc đi với `Dativ`**: `mit` *(với / bằng phương tiện)*, `nach` *(đến / sau)*, `aus` *(đến từ / ra khỏi)*, `zu` *(tới chỗ)*, `von` *(từ / của)*, `bei` *(ở tại / chỗ ai)*, `seit` *(từ khi)*, `ab` *(bắt đầu từ)*, `gegenüber` *(đối diện)*.
2. **Đứng sau 9 giới từ chỉ vị trí (`in, an, auf, neben, vor, hinter, über, unter, zwischen`) khi trả lời cho câu hỏi `Wo?` *(Ở đâu? — Trạng thái tĩnh, không có sự di chuyển sang vị trí mới)*** hoặc trả lời câu hỏi **`Wann?` *(Khi nào?)* với `am, im, in der`**.
3. **Đóng vai trò Tân ngữ gián tiếp (người nhận lợi ích — trả lời câu hỏi `Wem?` *Cho ai?*)** hoặc đi sau các động từ đòi hỏi `Dativ` như `helfen` *(giúp đỡ ai)*, `danken` *(cảm ơn ai)*, `gefallen` *(làm ai thích)*, `gehören` *(thuộc về ai)*, `antworten` *(trả lời ai)*.

---

#### 1.2. Bảng 1: Quy tắc Vàng Biến Đổi Mạo Từ Ở Cách 3 (`Dativ`)
> **Công thức cốt lõi cần khắc cốt ghi tâm ở `Dativ`**:
> * **Giống đực (`Maskulinum - der`)** và **Giống trung (`Neutrum - das`)** biến đổi **GIỐNG HỆT NHAU**: đều chuyển sang đuôi **`-m`** (**`dem / einem / keinem / meinem`**).
> * **Giống cái (`Femininum - die`)**: chuyển sang đuôi **`-r`** (**`der / einer / keiner / meiner`**).
> * **Số nhiều (`Plural - die`)**: Mạo từ chuyển sang đuôi **`-n`** (**`den / — / keinen / meinen`**) **VÀ ĐẶC BIỆT: Danh từ số nhiều bắt buộc phải cộng thêm đuôi `-n` ở cuối** (nếu bản thân danh từ số nhiều đó chưa kết thúc bằng `-n` hoặc `-s`)!
>   * *Ví dụ cộng thêm `-n`*: `die Tische` → `auf den Tische` + **`n`** = **`auf den Tischen`**; `die Kinder` → **`mit den Kindern`**; `die Stühle` → **`auf den Stühlen`**; `die Häuser` → **`zwischen den Häusern`**.
>   * *Ví dụ giữ nguyên vì đã có `-n` hoặc `-s`*: `die Taschen` → **`in den Taschen`**; `die Autos` → **`zwischen den Autos`**; `die Büros` → **`in den Büros`**.

---

#### 1.3. Bảng 2: Ma Trận Tổng Hợp Đối Chiếu 3 Cách (`Nominativ` – `Akkusativ` – `Dativ`) Cho Mạo Từ Xác Định, Không Xác Định & Phủ Định
| Giống của Danh từ (`Genus`) | Loai Mạo Từ | Cách 1: `Nominativ`<br>*(Chủ ngữ: Wer / Was?)* | Cách 4: `Akkusativ`<br>*(Tân ngữ trực tiếp / Wohin?)* | Cách 3: `Dativ`<br>*(Vị trí Wo? / Phương tiện / Wem?)* | Ví Dụ Danh Từ Thực Tế Ở Cách 3 (`Dativ`) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| <span style="color:#3b82f6">**Giống đực (`Maskulinum`)**</span><br>*(VD: der Bus, der Tisch)* | • Xác định<br>• Không xác định<br>• Phủ định | **der**<br>**ein**<br>**kein** | **de<u>n</u>**<br>**eine<u>n</u>**<br>**keine<u>n</u>** | <span style="color:#f59e0b">**de<u>m</u>**<br>**eine<u>m</u>**<br>**keine<u>m</u>**</span> | mit **dem** Bus *(bằng xe buýt)*<br>auf **einem** Tisch *(trên một cái bàn)*<br>auf **keinem** Stuhl *(không trên cái ghế nào)* |
| <span style="color:#f43f5e">**Giống cái (`Femininum`)**</span><br>*(VD: die U-Bahn, die Bank)* | • Xác định<br>• Không xác định<br>• Phủ định | **die**<br>**eine**<br>**keine** | **die**<br>**eine**<br>**keine** | <span style="color:#f59e0b">**de<u>r</u>**<br>**eine<u>r</u>**<br>**keine<u>r</u>**</span> | mit **der** U-Bahn *(bằng tàu điện ngầm)*<br>neben **einer** Bank *(bên cạnh một ngân hàng)*<br>in **keiner** Küche *(không trong căn bếp nào)* |
| <span style="color:#10b981">**Giống trung (`Neutrum`)**</span><br>*(VD: das Auto, das Haus)* | • Xác định<br>• Không xác định<br>• Phủ định | **das**<br>**ein**<br>**kein** | **das**<br>**ein**<br>**kein** | <span style="color:#f59e0b">**de<u>m</u>**<br>**eine<u>m</u>**<br>**keine<u>m</u>**</span> | mit **dem** Auto *(bằng ô tô)*<br>vor **einem** Haus *(phía trước một ngôi nhà)*<br>in **keinem** Zimmer *(không trong căn phòng nào)* |
| <span style="color:#a855f7">**Số nhiều (`Plural`)**</span><br>*(VD: die Busse, die Kinder)* | • Xác định<br>• Không xác định<br>• Phủ định | **die**<br>*(không có)*<br>**keine** | **die**<br>*(không có)*<br>**keine** | <span style="color:#f59e0b">**de<u>n</u> + ...<u>n</u>**<br>**— + ...<u>n</u>**<br>**keine<u>n</u> + ...<u>n</u>**</span> | mit **den** Busse**<u>n</u>** *(bằng những chiếc xe buýt)*<br>mit Kinder**<u>n</u>** *(với trẻ em)*<br>mit **keinen** Freunde**<u>n</u>** *(không với người bạn nào)* |

---

#### 1.4. Bảng 3: Đại Ma Trận Mạo Từ Sở Hữu (`Possessivartikel`) Theo 9 Ngôi Nhân Xưng Ở Cả 3 Cách (`Nominativ` – `Akkusativ` – `Dativ`)
> **Quy tắc dễ nhớ nhất**: Gốc sở hữu (`mein-, dein-, sein-, ihr-, unser-, euer-, Ihr-`) luôn mang **đuôi giống hệt mạo từ phủ định `kein`** ở từng Cách:
> * Ở **`Dativ`**: Giống đực (`m`) thêm **`-em`** | Giống cái (`f`) thêm **`-er`** | Giống trung (`n`) thêm **`-em`** | Số nhiều (`Pl`) thêm **`-en`** (+ Danh từ thêm **`-n`**).
> * **Lưu ý đặc biệt với ngôi `ihr (các bạn)` → gốc `euer`**: Khi thêm đuôi bắt đầu bằng nguyên âm (`-e, -en, -em, -er`), chữ `e` trước chữ `r` thường được lược bỏ: **`eurem`** (hoặc *euerem*), **`eurer`** (hoặc *euerer*), **`eurem`**, **`euren`**.

| Ngôi Nhân Xưng & Gốc Sở Hữu | Cách (`Kasus`) | Giống Đực (`Maskulinum - der`)<br>*VD: Vater / Tisch* | Giống Cái (`Femininum - die`)<br>*VD: Mutter / Tasche* | Giống Trung (`Neutrum - das`)<br>*VD: Kind / Auto* | Số Nhiều (`Plural - die`)<br>*VD: Eltern / Freunde (+n)* |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1. `ich` (tôi)**<br>→ **`mein-`** | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | mein<br>mein**en**<br><span style="color:#f59e0b">**mein<u>em</u>**</span> | mein**e**<br>mein**e**<br><span style="color:#f59e0b">**mein<u>er</u>**</span> | mein<br>mein<br><span style="color:#f59e0b">**mein<u>em</u>**</span> | mein**e**<br>mein**e**<br><span style="color:#f59e0b">**mein<u>en</u> (+ -n)**</span> |
| **2. `du` (bạn)**<br>→ **`dein-`** | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | dein<br>dein**en**<br><span style="color:#f59e0b">**dein<u>em</u>**</span> | dein**e**<br>dein**e**<br><span style="color:#f59e0b">**dein<u>er</u>**</span> | dein<br>dein<br><span style="color:#f59e0b">**dein<u>em</u>**</span> | dein**e**<br>dein**e**<br><span style="color:#f59e0b">**dein<u>en</u> (+ -n)**</span> |
| **3. `er / es` (anh ấy / nó)**<br>→ **`sein-`** | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | sein<br>sein**en**<br><span style="color:#f59e0b">**sein<u>em</u>**</span> | sein**e**<br>sein**e**<br><span style="color:#f59e0b">**sein<u>er</u>**</span> | sein<br>sein<br><span style="color:#f59e0b">**sein<u>em</u>**</span> | sein**e**<br>sein**e**<br><span style="color:#f59e0b">**sein<u>en</u> (+ -n)**</span> |
| **4. `sie` (cô ấy)**<br>→ **`ihr-`** | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | ihr<br>ihr**en**<br><span style="color:#f59e0b">**ihr<u>em</u>**</span> | ihr**e**<br>ihr**e**<br><span style="color:#f59e0b">**ihr<u>er</u>**</span> | ihr<br>ihr<br><span style="color:#f59e0b">**ihr<u>em</u>**</span> | ihr**e**<br>ihr**e**<br><span style="color:#f59e0b">**ihr<u>en</u> (+ -n)**</span> |
| **5. `wir` (chúng tôi)**<br>→ **`unser-`** | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | unser<br>unser**en**<br><span style="color:#f59e0b">**unser<u>em</u>**</span> | unser**e**<br>unser**e**<br><span style="color:#f59e0b">**unser<u>er</u>**</span> | unser<br>unser<br><span style="color:#f59e0b">**unser<u>em</u>**</span> | unser**e**<br>unser**e**<br><span style="color:#f59e0b">**unser<u>en</u> (+ -n)**</span> |
| **6. `ihr` (các bạn)**<br>→ **`euer-`** ⚠️ | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | euer<br>**eur<u>en</u>**<br><span style="color:#f59e0b">**eur<u>em</u>**</span> | **eur<u>e</u>**<br>**eur<u>e</u>**<br><span style="color:#f59e0b">**eur<u>er</u>**</span> | euer<br>euer<br><span style="color:#f59e0b">**eur<u>em</u>**</span> | **eur<u>e</u>**<br>**eur<u>e</u>**<br><span style="color:#f59e0b">**eur<u>en</u> (+ -n)**</span> |
| **7. `sie` (họ)**<br>→ **`ihr-`** | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | ihr<br>ihr**en**<br><span style="color:#f59e0b">**ihr<u>em</u>**</span> | ihr**e**<br>ihr**e**<br><span style="color:#f59e0b">**ihr<u>er</u>**</span> | ihr<br>ihr<br><span style="color:#f59e0b">**ihr<u>em</u>**</span> | ihr**e**<br>ihr**e**<br><span style="color:#f59e0b">**ihr<u>en</u> (+ -n)**</span> |
| **8. `Sie` (Ngài)**<br>→ **`Ihr-`** *(Viết hoa)* | `Nominativ`<br>`Akkusativ`<br>**`Dativ`** | Ihr<br>Ihr**en**<br><span style="color:#f59e0b">**Ihr<u>em</u>**</span> | Ihr**e**<br>Ihr**e**<br><span style="color:#f59e0b">**Ihr<u>er</u>**</span> | Ihr<br>Ihr<br><span style="color:#f59e0b">**Ihr<u>em</u>**</span> | Ihr**e**<br>Ihr**e**<br><span style="color:#f59e0b">**Ihr<u>en</u> (+ -n)**</span> |

---

### HỌC PHẦN 2: CÁC GIỚI TỪ TRONG DATIV (`PRÄPOSITIONEN MIT DATIV` & `WECHSELPRÄPOSITIONEN WO?`)

#### 2.1. Bảng 1: Nhóm Giới Từ LUÔN LUÔN Đi Với Cách 3 (`Reine Dativ-Präpositionen`)
*(Mẹo nhớ nhanh bằng giai điệu: **`mit – nach – aus – zu – von – bei – seit – ab – gegenüber`**)*

| Giới Từ + `Dativ` | Dạng Viết Tắt Bắt Buộc | Ý Nghĩa & Cách Dùng Trọng Tâm | Câu Ví Dụ Đa Ngữ Cảnh (`🔊 de-DE` + Dịch Nghĩa) |
| :---: | :---: | :--- | :--- |
| **`mit`** | *(không có)* | 1. **Cùng với** *(người/vật)*<br>2. **Bằng phương tiện giao thông** (`mit dem Bus / mit der U-Bahn`) | • *„Am Wochenende fährt Anna **mit ihrem Freund** nach München.“* *(Cuối tuần Anna đi tới München cùng bạn trai của cô ấy.)*<br>• *„Fährst du **mit dem Fahrrad** oder **mit der Straßenbahn**?“* *(Bạn đi bằng xe đạp hay bằng tàu điện?)* |
| **`nach`** | *(không có)* | 1. **Đi đến** *(thành phố, quốc gia không mạo từ, châu lục, phương hướng)*<br>2. Cụm cố định: **`nach Hause`** *(đi về nhà)*<br>3. **Sau** *(thời gian: `nach dem Deutschkurs`)* | • *„Im Herbst fliegen meine Eltern **nach Japan**.“* *(Vào mùa thu bố mẹ tôi bay sang Nhật Bản.)*<br>• *„**Nach der Arbeit** gehe ich direkt **nach Hause**.“* *(Sau giờ làm việc tôi đi thẳng về nhà.)* |
| **`aus`** | *(không có)* | 1. **Đến từ** *(quê hương, xuất xứ)*<br>2. **Đi từ bên trong ra khỏi** một không gian kín (`aus dem Haus, aus dem Büro, aus der Schule`) | • *„Unser neuer Kollege kommt **aus der Schweiz**.“* *(Người đồng nghiệp mới của chúng tôi đến từ Thụy Sĩ.)*<br>• *„Um 17 Uhr kommen die Mitarbeiter **aus dem Büro**.“* *(Lúc 17 giờ các nhân viên bước ra khỏi văn phòng.)* |
| **`zu`** | **`zu + dem = zum`**<br>**`zu + der = zur`** | 1. **Đi tới** một địa điểm trong thành phố, cơ quan, tiệm hoặc **tới chỗ một người** (`zum Bahnhof, zur Arbeit, zur Schule, zum Arzt, zu Paul`)<br>2. Cụm cố định: **`zu Hause`** *(đang ở nhà)*, **`zu Fuß`** *(đi bộ)* | • *„Wie komme ich **zum Bahnhof** und **zur Post**?“* *(Tôi đi đến nhà ga và bưu điện bằng cách nào?)*<br>• *„Heute Abend bleibt Herr Weber **zu Hause**, aber morgen geht er **zu Fuß** **zur Arbeit**.“* *(Tối nay ông Weber ở nhà, nhưng ngày mai ông ấy đi bộ đi làm.)* |
| **`von`** | **`von + dem = vom`** | 1. **Từ** *(một địa điểm mở hoặc từ chỗ một người trở về: `vom Bahnhof, vom Arzt, von der Arbeit`)*<br>2. **Của** *(sở hữu: `das Auto von meinem Bruder`)* | • *„Kommst du gerade **vom Supermarkt** oder **von der Bank**?“* *(Bạn vừa mới từ siêu thị hay từ ngân hàng về thế?)*<br>• *„Das Büro **von unserer Chefin** ist im zweiten Stock.“* *(Văn phòng của nữ giám đốc chúng tôi ở tầng hai.)* |
| **`bei`** | **`bei + dem = beim`** | 1. **Ở tại chỗ ai / nhà ai** (`bei meinen Eltern, bei einem Freund`)<br>2. **Làm việc tại công ty nào** (`bei Siemens, bei der Post`)<br>3. **Ở gần địa điểm nào** | • *„Lukas wohnt noch **bei seinen Eltern**.“* *(Lukas vẫn còn sống ở nhà bố mẹ cậu ấy.)*<br>• *„Frau Bui arbeitet **bei einer Bank** in Berlin.“* *(Bà Bùi làm việc tại một ngân hàng ở Berlin.)* |
| **`seit`** / **`ab`** / **`gegenüber`** | *(Mở rộng)* | • **`seit`**: từ khi *(kéo dài đến hiện tại)*<br>• **`ab`**: bắt đầu từ *(mốc thời gian/địa điểm)*<br>• **`gegenüber`**: đối diện với | • *„Die Apotheke liegt **dem Bahnhof gegenüber** (hoặc **gegenüber vom Bahnhof**).“* *(Hiệu thuốc nằm đối diện nhà ga.)* |

---

#### 2.2. Bảng 2: 9 Giới Từ Chỉ Vị Trí (`Lokale Präpositionen`) Với Câu Hỏi `Wo?` *(Ở đâu? → + Dativ)*
> **Quy tắc phân biệt `Wo?` và `Wohin?`**:
> * Khi hỏi **`Wo?` *(Ở đâu?)* → Chỉ vị trí tĩnh tại** (thường đi với các động từ **`sein`** *ở*, **`liegen`** *nằm*, **`stehen`** *đứng*, **`sitzen`** *ngồi*, **`hängen`** *treo*, **`wohnen`** *sống*, **`arbeiten`** *làm việc*) → **BẮT BUỘC CHIA CÁCH 3 (`DATIV`)**!
> * **Các dạng viết tắt chuẩn bắt buộc**:
>   * **`in + dem = im`** (*trong*: `im Büro`, `im ersten Stock`, `im Erdgeschoss`)
>   * **`an + dem = am`** (*sát cạnh / tại*: `am Fenster`, `am Schreibtisch`, `am Bahnhof`)

| STT | Giới Từ Vị Trí | Nghĩa Tiếng Việt & Bản Chất Không Gian | Ví Dụ Trong Văn Phòng / Tòa Nhà (`Wo? + Dativ` — Kèm `🔊 de-DE`) | Dịch Nghĩa Tiếng Việt Chuẩn Xác |
| :---: | :---: | :--- | :--- | :--- |
| **1** | **`in`**<br>*(`in + dem = im`)* | **Ở bên trong** *(một không gian kín 3 chiều: phòng, tòa nhà, túi, thành phố)* | *„Die Mitarbeiter sitzen **im Konferenzraum** (**in dem** Konferenzraum).“* | Các nhân viên đang ngồi **ở trong phòng họp**. |
| **2** | **`auf`** | **Ở trên bề mặt** *(nằm ngang, có tiếp xúc trực tiếp: trên bàn, trên ghế, trên sàn)* | *„Der Laptop und das Telefon stehen **auf dem Schreibtisch**.“* | Chiếc máy tính xách tay và điện thoại bàn nằm **trên bàn làm việc**. |
| **3** | **`unter`** | **Ở phía dưới / dưới gầm** *(thấp hơn vật mốc)* | *„Der Papierkorb steht **unter dem Schreibtisch** und die Katze schläft **unter dem Stuhl**.“* | Sọt rác đặt **dưới gầm bàn làm việc** và con mèo ngủ **dưới gầm ghế**. |
| **4** | **`über`** | **Ở phía trên** *(lơ lửng cao hơn vật mốc, KHÔNG tiếp xúc bề mặt)* | *„Die moderne Lampe hängt **über dem Esstisch**.“* | Chiếc đèn hiện đại treo **phía trên bàn ăn**. |
| **5** | **`an`**<br>*(`an + dem = am`)* | **Ở sát cạnh / tiếp xúc mặt thẳng đứng** *(trên tường, cửa sổ, bảng, bàn làm việc, trạm xe)* | *„Der Kalender hängt **an der Wand** und der Chef sitzt **am Schreibtisch**.“* | Cuốn lịch treo **trên tường** và người sếp đang ngồi **ở bàn làm việc**. |
| **6** | **`vor`** | **Ở phía trước** | *„Das Taxi wartet **vor dem Hotel** und der Bus hält **vor der Schule**.“* | Chiếc taxi đang đợi **phía trước khách sạn** và xe buýt đỗ **phía trước ngôi trường**. |
| **7** | **`hinter`** | **Ở phía sau** | *„Der große Parkplatz liegt **hinter dem Supermarkt**.“* | Bãi đỗ xe lớn nằm **phía sau siêu thị**. |
| **8** | **`neben`** | **Ở bên cạnh** *(sát bên trái hoặc bên phải)* | *„Die Maus liegt **neben der Tastatur** und die Bank ist **neben der Post**.“* | Con chuột máy tính nằm **bên cạnh bàn phím** và ngân hàng ở **bên cạnh bưu điện**. |
| **9** | **`zwischen`** | **Ở giữa hai vật / hai địa điểm** *(Nếu 2 danh từ khác giống, phải chia `Dativ` cho cả hai!)* | *„Das Café liegt **zwischen der Buchhandlung** und **dem Kino**.“* | Quán cà phê nằm **ở giữa hiệu sách** và **rạp chiếu phim**. |

---

### HỌC PHẦN 3: PHƯƠNG TIỆN GIAO THÔNG (`VERKEHRSMITTEL`) & ĐỊNH HƯỚNG TRONG TÒA NHÀ / THÀNH PHỐ

#### 3.1. Bảng Tổng Hợp Các Phương Tiện Giao Thông Theo Giống & Cấu Trúc `mit + Dativ`
> **Câu hỏi phương tiện giao thông**:
> * **`Wie kommst du zur Arbeit / zur Schule / zur Universität?`** *(Bạn đi đến chỗ làm / trường học / trường đại học bằng phương tiện gì?)*
> * **`Womit fährst du nach Berlin?`** *(Bạn đi tới Berlin bằng phương tiện gì?)*
> * **Quy tắc**: Mọi phương tiện giao thông đều dùng **`mit + Dativ`** (`mit dem` cho giống đực & giống trung; `mit der` cho giống cái; `mit den ...-n` cho số nhiều). **Ngoại lệ duy nhất**: **Đi bộ** = **`Ich gehe zu Fuß`** *(tuyệt đối không dùng mit Fuß!)*.

| Nhóm Giống | Danh Từ Nguyên Mẫu (`Nominativ`) | Dạng Số Nhiều (`Plural`) | Nghĩa Tiếng Việt | Cụm Đi Bằng Phương Tiện (`mit + Dativ`) + Động Từ Chuẩn | Câu Ví Dụ Thực Tế Đa Ngôi (`🔊 de-DE` + Dịch Nghĩa) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| <span style="color:#3b82f6">**Giống đực (`der` → `mit dem`)**</span> | **der Bus** | die Busse | xe buýt | **mit dem Bus** fahren | *„Meine Schwester fährt jeden Morgen **mit dem Bus** zur Schule.“* *(Em gái tôi đi đến trường mỗi sáng bằng xe buýt.)* |
| <span style="color:#3b82f6">**Giống đực (`der` → `mit dem`)**</span> | **der Zug** | die Züge | tàu hỏa | **mit dem Zug** fahren | *„Fahren Sie lieber **mit dem Zug** oder mit dem Auto nach München?“* *(Ngài thích đi tới München bằng tàu hỏa hay bằng ô tô hơn?)* |
| <span style="color:#3b82f6">**Giống đực (`der` → `mit dem`)**</span> | **der Pkw / der Wagen** | die Pkws / die Wagen | xe hơi cá nhân | **mit dem Wagen** fahren | *„Herr Müller fährt heute **mit seinem Wagen** ins Büro.“* *(Hôm nay ông Müller lái chiếc xe hơi của ông ấy đến văn phòng.)* |
| <span style="color:#f43f5e">**Giống cái (`die` → `mit der`)**</span> | **die U-Bahn** | die U-Bahnen | tàu điện ngầm | **mit der U-Bahn** fahren | *„In Berlin fahren wir immer **mit der U-Bahn**, das ist sehr schnell.“* *(Ở Berlin chúng tôi luôn đi bằng tàu điện ngầm, nó rất nhanh.)* |
| <span style="color:#f43f5e">**Giống cái (`die` → `mit der`)**</span> | **die S-Bahn** | die S-Bahnen | tàu điện nhanh đô thị | **mit der S-Bahn** fahren | *„Vom Flughafen fährt der Tourist **mit der S-Bahn** ins Stadtzentrum.“* *(Từ sân bay vị khách du lịch đi bằng tàu điện đô thị vào trung tâm thành phố.)* |
| <span style="color:#f43f5e">**Giống cái (`die` → `mit der`)**</span> | **die Straßenbahn**<br>*(/ die Tram)* | die Straßenbahnen | tàu điện mặt đất | **mit der Straßenbahn** fahren | *„Meine Großeltern fahren gern **mit der Straßenbahn** zum Markt.“* *(Ông bà tôi thích đi bằng tàu điện mặt đất ra chợ.)* |
| <span style="color:#f43f5e">**Giống cái (`die` → `mit der`)**</span> | **die Fähre** | die Fähren | phà | **mit der Fähre** fahren | *„Wir fahren **mit der Fähre** auf die Insel.“* *(Chúng tôi đi bằng phà ra đảo.)* |
| <span style="color:#10b981">**Giống trung (`das` → `mit dem`)**</span> | **das Auto** | die Autos | ô tô | **mit dem Auto** fahren | *„Am Sonntag fahren unsere Nachbarn **mit dem Auto** ans Meer.“* *(Vào Chủ nhật những người hàng xóm của chúng tôi đi bằng ô tô ra biển.)* |
| <span style="color:#10b981">**Giống trung (`das` → `mit dem`)**</span> | **das Fahrrad**<br>*(/ **das Rad**)* | die Fahrräder<br>*(/ die Räder)* | xe đạp | **mit dem Fahrrad / mit dem Rad** fahren | *„Bei schönem Wetter fährst du doch gern **mit dem Fahrrad** zur Uni, oder?“* *(Khi thời tiết đẹp bạn thích đi xe đạp tới trường đại học phải không?)* |
| <span style="color:#10b981">**Giống trung (`das` → `mit dem`)**</span> | **das Motorrad** / **das Moped** | die Motorräder / die Mopeds | xe mô tô / xe máy | **mit dem Motorrad / Moped** fahren | *„In Vietnam fahren viele Menschen **mit dem Moped** zur Arbeit.“* *(Ở Việt Nam nhiều người đi làm bằng xe máy.)* |
| <span style="color:#10b981">**Giống trung (`das` → `mit dem`)**</span> | **das Taxi** | die Taxis | xe taxi | **mit dem Taxi** fahren | *„Es ist schon spät. Nehmen wir ein Taxi? — Ja, wir fahren **mit dem Taxi** nach Hause.“* *(Đã muộn rồi. Chúng ta bắt một chiếc taxi nhé? — Ừ, chúng ta đi bằng taxi về nhà.)* |
| <span style="color:#10b981">**Giống trung (`das` → `mit dem`)**</span> | **das Flugzeug** | die Flugzeuge | máy bay | **mit dem Flugzeug** fliegen | *„Fliegt ihr im Sommer **mit dem Flugzeug** nach Spanien?“* *(Mùa hè các bạn có bay bằng máy bay sang Tây Ban Nha không?)* |
| <span style="color:#10b981">**Giống trung (`das` → `mit dem`)**</span> | **das Schiff** | die Schiffe | tàu thủy lớn | **mit dem Schiff** fahren | *„Die Touristen machen eine Reise **mit dem Schiff**.“* *(Những du khách thực hiện một chuyến du hành bằng tàu thủy.)* |
| <span style="color:#f59e0b">**Cụm đặc biệt (Đi bộ)**</span> | **der Fuß** | die Füße | bàn chân → **đi bộ** | **zu Fuß gehen** ⚠️ | *„Die Schule ist gleich neben meinem Haus. Ich gehe immer **zu Fuß**.“* *(Ngôi trường ở ngay cạnh nhà tôi. Tôi luôn đi bộ.)* |

---

#### 3.2. Bảng Từ Vựng Định Hướng Trong Tòa Nhà, Văn Phòng & Thành Phố (`Orientierung im Haus, im Büro & in der Stadt`)
| Chủ Đề | Giống Đực (`der` → Dativ `dem / im / am`) | Giống Cái (`die` → Dativ `der / in der / an der`) | Giống Trung (`das` → Dativ `dem / im`) |
| :--- | :--- | :--- | :--- |
| **Tòa nhà & Tầng lầu (`Im Gebäude`)** | • **der Stock** *(tầng lầu → im 1. Stock)*<br>• **der Aufzug / der Fahrstuhl** *(thang máy)*<br>• **der Eingang** *(lối vào)*<br>• **der Ausgang** *(lối ra)*<br>• **der Flur** *(hành lang)*<br>• **der Keller** *(tầng hầm → im Keller)* | • **die Etage** *(tầng lầu → in der 2. Etage)*<br>• **die Treppe** *(cầu thang bộ)*<br>• **die Rezeption** *(quầy lễ tân → an der Rezeption)*<br>• **die Kantine / die Mensa** *(nhà ăn → in der Kantine)*<br>• **die Toilette** *(nhà vệ sinh)* | • **das Erdgeschoss** *(tầng trệt → **im Erdgeschoss**)*<br>• **das Büro** *(văn phòng → im Büro)*<br>• **das Dachgeschoss** *(tầng áp mái)*<br>• **das Zimmer** *(căn phòng)* |
| **Đồ vật Văn phòng (`Im Büro`)** | • **der Schreibtisch** *(bàn làm việc)*<br>• **der Computer / der Laptop** *(máy tính)*<br>• **der Bildschirm / der Monitor** *(màn hình)*<br>• **der Drucker** *(máy in)*<br>• **der Kalender** *(lịch)*<br>• **der Papierkorb** *(sọt rác)*<br>• **der Konferenzraum** *(phòng họp)* | • **die Tastatur** *(bàn phím)*<br>• **die Maus** *(chuột máy tính)*<br>• **die Kaffeetasse** *(tách cà phê)*<br>• **die Pflanze** *(cây cảnh)*<br>• **die Wand** *(bức tường → an der Wand)*<br>• **die Tür** *(cánh cửa → an der Tür)* | • **das Telefon** *(điện thoại bàn)*<br>• **das Bücherregal** *(giá sách)*<br>• **das Bild** *(bức tranh)*<br>• **das Fenster** *(cửa sổ → am Fenster)*<br>• **das Sofa** *(ghế sofa → auf dem Sofa)* |
| **Địa điểm Thành phố (`In der Stadt`)** | • **der Bahnhof** *(nhà ga → am/zum Bahnhof)*<br>• **der Flughafen** *(sân bay → am/zum Flughafen)*<br>• **der Parkplatz** *(bãi đỗ xe)*<br>• **der Supermarkt** *(siêu thị)*<br>• **der Markt** *(chợ → auf dem Markt)*<br>• **der Park** *(công viên → im Park)* | • **die Haltestelle** *(trạm xe buýt/tàu điện → an der Haltestelle)*<br>• **die Bank** *(ngân hàng)*<br>• **die Post** *(bưu điện → bei/neben der Post)*<br>• **die Bibliothek** *(thư viện)*<br>• **die Buchhandlung** *(hiệu sách)*<br>• **die Apotheke** *(hiệu thuốc)*<br>• **die Kirche** *(nhà thờ)*<br>• **die Polizei** *(đồn cảnh sát)* | • **das Krankenhaus** *(bệnh viện)*<br>• **das Hotel** *(khách sạn)*<br>• **das Café** *(quán cà phê)*<br>• **das Restaurant** *(nhà hàng)*<br>• **das Kino** *(rạp chiếu phim)*<br>• **das Theater** *(nhà hát)*<br>• **das Museum** *(bảo tàng)*<br>• **das Stadtzentrum** *(trung tâm thành phố)* |

---

### HỌC PHẦN 4: SỐ THỨ TỰ (`ORDINALZAHLEN / ORDNUNGSZAHLEN`)

#### 4.1. Quy tắc Cấu tạo Số thứ tự từ Số đếm (`Kardinalzahlen` → `Ordinalzahlen`)
1. **Cách ký hiệu bằng chữ số**: Trong tiếng Đức, khi viết một con số kèm theo **dấu chấm (`.`) ngay phía sau** (ví dụ: **`1.`**, **`2.`**, **`3.`**, **`15.`**, **`20.`**), dấu chấm đó biểu thị đây là **Số thứ tự** (*thứ nhất, thứ hai, thứ ba...*), bắt buộc phải đọc theo đuôi số thứ tự chứ không đọc như số đếm!
2. **Hai nhóm công thức cấu tạo**:
   * **Nhóm 1 — Từ `1.` đến `19.`**:
     $$\text{Số đếm} + \text{\textbf{-te}} \text{ (ở Nominativ sau } der/die/das\text{)} \quad \Big| \quad \text{Số đếm} + \text{\textbf{-ten}} \text{ (ở Dativ sau } am, im, vom, bis\text{ zum)}$$
     * ⚠️ **4 Trường hợp Bất quy tắc bắt buộc thuộc lòng trong nhóm 1–19**:
       1. **`1.`** (`eins` → gốc **`erst-`**): **der/die/das <u>erste</u>** | **am/im <u>ersten</u>** *(thứ nhất / tầng 1 / ngày mùng 1)*
       2. **`3.`** (`drei` → gốc **`dritt-`**): **der/die/das <u>dritte</u>** | **am/im <u>dritten</u>** *(thứ ba / tầng 3 / ngày mùng 3)*
       3. **`7.`** (`sieben` → lược `-en` thành **`siebt-`**): **der/die/das <u>siebte</u>** | **am/im <u>siebten</u>** *(thứ bảy / tầng 7 / ngày mùng 7)*
       4. **`8.`** (`acht` → đã có sẵn `-t` nên chỉ thêm `-e`/`-en` thành **`acht-`**): **der/die/das <u>achte</u>** | **am/im <u>achten</u>** *(thứ tám / tầng 8 / ngày mùng 8)*
   * **Nhóm 2 — Từ `20.` trở đi (`20. -> 31., 100., 1000.`)**:
     $$\text{Số đếm} + \text{\textbf{-ste}} \text{ (ở Nominativ sau } der/die/das\text{)} \quad \Big| \quad \text{Số đếm} + \text{\textbf{-sten}} \text{ (ở Dativ sau } am, im, vom, bis\text{ zum)}$$
     * *Lưu ý với số ghép (ví dụ `21.`, `23.`, `27.`, `28.`)*: Chỉ biến đổi thành số thứ tự ở phần chục phía cuối (`-zwanzigste`), phần hàng đơn vị phía trước vẫn giữ nguyên như số đếm (`einundzwanzigste`, `dreiundzwanzigste`, `siebenundzwanzigste`)!

#### 4.2. Bảng Tham Chiếu Đầy Đủ Số Thứ Tự Từ `1.` Đến `31.` (Ở Cả `Nominativ` Và `Dativ`)
| Ký Hiệu | Số Đếm (`Kardinalzahl`) | Số Thứ Tự Ở `Nominativ`<br>*(der / die / das ...)* | Số Thứ Tự Ở `Dativ`<br>*(am / im / vom / bis zum ...)* | Ứng Dụng Thực Tế (Tầng lầu / Ngày tháng) |
| :---: | :--- | :--- | :--- | :--- |
| **`1.`** ⚠️ | eins | **der/die/das <u>erste</u>** | **am/im <u>ersten</u>** | *im **ersten** Stock (ở tầng 1) / am **ersten** Mai (1/5)* |
| **`2.`** | zwei | **der/die/das zweite** | **am/im zweiten** | *im **zweiten** Stock (ở tầng 2) / der **zweite** Januar (2/1)* |
| **`3.`** ⚠️ | drei | **der/die/das <u>dritte</u>** | **am/im <u>dritten</u>** | *im **dritten** Stock (ở tầng 3) / am **dritten** März (3/3)* |
| **`4.`** | vier | **der/die/das vierte** | **am/im vierten** | *im **vierten** Stock (ở tầng 4) / am **vierten** Juli (4/7)* |
| **`5.`** | fünf | **der/die/das fünfte** | **am/im fünften** | *der **fünfte** Monat ist der Mai (tháng thứ 5 là tháng Năm)* |
| **`6.`** | sechs | **der/die/das sechste** | **am/im sechsten** | *am **sechsten** Dezember (vào ngày 6/12)* |
| **`7.`** ⚠️ | sieben | **der/die/das <u>siebte</u>** | **am/im <u>siebten</u>** | *im **siebten** Stock (ở tầng 7) / am **siebten** Juni (7/6)* |
| **`8.`** ⚠️ | acht | **der/die/das <u>achte</u>** | **am/im <u>achten</u>** | *am **achten** März ist Frauentag (8/3 là ngày Quốc tế Phụ nữ)* |
| **`9.`** | neun | **der/die/das neunte** | **am/im neunten** | *am **neunten** November (vào ngày 9/11)* |
| **`10.`** | zehn | **der/die/das zehnte** | **am/im zehnten** | *im **zehnten** Stock (ở tầng 10)* |
| **`11.`** | elf | **der/die/das elfte** | **am/im elften** | *der **elfte** November (ngày 11/11)* |
| **`12.`** | zwölf | **der/die/das zwölfte** | **am/im zwölften** | *der **zwölfte** Monat ist der Dezember (tháng thứ 12 là tháng 12)* |
| **`13. -> 19.`** | dreizehn → neunzehn | **dreizehnte → neunzehnte** | **dreizehnten → neunzehnten** | *am **fünfzehnten** August (15/8) / am **achtzehnten** April (18/4)* |
| **`20.`** ⚠️ | zwanzig | **der/die/das zwanzig<u>ste</u>** | **am/im zwanzig<u>sten</u>** | *Heute ist der **zwanzigste** Oktober (Hôm nay là ngày 20/10)* |
| **`21.`** | einundzwanzig | **einundzwanzig<u>ste</u>** | **einundzwanzig<u>sten</u>** | *am **einundzwanzigsten** Juni (vào ngày 21/6)* |
| **`22. -> 29.`** | zweiundzwanzig → neunundzwanzig | **...undzwanzig<u>ste</u>** | **...undzwanzig<u>sten</u>** | *am **vierundzwanzigsten** Dezember (vào ngày 24/12)* |
| **`30.`** | dreißig | **der/die/das dreißig<u>ste</u>** | **am/im dreißig<u>sten</u>** | *am **dreißigsten** April (vào ngày 30/4)* |
| **`31.`** | einunddreißig | **einunddreißig<u>ste</u>** | **einunddreißig<u>sten</u>** | *am **einunddreißigsten** Dezember ist Silvester (31/12 là Giao thừa)* |
| **`100.`** | hundert | **der/die/das hundert<u>ste</u>** | **am/im hundert<u>sten</u>** | *der **hundertste** Geburtstag (sinh nhật lần thứ 100)* |

---

### HỌC PHẦN 5: NGÀY – THÁNG – NĂM TRONG TIẾNG ĐỨC (`DAS DATUM & DIE JAHRESZAHLEN`)

#### 5.1. Bảng Ma Trận 3 Cấu Trúc Nói Ngày Tháng Chuẩn Xác (`der + -te/-ste` vs. `am + -ten/-sten` vs. `vom ... bis zum ...`)

| Tình Huống Giao Tiếp | Câu Hỏi Chuẩn (`🔊 de-DE`) | Công Thức Trả Lời & Cách Chia | 2 Cách Đọc Tháng (Bằng Tên Tháng hoặc Bằng Số Thứ Tự Tháng) | Giải Thích Ngữ Pháp |
| :--- | :--- | :--- | :--- | :--- |
| **1. Nói hôm nay là ngày mấy**<br>*(Đóng vai trò vị ngữ sau động từ `sein` → **Cách 1 `Nominativ`**)* | • **Welcher Tag ist heute?**<br>• **Der Wievielte ist heute?**<br>• **Welches Datum haben wir heute?** *(nếu dùng `haben` thì chia `den + -ten`)* | **Heute ist <u>der</u> + `[Số thứ tự -te / -ste]` + `[Tháng]`** | • **`01.05.`**: *Heute ist **der erste Mai**.* (hoặc: *Heute ist **der erste Fünfte**.*)<br>• **`23.11.`**: *Heute ist **der dreiundzwanzigste November**.* (hoặc: *... **der dreiundzwanzigste Elfte**.*) | Sau `Heute ist der ...` là **Cách 1 (`Nominativ`)** nên số thứ tự chỉ mang đuôi **`-te`** (từ 1–19) hoặc **`-ste`** (từ 20 trở đi). |
| **2. Nói một sự kiện diễn ra vào ngày mấy**<br>*(Có giới từ **`am`** = `an + dem` → **Cách 3 `Dativ`**)* | • **Wann hast du Geburtstag?** *(Sinh nhật bạn khi nào?)*<br>• **Wann beginnt der Kurs?**<br>• **Am Wievielten kommst du?** | **<u>Am</u> + `[Số thứ tự -ten / -sten]` + `[Tháng]`** | • **`07.03.`**: *Ich habe **am siebten März** Geburtstag.* (hoặc: ***am siebten Dritten***)<br>• **`28.09.`**: *Der Kurs beginnt **am achtundzwanzigsten September**.* (hoặc: ***am achtundzwanzigsten Neunten***) | Vì **`am`** là viết tắt của `an + dem` (**Cách 3 `Dativ`**), nên mọi số thứ tự đứng sau `am` bắt buộc phải kết thúc bằng **`-ten`** (1–19) hoặc **`-sten`** (từ 20 trở đi). |
| **3. Khoảng thời gian từ ngày ... đến ngày ...**<br>*(Có giới từ **`vom ... bis zum ...`** → Cả 2 vế đều chia **Cách 3 `Dativ`**)* | • **Von wann bis wann haben Sie Urlaub?** *(Ngài nghỉ phép từ khi nào đến khi nào?)*<br>• **Wann ist die Konferenz?** | **<u>vom</u> + `[-ten/-sten]` + <u>bis (zum)</u> + `[-ten/-sten]` + `[Tháng]`** | • **`03.08. – 18.08.`**: *Wir haben **vom dritten bis zum achtzehnten August** Urlaub.*<br>• **`20.12. – 02.01.`**: *Das Büro ist **vom zwanzigsten Dezember bis zum zweiten Januar** geschlossen.* | `vom` = `von + dem` (Dativ) và `zum` = `zu + dem` (Dativ), do đó **cả ngày bắt đầu và ngày kết thúc đều phải thêm đuôi `-n` (`-ten` / `-sten`)**. |

---

#### 5.2. Quy tắc Đọc Năm (`Jahreszahlen`) & Cách Đặt Giới Từ Trước Năm
1. **Cách phân tách đọc số Năm**:
   * **Từ năm `1100` đến `1999`**: Chia đôi thành **2 số đầu (đọc với đơn vị `hundert` = trăm) + 2 số cuối**.
     * `1990` = `19` (*neunzehn*) + `hundert` + `90` (*neunzig*) → **`neunzehnhundertneunzig`**
     * `1995` = `19` (*neunzehn*) + `hundert` + `95` (*fünfundneunzig*) → **`neunzehnhundertfünfundneunzig`**
     * `1989` = `19` (*neunzehn*) + `hundert` + `89` (*neunundachtzig*) → **`neunzehnhundertneunundachtzig`**
     * `1945` = `19` (*neunzehn*) + `hundert` + `45` (*fünfundvierzig*) → **`neunzehnhundertfünfundvierzig`**
   * **Từ năm `2000` trở đi**: Đọc theo hàng nghìn chuẩn (**`zweitausend` + phần số còn lại**).
     * `2000` → **`zweitausend`**
     * `2004` → **`zweitausendvier`**
     * `2015` → **`zweitausendfünfzehn`**
     * `2026` → **`zweitausendsechsundzwanzig`**
2. **Quy tắc Giới từ khi nói *"Vào năm ..."* (Cực kỳ quan trọng)**:
   * **Cách 1 (Phổ biến nhất)**: **KHÔNG dùng giới từ**, đặt trực tiếp con số năm vào câu:
     * *„Mein Bruder ist **1998** in Hanoi geboren.“ (Anh trai tôi sinh năm 1998 tại Hà Nội.)*
   * **Cách 2 (Trang trọng hơn)**: Dùng cụm **`im Jahr + [Năm]`**:
     * *„Meine Eltern haben **im Jahr 1995** geheiratet.“ (Bố mẹ tôi đã kết hôn vào năm 1995.)*
   * ⚠️ **Lỗi cấm tuyệt đối**: Không bao giờ được viết *„in 1998“* hay *„in 2026“* (đó là cấu trúc của tiếng Anh, trong tiếng Đức là sai ngữ pháp!).
3. **Cách nói trọn vẹn cả Ngày – Tháng – Năm sinh (`Geburtsdatum`)**:
   * Câu hỏi: **`Wann bist du geboren?`** *(Bạn sinh khi nào?)* hoặc **`Wann sind Sie geboren?`** *(Ngài sinh khi nào?)*
   * Câu trả lời: **`Ich bin am + [Ngày đuôi -ten/-sten] + [Tháng] + [Năm] + geboren.`**
   * Ví dụ (`15.08.1999`): *„Ich bin **am fünfzehnten August neunzehnhundertneunundneunzig** geboren.“*
   * Ví dụ (`03.10.2002`): *„Meine Tochter ist **am dritten Oktober zweitausendzwei** geboren.“*

---

### HỌC PHẦN 6: HỘI THOẠI THỰC CHIẾN ĐA NGỮ CẢNH (`PRAXIS-DIALOGE` — KÈM AUDIO `de-DE` & PHÂN TÍCH NGỮ PHÁP)

Hiển thị 2 đoạn hội thoại thực tế với nút **`🔊 Nghe từng câu (de-DE)`**, bản dịch tiếng Việt song ngữ và ghi chú giải thích các cấu trúc `Dativ`:

#### Hội thoại 1: Tìm phòng ban trong tòa nhà công ty & Đặt lịch hẹn (`Im Bürogebäude`)
* **Herr Hoàng**: *„Guten Morgen! Entschuldigung, ich suche das Büro **von Frau Schneider**. Wo finde ich sie?“*
  *(Chào buổi sáng! Xin lỗi, tôi đang tìm văn phòng của bà Schneider. Tôi có thể tìm thấy bà ấy ở đâu?)*
* **Rezeptionistin**: *„Guten Morgen! Frau Schneider arbeitet **in der Marketingabteilung**. Ihr Büro ist **im dritten Stock**, gleich **neben dem Konferenzraum**.“*
  *(Chào buổi sáng! Bà Schneider làm việc ở phòng Marketing. Văn phòng của bà ấy nằm ở tầng ba, ngay bên cạnh phòng họp.)*
* **Herr Hoàng**: *„Gibt es hier einen Aufzug?“*
  *(Ở đây có thang máy không?)*
* **Rezeptionistin**: *„Ja, natürlich. Der Aufzug ist dort hinten, **zwischen der Treppe** und **der Kantine** **im Erdgeschoss**. Aber heute haben wir leider ein Problem **mit dem Aufzug**. Sie müssen **über die Treppe** gehen.“*
  *(Vâng, tất nhiên rồi. Thang máy ở phía sau đằng kia, nằm giữa cầu thang bộ và nhà ăn ở tầng trệt. Nhưng hôm nay rất tiếc chúng tôi đang có sự cố với chiếc thang máy. Ngài phải đi bằng cầu thang bộ.)*
* **Herr Hoàng**: *„Kein Problem, ich gehe gern **zu Fuß**. Unser Termin ist **am zwölften Mai** um 10 Uhr.“*
  *(Không sao cả, tôi thích đi bộ. Cuộc hẹn của chúng tôi là vào ngày 12 tháng Năm lúc 10 giờ.)*

#### Hội thoại 2: Hỏi đường & Phương tiện di chuyển trong thành phố (`In der Stadt & Verkehrsmittel`)
* **Touristin (Maria)**: *„Entschuldigen Sie bitte, wie komme ich **vom Hauptbahnhof** **zum Stadtmuseum**?“*
  *(Xin lỗi Ngài làm ơn cho hỏi, tôi đi từ nhà ga trung tâm đến bảo tàng thành phố bằng cách nào?)*
* **Passant (Lukas)**: *„Das Stadtmuseum liegt **im Zentrum**, direkt **vor dem großen Park** und **neben einer alten Kirche**. Sie können **mit der U-Bahn** oder **mit dem Bus** fahren.“*
  *(Bảo tàng thành phố nằm ở trung tâm, ngay phía trước công viên lớn và bên cạnh một nhà thờ cổ. Cô có thể đi bằng tàu điện ngầm hoặc bằng xe buýt.)*
* **Touristin (Maria)**: *„Und wo ist die Haltestelle?“*
  *(Và trạm dừng ở đâu ạ?)*
* **Passant (Lukas)**: *„Die Bushaltestelle ist gleich dort **vor der Bank**, **zwischen dem Hotel** und **der Post**. Meine Kollegen und ich fahren jeden Tag **mit den Bussen** zur Arbeit.“*
  *(Trạm xe buýt ở ngay đằng kia phía trước ngân hàng, ở giữa khách sạn và bưu điện. Các đồng nghiệp của tôi và tôi đi làm mỗi ngày bằng những chiếc xe buýt đó.)*

---

## PHẦN 3: KHO 100 BÀI TẬP ĐA DẠNG HÓA CỦA BÀI 6 (`lessons/a1/seed_a1_b6.py`) & BỘ RANDOM ĐỔI ĐỀ ĐA CHIỀU

Theo đúng yêu cầu của người dùng, quy mô bài tập của **Bài 6** được nâng lên **100 câu hỏi (`100 Exercises`)** chia đều cho **9 dạng bài tập tương tác**. Đặc biệt, các câu hỏi phải **đa dạng hóa chủ ngữ (`ich, du, er, sie, es, wir, ihr, sie, Sie`, tên riêng, danh từ gia đình/nghề nghiệp)**, **đa dạng hóa ngữ cảnh**, và tích hợp **Bộ Sinh Đề Động (`Dynamic Multi-Variable Randomizer`)** để mỗi lần người học vào làm hoặc bấm **`🔄 Đổi đề khác`** thì các con số, ngày tháng năm, tầng lầu, phương tiện giao thông, chủ ngữ và vị trí đồ vật đều thay đổi linh hoạt mà vẫn khớp đáp án – dịch nghĩa – giải thích 100%!

### 3.1. Bảng Phân Bổ 100 Câu Hỏi Bài 6 Theo 9 Dạng Bài Tập

| STT | Mã Dạng (`type`) | Tên Dạng Bài Tập Hiển Thị | Số Lượng | Nội Dung Trọng Tâm Đa Ngữ Cảnh Trong Bài 6 |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **`trac_nghiem`** | **Trắc nghiệm (Multiple Choice)** | **18 câu** | • Biến đổi mạo từ xác định/không xác định/phủ định ở `Dativ` (`dem, der, den + -n`)<br>• Mạo từ sở hữu ở `Dativ` với đủ 9 ngôi (`meinem, deiner, seinem, ihrer, unserem, eurem, Ihrem`)<br>• Giới từ `mit, nach, aus, zu (zum/zur), von (vom), bei (beim)`<br>• 9 giới từ vị trí `Wo? + Dativ` (`in, an, auf, neben, vor, hinter, über, unter, zwischen`)<br>• Phương tiện giao thông & động từ `fahren / fliegen / zu Fuß gehen`<br>• Số thứ tự (`erste, dritte, siebte, achte, zwanzigste`) & Ngày tháng năm (`der erste Mai` vs. `am ersten Mai` vs. `vom ... bis zum ...`). |
| **2** | **`dien_khuyet`** | **Điền khuyết (Fill in the Blank)** | **15 câu** | • Điền mạo từ `Dativ` hoặc đuôi sở hữu (`-em, -er, -en`)<br>• Điền giới từ thu gọn (`im, am, zum, zur, vom, beim`)<br>• Điền dạng số thứ tự đúng của ngày tháng và tầng lầu (`ersten, dritten, siebten, achten, zwanzigsten...`)<br>• Điền dạng chia đúng của động từ biến âm (`fährst, fährt, hilft, gefällt`). |
| **3** | **`dich_nghia_vd`** | **Dịch từ/cụm từ: Việt → Đức** | **12 câu** | Dịch các phương tiện giao thông (`bằng tàu điện ngầm, bằng máy bay, đi bộ...`), địa điểm/tòa nhà (`ở tầng trệt, ở tầng ba, trạm xe buýt, thang máy...`), cụm ngày tháng (`vào ngày 8 tháng 3, từ ngày 2 đến ngày 15...`) sang tiếng Đức. |
| **4** | **`dich_nghia_dv`** | **Dịch từ/cụm từ: Đức → Việt** | **12 câu** | Dịch các cụm giới từ `Dativ`, vị trí đồ vật trên bàn làm việc, số thứ tự và ngày tháng năm sang tiếng Việt (`mit der Straßenbahn, im Erdgeschoss, zwischen dem Stuhl und dem Schreibtisch, am einundzwanzigsten Juni...`). |
| **5** | **`noi_o`** | **Nối ô từ trái qua phải (Matching Pairs)** | **10 bài** | 10 bài ghép cặp (mỗi bài 4 cặp = 40 mệnh đề):<br>• Bài 1: Nối Giống ở Nominativ $\leftrightarrow$ Dạng mạo từ ở Dativ (`der -> dem`, `die -> der`, `das -> dem`, `die Pl -> den + -n`)<br>• Bài 2: Nối Giới từ + Mạo từ $\leftrightarrow$ Dạng viết tắt (`zu + dem -> zum`, `zu + der -> zur`, `von + dem -> vom`, `bei + dem -> beim`)<br>• Bài 3: Nối Phương tiện $\leftrightarrow$ Cụm `mit + Dativ` (`die U-Bahn -> mit der U-Bahn`, `das Flugzeug -> mit dem Flugzeug`, `der Zug -> mit dem Zug`, `der Fuß -> zu Fuß`)<br>• Bài 4: Nối Số đếm $\leftrightarrow$ Số thứ tự bất quy tắc (`eins -> erste`, `drei -> dritte`, `sieben -> siebte`, `zwanzig -> zwanzigste`)<br>• Bài 5: Nối Vị trí tiếng Đức $\leftrightarrow$ Nghĩa tiếng Việt (`auf dem Tisch`, `unter dem Stuhl`, `über dem Sofa`, `hinter dem Haus`)<br>• Bài 6: Nối Câu hỏi định hướng $\leftrightarrow$ Câu trả lời chuẩn (`Wo? / Wohin? / Womit? / Wann?`)<br>• Bài 7: Nối Mốc ngày số $\leftrightarrow$ Cách đọc sau `am` (`am 1.5. -> am ersten Mai`, `am 3.8. -> am dritten August`, `am 7.10. -> am siebten Oktober`, `am 20.12. -> am zwanzigsten Dezember`)<br>• Bài 8: Nối Năm số $\leftrightarrow$ Cách đọc chữ (`1995`, `1989`, `2004`, `2026`)<br>• Bài 9: Nối Đại từ nhân xưng $\leftrightarrow$ Mạo từ sở hữu ở Dativ (`ich -> meinem/meiner`, `wir -> unserem/unserer`, `ihr -> eurem/eurer`, `er -> seinem/seiner`)<br>• Bài 10: Nối Địa điểm thành phố $\leftrightarrow$ Hoạt động tương ứng (`am Bahnhof, an der Haltestelle, in der Kantine, an der Rezeption`). |
| **6** | **`dien_tao_cau`** | **Điền vào chỗ trống để tạo thành câu** | **10 câu** | Điền 2–3 vị trí ngữ pháp trong câu phức hợp (kết hợp chia động từ `fährt/fliegt/steht/hängt` + giới từ `Dativ` + mạo từ sở hữu / số thứ tự) với đa dạng chủ ngữ (`du, er, sie, wir, ihr, meine Eltern, die Kinder`). |
| **7** | **`nghe_dien`** | **Nghe giọng đọc `de-DE` và điền từ** | **9 câu** | Nghe câu phát âm chuẩn `de-DE` (hỗ trợ cả `1.0x` và `0.65x`) và điền từ chính xác: nghe phương tiện giao thông (`Straßenbahn`, `Flugzeug`), nghe vị trí tầng lầu (`Erdgeschoss`, `dritten`), nghe giới từ vị trí (`zwischen`, `hinter`), nghe ngày tháng năm sinh (`fünfzehnten`, `zwanzigsten`, `Kinder`). |
| **8** | **`dich_cau_vd`** | **Dịch câu: Việt → Đức** | **7 câu** | Dịch câu hoàn chỉnh đa chủ ngữ từ tiếng Việt sang tiếng Đức (chấm linh hoạt đa đáp án): câu về phương tiện giao thông, vị trí đồ vật trên bàn làm việc, địa điểm trong thành phố, tầng lầu và ngày tháng năm sinh. |
| **9** | **`dich_cau_dv`** | **Dịch câu: Đức → Việt** | **7 câu** | Dịch câu hoàn chỉnh từ tiếng Đức sang tiếng Việt (chấm linh hoạt đa đáp án): câu có mạo từ sở hữu ở Dativ, số nhiều thêm `-n` ở Dativ, khoảng ngày `vom ... bis zum ...`, và vị trí trong tòa nhà. |
| | | **TỔNG CỘNG BÀI 6** | **100 CÂU** | **Đầy đủ 9 dạng bài + Đa dạng hóa Ngôi/Số/Ngữ cảnh + QA 100%** |

---

### 3.2. Danh Sách Chi Tiết 100 Câu Hỏi Chuẩn Xác Của Bài 6 (Để Seed Vào `lessons/a1/seed_a1_b6.py`)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 18 Câu: Câu 1 → Câu 18)
1. **Câu 1 (Phương tiện giống cái `die` ở Dativ)**: Chọn cụm từ đúng để hoàn thành câu: *„Meine Mutter fährt jeden Morgen ___ zur Arbeit.“* *(Gợi ý: `die Straßenbahn` - tàu điện mặt đất)*
   * Đáp án: `A. mit die Straßenbahn` | `B. mit der Straßenbahn` (Đúng) | `C. mit dem Straßenbahn` | `D. mit den Straßenbahn`
   * Dịch nghĩa câu: *"Mẹ tôi đi làm mỗi buổi sáng bằng tàu điện mặt đất."*
   * Giải thích: Giới từ `mit` luôn đi với Cách 3 (`Dativ`). Danh từ `die Straßenbahn` mang giống cái (`Femininum`), nên ở `Dativ` mạo từ `die` biến đổi thành `der` → `mit der Straßenbahn`.
2. **Câu 2 (Phương tiện giống trung `das` & Động từ biến âm `fahren`)**: Chọn phương án đúng điền vào 2 chỗ trống: *„Womit ___ dein Bruder zur Universität? — Er ___ ___ Fahrrad.“*
   * Đáp án: `A. fährt / fährt mit dem` (Đúng) | `B. fahrst / fährt mit das` | `C. fährt / fahrt mit einem` | `D. fahren / fährt zu dem`
   * Dịch nghĩa câu: *"Anh trai của bạn đi đến trường đại học bằng phương tiện gì? — Anh ấy đi bằng xe đạp."*
   * Giải thích: Chủ ngữ `dein Bruder` (= ngôi `er`) nên động từ `fahren` biến âm `a -> ä` thành `fährt`. Danh từ `das Fahrrad` mang giống trung nên sau `mit` (`Dativ`) biến đổi thành `mit dem Fahrrad`.
3. **Câu 3 (Trường hợp đặc biệt: Đi bộ)**: Chọn cách diễn đạt đúng nhất: *„Die Schule liegt direkt neben unserem Haus. Deshalb gehen die Kinder immer ___.“*
   * Đáp án: `A. mit dem Fuß` | `B. mit den Füßen` | `C. zu Fuß` (Đúng) | `D. auf dem Fuß`
   * Dịch nghĩa câu: *"Ngôi trường nằm ngay bên cạnh nhà chúng tôi. Vì vậy bọn trẻ luôn đi bộ."*
   * Giải thích: Khác với các phương tiện dùng `mit + Dativ`, cụm từ cố định chỉ việc *"đi bộ"* trong tiếng Đức là **`zu Fuß gehen`**.
4. **Câu 4 (Danh từ Số nhiều ở `Dativ` bắt buộc thêm `-n`)**: Chọn đáp án đúng ngữ pháp Cách 3 (`Dativ`): *„Am Wochenende macht Herr Wagner einen Ausflug mit ___.“* *(Gợi ý: `seine Kinder` - các con của ông ấy)*
   * Đáp án: `A. seine Kinder` | `B. seinen Kinder` | `C. seinen Kindern` (Đúng) | `D. seinem Kindern`
   * Dịch nghĩa câu: *"Vào cuối tuần ông Wagner đi dã ngoại cùng với các con của ông ấy."*
   * Giải thích: Sau giới từ `mit` là Cách 3 (`Dativ`). Ở dạng số nhiều (`Plural`), mạo từ sở hữu `seine` đổi thành `seinen` **và danh từ số nhiều `Kinder` bắt buộc phải cộng thêm đuôi `-n`** thành **`seinen Kindern`**.
5. **Câu 5 (Mạo từ sở hữu ngôi `ihr - các bạn` ở `Dativ`)**: Chọn dạng mạo từ sở hữu đúng: *„Kinder, wohnt ihr noch bei ___ Eltern oder habt ihr schon eine eigene Wohnung?“*
   * Đáp án: `A. eure` | `B. eurem` | `C. eurer` | `D. euren` (Đúng)
   * Dịch nghĩa câu: *"Các con ơi, các con vẫn còn sống ở nhà bố mẹ của các con hay là đã có một căn hộ riêng rồi?"*
   * Giải thích: Chủ ngữ đang được hỏi là `ihr` (các bạn/các con) → gốc sở hữu là `euer`. Đi sau giới từ `bei` (+ `Dativ`) và trước danh từ số nhiều `Eltern`, `euer` thêm đuôi `-en` và lược chữ `e` ở giữa thành **`euren Eltern`**.
6. **Câu 6 (Mạo từ sở hữu ngôi `wir` với danh từ giống cái ở `Dativ`)**: Chọn đáp án đúng: *„Das Geschenk auf dem Tisch ist von ___ Lehrerin.“* *(của cô giáo chúng tôi)*
   * Đáp án: `A. unsere` | `B. unserer` (Đúng) | `C. unserem` | `D. unseren`
   * Dịch nghĩa câu: *"Món quà ở trên bàn là của cô giáo chúng tôi."*
   * Giải thích: Sau giới từ `von` là Cách 3 (`Dativ`). Danh từ `die Lehrerin` mang giống cái (`Femininum`), nên gốc sở hữu `unser` (của chúng tôi) nhận đuôi `-er` thành **`unserer Lehrerin`**.
7. **Câu 7 (Phân biệt `zu`, `nach`, `in` khi chỉ hướng đến)**: Chọn giới từ đúng: *„Nach dem Frühstück fährt Frau Weber zuerst ___ Bahnhof und dann mit dem ICE ___ Frankfurt.“*
   * Đáp án: `A. nach / zu` | `B. zum / nach` (Đúng) | `C. zur / in` | `D. im / nach`
   * Dịch nghĩa câu: *"Sau bữa sáng bà Weber trước tiên đi đến nhà ga rồi sau đó đi bằng tàu cao tốc ICE tới Frankfurt."*
   * Giải thích: Đi tới một địa điểm cụ thể trong thành phố (`der Bahnhof`) dùng `zu + dem = zum Bahnhof`. Đi tới một thành phố không có mạo từ (`Frankfurt`) dùng giới từ `nach` (`nach Frankfurt`).
8. **Câu 8 (Phân biệt `zu Hause`, `nach Hause` và `von zu Hause`)**: Chọn cặp từ đúng điền vào câu: *„Am Sonntag bleibe ich den ganzen Tag ___, aber am Montag gehe ich um 18 Uhr von der Arbeit ___.“*
   * Đáp án: `A. nach Hause / zu Hause` | `B. zu Hause / nach Hause` (Đúng) | `C. im Haus / zum Haus` | `D. bei Hause / nach Hause`
   * Dịch nghĩa câu: *"Vào Chủ nhật tôi ở nhà cả ngày, nhưng vào thứ Hai tôi đi từ chỗ làm về nhà lúc 18 giờ."*
   * Giải thích: **`zu Hause`** chỉ trạng thái tĩnh *(đang ở nhà - Wo?)*, còn **`nach Hause`** chỉ sự di chuyển *(đi về nhà - Wohin?)*.
9. **Câu 9 (Giới từ vị trí `zwischen` với 2 danh từ khác giống ở `Dativ`)**: Chọn phương án đúng: *„Wo liegt die neue Buchhandlung? — Sie liegt direkt zwischen ___ Supermarkt und ___ Post.“* *(Gợi ý: `der Supermarkt` & `die Post`)*
   * Đáp án: `A. den / die` | `B. dem / der` (Đúng) | `C. der / dem` | `D. einem / eine`
   * Dịch nghĩa câu: *"Hiệu sách mới nằm ở đâu? — Nó nằm ngay giữa siêu thị và bưu điện."*
   * Giải thích: Câu hỏi `Wo?` với giới từ `zwischen` đòi hỏi cả 2 danh từ phía sau đều phải chia ở Cách 3 (`Dativ`): `der Supermarkt` (giống đực) → **`dem Supermarkt`**; `die Post` (giống cái) → **`der Post`**.
10. **Câu 10 (Phân biệt `auf` và `über` / `an` khi miêu tả phòng làm việc)**: Chọn giới từ vị trí đúng: *„Der schwere Drucker steht ___ dem Schreibtisch, und das schöne Familienfoto hängt ___ der Wand.“*
    * Đáp án: `A. über / auf` | `B. auf / an` (Đúng) | `C. an / in` | `D. unter / neben`
    * Dịch nghĩa câu: *"Chiếc máy in nặng đặt ở trên mặt bàn làm việc, và bức ảnh gia đình đẹp đẽ treo ở trên tường."*
    * Giải thích: Đặt tiếp xúc trên bề mặt nằm ngang (`der Schreibtisch`) dùng **`auf dem Schreibtisch`**; treo tiếp xúc trên bề mặt thẳng đứng (`die Wand` - giống cái) dùng **`an der Wand`**.
11. **Câu 11 (Vị trí tầng lầu `im Erdgeschoss` và `im ... Stock`)**: Chọn câu trả lời đúng ngữ pháp: *„Wo befindet sich die Kantine in Ihrer Firma? — Sie liegt ___ Erdgeschoss, und mein Büro ist ___ dritten Stock.“*
    * Đáp án: `A. im / im` (Đúng) | `B. am / am` | `C. in der / im` | `D. auf dem / in der`
    * Dịch nghĩa câu: *"Nhà ăn trong công ty của Ngài nằm ở đâu? — Nó nằm ở tầng trệt, còn văn phòng của tôi ở tầng ba."*
    * Giải thích: Cả `das Erdgeschoss` (giống trung) và `der Stock` (giống đực) khi chỉ vị trí `Wo?` đều dùng `in + dem = im`: **`im Erdgeschoss`** và **`im dritten Stock`**.
12. **Câu 12 (Số thứ tự bất quy tắc `1., 3., 7., 8.`)**: Dãy số thứ tự nào sau đây được viết **ĐÚNG HOÀN TOÀN** cho các mốc **`1. — 3. — 7. — 8.`** ở Cách 1 (`Nominativ`)?
    * Đáp án: `A. der einsigste — der dreite — der siebente — der achtte` | `B. der erste — der dritte — der siebte — der achte` (Đúng) | `C. der erste — der dreite — der siebte — der achte` | `D. der ersten — der dritten — der siebten — der achten`
    * Dịch nghĩa câu: *"Thứ nhất — Thứ ba — Thứ bảy — Thứ tám."*
    * Giải thích: Bốn số thứ tự bất quy tắc từ 1 đến 19 ở `Nominativ` là: `1. -> erste`, `3. -> dritte`, `7. -> siebte` (bỏ `-en`), `8. -> achte` (chỉ có một chữ `t`).
13. **Câu 13 (Số thứ tự từ 20 trở đi)**: Số thứ tự của **`23.`** sau mạo từ `der` ở Cách 1 (`Nominativ`) được viết như thế nào?
    * Đáp án: `A. derdreiundzwanzigste` | `B. der dritteundzwanzigste` | `C. der dreiundzwanzigste` (Đúng) | `D. der dreiundzwanzigsten`
    * Dịch nghĩa câu: *"Thứ hai mươi ba (ngày 23)."*
    * Giải thích: Từ 20 trở đi, số thứ tự được tạo bằng cách thêm đuôi **`-ste`** vào cuối số đếm: `dreiundzwanzig` + `-ste` → **`der dreiundzwanzigste`** (phần hàng đơn vị `drei` ở đầu giữ nguyên, không đổi thành *dritte*).
14. **Câu 14 (Phân biệt `der + -te/-ste` và `am + -ten/-sten` khi nói Ngày tháng)**: Chọn cặp từ đúng cho cuộc hội thoại: *„Welcher Tag ist heute? — Heute ist der ___ Oktober (`20.10.`). Und wann fliegt ihr nach Wien? — Wir fliegen am ___ Oktober (`25.10.`).“*
    * Đáp án: `A. zwanzigsten / fünfundzwanzigste` | `B. zwanzigste / fünfundzwanzigsten` (Đúng) | `C. zwanzig / fünfundzwanzig` | `D. zwanzigster / fünfundzwanzigster`
    * Dịch nghĩa câu: *"Hôm nay là ngày mấy? — Hôm nay là ngày 20 tháng Mười. Và khi nào các bạn bay đi Viên? — Chúng tôi bay vào ngày 25 tháng Mười."*
    * Giải thích: Sau `Heute ist der ...` (`Nominativ`) dùng đuôi **`-ste`** (`der zwanzigste Oktober`). Sau giới từ `am` (`Dativ`) bắt buộc phải thêm `-n` thành đuôi **`-sten`** (`am fünfundzwanzigsten Oktober`).
15. **Câu 15 (Khoảng ngày `vom ... bis zum ...`)**: Chọn phương án đúng để diễn đạt *"từ ngày 01/07 đến ngày 14/07"*: *„Unsere Kollegen haben ___ Juli Sommerurlaub.“*
    * Đáp án: `A. von ersten bis vierzehnte` | `B. vom erste bis zum vierzehnte` | `C. vom ersten bis zum vierzehnten` (Đúng) | `D. am ersten bis am vierzehnten`
    * Dịch nghĩa câu: *"Các đồng nghiệp của chúng tôi có kỳ nghỉ hè từ ngày mùng 1 đến ngày 14 tháng Bảy."*
    * Giải thích: Trong cấu trúc `vom ... bis zum ...`, cả `vom` (`von + dem`) và `zum` (`zu + dem`) đều ở Cách 3 (`Dativ`), nên cả hai số thứ tự đều phải chia đuôi **`-ten`** (`vom ersten bis zum vierzehnten Juli`).
16. **Câu 16 (Cách đọc Năm trước năm 2000 và giới từ với Năm)**: Câu nào dưới đây viết và đọc **ĐÚNG** nghĩa *"Bố tôi sinh năm 1968 tại Hải Phòng"*?
    * Đáp án: `A. Mein Vater ist in 1968 (neunzehnhundertachtundsechzig) in Hai Phong geboren.` | `B. Mein Vater ist 1968 (neunzehnhundertachtundsechzig) in Hai Phong geboren.` (Đúng) | `C. Mein Vater ist am 1968 (tausendneunhundertachtundsechzig) in Hai Phong geboren.` | `D. Mein Vater war im 1968 in Hai Phong geboren.`
    * Dịch nghĩa câu: *"Bố tôi sinh năm 1968 tại Hải Phòng."*
    * Giải thích: Trong tiếng Đức, khi chỉ năm đơn lẻ, ta viết trực tiếp số năm (`1968`) hoặc dùng `im Jahr 1968` (tuyệt đối không dùng `in 1968` hay `am 1968`). Năm `1968` đọc theo hàng trăm là `neunzehnhundertachtundsechzig`.
17. **Câu 17 (Động từ đi với `Dativ`: `helfen` & `gefallen`)**: Chọn phương án đúng hoàn thành câu: *„Paula, ___ du bitte ___ Großmutter in der Küche?“*
    * Đáp án: `A. helfst / die` | `B. hilfst / deiner` (Đúng) | `C. hilft / deine` | `D. helfe / deinem`
    * Dịch nghĩa câu: *"Paula ơi, bạn làm ơn giúp bà của bạn ở trong bếp nhé?"*
    * Giải thích: Động từ `helfen` biến âm `e -> i` ở ngôi `du` thành **`hilfst`**, và đòi hỏi tân ngữ ở Cách 3 (`Dativ`). Vì `die Großmutter` mang giống cái nên `deine` đổi thành **`deiner Großmutter`**.
18. **Câu 18 (Tổng hợp định hướng & thời gian)**: Chọn câu hoàn chỉnh đúng ngữ pháp 100%:
    * Đáp án:
      * `A. Am drittem Mai fahren wir mit den Zug zu unseren Freunden.`
      * `B. Am dritten Mai fahren wir mit dem Zug zu unseren Freunden.` (Đúng)
      * `C. Im dritten Mai fahren wir mit dem Zug nach unseren Freunden.`
      * `D. Am dritte Mai fährt wir mit der Zug bei unseren Freunde.`
    * Dịch nghĩa câu: *"Vào ngày mùng 3 tháng Năm, chúng tôi đi bằng tàu hỏa tới chỗ những người bạn của chúng tôi."*
    * Giải thích: Ngày cụ thể dùng `Am dritten Mai`; phương tiện `der Zug` dùng `mit dem Zug`; đi tới chỗ người dùng `zu + Dativ số nhiều` là `zu unseren Freunden` (danh từ `Freunde` thêm `-n`).

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 15 Câu: Câu 19 → Câu 33)
19. **Câu 19**: Điền giới từ thu gọn thích hợp (`zu + der`) vào chỗ trống: *„Jeden Morgen geht mein Sohn um 7 Uhr zu Fuß ___ Schule.“*
    * Đáp án chấp nhận: `["zur"]`
    * Dịch nghĩa câu: *"Mỗi buổi sáng con trai tôi đi bộ đến trường lúc 7 giờ."*
    * Giải thích: `die Schule` mang giống cái; đi đến trường dùng `zu + der Schule` viết tắt bắt buộc thành **`zur Schule`**.
20. **Câu 20**: Điền giới từ thu gọn thích hợp (`von + dem`) vào chỗ trống: *„Wann kommt deine Schwester heute Abend ___ Flughafen zurück?“*
    * Đáp án chấp nhận: `["vom"]`
    * Dịch nghĩa câu: *"Tối nay khi nào chị gái của bạn từ sân bay trở về?"*
    * Giải thích: Từ một địa điểm trở về dùng giới từ `von` + `Dativ`; `der Flughafen` mang giống đực nên `von + dem` viết tắt thành **`vom Flughafen`**.
21. **Câu 21**: Điền giới từ thu gọn thích hợp (`bei + dem`) vào chỗ trống: *„Gestern war mein Großvater zwei Stunden ___ Arzt.“*
    * Đáp án chấp nhận: `["beim"]`
    * Dịch nghĩa câu: *"Hôm qua ông của tôi đã ở chỗ bác sĩ hai tiếng đồng hồ."*
    * Giải thích: Ở chỗ bác sĩ (`der Arzt`) dùng `bei + dem Arzt` viết tắt thành **`beim Arzt`**.
22. **Câu 22**: Điền mạo từ xác định đúng ở Cách 3 (`Dativ`) vào chỗ trống: *„Warum sitzt der Hund immer unter ___ Esstisch?“* *(Gợi ý: `der Esstisch`)*
    * Đáp án chấp nhận: `["dem"]`
    * Dịch nghĩa câu: *"Tại sao chú chó luôn ngồi ở dưới gầm bàn ăn thế?"*
    * Giải thích: Câu chỉ vị trí tĩnh (`sitzt` — `Wo?`) sau giới từ `unter` chia ở `Dativ`. `der Esstisch` (giống đực) đổi thành **`unter dem Esstisch`**.
23. **Câu 23**: Điền mạo từ sở hữu đúng của ngôi `er` (`sein-`) ở Cách 3 (`Dativ`) vào chỗ trống: *„Peter spricht gerade im Flur mit ___ Chefin.“* *(Gợi ý: `die Chefin` - nữ giám đốc)*
    * Đáp án chấp nhận: `["seiner"]`
    * Dịch nghĩa câu: *"Peter đang nói chuyện ở ngoài hành lang với nữ giám đốc của anh ấy."*
    * Giải thích: Sau giới từ `mit` là `Dativ`. Danh từ `die Chefin` mang giống cái, nên gốc sở hữu `sein-` của Peter (`er`) thêm đuôi `-er` thành **`seiner Chefin`**.
24. **Câu 24**: Điền mạo từ sở hữu đúng của ngôi `Sie` (`Ihr-` viết hoa) ở Cách 3 (`Dativ`) vào chỗ trống: *„Herr Direktor, der Brief liegt auf ___ Schreibtisch neben dem Laptop.“* *(Gợi ý: `der Schreibtisch`)*
    * Đáp án chấp nhận: `["Ihrem"]`
    * Dịch nghĩa câu: *"Thưa Ngài Giám đốc, bức thư nằm ở trên bàn làm việc của Ngài bên cạnh chiếc máy tính xách tay."*
    * Giải thích: `der Schreibtisch` mang giống đực, ở `Dativ` sau giới từ `auf` thì mạo từ sở hữu của ngôi `Sie` là **`Ihrem Schreibtisch`**.
25. **Câu 25**: Điền dạng đúng của danh từ số nhiều `die Freunde` (những người bạn) ở Cách 3 (`Dativ`) vào chỗ trống: *„Am Samstag gehen wir mit unseren ___ ins Kino.“*
    * Đáp án chấp nhận: `["Freunden"]`
    * Dịch nghĩa câu: *"Vào thứ Bảy chúng tôi đi xem phim cùng với những người bạn của chúng tôi."*
    * Giải thích: Ở Cách 3 (`Dativ`) số nhiều, danh từ `die Freunde` bắt buộc phải thêm đuôi **`-n`** thành **`Freunden`**.
26. **Câu 26**: Điền dạng chia đúng của động từ `fahren` theo chủ ngữ vào chỗ trống: *„Frau Kien, wann ___ der nächste Bus zum Hauptbahnhof?“*
    * Đáp án chấp nhận: `["fährt", "faehrt"]`
    * Dịch nghĩa câu: *"Bà Kiên ơi, khi nào chuyến xe buýt tiếp theo chạy tới nhà ga trung tâm vậy?"*
    * Giải thích: Chủ ngữ của câu hỏi là `der nächste Bus` (ngôi thứ 3 số ít `er`), nên động từ `fahren` biến âm `a -> ä` thành **`fährt`**.
27. **Câu 27**: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: *„Die Personalabteilung befindet sich im ___ (1.) Stock.“*
    * Đáp án chấp nhận: `["ersten"]`
    * Dịch nghĩa câu: *"Phòng nhân sự nằm ở tầng một."*
    * Giải thích: Đi sau giới từ `im` (`in + dem` — `Dativ`), số thứ tự `1.` (`erste`) phải thêm đuôi `-n` thành **`im ersten Stock`**.
28. **Câu 28**: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: *„Unsere neue Wohnung liegt im ___ (7.) Stock.“*
    * Đáp án chấp nhận: `["siebten"]`
    * Dịch nghĩa câu: *"Căn hộ mới của chúng tôi nằm ở tầng bảy."*
    * Giải thích: Số thứ tự của `7` là bất quy tắc (`siebte`), đi sau `im` (`Dativ`) thêm `-n` thành **`im siebten Stock`**.
29. **Câu 29**: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: *„Welcher Tag ist heute? — Heute ist der ___ (3.) April.“*
    * Đáp án chấp nhận: `["dritte"]`
    * Dịch nghĩa câu: *"Hôm nay là ngày mấy? — Hôm nay là ngày mùng 3 tháng Tư."*
    * Giải thích: Sau `Heute ist der ...` là Cách 1 (`Nominativ`), nên số thứ tự `3.` chia là **`der dritte April`** (không có `-n`).
30. **Câu 30**: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: *„Wann hat deine Mutter Geburtstag? — Sie hat am ___ (8.) März Geburtstag.“*
    * Đáp án chấp nhận: `["achten"]`
    * Dịch nghĩa câu: *"Mẹ của bạn có sinh nhật vào khi nào? — Bà ấy có sinh nhật vào ngày mùng 8 tháng Ba."*
    * Giải thích: Số thứ tự của `8` là `achte` (chỉ có 1 chữ `t`); đứng sau giới từ `am` (`Dativ`) thêm `-n` thành **`am achten März`**.
31. **Câu 31**: Điền dạng chữ của số thứ tự trong ngoặc đơn vào chỗ trống: *„Der Deutschkurs beginnt am ___ (20.) September.“*
    * Đáp án chấp nhận: `["zwanzigsten"]`
    * Dịch nghĩa câu: *"Khóa học tiếng Đức bắt đầu vào ngày 20 tháng Chín."*
    * Giải thích: Từ số 20 trở đi, số thứ tự dùng đuôi `-ste` (`Nominativ`) và **`-sten`** (`Dativ` sau `am`) → **`am zwanzigsten September`**.
32. **Câu 32**: Điền giới từ chỉ vị trí phù hợp với bức tranh và bức tường: *„In unserem Wohnzimmer hängt eine große Uhr ___ der Wand.“*
    * Đáp án chấp nhận: `["an"]`
    * Dịch nghĩa câu: *"Trong phòng khách của chúng tôi có một chiếc đồng hồ lớn treo trên tường."*
    * Giải thích: Treo áp sát lên bề mặt thẳng đứng (`die Wand`) dùng giới từ **`an`** (`an der Wand`).
33. **Câu 33**: Điền dạng chia đúng của động từ `gefallen` vào chỗ trống: *„Wie ___ dir das neue Fahrrad von deinem Bruder?“*
    * Đáp án chấp nhận: `["gefällt", "gefaellt"]`
    * Dịch nghĩa câu: *"Bạn thấy thích chiếc xe đạp mới của anh trai bạn như thế nào?"*
    * Giải thích: Chủ ngữ của câu là `das neue Fahrrad` (ngôi `es`), nên động từ `gefallen` biến âm `a -> ä` thành **`gefällt`** (đi với tân ngữ `Dativ` là `dir`).

---

#### NHÓM 3: DỊCH NGHĨA TỪ / CỤM TỪ VIỆT → ĐỨC (`dich_nghia_vd` — 12 Câu: Câu 34 → Câu 45)
34. **Câu 34**: Dịch sang tiếng Đức: ***"bằng tàu điện ngầm"***
    * Đáp án chấp nhận: `["mit der U-Bahn", "mit der U Bahn"]`
    * Giải thích: `die U-Bahn` (giống cái) đi sau giới từ `mit` (`Dativ`) biến đổi thành **`mit der U-Bahn`**.
35. **Câu 35**: Dịch sang tiếng Đức: ***"bằng máy bay"***
    * Đáp án chấp nhận: `["mit dem Flugzeug"]`
    * Giải thích: `das Flugzeug` (giống trung) đi sau giới từ `mit` (`Dativ`) biến đổi thành **`mit dem Flugzeug`**.
36. **Câu 36**: Dịch sang tiếng Đức: ***"đi bộ"***
    * Đáp án chấp nhận: `["zu Fuß", "zu Fuß gehen", "zu Fuss", "zu Fuss gehen"]`
    * Giải thích: Cụm cố định chỉ việc đi bộ trong tiếng Đức là **`zu Fuß`** (hoặc **`zu Fuß gehen`**).
37. **Câu 37**: Dịch sang tiếng Đức: ***"ở tầng trệt"***
    * Đáp án chấp nhận: `["im Erdgeschoss", "in dem Erdgeschoss"]`
    * Giải thích: Tầng trệt là danh từ giống trung `das Erdgeschoss` → ở tầng trệt là **`im Erdgeschoss`**.
38. **Câu 38**: Dịch sang tiếng Đức: ***"ở tầng ba"***
    * Đáp án chấp nhận: `["im dritten Stock", "im 3. Stock", "in der dritten Etage", "in der 3. Etage"]`
    * Giải thích: Tầng lầu là `der Stock` (hoặc `die Etage`), số thứ tự 3 ở `Dativ` là `dritten` → **`im dritten Stock`**.
39. **Câu 39**: Dịch sang tiếng Đức (kèm mạo từ): ***"trạm dừng (xe buýt / tàu điện)"***
    * Đáp án chấp nhận: `["die Haltestelle", "Haltestelle", "die Bushaltestelle"]`
    * Giải thích: Trạm dừng phương tiện công cộng là danh từ giống cái **`die Haltestelle`** (số nhiều: `die Haltestellen`).
40. **Câu 40**: Dịch sang tiếng Đức (kèm mạo từ): ***"thang máy"***
    * Đáp án chấp nhận: `["der Aufzug", "Aufzug", "der Fahrstuhl", "Fahrstuhl"]`
    * Giải thích: Thang máy trong tiếng Đức là danh từ giống đực **`der Aufzug`** hoặc **`der Fahrstuhl`**.
41. **Câu 41**: Dịch sang tiếng Đức (kèm mạo từ): ***"bàn làm việc"***
    * Đáp án chấp nhận: `["der Schreibtisch", "Schreibtisch"]`
    * Giải thích: Bàn làm việc / bàn viết là danh từ ghép giống đực **`der Schreibtisch`** (số nhiều: `die Schreibtische`).
42. **Câu 42**: Dịch sang tiếng Đức (kèm mạo từ): ***"máy in"***
    * Đáp án chấp nhận: `["der Drucker", "Drucker"]`
    * Giải thích: Máy in là danh từ giống đực **`der Drucker`**.
43. **Câu 43**: Dịch cụm vị trí sau sang tiếng Đức: ***"phía trước khách sạn"***
    * Đáp án chấp nhận: `["vor dem Hotel"]`
    * Giải thích: Giới từ *"phía trước"* là `vor`; `das Hotel` (giống trung) ở Cách 3 (`Dativ`) đổi thành `dem Hotel` → **`vor dem Hotel`**.
44. **Câu 44**: Dịch cụm ngày tháng sau sang tiếng Đức: ***"vào ngày mùng 1 tháng Năm"***
    * Đáp án chấp nhận: `["am ersten Mai", "am 1. Mai", "am ersten Fünften", "am 1.5."]`
    * Giải thích: Giới từ `am` + số thứ tự `1.` ở `Dativ` (`ersten`) + `Mai` → **`am ersten Mai`**.
45. **Câu 45**: Dịch cụm vị trí sau sang tiếng Đức: ***"đang ở nhà / đi về nhà"*** (Ghi theo thứ tự: `ở nhà / về nhà`)
    * Đáp án chấp nhận: `["zu Hause / nach Hause", "zu Hause, nach Hause", "zuhause / nachhause"]`
    * Giải thích: **`zu Hause`** dùng cho trạng thái tĩnh *(đang ở nhà - Wo?)*, còn **`nach Hause`** dùng cho hành động di chuyển *(đi về nhà - Wohin?)*.

---

#### NHÓM 4: DỊCH NGHĨA TỪ / CỤM TỪ ĐỨC → VIỆT (`dich_nghia_dv` — 12 Câu: Câu 46 → Câu 57)
46. **Câu 46**: Dịch sang tiếng Việt: ***„mit der S-Bahn“***
    * Đáp án chấp nhận: `["bằng tàu điện nhanh", "bằng tàu điện đô thị", "bằng tàu S-Bahn", "bằng tàu điện", "với tàu điện đô thị"]`
    * Giải thích: `die S-Bahn` (*Stadtschnellbahn*) là tàu điện nhanh đô thị; `mit der S-Bahn` = bằng tàu điện đô thị.
47. **Câu 47**: Dịch sang tiếng Việt: ***„die Straßenbahn“***
    * Đáp án chấp nhận: `["tàu điện", "tàu điện mặt đất", "xe điện", "tàu điện trên mặt đất"]`
    * Giải thích: `die Straßenbahn` là tàu điện chạy trên đường phố (tàu điện mặt đất).
48. **Câu 48**: Dịch sang tiếng Việt: ***„der Konferenzraum“***
    * Đáp án chấp nhận: `["phòng họp", "phòng hội nghị"]`
    * Giải thích: `der Konferenzraum` (`die Konferenz` + `der Raum`) có nghĩa là phòng họp / phòng hội nghị.
49. **Câu 49**: Dịch sang tiếng Việt: ***„an der Rezeption“***
    * Đáp án chấp nhận: `["ở quầy lễ tân", "tại quầy lễ tân", "ở lễ tân", "tại bàn tiếp tân"]`
    * Giải thích: `die Rezeption` là quầy lễ tân; ở tại quầy lễ tân dùng giới từ `an` + `Dativ` → `an der Rezeption`.
50. **Câu 50**: Dịch sang tiếng Việt: ***„zwischen dem Stuhl und dem Schreibtisch“***
    * Đáp án chấp nhận: `["ở giữa cái ghế và bàn làm việc", "giữa ghế và bàn làm việc", "nằm giữa chiếc ghế và cái bàn làm việc", "ở giữa ghế và bàn viết"]`
    * Giải thích: `zwischen` = ở giữa; `der Stuhl` = cái ghế; `der Schreibtisch` = bàn làm việc.
51. **Câu 51**: Dịch sang tiếng Việt: ***„hinter dem Bahnhof“***
    * Đáp án chấp nhận: `["ở phía sau nhà ga", "phía sau nhà ga", "đằng sau nhà ga", "sau nhà ga"]`
    * Giải thích: Giới từ `hinter` có nghĩa là ở phía sau / đằng sau; `der Bahnhof` = nhà ga.
52. **Câu 52**: Dịch sang tiếng Việt: ***„unter dem Tisch“***
    * Đáp án chấp nhận: `["dưới bàn", "ở dưới bàn", "dưới gầm bàn", "ở dưới gầm bàn", "phía dưới cái bàn"]`
    * Giải thích: Giới từ `unter` có nghĩa là ở phía dưới / dưới gầm.
53. **Câu 53**: Dịch sang tiếng Việt: ***„über dem Sofa“***
    * Đáp án chấp nhận: `["phía trên ghế sofa", "ở phía trên ghế sofa", "trên ghế sofa (không tiếp xúc)", "treo phía trên ghế sô pha"]`
    * Giải thích: Giới từ `über` chỉ vị trí ở phía trên cao hơn vật mốc (không tiếp xúc trực tiếp với bề mặt sofa).
54. **Câu 54**: Dịch sang tiếng Việt: ***„bei meinen Eltern“***
    * Đáp án chấp nhận: `["ở chỗ bố mẹ tôi", "ở nhà bố mẹ tôi", "tại nhà bố mẹ tôi", "với bố mẹ tôi"]`
    * Giải thích: Giới từ `bei` + người có nghĩa là ở tại nhà / chỗ của người đó (`bei meinen Eltern` = ở nhà bố mẹ tôi).
55. **Câu 55**: Dịch sang tiếng Việt: ***„am einundzwanzigsten Juni“***
    * Đáp án chấp nhận: `["vào ngày 21 tháng 6", "vào ngày 21 tháng Sáu", "ngày 21 tháng 6", "ngày 21/6", "vào ngày hai mươi mốt tháng Sáu"]`
    * Giải thích: `einundzwanzigsten` là số thứ tự `21.` ở Cách 3 (`Dativ`) sau giới từ `am`; `Juni` = tháng Sáu.
56. **Câu 56**: Dịch sang tiếng Việt: ***„vom dritten bis zum zehnten August“***
    * Đáp án chấp nhận: `["từ ngày 3 đến ngày 10 tháng 8", "từ ngày mùng 3 đến ngày 10 tháng Tám", "từ 3/8 đến 10/8", "từ ngày 3 đến 10 tháng 8"]`
    * Giải thích: `vom ... bis zum ...` = từ ngày ... đến ngày ...; `dritten` = ngày 3; `zehnten` = ngày 10; `August` = tháng Tám.
57. **Câu 57**: Dịch sang tiếng Việt: ***„die Tastatur und die Maus“***
    * Đáp án chấp nhận: `["bàn phím và chuột", "bàn phím và con chuột máy tính", "bàn phím và chuột máy tính"]`
    * Giải thích: `die Tastatur` = bàn phím máy tính; `die Maus` = con chuột máy tính.

---

#### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 10 Bài: Câu 58 → Câu 67, mỗi bài 4 cặp)
58. **Câu 58 (Bài nối ô 1 — Biến đổi mạo từ sang Cách 3 `Dativ`)**:
    * `Đi bằng tàu điện ngầm (danh từ giống Cái: die U-Bahn)` ⇄ `mit der U-Bahn (die biến đổi thành der)`
    * `Gặp nhau ở nhà ga (danh từ giống Đực: der Bahnhof)` ⇄ `am Bahnhof (an + dem gộp thành am)`
    * `Đỗ xe phía trước khách sạn (danh từ giống Trung: das Hotel)` ⇄ `vor dem Hotel (das biến đổi thành dem)`
    * `Đi dã ngoại cùng bọn trẻ (danh từ Số nhiều: die Kinder)` ⇄ `mit den Kindern (die biến đổi thành den + thêm đuôi -n)`
59. **Câu 59 (Bài nối ô 2 — Các dạng gộp giới từ + mạo từ ở `Dativ`)**:
    * `Đi bộ đến trường học (địa điểm giống Cái)` ⇄ `zur Schule (viết gọn bắt buộc của zu + der Schule)`
    * `Đi tàu ra ga chính (địa điểm giống Đực)` ⇄ `zum Hauptbahnhof (viết gọn bắt buộc của zu + dem Hauptbahnhof)`
    * `Đang ở chỗ bác sĩ khám bệnh (người / chuyên gia)` ⇄ `beim Arzt (viết gọn bắt buộc của bei + dem Arzt)`
    * `Đón người thân trở về từ sân bay (địa điểm xuất phát)` ⇄ `vom Flughafen (viết gọn bắt buộc của von + dem Flughafen)`
60. **Câu 60 (Bài nối ô 3 — Phương tiện giao thông & Cách diễn đạt chuẩn)**:
    * `die U-Bahn (tàu điện ngầm)` ⇄ `mit der U-Bahn fahren`
    * `das Flugzeug (máy bay)` ⇄ `mit dem Flugzeug fliegen`
    * `das Fahrrad (xe đạp)` ⇄ `mit dem Fahrrad fahren`
    * `der Fuß (đi bộ - ngoại lệ)` ⇄ `zu Fuß gehen`
61. **Câu 61 (Bài nối ô 4 — Giới từ vị trí `Wo?` trên bàn làm việc)**:
    * `auf dem Schreibtisch` ⇄ `nằm ở trên mặt bàn làm việc (có tiếp xúc)`
    * `unter dem Schreibtisch` ⇄ `đặt ở dưới gầm bàn làm việc`
    * `neben der Tastatur` ⇄ `nằm ở bên cạnh bàn phím`
    * `an der Wand über dem Tisch` ⇄ `treo trên tường phía trên cái bàn`
62. **Câu 62 (Bài nối ô 5 — Số đếm sang Số thứ tự bất quy tắc & từ 20)**:
    * `1 (eins)` ⇄ `der erste / am ersten`
    * `3 (drei)` ⇄ `der dritte / am dritten`
    * `7 (sieben)` ⇄ `der siebte / am siebten`
    * `20 (zwanzig)` ⇄ `der zwanzigste / am zwanzigsten`
63. **Câu 63 (Bài nối ô 6 — Ngày tháng bằng số sang Cách đọc sau giới từ `am`)**:
    * `am 01.01.` ⇄ `am ersten Januar`
    * `am 08.03.` ⇄ `am achten März`
    * `am 15.08.` ⇄ `am fünfzehnten August`
    * `am 24.12.` ⇄ `am vierundzwanzigsten Dezember`
64. **Câu 64 (Bài nối ô 7 — Năm bằng số sang Cách đọc chữ tiếng Đức)**:
    * `1945` ⇄ `neunzehnhundertfünfundvierzig`
    * `1989` ⇄ `neunzehnhundertneunundachtzig`
    * `1998` ⇄ `neunzehnhundertachtundneunzig`
    * `2026` ⇄ `zweitausendsechsundzwanzig`
65. **Câu 65 (Bài nối ô 8 — Đại từ nhân xưng sang Mạo từ sở hữu ở `Dativ`)**:
    * `ich (tôi)` ⇄ `mit meinem Bruder / mit meiner Schwester`
    * `sie (cô ấy)` ⇄ `mit ihrem Bruder / mit ihrer Schwester`
    * `wir (chúng tôi)` ⇄ `mit unserem Bruder / mit unserer Schwester`
    * `ihr (các bạn)` ⇄ `mit eurem Bruder / mit eurer Schwester`
66. **Câu 66 (Bài nối ô 9 — Câu hỏi định hướng & Thời gian sang Câu trả lời)**:
    * `Womit fährt Herr Müller nach Berlin?` ⇄ `Er fährt mit dem Zug.`
    * `Wo ist das Büro von Frau Schneider?` ⇄ `Es liegt im dritten Stock neben dem Aufzug.`
    * `Welcher Tag ist heute?` ⇄ `Heute ist der zwölfte Oktober.`
    * `Wann hast du Geburtstag?` ⇄ `Ich habe am siebten Mai Geburtstag.`
67. **Câu 67 (Bài nối ô 10 — Động từ Bài 6 sang Nghĩa & Quy tắc biến âm)**:
    * `fahren (du fährst, er fährt)` ⇄ `đi bằng xe/tàu (biến âm a -> ä)`
    * `umsteigen (steigt ... um)` ⇄ `đổi tàu / chuyển tuyến xe (động từ tách)`
    * `helfen (du hilfst, er hilft + Dativ)` ⇄ `giúp đỡ ai đó (biến âm e -> i)`
    * `hängen (hängt + Wo? Dativ)` ⇄ `treo ở đâu đó (vị trí tĩnh)`

---

#### NHÓM 6: ĐIỀN VÀO CHỖ TRỐNG ĐỂ TẠO THÀNH CÂU (`dien_tao_cau` — 10 Câu: Câu 68 → Câu 77)
68. **Câu 68**: Điền 2 từ còn thiếu để hoàn thành câu: *„Mỗi buổi sáng anh trai tôi đi làm bằng tàu điện ngầm.“*
    * Khung câu hiển thị: `Jeden Morgen [1] mein Bruder mit [2] U-Bahn zur Arbeit.` (Gợi ý: `fahren`, `die U-Bahn`)
    * Đáp án từng ô: Ô 1 = `["fährt", "faehrt"]`, Ô 2 = `["der"]`.
    * Giải thích: Chủ ngữ `mein Bruder` (`er`) chia động từ `fahren` là `fährt`; `die U-Bahn` (giống cái) sau `mit` (`Dativ`) đổi thành `mit der U-Bahn`.
69. **Câu 69**: Điền 2 từ còn thiếu để hoàn thành câu: *„Văn phòng của chúng tôi nằm ở tầng hai bên cạnh thang máy.“*
    * Khung câu hiển thị: `Unser Büro liegt [1] zweiten Stock neben [2] Aufzug.` (Gợi ý: `der Stock`, `der Aufzug`)
    * Đáp án từng ô: Ô 1 = `["im"]`, Ô 2 = `["dem"]`.
    * Giải thích: Ở tầng hai dùng `im zweiten Stock`; `der Aufzug` (giống đực) sau giới từ `neben` (`Wo? + Dativ`) đổi thành `neben dem Aufzug`.
70. **Câu 70**: Điền 2 từ còn thiếu để hoàn thành câu: *„Quán cà phê nằm giữa ngân hàng và rạp chiếu phim.“*
    * Khung câu hiển thị: `Das Café liegt zwischen [1] Bank und [2] Kino.` (Gợi ý: `die Bank`, `das Kino`)
    * Đáp án từng ô: Ô 1 = `["der"]`, Ô 2 = `["dem"]`.
    * Giải thích: Sau `zwischen` (`Wo? + Dativ`), danh từ giống cái `die Bank` đổi thành `der Bank`, danh từ giống trung `das Kino` đổi thành `dem Kino`.
71. **Câu 71**: Điền 2 từ còn thiếu để hoàn thành câu: *„Hôm nay là ngày mùng 1 tháng Năm, và ngày mai vào ngày mùng 2 tháng Năm chúng tôi bay sang Ý.“*
    * Khung câu hiển thị: `Heute ist der [1] Mai, und morgen am [2] Mai fliegen wir nach Italien.` (Gợi ý: `1.`, `2.`)
    * Đáp án từng ô: Ô 1 = `["erste"]`, Ô 2 = `["zweiten"]`.
    * Giải thích: Sau `Heute ist der ...` (`Nominativ`) dùng đuôi `-te` (`erste`); sau `am` (`Dativ`) dùng đuôi `-ten` (`zweiten`).
72. **Câu 72**: Điền 2 từ còn thiếu để hoàn thành câu: *„Vào Chủ nhật bọn trẻ chơi ở trong công viên với những người bạn của chúng.“*
    * Khung câu hiển thị: `Am Sonntag spielen die Kinder [1] Park mit ihren [2].` (Gợi ý: `der Park`, `die Freunde`)
    * Đáp án từng ô: Ô 1 = `["im"]`, Ô 2 = `["Freunden"]`.
    * Giải thích: Trong công viên (`der Park`) là `im Park`; danh từ số nhiều `Freunde` ở Cách 3 (`Dativ`) sau `mit ihren` bắt buộc thêm `-n` thành `Freunden`.
73. **Câu 73**: Điền 2 từ còn thiếu để hoàn thành câu: *„Các bạn có kỳ nghỉ từ ngày mùng 7 đến ngày 20 tháng Tám phải không?“*
    * Khung câu hiển thị: `Habt ihr vom [1] bis zum [2] August Urlaub?` (Gợi ý: `7.`, `20.`)
    * Đáp án từng ô: Ô 1 = `["siebten"]`, Ô 2 = `["zwanzigsten"]`.
    * Giải thích: Cả hai vị trí sau `vom` và `bis zum` đều chia ở `Dativ`: `7. -> siebten`, `20. -> zwanzigsten`.
74. **Câu 74**: Điền 2 từ còn thiếu để hoàn thành câu: *„Chuyến tàu khởi hành lúc 9 giờ từ nhà ga trung tâm.“*
    * Khung câu hiển thị: `Der Zug [1] um 9 Uhr vom Hauptbahnhof [2].` (Gợi ý động từ tách: `abfahren`)
    * Đáp án từng ô: Ô 1 = `["fährt", "faehrt"]`, Ô 2 = `["ab"]`.
    * Giải thích: Động từ tách `abfahren` chia cho ngôi thứ 3 số ít (`der Zug`) biến âm thành `fährt` ở vị trí số 2 và tách tiền tố `ab` xuống cuối câu.
75. **Câu 75**: Điền 2 từ còn thiếu để hoàn thành câu: *„Con mèo đang ngủ dưới gầm ghế của bố tôi.“*
    * Khung câu hiển thị: `Die Katze schläft [1] dem Stuhl von [2] Vater.` (Gợi ý: `dưới gầm`, `mein Vater`)
    * Đáp án từng ô: Ô 1 = `["unter"]`, Ô 2 = `["meinem"]`.
    * Giải thích: Giới từ *"dưới gầm"* là `unter`; sau giới từ `von` (+ `Dativ`), `mein Vater` (giống đực) đổi thành `von meinem Vater`.
76. **Câu 76**: Điền 2 từ còn thiếu để hoàn thành câu: *„Tối nay chúng tôi ở nhà, nhưng ngày mai chúng tôi đi bộ đến thư viện.“*
    * Khung câu hiển thị: `Heute Abend bleiben wir [1] Hause, aber morgen gehen wir zu [2] zur Bibliothek.`
    * Đáp án từng ô: Ô 1 = `["zu"]`, Ô 2 = `["Fuß", "Fuss"]`.
    * Giải thích: Cụm cố định *"ở nhà"* là `zu Hause` và *"đi bộ"* là `zu Fuß`.
77. **Câu 77**: Điền 2 từ còn thiếu để hoàn thành câu: *„Bức tranh đẹp treo trên tường phía trên ghế sofa.“*
    * Khung câu hiển thị: `Das schöne Bild hängt an [1] Wand über [2] Sofa.` (Gợi ý: `die Wand`, `das Sofa`)
    * Đáp án từng ô: Ô 1 = `["der"]`, Ô 2 = `["dem"]`.
    * Giải thích: `die Wand` (giống cái) ở `Dativ` là `an der Wand`; `das Sofa` (giống trung) ở `Dativ` là `über dem Sofa`.

---

#### NHÓM 7: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 9 Câu: Câu 78 → Câu 86)
78. **Câu 78**:
    * `audio_text`: *"Meine Kollegin fährt jeden Tag mit der Straßenbahn ins Büro."*
    * `display_sentence`: *"Meine Kollegin fährt jeden Tag mit der ___ ins Büro."*
    * `hint_vi`: *"Nữ đồng nghiệp của tôi mỗi ngày đều đi bằng tàu điện mặt đất đến văn phòng."*
    * `accepted_answers`: `["Straßenbahn", "Strassenbahn"]`
    * Giải thích: Danh từ giống cái `die Straßenbahn` (tàu điện mặt đất) sau giới từ `mit` là `mit der Straßenbahn`.
79. **Câu 79**:
    * `audio_text`: *"Die Rezeption befindet sich im Erdgeschoss neben dem Eingang."*
    * `display_sentence`: *"Die Rezeption befindet sich im ___ neben dem Eingang."*
    * `hint_vi`: *"Quầy lễ tân nằm ở tầng trệt bên cạnh lối vào."*
    * `accepted_answers`: `["Erdgeschoss"]`
    * Giải thích: Danh từ `das Erdgeschoss` có nghĩa là tầng trệt (`im Erdgeschoss`).
80. **Câu 80**:
    * `audio_text`: *"Das Büro von Herrn Müller liegt im dritten Stock."*
    * `display_sentence`: *"Das Büro von Herrn Müller liegt im ___ Stock."*
    * `hint_vi`: *"Văn phòng của ông Müller nằm ở tầng ba."*
    * `accepted_answers`: `["dritten", "3."]`
    * Giải thích: Số thứ tự `3.` ở Cách 3 (`Dativ`) sau giới từ `im` đọc và viết là `dritten`.
81. **Câu 81**:
    * `audio_text`: *"Der Drucker steht auf dem Schreibtisch zwischen dem Computer und dem Telefon."*
    * `display_sentence`: *"Der Drucker steht auf dem Schreibtisch ___ dem Computer und dem Telefon."*
    * `hint_vi`: *"Chiếc máy in đặt trên bàn làm việc ở giữa máy tính và điện thoại bàn."*
    * `accepted_answers`: `["zwischen"]`
    * Giải thích: Giới từ `zwischen` có nghĩa là ở giữa hai vật.
82. **Câu 82**:
    * `audio_text`: *"Im Sommer fliegen unsere Eltern mit dem Flugzeug nach Spanien."*
    * `display_sentence`: *"Im Sommer fliegen unsere Eltern mit dem ___ nach Spanien."*
    * `hint_vi`: *"Vào mùa hè bố mẹ chúng tôi bay bằng máy bay sang Tây Ban Nha."*
    * `accepted_answers`: `["Flugzeug"]`
    * Giải thích: Danh từ `das Flugzeug` có nghĩa là máy bay (`mit dem Flugzeug`).
83. **Câu 83**:
    * `audio_text`: *"Mein Bruder hat am fünfzehnten August Geburtstag."*
    * `display_sentence`: *"Mein Bruder hat am ___ August Geburtstag."*
    * `hint_vi`: *"Anh trai tôi có sinh nhật vào ngày 15 tháng Tám."*
    * `accepted_answers`: `["fünfzehnten", "fuenfzehnten", "15."]`
    * Giải thích: Ngày 15 đi sau giới từ `am` (`Dativ`) là `fünfzehnten`.
84. **Câu 84**:
    * `audio_text`: *"Heute ist der zwanzigste Oktober."*
    * `display_sentence`: *"Heute ist der ___ Oktober."*
    * `hint_vi`: *"Hôm nay là ngày 20 tháng Mười."*
    * `accepted_answers`: `["zwanzigste", "20."]`
    * Giải thích: Sau `Heute ist der ...` (`Nominativ`), số thứ tự 20 có đuôi `-ste` là `zwanzigste`.
85. **Câu 85**:
    * `audio_text`: *"Am Wochenende fährt Lukas mit seinen Kindern in den Zoo."*
    * `display_sentence`: *"Am Wochenende fährt Lukas mit seinen ___ in den Zoo."*
    * `hint_vi`: *"Vào cuối tuần Lukas đi sở thú cùng với các con của anh ấy."*
    * `accepted_answers`: `["Kindern"]`
    * Giải thích: Danh từ số nhiều `die Kinder` khi chia ở Cách 3 (`Dativ`) phải thêm đuôi `-n` thành `Kindern`.
86. **Câu 86**:
    * `audio_text`: *"Der große Parkplatz liegt direkt hinter dem Krankenhaus."*
    * `display_sentence`: *"Der große Parkplatz liegt direkt ___ dem Krankenhaus."*
    * `hint_vi`: *"Bãi đỗ xe lớn nằm ngay phía sau bệnh viện."*
    * `accepted_answers`: `["hinter"]`
    * Giải thích: Giới từ chỉ vị trí `hinter` có nghĩa là ở phía sau.

---

#### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (`dich_cau_vd` — 7 Câu: Câu 87 → Câu 93, chấm đa đáp án linh hoạt)
87. **Câu 87**: Dịch câu sau sang tiếng Đức: ***"Anh trai tôi đi làm mỗi ngày bằng xe buýt."***
    * `accepted_answers`:
      * `"Mein Bruder fährt jeden Tag mit dem Bus zur Arbeit."`
      * `"Jeden Tag fährt mein Bruder mit dem Bus zur Arbeit."`
      * `"Mein Bruder fährt täglich mit dem Bus zur Arbeit."`
      * `"Mit dem Bus fährt mein Bruder jeden Tag zur Arbeit."`
    * Giải thích: Chủ ngữ `Mein Bruder` chia động từ `fahren` thành `fährt`; phương tiện `der Bus` ở `Dativ` là `mit dem Bus`; đi làm là `zur Arbeit`.
88. **Câu 88**: Dịch câu sau sang tiếng Đức: ***"Văn phòng của bà Schneider nằm ở tầng ba bên cạnh thang máy."***
    * `accepted_answers`:
      * `"Das Büro von Frau Schneider liegt im dritten Stock neben dem Aufzug."`
      * `"Das Büro von Frau Schneider ist im dritten Stock neben dem Aufzug."`
      * `"Das Büro von Frau Schneider liegt im 3. Stock neben dem Aufzug."`
      * `"Das Büro von Frau Schneider ist im 3. Stock neben dem Fahrstuhl."`
      * `"Frau Schneiders Büro liegt im dritten Stock neben dem Aufzug."`
    * Giải thích: Ở tầng ba là `im dritten Stock`; bên cạnh thang máy (`der Aufzug / der Fahrstuhl`) ở `Dativ` là `neben dem Aufzug`.
89. **Câu 89**: Dịch câu sau sang tiếng Đức: ***"Hôm nay là ngày mùng 8 tháng Ba."***
    * `accepted_answers`:
      * `"Heute ist der achte März."`
      * `"Heute ist der 8. März."`
      * `"Heute ist der achte Dritte."`
    * Giải thích: Cấu trúc nói ngày hiện tại với động từ `sein` dùng Cách 1 (`Nominativ`): `Heute ist der achte März`.
90. **Câu 90**: Dịch câu sau sang tiếng Đức: ***"Em gái tôi có sinh nhật vào ngày 21 tháng Sáu."***
    * `accepted_answers`:
      * `"Meine Schwester hat am einundzwanzigsten Juni Geburtstag."`
      * `"Meine Schwester hat am 21. Juni Geburtstag."`
      * `"Am einundzwanzigsten Juni hat meine Schwester Geburtstag."`
      * `"Am 21. Juni hat meine Schwester Geburtstag."`
    * Giải thích: Sự kiện diễn ra vào ngày nào dùng giới từ `am` + số thứ tự đuôi `-sten` (`am einundzwanzigsten Juni`).
91. **Câu 91**: Dịch câu sau sang tiếng Đức: ***"Chiếc máy tính xách tay nằm trên bàn làm việc giữa cái đèn và điện thoại."***
    * `accepted_answers`:
      * `"Der Laptop liegt auf dem Schreibtisch zwischen der Lampe und dem Telefon."`
      * `"Der Laptop steht auf dem Schreibtisch zwischen der Lampe und dem Telefon."`
      * `"Der Laptop ist auf dem Schreibtisch zwischen der Lampe und dem Telefon."`
      * `"Der Laptop liegt auf dem Schreibtisch zwischen dem Telefon und der Lampe."`
    * Giải thích: Trên bàn làm việc (`der Schreibtisch`) là `auf dem Schreibtisch`; giữa cái đèn (`die Lampe -> der Lampe`) và điện thoại (`das Telefon -> dem Telefon`).
92. **Câu 92**: Dịch câu sau sang tiếng Đức: ***"Chúng tôi có kỳ nghỉ từ ngày mùng 3 đến ngày 15 tháng Tám."***
    * `accepted_answers`:
      * `"Wir haben vom dritten bis zum fünfzehnten August Urlaub."`
      * `"Wir haben vom 3. bis zum 15. August Urlaub."`
      * `"Vom dritten bis zum fünfzehnten August haben wir Urlaub."`
      * `"Wir haben Urlaub vom dritten bis zum fünfzehnten August."`
    * Giải thích: Khoảng từ ngày ... đến ngày ... dùng `vom + [-ten] + bis zum + [-ten]` (`vom dritten bis zum fünfzehnten August`).
93. **Câu 93**: Dịch câu sau sang tiếng Đức: ***"Trường học ở ngay cạnh nhà tôi nên tôi luôn đi bộ."***
    * `accepted_answers`:
      * `"Die Schule liegt direkt neben meinem Haus, deshalb gehe ich immer zu Fuß."`
      * `"Die Schule ist neben meinem Haus, also gehe ich immer zu Fuß."`
      * `"Die Schule ist gleich neben meinem Haus. Ich gehe immer zu Fuß."`
      * `"Die Schule liegt neben meinem Haus. Ich gehe immer zu Fuß."`
    * Giải thích: Bên cạnh nhà tôi (`das Haus`) ở `Dativ` là `neben meinem Haus`; đi bộ là `zu Fuß gehen`.

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (`dich_cau_dv` — 7 Câu: Câu 94 → Câu 100, chấm đa đáp án linh hoạt)
94. **Câu 94**: Dịch câu sau sang tiếng Việt: ***„Am Wochenende fahren unsere Großeltern mit der Straßenbahn zum Markt.“***
    * `accepted_answers`:
      * `"Vào cuối tuần ông bà của chúng tôi đi bằng tàu điện ra chợ"`
      * `"Cuối tuần ông bà chúng tôi đi chợ bằng tàu điện mặt đất"`
      * `"Vào cuối tuần ông bà tôi đi bằng tàu điện mặt đất đến chợ"`
      * `"Cuối tuần ông bà của chúng mình đi tàu điện ra chợ"`
    * Giải thích: `unsere Großeltern` = ông bà của chúng tôi; `mit der Straßenbahn` = bằng tàu điện mặt đất; `zum Markt` = ra chợ / đến chợ.
95. **Câu 95**: Dịch câu sau sang tiếng Việt: ***„Das Café liegt direkt zwischen der Buchhandlung und dem Kino.“***
    * `accepted_answers`:
      * `"Quán cà phê nằm ngay giữa hiệu sách và rạp chiếu phim"`
      * `"Quán cà phê ở ngay giữa tiệm sách và rạp chiếu phim"`
      * `"Quán cà phê nằm ở giữa hiệu sách và rạp phim"`
    * Giải thích: `zwischen der Buchhandlung und dem Kino` = ở giữa hiệu sách và rạp chiếu phim.
96. **Câu 96**: Dịch câu sau sang tiếng Việt: ***„Die Kantine befindet sich im Erdgeschoss und der Konferenzraum ist im siebten Stock.“***
    * `accepted_answers`:
      * `"Nhà ăn nằm ở tầng trệt và phòng họp ở tầng bảy"`
      * `"Căn tin ở tầng trệt còn phòng họp nằm ở tầng 7"`
      * `"Nhà ăn ở tầng trệt và phòng hội nghị nằm ở tầng bảy"`
    * Giải thích: `die Kantine` = nhà ăn / căng tin; `im Erdgeschoss` = ở tầng trệt; `im siebten Stock` = ở tầng bảy.
97. **Câu 97**: Dịch câu sau sang tiếng Việt: ***„Meine Tochter ist am dritten Oktober zweitausendzwei in Berlin geboren.“***
    * `accepted_answers`:
      * `"Con gái tôi sinh vào ngày mùng 3 tháng 10 năm 2002 tại Berlin"`
      * `"Con gái của tôi sinh ngày 3 tháng 10 năm 2002 ở Berlin"`
      * `"Con gái tôi sinh ngày 3/10/2002 ở Berlin"`
      * `"Con gái tôi sinh vào ngày ba tháng Mười năm 2002 tại Berlin"`
    * Giải thích: `am dritten Oktober zweitausendzwei` = vào ngày 3 tháng 10 năm 2002; `ist ... geboren` = sinh ra.
98. **Câu 98**: Dịch câu sau sang tiếng Việt: ***„Nach der Arbeit gehe ich nicht sofort nach Hause, sondern ich treffe mich mit meinen Freunden im Park.“***
    * `accepted_answers`:
      * `"Sau giờ làm việc tôi không đi về nhà ngay mà tôi gặp gỡ những người bạn của tôi ở trong công viên"`
      * `"Sau khi tan làm tôi không về nhà ngay mà hẹn gặp bạn bè của mình trong công viên"`
      * `"Sau giờ làm tôi không về nhà liền mà gặp những người bạn của tôi ở công viên"`
    * Giải thích: `Nach der Arbeit` = sau giờ làm việc; `nach Hause gehen` = đi về nhà; `mit meinen Freunden` = với những người bạn của tôi (`Dativ` số nhiều); `im Park` = ở trong công viên.
99. **Câu 99**: Dịch câu sau sang tiếng Việt: ***„Das große Familienfoto hängt an der Wand über dem Sofa.“***
    * `accepted_answers`:
      * `"Bức ảnh gia đình lớn treo trên tường phía trên ghế sofa"`
      * `"Tấm ảnh gia đình lớn được treo ở trên tường phía trên ghế sô pha"`
      * `"Bức ảnh gia đình to treo trên bức tường phía trên ghế sofa"`
    * Giải thích: `an der Wand` = trên tường (tiếp xúc mặt đứng); `über dem Sofa` = phía trên ghế sofa (không tiếp xúc).
100. **Câu 100**: Dịch câu sau sang tiếng Việt: ***„Vom ersten bis zum vierzehnten Juli bleibt unsere Arztpraxis geschlossen.“***
     * `accepted_answers`:
       * `"Từ ngày mùng 1 đến ngày 14 tháng 7 phòng khám bác sĩ của chúng tôi đóng cửa"`
       * `"Từ ngày 1 đến ngày 14 tháng Bảy phòng khám của chúng tôi đóng cửa"`
       * `"Từ 1/7 đến 14/7 phòng mạch của chúng tôi nghỉ đóng cửa"`
     * Giải thích: `Vom ersten bis zum vierzehnten Juli` = từ ngày 1 đến ngày 14 tháng 7; `die Arztpraxis` = phòng khám bác sĩ.

---

## PHẦN 4: KIẾN TRÚC BỘ SINH ĐỀ NGẪU NHIÊN ĐA CHIỀU (`DYNAMIC MULTI-VARIABLE RANDOMIZER`) CHO BÀI 6

Để thực hiện triệt để yêu cầu của người dùng: **"Đổi ngôi cho đa dạng chứ đừng dùng mỗi ngôi ich, số thì random thay đổi liên tục, chế tạo ra thêm những câu mới có nhiều nghĩa, ngữ cảnh mới"**, Antigravity IDE phải cài đặt 5 Engine sinh câu hỏi động (`Atomic Question Generators`) cho Bài 6:

### 4.1. Engine 1: Biến thiên Đa Chủ Ngữ $\times$ Phương Tiện Giao Thông $\times$ Điểm Đến (`Transport & Destination Matrix`)
* **Ngân hàng Chủ ngữ (12 chủ ngữ thuộc mọi ngôi)**:
  * `("Ich", "ich", "fahre", "fliege", "gehe", "Tôi")`
  * `("Du", "du", "fährst", "fliegst", "gehst", "Bạn")`
  * `("Mein Bruder", "er", "fährt", "fliegt", "geht", "Anh trai tôi")`
  * `("Deine Schwester", "sie", "fährt", "fliegt", "geht", "Chị gái của bạn")`
  * `("Herr Schneider", "er", "fährt", "fliegt", "geht", "Ông Schneider")`
  * `("Frau Wagner", "sie", "fährt", "fliegt", "geht", "Bà Wagner")`
  * `("Wir", "wir", "fahren", "fliegen", "gehen", "Chúng tôi")`
  * `("Ihr", "ihr", "fahrt", "fliegt", "geht", "Các bạn")`
  * `("Meine Eltern", "sie_pl", "fahren", "fliegen", "gehen", "Bố mẹ tôi")`
  * `("Die Studenten", "sie_pl", "fahren", "fliegen", "gehen", "Các sinh viên")`
  * `("Unsere Kollegen", "sie_pl", "fahren", "fliegen", "gehen", "Các đồng nghiệp của chúng tôi")`
  * `("Sie (Ngài)", "Sie", "fahren", "fliegen", "gehen", "Ngài")`
* **Ngân hàng Phương tiện (11 phương tiện chia đủ `der/die/das` + `zu Fuß`)** $\times$ **Ngân hàng Điểm đến (`zur Arbeit`, `zur Schule`, `zur Universität`, `zum Bahnhof`, `zum Flughafen`, `zum Krankenhaus`, `zur Bank`, `zur Post`, `nach Berlin`, `nach München`)**.
* Mỗi lần random sẽ kết hợp tự động `Chủ ngữ + Động từ chia đúng ngôi + Phương tiện ở Dativ + Điểm đến ở Dativ` và tự động sinh câu hỏi, đáp án, bản dịch tiếng Việt và lời giải thích khớp 100% với tổ hợp vừa rút!

### 4.2. Engine 2: Biến thiên Liên Tục Số Thứ Tự, Tầng Lầu & Ngày – Tháng – Năm (`Dynamic Date, Floor & Year Generator`)
* **Tự động sinh ngẫu nhiên**:
  * **Ngày (`1.` → `31.`)** kết hợp với **12 Tháng (`Januar` → `Dezember`)** và **Năm (`1950` → `2026`)**.
  * **Tầng lầu (`im Erdgeschoss`, `im 1. Stock` → `im 25. Stock`)** kết hợp với các phòng ban (`das Büro, die Kantine, der Konferenzraum, die Personalabteilung, die Bibliothek, die Arztpraxis`).
* Hệ thống có sẵn bảng tra từ điển đầy đủ cho cả **31 số thứ tự** ở 2 dạng `Nominativ (-te/-ste)` và `Dativ (-ten/-sten)` để khi random ra bất kỳ ngày nào (ví dụ `03.04.`, `07.09.`, `08.11.`, `16.02.`, `21.06.`, `28.10.`, `31.12.`), cả đề bài, phát âm TTS `de-DE`, đáp án và giải thích đều tự động cập nhật chính xác tuyệt đối!

### 4.3. Engine 3: Biến thiên Không Gian 9 Giới Từ Vị Trí (`Spatial Layout Engine: Wo? + Dativ`)
* Tự động kết hợp **20 đồ vật / địa điểm** với **9 giới từ vị trí (`in, an, auf, neben, vor, hinter, über, unter, zwischen`)** và **5 động từ vị trí (`steht, liegt, hängt, sitzt, befindet sich`)** để tạo ra hàng trăm câu miêu tả phòng làm việc, phòng khách và đường phố khác nhau.

### 4.4. Engine 4: Biến thiên Ma Trận Mạo Từ Sở Hữu Ở Cách 3 (`Possessive Dativ Matrix: 9 Ngôi × 4 Giống`)
* Tự động kết hợp 9 ngôi sở hữu (`mein-, dein-, sein-, ihr-, unser-, euer-, Ihr-`) với các giới từ `mit, bei, von, zu` và danh từ thuộc cả 4 nhóm (`Maskulinum`, `Femininum`, `Neutrum`, `Plural + -n`) để rèn luyện phản xạ chia đuôi `-em, -er, -en` không bao giờ nhầm lẫn.

---

## PHẦN 5: DANH SÁCH KIỂM THỬ BẮT BUỘC SAU KHI CODE (`POST-CODING QA CHECKLIST`)

Sau khi code xong Bài 6, Antigravity IDE **BẮT BUỘC** phải viết và chạy kịch bản kiểm thử tự động (`verify_lesson6_qa.py`) để kiểm tra 6 tiêu chí sau trước khi hoàn tất:

1. **Kiểm tra Bảo toàn Tuyệt đối Bài 1 → Bài 5 (`Zero-Regression Check`)**:
   * Xác nhận trong cơ sở dữ liệu `deutsch_meister.db`: **Bài 1 (P1), Bài 1 (P2), Bài 2, Bài 3, Bài 4, Bài 5** vẫn giữ nguyên 100% nội dung lý thuyết, từ vựng và số lượng câu hỏi bài tập, không có bất kỳ bài học cũ nào bị xóa hay thay đổi.
2. **Kiểm tra Quy mô 100 Câu hỏi & Đủ 9 Dạng Bài Tập của Bài 6 (`100-Question & 9-Type Verification`)**:
   * Xác nhận **Bài 6** có đúng **100 câu hỏi** (`trac_nghiem`: 18, `dien_khuyet`: 15, `dich_nghia_vd`: 12, `dich_nghia_dv`: 12, `noi_o`: 10, `dien_tao_cau`: 10, `nghe_dien`: 9, `dich_cau_vd`: 7, `dich_cau_dv`: 7).
3. **Kiểm tra Khớp Nguyên Tử Đề Bài – Đáp Án – Dịch Nghĩa – Giải Thích (`Atomic Alignment Check`)**:
   * Chạy vòng lặp giả lập 20 lần gọi API lấy đề bài tập Bài 6 (bao gồm cả khi kích hoạt Randomizer): Đảm bảo 100% câu hỏi đều có `correct_answer` nằm trong `options` (với trắc nghiệm), `accepted_answers` không rỗng (với tự luận/điền từ), `translation_vi` và `explanation` khớp chính xác với chủ ngữ, số thứ tự, ngày tháng và địa điểm trong câu hỏi.
4. **Kiểm tra 100% Thẻ Từ Vựng & Câu Ví Dụ (`Vocabulary Card Match Check`)**:
   * Quét toàn bộ từ vựng của Bài 6 trong `seed_a1_b6.py` và `lexikon_db.js`: Đảm bảo 100% câu ví dụ tiếng Đức (`example_de`) có chứa chính xác danh từ trên thẻ đó và bản dịch tiếng Việt (`example_vi`) dịch đúng nghĩa của câu ví dụ đó.
5. **Kiểm tra Giọng Đọc TTS `de-DE` (`Voice & Ordinal Number TTS Check`)**:
   * Đảm bảo mọi nút `🔊` trong Bài 6 và câu hỏi `nghe_dien` chỉ truyền văn bản tiếng Đức chuẩn vào `speakGerman()`, đọc chính xác các số thứ tự (`erste, dritte, siebte, achte, zwanzigste...`) và không đọc lẫn tiếng Việt hay ký tự đặc biệt.
6. **Đồng bộ lên GitHub (`Git Commit & Push`)**:
   * Sau khi toàn bộ bài kiểm thử đạt `100% PASS`, đẩy code lên repository `taolagautruc/deutsch-meister`:
     ```bash
     git add .
     git commit -m "Add Lesson 6 (Dativ, Praepositionen, Verkehrsmittel, Ordinalzahlen, Datum) with 100 diverse randomized exercises and full Zero-Bug QA"
     git push origin main
     ```