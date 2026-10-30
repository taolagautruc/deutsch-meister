# 📋 BÁO CÁO KIỂM LỖI CHUYÊN MÔN TIẾNG ĐỨC - DEUTSCHMEISTER (BÀI 1 - P1)

Tài liệu này tổng hợp toàn bộ các lỗi sai và điểm cần chuẩn hóa về **ngữ âm (Phonetics/IPA), chính tả (Orthografie), từ vựng (Wortschatz), ngữ dụng học (Pragmatik) và logic dữ liệu** được phát hiện qua rà soát chi tiết trên giao diện Bài 1 (P1).

File được thiết kế theo cấu trúc: **Vị trí -> Nội dung hiện tại -> Phân tích lỗi chuyên môn -> Nội dung chuẩn cần thay thế**, giúp AI/IDE có thể tìm kiếm (search) chuỗi văn bản cũ và thay thế (replace) chính xác vào mã nguồn.

---

## 🚨 PHẦN 1: CÁC LỖI NGHIÊM TRỌNG VỀ NGỮ ÂM & CHÍNH TẢ (CẦN SỬA NGAY)

### 1. Lỗi sai bản chất ngữ âm của tổ hợp `-er` (Mục 2A: Nguyên âm đôi & Tổ hợp có -r)
* **Vị trí:** Mục `2. QUY TẮC ĐÁNH VẦN NGUYÊN ÂM GHÉP & PHỤ ÂM` -> Cột `A. Nguyên âm đôi & Tổ hợp có -r` -> Dòng cuối cùng (`er`).
* **Nội dung hiện tại:**
  ```text
  er (ơ): der, wer, woher
  ```
* **Phân tích lỗi chuyên môn:**
  * Đuôi `-er` chỉ đọc thành âm **ơ ngắn** (`[ɐ]` - Tiefschwa) khi nó nằm ở **âm tiết KHÔNG nhấn trọng âm** (thường ở cuối từ đa âm tiết như *Vater, Mutter, Lehrer, Verkäufer, immer, oder, aber*).
  * Trong các từ đơn âm tiết hoặc nhấn trọng âm vào âm tiết cuối như **`der`** (`/deːɐ̯/`), **`wer`** (`/veːɐ̯/`), **`woher`** (`/voˈheːɐ̯/`), chữ `e` là nguyên âm dài được nhấn trọng âm kết hợp với `r` nguyên âm hóa, bắt buộc phải đọc là **ê-ơ** (`[eːɐ̯]`), tuyệt đối **không đọc là "ơ"** (nếu đọc thành *đơ, vơ, vô-hơ* là sai hoàn toàn phát âm tiếng Đức).
* **Đề xuất sửa thành:**
  ```text
  er (cuối từ không nhấn trọng âm -> đọc là ơ ngắn [ɐ]): Vater, Mutter, oder, Verkäufer | er (nhấn trọng âm -> đọc là ê-ơ [eːɐ̯]): der, wer, woher
  ```

---

### 2. Lỗi sai độ dài nguyên âm trong tổ hợp `ir` vs `ier` & xếp nhầm từ `vier` (Mục 2A)
* **Vị trí:** Mục `2. QUY TẮC ĐÁNH VẦN NGUYÊN ÂM GHÉP & PHỤ ÂM` -> Cột `A. Nguyên âm đôi & Tổ hợp có -r` -> Dòng 2 (`ie`) và Dòng 4 (`ir | ier`).
* **Nội dung hiện tại:**
  * Dòng 2: `• ie [i:] -> đọc là i kéo dài (tuyệt đối không đọc "đai"): die, Sie, vier, sieben`
  * Dòng 4: `• ir (i-ơ ngắn): mir, dir | ier (i-ơ dài): hier, Bier, Tier`
* **Phân tích lỗi chuyên môn:**
  1. **Tại dòng 4 (`ir` vs `ier`):** Các đại từ đơn âm tiết như **`mir`** (`/miːɐ̯/`), **`dir`** (`/diːɐ̯/`), **`wir`** (`/viːɐ̯/`) có nguyên âm `i` là **nguyên âm dài (`/iː/`)**, phát âm là **i-ơ dài (`[iːɐ̯]`)** và bắt vần giống hệt 100% với `hier, Bier, Tier`. Tổ hợp `ir` chỉ đọc thành **i-ơ ngắn (`[ɪɐ̯]`)** khi theo sau nó là một phụ âm khác trong cùng âm tiết (ví dụ: *Kirche, Birne, Schirm, Wirtschaft*).
  2. **Tại dòng 2 (`ie [i:]`):** Từ **`vier`** (`/fiːɐ̯/`) có chữ `r` ở cuối nên âm `r` bị nguyên âm hóa thành `[ɐ̯]`, đọc là **ph-i-ơ (`[fiːɐ̯]`)** giống hệt *hier, Bier, Tier*, chứ không đọc là âm `[iː]` thuần túy như *die, Sie, sieben*. Do đó, cần chuyển `vier` từ dòng `ie [i:]` xuống dòng `ier [iːɐ̯]`.
* **Đề xuất sửa thành:**
  * Dòng 2:
    ```text
    • ie [i:] -> đọc là i kéo dài (tuyệt đối không đọc "đai"): die, Sie, wie, sieben
    ```
  * Dòng 4:
    ```text
    • ir (i-ơ ngắn [ɪɐ̯]): Kirche, Birne, Schirm | ir / ier (i-ơ dài [iːɐ̯]): mir, dir, wir, vier, hier, Bier, Tier
    ```

---

### 3. Lỗi viết hoa liên từ trong tiêu đề tiếng Đức (Menu danh mục bài học bên trái)
* **Vị trí:** Cột `DANH MỤC BÀI HỌC` bên trái -> `Bài 1 (P2)`.
* **Nội dung hiện tại:**
  ```text
  Bài 1 (P2): "Kaffee Oder Tee...
  ```
* **Phân tích lỗi chuyên môn:**
  * Trong quy tắc chính tả tiếng Đức (Rechtschreibung), tiếng Đức **không viết hoa tất cả các từ trong tiêu đề** (Title Case) như tiếng Anh. Chỉ viết hoa chữ cái đầu câu và Danh từ (Nomen).
  * Từ `oder` là liên từ (Konjunktion) nên bắt buộc phải viết thường là **`oder`** (tương tự như Bài 2: *"Sprache im Kurs"* và Bài 4: *"Menschen und Häuser"* đã viết thường chữ *im* và *und*).
* **Đề xuất sửa thành:**
  ```text
  Bài 1 (P2): "Kaffee oder Tee...
  ```

---

## ⚠️ PHẦN 2: CÁC LỖI NGỮ ÂM, BẢNG CHỮ CÁI & QUY TẮC ĐÁNH VẦN CẦN CHUẨN HÓA

### 4. Chuẩn hóa mô tả phát âm Bảng chữ cái (`Ll`, `Jj`, `Rr`, `Ff`, `Ss`)
* **Vị trí:** Mục `1. BẢNG CHỮ CÁI TIẾNG ĐỨC (DAS ALPHABET)`.
* **Chi tiết các ô chữ cái cần sửa:**
  1. **Ô chữ `Ll` (`/ɛl/`):**
     * *Hiện tại:* `đọc như en-lờ`
     * *Phân tích lỗi:* Đây là nguyên nhân hàng đầu khiến người Việt phát âm sai chữ `L` trong tiếng Đức thành âm mũi `n` (*en*). Trong tiếng Đức, tên chữ cái `L` là `/ɛl/` (1 âm tiết: mở miệng đọc âm *e* ngắn rồi uốn đầu lưỡi chạm lợi hàm trên), **hoàn toàn không có âm "n"**.
     * *Đề xuất sửa:* `đọc như e-l (cong lưỡi chạm hàm trên, không đọc "en")`
  2. **Ô chữ `Jj` (`/jɔt/`):**
     * *Hiện tại:* `đọc như dốt`
     * *Phân tích lỗi:*
       * Thứ nhất, nguyên âm `/ɔ/` trong `/jɔt/` là âm **o ngắn mở** (vần với *Gott*), không phải âm *ô* đóng (*dốt*).
       * Thứ hai, ghi chữ "d" chỉ đúng với người miền Nam (phát âm D thành `/j/`), còn người miền Bắc đọc chữ "d" sẽ thành âm `/z/`, dẫn đến đọc sai toàn bộ các từ có chữ `J` (*ja, Jahr, jung*).
     * *Đề xuất sửa:* `đọc như i-ót (nối âm nhanh) / dót (giọng Nam)`
  3. **Ô chữ `Rr` (`/ɛɐ/`):**
     * *Hiện tại:* IPA ghi `/ɛɐ/` nhưng mô tả ghi `đọc như e-rờ rung cuống họng`.
     * *Phân tích lỗi:* IPA `/ɛɐ̯/` là cách đọc R nguyên âm hóa (*e-ơ*), còn đọc "e-rờ rung cuống họng" có IPA là `/ɛʁ/`.
     * *Đề xuất sửa:* Đổi IPA thành `/ɛʁ/` (hoặc `/ɛʁ/ ~ /ɛɐ̯/`) và mô tả: `đọc như e-rờ (rung cuống họng) hoặc e-ơ`.
  4. **Ô chữ `Ff` (`/ɛf/`), `Mm` (`/ɛm/`), `Nn` (`/ɛn/`), `Ss` (`/ɛs/`):**
     * *Hiện tại:* `ép-phờ`, `em-mờ`, `en-nờ`, `ét-sờ`.
     * *Phân tích lỗi:* Người mới học rất dễ đọc thành 2 âm tiết rời nhau. Đặc biệt ở chữ `Ss` (`/ɛs/`), âm cuối là `/s/` nhẹ (như *x*), không phải *s* nặng tiếng Việt.
     * *Đề xuất sửa:* `đọc như ép-ph (1 âm tiết)`, `đọc như em-m (1 âm tiết)`, `đọc như en-n (1 âm tiết)`, `đọc như ét-x (1 âm tiết, xì hơi nhẹ)`.

---

### 5. Lỗi giải thích khẩu hình 4 ký tự đặc biệt (`Ä`, `Ü`, `ß`)
* **Vị trí:** Mục `1. BẢNG CHỮ CÁI TIẾNG ĐỨC` -> 4 ô cuối bảng và khung màu vàng `Khẩu hình 4 chữ cái đặc biệt (Umlaut & Eszett)`.
* **Chi tiết từng ký tự:**
  1. **Chữ `Ä / ä` (`/ɛː/`):**
     * *Hiện tại:* Ô chữ cái ghi `a-Umlaut (mở miệng đọc ê)`; Khung vàng ghi `Ä / ä /ɛ:/: a-Umlaut — miệng mở rộng đọc âm ê (Qualität, Universität)`.
     * *Phân tích lỗi:* Ký hiệu IPA `/ɛː/` là nguyên âm mở (tương đương chữ **"e"** tiếng Việt trong *mẹ, kem*), còn chữ **"ê"** là nguyên âm đóng `/eː/` (của chữ `E / e`). Về mặt cấu âm, khi mở rộng miệng/hạ cằm thì chỉ có thể phát ra âm **"e"**, nếu đọc âm **"ê"** học viên sẽ phát âm `Ä` trùng với `E`.
     * *Đề xuất sửa:*
       * Ô chữ cái: `a-Umlaut (mở rộng miệng đọc e)`
       * Khung vàng: `• Ä / ä /ɛ:/: a-Umlaut — hạ cằm mở rộng miệng đọc âm e kéo dài (Qualität, Universität, Bär)`
  2. **Chữ `Ü / ü` (`/yː/`):**
     * *Hiện tại:* Khung vàng ghi `• Ü / ü /y:/: u-Umlaut — giữ tròn môi chữ u nhưng phát âm chữ uy (müde, Küche)`.
     * *Phân tích lỗi:* Để tạo ra nguyên âm đơn `/yː/`, kỹ thuật cấu âm chuẩn là: **Giữ cố định khẩu hình tròn môi của chữ u, nhưng vị trí lưỡi phát âm chữ i** (kết quả tạo ra âm nghe gần giống *uy*). Nếu hướng dẫn "tròn môi chữ u nhưng phát âm chữ uy", người học sẽ trượt môi từ *u* sang *i* thành nguyên âm đôi `/wi/` của tiếng Việt. Ngoài ra, từ *müde* là âm dài `/yː/` còn *Küche* là âm ngắn `/ʏ/`.
     * *Đề xuất sửa:*
       * Ô chữ cái: `u-Umlaut (tròn môi u, đọc i -> âm uy)`
       * Khung vàng: `• Ü / ü /y:/: u-Umlaut — giữ cố định môi tròn chữ u nhưng lưỡi phát âm chữ i, tạo thành âm uy (müde, Tür, Küche)`
  3. **Chữ `ß` (`/ɛsˈtsɛt/`):**
     * *Hiện tại:* Ô chữ cái ghi `Eszett (đọc như s kéo dài)`; Khung vàng ghi `• ß /ɛsˈtsɛt/: Eszett — đọc như âm s kéo dài (heißen, dreißig)`.
     * *Phân tích lỗi:* Trong tiếng Đức chuẩn, phụ âm không đọc kéo dài. Chữ `ß` đại diện cho âm **s vô thanh (`/s/`)** — đọc như chữ **"x"** nhẹ tiếng Việt, và luôn đứng sau **nguyên âm dài hoặc nguyên âm đôi**. Ghi "đọc như âm s kéo dài" khiến học viên xì hơi chữ s thật dài thay vì kéo dài nguyên âm đứng trước nó.
     * *Đề xuất sửa:*
       * Ô chữ cái: `Eszett (đọc như x nhẹ /s/ vô thanh)`
       * Khung vàng: `• ß /ɛsˈtsɛt/: Eszett — đọc như âm x nhẹ (/s/ vô thanh), luôn đứng sau nguyên âm dài hoặc nguyên âm đôi (heißen, groß, dreißig)`

---

### 6. Lỗi thiếu hụt ngữ âm ở tổ hợp `or` (Mục 2A)
* **Vị trí:** Mục `2. QUY TẮC ĐÁNH VẦN NGUYÊN ÂM GHÉP & PHỤ ÂM` -> Cột `A` -> Dòng cuối (`or`).
* **Nội dung hiện tại:**
  ```text
  or (o): Tor, sorgen
  ```
* **Phân tích lỗi chuyên môn:**
  * Không đồng nhất với quy tắc `-r` ở các dòng trên (`ir, ur, ür`).
  * Trong từ `Tor` (`/toːɐ̯/`), nguyên âm `o` là âm dài đóng kết hợp `r` nguyên âm hóa (đọc là **ô-ơ**). Trong từ `sorgen` (`/ˈzɔʁɡn̩/` hoặc `/ˈzɔɐ̯ɡn̩/`), nguyên âm `o` là âm ngắn mở (đọc là **o-ơ** hoặc **o-r**). Ghi `or (o)` khiến người học bỏ mất âm `-r` và đọc sai chữ `Tor` thành "to" thay vì "tô-ơ".
* **Đề xuất sửa thành:**
  ```text
  or (o-ơ ngắn [ɔɐ̯]): sorgen, Wort, Norden | or (ô-ơ dài [oːɐ̯]): Tor, Ohr, vor
  ```

---

### 7. Mô tả chưa rõ của phụ âm `ch`, `s` và thiếu đồng bộ IPA ở Mục 2B
* **Vị trí:** Mục `2. QUY TẮC ĐÁNH VẦN NGUYÊN ÂM GHÉP & PHỤ ÂM` -> Cột `B. Phụ âm & Tổ hợp phụ âm đặc trưng`.
* **Nội dung hiện tại & Phân tích lỗi:**
  1. **Dòng 4 (`ch`):**
     * *Hiện tại:* `• ch: sau a, o, u, au đọc như kh (auch, Koch); còn lại đọc nhẹ (mich, dich, ich)`
     * *Phân tích lỗi:* Ghi `"còn lại đọc nhẹ"` khiến người học hiểu lầm là đọc thành âm *"kh nhẹ"* ở cổ họng. Thực chất, `ch` có 2 âm vị hoàn toàn khác nhau:
       * Sau `a, o, u, au`: đọc là **`[x]`** (Ach-Laut — đọc như **kh** tiếng Việt: *auch, Koch, Buch, Nacht*).
       * Các trường hợp còn lại (sau `e, i, ä, ö, ü, ei, eu/äu` và sau phụ âm `l, n, r`): đọc là **`[ç]`** (Ich-Laut — âm **ch nhẹ thoát hơi qua vòm miệng**: nâng mặt lưỡi gần vòm cứng như khi đọc chữ *i*, đẩy hơi xát qua kẽ răng: *ich, mich, dich, Küche, München*).
  2. **Dòng 1 (`s trước nguyên âm`):**
     * *Hiện tại:* `• s (trước nguyên âm) -> đọc như z/d: Sie, sorgen, sieben`
     * *Phân tích lỗi:* Thiếu ký hiệu IPA `[z]`. Ngoài ra ghi `z/d` dễ làm học viên miền Nam phát âm thành `/j/` (như *dờ*).
  3. **Dòng 2 (`v | w`) & Dòng 6 (`sp / st`):**
     * *Hiện tại:* Thiếu ký hiệu IPA trong ngoặc vuông `[f]`, `[v]`, `[ʃp]`, `[ʃt]` (trong khi `z [ts]`, `sch [ʃ]`, `tsch [tʃ]` đều có IPA đầy đủ).
* **Đề xuất sửa toàn bộ các dòng liên quan ở Cột B thành:**
  * Dòng 1:
    ```text
    • s [z] (trước nguyên âm) -> đọc như âm z tiếng Anh (hoặc d giọng Bắc): Sie, sorgen, sieben
    ```
  * Dòng 2:
    ```text
    • v [f] -> đọc như ph: Vater, vier | w [v] -> đọc như v: was, wer
    ```
  * Dòng 4:
    ```text
    • ch: sau a, o, u, au đọc là [x] như kh (auch, Koch, Nacht); còn lại đọc là [ç] như ch nhẹ xì hơi qua vòm miệng (ich, mich, dich, Küche)
    ```
  * Dòng 6:
    ```text
    • sp [ʃp] / st [ʃt] (đầu từ/âm tiết) -> đọc s như sch (s nặng): Sport, Spiel, Stadt, Stuhl
    ```

---

### 8. Lỗi ngữ dụng học ở Mục 3 (Chào hỏi) & Chú thích ngôi `Sie` ở Mục 4
* **Vị trí:** Mục `3. CHÀO HỎI & TẠM BIỆT` và Mục `4. 5 MẪU CÂU GIỚI THIỆU BẢN THÂN`.
* **Chi tiết:**
  1. **Từ `Hallo!` (Mục 3 - Dòng 1):**
     * *Hiện tại:* `• Hallo!: Xin chào (lịch sự) | Hi! / Grüß dich! / Hallöchen!: Chào thân mật`
     * *Phân tích lỗi:* Trong tiếng Đức chuẩn CEFR (Goethe/Telc), `Hallo!` là lời chào **thông dụng / trung tính thiên về thân mật (informell / neutral)**, **KHÔNG PHẢI** là lời chào lịch sự/trang trọng (formell/höflich). Lời chào lịch sự/trang trọng đi với ngôi *Sie* là `Guten Morgen!`, `Guten Tag!`, `Guten Abend!`.
     * *Đề xuất sửa:*
       ```text
       • Hallo!: Xin chào (thông dụng/phổ biến) | Hi! / Grüß dich! / Hallöchen!: Chào thân mật (bạn bè)
       ```
  2. **Từ `Tschüss!` (Mục 3 - Dòng 4):**
     * *Hiện tại:* `• Tschüss! [tʃʏs]: Tạm biệt | Auf Wiedersehen!: Hẹn gặp lại (trang trọng)`
     * *Đề xuất sửa:* Thêm chữ `(thân mật)` sau `Tạm biệt` để đối xứng với `(trang trọng)` của `Auf Wiedersehen!` và khớp với thẻ từ ở cuối trang:
       ```text
       • Tschüss! [tʃʏs]: Tạm biệt (thân mật) | Auf Wiedersehen!: Hẹn gặp lại (trang trọng)
       ```
  3. **Ngôi `Sie` trong Mục 4 (`5 MẪU CÂU GIỚI THIỆU BẢN THÂN`):**
     * *Hiện tại:* Cả 5 câu hỏi đều dùng đại từ `Sie` (`Wer sind Sie?`, `Wie heißen Sie?...`) nhưng chưa có ghi chú giải thích `Sie` là gì và chưa có nghĩa tiếng Việt như ở Mục 3.
     * *Đề xuất bổ sung:* Thêm dòng ghi chú nhỏ hoặc tiêu đề phụ: `(Sử dụng đại từ "Sie" - Ngài/Bạn lịch sự)`.

---

## 💡 PHẦN 3: LỖI LOGIC SỐ ĐẾM & TỐI ƯU HỆ THỐNG THẺ TỪ VỰNG

### 9. Thiếu đánh dấu bất quy tắc cho số `20: zwanzig` & Lưu ý quy tắc số `100–9999` (Mục 5)
* **Vị trí:** Mục `5. HỆ THỐNG SỐ ĐẾM (0 – 9999)`.
* **Phân tích chuyên môn:**
  1. **Tại ô `Số tròn chục, trăm, nghìn`:**
     * *Hiện tại:* Chỉ có `30: dreißig (ß)`, `60: sechzig`, `70: siebzig` được tô màu đỏ (nhóm bất quy tắc), còn **`20: zwanzig`** đang để màu trắng như các số có quy tắc (`40, 50, 80, 90`).
     * *Vấn đề:* Trong tiếng Đức, bộ 4 số tròn chục bất quy tắc kinh điển luôn gồm **`20 (zwanzig - đổi gốc từ zwei)`**, **`30 (dreißig - đuôi ßig)`**, **`60 (sechzig - bỏ s)`**, **`70 (siebzig - bỏ en)`**.
     * *Đề xuất sửa:* Tô màu đỏ cho cả **`20: zwanzig (đổi gốc)`** để học viên không viết nhầm thành *zweizig*.
  2. **Tại khung `🔢 Quy tắc ghép số (Viết liền một từ duy nhất)`:**
     * *Hiện tại:*
       ```text
       • 100–9999: [Nghìn] + [Trăm] + [2 số cuối] (Không có und sau hundert/tausend: 707 = siebenhundertsieben, 912 = neunhundertzwölf).
       ```
     * *Vấn đề:*
       * Chưa có ví dụ nào cho hàng nghìn (`[Nghìn]`).
       * Cần lưu ý thêm (cho cả người học và thuật toán Random số đếm của 50 câu bài tập): Khi số từ `100–9999` kết thúc bằng `01` (như `101`, `1001`), chữ **`eins`** đứng ở cuối từ nên **phải giữ nguyên chữ `-s`** (`101 = einhunderteins`), khác với khi đứng trước `und` (`121 = einhunderteinundzwanzig`).
     * *Đề xuất sửa thành:*
       ```text
       • 100–9999: [Nghìn] + [Trăm] + [2 số cuối] (Không có und sau hundert/tausend: 101 = einhunderteins, 707 = siebenhundertsieben, 912 = neunhundertzwölf, 2026 = zweitausendsechsundzwanzig).
       ```

---

### 10. Lệch số lượng "30 Thẻ từ vựng có mạo từ der/die/das"
* **Vị trí:**
  * Phần giới thiệu đầu trang: `✓ 30 Thẻ từ vựng có mạo từ der/die/das`
  * Khu vực cuối trang: `Từ Vựng & Mẫu Câu Trọng Tâm (Có Phát Âm)`
* **Phân tích lỗi logic:**
  * Trên giao diện hiện tại có tổng cộng 30 thẻ, nhưng thực tế chỉ có **26 thẻ danh từ có mạo từ** (`12 thẻ der` + `9 thẻ die` + `5 thẻ das`) và **4 thẻ `Mẫu câu`** (*Auf Wiedersehen!, Tschüss!, Woher kommen Sie?, Wo wohnen Sie?* — vốn đã xuất hiện ở Mục 3 và Mục 4 ngay phía trên).
  * Hơn nữa, thanh bộ lọc (Filter Tabs) phía trên danh sách thẻ chỉ có 3 nút: `der (Giống đực)`, `die (Giống cái)`, `das (Giống trung)`, không có nút lọc cho `Mẫu câu`.
* **Đề xuất xử lý cho IDE (Chọn 1 trong 2 cách):**
  * **Cách 1 (Khuyên dùng):** Thay thế 4 thẻ `Mẫu câu` bị trùng lặp bằng **4 thẻ danh từ giống trung (`das`)** lấy từ các từ căn bản A1 (để nâng số lượng từ `das` từ 5 lên 9 thẻ, đủ đúng **30 thẻ từ vựng có mạo từ der/die/das**):
    1. `das Wort` — *Từ vựng / Lời nói* — `"Das Wort ist neu. (Từ này mới.)"`
    2. `das Land` — *Đất nước / Quốc gia* — `"Vietnam ist ein schönes Land. (Việt Nam là một đất nước đẹp.)"`
    3. `das Haus` — *Ngôi nhà* — `"Das Haus ist groß. (Ngôi nhà lớn.)"`
    4. `das Buch` — *Quyển sách* — `"Das Buch ist gut. (Quyển sách rất hay.)"`
  * **Cách 2:** Giữ nguyên 30 thẻ hiện tại nhưng sửa dòng mô tả ở phần Mục tiêu bài học thành: `✓ 30 Thẻ từ vựng (der/die/das) & Mẫu câu giao tiếp`, đồng thời thêm tab `Mẫu câu` và `Tất cả` vào thanh lọc.

---

### 11. Tinh chỉnh ngữ nghĩa & tính thực tế của thẻ từ `die Burg` và `die Ruhe`
* **Vị trí:** Khu vực `Từ Vựng & Mẫu Câu Trọng Tâm` (Nhóm thẻ màu đỏ `die`).
* **Chi tiết:**
  1. **Thẻ `die Burg`:**
     * *Hiện tại:* Nghĩa tiếng Việt là `Lâu đài / Thành cổ`. Câu ví dụ: `"Die Burg in Hamburg ist alt. (Lâu đài ở Hamburg cổ kính.)"`
     * *Vấn đề chuyên môn:*
       * Về từ vựng: Trong tiếng Đức, `die Burg` là **Pháo đài / Thành cổ phòng thủ** thời Trung cổ, còn "Lâu đài" nguy nga (như lâu đài Neuschwanstein) là `das Schloss`. Nên dịch rõ để học viên không bị nhầm với từ `das Schloss` ở các bài sau.
       * Về kiến thức thực tế (Landeskunde): Thành phố Hamburg hiện nay không còn tòa *Burg* cổ nào tồn tại (pháo đài *Hammaburg* nguyên thủy đã bị phá hủy từ thế kỷ thứ 9). Câu *"Die Burg in Hamburg ist alt"* nghe không thực tế đối với người bản xứ.
     * *Đề xuất sửa thành:*
       * Nghĩa: `Pháo đài / Thành cổ`
       * Ví dụ: `"Die Burg in Nürnberg ist sehr alt. (Thành cổ ở Nürnberg rất cổ kính.)"` (Hoặc: `"Die alte Burg ist sehr schön. (Pháo đài cổ rất đẹp.)"`)
  2. **Thẻ `die Ruhe`:**
     * *Hiện tại:* `"Bitte Ruhe! (Xin hãy giữ yên lặng!)"`
     * *Góp ý tự nhiên hóa:* Trong giao tiếp thực tế, người Đức thường nói **`"Ruhe, bitte!"`** tự nhiên và phổ biến hơn `"Bitte Ruhe!"`.