import os
import sys
import json

def generate_seed_script():
    # 1. GRAMMAR HTML
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
    return grammar_html

print('Helper script test passed.')

