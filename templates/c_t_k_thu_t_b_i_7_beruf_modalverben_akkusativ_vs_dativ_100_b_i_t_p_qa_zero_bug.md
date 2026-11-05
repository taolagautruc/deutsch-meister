# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 7 (A1) "BERUF - MODALVERBEN - ARTIKELWÖRTER IN AKKUSATIV" & CHUYÊN ĐỀ PHÂN BIỆT AKKUSATIV VS. DATIV — KHO 100 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa làm hỏng, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**, **Bài 4**, **Bài 5**, **Bài 6**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này là **tạo mới hoàn toàn Bài 7 (`lessons/a1/seed_a1_b7.py`)** với quy mô **100 câu hỏi bài tập độc nhất**, nối tiếp vào danh sách bài học cấp độ **A1** (`lesson_order = 8`), cộng dồn động từ và từ vựng của Bài 7 vào 2 chuyên mục tra cứu, mở rộng trần kiến thức Đấu trường tới Bài 7, và chạy kịch bản kiểm thử toàn diện.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu.
>
> ---
>
> ### 🔍 2. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI & CHỐNG TRÙNG LẶP CÂU HỎI (`ZERO-BUG & ZERO-DUPLICATE QA PROTOCOL`)
> Antigravity IDE **BẮT BUỘC TUYỆT ĐỐI KHÔNG ĐƯỢC MẮC LẠI** bất kỳ lỗi nào từng xuất hiện trước đây:
>
> 1. **Chống trùng lặp câu hỏi 100% (`Strict Deduplication Check`)**:
>    * Toàn bộ **100 câu hỏi** trong Bài 7 (`seed_a1_b7.py`) phải hoàn toàn khác biệt nhau về nội dung câu hỏi, ngữ cảnh, chủ ngữ và cấu trúc kiểm tra. Sau khi khởi tạo, kịch bản kiểm thử phải quét mã băm (`hash` / chuẩn hóa chuỗi `question`) để đảm bảo $100/100$ câu là duy nhất (`len(set(questions)) == 100`).
> 2. **Cấm dịch sai nghĩa hoặc thiếu phần dịch nghĩa (`No Missing/Wrong Translations`)**:
>    * 100% từ vựng, câu ví dụ trên thẻ từ vựng, bảng biểu lý thuyết, đoạn văn mẫu và 100% câu hỏi trong phần bài tập phải có bản dịch tiếng Việt chuẩn xác, tự nhiên. Tuyệt đối không để trống hoặc hiện `undefined` / `null`.
> 3. **Cấm dịch đáp án hoặc giải thích không liên quan đến đề bài (`Strict Atomic Alignment`)**:
>    * Khi tạo câu hỏi tĩnh cũng như khi chạy bộ sinh đề ngẫu nhiên (`Dynamic Randomizer`), **Đề bài (`question`) – Đáp án đúng (`correct_answer` / `accepted_answers`) – Bản dịch tiếng Việt của câu hỏi (`translation_vi`) – Lời giải thích (`explanation`)** phải được đóng gói trong cùng một hàm sinh nguyên tử (`Atomic Question Generator`).
>    * **Cấm tuyệt đối** việc đề bài hỏi về ngôi `ihr` hoặc nghề `Programmiererin` nhưng đáp án hoặc lời giải thích lại nói về ngôi `ich` hoặc nghề `Lehrer`!
> 4. **Cấm thiếu Voice hoặc Voice đọc sai ngôn ngữ (`100% Clean German TTS Voice`)**:
>    * Mọi thẻ từ vựng, mọi dòng chia động từ, mọi đoạn văn mẫu và mọi câu hỏi nghe (`nghe_dien`) phải có nút `🔊` hoạt động 100%.
>    * Hàm `speakGerman(text, rate)` chỉ được truyền chuỗi tiếng Đức sạch (`de-DE`), tuyệt đối không đọc lẫn nghĩa tiếng Việt, không đọc dấu gạch dưới `___`, mũi tên `->` hay ký hiệu `(m)/(f)/(n)/(Pl)`.
> 5. **Cấm đưa câu ví dụ không khớp với thẻ từ vựng đang học (`Exact Vocabulary-Example Matching`)**:
>    * Thẻ từ vựng đang dạy từ nào (ví dụ `der Krankenpfleger`, `die Werkstatt`, `die Baustelle`, `das Blumengeschäft`) thì câu ví dụ tiếng Đức (`example_de`) và dịch nghĩa (`example_vi`) **bắt buộc phải chứa chính xác từ vựng đó**.
> 6. **Đa dạng hóa Chủ ngữ, Ngữ cảnh & Biến thiên Số liệu (`Multi-Subject & Multi-Context Diversity`)**:
>    * Tuyệt đối không chỉ dùng mỗi ngôi `ich` hay chép y nguyên vài câu trong giáo trình. Phải luân phiên đủ 9 đại từ nhân xưng (`ich, du, er, sie, es, wir, ihr, sie, Sie`) và các danh từ/tên riêng (`Paula Rausch, Frank Müller, Petra May, mein Onkel, deine Tante, die Ärztin, der Koch, unsere Praktikanten...`) với giờ giấc và số lượng thay đổi liên tục.

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 $\rightarrow$ Bài 6 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 7**:

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung **14 động từ trọng tâm của Bài 7** (bao gồm bộ Động từ khuyết thiếu `Modalverben` và các động từ chỉ hoạt động nghề nghiệp), kèm phát âm `de-DE` cho từng ngôi và câu ví dụ chuẩn:
1. **`müssen`** (*phải, bắt buộc phải làm gì* — **Modalverb**, biến đổi nguyên âm gốc `ü -> u` ở số ít, ngôi `ich` và `er/sie/es` không có đuôi):
   * Chia theo ngôi: `ich muss`, `du musst`, `er/sie/es muss`, `wir müssen`, `ihr müsst`, `sie/Sie müssen`.
   * Ví dụ: *„Um sechs Uhr fünfzehn muss Paula aufstehen.“ (Lúc 6 giờ 15 phút Paula phải thức dậy.)*
2. **`können`** (*có thể, có khả năng / biết làm gì* — **Modalverb**, biến đổi nguyên âm gốc `ö -> a` ở số ít, ngôi `ich` và `er/sie/es` không có đuôi):
   * Chia theo ngôi: `ich kann`, `du kannst`, `er/sie/es kann`, `wir können`, `ihr könnt`, `sie/Sie können`.
   * Ví dụ: *„Mein Bruder kann sehr gut kochen und Autos reparieren.“ (Anh trai tôi có thể nấu ăn và sửa ô tô rất giỏi.)*
3. **`wollen`** (*muốn [ý định mạnh mẽ, kế hoạch]* — **Modalverb** mở rộng, biến đổi `o -> i` ở số ít):
   * Chia theo ngôi: `ich will`, `du willst`, `er/sie/es will`, `wir wollen`, `ihr wollt`, `sie/Sie wollen`.
   * Ví dụ: *„Nach dem Studium will mein Sohn als Programmierer arbeiten.“ (Sau khi học đại học xong, con trai tôi muốn làm việc với tư cách là lập trình viên.)*
4. **`dürfen`** (*được phép làm gì* — **Modalverb** mở rộng, biến đổi `ü -> a` ở số ít):
   * Chia theo ngôi: `ich darf`, `du darfst`, `er/sie/es darf`, `wir dürfen`, `ihr dürft`, `sie/Sie dürfen`.
   * Ví dụ: *„Im Krankenhaus darf man nicht rauchen.“ (Ở trong bệnh viện người ta không được phép hút thuốc.)*
5. **`sollen`** (*nên, được giao nhiệm vụ làm gì* — **Modalverb** mở rộng):
   * Chia theo ngôi: `ich soll`, `du sollst`, `er/sie/es soll`, `wir sollen`, `ihr sollt`, `sie/Sie sollen`.
   * Ví dụ: *„Die Sekretärin soll heute viele Kunden anrufen.“ (Nữ thư ký hôm nay cần phải gọi điện cho nhiều khách hàng.)*
6. **`unterrichten`** (*giảng dạy, dạy học* — Gốc kết thúc bằng `-t` nên thêm `-e-` ở ngôi `du, er/sie/es, ihr`; **KHÔNG tách**):
   * Chia theo ngôi: `ich unterrichte`, `du unterrichtest`, `er/sie/es unterrichtet`, `wir unterrichten`, `ihr unterrichtet`, `sie/Sie unterrichten`.
   * Ví dụ: *„Frau Weber unterrichtet Schüler an einer Schule in Berlin.“ (Bà Weber dạy học sinh tại một ngôi trường ở Berlin.)*
7. **`untersuchen`** (*khám bệnh, kiểm tra* — **KHÔNG tách**):
   * Chia theo ngôi: `ich untersuche`, `du untersuchst`, `er/sie/es untersucht`, `wir untersuchen`, `ihr untersucht`, `sie/Sie untersuchen`.
   * Ví dụ: *„Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus.“ (Bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện.)*
8. **`reparieren`** (*sửa chữa* — Động từ đuôi `-ieren`, quy tắc):
   * Chia theo ngôi: `ich repariere`, `du reparierst`, `er/sie/es repariert`, `wir reparieren`, `ihr repariert`, `sie/Sie reparieren`.
   * Ví dụ: *„Der KFZ-Mechatroniker repariert das Auto in einer Werkstatt.“ (Người thợ cơ khí ô tô sửa chiếc xe hơi ở trong một xưởng sửa chữa.)*
9. **`verkaufen`** (*bán hàng* — Tiền tố `ver-` không tách):
   * Chia theo ngôi: `ich verkaufe`, `du verkaufst`, `er/sie/es verkauft`, `wir verkaufen`, `ihr verkauft`, `sie/Sie verkaufen`.
   * Ví dụ: *„Die Verkäuferin verkauft moderne Schuhe im Schuhgeschäft.“ (Nữ nhân viên bán hàng bán những đôi giày hiện đại ở trong cửa hàng giày.)*
10. **`schneiden`** (*cắt [tóc, giấy, bánh...]* — Gốc kết thúc bằng `-d` nên thêm `-e-` ở `du schneidest, er/sie/es schneidet, ihr schneidet`):
    * Chia theo ngôi: `ich schneide`, `du schneidest`, `er/sie/es schneidet`, `wir schneiden`, `ihr schneidet`, `sie/Sie schneiden`.
    * Ví dụ: *„Der Friseur schneidet die Haare im Friseursalon.“ (Người thợ làm tóc cắt tóc ở trong tiệm làm tóc.)*
11. **`brauchen`** (*cần cái gì [+ Cách 4 Akkusativ]*):
    * Chia theo ngôi: `ich brauche`, `du brauchst`, `er/sie/es braucht`, `wir brauchen`, `ihr braucht`, `sie/Sie brauchen`.
    * Ví dụ: *„Bei ihrer Arbeit braucht Petra einen schnellen Computer und einen großen Schreibtisch.“ (Trong công việc của mình, Petra cần một chiếc máy tính nhanh và một cái bàn làm việc lớn.)*
12. **`bringen`** (*mang, đưa, dẫn [ai/cái gì đi đâu]*):
    * Chia theo ngôi: `ich bringe`, `du bringst`, `er/sie/es bringt`, `wir bringen`, `ihr bringt`, `sie/Sie bringen`.
    * Ví dụ: *„Um acht Uhr dreißig muss Frank seine Tochter in den Kindergarten bringen.“ (Lúc 8 giờ 30 phút Frank phải đưa con gái mình đến trường mẫu giáo.)*
13. **`abholen`** (*đón [ai], lấy [đồ]* — **Động từ tách** `ab-` + `holen`):
    * Chia theo ngôi: `ich hole ... ab`, `du holst ... ab`, `er/sie/es holt ... ab`, `wir holen ... ab`, `ihr holt ... ab`, `sie/Sie holen ... ab`.
    * Ví dụ: *„Am Nachmittag holt die Mutter ihren Sohn vom Kindergarten ab.“ (Vào buổi chiều người mẹ đón con trai của mình từ trường mẫu giáo về.)*
14. **`schlafen`** (*ngủ* — **Biến âm `a -> ä`** ở `du schläfst, er/sie/es schläft`):
    * Chia theo ngôi: `ich schlafe`, `du schläfst`, `er/sie/es schläft`, `wir schlafen`, `ihr schlaft`, `sie/Sie schlafen`.
    * Ví dụ: *„Herr Müller hat heute Ferien, deshalb kann er bis sieben Uhr schlafen.“ (Hôm nay ông Müller có kỳ nghỉ nên ông ấy có thể ngủ đến 7 giờ.)*

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung 2 chủ đề lọc mới của Bài 7 với đầy đủ **50 danh từ có mạo từ (`der/die/das`), dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng thẻ từ vựng**:
1. **`Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)`** *(Bao gồm đầy đủ cặp danh từ nam `der` và danh từ nữ `die ...-in`)*
2. **`Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)`**

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 7: "BERUF - MODALVERBEN - ARTIKELWÖRTER IN AKKUSATIV" & PHÂN BIỆT AKKUSATIV VS. DATIV

Bài học thứ 8 trong danh sách Cấp độ A1 (`lesson_order = 8`):
* **Tiêu đề bài học**: `Bài 7: Beruf - Modalverben - Artikelwörter in Akkusativ (Nghề nghiệp - Động từ khuyết thiếu - Từ hạn định Cách 4 & Phân biệt Akkusativ / Dativ)`
* **Mô tả ngắn**: `Nắm vững hệ thống từ vựng Nghề nghiệp (Nam/Nữ), Nơi làm việc và cấu trúc hỏi đáp nghề nghiệp chuẩn Đức; làm chủ các Động từ khuyết thiếu (möchten, müssen, können, wollen, dürfen, sollen) và cấu trúc khung câu (Satzklammer); hệ thống bảng ma trận Từ hạn định ở Cách 4 (Artikelwörter im Akkusativ) và Cẩm nang Chuyên sâu Phân biệt Cách 4 (Akkusativ) vs. Cách 3 (Dativ).`

---

### HỌC PHẦN 1: NGHỀ NGHIỆP (`BERUFE`), NƠI LÀM VIỆC (`ARBEITSORTE`) & CẤU TRÚC HỎI ĐÁP NGHỀ NGHIỆP

#### 1.1. Quy tắc Cấu tạo Danh từ Nghề nghiệp Nam (`Maskulinum - der`) $\rightarrow$ Nữ (`Femininum - die`)
1. **Quy tắc chung (90% các nghề)**: Lấy danh từ chỉ nghề nghiệp của **Nam (`der ...`)** cộng thêm hậu tố **`-in`** để tạo thành danh từ chỉ nghề nghiệp của **Nữ (`die ...-in`)**.
   * Khi chuyển sang **Số nhiều (`Plural`)**:
     * Nghề nghiệp Nam thường giữ nguyên(với đuôi `-er`) hoặc thêm `-en`/`-e`.
     * Nghề nghiệp Nữ (`die ...-in`) khi sang số nhiều **bắt buộc gấp đôi chữ `n` thành `-innen`** (ví dụ: `die Lehrerin` $\rightarrow$ `die Lehrerinnen`, `die Ärztin` $\rightarrow$ `die Ärztinnen`).
2. **Nhóm biến âm Umlaut (`a -> ä`, `o -> ö`, `u -> ü`) khi chuyển sang Nữ**:
   * **`der Arzt`** *(bác sĩ nam)* $\longrightarrow$ **`die Ärztin`** *(bác sĩ nữ)*
   * **`der Koch`** *(đầu bếp nam)* $\longrightarrow$ **`die Köchin`** *(đầu bếp nữ)*
   * **`der Bauer`** *(nông dân nam)* $\longrightarrow$ **`die Bäuerin`** *(nông dân nữ)*
3. **Nhóm đổi từ gốc đặc biệt**:
   * **`der Hausmann`** *(người đàn ông nội trợ)* $\longrightarrow$ **`die Hausfrau`** *(người phụ nữ nội trợ)*
   * **`der Krankenpfleger`** *(nam y tá / điều dưỡng)* $\longrightarrow$ **`die Krankenpflegerin`** hoặc **`die Krankenschwester`** *(nữ y tá / điều dưỡng)*
   * **`der Kaufmann`** *(nam nhân viên thương mại / doanh nhân)* $\longrightarrow$ **`die Kauffrau`** *(nữ nhân viên thương mại)*

#### 1.2. Bảng 1: Tổng Hợp 16 Cặp Nghề Nghiệp Trọng Tâm (Nam – Nữ – Số Nhiều – Nghĩa – Câu Ví Dụ `🔊 de-DE`)
| STT | Nghề Nghiệp Nam (`Maskulinum - der`) | Nghề Nghiệp Nữ (`Femininum - die`) | Nghĩa Tiếng Việt | Hoạt Động Đặc Trưng & Nơi Làm Việc (`Tätigkeit & Arbeitsort`) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **der Programmierer**<br>*(Pl: die Programmierer)* | **die Programmiererin**<br>*(Pl: die Programmiererinnen)* | lập trình viên | *schreibt Computerprogramme **im Büro** / **in einer IT-Firma*** *(viết chương trình máy tính ở văn phòng / công ty IT)* |
| **2** | **der Taxifahrer**<br>*(Pl: die Taxifahrer)* | **die Taxifahrerin**<br>*(Pl: die Taxifahrerinnen)* | tài xế taxi | *fährt Fahrgäste **mit dem Taxi** durch die Stadt* *(chở hành khách bằng taxi khắp thành phố)* |
| **3** | **der Krankenpfleger**<br>*(Pl: die Krankenpfleger)* | **die Krankenpflegerin** /<br>**die Krankenschwester** | y tá, điều dưỡng | *hilft den Ärzten und pflegt Patienten **im Krankenhaus*** *(giúp các bác sĩ và chăm sóc bệnh nhân ở bệnh viện)* |
| **4** | **der Florist**<br>*(Pl: die Floristen)* | **die Floristin**<br>*(Pl: die Floristinnen)* | người bán hoa, nghệ nhân cắm hoa | *verkauft schöne Blumen **im Blumengeschäft*** *(bán những bông hoa đẹp ở cửa hàng hoa)* |
| **5** | **der Verkäufer**<br>*(Pl: die Verkäufer)* | **die Verkäuferin**<br>*(Pl: die Verkäuferinnen)* | nhân viên bán hàng | *verkauft Schuhe **im Schuhgeschäft** oder Lebensmittel **im Supermarkt*** *(bán giày ở tiệm giày hoặc thực phẩm ở siêu thị)* |
| **6** | **der (KFZ-)Mechatroniker**<br>*(Pl: die Mechatroniker)* | **die (KFZ-)Mechatronikerin**<br>*(Pl: die Mechatronikerinnen)* | thợ cơ khí (thợ sửa chữa ô tô) | *repariert Autos und Motoren **in einer Werkstatt*** *(sửa chữa ô tô và động cơ ở trong một xưởng)* |
| **7** | **der Trainer**<br>*(Pl: die Trainer)* | **die Trainerin**<br>*(Pl: die Trainerinnen)* | huấn luyện viên | *trainiert Sportler **im Fitnessstudio** oder **im Stadion*** *(huấn luyện vận động viên ở phòng tập hoặc sân vận động)* |
| **8** | **der Lehrer**<br>*(Pl: die Lehrer)* | **die Lehrerin**<br>*(Pl: die Lehrerinnen)* | giáo viên | *unterrichtet Schüler **an einer Schule** oder **im Sprachzentrum*** *(giảng dạy học sinh tại một trường học hoặc trung tâm ngoại ngữ)* |
| **9** | **der Schüler**<br>*(Pl: die Schüler)* | **die Schülerin**<br>*(Pl: die Schülerinnen)* | học sinh (cấp 1–3) | *lernt viele Fächer **in der Schule*** *(học nhiều môn học ở trường phổ thông)* |
| **10** | **der Student**<br>*(Pl: die Studenten)* | **die Studentin**<br>*(Pl: die Studentinnen)* | sinh viên (đại học) | *studiert **an der Universität** / **an einer Hochschule*** *(học đại học tại trường đại học)* |
| **11** | **der Sekretär**<br>*(Pl: die Sekretäre)* | **die Sekretärin**<br>*(Pl: die Sekretärinnen)* | thư ký | *schreibt E-Mails und ruft Kunden **im Büro** an* *(viết email và gọi điện cho khách hàng ở trong văn phòng)* |
| **12** | **der Friseur**<br>*(Pl: die Friseure)* | **die Friseurin**<br>*(Pl: die Friseurinnen)* | thợ cắt tóc, tạo mẫu tóc | *schneidet Haare **im Friseursalon*** *(cắt tóc ở trong tiệm làm tóc)* |
| **13** | **der Kellner**<br>*(Pl: die Kellner)* | **die Kellnerin**<br>*(Pl: die Kellnerinnen)* | nhân viên phục vụ bàn, bồi bàn | *bedient Gäste **im Restaurant** oder **im Café*** *(phục vụ thực khách ở trong nhà hàng hoặc quán cà phê)* |
| **14** | **der Koch** ⚠️<br>*(Pl: die Köche)* | **die K<u>ö</u>chin** ⚠️<br>*(Pl: die Köchinnen)* | đầu bếp | *kocht leckere Speisen **im Restaurant** / **in der Kantine*** *(nấu những món ăn ngon ở nhà hàng / nhà ăn)* |
| **15** | **der Arzt** ⚠️<br>*(Pl: die Ärzte)* | **die <u>Ä</u>rztin** ⚠️<br>*(Pl: die Ärztinnen)* | bác sĩ | *untersucht Patienten **im Krankenhaus** oder **in einer Arztpraxis*** *(khám cho bệnh nhân ở bệnh viện hoặc phòng khám)* |
| **16** | **der Hausmann** ⚠️<br>*(Pl: die Hausmänner)* | **die Haus<u>frau</u>** ⚠️<br>*(Pl: die Hausfrauen)* | người nội trợ | *arbeitet **zu Hause**, kocht und kümmert sich um die Familie* *(làm việc ở nhà, nấu ăn và chăm sóc gia đình)* |

---

#### 1.3. Bảng 2: Từ Vựng Các Nơi Làm Việc (`Arbeitsorte`) & Cách Dùng Giới Từ Vị Trí (`Wo arbeiten Sie?` $\rightarrow$ `Dativ`)
> **Câu hỏi nơi làm việc**: **`Wo arbeiten Sie?`** *(Ngài làm việc ở đâu?)* / **`Wo arbeitet er/sie?`** *(Anh ấy/Cô ấy làm việc ở đâu?)*
> * Vì câu hỏi là **`Wo?` *(Ở đâu? — Vị trí tĩnh)***, mọi danh từ chỉ nơi làm việc đi sau giới từ **`in`** hoặc **`an`** đều **bắt buộc chia ở Cách 3 (`Dativ`)**:
>   * Với danh từ giống đực (`der`) và giống trung (`das`): **`in + dem = im`** (*im Friseursalon, im Krankenhaus, im Büro, im Restaurant, im Blumengeschäft, im Schuhgeschäft, im Sprachzentrum*).
>   * Với danh từ giống cái (`die`): **`in + der = in der`** hoặc **`an + einer = an einer`** (*in der Schule / an einer Schule, an der Universität, in einer Werkstatt, auf einer Baustelle, in einer Firma*).

| Giống Danh Từ | Danh Từ Nguyên Mẫu (`Nominativ`) | Dạng Số Nhiều (`Plural`) | Nghĩa Tiếng Việt | Cụm Trả Lời Câu Hỏi `Wo arbeiten Sie?` (`+ Dativ`) |
| :--- | :--- | :--- | :--- | :--- |
| <span style="color:#3b82f6">**Giống đực (`der`)**</span> | **der Friseursalon** | die Friseursalons | tiệm làm tóc, salon tóc | **im** Friseursalon *(in dem Friseursalon)* |
| <span style="color:#3b82f6">**Giống đực (`der`)**</span> | **der Supermarkt** | die Supermärkte | siêu thị | **im** Supermarkt *(in dem Supermarkt)* |
| <span style="color:#3b82f6">**Giống đực (`der`)**</span> | **der Kindergarten** | die Kindergärten | trường mẫu giáo, nhà trẻ | **im** Kindergarten *(in dem Kindergarten)* |
| <span style="color:#f43f5e">**Giống cái (`die`)**</span> | **die Schule** | die Schulen | trường học (phổ thông) | **an einer** Schule / **in der** Schule |
| <span style="color:#f43f5e">**Giống cái (`die`)**</span> | **die Universität** | die Universitäten | trường đại học | **an der** Universität / **an einer** Universität |
| <span style="color:#f43f5e">**Giống cái (`die`)**</span> | **die Werkstatt** | die Werkstätten | xưởng sửa chữa | **in einer** Werkstatt / **in der** Werkstatt |
| <span style="color:#f43f5e">**Giống cái (`die`)**</span> | **die Baustelle** | die Baustellen | công trường xây dựng | **auf einer** Baustelle / **auf der** Baustelle |
| <span style="color:#f43f5e">**Giống cái (`die`)**</span> | **die Firma** | die Firmen | công ty | **in einer** Firma / **bei einer** Firma |
| <span style="color:#10b981">**Giống trung (`das`)**</span> | **das Krankenhaus** | die Krankenhäuser | bệnh viện | **im** Krankenhaus *(in dem Krankenhaus)* |
| <span style="color:#10b981">**Giống trung (`das`)**</span> | **das Büro** | die Büros | văn phòng | **im** Büro *(in dem Büro)* |
| <span style="color:#10b981">**Giống trung (`das`)**</span> | **das Restaurant** | die Restaurants | nhà hàng | **im** Restaurant *(in dem Restaurant)* |
| <span style="color:#10b981">**Giống trung (`das`)**</span> | **das Blumengeschäft** | die Blumengeschäfte | cửa hàng hoa | **im** Blumengeschäft *(in dem Blumengeschäft)* |
| <span style="color:#10b981">**Giống trung (`das`)**</span> | **das Schuhgeschäft** | die Schuhgeschäfte | cửa hàng giày dép | **im** Schuhgeschäft *(in dem Schuhgeschäft)* |
| <span style="color:#10b981">**Giống trung (`das`)**</span> | **das Sprachzentrum** | die Sprachzentren | trung tâm ngoại ngữ | **im** Sprachzentrum *(VD: im Amanda Sprachzentrum)* |

---

#### 1.4. Bảng 3: Ba Mẫu Câu Hỏi & Ba Cách Trả Lời Nghề Nghiệp Chuẩn Ngữ Pháp
> ⚠️ **Quy tắc Ngữ pháp Quan trọng**: Khi nói nghề nghiệp của một người bằng cấu trúc `sein + [Nghề]` hoặc `arbeiten als + [Nghề]`, trong tiếng Đức **TUYỆT ĐỐI KHÔNG DÙNG MẠO TỪ `ein/eine`** trước danh từ chỉ nghề nghiệp! (Ví dụ: Nói *„Ich bin Lehrer.“* hoặc *„Ich arbeite als Florist.“*, **không** nói *„Ich bin ein Lehrer“*). Chỉ dùng `ein/eine` khi có thêm tính từ đứng trước danh từ nghề nghiệp (VD: *„Er ist ein guter Arzt.“*).

| 3 Câu Hỏi Nghề Nghiệp Thông Dụng (`🔊 de-DE`) | 3 Cấu Trúc Trả Lời Chuẩn Xác (`🔊 de-DE`) | Dịch Nghĩa Tiếng Việt |
| :--- | :--- | :--- |
| **1. `Was sind Sie von Beruf?`** *(Trang trọng)*<br>*(hoặc thân mật: **`Was bist du von Beruf?`**)* | **Cách 1: `[Chủ ngữ] + sein + [Nghề nghiệp].`**<br>$\rightarrow$ *„Ich bin **Schüler** / **Ärztin**.“* | Bạn / Ngài làm nghề gì?<br>$\rightarrow$ Tôi là học sinh / nữ bác sĩ. |
| **2. `Was machen Sie beruflich?`** *(Trang trọng)*<br>*(hoặc thân mật: **`Was machst du beruflich?`**)* | **Cách 2: `[Chủ ngữ] + sein + [Nghề nghiệp] + von Beruf.`**<br>$\rightarrow$ *„Ich bin **Lehrer** von Beruf.“* / *„Er ist **Koch** von Beruf.“* | Công việc chuyên môn của Ngài là gì?<br>$\rightarrow$ Nghề nghiệp của tôi là giáo viên. / Nghề của anh ấy là đầu bếp. |
| **3. `Was ist Ihr Beruf?`** *(Trang trọng)*<br>*(hoặc thân mật: **`Was ist dein Beruf?`**)* | **Cách 3: `[Chủ ngữ] + arbeiten als + [Nghề nghiệp].`**<br>$\rightarrow$ *„Ich arbeite **als Florist**.“* / *„Sie arbeitet **als Programmiererin**.“* | Nghề nghiệp của Ngài là gì?<br>$\rightarrow$ Tôi làm nghề bán hoa. / Cô ấy làm nghề lập trình viên. |

---

### HỌC PHẦN 2: ĐỘNG TỪ KHUYẾT THIẾU (`MODALVERBEN`) & CẤU TRÚC KHUNG CÂU (`SATZKLAMMER`)

#### 2.1. Đặc điểm Ngữ pháp Cốt lõi của Động từ Khuyết thiếu (`Modalverben`)
1. **Quy tắc Chia Động từ Khuyết thiếu ở Thì Hiện tại (`Präsens`)**:
   * **Số ít (`ich, du, er/sie/es`)**: Hầu hết các động từ khuyết thiếu (trừ `sollen` và `möchten`) đều **đổi nguyên âm gốc** (`müssen -> muss-`, `können -> kann-`, `wollen -> will-`, `dürfen -> darf-`).
   * **Ngôi thứ 1 (`ich`) và Ngôi thứ 3 số ít (`er/sie/es`) GIỐNG HỆT NHAU và KHÔNG CÓ ĐUÔI `-e` hay `-t`** (trừ `möchte`):
     * `ich muss` = `er/sie/es muss` *(tuyệt đối không viết musse hay musst!)*
     * `ich kann` = `er/sie/es kann` *(tuyệt đối không viết kanne hay kannt!)*
     * `ich will` = `er/sie/es will` | `ich darf` = `er/sie/es darf` | `ich soll` = `er/sie/es soll`.
     * Riêng **`möchten`**: `ich möchte` = `er/sie/es möchte` *(ngôi `er/sie/es` không thêm `-t`)*.
   * **Số nhiều (`wir, ihr, sie/Sie`)**: Giữ nguyên nguyên âm gốc của động từ nguyên mẫu (`müssen, müsst`, `können, könnt`).

#### 2.2. Bảng Ma Trận Chia Đầy Đủ 6 Động Từ Khuyết Thiếu Theo Từng Ngôi Nhân Xưng
| Ngôi Nhân Xưng | 1. **`möchten`**<br>*(muốn - lịch sự)*<br>⭐ Trọng tâm B7 | 2. **`müssen`**<br>*(phải, bắt buộc)*<br>⭐ Trọng tâm B7 | 3. **`können`**<br>*(có thể, biết làm)*<br>⭐ Trọng tâm B7 | 4. **`wollen`**<br>*(muốn - ý chí mạnh)*<br>*(Mở rộng)* | 5. **`dürfen`**<br>*(được phép)*<br>*(Mở rộng)* | 6. **`sollen`**<br>*(nên, có bổn phận)*<br>*(Mở rộng)* |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`ich`** *(tôi)* | **möchte** | <span style="color:#f59e0b">**muss**</span> | <span style="color:#10b981">**kann**</span> | **will** | **darf** | **soll** |
| **`du`** *(bạn)* | **möchtest** | <span style="color:#f59e0b">**musst**</span> | <span style="color:#10b981">**kannst**</span> | **willst** | **darfst** | **sollst** |
| **`er / sie / es`** *(anh/cô ấy/nó)* | **möchte** ⚠️ | <span style="color:#f59e0b">**muss**</span> ⚠️ | <span style="color:#10b981">**kann**</span> ⚠️ | **will** ⚠️ | **darf** ⚠️ | **soll** ⚠️ |
| **`wir`** *(chúng tôi)* | **möchten** | **müssen** | **können** | **wollen** | **dürfen** | **sollen** |
| **`ihr`** *(các bạn)* | **möchtet** | **müsst** | **könnt** | **wollt** | **dürft** | **sollt** |
| **`sie / Sie`** *(họ / Ngài)* | **möchten** | **müssen** | **können** | **wollen** | **dürfen** | **sollen** |

---

#### 2.3. Cấu trúc Khung Câu (`Satzklammer`) Khi Dùng `Modalverben` & Trường Hợp Kết Hợp Động Từ Tách (`Trennbare Verben`)
$$\text{Vị trí 1 (Chủ ngữ / Trạng từ)} + \underbrace{\textbf{Modalverb (Chia theo Chủ ngữ)}}_{\text{Vị trí số 2 cố định}} + \text{Thành phần giữa câu (Thời gian, Tân ngữ, Nơi chốn)} + \underbrace{\textbf{Động từ chính (Nguyên mẫu - Infinitiv)}}_{\text{Đứng ở CUỐI CÙNG của câu}}$$

* **Trường hợp 1 — Với động từ thường**:
  * *„Ich **möchte** jetzt einen Kaffee **trinken**.“* *(Tôi muốn uống một tách cà phê bây giờ.)*
  * *„Heute **muss** ich viele Hausaufgaben **machen**.“* *(Hôm nay tôi phải làm nhiều bài tập về nhà.)*
  * *„Mein Vater **kann** sehr gut **kochen**.“* *(Bố tôi có thể nấu ăn rất giỏi.)*
* **Trường hợp 2 — Với ĐỘNG TỪ TÁCH (`aufstehen`, `abholen`, `fernsehen`, `anrufen`, `einkaufen`...)**:
  > 💡 **Quy tắc Vàng**: Khi trong câu có mặt **Động từ khuyết thiếu (`Modalverb`)**, động từ tách **KHÔNG TÁCH NỮA** mà **gộp liền lại thành dạng nguyên mẫu (`Infinitiv`) và đứng ở cuối câu**!
  * *Khi KHÔNG có Modalverb (Tách tiền tố ra cuối câu)*:
    * *„Paula **steht** jeden Tag um 6.15 Uhr **auf**.“*
    * *„Sie **holt** um 16.30 Uhr ihre Tochter vom Kindergarten **ab**.“*
    * *„Von 20 bis 22 Uhr **sieht** sie **fern**.“*
  * *Khi CÓ Modalverb (Gộp liền tiền tố + gốc thành nguyên mẫu ở cuối câu)*:
    * *„Um 6.15 Uhr **muss** Paula **<u>aufstehen</u>**.“* *(Lúc 6 giờ 15 phút Paula phải thức dậy.)*
    * *„Um 16.30 Uhr **muss** sie ihre Tochter vom Kindergarten **<u>abholen</u>**.“* *(Lúc 16 giờ 30 phút cô ấy phải đón con gái từ trường mẫu giáo.)*
    * *„Von 20 bis 22 Uhr **kann** sie **<u>fernsehen</u>**.“* *(Từ 20 đến 22 giờ cô ấy có thể xem tivi.)*
    * *„Petra **muss** ihre Kunden oft **<u>anrufen</u>**.“* *(Petra thường xuyên phải gọi điện cho khách hàng của cô ấy.)*

---

### HỌC PHẦN 3: HỆ THỐNG BẢNG MA TRẬN TỪ HẠN ĐỊNH Ở CÁCH 4 (`ARTIKELWÖRTER IM AKKUSATIV`)

#### 3.1. Bảng 1: Bảng Tổng Hợp 4 Loại Từ Hạn Định Ở Cách 4 (`Artikelwörter im Akkusativ` — Bảng Chuẩn Trên Bảng Viết)
> **Quy tắc bất biến của Cách 4 (`Akkusativ`)**:
> * Chỉ duy nhất **Giống đực (`Maskulinum - der`)** biến đổi toàn bộ đuôi từ hạn định sang **`-en`**: **`den / einen / keinen / meinen (deinen, seinen, ihren, unseren, euren, Ihren)`**.
> * **Giống cái (`Femininum - die`)**, **Giống trung (`Neutrum - das`)** và **Số nhiều (`Plural - die`)** **GIỮ NGUYÊN 100%** giống hệt như ở Cách 1 (`Nominativ`)!

| Giống của Danh từ (`Genus`) | 1. Mạo từ xác định<br>(`bestimmter Artikel`) | 2. Mạo từ không xác định<br>(`unbestimmter Artikel`) | 3. Phủ định với `kein`<br>(`Verneinung mit kein`) | 4. Mạo từ sở hữu<br>(`Possessivartikel`) |
| :--- | :---: | :---: | :---: | :---: |
| <span style="color:#3b82f6">**`m` — Giống đực (`Maskulinum`)**</span> ⚠️ | **<u>den</u> Tisch** | **<u>einen</u> Tisch** | **<u>keinen</u> Tisch** | **<u>meinen</u> Tisch** |
| <span style="color:#f43f5e">**`f` — Giống cái (`Femininum`)**</span> | **die Tasche** | **eine Tasche** | **keine Tasche** | **meine Tasche** |
| <span style="color:#10b981">**`n` — Giống trung (`Neutrum`)**</span> | **das Buch** | **ein Buch** | **kein Buch** | **mein Buch** |
| <span style="color:#a855f7">**`Pl` — Số nhiều (`Plural`)**</span> | **die Bücher** | **— Bücher** | **keine Bücher** | **meine Bücher** |

#### 3.2. Bảng 2: Ma Trận Mạo Từ Sở Hữu Ở Cách 4 (`Possessivartikel im Akkusativ`) Theo Đầy Đủ 9 Ngôi Nhân Xưng
| Ngôi Nhân Xưng | Gốc Sở Hữu | Giống Đực (`m`) ⚠️<br>*(+ `-en`: Computer / Tisch)* | Giống Cái (`f`)<br>*(+ `-e`: Tochter / Tasche)* | Giống Trung (`n`)<br>*(giữ nguyên: Auto / Buch)* | Số Nhiều (`Pl`)<br>*(+ `-e`: Kunden / Bücher)* |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1. `ich` (tôi)** | `mein-` | **mein<u>en</u>** Computer | **meine** Tochter | **mein** Auto | **meine** Kunden |
| **2. `du` (bạn)** | `dein-` | **dein<u>en</u>** Computer | **deine** Tochter | **dein** Auto | **deine** Kunden |
| **3. `er / es` (anh ấy / nó)** | `sein-` | **sein<u>en</u>** Computer | **seine** Tochter | **sein** Auto | **seine** Kunden |
| **4. `sie` (cô ấy)** | `ihr-` | **ihr<u>en</u>** Computer | **ihre** Tochter | **ihr** Auto | **ihre** Kunden |
| **5. `wir` (chúng tôi)** | `unser-` | **unser<u>en</u>** Computer | **unsere** Tochter | **unser** Auto | **unsere** Kunden |
| **6. `ihr` (các bạn)** ⚠️ | `euer-` | **eur<u>en</u>** Computer | **eure** Tochter | **euer** Auto | **eure** Kunden |
| **7. `sie` (họ)** | `ihr-` | **ihr<u>en</u>** Computer | **ihre** Tochter | **ihr** Auto | **ihre** Kunden |
| **8. `Sie` (Ngài)** | `Ihr-` | **Ihr<u>en</u>** Computer | **Ihre** Tochter | **Ihr** Auto | **Ihre** Kunden |

---

### HỌC PHẦN 4: CHUYÊN ĐỀ ĐẶC BIỆT — CẨM NANG PHÂN BIỆT TOÀN DIỆN CÁCH 4 (`AKKUSATIV`) VÀ CÁCH 3 (`DATIV`)
*(Chuyên đề trọng tâm theo yêu cầu: Khi nào bắt buộc dùng `Akkusativ` (Cách 4)? Khi nào bắt buộc dùng `Dativ` (Cách 3)? Đối chiếu qua các cặp ví dụ cụ thể)*

Để không bao giờ nhầm lẫn giữa **Cách 4 (`Akkusativ`)** và **Cách 3 (`Dativ`)**, người học chỉ cần xét **3 tiêu chí phân loại cốt lõi** dưới đây:

#### TIÊU CHÍ 1: Phân biệt theo ĐỘNG TỪ & VAI TRÒ TÂN NGỮ TRONG CÂU (`Verb & Objekt`)
| Đặc điểm So sánh | CÁCH 4: `AKKUSATIV` *(Tân ngữ trực tiếp)* | CÁCH 3: `DATIV` *(Tân ngữ gián tiếp)* |
| :--- | :--- | :--- |
| **1. Câu hỏi nhận diện** | • **`Wen?`** *(Ai? — cho người)*<br>• **`Was?`** *(Cái gì? — cho vật)* | • **`Wem?`** *(Cho ai? / Với ai?)* |
| **2. Bản chất ngữ pháp** | Chỉ **đối tượng trực tiếp chịu tác động** của hành động (vật được mua, được cần, được sửa, người được gọi điện/khám bệnh...). **90% động từ tiếng Đức đi với `Akkusativ`!** | Chỉ **người nhận lợi ích/tác động gián tiếp** từ hành động, hoặc đi sau một nhóm **động từ đặc biệt quy định `Dativ`**. |
| **3. Danh sách Động từ điển hình** | • **`haben`** *(có)*, **`brauchen`** *(cần)*, **`suchen`** *(tìm)*, **`finden`** *(thấy)*<br>• **`kaufen`** *(mua)*, **`verkaufen`** *(bán)*, **`reparieren`** *(sửa)*<br>• **`schreiben`** *(viết)*, **`lesen`** *(đọc)*, **`machen`** *(làm)*<br>• **`trinken`** *(uống)*, **`essen`** *(ăn)*, **`nehmen`** *(dùng)*<br>• **`untersuchen`** *(khám)*, **`unterrichten`** *(dạy)*, **`anrufen`** *(gọi điện)*, **`abholen`** *(đón)*, **`besuchen`** *(thăm)*<br>• Cấu trúc **`es gibt + Akkusativ`** *(có cái gì)*. | • **`helfen`** *(giúp đỡ ai)*<br>• **`danken`** *(cảm ơn ai)*<br>• **`gefallen`** *(làm ai thích / hợp ý ai)*<br>• **`gehören`** *(thuộc về ai)*<br>• **`antworten`** *(trả lời ai)*<br>• **`gratulieren`** *(chúc mừng ai)*<br>• **`schmecken`** *(ngon miệng đối với ai)*<br>• **`passen`** *(vừa vặn với ai)*. |
| **4. Ví dụ cụ thể đối chiếu trực tiếp (`🔊 de-DE`)** | • *„Petra braucht **<u>einen</u> Computer** und **<u>einen</u> großen Schreibtisch**.“* *(Petra cần một chiếc máy tính và một cái bàn làm việc lớn — `Computer` & `Schreibtisch` là vật được cần trực tiếp $\rightarrow$ `Akkusativ`).*<br>• *„Der Arzt untersucht **<u>den</u> Patienten**.“* *(Bác sĩ khám cho người bệnh nhân $\rightarrow$ `untersuchen + Akkusativ`).*<br>• *„Sie muss **<u>ihre</u> Kunden** oft anrufen.“* *(Cô ấy phải gọi điện cho các khách hàng của mình $\rightarrow$ `anrufen + Akkusativ`).* | • *„Der Krankenpfleger hilft **<u>dem</u> Arzt** im Krankenhaus.“* *(Người nam điều dưỡng giúp đỡ bác sĩ ở bệnh viện $\rightarrow$ `helfen + Dativ`: `der Arzt` $\rightarrow$ `dem Arzt`).*<br>• *„Die neue Arbeit gefällt **<u>meinem</u> Bruder** sehr gut.“* *(Công việc mới làm anh trai tôi rất thích $\rightarrow$ `gefallen + Dativ`: `mein Bruder` $\rightarrow$ `meinem Bruder`).*<br>• *„Das Auto gehört **<u>unserer</u> Chefin**.“* *(Chiếc ô tô thuộc về nữ giám đốc của chúng tôi $\rightarrow$ `gehören + Dativ`).* |

> 💡 **Trường hợp câu có CẢ 2 TÂN NGỮ (`Dativ` + `Akkusativ` trong cùng 1 câu)**:
> Khi các động từ chỉ sự trao tặng/đưa/gửi/mua cho ai (`geben` *đưa*, `schenken` *tặng*, `kaufen` *mua*, `schreiben` *viết*, `bringen` *mang cho*, `zeigen` *chỉ cho*) có cả **Người nhận** và **Vật được trao**:
> $$\text{\textbf{Người nhận (Wem?)}} \longrightarrow \textbf{Cách 3 (\texttt{Dativ})} \qquad \Big| \qquad \text{\textbf{Vật được trao (Was?)}} \longrightarrow \textbf{Cách 4 (\texttt{Akkusativ})}$$
> * **Ví dụ 1**: *„Der Chef gibt **<u>der</u> Sekretärin** (`Wem? -> Dativ`) **<u>einen</u> neuen Laptop** (`Was? -> Akkusativ`).“* *(Người sếp đưa **cho nữ thư ký** **một chiếc máy tính xách tay mới**.)*
> * **Ví dụ 2**: *„Ich kaufe **<u>meinem</u> Vater** (`Wem? -> Dativ`) **<u>einen</u> Mantel** (`Was? -> Akkusativ`).“* *(Tôi mua **cho bố tôi** **một chiếc áo khoác**.)*

---

#### TIÊU CHÍ 2: Phân biệt theo GIỚI TỪ CỐ ĐỊNH (`Reine Akkusativ-Präpositionen` vs. `Reine Dativ-Präpositionen`)
Có những giới từ mà hễ nhìn thấy chúng, ta lập tức chia danh từ phía sau ở `Akkusativ` hoặc `Dativ` mà không cần suy nghĩ:

| Nhóm Giới Từ LUÔN Đi Với CÁCH 4 (`AKKUSATIV`)<br>*(Mẹo nhớ: **`FUDGE-BO`** = `für, um, durch, gegen, entlang, bis, ohne`)* | Nhóm Giới Từ LUÔN Đi Với CÁCH 3 (`DATIV`)<br>*(Mẹo nhớ: **`mit, nach, aus, zu, von, bei, seit, ab, gegenüber`**)* |
| :--- | :--- |
| 1. **`für`** *(dành cho)*:<br>   • *„Das Telefon ist wichtig **für <u>sie</u>** / **für <u>den</u> Sekretär**.“* *(Điện thoại rất quan trọng đối với cô ấy / đối với nam thư ký.)*<br>   • *„Ich kaufe Blumen **für <u>meine</u> Mutter**.“*<br>2. **`ohne`** *(không có)*:<br>   • *„Herr Müller trinkt Kaffee **ohne <u>einen</u> Löffel** Zucker.“*<br>3. **`durch`** *(xuyên qua)*:<br>   • *„Der Taxifahrer fährt **durch <u>den</u> Park**.“* *(Tài xế taxi lái xe xuyên qua công viên.)*<br>4. **`um`** *(vào lúc [giờ] / xung quanh [không gian])*:<br>   • *„Die Familie sitzt **um <u>den</u> Esstisch**.“* *(Gia đình ngồi xung quanh bàn ăn.)*<br>5. **`gegen`** *(chống lại / đâm vào / khoảng)*:<br>   • *„Das Auto fährt **gegen <u>einen</u> Baum**.“* | 1. **`mit`** *(cùng với / bằng phương tiện)*:<br>   • *„Paula fährt **mit <u>dem</u> Bus** zur Arbeit.“*<br>2. **`bei`** *(ở tại chỗ ai / làm việc tại đâu / trong lúc)*:<br>   • *„**Bei <u>ihrer</u> Arbeit** (`die Arbeit -> Dativ`) braucht Petra einen Computer.“* *(Trong công việc của mình, Petra cần một chiếc máy tính.)*<br>3. **`von`** *(từ / của — `von + dem = vom`)*:<br>   • *„Paula holt ihre Tochter **<u>vom</u> Kindergarten** ab.“* *(Paula đón con gái từ trường mẫu giáo.)*<br>4. **`zu`** *(đến địa điểm — `zum / zur`)*:<br>   • *„Frank geht **<u>zum</u> Fußballtraining**.“* *(Frank đi đến buổi tập bóng đá.)*<br>5. **`aus`** *(ra khỏi / đến từ)* & **`nach`** *(tới thành phố/quốc gia, sau khi)*. |

---

#### TIÊU CHÍ 3: Phân biệt theo SỰ DI CHUYỂN (`Wohin?` $\rightarrow$ `Akkusativ`) vs. VỊ TRÍ TĨNH (`Wo?` $\rightarrow$ `Dativ`) Với 9 Giới Từ Chung (`in, an, auf, neben, vor, hinter, über, unter, zwischen`)
Đây là điểm ngữ pháp xuất hiện trực tiếp trong đoạn văn về **Frank Müller** trên bảng viết và cực kỳ quan trọng:

* **Khi câu trả lời cho câu hỏi `Wohin?` *(Đi đến đâu? / Đưa vào đâu?)* $\rightarrow$ Có sự di chuyển từ ngoài vào trong hoặc thay đổi vị trí** (thường đi với động từ `gehen` *đi*, `fahren` *lái xe*, `bringen` *đưa/mang vào*, `stellen` *đặt*, `legen` *để*):
  $$\text{Giới từ (`in, auf, an...`)} + \textbf{CÁCH 4 (\texttt{AKKUSATIV})} \quad (\text{Lưu ý viết tắt: } \textbf{\texttt{in + das = ins}}, \ \textbf{\texttt{an + das = ans}})$$
* **Khi câu trả lời cho câu hỏi `Wo?` *(Ở đâu?)* $\rightarrow$ Trạng thái tĩnh tại một chỗ, không di chuyển sang nơi khác** (thường đi với động từ `sein` *ở*, `arbeiten` *làm việc*, `schlafen` *ngủ*, `lernen` *học*, `stehen` *đứng*, `liegen` *nằm*, `sitzen` *ngồi*):
  $$\text{Giới từ (`in, auf, an...`)} + \textbf{CÁCH 3 (\texttt{DATIV})} \quad (\text{Lưu ý viết tắt: } \textbf{\texttt{in + dem = im}}, \ \textbf{\texttt{an + dem = am}})$$

##### Bảng Đối Chiếu Cặp Ví Dụ Thực Tế Song Song (`Wohin? + Akkusativ` vs. `Wo? + Dativ`)
| Danh Từ Gốc | Tình Huống 1: `Wohin?` *(Đưa đến đâu / Đi vào đâu)*<br>$\longrightarrow$ **Dùng CÁCH 4 (`AKKUSATIV`)** | Tình Huống 2: `Wo?` *(Đang ở đâu / Làm việc ở đâu)*<br>$\longrightarrow$ **Dùng CÁCH 3 (`DATIV`)** |
| :--- | :--- | :--- |
| **1. `der Kindergarten`**<br>*(trường mẫu giáo — Giống đực)* | *„Um 8.30 Uhr muss Frank die Tochter **in <u>den</u> Kindergarten** bringen.“*<br>*(Lúc 8:30 Frank phải đưa con gái **vào trường mẫu giáo** $\rightarrow$ Di chuyển `Wohin?` nên `der` đổi thành **`in den`**).* | *„Von 8.30 bis 16.00 Uhr spielt die Tochter **<u>im</u>** (**in <u>dem</u>**) **Kindergarten**.“*<br>*(Từ 8:30 đến 16:00 cô con gái chơi **ở trong trường mẫu giáo** $\rightarrow$ Vị trí tĩnh `Wo?` nên `der` đổi thành **`im / in dem`**).* |
| **2. `die Werkstatt`**<br>*(xưởng sửa xe — Giống cái)* | *„Um 12.30 Uhr bringt Frank das Auto **in <u>die</u> Werkstatt**.“*<br>*(Lúc 12:30 Frank mang chiếc ô tô **vào xưởng sửa chữa** $\rightarrow$ Di chuyển `Wohin?` nên `die` giữ nguyên là **`in die`**).* | *„Der KFZ-Mechatroniker repariert das Auto **in <u>der</u> Werkstatt** (hoặc **in <u>einer</u> Werkstatt**).“*<br>*(Người thợ cơ khí sửa chiếc ô tô **ở trong xưởng sửa chữa** $\rightarrow$ Vị trí tĩnh `Wo?` nên `die` đổi thành **`in der / in einer`**).* |
| **3. `das Bett`**<br>*(cái giường — Giống trung)* | *„Um 19 Uhr bringt Frank die Tochter **<u>ins</u>** (**in <u>das</u>**) **Bett**.“*<br>*(Lúc 19 giờ Frank đưa con gái **lên giường đi ngủ** $\rightarrow$ Di chuyển `Wohin?` nên `in + das` gộp thành **`ins Bett`**).* | *„Das Kind liegt schon **<u>im</u>** (**in <u>dem</u>**) **Bett** und schläft.“*<br>*(Đứa trẻ đã nằm **ở trên giường** và đang ngủ $\rightarrow$ Vị trí tĩnh `Wo?` nên `in + dem` gộp thành **`im Bett`**).* |
| **4. `das Büro`**<br>*(văn phòng — Giống trung)* | *„Jeden Morgen geht Petra um 8 Uhr **<u>ins</u>** (**in <u>das</u>**) **Büro**.“*<br>*(Mỗi sáng Petra đi **vào văn phòng** lúc 8 giờ $\rightarrow$ Di chuyển `Wohin?` $\rightarrow$ **`ins Büro`**).* | *„Petra arbeitet allein **<u>im</u>** (**in <u>dem</u>**) **Büro**.“*<br>*(Petra làm việc một mình **ở trong văn phòng** $\rightarrow$ Vị trí tĩnh `Wo?` $\rightarrow$ **`im Büro`**).* |
| **5. `die Schule`**<br>*(trường học — Giống cái)* | *„Die Schüler gehen um 7 Uhr **in <u>die</u> Schule**.“*<br>*(Các học sinh đi **đến trường** lúc 7 giờ $\rightarrow$ Di chuyển `Wohin?` $\rightarrow$ **`in die Schule`**).* | *„Der Lehrer unterrichtet Schüler **an <u>einer</u> Schule** / **in <u>der</u> Schule**.“*<br>*(Người giáo viên dạy học sinh **ở tại một ngôi trường** $\rightarrow$ Vị trí tĩnh `Wo?` $\rightarrow$ **`an einer / in der Schule`**).* |

---

### HỌC PHẦN 5: PHÂN TÍCH 3 ĐOẠN VĂN MẪU TRONG BÀI GIẢNG (`TEXTANALYSE & PRAXIS` — KÈM AUDIO `de-DE`)

Hiển thị đầy đủ 3 đoạn văn thực chiến từ bảng viết với nút **`🔊 Nghe đọc chuẩn (de-DE)`**, bản dịch tiếng Việt và phân tích từng điểm ngữ pháp:

#### 5.1. Đoạn văn 1: Một ngày làm việc của Lập trình viên Paula Rausch (`Modalverben + Động từ tách`)
* **Dữ kiện gốc**:
  * *Paula Rausch (35), Programmiererin*
  * *um 6.15 Uhr / aufstehen / müssen*
  * *um 7.15 Uhr / mit dem Bus zur Arbeit / fahren / müssen*
  * *von 7.30 bis 15 Uhr / arbeiten*
  * *um 16.30 Uhr / ihre Tochter / vom Kindergarten / abholen / müssen*
  * *um 18.30 Uhr / das Abendessen / machen*
  * *von 20 bis 22 Uhr / fernsehen / können*
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Paula Rausch ist 35 Jahre alt. Sie arbeitet **als Programmiererin**. Um 6.15 Uhr **muss** sie **aufstehen**. Um 7.15 Uhr **muss** sie **mit dem Bus zur Arbeit fahren**. Von 7.30 bis 15 Uhr **arbeitet** sie. Um 16.30 Uhr **muss** sie **ihre Tochter vom Kindergarten abholen**. Um 18.30 Uhr **macht** sie **das Abendessen**. Von 20 bis 22 Uhr **kann** sie **fernsehen**.“*
* **Dịch nghĩa tiếng Việt**:
  > *„Paula Rausch 35 tuổi. Cô ấy làm nghề lập trình viên. Lúc 6 giờ 15 phút cô ấy phải thức dậy. Lúc 7 giờ 15 phút cô ấy phải đi bằng xe buýt đến chỗ làm. Từ 7 giờ 30 đến 15 giờ cô ấy làm việc. Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo. Lúc 18 giờ 30 phút cô ấy làm bữa tối. Từ 20 đến 22 giờ cô ấy có thể xem tivi.“*

#### 5.2. Đoạn văn 2: Ngày nghỉ của Giáo viên Frank Müller (`Modalverben + Wohin? Akkusativ vs. Dativ`)
* **Dữ kiện gốc**:
  * *Frank Müller (36), Lehrer, hat Ferien*
  * *bis 7 Uhr / schlafen / können*
  * *um 8.30 Uhr / die Tochter / in den Kindergarten / bringen / müssen*
  * *um 12.30 Uhr / das Auto in die Werkstatt / bringen*
  * *von 17 bis 18.30 Uhr / zum Fußballtraining / gehen*
  * *um 19 Uhr / die Tochter / ins Bett / bringen*
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Frank Müller ist 36 Jahre alt. Er ist **Lehrer von Beruf**. Er hat Ferien. Bis 7 Uhr **kann** er **schlafen**. Um 8.30 Uhr **muss** er **die Tochter in den Kindergarten bringen**. Um 12.30 Uhr **bringt** er **das Auto in die Werkstatt**. Von 17 bis 18.30 Uhr **geht** er **zum Fußballtraining**. Um 19 Uhr **bringt** er **die Tochter ins Bett**.“*
* **Dịch nghĩa tiếng Việt**:
  > *„Frank Müller 36 tuổi. Nghề nghiệp của anh ấy là giáo viên. Anh ấy đang có kỳ nghỉ. Anh ấy có thể ngủ đến 7 giờ. Lúc 8 giờ 30 phút anh ấy phải đưa con gái đến trường mẫu giáo. Lúc 12 giờ 30 phút anh ấy mang chiếc ô tô vào xưởng sửa chữa. Từ 17 đến 18 giờ 30 phút anh ấy đi đến buổi tập bóng đá. Lúc 19 giờ anh ấy đưa con gái lên giường đi ngủ.“*

#### 5.3. Đoạn văn 3: Công việc tại Văn phòng của Petra May (`Artikelwörter im Nominativ, Akkusativ & Dativ`)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Das ist Petra May. **Bei ihrer Arbeit** (`Dativ`) braucht sie **einen Computer** (`Akkusativ - m`) und **einen großen Schreibtisch** (`Akkusativ - m`). Sie schreibt Computerprogramme. **Das Telefon** (`Nominativ - n`) ist wichtig **für sie** (`Akkusativ`). Sie **muss ihre Kunden** (`Akkusativ - Pl`) oft **anrufen**. Sie arbeitet allein **im Büro** (`Dativ - n`).“*
* **Dịch nghĩa tiếng Việt & Lưu ý ngữ pháp**:
  > *„Đây là Petra May. Trong công việc của mình, cô ấy cần một chiếc máy tính và một chiếc bàn làm việc lớn. Cô ấy viết các chương trình máy tính. Chiếc điện thoại rất quan trọng đối với cô ấy. Cô ấy thường xuyên phải gọi điện cho các khách hàng của mình. Cô ấy làm việc một mình ở trong văn phòng.“*
  > *(⚠️ **Lưu ý mạo từ**: Danh từ `das Telefon` mang giống trung (`Neutrum`) và đóng vai trò chủ ngữ (`Nominativ`) của câu `Das Telefon ist wichtig für sie`; còn nếu dùng danh từ `der Computer` hoặc `der Apparat` làm chủ ngữ thì mới dùng `Der Computer ist wichtig für sie`).*

---

## PHẦN 3: KHO 100 BÀI TẬP ĐỘC NHẤT CỦA BÀI 7 (`lessons/a1/seed_a1_b7.py`) & BỘ RANDOM ĐỔI ĐỀ ĐA CHIỀU

Toàn bộ **100 câu hỏi (`100 Unique Exercises`)** dưới đây đã được thiết kế và kiểm tra chéo để đảm bảo **không có bất kỳ câu hỏi nào bị trùng lặp**, bao phủ trọn vẹn 9 dạng bài tập tương tác, đa dạng hóa chủ ngữ (`ich, du, er, sie, es, wir, ihr, sie, Sie`, tên riêng, nghề nghiệp) và tích hợp **4 Engine Sinh Đề Động (`Dynamic Multi-Variable Randomizers`)**.

### 3.1. Bảng Phân Bổ 100 Câu Hỏi Bài 7 Theo 9 Dạng Bài Tập
| STT | Mã Dạng (`type`) | Tên Dạng Bài Tập Hiển Thị | Số Lượng | Nội Dung Trọng Tâm Đa Ngữ Cảnh Trong Bài 7 |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **`trac_nghiem`** | **Trắc nghiệm (Multiple Choice)** | **18 câu** | • Hỏi đáp nghề nghiệp (`von Beruf / beruflich / arbeiten als`) và biến đổi nghề nghiệp Nam $\rightarrow$ Nữ (`Arzt -> Ärztin`, `Koch -> Köchin`, `Hausmann -> Hausfrau`)<br>• Chia động từ khuyết thiếu (`möchten, müssen, können, wollen, dürfen, sollen`) và cấu trúc khung câu (`Satzklammer`) với động từ tách<br>• Từ hạn định ở `Akkusativ` (`den, einen, keinen, meinen, ihren, euren`)<br>• Phân biệt chuyên sâu `Akkusativ` (`brauchen, untersuchen, für, Wohin?: in den, in die, ins`) vs. `Dativ` (`helfen, gefallen, bei, mit, vom, zum, Wo?: im, in der`). |
| **2** | **`dien_khuyet`** | **Điền khuyết (Fill in the Blank)** | **15 câu** | • Điền dạng chia đúng của `müssen, können, möchten, wollen, dürfen`<br>• Điền từ hạn định ở `Akkusativ` vs. `Dativ`<br>• Điền hậu tố nghề nghiệp nữ (`-in`, `-innen`) hoặc giới từ nghề nghiệp (`als`, `von`). |
| **3** | **`dich_nghia_vd`** | **Dịch từ/cụm từ: Việt $\rightarrow$ Đức** | **12 câu** | Dịch các danh từ nghề nghiệp (nam & nữ), nơi làm việc và các cụm hoạt động nghề nghiệp từ tiếng Việt sang tiếng Đức. |
| **4** | **`dich_nghia_dv`** | **Dịch từ/cụm từ: Đức $\rightarrow$ Việt** | **12 câu** | Dịch các danh từ nghề nghiệp, cụm nơi làm việc, động từ khuyết thiếu và các cụm `Akkusativ / Dativ` từ tiếng Đức sang tiếng Việt. |
| **5** | **`noi_o`** | **Nối ô từ trái qua phải (Matching Pairs)** | **10 bài** | 10 bài ghép cặp (mỗi bài 4 cặp = 40 mệnh đề độc nhất):<br>• Bài 1 & 2: Nối Nghề nghiệp $\leftrightarrow$ Công việc đặc trưng (`Lehrer`, `Verkäufer`, `Arzt`, `KFZ-Mechatroniker`, `Friseur`, `Programmierer`, `Koch`, `Florist`)<br>• Bài 3: Nối Nghề nghiệp $\leftrightarrow$ Nơi làm việc ở `Dativ` (`an einer Schule`, `im Krankenhaus`, `in einer Werkstatt`, `im Friseursalon`)<br>• Bài 4: Nối Nghề nghiệp Nam $\leftrightarrow$ Nghề nghiệp Nữ bất quy tắc/đặc biệt<br>• Bài 5: Nối Chủ ngữ $\leftrightarrow$ Dạng chia của `müssen` và `können`<br>• Bài 6: Nối Câu hỏi nghề nghiệp $\leftrightarrow$ Câu trả lời chuẩn<br>• Bài 7: Nối Động từ $\leftrightarrow$ Cách ngữ pháp yêu cầu (`Akkusativ` vs. `Dativ`)<br>• Bài 8: Nối Cụm `Wohin? (Akkusativ)` $\leftrightarrow$ Cụm `Wo? (Dativ)` tương ứng<br>• Bài 9: Nối Danh từ ở `Nominativ` $\leftrightarrow$ Cụm từ hạn định ở `Akkusativ`<br>• Bài 10: Nối Thời gian trong lịch trình của Paula & Frank $\leftrightarrow$ Hoạt động tương ứng. |
| **6** | **`dien_tao_cau`** | **Điền vào chỗ trống để tạo thành câu** | **10 câu** | Điền 2 từ còn thiếu trong câu phức hợp (kết hợp `Modalverb` ở vị trí số 2 + động từ nguyên mẫu ở cuối câu, hoặc phân biệt cặp `Akkusativ` và `Dativ` trong cùng một câu). |
| **7** | **`nghe_dien`** | **Nghe giọng đọc `de-DE` và điền từ** | **9 câu** | Nghe câu phát âm chuẩn `de-DE` và điền từ chính xác: nghe nghề nghiệp, nơi làm việc, động từ khuyết thiếu và mạo từ `Akkusativ`. |
| **8** | **`dich_cau_vd`** | **Dịch câu: Việt $\rightarrow$ Đức** | **7 câu** | Dịch câu hoàn chỉnh đa chủ ngữ từ tiếng Việt sang tiếng Đức (chấm linh hoạt đa đáp án): câu về nghề nghiệp, nơi làm việc, lịch trình với `müssen/können` và phân biệt `Akkusativ/Dativ`. |
| **9** | **`dich_cau_dv`** | **Dịch câu: Đức $\rightarrow$ Việt** | **7 câu** | Dịch câu hoàn chỉnh từ tiếng Đức sang tiếng Việt (chấm linh hoạt đa đáp án): các câu trích và mở rộng từ lịch trình của Paula Rausch, Frank Müller và Petra May. |
| | | **TỔNG CỘNG BÀI 7** | **100 CÂU** | **100% Câu hỏi Độc nhất + Đa dạng hóa Ngôi/Ngữ cảnh + QA Zero-Bug** |

---

### 3.2. Danh Sách Chi Tiết 100 Câu Hỏi Chuẩn Xác & Độc Nhất Của Bài 7 (Để Seed Vào `lessons/a1/seed_a1_b7.py`)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 18 Câu: Câu 1 $\rightarrow$ Câu 18)
1. **Câu 1 (Cách hỏi & trả lời nghề nghiệp với `als`)**: Chọn phương án đúng để hoàn thành cuộc hội thoại: *„Was machen Sie beruflich, Frau Lindner? — Ich arbeite ___ Programmiererin bei einer IT-Firma.“*
   * Đáp án: `A. wie eine` | `B. als` (Đúng) | `C. von` | `D. für`
   * Dịch nghĩa câu: *"Công việc chuyên môn của bà là gì, thưa bà Lindner? — Tôi làm nghề lập trình viên tại một công ty công nghệ thông tin."*
   * Giải thích: Khi dùng động từ `arbeiten` để giới thiệu nghề nghiệp, tiếng Đức dùng giới từ **`als`** + danh từ nghề nghiệp không có mạo từ (`Ich arbeite als Programmiererin`).
2. **Câu 2 (Cấu trúc `von Beruf` không dùng mạo từ)**: Chọn câu đúng ngữ pháp tiếng Đức khi giới thiệu nghề nghiệp của anh trai:
   * Đáp án: `A. Mein Bruder ist einen Lehrer von Beruf.` | `B. Mein Bruder ist Lehrer von Beruf.` (Đúng) | `C. Mein Bruder arbeitet von Beruf Lehrer.` | `D. Mein Bruder ist der Lehrer beruflich.`
   * Dịch nghĩa câu: *"Anh trai tôi làm nghề giáo viên."*
   * Giải thích: Với cấu trúc `[Chủ ngữ] + sein + [Nghề nghiệp] + von Beruf`, danh từ chỉ nghề nghiệp đứng một mình không dùng mạo từ `ein/einen`.
3. **Câu 3 (Biến đổi danh từ nghề nghiệp Nam $\rightarrow$ Nữ có Umlaut)**: Cặp danh từ nghề nghiệp **Nam – Nữ** nào dưới đây được viết **ĐÚNG CHÍNH TẢ 100%**?
   * Đáp án: `A. der Koch -> die Kochin / der Arzt -> die Arztin` | `B. der Koch -> die Köchin / der Arzt -> die Ärztin` (Đúng) | `C. der Koch -> die Köcherin / der Arzt -> die Ärztinn` | `D. der Hausmann -> die Hausmännin / der Krankenpfleger -> die Krankenpfleger`
   * Dịch nghĩa câu: *"Nam đầu bếp -> Nữ đầu bếp / Nam bác sĩ -> Nữ bác sĩ."*
   * Giải thích: Hai danh từ `der Koch` và `der Arzt` khi chuyển sang giống cái (`Femininum`) vừa thêm hậu tố `-in` vừa phải thêm dấu Umlaut trên nguyên âm gốc: **`die Köchin`** và **`die Ärztin`**.
4. **Câu 4 (Phối hợp Nghề nghiệp – Hoạt động – Nơi làm việc)**: Chọn phương án đúng hoàn thành câu: *„Ein KFZ-Mechatroniker ___ Autos und arbeitet ___.“*
   * Đáp án: `A. verkauft / im Schuhgeschäft` | `B. untersucht / im Krankenhaus` | `C. repariert / in einer Werkstatt` (Đúng) | `D. schneidet / im Friseursalon`
   * Dịch nghĩa câu: *"Một người thợ cơ khí ô tô sửa chữa xe hơi và làm việc ở trong một xưởng sửa chữa."*
   * Giải thích: `KFZ-Mechatroniker` là thợ cơ khí ô tô; công việc là `repariert Autos` (sửa ô tô) và nơi làm việc (`Wo? + Dativ`) là `in einer Werkstatt` (`die Werkstatt` $\rightarrow$ `in einer Werkstatt`).
5. **Câu 5 (Nơi làm việc ở Cách 3 `Dativ` khi trả lời `Wo?`)**: Chọn giới từ và mạo từ đúng: *„Wo arbeitet deine Schwester? — Sie ist Floristin und arbeitet ___ Blumengeschäft neben dem Bahnhof.“* *(Gợi ý: `das Blumengeschäft`)*
   * Đáp án: `A. ins` | `B. in der` | `C. im` (Đúng) | `D. auf dem`
   * Dịch nghĩa câu: *"Chị gái của bạn làm việc ở đâu? — Chị ấy là người bán hoa và làm việc ở trong cửa hàng hoa bên cạnh nhà ga."*
   * Giải thích: Câu hỏi `Wo?` (làm việc ở đâu) đòi hỏi Cách 3 (`Dativ`). `das Blumengeschäft` mang giống trung nên `in + dem` viết tắt là **`im Blumengeschäft`**.
6. **Câu 6 (Chia động từ khuyết thiếu `müssen` ở ngôi thứ 3 số ít)**: Chọn dạng chia đúng của động từ `müssen`: *„Paula Rausch arbeitet als Programmiererin. Jeden Morgen ___ sie schon um 6.15 Uhr aufstehen.“*
   * Đáp án: `A. müsst` | `B. musst` | `C. muss` (Đúng) | `D. müssen`
   * Dịch nghĩa câu: *"Paula Rausch làm nghề lập trình viên. Mỗi buổi sáng cô ấy đã phải thức dậy lúc 6 giờ 15 phút."*
   * Giải thích: Với động từ khuyết thiếu `müssen`, ngôi `ich` và ngôi `er/sie/es` chia giống hệt nhau là **`muss`** (đổi `ü -> u` và không có đuôi `-t`).
7. **Câu 7 (Chia động từ khuyết thiếu `können` ở ngôi `ihr - các bạn`)**: Chọn phương án đúng: *„Kinder, heute habt ihr Ferien! ___ ihr bis 9 Uhr schlafen?“*
   * Đáp án: `A. Könnt` (Đúng) | `B. Kannst` | `C. Können` | `D. Kannt`
   * Dịch nghĩa câu: *"Các con ơi, hôm nay các con được nghỉ lễ! Các con có thể ngủ đến 9 giờ không?"*
   * Giải thích: Chủ ngữ là `ihr` (các con/các bạn), động từ `können` giữ nguyên nguyên âm `ö` và chia đuôi `-t` thành **`könnt`**.
8. **Câu 8 (Khung câu `Satzklammer` kết hợp `Modalverb` và Động từ tách)**: Chọn câu đúng trật tự từ ngữ pháp tiếng Đức:
   * Đáp án:
     * `A. Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholt.`
     * `B. Um 16.30 Uhr holt Paula ihre Tochter vom Kindergarten müssen ab.`
     * `C. Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.` (Đúng)
     * `D. Um 16.30 Uhr muss abholen Paula ihre Tochter vom Kindergarten.`
   * Dịch nghĩa câu: *"Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo."*
   * Giải thích: Khi có động từ khuyết thiếu `muss` đứng ở vị trí số 2, động từ tách `abholen` không tách nữa mà giữ nguyên dạng nguyên mẫu (`Infinitiv`) đứng ở cuối câu.
9. **Câu 9 (Từ hạn định ở `Akkusativ` với động từ `brauchen`)**: Chọn cặp từ đúng điền vào câu: *„Bei ihrer Arbeit braucht Petra ___ Computer und ___ großen Schreibtisch.“* *(Gợi ý: `der Computer`, `der Schreibtisch`)*
   * Đáp án: `A. ein / ein` | `B. einen / einen` (Đúng) | `C. einem / einem` | `D. den / dem`
   * Dịch nghĩa câu: *"Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."*
   * Giải thích: Động từ `brauchen` (cần cái gì) luôn đi với tân ngữ trực tiếp ở **Cách 4 (`Akkusativ`)**. Cả `der Computer` và `der Schreibtisch` đều mang giống đực (`Maskulinum`), nên mạo từ `ein` đổi thành **`einen`**.
10. **Câu 10 (Phủ định `kein` ở `Akkusativ` với danh từ giống đực)**: Chọn phương án đúng: *„Herr Weber arbeitet heute von zu Hause. Er braucht ___ Anzug, sondern nur ___ Laptop.“* *(Gợi ý: `der Anzug` - bộ vest, `der Laptop`)*
    * Đáp án: `A. kein / ein` | `B. keinen / einen` (Đúng) | `C. keinem / einem` | `D. keine / eine`
    * Dịch nghĩa câu: *"Hôm nay ông Weber làm việc tại nhà. Ông ấy không cần bộ vest nào cả mà chỉ cần một chiếc máy tính xách tay."*
    * Giải thích: Cả `der Anzug` và `der Laptop` đều là danh từ giống đực làm tân ngữ trực tiếp (`Akkusativ`) sau động từ `braucht`, nên chia là **`keinen Anzug`** và **`einen Laptop`**.
11. **Câu 11 (Mạo từ sở hữu ở `Akkusativ` số nhiều & giống cái)**: Chọn phương án đúng: *„Die Sekretärin muss heute Vormittag ___ Chef und ___ Kunden anrufen.“* *(Gợi ý: `der Chef` - ông sếp, `die Kunden` - những khách hàng)*
    * Đáp án: `A. ihren / ihre` (Đúng) | `B. ihrem / ihren` | `C. ihre / ihren` | `D. ihr / ihre`
    * Dịch nghĩa câu: *"Nữ thư ký sáng nay phải gọi điện cho ông sếp của cô ấy và các khách hàng của cô ấy."*
    * Giải thích: Động từ `anrufen` (gọi điện cho ai) đi với **Cách 4 (`Akkusativ`)**. Với `der Chef` (giống đực), mạo từ sở hữu của cô ấy (`ihr-`) đổi thành **`ihren Chef`**; với `die Kunden` (số nhiều) ở `Akkusativ` thì giữ nguyên đuôi `-e` là **`ihre Kunden`**.
12. **Câu 12 (Phân biệt `Akkusativ` và `Dativ` theo Động từ: `untersuchen` vs. `helfen`)**: Chọn cặp mạo từ đúng điền vào 2 câu sau: *„1. Die Ärztin untersucht ___ kranken Mann (`der Mann`). — 2. Die Krankenschwester hilft ___ kranken Mann (`der Mann`).“*
    * Đáp án: `A. den / den` | `B. dem / den` | `C. den / dem` (Đúng) | `D. der / dem`
    * Dịch nghĩa câu: *"1. Nữ bác sĩ khám cho người đàn ông bị ốm. — 2. Nữ y tá giúp đỡ người đàn ông bị ốm."*
    * Giải thích: Động từ `untersuchen` (khám bệnh cho ai) đòi hỏi **Cách 4 (`Akkusativ`)** $\rightarrow$ **`den kranken Mann`**. Ngược lại, động từ `helfen` (giúp đỡ ai) bắt buộc đi với **Cách 3 (`Dativ`)** $\rightarrow$ **`dem kranken Mann`**.
13. **Câu 13 (Phân biệt `Akkusativ` và `Dativ` theo Giới từ cố định: `bei` vs. `für`)**: Chọn phương án đúng hoàn thành câu: *„___ seiner Arbeit im Krankenhaus hat der Arzt wenig Pause, aber die Arbeit ist sehr wichtig ___ seine Patienten.“*
    * Đáp án: `A. Für / bei` | `B. Bei / für` (Đúng) | `C. Mit / von` | `D. Zu / ohne`
    * Dịch nghĩa câu: *"Trong công việc của mình ở bệnh viện, vị bác sĩ có ít thời gian nghỉ giải lao, nhưng công việc đó rất quan trọng đối với các bệnh nhân của ông ấy."*
    * Giải thích: Cụm *"Trong công việc của mình"* dùng **`Bei seiner Arbeit`** (`bei + Dativ`), còn *"quan trọng đối với ai"* dùng **`wichtig für + Akkusativ`** (`für seine Patienten`).
14. **Câu 14 (Phân biệt `Wohin? + Akkusativ` và `Wo? + Dativ` với `der Kindergarten`)**: Chọn phương án đúng điền vào 2 chỗ trống: *„Um 8.30 Uhr bringt Frank seine Tochter ___ Kindergarten (`Wohin?`), und um 16.30 Uhr holt Paula die Tochter ___ Kindergarten (`Woher?`) ab.“*
    * Đáp án: `A. im / in den` | `B. in den / vom` (Đúng) | `C. zum / im` | `D. in dem / von der`
    * Dịch nghĩa câu: *"Lúc 8 giờ 30 phút Frank đưa con gái vào trường mẫu giáo, và lúc 16 giờ 30 phút Paula đón con gái từ trường mẫu giáo về."*
    * Giải thích: Đưa vào trường mẫu giáo (`bringen` $\rightarrow$ `Wohin? + Akkusativ`) với danh từ giống đực `der Kindergarten` là **`in den Kindergarten`**. Đón từ trường mẫu giáo về (`abholen` $\rightarrow$ `von + Dativ`) là **`vom Kindergarten`**.
15. **Câu 15 (Phân biệt `Wohin? + Akkusativ` và `Wo? + Dativ` với `die Werkstatt`)**: Chọn cặp từ đúng: *„Herr Müller bringt sein Auto ___ Werkstatt (`Wohin?`). Dort repariert der Mechatroniker das Auto ___ Werkstatt (`Wo?`).“*
    * Đáp án: `A. in die / in der` (Đúng) | `B. in der / in die` | `C. zur / in die` | `D. in eine / in eine`
    * Dịch nghĩa câu: *"Ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa. Ở đó người thợ cơ khí sửa chiếc ô tô ở trong xưởng."*
    * Giải thích: Danh từ `die Werkstatt` mang giống cái (`Femininum`). Khi di chuyển vào xưởng (`Wohin? + Akkusativ`) dùng **`in die Werkstatt`**; khi làm việc ở bên trong xưởng (`Wo? + Dativ`) dùng **`in der Werkstatt`**.
16. **Câu 16 (Phân biệt `ins Bett` [`Akkusativ`] và `im Bett` [`Dativ`])**: Chọn phương án đúng: *„Um 19 Uhr bringt die Mutter ihren Sohn ___ Bett. Um 20 Uhr liegt er schon ___ Bett und schläft.“*
    * Đáp án: `A. im / ins` | `B. ins / im` (Đúng) | `C. in dem / in das` | `D. ans / am`
    * Dịch nghĩa câu: *"Lúc 19 giờ người mẹ đưa con trai lên giường ngủ. Lúc 20 giờ cậu bé đã nằm trên giường và ngủ."*
    * Giải thích: Đưa lên giường (`bringen` — di chuyển `Wohin?`) dùng `in + das` = **`ins Bett`** (`Akkusativ`). Nằm ngủ trên giường (`liegen/schlafen` — vị trí tĩnh `Wo?`) dùng `in + dem` = **`im Bett`** (`Dativ`).
17. **Câu 17 (Câu có cả 2 tân ngữ `Dativ` [Người nhận] + `Akkusativ` [Vật được trao])**: Chọn phương án đúng ngữ pháp: *„Der Chef kauft ___ Sekretärin (`die Sekretärin`) ___ neuen Computer (`der Computer`).“*
    * Đáp án: `A. die / einen` | `B. der / einen` (Đúng) | `C. der / einem` | `D. einer / den`
    * Dịch nghĩa câu: *"Người sếp mua cho nữ thư ký một chiếc máy tính mới."*
    * Giải thích: Trong câu có 2 tân ngữ: Người nhận lợi ích (`Wem?` *cho nữ thư ký*) chia ở **Cách 3 (`Dativ`)** $\rightarrow$ **`der Sekretärin`**; Vật được mua (`Was?` *một chiếc máy tính mới*) chia ở **Cách 4 (`Akkusativ`)** $\rightarrow$ **`einen neuen Computer`**.
18. **Câu 18 (Mạo từ sở hữu ngôi `ihr - các bạn` ở `Akkusativ` giống đực)**: Chọn dạng mạo từ sở hữu đúng: *„Liebe Schüler, ihr müsst morgen ___ Lehrer fragen und ___ Hefte mitbringen!“* *(Gợi ý: `der Lehrer` & `die Hefte`)*
    * Đáp án: `A. euer / eure` | `B. euren / eure` (Đúng) | `C. eurem / euren` | `D. eurer / eure`
    * Dịch nghĩa câu: *"Các em học sinh thân mến, ngày mai các em phải hỏi thầy giáo của các em và mang theo vở của các em nhé!"*
    * Giải thích: Động từ `fragen` (hỏi ai) và `mitbringen` (mang theo cái gì) đều đi với **Cách 4 (`Akkusativ`)**. Chủ ngữ là `ihr` (các em) $\rightarrow$ gốc `euer`. Trước `der Lehrer` (giống đực `Akkusativ`) đổi thành **`euren Lehrer`**; trước `die Hefte` (số nhiều `Akkusativ`) đổi thành **`eure Hefte`**.

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 15 Câu: Câu 19 $\rightarrow$ Câu 33)
19. **Câu 19**: Điền giới từ chỉ nghề nghiệp thích hợp vào chỗ trống: *„Mein Onkel arbeitet seit fünf Jahren ___ Taxifahrer in Hamburg.“*
    * Đáp án chấp nhận: `["als"]`
    * Dịch nghĩa câu: *"Chú của tôi làm nghề tài xế taxi ở Hamburg từ 5 năm nay."*
    * Giải thích: Cụm `arbeiten als + [Nghề nghiệp]` dùng để nói làm nghề gì.
20. **Câu 20**: Điền danh từ nghề nghiệp dạng **Nữ (`Femininum`)** tương ứng với `der Arzt` vào chỗ trống: *„Meine Tante arbeitet im Krankenhaus. Sie ist ___ von Beruf.“*
    * Đáp án chấp nhận: `["Ärztin", "Aerztin"]`
    * Dịch nghĩa câu: *"Dì của tôi làm việc ở trong bệnh viện. Dì ấy làm nghề nữ bác sĩ."*
    * Giải thích: `der Arzt` khi chuyển sang danh từ nghề nghiệp nữ phải thêm dấu Umlaut và đuôi `-in` thành **`Ärztin`**.
21. **Câu 21**: Điền danh từ nghề nghiệp dạng **Nữ (`Femininum`)** tương ứng với `der Koch` vào chỗ trống: *„Frau Bui kocht sehr gut in einem großen Restaurant. Sie arbeitet als ___.“*
    * Đáp án chấp nhận: `["Köchin", "Koechin"]`
    * Dịch nghĩa câu: *"Bà Bùi nấu ăn rất ngon trong một nhà hàng lớn. Bà ấy làm nghề nữ đầu bếp."*
    * Giải thích: `der Koch` chuyển sang giống cái thêm Umlaut `o -> ö` và `-in` thành **`Köchin`**.
22. **Câu 22**: Điền dạng chia đúng của động từ khuyết thiếu `müssen` vào chỗ trống: *„Ich habe morgen eine Prüfung, deshalb ___ ich heute Abend viel lernen.“*
    * Đáp án chấp nhận: `["muss"]`
    * Dịch nghĩa câu: *"Ngày mai tôi có một kỳ thi, vì vậy tối nay tôi phải học bài nhiều."*
    * Giải thích: Ngôi thứ nhất số ít (`ich`) của động từ `müssen` là **`muss`**.
23. **Câu 23**: Điền dạng chia đúng của động từ khuyết thiếu `müssen` vào chỗ trống: *„Wann ___ du morgen früh zur Arbeit fahren, Lukas?“*
    * Đáp án chấp nhận: `["musst"]`
    * Dịch nghĩa câu: *"Sáng sớm mai bạn phải đi làm lúc mấy giờ thế, Lukas?"*
    * Giải thích: Ngôi thứ hai số ít (`du`) của động từ `müssen` là **`musst`**.
24. **Câu 24**: Điền dạng chia đúng của động từ khuyết thiếu `können` vào chỗ trống: *„Herr Müller hat heute Ferien. Er ___ bis 8 Uhr schlafen.“*
    * Đáp án chấp nhận: `["kann"]`
    * Dịch nghĩa câu: *"Ông Müller hôm nay có kỳ nghỉ. Ông ấy có thể ngủ đến 8 giờ."*
    * Giải thích: Ngôi thứ ba số ít (`er`) của động từ `können` là **`kann`** (không có đuôi `-t`).
25. **Câu 25**: Điền dạng chia đúng của động từ khuyết thiếu `möchten` vào chỗ trống: *„Anna ist Schülerin, aber später ___ sie Medizin an der Universität studieren.“*
    * Đáp án chấp nhận: `["möchte", "moechte"]`
    * Dịch nghĩa câu: *"Anna là học sinh, nhưng sau này cô ấy muốn học ngành Y ở trường đại học."*
    * Giải thích: Ngôi thứ ba số ít (`sie` - cô ấy) của `möchten` là **`möchte`**.
26. **Câu 26**: Điền dạng nguyên mẫu của động từ tách `aufstehen` vào cuối câu có `Modalverb`: *„Am Sonntag müssen wir nicht früh ___.“*
    * Đáp án chấp nhận: `["aufstehen"]`
    * Dịch nghĩa câu: *"Vào Chủ nhật chúng tôi không phải thức dậy sớm."*
    * Giải thích: Khi câu đã có động từ khuyết thiếu `müssen` ở vị trí số 2, động từ tách `aufstehen` giữ nguyên dạng nguyên mẫu viết liền ở cuối câu.
27. **Câu 27**: Điền mạo từ không xác định đúng ở Cách 4 (`Akkusativ`) vào chỗ trống: *„Für seine Arbeit im Büro braucht mein Bruder ___ schnellen Laptop.“* *(Gợi ý: `der Laptop`)*
    * Đáp án chấp nhận: `["einen"]`
    * Dịch nghĩa câu: *"Cho công việc của mình ở văn phòng, anh trai tôi cần một chiếc máy tính xách tay nhanh."*
    * Giải thích: Động từ `brauchen` đòi hỏi Cách 4 (`Akkusativ`). `der Laptop` mang giống đực nên `ein` đổi thành **`einen`**.
28. **Câu 28**: Điền mạo từ phủ định `kein` đúng ở Cách 4 (`Akkusativ`) vào chỗ trống: *„Ich trinke meinen Tee bitte ohne Zucker, ich brauche ___ Löffel.“* *(Gợi ý: `der Löffel` - cái thìa)*
    * Đáp án chấp nhận: `["keinen"]`
    * Dịch nghĩa câu: *"Tôi uống trà không đường, tôi không cần cái thìa nào cả."*
    * Giải thích: `der Löffel` mang giống đực, làm tân ngữ trực tiếp (`Akkusativ`) sau `brauche`, nên `kein` đổi thành **`keinen`**.
29. **Câu 29**: Điền mạo từ sở hữu của ngôi `er` (`sein-`) đúng ở Cách 4 (`Akkusativ`) vào chỗ trống: *„Der Programmierer ruft ___ Chef im Büro an.“* *(Gợi ý: `der Chef`)*
    * Đáp án chấp nhận: `["seinen"]`
    * Dịch nghĩa câu: *"Lập trình viên gọi điện cho ông sếp của anh ấy ở văn phòng."*
    * Giải thích: Động từ `anrufen` đi với Cách 4 (`Akkusativ`). `der Chef` mang giống đực nên gốc sở hữu `sein-` của `er` đổi thành **`seinen`**.
30. **Câu 30**: Điền mạo từ xác định đúng (phân biệt `Wohin? Akkusativ`) vào chỗ trống: *„Jeden Morgen um 8 Uhr bringt Frau Rausch ihren Sohn in ___ Kindergarten.“* *(Gợi ý: `der Kindergarten`)*
    * Đáp án chấp nhận: `["den"]`
    * Dịch nghĩa câu: *"Mỗi buổi sáng lúc 8 giờ bà Rausch đưa con trai mình vào trường mẫu giáo."*
    * Giải thích: Hành động đưa con đến trường mẫu giáo (`bringen` $\rightarrow$ câu hỏi `Wohin?`) dùng **Cách 4 (`Akkusativ`)**: `der Kindergarten` $\rightarrow$ **`in den Kindergarten`**.
31. **Câu 31**: Điền giới từ thu gọn (`in + das`) chỉ hướng di chuyển `Wohin?` (`Akkusativ`) vào chỗ trống: *„Es ist schon 22 Uhr. Die Kinder müssen jetzt ___ Bett gehen.“* *(Gợi ý: `das Bett`)*
    * Đáp án chấp nhận: `["ins"]`
    * Dịch nghĩa câu: *"Đã 22 giờ rồi. Bọn trẻ bây giờ phải đi lên giường ngủ."*
    * Giải thích: Đi lên giường ngủ (`Wohin? + Akkusativ`) với danh từ giống trung `das Bett` dùng `in + das` gộp thành **`ins Bett`**.
32. **Câu 32**: Điền mạo từ xác định đúng ở Cách 3 (`Dativ`) sau động từ `helfen`: *„Die Sekretärin hilft ___ neuen Praktikanten bei der Arbeit.“* *(Gợi ý: `der Praktikant`)*
    * Đáp án chấp nhận: `["dem"]`
    * Dịch nghĩa câu: *"Nữ thư ký giúp đỡ nam thực tập sinh mới trong công việc."*
    * Giải thích: Động từ `helfen` luôn đi với Cách 3 (`Dativ`), nên `der Praktikant` chuyển thành **`dem neuen Praktikanten`**.
33. **Câu 33**: Điền dạng chia đúng của động từ `unterrichten` theo chủ ngữ vào chỗ trống: *„Herr Müller ist Lehrer von Beruf und ___ Mathematik an einer Schule.“*
    * Đáp án chấp nhận: `["unterrichtet"]`
    * Dịch nghĩa câu: *"Ông Müller làm nghề giáo viên và giảng dạy môn Toán tại một trường học."*
    * Giải thích: Động từ `unterrichten` có gốc kết thúc bằng `-t` (`unterricht-`), nên ở ngôi thứ 3 số ít (`er`) phải thêm `-e-` trước `-t` thành **`unterrichtet`**.

---

#### NHÓM 3: DỊCH NGHĨA TỪ / CỤM TỪ VIỆT $\rightarrow$ ĐỨC (`dich_nghia_vd` — 12 Câu: Câu 34 $\rightarrow$ Câu 45)
34. **Câu 34**: Dịch sang tiếng Đức (kèm mạo từ): ***"nữ lập trình viên"***
    * Đáp án chấp nhận: `["die Programmiererin", "Programmiererin"]`
    * Giải thích: Nam lập trình viên là `der Programmierer` $\rightarrow$ Nữ lập trình viên thêm `-in` là **`die Programmiererin`**.
35. **Câu 35**: Dịch sang tiếng Đức (kèm mạo từ): ***"thợ cơ khí ô tô (nam)"***
    * Đáp án chấp nhận: `["der KFZ-Mechatroniker", "der Mechatroniker", "KFZ-Mechatroniker", "Mechatroniker"]`
    * Giải thích: Thợ cơ khí / kỹ thuật viên sửa chữa ô tô là **`der KFZ-Mechatroniker`** (hoặc **`der Mechatroniker`**).
36. **Câu 36**: Dịch sang tiếng Đức (kèm mạo từ): ***"nữ y tá / điều dưỡng"***
    * Đáp án chấp nhận: `["die Krankenpflegerin", "die Krankenschwester", "Krankenpflegerin", "Krankenschwester"]`
    * Giải thích: Nữ y tá / điều dưỡng trong tiếng Đức là **`die Krankenpflegerin`** hoặc **`die Krankenschwester`**.
37. **Câu 37**: Dịch sang tiếng Đức (kèm mạo từ): ***"người bán hoa (nữ)"***
    * Đáp án chấp nhận: `["die Floristin", "Floristin"]`
    * Giải thích: Nam bán hoa là `der Florist` $\rightarrow$ Nữ bán hoa là **`die Floristin`**.
38. **Câu 38**: Dịch sang tiếng Đức (kèm mạo từ): ***"tiệm làm tóc / salon tóc"***
    * Đáp án chấp nhận: `["der Friseursalon", "Friseursalon"]`
    * Giải thích: Tiệm làm tóc là danh từ giống đực **`der Friseursalon`** (số nhiều: `die Friseursalons`).
39. **Câu 39**: Dịch sang tiếng Đức (kèm mạo từ): ***"xưởng sửa chữa"***
    * Đáp án chấp nhận: `["die Werkstatt", "Werkstatt"]`
    * Giải thích: Xưởng sửa chữa là danh từ giống cái **`die Werkstatt`** (số nhiều: `die Werkstätten`).
40. **Câu 40**: Dịch sang tiếng Đức (kèm mạo từ): ***"công trường xây dựng"***
    * Đáp án chấp nhận: `["die Baustelle", "Baustelle"]`
    * Giải thích: Công trường xây dựng là danh từ giống cái **`die Baustelle`** (số nhiều: `die Baustellen`).
41. **Câu 41**: Dịch sang tiếng Đức (kèm mạo từ): ***"cửa hàng hoa"***
    * Đáp án chấp nhận: `["das Blumengeschäft", "Blumengeschäft", "das Blumengeschaeft"]`
    * Giải thích: Cửa hàng hoa là danh từ ghép giống trung **`das Blumengeschäft`** (số nhiều: `die Blumengeschäfte`).
42. **Câu 42**: Dịch sang tiếng Đức (kèm mạo từ): ***"trung tâm ngoại ngữ"***
    * Đáp án chấp nhận: `["das Sprachzentrum", "Sprachzentrum"]`
    * Giải thích: Trung tâm ngoại ngữ là danh từ giống trung **`das Sprachzentrum`** (số nhiều: `die Sprachzentren`).
43. **Câu 43**: Dịch cụm hoạt động nghề nghiệp sau sang tiếng Đức: ***"khám cho các bệnh nhân"***
    * Đáp án chấp nhận: `["Patienten untersuchen", "die Patienten untersuchen", "untersucht Patienten"]`
    * Giải thích: Động từ *"khám bệnh"* là `untersuchen`, bệnh nhân số nhiều là `die Patienten` $\rightarrow$ **`Patienten untersuchen`**.
44. **Câu 44**: Dịch cụm hoạt động nghề nghiệp sau sang tiếng Đức: ***"cắt tóc"***
    * Đáp án chấp nhận: `["Haare schneiden", "die Haare schneiden", "schneidet Haare"]`
    * Giải thích: Danh từ *"tóc"* (số nhiều) là `die Haare`, động từ *"cắt"* là `schneiden` $\rightarrow$ **`Haare schneiden`**.
45. **Câu 45**: Dịch câu hỏi nghề nghiệp sau sang tiếng Đức (dạng trang trọng `Sie`): ***"Ngài làm nghề gì?"***
    * Đáp án chấp nhận: `["Was sind Sie von Beruf?", "Was machen Sie beruflich?", "Was ist Ihr Beruf?"]`
    * Giải thích: Cả 3 mẫu câu `Was sind Sie von Beruf?`, `Was machen Sie beruflich?` và `Was ist Ihr Beruf?` đều chuẩn xác 100%.

---

#### NHÓM 4: DỊCH NGHĨA TỪ / CỤM TỪ ĐỨC $\rightarrow$ VIỆT (`dich_nghia_dv` — 12 Câu: Câu 46 $\rightarrow$ Câu 57)
46. **Câu 46**: Dịch sang tiếng Việt: ***„der Taxifahrer / die Taxifahrerin“***
    * Đáp án chấp nhận: `["tài xế taxi", "người lái xe taxi", "nam tài xế taxi và nữ tài xế taxi", "lái xe taxi"]`
    * Giải thích: `der Taxifahrer` (nam) và `die Taxifahrerin` (nữ) có nghĩa là tài xế taxi.
47. **Câu 47**: Dịch sang tiếng Việt: ***„der Hausmann / die Hausfrau“***
    * Đáp án chấp nhận: `["người nội trợ", "nam nội trợ và nữ nội trợ", "đàn ông nội trợ và phụ nữ nội trợ", "nội trợ"]`
    * Giải thích: `der Hausmann` (nam nội trợ) và `die Hausfrau` (nữ nội trợ).
48. **Câu 48**: Dịch sang tiếng Việt: ***„der Kellner / die Kellnerin“***
    * Đáp án chấp nhận: `["nhân viên phục vụ bàn", "bồi bàn", "người phục vụ nhà hàng", "nam bồi bàn và nữ bồi bàn"]`
    * Giải thích: `der Kellner / die Kellnerin` là nhân viên phục vụ bàn (bồi bàn) trong nhà hàng hoặc quán cà phê.
49. **Câu 49**: Dịch sang tiếng Việt: ***„der Sekretär / die Sekretärin“***
    * Đáp án chấp nhận: `["thư ký", "nam thư ký và nữ thư ký", "người thư ký"]`
    * Giải thích: `der Sekretär / die Sekretärin` có nghĩa là thư ký văn phòng.
50. **Câu 50**: Dịch sang tiếng Việt: ***„Schüler an einer Schule unterrichten“***
    * Đáp án chấp nhận: `["dạy học sinh ở một trường học", "giảng dạy học sinh tại một ngôi trường", "dạy học sinh tại một trường học"]`
    * Giải thích: `unterrichten` = giảng dạy; `Schüler` = học sinh; `an einer Schule` = tại một ngôi trường.
51. **Câu 51**: Dịch sang tiếng Việt: ***„Computerprogramme schreiben“***
    * Đáp án chấp nhận: `["viết chương trình máy tính", "viết các chương trình máy tính", "lập trình phần mềm máy tính"]`
    * Giải thích: `die Computerprogramme` = các chương trình máy tính; `schreiben` = viết.
52. **Câu 52**: Dịch sang tiếng Việt: ***„die Tochter vom Kindergarten abholen“***
    * Đáp án chấp nhận: `["đón con gái từ trường mẫu giáo", "đón con gái từ nhà trẻ về", "đón cô con gái ở trường mầm non"]`
    * Giải thích: `abholen` = đón; `vom Kindergarten` = từ trường mẫu giáo / nhà trẻ.
53. **Câu 53**: Dịch sang tiếng Việt: ***„das Auto in die Werkstatt bringen“***
    * Đáp án chấp nhận: `["mang ô tô vào xưởng sửa chữa", "đưa xe hơi đến xưởng sửa chữa", "đem ô tô vào xưởng"]`
    * Giải thích: `in die Werkstatt bringen` (`Wohin? + Akkusativ`) = mang/đưa vào xưởng sửa chữa.
54. **Câu 54**: Dịch sang tiếng Việt: ***„zum Fußballtraining gehen“***
    * Đáp án chấp nhận: `["đi đến buổi tập bóng đá", "đi tập đá bóng", "đi tới buổi huấn luyện bóng đá"]`
    * Giải thích: `das Fußballtraining` = buổi tập luyện bóng đá; `zum Fußballtraining gehen` = đi tập bóng đá.
55. **Câu 55**: Dịch sang tiếng Việt: ***„Kunden im Büro anrufen“***
    * Đáp án chấp nhận: `["gọi điện cho khách hàng ở trong văn phòng", "gọi điện thoại cho khách hàng tại văn phòng", "gọi cho khách hàng ở văn phòng"]`
    * Giải thích: `die Kunden` = khách hàng; `anrufen` = gọi điện thoại; `im Büro` = ở trong văn phòng.
56. **Câu 56**: Dịch sang tiếng Việt: ***„müssen — können — möchten“***
    * Đáp án chấp nhận: `["phải - có thể - muốn", "phải, có thể, muốn", "bắt buộc phải - có thể - muốn"]`
    * Giải thích: Ba động từ khuyết thiếu trọng tâm: `müssen` (phải), `können` (có thể), `möchten` (muốn).
57. **Câu 57**: Dịch sang tiếng Việt: ***„im Schuhgeschäft Schuhe verkaufen“***
    * Đáp án chấp nhận: `["bán giày ở trong cửa hàng giày", "bán giày dép tại tiệm giày", "bán giày trong tiệm giày"]`
    * Giải thích: `im Schuhgeschäft` = ở trong cửa hàng giày dép; `Schuhe verkaufen` = bán giày.

---

#### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 10 Bài: Câu 58 $\rightarrow$ Câu 67, mỗi bài 4 cặp độc nhất)
58. **Câu 58 (Bài nối ô 1 — Nối Nghề nghiệp với Hoạt động đặc trưng - Phần 1)**:
    * `der Lehrer / die Lehrerin` $\longleftrightarrow$ `unterrichtet Schüler (giảng dạy học sinh)`
    * `der Arzt / die Ärztin` $\longleftrightarrow$ `untersucht Patienten (khám cho bệnh nhân)`
    * `der KFZ-Mechatroniker` $\longleftrightarrow$ `repariert Autos (sửa chữa xe ô tô)`
    * `der Programmierer` $\longleftrightarrow$ `schreibt Computerprogramme (viết chương trình máy tính)`
59. **Câu 59 (Bài nối ô 2 — Nối Nghề nghiệp với Hoạt động đặc trưng - Phần 2)**:
    * `der Friseur / die Friseurin` $\longleftrightarrow$ `schneidet Haare (cắt tóc)`
    * `der Verkäufer / die Verkäuferin` $\longleftrightarrow$ `verkauft Schuhe (bán giày dép)`
    * `der Florist / die Floristin` $\longleftrightarrow$ `verkauft Blumen (bán hoa tươi)`
    * `der Koch / die Köchin` $\longleftrightarrow$ `kocht leckere Speisen (nấu những món ăn ngon)`
60. **Câu 60 (Bài nối ô 3 — Nối Nghề nghiệp với Nơi làm việc ở `Dativ`)**:
    * `der Lehrer` $\longleftrightarrow$ `arbeitet an einer Schule / im Sprachzentrum`
    * `die Ärztin und der Krankenpfleger` $\longleftrightarrow$ `arbeiten im Krankenhaus`
    * `der KFZ-Mechatroniker` $\longleftrightarrow$ `arbeitet in einer Werkstatt`
    * `die Friseurin` $\longleftrightarrow$ `arbeitet im Friseursalon`
61. **Câu 61 (Bài nối ô 4 — Nối Danh từ Nghề nghiệp Nam với Dạng Nữ đặc biệt)**:
    * `der Arzt (nam bác sĩ)` $\longleftrightarrow$ `die Ärztin (thêm Umlaut ä + -in)`
    * `der Koch (nam đầu bếp)` $\longleftrightarrow$ `die Köchin (thêm Umlaut ö + -in)`
    * `der Hausmann (nam nội trợ)` $\longleftrightarrow$ `die Hausfrau (đổi gốc sang -frau)`
    * `der Krankenpfleger (nam điều dưỡng)` $\longleftrightarrow$ `die Krankenschwester / die Krankenpflegerin`
62. **Câu 62 (Bài nối ô 5 — Nối Chủ ngữ với Dạng chia của Động từ khuyết thiếu)**:
    * `ich / er / sie / es (với müssen)` $\longleftrightarrow$ `muss (đổi ü -> u, không có đuôi)`
    * `ich / er / sie / es (với können)` $\longleftrightarrow$ `kann (đổi ö -> a, không có đuôi)`
    * `du (với müssen & können)` $\longleftrightarrow$ `musst / kannst (thêm đuôi -st)`
    * `ihr (với müssen & können)` $\longleftrightarrow$ `müsst / könnt (giữ Umlaut, thêm đuôi -t)`
63. **Câu 63 (Bài nối ô 6 — Nối Câu hỏi Nghề nghiệp & Nơi làm việc với Câu trả lời chuẩn)**:
    * `Was sind Sie von Beruf?` $\longleftrightarrow$ `Ich bin Sekretärin von Beruf.`
    * `Als was arbeitet dein Bruder?` $\longleftrightarrow$ `Er arbeitet als Programmierer.`
    * `Wo arbeitet Frau Wagner?` $\longleftrightarrow$ `Sie arbeitet im Blumengeschäft.`
    * `Was muss Petra im Büro machen?` $\longleftrightarrow$ `Sie muss ihre Kunden anrufen.`
64. **Câu 64 (Bài nối ô 7 — Phân biệt Động từ đi với `Akkusativ` vs. Động từ đi với `Dativ`)**:
    * `brauchen (cần) & suchen (tìm)` $\longleftrightarrow$ `luôn đi với Cách 4 (Akkusativ: einen Computer)`
    * `anrufen (gọi điện) & untersuchen (khám)` $\longleftrightarrow$ `luôn đi với Cách 4 (Akkusativ: den Patienten)`
    * `helfen (giúp đỡ) & danken (cảm ơn)` $\longleftrightarrow$ `luôn đi với Cách 3 (Dativ: dem Arzt)`
    * `gefallen (làm ai thích) & gehören (thuộc về)` $\longleftrightarrow$ `luôn đi với Cách 3 (Dativ: meiner Mutter)`
65. **Câu 65 (Bài nối ô 8 — Đối chiếu trực tiếp `Wohin? (Akkusativ)` và `Wo? (Dativ)`)**:
    * `in den Kindergarten bringen (Wohin?)` $\longleftrightarrow$ `im Kindergarten spielen (Wo?)`
    * `in die Werkstatt fahren (Wohin?)` $\longleftrightarrow$ `in der Werkstatt reparieren (Wo?)`
    * `ins Bett gehen (Wohin?)` $\longleftrightarrow$ `im Bett schlafen (Wo?)`
    * `ins Büro kommen (Wohin?)` $\longleftrightarrow$ `im Büro arbeiten (Wo?)`
66. **Câu 66 (Bài nối ô 9 — Biến đổi Từ hạn định từ `Nominativ` sang `Akkusativ`)**:
    * `der Tisch / ein Computer (Maskulinum)` $\longleftrightarrow$ `den Tisch / einen Computer (đổi sang đuôi -en)`
    * `die Tasche / meine Tochter (Femininum)` $\longleftrightarrow$ `die Tasche / meine Tochter (giữ nguyên)`
    * `das Buch / kein Auto (Neutrum)` $\longleftrightarrow$ `das Buch / kein Auto (giữ nguyên)`
    * `die Bücher / ihre Kunden (Plural)` $\longleftrightarrow$ `die Bücher / ihre Kunden (giữ nguyên, không thêm -n)`
67. **Câu 67 (Bài nối ô 10 — Lịch trình trong ngày của Paula Rausch & Frank Müller)**:
    * `Paula: um 6.15 Uhr` $\longleftrightarrow$ `muss sie aufstehen`
    * `Paula: um 16.30 Uhr` $\longleftrightarrow$ `muss sie ihre Tochter vom Kindergarten abholen`
    * `Frank: bis 7.00 Uhr` $\longleftrightarrow$ `kann er schlafen, weil er Ferien hat`
    * `Frank: um 12.30 Uhr` $\longleftrightarrow$ `bringt er das Auto in die Werkstatt`

---

#### NHÓM 6: ĐIỀN VÀO CHỖ TRỐNG ĐỂ TẠO THÀNH CÂU (`dien_tao_cau` — 10 Câu: Câu 68 $\rightarrow$ Câu 77)
68. **Câu 68**: Điền 2 từ còn thiếu để hoàn thành câu: *„Lúc 6 giờ 15 phút Paula phải thức dậy.“*
    * Khung câu hiển thị: `Um 6.15 Uhr [1] Paula [2].` (Gợi ý: `müssen`, `aufstehen`)
    * Đáp án từng ô: Ô 1 = `["muss"]`, Ô 2 = `["aufstehen"]`.
    * Giải thích: Động từ khuyết thiếu `müssen` chia theo ngôi thứ 3 số ít (`Paula`) là `muss` đứng ở vị trí số 2; động từ tách `aufstehen` giữ nguyên mẫu viết liền ở cuối câu.
69. **Câu 69**: Điền 2 từ còn thiếu để hoàn thành câu: *„Từ 20 giờ đến 22 giờ cô ấy có thể xem tivi.“*
    * Khung câu hiển thị: `Von 20 bis 22 Uhr [1] sie [2].` (Gợi ý: `können`, `fernsehen`)
    * Đáp án từng ô: Ô 1 = `["kann"]`, Ô 2 = `["fernsehen"]`.
    * Giải thích: `können` chia cho ngôi `sie` (cô ấy) là `kann` ở vị trí số 2; động từ tách `fernsehen` giữ nguyên mẫu ở cuối câu.
70. **Câu 70**: Điền 2 từ còn thiếu để hoàn thành câu: *„Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo.“*
    * Khung câu hiển thị: `Um 16.30 Uhr muss sie ihre Tochter [1] Kindergarten [2].` (Gợi ý: `von + dem`, `abholen`)
    * Đáp án từng ô: Ô 1 = `["vom"]`, Ô 2 = `["abholen"]`.
    * Giải thích: Đón từ trường mẫu giáo dùng `von + dem = vom Kindergarten`; động từ `abholen` đứng nguyên mẫu ở cuối câu sau `muss`.
71. **Câu 71**: Điền 2 từ còn thiếu để hoàn thành câu: *„Trong công việc của mình, Petra cần một chiếc máy tính và một chiếc bàn làm việc lớn.“*
    * Khung câu hiển thị: `Bei [1] Arbeit braucht Petra [2] Computer und einen großen Schreibtisch.` (Gợi ý: `ihr-`, `ein-`)
    * Đáp án từng ô: Ô 1 = `["ihrer"]`, Ô 2 = `["einen"]`.
    * Giải thích: Sau giới từ `Bei` là Cách 3 (`Dativ`) với `die Arbeit` (giống cái) $\rightarrow$ `Bei ihrer Arbeit`. Sau động từ `braucht` là Cách 4 (`Akkusativ`) với `der Computer` (giống đực) $\rightarrow$ `einen Computer`.
72. **Câu 72**: Điền 2 từ còn thiếu (phân biệt `Wohin? Akkusativ` và `Wo? Dativ`) để hoàn thành câu: *„Buổi sáng Frank đưa con gái vào trường mẫu giáo, và buổi chiều con bé chơi ở trong trường mẫu giáo.“*
    * Khung câu hiển thị: `Am Morgen bringt Frank die Tochter in [1] Kindergarten, und am Nachmittag spielt sie [2] Kindergarten.`
    * Đáp án từng ô: Ô 1 = `["den"]`, Ô 2 = `["im"]`.
    * Giải thích: Đưa vào trường mẫu giáo (`Wohin? + Akkusativ`) là `in den Kindergarten`; chơi ở trong trường mẫu giáo (`Wo? + Dativ`) là `im Kindergarten`.
73. **Câu 73**: Điền 2 từ còn thiếu để hoàn thành câu: *„Vị bác sĩ khám cho người bệnh nhân ở trong bệnh viện.“*
    * Khung câu hiển thị: `Der Arzt untersucht [1] Patienten [2] Krankenhaus.` (Gợi ý: `der Patient`, `das Krankenhaus`)
    * Đáp án từng ô: Ô 1 = `["den"]`, Ô 2 = `["im"]`.
    * Giải thích: `untersuchen` đi với `Akkusativ` (`den Patienten`), còn nơi chốn tĩnh `Wo?` với `das Krankenhaus` đi với `Dativ` (`im Krankenhaus`).
74. **Câu 74**: Điền 2 từ còn thiếu để hoàn thành câu: *„Chị gái của tôi làm nghề nữ đầu bếp và có thể nấu ăn rất giỏi.“*
    * Khung câu hiển thị: `Meine Schwester arbeitet als [1] und [2] sehr gut kochen.` (Gợi ý: `nữ đầu bếp`, `können`)
    * Đáp án từng ô: Ô 1 = `["Köchin", "Koechin"]`, Ô 2 = `["kann"]`.
    * Giải thích: Nữ đầu bếp là `Köchin`; động từ `können` chia cho `meine Schwester` (`sie`) là `kann`.
75. **Câu 75**: Điền 2 từ còn thiếu (phân biệt `Dativ` và `Akkusativ` trong cùng 1 câu) để hoàn thành câu: *„Người nam điều dưỡng đưa cho vị bác sĩ một chiếc bút bi.“*
    * Khung câu hiển thị: `Der Krankenpfleger gibt [1] Arzt [2] Kuli.` (Gợi ý: `der Arzt`, `ein Kuli`)
    * Đáp án từng ô: Ô 1 = `["dem"]`, Ô 2 = `["einen"]`.
    * Giải thích: Người nhận (`Wem?` *cho bác sĩ*) chia ở Cách 3 (`Dativ`) $\rightarrow$ `dem Arzt`; vật được đưa (`Was?` *một chiếc bút bi*) chia ở Cách 4 (`Akkusativ`) $\rightarrow$ `einen Kuli`.
76. **Câu 76**: Điền 2 từ còn thiếu để hoàn thành câu: *„Lúc 12 giờ 30 phút anh ấy mang chiếc ô tô vào xưởng sửa chữa.“*
    * Khung câu hiển thị: `Um 12.30 Uhr [1] er das Auto in [2] Werkstatt.` (Gợi ý: `bringen`, `die Werkstatt`)
    * Đáp án từng ô: Ô 1 = `["bringt"]`, Ô 2 = `["die"]`.
    * Giải thích: Động từ `bringen` chia ở ngôi `er` là `bringt`; mang vào xưởng (`Wohin? + Akkusativ`) với danh từ giống cái `die Werkstatt` là `in die Werkstatt`.
77. **Câu 77**: Điền 2 từ còn thiếu để hoàn thành câu: *„Các bạn có phải làm việc vào thứ Bảy ở trong văn phòng không?“*
    * Khung câu hiển thị: `[1] ihr am Samstag [2] Büro arbeiten?` (Gợi ý: `müssen`, `das Büro`)
    * Đáp án từng ô: Ô 1 = `["Müsst", "müsst", "Muesst", "muesst"]`, Ô 2 = `["im"]`.
    * Giải thích: Câu hỏi đảo động từ khuyết thiếu `müssen` với chủ ngữ `ihr` là `Müsst ihr ...?`; làm việc ở trong văn phòng (`Wo? + Dativ`) là `im Büro`.

---

#### NHÓM 7: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 9 Câu: Câu 78 $\rightarrow$ Câu 86)
78. **Câu 78**:
    * `audio_text`: *"Paula Rausch ist fünfunddreißig Jahre alt und arbeitet als Programmiererin."*
    * `display_sentence`: *"Paula Rausch ist 35 Jahre alt und arbeitet als ___."*
    * `hint_vi`: *"Paula Rausch 35 tuổi và làm nghề nữ lập trình viên."*
    * `accepted_answers`: `["Programmiererin"]`
    * Giải thích: Danh từ chỉ nữ lập trình viên là `die Programmiererin`.
79. **Câu 79**:
    * `audio_text`: *"Der KFZ-Mechatroniker repariert Autos in einer Werkstatt."*
    * `display_sentence`: *"Der KFZ-Mechatroniker repariert Autos in einer ___."*
    * `hint_vi`: *"Người thợ cơ khí ô tô sửa chữa xe hơi ở trong một xưởng sửa chữa."*
    * `accepted_answers`: `["Werkstatt"]`
    * Giải thích: Danh từ `die Werkstatt` có nghĩa là xưởng sửa chữa (`in einer Werkstatt`).
80. **Câu 80**:
    * `audio_text`: *"Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus."*
    * `display_sentence`: *"Der Arzt ___ jeden Tag viele Patienten im Krankenhaus."*
    * `hint_vi`: *"Vị bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện."*
    * `accepted_answers`: `["untersucht"]`
    * Giải thích: Động từ `untersuchen` (khám bệnh) chia ở ngôi thứ 3 số ít (`der Arzt`) là `untersucht`.
81. **Câu 81**:
    * `audio_text`: *"Bei ihrer Arbeit braucht Petra einen schnellen Computer und einen großen Schreibtisch."*
    * `display_sentence`: *"Bei ihrer Arbeit braucht Petra ___ schnellen Computer und einen großen Schreibtisch."*
    * `hint_vi`: *"Trong công việc của mình, Petra cần một chiếc máy tính nhanh và một cái bàn làm việc lớn."*
    * `accepted_answers`: `["einen"]`
    * Giải thích: Sau động từ `braucht` (`Akkusativ`), mạo từ không xác định của `der Computer` là `einen`.
82. **Câu 82**:
    * `audio_text`: *"Um sechzehn Uhr dreißig muss sie ihre Tochter vom Kindergarten abholen."*
    * `display_sentence`: *"Um 16.30 Uhr muss sie ihre Tochter vom Kindergarten ___."*
    * `hint_vi`: *"Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo."*
    * `accepted_answers`: `["abholen"]`
    * Giải thích: Động từ tách `abholen` đứng ở cuối câu ở dạng nguyên mẫu khi đi cùng `muss`.
83. **Câu 83**:
    * `audio_text`: *"Frank Müller ist Lehrer von Beruf und hat jetzt Ferien."*
    * `display_sentence`: *"Frank Müller ist ___ von Beruf und hat jetzt Ferien."*
    * `hint_vi`: *"Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ."*
    * `accepted_answers`: `["Lehrer"]`
    * Giải thích: Danh từ chỉ nam giáo viên là `der Lehrer` (`Er ist Lehrer von Beruf`).
84. **Câu 84**:
    * `audio_text`: *"Die Floristin verkauft schöne Blumen im Blumengeschäft."*
    * `display_sentence`: *"Die Floristin verkauft schöne Blumen im ___."*
    * `hint_vi`: *"Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa."*
    * `accepted_answers`: `["Blumengeschäft", "Blumengeschaeft"]`
    * Giải thích: Danh từ `das Blumengeschäft` có nghĩa là cửa hàng hoa (`im Blumengeschäft`).
85. **Câu 85**:
    * `audio_text`: *"Sie muss ihre Kunden im Büro oft anrufen."*
    * `display_sentence`: *"Sie muss ihre ___ im Büro oft anrufen."*
    * `hint_vi`: *"Cô ấy thường xuyên phải gọi điện cho các khách hàng của mình ở trong văn phòng."*
    * `accepted_answers`: `["Kunden"]`
    * Giải thích: Danh từ số nhiều `die Kunden` có nghĩa là những khách hàng.
86. **Câu 86**:
    * `audio_text`: *"Um neunzehn Uhr bringt der Vater seine Tochter ins Bett."*
    * `display_sentence`: *"Um 19 Uhr bringt der Vater seine Tochter ___ Bett."*
    * `hint_vi`: *"Lúc 19 giờ người bố đưa con gái của mình lên giường đi ngủ."*
    * `accepted_answers`: `["ins"]`
    * Giải thích: Cụm `ins Bett bringen` (`in + das Bett` — `Wohin? Akkusativ`) có nghĩa là đưa lên giường đi ngủ.

---

#### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT $\rightarrow$ ĐỨC (`dich_cau_vd` — 7 Câu: Câu 87 $\rightarrow$ Câu 93, chấm đa đáp án linh hoạt)
87. **Câu 87**: Dịch câu sau sang tiếng Đức: ***"Bạn làm nghề gì? — Tôi làm nghề lập trình viên."***
    * `accepted_answers`:
      * `"Was bist du von Beruf? Ich arbeite als Programmierer."`
      * `"Was bist du von Beruf? Ich bin Programmierer."`
      * `"Was bist du von Beruf? Ich bin Programmierer von Beruf."`
      * `"Was machst du beruflich? Ich arbeite als Programmierer."`
      * `"Was machst du beruflich? Ich bin Programmiererin."`
    * Giải thích: Hỏi nghề nghiệp thân mật dùng `Was bist du von Beruf?` hoặc `Was machst du beruflich?`; trả lời dùng `Ich bin Programmierer` hoặc `Ich arbeite als Programmierer`.
88. **Câu 88**: Dịch câu sau sang tiếng Đức: ***"Lúc 7 giờ 15 phút cô ấy phải đi bằng xe buýt đến chỗ làm."***
    * `accepted_answers`:
      * `"Um 7.15 Uhr muss sie mit dem Bus zur Arbeit fahren."`
      * `"Um Viertel nach sieben muss sie mit dem Bus zur Arbeit fahren."`
      * `"Sie muss um 7.15 Uhr mit dem Bus zur Arbeit fahren."`
      * `"Um sieben Uhr fünfzehn muss sie mit dem Bus zur Arbeit fahren."`
    * Giải thích: Động từ khuyết thiếu `muss` đứng ở vị trí số 2, động từ chính `fahren` đứng nguyên mẫu ở cuối câu; phương tiện `mit dem Bus` và đích đến `zur Arbeit` đều chia ở `Dativ`.
89. **Câu 89**: Dịch câu sau sang tiếng Đức: ***"Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."***
    * `accepted_answers`:
      * `"Bei ihrer Arbeit braucht Petra einen Computer und einen großen Schreibtisch."`
      * `"Petra braucht bei ihrer Arbeit einen Computer und einen großen Schreibtisch."`
      * `"Für ihre Arbeit braucht Petra einen Computer und einen großen Schreibtisch."`
    * Giải thích: `Bei ihrer Arbeit` chia ở `Dativ`; sau động từ `braucht` thì cả `der Computer` và `der Schreibtisch` đều chia ở `Akkusativ` (`einen Computer und einen großen Schreibtisch`).
90. **Câu 90**: Dịch câu sau sang tiếng Đức: ***"Người thợ cơ khí sửa chữa ô tô ở trong một xưởng sửa chữa."***
    * `accepted_answers`:
      * `"Der Mechatroniker repariert Autos in einer Werkstatt."`
      * `"Der KFZ-Mechatroniker repariert Autos in einer Werkstatt."`
      * `"Der Mechatroniker repariert das Auto in einer Werkstatt."`
      * `"In einer Werkstatt repariert der KFZ-Mechatroniker Autos."`
    * Giải thích: Tân ngữ trực tiếp `Autos` ở `Akkusativ`, còn nơi làm việc tĩnh `in einer Werkstatt` chia ở `Dativ`.
91. **Câu 91**: Dịch câu sau sang tiếng Đức: ***"Lúc 8 giờ 30 phút anh ấy phải đưa con gái vào trường mẫu giáo."***
    * `accepted_answers`:
      * `"Um 8.30 Uhr muss er die Tochter in den Kindergarten bringen."`
      * `"Um halb neun muss er die Tochter in den Kindergarten bringen."`
      * `"Um 8.30 Uhr muss er seine Tochter in den Kindergarten bringen."`
      * `"Er muss um 8.30 Uhr seine Tochter in den Kindergarten bringen."`
    * Giải thích: Đưa con gái vào trường mẫu giáo (`bringen` $\rightarrow$ di chuyển `Wohin?`) dùng **Cách 4 (`Akkusativ`)**: `in den Kindergarten`.
92. **Câu 92**: Dịch câu sau sang tiếng Đức: ***"Nữ bác sĩ khám cho các bệnh nhân ở trong bệnh viện."***
    * `accepted_answers`:
      * `"Die Ärztin untersucht Patienten im Krankenhaus."`
      * `"Die Ärztin untersucht die Patienten im Krankenhaus."`
      * `"Im Krankenhaus untersucht die Ärztin Patienten."`
    * Giải thích: Nữ bác sĩ là `Die Ärztin`; khám cho bệnh nhân là `untersucht Patienten` (`Akkusativ`); ở trong bệnh viện là `im Krankenhaus` (`Dativ`).
93. **Câu 93**: Dịch câu sau sang tiếng Đức: ***"Người điều dưỡng giúp đỡ vị bác sĩ mỗi ngày."***
    * `accepted_answers`:
      * `"Der Krankenpfleger hilft dem Arzt jeden Tag."`
      * `"Jeden Tag hilft der Krankenpfleger dem Arzt."`
      * `"Die Krankenschwester hilft dem Arzt jeden Tag."`
      * `"Die Krankenpflegerin hilft dem Arzt jeden Tag."`
    * Giải thích: Động từ `helfen` biến âm `e -> i` thành `hilft` và bắt buộc đi với **Cách 3 (`Dativ`)**: `der Arzt` $\rightarrow$ **`dem Arzt`**.

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC $\rightarrow$ VIỆT (`dich_cau_dv` — 7 Câu: Câu 94 $\rightarrow$ Câu 100, chấm đa đáp án linh hoạt)
94. **Câu 94**: Dịch câu sau sang tiếng Việt: ***„Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.“***
    * `accepted_answers`:
      * `"Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo"`
      * `"Vào lúc 16h30 Paula phải đón con gái từ nhà trẻ về"`
      * `"Lúc 4 giờ rưỡi chiều Paula phải đón con gái của cô ấy từ trường mầm non"`
    * Giải thích: `muss ... abholen` = phải đón; `ihre Tochter` = con gái của cô ấy; `vom Kindergarten` = từ trường mẫu giáo.
95. **Câu 95**: Dịch câu sau sang tiếng Việt: ***„Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen.“***
    * `accepted_answers`:
      * `"Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ"`
      * `"Nghề của Frank Müller là giáo viên nhưng hôm nay anh ấy được nghỉ lễ và có thể ngủ tới 7 giờ"`
      * `"Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ đến 7 giờ"`
    * Giải thích: `ist Lehrer von Beruf` = làm nghề giáo viên; `hat Ferien` = có kỳ nghỉ; `kann bis 7 Uhr schlafen` = có thể ngủ đến 7 giờ.
96. **Câu 96**: Dịch câu sau sang tiếng Việt: ***„Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen.“***
    * `accepted_answers`:
      * `"Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình"`
      * `"Điện thoại rất quan trọng với cô ấy bởi vì cô ấy phải gọi điện cho khách hàng của mình thường xuyên"`
      * `"Cái điện thoại rất quan trọng đối với cô ấy vì cô ấy thường phải gọi cho khách hàng"`
    * Giải thích: `wichtig für sie` = quan trọng đối với cô ấy; `muss ihre Kunden oft anrufen` = thường xuyên phải gọi điện cho khách hàng của mình.
97. **Câu 97**: Dịch câu sau sang tiếng Việt: ***„Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining.“***
    * `accepted_answers`:
      * `"Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá"`
      * `"Buổi chiều ông Müller đưa xe hơi vào xưởng sửa chữa và sau đó đi tập đá bóng"`
      * `"Vào buổi chiều anh Müller đem ô tô tới xưởng sửa xe rồi đi tập bóng đá"`
    * Giải thích: `bringt sein Auto in die Werkstatt` = mang ô tô vào xưởng sửa chữa (`Akkusativ`); `geht zum Fußballtraining` = đi đến buổi tập bóng đá (`Dativ`).
98. **Câu 98**: Dịch câu sau sang tiếng Việt: ***„Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität.“***
    * `accepted_answers`:
      * `"Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học"`
      * `"Nữ giáo viên dạy học sinh ở một ngôi trường vào buổi sáng và dạy sinh viên tại trường đại học vào buổi chiều"`
      * `"Buổi sáng cô giáo giảng dạy học sinh ở trường phổ thông và buổi chiều dạy sinh viên ở trường đại học"`
    * Giải thích: `vormittags` = vào buổi sáng; `Schüler an einer Schule` = học sinh tại một trường học; `nachmittags` = vào buổi chiều; `Studenten an der Universität` = sinh viên tại trường đại học.
99. **Câu 99**: Dịch câu sau sang tiếng Việt: ***„Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat.“***
    * `accepted_answers`:
      * `"Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối"`
      * `"Từ 8 giờ đến 10 giờ tối Paula có thể xem truyền hình trong phòng khách sau khi làm xong bữa tối"`
      * `"Từ 20 giờ đến 22 giờ Paula có thể xem tivi trong phòng khách sau khi nấu bữa tối"`
    * Giải thích: `kann ... fernsehen` = có thể xem tivi; `im Wohnzimmer` = ở trong phòng khách; `das Abendessen machen` = làm bữa tối.
100. **Câu 100**: Dịch câu sau sang tiếng Việt: ***„Der Friseur schneidet meinem Bruder im Friseursalon die Haare.“***
     * `accepted_answers`:
       * `"Người thợ cắt tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc"`
       * `"Thợ làm tóc cắt tóc cho anh trai của tôi tại tiệm cắt tóc"`
       * `"Người thợ làm tóc đang cắt tóc cho anh tôi ở trong salon tóc"`
     * Giải thích: Câu kết hợp cả `Dativ` và `Akkusativ`: `meinem Bruder` (`Wem? -> Dativ`: cho anh trai tôi), `im Friseursalon` (`Wo? -> Dativ`: ở trong tiệm làm tóc), `die Haare` (`Was? -> Akkusativ`: mái tóc).

---

## PHẦN 4: KIẾN TRÚC BỘ SINH ĐỀ NGẪU NHIÊN ĐA CHIỀU (`DYNAMIC MULTI-VARIABLE RANDOMIZER`) CHO BÀI 7

Để đảm bảo mỗi lần người học vào làm hoặc bấm **`🔄 Đổi đề khác`** sẽ nhận được các biến thể câu hỏi hoàn toàn mới mẻ với **đủ mọi ngôi nhân xưng, số tuổi, khung giờ và ngữ cảnh**, Antigravity IDE phải cài đặt 4 Engine sinh câu hỏi động (`Atomic Question Generators`) cho Bài 7:

### 4.1. Engine 1: Biến thiên Đa Chủ Ngữ $\times$ 16 Nghề Nghiệp (Nam/Nữ) $\times$ Hoạt Động $\times$ Nơi Làm Việc (`Profession-Activity-Workplace Generator`)
* Tự động rút ngẫu nhiên chủ ngữ (`Ich, Du, Mein Vater, Meine Mutter, Herr Kien, Frau Linh, Unser Nachbar, Deine Tante, Wir, Ihr, Die Kollegen...`), tự động chọn đúng danh từ nghề nghiệp theo giới tính của chủ ngữ (`Programmierer` vs. `Programmiererin`, `Arzt` vs. `Ärztin`, `Koch` vs. `Köchin`), ghép với hoạt động nghề nghiệp và nơi làm việc chia đúng ở Cách 3 (`Dativ`).

### 4.2. Engine 2: Biến thiên Lịch Trình Hàng Ngày Với 6 `Modalverben` & Động Từ Tách (`Daily Schedule & Modalverb Generator`)
* Tự động biến thiên:
  * **Tên nhân vật & Tuổi** (random từ `22` đến `60` tuổi) + **Nghề nghiệp**.
  * **Khung giờ ngẫu nhiên** (`um 6.00 Uhr`, `um 6.45 Uhr`, `um 7.30 Uhr`, `von 8.00 bis 16.30 Uhr`, `um 17.15 Uhr`, `von 20.30 bis 22.15 Uhr`...).
  * **Động từ khuyết thiếu** (`müssen, können, möchten, wollen, dürfen, sollen`) chia theo đủ 9 ngôi + **Động từ nguyên mẫu ở cuối câu** (`aufstehen, abholen, fernsehen, einkaufen, anrufen, kochen, schlafen, mit dem Bus zur Arbeit fahren, in den Kindergarten bringen...`).

### 4.3. Engine 3: Bộ Đối Chiếu Thực Chiến `Akkusativ` vs. `Dativ` (`Kasus-Kontrast Engine`)
* Tự động sinh các cặp câu đối xứng để kiểm tra khả năng phân biệt Cách 4 và Cách 3 của người học:
  1. **Đối xứng Động từ**: `brauchen / suchen / untersuchen / anrufen / kaufen (+ Akkusativ)` $\longleftrightarrow$ `helfen / danken / gefallen / gehören (+ Dativ)`.
  2. **Đối xứng Giới từ cố định**: `für / ohne / durch / um (+ Akkusativ)` $\longleftrightarrow$ `mit / bei / von / zu / aus / nach (+ Dativ)`.
  3. **Đối xứng `Wohin? (Akkusativ)` vs. `Wo? (Dativ)`**: `in den Kindergarten bringen` $\leftrightarrow$ `im Kindergarten sein`; `in die Werkstatt fahren` $\leftrightarrow$ `in der Werkstatt arbeiten`; `ins Bett gehen` $\leftrightarrow$ `im Bett liegen`; `ins Büro gehen` $\leftrightarrow$ `im Büro sitzen`; `an einen Tisch setzen` $\leftrightarrow$ `an einem Tisch sitzen`.

### 4.4. Engine 4: Ma Trận Từ Hạn Định Cách 4 Theo 9 Ngôi Sở Hữu (`Possessivartikel im Akkusativ Matrix`)
* Tự động kết hợp 9 ngôi (`ich -> meinen/meine/mein`, `du -> deinen/deine/dein`, `er -> seinen...`, `sie -> ihren...`, `wir -> unseren...`, `ihr -> euren/eure/euer`, `Sie -> Ihren...`) với 25 danh từ đồ dùng công việc (`der Computer, der Schreibtisch, der Drucker, der Kalender, der Kuli, die Tasche, die Maus, die Brille, das Telefon, das Buch, das Auto, die Kunden, die Kollegen...`).

---

## PHẦN 5: DANH SÁCH KIỂM THỬ BẮT BUỘC SAU KHI CODE (`POST-CODING QA & DEDUPLICATION CHECKLIST`)

Sau khi code xong Bài 7, Antigravity IDE **BẮT BUỘC** phải viết và chạy kịch bản kiểm thử tự động (`verify_lesson7_qa.py`) để kiểm tra 6 tiêu chí sau trước khi hoàn tất:

1. **Kiểm tra Bảo toàn Tuyệt đối Bài 1 $\rightarrow$ Bài 6 (`Zero-Regression Check`)**:
   * Xác nhận trong cơ sở dữ liệu `deutsch_meister.db`: **Bài 1 (P1), Bài 1 (P2), Bài 2, Bài 3, Bài 4, Bài 5, Bài 6** vẫn giữ nguyên 100% nội dung lý thuyết, từ vựng và số lượng câu hỏi bài tập, không có bất kỳ bài học cũ nào bị xóa hay thay đổi.
2. **Kiểm tra Quy mô 100 Câu hỏi & Chống Trùng Lặp Tuyệt Đối (`100-Question & Zero-Duplicate Verification`)**:
   * Xác nhận **Bài 7** có đúng **100 câu hỏi** (`trac_nghiem`: 18, `dien_khuyet`: 15, `dich_nghia_vd`: 12, `dich_nghia_dv`: 12, `noi_o`: 10, `dien_tao_cau`: 10, `nghe_dien`: 9, `dich_cau_vd`: 7, `dich_cau_dv`: 7).
   * Quét toàn bộ 100 câu hỏi để khẳng định **0 câu trùng lặp** (`len(unique_questions) == 100`). Nếu phát hiện bất kỳ 2 câu nào trùng nhau, kịch bản phải báo lỗi và thay thế ngay lập tức.
3. **Kiểm tra Khớp Nguyên Tử Đề Bài – Đáp Án – Dịch Nghĩa – Giải Thích (`Atomic Alignment Check`)**:
   * Chạy vòng lặp giả lập 20 lần gọi API lấy đề bài tập Bài 7 (bao gồm cả khi kích hoạt Randomizer): Đảm bảo 100% câu hỏi đều có `correct_answer` nằm trong `options` (với trắc nghiệm), `accepted_answers` không rỗng (với tự luận/điền từ), `translation_vi` và `explanation` khớp chính xác với chủ ngữ, nghề nghiệp, động từ khuyết thiếu và cách ngữ pháp (`Akkusativ` hay `Dativ`) trong câu hỏi.
4. **Kiểm tra 100% Thẻ Từ Vựng & Câu Ví Dụ (`Vocabulary Card Match Check`)**:
   * Quét toàn bộ từ vựng của Bài 7 trong `seed_a1_b7.py` và `lexikon_db.js`: Đảm bảo 100% câu ví dụ tiếng Đức (`example_de`) có chứa chính xác danh từ trên thẻ đó và bản dịch tiếng Việt (`example_vi`) dịch đúng nghĩa của câu ví dụ đó.
5. **Kiểm tra Giọng Đọc TTS `de-DE` (`Voice Check`)**:
   * Đảm bảo mọi nút `🔊` trong Bài 7 và câu hỏi `nghe_dien` chỉ truyền văn bản tiếng Đức chuẩn vào `speakGerman()`, không đọc lẫn tiếng Việt hay ký tự đặc biệt.
6. **Đồng bộ lên GitHub (`Git Commit & Push`)**:
   * Sau khi toàn bộ bài kiểm thử đạt `100% PASS`, đẩy code lên repository `taolagautruc/deutsch-meister`:
     ```bash
     git add .
     git commit -m "Add Lesson 7 (Beruf, Modalverben, Artikelwoerter im Akkusativ vs Dativ) with 100 unique randomized exercises and full Zero-Bug QA"
     git push origin main
     ```