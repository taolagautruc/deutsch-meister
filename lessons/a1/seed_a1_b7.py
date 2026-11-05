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
                    ⚠️ <b>LƯU Ý CỐT LÕI:</b> Khi nói nghề nghiệp với cấu trúc <code>sein + [Nghề]</code> hoặc <code>arbeiten als + [Nghề]</code>, <b>TUYỆT ĐỐI KHÔNG DÙNG MẠO TỪ ein/eine</b>! Nói: <i>„Ich bin Lehrer.“</i> hoặc <i>„Ich arbeite als Programmierer.“</i> (Không nói: <i>„Ich bin ein Lehrer.“</i>).
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
                        <p class="text-slate-700"><b>für</b> (cho), <b>ohne</b> (không có), <b>durch</b> (xuyên qua), <b>um</b> (xung quanh/vào lúc), <b>gegen</b> (chống lại/khoảng).</p>
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
                "example": "Sie lernt fleißig und möchte eine Mechatronikerin werden.",
                "example_vi": "Cô ấy học tập chăm chỉ và muốn trở thành một nữ thợ cơ khí."
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
                "example_vi": "Anna là một nữ học sinh chăm chỉ tại trường chuyên."
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
                "example": "Der Arzt untersucht den kranken Patient im Behandlungszimmer.",
                "example_vi": "Bác sĩ khám cho bệnh nhân bị ốm ở trong phòng khám bệnh."
        }
]

    vocabularies = []
    for item in vocab_raw:
        vocabularies.append((
            lesson_id,
            f"{item['article']} {item['word']}",
            item["article"],
            item["meaning"],
            item["example"]
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
                "question": "Câu 1: Chọn phương án đúng để hoàn thành cuộc hội thoại: 'Was machen Sie beruflich, Frau Lindner? — Ich arbeite ___ Programmiererin bei einer IT-Firma.'",
                "options": [
                        "wie eine",
                        "als",
                        "von",
                        "für"
                ],
                "correct_answer": "als",
                "explanation": "Khi dùng động từ 'arbeiten' để giới thiệu nghề nghiệp, tiếng Đức dùng giới từ 'als' + danh từ nghề nghiệp không có mạo từ (Ich arbeite als Programmiererin).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "als"
                        ],
                        "translation": "Công việc chuyên môn của bà là gì, thưa bà Lindner? — Tôi làm nghề lập trình viên tại một công ty công nghệ thông tin."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 2: Chọn câu đúng ngữ pháp tiếng Đức khi giới thiệu nghề nghiệp của anh trai:",
                "options": [
                        "Mein Bruder ist einen Lehrer von Beruf.",
                        "Mein Bruder ist Lehrer von Beruf.",
                        "Mein Bruder arbeitet von Beruf Lehrer.",
                        "Mein Bruder ist der Lehrer beruflich."
                ],
                "correct_answer": "Mein Bruder ist Lehrer von Beruf.",
                "explanation": "Với cấu trúc '[Chủ ngữ] + sein + [Nghề nghiệp] + von Beruf', danh từ chỉ nghề nghiệp đứng một mình không dùng mạo từ ein/einen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Mein Bruder ist Lehrer von Beruf."
                        ],
                        "translation": "Anh trai tôi làm nghề giáo viên."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 3: Cặp danh từ nghề nghiệp Nam – Nữ nào dưới đây được viết ĐÚNG CHÍNH TẢ 100%?",
                "options": [
                        "der Koch -> die Kochin / der Arzt -> die Arztin",
                        "der Koch -> die Köchin / der Arzt -> die Ärztin",
                        "der Koch -> die Köcherin / der Arzt -> die Ärztinn",
                        "der Hausmann -> die Hausmännin / der Krankenpfleger -> die Krankenpfleger"
                ],
                "correct_answer": "der Koch -> die Köchin / der Arzt -> die Ärztin",
                "explanation": "Hai danh từ der Koch và der Arzt khi chuyển sang giống cái (Femininum) vừa thêm hậu tố -in vừa phải thêm dấu Umlaut trên nguyên âm gốc: die Köchin và die Ärztin.",
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
                "explanation": "KFZ-Mechatroniker là thợ cơ khí ô tô; công việc là repariert Autos (sửa ô tô) và nơi làm việc (Wo? + Dativ) là in einer Werkstatt (die Werkstatt -> in einer Werkstatt).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "repariert / in einer Werkstatt"
                        ],
                        "translation": "Một người thợ cơ khí ô tô sửa chữa xe hơi và làm việc ở trong một xưởng sửa chữa.",
                        "dynamic_profession_quiz": true
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 5: Chọn giới từ và mạo từ đúng: 'Wo arbeitet deine Schwester? — Sie ist Floristin und arbeitet ___ Blumengeschäft neben dem Bahnhof.'",
                "options": [
                        "ins",
                        "in der",
                        "im",
                        "auf dem"
                ],
                "correct_answer": "im",
                "explanation": "Câu hỏi Wo? (làm việc ở đâu) đòi hỏi Cách 3 (Dativ). das Blumengeschäft mang giống trung nên in + dem viết tắt là im Blumengeschäft.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "im"
                        ],
                        "translation": "Chị gái của bạn làm việc ở đâu? — Chị ấy là người bán hoa và làm việc ở trong cửa hàng hoa bên cạnh nhà ga."
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
                        "translation": "Paula Rausch làm nghề lập trình viên. Mỗi buổi sáng cô ấy đã phải thức dậy lúc 6 giờ 15 phút.",
                        "dynamic_modalverb_schedule_quiz": true
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 7: Chọn phương án đúng: 'Kinder, heute habt ihr Ferien! ___ ihr bis 9 Uhr schlafen?'",
                "options": [
                        "Könnt",
                        "Kannst",
                        "Können",
                        "Kannt"
                ],
                "correct_answer": "Könnt",
                "explanation": "Chủ ngữ là ihr (các con/các bạn), động từ können giữ nguyên nguyên âm ö và chia đuôi -t thành könnt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Könnt"
                        ],
                        "translation": "Các con ơi, hôm nay các con được nghỉ lễ! Các con có thể ngủ đến 9 giờ không?"
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 8: Chọn câu đúng trật tự từ ngữ pháp tiếng Đức:",
                "options": [
                        "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholt.",
                        "Um 16.30 Uhr holt Paula ihre Tochter vom Kindergarten müssen ab.",
                        "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.",
                        "Um 16.30 Uhr muss abholen Paula ihre Tochter vom Kindergarten."
                ],
                "correct_answer": "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.",
                "explanation": "Khi có động từ khuyết thiếu muss đứng ở vị trí số 2, động từ tách abholen không tách nữa mà giữ nguyên dạng nguyên mẫu (Infinitiv) đứng ở cuối câu.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen."
                        ],
                        "translation": "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 9: Chọn cặp từ đúng điền vào câu: 'Bei ihrer Arbeit braucht Petra ___ Computer und ___ großen Schreibtisch.'",
                "options": [
                        "ein / ein",
                        "einen / einen",
                        "einem / einem",
                        "den / dem"
                ],
                "correct_answer": "einen / einen",
                "explanation": "Động từ brauchen (cần cái gì) luôn đi với tân ngữ trực tiếp ở Cách 4 (Akkusativ). Cả der Computer và der Schreibtisch đều mang giống đực (Maskulinum), nên mạo từ ein đổi thành einen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "einen / einen"
                        ],
                        "translation": "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 10: Chọn phương án đúng: 'Herr Weber arbeitet heute von zu Hause. Er braucht ___ Anzug, sondern nur ___ Laptop.'",
                "options": [
                        "kein / ein",
                        "keinen / einen",
                        "keinem / một",
                        "keine / eine"
                ],
                "correct_answer": "keinen / einen",
                "explanation": "Cả der Anzug và der Laptop đều là danh từ giống đực làm tân ngữ trực tiếp (Akkusativ) sau động từ braucht, nên chia là keinen Anzug và einen Laptop.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "keinen / einen"
                        ],
                        "translation": "Hôm nay ông Weber làm việc tại nhà. Ông ấy không cần bộ vest nào cả mà chỉ cần một chiếc máy tính xách tay."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 11: Chọn phương án đúng: 'Die Sekretärin muss heute Vormittag ___ Chef und ___ Kunden anrufen.'",
                "options": [
                        "ihren / ihre",
                        "ihrem / ihren",
                        "ihre / ihren",
                        "ihr / ihre"
                ],
                "correct_answer": "ihren / ihre",
                "explanation": "Động từ anrufen (gọi điện cho ai) đi với Cách 4 (Akkusativ). Với der Chef (giống đực), mạo từ sở hữu của cô ấy (ihr-) đổi thành ihren Chef; với die Kunden (số nhiều) ở Akkusativ thì giữ nguyên đuôi -e là ihre Kunden.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ihren / ihre"
                        ],
                        "translation": "Nữ thư ký sáng nay phải gọi điện cho ông sếp của cô ấy và các khách hàng của cô ấy."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 12: Chọn cặp mạo từ đúng điền vào 2 câu sau: '1. Die Ärztin untersucht ___ kranken Mann. — 2. Die Krankenschwester hilft ___ kranken Mann.'",
                "options": [
                        "den / den",
                        "dem / den",
                        "den / dem",
                        "der / dem"
                ],
                "correct_answer": "den / dem",
                "explanation": "Động từ untersuchen (khám bệnh cho ai) đòi hỏi Cách 4 (Akkusativ) -> den kranken Mann. Ngược lại, động từ helfen (giúp đỡ ai) bắt buộc đi với Cách 3 (Dativ) -> dem kranken Mann.",
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
                "question": "Câu 13: Chọn phương án đúng hoàn thành câu: '___ seiner Arbeit im Krankenhaus hat der Arzt wenig Pause, aber die Arbeit ist sehr wichtig ___ seine Patienten.'",
                "options": [
                        "Für / bei",
                        "Bei / für",
                        "Mit / von",
                        "Zu / ohne"
                ],
                "correct_answer": "Bei / für",
                "explanation": "Cụm 'Trong công việc của mình' dùng Bei seiner Arbeit (bei + Dativ), còn 'quan trọng đối với ai' dùng wichtig für + Akkusativ (für seine Patienten).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Bei / für"
                        ],
                        "translation": "Trong công việc của mình ở bệnh viện, vị bác sĩ có ít thời gian nghỉ giải lao, nhưng công việc đó rất quan trọng đối với các bệnh nhân của ông ấy."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 14: Chọn phương án đúng điền vào 2 chỗ trống: 'Um 8.30 Uhr bringt Frank seine Tochter ___ Kindergarten (Wohin?), und um 16.30 Uhr holt Paula die Tochter ___ Kindergarten (Woher?) ab.'",
                "options": [
                        "im / in den",
                        "in den / vom",
                        "zum / im",
                        "in dem / von der"
                ],
                "correct_answer": "in den / vom",
                "explanation": "Đưa vào trường mẫu giáo (bringen -> câu hỏi Wohin? + Akkusativ) với danh từ giống đực der Kindergarten là in den Kindergarten. Đón từ trường mẫu giáo về (abholen -> von + Dativ) là vom Kindergarten.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "in den / vom"
                        ],
                        "translation": "Lúc 8 giờ 30 phút Frank đưa con gái vào trường mẫu giáo, và lúc 16 giờ 30 phút Paula đón con gái từ trường mẫu giáo về."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 15: Chọn cặp từ đúng: 'Herr Müller bringt sein Auto ___ Werkstatt (Wohin?). Dort repariert der Mechatroniker das Auto ___ Werkstatt (Wo?).'",
                "options": [
                        "in die / in der",
                        "in der / in die",
                        "zur / in die",
                        "in eine / in eine"
                ],
                "correct_answer": "in die / in der",
                "explanation": "Danh từ die Werkstatt mang giống cái (Femininum). Khi di chuyển vào xưởng (Wohin? + Akkusativ) dùng in die Werkstatt; khi làm việc ở bên trong xưởng (Wo? + Dativ) dùng in der Werkstatt.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "in die / in der"
                        ],
                        "translation": "Ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa. Ở đó người thợ cơ khí sửa chiếc ô tô ở trong xưởng."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 16: Chọn phương án đúng: 'Um 19 Uhr bringt die Mutter ihren Sohn ___ Bett. Um 20 Uhr liegt er schon ___ Bett und schläft.'",
                "options": [
                        "im / ins",
                        "ins / im",
                        "in dem / in das",
                        "ans / am"
                ],
                "correct_answer": "ins / im",
                "explanation": "Đưa lên giường (bringen — di chuyển Wohin?) dùng in + das = ins Bett (Akkusativ). Nằm ngủ trên giường (liegen/schlafen — vị trí tĩnh Wo?) dùng in + dem = im Bett (Dativ).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ins / im"
                        ],
                        "translation": "Lúc 19 giờ người mẹ đưa con trai lên giường ngủ. Lúc 20 giờ cậu bé đã nằm trên giường và ngủ."
                }
        },
        {
                "type": "trac_nghiem",
                "question": "Câu 17: Chọn phương án đúng ngữ pháp: 'Der Chef kauft ___ Sekretärin (die Sekretärin) ___ neuen Computer (der Computer).'",
                "options": [
                        "die / einen",
                        "der / einen",
                        "der / một",
                        "einer / den"
                ],
                "correct_answer": "der / einen",
                "explanation": "Trong câu có 2 tân ngữ: Người nhận lợi ích (Wem? cho nữ thư ký) chia ở Cách 3 (Dativ) -> der Sekretärin; Vật được mua (Was? một chiếc máy tính mới) chia ở Cách 4 (Akkusativ) -> einen neuen Computer.",
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
                "question": "Câu 19: Điền giới từ chỉ nghề nghiệp thích hợp vào chỗ trống: 'Mein Onkel arbeitet seit fünf Jahren ___ Taxifahrer in Hamburg.'",
                "options": null,
                "correct_answer": "als",
                "explanation": "Cụm arbeiten als + [Nghề nghiệp] dùng để nói làm nghề gì.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "als"
                        ],
                        "translation": "Chú của tôi làm nghề tài xế taxi ở Hamburg từ 5 năm nay."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 20: Điền danh từ nghề nghiệp dạng Nữ (Femininum) tương ứng với 'der Arzt' vào chỗ trống: 'Meine Tante arbeitet im Krankenhaus. Sie ist ___ von Beruf.'",
                "options": null,
                "correct_answer": "Ärztin",
                "explanation": "der Arzt khi chuyển sang danh từ nghề nghiệp nữ phải thêm dấu Umlaut và đuôi -in thành Ärztin.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Ärztin",
                                "Aerztin"
                        ],
                        "translation": "Dì của tôi làm việc ở trong bệnh viện. Dì ấy làm nghề nữ bác sĩ."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 21: Điền danh từ nghề nghiệp dạng Nữ (Femininum) tương ứng với 'der Koch' vào chỗ trống: 'Frau Bui kocht sehr gut in einem großen Restaurant. Sie arbeitet als ___.'",
                "options": null,
                "correct_answer": "Köchin",
                "explanation": "der Koch chuyển sang giống cái thêm Umlaut o -> ö và -in thành Köchin.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "Köchin",
                                "Koechin"
                        ],
                        "translation": "Bà Bùi nấu ăn rất ngon trong một nhà hàng lớn. Bà ấy làm nghề nữ đầu bếp."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 22: Điền dạng chia đúng của động từ khuyết thiếu 'müssen' vào chỗ trống: 'Ich habe morgen eine Prüfung, deshalb ___ ich heute Abend viel lernen.'",
                "options": null,
                "correct_answer": "muss",
                "explanation": "Ngôi thứ nhất số ít (ich) của động từ müssen là muss.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "muss"
                        ],
                        "translation": "Ngày mai tôi có một kỳ thi, vì vậy tối nay tôi phải học bài nhiều."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 23: Điền dạng chia đúng của động từ khuyết thiếu 'müssen' vào chỗ trống: 'Wann ___ du morgen früh zur Arbeit fahren, Lukas?'",
                "options": null,
                "correct_answer": "musst",
                "explanation": "Ngôi thứ hai số ít (du) của động từ müssen là musst.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "musst"
                        ],
                        "translation": "Sáng sớm mai bạn phải đi làm lúc mấy giờ thế, Lukas?"
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 24: Điền dạng chia đúng của động từ khuyết thiếu 'können' vào chỗ trống: 'Herr Müller hat heute Ferien. Er ___ bis 8 Uhr schlafen.'",
                "options": null,
                "correct_answer": "kann",
                "explanation": "Ngôi thứ ba số ít (er) của động từ können là kann (không có đuôi -t).",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "kann"
                        ],
                        "translation": "Ông Müller hôm nay có kỳ nghỉ. Ông ấy có thể ngủ đến 8 giờ."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 25: Điền dạng chia đúng của động từ khuyết thiếu 'möchten' vào chỗ trống: 'Anna ist Schülerin, aber später ___ sie Medizin an der Universität studieren.'",
                "options": null,
                "correct_answer": "möchte",
                "explanation": "Ngôi thứ ba số ít (sie - cô ấy) của möchten là möchte.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "möchte",
                                "moechte"
                        ],
                        "translation": "Anna là học sinh, nhưng sau này cô ấy muốn học ngành Y ở trường đại học."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 26: Điền dạng nguyên mẫu của động từ tách 'aufstehen' vào cuối câu có Modalverb: 'Am Sonntag müssen wir nicht früh ___.'",
                "options": null,
                "correct_answer": "aufstehen",
                "explanation": "Khi câu đã có động từ khuyết thiếu müssen ở vị trí số 2, động từ tách aufstehen giữ nguyên dạng nguyên mẫu viết liền ở cuối câu.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "aufstehen"
                        ],
                        "translation": "Vào Chủ nhật chúng tôi không phải thức dậy sớm."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 27: Điền mạo từ không xác định đúng ở Cách 4 (Akkusativ) vào chỗ trống: 'Für seine Arbeit im Büro braucht mein Bruder ___ schnellen Laptop.'",
                "options": null,
                "correct_answer": "einen",
                "explanation": "Động từ brauchen đòi hỏi Cách 4 (Akkusativ). der Laptop mang giống đực nên ein đổi thành einen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "einen"
                        ],
                        "translation": "Cho công việc của mình ở văn phòng, anh trai tôi cần một chiếc máy tính xách tay nhanh."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 28: Điền mạo từ phủ định 'kein' đúng ở Cách 4 (Akkusativ) vào chỗ trống: 'Ich trinke meinen Tee bitte ohne Zucker, ich brauche ___ Löffel.'",
                "options": null,
                "correct_answer": "keinen",
                "explanation": "der Löffel mang giống đực, làm tân ngữ trực tiếp (Akkusativ) sau brauche, nên kein đổi thành keinen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "keinen"
                        ],
                        "translation": "Tôi uống trà không đường, tôi không cần cái thìa nào cả."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 29: Điền mạo từ sở hữu của ngôi 'er' (sein-) đúng ở Cách 4 (Akkusativ) vào chỗ trống: 'Der Programmierer ruft ___ Chef im Büro an.'",
                "options": null,
                "correct_answer": "seinen",
                "explanation": "Động từ anrufen đi với Cách 4 (Akkusativ). der Chef mang giống đực nên gốc sở hữu sein- của er đổi thành seinen.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "seinen"
                        ],
                        "translation": "Lập trình viên gọi điện cho ông sếp của anh ấy ở văn phòng."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 30: Điền mạo từ xác định đúng (phân biệt Wohin? Akkusativ) vào chỗ trống: 'Jeden Morgen um 8 Uhr bringt Frau Rausch ihren Sohn in ___ Kindergarten.'",
                "options": null,
                "correct_answer": "den",
                "explanation": "Hành động đưa con đến trường mẫu giáo (bringen -> câu hỏi Wohin?) dùng Cách 4 (Akkusativ): der Kindergarten -> in den Kindergarten.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "den"
                        ],
                        "translation": "Mỗi buổi sáng lúc 8 giờ bà Rausch đưa con trai mình vào trường mẫu giáo."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 31: Điền giới từ thu gọn (in + das) chỉ hướng di chuyển Wohin? (Akkusativ) vào chỗ trống: 'Es ist schon 22 Uhr. Die Kinder müssen jetzt ___ Bett gehen.'",
                "options": null,
                "correct_answer": "ins",
                "explanation": "Đi lên giường ngủ (Wohin? + Akkusativ) với danh từ giống trung das Bett dùng in + das gộp thành ins Bett.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "ins"
                        ],
                        "translation": "Đã 22 giờ rồi. Bọn trẻ bây giờ phải đi lên giường ngủ."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 32: Điền mạo từ xác định đúng ở Cách 3 (Dativ) sau động từ 'helfen': 'Die Sekretärin hilft ___ neuen Praktikanten bei der Arbeit.'",
                "options": null,
                "correct_answer": "dem",
                "explanation": "Động từ helfen luôn đi với Cách 3 (Dativ), nên der Praktikant chuyển thành dem neuen Praktikanten.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "dem"
                        ],
                        "translation": "Nữ thư ký giúp đỡ nam thực tập sinh mới trong công việc."
                }
        },
        {
                "type": "dien_khuyet",
                "question": "Câu 33: Điền dạng chia đúng của động từ 'unterrichten' theo chủ ngữ vào chỗ trống: 'Herr Müller ist Lehrer von Beruf und ___ Mathematik an einer Schule.'",
                "options": null,
                "correct_answer": "unterrichtet",
                "explanation": "Động từ unterrichten có gốc kết thúc bằng -t (unterricht-), nên ở ngôi thứ 3 số ít (er) phải thêm -e- trước -t thành unterrichtet.",
                "exp_reward": 15,
                "extra_data": {
                        "accepted_answers": [
                                "unterrichtet"
                        ],
                        "translation": "Ông Müller làm nghề giáo viên và giảng dạy môn Toán tại một trường học."
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
                        "translation": "der Taxifahrer / die Taxifahrerin"
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
                        "translation": "der Hausmann / die Hausfrau"
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
                        "translation": "der Kellner / die Kellnerin"
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
                        "translation": "der Sekretär / die Sekretärin"
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
                        "translation": "Schüler an einer Schule unterrichten"
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
                        "translation": "Computerprogramme schreiben"
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
                        "translation": "die Tochter vom Kindergarten abholen"
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
                        "translation": "das Auto in die Werkstatt bringen"
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
                        "translation": "zum Fußballtraining gehen"
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
                        "translation": "Kunden im Büro anrufen"
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
                        "translation": "müssen — können — möchten"
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
                        "translation": "im Schuhgeschäft Schuhe verkaufen"
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 58: Nối Nghề nghiệp với Hoạt động đặc trưng tương ứng:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Nghề giáo viên giảng dạy học sinh, bác sĩ khám bệnh nhân, thợ cơ khí sửa ô tô, lập trình viên viết phần mềm.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Lehrer / die Lehrerin",
                                        "right": "unterrichtet Schüler (giảng dạy học sinh)"
                                },
                                {
                                        "left": "der Arzt / die Ärztin",
                                        "right": "untersucht Patienten (khám cho bệnh nhân)"
                                },
                                {
                                        "left": "der KFZ-Mechatroniker",
                                        "right": "repariert Autos (sửa chữa xe ô tô)"
                                },
                                {
                                        "left": "der Programmierer",
                                        "right": "schreibt Computerprogramme (viết chương trình máy tính)"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 59: Nối Nghề nghiệp với Hoạt động đặc trưng tương ứng (Phần 2):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Thợ làm tóc cắt tóc, nhân viên bán hàng bán giày dép, thợ hoa bán hoa, đầu bếp nấu món ăn ngon.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Friseur / die Friseurin",
                                        "right": "schneidet Haare (cắt tóc)"
                                },
                                {
                                        "left": "der Verkäufer / die Verkäuferin",
                                        "right": "verkauft Schuhe (bán giày dép)"
                                },
                                {
                                        "left": "der Florist / die Floristin",
                                        "right": "verkauft Blumen (bán hoa tươi)"
                                },
                                {
                                        "left": "der Koch / die Köchin",
                                        "right": "kocht leckere Speisen (nấu những món ăn ngon)"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 60: Nối Nghề nghiệp với Nơi làm việc chuẩn ở Dativ:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Giáo viên làm việc ở trường học/trung tâm ngoại ngữ, bác sĩ và y tá ở bệnh viện, thợ cơ khí ở xưởng, thợ tóc ở tiệm làm tóc.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Lehrer",
                                        "right": "arbeitet an einer Schule / im Sprachzentrum"
                                },
                                {
                                        "left": "die Ärztin und der Krankenpfleger",
                                        "right": "arbeiten im Krankenhaus"
                                },
                                {
                                        "left": "der KFZ-Mechatroniker",
                                        "right": "arbeitet in einer Werkstatt"
                                },
                                {
                                        "left": "die Friseurin",
                                        "right": "arbeitet im Friseursalon"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 61: Nối Danh từ Nghề nghiệp Nam với Dạng Nữ đặc biệt:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Các trường hợp biến đổi đặc biệt sang giống cái: thêm Umlaut (Ärztin, Köchin), đổi gốc (Hausfrau), và danh xưng truyền thống (Krankenschwester).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Arzt (nam bác sĩ)",
                                        "right": "die Ärztin (thêm Umlaut ä + -in)"
                                },
                                {
                                        "left": "der Koch (nam đầu bếp)",
                                        "right": "die Köchin (thêm Umlaut ö + -in)"
                                },
                                {
                                        "left": "der Hausmann (nam nội trợ)",
                                        "right": "die Hausfrau (đổi gốc sang -frau)"
                                },
                                {
                                        "left": "der Krankenpfleger (nam điều dưỡng)",
                                        "right": "die Krankenschwester / die Krankenpflegerin"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 62: Nối Chủ ngữ với Dạng chia của Động từ khuyết thiếu müssen và können:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Quy tắc chia Modalverben: ngôi 1 và 3 số ít đổi nguyên âm và không có đuôi; ngôi du thêm -st; ngôi ihr giữ nguyên âm gốc và thêm đuôi -t.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "ich / er / sie / es (với müssen)",
                                        "right": "muss (đổi ü -> u, không có đuôi)"
                                },
                                {
                                        "left": "ich / er / sie / es (với können)",
                                        "right": "kann (đổi ö -> a, không có đuôi)"
                                },
                                {
                                        "left": "du (với müssen & können)",
                                        "right": "musst / kannst (thêm đuôi -st)"
                                },
                                {
                                        "left": "ihr (với müssen & können)",
                                        "right": "müsst / könnt (giữ Umlaut, thêm đuôi -t)"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 63: Nối Câu hỏi Nghề nghiệp & Nơi làm việc với Câu trả lời chuẩn:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Cặp câu hỏi và câu trả lời hoàn chỉnh tương ứng về nghề nghiệp, nơi làm việc và nhiệm vụ công việc.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Was sind Sie von Beruf?",
                                        "right": "Ich bin Sekretärin von Beruf."
                                },
                                {
                                        "left": "Als was arbeitet dein Bruder?",
                                        "right": "Er arbeitet als Programmierer."
                                },
                                {
                                        "left": "Wo arbeitet Frau Wagner?",
                                        "right": "Sie arbeitet im Blumengeschäft."
                                },
                                {
                                        "left": "Was muss Petra im Büro machen?",
                                        "right": "Sie muss ihre Kunden anrufen."
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 64: Phân biệt Động từ đi với Cách 4 (Akkusativ) vs. Động từ đi với Cách 3 (Dativ):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Động từ Akkusativ chỉ tân ngữ trực tiếp (cần, tìm, gọi, khám); Động từ Dativ quy định người nhận tác động (giúp đỡ, cảm ơn, thích, thuộc về).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "brauchen (cần) & suchen (tìm)",
                                        "right": "luôn đi với Cách 4 (Akkusativ: einen Computer)"
                                },
                                {
                                        "left": "anrufen (gọi điện) & untersuchen (khám)",
                                        "right": "luôn đi với Cách 4 (Akkusativ: den Patienten)"
                                },
                                {
                                        "left": "helfen (giúp đỡ) & danken (cảm ơn)",
                                        "right": "luôn đi với Cách 3 (Dativ: dem Arzt)"
                                },
                                {
                                        "left": "gefallen (làm ai thích) & gehören (thuộc về)",
                                        "right": "luôn đi với Cách 3 (Dativ: meiner Mutter)"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 65: Đối chiếu trực tiếp giữa Hướng di chuyển Wohin? (Akkusativ) và Vị trí tĩnh Wo? (Dativ):",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Wohin? (hướng di chuyển) dùng Akkusativ (in den Kindergarten, in die Werkstatt, ins Bett, ins Büro); Wo? (vị trí tĩnh) dùng Dativ (im Kindergarten, in der Werkstatt, im Bett, im Büro).",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "in den Kindergarten bringen (Wohin?)",
                                        "right": "im Kindergarten spielen (Wo?)"
                                },
                                {
                                        "left": "in die Werkstatt fahren (Wohin?)",
                                        "right": "in der Werkstatt reparieren (Wo?)"
                                },
                                {
                                        "left": "ins Bett gehen (Wohin?)",
                                        "right": "im Bett schlafen (Wo?)"
                                },
                                {
                                        "left": "ins Büro kommen (Wohin?)",
                                        "right": "im Büro arbeiten (Wo?)"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 66: Biến đổi Từ hạn định từ Nominativ sang Akkusativ:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Ở Cách 4 Akkusativ, chỉ duy nhất giống đực (der) biến đổi đuôi sang -en; giống cái, giống trung và số nhiều giữ nguyên dạng Nominativ.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "der Tisch / ein Computer (Maskulinum)",
                                        "right": "den Tisch / einen Computer (đổi sang đuôi -en)"
                                },
                                {
                                        "left": "die Tasche / meine Tochter (Femininum)",
                                        "right": "die Tasche / meine Tochter (giữ nguyên)"
                                },
                                {
                                        "left": "das Buch / kein Auto (Neutrum)",
                                        "right": "das Buch / kein Auto (giữ nguyên)"
                                },
                                {
                                        "left": "die Bücher / ihre Kunden (Plural)",
                                        "right": "die Bücher / ihre Kunden (giữ nguyên, không thêm -n)"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "noi_o",
                "question": "Câu 67: Nối Mốc thời gian với Hoạt động trong lịch trình của Paula Rausch & Frank Müller:",
                "options": null,
                "correct_answer": "Hoàn thành nối ô",
                "explanation": "Lịch trình hàng ngày thực tế của Paula Rausch và Frank Müller trong đoạn văn bài học.",
                "exp_reward": 20,
                "extra_data": {
                        "noi_o_pairs": [
                                {
                                        "left": "Paula: um 6.15 Uhr",
                                        "right": "muss sie aufstehen"
                                },
                                {
                                        "left": "Paula: um 16.30 Uhr",
                                        "right": "muss sie ihre Tochter vom Kindergarten abholen"
                                },
                                {
                                        "left": "Frank: bis 7.00 Uhr",
                                        "right": "kann er schlafen, weil er Ferien hat"
                                },
                                {
                                        "left": "Frank: um 12.30 Uhr",
                                        "right": "bringt er das Auto in die Werkstatt"
                                }
                        ],
                        "translation": "Nối các cặp tương ứng giữa 2 cột."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 68: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Um 6.15 Uhr [1] Paula [2].' (Gợi ý: 'Lúc 6 giờ 15 phút Paula phải thức dậy.')",
                "options": null,
                "correct_answer": "muss / aufstehen",
                "explanation": "Động từ khuyết thiếu müssen chia theo ngôi thứ 3 số ít (Paula) là muss đứng ở vị trí số 2; động từ tách aufstehen giữ nguyên mẫu viết liền ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "muss / aufstehen",
                                "muss/aufstehen"
                        ],
                        "display_frame": "Um 6.15 Uhr [1] Paula [2].",
                        "translation": "Lúc 6 giờ 15 phút Paula phải thức dậy."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 69: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Von 20 bis 22 Uhr [1] sie [2].' (Gợi ý: 'Từ 20 giờ đến 22 giờ cô ấy có thể xem tivi.')",
                "options": null,
                "correct_answer": "kann / fernsehen",
                "explanation": "können chia cho ngôi sie (cô ấy) là kann ở vị trí số 2; động từ tách fernsehen giữ nguyên mẫu ở cuối câu.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "kann / fernsehen",
                                "kann/fernsehen"
                        ],
                        "display_frame": "Von 20 bis 22 Uhr [1] sie [2].",
                        "translation": "Từ 20 giờ đến 22 giờ cô ấy có thể xem tivi."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Um 16.30 Uhr muss sie ihre Tochter [1] Kindergarten [2].' (Gợi ý: 'Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo.')",
                "options": null,
                "correct_answer": "vom / abholen",
                "explanation": "Đón từ trường mẫu giáo dùng von + dem = vom Kindergarten; động từ abholen đứng nguyên mẫu ở cuối câu sau muss.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "vom / abholen",
                                "vom/abholen"
                        ],
                        "display_frame": "Um 16.30 Uhr muss sie ihre Tochter [1] Kindergarten [2].",
                        "translation": "Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 71: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Bei [1] Arbeit braucht Petra [2] Computer und einen großen Schreibtisch.' (Gợi ý: 'Trong công việc của mình, Petra cần một chiếc máy tính và một chiếc bàn làm việc lớn.')",
                "options": null,
                "correct_answer": "ihrer / einen",
                "explanation": "Sau giới từ Bei là Cách 3 (Dativ) với die Arbeit (giống cái) -> Bei ihrer Arbeit. Sau động từ braucht là Cách 4 (Akkusativ) với der Computer (giống đực) -> einen Computer.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "ihrer / einen",
                                "ihrer/einen"
                        ],
                        "display_frame": "Bei [1] Arbeit braucht Petra [2] Computer und einen großen Schreibtisch.",
                        "translation": "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 72: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Am Morgen bringt Frank die Tochter in [1] Kindergarten, und am Nachmittag spielt sie [2] Kindergarten.' (Gợi ý: 'Buổi sáng Frank đưa con gái vào trường mẫu giáo, và buổi chiều con bé chơi ở trong trường mẫu giáo.')",
                "options": null,
                "correct_answer": "den / im",
                "explanation": "Đưa vào trường mẫu giáo (Wohin? + Akkusativ) là in den Kindergarten; chơi ở trong trường mẫu giáo (Wo? + Dativ) là im Kindergarten.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "den / im",
                                "den/im"
                        ],
                        "display_frame": "Am Morgen bringt Frank die Tochter in [1] Kindergarten, und am Nachmittag spielt sie [2] Kindergarten.",
                        "translation": "Buổi sáng Frank đưa con gái vào trường mẫu giáo, và buổi chiều con bé chơi ở trong trường mẫu giáo."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 73: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Arzt untersucht [1] Patienten [2] Krankenhaus.' (Gợi ý: 'Vị bác sĩ khám cho người bệnh nhân ở trong bệnh viện.')",
                "options": null,
                "correct_answer": "den / im",
                "explanation": "untersuchen đi với Akkusativ (den Patienten), còn nơi chốn tĩnh Wo? với das Krankenhaus đi với Dativ (im Krankenhaus).",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "den / im",
                                "den/im"
                        ],
                        "display_frame": "Der Arzt untersucht [1] Patienten [2] Krankenhaus.",
                        "translation": "Vị bác sĩ khám cho người bệnh nhân ở trong bệnh viện."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Meine Schwester arbeitet als [1] und [2] sehr gut kochen.' (Gợi ý: 'Chị gái của tôi làm nghề nữ đầu bếp và có thể nấu ăn rất giỏi.')",
                "options": null,
                "correct_answer": "Köchin / kann",
                "explanation": "Nữ đầu bếp là Köchin; động từ können chia cho meine Schwester (sie) là kann.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Köchin / kann",
                                "Köchin/kann",
                                "Koechin / kann",
                                "Koechin/kann"
                        ],
                        "display_frame": "Meine Schwester arbeitet als [1] und [2] sehr gut kochen.",
                        "translation": "Chị gái của tôi làm nghề nữ đầu bếp và có thể nấu ăn rất giỏi."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Krankenpfleger gibt [1] Arzt [2] Kuli.' (Gợi ý: 'Người nam điều dưỡng đưa cho vị bác sĩ một chiếc bút bi.')",
                "options": null,
                "correct_answer": "dem / einen",
                "explanation": "Người nhận (Wem? cho bác sĩ) chia ở Cách 3 (Dativ) -> dem Arzt; vật được đưa (Was? một chiếc bút bi) chia ở Cách 4 (Akkusativ) -> einen Kuli.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "dem / einen",
                                "dem/einen"
                        ],
                        "display_frame": "Der Krankenpfleger gibt [1] Arzt [2] Kuli.",
                        "translation": "Người nam điều dưỡng đưa cho vị bác sĩ một chiếc bút bi."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 76: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Um 12.30 Uhr [1] er das Auto in [2] Werkstatt.' (Gợi ý: 'Lúc 12 giờ 30 phút anh ấy mang chiếc ô tô vào xưởng sửa chữa.')",
                "options": null,
                "correct_answer": "bringt / die",
                "explanation": "Động từ bringen chia ở ngôi er là bringt; mang vào xưởng (Wohin? + Akkusativ) với danh từ giống cái die Werkstatt là in die Werkstatt.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "bringt / die",
                                "bringt/die"
                        ],
                        "display_frame": "Um 12.30 Uhr [1] er das Auto in [2] Werkstatt.",
                        "translation": "Lúc 12 giờ 30 phút anh ấy mang chiếc ô tô vào xưởng sửa chữa."
                }
        },
        {
                "type": "dien_tao_cau",
                "question": "Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): '[1] ihr am Samstag [2] Büro arbeiten?' (Gợi ý: 'Các bạn có phải làm việc vào thứ Bảy ở trong văn phòng không?')",
                "options": null,
                "correct_answer": "Müsst / im",
                "explanation": "Câu hỏi đảo động từ khuyết thiếu müssen với chủ ngữ ihr là Müsst ihr ...?; làm việc ở trong văn phòng (Wo? + Dativ) là im Büro.",
                "exp_reward": 20,
                "extra_data": {
                        "accepted_answers": [
                                "Müsst / im",
                                "Müsst/im",
                                "müsst / im",
                                "müsst/im",
                                "Muesst / im",
                                "muesst / im"
                        ],
                        "display_frame": "[1] ihr am Samstag [2] Büro arbeiten?",
                        "translation": "Các bạn có phải làm việc vào thứ Bảy ở trong văn phòng không?"
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 78: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Paula Rausch ist 35 Jahre alt und arbeitet als ___.'",
                "options": null,
                "correct_answer": "Programmiererin",
                "explanation": "Danh từ chỉ nữ lập trình viên là die Programmiererin.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Paula Rausch ist fünfunddreißig Jahre alt und arbeitet als Programmiererin.",
                        "accepted_answers": [
                                "Programmiererin"
                        ],
                        "hint_vi": "Paula Rausch 35 tuổi và làm nghề nữ lập trình viên.",
                        "translation": "Paula Rausch 35 tuổi và làm nghề nữ lập trình viên."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 79: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der KFZ-Mechatroniker repariert Autos in einer ___.'",
                "options": null,
                "correct_answer": "Werkstatt",
                "explanation": "Danh từ die Werkstatt có nghĩa là xưởng sửa chữa (in einer Werkstatt).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der KFZ-Mechatroniker repariert Autos in einer Werkstatt.",
                        "accepted_answers": [
                                "Werkstatt"
                        ],
                        "hint_vi": "Người thợ cơ khí ô tô sửa chữa xe hơi ở trong một xưởng sửa chữa.",
                        "translation": "Người thợ cơ khí ô tô sửa chữa xe hơi ở trong một xưởng sửa chữa."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 80: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Arzt ___ jeden Tag viele Patienten im Krankenhaus.'",
                "options": null,
                "correct_answer": "untersucht",
                "explanation": "Động từ untersuchen (khám bệnh) chia ở ngôi thứ 3 số ít (der Arzt) là untersucht.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus.",
                        "accepted_answers": [
                                "untersucht"
                        ],
                        "hint_vi": "Vị bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện.",
                        "translation": "Vị bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 81: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Bei ihrer Arbeit braucht Petra ___ schnellen Computer und einen großen Schreibtisch.'",
                "options": null,
                "correct_answer": "einen",
                "explanation": "Sau động từ braucht (Akkusativ), mạo từ không xác định của der Computer là einen.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Bei ihrer Arbeit braucht Petra einen schnellen Computer und einen großen Schreibtisch.",
                        "accepted_answers": [
                                "einen"
                        ],
                        "hint_vi": "Trong công việc của mình, Petra cần một chiếc máy tính nhanh và một cái bàn làm việc lớn.",
                        "translation": "Trong công việc của mình, Petra cần một chiếc máy tính nhanh và một cái bàn làm việc lớn."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 82: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Um 16.30 Uhr muss sie ihre Tochter vom Kindergarten ___.'",
                "options": null,
                "correct_answer": "abholen",
                "explanation": "Động từ tách abholen đứng ở cuối câu ở dạng nguyên mẫu khi đi cùng muss.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Um sechzehn Uhr dreißig muss sie ihre Tochter vom Kindergarten abholen.",
                        "accepted_answers": [
                                "abholen"
                        ],
                        "hint_vi": "Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo.",
                        "translation": "Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 83: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Frank Müller ist ___ von Beruf und hat jetzt Ferien.'",
                "options": null,
                "correct_answer": "Lehrer",
                "explanation": "Danh từ chỉ nam giáo viên là der Lehrer (Er ist Lehrer von Beruf).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Frank Müller ist Lehrer von Beruf und hat jetzt Ferien.",
                        "accepted_answers": [
                                "Lehrer"
                        ],
                        "hint_vi": "Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ.",
                        "translation": "Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 84: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Floristin verkauft schöne Blumen im ___.'",
                "options": null,
                "correct_answer": "Blumengeschäft",
                "explanation": "Danh từ das Blumengeschäft có nghĩa là cửa hàng hoa (im Blumengeschäft).",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Die Floristin verkauft schöne Blumen im Blumengeschäft.",
                        "accepted_answers": [
                                "Blumengeschäft",
                                "Blumengeschaeft"
                        ],
                        "hint_vi": "Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa.",
                        "translation": "Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 85: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Sie muss ihre ___ im Büro oft anrufen.'",
                "options": null,
                "correct_answer": "Kunden",
                "explanation": "Danh từ số nhiều die Kunden có nghĩa là những khách hàng.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Sie muss ihre Kunden im Büro oft anrufen.",
                        "accepted_answers": [
                                "Kunden"
                        ],
                        "hint_vi": "Cô ấy thường xuyên phải gọi điện cho các khách hàng của mình ở trong văn phòng.",
                        "translation": "Cô ấy thường xuyên phải gọi điện cho các khách hàng của mình ở trong văn phòng."
                }
        },
        {
                "type": "nghe_dien",
                "question": "Câu 86: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Um 19 Uhr bringt der Vater seine Tochter ___ Bett.'",
                "options": null,
                "correct_answer": "ins",
                "explanation": "Cụm ins Bett bringen (in + das Bett — Wohin? Akkusativ) có nghĩa là đưa lên giường đi ngủ.",
                "exp_reward": 20,
                "extra_data": {
                        "audio_text": "Um neunzehn Uhr bringt der Vater seine Tochter ins Bett.",
                        "accepted_answers": [
                                "ins"
                        ],
                        "hint_vi": "Lúc 19 giờ người bố đưa con gái của mình lên giường đi ngủ.",
                        "translation": "Lúc 19 giờ người bố đưa con gái của mình lên giường đi ngủ."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 87: Dịch câu sau sang tiếng Đức: 'Bạn làm nghề gì? — Tôi làm nghề lập trình viên.'",
                "options": null,
                "correct_answer": "Was bist du von Beruf? Ich arbeite als Programmierer.",
                "explanation": "Hỏi nghề nghiệp thân mật dùng Was bist du von Beruf? hoặc Was machst du beruflich?; trả lời dùng Ich bin Programmierer hoặc Ich arbeite als Programmierer.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Was bist du von Beruf? Ich arbeite als Programmierer.",
                                "Was bist du von Beruf? Ich bin Programmierer.",
                                "Was bist du von Beruf? Ich bin Programmierer von Beruf.",
                                "Was machst du beruflich? Ich arbeite als Programmierer.",
                                "Was machst du beruflich? Ich bin Programmiererin.",
                                "Was machst du beruflich? Ich bin Programmierer."
                        ],
                        "translation": "Bạn làm nghề gì? — Tôi làm nghề lập trình viên."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 88: Dịch câu sau sang tiếng Đức: 'Lúc 7 giờ 15 phút cô ấy phải đi bằng xe buýt đến chỗ làm.'",
                "options": null,
                "correct_answer": "Um 7.15 Uhr muss sie mit dem Bus zur Arbeit fahren.",
                "explanation": "Động từ khuyết thiếu muss đứng ở vị trí số 2, động từ chính fahren đứng nguyên mẫu ở cuối câu; phương tiện mit dem Bus và đích đến zur Arbeit đều chia ở Dativ.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Um 7.15 Uhr muss sie mit dem Bus zur Arbeit fahren.",
                                "Um Viertel nach sieben muss sie mit dem Bus zur Arbeit fahren.",
                                "Sie muss um 7.15 Uhr mit dem Bus zur Arbeit fahren.",
                                "Um sieben Uhr fünfzehn muss sie mit dem Bus zur Arbeit fahren."
                        ],
                        "translation": "Lúc 7 giờ 15 phút cô ấy phải đi bằng xe buýt đến chỗ làm."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 89: Dịch câu sau sang tiếng Đức: 'Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn.'",
                "options": null,
                "correct_answer": "Bei ihrer Arbeit braucht Petra einen Computer und einen großen Schreibtisch.",
                "explanation": "Bei ihrer Arbeit chia ở Dativ; sau động từ braucht thì cả der Computer và der Schreibtisch đều chia ở Akkusativ (einen Computer und einen großen Schreibtisch).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Bei ihrer Arbeit braucht Petra einen Computer und einen großen Schreibtisch.",
                                "Petra braucht bei ihrer Arbeit einen Computer und einen großen Schreibtisch.",
                                "Für ihre Arbeit braucht Petra einen Computer und einen großen Schreibtisch."
                        ],
                        "translation": "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 90: Dịch câu sau sang tiếng Đức: 'Người thợ cơ khí sửa chữa ô tô ở trong một xưởng sửa chữa.'",
                "options": null,
                "correct_answer": "Der Mechatroniker repariert Autos in einer Werkstatt.",
                "explanation": "Tân ngữ trực tiếp Autos ở Akkusativ, còn nơi làm việc tĩnh in einer Werkstatt chia ở Dativ.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Der Mechatroniker repariert Autos in einer Werkstatt.",
                                "Der KFZ-Mechatroniker repariert Autos in einer Werkstatt.",
                                "Der Mechatroniker repariert das Auto in einer Werkstatt.",
                                "In einer Werkstatt repariert der KFZ-Mechatroniker Autos."
                        ],
                        "translation": "Người thợ cơ khí sửa chữa ô tô ở trong một xưởng sửa chữa."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 91: Dịch câu sau sang tiếng Đức: 'Lúc 8 giờ 30 phút anh ấy phải đưa con gái vào trường mẫu giáo.'",
                "options": null,
                "correct_answer": "Um 8.30 Uhr muss er die Tochter in den Kindergarten bringen.",
                "explanation": "Đưa con gái vào trường mẫu giáo (bringen -> di chuyển Wohin?) dùng Cách 4 (Akkusativ): in den Kindergarten.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Um 8.30 Uhr muss er die Tochter in den Kindergarten bringen.",
                                "Um halb neun muss er die Tochter in den Kindergarten bringen.",
                                "Um 8.30 Uhr muss er seine Tochter in den Kindergarten bringen.",
                                "Er muss um 8.30 Uhr seine Tochter in den Kindergarten bringen."
                        ],
                        "translation": "Lúc 8 giờ 30 phút anh ấy phải đưa con gái vào trường mẫu giáo."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 92: Dịch câu sau sang tiếng Đức: 'Nữ bác sĩ khám cho các bệnh nhân ở trong bệnh viện.'",
                "options": null,
                "correct_answer": "Die Ärztin untersucht Patienten im Krankenhaus.",
                "explanation": "Nữ bác sĩ là Die Ärztin; khám cho bệnh nhân là untersucht Patienten (Akkusativ); ở trong bệnh viện là im Krankenhaus (Dativ).",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Die Ärztin untersucht Patienten im Krankenhaus.",
                                "Die Ärztin untersucht die Patienten im Krankenhaus.",
                                "Im Krankenhaus untersucht die Ärztin Patienten."
                        ],
                        "translation": "Nữ bác sĩ khám cho các bệnh nhân ở trong bệnh viện."
                }
        },
        {
                "type": "dich_cau_vd",
                "question": "Câu 93: Dịch câu sau sang tiếng Đức: 'Người điều dưỡng giúp đỡ vị bác sĩ mỗi ngày.'",
                "options": null,
                "correct_answer": "Der Krankenpfleger hilft dem Arzt jeden Tag.",
                "explanation": "Động từ helfen biến âm e -> i thành hilft và bắt buộc đi với Cách 3 (Dativ): der Arzt -> dem Arzt.",
                "exp_reward": 25,
                "extra_data": {
                        "accepted_answers": [
                                "Der Krankenpfleger hilft dem Arzt jeden Tag.",
                                "Jeden Tag hilft der Krankenpfleger dem Arzt.",
                                "Die Krankenschwester hilft dem Arzt jeden Tag.",
                                "Die Krankenpflegerin hilft dem Arzt jeden Tag."
                        ],
                        "translation": "Người điều dưỡng giúp đỡ vị bác sĩ mỗi ngày."
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
                                "Vào lúc 16h30 Paula phải đón con gái từ nhà trẻ về",
                                "Lúc 4 giờ rưỡi chiều Paula phải đón con gái của cô ấy từ trường mầm non",
                                "Lúc 16 giờ 30 Paula phải đón con gái từ trường mẫu giáo",
                                "Lúc 16h30 phút Paula phải đón con gái từ trường mẫu giáo"
                        ],
                        "translation": "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen."
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
                                "Nghề của Frank Müller là giáo viên nhưng hôm nay anh ấy được nghỉ lễ và có thể ngủ tới 7 giờ",
                                "Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ đến 7 giờ",
                                "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ tới 7 giờ"
                        ],
                        "translation": "Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen."
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
                                "Điện thoại rất quan trọng với cô ấy bởi vì cô ấy phải gọi điện cho khách hàng của mình thường xuyên",
                                "Cái điện thoại rất quan trọng đối với cô ấy vì cô ấy thường phải gọi cho khách hàng",
                                "Chiếc điện thoại rất quan trọng với cô ấy vì cô ấy phải thường xuyên gọi điện cho khách hàng"
                        ],
                        "translation": "Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen."
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
                                "Buổi chiều ông Müller đưa xe hơi vào xưởng sửa chữa và sau đó đi tập đá bóng",
                                "Vào buổi chiều anh Müller đem ô tô tới xưởng sửa xe rồi đi tập bóng đá",
                                "Buổi chiều ông Müller mang ô tô vào xưởng sửa chữa rồi đi đến buổi tập bóng đá"
                        ],
                        "translation": "Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining."
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
                                "Nữ giáo viên dạy học sinh ở một ngôi trường vào buổi sáng và dạy sinh viên tại trường đại học vào buổi chiều",
                                "Buổi sáng cô giáo giảng dạy học sinh ở trường phổ thông và buổi chiều dạy sinh viên ở trường đại học",
                                "Nữ giáo viên buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học"
                        ],
                        "translation": "Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität."
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
                                "Từ 8 giờ đến 10 giờ tối Paula có thể xem truyền hình trong phòng khách sau khi làm xong bữa tối",
                                "Từ 20 giờ đến 22 giờ Paula có thể xem tivi trong phòng khách sau khi nấu bữa tối",
                                "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi làm bữa tối"
                        ],
                        "translation": "Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat."
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
                                "Thợ làm tóc cắt tóc cho anh trai của tôi tại tiệm cắt tóc",
                                "Người thợ làm tóc đang cắt tóc cho anh tôi ở trong salon tóc",
                                "Thợ cắt tóc cắt tóc cho anh trai tôi trong tiệm làm tóc"
                        ],
                        "translation": "Der Friseur schneidet meinem Bruder im Friseursalon die Haare."
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
