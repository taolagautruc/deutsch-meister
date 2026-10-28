# ĐẶC TẢ KỸ THUẬT: BÀI 1 (PHẦN 2) "KAFFEE ODER TEE?" & TAB TRA CỨU CHIA ĐỘNG TỪ (KONJUGATOR)

Tài liệu này hướng dẫn **Antigravity IDE / AI Agent** nâng cấp hệ thống **DeutschMeister (A1 - B2)** với 3 nhiệm vụ trọng tâm:
1. **Xây dựng Bài 1 (P2): "Kaffee oder Tee? - Cà Phê Hoặc Trà"** (Lý thuyết chuyên sâu + Từ vựng có phát âm + 50 bài tập tương tác đa dạng kèm cơ chế Random đổi đề).
2. **Bổ sung Tab mới "📖 Chia động từ" (Verb-Konjugator)** nằm **chính giữa** tab `"Không gian học (A1)"` và `"Đấu trường & BXH"` trên thanh điều hướng chính.
3. **Đảm bảo nguyên tắc bản quyền & âm thanh**: Tuyệt đối không chèn bất kỳ link YouTube nào vào giao diện; toàn bộ từ vựng, bảng chia động từ và câu hội thoại đều dùng bộ phát âm chuẩn bản xứ `de-DE` (`speakGerman`).

---

## PHẦN 1: THIẾT KẾ MỤC RIÊNG "📖 CHIA ĐỘNG TỪ" (NẰM GIỮA "KHÔNG GIAN HỌC" VÀ "ĐẤU TRƯỜNG")

### 1.1. Vị trí trên Thanh Điều Hướng (`templates/index.html`)
Cập nhật thanh Navigation Bar ở đầu trang (`header`) theo đúng thứ tự 5 mục sau:
1. `🎯 Cấp độ (A1 - B2)`
2. `🎓 Không gian học (A1)`
3. **`📖 Chia động từ` (MỤC MỚI — Nằm chính giữa Không gian học và Đấu trường)**
4. `🏆 Đấu trường & BXH`
5. `🗄️ Kiến trúc Python/SQL`

### 1.2. Chức năng của Tab "📖 Chia động từ" (Verb-Konjugator)
Khi người học bấm vào tab **`📖 Chia động từ`**, hệ thống mở ra công cụ tra cứu nhanh cách chia động từ theo toàn bộ các ngôi nhân xưng:
* **Thanh tìm kiếm thông minh (Instant Search & Filter)**:
  * Cho phép gõ tiếng Đức (ví dụ: `machen`, `sein`, `nehmen`, `möchten`, `lesen`, `heissen`...) hoặc nghĩa tiếng Việt (ví dụ: `làm`, `uống`, `muốn`, `thuê`, `thanh toán`...).
  * Bộ lọc phân loại nhanh theo nhóm động từ:
    * `Tất cả`
    * `Quy tắc (Regelmäßig)`: *machen, wohnen, kommen, trinken, zahlen, lernen, hören, spielen, kaufen, leben, fragen, sagen*
    * `Gốc kết thúc bằng -s, -ß, -z`: *heißen, tanzen, reisen, sitzen* (ngôi `du` chỉ thêm `-t`, trùng với `er/sie/es`)
    * `Gốc kết thúc bằng -t, -d`: *mieten, arbeiten, antworten, finden, kosten, warten* (thêm `-e-` thành `-est` ở ngôi `du`, `-et` ở ngôi `er/sie/es` và `ihr`)
    * `Biến âm gốc (Vokalwechsel e -> i/ie, a -> ä)`: *nehmen, lesen, sprechen, sehen, essen, geben, helfen, treffen, fahren, schlafen, waschen, tragen*
    * `Bất quy tắc & Khuyết thiếu (Unregelmäßig & Modalverben)`: *sein, haben, werden, möchten, können, müssen, wollen, dürfen, sollen, mögen, wissen*
* **Thẻ hiển thị Bảng Chia Động Từ (Conjugation Card)**:
  * Hiển thị rõ: **Nguyên mẫu (Infinitiv)**, **Nghĩa tiếng Việt**, **Nhóm quy tắc**, **Phân tách Gốc động từ (Verbstamm) + Đuôi (-en)** và **Câu ví dụ thực tế**.
  * Bảng chia đầy đủ cho các ngôi (kèm nút `🔊` phát âm từng ngôi và nút `🔊 Đọc toàn bộ bảng`):
    * `ich` (tôi)
    * `du` (bạn)
    * `er / sie / es` (anh ấy / cô ấy / nó)
    * `wir` (chúng tôi, chúng ta)
    * `ihr` (các bạn)
    * `sie / Sie` (họ / Ngài, các Ngài)
  * **Highlight màu sắc trực quan**: Đuôi động từ (`-e, -st, -t, -en, -t, -en` hoặc `-est, -et`) và các nguyên âm bị biến đổi (`e -> i`, `e -> ie`, `a -> ä`) hoặc dạng bất quy tắc (`bin, bist, ist...`, `möchte...`) phải được tô màu nổi bật (ví dụ: màu vàng/cam hoặc xanh ngọc) để người học nhìn thấy ngay sự thay đổi.

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT & TỪ VỰNG BÀI 1 (P2) — "KAFFEE ODER TEE? (CÀ PHÊ HOẶC TRÀ)"

Tạo tệp `seed_a1_b1_p2.py` (hoặc tích hợp vào script seed) để nạp **Bài 1 (P2): "Kaffee oder Tee? - Đại Từ Nhân Xưng, Chia Động Từ & Gọi Đồ Uống"** vào bảng `lessons` với 6 phần lý thuyết chi tiết (tuyệt đối không có link YouTube):

### Mục 1: Hệ thống Đại từ nhân xưng (Personalpronomen) ở cách 1 (Nominativ)
| Đại từ | Nghĩa tiếng Việt | Ghi chú sử dụng & Phân biệt 3 chữ `sie/Sie` |
| :--- | :--- | :--- |
| **`ich`** | tôi | Ngôi thứ nhất số ít |
| **`du`** | bạn / cậu / em | Ngôi thứ hai số ít (thân mật: bạn bè, người thân, trẻ em) |
| **`er`** | anh ấy / ông ấy / nó (danh từ giống đực `der`) | Ngôi thứ ba số ít |
| **`sie`** *(nhỏ, số ít)* | cô ấy / bà ấy / nó (danh từ giống cái `die`) | Đi với động từ chia đuôi **`-t`** (hoặc `ist`) |
| **`es`** | nó (danh từ giống trung `das`) | Ngôi thứ ba số ít |
| **`wir`** | chúng tôi / chúng ta | Ngôi thứ nhất số nhiều *(Lưu ý: `Anna und ich` = `wir`)* |
| **`ihr`** | các bạn / các cậu | Ngôi thứ hai số nhiều (thân mật — nhiều người `du` cộng lại, ví dụ: `Anna und Peter` khi hỏi trực tiếp = `ihr`) |
| **`sie`** *(nhỏ, số nhiều)* | họ / chúng | Đi với động từ chia đuôi **`-en`** (hoặc `sind`) |
| **`Sie`** *(viết hoa chữ S)* | Ngài / các Ngài / Ông / Bà | Ngôi xưng hô lịch sự, trang trọng (dùng với `Herr ...`, `Frau ...`, người lạ, nơi công sở). Luôn viết hoa chữ `S` ở mọi vị trí trong câu. |

### Mục 2: Cấu tạo Động từ & Quy tắc Chia Động Từ Có Quy Tắc (Regelmäßige Verben)
* **Cấu tạo động từ nguyên mẫu (Infinitiv)**: Gồm **Gốc động từ (Verbstamm)** + **Đuôi nguyên mẫu (`-en` / `-n`)**.
  * Ví dụ: `mach|en` $\rightarrow$ Gốc: **`mach-`**, Đuôi: **`-en`**.
  * Ví dụ: `wohn|en` $\rightarrow$ Gốc: **`wohn-`**, Đuôi: **`-en`**.
  * Ví dụ: `komm|en` $\rightarrow$ Gốc: **`komm-`**, Đuôi: **`-en`**.
  * Ví dụ: `trink|en` $\rightarrow$ Gốc: **`trink-`**, Đuôi: **`-en`**.
* **Công thức chia chuẩn ở thì Hiện tại (Präsens)**:
  * `ich` $\rightarrow$ Gốc + **`-e`** (*ich mache, wohne, komme, trinke*)
  * `du` $\rightarrow$ Gốc + **`-st`** (*du machst, wohnst, kommst, trinkst*)
  * `er / sie / es` $\rightarrow$ Gốc + **`-t`** (*er/sie/es macht, wohnt, kommt, trinkt*)
  * `wir` $\rightarrow$ Gốc + **`-en`** (*wir machen, wohnen, kommen, trinken*)
  * `ihr` $\rightarrow$ Gốc + **`-t`** (*ihr macht, wohnt, kommt, trinkt*)
  * `sie / Sie` $\rightarrow$ Gốc + **`-en`** (*sie/Sie machen, wohnen, kommen, trinken*)
* **Quy tắc vị trí động từ (Position 2)**: Trong câu trần thuật đơn và câu hỏi có từ để hỏi (`W-Frage`), động từ đã chia theo chủ ngữ **luôn luôn đứng ở vị trí thứ 2** (`S + V2 + ...` hoặc `W-Wort + V2 + S + ...`).
  * Ví dụ: `Ich komme aus Vietnam.` / `Ich wohne in Hai Phong.`

### Mục 3: Hai trường hợp đặc biệt về phát âm khi chia động từ (`-s, -ß, -z` và `-t, -d`)
1. **Nhóm gốc động từ kết thúc bằng `-s`, `-ß`, `-z`, `-ss`, `-x`** (Ví dụ: **`heißen`** - tên là, **`tanzen`** - nhảy):
   * Vì gốc đã có âm gió `/s/` ở cuối (`heiß-`), khi chia ở ngôi **`du`**, ta **không thêm `-st`** mà **chỉ thêm `-t`** $\rightarrow$ ngôi `du`, `er/sie/es`, `ihr` viết giống hệt nhau:
   * `ich heiße`, **`du heißt`**, **`er/sie/es heißt`**, `wir heißen`, **`ihr heißt`**, `sie/Sie heißen`.
2. **Nhóm gốc động từ kết thúc bằng `-t`, `-d`** (hoặc `-chn`, `-ffn`, `-tm`) (Ví dụ: **`mieten`** - thuê, **`arbeiten`** - làm việc, **`antworten`** - trả lời, **`kosten`** - có giá):
   * Để đọc được rõ âm đuôi mà không bị líu lưỡi, ta phải **chèn thêm nguyên âm `-e-`** trước đuôi `-st` và `-t` ở các ngôi **`du` (`-est`)**, **`er/sie/es` (`-et`)** và **`ihr` (`-et`)**:
   * **Bảng chia `mieten` (thuê) & `arbeiten` (làm việc)**:
     * `ich`: `miete` | `arbeite`
     * `du`: **`mietest`** | **`arbeitest`**
     * `er/sie/es`: **`mietet`** | **`arbeitet`**
     * `wir`: `mieten` | `arbeiten`
     * `ihr`: **`mietet`** | **`arbeitet`**
     * `sie/Sie`: `mieten` | `arbeiten`
   * **Hội thoại mẫu thực tế 1**:
     * **Marc**: *Woher kommst du?* (Bạn đến từ đâu?)
     * **Anna**: *Ich komme aus Brasilien. Das ist mein Freund, er kommt aus Russland.* (Tôi đến từ Brazil. Đây là bạn tôi, anh ấy đến từ Nga.)
     * **Marc**: *Und wo wohnt ihr?* (Và các bạn sống ở đâu?)
     * **Anna und Peter**: *Wir wohnen in Berlin. Wo arbeitest du?* (Chúng tôi sống ở Berlin. Bạn làm việc ở đâu?)
     * **Marc**: *Ich arbeite bei der Post.* (Tôi làm việc tại bưu điện.)
   * **Hội thoại mẫu thực tế 2 (Lịch sự với `Frau` / `Herr` $\rightarrow$ dùng ngôi `Sie`)**:
     * **Frau Bui**: *Guten Tag, wie heißen Sie?*
     * **Herr Nguyen**: *Ich heiße Dat.*
     * **Frau Bui**: *Woher kommen Sie?*
     * **Herr Nguyen**: *Ich komme aus Vietnam.*

### Mục 4: Động từ Bất quy tắc cốt lõi (`sein`, `haben`) & Động từ Biến âm (`lesen`, `nehmen`)
1. **Động từ `sein` (thì, là, ở) — Bất quy tắc hoàn toàn (Học thuộc lòng)**:
   * `ich` **`bin`** | `du` **`bist`** | `er/sie/es` **`ist`** | `wir` **`sind`** | `ihr` **`seid`** | `sie/Sie` **`sind`**.
   * **Đoạn văn mẫu thực hành `sein`**:
     * *- Hi, Anna und ich **sind** im Café Kafka. Wo **bist** du? Maria **ist** auch da. Kommst du auch?* (Chào, Anna và tôi đang ở trong quán cà phê Kafka. Bạn đang ở đâu? Maria cũng ở đây. Bạn có đến luôn không?)
     * *- Wo **seid** ihr? Ich **bin** im Deutschkurs. Die Lehrerin **ist** nett, sie **ist** aus den USA.* (Các bạn đang ở đâu? Tôi đang ở trong khóa học tiếng Đức. Cô giáo rất tốt bụng, cô ấy đến từ Mỹ.)
     * *(Lưu ý ngữ pháp: `Anna und ich` = `wir` $\rightarrow$ chia `sind`; `Die Lehrerin` = `sie` (cô ấy) $\rightarrow$ chia `ist`; `aus den USA` dùng cho quốc gia số nhiều).*
2. **Động từ `haben` (có)**:
   * Biến đổi ở ngôi `du` và `er/sie/es` (bỏ `-b-` ở gốc `hab-`):
   * `ich habe`, **`du hast`**, **`er/sie/es hat`**, `wir haben`, `ihr habt`, `sie/Sie haben`.
3. **Động từ biến âm gốc `e` $\rightarrow$ `ie` / `i` ở ngôi `du` và `er/sie/es` (`lesen` - đọc, `nehmen` - dùng/lấy/gọi món)**:
   * Chỉ biến âm ở **ngôi thứ 2 và ngôi thứ 3 số ít (`du`, `er/sie/es`)**, các ngôi số nhiều (`wir, ihr, sie/Sie`) và ngôi `ich` giữ nguyên gốc!
   * **`lesen` (đọc — `e` $\rightarrow$ `ie`, gốc kết thúc bằng `-s` nên `du` và `er/sie/es` viết giống nhau)**:
     * `ich lese`, **`du liest`**, **`er/sie/es liest`**, `wir lesen`, `ihr lest`, `sie/Sie lesen`.
   * **`nehmen` (dùng, sử dụng, chọn món — `eh` $\rightarrow$ `imm`)**:
     * `ich nehme`, **`du nimmst`**, **`er/sie/es nimmt`**, `wir nehmen`, `ihr nehmt`, `sie/Sie nehmen`.

### Mục 5: Động từ khuyết thiếu `möchten` (muốn một cách lịch sự) & Cấu trúc khung câu (Satzklammer)
* **Bảng chia động từ khuyết thiếu (`Modalverb`) `möchten` (muốn)**:
  * Lưu ý đặc biệt: Ngôi **`ich`** và ngôi **`er/sie/es`** chia **giống hệt nhau** (`möchte` — đều không có đuôi `-t`), đồng thời vì gốc kết thúc bằng `-t` nên ngôi `du` và `ihr` có thêm `-e-` (`möchtest`, `möchtet`):
  * `ich` **`möchte`**
  * `du` **`möchtest`**
  * `er/sie/es` **`möchte`** *(Chú ý: KHÔNG có chữ `-t` ở cuối!)*
  * `wir` **`möchten`**
  * `ihr` **`möchtet`**
  * `sie/Sie` **`möchten`**
* **Cấu trúc câu với `möchten` + Động từ nguyên mẫu**:
  * Khi trong câu có `möchten` đi kèm một động từ chỉ hành động khác (như `trinken` - uống, `zahlen` - thanh toán), **`möchten` đứng ở vị trí thứ 2** (chia theo chủ ngữ), còn **động từ chính đẩy về CUỐI CÂU và giữ nguyên mẫu (`-en`)**:
  * *1) Was **trinken** Sie?* $\rightarrow$ *Ich **trinke** Kaffee.*
  * *2) Was **nehmen** Sie?* $\rightarrow$ *Ich **nehme** Tee.*
  * *3) Was **möchten** Sie **trinken**?* $\rightarrow$ *Ich **möchte** Kakao **trinken**.*

### Mục 6: Từ vựng Đồ uống, Gia vị, Cách gọi món & Thanh toán tiền Euro (`€`) tại Quán Cà Phê
* **Danh sách Đồ uống & Đi kèm**:
  * `der Kaffee`: cà phê | `der Tee`: trà | `die Milch`: sữa | `die Cola`: nước ngọt Coca-Cola
  * `der Wein`: rượu vang | `der Kakao`: ca cao | `der Zucker`: đường | `das Eis`: đá lạnh / kem
  * `das Wasser` / `das Mineralwasser`: nước lọc / nước khoáng | `der Saft` / `der Orangensaft`: nước ép / nước cam
* **Giới từ & Lượng từ kết hợp khi gọi đồ uống**:
  * `mit` (với / có) $\leftrightarrow$ `ohne` (không có / không kèm)
  * `viel` (nhiều) $\leftrightarrow$ `wenig` (ít)
  * *Ví dụ*: `Ich trinke Kaffee mit viel Milch.` (Tôi uống cà phê với nhiều sữa.) / `Tee ohne Zucker, bitte.` (Cho trà không đường ạ.)
* **Cách hỏi giá & Đọc tiền tệ Euro (`1 Euro = 100 Cent`)**:
  * Dấu phẩy `,` trong giá tiền đọc là **`Euro`**, phần thập phân phía sau đọc số bình thường (có thể kèm chữ `Cent` hoặc không):
  * `1,29 €` $\rightarrow$ **`ein Euro neunundzwanzig`** (hoặc *ein Euro neunundzwanzig Cent*)
  * `2,99 €` $\rightarrow$ **`zwei Euro neunundneunzig`**
  * `3,99 €` $\rightarrow$ **`drei Euro neunundneunzig`**
  * `9,86 €` $\rightarrow$ **`neun Euro sechsundachtzig`**
  * `3,00 €` $\rightarrow$ **`drei Euro`**
* **Hội thoại mẫu tại Quán Cà Phê (Gọi món & Thanh toán)**:
  * **Kellner (Bồi bàn)**: *Was möchten Sie trinken?* (Quý khách muốn uống gì ạ?)
  * **Anna**: *Ich trinke Kaffee mit viel Milch.* (Tôi uống cà phê với nhiều sữa.)
  * **Sophie**: *Ich nehme Tee.* (Tôi dùng trà.)
  * *(Sau khi uống xong - Gọi tính tiền)*:
  * **Anna und Sophie**: *Wir möchten bitte zahlen.* (hoặc *Ich möchte zahlen, bitte.* — Chúng tôi muốn thanh toán ạ.)
  * **Kellner**: *Zusammen oder getrennt?* (Thanh toán chung hay riêng ạ? — `zusammen`: chung, `oder`: hoặc, `getrennt`: riêng)
  * **Anna**: *Zusammen, bitte.* (Thanh toán chung ạ.)
  * **Kellner**: *Das macht 3,99 Euro.* (Của quý khách hết $3,99$ Euro ạ. — Cấu trúc `Das macht + [Số tiền] + Euro`: Tổng cộng hết bao nhiêu tiền).

---

## PHẦN 3: KHO 50 CÂU HỎI BÀI 1 (P2) & CƠ CHẾ RANDOM ĐỔI ĐỀ TỰ ĐỘNG

Trong tệp `seed_a1_b1_p2.py`, nạp **đúng 50 câu hỏi** vào bảng `exercises` cho Bài 1 (P2), phân bổ đầy đủ 7 dạng kỹ năng:
1. **Dạng 1 - Trắc nghiệm (`trac_nghiem` - 10 câu)**:
   * Phân biệt đại từ nhân xưng (`Anna und ich` = `wir`, `Anna und du` = `ihr`, `Herr Nguyen` = `Sie`, `Die Lehrerin` = `sie`).
   * Chia động từ đặc biệt: `du heißt`, `du arbeitest`, `ihr mietet`, `du liest`, `er nimmt`, `er möchte` (bẫy `möchtet`), `ihr seid`, `er hat`.
   * Nghĩa từ vựng `mit/ohne`, `viel/wenig`, `zusammen/getrennt`.
2. **Dạng 2 - Điền khuyết chia động từ (`dien_khuyet` - 10 câu)**:
   * Điền dạng đúng của động từ vào câu hoàn chỉnh: `sein` (*bin, bist, ist, sind, seid*), `haben` (*habe, hast, hat, haben, habt*), `machen, wohnen, kommen, heißen, mieten, arbeiten, lesen, nehmen, trinken, möchten, zahlen*.
3. **Dạng 3 - Dịch 2 chiều Việt ⇄ Đức & Đổi giá tiền Euro (`dich` - 8 câu)**:
   * Dịch các câu gọi đồ uống, thanh toán (*"Tôi uống cà phê với nhiều sữa"*, *"Chúng tôi muốn thanh toán"*, *"Thanh toán chung hay riêng?"*, *"Tổng cộng hết 3,99 Euro"*).
   * Đổi cách viết chữ giá tiền sang số Euro và ngược lại.
4. **Dạng 4 - Luyện Nghe 1.0x & 0.65x (`nghe` - 6 câu)**:
   * Nghe câu hội thoại gọi món, nghe câu có động từ biến âm (`liest`, `nimmt`, `arbeitest`, `seid`) và nghe nhân viên phục vụ báo giá tiền (`Das macht ... Euro`) để điền đúng số tiền/câu.
5. **Dạng 5 - Luyện Nói & Phát âm (`noi` - 5 câu)**:
   * Phát âm chuẩn các câu có âm Umlaut và cụm phụ âm khó: *"Was möchten Sie trinken?"*, *"Ich trinke Kaffee mit viel Milch."*, *"Zusammen oder getrennt?"*, *"Die Lehrerin ist nett, sie ist aus den USA."*, *"Wo arbeitest du? Ich arbeite bei der Post."*
6. **Dạng 6 - Đọc hiểu hội thoại (`doc` - 4 câu)**:
   * Đọc hiểu 3 đoạn hội thoại thực tế: (1) Hội thoại của Marc, Anna và Peter (quê quán, nơi ở, nơi làm việc); (2) Tin nhắn tại Café Kafka & khóa học tiếng Đức (`im Café Kafka`, `im Deutschkurs`); (3) Hội thoại gọi món và tính tiền của Anna, Sophie với bồi bàn (`Kellner`).
7. **Dạng 7 - Viết câu, Chia động từ tổng hợp & Viết giá tiền (`viet` - 7 câu)**:
   * Sắp xếp/viết câu có `möchten ... trinken/zahlen` (khung câu `Satzklammer`), viết bảng chia động từ theo ngôi và viết cách đọc số tiền Euro (`€`, `Cent`) bằng chữ tiếng Đức.

### Cơ chế Random Đổi Đề Tự Động cho Bài 1 (P2) (`templates/index.html`)
Mở rộng bộ sinh đề ngẫu nhiên trên Frontend sao cho mỗi khi người học **hoàn thành 1 câu và bấm `🔄 Đổi đề khác`** hoặc **thoát ra khỏi phần Bài tập rồi vào lại / bấm nút `🎲 Đổi bộ đề ngẫu nhiên mới`**:
1. **Random câu hỏi Giá tiền Euro (`dynamic_price`)**:
   * Tự động sinh ngẫu nhiên số tiền từ `1,05 €` đến `99,99 €` (ví dụ: `4,50 €`, `12,89 €`, `3,99 €`, `19,75 €`).
   * Dùng hàm `priceToGerman(euros, cents)` (kết hợp với `numberToGerman`) để tạo đáp án chuẩn: `${numberToGerman(euros)} Euro ${numberToGerman(cents)}` (chấp nhận cả phương án có hoặc không có chữ `Cent` ở cuối, lưu ý `1 Euro` dùng `ein Euro` chứ không phải `eins Euro`).
2. **Random câu hỏi Chia động từ theo ngôi (`dynamic_conjugation`)**:
   * Tự động chọn ngẫu nhiên 1 động từ trong ngân hàng động từ (*machen, wohnen, kommen, heißen, mieten, arbeiten, trinken, nehmen, lesen, sein, haben, möchten, zahlen*) kết hợp với 1 chủ ngữ ngẫu nhiên (*ich, du, er, sie (cô ấy), es, wir, ihr, sie (họ), Sie, Anna und ich, Du und Peter, Die Lehrerin, Mein Freund*) để người học rèn phản xạ chia động từ biến hóa liên tục không bao giờ bị trùng lặp nhàm chán!

---

## PHẦN 4: DỮ LIỆU CHUẨN BỘ CHIA ĐỘNG TỪ (INTEGRATED VERB DATABASE)

Antigravity IDE hãy nhúng cấu trúc dữ liệu `GERMAN_VERBS_DB` (tối thiểu 25 động từ cốt lõi trình độ A1-A2) vào `templates/index.html` (hoặc API trong `app.py`) để phục vụ đồng thời cho **Tab "📖 Chia động từ"** và **Bộ Random Bài Tập**:

```javascript
const GERMAN_VERBS_DB = [
    {
        infinitiv: "sein", meaning: "thì, là, ở", group: "Bất quy tắc (Unregelmäßig)",
        stem: "sei-", ending: "-n",
        forms: { ich: "bin", du: "bist", er_sie_es: "ist", wir: "sind", ihr: "seid", sie_Sie: "sind" },
        note: "Động từ bất quy tắc quan trọng nhất trong tiếng Đức, biến đổi hoàn toàn ở tất cả các ngôi.",
        example: "Ich bin im Deutschkurs. Wo seid ihr?"
    },
    {
        infinitiv: "haben", meaning: "có", group: "Bất quy tắc (Unregelmäßig)",
        stem: "hab-", ending: "-en",
        forms: { ich: "habe", du: "hast", er_sie_es: "hat", wir: "haben", ihr: "habt", sie_Sie: "haben" },
        note: "Ngôi du và er/sie/es lược bỏ phụ âm -b- ở gốc (hast, hat).",
        example: "Ich habe Zeit. Hast du Kaffee?"
    },
    {
        infinitiv: "machen", meaning: "làm, thực hiện (Das macht... = Tổng cộng hết...)", group: "Quy tắc (Regelmäßig)",
        stem: "mach-", ending: "-en",
        forms: { ich: "mache", du: "machst", er_sie_es: "macht", wir: "machen", ihr: "macht", sie_Sie: "machen" },
        note: "Chia theo đúng công thức chuẩn: -e, -st, -t, -en, -t, -en.",
        example: "Das macht 3,99 Euro."
    },
    {
        infinitiv: "wohnen", meaning: "sống, cư trú", group: "Quy tắc (Regelmäßig)",
        stem: "wohn-", ending: "-en",
        forms: { ich: "wohne", du: "wohnst", er_sie_es: "wohnt", wir: "wohnen", ihr: "wohnt", sie_Sie: "wohnen" },
        note: "Thường đi với giới từ 'in' (wohnen in Berlin).",
        example: "Und wo wohnt ihr? Wir wohnen in Berlin."
    },
    {
        infinitiv: "kommen", meaning: "đến", group: "Quy tắc (Regelmäßig)",
        stem: "komm-", ending: "-en",
        forms: { ich: "komme", du: "kommst", er_sie_es: "kommt", wir: "kommen", ihr: "kommt", sie_Sie: "kommen" },
        note: "Thường đi với giới từ 'aus' chỉ nguồn gốc quê quán (kommen aus Vietnam).",
        example: "Mein Freund kommt aus Russland."
    },
    {
        infinitiv: "heißen", meaning: "tên là, gọi là", group: "Gốc kết thúc bằng -s, -ß, -z",
        stem: "heiß-", ending: "-en",
        forms: { ich: "heiße", du: "heißt", er_sie_es: "heißt", wir: "heißen", ihr: "heißt", sie_Sie: "heißen" },
        note: "Gốc kết thúc bằng -ß nên ngôi 'du' chỉ thêm -t (du heißt), viết giống hệt ngôi er/sie/es và ihr.",
        example: "Guten Tag, wie heißen Sie? Ich heiße Dat."
    },
    {
        infinitiv: "mieten", meaning: "thuê (nhà, căn hộ, xe)", group: "Gốc kết thúc bằng -t, -d",
        stem: "miet-", ending: "-en",
        forms: { ich: "miete", du: "mietest", er_sie_es: "mietet", wir: "mieten", ihr: "mietet", sie_Sie: "mieten" },
        note: "Gốc kết thúc bằng -t nên phải thêm -e- trước đuôi -st (du mietest) và -t (er/sie/es mietet, ihr mietet).",
        example: "Er mietet eine Wohnung in München."
    },
    {
        infinitiv: "arbeiten", meaning: "làm việc", group: "Gốc kết thúc bằng -t, -d",
        stem: "arbeit-", ending: "-en",
        forms: { ich: "arbeite", du: "arbeitest", er_sie_es: "arbeitet", wir: "arbeiten", ihr: "arbeitet", sie_Sie: "arbeiten" },
        note: "Gốc kết thúc bằng -t nên thêm -e- ở ngôi du (arbeitest), er/sie/es (arbeitet) và ihr (arbeitet).",
        example: "Wo arbeitest du? Ich arbeite bei der Post."
    },
    {
        infinitiv: "trinken", meaning: "uống", group: "Quy tắc (Regelmäßig)",
        stem: "trink-", ending: "-en",
        forms: { ich: "trinke", du: "trinkst", er_sie_es: "trinkt", wir: "trinken", ihr: "trinkt", sie_Sie: "trinken" },
        note: "Động từ có quy tắc dùng phổ biến khi gọi đồ uống.",
        example: "Ich trinke Kaffee mit viel Milch."
    },
    {
        infinitiv: "nehmen", meaning: "dùng, lấy, chọn (món)", group: "Biến âm gốc (e -> i/imm)",
        stem: "nehm-", ending: "-en",
        forms: { ich: "nehme", du: "nimmst", er_sie_es: "nimmt", wir: "nehmen", ihr: "nehmt", sie_Sie: "nehmen" },
        note: "Biến đổi gốc 'nehm-' thành 'nimm-' ở ngôi du (nimmst) và er/sie/es (nimmt).",
        example: "Was nehmen Sie? Ich nehme Tee."
    },
    {
        infinitiv: "lesen", meaning: "đọc", group: "Biến âm gốc (e -> ie)",
        stem: "les-", ending: "-en",
        forms: { ich: "lese", du: "liest", er_sie_es: "liest", wir: "lesen", ihr: "lest", sie_Sie: "lesen" },
        note: "Biến âm e -> ie ở ngôi du và er/sie/es. Vì gốc kết thúc bằng -s nên du và er/sie/es đều là 'liest'.",
        example: "Du liest ein Buch auf Deutsch."
    },
    {
        infinitiv: "möchten", meaning: "muốn (lịch sự)", group: "Khuyết thiếu (Modalverb)",
        stem: "möcht-", ending: "-en",
        forms: { ich: "möchte", du: "möchtest", er_sie_es: "möchte", wir: "möchten", ihr: "möchtet", sie_Sie: "möchten" },
        note: "Ngôi 'ich' và 'er/sie/es' chia giống hệt nhau (möchte - không có đuôi -t). Đi kèm động từ nguyên mẫu ở cuối câu.",
        example: "Was möchten Sie trinken? Wir möchten bitte zahlen."
    },
    {
        infinitiv: "zahlen", meaning: "thanh toán, trả tiền", group: "Quy tắc (Regelmäßig)",
        stem: "zahl-", ending: "-en",
        forms: { ich: "zahle", du: "zahlst", er_sie_es: "zahlt", wir: "zahlen", ihr: "zahlt", sie_Sie: "zahlen" },
        note: "Động từ có quy tắc, thường đi cùng möchten: 'Ich möchte zahlen, bitte.'",
        example: "Wir möchten bitte zahlen. Zusammen oder getrennt?"
    }
    // Antigravity IDE bổ sung thêm các động từ A1 phổ biến khác: sprechen, essen, geben, sehen, fahren, schlafen, kosten, antworten, lernen, kaufen...
];
```

---

## PHẦN 5: CÁC BƯỚC THỰC THI DÀNH CHO ANTIGRAVITY IDE

1. **Tạo và chạy tệp `seed_a1_b1_p2.py`**:
   * Thêm bài học thứ 2 của cấp độ A1: `Bài 1 (P2): "Kaffee oder Tee? - Đại Từ Nhân Xưng, Chia Động Từ & Gọi Đồ Uống"` vào bảng `lessons` trong `deutsch_meister.db`.
   * Nạp danh sách từ vựng & mẫu câu của Bài 1 (P2) vào bảng `vocabulary` (bao gồm các đại từ, động từ chia mẫu, tên đồ uống, câu giao tiếp với bồi bàn).
   * Nạp đủ **50 câu hỏi** vào bảng `exercises` cho Bài 1 (P2), gắn cờ `dynamic_price` và `dynamic_conjugation` trong `extra_data` để kích hoạt tính năng Random đổi đề.
2. **Cập nhật tệp `templates/index.html`**:
   * Thêm nút **`📖 Chia động từ`** nằm chính giữa `"Không gian học (A1)"` và `"Đấu trường & BXH"`.
   * Xây dựng giao diện tra cứu chia động từ tương tác (tìm kiếm tức thì, lọc theo nhóm, tô màu đuôi động từ và nguyên âm biến đổi, tích hợp nút phát âm `speakGerman` chuẩn `de-DE`).
   * Bổ sung các từ vựng mới của Bài 1 (P2) vào `GERMAN_PRONUNCIATION_MAP` (đặc biệt là `Café`, `Kakao`, `Euro`, `Cent`, `möchte`, `möchten`, `liest`, `nimmt`, `heißt`).
   * Tích hợp bộ sinh đề ngẫu nhiên cho cả **Giá tiền Euro (`€`)** và **Chia động từ theo ngôi**.
3. **Kiểm tra & Khởi chạy**:
   * Chạy `python3 seed_a1_b1_p2.py` để cập nhật `deutsch_meister.db`.
   * Kiểm tra cú pháp `python3 -m py_compile app.py seed_a1_b1_p2.py`.
   * Khởi động lại server và kiểm tra trên trình duyệt.