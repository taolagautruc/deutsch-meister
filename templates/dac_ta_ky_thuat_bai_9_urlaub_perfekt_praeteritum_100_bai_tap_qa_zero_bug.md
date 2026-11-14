# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 9 (A1) "URLAUB - DU LỊCH - PERFEKT & PRÄTERITUM (QUÁ KHỨ VĂN NÓI)" — TÍCH HỢP SƠ ĐỒ TƯƠNG TÁC, BẢNG ĐỘNG TỪ NGUỒN CHUẨN & 100 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1**, **Bài 1 P2**, **Bài 2**, **Bài 3**, **Bài 4**, **Bài 5**, **Bài 6**, **Bài 7**, **Bài 8**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này chỉ gồm: **(1)** tạo mới hoàn toàn **Bài 9 (`lessons/a1/seed_a1_b9.py`)** ở vị trí **`lesson_order = 10`** của cấp độ **A1**; **(2)** *cộng dồn thêm* động từ và từ vựng mới của Bài 9 vào 2 chuyên mục tra cứu; **(3)** *mở rộng thêm* (không thay thế) kiến thức Đấu trường tới Bài 9; **(4)** viết và chạy kịch bản kiểm thử toàn diện.
> * **Quy tắc chống ghi đè khi cộng dồn dữ liệu**: Nếu một động từ / danh từ của Bài 9 **đã tồn tại** trong `verbs_db.js` / `lexikon_db.js` từ bài trước (ví dụ `gehen`, `fahren`, `das Hotel`, `das Wetter`, `das Essen`...), thì **GIỮ NGUYÊN thẻ cũ, KHÔNG tạo thẻ trùng, KHÔNG sửa thẻ cũ**. Chỉ thêm các mục chưa có (so khớp theo `lemma` + `article`). Nếu schema cho phép thêm trường mới mà không phá thẻ cũ (ví dụ `perfekt`), chỉ thêm trường đó cho **thẻ mới của Bài 9**.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu. Video bài giảng chỉ là tài liệu tham khảo để soạn nội dung.
>
> ---
>
> ### 🎯 2. PHẠM VI KIẾN THỨC & ĐỘ KHÓ (`A1+ SCOPE CONTROL`)
> * **Trọng tâm tuyệt đối của Bài 9 là `Perfekt` (quá khứ văn nói)**: công thức `haben/sein + Partizip II`, vị trí động từ (`Satzklammer`), quy tắc tạo `Partizip II` (6 nhóm), phân biệt `haben` / `sein`, và danh sách động từ bất quy tắc. Đi kèm là **`Präteritum` của `sein` (`war`) và `haben` (`hatte`)** để nói về kỳ nghỉ, cùng từ vựng *Natur - Reise - Urlaub*.
> * **Độ khó**: chỉ cao hơn tài liệu gốc *một chút* (có thêm câu phủ định, câu hỏi, đảo ngữ với trạng từ thời gian, động từ tách / không tách, `-ieren`, động từ bất quy tắc phổ biến). **Không** đưa vào bài tập: `Plusquamperfekt`, `Präteritum` của động từ thường (chỉ *nhận biết* trong lý thuyết ⭐), `Perfekt` với động từ phản thân hoặc động từ khuyết thiếu, câu phụ `weil / dass / wenn`. Mọi câu hỏi phải làm được với kiến thức A1.
> * **Tên gọi chuẩn**: Tiêu đề bài là **`Perfekt`** (viết bằng **k**, không phải *Perfect*). Cụm "Perfekt Präteritum" trong yêu cầu được hiểu là **cả hai thì quá khứ**: `Perfekt` (trọng tâm) và `Präteritum` (của `sein/haben`). Lý thuyết phải giải thích rõ hai thì này khác nhau thế nào.
>
> ---
>
> ### 🗺️ 3. YÊU CẦU HÌNH ẢNH MINH HỌA (`VISUAL DIAGRAMS`) CHO BÀI 9
> Perfekt là phần khó, nên Antigravity IDE **BẮT BUỘC** xây dựng module **`static/js/perfekt_svg.js`** (SVG nội tuyến, tương thích Dark/Light mode) gồm **6 sơ đồ** (đặc tả chi tiết ở mục 2.7): `V1` Khung câu `Satzklammer`; `V2` Lưu đồ tạo `Partizip II`; `V3` Cây quyết định `haben / sein`; `V4` Bản đồ hành trình sông Donau (tương tác); `V5` Trục thời gian `Perfekt / Präteritum`; `V6` Máy tính `Partizip` tương tác. Một số câu hỏi bài tập có trường `visual` để hiển thị sơ đồ ngay trên khung câu hỏi.
>
> ---
>
> ### 🔍 4. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI & CHỐNG TRÙNG LẶP (`ZERO-BUG & ZERO-DUPLICATE QA PROTOCOL`)
> Các lỗi sau đã từng xuất hiện trên web và **KHÔNG ĐƯỢC LẶP LẠI**. Mỗi lỗi có một quy tắc kiểm tra cụ thể:
> 1. **Dịch sai nghĩa** → Mọi bản dịch tiếng Việt phải dịch **đúng câu tiếng Đức đã hoàn chỉnh** (đã điền đáp án), đúng thì quá khứ (dùng *"đã"*), đúng ngôi chủ ngữ.
> 2. **Thiếu phần dịch nghĩa** → 100% từ vựng, ví dụ, đoạn văn, bảng lý thuyết và **100 câu hỏi** đều phải có `translation_vi` không rỗng.
> 3. **Dịch / đáp án không liên quan đến đề bài** → Đề bài, hình minh họa, đáp án, dịch nghĩa và giải thích phải cùng sinh ra từ **một đối tượng dữ liệu duy nhất** (`single source of truth`). Mục `Giải thích` bắt buộc **chứa chính chuỗi đáp án đúng**.
> 4. **Voice thiếu / voice sai** → Mọi nút `🔊` phải có và chỉ truyền **chuỗi tiếng Đức sạch** (`de-DE`) vào `speakGerman()`. Không đọc lẫn tiếng Việt, không đọc ký hiệu `___`, `→`, `[1]`, `/`. Với câu điền khuyết, voice đọc **câu đã điền đầy đủ**, không đọc chỗ trống.
> 5. **Ví dụ không khớp thẻ từ vựng** → Thẻ từ nào thì `example_de` phải chứa **đúng dạng từ đó** (ví dụ thẻ `die Alpen` thì ví dụ phải có `Alpen`), và `example_vi` phải dịch đúng câu đó.
> 6. **Giải thích sai đáp án** → Giải thích phải khớp đáp án đúng và quy tắc ngữ pháp thật sự (ví dụ: không giải thích `gearbeitet` bằng quy tắc `-ieren`).
> 7. **Chống trùng lặp câu hỏi 100%** → `len(set(normalized_questions)) == 100`. Toàn bộ 100 câu trong Bài 9 là câu **mới sáng tác**, chỉ *tham khảo* ý tưởng từ bảng giảng, **không sao chép** nguyên câu của giáo trình hay của Bài 8.
> 8. **Đa dạng ngôi & ngữ cảnh** → Câu hỏi dùng đủ `ich, du, er, sie, es, wir, ihr, sie (số nhiều), Sie`, tên riêng, nghề nghiệp, gia đình, và các bối cảnh Việt Nam (Đà Lạt, Hội An, Phú Quốc, Hạ Long, Cát Bà) lẫn châu Âu (Wien, Linz, Passau, Budapest, Marseille, Alpen).
> 9. **Không sửa bài cũ** → chạy `Zero-Regression Check` (xem Phần 5).
>
> ---
>
> ### ⚠️ 5. NHỮNG ĐIỂM CẦN CHUẨN HÓA SO VỚI BẢNG VIẾT TRÊN LỚP (ĐỌC KỸ TRƯỚC KHI CODE)
> Bảng giảng được viết gọn cho người mới học. Khi đưa lên web cần ghi chú thêm để người học không bị sai về sau:
> 1. **`ziehen`**: Bảng ghi `ziehen: kéo → ist gezogen`. Thực tế: **`ziehen` = *kéo* → `hat gezogen`**; còn **`ziehen` = *chuyển nhà / dọn đến* → `ist gezogen`** (thường dùng `umziehen → ist umgezogen`). Web phải hiển thị cả hai nghĩa; **bài tập chỉ dùng nghĩa rõ ràng**, không hỏi mơ hồ.
> 2. **`laufen`**: `ist gelaufen` (đi bộ / chạy tới đâu đó). Nếu có tân ngữ chỉ quãng đường kiểu thể thao thì có thể gặp `hat gelaufen`; ở A1 chỉ dạy `ist gelaufen`.
> 3. **`liegen`**: bảng ghi `hat gelegen` (chuẩn ở miền Bắc Đức). Ở Nam Đức, Áo, Thụy Sĩ người ta nói `ist gelegen`. Web dạy `hat gelegen` và ghi chú ngắn về biến thể vùng miền.
> 4. **`fahren / fliegen / schwimmen`** dùng `sein` khi chỉ sự di chuyển tới / trong không gian; nhưng nếu có **tân ngữ trực tiếp** (`das Auto fahren`) thì dùng `haben`. Bài tập chỉ dùng trường hợp di chuyển rõ ràng (`sein`).
> 5. **`wissen: hat gewusst`, `denken: hat gedacht`, `bringen: hat gebracht`** là **động từ hỗn hợp** (đuôi `-t` nhưng đổi gốc từ) — phải dạy thành nhóm riêng.
> 6. **Ngày tháng thực tế**: cuộc đạp xe sông Donau đi theo thứ tự **Passau → Linz → Wien → Budapest** (đúng địa lý). Không đảo thứ tự các thành phố trong sơ đồ.

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 → Bài 8 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 9** theo quy tắc chống ghi đè ở mục 1.

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung **22 động từ trọng tâm của Bài 9**. Với mỗi thẻ: bảng chia **Präsens** theo 6 ngôi, dòng **Perfekt** (`hat/ist + Partizip II`), loại động từ, phát âm `de-DE` và 1 câu ví dụ **chứa đúng động từ đó** (dạng Perfekt) kèm dịch nghĩa. Đây cũng là dữ liệu mẫu cho các Engine sinh đề.

| # | Động từ (nghĩa) | Loại | Präsens: ich / du / er·sie·es / wir / ihr / sie·Sie | Perfekt | Ví dụ (`🔊 de-DE`) & Dịch |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **machen** *(làm, thực hiện)* | Quy tắc `ge-t` | mache / machst / macht / machen / macht / machen | **hat gemacht** | *„Wir haben gestern eine Radtour gemacht.“* — Hôm qua chúng tôi đã đi một chuyến đạp xe. |
| 2 | **besichtigen** *(tham quan)* | Tiền tố `be-` không tách | besichtige / besichtigst / besichtigt / besichtigen / besichtigt / besichtigen | **hat besichtigt** | *„Im Urlaub haben wir ein altes Schloss besichtigt.“* — Trong kỳ nghỉ chúng tôi đã tham quan một lâu đài cổ. |
| 3 | **übernachten** *(qua đêm, ngủ lại)* | Tiền tố `über-` không tách + gốc đuôi `-t` → `-et` | übernachte / übernachtest / übernachtet / übernachten / übernachtet / übernachten | **hat übernachtet** | *„Die Familie hat in einer kleinen Pension übernachtet.“* — Gia đình đã ngủ lại trong một nhà nghỉ nhỏ. |
| 4 | **besuchen** *(thăm, ghé thăm)* | Tiền tố `be-` không tách | besuche / besuchst / besucht / besuchen / besucht / besuchen | **hat besucht** | *„Im Sommer habe ich meine Großeltern besucht.“* — Vào mùa hè tôi đã đi thăm ông bà. |
| 5 | **einkaufen** *(mua sắm)* | **Động từ tách** `ein-` | ich kaufe … ein / du kaufst … ein / er kauft … ein / wir kaufen … ein / ihr kauft … ein / sie kaufen … ein | **hat eingekauft** | *„Am zweiten Tag haben wir auf dem Markt eingekauft.“* — Vào ngày thứ hai chúng tôi đã đi mua sắm ở chợ. |
| 6 | **fotografieren** *(chụp ảnh)* | Đuôi `-ieren` (không có `ge-`) | fotografiere / fotografierst / fotografiert / fotografieren / fotografiert / fotografieren | **hat fotografiert** | *„Er hat den Sonnenuntergang am Meer fotografiert.“* — Anh ấy đã chụp ảnh hoàng hôn bên bờ biển. |
| 7 | **erreichen** *(đến được, đạt tới)* | Tiền tố `er-` không tách | erreiche / erreichst / erreicht / erreichen / erreicht / erreichen | **hat erreicht** | *„Wir haben das Reiseziel am Abend erreicht.“* — Chúng tôi đã đến được điểm đến vào buổi tối. |
| 8 | **wandern** *(đi bộ đường dài)* | Quy tắc, **dùng `sein`** (di chuyển) | wand(e)re / wanderst / wandert / wandern / wandert / wandern | **ist gewandert** | *„Mein Vater ist früher oft in den Bergen gewandert.“* — Ngày trước bố tôi thường đi bộ đường dài trên núi. |
| 9 | **zelten** *(cắm trại, dựng lều)* | Gốc đuôi `-t` → `ge-et` | zelte / zeltest / zeltet / zelten / zeltet / zelten | **hat gezeltet** | *„Die Kinder haben im Garten gezeltet.“* — Những đứa trẻ đã cắm trại trong vườn. |
| 10 | **probieren** *(thử [món ăn])* | Đuôi `-ieren` | probiere / probierst / probiert / probieren / probiert / probieren | **hat probiert** | *„Hast du schon die Nudelsuppe probiert?“* — Bạn đã thử món súp mì chưa? |
| 11 | **passieren** *(xảy ra)* | Đuôi `-ieren`, **dùng `sein`**, chủ yếu ngôi `es` | es passiert (ich passiere / du passierst / wir passieren …) | **ist passiert** | *„Im Urlaub ist etwas Lustiges passiert.“* — Trong kỳ nghỉ đã xảy ra một chuyện vui. |
| 12 | **anschauen** *(ngắm, xem)* | **Động từ tách** `an-` | ich schaue … an / du schaust … an / er schaut … an / wir schauen … an / ihr schaut … an / sie schauen … an | **hat angeschaut** | *„Die Touristen haben die Altstadt angeschaut.“* — Các du khách đã ngắm phố cổ. |
| 13 | **planen** *(lên kế hoạch)* | Quy tắc `ge-t` | plane / planst / plant / planen / plant / planen | **hat geplant** | *„Mein Onkel hat die Reise im Januar geplant.“* — Chú tôi đã lên kế hoạch cho chuyến đi vào tháng Giêng. |
| 14 | **regnen** *(mưa)* | Gốc `-gn` → `ge-et`, chỉ ngôi `es` | es regnet (sie regnen — hiếm) | **hat geregnet** | *„In den Alpen hat es drei Tage geregnet.“* — Ở dãy Alps trời đã mưa ba ngày. |
| 15 | **bleiben** *(ở lại)* | Bất quy tắc, **`sein`** | bleibe / bleibst / bleibt / bleiben / bleibt / bleiben | **ist geblieben** | *„Meine Freunde sind nur einen Tag in der Stadt geblieben.“* — Các bạn tôi chỉ ở lại thành phố một ngày. |
| 16 | **fliegen** *(bay)* | Bất quy tắc, **`sein`** | fliege / fliegst / fliegt / fliegen / fliegt / fliegen | **ist geflogen** | *„Sie sind von Frankfurt nach Hanoi geflogen.“* — Họ đã bay từ Frankfurt đến Hà Nội. |
| 17 | **schwimmen** *(bơi)* | Bất quy tắc, **`sein`** (di chuyển) | schwimme / schwimmst / schwimmt / schwimmen / schwimmt / schwimmen | **ist geschwommen** | *„Die Kinder sind zur Insel geschwommen.“* — Những đứa trẻ đã bơi tới hòn đảo. |
| 18 | **treffen** *(gặp)* | Bất quy tắc, đổi `e → i` ở `du, er/sie/es` | treffe / triffst / trifft / treffen / trefft / treffen | **hat getroffen** | *„Am Strand habe ich eine Freundin getroffen.“* — Ở bãi biển tôi đã gặp một người bạn gái. |
| 19 | **schlafen** *(ngủ)* | Bất quy tắc, đổi `a → ä` ở `du, er/sie/es` | schlafe / schläfst / schläft / schlafen / schlaft / schlafen | **hat geschlafen** | *„Wir haben im Zug gut geschlafen.“* — Chúng tôi đã ngủ ngon trên tàu. |
| 20 | **anrufen** *(gọi điện)* | **Động từ tách** `an-` + bất quy tắc | ich rufe … an / du rufst … an / er ruft … an / wir rufen … an / ihr ruft … an / sie rufen … an | **hat angerufen** | *„Meine Mutter hat mich aus dem Urlaub angerufen.“* — Mẹ tôi đã gọi điện cho tôi từ kỳ nghỉ. |
| 21 | **reisen** *(đi du lịch, đi xa)* | Quy tắc, **dùng `sein`** | reise / reist / reist / reisen / reist / reisen | **ist gereist** | *„Sie sind mit dem Zug durch Europa gereist.“* — Họ đã đi du lịch khắp châu Âu bằng tàu hỏa. |
| 22 | **buchen** *(đặt [phòng, vé])* | Quy tắc `ge-t` | buche / buchst / bucht / buchen / bucht / buchen | **hat gebucht** | *„Wir haben zwei Zimmer für drei Nächte gebucht.“* — Chúng tôi đã đặt hai phòng cho ba đêm. |

> 📌 **Lưu ý hiển thị**: thẻ động từ phải có thêm dòng *"Perfekt: ich habe/bin … + Partizip II"* chia đủ 6 ngôi (`ich habe gemacht → habe … gemacht`, `du hast … gemacht`, `er hat … gemacht`, `wir haben … gemacht`, `ihr habt … gemacht`, `sie haben … gemacht`; với `sein`: `bin, bist, ist, sind, seid, sind`). Phát âm `🔊` đọc **một câu hoàn chỉnh** như `„Ich habe eine Radtour gemacht.“`, không đọc bảng.

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung **2 chủ đề lọc mới** với đầy đủ **50 danh từ có mạo từ `der/die/das`, dạng số nhiều, nghĩa tiếng Việt và câu ví dụ khớp 100% với từng thẻ** (danh từ nào đã có ở bài trước thì **giữ thẻ cũ, không tạo trùng**; số lượng thẻ mới thực tế có thể ít hơn 50 — khi đó chỉ báo cáo số đã bỏ qua vì trùng):

#### Chủ đề A: `Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **der Wald** | die Wälder | rừng | Wir machen ein Picknick im Wald. | Chúng tôi dã ngoại trong rừng. |
| 2 | **der Berg** | die Berge | núi | Im Winter liegt auf dem Berg viel Schnee. | Vào mùa đông trên núi có nhiều tuyết. |
| 3 | **der Fluss** | die Flüsse | sông | Die Familie macht am Fluss ein Picknick. | Gia đình dã ngoại bên bờ sông. |
| 4 | **der See** | die Seen | hồ | Der See ist morgens ganz ruhig. | Buổi sáng hồ hoàn toàn yên tĩnh. |
| 5 | **der Strand** | die Strände | bãi biển | Die Kinder spielen am Strand. | Những đứa trẻ chơi ở bãi biển. |
| 6 | **der Bummel** | die Bummel | cuộc đi dạo (phố) | Nach dem Essen machen wir einen Bummel durch die Stadt. | Sau bữa ăn chúng tôi đi dạo quanh thành phố. |
| 7 | **der Urlaub** | die Urlaube | kỳ nghỉ | Mein Urlaub war leider zu kurz. | Kỳ nghỉ của tôi tiếc là quá ngắn. |
| 8 | **der Reiseführer** | die Reiseführer | sách hướng dẫn du lịch; hướng dẫn viên | Der Reiseführer hat viele Tipps für Wien. | Cuốn sách hướng dẫn có nhiều mẹo cho Wien. |
| 9 | **der Sonnenuntergang** | die Sonnenuntergänge | hoàng hôn | Am Meer ist der Sonnenuntergang besonders schön. | Bên biển hoàng hôn đặc biệt đẹp. |
| 10 | **der Ausflug** | die Ausflüge | chuyến đi chơi trong ngày | Am Sonntag machen wir einen Ausflug. | Chủ nhật chúng tôi đi chơi một chuyến. |
| 11 | **der Campingplatz** | die Campingplätze | khu cắm trại | Auf dem Campingplatz stehen viele Zelte. | Trên khu cắm trại có nhiều lều. |
| 12 | **die Altstadt** | die Altstädte | phố cổ | Die Altstadt von Hội An ist sehr schön. | Phố cổ Hội An rất đẹp. |
| 13 | **die Insel** | die Inseln | hòn đảo | Auf der Insel gibt es keine Autos. | Trên đảo không có ô tô. |
| 14 | **die Sonne** | die Sonnen | mặt trời | Die Sonne scheint den ganzen Tag. | Mặt trời chiếu sáng cả ngày. |
| 15 | **die Alpen** | *(nur Plural)* | dãy An-pơ (Alps) | Im Winter fahren viele Touristen in die Alpen. | Vào mùa đông nhiều khách du lịch đi lên dãy Alps. |
| 16 | **die Besichtigung** | die Besichtigungen | sự tham quan, buổi tham quan | Die Besichtigung des Schlosses dauert eine Stunde. | Buổi tham quan lâu đài kéo dài một giờ. |
| 17 | **die Radtour** | die Radtouren | chuyến đạp xe | Die Radtour war sehr anstrengend. | Chuyến đạp xe rất mệt. |
| 18 | **die Reise** | die Reisen | chuyến du lịch, chuyến đi | Die Reise nach Wien dauert vier Stunden. | Chuyến đi đến Wien mất bốn tiếng. |
| 19 | **die Landschaft** | die Landschaften | phong cảnh, cảnh quan | Die Landschaft in den Bergen ist wunderschön. | Phong cảnh trên núi tuyệt đẹp. |
| 20 | **die Küste** | die Küsten | bờ biển | Wir fahren mit dem Bus die Küste entlang. | Chúng tôi đi xe buýt dọc theo bờ biển. |
| 21 | **die Pause** | die Pausen | giờ nghỉ, sự nghỉ ngơi | Wir machen eine Pause am See. | Chúng tôi nghỉ một lát bên hồ. |
| 22 | **das Meer** | die Meere | biển | Das Meer ist heute sehr ruhig. | Hôm nay biển rất lặng. |
| 23 | **das Schloss** | die Schlösser | lâu đài, cung điện | Das Schloss steht auf einem Berg. | Lâu đài nằm trên một ngọn núi. |
| 24 | **das Reiseland** | die Reiseländer | quốc gia du lịch | Vietnam ist ein beliebtes Reiseland. | Việt Nam là một quốc gia du lịch được ưa chuộng. |
| 25 | **das Reiseziel** | die Reiseziele | điểm đến du lịch | Unser Reiseziel ist die Insel Cát Bà. | Điểm đến của chúng tôi là đảo Cát Bà. |

#### Chủ đề B: `Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 26 | **das Wetter** | *(nur Singular)* | thời tiết | Das Wetter ist heute wunderbar. | Hôm nay thời tiết tuyệt vời. |
| 27 | **das Essen** | die Essen | đồ ăn, bữa ăn | Das Essen im Hotel war sehr gut. | Đồ ăn ở khách sạn rất ngon. |
| 28 | **das Hotel** | die Hotels | khách sạn | Unser Hotel liegt direkt am Strand. | Khách sạn của chúng tôi nằm ngay cạnh bãi biển. |
| 29 | **das Dorf** | die Dörfer | làng | Mein Opa wohnt in einem kleinen Dorf. | Ông tôi sống trong một ngôi làng nhỏ. |
| 30 | **das Picknick** | die Picknicks | buổi dã ngoại ăn ngoài trời | Das Picknick am Fluss war schön. | Buổi dã ngoại bên sông thật đẹp. |
| 31 | **das Kloster** | die Klöster | tu viện | Das Kloster ist über fünfhundert Jahre alt. | Tu viện đã hơn năm trăm năm tuổi. |
| 32 | **das Zelt** | die Zelte | cái lều | Unser Zelt ist sehr klein. | Lều của chúng tôi rất nhỏ. |
| 33 | **das Foto** | die Fotos | bức ảnh | Auf dem Foto sieht man die ganze Familie. | Trong bức ảnh có thể thấy cả gia đình. |
| 34 | **das Flugzeug** | die Flugzeuge | máy bay | Das Flugzeug landet um zehn Uhr. | Máy bay hạ cánh lúc mười giờ. |
| 35 | **das Schiff** | die Schiffe | tàu thủy | Das Schiff fährt zur Insel. | Tàu thủy chạy ra đảo. |
| 36 | **das Zimmer** | die Zimmer | căn phòng | Das Zimmer hat einen Balkon. | Căn phòng có một ban công. |
| 37 | **das Souvenir** | die Souvenirs | quà lưu niệm | Ich kaufe ein Souvenir für meine Mutter. | Tôi mua một món quà lưu niệm cho mẹ. |
| 38 | **das Gepäck** | *(nur Singular)* | hành lý | Das Gepäck ist sehr schwer. | Hành lý rất nặng. |
| 39 | **das Frühstück** | die Frühstücke | bữa sáng | Das Frühstück gibt es von sieben bis zehn Uhr. | Bữa sáng có từ bảy đến mười giờ. |
| 40 | **der Koffer** | die Koffer | vali | Mein Koffer ist rot. | Vali của tôi màu đỏ. |
| 41 | **der Rucksack** | die Rucksäcke | ba lô | Im Rucksack sind Wasser und Obst. | Trong ba lô có nước và trái cây. |
| 42 | **der Zug** | die Züge | tàu hỏa | Der Zug nach München fährt um acht Uhr. | Chuyến tàu đi München chạy lúc tám giờ. |
| 43 | **der Reisepass** | die Reisepässe | hộ chiếu | Ohne Reisepass kann man nicht fliegen. | Không có hộ chiếu thì không thể bay. |
| 44 | **der Regen** | *(nur Singular)* | mưa | Der Regen hört am Abend auf. | Cơn mưa tạnh vào buổi tối. |
| 45 | **der Gast** | die Gäste | khách | Die Gäste frühstücken auf der Terrasse. | Các vị khách ăn sáng trên sân thượng. |
| 46 | **die Pension** | die Pensionen | nhà nghỉ (nhỏ) | Die Pension ist klein, aber gemütlich. | Nhà nghỉ nhỏ nhưng ấm cúng. |
| 47 | **die Jugendherberge** | die Jugendherbergen | nhà trọ thanh niên (hostel) | In der Jugendherberge schlafen viele junge Leute. | Trong nhà trọ thanh niên có nhiều người trẻ ngủ lại. |
| 48 | **die Fahrkarte** | die Fahrkarten | vé tàu / xe | Ich brauche eine Fahrkarte nach Hamburg. | Tôi cần một vé đi Hamburg. |
| 49 | **die Rechnung** | die Rechnungen | hóa đơn | Die Rechnung für das Zimmer ist hoch. | Hóa đơn tiền phòng khá cao. |
| 50 | **die Postkarte** | die Postkarten | bưu thiếp | Ich schreibe meiner Oma eine Postkarte. | Tôi viết một tấm bưu thiếp cho bà. |

> ✅ **Mẹo quy tắc giống hiển thị trên thẻ**: danh từ ghép lấy giống của từ cuối (`die Reise + das Land = das Reiseland`; `die Reise + das Ziel = das Reiseziel`; `die Reise + der Führer = der Reiseführer`; `die Sonne + der Untergang = der Sonnenuntergang`). Đuôi **`-ung`** luôn là **`die`** (`die Besichtigung`). Danh từ **chỉ số ít**: `das Wetter, das Gepäck, der Regen`. Danh từ **chỉ số nhiều**: `die Alpen, die Ferien`.

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 9: "URLAUB - DU LỊCH - PERFEKT & PRÄTERITUM"

Bài học thứ 10 trong danh sách Cấp độ A1 (`lesson_order = 10`):
* **Tiêu đề bài học**: `Bài 9: Du lịch - Perfekt & Präteritum (Quá khứ văn nói)` *(chủ đề trên bảng: "Ab in den Urlaub")*
* **Mô tả ngắn**: `Học từ vựng Thiên nhiên - Du lịch (der Strand, die Insel, das Reiseziel...), các cụm động từ đi với danh từ (eine Radtour machen, ein Schloss besichtigen...), cách kể và hỏi về kỳ nghỉ bằng Präteritum của sein/haben (war, waren, hatte); và đặc biệt làm chủ thì PERFEKT (haben/sein + Partizip II): công thức, vị trí động từ, 6 quy tắc tạo Partizip II, cách chọn haben hay sein và bảng động từ bất quy tắc.`
* **Cấu trúc bài**: Học phần 1 (Từ vựng) → 2 (Cụm từ) → 3 (Nói về kỳ nghỉ + Präteritum) → **4 (PERFEKT — phần trọng tâm, dài nhất)** → 5 (Đọc hiểu & phân tích văn bản) → 6 (Bảng tổng hợp) → 7 (Đặc tả sơ đồ SVG).

---

### HỌC PHẦN 1: TỪ VỰNG THIÊN NHIÊN & DU LỊCH (`DIE NATUR - DIE REISE`)

> 💡 **Cách đọc ký hiệu trên bảng giảng**: `r.` = **der**, `e.` = **die**, `s.` = **das**; trong ngoặc là **số nhiều** (`Pl.`); `(-)` nghĩa là số nhiều **giữ nguyên** hình thức (`der Reiseführer → die Reiseführer`); `(Sg.)` = chỉ có **số ít**; `(PL)` = chỉ có **số nhiều**.

#### 1.1. Bảng từ vựng chính (khớp bảng giảng) — phân theo 3 giống
| Giống Đực (<span style="color:#3b82f6">**`der`**</span>) | Giống Cái (<span style="color:#f43f5e">**`die`**</span>) | Giống Trung (<span style="color:#10b981">**`das`**</span>) |
| :--- | :--- | :--- |
| • **der Wald** *(Pl: die W<u>ä</u>lder)*: rừng<br>• **der Berg** *(Pl: die Berge)*: núi<br>• **der Fluss** *(Pl: die Fl<u>ü</u>sse)*: sông<br>• **der See** *(Pl: die Seen)*: hồ<br>• **der Strand** *(Pl: die Str<u>ä</u>nde)*: bãi biển<br>• **der Bummel** *(Pl: die Bummel)*: cuộc đi dạo<br>• **der Reiseführer** *(Pl: die Reiseführer)*: sách hướng dẫn du lịch (cũng là *hướng dẫn viên*)<br>• **der Urlaub** *(Pl: die Urlaube)*: kỳ nghỉ | • **die Altstadt** *(Pl: die Altst<u>ä</u>dte)*: phố cổ<br>• **die Insel** *(Pl: die Inseln)*: hòn đảo<br>• **die Sonne** *(Pl: die Sonnen)*: mặt trời<br>• **die Alpen** *(nur Plural)*: dãy An-pơ<br>• **die Besichtigung** *(Pl: die Besichtigungen)*: sự tham quan<br>• **die Radtour** *(Pl: die Radtouren)*: cuộc hành trình bằng xe đạp<br>• **die Reise** *(Pl: die Reisen)*: chuyến du lịch | • **das Meer** *(Pl: die Meere)*: biển<br>• **das Schloss** *(Pl: die Schl<u>ö</u>sser)*: lâu đài, cung điện<br>• **das Reiseland** *(Pl: die Reisel<u>ä</u>nder)*: đất nước du lịch<br>• **das Reiseziel** *(Pl: die Reiseziele)*: đích đến / điểm đến du lịch<br>• **das Wetter** *(nur Singular)*: thời tiết<br>• **das Essen** *(Pl: die Essen)*: đồ ăn<br>• **das Hotel** *(Pl: die Hotels)*: khách sạn |

> 🔎 **Mẹo nhớ giống (không học vẹt)**:
> * **`-ung` luôn là `die`**: `die Besichtigung` (từ động từ `besichtigen`). Tương tự `die Wanderung` (từ `wandern`), `die Übernachtung` (từ `übernachten`).
> * **Danh từ ghép lấy giống của từ cuối**: `die Reise` + `das Land` = **`das Reiseland`**; `die Reise` + `das Ziel` = **`das Reiseziel`**; `die Reise` + `der Führer` = **`der Reiseführer`**; `die Alt-` + `die Stadt` = **`die Altstadt`**.
> * **`der Urlaub`** (kỳ nghỉ của người đi làm) khác với **`die Ferien`** (kỳ nghỉ của học sinh, sinh viên — luôn số nhiều). *„Ich habe zwei Wochen Urlaub.“* — Tôi có hai tuần nghỉ phép. *„Die Kinder haben im Sommer Ferien.“* — Bọn trẻ nghỉ hè.
> * **Hai nghĩa của `der Reiseführer`**: *quyển sách hướng dẫn* và *người hướng dẫn du lịch*. Ngữ cảnh quyết định nghĩa.

#### 1.2. Bảng 7 động từ du lịch trên bảng giảng — kèm Perfekt *(học trước để dùng ở Học phần 4)*
| Động từ | Nghĩa | Loại | Perfekt (ngôi `er/sie/es`) | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- | :--- | :--- |
| **wandern** | đi bộ đường dài (trong rừng / núi) | quy tắc, `sein` | **ist gewandert** | *„Wir sind im Wald gewandert.“* — Chúng tôi đã đi bộ đường dài trong rừng. |
| **besichtigen** | tham quan | `be-` không tách | **hat besichtigt** | *„Er hat das Schloss besichtigt.“* — Anh ấy đã tham quan lâu đài. |
| **übernachten** | qua đêm, ngủ lại | `über-` không tách, gốc `-t` | **hat übernachtet** | *„Sie hat in einer Pension übernachtet.“* — Cô ấy đã ngủ lại trong một nhà nghỉ. |
| **probieren** | thử | `-ieren` | **hat probiert** | *„Ich habe die Suppe probiert.“* — Tôi đã thử món súp. |
| **zelten** | dựng lều, cắm trại | gốc `-t` → `-et` | **hat gezeltet** | *„Ihr habt am Fluss gezeltet.“* — Các bạn đã cắm trại bên sông. |
| **passieren** | xảy ra | `-ieren`, `sein` | **ist passiert** | *„Was ist passiert?“* — Chuyện gì đã xảy ra? |
| **anschauen** | nhìn ngắm, xem | tách `an-` | **hat angeschaut** | *„Wir haben die Fotos angeschaut.“* — Chúng tôi đã xem những bức ảnh. |

> ⚠️ **`besichtigen` ≠ `besuchen`**: `besichtigen` dùng cho **địa điểm / công trình** (lâu đài, thành phố, bảo tàng); `besuchen` dùng cho **người** (thăm bạn, thăm bà) và cũng dùng cho địa điểm (ghé thăm). *„Wir haben das Schloss besichtigt.“* / *„Wir haben Freunde besucht.“*

---

### HỌC PHẦN 2: CỤM ĐỘNG TỪ + DANH TỪ (`KOLLOKATIONEN`) — GHÉP ĐÚNG, ĐỪNG GHÉP BỪA

Trong tiếng Đức, mỗi danh từ có những động từ "đi cặp" tự nhiên (`Kollokationen`). Bảng giảng dạy ghép **4 động từ** `besichtigen – kaufen – machen – planen` với **8 danh từ**. Ghép đúng ngữ pháp thì nhiều, nhưng **ghép đúng ngữ cảnh du lịch** thì chỉ một số cụm:

#### 2.1. Bảng ma trận ghép từ (✔ = tự nhiên, ✘ = sai nghĩa hoặc kỳ quặc)
| Danh từ ↓ / Động từ → | **machen** | **planen** | **besichtigen** | **kaufen** |
| :--- | :---: | :---: | :---: | :---: |
| **eine Pause** *(nghỉ giải lao)* | ✔ eine Pause machen | ✘ | ✘ | ✘ |
| **eine Radtour** | ✔ eine Radtour machen | ✔ eine Radtour planen | ✘ | ✘ |
| **ein Picknick** | ✔ ein Picknick machen | ✔ ein Picknick planen | ✘ | ✘ |
| **ein Schloss** | ✘ | ✘ | ✔ ein Schloss besichtigen | ✘ *(không ai mua lâu đài khi đi du lịch!)* |
| **einen Reiseführer** | ✘ | ✘ | ✘ | ✔ einen Reiseführer kaufen |
| **Fotos** | ✔ Fotos machen | ✘ | ✘ | ✘ *(trừ khi mua ảnh in)* |
| **Ferien** | ✘ *(Ferien machen — ít dùng; nói `Urlaub machen`)* | ✔ Ferien planen | ✘ | ✘ |
| **eine Stadt** | ✘ | ✘ | ✔ eine Stadt besichtigen | ✘ |

> 📌 Lưu ý ngữ pháp: `eine Pause machen` = nghỉ giải lao; `Fotos machen` = chụp ảnh (người Đức **không** nói `Fotos nehmen`); `Urlaub machen` = đi nghỉ; `eine Reise machen` = thực hiện một chuyến đi.

#### 2.2. Mở rộng: 24 cụm động từ - danh từ du lịch thông dụng (⭐ học thêm, mỗi cụm có `🔊`)
| Cụm tiếng Đức (`🔊 de-DE`) | Nghĩa tiếng Việt | Cụm tiếng Đức (`🔊 de-DE`) | Nghĩa tiếng Việt |
| :--- | :--- | :--- | :--- |
| **Urlaub machen** | đi nghỉ | **eine Reise planen** | lên kế hoạch một chuyến đi |
| **eine Reise machen** | thực hiện một chuyến đi | **ein Zimmer buchen** | đặt một phòng |
| **einen Koffer packen** | đóng một chiếc vali | **eine Fahrkarte kaufen** | mua một tấm vé tàu/xe |
| **ein Souvenir kaufen** | mua một món quà lưu niệm | **eine Postkarte schreiben** | viết một tấm bưu thiếp |
| **einen Ausflug machen** | đi chơi một chuyến trong ngày | **einen Bummel machen** | đi dạo phố |
| **eine Wanderung machen** | thực hiện một chuyến đi bộ đường dài | **ein Zelt aufbauen** | dựng một cái lều |
| **die Altstadt besichtigen** | tham quan phố cổ | **ein Museum besuchen** | ghé thăm một bảo tàng |
| **ein Kloster besichtigen** | tham quan một tu viện | **die Rechnung bezahlen** | trả hóa đơn |
| **das Essen probieren** | thử món ăn | **die Sonne genießen** | tận hưởng ánh nắng |
| **in einer Pension übernachten** | ngủ lại trong nhà nghỉ | **im Zelt übernachten** | ngủ lại trong lều |
| **am Strand liegen** | nằm ở bãi biển | **im Meer baden** | tắm biển |
| **mit dem Zug fahren** | đi bằng tàu hỏa | **mit dem Flugzeug fliegen** | đi bằng máy bay |

---

### HỌC PHẦN 3: NÓI VỀ KỲ NGHỈ (`ÜBER URLAUB SPRECHEN`) & PRÄTERITUM CỦA `SEIN` / `HABEN`

#### 3.1. Ba câu hỏi - đáp quan trọng nhất (khớp bảng giảng, có mở rộng)
| Câu hỏi (`🔊 de-DE`) | Cách trả lời (`🔊 de-DE`) | Giải thích & Dịch |
| :--- | :--- | :--- |
| **`Wo waren Sie in Urlaub?`** *(Ngài đã đi nghỉ ở đâu?)*<br>`Wo warst du im Urlaub?` *(Bạn thì sao?)* | • *„Ich war **am** Do Son **Meer**.“*<br>• *„Ich war **in** Berlin / **in** Frankreich.“*<br>• *„Ich war **auf der** Cát Bà **Insel**.“* | **`Wo?` + Dativ** (chỉ vị trí đã ở). Chọn giới từ theo loại địa điểm (xem bảng 3.4). `Sie` = ngài/ông/bà (trang trọng), `du` = bạn (thân mật). |
| **`Wie war es?`** *(Nó như thế nào?)* | *„Es war **super / toll / schön / langweilig**.“* | `es` thay cho cả kỳ nghỉ. Tính từ cảm xúc đứng cuối câu: `super` (siêu), `toll` (tuyệt), `schön` (đẹp, hay), `langweilig` (chán). |
| **`Wie war das Wetter?`** *(Thời tiết thế nào?)*<br>`Wie war das Essen?` / `Wie war das Hotel?` | *„Das Wetter war **prima / gut / schlecht**.“*<br>*„Das Essen war **lecker**.“* / *„Das Hotel war **sauber**.“* | Hỏi bằng `Wie war + [das + danh từ]?`, đáp `Das ... war + tính từ.` Cả hai câu đều dùng **`Präteritum` của `sein`**. |

#### 3.2. Präteritum của `sein` — BẢNG CHIA BẮT BUỘC THUỘC LÒNG
| Ngôi | `sein` — Präteritum | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **ich** | **war** | *„Ich war letzten Sommer in Đà Lạt.“* — Mùa hè năm ngoái tôi đã ở Đà Lạt. |
| **du** | **warst** | *„Wo warst du gestern?“* — Hôm qua bạn đã ở đâu? |
| **er / sie / es** | **war** | *„Es war sehr schön.“* — Nó rất đẹp. |
| **wir** | **waren** | *„Wir waren zwei Wochen am Meer.“* — Chúng tôi đã ở biển hai tuần. |
| **ihr** | **wart** | *„Wart ihr schon in Wien?“* — Các bạn đã từng ở Wien chưa? |
| **sie / Sie** | **waren** | *„Wo waren Sie in Urlaub, Frau Müller?“* — Bà Müller, bà đã đi nghỉ ở đâu ạ? |

> 🔑 **Điểm đặc biệt**: Ngôi `ich` và `er/sie/es` **giống hệt nhau (`war`)**; ngôi `wir` và `sie/Sie` **giống hệt nhau (`waren`)**. Ngôi `du` có đuôi `-st` (`warst`), ngôi `ihr` có đuôi `-t` (`wart`).

#### 3.3. Präteritum của `haben` ⭐ (mở rộng)
| Ngôi | `haben` — Präteritum | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **ich** | **hatte** | *„Ich hatte im Urlaub viel Spaß.“* — Trong kỳ nghỉ tôi đã rất vui. |
| **du** | **hattest** | *„Hattest du schönes Wetter?“* — Bạn có thời tiết đẹp không? |
| **er / sie / es** | **hatte** | *„Das Hotel hatte einen kleinen Pool.“* — Khách sạn có một cái hồ bơi nhỏ. |
| **wir** | **hatten** | *„Wir hatten leider keine Zeit.“* — Tiếc là chúng tôi đã không có thời gian. |
| **ihr** | **hattet** | *„Hattet ihr Hunger?“* — Các bạn đã đói chưa? |
| **sie / Sie** | **hatten** | *„Die Gäste hatten ein großes Zimmer.“* — Các vị khách có một căn phòng lớn. |

> 💬 **Vì sao `sein` và `haben` dùng Präteritum cả khi nói chuyện?** Hai động từ này rất ngắn và rất thông dụng. Người Đức nói *„Ich war in Berlin.“* chứ hiếm khi nói *„Ich bin in Berlin gewesen.“* Quy tắc thực hành: **`sein`, `haben` (và động từ khuyết thiếu) → dùng Präteritum; hầu hết các động từ còn lại → dùng Perfekt khi nói** (xem Học phần 4, mục 4.7).

#### 3.4. Chọn giới từ chỉ địa điểm cho câu `Wo warst du?` (`Wo? + Dativ`)
| Loại địa điểm | Giới từ + Mạo từ | Ví dụ (`🔊 de-DE`) | Dịch |
| :--- | :--- | :--- | :--- |
| Thành phố, đa số quốc gia (không mạo từ) | **in** + (không mạo từ) | *„Ich war in Berlin / in Frankreich / in Vietnam.“* | Tôi đã ở Berlin / Pháp / Việt Nam. |
| Quốc gia có mạo từ | **in der** (die) / **in den** (Pl.) | *„Wir waren in der Schweiz / in der Türkei / in den USA.“* | Chúng tôi đã ở Thụy Sĩ / Thổ Nhĩ Kỳ / Mỹ. |
| Biển, hồ, sông, bãi biển (nơi nằm sát mép nước) | **an** + Dativ → **am** (der/das), **an der** (die) | *„Ich war am Meer / am See / am Strand / an der Küste.“* | Tôi đã ở biển / hồ / bãi biển / bờ biển. |
| Hòn đảo | **auf** + Dativ → **auf der** (die Insel) | *„Sie waren auf der Insel Phú Quốc.“* | Họ đã ở trên đảo Phú Quốc. |
| Núi, rừng, dãy núi | **in** + Dativ → **in den Bergen / im Wald / in den Alpen** | *„Wir waren im Wald und in den Bergen.“* | Chúng tôi đã ở trong rừng và trên núi. |
| Nhà người quen | **bei** + Dativ | *„Ich war bei Freunden in Hamburg.“* | Tôi đã ở nhà bạn bè tại Hamburg. |
| Ở nhà | **zu Hause** | *„Im Sommer war ich zu Hause.“* | Mùa hè tôi đã ở nhà. |

> 🔗 **Nối với Bài 8**: Bài 8 dùng `Wohin? → zum / zur / in den / ins` (đi *tới*), còn Bài 9 dùng `Wo? → am / im / auf der / in der` (đã *ở*). Cùng là địa điểm nhưng khác câu hỏi nên khác giới từ.

#### 3.5. Tính từ miêu tả kỳ nghỉ & thời tiết (⭐ mở rộng, mỗi từ có `🔊`)
| Nhóm | Từ & Nghĩa |
| :--- | :--- |
| **Cảm nhận về kỳ nghỉ** | `super` (siêu), `toll` (tuyệt), `schön` (đẹp, hay), `wunderbar` (tuyệt diệu), `prima` (rất tốt), `gut` (tốt), `schlecht` (tệ), `langweilig` (chán), `anstrengend` (mệt mỏi), `teuer` (đắt), `billig` (rẻ) |
| **Về khách sạn / đồ ăn** | `sauber` (sạch), `gemütlich` (ấm cúng), `klein` (nhỏ), `groß` (lớn), `lecker` (ngon), `scharf` (cay) |
| **Thời tiết** | `sonnig` (nắng), `warm` (ấm), `heiß` (nóng), `kalt` (lạnh), `windig` (có gió), `regnerisch` (nhiều mưa), `bewölkt` (nhiều mây) |
| **Động từ thời tiết (Perfekt, ngôi `es`)** | `es hat geregnet` (trời đã mưa), `es hat geschneit` (tuyết đã rơi), `die Sonne hat geschienen` (mặt trời đã chiếu sáng) |

#### 3.6. Bốn mẫu hội thoại hỏi đáp về kỳ nghỉ (`🔊 de-DE` từng câu — kết hợp Präteritum & Perfekt)
> **Hội thoại 1 — Ở đâu và như thế nào?**
> * A: *„Wo warst du im Urlaub, Linh?“* — Linh ơi, bạn đã đi nghỉ ở đâu?
> * B: *„Ich war mit meiner Familie auf der Insel Phú Quốc.“* — Tôi đã ở trên đảo Phú Quốc cùng gia đình.
> * A: *„Wie war es?“* — Thế nào?
> * B: *„Es war toll! Das Wetter war prima und das Essen war sehr lecker.“* — Tuyệt lắm! Thời tiết rất đẹp và đồ ăn rất ngon.
>
> **Hội thoại 2 — Đã làm gì?**
> * A: *„Was habt ihr dort gemacht?“* — Các bạn đã làm gì ở đó?
> * B: *„Wir sind jeden Tag im Meer geschwommen und haben viele Fotos gemacht.“* — Ngày nào chúng tôi cũng bơi biển và chụp nhiều ảnh.
>
> **Hội thoại 3 — Đi bằng gì, ở đâu?**
> * A: *„Wie seid ihr gereist?“* — Các bạn đã đi bằng gì?
> * B: *„Wir sind mit dem Flugzeug geflogen. Dann haben wir in einem kleinen Hotel übernachtet.“* — Chúng tôi đã đi máy bay. Sau đó chúng tôi đã ở một khách sạn nhỏ.
>
> **Hội thoại 4 — Chuyện không may**
> * A: *„Hattest du schönes Wetter in Hạ Long?“* — Bạn có thời tiết đẹp ở Hạ Long không?
> * B: *„Nein, leider nicht. Es hat zwei Tage geregnet. Aber die Landschaft war wunderschön.“* — Không, tiếc là không. Trời đã mưa hai ngày. Nhưng phong cảnh thì tuyệt đẹp.

---

### HỌC PHẦN 4: ⭐ PERFEKT — THÌ QUÁ KHỨ CỦA VĂN NÓI (PHẦN TRỌNG TÂM, CẦN HỌC KỸ NHẤT) ⭐

> 🧭 **Bản đồ phần này**: 4.1 Khái niệm → 4.2 Công thức & vị trí động từ → 4.3 Chia `haben/sein` → **4.4 Partizip II: 6 quy tắc** → **4.5 Động từ bất quy tắc** → **4.6 Chọn `haben` hay `sein`** → 4.7 Perfekt hay Präteritum? → 4.8 Từ chỉ thời gian → 4.9 Mười ba lỗi thường gặp → 4.10 Quy trình 5 bước.

#### 4.1. Perfekt là gì, dùng khi nào? (`Was ist das Perfekt?`)
* **Ý nghĩa**: diễn tả **hành động đã xảy ra trong quá khứ** (≈ *"đã"*, *"đã … rồi"* trong tiếng Việt).
* **Cách dùng**: là thì quá khứ **thường dùng trong văn nói** (hội thoại, kể chuyện với bạn bè, tin nhắn, hỏi thăm hằng ngày). Trong **văn viết** (tiểu thuyết, báo chí, tường thuật) người Đức hay dùng `Präteritum`.
* **Ví dụ so sánh ngắn**:
  * Hiện tại: *„Ich mache Hausaufgaben.“* — Tôi (đang) làm bài tập.
  * Perfekt: *„Ich habe Hausaufgaben gemacht.“* — Tôi **đã** làm bài tập.
* **Đặc điểm hình thức**: Perfekt là **thì ghép gồm 2 phần tách xa nhau** — trợ động từ (`haben` / `sein`) đứng ở **vị trí thứ 2**, còn `Partizip II` (phân từ 2) đứng **cuối câu**.

#### 4.2. Công thức & vị trí động từ trong câu (`Satzklammer` — "khung kẹp câu")
> ### 📐 CÔNG THỨC: &nbsp; **`S + haben / sein (chia theo S) + ……… + Partizip II`**
> * **Vị trí 2** = `haben / sein` đã chia theo chủ ngữ. **Cuối câu** = `Partizip II`. **Ở giữa** = mọi thông tin khác (thời gian, địa điểm, tân ngữ...).
> * Hình dung như một **cặp ngoặc**: `haben/sein` là ngoặc mở, `Partizip II` là ngoặc đóng — phần còn lại nằm **kẹp ở giữa** (sơ đồ **V1**).

| Loại câu | Cấu trúc | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **Câu khẳng định** | S + **haben/sein** + [bổ ngữ] + **Partizip II** | *„Ich **habe** Hausaufgaben **gemacht**.“* — Tôi đã làm bài tập.<br>*„Wir **haben** gestern ein Schloss **besichtigt**.“* — Hôm qua chúng tôi đã tham quan một lâu đài. |
| **Đảo ngữ (trạng từ thời gian đứng đầu)** | [Thời gian] + **haben/sein** + S + … + **Partizip II** | *„Gestern **habe** ich Hausaufgaben **gemacht**.“* — Hôm qua tôi đã làm bài tập.<br>*„Am Wochenende **sind** wir nach Hamburg **gefahren**.“* — Cuối tuần chúng tôi đã đi Hamburg. *(Động từ trợ vẫn ở vị trí 2!)* |
| **Câu hỏi Ja/Nein** | **Haben/Sein** + S + … + **Partizip II**? | *„**Hast** du die Fotos **gemacht**?“* — Bạn đã chụp ảnh chưa?<br>*„**Seid** ihr mit dem Zug **gefahren**?“* — Các bạn đã đi bằng tàu hỏa phải không? |
| **Câu hỏi W-Frage** | W-Wort + **haben/sein** + S + … + **Partizip II**? | *„Was **hast** du im Urlaub **gemacht**?“* — Bạn đã làm gì trong kỳ nghỉ?<br>*„Wohin **bist** du **gefahren**?“* — Bạn đã đi đâu? |
| **Phủ định với `nicht`** | `nicht` đứng **trước Partizip II** (phủ định cả hành động) hoặc **trước bổ ngữ** chỉ hướng / nơi chốn | *„Ich **habe** das Schloss **nicht** **besichtigt**.“* — Tôi đã không tham quan lâu đài.<br>*„Ich **bin** gestern **nicht** zur Schule **gegangen**.“* — Hôm qua tôi đã không đi học. *(khớp bảng giảng)* |
| **Phủ định với `kein`** | `kein-` thay cho `ein-` / danh từ không mạo từ | *„Wir **haben** keine Fotos **gemacht**.“* — Chúng tôi đã không chụp ảnh nào. |
| **Hai hành động nối bằng `und`** | Trợ động từ chỉ cần **1 lần**, hai Partizip II đứng cuối | *„Wir **haben** viel **gegessen** und **getrunken**.“* — Chúng tôi đã ăn và uống nhiều. |
| **Động từ tách** | Tiền tố **không** tách ra cuối câu như Präsens; nằm **trong Partizip II** | Präsens: *„Ich kaufe auf dem Markt **ein**.“*<br>Perfekt: *„Ich **habe** auf dem Markt **eingekauft**.“* — Tôi đã mua sắm ở chợ. |

> ❗ **Trong tiếng Việt chỉ cần thêm "đã", nhưng tiếng Đức thì phải ĐỔI CẤU TRÚC CÂU**: `Ich mache` (1 từ) → `Ich habe … gemacht` (2 từ, tách xa nhau). Quên Partizip ở cuối câu là lỗi số 1 của người mới học.

#### 4.3. Chia trợ động từ `haben` và `sein` ở Präsens (nền tảng của Perfekt)
| Ngôi | **haben** | **sein** |
| :--- | :--- | :--- |
| **ich** | habe | bin |
| **du** | hast | bist |
| **er / sie / es** | hat | ist |
| **wir** | haben | sind |
| **ihr** | habt | seid |
| **sie / Sie** | haben | sind |

* *Ví dụ chia đầy đủ với `machen` (`haben`)*: ich **habe** gemacht · du **hast** gemacht · er/sie/es **hat** gemacht · wir **haben** gemacht · ihr **habt** gemacht · sie/Sie **haben** gemacht.
* *Ví dụ chia đầy đủ với `fahren` (`sein`)*: ich **bin** gefahren · du **bist** gefahren · er/sie/es **ist** gefahren · wir **sind** gefahren · ihr **seid** gefahren · sie/Sie **sind** gefahren.
* ⚠️ **Chỉ trợ động từ thay đổi theo ngôi; `Partizip II` luôn giữ nguyên** cho mọi ngôi (`gemacht` cho cả `ich`, `du`, `wir`...).

#### 4.4. ⭐ PARTIZIP II — 6 QUY TẮC TẠO PHÂN TỪ 2 (PHẦN KHÓ NHẤT, HỌC THEO THỨ TỰ)
> 🔑 **Hai câu hỏi "chẩn đoán" cho mọi động từ**: **(1)** Động từ này **có tiền tố không?** (tách được / không tách được) → **(2)** Động từ này **có quy tắc hay bất quy tắc?** Kết quả quyết định bạn dùng quy tắc nào dưới đây (sơ đồ **V2**).

| # | Nhóm động từ | Công thức Partizip II | Ví dụ (`🔊 de-DE`) |
| :-: | :--- | :--- | :--- |
| **1** | **Động từ có quy tắc** *(bảng giảng)* | **`ge` + gốc động từ + `t`** *(bỏ đuôi `-en`)* | `machen → **ge**mach**t**` (đã làm)<br>`hören → **ge**hör**t**` (đã nghe)<br>`kaufen → **ge**kauf**t**` · `spielen → **ge**spiel**t**` · `lernen → **ge**lern**t**` · `wohnen → **ge**wohn**t**` · `planen → **ge**plan**t**` |
| **2** | **Gốc động từ kết thúc bằng `-t` hoặc `-d`** *(bảng giảng)* — và vài gốc khó đọc như `-gn`, `-ffn`, `-chn` | **`ge` + gốc + `et`** *(thêm `e` để dễ phát âm)* | `arbeiten → **ge**arbeit**et**` (đã làm việc)<br>`warten → **ge**wart**et**` · `baden → **ge**bad**et**` · `zelten → **ge**zelt**et**` · `kosten → **ge**kost**et**` · `antworten → **ge**antwort**et**`<br>`regnen → **ge**regn**et**` · `öffnen → **ge**öffn**et**` · `zeichnen → **ge**zeichn**et**` |
| **3** | **Động từ đuôi `-ieren`** *(bảng giảng)* | **KHÔNG có `ge-`**: gốc + `t` | `notieren → notier**t**` (đã ghi chú)<br>`fotografieren → fotografier**t**` · `studieren → studier**t**` · `probieren → probier**t**` · `telefonieren → telefonier**t**` · `reservieren → reservier**t**` · `passieren → passier**t**` |
| **4** | **Động từ có tiền tố KHÔNG tách** (`be-, ge-, er-, ver-, zer-, ent-, emp-, miss-` và `über-` ở một số từ như `übernachten`) *(bảng giảng)* | **KHÔNG có `ge-`**: tiền tố + gốc + `(e)t` | `bezahlen → bezahl**t**` (đã trả tiền)<br>`besuchen → besucht` · `besichtigen → besichtigt` · `erreichen → erreicht` · `erleben → erlebt` · `erzählen → erzählt` · `verkaufen → verkauft` · `entdecken → entdeckt`<br>`übernachten → übernacht**et**` *(gốc `-t` nên thêm `-et`)* |
| **5** | **Động từ có tiền tố TÁCH được** (`ein-, an-, aus-, auf-, ab-, mit-, zu-, vor-, nach-, zurück-, weg-, los-, vorbei-, fern-...`) *(bảng giảng)* | **tiền tố + `ge` + gốc + `(e)t`** *(`ge` chèn vào GIỮA tiền tố và gốc)* | `einkaufen → **ein**ge**kauf**t` (đã mua sắm)<br>`anschauen → angeschaut` · `aufräumen → aufgeräumt` · `zuhören → zugehört` · `abholen → abgeholt` · `aufwachen → aufgewacht` |
| **6** | **Động từ bất quy tắc** (`starke Verben`) — *học thuộc* | **`ge` + gốc (thường đổi nguyên âm) + `en`** | `gehen → **ge**gang**en**` · `trinken → **ge**trunk**en**` · `schreiben → **ge**schrieb**en**` · `sprechen → **ge**sproch**en**` *(xem bảng 4.5)* |
| **6b** | **Động từ hỗn hợp** (`gemischte Verben`): đuôi `-t` như có quy tắc **nhưng đổi gốc** | **`ge` + gốc đổi + `t`** | `bringen → **ge**brach**t**` · `denken → **ge**dach**t**` · `wissen → **ge**wuss**t**` · `kennen → **ge**kann**t**` · `nennen → **ge**nann**t**` |

> 🎧 **Mẹo "nhấn trọng âm" để biết tiền tố tách hay không tách** *(rất hữu ích cho người Việt)*:
> * Tiền tố **được nhấn mạnh khi đọc** → **tách được** → nhóm 5: **EINkaufen, ANschauen, AUFräumen, ABholen** *(phần viết hoa là âm tiết được nhấn)*.
> * Tiền tố **không được nhấn** (nhấn rơi vào gốc) → **không tách** → nhóm 4: **beSUchen, beZAHlen, erREIchen, überNACHten** *(phần viết hoa là âm tiết được nhấn)*.

> ➕ **Động từ vừa tách vừa có `-ieren`** → vẫn **không có `ge-`**: `ausprobieren → ausprobiert`, `anprobieren → anprobiert`.
> ➕ **Động từ không tách nhưng bất quy tắc** → cũng **không có `ge-`**: `bekommen → bekommen`, `verstehen → verstanden`, `vergessen → vergessen`, `verlieren → verloren`, `beginnen → begonnen`, `gewinnen → gewonnen`, `empfehlen → empfohlen`.
> ➕ **Động từ vừa tách vừa bất quy tắc** → `ge` chèn giữa: `anrufen → angerufen`, `einladen → eingeladen`, `mitnehmen → mitgenommen`, `aufstehen → aufgestanden`, `einsteigen → eingestiegen`, `ankommen → angekommen`.

##### 4.4.1. Bảng luyện nhanh: nhìn động từ → viết Partizip II (kèm lý do)
| Infinitiv | Nghĩa | Nhóm | Partizip II | Vì sao? |
| :--- | :--- | :-: | :--- | :--- |
| **machen** | làm | 1 | **gemacht** | `ge` + `mach` + `t` |
| **arbeiten** | làm việc | 2 | **gearbeitet** | gốc `arbeit` đuôi `-t` → thêm `-et` |
| **warten** | chờ | 2 | **gewartet** | gốc `wart` đuôi `-t` → `-et` |
| **baden** | tắm | 2 | **gebadet** | gốc `bad` đuôi `-d` → `-et` |
| **regnen** | mưa | 2 | **geregnet** | gốc `regn` khó đọc → `-et` |
| **studieren** | học đại học | 3 | **studiert** | đuôi `-ieren` → không `ge-` |
| **fotografieren** | chụp ảnh | 3 | **fotografiert** | đuôi `-ieren` → không `ge-` |
| **besuchen** | thăm | 4 | **besucht** | tiền tố `be-` không tách → không `ge-` |
| **bezahlen** | trả tiền | 4 | **bezahlt** | tiền tố `be-` không tách |
| **erreichen** | đến được | 4 | **erreicht** | tiền tố `er-` không tách |
| **übernachten** | qua đêm | 4 | **übernachtet** | tiền tố `über-` không tách + gốc `-t` → `-et` |
| **einkaufen** | mua sắm | 5 | **eingekauft** | tiền tố `ein-` tách → `ein` + `ge` + `kauf` + `t` |
| **anschauen** | ngắm, xem | 5 | **angeschaut** | `an` + `ge` + `schau` + `t` |
| **gehen** | đi bộ | 6 | **gegangen** | bất quy tắc |
| **bringen** | mang | 6b | **gebracht** | hỗn hợp |

#### 4.5. ⭐ ĐỘNG TỪ BẤT QUY TẮC & HỖN HỢP — BẢNG TỔNG HỢP (HỌC THUỘC)
> 🧠 **Mọi động từ bất quy tắc phải học thuộc 3 thông tin cùng lúc**: **Infinitiv — trợ động từ (`hat`/`ist`) — Partizip II**. Ví dụ không học riêng `gegangen` mà học cả cụm **`gehen → ist gegangen`**.

##### 4.5.1. Bảng A: Nhóm dùng **`sein`** *(khớp bảng giảng — chuyển động đổi vị trí)*
| Infinitiv | Nghĩa (bảng giảng) | Perfekt (ngôi `er/sie/es`) | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- | :--- |
| **bleiben** | ở lại | **ist geblieben** | *„Sie ist zu Hause geblieben.“* — Cô ấy đã ở nhà. |
| **fahren** | đi (bằng phương tiện) | **ist gefahren** | *„Er ist mit dem Bus nach Hue gefahren.“* — Anh ấy đã đi xe buýt đến Huế. |
| **fallen** | rơi | **ist gefallen** | *„Das Handy ist ins Wasser gefallen.“* — Chiếc điện thoại đã rơi xuống nước. |
| **fliegen** | bay | **ist geflogen** | *„Wir sind nach Seoul geflogen.“* — Chúng tôi đã bay đến Seoul. |
| **gehen** | đi bộ | **ist gegangen** | *„Ich bin gestern nicht zur Schule gegangen.“* — Hôm qua tôi đã không đi học. *(câu trên bảng)* |
| **kommen** | đến | **ist gekommen** | *„Der Gast ist spät gekommen.“* — Vị khách đã đến muộn. |
| **laufen** | chạy, đi bộ | **ist gelaufen** | *„Wir sind zum Strand gelaufen.“* — Chúng tôi đã chạy ra bãi biển. |
| **wachsen** | trưởng thành, lớn lên | **ist gewachsen** | *„Der Baum ist sehr schnell gewachsen.“* — Cái cây đã lớn rất nhanh. |
| **ziehen** *(= chuyển nhà)* | chuyển nơi ở | **ist gezogen** | *„Meine Tante ist nach Berlin gezogen.“* — Dì tôi đã chuyển đến Berlin. |

> ⚠️ **`ziehen` có 2 nghĩa với 2 trợ động từ khác nhau** *(bảng giảng chỉ ghi nghĩa "kéo")*: **`ziehen` = kéo, lôi → `hat gezogen`** (*„Er hat den Koffer gezogen.“* — Anh ấy đã kéo vali) | **`ziehen` = chuyển nhà → `ist gezogen`** (*„Wir sind nach Köln gezogen.“*). Cả hai đều có Partizip II là `gezogen`.

##### 4.5.2. Bảng B: Nhóm dùng **`haben`** *(khớp bảng giảng)*
| Infinitiv | Nghĩa (bảng giảng) | Perfekt | Infinitiv | Nghĩa (bảng giảng) | Perfekt |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **bringen** *(hỗn hợp)* | mang | hat **gebracht** | **rufen** | gọi | hat **gerufen** |
| **denken** *(hỗn hợp)* | nghĩ | hat **gedacht** | **schlafen** | ngủ | hat **geschlafen** |
| **essen** | ăn | hat **gegessen** | **schreiben** | viết | hat **geschrieben** |
| **finden** | tìm thấy | hat **gefunden** | **sehen** | nhìn, xem | hat **gesehen** |
| **geben** | đưa, cho | hat **gegeben** | **singen** | hát | hat **gesungen** |
| **helfen** | giúp đỡ | hat **geholfen** | **sprechen** | nói | hat **gesprochen** |
| **lesen** | đọc | hat **gelesen** | **tragen** | mang, vác, mặc | hat **getragen** |
| **liegen** | nằm | hat **gelegen** *(miền Bắc)* | **treffen** | gặp | hat **getroffen** |
| **nehmen** | dùng, lấy | hat **genommen** | **trinken** | uống | hat **getrunken** |
| | | | **wissen** *(hỗn hợp)* | biết | hat **gewusst** |

##### 4.5.3. Bảng C (⭐ mở rộng): thêm 40 động từ bất quy tắc thông dụng cho kỳ nghỉ
| Nhóm | Infinitiv → Perfekt |
| :--- | :--- |
| **`sein` — di chuyển** | `schwimmen → ist geschwommen` · `steigen → ist gestiegen` · `rennen → ist gerannt` *(hỗn hợp)* · `reisen → ist gereist` *(có quy tắc)* · `wandern → ist gewandert` *(có quy tắc)* |
| **`sein` — động từ tách** | `ankommen → ist angekommen` (đến nơi) · `abfahren → ist abgefahren` (khởi hành) · `aussteigen → ist ausgestiegen` (xuống xe) · `einsteigen → ist eingestiegen` (lên xe) · `umsteigen → ist umgestiegen` (đổi tàu) · `mitkommen → ist mitgekommen` (đi cùng) · `zurückkommen → ist zurückgekommen` (quay về) · `vorbeigehen → ist vorbeigegangen` (đi ngang qua) · `abbiegen → ist abgebogen` (rẽ) · `abfliegen → ist abgeflogen` (cất cánh) |
| **`sein` — đổi trạng thái** | `einschlafen → ist eingeschlafen` (ngủ thiếp đi) · `aufwachen → ist aufgewacht` (thức dậy) · `aufstehen → ist aufgestanden` (đứng dậy, dậy) · `sterben → ist gestorben` (chết) · `schmelzen → ist geschmolzen` (tan chảy) · `gefrieren → ist gefroren` (đóng băng) · `passieren → ist passiert` (xảy ra) · `werden → ist geworden` (trở thành) · `sein → ist gewesen` (đã là) |
| **`haben` — bất quy tắc** | `stehen → hat gestanden` · `sitzen → hat gesessen` · `scheinen → hat geschienen` (chiếu sáng) · `schließen → hat geschlossen` · `halten → hat gehalten` · `ziehen (kéo) → hat gezogen` |
| **`haben` — tiền tố không tách** | `bekommen → hat bekommen` (nhận được) · `verstehen → hat verstanden` · `vergessen → hat vergessen` · `verlieren → hat verloren` · `beginnen → hat begonnen` · `gewinnen → hat gewonnen` · `empfehlen → hat empfohlen` |
| **`haben` — động từ tách** | `anrufen → hat angerufen` · `einladen → hat eingeladen` · `mitnehmen → hat mitgenommen` |
| **`haben` — hỗn hợp** | `kennen → hat gekannt` · `nennen → hat genannt` · `mitbringen → hat mitgebracht` · `verbringen → hat verbracht` (trải qua [thời gian]) |

##### 4.5.4. ⭐ Mẹo gom nhóm theo kiểu đổi nguyên âm (để dễ nhớ, không bắt buộc)
| Kiểu biến đổi | Các động từ cùng kiểu |
| :--- | :--- |
| **Nguyên âm KHÔNG đổi** (`ge` + nguyên mẫu bỏ `-en`/… + `en`) | `fahren → gefahren` · `schlafen → geschlafen` · `tragen → getragen` · `laufen → gelaufen` · `rufen → gerufen` · `lesen → gelesen` · `essen → gegessen` · `sehen → gesehen` · `geben → gegeben` · `liegen → gelegen` · `kommen → gekommen` · `fallen → gefallen` · `halten → gehalten` · `wachsen → gewachsen` |
| **`ei → ie`** | `schreiben → geschrieben` · `bleiben → geblieben` · `steigen → gestiegen` |
| **`i → u`** | `trinken → getrunken` · `singen → gesungen` · `finden → gefunden` |
| **`e → o`** | `sprechen → gesprochen` · `nehmen → genommen` · `helfen → geholfen` · `treffen → getroffen` · `empfehlen → empfohlen` |
| **`ie → o`** | `fliegen → geflogen` · `ziehen → gezogen` · `verlieren → verloren` |
| **Đổi hẳn** | `gehen → gegangen` · `stehen → gestanden` · `sitzen → gesessen` · `schwimmen → geschwommen` · `sterben → gestorben` |
| **Hỗn hợp (`-t` + đổi gốc)** | `bringen → gebracht` · `denken → gedacht` · `wissen → gewusst` · `kennen → gekannt` · `nennen → genannt` · `rennen → gerannt` |

#### 4.6. ⭐ CHỌN TRỢ ĐỘNG TỪ: `SEIN` HAY `HABEN`? *(bảng giảng + mở rộng)*
##### 4.6.1. Quy tắc cốt lõi (khớp bảng giảng)
> * **Dùng `sein`** khi động từ là:
>   1. **Động từ chỉ sự CHUYỂN ĐỘNG làm thay đổi VỊ TRÍ** (đi từ nơi này đến nơi khác): `gehen` (đi bộ), `fahren` (đi phương tiện), `kommen` (đến), `fliegen` (bay), `laufen`, `reisen`, `wandern`, `ankommen`, `abfahren`...
>   2. **Động từ chỉ sự THAY ĐỔI TRẠNG THÁI** (từ trạng thái này sang trạng thái khác): `einschlafen` (ngủ thiếp đi), `aufwachen` (thức dậy), `schmelzen` (tan chảy), `gefrieren` (đóng băng), `sterben`, `passieren`...
>   3. **Ba động từ đặc biệt**: **`sein`, `bleiben`, `werden`**.
> * **Dùng `haben`** cho **tất cả các trường hợp còn lại** — nhất là động từ **có tân ngữ `Akkusativ`** (`machen`, `kaufen`, `besichtigen`, `essen`, `lesen`, `schreiben`...) và động từ chỉ **hoạt động / trạng thái không đổi vị trí** (`schlafen`, `wohnen`, `arbeiten`, `regnen`, `scheinen`...).

##### 4.6.2. Bảng đối chiếu thực tế (`🔊 de-DE`)
| Kiểu động từ | Trợ động từ | Ví dụ (`🔊 de-DE`) | Dịch |
| :--- | :---: | :--- | :--- |
| Di chuyển đổi vị trí | **sein** | *„Wir **sind** nach Wien **gefahren**.“* | Chúng tôi đã đi tới Wien. |
| Đổi trạng thái | **sein** | *„Das Baby **ist** im Auto **eingeschlafen**.“* | Em bé đã ngủ thiếp đi trong xe. |
| `sein` / `bleiben` / `werden` | **sein** | *„Ich **bin** eine Woche in Bonn **geblieben**.“* | Tôi đã ở lại Bonn một tuần. |
| Có tân ngữ Akkusativ | **haben** | *„Sie **hat** ein Foto **gemacht**.“* | Cô ấy đã chụp một tấm ảnh. |
| Hoạt động tại chỗ | **haben** | *„Er **hat** neun Stunden **geschlafen**.“* | Anh ấy đã ngủ chín tiếng. |
| Thời tiết | **haben** | *„Es **hat** gestern **geregnet**.“* | Hôm qua trời đã mưa. |

##### 4.6.3. Các trường hợp đặc biệt cần nhớ ⭐
| # | Trường hợp | Giải thích & Ví dụ |
| :-: | :--- | :--- |
| 1 | **`schlafen` ≠ `einschlafen`** | `schlafen` = *đang ngủ (trạng thái kéo dài)* → **`hat geschlafen`**; `einschlafen` = *chìm vào giấc ngủ (đổi trạng thái)* → **`ist eingeschlafen`**. |
| 2 | **`fahren / fliegen / schwimmen` có tân ngữ** | Chỉ **di chuyển** → `sein` (*„Ich bin nach Hue gefahren.“*). Nếu **lái / điều khiển cái gì** (tân ngữ Akkusativ) → `haben` (*„Ich habe das Auto gefahren.“* — Tôi đã lái chiếc xe). |
| 3 | **`liegen`, `sitzen`, `stehen`** | Chuẩn miền Bắc Đức dùng **`haben`** (*„Ich habe am Strand gelegen.“*). Nam Đức / Áo / Thụy Sĩ dùng `sein`. Ở A1 học **`haben`**. |
| 4 | **`gefallen` (làm hài lòng, được ưa thích) ≠ `fallen` (rơi)** | `fallen → ist gefallen` (rơi). Còn động từ `gefallen` (nguyên mẫu và Partizip II viết giống nhau) → `hat gefallen`: *„Das Hotel hat mir gefallen.“* — Khách sạn đã làm tôi hài lòng. *(Chỉ cần nhận biết; không dùng trong bài tập.)* |
| 5 | **`passieren` (xảy ra)** | Luôn **`ist passiert`**: *„Was ist passiert?“* |
| 6 | **`reisen`, `wandern`** | Có quy tắc nhưng vì là **di chuyển** nên dùng **`sein`**: *`ist gereist`, `ist gewandert`*. |
| 7 | **`ziehen`** | `ziehen` = *kéo* → `hat gezogen`; `ziehen` = *chuyển nhà* → `ist gezogen` (xem 4.5.1). |

##### 4.6.4. Cây quyết định 4 câu hỏi (sơ đồ **V3**)
1. Động từ là `sein`, `bleiben` hoặc `werden`? → **Có → `sein`**.
2. Có chuyển động đổi vị trí (từ A đến B)? → **Có → `sein`**.
3. Có đổi trạng thái (ngủ thiếp đi, tan chảy, xảy ra...)? → **Có → `sein`**.
4. Còn lại → **`haben`**.

#### 4.7. PERFEKT hay PRÄTERITUM? (`Wann benutze ich welche Zeitform?`)
| Tiêu chí | **Perfekt** | **Präteritum** |
| :--- | :--- | :--- |
| **Văn phong** | Nói, tin nhắn, thư từ thân mật | Viết: truyện, báo, tường thuật, sách |
| **Hình thức** | `haben/sein` + `Partizip II` (2 phần) | Một từ đã chia (`ich war`, `ich hatte`, `ich ging`) |
| **Động từ nào?** | **Hầu hết các động từ** khi nói | **`sein`, `haben`** (và động từ khuyết thiếu) dùng Präteritum **ngay cả khi nói** |
| **Ví dụ** | *„Gestern **habe** ich eine Radtour **gemacht**.“* | *„Gestern **war** ich in der Stadt.“* / *„Ich **hatte** viel Spaß.“* |

> 🗣️ **Mẫu câu thực tế (cách người Đức kể chuyện)**: **Perfekt cho hành động + Präteritum cho `sein/haben`**
> *„Wir **sind** nach Hạ Long **gefahren**. Das Wetter **war** super, und wir **hatten** viel Spaß. Wir **haben** viele Fotos **gemacht**.“*
> — Chúng tôi đã đi Hạ Long. Thời tiết rất tuyệt, và chúng tôi đã rất vui. Chúng tôi đã chụp nhiều ảnh.

##### ⭐ 4.7.1. Nhận biết (không cần học thuộc): Präteritum của động từ thường
Khi đọc sách, truyện hay thấy dạng Präteritum của động từ thường. Ở A1 chỉ cần **nhận ra** chúng:
| Có quy tắc | Bất quy tắc |
| :--- | :--- |
| `machen → ich **machte**` (đã làm) · `kaufen → er **kaufte**` · `arbeiten → sie **arbeitete**` | `gehen → ich **ging**` · `fahren → er **fuhr**` · `kommen → sie **kam**` · `sehen → wir **sahen**` · `essen → ich **aß**` |

#### 4.8. Từ chỉ thời gian đi kèm Perfekt (`Zeitangaben`)
| Từ / Cụm | Nghĩa | Ví dụ (`🔊 de-DE`) & Dịch |
| :--- | :--- | :--- |
| **gestern** · **vorgestern** | hôm qua · hôm kia | *„Vorgestern **sind** wir in Linz **angekommen**.“* — Hôm kia chúng tôi đã đến Linz. |
| **gestern Abend / Morgen / Nachmittag** | tối / sáng / chiều qua | *„Gestern Abend **habe** ich meine Oma **angerufen**.“* — Tối qua tôi đã gọi điện cho bà. |
| **letzte Woche** · **letzten Monat** · **letztes Jahr** | tuần / tháng / năm trước | *„Letztes Jahr **bin** ich nach Japan **geflogen**.“* — Năm ngoái tôi đã bay đến Nhật. |
| **letzten Sommer** · **letzten Montag** | mùa hè năm ngoái · thứ Hai tuần trước | *„Letzten Sommer **haben** wir am See **gezeltet**.“* |
| **am Wochenende** | vào cuối tuần | *„Am Wochenende **habe** ich eingekauft.“* |
| **vor zwei Tagen** · **vor einer Woche** | cách đây hai ngày · một tuần | *„Vor zwei Tagen **hat** es **geschneit**.“* |
| **früher** · **neulich** | ngày trước · hôm nọ | *„Früher **hat** mein Opa in einem Dorf **gewohnt**.“* |
| **schon** · **noch nicht** | đã … rồi · chưa | *„**Hast** du **schon** das Zimmer **gebucht**?“ — „Nein, **noch nicht**.“* |
| **schon einmal** · **noch nie** | đã từng một lần · chưa bao giờ | *„Ich **bin noch nie** in Wien **gewesen**.“* — Tôi chưa bao giờ ở Wien. |
| **gerade** · **vorhin** | vừa mới · lúc nãy | *„Ich **habe** gerade die Postkarte **geschrieben**.“* |

> 📍 **Vị trí**: Từ chỉ thời gian đứng ở **vị trí 1** (đảo chủ ngữ) hoặc **sau trợ động từ**, **không bao giờ** đứng sau `Partizip II`. Ví dụ đúng: *„Gestern habe ich Fotos gemacht.“* / *„Ich habe gestern Fotos gemacht.“* — Sai: ✘ *„Ich habe Fotos gemacht gestern.“*

#### 4.9. ⚠️ MƯỜI BA LỖI THƯỜNG GẶP KHI DÙNG PERFEKT (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Quên / đặt sai vị trí Partizip II | ✘ *Ich habe gemacht eine Radtour.* | ✔ *Ich habe eine Radtour gemacht.* | Partizip II luôn ở **cuối câu**. |
| 2 | Dùng `haben` cho động từ chuyển động | ✘ *Wir haben nach Wien gefahren.* | ✔ *Wir sind nach Wien gefahren.* | `fahren` (đổi vị trí) → `sein`. |
| 3 | Dùng `sein` cho động từ có tân ngữ | ✘ *Ich bin ein Foto gemacht.* | ✔ *Ich habe ein Foto gemacht.* | Có tân ngữ Akkusativ → `haben`. |
| 4 | Thêm `ge-` cho `-ieren` | ✘ *gefotografiert* | ✔ *fotografiert* | Nhóm 3: không `ge-`. |
| 5 | Thêm `ge-` cho tiền tố không tách | ✘ *gebesucht / gebezahlt* | ✔ *besucht / bezahlt* | Nhóm 4: không `ge-`. |
| 6 | Đặt `ge-` sai chỗ ở động từ tách | ✘ *geeinkauft / gekauft ein* | ✔ *eingekauft* | Nhóm 5: `ein` + `ge` + `kauft`. |
| 7 | Quên `-e-` khi gốc đuôi `-t/-d` | ✘ *gearbeitt / gewartt* | ✔ *gearbeitet / gewartet* | Nhóm 2: thêm `-et`. |
| 8 | Chia sai động từ bất quy tắc | ✘ *gegehen / gefahrt / gesprecht* | ✔ *gegangen / gefahren / gesprochen* | Nhóm 6: phải học thuộc. |
| 9 | Không chia trợ động từ theo ngôi | ✘ *Wir hat Fotos gemacht.* | ✔ *Wir haben Fotos gemacht.* | `wir` → `haben`. |
| 10 | Chia sai Partizip II theo ngôi | ✘ *Du hast gemachst.* | ✔ *Du hast gemacht.* | Partizip II **không đổi** theo ngôi. |
| 11 | Sai trật tự câu hỏi | ✘ *Du hast gemacht was?* | ✔ *Was hast du gemacht?* | W-Wort đứng đầu, trợ động từ vị trí 2. |
| 12 | Sai ngôi `ihr` của `sein` Präteritum | ✘ *Ihr warst in Wien.* | ✔ *Ihr wart in Wien.* | `ihr wart` (không phải `warst`). |
| 13 | Nhầm `essen`/`trinken` với `sein` | ✘ *Ich bin gegessen.* | ✔ *Ich habe gegessen.* | `essen` không chỉ chuyển động / đổi trạng thái → `haben`. |

#### 4.10. 🧰 QUY TRÌNH 5 BƯỚC TẠO CÂU PERFEKT KHÔNG SAI (`Fünf-Schritte-Methode`)
1. **Xác định động từ** và nghĩa trong câu (ví dụ: *đi du lịch Hạ Long* → `fahren`).
2. **Chọn trợ động từ**: `sein` (chuyển động / đổi trạng thái / sein-bleiben-werden) hay `haben` (còn lại)? → `fahren` = **`sein`**.
3. **Chia trợ động từ theo chủ ngữ**: `wir` → **`sind`**.
4. **Tạo Partizip II**: bất quy tắc → tra bảng → **`gefahren`**.
5. **Ráp câu**: trợ động từ ở vị trí 2, Partizip II ở **cuối**: *„Wir **sind** letzten Sommer nach Hạ Long **gefahren**.“*

---

### HỌC PHẦN 5: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN (`TEXTANALYSE: AB IN DEN URLAUB` — KÈM AUDIO `de-DE`)

#### 5.1. Phân tích bài điền từ trên bảng giảng: *"Familie Müller macht eine Radtour"* — vì sao mỗi Partizip II lại có dạng đó?
Bài trên bảng yêu cầu điền Partizip II cho 8 động từ trong 6 câu. Web hiển thị **bảng phân tích** sau (mỗi câu có `🔊`):

| # | Câu hoàn chỉnh (`🔊 de-DE`) | Dịch nghĩa | Partizip II | Nhóm quy tắc & Lý do |
| :-: | :--- | :--- | :--- | :--- |
| 1 | *„Familie Müller **hat** eine Radtour von Passau nach Linz **gemacht**.“* | Gia đình Müller đã đi một chuyến xe đạp từ Passau đến Linz. | **gemacht** | Nhóm 1: `ge` + `mach` + `t`; `machen` + tân ngữ `eine Radtour` → `haben`. |
| 2 | *„Am zweiten Tag **haben** sie **eingekauft** und an der Donau ein Picknick **gemacht**.“* | Vào ngày thứ hai họ đã đi mua sắm và dã ngoại bên sông Donau. | **eingekauft**, **gemacht** | `einkaufen` thuộc nhóm 5 (tiền tố tách): `ein` + `ge` + `kauf` + `t`. `ein Picknick machen` là cụm cố định (xem Học phần 2). |
| 3 | *„In Linz **haben** sie in einer Pension **übernachtet**.“* | Ở Linz họ đã ngủ lại trong một nhà nghỉ. | **übernachtet** | Nhóm 4 (tiền tố `über-` không tách → không `ge-`) + gốc `-t` nên thêm `-et`. |
| 4 | *„In Linz **haben** sie ein Kloster **besichtigt**.“* | Ở Linz họ đã tham quan một tu viện. | **besichtigt** | Nhóm 4: tiền tố `be-` không tách → không `ge-`. |
| 5 | *„In Wien **haben** sie das Rathaus **besucht** und **fotografiert**.“* | Ở Wien họ đã thăm tòa thị chính và chụp ảnh. | **besucht**, **fotografiert** | `besuchen` nhóm 4 (`be-`); `fotografieren` nhóm 3 (`-ieren`, không `ge-`). |
| 6 | *„In Budapest **hat** die Familie ihr Ziel **erreicht**.“* | Ở Budapest gia đình đã đến được đích. | **erreicht** | Nhóm 4: tiền tố `er-` không tách. |

> 🔍 **Quan sát quan trọng**: cả **6 câu đều dùng `haben`** vì không có động từ nào là chuyển động đổi vị trí được chia ở Perfekt (động từ `machen`, `einkaufen`, `übernachten`, `besichtigen`, `besuchen`, `fotografieren`, `erreichen` đều có tân ngữ hoặc là hoạt động tại chỗ). Muốn nói *"họ đã đạp xe đến Budapest"* thì phải dùng `sein`: *„Sie sind nach Budapest gefahren.“*

#### 5.2. Đoạn văn 1: *"Die Radtour der Familie Müller"* — bản mở rộng từ bảng giảng (Perfekt + Präteritum)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Familie Müller **hat** im Sommer eine Radtour an der Donau **gemacht**. Sie **sind** von Passau nach Linz **gefahren**. Am zweiten Tag **haben** sie **eingekauft** und an der Donau ein Picknick **gemacht**. In Linz **haben** sie in einer Pension **übernachtet** und ein Kloster **besichtigt**. Das Wetter **war** gut, aber einen Tag **hat** es **geregnet**. Danach **sind** sie weiter nach Wien **gefahren**. In Wien **haben** sie das Rathaus **besucht** und **fotografiert**. Am Ende **hat** die Familie in Budapest ihr Ziel **erreicht**. Die Reise **war** anstrengend, aber sehr schön.“*
* **Dịch nghĩa tiếng Việt**:
  > *„Gia đình Müller đã đi một chuyến xe đạp dọc sông Donau vào mùa hè. Họ đã đạp xe từ Passau đến Linz. Vào ngày thứ hai họ đã đi mua sắm và dã ngoại bên sông Donau. Ở Linz họ đã ngủ lại trong một nhà nghỉ và đã tham quan một tu viện. Thời tiết đã tốt, nhưng có một ngày trời đã mưa. Sau đó họ đã đi tiếp đến Wien. Ở Wien họ đã thăm tòa thị chính và chụp ảnh. Cuối cùng gia đình đã đến được đích tại Budapest. Chuyến đi mệt mỏi nhưng rất đẹp.“*
* **Bảng tô màu cho người học**: *xanh dương* = trợ động từ (`hat/haben/sind`), *đỏ* = Partizip II, *xanh lá* = Präteritum của `sein` (`war`). Bấm vào một câu → hiện sơ đồ **V1** (khung câu) của chính câu đó.
* **Sơ đồ đi kèm**: **V4** (bản đồ hành trình Passau → Linz → Wien → Budapest).

#### 5.3. Đoạn văn 2: *Phỏng vấn về kỳ nghỉ — Frau Müller & Sophie* (`Präteritum von sein` + Perfekt thời tiết) — khớp bài nối trên bảng giảng
* **Đoạn hội thoại (`🔊 de-DE`, mỗi dòng một nút)**:
  > **Reporter**: *„Wo **waren** Sie in Urlaub, Frau Müller?“*
  > **Frau Müller**: *„Mein Mann und ich **waren** zehn Tage in der Schweiz, nur unsere Tochter Sophie nicht.“*
  > **Reporter**: *„Wo **warst** du, Sophie?“*
  > **Sophie**: *„Ich **war** mit meinem Freund zwei Wochen in Südfrankreich.“*
  > **Reporter**: *„Wie **war** es in Südfrankreich?“*
  > **Sophie**: *„Es **war** sehr schön. In Marseille **war** es toll.“*
  > **Reporter**: *„Wie **war** das Wetter?“*
  > **Sophie**: *„Das Wetter **war** in den ersten Tagen gut. In Marseille **hat** es einen Tag **geregnet**.“*
* **Dịch nghĩa**:
  > **Phóng viên**: *„Bà Müller, bà đã đi nghỉ ở đâu ạ?“* — **Bà Müller**: *„Chồng tôi và tôi đã ở Thụy Sĩ mười ngày, chỉ có con gái chúng tôi là Sophie thì không.“* — **Phóng viên**: *„Còn bạn, Sophie, bạn đã ở đâu?“* — **Sophie**: *„Tôi đã ở miền Nam nước Pháp hai tuần cùng bạn trai.“* — **Phóng viên**: *„Ở miền Nam nước Pháp thế nào?“* — **Sophie**: *„Rất đẹp. Ở Marseille thì tuyệt.“* — **Phóng viên**: *„Thời tiết thế nào?“* — **Sophie**: *„Mấy ngày đầu thời tiết đẹp. Ở Marseille có một ngày trời mưa.“*
* **Điểm ngữ pháp tô sáng**: 5 dạng `war / warst / waren` + `hat geregnet` (động từ thời tiết dùng `haben`, ngôi `es`) + `in der Schweiz` (quốc gia có mạo từ → `in der`).

#### 5.4. Đoạn văn 3 (mới): *E-Mail von Linh aus Hội An* (Perfekt kết hợp Präteritum — văn phong thân mật)
* **Đoạn văn hoàn chỉnh (`🔊 de-DE`)**:
  > *„Hallo Anna, ich **bin** jetzt wieder zu Hause. Der Urlaub in Hội An **war** wunderbar! Wir **waren** eine Woche dort. Wir **sind** mit dem Flugzeug nach Đà Nẵng **geflogen** und dann mit dem Taxi nach Hội An **gefahren**. Das Hotel **war** klein, aber sehr sauber. Jeden Tag **haben** wir die Altstadt **angeschaut** und viele Fotos **gemacht**. Wir **haben** viel **gegessen**, und das Essen **war** sehr lecker. Am Strand **sind** wir im Meer **geschwommen**. Nur das Wetter **war** nicht immer gut: Zwei Tage **hat** es **geregnet**. Am Sonntag **sind** wir wieder nach Hause **geflogen**. Ich **habe** viele Souvenirs **gekauft**. Bis bald! Deine Linh“*
* **Dịch nghĩa**:
  > *„Chào Anna, bây giờ mình đã về nhà rồi. Kỳ nghỉ ở Hội An thật tuyệt vời! Chúng mình đã ở đó một tuần. Chúng mình đã bay đến Đà Nẵng rồi đi taxi tới Hội An. Khách sạn nhỏ nhưng rất sạch. Ngày nào chúng mình cũng ngắm phố cổ và chụp nhiều ảnh. Chúng mình đã ăn rất nhiều và đồ ăn rất ngon. Ở bãi biển chúng mình đã bơi dưới biển. Chỉ có thời tiết không phải lúc nào cũng tốt: trời đã mưa hai ngày. Vào Chủ nhật chúng mình đã bay về nhà. Mình đã mua nhiều quà lưu niệm. Hẹn gặp lại! Linh của bạn“*
* **Bảng phân tích bắt buộc kèm theo (hiển thị khi bấm "🔍 Phân tích")**:

| Cụm trong thư | Trợ động từ | Partizip II | Lý do |
| :--- | :---: | :--- | :--- |
| *wir sind … nach Đà Nẵng geflogen* | **sein** | geflogen | `fliegen`: chuyển động đổi vị trí, bất quy tắc |
| *dann … nach Hội An gefahren* | **sein** | gefahren | `fahren`: chuyển động đổi vị trí |
| *wir haben die Altstadt angeschaut* | **haben** | angeschaut | `anschauen`: tách, có tân ngữ → `an` + `ge` + `schaut` |
| *viele Fotos gemacht* | **haben** | gemacht | `machen` + tân ngữ Akkusativ |
| *wir haben viel gegessen* | **haben** | gegessen | `essen` bất quy tắc, không chuyển động |
| *wir sind im Meer geschwommen* | **sein** | geschwommen | `schwimmen`: di chuyển trong nước |
| *hat es geregnet* | **haben** | geregnet | động từ thời tiết, gốc `regn-` → `-et` |
| *wir sind wieder nach Hause geflogen* | **sein** | geflogen | `fliegen` hướng về nhà |
| *ich habe … Souvenirs gekauft* | **haben** | gekauft | `kaufen` + tân ngữ |
| *war / waren* | — | — | Präteritum của `sein` (không dùng Perfekt `bin gewesen`) |

---

### HỌC PHẦN 6: BẢNG TỔNG HỢP KIẾN THỨC (`CHEAT SHEET` — IN ĐƯỢC TRÊN 1 TRANG)
| Mục | Ghi nhớ nhanh |
| :--- | :--- |
| **Công thức** | `S + haben/sein (vị trí 2) + … + Partizip II (cuối câu)` |
| **haben** | habe · hast · hat · haben · habt · haben |
| **sein** | bin · bist · ist · sind · seid · sind |
| **Chọn sein** | Chuyển động đổi vị trí (gehen, fahren, fliegen, kommen, laufen, reisen, wandern, ankommen…) · đổi trạng thái (einschlafen, aufwachen, schmelzen, passieren…) · `sein / bleiben / werden` |
| **Chọn haben** | Mọi trường hợp còn lại, nhất là có tân ngữ Akkusativ và động từ tại chỗ (schlafen, wohnen, arbeiten, regnen…) |
| **Partizip II — 6 nhóm** | ① `ge+gốc+t` · ② `ge+gốc+et` (gốc `-t/-d`…) · ③ `-ieren` → `gốc+t` (không `ge-`) · ④ tiền tố không tách → không `ge-` · ⑤ tiền tố tách → `tiền tố+ge+gốc+t` · ⑥ bất quy tắc `ge+…+en` (+ hỗn hợp `ge+…+t`) |
| **Präteritum sein** | war · warst · war · waren · wart · waren |
| **Präteritum haben** | hatte · hattest · hatte · hatten · hattet · hatten |
| **Nói về kỳ nghỉ** | `Wo warst du?` → `Ich war am Meer / in Berlin / auf der Insel…` · `Wie war es?` → `Es war toll.` · `Wie war das Wetter?` → `Das Wetter war gut.` |
| **Từ chỉ thời gian** | gestern, vorgestern, letzte Woche, letzten Sommer, am Wochenende, vor zwei Tagen, früher, schon, noch nicht, noch nie |
| **Phủ định** | `nicht` trước Partizip II / bổ ngữ hướng; `kein-` trước danh từ |

---

### HỌC PHẦN 7 (MỤC 2.7): ĐẶC TẢ 6 SƠ ĐỒ SVG TRỰC QUAN (`static/js/perfekt_svg.js`)
Mỗi sơ đồ phải có **tiêu đề tiếng Việt + nhãn tiếng Đức**, hoạt động đúng ở chế độ Dark/Light, và mọi câu tiếng Đức hiển thị trong sơ đồ có nút **`🔊`** (chỉ đọc chuỗi tiếng Đức sạch).

| Mã | Tên sơ đồ | Hình vẽ & hành vi bắt buộc |
| :-: | :--- | :--- |
| **V1** | **Khung câu Perfekt (`Satzklammer`)** | Một hàng 4 ô: **Vị trí 1** (Chủ ngữ / Thời gian) · **Vị trí 2** (`haben/sein`, ô màu xanh dương) · **Phần giữa** (tân ngữ, địa điểm, thời gian — ô xám) · **Cuối câu** (`Partizip II`, ô màu đỏ). Một **đường cong mũi tên nối ô Vị trí 2 với ô Cuối câu** như cặp ngoặc kẹp lấy phần giữa. Có 4 ví dụ chuyển được bằng nút `◀ ▶`: *„Ich \| habe \| Hausaufgaben \| gemacht.“* · *„Gestern \| bin \| ich nicht zur Schule \| gegangen.“* · *„Hast \| du \| die Fotos \| gemacht?“* · *„Wir \| haben \| auf dem Markt \| eingekauft.“* |
| **V2** | **Lưu đồ tạo Partizip II** | Sơ đồ khối từ trên xuống: `Infinitiv` → *"Bất quy tắc? (tra bảng 4.5)"* → *"Có tiền tố tách được?"* (nhấn trọng âm ở tiền tố) → *"Có tiền tố không tách?"* → *"Đuôi `-ieren`?"* → *"Gốc kết thúc `-t/-d/-gn/-ffn/-chn`?"* → 6 ô kết quả có ví dụ (`machen → gemacht`, `arbeiten → gearbeitet`, `studieren → studiert`, `besuchen → besucht`, `einkaufen → eingekauft`, `gehen → gegangen`). Bấm ô kết quả → phát âm ví dụ. |
| **V3** | **Cây quyết định `haben` / `sein`** | Cây 4 nút theo mục 4.6.4. Nhánh `sein` màu cam, nhánh `haben` màu xanh lá. Cuối mỗi nhánh có 3 ví dụ động từ (`sein`: *fahren, einschlafen, bleiben*; `haben`: *machen, schlafen, regnen*). |
| **V4** | **Bản đồ hành trình sông Donau (tương tác)** | Đường sông uốn lượn nối **4 điểm theo đúng thứ tự địa lý: 📍 Passau → 📍 Linz → 📍 Wien → 🏁 Budapest**. Mỗi điểm có biểu tượng hoạt động (🚴 xe đạp tại Passau, 🏨 `Pension` + ⛪ `Kloster` tại Linz, 🏛️ `Rathaus` + 📷 tại Wien, 🏁 `Ziel` tại Budapest). **Bấm một điểm → hiện 1–2 câu Perfekt tương ứng của Đoạn văn 5.2** (kèm dịch và `🔊`); nút **▶ "Đọc cả hành trình"** đọc lần lượt 4 chặng bằng `de-DE`. |
| **V5** | **Trục thời gian Perfekt / Präteritum** | Trục ngang `Vergangenheit (quá khứ) — Gegenwart (hiện tại: jetzt) — Zukunft`. Bên trái điểm "jetzt": hai tầng — tầng trên **Perfekt (văn nói)** *„Ich habe Fotos gemacht.“*, tầng dưới **Präteritum (văn viết)** *„Ich machte Fotos.“* — kèm nhãn *"sein/haben luôn dùng Präteritum khi nói: ich war, ich hatte"*. Tại "jetzt": *„Ich mache Fotos.“* |
| **V6** | **Máy tính Partizip II tương tác** | Ô chọn / gõ một động từ trong bảng nguồn `PERFEKT_VERBS` (Phần 4, mục 4.5 & Phụ lục A). Hiển thị **từng bước chẩn đoán** (tách / không tách → quy tắc → trợ động từ) và kết quả *„Ich habe/bin … + Partizip II“*; bấm `🔊` đọc câu ví dụ chứa động từ đó. **Chỉ dùng dữ liệu của bảng nguồn, tuyệt đối không tự suy diễn** để tránh sinh ra Partizip sai. |

---

## PHẦN 3: KHO 100 BÀI TẬP ĐỘC NHẤT CỦA BÀI 9 (`lessons/a1/seed_a1_b9.py`) — 14 DẠNG BÀI, TRỌNG TÂM PERFEKT

Toàn bộ **100 câu hỏi** dưới đây là **câu mới sáng tác**, chỉ tham khảo ý tưởng từ bảng giảng; không trùng với giáo trình và không trùng với Bài 8. Chủ ngữ được **xoay vòng đủ 9 ngôi** (`ich, du, er, sie, es, wir, ihr, sie, Sie`) cùng tên riêng, gia đình, du khách, học sinh; ngữ cảnh đa dạng (Đà Lạt, Hội An, Phú Quốc, Hạ Long, Cát Bà, Berlin, Wien, Hamburg, Alpen...). Độ khó chỉ nhỉnh hơn tài liệu gốc (có câu phủ định, câu hỏi, đảo ngữ, động từ tách).

### 3.1. Bảng Phân Bổ 100 Câu Hỏi Theo 14 Dạng Bài Tập
| STT | Mã dạng (`type`) | Tên dạng bài hiển thị | Số lượng | Mã câu | Trọng tâm |
| :-: | :--- | :--- | :-: | :-: | :--- |
| 1 | `trac_nghiem` | Trắc nghiệm | **12** | 1–12 | Vị trí động từ, Partizip II, chọn trợ động từ, tìm câu sai, Präteritum `sein`, giống & số nhiều từ vựng |
| 2 | `dien_khuyet` | Điền khuyết | **14** | 13–26 | Điền trợ động từ / Partizip II / `war, warst, hatten` |
| 3 | `dich_nghia_vd` | Dịch từ / cụm: Việt → Đức | **8** | 27–34 | Danh từ du lịch (kèm mạo từ) + cụm Perfekt ngắn |
| 4 | `dich_nghia_dv` | Dịch từ / cụm: Đức → Việt | **8** | 35–42 | Danh từ + câu ngắn |
| 5 | `noi_o` | Nối ô (Matching) | **8** | 43–50 | Nối Infinitiv ↔ Partizip II (5 nhóm), quy tắc ↔ ví dụ, hỏi ↔ đáp, ngôi ↔ `war/hatte` |
| 6 | `dien_tao_cau` | Điền 2 chỗ trống tạo câu | **8** | 51–58 | Điền trợ động từ + Partizip II trong cùng một câu |
| 7 | `nghe_dien` | Nghe `de-DE` và điền từ | **8** | 59–66 | Nghe câu Perfekt / Präteritum rồi điền từ |
| 8 | `dich_cau_vd` | Dịch câu: Việt → Đức | **6** | 67–72 | Dịch câu Perfekt (đa đáp án) |
| 9 | `dich_cau_dv` | Dịch câu: Đức → Việt | **6** | 73–78 | Dịch câu / đoạn hội thoại ngắn |
| 10 | `sap_xep_cau` 🆕 | **Sắp xếp từ thành câu** | **6** | 79–84 | Luyện `Satzklammer` (vị trí trợ động từ & Partizip II) |
| 11 | `chon_haben_sein` 🆕 | **Phân loại `haben` / `sein`** | **4** | 85–88 | Mỗi câu 4 động từ → xếp vào cột `haben` hoặc `sein` |
| 12 | `tim_loi_sai` 🆕 | **Tìm lỗi và sửa câu** | **4** | 89–92 | Sai trợ động từ / Partizip II / vị trí động từ |
| 13 | `viet_lai_perfekt` 🆕 | **Viết lại câu: Präsens → Perfekt** | **4** | 93–96 | Chuyển thì, chọn `haben/sein`, tạo Partizip II |
| 14 | `dung_sai` 🆕 | **Đọc hiểu Đúng / Sai (Richtig / Falsch)** | **4** | 97–100 | 2 đoạn văn ngắn, mỗi đoạn 2 mệnh đề |
| | | **TỔNG CỘNG BÀI 9** | **100** | 1–100 | **100% độc nhất + QA Zero-Bug** |

> 📌 Phân bổ trọng tâm: **hơn 75 / 100 câu** kiểm tra trực tiếp Perfekt (Partizip II, trợ động từ, vị trí động từ, chuyển thì), phần còn lại kiểm tra từ vựng du lịch và Präteritum `sein/haben`.

### 3.2. Đặc tả giao diện & chấm điểm cho 5 dạng bài MỚI (🆕)
| Dạng | Giao diện người học | Dữ liệu câu hỏi (`question object`) | Quy tắc chấm điểm |
| :--- | :--- | :--- | :--- |
| `sap_xep_cau` | Các **ô từ / cụm từ** xáo trộn; người học bấm lần lượt để xếp thành câu; có nút `↩ Xóa` và `🔊 Nghe thử` (đọc câu đúng sau khi trả lời xong) | `tokens` (danh sách đã xáo trộn, **không** đánh dấu chữ hoa đầu câu), `accepted_answers` (mọi trật tự hợp lệ), `translation_vi` | So khớp **không phân biệt hoa/thường**, bỏ dấu câu cuối, chuẩn hóa khoảng trắng. Mọi trật tự hợp lệ (đảo ngữ với thời gian) đều phải có trong `accepted_answers`. |
| `chon_haben_sein` | Bảng 4 hàng, mỗi hàng 1 động từ + nghĩa tiếng Việt + 2 nút **`haben`** / **`sein`**; kèm sơ đồ `V3` | `items` = 4 × {`verb`, `meaning_vi`, `aux`, `partizip`, `reason_vi`} | Đúng khi **cả 4 hàng** đều đúng; sai hàng nào thì tô đỏ hàng đó và hiện `reason_vi`. |
| `tim_loi_sai` | Hiển thị 1 câu có **đúng 1 lỗi**; người học **gõ lại cả câu đã sửa** | `wrong_sentence`, `error_type` (`hilfsverb` / `partizip` / `wortstellung`), `accepted_answers`, `translation_vi` (dịch **câu đúng**) | So khớp như `dich_cau_vd`. Giải thích phải nêu rõ **lỗi gì**. |
| `viet_lai_perfekt` | Hiển thị câu Präsens; người học **gõ lại ở Perfekt** (giữ nguyên các từ khác) | `source_sentence`, `accepted_answers`, `translation_vi` (dịch câu Perfekt) | So khớp như `dich_cau_vd`. |
| `dung_sai` | Đoạn văn ngắn + 1 mệnh đề + 2 nút **Richtig (Đúng)** / **Falsch (Sai)** | `reading_text`, `reading_translation_vi`, `statement`, `statement_vi`, `answer` (`Richtig`/`Falsch`) | Giải thích phải **trích đúng câu trong đoạn văn** chứng minh đáp án. |

> 🔊 **Quy tắc voice cho mọi dạng**: sau khi người học trả lời xong, nút `🔊` đọc **câu tiếng Đức đúng đầy đủ** (đã điền chỗ trống / đã sắp xếp / đã sửa lỗi). Dạng `dich_nghia_dv`, `dich_cau_dv`: đọc câu tiếng Đức ở đề bài. Không bao giờ đọc ký hiệu `___`, `[1]`, `→`.

---

### 3.3. Danh Sách Chi Tiết 100 Câu Hỏi (Để Seed Vào `lessons/a1/seed_a1_b9.py`)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 12 Câu: Câu 1 → Câu 12)
1. **Câu 1** *(kèm sơ đồ `visual: V1`)*
   * `question`: Quan sát **sơ đồ V1 (khung câu Perfekt)** bên trên. Chọn câu có **vị trí động từ ĐÚNG**:
   * Đáp án: `A. Wir haben gestern ein Schloss besichtigt.` (Đúng) | `B. Wir haben gestern besichtigt ein Schloss.` | `C. Wir gestern haben ein Schloss besichtigt.` | `D. Wir besichtigt haben gestern ein Schloss.`
   * Dịch nghĩa câu: *„Hôm qua chúng tôi đã tham quan một lâu đài.“*
   * Giải thích: Trợ động từ **`haben`** đứng ở **vị trí thứ 2**, còn **`Partizip II` (`besichtigt`) phải đứng cuối câu** → **`Wir haben gestern ein Schloss besichtigt.`**
2. **Câu 2**
   * `question`: Chọn Partizip II đúng cho động từ `fotografieren`: *„Die Touristen haben den Dom ___.“*
   * Đáp án: `A. gefotografiert` | `B. fotografiert` (Đúng) | `C. fotografieren` | `D. gefotografieret`
   * Dịch nghĩa câu: *„Các du khách đã chụp ảnh nhà thờ lớn.“*
   * Giải thích: Động từ đuôi **`-ieren`** **không có `ge-`**: gốc `fotografier` + `t` = **`fotografiert`**.
3. **Câu 3**
   * `question`: `einkaufen` là động từ tách. Chọn Partizip II đúng: *„Wir haben auf dem Markt frisches Obst ___.“*
   * Đáp án: `A. geeinkauft` | `B. eingekauft` (Đúng) | `C. einkauft` | `D. gekauft ein`
   * Dịch nghĩa câu: *„Chúng tôi đã mua sắm trái cây tươi ở chợ.“*
   * Giải thích: Tiền tố tách `ein-` → **`ein` + `ge` + `kauf` + `t` = `eingekauft`** (`ge` chèn vào giữa tiền tố và gốc).
4. **Câu 4**
   * `question`: Chọn trợ động từ đúng: *„Gestern ___ wir um sieben Uhr nach Wien gefahren.“*
   * Đáp án: `A. haben` | `B. sind` (Đúng) | `C. ist` | `D. hat`
   * Dịch nghĩa câu: *„Hôm qua lúc bảy giờ chúng tôi đã đi đến Wien.“*
   * Giải thích: `fahren` là chuyển động đổi vị trí → dùng **`sein`**; chủ ngữ `wir` → **`sind`**.
5. **Câu 5**
   * `question`: Chọn câu **SAI** ngữ pháp:
   * Đáp án: `A. Ich bin im Urlaub nach Hạ Long geflogen.` | `B. Meine Eltern sind drei Tage in Đà Lạt geblieben.` | `C. Der Schnee ist in der Sonne geschmolzen.` | `D. Wir sind gestern ein Picknick gemacht.` (Đúng — đây là câu sai)
   * Dịch nghĩa câu (D sửa lại): *„Hôm qua chúng tôi đã dã ngoại.“*
   * Giải thích: `machen` có tân ngữ `ein Picknick` → phải dùng **`haben`**: **`Wir haben gestern ein Picknick gemacht.`** Ba câu A, B, C đều đúng (`fliegen`, `bleiben`, `schmelzen` đều dùng `sein`).
6. **Câu 6**
   * `question`: Cặp Infinitiv – Partizip II nào **ĐÚNG 100%**?
   * Đáp án: `A. essen – geesst / trinken – getrinkt` | `B. sehen – gesehen / schlafen – geschlafen` (Đúng) | `C. nehmen – genehmt / finden – gefindet` | `D. schreiben – geschreibt / singen – gesingt`
   * Dịch nghĩa câu: *„nhìn – đã nhìn / ngủ – đã ngủ.“*
   * Giải thích: **`sehen → gesehen`**, **`schlafen → geschlafen`** là bất quy tắc đúng; các dạng còn lại phải là `gegessen`, `getrunken`, `genommen`, `gefunden`, `geschrieben`, `gesungen`.
7. **Câu 7**
   * `question`: Chọn cặp dạng chia `sein` ở Präteritum: *„Wie war das Wetter in Đà Lạt? — Es ___ sehr kalt, aber wir ___ glücklich.“*
   * Đáp án: `A. war / waren` (Đúng) | `B. waren / war` | `C. warst / wart` | `D. wart / warst`
   * Dịch nghĩa câu: *„Thời tiết ở Đà Lạt thế nào? — Trời rất lạnh, nhưng chúng tôi đã rất hạnh phúc.“*
   * Giải thích: `es` → **`war`**; `wir` → **`waren`**.
8. **Câu 8**
   * `question`: Chọn cặp đúng: *„Wo ___ ihr letztes Wochenende? — Wir ___ am See.“*
   * Đáp án: `A. wart / waren` (Đúng) | `B. warst / waren` | `C. wart / war` | `D. seid / sind`
   * Dịch nghĩa câu: *„Cuối tuần trước các bạn đã ở đâu? — Chúng tôi đã ở bên hồ.“*
   * Giải thích: Präteritum của `sein`: `ihr` → **`wart`**, `wir` → **`waren`**. `seid / sind` là Präsens (hiện tại), không phải quá khứ.
9. **Câu 9** *(Partizip II của 3 động từ có tiền tố không tách)*
   * `question`: Chọn dãy Partizip II đúng của `besuchen – übernachten – erreichen`:
   * Đáp án: `A. gebesucht – geübernachtet – geerreicht` | `B. besucht – übernachtet – erreicht` (Đúng) | `C. besuchet – übernachtt – erreichet` | `D. besucht – geübernachtet – erreicht`
   * Dịch nghĩa câu: *„đã thăm – đã ngủ lại – đã đến được.“*
   * Giải thích: Tiền tố **`be-`, `über-`, `er-` không tách → không có `ge-`**. Riêng `übernachten` có gốc kết thúc `-t` nên thêm `-et`: **`übernachtet`**.
10. **Câu 10** *(kèm sơ đồ `visual: V2`)*
    * `question`: Quan sát **lưu đồ V2**. Vì sao Partizip II của `arbeiten` là `gearbeitet` (có `-et`) mà không phải `gearbeit`?
    * Đáp án: `A. Vì arbeiten là động từ bất quy tắc.` | `B. Vì gốc "arbeit" kết thúc bằng -t nên phải thêm -e- để dễ phát âm.` (Đúng) | `C. Vì arbeiten là động từ tách.` | `D. Vì arbeiten dùng trợ động từ sein.`
    * Dịch nghĩa câu: *„Đã làm việc.“*
    * Giải thích: Gốc động từ kết thúc bằng **`-t` hoặc `-d`** thì dùng công thức **`ge` + gốc + `et`** → **`gearbeitet`** (tương tự `gewartet`, `gebadet`).
11. **Câu 11**
    * `question`: Dòng nào ghi **ĐÚNG cả mạo từ lẫn số nhiều**?
    * Đáp án: `A. der Strand – die Strände / die Insel – die Inseln / das Meer – die Meere` (Đúng) | `B. der Strand – die Strands / der Insel – die Insel / das Meer – die Meeren` | `C. der Berg – die Berge / der See – die Seen / die Fluss – die Flüsse` | `D. der Urlaub – die Urlauber / das Hotel – die Hotelse / das Schloss – die Schlosse`
    * Dịch nghĩa câu: *„bãi biển – các bãi biển / hòn đảo – các hòn đảo / biển – các biển.“*
    * Giải thích: `der Strand → die Strände` (thêm Umlaut), `die Insel → die Inseln`, `das Meer → die Meere`. Ở C sai vì `der Fluss` là giống đực; ở D sai số nhiều (`die Urlaube`, `die Hotels`, `die Schlösser`).
12. **Câu 12**
    * `question`: Khi **nói chuyện hằng ngày**, câu nào vừa đúng ngữ pháp vừa tự nhiên nhất để kể *"Hôm qua tôi đã đi mua sắm"*?
    * Đáp án: `A. Gestern kaufte ich ein.` | `B. Gestern habe ich eingekauft.` (Đúng) | `C. Gestern bin ich eingekauft.` | `D. Gestern habe ich einkauft.`
    * Dịch nghĩa câu: *„Hôm qua tôi đã đi mua sắm.“*
    * Giải thích: Văn nói dùng **Perfekt**: `einkaufen` (có hoạt động, không đổi vị trí) → **`haben`** + **`eingekauft`**. A đúng ngữ pháp nhưng là Präteritum mang văn viết; C sai trợ động từ; D sai Partizip II.

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 14 Câu: Câu 13 → Câu 26)
13. **Câu 13**: Điền trợ động từ thích hợp: *„Meine Oma ___ im Sommer auf der Insel Phú Quốc Urlaub gemacht.“*
    * Đáp án chấp nhận: `["hat"]`
    * Dịch nghĩa câu: *„Bà tôi đã đi nghỉ trên đảo Phú Quốc vào mùa hè.“*
    * Giải thích: Cụm 'Urlaub machen' chỉ hoạt động và có tân ngữ nên đi với trợ động từ 'haben'. Chủ ngữ 'Meine Oma' thuộc ngôi thứ 3 số ít (sie) nên chia là 'hat'.
14. **Câu 14**: Điền trợ động từ thích hợp: *„Mein Bruder ___ gestern Abend um zehn Uhr eingeschlafen.“*
    * Đáp án chấp nhận: `["ist"]`
    * Dịch nghĩa câu: *„Anh trai tôi đã ngủ thiếp đi lúc mười giờ tối qua.“*
    * Giải thích: Động từ tách 'einschlafen' (ngủ thiếp đi) diễn tả sự thay đổi trạng thái nên đi với trợ động từ 'sein'. Chủ ngữ 'Mein Bruder' thuộc ngôi thứ 3 số ít (er) nên chia là 'ist'.
15. **Câu 15**: Chia dạng đúng của động từ 'suchen': *„Habt ihr am Strand den Reiseführer ___?“*
    * Đáp án chấp nhận: `["gesucht"]`
    * Dịch nghĩa câu: *„Các bạn đã tìm người hướng dẫn viên du lịch (hoặc: cuốn sách hướng dẫn du lịch) ở bãi biển phải không?“*
    * Giải thích: Câu có trợ động từ 'Habt' ở đầu câu nên cuối câu cần điền Partizip II. 'suchen' là động từ có quy tắc: ge + such + t -> gesucht.
16. **Câu 16**: Chia dạng đúng của động từ 'ankommen': *„Der Zug ist pünktlich in München ___.“*
    * Đáp án chấp nhận: `["angekommen"]`
    * Dịch nghĩa câu: *„Chuyến tàu đã đến München đúng giờ.“*
    * Giải thích: 'ankommen' là động từ tách (tiền tố 'an-') kết hợp với động từ bất quy tắc 'kommen' (Partizip II là 'gekommen'). Khi ghép lại, '-ge-' nằm giữa tiền tố và gốc động từ: an + ge + kommen -> angekommen.
17. **Câu 17**: Chia dạng đúng của động từ 'übernachten': *„Wir haben im Zelt ___.“*
    * Đáp án chấp nhận: `["übernachtet", "uebernachtet"]`
    * Dịch nghĩa câu: *„Chúng tôi đã ngủ lại trong lều.“*
    * Giải thích: Động từ 'übernachten' có tiền tố không tách 'über-' nên không thêm 'ge-' ở Partizip II. Vì gốc động từ 'übernacht-' kết thúc bằng âm '-t' nên phải thêm đuôi '-et' -> übernachtet.
18. **Câu 18**: Chia dạng đúng của động từ 'bezahlen': *„Hast du schon die Rechnung ___?“*
    * Đáp án chấp nhận: `["bezahlt"]`
    * Dịch nghĩa câu: *„Bạn đã trả hóa đơn chưa?“*
    * Giải thích: Động từ 'bezahlen' là động từ có quy tắc mang tiền tố không tách 'be-', nên khi chuyển sang Partizip II không thêm 'ge-', chỉ lấy gốc 'bezahl-' + '-t' -> bezahlt.
19. **Câu 19**: Chia dạng đúng của động từ 'baden': *„Die Kinder haben den ganzen Tag im Meer ___.“*
    * Đáp án chấp nhận: `["gebadet"]`
    * Dịch nghĩa câu: *„Bọn trẻ đã tắm biển cả ngày.“*
    * Giải thích: 'baden' là động từ có quy tắc nhưng gốc 'bad-' kết thúc bằng phụ âm '-d', do đó phải thêm âm đệm '-e-' trước đuôi '-t' để dễ phát âm: ge + bad + et -> gebadet.
20. **Câu 20**: Chia dạng đúng của động từ 'regnen': *„Gestern hat es den ganzen Tag ___.“*
    * Đáp án chấp nhận: `["geregnet"]`
    * Dịch nghĩa câu: *„Hôm qua trời đã mưa cả ngày.“*
    * Giải thích: 'regnen' là động từ có quy tắc có gốc 'regn-' kết thúc bằng cụm phụ âm '-gn', nên khi tạo Partizip II phải thêm âm đệm '-e-' trước đuôi '-t': ge + regn + et -> geregnet.
21. **Câu 21**: Chia dạng đúng của động từ 'essen': *„Ich habe am Abend Reis mit Fisch ___.“*
    * Đáp án chấp nhận: `["gegessen"]`
    * Dịch nghĩa câu: *„Buổi tối tôi đã ăn cơm với cá.“*
    * Giải thích: 'essen' là động từ bất quy tắc đặc biệt: khi chuyển sang Partizip II cần chèn thêm phụ âm '-g-' vào giữa tiền tố 'ge-' và gốc 'essen' -> gegessen.
22. **Câu 22**: Chia dạng đúng của động từ 'studieren': *„Die Studentin hat ein Jahr in Wien ___.“*
    * Đáp án chấp nhận: `["studiert"]`
    * Dịch nghĩa câu: *„Nữ sinh viên đã học đại học một năm ở Wien.“*
    * Giải thích: Các động từ có đuôi '-ieren' khi chuyển sang Partizip II không thêm tiền tố 'ge-', chỉ lấy gốc động từ 'studier-' cộng đuôi '-t' -> studiert.
23. **Câu 23**: Điền động từ thích hợp ở thì quá khứ: *„Letzten Sommer ___ ich mit meiner Familie in Đà Nẵng.“*
    * Đáp án chấp nhận: `["war"]`
    * Dịch nghĩa câu: *„Mùa hè năm ngoái tôi đã ở Đà Nẵng cùng gia đình.“*
    * Giải thích: Trạng ngữ 'Letzten Sommer' (mùa hè năm ngoái) chỉ quá khứ và cụm 'in Đà Nẵng' chỉ nơi chốn nên ta dùng động từ 'sein' ở thì Präteritum. Đi với chủ ngữ ngôi thứ nhất số ít 'ich' chia là 'war'.
24. **Câu 24**: Điền động từ thích hợp ở thì quá khứ: *„Wo ___ du gestern Nachmittag, Linh? Ich habe dich nicht gesehen.“*
    * Đáp án chấp nhận: `["warst"]`
    * Dịch nghĩa câu: *„Chiều qua bạn đã ở đâu vậy, Linh? Mình đã không nhìn thấy bạn.“*
    * Giải thích: Câu hỏi về địa điểm ('Wo') vào thời điểm 'gestern Nachmittag' (chiều hôm qua) nên dùng động từ 'sein' ở thì Präteritum. Chia theo chủ ngữ ngôi thứ hai số ít 'du' là 'warst'.
25. **Câu 25**: Điền động từ thích hợp ở thì quá khứ: *„Die Kinder ___ gestern viel Spaß am Strand.“*
    * Đáp án chấp nhận: `["hatten"]`
    * Dịch nghĩa câu: *„Hôm qua bọn trẻ đã rất vui ở bãi biển.“*
    * Giải thích: Cụm 'viel Spaß haben' (có nhiều niềm vui / rất vui) diễn ra vào 'gestern' (hôm qua) nên dùng động từ 'haben' ở thì Präteritum. Chủ ngữ 'Die Kinder' là ngôi thứ 3 số nhiều (sie) nên chia là 'hatten'.
26. **Câu 26**: Chia dạng đúng của động từ 'wandern': *„Ihr seid am Wochenende in den Bergen ___.“*
    * Đáp án chấp nhận: `["gewandert"]`
    * Dịch nghĩa câu: *„Cuối tuần các bạn đã đi bộ đường dài trên núi.“*
    * Giải thích: Câu đã có trợ động từ 'seid' ở vị trí thứ 2 nên cuối câu cần điền Partizip II. 'wandern' là động từ có quy tắc: ge + wander + t -> gewandert.

---

#### NHÓM 3: DỊCH TỪ / CỤM TỪ VIỆT → ĐỨC (`dich_nghia_vd` — 8 Câu: Câu 27 → Câu 34)
27. **Câu 27**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"cuộc hành trình bằng xe đạp"***
    * Đáp án chấp nhận: `["die Radtour", "Radtour"]`
    * Giải thích: Cuộc hành trình bằng xe đạp là danh từ giống cái **`die Radtour`** (số nhiều: `die Radtouren`).
28. **Câu 28**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"phố cổ"***
    * Đáp án chấp nhận: `["die Altstadt", "Altstadt"]`
    * Giải thích: Phố cổ là **`die Altstadt`** (số nhiều: `die Altstädte`).
29. **Câu 29**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"sách hướng dẫn du lịch"***
    * Đáp án chấp nhận: `["der Reiseführer", "Reiseführer", "der Reisefuehrer"]`
    * Giải thích: Sách hướng dẫn du lịch là **`der Reiseführer`** (số nhiều: `die Reiseführer`).
30. **Câu 30**: Dịch sang tiếng Đức (kèm mạo từ số ít): ***"điểm đến du lịch"***
    * Đáp án chấp nhận: `["das Reiseziel", "Reiseziel"]`
    * Giải thích: `die Reise` + `das Ziel` → giống của từ cuối: **`das Reiseziel`** (số nhiều: `die Reiseziele`).
31. **Câu 31**: Dịch sang tiếng Đức bằng **Perfekt**: ***"Anh ấy đã đến nơi."*** *(động từ `ankommen`)*
    * Đáp án chấp nhận: `["er ist angekommen", "Er ist angekommen."]`
    * Giải thích: `ankommen` là chuyển động → `sein`; `er` → `ist`; Partizip II **`angekommen`** → **`er ist angekommen`**.
32. **Câu 32**: Dịch sang tiếng Đức bằng **Perfekt**: ***"Chúng tôi đã cắm trại."*** *(động từ `zelten`)*
    * Đáp án chấp nhận: `["wir haben gezeltet", "Wir haben gezeltet."]`
    * Giải thích: `zelten` dùng `haben`; `wir` → `haben`; gốc `zelt` đuôi `-t` → **`gezeltet`** → **`wir haben gezeltet`**.
33. **Câu 33**: Dịch sang tiếng Đức (**dạng số nhiều**): ***"những kỳ nghỉ"*** *(số nhiều của `der Urlaub`)*
    * Đáp án chấp nhận: `["die Urlaube", "Urlaube"]`
    * Giải thích: Số nhiều của `der Urlaub` là **`die Urlaube`**.
34. **Câu 34**: Dịch sang tiếng Đức bằng **Perfekt**: ***"Tôi đã thử món ăn."*** *(`das Essen probieren`)*
    * Đáp án chấp nhận: `["ich habe das Essen probiert", "Ich habe das Essen probiert."]`
    * Giải thích: `probieren` đuôi `-ieren` → không `ge-`: **`probiert`**; `ich` → `habe` → **`ich habe das Essen probiert`**.

---

#### NHÓM 4: DỊCH TỪ & CÂU NGẮN ĐỨC → VIỆT (`dich_nghia_dv` — 8 Câu: Câu 35 → Câu 42)
35. **Câu 35**: Dịch sang tiếng Việt: ***„das Reiseland“***
    * Đáp án chấp nhận: `["đất nước du lịch", "quốc gia du lịch", "nước du lịch", "xứ sở du lịch", "một đất nước du lịch", "một quốc gia du lịch", "một nước du lịch", "một xứ sở du lịch", "cái đất nước du lịch"]`
    * Dịch nghĩa câu: *„đất nước du lịch / quốc gia du lịch“*
    * Giải thích: `die Reise` (chuyến du lịch) + `das Land` (đất nước) = **`das Reiseland`**.
36. **Câu 36**: Dịch sang tiếng Việt: ***„der Bummel“***
    * Đáp án chấp nhận: `["cuộc đi dạo", "chuyến đi dạo", "buổi đi dạo", "cuộc dạo phố", "buổi dạo phố", "chuyến dạo phố", "đi dạo", "đi dạo phố", "dạo phố", "sự đi dạo", "cuộc tản bộ", "chuyến tản bộ", "buổi tản bộ", "đi tản bộ", "tản bộ"]`
    * Dịch nghĩa câu: *„cuộc đi dạo (phố) / buổi dạo phố / đi dạo“*
    * Giải thích: `der Bummel` là cuộc đi dạo phố, tản bộ ngắm cảnh (số nhiều: `die Bummel`).
37. **Câu 37**: Dịch sang tiếng Việt: ***„die Besichtigung“***
    * Đáp án chấp nhận: `["sự tham quan", "cuộc tham quan", "buổi tham quan", "chuyến tham quan", "việc tham quan", "tham quan", "chuyến đi tham quan", "buổi đi tham quan", "cuộc đi tham quan"]`
    * Dịch nghĩa câu: *„sự tham quan / cuộc tham quan / buổi tham quan“*
    * Giải thích: `die Besichtigung` xuất phát từ động từ `besichtigen` (tham quan); đuôi `-ung` luôn là `die`.
38. **Câu 38**: Dịch sang tiếng Việt: ***„Es war langweilig.“***
    * Đáp án chấp nhận: `["Nó chán.", "nó chán", "Nó rất chán.", "nó rất chán", "Nó đã chán.", "nó đã chán", "Nó nhàm chán.", "nó nhàm chán", "Nó đã rất nhàm chán.", "nó đã rất nhàm chán", "Nó thật nhàm chán.", "nó thật nhàm chán", "Thật nhàm chán.", "thật nhàm chán", "Rất nhàm chán.", "rất nhàm chán", "Rất chán.", "rất chán", "Chán lắm.", "chán lắm", "Kỳ nghỉ thật nhàm chán.", "kỳ nghỉ thật nhàm chán", "kỳ nghỉ rất chán", "Chuyến đi thật nhàm chán.", "chuyến đi thật nhàm chán", "Chuyến đi rất chán.", "chuyến đi rất chán", "Chuyến đi đã rất chán.", "chuyến đi đã rất chán", "Kỳ nghỉ đã rất chán.", "kỳ nghỉ đã rất chán", "Mọi thứ thật nhàm chán.", "mọi thứ thật nhàm chán", "Mọi thứ rất chán.", "mọi thứ rất chán", "Điều đó thật nhàm chán.", "điều đó thật nhàm chán", "Nó tẻ nhạt.", "nó tẻ nhạt", "Thật tẻ nhạt.", "thật tẻ nhạt", "Rất tẻ nhạt.", "rất tẻ nhạt", "Buồn tẻ.", "buồn tẻ", "Thật buồn tẻ.", "thật buồn tẻ", "Nó buồn tẻ.", "nó buồn tẻ", "Nó đã rất chán.", "nó đã rất chán", "Nó khá chán.", "nó khá chán", "Thật là chán.", "thật là chán", "Thật là nhàm chán.", "thật là nhàm chán", "Nó đã tẻ nhạt.", "nó đã tẻ nhạt", "Kỳ nghỉ tẻ nhạt.", "kỳ nghỉ tẻ nhạt", "Chuyến đi tẻ nhạt.", "chuyến đi tẻ nhạt"]`
    * Dịch nghĩa câu: *„Nó (đã) rất nhàm chán. / Nó chán.“*
    * Giải thích: `es war` là Präteritum của `sein` (*"nó đã là"*), `langweilig` = chán, nhàm chán.
39. **Câu 39**: Dịch sang tiếng Việt: ***„Ich habe Fotos gemacht.“***
    * Đáp án chấp nhận: `["Tôi đã chụp ảnh.", "tôi đã chụp ảnh", "Tôi đã chụp hình.", "tôi đã chụp hình", "Tôi chụp ảnh.", "tôi chụp ảnh", "Tôi chụp hình.", "tôi chụp hình", "Mình đã chụp ảnh.", "mình đã chụp ảnh", "Mình đã chụp hình.", "mình đã chụp hình", "Mình chụp ảnh.", "mình chụp ảnh", "Mình chụp hình.", "mình chụp hình", "Tớ đã chụp ảnh.", "tớ đã chụp ảnh", "Tớ đã chụp hình.", "tớ đã chụp hình", "Tớ chụp ảnh.", "tớ chụp ảnh", "Tớ chụp hình.", "tớ chụp hình", "Tôi đã chụp những bức ảnh.", "tôi đã chụp những bức ảnh", "Tôi đã chụp các bức ảnh.", "tôi đã chụp các bức ảnh", "Tôi đã chụp nhiều ảnh.", "tôi đã chụp nhiều ảnh", "Tôi đã chụp nhiều hình.", "tôi đã chụp nhiều hình", "Tôi đã chụp mấy tấm hình.", "tôi đã chụp mấy tấm hình", "Tôi đã chụp mấy bức ảnh.", "tôi đã chụp mấy bức ảnh", "Tôi đã chụp những tấm ảnh.", "tôi đã chụp những tấm hình", "Mình đã chụp nhiều ảnh.", "mình đã chụp nhiều ảnh", "Mình đã chụp nhiều hình.", "mình đã chụp nhiều hình", "Tôi có chụp ảnh.", "tôi có chụp ảnh", "Tôi vừa chụp ảnh.", "tôi vừa chụp ảnh", "Mình có chụp ảnh.", "mình có chụp ảnh", "Tôi đã chụp được nhiều ảnh.", "tôi đã chụp được nhiều ảnh", "Tôi đã chụp được nhiều bức ảnh.", "tôi đã chụp được nhiều bức ảnh"]`
    * Dịch nghĩa câu: *„Tôi đã chụp ảnh. / Tôi đã chụp hình.“*
    * Giải thích: `Fotos machen` = chụp ảnh; Perfekt `ich habe … gemacht` = *"tôi đã …"*.
40. **Câu 40**: Dịch sang tiếng Việt: ***„Wir sind in den Alpen gewandert.“***
    * Đáp án chấp nhận: `["Chúng tôi đã đi bộ đường dài trên dãy Alps.", "chúng tôi đã đi bộ đường dài trên dãy alps", "Chúng tôi đã đi bộ đường dài ở dãy Alps.", "chúng tôi đã đi bộ đường dài ở dãy alps", "Chúng tôi đã đi bộ đường dài trong dãy Alps.", "chúng tôi đã đi bộ đường dài trong dãy alps", "Chúng tôi đã đi bộ trên dãy Alps.", "chúng tôi đã đi bộ trên dãy alps", "Chúng tôi đã đi bộ ở dãy Alps.", "chúng tôi đã đi bộ ở dãy alps", "Chúng tôi đã đi bộ trong dãy Alps.", "chúng tôi đã đi bộ trong dãy alps", "Chúng tôi đã đi bộ trong dãy Alpen.", "chúng tôi đã đi bộ trong dãy alpen", "Chúng tôi đã đi bộ trên dãy Alpen.", "chúng tôi đã đi bộ trên dãy alpen", "Chúng tôi đã đi bộ ở dãy Alpen.", "chúng tôi đã đi bộ ở dãy alpen", "Chúng tôi đã đi bộ đường dài trên dãy Alpen.", "chúng tôi đã đi bộ đường dài trên dãy alpen", "Chúng tôi đã đi bộ leo núi ở dãy an-pơ.", "chúng tôi đã đi bộ leo núi ở dãy an-pơ", "Chúng tôi đã đi bộ leo núi ở dãy an pơ.", "chúng tôi đã đi bộ leo núi ở dãy an pơ", "Chúng tôi đã đi bộ leo núi trên dãy Alps.", "chúng tôi đã đi bộ leo núi trên dãy alps", "Chúng tôi đã đi bộ leo núi ở dãy Alps.", "chúng tôi đã đi bộ leo núi ở dãy alps", "Chúng tôi đã đi bộ leo núi trong dãy Alps.", "chúng tôi đã đi bộ leo núi trong dãy alps", "Chúng tôi đã leo núi trên dãy Alps.", "chúng tôi đã leo núi trên dãy alps", "Chúng tôi đã leo núi ở dãy Alps.", "chúng tôi đã leo núi ở dãy alps", "Chúng tôi đã đi dạo bộ trên dãy Alps.", "chúng tôi đã đi dạo bộ trên dãy alps", "Chúng tôi đã đi dạo bộ ở dãy Alps.", "chúng tôi đã đi dạo bộ ở dãy alps", "Chúng tôi đã đi phượt bộ trên dãy Alps.", "chúng tôi đã đi phượt bộ trên dãy alps", "Chúng tôi đã đi phượt bộ ở dãy Alps.", "chúng tôi đã đi phượt bộ ở dãy alps", "Chúng tôi đã đi bộ trên núi Alps.", "chúng tôi đã đi bộ trên núi alps", "Chúng tôi đã đi bộ ở núi Alps.", "chúng tôi đã đi bộ ở núi alps", "Chúng tôi đã đi bộ trên núi Alpen.", "chúng tôi đã đi bộ trên núi alpen", "Chúng tôi đã đi bộ ở núi Alpen.", "chúng tôi đã đi bộ ở núi alpen", "Chúng tôi đã đi bộ ở Alps.", "chúng tôi đã đi bộ ở alps", "Chúng tôi đã đi bộ trên Alps.", "chúng tôi đã đi bộ trên alps", "Chúng tôi đã đi bộ đường dài ở Alps.", "chúng tôi đã đi bộ đường dài ở alps", "Chúng tôi đã đi bộ đường dài trên Alps.", "chúng tôi đã đi bộ đường dài trên alps", "Chúng tôi đi bộ trên dãy Alps.", "chúng tôi đi bộ trên dãy alps", "Chúng tôi đi bộ ở dãy Alps.", "chúng tôi đi bộ ở dãy alps", "Chúng tôi đi bộ đường dài trên dãy Alps.", "chúng tôi đi bộ đường dài trên dãy alps", "Chúng tôi đi bộ đường dài ở dãy Alps.", "chúng tôi đi bộ đường dài ở dãy alps", "Chúng mình đã đi bộ trên dãy Alps.", "chúng mình đã đi bộ trên dãy alps", "Chúng mình đã đi bộ ở dãy Alps.", "chúng mình đã đi bộ ở dãy alps", "Chúng mình đã đi bộ đường dài trên dãy Alps.", "chúng mình đã đi bộ đường dài trên dãy alps", "Tụi mình đã đi bộ trên dãy Alps.", "tụi mình đã đi bộ trên dãy alps", "Bọn mình đã đi bộ trên dãy Alps.", "bọn mình đã đi bộ trên dãy alps", "Chúng ta đã đi bộ trên dãy Alps.", "chúng ta đã đi bộ trên dãy alps"]`
    * Dịch nghĩa câu: *„Chúng tôi đã đi bộ (đường dài / leo núi) trên dãy Alps.“*
    * Giải thích: `wandern` = đi bộ đường dài (dùng `sein`); `in den Alpen` = ở / trong dãy Alps.
41. **Câu 41**: Dịch sang tiếng Việt: ***„Das Wetter war prima.“***
    * Đáp án chấp nhận: `["thời tiết thật tuyệt", "thời tiết thật tuyệt.", "thời tiết rất tuyệt", "thời tiết rất tuyệt.", "thời tiết tuyệt vời", "thời tiết tuyệt vời.", "thời tiết rất tuyệt vời", "thời tiết rất tuyệt vời.", "thời tiết đã rất tuyệt", "thời tiết đã rất tuyệt.", "thời tiết rất tốt", "thời tiết rất tốt.", "thời tiết đã rất tốt", "thời tiết đã rất tốt.", "thời tiết rất đẹp", "thời tiết rất đẹp.", "thời tiết thật đẹp", "thời tiết thật đẹp.", "thời tiết quá tuyệt", "thời tiết quá tuyệt.", "thời tiết cực đẹp", "thời tiết cực đẹp.", "thời tiết đã thật tuyệt", "thời tiết thật là tuyệt", "thời tiết đã rất đẹp", "thời tiết cực kỳ đẹp", "thời tiết quá đẹp", "thời tiết đã tuyệt vời", "thời tiết tốt lắm", "thời tiết đẹp lắm", "thời tiết tuyệt lắm"]`
    * Dịch nghĩa câu: *„Thời tiết (đã) rất tuyệt vời / rất tốt / rất đẹp.“*
    * Giải thích: `das Wetter` (thời tiết) + `war` (Präteritum của `sein`) + `prima` (rất tốt, tuyệt).
42. **Câu 42**: Dịch sang tiếng Việt: ***„Was ist passiert?“***
    * Đáp án chấp nhận: `["chuyện gì đã xảy ra", "chuyện gì đã xảy ra?", "chuyện gì đã xảy ra vậy", "chuyện gì đã xảy ra vậy?", "chuyện gì đã xảy ra thế", "chuyện gì đã xảy ra thế?", "chuyện gì xảy ra vậy", "chuyện gì xảy ra vậy?", "chuyện gì xảy ra thế", "chuyện gì xảy ra thế?", "điều gì đã xảy ra", "điều gì đã xảy ra?", "điều gì đã xảy ra vậy", "điều gì đã xảy ra vậy?", "điều gì xảy ra vậy", "điều gì xảy ra vậy?", "có chuyện gì đã xảy ra", "có chuyện gì đã xảy ra?", "có chuyện gì xảy ra vậy", "có chuyện gì xảy ra vậy?", "có chuyện gì thế", "có chuyện gì thế?", "có chuyện gì vậy", "có chuyện gì vậy?", "việc gì đã xảy ra", "việc gì đã xảy ra?", "việc gì xảy ra vậy", "việc gì xảy ra vậy?", "cái gì đã xảy ra", "cái gì đã xảy ra?", "cái gì đã xảy ra vậy", "cái gì đã xảy ra vậy?", "chuyện gì thế", "chuyện gì thế?"]`
    * Dịch nghĩa câu: *„Chuyện gì đã xảy ra (vậy)? / Điều gì đã xảy ra?“*
    * Giải thích: `passieren` (xảy ra) dùng `sein` → `es ist passiert`; câu hỏi `Was ist passiert?`.

---

#### NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (`noi_o` — 8 Bài: Câu 43 → Câu 50, mỗi bài 4 cặp độc nhất)
43. **Câu 43 (Bài nối 1 — Infinitiv ↔ Partizip II, động từ có quy tắc)**:
    * `machen` ↔ `gemacht`
    * `arbeiten` ↔ `gearbeitet`
    * `studieren` ↔ `studiert`
    * `bezahlen` ↔ `bezahlt`
    * Giải thích: `machen` (nhóm 1: `ge-t`), `arbeiten` (nhóm 2: `ge-et`), `studieren` (nhóm 3: `-ieren`, không `ge-`), `bezahlen` (nhóm 4: `be-`, không `ge-`).
44. **Câu 44 (Bài nối 2 — Infinitiv ↔ Partizip II, bất quy tắc dùng `haben`)**:
    * `essen` ↔ `gegessen`
    * `trinken` ↔ `getrunken`
    * `schreiben` ↔ `geschrieben`
    * `sehen` ↔ `gesehen`
    * Giải thích: Bốn động từ bất quy tắc có dạng `ge- … -en` (`trinken` đổi `i → u`, `schreiben` đổi `ei → ie`).
45. **Câu 45 (Bài nối 3 — Infinitiv ↔ Perfekt dùng `sein`)**:
    * `fahren` ↔ `ist gefahren`
    * `fliegen` ↔ `ist geflogen`
    * `bleiben` ↔ `ist geblieben`
    * `laufen` ↔ `ist gelaufen`
    * Giải thích: Cả bốn động từ đều chỉ chuyển động đổi vị trí hoặc `bleiben` nên dùng **`sein`**.
46. **Câu 46 (Bài nối 4 — Động từ tách ↔ Partizip II)**:
    * `einkaufen` ↔ `eingekauft`
    * `anschauen` ↔ `angeschaut`
    * `aufstehen` ↔ `aufgestanden`
    * `mitnehmen` ↔ `mitgenommen`
    * Giải thích: Động từ tách chèn `ge` giữa tiền tố và gốc: `ein` + `ge` + `kauft`, `an` + `ge` + `schaut`, `auf` + `ge` + `standen`, `mit` + `ge` + `nommen`.
47. **Câu 47 (Bài nối 5 — Quy tắc ↔ Ví dụ)**:
    * `ge + gốc + t` ↔ `spielen → gespielt`
    * `ge + gốc + et (gốc đuôi -t)` ↔ `warten → gewartet`
    * `đuôi -ieren, không ge-` ↔ `reservieren → reserviert`
    * `tiền tố không tách, không ge-` ↔ `erleben → erlebt`
    * Giải thích: Bốn quy tắc đầu của Partizip II (nhóm 1, 2, 3, 4).
48. **Câu 48 (Bài nối 6 — Câu hỏi về kỳ nghỉ ↔ Câu trả lời phù hợp)**:
    * `Wo warst du im Urlaub?` ↔ `Ich war auf der Insel Phú Quốc.`
    * `Wie war das Hotel?` ↔ `Es war sauber und gemütlich.`
    * `Was hast du gemacht?` ↔ `Ich habe viele Fotos gemacht.`
    * `Wie bist du gefahren?` ↔ `Ich bin mit dem Zug gefahren.`
    * Giải thích: Câu hỏi `Wo`, `Wie war`, `Was`, `Wie` phải được đáp bằng câu cùng loại thông tin (nơi chốn, tính chất, hành động, phương tiện).
49. **Câu 49 (Bài nối 7 — Danh từ ↔ Động từ đi cặp, `Kollokation`)**:
    * `ein Hotel` ↔ `buchen`
    * `den Koffer` ↔ `packen`
    * `ein Schloss` ↔ `besichtigen`
    * `ein Picknick` ↔ `machen`
    * Giải thích: `ein Hotel buchen` (đặt khách sạn), `den Koffer packen` (đóng vali), `ein Schloss besichtigen` (tham quan lâu đài), `ein Picknick machen` (đi dã ngoại).
50. **Câu 50 (Bài nối 8 — Ngôi ↔ Dạng Präteritum)**:
    * `ich (sein)` ↔ `war`
    * `du (sein)` ↔ `warst`
    * `ihr (haben)` ↔ `hattet`
    * `wir (haben)` ↔ `hatten`
    * Giải thích: `ich war`, `du warst`, `ihr hattet`, `wir hatten`.

---

#### NHÓM 6: ĐIỀN VÀO 2 CHỖ TRỐNG TẠO CÂU (`dien_tao_cau` — 8 Câu: Câu 51 → Câu 58)
51. **Câu 51**: Điền 2 từ để hoàn thành câu: *„Hôm qua tôi đã tham quan viện bảo tàng và chụp ảnh.“*
    * Khung câu hiển thị: `Gestern [1] ich das Museum [2] und Fotos gemacht.`
    * Đáp án từng ô: Ô 1 = `["habe"]`, Ô 2 = `["besichtigt"]`.
    * Giải thích: `ich` → `habe`; `besichtigen` (tiền tố `be-`) → **`besichtigt`**.
52. **Câu 52**: Điền 2 từ để hoàn thành câu: *„Chúng tôi đã đi bằng tàu hỏa đến Hamburg.“*
    * Khung câu hiển thị: `Wir [1] mit dem Zug nach Hamburg [2].`
    * Đáp án từng ô: Ô 1 = `["sind"]`, Ô 2 = `["gefahren"]`.
    * Giải thích: `fahren` chuyển động → `sein`; `wir` → **`sind`**; Partizip II **`gefahren`**.
53. **Câu 53**: Điền 2 từ để hoàn thành câu: *„Linh đã ở lại Hội An hai tuần.“*
    * Khung câu hiển thị: `Linh [1] zwei Wochen in Hội An [2].`
    * Đáp án từng ô: Ô 1 = `["ist"]`, Ô 2 = `["geblieben"]`.
    * Giải thích: `bleiben` luôn dùng `sein`; `Linh` = `sie` → **`ist`**; Partizip II **`geblieben`**.
54. **Câu 54**: Điền 2 từ để hoàn thành câu hỏi: *„Các bạn đã ngủ ngon chứ?“*
    * Khung câu hiển thị: `[1] ihr gut [2]?`
    * Đáp án từng ô: Ô 1 = `["habt"]`, Ô 2 = `["geschlafen"]`.
    * Giải thích: Câu hỏi Ja/Nein bắt đầu bằng trợ động từ; `ihr` → **`habt`**; `schlafen` → **`geschlafen`**.
55. **Câu 55**: Điền 2 Partizip II để hoàn thành câu: *„Tôi đã đặt phòng và đã trả tiền.“*
    * Khung câu hiển thị: `Ich habe das Zimmer [1] und [2].`
    * Đáp án từng ô: Ô 1 = `["gebucht"]`, Ô 2 = `["bezahlt"]`.
    * Giải thích: `buchen` → **`gebucht`**; `bezahlen` (tiền tố `be-`) → **`bezahlt`**.
56. **Câu 56**: Điền 2 dạng Präteritum của `sein` để hoàn thành câu: *„Hôm qua thời tiết rất tốt, và chúng tôi đã ở bãi biển.“*
    * Khung câu hiển thị: `Das Wetter [1] gestern sehr gut, und wir [2] am Strand.`
    * Đáp án từng ô: Ô 1 = `["war"]`, Ô 2 = `["waren"]`.
    * Giải thích: `das Wetter` = `es` → **`war`**; `wir` → **`waren`**.
57. **Câu 57**: Điền 2 từ để hoàn thành câu: *„Anna đã đóng vali của mình rồi sau đó đã đi đến nhà ga.“*
    * Khung câu hiển thị: `Anna [1] ihren Koffer [2] und ist dann zum Bahnhof gegangen.`
    * Đáp án từng ô: Ô 1 = `["hat"]`, Ô 2 = `["gepackt"]`.
    * Giải thích: `packen` có tân ngữ `den Koffer` → `haben`; `Anna` = `sie` → **`hat`**; Partizip II **`gepackt`**.
58. **Câu 58**: Điền 2 từ để hoàn thành câu: *„Họ đã gặp những người bạn mới và đã nói chuyện nhiều.“*
    * Khung câu hiển thị: `Sie [1] neue Freunde [2] und viel gesprochen.` *(Sie = họ)*
    * Đáp án từng ô: Ô 1 = `["haben"]`, Ô 2 = `["getroffen"]`.
    * Giải thích: `sie` (họ, số nhiều) → **`haben`**; `treffen` bất quy tắc → **`getroffen`**.

---

#### NHÓM 7: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 8 Câu: Câu 59 → Câu 66)
59. **Câu 59**:
    * `audio_text`: *"Meine Eltern sind letzte Woche nach Italien geflogen."*
    * `display_sentence`: *"Meine Eltern sind letzte Woche nach Italien ___."*
    * `hint_vi`: *"Bố mẹ tôi đã bay đến Ý vào tuần trước."*
    * `accepted_answers`: `["geflogen"]`
    * Giải thích: `fliegen → ist geflogen`.
60. **Câu 60**:
    * `audio_text`: *"Im Sommer haben wir zwei Nächte am See gezeltet."*
    * `display_sentence`: *"Im Sommer haben wir zwei Nächte am See ___."*
    * `hint_vi`: *"Vào mùa hè chúng tôi đã cắm trại hai đêm bên hồ."*
    * `accepted_answers`: `["gezeltet"]`
    * Giải thích: Gốc `zelt` kết thúc `-t` → **`gezeltet`**.
61. **Câu 61**:
    * `audio_text`: *"Ich habe das Hotel im Internet gebucht."*
    * `display_sentence`: *"Ich habe das Hotel im Internet ___."*
    * `hint_vi`: *"Tôi đã đặt khách sạn trên mạng."*
    * `accepted_answers`: `["gebucht"]`
    * Giải thích: `buchen → gebucht`.
62. **Câu 62**:
    * `audio_text`: *"Der Bus ist um neun Uhr abgefahren."*
    * `display_sentence`: *"Der Bus ist um neun Uhr ___."*
    * `hint_vi`: *"Chiếc xe buýt đã khởi hành lúc chín giờ."*
    * `accepted_answers`: `["abgefahren"]`
    * Giải thích: `abfahren` (tách) → `ab` + `ge` + `fahren` = **`abgefahren`**, dùng `sein`.
63. **Câu 63**:
    * `audio_text`: *"Wo wart ihr im Sommer? Wir waren in den Alpen."*
    * `display_sentence`: *"Wo ___ ihr im Sommer? Wir waren in den Alpen."*
    * `hint_vi`: *"Vào mùa hè các bạn đã ở đâu? Chúng tôi đã ở dãy Alps."*
    * `accepted_answers`: `["wart"]`
    * Giải thích: `ihr` + Präteritum của `sein` = **`wart`**.
64. **Câu 64**:
    * `audio_text`: *"Am Abend haben wir die Nudelsuppe probiert."*
    * `display_sentence`: *"Am Abend haben wir die Nudelsuppe ___."*
    * `hint_vi`: *"Buổi tối chúng tôi đã thử món súp mì."*
    * `accepted_answers`: `["probiert"]`
    * Giải thích: Đuôi `-ieren` → không `ge-`: **`probiert`**.
65. **Câu 65**:
    * `audio_text`: *"Was ist denn passiert? Mein Koffer ist nicht angekommen!"*
    * `display_sentence`: *"Was ist denn ___? Mein Koffer ist nicht angekommen!"*
    * `hint_vi`: *"Chuyện gì đã xảy ra vậy? Vali của tôi đã không đến nơi!"*
    * `accepted_answers`: `["passiert"]`
    * Giải thích: `passieren` đuôi `-ieren` → **`passiert`** (dùng `sein`: `ist passiert`).
66. **Câu 66**:
    * `audio_text`: *"Nach dem Frühstück haben wir den Reiseführer gelesen."*
    * `display_sentence`: *"Nach dem Frühstück haben wir den Reiseführer ___."*
    * `hint_vi`: *"Sau bữa sáng chúng tôi đã đọc cuốn sách hướng dẫn du lịch."*
    * `accepted_answers`: `["gelesen"]`
    * Giải thích: `lesen` bất quy tắc: **`gelesen`**.

---

#### NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (`dich_cau_vd` — 6 Câu: Câu 67 → Câu 72, chấm đa đáp án)
67. **Câu 67**: Dịch câu sau sang tiếng Đức: ***"Mùa hè năm ngoái tôi đã đi du lịch đến Berlin."***
    * `accepted_answers`:
      * `"Letzten Sommer bin ich nach Berlin gereist."`
      * `"Ich bin letzten Sommer nach Berlin gereist."`
      * `"Im letzten Sommer bin ich nach Berlin gereist."`
      * `"Letzten Sommer bin ich nach Berlin gefahren."`
      * `"Ich bin letzten Sommer nach Berlin gefahren."`
    * Giải thích: `reisen` / `fahren` đều là di chuyển → **`ich bin … gereist / gefahren`**; trạng từ thời gian ở đầu câu thì đảo `bin ich`.
68. **Câu 68**: Dịch câu sau sang tiếng Đức: ***"Gia đình tôi đã ở qua đêm trong một khách sạn nhỏ và đã ăn nhiều cá."***
    * `accepted_answers`:
      * `"Meine Familie hat in einem kleinen Hotel übernachtet und viel Fisch gegessen."`
      * `"Meine Familie hat in einem kleinen Hotel übernachtet und hat viel Fisch gegessen."`
    * Giải thích: `übernachten → übernachtet`, `essen → gegessen`; cả hai dùng `haben` nên `hat` chỉ cần xuất hiện một lần.
69. **Câu 69**: Dịch câu hỏi sau sang tiếng Đức: ***"Bạn đã làm gì vào cuối tuần, Tom?"***
    * `accepted_answers`:
      * `"Was hast du am Wochenende gemacht, Tom?"`
      * `"Tom, was hast du am Wochenende gemacht?"`
      * `"Was hast du am Wochenende gemacht?"`
    * Giải thích: W-Frage: `Was` + `hast` (vị trí 2) + `du` + … + `gemacht` (cuối câu).
70. **Câu 70**: Dịch câu sau sang tiếng Đức: ***"Hôm qua trời đã mưa cả ngày, nhưng buổi tối thì tuyệt."***
    * `accepted_answers`:
      * `"Gestern hat es den ganzen Tag geregnet, aber der Abend war toll."`
      * `"Gestern hat es den ganzen Tag geregnet, aber der Abend war super."`
      * `"Gestern hat es den ganzen Tag geregnet, aber der Abend war schön."`
    * Giải thích: `regnen → hat geregnet` (ngôi `es`); `der Abend war toll` dùng Präteritum của `sein`.
71. **Câu 71**: Dịch câu sau sang tiếng Đức: ***"Chúng tôi đã không ở lại bãi biển lâu."***
    * `accepted_answers`:
      * `"Wir sind nicht lange am Strand geblieben."`
      * `"Wir sind am Strand nicht lange geblieben."`
    * Giải thích: `bleiben → sind … geblieben`; `nicht` đứng trước `lange`.
72. **Câu 72**: Dịch câu sau sang tiếng Đức: ***"Tối qua em gái tôi đã gọi điện cho tôi."***
    * `accepted_answers`:
      * `"Meine Schwester hat mich gestern Abend angerufen."`
      * `"Gestern Abend hat mich meine Schwester angerufen."`
      * `"Gestern Abend hat meine Schwester mich angerufen."`
    * Giải thích: `anrufen` (tách, bất quy tắc) → `hat … angerufen`; `mich` (tôi, Akkusativ).

---

#### NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (`dich_cau_dv` — 6 Câu: Câu 73 → Câu 78, chấm đa đáp án)
73. **Câu 73**: Dịch câu sau sang tiếng Việt: ***„Letzten Winter sind wir nach Österreich gefahren. Dort hat es viel geschneit.“***
    * `accepted_answers`:
      * `"Mùa đông năm ngoái chúng tôi đã đi Áo. Ở đó tuyết đã rơi nhiều."`
      * `"Mùa đông năm ngoái chúng tôi đã đến nước Áo. Ở đó đã có nhiều tuyết rơi."`
    * Giải thích: `sind … gefahren` (chuyển động); `es hat geschneit` = tuyết đã rơi.
74. **Câu 74**: Dịch câu sau sang tiếng Việt: ***„Ich habe mein Handy im Hotel vergessen, und jetzt muss ich zurückfahren.“***
    * `accepted_answers`:
      * `"Tôi đã quên điện thoại trong khách sạn và bây giờ tôi phải quay lại."`
      * `"Tôi đã để quên điện thoại ở khách sạn, giờ tôi phải quay lại."`
    * Giải thích: `vergessen → hat vergessen`; `muss … zurückfahren` = phải quay lại.
75. **Câu 75**: Dịch câu sau sang tiếng Việt: ***„Wo wart ihr denn gestern? Wir haben euch angerufen, aber ihr habt nicht geantwortet.“***
    * `accepted_answers`:
      * `"Hôm qua các bạn đã ở đâu vậy? Chúng tôi đã gọi cho các bạn nhưng các bạn đã không trả lời."`
      * `"Hôm qua các bạn ở đâu thế? Chúng mình đã gọi điện cho các bạn nhưng các bạn không trả lời."`
    * Giải thích: `wart` (Präteritum `sein`, `ihr`); `angerufen`; `geantwortet` (gốc `-t` → `-et`), ở đây phủ định `nicht geantwortet`.
76. **Câu 76**: Dịch câu sau sang tiếng Việt: ***„Die Reise war lang, aber schön. Wir sind mit dem Schiff gefahren und haben viele Inseln gesehen.“***
    * `accepted_answers`:
      * `"Chuyến đi dài nhưng đẹp. Chúng tôi đã đi bằng tàu thủy và đã nhìn thấy nhiều hòn đảo."`
      * `"Chuyến đi dài nhưng rất đẹp. Chúng tôi đã đi tàu thủy và đã thấy nhiều hòn đảo."`
    * Giải thích: `war` (Präteritum `sein`); `sind … gefahren`; `haben … gesehen`.
77. **Câu 77**: Dịch câu sau sang tiếng Việt: ***„Mein Opa hat früher in einem Dorf in den Bergen gewohnt.“***
    * `accepted_answers`:
      * `"Ông tôi ngày trước đã sống trong một ngôi làng trên núi."`
      * `"Ngày xưa ông tôi đã sống trong một ngôi làng ở trên núi."`
    * Giải thích: `früher` = ngày trước; `wohnen → hat gewohnt` (trạng thái tại chỗ → `haben`).
78. **Câu 78**: Dịch đoạn hội thoại sau sang tiếng Việt: ***„Hast du schon den Koffer gepackt? — Nein, noch nicht. Ich habe zuerst die Fahrkarten gekauft.“***
    * `accepted_answers`:
      * `"Bạn đã đóng vali chưa? — Chưa, chưa đâu. Trước tiên tôi đã mua vé."`
      * `"Bạn đã đóng vali chưa? — Chưa, vẫn chưa. Đầu tiên tôi đã mua vé tàu."`
    * Giải thích: `schon` = đã … rồi; `noch nicht` = chưa; `gepackt`, `gekauft` là Partizip II có quy tắc.

---

#### NHÓM 10: 🆕 SẮP XẾP TỪ THÀNH CÂU (`sap_xep_cau` — 6 Câu: Câu 79 → Câu 84)
79. **Câu 79**
    * `tokens` (đã xáo trộn): `[geschrieben, ich, Gestern, Postkarten, habe]`
    * `accepted_answers`: `["Gestern habe ich Postkarten geschrieben.", "Ich habe gestern Postkarten geschrieben."]`
    * Dịch nghĩa câu: *„Hôm qua tôi đã viết bưu thiếp.“*
    * Giải thích: Có thể mở đầu bằng `Gestern` (khi đó `habe` ở vị trí 2, `ich` đứng sau) hoặc bằng `Ich`; `geschrieben` luôn ở cuối.
80. **Câu 80**
    * `tokens`: `[gefahren, nach Köln, Wir, am Wochenende, sind]`
    * `accepted_answers`: `["Wir sind am Wochenende nach Köln gefahren.", "Am Wochenende sind wir nach Köln gefahren."]`
    * Dịch nghĩa câu: *„Cuối tuần chúng tôi đã đi Köln.“*
    * Giải thích: `sind` ở vị trí 2, `gefahren` ở cuối câu; `am Wochenende` có thể đứng đầu câu (đảo ngữ).
81. **Câu 81**
    * `tokens`: `[gespielt, Die Kinder, im Meer, haben]`
    * `accepted_answers`: `["Die Kinder haben im Meer gespielt.", "Im Meer haben die Kinder gespielt."]`
    * Dịch nghĩa câu: *„Bọn trẻ đã chơi dưới biển.“*
    * Giải thích: `haben` ở vị trí 2; `gespielt` cuối câu.
82. **Câu 82** *(phủ định)*
    * `tokens`: `[gegangen, nicht, Wir, ins Museum, sind]`
    * `accepted_answers`: `["Wir sind nicht ins Museum gegangen."]`
    * Dịch nghĩa câu: *„Chúng tôi đã không đi vào viện bảo tàng.“*
    * Giải thích: `nicht` đứng trước bổ ngữ chỉ hướng `ins Museum`; `gegangen` ở cuối câu.
83. **Câu 83** *(câu hỏi Ja/Nein)*
    * `tokens`: `[gemacht, du, Hast, viele Fotos, im Urlaub]`
    * `accepted_answers`: `["Hast du im Urlaub viele Fotos gemacht?", "Hast du viele Fotos im Urlaub gemacht?"]`
    * Dịch nghĩa câu: *„Bạn đã chụp nhiều ảnh trong kỳ nghỉ chứ?“*
    * Giải thích: Câu hỏi Ja/Nein bắt đầu bằng trợ động từ `Hast`, tiếp theo là `du`; `gemacht` cuối câu.
84. **Câu 84** *(động từ tách)*
    * `tokens`: `[angekommen, Die Gäste, um zehn Uhr, sind]`
    * `accepted_answers`: `["Die Gäste sind um zehn Uhr angekommen.", "Um zehn Uhr sind die Gäste angekommen."]`
    * Dịch nghĩa câu: *„Các vị khách đã đến nơi lúc mười giờ.“*
    * Giải thích: `ankommen` dùng `sein`; Partizip II **`angekommen`** nằm cuối câu.

---

#### NHÓM 11: 🆕 PHÂN LOẠI `HABEN` / `SEIN` (`chon_haben_sein` — 4 Câu: Câu 85 → Câu 88, kèm sơ đồ `visual: V3`)
Mỗi câu: xếp **4 động từ** vào đúng trợ động từ. Đúng khi cả 4 đều đúng.
85. **Câu 85**: Xếp các động từ sau:
    * `fahren` (đi xe) → **sein** (`ist gefahren`)
    * `machen` (làm) → **haben** (`hat gemacht`)
    * `bleiben` (ở lại) → **sein** (`ist geblieben`)
    * `essen` (ăn) → **haben** (`hat gegessen`)
    * Giải thích: `fahren` chuyển động; `bleiben` là một trong ba động từ `sein/bleiben/werden`; `machen` và `essen` có tân ngữ nên dùng `haben`.
86. **Câu 86**: Xếp các động từ sau:
    * `einschlafen` (ngủ thiếp đi) → **sein** (`ist eingeschlafen`)
    * `schlafen` (ngủ) → **haben** (`hat geschlafen`)
    * `fliegen` (bay) → **sein** (`ist geflogen`)
    * `fotografieren` (chụp ảnh) → **haben** (`hat fotografiert`)
    * Giải thích: `einschlafen` đổi trạng thái; `schlafen` là trạng thái kéo dài; `fliegen` chuyển động; `fotografieren` có tân ngữ.
87. **Câu 87**: Xếp các động từ sau:
    * `übernachten` (qua đêm) → **haben** (`hat übernachtet`)
    * `wandern` (đi bộ đường dài) → **sein** (`ist gewandert`)
    * `aufwachen` (thức dậy) → **sein** (`ist aufgewacht`)
    * `besichtigen` (tham quan) → **haben** (`hat besichtigt`)
    * Giải thích: `wandern` chuyển động; `aufwachen` đổi trạng thái; `übernachten` (tại chỗ) và `besichtigen` (có tân ngữ) dùng `haben`.
88. **Câu 88**: Xếp các động từ sau:
    * `passieren` (xảy ra) → **sein** (`ist passiert`)
    * `bezahlen` (trả tiền) → **haben** (`hat bezahlt`)
    * `kommen` (đến) → **sein** (`ist gekommen`)
    * `regnen` (mưa) → **haben** (`hat geregnet`)
    * Giải thích: `passieren` và `kommen` dùng `sein`; `bezahlen` có tân ngữ; `regnen` là động từ thời tiết dùng `haben`.

---

#### NHÓM 12: 🆕 TÌM LỖI VÀ SỬA CÂU (`tim_loi_sai` — 4 Câu: Câu 89 → Câu 92)
Mỗi câu có **đúng 1 lỗi**. Người học gõ lại **cả câu đúng**.
89. **Câu 89** *(lỗi `hilfsverb`)*
    * `wrong_sentence`: *„Wir haben gestern nach Berlin gefahren.“*
    * `accepted_answers`: `["Wir sind gestern nach Berlin gefahren.", "Gestern sind wir nach Berlin gefahren."]`
    * Dịch nghĩa câu đúng: *„Hôm qua chúng tôi đã đi Berlin.“*
    * Giải thích: Lỗi **trợ động từ**: `fahren` là chuyển động đổi vị trí nên phải dùng **`sind`**, không phải `haben`.
90. **Câu 90** *(lỗi `partizip`)*
    * `wrong_sentence`: *„Ich habe im Urlaub viele Fotos gemachen.“*
    * `accepted_answers`: `["Ich habe im Urlaub viele Fotos gemacht."]`
    * Dịch nghĩa câu đúng: *„Tôi đã chụp nhiều ảnh trong kỳ nghỉ.“*
    * Giải thích: Lỗi **Partizip II**: động từ có quy tắc là `ge` + gốc + `t` = **`gemacht`**, không phải `gemachen`.
91. **Câu 91** *(lỗi `wortstellung`)*
    * `wrong_sentence`: *„Sie hat ein Picknick gemacht am Fluss.“*
    * `accepted_answers`: `["Sie hat am Fluss ein Picknick gemacht.", "Sie hat ein Picknick am Fluss gemacht."]`
    * Dịch nghĩa câu đúng: *„Cô ấy đã dã ngoại bên sông.“*
    * Giải thích: Lỗi **vị trí động từ**: `gemacht` (Partizip II) phải đứng **cuối câu**, sau cả cụm `am Fluss`.
92. **Câu 92** *(lỗi `partizip`)*
    * `wrong_sentence`: *„Wir haben die Rechnung gebezahlt.“*
    * `accepted_answers`: `["Wir haben die Rechnung bezahlt."]`
    * Dịch nghĩa câu đúng: *„Chúng tôi đã trả hóa đơn.“*
    * Giải thích: Lỗi **Partizip II**: `bezahlen` có tiền tố `be-` không tách nên **không có `ge-`** → **`bezahlt`**.

---

#### NHÓM 13: 🆕 VIẾT LẠI CÂU TỪ PRÄSENS SANG PERFEKT (`viet_lai_perfekt` — 4 Câu: Câu 93 → Câu 96)
93. **Câu 93**
    * `source_sentence`: *„Ich besuche meine Tante in Bremen.“*
    * `accepted_answers`: `["Ich habe meine Tante in Bremen besucht."]`
    * Dịch nghĩa câu Perfekt: *„Tôi đã thăm dì của tôi ở Bremen.“*
    * Giải thích: `besuchen` → `haben` + **`besucht`** (tiền tố `be-`, không `ge-`), Partizip II đứng cuối câu.
94. **Câu 94**
    * `source_sentence`: *„Maria fährt mit dem Rad zum See.“*
    * `accepted_answers`: `["Maria ist mit dem Rad zum See gefahren."]`
    * Dịch nghĩa câu Perfekt: *„Maria đã đạp xe đến hồ.“*
    * Giải thích: `fahren` chuyển động → `ist` + **`gefahren`**.
95. **Câu 95**
    * `source_sentence`: *„Die Gäste steigen in Köln aus.“*
    * `accepted_answers`: `["Die Gäste sind in Köln ausgestiegen."]`
    * Dịch nghĩa câu Perfekt: *„Các vị khách đã xuống xe ở Köln.“*
    * Giải thích: `aussteigen` (tách, chuyển động) → `sind` + `aus` + `ge` + `stiegen` = **`ausgestiegen`**.
96. **Câu 96**
    * `source_sentence`: *„Ihr reserviert den Tisch und telefoniert mit dem Hotel.“*
    * `accepted_answers`: `["Ihr habt den Tisch reserviert und mit dem Hotel telefoniert.", "Ihr habt den Tisch reserviert und habt mit dem Hotel telefoniert."]`
    * Dịch nghĩa câu Perfekt: *„Các bạn đã đặt bàn và đã gọi điện cho khách sạn.“*
    * Giải thích: Hai động từ đuôi `-ieren` → không `ge-`: **`reserviert`**, **`telefoniert`**; `ihr` → `habt`.

---

#### NHÓM 14: 🆕 ĐỌC HIỂU ĐÚNG / SAI — RICHTIG / FALSCH (`dung_sai` — 4 Câu: Câu 97 → Câu 100)
**Đoạn văn A** *(dùng cho Câu 97 và 98, kèm `visual: route_donau` tô sáng Passau → Linz → Wien)*:
> *„Familie Weber hat im August eine Radtour an der Donau gemacht. Sie sind von Passau nach Wien gefahren. Das Wetter war meistens sonnig, aber in Linz hat es zwei Tage geregnet. Sie haben dort in einer Pension übernachtet und ein Museum besucht. In Wien haben sie das Rathaus fotografiert. Am Ende sind sie mit dem Zug nach Hause gefahren.“*
> **Dịch**: *„Gia đình Weber đã đi một chuyến đạp xe dọc sông Donau vào tháng Tám. Họ đã đi từ Passau đến Wien. Thời tiết phần lớn là nắng, nhưng ở Linz trời đã mưa hai ngày. Họ đã ngủ lại ở đó trong một nhà nghỉ và thăm một bảo tàng. Ở Wien họ đã chụp ảnh tòa thị chính. Cuối cùng họ đã đi tàu hỏa về nhà.“*

97. **Câu 97**: Mệnh đề: *„Familie Weber ist mit dem Auto nach Wien gefahren.“*
    * Đáp án: **Falsch (Sai)**
    * Dịch nghĩa mệnh đề: *„Gia đình Weber đã đi Wien bằng ô tô.“*
    * Giải thích: Trong đoạn văn: *„Familie Weber hat … eine Radtour an der Donau gemacht.“* — họ đi **bằng xe đạp** (`Radtour`), không đi ô tô.
98. **Câu 98**: Mệnh đề: *„In Linz hat es geregnet.“*
    * Đáp án: **Richtig (Đúng)**
    * Dịch nghĩa mệnh đề: *„Ở Linz trời đã mưa.“*
    * Giải thích: Đoạn văn viết *„… aber in Linz hat es zwei Tage geregnet.“*

**Đoạn văn B** *(dùng cho Câu 99 và 100)*:
> *„Hallo Tom, ich bin wieder zu Hause. Der Urlaub in Spanien war super! Wir waren eine Woche in Barcelona. Das Hotel war klein, aber sehr sauber. Wir haben viel gegessen, getanzt und am Strand gelegen. Nur das Essen war manchmal zu scharf.“*
> **Dịch**: *„Chào Tom, mình đã về nhà rồi. Kỳ nghỉ ở Tây Ban Nha thật tuyệt! Chúng mình đã ở Barcelona một tuần. Khách sạn nhỏ nhưng rất sạch. Chúng mình đã ăn nhiều, đã nhảy và đã nằm ở bãi biển. Chỉ có đồ ăn đôi khi quá cay.“*

99. **Câu 99**: Mệnh đề: *„Sie waren zwei Wochen in Barcelona.“*
    * Đáp án: **Falsch (Sai)**
    * Dịch nghĩa mệnh đề: *„Họ đã ở Barcelona hai tuần.“*
    * Giải thích: Đoạn văn viết *„Wir waren eine Woche in Barcelona.“* — chỉ **một tuần**.
100. **Câu 100**: Mệnh đề: *„Sie haben viel gegessen und getanzt.“*
     * Đáp án: **Richtig (Đúng)**
     * Dịch nghĩa mệnh đề: *„Họ đã ăn nhiều và đã nhảy.“*
     * Giải thích: Đoạn văn viết *„Wir haben viel gegessen, getanzt und am Strand gelegen.“*

---
