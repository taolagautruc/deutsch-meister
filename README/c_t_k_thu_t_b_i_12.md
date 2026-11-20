# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: BÀI 12 (A1) "KÖRPER UND GESUNDHEIT — CƠ THỂ, SỨC KHỎE, ĐẠI TỪ AKKUSATIV, DÜRFEN & IMPERATIV" — TÍCH HỢP SƠ ĐỒ TƯƠNG TÁC, BỘ DỮ LIỆU NGUỒN CHUẨN & 125 BÀI TẬP ĐỘC NHẤT (`DEUTSCHMEISTER`)

> **CHỈ THỊ TỐI CAO & CAM KẾT CHẤT LƯỢNG BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
>
> ### 🛡️ 1. NGUYÊN TẮC BẤT KHẢ XÂM PHẠM DỮ LIỆU CŨ (`ZERO MODIFICATION ON EXISTING LESSONS`)
> * **Tuyệt đối KHÔNG được xóa, chỉnh sửa, rút gọn hay ghi đè** bất kỳ bài học nào đã hoàn thành trước đó (**Bài 1 P1** → **Bài 11**), cũng như dữ liệu hiện có trong **Tab Chia động từ (`verbs_db.js`)**, **Tab Từ vựng & Giống (`lexikon_db.js`)** và **Hệ thống Đấu trường (`arena_generator.py`)**.
> * Công việc của lần nâng cấp này chỉ gồm: **(1)** tạo mới hoàn toàn **Bài 12 (`lessons/a1/seed_a1_b12.py`)** ở vị trí **`lesson_order = 13`** của cấp độ **A1**; **(2)** *cộng dồn thêm* động từ và từ vựng mới của Bài 12 vào 2 chuyên mục tra cứu; **(3)** *mở rộng thêm* (không thay thế) kiến thức Đấu trường tới Bài 12; **(4)** viết và chạy kịch bản kiểm thử toàn diện `verify_lesson12_qa.py`.
> * **Quy tắc chống ghi đè khi cộng dồn dữ liệu**: Nếu một động từ / danh từ của Bài 12 **đã tồn tại** trong `verbs_db.js` / `lexikon_db.js` từ bài trước (rất có thể đã có `das Auge`, `warten`, `essen`...), thì **GIỮ NGUYÊN thẻ cũ, KHÔNG tạo thẻ trùng, KHÔNG sửa thẻ cũ**. Chỉ thêm các mục chưa có (so khớp theo `lemma` + `article`). Báo cáo ở cuối quá trình: *"đã thêm N thẻ mới, bỏ qua M thẻ trùng"*.
> * **Quy tắc chống phá vỡ giao diện cũ (`Zero-Regression for UI`)**: Các dạng bài mới của Bài 12 (xem mục 3.2) phải được làm bằng cách **thêm component mới hoặc tổng quát hóa component có sẵn một cách tương thích ngược** (ví dụ: `phan_loai_cach` có thể kế thừa từ bài 11, `chia_imperativ` có thể kế thừa từ điền khuyết). Sau khi code xong, mở lại **Bài 10, Bài 11** để kiểm tra các dạng bài cũ vẫn hoạt động.
> * **Bản quyền & Độc lập 100%**: Tuyệt đối không chèn bất kỳ link, nút bấm hay thẻ `<iframe>` YouTube nào vào giao diện web hoặc cơ sở dữ liệu. Video bài giảng chỉ là tài liệu tham khảo để soạn nội dung.
>
> ---
>
> ### 🎯 2. PHẠM VI KIẾN THỨC & ĐỘ KHÓ (`A1+ SCOPE CONTROL`)
> * **Bốn trọng tâm của Bài 12** *(đúng theo yêu cầu từ video & bảng giảng)*:
>   1. **Từ vựng Cơ thể & Sức khỏe (`Körper & Gesundheit`)**: Hơn 30 bộ phận cơ thể (der Bauch, die Nase, das Auge...), triệu chứng bệnh (Kopfschmerzen, Husten), khám bác sĩ, nhà thuốc.
>   2. **Đại từ nhân xưng ở `Akkusativ` (`Personalpronomen im Akkusativ`)**: `mich, dich, ihn, sie, es, uns, euch, sie, Sie`. Cách dùng sau động từ (`lieben, treffen, anrufen`) và giới từ (`für, ohne`). Đặc biệt **kết hợp ôn lại phân biệt `Akkusativ` và `Dativ`**.
>   3. **Động từ khuyết thiếu `dürfen`**: Dùng để xin phép / cho phép (`darf ich?`) hoặc cấm đoán (`nicht dürfen`). Nắm vững biến âm `ü → a` ở số ít.
>   4. **Câu mệnh lệnh (`Imperativ`)**: Khuyên bảo, ra lệnh cho 3 ngôi `Sie` (Ngài), `ihr` (các bạn), `du` (bạn). Đặc biệt chú ý ngôi `du` (bỏ -st, giữ biến âm e→i, mất biến âm a→ä, thêm đuôi -e với gốc d/t).
> * **Ôn tập có chủ đích**: Dativ với `helfen`, `wehtun`, `passen`, `gefallen`.
> * **Độ khó**: Nâng cao hơn Bài 11. Đòi hỏi sự chính xác tuyệt đối trong việc chia động từ bất quy tắc ở câu mệnh lệnh.
>
> ---
>
> ### 🎨 3. QUY TẮC VÀNG VỀ IMPERATIV & ĐẠI TỪ TRONG BÀI TẬP (`IMPERATIV–PRONOUN RULES`) — **BẮT BUỘC TUYỆT ĐỐI**
> * **R1 — Cấm chủ ngữ ngôi du/ihr trong Imperativ**: Câu mệnh lệnh ngôi du/ihr chỉ bắt đầu bằng Động từ, không bao giờ có chủ ngữ (Sai: *Gehst du spazieren!* -> Đúng: *Geh spazieren!*). Ngôi `Sie` bắt buộc phải có chủ ngữ đứng ngay sau động từ (*Gehen Sie!*).
> * **R2 — Quy tắc biến âm Imperativ ngôi `du`**: Động từ đổi `e → i/ie` ở hiện tại thì Imperativ GIỮ biến âm (*essen → iss*, *lesen → lies*). Động từ đổi `a → ä` ở hiện tại thì Imperativ MẤT biến âm, trở về nguyên gốc (*fahren → fahr*, *schlafen → schlaf*).
> * **R3 — Rõ ràng ngữ cảnh Akkusativ/Dativ**: Khi yêu cầu điền đại từ, động từ trong câu phải thể hiện rõ Cách. VD: `helfen` (Dativ -> mir, dir), `lieben/anrufen` (Akkusativ -> mich, dich).
> * **R4 — Đa dạng hóa đáp án (Input leniency)**: Mọi câu dạng gõ phím (`chia_imperativ`) phải có danh sách `accepted_answers` lường trước việc người dùng có gõ dấu chấm than `!` hay không, viết hoa chữ cái đầu hay không.
> * **R5 — Kiểm tra tự động**: `test_imperativ_rules` (Phần 5) quét **toàn bộ** câu đề, đáp án, ví dụ của 125 câu. Vi phạm = **không đạt**.
>
> ---
>
> ### 🗺️ 4. YÊU CẦU HÌNH ẢNH MINH HỌA (`VISUAL DIAGRAMS`) CHO BÀI 12
> Antigravity IDE **BẮT BUỘC** xây dựng module **`static/js/gesundheit_svg.js`** (SVG nội tuyến, tương thích Dark/Light mode) gồm **6 sơ đồ** (đặc tả chi tiết ở **mục 2.9**): `V1` Bản đồ cơ thể người (Körperkarte); `V2` Bảng Đại từ Nhân xưng Nom-Akk-Dat; `V3` Lưu đồ phân biệt Akkusativ / Dativ; `V4` Máy chế tạo Imperativ (Biến đổi 3 bước); `V5` Bảng điều khiển Modalverb dürfen; `V6` Hoạt cảnh tại phòng khám bác sĩ.
>
> ---
>
> ### 🔍 5. GIAO THỨC CHỐNG LỖI TUYỆT ĐỐI & CHỐNG TRÙNG LẶP (`ZERO-BUG & ZERO-DUPLICATE QA PROTOCOL`)
> Các lỗi sau đã từng xuất hiện trên web và **KHÔNG ĐƯỢC LẶP LẠI**:
> 1. **Dịch sai nghĩa / Thiếu phần dịch nghĩa** → Mọi bản dịch tiếng Việt phải dịch đúng câu tiếng Đức hoàn chỉnh. Câu Mệnh lệnh phải có từ "Hãy", "Xin ngài hãy", "Đừng". 100% câu hỏi (125 câu) phải có phần dịch.
> 2. **Dịch / đáp án không liên quan đến đề bài** → Đề bài, hình minh họa, đáp án, dịch nghĩa và giải thích phải cùng sinh ra từ **một đối tượng dữ liệu duy nhất**. Mục `Giải thích` bắt buộc **chứa chính chuỗi đáp án đúng**.
> 3. **Voice thiếu / voice sai** → Mọi nút `🔊` phải có và chỉ truyền **chuỗi tiếng Đức sạch** (`de-DE`). Không đọc ký hiệu `___`, `[1]`, `!`, `?`, emoji. Số đếm phải chuyển thành chữ.
> 4. **Giải thích sai đáp án** → Giải thích phải khớp đáp án đúng. Ví dụ Imperativ của essen phải giải thích: "Vì động từ essen đổi e->i, ngôi du bỏ -st nên thành 'Iss'".
> 5. **Chống trùng lặp câu hỏi 100%** → `len(set(normalized_questions)) == 125`. Toàn bộ 125 câu trong Bài 12 là câu **mới sáng tác**, đa dạng hóa chủ ngữ (Bác sĩ, bệnh nhân, Peter, Maria, mẹ và con).
> 6. **Không sửa bài cũ** → chạy `Zero-Regression Check` (xem Phần 5).
>
> ---
>
> ### ⚠️ 6. NHỮNG ĐIỂM CẦN CHUẨN HÓA SO VỚI BẢNG VIẾT TRÊN LỚP (ĐỌC KỸ TRƯỚC KHI CODE)
> Bảng giảng được viết tay nên có vài chỗ cần xử lý khi đưa lên web để người học **không học sai / không bối rối**:
> 1. **`r. Schulter` → `die Schulter`**: Bảng ghi nhầm vai là giống đực, chuẩn từ điển tiếng Đức là **die Schulter** (giống cái). Web hiển thị thẻ chuẩn `die Schulter`.
> 2. **`s. Tablette` → `die Tablette`**: Bảng ghi nhầm thuốc viên là giống trung, chuẩn là **die Tablette** (giống cái, số nhiều die Tabletten). Web hiển thị `die Tablette`.
> 3. **Mệnh lệnh của `essen`**: Trên bảng viết "Isst", thực tế `du isst` bỏ `-st` sẽ thành **Iss!** (vì gốc đã có ss, nên chỉ bỏ 1 chữ s cuối). Web phải dùng chuẩn `Iss!`.

---

## PHẦN 1: MỞ RỘNG CỘNG DỒN 2 TAB TRA CỨU TRÊN THANH ĐIỀU HƯỚNG

Giữ nguyên toàn bộ dữ liệu của Bài 1 → Bài 11 trong 2 tab **"📖 Chia động từ"** và **"🏷️ Từ vựng & Giống"**, đồng thời bổ sung nối tiếp dữ liệu của **Bài 12** theo quy tắc chống ghi đè.

### 1.1. Bổ sung vào Tab `"📖 Chia động từ"` (`static/js/verbs_db.js`)
Bổ sung **25 động từ trọng tâm của Bài 12**. Cấu trúc UI của Tab này đối với Bài 12 cần **bổ sung thêm cột hiển thị `Imperativ (du/ihr/Sie)`** để người học dễ tra cứu.

| # | Động từ (nghĩa) | Loại / Cách | Präsens (ich / du / er·sie·es / wir / ihr / sie·Sie) | Imperativ (du / ihr / Sie) | Ví dụ (`🔊 de-DE`) & Dịch |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **dürfen** (được phép) | Modalverb, `ü→a` | darf / **darfst** / **darf** / dürfen / dürft / dürfen | *(Không dùng)* | *„Hier darf man nicht rauchen.“* — Ở đây người ta không được phép hút thuốc. |
| 2 | **wehtun** (làm đau, đau) | Tách `weh-` · **+ Dativ** | tue weh / tust weh / tut weh / tun weh / tut weh / tun weh | *(Ít dùng)* | *„Mein Rücken tut mir sehr weh.“* — Lưng tôi rất đau. |
| 3 | **fehlen** (thiếu, có vấn đề) | **+ Dativ** | fehle / fehlst / fehlt / fehlen / fehlt / fehlen | *(Ít dùng)* | *„Was fehlt Ihnen denn?“* — Ngài có vấn đề gì vậy? (Ngài bệnh gì?) |
| 4 | **husten** (ho) | Gốc `-t` → thêm `e` | huste / **hustest** / **hustet** / husten / **hustet** / husten | **huste** / **hustet** / **husten Sie** | *„Der Patient hustet stark.“* — Bệnh nhân ho rất mạnh. |
| 5 | **rauchen** (hút thuốc) | Có quy tắc | rauche / rauchst / raucht / rauchen / raucht / rauchen | **rauch(e)** / **raucht** / **rauchen Sie** | *„Er raucht jeden Tag fünf Zigaretten.“* — Anh ấy hút 5 điếu thuốc mỗi ngày. |
| 6 | **ausruhen (sich)** (nghỉ ngơi) | Tách, phản thân | ruhe aus / ruhst aus / ruht aus / ruhen aus / ruht aus / ruhen aus | **ruh(e) dich aus** / **ruht euch aus** / **ruhen Sie sich aus** | *„Sie müssen sich viel ausruhen.“* — Ngài phải nghỉ ngơi nhiều. |
| 7 | **einreiben** (thoa, xoa bóp) | Tách `ein-` | reibe ein / reibst ein / reibt ein / reiben ein / reibt ein / reiben ein | **reib(e) ein** / **reibt ein** / **reiben Sie ein** | *„Reiben Sie den Fuß mit Salbe ein.“* — Hãy thoa thuốc mỡ lên bàn chân. |
| 8 | **zunehmen** (tăng cân) | Tách, `e→i` | nehme zu / **nimmst zu** / **nimmt zu** / nehmen zu / nehmt zu / nehmen zu | **nimm zu** / **nehmt zu** / **nehmen Sie zu** | *„Er hat im Urlaub viel zugenommen.“* — Anh ấy đã tăng cân nhiều trong kỳ nghỉ. |
| 9 | **abnehmen** (giảm cân) | Tách, `e→i` | nehme ab / **nimmst ab** / **nimmt ab** / nehmen ab / nehmt ab / nehmen ab | **nimm ab** / **nehmt ab** / **nehmen Sie ab** | *„Sie möchte fünf Kilo abnehmen.“* — Cô ấy muốn giảm 5 ký. |
| 10 | **verschreiben** (kê đơn thuốc) | **+ Dat + Akk** | verschreibe / verschreibst / verschreibt / verschreiben / verschreibt / verschreiben | **verschreib(e)** / **verschreibt** / **verschreiben Sie** | *„Der Arzt verschreibt mir ein Medikament.“* — Bác sĩ kê cho tôi một loại thuốc. |
| 11 | **krankschreiben** (viết giấy nghỉ) | Tách `krank-` | schreibe krank / schreibst krank / schreibt krank / schreiben krank... | *(như schreiben)* | *„Die Ärztin schreibt mich für drei Tage krank.“* — Bác sĩ nữ cho tôi nghỉ ốm 3 ngày. |
| 12 | **klopfen** (đập) | Có quy tắc | klopfe / klopfst / klopft / klopfen / klopft / klopfen | **klopf(e)** / **klopft** / **klopfen Sie** | *„Mein Herz klopft sehr laut.“* — Tim tôi đập rất to. |
| 13 | **atmen** (thở) | Gốc `-m` → thêm `e` | atme / **atmest** / **atmet** / atmen / **atmet** / atmen | **atme** / **atmet** / **atmen Sie** | *„Atmen Sie bitte tief ein und aus!“* — Xin hãy hít vào và thở ra thật sâu! |
| 14 | **warten** (chờ đợi) | Gốc `-t` → thêm `e` | warte / **wartest** / **wartet** / warten / **wartet** / warten | **warte** / **wartet** / **warten Sie** | *„Warte bitte auf mich!“* — Xin hãy đợi tôi với! |
| 15 | **lieben** (yêu) | **+ Akk** | liebe / liebst / liebt / lieben / liebt / lieben | **liebe** / **liebt** / **lieben Sie** | *„Ich liebe dich.“* — Tôi yêu bạn. |
| 16 | **treffen** (gặp) | Bất quy tắc `e→i` | treffe / **triffst** / **trifft** / treffen / trefft / treffen | **triff** / **trefft** / **treffen Sie** | *„Ich treffe ihn heute im Park.“* — Tôi gặp anh ấy hôm nay ở công viên. |
| 17 | **ansehen** (nhìn) | Tách, `e→ie` | sehe an / **siehst an** / **sieht an** / sehen an / seht an / sehen an | **sieh an** / **seht an** / **sehen Sie an** | *„Manchmal siehst du mich an.“* — Đôi khi bạn nhìn tôi. |
| 18 | **baden** (tắm bồn) | Gốc `-d` → thêm `e`| bade / **badest** / **badet** / baden / **badet** / baden | **bade** / **badet** / **baden Sie** | *„Bade nicht im kalten Wasser!“* — Đừng tắm trong nước lạnh! |
| 19 | **laufen** (chạy, đi bộ) | Bất quy tắc `a→ä` | laufe / **läufst** / **läuft** / laufen / lauft / laufen | **lauf(e)** / **lauft** / **laufen Sie** | *„Lauf nicht so schnell!“* — Đừng chạy nhanh quá! *(Mất biến âm)* |
| 20 | **schlafen** (ngủ) | Bất quy tắc `a→ä` | schlafe / **schläfst** / **schläft** / schlafen / schlaft / schlafen | **schlaf(e)** / **schlaft** / **schlafen Sie** | *„Schlaf gut!“* — Ngủ ngon nhé! *(Mất biến âm)* |
| 21 | **essen** (ăn) | Bất quy tắc `e→i` | esse / **isst** / **isst** / essen / esst / essen | **iss** / **esst** / **essen Sie** | *„Iss weniger Schokolade!“* — Hãy ăn ít sô cô la lại! *(Giữ biến âm)* |
| 22 | **trinken** (uống) | Có quy tắc | trinke / trinkst / trinkt / trinken / trinkt / trinken | **trink(e)** / **trinkt** / **trinken Sie** | *„Trinkt mindestens 3 Liter Wasser!“* — Các bạn hãy uống ít nhất 3 lít nước! |
| 23 | **nehmen** (lấy, uống thuốc)| Bất quy tắc `e→i` | nehme / **nimmst** / **nimmt** / nehmen / nehmt / nehmen | **nimm** / **nehmt** / **nehmen Sie** | *„Nimm die Tabletten nach dem Essen!“* — Hãy uống thuốc viên sau bữa ăn! |
| 24 | **sein** (thì, là, ở) | Bất quy tắc (ĐB) | bin / bist / ist / sind / seid / sind | **sei** / **seid** / **seien Sie** | *„Sei bitte ruhig!“* — Xin hãy trật tự! |
| 25 | **haben** (có) | Bất quy tắc | habe / hast / hat / haben / habt / haben | **hab(e)** / **habt** / **haben Sie** | *„Hab Geduld!“* — Hãy kiên nhẫn! |

> 📌 **Lưu ý hiển thị**: Thẻ động từ phải có nhãn **cách đi cùng** (`+ Akk` / `+ Dativ` / `+ Dativ + Akk`) in nổi bật. Cột Imperativ phải tô đậm sự biến âm hoặc mất biến âm.

---

### 1.2. Bổ sung vào Tab `"🏷️ Từ vựng & Giống"` (`static/js/lexikon_db.js`)
Bổ sung **50 danh từ mới** cực kỳ quan trọng về giải phẫu cơ thể và y tế (chia theo đúng bảng viết tay của giáo viên, đã chuẩn hóa lỗi `Schulter`, `Tablette`).

#### Chủ đề A: `Körperteile: Các bộ phận cơ thể (Bài 12)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | **der Kopf** | die Köpfe | cái đầu | Mein Kopf tut sehr weh. | Đầu tôi rất đau. |
| 2 | **der Hals** | die Hälse | cổ, họng | Ich habe Schmerzen im Hals. | Tôi bị đau ở họng. |
| 3 | **der Arm** | die Arme | cánh tay | Sein linker Arm ist gebrochen. | Cánh tay trái của anh ấy bị gãy. |
| 4 | **der Bauch** | die Bäuche | bụng | Nach dem Essen tut mein Bauch weh. | Sau khi ăn bụng tôi bị đau. |
| 5 | **der Rücken** | die Rücken | lưng | Er hat Probleme mit dem Rücken. | Anh ấy có vấn đề với cái lưng. |
| 6 | **der Fuß** | die Füße | bàn chân | Meine Füße sind sehr kalt. | Hai bàn chân tôi rất lạnh. |
| 7 | **der Finger** | die Finger | ngón tay | Zeig mir deine Finger! | Hãy cho tôi xem ngón tay của bạn! |
| 8 | **der Zahn** | die Zähne | răng | Du musst deine Zähne putzen. | Bạn phải đánh răng. |
| 9 | **der Muskel** | die Muskeln | cơ bắp | Er trainiert seine Muskeln. | Anh ấy tập luyện cơ bắp. |
| 10 | **der Mund** | die Münder | miệng | Mach bitte den Mund auf! | Xin hãy há miệng ra! |
| 11 | **der Zeh** | die Zehen | ngón chân | Ein Zeh tut mir weh. | Một ngón chân làm tôi đau. |
| 12 | **der Magen** | die Mägen | dạ dày | Der Magen ist leer. | Dạ dày đang trống rỗng. |
| 13 | **die Hand** | die Hände | bàn tay | Bitte waschen Sie Ihre Hände! | Xin ngài hãy rửa tay! |
| 14 | **die Nase** | die Nasen | mũi | Meine Nase läuft. | Mũi tôi đang chảy nước. |
| 15 | **die Lunge** | die Lungen | phổi | Rauchen ist schlecht für die Lunge. | Hút thuốc thì tồi tệ cho phổi. |
| 16 | **die Schulter** | die Schultern | vai | Sie hat Schmerzen in der Schulter. | Cô ấy bị đau ở vai. |
| 17 | **die Brust** | die Brüste | ngực | Der Arzt hört meine Brust ab. | Bác sĩ nghe lồng ngực của tôi. |
| 18 | **die Zunge** | die Zungen | lưỡi | Zeigen Sie mir Ihre Zunge! | Hãy cho tôi xem lưỡi của ngài! |
| 19 | **das Auge** | die Augen | mắt | Deine Augen sind sehr schön. | Đôi mắt của bạn rất đẹp. |
| 20 | **das Ohr** | die Ohren | tai | Ein Ohr tut ihm weh. | Một bên tai làm anh ấy đau. |
| 21 | **das Bein** | die Beine | chân (cả cẳng) | Sie hat lange Beine. | Cô ấy có đôi chân dài. |
| 22 | **das Herz** | die Herzen | tim | Mein Herz schlägt schnell. | Tim tôi đập nhanh. |
| 23 | **das Knie** | die Knie | đầu gối | Mein Knie tut beim Laufen weh. | Đầu gối tôi đau khi chạy. |
| 24 | **das Haar** | die Haare | tóc | Sie wäscht ihre Haare jeden Tag. | Cô ấy gội đầu mỗi ngày. |
| 25 | **das Gesicht** | die Gesichter | khuôn mặt | Wasch dir das Gesicht! | Hãy rửa mặt đi! |

#### Chủ đề B: `Gesundheit & Krankheit: Sức khỏe, Khám bệnh (Bài 12)` — 25 danh từ
| # | Danh từ | Số nhiều | Nghĩa | Ví dụ (`example_de`) | Dịch (`example_vi`) |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 26 | **der Hausarzt** | die Hausärzte | bác sĩ gia đình (nam) | Ich muss zum Hausarzt gehen. | Tôi phải đi bác sĩ gia đình. |
| 27 | **der Schmerz** | die Schmerzen | cơn đau | Ich habe starke Zahnschmerzen. | Tôi bị đau răng dữ dội. |
| 28 | **der Hustensaft**| die Hustensäfte | siro ho | Nehmen Sie diesen Hustensaft! | Ngài hãy uống siro ho này! |
| 29 | **der Schnupfen** | *(nur Sg.)* | bệnh sổ mũi | Bei Schnupfen brauche ich Taschentücher.| Khi sổ mũi tôi cần khăn giấy. |
| 30 | **der Husten** | *(nur Sg.)* | bệnh ho | Dein Husten klingt schlimm. | Tiếng ho của bạn nghe tệ đấy. |
| 31 | **der Ratschlag** | die Ratschläge | lời khuyên | Der Arzt gibt mir einen guten Ratschlag.| Bác sĩ cho tôi một lời khuyên tốt. |
| 32 | **der Termin** | die Termine | cuộc hẹn | Haben Sie einen Termin? | Ngài có lịch hẹn không? |
| 33 | **der Patient** | die Patienten | bệnh nhân (nam) | Der Patient muss im Bett bleiben. | Bệnh nhân phải nằm lại trên giường. |
| 34 | **die Hausärztin** | die Hausärztinnen| bác sĩ gia đình (nữ) | Ich habe einen Termin bei der Hausärztin.| Tôi có lịch hẹn với bác sĩ nữ. |
| 35 | **die Patientin** | die Patientinnen | bệnh nhân (nữ) | Die Patientin wartet schon lange. | Bệnh nhân nữ đã đợi lâu rồi. |
| 36 | **die Entspannung**| *(nur Sg.)* | sự thư giãn | Yoga ist gut für die Entspannung. | Yoga tốt cho sự thư giãn. |
| 37 | **die Konzentration**| *(nur Sg.)*| sự tập trung | Die Konzentration fällt mir schwer. | Sự tập trung thật khó với tôi. |
| 38 | **die Bewegung** | *(nur Sg.)* | sự vận động | Bewegung ist wichtig für die Gesundheit.| Vận động rất quan trọng cho sức khỏe. |
| 39 | **die Versichertenkarte**| die -karten | thẻ BHYT | Ich brauche Ihre Versichertenkarte. | Tôi cần thẻ BHYT của ngài. |
| 40 | **die Arztkosten** | *(nur Pl.)* | chi phí y tế | Die Versicherung bezahlt die Arztkosten.| Bảo hiểm chi trả chi phí y tế. |
| 41 | **die Apotheke** | die Apotheken | hiệu thuốc | Die Apotheke ist gleich um die Ecke. | Hiệu thuốc ở ngay góc phố. |
| 42 | **die Entzündung** | die Entzündungen | chứng viêm | Er hat eine Halsentzündung. | Anh ấy bị viêm họng. |
| 43 | **die Zigarette** | die Zigaretten | điếu thuốc lá | Zigaretten sind ungesund. | Thuốc lá thì không tốt cho sức khỏe. |
| 44 | **die Salbe** | die Salben | thuốc mỡ | Diese Salbe hilft gegen Rückenschmerzen.| Thuốc mỡ này giúp trị đau lưng. |
| 45 | **die Erkältung** | die Erkältungen | chứng cảm lạnh | Mit einer Erkältung soll man im Bett bleiben.| Khi bị cảm lạnh nên nằm nghỉ. |
| 46 | **die Gesundheit** | *(nur Sg.)* | sức khỏe | Gesundheit ist das Wichtigste im Leben.| Sức khỏe là điều quan trọng nhất. |
| 47 | **die Krankheit** | die Krankheiten | bệnh tật | Das ist eine schwere Krankheit. | Đó là một căn bệnh nặng. |
| 48 | **die Tablette** | die Tabletten | thuốc viên | Nehmen Sie täglich zwei Tabletten! | Mỗi ngày uống hai viên thuốc! |
| 49 | **das Fieber** | *(nur Sg.)* | cơn sốt | Das Kind hat hohes Fieber. | Đứa trẻ bị sốt cao. |
| 50 | **das Medikament** | die Medikamente | thuốc men | Nehmen Sie das Medikament nach dem Essen.| Hãy uống thuốc sau bữa ăn. |
| 51 | **das Rezept** | die Rezepte | đơn thuốc | Der Arzt schreibt mir ein Rezept. | Bác sĩ viết cho tôi một đơn thuốc. |

---

## PHẦN 2: NỘI DUNG LÝ THUYẾT CHUYÊN SÂU BÀI 12 (HIỂN THỊ TRÊN WEB)

Bài học thứ 13 trong danh sách Cấp độ A1 (`lesson_order = 13`):
- **Tiêu đề bài học**: `Bài 12: Körper - Gesundheit - dürfen - Pronomen im Akkusativ - Imperativ`
- **Tiêu đề đầy đủ ở khung bài**: `Bài 12: Körper und Gesundheit: Cơ thể, Sức khỏe, Đại từ Akkusativ, Dürfen & Imperativ`
- **Mô tả ngắn**: `Làm chủ từ vựng 30+ bộ phận cơ thể và các triệu chứng bệnh tật. Học cách dùng Modalverb 'dürfen' (được phép/cấm). Phân biệt cực kỳ chi tiết Đại từ nhân xưng ở Akkusativ so với Dativ. Đặc biệt, nắm vững nghệ thuật ra lệnh và khuyên bảo qua câu mệnh lệnh (Imperativ) ở 3 ngôi: du, ihr, Sie.`

### CẤU TRÚC HIỂN THỊ TRANG LÝ THUYẾT (Kế thừa UI Bài 11)
Bố cục bao gồm:
* **Huy hiệu đầu khung**: `DeutschMeister A1 • Körper & Gesundheit • dürfen • Imperativ (Bài 12)`
* **4 viên thuốc chủ đề**: `🏥 50 Từ vựng Cơ thể & Bệnh tật` · `🧍 Đại từ Akkusativ (mich, dich...)` · `🛑 Modalverb: dürfen` · `❗️ Câu mệnh lệnh (Imperativ)`
* **8 Thẻ mục đánh số** cho 8 phần lý thuyết bên dưới.
* **6 Sơ đồ SVG nhúng** vào đúng ngữ cảnh.

---

### HỌC PHẦN 1: TỪ VỰNG CƠ THỂ VÀ BỆNH LÝ (KÖRPER & KRANKHEIT)
*   **Trình bày danh sách từ vựng theo cấu trúc 3 giống (der/die/das) đã liệt kê ở phần 1.2.**
*   **Bổ sung khái niệm ghép từ (Komposita)**:
    *   `Bộ phận cơ thể + schmerzen (Luôn số nhiều) = Bệnh đau nhức.`
    *   Ví dụ: `der Kopf + die Schmerzen = die Kopfschmerzen` (Đau đầu); `der Bauch + die Schmerzen = die Bauchschmerzen` (Đau bụng); `der Zahn + die Schmerzen = die Zahnschmerzen` (Đau răng).
*   **Cách diễn đạt triệu chứng bệnh với `wehtun`**:
    *   `[Bộ phận cơ thể ở Nominativ] + tut/tun + [Người bị đau ở Dativ] + weh`
    *   *„Mein Kopf (số ít) **tut mir** weh.“* — Đầu tôi làm tôi đau (Đầu tôi đau).
    *   *„Meine Füße (số nhiều) **tun ihm** weh.“* — Bàn chân anh ấy làm anh ấy đau.
*   *Tích hợp Sơ đồ V1 (Bản đồ cơ thể Körperkarte) tại đây.*

### HỌC PHẦN 2: ⭐ ĐẠI TỪ NHÂN XƯNG CÁCH 4 (PERSONALPRONOMEN IM AKKUSATIV)

| Nominativ (Chủ ngữ - Người thực hiện) | Akkusativ (Tân ngữ Trực tiếp - Bị tác động) | Dativ (Tân ngữ Gián tiếp - Mở rộng) |
| :--- | :--- | :--- |
| **ich** (tôi) | ➔ **mich** | mir |
| **du** (bạn) | ➔ **dich** | dir |
| **er** (anh ấy) | ➔ **ihn** | ihm |
| **sie** (cô ấy) | ➔ **sie** | ihr |
| **es** (nó) | ➔ **es** | ihm |
| **wir** (chúng tôi) | ➔ **uns** | uns |
| **ihr** (các bạn) | ➔ **euch** | euch |
| **sie** (họ) / **Sie** (Ngài) | ➔ **sie / Sie** | ihnen / Ihnen |

> 💡 **KHUNG NHẤN MẠNH: PHÂN BIỆT KHI NÀO DÙNG AKKUSATIV, KHI NÀO DÙNG DATIV?**
> *   Dùng đại từ **Akkusativ** sau các động từ tác động trực tiếp: `lieben` (yêu), `treffen` (gặp), `kennen` (biết), `hören` (nghe), `ansehen` (nhìn), `besuchen` (thăm), `brauchen` (cần), `anrufen` (gọi điện). Cũng dùng sau giới từ `für, ohne`.
>     *   *Ví dụ:* Ich liebe **dich**. (Tôi yêu bạn).
>     *   *Ví dụ:* Ich treffe **ihn** im Krankenhaus. (Tôi gặp anh ấy ở bệnh viện).
> *   Dùng đại từ **Dativ** (mir, dir, ihm, ihr, uns, euch, ihnen, Ihnen) sau các động từ: `helfen` (giúp đỡ), `gefallen` (thích), `passen` (vừa vặn), `wehtun` (làm đau). Hoặc sau giới từ `mit, bei, von, zu`.
>     *   *Ví dụ:* Der Kopf tut **mir** weh. (Tôi bị đau đầu).
>     *   *Ví dụ:* Kann ich **Ihnen** helfen? (Tôi có thể giúp NGÀI không?)
> *   *Tích hợp Sơ đồ V2 (Lưu đồ Akk/Dat) tại đây.*

#### 2.1. ⚠️ 10 LỖI THƯỜNG GẶP KHI DÙNG ĐẠI TỪ (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Dùng Dativ thay Akk | ✘ *Ich liebe dir.* | ✔ *Ich liebe dich.* | `lieben` + Akkusativ. |
| 2 | Dùng Akk thay Dativ | ✘ *Der Arzt hilft mich.* | ✔ *Der Arzt hilft mir.* | `helfen` + Dativ. |
| 3 | Sai đại từ của 'er' | ✘ *Ich kenne ihm nicht.* | ✔ *Ich kenne ihn nicht.* | `kennen` + Akkusativ (ihn). |
| 4 | Nhầm lẫn sau giới từ | ✘ *Das ist für mir.* | ✔ *Das ist für mich.* | Giới từ `für` + Akkusativ. |
| 5 | Dùng Nom làm tân ngữ | ✘ *Ich besuche du morgen.* | ✔ *Ich besuche dich morgen.* | `besuchen` + Akkusativ. |
| 6 | Nhầm phản thân | ✘ *Wir sehen wir.* | ✔ *Wir sehen uns.* | Đại từ Akkusativ của wir là `uns`. |
| 7 | Nhầm 'ihr' (Dat) với 'sie' | ✘ *Ich treffe ihr.* | ✔ *Ich treffe sie.* | Gặp cô ấy: `treffen` + Akk (sie). |
| 8 | Dùng sai với wehtun | ✘ *Der Bauch tut mich weh.* | ✔ *Der Bauch tut mir weh.* | `wehtun` + Dativ. |
| 9 | Dùng sai với anrufen | ✘ *Ruf mir bitte an.* | ✔ *Ruf mich bitte an.* | `anrufen` + Akkusativ. |
| 10 | Bẫy đại từ giống nhau | ✘ *Das Auto gehört uns.* (Akk) | ✔ *Das Auto gehört uns.* (Dat) | (`uns` ở Akk/Dat giống nhau, nhưng đây là Dat vì `gehören`). |

### HỌC PHẦN 3: ĐỘNG TỪ KHUYẾT THIẾU `DÜRFEN` (SỰ CHO PHÉP / CẤM ĐOÁN)
*   **Ý nghĩa**: `dürfen` dùng để diễn tả sự xin phép, được phép làm gì (do nội quy, pháp luật, hoặc người khác cho phép). Khi đi với `nicht` (nicht dürfen), nó có nghĩa là **CẤM** (không được phép).
*   **Bảng chia động từ:** (Nhấn mạnh sự biến đổi nguyên âm ở số ít `ü` ➔ `a` và ngôi ich/er/sie/es không có đuôi).
    *   ich **darf**
    *   du **darfst**
    *   er/sie/es **darf**
    *   wir dürfen
    *   ihr dürft
    *   sie/Sie dürfen
*   **Cấu trúc câu**: Động từ `dürfen` đứng vị trí số 2 (chia theo chủ ngữ), động từ chính nằm ở **cuối câu, nguyên thể**.
*   **Ví dụ phân tích (`🔊`)**:
    *   *Die Kinder **dürfen** im Garten Fußball **spielen**.* (Bọn trẻ được phép chơi bóng đá trong vườn).
    *   *Im Restaurant **darf** man nicht **rauchen**.* (Trong nhà hàng người ta không được phép/bị cấm hút thuốc).
*   *Tích hợp Sơ đồ V5 (Bảng điều khiển Modalverb) tại đây.*

### HỌC PHẦN 4: CÂU MỆNH LỆNH (IMPERATIV)
Câu mệnh lệnh dùng để ra lệnh, yêu cầu, khuyên bảo. Trong tiếng Đức, câu mệnh lệnh chủ yếu dùng cho 3 ngôi: `du` (bạn - thân mật số ít), `ihr` (các bạn - thân mật số nhiều), và `Sie` (Ngài/Các ngài - trang trọng).

#### 4.1. Ngôi `Sie` (Lịch sự, trang trọng)
*   **Quy tắc**: Động từ nguyên thể + Sie + (các thành phần khác) + !
*   *Ví dụ*: `Sie gehen geradeaus.` ➔ **Gehen Sie** geradeaus! (Ngài hãy đi thẳng!)
*   *Ví dụ*: `Sie essen die Suppe.` ➔ **Essen Sie** die Suppe, bitte! (Xin Ngài hãy ăn súp!)

#### 4.2. Ngôi `ihr` (Thân mật, số nhiều - "các bạn/các con")
*   **Quy tắc**: Động từ chia ở ngôi ihr (thêm đuôi 't') + BỎ chữ 'ihr' + !
*   *Ví dụ*: `Ihr geht geradeaus.` ➔ **Geht** geradeaus! (Các bạn hãy đi thẳng!)
*   *Ví dụ*: `Ihr esst die Suppe.` ➔ **Esst** die Suppe, bitte! (Các bạn hãy ăn súp đi!)

#### 4.3. Ngôi `du` (Thân mật, số ít - "mày/bạn/con") — ⚠️ ĐẶC BIỆT CHÚ Ý
*   **Quy tắc chung**: Lấy động từ chia ở ngôi du (thêm đuôi 'st') ➔ **BỎ đuôi 'st'** và **BỎ chữ 'du'**.
*   *Ví dụ*: `Du gehst geradeaus.` ➔ **Geh** geradeaus! (Con hãy đi thẳng!)
*   **A. Trường hợp biến âm `e` ➔ `i/ie`**: Vẫn GIỮ NGUYÊN sự biến âm, sau đó bỏ 'st' và 'du'.
    *   *Ví dụ với essen*: ich esse, du isst ➔ Bỏ 'st', do isst tận cùng bằng 's' nên chỉ còn 's' ➔ **Iss!** (Ăn đi!). *(Ghi chú: Cô giáo khoanh tròn kỹ lỗi hay sai chữ Iss trên bảng)*.
    *   *Ví dụ với nehmen*: du nimmst ➔ **Nimm!** (Lấy đi!).
*   **B. Trường hợp biến âm `a` ➔ `ä`**: Bắt buộc **MẤT BIẾN ÂM**, trở về 'a' ban đầu.
    *   *Ví dụ với fahren*: du fährst ➔ **Fahr!** (Hãy lái xe đi!).
    *   *Ví dụ với laufen*: du läufst ➔ **Lauf!** (Hãy chạy đi!).
*   **C. Quy tắc thêm đuôi `-e`**: Dành cho các động từ có gốc kết thúc bằng **-d, -t, -ig, -nen, -ieren, -eln, -ern** để dễ phát âm.
    *   *Ví dụ*: `Du wartest` ➔ **Warte!** (Chờ đã!)
    *   *Ví dụ*: `Du lernst` ➔ **Lerne!** (Học đi!)
    *   *Ví dụ*: `Du badest` ➔ **Bade!** (Tắm đi!)

#### 4.4. Động từ bất quy tắc trong Imperativ (Học thuộc lòng)
*   **sein** (là/thì/ở):
    *   du: **Sei** ruhig! (Hãy trật tự!)
    *   ihr: **Seid** ruhig!
    *   Sie: **Seien Sie** ruhig! (Ngài hãy trật tự!)
*   **haben** (có):
    *   du: **Hab** Geduld! (Hãy kiên nhẫn!)
    *   ihr: **Habt** Geduld!
    *   Sie: **Haben Sie** Geduld!

#### 4.5. Phân tích bài tập trên bảng giáo viên (Rèn luyện Imperativ)
1. mindestens 3 Liter Wasser am Tag trinken (ihr) ➔ **Trinkt mindestens 3 Liter Wasser am Tag!**
2. mehr Obst und Gemüse essen (Sie) ➔ **Essen Sie mehr Obst und Gemüse, bitte!**
3. jeden Tag spazieren gehen (du) ➔ **Geh jeden Tag spazieren!** *(Chú ý động từ tách 'spazieren gehen', 'geh' đứng đầu, 'spazieren' đứng cuối).*
4. weniger Schokolade essen (du) ➔ **Iss weniger Schokolade!**
5. heute einen Termin beim Arzt machen (ihr) ➔ **Macht heute einen Termin beim Arzt!**

#### 4.6. ⚠️ 10 LỖI THƯỜNG GẶP VỚI IMPERATIV (✘ sai → ✔ đúng)
| # | Lỗi | ✘ Sai | ✔ Đúng | Giải thích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Giữ chữ 'du' | ✘ *Gehst du nach Hause!* | ✔ *Geh nach Hause!* | Ngôi 'du' bắt buộc bỏ chữ 'du'. |
| 2 | Giữ đuôi -st | ✘ *Gehst nach Hause!* | ✔ *Geh nach Hause!* | Ngôi 'du' bắt buộc bỏ đuôi -st. |
| 3 | Giữ biến âm 'ä' | ✘ *Fähr langsam!* | ✔ *Fahr langsam!* | Các từ a->ä sẽ mất biến âm (trở về a). |
| 4 | Mất biến âm 'i' | ✘ *Geb mir das!* | ✔ *Gib mir das!* | Các từ e->i/ie giữ nguyên biến âm. |
| 5 | Quên thêm 'e' (gốc t/d) | ✘ *Wart hier!* | ✔ *Warte hier!* | Gốc tận cùng bằng -t, -d phải thêm -e. |
| 6 | Giữ chữ 'ihr' | ✘ *Trinkt ihr viel!* | ✔ *Trinkt viel!* | Ngôi 'ihr' bắt buộc bỏ chữ 'ihr'. |
| 7 | Quên chữ 'Sie' | ✘ *Essen viel Obst!* | ✔ *Essen Sie viel Obst!* | Ngôi 'Sie' bắt buộc phải có chữ 'Sie'. |
| 8 | Sai Imperativ của sein | ✘ *Bist ruhig!* | ✔ *Sei ruhig!* | Mệnh lệnh ngôi du của sein là 'Sei'. |
| 9 | Động từ tách sai vị trí | ✘ *Zieh an die Jacke!* | ✔ *Zieh die Jacke an!* | Tiền tố tách luôn đứng cuối câu. |
| 10 | Chia sai essen | ✘ *Ess die Suppe!* | ✔ *Iss die Suppe!* | essen ➔ du isst ➔ Iss! |

### HỌC PHẦN 5: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN (`TEXTANALYSE` — KÈM AUDIO `de-DE`)

#### 5.1. Hội thoại đăng ký khám bệnh (`🔊`)
*   A: Guten Tag.
*   B: Guten Tag, ich habe starke Zahnschmerzen. (Xin chào, tôi bị đau răng rất nặng).
*   A: Haben Sie einen Termin? (Ngài có lịch hẹn không?)
*   B: Nein, leider nicht. Muss ich lange warten? (Không, rất tiếc là không. Tôi có phải đợi lâu không?)
*   A: Waren Sie schon einmal bei uns? (Ngài đã từng đến chỗ chúng tôi chưa?)
*   B: Ja, mein Name ist Maria. (Có, tên tôi là Maria).
*   A: Ja. Wir haben heute viele Patienten. Ich brauche Ihre Versichertenkarte. (Vâng. Hôm nay chúng tôi có nhiều bệnh nhân. Tôi cần thẻ bảo hiểm y tế của ngài).
*   B: Hier, bitte. (Đây ạ, xin mời).
*   A: Danke... So, hier ist Ihre Karte. Bitte nehmen Sie im Wartezimmer Platz. (Cảm ơn... Rồi, đây là thẻ của ngài. Xin mời ngài ngồi ở phòng chờ).
*   B: Gut, mache ich. Danke. (Vâng, tôi sẽ làm vậy. Cảm ơn).

#### 5.2. Lá thư của Peter (Phân tích Đại từ Akkusativ) (`🔊`)
> "Liebe Jenny, **du** (Nom) kennst **mich** (Akk). **Wir** (Nom) sehen **uns** (Akk) jeden Morgen im Bus. Ein Morgen ohne **dich** (Akk) ist wie ein Morgen ohne Sonne! Manchmal siehst **du** (Nom) **mich** (Akk) an, **das** (Nom) macht **mich** (Akk) sehr glücklich. Mein Herz klopft dann sehr laut - kannst **du** (Nom) **es** (Akk) hören? Ich denke oft an **dich** (Akk). Deine Augen, deine Haare - **du** (Nom) bist für **mich** (Akk) eine Traumfrau! Ich möchte **dich** (Akk) kennen lernen. Kommst du morgen um 19:30 Uhr ins Café Müller?
> Viele Grüße, Peter."

#### 5.3. Gia đình Annika (Dürfen & Imperativ) (`🔊`)
*   Mutter: "Annika, du **darfst** jetzt nicht Computer **spielen**!" (Annika, bây giờ con không được phép chơi máy tính!)
*   Annika: "Warum **darf** ich nicht?" (Tại sao con không được?)
*   Mutter: "Du musst Hausaufgaben machen." (Con phải làm bài tập về nhà.)
*   Annika: "**Darf** Julia Computer **spielen**?" (Julia có được chơi máy tính không?)
*   Mutter: "Nein, ihr **dürft** nicht Computer spielen und ihr **dürft** auch nicht fernsehen." (Không, các con không được chơi máy tính và cũng không được xem TV.)
*   Julia: "Wir **dürfen** nicht fernsehen? Dann **dürfen** Mama und Papa auch nicht fernsehen!" (Chúng ta không được xem TV? Vậy thì bố và mẹ cũng không được xem TV!)

### HỌC PHẦN 6 (MỤC 2.9): ĐẶC TẢ 6 SƠ ĐỒ SVG TƯƠNG TÁC (`static/js/gesundheit_svg.js`)
Mỗi sơ đồ phải có **tiêu đề tiếng Việt + nhãn tiếng Đức**, hoạt động đúng ở chế độ Dark/Light, **hiển thị tiêu đề `Sơ đồ V#: …`** và nút chuyển ví dụ, mọi câu tiếng Đức hiển thị trong sơ đồ có nút **`🔊`**.

| Mã | Đặt ở mục | Tên sơ đồ | Hình vẽ & hành vi bắt buộc |
| :-: | :-: | :--- | :--- |
| **V1** | 1 | **Bản đồ Cơ thể (Körperkarte)** | Hình vector người. Có các điểm hotspot ở đầu, vai, bụng, tay, chân... Click vào hotspot sẽ bung Tooltip hiển thị: Mạo từ + Tên bộ phận + Số nhiều (VD: `das Auge / die Augen`) kèm nút `🔊` đọc tên từ vựng. |
| **V2** | 2 | **Lưu đồ Quyết định Akk/Dat** | Sơ đồ khối: "Đại từ làm tân ngữ?" ➔ Nhánh 1: "Động từ/Giới từ đòi Akk (lieben, treffen, für)?" ➔ Dùng `mich, dich, ihn`. Nhánh 2: "Động từ/Giới từ đòi Dat (helfen, wehtun, mit)?" ➔ Dùng `mir, dir, ihm`. Click vào nhánh sinh ra câu ví dụ mẫu. |
| **V3** | 4 | **Máy chế tạo Imperativ (Ngôi du)** | Chọn động từ từ list (gehen, essen, fahren, warten, sein). Sơ đồ hiển thị 3 bước biến đổi: `1. Hiện tại (Du isst) ➔ 2. Bỏ Du, Bỏ -st ➔ 3. Kết quả (Iss!)`. Áp dụng các quy tắc để nhấn mạnh sự biến âm/mất biến âm hoặc thêm chữ `-e`. |
| **V4** | 4 | **So sánh 3 ngôi Imperativ** | Nhập hoặc chọn một động từ. Màn hình chia 3 cột: `du`, `ihr`, `Sie`. Render đồng loạt 3 câu mệnh lệnh song song để so sánh sự khác biệt. |
| **V5** | 3 | **Bảng điều khiển Modalverb** | Chọn Chủ ngữ (ich, du, er, wir...) từ Dropdown. Chọn hành động (rauchen, fernsehen, parken). Máy tính tự động xếp thành câu cấm đoán: `[Chủ ngữ] + [darf/darfst...] + hier nicht + [Động từ nguyên mẫu]`. |
| **V6** | 5 | **Hoạt cảnh Phòng Khám** | Khung cảnh cửa hàng/phòng mạch: người bán/lễ tân và khách (hai bóng nói). Bấm **▶ "Khám bệnh"** → chạy lần lượt Hội thoại 5.1, mỗi lượt phát `🔊`. Có nút chọn lượt `◀ ▶` và nút ẩn / hiện bản dịch. |

---

## PHẦN 3: KHO 125 BÀI TẬP ĐỘC NHẤT CỦA BÀI 12 (`lessons/a1/seed_a1_b12.py`) — 18 DẠNG BÀI

Toàn bộ **125 câu hỏi** dưới đây là **câu mới sáng tác**, không trùng với giáo trình hay Bài 11. Chủ ngữ được **xoay vòng đủ 9 ngôi** cùng tên riêng; ngữ cảnh đa dạng (phòng mạch, nhà thuốc, gia đình, công viên). **Mọi câu Mệnh lệnh đều tuân thủ Quy tắc R1–R2, mọi câu Đại từ tuân thủ R3.**

### 3.1. Bảng Phân Bổ 125 Câu Hỏi Theo 18 Dạng Bài Tập
| STT | Mã dạng (`type`) | Tên dạng bài hiển thị | Số lượng | Mã câu | Trọng tâm |
| :-: | :--- | :--- | :-: | :-: | :--- |
| 1 | `trac_nghiem` | Trắc nghiệm | **15** | 1–15 | Phân biệt Akkusativ/Dativ, chia dürfen, từ vựng cơ thể. |
| 2 | `dien_khuyet` | Điền khuyết | **15** | 16–30 | Chia động từ, Imperativ (chủ yếu du/ihr), điền đại từ. |
| 3 | `chia_imperativ` 🆕 | **Biến đổi Imperativ** | **10** | 31–40 | Cho câu trần thuật -> Gõ lại thành câu Imperativ. |
| 4 | `dien_dai_tu_akk` 🆕 | **Điền đại từ Akkusativ** | **10** | 41–50 | Xác định tân ngữ và điền mich, dich, ihn, sie, es, uns, euch. |
| 5 | `phan_loai_cach` 🆕 | **Phân loại Akkusativ / Dativ** | **5** | 51–55 | 4 hàng/câu: Xác định từ in đậm là Akk hay Dat |
| 6 | `phan_loai_giong` | Phân loại `der / die / das` | **4** | 56–59 | 4 từ mỗi câu: kéo thả vào đúng giống (Từ vựng Körper). |
| 7 | `noi_o_tu_vung` | Nối ô Từ vựng | **8** | 60–67 | Bộ phận cơ thể, số nhiều, triệu chứng bệnh. |
| 8 | `dien_tao_cau` | Điền 2-3 chỗ trống | **5** | 68–72 | Kết hợp dürfen + động từ nguyên thể cuối câu, Imperativ. |
| 9 | `nghe_dien` | Nghe `de-DE` và điền từ | **8** | 73–80 | Luyện nghe Pronomen, bộ phận cơ thể, mệnh lệnh. |
| 10 | `dich_cau_vd` | Dịch câu: Việt → Đức | **6** | 81–86 | Dịch câu mệnh lệnh, câu xin phép, cấm đoán |
| 11 | `dich_cau_dv` | Dịch câu: Đức → Việt | **6** | 87–92 | Các câu phàn nàn về bệnh tật, phòng khám |
| 12 | `sap_xep_cau` | Sắp xếp từ thành câu | **8** | 93–100 | Cấu trúc câu mệnh lệnh, câu có Modalverb. |
| 13 | `tim_loi_sai` | Tìm lỗi và sửa câu | **6** | 101–106 | Lỗi sai biến âm, sai đuôi Imperativ, sai Cách |
| 14 | `dich_nghia_vd` | Dịch từ: Việt → Đức | **4** | 107–110 | Từ vựng y tế / cơ thể (yêu cầu mạo từ) |
| 15 | `dich_nghia_dv` | Dịch từ: Đức → Việt | **4** | 111–114 | Từ vựng y tế / cơ thể |
| 16 | `dung_sai` | Đọc hiểu Đúng / Sai | **4** | 115–118 | Đọc đoạn văn về lối sống khỏe và phán đoán. |
| 17 | `hoi_thoai_sap_xep` | Sắp xếp hội thoại | **3** | 119–121 | Hội thoại tại nhà thuốc, phòng khám bác sĩ. |
| 18 | `bieu_tuong_benh` 🆕 | **Nhìn Emoji đoán bệnh** | **4** | 122-125 | Trắc nghiệm hình ảnh (Đau đầu, ho, sốt). |
| | | **TỔNG CỘNG BÀI 12** | **125** | 1–125 | **100% độc nhất + QA Zero-Bug** |

> 📌 Phân bổ trọng tâm (ước lượng): **35% Imperativ**, **30% Đại từ Akkusativ/Dativ**, **20% dürfen**, **15% Từ vựng Y tế**.

### 3.2. Đặc tả giao diện & chấm điểm cho 3 dạng bài MỚI (🆕) — *làm thêm, không phá component cũ*
Các dạng `sap_xep_cau`, `tim_loi_sai`, `dung_sai`, `phan_loai_giong`, `hoi_thoai_sap_xep` **dùng lại nguyên component của Bài 11**. Ba dạng mới:
| Dạng | Giao diện người học | Dữ liệu câu hỏi (`question object`) | Quy tắc chấm điểm |
| :--- | :--- | :--- | :--- |
| `chia_imperativ` | Hiển thị 1 câu trần thuật (VD: `Du gehst nach Hause.`). Ô input text yêu cầu nhập câu mệnh lệnh tương ứng. | `source_sentence`, `accepted_answers` (chứa các chuỗi đáp án), `translation_vi`, `explanation` | So khớp chuỗi `lowercase`, tự động loại bỏ khoảng trắng thừa và dấu câu `. ! ?` ở cuối. Chấp nhận viết hoa/thường. |
| `dien_dai_tu_akk` | Câu có chỗ trống, gợi ý trong ngoặc: `Ich liebe ___ (du).` | `display_sentence` (có `___`), `accepted_answers`, `translation_vi` | Điền text ngắn. Khớp 100% text (case-insensitive). Giống `dien_khuyet` về UI, chỉ tách ra vì mục đích sư phạm nhóm câu hỏi. |
| `bieu_tuong_benh` | Hiển thị **biểu tượng cảm xúc lớn** (emoji, có `alt` bằng tiếng Việt) + 4 lựa chọn là câu tiếng Đức. | `emoji_icon`, `icon_alt_vi`, `options`, `correct_option_id`, `translation_vi`, `explanation` | Trắc nghiệm chọn một đáp án. Voice đọc **câu đúng**; không bao giờ đọc tên emoji. Tương tự `bieu_tuong_thoi_tiet` Bài 11. |

> 🔊 **Quy tắc voice cho mọi dạng**: sau khi người học trả lời xong, nút `🔊` đọc **câu tiếng Đức đúng đầy đủ**. Không bao giờ đọc ký hiệu `___`, `__`, `[1]`, `!`, `?`, emoji.
> 🈯 **Quy tắc `translation_vi` theo dạng**: Không được để trống phần dịch ở bất kỳ dạng nào. Câu mệnh lệnh phải dịch rõ ý sai bảo ("Hãy", "Xin ngài hãy", "Đừng").
> 🔠 **Quy tắc chữ hoa**: so khớp **không phân biệt hoa/thường**; chấp nhận `ä/ö/ü/ß` được gõ thành `ae/oe/ue/ss`.

---

### 3.3. Danh Sách Chi Tiết 125 Câu Hỏi BÀI 12 (Viết tay toàn bộ 100% để Seed Data)

#### NHÓM 1: TRẮC NGHIỆM (`trac_nghiem` — 15 Câu: Câu 1 → Câu 15)
1. **Câu 1**: Chọn đại từ đúng: *„Ich liebe ___ .“*
  - Đáp án: `A. dir` | `B. dich` (Đúng) | `C. du` | `D. mich`
  - Dịch nghĩa câu: *„Tôi yêu bạn.“*
  - Giải thích: Động từ `lieben` tác động trực tiếp lên đối tượng nên đi kèm với Akkusativ (Cách 4). Đại từ Akkusativ của `du` là **`dich`**.
2. **Câu 2**: Chọn đại từ đúng: *„Der Arzt untersucht ___ heute.“* (ông ấy)
  - Đáp án: `A. er` | `B. ihm` | `C. ihn` (Đúng) | `D. es`
  - Dịch nghĩa câu: *„Bác sĩ khám cho ông ấy hôm nay.“*
  - Giải thích: Động từ `untersuchen` (khám bệnh) + Akkusativ. Akkusativ của `er` là **`ihn`**.
3. **Câu 3**: Chọn hình thức đúng của Modalverb: *„Die Kinder ___ nicht so viel Schokolade essen.“*
  - Đáp án: `A. dürft` | `B. darfst` | `C. darf` | `D. dürfen` (Đúng)
  - Dịch nghĩa câu: *„Bọn trẻ không được phép ăn quá nhiều sô cô la.“*
  - Giải thích: `Die Kinder` là chủ ngữ số nhiều (sie - họ). Động từ dürfen chia ở số nhiều là **`dürfen`**.
4. **Câu 4**: Chọn câu Mệnh lệnh (Imperativ) đúng cho ngôi **du**:
  - Đáp án: `A. Trinkt viel Wasser!` | `B. Trinken Sie viel Wasser!` | `C. Trink viel Wasser!` (Đúng) | `D. Trinkst du viel Wasser!`
  - Dịch nghĩa câu: *„Hãy uống nhiều nước!“*
  - Giải thích: Đối với ngôi `du`, ta bỏ `-st` và bỏ chủ ngữ `du`. `du trinkst` ➔ **`Trink!`**.
5. **Câu 5**: Tìm từ khác loại (về Giống - Artikel):
  - Đáp án: `A. Bauch` | `B. Rücken` | `C. Finger` | `D. Nase` (Đúng)
  - Dịch nghĩa câu: *Bụng, Lưng, Ngón tay, Mũi.*
  - Giải thích: der Bauch, der Rücken, der Finger đều là giống Đực (der). Chỉ có **`die Nase`** là giống Cái (die).
6. **Câu 6**: *„Guten Tag, Herr Müller. Was fehlt ___ ?“*
  - Đáp án: `A. Ihnen` (Đúng) | `B. Sie` | `C. dich` | `D. dir`
  - Dịch nghĩa câu: *„Chào ngài Müller. Ngài bị làm sao vậy?“*
  - Giải thích: Động từ `fehlen` trong y tế đi với Dativ. Herr Müller đòi hỏi sự trang trọng (Sie), Dativ của Sie là **`Ihnen`**.
7. **Câu 7**: Chọn đại từ đúng: *„Wir haben ein Problem. Kannst du ___ helfen?“*
  - Đáp án: `A. uns` (Đúng) | `B. wir` | `C. euch` | `D. mich`
  - Dịch nghĩa câu: *„Chúng tôi có một vấn đề. Bạn có thể giúp chúng tôi không?“*
  - Giải thích: Động từ `helfen` đi với Dativ. Dativ của `wir` (chúng tôi) là **`uns`**. (Bẫy: uns ở Akk và Dat giống nhau, nhưng bản chất ở đây là Dat).
8. **Câu 8**: *„Das ist Maria. Kennst du ___ ?“*
  - Đáp án: `A. ihr` | `B. sie` (Đúng) | `C. ihn` | `D. es`
  - Dịch nghĩa câu: *„Kia là Maria. Bạn có biết cô ấy không?“*
  - Giải thích: Động từ `kennen` + Akkusativ. Akkusativ của `sie` (cô ấy) vẫn là **`sie`**.
9. **Câu 9**: Chọn câu Mệnh lệnh đúng cho ngôi **ihr**: (Động từ essen)
  - Đáp án: `A. Isst mehr Gemüse!` | `B. Esst mehr Gemüse!` (Đúng) | `C. Essen Sie mehr Gemüse!` | `D. Iss mehr Gemüse!`
  - Dịch nghĩa câu: *„Các bạn hãy ăn nhiều rau hơn!“*
  - Giải thích: Mệnh lệnh ngôi `ihr`: chia động từ như bình thường (`ihr esst`) rồi bỏ chủ ngữ `ihr` ➔ **`Esst!`**. Không có biến âm 'i' như ngôi du.
10. **Câu 10**: Biển báo ghi: *„Hier darf man nicht parken.“* Nghĩa là gì?
  - Đáp án: `A. Người ta được phép đỗ xe ở đây.` | `B. Cấm đỗ xe ở đây.` (Đúng) | `C. Bãi đỗ xe miễn phí.` | `D. Bạn phải đỗ xe ở đây.`
  - Dịch nghĩa câu: *„Ở đây người ta không được đỗ xe.“*
  - Giải thích: `nicht dürfen` mang ý nghĩa cấm đoán (Verbot). `parken` = đỗ xe.
11. **Câu 11**: Điền vào chỗ trống: *„Mein rechter ___ tut weh. Ich kann nicht gut laufen.“*
  - Đáp án: `A. Fuß` (Đúng) | `B. Kopf` | `C. Hand` | `D. Bauch`
  - Dịch nghĩa câu: *„Bàn chân phải của tôi bị đau. Tôi không thể đi lại tốt được.“*
  - Giải thích: `laufen` (đi/chạy) liên quan đến chân (`der Fuß`). `rechter` cho thấy danh từ giống đực (der).
12. **Câu 12**: Chọn đại từ đúng: *„Ruf ___ bitte heute Abend an!“* (tôi)
  - Đáp án: `A. mir` | `B. mich` (Đúng) | `C. ich` | `D. mein`
  - Dịch nghĩa câu: *„Hãy gọi cho tôi vào tối nay nhé!“*
  - Giải thích: Động từ `anrufen` (gọi điện) + Akkusativ. Akkusativ của `ich` là **`mich`**.
13. **Câu 13**: Chọn hình thức Mệnh lệnh đúng của động từ **arbeiten** cho ngôi **du**:
  - Đáp án: `A. Arbeit!` | `B. Arbeitest!` | `C. Arbeite!` (Đúng) | `D. Arbeitet!`
  - Dịch nghĩa câu: *„Hãy làm việc đi!“*
  - Giải thích: Động từ kết thúc bằng `-t` (`arbeit-en`). Khi chuyển sang Imperativ ngôi `du`, ta phải giữ lại đuôi `-e` để dễ phát âm ➔ **`Arbeite!`**.
14. **Câu 14**: *„Wie oft muss ich die Tabletten nehmen?“ – „Nehmen ___ sie zweimal täglich.“*
  - Đáp án: `A. Sie` (Đúng) | `B. ihr` | `C. du` | `D. wir`
  - Dịch nghĩa câu: *„Tôi phải uống thuốc mấy lần?“ – „Ngài hãy uống hai lần mỗi ngày.“*
  - Giải thích: Động từ nguyên thể `Nehmen` đứng đầu câu + đại từ nhân xưng ➔ Câu mệnh lệnh ngôi lịch sự **`Sie`**.
15. **Câu 15**: Chọn hình thức đúng của Modalverb: *„___ ich einen Kaffee trinken?“*
  - Đáp án: `A. Darfst` | `B. Dürfen` | `C. Darf` (Đúng) | `D. Dürft`
  - Dịch nghĩa câu: *„Tôi có được phép uống một ly cà phê không?“*
  - Giải thích: Chủ ngữ là `ich` ➔ động từ dürfen chia là **`darf`**.

---

#### NHÓM 2: ĐIỀN KHUYẾT (`dien_khuyet` — 15 Câu: Câu 16 → Câu 30)
16. **Câu 16**: Điền Modalverb `dürfen`: *„Mama, ___ ich jetzt fernsehen?“*
- Đáp án chấp nhận: `["darf"]`
  - Dịch nghĩa câu: *„Mẹ ơi, con có được phép xem TV bây giờ không?“*
  - Giải thích: Chủ ngữ `ich` ➔ **`darf`**.
17. **Câu 17**: Điền Modalverb `dürfen`: *„Ihr ___ nicht so laut sprechen! Das Baby schläft.“*
- Đáp án chấp nhận: `["dürft", "duerft"]`
  - Dịch nghĩa câu: *„Các con không được nói chuyện lớn tiếng như vậy! Em bé đang ngủ.“*
  - Giải thích: Chủ ngữ `ihr` ➔ **`dürft`**.
18. **Câu 18**: Điền Modalverb `dürfen`: *„Entschuldigung, ___ man hier fotografieren?“*
- Đáp án chấp nhận: `["darf"]`
  - Dịch nghĩa câu: *„Xin lỗi, người ta có được phép chụp ảnh ở đây không?“*
  - Giải thích: Chủ ngữ `man` (người ta - ngôi thứ 3 số ít) ➔ **`darf`**.
19. **Câu 19**: Điền Modalverb `dürfen`: *„Lukas ___ heute Abend nicht ins Kino gehen.“*
- Đáp án chấp nhận: `["darf"]`
  - Dịch nghĩa câu: *„Lukas không được phép đi xem phim tối nay.“*
  - Giải thích: Chủ ngữ `Lukas` (er) ➔ **`darf`**.
20. **Câu 20**: Điền động từ chia ở Imperativ (ngôi du): *„___ bitte einen Moment!“* (warten)
- Đáp án chấp nhận: `["Warte"]`
  - Dịch nghĩa câu: *„Xin hãy đợi một lát!“*
  - Giải thích: Động từ `warten` gốc tận cùng bằng `t` ➔ Imperativ ngôi du phải thêm đuôi `-e`: **`Warte!`**.
21. **Câu 21**: Điền động từ chia ở Imperativ (ngôi ihr): *„Kinder, ___ eure Hausaufgaben!“* (machen)
- Đáp án chấp nhận: `["Macht"]`
  - Dịch nghĩa câu: *„Các con, hãy làm bài tập về nhà của các con đi!“*
  - Giải thích: Ngôi ihr chia bình thường `macht` rồi bỏ chữ `ihr` ➔ **`Macht!`**.
22. **Câu 22**: Điền động từ chia ở Imperativ (ngôi du): *„___ nicht so viel Cola!“* (trinken)
- Đáp án chấp nhận: `["Trink", "Trinke"]`
  - Dịch nghĩa câu: *„Đừng uống nhiều nước ngọt Cola quá!“*
  - Giải thích: Ngôi du của trinken là `trinkst`, bỏ `st` ➔ **`Trink!`** (hoặc Trinke! trong văn phong trang trọng).
23. **Câu 23**: Điền động từ chia ở Imperativ (ngôi Sie): *„___ Sie bitte Platz im Wartezimmer!“* (nehmen)
- Đáp án chấp nhận: `["Nehmen"]`
  - Dịch nghĩa câu: *„Xin ngài hãy ngồi chờ ở phòng đợi!“*
  - Giải thích: Cấu trúc mệnh lệnh lịch sự: Nguyên thể **`Nehmen`** + Sie.
24. **Câu 24**: Điền đại từ Akkusativ: *„Das ist mein neuer Pullover. Findest du ___ schön?“* (er)
- Đáp án chấp nhận: `["ihn"]`
  - Dịch nghĩa câu: *„Đó là chiếc áo len mới của tôi. Bạn thấy nó đẹp không?“*
  - Giải thích: `der Pullover` được thay thế bằng đại từ `er`. Đứng làm tân ngữ cho `finden` ➔ Akkusativ là **`ihn`**.
25. **Câu 25**: Điền đại từ Dativ: *„Wir suchen den Bahnhof. Können Sie ___ bitte helfen?“* (wir)
- Đáp án chấp nhận: `["uns"]`
  - Dịch nghĩa câu: *„Chúng tôi đang tìm nhà ga. Ngài có thể giúp chúng tôi được không?“*
  - Giải thích: LƯU Ý! Động từ `helfen` đi với Dativ. Dativ của `wir` là **`uns`**. (Câu này rèn luyện sự tỉnh táo).
26. **Câu 26**: Điền đại từ Akkusativ: *„Ich habe dich gestern angerufen, aber du hast ___ nicht gehört.“* (ich)
- Đáp án chấp nhận: `["mich"]`
  - Dịch nghĩa câu: *„Hôm qua tôi đã gọi điện cho bạn, nhưng bạn không nghe thấy tôi.“*
  - Giải thích: Động từ `hören` + Akkusativ. Akkusativ của `ich` là **`mich`**.
27. **Câu 27**: Điền bộ phận cơ thể: *„Ich kann nicht essen. Ich habe Zahn___.“*
- Đáp án chấp nhận: `["schmerzen"]`
  - Dịch nghĩa câu: *„Tôi không thể ăn. Tôi bị đau răng.“*
  - Giải thích: Ghép từ `Zahn` + `schmerzen` = **`Zahnschmerzen`**.
28. **Câu 28**: Điền bộ phận cơ thể: *„Er hat den ganzen Tag am Computer gearbeitet. Jetzt tun ihm die ___ weh.“* (đôi mắt)
- Đáp án chấp nhận: `["Augen"]`
  - Dịch nghĩa câu: *„Anh ấy đã làm việc cả ngày trên máy tính. Bây giờ đôi mắt của anh ấy bị đau.“*
  - Giải thích: Đôi mắt (số nhiều) = **`die Augen`**.
29. **Câu 29**: Điền dạng đúng của động từ: *„Der Arzt ___ mir Hustensaft.“* (verschreiben)
- Đáp án chấp nhận: `["verschreibt"]`
  - Dịch nghĩa câu: *„Bác sĩ kê cho tôi siro ho.“*
  - Giải thích: Chủ ngữ `Der Arzt` (er) ➔ **`verschreibt`**.
30. **Câu 30**: Điền dạng đúng của động từ: *„Bitte ___ Sie tief ein und aus!“* (atmen)
- Đáp án chấp nhận: `["atmen"]`
  - Dịch nghĩa câu: *„Xin ngài hãy hít vào và thở ra thật sâu!“*
  - Giải thích: Câu mệnh lệnh ngôi Sie ➔ động từ nguyên thể **`atmen`**.

---

#### NHÓM 3: 🆕 BIẾN ĐỔI IMPERATIV (`chia_imperativ` — 10 Câu: Câu 31 → Câu 40)
Người dùng được cung cấp một câu trần thuật và yêu cầu viết lại thành câu Imperativ (mệnh lệnh) cho đúng ngôi. Tự động loại bỏ dấu chấm than và khoảng trắng thừa.
31. **Câu 31**: *Du isst mehr Obst.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Iss mehr Obst!", "Iss mehr Obst"]`
  - Dịch nghĩa câu: *„Hãy ăn nhiều trái cây hơn!“*
  - Giải thích: Động từ essen có biến âm `e` thành `i` ở ngôi du (du isst). Bỏ `st` (vì tận cùng là s nên chỉ mất s) ➔ **`Iss`**.
32. **Câu 32**: *Ihr lest den Text.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Lest den Text!", "Lest den Text"]`
  - Dịch nghĩa câu: *„Các bạn hãy đọc đoạn văn!“*
  - Giải thích: Ngôi `ihr` chia là `lest`, bỏ chữ `ihr` đi ➔ **`Lest den Text!`**
33. **Câu 33**: *Sie (trang trọng) kommen bitte pünktlich.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Kommen Sie bitte pünktlich!", "Kommen Sie bitte pünktlich", "Bitte kommen Sie pünktlich!", "Bitte kommen Sie pünktlich"]`
  - Dịch nghĩa câu: *„Xin ngài hãy đến đúng giờ!“*
  - Giải thích: Đảo động từ nguyên thể lên trước `Sie` ➔ **`Kommen Sie`**.
34. **Câu 34**: *Du bist leise.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Sei leise!", "Sei leise"]`
  - Dịch nghĩa câu: *„Hãy trật tự!“*
  - Giải thích: `sein` là động từ bất quy tắc đặc biệt. Ở ngôi du, mệnh lệnh của nó là **`Sei`**.
35. **Câu 35**: *Ihr geht jetzt schlafen.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Geht jetzt schlafen!", "Geht jetzt schlafen"]`
  - Dịch nghĩa câu: *„Các con hãy đi ngủ ngay bây giờ!“*
  - Giải thích: Ngôi `ihr` chia là `geht`, bỏ `ihr` ➔ **`Geht jetzt schlafen!`**
36. **Câu 36**: *Du machst die Tür zu.* ➔ Hãy viết thành câu mệnh lệnh! (Lưu ý động từ tách)
- Đáp án chấp nhận: `["Mach die Tür zu!", "Mach die Tuer zu!", "Mach die Tür zu"]`
  - Dịch nghĩa câu: *„Hãy đóng cửa lại!“*
  - Giải thích: Động từ tách `zumachen`. Ngôi du là `du machst ... zu` ➔ Bỏ `st` và `du` ➔ **`Mach die Tür zu!`**
37. **Câu 37**: *Sie (trang trọng) rufen mich morgen an.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Rufen Sie mich morgen an!", "Rufen Sie mich morgen an"]`
  - Dịch nghĩa câu: *„Xin ngài hãy gọi cho tôi vào ngày mai!“*
  - Giải thích: Đảo `Rufen` lên đầu, tiền tố tách `an` vẫn ở cuối câu ➔ **`Rufen Sie ... an!`**.
38. **Câu 38**: *Du fährst langsamer.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Fahr langsamer!", "Fahr langsamer"]`
  - Dịch nghĩa câu: *„Hãy lái xe chậm lại!“*
  - Giải thích: Động từ `fahren` có biến âm ở ngôi du (du fährst). TUY NHIÊN, trong Imperativ, động từ có biến âm Umlaut (ä, ö, ü) sẽ bị **mất Umlaut** ➔ **`Fahr!`**
39. **Câu 39**: *Du zeichnest ein Bild.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Zeichne ein Bild!", "Zeichne ein Bild"]`
  - Dịch nghĩa câu: *„Hãy vẽ một bức tranh!“*
  - Giải thích: Động từ `zeichnen` có gốc tận cùng là `-nen` ➔ phải thêm đuôi `-e` ở mệnh lệnh ngôi du ➔ **`Zeichne!`**
40. **Câu 40**: *Ihr nehmt die Tabletten.* ➔ Hãy viết thành câu mệnh lệnh!
- Đáp án chấp nhận: `["Nehmt die Tabletten!", "Nehmt die Tabletten"]`
  - Dịch nghĩa câu: *„Các bạn hãy uống thuốc viên đi!“*
  - Giải thích: Ngôi `ihr` của nehmen là `nehmt`. Bỏ `ihr` ➔ **`Nehmt die Tabletten!`**

---

#### NHÓM 4: 🆕 ĐIỀN ĐẠI TỪ AKKUSATIV (`dien_dai_tu_akk` — 10 Câu: Câu 41 → Câu 50)
41. **Câu 41**: *„Ich liebe meine Eltern. Ich besuche ___ jedes Wochenende.“*
- Đáp án chấp nhận: `["sie"]`
  - Dịch nghĩa câu: *„Tôi yêu bố mẹ tôi. Tôi đến thăm họ mỗi cuối tuần.“*
  - Giải thích: `meine Eltern` (số nhiều) ➔ đại từ `sie` (họ). `besuchen` + Akkusativ ➔ vẫn là **`sie`**.
42. **Câu 42**: *„Das ist mein neuer Computer. Ich brauche ___ für die Arbeit.“*
- Đáp án chấp nhận: `["ihn"]`
  - Dịch nghĩa câu: *„Đó là chiếc máy tính mới của tôi. Tôi cần nó cho công việc.“*
  - Giải thích: `der Computer` (giống đực) ➔ đại từ `er`. `brauchen` + Akkusativ ➔ Akkusativ của `er` là **`ihn`**.
43. **Câu 43**: *„Wo ist Anna? Ich kann ___ nicht finden.“*
- Đáp án chấp nhận: `["sie"]`
  - Dịch nghĩa câu: *„Anna đâu rồi? Tôi không thể tìm thấy cô ấy.“*
  - Giải thích: `Anna` (giống cái) ➔ đại từ `sie` (cô ấy). `finden` + Akkusativ ➔ **`sie`**.
44. **Câu 44**: *„Wir haben ein neues Auto. Ich kaufe ___ morgen.“*
- Đáp án chấp nhận: `["es"]`
  - Dịch nghĩa câu: *„Chúng tôi có một chiếc ô tô mới. Tôi mua nó vào ngày mai.“*
  - Giải thích: `das Auto` (giống trung) ➔ đại từ `es`. `kaufen` + Akkusativ ➔ **`es`**.
45. **Câu 45**: *„Ihr seid meine besten Freunde. Ich vergesse ___ nie.“*
- Đáp án chấp nhận: `["euch"]`
  - Dịch nghĩa câu: *„Các bạn là những người bạn tốt nhất của tôi. Tôi sẽ không bao giờ quên các bạn.“*
  - Giải thích: `ihr` (các bạn). `vergessen` + Akkusativ ➔ Akkusativ của `ihr` là **`euch`**.
46. **Câu 46**: *„Herr Schmidt, der Chef möchte ___ sprechen.“*
- Đáp án chấp nhận: `["Sie"]`
  - Dịch nghĩa câu: *„Ngài Schmidt, sếp muốn nói chuyện với ngài.“*
  - Giải thích: Herr Schmidt ➔ xưng hô trang trọng (Sie). `sprechen` + Akkusativ ➔ **`Sie`** (viết hoa).
47. **Câu 47**: *„Der Salat ist lecker. Ich esse ___ gern.“*
- Đáp án chấp nhận: `["ihn"]`
  - Dịch nghĩa câu: *„Món salad ngon. Tôi thích ăn nó.“*
  - Giải thích: `der Salat` (giống đực) ➔ `er`. `essen` + Akkusativ ➔ **`ihn`**.
48. **Câu 48**: *„Das Buch ist interessant. Ich lese ___ jeden Abend.“*
- Đáp án chấp nhận: `["es"]`
  - Dịch nghĩa câu: *„Cuốn sách thật thú vị. Tôi đọc nó mỗi tối.“*
  - Giải thích: `das Buch` (giống trung) ➔ `es`. `lesen` + Akkusativ ➔ **`es`**.
49. **Câu 49**: *„Mein Bruder und ich spielen oft Fußball. Manchmal besucht unser Vater ___ beim Training.“*
- Đáp án chấp nhận: `["uns"]`
  - Dịch nghĩa câu: *„Anh trai tôi và tôi thường chơi bóng đá. Đôi khi bố chúng tôi đến thăm chúng tôi lúc tập luyện.“*
  - Giải thích: `Mein Bruder und ich` = wir (chúng tôi). `besuchen` + Akkusativ ➔ Akkusativ của `wir` là **`uns`**.
50. **Câu 50**: *„Hast du den Schlüssel? – Nein, ich habe ___ nicht gesehen.“*
- Đáp án chấp nhận: `["ihn"]`
  - Dịch nghĩa câu: *„Bạn có chìa khóa không? – Không, tôi chưa nhìn thấy nó.“*
  - Giải thích: `der Schlüssel` (giống đực) ➔ `er`. `sehen` + Akkusativ ➔ **`ihn`**.

---

#### NHÓM 5: 🆕 PHÂN LOẠI AKKUSATIV / DATIV (`phan_loai_cach` — 5 Câu: Câu 51 → Câu 55)
Mỗi hàng là **một câu**; xác định cụm **in đậm** thuộc **Akkusativ** hay **Dativ**. Đúng khi cả 4 hàng đúng. Rèn luyện tư duy phân biệt cách.
51. **Câu 51**:
- Hàng 1: *„Ich sehe **dich** jeden Tag.“* ➔ **Akkusativ** (`sehen` + Akk)
  - Hàng 2: *„Der Arzt hilft **mir**.“* ➔ **Dativ** (`helfen` + Dat)
  - Hàng 3: *„Wir treffen **ihn** morgen.“* ➔ **Akkusativ** (`treffen` + Akk)
  - Hàng 4: *„Das Auto gehört **uns**.“* ➔ **Dativ** (`gehören` + Dat)
  - Giải thích: Phân loại dựa trên động từ đi kèm.
52. **Câu 52**:
- Hàng 1: *„Der Kopf tut **ihm** weh.“* ➔ **Dativ** (`wehtun` + Dat)
  - Hàng 2: *„Sie liebt **mich**.“* ➔ **Akkusativ** (`lieben` + Akk)
  - Hàng 3: *„Passt **dir** die Hose?“* ➔ **Dativ** (`passen` + Dat)
  - Hàng 4: *„Ich brauche **es** nicht.“* ➔ **Akkusativ** (`brauchen` + Akk)
  - Giải thích: Phân loại dựa trên động từ đi kèm.
53. **Câu 53**:
- Hàng 1: *„Wie gefällt **Ihnen** das Hotel?“* ➔ **Dativ** (`gefallen` + Dat)
  - Hàng 2: *„Ich höre **euch** nicht.“* ➔ **Akkusativ** (`hören` + Akk)
  - Hàng 3: *„Er besucht **uns** am Sonntag.“* ➔ **Akkusativ** (`besuchen` + Akk)
  - Hàng 4: *„Ich danke **dir** für die Hilfe.“* ➔ **Dativ** (`danken` + Dat)
  - Giải thích: Phân loại dựa trên động từ đi kèm.
54. **Câu 54**:
- Hàng 1: *„Die Salbe hilft **ihr** sehr.“* ➔ **Dativ** (`helfen` + Dat)
  - Hàng 2: *„Manchmal sehe ich **sie** im Café.“* (cô ấy) ➔ **Akkusativ** (`sehen` + Akk)
  - Hàng 3: *„Steht **mir** das Kleid?“* ➔ **Dativ** (`stehen` + Dat)
  - Hàng 4: *„Ich kenne **Sie** nicht.“* (Ngài) ➔ **Akkusativ** (`kennen` + Akk)
  - Giải thích: Phân loại dựa trên động từ đi kèm.
55. **Câu 55**: (Câu khó - bẫy đại từ giống nhau)
- Hàng 1: *„Ich kaufe das Buch für **sie**.“* (cô ấy) ➔ **Akkusativ** (giới từ `für` + Akk)
  - Hàng 2: *„Das Buch gefällt **ihr**.“* ➔ **Dativ** (`gefallen` + Dat)
  - Hàng 3: *„Ich gebe **ihr** das Buch.“* ➔ **Dativ** (`geben` + Dat người nhận)
  - Hàng 4: *„Ich lese **es** jeden Tag.“* (cuốn sách) ➔ **Akkusativ** (`lesen` + Akk)
  - Giải thích: Chú ý giới từ 'für' và các động từ đi với 2 tân ngữ (geben).

---

#### NHÓM 6: PHÂN LOẠI `DER / DIE / DAS` (`phan_loai_giong` — 4 Câu: Câu 56 → Câu 59)
Mỗi câu: xếp **4 danh từ** vào đúng mạo từ. Đúng khi cả 4 đều đúng.
56. **Câu 56**: Xếp mạo từ đúng:
- `Kopf` (đầu) ➔ **der** (`der Kopf`)
  - `Hand` (bàn tay) ➔ **die** (`die Hand`)
  - `Auge` (mắt) ➔ **das** (`das Auge`)
  - `Zahn` (răng) ➔ **der** (`der Zahn`)
  - Giải thích: der Kopf, die Hand, das Auge, der Zahn.
57. **Câu 57**: Xếp mạo từ đúng:
- `Bauch` (bụng) ➔ **der** (`der Bauch`)
  - `Schulter` (vai) ➔ **die** (`die Schulter`)
  - `Knie` (đầu gối) ➔ **das** (`das Knie`)
  - `Finger` (ngón tay) ➔ **der** (`der Finger`)
  - Giải thích: der Bauch, die Schulter, das Knie, der Finger.
58. **Câu 58**: Xếp mạo từ đúng:
- `Fieber` (sốt) ➔ **das** (`das Fieber`)
  - `Erkältung` (cảm lạnh) ➔ **die** (`die Erkältung`)
  - `Husten` (ho) ➔ **der** (`der Husten`)
  - `Medikament` (thuốc men) ➔ **das** (`das Medikament`)
  - Giải thích: das Fieber, die Erkältung (đuôi -ung luôn là die), der Husten, das Medikament.
59. **Câu 59**: Xếp mạo từ đúng:
- `Apotheke` (nhà thuốc) ➔ **die** (`die Apotheke`)
  - `Rezept` (đơn thuốc) ➔ **das** (`das Rezept`)
  - `Schmerz` (cơn đau) ➔ **der** (`der Schmerz`)
  - `Tablette` (thuốc viên) ➔ **die** (`die Tablette`)
  - Giải thích: die Apotheke, das Rezept, der Schmerz, die Tablette.

---

#### NHÓM 7: NỐI Ô TỪ VỰNG TỪ TRÁI QUA PHẢI (`noi_o_tu_vung` — 8 Bài: Câu 60 → Câu 67)
60. **Câu 60 (Từ vựng Cơ thể 1)**:
- `der Bauch` ↔ `bụng`
  - `der Rücken` ↔ `lưng`
  - `die Schulter` ↔ `vai`
  - `die Brust` ↔ `ngực`
  - Giải thích: Các bộ phận phần thân trên.
61. **Câu 61 (Từ vựng Cơ thể 2)**:
- `der Fuß` ↔ `bàn chân`
  - `das Bein` ↔ `chân (từ đùi)`
  - `der Arm` ↔ `cánh tay`
  - `die Hand` ↔ `bàn tay`
  - Giải thích: Các bộ phận chi.
62. **Câu 62 (Số ít ↔ Số nhiều Cơ thể)**:
- `das Auge` ↔ `die Augen`
  - `das Ohr` ↔ `die Ohren`
  - `der Finger` ↔ `die Finger`
  - `der Zahn` ↔ `die Zähne`
  - Giải thích: Auge/Ohr thêm -n; Finger giữ nguyên; Zahn thêm Umlaut + e.
63. **Câu 63 (Từ vựng Y tế)**:
- `die Salbe` ↔ `thuốc mỡ`
  - `die Tablette` ↔ `thuốc viên`
  - `das Rezept` ↔ `đơn thuốc`
  - `das Medikament` ↔ `thuốc men`
  - Giải thích: Các vật dụng/thuốc tại nhà thuốc.
64. **Câu 64 (Triệu chứng bệnh)**:
- `das Fieber` ↔ `cơn sốt`
  - `der Schnupfen` ↔ `sổ mũi`
  - `der Husten` ↔ `bệnh ho`
  - `die Entzündung` ↔ `chứng viêm`
  - Giải thích: Các triệu chứng cảm lạnh thông thường.
65. **Câu 65 (Đại từ Nom ↔ Akk)**:
- `ich` ↔ `mich`
  - `du` ↔ `dich`
  - `wir` ↔ `uns`
  - `ihr` ↔ `euch`
  - Giải thích: Bảng biến đổi đại từ nhân xưng từ cách 1 sang cách 4.
66. **Câu 66 (Đại từ ngôi thứ 3 Nom ↔ Akk)**:
- `er` ↔ `ihn`
  - `sie (cô ấy)` ↔ `sie`
  - `es` ↔ `es`
  - `Sie (trang trọng)` ↔ `Sie`
  - Giải thích: Chỉ có giống đực (er) biến đổi thành ihn.
67. **Câu 67 (Câu hỏi ↔ Trả lời Bác sĩ)**:
- `Haben Sie einen Termin?` ↔ `Nein, leider nicht.`
  - `Was fehlt Ihnen denn?` ↔ `Ich habe Bauchschmerzen.`
  - `Waren Sie schon einmal bei uns?` ↔ `Ja, mein Name ist Schmidt.`
  - `Muss ich lange warten?` ↔ `Nehmen Sie bitte im Wartezimmer Platz.`
  - Giải thích: Logic hội thoại khi đăng ký khám bệnh.

---

#### NHÓM 8: ĐIỀN VÀO 2-3 CHỖ TRỐNG TẠO CÂU (`dien_tao_cau` — 5 Câu: Câu 68 → Câu 72)
68. **Câu 68**: Điền 2 từ để hoàn thành câu: *„Ở đây người ta không được phép hút thuốc.“* (man / rauchen)
- Khung câu hiển thị: `Hier [1] man nicht [2].`
  - Đáp án từng ô: [1] = `["darf"]`, [2] = `["rauchen"]`
  - Giải thích: Chủ ngữ `man` chia dürfen thành **`darf`**. Động từ chính **`rauchen`** nằm ở cuối câu ở dạng nguyên thể.
69. **Câu 69**: Điền 3 từ để hoàn thành câu: *„Bác sĩ, tôi có được phép chơi thể thao không?“* (ich / Sport / machen)
- Khung câu hiển thị: `Herr Doktor, [1] ich [2] [3]?`
  - Đáp án từng ô: [1] = `["darf"]`, [2] = `["Sport"]`, [3] = `["machen"]`
  - Giải thích: Câu hỏi nghi vấn: Đưa Modalverb **`darf`** lên đầu. **`Sport machen`** đứng cuối.
70. **Câu 70**: Điền 2 từ để hoàn thành câu: *„Đứa trẻ đang ngủ. Các con hãy trật tự!“* (ihr / sein / leise)
- Khung câu hiển thị: `Das Kind schläft. [1] [2]!`
  - Đáp án từng ô: [1] = `["Seid"]`, [2] = `["leise", "ruhig"]`
  - Giải thích: Imperativ ngôi ihr của động từ `sein` là **`Seid`**.
71. **Câu 71**: Điền 2 từ để hoàn thành câu: *„Bố yêu con. Con có yêu bố không?“* (ich / du)
- Khung câu hiển thị: `Ich liebe [1]. Liebst du [2]?`
  - Đáp án từng ô: [1] = `["dich"]`, [2] = `["mich"]`
  - Giải thích: `lieben` + Akkusativ. Yêu con -> **`dich`**, yêu bố (tôi) -> **`mich`**.
72. **Câu 72**: Điền 2 từ để hoàn thành câu: *„Cánh tay tôi đau. Tôi cần một loại thuốc mỡ.“* (weh / Salbe)
- Khung câu hiển thị: `Mein Arm tut mir [1]. Ich brauche eine [2].`
  - Đáp án từng ô: [1] = `["weh"]`, [2] = `["Salbe"]`
  - Giải thích: Động từ tách `wehtun` -> tut **`weh`**. Thuốc mỡ là **`Salbe`**.

---

#### NHÓM 9: NGHE GIỌNG BẢN XỨ `de-DE` VÀ ĐIỀN TỪ (`nghe_dien` — 8 Câu: Câu 73 → Câu 80)
*(Voice đọc toàn bộ câu nguyên vẹn, người học chỉ nghe và điền từ vào chỗ trống).*
73. **Câu 73**:
- `audio_text`: *"Geh jeden Tag spazieren!"*
  - `display_sentence`: *"___ jeden Tag spazieren!"*
  - `hint_vi`: *"Hãy đi dạo mỗi ngày!" (ngôi du)*
  - `accepted_answers`: `["Geh"]`
  - Giải thích: Imperativ của `gehen` ngôi du là **`Geh`**.
74. **Câu 74**:
- `audio_text`: *"Gute Besserung! Ruhen Sie sich aus."*
  - `display_sentence`: *"Gute Besserung! ___ Sie sich aus."*
  - `hint_vi`: *"Chúc mau khỏe! Ngài hãy nghỉ ngơi đi."*
  - `accepted_answers`: `["Ruhen"]`
  - Giải thích: Mệnh lệnh lịch sự của `sich ausruhen` là **`Ruhen Sie sich aus`**.
75. **Câu 75**:
- `audio_text`: *"Was fehlt Ihnen denn?"*
  - `display_sentence`: *"Was ___ Ihnen denn?"*
  - `hint_vi`: *"Ngài bị làm sao vậy?"*
  - `accepted_answers`: `["fehlt"]`
  - Giải thích: `fehlen` + Dativ dùng để hỏi thăm bệnh tình.
76. **Câu 76**:
- `audio_text`: *"Der Arzt schreibt mir ein Rezept."*
  - `display_sentence`: *"Der Arzt schreibt mir ein ___."*
  - `hint_vi`: *"Bác sĩ viết cho tôi một đơn thuốc."*
  - `accepted_answers`: `["Rezept"]`
  - Giải thích: Đơn thuốc là **`das Rezept`**.
77. **Câu 77**:
- `audio_text`: *"Wir dürfen hier nicht parken."*
  - `display_sentence`: *"Wir ___ hier nicht parken."*
  - `hint_vi`: *"Chúng tôi không được phép đỗ xe ở đây."*
  - `accepted_answers`: `["dürfen", "duerfen"]`
  - Giải thích: `wir` + **`dürfen`**.
78. **Câu 78**:
- `audio_text`: *"Du bist meine Traumfrau. Ich liebe dich."*
  - `display_sentence`: *"Du bist meine Traumfrau. Ich liebe ___."*
  - `hint_vi`: *"Em là người phụ nữ trong mơ của anh. Anh yêu em."*
  - `accepted_answers`: `["dich"]`
  - Giải thích: `lieben` + Akkusativ -> **`dich`**.
79. **Câu 79**:
- `audio_text`: *"Mein Bauch tut schrecklich weh."*
  - `display_sentence`: *"Mein ___ tut schrecklich weh."*
  - `hint_vi`: *"Bụng tôi đau kinh khủng."*
  - `accepted_answers`: `["Bauch"]`
  - Giải thích: Bụng là **`der Bauch`**.
80. **Câu 80**:
- `audio_text`: *"Nehmt täglich eine Tablette!"*
  - `display_sentence`: *"___ täglich eine Tablette!"*
  - `hint_vi`: *"Các bạn hãy uống mỗi ngày một viên thuốc!"*
  - `accepted_answers`: `["Nehmt"]`
  - Giải thích: Imperativ của `nehmen` ngôi ihr là **`Nehmt`**.

---

#### NHÓM 10: DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (`dich_cau_vd` — 6 Câu: Câu 81 → Câu 86, chấm đa đáp án)
81. **Câu 81**: Dịch câu sau sang tiếng Đức: ***"Ngài hãy uống nhiều nước!"*** (dùng động từ trinken)
- `accepted_answers`: `["Trinken Sie viel Wasser!", "Trinken Sie viel Wasser", "Bitte trinken Sie viel Wasser!"]`
  - Giải thích: Mệnh lệnh lịch sự: **`Trinken Sie + viel Wasser`**.
82. **Câu 82**: Dịch câu sau sang tiếng Đức: ***"Ở đây người ta không được phép hút thuốc."***
- `accepted_answers`: `["Hier darf man nicht rauchen.", "Man darf hier nicht rauchen.", "Hier darf man nicht rauchen"]`
  - Giải thích: man darf nicht = không được phép; rauchen (hút thuốc) để cuối câu.
83. **Câu 83**: Dịch câu sau sang tiếng Đức: ***"Hãy làm bài tập về nhà của bạn!"*** (nói với 1 người bạn - 'du', dùng 'deine Hausaufgaben')
- `accepted_answers`: `["Mach deine Hausaufgaben!", "Mach deine Hausaufgaben"]`
  - Giải thích: Imperativ ngôi du của `machen` là **`Mach`**.
84. **Câu 84**: Dịch câu sau sang tiếng Đức: ***"Tôi bị đau đầu dữ dội."*** (dùng 'starke Kopfschmerzen')
- `accepted_answers`: `["Ich habe starke Kopfschmerzen.", "Ich habe starke Kopfschmerzen"]`
  - Giải thích: Bị bệnh gì dùng động từ `haben` + tên bệnh.
85. **Câu 85**: Dịch câu sau sang tiếng Đức: ***"Các bạn hãy ăn nhiều rau hơn!"*** (dùng 'mehr Gemüse')
- `accepted_answers`: `["Esst mehr Gemüse!", "Esst mehr Gemüse", "Esst mehr Gemuese!"]`
  - Giải thích: Imperativ ngôi ihr của `essen` là **`Esst`**.
86. **Câu 86**: Dịch câu sau sang tiếng Đức: ***"Hãy nghỉ ngơi đi!"*** (nói với 1 người bạn, dùng 'sich ausruhen')
- `accepted_answers`: `["Ruh dich aus!", "Ruh dich aus", "Ruhe dich aus!"]`
  - Giải thích: Động từ phản thân tách. Ngôi du: **`ruh dich aus`**.

---

#### NHÓM 11: DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (`dich_cau_dv` — 6 Câu: Câu 87 → Câu 92, chấm đa đáp án)
87. **Câu 87**: Dịch câu sau sang tiếng Việt: ***„Atmen Sie bitte tief ein und aus!“***
- `accepted_answers`: `["Xin ngài hãy hít vào và thở ra thật sâu!", "Xin hãy hít vào và thở ra sâu!", "Hãy hít vào và thở ra thật sâu!"]`
  - Giải thích: `tief ein- und ausatmen` = hít sâu và thở ra.
88. **Câu 88**: Dịch câu sau sang tiếng Việt: ***„Der Rücken tut ihm weh.“***
- `accepted_answers`: `["Lưng của anh ấy bị đau.", "Anh ấy bị đau lưng.", "Lưng làm anh ấy đau."] `
  - Giải thích: Cấu trúc `wehtun` + Dativ (`ihm`).
89. **Câu 89**: Dịch câu sau sang tiếng Việt: ***„Darf ich hier fotografieren?“***
- `accepted_answers`: `["Tôi có được phép chụp ảnh ở đây không?", "Tôi có thể chụp ảnh ở đây không?", "Tôi chụp ảnh ở đây được không?"]`
  - Giải thích: `fotografieren` = chụp ảnh. `darf ich` = xin phép.
90. **Câu 90**: Dịch câu sau sang tiếng Việt: ***„Bleib heute im Bett!“***
- `accepted_answers`: `["Hôm nay hãy ở lại trên giường!", "Hãy nằm nghỉ trên giường hôm nay!", "Hôm nay hãy ở trên giường nhé!"]`
  - Giải thích: `Bleib` là mệnh lệnh ngôi du của `bleiben`. `im Bett` = trên giường.
91. **Câu 91**: Dịch câu sau sang tiếng Việt: ***„Wir sehen uns jeden Morgen im Bus.“***
- `accepted_answers`: `["Chúng ta gặp nhau mỗi sáng trên xe buýt.", "Chúng tôi gặp nhau mỗi sáng ở xe buýt.", "Chúng ta nhìn thấy nhau mỗi sáng trên xe buýt."] `
  - Giải thích: `sich sehen` = gặp/nhìn thấy nhau. `uns` ở đây là Akkusativ phản thân.
92. **Câu 92**: Dịch câu sau sang tiếng Việt: ***„Zeigen Sie mir Ihre Zunge!“***
- `accepted_answers`: `["Xin ngài hãy cho tôi xem lưỡi của ngài!", "Hãy cho tôi xem lưỡi của ngài!", "Xin hãy thè lưỡi ra!"]`
  - Giải thích: `zeigen` = chỉ/cho xem. `die Zunge` = lưỡi.

---

#### NHÓM 12: SẮP XẾP TỪ THÀNH CÂU (`sap_xep_cau` — 8 Câu: Câu 93 → Câu 100)
93. **Câu 93**: (Câu mệnh lệnh Sie)
- `tokens` (đã xáo trộn): `[Sie, viel Wasser, Trinken, bitte, !]`
  - `accepted_answers`: `["Trinken Sie bitte viel Wasser!", "Bitte trinken Sie viel Wasser!"]`
  - Dịch nghĩa câu: *„Xin ngài hãy uống nhiều nước!“*
94. **Câu 94**: (Câu mệnh lệnh ihr)
- `tokens`: `[eure Zimmer, Räumt, auf, !]`
  - `accepted_answers`: `["Räumt eure Zimmer auf!"]`
  - Dịch nghĩa câu: *„Các con hãy dọn dẹp phòng của mình đi!“*
  - Giải thích: Động từ tách `aufräumen`, tiền tố `auf` đứng cuối.
95. **Câu 95**: (Câu mệnh lệnh du)
- `tokens`: `[weniger, Iss, Schokolade, !]`
  - `accepted_answers`: `["Iss weniger Schokolade!"]`
  - Dịch nghĩa câu: *„Hãy ăn ít sô cô la lại!“*
96. **Câu 96**: (Modalverb dürfen cấm đoán)
- `tokens`: `[darf, man, Hier, rauchen, nicht, .]`
  - `accepted_answers`: `["Hier darf man nicht rauchen.", "Man darf hier nicht rauchen."] `
  - Dịch nghĩa câu: *„Ở đây người ta không được phép hút thuốc.“*
97. **Câu 97**: (Đại từ Akkusativ)
- `tokens`: `[dich, Ich, jeden Tag, vermisse, .]`
  - `accepted_answers`: `["Ich vermisse dich jeden Tag.", "Jeden Tag vermisse ich dich."] `
  - Dịch nghĩa câu: *„Anh nhớ em mỗi ngày.“* (`vermissen` + Akk).
98. **Câu 98**: (Đại từ Akkusativ & Dativ hỗn hợp)
- `tokens`: `[verschreibt, Der Arzt, ein Medikament, mir, .]`
  - `accepted_answers`: `["Der Arzt verschreibt mir ein Medikament."] `
  - Dịch nghĩa câu: *„Bác sĩ kê cho tôi một loại thuốc.“*
  - Giải thích: Dativ (`mir`) đứng trước Akkusativ (`ein Medikament`).
99. **Câu 99**: (Bệnh tật)
- `tokens`: `[starke, habe, Ich, Zahnschmerzen, .]`
  - `accepted_answers`: `["Ich habe starke Zahnschmerzen."] `
  - Dịch nghĩa câu: *„Tôi bị đau răng nặng.“*
100. **Câu 100**: (Modalverb xin phép)
- `tokens`: `[ins Kino, wir, heute Abend, Dürfen, gehen, ?]`
  - `accepted_answers`: `["Dürfen wir heute Abend ins Kino gehen?"] `
  - Dịch nghĩa câu: *„Tối nay chúng con có được đi xem phim không?“*

---

#### NHÓM 13: TÌM LỖI VÀ SỬA CÂU (`tim_loi_sai` — 6 Câu: Câu 101 → Câu 106)
Mỗi câu có **đúng 1 lỗi**. Người học gõ lại **cả câu đúng**.
101. **Câu 101**: (Sai chia Imperativ du)
- `wrong_sentence`: *„Arbeit nicht so viel!“*
  - `accepted_answers`: `["Arbeite nicht so viel!"]`
  - Dịch nghĩa câu đúng: *„Đừng làm việc nhiều quá!“*
  - Giải thích: Động từ `arbeiten` kết thúc bằng `t`, Imperativ ngôi du phải thêm `e` ➔ **`Arbeite!`**
102. **Câu 102**: (Sai chia dürfen số nhiều)
- `wrong_sentence`: *„Die Kinder darfen hier spielen.“*
  - `accepted_answers`: `["Die Kinder dürfen hier spielen."] `
  - Dịch nghĩa câu đúng: *„Bọn trẻ được phép chơi ở đây.“*
  - Giải thích: Ngôi số nhiều của dürfen là `dürfen`, không bị biến âm `ü` thành `a`.
103. **Câu 103**: (Sai Akkusativ/Dativ)
- `wrong_sentence`: *„Ich liebe dir.“*
  - `accepted_answers`: `["Ich liebe dich."] `
  - Dịch nghĩa câu đúng: *„Tôi yêu bạn.“*
  - Giải thích: `lieben` + Akkusativ. Akkusativ của `du` là **`dich`**, không phải `dir`.
104. **Câu 104**: (Sai chia Imperativ ihr)
- `wrong_sentence`: *„Trinkt ihr viel Wasser!“*
  - `accepted_answers`: `["Trinkt viel Wasser!"] `
  - Dịch nghĩa câu đúng: *„Các bạn hãy uống nhiều nước!“*
  - Giải thích: Imperativ ngôi `ihr` phải **BỎ từ `ihr`** đi.
105. **Câu 105**: (Sai chia dürfen ngôi 3 số ít)
- `wrong_sentence`: *„Er darft heute nicht rausgehen.“*
  - `accepted_answers`: `["Er darf heute nicht rausgehen."] `
  - Dịch nghĩa câu đúng: *„Hôm nay anh ấy không được phép ra ngoài.“*
  - Giải thích: Ngôi er/sie/es của dürfen KHÔNG có đuôi `t` ➔ chỉ là **`darf`**.
106. **Câu 106**: (Sai chia Imperativ động từ tách)
- `wrong_sentence`: *„Ruhen aus Sie sich!“*
  - `accepted_answers`: `["Ruhen Sie sich aus!"] `
  - Dịch nghĩa câu đúng: *„Xin ngài hãy nghỉ ngơi!“*
  - Giải thích: Động từ tách `ausruhen`, tiền tố `aus` phải nằm cuối câu.

---

#### NHÓM 14: DỊCH TỪ VIỆT → ĐỨC (`dich_nghia_vd` — 4 Câu: Câu 107 → Câu 110)
107. **Câu 107**: Dịch kèm mạo từ: *"cái mũi"* ➔ `["die Nase"]`
108. **Câu 108**: Dịch kèm mạo từ: *"bác sĩ gia đình (nam)"* ➔ `["der Hausarzt", "Hausarzt"]`
109. **Câu 109**: Dịch kèm mạo từ: *"đơn thuốc"* ➔ `["das Rezept", "Rezept"]`
110. **Câu 110**: Dịch kèm mạo từ: *"trái tim"* ➔ `["das Herz", "Herz"]`

---

#### NHÓM 15: DỊCH TỪ ĐỨC → VIỆT (`dich_nghia_dv` — 4 Câu: Câu 111 → Câu 114)
111. **Câu 111**: Dịch: *"die Schulter"* ➔ `["vai", "cái vai"]`
112. **Câu 112**: Dịch: *"die Apotheke"* ➔ `["nhà thuốc", "hiệu thuốc", "tiệm thuốc"]`
113. **Câu 113**: Dịch: *"das Bein"* ➔ `["chân", "cái chân"]`
114. **Câu 114**: Dịch: *"der Schnupfen"* ➔ `["sổ mũi", "bệnh sổ mũi"]`

---

#### NHÓM 16: ĐỌC HIỂU ĐÚNG / SAI — RICHTIG / FALSCH (`dung_sai` — 4 Câu: Câu 115 → Câu 118)
**Đoạn văn: Tipps für die Gesundheit (Mẹo giữ sức khỏe)**
> *„Um gesund zu bleiben, müssen Sie auf Ihren Körper achten. Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine. Trinken Sie täglich mindestens zwei Liter Wasser. Trinken Sie nicht zu viel Kaffee oder Alkohol. Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge. Wenn Sie am Computer arbeiten, machen Sie oft Pausen für Ihre Augen. Und vergessen Sie nicht: Bewegen Sie sich jeden Tag!“*
> **Dịch:** *„Để giữ sức khỏe, ngài phải chú ý đến cơ thể mình. Hãy ăn nhiều trái cây và rau củ, vì chúng có nhiều vitamin. Hãy uống ít nhất hai lít nước mỗi ngày. Đừng uống quá nhiều cà phê hoặc rượu. Ngài cũng không được phép hút thuốc, điều đó rất tệ cho phổi. Khi ngài làm việc trên máy tính, hãy thường xuyên nghỉ ngơi cho đôi mắt. Và đừng quên: Hãy vận động mỗi ngày!“*

115. **Câu 115**: Mệnh đề: *„Man soll jeden Tag zwei Liter Kaffee trinken.“*
- Đáp án: **Falsch (Sai)**
  - Dịch nghĩa mệnh đề: *Người ta nên uống 2 lít cà phê mỗi ngày.*
  - Giải thích: Đoạn văn khuyên uống hai lít nước (Wasser), không phải cà phê (Kaffee). Cà phê khuyên không nên uống nhiều.
116. **Câu 116**: Mệnh đề: *„Rauchen ist gesund.“*
- Đáp án: **Falsch (Sai)**
  - Dịch nghĩa mệnh đề: *Hút thuốc thì khỏe mạnh.*
  - Giải thích: Đoạn văn ghi rõ "Sie dürfen auch nicht rauchen, das ist sehr schlecht für die Lunge" (Hút thuốc rất tệ cho phổi).
117. **Câu 117**: Mệnh đề: *„Gemüse und Obst haben Vitamine.“*
- Đáp án: **Richtig (Đúng)**
  - Dịch nghĩa mệnh đề: *Rau củ và trái cây có vitamin.*
  - Giải thích: Đoạn văn có câu "Essen Sie viel Obst und Gemüse, denn sie haben viele Vitamine".
118. **Câu 118**: Mệnh đề: *„Man muss am Computer keine Pausen machen.“*
- Đáp án: **Falsch (Sai)**
  - Dịch nghĩa mệnh đề: *Người ta không cần nghỉ ngơi khi dùng máy tính.*
  - Giải thích: Đoạn văn khuyên "machen Sie oft Pausen für Ihre Augen" (hãy nghỉ ngơi thường xuyên cho mắt).

---

#### NHÓM 17: SẮP XẾP HỘI THOẠI (`hoi_thoai_sap_xep` — 3 Câu: Câu 119 → Câu 121)
Mỗi ô là **một lượt lời** (kèm nhãn người nói). Người học bấm theo đúng thứ tự.
119. **Câu 119 (Beim Arzt - Tại phòng khám)**
- `lines` (thứ tự đúng — web phải xáo trộn khi hiển thị):
  1. **Arzt**: Guten Tag, Herr Klein. Was fehlt Ihnen denn?
  2. **Herr Klein**: Guten Tag. Ich habe seit gestern starke Bauchschmerzen.
  3. **Arzt**: Haben Sie auch Fieber?
  4. **Herr Klein**: Ja, ein bisschen. Mir ist sehr warm.
  5. **Arzt**: Legen Sie sich bitte auf die Liege. Ich untersuche Ihren Bauch.
- `correct_order`: `[1, 2, 3, 4, 5]`
  - Giải thích: Bác sĩ chào hỏi -> Bệnh nhân kể bệnh (đau bụng) -> Bác sĩ hỏi thêm triệu chứng (sốt) -> Bệnh nhân xác nhận -> Bác sĩ yêu cầu nằm xuống để khám.
120. **Câu 120 (In der Apotheke - Tại nhà thuốc)**
- `lines`:
  1. **Apothekerin**: Guten Tag! Wie kann ich Ihnen helfen?
  2. **Kunde**: Guten Tag! Ich habe ein Rezept vom Arzt. Hier, bitte.
  3. **Apothekerin**: Danke. Einen Moment... Hier ist Ihr Medikament.
  4. **Kunde**: Wie oft muss ich die Tabletten nehmen?
  5. **Apothekerin**: Nehmen Sie zweimal täglich eine Tablette nach dem Essen.
  6. **Kunde**: Vielen Dank. Auf Wiedersehen!
- `correct_order`: `[1, 2, 3, 4, 5, 6]`
  - Giải thích: Chào -> Đưa đơn thuốc -> Đưa thuốc -> Hỏi cách dùng -> Hướng dẫn cách dùng -> Cảm ơn.
121. **Câu 121 (Mẹ và con - Imperativ & Dürfen)**
- `lines`:
  1. **Sohn**: Mama, ich bin fertig mit den Hausaufgaben. Darf ich jetzt rausgehen?
  2. **Mutter**: Regnet es draußen?
  3. **Sohn**: Nein, es regnet nicht. Die Sonne scheint.
  4. **Mutter**: Gut, du darfst eine Stunde auf dem Spielplatz spielen. Aber zieh eine Jacke an! Es ist kalt.
  5. **Sohn**: Danke, Mama! Mach ich.
- `correct_order`: `[1, 2, 3, 4, 5]`
  - Giải thích: Con xin phép ra ngoài -> Mẹ hỏi thời tiết -> Con trả lời trời nắng -> Mẹ cho phép nhưng dặn mặc áo khoác (Imperativ) -> Con cảm ơn.

---

#### NHÓM 18: 🆕 NHÌN BIỂU TƯỢNG ĐOÁN BỆNH (`bieu_tuong_benh` — 4 Câu: Câu 122 → Câu 125)
Hiển thị **biểu tượng lớn** (emoji, có `alt` tiếng Việt); chọn **câu tiếng Đức** đúng. Voice đọc **câu đúng**, không đọc tên emoji.
122. **Câu 122**: Emoji hiển thị: 🤒 (Mặt ngậm nhiệt kế)
- Lựa chọn: `A. Ich habe Fieber.` (Đúng) | `B. Ich habe Zahnschmerzen.` | `C. Mein Knie tut weh.` | `D. Ich habe Schnupfen.`
  - Dịch nghĩa câu đúng: *„Tôi bị sốt.“*
  - Giải thích: Biểu tượng ngậm nhiệt kế biểu thị bệnh Sốt (`Fieber`).
123. **Câu 123**: Emoji hiển thị: 🤧 (Mặt xì mũi)
- Lựa chọn: `A. Mein Bauch tut weh.` | `B. Ich habe Husten.` | `C. Ich habe Schnupfen.` (Đúng) | `D. Ich bin gesund.`
  - Dịch nghĩa câu đúng: *„Tôi bị sổ mũi.“*
  - Giải thích: Biểu tượng xì mũi bằng khăn giấy biểu thị bệnh Sổ mũi (`Schnupfen`).
124. **Câu 124**: Emoji hiển thị: 🤕 (Đầu quấn băng)
- Lựa chọn: `A. Ich habe Kopfschmerzen.` (Đúng) | `B. Mein Bein tut weh.` | `C. Ich habe Husten.` | `D. Ich bin müde.`
  - Dịch nghĩa câu đúng: *„Tôi bị đau đầu.“*
  - Giải thích: Biểu tượng đầu quấn băng biểu thị chứng Đau đầu (`Kopfschmerzen`).
125. **Câu 125**: Emoji hiển thị: 🤢 (Mặt xanh xao buồn nôn)
- Lựa chọn: `A. Ich habe Zahnschmerzen.` | `B. Mein Bauch tut weh.` (Đúng) | `C. Ich habe Schnupfen.` | `D. Mein Fuß tut weh.`
  - Dịch nghĩa câu đúng: *„Bụng tôi bị đau.“*
  - Giải thích: Biểu tượng buồn nôn liên quan đến bệnh Đau dạ dày/Đau bụng (`Bauchschmerzen / Bauch tut weh`).

---

## PHẦN 4: HỆ THỐNG SINH ĐỀ NGẪU NHIÊN VÔ HẠN & DỮ LIỆU NGUỒN CHUẨN (`SINGLE SOURCE OF TRUTH`)

### 4.1. Mục tiêu & nguyên tắc
Trong chế độ "Luyện Phản Xạ Ngẫu Nhiên", sử dụng các Engine sau để tự động tạo ra hàng triệu câu hỏi không trùng lặp (duy trì quy mô 125 câu/bộ đề với tỉ lệ phân bổ như mục 3.1).
* **Hạt giống (`seed`)** được lưu cùng bộ đề để tái hiện lỗi.
* **Mọi câu sinh ra đều phải đi qua `check_imperativ_rules()`** — vi phạm quy tắc (vd: có chữ du/ihr) thì **bỏ câu và sinh lại**.

### 4.2. DỮ LIỆU NGUỒN CHUẨN (Phụ lục B)
* `BODY_PARTS`: dict chứa 25 từ vựng cơ thể kèm giới tính (der/die/das).
* `ILLNESSES`: Fieber, Schnupfen, Husten, Erkältung, ...
* `PRONOUN_TABLE`: Map `ich->mich/mir`, `du->dich/dir`, `er->ihn/ihm`, v.v.
* `VERB_CASES`: Phân loại động từ. Nhóm AKK: `lieben, treffen, sehen, anrufen`. Nhóm DAT: `helfen, wehtun, passen, gefallen`.

### 4.3. CÁC ENGINE SINH ĐỀ
| Mã | Tên Engine | Chức năng (Sinh vô hạn) |
| :-: | :--- | :--- |
| **E1** | **Imperativ Generator** | Nhận Input là (Động từ, Ngôi du/ihr/Sie). Áp dụng logic biến đổi: Nếu `Sie` -> V + Sie. Nếu `ihr` -> V + t. Nếu `du` -> V (áp dụng rules: mất biến âm ä, giữ i/ie, bỏ -st, đuôi d/t thêm e). Output ra câu Mệnh lệnh chuẩn. |
| **E2** | **Pronoun Case Classifier** | Random 1 động từ từ `VERB_CASES` và 1 đại từ Nominativ. Đặt vào câu `Ich [verb] [pronoun]`. Engine tự tính toán Cách (Dat/Akk) và xuất ra đại từ đích chính xác (mich/mir). Phục vụ bài điền từ, tìm lỗi sai. |
| **E3** | **Dürfen Constructor** | Chọn ngẫu nhiên 1 chủ ngữ (ich, die Frau, wir...). Chia `dürfen` tương ứng. Gắn thêm 1 động từ nguyên mẫu ở cuối câu. Sinh ra vô số câu "Được phép / Cấm". |

### 4.4. HÀM `check_imperativ_rules()` — BẮT BUỘC CHẠY CHO MỌI CÂU MỆNH LỆNH
```python
import re

def check_imperativ_rules(sentence, person):
    """Kiểm tra một câu mệnh lệnh đã sinh ra có đúng quy tắc hay không."""
    toks = re.findall(r"[A-Za-zÄÖÜäöüß\-]+", sentence)
    low = [t.lower() for t in toks]
    errs = []
    
    if person in ["du", "ihr"]:
        if "du" in low or "ihr" in low:
            errs.append("Lỗi R1: Câu mệnh lệnh du/ihr không được chứa chủ ngữ du/ihr.")
            
    if person == "Sie":
        if "sie" not in low: # lowercase check
            errs.append("Lỗi R1: Câu mệnh lệnh Sie bắt buộc phải có chữ Sie.")
            
    # Bổ sung check đuôi -st, check biến âm tùy thuộc vào độ phức tạp của logic.
    return errs
```

---

## PHẦN 5: KIỂM THỬ TOÀN DIỆN & QA ZERO-BUG (`verify_lesson12_qa.py`)

> **Yêu cầu bắt buộc**: Sau khi code xong, Antigravity IDE phải **viết và chạy** `verify_lesson12_qa.py` (hoặc pytest tương đương), **sửa mọi lỗi** cho đến khi toàn bộ test đạt, rồi **dán báo cáo kết quả** theo mẫu mục 5.5.

### 5.1. Bảng đối chiếu: lỗi cũ → kiểm tra tự động
| # | Lỗi đã từng gặp | Kiểm tra tự động (phải đạt) |
| :-: | :--- | :--- |
| 1 | Dịch sai nghĩa | Với 100% câu: phần dịch không rỗng. Câu mệnh lệnh phải có chữ "Hãy", "Xin", "Đừng". |
| 2 | Dịch / đáp án không liên quan đề | Mỗi câu: `explanation` **chứa chuỗi đáp án đúng** (chuẩn hóa); ghép đáp án vào `display_sentence` → khớp `audio_text` (với `nghe_dien`). |
| 3 | Voice thiếu / sai | Mọi nút `🔊` có `speak_text` không rỗng; `speak_text` **không chứa** `[_→€°\[\]/]`, emoji, dấu chấm than `!`, dấu hỏi `?`. |
| 4 | Câu hỏi trùng nhau | `len(set(normalize(q))) == 125`; so sánh thêm với toàn bộ câu của **Bài 1-11**. |
| 5 | Làm hỏng bài cũ | `Zero-Regression Check` mục 5.2. |

### 5.2. Kiểm tra không phá bài cũ (`Zero-Regression Check`)
1. **Trước khi code**: lưu **băm SHA-256** của toàn bộ file bài cũ (`lessons/a1/seed_a1_b*.py`, `verbs_db.js`, `lexikon_db.js`, `arena_generator.py`) vào `baseline_hashes.json`.
2. **Sau khi code**: so sánh băm. Với `seed_a1_b1…b11.py`: **giữ nguyên 100%**. Với `verbs_db.js`, `lexikon_db.js`, `arena_generator.py`: chỉ được **thêm** dòng (`git diff --numstat`: số dòng xóa = 0).
3. **Kiểm tra giao diện cũ**: mở **Bài 10, 11**, chạy thử mỗi dạng bài → kết quả y như trước; **không có lỗi trong Console**.

### 5.3. Danh sách test tự động bắt buộc trong `verify_lesson12_qa.py`
| Nhóm | Test | Mô tả |
| :--- | :--- | :--- |
| **Dữ liệu** | `test_lexikon_counts` | 50 thẻ mới (trừ trùng); mỗi thẻ có `article`, `plural`, `meaning_vi`, `example_de`, `example_vi`. |
| | `test_verbs_imperativ_forms` | 25 động từ: bảng chia 6 ngôi Präsens + 3 ngôi Imperativ khớp công thức ngoại lệ (essen->iss, fahren->fahr, warten->warte). |
| **Engine** | `test_imperativ_engine` | 500 câu sinh ngẫu nhiên: Vượt qua `check_imperativ_rules`. |
| | `test_pronoun_classifier` | Động từ `helfen, wehtun, gehören` -> sinh ra `mir/dir...`. Động từ `lieben, treffen` -> sinh ra `mich/dich...`. |
| **Bài tập cố định** | `test_125_questions` | Đúng 125 câu; phân bổ 18 dạng đúng theo bảng 3.1; mã câu 1–125 liên tục. |
| | `test_unique_questions` | Không trùng sau chuẩn hóa. |
| | `test_every_question_has_translation_and_explanation` | Không rỗng; giải thích chứa đáp án. |
| **Hồi quy** | `test_zero_regression` | Theo mục 5.2. |

### 5.4. Danh sách kiểm tra thủ công cuối cùng (người thật rà soát)
1. Mở Bài 12, đọc **toàn bộ lý thuyết**: không ô trống, không bản dịch thiếu, không bảng vỡ cột. Đảm bảo bảng Imperativ thể hiện rõ việc mất/giữ biến âm.
2. Bấm `🔊` ở **mọi** bảng, sơ đồ. Voice phát âm sạch.
3. Làm thử **một câu mỗi dạng** (18 dạng) ở chế độ đúng và chế độ sai: kiểm tra *Dịch nghĩa* và *Giải thích* khớp đáp án. Đặc biệt check 3 component mới.
4. Làm đủ **125/125**: thanh tiến độ, EXP, huy hiệu lưu bình thường.
5. Chuyển sang **Bài 11**: các bài vẫn hoạt động (Zero Regression).

### 5.5. Mẫu báo cáo cuối cùng (bắt buộc dán vào terminal)
```
BÁO CÁO QA BÀI 12
- Số câu hỏi: 125 / 125 (Đúng phân bổ 18 dạng)                 [ĐẠT]
- Câu trùng nhau: 0                                            [ĐẠT]
- Thẻ từ vựng thêm mới / bỏ qua vì trùng: X / Y
- Thẻ động từ thêm mới / bỏ qua vì trùng: X / Y
- Logic Imperativ xử lý đúng ngoại lệ biến âm (essen, fahren)  [ĐẠT]
- Test TTS sạch (100% nút 🔊)                                  [ĐẠT]
- Zero-Regression (băm Bài 1–11 không đổi, git diff k xóa dòng)[ĐẠT]
- Giao diện Bài 10, 11 vẫn chạy đúng                           [ĐẠT]
- Các lỗi đã phát hiện và đã sửa: (liệt kê)
```

*Hết đặc tả Bài 12. Nhắc lại ba nguyên tắc cuối cùng cho Antigravity IDE: **(1)** không động chạm bài cũ; **(2)** mọi dữ liệu (đề, đáp án, dịch, giải thích, voice) phải sinh từ một nguồn; **(3)** chạy kiểm thử và dán báo cáo trước khi báo hoàn thành.*