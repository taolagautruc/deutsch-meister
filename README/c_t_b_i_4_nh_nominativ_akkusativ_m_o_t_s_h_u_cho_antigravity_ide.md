# ĐẶC TẢ KỸ THUẬT: BÀI 4 "NHÀ Ở - CÁCH 1 NOMINATIV / CÁCH 4 AKKUSATIV VÀ MẠO TỪ SỞ HỮU (MENSCHEN UND HÄUSER)"

> **NGUYÊN TẮC BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
> 1. **Cộng dồn & Mở rộng tuyệt đối (Additive Expansion Only)**: Tuyệt đối **KHÔNG ĐƯỢC XÓA BỚT** bất kỳ bài học nào đã có (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**) cũng như dữ liệu trong `static/js/verbs_db.js` và `static/js/lexikon_db.js`. Mọi nội dung của **Bài 4** phải được **nối tiếp bổ sung** để làm dày thêm kho kiến thức.
> 2. **Trình bày Bảng biểu Trực quan theo Ngôi – Giống – Cách**: Trong giao diện bài học lý thuyết của Bài 4 (và các bài ngữ pháp về sau), **bắt buộc phải trình bày bằng hệ thống Bảng ma trận (HTML/Tailwind Table)** chia rõ theo **Giống (`Maskulinum - der`, `Femininum - die`, `Neutrum - das`, `Plural - die`)**, **Cách (`Nominativ` vs. `Akkusativ`)**, và **9 Ngôi nhân xưng (`ich, du, er, es, sie, wir, ihr, sie, Sie`)** với màu sắc phân biệt trực quan để người học nhìn vào là nhớ ngay quy luật.
> 3. **Quy mô 50 Bài tập Ngữ pháp Chuyên sâu & Random Đổi đề**: Tạo tệp `lessons/a1/seed_a1_b4.py` nạp **đúng 50 câu hỏi** đánh mạnh vào ngữ pháp phân biệt `Nominativ` / `Akkusativ`, chia đuôi Mạo từ sở hữu (`Possessivartikel`), kết hợp từ vựng nhà ở – nội thất – tính từ và cơ chế **Random đổi đề tự động** khi bấm nút `🔄 Đổi đề khác` hoặc thoát ra vào lại.

---

## PHẦN 1: CẤU TRÚC TỆP DỰ ÁN CẦN CẬP NHẬT

Dựa trên cấu trúc hiện tại của dự án `deutsch_meister`, Antigravity IDE cần thực hiện:
1. **Tạo mới tệp `lessons/a1/seed_a1_b4.py`**: Nạp toàn bộ nội dung Lý thuyết (7 học phần kèm bảng ma trận HTML), Từ vựng (45+ mục từ) và 50 Bài tập Ngữ pháp của **Bài 4: `"Bài 4: Nhà ở - Cách 1 Nominativ / Cách 4 Akkusativ và Mạo từ sở hữu"`** vào `deutsch_meister.db`.
2. **Cập nhật `static/js/lexikon_db.js`**: Nối thêm toàn bộ danh từ chủ đề **Nhà ở & Các phòng (`Menschen und Häuser`)**, **Nội thất (`Möbel & Einrichtung`)** và **Bảng tra cứu nhanh Mạo từ sở hữu (`Possessivartikel`)** vào Tab `"🏷️ Từ vựng & Giống"`.
3. **Cập nhật `static/js/verbs_db.js`**: Bổ sung các động từ đòi hỏi Cách 4 (`Akkusativ`) xuất hiện trong Bài 4 (`finden` - cảm thấy/thấy rằng, `suchen` - tìm kiếm, `brauchen` - cần, `kaufen` - mua, `es gibt` - có [tồn tại]).
4. **Cập nhật `templates/index.html`**: Bổ sung các chế độ Random bài tập ngữ pháp của Bài 4 vào hàm `randomizeDynamicExercises()`.

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT BÀI 4 — "MENSCHEN UND HÄUSER: NHÀ Ở - CÁCH 1 NOMINATIV / CÁCH 4 AKKUSATIV & MẠO TỪ SỞ HỮU"

Nội dung lý thuyết của Bài 4 trong `lessons/a1/seed_a1_b4.py` phải được thiết kế dài, chi tiết, trình bày đẹp mắt thành **7 Học phần chuyên sâu** với đầy đủ **các Bảng ma trận theo Giống, Cách và Ngôi** dưới đây:

---

### HỌC PHẦN 1: TỪ VỰNG CHỦ ĐỀ NHÀ Ở & CÁC PHÒNG (`MENSCHEN UND HÄUSER`)

Tất cả danh từ chỉ không gian sống được phân loại nghiêm ngặt theo **3 Giống (`Maskulinum - der`, `Femininum - die`, `Neutrum - das`)** kèm theo **dạng Số nhiều (`Plural`)** và nút phát âm `🔊`:

#### 1.1. Bảng Phân Loại Danh Từ Nhà Ở Theo 3 Giống (`der` / `die` / `das`)

| Giống Đực (`Maskulinum` - **`der`**) | Giống Cái (`Femininum` - **`die`**) | Giống Trung (`Neutrum` - **`das`**) |
| :--- | :--- | :--- |
| 🔵 **`der Garten`** *(Số nhiều: `die Gärten`)*<br>👉 **Khu vườn** *(thêm Umlaut `a -> ä` ở số nhiều)* | 🔴 **`die Wohnung`** *(Số nhiều: `die Wohnungen`)*<br>👉 **Căn hộ** *(hậu tố `-ung` luôn là `die`, thêm `-en`)* | 🟢 **`das Haus`** *(Số nhiều: `die Häuser`)*<br>👉 **Ngôi nhà** *(thêm Umlaut `a -> ä` và đuôi `-er`)* |
| 🔵 **`der Balkon`** *(Số nhiều: `die Balkone`)*<br>👉 **Ban công** *(số nhiều thêm `-e`)* | 🔴 **`die Garage`** *(Số nhiều: `die Garagen`)*<br>👉 **Ga-ra ô tô / Nhà để xe** *(tận cùng `-e`, thêm `-n`)* | 🟢 **`das Wohnheim`** *(Số nhiều: `die Wohnheime`)*<br>👉 **Ký túc xá** *(ghép `wohnen` + `das Heim`, thêm `-e`)* |
| 🔵 **`der Flur`** *(Số nhiều: `die Flure`)*<br>👉 **Hành lang** *(số nhiều thêm `-e`)* | 🔴 **`die Terrasse`** *(Số nhiều: `die Terrassen`)*<br>👉 **Hiên nhà / Sân thượng** *(tận cùng `-e`, thêm `-n`)* | 🟢 **`das Fenster`** *(Số nhiều: `die Fenster`)*<br>👉 **Cửa sổ** *(tận cùng `-er`, số nhiều giữ nguyên)* |
| 🔵 **`der Keller`** *(Số nhiều: `die Keller`)*<br>👉 **Tầng hầm** *(tận cùng `-er`, số nhiều giữ nguyên)* | 🔴 **`die Küche`** *(Số nhiều: `die Küchen`)*<br>👉 **Nhà bếp / Phòng bếp** *(tận cùng `-e`, thêm `-n`)* | 🟢 **`das Zimmer`** *(Số nhiều: `die Zimmer`)*<br>👉 **Căn phòng** *(tận cùng `-er`, số nhiều giữ nguyên)* |
| *(Mở rộng)* 🔵 **`der Stock`** / **`die Etage`**<br>👉 **Tầng lầu** | 🔴 **`die Toilette`** *(Số nhiều: `die Toiletten`)*<br>👉 **Nhà vệ sinh** *(tận cùng `-e`, thêm `-n`)* | *(Mở rộng)* 🟢 **`das Bad`** *(Số nhiều: `die Bäder`)*<br>👉 **Phòng tắm** *(viết gọn của `das Badezimmer`)* |

#### 1.2. Bảng Hệ Thống Danh Từ Ghép Chỉ Các Phòng Trong Nhà (`Komposita mit "das Zimmer"`)
> 💡 **Quy tắc Danh từ ghép (`Komposita`)**: Vì từ đứng cuối cùng là **`das Zimmer`** (căn phòng - giống trung, số nhiều là **`die Zimmer`** giữ nguyên), nên **TẤT CẢ các phòng ghép với `-zimmer` đều mang giống trung (`das`) và dạng số nhiều đều giữ nguyên không thêm đuôi**!

| STT | Danh từ ghép (`Singular`) | Dạng Số nhiều (`Plural`) | Cấu tạo từ ghép | Nghĩa tiếng Việt | Câu ví dụ thực tế |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **`das Wohnzimmer`** | `die Wohnzimmer` | `wohnen` (sống/ở) + `das Zimmer` | **Phòng khách** | *Das Wohnzimmer ist groß und hell.* |
| 2 | **`das Badezimmer`** | `die Badezimmer` | `baden` (tắm) + `das Zimmer` | **Phòng tắm** | *Das Badezimmer ist modern.* |
| 3 | **`das Schlafzimmer`** | `die Schlafzimmer` | `schlafen` (ngủ) + `das Zimmer` | **Phòng ngủ** | *Mein Schlafzimmer ist sehr gemütlich.* |
| 4 | **`das Esszimmer`** | `die Esszimmer` | `essen` (ăn) + `das Zimmer` | **Phòng ăn** | *Wir essen zusammen im Esszimmer.* |
| 5 | **`das Arbeitszimmer`** | `die Arbeitszimmer` | `die Arbeit` (công việc) + `s` + `das Zimmer` | **Phòng làm việc** | *Mein Arbeitszimmer hat einen Tisch.* |
| 6 | **`das Kinderzimmer`** | `die Kinderzimmer` | `die Kinder` (trẻ em) + `das Zimmer` | **Phòng trẻ em** | *Das Kinderzimmer ist klein, aber schön.* |

---

### HỌC PHẦN 2: HỆ THỐNG 4 CÁCH (`4 KASUS`) & SO SÁNH CÁCH 1 (`NOMINATIV`) VS. CÁCH 4 (`AKKUSATIV`)

#### 2.1. Bảng Tổng Quan 4 Cách Trong Ngữ Pháp Tiếng Đức (`Die 4 Kasus`)

| Ký hiệu | Tên Cách (Tiếng Đức) | Tên gọi Tiếng Việt | Chức năng Ngữ pháp Cốt lõi | Câu hỏi nhận diện | Mức độ ưu tiên ở A1 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`C1`** | **`Nominativ`** | **Chủ ngữ cách** | Đóng vai trò làm **Chủ ngữ (`Subjekt`)** thực hiện hành động, hoặc đứng sau các động từ nối như **`sein`** (*thì, là, ở*), **`heißen`** (*tên là*), **`werden`** (*trở thành*). | `Wer?` (Ai?)<br>`Was?` (Cái gì?) | ⭐⭐⭐⭐⭐ *(Trọng tâm Bài 1 – Bài 4)* |
| **`C2`** | **`Genitiv`** | **Sở hữu cách** | Biểu thị sự sở hữu (*của ai / của cái gì*). Ở trình độ A1–A2 thường được thay thế bằng cấu trúc **`von + Dativ`** (*das Buch von Lena*). | `Wessen?` (Của ai?) | ⭐⭐ *(Học sâu ở A2/B1)* |
| **`C3`** | **`Dativ`** | **Tân ngữ gián tiếp** | Đóng vai trò là người/vật nhận tác động gián tiếp, hoặc đứng sau các giới từ chỉ vị trí tĩnh như **`in`**, **`aus`**, **`auf`**, **`an`**, **`mit`**, **`von`**. | `Wem?` (Cho ai?)<br>`Wo?` (Ở đâu?) | ⭐⭐⭐⭐ *(Đã gặp qua `im Norden`, `aus der Schweiz`)* |
| **`C4`** | **`Akkusativ`** | **Tân ngữ trực tiếp** | Đóng vai trò là **Tân ngữ trực tiếp (`Direktes Objekt`)** chịu sự tác động trực tiếp của ngoại động từ (**`haben, finden, brauchen, suchen, kaufen, sehen, lesen, trinken, nehmen, möchten...`**) và cấu trúc **`es gibt + Akkusativ`** (*có...*). | `Wen?` (Ai?)<br>`Was?` (Cái gì?) | ⭐⭐⭐⭐⭐ *(Trọng tâm cốt lõi của Bài 4)* |

---

#### 2.2. Quy Luật Vàng Khi Chuyển Từ Cách 1 (`Nominativ`) Sang Cách 4 (`Akkusativ`)
> 🔥 **QUY LUẬT DUY NHẤT CẦN NHỚ (90% GIỮ NGUYÊN, CHỈ GIỐNG ĐỰC THAY ĐỔI!)**:
> Khi chuyển từ Cách 1 (`Nominativ`) sang Cách 4 (`Akkusativ`):
> * **Chỉ duy nhất Danh từ Giống Đực (`Maskulinum - der`) bị biến đổi mạo từ sang đuôi `-en`**:
>   * **`der`** $\longrightarrow$ **`den`**
>   * **`ein`** $\longrightarrow$ **`einen`**
>   * **`kein`** $\longrightarrow$ **`keinen`**
>   * **`mein / dein / sein / ihr / unser / euer / Ihr`** $\longrightarrow$ **`meinen / deinen / seinen / ihren / unseren / euren / Ihren`**
> * **Tất cả các giống còn lại — Giống Cái (`Femininum - die`), Giống Trung (`Neutrum - das`) và Số Nhiều (`Plural - die`) — GIỮ NGUYÊN 100% NHƯ Ở NOMINATIV!**

---

#### 2.3. Bảng Ma Trận Đối Chiếu 3 Loại Mạo Từ: `Nominativ` (Cách 1) vs. `Akkusativ` (Cách 4)

##### BẢNG A: MẠO TỪ XÁC ĐỊNH (`DER BESTIMMTE ARTIKEL` — Khi vật đã xác định / được nhắc đến từ lần thứ 2)

| Giống / Số | Ký hiệu | Cách 1 (`Nominativ` - Chủ ngữ) | $\longrightarrow$ | Cách 4 (`Akkusativ` - Tân ngữ trực tiếp) | Ví dụ đối chiếu `Nominativ` vs. `Akkusativ` |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **Giống Đực (`Maskulinum`)** | **`m`** | 🔵 **`der`** `Garten` | $\longrightarrow$ | 🔴 **`den`** `Garten` *(Đổi thành **`den`**!)* | *`Der Garten` (C1) ist groß. $\rightarrow$ Ich finde **`den Garten`** (C4) sehr schön.* |
| **Giống Cái (`Femininum`)** | **`f`** | **`die`** `Wohnung` | $\longrightarrow$ | **`die`** `Wohnung` *(Giữ nguyên)* | *`Die Küche` (C1) ist neu. $\rightarrow$ Ich finde **`die Küche`** (C4) zu klein.* |
| **Giống Trung (`Neutrum`)** | **`n`** | **`das`** `Zimmer` | $\longrightarrow$ | **`das`** `Zimmer` *(Giữ nguyên)* | *`Das Zimmer` (C1) ist hell. $\rightarrow$ Ich miete **`das Zimmer`** (C4).* |
| **Số Nhiều (`Plural`)** | **`Pl`** | **`die`** `Toiletten` | $\longrightarrow$ | **`die`** `Toiletten` *(Giữ nguyên)* | *`Die Häuser` (C1) sind alt. $\rightarrow$ Wir kaufen **`die Häuser`** (C4).* |

##### BẢNG B: MẠO TỪ KHÔNG XÁC ĐỊNH (`DER UNBESTIMMTE ARTIKEL` — Khi vật mới được nhắc đến lần đầu tiên)

| Giống / Số | Ký hiệu | Cách 1 (`Nominativ` - Chủ ngữ) | $\longrightarrow$ | Cách 4 (`Akkusativ` - Tân ngữ trực tiếp) | Ví dụ đối chiếu `Nominativ` vs. `Akkusativ` |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **Giống Đực (`Maskulinum`)** | **`m`** | 🔵 **`ein`** `Garten` | $\longrightarrow$ | 🔴 **`einen`** `Garten` *(Thêm **`-en`**!)* | *Das ist `ein Balkon` (C1). $\rightarrow$ Oben gibt es **`einen Balkon`** (C4).* |
| **Giống Cái (`Femininum`)** | **`f`** | **`eine`** `Wohnung` | $\longrightarrow$ | **`eine`** `Wohnung` *(Giữ nguyên)* | *Das ist `eine Küche` (C1). $\rightarrow$ Das Haus hat **`eine Küche`** (C4).* |
| **Giống Trung (`Neutrum`)** | **`n`** | **`ein`** `Zimmer` | $\longrightarrow$ | **`ein`** `Zimmer` *(Giữ nguyên)* | *Das ist `ein Haus` (C1). $\rightarrow$ Wir haben **`ein Haus`** (C4).* |
| **Số Nhiều (`Plural`)** | **`Pl`** | *(Không có `ein`)* `Toiletten` | $\longrightarrow$ | *(Không có `ein`)* `Toiletten` *(Giữ nguyên)* | *Das sind `Zimmer` (C1). $\rightarrow$ Unser Haus hat `5 Zimmer` (C4).* |

##### BẢNG C: MẠO TỪ PHỦ ĐỊNH (`VERNEINUNG MIT "KEIN"` — Phủ định cho danh từ không xác định / không có مạo từ)

| Giống / Số | Ký hiệu | Cách 1 (`Nominativ` - Chủ ngữ) | $\longrightarrow$ | Cách 4 (`Akkusativ` - Tân ngữ trực tiếp) | Ví dụ đối chiếu `Nominativ` vs. `Akkusativ` |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **Giống Đực (`Maskulinum`)** | **`m`** | 🔵 **`kein`** `Garten` | $\longrightarrow$ | 🔴 **`keinen`** `Garten` *(Thêm **`-en`**!)* | *Das ist `kein Keller` (C1). $\rightarrow$ Die Wohnung hat **`keinen Keller`** (C4).* |
| **Giống Cái (`Femininum`)** | **`f`** | **`keine`** `Wohnung` | $\longrightarrow$ | **`keine`** `Wohnung` *(Giữ nguyên)* | *Das ist `keine Garage` (C1). $\rightarrow$ Wir haben **`keine Garage`** (C4).* |
| **Giống Trung (`Neutrum`)** | **`n`** | **`kein`** `Zimmer` | $\longrightarrow$ | **`kein`** `Zimmer` *(Giữ nguyên)* | *Das ist `kein Bad` (C1). $\rightarrow$ Das Zimmer hat **`kein Fenster`** (C4).* |
| **Số Nhiều (`Plural`)** | **`Pl`** | **`keine`** `Toiletten` | $\longrightarrow$ | **`keine`** `Toiletten` *(Giữ nguyên)* | *Das sind `keine Toiletten` (C1). $\rightarrow$ Hier gibt es **`keine Toiletten`** (C4).* |

---

#### 2.4. Khi Nào Dùng `Nominativ`? Khi Nào Dùng `Akkusativ`? (Bảng So Sánh Thực Chiến)

| Tiêu chí | Dùng Cách 1 (`Nominativ`: `der / ein / kein`) | Dùng Cách 4 (`Akkusativ`: **`den / einen / keinen`** cho giống đực) |
| :--- | :--- | :--- |
| **1. Vị trí & Vai trò trong câu** | Làm **Chủ ngữ (`Subjekt`)** đứng đầu câu hoặc ngay sau động từ đảo ngữ. | Làm **Tân ngữ trực tiếp (`Objekt`)** nhận tác động của động từ. |
| **2. Các động từ đi kèm phổ biến nhất** | • **`sein`** (*bin, bist, ist, sind, seid; war, warst, waren, wart*)<br>• **`heißen`** (*tên là*)<br>• **`liegen`** (*nằm ở — chủ ngữ địa danh*) | • **`haben`** (*có / sở hữu*: *Wir haben **einen** Garten*)<br>• **`es gibt`** (*có [tồn tại]*: *Oben gibt es **einen** Balkon*)<br>• **`finden`** (*cảm thấy / đánh giá*: *Ich finde **den** Garten schön*)<br>• **`brauchen`** (*cần*), **`suchen`** (*tìm*), **`kaufen`** (*mua*), **`mieten`** (*thuê*), **`sehen`** (*nhìn*), **`trinken`** (*uống*), **`nehmen`** (*dùng/lấy*) |
| **3. Câu mẫu minh họa trực tiếp** | • *Das **ist** **`ein`** Flur. **`Der`** Flur **ist** lang und dunkel.*<br>• ***`Mein`** Wohnzimmer **ist** hell und modern.* | • *Das Haus **hat** **`einen`** Flur.*<br>• *Es **hat** **`einen`** Fernseher, **`einen`** Tisch und **`einen`** Stuhl.* |

---

### HỌC PHẦN 3: PHÂN TÍCH NGỮ PHÁP BỨC THƯ CỦA JULIA GỬI CLAUDIA (THEO SÁT BẢNG VIẾT)

> **Văn bản chuẩn trên bảng:**
> *"Liebe Claudia,*
> *wir haben* **`ein`** *Haus. Unser Haus ist sehr alt und hat 5 Zimmer. Oben gibt es* **`einen`** *Balkon. Das Wohnzimmer ist groß, aber ich finde* **`die`** *Küche* **`zu klein`***. Das Haus hat* **`einen`** *Flur. Er ist lang und dunkel. Wir haben auch* **`einen`** *Garten. Ich finde* **`den`** *Garten sehr schön.*
> *Viele Grüße*
> *Julia"*

* **Bản dịch tiếng Việt chuẩn**:
  *"Claudia thân mến,*
  *Chúng mình có một ngôi nhà. Ngôi nhà của chúng mình rất cũ và có 5 phòng. Ở tầng trên có một cái ban công. Phòng khách thì rộng, nhưng mình thấy nhà bếp hơi quá nhỏ. Ngôi nhà có một hành lang. Nó dài và tối. Chúng mình cũng có một khu vườn. Mình thấy khu vườn đó rất đẹp.*
  *Thân ái chào bạn,*
  *Julia"*

* **Giải phẫu 6 Điểm Ngữ pháp Đắt giá trong Bức thư**:
  1. **`wir haben ein Haus`** $\rightarrow$ **`Unser Haus ist...`**:
     * Lần đầu tiên nhắc đến ngôi nhà (`das Haus` - giống trung) đứng sau động từ `haben` (Cách 4 - Akkusativ), vì chưa xác định nên dùng mạo từ bất định **`ein Haus`**.
     * Ngay câu sau, ngôi nhà đã xác định và làm chủ ngữ (Cách 1 - Nominativ): dùng mạo từ sở hữu của `wir` là **`Unser Haus`**.
  2. **`Oben gibt es einen Balkon`**:
     * **`oben`**: ở phía trên / tầng trên (trái nghĩa với **`unten`**: ở phía dưới / tầng dưới).
     * Cấu trúc **`es gibt + Akkusativ`** (*có / tồn tại cái gì đó*): Vì `der Balkon` là danh từ giống đực (`der`) và được nhắc đến lần đầu tiên, nên khi đứng sau `gibt es` bắt buộc phải đổi `ein` $\rightarrow$ **`einen Balkon`**!
  3. **`...aber ich finde die Küche zu klein`**:
     * Liên từ **`aber`** (*nhưng*) nối 2 mệnh đề đối lập và giữ nguyên trật tự câu trần thuật (`S + V`).
     * Cấu trúc **`finden + Akkusativ + Tính từ`** (*cảm thấy / đánh giá cái gì như thế nào*): Vì trong nhà chỉ có một căn bếp xác định (`die Küche` - giống cái), ở Akkusativ giữ nguyên là **`die Küche`**.
     * Phó từ **`zu + Tính từ`** (`zu klein` = *quá nhỏ*, `zu teuer` = *quá đắt*, `zu dunkel` = *quá tối*) mang sắc thái phàn nàn vượt mức mong muốn.
  4. **`Das Haus hat einen Flur. Er ist lang und dunkel`**:
     * Câu trước: `der Flur` (hành lang - giống đực) đứng sau `hat` (Akkusativ, nhắc lần đầu) $\rightarrow$ **`einen Flur`**.
     * Câu sau: Đại từ nhân xưng **`Er`** (*nó / anh ấy*) đứng đầu câu làm chủ ngữ (Nominativ) dùng để **thay thế cho danh từ giống đực `der Flur`** vừa nhắc ở câu trước! (Trong tiếng Đức: danh từ `der` thay bằng **`er`**, danh từ `die` thay bằng **`sie`**, danh từ `das` thay bằng **`es`**).
  5. **Sự chuyển đổi kinh điển từ `einen Garten` (lần 1) sang `den Garten` (lần 2)**:
     * Câu 1: *"Wir haben auch **`einen`** Garten."* $\rightarrow$ Khu vườn (`der Garten`) mới được giới thiệu lần đầu tiên sau động từ `haben` $\rightarrow$ dùng mạo từ bất định ở Akkusativ là **`einen Garten`**.
     * Câu 2: *"Ich finde **`den`** Garten sehr schön."* $\rightarrow$ Khu vườn lúc này **đã được xác định** (chính là khu vườn vừa kể ở câu trước!) và đứng sau động từ `finden` (đòi hỏi Akkusativ) $\rightarrow$ dùng mạo từ xác định ở Akkusativ: `der` đổi thành **`den Garten`**!

---

### HỌC PHẦN 4: HỆ THỐNG MẠO TỪ SỞ HỮU (`POSSESSIVARTIKEL`) THEO 9 NGÔI NHÂN XƯNG & 4 GIỐNG

Mạo từ sở hữu (`Possessivartikel`) luôn đứng trước một danh từ để chỉ quyền sở hữu (*của tôi, của bạn, của anh ấy, của chúng tôi...*). Để chia đúng mạo từ sở hữu, người học thực hiện **2 bước**:
* **Bước 1**: Chọn **Gốc sở hữu** tương ứng với **Người sở hữu (Ngôi nhân xưng)**.
* **Bước 2**: Gắn **Đuôi mạo từ** tương ứng với **Giống, Số và Cách của Danh từ đứng ngay sau nó** (quy tắc gắn đuôi **giống hệt 100% như từ phủ định `kein-`**!).

#### 4.1. Bảng Ma Trận Toàn Diện: Mạo Từ Sở Hữu Theo 9 Ngôi Nhân XưngỞ Cách 1 (`Nominativ`)

> ⚠️ **Quy tắc Đuôi ở Cách 1 (`Nominativ`)**:
> * Danh từ theo sau là **Giống Đực (`der`)** hoặc **Giống Trung (`das`)**: **KHÔNG thêm đuôi** (giữ nguyên gốc: *`mein Garten`, `mein Haus`, `unser Garten`, `euer Haus`*).
> * Danh từ theo sau là **Giống Cái (`die`)** hoặc **Số Nhiều (`die Pl.`)**: **Bắt buộc thêm đuôi `-e`** (*`meine Wohnung`, `meine Toiletten`, `unsere Wohnung`, `unsere Kinder`*).
> * 🔥 **ĐẶC BIỆT LƯU Ý NGÔI `ihr` (Các bạn) $\rightarrow$ `euer`**: Khi gốc **`euer`** cộng thêm đuôi **`-e`** (hoặc `-en`), chữ **`e` ở giữa bị lược bỏ** để dễ phát âm:
>   * ~~`euere Wohnung`~~ $\longrightarrow$ **`eure Wohnung`**
>   * ~~`euere Kinder`~~ $\longrightarrow$ **`eure Kinder`**

| STT | Đại từ Nhân xưng (`Personalpronomen`) | Nghĩa của Đại từ | Gốc Sở hữu (`Stamm`) | Nghĩa của Mạo từ Sở hữu | Đi với Giống Đực (`der Garten` - `m`) | Đi với Giống Trung (`das Haus` - `n`) | Đi với Giống Cái (`die Wohnung` - `f`) *(Thêm `-e`)* | Đi với Số Nhiều (`die Toiletten` - `Pl`) *(Thêm `-e`)* |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **`ich`** | tôi | **`mein`** | của tôi | **`mein`** `Garten` | **`mein`** `Haus` | **`meine`** `Wohnung` | **`meine`** `Toiletten` |
| 2 | **`du`** | bạn | **`dein`** | của bạn | **`dein`** `Garten` | **`dein`** `Haus` | **`deine`** `Wohnung` | **`deine`** `Toiletten` |
| 3 | **`er`** | anh ấy | **`sein`** | của anh ấy | **`sein`** `Garten` | **`sein`** `Haus` | **`seine`** `Wohnung` | **`seine`** `Toiletten` |
| 4 | **`es`** | nó | **`sein`** | của nó | **`sein`** `Garten` | **`sein`** `Haus` | **`seine`** `Wohnung` | **`seine`** `Toiletten` |
| 5 | **`sie`** *(số ít)* | cô ấy | **`ihr`** *(viết thường)* | của cô ấy | **`ihr`** `Garten` | **`ihr`** `Haus` | **`ihre`** `Wohnung` | **`ihre`** `Toiletten` |
| 6 | **`wir`** | chúng tôi / ta | **`unser`** | của chúng tôi | **`unser`** `Garten` | **`unser`** `Haus` | **`unsere`** `Wohnung` | **`unsere`** `Toiletten` |
| 7 | **`ihr`** *(số nhiều)* | các bạn | **`euer`** | của các bạn | **`euer`** `Garten` | **`euer`** `Haus` | 🔥 **`eure`** `Wohnung` *(bỏ `e`)* | 🔥 **`eure`** `Toiletten` *(bỏ `e`)* |
| 8 | **`sie`** *(số nhiều)* | họ / chúng | **`ihr`** *(viết thường)* | của họ | **`ihr`** `Garten` | **`ihr`** `Haus` | **`ihre`** `Wohnung` | **`ihre`** `Toiletten` |
| 9 | **`Sie`** *(trang trọng)* | Ngài / Các ngài | **`Ihr`** *(VIẾT HOA!)* | của Ngài | **`Ihr`** `Garten` | **`Ihr`** `Haus` | **`Ihre`** `Wohnung` | **`Ihre`** `Toiletten` |

---

#### 4.2. Bảng Ma Trận Mở Rộng: Mạo Từ Sở Hữu Ở Cách 4 (`Akkusativ`) Theo 9 Ngôi Nhân Xưng
Khi cụm danh từ có mạo từ sở hữu đứng ở vị trí **Tân ngữ trực tiếp (`Akkusativ`)** (sau `haben, finden, brauchen, suchen, kaufen, sehen...`), **chỉ duy nhất cột Giống Đực (`Maskulinum - der`) thêm đuôi `-en`**, còn lại giữ nguyên như bảng `Nominativ`:

| Ngôi Nhân xưng | Gốc Sở hữu | Giống Đực ở `Akkusativ` (`den Garten` - **`+en`**) | Giống Trung ở `Akkusativ` (`das Haus` - *Giữ nguyên*) | Giống Cái ở `Akkusativ` (`die Wohnung` - *Giữ nguyên*) | Số Nhiều ở `Akkusativ` (`die Toiletten` - *Giữ nguyên*) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`ich`** (tôi) | `mein-` | 🔴 **`meinen`** `Garten` | **`mein`** `Haus` | **`meine`** `Wohnung` | **`meine`** `Toiletten` |
| **`du`** (bạn) | `dein-` | 🔴 **`deinen`** `Garten` | **`dein`** `Haus` | **`deine`** `Wohnung` | **`deine`** `Toiletten` |
| **`er / es`** (anh ấy / nó) | `sein-` | 🔴 **`seinen`** `Garten` | **`sein`** `Haus` | **`seine`** `Wohnung` | **`seine`** `Toiletten` |
| **`sie`** (cô ấy) | `ihr-` | 🔴 **`ihren`** `Garten` | **`ihr`** `Haus` | **`ihre`** `Wohnung` | **`ihre`** `Toiletten` |
| **`wir`** (chúng tôi) | `unser-` | 🔴 **`unseren`** `Garten` | **`unser`** `Haus` | **`unsere`** `Wohnung` | **`unsere`** `Toiletten` |
| **`ihr`** (các bạn) | `euer-` | 🔴 **`euren`** `Garten` *(bỏ `e`)* | **`euer`** `Haus` | **`eure`** `Wohnung` *(bỏ `e`)* | **`eure`** `Toiletten` *(bỏ `e`)* |
| **`sie`** (họ) | `ihr-` | 🔴 **`ihren`** `Garten` | **`ihr`** `Haus` | **`ihre`** `Wohnung` | **`ihre`** `Toiletten` |
| **`Sie`** (Ngài) | `Ihr-` | 🔴 **`Ihren`** `Garten` | **`Ihr`** `Haus` | **`Ihre`** `Wohnung` | **`Ihre`** `Toiletten` |

---

#### 4.3. Phân Tích 4 Tình Huống Thực Hành Mạo Từ Sở Hữu Trên Bảng
1. **Tình huống 1 (Xưng hô thân mật với 1 người `Anna` = `du`, danh từ giống cái `die Tasche`)**:
   * Hỏi: *Ist das ~~dein~~ / **`deine`** Tasche, Anna?* (Vì `die Tasche` mang giống cái `die` $\rightarrow$ phải có đuôi `-e`: **`deine`**).
   * Đáp: *Ja, das ist ~~mein~~ / **`meine`** Tasche.* (Của tôi + `die Tasche` $\rightarrow$ **`meine`**).
2. **Tình huống 2 (Xưng hô lịch sự với `Herr Müller` = `Sie`, danh từ giống trung `das Auto`)**:
   * Hỏi: *Ist das **`Ihr`** / ~~Ihre~~ Auto, Herr Müller?* (Vì `das Auto` mang giống trung `das` $\rightarrow$ không thêm đuôi `-e`: **`Ihr Auto`**).
   * Đáp: *Ja, das ist **`mein`** / ~~meine~~ Auto.* (Của tôi + `das Auto` $\rightarrow$ **`mein Auto`**).
3. **Tình huống 3 (Hỏi 2 người `Maria und Lukas` = `ihr` [các bạn], danh từ số nhiều `die Kinder`)**:
   * Hỏi: *Sind das ~~euer~~ / **`eure`** Kinder, Maria und Lukas?* (Vì `die Kinder` là số nhiều + nói chuyện với 2 người `ihr` $\rightarrow$ `euer` + `-e` lược bỏ `e` thành **`eure Kinder`**).
   * Đáp: *Ja, das sind ~~unser~~ / **`unsere`** Kinder.* (Hai người trả lời thay cho `wir` [chúng tôi] + `die Kinder` số nhiều $\rightarrow$ **`unsere Kinder`**).
4. **Tình huống 4 (Phân biệt `sein` [của anh ấy] vs. `ihr` [của cô ấy] dựa vào chủ sở hữu `Lena`)**:
   * Hỏi: *Ist das **`dein`** / ~~deine~~ Buch, Tina?* (`das Buch` giống trung $\rightarrow$ **`dein Buch`**).
   * Đáp: *Nein, das ist das Buch von Lena. Es ist **`ihr`** / ~~sein~~ Buch.* (Vì quyển sách thuộc về **Lena** = nữ giới [`sie` - cô ấy], nên chọn gốc **`ihr`**, và vì `das Buch` là giống trung nên không thêm đuôi `-e` $\rightarrow$ **`ihr Buch`**!).

---

### HỌC PHẦN 5: TỪ VỰNG ĐỒ NỘI THẤT (`MÖBEL & EINRICHTUNG`) & TÍNH TỪ ĐỐI LẬP (`ADJEKTIVE & GEGENTEILE`)

#### 5.1. Bảng Danh Từ Đồ Nội Thất Phân Loại Theo 3 Giống (`der / die / das`) Kèm Dạng `Akkusativ`

| Phân nhóm Giống | Danh từ Số ít (`Nominativ`) | Dạng Số nhiều (`Plural`) | Nghĩa tiếng Việt | Khi đứng sau `haben / es gibt` (`Akkusativ`) | Giải thích & Từ ghép mở rộng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 🔵 **Giống Đực (`der`)** | **`der Schrank`** | `die Schränke` | Cái tủ *(tủ quần áo/tủ đồ)* | **`einen Schrank`** / `den Schrank` | Số nhiều thêm Umlaut `a -> ä` và `-e`. |
| 🔵 **Giống Đực (`der`)** | **`der Kühlschrank`** | `die Kühlschränke` | Tủ lạnh | **`einen Kühlschrank`** | Ghép `kühl` (mát/lạnh) + `der Schrank` (tủ). |
| 🔵 **Giống Đực (`der`)** | **`der Tisch`** | `die Tische` | Cái bàn | **`einen Tisch`** / `den Tisch` | `der Schreibtisch` (bàn làm việc), `der Esstisch` (bàn ăn). |
| 🔵 **Giống Đực (`der`)** | **`der Stuhl`** | `die Stühle` | Cái ghế | **`einen Stuhl`** / `den Stuhl` | Số nhiều thêm Umlaut `u -> ü` và `-e`. |
| 🔵 **Giống Đực (`der`)** | **`der Teppich`** | `die Teppiche` | Tấm thảm | **`einen Teppich`** / `den Teppich` | Hậu tố `-ich` luôn mang giống đực (`der`). |
| 🔵 **Giống Đực (`der`)** | **`der Spiegel`** | `die Spiegel` | Cái gương | **`einen Spiegel`** / `den Spiegel` | Danh từ tận cùng bằng `-el`, số nhiều giữ nguyên. |
| 🔵 **Giống Đực (`der`)** | **`der Fernseher`** | `die Fernseher` | Tivi (Máy truyền hình) | **`einen Fernseher`** / `den Fernseher` | Tận cùng bằng `-er` (thiết bị), số nhiều giữ nguyên. |
| 🔴 **Giống Cái (`die`)** | **`die Lampe`** | `die Lampen` | Cái đèn | **`eine Lampe`** / `die Lampe` | Tận cùng bằng `-e` $\rightarrow$ giống cái, số nhiều thêm `-n`. |
| 🔴 **Giống Cái (`die`)** | **`die Spüle`** | `die Spülen` | Bồn rửa bát | **`eine Spüle`** / `die Spüle` | Tận cùng bằng `-e` $\rightarrow$ giống cái, số nhiều thêm `-n`. |
| 🟢 **Giống Trung (`das`)** | **`das Bett`** | `die Betten` | Cái giường | **`ein Bett`** / `das Bett` | Ngoại lệ số nhiều của giống trung thêm `-en`: `die Betten`. |
| 🟢 **Giống Trung (`das`)** | **`das Regal`** | `die Regale` | Cái giá / Cái kệ | **`ein Regal`** / `das Regal` | Số nhiều thêm `-e` (`die Regale`). |
| 🟢 **Giống Trung (`das`)** | **`das Bücherregal`** | `die Bücherregale` | Giá sách / Kệ sách | **`ein Bücherregal`** | Ghép `die Bücher` (những cuốn sách) + `das Regal` (cái giá). |

---

#### 5.2. Bảng 9 Cặp Tính Từ Đối Lập (`Adjektive & Gegenteile`) Miêu Tả Nhà Cửa & Nội Thất

> 💡 **Quy tắc Ngữ pháp với Tính từ vị ngữ (`Prädikative Adjektive`)**: Khi tính từ đứng ở cuối câu sau động từ **`sein`** (*ist / sind*) hoặc **`finden`** (*Ich finde den Garten **schön***), tính từ **luôn giữ nguyên mẫu, KHÔNG chia đuôi**!

| STT | Tính từ Tích cực / Đặc tính 1 | Nghĩa tiếng Việt | $><$ | Tính từ Đối lập (`Gegenteil`) | Nghĩa tiếng Việt | Câu ví dụ thực tế trong bài |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- |
| 1 | **`hell`** | sáng sủa | $><$ | **`dunkel`** | tối tăm | *Mein Arbeitszimmer ist klein, aber **hell**. Der Flur ist **dunkel**.* |
| 2 | **`groß`** | to, lớn, rộng | $><$ | **`klein`** | nhỏ, hẹp | *Das Wohnzimmer ist **groß**, aber die Küche ist zu **klein**.* |
| 3 | **`leise`** | khẽ, yên tĩnh | $><$ | **`laut`** | ồn ào, ầm ĩ | *Die Straße ist **laut**, aber mein Schlafzimmer ist **leise** (ruhig).* |
| 4 | **`lang`** | dài | $><$ | **`kurz`** | ngắn | *Das Haus hat einen Flur. Er ist **lang** und dunkel.* |
| 5 | **`neu`** | mới | $><$ | **`alt`** | cũ, cổ, già | *Unser Haus ist sehr **alt**, aber die Möbel sind **neu**.* |
| 6 | **`billig`** *(hoặc `günstig`)* | rẻ (bình dân) | $><$ | **`teuer`** | đắt đỏ | *Die Wohnung in Berlin ist **teuer**, das Zimmer hier ist **billig**.* |
| 7 | **`schön`** | đẹp | $><$ | **`hässlich`** | xấu xí | *Ich finde den Garten sehr **schön**. Der alte Schrank ist **hässlich**.* |
| 8 | **`modern`** | hiện đại | $><$ | *(altmodisch)* | *(lỗi thời / cổ điển)* | *Mein Wohnzimmer ist hell und **modern**.* |
| 9 | **`gemütlich`** | ấm cúng, thoải mái | $><$ | *(ungemütlich)* | *(không thoải mái)* | *Mein Schlafzimmer ist **gemütlich** und hat ein Bett.* |

---

### HỌC PHẦN 6: PHÂN TÍCH BÀI DỊCH MẪU MIÊU TẢ NGÔI NHÀ CỦA TÔI (THEO SÁT BẢNG VIẾT)

Đây là bài tập tổng hợp toàn bộ kiến thức của Bài 4 (kết hợp **Mạo từ sở hữu ở `Nominativ`**, động từ **`sein` + tính từ**, và động từ **`haben` + `Akkusativ`**):

| Câu số | Câu Tiếng Việt trên bảng | Bản dịch Tiếng Đức chuẩn xác | Phân tích Ngữ pháp (`Nominativ` vs. `Akkusativ` & Sở hữu) |
| :---: | :--- | :--- | :--- |
| **1** | *"Tôi có một ngôi nhà. Ngôi nhà của tôi có 5 phòng: 1 phòng khách, 2 phòng ngủ, 1 phòng làm việc và 1 phòng bếp."* | **`Ich habe ein Haus. Mein Haus hat 5 Zimmer: ein Wohnzimmer, 2 Schlafzimmer, ein Arbeitszimmer und eine Küche.`** | • `ein Haus`: `das Haus` đứng sau `habe` (Akkusativ, giống trung) $\rightarrow$ `ein Haus`.<br>• `Mein Haus`: Chủ ngữ (Nominativ, giống trung) $\rightarrow$ `Mein Haus`.<br>• Các phòng `-zimmer` đều là `das` $\rightarrow$ `ein Wohnzimmer`, `ein Arbeitszimmer`, số nhiều `2 Schlafzimmer` (giữ nguyên).<br>• `die Küche` (giống cái) $\rightarrow$ **`eine Küche`**. |
| **2** | *"Phòng khách của tôi thì sáng và hiện đại. Nó có 1 Tivi và 1 giá sách."* | **`Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher und ein Bücherregal.`** | • `Mein Wohnzimmer`: Chủ ngữ giống trung (`das`) $\rightarrow$ `Mein`.<br>• Đại từ **`Es`** thay cho `das Wohnzimmer`.<br>• 🔥 `der Fernseher` (giống đực) đứng sau `hat` (Akkusativ) $\rightarrow$ bắt buộc đổi `ein` thành **`einen Fernseher`**!<br>• `das Bücherregal` (giống trung) đứng sau `hat` $\rightarrow$ giữ nguyên **`ein Bücherregal`**. |
| **3** | *"Phòng ngủ của tôi thì ấm cúng và có 1 giường."* | **`Mein Schlafzimmer ist gemütlich und hat ein Bett.`** | • Lược bỏ chủ ngữ ở vế sau sau chữ `und` (cùng chủ ngữ `Mein Schlafzimmer`).<br>• `das Bett` (giống trung) đứng sau `hat` (Akkusativ) $\rightarrow$ **`ein Bett`**. |
| **4** | *"Phòng làm việc của tôi thì nhỏ nhưng sáng. Nó có 1 bàn và 1 ghế."* | **`Mein Arbeitszimmer ist klein, aber hell. Es hat einen Tisch und einen Stuhl.`** | • Liên từ `aber` (*nhưng*) nối 2 tính từ trái ngược `klein, aber hell`.<br>• 🔥 Cả `der Tisch` (cái bàn) và `der Stuhl` (cái ghế) đều là **giống đực (`der`)** nên khi đứng sau `hat` (Akkusativ) đều phải biến đổi thành **`einen Tisch und einen Stuhl`**! |
| **5** | *"Phòng bếp của tôi thì nhỏ và đẹp."* | **`Meine Küche ist klein und schön.`** | • 🔥 Vì `die Küche` là danh từ **giống cái (`die`)**, nên mạo từ sở hữu đứng đầu câu làm chủ ngữ bắt buộc phải thêm đuôi **`-e`** $\rightarrow$ **`Meine Küche`**! |

---

## PHẦN 3: MỞ RỘNG DỮ LIỆU CHO 2 TAB TRA CỨU (`static/js/lexikon_db.js` & `static/js/verbs_db.js`)

### 3.1. Bổ sung vào `static/js/verbs_db.js` (Tab `"📖 Chia động từ"`)
Giữ nguyên toàn bộ các động từ hiện có và bổ sung các động từ đi với Cách 4 (`Akkusativ`) của Bài 4:
* **`finden`** (gốc `-d` $\rightarrow$ thêm `-e-`: `ich finde, du findest, er/sie/es findet, wir finden, ihr findet, sie/Sie finden`): tìm thấy; cảm thấy/đánh giá (+ `Akkusativ` + tính từ: *Ich finde den Garten sehr schön*).
* **`suchen`** (quy tắc: `suche, suchst, sucht, suchen, sucht, suchen`): tìm kiếm (+ `Akkusativ`: *Wir suchen eine Wohnung*).
* **`brauchen`** (quy tắc: `brauche, brauchst, braucht, brauchen, braucht, brauchen`): cần (+ `Akkusativ`: *Ich brauche einen Tisch und einen Stuhl*).
* **`kaufen`** (quy tắc: `kaufe, kaufst, kauft, kaufen, kauft, kaufen`): mua (+ `Akkusativ`: *Er kauft einen Kühlschrank*).

### 3.2. Bổ sung vào `static/js/lexikon_db.js` (Tab `"🏷️ Từ vựng & Giống"`)
1. **Thêm 2 nút lọc chủ đề mới** trên thanh Filter Pills của Tab `"🏷️ Từ vựng & Giống"`:
   * `🏠 Nhà ở & Phòng ốc (Menschen & Häuser)`
   * `🛋️ Nội thất & Đồ đạc (Möbel & Einrichtung)`
2. **Nạp đầy đủ 26 danh từ Nhà ở & Nội thất của Bài 4** vào `GERMAN_LEXIKON_DB`, mỗi thẻ hiển thị rõ:
   * Mạo từ gốc (`der / die / das`) + Dạng số nhiều (`die Gärten, die Häuser, die Schränke, die Stühle...`).
   * **Hiển thị thêm dòng `Cách 4 (Akkusativ)` ngay trên thẻ từ vựng**: Ví dụ với `der Garten` hiển thị rõ: `Nominativ: der / ein / kein Garten` $\rightarrow$ **`Akkusativ: den / einen / keinen Garten`** để người học tra cứu cả giống lẫn cách biến đổi sang Akkusativ tại một nơi duy nhất!
3. **Bổ sung Bảng Tra Cứu Nhanh Mạo Từ (`Nominativ / Akkusativ / Possessivartikel`)** ngay phía trên hoặc dưới thanh tìm kiếm của Tab `"🏷️ Từ vựng & Giống"` (có nút bật/tắt `📊 Xem Bảng Mạo Từ & Sở Hữu`) để bất cứ lúc nào làm bài tập người học cũng có thể bấm mở bảng ma trận `der/den`, `ein/einen`, `mein/dein/sein/ihr/unser/euer/Ihr` ra đối chiếu ngay lập tức.

---

## PHẦN 4: KHO 50 BÀI TẬP NGỮ PHÁP CHUYÊN SÂU BÀI 4 & 5 CHẾ ĐỘ RANDOM ĐỔI ĐỀ TỰ ĐỘNG

Trong tệp `lessons/a1/seed_a1_b4.py`, nạp **đúng 50 câu hỏi** tập trung xoáy sâu vào ngữ pháp và từ vựng của Bài 4:

1. **Dạng 1 – Trắc nghiệm Ngữ pháp & Từ vựng (`trac_nghiem` – 12 câu)**:
   * Phân biệt `Nominativ` (`der/ein/kein`) và `Akkusativ` (`den/einen/keinen`) sau các động từ `sein` vs. `haben / finden / es gibt`.
   * Chọn đúng Mạo từ sở hữu (`mein/meine`, `dein/deine`, `sein/ihr`, `unser/unsere`, `euer/eure`, `Ihr/Ihre`) ở cả `Nominativ` và `Akkusativ`.
   * Nhận diện giống của danh từ nhà ở, phòng ốc (`-zimmer` luôn là `das`) và đồ nội thất (`der Fernseher, der Kühlschrank, der Spiegel, der Teppich, die Spüle, das Bücherregal`) cũng như cặp tính từ trái nghĩa (`hell >< dunkel`, `laut >< leise`, `teuer >< billig`, `schön >< hässlich`).
2. **Dạng 2 – Điền khuyết Ngữ pháp Chuyên sâu (`dien_khuyet` – 12 câu)**:
   * Điền mạo từ `ein / eine / einen`, `kein / keine / keinen`, `der / die / das / den` vào bức thư của Julia gửi Claudia (*"Wir haben ___ Haus... Oben gibt es ___ Balkon... Ich finde ___ Küche zu klein... Das Haus hat ___ Flur... Wir haben auch ___ Garten. Ich finde ___ Garten sehr schön."*).
   * Điền mạo từ sở hữu chính xác vào 4 cặp hội thoại trên bảng (*Anna – deine/meine Tasche; Herr Müller – Ihr/mein Auto; Maria und Lukas – eure/unsere Kinder; Tina & Lena – dein/ihr Buch*) và các câu mở rộng ở `Akkusativ` (*meinen Fernseher, euren Garten, ihren Tisch*).
3. **Dạng 3 – Dịch 2 chiều Việt ⇄ Đức (`dich` – 8 câu)**:
   * Dịch trọn vẹn từng câu trong đoạn văn 5 câu miêu tả ngôi nhà trên bảng (*"Tôi có một ngôi nhà. Ngôi nhà của tôi có 5 phòng..."*, *"Phòng khách của tôi thì sáng và hiện đại. Nó có 1 Tivi và 1 giá sách."*, *"Phòng ngủ của tôi thì ấm cúng và có 1 giường."*, *"Phòng làm việc của tôi thì nhỏ nhưng sáng. Nó có 1 bàn và 1 ghế."*, *"Phòng bếp của tôi thì nhỏ và đẹp."*).
4. **Dạng 4 – Luyện Nghe 1.0x & 0.65x (`nghe` – 5 câu)**:
   * Nghe các câu miêu tả căn hộ, nội thất và bức thư của Julia để điền chính xác mạo từ `einen / den / meine / eure` và tên đồ vật.
5. **Dạng 5 – Luyện Nói & Phát âm (`noi` – 4 câu)**:
   * Luyện đọc chuẩn các câu chứa `Akkusativ` và `Possessivartikel`: *"Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher und ein Bücherregal."*, *"Sind das eure Kinder, Maria und Lukas? – Ja, das sind unsere Kinder."*, *"Das Haus hat einen Flur. Er ist lang und dunkel."*, *"Wir haben auch einen Garten. Ich finde den Garten sehr schön."*
6. **Dạng 6 – Đọc hiểu Bức thư của Julia (`doc` – 4 câu)**:
   * Đọc bức thư của Julia gửi Claudia và trả lời các câu hỏi kiểm tra chi tiết (*Ngôi nhà của Julia cũ hay mới và có mấy phòng? Ở tầng trên có gì? Julia thấy phòng bếp và khu vườn như thế nào? Hành lang được miêu tả ra sao?*).
7. **Dạng 7 – Viết lại câu & Biến đổi Ngữ pháp (`viet` – 5 câu)**:
   * Chuyển đổi cụm danh từ từ `Nominativ` (`Das ist ein... / Das ist der...`) sang câu có động từ `haben / finden / es gibt` ở `Akkusativ` (`Wir haben einen... / Ich finde den...`).
   * Thay thế cụm `das/die/der ... von [Chủ sở hữu]` bằng Mạo từ sở hữu tương ứng (*das Buch von Lena $\rightarrow$ ihr Buch; das Auto von Peter $\rightarrow$ sein Auto; die Kinder von Maria und Lukas $\rightarrow$ ihre/eure Kinder*).

### 5 Chế độ Random Đổi Đề Ngữ Pháp Tự Động cho Bài 4 (`templates/index.html`)
Bổ sung vào hàm `randomizeDynamicExercises()` trên Frontend để mỗi lần người học bấm `🔄 Đổi đề khác` hoặc mở lại bài tập, hệ thống tự động sinh câu hỏi mới:

1. **Random Phân biệt `Nominativ` vs. `Akkusativ` (`dynamic_nom_akk_quiz`)**:
   * Ngân hàng gồm 22 danh từ Nhà ở & Nội thất (*der Garten, der Balkon, der Flur, der Keller, der Schrank, der Kühlschrank, der Tisch, der Stuhl, der Teppich, der Spiegel, der Fernseher, die Wohnung, die Küche, die Garage, die Lampe, die Spüle, das Haus, das Zimmer, das Wohnzimmer, das Bett, das Bücherregal...*).
   * Tự động đổi động từ giữa nhóm **Cách 1 (`Das ist ___ ...`)** và nhóm **Cách 4 (`Wir haben ___ ... / Oben gibt es ___ ... / Ich finde ___ ... schön`)** để người học chia đúng `der/den`, `ein/eine/einen`, `kein/keine/keinen`.
2. **Random Ma trận Mạo từ sở hữu theo 9 Ngôi (`dynamic_possessiv_quiz`)**:
   * Tự động bắt cặp ngẫu nhiên 1 trong 9 chủ sở hữu (*ich, du, Anna [du], Herr Müller [Sie], Maria und Lukas [ihr], Lena [sie - cô ấy], Peter [er - anh ấy], wir, die Eltern [sie - họ]*) với 1 danh từ bất kỳ ở `Nominativ` hoặc `Akkusativ` để người học điền đúng `mein/meine/meinen`, `dein/deine/deinen`, `sein/seine/seinen`, `ihr/ihre/ihren`, `unser/unsere/unseren`, `euer/eure/euren`, `Ihr/Ihre/Ihren`.
3. **Random Tính từ Đối lập Miêu tả Nhà cửa (`dynamic_adjective_antonym_quiz`)**:
   * Tự động tráo đổi giữa 9 cặp tính từ trái nghĩa (*hell $\leftrightarrow$ dunkel, groß $\leftrightarrow$ klein, laut $\leftrightarrow$ leise, lang $\leftrightarrow$ kurz, alt $\leftrightarrow$ neu, teuer $\leftrightarrow$ billig, schön $\leftrightarrow$ hässlich, modern, gemütlich*) trong các ngữ cảnh miêu tả phòng ốc.
4. **Random Thay thế Đại từ Nhân xưng theo Giống của Đồ vật (`dynamic_pronoun_replacement_quiz`)**:
   * Tự động tạo câu dạng: *"Das Haus hat einen Flur / eine Küche / ein Wohnzimmer. `___` (`Er / Sie / Es`) ist..."* để rèn phản xạ thay thế danh từ `der` bằng `er`, `die` bằng `sie`, `das` bằng `es`.
5. **Random Dịch câu Miêu tả Phòng & Nội thất (`dynamic_house_translation_quiz`)**:
   * Tự động kết hợp ngẫu nhiên `[Phòng của ai đó]` + `[2 Tính từ]` + `[Có 2 đồ nội thất ở Akkusativ]` để người học luyện dịch trọn vẹn câu tiếng Đức chuẩn ngữ pháp.

---

## PHẦN 5: HƯỚNG DẪN THỰC THI DÀNH CHO ANTIGRAVITY IDE

1. Tạo tệp **`lessons/a1/seed_a1_b4.py`** và chạy lệnh `python3 lessons/a1/seed_a1_b4.py` để nạp Bài 4 vào cơ sở dữ liệu `deutsch_meister.db` (đảm bảo giữ nguyên Bài 1 P1, Bài 1 P2, Bài 2 và Bài 3).
2. Cập nhật **`static/js/lexikon_db.js`**, **`static/js/verbs_db.js`** và **`templates/index.html`** để bổ sung toàn bộ từ vựng Bài 4, bảng ma trận tra cứu nhanh Mạo từ (`Nominativ / Akkusativ / Possessivartikel`) và 5 chế độ random bài tập ngữ pháp của Bài 4.
3. Kiểm tra cú pháp Python & JS, sau đó chạy `git add . && git commit -m "Add Lesson 4 (Menschen und Haeuser, Nominativ/Akkusativ, Possessivartikel) with full matrix tables and 50 grammar exercises" && git push` để cập nhật lên trang web Public.