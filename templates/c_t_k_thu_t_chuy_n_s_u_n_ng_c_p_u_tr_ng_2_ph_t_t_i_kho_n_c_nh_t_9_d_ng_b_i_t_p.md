# ĐẶC TẢ KỸ THUẬT CHUYÊN SÂU: HỆ THỐNG TÀI KHOẢN ĐUA TOP, ĐẤU TRƯỜNG PHẢN XẠ 2 PHÚT (9 DẠNG BÀI - GIỚI HẠN 2 LƯỢT/NGÀY) & CHUẨN HÓA BÀI TẬP TỪ BÀI 5 A1 (`DEUTSCHMEISTER`)

> **CHỈ THỊ BẮT BUỘC DÀNH CHO ANTIGRAVITY IDE / AI AGENT:**
> 1. **Tuyệt đối không xóa dữ liệu cũ (Zero Data Loss)**: Giữ nguyên 100% nội dung lý thuyết, từ vựng, bảng tra cứu (`verbs_db.js`, `lexikon_db.js`) và kho 50 bài tập của các bài đã có (**Bài 1 P1, Bài 1 P2, Bài 2, Bài 3, Bài 4**).
> 2. **Thực thi đầy đủ Backend + Database + Frontend**: Không làm giả lập (mock) trên giao diện tĩnh. Toàn bộ tài khoản người chơi, mật khẩu mã hóa, tiến độ bài đã học, giới hạn **2 lượt chơi Đấu trường/ngày/tài khoản**, bộ lọc câu hỏi theo tiến độ và Bảng Xếp Hạng phải hoạt động thực tế với cơ sở dữ liệu SQLite `deutsch_meister.db`.
> 3. **Triển khai chính xác 9 dạng bài tập & hệ số cộng/trừ điểm**: Mọi dạng bài trong Đấu trường và trong các bài học từ **Bài 5 (A1)** trở đi phải tuân thủ tuyệt đối ma trận điểm số và giao diện tương tác được quy định trong tài liệu này.

---

## PHẦN 1: HỆ THỐNG ĐĂNG KÝ / ĐĂNG NHẬP TÀI KHOẢN CẠNH TRANH (`UNIQUE AUTH SYSTEM`)

Do mục **"🏆 Đấu trường & BXH"** mang tính chất thi đua xếp hạng giữa các người học, hệ thống bắt buộc phải định danh người chơi qua tài khoản riêng biệt.

### 1.1. Quy tắc Kiểm tra Tài khoản & Mật khẩu Nghiêm ngặt
1. **Tên tài khoản (`username`)**:
   * **Độ dài**: Tối thiểu **4 ký tự**, tối đa **24 ký tự** (`4 <= len(username.strip()) <= 24`).
   * **Định dạng ký tự**: Chỉ chấp nhận chữ cái không dấu (`a-z`, `A-Z`), chữ số (`0-9`) và dấu gạch dưới (`_`). Không chấp nhận khoảng trắng hoặc ký tự đặc biệt (`Regex: ^[a-zA-Z0-9_]{4,24}$`).
   * **Tính độc nhất tuyệt đối (`UNIQUE CASE-INSENSITIVE`)**:
     * Không cho phép 2 người chơi có cùng tên tài khoản dưới bất kỳ hình thức viết hoa hay viết thường nào.
     * **Ví dụ thực tế**: Nếu trong hệ thống đã có người đăng ký tài khoản tên là **`hieu3001`**, thì không ai khác được phép tạo tài khoản tên `hieu3001`, `Hieu3001` hay `HIEU3001`.
     * Khi trùng tên, API phải trả về mã lỗi `409 Conflict` kèm thông báo tiếng Việt rõ ràng:
       > ❌ *"Tên tài khoản 'hieu3001' đã tồn tại trên hệ thống! Vui lòng chọn một tên khác để thi đua."*
2. **Mật khẩu (`password`)**:
   * **Độ dài**: Tối thiểu **8 ký tự** (`len(password) >= 8`).
   * **Bảo mật**: Bắt buộc băm mật khẩu bằng `werkzeug.security.generate_password_hash(password)` trước khi lưu vào bảng `users` và kiểm tra đăng nhập bằng `check_password_hash(user.password_hash, password)`.

---

### 1.2. Thiết kế Bảng Cơ sở Dữ liệu SQLite (`database.py`)
Cập nhật tệp `database.py` để khởi tạo các bảng quản lý tài khoản, tiến độ học thực tế và lịch sử ván đấu Đấu trường:

```sql
-- 1. BẢNG TÀI KHOẢN NGƯỜI CHƠI (Đảm bảo UNIQUE COLLATE NOCASE cho username)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE COLLATE NOCASE, -- Chặn tuyệt đối trùng tên (VD: hieu3001 == Hieu3001)
    password_hash TEXT NOT NULL,
    highest_level_code TEXT DEFAULT 'A1',         -- Cấp độ cao nhất đang học: 'A1', 'A2', 'B1', 'B2'
    highest_lesson_order INTEGER DEFAULT 1,       -- Thứ tự bài học cao nhất đã học tới trong cấp độ đó
    total_exp INTEGER DEFAULT 0,                  -- Tổng điểm EXP tích lũy toàn hệ thống
    arena_best_score INTEGER DEFAULT 0,           -- Kỷ lục điểm cao nhất đạt được trong 1 ván Đấu trường 2 phút
    arena_total_games INTEGER DEFAULT 0,          -- Tổng số ván Đấu trường đã tham gia
    streak_days INTEGER DEFAULT 1,
    last_active_date TEXT,                        -- Định dạng YYYY-MM-DD (Múi giờ Việt Nam UTC+7)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index tăng tốc kiểm tra trùng tên tài khoản
CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username_lower ON users(LOWER(username));

-- 2. BẢNG TIẾN ĐỘ BÀI HỌC CỦA TỪNG TÀI KHOẢN (Dùng để giới hạn phạm vi câu hỏi Đấu trường)
CREATE TABLE IF NOT EXISTS user_studied_lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    lesson_id INTEGER NOT NULL,                   -- ID bài học trong bảng lessons
    level_code TEXT NOT NULL,                     -- 'A1', 'A2', 'B1', 'B2'
    lesson_order INTEGER NOT NULL,                -- Thứ tự bài học (VD: Bài 1 P1 = 1, Bài 1 P2 = 2, Bài 2 = 3, Bài 3 = 4, Bài 4 = 5...)
    studied_theory INTEGER DEFAULT 1,             -- Đã mở xem lý thuyết
    practice_completed INTEGER DEFAULT 0,         -- Số lần hoàn thành bài tập của bài này
    best_practice_score INTEGER DEFAULT 0,
    last_studied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, lesson_id),
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 3. BẢNG PHIÊN CHƠI ĐẤU TRƯỜNG (Kiểm soát giới hạn tối đa 2 lần/ngày/tài khoản)
CREATE TABLE IF NOT EXISTS arena_daily_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_token TEXT NOT NULL UNIQUE,           -- Token định danh ván đấu chống gian lận
    user_id INTEGER NOT NULL,
    play_date TEXT NOT NULL,                      -- Ngày chơi theo chuẩn 'YYYY-MM-DD' (UTC+7)
    attempt_number INTEGER NOT NULL,              -- Lượt thứ mấy trong ngày (1 hoặc 2)
    status TEXT DEFAULT 'in_progress',            -- 'in_progress' | 'completed' | 'expired'
    final_score INTEGER DEFAULT 0,                -- Điểm tổng kết sau 2 phút
    correct_count INTEGER DEFAULT 0,              -- Tổng số câu trả lời đúng
    wrong_count INTEGER DEFAULT 0,                -- Tổng số câu trả lời sai
    scope_summary TEXT,                           -- Lưu phạm vi bài học lúc thi (VD: 'A1: Bài 1 P1 -> Bài 4')
    breakdown_json TEXT,                          -- Thống kê điểm theo từng dạng trong 9 dạng câu hỏi
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_arena_user_date ON arena_daily_attempts(user_id, play_date);
```

---

## PHẦN 2: LUẬT CHƠI & CƠ CHẾ "ĐẤU TRƯỜNG PHẢN XẠ 2 PHÚT" (`SPEED ARENA ENGINE`)

### 2.1. Quy tắc Vận hành Ván đấu
1. **Thời lượng ván đấu cố định**: **2 phút (120 giây)** đếm ngược liên tục từ `02:00` về `00:00`.
2. **Nhịp độ phản xạ**:
   * Trong suốt 120 giây, hệ thống liên tục nạp từng câu hỏi ngẫu nhiên lên màn hình.
   * Ngay khi người chơi chọn đáp án / bấm `Enter` / hoàn tất nối ô, hệ thống chấm điểm tức thì:
     * Nếu **ĐÚNG**: Phát âm thanh phản hồi tích cực, hiển thị hiệu ứng cộng điểm màu xanh lá (ví dụ: `+5`, `+7`, `+10`, `+15`), cộng điểm vào tổng điểm ván đấu và chuyển sang câu hỏi tiếp theo sau `450ms`.
     * Nếu **SAI**: Phát âm thanh cảnh báo, hiển thị hiệu ứng trừ điểm màu đỏ (ví dụ: `-2`, `-3`, `-4`, `-6`), hiển thị nhanh đáp án đúng trong `900ms` để người chơi rút kinh nghiệm rồi chuyển sang câu tiếp theo.
3. **Giới hạn Nghiêm ngặt `2 Lượt / Ngày / Tài khoản`**:
   * Hệ thống lấy ngày hiện tại theo múi giờ Việt Nam (`UTC+7`, định dạng `YYYY-MM-DD`).
   * Trước khi bắt đầu ván mới, Backend truy vấn:
     ```sql
     SELECT COUNT(*) AS used_attempts
     FROM arena_daily_attempts
     WHERE user_id = ? AND play_date = ?;
     ```
   * Nếu `used_attempts >= 2`:
     * Chặn hoàn toàn việc tạo ván đấu mới.
     * Hiển thị trên giao diện: **`🎟️ Lượt thi đấu hôm nay: 0/2 (Đã hết lượt — Reset vào 00:00 ngày mai)`** và vô hiệu hóa nút *"Bắt đầu ván mới"*.
   * Ngay khi người chơi bấm **"Bắt đầu ván mới"** (và `used_attempts < 2`), hệ thống lập tức ghi nhận `attempt_number = used_attempts + 1` vào bảng `arena_daily_attempts` (để tránh việc người chơi cố tình F5 tải lại trang khi đang thua nhằm gian lận lượt chơi).

---

### 2.2. Ma trận 9 Dạng Câu Hỏi & Hệ Số Điểm Thưởng / Phạt Tuyệt Đối

Cả Backend và Frontend phải áp dụng chính xác bảng điểm dưới đây cho từng câu hỏi trong Đấu trường:

| STT | Mã Dạng (`question_type`) | Tên Dạng Câu Hỏi Hiển Thị | Mô Tả Cơ Chế Làm Bài | Điểm Khi Làm Đúng | Điểm Khi Làm Sai |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **1** | **`trac_nghiem`** | **Trắc nghiệm (Multiple Choice)** | Chọn 1 trong 4 đáp án `A, B, C, D` về chia động từ, mạo từ `der/die/das/den/einen/keinen`, mạo từ sở hữu, từ vựng hoặc giao tiếp. | **`+5 điểm`** | **`-2 điểm`** |
| **2** | **`dien_khuyet`** | **Điền khuyết (Fill in the Blank)** | Điền từ vựng, đuôi động từ hoặc mạo từ/giới từ còn thiếu vào 1 ô trống `___` trong câu tiếng Đức. | **`+7 điểm`** | **`-3 điểm`** |
| **3** | **`dich_nghia_vd`** | **Dịch nghĩa từ/cụm từ: Việt $\rightarrow$ Đức** | Đề cho 1 từ hoặc cụm từ tiếng Việt (VD: *"cái tủ lạnh"*, *"ở phía Đông Bắc"*), người chơi gõ từ/cụm từ tiếng Đức tương ứng. | **`+6 điểm`** | **`-3 điểm`** |
| **4** | **`dich_nghia_dv`** | **Dịch nghĩa từ/cụm từ: Đức $\rightarrow$ Việt** | Đề cho 1 từ hoặc cụm từ tiếng Đức (VD: *"das Bücherregal"*, *"zusammen oder getrennt"*), người chơi gõ nghĩa tiếng Việt. | **`+6 điểm`** | **`-3 điểm`** |
| **5** | **`noi_o`** | **Nối ô từ trái qua phải (Matching Pairs)** | Hiển thị 4 ô bên Cột Trái và 4 ô bên Cột Phải (đã xáo trộn). Người chơi nối đủ 4 cặp tương ứng. **Đúng cả 4 cặp mới được cộng điểm; sai dù chỉ 1 cặp cũng bị trừ điểm.** | **`+10 điểm`**<br>*(đúng tuyệt đối)* | **`-4 điểm`**<br>*(sai $\ge 1$ cặp)* |
| **6** | **`dich_cau_vd`** | **Dịch câu hoàn chỉnh: Việt $\rightarrow$ Đức** | Đề cho 1 câu tiếng Việt hoàn chỉnh, người chơi dịch sang câu tiếng Đức đúng ngữ pháp và từ vựng. | **`+15 điểm`** | **`-6 điểm`** |
| **7** | **`dich_cau_dv`** | **Dịch câu hoàn chỉnh: Đức $\rightarrow$ Việt** | Đề cho 1 câu tiếng Đức hoàn chỉnh, người chơi dịch sang câu tiếng Việt tự nhiên, đúng nghĩa. | **`+15 điểm`** | **`-6 điểm`** |
| **8** | **`nghe_dien`** | **Nghe và điền vào (Listen & Fill)** | Hệ thống đọc câu/cụm từ bằng giọng chuẩn `de-DE` (có nút nghe `1.0x` và nghe chậm `0.65x`), người chơi nghe và điền từ/cụm từ còn khuyết. | **`+10 điểm`** | **`-4 điểm`** |
| **9** | **`dien_tao_cau`** | **Điền vào chỗ trống để tạo thành câu** | Đề cho khung câu có 2–3 chỗ trống cấu trúc (kèm gợi ý ngữ cảnh hoặc từ gốc trong ngoặc) để người chơi điền vào tạo thành câu hoàn chỉnh chuẩn trật tự `V2` / `Khung câu`. | **`+5 điểm`** | **`-2 điểm`** |

---

## PHẦN 3: THUẬT TOÁN LỌC CÂU HỎI THEO ĐÚNG TIẾN ĐỘ ĐÃ HỌC (`PROGRESSION-SCOPED QUESTION POOL`)

### 3.1. Quy tắc "Học Đến Đâu – Thi Đến Đó" (Không Vượt Cấp)
Hệ thống định nghĩa thứ tự cấp độ CEFR:
$$\text{LEVEL\_RANK} = \{ \text{"A1"}: 1, \text{"A2"}: 2, \text{"B1"}: 3, \text{"B2"}: 4 \}$$

1. **Cách ghi nhận bài học đã học của người dùng**:
   * Mỗi khi người dùng (đã đăng nhập) bấm vào xem lý thuyết hoặc làm bài tập của một bài học `(level_code, lesson_order, lesson_id)`, Frontend tự động gọi API `POST /api/progress/mark-studied` để lưu bài đó vào bảng `user_studied_lessons`, đồng thời cập nhật `highest_level_code` và `highest_lesson_order` của người dùng nếu bài đó cao hơn tiến độ cũ.
   * **Trường hợp người dùng mới đăng ký tài khoản** và vào thẳng Đấu trường khi chưa bấm vào bài học nào: Hệ thống mặc định phạm vi của họ là các bài học đang mở khóa ở cấp độ `A1` mà họ đã tương tác (hoặc mặc định **Cấp độ A1: từ Bài 1 P1 đến Bài hiện có trong A1**, tuyệt đối không lấy A2, B1, B2).
2. **Công thức lọc câu hỏi hợp lệ cho tài khoản `U`**:
   Một câu hỏi $Q$ có thuộc tính `(q_level, q_lesson_order)` chỉ được phép xuất hiện trong Đấu trường của người chơi $U$ nếu thỏa mãn một trong hai điều kiện:
   * **Điều kiện 1**: Bài học `(q_level, q_lesson_order)` nằm trực tiếp trong danh sách `user_studied_lessons` của người chơi $U$.
   * **Điều kiện 2 (Luật kế thừa cấp độ)**:
     $$\text{LEVEL\_RANK}[q\_level] < \text{LEVEL\_RANK}[U.\text{highest\_level\_code}]$$
     hoặc:
     $$\left(\text{LEVEL\_RANK}[q\_level] == \text{LEVEL\_RANK}[U.\text{highest\_level\_code}] \text{ VÀ } q\_lesson\_order \le U.\text{highest\_lesson\_order}\right)$$
   * **Ví dụ kiểm chứng**:
     * Nếu người chơi đang học đến **A1 - Bài 2**: Đấu trường chỉ lấy câu hỏi thuộc **Bài 1 (P1), Bài 1 (P2) và Bài 2 của A1**. Tuyệt đối không xuất hiện câu hỏi của Bài 3 (Präteritum `war/waren`, phương hướng), Bài 4 (`Akkusativ den/einen`, mạo từ sở hữu) hay A2, B1, B2.
     * Nếu người chơi đã học đến **A2 - Bài 3**: Đấu trường được phép lấy ngẫu nhiên toàn bộ câu hỏi của **A1 + A2 (từ Bài 1 đến Bài 3)**, nhưng **tuyệt đối không** lấy câu hỏi của A2 Bài 4 trở đi và không lấy B1, B2.

---

### 3.2. Bộ Sinh Câu Hỏi Động Tự Chế (`Procedural & Curated Arena Generator`)
Để người chơi không bị nhàm chán vì lặp lại câu hỏi cố định, hệ thống Đấu trường kết hợp **2 nguồn câu hỏi** theo tỷ lệ `50% - 50%`:
1. **Nguồn 1 (Từ Database Bài tập `exercises`)**: Lấy ngẫu nhiên các câu hỏi trong bảng `exercises` thuộc các `lesson_id` mà người dùng đã học, chuyển đổi sang định dạng 9 dạng câu hỏi của Đấu trường.
2. **Nguồn 2 (Bộ Tự Chế Động `ArenaProceduralGenerator`)**: Tự động sinh hàng trăm biến thể câu hỏi mới (nhưng 100% dùng từ vựng và ngữ pháp của đúng các bài người dùng đã học):

#### Bảng Phân vùng Kiến thức Dùng Để "Chế Thêm Câu Hỏi" Theo Từng Bài Học Hiện Có:

| Mã Bài Học (`level_code`, `lesson_order`) | Tên Bài Học | Kho Kiến Thức Được Phép Dùng Để Chế Câu Hỏi Trong Đấu Trường |
| :--- | :--- | :--- |
| **`('A1', 1)`** | **Bài 1 (P1): Hallo! - Chào hỏi, Số đếm & Giờ giấc** | • Chào hỏi & Tạm biệt (*Hallo, Guten Morgen/Tag/Abend, Gute Nacht, Tschüss, Auf Wiedersehen*)<br>• Bảng chữ cái & Đánh vần (*ä, ö, ü, ß, ch, sch, sp, st, ei, ie, eu/äu*)<br>• Số đếm từ `0` đến `10.000` (*null, eins, zwei... zwanzig, einundzwanzig, hundert, tausend*)<br>• Hỏi và trả lời giờ chính thống & đời thường (*Wie spät ist es? / Wie viel Uhr ist es? -> Es ist ... Uhr / Viertel nach / Viertel vor / halb / kurz vor / kurz nach*) |
| **`('A1', 2)`** | **Bài 1 (P2): Kaffee oder Tee? - Chia động từ & Gọi đồ** | • 9 Đại từ nhân xưng (*ich, du, er, sie, es, wir, ihr, sie, Sie*)<br>• Chia động từ quy tắc (`machen, wohnen, kommen`), gốc `-s/-ß/-z` (`heißen`), gốc `-t/-d` (`mieten, arbeiten`), biến âm (`lesen -> liest, nehmen -> nimmst/nimmt`), bất quy tắc (`sein, haben`) và khuyết thiếu (`möchten`)<br>• Từ vựng quán cà phê (*Kaffee, Tee, Milch, Cola, Wein, Kakao, Zucker, Eis, mit, ohne, viel, wenig*)<br>• Thanh toán & Giá tiền Euro (*zahlen, zusammen oder getrennt, Das macht ... Euro ...*) |
| **`('A1', 3)`** | **Bài 2: Sprache im Kurs - Động từ & Giống (`der/die/das`)** | • Quy tắc nhận diện giống `der / die / das` theo đuôi hậu tố (`-ant, -ent, -ich, -ismus, -ist, -ast, -ling` / `-heit, -keit, -schaft, -ung, -ie, -anz, -enz, -in` / `-ment, -um, -tum, -chen, -ma, -em, -nis`) và ngoại lệ (`der Moment`, `die Erlaubnis`)<br>• 18 danh từ đồ dùng lớp học số ít & số nhiều (*der Tisch, der Stuhl, der Füller, der Kuli, der Bleistift, der Radiergummi, der Becher, die Tafel, die Brille, die Tasche, die Landkarte, das Papier, das Heft, das Buch, das Wörterbuch, das Handy, das Whiteboard, das Brötchen*)<br>• Mạo từ `ein/eine` và phủ định `kein/keine` ở Nominativ<br>• 6 mẫu câu giao tiếp lớp học (*verstehen, wiederholen, buchstabieren, anschreiben*) |
| **`('A1', 4)`** | **Bài 3: Địa danh - Phương hướng - Präteritum** | • 18 Quốc gia & Ngôn ngữ (*Deutschland -> Deutsch, Österreich, Italien, Spanien, Griechenland, Frankreich, England, Niederlande, Polen, Tschechien, Russland, China, Vietnam*) + Quốc gia có mạo từ (*die Schweiz, die Türkei, die Slowakei, der Iran, die USA*)<br>• 7 Danh lam thắng cảnh châu Âu (*die Akropolis, der Big Ben, der Eiffelturm, der Schiefe Turm, der Prater, das Brandenburger Tor, der Rote Platz*)<br>• 8 Phương hướng danh từ & tính từ (*der Norden/nördlich, der Süden/südlich, der Osten/östlich, der Westen/westlich, Nordosten, Südosten, Nordwesten, Südwesten, in der Mitte von*)<br>• 9 từ để hỏi W-Frage & Động từ `sein` ở quá khứ **Präteritum** (`war, warst, war, waren, wart, waren`) |
| **`('A1', 5)`** | **Bài 4: Nhà ở - Cách 1 Nominativ / Cách 4 Akkusativ & Mạo từ sở hữu** | • Từ vựng nhà cửa, các phòng ghép với `-zimmer` (*der Garten, der Balkon, der Flur, der Keller, die Wohnung, die Garage, die Terrasse, die Küche, die Toilette, das Haus, das Wohnheim, das Fenster, das Wohn-/Bade-/Schlaf-/Ess-/Arbeits-/Kinderzimmer*)<br>• Nội thất & Tính từ đối lập (*der Schrank, der Kühlschrank, der Teppich, der Spiegel, der Fernseher, die Lampe, die Spüle, das Bett, das Bücherregal* | *hell/dunkel, groß/klein, laut/leise, lang/kurz, alt/neu, teuer/billig, schön/hässlich, modern, gemütlich*)<br>• Biến đổi **Nominativ vs. Akkusativ** (`der/ein/kein` $\rightarrow$ `den/einen/keinen` sau `haben, finden, es gibt...`)<br>• **Mạo từ sở hữu** theo 9 ngôi (`mein, dein, sein, ihr, unser, euer -> eure, Ihr`) |

---

## PHẦN 4: ĐẶC TẢ CHI TIẾT CẤU TRÚC DỮ LIỆU & GIAO DIỆN CỦA 9 DẠNG CÂU HỎI

Dưới đây là cấu trúc JSON chuẩn và logic chấm điểm cho từng dạng trong **9 dạng câu hỏi** để Antigravity IDE lập trình đồng nhất cho cả **Đấu trường** lẫn **Bài tập từ Bài 5 (A1) trở đi**:

### Dạng 1: Trắc nghiệm (`trac_nghiem`) — Đúng `+5` | Sai `-2`
```json
{
  "type": "trac_nghiem",
  "level": "A1",
  "lesson_order": 5,
  "points_correct": 5,
  "points_wrong": -2,
  "question": "Chọn mạo từ đúng điền vào chỗ trống: „Mein Arbeitszimmer ist klein, aber hell. Es hat ___ Tisch und ___ Stuhl.“",
  "options": [
    "ein / ein",
    "einen / einen",
    "der / der",
    "den / den"
  ],
  "correct_answer": "einen / einen",
  "explanation": "Động từ 'hat' (haben) đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ). Vì 'der Tisch' và 'der Stuhl' đều là danh từ giống đực nên mạo từ 'ein' biến đổi thành 'einen'."
}
```

### Dạng 2: Điền khuyết (`dien_khuyet`) — Đúng `+7` | Sai `-3`
```json
{
  "type": "dien_khuyet",
  "level": "A1",
  "lesson_order": 5,
  "points_correct": 7,
  "points_wrong": -3,
  "question": "Điền mạo từ sở hữu đúng của ngôi 'ihr (các bạn)' vào chỗ trống: „Maria und Lukas, sind das ___ Kinder?“",
  "accepted_answers": ["eure"],
  "explanation": "'Kinder' là danh từ số nhiều ở Cách 1 (Nominativ). Gốc sở hữu của 'ihr (các bạn)' là 'euer', khi thêm đuôi '-e' của số nhiều phải lược bỏ chữ 'e' ở giữa: euer + e -> eure."
}
```

### Dạng 3: Dịch nghĩa từ/cụm từ Việt $\rightarrow$ Đức (`dich_nghia_vd`) — Đúng `+6` | Sai `-3`
```json
{
  "type": "dich_nghia_vd",
  "level": "A1",
  "lesson_order": 5,
  "points_correct": 6,
  "points_wrong": -3,
  "prompt_vi": "cái tủ lạnh",
  "question": "Dịch từ/cụm từ sau sang tiếng Đức (có thể kèm hoặc không kèm mạo từ):",
  "accepted_answers": [
    "der Kühlschrank",
    "Kühlschrank",
    "ein Kühlschrank",
    "der Kuehlschrank",
    "Kuehlschrank"
  ],
  "explanation": "'Tủ lạnh' trong tiếng Đức là 'der Kühlschrank' (danh từ ghép từ 'kühl' + 'der Schrank')."
}
```

### Dạng 4: Dịch nghĩa từ/cụm từ Đức $\rightarrow$ Việt (`dich_nghia_dv`) — Đúng `+6` | Sai `-3`
```json
{
  "type": "dich_nghia_dv",
  "level": "A1",
  "lesson_order": 2,
  "points_correct": 6,
  "points_wrong": -3,
  "prompt_de": "zusammen oder getrennt?",
  "question": "Dịch cụm từ giao tiếp sau sang tiếng Việt:",
  "accepted_answers": [
    "chung hay riêng",
    "thanh toán chung hay riêng",
    "trả chung hay riêng",
    "tính tiền chung hay riêng",
    "gộp chung hay tách riêng",
    "chung hoặc riêng",
    "trả tiền chung hay trả riêng"
  ],
  "explanation": "'zusammen' = chung/cùng nhau, 'oder' = hay/hoặc, 'getrennt' = riêng."
}
```

### Dạng 5: Nối ô từ trái qua phải (`noi_o`) — Đúng cả 4 cặp `+10` | Sai dù chỉ 1 cặp `-4`
* **Cơ chế giao diện**:
  * Cột bên trái hiển thị 4 ô cố định `L1, L2, L3, L4`.
  * Cột bên phải hiển thị 4 ô `R1, R2, R3, R4` đã được xáo trộn ngẫu nhiên (`shuffle`).
  * Người chơi click vào 1 ô cột trái, sau đó click vào 1 ô cột phải để tạo liên kết (hiển thị badge số thứ tự cặp `Cặp #1, #2, #3, #4` và viền màu tương ứng). Người chơi có thể click lại vào ô đã nối để đổi cặp trước khi bấm nút **`Xác nhận nối ô`** (hoặc tự động chấm ngay khi nối xong cặp thứ 4).
  * **Quy tắc chấm điểm**: Kiểm tra toàn bộ 4 cặp. Nếu đúng đủ `4/4 cặp` $\rightarrow$ **`+10 điểm`**. Nếu chỉ cần **1 cặp bị nối sai** (`< 4/4 cặp`) $\rightarrow$ trừ ngay **`-4 điểm`**.
```json
{
  "type": "noi_o",
  "level": "A1",
  "lesson_order": 4,
  "points_correct": 10,
  "points_wrong": -4,
  "question": "Nối các danh từ chỉ phương hướng ở cột trái với tính từ và nghĩa tiếng Việt tương ứng ở cột phải:",
  "pairs": [
    { "left": "der Nordosten", "right": "nordöstlich (phía Đông Bắc)" },
    { "left": "der Südwesten", "right": "südwestlich (phía Tây Nam)" },
    { "left": "der Norden", "right": "nördlich (phía Bắc)" },
    { "left": "der Süden", "right": "südlich (phía Nam)" }
  ],
  "explanation": "Trong tiếng Đức, hướng phụ ghép chữ Bắc (Nord-) hoặc Nam (Süd-) đứng trước Đông (-osten) và Tây (-westen)."
}
```

### Dạng 6: Dịch câu Việt $\rightarrow$ Đức (`dich_cau_vd`) — Đúng `+15` | Sai `-6`
```json
{
  "type": "dich_cau_vd",
  "level": "A1",
  "lesson_order": 5,
  "points_correct": 15,
  "points_wrong": -6,
  "prompt_vi": "Phòng làm việc của tôi nhỏ nhưng sáng. Nó có một cái bàn và một cái ghế.",
  "question": "Dịch câu sau sang tiếng Đức:",
  "accepted_answers": [
    "Mein Arbeitszimmer ist klein, aber hell. Es hat einen Tisch und einen Stuhl.",
    "Mein Arbeitszimmer ist klein aber hell. Es hat einen Tisch und einen Stuhl.",
    "Mein Arbeitszimmer ist klein, aber es ist hell. Es hat einen Tisch und einen Stuhl.",
    "Mein Arbeitszimmer ist klein, aber hell. Es hat einen Stuhl und einen Tisch."
  ],
  "key_patterns": {
    "required_groups": [
      ["mein arbeitszimmer"],
      ["ist klein"],
      ["aber hell", "aber es ist hell"],
      ["es hat"],
      ["einen tisch"],
      ["einen stuhl"]
    ]
  },
  "explanation": "'das Arbeitszimmer' (giống trung) -> 'Mein Arbeitszimmer'. Sau 'Es hat' là Cách 4 (Akkusativ) nên 'der Tisch' -> 'einen Tisch' và 'der Stuhl' -> 'einen Stuhl'."
}
```

### Dạng 7: Dịch câu Đức $\rightarrow$ Việt (`dich_cau_dv`) — Đúng `+15` | Sai `-6`
```json
{
  "type": "dich_cau_dv",
  "level": "A1",
  "lesson_order": 4,
  "points_correct": 15,
  "points_wrong": -6,
  "prompt_de": "Gestern waren Paula und ich in Haiphong.",
  "question": "Dịch câu sau sang tiếng Việt:",
  "accepted_answers": [
    "Hôm qua Paula và tôi đã ở Hải Phòng",
    "Hôm qua Paula và mình đã ở Hải Phòng",
    "Hôm qua tôi và Paula đã ở Hải Phòng",
    "Hôm qua Paula và tôi ở Hải Phòng",
    "Ngày hôm qua Paula và tôi đã ở tại Hải Phòng",
    "Hôm qua Paula cùng với tôi đã ở Hải Phòng"
  ],
  "key_patterns": {
    "required_groups": [
      ["hôm qua", "ngày hôm qua"],
      ["paula"],
      ["tôi", "mình", "tớ", "em"],
      ["ở hải phòng", "tại hải phòng"]
    ]
  },
  "explanation": "'Gestern' = hôm qua; 'waren' là động từ 'sein' chia ở thì quá khứ đơn (Präteritum) cho ngôi 'wir' (Paula und ich) = đã ở."
}
```

### Dạng 8: Nghe và điền vào (`nghe_dien`) — Đúng `+10` | Sai `-4`
* **Cơ chế giao diện**:
  * Hiển thị nút bấm phát âm thanh nổi bật **`🔊 Nghe câu đọc (1.0x)`** và **`🐢 Nghe chậm (0.65x)`** sử dụng `window.speechSynthesis` giọng bản xứ `de-DE` (tự động phát 1 lần ngay khi câu hỏi hiện ra).
  * Hiển thị câu tiếng Đức có 1 chỗ trống `___` (kèm bản dịch nghĩa tiếng Việt bên dưới để định hướng ngữ cảnh), người chơi nghe và điền chính xác từ/cụm từ còn thiếu vào ô trống.
```json
{
  "type": "nghe_dien",
  "level": "A1",
  "lesson_order": 3,
  "points_correct": 10,
  "points_wrong": -4,
  "audio_text": "Das verstehe ich nicht. Können Sie das bitte buchstabieren?",
  "display_sentence": "Das verstehe ich nicht. Können Sie das bitte ___?",
  "hint_vi": "Điều đó tôi không hiểu. Ngài có thể làm ơn đánh vần từ đó được không?",
  "accepted_answers": ["buchstabieren"],
  "explanation": "Động từ nguyên mẫu 'buchstabieren' (đánh vần) đứng ở cuối câu khi đi cùng động từ khuyết thiếu 'Können'."
}
```

### Dạng 9: Điền vào chỗ trống để tạo thành câu (`dien_tao_cau`) — Đúng `+5` | Sai `-2`
* **Cơ chế giao diện**:
  * Đề bài đưa ra một khung câu có **2 đến 3 chỗ trống** (hoặc các thành phần gợi ý trong ngoặc + các thẻ từ gợi ý bên dưới).
  * Người chơi điền các từ còn thiếu vào các chỗ trống (hoặc bấm vào các thẻ từ gợi ý để điền nhanh vào từng ô trống) nhằm tạo thành một câu hoàn chỉnh đúng quy tắc vị trí động từ số 2 (`V2`) và khung câu tiếng Đức.
```json
{
  "type": "dien_tao_cau",
  "level": "A1",
  "lesson_order": 2,
  "points_correct": 5,
  "points_wrong": -2,
  "question": "Điền các từ thích hợp vào 3 chỗ trống để tạo thành câu hoàn chỉnh theo nghĩa: „Chúng tôi muốn thanh toán, làm ơn.“",
  "sentence_template": "Wir [1] bitte [2], hoặc: Wir [1] [2], [3].",
  "word_bank_hints": ["möchten", "zahlen", "bitte", "möchtet", "trinken"],
  "single_input_mode": true,
  "display_frame": "Wir ___ bitte ___.",
  "accepted_answers": [
    "möchten / zahlen",
    "möchten zahlen",
    "Wir möchten bitte zahlen",
    "Wir möchten zahlen, bitte"
  ],
  "slot_answers": [
    ["möchten", "moechten"],
    ["zahlen"]
  ],
  "explanation": "Với chủ ngữ 'Wir', động từ khuyết thiếu 'möchten' đứng ở vị trí số 2, còn động từ chính 'zahlen' (thanh toán) giữ nguyên mẫu ở cuối câu."
}
```

---

## PHẦN 5: THUẬT TOÁN CHẤM DỊCH ĐA ĐÁP ÁN & TỔ HỢP ĐỒNG NGHĨA (`FLEXIBLE TRANSLATION GRADER`)

Để đảm bảo khi người học làm các câu **Dịch nghĩa từ (`dich_nghia_vd`, `dich_nghia_dv`)** và **Dịch câu (`dich_cau_vd`, `dich_cau_dv`)**, dù diễn đạt theo văn phong cá nhân vẫn được chấm ĐÚNG công bằng, Antigravity IDE **bắt buộc phải cài đặt bộ chấm điểm 4 tầng** sau đây:

### 5.1. Tầng 1: Chuẩn hóa Chuỗi & Ký tự Đặc biệt (`String & Umlaut Normalizer`)
```javascript
function normalizeText(str, lang = 'de') {
    if (!str) return '';
    let s = str.toLowerCase().trim();
    // Xóa dấu câu ở đầu/cuối và chuẩn hóa khoảng trắng
    s = s.replace(/[.,!?;"'„“”«»()[\]]+/g, ' ').replace(/\s+/g, ' ').trim();
    if (lang === 'de') {
        // Hỗ trợ người dùng không có bàn phím tiếng Đức gõ ae, oe, ue, ss
        s = s.replace(/ä/g, 'ae').replace(/ö/g, 'oe').replace(/ü/g, 'ue').replace(/ß/g, 'ss');
        // Chuẩn hóa cách viết số phổ biến trong bài học
        const numMap = {
            'eins': '1', 'zwei': '2', 'drei': '3', 'vier': '4', 'fuenf': '5',
            'sechs': '6', 'sieben': '7', 'acht': '8', 'neun': '9', 'zehn': '10'
        };
        Object.keys(numMap).forEach(word => {
            s = s.replace(new RegExp(`\\b${word}\\b`, 'g'), numMap[word]);
        });
    }
    return s;
}
```

### 5.2. Tầng 2: Lược bỏ Từ Đệm / Lượng Từ Không Bắt Buộc Trong Tiếng Việt (`Vietnamese Optional Stopwords`)
Khi chấm câu trả lời bằng **Tiếng Việt** (`dich_nghia_dv` & `dich_cau_dv`), hệ thống so sánh cả bản gốc và bản đã rút gọn các từ đệm/hư từ mà người Việt có thể thêm hoặc bớt tùy thói quen:
* **Lượng từ đồ vật có thể lược bỏ khi so khớp cốt lõi**: `cái`, `chiếc`, `quyển`, `cuốn`, `tờ`, `bức`, `ngôi`, `căn`, `quả`, `trái`, `ly`, `cốc`, `tách`, `chai`.
  * *Ví dụ*: Đề hỏi `der Fernseher` $\rightarrow$ Người học gõ `"tivi"`, `"cái tivi"`, `"chiếc tivi"`, `"ti vi"`, `"màn hình tivi"`, `"vô tuyến"` đều khớp 100%!
* **Từ nối / Trợ từ cảm thán có thể có hoặc không**: `thì`, `là`, `mà`, `rất`, `khá`, `nhé`, `nha`, `ạ`, `vậy`, `đấy`, `đó`, `một`.
  * *Ví dụ*: Đề hỏi `Meine Küche ist klein und schön.` $\rightarrow$ Người học gõ:
    * *"Phòng bếp của tôi thì nhỏ và đẹp"*
    * *"Bếp của mình nhỏ và đẹp"*
    * *"Nhà bếp của tôi nhỏ mà đẹp"*
    * *"Căn bếp của em nhỏ và xinh đẹp"*
    $\rightarrow$ Tất cả đều được chấm **ĐÚNG (`+15 điểm`)**!

### 5.3. Tầng 3: Quy đổi Đồng nghĩa Đại từ & Từ vựng Phổ biến (`Synonym Equivalency Groups`)
Bộ chấm điểm tự động ánh xạ các nhóm từ đồng nghĩa về cùng một token chuẩn trước khi so khớp:
* **Nhóm đại từ tiếng Việt**:
  * `[tôi, mình, tớ, em, anh, chị]` (cho ngôi *ich*)
  * `[bạn, cậu, anh, chị, em, mày]` (cho ngôi *du*)
  * `[chúng tôi, chúng mình, chúng ta, tụi mình, bọn mình, bọn tôi]` (cho ngôi *wir*)
  * `[các bạn, các cậu, mọi người, tụi bây, các anh chị]` (cho ngôi *ihr*)
  * `[ngài, các ngài, quý khách, ông, bà, cô, chú, anh, chị, bạn]` (cho ngôi *Sie*)
  * `[anh ấy, ông ấy, cậu ấy, hắn, ảnh]` (cho ngôi *er*)
  * `[cô ấy, bà ấy, chị ấy, cổ, bả]` (cho ngôi *sie - số ít*)
* **Nhóm từ vựng đồng nghĩa thường gặp trong A1**:
  * `phòng bếp` $\equiv$ `nhà bếp` $\equiv$ `căn bếp` $\equiv$ `bếp`
  * `tủ sách` $\equiv$ `giá sách` $\equiv$ `kệ sách`
  * `bút bi` $\equiv$ `viết bi` $\equiv$ `cây bút bi`
  * `cục tẩy` $\equiv$ `cục gôm` $\equiv$ `tẩy` $\equiv$ `gôm`
  * `điện thoại di động` $\equiv$ `điện thoại` $\equiv$ `di động` $\equiv$ `dế yêu`
  * `thanh toán` $\equiv$ `trả tiền` $\equiv$ `tính tiền`
  * `ở phía bắc` $\equiv$ `nằm ở phía bắc` $\equiv$ `ở miền bắc` $\equiv$ `nằm về phía bắc`

### 5.4. Tầng 4: Chấp nhận Biến thể Ngữ pháp Tiếng Đức Hợp lệ (`German Syntactic Variants`)
Khi chấm câu trả lời bằng **Tiếng Đức** (`dich_nghia_vd` & `dich_cau_vd`):
1. **Đối với Dịch từ vựng (`dich_nghia_vd`)**:
   * Chấp nhận cả khi người học gõ **có mạo từ xác định** (`der Tisch`), **có mạo từ không xác định** (`ein Tisch`) hoặc **chỉ gõ danh từ gốc** (`Tisch`).
2. **Đối với Dịch câu (`dich_cau_vd`)**:
   * Chấp nhận hoán đổi vị trí trạng từ lịch sự `bitte` (*"Wir möchten bitte zahlen"* $\equiv$ *"Wir möchten zahlen, bitte"* $\equiv$ *"Bitte, wir möchten zahlen"*).
   * Chấp nhận hoán đổi 2 danh từ đẳng lập nối bằng `und` (*"Es hat einen Tisch und einen Stuhl"* $\equiv$ *"Es hat einen Stuhl und einen Tisch"*).
   * Chấp nhận cả 2 cấu trúc chỉ phương hướng (*"Ha Noi liegt im Norden von Vietnam"* $\equiv$ *"Ha Noi liegt nördlich von Vietnam"*).
   * Chấp nhận cả cách viết tách và viết gộp của giới từ (`im` $\equiv$ `in dem`, `am` $\equiv$ `an dem`).

---

## PHẦN 6: QUY CHUẨN ĐA DẠNG HÓA 9 DẠNG BÀI TẬP CHO TẤT CẢ CÁC BÀI TỪ BÀI 5 (A1) TRỞ ĐI

> **LƯU Ý QUAN TRỌNG**: Từ **Bài 5 (A1)** trở đi (và tất cả các bài A1, A2, B1, B2 tiếp theo), phần **Luyện tập 50 câu** của mỗi bài học **TUYỆT ĐỐI KHÔNG** được chỉ làm mỗi Trắc nghiệm và Điền từ đơn điệu như trước.

Mỗi bài học mới (50 câu) bắt buộc phải phân bổ đầy đủ cả **9 dạng bài tập** theo đúng tỷ lệ chuẩn sau đây:

| STT | Mã Dạng (`type`) | Tên Dạng Bài Tập Trong Phần Luyện Tập (Từ Bài 5 A1 trở đi) | Số Lượng / 50 Câu |
| :---: | :--- | :--- | :---: |
| **1** | **`trac_nghiem`** | Trắc nghiệm ngữ pháp, chia động từ, mạo từ & tình huống (4 đáp án A, B, C, D) | **8 câu** |
| **2** | **`dien_khuyet`** | Điền khuyết mạo từ, đuôi động từ, giới từ vào chỗ trống | **7 câu** |
| **3** | **`dich_nghia_vd`** | Dịch nghĩa từ / cụm từ từ **Tiếng Việt $\rightarrow$ Tiếng Đức** | **6 câu** |
| **4** | **`dich_nghia_dv`** | Dịch nghĩa từ / cụm từ từ **Tiếng Đức $\rightarrow$ Tiếng Việt** | **6 câu** |
| **5** | **`noi_o`** | **Nối ô từ trái qua phải** (4 cặp nối/bài: Từ vựng – Nghĩa, Chủ ngữ – Động từ, Câu hỏi – Đáp án) | **6 bài** |
| **6** | **`dien_tao_cau`** | **Điền vào chỗ trống để tạo thành câu hoàn chỉnh** (2–3 khoảng trống cấu trúc `V2` / khung câu) | **5 câu** |
| **7** | **`nghe_dien`** | **Nghe giọng đọc bản xứ `de-DE` và điền từ/cụm từ còn thiếu** | **4 câu** |
| **8** | **`dich_cau_vd`** | **Dịch câu hoàn chỉnh từ Tiếng Việt $\rightarrow$ Tiếng Đức** (chấm linh hoạt đa đáp án) | **4 câu** |
| **9** | **`dich_cau_dv`** | **Dịch câu hoàn chỉnh từ Tiếng Đức $\rightarrow$ Tiếng Việt** (chấm linh hoạt đa đáp án) | **4 câu** |
| | | **TỔNG CỘNG MỖI BÀI HỌC** | **50 CÂU / BÀI** |

---

## PHẦN 7: DANH SÁCH API BACKEND CẦN TRIỂN KHAI TRONG `app.py`

Antigravity IDE cần lập trình đầy đủ các API RESTful sau trong `app.py`:

1. **`GET /api/auth/check-username?username=...`**
   * Kiểm tra nhanh xem `username` có hợp lệ ($\ge 4$ ký tự) và đã tồn tại trong bảng `users` chưa (`SELECT 1 FROM users WHERE LOWER(username) = LOWER(?)`).
   * Trả về `{ "available": false, "message": "Tên tài khoản 'hieu3001' đã có người sử dụng!" }` nếu trùng.
2. **`POST /api/auth/register`**
   * Body: `{ "username": "...", "password": "..." }`.
   * Kiểm tra `len(username) >= 4`, `len(password) >= 8`, và kiểm tra trùng tên không phân biệt hoa thường.
   * Tạo tài khoản mới, tự động khởi tạo tiến độ mặc định (`A1 - Bài 1 P1`), đăng nhập luôn vào `session['user_id']` và trả về thông tin người dùng.
3. **`POST /api/auth/login`** & **`POST /api/auth/logout`** & **`GET /api/auth/me`**
   * Xác thực tài khoản, trả về thông tin người chơi hiện tại kèm:
     * `studied_lessons`: Danh sách các bài người dùng đã học.
     * `highest_level_code` & `highest_lesson_order`: Giới hạn trần câu hỏi Đấu trường.
     * `arena_attempts_today`: Số lượt Đấu trường đã chơi trong ngày hôm nay (`0`, `1` hoặc `2`).
     * `arena_remaining_today`: `max(0, 2 - arena_attempts_today)`.
4. **`POST /api/progress/mark-studied`**
   * Body: `{ "lesson_id": 5, "level_code": "A1", "lesson_order": 5 }`.
   * Lưu bài học người dùng vừa mở vào `user_studied_lessons` để Đấu trường tự động mở rộng phạm vi câu hỏi tới bài đó.
5. **`POST /api/arena/start`**
   * Kiểm tra người dùng đã đăng nhập chưa.
   * Kiểm tra số lượt chơi trong ngày (`play_date = YYYY-MM-DD` theo giờ VN). Nếu `>= 2` lượt $\rightarrow$ trả về `403 Forbidden`: *"Mỗi tài khoản chỉ được tham gia Đấu trường tối đa 2 lần mỗi ngày! Hãy quay lại vào ngày mai nhé."*
   * Nếu còn lượt:
     * Tạo bản ghi phiên đấu mới trong `arena_daily_attempts` (`attempt_number = 1` hoặc `2`).
     * Truy vấn toàn bộ bài tập thuộc các bài học nằm trong phạm vi đã học của người dùng (`<= highest_level_code` & `<= highest_lesson_order`), kết hợp với `ArenaProceduralGenerator` để xuất ra một danh sách **80 câu hỏi đã xáo trộn ngẫu nhiên** bao phủ đủ **9 dạng bài** (`trac_nghiem`, `dien_khuyet`, `dich_nghia_vd`, `dich_nghia_dv`, `noi_o`, `dich_cau_vd`, `dich_cau_dv`, `nghe_dien`, `dien_tao_cau`).
6. **`POST /api/arena/finish`**
   * Body: `{ "session_token": "...", "final_score": 145, "correct_count": 18, "wrong_count": 3, "breakdown": {...} }`.
   * Cập nhật trạng thái phiên đấu thành `completed`, lưu điểm vào `arena_daily_attempts`, cập nhật `total_exp = total_exp + MAX(0, final_score)` và `arena_best_score = MAX(arena_best_score, final_score)` trong bảng `users`.
7. **`GET /api/arena/leaderboard`**
   * Trả về 2 danh sách xếp hạng thực tế từ Database:
     * `daily_top`: Top người chơi có điểm ván đấu cao nhất trong ngày hôm nay (`play_date = hôm nay`).
     * `all_time_top`: Top người chơi có `arena_best_score` và `total_exp` cao nhất hệ thống.

---

## PHẦN 8: GIAO DIỆN ĐẤU TRƯỜNG & MODAL ĐĂNG NHẬP TRÊN `templates/index.html`

1. **Thanh Header Tài Khoản**:
   * Nếu chưa đăng nhập: Hiển thị nút nổi bật **`🔐 Đăng nhập / Đăng ký Đua Top`**.
   * Nếu đã đăng nhập: Hiển thị **`👤 [username]`** | **`📚 Tiến độ: A1 - Bài X`** | **`🎟️ Lượt Đấu trường: Còn X/2`** | Nút **`Đăng xuất`**.
2. **Modal Đăng Nhập / Đăng Ký**:
   * Chuyển đổi mượt mà giữa 2 chế độ: **Đăng nhập** và **Tạo tài khoản thi đua mới**.
   * Ô nhập `Tên tài khoản (tối thiểu 4 ký tự)` có kiểm tra realtime (debounce 300ms gọi `/api/auth/check-username`): nếu người dùng gõ tên đã tồn tại (ví dụ `hieu3001`), hiển thị ngay dòng chữ đỏ dưới ô nhập: *"❌ Tên 'hieu3001' đã có người sử dụng, không thể đặt trùng tên!"*.
   * Ô nhập `Mật khẩu (tối thiểu 8 ký tự)` có nút ẩn/hiện mật khẩu và đếm số ký tự.
3. **Màn Hình Sân Đấu Đấu Trường 2 Phút**:
   * **Header Sân Đấu**:
     * Đồng hồ lớn: **`⏱️ 02:00`** (đếm ngược từng giây từ `120s` về `0s`, đổi màu cam khi `< 30s`, nhấp nháy đỏ khi `< 10s`).
     * Bảng điểm trực tiếp: **`⚡ Điểm hiện tại: 0`** (kèm hiệu ứng chữ bay lên `+5`, `+7`, `+6`, `+10`, `+15` màu xanh hoặc `-2`, `-3`, `-4`, `-6` màu đỏ).
     * Huy hiệu phạm vi kiến thức: **`🎯 Phạm vi đề: Chỉ lấy kiến thức từ A1 Bài 1 -> Bài hiện tại bạn đã học`**.
     * Huy hiệu lượt chơi: **`🎟️ Lượt hôm nay: Còn X/2 lượt`**.
   * **Bảng Quy Tắc Điểm Số Hiển Thị Rõ Trước Khi Bắt Đầu Ván**:
     * Trắc nghiệm: **`+5 / -2`** | Điền khuyết: **`+7 / -3`** | Dịch nghĩa từ (Việt $\rightleftarrows$ Đức): **`+6 / -3`**
     * Nối ô trái – phải: **`+10 / -4`** *(sai 1 cặp cũng `-4`)* | Dịch câu (Việt $\rightleftarrows$ Đức): **`+15 / -6`**
     * Nghe & điền: **`+10 / -4`** | Điền tạo thành câu: **`+5 / -2`**.

---

## PHẦN 9: TRÌNH TỰ THỰC THI DÀNH CHO ANTIGRAVITY IDE

1. **Bước 1**: Nâng cấp `database.py` để tạo các bảng `users`, `user_studied_lessons`, `arena_daily_attempts` (giữ nguyên toàn bộ dữ liệu các bảng bài học cũ).
2. **Bước 2**: Tạo mô-đun `arena_generator.py` chứa bộ lọc câu hỏi theo tiến độ bài đã học (`user_studied_lessons`) và bộ sinh câu hỏi động bao phủ đủ **9 dạng bài** cho từng bài học từ Bài 1 (P1) đến Bài 4 (và tự động mở rộng cho các bài tiếp theo).
3. **Bước 3**: Cập nhật `app.py` để thêm đầy đủ các API Đăng ký (chặn trùng tên `UNIQUE COLLATE NOCASE`, kiểm tra `username >= 4`, `password >= 8`), Đăng nhập, Ghi nhận tiến độ bài đã học, Kiểm tra giới hạn `2 lượt/ngày` và Xử lý điểm số Bảng Xếp Hạng.
4. **Bước 4**: Cập nhật `templates/index.html` (và tệp JS đi kèm) để tích hợp Modal Đăng nhập/Đăng ký, Giao diện Đấu trường 2 phút với đủ 9 dạng câu hỏi tương tác (đặc biệt là giao diện **Nối ô trái – phải**, **Nghe & điền**, **Điền chỗ trống tạo câu**) và Bộ chấm điểm dịch đa đáp án linh hoạt (`evaluateFlexibleTranslation`).
5. **Bước 5**: Chạy thử nghiệm máy chủ Flask để kiểm tra toàn bộ luồng Đăng ký trùng tên (`hieu3001`), giới hạn 2 lượt/ngày, đồng hồ 120s và 9 dạng bài tập, sau đó đẩy code lên GitHub (`git add . && git commit -m "Implement deep Speed Arena 2-min 9-types engine, progression filter, 2 daily limit, and unique user auth" && git push`).