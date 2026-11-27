# ĐẶC TẢ KỸ THUẬT: CẬP NHẬT PHẦN BÀI TẬP BÀI 14 (A1)

## HỆ THỐNG: ANTIGRAVITY IDE \- DỰ ÁN DEUTSCHMEISTER

> **CHỈ THỊ TỐI CAO:**  
> 

> 1. Tài liệu này là Nguồn Đặc Tả Duy Nhất (Single Source of Truth) cho **Phần Bài Tập** của Bài 14\.  
> 2. Antigravity IDE CHỈ giới hạn hoạt động trong Phần Bài Tập của Bài 14\.  
> 3. TUYỆT ĐỐI KHÔNG can thiệp, chỉnh sửa hay xóa bớt Phần Lý Thuyết của Bài 14 và mọi dữ liệu của các Bài học cũ (Từ Bài 1 đến Bài 13).

---

## I. QUY ĐỊNH KIỂM SOÁT CHẤT LƯỢNG (QA) CHO 125 CÂU HỎI MỚI

Nhằm khắc phục triệt để các lỗi đã từng xảy ra trên web, hệ thống sinh đề bắt buộc tuân thủ:

1. **Dạng Trắc nghiệm (Dạng 1):** 100% các câu hỏi phải render **ĐỦ 4 LỰA CHỌN (A, B, C, D)**. Hệ thống phải tự động sinh các đáp án gây nhiễu (distractors) hợp lý dựa trên lỗi sai A1 phổ biến. Tuyệt đối không để trống (hiển thị "(để trống)") ở bất kỳ lựa chọn nào.  
2. **Dịch nghĩa:** 100% câu hỏi (bao gồm đề bài, các đáp án và lời giải) phải có bản dịch tiếng Việt chuẩn xác. Không được dịch sai nghĩa hay bỏ sót phần dịch.  
3. **Giải thích:** Phần giải thích bắt buộc phải nhắc lại đáp án đúng và phân tích rõ nguyên lý ngữ pháp (Tại sao dùng giới từ đó? Tại sao lại biến âm?...). Không giải thích chung chung hay sai sự thật.  
4. **Phát âm (Voice):** Các nút âm thanh (Audio) chỉ được truyền chuỗi tiếng Đức hoàn chỉnh, sạch (de-DE). Cấm truyền các ký tự đặc biệt (`___`, `[1]`, `->`, emoji) vào bộ đọc TTS.  
5. **Chống trùng lặp:** Sinh đủ 125 câu mới hoàn toàn. Chạy thuật toán đối chiếu để loại bỏ và thay thế các câu trùng lặp.

---

## II. CẤU TRÚC 18 DẠNG BÀI TẬP BẮT BUỘC

Thanh bộ lọc (chips) trên giao diện phải được khôi phục hiển thị chính xác **18 dạng** sau đây (với số lượng tương ứng trong ngoặc), xếp theo thứ tự tịnh tiến từ 1 đến 18:

1. Trắc nghiệm (15)  
2. Điền khuyết (10)  
3. Chia ĐT bất quy tắc (10)  
4. Dịch từ: Việt \-\> Đức (5)  
5. Dịch từ: Đức \-\> Việt (5)  
6. Nối ô tương ứng (10)  
7. Điền 2 chỗ trống tạo câu (8)  
8. Nghe chép chính tả (8)  
9. Dịch câu: Việt \-\> Đức (8)  
10. Dịch câu: Đức \-\> Việt (7)  
11. Sắp xếp từ thành câu (10)  
12. Phân loại động từ (3)  
13. Phân loại từ để hỏi (3)  
14. Tìm và sửa lỗi sai (10)  
15. Đặt câu hỏi cho từ gạch chân (5)  
16. Đọc hiểu Đúng / Sai (3)  
17. Sắp xếp hội thoại (3)  
18. Đọc menu chọn phản hồi (2)

**Tổng cộng: 125 câu.**

---

## III. KHO DỮ LIỆU BÀI TẬP MẪU (DÀNH CHO ENGINE SINH ĐỀ)

*(Lưu ý cho Dev: Engine dựa vào cấu trúc của 30 câu mẫu dưới đây để tự động scale up và sinh ra đủ 125 câu hỏi. 100% câu phải có đủ dữ kiện, đủ 4 lựa chọn cho trắc nghiệm, và có giải thích / dịch nghĩa tường minh).*

### DẠNG 1: TRẮC NGHIỆM (15 CÂU)

*(Yêu cầu: Bắt buộc render đủ 4 lựa chọn A, B, C, D).*

**Câu 1:**

* **Đề bài:** Chọn giới từ thích hợp: "Berlin liegt \_\_\_ Nordosten von Deutschland."  
* **Lựa chọn:** A. in \| B. im \| C. an \| D. bei  
* **Đáp án đúng:** B  
* **Dịch nghĩa:** Berlin nằm ở miền Đông Bắc của nước Đức.  
* **Giải thích:** "Nordosten" là danh từ viết hoa chỉ hướng, bắt buộc dùng cụm "im \+ \[Danh từ hướng\]". Đáp án: im.

**Câu 2:**

* **Đề bài:** Chọn giới từ thích hợp: "Hamburg liegt \_\_\_ nördlich von Hannover."  
* **Lựa chọn:** A. in \| B. im \| C. (không điền giới từ) \| D. am  
* **Đáp án đúng:** C  
* **Dịch nghĩa:** Hamburg nằm ở phía Bắc của Hannover.  
* **Giải thích:** "nördlich" là tính từ (có đuôi \-lich), tuyệt đối không dùng giới từ "im" hay "in". Đáp án: (không điền giới từ).

**Câu 3:**

* **Đề bài:** Chọn câu ĐÚNG NHẤT mô tả vị trí của Cần Thơ (thuộc Việt Nam):  
* **Lựa chọn:** A. Can Tho liegt im südlich von Vietnam. \| B. Can Tho liegt im Süden von Vietnam. \| C. Can Tho liegt im Süden Vietnam. \| D. Can Tho liegt südlich in Vietnam.  
* **Đáp án đúng:** B  
* **Dịch nghĩa:** Cần Thơ nằm ở miền Nam của Việt Nam.  
* **Giải thích:** Dùng danh từ chỉ hướng "Süden" thì phải có cụm "im ... von". Phương án A sai vì ghép "im" với tính từ, phương án C thiếu giới từ "von". Đáp án: Can Tho liegt im Süden von Vietnam.

**Câu 4:**

* **Đề bài:** Cụm "im Nordwesten" chỉ CÙNG HƯỚNG LA BÀN với tính từ nào sau đây?  
* **Lựa chọn:** A. südwestlich \| B. nordöstlich \| C. nordwestlich \| D. südöstlich  
* **Đáp án đúng:** C  
* **Dịch nghĩa:** Cùng hướng Tây Bắc: im Nordwesten (bên trong) / nordwestlich (bên ngoài).  
* **Giải thích:** Nord (Bắc) \+ Westen (Tây) \= Tây Bắc. Tính từ tương ứng chỉ hướng Tây Bắc là "nordwestlich". Đáp án: nordwestlich.

**Câu 5:**

* **Đề bài:** "Ist das eine Brille? \- Nein, das ist \_\_\_ Brille."  
* **Lựa chọn:** A. kein \| B. keine \| C. eine \| D. nicht  
* **Đáp án đúng:** B  
* **Dịch nghĩa:** Đây là mắt kính à? \- Không, đó không phải mắt kính.  
* **Giải thích:** "die Brille" mang giống cái, phủ định danh từ giống cái dùng "keine". Đáp án: keine.

---

### DẠNG 2: ĐIỀN KHUYẾT (10 CÂU)

**Câu 16:**

* **Đề bài:** Điền từ thích hợp: "Hai Phong liegt im \_\_\_ von Vietnam." (hướng Đông Bắc)  
* **Đáp án:** Nordosten  
* **Dịch nghĩa:** Hải Phòng nằm ở miền Đông Bắc của Việt Nam.  
* **Giải thích:** Sau "im" cần dùng danh từ viết hoa chỉ hướng. Đông Bắc là "Nordosten".

**Câu 17:**

* **Đề bài:** Điền tính từ chỉ hướng: "Polen liegt \_\_\_ von Deutschland." (phía Đông)  
* **Đáp án:** östlich  
* **Dịch nghĩa:** Ba Lan nằm ở phía Đông của nước Đức.  
* **Giải thích:** Phía Đông khi dùng như tính từ (không có giới từ) là "östlich".

**Câu 18:**

* **Đề bài:** Điền giới từ thích hợp: "Italien liegt \_\_\_ Süden von Österreich."  
* **Đáp án:** im  
* **Dịch nghĩa:** Ý nằm ở miền Nam của nước Áo.  
* **Giải thích:** "Süden" là danh từ, cần đi kèm giới từ "im".

---

### DẠNG 3: CHIA ĐỘNG TỪ BẤT QUY TẮC (10 CÂU)

**Câu 26:**

* **Đề bài:** Chia động từ 'sein': "Früher \_\_\_ er sehr sportlich."  
* **Đáp án:** war  
* **Dịch nghĩa:** Trước đây anh ấy rất đam mê thể thao.  
* **Giải thích:** "Früher" (trước đây) là dấu hiệu quá khứ. Ngôi "er" chia Präteritum là "war".

**Câu 27:**

* **Đề bài:** Chia động từ 'sein': "Wo \_\_\_ ihr jetzt?"  
* **Đáp án:** seid  
* **Dịch nghĩa:** Bây giờ các bạn đang ở đâu?  
* **Giải thích:** "jetzt" (bây giờ) là hiện tại. Ngôi "ihr" chia là "seid".

**Câu 28:**

* **Đề bài:** Chia động từ 'tragen': "Anna \_\_\_ gern ein blaues Kleid."  
* **Đáp án:** trägt  
* **Dịch nghĩa:** Anna thích mặc một chiếc đầm màu xanh dương.  
* **Giải thích:** Động từ "tragen" (mặc) biến âm a \-\> ä ở ngôi er/sie/es.

---

### DẠNG 4: DỊCH TỪ VIỆT \-\> ĐỨC (5 CÂU)

**Câu 36:**

* **Đề bài:** Dịch sang tiếng Đức (kèm mạo từ số ít): "áo khoác mùa đông"  
* **Đáp án:** der Wintermantel  
* **Dịch nghĩa:** áo khoác mùa đông.  
* **Giải thích:** der Wintermantel \= áo khoác mùa đông.

**Câu 37:**

* **Đề bài:** Dịch sang tiếng Đức (kèm mạo từ số ít): "sương mù"  
* **Đáp án:** der Nebel  
* **Dịch nghĩa:** sương mù.  
* **Giải thích:** der Nebel \= sương mù.

---

### DẠNG 5: DỊCH TỪ ĐỨC \-\> VIỆT (5 CÂU)

**Câu 41:**

* **Đề bài:** Dịch sang tiếng Việt: "die Krawatte"  
* **Đáp án:** cà vạt  
* **Dịch nghĩa:** die Krawatte \= cà vạt.  
* **Giải thích:** die Krawatte là chiếc cà vạt.

**Câu 42:**

* **Đề bài:** Dịch sang tiếng Việt: "Es ist neblig."  
* **Đáp án:** Trời có sương mù.  
* **Dịch nghĩa:** Es ist neblig \= Trời có sương mù.  
* **Giải thích:** Tính từ "neblig" mang nghĩa là có sương mù.

---

### DẠNG 6: NỐI Ô TƯƠNG ỨNG (10 BÀI)

*(Mỗi bài gồm 4 cặp dữ liệu cần nối)*

**Câu 46 (Bài nối 1: Quốc gia và Ngôn ngữ):**

* Deutschland \<-\> Deutsch  
* Frankreich \<-\> Französisch  
* Polen \<-\> Polnisch  
* Italien \<-\> Italienisch  
* **Dịch nghĩa:** Đức \-\> Tiếng Đức, Pháp \-\> Tiếng Pháp, Ba Lan \-\> Tiếng Ba Lan, Ý \-\> Tiếng Ý.  
* **Giải thích:** Quy tắc tạo ngôn ngữ thường thêm đuôi \-sch hoặc \-isch vào tên quốc gia.

**Câu 47 (Bài nối 2: Từ vựng quần áo):**

* der Stiefel \<-\> bốt  
* der Mantel \<-\> áo măng tô  
* der Pullover \<-\> áo len  
* der Rock \<-\> chân váy  
* **Dịch nghĩa:** der Stiefel \-\> bốt, der Mantel \-\> áo măng tô, der Pullover \-\> áo len, der Rock \-\> chân váy.  
* **Giải thích:** Nhận diện các từ vựng trang phục cơ bản trong tiếng Đức.

---

### DẠNG 7: ĐIỀN 2 CHỖ TRỐNG TẠO CÂU (8 CÂU)

**Câu 56:**

* **Đề bài:** München liegt \[1\] \[2\] von Deutschland. (miền Nam)  
* **Đáp án:** \[1\] im, \[2\] Süden  
* **Dịch nghĩa:** München nằm ở miền Nam của nước Đức.  
* **Giải thích:** Có 2 ô trống nên phải dùng cấu trúc danh từ "im Süden".

**Câu 57:**

* **Đề bài:** Das ist \[1\] Kuli. \[2\] Kuli ist blau. (một / cái \- xác định)  
* **Đáp án:** \[1\] ein, \[2\] Der  
* **Dịch nghĩa:** Đây là một cây bút bi. Cây bút bi màu xanh.  
* **Giải thích:** Lần đầu nhắc đến dùng mạo từ không xác định "ein". Lần sau đã xác định dùng mạo từ "Der".

---

### DẠNG 8: NGHE CHÉP CHÍNH TẢ (8 CÂU)

*(Yêu cầu: Ẩn 100% văn bản gợi ý. Chỉ hiển thị Audio và ô nhập liệu).*

**Câu 64:**

* **Audio:** "Wo waren Sie gestern, Herr Müller?"  
* **Đáp án:** Wo waren Sie gestern, Herr Müller?  
* **Dịch nghĩa:** Hôm qua ngài ở đâu, ngài Müller?  
* **Giải thích:** Luyện nghe câu hỏi về thì quá khứ lịch sự ngôi Sie.

**Câu 65:**

* **Audio:** "Paris liegt westlich von Deutschland."  
* **Đáp án:** Paris liegt westlich von Deutschland.  
* **Dịch nghĩa:** Paris nằm ở phía Tây của nước Đức.  
* **Giải thích:** Luyện nghe cấu trúc phương hướng dùng tính từ (westlich).

---

### DẠNG 9: DỊCH CÂU VIỆT \-\> ĐỨC (8 CÂU)

**Câu 72:**

* **Đề bài:** Nước Áo nằm ở phía Nam của nước Đức. (Dùng tính từ)  
* **Đáp án:** Österreich liegt südlich von Deutschland.  
* **Dịch nghĩa:** Nước Áo nằm ở phía Nam của nước Đức.  
* **Giải thích:** Phía Nam (tính từ) là "südlich", tuyệt đối không dùng "im".

**Câu 73:**

* **Đề bài:** Tây Ban Nha nằm ở miền Tây Nam của Châu Âu. (Dùng danh từ)  
* **Đáp án:** Spanien liegt im Südwesten von Europa.  
* **Dịch nghĩa:** Tây Ban Nha nằm ở miền Tây Nam của Châu Âu.  
* **Giải thích:** Miền Tây Nam (danh từ) là "Südwesten", đi kèm với giới từ "im".

---

### DẠNG 10: DỊCH CÂU ĐỨC \-\> VIỆT (7 CÂU)

**Câu 80:**

* **Đề bài:** Russland liegt im Osten von Europa.  
* **Đáp án:** Nga nằm ở miền Đông của châu Âu.  
* **Dịch nghĩa:** Nga nằm ở miền Đông của châu Âu.  
* **Giải thích:** "im Osten" mô tả vị trí ở miền Đông / phía Đông (danh từ).

**Câu 81:**

* **Đề bài:** Letztes Jahr war sie in Vietnam.  
* **Đáp án:** Năm ngoái cô ấy đã ở Việt Nam.  
* **Dịch nghĩa:** Năm ngoái cô ấy đã ở Việt Nam.  
* **Giải thích:** Letztes Jahr \= Năm ngoái. Động từ "war" thể hiện sự việc đã xảy ra.

---

### DẠNG 11: SẮP XẾP TỪ THÀNH CÂU (10 CÂU)

**Câu 87:**

* **Đề bài:** liegt / Bonn / südwestlich / Rostock / von / .  
* **Đáp án:** Bonn liegt südwestlich von Rostock.  
* **Dịch nghĩa:** Bonn nằm ở phía Tây Nam của Rostock.  
* **Giải thích:** Chủ ngữ \+ liegt \+ tính từ hướng (không có im) \+ von \+ Danh từ.

**Câu 88:**

* **Đề bài:** das / Ist / Auto / von / Thomas / ?  
* **Đáp án:** Ist das das Auto von Thomas?  
* **Dịch nghĩa:** Đó có phải là xe ô tô của Thomas không?  
* **Giải thích:** Câu hỏi Yes/No luôn đảo động từ lên đầu câu. Mạo từ xác định "das" đi chung với "Auto".

---

### DẠNG 12: PHÂN LOẠI ĐỘNG TỪ (3 CÂU)

**Câu 97:**

* **Đề bài:** Phân loại các động từ "sein" sau đây vào 2 nhóm: Hiện tại (Präsens) / Quá khứ (Präteritum)  
* **Từ cho sẵn:** bin, ist, seid, war, waren, warst  
* **Đáp án:** Hiện tại: bin, ist, seid. Quá khứ: war, waren, warst.  
* **Dịch nghĩa:** Hiện tại (tôi là, anh ấy là, các bạn là). Quá khứ (tôi đã là, chúng tôi đã là, bạn đã là).  
* **Giải thích:** Giúp học viên ghi nhớ các dạng chia của động từ sein theo các thì khác nhau.

---

### DẠNG 13: PHÂN LOẠI TỪ ĐỂ HỎI (3 CÂU)

**Câu 100:**

* **Đề bài:** Chọn từ để hỏi thích hợp (Wo / Woher)  
  * \_\_\_ kommst du? \-\> Đáp án: Woher  
  * \_\_\_ liegt München? \-\> Đáp án: Wo  
  * \_\_\_ waren Sie gestern? \-\> Đáp án: Wo  
  * \_\_\_ kommt sie? \-\> Đáp án: Woher  
* **Dịch nghĩa:** Bạn đến từ đâu? / München nằm ở đâu? / Hôm qua ngài ở đâu? / Cô ấy đến từ đâu?  
* **Giải thích:** Động từ kommen (đến từ đâu) dùng Woher. Các vị trí tĩnh dùng Wo.

---

### DẠNG 14: TÌM VÀ SỬA LỖI SAI (10 CÂU)

**Câu 103:**

* **Đề bài:** Bremen liegt im nordwestlich von Deutschland.  
* **Đáp án:** Bremen liegt nordwestlich von Deutschland.  
* **Dịch nghĩa:** Bremen nằm ở phía Tây Bắc của nước Đức.  
* **Giải thích:** Bỏ "im" đi vì "nordwestlich" là tính từ.

**Câu 104:**

* **Đề bài:** Das ist kein Kamera. Das ist ein Handy.  
* **Đáp án:** Das ist keine Kamera. Das ist ein Handy.  
* **Dịch nghĩa:** Đó không phải máy ảnh. Đó là một chiếc điện thoại.  
* **Giải thích:** "die Kamera" mang giống cái, mạo từ phủ định phải là "keine".

---

### DẠNG 15: ĐẶT CÂU HỎI CHO TỪ GẠCH CHÂN (5 CÂU)

**Câu 113:**

* **Đề bài:** Ich komme *aus Russland*. (Hỏi ở ngôi du) \-\> \_\_\_  
* **Đáp án:** Woher kommst du?  
* **Dịch nghĩa:** Bạn đến từ đâu?  
* **Giải thích:** Cụm "aus Russland" chỉ xuất xứ, nên dùng từ để hỏi "Woher".

**Câu 114:**

* **Đề bài:** Wir trinken *Kaffee*. (Hỏi ở ngôi ihr) \-\> \_\_\_  
* **Đáp án:** Was trinkt ihr?  
* **Dịch nghĩa:** Các bạn uống gì?  
* **Giải thích:** "Kaffee" là sự vật, dùng từ để hỏi "Was". Ngôi ihr chia động từ là trinkt.

---

### DẠNG 16: ĐỌC HIỂU ĐÚNG / SAI (3 CÂU)

**Câu 118:**

* **Đề bài:** Đọc đoạn văn: "Hamburg liegt im Norden von Deutschland. München liegt im Süden."  
* **Mệnh đề:** Hamburg liegt südlich von Deutschland.  
* **Đáp án:** Falsch (Sai)  
* **Dịch nghĩa:** Đoạn văn: Hamburg nằm ở miền Bắc nước Đức. München nằm ở miền Nam. Mệnh đề: Hamburg nằm ở phía Nam nước Đức.  
* **Giải thích:** Đoạn văn xác nhận Hamburg nằm ở phía Bắc (im Norden), do đó mệnh đề nói nằm ở phía Nam là sai.

---

### DẠNG 17: SẮP XẾP HỘI THOẠI (3 CÂU)

**Câu 121:**

* **Đề bài:** Kéo thả các câu sau theo thứ tự một đoạn hội thoại hỏi đường hợp lý:  
  1. Entschuldigung, wo liegt München?  
  2. München? Das liegt in Deutschland.  
  3. Ja, aber wo genau in Deutschland?  
  4. München liegt im Süden von Deutschland.  
* **Đáp án:** 1 \-\> 2 \-\> 3 \-\> 4  
* **Dịch nghĩa:** Xin lỗi, München nằm ở đâu? / München à? Nó nằm ở Đức. / Vâng, nhưng chính xác ở đâu tại Đức? / München nằm ở miền Nam nước Đức.  
* **Giải thích:** Trình tự logic: Hỏi vị trí chung \-\> Trả lời chung cấp quốc gia \-\> Hỏi kỹ hơn \-\> Trả lời chi tiết bằng phương hướng.

---

### DẠNG 18: ĐỌC MENU / BẢN ĐỒ CHỌN PHẢN HỒI (2 CÂU)

**Câu 124:**

* **Đề bài:** Nhìn vào bản đồ, bạn thấy Berlin ở góc trên bên phải của Đức. Chọn câu miêu tả đúng: A. Berlin liegt im Nordosten von Deutschland. B. Berlin liegt im Südwesten von Deutschland. C. Berlin liegt im Nordwesten von Deutschland. D. Berlin liegt im Südosten von Deutschland.  
* **Đáp án đúng:** A  
* **Dịch nghĩa:** Berlin nằm ở miền Đông Bắc của Đức.  
* **Giải thích:** Vị trí góc trên bên phải tương ứng với hướng Đông Bắc (Nordosten).

```

```

