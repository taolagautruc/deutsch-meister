# HƯỚNG DẪN CẬP NHẬT HỆ THỐNG DEUTSCHMEISTER (BÀI 1 - PHẦN 1: A1)

Tài liệu này là đặc tả kỹ thuật dành cho AI Agent / Antigravity IDE để nâng cấp **Bài 1 (P1): "Làm Quen Với Tiếng Đức, Bảng Chữ Cái và Đếm Số"** trong dự án web học tiếng Đức **DeutschMeister (A1 - B2)**.

---

## 1. Cấu trúc thư mục hiện tại của dự án

```text
deutsch_meister/
├── app.py                  # Máy chủ Flask & REST API kết nối SQLite
├── database.py             # Khởi tạo bảng cơ sở dữ liệu SQLite (deutsch_meister.db)
├── deutsch_meister.db      # Tệp cơ sở dữ liệu SQLite
├── setup_exercises.py      # Tệp khởi tạo bảng exercises ban đầu
├── seed_a1_b1_p1.py        # Tệp nạp dữ liệu Lý thuyết, Từ vựng & Bài tập của Bài 1 (P1)
└── templates/
    └── index.html          # Giao diện người dùng (TailwindCSS + Vanilla JS)
```

---

## 2. Danh sách 4 hạng mục cần thực hiện (Yêu cầu bắt buộc)

### Hạng mục 1: Xóa bỏ hoàn toàn liên kết YouTube trong Bài 1 (P1)
* **Vấn đề hiện tại**: Trong phần lý thuyết của `seed_a1_b1_p1.py` đang có khối banner `"Video Bài Giảng Gốc"` kèm nút `"Xem trên YouTube"` trỏ ra link bên ngoài.
* **Yêu cầu xử lý**:
  1. Trong tệp `seed_a1_b1_p1.py`, xóa bỏ hoàn toàn thẻ `<div>` chứa tiêu đề `"Video Bài Giảng Gốc"` và thẻ `<a href="https://www.youtube.com/...">Xem trên YouTube</a>`.
  2. Thay thế bằng một khối giới thiệu tổng quan bài học mang thương hiệu riêng của dự án **DeutschMeister** (ví dụ: *"Mục tiêu bài học: Nắm vững 26 chữ cái Latinh, 4 ký tự đặc biệt (Ä, Ö, Ü, ß), quy tắc ghép âm chuẩn bản xứ, mẫu câu chào hỏi - giới thiệu bản thân và hệ thống số đếm từ $0$ đến $9999$."*).

---

### Hạng mục 2: Nâng cấp Bảng Chữ Cái (`Das Alphabet`) có Phiên âm chi tiết & Nút phát âm từng chữ cái
* **Vấn đề hiện tại**: Mục `1. BẢNG CHỮ CÁI TIẾNG ĐỨC (DAS ALPHABET) & 4 KÝ TỰ ĐẶC BIỆT` hiện chỉ là văn bản tĩnh (`A [a]`, `B [be]`...), người học không bấm vào để nghe phát âm mẫu từng chữ cái được và thiếu hướng dẫn khẩu hình/phiên âm rõ ràng.
* **Yêu cầu xử lý**:
  1. Thiết kế lại bảng 26 chữ cái (`A` đến `Z`) và 4 chữ cái đặc biệt (`Ä`, `Ö`, `Ü`, `ß`) thành các **thẻ tương tác (Interactive Cards/Buttons)**.
  2. Mỗi thẻ chữ cái phải hiển thị đầy đủ 3 thông tin:
     * **Chữ cái in hoa & in thường**: Ví dụ `A a`, `B b`, ..., `Ä ä`, `Ö ö`, `Ü ü`, `ß`.
     * **Phiên âm quốc tế (IPA) & Gợi ý cách đọc tiếng Việt**:
       * `A a`: `/aː/` (đọc như *a*)
       * `B b`: `/beː/` (đọc như *bê*)
       * `C c`: `/tseː/` (đọc như *tsê*)
       * `D d`: `/deː/` (đọc như *đê*)
       * `E e`: `/eː/` (đọc như *ê*)
       * `F f`: `/ɛf/` (đọc như *ép-phờ*)
       * `G g`: `/geː/` (đọc như *ghê*)
       * `H h`: `/haː/` (đọc như *ha*)
       * `I i`: `/iː/` (đọc như *i*)
       * `J j`: `/jɔt/` (đọc như *dốt*)
       * `K k`: `/kaː/` (đọc như *ca*)
       * `L l`: `/ɛl/` (đọc như *en-lờ*)
       * `M m`: `/ɛm/` (đọc như *em-mờ*)
       * `N n`: `/ɛn/` (đọc như *en-nờ*)
       * `O o`: `/oː/` (đọc như *ô*)
       * `P p`: `/peː/` (đọc như *pê*)
       * `Q q`: `/kuː/` (đọc như *cu*)
       * `R r`: `/ɛɐ̯/` (đọc như *e-rờ* rung cuống họng)
       * `S s`: `/ɛs/` (đọc như *ét-sờ*)
       * `T t`: `/teː/` (đọc như *thê* bật hơi)
       * `U u`: `/uː/` (đọc như *u*)
       * `V v`: `/faʊ̯/` (đọc là *phao* — khi vào từ đọc như *ph*)
       * `W w`: `/veː/` (đọc là *vê* — khi vào từ đọc như *v*)
       * `X x`: `/ɪks/` (đọc như *ích-xờ*)
       * `Y y`: `/ˈʏpsilɔn/` (đọc như *uýp-xi-lon*)
       * `Z z`: `/tsɛt/` (đọc như *tsét*)
       * `Ä ä`: `/ɛː/` (*a-Umlaut* — miệng mở rộng đọc âm *ê*)
       * `Ö ö`: `/øː/` (*o-Umlaut* — tròn môi chữ *ô* nhưng phát âm chữ *ê*)
       * `Ü ü`: `/yː/` (*u-Umlaut* — tròn môi chữ *u* nhưng phát âm chữ *uy*)
       * `ß`: `/ɛsˈtsɛt/` (*Eszett* — đọc như âm *x/s* kéo dài)
     * **Nút bấm phát âm (`🔊`)**: Khi người học bấm vào bất kỳ chữ cái nào (hoặc 4 thành phố mẫu `HAMBURG`, `FRANKFURT`, `BERLIN`, `MÜNCHEN`), hệ thống sẽ phát âm chuẩn tên chữ cái đó bằng tiếng Đức.

---

### Hạng mục 3: Sửa triệt để lỗi Giọng đọc (Voice TTS) bị sai trên Safari / macOS (`die`, `Tschüss`, mạo từ, chữ cái đơn)
* **Vấn đề hiện tại**:
  * Khi dùng `window.speechSynthesis` mặc định trên Safari (macOS), nếu không chỉ định rõ đối tượng giọng đọc `SpeechSynthesisVoice` bản xứ (`de-DE`), trình duyệt thường lấy giọng mặc định của máy (tiếng Anh hoặc tiếng Việt) để đọc chữ tiếng Đức. Hậu quả là từ `"die"` bị đọc thành *"đai"* (tiếng Anh), `"Tschüss"` bị đọc sai âm `ü` và `tsch`, các từ như `"das Rad"`, `"das Spiel"`, `"das Tier"` bị đọc cứng và sai ngữ điệu.
  * Khi truyền 1 chữ cái đơn lẻ (như `'V'`, `'W'`, `'J'`, `'Y'`, `'Z'`) vào TTS, máy đọc không chuẩn tên chữ cái trong bảng chữ cái.
* **Yêu cầu xử lý trong `templates/index.html`**:
  1. **Khóa giọng đọc bản xứ Đức (`de-DE` Voice Locking)**:
     * Viết hàm `getBestGermanVoice()` lắng nghe sự kiện `window.speechSynthesis.onvoiceschanged`.
     * Lọc danh sách `speechSynthesis.getVoices()` chỉ lấy các giọng có `lang` là `'de-DE'` hoặc `'de_DE'` (ưu tiên giọng chất lượng cao trên macOS/Chrome như `'Anna'`, `'Helena'`, `'Petra'`, `'Markus'`, `'Yannick'`, `'Google Deutsch'`, `'Microsoft Katja'`).
     * Gán trực tiếp `utterance.voice = bestGermanVoice` và `utterance.lang = 'de-DE'`.
  2. **Bảng ánh xạ chuẩn hóa phát âm (`GERMAN_PRONUNCIATION_MAP`)**:
     * Trước khi đưa chuỗi vào hàm `speakGerman(text, rate)`, kiểm tra qua từ điển chuẩn hóa để tránh việc TTS đọc sai các từ ngắn hoặc chữ cái đơn:
       ```javascript
       const GERMAN_PRONUNCIATION_MAP = {
           // Chữ cái đơn trong bảng chữ cái
           "A": "A", "B": "Be", "C": "Ce", "D": "De", "E": "E", "F": "Ef",
           "G": "Ge", "H": "Ha", "I": "I", "J": "Jot", "K": "Ka", "L": "El",
           "M": "Em", "N": "En", "O": "O", "P": "Pe", "Q": "Ku", "R": "Er",
           "S": "Es", "T": "Te", "U": "U", "V": "Vau", "W": "We", "X": "Iks",
           "Y": "Üpsilon", "Z": "Zett", "Ä": "Ä", "Ö": "Ö", "Ü": "Ü", "ß": "Eszett",
           // Các từ ngắn dễ bị trình duyệt nhận diện nhầm sang tiếng Anh
           "die": "die.",
           "der": "der.",
           "das": "das.",
           "Tschüss": "Tschüüs!",
           "Tschüss!": "Tschüüs!",
           "Hi": "Hi!",
           "das Bier": "das Bier.",
           "das Tier": "das Tier.",
           "das Tor": "das Tor.",
           "das Rad": "das Rad.",
           "das Spiel": "das Spiel.",
           "die Tür": "die Tür.",
           "die Küche": "die Küche."
       };
       ```
     * Việc thêm dấu chấm câu `.` hoặc `!` và gán đúng `utterance.voice` (`de-DE`, `rate = 0.9`, `pitch = 1.0`) sẽ buộc bộ tổng hợp âm thanh của macOS Safari đọc chuẩn âm `/diː/` cho `"die"` và tròn môi chuẩn âm `/tʃʏs/` cho `"Tschüss"`.
  3. **Thêm cơ chế Fallback Audio (Dự phòng)**: Nếu trình duyệt của người dùng không cài giọng `de-DE` trong máy, tự động sử dụng luồng phát âm thanh dự phòng hoặc thông báo chọn giọng `de-DE`.

---

### Hạng mục 4: Mở rộng Kho Bài Tập lên 50 Câu & Tự động Random đổi đề phần Số đếm (Đọc số / Viết số)
* **Vấn đề hiện tại**:
  * Số lượng bài tập hiện tại chỉ có 37 câu là quá ít.
  * Các câu hỏi về số đếm (viết số từ tiếng Đức sang số tự nhiên và từ số tự nhiên sang chữ tiếng Đức) hiện đang cố định một vài số (như `83, 92, 677, 1234`), làm xong 1 lần là thuộc đáp án, không rèn luyện phản xạ lâu dài được.
* **Yêu cầu xử lý**:
  1. **Mở rộng CSDL lên đúng 50 câu hỏi đa dạng trong `seed_a1_b1_p1.py`**:
     * Phân bổ đều và phong phú trên cả 7 dạng bài tập của Bài 1 (P1):
       * **Dạng 1 - Trắc nghiệm (`trac_nghiem`)**: 10 câu (Bảng chữ cái, quy tắc phát âm `ei/ie`, `eu/äu`, `ch`, `sp/st`, chào hỏi, số bất quy tắc `16, 17, 30, 60, 70`).
       * **Dạng 2 - Điền khuyết (`dien_khuyet`)**: 8 câu (`Wer, Wie, Woher, Wo, heißen, kommen aus, wohnen in, Guten Morgen/Tag/Abend, Gute Nacht`).
       * **Dạng 3 - Dịch 2 chiều Việt ⇄ Đức & Đổi số (`dich`)**: 8 câu (Dịch câu giao tiếp Việt $\leftrightarrow$ Đức + Đổi chữ số tiếng Đức sang số tự nhiên).
       * **Dạng 4 - Luyện Nghe 1.0x & 0.65x (`nghe`)**: 7 câu (Nghe từ vựng có Umlaut, nghe câu giao tiếp, nghe số đếm 2-3-4 chữ số và nhập số).
       * **Dạng 5 - Luyện Nói & Phát âm (`noi`)**: 5 câu (Phát âm từ chứa `ä, ö, ü, ß, sch, tsch`, đọc câu tự giới thiệu, đọc dãy số).
       * **Dạng 6 - Đọc hiểu hội thoại (`doc`)**: 4 câu (Đọc các đoạn hội thoại làm quen, hỏi tên, quê quán, nơi ở, tuổi và số nhà/số điện thoại).
       * **Dạng 7 - Viết câu & Viết số chuyên sâu (`viet`)**: 8 câu (Viết số 1 chữ số, 2 chữ số, 3 chữ số, 4 chữ số từ số sang chữ tiếng Đức và ngược lại, viết câu tự giới thiệu hoàn chỉnh).
     * **Tổng cộng**: $10 + 8 + 8 + 7 + 5 + 4 + 8 = 50$ câu hỏi trong cơ sở dữ liệu.

  2. **Cơ chế Random tự động đổi đề cho các bài tập Số đếm (Dynamic Number Exercise Generator)**:
     * Xây dựng hàm chuyển đổi số tự nhiên sang chữ tiếng Đức chuẩn xác 100% trong JavaScript (`numberToGerman(n)` cho $0 \le n \le 9999$) ngay trong `templates/index.html`:
       * Xử lý đúng các số cơ bản $0 \to 12$ (`null, eins, zwei, ..., elf, zwölf`).
       * Xử lý đúng $13 \to 19$ (`dreizehn, ..., sechzehn, siebzehn, ...`).
       * Xử lý đúng số tròn chục (`zwanzig, dreißig, vierzig, fünfzig, sechzig, siebzig, achtzig, neunzig`).
       * Xử lý đúng số ghép 2 chữ số (`21` $\to$ `einundzwanzig`, lưu ý `1` bỏ `s` thành `ein`).
       * Xử lý đúng số 3 và 4 chữ số (`hundert`, `tausend`, không dùng `und` ngay sau `hundert`/`tausend`, ví dụ `707` $\to$ `siebenhundertsieben`, `1234` $\to$ `eintausendzweihundertvierunddreißig`, chấp nhận cả `hundert...` và `einhundert...`, `tausend...` và `eintausend...`).
     * **Khi nào hệ thống tự động Random số mới?**:
       1. **Khi người học trả lời ĐÚNG** một câu hỏi về số đếm (Nghe số, Đổi chữ sang số, Viết số sang chữ): Hiển thị thông báo chúc mừng + cộng EXP, đồng thời hiện nút **`🔄 Đổi số khác để luyện tiếp`** (hoặc tự động sinh số mới sau 2.5 giây) để người học luyện tập liên tục không giới hạn.
       2. **Khi người học thoát khỏi phần Bài tập** (chuyển sang tab Lý thuyết, Đấu trường, Cấp độ) rồi **quay lại phần Bài tập**, hoặc bấm nút **`🎲 Đổi bộ số ngẫu nhiên mới`** ở đầu khu vực bài tập: Toàn bộ các câu hỏi thuộc nhóm Số đếm (2 chữ số, 3 chữ số, 4 chữ số, nghe số, đọc số, viết số) sẽ tự động sinh ra các con số ngẫu nhiên hoàn toàn mới kèm đáp án và lời giải thích mới tương ứng!

---

## 3. Thuật toán chuẩn `numberToGerman(n)` (Từ 0 đến 9999) để tích hợp vào Frontend/Backend

AI Agent cần tích hợp hàm dưới đây vào `templates/index.html` để phục vụ việc sinh đề số đếm ngẫu nhiên:

```javascript
function numberToGerman(n) {
    n = parseInt(n, 10);
    if (isNaN(n) || n < 0 || n > 9999) return "";
    if (n === 0) return "null";

    const ones = ["", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"];
    const teens = {
        10: "zehn", 11: "elf", 12: "zwölf", 13: "dreizehn", 14: "vierzehn",
        15: "fünfzehn", 16: "sechzehn", 17: "siebzehn", 18: "achtzehn", 19: "neunzehn"
    };
    const tens = {
        2: "zwanzig", 3: "dreißig", 4: "vierzig", 5: "fünfzig",
        6: "sechzig", 7: "siebzig", 8: "achtzig", 9: "neunzig"
    };

    function convertUnder100(num) {
        if (num === 0) return "";
        if (num === 1) return "eins";
        if (num < 10) return ones[num];
        if (num < 20) return teens[num];
        const t = Math.floor(num / 10);
        const o = num % 10;
        if (o === 0) return tens[t];
        return `${ones[o]}und${tens[t]}`;
    }

    let result = "";
    if (n >= 1000) {
        const th = Math.floor(n / 1000);
        result += (th === 1 ? "eintausend" : `${ones[th]}tausend`);
        n %= 1000;
    }
    if (n >= 100) {
        const h = Math.floor(n / 100);
        result += (h === 1 ? "einhundert" : `${ones[h]}hundert`);
        n %= 100;
    }
    if (n > 0) {
        result += convertUnder100(n);
    }
    return result;
}
```

*Lưu ý khi chấm điểm số có hàng trăm/nghìn*: Nếu số bắt đầu bằng `100` hoặc `1000`, cần chấp nhận cả 2 cách viết có hoặc không có chữ `ein` ở đầu (ví dụ: `121` chấp nhận cả `einhunderteinundzwanzig` và `hunderteinundzwanzig`).

---

## 4. Các bước thực thi dành cho Antigravity IDE

Khi đọc tệp `README.md` này, Antigravity IDE hãy thực hiện lần lượt các bước sau:
1. **Cập nhật `seed_a1_b1_p1.py`**:
   * Xóa bỏ hoàn toàn khối link YouTube.
   * Cập nhật bảng chữ cái (`A-Z`, `Ä, Ö, Ü, ß`) và 4 thành phố mẫu trong `grammar_html` có đầy đủ phiên âm và gắn sự kiện `onclick="speakGerman(...)"` cho từng chữ cái.
   * Nạp đủ **50 câu hỏi** vào bảng `exercises`, đánh dấu các câu hỏi về số đếm bằng cờ `"dynamic_number": true` (kèm phạm vi số như `min: 21, max: 99` hoặc `min: 100, max: 999` hoặc `min: 1000, max: 9999`) trong cột `extra_data` (dạng JSON).
2. **Cập nhật `templates/index.html`**:
   * Nâng cấp hàm `speakGerman(text, rate)` với bộ lọc giọng `de-DE` bản xứ và từ điển `GERMAN_PRONUNCIATION_MAP` để khắc phục triệt để lỗi phát âm từ `die`, `Tschüss`, v.v.
   * Tích hợp hàm `numberToGerman(n)` và hàm `randomizeNumberExercises()` để mỗi khi người học mở phần bài tập, chuyển tab hoặc hoàn thành 1 câu số đếm, đề bài sẽ tự động đổi sang con số ngẫu nhiên mới.
3. **Chạy lệnh cập nhật Database**:
   * Thực thi `python3 seed_a1_b1_p1.py` để cập nhật lại tệp `deutsch_meister.db`.
   * Khởi động lại máy chủ `python3 app.py` và kiểm tra trên `http://127.0.0.1:5000`.