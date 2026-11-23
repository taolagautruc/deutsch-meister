# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 13 (A1) "ÔN TẬP TỔNG HỢP A1 — ĐỘNG TỪ BẤT QUY TẮC, W-FRAGEN & GIAO TIẾP QUÁN CAFE" — BỘ DỮ LIỆU NGUỒN CHUẨN & 125 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (Bài 1 → Bài 12), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của Bài 13 gồm: **(1)** tạo mới hoàn toàn **Bài 13 (`lessons/a1/seed_a1_b13.py`)** ở vị trí **`lesson_order = 14`** của cấp độ **A1**; **(2)** *cộng dồn* động từ và từ vựng mới vào 2 chuyên mục tra cứu; **(3)** *mở rộng* 25 câu hỏi Đấu trường; **(4)** viết và chạy kịch bản kiểm thử toàn diện `verify_lesson13_qa.py`.
> * **Quy tắc chống phá vỡ giao diện cũ (`Zero-Regression for UI`)**: 18 dạng bài của Bài 13 phải kế thừa trọn vẹn 18 component UI đã có từ các bài trước (như ảnh giao diện đã mô tả). Không tự ý chế ra UI mới làm hỏng code cũ.
>
> ---
>
> ### 🎯 2. PHẠM VI KIẾN THỨC & SỰ SÁNG TẠO ĐA DẠNG (`A1 REVIEW SCOPE & CREATIVITY`)
> Bài 13 là bài ôn tập bản lề, trọng tâm gồm 3 phần (được đẩy mạnh tư duy từ bảng giảng cơ bản thành các tình huống đa dạng):
> 1. **Chia động từ bất quy tắc (Vowel Shift)**: Sự biến đổi nguyên âm (`a → ä`, `e → i`, `e → ie`) CHỈ XẢY RA ở ngôi `du` và `er/sie/es`. *Cấm kỵ:* Tuyệt đối không biến âm ở ngôi `ihr` (các bạn).
> 2. **Động từ có quy tắc & Gốc ngoại lệ**: Các động từ như `reisen, heißen` (gốc s/ß) chỉ thêm `-t` ở ngôi `du`.
> 3. **W-Fragen & Giao tiếp (Kaffee oder Tee)**: Hỏi thông tin cá nhân (`Wie, Woher, Wo, Was, Wann`) và cách đặt món, hỏi chỗ ngồi trong quán Cafe.
>
> ---
>
> ### 🔍 3. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI (`ZERO-BUG QA PROTOCOL`)
> 1. **Dịch sai nghĩa / Lạc ngữ cảnh**: Dịch tiếng Việt phải bám sát câu tiếng Đức ĐÃ HOÀN CHỈNH. Đổi ngôi `ihr` phải dịch đúng "các bạn", `Sie` dịch "Ngài/Ông/Bà".
> 2. **Giải thích phải chứa đáp án**: Phần `explanation` BẮT BUỘC chứa chuỗi đáp án đúng và phân tích rõ logic (VD: *"Vì chủ ngữ là 'Das Mädchen' (es) nên động từ 'lesen' biến âm 'e' thành 'ie' → Đáp án: liest"*).
> 3. **Voice Sạch (`de-DE`)**: Voice `🔊` truyền chuỗi tiếng Đức chuẩn, loại bỏ dấu điền khuyết `___`, `[1]`.
> 4. **Bẫy Ngôi "ihr"**: Ngôi `ihr` KHÔNG biến âm (`ihr fahrt, ihr schlaft, ihr lest`). Dạng bài "Tìm lỗi sai" sẽ đánh mạnh vào bẫy này.

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN TAB TRA CỨU ĐỘNG TỪ & TỪ VỰNG

Chỉ bổ sung các từ **chưa từng xuất hiện** ở Bài 1 → 12. Giữ nguyên toàn bộ dữ liệu cũ.

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Phải đánh nhãn loại động từ nổi bật (`Bất quy tắc e → ie`, `Có quy tắc`, v.v.).

| Động từ (nghĩa) | Loại | Präsens: ich / du / er·sie·es / wir / ihr / sie·Sie | Ví dụ (`🔊 de-DE`) & Dịch (Sáng tạo mới) |
| :--- | :--- | :--- | :--- |
| **lesen** *(đọc)* | Bất quy tắc `e → ie` | lese / **liest** / **liest** / lesen / lest / lesen | *„Jeden Abend liest mein Großvater die Zeitung.“* — Mỗi tối ông tôi đều đọc báo. |
| **fahren** *(lái xe, đi)* | Bất quy tắc `a → ä` | fahre / **fährst** / **fährt** / fahren / fahrt / fahren | *„Fährst du am Wochenende mit dem Zug nach Berlin?“* — Cuối tuần bạn có đi tàu tới Berlin không? |
| **sprechen** *(nói)* | Bất quy tắc `e → i` | spreche / **sprichst** / **spricht** / sprechen / sprecht / sprechen | *„Die Lehrerin spricht sehr laut und deutlich.“* — Cô giáo nói rất to và rõ ràng. |
| **treffen** *(gặp)* | Bất quy tắc `e → i` | treffe / **triffst** / **trifft** / treffen / trefft / treffen | *„Am Nachmittag trifft Anna ihre Freunde im Café.“* — Vào buổi chiều, Anna gặp bạn bè ở quán cà phê. |
| **essen** *(ăn)* | Bất quy tắc `e → i` | esse / **isst** / **isst** / essen / esst / essen | *„Im Sommer essen die Kinder sehr gern Schokoladeneis.“* — Vào mùa hè, bọn trẻ rất thích ăn kem sô-cô-la. |
| **schlafen** *(ngủ)* | Bất quy tắc `a → ä` | schlafe / **schläfst** / **schläft** / schlafen / schlaft / schlafen | *„Warum schläfst du heute im Hotel und nicht zu Hause?“* — Tại sao hôm nay bạn lại ngủ ở khách sạn mà không phải ở nhà? |
| **geben** *(cho, đưa)* | Bất quy tắc `e → i` | gebe / **gibst** / **gibt** / geben / gebt / geben | *„Hannes und Julia geben dem kleinen Hund das Futter.“* — Hannes và Julia cho chú chó nhỏ ăn thức ăn. |
| **reisen** *(du lịch)* | Có quy tắc (`s`) | reise / **reist** / reist / reisen / reist / reisen | *„Wir reisen diesen Sommer nach Italien und Frankreich.“* — Mùa hè này chúng tôi đi du lịch Ý và Pháp. |
| **grillen** *(nướng BBQ)* | Có quy tắc | grille / grillst / grillt / grillen / grillt / grillen | *„Mein Vater grillt am Sonntag das Fleisch und das Gemüse.“* — Bố tôi nướng thịt và rau củ vào Chủ nhật. |
| **liegen** *(nằm, ở vị trí)* | Có quy tắc | liege / liegst / liegt / liegen / liegt / liegen | *„Das neue Handy liegt auf dem Tisch in der Küche.“* — Chiếc điện thoại mới nằm trên bàn trong bếp. |

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
| Danh từ (Giống) | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :--- | :--- | :--- | :--- | :--- |
| **der Kaffee** | die Kaffees | cà phê | Ich trinke meinen Kaffee immer mit viel Zucker. | Tôi luôn uống cà phê của mình với nhiều đường. |
| **der Tee** | die Tees | trà | Möchtest du eine Tasse schwarzen Tee? | Bạn có muốn một tách trà đen không? |
| **der Zucker** | *(nur Sg.)* | đường | Zwei Kaffee mit Zucker, bitte! | Xin cho hai cà phê có đường! |
| **der Käse** | die Käse | phô mai | Wir kaufen frischen Käse im Supermarkt. | Chúng tôi mua phô mai tươi ở siêu thị. |
| **der Salat** | die Salate | rau xà lách | Ich mache heute Abend einen Tomatensalat. | Tối nay tôi làm một món salad cà chua. |
| **der Hund** | die Hunde | con chó | Der Hund schläft gemütlich auf dem Sofa. | Chú chó đang ngủ thoải mái trên ghế sofa. |
| **der Brief** | die Briefe | bức thư | Anna schreibt einen langen Brief an ihre Oma. | Anna viết một bức thư dài cho bà của cô ấy. |
| **das Eis** | *(nur Sg.)* | kem, đá | Ich esse gern Erdbeereis. | Tôi thích ăn kem dâu. |
| **das Futter** | *(nur Sg.)* | thức ăn thú | Hannes gibt der Katze das Futter. | Hannes cho mèo ăn thức ăn. |
| **das Hotel** | die Hotels | khách sạn | Das Hotelzimmer ist groß und sehr sauber. | Phòng khách sạn lớn và rất sạch sẽ. |
| **das Rathaus** | die Rathäuser | tòa thị chính | Die Touristen besuchen das alte Rathaus. | Du khách tham quan tòa thị chính cũ. |
| **das Gemüse** | *(nur Sg.)* | rau củ | Gemüse ist sehr gesund für den Körper. | Rau củ rất tốt cho sức khỏe cơ thể. |

---

## PHẦN 2: LÝ THUYẾT CHUYÊN SÂU BÀI 13 (UI COMPONENTS)

Trang lý thuyết tuân thủ UI 4 viên thuốc, thẻ mục đánh số và SVG tương tác như hệ thống Bài 11.

### 2.0. CẤU TRÚC HIỂN THỊ
| Thành phần | Nội dung cho Bài 13 |
| :--- | :--- |
| **Huy hiệu đầu** | `DeutschMeister A1 • ÖK A1 • Verben & W-Fragen (Bài 13)` |
| **Tiêu đề lớn** | `Ôn tập A1: Động từ bất quy tắc, W-Fragen & Giao tiếp quán Cafe` |
| **Mô tả ngắn** | `Hệ thống hóa toàn bộ quy tắc chia động từ mạnh (biến đổi nguyên âm a→ä, e→i, e→ie), phân biệt đại từ nhân xưng. Nắm vững nghệ thuật đặt câu hỏi W-Fragen và thực hành hội thoại gọi món tại quán Cafe.` |
| **4 Viên thuốc** | `🔥 Bất quy tắc (a→ä, e→i, e→ie)` · `📝 Động từ Có quy tắc` · `❓ W-Fragen (Wie, Wo, Woher)` · `☕ Hội thoại Cafe` |
| **Sơ đồ SVG** | `V1`: Cỗ máy biến âm (Mục 2.2) · `V2`: Bản đồ W-Fragen & Giới từ (Mục 2.3) |
| **Tab bài tập** | Nhãn **`Phần 2: Bài tập (Đủ 18 Dạng)`** |

### HỌC PHẦN 1: HỆ THỐNG ĐẠI TỪ NHÂN XƯNG & TRỢ ĐỘNG TỪ `SEIN/HABEN`
* **Số ít**: `ich` (tôi), `du` (bạn - thân mật), `er/sie/es` (anh ấy/cô ấy/nó).
* **Số nhiều**: `wir` (chúng ta), `ihr` (các bạn - thân mật số nhiều), `sie` (họ), `Sie` (Ngài/Các ngài - trang trọng).
* ⚠️ **Khung Vàng Cảnh Báo**: Phân biệt 3 chữ `sie` (cô ấy - động từ chia số ít `-t`), `sie` (họ - động từ chia nguyên thể `-en`) và `Sie` (Ngài - viết hoa chữ S).

### HỌC PHẦN 2: 🔥 ĐỘNG TỪ BẤT QUY TẮC (BIẾN ÂM VOWEL-SHIFT)
> **QUY TẮC VÀNG**: Biến âm CHỈ xảy ra ở ngôi `du` và `er/sie/es`. Ngôi `ihr` (các bạn) KHÔNG BAO GIỜ biến âm.
* **Nhóm `a → ä`**: `fahren` (du fährst, er fährt), `schlafen` (du schläfst, er schläft).
* **Nhóm `e → i`**: `sprechen` (du sprichst, er spricht), `treffen` (du triffst, er trifft), `essen` (du isst, er isst), `geben` (du gibst, er gibt).
* **Nhóm `e → ie`**: `lesen` (du liest, er liest).
* ⚙️ **Sơ đồ V1 (Cỗ Máy Chia Động Từ)**: UI có Dropdown chọn 7 động từ trên. Bên dưới là 6 bóng đèn (6 ngôi). Bấm vào `du` hoặc `er/sie/es` -> Bóng đèn chớp đỏ, nguyên âm nhảy hiệu ứng biến đổi (Vd: a thành ä). Bấm vào `ihr` -> Bóng đèn xanh, giữ nguyên âm gốc.

### HỌC PHẦN 3: ❓ TỪ ĐỂ HỎI (W-FRAGEN) & QUY TẮC GIỚI TỪ
* **Hỏi Tên (`Wie`)**: `Wie heißen Sie? / Wie ist Ihr Name?` → `Ich heiße Anna. / Mein Name ist Anna.`
* **Hỏi Quê quán (`Woher`)**: `Woher kommen Sie?` → `Ich komme aus Vietnam / aus Deutschland.` (Woher luôn đi với **aus**).
* **Hỏi Nơi ở (`Wo`)**: `Wo wohnen Sie? / Wo lebst du?` → `Ich wohne in Ha Noi / in Berlin.` (Wo luôn đi với **in**).
* **Hỏi Sự vật (`Was`)**: `Was trinken Sie? / Was machen Sie?`
* 🗺️ **Sơ đồ V2 (Bản đồ W-Fragen)**: SVG kéo thả. Kéo từ `Wo` vào bảng, mũi tên tự động chỉ ra giới từ `in` kèm câu ví dụ. Kéo `Woher` chỉ ra `aus`.

### HỌC PHẦN 4: ☕ HỘI THOẠI THỰC TẾ: KAFFEE ODER TEE
* **Tìm chỗ ngồi**: *„Entschuldigung, ist hier frei?“* (Xin lỗi, chỗ này còn trống không?) — *„Ja klar, bitte.“*
* **Làm quen**: *„Ich bin John aus Frankreich, und du?“*
* **Gọi món**: *„Was trinkst du: Kaffee oder Tee?“ / „Was möchten Sie trinken?“* — *„Zwei Kaffee mit Zucker, bitte!“ / „Ich trinke Tee.“*

---

## PHẦN 3: KHO 125 BÀI TẬP ĐỘC NHẤT CỦA BÀI 13 (`lessons/a1/seed_a1_b13.py`)

Đây là linh hồn của Bài 13. Toàn bộ 125 câu được tôi **soạn thảo thủ công và mở rộng độ khó, ngữ cảnh** dựa trên tài liệu gốc, phủ kín 18 dạng bài tập của hệ thống DeutschMeister. Mọi câu hỏi đều có giải thích sắc bén chứa đúng đáp án.

### 3.1. TRẮC NGHIỆM (`trac_nghiem` - 15 CÂU)
**Câu 1:** Chọn dạng đúng: *„Meine Schwester ___ am Abend oft einen Roman.“ (lesen)*
*   Đáp án: `A. lest | B. lese | C. liest | D. liesst` -> **C**
*   Dịch: *Chị gái tôi thường đọc một cuốn tiểu thuyết vào buổi tối.*
*   Giải thích: `Meine Schwester` tương đương ngôi cô ấy (sie), động từ bất quy tắc `lesen` đổi `e → ie` thành `liest` → Đáp án: "liest".
**Câu 2:** Chọn dạng đúng: *„Wann ___ ihr am Wochenende nach Berlin?“ (fahren)*
*   Đáp án: `A. fährst | B. fahrt | C. fährt | D. fahren` -> **B**
*   Dịch: *Khi nào các bạn đi Berlin vào cuối tuần?*
*   Giải thích: LƯU Ý: Ngôi `ihr` (các bạn) KHÔNG biến âm. `fahren` bỏ -en thêm -t thành `fahrt` → Đáp án: "fahrt".
**Câu 3:** Chọn từ để hỏi: *„___ kommst du, Maria?“ — „Aus Spanien.“*
*   Đáp án: `A. Wo | B. Wie | C. Was | D. Woher` -> **D**
*   Dịch: *Bạn đến từ đâu, Maria? — Từ Tây Ban Nha.*
*   Giải thích: Trả lời dùng giới từ `Aus` (từ) chỉ xuất xứ, nên câu hỏi phải dùng `Woher` (từ đâu) → Đáp án: "Woher".
**Câu 4:** Chọn dạng đúng: *„Der Lehrer ___ heute sehr laut.“ (sprechen)*
*   Đáp án: `A. sprechet | B. sprech | C. spricht | D. spracht` -> **C**
*   Dịch: *Thầy giáo hôm nay nói rất to.*
*   Giải thích: `Der Lehrer` (er), động từ bất quy tắc `sprechen` đổi `e → i` thành `spricht` → Đáp án: "spricht".
**Câu 5:** Chọn dạng đúng: *„Was ___ Hannes und Julia dem kleinen Hund?“ (geben)*
*   Đáp án: `A. gibt | B. gebt | C. gibst | D. geben` -> **D**
*   Dịch: *Hannes và Julia cho chú chó nhỏ cái gì?*
*   Giải thích: Chủ ngữ là `Hannes und Julia` (họ - sie số nhiều), động từ giữ nguyên thể `geben` → Đáp án: "geben".
**Câu 6:** Chọn dạng đúng: *„Das Handy ___ in der Küche auf dem Tisch.“ (liegen)*
*   Đáp án: `A. liegst | B. lege | C. liegt | D. liegen` -> **C**
*   Dịch: *Chiếc điện thoại nằm trên bàn trong bếp.*
*   Giải thích: `Das Handy` (es) đi với động từ có quy tắc `liegen` thêm đuôi -t thành `liegt` → Đáp án: "liegt".
**Câu 7:** Chọn dạng đúng: *„___ du heute Nacht bei mir?“ (schlafen)*
*   Đáp án: `A. Schlafst | B. Schläfst | C. Schläft | D. Schlafen` -> **B**
*   Dịch: *Đêm nay bạn có ngủ ở nhà tôi không?*
*   Giải thích: Ngôi `du`, động từ `schlafen` đổi `a → ä` và thêm -st thành `schläfst` → Đáp án: "Schläfst".
**Câu 8:** Chọn đại từ: *„Der Vater grillt am Sonntag Fleisch. ___ macht auch einen Salat.“*
*   Đáp án: `A. Er | B. Sie | C. Es | D. Ihr` -> **A**
*   Dịch: *Bố nướng thịt vào Chủ nhật. Ông ấy cũng làm một món salad.*
*   Giải thích: Đại từ thay thế cho `Der Vater` (giống đực) là `Er` → Đáp án: "Er".
**Câu 9:** Chọn câu hỏi ĐÚNG cho câu trả lời: *„Ich trinke Kaffee mit Zucker.“*
*   Đáp án: `A. Wo wohnst du? | B. Was trinken Sie? | C. Wie heißt du? | D. Wer trinkt Tee?` -> **B**
*   Dịch: *Ngài uống gì? — Tôi uống cà phê có đường.*
*   Giải thích: Câu trả lời nói về đồ uống (Kaffee), nên câu hỏi phù hợp nhất là `Was trinken Sie?` → Đáp án: "Was trinken Sie?".
**Câu 10:** Chọn từ đúng: *„Entschuldigung, ___ hier frei?“*
*   Đáp án: `A. ist | B. sind | C. bin | D. bist` -> **A**
*   Dịch: *Xin lỗi, chỗ này còn trống không?*
*   Giải thích: Chủ ngữ giả định cho chỗ ngồi/nơi chốn là `es`, đi với động từ tobe `ist` → Đáp án: "ist".
**Câu 11:** Chọn dạng đúng: *„Wann ___ du deine Freunde im Café?“ (treffen)*
*   Đáp án: `A. treffst | B. triffst | C. trifft | D. treffen` -> **B**
*   Dịch: *Khi nào bạn gặp bạn bè ở quán cà phê?*
*   Giải thích: Ngôi `du`, động từ bất quy tắc `treffen` đổi `e → i` thành `triffst` → Đáp án: "triffst".
**Câu 12:** Chọn dạng đúng: *„Wir ___ im Sommer gern Vanilleeis.“ (essen)*
*   Đáp án: `A. isst | B. esse | C. essen | D. esst` -> **C**
*   Dịch: *Vào mùa hè chúng tôi thích ăn kem vani.*
*   Giải thích: Ngôi `wir` (chúng tôi) luôn dùng động từ nguyên thể `essen` → Đáp án: "essen".
**Câu 13:** Chọn dạng đúng: *„Julia und Lara ___ nach Italien.“ (reisen)*
*   Đáp án: `A. reist | B. reisen | C. reisst | D. reise` -> **B**
*   Dịch: *Julia và Lara đi du lịch đến Ý.*
*   Giải thích: Chủ ngữ số nhiều (họ), động từ giữ nguyên thể `reisen` → Đáp án: "reisen".
**Câu 14:** Chọn từ để hỏi: *„___ wohnen Sie jetzt?“ — „In München.“*
*   Đáp án: `A. Woher | B. Was | C. Wie | D. Wo` -> **D**
*   Dịch: *Ngài hiện sống ở đâu? — Ở München.*
*   Giải thích: Trả lời dùng giới từ `In` (ở), hỏi về địa điểm cư trú dùng `Wo` (ở đâu) → Đáp án: "Wo".
**Câu 15:** Chọn dạng đúng: *„Die Touristen ___ das alte Rathaus.“ (besuchen)*
*   Đáp án: `A. besucht | B. besuche | C. besuchen | D. besuchst` -> **C**
*   Dịch: *Du khách tham quan tòa thị chính cũ.*
*   Giải thích: `Die Touristen` (số nhiều - họ) dùng nguyên thể `besuchen` → Đáp án: "besuchen".

### 3.2. ĐIỀN KHUYẾT (`dien_khuyet` - 10 CÂU)
*(Học viên gõ 1 từ vào ô trống)*
**Câu 16:** *„___ heißt du?“ — „Ich heiße David.“*
*   Đáp án: `["Wie", "wie"]`
*   Dịch: *Bạn tên là gì? — Tôi tên là David.*
*   Giải thích: Hỏi tên luôn dùng từ để hỏi `Wie` (Wie heißen Sie / Wie heißt du) → Đáp án: "Wie".
**Câu 17:** *„Wir ___ den Käse im Supermarkt.“ (kaufen)*
*   Đáp án: `["kaufen"]`
*   Dịch: *Chúng tôi mua phô mai ở siêu thị.*
*   Giải thích: Chủ ngữ `wir` đi với nguyên thể `kaufen` → Đáp án: "kaufen".
**Câu 18:** *„Mein Onkel ___ gern schwarzen Tee.“ (trinken)*
*   Đáp án: `["trinkt"]`
*   Dịch: *Chú tôi thích uống trà đen.*
*   Giải thích: `Mein Onkel` (er), động từ có quy tắc `trinken` thêm -t thành `trinkt` → Đáp án: "trinkt".
**Câu 19:** *„Ich ___ meine Hausaufgaben.“ (machen)*
*   Đáp án: `["mache"]`
*   Dịch: *Tôi làm bài tập về nhà.*
*   Giải thích: Chủ ngữ `ich` đi với động từ thêm -e thành `mache` → Đáp án: "mache".
**Câu 20:** *„Die Kinder ___ Fußball auf dem Hof.“ (spielen)*
*   Đáp án: `["spielen"]`
*   Dịch: *Bọn trẻ chơi bóng đá trên sân.*
*   Giải thích: Chủ ngữ số nhiều `Die Kinder`, động từ ở nguyên thể `spielen` → Đáp án: "spielen".
**Câu 21:** *„Herr Müller, was ___ Sie trinken?“ (muốn)*
*   Đáp án: `["möchten", "moechten"]`
*   Dịch: *Ông Müller, ông muốn uống gì ạ?*
*   Giải thích: Động từ khuyết thiếu chỉ sự mong muốn lịch sự đi với Ngài (Sie) là `möchten` → Đáp án: "möchten".
**Câu 22:** *„Ich komme ___ Frankreich.“ (từ)*
*   Đáp án: `["aus"]`
*   Dịch: *Tôi đến từ nước Pháp.*
*   Giải thích: Giới từ chỉ xuất xứ đi với động từ kommen là `aus` → Đáp án: "aus".
**Câu 23:** *„___ ihr einen Brief an die Großmutter?“ (schreiben)*
*   Đáp án: `["Schreibt", "schreibt"]`
*   Dịch: *Các bạn đang viết thư cho bà nội phải không?*
*   Giải thích: Ngôi `ihr` (các bạn), động từ `schreiben` thêm -t thành `Schreibt` → Đáp án: "Schreibt".
**Câu 24:** *„Karin ___ sehr gern klassische Musik.“ (hören)*
*   Đáp án: `["hört", "hoert"]`
*   Dịch: *Karin rất thích nghe nhạc cổ điển.*
*   Giải thích: Karin (sie số ít), động từ `hören` thêm -t thành `hört` → Đáp án: "hört".
**Câu 25:** *„___ singst du so gern?“ — „Weil ich Musik liebe.“*
*   Đáp án: `["Warum", "warum"]`
*   Dịch: *Tại sao bạn lại thích hát như vậy? — Vì tôi yêu âm nhạc.*
*   Giải thích: Câu trả lời có Weil (Bởi vì), nên từ để hỏi phải là `Warum` (Tại sao) → Đáp án: "Warum".

### 3.3. CHIA ĐỘNG TỪ BẤT QUY TẮC (`dien_chia_dong_tu` - 10 CÂU) 🆕
*(Giao diện có gợi ý động từ nguyên thể trong ngoặc, yêu cầu gõ từ đã chia biến âm)*
**Câu 26:** *„Das Mädchen ___ im Wohnzimmer ein Buch.“ (lesen)*
*   Đáp án: `["liest"]`
*   Dịch: *Cô bé đọc sách trong phòng khách.*
*   Giải thích: Chủ ngữ `Das Mädchen` (es), `lesen` đổi e→ie thành `liest` → Đáp án: "liest".
**Câu 27:** *„Er ___ am Sonntag nach Hamburg.“ (fahren)*
*   Đáp án: `["fährt", "faehrt"]`
*   Dịch: *Anh ấy đi Hamburg vào Chủ nhật.*
*   Giải thích: Ngôi `er`, `fahren` đổi a→ä thành `fährt` → Đáp án: "fährt".
**Câu 28:** *„Was ___ du heute zum Frühstück?“ (essen)*
*   Đáp án: `["isst"]`
*   Dịch: *Bạn ăn gì cho bữa sáng hôm nay?*
*   Giải thích: Ngôi `du`, `essen` đổi e→i thành `isst` → Đáp án: "isst".
**Câu 29:** *„Der Tourist ___ fließend Deutsch.“ (sprechen)*
*   Đáp án: `["spricht"]`
*   Dịch: *Du khách nói tiếng Đức trôi chảy.*
*   Giải thích: `Der Tourist` (er), `sprechen` đổi e→i thành `spricht` → Đáp án: "spricht".
**Câu 30:** *„Bitte ___ mir den Zucker!“ (geben - ngôi du)*
*   Đáp án: `["gib"]`
*   Dịch: *Làm ơn đưa cho tôi đường!*
*   Giải thích: Thể mệnh lệnh ngôi du của `geben` (bất quy tắc e→i) là `gib` (bỏ -st) → Đáp án: "gib".
**Câu 31:** *„Wann ___ er seine neue Freundin?“ (treffen)*
*   Đáp án: `["trifft"]`
*   Dịch: *Khi nào anh ấy gặp bạn gái mới của mình?*
*   Giải thích: Ngôi `er`, `treffen` đổi e→i thành `trifft` → Đáp án: "trifft".
**Câu 32:** *„Der Hund ___ gemütlich auf dem Sofa.“ (schlafen)*
*   Đáp án: `["schläft", "schlaeft"]`
*   Dịch: *Chú chó ngủ thoải mái trên ghế sofa.*
*   Giải thích: `Der Hund` (er), `schlafen` đổi a→ä thành `schläft` → Đáp án: "schläft".
**Câu 33:** *„Ihr ___ am Wochenende zu lange!“ (schlafen)*
*   Đáp án: `["schlaft"]`
*   Dịch: *Các bạn ngủ quá nhiều vào cuối tuần!*
*   Giải thích: BẪY: Ngôi `ihr` KHÔNG biến âm. `schlafen` chỉ thêm -t thành `schlaft` → Đáp án: "schlaft".
**Câu 34:** *„___ du gern Romane oder Zeitungen?“ (lesen)*
*   Đáp án: `["Liest", "liest"]`
*   Dịch: *Bạn thích đọc tiểu thuyết hay báo?*
*   Giải thích: Ngôi `du`, `lesen` đổi e→ie thành `Liest` → Đáp án: "Liest".
**Câu 35:** *„Die Chefin ___ gerade mit einem Kunden.“ (sprechen)*
*   Đáp án: `["spricht"]`
*   Dịch: *Sếp nữ đang nói chuyện với một khách hàng.*
*   Giải thích: `Die Chefin` (cô ấy - sie), `sprechen` đổi e→i thành `spricht` → Đáp án: "spricht".

### 3.4. DỊCH TỪ VIỆT → ĐỨC (`dich_nghia_vd` - 5 CÂU)
*(Nhập danh từ có mạo từ)*
**Câu 36:** *cà phê*
*   Đáp án: `["der Kaffee", "Kaffee"]`
*   Giải thích: Cà phê trong tiếng Đức là `der Kaffee`.
**Câu 37:** *trà*
*   Đáp án: `["der Tee", "Tee"]`
*   Giải thích: Trà là `der Tee`.
**Câu 38:** *rau củ*
*   Đáp án: `["das Gemüse", "Gemüse", "Gemuese", "das Gemuese"]`
*   Giải thích: Rau củ là danh từ giống trung `das Gemüse`.
**Câu 39:** *bức thư*
*   Đáp án: `["der Brief", "Brief"]`
*   Giải thích: Bức thư là `der Brief`.
**Câu 40:** *tòa thị chính*
*   Đáp án: `["das Rathaus", "Rathaus"]`
*   Giải thích: Tòa thị chính là danh từ ghép (der Rat + das Haus) -> `das Rathaus`.

### 3.5. DỊCH TỪ / CÂU NGẮN ĐỨC → VIỆT (`dich_nghia_dv` - 5 CÂU)
**Câu 41:** *„Entschuldigung, ist hier frei?“*
*   Đáp án: `["Xin lỗi, chỗ này còn trống không?", "Xin lỗi chỗ này trống không?"]`
*   Giải thích: Câu hỏi lịch sự khi muốn ngồi vào bàn trong quán Cafe.
**Câu 42:** *„Ja klar, bitte.“*
*   Đáp án: `["Vâng tất nhiên, xin mời.", "Vâng, xin mời.", "Tất nhiên rồi, xin mời."]`
*   Giải thích: Câu trả lời đồng ý cho người khác ngồi.
**Câu 43:** *„Zwei Kaffee, bitte!“*
*   Đáp án: `["Xin cho hai cà phê!", "Hai cà phê nhé!", "Cho hai cà phê!"]`
*   Giải thích: Cách gọi món nhanh gọn với từ `bitte` (làm ơn/xin vui lòng).
**Câu 44:** *„das Futter“*
*   Đáp án: `["thức ăn thú cưng", "thức ăn cho thú", "thức ăn động vật", "thức ăn"]`
*   Giải thích: `das Futter` dùng riêng để chỉ thức ăn cho động vật (chó, mèo...).
**Câu 45:** *„der Käse“*
*   Đáp án: `["phô mai", "pho mát"]`
*   Giải thích: `der Käse` là phô mai.

### 3.6. NỐI Ô TƯƠNG ỨNG (`noi_o` - 10 BÀI x 4 CẶP)
*(Hệ thống tự render 10 bài tập, mỗi bài 4 cặp trộn lẫn. Dưới đây là dữ liệu nguồn cho 10 bài)*
**Bài Nối 1 (Đại từ ↔ Động từ bất quy tắc nhóm e→i):**
*   `ich` ↔ `spreche`
*   `du` ↔ `sprichst`
*   `er` ↔ `spricht`
*   `ihr` ↔ `sprecht`
*(Giải thích: Ngôi ich/ihr giữ nguyên 'e', ngôi du/er biến 'e' thành 'i'.)*
**Bài Nối 2 (Đại từ ↔ Động từ bất quy tắc nhóm a→ä):**
*   `wir` ↔ `fahren`
*   `du` ↔ `fährst`
*   `sie (cô ấy)` ↔ `fährt`
*   `ihr` ↔ `fahrt`
**Bài Nối 3 (Đại từ ↔ Động từ schlafen):**
*   `ich` ↔ `schlafe`
*   `du` ↔ `schläfst`
*   `es` ↔ `schläft`
*   `ihr` ↔ `schlaft`
**Bài Nối 4 (W-Fragen ↔ Trả lời):**
*   `Woher kommen Sie?` ↔ `Aus Vietnam.`
*   `Wo wohnen Sie?` ↔ `In Berlin.`
*   `Wie heißen Sie?` ↔ `Ich bin Anna.`
*   `Was trinken Sie?` ↔ `Kaffee, bitte.`
**Bài Nối 5 (Danh từ ↔ Nghĩa Việt):**
*   `der Zucker` ↔ `đường`
*   `das Rathaus` ↔ `tòa thị chính`
*   `der Brief` ↔ `bức thư`
*   `der Hund` ↔ `con chó`
**Bài Nối 6 (Giao tiếp Cafe ↔ Phản hồi):**
*   `Ist hier frei?` ↔ `Ja klar, bitte.`
*   `Was möchten Sie trinken?` ↔ `Einen Tee, bitte.`
*   `Ich bin John.` ↔ `Ich heiße Maria.`
*   `Trinkst du Kaffee oder Tee?` ↔ `Kaffee mit Zucker.`
**Bài Nối 7 (Đại từ ↔ Động từ lesen):**
*   `ich` ↔ `lese`
*   `du` ↔ `liest`
*   `er` ↔ `liest`
*   `ihr` ↔ `lest`
**Bài Nối 8 (Động từ nguyên thể ↔ Nghĩa Việt):**
*   `geben` ↔ `cho, đưa`
*   `treffen` ↔ `gặp gỡ`
*   `reisen` ↔ `du lịch`
*   `grillen` ↔ `nướng BBQ`
**Bài Nối 9 (Chia động từ sein/haben):**
*   `ich` ↔ `bin`
*   `du` ↔ `bist`
*   `wir` ↔ `haben`
*   `er` ↔ `hat`
**Bài Nối 10 (Chủ ngữ ↔ Động từ essen):**
*   `Das Mädchen` ↔ `isst Eis.`
*   `Die Kinder` ↔ `essen Eis.`
*   `Ich` ↔ `esse Eis.`
*   `Ihr` ↔ `esst Eis.`

### 3.7. ĐIỀN 2 CHỖ TRỐNG TẠO CÂU (`dien_tao_cau` - 8 CÂU)
**Câu 46:** *„[1] heißt du und woher [2] du?“*
*   Đáp án: [1] `Wie`, [2] `kommst`
*   Giải thích: Hỏi tên dùng `Wie`; chủ ngữ `du` đi với `kommen` thành `kommst`.
**Câu 47:** *„Die Touristen [1] das Rathaus und [2] Fotos.“ (besuchen / machen)*
*   Đáp án: [1] `besuchen`, [2] `machen`
*   Giải thích: `Die Touristen` (số nhiều) → dùng nguyên thể `besuchen` và `machen`.
**Câu 48:** *„Mein Bruder [1] am Wochenende nach München. Er [2] dort Freunde.“ (fahren / treffen)*
*   Đáp án: [1] `fährt`, [2] `trifft`
*   Giải thích: `Mein Bruder` (er) → `fährt` (a→ä) và `trifft` (e→i).
**Câu 49:** *„[1] schläft das Baby? — Es [2] im Schlafzimmer.“ (Wo / schlafen)*
*   Đáp án: [1] `Wo`, [2] `schläft`
*   Giải thích: Hỏi ở đâu dùng `Wo`; `Es` đi với `schlafen` thành `schläft`.
**Câu 50:** *„Wir [1] gern Fleisch, aber Anna [2] lieber Gemüse.“ (grillen)*
*   Đáp án: [1] `grillen`, [2] `grillt`
*   Giải thích: `Wir` → nguyên thể `grillen`; `Anna` (sie) → thêm -t thành `grillt`.
**Câu 51:** *„Was [1] ihr? Kaffee oder Tee? — Wir [2] Tee.“ (trinken)*
*   Đáp án: [1] `trinkt`, [2] `trinken`
*   Giải thích: Ngôi `ihr` → `trinkt`; Ngôi `wir` → `trinken`.
**Câu 52:** *„[1] kommen Sie? — [2] der Türkei.“*
*   Đáp án: [1] `Woher`, [2] `Aus`
*   Giải thích: Hỏi xuất xứ dùng `Woher` đi kèm giới từ `Aus`.
**Câu 53:** *„[1] isst du gern? — Ich [2] gern Käse.“ (essen)*
*   Đáp án: [1] `Was`, [2] `esse`
*   Giải thích: Hỏi ăn món gì dùng `Was`; Ngôi `ich` → `esse`.

### 3.8. NGHE GIỌNG BẢN XỨ VÀ ĐIỀN TỪ (`nghe_dien` - 8 CÂU)
*(Audio đọc 1 câu chuẩn de-DE, học viên nghe và điền từ còn thiếu)*
**Câu 54:** `Audio: "Der Vater liest die Zeitung."`
*   Hiển thị: *Der Vater ___ die Zeitung.*
*   Đáp án: `["liest"]`
*   Giải thích: Nghe kỹ âm "ie" dài trong từ `liest`.
**Câu 55:** `Audio: "Wann fahrt ihr nach Hause?"`
*   Hiển thị: *Wann ___ ihr nach Hause?*
*   Đáp án: `["fahrt"]`
*   Giải thích: Chú ý ngôi ihr, nghe âm "a" ngắn, không phải "ä".
**Câu 56:** `Audio: "Ich komme aus Vietnam."`
*   Hiển thị: *Ich komme ___ Vietnam.*
*   Đáp án: `["aus"]`
*   Giải thích: Giới từ chỉ xuất xứ là `aus`.
**Câu 57:** `Audio: "Das Kind isst ein Eis."`
*   Hiển thị: *Das Kind ___ ein Eis.*
*   Đáp án: `["isst"]`
*   Giải thích: Ngôi `es` (Das Kind), động từ essen biến thành `isst`.
**Câu 58:** `Audio: "Sprichst du Deutsch?"`
*   Hiển thị: *___ du Deutsch?*
*   Đáp án: `["Sprichst", "sprichst"]`
*   Giải thích: Động từ đảo lên đầu trong câu hỏi Yes/No, ngôi du → `Sprichst`.
**Câu 59:** `Audio: "Wir wohnen in Berlin."`
*   Hiển thị: *Wir wohnen ___ Berlin.*
*   Đáp án: `["in"]`
*   Giải thích: Giới từ chỉ nơi chốn (thành phố) là `in`.
**Câu 60:** `Audio: "Zwei Kaffee, bitte!"`
*   Hiển thị: *Zwei ___, bitte!*
*   Đáp án: `["Kaffee"]`
*   Giải thích: Danh từ `Kaffee`.
**Câu 61:** `Audio: "Der Hund schläft auf dem Sofa."`
*   Hiển thị: *Der Hund ___ auf dem Sofa.*
*   Đáp án: `["schläft", "schlaeft"]`
*   Giải thích: Ngôi 3 số ít, schlafen → `schläft`.

### 3.9. DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (`dich_cau_vd` - 8 CÂU)
**Câu 62:** *Tôi đến từ nước Đức.*
*   Đáp án: `["Ich komme aus Deutschland."]`, `["Ich komme aus Deutschland"]`
*   Giải thích: Chủ ngữ Ich + động từ komme + giới từ aus + Deutschland.
**Câu 63:** *Bạn sống ở đâu?*
*   Đáp án: `["Wo wohnst du?", "Wo wohnen Sie?"]`
*   Giải thích: Từ để hỏi Wo + động từ wohnen chia theo ngôi du/Sie.
**Câu 64:** *Ông nội tôi đọc báo.*
*   Đáp án: `["Mein Opa liest die Zeitung.", "Mein Großvater liest die Zeitung."]`, `["Mein Opa liest Zeitung."]`, `["Mein Opa liest eine Zeitung."]`, `["Mein Opa liest"]`
*   Giải thích: Opa (er) → lesen biến âm thành `liest`. (Chấm nới lỏng các phương án mạo từ).
**Câu 65:** *Cô ấy đi Berlin.*
*   Đáp án: `["Sie fährt nach Berlin."]`, `["Sie fahrt nach Berlin"]` (Sai - sẽ bị loại) -> `["Sie fährt nach Berlin"]`
*   Giải thích: Sie (cô ấy) → fahren biến âm thành `fährt`. Giới từ đi tới thành phố là `nach`.
**Câu 66:** *Anh ấy gặp bạn bè của anh ấy.*
*   Đáp án: `["Er trifft seine Freunde."]`, `["Er trifft seine Freunde"]`
*   Giải thích: Er → treffen biến âm thành `trifft`.
**Câu 67:** *Chúng tôi ăn kem.*
*   Đáp án: `["Wir essen Eis."]`, `["Wir essen ein Eis."]`, `["Wir essen Eis"]`
*   Giải thích: Wir → giữ nguyên thể `essen`.
**Câu 68:** *Các bạn ngủ ở khách sạn phải không?*
*   Đáp án: `["Schlaft ihr im Hotel?"]`
*   Giải thích: Câu hỏi Yes/No đảo động từ. Ngôi ihr KHÔNG biến âm → `Schlaft ihr`.
**Câu 69:** *Ngài muốn uống gì ạ?*
*   Đáp án: `["Was möchten Sie trinken?"]`, `["Was moechten Sie trinken?"]`
*   Giải thích: Câu giao tiếp lịch sự dùng `möchten Sie trinken`.

### 3.10. DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (`dich_cau_dv` - 7 CÂU)
**Câu 70:** *„Wie ist Ihr Name?“*
*   Đáp án: `["Tên của ngài là gì?", "Tên ngài là gì?", "Ngài tên là gì?"]`
*   Giải thích: Câu hỏi tên trang trọng.
**Câu 71:** *„Entschuldigung, ist hier frei?“*
*   Đáp án: `["Xin lỗi, chỗ này còn trống không?", "Xin lỗi, ở đây trống không?"]`
*   Giải thích: Câu hỏi kinh điển khi muốn ngồi ghép bàn ở quán.
**Câu 72:** *„Ich trinke Tee mit Zucker.“*
*   Đáp án: `["Tôi uống trà với đường.", "Tôi uống trà có đường."]`, `["Tôi uống trà đường."] `
*   Giải thích: mit Zucker = với đường.
**Câu 73:** *„Der Lehrer spricht zu leise.“*
*   Đáp án: `["Thầy giáo nói quá nhỏ.", "Giáo viên nói quá nhỏ."]`, `["Thầy giáo nói quá khẽ."] `
*   Giải thích: spricht = nói, zu leise = quá nhỏ/khẽ.
**Câu 74:** *„Hannes gibt dem Hund das Futter.“*
*   Đáp án: `["Hannes cho chó ăn thức ăn.", "Hannes đưa thức ăn cho chó."]`, `["Hannes cho chú chó thức ăn."] `
*   Giải thích: gibt = đưa/cho, Futter = thức ăn.
**Câu 75:** *„Fährst du am Wochenende nach Polen?“*
*   Đáp án: `["Cuối tuần bạn có đi Ba Lan không?", "Bạn có đi Ba Lan vào cuối tuần không?"]`
*   Giải thích: Fährst du = Bạn có lái xe/đi...
**Câu 76:** *„Karin wohnt in München.“*
*   Đáp án: `["Karin sống ở München.", "Karin sống tại München."] `
*   Giải thích: wohnen in = sống ở.

### 3.11. SẮP XẾP TỪ THÀNH CÂU (`sap_xep_cau` - 10 CÂU)
*(Kéo thả các khối từ để tạo thành câu chuẩn Satzstellung)*
**Câu 77:** `[die Kinder, essen, Eis, Im Sommer, gern]`
*   Đáp án: `["Im Sommer essen die Kinder gern Eis.", "Die Kinder essen im Sommer gern Eis."]`
*   Giải thích: Trạng ngữ "Im Sommer" đứng đầu thì động từ "essen" vẫn phải ở vị trí số 2, sau đó mới đến chủ ngữ "die Kinder".
**Câu 78:** `[ihr, nach, Reist, Italien, ?]`
*   Đáp án: `["Reist ihr nach Italien?"]`
*   Giải thích: Câu hỏi Yes/No động từ đảo lên đầu.
**Câu 79:** `[wohnen, in, Sie, Wo, Berlin, ?]` -> `[wohnen, Sie, Wo, in, Berlin, ?]` (fix tokens)
*   Tokens: `[wohnen, Sie, in Berlin, Wo, ?]`
*   Đáp án: `["Wo wohnen Sie in Berlin?"]`
*   Giải thích: Từ để hỏi Wo đứng đầu, động từ wohnen đứng thứ 2.
**Câu 80:** `[trinkt, Was, am Morgen, der Opa, ?]`
*   Đáp án: `["Was trinkst der Opa am Morgen?", "Was trinkt der Opa am Morgen?"]` (Đúng: trinkt)
*   Giải thích: Từ để hỏi Was đứng đầu, động từ trinkt vị trí 2, chủ ngữ der Opa.
**Câu 81:** `[die Zeitung, Der Großvater, am Morgen, liest]`
*   Đáp án: `["Der Großvater liest am Morgen die Zeitung.", "Am Morgen liest der Großvater die Zeitung."]`
*   Giải thích: Động từ "liest" luôn ở vị trí 2.
**Câu 82:** `[dem Hund, Hannes, das Futter, gibt]`
*   Đáp án: `["Hannes gibt dem Hund das Futter.", "Dem Hund gibt Hannes das Futter."]`
*   Giải thích: Động từ "gibt" ở vị trí 2.
**Câu 83:** `[im Hotel, schlafen, Wir, heute]`
*   Đáp án: `["Wir schlafen heute im Hotel.", "Heute schlafen wir im Hotel."]`
*   Giải thích: Động từ "schlafen" ở vị trí 2.
**Câu 84:** `[spricht, Der Lehrer, Deutsch, fließend]`
*   Đáp án: `["Der Lehrer spricht fließend Deutsch.", "Fließend Deutsch spricht der Lehrer."]`
*   Giải thích: Động từ "spricht" ở vị trí 2.
**Câu 85:** `[treffe, ich, Heute, meine Freunde]`
*   Đáp án: `["Heute treffe ich meine Freunde.", "Ich treffe heute meine Freunde."]`
*   Giải thích: Động từ "treffe" ở vị trí 2.
**Câu 86:** `[aus, kommst, Woher, du, ?]`
*   Đáp án: `["Woher kommst du?"]` (Có dư từ aus? Fix: `[kommst, Woher, du, ?]`) -> `["Woher kommst du?"]`
*   Giải thích: Woher đã bao hàm nghĩa "từ", đi kèm động từ kommst vị trí 2.

### 3.12. PHÂN LOẠI ĐỘNG TỪ (`phan_loai_dong_tu` - 3 BÀI) 🆕
*(Kéo 4 động từ vào 2 cột: Bất quy tắc (Có biến âm) / Có quy tắc (Không biến âm))*
**Câu 87:**
*   `lesen` → **Bất quy tắc**
*   `kaufen` → **Có quy tắc**
*   `fahren` → **Bất quy tắc**
*   `machen` → **Có quy tắc**
*   Giải thích: `lesen (e→ie)`, `fahren (a→ä)` là bất quy tắc.
**Câu 88:**
*   `sprechen` → **Bất quy tắc**
*   `hören` → **Có quy tắc**
*   `spielen` → **Có quy tắc**
*   `treffen` → **Bất quy tắc**
*   Giải thích: `sprechen (e→i)`, `treffen (e→i)` là bất quy tắc.
**Câu 89:**
*   `schlafen` → **Bất quy tắc**
*   `reisen` → **Có quy tắc**
*   `geben` → **Bất quy tắc**
*   `grillen` → **Có quy tắc**
*   Giải thích: `schlafen (a→ä)`, `geben (e→i)` là bất quy tắc.

### 3.13. PHÂN LOẠI TỪ ĐỂ HỎI (`phan_loai_tu_hoi` - 3 BÀI) 🆕
*(Kéo 4 câu trả lời vào 4 cột từ để hỏi: Wie, Wo, Woher, Was)*
**Câu 90:**
*   `Aus Vietnam.` → **Woher**
*   `In Berlin.` → **Wo**
*   `Anna.` → **Wie** (Wie heißt du?)
*   `Kaffee.` → **Was** (Was trinkst du?)
*   Giải thích: Aus đi với Woher, In đi với Wo, Tên đi với Wie, Đồ vật đi với Was.
**Câu 91:**
*   `Ich bin John.` → **Wie** (hoặc Wer - nhưng trong bài này ưu tiên ghép với câu hỏi tên) -> Sửa đề: `Mein Name ist John.` → **Wie**
*   `Aus Frankreich.` → **Woher**
*   `In München.` → **Wo**
*   `Ein Eis.` → **Was**
**Câu 92:**
*   `Aus der Türkei.` → **Woher**
*   `Ich heiße Julia.` → **Wie**
*   `In Hamburg.` → **Wo**
*   `Einen Tomatensalat.` → **Was**

### 3.14. TÌM LỖI SAI VÀ SỬA LẠI (`tim_loi_sai` - 10 CÂU)
*(Bẫy kinh điển: ihr biến âm, aus/in)*
**Câu 93:** *„Ihr schläft heute Nacht im Hotel, oder?“*
*   Đáp án: `["Ihr schlaft heute Nacht im Hotel, oder?"]`
*   Giải thích: BẪY: Ngôi `ihr` (các bạn) KHÔNG biến âm. `schlafen` + `ihr` → **`schlaft`**.
**Câu 94:** *„Wann treffst du heute deine Freunde?“*
*   Đáp án: `["Wann triffst du heute deine Freunde?"]`
*   Giải thích: Động từ `treffen` biến âm `e→i`. Ngôi `du` chuyển thành **`triffst`**.
**Câu 95:** *„Woher wohnst du in Berlin?“*
*   Đáp án: `["Wo wohnst du in Berlin?"]`
*   Giải thích: Hỏi nơi ở (với giới từ in) phải dùng **`Wo`**, không dùng `Woher`.
**Câu 96:** *„Das Mädchen lest im Wohnzimmer ein Buch.“*
*   Đáp án: `["Das Mädchen liest im Wohnzimmer ein Buch."]`
*   Giải thích: `Das Mädchen` = es. `lesen` đổi `e→ie` thành **`liest`**.
**Câu 97:** *„Ich fahrt am Wochenende ans Meer.“*
*   Đáp án: `["Ich fahre am Wochenende ans Meer."]`
*   Giải thích: Ngôi `ich` thêm đuôi `-e` bình thường → **`fahre`**.
**Câu 98:** *„Der Lehrer sprechen zu leise.“*
*   Đáp án: `["Der Lehrer spricht zu leise."]`
*   Giải thích: `Der Lehrer` (er). `sprechen` biến đổi thành **`spricht`**.
**Câu 99:** *„Ich komme in Deutschland.“*
*   Đáp án: `["Ich komme aus Deutschland."]`
*   Giải thích: Xuất xứ dùng giới từ **`aus`**.
**Câu 100:** *„Was esst er gern?“*
*   Đáp án: `["Was isst er gern?"]`
*   Giải thích: Ngôi `er`, `essen` đổi `e→i` thành **`isst`**.
**Câu 101:** *„Entschuldigung, ist hier frei sein?“*
*   Đáp án: `["Entschuldigung, ist hier frei?"]`
*   Giải thích: Đã có tobe `ist`, không thêm `sein` ở cuối.
**Câu 102:** *„Hannes und Julia gibt dem Hund das Futter.“*
*   Đáp án: `["Hannes und Julia geben dem Hund das Futter."]`
*   Giải thích: Chủ ngữ số nhiều (Hannes và Julia), động từ giữ nguyên thể **`geben`**.

### 3.15. ĐẶT CÂU HỎI CHO TỪ GẠCH CHÂN (`viet_lai_cau_w` - 5 CÂU) 🆕
*(Giao diện: Câu có 1 cụm in đậm, gõ câu hỏi cho cụm đó)*
**Câu 103:** *„Ich komme **aus Polen**.“* (Hỏi ngôi du)
*   Đáp án: `["Woher kommst du?"]`
*   Giải thích: `aus Polen` (xuất xứ) → hỏi bằng `Woher`. `ich` → đổi thành `du` → `kommst`.
**Câu 104:** *„Mein Name ist **Anna**.“* (Hỏi ngôi Sie)
*   Đáp án: `["Wie ist Ihr Name?", "Wie heißen Sie?"]`
*   Giải thích: Hỏi tên trang trọng.
**Câu 105:** *„Ich wohne **in Ha Noi**.“* (Hỏi ngôi du)
*   Đáp án: `["Wo wohnst du?"]`
*   Giải thích: `in Ha Noi` (địa điểm) → hỏi bằng `Wo`.
**Câu 106:** *„Wir trinken **Kaffee**.“* (Hỏi ngôi ihr)
*   Đáp án: `["Was trinkt ihr?"]`
*   Giải thích: Hỏi sự vật → `Was`. Đổi `wir` thành `ihr` → `trinkt`.
**Câu 107:** *„Sie kommt **aus der Türkei**.“* (Hỏi ngôi sie - cô ấy)
*   Đáp án: `["Woher kommt sie?"]`
*   Giải thích: `aus` → `Woher`. Giữ nguyên ngôi 3 số ít.

### 3.16. ĐÚNG HAY SAI (`dung_sai` - 3 CÂU)
**Đoạn văn A:**
> *"Das ist David. Er kommt aus Spanien, aber er wohnt jetzt in Berlin. Am Wochenende fährt er oft mit dem Fahrrad in den Park. Er liest gern Bücher und isst Pizza. Heute trifft er Maria im Café. Sie trinken zusammen Kaffee mit viel Zucker."*
**Câu 108:** Mệnh đề: *„David kommt aus Deutschland.“*
*   Đáp án: **Falsch (Sai)**
*   Giải thích: Đoạn văn ghi anh ấy đến từ Tây Ban Nha (*kommt aus Spanien*).
**Câu 109:** Mệnh đề: *„Maria und David trinken Kaffee.“*
*   Đáp án: **Richtig (Đúng)**
*   Giải thích: Đoạn cuối nói *Sie trinken zusammen Kaffee* (Họ cùng uống cà phê).
**Câu 110:** Mệnh đề: *„David isst gern Pizza und liest Bücher.“*
*   Đáp án: **Richtig (Đúng)**
*   Giải thích: Đoạn văn ghi *Er liest gern Bücher und isst Pizza*.

### 3.17. SẮP XẾP HỘI THOẠI (`hoi_thoai_sap_xep` - 3 CÂU)
**Câu 111:** (Hội thoại quán Cafe)
*   1. **Gast**: Entschuldigung, ist hier frei?
*   2. **Anna**: Ja klar, bitte. Setzen Sie sich.
*   3. **Gast**: Danke. Ich bin John aus Frankreich, und du?
*   4. **Anna**: Ich heiße Anna. Ich komme aus Polen.
*   5. **Kellner**: Was möchtet ihr trinken: Kaffee oder Tee?
*   6. **Gast**: Zwei Kaffee mit Zucker, bitte!
*(Giải thích: Theo đúng flow logic: Hỏi chỗ → Đồng ý → Cảm ơn & Giới thiệu → Đáp lại → Bồi bàn ra hỏi → Gọi món).*

**Câu 112:** (Làm quen cơ bản)
*   1. Guten Tag! Wer sind Sie?
*   2. Guten Tag, mein Name ist David. Und wie heißen Sie?
*   3. Ich bin Maria. Woher kommen Sie, David?
*   4. Ich komme aus Deutschland.
*   5. Und wo wohnen Sie jetzt?
*   6. Ich wohne in Berlin.

**Câu 113:** (Tình huống rủ rê)
*   1. Hallo! Wann triffst du heute deine Freunde?
*   2. Hallo! Wir treffen uns um 15 Uhr im Café.
*   3. Was macht ihr dort?
*   4. Wir trinken Kaffee und essen Kuchen.
*   5. Das klingt gut! Viel Spaß!
*   6. Danke!

### 3.18. NHÌN MENU CHỌN PHẢN HỒI (`nghe_chon_dap_an` -> Chuyển thành `doc_menu_cafe` theo concept ôn tập - 2 CÂU)
*(Hiển thị 1 bảng thực đơn nhỏ, yêu cầu chọn câu nói đúng của khách)*
**Câu 114:** (Menu có Kaffee, Tee, Kuchen). Bồi bàn hỏi: *„Was möchten Sie trinken?“*
*   Đáp án đúng: `Ich trinke einen Kaffee.` (Các phương án sai: Ich esse Kuchen / Ich heiße Anna / Ich komme aus Vietnam).
*   Giải thích: Bồi bàn hỏi đồ uống, phải trả lời bằng thức uống có trong menu.
**Câu 115:** (Menu có Pizza, Salat, Eis). Bạn của bạn hỏi: *„Was essen wir jetzt?“*
*   Đáp án đúng: `Wir essen ein Eis.` (Các phương án sai: Wir trinken Kaffee / Wir schlafen / Wir fahren).
*   Giải thích: Hỏi ăn gì, trả lời món ăn.

---

## PHẦN 4: HỆ THỐNG ENGINE SINH ĐỀ VÔ HẠN (`GENERATIVE ENGINES`)

Để tính năng "Đổi bộ đề ngẫu nhiên mới" hoạt động với quy mô 125 câu, Antigravity IDE sử dụng các thuật toán nội suy dựa trên các Dictionary Lõi.

### 4.1. Dictionary Lõi (The Brain)
```python
SUBJECTS = {
    "1st_sg": ["ich"], "2nd_sg": ["du"], "3rd_sg": ["er", "sie", "es", "Der Lehrer", "Das Mädchen", "Mein Vater"],
    "1st_pl": ["wir"], "2nd_pl": ["ihr"], "3rd_pl": ["sie", "Die Kinder", "Meine Freunde"], "formal": ["Sie"]
}

IRREGULAR_VERBS = {
    "lesen":    {"base": "les", "shift": "lies", "type": "e->ie"},
    "fahren":   {"base": "fahr", "shift": "fähr", "type": "a->ä"},
    "schlafen": {"base": "schlaf", "shift": "schläf", "type": "a->ä"},
    "sprechen": {"base": "sprech", "shift": "sprich", "type": "e->i"},
    "treffen":  {"base": "treff", "shift": "triff", "type": "e->i"},
    "essen":    {"base": "ess", "shift": "iss", "type": "e->i"},
    "geben":    {"base": "geb", "shift": "gib", "type": "e->i"}
}

def conjugate_verb(verb, person_key):
    v = IRREGULAR_VERBS.get(verb)
    if not v: return regular_conjugate(verb, person_key) 
    
    # R1 & R2: Biến âm CHỈ ở 2nd_sg và 3rd_sg. Ngôi "ihr" dùng base.
    stem = v["shift"] if person_key in ["2nd_sg", "3rd_sg"] else v["base"]
    
    if person_key == "1st_sg": return stem + "e"
    if person_key == "2nd_sg": return stem + "t" if verb in ["essen", "lesen"] else stem + "st"
    if person_key in ["3rd_sg", "2nd_pl"]: return stem + "t"
    return verb # 1st_pl, 3rd_pl, formal
```

### 4.2. Khung Render Động (Prompt Templates)
*   **E1 (Irregular Verb Gen)**: `"{Subject} {Conjugated_Verb} {Context}."`
    *   `fahren` + `["nach Berlin", "ans Meer", "in die Schweiz", "nach Hause"]`.
    *   `lesen` + `["einen Roman", "die Zeitung", "ein langes Buch", "eine E-Mail"]`.
*   **E2 (W-Fragen Builder)**: `Woher` + `kommen` + `aus`. `Wo` + `wohnen` + `in`. `Wie` + `heißen`.
*   **E3 (Cafe Simulator)**: `[Ich trinke] + [Kaffee / Tee] + [mit Zucker / ohne Milch]`.

---

## PHẦN 5: KIỂM THỬ TOÀN DIỆN & ZERO-BUG QA (`verify_lesson13_qa.py`)

> **Yêu cầu sinh tử cho IDE**: Sau khi code, BẮT BUỘC thực thi script QA, sửa lỗi cho đến khi PASS 100%, rồi mới dán báo cáo.

### Danh sách Test Tự động
1.  **`test_total_count_125`**: Đảm bảo mảng bài tập có exactly 125 câu, đúng phân bổ 18 dạng.
2.  **`test_unique_hashes`**: Xóa khoảng trắng, dấu câu, lower case toàn bộ 125 câu. `len(set) == 125`. Trùng lặp = FAIL.
3.  **`test_ihr_conjugation_safety` (Chống bẫy `ihr`)**: Quét Regex đáp án. Nếu xuất hiện `ihr läst, ihr fäht, ihr schläft, ihr triffst, ihr isst, ihr gibt` → Báo lỗi FATAL, render lại.
4.  **`test_w_fragen_logic`**: Câu có `aus` phải đi với `Woher / kommen`. Câu có `in` đi với `Wo / wohnen`.
5.  **`test_explanation_contains_answer`**: Lặp qua 125 câu, chứng minh `explanation` có chứa chuỗi của `accepted_answers`.
6.  **`test_tts_cleanliness`**: `speak_text` không chứa `___`, `[1]`, ngoặc vuông.
7.  **`test_zero_regression`**: Load hash SHA-256 của các bài 1-12. Đảm bảo file cũ không bị mất dòng nào.

### Mẫu Báo Cáo Console (Dán vào cuối quá trình)
```
[✓] BÁO CÁO QA BÀI 13 (ÖK A1)
    - Tổng số câu sinh ra: 125 / 125 (Phủ đủ 18 dạng UI).
    - Tỉ lệ trùng lặp: 0% (125 Unique Hashes).
    - DB Update: Thêm 10 động từ, 12 danh từ.
[✓] Zero-Bug Protocol:
    - 'ihr_conjugation_safety': PASS (Không sinh Umlaut sai cho ngôi ihr).
    - 'w_fragen_logic': PASS.
    - 'tts_cleanliness': PASS.
    - 'explanations_validated': PASS.
[✓] Zero-Regression: Bài 1-12 nguyên vẹn. UI components tương thích.
[!] STATUS: READY TO DEPLOY LESSON 13.
```