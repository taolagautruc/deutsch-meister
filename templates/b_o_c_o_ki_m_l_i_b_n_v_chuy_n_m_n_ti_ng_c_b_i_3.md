# 🛠 BÁO CÁO KIỂM LỖI CHUYÊN MÔN TIẾNG ĐỨC & BẢN VÁ NỘI DUNG (BÀI 3)

**Phạm vi kiểm duyệt:** Trình độ A1 — Bài 3: *"Städte – Länder – Sprachen: Địa Danh, Phương Hướng & Thì Quá Khứ Đơn (Präteritum)"*  
**Nguyên tắc cập nhật cho Antigravity IDE:** Chỉ chỉnh sửa các chuỗi văn bản (strings) và dữ liệu thuộc phạm vi **Bài 3**, tuyệt đối không tác động đến các bài học khác.

---

## 🚨 PHẦN 1: CÁC LỖI NGHIÊM TRỌNG VỀ NGỮ PHÁP, NGỮ NGHĨA & CHÍNH TẢ TIẾNG ĐỨC (CẦN SỬA NGAY)

### 1.1. Sai lầm nghiêm trọng khi đánh đồng `im Norden von [Quốc gia]` và `nördlich von [Quốc gia]`
* **Vị trí:**
  1. Mục `3. Định Hướng Bản Đồ & Hệ Thống 8 Phương Hướng` (Bảng 8 phương hướng + Khung `Cách 2: Dùng Tính Từ (-lich von)`).
  2. Khung `🎯 Tổng Kết Ngữ Pháp Cốt Lõi Bài 3 (A1 Checklist)` -> Mục `1. Địa danh & Phương hướng`.
  3. Các thẻ từ vựng `der Norden`, `der Süden`, `der Osten`, `der Westen`, `der Nordosten` ở cuối bài.
* **Nội dung hiện tại trên web:**
  * Trong bảng Mục 3:
    * `Hanoi liegt im Norden von Vietnam (nördlich von Vietnam).`
    * `Long An liegt im Süden von Vietnam (südlich von Vietnam).`
  * Trong khung `Cách 2: Dùng Tính Từ (-lich von)`:
    * `Công thức: [Thành phố] + liegt + [Tính từ -lich] + von + [Quốc gia].`
    * `"Hai Phong liegt nordöstlich von Vietnam." (Tuyệt đối KHÔNG có "im")`
    * `"München liegt südlich von Deutschland."`
  * Trong `Tổng Kết Ngữ Pháp Cốt Lõi Bài 3`:
    * `2 cách viết vị trí: liegt im Norden von... (danh từ) = liegt nördlich von... (tính từ).`
* **Phân tích lỗi chuyên môn (Cực kỳ nghiêm trọng):**
  * Trong tiếng Đức, hai cấu trúc này mang ý nghĩa địa lý **hoàn toàn khác nhau** và **KHÔNG THỂ** thay thế cho nhau trước tên một quốc gia chứa thành phố đó:
    1. **`im Norden / Süden von [Quốc gia]`** = nằm **BÊN TRONG** phần phía Bắc / phía Nam của quốc gia đó.  
       * Ví dụ đúng: *"Hanoi liegt im Norden von Vietnam."* (Hà Nội nằm ở miền Bắc Việt Nam) / *"München liegt im Süden von Deutschland."* (München nằm ở miền Nam nước Đức).
    2. **`nördlich / südlich von [Địa danh X]`** = nằm **BÊN NGOÀI** ranh giới của X và lệch về hướng Bắc / Nam so với X!  
       * Nếu nói **`"Hanoi liegt nördlich von Vietnam"`**, người Đức sẽ hiểu là: **"Hà Nội nằm ở phía Bắc của nước Việt Nam (tức nằm ngoài lãnh thổ Việt Nam, bên phía Trung Quốc)!"**  
       * Nếu nói **`"München liegt südlich von Deutschland"`**, câu này có nghĩa là: **"München nằm ở phía Nam của nước Đức (tức nằm ngoài nước Đức, bên phía Áo/Ý)!"**  
       * Cấu trúc `nördlich / südlich / östlich / westlich von...` chỉ đúng khi mốc so sánh phía sau `von` là **một thành phố khác** hoặc **một quốc gia khác nằm ngoài chủ ngữ** (Ví dụ: *"Hai Phong liegt östlich von Hanoi."* = Hải Phòng nằm ở phía Đông của Hà Nội; *"Österreich liegt südlich von Deutschland."* = Nước Áo nằm ở phía Nam của nước Đức).
* **Đề xuất sửa đổi cho IDE:**
  * **Tại bảng Mục 3 (Dòng `Bắc` và `Nam`):** Đổi phần trong ngoặc để so sánh với một thành phố khác thay vì tên quốc gia:
    ```text
    Hanoi liegt im Norden von Vietnam (nördlich von Hue).
    ```
    ```text
    Long An liegt im Süden von Vietnam (südwestlich von Ho-Chi-Minh-Stadt).
    ```
  * **Tại khung `Cách 2: Dùng Tính Từ (-lich von)` (Mục 3):** Sửa lại công thức và ví dụ cho chuẩn xác:
    ```text
    Cách 2: Dùng Tính Từ (-lich von) — So sánh vị trí giữa 2 địa điểm tách biệt
    Công thức: [Địa điểm A] + liegt + [Tính từ -lich] + von + [Địa điểm B].
    👉 "Hai Phong liegt östlich von Hanoi." (Hải Phòng nằm ở phía Đông của Hà Nội — Tuyệt đối KHÔNG có "im")
    👉 "Österreich liegt südlich von Deutschland." (Nước Áo nằm ở phía Nam của nước Đức.)
    ```
  * **Tại khung `Tổng Kết Ngữ Pháp Cốt Lõi Bài 3 (A1 Checklist)`:**
    ```text
    • 2 cách diễn đạt vị trí: liegt im Norden von [Quốc gia] (nằm ở miền Bắc của nước...) vs. liegt nördlich von [Thành phố/Quốc gia khác] (nằm về phía Bắc so với...).
    ```

---

### 1.2. Lỗi ghép từ sai ngữ pháp & chính tả tiếng Đức: `"am Do Son Meer"`, `"im BigC Supermarkt"`, `"auf dem Cat Bi Markt"`
* **Vị trí:**
  1. Mục `6. Phân Tích Hội Thoại Carlos & Bưu Thiếp Du Lịch Hải Phòng` -> Khung `✉️ Bưu Thiếp Du Lịch Hải Phòng Gửi Anna` & mục `🔍 Phân tích Ngữ pháp Đắt giá`.
  2. Các thẻ từ vựng `der Supermarkt`, `der Markt`, `das Meer` ở cuối bài.
* **Nội dung hiện tại trên web:**
  * `"Ich war im BigC Supermarkt und Paula [war] im Theater. Wart ihr schon auf dem Cat Bi Markt? Der Cat Bi Markt war sehr interessant. ... Heute sind wir am Do Son Meer."`
  * Ô công thức: `am Do Son Meer (an dem)`
* **Phân tích lỗi chuyên môn:**
  1. **Lỗi `"am Do Son Meer"` (Sai cả từ vựng lẫn ngữ pháp tiếng Đức):**
     * Trong tiếng Đức, `das Meer` là đại dương / vùng biển lớn (như *das Ostmeer / die Ostsee*). Người Đức **tuyệt đối không** ghép tên một quận/thị xã/bãi biển trước chữ `Meer` kiểu dịch từng chữ từ tiếng Việt (*"biển Đồ Sơn"* $\rightarrow$ `*Do Son Meer`).
     * Hơn nữa, Đồ Sơn là tên địa danh (bán đảo / bãi biển). Để nói *"Hôm nay chúng tôi đang ở biển tại Đồ Sơn"* hoặc *"ở bãi biển Đồ Sơn"*, tiếng Đức chuẩn phải viết là: **`Heute sind wir in Do Son am Meer.`** (hoặc **`am Strand in Do Son`**).
  2. **Lỗi chính tả khoảng trắng trong danh từ ghép (*Deppenleerzeichen*) ở `"BigC Supermarkt"` và `"Cat Bi Markt"`:**
     * Theo quy tắc chính tả tiếng Đức chuẩn (Duden Rechtschreibung), khi ghép tên riêng (đặc biệt là tên riêng nước ngoài có nhiều âm tiết như *Cat Bi*, *Big C*) với một danh từ chung (*Markt*, *Supermarkt*), bắt buộc phải nối bằng **dấu gạch nối (`Bindestrich`)**: **`im Big-C-Supermarkt`**, **`auf dem Cat-Bi-Markt`**, **`Der Cat-Bi-Markt`** (hoặc đặt tên riêng ra sau: *im Supermarkt Big C*, *auf dem Markt Cat Bi*). Viết rời có khoảng trắng `Cat Bi Markt` là lỗi chính tả trong các kỳ thi tiếng Đức.
  3. **Lỗi giải nghĩa thiếu nhất quán ở 4 ô Giới từ Cách 3 (Dativ):**
     * Ô 1: `im Supermarkt` $\rightarrow$ `(in dem)`
     * Ô 2: `im Theater` $\rightarrow$ `(in dem)`
     * Ô 3: `auf dem Markt` $\rightarrow$ **`(trên chợ)`** *(Sai! Trong tiếng Việt không ai dịch nghĩa chuẩn là "trên chợ", và 3 ô kia đều đang ghi công thức giới từ + mạo từ gốc `in dem`, `an dem`, tự nhiên ô này lại ghi nghĩa tiếng Việt thô là `trên chợ`)*.
     * Ô 4: `am Do Son Meer` $\rightarrow$ `(an dem)`
* **Đề xuất sửa đổi cho IDE:**
  * **Sửa đoạn văn trong Bưu thiếp (Mục 6) và bổ sung bản dịch tiếng Việt:**
    ```text
    Liebe Anna,
    gestern waren Paula und ich in Haiphong. Ich war im Big-C-Supermarkt und Paula [war] im Theater. Wart ihr schon auf dem Cat-Bi-Markt? Der Cat-Bi-Markt war sehr interessant. Hier sind ein paar Fotos. Es war super! Heute sind wir in Do Son am Meer.

    Viele Grüße
    Paula und Peter
    ```
  * **Sửa 4 ô Cụm Giới từ Chỉ Địa Điểm (Cách 3 - Dativ) ở Mục 6:**
    * Ô 1: `im Supermarkt` | `(in + dem: ở siêu thị)`
    * Ô 2: `im Theater` | `(in + dem: ở nhà hát)`
    * Ô 3: `auf dem Markt` | `(auf + dem: ở chợ)`
    * Ô 4: `am Meer` | `(an + dem: ở biển)`

---

### 1.3. Mâu thuẫn nghiêm trọng ở Thẻ Từ Vựng: Gắn mạo từ `das` cho 12 quốc gia "Không dùng mạo từ", nhưng lại bỏ mất `die` ở `USA` và `Niederlande`!
* **Vị trí:** Phần `Từ Vựng & Mẫu Câu Trọng Tâm (Có Phát Âm)` ở cuối bài (18 thẻ từ vựng chỉ quốc gia).
* **Nội dung hiện tại trên web:**
  * 12 thẻ quốc gia đầu tiên hiển thị nhãn xanh lá `das` và tiêu đề in đậm: **`das Deutschland`**, **`das Österreich`**, **`das Italien`**, **`das Spanien`**, **`das Griechenland`**, **`das Frankreich`**, **`das England`**, **`das Polen`**, **`das Tschechien`**, **`das Russland`**, **`das China`**, **`das Vietnam`**.
  * Trong khi đó, 2 thẻ quốc gia số nhiều bắt buộc có mạo từ lại chỉ ghi tiêu đề là: **`USA`** và **`Niederlande`** (thiếu hẳn chữ `die` ở tên từ vựng, dù `die Schweiz`, `die Türkei`, `die Slowakei`, `der Iran` đều có mạo từ đi kèm ở tiêu đề).
* **Phân tích lỗi chuyên môn:**
  * Dù về mặt ngữ pháp lịch đại, các tên quốc gia như *Deutschland, Vietnam* mang giống trung ẩn (chỉ xuất hiện khi có tính từ đứng trước ở trình độ B1/B2 như *das schöne Vietnam*), nhưng trong tiếng Đức tiêu chuẩn và đặc biệt ở trình độ A1, chúng được quy định là **Danh từ không dùng mạo từ (ohne Artikel)**.
  * Ngay ở Mục 1.1 của bài học, web đã dạy rất rõ: **"BẢNG 13 QUỐC GIA KHÔNG DÙNG MẠO TỪ"**. Việc hiển thị to rõ chữ **`das Deutschland`**, **`das Vietnam`**, **`das Frankreich`** ở thẻ học từ vựng sẽ khiến học viên A1 học vẹt mạo từ `das` và viết sai trong bài thi thành *"Das Deutschland ist schön"* hoặc *"Ich komme aus dem Vietnam"*.
  * Ngược lại, **`die USA`** và **`die Niederlande`** là 2 quốc gia **bắt buộc phải có mạo từ `die`** (như đã dạy ở Bảng 1.2), thì trên tiêu đề thẻ từ vựng lại bị mất chữ `die`!
* **Đề xuất sửa đổi cho IDE:**
  1. Với 12 thẻ quốc gia không dùng mạo từ (`Deutschland` $\rightarrow$ `Vietnam`):
     * Bỏ chữ `das` trước tên quốc gia ở dòng tiêu đề chính (chỉ viết **`Deutschland`**, **`Österreich`**, **`Italien`**, ..., **`Vietnam`**; hoặc viết **`(das) Deutschland`**).
     * Ở dòng nghĩa tiếng Việt bên dưới, ghi chú thêm: `nước Đức (không dùng mạo từ)` để đồng bộ tuyệt đối với lý thuyết Mục 1.1.
  2. Với 2 thẻ `USA` và `Niederlande`:
     * Thêm mạo từ **`die`** vào tiêu đề chính của thẻ: **`die USA`** và **`die Niederlande`** (đồng bộ với bảng 1.2 và các thẻ `die Schweiz`, `der Iran`).

---

### 1.4. Sai cách đặt câu hỏi nghề nghiệp trong tiếng Đức: `"Wer ist sie? – Sie ist Lehrerin."`
* **Vị trí:** Mục `4. Ba Cấu Trúc Câu Cốt Lõi & Bảng 9 Từ Để Hỏi (W-Fragen)` -> Bảng W-Fragen (dòng `Wer`) & Khung `4 Tình Huống Thực Hành Chuyển Đổi Trên Bảng Viết` (ô số 4).
* **Nội dung hiện tại trên web:**
  * Bảng W-Fragen (dòng `Wer`): `Hỏi người: Wer ist das? – Das ist Frau Schiller. / Wer ist sie? – Sie ist Lehrerin.`
  * Ô số 4:
    ```text
    4. "Sie ist Lehrerin." (Cô ấy là giáo viên)
    -> W-Frage: Wer ist sie? (hoặc Was ist sie von Beruf?)
    -> Ja/Nein: Ist sie Lehrerin?
    ```
* **Phân tích lỗi chuyên môn:**
  * Trong tiếng Đức, câu hỏi **`"Wer ist sie?"`** (*Cô ấy là ai?*) dùng để hỏi **danh tính / tên tuổi / mối quan hệ** (Câu trả lời phải là: *Das ist Anna / Sie ist meine Schwester / Das ist Frau Schiller*).
  * Khi câu trả lời là nghề nghiệp (**`"Sie ist Lehrerin."`**), người Đức **không** hỏi bằng `Wer`, mà hỏi bằng **`Was ist sie (von Beruf)?`** hoặc **`Was macht sie (beruflich)?`**.
* **Đề xuất sửa đổi cho IDE:**
  * **Tại bảng W-Fragen (dòng `Wer`):** Đổi câu ví dụ thứ hai thành câu chỉ danh tính/mối quan hệ:
    ```text
    Hỏi người: Wer ist das? – Das ist Frau Schiller. / Wer ist sie? – Sie ist meine Kollegin.
    ```
  * **Tại Ô số 4 (`4. "Sie ist Lehrerin."`):** Đưa `Was ist sie von Beruf?` lên làm câu hỏi chính:
    ```text
    4. "Sie ist Lehrerin." (Cô ấy là giáo viên)
    -> W-Frage: Was ist sie von Beruf? (hoặc Was macht sie beruflich?)
    -> Ja/Nein: Ist sie Lehrerin?
    ```

---

### 1.5. Sai bản chất ngữ pháp của từ `schon` trong mục "Dấu hiệu nhận biết thì Quá khứ (Präteritum)"
* **Vị trí:** Mục `5. Thì Quá Khứ Đơn (Präteritum) Của Động Từ "sein" & "haben"` -> Khung `⏰ Dấu hiệu nhận biết thì Quá khứ (Präteritum):`.
* **Nội dung hiện tại trên web:**
  * `• schon: đã từng (Warst du schon in Hanoi?)`
* **Phân tích lỗi chuyên môn:**
  * Bản thân trạng từ `schon` có nghĩa gốc là **"đã / rồi"** (tương đương *already* trong tiếng Anh) và xuất hiện rất nhiều ở **thì Hiện tại (Präsens)** (Ví dụ: *Ich bin schon in Berlin* = Tôi đã ở Berlin rồi). Tự thân chữ `schon` **không phải** là dấu hiệu nhận biết thì Quá khứ!
  * Nó chỉ mang nghĩa **"đã từng (ever)"** khi nằm trong câu hỏi/câu kể về trải nghiệm quá khứ (thường đi theo cụm **`schon einmal` / `schon mal`**, hoặc rút gọn thành `schon` trong câu *Warst du schon [mal] in...?*).
* **Đề xuất sửa đổi cho IDE:**
  * Sửa dòng cuối trong khung `⏰ Dấu hiệu nhận biết thì Quá khứ (Präteritum):` thành:
    ```text
    • schon (mal) (đi với war/wart): đã từng (hỏi trải nghiệm quá khứ: Warst du schon [mal] in Hanoi?)
    ```

---

## 🔍 PHẦN 2: LỖI LOGIC HỘI THOẠI, ĐỊA DANH & TÍNH NHẤT QUÁN NỘI BỘ BÀI 3

### 2.1. Mâu thuẫn nhân vật `Carlos` giữa Mục 1 và Mục 6 & Thiếu bản dịch tiếng Việt
* **Vị trí:** Mục `6. Phân Tích Hội Thoại Carlos & Bưu Thiếp Du Lịch Hải Phòng` -> Khung `💬 Đoạn Hội Thoại Carlos & Người Bạn (Athen / Wien):`.
* **Nội dung hiện tại trên web:**
  ```text
  A: Carlos, woher kommst du?
  Carlos: Ich komme aus Wien. Das ist in Österreich. Und du, woher kommst du?
  A: Ich komme aus Athen. Warst du schon in Athen?
  Carlos: Nein, wo ist denn das?
  A: Das ist in Griechenland.
  ```
* **Phân tích lỗi logic & sư phạm:**
  1. **Mâu thuẫn thông tin ngay trong cùng Bài 3:** Ở Mục 1.1 (`Bảng quốc gia`) và Thẻ từ vựng `Spanien`, bài học vừa lấy ví dụ: **`"Carlos kommt aus Spanien und spricht Spanisch."`** (Carlos đến từ Tây Ban Nha và nói tiếng Tây Ban Nha — hoặc đến từ Madrid, Tây Ban Nha). Thế nhưng xuống Mục 6, cũng nhân vật `Carlos` lại trả lời: **`"Ich komme aus Wien. Das ist in Österreich."`** (Tôi đến từ Viên, nước Áo)! (Trong sách gốc *Menschen A1*, Carlos đến từ Madrid/Tây Ban Nha, còn người bạn mới đến từ nơi khác, hoặc đổi tên nhân vật đến từ Wien thành `Lukas` / `Markus` nếu muốn giữ nguyên địa danh `Wien / Österreich`).
  2. **Thiếu toàn bộ bản dịch tiếng Việt:** Cả đoạn hội thoại 5 câu và bức bưu thiếp bên dưới đều không có dịch tiếng Việt để hỗ trợ người học A1.
* **Đề xuất sửa đổi cho IDE (Giữ nguyên tên Carlos ở tiêu đề nhưng sửa quê quán khớp với Tây Ban Nha hoặc bổ sung dịch tiếng Việt):**
  * **Phương án A (Giữ nguyên địa danh Wien/Athen trên tiêu đề, bổ sung bản dịch tiếng Việt đầy đủ cho cả Hội thoại và Bưu thiếp):**
    ```text
    A: Carlos, woher kommst du? (Carlos, bạn đến từ đâu?)
    Carlos: Ich komme aus Wien. Das ist in Österreich. Und du, woher kommst du? (Mình đến từ Viên. Nó nằm ở nước Áo. Còn bạn, bạn đến từ đâu?)
    A: Ich komme aus Athen. Warst du schon in Athen? (Mình đến từ Athen. Bạn đã từng đến Athen chưa?)
    Carlos: Nein, wo ist denn das? (Chưa, thế nó nằm ở đâu vậy?)
    A: Das ist in Griechenland. (Nó nằm ở Hy Lạp.)
    ```
  * **Bổ sung bản dịch tiếng Việt dưới Bưu thiếp Hải Phòng (Mục 6):**
    ```text
    (Dịch nghĩa: Anna thân mến, hôm qua Paula và mình đã ở Hải Phòng. Mình đã ở siêu thị Big C còn Paula [đã ở] trong nhà hát. Các bạn đã từng đến chợ Cát Bi chưa? Chợ Cát Bi rất thú vị. Đây là một vài bức ảnh. Tuyệt vời lắm! Hôm nay chúng mình đang ở biển tại Đồ Sơn. Nhiều lời chào thân ái, Paula và Peter.)
    ```

### 2.2. Lỗi phân vai `A - B - C` phi logic trong "Mẫu Hội Thoại Hỏi Trải Nghiệm Du Lịch" (Mục 5)
* **Vị trí:** Mục 5 -> Khung `✈️ Mẫu Hội Thoại Hỏi Trải Nghiệm Du Lịch:`.
* **Nội dung hiện tại trên web:**
  ```text
  A: "Warst du schon in Hanoi?" (Bạn đã từng ở Hà Nội chưa?)
  B: "Ja, ich war schon in Hanoi." (Rồi, mình đã từng ở Hà Nội.)
  C: "Nein, wo ist denn das?" (Chưa, thế nó ở đâu vậy?)
  A: "Hanoi liegt im Norden von Vietnam."
  ```
* **Phân tích lỗi logic:**
  1. Nhân vật `A` hỏi bằng đại từ số ít **`du`** (*"Warst du..."* — hỏi 1 người), nhưng lại có cả `B` trả lời *"Rồi"* lẫn `C` trả lời *"Chưa"* nối tiếp nhau như một cuộc hội thoại 3 người. Thực chất đây là **2 hướng trả lời (Có / Không)** cho câu hỏi của A.
  2. Câu cuối cùng của `A` (`"Hanoi liegt im Norden von Vietnam."`) bị thiếu bản dịch tiếng Việt trong ngoặc đơn.
* **Đề xuất sửa đổi cho IDE:**
  ```text
  A: "Warst du schon in Hanoi?" (Bạn đã từng đến Hà Nội chưa?)
  • Nếu ĐÃ đi (B): "Ja, ich war schon in Hanoi." (Rồi, mình đã từng ở Hà Nội.)
  • Nếu CHƯA đi (B): "Nein, wo ist denn das?" (Chưa, thế nó nằm ở đâu vậy?)
  A: "Hanoi liegt im Norden von Vietnam." (Hà Nội nằm ở miền Bắc Việt Nam.)
  ```

### 2.3. Lỗi đếm sai số lượng quốc gia ở tiêu đề Mục 1.1 & Gộp sai `Großbritannien / England`
* **Vị trí:** Mục `1.1. BẢNG 13 QUỐC GIA KHÔNG DÙNG MẠO TỪ & NGÔN NGỮ TƯƠNG ỨNG`.
* **Phân tích lỗi:**
  1. **Sai số lượng trên tiêu đề:** Tiêu đề ghi **`BẢNG 13 QUỐC GIA...`**, nhưng thực tế bảng bên dưới chỉ có **12 hàng** (tương ứng với 12 thẻ từ vựng quốc gia ở cuối bài).
  2. **Gộp địa danh chưa chính xác:** Ở hàng thứ 7, cột Quốc gia ghi `Großbritannien / England`, cột Nghĩa tiếng Việt chỉ ghi `Nước Anh`. Thực tế, *Großbritannien* là **Vương quốc Anh (Đảo Anh)** còn *England* là **Nước Anh**.
  3. **Thiếu đồng bộ mạo từ trước `Big Ben`:** Trong bảng 1.1 và thẻ `England`, câu ví dụ viết `"Big Ben ist in England."` (không có `der`), nhưng ở Mục 2 và thẻ `der Big Ben` lại dạy `"Wo ist der Big Ben?"` (có `der`).
* **Đề xuất sửa đổi cho IDE:**
  * Sửa tiêu đề `1.1` thành: `1.1. BẢNG 12 QUỐC GIA KHÔNG DÙNG MẠO TỪ & NGÔN NGỮ TƯƠNG ỨNG` (hoặc tách `Großbritannien` và `England` thành 2 dòng riêng nếu muốn đủ 13 quốc gia).
  * Sửa nghĩa tiếng Việt của dòng `Großbritannien / England` thành: `Vương quốc Anh / Nước Anh`.
  * Đồng bộ câu ví dụ thành: `"Der Big Ben ist in England. Sprichst du Englisch?"`.

### 2.4. Tên gọi đầy đủ của Tháp nghiêng Pisa trong tiếng Đức (`der Schiefe Turm von Pisa`)
* **Vị trí:** Mục `2. Danh Lam Thắng Cảnh Châu Âu`, Khung `Tổng Kết Ngữ Pháp Cốt Lõi Bài 3`, và Thẻ từ vựng `der Schiefe Turm`.
* **Phân tích lỗi chuyên môn:**
  * Trong tiếng Đức, tên riêng đầy đủ của danh thắng này luôn là **`der Schiefe Turm von Pisa`** (bởi ở Đức cũng có *der Schiefe Turm von Suurhusen* rất nổi tiếng). Nếu đứng độc lập trong danh sách danh thắng hoặc trong câu hỏi mở đầu mà chỉ nói *"Wo ist der Schiefe Turm?"* thì câu văn bị cụt nghĩa.
* **Đề xuất sửa đổi cho IDE:**
  * Tại tiêu đề thẻ ở Mục 2 và Thẻ từ vựng cuối bài: Đổi `der Schiefe Turm` $\rightarrow$ **`der Schiefe Turm (von Pisa)`**.

### 2.5. Lỗi dùng mạo từ xác định trong câu `"Er macht die Hausaufgaben."` & Nghĩa của từ để hỏi `Wie`
* **Vị trí:**
  1. Mục 4 -> Bảng W-Fragen (dòng `Was` và dòng `Wie`), Ô thực hành số 3.
  2. Thẻ từ vựng `die Hausaufgabe` ở cuối bài.
* **Phân tích lỗi chuyên môn:**
  1. **`"Er macht die Hausaufgaben."`:** Trong tiếng Đức tự nhiên, cụm cố định *"làm bài tập về nhà"* được nói là **`Hausaufgaben machen`** (không có mạo từ: *Er macht Hausaufgaben*) hoặc đi với tính từ sở hữu (*Er macht seine Hausaufgaben*). Dùng mạo từ xác định `die Hausaufgaben` khi không có mệnh đề phụ bổ nghĩa nghe rất gượng gạo.
  2. **Dòng từ để hỏi `Wie` trong bảng W-Fragen:** Cột nghĩa tiếng Việt ghi `Như thế nào? / Bao nhiêu?`, nhưng 3 câu ví dụ bên phải (`Wie heißen Sie? / Wie geht es dir? / Wie bitte?`) hoàn toàn không có câu nào mang nghĩa *"Bao nhiêu?"* (ở trình độ A1, `Wie` dịch là *"Bao nhiêu"* khi hỏi số điện thoại `Wie ist Ihre Telefonnummer?` hoặc kết hợp trong `Wie viel` / `Wie alt`).
* **Đề xuất sửa đổi cho IDE:**
  * Đổi câu `"Er macht die Hausaufgaben."` (ở bảng W-Fragen, Ô số 3 và thẻ từ vựng `die Hausaufgabe`) thành: **`"Er macht Hausaufgaben."`** (hoặc giữ song song: `Er macht Hausaufgaben`).
  * Ở dòng `Wie` trong bảng W-Fragen, bổ sung thêm ví dụ hỏi số điện thoại vào cột phải: `Wie heißen Sie? / Wie geht es dir? / Wie ist Ihre Telefonnummer? / Wie bitte?`.

---

## 📋 PHẦN 3: BẢNG ĐỐI CHIẾU & CHUẨN HÓA CÁC THẺ TỪ VỰNG CUỐI BÀI 3 (DÀNH CHO IDE)

> **Lưu ý kỹ thuật cho IDE:** Trên thanh lọc (Filter Tabs) của mục `Từ Vựng & Mẫu Câu Trọng Tâm` hiện có tab **`Verb (Động từ)`**, nhưng trong danh sách thẻ từ vựng của Bài 3 hiện chỉ toàn Danh từ (Quốc gia, Danh thắng, Phương hướng, Địa điểm), **chưa có thẻ Động từ nào** (`sprechen`, `liegen`, `sein – war`, `haben – hatte`). Hãy bổ sung 4 thẻ động từ này hoặc ẩn tab `Verb (Động từ)` ở Bài 3 để tránh lỗi tab rỗng khi người dùng bấm vào!

Dưới đây là bảng chuẩn hóa các thẻ từ vựng hiện có ở cuối Bài 3:

| Thẻ từ hiện tại | Nội dung hiện tại có lỗi | Nguyên nhân chuyên môn | Bản chuẩn hóa cho IDE (Search & Replace) |
| :--- | :--- | :--- | :--- |
| **`das Deutschland` ... `das Vietnam`** *(12 thẻ)* | Tiêu đề gắn cứng `das ...` trước tên 12 quốc gia | Mâu thuẫn trực tiếp với quy tắc "Quốc gia KHÔNG dùng mạo từ" ở Mục 1.1; dễ làm học viên A1 dùng sai `das` trong câu. | **Tiêu đề thẻ:** Bỏ `das` (chỉ để `Deutschland`, `Österreich`, ..., `Vietnam` hoặc ghi `(das) Deutschland`).<br>**Dòng nghĩa:** Thêm chú thích `(không dùng mạo từ)`. |
| **`USA`** | Tiêu đề thiếu mạo từ `die` | Quốc gia số nhiều bắt buộc phải đi kèm mạo từ `die` (như đã dạy ở Bảng 1.2). | **Tiêu đề thẻ:** `die USA`<br>**Dòng nghĩa:** `Hợp chúng quốc Hoa Kỳ - Mỹ (aus den / in den USA)` |
| **`Niederlande`** | Tiêu đề thiếu mạo từ `die` | Quốc gia số nhiều bắt buộc phải đi kèm mạo từ `die`. | **Tiêu đề thẻ:** `die Niederlande`<br>**Dòng nghĩa:** `Hà Lan (aus den / in den Niederlanden)` |
| **`der Eiffelturm`** | Dịch: *"Tháp Eiffel đứng sừng sững ở Paris."* | Động từ `stehen` dùng cho công trình cao tầng chỉ đơn thuần nghĩa là *"nằm ở / tọa lạc ở"*, dịch *"đứng sừng sững"* dễ làm học viên hiểu sai nghĩa gốc của `stehen`. | **Câu ví dụ:** `"Der Eiffelturm steht in Paris. Paris liegt in Frankreich. (Tháp Eiffel tọa lạc ở Paris. Paris nằm ở nước Pháp.)"` |
| **`der Norden`, `der Süden`, `der Osten`, `der Westen`, `der Nordosten`** | Dòng nghĩa xanh dương ghi gộp: `(im Norden von / nördlich von)` | Gây nhầm lẫn rằng hai cụm này dùng giống hệt nhau trước tên quốc gia. | **Dòng nghĩa:** `phía Bắc, miền Bắc (im Norden von + Quốc gia / nördlich von + Địa điểm khác)` *(Tương tự cho Süden, Osten, Westen, Nordosten)*. |
| **`der Supermarkt`** | Dòng nghĩa: `siêu thị (im BigC Supermarkt)`<br>Ví dụ: `"...im BigC Supermarkt."` | Lỗi thiếu gạch nối trong danh từ ghép tiếng Đức (*Deppenleerzeichen*). | **Dòng nghĩa:** `siêu thị (im Supermarkt)`<br>**Câu ví dụ:** `"Ich war gestern im Big-C-Supermarkt. (Hôm qua tôi đã ở siêu thị Big C.)"` |
| **`der Markt`** | Dòng nghĩa: `chợ (auf dem Cat Bi Markt)`<br>Ví dụ: `"...auf dem Cat Bi Markt?"` | Lỗi thiếu gạch nối trong danh từ ghép tiếng Đức (*Deppenleerzeichen*). | **Dòng nghĩa:** `chợ (auf dem Markt)`<br>**Câu ví dụ:** `"Wart ihr schon auf dem Cat-Bi-Markt? (Các bạn đã từng đi chợ Cát Bi chưa?)"` |
| **`das Meer`** | Dòng nghĩa: `biển (am Do Son Meer)`<br>Ví dụ: `"Heute sind wir am Do Son Meer."` | Sai cấu trúc ghép địa danh tiếng Đức (không ghép `Do Son Meer`). | **Dòng nghĩa:** `biển (am Meer)`<br>**Câu ví dụ:** `"Heute sind wir in Do Son am Meer. (Hôm nay chúng tôi đang ở biển tại Đồ Sơn.)"` |
| **`die Hausaufgabe`** | Dòng nghĩa: `bài tập về nhà`<br>Ví dụ: `"Er macht die Hausaufgaben."` | Danh từ này hầu như luôn dùng ở số nhiều (`die Hausaufgaben`) và không dùng mạo từ `die` trong cụm `Hausaufgaben machen`. | **Tiêu đề thẻ:** `die Hausaufgabe (Pl. die Hausaufgaben)`<br>**Câu ví dụ:** `"Er macht Hausaufgaben. (Anh ấy đang làm bài tập về nhà.)"` |