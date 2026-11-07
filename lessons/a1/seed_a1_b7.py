import json
import os
import sys

true = True
false = False
null = None

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_7():
    conn = get_connection()
    cursor = conn.cursor()

    # Đảm bảo bảng exercises có cột extra_data
    cursor.execute("PRAGMA table_info(exercises);")
    columns = [col["name"] for col in cursor.fetchall()]
    if "extra_data" not in columns:
        cursor.execute("ALTER TABLE exercises ADD COLUMN extra_data TEXT;")

    cursor.execute("SELECT id FROM levels WHERE code = 'A1';")
    level_a1 = cursor.fetchone()
    if not level_a1:
        print("❌ Hãy chạy database.py trước!")
        conn.close()
        return
    a1_id = level_a1["id"]

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 7%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 21

    # Xóa dữ liệu cũ của Bài 7 nếu có để cập nhật sạch sẽ (Bảo toàn tuyệt đối Bài 1 -> Bài 6)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    lesson_title = 'Bài 7: "Beruf - Modalverben - Artikelwörter in Akkusativ (Nghề nghiệp - Động từ khuyết thiếu - Từ hạn định Cách 4 & Phân biệt Akkusativ / Dativ)"'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 7 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Beruf • Modalverben • Akkusativ vs. Dativ (Bài 7)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 120 phút • ⚡ 1800+ EXP • 🎯 100 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Bài 7: Beruf - Modalverben - Artikelwörter in Akkusativ (Nghề nghiệp - Động từ khuyết thiếu - Từ hạn định Cách 4 & Phân biệt Akkusativ / Dativ)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Nắm vững hệ thống từ vựng <b>Nghề nghiệp (Nam/Nữ)</b>, <b>Nơi làm việc</b> và cấu trúc hỏi đáp nghề nghiệp chuẩn Đức (<i>Was sind Sie von Beruf? / Was machen Sie beruflich? / Was ist Ihr Beruf?</i>); làm chủ các <b>Động từ khuyết thiếu (möchten, müssen, können, wollen, dürfen, sollen)</b> và cấu trúc khung câu (<i>Satzklammer</i>) với động từ tách; hệ thống bảng ma trận <b>Từ hạn định ở Cách 4 (Artikelwörter im Akkusativ)</b> theo 9 ngôi; và cẩm nang chuyên sâu <b>Phân biệt Cách 4 (Akkusativ) vs. Cách 3 (Dativ)</b> theo 3 tiêu chí cốt lõi: vai trò động từ, nhóm giới từ cố định và cặp đối chiếu <i>Wohin? (Akkusativ)</i> vs. <i>Wo? (Dativ)</i>.
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: NGHỀ NGHIỆP, NƠI LÀM VIỆC & CẤU TRÚC HỎI ĐÁP -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Nghề Nghiệp (Berufe), Nơi Làm Việc (Arbeitsorte) & Cấu Trúc Hỏi Đáp</h4>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>💡</span> Quy tắc Cấu tạo Danh từ Nghề nghiệp Nam (der) → Nữ (die):</p>
                <ol class="list-decimal pl-5 space-y-1 text-slate-700">
                    <li><b>Quy tắc chung (90% các nghề):</b> Lấy danh từ Nam (<i>der ...</i>) thêm hậu tố <b>-in</b> thành Nữ (<i>die ...-in</i>). Khi sang số nhiều, danh từ Nữ bắt buộc gấp đôi chữ n thành <b>-innen</b> (<i>die Lehrerin → die Lehrerinnen</i>).</li>
                    <li><b>Biến âm Umlaut (a → ä, o → ö):</b> <i>der Arzt → die <b>Ä</b>rztin</i>; <i>der Koch → die <b>K</b>öchin</i>; <i>der Bauer → die <b>B</b>äuerin</i>.</li>
                    <li><b>Đổi gốc từ đặc biệt:</b> <i>der Hausmann → die Haus<b>frau</b></i>; <i>der Krankenpfleger → die Krankenpflegerin / die Krankenschwester</i>; <i>der Kaufmann → die Kauffrau</i>.</li>
                </ol>
            </div>

            <!-- Bảng 1.1: 16 Cặp nghề nghiệp trọng tâm -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>👨‍💼</span> 1.1. Bảng 16 Cặp Nghề Nghiệp Trọng Tâm (Nam – Nữ – Hoạt Động & Nơi Làm Việc)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">STT</th>
                                <th class="p-3">Nghề Nam (der)</th>
                                <th class="p-3">Nghề Nữ (die)</th>
                                <th class="p-3">Nghĩa Tiếng Việt</th>
                                <th class="p-3">Hoạt Động & Nơi Làm Việc (Dativ)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">1</td>
                                <td class="p-3 font-bold text-blue-600">der Programmierer</td>
                                <td class="p-3 font-bold text-rose-600">die Programmiererin</td>
                                <td class="p-3">lập trình viên</td>
                                <td class="p-3">schreibt Computerprogramme <b>im Büro</b> / in einer IT-Firma</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">2</td>
                                <td class="p-3 font-bold text-blue-600">der Taxifahrer</td>
                                <td class="p-3 font-bold text-rose-600">die Taxifahrerin</td>
                                <td class="p-3">tài xế taxi</td>
                                <td class="p-3">fährt Fahrgäste <b>mit dem Taxi</b> durch die Stadt</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">3</td>
                                <td class="p-3 font-bold text-blue-600">der Krankenpfleger</td>
                                <td class="p-3 font-bold text-rose-600">die Krankenpflegerin / Krankenschwester</td>
                                <td class="p-3">y tá, điều dưỡng</td>
                                <td class="p-3">hilft den Ärzten und pflegt Patienten <b>im Krankenhaus</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">4</td>
                                <td class="p-3 font-bold text-blue-600">der Florist</td>
                                <td class="p-3 font-bold text-rose-600">die Floristin</td>
                                <td class="p-3">người bán hoa</td>
                                <td class="p-3">verkauft schöne Blumen <b>im Blumengeschäft</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">5</td>
                                <td class="p-3 font-bold text-blue-600">der Verkäufer</td>
                                <td class="p-3 font-bold text-rose-600">die Verkäuferin</td>
                                <td class="p-3">nhân viên bán hàng</td>
                                <td class="p-3">verkauft Schuhe <b>im Schuhgeschäft</b> / Lebensmittel <b>im Supermarkt</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">6</td>
                                <td class="p-3 font-bold text-blue-600">der (KFZ-)Mechatroniker</td>
                                <td class="p-3 font-bold text-rose-600">die (KFZ-)Mechatronikerin</td>
                                <td class="p-3">thợ cơ khí ô tô</td>
                                <td class="p-3">repariert Autos und Motoren <b>in einer Werkstatt</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">7</td>
                                <td class="p-3 font-bold text-blue-600">der Trainer</td>
                                <td class="p-3 font-bold text-rose-600">die Trainerin</td>
                                <td class="p-3">huấn luyện viên</td>
                                <td class="p-3">trainiert Sportler <b>im Fitnessstudio</b> / <b>im Stadion</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">8</td>
                                <td class="p-3 font-bold text-blue-600">der Lehrer</td>
                                <td class="p-3 font-bold text-rose-600">die Lehrerin</td>
                                <td class="p-3">giáo viên</td>
                                <td class="p-3">unterrichtet Schüler <b>an einer Schule</b> / <b>im Sprachzentrum</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">9</td>
                                <td class="p-3 font-bold text-blue-600">der Schüler</td>
                                <td class="p-3 font-bold text-rose-600">die Schülerin</td>
                                <td class="p-3">học sinh (cấp 1-3)</td>
                                <td class="p-3">lernt viele Fächer <b>in der Schule</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">10</td>
                                <td class="p-3 font-bold text-blue-600">der Student</td>
                                <td class="p-3 font-bold text-rose-600">die Studentin</td>
                                <td class="p-3">sinh viên đại học</td>
                                <td class="p-3">studiert <b>an der Universität</b> / an einer Hochschule</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">11</td>
                                <td class="p-3 font-bold text-blue-600">der Sekretär</td>
                                <td class="p-3 font-bold text-rose-600">die Sekretärin</td>
                                <td class="p-3">thư ký</td>
                                <td class="p-3">schreibt E-Mails und ruft Kunden <b>im Büro</b> an</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">12</td>
                                <td class="p-3 font-bold text-blue-600">der Friseur</td>
                                <td class="p-3 font-bold text-rose-600">die Friseurin</td>
                                <td class="p-3">thợ làm tóc</td>
                                <td class="p-3">schneidet Haare <b>im Friseursalon</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-slate-400">13</td>
                                <td class="p-3 font-bold text-blue-600">der Kellner</td>
                                <td class="p-3 font-bold text-rose-600">die Kellnerin</td>
                                <td class="p-3">nhân viên bồi bàn</td>
                                <td class="p-3">bedient Gäste <b>im Restaurant</b> / im Café</td>
                            </tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/30">
                                <td class="p-3 font-bold text-slate-400">14</td>
                                <td class="p-3 font-bold text-blue-600">der Koch ⚠️</td>
                                <td class="p-3 font-bold text-rose-600">die K<u>ö</u>chin ⚠️</td>
                                <td class="p-3">đầu bếp</td>
                                <td class="p-3">kocht leckere Speisen <b>im Restaurant</b> / in der Kantine</td>
                            </tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/30">
                                <td class="p-3 font-bold text-slate-400">15</td>
                                <td class="p-3 font-bold text-blue-600">der Arzt ⚠️</td>
                                <td class="p-3 font-bold text-rose-600">die <u>Ä</u>rztin ⚠️</td>
                                <td class="p-3">bác sĩ</td>
                                <td class="p-3">untersucht Patienten <b>im Krankenhaus</b> / in einer Praxis</td>
                            </tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/30">
                                <td class="p-3 font-bold text-slate-400">16</td>
                                <td class="p-3 font-bold text-blue-600">der Hausmann ⚠️</td>
                                <td class="p-3 font-bold text-rose-600">die Haus<u>frau</u> ⚠️</td>
                                <td class="p-3">người nội trợ</td>
                                <td class="p-3">arbeitet <b>zu Hause</b>, kocht und kümmert sich um die Familie</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng 1.2: Nơi làm việc & Giới từ vị trí Wo? -> Dativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🏢</span> 1.2. Nơi Làm Việc (Arbeitsorte) & Giới Từ Vị Trí Ở Cách 3 (Dativ: Wo arbeiten Sie?)
                </h5>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700">
                    💡 <b>Quy tắc rút gọn giới từ:</b> <code>in + dem = im</code> (<i>im Friseursalon, im Supermarkt, im Kindergarten, im Krankenhaus, im Büro, im Restaurant, im Blumengeschäft, im Schuhgeschäft, im Sprachzentrum</i>); danh từ giống cái <code>in + der = in der</code> hoặc <code>an + einer = an einer</code> (<i>in der Schule, an der Universität, in einer Werkstatt, auf einer Baustelle, in einer Firma</i>).
                </div>
            </div>

            <!-- Bảng 1.3: Ba Mẫu câu hỏi & Trả lời nghề nghiệp -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🗣️</span> 1.3. Ba Mẫu Câu Hỏi & Ba Cách Trả Lời Nghề Nghiệp Chuẩn Ngữ Pháp
                </h5>
                <div class="p-3 rounded-xl bg-rose-50 border border-rose-200 text-xs text-rose-800">
                    ⚠️ <b>LƯU Ý CỐT LÕI:</b> Khi chỉ nói tên nghề nghiệp với cấu trúc <code>sein + [Nghề]</code> hoặc <code>arbeiten als + [Nghề]</code>, <b>không dùng mạo từ ein/eine</b>: <i>„Ich bin Lehrer.“</i> hoặc <i>„Ich arbeite als Programmierer.“</i> (Không nói: <i>„Ich bin ein Lehrer.“</i>). <b>Ngoại lệ bắt buộc:</b> Nếu có tính từ đi kèm bổ nghĩa cho nghề thì <b>phải dùng mạo từ</b>: <i>„Sie ist eine gute Ärztin.“</i>, <i>„Frau Becker ist eine erfahrene Taxifahrerin.“</i>, <i>„Anna ist eine fleißige Schülerin.“</i>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-3 text-xs sm:text-sm">
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">Cách 1: sein + [Nghề]</span>
                        <p class="text-slate-800 font-semibold">„Was sind Sie von Beruf?“</p>
                        <p class="text-emerald-700">→ „Ich bin <b>Schüler</b> / <b>Ärztin</b>.“</p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">Cách 2: sein + [Nghề] + von Beruf</span>
                        <p class="text-slate-800 font-semibold">„Was machen Sie beruflich?“</p>
                        <p class="text-emerald-700">→ „Ich bin <b>Lehrer von Beruf</b>.“</p>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 space-y-1">
                        <span class="font-bold text-indigo-700">Cách 3: arbeiten als + [Nghề]</span>
                        <p class="text-slate-800 font-semibold">„Was ist Ihr Beruf?“</p>
                        <p class="text-emerald-700">→ „Ich arbeite <b>als Florist</b>.“</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: ĐỘNG TỪ KHUYẾT THIẾU (MODALVERBEN) & CẤU TRÚC KHUNG CÂU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Động Từ Khuyết Thiếu (Modalverben) & Cấu Trúc Khung Câu (Satzklammer)</h4>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm text-amber-900 space-y-2">
                <p class="font-bold flex items-center gap-2"><span>🔑</span> 2 Đặc Điểm Ngữ Pháp Cốt Lõi:</p>
                <ol class="list-decimal pl-5 space-y-1 text-slate-700">
                    <li><b>Đổi nguyên âm ở số ít (ich, du, er/sie/es):</b> <i>müssen → muss-</i>, <i>können → kann-</i>, <i>wollen → will-</i>, <i>dürfen → darf-</i>. Riêng <i>sollen</i> giữ nguyên o.</li>
                    <li><b>Ngôi thứ 1 (ich) và Ngôi thứ 3 số ít (er/sie/es) GIỐNG HỆT NHAU VÀ KHÔNG CÓ ĐUÔI -e hay -t:</b> <i>ich muss = er muss</i>; <i>ich kann = er kann</i>; <i>ich will = er will</i>; <i>ich darf = er darf</i>; <i>ich soll = er soll</i>; <i>ich möchte = er möchte</i>.</li>
                </ol>
            </div>

            <!-- Bảng ma trận 6 Modalverben -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📊</span> 2.1. Ma Trận Chia Đầy Đủ 6 Động Từ Khuyết Thiếu Theo 9 Ngôi
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-center text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3 text-left">Ngôi nhân xưng</th>
                                <th class="p-3 bg-indigo-50/50 text-indigo-900">1. möchten<br><span class="text-xs font-normal text-slate-500">(muốn - lịch sự)</span></th>
                                <th class="p-3 bg-amber-50/50 text-amber-900">2. müssen<br><span class="text-xs font-normal text-slate-500">(phải, bắt buộc)</span></th>
                                <th class="p-3 bg-emerald-50/50 text-emerald-900">3. können<br><span class="text-xs font-normal text-slate-500">(có thể, biết làm)</span></th>
                                <th class="p-3">4. wollen<br><span class="text-xs font-normal text-slate-500">(muốn - ý chí)</span></th>
                                <th class="p-3">5. dürfen<br><span class="text-xs font-normal text-slate-500">(được phép)</span></th>
                                <th class="p-3">6. sollen<br><span class="text-xs font-normal text-slate-500">(nên, bổn phận)</span></th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 text-left font-bold">ich</td>
                                <td class="p-3 font-black text-rose-700 bg-rose-50/30">möchte</td>
                                <td class="p-3 font-black text-amber-700 bg-amber-50/30">muss</td>
                                <td class="p-3 font-black text-emerald-700 bg-emerald-50/30">kann</td>
                                <td class="p-3 font-bold text-slate-900">will</td>
                                <td class="p-3 font-bold text-slate-900">darf</td>
                                <td class="p-3 font-bold text-slate-900">soll</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 text-left font-bold">du</td>
                                <td class="p-3">möchtest</td>
                                <td class="p-3 font-semibold text-amber-800">musst</td>
                                <td class="p-3 font-semibold text-emerald-800">kannst</td>
                                <td class="p-3">willst</td>
                                <td class="p-3">darfst</td>
                                <td class="p-3">sollst</td>
                            </tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/20">
                                <td class="p-3 text-left font-bold text-rose-600">er / sie / es ⚠️</td>
                                <td class="p-3 font-black text-rose-700 bg-rose-50/50">möchte ⚠️</td>
                                <td class="p-3 font-black text-amber-700 bg-amber-50/50">muss ⚠️</td>
                                <td class="p-3 font-black text-emerald-700 bg-emerald-50/50">kann ⚠️</td>
                                <td class="p-3 font-black text-slate-900">will ⚠️</td>
                                <td class="p-3 font-black text-slate-900">darf ⚠️</td>
                                <td class="p-3 font-black text-slate-900">soll ⚠️</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 text-left font-bold">wir</td>
                                <td class="p-3">möchten</td>
                                <td class="p-3">müssen</td>
                                <td class="p-3">können</td>
                                <td class="p-3">wollen</td>
                                <td class="p-3">dürfen</td>
                                <td class="p-3">sollen</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 text-left font-bold">ihr</td>
                                <td class="p-3">möchtet</td>
                                <td class="p-3 font-semibold text-amber-800">müsst</td>
                                <td class="p-3 font-semibold text-emerald-800">könnt</td>
                                <td class="p-3">wollt</td>
                                <td class="p-3">dürft</td>
                                <td class="p-3">sollt</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 text-left font-bold">sie / Sie</td>
                                <td class="p-3">möchten</td>
                                <td class="p-3">müssen</td>
                                <td class="p-3">können</td>
                                <td class="p-3">wollen</td>
                                <td class="p-3">dürfen</td>
                                <td class="p-3">sollen</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Cấu trúc Satzklammer & Động từ tách -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📐</span> 2.2. Cấu Trúc Khung Câu (Satzklammer) & Quy Tắc Vàng Với Động Từ Tách
                </h5>
                <div class="p-4 rounded-2xl bg-indigo-50 border border-indigo-200 text-xs sm:text-sm text-indigo-950 font-mono text-center">
                    [Vị trí 1: Chủ ngữ/Thời gian] + <b>[Vị trí 2: MODALVERB chia]</b> + [Thành phần giữa câu] + <b>[CUỐI CÂU: ĐỘNG TỪ NGUYÊN MẪU (Infinitiv)]</b>
                </div>
                <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-xs text-amber-900 space-y-1">
                    <p class="font-bold">⭐ QUY TẮC VÀNG VỚI ĐỘNG TỪ TÁCH (Trennbare Verben):</p>
                    <p class="text-slate-700">Khi trong câu <b>CÓ MẶT MODALVERB</b>, động từ tách <b>KHÔNG ĐƯỢC TÁCH NỮA</b> mà gộp liền lại thành dạng nguyên mẫu ở cuối câu:</p>
                    <ul class="list-disc pl-5 space-y-0.5 text-slate-700">
                        <li>Không có Modalverb: <i>Paula <b>steht</b> um 6.15 Uhr <b>auf</b>.</i> / <i>Sie <b>holt</b> die Tochter <b>ab</b>.</i></li>
                        <li>Có Modalverb: <i>Um 6.15 Uhr <b>muss</b> Paula <b><u>aufstehen</u></b>.</i> / <i>Sie <b>muss</b> die Tochter <b><u>abholen</u></b>.</i></li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: MA TRẬN TỪ HẠN ĐỊNH Ở CÁCH 4 (AKKUSATIV) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Hệ Thống Ma Trận Từ Hạn Định Ở Cách 4 (Artikelwörter im Akkusativ)</h4>
            </div>

            <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 text-xs sm:text-sm text-purple-950 space-y-1">
                <p class="font-bold">⚡ Quy tắc bất biến của Cách 4 (Akkusativ):</p>
                <p>Chỉ duy nhất <b>Giống đực (Maskulinum - der)</b> đổi đuôi sang <b>-en</b> (<i>den / einen / keinen / meinen, seinen, euren...</i>). Các giống còn lại: <b>Giống cái (die)</b>, <b>Giống trung (das)</b> và <b>Số nhiều (die)</b> <b>GIỮ NGUYÊN 100%</b> giống như Cách 1 (Nominativ)!</p>
            </div>

            <!-- Bảng ma trận 9 ngôi sở hữu Akkusativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>👑</span> 3.1. Bảng Ma Trận Mạo Từ Sở Hữu Ở Cách 4 (Possessivartikel im Akkusativ)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-center text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3 text-left">Ngôi Nhân Xưng</th>
                                <th class="p-3 text-left">Gốc Sở Hữu</th>
                                <th class="p-3 text-amber-700 bg-amber-50">Giống Đực (m) ⚠️<br><span class="text-xs font-normal">Computer (+ -en)</span></th>
                                <th class="p-3 text-rose-700">Giống Cái (f)<br><span class="text-xs font-normal">Tochter (+ -e)</span></th>
                                <th class="p-3 text-emerald-700">Giống Trung (n)<br><span class="text-xs font-normal">Auto (giữ nguyên)</span></th>
                                <th class="p-3 text-purple-700">Số Nhiều (Pl)<br><span class="text-xs font-normal">Kunden (+ -e)</span></th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">1. ich</td><td class="p-3 text-left">mein-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">mein<u>en</u></td><td class="p-3">meine</td><td class="p-3">mein</td><td class="p-3">meine</td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">2. du</td><td class="p-3 text-left">dein-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">dein<u>en</u></td><td class="p-3">deine</td><td class="p-3">dein</td><td class="p-3">deine</td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">3. er / es</td><td class="p-3 text-left">sein-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">sein<u>en</u></td><td class="p-3">seine</td><td class="p-3">sein</td><td class="p-3">seine</td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">4. sie (cô ấy)</td><td class="p-3 text-left">ihr-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">ihr<u>en</u></td><td class="p-3">ihre</td><td class="p-3">ihr</td><td class="p-3">ihre</td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">5. wir</td><td class="p-3 text-left">unser-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">unser<u>en</u></td><td class="p-3">unsere</td><td class="p-3">unser</td><td class="p-3">unsere</td></tr>
                            <tr class="hover:bg-slate-50 bg-amber-50/20"><td class="p-3 text-left font-bold text-rose-600">6. ihr (các bạn) ⚠️</td><td class="p-3 text-left font-bold">euer-</td><td class="p-3 font-black text-amber-700 bg-amber-100/60">eur<u>en</u> ⚠️</td><td class="p-3 font-bold">eure</td><td class="p-3 font-bold">euer</td><td class="p-3 font-bold">eure</td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">7. sie (họ)</td><td class="p-3 text-left">ihr-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">ihr<u>en</u></td><td class="p-3">ihre</td><td class="p-3">ihr</td><td class="p-3">ihre</td></tr>
                            <tr class="hover:bg-slate-50"><td class="p-3 text-left font-bold">8. Sie (Ngài)</td><td class="p-3 text-left">Ihr-</td><td class="p-3 font-bold text-amber-700 bg-amber-50/50">Ihr<u>en</u></td><td class="p-3">Ihre</td><td class="p-3">Ihr</td><td class="p-3">Ihre</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: CHUYÊN ĐỀ ĐẶC BIỆT: PHÂN BIỆT TOÀN DIỆN AKKUSATIV VS. DATIV -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-rose-100 text-rose-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Cẩm Nang Chuyên Sâu: Phân Biệt Toàn Diện Cách 4 (Akkusativ) vs. Cách 3 (Dativ)</h4>
            </div>

            <!-- Tiêu chí 1: Động từ & vai trò -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📌</span> TIÊU CHÍ 1: Phân Biệt Theo Động Từ & Vai Trò Tân Ngữ (Wen/Was? vs. Wem?)
                </h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                    <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-2">
                        <span class="font-bold text-blue-900 block text-sm">CÁCH 4: AKKUSATIV (Tân ngữ trực tiếp)</span>
                        <p class="text-slate-700">• Trả lời câu hỏi: <b>Wen?</b> (Ai - cho người) / <b>Was?</b> (Cái gì - cho vật).</p>
                        <p class="text-slate-700">• <b>Động từ điển hình:</b> <i>haben, brauchen, suchen, finden, kaufen, reparieren, schreiben, lesen, untersuchen, anrufen, abholen</i> (90% động từ tiếng Đức!).</p>
                        <p class="text-emerald-800 font-semibold">• Ví dụ: <i>„Petra braucht <b><u>einen</u> Computer</b>.“</i> / <i>„Der Arzt untersucht <b><u>den</u> Patienten</b>.“</i></p>
                    </div>
                    <div class="p-4 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-2">
                        <span class="font-bold text-amber-900 block text-sm">CÁCH 3: DATIV (Tân ngữ gián tiếp)</span>
                        <p class="text-slate-700">• Trả lời câu hỏi: <b>Wem?</b> (Cho ai? / Đối với ai?).</p>
                        <p class="text-slate-700">• <b>Động từ quy định Dativ:</b> <i>helfen (giúp đỡ), danken (cảm ơn), gefallen (làm ai thích), gehören (thuộc về ai), antworten (trả lời)</i>.</p>
                        <p class="text-amber-900 font-semibold">• Ví dụ: <i>„Der Krankenpfleger hilft <b><u>dem</u> Arzt</b>.“</i> / <i>„Das Auto gehört <b><u>meinem</u> Bruder</b>.“</i></p>
                    </div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-700">
                    💡 <b>Trường hợp câu có CẢ 2 TÂN NGỮ:</b> Người nhận (<i>Wem?</i>) chia ở <b>Dativ</b>, Vật được trao/tặng/mua (<i>Was?</i>) chia ở <b>Akkusativ</b>: <i>„Der Chef gibt <b><u>der</u> Sekretärin</b> (Dativ) <b><u>einen</u> neuen Laptop</b> (Akkusativ).“</i>
                </div>
            </div>

            <!-- Tiêu chí 2: Giới từ cố định -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📌</span> TIÊU CHÍ 2: Phân Biệt Theo Nhóm Giới Từ Cố Định
                </h5>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="font-bold text-indigo-700">LUÔN ĐI VỚI AKKUSATIV (FUDGE-BO):</span>
                        <p class="text-slate-700"><b>F</b>ür (cho), <b>U</b>m (vào lúc/xung quanh), <b>D</b>urch (xuyên qua), <b>G</b>egen (khoảng/chống lại), <b>E</b>ntlang (dọc theo), <b>B</b>is (cho đến), <b>O</b>hne (không có).</p>
                        <p class="text-emerald-700"><i>„Das Telefon ist wichtig <b>für <u>sie</u></b> / <b>für <u>den</u> Chef</b>.“</i></p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="font-bold text-indigo-700">LUÔN ĐI VỚI DATIV:</span>
                        <p class="text-slate-700"><b>mit</b> (cùng/bằng), <b>nach</b> (sau khi/đến), <b>aus</b> (ra từ), <b>zu</b> (đến), <b>von</b> (từ/của), <b>bei</b> (tại/trong lúc), <b>seit</b> (từ khi).</p>
                        <p class="text-amber-800"><i>„<b>Bei <u>ihrer</u> Arbeit</b> braucht Petra einen Laptop.“</i> / <i>„<b>mit <u>dem</u> Bus</b>“</i></p>
                    </div>
                </div>
            </div>

            <!-- Tiêu chí 3: Wohin? Akkusativ vs. Wo? Dativ -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📌</span> TIÊU CHÍ 3: Sự Di Chuyển (Wohin? → Akkusativ) vs. Vị Trí Tĩnh (Wo? → Dativ)
                </h5>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Địa điểm</th>
                                <th class="p-3 text-indigo-800 bg-indigo-50/50">Di chuyển Wohin? (+ AKKUSATIV)</th>
                                <th class="p-3 text-amber-800 bg-amber-50/50">Vị trí tĩnh Wo? (+ DATIV)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold">der Kindergarten</td>
                                <td class="p-3 text-indigo-700">bringt die Tochter <b>in <u>den</u> Kindergarten</b></td>
                                <td class="p-3 text-amber-700">spielt <b><u>im</u> Kindergarten</b> (in dem)</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold">die Werkstatt</td>
                                <td class="p-3 text-indigo-700">bringt das Auto <b>in <u>die</u> Werkstatt</b></td>
                                <td class="p-3 text-amber-700">repariert das Auto <b>in <u>der</u> Werkstatt</b></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold">das Bett</td>
                                <td class="p-3 text-indigo-700">bringt das Kind <b><u>ins</u> Bett</b> (in das)</td>
                                <td class="p-3 text-amber-700">schläft <b><u>im</u> Bett</b> (in dem)</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold">das Büro</td>
                                <td class="p-3 text-indigo-700">geht um 8 Uhr <b><u>ins</u> Büro</b> (in das)</td>
                                <td class="p-3 text-amber-700">arbeitet allein <b><u>im</u> Büro</b> (in dem)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 5: PHÂN TÍCH 3 ĐOẠN VĂN MẪU (TEXTANALYSE & PRAXIS) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Phân Tích 3 Đoạn Văn Mẫu Thực Chiến (Kèm Audio Phát Âm Chuẩn)</h4>
            </div>

            <!-- Đoạn 1: Paula Rausch -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                    <span class="font-bold text-slate-900">1. Lập trình viên Paula Rausch (35 tuổi) — Modalverben & Động từ tách</span>
                    <button type="button" onclick="speakGerman('Paula Rausch ist 35 Jahre alt. Sie arbeitet als Programmiererin. Um 6.15 Uhr muss sie aufstehen. Um 7.15 Uhr muss sie mit dem Bus zur Arbeit fahren. Von 7.30 bis 15 Uhr arbeitet sie. Um 16.30 Uhr muss sie ihre Tochter vom Kindergarten abholen. Um 18.30 Uhr macht sie das Abendessen. Von 20 bis 22 Uhr kann sie fernsehen.')" class="px-3 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold text-xs hover:bg-indigo-100 transition-colors">🔊 Nghe đoạn văn</button>
                </div>
                <p class="text-xs sm:text-sm text-slate-700 italic">
                    „Paula Rausch ist 35 Jahre alt. Sie arbeitet <b>als Programmiererin</b>. Um 6.15 Uhr <b>muss</b> sie <b>aufstehen</b>. Um 7.15 Uhr <b>muss</b> sie <b>mit dem Bus zur Arbeit fahren</b>. Von 7.30 bis 15 Uhr <b>arbeitet</b> sie. Um 16.30 Uhr <b>muss</b> sie <b>ihre Tochter vom Kindergarten abholen</b>. Um 18.30 Uhr <b>macht</b> sie <b>das Abendessen</b>. Von 20 bis 22 Uhr <b>kann</b> sie <b>fernsehen</b>.“
                </p>
                <p class="text-xs text-slate-500">
                    <b>Dịch nghĩa:</b> Paula Rausch 35 tuổi. Cô ấy làm nghề lập trình viên. Lúc 6:15 cô ấy phải thức dậy. Lúc 7:15 cô ấy phải đi xe buýt đến chỗ làm. Từ 7:30 đến 15:00 cô ấy làm việc. Lúc 16:30 cô ấy phải đón con gái từ trường mẫu giáo. Lúc 18:30 cô ấy làm bữa tối. Từ 20:00 đến 22:00 cô ấy có thể xem tivi.
                </p>
            </div>

            <!-- Đoạn 2: Frank Müller -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                    <span class="font-bold text-slate-900">2. Thầy giáo Frank Müller (36 tuổi) — Modalverben & Wohin? Akkusativ vs. Dativ</span>
                    <button type="button" onclick="speakGerman('Frank Müller ist 36 Jahre alt. Er ist Lehrer von Beruf. Er hat Ferien. Bis 7 Uhr kann er schlafen. Um 8.30 Uhr muss er die Tochter in den Kindergarten bringen. Um 12.30 Uhr bringt er das Auto in die Werkstatt. Von 17 bis 18.30 Uhr geht er zum Fußballtraining. Um 19 Uhr bringt er die Tochter ins Bett.')" class="px-3 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold text-xs hover:bg-indigo-100 transition-colors">🔊 Nghe đoạn văn</button>
                </div>
                <p class="text-xs sm:text-sm text-slate-700 italic">
                    „Frank Müller ist 36 Jahre alt. Er ist <b>Lehrer von Beruf</b>. Er hat Ferien. Bis 7 Uhr <b>kann</b> er <b>schlafen</b>. Um 8.30 Uhr <b>muss</b> er <b>die Tochter in den Kindergarten bringen</b>. Um 12.30 Uhr <b>bringt</b> er <b>das Auto in die Werkstatt</b>. Von 17 bis 18.30 Uhr <b>geht</b> er <b>zum Fußballtraining</b>. Um 19 Uhr <b>bringt</b> er <b>die Tochter ins Bett</b>.“
                </p>
                <p class="text-xs text-slate-500">
                    <b>Dịch nghĩa:</b> Frank Müller 36 tuổi. Nghề nghiệp của anh ấy là giáo viên. Anh ấy đang có kỳ nghỉ. Anh ấy có thể ngủ đến 7 giờ. Lúc 8:30 anh ấy phải đưa con gái vào trường mẫu giáo. Lúc 12:30 anh ấy mang chiếc xe vào xưởng sửa chữa. Từ 17:00 đến 18:30 anh ấy đi đến buổi tập bóng đá. Lúc 19:00 anh ấy đưa con gái lên giường đi ngủ.
                </p>
            </div>

            <!-- Đoạn 3: Petra May -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                <div class="flex items-center justify-between">
                    <span class="font-bold text-slate-900">3. Nhân viên văn phòng Petra May — Từ hạn định Nominativ, Akkusativ & Dativ</span>
                    <button type="button" onclick="speakGerman('Das ist Petra May. Bei ihrer Arbeit braucht sie einen Computer und einen großen Schreibtisch. Sie schreibt Computerprogramme. Das Telefon ist wichtig für sie. Sie muss ihre Kunden oft anrufen. Sie arbeitet allein im Büro.')" class="px-3 py-1 rounded-lg bg-indigo-50 text-indigo-700 font-bold text-xs hover:bg-indigo-100 transition-colors">🔊 Nghe đoạn văn</button>
                </div>
                <p class="text-xs sm:text-sm text-slate-700 italic">
                    „Das ist Petra May. <b>Bei ihrer Arbeit</b> braucht sie <b>einen Computer</b> und <b>einen großen Schreibtisch</b>. Sie schreibt Computerprogramme. <b>Das Telefon</b> ist wichtig <b>für sie</b>. Sie <b>muss ihre Kunden</b> oft <b>anrufen</b>. Sie arbeitet allein <b>im Büro</b>.“
                </p>
                <p class="text-xs text-slate-500">
                    <b>Dịch nghĩa:</b> Đây là Petra May. Trong công việc của mình, cô ấy cần một chiếc máy tính và một cái bàn làm việc lớn. Cô ấy viết các chương trình máy tính. Chiếc điện thoại rất quan trọng đối với cô ấy. Cô ấy thường xuyên phải gọi điện cho các khách hàng của mình. Cô ấy làm việc một mình ở trong văn phòng.
                </p>
            </div>
        </div>
    </div>
    """

    if existing_lesson:
        cursor.execute("""
            UPDATE lessons SET title = ?, grammar_content = ? WHERE id = ?;
        """, (lesson_title, grammar_html, lesson_id))
    else:
        cursor.execute("""
            INSERT INTO lessons (id, level_id, title, grammar_content)
            VALUES (?, ?, ?, ?);
        """, (lesson_id, a1_id, lesson_title, grammar_html))

    # =========================================================================
    # DANH MỤC 50 TỪ VỰNG TRỌNG TÂM BÀI 7 (KHỚP 100% VỚI LEXIKON_DB.JS)
    # =========================================================================
    vocab_raw = [
        {
                "word": "Programmierer",
                "article": "der",
                "gender": "der",
                "plural": "die Programmierer",
                "indefinite": "ein Programmierer",
                "negation": "kein Programmierer",
                "akkusativ": "den / einen / keinen Programmierer",
                "meaning": "nam lập trình viên",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Programmierer). Số nhiều giữ nguyên die Programmierer.",
                "example": "Paula Rausch arbeitet mit einem Programmierer im Büro zusammen.",
                "example_vi": "Paula Rausch làm việc cùng một nam lập trình viên ở văn phòng."
        },
        {
                "word": "Programmiererin",
                "article": "die",
                "gender": "die",
                "plural": "die Programmiererinnen",
                "indefinite": "eine Programmiererin",
                "negation": "keine Programmiererin",
                "akkusativ": "die / eine / keine Programmiererin",
                "meaning": "nữ lập trình viên",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái kết thúc bằng -in. Số nhiều gấp đôi -nn thành die Programmiererinnen.",
                "example": "Paula Rausch ist 35 Jahre alt und arbeitet als Programmiererin.",
                "example_vi": "Paula Rausch 35 tuổi và làm nghề nữ lập trình viên."
        },
        {
                "word": "Taxifahrer",
                "article": "der",
                "gender": "der",
                "plural": "die Taxifahrer",
                "indefinite": "ein Taxifahrer",
                "negation": "kein Taxifahrer",
                "akkusativ": "den / einen / keinen Taxifahrer",
                "meaning": "nam tài xế taxi",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Taxifahrer). Nghề nghiệp nói sein + Taxifahrer hoặc arbeiten als Taxifahrer.",
                "example": "Mein Onkel arbeitet seit fünf Jahren als Taxifahrer in Hamburg.",
                "example_vi": "Chú tôi làm nghề tài xế taxi ở Hamburg từ 5 năm nay."
        },
        {
                "word": "Taxifahrerin",
                "article": "die",
                "gender": "die",
                "plural": "die Taxifahrerinnen",
                "indefinite": "eine Taxifahrerin",
                "negation": "keine Taxifahrerin",
                "akkusativ": "die / eine / keine Taxifahrerin",
                "meaning": "nữ tài xế taxi",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái. Số nhiều thêm -nen: die Taxifahrerinnen.",
                "example": "Frau Becker ist eine erfahrene Taxifahrerin in Berlin.",
                "example_vi": "Bà Becker là một nữ tài xế taxi giàu kinh nghiệm ở Berlin."
        },
        {
                "word": "Krankenpfleger",
                "article": "der",
                "gender": "der",
                "plural": "die Krankenpfleger",
                "indefinite": "ein Krankenpfleger",
                "negation": "kein Krankenpfleger",
                "akkusativ": "den / einen / keinen Krankenpfleger",
                "meaning": "nam điều dưỡng / y tá",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực chỉ nam y tá, chăm sóc bệnh nhân trong bệnh viện.",
                "example": "Der Krankenpfleger hilft dem Arzt jeden Tag im Krankenhaus.",
                "example_vi": "Người nam điều dưỡng giúp đỡ bác sĩ mỗi ngày ở bệnh viện."
        },
        {
                "word": "Krankenpflegerin",
                "article": "die",
                "gender": "die",
                "plural": "die Krankenpflegerinnen",
                "indefinite": "eine Krankenpflegerin",
                "negation": "keine Krankenpflegerin",
                "akkusativ": "die / eine / keine Krankenpflegerin",
                "meaning": "nữ điều dưỡng / y tá",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái chỉ nữ y tá (hoặc die Krankenschwester).",
                "example": "Meine Tante arbeitet als Krankenpflegerin auf der Station.",
                "example_vi": "Dì tôi làm nghề nữ điều dưỡng ở khoa điều trị."
        },
        {
                "word": "Florist",
                "article": "der",
                "gender": "der",
                "plural": "die Floristen",
                "indefinite": "ein Florist",
                "negation": "kein Florist",
                "akkusativ": "den / einen / keinen Florist",
                "meaning": "nam nhân viên bán hoa / cắm hoa",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực thuộc nhóm N-Deklination: số nhiều die Floristen.",
                "example": "Der Florist bindet wunderschöne Blumen für die Hochzeit.",
                "example_vi": "Người nam thợ hoa bó những bông hoa tuyệt đẹp cho đám cưới."
        },
        {
                "word": "Floristin",
                "article": "die",
                "gender": "die",
                "plural": "die Floristinnen",
                "indefinite": "eine Floristin",
                "negation": "keine Floristin",
                "akkusativ": "die / eine / keine Floristin",
                "meaning": "nữ nhân viên bán hoa",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Floristin). Nơi làm việc im Blumengeschäft.",
                "example": "Die Floristin verkauft schöne Blumen im Blumengeschäft.",
                "example_vi": "Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa."
        },
        {
                "word": "Verkäufer",
                "article": "der",
                "gender": "der",
                "plural": "die Verkäufer",
                "indefinite": "ein Verkäufer",
                "negation": "kein Verkäufer",
                "akkusativ": "den / einen / keinen Verkäufer",
                "meaning": "nam nhân viên bán hàng",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực. Bán hàng trong siêu thị hoặc cửa hàng.",
                "example": "Der Verkäufer berät die Kunden freundlich im Supermarkt.",
                "example_vi": "Nam nhân viên bán hàng tư vấn khách hàng thân thiện ở siêu thị."
        },
        {
                "word": "Verkäuferin",
                "article": "die",
                "gender": "die",
                "plural": "die Verkäuferinnen",
                "indefinite": "eine Verkäuferin",
                "negation": "keine Verkäuferin",
                "akkusativ": "die / eine / keine Verkäuferin",
                "meaning": "nữ nhân viên bán hàng",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Verkäuferin). Số nhiều die Verkäuferinnen.",
                "example": "Die Verkäuferin verkauft moderne Schuhe im Schuhgeschäft.",
                "example_vi": "Nữ nhân viên bán hàng bán những đôi giày hiện đại ở trong cửa hàng giày."
        },
        {
                "word": "Mechatroniker",
                "article": "der",
                "gender": "der",
                "plural": "die Mechatroniker",
                "indefinite": "ein Mechatroniker",
                "negation": "kein Mechatroniker",
                "akkusativ": "den / einen / keinen Mechatroniker",
                "meaning": "nam thợ cơ khí ô tô",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Thợ cơ khí điện tử ô tô (KFZ-Mechatroniker), làm việc in einer Werkstatt.",
                "example": "Der Mechatroniker repariert das Auto in einer Werkstatt.",
                "example_vi": "Người thợ cơ khí sửa chiếc ô tô ở trong một xưởng sửa chữa."
        },
        {
                "word": "Mechatronikerin",
                "article": "die",
                "gender": "die",
                "plural": "die Mechatronikerinnen",
                "indefinite": "eine Mechatronikerin",
                "negation": "keine Mechatronikerin",
                "akkusativ": "die / eine / keine Mechatronikerin",
                "meaning": "nữ thợ cơ khí ô tô",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Nữ thợ cơ khí ô tô (KFZ-Mechatronikerin).",
                "example": "Sie lernt fleißig und möchte Mechatronikerin werden.",
                "example_vi": "Cô ấy học tập chăm chỉ và muốn trở thành nữ thợ cơ khí."
        },
        {
                "word": "Trainer",
                "article": "der",
                "gender": "der",
                "plural": "die Trainer",
                "indefinite": "ein Trainer",
                "negation": "kein Trainer",
                "akkusativ": "den / einen / keinen Trainer",
                "meaning": "nam huấn luyện viên",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Trainer), làm việc im Fitnessstudio hoặc im Stadion.",
                "example": "Der Trainer leitet das Training im Fitnessstudio.",
                "example_vi": "Huấn luyện viên phụ trách buổi tập ở phòng gym."
        },
        {
                "word": "Trainerin",
                "article": "die",
                "gender": "die",
                "plural": "die Trainerinnen",
                "indefinite": "eine Trainerin",
                "negation": "keine Trainerin",
                "akkusativ": "die / eine / keine Trainerin",
                "meaning": "nữ huấn luyện viên",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Trainerin), số nhiều die Trainerinnen.",
                "example": "Unsere Trainerin hilft den Sportlern jeden Tag im Stadion.",
                "example_vi": "Nữ huấn luyện viên của chúng tôi giúp đỡ các vận động viên mỗi ngày ở sân vận động."
        },
        {
                "word": "Lehrer",
                "article": "der",
                "gender": "der",
                "plural": "die Lehrer",
                "indefinite": "ein Lehrer",
                "negation": "kein Lehrer",
                "akkusativ": "den / einen / keinen Lehrer",
                "meaning": "nam giáo viên",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Lehrer). Cấu trúc Er ist Lehrer von Beruf không dùng mạo từ.",
                "example": "Frank Müller ist Lehrer von Beruf und hat jetzt Ferien.",
                "example_vi": "Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ."
        },
        {
                "word": "Lehrerin",
                "article": "die",
                "gender": "die",
                "plural": "die Lehrerinnen",
                "indefinite": "eine Lehrerin",
                "negation": "keine Lehrerin",
                "akkusativ": "die / eine / keine Lehrerin",
                "meaning": "nữ giáo viên",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Lehrerin). Giảng dạy ở trường: an einer Schule unterrichten.",
                "example": "Die Lehrerin unterrichtet Schüler an einer Schule in Berlin.",
                "example_vi": "Nữ giáo viên giảng dạy học sinh tại một trường học ở Berlin."
        },
        {
                "word": "Schüler",
                "article": "der",
                "gender": "der",
                "plural": "die Schüler",
                "indefinite": "ein Schüler",
                "negation": "kein Schüler",
                "akkusativ": "den / einen / keinen Schüler",
                "meaning": "nam học sinh (phổ thông)",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Schüler), học sinh cấp 1 đến cấp 3.",
                "example": "Der Schüler lernt viele Fächer in der Schule.",
                "example_vi": "Cậu học sinh học nhiều môn học ở trường."
        },
        {
                "word": "Schülerin",
                "article": "die",
                "gender": "die",
                "plural": "die Schülerinnen",
                "indefinite": "eine Schülerin",
                "negation": "keine Schülerin",
                "akkusativ": "die / eine / keine Schülerin",
                "meaning": "nữ học sinh (phổ thông)",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Schülerin), số nhiều die Schülerinnen.",
                "example": "Anna ist eine fleißige Schülerin am Gymnasium.",
                "example_vi": "Anna là một nữ học sinh chăm chỉ tại trường THPT (Gymnasium)."
        },
        {
                "word": "Student",
                "article": "der",
                "gender": "der",
                "plural": "die Studenten",
                "indefinite": "ein Student",
                "negation": "kein Student",
                "akkusativ": "den / einen / keinen Student",
                "meaning": "nam sinh viên (đại học)",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực nhóm N-Deklination: der Student, des Studenten, die Studenten.",
                "example": "Der Student studiert Informatik an der Universität.",
                "example_vi": "Nam sinh viên học ngành công nghệ thông tin tại trường đại học."
        },
        {
                "word": "Studentin",
                "article": "die",
                "gender": "die",
                "plural": "die Studentinnen",
                "indefinite": "eine Studentin",
                "negation": "keine Studentin",
                "akkusativ": "die / eine / keine Studentin",
                "meaning": "nữ sinh viên (đại học)",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Studentin). Học đại học: an der Universität studieren.",
                "example": "Die Studentin liest viele deutsche Fachbücher in der Bibliothek.",
                "example_vi": "Nữ sinh viên đọc nhiều sách chuyên ngành tiếng Đức trong thư viện."
        },
        {
                "word": "Sekretär",
                "article": "der",
                "gender": "der",
                "plural": "die Sekretäre",
                "indefinite": "ein Sekretär",
                "negation": "kein Sekretär",
                "akkusativ": "den / einen / keinen Sekretär",
                "meaning": "nam thư ký",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Sekretär), số nhiều die Sekretäre.",
                "example": "Der Sekretär vereinbart wichtige Termine mit Kunden.",
                "example_vi": "Nam thư ký sắp xếp các cuộc hẹn quan trọng với khách hàng."
        },
        {
                "word": "Sekretärin",
                "article": "die",
                "gender": "die",
                "plural": "die Sekretärinnen",
                "indefinite": "eine Sekretärin",
                "negation": "keine Sekretärin",
                "akkusativ": "die / eine / keine Sekretärin",
                "meaning": "nữ thư ký",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Sekretärin). Viết email và gọi điện: E-Mails schreiben und Kunden anrufen.",
                "example": "Die Sekretärin schreibt E-Mails und ruft Kunden im Büro an.",
                "example_vi": "Nữ thư ký viết email và gọi điện cho khách hàng ở văn phòng."
        },
        {
                "word": "Friseur",
                "article": "der",
                "gender": "der",
                "plural": "die Friseure",
                "indefinite": "ein Friseur",
                "negation": "kein Friseur",
                "akkusativ": "den / einen / keinen Friseur",
                "meaning": "nam thợ cắt tóc",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Friseur). Nơi làm việc im Friseursalon.",
                "example": "Der Friseur schneidet meinem Bruder im Friseursalon die Haare.",
                "example_vi": "Người thợ làm tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc."
        },
        {
                "word": "Friseurin",
                "article": "die",
                "gender": "die",
                "plural": "die Friseurinnen",
                "indefinite": "eine Friseurin",
                "negation": "keine Friseurin",
                "akkusativ": "die / eine / keine Friseurin",
                "meaning": "nữ thợ làm tóc",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Friseurin), số nhiều die Friseurinnen.",
                "example": "Die Friseurin macht eine sehr schöne moderne Frisur.",
                "example_vi": "Nữ thợ làm tóc làm một kiểu tóc hiện đại rất đẹp."
        },
        {
                "word": "Kellner",
                "article": "der",
                "gender": "der",
                "plural": "die Kellner",
                "indefinite": "ein Kellner",
                "negation": "kein Kellner",
                "akkusativ": "den / einen / keinen Kellner",
                "meaning": "nam nhân viên phục vụ bàn",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Kellner). Phục vụ thực khách im Restaurant.",
                "example": "Der Kellner bringt den Gästen das Essen im Restaurant.",
                "example_vi": "Người bồi bàn mang thức ăn cho thực khách ở nhà hàng."
        },
        {
                "word": "Kellnerin",
                "article": "die",
                "gender": "die",
                "plural": "die Kellnerinnen",
                "indefinite": "eine Kellnerin",
                "negation": "keine Kellnerin",
                "akkusativ": "die / eine / keine Kellnerin",
                "meaning": "nữ nhân viên phục vụ bàn",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái (die Kellnerin), số nhiều die Kellnerinnen.",
                "example": "Die Kellnerin bedient Gäste freundlich im Café.",
                "example_vi": "Nữ phục vụ bàn phục vụ thực khách thân thiện ở quán cà phê."
        },
        {
                "word": "Koch",
                "article": "der",
                "gender": "der",
                "plural": "die Köche",
                "indefinite": "ein Koch",
                "negation": "kein Koch",
                "akkusativ": "den / einen / keinen Koch",
                "meaning": "nam đầu bếp",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực đặc biệt: số nhiều đổi biến âm die Köche.",
                "example": "Der Koch bereitet köstliche Gerichte in der Küche zu.",
                "example_vi": "Người đầu bếp chuẩn bị những món ăn ngon tuyệt trong nhà bếp."
        },
        {
                "word": "Köchin",
                "article": "die",
                "gender": "die",
                "plural": "die Köchinnen",
                "indefinite": "eine Köchin",
                "negation": "keine Köchin",
                "akkusativ": "die / eine / keine Köchin",
                "meaning": "nữ đầu bếp",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái đặc biệt: thêm Umlaut ö và đuôi -in thành die Köchin.",
                "example": "Frau Bui ist eine talentierte Köchin in einem Restaurant.",
                "example_vi": "Bà Bùi là một nữ đầu bếp tài năng trong một nhà hàng."
        },
        {
                "word": "Arzt",
                "article": "der",
                "gender": "der",
                "plural": "die Ärzte",
                "indefinite": "ein Arzt",
                "negation": "kein Arzt",
                "akkusativ": "den / einen / keinen Arzt",
                "meaning": "nam bác sĩ",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực đặc biệt: số nhiều thêm Umlaut die Ärzte.",
                "example": "Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus.",
                "example_vi": "Bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện."
        },
        {
                "word": "Ärztin",
                "article": "die",
                "gender": "die",
                "plural": "die Ärztinnen",
                "indefinite": "eine Ärztin",
                "negation": "keine Ärztin",
                "akkusativ": "die / eine / keine Ärztin",
                "meaning": "nữ bác sĩ",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái đặc biệt: thêm Umlaut ä và đuôi -in thành die Ärztin.",
                "example": "Die Ärztin hilft kranken Menschen mit großer Geduld.",
                "example_vi": "Nữ bác sĩ giúp đỡ những người bệnh bằng sự kiên nhẫn to lớn."
        },
        {
                "word": "Hausmann",
                "article": "der",
                "gender": "der",
                "plural": "die Hausmänner",
                "indefinite": "ein Hausmann",
                "negation": "kein Hausmann",
                "akkusativ": "den / einen / keinen Hausmann",
                "meaning": "người đàn ông nội trợ",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống đực (der Hausmann), số nhiều die Hausmänner.",
                "example": "Mein Onkel ist Hausmann und kümmert sich um die Kinder.",
                "example_vi": "Chú tôi là người nội trợ và chăm sóc con cái."
        },
        {
                "word": "Hausfrau",
                "article": "die",
                "gender": "die",
                "plural": "die Hausfrauen",
                "indefinite": "eine Hausfrau",
                "negation": "keine Hausfrau",
                "akkusativ": "die / eine / keine Hausfrau",
                "meaning": "người phụ nữ nội trợ",
                "category": "Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)",
                "rule": "Danh từ giống cái chuyển từ gốc -mann sang -frau: die Hausfrau.",
                "example": "Meine Großmutter war viele Jahre Hausfrau und kochte gern.",
                "example_vi": "Bà tôi đã làm nội trợ nhiều năm và rất thích nấu ăn."
        },
        {
                "word": "Friseursalon",
                "article": "der",
                "gender": "der",
                "plural": "die Friseursalons",
                "indefinite": "ein Friseursalon",
                "negation": "kein Friseursalon",
                "akkusativ": "den / einen / keinen Friseursalon",
                "meaning": "tiệm làm tóc, salon tóc",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống đực (der Friseursalon). Trả lời Wo? dùng im Friseursalon (in + dem).",
                "example": "Der Friseur arbeitet jeden Tag im Friseursalon.",
                "example_vi": "Người thợ làm tóc làm việc mỗi ngày ở trong tiệm làm tóc."
        },
        {
                "word": "Supermarkt",
                "article": "der",
                "gender": "der",
                "plural": "die Supermärkte",
                "indefinite": "ein Supermarkt",
                "negation": "kein Supermarkt",
                "akkusativ": "den / einen / keinen Supermarkt",
                "meaning": "siêu thị",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống đực (der Supermarkt). Trả lời Wo? dùng im Supermarkt.",
                "example": "Frau Lindner kauft frische Lebensmittel im Supermarkt ein.",
                "example_vi": "Bà Lindner mua thực phẩm tươi ở trong siêu thị."
        },
        {
                "word": "Kindergarten",
                "article": "der",
                "gender": "der",
                "plural": "die Kindergärten",
                "indefinite": "ein Kindergarten",
                "negation": "kein Kindergarten",
                "akkusativ": "den / einen / keinen Kindergarten",
                "meaning": "trường mẫu giáo, nhà trẻ",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống đực. Di chuyển Wohin? -> in den Kindergarten; ở lại Wo? -> im Kindergarten.",
                "example": "Um 8.30 Uhr bringt Frank seine Tochter in den Kindergarten.",
                "example_vi": "Lúc 8 giờ 30 phút Frank đưa con gái vào trường mẫu giáo."
        },
        {
                "word": "Schule",
                "article": "die",
                "gender": "die",
                "plural": "die Schulen",
                "indefinite": "eine Schule",
                "negation": "keine Schule",
                "akkusativ": "die / eine / keine Schule",
                "meaning": "trường học (phổ thông)",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống cái (die Schule). Trả lời Wo? dùng an einer Schule hoặc in der Schule.",
                "example": "Frau Weber unterrichtet viele Schüler an einer Schule in Berlin.",
                "example_vi": "Bà Weber giảng dạy nhiều học sinh tại một trường học ở Berlin."
        },
        {
                "word": "Universität",
                "article": "die",
                "gender": "die",
                "plural": "die Universitäten",
                "indefinite": "eine Universität",
                "negation": "keine Universität",
                "akkusativ": "die / eine / keine Universität",
                "meaning": "trường đại học",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống cái đuôi -tät. Trả lời Wo? dùng an der Universität / an einer Hochschule.",
                "example": "Mein Bruder studiert Informatik an der Universität.",
                "example_vi": "Anh trai tôi học ngành tin học tại trường đại học."
        },
        {
                "word": "Werkstatt",
                "article": "die",
                "gender": "die",
                "plural": "die Werkstätten",
                "indefinite": "eine Werkstatt",
                "negation": "keine Werkstatt",
                "akkusativ": "die / eine / keine Werkstatt",
                "meaning": "xưởng sửa chữa",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống cái (die Werkstatt). Di chuyển Wohin? -> in die Werkstatt; ở tại Wo? -> in der Werkstatt.",
                "example": "Der KFZ-Mechatroniker repariert das Auto in einer Werkstatt.",
                "example_vi": "Người thợ cơ khí ô tô sửa chiếc xe trong một xưởng sửa chữa."
        },
        {
                "word": "Baustelle",
                "article": "die",
                "gender": "die",
                "plural": "die Baustellen",
                "indefinite": "eine Baustelle",
                "negation": "keine Baustelle",
                "akkusativ": "die / eine / keine Baustelle",
                "meaning": "công trường xây dựng",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống cái (die Baustelle). Trả lời Wo? dùng auf der Baustelle / auf einer Baustelle.",
                "example": "Die Arbeiter tragen Helme auf der Baustelle.",
                "example_vi": "Các công nhân đội mũ bảo hộ trên công trường xây dựng."
        },
        {
                "word": "Firma",
                "article": "die",
                "gender": "die",
                "plural": "die Firmen",
                "indefinite": "eine Firma",
                "negation": "keine Firma",
                "akkusativ": "die / eine / keine Firma",
                "meaning": "công ty, doanh nghiệp",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống cái (die Firma). Trả lời Wo? dùng in einer Firma hoặc bei einer IT-Firma.",
                "example": "Paula Rausch arbeitet als Programmiererin bei einer IT-Firma.",
                "example_vi": "Paula Rausch làm nghề lập trình viên tại một công ty công nghệ thông tin."
        },
        {
                "word": "Krankenhaus",
                "article": "das",
                "gender": "das",
                "plural": "die Krankenhäuser",
                "indefinite": "ein Krankenhaus",
                "negation": "kein Krankenhaus",
                "akkusativ": "das / ein / kein Krankenhaus",
                "meaning": "bệnh viện",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống trung (das Krankenhaus). Trả lời Wo? dùng im Krankenhaus (in + dem).",
                "example": "Der Arzt untersucht die Patienten im Krankenhaus.",
                "example_vi": "Bác sĩ khám cho các bệnh nhân ở trong bệnh viện."
        },
        {
                "word": "Restaurant",
                "article": "das",
                "gender": "das",
                "plural": "die Restaurants",
                "indefinite": "ein Restaurant",
                "negation": "kein Restaurant",
                "akkusativ": "das / ein / kein Restaurant",
                "meaning": "nhà hàng",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống trung gốc Pháp (das Restaurant). Trả lời Wo? dùng im Restaurant.",
                "example": "Die Köchin kocht leckere Spezialitäten im Restaurant.",
                "example_vi": "Nữ đầu bếp nấu các món đặc sản ngon miệng ở trong nhà hàng."
        },
        {
                "word": "Blumengeschäft",
                "article": "das",
                "gender": "das",
                "plural": "die Blumengeschäfte",
                "indefinite": "ein Blumengeschäft",
                "negation": "kein Blumengeschäft",
                "akkusativ": "das / ein / kein Blumengeschäft",
                "meaning": "cửa hàng hoa tươi",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ ghép giống trung (das Blumengeschäft). Trả lời Wo? dùng im Blumengeschäft.",
                "example": "Die Floristin verkauft bunte Rosen im Blumengeschäft.",
                "example_vi": "Người nữ bán hoa bán hoa hồng nhiều màu sắc ở trong cửa hàng hoa."
        },
        {
                "word": "Schuhgeschäft",
                "article": "das",
                "gender": "das",
                "plural": "die Schuhgeschäfte",
                "indefinite": "ein Schuhgeschäft",
                "negation": "kein Schuhgeschäft",
                "akkusativ": "das / ein / kein Schuhgeschäft",
                "meaning": "cửa hàng giày dép",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ ghép giống trung (das Schuhgeschäft). Trả lời Wo? dùng im Schuhgeschäft.",
                "example": "Die Verkäuferin verkauft modische Schuhe im Schuhgeschäft.",
                "example_vi": "Nữ nhân viên bán hàng bán giày thời trang ở trong cửa hàng giày."
        },
        {
                "word": "Sprachzentrum",
                "article": "das",
                "gender": "das",
                "plural": "die Sprachzentren",
                "indefinite": "ein Sprachzentrum",
                "negation": "kein Sprachzentrum",
                "akkusativ": "das / ein / kein Sprachzentrum",
                "meaning": "trung tâm ngoại ngữ",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống trung đuôi -um đổi số nhiều sang -en: die Sprachzentren. Dùng im Sprachzentrum.",
                "example": "Wir lernen jeden Tag Deutsch im Sprachzentrum.",
                "example_vi": "Chúng tôi học tiếng Đức mỗi ngày ở trong trung tâm ngoại ngữ."
        },
        {
                "word": "Bett",
                "article": "das",
                "gender": "das",
                "plural": "die Betten",
                "indefinite": "ein Bett",
                "negation": "kein Bett",
                "akkusativ": "das / ein / kein Bett",
                "meaning": "chiếc giường ngủ",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống trung (das Bett). Hướng di chuyển Wohin? -> ins Bett; Vị trí tĩnh Wo? -> im Bett.",
                "example": "Um neunzehn Uhr bringt Frank seine Tochter ins Bett.",
                "example_vi": "Lúc 19 giờ Frank đưa con gái của mình lên giường đi ngủ."
        },
        {
                "word": "Fitnessstudio",
                "article": "das",
                "gender": "das",
                "plural": "die Fitnessstudios",
                "indefinite": "ein Fitnessstudio",
                "negation": "kein Fitnessstudio",
                "akkusativ": "das / ein / kein Fitnessstudio",
                "meaning": "phòng tập thể hình, gym",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống trung (das Fitnessstudio). Trả lời Wo? dùng im Fitnessstudio.",
                "example": "Der Trainer trainiert fleißig Sportler im Fitnessstudio.",
                "example_vi": "Huấn luyện viên rèn luyện chăm chỉ cho vận động viên ở phòng gym."
        },
        {
                "word": "Stadion",
                "article": "das",
                "gender": "das",
                "plural": "die Stadien",
                "indefinite": "ein Stadion",
                "negation": "kein Stadion",
                "akkusativ": "das / ein / kein Stadion",
                "meaning": "sân vận động",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống trung (das Stadion), số nhiều die Stadien. Trả lời Wo? dùng im Stadion.",
                "example": "Am Wochenende spielen Fußballer im großen Stadion.",
                "example_vi": "Vào cuối tuần các cầu thủ thi đấu ở trong sân vận động lớn."
        },
        {
                "word": "Computer",
                "article": "der",
                "gender": "der",
                "plural": "die Computer",
                "indefinite": "ein Computer",
                "negation": "kein Computer",
                "akkusativ": "den / einen / keinen Computer",
                "meaning": "máy vi tính",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống đực (der Computer). Tân ngữ Akkusativ sau brauchen: einen Computer brauchen.",
                "example": "Bei ihrer Arbeit braucht Petra May einen schnellen Computer.",
                "example_vi": "Trong công việc của mình, Petra May cần một chiếc máy tính nhanh."
        },
        {
                "word": "Patient",
                "article": "der",
                "gender": "der",
                "plural": "die Patienten",
                "indefinite": "ein Patient",
                "negation": "kein Patient",
                "akkusativ": "den / einen / keinen Patient",
                "meaning": "bệnh nhân",
                "category": "Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)",
                "rule": "Danh từ giống đực N-Deklination (der Patient). Tân ngữ Akkusativ sau untersuchen: den Patienten untersuchen.",
                "example": "Der Arzt untersucht den kranken Patienten im Behandlungszimmer.",
                "example_vi": "Bác sĩ khám cho bệnh nhân bị ốm ở trong phòng khám bệnh."
        }
]

    vocabularies = []
    for item in vocab_raw:
        meaning = f"{item['meaning']} (Pl: {item['plural']})" if item.get("plural") else item["meaning"]
        example_str = f"{item['example']} ({item['example_vi']})" if item.get("example_vi") else item["example"]
        vocabularies.append((
            lesson_id,
            f"{item['article']} {item['word']}",
            item["article"],
            meaning,
            example_str
        ))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # KHO 100 BÀI TẬP ĐỘC NHẤT BÀI 7 (9 DẠNG CHUẨN DEUTSCHMEISTER)
    # =========================================================================
    raw_exercises = [
        {
                "type": "trac_nghiem",
                "question": "Câu 1: Chọn phương án đúng hoàn thành câu giới thiệu nghề nghiệp: 'Herr Hoffmann arbeitet seit drei Jahren ___ Mechatroniker in München.'",
                "options": [
                        "wie ein",
                        "als",
                        "von",
                        "für"
                ],
                "correct_answer": "als",
                "explanation": "Khi dùng động từ 'arbeiten' để giới thiệu nghề nghiệp, tiếng Đức dùng cấu trúc 'arbeiten als + [Nghề nghiệp]' không có mạo từ (Herr Hoffmann arbeitet als Mechatroniker).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "als"
                        ],
                        "translation": "Ông Hoffmann làm kỹ thuật viên cơ điện tử ở Munich được ba năm rồi."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 2: Chọn câu đúng ngữ pháp tiếng Đức khi miêu tả nghề nghiệp có tính từ đi kèm:",
                "options": [
                        "Frau Schneider ist sehr fleißige Verkäuferin.",
                        "Frau Schneider ist eine sehr fleißige Verkäuferin.",
                        "Frau Schneider arbeitet als eine Verkäuferin.",
                        "Frau Schneider ist einer fleißige Verkäuferin."
                ],
                "correct_answer": "Frau Schneider ist eine sehr fleißige Verkäuferin.",
                "explanation": "Quy tắc nghề nghiệp: Bình thường nói tên nghề không dùng mạo từ (Sie ist Verkäuferin), nhưng khi có tính từ bổ nghĩa (sehr fleißige) thì BẮT BUỘC phải dùng mạo từ không xác định (eine sehr fleißige Verkäuferin).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Frau Schneider ist eine sehr fleißige Verkäuferin."
                        ],
                        "translation": "Bà Schneider là một nữ nhân viên bán hàng rất chăm chỉ."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 3: Cặp danh từ nghề nghiệp Nam – Nữ nào dưới đây được viết ĐÚNG CHÍNH TẢ 100%?",
                "options": [
                        "der Hausmann -> die Hausmännerin / der Krankenpfleger -> die Krankenpfleger",
                        "der Koch -> die Köcherin / der Arzt -> die Ärztinn",
                        "der Koch -> die Köchin / der Arzt -> die Ärztin",
                        "der Koch -> die Kochin / der Arzt -> die Arztin"
                ],
                "correct_answer": "der Koch -> die Köchin / der Arzt -> die Ärztin",
                "explanation": "Hai danh từ der Koch và der Arzt khi chuyển sang giống cái (Femininum) vừa thêm hậu tố -in vừa phải thêm dấu Umlaut trên nguyên âm gốc: die Köchin và die Ärztin. Dạng die Kochin / die Arztin thiếu dấu Umlaut nên sai chính tả.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der Koch -> die Köchin / der Arzt -> die Ärztin"
                        ],
                        "translation": "Nam đầu bếp -> Nữ đầu bếp / Nam bác sĩ -> Nữ bác sĩ."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 4: Chọn phương án đúng hoàn thành câu: 'Ein KFZ-Mechatroniker ___ Autos und arbeitet ___.'",
                "options": [
                        "verkauft / im Schuhgeschäft",
                        "untersucht / im Krankenhaus",
                        "repariert / in einer Werkstatt",
                        "schneidet / im Friseursalon"
                ],
                "correct_answer": "repariert / in einer Werkstatt",
                "explanation": "KFZ-Mechatroniker là kỹ thuật viên cơ điện tử ô tô; công việc là repariert Autos (sửa ô tô) và nơi làm việc (Wo? + Dativ) là in einer Werkstatt (die Werkstatt -> in einer Werkstatt).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "repariert / in einer Werkstatt"
                        ],
                        "translation": "Một kỹ thuật viên cơ điện tử ô tô (KFZ-Mechatroniker) sửa chữa xe hơi và làm việc ở trong một xưởng sửa chữa.",
                        "dynamic_profession_quiz": true
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 5: Chọn dạng chia đúng của động từ khuyết thiếu: 'Mein Kollege ist Programmierer von Beruf. Er ___ drei moderne Programmiersprachen fließend sprechen.'",
                "options": [
                        "könnt",
                        "kannst",
                        "kann",
                        "können"
                ],
                "correct_answer": "kann",
                "explanation": "Động từ können diễn tả khả năng/năng lực chuyên môn. Với ngôi er/sie/es, können chia là 'kann' (đổi nguyên âm ö -> a và không thêm đuôi -t).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "kann"
                        ],
                        "translation": "Đồng nghiệp của tôi làm nghề lập trình viên. Anh ấy có thể nói trôi chảy ba ngôn ngữ lập trình hiện đại."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 6: Chọn dạng chia đúng của động từ khuyết thiếu 'müssen': 'Paula Rausch arbeitet als Programmiererin. Jeden Morgen ___ sie schon um 6.15 Uhr aufstehen.'",
                "options": [
                        "müsst",
                        "musst",
                        "muss",
                        "müssen"
                ],
                "correct_answer": "muss",
                "explanation": "Với động từ khuyết thiếu müssen, ngôi ich và ngôi er/sie/es chia giống hệt nhau là muss (đổi ü -> u và không có đuôi -t).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "muss"
                        ],
                        "translation": "Paula Rausch làm nghề lập trình viên. Mỗi buổi sáng cô ấy phải thức dậy lúc 6 giờ 15.",
                        "dynamic_modalverb_schedule_quiz": true
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 7: Chọn phương án đúng diễn tả quy định an toàn lao động: 'Auf der Baustelle ___ die Arbeiter ohne Schutzhelm nicht arbeiten.'",
                "options": [
                        "dürft",
                        "darf",
                        "dürfen",
                        "darfst"
                ],
                "correct_answer": "dürfen",
                "explanation": "Chủ ngữ 'die Arbeiter' là danh từ số nhiều (họ - sie). Động từ dürfen chia theo ngôi số nhiều là 'dürfen'. Kết hợp với 'nicht' diễn tả điều cấm đoán tuyệt đối trên công trường.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "dürfen"
                        ],
                        "translation": "Trên công trường xây dựng, các công nhân không được phép làm việc khi không đội mũ bảo hộ."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 8: Chọn dạng chia đúng của 'wollen': 'Nach dem Abitur an der Schule ___ meine Schwester Medizin an der Universität studieren.'",
                "options": [
                        "willst",
                        "wollt",
                        "will",
                        "wollen"
                ],
                "correct_answer": "will",
                "explanation": "Động từ wollen diễn tả nguyện vọng, ý chí quyết tâm. Với chủ ngữ 'meine Schwester' (ngôi sie số ít), wollen đổi nguyên âm o -> i thành 'will' (ngôi ich và er/sie/es đều là will).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "will"
                        ],
                        "translation": "Sau khi tốt nghiệp trung học phổ thông, em gái tôi muốn học ngành Y tại trường đại học."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 9: Chọn dạng chia đúng của 'sollen': 'Der Arzt rät dem Patienten: „Herr Braun, Sie haben hohes Fieber. Sie ___ viel Tee trinken und im Bett bleiben.“'",
                "options": [
                        "sollt",
                        "sollen",
                        "soll",
                        "sollst"
                ],
                "correct_answer": "sollen",
                "explanation": "Động từ sollen dùng để truyền đạt lời khuyên hoặc yêu cầu từ người có thẩm quyền (như bác sĩ). Đi với ngôi lịch sự 'Sie' thì động từ giữ nguyên là 'sollen'.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "sollen"
                        ],
                        "translation": "Bác sĩ khuyên bệnh nhân: „Thưa ông Braun, ông bị sốt cao. Ông nên uống nhiều trà và ở trên giường.“"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 10: Chọn câu có cấu trúc khung câu (Satzklammer) đúng ngữ pháp tiếng Đức:",
                "options": [
                        "Im Restaurant muss der Kellner servieren das Essen schnell.",
                        "Im Restaurant muss der Kellner den Gästen das Essen schnell servieren.",
                        "Im Restaurant der Kellner muss servieren das Essen schnell.",
                        "Im Restaurant muss servieren der Kellner schnell das Essen."
                ],
                "correct_answer": "Im Restaurant muss der Kellner den Gästen das Essen schnell servieren.",
                "explanation": "Quy tắc Satzklammer (khung câu): Động từ khuyết thiếu (muss) đứng ở vị trí số 2, toàn bộ các tân ngữ và trạng từ đứng ở giữa, và động từ nguyên mẫu (servieren) bắt buộc phải đứng ở cuối câu cùng.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Im Restaurant muss der Kellner den Gästen das Essen schnell servieren."
                        ],
                        "translation": "Trong nhà hàng, người phục vụ phải nhanh chóng bưng thức ăn cho thực khách."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 11: Chọn mạo từ đúng: 'Der Kellner bringt ___ frischen Kaffee an den Tisch.'",
                "options": [
                        "der",
                        "dem",
                        "den",
                        "das"
                ],
                "correct_answer": "den",
                "explanation": "Danh từ 'Kaffee' mang giống đực (der Kaffee). Làm tân ngữ trực tiếp chịu tác động của hành động 'bringen' nên chia ở Cách 4 (Akkusativ): mạo từ der chuyển thành den.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "den"
                        ],
                        "translation": "Người phục vụ mang cà phê tươi đến bàn."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 12: Chọn cặp mạo từ đúng: '1. Die Ärztin untersucht ___ kranken Mann. — 2. Die Krankenschwester hilft ___ kranken Mann.'",
                "options": [
                        "den / dem",
                        "dem / den",
                        "den / den",
                        "dem / dem"
                ],
                "correct_answer": "den / dem",
                "explanation": "Động từ untersuchen đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ: der Mann -> den Mann). Động từ helfen đòi hỏi tân ngữ ở Cách 3 (Dativ: der Mann -> dem Mann).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "den / dem"
                        ],
                        "translation": "1. Nữ bác sĩ khám cho người đàn ông bị ốm. — 2. Nữ y tá giúp đỡ người đàn ông bị ốm.",
                        "dynamic_akkdativ_kontrast_quiz": true
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 13: Chọn mạo từ đúng: 'Für seine tägliche Arbeit im Büro kauft der Sekretär ___ neuen Drucker.'",
                "options": [
                        "ein",
                        "einen",
                        "einem",
                        "einer"
                ],
                "correct_answer": "einen",
                "explanation": "Động từ kaufen đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ). Danh từ der Drucker là giống đực, nên mạo từ không xác định ein đổi sang Akkusativ là einen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "einen"
                        ],
                        "translation": "Cho công việc hằng ngày ở văn phòng, nam thư ký mua một chiếc máy in mới."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 14: Chọn mạo từ phủ định đúng: 'Heute ist Sonntag und der Schüler hat schulfrei. Er braucht ___ Wecker.'",
                "options": [
                        "kein",
                        "keinen",
                        "keinem",
                        "keine"
                ],
                "correct_answer": "keinen",
                "explanation": "Động từ brauchen đi với Cách 4 (Akkusativ). Danh từ der Wecker mang giống đực, do đó mạo từ phủ định kein đổi thành keinen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "keinen"
                        ],
                        "translation": "Hôm nay là Chủ nhật và học sinh được nghỉ học. Cậu ấy không cần đồng hồ báo thức."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 15: Chọn cặp giới từ đúng: 'Der Trainer kauft neue Bälle ___ sein Team und läuft niemals ___ seine Sportschuhe.'",
                "options": [
                        "für / ohne",
                        "mit / für",
                        "zu / von",
                        "bei / mit"
                ],
                "correct_answer": "für / ohne",
                "explanation": "Hai giới từ 'für' (dành cho) và 'ohne' (không có) thuộc nhóm FUDGE-BO luôn luôn đòi hỏi danh từ đi sau chia ở Cách 4 (Akkusativ): für sein Team, ohne seine Sportschuhe.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "für / ohne"
                        ],
                        "translation": "Huấn luyện viên mua những quả bóng mới cho đội của mình và không bao giờ chạy mà không có giày thể thao."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 16: Chọn dạng mạo từ sở hữu đúng: 'Der Taxifahrer holt ___ Wagen am Morgen aus der Garage.'",
                "options": [
                        "sein",
                        "seinen",
                        "seinem",
                        "seiner"
                ],
                "correct_answer": "seinen",
                "explanation": "Chủ ngữ là der Taxifahrer (ngôi er), gốc sở hữu là sein-. Danh từ der Wagen mang giống đực làm tân ngữ trực tiếp (Akkusativ) cho holt, nên mạo từ sở hữu đổi thành seinen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "seinen"
                        ],
                        "translation": "Người tài xế taxi lấy chiếc xe của mình ra khỏi gara vào buổi sáng."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 17: Chọn phương án đúng ngữ pháp: 'Der Chef kauft ___ Sekretärin ___ neuen Computer.'",
                "options": [
                        "der / ein",
                        "einer / dem",
                        "die / einen",
                        "der / einen"
                ],
                "correct_answer": "der / einen",
                "explanation": "Trong câu có 2 tân ngữ: Người nhận lợi ích (Wem? cho nữ thư ký) chia ở Cách 3 (Dativ: die -> der Sekretärin); Vật được mua (Was? một chiếc máy tính mới) chia ở Cách 4 (Akkusativ: der -> einen neuen Computer).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der / einen"
                        ],
                        "translation": "Người sếp mua cho nữ thư ký một chiếc máy tính mới."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 18: Chọn dạng mạo từ sở hữu đúng: 'Liebe Schüler, ihr müsst morgen ___ Lehrer fragen und ___ Hefte mitbringen!'",
                "options": [
                        "euer / eure",
                        "euren / eure",
                        "eurem / euren",
                        "eurer / eure"
                ],
                "correct_answer": "euren / eure",
                "explanation": "Động từ fragen (hỏi ai) và mitbringen (mang theo cái gì) đều đi với Cách 4 (Akkusativ). Chủ ngữ là ihr (các em) -> gốc euer. Trước der Lehrer (giống đực Akkusativ) đổi thành euren Lehrer; trước die Hefte (số nhiều Akkusativ) đổi thành eure Hefte.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "euren / eure"
                        ],
                        "translation": "Các em học sinh thân mến, ngày mai các em phải hỏi thầy giáo của các em và mang theo vở của các em nhé!",
                        "dynamic_possessivartikel_akkusativ_quiz": true
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 19: Điền dạng chia đúng của động từ khuyết thiếu 'können' vào chỗ trống: 'Am Samstag haben wir frei. ___ ihr mit uns ins Restaurant kommen?'",
                "options": null,
                "correct_answer": "Könnt",
                "explanation": "Chủ ngữ là 'ihr' (các bạn). Động từ können chia cho ngôi ihr là könnt (giữ nguyên âm ö và thêm đuôi -t). Đứng đầu câu hỏi đảo ngữ nên viết hoa Könnt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Könnt",
                                "könnt"
                        ],
                        "translation": "Thứ Bảy chúng tôi được nghỉ. Các bạn có thể đi nhà hàng cùng chúng tôi không?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 20: Điền dạng chia đúng của động từ khuyết thiếu 'müssen' vào chỗ trống: 'Wie viele Stunden ___ du pro Tag im Büro arbeiten?'",
                "options": null,
                "correct_answer": "musst",
                "explanation": "Chủ ngữ là 'du'. Động từ müssen đổi ü -> u và chia đuôi -st thành musst.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "musst"
                        ],
                        "translation": "Bạn phải làm việc bao nhiêu tiếng mỗi ngày ở văn phòng?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 21: Điền dạng chia đúng của động từ khuyết thiếu 'dürfen' vào chỗ trống: 'Hier ist eine gefährliche Baustelle. ___ Besucher das Gelände betreten?'",
                "options": null,
                "correct_answer": "Dürfen",
                "explanation": "Chủ ngữ 'Besucher' là danh từ số nhiều (những vị khách). Động từ dürfen giữ nguyên là Dürfen ở đầu câu hỏi.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Dürfen",
                                "dürfen"
                        ],
                        "translation": "Đây là công trường nguy hiểm. Khách tham quan có được phép đi vào khu vực này không?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 22: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'Nächste Woche ___ wir einen schönen Ausflug mit der Familie machen.'",
                "options": null,
                "correct_answer": "wollen",
                "explanation": "Chủ ngữ là 'wir' (chúng tôi). Động từ wollen giữ nguyên dạng nguyên mẫu là wollen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "wollen"
                        ],
                        "translation": "Tuần tới chúng tôi muốn có một chuyến dã ngoại tuyệt đẹp cùng gia đình."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 23: Điền mạo từ xác định thích hợp vào chỗ trống: 'Der Lehrer korrigiert ___ schwierigen Test der Schüler am Schreibtisch.'",
                "options": null,
                "correct_answer": "den",
                "explanation": "Danh từ 'der Test' mang giống đực. Làm tân ngữ trực tiếp cho động từ korrigieren nên đổi thành den.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "den"
                        ],
                        "translation": "Thầy giáo chấm bài kiểm tra khó của học sinh tại bàn làm việc."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 24: Điền mạo từ không xác định thích hợp vào chỗ trống: 'Im Blumengeschäft bestellt der Kunde ___ bunten Blumenstrauß.'",
                "options": null,
                "correct_answer": "einen",
                "explanation": "Danh từ 'der Blumenstrauß' mang giống đực, làm tân ngữ trực tiếp cho bestellt nên mạo từ ein đổi thành einen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "einen"
                        ],
                        "translation": "Ở cửa hàng hoa, người khách đặt một bó hoa rực rỡ sắc màu."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 25: Điền mạo từ phủ định thích hợp vào chỗ trống: 'Heute scheint den ganzen Tag die Sonne, ich brauche ___ Regenschirm.'",
                "options": null,
                "correct_answer": "keinen",
                "explanation": "Động từ brauchen đi với Cách 4 (Akkusativ). Danh từ der Regenschirm là giống đực nên kein đổi thành keinen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "keinen"
                        ],
                        "translation": "Hôm nay trời nắng cả ngày, tôi không cần chiếc ô nào cả."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 26: Điền mạo từ sở hữu của ngôi 'ich' (mein-) thích hợp vào chỗ trống: 'Vor der Konferenz rufe ich ___ Kollegen noch einmal an.'",
                "options": null,
                "correct_answer": "meinen",
                "explanation": "Động từ anrufen đòi hỏi tân ngữ Akkusativ. Chủ ngữ ich -> gốc mein-. Trước danh từ giống đực der Kollege đổi thành meinen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "meinen"
                        ],
                        "translation": "Trước hội nghị, tôi gọi điện cho người đồng nghiệp của mình một lần nữa."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 27: Điền mạo từ thích hợp vào chỗ trống: 'Die Trainerin lobt ___ besten Sportler nach dem Spiel.'",
                "options": null,
                "correct_answer": "ihren",
                "explanation": "Động từ loben (khen ngợi) đi với Cách 4 (Akkusativ). Danh từ der Sportler mang giống đực nên mạo từ sở hữu của cô ấy ihr- đổi thành ihren (hoặc mạo từ xác định den).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ihren",
                                "den"
                        ],
                        "translation": "Nữ huấn luyện viên khen ngợi vận động viên xuất sắc nhất của mình sau trận đấu."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 28: Điền giới từ thích hợp vào chỗ trống: 'Der Koch kauft frische Zutaten ___ das Abendessen.'",
                "options": null,
                "correct_answer": "für",
                "explanation": "Giới từ für luôn luôn đòi hỏi danh từ đi sau chia ở Cách 4 (Akkusativ): für das Abendessen (cho bữa tối).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "für",
                                "fuer"
                        ],
                        "translation": "Người đầu bếp mua các nguyên liệu tươi ngon cho bữa tối."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 29: Điền giới từ thích hợp vào chỗ trống: 'Der Student kann ___ sein Wörterbuch den Fachtext nicht verstehen.'",
                "options": null,
                "correct_answer": "ohne",
                "explanation": "Giới từ ohne mang nghĩa 'không có / thiếu' và luôn đi với Akkusativ (ohne sein Wörterbuch).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ohne"
                        ],
                        "translation": "Cậu sinh viên không thể hiểu được bài đọc chuyên ngành nếu thiếu cuốn từ điển."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 30: Điền từ thích hợp vào chỗ trống: 'Der Kunde parkt den Wagen und geht in ___ Supermarkt.'",
                "options": null,
                "correct_answer": "den",
                "explanation": "Động từ gehen chỉ sự di chuyển (hướng đi Wohin?) đòi hỏi in + Akkusativ: in den Supermarkt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "den",
                                "einen"
                        ],
                        "translation": "Người khách hàng đỗ xe và đi vào trong siêu thị."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 31: Điền từ thích hợp vào chỗ trống: 'Nach dem langen Arbeitstag legt sich der Arzt müde ___ Bett.'",
                "options": null,
                "correct_answer": "ins",
                "explanation": "Hành động nằm lên giường (di chuyển Wohin? + Akkusativ) với danh từ giống trung das Bett được rút gọn in + das = ins Bett.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ins",
                                "in das"
                        ],
                        "translation": "Sau một ngày làm việc dài, vị bác sĩ mệt mỏi ngả lưng lên giường."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 32: Điền từ thích hợp vào chỗ trống: 'Die Mechatronikerin prüft die Bremsen des Autos in ___ Werkstatt.'",
                "options": null,
                "correct_answer": "der",
                "explanation": "Câu hỏi Wo? (vị trí tĩnh) đòi hỏi Cách 3 (Dativ). Danh từ die Werkstatt mang giống cái nên in + der = in der Werkstatt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der"
                        ],
                        "translation": "Nữ thợ cơ khí kiểm tra phanh xe hơi ở trong xưởng sửa chữa."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 33: Điền mạo từ thích hợp vào chỗ trống: 'Der erfahrene Krankenpfleger hilft ___ jungen Ärztin bei der Operation.'",
                "options": null,
                "correct_answer": "der",
                "explanation": "Động từ helfen luôn luôn đòi hỏi tân ngữ ở Cách 3 (Dativ). Danh từ die Ärztin (giống cái) chuyển mạo từ thành der Ärztin.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der"
                        ],
                        "translation": "Người nam điều dưỡng giàu kinh nghiệm giúp đỡ nữ bác sĩ trẻ trong ca phẫu thuật."
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 34: Dịch sang tiếng Đức (kèm mạo từ): 'nữ lập trình viên'",
                "options": null,
                "correct_answer": "die Programmiererin",
                "explanation": "Nam lập trình viên là der Programmierer -> Nữ lập trình viên thêm -in là die Programmiererin.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "die Programmiererin",
                                "Programmiererin"
                        ],
                        "translation": "nữ lập trình viên"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 35: Dịch sang tiếng Đức (kèm mạo từ): 'thợ cơ khí ô tô (nam)'",
                "options": null,
                "correct_answer": "der KFZ-Mechatroniker",
                "explanation": "Thợ cơ khí / kỹ thuật viên sửa chữa ô tô là der KFZ-Mechatroniker (hoặc der Mechatroniker).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der KFZ-Mechatroniker",
                                "der Mechatroniker",
                                "KFZ-Mechatroniker",
                                "Mechatroniker"
                        ],
                        "translation": "thợ cơ khí ô tô (nam)"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 36: Dịch sang tiếng Đức (kèm mạo từ): 'nữ y tá / điều dưỡng'",
                "options": null,
                "correct_answer": "die Krankenpflegerin",
                "explanation": "Nữ y tá / điều dưỡng trong tiếng Đức là die Krankenpflegerin hoặc die Krankenschwester.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "die Krankenpflegerin",
                                "die Krankenschwester",
                                "Krankenpflegerin",
                                "Krankenschwester"
                        ],
                        "translation": "nữ y tá / điều dưỡng"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 37: Dịch sang tiếng Đức (kèm mạo từ): 'người bán hoa (nữ)'",
                "options": null,
                "correct_answer": "die Floristin",
                "explanation": "Nam bán hoa là der Florist -> Nữ bán hoa là die Floristin.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "die Floristin",
                                "Floristin"
                        ],
                        "translation": "người bán hoa (nữ)"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 38: Dịch sang tiếng Đức (kèm mạo từ): 'tiệm làm tóc / salon tóc'",
                "options": null,
                "correct_answer": "der Friseursalon",
                "explanation": "Tiệm làm tóc là danh từ giống đực der Friseursalon (số nhiều: die Friseursalons).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "der Friseursalon",
                                "Friseursalon"
                        ],
                        "translation": "tiệm làm tóc / salon tóc"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 39: Dịch sang tiếng Đức (kèm mạo từ): 'xưởng sửa chữa'",
                "options": null,
                "correct_answer": "die Werkstatt",
                "explanation": "Xưởng sửa chữa là danh từ giống cái die Werkstatt (số nhiều: die Werkstätten).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "die Werkstatt",
                                "Werkstatt"
                        ],
                        "translation": "xưởng sửa chữa"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 40: Dịch sang tiếng Đức (kèm mạo từ): 'công trường xây dựng'",
                "options": null,
                "correct_answer": "die Baustelle",
                "explanation": "Công trường xây dựng là danh từ giống cái die Baustelle (số nhiều: die Baustellen).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "die Baustelle",
                                "Baustelle"
                        ],
                        "translation": "công trường xây dựng"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 41: Dịch sang tiếng Đức (kèm mạo từ): 'cửa hàng hoa'",
                "options": null,
                "correct_answer": "das Blumengeschäft",
                "explanation": "Cửa hàng hoa là danh từ ghép giống trung das Blumengeschäft (số nhiều: die Blumengeschäfte).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "das Blumengeschäft",
                                "Blumengeschäft",
                                "das Blumengeschaeft"
                        ],
                        "translation": "cửa hàng hoa"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 42: Dịch sang tiếng Đức (kèm mạo từ): 'trung tâm ngoại ngữ'",
                "options": null,
                "correct_answer": "das Sprachzentrum",
                "explanation": "Trung tâm ngoại ngữ là danh từ giống trung das Sprachzentrum (số nhiều: die Sprachzentren).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "das Sprachzentrum",
                                "Sprachzentrum"
                        ],
                        "translation": "trung tâm ngoại ngữ"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 43: Dịch cụm hoạt động nghề nghiệp sau sang tiếng Đức: 'khám cho các bệnh nhân'",
                "options": null,
                "correct_answer": "Patienten untersuchen",
                "explanation": "Động từ 'khám bệnh' là untersuchen, bệnh nhân số nhiều là die Patienten -> Patienten untersuchen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Patienten untersuchen",
                                "die Patienten untersuchen",
                                "untersucht Patienten"
                        ],
                        "translation": "khám cho các bệnh nhân"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 44: Dịch cụm hoạt động nghề nghiệp sau sang tiếng Đức: 'cắt tóc'",
                "options": null,
                "correct_answer": "Haare schneiden",
                "explanation": "Danh từ 'tóc' (số nhiều) là die Haare, động từ 'cắt' là schneiden -> Haare schneiden.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Haare schneiden",
                                "die Haare schneiden",
                                "schneidet Haare"
                        ],
                        "translation": "cắt tóc"
                }
        },
        {
                "type": "dich_nghia_vd",
                "question": "Câu 45: Dịch câu hỏi nghề nghiệp sau sang tiếng Đức (dạng trang trọng 'Sie'): 'Ngài làm nghề gì?'",
                "options": null,
                "correct_answer": "Was sind Sie von Beruf?",
                "explanation": "Cả 3 mẫu câu Was sind Sie von Beruf?, Was machen Sie beruflich? và Was ist Ihr Beruf? đều chuẩn xác 100%.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Was sind Sie von Beruf?",
                                "Was machen Sie beruflich?",
                                "Was ist Ihr Beruf?"
                        ],
                        "translation": "Sie"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 46: Dịch sang tiếng Việt: 'der Taxifahrer / die Taxifahrerin'",
                "options": null,
                "correct_answer": "tài xế taxi",
                "explanation": "der Taxifahrer (nam) và die Taxifahrerin (nữ) có nghĩa là tài xế taxi.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "tài xế taxi",
                                "người lái xe taxi",
                                "nam tài xế taxi và nữ tài xế taxi",
                                "lái xe taxi"
                        ],
                        "translation": "tài xế taxi"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 47: Dịch sang tiếng Việt: 'der Hausmann / die Hausfrau'",
                "options": null,
                "correct_answer": "người nội trợ",
                "explanation": "der Hausmann (nam nội trợ) và die Hausfrau (nữ nội trợ).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "người nội trợ",
                                "nam nội trợ và nữ nội trợ",
                                "đàn ông nội trợ và phụ nữ nội trợ",
                                "nội trợ"
                        ],
                        "translation": "người nội trợ"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 48: Dịch sang tiếng Việt: 'der Kellner / die Kellnerin'",
                "options": null,
                "correct_answer": "nhân viên phục vụ bàn",
                "explanation": "der Kellner / die Kellnerin là nhân viên phục vụ bàn (bồi bàn) trong nhà hàng hoặc quán cà phê.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "nhân viên phục vụ bàn",
                                "bồi bàn",
                                "người phục vụ nhà hàng",
                                "nam bồi bàn và nữ bồi bàn"
                        ],
                        "translation": "nhân viên phục vụ bàn"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 49: Dịch sang tiếng Việt: 'der Sekretär / die Sekretärin'",
                "options": null,
                "correct_answer": "thư ký",
                "explanation": "der Sekretär / die Sekretärin có nghĩa là thư ký văn phòng.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "thư ký",
                                "nam thư ký và nữ thư ký",
                                "người thư ký"
                        ],
                        "translation": "thư ký"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 50: Dịch sang tiếng Việt: 'Schüler an einer Schule unterrichten'",
                "options": null,
                "correct_answer": "dạy học sinh ở một trường học",
                "explanation": "unterrichten = giảng dạy; Schüler = học sinh; an einer Schule = tại một ngôi trường.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "dạy học sinh ở một trường học",
                                "giảng dạy học sinh tại một ngôi trường",
                                "dạy học sinh tại một trường học"
                        ],
                        "translation": "dạy học sinh ở một trường học"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 51: Dịch sang tiếng Việt: 'Computerprogramme schreiben'",
                "options": null,
                "correct_answer": "viết chương trình máy tính",
                "explanation": "die Computerprogramme = các chương trình máy tính; schreiben = viết.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "viết chương trình máy tính",
                                "viết các chương trình máy tính",
                                "lập trình phần mềm máy tính"
                        ],
                        "translation": "viết chương trình máy tính"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 52: Dịch sang tiếng Việt: 'die Tochter vom Kindergarten abholen'",
                "options": null,
                "correct_answer": "đón con gái từ trường mẫu giáo",
                "explanation": "abholen = đón; vom Kindergarten = từ trường mẫu giáo / nhà trẻ.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "đón con gái từ trường mẫu giáo",
                                "đón con gái từ nhà trẻ về",
                                "đón cô con gái ở trường mầm non"
                        ],
                        "translation": "đón con gái từ trường mẫu giáo"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 53: Dịch sang tiếng Việt: 'das Auto in die Werkstatt bringen'",
                "options": null,
                "correct_answer": "mang ô tô vào xưởng sửa chữa",
                "explanation": "in die Werkstatt bringen (Wohin? + Akkusativ) = mang/đưa vào xưởng sửa chữa.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "mang ô tô vào xưởng sửa chữa",
                                "đưa xe hơi đến xưởng sửa chữa",
                                "đem ô tô vào xưởng"
                        ],
                        "translation": "mang ô tô vào xưởng sửa chữa"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 54: Dịch sang tiếng Việt: 'zum Fußballtraining gehen'",
                "options": null,
                "correct_answer": "đi đến buổi tập bóng đá",
                "explanation": "das Fußballtraining = buổi tập luyện bóng đá; zum Fußballtraining gehen = đi tập bóng đá.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "đi đến buổi tập bóng đá",
                                "đi tập đá bóng",
                                "đi tới buổi huấn luyện bóng đá"
                        ],
                        "translation": "đi đến buổi tập bóng đá"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 55: Dịch sang tiếng Việt: 'Kunden im Büro anrufen'",
                "options": null,
                "correct_answer": "gọi điện cho khách hàng ở trong văn phòng",
                "explanation": "die Kunden = khách hàng; anrufen = gọi điện thoại; im Büro = ở trong văn phòng.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "gọi điện cho khách hàng ở trong văn phòng",
                                "gọi điện thoại cho khách hàng tại văn phòng",
                                "gọi cho khách hàng ở văn phòng"
                        ],
                        "translation": "gọi điện cho khách hàng ở trong văn phòng"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 56: Dịch sang tiếng Việt: 'müssen — können — möchten'",
                "options": null,
                "correct_answer": "phải - có thể - muốn",
                "explanation": "Ba động từ khuyết thiếu trọng tâm: müssen (phải), können (có thể), möchten (muốn).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "phải - có thể - muốn",
                                "phải, có thể, muốn",
                                "bắt buộc phải - có thể - muốn"
                        ],
                        "translation": "phải - có thể - muốn"
                }
        },
        {
                "type": "dich_nghia_dv",
                "question": "Câu 57: Dịch sang tiếng Việt: 'im Schuhgeschäft Schuhe verkaufen'",
                "options": null,
                "correct_answer": "bán giày ở trong cửa hàng giày",
                "explanation": "im Schuhgeschäft = ở trong cửa hàng giày dép; Schuhe verkaufen = bán giày.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "bán giày ở trong cửa hàng giày",
                                "bán giày dép tại tiệm giày",
                                "bán giày trong tiệm giày"
                        ],
                        "translation": "bán giày ở trong cửa hàng giày"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 58: Nối Nghề nghiệp (Cột Trái) với Nhiệm vụ chuyên môn đặc trưng (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Nối nghề nghiệp với nhiệm vụ và nơi làm việc đặc trưng: 1. Florist/in (thợ hoa) làm việc tại Blumengeschäft, nhiệm vụ là cắm hoa (bindet Blumensträuße) và bán hoa (verkauft Rosen). 2. KFZ-Mechatroniker/in (kỹ thuật viên cơ điện tử ô tô) làm việc trong Werkstatt, nhiệm vụ là sửa động cơ (repariert Motoren) và kiểm tra phanh (prüft Bremsen). 3. Kellner/in (nhân viên phục vụ bàn) làm việc tại quán ăn/nhà hàng, nhiệm vụ là bưng đồ uống (serviert Getränke) và mang món ăn ra bàn (bringt Speisen an den Tisch). 4. Bauarbeiter/in (công nhân xây dựng) làm việc tại Baustelle, nhiệm vụ là xây nhà (baut Gebäude) và phải đội mũ bảo hộ lao động (trägt Schutzhelm).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Florist / Floristin",
                                        "right": "bindet Blumensträuße und verkauft Rosen im Blumengeschäft"
                                },
                                {
                                        "left": "KFZ-Mechatroniker / Mechatronikerin",
                                        "right": "repariert defekte Motoren und prüft Bremsen in der Werkstatt"
                                },
                                {
                                        "left": "Kellner / Kellnerin",
                                        "right": "serviert Getränke und bringt Speisen an den Tisch"
                                },
                                {
                                        "left": "Bauarbeiter / Bauarbeiterin",
                                        "right": "baut moderne Gebäude und trägt Schutzhelm auf der Baustelle"
                                }
                        ],
                        "translation": "1. Thợ hoa: cắm/bó hoa và bán hoa hồng trong cửa hàng hoa. | 2. Kỹ thuật viên cơ điện tử ô tô: sửa chữa động cơ hỏng và kiểm tra phanh trong xưởng sửa chữa. | 3. Nhân viên phục vụ bàn: bưng đồ uống và mang món ăn đến bàn cho khách. | 4. Công nhân xây dựng: xây các tòa nhà hiện đại và đội mũ bảo hộ trên công trường."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 59: Nối Nghề nghiệp (Cột Trái) với Nơi làm việc chuẩn ngữ pháp (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Vị trí nơi làm việc (câu hỏi Wo? - Ở đâu?) đi với giới từ in + Cách 3 (Dativ): 1. die Verkäuferin bán hàng ở siêu thị/tiệm giày: der Supermarkt / das Schuhgeschäft là giống đực/trung nên in + dem rút gọn thành 'im Supermarkt / im Schuhgeschäft'. 2. der Koch nấu nướng trong bếp: die Restaurantküche là danh từ giống cái nên in + der chuyển thành 'in der Restaurantküche'. 3. die Schülerin & der Lehrer dạy và học ở trường: das Klassenzimmer là giống trung nên in + dem rút gọn thành 'im Klassenzimmer'. 4. die Trainerin & der Sportler tập luyện ở sân vận động: das Fußballstadion là giống trung nên in + dem rút gọn thành 'im großen Fußballstadion'.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "die Verkäuferin",
                                        "right": "im Supermarkt oder im Schuhgeschäft"
                                },
                                {
                                        "left": "der Koch",
                                        "right": "in der Restaurantküche am Herd"
                                },
                                {
                                        "left": "die Schülerin und der Lehrer",
                                        "right": "im Klassenzimmer am Gymnasium"
                                },
                                {
                                        "left": "die Trainerin und der Sportler",
                                        "right": "im großen Fußballstadion"
                                }
                        ],
                        "translation": "1. Nữ nhân viên bán hàng: ở trong siêu thị hoặc trong cửa hàng giày. | 2. Nam đầu bếp: ở trong gian bếp nhà hàng bên cạnh bếp nấu. | 3. Nữ học sinh và nam thầy giáo: ở trong phòng học tại trường trung học. | 4. Nữ huấn luyện viên và nam vận động viên: ở trong sân vận động bóng đá lớn."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 60: Nối Cụm động từ cố định (Cột Trái) với Thành phần đi kèm phù hợp ngữ pháp (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Quy tắc ngữ pháp của các cụm động từ đi kèm giới từ cố định: 1. 'arbeiten als' đi trực tiếp với tên nghề nghiệp mà không dùng mạo từ (không dùng ein/der): arbeiten als Mechatroniker. 2. 'telefonieren mit' luôn đòi hỏi Cách 3 (Dativ): danh từ giống đực der Kunde đổi thành 'mit dem Kunden'. 3. 'danken für' luôn đòi hỏi Cách 4 (Akkusativ): danh từ giống cái die Hilfe giữ nguyên mạo từ 'für die große Hilfe'. 4. 'helfen bei' luôn đòi hỏi Cách 3 (Dativ): danh từ giống cái die Arbeit đổi mạo từ thành 'bei der schweren Arbeit'.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "arbeiten als",
                                        "right": "Mechatroniker bei einer Autofirma"
                                },
                                {
                                        "left": "telefonieren mit",
                                        "right": "dem Kunden im Büro"
                                },
                                {
                                        "left": "danken für",
                                        "right": "die große Hilfe der Kollegen"
                                },
                                {
                                        "left": "helfen bei",
                                        "right": "der schweren Arbeit am Computer"
                                }
                        ],
                        "translation": "1. làm việc với tư cách là kỹ thuật viên cơ điện tử tại một công ty ô tô | 2. gọi điện thoại với khách hàng ở văn phòng | 3. cảm ơn vì sự giúp đỡ to lớn của các đồng nghiệp | 4. giúp đỡ trong công việc nặng nhọc bên máy vi tính."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 61: Nối Động từ khuyết thiếu (Cột Trái) với Tình huống thực tế sử dụng (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Bản chất và ngữ cảnh sử dụng của 4 động từ khuyết thiếu: 1. 'müssen' diễn tả sự bắt buộc khách quan, luật lệ hoặc quy định bắt buộc phải tuân theo (đèn đỏ thì xe cộ bắt buộc phải dừng). 2. 'können' diễn tả năng lực, khả năng chuyên môn hoặc kỹ năng cá nhân (khả năng nói được 4 ngoại ngữ). 3. 'nicht dürfen' diễn tả sự cấm đoán tuyệt đối, liên quan đến an toàn lao động hoặc biển báo cấm (cấm người ngoài vào công trường nguy hiểm). 4. 'wollen' diễn tả ý chí quyết tâm mạnh mẽ, mong muốn chủ quan hoặc kế hoạch đã định sẵn cho tương lai.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "müssen",
                                        "right": "Die Ampel ist rot, alle Autos stoppen hier."
                                },
                                {
                                        "left": "können",
                                        "right": "Er spricht fließend vier Fremdsprachen."
                                },
                                {
                                        "left": "nicht dürfen",
                                        "right": "Hier ist eine Baustelle, Betreten verboten!"
                                },
                                {
                                        "left": "wollen",
                                        "right": "Wir haben einen festen Plan für die Zukunft."
                                }
                        ],
                        "translation": "1. müssen: Đèn giao thông màu đỏ, tất cả ô tô phải dừng lại ở đây. | 2. können: Anh ấy có thể nói trôi chảy bốn thứ tiếng ngoại ngữ. | 3. nicht dürfen: Đây là công trường xây dựng, cấm vào (không được phép vào)! | 4. wollen: Chúng tôi có một kế hoạch kiên định cho tương lai (muốn / quyết tâm thực hiện)."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 62: Nối Chủ ngữ (Cột Trái) với Dạng chia đúng của Modalverb wollen & dürfen (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Quy tắc chia động từ khuyết thiếu wollen (muốn) và dürfen (được phép): 1. Ngôi 'ich' và ngôi số ít 'er/sie/es' luôn chia giống hệt nhau, đổi nguyên âm (o -> i, ü -> a) và hoàn toàn KHÔNG có đuôi động từ (-t): ich/er/sie/es will, darf. 2. Ngôi 'du' đổi nguyên âm và thêm đuôi -st theo quy tắc chia: du willst, darfst. 3. Ngôi 'ihr' giữ nguyên âm gốc của động từ (o, ü) và thêm đuôi -t: ihr wollt, dürft. 4. Ngôi số nhiều 'wir', 'sie' (họ) và ngôi lịch sự 'Sie' giữ nguyên dạng nguyên mẫu tận cùng đuôi -en: wir/sie/Sie wollen, dürfen.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "ich / er / sie / es",
                                        "right": "will / darf"
                                },
                                {
                                        "left": "du",
                                        "right": "willst / darfst"
                                },
                                {
                                        "left": "ihr",
                                        "right": "wollt / dürft"
                                },
                                {
                                        "left": "wir / sie / Sie",
                                        "right": "wollen / dürfen"
                                }
                        ],
                        "translation": "1. ich / er / sie / es: tôi / anh ấy / cô ấy / nó muốn / được phép | 2. du: bạn muốn / được phép | 3. ihr: các bạn muốn / được phép | 4. wir / sie / Sie: chúng tôi / họ / Ngài muốn / được phép."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 63: Nối Câu hỏi phỏng vấn công việc (Cột Trái) với Câu trả lời phù hợp ngữ cảnh (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Đối chiếu ngữ cảnh câu hỏi và câu trả lời trong phỏng vấn nghề nghiệp: 1. 'Was machen Sie beruflich?' (hỏi nghề nghiệp) -> trả lời bằng cấu trúc chức danh nghề 'Ich arbeite als Mechatroniker...'. 2. 'Wo arbeiten Sie...?' (hỏi địa điểm làm việc) -> trả lời bằng cụm chỉ nơi chốn 'In einer modernen Werkstatt...'. 3. 'Welche Aufgaben müssen Sie übernehmen?' (hỏi nhiệm vụ công việc) -> trả lời bằng các hành động chuyên môn 'Ich muss Fahrzeuge warten und Fehler diagnostizieren'. 4. 'Wie gefällt Ihnen die Arbeit?' (hỏi cảm nhận/mức độ yêu thích) -> trả lời bằng đánh giá tích cực 'Sehr gut, ich kann viele neue Technologien lernen'.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Was machen Sie beruflich, Herr Bauer?",
                                        "right": "Ich arbeite als Mechatroniker bei einer Autofirma."
                                },
                                {
                                        "left": "Wo arbeiten Sie jeden Tag?",
                                        "right": "In einer modernen Werkstatt am Stadtrand."
                                },
                                {
                                        "left": "Welche Aufgaben müssen Sie übernehmen?",
                                        "right": "Ich muss Fahrzeuge warten und Fehler diagnostizieren."
                                },
                                {
                                        "left": "Wie gefällt Ihnen die Arbeit?",
                                        "right": "Sehr gut, ich kann viele neue Technologien lernen."
                                }
                        ],
                        "translation": "1. 'Thưa ông Bauer, ông làm nghề gì?' — 'Tôi làm kỹ thuật viên cơ điện tử tại một công ty ô tô.' | 2. 'Hằng ngày ông làm việc ở đâu?' — 'Trong một xưởng sửa chữa hiện đại ở ngoại ô thành phố.' | 3. 'Ông phải đảm nhận những nhiệm vụ nào?' — 'Tôi phải bảo dưỡng xe cộ và chẩn đoán lỗi hỏng.' | 4. 'Ông thấy công việc này thế nào?' — 'Rất tốt, tôi có thể học hỏi nhiều công nghệ mới.'"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 64: Nối Động từ (Cột Trái) với Cụm danh từ tân ngữ phù hợp ngữ pháp (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Quy tắc đòi hỏi Cách (Kasus) của từng động từ: 1. 'untersuchen' (khám bệnh) đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ): danh từ giống đực der Patient (danh từ N-Deklination) đổi thành 'den kranken Patienten'. 2. 'helfen' (giúp đỡ) luôn đòi hỏi tân ngữ ở Cách 3 (Dativ): danh từ giống cái die Dame đổi mạo từ thành 'der älteren Dame'. 3. 'anrufen' (gọi điện cho ai) đòi hỏi tân ngữ ở Cách 4 (Akkusativ): danh từ giống đực der Kollege (mein-) đổi thành 'meinen besten Kollegen'. 4. 'gehören' (thuộc về ai) luôn đòi hỏi tân ngữ ở Cách 3 (Dativ): danh từ giống đực der Trainer đổi mạo từ thành 'dem neuen Trainer'.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "untersuchen",
                                        "right": "den kranken Patienten im Behandlungszimmer"
                                },
                                {
                                        "left": "helfen",
                                        "right": "der älteren Dame beim Überqueren der Straße"
                                },
                                {
                                        "left": "anrufen",
                                        "right": "meinen besten Kollegen im Büro"
                                },
                                {
                                        "left": "gehören",
                                        "right": "dem neuen Trainer der Fußballmannschaft"
                                }
                        ],
                        "translation": "1. untersuchen: khám cho bệnh nhân bị ốm ở trong phòng khám bệnh | 2. helfen: giúp đỡ bà cụ lớn tuổi khi băng qua đường | 3. anrufen: gọi điện thoại cho người đồng nghiệp thân nhất của tôi ở văn phòng | 4. gehören: thuộc về vị huấn luyện viên mới của đội bóng đá."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 65: Ghép hành động và địa điểm (Cột Trái) với cụm giới từ chỉ hướng Wohin? hoặc vị trí Wo? (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Phân biệt hướng di chuyển Wohin? (Akkusativ) vs. Vị trí tĩnh Wo? (Dativ): 1. gehen chỉ hành động di chuyển (Wohin?) đòi hỏi in + Akkusativ: danh từ giống đực der Supermarkt đổi thành 'in den Supermarkt'. 2. einkaufen chỉ hành động tại chỗ (Wo?) đòi hỏi in + Dativ: danh từ giống đực der Supermarkt đổi in + dem thành 'im Supermarkt'. 3. fahren chỉ hành động di chuyển (Wohin?) đòi hỏi in + Akkusativ: danh từ giống cái die Schule giữ nguyên mạo từ 'in die Schule'. 4. lernen chỉ hoạt động tại chỗ (Wo?) đòi hỏi in + Dativ: danh từ giống trung das Klassenzimmer đổi in + dem thành 'im Klassenzimmer'.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "gehen + der Supermarkt (Wohin?)",
                                        "right": "in den Supermarkt"
                                },
                                {
                                        "left": "einkaufen + der Supermarkt (Wo?)",
                                        "right": "im Supermarkt"
                                },
                                {
                                        "left": "fahren + die Schule (Wohin?)",
                                        "right": "in die Schule"
                                },
                                {
                                        "left": "lernen + das Klassenzimmer (Wo?)",
                                        "right": "im Klassenzimmer"
                                }
                        ],
                        "translation": "1. gehen + der Supermarkt (Wohin?): đi vào trong siêu thị | 2. einkaufen + der Supermarkt (Wo?): mua sắm ở trong siêu thị | 3. fahren + die Schule (Wohin?): đi/lái xe đến trường học | 4. lernen + das Klassenzimmer (Wo?): học bài ở trong phòng học."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 66: Ghép danh từ theo Giống (Cột Trái) với câu biến đổi sang Tân ngữ Cách 4 tương ứng (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Quy tắc biến đổi mạo từ từ Cách 1 (Nominativ) sang Cách 4 (Akkusativ): 1. Giống đực (Maskulinum): Là giống DUY NHẤT bị biến đổi mạo từ sang đuôi -en (der -> den, ein -> einen): Er kauft den Stuhl / einen Stift. 2. Giống cái (Femininum): Mạo từ giữ nguyên dạng đuôi -e giống như Nominativ (die, meine): Ich suche die Lampe / meine Brille. 3. Giống trung (Neutrum): Mạo từ giữ nguyên dạng gốc giống như Nominativ (das, kein): Sie hat das Handy / kein Geld. 4. Số nhiều (Plural): Mạo từ giữ nguyên dạng giống như Nominativ (die, eure): Wir brauchen die Stifte / eure Taschen.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Maskulinum: der Stuhl / ein Stift",
                                        "right": "Er kauft den Stuhl / einen Stift."
                                },
                                {
                                        "left": "Femininum: die Lampe / meine Brille",
                                        "right": "Ich suche die Lampe / meine Brille."
                                },
                                {
                                        "left": "Neutrum: das Handy / kein Geld",
                                        "right": "Sie hat das Handy / kein Geld."
                                },
                                {
                                        "left": "Plural: die Stifte / eure Taschen",
                                        "right": "Wir brauchen die Stifte / eure Taschen."
                                }
                        ],
                        "translation": "1. Maskulinum: Anh ấy mua chiếc ghế / một chiếc bút. | 2. Femininum: Tôi đang tìm chiếc đèn / cặp kính của tôi. | 3. Neutrum: Cô ấy có chiếc điện thoại di động / không có tiền. | 4. Plural: Chúng tôi cần những chiếc bút / những chiếc túi của các bạn."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 67: Nối Tình huống ở vế đầu (Cột Trái) với Hoạt động dùng động từ khuyết thiếu phù hợp (Cột Phải):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Ghép nối dựa trên sự hòa hợp chủ ngữ và ngữ nghĩa của Modalverb: 1. Chủ ngữ 'Ich' tương ứng với cách chia 'kann ich' (làm ca muộn nên buổi sáng có thể ngủ dậy muộn). 2. Chủ ngữ 'Mein Sohn' (ngôi er) bị ốm tương ứng với sự cấm đoán 'darf er nicht' (bị ốm nên không được phép đến trường để tránh lây bệnh). 3. Câu hỏi với chủ ngữ 'ihr' đi liền với vế 'oder müsst ihr' (hỏi các bạn được nghỉ hay phải có mặt ở công ty lúc 8 giờ). 4. Chủ ngữ 'Frau Klein' (ngôi sie) làm thư ký tương ứng với năng lực chuyên môn 'sie kann sehr schnell E-Mails schreiben'.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Ich arbeite heute im Spätdienst,",
                                        "right": "deshalb kann ich am Morgen bis 9.00 Uhr schlafen."
                                },
                                {
                                        "left": "Mein Sohn ist heute leider krank,",
                                        "right": "deshalb darf er heute nicht in die Schule gehen."
                                },
                                {
                                        "left": "Habt ihr morgen frei,",
                                        "right": "oder müsst ihr um 8.00 Uhr in der Firma sein?"
                                },
                                {
                                        "left": "Frau Klein arbeitet als Sekretärin im Büro,",
                                        "right": "und sie kann sehr schnell E-Mails schreiben."
                                }
                        ],
                        "translation": "1. Hôm nay tôi làm ca muộn, vì vậy buổi sáng tôi có thể ngủ đến 9 giờ. | 2. Hôm nay con trai tôi không may bị ốm, vì vậy cháu không được phép đến trường. | 3. Ngày mai các bạn được nghỉ, hay các bạn phải có mặt ở công ty lúc 8 giờ? | 4. Bà Klein làm thư ký ở văn phòng, và bà ấy có thể gõ email rất nhanh."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 68: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Nachts [1] die Taxifahrer sehr vorsichtig [2].' (Gợi ý: 'Ban đêm các tài xế taxi phải lái xe rất cẩn thận.')",
                "options": null,
                "correct_answer": "müssen / fahren",
                "explanation": "Động từ khuyết thiếu müssen chia cho danh từ số nhiều die Taxifahrer là müssen ở vị trí số 2; động từ fahren ở dạng nguyên mẫu đứng cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "müssen / fahren",
                                "müssen/fahren",
                                "muessen / fahren",
                                "muessen/fahren"
                        ],
                        "display_frame": "Nachts [1] die Taxifahrer sehr vorsichtig [2].",
                        "translation": "Ban đêm các tài xế taxi phải lái xe rất cẩn thận."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 69: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Kellner [1] das Essen nhanh an den Tisch [2].' (Gợi ý: 'Người bồi bàn có thể mang thức ăn nhanh đến bàn.')",
                "options": null,
                "correct_answer": "kann / bringen",
                "explanation": "Động từ können chia cho ngôi thứ ba số ít der Kellner là kann ở vị trí số 2; động từ bringen giữ nguyên mẫu ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "kann / bringen",
                                "kann/bringen"
                        ],
                        "display_frame": "Der Kellner [1] das Essen schnell an den Tisch [2].",
                        "translation": "Người bồi bàn có thể mang thức ăn nhanh đến bàn."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'In der Universitätsbibliothek [1] man nicht laut [2].' (Gợi ý: 'Trong thư viện trường đại học người ta không được phép nói to.')",
                "options": null,
                "correct_answer": "darf / sprechen",
                "explanation": "Đại từ bất định man đi với dạng chia ngôi thứ 3 số ít: dürfen đổi thành darf; động từ sprechen nguyên mẫu đứng cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "darf / sprechen",
                                "darf/sprechen"
                        ],
                        "display_frame": "In der Universitätsbibliothek [1] man nicht laut [2].",
                        "translation": "Trong thư viện trường đại học người ta không được phép nói to."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 71: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Trainer [1] morgen ein wichtiges Fußballtraining [2].' (Gợi ý: 'Ngày mai huấn luyện viên muốn dẫn dắt một buổi tập bóng đá quan trọng.')",
                "options": null,
                "correct_answer": "will / leiten",
                "explanation": "Động từ wollen chia cho der Trainer (er) là will ở vị trí số 2; động từ nguyên mẫu leiten (hoặc organisieren/machen) đứng ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "will / leiten",
                                "will/leiten",
                                "will / machen",
                                "will/machen",
                                "will / organisieren",
                                "will/organisieren"
                        ],
                        "display_frame": "Der Trainer [1] morgen ein wichtiges Fußballtraining [2].",
                        "translation": "Ngày mai huấn luyện viên muốn dẫn dắt một buổi tập bóng đá quan trọng."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 72: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Patient mit Fieber [1] täglich viel Wasser [2].' (Gợi ý: 'Người bệnh nhân bị sốt nên uống nhiều nước mỗi ngày.')",
                "options": null,
                "correct_answer": "soll / trinken",
                "explanation": "Động từ sollen truyền đạt lời khuyên y tế, chia cho der Patient (er) là soll; động từ nguyên mẫu trinken đứng ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "soll / trinken",
                                "soll/trinken"
                        ],
                        "display_frame": "Der Patient mit Fieber [1] täglich viel Wasser [2].",
                        "translation": "Người bệnh nhân bị sốt nên uống nhiều nước mỗi ngày."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 73: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Heute Nachmittag [1] der Hausmann frische Lebensmittel [2].' (Gợi ý: 'Chiều nay người đàn ông nội trợ muốn mua thực phẩm tươi.')",
                "options": null,
                "correct_answer": "möchte / einkaufen",
                "explanation": "Động từ möchten chia cho ngôi er (der Hausmann) là möchte; động từ tách einkaufen giữ nguyên mẫu viết liền ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "möchte / einkaufen",
                                "möchte/einkaufen",
                                "moechte / einkaufen",
                                "moechte/einkaufen",
                                "möchte / kaufen",
                                "möchte/kaufen"
                        ],
                        "display_frame": "Heute Nachmittag [1] der Hausmann frische Lebensmittel [2].",
                        "translation": "Chiều nay người đàn ông nội trợ muốn mua thực phẩm tươi."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Die Floristin [1] wunderschöne Blumen an die Kunden [2].' (Gợi ý: 'Nữ thợ hoa phải giao những bông hoa tuyệt đẹp cho khách hàng.')",
                "options": null,
                "correct_answer": "muss / liefern",
                "explanation": "Động từ müssen chia cho die Floristin (sie) là muss; động từ liefern (hoặc verkaufen) giữ nguyên mẫu ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "muss / liefern",
                                "muss/liefern",
                                "muss / verkaufen",
                                "muss/verkaufen"
                        ],
                        "display_frame": "Die Floristin [1] wunderschöne Blumen an die Kunden [2].",
                        "translation": "Nữ thợ hoa phải giao những bông hoa tuyệt đẹp cho khách hàng."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Im Sprachzentrum [1] die Schüler fleißig Deutsch [2].' (Gợi ý: 'Ở trung tâm ngôn ngữ các học viên có thể học tiếng Đức chăm chỉ.')",
                "options": null,
                "correct_answer": "können / lernen",
                "explanation": "Chủ ngữ die Schüler là số nhiều nên können giữ nguyên; động từ lernen đứng ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "können / lernen",
                                "können/lernen",
                                "koennen / lernen",
                                "koennen/lernen"
                        ],
                        "display_frame": "Im Sprachzentrum [1] die Schüler fleißig Deutsch [2].",
                        "translation": "Ở trung tâm ngôn ngữ các học viên có thể học tiếng Đức chăm chỉ."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 76: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Die Programmiererin [1] einen neuen Laptop für ihre Arbeit [2].' (Gợi ý: 'Nữ lập trình viên muốn mua một chiếc máy tính xách tay mới cho công việc.')",
                "options": null,
                "correct_answer": "will / kaufen",
                "explanation": "Động từ wollen chia cho ngôi sie là will ở vị trí số 2; động từ kaufen đứng ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "will / kaufen",
                                "will/kaufen",
                                "möchte / kaufen",
                                "möchte/kaufen"
                        ],
                        "display_frame": "Die Programmiererin [1] einen neuen Laptop für ihre Arbeit [2].",
                        "translation": "Nữ lập trình viên muốn mua một chiếc máy tính xách tay mới cho công việc."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Nach der langen Nachtschicht [1] der Krankenpfleger ruhig [2].' (Gợi ý: 'Sau ca trực đêm dài người nam điều dưỡng được phép ngủ yên tĩnh.')",
                "options": null,
                "correct_answer": "darf / schlafen",
                "explanation": "Động từ dürfen chia cho der Krankenpfleger là darf ở vị trí 2; động từ schlafen giữ nguyên mẫu ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "darf / schlafen",
                                "darf/schlafen",
                                "kann / schlafen",
                                "kann/schlafen"
                        ],
                        "display_frame": "Nach der langen Nachtschicht [1] der Krankenpfleger ruhig [2].",
                        "translation": "Sau ca trực đêm dài người nam điều dưỡng được phép ngủ yên tĩnh."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 78: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Koch bereitet köstliche Gerichte in der ___ zu.'",
                "options": null,
                "correct_answer": "Küche",
                "explanation": "Danh từ chỉ nơi làm việc của đầu bếp là die Küche (in der Küche = trong nhà bếp).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der Koch bereitet köstliche Gerichte in der Küche zu.",
                        "accepted_answers": [
                                "Küche",
                                "Kueche",
                                "küche",
                                "kueche"
                        ],
                        "hint_vi": "Người đầu bếp chuẩn bị các món ăn ngon trong nhà bếp.",
                        "translation": "Người đầu bếp chuẩn bị các món ăn ngon trong nhà bếp."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 79: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Studentin besucht am Nachmittag eine Vorlesung an der ___.'",
                "options": null,
                "correct_answer": "Universität",
                "explanation": "Nơi học tập của sinh viên đại học là die Universität (an der Universität = tại trường đại học).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Die Studentin besucht am Nachmittag eine Vorlesung an der Universität.",
                        "accepted_answers": [
                                "Universität",
                                "Universitaet",
                                "universität",
                                "universitaet",
                                "Uni",
                                "uni"
                        ],
                        "hint_vi": "Nữ sinh viên tham dự một buổi giảng tại trường đại học vào buổi chiều.",
                        "translation": "Nữ sinh viên tham dự một buổi giảng tại trường đại học vào buổi chiều."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 80: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Verkäufer berät die Kunden freundlich im ___.'",
                "options": null,
                "correct_answer": "Schuhgeschäft",
                "explanation": "Cửa hàng bán giày dép là das Schuhgeschäft (im Schuhgeschäft).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der Verkäufer berät die Kunden freundlich im Schuhgeschäft.",
                        "accepted_answers": [
                                "Schuhgeschäft",
                                "Schuhgeschaeft",
                                "schuhgeschäft",
                                "schuhgeschaeft"
                        ],
                        "hint_vi": "Người bán hàng tư vấn khách hàng thân thiện ở trong cửa hàng giày.",
                        "translation": "Người bán hàng tư vấn khách hàng thân thiện ở trong cửa hàng giày."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 81: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Friseurin macht eine sehr schöne moderne Frisur im ___.'",
                "options": null,
                "correct_answer": "Friseursalon",
                "explanation": "Tiệm làm tóc là der Friseursalon (im Friseursalon).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Die Friseurin macht eine sehr schöne moderne Frisur im Friseursalon.",
                        "accepted_answers": [
                                "Friseursalon",
                                "friseursalon"
                        ],
                        "hint_vi": "Nữ thợ làm tóc làm một kiểu tóc hiện đại rất đẹp trong tiệm làm tóc.",
                        "translation": "Nữ thợ làm tóc làm một kiểu tóc hiện đại rất đẹp trong tiệm làm tóc."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 82: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Auf der ___ müssen alle Arbeiter einen Schutzhelm tragen.'",
                "options": null,
                "correct_answer": "Baustelle",
                "explanation": "Công trường xây dựng là die Baustelle (auf der Baustelle).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Auf der Baustelle müssen alle Arbeiter einen Schutzhelm tragen.",
                        "accepted_answers": [
                                "Baustelle",
                                "baustelle"
                        ],
                        "hint_vi": "Trên công trường tất cả công nhân phải đội mũ bảo hộ.",
                        "translation": "Trên công trường tất cả công nhân phải đội mũ bảo hộ."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 83: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Trainer leitet das Training für die Mannschaft im ___.'",
                "options": null,
                "correct_answer": "Stadion",
                "explanation": "Sân vận động thể thao là das Stadion (im Stadion).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der Trainer leitet das Training für die Mannschaft im Stadion.",
                        "accepted_answers": [
                                "Stadion",
                                "stadion"
                        ],
                        "hint_vi": "Huấn luyện viên điều hành buổi tập cho đội bóng ở sân vận động.",
                        "translation": "Huấn luyện viên điều hành buổi tập cho đội bóng ở sân vận động."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 84: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Sekretär schreibt wichtige E-Mails an seinem ___.'",
                "options": null,
                "correct_answer": "Computer",
                "explanation": "Thiết bị văn phòng để gõ email là der Computer (am Computer / an seinem Computer).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der Sekretär schreibt wichtige E-Mails an seinem Computer.",
                        "accepted_answers": [
                                "Computer",
                                "computer"
                        ],
                        "hint_vi": "Nam thư ký viết những email quan trọng trên máy tính của mình.",
                        "translation": "Nam thư ký viết những email quan trọng trên máy tính của mình."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 85: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Viele Ausländer lernen gemeinsam Deutsch im ___.'",
                "options": null,
                "correct_answer": "Sprachzentrum",
                "explanation": "Trung tâm ngoại ngữ là das Sprachzentrum (im Sprachzentrum).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Viele Ausländer lernen gemeinsam Deutsch im Sprachzentrum.",
                        "accepted_answers": [
                                "Sprachzentrum",
                                "sprachzentrum"
                        ],
                        "hint_vi": "Nhiều người nước ngoài cùng nhau học tiếng Đức ở trung tâm ngoại ngữ.",
                        "translation": "Nhiều người nước ngoài cùng nhau học tiếng Đức ở trung tâm ngoại ngữ."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 86: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Krankenschwester misst die Temperatur für den ___.'",
                "options": null,
                "correct_answer": "Patienten",
                "explanation": "Người bệnh nhân ở Cách 4 (Akkusativ N-Deklination) là den Patienten.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Die Krankenschwester misst die Temperatur für den Patienten.",
                        "accepted_answers": [
                                "Patienten",
                                "Patient",
                                "patienten",
                                "patient"
                        ],
                        "hint_vi": "Nữ y tá đo nhiệt độ cho người bệnh nhân.",
                        "translation": "Nữ y tá đo nhiệt độ cho người bệnh nhân."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 87: Dịch câu sau sang tiếng Đức: 'Nam nhân viên bán hàng tư vấn khách hàng rất thân thiện trong siêu thị.'",
                "options": null,
                "correct_answer": "Der Verkäufer berät die Kunden sehr freundlich im Supermarkt.",
                "explanation": "Nam nhân viên bán hàng là Der Verkäufer; động từ beraten biến âm a -> ä (berät) đi với Akkusativ (die Kunden); ở trong siêu thị là im Supermarkt.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Der Verkäufer berät die Kunden sehr freundlich im Supermarkt.",
                                "Der Verkäufer berät im Supermarkt die Kunden rất freundlich.",
                                "Im Supermarkt berät der Verkäufer die Kunden sehr freundlich.",
                                "Der Verkaeufer beraet die Kunden sehr freundlich im Supermarkt.",
                                "Der Verkäufer berät Kunden sehr freundlich im Supermarkt."
                        ],
                        "translation": "Nam nhân viên bán hàng tư vấn khách hàng rất thân thiện trong siêu thị."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 88: Dịch câu sau sang tiếng Đức: 'Nữ thợ làm tóc có thể tạo một kiểu tóc rất đẹp.'",
                "options": null,
                "correct_answer": "Die Friseurin kann eine sehr schöne Frisur machen.",
                "explanation": "Nữ thợ làm tóc là Die Friseurin; có thể là kann (Modalverb ở vị trí số 2); động từ nguyên mẫu machen đứng ở cuối câu.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Die Friseurin kann eine sehr schöne Frisur machen.",
                                "Die Friseurin kann eine sehr schöne Frisur kreieren.",
                                "Die Friseurin kann eine sehr schoene Frisur machen.",
                                "Eine sehr schöne Frisur kann die Friseurin machen.",
                                "Die Friseurin kann eine schöne Frisur machen."
                        ],
                        "translation": "Nữ thợ làm tóc có thể tạo một kiểu tóc rất đẹp."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 89: Dịch câu sau sang tiếng Đức: 'Các học sinh phải nộp bài tập về nhà cho thầy giáo.'",
                "options": null,
                "correct_answer": "Die Schüler müssen dem Lehrer die Hausaufgaben abgeben.",
                "explanation": "Chủ ngữ die Schüler số nhiều đi với müssen; thầy giáo là người nhận ở Dativ (dem Lehrer); bài tập về nhà là Akkusativ (die Hausaufgaben); abgeben đứng cuối câu.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Die Schüler müssen dem Lehrer die Hausaufgaben abgeben.",
                                "Die Schüler müssen die Hausaufgaben dem Lehrer abgeben.",
                                "Die Schueler muessen dem Lehrer die Hausaufgaben abgeben.",
                                "Dem Lehrer müssen die Schüler die Hausaufgaben abgeben.",
                                "Die Schüler müssen dem Lehrer ihre Hausaufgaben abgeben."
                        ],
                        "translation": "Các học sinh phải nộp bài tập về nhà cho thầy giáo."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 90: Dịch câu sau sang tiếng Đức: 'Ở trong bệnh viện, người ta không được phép hút thuốc lá.'",
                "options": null,
                "correct_answer": "Im Krankenhaus darf man nicht rauchen.",
                "explanation": "Ở bệnh viện là Im Krankenhaus; đại từ man chia động từ darf ở vị trí 2; không được phép hút thuốc là darf ... nicht rauchen.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Im Krankenhaus darf man nicht rauchen.",
                                "Man darf im Krankenhaus nicht rauchen.",
                                "In dem Krankenhaus darf man nicht rauchen.",
                                "Im Krankenhaus darf man keine Zigaretten rauchen."
                        ],
                        "translation": "Ở trong bệnh viện, người ta không được phép hút thuốc lá."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 91: Dịch câu sau sang tiếng Đức: 'Người phụ nữ nội trợ chuẩn bị bữa tối cho cả gia đình trong bếp.'",
                "options": null,
                "correct_answer": "Die Hausfrau bereitet das Abendessen für die Familie in der Küche zu.",
                "explanation": "Người phụ nữ nội trợ là Die Hausfrau; chuẩn bị là zubereiten (động từ tách: bereitet ... zu); cho gia đình là für die Familie (Akkusativ); trong bếp là in der Küche (Dativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Die Hausfrau bereitet das Abendessen für die Familie in der Küche zu.",
                                "In der Küche bereitet die Hausfrau das Abendessen für die Familie zu.",
                                "Die Hausfrau bereitet in der Küche das Abendessen für die Familie zu.",
                                "Die Hausfrau kocht das Abendessen für die Familie in der Küche.",
                                "Die Hausfrau bereitet das Abendessen fuer die Familie in der Kueche zu."
                        ],
                        "translation": "Người phụ nữ nội trợ chuẩn bị bữa tối cho cả gia đình trong bếp."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 92: Dịch câu sau sang tiếng Đức: 'Vị huấn luyện viên giúp đỡ các cầu thủ trẻ trong sân vận động.'",
                "options": null,
                "correct_answer": "Der Trainer hilft den jungen Spielern im Stadion.",
                "explanation": "Huấn luyện viên là Der Trainer; động từ helfen biến âm e -> i thành hilft và bắt buộc đi với Dativ số nhiều (den jungen Spielern); trong sân vận động là im Stadion.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Der Trainer hilft den jungen Spielern im Stadion.",
                                "Im Stadion hilft der Trainer den jungen Spielern.",
                                "Der Trainer hilft im Stadion den jungen Spielern.",
                                "Der Trainer hilft jungen Spielern im Stadion."
                        ],
                        "translation": "Vị huấn luyện viên giúp đỡ các cầu thủ trẻ trong sân vận động."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 93: Dịch câu sau sang tiếng Đức: 'Nam thư ký gọi điện cho khách hàng vì một cuộc hẹn quan trọng.'",
                "options": null,
                "correct_answer": "Der Sekretär ruft den Kunden für einen wichtigen Termin an.",
                "explanation": "Nam thư ký là Der Sekretär; động từ anrufen là động từ tách (ruft ... an) đi với Akkusativ (den Kunden); vì một cuộc hẹn là für einen wichtigen Termin (Akkusativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Der Sekretär ruft den Kunden für einen wichtigen Termin an.",
                                "Für einen wichtigen Termin ruft der Sekretär den Kunden an.",
                                "Der Sekretaer ruft den Kunden fuer einen wichtigen Termin an.",
                                "Der Sekretär ruft für einen wichtigen Termin den Kunden an."
                        ],
                        "translation": "Nam thư ký gọi điện cho khách hàng vì một cuộc hẹn quan trọng."
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 94: Dịch câu sau sang tiếng Việt: 'Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.'",
                "options": null,
                "correct_answer": "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo",
                "explanation": "muss ... abholen = phải đón; ihre Tochter = con gái của cô ấy; vom Kindergarten = từ trường mẫu giáo.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo",
                                "Lúc 16 giờ 30 Paula phải đón con gái của mình từ trường mẫu giáo",
                                "Vào 16 giờ 30 Paula phải đón con gái của cô ấy từ trường mẫu giáo",
                                "Vào 16 giờ 30 phút Paula phải đón con gái của cô ấy từ trường mẫu giáo",
                                "Vào lúc 16h30 Paula phải đón con gái từ nhà trẻ về",
                                "Lúc 16h30 Paula phải đón con gái từ trường mẫu giáo",
                                "Vào 16h30 Paula phải đón con gái của cô ấy từ trường mẫu giáo",
                                "Vào lúc 16 giờ 30 Paula phải đón con gái từ trường mẫu giáo",
                                "Lúc 16h30 phút Paula phải đón con gái từ trường mẫu giáo",
                                "Lúc 4 giờ rưỡi chiều Paula phải đón con gái của cô ấy từ trường mầm non",
                                "Vào 4 giờ rưỡi chiều Paula phải đón con gái từ trường mẫu giáo",
                                "Lúc 16 giờ 30 phút Paula phải đón con gái từ trường mầm non",
                                "Lúc 16 giờ 30 Paula phải đón con gái từ nhà trẻ",
                                "Vào 16 giờ 30 Paula phải đón con gái mình từ trường mầm non",
                                "Vào 16 giờ 30 Paula phải đón con gái từ trường mẫu giáo",
                                "Lúc 16h30 Paula phải đón con gái của mình từ trường mẫu giáo",
                                "16h30 Paula phải đón con gái từ trường mẫu giáo",
                                "16 giờ 30 Paula phải đón con gái của mình từ trường mẫu giáo",
                                "Paula phải đón con gái của mình từ trường mẫu giáo lúc 16 giờ 30",
                                "Paula phải đón con gái từ trường mẫu giáo lúc 16h30",
                                "Paula phải đón con gái của cô ấy từ trường mầm non lúc 16 giờ 30"
                        ],
                        "translation": "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 95: Dịch câu sau sang tiếng Việt: 'Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen.'",
                "options": null,
                "correct_answer": "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                "explanation": "ist Lehrer von Beruf = làm nghề giáo viên; hat Ferien = có kỳ nghỉ; kann bis 7 Uhr schlafen = có thể ngủ đến 7 giờ.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy có kì nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy được nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy được nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ tới 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ đến 7 giờ",
                                "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ đến 7 giờ",
                                "Frank Müller là một giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller làm giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Nghề của Frank Müller là giáo viên nhưng hôm nay anh ấy được nghỉ lễ và có thể ngủ tới 7 giờ",
                                "Nghề của Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay ông ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller làm nghề giáo viên nhưng hôm nay ông ấy được nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7h",
                                "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7h",
                                "Frank Müller là giáo viên, nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên, nhưng hôm nay anh ấy được nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller làm nghề giáo viên, nhưng hôm nay anh ấy có kì nghỉ và có thể ngủ đến 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy được nghỉ phép và có thể ngủ đến 7 giờ"
                        ],
                        "translation": "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 96: Dịch câu sau sang tiếng Việt: 'Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen.'",
                "options": null,
                "correct_answer": "Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                "explanation": "wichtig für sie = quan trọng đối với cô ấy; muss ihre Kunden oft anrufen = thường xuyên phải gọi điện cho khách hàng của mình.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "Chiếc điện thoại rất quan trọng với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "chiếc điện thoại đó rất quan trọng với cô ấy, vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "Chiếc điện thoại đó rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "Chiếc điện thoại đó rất quan trọng với cô ấy vì cô ấy thường phải gọi điện cho khách hàng của mình",
                                "Điện thoại rất quan trọng với cô ấy bởi vì cô ấy phải gọi điện cho khách hàng của mình thường xuyên",
                                "Điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho khách hàng của mình",
                                "Cái điện thoại rất quan trọng đối với cô ấy vì cô ấy thường phải gọi cho khách hàng",
                                "Cái điện thoại đó rất quan trọng với cô ấy vì cô ấy thường xuyên phải gọi điện cho khách hàng của mình",
                                "Chiếc điện thoại rất quan trọng với cô ấy vì cô ấy phải thường xuyên gọi điện cho khách hàng",
                                "Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường phải gọi điện cho khách hàng",
                                "Điện thoại rất quan trọng đối với cô ấy vì cô ấy thường phải gọi cho khách hàng của mình",
                                "Chiếc điện thoại rất quan trọng với cô ấy bởi vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "Điện thoại rất quan trọng với cô ấy vì cô ấy thường xuyên phải gọi điện cho khách hàng",
                                "Cái điện thoại rất quan trọng với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "Chiếc điện thoại đó rất quan trọng đối với cô ấy vì cô ấy phải thường xuyên gọi điện cho khách hàng",
                                "Điện thoại rất quan trọng cho cô ấy vì cô ấy thường xuyên phải gọi điện cho khách hàng của mình",
                                "Chiếc điện thoại rất quan trọng cho cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
                                "Chiếc điện thoại này rất quan trọng với cô ấy vì cô ấy thường xuyên phải gọi điện cho khách hàng của mình"
                        ],
                        "translation": "Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 97: Dịch câu sau sang tiếng Việt: 'Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining.'",
                "options": null,
                "correct_answer": "Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá",
                "explanation": "bringt sein Auto in die Werkstatt = mang ô tô vào xưởng sửa chữa (Akkusativ); geht zum Fußballtraining = đi đến buổi tập bóng đá (Dativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá",
                                "Vào buổi chiều ông Müller đem chiếc xe hơi của mình đến xưởng sửa chữa và sau đó đi đến buổi tập đá bóng",
                                "vào buổi chiều ông Müller đem chiếc xe hơi của mình đến xưởng sửa chữa và sau đó đi đến buổi tập đá bóng",
                                "Buổi chiều ông Müller đưa xe hơi vào xưởng sửa chữa và sau đó đi tập đá bóng",
                                "Vào buổi chiều anh Müller đem ô tô tới xưởng sửa xe rồi đi tập bóng đá",
                                "Buổi chiều ông Müller mang ô tô vào xưởng sửa chữa rồi đi đến buổi tập bóng đá",
                                "Vào buổi chiều ông Müller mang ô tô vào xưởng sửa chữa và sau đó đi đến buổi tập bóng đá",
                                "Vào buổi chiều ông Müller mang chiếc ô tô của mình đến xưởng sửa chữa rồi sau đó đi tập bóng đá",
                                "Buổi chiều ông Müller mang xe hơi của mình vào xưởng sửa chữa và sau đó đi đến buổi tập bóng đá",
                                "Vào buổi chiều ông Müller đem ô tô của mình đến xưởng sửa chữa rồi đi tập đá bóng",
                                "Vào buổi chiều ông Müller đưa chiếc ô tô của mình đến gara rồi sau đó đi tập bóng đá",
                                "Buổi chiều ông Müller đem chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá",
                                "Buổi chiều ông Müller mang xe vào xưởng sửa chữa và sau đó đi tập bóng đá",
                                "Vào buổi chiều ông Müller đem xe hơi vào xưởng sửa chữa và sau đó đi đến buổi tập bóng đá",
                                "Buổi chiều ông Müller đem xe hơi của mình đến xưởng sửa chữa rồi sau đó đi tập đá bóng",
                                "Vào buổi chiều ông Müller mang xe của mình tới xưởng sửa xe rồi đi tập bóng đá",
                                "Ông Müller vào buổi chiều mang ô tô vào xưởng sửa chữa rồi sau đó đi tập bóng đá",
                                "Vào buổi chiều ông Müller mang ô tô đến tiệm sửa xe rồi sau đó đi đến buổi tập bóng đá"
                        ],
                        "translation": "Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 98: Dịch câu sau sang tiếng Việt: 'Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität.'",
                "options": null,
                "correct_answer": "Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học",
                "explanation": "vormittags = vào buổi sáng; Schüler an einer Schule = học sinh tại một trường học; nachmittags = vào buổi chiều; Studenten an der Universität = sinh viên tại trường đại học.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học",
                                "Cô giáo dạy học sinh ở trường học vào buổi sáng và dạy sinh viên ở trường đại học vào buổi chiều",
                                "cô giáo dạy học sinh ở trường học vào buổi sáng và dạy sinh viên ở trường đại học vào buổi chiều",
                                "Cô giáo dạy học sinh tại một trường học vào buổi sáng và dạy sinh viên ở trường đại học vào buổi chiều",
                                "Cô giáo dạy học sinh tại trường học vào buổi sáng và dạy sinh viên tại trường đại học vào buổi chiều",
                                "Cô giáo dạy học sinh ở một trường học vào buổi sáng và dạy sinh viên ở trường đại học vào buổi chiều",
                                "Nữ giáo viên dạy học sinh ở một ngôi trường vào buổi sáng và dạy sinh viên tại trường đại học vào buổi chiều",
                                "Buổi sáng cô giáo giảng dạy học sinh ở trường phổ thông và buổi chiều dạy sinh viên ở trường đại học",
                                "Nữ giáo viên buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học",
                                "Buổi sáng cô giáo dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học",
                                "Vào buổi sáng cô giáo dạy học sinh ở trường học và vào buổi chiều dạy sinh viên ở trường đại học",
                                "Cô giáo buổi sáng giảng dạy học sinh ở một trường học và buổi chiều giảng dạy sinh viên ở trường đại học",
                                "Nữ giáo viên dạy học sinh ở trường học vào buổi sáng và dạy sinh viên ở trường đại học vào buổi chiều",
                                "Cô giáo buổi sáng dạy học sinh ở trường và buổi chiều dạy sinh viên ở trường đại học",
                                "Cô giáo buổi sáng dạy học sinh tại trường học và buổi chiều dạy sinh viên tại trường đại học",
                                "Buổi sáng cô giáo dạy học sinh ở trường học và buổi chiều dạy sinh viên tại trường đại học",
                                "Cô giáo dạy học sinh ở trường vào buổi sáng và dạy sinh viên ở đại học vào buổi chiều",
                                "Nữ giáo viên buổi sáng dạy học sinh ở trường học và buổi chiều dạy sinh viên ở đại học"
                        ],
                        "translation": "Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 99: Dịch câu sau sang tiếng Việt: 'Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat.'",
                "options": null,
                "correct_answer": "Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối",
                "explanation": "kann ... fernsehen = có thể xem tivi; im Wohnzimmer = ở trong phòng khách; das Abendessen machen = làm bữa tối.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi cô ấy đã làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi cô ấy làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi trong phòng khách sau khi nấu bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi trong phòng khách sau khi cô ấy đã nấu bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi đã làm bữa tối",
                                "Từ 20h đến 22h Paula có thể xem tivi ở phòng khách sau khi làm bữa tối",
                                "Từ 20 giờ đến 22 giờ Paula có thể xem tivi trong phòng khách sau khi nấu bữa tối",
                                "Từ 20 giờ đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi cô ấy làm bữa tối",
                                "Từ 8 giờ đến 10 giờ tối Paula có thể xem truyền hình trong phòng khách sau khi làm xong bữa tối",
                                "Từ 8 giờ đến 10 giờ tối Paula có thể xem tivi ở trong phòng khách sau khi nấu bữa tối",
                                "Từ 8h đến 10h tối Paula có thể xem tivi ở phòng khách sau khi làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem TV trong phòng khách sau khi làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi cô ấy nấu xong bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi hoàn thành bữa tối",
                                "Paula có thể xem tivi ở phòng khách từ 20 đến 22 giờ sau khi làm bữa tối",
                                "Paula có thể xem tivi trong phòng khách từ 20 đến 22 giờ sau khi cô ấy đã làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem ti vi ở phòng khách sau khi cô ấy đã làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách, sau khi cô ấy đã làm bữa tối",
                                "từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi cô ấy đã làm bữa tối",
                                "từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau đó cô ấy đã làm bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau đó cô ấy đã làm bữa tối"
                        ],
                        "translation": "Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối"
                }
        },
        {
                "type": "dich_cau_dv",
                "question": "Câu 100: Dịch câu sau sang tiếng Việt: 'Der Friseur schneidet meinem Bruder im Friseursalon die Haare.'",
                "options": null,
                "correct_answer": "Người thợ cắt tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc",
                "explanation": "Câu kết hợp cả Dativ và Akkusativ: meinem Bruder (Wem? -> Dativ: cho anh trai tôi), im Friseursalon (Wo? -> Dativ: ở trong tiệm làm tóc), die Haare (Was? -> Akkusativ: mái tóc).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Người thợ cắt tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc",
                                "thợ cắt tóc cắt tóc cho em trai tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho em trai tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho anh trai tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho anh trai tôi trong tiệm làm tóc",
                                "Thợ làm tóc cắt tóc cho anh trai của tôi tại tiệm cắt tóc",
                                "Thợ làm tóc cắt tóc cho em trai của tôi tại tiệm cắt tóc",
                                "Người thợ làm tóc đang cắt tóc cho anh tôi ở trong salon tóc",
                                "Người thợ làm tóc cắt tóc cho em tôi ở trong salon tóc",
                                "Người thợ cắt tóc cắt tóc cho em trai tôi ở trong tiệm làm tóc",
                                "Người thợ cắt tóc cắt tóc cho em trai tôi ở tiệm cắt tóc",
                                "Người thợ cắt tóc cắt tóc cho anh trai tôi tại tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho em trai tôi tại tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho anh trai tôi tại tiệm cắt tóc",
                                "Người thợ làm tóc cắt tóc cho anh trai tôi ở tiệm làm tóc",
                                "Người thợ làm tóc cắt tóc cho em trai tôi ở tiệm làm tóc",
                                "Thợ làm tóc cắt tóc cho anh trai tôi ở trong salon tóc",
                                "Thợ làm tóc cắt tóc cho em trai tôi ở trong salon tóc",
                                "Thợ cắt tóc cắt tóc cho anh trai tôi ở trong quán cắt tóc",
                                "Thợ cắt tóc cắt tóc cho em trai tôi ở trong quán cắt tóc",
                                "Người thợ cắt tóc đang cắt tóc cho anh trai tôi ở tiệm cắt tóc",
                                "Người thợ cắt tóc đang cắt tóc cho em trai tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho anh tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho em tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho anh trai của tôi ở tiệm cắt tóc",
                                "Thợ cắt tóc cắt tóc cho em trai của tôi ở tiệm cắt tóc"
                        ],
                        "translation": "Người thợ cắt tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc"
                }
        }
]

    exercises = []
    for ex in raw_exercises:
        ex_type = ex["type"]
        question = ex["question"]
        corr = ex["correct_answer"]
        exp = ex["explanation"]
        pts = ex["exp_reward"]
        opts = json.dumps(ex["options"], ensure_ascii=False) if ex["options"] else None
        extra = ex.get("extra_data")
        extra_json = json.dumps(extra, ensure_ascii=False) if extra else None
        exercises.append((
            lesson_id, ex_type, question, opts, corr, exp, pts, extra_json
        ))

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công Bài 7: 'Beruf - Modalverben - Artikelwörter in Akkusativ' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_7()
