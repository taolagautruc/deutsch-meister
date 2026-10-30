# 📋 BÁO CÁO KIỂM LỖI CHUYÊN MÔN TIẾNG ĐỨC - DEUTSCHMEISTER (BÀI 2 - A1)

Tài liệu này tổng hợp toàn bộ các lỗi sai và điểm cần chuẩn hóa về **ngữ pháp (Grammatik), hình thái học (Morphologie), từ vựng (Wortschatz), chính tả/dấu câu (Orthografie & Interpunktion) và tính logic ngữ dụng (Pragmatik)** trong phạm vi **Bài 2: "Sprache im Kurs - Động Từ và Giống (der, die, das & Mạo Từ)"**.

File được trình bày theo cấu trúc: **Vị trí -> Nội dung hiện tại -> Phân tích lỗi chuyên môn -> Nội dung chuẩn cần thay thế**, giúp Antigravity IDE dễ dàng tìm kiếm (search) và thay thế (replace) chính xác trong mã nguồn.

---

## 🚨 PHẦN 1: CÁC LỖI NGHIÊM TRỌNG VỀ NGỮ PHÁP, HẬU TỐ, TỪ VỰNG & DẤU CÂU (CẦN SỬA NGAY)

### 1. Lỗi xếp nhầm từ `das Präteritum` vào hậu tố `-tum` và thiếu ngoại lệ phổ biến (Mục 2 - Cột `das`)
* **Vị trí:** Mục `2. Bí quyết Nhận diện Giống của Danh từ (der / die / das) theo Hậu tố & Nhóm nghĩa` -> Cột `das (Neutrum)` -> Nhóm `🟢 Hậu tố luôn mang giống trung`.
* **Nội dung hiện tại:**
  ```text
  • -um: das Studium, das Museum, das Zentrum
  • -tum: das Präteritum, das Eigentum
  • -ma / -em: das Thema, das Klima, das System
  ```
* **Phân tích lỗi chuyên môn:**
  1. **Lỗi hình thái học (`das Präteritum`):** Từ `das Präteritum` là từ mượn gốc Latinh (*praeterit-um*), có hậu tố là **`-um`** (chữ `t` thuộc gốc từ *praeterit-*, hoàn toàn giống với *das Studium, das Zentrum, das Datum*), **KHÔNG PHẢI** hậu tố **`-tum`** của tiếng Đức (như *das Eigentum, das Wachstum, das Christentum, das Bürgertum*). Việc xếp `das Präteritum` vào mục `-tum` là sai về cấu tạo từ.
  2. **Thiếu cảnh báo ngoại lệ của `-tum` và `-ma`:**
     * Hậu tố `-tum` không phải 100% giống trung mà có **2 ngoại lệ giống đực (`der`) rất phổ biến** là **`der Reichtum`** (sự giàu có) và **`der Irrtum`** (sự nhầm lẫn).
     * Hậu tố `-ma` có ngoại lệ giống cái (`die`) cực kỳ cơ bản ở trình độ A1 là **`die Firma`** (công ty). (Trong khi ở mục `-ment` và `-nis` bài học đều có dòng `⚠️ Ngoại lệ` rất rõ ràng).
* **Đề xuất sửa thành:**
  ```text
  • -um: das Studium, das Museum, das Zentrum, das Präteritum
  • -tum: das Eigentum, das Wachstum (⚠️ Ngoại lệ: der Reichtum, der Irrtum)
  • -ma / -em: das Thema, das Klima, das System, das Problem (⚠️ Ngoại lệ: die Firma)
  ```

---

### 2. Lỗi khái quát hóa sai nhóm nghĩa "Thời tiết" luôn mang giống đực `der` (Mục 2 - Cột `der`)
* **Vị trí:** Mục `2. Bí quyết Nhận diện Giống của Danh từ` -> Cột `der (Maskulinum)` -> Nhóm `🔹 Nhóm ý nghĩa luôn mang giống đực`.
* **Nội dung hiện tại:**
  ```text
  • Thời tiết (der Wind, der Regen, der Schnee, der Nebel)
  ```
* **Phân tích lỗi chuyên môn:**
  * Khẳng định nhóm nghĩa **"Thời tiết"** luôn mang giống đực (`der`) là không chính xác. Bản thân danh từ "thời tiết" trong tiếng Đức là **`das Wetter`** (giống trung), "cơn dông/sấm sét" là **`das Gewitter`** (giống trung), "băng" là **`das Eis`** (giống trung), "mặt trời" là **`die Sonne`** (giống cái), "đám mây" là **`die Wolke`** (giống cái).
  * Trong ngữ pháp tiếng Đức chuẩn, quy tắc giống đực `der` chỉ áp dụng cụ thể cho **Các hiện tượng mưa, gió, bão, sương (Niederschläge & Winde)** như *der Regen, der Schnee, der Wind, der Sturm, der Nebel, der Frost, der Hagel*.
* **Đề xuất sửa thành:**
  ```text
  • Hiện tượng mưa, gió, sương, bão (der Wind, der Regen, der Schnee, der Nebel, der Sturm)
  ```

---

### 3. Lỗi cách dùng danh từ không đếm được `das Papier` / `ein Papier` (Mục 3, Mục 6.4 & Thẻ từ `das Papier`)
* **Vị trí:**
  1. Mục `3. 18 Từ vựng Đồ dùng Lớp học` -> Dòng `das Papier`: Nghĩa tiếng Việt ghi `tờ giấy`.
  2. Mục `6. Thực hành Hỏi - Đáp` -> Câu 4: `Đáp: Nein, das ist kein Becher. Das ist ein Papier. (Không, đó không phải là cái cốc. Đó là một tờ giấy.)`
  3. Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm` -> Thẻ `das Papier`: `"Ist das ein Becher? – Nein, das ist ein Papier. (Đây có phải cái cốc không? – Không, đó là một tờ giấy.)"`
* **Phân tích lỗi chuyên môn:**
  * Trong tiếng Đức chuẩn, **`das Papier`** khi mang nghĩa là **"giấy"** (vật liệu viết/in ấn) là **danh từ chỉ chất liệu không đếm được (Stoffnomen)**. Người Đức không nói *"Das ist ein Papier"* để chỉ "Đó là một tờ giấy".
  * Khi muốn đếm **"một tờ giấy"**, tiếng Đức dùng **`ein Blatt Papier`** (`das Blatt, die Blätter`) hoặc **`der Zettel`** (tờ giấy nhỏ / mảnh giấy ghi chú).
  * Nếu dùng `ein Papier` hoặc số nhiều `die Papiere` như danh từ đếm được, nghĩa của từ sẽ chuyển thành **"văn kiện / tài liệu / giấy tờ tùy thân (Ausweispapiere)"**.
  * Ngoài ra, về mặt logic tình huống: Nhìn vào một tờ giấy mà hỏi *"Đây có phải là cái cốc không?"* (`Ist das ein Becher?`) là hoàn toàn phi thực tế vì hai vật thể không có nét tương đồng nào.
* **Đề xuất sửa thành:**
  * **Tại Mục 3 (Bảng 18 từ vựng - Dòng `das Papier`):**
    * Nghĩa tiếng Việt: `giấy (chất liệu) / giấy tờ (số nhiều)`
  * **Tại Mục 6 (Câu 4 - Hỏi cái cốc):** Đổi sang cặp đồ vật dễ nhầm lẫn trong lớp học hoặc sửa câu đính chính sang danh từ đếm được chuẩn:
    ```text
    4. Hỏi cái cốc và cáibút lông / tờ giấy (der Becher & das Heft):
    Hỏi: Ist das ein Becher? (Đây có phải là cái cốc không?)
    Đáp: Nein, das ist kein Becher. Das ist ein Heft. (Không, đó không phải là cái cốc. Đó là một quyển vở.)
    ```
    *(Hoặc nếu giữ `das Papier` thì viết đúng ngữ pháp danh từ chất liệu: `Das ist ein Blatt Papier.` = Đó là một tờ giấy).*
  * **Tại Thẻ từ `das Papier`:**
    * Nghĩa tiếng Việt: `giấy / tờ giấy (ein Blatt Papier)`
    * Câu ví dụ:
      ```text
      "Brauchst du Papier? – Ja, ich brauche ein Blatt Papier. (Bạn có cần giấy không? – Vâng, tôi cần một tờ giấy.)"
      ```
      *(Hoặc ở mức A1 đơn giản: `"Ist das Papier? – Ja, das ist Papier für den Drucker. (Đây có phải là giấy không? – Vâng, đó là giấy cho máy in.)"`)*

---

### 4. Lỗi bất nhất giữa câu hỏi và câu trả lời đánh vần ở thẻ từ `das Heft`
* **Vị trí:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm` -> Thẻ `das Heft` (quyển vở).
* **Nội dung hiện tại:**
  ```text
  "Können Sie 'das Heft' bitte buchstabieren? – H - E - F - T. (Ngài có thể vui lòng đánh vần từ 'das Heft' được không? – H - E - F - T.)"
  ```
* **Phân tích lỗi chuyên môn:**
  * Trong câu hỏi, người nói đặt cả cụm **`'das Heft'`** trong dấu nháy đơn (tức yêu cầu đánh vần 7 chữ cái `D - A - S - H - E - F - T`), nhưng câu trả lời chỉ đánh vần **`H - E - F - T`**.
  * Trong giao tiếp thực tế tiếng Đức, khi nhờ đánh vần một từ, người ta chỉ trích dẫn bản thân từ đó (`'Heft'`) hoặc hỏi `"Können Sie das Wort 'Heft' bitte buchstabieren?"`.
* **Đề xuất sửa thành:**
  ```text
  "Können Sie 'Heft' bitte buchstabieren? – H - E - F - T. (Ngài có thể vui lòng đánh vần từ 'Heft' được không? – H - E - F - T.)"
  ```

---

### 5. Lỗi dấu phẩy cuối câu ở thẻ `die Landkarte` & Thiếu bản dịch tiếng Việt ở Mục 6.3
* **Vị trí 1:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm` -> Thẻ `die Landkarte` (bản đồ).
  * **Nội dung hiện tại:**
    ```text
    "Das ist keine Brille, das ist eine Landkarte, (Đó không phải là kính mắt, đó là một tấm bản đồ.)"
    ```
  * **Phân tích lỗi:** Cuối câu tiếng Đức sau từ `Landkarte` đang đặt **dấu phẩy (`,`)** thay vì **dấu chấm (`.`)**.
  * **Đề xuất sửa thành:**
    ```text
    "Das ist keine Brille, das ist eine Landkarte. (Đó không phải là kính mắt, đó là một tấm bản đồ.)"
    ```
* **Vị trí 2:** Mục `6. Thực hành Hỏi - Đáp Đồ vật & Sở hữu` -> Khung `3. Hỏi kính mắt và phủ định (die Brille)`.
  * **Nội dung hiện tại:**
    ```text
    Đáp phủ định + đính chính: Nein, das ist keine Brille. Das ist eine Landkarte.
    ```
  * **Phân tích lỗi:** Các khung 1, 2 và 4 đều có câu dịch tiếng Việt trong ngoặc đơn ở dòng `Đáp`, riêng khung 3 bị bỏ sót phần dịch tiếng Việt.
  * **Đề xuất sửa thành:**
    ```text
    Đáp phủ định + đính chính: Nein, das ist keine Brille. Das ist eine Landkarte. (Không, đó không phải là kính mắt. Đó là một tấm bản đồ.)
    ```

---

## ⚠️ PHẦN 2: CÁC LỖI NGỮ PHÁP & NGỮ DỤNG HỌC TRONG CÂU VÍ DỤ (CẦN CHUẨN HÓA)

### 6. Lỗi thừa mạo từ `ein` khi nói về nghề nghiệp/tư cách ở thẻ `der Praktikant` và `der Student`
* **Vị trí:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm` -> Thẻ `der Praktikant` và thẻ `der Student`.
* **Nội dung hiện tại:**
  * Thẻ `der Praktikant`: `"Er ist ein Praktikant bei der Post. (Anh ấy là một thực tập sinh ở bưu điện.)"`
  * Thẻ `der Student`: `"David ist ein Student aus den USA. (David là một nam sinh viên đến từ Mỹ.)"`
* **Phân tích lỗi chuyên môn:**
  * Theo quy tắc ngữ pháp tiếng Đức chuẩn (được dạy ngay ở trình độ A1), khi giới thiệu nghề nghiệp, tư cách học tập/làm việc hoặc quốc tịch sau động từ `sein` (mà không có tính từ đứng trước bổ nghĩa), **bắt buộc KHÔNG dùng mạo từ bất định `ein/eine`** (tương tự như tiếng Việt nói *"Anh ấy là thực tập sinh"*, *"David là sinh viên"*).
  * Chỉ dùng `ein` khi có tính từ đi kèm (ví dụ: *Er ist ein guter Praktikant*).
* **Đề xuất sửa thành:**
  * Thẻ `der Praktikant`:
    ```text
    "Er ist Praktikant bei der Post. (Anh ấy là thực tập sinh ở bưu điện.)"
    ```
  * Thẻ `der Student`:
    ```text
    "David ist Student und kommt aus den USA. (David là sinh viên và đến từ Mỹ.)"
    ```
    *(Hoặc giữ ngắn gọn: `"David ist Student aus den USA. (David là sinh viên đến từ Mỹ.)"`)*

---

### 7. Lỗi dùng mạo từ `eine` thay vì `die` trong thẻ `die Erlaubnis` (Mâu thuẫn với Quy tắc 3 Mục 5)
* **Vị trí:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm` -> Thẻ `die Erlaubnis` (Cuối trang).
* **Nội dung hiện tại:**
  ```text
  "Hast du eine Erlaubnis von der Lehrerin? (Bạn có sự cho phép của cô giáo chưa?)"
  ```
* **Phân tích lỗi chuyên môn:**
  * Khi danh từ `Erlaubnis` đã được xác định cụ thể bởi cụm giới từ chỉ nguồn gốc/sở hữu `von der Lehrerin` (sự cho phép *của cô giáo*), tiếng Đức chuẩn dùng **mạo từ xác định `die`**: **`die Erlaubnis von der Lehrerin`**.
  * Việc dùng `die` cũng giúp câu ví dụ này tuân thủ đúng **Mẹo số 3 ở Mục 5** của chính bài học (*"Khi có cụm sở hữu von + ..., đã được xác định cụ thể nên ta dùng lại mạo từ xác định der/die/das!"*).
* **Đề xuất sửa thành:**
  ```text
  "Hast du die Erlaubnis von der Lehrerin? (Bạn đã có sự cho phép của cô giáo chưa?)"
  ```

---

### 8. Chuẩn hóa giải thích về `Genitiv` và cấu trúc `von + Tên riêng` (Mục 1 - Tổng quan 4 Cách)
* **Vị trí:** Mục `1. Khái niệm Mạo từ...` -> Khung `🧭 Tổng quan 4 Cách (Kasus) trong tiếng Đức` -> Ô `2. Genitiv (Cách 2 - Sở hữu cách)`.
* **Nội dung hiện tại:**
  ```text
  2. Genitiv (Cách 2 - Sở hữu cách):
  Chỉ sự sở hữu (ở trình độ A1 thường dùng cấu trúc von + Tên riêng, ví dụ: der Kuli von Anna).
  ```
* **Phân tích lỗi chuyên môn:**
  * Về mặt ngữ pháp, giới từ **`von` luôn đi với Cách 3 (Dativ)** chứ không phải Cách 2 (Genitiv) — bằng chứng là ngay ở thẻ `das Dokument` cuối bài có câu `"das Dokument von Herrn Nguyen"` (danh từ yếu *Herr* nhận đuôi `-n` ở Dativ sau *von*).
  * Cấu trúc `von + Tên riêng (Cách 3)` là cấu trúc **dùng để thay thế** cho Genitiv (*Annas Kuli* / *der Kuli des Lehrers*) trong văn nói và ở trình độ A1. Nếu không ghi chữ **"thay thế bằng"**, học viên khi lên A2/B1 sẽ hiểu lầm rằng cụm `von Anna` được chia ở cách Genitiv.
* **Đề xuất sửa thành:**
  ```text
  2. Genitiv (Cách 2 - Sở hữu cách):
  Chỉ sự sở hữu (ví dụ: Annas Kuli; ở trình độ A1 thường thay thế bằng cấu trúc giới từ von + Tên riêng ở Cách 3, ví dụ: der Kuli von Anna).
  ```

---

### 9. Bổ sung phạm vi `(Cách 1 - Nominativ)` cho Bảng 3 Cột Mạo từ & Mẹo ghi nhớ (Mục 5)
* **Vị trí:** Mục `5. Bảng 3 Cột Mạo từ: Xác định, Bất định & Phủ định với "kein/keine"`.
* **Nội dung hiện tại:**
  * Tiêu đề Mục 5: `5. Bảng 3 Cột Mạo từ: Xác định, Bất định & Phủ định với "kein/keine"`
  * Mẹo 1: `1. Giống đực (der) và giống trung (das) dùng chung mạo từ bất định: ein, phủ định: kein.`
* **Phân tích lỗi chuyên môn:**
  * Quy tắc giống đực (`der`) và giống trung (`das`) dùng chung `ein / kein` **chỉ đúng ở Cách 1 (Nominativ)**.
  * Ngay trong bài học này (ở Mục 1.4, thẻ `der Bleistift` và thẻ `das Brötchen`), học viên đã gặp Cách 4 (Akkusativ) với các câu như: *"Ich habe **keinen** Kuli, aber ich habe **einen** Bleistift"*, *"trinke **einen** Kaffee"*. Nếu Mục 5 không ghi rõ bảng này đang xét ở **Cách 1 (Nominativ)**, người học sẽ thấy mâu thuẫn giữa bảng lý thuyết (`ein/kein Kuli`) và thẻ từ vựng bên dưới (`einen/keinen Kuli`).
* **Đề xuất sửa thành:**
  * Tiêu đề Mục 5: `5. Bảng 3 Cột Mạo từ ở Cách 1 (Nominativ): Xác định, Bất định & Phủ định với "kein/keine"`
  * Mẹo 1: `1. Ở Cách 1 (Nominativ), giống đực (der) và giống trung (das) dùng chung mạo từ bất định: ein, phủ định: kein.`

---

## 💡 PHẦN 3: LỖI LOGIC PHÂN LOẠI TỪ VỰNG, TÍNH TỰ NHIÊN & ĐỒNG BỘ GIAO DIỆN BÀI 2

### 10. Lỗi lệch chủ đề của từ `das Brötchen` trong bảng "18 Từ vựng Đồ dùng Lớp học" (Mục 3)
* **Vị trí:** Mục `3. 18 Từ vựng Đồ dùng Lớp học & Quy tắc Số nhiều (Plural)` (dòng thứ 18) và Thẻ từ `das Brötchen`.
* **Phân tích lỗi logic:**
  * Cả phần Mục tiêu bài học lẫn tiêu đề Mục 3 đều khẳng định đây là **`18 danh từ đồ dùng lớp học`**, nhưng từ thứ 18 lại là **`das Brötchen` (bánh mì nhỏ)** — thuộc chủ đề Đồ ăn/Thực phẩm, hoàn toàn không phải đồ dùng lớp học.
* **Đề xuất xử lý (Chọn 1 trong 2 cách):**
  * **Cách 1 (Khuyên dùng - Chuẩn chủ đề lớp học 100%):** Thay `das Brötchen` ở Mục 3 và Thẻ từ vựng bằng từ **`das Mäppchen`** (*hộp bút / túi đựng bút*). Từ `das Mäppchen` vừa là đồ dùng lớp học cốt lõi ở A1, vừa giữ nguyên hậu tố thu nhỏ **`-chen`** (Mục 2) và quy tắc số nhiều **`die Mäppchen` (Đuôi -chen giữ nguyên dạng)** giống hệt `das Brötchen`:
    * Bảng Mục 3: `das | das Mäppchen | die Mäppchen | hộp bút | Đuôi -chen giữ nguyên dạng`
    * Thẻ từ: `das Mäppchen` — `hộp bút / túi đựng bút` — `"Ist das dein Mäppchen? – Ja, im Mäppchen sind ein Kuli und ein Bleistift. (Đây là hộp bút của bạn à? – Vâng, trong hộp bút có một cây bút bi và một cây bút chì.)"`
    *(Lưu ý: Ở Mục 2 Cột `das`, dòng `-chen / -lein` vẫn giữ nguyên ví dụ `das Brötchen, das Mädchen` hoặc thêm `das Mäppchen`).*
  * **Cách 2 (Nếu muốn giữ `das Brötchen`):** Sửa tiêu đề Mục 3 thành `3. 18 Từ vựng Đồ dùng Lớp học & Danh từ Thông dụng (Plural)`.

---

### 11. Tinh chỉnh logic ngữ cảnh & câu dịch ở Mục 4 (`6 Mẫu câu giao tiếp`) và Thẻ động từ
* **Vị trí:** Mục `4. Động từ & 6 Mẫu câu Giao tiếp trong Lớp học (Sprache im Kurs)` và các thẻ động từ `buchstabieren`, `anschreiben`.
* **Phân tích chuyên môn:**
  1. **Câu dịch tiếng Việt ở câu 5 và câu 6 (Khung phải Mục 4):**
     * *Hiện tại:*
       * `5. Das verstehe ich nicht. Können Sie das bitte buchstabieren? -> Tôi không hiểu. Ngài đánh vần giúp tôi?`
       * `6. Das verstehe ich nicht. Können Sie das bitte anschreiben? -> Tôi không hiểu. Ngài viết lên bảng giúp tôi?`
     * *Vấn đề:* Câu hỏi tiếng Việt kết thúc bằng `"giúp tôi?"` (thiếu từ nghi vấn cuối câu như *"được không?"* hoặc *"nhé/ạ?"*) nghe bị cụt và kém lịch sự hơn hẳn so với sắc thái của `Können Sie ... bitte ...?` (và không đồng bộ với câu 4 ngay phía trên là *"Ngài lặp lại được không?"*).
  2. **Thiếu động từ `erklären` (giải thích):**
     * Trong thẻ từ vựng `verstehen` (bên dưới), câu ví dụ là `"Das verstehe ich nicht. Können Sie das bitte erklären?"`, nhưng động từ `erklären` lại chưa được liệt kê trong cột `Các Động từ lớp học cốt lõi` ở Mục 4.
* **Đề xuất sửa tại Mục 4 (Khung phải - Câu 5 & 6):**
  ```text
  5. Das verstehe ich nicht. Können Sie das bitte buchstabieren? -> Tôi không hiểu. Ngài đánh vần giúp tôi được không?
  6. Das verstehe ich nicht. Können Sie das bitte anschreiben? -> Tôi không hiểu. Ngài viết lên bảng giúp tôi được không?
  ```
  *(Và có thể bổ sung thêm `erklären (giải thích): Können Sie das bitte erklären?` vào khung trái Mục 4).*

---

### 12. Tinh chỉnh tính tự nhiên trong câu ví dụ của 3 thẻ từ (`die Tasche`, `die Freundschaft`, `der Polizist`)
* **Vị trí:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm`.
* **Chi tiết cần tinh chỉnh:**
  1. **Thẻ `die Tasche`:**
     * *Hiện tại:* `"Ja, das ist die Tasche von Anna. (Vâng, đó là chiếc túi xách của Anna.)"`
     * *Vấn đề:* Câu bắt đầu bằng `"Ja, ..."` (Vâng,...) nhưng lại bị thiếu vế câu hỏi phía trước (khác với tất cả các thẻ `der Tisch, der Füller, der Kuli, das Buch, das Handy` đều có dạng `"Ist das ...? – Ja, ..."`).
     * *Đề xuất sửa:* `"Ist das eine Tasche? – Ja, das ist die Tasche von Anna. (Đây có phải là chiếc túi xách không? – Vâng, đó là chiếc túi xách của Anna.)"`
  2. **Thẻ `die Freundschaft`:**
     * *Hiện tại:* `"Die Freundschaft von Anna und Sophie ist toll. (Tình bạn giữa Anna và Sophie thật tuyệt vời.)"`
     * *Vấn đề:* Để diễn đạt "tình bạn **giữa** A và B", tiếng Đức tự nhiên dùng giới từ **`zwischen`** (`Die Freundschaft zwischen Anna und Sophie`) thay vì `von`.
     * *Đề xuất sửa:* `"Die Freundschaft zwischen Anna und Sophie ist toll. (Tình bạn giữa Anna và Sophie thật tuyệt vời.)"`
  3. **Thẻ `der Polizist`:**
     * *Hiện tại:* `"Mein Freund arbeitet als Polizist in Berlin. (Bạn tôi làm việc với tư cách là cảnh sát ở Berlin.)"`
     * *Vấn đề:* Cụm `"làm việc với tư cách là cảnh sát"` là dịch word-by-word từ cấu trúc `arbeitet als`, nghe rất nặng nề trong tiếng Việt.
     * *Đề xuất sửa phần dịch tiếng Việt:* `"Mein Freund arbeitet als Polizist in Berlin. (Bạn tôi làm cảnh sát ở Berlin.)"`

---

### 13. Thiếu nút lọc (Filter Tab) cho nhóm thẻ `Động từ (Verb)` & Tràn chữ nhãn `Modalverb`
* **Vị trí:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm (Có Phát Âm)` của Bài 2.
* **Phân tích lỗi logic giao diện dữ liệu:**
  1. Tổng số 36 thẻ của Bài 2 bao gồm 30 thẻ danh từ (`der`, `die`, `das`) và **6 thẻ động từ** (`verstehen`, `wiederholen`, `buchstabieren`, `anschreiben`, `können`, `heißen` mang nhãn `Verb` / `Modalverb`), nhưng thanh bộ lọc phía trên chỉ có 3 tab: `der (Giống đực)`, `die (Giống cái)`, `das (Giống trung)`. Cần bổ sung thêm tab **`Verb (Động từ)`** (và tab **`Tất cả`**) để người học lọc được 6 thẻ động từ này.
  2. Ở thẻ **`können`**, nhãn cam đang ghi chữ `Modalverb` quá dài khiến nút `🔊 Phát âm` bên cạnh bị ép gãy làm 2 dòng (`🔊 Phát` / `âm`). Nên rút gọn nhãn thành **`Verb`** (hoặc `Modalv.`) để đồng bộ kích thước 1 dòng với 35 thẻ còn lại.