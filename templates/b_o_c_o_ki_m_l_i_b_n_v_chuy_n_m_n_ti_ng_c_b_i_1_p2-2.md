# 🛠 BÁO CÁO KIỂM LỖI CHUYÊN MÔN TIẾNG ĐỨC & HƯỚNG DẪN CẬP NHẬT NỘI DUNG

**Phạm vi kiểm duyệt:** Trình độ A1 — Bài 1 (P2): *"Kaffee oder Tee - Cà Phê Hoặc Trà"*

**Mục đích:** Tài liệu đặc tả kỹ thuật nội dung (Content QA Spec) dành cho **Antigravity IDE** để tìm kiếm (search) các chuỗi văn bản hiện tại và thay thế (replace) bằng nội dung chuẩn xác về mặt ngôn ngữ học, ngữ dụng học và sư phạm tiếng Đức.

## 🚨 PHẦN 1: CÁC LỖI NGHIÊM TRỌNG VỀ NGỮ PHÁP, NGỮ ÂM & TỪ VỰNG (CẦN SỬA NGAY)

### 1.1. Thiếu quy tắc "Bỏ `h`, gấp đôi phụ âm `m`" ở động từ `nehmen`

* **Vị trí:** Mục `4. Động Từ Bất Quy Tắc Cốt Lõi (sein, haben) & Động Từ Biến Âm (lesen, nehmen)` -> Bảng `2. Biến âm e -> ie / i (lesen, nehmen)`.

* **Nội dung hiện tại:**

  * Tiêu đề bảng: `2. Biến âm e -> ie / i (lesen, nehmen)`

  * Dòng `du`: `liest` | `nimmst`

  * Dòng `er/sie/es`: `er/sie/esliest` *(bị dính chữ)* | `nimmt`

* **Vấn đề chuyên môn:**

  1. Ở bảng 1 (`haben`), web có chú thích rất rõ `hast (bỏ b)` và `hat (bỏ b)`. Tuy nhiên ở bảng 2, động từ `nehmen` không chỉ biến âm `e -> i` mà còn **bỏ âm câm `h` (Dehnungs-h) và gấp đôi phụ âm `m`** (`nehm-` $\rightarrow$ `nimm-`). Nếu học viên chỉ áp dụng quy tắc "Biến âm `e -> i`" trên tiêu đề, họ sẽ chia sai thành `*nihmst` và `*nihmt`.

  2. Ở động từ `lesen` (gốc `les-` kết thúc bằng `-s`), ngôi `du` (`liest`) và `er/sie/es` (`liest`) viết giống hệt nhau vì kết hợp cả quy tắc biến âm (`e -> ie`) lẫn quy tắc gốc kết thúc bằng `-s` ở Mục 3 (ngôi `du` chỉ thêm `-t`, không thêm `-st`).

  3. Lỗi hiển thị dính chữ: `er/sie/esliest` không có khoảng trắng giữa chủ ngữ và động từ.

* **Đề xuất sửa đổi cho IDE:**

  * Tạo khoảng cách giữa cột `er/sie/es` và `liest`.

  * Cập nhật dòng `du` và `er/sie/es` của cột `nehmen` và bổ sung chú thích dưới bảng:

    ```
    du        | liest (chỉ +t) | nimmst (bỏ h, gấp đôi m)
    er/sie/es | liest          | nimmt (bỏ h, gấp đôi m)
    
    ```

### 1.2. Sai lệch ký hiệu ngữ âm Quốc tế (IPA) ở nhóm động từ kết thúc bằng `-s, -ß, -z, -x`

* **Vị trí:** Mục `3. Hai Trường Hợp Đặc Biệt Về Phát Âm Khi Chia Động Từ (-s, -ß, -z & -t, -d)` -> Khung 1 (Màu tím).

* **Nội dung hiện tại:**

  > `1. Gốc kết thúc -s, -ß, -z, -x` (`heißen, tanzen`)
  >
  > `Vì gốc đã có âm gió /s/, ở ngôi du ta chỉ thêm -t (không thêm -st). Ngôi du, er/sie/es, ihr viết giống nhau:`

* **Vấn đề chuyên môn:**

  * Về mặt ngữ âm học tiếng Đức, 4 chữ cái `-s, -ß, -z, -x` **không phải** đều phát âm là `/s/`:

    * `-ß` / `-ss` mới là âm `/s/` (như *heißen* `/ˈhaɪ̯sn̩/`).

    * `-s` đứng cuối gốc trước nguyên âm thường là âm hữu thanh `/z/` (như *reisen* `/ˈʁaɪ̯zn̩/`), khi ghép với `-t` mới vô thanh hóa thành `/s/`.

    * `-z` là âm tắc xát `/ts/` (như *tanzen* `/ˈtantsn̩/`).

    * `-x` là tổ hợp âm `/ks/` (như *mixen* `/ˈmɪksn̩/`).

  * Việc gộp cả `-z` (*tanzen*) và `-x` vào ký hiệu IPA `/s/` là sai kiến thức ngữ âm.

  * Ngoài ra, huy hiệu ví dụ ghi `heißen, tanzen`, nhưng bên dưới chỉ chia mỗi động từ `heißen` (trong khi khung 2 bên cạnh chia song song cả `mieten | arbeiten`).

* **Đề xuất sửa đổi cho IDE:**

  * Thay đoạn giải thích bằng:

    ```
    Vì gốc động từ đã kết thúc bằng nhóm âm xuýt (/s/, /z/, /ts/, /ks/), ở ngôi du ta chỉ thêm -t (không thêm -st). Do đó, ngôi du, er/sie/es và ihr có cách viết giống hệt nhau:
    
    ```

  * Cập nhật khung chia động từ để hiển thị cả `heißen` và `tanzen` đồng bộ với khung 2:

    ```
    ich heiße | tanze
    du heißt | tanzt (chỉ thêm -t!)
    er/sie/es heißt | tanzt
    wir heißen | tanzen
    ihr heißt | tanzt
    sie/Sie heißen | tanzen
    
    ```

### 1.3. Nhầm lẫn thuật ngữ "Động từ có quy tắc (Regelmäßige Verben)" với `kommen`, `trinken`, `heißen`

* **Vị trí:** Mục `2. Cấu Tạo Động Từ & Công Thức Chia Động Từ Có Quy Tắc (Regelmäßige Verben)`.

* **Nội dung hiện tại:**

  * Tiêu đề: `Cấu Tạo Động Từ & Công Thức Chia Động Từ Có Quy Tắc (Regelmäßige Verben)`

  * Bảng chia 4 động từ: `machen (làm)`, `wohnen (sống)`, `kommen (đến)`, `trinken (uống)`.

* **Vấn đề chuyên môn:**

  * Trong ngữ pháp tiếng Đức, chỉ có `machen` và `wohnen` là **Regelmäßige / Schwache Verben** (Động từ có quy tắc / Động từ yếu).

  * Hai động từ `kommen` (*kam – ist gekommen*) và `trinken` (*trank – hat getrunken*) thực chất là **Unregelmäßige / Starke Verben** (Động từ bất quy tắc / Động từ mạnh), chỉ là **ở thì Hiện tại (Präsens) chúng được chia đuôi theo quy tắc chuẩn và không bị biến âm**. Nếu gắn nhãn chúng là *Regelmäßige Verben*, khi lên cuối A1 / đầu A2 học thì Quá khứ (Perfekt), học viên sẽ chia sai thành `*gekommt` và `*getrinkt`.

* **Đề xuất sửa đổi cho IDE:**

  * Sửa tiêu đề Mục 2 thành:

    ```
    Cấu Tạo Động Từ & Quy Tắc Chia Đuôi Chuẩn Ở Thì Hiện Tại (Präsens)
    
    ```

  * Sửa dòng phụ đề Mục 2 thành:

    ```
    Công thức chia đuôi tiêu chuẩn ở thì Hiện tại (Präsens) và Quy tắc Vị trí số 2 (Position 2)
    
    ```

### 1.4. Định nghĩa sai bản chất từ vựng của động từ `kommen` và `kosten`

* **Vị trí:** Phần `Từ Vựng & Mẫu Câu Trọng Tâm (Có Phát Âm)` ở cuối trang.

* **Vấn đề chuyên môn & Đề xuất sửa đổi:**

  1. **Thẻ từ `kommen`:**

     * **Hiện tại:** Nghĩa tiếng Việt ghi là `Đến từ, xuất thân`.

     * **Lỗi:** Bản thân động từ `kommen` chỉ có nghĩa là **"Đến, tới"** (như trong câu hội thoại ở Mục 4: *"Kommst du auch?"* = *Bạn cũng đến chứ?*). Nó chỉ mang nghĩa **"Đến từ, xuất thân từ"** khi đi kèm giới từ **`aus`** (`kommen aus + Quốc gia/Thành phố`).

     * **Sửa thành:** `Đến, tới (kommen aus: đến từ)`

  2. **Thẻ từ `kosten`:**

     * **Hiện tại:** Nghĩa tiếng Việt ghi là `Có giá là, tốn bao nhiêu`.

     * **Lỗi:** Động từ `kosten` không hề có nghĩa nghi vấn `"bao nhiêu"`. Chữ *"bao nhiêu"* nằm ở cụm từ để hỏi `wie viel` trong câu ví dụ (*"Wie viel kostet der Kaffee?"*). Nếu dịch `kosten` là *"tốn bao nhiêu"*, học viên sẽ hiểu nhầm bản thân động từ này đã mang nghĩa câu hỏi.

     * **Sửa thành:** `Có giá là, trị giá, tốn`

### 1.5. "Bẫy văn hóa & ngôn ngữ" nghiêm trọng ở thẻ từ `das Eis`: `"Kaffee mit Eis"` KHÔNG PHẢI là `"Cà phê đá"` Việt Nam!

* **Vị trí:** Phần `Từ Vựng & Mẫu Câu Trọng Tâm` -> Thẻ `das Eis`.

* **Nội dung hiện tại:**

  * Nghĩa: `Đá lạnh / Kem`

  * Câu ví dụ: `"Kaffee mit Eis, bitte. (Làm ơn cho cà phê đá.)"`

* **Vấn đề chuyên môn (Cực kỳ quan trọng trong giao tiếp thực tế tại Đức):**

  * Trong tiếng Đức, khi nói đến đồ uống `Kaffee`, từ `Eis` mặc định được hiểu là **Kem ăn (Speiseeis / Vanilleeis)** — tức món **Eiskaffee** (cà phê uống kèm 1 viên kem vani bên trên).

  * Nếu người Việt vào quán cà phê ở Đức và gọi `"Kaffee mit Eis, bitte"`, bồi bàn sẽ mang ra cà phê kem hoặc hỏi lại xem khách muốn kem vani hay đá viên! Để gọi **cà phê đá (đá viên)**, người Đức dùng **`Kaffee mit Eiswürfeln`** (hoặc *Iced Coffee* / *Kaffee auf Eis*). Ngược lại, với nước ngọt (`Cola`, `Wasser`), nói `"Cola mit Eis"` thì mới mặc định là đá viên.

* **Đề xuất sửa đổi cho IDE:**

  * Đổi câu ví dụ ở thẻ `das Eis` sang câu chuẩn xác, không gây hiểu lầm khi gọi món ở Đức:

    ```
    "Cola mit Eis, bitte. (Làm ơn cho một ly Cola có đá.)"
    
    ```

  * *(Tùy chọn)* Hoặc giữ câu cà phê nhưng sửa thành:

    ```
    "Ich trinke Cola mit Eis. (Tôi uống Cola có đá.)"
    
    ```

## 💬 PHẦN 2: LỖI LOGIC HỘI THOẠI & NGỮ DỤNG HỌC VĂN HÓA ĐỨC (PRAGMATICS)

### 2.1. Lỗi mâu thuẫn logic trong "Đoạn tin nhắn thực tế tại Café Kafka"

* **Vị trí:** Cuối Mục `4. Động Từ Bất Quy Tắc Cốt Lõi (sein, haben)...` -> Khung `☕ Đoạn tin nhắn thực tế tại Café Kafka (Luyện phản xạ 'sein'):`.

* **Nội dung hiện tại:**

  * **Tin nhắn 1:** `"Hi, Anna und ich sind im Café Kafka. Wo bist du? Maria ist auch da. Kommst du auch?"`

    *(Chào, Anna và tôi đang ở quán Café Kafka. Bạn ở đâu? Maria cũng ở đây. Bạn đến luôn nhé?)*

  * **Tin nhắn 2:** `"Wo seid ihr? Ich bin im Deutschkurs. Die Lehrerin ist nett, sie ist aus den USA."`

    *(Các bạn ở đâu? Tôi đang ở trong khóa học tiếng Đức. Cô giáo rất tốt bụng, cô ấy đến từ Mỹ.)*

* **Vấn đề chuyên môn & Logic:**

  1. **Mâu thuẫn logic hội thoại:** Ở ngay câu đầu tiên của Tin nhắn 1, người gửi đã nói rõ: *"Anna và tôi đang ở quán Café Kafka. Bạn ở đâu?"*. Thế nhưng ở Tin nhắn 2 (tin nhắn phản hồi), người kia lại hỏi ngược lại: ***"Wo seid ihr?" (Các bạn ở đâu?)***! Điều này hoàn toàn phi lý trong một đoạn chat liên tiếp.

  2. **Dịch sai từ `auch` và thiếu tự nhiên:**

     * `"Kommst du auch?"`: Chữ `auch` nghĩa là **"cũng"** (vì Anna, tôi và Maria đều đã ở đó rồi). Dịch là *"Bạn đến luôn nhé?"* làm mất nghĩa của từ vựng trọng tâm `auch`. Nên dịch là: *"Bạn cũng đến chứ?"*.

     * `"Ich bin im Deutschkurs"`: Trong tiếng Việt tự nhiên, ta nói *"Tôi đang ở lớp học tiếng Đức"* thay vì dịch word-by-word *"Tôi đang ở trong khóa học tiếng Đức"*.

* **Đề xuất sửa đổi cho IDE:**

  * **Cách 1 (Khuyên dùng - Giữ nguyên việc luyện tập chữ `seid` ở câu hỏi mà vẫn hợp logic 100%):** Thay `"Wo seid ihr?"` ở Tin nhắn 2 bằng `"Seid ihr noch lange da?"` (Các bạn còn ở đó lâu không?) hoặc đảo câu hỏi `"Wo seid ihr?"` thành lời nhắn mở đầu. Nếu muốn giữ câu đơn giản trình độ A1.1:

    * **Tin nhắn 2 (Sửa):**

      ```
      "Ach, ihr seid im Café Kafka! Ich bin im Deutschkurs. Die Lehrerin ist nett, sie ist aus den USA."
      Các bạn đang ở quán Café Kafka à! Tôi đang ở lớp học tiếng Đức. Cô giáo rất thân thiện, cô ấy đến từ Mỹ.
      
      ```

  * **Cách 2 (Nếu bắt buộc giữ câu hỏi `"Wo seid ihr?"`):** Tách nhãn rõ ràng thành 2 ngữ cảnh độc lập (`Ngữ cảnh 1` và `Ngữ cảnh 2`) thay vì trình bày như 2 tin nhắn trả lời nhau tại Café Kafka.

  * **Sửa bản dịch Tin nhắn 1:**

    ```
    Chào, Anna và tôi đang ở quán Café Kafka. Bạn đang ở đâu? Maria cũng ở đây. Bạn cũng đến chứ?
    
    ```

### 2.2. Lỗi văn hóa giao tiếp lịch sự (Ngôi `Sie`) trong Hội thoại 2 & Thẻ từ `heißen`

* **Vị trí:**

  1. Mục 3 -> `Hội thoại 2: Giao tiếp lịch sự (ngôi Sie)` (`Frau Bui & Herr Nguyen`).

  2. Phần Từ vựng cuối trang -> Thẻ từ `heißen`.

* **Nội dung hiện tại:**

  ```
  Frau Bui: Guten Tag, wie heißen Sie?
  Herr Nguyen: Ich heiße Dat.
  Frau Bui: Woher kommen Sie?
  Herr Nguyen: Ich komme aus Vietnam.
  
  ```

* **Vấn đề chuyên môn (Ngữ dụng học tiếng Đức):**

  1. **Lệch chuẩn văn hóa xưng hô `Sie` (Siezen):** Trong văn hóa Đức, khi giao tiếp lịch sự bằng ngôi `Sie` giữa `Frau Bui` và `Herr Nguyen`, việc trả lời câu hỏi *"Wie heißen Sie?"* chỉ bằng **tên riêng (Vorname)** là `"Ich heiße Dat."` là không phù hợp (chỉ dùng tên riêng khi xưng `du`). Khi xưng `Sie`, người Đức luôn giới thiệu **Họ và Tên đầy đủ (`Ich heiße Dat Nguyen.`)** hoặc **Họ (`Mein Name ist Nguyen.`)**.

  2. **Thiếu bản dịch tiếng Việt:** Ở `Hội thoại 1` (bên trái), 3 câu của Marc có dịch tiếng Việt nhưng 2 câu của Anna bị quên dịch; còn ở `Hội thoại 2` (bên phải), cả 4 câu đều bị thiếu bản dịch tiếng Việt!

* **Đề xuất sửa đổi cho IDE:**

  * Cập nhật `Hội thoại 2` (sửa thành `Dat Nguyen` và bổ sung đầy đủ dịch tiếng Việt):

    ```
    Frau Bui: Guten Tag, wie heißen Sie? (Xin chào, tên Ngài là gì ạ?)
    Herr Nguyen: Ich heiße Dat Nguyen. (Tôi tên là Đạt Nguyễn.)
    Frau Bui: Woher kommen Sie? (Ngài đến từ đâu ạ?)
    Herr Nguyen: Ich komme aus Vietnam. (Tôi đến từ Việt Nam.)
    
    ```

  * Đồng bộ câu ví dụ ở thẻ từ `heißen` cuối trang:

    ```
    "Wie heißen Sie? Ich heiße Dat Nguyen. (Ngài tên là gì? - Tôi tên là Đạt Nguyễn.)"
    
    ```

### 2.3. Lỗi thiếu dịch tiếng Việt, thiếu giới thiệu nhân vật `Peter` và nghĩa của `"mein Freund"` trong Hội thoại 1

* **Vị trí:** Mục 3 -> `Hội thoại 1: Quê quán, nơi ở & làm việc` (`Marc, Anna, Peter`).

* **Nội dung hiện tại:**

  ```
  Marc: Woher kommst du? (Bạn đến từ đâu?)
  Anna: Ich komme aus Brasilien. Das ist mein Freund, er kommt aus Russland.
  Marc: Und wo wohnt ihr? (Và các bạn sống ở đâu?)
  Anna: Wir wohnen in Berlin. Wo arbeitest du?
  Marc: Ich arbeite bei der Post. (Tôi làm việc tại bưu điện.)
  
  ```

* **Vấn đề chuyên môn:**

  1. Trên tiêu đề liệt kê 3 nhân vật `Marc, Anna, Peter` (để minh họa cho ngôi `ihr = Anna und Peter` ở Mục 1), nhưng trong bài hội thoại tên của `Peter` hoàn toàn không xuất hiện!

  2. Hai lượt lời của `Anna` bị bỏ sót bản dịch tiếng Việt (trong khi các câu của `Marc` đều có dịch).

  3. Trong tiếng Đức, `"mein Freund"` (có đại từ sở hữu *mein*) mặc định mang nghĩa là **"bạn trai của tôi"** (còn *"một người bạn"* phải nói là *"ein Freund von mir"*). Nếu giới thiệu kèm tên và dịch rõ sẽ giúp học viên hiểu ngay ngữ cảnh.

* **Đề xuất sửa đổi cho IDE:**

  ```
  Marc: Woher kommst du? (Bạn đến từ đâu?)
  Anna: Ich komme aus Brasilien. Das ist mein Freund Peter, er kommt aus Russland. (Mình đến từ Brazil. Đây là bạn trai mình, Peter, anh ấy đến từ Nga.)
  Marc: Und wo wohnt ihr? (Và hai bạn sống ở đâu?)
  Anna: Wir wohnen in Berlin. Wo arbeitest du? (Chúng mình sống ở Berlin. Còn bạn làm việc ở đâu?)
  Marc: Ich arbeite bei der Post. (Mình làm việc tại bưu điện.)
  
  ```

### 2.4. Giá tiền `3,99 Euro` cho 2 đồ uống tại Quán Cà Phê thiếu thực tế văn hóa DACH

* **Vị trí:** Mục 6 -> `☕ Hội thoại gọi món & Thanh toán tại Quán Cà Phê` & Thẻ từ `der Euro`.

* **Nội dung hiện tại:**

  * Anna gọi 1 cà phê nhiều sữa, Sophie gọi 1 trà, hai người chọn thanh toán chung (`Zusammen, bitte`).

  * **Kellner:** `Das macht 3,99 Euro. (Tổng cộng hết 3,99 Euro ạ.)`

* **Vấn đề chuyên môn (Văn hóa thực tế tại Đức, Áo, Thụy Sĩ):**

  1. Ở Đức/Áo/Thụy Sĩ, mức giá đuôi `,99` (như `3,99 €`) là **giá tâm lý trong siêu thị** (Aldi, Lidl, Rewe), **không bao giờ** xuất hiện trong menu quán cà phê / nhà hàng (Gastronomie). Giá trong quán cà phê luôn làm tròn đến `,00`, `,20`, `,50` hoặc `,80` (ví dụ: `3,50 €`, `6,80 €`).

  2. Tổng hóa đơn cho **2 món đồ uống** (1 cà phê + 1 trà) tại quán cà phê ở Đức không thể có giá `3,99 €` (mức này chỉ mới đủ cho 1 tách trà hoặc 1 tách cà phê bình dân). Tổng 2 ly thực tế rơi vào khoảng `6,50 €` – `7,80 €`.

  3. Câu gọi món của Anna (`"Ich trinke Kaffee mit viel Milch."`) và Sophie (`"Ich nehme Tee."`) trả lời bồi bàn thiếu từ lịch sự **`bitte`** (trong văn hóa Đức, khi gọi món luôn kèm *bitte*).

* **Đề xuất sửa đổi cho IDE:**

  * Trong `Hội thoại gọi món & Thanh toán tại Quán Cà Phê`:

    * Sửa câu của Sophie thành: `Ich nehme Tee, bitte. (Cho tôi dùng trà ạ.)`

    * Sửa câu chốt tiền của Kellner từ `3,99 Euro` thành **`6,50 Euro`** hoặc **`6,80 Euro`**:

      ```
      Kellner: Das macht 6,80 Euro. (Tổng cộng hết 6,80 Euro ạ.)
      
      ```

## 🔍 PHẦN 3: CÁC ĐIỂM CẦN ĐỒNG BỘ & TINH CHỈNH SƯ PHẠM CHI TIẾT

### 3.1. Đồng bộ hóa hệ thống Đại từ nhân xưng ở Mục 1

* **Vị trí:** Mục `1. Hệ Thống Đại Từ Nhân Xưng (Personalpronomen) ở Cách 1 (Nominativ)` (9 ô đại từ & khung Mẹo).

* **Các điểm thiếu nhất quán hiện tại:**

  1. Ô `du` ghi `(ngôi 2 thân mật)` — thiếu chữ **`số ít`** (trong khi `ich` ghi `ngôi 1 số ít`, `ihr` ghi `ngôi 2 số nhiều thân mật`).

  2. Ô `sie (số ít)` ghi: `Động từ chia đuôi: -t (hoặc ist)`, nhưng hai ô cùng ngôi 3 số ít là `er` và `es` lại chỉ ghi `Đuôi: -t` mà không có `(hoặc ist)`. Tương tự, ô `sie (số nhiều)` ghi `Động từ chia đuôi: -en (hoặc sind)`, nhưng ô `wir` và `Sie` cũng đi với `sind` lại không ghi `(hoặc sind)`.

  3. Trong khung `⚠️ Mẹo Phân Biệt Tuyệt Đối 3 Chữ "sie / Sie" Trong Đề Thi:`:

     * **Hiện tại:** `Sie (Ngài - lịch sự): Luôn viết hoa chữ S dù đứng đầu hay giữa câu, động từ chia đuôi -en (ví dụ: Was trinken Sie?).`

     * **Lỗi logic:** Ngay trong câu ví dụ `Was trinken Sie?`, chữ `Sie` đang đứng ở **cuối câu**, nhưng lời giải thích chỉ nói *"dù đứng đầu hay giữa câu"*.

* **Đề xuất sửa đổi cho IDE:**

  * Ô `du`: Sửa thành `bạn, cậu, em (ngôi 2 số ít thân mật)`.

  * Ô `Sie (Viết hoa S)`: Sửa dòng giải thích thành `Ngài / các Ngài / Ông / Bà (ngôi 2 lịch sự)`.

  * Đồng bộ chú thích đuôi chia ở cả 9 ô (hoặc bỏ `(hoặc ist)` / `(hoặc sind)` ở 2 ô lẻ để tránh học viên tưởng chỉ mỗi `sie` mới đi với `ist/sind`, vì bảng chia `sein` đã được dạy riêng cực kỳ chi tiết ở Mục 4).

  * Khung Mẹo `Sie (Ngài - lịch sự)`: Sửa thành:

    ```
    • Sie (Ngài - lịch sự): Luôn viết hoa chữ S ở mọi vị trí (đầu, giữa hay cuối câu), động từ chia đuôi -en (ví dụ: Was trinken Sie?).
    
    ```

### 3.2. Làm rõ khái niệm "Vị trí số 2 (Position 2)" ở Mục 2

* **Vị trí:** Mục 2 -> Khung `📌 Quy tắc Vị trí số 2 (Position 2):`.

* **Nội dung hiện tại:**

  > `Trong câu trần thuật và câu hỏi có từ để hỏi (W-Frage), động từ đã chia theo chủ ngữ luôn luôn đứng ở vị trí thứ 2:`
  >
  > `Ich [1] komme [2] aus Vietnam.` | `Wo [1] wohnen [2] Sie?`

* **Vấn đề sư phạm:**

  * Học viên A1 rất hay hiểu nhầm "Vị trí thứ 2" là "Từ thứ 2 trong câu" (đếm từng chữ). Khi gặp chủ ngữ dài như *"Anna und ich"* (3 từ), học viên sẽ bối rối vì sao động từ đứng ở từ thứ 4 (`[Anna und ich] [1] [sind] [2] im Café Kafka`).

* **Đề xuất sửa đổi cho IDE:**

  * Bổ sung chú thích ngắn:

    ```
    Trong câu trần thuật và câu hỏi có từ để hỏi (W-Frage), động từ đã chia theo chủ ngữ luôn luôn đứng ở vị trí thành phần thứ 2 trong câu (tính theo cụm thành phần câu, không đếm theo từng từ đơn lẻ):
    
    ```

### 3.3. Làm rõ bản chất ngữ pháp của `möchten` và cách gọi món lược giản ở Mục 5

* **Vị trí:** Mục `5. Động Từ Khuyết Thiếu möchten (Muốn Lịch Sự) & Khung Câu (Satzklammer)`.

* **Vấn đề chuyên môn:**

  1. Về mặt ngữ pháp học tiếng Đức, không có động từ nguyên mẫu độc lập nào tên là `möchten` trong từ điển chuẩn — `möchten` thực chất là dạng **Konjunktiv II (Giả định thức II)** của động từ khuyết thiếu **`mögen`**, được dùng độc lập ở trình độ A1 với nghĩa *"muốn một cách lịch sự (would like)"*. Việc giải thích ngắn gọn nguồn gốc này giúp giải đáp thắc mắc vì sao ngôi `ich möchte` và `er/sie/es möchte` lại kết thúc bằng `-e` (giống quy tắc Konjunktiv II) mà vẫn giữ sự đơn giản cho A1.

  2. Trong khung `Cấu trúc khung câu (Satzklammer)`, bài học nêu `möchten` đi kèm động từ nguyên mẫu ở cuối câu (`Was möchten Sie trinken?`). Tuy nhiên, ở thẻ từ `die Milch` bên dưới lại xuất hiện câu `"Möchten Sie Kaffee mit Milch?"` (không có động từ nguyên mẫu ở cuối). Cần ghi chú thêm rằng khi gọi đồ ăn/thức uống, động từ `trinken/nehmen` ở cuối câu có thể được lược bỏ nếu ngữ cảnh đã rõ ràng.

* **Đề xuất sửa đổi cho IDE:**

  * Bổ sung chú thích nhỏ dưới bảng chia `'möchten'`:

    ```
    💡 Bản chất: 'möchten' là dạng giả định lịch sự (Konjunktiv II) của động từ 'mögen', được sử dụng với cấu trúc giống hệt động từ khuyết thiếu. Khi ngữ cảnh gọi món đã rõ, có thể lược bỏ động từ thường ở cuối câu (VD: Möchten Sie Kaffee mit Milch?).
    
    ```

### 3.4. Chỉnh sửa thuật ngữ tiếng Việt "Gia vị" và lỗi dấu câu ở Mục 6 & Tiêu đề bài học

* **Vị trí:**

  1. Phần `Mục tiêu bài học` (Đầu trang): `...tự tin gọi đồ uống, tùy chọn gia vị (mit/ohne, viel/wenig)...`

  2. Tiêu đề Mục 6: `Từ Vựng Đồ Uống, Gia Vị, Cách Gọi Món & Thanh Toán Euro (€)`

  3. Mục 6 -> Khung `Quy tắc đọc giá tiền Euro (1 € = 100 Cent):`: `Dấu phẩy , đọc là Euro, phần lẻ đọc số bình thường:`

* **Vấn đề chuyên môn:**

  1. Trong tiếng Việt, **sữa (`die Milch`)** và **đá (`das Eis`)** cho vào cà phê/trà không được gọi là **"gia vị"** (gia vị thường dùng cho muối, tiêu, ớt, mắm trong nấu ăn). Dùng từ **"Thành phần đi kèm"** hoặc **"Đường / Sữa / Đá"** sẽ chuẩn xác và tự nhiên hơn rất nhiều.

  2. Trong câu `Dấu phẩy , đọc là Euro...`, dấu phẩy đặt lơ lửng giữa hai khoảng trắng dễ bị nhìn nhầm là lỗi đánh máy (typo).

* **Đề xuất sửa đổi cho IDE:**

  * Phần `Mục tiêu bài học`: Đổi `tùy chọn gia vị (mit/ohne, viel/wenig)` $\rightarrow$ `tùy chọn thành phần đi kèm như đường, sữa, đá (mit/ohne, viel/wenig)`.

  * Tiêu đề Mục 6: Đổi thành `Từ Vựng Đồ Uống, Thành Phần Đi Kèm, Cách Gọi Món & Thanh Toán Euro (€)`.

  * Khung `Quy tắc đọc giá tiền Euro`: Đổi `Dấu phẩy , đọc là Euro, phần lẻ đọc số bình thường:` $\rightarrow$ `Dấu phẩy (,) đọc là "Euro", phần số lẻ phía sau đọc như số đếm bình thường:`.

### 3.5. Rà soát chi tiết các thẻ từ vựng ở phần `Từ Vựng & Mẫu Câu Trọng Tâm`

Dưới đây là bảng tinh chỉnh cho các thẻ từ vựng ở cuối trang để đạt độ chuẩn xác 100%:

| Thẻ từ hiện tại | Nội dung hiện tại có vấn đề | Nguyên nhân chuyên môn | Đề xuất sửa đổi cho IDE | 
| ----- | ----- | ----- | ----- | 
| **`der Tee`** | Dịch: *(Làm ơn cho tôi dùng trà không đường.)* | Cụm *"Làm ơn cho tôi dùng..."* bị lai căng cấu trúc dịch máy, người Việt không nói *"cho tôi dùng trà"*. | Sửa dịch thành: `(Cho tôi dùng trà không đường ạ.)` hoặc `(Làm ơn cho tôi một phần trà không đường.)` | 
| **`die Cola`** | Nghĩa: `Nước ngọt Coca-Cola`  Dịch: *(Anh ấy uống một lon Coca-Cola.)* | 1\. Trong tiếng Đức, `die Cola` chỉ chung mọi loại nước ngọt vị Cola (Pepsi, Fritz-Kola, Coca-Cola...), đồng thời ở Mục 6 đang ghi là `nước ngọt Cola` (chưa đồng bộ).  2\. `"eine Cola"` là 1 ly/chai/phần Cola nói chung (còn 1 lon là *eine Dose Cola*). | Nghĩa: `Nước ngọt Cola`  Dịch: `(Anh ấy uống một ly/chai nước ngọt Cola.)` | 
| **`der Saft`** | Ví dụ: `"Der Orangensaft ist lecker. (Nước cam ngon.)"` | Từ vựng trên thẻ là `der Saft`, nhưng câu ví dụ lại dùng danh từ ghép `der Orangensaft` khiến người học mới bấm nghe dễ nhầm phát âm của `Saft` với `Orangensaft`. | Đổi ví dụ thành: `"Der Saft ist sehr lecker. (Nước ép hoa quả rất ngon.)"` (hoặc ghi chú `der Orangensaft = nước cam`). | 
| **`der Kellner`** | Nghĩa: `Người bồi bàn / nhân viên phục vụ` | Trong tiếng Đức, danh từ chỉ nghề nghiệp phân biệt giới tính rất rõ: `der Kellner` là **nam** nhân viên phục vụ (còn nữ là `die Kellnerin` — tương tự như `die Lehrerin` đã xuất hiện ở Mục 4). | Sửa nghĩa thành: `Nam bồi bàn / Nam nhân viên phục vụ (nữ: die Kellnerin)` | 
| **`der Cent`** | Nghĩa: `Đồng xu Cent (1 € = 100 Cent)` | Trong câu ví dụ `"Ein Euro hat hundert Cent"`, `Cent` là **đơn vị tiền tệ (xu)** chứ không phải 100 đồng xu vật lý (*Centmünzen*). | Sửa nghĩa thành: `Đơn vị xu Cent (1 € = 100 Cent)` | 
| **`sein`** | Dịch: *(Tôi đang ở trong khóa học tiếng Đức.)* | Dịch thô từ giới từ `im`. | Sửa dịch thành: `(Tôi đang ở lớp học tiếng Đức.)` | 
| **`wenig`** | Dịch: *(Chỉ một chút đường thôi, làm ơn.)* | Từ `wenig` mang nghĩa định lượng **"ít"** (đối lập với `viel` = nhiều), còn *"một chút"* trong tiếng Đức là `ein bisschen`. | Sửa dịch thành: `(Chỉ một ít đường thôi ạ.)` | 
| **Nhãn `Từ` (Badge màu cam)** | Toàn bộ động từ (`trinken`, `wohnen`...), giới từ (`mit`, `ohne`), lượng từ/trạng từ (`viel`, `wenig`, `zusammen`) đều gắn chung nhãn `Từ`. | Các danh từ được phân loại rất rõ bằng nhãn `der`, `die`, `das`, nhưng các từ loại khác lại chỉ ghi chung chung là `Từ`, làm giảm giá trị tra cứu ngữ pháp. | Đổi nhãn `Từ` thành loại từ cụ thể: **`Động từ`** (cho *trinken, nehmen, möchten, zahlen, kosten, mieten, arbeiten, wohnen, kommen, heißen, sein, haben, lesen*), **`Giới từ`** (cho *mit, ohne*), và **`Từ vựng / Trạng từ`** (cho *viel, wenig, zusammen, getrennt*). | 
