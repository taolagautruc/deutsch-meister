# ĐẶC TẢ KỸ THUẬT: BÀI 2 "SPRACHE IM KURS - ĐỘNG TỪ VÀ GIỐNG (DER / DIE / DAS)" & BỘ TRA CỨU GIỐNG - TỪ VỰNG THEO CHỦ ĐỀ

Tài liệu này hướng dẫn **Antigravity IDE / AI Agent** nâng cấp hệ thống **DeutschMeister (A1 - B2)** với 3 hạng mục trọng tâm:
1. **Xây dựng Bài 2: "Sprache im Kurs - Động Từ và Giống (der, die, das & Mạo Từ)"** dựa trên toàn bộ nội dung bài giảng gốc, mở rộng lý thuyết chuyên sâu và tuyệt đối **không gắn link YouTube**.
2. **Bổ sung Tab mới `"🏷️ Từ vựng & Giống"`** nằm **chính giữa** mục `"📖 Chia động từ"` và `"🏆 Đấu trường & BXH"`, có giao diện đồng bộ 100% với mục `"📖 Chia động từ"` (thanh tìm kiếm tức thì, bộ lọc theo chủ đề & giống, thẻ tra cứu nghĩa, giống `der/die/das`, dạng số nhiều, quy tắc nhận diện và câu ví dụ kèm phát âm chuẩn `de-DE`).
3. **Thiết lập Kho 50 câu hỏi Bài 2 + Cơ chế Random đổi đề tự động** cho các bài tập xác định giống (`der/die/das`), mạo từ (`ein/eine`, `kein/keine`), dạng số nhiều (`Plural`) và câu giao tiếp trong lớp học.

---

## PHẦN 1: THIẾT KẾ MỤC MỚI "🏷️ TỪ VỰNG & GIỐNG" (NẰM GIỮA "CHIA ĐỘNG TỪ" VÀ "ĐẤU TRƯỜNG")

### 1.1. Vị trí trên Thanh Điều Hướng (`templates/index.html`)
Cập nhật thanh Navigation Bar ở đầu trang (`header`) theo đúng thứ tự 6 nút:
1. `🎯 Cấp độ (A1 - B2)`
2. `🎓 Không gian học (A1)`
3. `📖 Chia động từ`
4. **`🏷️ Từ vựng & Giống` (MỤC MỚI — Nằm chính giữa "Chia động từ" và "Đấu trường & BXH")**
5. `🏆 Đấu trường & BXH`
6. `🗄️ Kiến trúc Python/SQL`

### 1.2. Giao diện & Tính năng của Tab "🏷️ Từ vựng & Giống" (Y hệt phong cách mục "Chia động từ")
Thiết kế giao diện đồng nhất hoàn toàn với khung **"Tra Cứu & Luyện Phát Âm Chia Động Từ"**:
* **Banner Tiêu đề**:
  * Badge nhỏ: `🏷️ DeutschMeister Genus- & Wortschatz-Lexikon • Tra Cứu Giống & Từ Vựng A1 - A2`
  * Tiêu đề lớn: **Tra Cứu Giống (`der / die / das`), Số Nhiều & Từ Vựng Theo Chủ Đề**
  * Mô tả: *Hệ thống phân loại tự động Giống đực (`der`), Giống cái (`die`), Giống trung (`das`), Dạng số nhiều (`Plural`), Mạo từ bất định (`ein/eine`), Phủ định (`kein/keine`) và Động từ theo chủ đề kèm câu ví dụ thực tế và giọng đọc bản xứ `de-DE`.*
  * Badge góc phải: `⚡ 65+ Từ vựng & Quy tắc cốt lõi`
* **Thanh tìm kiếm tức thì (Instant Search)**:
  * Placeholder: `🔍 Gõ từ tiếng Đức (Kuli, Brille, Handy, verstehen...) hoặc nghĩa tiếng Việt (bút bi, kính mắt, bảng đen, đánh vần...)`
  * Cho phép tìm theo từ gốc, mạo từ, hậu tố (`-ung`, `-heit`, `-chen`, `-ment`...) hoặc nghĩa tiếng Việt.
* **Thanh Bộ lọc (Filter Pills) theo Chủ đề & Giống**:
  * `Tất cả`
  * `🔵 Giống đực - der (Maskulinum)`
  * `🔴 Giống cái - die (Femininum)`
  * `🟢 Giống trung - das (Neutrum)`
  * `🏫 Đồ dùng & Ngôn ngữ lớp học (Sprache im Kurs)`
  * `🗣️ Động từ lớp học & Giao tiếp (Verben im Kurs)`
  * `🧩 Quy tắc hậu tố nhận biết giống (-ung, -keit, -chen, -ismus...)`
  * `☕ Đồ uống & Đời sống`
* **Thiết kế Thẻ Từ Vựng & Giống (Lexikon Card)**:
  Mỗi thẻ hiển thị rõ ràng, trực quan:
  1. **Header thẻ**:
     * Hiển thị mạo từ + từ chính (ví dụ: **`der Kuli`**, **`die Brille`**, **`das Wörterbuch`**, hoặc động từ **`buchstabieren`**) + Nút loa `🔊` phát âm chuẩn `de-DE`.
     * Badge phân loại giống có màu sắc đặc trưng:
       * **`der (Maskulinum - Giống đực)`**: Màu xanh dương (`bg-blue-500/20 text-blue-300 border-blue-500/40`)
       * **`die (Femininum - Giống cái)`**: Màu hồng/đỏ (`bg-rose-500/20 text-rose-300 border-rose-500/40`)
       * **`das (Neutrum - Giống trung)`**: Màu xanh lá/ngọc (`bg-emerald-500/20 text-emerald-300 border-emerald-500/40`)
       * **`Động từ chủ đề (Verb)`**: Màu tím (`bg-purple-500/20 text-purple-300 border-purple-500/40`)
  2. **Nghĩa tiếng Việt & Chủ đề**: Hiển thị nổi bật bên dưới từ chính.
  3. **Thông tin Ngữ pháp (Pills/Badges)**:
     * Đối với Danh từ:
       * `Số ít: der Kuli` | `Số nhiều: die Kulis`
       * `Bất định: ein Kuli` | `Phủ định: kein Kuli`
       * `Mẹo/Quy tắc`: Ví dụ *"Đuôi -chen luôn là giống trung (das)"* hoặc *"Danh từ ghép lấy giống theo từ cuối cùng (das Buch -> das Wörterbuch)"*.
     * Đối với Động từ theo chủ đề:
       * `Nguyên mẫu: wiederholen` | `Ngôi ich: wiederhole` | `Ngôi Sie: wiederholen`
  4. **Câu ví dụ thực tế (Beispielsatz)**:
     * Hiển thị 1 câu ví dụ hoàn chỉnh bằng tiếng Đức kèm dịch nghĩa tiếng Việt và nút `🔊` để nghe phát âm cả câu (Ví dụ: *"Ist das ein Kuli? – Ja, das ist der Kuli von Anna."*).

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT BÀI 2 — "SPRACHE IM KURS (ĐỘNG TỪ VÀ GIỐNG)"

Tạo tệp `seed_a1_b2.py` để nạp **Bài 2: "Sprache im Kurs - Động Từ Lớp Học, Giống Danh Từ (der/die/das) & Mạo Từ"** vào bảng `lessons` trong `deutsch_meister.db` với 6 học phần chi tiết (tuyệt đối không có link YouTube):

### Học phần 1: Khái niệm Mạo từ (Artikel), Giống của Danh từ & 4 Cách trong tiếng Đức
* **Đặc điểm cốt lõi của Danh từ tiếng Đức (Nomen / Substantive)**:
  1. **Luôn luôn viết hoa chữ cái đầu tiên** dù đứng ở đầu câu hay giữa câu (ví dụ: *der Tisch, die Brille, das Buch*).
  2. Mỗi danh từ đều mang một **giống ngữ pháp (Genus)** cố định, được thể hiện qua **Mạo từ (Artikel)** đứng trước nó.
* **3 Giống của Danh từ ở Số ít & Mạo từ Số nhiều (Cách 1 - Nominativ)**:
  * **Maskulinum (`m` - Giống đực)**: dùng mạo từ xác định **`der`** (ví dụ: *der Tisch* - cái bàn).
  * **Femininum (`f` - Giống cái)**: dùng mạo từ xác định **`die`** (ví dụ: *die Tasche* - túi xách).
  * **Neutrum (`n` - Giống trung)**: dùng mạo từ xác định **`das`** (ví dụ: *das Heft* - quyển vở).
  * **Plural (`Pl.` - Số nhiều cho cả 3 giống)**: Tất cả các danh từ khi chuyển sang số nhiều ở cách 1 đều dùng chung mạo từ xác định **`die`** (ví dụ: *die Tische, die Taschen, die Hefte*).
* **Tổng quan 4 Cách (Kasus) trong tiếng Đức**:
  * **Cách 1 — Chủ ngữ cách (`Nominativ`) (* Trọng tâm bài học)**: Dùng cho chủ ngữ của câu hoặc danh từ đứng sau động từ `sein` (*Das ist ...*), `heißen`.
  * **Cách 2 — Sở hữu cách (`Genitiv`)**: Chỉ sự sở hữu (*của ai/cái gì* — ở trình độ A1 thường dùng giới từ **`von + Tên riêng`** để thay thế, ví dụ: *der Kuli von Anna*).
  * **Cách 3 — Tân ngữ gián tiếp (`Dativ`)**: Chỉ đối tượng tiếp nhận hành động hoặc vị trí tĩnh.
  * **Cách 4 — Tân ngữ trực tiếp (`Akkusativ`)**: Chỉ đối tượng trực tiếp chịu tác động của ngoại động từ.

### Học phần 2: Bí quyết Nhận diện Giống của Danh từ (`der` / `die` / `das`) theo Đuôi hậu tố & Nhóm nghĩa
Đây là bảng quy tắc vàng giúp nhận diện nhanh giống của hàng nghìn danh từ tiếng Đức mà không cần học vẹt:

#### 1. Nhóm Giống Đực — Maskulinum (`der`)
* **Theo đuôi hậu tố**:
  * **`-ant`**: `der Praktikant` (nam thực tập sinh)
  * **`-ent`**: `der Student` (nam sinh viên)
  * **`-ich`**: `der Teppich` (tấm thảm)
  * **`-ismus`**: `der Organismus` (cơ thể sống / sinh vật), `der Tourismus` (du lịch)
  * **`-ist`**: `der Polizist` (cảnh sát), `der Optimist` (người lạc quan)
  * **`-ast`**: `der Kontrast` (sự tương phản), `der Palast` (cung điện)
  * **`-ling`**: `der Zwilling` (anh/em sinh đôi), `der Schmetterling` (con bướm)
* **Theo nhóm ý nghĩa**:
  * **Các tháng trong năm**: `der Juni` (tháng 6), `der Januar` (tháng 1), `der Mai` (tháng 5)...
  * **Các thứ trong tuần**: `der Montag` (thứ Hai), `der Dienstag` (thứ Ba), `der Sonntag` (Chủ nhật)...
  * **Các mùa trong năm**: `der Sommer` (mùa hè), `der Winter` (mùa đông), `der Frühling` (mùa xuân), `der Herbst` (mùa thu).
  * **Các hướng trong không gian**: `der Norden` (hướng Bắc), `der Süden` (hướng Nam), `der Osten` (hướng Đông), `der Westen` (hướng Tây).
  * **Đa số hiện tượng thời tiết**: `der Wind` (gió), `der Regen` (mưa), `der Schnee` (tuyết), `der Nebel` (sương mù).
  * **Danh từ chỉ nghề nghiệp nam giới**: `der Koch` (nam đầu bếp), `der Lehrer` (thầy giáo), `der Arzt` (nam bác sĩ).

#### 2. Nhóm Giống Cái — Femininum (`die`)
* **Theo đuôi hậu tố (Luôn luôn là `die` 100%)**:
  * **`-heit`**: `die Krankheit` (căn bệnh), `die Gesundheit` (sức khỏe), `die Freiheit` (sự tự do)
  * **`-keit`**: `die Möglichkeit` (khả năng / cơ hội), `die Pünktlichkeit` (tính đúng giờ)
  * **`-schaft`**: `die Freundschaft` (tình bạn), `die Mannschaft` (đội bóng)
  * **`-ung`**: `die Kleidung` (quần áo / trang phục), `die Wohnung` (căn hộ), `die Übung` (bài tập), `die Entschuldigung` (lời xin lỗi)
  * **`-ie`**: `die Allergie` (sự dị ứng), `die Biologie` (sinh học), `die Energie` (năng lượng)
  * **`-anz`**: `die Dominanz` (sự thống trị / ưu thế), `die Distanz` (khoảng cách)
  * **`-enz`**: `die Potenz` (lũy thừa / tiềm lực), `die Konferenz` (hội nghị)
  * **`-in` (Nghề nghiệp nữ giới)**: `die Sekretärin` (nữ thư ký), `die Lehrerin` (cô giáo), `die Studentin` (nữ sinh viên)
* **Theo nhóm ý nghĩa**:
  * **Đa số các loài cây**: `die Tanne` (cây thông / linh sam), `die Eiche` (cây sồi)
  * **Đa số các loài hoa**: `die Rose` (hoa hồng), `die Tulpe` (hoa tulip), `die Orchidee` (hoa lan)

#### 3. Nhóm Giống Trung — Neutrum (`das`)
* **Theo đuôi hậu tố**:
  * **`-ment`**: `das Dokument` (tài liệu), `das Medikament` (thuốc), `das Instrument` (nhạc cụ)
    * ⚠️ **Ngoại lệ cực kỳ quan trọng cần nhớ**: **`der Moment`** (khoảnh khắc / giây lát — mang giống đực!).
  * **`-um`**: `das Studium` (việc học đại học), `das Museum` (bảo tàng), `das Zentrum` (trung tâm)
  * **`-tum`**: `das Präteritum` (thì quá khứ đơn), `das Eigentum` (tài sản)
  * **`-chen` & `-lein` (Đuôi giảm nhẹ / thu nhỏ — Luôn là `das` 100%)**: `das Brötchen` (bánh mì nhỏ), `das Mädchen` (cô bé)
  * **`-ma`**: `das Thema` (chủ đề), `das Klima` (khí hậu)
  * **`-em`**: `das System` (hệ thống), `das Problem` (vấn đề)
  * **`-nis`**: `das Ergebnis` (kết quả), `das Zeugnis` (bảng điểm / chứng chỉ)
    * ⚠️ **Ngoại lệ cực kỳ quan trọng cần nhớ**: **`die Erlaubnis`** (sự cho phép / giấy phép — mang giống cái!).
* **Theo nhóm cấu tạo từ & ý nghĩa**:
  * **Danh từ có nguyên mẫu từ Động từ (Substantivierte Verben)**: Khi viết hoa động từ nguyên mẫu để biến thành danh từ chỉ hoạt động/sự việc $\rightarrow$ luôn dùng **`das`**.
    * Ví dụ: `essen` (ăn) $\rightarrow$ **`das Essen`** (việc ăn uống / bữa ăn / món ăn); `lesen` (đọc) $\rightarrow$ **`das Lesen`** (việc đọc sách).
  * **Tính từ hóa Danh từ (Substantivierte Adjektive)**:
    * Ví dụ: `gut` (tốt) $\rightarrow$ **`das Gute`** (điều tốt đẹp); `neu` (mới) $\rightarrow$ **`das Neue`** (điều mới mẻ).
  * **Đa số các nguyên tố hóa học & kim loại**: **`das Eisen`** (sắt), `das Gold` (vàng), `das Silber` (bạc).

---

### Học phần 3: Từ vựng Đồ dùng Lớp học (`Sprache im Kurs`) & Quy tắc tạo Số nhiều (`Plural`)
Bảng tổng hợp đầy đủ **18 danh từ đồ dùng học tập & lớp học** chia theo 3 giống kèm dạng **Số nhiều (`die ...`)**:

| Giống | Danh từ Số ít (Singular) | Dạng Số nhiều (Plural) | Nghĩa tiếng Việt | Quy tắc biến đổi Số nhiều & Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| **`der`** *(m)* | **`der Tisch`** | **`die Tische`** | cái bàn | Thêm đuôi **`-e`** |
| **`der`** *(m)* | **`der Stuhl`** | **`die Stühle`** | cái ghế | Thêm **`¨-e`** (biến âm `u` $\rightarrow$ `ü` + `-e`) |
| **`der`** *(m)* | **`der Füller`** | **`die Füller`** | bút máy / bút mực | Giữ nguyên **`-`** (danh từ kết thúc bằng `-er`) |
| **`der`** *(m)* | **`der Kuli`** | **`die Kulis`** | bút bi *(viết tắt của Kugelschreiber)* | Thêm đuôi **`-s`** |
| **`der`** *(m)* | **`der Bleistift`** | **`die Bleistifte`** | bút chì | Thêm đuôi **`-e`** |
| **`der`** *(m)* | **`der Radiergummi`** | **`die Radiergummis`** | cục tẩy / gôm | Thêm đuôi **`-s`** |
| **`der`** *(m)* | **`der Becher`** | **`die Becher`** | cái cốc / ly (không quai) | Giữ nguyên **`-`** (kết thúc bằng `-er`) |
| **`die`** *(f)* | **`die Tafel`** | **`die Tafeln`** | cái bảng đen | Thêm đuôi **`-n`** |
| **`die`** *(f)* | **`die Brille`** | **`die Brillen`** | cái kính mắt | Thêm đuôi **`-n`** (danh từ `die` tận cùng bằng `-e`) |
| **`die`** *(f)* | **`die Tasche`** | **`die Taschen`** | túi xách / cặp sách | Thêm đuôi **`-n`** |
| **`die`** *(f)* | **`die Landkarte`** | **`die Landkarten`** | bản đồ | Thêm đuôi **`-n`** |
| **`das`** *(n)* | **`das Papier`** | **`die Papiere`** | tờ giấy | Thêm đuôi **`-e`** |
| **`das`** *(n)* | **`das Heft`** | **`die Hefte`** | quyển vở | Thêm đuôi **`-e`** |
| **`das`** *(n)* | **`das Buch`** | **`die Bücher`** | quyển sách | Thêm **`¨-er`** (biến âm `u` $\rightarrow$ `ü` + `-er`) |
| **`das`** *(n)* | **`das Wörterbuch`** | **`die Wörterbücher`** | quyển từ điển | Danh từ ghép (`Wörter` + `das Buch`) $\rightarrow$ lấy giống `das` và số nhiều theo từ cuối `Bücher`! |
| **`das`** *(n)* | **`das Handy`** | **`die Handys`** | điện thoại di động | Thêm đuôi **`-s`** (từ mượn/kết thúc nguyên âm) |
| **`das`** *(n)* | **`das Whiteboard`** | **`die Whiteboards`** | bảng trắng | Thêm đuôi **`-s`** |
| **`das`** *(n)* | **`das Brötchen`** | **`die Brötchen`** | bánh mì nhỏ | Giữ nguyên **`-`** (danh từ đuôi `-chen` số nhiều không đổi) |

---

### Học phần 4: Động từ & Mẫu câu Giao tiếp trong Lớp học (`Sprache im Kurs`)
Khi học trên lớp, nếu chưa biết tên một đồ vật hoặc chưa nghe kịp giáo viên nói, người học sử dụng **6 mẫu câu vàng** và **5 động từ trọng tâm** sau:

#### 1. Các Động từ Lớp học cốt lõi (`Verben im Kurs`)
* **`heißen`** (gọi là / tên là): *Wie **heißt** das auf Deutsch?*
* **`verstehen`** (hiểu): *Ich **verstehe** das nicht.* / *Das **verstehe** ich nicht.* (Đảo tân ngữ `Das` lên đầu câu để nhấn mạnh, động từ `verstehe` vẫn giữ vững ở vị trí số 2!).
* **`können`** (có thể — động từ khuyết thiếu): ***Können** Sie das bitte ...?* (Ngài có thể làm ơn ... điều đó được không? — Động từ chính đứng ở cuối câu ở dạng nguyên mẫu).
* **`wiederholen`** (lặp lại / nhắc lại): *Können Sie das bitte **wiederholen**?*
* **`buchstabieren`** (đánh vần): *Können Sie das bitte **buchstabieren**?* (Ví dụ đánh vần `das Heft`: *ha – e – ef – te*).
* **`anschreiben`** (viết lên bảng — động từ tách): *Können Sie das bitte **anschreiben**?*

#### 2. 6 Mẫu câu Giao tiếp chuẩn trong Lớp học
1. **`Wie heißt das auf Deutsch?`** $\rightarrow$ Cái này tiếng Đức gọi là gì?
2. **`Was ist das auf Deutsch?`** $\rightarrow$ Cái này trong tiếng Đức là gì?
3. **`Entschuldigung, wie bitte?`** $\rightarrow$ Xin lỗi, Ngài nói sao cơ ạ? (Dùng khi nghe không rõ).
4. **`Das verstehe ich nicht. Können Sie das bitte wiederholen?`** $\rightarrow$ Điều này tôi không hiểu. Ngài có thể vui lòng lặp lại được không ạ?
5. **`Das verstehe ich nicht. Können Sie das bitte buchstabieren?`** $\rightarrow$ Điều này tôi không hiểu. Ngài có thể vui lòng đánh vần từ đó được không ạ?
6. **`Das verstehe ich nicht. Können Sie das bitte anschreiben?`** $\rightarrow$ Điều này tôi không hiểu. Ngài có thể vui lòng viết từ đó lên bảng được không ạ?

---

### Học phần 5: Hệ thống Mạo từ Xác định (`der/die/das`), Mạo từ Bất định (`ein/eine`) & Phủ định với `kein/keine` (Cách 1 - Nominativ)

#### 1. Bảng đối chiếu 3 cột Mạo từ ở Cách 1 (Nominativ)
| Phân loại Giống | Mạo từ Xác định (`der bestimmte Artikel` — *cái đã biết rõ*) | Mạo từ Bất định (`der unbestimmte Artikel` — *một cái bất kỳ*) | Mạo từ Phủ định (`Verneinung mit "kein"` — *không phải là...*) |
| :--- | :--- | :--- | :--- |
| **Maskulinum (`der`)** | **`der`** Kuli | **`ein`** Kuli | **`kein`** Kuli |
| **Femininum (`die`)** | **`die`** Brille | **`eine`** Brille | **`keine`** Brille |
| **Neutrum (`das`)** | **`das`** Handy | **`ein`** Handy | **`kein`** Handy |
| **Plural (`die` - Số nhiều)** | **`die`** Bücher | **`—` (Không có)** Bücher | **`keine`** Bücher |

#### 2. Quy tắc sử dụng & Ghi nhớ nhanh
* **Mạo từ bất định (`ein` / `eine`)**:
  * Nghĩa là *"một"*, dùng khi nhắc đến sự vật lần đầu tiên hoặc chưa xác định cụ thể của ai.
  * Giống đực (`der`) và giống trung (`das`) đều dùng **`ein`** (*ein Kuli, ein Handy, ein Buch, ein Becher*).
  * Giống cái (`die`) dùng **`eine`** (*eine Brille, eine Tasche, eine Tafel, eine Landkarte*).
  * **Số nhiều (`Plural`) tuyệt đối KHÔNG có mạo từ bất định** (chỉ nói *Das sind Bücher*, không có *eine Bücher*).
* **Mạo từ phủ định (`kein` / `keine`)**:
  * Dùng để phủ định một danh từ có mạo từ bất định hoặc không có mạo từ (*"không phải là một..."* / *"không có..."*).
  * Cách chia cực dễ: Chỉ cần thêm chữ **`k-`** vào trước `ein` / `eine`:
    * Giống đực (`der`) & Giống trung (`das`) $\rightarrow$ **`kein`** (*kein Kuli, kein Handy, kein Buch*).
    * Giống cái (`die`) & **Số nhiều (`Plural`)** $\rightarrow$ **`keine`** (*keine Brille, keine Bücher*).
* **Khi nào dùng lại Mạo từ xác định (`der / die / das`)?**:
  * Khi đồ vật đó đã được xác định cụ thể (ví dụ: có cụm chỉ sở hữu **`von + Tên người`** theo sau như *von Anna, von David, von Frau Schiller*).

---

### Học phần 6: Thực hành Hỏi - Đáp Đồ vật & Sở hữu (`Ist das ein/eine ...?`)
Phân tích 5 tình huống hội thoại chuẩn trên bảng:
1. **Câu 1 (`der Kuli` — Giống đực)**:
   * Hỏi: *Ist das **ein** Kuli?* (Đây có phải là một cây bút bi không?)
   * Trả lời khẳng định (xác định chủ sở hữu): *Ja, das ist **der** Kuli **von Anna**.* (Đúng vậy, đó là cây bút bi của Anna.)
2. **Câu 2 (`das Handy` — Giống trung)**:
   * Hỏi: *Ist das **ein** Handy?* (Đây có phải là một chiếc điện thoại không?)
   * Trả lời: *Ja, das ist **das** Handy **von David**.* (Đúng vậy, đó là chiếc điện thoại của David.)
3. **Câu 3 (`das Buch` — Giống trung)**:
   * Hỏi: *Ist das **ein** Buch?* (Đây có phải là một quyển sách không?)
   * Trả lời: *Ja, das ist **das** Buch **von Frau Schiller**.* (Đúng vậy, đó là quyển sách của bà Schiller.)
4. **Câu 4 (`die Brille` & `die Landkarte` — Giống cái)**:
   * Hỏi: *Ist das **eine** Brille?* (Đây có phải là một cặp kính mắt không?)
   * Trả lời phủ định + đính chính: *Nein, das ist **keine** Brille. Das ist **eine** Landkarte.* (Không, đó không phải là kính mắt. Đó là một tấm bản đồ.)
   * *(Hoặc nếu trả lời khẳng định: Ja, das ist **die** Brille von David.)*
5. **Câu 5 (`der Becher` — Giống đực & `das Papier` — Giống trung)**:
   * Hỏi: *Ist das **ein** Becher?* (Đây có phải là một cái cốc không?)
   * Trả lời: *Nein, das ist (**kein** Becher. Das ist) **ein** Papier.* (Không, đó là một tờ giấy.)

---

## PHẦN 3: KHO 50 CÂU HỎI BÀI 2 & CƠ CHẾ RANDOM ĐỔI ĐỀ TỰ ĐỘNG

Trong tệp `seed_a1_b2.py`, nạp **đúng 50 câu hỏi** vào bảng `exercises` cho Bài 2, phân bổ đều qua 7 dạng kỹ năng:
1. **Dạng 1 - Trắc nghiệm (`trac_nghiem` - 10 câu)**:
   * Nhận diện giống `der / die / das` qua hậu tố (`-ung`, `-heit`, `-keit`, `-schaft`, `-chen`, `-ment`, `-um`, `-nis`, `-ant`, `-ist`, `-ismus`, `-ling`) và nhóm nghĩa (thứ, tháng, mùa, hướng, thời tiết, cây, hoa).
   * Bẫy ngoại lệ kinh điển: **`der Moment`** (đuôi `-ment` nhưng là `der`) và **`die Erlaubnis`** (đuôi `-nis` nhưng là `die`).
   * Quy tắc danh từ ghép: `das Wörterbuch` lấy giống theo `das Buch`.
2. **Dạng 2 - Điền khuyết Mạo từ & Động từ lớp học (`dien_khuyet` - 10 câu)**:
   * Điền `der / die / das`, `ein / eine`, `kein / keine` vào các câu hỏi - đáp (*"Ist das ___ Brille? – Nein, das ist ___ Brille."*).
   * Điền động từ lớp học: `verstehe`, `wiederholen`, `buchstabieren`, `anschreiben`, `heißt`.
   * Điền dạng số nhiều đúng của danh từ (*der Stuhl $\rightarrow$ die Stühle*, *das Buch $\rightarrow$ die Bücher*, *die Tasche $\rightarrow$ die Taschen*).
3. **Dạng 3 - Dịch 2 chiều Việt ⇄ Đức (`dich` - 8 câu)**:
   * Dịch các câu giao tiếp trong lớp học (*"Cái này tiếng Đức gọi là gì?"*, *"Tôi không hiểu điều đó. Ngài có thể đánh vần từ đó được không?"*, *"Ngài có thể viết lên bảng được không?"*).
   * Dịch các câu hỏi đáp đồ vật & sở hữu (*"Đây có phải là điện thoại không? – Đúng, đó là điện thoại của David."*).
4. **Dạng 4 - Luyện Nghe 1.0x & 0.65x (`nghe` - 6 câu)**:
   * Nghe câu hỏi trong lớp học và câu xác định đồ vật (*"Nein, das ist keine Brille. Das ist eine Landkarte."*, *"Ja, das ist das Buch von Frau Schiller."*) để điền đúng từ/mạo từ nghe được.
5. **Dạng 5 - Luyện Nói & Phát âm (`noi` - 5 câu)**:
   * Luyện đọc chuẩn các câu: *"Wie heißt das auf Deutsch?"*, *"Das verstehe ich nicht. Können Sie das bitte wiederholen?"*, *"Können Sie das bitte buchstabieren?"*, *"Nein, das ist keine Brille. Das ist eine Landkarte."*, *"Ja, das ist das Wörterbuch von Frau Schiller."*
6. **Dạng 6 - Đọc hiểu tình huống Lớp học (`doc` - 4 câu)**:
   * Đọc đoạn hội thoại trong giờ học tiếng Đức giữa cô giáo (`Frau Schiller`) và các học viên (`Anna, David, Marc`) khi hỏi từ vựng, nhờ đánh vần, viết lên bảng và tìm đồ dùng học tập trên bàn.
7. **Dạng 7 - Viết câu, Chuyển đổi Số nhiều & Sắp xếp câu (`viet` - 7 câu)**:
   * Viết câu trả lời phủ định với `kein/keine` và khẳng định với `der/die/das ... von ...`.
   * Chuyển cụm danh từ từ số ít sang số nhiều và ngược lại.

### Cơ chế Random Đổi Đề Tự Động cho Bài 2 (`templates/index.html`)
Bổ sung thêm 2 chế độ sinh đề ngẫu nhiên vào hàm `randomizeDynamicExercises()` trên Frontend để mỗi lần người học **làm xong bấm `🔄 Đổi đề khác`** hoặc **thoát ra vào lại**:
1. **Random câu hỏi Mạo từ & Phủ định (`dynamic_article_quiz`)**:
   * Tự động lấy ngẫu nhiên 2 danh từ khác nhau trong ngân hàng `GERMAN_LEXIKON_DB` (ví dụ: Danh từ 1 = `die Tasche`, Danh từ 2 = `der Bleistift`) để sinh câu hỏi mới:
   * Đề: *"Hoàn thành câu trả lời phủ định: 'Ist das [ein/eine] [Noun1]?' $\rightarrow$ 'Nein, das ist ___ [Noun1]. Das ist ___ [Noun2].'"*
   * Đáp án tự động cập nhật theo đúng giống của 2 danh từ vừa random (ví dụ: `keine, ein` hoặc viết cả câu).
2. **Random câu hỏi Sở hữu với Mạo từ xác định (`dynamic_possessive_article`) & Số nhiều (`dynamic_plural_quiz`)**:
   * Tự động chọn ngẫu nhiên 1 danh từ và 1 tên người (*Anna, David, Marc, Frau Schiller, Herr Nguyen*) để yêu cầu người học điền đúng `ein/eine` và `der/die/das` hoặc viết dạng số nhiều (`die ...`) của danh từ đó.

---

## PHẦN 4: DỮ LIỆU CHUẨN CHO TAB "🏷️ TỪ VỰNG & GIỐNG" (`GERMAN_LEXIKON_DB`)

Antigravity IDE hãy tích hợp mảng dữ liệu `GERMAN_LEXIKON_DB` dưới đây vào `templates/index.html` để hiển thị trong **Tab "🏷️ Từ vựng & Giống"** và dùng làm nguồn cho bộ Random bài tập:

```javascript
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
        example: "Die Lehrerin пишет an die Tafel. Das ist eine Tafel.",
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
    }
];
```

---

## PHẦN 5: CÁC BƯỚC THỰC THI DÀNH CHO ANTIGRAVITY IDE

1. **Tạo và chạy tệp `seed_a1_b2.py`**:
   * Thêm bài học thứ 3 của cấp độ A1: `Bài 2: "Sprache im Kurs - Động Từ và Giống (der/die/das & Mạo Từ)"` vào bảng `lessons` trong `deutsch_meister.db`.
   * Nạp toàn bộ từ vựng đồ dùng lớp học, các danh từ theo quy tắc hậu tố và 6 mẫu câu giao tiếp lớp học vào bảng `vocabulary`.
   * Nạp đủ **50 câu hỏi** vào bảng `exercises` cho Bài 2, gắn cờ `dynamic_article_quiz`, `dynamic_possessive_article` và `dynamic_plural_quiz` trong `extra_data` để kích hoạt tính năng Random đổi đề tự động.
2. **Cập nhật tệp `templates/index.html`**:
   * Thêm nút **`🏷️ Từ vựng & Giống`** nằm **chính giữa** `"📖 Chia động từ"` và `"🏆 Đấu trường & BXH"`.
   * Xây dựng giao diện tra cứu `"🏷️ Từ vựng & Giống"` đồng bộ hoàn toàn với giao diện `"📖 Chia động từ"` (tìm kiếm tức thì, bộ lọc theo giống `der/die/das` và chủ đề, thẻ hiển thị số ít/số nhiều/bất định/phủ định, câu ví dụ kèm phát âm `speakGerman` chuẩn `de-DE`).
   * Bổ sung quy tắc đọc phân biệt rõ `ein` vs `eine`, `kein` vs `keine`, `Stühle`, `Bücher`, `Wörterbuch`, `Brötchen` trong `GERMAN_PRONUNCIATION_MAP`.
3. **Kiểm tra & Đẩy lên GitHub / Render**:
   * Chạy `python3 seed_a1_b2.py` để cập nhật `deutsch_meister.db`.
   * Kiểm tra cú pháp `python3 -m py_compile app.py seed_a1_b2.py`.
   * Sau khi kiểm tra trên máy Mac hoàn tất, chạy `git add . && git commit -m "Add Lesson 2 and Genus/Lexikon Lookup Tab" && git push` để tự động cập nhật lên đường link Public vĩnh viễn trên Render.