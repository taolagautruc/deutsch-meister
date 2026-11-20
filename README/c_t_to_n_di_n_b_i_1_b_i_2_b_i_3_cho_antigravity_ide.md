# ĐẶC TẢ KỸ THUẬT TOÀN DIỆN HỆ THỐNG DEUTSCHMEISTER (TỪ BÀI 1 ĐẾN BÀI 3 - CẤP ĐỘ A1)

> **NGUYÊN TẮC BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
> 1. **Cộng dồn & Mở rộng tuyệt đối (Additive Expansion Only)**: Tuyệt đối **KHÔNG ĐƯỢC XÓA BỚT** bất kỳ nội dung lý thuyết, từ vựng, bảng tra cứu hay bài tập nào của các bài học trước (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**). Mọi nâng cấp phải được **bổ sung nối tiếp và làm dài thêm** nội dung bài giảng.
> 2. **Bản quyền & Độc lập 100%**: Tuyệt đối **KHÔNG** chèn bất kỳ đường dẫn, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu.
> 3. **Quy mô Bài tập chuẩn**: Mỗi bài học (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**) đều phải có **đúng 50 câu hỏi đa dạng** kèm **hệ thống Random đổi đề tự động** mỗi khi người học bấm nút `🔄 Đổi đề khác` hoặc thoát ra vào lại.

---

## PHẦN 1: CẤU TRÚC THANH ĐIỀU HƯỚNG & 2 BỘ TRA CỨU CHUYÊN SÂU (`templates/index.html`)

### 1.1. Thứ tự 6 Tab trên Thanh Điều Hướng Chính (`header`)
1. `🎯 Cấp độ (A1 - B2)`
2. `🎓 Không gian học (A1)`
3. **`📖 Chia động từ`** *(Nằm giữa "Không gian học" và "Từ vựng & Giống")*
4. **`🏷️ Từ vựng & Giống`** *(Nằm giữa "Chia động từ" và "Đấu trường & BXH")*
5. `🏆 Đấu trường & BXH`
6. `🗄️ Kiến trúc Python/SQL`

### 1.2. Mở rộng Tab `"📖 Chia động từ"` (Bổ sung Thì Hiện Tại `Präsens` + Quá Khứ Đơn `Präteritum`)
* Giữ nguyên toàn bộ 35 động từ đã có ở Bài 1 (P2) & Bài 2, đồng thời **mở rộng lên 45+ động từ** (bổ sung các động từ của Bài 3: **`liegen`** - nằm ở/tọa lạc, **`sprechen`** - nói ngôn ngữ [biến âm `e -> i`], **`reisen`** - đi du lịch [gốc `-s`], **`besuchen`** - thăm/ghé thăm, **`sehen`** - nhìn/xem [biến âm `e -> ie`], **`fahren`** - đi bằng phương tiện [biến âm `a -> ä`]).
* **Nâng cấp Thẻ Động Từ cho `sein` và `haben`**:
  * Bên cạnh bảng chia ở thì Hiện tại (**`Präsens`**), hiển thị thêm bảng chia ở thì Quá khứ đơn (**`Präteritum`**):
    * **`sein` (Präteritum)**: `ich war`, `du warst`, `er/sie/es war`, `wir waren`, `ihr wart`, `sie/Sie waren`.
    * **`haben` (Präteritum)**: `ich hatte`, `du hattest`, `er/sie/es hatte`, `wir hatten`, `ihr hattet`, `sie/Sie hatten`.
  * Tất cả các ngôi ở cả `Präsens` và `Präteritum` đều có nút loa `🔊` phát âm chuẩn giọng bản xứ `de-DE`.

### 1.3. Mở rộng Tab `"🏷️ Từ vựng & Giống"` (Bổ sung Quốc gia có Mạo từ, Danh lam thắng cảnh & Phương hướng)
* Giữ nguyên toàn bộ danh từ đồ dùng lớp học, động từ lớp học và các danh từ theo quy tắc hậu tố ở Bài 2.
* **Bổ sung thêm 3 bộ lọc chủ đề mới** trên thanh Filter Pills của Tab `"🏷️ Từ vựng & Giống"`:
  * `🌍 Quốc gia & Ngôn ngữ (Länder & Sprachen)`
  * `🏛️ Danh lam thắng cảnh (Sehenswürdigkeiten)`
  * `🧭 Phương hướng & Bản đồ (Himmelsrichtungen)`

---

## PHẦN 2: CỦNG CỐ & MỞ RỘNG KIẾN THỨC BÀI 1 (P1), BÀI 1 (P2) & BÀI 2 (KHÔNG XÓA BỚT, CHỈ BỔ SUNG DÀI THÊM)

Antigravity IDE cần kiểm tra và đảm bảo 3 bài học đầu tiên trong `deutsch_meister.db` có đầy đủ nội dung mở rộng sau:

### 2.1. Bổ sung mở rộng cho Bài 1 (P1): "Làm Quen Với Tiếng Đức, Bảng Chữ Cái và Đếm Số"
* **6 Học phần Lý thuyết đầy đủ**:
  1. **Bảng chữ cái (`Das Alphabet`) & 4 ký tự đặc biệt (`Ä, Ö, Ü, ß`)**: Hiển thị đầy đủ 30 nút bấm phát âm trực tiếp kèm phiên âm `[a:]`, `[be:]`, `[tse:]`, `[de:]`, `[e:]`, `[ɛf]`, `[ge:]`, `[ha:]`, `[i:]`, `[jɔt]`, `[ka:]`, `[ɛl]`, `[ɛm]`, `[ɛn]`, `[o:]`, `[pe:]`, `[ku:]`, `[ɛʁ]`, `[ɛs]`, `[te:]`, `[u:]`, `[faʊ]`, `[ve:]`, `[ɪks]`, `[ˈʏpsilɔn]`, `[tsɛt]`, `[ɛː]`, `[øː]`, `[yː]`, `[ɛsˈtsɛt]`.
  2. **12 Quy tắc Vàng trong Phát âm tiếng Đức**: `eu/äu` $\rightarrow$ `[ɔɪ]`; `ei/ai` $\rightarrow$ `[aɪ]`; `ie` $\rightarrow$ `[i:]` kéo dài; `sch` $\rightarrow$ `[ʃ]` tròn môi; `sp/st` đầu từ/âm tiết $\rightarrow$ `[ʃp]/[ʃt]`; `ch` sau `a, o, u, au` (Ach-Laut `[x]`) vs. `ch` sau `e, i, ä, ö, ü, eu, ei` (Ich-Laut `[ç]`); đuôi `-ig` cuối từ (`zwanzig, dreißig`) đọc là `[ɪç]`; nguyên âm + `h` câm kéo dài (`wohnen, gehen, sehen, Ihr`).
  3. **Mở rộng Hệ thống Đếm số từ `0` đến `1.000.000` (`Die Zahlen`)**:
     * Số `0` – `12` (bất quy tắc), `13` – `19` (`Đơn vị + zehn`, lưu ý `sechzehn` bỏ `s`, `siebzehn` bỏ `en`).
     * Các chục chẵn `20` – `90` (đuôi `-zig`, riêng `30` là `dreißig`, `20` là `zwanzig`, `60` là `sechzig`, `70` là `siebzig`).
     * Số ghép 2 chữ số `21` – `99`: `Đơn vị + und + Hàng chục` viết liền không dấu cách (số `1` dùng `ein-`, không có `s`: `einundzwanzig`).
     * Số hàng trăm (`100` – `999`) và hàng nghìn (`1000` – `9999`), cách đọc năm sinh (1998 = *neunzehnhundertachtundneunzig*, từ năm 2000 đọc theo nghìn: 2026 = *zweitausendsechsundzwanzig*).
  4. **Giao tiếp Chào hỏi & Tạm biệt theo khung giờ**: Phân biệt trang trọng (`Sie`: *Guten Morgen, Guten Tag, Guten Abend, Auf Wiedersehen*) và thân mật (`du`: *Hallo, Hi, Morgen, Tschüss, Bis bald, Bis später, Bis morgen*), cùng câu chúc ngủ ngon (*Gute Nacht*) và câu chúc trên điện thoại (*Auf Wiederhören*).
  5. **Hội thoại Giới thiệu bản thân**: Tên (*Ich heiße... / Mein Name ist... / Ich bin...*), quê quán (*Woher kommen Sie? – Ich komme aus...*), nơi ở (*Wo wohnen Sie? – Ich wohne in...*), hỏi thăm sức khỏe (*Wie geht es Ihnen? / Wie geht's? – Danke, sehr gut! Und Ihnen / dir?*).
  6. **50 câu hỏi luyện tập + Bộ sinh số ngẫu nhiên (`dynamic_number`)**.

### 2.2. Bổ sung mở rộng cho Bài 1 (P2): "Kaffee Oder Tee? - Cà Phê Hoặc Trà"
* **6 Học phần Lý thuyết đầy đủ**:
  1. **Hệ thống 9 Đại từ nhân xưng ở Cách 1 (`Nominativ`)**: Phân biệt rõ bộ 3 chữ `sie / Sie` (`sie` = cô ấy $+ -t$; `sie` = họ $+ -en$; `Sie` = Ngài/Các ngài $+ -en`) và cách quy đổi chủ ngữ danh từ ghép (`Anna und ich` = `wir`; `du und Peter` = `ihr`; `die Lehrerin` = `sie`; `das Café` = `es`).
  2. **Quy tắc Chia Động từ có quy tắc (`Regelmäßige Verben`)**: Tách gốc (`Verbstamm`) + đuôi `-e, -st, -t, -en, -t, -en` (`machen, wohnen, kommen, trinken, zahlen, lernen, hören, spielen, kaufen, leben, gehen, fragen, sagen`).
  3. **2 Nhóm Động từ có quy tắc đặc biệt về phát âm**:
     * Nhóm gốc tận cùng bằng `-s, -ß, -z` (`heißen, tanzen, reisen, sitzen`): Ngôi `du` chỉ thêm `-t` (nên `du` và `er/sie/es` viết giống hệt nhau: `du heißt = er heißt`, `du reist = er reist`).
     * Nhóm gốc tận cùng bằng `-t, -d` hoặc `-chn, -ffn, -tm` (`arbeiten, mieten, antworten, kosten, finden, warten, öffnen`): Thêm âm đệm `-e-` ở ngôi `du` (`-est`: *arbeitest, mietest*), `er/sie/es` (`-et`: *arbeitet, mietet*) và `ihr` (`-et`: *arbeitet, mietet*).
  4. **Động từ Bất quy tắc & Biến âm gốc (`Unregelmäßige Verben & Vokalwechsel`)**:
     * Bộ đôi nền tảng `sein` (*bin, bist, ist, sind, seid, sind*) & `haben` (*habe, hast, hat, haben, habt, haben*).
     * Động từ biến âm ở ngôi `du` và `er/sie/es`: Nhóm `e -> ie` (`lesen -> liest`, `sehen -> sieht`), nhóm `e -> i` (`nehmen -> nimmst/nimmt`, `sprechen -> sprichst/spricht`, `essen -> isst`, `geben -> gibst/gibt`, `helfen -> hilfst/hilft`), nhóm `a -> ä` (`fahren -> fährst/fährt`, `schlafen -> schläfst/schläft`).
  5. **Động từ khuyết thiếu `möchten` & Cấu trúc Khung câu (`Satzklammer`)**:
     * Ngôi `ich` và `er/sie/es` của `möchten` giống hệt nhau (`ich möchte = er/sie/es möchte`).
     * Khung câu: `möchten` đứng vị trí số 2 chia theo chủ ngữ, đẩy động từ chính về cuối câu ở dạng nguyên mẫu (*Was **möchten** Sie **trinken**? $\rightarrow$ Ich **möchte** Kakao **trinken**.*).
  6. **Từ vựng Đồ uống, Giới từ `mit/ohne`, Lượng từ `viel/wenig` & Hội thoại Thanh toán tại Quán Café (`1 Euro = 100 Cent`)**:
     * Hỏi thanh toán: *Ich möchte (bitte) zahlen. / Wir möchten bitte zahlen.*
     * Phục vụ hỏi: *Zusammen oder getrennt?* (Thanh toán chung hay riêng?) $\rightarrow$ *Zusammen, bitte! / Getrennt, bitte!*
     * Báo giá tiền: *Das macht 3,99 Euro.* (Đọc là: *drei Euro neunundneunzig*).

### 2.3. Bổ sung mở rộng cho Bài 2: "Sprache im Kurs - Động Từ và Giống (der / die / das)"
* **6 Học phần Lý thuyết đầy đủ**:
  1. **Bản chất Mạo từ (`Artikel`), 3 Giống (`Maskulinum, Femininum, Neutrum`), Số nhiều (`Plural`) & Tổng quan 4 Cách (`Nominativ, Genitiv, Dativ, Akkusativ`)**.
  2. **Bảng Quy tắc Vàng nhận diện Giống qua Hậu tố & Nhóm nghĩa**:
     * **`der`**: `-ant, -ent, -ich, -ismus, -ist, -ast, -ling, -or, -er` + Tháng, Thứ, Mùa, Hướng, Thời tiết, Nghề nghiệp nam, Hãng xe hơi (`der BMW, der Mercedes`).
     * **`die`**: `-heit, -keit, -schaft, -ung, -ie, -anz, -enz, -ion, -tät, -ik, -ur, -in, -e` + Đa số Cây, Hoa, Số đếm làm danh từ (`die Eins`).
     * **`das`**: `-ment` (**Ngoại lệ: `der Moment`**), `-um, -tum, -chen, -lein, -ma, -em`, `-nis` (**Ngoại lệ: `die Erlaubnis`**) + Động từ nguyên mẫu viết hoa (`das Essen, das Lesen`), Tính từ hóa danh từ (`das Gute`), Nguyên tố hóa học/Kim loại (`das Eisen, das Gold`), Màu sắc & Ngôn ngữ.
     * **Quy tắc Danh từ ghép (`Komposita`)**: Giống và dạng số nhiều của danh từ ghép luôn quyết định bởi **từ đứng cuối cùng** (`die Wörter` + `das Buch` = **`das Wörterbuch`**; `das Land` + `die Karte` = **`die Landkarte`**).
  3. **18 Danh từ Đồ dùng Lớp học (`Sprache im Kurs`) & 5 Quy tắc tạo Số nhiều (`-e / ¨-e`, `-er / ¨-er`, `-(e)n`, `-s`, giữ nguyên `-`)**.
  4. **Động từ & 6 Mẫu câu Giao tiếp Lớp học**: `heißen, verstehen, können, wiederholen, buchstabieren, anschreiben` (*Wie heißt das auf Deutsch? / Was ist das auf Deutsch? / Entschuldigung, wie bitte? / Das verstehe ich nicht. Können Sie das bitte wiederholen / buchstabieren / anschreiben?*).
  5. **Bảng đối chiếu 3 cột Mạo từ ở Cách 1 (`Nominativ`)**: Xác định (`der, die, das, die`) $\rightarrow$ Bất định (`ein, eine, ein, —`) $\rightarrow$ Phủ định (`kein, keine, kein, keine`).
  6. **Thực hành Hỏi - Đáp Đồ vật & Sở hữu với `von + Tên riêng`**: *Ist das ein Kuli? $\rightarrow$ Ja, das ist der Kuli von Anna. / Ist das eine Brille? $\rightarrow$ Nein, das ist keine Brille. Das ist eine Landkarte.*

---

## PHẦN 3: NỘI DUNG CHI TIẾT BÀI 3 — "ĐỊA DANH - PHƯƠNG HƯỚNG - PRÄTERITUM (STÄDTE – LÄNDER – SPRACHEN)"

Tạo tệp **`seed_a1_b3.py`** để nạp **Bài 3: "Städte – Länder – Sprachen: Địa Danh, Phương Hướng & Thì Quá Khứ Đơn (Präteritum)"** vào bảng `lessons` trong `deutsch_meister.db`. Nội dung lý thuyết của Bài 3 phải được trình bày **thật dài, chi tiết, trực quan thành 7 Học phần chuyên sâu** dưới đây:

---

### HỌC PHẦN 1: QUỐC GIA (`DIE LÄNDER`), NGÔN NGỮ (`DIE SPRACHEN`) & QUY TẮC MẠO TỪ ĐỊA LÝ

Trong tiếng Đức, các quốc gia được chia thành **2 nhóm ngữ pháp cực kỳ quan trọng**: Nhóm **không có mạo từ** (chiếm khoảng 85% các nước trên thế giới) và Nhóm **bắt buộc phải đi kèm mạo từ** (`die`, `der`, hoặc `die` số nhiều).

#### 1.1. Bảng 13 Quốc gia Không dùng Mạo từ & Ngôn ngữ tương ứng (Theo sát bảng viết + Mở rộng)
Khi nói *"đến từ"* dùng giới từ **`aus`**, khi nói *"ở tại"* dùng giới từ **`in`**, và khi nói *"đi đến"* dùng giới từ **`nach`** (không cần mạo từ ở giữa):

| STT | Quốc gia (`Das Land`) | Nghĩa tiếng Việt | Ngôn ngữ chính (`Die Sprache`) | Nghĩa tiếng Việt | Câu ví dụ chuẩn (Nguồn gốc, Nơi ở & Ngôn ngữ) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **`Deutschland`** | Nước Đức | **`Deutsch`** | Tiếng Đức | *Ich komme aus **Deutschland** und spreche **Deutsch**.* |
| 2 | **`Österreich`** | Nước Áo | **`Deutsch`** | Tiếng Đức | *Wien liegt in **Österreich**. Man spricht dort **Deutsch**.* |
| 3 | **`Italien`** | Nước Ý | **`Italienisch`** | Tiếng Ý | *Pisa ist in **Italien**. Sie spricht gut **Italienisch**.* |
| 4 | **`Spanien`** | Tây Ban Nha | **`Spanisch`** | Tiếng Tây Ban Nha | *Carlos kommt aus **Spanien** und spricht **Spanisch**.* |
| 5 | **`Griechenland`** | Hy Lạp | **`Griechisch`** | Tiếng Hy Lạp | *Athen ist in **Griechenland**. Er lernt **Griechisch**.* |
| 6 | **`Frankreich`** | Nước Pháp | **`Französisch`** | Tiếng Pháp | *Der Eiffelturm ist in **Frankreich**. Wir sprechen **Französisch**.* |
| 7 | **`Großbritannien / England`** | Vương quốc Anh / Nước Anh | **`Englisch`** | Tiếng Anh | *Big Ben ist in **England**. Sprichst du **Englisch**?* |
| 8 | **`Niederlande`** *(thường dùng `die Niederlande`)* | Hà Lan | **`Niederländisch`** | Tiếng Hà Lan | *Amsterdam ist in Holland / in den **Niederlanden**. Man spricht **Niederländisch**.* |
| 9 | **`Polen`** | Ba Lan | **`Polnisch`** | Tiếng Ba Lan | *Mein Freund kommt aus **Polen** und spricht **Polnisch**.* |
| 10 | **`Tschechien`** | Cộng hòa Séc | **`Tschechisch`** | Tiếng Séc | *Prag liegt in **Tschechien**. Dort spricht man **Tschechisch**.* |
| 11 | **`Russland`** | Nước Nga | **`Russisch`** | Tiếng Nga | *Moskau ist in **Russland**. Anna spricht **Russisch**.* |
| 12 | **`China`** | Trung Quốc | **`Chinesisch`** | Tiếng Trung Quốc | *Frau Wang kommt aus **China** und spricht **Chinesisch**.* |
| 13 | **`Vietnam`** | Việt Nam | **`Vietnamesisch`** | Tiếng Việt | *Ich komme aus **Vietnam** und spreche **Vietnamesisch**.* |

> 💡 **Ghi chú Ngữ pháp & Chính tả về Tên Ngôn ngữ**:
> * Hầu hết tên ngôn ngữ trong tiếng Đức đều kết thúc bằng hậu tố **`-isch`** (đọc là `[ɪʃ]`).
> * Khi dùng như một **Danh từ** chỉ môn học hoặc ngôn ngữ độc lập (*Ich lerne Deutsch / Vietnamesisch*), chữ cái đầu **viết hoa**. Khi dùng như một **Tính từ / Trạng từ** đi sau động từ `sprechen` hoặc bổ nghĩa (*niederländisch, englisch*), trong tiếng Đức hiện đại có thể viết hoa hoặc viết thường, nhưng ở trình độ A1–B1 khi liệt kê tên ngôn ngữ chuẩn luôn viết hoa (**`Deutsch, Englisch, Französisch, Vietnamesisch...`**).
> * Động từ đi kèm với ngôn ngữ là **`sprechen`** (nói — động từ bất quy tắc biến âm `e` $\rightarrow$ `i` ở ngôi `du` và `er/sie/es`):
>   * `ich spreche` | **`du sprichst`** | **`er/sie/es spricht`** | `wir sprechen` | `ihr sprecht` | `sie/Sie sprechen`.

---

#### 1.2. Nhóm Quốc gia ĐẶC BIỆT Bắt buộc có Mạo từ (`Länder mit Artikel`)
Không giống như *Vietnam* hay *Deutschland*, một số quốc gia bắt buộc phải có mạo từ (`die`, `der`, hoặc `die` số nhiều) đi kèm. Khi kết hợp với giới từ **`aus`** (*đến từ*) hoặc **`in`** (*ở tại*), mạo từ của các nước này sẽ **biến đổi theo Cách 3 (`Dativ`)**:

| Phân nhóm Giống | Tên Quốc gia gốc (`Nominativ`) | Nghĩa tiếng Việt | Ngôn ngữ sử dụng (`Sprache`) | Đến từ (`aus + Dativ`) | Ở tại (`in + Dativ`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Giống cái (`die`)** | **`die Schweiz`** | Thụy Sỹ | **`Deutsch, Französisch, Italienisch`** *(3 ngôn ngữ chính)* | `aus` **`der`** `Schweiz` | `in` **`der`** `Schweiz` |
| **1. Giống cái (`die`)** | **`die Türkei`** | Thổ Nhĩ Kỳ | **`Türkisch`** (Tiếng Thổ Nhĩ Kỳ) | `aus` **`der`** `Türkei` | `in` **`der`** `Türkei` |
| **1. Giống cái (`die`)** | **`die Slowakei`** | Slovakia | **`Slowakisch`** (Tiếng Slovakia) | `aus` **`der`** `Slowakei` | `in` **`der`** `Slowakei` |
| **2. Giống đực (`der`)** | **`der Iran`** | Iran | **`Persisch`** (Tiếng Ba Tư) | `aus` **`dem`** `Iran` | **`im`** *(in dem)* `Iran` |
| **3. Số nhiều (`die Pl.`)** | **`die USA`** *(Plural)* | Hợp chủng quốc Hoa Kỳ (Mỹ) | **`Englisch`** (Tiếng Anh) | `aus` **`den`** `USA` | `in` **`den`** `USA` |
| **3. Số nhiều (`die Pl.`)** | **`die Niederlande`** *(Plural)* | Hà Lan | **`Niederländisch`** (Tiếng Hà Lan) | `aus` **`den`** `Niederlanden` | `in` **`den`** `Niederlanden` |

> 🔥 **Mẹo Vàng Ghi Nhớ cho Học Viên A1**:
> * Mọi quốc gia có hậu tố **`-ei`** (*die Türkei, die Slowakei, die Mongolei*) luôn luôn mang giống cái (**`die`**).
> * Thụy Sỹ (**`die Schweiz`**) là quốc gia đa ngôn ngữ nổi tiếng ở trung tâm châu Âu với 4 ngôn ngữ chính thức, trong đó 3 ngôn ngữ phổ biến nhất cần nhớ trong bài là: **`Deutsch`**, **`Französisch`** và **`Italienisch`**.
> * Với **`der Iran`**, ngôn ngữ chính thức không phải là "Iranisch" mà là **`Persisch`** (tiếng Ba Tư).
> * Với **`die USA`** (số nhiều), luôn nói: *"Die Lehrerin ist **aus den USA**"* hoặc *"New York liegt **in den USA**."*

---

### HỌC PHẦN 2: DANH LAM THẮNG CẢNH CHÂU ÂU (`SEHENSWÜRDIGKEITEN IN EUROPA`)

Danh từ **`die Sehenswürdigkeit`** (số nhiều: **`die Sehenswürdigkeiten`**) có nghĩa là *danh lam thắng cảnh / địa điểm tham quan đáng xem* (ghép từ `sehen` = nhìn/xem + `würdig` = xứng đáng + hậu tố `-keit` = giống cái `die`).

#### 2.1. Bảng 7 Danh lam Thắng cảnh Biểu tượng của Châu Âu (Kèm Giống, Thành phố & Quốc gia)

| STT | Danh lam thắng cảnh (`Sehenswürdigkeit`) | Giống & Giải thích cấu tạo từ | Nghĩa tiếng Việt | Thành phố (`Stadt`) | Quốc gia (`Land`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **`die Akropolis`** | **`die`** *(Giống cái)* | Thành cổ Akropolis | **`Athen`** (Athens) | **`Griechenland`** (Hy Lạp) |
| 2 | **`der Big Ben`** | **`der`** *(Giống đực — theo `der Turm`)* | Tháp đồng hồ Big Ben | **`London`** | **`England / Großbritannien`** (Anh) |
| 3 | **`der Eiffelturm`** | **`der`** *(Danh từ ghép với `der Turm` = ngọn tháp)* | Tháp Eiffel (Ép-phen) | **`Paris`** | **`Frankreich`** (Pháp) |
| 4 | **`der Schiefe Turm`** *(trên bảng: `der Schiefel Turm`)* | **`der`** (`schief` = nghiêng + `der Turm` = tháp) | Tháp nghiêng (Pisa) | **`Pisa`** | **`Italien`** (Ý) |
| 5 | **`der Prater`** | **`der`** *(Giống đực)* | Công viên giải trí Prater | **`Wien`** (Viên) | **`Österreich`** (Áo) |
| 6 | **`das Brandenburger Tor`** | **`das`** *(Danh từ ghép lấy giống theo `das Tor` = cái cổng)* | Cổng Brandenburg | **`Berlin`** | **`Deutschland`** (Đức) |
| 7 | **`der Rote Platz`** | **`der`** (`rot` = đỏ + `der Platz` = quảng trường) | Quảng trường Đỏ | **`Moskau`** (Mát-xcơ-va) | **`Russland`** (Nga) |

#### 2.2. Ba Mẫu Câu Hỏi – Đáp kinh điển về Địa danh & Thắng cảnh
Khi nhìn vào bức ảnh một công trình nổi tiếng, người Đức sử dụng chuỗi 3 câu hỏi liên hoàn sau:

1. **Hỏi tên địa danh (`Was ist das?`)**:
   * **Hỏi**: **`Was ist das?`** *(Đây là cái gì / công trình gì?)*
   * **Trả lời**: **`Das ist die Akropolis.`** *(Đó là thành cổ Akropolis.)* / **`Das ist das Brandenburger Tor.`** / **`Das ist der Eiffelturm.`** *(Lưu ý giữ nguyên mạo từ `der / die / das` ở Cách 1 - Nominativ sau `Das ist...`)*.
2. **Hỏi vị trí thành phố kèm tiểu từ biểu cảm `denn` (`Wo ist denn das?`)**:
   * **Hỏi**: **`Wo ist denn das?`** *(Thế cái đó nằm ở đâu vậy nhỉ?)*
   * **Trả lời**: **`Das ist in Athen.`** *(Nó nằm ở thành phố Athens.)* / **`Das ist in Paris.`** / **`Das ist in Wien.`**
   * 💡 *Giải thích tiểu từ **`denn`**:* Trong câu hỏi tiếng Đức, từ **`denn`** không dịch cứng sang tiếng Việt mà đóng vai trò là **tiểu từ ngữ khí (`Modalpartikel`)**, giúp câu hỏi nghe tự nhiên, thân thiện và thể hiện sự tò mò, hào hứng của người hỏi (*"Thế nó ở đâu vậy?"*).
3. **Hỏi quốc gia bằng từ để hỏi `In welchem Land...?`**:
   * **Hỏi**: **`In welchem Land ist das?`** *(Cái đó / Thành phố đó nằm ở đất nước nào?)*
   * **Trả lời**: **`Athen ist in Griechenland.`** *(Athens nằm ở Hy Lạp.)* / **`Wien ist in Österreich.`** / **`Moskau ist in Russland.`**

---

### HỌC PHẦN 3: ĐỊNH HƯỚNG TRÊN BẢN ĐỒ (`ORIENTIERUNG AUF DER LANDKARTE`) & HỆ THỐNG 8 PHƯƠNG HƯỚNG

Để mô tả vị trí địa lý của một thành phố hay vùng miền trên bản đồ (`auf der Landkarte`), tiếng Đức sử dụng hệ thống **8 phương hướng (4 hướng chính + 4 hướng phụ)** và vị trí **trung tâm (`die Mitte`)** kết hợp với động từ **`liegen`** (*nằm ở / tọa lạc ở*).

#### 3.1. Sơ đồ La bàn 8 Phương hướng: Danh từ (`der`) vs. Tính từ chỉ hướng (`-lich`)

> ⚠️ **2 Quy tắc Vàng về Phương hướng trong tiếng Đức**:
> 1. **Mọi danh từ chỉ phương hướng đều mang giống đực (`der`)** (đã học ở Bài 2). Khi muốn nói *"ở phía..."*, ta dùng giới từ `in` + `dem` (Cách 3 - Dativ) viết tắt thành **`im`** + **Danh từ phương hướng** + **`von`** (*của*).
> 2. **Khi chuyển sang Tính từ / Trạng từ chỉ hướng**, ta thêm hậu tố **`-lich`** vào gốc từ, **viết thường** và **thêm dấu Umlaut (`¨`)** vào nguyên âm gốc (`o -> ö`, `u -> ü`): `Norden` $\rightarrow$ **`nördlich`**, `Osten` $\rightarrow$ **`östlich`**, `Süden` $\rightarrow$ **`südlich`**, `Westen` $\rightarrow$ **`westlich`**.
> 3. **Thứ tự ghép 4 hướng phụ (Đông Bắc, Đông Nam, Tây Bắc, Tây Nam)**: Ngược lại với tiếng Việt (tiếng Việt lấy *Đông / Tây* làm gốc trước), **tiếng Đức lấy *Bắc (`Nord-`) / Nam (`Süd-`)* đặt lên trước**, sau đó mới ghép với *Đông (`-osten`) / Tây (`-westen`)*!

| Ký hiệu | Phương hướng (Tiếng Việt) | Danh từ Phương hướng (`der`) | Cụm giới từ (`im ... von`) | Tính từ Phương hướng (`...lich von`) | Lưu ý biến âm & ghép từ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **B** | **Phía Bắc (Miền Bắc)** | **`der Norden`** | **`im Norden von`** | **`nördlich von`** | `o` $\rightarrow$ **`ö`** (`nördlich`) |
| **N** | **Phía Nam (Miền Nam)** | **`der Süden`** | **`im Süden von`** | **`südlich von`** | Giữ nguyên **`ü`** (`südlich`) |
| **Đ** | **Phía Đông (Miền Đông)** | **`der Osten`** | **`im Osten von`** | **`östlich von`** | `o` $\rightarrow$ **`ö`** (`östlich`) |
| **T** | **Phía Tây (Miền Tây)** | **`der Westen`** | **`im Westen von`** | **`westlich von`** | Giữ nguyên `e` (`westlich`) |
| **ĐB** | **Đông Bắc** | **`der Nordosten`** | **`im Nordosten von`** | **`nordöstlich von`** | `Nord` (Bắc) + `osten`/`östlich` (Đông) |
| **ĐN** | **Đông Nam** | **`der Südosten`** | **`im Südosten von`** | **`südöstlich von`** | `Süd` (Nam) + `osten`/`östlich` (Đông) |
| **TB** | **Tây Bắc** | **`der Nordwesten`** | **`im Nordwesten von`** | **`nordwestlich von`** | `Nord` (Bắc) + `westen`/`westlich` (Tây) |
| **TN** | **Tây Nam** | **`der Südwesten`** | **`im Südwesten von`** | **`südwestlich von`** | `Süd` (Nam) + `westen`/`westlich` (Tây) |
| **TT** | **Ở giữa / Miền Trung** | **`die Mitte`** *(Giống cái!)* | **`in der Mitte von`** | *(Không dùng dạng `-lich`)* | Vì là **`die Mitte`** nên ở Dativ đổi thành **`in der Mitte von`**! |

---

#### 3.2. Hai Cách Trả Lời Câu Hỏi Vị Trí Địa Lý (`Wo liegt ...?`)
Động từ **`liegen`** (nằm ở / tọa lạc ở) là động từ có quy tắc ở thì hiện tại:
* `ich liege` | `du liegst` | **`er / sie / es (Thành phố) liegt`** | `wir liegen` | `ihr liegt` | `sie / Sie liegen`.

Khi được hỏi **`Wo liegt + [Tên thành phố]?`**, người học có thể trả lời theo **2 cách tương đương** (trừ trường hợp *in der Mitte*):

* **Ví dụ mẫu (`Hai Phong` — Đông Bắc Việt Nam)**:
  * **Câu hỏi**: **`Wo liegt Hai Phong?`** *(Hải Phòng nằm ở đâu?)*
  * **Cách 1 (Dùng Cụm Danh từ: `liegt + im + Danh từ hướng + von`)**:
    👉 **`Hai Phong liegt im Nordosten von Vietnam.`**
  * **Cách 2 (Dùng Tính từ: `liegt + Tính từ hướng (-lich) + von` — tuyệt đối KHÔNG có `im`!)**:
    👉 **`Hai Phong liegt nordöstlich von Vietnam.`**

* **3 Tình huống thực hành chuẩn trên bảng (`Ha Noi`, `Long An`, `Da Nang`)**:
  1. **Tình huống 1 (`Ha Noi` — Miền Bắc)**:
     * Hỏi: **`Wo liegt Ha Noi?`**
     * Cách 1 (Danh từ): **`Ha Noi liegt im Norden von Vietnam.`**
     * Cách 2 (Tính từ): **`Ha Noi liegt nördlich von Vietnam.`**
  2. **Tình huống 2 (`Long An` — Miền Nam)**:
     * Hỏi: **`Wo liegt Long An?`**
     * Cách 1 (Danh từ): **`Long An liegt im Süden von Vietnam.`**
     * Cách 2 (Tính từ): **`Long An liegt südlich von Vietnam.`**
  3. **Tình huống 3 (`Da Nang` — Miền Trung / Ở giữa)**:
     * Hỏi: **`Wo liegt Da Nang?`**
     * Trả lời duy nhất: **`Da Nang liegt in der Mitte von Vietnam.`** *(Đà Nẵng nằm ở miền Trung của Việt Nam — Lưu ý: vì `die Mitte` mang giống cái nên dùng `in der Mitte`, không dùng `im`!)*.

---

### HỌC PHẦN 4: BA CẤU TRÚC CÂU TRỌNG TÂM & HỆ THỐNG 9 TỪ ĐỂ HỎI (`W-FRAGEN`)

#### 4.1. Tổng hợp 3 Cấu trúc Câu Cốt lõi trong Tiếng Đức
1. **Câu Trần thuật (`Aussagesatz`: `S + V + O...`)**:
   * Động từ chia theo chủ ngữ **luôn luôn đứng ở vị trí thứ 2 (Position 2)**.
   * Ví dụ: **`Ich`** *(S - Vị trí 1)* **`komme`** *(V - Vị trí 2)* **`aus Vietnam.`** *(O/Trạng ngữ)*.
2. **Câu hỏi có Từ để hỏi (`W-Frage`: `W-Wort + V + S ...?`)**:
   * Từ để hỏi (`W-Wort`) đứng ở vị trí số 1, **Động từ chia theo chủ ngữ vẫn đứng ở vị trí số 2**, Chủ ngữ (`S`) lùi về vị trí số 3.
   * Ví dụ: **`Woher`** *(W-Wort - Vị trí 1)* **`kommen`** *(V - Vị trí 2)* **`Sie`** *(S - Vị trí 3)* **`?`**
3. **Câu hỏi Có / Không (`Ja/Nein-Frage`: `V + S + ...?`)**:
   * Không có từ để hỏi, **đẩy Động từ chia theo chủ ngữ lên thẳng vị trí số 1 (đầu câu)** và lên giọng ở cuối câu!
   * Ví dụ: **`Kommen`** *(V - Vị trí 1)* **`Sie`** *(S - Vị trí 2)* **`aus Vietnam?`**
     * Trả lời khẳng định (`Ja`): **`Ja, ich komme aus Vietnam.`**
     * Trả lời phủ định (`Nein`): **`Nein, ich komme aus Deutschland.`** *(Hoặc: Nein, ich komme nicht aus Vietnam.)*

#### 4.2. Bảng 9 Từ Để Hỏi `W-Fragen` Cần Thuộc Lòng Ở Trình Độ A1

| STT | Từ để hỏi (`W-Wort`) | Nghĩa tiếng Việt | Chức năng ngữ pháp & Câu ví dụ minh họa |
| :--- | :--- | :--- | :--- |
| 1 | **`Wer`** | **Ai?** *(Chủ ngữ - Cách 1)* | Hỏi người: *`Wer` ist das? – Das ist Frau Schiller. / `Wer` ist sie? – Sie ist Lehrerin.* |
| 2 | **`Wo`** | **Ở đâu?** *(Vị trí tĩnh)* | Hỏi nơi chốn hiện tại: *`Wo` wohnen Sie? – Ich wohne in Hai Phong. / `Wo` liegt Hanoi?* |
| 3 | **`Woher`** | **Từ đâu đến?** *(Nguồn gốc)* | Hỏi quê quán, xuất xứ (đi với `aus`): *`Woher` kommst du? – Ich komme aus Vietnam.* |
| 4 | **`Wohin`** | **Đến đâu?** *(Hướng di chuyển)* | Hỏi điểm đến (đi với `nach / in`): *`Wohin` fahren Sie? – Ich fahre nach Berlin.* |
| 5 | **`Was`** | **Cái gì?** | Hỏi sự vật, hành động, nghề nghiệp: *`Was` ist das? / `Was` macht er? / `Was` trinken Sie?* |
| 6 | **`Wie`** | **Như thế nào? / Bao nhiêu?** | Hỏi tên, tính chất, sức khỏe: *`Wie` heißen Sie? / `Wie` geht es dir? / `Wie` bitte?* |
| 7 | **`Wann`** | **Khi nào? / Bao giờ?** | Hỏi thời gian: *`Wann` beginnt der Deutschkurs? – Am Montag.* |
| 8 | **`Warum`** | **Tại sao? / Vì sao?** | Hỏi lý do: *`Warum` lernst du Deutsch? – Für das Studium in Deutschland.* |
| 9 | **`Welch-`** *(Welcher / Welche / Welches / In welchem...)* | **... nào?** *(Lựa chọn)* | Đi trước danh từ và chia đuôi theo giống/cách: *`In welchem` Land ist das? / `Welche` Sprache sprichst du?* |

---

#### 4.3. Thực hành Chuyển đổi từ Câu Trần thuật sang `W-Frage` và `Ja/Nein-Frage` (4 Bài mẫu trên bảng)

| STT | Câu Trần thuật gốc (`Aussagesatz`) | Chuyển sang Câu hỏi `W-Frage` | Chuyển sang Câu hỏi `Ja/Nein-Frage` | Giải thích từ vựng & Ngữ pháp |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **`Ich heiße Anna.`** *(Tôi tên là Anna.)* | **`Wie heißen Sie?`** *(hoặc: `Wie heißt du?`)* | **`Heißen Sie Anna?`** *(hoặc: `Heißt du Anna?`)* | Khi hỏi tên với động từ `heißen`, bắt buộc dùng từ để hỏi **`Wie`** (*Như thế nào*), không dùng *Was*! |
| **2** | **`Ich wohne in Hai Phong.`** *(Tôi sống ở Hải Phòng.)* | **`Wo wohnen Sie?`** *(hoặc: `Wo wohnst du?`)* | **`Wohnen Sie in Hai Phong?`** *(hoặc: `Wohnst du in Hai Phong?`)* | Cụm `in Hai Phong` chỉ nơi ở cố định $\rightarrow$ dùng từ để hỏi **`Wo`** (*Ở đâu*). |
| **3** | **`Er macht die Hausaufgaben.`** *(Anh ấy làm bài tập về nhà.)* | **`Was macht er?`** *(Anh ấy đang làm cái gì?)* | **`Macht er die Hausaufgaben?`** *(Anh ấy có làm bài tập về nhà không?)* | Danh từ **`die Hausaufgaben`** *(số nhiều: bài tập về nhà)*. Hỏi cho hành động/sự vật $\rightarrow$ dùng **`Was`**. |
| **4** | **`Sie ist Lehrerin.`** *(Cô ấy là giáo viên.)* | **`Wer ist sie?`** *(Cô ấy là ai? / hoặc `Was ist sie von Beruf?`)* | **`Ist sie Lehrerin?`** *(Cô ấy có phải là giáo viên không?)* | Khi nói nghề nghiệp sau động từ `sein` (*Sie ist Lehrerin*), tiếng Đức **bỏ mạo từ `eine`**. Hỏi định danh người $\rightarrow$ dùng **`Wer`**. |

---

### HỌC PHẦN 5: THÌ QUÁ KHỨ ĐƠN (`PRÄTERITUM`) CỦA ĐỘNG TỪ `"SEIN"` (VÀ MỞ RỘNG `"HABEN"`)

#### 5.1. Khái niệm Thì `Präteritum` là gì?
* **`Das Präteritum`** là **Thì Quá khứ đơn** (hay còn gọi là **Quá khứ văn viết**).
* Trong tiếng Đức giao tiếp hàng ngày, mặc dù đa số các động từ thường sẽ dùng thì Hiện tại hoàn thành (*Perfekt*) để kể chuyện quá khứ, nhưng riêng **động từ `sein` (thì, là, ở)**, **động từ `haben` (có)** và các động từ khuyết thiếu thì người Đức **luôn ưu tiên dùng thì `Präteritum` trong cả văn nói lẫn văn viết** vì ngắn gọn và tự nhiên hơn rất nhiều!

#### 5.2. Bảng Đối chiếu Chia Động từ `"sein"` (và mở rộng `"haben"`) ở `Präsens` vs. `Präteritum`

| Ngôi nhân xưng (`Personalpronomen`) | `"sein"` ở Hiện tại (`Präsens`) | `"sein"` ở Quá khứ đơn (`Präteritum`) | `"haben"` ở Hiện tại (`Präsens`) | `"haben"` ở Quá khứ đơn (`Präteritum` - *Mở rộng*) | Nghĩa ở thì Quá khứ (`Präteritum`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`ich`** *(tôi)* | `bin` | **`war`** | `habe` | **`hatte`** | Tôi đã ở / đã là / đã có |
| **`du`** *(bạn)* | `bist` | **`warst`** | `hast` | **`hattest`** | Bạn đã ở / đã là / đã có |
| **`er / sie / es`** *(anh ấy / cô ấy / nó)* | `ist` | **`war`** *(Giống hệt ngôi `ich`!)* | `hat` | **`hatte`** *(Giống hệt ngôi `ich`!)* | Anh/cô ấy/nó đã ở / đã là / đã có |
| **`wir`** *(chúng tôi)* | `sind` | **`waren`** | `haben` | **`hatten`** | Chúng tôi đã ở / đã là / đã có |
| **`ihr`** *(các bạn)* | `seid` | **`wart`** | `habt` | **`hattet`** | Các bạn đã ở / đã là / đã có |
| **`sie / Sie`** *(họ / Ngài)* | `sind` | **`waren`** | `haben` | **`hatten`** | Họ / Ngài đã ở / đã là / đã có |

> 📌 **Quy luật Cực Dễ Nhớ của `sein` ở thì `Präteritum`**:
> 1. Gốc quá khứ của `sein` là **`war-`**.
> 2. **Ngôi thứ nhất số ít (`ich`) và Ngôi thứ ba số ít (`er / sie / es`) trong thì `Präteritum` LUÔN LUÔN GIỐNG HỆT NHAU**:
>    * `ich` **`war`** = `er / sie / es` **`war`** *(Tuyệt đối không có `ware` hay `wart` cho ngôi `er/sie/es`!)*.
> 3. Các ngôi còn lại gắn đuôi quen thuộc vào gốc `war-`:
>    * `du` $\rightarrow$ `war` + `-st` = **`warst`**
>    * `wir` & `sie/Sie` $\rightarrow$ `war` + `-en` = **`waren`**
>    * `ihr` $\rightarrow$ `war` + `-t` = **`wart`**

#### 5.3. Các Trạng từ chỉ Thời gian đi kèm với `Präteritum` vs. `Präsens`
* **Dấu hiệu nhận biết thì Quá khứ (`Präteritum` $\rightarrow$ dùng `war / warst / waren / wart`)**:
  * **`gestern`**: hôm qua (*Gestern **waren** Paula und ich in Haiphong.*)
  * **`vorgestern`**: hôm kia
  * **`früher`**: trước đây / ngày xưa
  * **`letztes Jahr` / `letzte Woche`**: năm ngoái / tuần trước
  * **`schon`** *(trong câu hỏi/trả lời trải nghiệm)*: đã từng / rồi (*`Warst` du **schon** in Hanoi?* $\rightarrow$ *Ja, ich **war schon** in Hanoi.*)
* **Dấu hiệu nhận biết thì Hiện tại (`Präsens` $\rightarrow$ dùng `bin / bist / ist / sind / seid`)**:
  * **`heute`**: hôm nay (*`Heute sind` wir am Do Son Meer.*)
  * **`jetzt`**: bây giờ

#### 5.4. Mẫu Hội thoại Hỏi Trải nghiệm Du lịch với `"Warst du schon in ...?"`
* **Câu hỏi**: **`Warst du schon in Hanoi?`** *(Bạn đã từng đến / ở Hà Nội chưa?)*
  * **Trả lời Khẳng định (`Ja`)**: **`Ja, ich war schon in Hanoi.`** *(Rồi, mình đã từng ở Hà Nội rồi.)*
  * **Trả lời Phủ định (`Nein`) + Hỏi lại vị trí**:
    * **`Nein, wo ist denn das?`** *(Chưa, thế nó nằm ở đâu vậy?)*
    * **`Hanoi liegt im Norden von Vietnam.`** *(Hà Nội nằm ở miền Bắc của Việt Nam.)*

---

### HỌC PHẦN 6: PHÂN TÍCH HỘI THOẠI ĐIỀN TỪ & BƯU THIẾP DU LỊCH HẢI PHÒNG (THEO SÁT BẢNG VIẾT)

#### 6.1. Bài tập Hội thoại Điền Động từ (`Carlos & Người bạn`)
* **Ngân hàng từ cho sẵn trên bảng**: `ist` – `ist` – `ist` – `komme` – `komme` – `kommst` – `kommst` – `warst`
* **Đoạn hội thoại hoàn chỉnh & Giải thích ngữ pháp**:
  * **A**: *Carlos, woher **`kommst`** du?* (Chủ ngữ `du` $\rightarrow$ chia `kommst`).
  * **Carlos**: *Ich **`komme`** aus Wien. Das **`ist`** in Österreich. Und du, woher **`kommst`** du?* (`Ich` $\rightarrow$ `komme`; `Das` [thành phố Wien ở hiện tại] $\rightarrow$ `ist`; `du` $\rightarrow$ `kommst`).
  * **A**: *Ich **`komme`** aus Athen. **`Warst`** du schon in Athen?* (`Ich` $\rightarrow$ `komme`; câu hỏi trải nghiệm quá khứ với `du` và `schon` $\rightarrow$ đảo **`Warst`** lên đầu câu).
  * **Carlos**: *Nein, wo **`ist`** denn das?* (Hỏi vị trí địa lý hiện tại của thành phố Athen $\rightarrow$ dùng hiện tại **`ist`**, không dùng quá khứ vì thành phố vẫn nằm ở đó!).
  * **A**: *Das **`ist`** in Griechenland.* (Khẳng định vị trí địa lý $\rightarrow$ **`ist`**).

#### 6.2. Phân tích Bưu thiếp / Thư kể chuyện Du lịch Hải Phòng (`Liebe Anna...`)
Đây là văn bản mẫu kinh điển kết hợp giữa **Thì Quá khứ đơn (`Präteritum`)** để kể lại hoạt động ngày hôm qua (`gestern`) và **Thì Hiện tại (`Präsens`)** để nói về trạng thái ngày hôm nay (`heute`):

> **Văn bản chuẩn trên bảng:**
> *"Liebe Anna,*
> ***gestern*** **`waren`** *Paula und ich in Haiphong. **Ich*** **`war`** *im BigC Supermarkt und **Paula** [war] im Theater.* **`Wart`** ***ihr** schon auf dem Cat Bi Markt? Der Cat Bi Markt* **`war`** *sehr interessant. Hier sind ein paar Fotos. Es* **`war`** *super! **Heute** **sind** wir am Do Son Meer.*
> *Viele Grüße*
> *Paula und Peter"*

* **Bản dịch tiếng Việt hoàn chỉnh**:
  *"Anna thân mến,*
  *Hôm qua Paula và mình đã ở Hải Phòng. Mình đã ở siêu thị BigC còn Paula (đã ở) trong nhà hát. Các bạn đã từng đến chợ Cát Bi chưa? Chợ Cát Bi đã rất thú vị. Đây là một vài bức ảnh. Mọi thứ đã tuyệt lắm! Hôm nay chúng mình đang ở biển Đồ Sơn.*
  *Thân ái chào bạn,*
  *Paula và Peter"*
* **Phân tích cấu trúc ngữ pháp & Từ vựng đắt giá trong bức thư**:
  1. **`Liebe Anna,` / `Viele Grüße`**: Công thức mở đầu (*"Anna thân mến,"* — dùng `Liebe` cho người nhận là nữ, `Lieber` cho người nhận là nam) và kết thúc (*"Nhiều lời chào thân ái"*) chuẩn cho thư/bưu thiếp thân mật ở trình độ A1.
  2. **`gestern waren Paula und ich...`**: Vì trạng ngữ thời gian `gestern` (*hôm qua*) được đưa lên đầu câu (Vị trí 1), động từ chia ở quá khứ **`waren`** giữ vững ở Vị trí 2, còn chủ ngữ **`Paula und ich`** (`= wir` - chúng tôi) lùi về Vị trí 3!
  3. **`Ich war im BigC Supermarkt und Paula (war) im Theater`**: Ngôi `ich` và ngôi thứ 3 số ít `Paula` (`= sie`) đều chia là **`war`**. Ở vế sau có thể lược bỏ `war` để tránh lặp từ.
  4. **`Wart ihr schon auf dem Cat Bi Markt?`**: Câu hỏi `Ja/Nein-Frage` ở quá khứ dành cho ngôi **`ihr`** (*các bạn*) $\rightarrow$ đẩy **`Wart`** lên đầu câu.
  5. **`Der Cat Bi Markt war sehr interessant` & `Es war super!`**: Chủ ngữ số ít (`Der Cat Bi Markt` = `er`, và đại từ `Es`) $\rightarrow$ chia là **`war`**.
  6. **Sự chuyển đổi thì tinh tế**: Câu kế cuối và cuối chuyển về thì **Hiện tại (`sind`)** vì nói về bức ảnh đang đính kèm (*`Hier sind ein paar Fotos`*) và hoạt động của ngày hôm nay (*`Heute sind wir am Do Son Meer`*).
  7. **4 Cụm giới từ chỉ địa điểm (Cách 3 - `Dativ`) cần ghi nhớ**:
     * **`im BigC Supermarkt`** (`der Supermarkt` $\rightarrow$ `in dem = im`: ở trong siêu thị BigC).
     * **`im Theater`** (`das Theater` $\rightarrow$ `in dem = im`: ở trong nhà hát).
     * **`auf dem Cat Bi Markt`** (`der Markt` $\rightarrow$ chợ ngoài trời/quảng trường dùng giới từ `auf dem`: ở trên/tại chợ Cát Bi).
     * **`am Do Son Meer`** (`das Meer` $\rightarrow$ ở bờ biển dùng giới từ `an dem = am`: ở biển Đồ Sơn).

---

## PHẦN 4: MỞ RỘNG CƠ SỞ DỮ LIỆU CHO 2 TAB TRA CỨU (`templates/index.html`)

### 4.1. Bổ sung vào `GERMAN_VERB_CONJUGATION_DB` (Tab `"📖 Chia động từ"`)
Antigravity IDE hãy giữ nguyên 35 động từ đã có và **bổ sung thêm các động từ của Bài 3** cùng dữ liệu **`praeteritum`** cho `sein` và `haben`:

```javascript
// Bổ sung trường praeteritum cho 'sein' và 'haben' + thêm các động từ Bài 3 vào GERMAN_VERB_CONJUGATION_DB:
{
    infinitive: "liegen", stem: "lieg", ending: "en",
    category: "reg", badge: "Quy tắc (Vị trí địa lý)",
    meaning: "nằm ở, tọa lạc ở (thành phố, địa danh trên bản đồ)",
    note: "Đi với giới từ 'im + Phương hướng + von' hoặc 'Tính từ hướng (-lich) + von': Hanoi liegt im Norden von Vietnam.",
    forms: { ich: "liege", du: "liegst", er_sie_es: "liegt", wir: "liegen", ihr: "liegt", sie_Sie: "liegen" },
    praeteritum: { ich: "lag", du: "lagst", er_sie_es: "lag", wir: "lagen", ihr: "lagt", sie_Sie: "lagen" }
},
{
    infinitive: "sprechen", stem: "sprech", ending: "en",
    category: "vowel", badge: "Biến âm (e → i)",
    meaning: "nói (ngôn ngữ), trò chuyện",
    note: "Biến đổi nguyên âm gốc e → i ở ngôi du (sprichst) và er/sie/es (spricht). Ví dụ: Welche Sprache sprichst du?",
    forms: { ich: "spreche", du: "sprichst", er_sie_es: "spricht", wir: "sprechen", ihr: "sprecht", sie_Sie: "sprechen" }
},
{
    infinitive: "reisen", stem: "reis", ending: "en",
    category: "s_stem", badge: "Gốc -s, -ß, -z",
    meaning: "đi du lịch, du hành",
    note: "Gốc kết thúc bằng -s nên ngôi du chỉ thêm -t (du reist = er/sie/es reist).",
    forms: { ich: "reise", du: "reist", er_sie_es: "reist", wir: "reisen", ihr: "reist", sie_Sie: "reisen" }
},
{
    infinitive: "besuchen", stem: "besuch", ending: "en",
    category: "reg", badge: "Quy tắc (Không tách)",
    meaning: "thăm, ghé thăm (địa danh, bạn bè)",
    note: "Tiền tố 'be-' không tách. Ví dụ: Wir besuchen das Brandenburger Tor in Berlin.",
    forms: { ich: "besuche", du: "besuchst", er_sie_es: "besucht", wir: "besuchen", ihr: "besucht", sie_Sie: "besuchen" }
}
```

### 4.2. Bổ sung vào `GERMAN_LEXIKON_DB` (Tab `"🏷️ Từ vựng & Giống"`)
Giữ nguyên toàn bộ từ vựng Bài 2 và **nối thêm 25 mục từ mới của Bài 3** (Danh lam thắng cảnh, Quốc gia có mạo từ, Phương hướng, Địa điểm):

```javascript
// Nối thêm vào mảng GERMAN_LEXIKON_DB trong templates/index.html:
    {
        word: "Sehenswürdigkeit", article: "die", gender: "die", plural: "die Sehenswürdigkeiten",
        indefinite: "eine Sehenswürdigkeit", negation: "keine Sehenswürdigkeit",
        meaning: "danh lam thắng cảnh, điểm tham quan", category: "Danh lam thắng cảnh",
        rule: "Hậu tố -keit luôn mang giống cái (die) 100%, số nhiều thêm -en.",
        example: "Der Eiffelturm ist eine berühmte Sehenswürdigkeit in Europa.",
        example_vi: "Tháp Eiffel là một danh lam thắng cảnh nổi tiếng ở châu Âu."
    },
    {
        word: "Akropolis", article: "die", gender: "die", plural: "— (Danh từ riêng)",
        indefinite: "Athen (Hy Lạp)", negation: "Griechenland",
        meaning: "Thành cổ Akropolis (ở Athens, Hy Lạp)", category: "Danh lam thắng cảnh",
        rule: "Danh thắng nổi tiếng ở Athen (Griechenland), luôn đi kèm mạo từ xác định 'die'.",
        example: "Was ist das? – Das ist die Akropolis. Sie liegt in Athen, Griechenland.",
        example_vi: "Đây là gì? – Đó là thành cổ Akropolis. Nó nằm ở Athens, Hy Lạp."
    },
    {
        word: "Big Ben", article: "der", gender: "der", plural: "— (Danh từ riêng)",
        indefinite: "London (Anh)", negation: "England / Großbritannien",
        meaning: "Tháp đồng hồ Big Ben (ở London, Anh)", category: "Danh lam thắng cảnh",
        rule: "Mang giống đực (der) theo danh từ der Turm (ngọn tháp).",
        example: "Wo ist der Big Ben? – Der Big Ben ist in London, England.",
        example_vi: "Tháp Big Ben ở đâu? – Tháp Big Ben ở London, nước Anh."
    },
    {
        word: "Eiffelturm", article: "der", gender: "der", plural: "die Eiffeltürme",
        indefinite: "Paris (Pháp)", negation: "Frankreich",
        meaning: "Tháp Eiffel (ở Paris, Pháp)", category: "Danh lam thắng cảnh",
        rule: "Danh từ ghép lấy giống theo từ cuối: der Turm (ngọn tháp) -> der Eiffelturm.",
        example: "Der Eiffelturm steht in Paris. Paris liegt in Frankreich.",
        example_vi: "Tháp Eiffel nằm ở Paris. Paris thuộc nước Pháp."
    },
    {
        word: "Schiefe Turm", article: "der", gender: "der", plural: "Pisa (Ý)",
        indefinite: "ein schiefer Turm", negation: "Italien",
        meaning: "Tháp nghiêng Pisa (ở Pisa, Ý)", category: "Danh lam thắng cảnh",
        rule: "Cụm danh từ có tính từ 'schief' (nghiêng) + der Turm (tháp) -> der Schiefe Turm von Pisa.",
        example: "Wo ist der Schiefe Turm? – Er ist in Pisa, Italien.",
        example_vi: "Tháp nghiêng ở đâu? – Nó nằm ở thành phố Pisa, nước Ý."
    },
    {
        word: "Prater", article: "der", gender: "der", plural: "— (Danh từ riêng)",
        indefinite: "Wien (Áo)", negation: "Österreich",
        meaning: "Công viên giải trí Prater (ở Viên, Áo)", category: "Danh lam thắng cảnh",
        rule: "Mang giống đực (der), tọa lạc tại thủ đô Wien của nước Áo (Österreich).",
        example: "Der Prater ist in Wien. Wien liegt im Osten von Österreich.",
        example_vi: "Công viên Prater ở Viên. Viên nằm ở phía Đông của nước Áo."
    },
    {
        word: "Brandenburger Tor", article: "das", gender: "das", plural: "Berlin (Đức)",
        indefinite: "ein Tor", negation: "Deutschland",
        meaning: "Cổng Brandenburg (ở Berlin, Đức)", category: "Danh lam thắng cảnh",
        rule: "Lấy giống trung (das) theo danh từ chính das Tor (cái cổng).",
        example: "Was ist das? – Das ist das Brandenburger Tor in Berlin, Deutschland.",
        example_vi: "Đây là gì? – Đó là Cổng Brandenburg ở Berlin, CHLB Đức."
    },
    {
        word: "Rote Platz", article: "der", gender: "der", plural: "Moskau (Nga)",
        indefinite: "ein Platz", negation: "Russland",
        meaning: "Quảng trường Đỏ (ở Mát-xcơ-va, Nga)", category: "Danh lam thắng cảnh",
        rule: "Lấy giống đực (der) theo danh từ der Platz (quảng trường).",
        example: "Der Rote Platz ist in Moskau. Moskau liegt in Russland.",
        example_vi: "Quảng trường Đỏ nằm ở Mát-xcơ-va. Mát-xcơ-va thuộc nước Nga."
    },
    {
        word: "Schweiz", article: "die", gender: "die", plural: "Ngôn ngữ: Deutsch, Französisch, Italienisch",
        indefinite: "in der Schweiz", negation: "aus der Schweiz",
        meaning: "Thụy Sỹ (Quốc gia có mạo từ die)", category: "Quốc gia & Ngôn ngữ",
        rule: "Quốc gia mang giống cái (die). Khi đi với 'aus' hoặc 'in' ở Dativ phải đổi thành 'aus der Schweiz' / 'in der Schweiz'.",
        example: "Meine Tante wohnt in der Schweiz. Dort spricht man Deutsch, Französisch und Italienisch.",
        example_vi: "Cô của tôi sống ở Thụy Sỹ. Ở đó người ta nói tiếng Đức, tiếng Pháp và tiếng Ý."
    },
    {
        word: "Türkei", article: "die", gender: "die", plural: "Ngôn ngữ: Türkisch",
        indefinite: "in der Türkei", negation: "aus der Türkei",
        meaning: "Thổ Nhĩ Kỳ (Quốc gia có mạo từ die)", category: "Quốc gia & Ngôn ngữ",
        rule: "Mọi quốc gia tận cùng bằng đuôi -ei đều mang giống cái (die). Dativ: aus/in der Türkei.",
        example: "Er kommt aus der Türkei und spricht Türkisch.",
        example_vi: "Anh ấy đến từ Thổ Nhĩ Kỳ và nói tiếng Thổ Nhĩ Kỳ."
    },
    {
        word: "Slowakei", article: "die", gender: "die", plural: "Ngôn ngữ: Slowakisch",
        indefinite: "in der Slowakei", negation: "aus der Slowakei",
        meaning: "Slovakia (Quốc gia có mạo từ die)", category: "Quốc gia & Ngôn ngữ",
        rule: "Đuôi -ei mang giống cái (die). Dativ: aus/in der Slowakei.",
        example: "Bratislava liegt in der Slowakei. Man spricht dort Slowakisch.",
        example_vi: "Bratislava nằm ở Slovakia. Ở đó người ta nói tiếng Slovakia."
    },
    {
        word: "Iran", article: "der", gender: "der", plural: "Ngôn ngữ: Persisch (Tiếng Ba Tư)",
        indefinite: "im (in dem) Iran", negation: "aus dem Iran",
        meaning: "Iran (Quốc gia có mạo từ der)", category: "Quốc gia & Ngôn ngữ",
        rule: "Quốc gia mang giống đực (der). Ở Dativ đổi thành 'aus dem Iran' và 'im Iran'. Ngôn ngữ là Persisch!",
        example: "Mein Kollege kommt aus dem Iran. Er spricht Persisch.",
        example_vi: "Đồng nghiệp của tôi đến từ Iran. Anh ấy nói tiếng Ba Tư."
    },
    {
        word: "USA", article: "die (Pl.)", gender: "die", plural: "Ngôn ngữ: Englisch",
        indefinite: "in den USA", negation: "aus den USA",
        meaning: "Hợp chủng quốc Hoa Kỳ - Mỹ (Số nhiều)", category: "Quốc gia & Ngôn ngữ",
        rule: "Danh từ số nhiều (Plural). Khi đi với 'aus' hoặc 'in' ở Dativ đổi thành 'aus den USA' / 'in den USA'.",
        example: "Die Lehrerin ist nett, sie kommt aus den USA.",
        example_vi: "Cô giáo rất tốt bụng, cô ấy đến từ nước Mỹ."
    },
    {
        word: "Norden", article: "der", gender: "der", plural: "Tính từ: nördlich",
        indefinite: "im Norden von", negation: "nördlich von",
        meaning: "phía Bắc, miền Bắc", category: "Phương hướng & Bản đồ",
        rule: "Mọi phương hướng đều mang giống đực (der). Có 2 cách nói: 'im Norden von' hoặc 'nördlich von'.",
        example: "Wo liegt Hanoi? – Hanoi liegt im Norden von Vietnam (nördlich von Vietnam).",
        example_vi: "Hà Nội nằm ở đâu? – Hà Nội nằm ở miền Bắc Việt Nam."
    },
    {
        word: "Süden", article: "der", gender: "der", plural: "Tính từ: südlich",
        indefinite: "im Süden von", negation: "südlich von",
        meaning: "phía Nam, miền Nam", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). Hai cách diễn đạt: 'im Süden von' hoặc 'südlich von'.",
        example: "Long An liegt im Süden von Vietnam (südlich von Vietnam).",
        example_vi: "Long An nằm ở miền Nam của Việt Nam."
    },
    {
        word: "Osten", article: "der", gender: "der", plural: "Tính từ: östlich",
        indefinite: "im Osten von", negation: "östlich von",
        meaning: "phía Đông, miền Đông", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). Khi chuyển sang tính từ thêm Umlaut o -> ö: östlich.",
        example: "Berlin liegt im Osten von Deutschland (östlich von Deutschland).",
        example_vi: "Berlin nằm ở phía Đông của nước Đức."
    },
    {
        word: "Westen", article: "der", gender: "der", plural: "Tính từ: westlich",
        indefinite: "im Westen von", negation: "westlich von",
        meaning: "phía Tây, miền Tây", category: "Phương hướng & Bản đồ",
        rule: "Giống đực (der). Tính từ là 'westlich' (không có Umlaut).",
        example: "Köln liegt im Westen von Deutschland (westlich von Deutschland).",
        example_vi: "Köln nằm ở phía Tây của nước Đức."
    },
    {
        word: "Nordosten", article: "der", gender: "der", plural: "Tính từ: nordöstlich",
        indefinite: "im Nordosten von", negation: "nordöstlich von",
        meaning: "phía Đông Bắc (ghép Bắc + Đông)", category: "Phương hướng & Bản đồ",
        rule: "Tiếng Đức đặt Bắc (Nord-) trước Đông (-osten). Tính từ: nordöstlich.",
        example: "Hai Phong liegt im Nordosten von Vietnam (nordöstlich von Vietnam).",
        example_vi: "Hải Phòng nằm ở phía Đông Bắc của Việt Nam."
    },
    {
        word: "Mitte", article: "die", gender: "die", plural: "Cụm cố định: in der Mitte von",
        indefinite: "in der Mitte", negation: "Không có dạng -lich",
        meaning: "trung tâm, ở giữa, miền Trung", category: "Phương hướng & Bản đồ",
        rule: "Mang giống cái (die) nên khi đi với giới từ 'in' ở Dativ phải đổi thành 'in der Mitte von'.",
        example: "Wo liegt Da Nang? – Da Nang liegt in der Mitte von Vietnam.",
        example_vi: "Đà Nẵng nằm ở đâu? – Đà Nẵng nằm ở miền Trung của Việt Nam."
    },
    {
        word: "Hausaufgabe", article: "die", gender: "die", plural: "die Hausaufgaben (thường dùng số nhiều)",
        indefinite: "eine Hausaufgabe", negation: "keine Hausaufgaben",
        meaning: "bài tập về nhà", category: "Đồ dùng lớp học",
        rule: "Danh từ ghép (das Haus + die Aufgabe) -> lấy giống cái (die), thường dùng ở dạng số nhiều: die Hausaufgaben machen.",
        example: "Er macht die Hausaufgaben. – Was macht er? / Macht er die Hausaufgaben?",
        example_vi: "Anh ấy làm bài tập về nhà. – Anh ấy làm gì? / Anh ấy có làm bài tập về nhà không?"
    }
];
```

---

## PHẦN 5: KHO 50 CÂU HỎI BÀI 3 & 5 CHẾ ĐỘ RANDOM ĐỔI ĐỀ TỰ ĐỘNG

Trong tệp `seed_a1_b3.py`, nạp **đúng 50 câu hỏi** cho Bài 3, phân bổ đầy đủ qua 7 dạng kỹ năng:
1. **Dạng 1 - Trắc nghiệm (`trac_nghiem` - 10 câu)**:
   * Quốc gia & Ngôn ngữ (*Đức, Áo, Thụy Sỹ nói tiếng gì? Iran nói tiếng gì? Quốc gia nào đi kèm mạo từ `die / der / die Pl.`?*).
   * Danh lam thắng cảnh (*`das Brandenburger Tor`, `der Eiffelturm`, `die Akropolis`, `der Prater`, `der Rote Platz`, `der Schiefe Turm`, `der Big Ben` thuộc thành phố và đất nước nào?*).
   * Phương hướng (*Đông Bắc là `Nordosten`, Tây Nam là `Südwesten`, miền Trung là `in der Mitte`*).
   * Chia động từ `sein` ở thì `Präteritum` (*`war / warst / waren / wart`*).
2. **Dạng 2 - Điền khuyết (`dien_khuyet` - 10 câu)**:
   * Điền `im Norden`, `nördlich`, `im Nordosten`, `nordöstlich`, `in der Mitte` vào câu hỏi vị trí `Wo liegt...?`.
   * Điền `war, warst, waren, wart` vào đoạn bưu thiếp Hải Phòng (*"Gestern ___ Paula und ich in Haiphong. Ich ___ im BigC Supermarkt... ___ ihr schon auf dem Cat Bi Markt?"*).
   * Điền đoạn hội thoại của Carlos (*`kommst, komme, ist, warst`*).
3. **Dạng 3 - Dịch 2 chiều Việt ⇄ Đức (`dich` - 8 câu)**:
   * Dịch câu phương hướng bằng cả 2 cách (*"Hải Phòng nằm ở phía Đông Bắc Việt Nam"*, *"Đà Nẵng nằm ở miền Trung Việt Nam"*, *"Long An nằm ở miền Nam Việt Nam"*).
   * Dịch câu quá khứ `Präteritum` (*"Bạn đã từng ở Hà Nội chưa? – Rồi, hôm qua tôi đã ở Hà Nội."*, *"Các bạn đã từng đến chợ Cát Bi chưa? – Nó đã rất thú vị!"*).
4. **Dạng 4 - Luyện Nghe 1.0x & 0.65x (`nghe` - 6 câu)**:
   * Nghe các câu mô tả thắng cảnh châu Âu, vị trí bản đồ và đoạn thư của Paula & Peter ở Hải Phòng để điền từ chính xác.
5. **Dạng 5 - Luyện Nói & Phát âm (`noi` - 5 câu)**:
   * Luyện đọc chuẩn: *"Hai Phong liegt im Nordosten von Vietnam."*, *"Da Nang liegt in der Mitte von Vietnam."*, *"Warst du schon in Athen? – Nein, wo ist denn das?"*, *"Gestern waren Paula und ich in Haiphong. Es war super!"*, *"In der Schweiz spricht man Deutsch, Französisch und Italienisch."*
6. **Dạng 6 - Đọc hiểu Bưu thiếp Du lịch (`doc` - 4 câu)**:
   * Đọc bức thư của Paula và Peter gửi Anna về chuyến đi Hải Phòng (*siêu thị BigC, nhà hát, chợ Cát Bi, biển Đồ Sơn*) và trả lời các câu hỏi đọc hiểu chi tiết.
7. **Dạng 7 - Viết câu & Chuyển đổi Câu hỏi (`viet` - 7 câu)**:
   * Chuyển đổi câu trần thuật sang cả `W-Frage` và `Ja/Nein-Frage` (*"Ich heiße Anna"*, *"Ich wohne in Hai Phong"*, *"Er macht die Hausaufgaben"*, *"Sie ist Lehrerin"*).
   * Viết lại câu vị trí địa lý từ dạng Danh từ (`im ... von`) sang dạng Tính từ (`...lich von`) và ngược lại.

### 5 Chế độ Random Đổi Đề Tự Động Mới cho Bài 3 (`templates/index.html`)
Mở rộng hàm `randomizeDynamicExercises()` trên Frontend để tự động đổi đề mỗi khi người học hoàn thành bài tập (bấm `🔄 Đổi đề khác`) hoặc thoát ra vào lại:

1. **Random Phương hướng & Bản đồ (`dynamic_direction_quiz`)**:
   * Ngân hàng gồm 12 thành phố Việt Nam & Đức (*Ha Noi, Hai Phong, Da Nang, Long An, Dien Bien, Can Tho, Berlin, München, Hamburg, Köln, Frankfurt, Dresden*) kèm phương hướng chuẩn (`Norden/nördlich`, `Nordosten/nordöstlich`, `Mitte/in der Mitte`, `Süden/südlich`, `Nordwesten/nordwestlich`, `Südwesten/südwestlich`, `Osten/östlich`, `Westen/westlich`).
   * Mỗi lần random sẽ chọn 1 thành phố bất kỳ và yêu cầu viết câu theo Cách 1 (`liegt im ... von ...`) hoặc Cách 2 (`liegt ...lich von ...`).
2. **Random Danh lam Thắng cảnh Châu Âu (`dynamic_landmark_quiz`)**:
   * Tự động chọn ngẫu nhiên 1 trong 7 thắng cảnh (*die Akropolis, der Big Ben, der Eiffelturm, der Schiefe Turm, der Prater, das Brandenburger Tor, der Rote Platz*) để hỏi mạo từ (`der/die/das`), thành phố (`Athen, London, Paris, Pisa, Wien, Berlin, Moskau`) hoặc quốc gia (`Griechenland, England, Frankreich, Italien, Österreich, Deutschland, Russland`).
3. **Random Chia `"sein"` ở Thì `Präteritum` (`dynamic_praeteritum_quiz`)**:
   * Tự động đổi chủ ngữ (*ich, du, er, sie, es, wir, ihr, Sie, Paula und ich, du und Peter, der Cat Bi Markt, die Fotos*) và địa điểm (*in Hanoi, in Haiphong, im BigC Supermarkt, im Theater, auf dem Cat Bi Markt, in Wien, in Athen*) để người học chia đúng **`war / warst / waren / wart`**.
4. **Random Quốc gia & Ngôn ngữ (`dynamic_country_language_quiz`)**:
   * Tự động bốc ngẫu nhiên 1 trong 18 quốc gia (cả nhóm không mạo từ và nhóm có mạo từ `die Schweiz, die Türkei, die Slowakei, der Iran, die USA`) để hỏi tên ngôn ngữ hoặc cách dùng giới từ `aus / in` (`aus der Schweiz`, `im Iran`, `in den USA`...).
5. **Random Chuyển đổi Câu Trần thuật sang `W-Frage` & `Ja/Nein-Frage` (`dynamic_question_transform`)**:
   * Tự động thay đổi câu trần thuật gốc (*Ich heiße..., Ich wohne in..., Er macht die Hausaufgaben, Sie ist Lehrerin, Carlos kommt aus Wien, Hanoi liegt im Norden...*) để người học viết đúng câu hỏi `W-Frage` và `Ja/Nein-Frage`.

---

## PHẦN 6: HƯỚNG DẪN THỰC THI DÀNH CHO ANTIGRAVITY IDE

1. **Tạo và chạy tệp `seed_a1_b3.py`**:
   * Giữ nguyên toàn bộ dữ liệu của Bài 1 (P1), Bài 1 (P2) và Bài 2 trong `deutsch_meister.db`.
   * Chèn nối tiếp (hoặc cập nhật nếu đã tồn tại tiêu đề) **Bài 3: `"Địa danh - Phương hướng - Präteritum (Städte – Länder – Sprachen)"`** vào bảng `lessons` với đầy đủ 7 học phần lý thuyết dài và chi tiết ở Phần 3.
   * Nạp toàn bộ từ vựng Quốc gia, Ngôn ngữ, 7 Danh lam thắng cảnh, 8 Phương hướng và các mẫu câu `Präteritum` vào bảng `vocabulary` của Bài 3.
   * Nạp đủ **50 câu hỏi** vào bảng `exercises` cho Bài 3, gắn đầy đủ các nhãn `dynamic_direction_quiz`, `dynamic_landmark_quiz`, `dynamic_praeteritum_quiz`, `dynamic_country_language_quiz`, `dynamic_question_transform` trong cột `extra_data`.
2. **Cập nhật tệp `templates/index.html`**:
   * Bổ sung dữ liệu mới vào `GERMAN_VERB_CONJUGATION_DB` (thêm bảng `Präteritum` cho `sein`/`haben` và các động từ Bài 3) và `GERMAN_LEXIKON_DB` (thêm Danh lam thắng cảnh, Quốc gia có mạo từ, Phương hướng).
   * Bổ sung 5 bộ sinh đề ngẫu nhiên mới của Bài 3 vào hàm `randomizeDynamicExercises()`.
   * Bổ sung từ điển phát âm chuẩn `de-DE` cho các từ khó trong Bài 3 (`Österreich`, `Griechenland`, `Tschechien`, `Französisch`, `Sehenswürdigkeiten`, `Eiffelturm`, `nördlich`, `nordöstlich`, `südöstlich`, `Präteritum`).
3. **Kiểm tra & Cập nhật lên GitHub / Render**:
   * Chạy `python3 seed_a1_b3.py` và kiểm tra `python3 -m py_compile app.py seed_a1_b3.py`.
   * Chạy lệnh `git add . && git commit -m "Add Lesson 3 (Staedte, Laender, Sprachen, Praeteritum) and expand Lexikon/Conjugator" && git push` để đồng bộ lên đường link Public vĩnh viễn.