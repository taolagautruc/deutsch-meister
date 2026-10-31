# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 5 (A1) "THỜI GIAN - ĐỘNG TỪ TÁCH - HABEN IN PRÄTERITUM" (`TERMINE`) & QUY CHUẨN KIỂM THỬ KHÔNG LỖI (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa làm hỏng, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**, **Bài 4**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Nhiệm vụ của lần cập nhật này là **tạo mới hoàn toàn Bài 5 (`seed_a1_b5.py`)**, nối tiếp vào danh sách bài học cấp độ **A1**, bổ sung thêm động từ và từ vựng của Bài 5 vào kho tra cứu chung theo cơ chế **cộng dồn (`Additive Expansion Only`)**, và mở rộng phạm vi câu hỏi Đấu trường cho người học đạt tới Bài 5.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu.
>
> ---
>
> ### 🔍 2. DANH SÁCH CÁC LỖI CẤM LẶP LẠI & GIAO THỨC RÀ SOÁT (`ZERO-BUG QA PROTOCOL`)
> Trước đây hệ thống từng mắc một số lỗi nghiêm trọng trên giao diện. Trong quá trình code Bài 5 và rà soát hệ thống, Antigravity IDE **BẮT BUỘC TUYỆT ĐỐI KHÔNG ĐƯỢC MẮC LẠI** các lỗi sau:
>
> 1. **Cấm dịch sai nghĩa hoặc thiếu phần dịch nghĩa (`No Missing/Wrong Translations`)**:
>    * Mọi từ vựng Đức, mọi câu ví dụ Đức, mọi câu hỏi trong đề bài và mọi câu trong đoạn hội thoại/thư mẫu **bắt buộc phải đi kèm bản dịch tiếng Việt chuẩn xác 100%**.
>    * Tuyệt đối không để trống trường `meaning_vi`, `example_vi`, `translation_vi` hoặc hiển thị `undefined` / `null` trên giao diện.
> 2. **Cấm dịch đáp án hoặc giải thích không liên quan đến đề bài (`Strict Prompt-Answer-Explanation Alignment`)**:
>    * Trong phần bài tập (và khi dùng cơ chế Random đổi đề), **Đề bài (`question`) – Đáp án đúng (`correct_answer` / `accepted_answers`) – Phần dịch nghĩa câu hỏi – Giải thích đáp án (`explanation`)** phải khớp với nhau thành **một khối dữ liệu nguyên tử duy nhất (`Atomic Question Object`)**.
>    * **Cấm tuyệt đối** việc random ghép nhầm câu hỏi của biến thể A với đáp án hoặc lời giải thích của biến thể B!
> 3. **Cấm lỗi thiếu Voice hoặc phát âm sai ngôn ngữ (`100% Accurate German TTS Voice`)**:
>    * Mọi thẻ từ vựng, mọi dòng trong bảng chia động từ, mọi câu giao tiếp mẫu và câu hỏi nghe (`nghe_dien`) đều phải có nút `🔊` hoạt động 100%.
>    * Hàm `speakGerman(text, rate)` **chỉ được đọc phần văn bản tiếng Đức chuẩn (`de-DE`)**; tuyệt đối không đọc lẫn nghĩa tiếng Việt, không đọc ký hiệu mũi tên `->`, dấu gạch dưới `___`, hoặc ký hiệu ngữ pháp `(m)/(f)/(n)/(Pl)` bằng giọng Đức!
>    * Ví dụ: Trên thẻ hiển thị `der Montag (die Montage) - thứ Hai`, khi bấm nút `🔊` tại từ chính thì chuỗi truyền vào TTS phải là `"der Montag"`, khi bấm nút nghe số nhiều thì truyền `"die Montage"`, khi bấm nghe câu ví dụ thì chỉ truyền câu tiếng Đức `"Am Montag arbeite ich von acht bis zwölf Uhr."`.
> 4. **Cấm đưa câu ví dụ không khớp với thẻ từ vựng đang học (`Exact Vocabulary-Example Matching`)**:
>    * Thẻ từ vựng đang dạy từ nào thì **câu ví dụ (`example_de` & `example_vi`) bắt buộc phải chứa chính xác từ vựng đó** và đúng ngữ cảnh thực tế của Bài 5.
>    * *Ví dụ lỗi cấm lặp lại*: Thẻ từ vựng là `der Dienstag (thứ Ba)` nhưng câu ví dụ lại viết về `der Montag` hoặc `das Haus` $\rightarrow$ **CẤM TUYỆT ĐỐI!** Thẻ `der Dienstag` bắt buộc phải có ví dụ chứa chữ `Dienstag` (VD: *"Am Dienstag habe ich einen Deutschkurs."* — *"Vào thứ Ba tôi có một khóa học tiếng Đức."*).
> 5. **Cấm giải thích sai ngữ pháp của đáp án (`Verified Grammar Explanation`)**:
>    * Mọi lời giải thích đáp án phải nêu rõ: (a) Nghĩa tiếng Việt của cả câu hoàn chỉnh sau khi điền đáp án, (b) Quy tắc ngữ pháp cụ thể (tại sao dùng giới từ `am`/`um`/`im`, tại sao tách tiền tố `auf`/`aus`/`an` xuống cuối câu, tại sao chia `hatte`/`hattest`/`hatten`/`waren`).

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 $\rightarrow$ Bài 4 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 5**:

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
1. **Cập nhật chế độ xem Thì Quá Khứ Đơn (`Präteritum`) cho động từ `haben`**:
   * Bổ sung đầy đủ bảng đối chiếu song song **Hiện tại (`Präsens`) vs. Quá khứ đơn (`Präteritum`)** cho bộ đôi động từ nền tảng **`sein`** và **`haben`**:
     * `ich`: `bin` $\rightarrow$ **`war`** | `habe` $\rightarrow$ **`hatte`**
     * `du`: `bist` $\rightarrow$ **`warst`** | `hast` $\rightarrow$ **`hattest`**
     * `er/sie/es`: `ist` $\rightarrow$ **`war`** | `hat` $\rightarrow$ **`hatte`**
     * `wir`: `sind` $\rightarrow$ **`waren`** | `haben` $\rightarrow$ **`hatten`**
     * `ihr`: `seid` $\rightarrow$ **`wart`** | `habt` $\rightarrow$ **`hattet`**
     * `sie/Sie`: `sind` $\rightarrow$ **`waren`** | `haben` $\rightarrow$ **`hatten`**
2. **Bổ sung bộ lọc mới trên Tab Chia Động Từ**: `Động từ tách (Trennbare Verben)` và thêm **12 động từ mới của Bài 5** (kèm phát âm `de-DE` cho từng ngôi và câu ví dụ chuẩn):
   * **`aufmachen`** (*mở [cửa, sổ...]* — Tiền tố tách `auf-` + gốc `machen`):
     * Chia theo ngôi: `ich mache ... auf`, `du machst ... auf`, `er/sie/es macht ... auf`, `wir machen ... auf`, `ihr macht ... auf`, `sie/Sie machen ... auf`.
     * Ví dụ: *„Ich mache die Tür auf.“ (Tôi mở cánh cửa ra.)*
   * **`zumachen`** (*đóng lại* — Tiền tố tách `zu-` + gốc `machen`):
     * Chia theo ngôi: `ich mache ... zu`, `du machst ... zu`, `er/sie/es macht ... zu`...
     * Ví dụ: *„Es ist kalt. Machst du bitte das Fenster zu?“ (Trời lạnh đấy. Bạn làm ơn đóng cửa sổ lại nhé?)*
   * **`anmachen`** (*bật [đèn, tivi, thiết bị]* — Tiền tố tách `an-` + gốc `machen`):
     * Chia theo ngôi: `ich mache ... an`, `du machst ... an`, `er/sie/es macht ... an`...
     * Ví dụ: *„Am Abend mache ich die Lampe an.“ (Vào buổi tối tôi bật đèn lên.)*
   * **`ausmachen`** (*tắt [đèn, tivi, thiết bị]* — Tiền tố tách `aus-` + gốc `machen`):
     * Chia theo ngôi: `ich mache ... aus`, `du machst ... aus`, `er/sie/es macht ... aus`...
     * Ví dụ: *„Um 22 Uhr mache ich den Fernseher aus.“ (Vào lúc 22 giờ tôi tắt tivi.)*
   * **`aufstehen`** (*thức dậy, đứng dậy* — Tiền tố tách `auf-` + gốc `stehen`):
     * Chia theo ngôi: `ich stehe ... auf`, `du stehst ... auf`, `er/sie/es steht ... auf`, `wir stehen ... auf`, `ihr steht ... auf`, `sie/Sie stehen ... auf`.
     * Ví dụ: *„Am Sonntag stehe ich um 8 Uhr auf.“ (Vào Chủ nhật tôi thức dậy lúc 8 giờ.)*
   * **`ausgehen`** (*đi ra ngoài, đi chơi tối* — Tiền tố tách `aus-` + gốc `gehen`):
     * Chia theo ngôi: `ich gehe ... aus`, `du gehst ... aus`, `er/sie/es geht ... aus`, `wir gehen ... aus`, `ihr geht ... aus`, `sie/Sie gehen ... aus`.
     * Ví dụ: *„Am Freitag um 20 Uhr gehe ich aus.“ (Vào thứ Sáu lúc 20 giờ tôi đi chơi.)*
   * **`einkaufen`** (*đi mua sắm* — Tiền tố tách `ein-` + gốc `kaufen`):
     * Chia theo ngôi: `ich kaufe ... ein`, `du kaufst ... ein`, `er/sie/es kauft ... ein`, `wir kaufen ... ein`, `ihr kauft ... ein`, `sie/Sie kaufen ... ein`.
     * Ví dụ: *„Am Samstag kaufen wir im Supermarkt ein.“ (Vào thứ Bảy chúng tôi đi mua sắm ở siêu thị.)*
   * **`anrufen`** (*gọi điện thoại* — Tiền tố tách `an-` + gốc `rufen`):
     * Chia theo ngôi: `ich rufe ... an`, `du rufst ... an`, `er/sie/es ruft ... an`, `wir rufen ... an`, `ihr ruft ... an`, `sie/Sie rufen ... an`.
     * Ví dụ: *„Ich rufe dich am Nachmittag an.“ (Tôi sẽ gọi điện cho bạn vào buổi chiều.)*
   * **`fernsehen`** (*xem tivi* — Tiền tố tách `fern-` + gốc biến âm `sehen`: `e -> ie` ở `du, er/sie/es`):
     * Chia theo ngôi: `ich sehe ... fern`, `du siehst ... fern`, `er/sie/es sieht ... fern`, `wir sehen ... fern`, `ihr seht ... fern`, `sie/Sie sehen ... fern`.
     * Ví dụ: *„Am Abend sieht mein Vater gern fern.“ (Vào buổi tối bố tôi thích xem tivi.)*
   * **`mitkommen`** (*đi cùng, tham gia cùng* — Tiền tố tách `mit-` + gốc `kommen`):
     * Chia theo ngôi: `ich komme ... mit`, `du kommst ... mit`, `er/sie/es kommt ... mit`...
     * Ví dụ: *„Wir gehen ins Kino. Kommst du mit?“ (Chúng tôi đi xem phim. Bạn có đi cùng không?)*
   * **`vorbereiten`** (*chuẩn bị* — Tiền tố tách `vor-` + gốc `-t` `bereiten`):
     * Chia theo ngôi: `ich bereite ... vor`, `du bereitest ... vor`, `er/sie/es bereitet ... vor`...
     * Ví dụ: *„Die Lehrerin bereitet den Deutschkurs vor.“ (Cô giáo chuẩn bị cho khóa học tiếng Đức.)*
   * **`frühstücken`** (*ăn sáng* — Động từ quy tắc **KHÔNG tách**):
     * Chia theo ngôi: `ich frühstücke`, `du frühstückst`, `er/sie/es frühstückt`, `wir frühstücken`, `ihr frühstückt`, `sie/Sie frühstücken`.
     * Ví dụ: *„Um 9 Uhr frühstücke ich.“ (Vào lúc 9 giờ tôi ăn sáng.)*

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung chủ đề lọc mới: **`Thời gian, Thứ, Tháng & Lịch trình (Bài 5)`** gồm đầy đủ **38 danh từ có mạo từ (`der/die/das`), dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng từ**.

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 5: "THỜI GIAN - ĐỘNG TỪ TÁCH - HABEN IN PRÄTERITUM" (`TERMINE`)

Bài học thứ 6 trong danh sách Cấp độ A1 (`lesson_order = 6`):
* **Tiêu đề bài học**: `Bài 5: Thời gian - Động từ tách - Haben in Präteritum (Termine)`
* **Mô tả ngắn**: `Hệ thống toàn diện đơn vị thời gian, các thứ, các buổi, 12 tháng; ôn tập nâng cao 2 cách đọc giờ; làm chủ các giới từ thời gian (um, am, im, von...bis), cấu trúc khung câu với Động từ tách (Trennbare Verben), miêu tả lịch trình trong ngày (Tagesabläufe) và chia động từ "haben" ở thì quá khứ đơn (Präteritum).`

---

### HỌC PHẦN 1: ĐƠN VỊ THỜI GIAN, CÁC THỨ, CÁC BUỔI TRONG NGÀY & 12 THÁNG (`ZEITEINHEITEN, WOCHENTAGE, TAGESZEITEN & MONATE`)

#### 1.1. Bảng 1: Các Đơn vị Thời gian cơ bản (`Zeiteinheiten`)
> **Mẹo nhớ giống**: Các đơn vị nhỏ (`die Sekunde, die Minute, die Stunde, die Woche`) mang giống cái **`die`**; `der Tag` và `der Monat` mang giống đực **`der`**; `das Wochenende` và `das Jahr` mang giống trung **`das`**.

| Giống & Mạo Từ | Danh Từ Số Ít (Singular) | Dạng Số Nhiều (Plural) | Nghĩa Tiếng Việt | Câu Ví Dụ Thực Tế Khớp 100% Từ Vựng (`🔊 de-DE` + Dịch Nghĩa) |
| :---: | :--- | :--- | :--- | :--- |
| <span style="color:#f43f5e">**die (f)**</span> | **die Sekunde** | **die Sekunden** | giây | *„Eine Minute hat sechzig **Sekunden**.“*<br>*(Một phút có sáu mươi giây.)* |
| <span style="color:#f43f5e">**die (f)**</span> | **die Minute** | **die Minuten** | phút | *„Der Bus kommt in fünf **Minuten**.“*<br>*(Xe buýt sẽ đến trong năm phút nữa.)* |
| <span style="color:#f43f5e">**die (f)**</span> | **die Stunde** | **die Stunden** | giờ, tiếng đồng hồ *(thời lượng)* | *„Heute arbeite ich acht **Stunden**.“*<br>*(Hôm nay tôi làm việc tám tiếng đồng hồ.)* |
| <span style="color:#3b82f6">**der (m)**</span> | **der Tag** | **die Tage** | ngày | *„Ein Tag hat vierundzwanzig Stunden.“*<br>*(Một ngày có hai mươi tư tiếng đồng hồ.)* |
| <span style="color:#f43f5e">**die (f)**</span> | **die Woche** | **die Wochen** | tuần | *„Eine **Woche** hat sieben Tage.“*<br>*(Một tuần có bảy ngày.)* |
| <span style="color:#10b981">**das (n)**</span> | **das Wochenende** | **die Wochenenden** | cuối tuần | *„Am **Wochenende** arbeite ich nicht.“*<br>*(Vào cuối tuần tôi không làm việc.)* |
| <span style="color:#3b82f6">**der (m)**</span> | **der Monat** | **die Monate** | tháng | *„Ein **Monat** hat dreißig oder einunddreißig Tage.“*<br>*(Một tháng có ba mươi hoặc ba mươi mốt ngày.)* |
| <span style="color:#10b981">**das (n)**</span> | **das Jahr** | **die Jahre** | năm | *„Ein **Jahr** hat zwölf Monate.“*<br>*(Một năm có mười hai tháng.)* |

> **Phân biệt cực kỳ quan trọng giữa `die Uhr` và `die Stunde`**:
> * **`die Uhr`**: Dùng để chỉ **mốc thời gian trên đồng hồ** (*Es ist 8 **Uhr** = Bây giờ là 8 giờ đúng*) hoặc cái đồng hồ đeo tay/treo tường.
> * **`die Stunde`**: Dùng để chỉ **khoảng thời gian / thời lượng** kéo dài bao nhiêu tiếng đồng hồ (*Der Deutschkurs dauert zwei **Stunden** = Khóa học tiếng Đức kéo dài 2 tiếng*).

---

#### 1.2. Bảng 2: 7 Thứ trong tuần (`die Wochentage`) & 6 Buổi trong ngày (`die Tageszeiten`)
> **Quy tắc vàng**:
> * **Tất cả 7 thứ trong tuần** đều mang giống đực **`der` (`Maskulinum`)** và khi trả lời cho câu hỏi *"Khi nào? (`Wann?`)"* đều đi với giới từ **`am`** (`am Montag`, `am Sonntag`...).
> * **5 buổi trong ngày** (`der Morgen, der Vormittag, der Mittag, der Nachmittag, der Abend`) đều mang giống đực **`der`** và đi với giới từ **`am`** (`am Morgen`, `am Abend`...).
> * **Ngoại lệ duy nhất**: **`die Nacht`** *(ban đêm, 22h – 6h)* mang giống cái **`die` (`Femininum`)**, nên khi nói *"vào ban đêm"* bắt buộc phải dùng **`in der Nacht`** (tuyệt đối không dùng *am Nacht*).

| Phân Loại | Danh Từ Số Ít | Dạng Số Nhiều | Khung Giờ / Nghĩa Tiếng Việt | Cụm Giới Từ (`Wann?`) | Câu Ví Dụ Chuẩn (`🔊 de-DE` + Dịch Nghĩa) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Montag**</span> | die Montage | Thứ Hai | **am Montag** | *„**Am Montag** beginnt meine Arbeitswoche.“* *(Vào thứ Hai tuần làm việc của tôi bắt đầu.)* |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Dienstag**</span> | die Dienstage | Thứ Ba | **am Dienstag** | *„**Am Dienstag** habe ich einen Deutschkurs.“* *(Vào thứ Ba tôi có một khóa học tiếng Đức.)* |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Mittwoch**</span> | die Mittwoche | Thứ Tư | **am Mittwoch** | *„**Am Mittwoch** mache ich um 17 Uhr Sport.“* *(Vào thứ Tư tôi tập thể thao lúc 17 giờ.)* |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Donnerstag**</span> | die Donnerstage | Thứ Năm | **am Donnerstag** | *„**Am Donnerstag** kauft Anna im Supermarkt ein.“* *(Vào thứ Năm Anna đi mua sắm ở siêu thị.)* |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Freitag**</span> | die Freitage | Thứ Sáu | **am Freitag** | *„**Am Freitag** um 20 Uhr gehe ich aus.“* *(Vào thứ Sáu lúc 20 giờ tôi đi chơi.)* |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Samstag**</span><br>*(/ der Sonnabend)* | die Samstage | Thứ Bảy | **am Samstag** | *„**Am Samstag** treffen wir unsere Freunde.“* *(Vào thứ Bảy chúng tôi gặp gỡ bạn bè của mình.)* |
| **Thứ trong tuần** | <span style="color:#3b82f6">**der Sonntag**</span> | die Sonntage | Chủ Nhật | **am Sonntag** | *„**Am Sonntag** stehe ich um 8 Uhr auf.“* *(Vào Chủ nhật tôi thức dậy lúc 8 giờ.)* |
| **Buổi trong ngày** | <span style="color:#3b82f6">**der Morgen**</span> | die Morgen | Buổi sáng sớm **(06:00 – 10:00)** | **am Morgen** | *„**Am Morgen** trinke ich gern eine Tasse Kaffee.“* *(Vào buổi sáng tôi thích uống một tách cà phê.)* |
| **Buổi trong ngày** | <span style="color:#3b82f6">**der Vormittag**</span> | die Vormittage | Buổi sáng **(10:00 – 12:00)** | **am Vormittag** | *„**Am Vormittag** arbeite ich im Büro.“* *(Vào buổi sáng trước trưa tôi làm việc ở văn phòng.)* |
| **Buổi trong ngày** | <span style="color:#3b82f6">**der Mittag**</span> | die Mittage | Buổi trưa **(12:00 – 14:00)** | **am Mittag** | *„**Am Mittag** mache ich um 12 Uhr Mittagspause.“* *(Vào buổi trưa tôi nghỉ trưa lúc 12 giờ.)* |
| **Buổi trong ngày** | <span style="color:#3b82f6">**der Nachmittag**</span> | die Nachmittage | Buổi chiều **(14:00 – 18:00)** | **am Nachmittag** | *„**Am Nachmittag** trinken wir Tee und lesen ein Buch.“* *(Vào buổi chiều chúng tôi uống trà và đọc một quyển sách.)* |
| **Buổi trong ngày** | <span style="color:#3b82f6">**der Abend**</span> | die Abende | Buổi tối **(18:00 – 22:00)** | **am Abend** | *„**Am Abend** sehe ich mit meiner Familie fern.“* *(Vào buổi tối tôi xem tivi cùng gia đình mình.)* |
| **Buổi (Ngoại lệ!)** | <span style="color:#f43f5e">**die Nacht**</span> | die Nächte | Ban đêm **(22:00 – 06:00)** | **in der Nacht** ⚠️ | *„**In der Nacht** schlafe ich acht Stunden.“* *(Vào ban đêm tôi ngủ tám tiếng đồng hồ.)* |

---

#### 1.3. Bảng 3: 12 Tháng trong năm (`die Monate`) & 4 Mùa (`die Jahreszeiten`)
> **Quy tắc vàng**: Tất cả **12 tháng trong năm** và **4 mùa** đều mang giống đực **`der` (`Maskulinum`)** và đi với giới từ **`im`** (`im Januar`, `im März`, `im Juni`, `im Sommer`...).

| Tháng / Mùa | Danh Từ Tiếng Đức (`der`) | Cụm Giới Từ (`Wann?`) | Nghĩa Tiếng Việt | Câu Ví Dụ Chuẩn (`🔊 de-DE` + Dịch Nghĩa) |
| :---: | :--- | :--- | :--- | :--- |
| **Tháng 1** | <span style="color:#3b82f6">**der Januar**</span> | **im Januar** | Tháng Một | *„**Im Januar** ist es in Deutschland sehr kalt.“* *(Vào tháng Một trời ở Đức rất lạnh.)* |
| **Tháng 2** | <span style="color:#3b82f6">**der Februar**</span> | **im Februar** | Tháng Hai | *„**Im Februar** hat der Monat nur 28 oder 29 Tage.“* *(Vào tháng Hai tháng chỉ có 28 hoặc 29 ngày.)* |
| **Tháng 3** | <span style="color:#3b82f6">**der März**</span> | **im März** | Tháng Ba | *„**Im März** beginnt der Frühling.“* *(Vào tháng Ba mùa xuân bắt đầu.)* |
| **Tháng 4** | <span style="color:#3b82f6">**der April**</span> | **im April** | Tháng Tư | *„Mein Bruder hat **im April** Geburtstag.“* *(Anh trai tôi có sinh nhật vào tháng Tư.)* |
| **Tháng 5** | <span style="color:#3b82f6">**der Mai**</span> | **im Mai** | Tháng Năm | *„**Im Mai** ist das Wetter in Berlin sehr schön.“* *(Vào tháng Năm thời tiết ở Berlin rất đẹp.)* |
| **Tháng 6** | <span style="color:#3b82f6">**der Juni**</span> | **im Juni** | Tháng Sáu | *„**Im Juni** fahren wir nach Italien.“* *(Vào tháng Sáu chúng tôi đi sang Ý.)* |
| **Tháng 7** | <span style="color:#3b82f6">**der Juli**</span> | **im Juli** | Tháng Bảy | *„**Im Juli** haben die Studenten Sommerferien.“* *(Vào tháng Bảy các sinh viên có kỳ nghỉ hè.)* |
| **Tháng 8** | <span style="color:#3b82f6">**der August**</span> | **im August** | Tháng Tám | *„**Im August** ist es in Vietnam oft heiß.“* *(Vào tháng Tám trời ở Việt Nam thường nóng.)* |
| **Tháng 9** | <span style="color:#3b82f6">**der September**</span> | **im September** | Tháng Chín | *„**Im September** beginnt mein Studium.“* *(Vào tháng Chín việc học đại học của tôi bắt đầu.)* |
| **Tháng 10** | <span style="color:#3b82f6">**der Oktober**</span> | **im Oktober** | Tháng Mười | *„**Im Oktober** ist der Herbst sehr schön.“* *(Vào tháng Mười mùa thu rất đẹp.)* |
| **Tháng 11** | <span style="color:#3b82f6">**der November**</span> | **im November** | Tháng Mười Một | *„**Im November** arbeite ich viel.“* *(Vào tháng Mười Một tôi làm việc nhiều.)* |
| **Tháng 12** | <span style="color:#3b82f6">**der Dezember**</span> | **im Dezember** | Tháng Mười Hai | *„**Im Dezember** ist Weihnachten.“* *(Vào tháng Mười Hai là lễ Giáng sinh.)* |
| *Mở rộng 4 Mùa* | **der Frühling / der Sommer / der Herbst / der Winter** | **im Frühling / im Sommer / im Herbst / im Winter** | Mùa xuân / hạ / thu / đông | *„**Im Sommer** gehen wir gern schwimmen.“* *(Vào mùa hè chúng tôi thích đi bơi.)* |

---

### HỌC PHẦN 2: HỆ THỐNG HÓA 2 CÁCH ĐỌC GIỜ (`DIE UHRZEIT: OFFIZIELL & INOFFIZIELL`)

#### 2.1. Hai mẫu câu hỏi giờ chuẩn
1. **`Wie spät ist es?`** *(Bây giờ là mấy giờ?)* $\rightarrow$ **`Es ist ...`**
2. **`Wie viel Uhr ist es?`** *(Bây giờ là mấy giờ?)* $\rightarrow$ **`Es ist ...`**

#### 2.2. Bảng So sánh Cách đọc Chính thống (`Offiziell`) vs. Đời thường (`Inoffiziell`)
| Đặc điểm | Cách 1: Chính thống (`Offiziell` — Đài báo, nhà ga, sân bay) | Cách 2: Đời thường (`Inoffiziell` — Giao tiếp hàng ngày) |
| :--- | :--- | :--- |
| **Hệ khung giờ** | Hệ **24 giờ** (`0h` $\rightarrow$ `24h`) | Hệ **12 tiếng** (`1h` $\rightarrow$ `12h`). Nếu là giờ chiều/tối (VD: `20h10`), phải đổi về hệ 12 tiếng (`8h10`). |
| **Từ `"Uhr"`** | **BẮT BUỘC có từ `"Uhr"`** đứng giữa giờ và phút | **KHÔNG sử dụng từ `"Uhr"`** (trừ giờ chẵn đúng như *Es ist acht Uhr*) |
| **Công thức** | $$\text{Giờ} + \text{\textbf{Uhr}} + \text{Phút}$$ | • **Giờ hơn**: $\text{Phút} + \text{\textbf{nach}} + \text{Giờ}$<br>• **Giờ kém**: $\text{Phút kém} + \text{\textbf{vor}} + \text{Giờ kế tiếp}$<br>• **Hơn 15 phút ($\frac{1}{4}$ giờ)**: $\text{\textbf{Viertel nach}} + \text{Giờ}$<br>• **Kém 15 phút ($\frac{1}{4}$ giờ)**: $\text{\textbf{Viertel vor}} + \text{Giờ kế tiếp}$<br>• **Giờ rưỡi ($\frac{1}{2}$ giờ = 30')**: $\text{\textbf{halb}} + \text{\textbf{Giờ kế tiếp (Giờ + 1)}}$ ⚠️ |

#### 2.3. Bảng 10 Ví dụ Thực hành Chuyển đổi Giờ trên Bảng viết (Kèm Audio `de-DE`)
| Giờ Số | Cách 1: Chính thống (`Giờ + Uhr + Phút`) | Cách 2: Đời thường (`vor / nach / Viertel / halb`) | Giải thích chi tiết cách đổi sang Đời thường |
| :---: | :--- | :--- | :--- |
| **`08:15`** | *Es ist **acht Uhr fünfzehn**.* | *Es ist **Viertel nach acht**.* | Hơn 15 phút ($\frac{1}{4}$ giờ) qua mốc 8 giờ $\rightarrow$ `Viertel nach acht`. |
| **`09:30`** | *Es ist **neun Uhr dreißig**.* | *Es ist **halb zehn**.* | 9 giờ 30 phút = còn nửa tiếng nữa đến 10 giờ $\rightarrow$ `halb` + giờ kế tiếp (`zehn`). |
| **`09:05`** | *Es ist **neun Uhr fünf**.* | *Es ist **fünf nach neun**.* | 9 giờ hơn 5 phút $\rightarrow$ 5 (`fünf`) + hơn (`nach`) + 9 (`neun`). |
| **`07:50`** | *Es ist **sieben Uhr fünfzig**.* | *Es ist **zehn vor acht**.* | 7 giờ 50 phút = **8 giờ kém 10 phút** $\rightarrow$ 10 (`zehn`) + kém (`vor`) + 8 (`acht`). |
| **`20:10`** | *Es ist **zwanzig Uhr zehn**.* | *Es ist **zehn nach acht**.* | `20h10` đổi sang hệ 12 tiếng là `8h10` $\rightarrow$ 10 (`zehn`) + hơn (`nach`) + 8 (`acht`). |
| **`03:15`** | *Es ist **drei Uhr fünfzehn**.* | *Es ist **Viertel nach drei**.* | 3 giờ hơn 15 phút $\rightarrow$ `Viertel nach drei`. |
| **`05:45`** | *Es ist **fünf Uhr fünfundvierzig**.* | *Es ist **Viertel vor sechs**.* | 5 giờ 45 phút = **6 giờ kém 15 phút** $\rightarrow$ `Viertel vor sechs`. |
| **`08:30`** | *Es ist **acht Uhr dreißig**.* | *Es ist **halb neun**.* | 8 giờ rưỡi $\rightarrow$ `halb` + giờ kế tiếp (`neun`). |
| **`09:10`** | *Es ist **neun Uhr zehn**.* | *Es ist **zehn nach neun**.* | 9 giờ hơn 10 phút $\rightarrow$ `zehn nach neun`. |
| **`02:30`** | *Es ist **zwei Uhr dreißig**.* | *Es ist **halb drei**.* | 2 giờ rưỡi $\rightarrow$ `halb` + giờ kế tiếp (`drei`). |
| **`05:50`** | *Es ist **fünf Uhr fünfzig**.* | *Es ist **zehn vor sechs**.* | 5 giờ 50 phút = **6 giờ kém 10 phút** $\rightarrow$ `zehn vor sechs`. |
| **`06:05`** | *Es ist **sechs Uhr fünf**.* | *Es ist **fünf nach sechs**.* | 6 giờ hơn 5 phút $\rightarrow$ `fünf nach sechs`. |

---

### HỌC PHẦN 3: BẢNG MA TRẬN GIỚI TỪ CHỈ THỜI GIAN (`TEMPORALE PRÄPOSITIONEN: UM, AM, IM, VON...BIS`)

| Giới Từ Thời Gian | Đi Kèm Với Thành Phần Nào? | Câu Hỏi Tương Ứng | Ví Dụ Chuẩn (`🔊 de-DE`) | Dịch Nghĩa Tiếng Việt |
| :---: | :--- | :--- | :--- | :--- |
| **`um`** | **Giờ giấc cụ thể** (`Uhrzeit`) | *Um wie viel Uhr?* / *Wann?* | *„Ich stehe **um** 8 Uhr auf.“*<br>*„**Um** 12 Uhr mache ich Mittagspause.“* | Tôi thức dậy **vào lúc** 8 giờ.<br>**Vào lúc** 12 giờ tôi nghỉ trưa. |
| **`am`**<br>*(an + dem)* | • **Thứ trong tuần** (`Montag -> Sonntag`)<br>• **Buổi trong ngày** (`Morgen, Vormittag, Mittag, Nachmittag, Abend`)<br>• **Cuối tuần** (`am Wochenende`)<br>• **Ngày tháng cụ thể** | *Wann?* / *An welchem Tag?* | *„**Am** Sonntag stehe ich spät auf.“*<br>*„**Am** Freitag **um** 20 Uhr gehe ich aus.“*<br>*„**Am** Morgen trinke ich Kaffee.“* | **Vào** Chủ nhật tôi dậy muộn.<br>**Vào** thứ Sáu **lúc** 20 giờ tôi đi chơi.<br>**Vào** buổi sáng tôi uống cà phê. |
| **`im`**<br>*(in + dem)* | • **12 Tháng trong năm** (`Januar -> Dezember`)<br>• **4 Mùa trong năm** (`Frühling, Sommer, Herbst, Winter`) | *Wann?* / *In welchem Monat?* | *„**Im** Juni fahren wir nach Berlin.“*<br>*„**Im** Sommer ist es warm.“* | **Vào** tháng Sáu chúng tôi đi tới Berlin.<br>**Vào** mùa hè trời ấm áp. |
| **`in der`** *(Ngoại lệ)* | **Ban đêm** (`die Nacht` — giống cái) | *Wann?* | *„**In der** Nacht schlafe ich.“* | **Vào** ban đêm tôi ngủ. |
| **`von ... bis ...`** | **Khoảng thời gian** (*từ ... đến ...*): khoảng giờ hoặc khoảng ngày/tháng | *Von wann bis wann?* / *Wie lange?* | *„**Von** 8 **bis** 12 Uhr arbeite ich.“*<br>*„Ich arbeite **von** Montag **bis** Freitag.“* | **Từ** 8 **đến** 12 giờ tôi làm việc.<br>Tôi làm việc **từ** thứ Hai **đến** thứ Sáu. |

---

### HỌC PHẦN 4: ĐỘNG TỪ TÁCH TRONG TIẾNG ĐỨC (`TRENNBARE VERBEN` & KHUNG CÂU `SATZKLAMMER`)

#### 4.1. Khái niệm & Cấu tạo của Động từ tách (`Trennbare Verben`)
1. **Cấu tạo gồm 2 phần**:
   $$\underbrace{\text{\textbf{auf}}}_{\text{Tiền tố (Präfix)}} + \underbrace{\text{\textbf{machen}}}_{\text{Động từ gốc (Verbstamm)}} \longrightarrow \text{\textbf{aufmachen}} \text{ (mở ra)}$$
2. **Tiền tố làm thay đổi hoàn toàn ý nghĩa của động từ gốc**:
   * Động từ gốc **`machen`** *(làm)*:
     * + `auf-` $\rightarrow$ **`aufmachen`** *(mở cửa, mở sách...)*
     * + `zu-` $\rightarrow$ **`zumachen`** *(đóng cửa, gấp sách...)*
     * + `an-` $\rightarrow$ **`anmachen`** *(bật đèn, bật máy...)*
     * + `aus-` $\rightarrow$ **`ausmachen`** *(tắt đèn, tắt máy...)*
   * Danh sách các tiền tố tách phổ biến nhất ở trình độ A1 – A2:
     $$\langle \text{\textbf{an-}}, \text{ \textbf{ab-}}, \text{ \textbf{auf-}}, \text{ \textbf{aus-}}, \text{ \textbf{ein-}}, \text{ \textbf{mit-}}, \text{ \textbf{zu-}}, \text{ \textbf{vor-}}, \text{ \textbf{fern-}}, \text{ \textbf{zurück-}}, \text{ \textbf{weg-}}, \text{ \textbf{weiter-}} \rangle$$
   * *(Lưu ý mở rộng: Các tiền tố KHÔNG tách như `be-, ge-, er-, ver-, zer-, ent-, emp-, miss-` ví dụ `verstehen`, `besuchen`, `erzählen` thì luôn giữ nguyên, không bao giờ tách).*

#### 4.2. Quy tắc Khung Câu (`Satzklammer`) khi chia Động từ tách
Trong câu đơn ở thì hiện tại (`Präsens`):
* **Động từ gốc (`Verbstamm`)**: Đứng ở **vị trí thứ 2 (`V/2`)** trong câu trần thuật và câu hỏi `W-Frage` (hoặc đứng ở **vị trí thứ 1 (`V/1`)** trong câu hỏi `Ja/Nein-Frage`), được **chia theo ngôi của chủ ngữ**.
* **Tiền tố (`Präfix`)**: Bị **tách rời ra và đẩy xuống ĐỨNG CUỐI CÙNG CỦA CÂU**.

| Loại Câu | Vị Trí Số 1 | Vị Trí Số 2 (`Động từ gốc chia theo ngôi`) | Thành Phần Giữa Câu | Cuối Câu (`Tiền tố tách`) | Dịch Nghĩa Tiếng Việt |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Câu trần thuật (Chủ ngữ đứng đầu)** | **Ich** | **mache** | die Tür | **auf**. | Tôi mở cánh cửa ra. |
| **Câu trần thuật (Đảo trạng ngữ lên đầu)** | **Am Sonntag** | **stehe** | ich um 8 Uhr | **auf**. | Vào Chủ nhật tôi thức dậy lúc 8 giờ. |
| **Câu hỏi W-Frage** | **Wann** | **stehst** | du am Sonntag | **auf**? | Khi nào bạn thức dậy vào Chủ nhật? |
| **Câu hỏi W-Frage** | **Wann** | **gehst** | du am Freitag | **aus**? | Khi nào bạn đi chơi vào thứ Sáu? |
| **Câu hỏi Ja/Nein-Frage** | *(Đảo V lên 1)* | **Machst** | du bitte das Fenster | **zu**? | Bạn làm ơn đóng cửa sổ lại nhé? |
| **Đi kèm Động từ khuyết thiếu (`möchten / können`)** | **Ich** | **möchte** *(Modalverb V2)* | die Tür | **aufmachen**. *(Nguyên mẫu cuối câu)* | Tôi muốn mở cánh cửa ra. |

#### 4.3. Bảng Chia Động Từ Tách Theo 9 Ngôi Nhân Xưng (Trực quan hóa cho người học)
| Ngôi nhân xưng | `aufmachen` *(mở)* | `aufstehen` *(thức dậy)* | `ausgehen` *(đi chơi)* | `einkaufen` *(mua sắm)* | `anrufen` *(gọi điện)* | `fernsehen` *(xem tivi - biến âm `e -> ie`)* |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **ich** | **mache** ... **auf** | **stehe** ... **auf** | **gehe** ... **aus** | **kaufe** ... **ein** | **rufe** ... **an** | **sehe** ... **fern** |
| **du** | **machst** ... **auf** | **stehst** ... **auf** | **gehst** ... **aus** | **kaufst** ... **ein** | **rufst** ... **an** | **s<u>ieh</u>st** ... **fern** |
| **er / sie / es** | **macht** ... **auf** | **steht** ... **auf** | **geht** ... **aus** | **kauft** ... **ein** | **ruft** ... **an** | **s<u>ieh</u>t** ... **fern** |
| **wir** | **machen** ... **auf** | **stehen** ... **auf** | **gehen** ... **aus** | **kaufen** ... **ein** | **rufen** ... **an** | **sehen** ... **fern** |
| **ihr** | **macht** ... **auf** | **steht** ... **auf** | **geht** ... **aus** | **kauft** ... **ein** | **ruft** ... **an** | **seht** ... **fern** |
| **sie / Sie** | **machen** ... **auf** | **stehen** ... **auf** | **gehen** ... **aus** | **kaufen** ... **ein** | **rufen** ... **an** | **sehen** ... **fern** |

---

### HỌC PHẦN 5: DIỄN BIẾN TRONG NGÀY (`TAGESABLÄUFE`) & QUY TẮC ĐẢO NGỮ VỊ TRÍ SỐ 2 (`INVERSION`)

Khi bạn đưa trạng ngữ chỉ thời gian (`Am Sonntag`, `Um 9 Uhr`, `Von 8 bis 12 Uhr`, `Am Freitag um 20 Uhr`) lên đứng ở **vị trí số 1** để nhấn mạnh, thì **động từ chia theo ngôi bắt buộc vẫn phải đứng ở vị trí số 2**, và **chủ ngữ (`ich, du, wir...`) phải lùi sang vị trí số 3**!

#### Bảng 7 Mẫu Câu Hỏi – Đáp Lịch Trình Hàng Ngày Trên Bảng Viết (`Tagesabläufe`)
| STT | Câu Hỏi Lịch Trình (`W-Frage`) + Dịch Nghĩa | Câu Trả Lời Chuẩn (`Đảo ngữ V2`) + Dịch Nghĩa | Phân Tích Cấu Trúc Ngữ Pháp |
| :---: | :--- | :--- | :--- |
| **1** | **Wann stehst du am Sonntag auf?**<br>*(Bạn thức dậy lúc nào vào Chủ nhật?)* | **<u>Am Sonntag</u> <u>stehe</u> <u>ich</u> um 8 Uhr <u>auf</u>.**<br>*(Vào Chủ nhật tôi thức dậy vào lúc 8 giờ.)* | • Vị trí 1: `Am Sonntag`<br>• Vị trí 2 (V2): `stehe`<br>• Vị trí 3 (S): `ich`<br>• Cuối câu (Präfix): `auf` |
| **2** | **Um wie viel Uhr frühstückst du?**<br>*(Bạn ăn sáng vào lúc mấy giờ?)* | **<u>Um 9 Uhr</u> <u>frühstücke</u> <u>ich</u>.**<br>*(Vào lúc 9 giờ tôi ăn sáng.)* | • `frühstücken` là động từ **không tách**.<br>• Vị trí 1: `Um 9 Uhr` $\rightarrow$ Vị trí 2: `frühstücke` $\rightarrow$ Vị trí 3: `ich`. |
| **3** | **Wann machst du Mittagspause?**<br>*(Khi nào bạn nghỉ trưa?)* | **<u>Um 12 Uhr</u> <u>mache</u> <u>ich</u> Mittagspause.**<br>*(Vào lúc 12 giờ tôi nghỉ trưa.)* | • Cụm cố định: `Mittagspause machen` (nghỉ trưa). |
| **4** | **Von wann bis wann arbeitest du?**<br>*(Bạn làm việc từ mấy giờ đến mấy giờ?)* | **<u>Von 8 bis 12 Uhr</u> <u>arbeite</u> <u>ich</u>.**<br>*(Từ 8 giờ đến 12 giờ tôi làm việc.)* | • Động từ `arbeiten` có gốc kết thúc bằng `-t` nên ngôi `du` thêm `-est` (`arbeitest`). |
| **5** | **Wann gehst du am Freitag aus?**<br>*(Khi nào bạn đi chơi vào thứ Sáu?)* | **<u>Am Freitag um 20 Uhr</u> <u>gehe</u> <u>ich</u> <u>aus</u>.**<br>*(Vào thứ Sáu lúc 20 giờ tôi đi ra ngoài/đi chơi.)* | • Động từ tách `ausgehen`: gốc `gehe` đứng ở vị trí 2, tiền tố `aus` đứng cuối câu. |
| **6** | **Wann machst du Sport?**<br>*(Khi nào bạn tập thể thao?)* | **<u>Um 17 Uhr</u> <u>mache</u> <u>ich</u> Sport.**<br>*(Vào lúc 17 giờ tôi tập thể thao.)* | • Cụm cố định: `Sport machen` (tập thể thao). |
| **7** | **Wann gehst du ins Bett?**<br>*(Khi nào bạn đi ngủ?)* | **<u>Um 22 Uhr</u> <u>gehe</u> <u>ich</u> ins Bett.**<br>*(Vào lúc 22 giờ tôi đi ngủ.)* | • Cụm cố định: `ins Bett gehen` (`ins` = `in das Bett`). |

---

### HỌC PHẦN 6: ĐỘNG TỪ `"HABEN"` Ở THÌ QUÁ KHỨ ĐƠN (`"HABEN" IM PRÄTERITUM`) & ĐỐI CHIẾU VỚI `"SEIN"`

Ở Bài 3, chúng ta đã học quá khứ đơn (`Präteritum`) của động từ `sein` (`war / warst / waren / wart`). Sang Bài 5, chúng ta hoàn thiện mảnh ghép quan trọng thứ hai: quá khứ đơn của động từ **`haben`** *(đã có)*. Khi nói hoặc viết về quá khứ với 2 động từ `sein` và `haben`, người Đức ưu tiên dùng trực tiếp **`Präteritum` (`war` / `hatte`)** vì ngắn gọn và tự nhiên.

#### 6.1. Bảng Tổng Hợp Chia Động Từ `sein` và `haben` ở `Präsens` (Hiện tại) vs. `Präteritum` (Quá khứ đơn)
| Ngôi nhân xưng (`Personalpronomen`) | Nghĩa Tiếng Việt | `<sein>` ở Hiện tại (`Präsens`) | `<sein>` ở Quá khứ (`Präteritum`: *đã thì/là/ở*) | `<haben>` ở Hiện tại (`Präsens`) | `<haben>` ở Quá khứ (`Präteritum`: *đã có*) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **ich** | tôi | bin | **war** | habe | **hatte** |
| **du** | bạn | bist | **warst** | hast | **hattest** |
| **er / sie / es** | anh ấy / cô ấy / nó | ist | **war** | hat | **hatte** |
| **wir** | chúng tôi, chúng ta | sind | **waren** | haben | **hatten** |
| **ihr** | các bạn | seid | **wart** | habt | **hattet** |
| **sie / Sie** | họ / Ngài | sind | **waren** | haben | **hatten** |

> **Đặc điểm cần nhớ của `haben` ở `Präteritum`**:
> * Ngôi **`ich`** và ngôi **`er / sie / es`** có cách chia **giống hệt nhau**: đều là **`hatte`** (tương tự như `ich war` = `er/sie/es war`).
> * Ngôi **`wir`** và ngôi **`sie / Sie`** có cách chia **giống hệt nhau**: đều là **`hatten`**.
> * Lưu ý sau `haben` (`habe/hast/hat` hay `hatte/hattest/hatten`) luôn là tân ngữ trực tiếp ở **Cách 4 (`Akkusativ`)**!

#### 6.2. Bảng 4 Câu Đối Chiếu Quá Khứ (`Gestern` - Hôm qua) vs. Hiện Tại (`Heute` - Hôm nay) Trên Bảng Viết
*Từ vựng trọng tâm trong các câu ví dụ:*
* `die Zeit` (thời gian) $\rightarrow$ `keine Zeit haben` (không có thời gian) >< `viel Zeit haben` (có nhiều thời gian).
* `die Panne` (sự cố hỏng xe dọc đường) $\rightarrow$ `eine Panne haben` (gặp sự cố hỏng xe).
* `das Glück` (sự may mắn) $\rightarrow$ `kein Glück haben` (không gặp may) >< `viel Glück haben` (rất may mắn).
* `das Geld` (tiền bạc) $\rightarrow$ `kein Geld haben` (không có tiền) >< `viel Geld haben` (có nhiều tiền).

| STT | Mệnh Đề Quá Khứ (`Gestern` + `Präteritum`) | Mệnh Đề Hiện Tại (`aber heute` + `Präsens`) | Bản Dịch Tiếng Việt Chuẩn Xác |
| :---: | :--- | :--- | :--- |
| **1** | **Gestern <u>hatte</u> ich keine Zeit,** | **aber heute <u>habe</u> ich viel Zeit.** | Hôm qua tôi đã không có thời gian, nhưng hôm nay tôi có nhiều thời gian. |
| **2** | **Gestern <u>hatten</u> wir eine Panne,** | **aber heute <u>haben</u> wir keine Panne.** | Hôm qua chúng tôi đã gặp một sự cố (hỏng xe), nhưng hôm nay chúng tôi không gặp sự cố nào. |
| **3** | **Gestern <u>hattest</u> du kein Glück,** | **aber heute <u>hast</u> du viel Glück.** | Hôm qua bạn đã không gặp may, nhưng hôm nay bạn có nhiều may mắn. |
| **4** | **Gestern <u>hatte</u> er kein Geld,** | **aber heute <u>hat</u> er viel Geld.** | Hôm qua anh ấy đã không có tiền, nhưng hôm nay anh ấy có nhiều tiền. |

---

#### 6.3. Phân Tích Bức Thư Mẫu Của Maria Gửi Thomas (`"Sein" & "Haben" im Präteritum`)
Hiển thị bức thư dưới dạng hộp tương tác có nút **`🔊 Nghe đọc toàn bộ bức thư (de-DE)`**, bản dịch tiếng Việt từng câu và giải thích ngữ pháp từng vị trí gạch chân:

> **Lieber Thomas,**
> Entschuldigung, wir **<u>waren</u>** *(1)* gestern Abend nicht bei der Party. Wir **<u>hatten</u>** *(2)* eine Panne. Ich **<u>hatte</u>** *(3)* kein Handy und kein Geld für den Bus. Und ein Rad **<u>hatten</u>** *(4)* Joan und ich auch nicht. Joan **<u>hatte</u>** *(5)* ein Handy, aber sie **<u>hatte</u>** *(6)* deine Nummer nicht. **<u>Hattet</u>** *(7)* ihr eine tolle Party?
> **Liebe Grüße**
> **Maria**

* **Dịch nghĩa toàn văn bức thư**:
  > *Thomas thân mến,*
  > *Xin lỗi nhé, tối hôm qua chúng mình đã không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe. Mình đã không có điện thoại di động và cũng không có tiền đi xe buýt. Và một chiếc xe đạp thì Joan và mình cũng đã không có. Joan đã có một chiếc điện thoại di động, nhưng cô ấy lại không có số của bạn. Các bạn đã có một bữa tiệc tuyệt vời chứ?*
  > *Thân mến,*
  > *Maria*

* **Giải thích ngữ pháp 7 vị trí chia động từ trong thư**:
  1. **`waren`**: Chủ ngữ `wir`, chỉ trạng thái ở địa điểm (`bei der Party`) vào tối hôm qua (`gestern Abend`) $\rightarrow$ Dùng `sein` ở Präteritum là `waren`.
  2. **`hatten`**: Chủ ngữ `wir`, đi với danh từ `eine Panne` (gặp một sự cố) $\rightarrow$ Dùng `haben` ở Präteritum là `hatten`.
  3. **`hatte`**: Chủ ngữ `Ich` $\rightarrow$ `haben` ở Präteritum chia là `hatte` (`kein Handy und kein Geld`).
  4. **`hatten`**: Chủ ngữ là `Joan und ich` (= ngôi `wir`), tân ngữ `ein Rad` (*das Fahrrad / das Rad* = chiếc xe đạp) được đưa lên đầu câu để nhấn mạnh, động từ vẫn đứng ở vị trí số 2 chia theo `wir` là `hatten`.
  5. **`hatte`**: Chủ ngữ `Joan` (= ngôi `sie` - cô ấy) $\rightarrow$ `haben` ở Präteritum chia là `hatte`.
  6. **`hatte`**: Chủ ngữ `sie` (cô ấy) $\rightarrow$ `hatte` (`deine Nummer nicht` - không có số điện thoại của bạn).
  7. **`Hattet`**: Câu hỏi `Ja/Nein-Frage` đảo động từ lên đầu câu với chủ ngữ `ihr` (các bạn) $\rightarrow$ `Hattet ihr eine tolle Party?`.

---

## PHẦN 3: KHO 50 BÀI TẬP CHUẨN 9 DẠNG CỦA BÀI 5 (`lessons/a1/seed_a1_b5.py`) & HỆ THỐNG RANDOM ĐỔI ĐỀ

Tuân thủ quy chuẩn mới áp dụng từ **Bài 5 (A1)** trở đi, kho **50 câu hỏi** của Bài 5 phải được phân bổ đầy đủ vào **9 dạng bài tập tương tác** và có bộ sinh đề ngẫu nhiên (`Dynamic Exercise Randomizer`) đảm bảo **Câu hỏi – Đáp án – Dịch nghĩa – Giải thích khớp nhau 100%**:

### 3.1. Bảng Phân Bổ 50 Câu Hỏi Bài 5 Theo 9 Dạng Bài Tập

| STT | Mã Dạng (`type`) | Tên Dạng Bài Tập Hiển Thị | Số Lượng | Nội Dung Trọng Tâm Của Các Câu Hỏi Trong Bài 5 |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **`trac_nghiem`** | **Trắc nghiệm (Multiple Choice)** | **8 câu** | Chọn giới từ thời gian (`um / am / im / in der / von...bis`), chọn dạng chia đúng của động từ tách, chọn `war/waren` vs. `hatte/hattest/hatten/hattet`, chọn cách đọc giờ `halb / Viertel vor / Viertel nach`. |
| **2** | **`dien_khuyet`** | **Điền khuyết (Fill in the Blank)** | **7 câu** | Điền tiền tố tách (`auf, aus, an, zu, ein, mit, fern`) vào cuối câu; điền `hatte, hattest, hatten, hattet` vào bức thư của Maria và các câu `Gestern ... aber heute ...`; điền giới từ `am, um, im`. |
| **3** | **`dich_nghia_vd`** | **Dịch từ/cụm từ: Việt $\rightarrow$ Đức** | **6 câu** | Dịch các thứ, các buổi, các tháng, các đơn vị thời gian và động từ tách sang tiếng Đức (*thứ Tư, cuối tuần, vào ban đêm, thức dậy, sự cố hỏng xe, buổi chiều...*). |
| **4** | **`dich_nghia_dv`** | **Dịch từ/cụm từ: Đức $\rightarrow$ Việt** | **6 câu** | Dịch các cụm thời gian, giờ giấc đời thường và động từ tách sang tiếng Việt (*das Wochenende, Viertel vor sechs, halb drei, die Mittagspause, einkaufen, gestern Abend...*). |
| **5** | **`noi_o`** | **Nối ô từ trái qua phải (Matching Pairs)** | **6 bài** | • Bài 1: Nối Giờ chính thống $\leftrightarrow$ Giờ đời thường (`8h15 -> Viertel nach acht`, `2h30 -> halb drei`, `5h50 -> zehn vor sechs`, `9h10 -> zehn nach neun`)<br>• Bài 2: Nối Giới từ (`um, am, im, in der`) $\leftrightarrow$ Danh từ thời gian (`8 Uhr, Sonntag, Juni, Nacht`)<br>• Bài 3: Nối Động từ tách $\leftrightarrow$ Nghĩa tiếng Việt (`aufstehen, ausgehen, aufmachen, einkaufen`)<br>• Bài 4: Nối Chủ ngữ $\leftrightarrow$ Dạng chia `haben` ở Präteritum (`ich -> hatte`, `du -> hattest`, `wir -> hatten`, `ihr -> hattet`)<br>• Bài 5: Nối Buổi trong ngày $\leftrightarrow$ Khung giờ chuẩn (`der Morgen -> 6-10h`, `der Vormittag -> 10-12h`, `der Nachmittag -> 14-18h`, `die Nacht -> 22-6h`)<br>• Bài 6: Nối Câu hỏi `Tagesabläufe` $\leftrightarrow$ Câu trả lời tương ứng. |
| **6** | **`dien_tao_cau`** | **Điền vào chỗ trống để tạo thành câu** | **5 câu** | Điền 2–3 chỗ trống để tạo câu hoàn chỉnh có khung câu động từ tách (`Am Sonntag [stehe] ich um 8 Uhr [auf]`, `Am Freitag um 20 Uhr [gehe] ich [aus]`, `Ich [mache] die Tür [auf]`, `Gestern [hatten] wir eine Panne, aber heute [haben] wir keine Panne`, `Von 8 [bis] 12 Uhr [arbeite] ich`). |
| **7** | **`nghe_dien`** | **Nghe giọng đọc `de-DE` và điền từ** | **4 câu** | Nghe câu phát âm chuẩn `de-DE` (tốc độ `1.0x` và `0.65x`) và điền từ còn thiếu: nghe giờ giấc (`halb drei`, `Viertel nach acht`), nghe động từ tách (`aufstehen`, `ausgehen`) và nghe câu trong bức thư của Maria (`hatten`, `Panne`). |
| **8** | **`dich_cau_vd`** | **Dịch câu: Việt $\rightarrow$ Đức** | **4 câu** | Dịch các câu lịch trình và quá khứ sang tiếng Đức (chấm linh hoạt đa đáp án):<br>1. *"Vào Chủ nhật tôi thức dậy lúc 8 giờ."*<br>2. *"Từ 8 giờ đến 12 giờ tôi làm việc."*<br>3. *"Hôm qua tôi không có thời gian, nhưng hôm nay tôi có nhiều thời gian."*<br>4. *"Vào thứ Sáu lúc 20 giờ tôi đi chơi."* |
| **9** | **`dich_cau_dv`** | **Dịch câu: Đức $\rightarrow$ Việt** | **4 câu** | Dịch các câu tiếng Đức trong bài sang tiếng Việt (chấm linh hoạt đa đáp án):<br>1. *„Ich mache die Tür auf.“*<br>2. *„Um 12 Uhr mache ich Mittagspause.“*<br>3. *„Gestern hatten wir eine Panne, aber heute haben wir keine Panne.“*<br>4. *„Um 22 Uhr gehe ich ins Bett.“* |
| | | **TỔNG CỘNG BÀI 5** | **50 CÂU** | **Đầy đủ 9 dạng bài + Giải thích chi tiết + Dịch nghĩa 100%** |

---

### 3.2. Danh sách Chi Tiết 50 Câu Hỏi Chuẩn Xác Của Bài 5 (Để Seed Vào `lessons/a1/seed_a1_b5.py`)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 8 Câu)
1. **Câu 1**: Chọn giới từ chỉ thời gian đúng điền vào câu: *„___ Sonntag stehe ich ___ 8 Uhr auf.“*
   * Đáp án: `A. Am / um` (Đúng) | `B. Im / um` | `C. Um / am` | `D. Am / im`
   * Dịch nghĩa câu: *"Vào Chủ nhật tôi thức dậy vào lúc 8 giờ."*
   * Giải thích: Thứ trong tuần (`Sonntag`) đi với giới từ `am`; giờ giấc cụ thể (`8 Uhr`) đi với giới từ `um`.
2. **Câu 2**: Cách đọc giờ đời thường (`Inoffiziell`) nào sau đây tương ứng với **`2h30`** (*zwei Uhr dreißig*)?
   * Đáp án: `A. halb zwei` | `B. halb drei` (Đúng) | `C. Viertel nach zwei` | `D. dreißig nach zwei`
   * Dịch nghĩa câu: *"2 giờ 30 phút (2 giờ rưỡi) đọc là 'halb drei'."*
   * Giải thích: Trong tiếng Đức, giờ rưỡi dùng công thức `halb + giờ kế tiếp (giờ + 1)`. Vì vậy `2h30` phải tính tới mốc 3 giờ là `halb drei`.
3. **Câu 3**: Cách đọc giờ đời thường nào sau đây tương ứng với **`5h50`** (*fünf Uhr fünfzig*)?
   * Đáp án: `A. zehn nach fünf` | `B. fünfzig nach fünf` | `C. zehn vor sechs` (Đúng) | `D. Viertel vor sechs`
   * Dịch nghĩa câu: *"5 giờ 50 phút (6 giờ kém 10 phút) đọc là 'zehn vor sechs'."*
   * Giải thích: `5h50` tức là còn thiếu 10 phút nữa là đến 6 giờ (6 giờ kém 10), áp dụng công thức `Phút kém (zehn) + vor + Giờ kế tiếp (sechs)`.
4. **Câu 4**: Chọn dạng đúng của động từ tách `aufmachen` (mở) cho câu: *„Es ist heiß. Ich ___ das Fenster ___.“*
   * Đáp án: `A. aufmache / —` | `B. mache / auf` (Đúng) | `C. machst / auf` | `D. auf / mache`
   * Dịch nghĩa câu: *"Trời nóng quá. Tôi mở cửa sổ ra."*
   * Giải thích: Với động từ tách `aufmachen`, trong câu đơn động từ gốc `machen` đứng ở vị trí số 2 chia theo ngôi `ich` là `mache`, còn tiền tố `auf` tách ra đứng ở cuối câu.
5. **Câu 5**: Chọn giới từ đúng cho danh từ chỉ buổi `die Nacht` (ban đêm): *„___ Nacht schlafe ich acht Stunden.“*
   * Đáp án: `A. Am` | `B. Im` | `C. In der` (Đúng) | `D. Um`
   * Dịch nghĩa câu: *"Vào ban đêm tôi ngủ tám tiếng đồng hồ."*
   * Giải thích: Khác với các buổi khác mang giống đực (`am Morgen, am Abend`), riêng `die Nacht` mang giống cái nên bắt buộc phải dùng cụm giới từ `in der Nacht`.
6. **Câu 6**: Chọn từ để hỏi đúng cho câu trả lời *„Von 8 bis 12 Uhr arbeite ich.“*: *„___ arbeitest du?“*
   * Đáp án: `A. Von wann bis wann` (Đúng) | `B. Um wie viel Uhr` | `C. Woher` | `D. Wer`
   * Dịch nghĩa câu: *"Bạn làm việc từ lúc nào đến lúc nào? — Từ 8 giờ đến 12 giờ tôi làm việc."*
   * Giải thích: Để hỏi khoảng thời gian bắt đầu và kết thúc tương ứng với câu trả lời `Von ... bis ...`, ta dùng cụm từ để hỏi `Von wann bis wann...?`.
7. **Câu 7**: Chọn dạng quá khứ đơn (`Präteritum`) đúng của `haben` trong câu: *„Gestern ___ du kein Glück, aber heute hast du viel Glück.“*
   * Đáp án: `A. hatte` | `B. hattest` (Đúng) | `C. hattet` | `D. warst`
   * Dịch nghĩa câu: *"Hôm qua bạn đã không gặp may, nhưng hôm nay bạn có nhiều may mắn."*
   * Giải thích: Chủ ngữ là ngôi `du` (bạn), động từ `haben` chia ở thì quá khứ đơn (`Präteritum`) cho ngôi `du` là `hattest`.
8. **Câu 8**: Trong bức thư của Maria, câu hỏi cuối thư gửi cho các bạn của Thomas (`ihr`) được viết như thế nào?
   * Đáp án: `A. Hattest ihr eine tolle Party?` | `B. Hatten ihr eine tolle Party?` | `C. Hattet ihr eine tolle Party?` (Đúng) | `D. Wart ihr eine tolle Party?`
   * Dịch nghĩa câu: *"Các bạn đã có một bữa tiệc tuyệt vời chứ?"*
   * Giải thích: Với chủ ngữ `ihr` (các bạn), động từ `haben` ở thì `Präteritum` được chia là `hattet`.

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 7 Câu)
9. **Câu 9**: Điền giới từ chỉ thời gian thích hợp vào chỗ trống: *„Mein Bruder hat ___ Juni Geburtstag.“*
   * Đáp án chấp nhận: `["im", "Im"]`
   * Dịch nghĩa câu: *"Anh trai tôi có sinh nhật vào tháng Sáu."*
   * Giải thích: Tất cả 12 tháng trong năm (`der Januar` $\rightarrow$ `der Dezember`) đều đi với giới từ `im`.
10. **Câu 10**: Điền tiền tố tách còn thiếu vào cuối câu: *„Wann stehst du am Sonntag ___?“* *(Nghĩa: Khi nào bạn thức dậy vào Chủ nhật?)*
    * Đáp án chấp nhận: `["auf"]`
    * Dịch nghĩa câu: *"Khi nào bạn thức dậy vào Chủ nhật?"*
    * Giải thích: Động từ *"thức dậy"* là `aufstehen`, khi chia với `du` thì `stehst` đứng ở vị trí số 2 và tiền tố `auf` đứng ở cuối câu.
11. **Câu 11**: Điền tiền tố tách còn thiếu vào cuối câu: *„Am Freitag um 20 Uhr gehe ich ___.“* *(Nghĩa: Vào thứ Sáu lúc 20 giờ tôi đi chơi / đi ra ngoài.)*
    * Đáp án chấp nhận: `["aus"]`
    * Dịch nghĩa câu: *"Vào thứ Sáu lúc 20 giờ tôi đi ra ngoài / đi chơi."*
    * Giải thích: Động từ *"đi chơi / đi ra ngoài"* là `ausgehen` (`ich gehe ... aus`).
12. **Câu 12**: Điền dạng chia đúng của động từ `haben` ở thì quá khứ đơn (`Präteritum`): *„Gestern ___ ich keine Zeit, aber heute habe ich viel Zeit.“*
    * Đáp án chấp nhận: `["hatte"]`
    * Dịch nghĩa câu: *"Hôm qua tôi đã không có thời gian, nhưng hôm nay tôi có nhiều thời gian."*
    * Giải thích: Ngôi `ich` của động từ `haben` ở thì `Präteritum` là `hatte`.
13. **Câu 13**: Điền dạng chia đúng của động từ `haben` ở thì quá khứ đơn (`Präteritum`): *„Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir ___ eine Panne.“*
    * Đáp án chấp nhận: `["hatten"]`
    * Dịch nghĩa câu: *"Xin lỗi, tối qua chúng mình không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe."*
    * Giải thích: Ngôi `wir` của động từ `haben` ở thì `Präteritum` là `hatten`.
14. **Câu 14**: Điền dạng chia đúng của động từ `haben` ở thì quá khứ đơn (`Präteritum`): *„Joan ___ ein Handy, aber sie hatte deine Nummer nicht.“*
    * Đáp án chấp nhận: `["hatte"]`
    * Dịch nghĩa câu: *"Joan đã có một chiếc điện thoại di động, nhưng cô ấy đã không có số của bạn."*
    * Giải thích: Chủ ngữ `Joan` tương ứng với ngôi thứ 3 số ít (`sie` - cô ấy), nên `haben` ở `Präteritum` chia là `hatte`.
15. **Câu 15**: Điền từ chỉ giờ đời thường còn thiếu cho mốc **`8h15`**: *„Es ist ___ nach acht.“*
    * Đáp án chấp nhận: `["Viertel", "viertel"]`
    * Dịch nghĩa câu: *"Bây giờ là 8 giờ 15 phút (Một phần tư giờ sau mốc 8 giờ)."*
    * Giải thích: 15 phút bằng $\frac{1}{4}$ giờ (`Viertel`), vì vậy `8h15` đọc là `Viertel nach acht`.

---

#### NHÓM 3: DỊCH NGHĨA TỪ / CỤM TỪ VIỆT $\rightarrow$ ĐỨC (`dich_nghia_vd` — 6 Câu)
16. **Câu 16**: Dịch sang tiếng Đức: ***"cuối tuần"***
    * Đáp án chấp nhận: `["das Wochenende", "Wochenende", "ein Wochenende"]`
    * Giải thích: *"Cuối tuần"* trong tiếng Đức là danh từ giống trung `das Wochenende` (số nhiều: `die Wochenenden`).
17. **Câu 17**: Dịch sang tiếng Đức: ***"thứ Tư"***
    * Đáp án chấp nhận: `["der Mittwoch", "Mittwoch"]`
    * Giải thích: *"Thứ Tư"* trong tiếng Đức là `der Mittwoch` (tất cả các thứ trong tuần đều mang giống đực `der`).
18. **Câu 18**: Dịch sang tiếng Đức (động từ nguyên mẫu): ***"thức dậy"***
    * Đáp án chấp nhận: `["aufstehen"]`
    * Giải thích: *"Thức dậy"* là động từ tách `aufstehen` (tiền tố `auf-` + động từ gốc `stehen`).
19. **Câu 19**: Dịch sang tiếng Đức (động từ nguyên mẫu): ***"ăn sáng"***
    * Đáp án chấp nhận: `["frühstücken", "fruehstuecken"]`
    * Giải thích: *"Ăn sáng"* trong tiếng Đức là động từ không tách `frühstücken`.
20. **Câu 20**: Dịch sang tiếng Đức: ***"sự cố (hỏng xe)"***
    * Đáp án chấp nhận: `["die Panne", "Panne", "eine Panne"]`
    * Giải thích: *"Sự cố / hỏng xe dọc đường"* là danh từ giống cái `die Panne` (*Wir hatten eine Panne*).
21. **Câu 21**: Dịch cụm giới từ thời gian sau sang tiếng Đức: ***"từ thứ Hai đến thứ Sáu"***
    * Đáp án chấp nhận: `["von Montag bis Freitag"]`
    * Giải thích: Cấu trúc chỉ khoảng thời gian *"từ ... đến ..."* là `von ... bis ...` $\rightarrow$ `von Montag bis Freitag`.

---

#### NHÓM 4: DỊCH NGHĨA TỪ / CỤM TỪ ĐỨC $\rightarrow$ VIỆT (`dich_nghia_dv` — 6 Câu)
22. **Câu 22**: Dịch sang tiếng Việt: ***„der Nachmittag“***
    * Đáp án chấp nhận: `["buổi chiều", "chiều"]`
    * Giải thích: `der Nachmittag` là buổi chiều (khung giờ từ 14h đến 18h).
23. **Câu 23**: Dịch sang tiếng Việt: ***„die Stunde“***
    * Đáp án chấp nhận: `["giờ", "tiếng", "tiếng đồng hồ", "giờ đồng hồ", "một giờ", "một tiếng"]`
    * Giải thích: `die Stunde` (số nhiều: `die Stunden`) có nghĩa là giờ / tiếng đồng hồ (chỉ khoảng thời gian).
24. **Câu 24**: Dịch sang tiếng Việt: ***„aufmachen“***
    * Đáp án chấp nhận: `["mở", "mở ra", "mở cửa"]`
    * Giải thích: Động từ tách `aufmachen` (`auf-` + `machen`) có nghĩa là mở ra (như mở cửa, mở sách...).
25. **Câu 25**: Dịch sang tiếng Việt: ***„ausgehen“***
    * Đáp án chấp nhận: `["đi chơi", "đi ra ngoài", "ra ngoài", "đi dạo phố", "đi chơi tối"]`
    * Giải thích: Động từ tách `ausgehen` (`aus-` + `gehen`) có nghĩa là đi ra ngoài / đi chơi.
26. **Câu 26**: Dịch cách nói giờ sau sang tiếng Việt: ***„halb drei“***
    * Đáp án chấp nhận: `["2 giờ rưỡi", "hai giờ rưỡi", "2 giờ 30", "2 giờ 30 phút", "hai giờ ba mươi phút", "2h30"]`
    * Giải thích: `halb drei` (nửa tiếng trước mốc 3 giờ) có nghĩa là **2 giờ rưỡi (2h30)**.
27. **Câu 27**: Dịch cụm từ sau sang tiếng Việt: ***„Mittagspause machen“***
    * Đáp án chấp nhận: `["nghỉ trưa", "làm giờ nghỉ trưa", "nghỉ ăn trưa", "giải lao buổi trưa"]`
    * Giải thích: `die Mittagspause` = giờ nghỉ trưa; `Mittagspause machen` = nghỉ trưa.

---

#### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 6 Bài, mỗi bài 4 cặp)
28. **Câu 28 (Bài nối ô 1)**: Nối giờ chính thống ở cột trái với cách nói giờ đời thường tương ứng ở cột phải:
    * `acht Uhr fünfzehn (8h15)` $\longleftrightarrow$ `Viertel nach acht`
    * `neun Uhr zehn (9h10)` $\longleftrightarrow$ `zehn nach neun`
    * `zwei Uhr dreißig (2h30)` $\longleftrightarrow$ `halb drei`
    * `fünf Uhr fünfzig (5h50)` $\longleftrightarrow$ `zehn vor sechs`
29. **Câu 29 (Bài nối ô 2)**: Nối giới từ thời gian ở cột trái với danh từ phù hợp ở cột phải:
    * `um` $\longleftrightarrow$ `8 Uhr (lúc 8 giờ)`
    * `am` $\longleftrightarrow$ `Sonntag / Morgen (vào Chủ nhật / buổi sáng)`
    * `im` $\longleftrightarrow$ `Juni / Sommer (vào tháng Sáu / mùa hè)`
    * `in der` $\longleftrightarrow$ `Nacht (vào ban đêm)`
30. **Câu 30 (Bài nối ô 3)**: Nối các động từ trong bài ở cột trái với nghĩa tiếng Việt chính xác ở cột phải:
    * `aufstehen` $\longleftrightarrow$ `thức dậy (động từ tách)`
    * `frühstücken` $\longleftrightarrow$ `ăn sáng (động từ không tách)`
    * `ausgehen` $\longleftrightarrow$ `đi ra ngoài / đi chơi (động từ tách)`
    * `aufmachen` $\longleftrightarrow$ `mở ra (động từ tách)`
31. **Câu 31 (Bài nối ô 4)**: Nối đại từ nhân xưng ở cột trái với dạng chia đúng của động từ `haben` ở thì quá khứ đơn (`Präteritum`) ở cột phải:
    * `ich / er / sie / es` $\longleftrightarrow$ `hatte`
    * `du` $\longleftrightarrow$ `hattest`
    * `wir / sie / Sie` $\longleftrightarrow$ `hatten`
    * `ihr` $\longleftrightarrow$ `hattet`
32. **Câu 32 (Bài nối ô 5)**: Nối các buổi trong ngày ở cột trái với khung giờ và nghĩa tiếng Việt ở cột phải:
    * `der Morgen` $\longleftrightarrow$ `06:00 – 10:00 (Buổi sáng sớm)`
    * `der Vormittag` $\longleftrightarrow$ `10:00 – 12:00 (Buổi sáng trước trưa)`
    * `der Nachmittag` $\longleftrightarrow$ `14:00 – 18:00 (Buổi chiều)`
    * `die Nacht` $\longleftrightarrow$ `22:00 – 06:00 (Ban đêm)`
33. **Câu 33 (Bài nối ô 6)**: Nối câu hỏi lịch trình (`Tagesabläufe`) ở cột trái với câu trả lời tương ứng ở cột phải:
    * `Wann stehst du am Sonntag auf?` $\longleftrightarrow$ `Am Sonntag stehe ich um 8 Uhr auf.`
    * `Um wie viel Uhr frühstückst du?` $\longleftrightarrow$ `Um 9 Uhr frühstücke ich.`
    * `Von wann bis wann arbeitest du?` $\longleftrightarrow$ `Von 8 bis 12 Uhr arbeite ich.`
    * `Wann gehst du ins Bett?` $\longleftrightarrow$ `Um 22 Uhr gehe ich ins Bett.`

---

#### NHÓM 6: ĐIỀN VÀO CHỖ TRỐNG ĐỂ TẠO THÀNH CÂU (`dien_tao_cau` — 5 Câu)
34. **Câu 34**: Điền 2 từ còn thiếu vào khung câu để tạo thành câu hoàn chỉnh theo nghĩa: *„Vào Chủ nhật tôi thức dậy vào lúc 8 giờ.“*
    * Khung câu hiển thị: `Am Sonntag [1] ich um 8 Uhr [2].` (Gợi ý động từ: `aufstehen`)
    * Đáp án từng ô: Ô 1 = `["stehe"]`, Ô 2 = `["auf"]` (Hoặc gộp: `stehe / auf`).
    * Giải thích: Khi `Am Sonntag` đứng đầu câu, động từ gốc `stehe` đứng ở vị trí số 2 (trước chủ ngữ `ich`), còn tiền tố `auf` đứng ở cuối câu.
35. **Câu 35**: Điền 2 từ còn thiếu vào khung câu để tạo thành câu hoàn chỉnh theo nghĩa: *„Tôi mở cánh cửa ra.“*
    * Khung câu hiển thị: `Ich [1] die Tür [2].` (Gợi ý động từ: `aufmachen`)
    * Đáp án từng ô: Ô 1 = `["mache"]`, Ô 2 = `["auf"]`.
    * Giải thích: Động từ tách `aufmachen` chia cho ngôi `ich`: `mache` đứng vị trí số 2 và `auf` đứng cuối câu.
36. **Câu 36**: Điền 2 từ còn thiếu vào khung câu đối chiếu quá khứ – hiện tại: *„Hôm qua chúng tôi đã gặp một sự cố, nhưng hôm nay chúng tôi không gặp sự cố nào.“*
    * Khung câu hiển thị: `Gestern [1] wir eine Panne, aber heute [2] wir keine Panne.`
    * Đáp án từng ô: Ô 1 = `["hatten"]`, Ô 2 = `["haben"]`.
    * Giải thích: Với chủ ngữ `wir`, ở mệnh đề quá khứ (`Gestern`) ta dùng `hatten` (`Präteritum`), còn ở mệnh đề hiện tại (`heute`) ta dùng `haben` (`Präsens`).
37. **Câu 37**: Điền 2 từ còn thiếu vào khung câu lịch trình: *„Từ 8 giờ đến 12 giờ tôi làm việc.“*
    * Khung câu hiển thị: `Von 8 [1] 12 Uhr [2] ich.`
    * Đáp án từng ô: Ô 1 = `["bis"]`, Ô 2 = `["arbeite"]`.
    * Giải thích: Cấu trúc chỉ khoảng thời gian `Von 8 bis 12 Uhr` đứng ở vị trí số 1, động từ `arbeite` đứng ở vị trí số 2.
38. **Câu 38**: Điền 2 từ còn thiếu vào khung câu hỏi – đáp với động từ tách `ausgehen`: *„Bạn đi chơi vào thứ Sáu lúc nào? — Vào thứ Sáu lúc 20 giờ tôi đi chơi.“*
    * Khung câu hiển thị: `Wann gehst du am Freitag [1]? — Am Freitag um 20 Uhr [2] ich aus.`
    * Đáp án từng ô: Ô 1 = `["aus"]`, Ô 2 = `["gehe"]`.
    * Giải thích: Động từ tách `ausgehen` tách tiền tố `aus` xuống cuối câu hỏi, và ở câu trả lời động từ gốc `gehe` đứng ở vị trí số 2.

---

#### NHÓM 7: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 4 Câu)
39. **Câu 39**:
    * `audio_text`: *"Am Sonntag stehe ich um acht Uhr auf."*
    * `display_sentence`: *"Am Sonntag ___ ich um acht Uhr auf."*
    * `hint_vi`: *"Vào Chủ nhật tôi thức dậy vào lúc 8 giờ."*
    * `accepted_answers`: `["stehe"]`
    * Giải thích: Nghe và điền động từ gốc `stehe` ở vị trí thứ 2 trong câu.
40. **Câu 40**:
    * `audio_text`: *"Um neun Uhr frühstücke ich."*
    * `display_sentence`: *"Um neun Uhr ___ ich."*
    * `hint_vi`: *"Vào lúc 9 giờ tôi ăn sáng."*
    * `accepted_answers`: `["frühstücke", "fruehstuecke"]`
    * Giải thích: Động từ không tách `frühstücken` chia ở ngôi `ich` là `frühstücke`.
41. **Câu 41**:
    * `audio_text`: *"Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine Panne."*
    * `display_sentence`: *"Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine ___."*
    * `hint_vi`: *"Xin lỗi, tối qua chúng mình không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe."*
    * `accepted_answers`: `["Panne"]`
    * Giải thích: Danh từ `die Panne` có nghĩa là sự cố hỏng xe dọc đường.
42. **Câu 42**:
    * `audio_text`: *"Gestern hatte er kein Geld, aber heute hat er viel Geld."*
    * `display_sentence`: *"Gestern ___ er kein Geld, aber heute hat er viel Geld."*
    * `hint_vi`: *"Hôm qua anh ấy đã không có tiền, nhưng hôm nay anh ấy có nhiều tiền."*
    * `accepted_answers`: `["hatte"]`
    * Giải thích: Quá khứ đơn (`Präteritum`) của động từ `haben` với ngôi `er` là `hatte`.

---

#### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT $\rightarrow$ ĐỨC (`dich_cau_vd` — 4 Câu, chấm đa đáp án linh hoạt)
43. **Câu 43**: Dịch câu sau sang tiếng Đức: ***"Vào Chủ nhật tôi thức dậy lúc 8 giờ."***
    * `accepted_answers`:
      * `"Am Sonntag stehe ich um 8 Uhr auf."`
      * `"Am Sonntag stehe ich um acht Uhr auf."`
      * `"Ich stehe am Sonntag um 8 Uhr auf."`
      * `"Ich stehe am Sonntag um acht Uhr auf."`
      * `"Um 8 Uhr stehe ich am Sonntag auf."`
    * Giải thích: Chấp nhận cả cách đưa trạng ngữ `Am Sonntag` lên đầu câu (đảo ngữ `stehe ich`) hoặc để chủ ngữ `Ich stehe` ở đầu câu, miễn động từ `stehe` ở vị trí số 2 và tiền tố `auf` ở cuối câu.
44. **Câu 44**: Dịch câu sau sang tiếng Đức: ***"Từ 8 giờ đến 12 giờ tôi làm việc."***
    * `accepted_answers`:
      * `"Von 8 bis 12 Uhr arbeite ich."`
      * `"Von acht bis zwölf Uhr arbeite ich."`
      * `"Ich arbeite von 8 bis 12 Uhr."`
      * `"Ich arbeite von acht bis zwölf Uhr."`
      * `"Von 8 Uhr bis 12 Uhr arbeite ich."`
    * Giải thích: Cấu trúc `von ... bis ...` kết hợp với động từ `arbeiten` chia cho ngôi `ich` là `arbeite`.
45. **Câu 45**: Dịch câu sau sang tiếng Đức: ***"Hôm qua tôi không có thời gian, nhưng hôm nay tôi có nhiều thời gian."***
    * `accepted_answers`:
      * `"Gestern hatte ich keine Zeit, aber heute habe ich viel Zeit."`
      * `"Ich hatte gestern keine Zeit, aber heute habe ich viel Zeit."`
      * `"Gestern hatte ich keine Zeit, aber ich habe heute viel Zeit."`
      * `"Ich hatte gestern keine Zeit, aber ich habe heute viel Zeit."`
    * Giải thích: Mệnh đề quá khứ với `gestern` dùng `hatte ich keine Zeit`, mệnh đề hiện tại với `heute` dùng `habe ich viel Zeit`.
46. **Câu 46**: Dịch câu sau sang tiếng Đức: ***"Vào thứ Sáu lúc 20 giờ tôi đi chơi."***
    * `accepted_answers`:
      * `"Am Freitag um 20 Uhr gehe ich aus."`
      * `"Am Freitag um zwanzig Uhr gehe ich aus."`
      * `"Ich gehe am Freitag um 20 Uhr aus."`
      * `"Ich gehe am Freitag um zwanzig Uhr aus."`
      * `"Am Freitag gehe ich um 20 Uhr aus."`
    * Giải thích: Động từ tách `ausgehen` chia cho ngôi `ich`: `gehe` đứng ở vị trí số 2, tiền tố `aus` tách ra đứng ở cuối câu.

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC $\rightarrow$ VIỆT (`dich_cau_dv` — 4 Câu, chấm đa đáp án linh hoạt)
47. **Câu 47**: Dịch câu sau sang tiếng Việt: ***„Ich mache die Tür auf.“***
    * `accepted_answers`:
      * `"Tôi mở cửa"`
      * `"Tôi mở cánh cửa"`
      * `"Tôi mở cửa ra"`
      * `"Tôi mở cánh cửa ra"`
      * `"Mình mở cửa ra"`
    * Giải thích: `aufmachen` = mở ra; `die Tür` = cánh cửa.
48. **Câu 48**: Dịch câu sau sang tiếng Việt: ***„Um 12 Uhr mache ich Mittagspause.“***
    * `accepted_answers`:
      * `"Vào lúc 12 giờ tôi nghỉ trưa"`
      * `"Lúc 12 giờ tôi nghỉ trưa"`
      * `"12 giờ tôi nghỉ trưa"`
      * `"Tôi nghỉ trưa vào lúc 12 giờ"`
      * `"Tôi nghỉ trưa lúc 12 giờ"`
    * Giải thích: `Um 12 Uhr` = vào lúc 12 giờ; `Mittagspause machen` = nghỉ trưa.
49. **Câu 49**: Dịch câu sau sang tiếng Việt: ***„Gestern hatten wir eine Panne, aber heute haben wir keine Panne.“***
    * `accepted_answers`:
      * `"Hôm qua chúng tôi đã gặp một sự cố, nhưng hôm nay chúng tôi không gặp sự cố nào"`
      * `"Hôm qua chúng tôi có một sự cố hỏng xe, nhưng hôm nay chúng tôi không có sự cố nào"`
      * `"Hôm qua chúng tôi bị hỏng xe, nhưng hôm nay chúng tôi không bị hỏng xe"`
      * `"Hôm qua chúng mình gặp sự cố, nhưng hôm nay chúng mình không gặp sự cố"`
    * Giải thích: `eine Panne haben` = gặp sự cố (hỏng xe); `hatten` là quá khứ đơn của `haben` ở ngôi `wir`.
50. **Câu 50**: Dịch câu sau sang tiếng Việt: ***„Um 22 Uhr gehe ich ins Bett.“***
    * `accepted_answers`:
      * `"Vào lúc 22 giờ tôi đi ngủ"`
      * `"Lúc 22 giờ tôi đi ngủ"`
      * `"22 giờ tôi đi ngủ"`
      * `"Tôi đi ngủ vào lúc 22 giờ"`
      * `"Tôi đi ngủ lúc 22 giờ"`
      * `"Vào lúc 10 giờ tối tôi đi ngủ"`
      * `"Lúc 22 giờ tôi lên giường đi ngủ"`
    * Giải thích: `Um 22 Uhr` = vào lúc 22 giờ; `ins Bett gehen` = lên giường / đi ngủ.

---

## PHẦN 4: HỆ THỐNG SINH ĐỀ NGẪU NHIÊN (`DYNAMIC RANDOMIZER`) CHO BÀI 5

Để mỗi lần người học bấm nút **`🔄 Đổi đề khác`** hoặc thoát ra vào lại Bài 5 đều có trải nghiệm bài tập mới mẻ nhưng **tuyệt đối không bao giờ lệch câu hỏi – đáp án – giải thích**, hàm random của Bài 5 phải sinh các câu hỏi theo **khối nguyên tử (`Atomic Question Object`)** từ 4 ngân hàng dữ liệu chuẩn sau:

1. **Randomizer 1 — Chuyển đổi Giờ Chính thống $\leftrightarrow$ Đời thường (16 mốc giờ chuẩn)**:
   * Tự động chọn ngẫu nhiên từ 16 mốc giờ (`8h15 -> Viertel nach acht`, `9h10 -> zehn nach neun`, `2h30 -> halb drei`, `5h50 -> zehn vor sechs`, `6h05 -> fünf nach sechs`, `8h30 -> halb neun`, `3h15 -> Viertel nach drei`, `5h45 -> Viertel vor sechs`, `7h50 -> zehn vor acht`, `20h10 -> zehn nach acht`, `10h30 -> halb elf`, `11h15 -> Viertel nach elf`, `4h45 -> Viertel vor fünf`, `1h30 -> halb zwei`) và tạo đồng bộ cả câu hỏi, 4 phương án lựa chọn, bản dịch tiếng Việt lẫn lời giải thích công thức.
2. **Randomizer 2 — Ma trận Giới từ Thời gian `um / am / im / in der / von...bis` (30 cụm thời gian)**:
   * Chọn ngẫu nhiên các danh từ chỉ giờ (`um 7 Uhr, um 8 Uhr, um 12 Uhr, um 20 Uhr`), thứ (`am Montag ... am Sonntag, am Wochenende`), buổi (`am Morgen, am Vormittag, am Mittag, am Nachmittag, am Abend` vs. ngoại lệ `in der Nacht`), tháng (`im Januar ... im Dezember`) và tạo câu hỏi + lời giải thích tương ứng chính xác với danh từ vừa chọn.
3. **Randomizer 3 — Chia Động Từ Tách Trong Khung Câu (10 động từ tách $\times$ 6 ngôi)**:
   * Tự động kết hợp các động từ tách (`aufstehen, ausgehen, aufmachen, zumachen, anmachen, ausmachen, einkaufen, anrufen, fernsehen, mitkommen`) với các chủ ngữ (`ich, du, er, sie, wir, ihr, Sie`) để tạo câu trắc nghiệm, điền khuyết và điền tạo câu hoàn chỉnh, kèm bản dịch tiếng Việt chính xác của đúng chủ ngữ và động từ đó.
4. **Randomizer 4 — Đối chiếu `sein` (`war/warst/waren/wart`) & `haben` (`hatte/hattest/hatten/hattet`) ở `Präteritum`**:
   * Tự động biến thiên chủ ngữ (`ich, du, er, sie, wir, ihr, Joan und ich, Maria`) với các cụm danh từ (`keine Zeit, eine Panne, kein Glück, kein Geld, kein Handy, eine tolle Party`) để luyện tập phản xạ chia động từ quá khứ đơn chuẩn xác.

---

## PHẦN 5: DANH SÁCH KIỂM THỬ BẮT BUỘC SAU KHI CODE (`POST-CODING QA CHECKLIST`)

Sau khi viết xong code cho Bài 5, Antigravity IDE **BẮT BUỘC** phải chạy kịch bản kiểm thử tự động (Python test script + kiểm tra DOM/JS) qua 6 bước sau trước khi báo cáo hoàn thành:

1. **Kiểm tra Bảo toàn Dữ liệu Cũ (`Regression Check`)**:
   * Truy vấn SQLite `deutsch_meister.db`: Xác nhận **Bài 1 (P1), Bài 1 (P2), Bài 2, Bài 3, Bài 4** vẫn còn nguyên vẹn 100% lý thuyết, từ vựng và đúng 50 câu hỏi mỗi bài, không bị mất hay biến dạng bất kỳ trường nào.
2. **Kiểm tra Bài 5 (`Lesson 5 Completeness Check`)**:
   * Xác nhận **Bài 5: "Thời gian - Động từ tách - Haben in Präteritum"** đã xuất hiện trong danh sách bài học cấp độ A1 với đầy đủ 6 học phần lý thuyết, bảng đơn vị thời gian, bảng 7 thứ, 6 buổi, 12 tháng, bảng giờ giấc, bảng giới từ `um/am/im`, bảng động từ tách, 7 câu `Tagesabläufe`, bảng `sein & haben im Präteritum` và bức thư của Maria gửi Thomas.
3. **Kiểm tra 100% Từ vựng – Câu ví dụ – Dịch nghĩa (`Zero-Mismatch Check`)**:
   * Quét toàn bộ danh sách từ vựng của Bài 5 (và trong `lexikon_db.js`): Đảm bảo **không có bất kỳ từ vựng nào thiếu nghĩa tiếng Việt**, và **100% câu ví dụ tiếng Đức (`example_de`) đều chứa đúng từ vựng của thẻ đó** kèm bản dịch tiếng Việt (`example_vi`) khớp nghĩa tuyệt đối.
4. **Kiểm tra 50 Câu hỏi & 9 Dạng bài tập của Bài 5 (`Question Integrity Check`)**:
   * Viết một đoạn script Python chạy kiểm tra toàn bộ 50 câu hỏi của Bài 5 (kể cả sau khi chạy hàm Random đổi đề 10 lần liên tiếp):
     * Đảm bảo đủ **9 dạng bài** (`trac_nghiem`: 8, `dien_khuyet`: 7, `dich_nghia_vd`: 6, `dich_nghia_dv`: 6, `noi_o`: 6, `dien_tao_cau`: 5, `nghe_dien`: 4, `dich_cau_vd`: 4, `dich_cau_dv`: 4).
     * Đảm bảo ở mọi câu hỏi: `correct_answer` nằm trong `options` (đối với trắc nghiệm), `explanation` giải thích đúng chính xác đáp án của câu hỏi đó, và không có bất kỳ câu nào bị lệch đề bài với đáp án.
5. **Kiểm tra Voice TTS (`Audio Verification`)**:
   * Kiểm tra mọi nút `🔊` trong Bài 5, Tab Chia động từ, Tab Từ vựng & Giống và phần bài tập `nghe_dien`: đảm bảo hàm `speakGerman()` chỉ nhận chuỗi tiếng Đức sạch, phát âm chuẩn giọng `de-DE`, không đọc ký tự rác hay tiếng Việt.
6. **Đẩy code lên GitHub (`Git Push`)**:
   * Sau khi toàn bộ bài kiểm thử đạt `100% PASS`, tiến hành commit và push lên kho lưu trữ `taolagautruc/deutsch-meister`:
     ```bash
     git add .
     git commit -m "Add Lesson 5 (Termine, Trennbare Verben, Haben im Praeteritum) with 9 exercise types and full QA verification"
     git push origin main
     ```