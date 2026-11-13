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

def seed_lesson_9():
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
        print("❌ Cần khởi tạo level A1 trước!")
        conn.close()
        return
    a1_id = level_a1["id"]

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 9%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 23

    # Xóa dữ liệu cũ của Bài 9 nếu có để cập nhật sạch sẽ (Bảo toàn tuyệt đối Bài 1 -> Bài 8)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    lesson_title = 'Bài 9: Du lịch - Perfekt Präteritum (Quá khứ văn nói)'

    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 9 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Urlaub • Perfekt & Präteritum (Bài 9)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 120 phút • ⚡ 1800+ EXP • 🎯 100 Bài tập
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Bài 9: Du lịch - Perfekt Präteritum (Quá khứ văn nói)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Chinh phục chủ đề <b>Thiên nhiên & Kỳ nghỉ du lịch (Natur & Urlaub)</b>; làm chủ trọn vẹn <b>Thì Quá Khứ Hoàn Thành Perfekt</b> (haben/sein + Partizip II) với cấu trúc khung câu Satzklammer; phân biệt và sử dụng chuẩn xác <b>6 nhóm quy tắc tạo Partizip II</b>; phương pháp chọn trợ động từ <b>haben hay sein</b> không sai sót; và kết hợp tự nhiên thì <b>Präteritum của sein (war/waren) & haben (hatte/hatten)</b> trong giao tiếp hằng ngày.
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: TỪ VỰNG THIÊN NHIÊN & DU LỊCH -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Từ Vựng Thiên Nhiên & Du Lịch (Die Natur - Die Reise)</h4>
            </div>

            <p class="text-xs text-slate-600">Hệ thống từ vựng cốt lõi phân loại theo 3 giống ngữ pháp:</p>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                <!-- Giống đực der -->
                <div class="p-4 rounded-2xl bg-blue-50/70 border border-blue-200 space-y-2">
                    <div class="flex items-center justify-between pb-2 border-b border-blue-200">
                        <span class="font-extrabold text-blue-900 text-sm">🔵 GIỐNG ĐỰC (DER)</span>
                        <span class="text-[10px] text-blue-600 font-bold">Maskulinum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-700">
                        <li>• <b class="text-blue-950 font-bold">der Wald</b> <i>(Pl: die Wälder)</i>: rừng</li>
                        <li>• <b class="text-blue-950 font-bold">der Berg</b> <i>(Pl: die Berge)</i>: núi</li>
                        <li>• <b class="text-blue-950 font-bold">der Fluss</b> <i>(Pl: die Flüsse)</i>: sông</li>
                        <li>• <b class="text-blue-950 font-bold">der See</b> <i>(Pl: die Seen)</i>: hồ</li>
                        <li>• <b class="text-blue-950 font-bold">der Strand</b> <i>(Pl: die Strände)</i>: bãi biển</li>
                        <li>• <b class="text-blue-950 font-bold">der Bummel</b> <i>(Pl: die Bummel)</i>: cuộc đi dạo phố</li>
                        <li>• <b class="text-blue-950 font-bold">der Reiseführer</b> <i>(Pl: die Reiseführer)</i>: sách hướng dẫn / HDV</li>
                        <li>• <b class="text-blue-950 font-bold">der Urlaub</b> <i>(Pl: die Urlaube)</i>: kỳ nghỉ</li>
                    </ul>
                </div>

                <!-- Giống cái die -->
                <div class="p-4 rounded-2xl bg-rose-50/70 border border-rose-200 space-y-2">
                    <div class="flex items-center justify-between pb-2 border-b border-rose-200">
                        <span class="font-extrabold text-rose-900 text-sm">🔴 GIỐNG CÁI (DIE)</span>
                        <span class="text-[10px] text-rose-600 font-bold">Femininum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-700">
                        <li>• <b class="text-rose-950 font-bold">die Altstadt</b> <i>(Pl: die Altstädte)</i>: phố cổ</li>
                        <li>• <b class="text-rose-950 font-bold">die Insel</b> <i>(Pl: die Inseln)</i>: hòn đảo</li>
                        <li>• <b class="text-rose-950 font-bold">die Sonne</b> <i>(Plural: nur Singular - thường chỉ dùng số ít)</i>: mặt trời</li>
                        <li>• <b class="text-rose-950 font-bold">die Alpen</b> <i>(nur Plural - Danh từ số nhiều, ở Dativ đổi thành: in den Alpen)</i>: dãy núi Alps</li>
                        <li>• <b class="text-rose-950 font-bold">die Besichtigung</b> <i>(Pl: die Besichtigungen)</i>: sự tham quan</li>
                        <li>• <b class="text-rose-950 font-bold">die Radtour</b> <i>(Pl: die Radtouren)</i>: chuyến đạp xe</li>
                        <li>• <b class="text-rose-950 font-bold">die Reise</b> <i>(Pl: die Reisen)</i>: chuyến du lịch</li>
                    </ul>
                </div>

                <!-- Giống trung das -->
                <div class="p-4 rounded-2xl bg-emerald-50/70 border border-emerald-200 space-y-2">
                    <div class="flex items-center justify-between pb-2 border-b border-emerald-200">
                        <span class="font-extrabold text-emerald-900 text-sm">🟢 GIỐNG TRUNG (DAS)</span>
                        <span class="text-[10px] text-emerald-600 font-bold">Neutrum</span>
                    </div>
                    <ul class="space-y-1.5 text-slate-700">
                        <li>• <b class="text-emerald-950 font-bold">das Meer</b> <i>(Pl: die Meere)</i>: biển</li>
                        <li>• <b class="text-emerald-950 font-bold">das Schloss</b> <i>(Pl: die Schlösser)</i>: lâu đài, cung điện</li>
                        <li>• <b class="text-emerald-950 font-bold">das Reiseland</b> <i>(Pl: die Reiseländer)</i>: quốc gia du lịch</li>
                        <li>• <b class="text-emerald-950 font-bold">das Reiseziel</b> <i>(Pl: die Reiseziele)</i>: điểm đến du lịch</li>
                        <li>• <b class="text-emerald-950 font-bold">das Wetter</b> <i>(nur Singular)</i>: thời tiết</li>
                        <li>• <b class="text-emerald-950 font-bold">das Essen</b> <i>(Pl: die Essen)</i>: đồ ăn, bữa ăn</li>
                        <li>• <b class="text-emerald-950 font-bold">das Hotel</b> <i>(Pl: die Hotels)</i>: khách sạn</li>
                        <li>• <b class="text-emerald-950 font-bold">das Frühstück</b> <i>(Plural: nur Singular - thường chỉ dùng số ít)</i>: bữa sáng</li>
                    </ul>
                </div>
            </div>

            <!-- Mẹo nhớ giống -->
            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs space-y-1.5">
                <div class="font-bold text-amber-900 flex items-center gap-1.5">
                    💡 Mẹo Nhớ Giống Không Cần Học Vẹt:
                </div>
                <div class="text-slate-700">
                    1. Hậu tố <b>-ung</b> luôn luôn là giống cái <b>die</b>: <i>die Besichtigung, die Wanderung, die Übernachtung</i>.<br>
                    2. Danh từ ghép lấy mạo từ của <b>từ đứng cuối cùng</b>: <i>die Reise + das Land = <b>das Reiseland</b>; die Sonne + der Untergang = <b>der Sonnenuntergang</b></i>.<br>
                    3. Phân biệt <b>der Urlaub</b> (kỳ nghỉ của người lớn/đi làm) và <b>die Ferien</b> (kỳ nghỉ hè/nghỉ học của học sinh, luôn ở số nhiều).
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: CỤM ĐỘNG TỪ + DANH TỪ (KOLLOKATIONEN) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Cụm Động Từ + Danh Từ Du Lịch (Kollokationen)</h4>
            </div>

            <p class="text-xs text-slate-600">Trong tiếng Đức, danh từ đi kèm với động từ tự nhiên tạo thành các cụm cố định:</p>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs">
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">Urlaub machen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">đi nghỉ / nghỉ mát</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">eine Radtour machen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">đi một chuyến xe đạp</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">ein Picknick machen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">đi dã ngoại ngoài trời</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">Fotos machen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">chụp ảnh (không dùng nehmen)</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">eine Pause machen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">nghỉ giải lao một lát</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">ein Schloss besichtigen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">tham quan một lâu đài</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">die Altstadt besichtigen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">tham quan khu phố cổ</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">in einer Pension übernachten</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">ngủ lại trong nhà nghỉ nhỏ</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">im Zelt übernachten</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">ngủ lại trong lều cắm trại</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">ein Zimmer buchen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">đặt một căn phòng</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">den Koffer packen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">đóng gói hành lý / vali</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">die Rechnung bezahlen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">thanh toán hóa đơn</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">eine Reise / Ferien planen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">lên kế hoạch cho chuyến đi / kỳ nghỉ</div>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <b class="text-indigo-900">einen Reiseführer kaufen</b>
                    <div class="text-slate-500 text-[11px] mt-0.5">mua một cuốn sách hướng dẫn du lịch</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: NÓI VỀ KỲ NGHỈ & PRÄTERITUM SEIN / HABEN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Nói Về Kỳ Nghỉ & Präteritum Của sein / haben</h4>
            </div>

            <!-- Bảng chia Präteritum sein & haben -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-200 space-y-2">
                    <div class="font-extrabold text-amber-900 text-sm pb-1 border-b border-amber-200">
                        Präteritum của "sein" (đã là / đã ở)
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-slate-700">
                        <div>ich <b>war</b></div>
                        <div>wir <b>waren</b></div>
                        <div>du <b>warst</b></div>
                        <div>ihr <b>wart</b></div>
                        <div>er/sie/es <b>war</b></div>
                        <div>sie/Sie <b>waren</b></div>
                    </div>
                    <div class="text-[11px] text-amber-800 italic pt-1">
                        Ví dụ: <i>„Wo warst du im Urlaub? — Ich war am Meer.“</i>
                    </div>
                </div>

                <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-200 space-y-2">
                    <div class="font-extrabold text-indigo-900 text-sm pb-1 border-b border-indigo-200">
                        Präteritum của "haben" (đã có)
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-slate-700">
                        <div>ich <b>hatte</b></div>
                        <div>wir <b>hatten</b></div>
                        <div>du <b>hattest</b></div>
                        <div>ihr <b>hattet</b></div>
                        <div>er/sie/es <b>hatte</b></div>
                        <div>sie/Sie <b>hatten</b></div>
                    </div>
                    <div class="text-[11px] text-indigo-800 italic pt-1">
                        Ví dụ: <i>„Wir hatten im Urlaub viel Spaß und schönes Wetter.“</i>
                    </div>
                </div>
            </div>

            <!-- Giới từ chỉ địa điểm Wo warst du? -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-xs space-y-2">
                <div class="font-bold text-slate-800">Chọn giới từ chỉ địa điểm cho câu hỏi "Wo warst du?" (Wo? + Dativ):</div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-slate-700">
                    <div>• Thành phố, quốc gia không mạo từ: <b>in</b> Berlin, <b>in</b> Vietnam</div>
                    <div>• Quốc gia có mạo từ: <b>in der</b> Schweiz, <b>in den</b> USA</div>
                    <div>• Biển, hồ, sông, bãi biển: <b>am</b> Meer, <b>am</b> See, <b>am</b> Strand</div>
                    <div>• Hòn đảo: <b>auf der</b> Insel Phú Quốc, <b>auf der</b> Insel Cát Bà</div>
                    <div>• Vùng núi, rừng: <b>in den</b> Bergen, <b>im</b> Wald, <b>in den</b> Alpen</div>
                    <div>• Ở nhà / Nhà bạn bè: <b>zu Hause</b>, <b>bei</b> Freunden</div>
                </div>
            </div>

            <!-- Mẫu câu hỏi thăm & đánh giá kỳ nghỉ thường gặp -->
            <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-200 text-xs space-y-2">
                <div class="font-extrabold text-indigo-950 text-sm flex items-center gap-2">
                    <span>🌟 Mẫu câu hỏi thăm & đánh giá kỳ nghỉ thường gặp:</span>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-slate-700">
                    <div class="p-2.5 rounded-xl bg-white border border-indigo-100 space-y-1">
                        <div class="font-bold text-indigo-900">• Hỏi nơi chốn đã ở:</div>
                        <div class="font-semibold text-slate-800">„Wo warst du / waren Sie im Urlaub?“</div>
                        <div class="text-slate-600">→ „Ich war am Meer / in den Bergen / in Berlin / auf der Insel Phú Quốc.“</div>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-indigo-100 space-y-1">
                        <div class="font-bold text-indigo-900">• Đánh giá kỳ nghỉ chung:</div>
                        <div class="font-semibold text-slate-800">„Wie war der Urlaub / wie war es?“</div>
                        <div class="text-slate-600">→ „Es war super / toll / wunderschön / langweilig.“</div>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-indigo-100 space-y-1">
                        <div class="font-bold text-indigo-900">• Hỏi thăm thời tiết:</div>
                        <div class="font-semibold text-slate-800">„Wie war das Wetter?“</div>
                        <div class="text-slate-600">→ „Das Wetter war herrlich / gut / schlecht.“</div>
                    </div>
                    <div class="p-2.5 rounded-xl bg-white border border-indigo-100 space-y-1">
                        <div class="font-bold text-indigo-900">• Hỏi thăm đồ ăn & khách sạn:</div>
                        <div class="font-semibold text-slate-800">„Wie war das Essen / das Hotel?“</div>
                        <div class="text-slate-600">→ „Das Essen war sehr lecker. Das Hotel war sauber und gemütlich.“</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 4: THÌ PERFEKT (TRỌNG TÂM CỐT LÕI) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-rose-100 text-rose-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">⭐ Thì Quá Khứ Perfekt - Thì Quá Khứ Văn Nói (Trọng Tâm)</h4>
            </div>

            <!-- Khung Satzklammer -->
            <div class="p-4 rounded-2xl bg-blue-50 border border-blue-200 text-xs space-y-2">
                <div class="font-extrabold text-blue-900 text-sm">📐 CÔNG THỨC KHUNG CÂU (SATZKLAMMER):</div>
                <div class="font-mono text-sm font-bold text-blue-950 bg-white p-3 rounded-xl border border-blue-200">
                    S + haben / sein (vị trí 2) + ............ + Partizip II (cuối câu)
                </div>
                <p class="text-slate-600">
                    Trợ động từ <b>haben/sein</b> chia theo chủ ngữ và luôn đứng ở <b>vị trí thứ 2</b>. <b>Partizip II</b> đứng cố định ở <b>cuối cùng của mệnh đề</b>, tạo thành cặp kẹp ôm lấy mọi thông tin thời gian, địa điểm, tân ngữ ở giữa.
                </p>
            </div>

            <!-- Container Sơ đồ V1 (Khung câu Perfekt) -->
            <div id="svg-v1-container"></div>

            <!-- Container Sơ đồ V2 (Lưu đồ Partizip II) -->
            <div id="svg-v2-container"></div>

            <!-- Container Sơ đồ V3 (Cây quyết định haben / sein) -->
            <div id="svg-v3-container"></div>

            <!-- Container Sơ đồ V4 (Trục thời gian Perfekt vs Präteritum) -->
            <div id="svg-v4-container"></div>
        </div>

        <!-- HỌC PHẦN 5: ĐỌC HIỂU & PHÂN TÍCH VĂN BẢN DU LỊCH -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-cyan-100 text-cyan-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Đọc Hiểu & Phân Tích Văn Bản: "Ab in den Urlaub"</h4>
            </div>

            <!-- Container Sơ đồ V5 (Bản đồ sông Donau) -->
            <div id="svg-v5-container"></div>

            <!-- Thư của Linh gửi từ Hội An -->
            <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-3 text-xs">
                <div class="flex items-center justify-between pb-2 border-b border-slate-200">
                    <span class="font-bold text-slate-800 text-sm">✉️ E-Mail von Linh aus Hội An (Thư bạn Linh gửi từ Hội An)</span>
                    <button onclick="speakGerman('Hallo Anna, ich bin jetzt wieder zu Hause. Der Urlaub in Hội An war wunderbar!', 1.0)" class="px-2.5 py-1 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 border border-indigo-200 font-bold transition">
                        🔊 Nghe đoạn mở đầu
                    </button>
                </div>
                <div class="text-slate-700 leading-relaxed font-sans text-xs bg-white p-3.5 rounded-xl border border-slate-200">
                    „Hallo Anna, ich <b>bin</b> jetzt wieder zu Hause. Der Urlaub in Hội An <b>war</b> wunderbar! Wir <b>waren</b> eine Woche dort. Wir <b>sind</b> mit dem Flugzeug nach Đà Nẵng <b>geflogen</b> und dann mit dem Taxi nach Hội An <b>gefahren</b>. Das Hotel <b>war</b> klein, aber sehr sauber. Jeden Tag <b>haben</b> wir die Altstadt <b>angeschaut</b> und viele Fotos <b>gemacht</b>. Wir <b>haben</b> viel <b>gegessen</b>, und das Essen <b>war</b> sehr lecker. Am Strand <b>sind</b> wir im Meer <b>geschwommen</b>. Nur das Wetter <b>war</b> nicht immer gut: Zwei Tage <b>hat</b> es <b>geregnet</b>. Am Sonntag <b>sind</b> wir wieder nach Hause <b>geflogen</b>. Ich <b>habe</b> viele Souvenirs <b>gekauft</b>. Bis bald! Deine Linh“
                </div>
                <div class="text-slate-500 italic text-[11px]">
                    👉 Bản dịch: „Chào Anna, bây giờ mình đã về nhà rồi. Kỳ nghỉ ở Hội An thật tuyệt vời! Chúng mình đã ở đó một tuần. Chúng mình đã bay đến Đà Nẵng rồi đi taxi tới Hội An. Khách sạn nhỏ nhưng rất sạch. Ngày nào chúng mình cũng ngắm phố cổ và chụp nhiều ảnh. Chúng mình đã ăn rất nhiều và đồ ăn rất ngon. Ở bãi biển chúng mình đã bơi dưới biển. Chỉ có thời tiết không phải lúc nào cũng tốt: trời đã mưa hai ngày. Vào Chủ nhật chúng mình đã bay về nhà. Mình đã mua nhiều quà lưu niệm. Hẹn gặp lại! Linh của bạn“
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 6 & 7: CHEAT SHEET & MÁY TÍNH TRA CỨU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">6</span>
                <h4 class="text-lg font-bold text-slate-900">Máy Tính Tra Cứu Partizip II Tương Tác & Bảng Tổng Hợp</h4>
            </div>

            <!-- Container Sơ đồ V6 (Máy tính Partizip II) -->
            <div id="svg-v6-container"></div>

            <!-- BẢNG TỔNG HỢP ĐỘNG TỪ BẤT QUY TẮC & TRỌNG TÂM Ở THÌ PERFEKT -->
            <div class="p-5 rounded-2xl bg-slate-900 text-white border border-slate-700 space-y-4">
                <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                    <div class="flex items-center gap-2">
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-black bg-purple-500/20 text-purple-400 border border-purple-500/30">CHEAT SHEET</span>
                        <h5 class="text-sm font-extrabold text-white">Bảng Tổng Hợp Động Từ Bất Quy Tắc & Trọng Tâm Ở Thì Perfekt</h5>
                    </div>
                    <span class="text-[11px] text-slate-400">Bấm 🔊 để nghe phát âm từng động từ</span>
                </div>

                <!-- BẢNG A: 13 ĐỘNG TỪ ĐI VỚI SEIN -->
                <div class="space-y-2">
                    <div class="flex items-center gap-2 text-xs font-bold text-amber-300">
                        <span>🟠 BẢNG A: 13 Động từ chuyển động / đổi trạng thái đi kèm SEIN (ist + Partizip II)</span>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="p-2">STT</th>
                                    <th class="p-2">Nguyên mẫu (Infinitiv)</th>
                                    <th class="p-2">Perfekt với sein</th>
                                    <th class="p-2">Ý nghĩa tiếng Việt</th>
                                    <th class="p-2">Phát âm</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-200">
                                <tr><td class="p-2 font-mono text-slate-400">1</td><td class="p-2 font-bold text-white">fahren</td><td class="p-2 text-amber-300 font-mono font-bold">ist gefahren</td><td class="p-2 text-slate-300">lái xe, đi xe</td><td class="p-2"><button onclick="speakGerman('fahren, ist gefahren', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">2</td><td class="p-2 font-bold text-white">fliegen</td><td class="p-2 text-amber-300 font-mono font-bold">ist geflogen</td><td class="p-2 text-slate-300">bay</td><td class="p-2"><button onclick="speakGerman('fliegen, ist geflogen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">3</td><td class="p-2 font-bold text-white">gehen</td><td class="p-2 text-amber-300 font-mono font-bold">ist gegangen</td><td class="p-2 text-slate-300">đi bộ</td><td class="p-2"><button onclick="speakGerman('gehen, ist gegangen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">4</td><td class="p-2 font-bold text-white">kommen</td><td class="p-2 text-amber-300 font-mono font-bold">ist gekommen</td><td class="p-2 text-slate-300">đến</td><td class="p-2"><button onclick="speakGerman('kommen, ist gekommen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">5</td><td class="p-2 font-bold text-white">schwimmen</td><td class="p-2 text-amber-300 font-mono font-bold">ist geschwommen</td><td class="p-2 text-slate-300">bơi</td><td class="p-2"><button onclick="speakGerman('schwimmen, ist geschwommen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">6</td><td class="p-2 font-bold text-white">reisen</td><td class="p-2 text-amber-300 font-mono font-bold">ist gereist</td><td class="p-2 text-slate-300">đi du lịch</td><td class="p-2"><button onclick="speakGerman('reisen, ist gereist', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">7</td><td class="p-2 font-bold text-white">wandern</td><td class="p-2 text-amber-300 font-mono font-bold">ist gewandert</td><td class="p-2 text-slate-300">đi bộ đường dài</td><td class="p-2"><button onclick="speakGerman('wandern, ist gewandert', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">8</td><td class="p-2 font-bold text-white">laufen</td><td class="p-2 text-amber-300 font-mono font-bold">ist gelaufen</td><td class="p-2 text-slate-300">chạy bộ</td><td class="p-2"><button onclick="speakGerman('laufen, ist gelaufen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">9</td><td class="p-2 font-bold text-white">aufstehen</td><td class="p-2 text-amber-300 font-mono font-bold">ist aufgestanden</td><td class="p-2 text-slate-300">thức dậy</td><td class="p-2"><button onclick="speakGerman('aufstehen, ist aufgestanden', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">10</td><td class="p-2 font-bold text-white">einschlafen</td><td class="p-2 text-amber-300 font-mono font-bold">ist eingeschlafen</td><td class="p-2 text-slate-300">ngủ thiếp đi</td><td class="p-2"><button onclick="speakGerman('einschlafen, ist eingeschlafen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">11</td><td class="p-2 font-bold text-white">bleiben</td><td class="p-2 text-amber-300 font-mono font-bold">ist geblieben</td><td class="p-2 text-slate-300">ở lại</td><td class="p-2"><button onclick="speakGerman('bleiben, ist geblieben', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">12</td><td class="p-2 font-bold text-white">sein</td><td class="p-2 text-amber-300 font-mono font-bold">ist gewesen</td><td class="p-2 text-slate-300">thì, là, ở</td><td class="p-2"><button onclick="speakGerman('sein, ist gewesen', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">13</td><td class="p-2 font-bold text-white">werden</td><td class="p-2 text-amber-300 font-mono font-bold">ist geworden</td><td class="p-2 text-slate-300">trở thành, trở nên</td><td class="p-2"><button onclick="speakGerman('werden, ist geworden', 1.0)" class="px-2 py-0.5 rounded bg-amber-500/20 hover:bg-amber-500/40 text-amber-200 text-[10px] font-bold">🔊</button></td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- BẢNG B: 19 ĐỘNG TỪ BẤT QUY TẮC ĐI VỚI HABEN -->
                <div class="space-y-2 pt-3 border-t border-slate-800">
                    <div class="flex items-center gap-2 text-xs font-bold text-emerald-300">
                        <span>🟢 BẢNG B: 19 Động từ bất quy tắc cốt lõi đi kèm HABEN (hat + Partizip II)</span>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs border-collapse">
                            <thead>
                                <tr class="border-b border-slate-700 text-slate-400">
                                    <th class="p-2">STT</th>
                                    <th class="p-2">Nguyên mẫu (Infinitiv)</th>
                                    <th class="p-2">Perfekt với haben</th>
                                    <th class="p-2">Ý nghĩa tiếng Việt</th>
                                    <th class="p-2">Phát âm</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-800 text-slate-200">
                                <tr><td class="p-2 font-mono text-slate-400">1</td><td class="p-2 font-bold text-white">essen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat gegessen</td><td class="p-2 text-slate-300">ăn</td><td class="p-2"><button onclick="speakGerman('essen, hat gegessen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">2</td><td class="p-2 font-bold text-white">trinken</td><td class="p-2 text-emerald-300 font-mono font-bold">hat getrunken</td><td class="p-2 text-slate-300">uống</td><td class="p-2"><button onclick="speakGerman('trinken, hat getrunken', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">3</td><td class="p-2 font-bold text-white">schlafen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat geschlafen</td><td class="p-2 text-slate-300">ngủ</td><td class="p-2"><button onclick="speakGerman('schlafen, hat geschlafen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">4</td><td class="p-2 font-bold text-white">sehen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat gesehen</td><td class="p-2 text-slate-300">nhìn, thấy</td><td class="p-2"><button onclick="speakGerman('sehen, hat gesehen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">5</td><td class="p-2 font-bold text-white">lesen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat gelesen</td><td class="p-2 text-slate-300">đọc</td><td class="p-2"><button onclick="speakGerman('lesen, hat gelesen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">6</td><td class="p-2 font-bold text-white">treffen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat getroffen</td><td class="p-2 text-slate-300">gặp gỡ</td><td class="p-2"><button onclick="speakGerman('treffen, hat getroffen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">7</td><td class="p-2 font-bold text-white">nehmen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat genommen</td><td class="p-2 text-slate-300">lấy, đón xe</td><td class="p-2"><button onclick="speakGerman('nehmen, hat genommen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">8</td><td class="p-2 font-bold text-white">schreiben</td><td class="p-2 text-emerald-300 font-mono font-bold">hat geschrieben</td><td class="p-2 text-slate-300">viết</td><td class="p-2"><button onclick="speakGerman('schreiben, hat geschrieben', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">9</td><td class="p-2 font-bold text-white">finden</td><td class="p-2 text-emerald-300 font-mono font-bold">hat gefunden</td><td class="p-2 text-slate-300">tìm thấy</td><td class="p-2"><button onclick="speakGerman('finden, hat gefunden', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">10</td><td class="p-2 font-bold text-white">sprechen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat gesprochen</td><td class="p-2 text-slate-300">nói chuyện</td><td class="p-2"><button onclick="speakGerman('sprechen, hat gesprochen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">11</td><td class="p-2 font-bold text-white">anrufen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat angerufen</td><td class="p-2 text-slate-300">gọi điện thoại</td><td class="p-2"><button onclick="speakGerman('anrufen, hat angerufen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">12</td><td class="p-2 font-bold text-white">fernsehen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat ferngesehen</td><td class="p-2 text-slate-300">xem tivi</td><td class="p-2"><button onclick="speakGerman('fernsehen, hat ferngesehen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">13</td><td class="p-2 font-bold text-white">mitbringen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat mitgebracht</td><td class="p-2 text-slate-300">mang theo</td><td class="p-2"><button onclick="speakGerman('mitbringen, hat mitgebracht', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">14</td><td class="p-2 font-bold text-white">einladen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat eingeladen</td><td class="p-2 text-slate-300">mời</td><td class="p-2"><button onclick="speakGerman('einladen, hat eingeladen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">15</td><td class="p-2 font-bold text-white">verstehen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat verstanden</td><td class="p-2 text-slate-300">hiểu</td><td class="p-2"><button onclick="speakGerman('verstehen, hat verstanden', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">16</td><td class="p-2 font-bold text-white">bekommen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat bekommen</td><td class="p-2 text-slate-300">nhận được</td><td class="p-2"><button onclick="speakGerman('bekommen, hat bekommen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">17</td><td class="p-2 font-bold text-white">beginnen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat begonnen</td><td class="p-2 text-slate-300">bắt đầu</td><td class="p-2"><button onclick="speakGerman('beginnen, hat begonnen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">18</td><td class="p-2 font-bold text-white">vergessen</td><td class="p-2 text-emerald-300 font-mono font-bold">hat vergessen</td><td class="p-2 text-slate-300">quên</td><td class="p-2"><button onclick="speakGerman('vergessen, hat vergessen', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                                <tr><td class="p-2 font-mono text-slate-400">19</td><td class="p-2 font-bold text-white">verlieren</td><td class="p-2 text-emerald-300 font-mono font-bold">hat verloren</td><td class="p-2 text-slate-300">làm mất</td><td class="p-2"><button onclick="speakGerman('verlieren, hat verloren', 1.0)" class="px-2 py-0.5 rounded bg-emerald-500/20 hover:bg-emerald-500/40 text-emerald-200 text-[10px] font-bold">🔊</button></td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """

    vocab_raw = [
        {
                "word": "Wald",
                "article": "der",
                "gender": "der",
                "plural": "die Wälder",
                "indefinite": "ein Wald",
                "negation": "kein Wald",
                "akkusativ": "den Wald",
                "meaning": "rừng",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ đơn âm tiết giống đực, số nhiều biến âm a -> ä và thêm đuôi -er (die Wälder).",
                "example": "Wir haben gestern eine Wanderung im Wald gemacht.",
                "example_vi": "Hôm qua chúng tôi đã đi bộ đường dài trong rừng."
        },
        {
                "word": "Berg",
                "article": "der",
                "gender": "der",
                "plural": "die Berge",
                "indefinite": "ein Berg",
                "negation": "kein Berg",
                "akkusativ": "den Berg",
                "meaning": "núi, ngọn núi",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống đực, số nhiều thêm -e (die Berge). Thành ngữ: in den Bergen sein (ở trên vùng núi).",
                "example": "Im Urlaub sind wir auf einen hohen Berg gestiegen.",
                "example_vi": "Trong kỳ nghỉ chúng tôi đã leo lên một ngọn núi cao."
        },
        {
                "word": "Fluss",
                "article": "der",
                "gender": "der",
                "plural": "die Flüsse",
                "indefinite": "ein Fluss",
                "negation": "kein Fluss",
                "akkusativ": "den Fluss",
                "meaning": "con sông",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Số nhiều biến âm u -> ü và thêm đuôi -e (die Flüsse).",
                "example": "Wir sind mit dem Schiff auf dem Fluss gefahren.",
                "example_vi": "Chúng tôi đã đi tàu thủy trên sông."
        },
        {
                "word": "See",
                "article": "der",
                "gender": "der",
                "plural": "die Seen",
                "indefinite": "ein See",
                "negation": "kein See",
                "akkusativ": "den See",
                "meaning": "hồ nước",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Phân biệt: der See (hồ nước, số nhiều die Seen) vs die See (biển cả = das Meer).",
                "example": "Am Wochenende haben die Kinder im See gebadet.",
                "example_vi": "Vào cuối tuần những đứa trẻ đã tắm trong hồ."
        },
        {
                "word": "Strand",
                "article": "der",
                "gender": "der",
                "plural": "die Strände",
                "indefinite": "ein Strand",
                "negation": "kein Strand",
                "akkusativ": "den Strand",
                "meaning": "bãi biển",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Số nhiều biến âm a -> ä và thêm đuôi -e (die Strände). Giới từ: am Strand (ở bãi biển), an den Strand (ra bãi biển).",
                "example": "Wir haben den ganzen Tag am Strand gelegen und uns entspannt.",
                "example_vi": "Chúng tôi đã nằm cả ngày ở bãi biển và thư giãn."
        },
        {
                "word": "Bummel",
                "article": "der",
                "gender": "der",
                "plural": "die Bummel",
                "indefinite": "ein Bummel",
                "negation": "kein Bummel",
                "akkusativ": "den Bummel",
                "meaning": "cuộc đi dạo phố",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Đuôi -el giống đực, số nhiều giữ nguyên hình thức (die Bummel). Cụm cố định: einen Stadtbummel machen.",
                "example": "Gestern Abend haben wir einen gemütlichen Bummel durch die Altstadt gemacht.",
                "example_vi": "Tối hôm qua chúng tôi đã có một cuộc đi dạo thư thái qua khu phố cổ."
        },
        {
                "word": "Urlaub",
                "article": "der",
                "gender": "der",
                "plural": "die Urlaube",
                "indefinite": "ein Urlaub",
                "negation": "kein Urlaub",
                "akkusativ": "den Urlaub",
                "meaning": "kỳ nghỉ, chuyến nghỉ phép",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống đực (der Urlaub). Cụm kinh điển: im Urlaub sein (đang trong kỳ nghỉ), Urlaub machen (đi nghỉ mát).",
                "example": "Wo hast du deinen Sommerurlaub verbracht?",
                "example_vi": "Bạn đã trải qua kỳ nghỉ hè ở đâu?"
        },
        {
                "word": "Reiseführer",
                "article": "der",
                "gender": "der",
                "plural": "die Reiseführer",
                "indefinite": "ein Reiseführer",
                "negation": "kein Reiseführer",
                "akkusativ": "den Reiseführer",
                "meaning": "sách hướng dẫn du lịch / hướng dẫn viên",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Đuôi chỉ người hoặc đồ vật -er mang giống đực (der), số nhiều không đổi (die Reiseführer).",
                "example": "Vor der Reise habe ich einen guten Reiseführer gekauft.",
                "example_vi": "Trước chuyến đi tôi đã mua một cuốn sách hướng dẫn du lịch hay."
        },
        {
                "word": "Sonnenuntergang",
                "article": "der",
                "gender": "der",
                "plural": "die Sonnenuntergänge",
                "indefinite": "ein Sonnenuntergang",
                "negation": "kein Sonnenuntergang",
                "akkusativ": "den Sonnenuntergang",
                "meaning": "hoàng hôn, cảnh mặt trời lặn",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Ghép từ die Sonne + der Untergang -> mạo từ theo từ cuối: der Sonnenuntergang.",
                "example": "Lukas hat gestern den schönen Sonnenuntergang am Meer fotografiert.",
                "example_vi": "Hôm qua Lukas đã chụp ảnh hoàng hôn tuyệt đẹp bên bờ biển."
        },
        {
                "word": "Ausflug",
                "article": "der",
                "gender": "der",
                "plural": "die Ausflüge",
                "indefinite": "ein Ausflug",
                "negation": "kein Ausflug",
                "akkusativ": "den Ausflug",
                "meaning": "chuyến đi chơi trong ngày, dã ngoại",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống đực, số nhiều biến âm u -> ü (die Ausflüge). Cụm: einen Ausflug machen.",
                "example": "Am Sonntag haben wir einen tollen Ausflug nach Potsdam gemacht.",
                "example_vi": "Vào Chủ nhật chúng tôi đã có một chuyến đi chơi tuyệt vời đến Potsdam."
        },
        {
                "word": "Campingplatz",
                "article": "der",
                "gender": "der",
                "plural": "die Campingplätze",
                "indefinite": "ein Campingplatz",
                "negation": "kein Campingplatz",
                "akkusativ": "den Campingplatz",
                "meaning": "khu cắm trại",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Ghép từ Camping + der Platz -> số nhiều biến âm: die Campingplätze. Cụm: auf dem Campingplatz.",
                "example": "Sie haben zwei Wochen auf einem Campingplatz an der Ostsee gezeltet.",
                "example_vi": "Họ đã cắm trại hai tuần trên một khu cắm trại bên bờ biển Baltic."
        },
        {
                "word": "Koffer",
                "article": "der",
                "gender": "der",
                "plural": "die Koffer",
                "indefinite": "ein Koffer",
                "negation": "kein Koffer",
                "akkusativ": "den Koffer",
                "meaning": "vali",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Danh từ giống đực kết thúc -er, số nhiều giữ nguyên (die Koffer). Cụm den Koffer packen.",
                "example": "Gestern Abend habe ich meinen Koffer für die Reise gepackt.",
                "example_vi": "Tối qua tôi đã đóng gói xong vali cho chuyến đi."
        },
        {
                "word": "Rucksack",
                "article": "der",
                "gender": "der",
                "plural": "die Rucksäcke",
                "indefinite": "ein Rucksack",
                "negation": "kein Rucksack",
                "akkusativ": "den Rucksack",
                "meaning": "ba lô",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Ghép từ der Rücken (lưng) + der Sack (bao tải). Số nhiều biến âm: die Rucksäcke.",
                "example": "Mein Bruder hat Proviant und Wasser in den Rucksack gepackt.",
                "example_vi": "Anh trai tôi đã xếp đồ ăn dự trữ và nước vào ba lô."
        },
        {
                "word": "Zug",
                "article": "der",
                "gender": "der",
                "plural": "die Züge",
                "indefinite": "ein Zug",
                "negation": "kein Zug",
                "akkusativ": "den Zug",
                "meaning": "tàu hỏa",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Số nhiều biến âm u -> ü (die Züge). Cụm mit dem Zug fahren.",
                "example": "Wir sind gestern mit dem schnellen ICE-Zug nach München gefahren.",
                "example_vi": "Hôm qua chúng tôi đã đi chuyến tàu nhanh ICE đến München."
        },
        {
                "word": "Reisepass",
                "article": "der",
                "gender": "der",
                "plural": "die Reisepässe",
                "indefinite": "ein Reisepass",
                "negation": "kein Reisepass",
                "akkusativ": "den Reisepass",
                "meaning": "hộ chiếu",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Ghép từ die Reise + der Pass -> lấy giống theo der Pass. Số nhiều: die Reisepässe.",
                "example": "Ich habe meinen Reisepass rechtzeitig vor dem Flug verlängert.",
                "example_vi": "Tôi đã gia hạn hộ chiếu kịp thời trước chuyến bay."
        },
        {
                "word": "Regen",
                "article": "der",
                "gender": "der",
                "plural": "nur Singular",
                "indefinite": "ein Regen",
                "negation": "kein Regen",
                "akkusativ": "den Regen",
                "meaning": "mưa, cơn mưa",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Danh từ giống đực chỉ thời tiết, chỉ có số ít (der Regen).",
                "example": "Wegen des starken Regens sind wir den ganzen Tag im Hotel geblieben.",
                "example_vi": "Vì cơn mưa lớn nên chúng tôi đã ở lại khách sạn cả ngày."
        },
        {
                "word": "Gast",
                "article": "der",
                "gender": "der",
                "plural": "die Gäste",
                "indefinite": "ein Gast",
                "negation": "kein Gast",
                "akkusativ": "den Gast",
                "meaning": "vị khách",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Danh từ giống đực, số nhiều biến âm a -> ä và thêm đuôi -e (die Gäste).",
                "example": "Gestern sind viele neue Gäste im Hotel angekommen.",
                "example_vi": "Hôm qua nhiều vị khách mới đã đến khách sạn."
        },
        {
                "word": "Altstadt",
                "article": "die",
                "gender": "die",
                "plural": "die Altstädte",
                "indefinite": "eine Altstadt",
                "negation": "keine Altstadt",
                "akkusativ": "die Altstadt",
                "meaning": "khu phố cổ",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Ghép từ alt + die Stadt -> số nhiều biến âm: die Altstädte.",
                "example": "Wir haben die historische Altstadt von Hội An besichtigt.",
                "example_vi": "Chúng tôi đã tham quan khu phố cổ lịch sử của Hội An."
        },
        {
                "word": "Insel",
                "article": "die",
                "gender": "die",
                "plural": "die Inseln",
                "indefinite": "eine Insel",
                "negation": "keine Insel",
                "akkusativ": "die Insel",
                "meaning": "hòn đảo",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Đuôi -el giống cái, số nhiều thêm -n (die Inseln). Giới từ đi kèm: auf der Insel (trên hòn đảo).",
                "example": "Letzten Sommer sind wir auf die Insel Phú Quốc geflogen.",
                "example_vi": "Mùa hè năm ngoái chúng tôi đã bay đến đảo Phú Quốc."
        },
        {
                "word": "Sonne",
                "article": "die",
                "gender": "die",
                "plural": "nur Singular (thường chỉ dùng số ít)",
                "indefinite": "eine Sonne",
                "negation": "keine Sonne",
                "akkusativ": "die Sonne",
                "meaning": "mặt trời, ánh nắng",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống cái kết thúc bằng -e: die Sonne. Trong giao tiếp thường chỉ dùng dạng số ít.",
                "example": "Gestern hat die Sonne den ganzen Tag geschienen.",
                "example_vi": "Hôm qua mặt trời đã chiếu sáng suốt cả ngày."
        },
        {
                "word": "Alpen",
                "article": "die",
                "gender": "die",
                "plural": "nur Plural (ở Dativ đổi thành: in den Alpen)",
                "indefinite": "Alpen",
                "negation": "keine Alpen",
                "akkusativ": "die Alpen",
                "meaning": "dãy núi Alps",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ CHỈ CÓ SỐ NHIỀU (Pluralwort). Ở Cách 3 (Dativ) bắt buộc đổi thành: in den Alpen.",
                "example": "Familie Weber ist im Winter zum Skifahren in den Alpen gewesen.",
                "example_vi": "Gia đình Weber đã đi trượt tuyết ở dãy Alps vào mùa đông."
        },
        {
                "word": "Besichtigung",
                "article": "die",
                "gender": "die",
                "plural": "die Besichtigungen",
                "indefinite": "eine Besichtigung",
                "negation": "keine Besichtigung",
                "akkusativ": "die Besichtigung",
                "meaning": "sự tham quan",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Mọi danh từ có hậu tố -ung luôn luôn mang giống cái (die), số nhiều thêm -en (die Besichtigungen).",
                "example": "Gestern hat die Besichtigung des Schlosses zwei Stunden gedauert.",
                "example_vi": "Hôm qua chuyến tham quan lâu đài đã kéo dài hai tiếng."
        },
        {
                "word": "Radtour",
                "article": "die",
                "gender": "die",
                "plural": "die Radtouren",
                "indefinite": "eine Radtour",
                "negation": "keine Radtour",
                "akkusativ": "die Radtour",
                "meaning": "chuyến đạp xe",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Ghép từ das Rad + die Tour -> mang giống cái die Radtour. Cụm: eine Radtour machen.",
                "example": "Sie haben eine wunderschöne Radtour an der Donau gemacht.",
                "example_vi": "Họ đã thực hiện một chuyến đạp xe tuyệt đẹp dọc sông Donau."
        },
        {
                "word": "Reise",
                "article": "die",
                "gender": "die",
                "plural": "die Reisen",
                "indefinite": "eine Reise",
                "negation": "keine Reise",
                "akkusativ": "die Reise",
                "meaning": "chuyến du lịch, chuyến đi",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống cái kết thúc bằng -e, số nhiều thêm -n (die Reisen). Cụm: eine Reise planen / machen.",
                "example": "Meine Eltern haben eine lange Reise durch Europa geplant.",
                "example_vi": "Bố mẹ tôi đã lên kế hoạch cho một chuyến du lịch dài xuyên châu Âu."
        },
        {
                "word": "Landschaft",
                "article": "die",
                "gender": "die",
                "plural": "die Landschaften",
                "indefinite": "eine Landschaft",
                "negation": "keine Landschaft",
                "akkusativ": "die Landschaft",
                "meaning": "phong cảnh, cảnh quan",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Hậu tố -schaft luôn luôn là giống cái die, số nhiều thêm -en (die Landschaften).",
                "example": "Vom Berggipfel aus haben wir die herrliche Landschaft bewundert.",
                "example_vi": "Từ đỉnh núi chúng tôi đã chiêm ngưỡng phong cảnh tuyệt mỹ."
        },
        {
                "word": "Küste",
                "article": "die",
                "gender": "die",
                "plural": "die Küsten",
                "indefinite": "eine Küste",
                "negation": "keine Küste",
                "akkusativ": "die Küste",
                "meaning": "bờ biển",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống cái, số nhiều thêm -n (die Küsten). Giới từ: an der Küste (ở bờ biển).",
                "example": "Wir sind mit dem Fahrrad entlang der Küste gefahren.",
                "example_vi": "Chúng tôi đã đi xe đạp dọc theo bờ biển."
        },
        {
                "word": "Pause",
                "article": "die",
                "gender": "die",
                "plural": "die Pausen",
                "indefinite": "eine Pause",
                "negation": "keine Pause",
                "akkusativ": "die Pause",
                "meaning": "giờ nghỉ giải lao",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống cái kết thúc -e, số nhiều thêm -n (die Pausen). Cụm: eine Pause machen.",
                "example": "Nach drei Stunden Fahrt haben wir eine kurze Pause gemacht.",
                "example_vi": "Sau ba tiếng lái xe chúng tôi đã nghỉ giải lao một lát."
        },
        {
                "word": "Pension",
                "article": "die",
                "gender": "die",
                "plural": "die Pensionen",
                "indefinite": "eine Pension",
                "negation": "keine Pension",
                "akkusativ": "die Pension",
                "meaning": "nhà nghỉ nhỏ",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Hậu tố -ion luôn luôn mang giống cái (die), số nhiều thêm -en (die Pensionen).",
                "example": "In Linz haben die Urlauber in einer gemütlichen Pension übernachtet.",
                "example_vi": "Ở Linz những người đi du lịch đã ngủ lại trong một nhà nghỉ nhỏ ấm cúng."
        },
        {
                "word": "Jugendherberge",
                "article": "die",
                "gender": "die",
                "plural": "die Jugendherbergen",
                "indefinite": "eine Jugendherberge",
                "negation": "keine Jugendherberge",
                "akkusativ": "die Jugendherberge",
                "meaning": "nhà trọ thanh niên (hostel)",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Danh từ giống cái kết thúc bằng -e, số nhiều thêm -n (die Jugendherbergen).",
                "example": "Die Studenten haben preiswert in der Jugendherberge übernachtet.",
                "example_vi": "Các sinh viên đã ngủ lại giá rẻ trong nhà trọ thanh niên."
        },
        {
                "word": "Fahrkarte",
                "article": "die",
                "gender": "die",
                "plural": "die Fahrkarten",
                "indefinite": "eine Fahrkarte",
                "negation": "keine Fahrkarte",
                "akkusativ": "die Fahrkarte",
                "meaning": "vé tàu / xe",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Ghép từ fahren + die Karte -> die Fahrkarte. Số nhiều: die Fahrkarten.",
                "example": "Anna hat die Fahrkarten online auf dem Smartphone gebucht.",
                "example_vi": "Anna đã đặt vé tàu xe trực tuyến trên điện thoại thông minh."
        },
        {
                "word": "Rechnung",
                "article": "die",
                "gender": "die",
                "plural": "die Rechnungen",
                "indefinite": "eine Rechnung",
                "negation": "keine Rechnung",
                "akkusativ": "die Rechnung",
                "meaning": "hóa đơn",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Hậu tố -ung luôn luôn mang giống cái (die), số nhiều thêm -en. Cụm die Rechnung bezahlen.",
                "example": "Am Abreisetag hat der Vater die Rechnung im Hotel bezahlt.",
                "example_vi": "Vào ngày rời đi người bố đã thanh toán hóa đơn ở khách sạn."
        },
        {
                "word": "Postkarte",
                "article": "die",
                "gender": "die",
                "plural": "die Postkarten",
                "indefinite": "eine Postkarte",
                "negation": "keine Postkarte",
                "akkusativ": "die Postkarte",
                "meaning": "bưu thiếp",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Ghép từ die Post + die Karte -> die Postkarte. Cụm eine Postkarte schreiben.",
                "example": "Aus dem Urlaub habe ich eine Postkarte an meine Großeltern geschickt.",
                "example_vi": "Từ kỳ nghỉ tôi đã gửi một tấm bưu thiếp cho ông bà tôi."
        },
        {
                "word": "Meer",
                "article": "das",
                "gender": "das",
                "plural": "die Meere",
                "indefinite": "ein Meer",
                "negation": "kein Meer",
                "akkusativ": "das Meer",
                "meaning": "biển, biển cả",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống trung (das Meer). Giới từ: am Meer sein (ở biển), ans Meer fahren (ra biển).",
                "example": "Am Strand sind wir jeden Vormittag im Meer geschwommen.",
                "example_vi": "Ở bãi biển chúng tôi đã bơi dưới biển vào mỗi buổi sáng."
        },
        {
                "word": "Schloss",
                "article": "das",
                "gender": "das",
                "plural": "die Schlösser",
                "indefinite": "ein Schloss",
                "negation": "kein Schloss",
                "akkusativ": "das Schloss",
                "meaning": "lâu đài, cung điện",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Số nhiều biến âm o -> ö và thêm đuôi -er: die Schlösser. Cụm: ein Schloss besichtigen.",
                "example": "In Deutschland haben die Touristen das berühmte Schloss Neuschwanstein besichtigt.",
                "example_vi": "Ở Đức các du khách đã tham quan lâu đài Neuschwanstein nổi tiếng."
        },
        {
                "word": "Reiseland",
                "article": "das",
                "gender": "das",
                "plural": "die Reiseländer",
                "indefinite": "ein Reiseland",
                "negation": "kein Reiseland",
                "akkusativ": "das Reiseland",
                "meaning": "quốc gia du lịch",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Ghép từ die Reise + das Land -> lấy mạo từ theo das Land. Số nhiều: die Reiseländer.",
                "example": "Vietnam ist in den letzten Jahren ein sehr beliebtes Reiseland geworden.",
                "example_vi": "Việt Nam đã trở thành một quốc gia du lịch rất được yêu thích trong những năm gần đây."
        },
        {
                "word": "Reiseziel",
                "article": "das",
                "gender": "das",
                "plural": "die Reiseziele",
                "indefinite": "ein Reiseziel",
                "negation": "kein Reiseziel",
                "akkusativ": "das Reiseziel",
                "meaning": "điểm đến du lịch",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Ghép từ die Reise + das Ziel -> mạo từ theo das Ziel, số nhiều thêm -e: die Reiseziele.",
                "example": "Nach einer langen Fahrt haben wir unser Reiseziel endlich erreicht.",
                "example_vi": "Sau chuyến đi dài cuối cùng chúng tôi đã đến được điểm đến du lịch."
        },
        {
                "word": "Wetter",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Wetter",
                "negation": "kein Wetter",
                "akkusativ": "das Wetter",
                "meaning": "thời tiết",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống trung chỉ hiện tượng tự nhiên, chỉ có số ít (das Wetter). Cụm: Wie war das Wetter?",
                "example": "Das Wetter im Urlaub war herrlich und sonnig.",
                "example_vi": "Thời tiết trong kỳ nghỉ đã rất tuyệt vời và có nắng."
        },
        {
                "word": "Essen",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular (thường chỉ dùng số ít)",
                "indefinite": "ein Essen",
                "negation": "kein Essen",
                "akkusativ": "das Essen",
                "meaning": "đồ ăn, bữa ăn",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Động từ danh từ hóa từ essen -> luôn mang giống trung das Essen. Thường dùng ở số ít.",
                "example": "Im Hotel war das Essen sehr lecker, und wir haben viel gegessen.",
                "example_vi": "Ở khách sạn đồ ăn rất ngon và chúng tôi đã ăn rất nhiều."
        },
        {
                "word": "Hotel",
                "article": "das",
                "gender": "das",
                "plural": "die Hotels",
                "indefinite": "ein Hotel",
                "negation": "kein Hotel",
                "akkusativ": "das Hotel",
                "meaning": "khách sạn",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Từ mượn quốc tế mang giống trung (das Hotel), số nhiều thêm -s: die Hotels.",
                "example": "Wir haben fünf Tage in einem sauberen Hotel am Strand übernachtet.",
                "example_vi": "Chúng tôi đã ở qua đêm năm ngày trong một khách sạn sạch sẽ bên bãi biển."
        },
        {
                "word": "Dorf",
                "article": "das",
                "gender": "das",
                "plural": "die Dörfer",
                "indefinite": "ein Dorf",
                "negation": "kein Dorf",
                "akkusativ": "das Dorf",
                "meaning": "ngôi làng",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ đơn âm tiết giống trung, số nhiều biến âm o -> ö và thêm -er (die Dörfer).",
                "example": "Gestern sind wir durch ein malerisches kleines Dorf gewandert.",
                "example_vi": "Hôm qua chúng tôi đã đi bộ đường dài qua một ngôi làng nhỏ đẹp như tranh vẽ."
        },
        {
                "word": "Picknick",
                "article": "das",
                "gender": "das",
                "plural": "die Picknicks",
                "indefinite": "ein Picknick",
                "negation": "kein Picknick",
                "akkusativ": "das Picknick",
                "meaning": "chuyến dã ngoại ngoài trời",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Từ mượn tiếng Anh mang giống trung das Picknick, số nhiều thêm -s. Cụm: ein Picknick machen.",
                "example": "Am Ufer des Sees haben wir ein fröhliches Picknick gemacht.",
                "example_vi": "Bên bờ hồ chúng tôi đã có một chuyến dã ngoại vui vẻ."
        },
        {
                "word": "Kloster",
                "article": "das",
                "gender": "das",
                "plural": "die Klöster",
                "indefinite": "ein Kloster",
                "negation": "kein Kloster",
                "akkusativ": "das Kloster",
                "meaning": "tu viện",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống trung, số nhiều biến âm o -> ö (die Klöster). Cụm: ein altes Kloster besichtigen.",
                "example": "In Linz hat die Reisegruppe ein sehr altes Kloster besucht.",
                "example_vi": "Ở Linz đoàn du lịch đã đến thăm một tu viện rất cổ kính."
        },
        {
                "word": "Zelt",
                "article": "das",
                "gender": "das",
                "plural": "die Zelte",
                "indefinite": "ein Zelt",
                "negation": "kein Zelt",
                "akkusativ": "das Zelt",
                "meaning": "lều cắm trại",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Danh từ giống trung, số nhiều thêm -e: die Zelte. Động từ liên quan: zelten (cắm trại).",
                "example": "Am Seeufer haben wir unser Zelt direkt unter den Bäumen aufgebaut.",
                "example_vi": "Bên bờ hồ chúng tôi đã dựng lều ngay dưới những tán cây."
        },
        {
                "word": "Foto",
                "article": "das",
                "gender": "das",
                "plural": "die Fotos",
                "indefinite": "ein Foto",
                "negation": "kein Foto",
                "akkusativ": "das Foto",
                "meaning": "bức ảnh",
                "category": "Thiên nhiên & Điểm đến Du lịch (Natur & Reiseziele - Bài 9)",
                "notes": "Từ viết tắt của die Fotografie nhưng mang giống trung das Foto, số nhiều thêm -s. Cụm: Fotos machen.",
                "example": "Im Urlaub hat mein Freund viele schöne Fotos von der Natur gemacht.",
                "example_vi": "Trong kỳ nghỉ bạn tôi đã chụp nhiều bức ảnh đẹp về thiên nhiên."
        },
        {
                "word": "Flugzeug",
                "article": "das",
                "gender": "das",
                "plural": "die Flugzeuge",
                "indefinite": "ein Flugzeug",
                "negation": "kein Flugzeug",
                "akkusativ": "das Flugzeug",
                "meaning": "máy bay",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Hậu tố -zeug luôn mang giống trung das, số nhiều thêm -e (die Flugzeuge). Cụm: mit dem Flugzeug fliegen.",
                "example": "Wir sind gestern pünktlich mit dem Flugzeug in Frankfurt gelandet.",
                "example_vi": "Hôm qua chúng tôi đã hạ cánh đúng giờ bằng máy bay ở Frankfurt."
        },
        {
                "word": "Schiff",
                "article": "das",
                "gender": "das",
                "plural": "die Schiffe",
                "indefinite": "ein Schiff",
                "negation": "kein Schiff",
                "akkusativ": "das Schiff",
                "meaning": "tàu thủy",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Danh từ đơn âm tiết giống trung, số nhiều thêm -e: die Schiffe. Cụm: mit dem Schiff fahren.",
                "example": "Auf der Donau sind wir mit einem großen Schiff gefahren.",
                "example_vi": "Trên sông Donau chúng tôi đã đi trên một con tàu lớn."
        },
        {
                "word": "Zimmer",
                "article": "das",
                "gender": "das",
                "plural": "die Zimmer",
                "indefinite": "ein Zimmer",
                "negation": "kein Zimmer",
                "akkusativ": "das Zimmer",
                "meaning": "căn phòng",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Đuôi -er giống trung, số nhiều giữ nguyên hình thức (die Zimmer). Cụm ein Zimmer buchen.",
                "example": "Für das Wochenende haben wir ein Doppelzimmer mit Meerblick gebucht.",
                "example_vi": "Cho dịp cuối tuần chúng tôi đã đặt một phòng đôi nhìn ra biển."
        },
        {
                "word": "Souvenir",
                "article": "das",
                "gender": "das",
                "plural": "die Souvenirs",
                "indefinite": "ein Souvenir",
                "negation": "kein Souvenir",
                "akkusativ": "das Souvenir",
                "meaning": "quà lưu niệm",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Từ mượn tiếng Pháp, mang giống trung das Souvenir, số nhiều thêm -s.",
                "example": "In der Altstadt hat Linh viele hübsche Souvenirs für ihre Freunde gekauft.",
                "example_vi": "Ở phố cổ Linh đã mua nhiều món quà lưu niệm xinh xắn cho bạn bè."
        },
        {
                "word": "Gepäck",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular",
                "indefinite": "ein Gepäck",
                "negation": "kein Gepäck",
                "akkusativ": "das Gepäck",
                "meaning": "hành lý",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Danh từ giống trung chỉ tồn tại ở dạng số ít: das Gepäck.",
                "example": "Am Flughafen haben wir unser schweres Gepäck abgeholt.",
                "example_vi": "Tại sân bay chúng tôi đã nhận hành lý nặng của mình."
        },
        {
                "word": "Frühstück",
                "article": "das",
                "gender": "das",
                "plural": "nur Singular (thường chỉ dùng số ít)",
                "indefinite": "ein Frühstück",
                "negation": "kein Frühstück",
                "akkusativ": "das Frühstück",
                "meaning": "bữa sáng",
                "category": "Kỳ nghỉ: Chỗ ở, Phương tiện, Hành lý & Thời tiết (Urlaub - Bài 9)",
                "notes": "Ghép từ früh + das Stück -> mang giống trung das Frühstück. Thường dùng dạng số ít.",
                "example": "Im Hotel haben wir jeden Morgen ein reichhaltiges Frühstück gegessen.",
                "example_vi": "Tại khách sạn mỗi buổi sáng chúng tôi đều đã ăn một bữa sáng thịnh soạn."
        }
    ]

    vocabularies = []
    for v in vocab_raw:
        art = v.get("article") or ""
        w = v.get("word") or ""
        full_w = (art + " " + w).strip() if art else w
        pl = v.get("plural")
        meaning = (v["meaning"] + " (Pl: " + pl + ")") if pl else v["meaning"]
        ex_vi = v.get("example_vi")
        example_str = (v["example"] + " (" + ex_vi + ")") if ex_vi else v.get("example")
        vocabularies.append((
            lesson_id,
            full_w,
            art if art else None,
            meaning,
            example_str
        ))

    if existing_lesson:
        cursor.execute("""
            UPDATE lessons SET title = ?, grammar_content = ? WHERE id = ?;
        """, (lesson_title, grammar_html, lesson_id))
    else:
        cursor.execute("""
            INSERT INTO lessons (id, level_id, title, grammar_content)
            VALUES (?, ?, ?, ?);
        """, (lesson_id, a1_id, lesson_title, grammar_html))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    exercises_raw = [
            {
                    "type": "trac_nghiem",
                    "question": "Câu 1: Chọn câu đúng ngữ pháp ở thì Perfekt:",
                    "options": [
                            "Wir haben gestern ein Schloss besichtigt.",
                            "Wir haben gestern besichtigt ein Schloss.",
                            "Wir gestern haben ein Schloss besichtigt.",
                            "Wir besichtigt haben gestern ein Schloss."
                    ],
                    "correct_answer": "Wir haben gestern ein Schloss besichtigt.",
                    "explanation": "Trong câu trần thuật ở thì Perfekt, trợ động từ 'haben' đứng ở vị trí thứ 2, còn Partizip II ('besichtigt') bắt buộc đứng ở cuối câu: „Wir haben gestern ein Schloss besichtigt.“",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Hôm qua chúng tôi đã tham quan một lâu đài."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 2: Chọn dạng Partizip II đúng của động từ 'fotografieren': „Die Touristen haben den Dom ___.“",
                    "options": [
                            "fotografiert",
                            "gefotografiert",
                            "fotografieren",
                            "gefotografieret"
                    ],
                    "correct_answer": "fotografiert",
                    "explanation": "Động từ kết thúc bằng đuôi '-ieren' khi chuyển sang Partizip II không thêm tiền tố 'ge-', chỉ lấy gốc động từ 'fotografier-' + '-t' -> fotografiert.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Các du khách đã chụp ảnh nhà thờ lớn."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 3: Chọn dạng Partizip II đúng của động từ 'einkaufen': „Wir haben auf dem Markt frisches Obst ___.“",
                    "options": [
                            "eingekauft",
                            "geeinkauft",
                            "einkauft",
                            "gekauft ein"
                    ],
                    "correct_answer": "eingekauft",
                    "explanation": "'einkaufen' là động từ tách (tiền tố 'ein-'), nên khi tạo Partizip II ta chèn '-ge-' vào giữa tiền tố và gốc động từ: ein + ge + kauf + t -> eingekauft.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Chúng tôi đã mua sắm trái cây tươi ở chợ."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 4: Chọn trợ động từ đúng: „Gestern ___ wir um sieben Uhr nach Wien gefahren.“",
                    "options": [
                            "sind",
                            "haben",
                            "ist",
                            "hat"
                    ],
                    "correct_answer": "sind",
                    "explanation": "Động từ 'fahren' chỉ sự di chuyển thay đổi vị trí nên đi với trợ động từ 'sein'. Chia theo chủ ngữ ngôi thứ nhất số nhiều 'wir' là 'sind'.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Hôm qua lúc bảy giờ chúng tôi đã đi đến Wien."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 5: Chọn câu SAI ngữ pháp:",
                    "options": [
                            "Wir sind gestern ein Picknick gemacht.",
                            "Ich bin im Urlaub nach Hạ Long geflogen.",
                            "Meine Eltern sind drei Tage in Đà Lạt geblieben.",
                            "Der Schnee ist in der Sonne geschmolzen."
                    ],
                    "correct_answer": "Wir sind gestern ein Picknick gemacht.",
                    "explanation": "Cụm 'ein Picknick machen' có tân ngữ Akkusativ và không chỉ sự di chuyển nên bắt buộc dùng trợ động từ 'haben' (Câu đúng: „Wir haben gestern ein Picknick gemacht.“). Các động từ 'fliegen' (di chuyển), 'bleiben' (động từ cố định với sein) và 'schmelzen' (thay đổi trạng thái) đều dùng trợ động từ 'sein'.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "(Câu sai sau khi sửa đúng): Hôm qua chúng tôi đã đi dã ngoại."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 6: Cặp động từ nguyên mẫu (Infinitiv) – phân từ hai (Partizip II) nào sau đây ĐÚNG?",
                    "options": [
                            "sehen – gesehen / schlafen – geschlafen",
                            "essen – geesst / trinken – getrinkt",
                            "nehmen – genehmt / finden – gefindet",
                            "schreiben – geschreibt / singen – gesingt"
                    ],
                    "correct_answer": "sehen – gesehen / schlafen – geschlafen",
                    "explanation": "'sehen -> gesehen' và 'schlafen -> geschlafen' là hai động từ bất quy tắc chia đúng. Các động từ còn lại phải chia là: essen -> gegessen, trinken -> getrunken, nehmen -> genommen, finden -> gefunden, schreiben -> geschrieben, singen -> gesungen.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "sehen (nhìn/xem) – gesehen / schlafen (ngủ) – geschlafen."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 7: Chọn cặp từ đúng để hoàn thành câu: „Letzte Woche in Đà Lạt ___ das Wetter sehr kalt, aber wir ___ sehr glücklich.“",
                    "options": [
                            "war / waren",
                            "waren / war",
                            "warst / wart",
                            "wart / warst"
                    ],
                    "correct_answer": "war / waren",
                    "explanation": "Câu kể về sự việc trong quá khứ ('letzte Woche') với động từ 'sein' nên chia ở thì Präteritum: chủ ngữ số ít 'das Wetter' (ngôi es) chia là 'war', chủ ngữ số nhiều 'wir' chia là 'waren'.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Tuần trước ở Đà Lạt thời tiết rất lạnh, nhưng chúng tôi đã rất hạnh phúc."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 8: Chọn cặp từ đúng: „Wo ___ ihr letztes Wochenende? — Wir ___ am See.“",
                    "options": [
                            "wart / waren",
                            "warst / waren",
                            "wart / war",
                            "seid / sind"
                    ],
                    "correct_answer": "wart / waren",
                    "explanation": "Trạng ngữ 'letztes Wochenende' (cuối tuần trước) chỉ quá khứ nên động từ 'sein' được chia ở thì Präteritum: ngôi 'ihr' chia là 'wart', ngôi 'wir' chia là 'waren' (cặp 'seid / sind' là thì hiện tại Präsens).",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Cuối tuần trước các bạn đã ở đâu? — Chúng tôi đã ở bên hồ."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 9: Chọn dãy Partizip II đúng tương ứng với 'besuchen – übernachten – erreichen':",
                    "options": [
                            "besucht – übernachtet – erreicht",
                            "gebesucht – geübernachtet – geerreicht",
                            "besuchet – übernachtt – erreichet",
                            "besucht – geübernachtet – erreicht"
                    ],
                    "correct_answer": "besucht – übernachtet – erreicht",
                    "explanation": "Cả 3 động từ đều bắt đầu bằng tiền tố không tách ('be-', 'über-', 'er-') nên không thêm 'ge-' ở Partizip II. Riêng 'übernachten' có gốc 'übernacht-' kết thúc bằng '-t' nên phải thêm '-et' thành 'übernachtet' (besucht – übernachtet – erreicht).",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "đã thăm – đã ngủ lại – đã đến được."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 10: Vì sao dạng Partizip II của động từ 'arbeiten' là 'gearbeitet' mà không phải là 'gearbeit'?",
                    "options": [
                            "Vì gốc \"arbeit\" kết thúc bằng -t nên phải thêm -e- để dễ phát âm.",
                            "Vì arbeiten là động từ bất quy tắc.",
                            "Vì arbeiten là động từ tách.",
                            "Vì arbeiten dùng trợ động từ sein."
                    ],
                    "correct_answer": "Vì gốc \"arbeit\" kết thúc bằng -t nên phải thêm -e- để dễ phát âm.",
                    "explanation": "Các động từ có quy tắc mà gốc kết thúc bằng '-t' hoặc '-d' (như 'arbeit-', 'wart-', 'bad-') phải thêm âm đệm '-e-' trước đuôi '-t' để có thể phát âm rõ âm cuối: ge + arbeit + et -> gearbeitet.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "arbeiten (làm việc) -> gearbeitet."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 11: Dòng nào ghi ĐÚNG cả mạo từ số ít lẫn dạng số nhiều?",
                    "options": [
                            "der Strand – die Strände / die Insel – die Inseln / das Meer – die Meere",
                            "der Strand – die Strands / der Insel – die Insel / das Meer – die Meeren",
                            "der Berg – die Berge / der See – die Seen / die Fluss – die Flüsse",
                            "der Urlaub – die Urlauber / das Hotel – die Hotelse / das Schloss – die Schlosse"
                    ],
                    "correct_answer": "der Strand – die Strände / die Insel – die Inseln / das Meer – die Meere",
                    "explanation": "Dạng đúng là: der Strand – die Strände (thêm Umlaut + -e), die Insel – die Inseln (thêm -n), das Meer – die Meere (thêm -e). Các phương án khác sai vì: 'der Fluss' là giống đực (không phải 'die Fluss'); số nhiều của 'der Urlaub' là 'die Urlaube' (còn 'die Urlauber' nghĩa là những người đi du lịch), 'das Hotel' -> 'die Hotels', 'das Schloss' -> 'die Schlösser'.",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "bãi biển – các bãi biển / hòn đảo – các hòn đảo / biển – các biển."
                    }
            },
            {
                    "type": "trac_nghiem",
                    "question": "Câu 12: Trong giao tiếp hằng ngày, câu nào diễn đạt đúng ngữ pháp và tự nhiên nhất ý: „Hôm qua tôi đã đi mua sắm.“?",
                    "options": [
                            "Gestern habe ich eingekauft.",
                            "Gestern kaufte ich ein.",
                            "Gestern bin ich eingekauft.",
                            "Gestern habe ich einkauft."
                    ],
                    "correct_answer": "Gestern habe ich eingekauft.",
                    "explanation": "Trong giao tiếp hằng ngày (văn nói), người Đức dùng thì Perfekt. Động từ tách 'einkaufen' chỉ hoạt động mua sắm (không chỉ sự di chuyển từ nơi này sang nơi khác) nên đi với trợ động từ 'haben' và Partizip II 'eingekauft' -> „Gestern habe ich eingekauft.“ (Câu „Gestern kaufte ich ein.“ dùng thì Präteritum mang sắc thái văn viết).",
                    "exp_reward": 10,
                    "extra_data": {
                            "translation": "Hôm qua tôi đã đi mua sắm."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 13: Điền trợ động từ: „Meine Oma ___ im Sommer auf der Insel Phú Quốc Urlaub gemacht.“",
                    "options": null,
                    "correct_answer": "hat",
                    "explanation": "'Urlaub machen' có tân ngữ → 'haben'; 'meine Oma' = 'sie' → 'hat'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "hat"
                            ],
                            "translation": "Bà tôi đã đi nghỉ trên đảo Phú Quốc vào mùa hè."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 14: Điền trợ động từ: „Mein Bruder ___ gestern Abend um zehn Uhr eingeschlafen.“",
                    "options": null,
                    "correct_answer": "ist",
                    "explanation": "'einschlafen' là đổi trạng thái → 'sein'; 'mein Bruder' = 'er' → 'ist'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "ist"
                            ],
                            "translation": "Anh trai tôi đã ngủ thiếp đi lúc mười giờ tối qua."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 15: Điền Partizip II của 'suchen': „Habt ihr am Strand den Reiseführer ___?“",
                    "options": null,
                    "correct_answer": "gesucht",
                    "explanation": "'suchen' có quy tắc: 'ge' + 'such' + 't' = 'gesucht'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "gesucht"
                            ],
                            "translation": "Các bạn đã tìm cuốn sách hướng dẫn du lịch ở bãi biển phải không?"
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 16: Điền Partizip II của 'ankommen': „Der Zug ist pünktlich in München ___.“",
                    "options": null,
                    "correct_answer": "angekommen",
                    "explanation": "Tiền tố tách 'an-' + bất quy tắc 'kommen → gekommen' → 'an' + 'ge' + 'kommen' = 'angekommen' (dùng 'sein').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "angekommen"
                            ],
                            "translation": "Chuyến tàu đã đến München đúng giờ."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 17: Điền Partizip II của 'übernachten': „Wir haben im Zelt ___.“",
                    "options": null,
                    "correct_answer": "übernachtet",
                    "explanation": "Tiền tố 'über-' không tách → không 'ge-'; gốc 'übernacht' đuôi '-t' → thêm '-et': 'übernachtet'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "übernachtet",
                                    "uebernachtet"
                            ],
                            "translation": "Chúng tôi đã ngủ lại trong lều."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 18: Điền Partizip II của 'bezahlen': „Hast du schon die Rechnung ___?“",
                    "options": null,
                    "correct_answer": "bezahlt",
                    "explanation": "Tiền tố 'be-' không tách → không 'ge-': 'bezahlt'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "bezahlt"
                            ],
                            "translation": "Bạn đã trả hóa đơn chưa?"
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 19: Điền Partizip II của 'baden': „Die Kinder haben den ganzen Tag im Meer ___.“",
                    "options": null,
                    "correct_answer": "gebadet",
                    "explanation": "Gốc 'bad' kết thúc '-d' → 'ge' + 'bad' + 'et' = 'gebadet'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "gebadet"
                            ],
                            "translation": "Bọn trẻ đã tắm biển cả ngày."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 20: Điền Partizip II của 'regnen': „Gestern hat es den ganzen Tag ___.“",
                    "options": null,
                    "correct_answer": "geregnet",
                    "explanation": "Gốc 'regn' khó phát âm nếu chỉ thêm '-t' → 'geregnet' (động từ thời tiết dùng 'haben').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "geregnet"
                            ],
                            "translation": "Hôm qua trời đã mưa cả ngày."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 21: Điền Partizip II của 'essen': „Ich habe am Abend Reis mit Fisch ___.“",
                    "options": null,
                    "correct_answer": "gegessen",
                    "explanation": "'essen' bất quy tắc: 'gegessen'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "gegessen"
                            ],
                            "translation": "Buổi tối tôi đã ăn cơm với cá."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 22: Điền Partizip II của 'studieren': „Die Studentin hat ein Jahr in Wien ___.“",
                    "options": null,
                    "correct_answer": "studiert",
                    "explanation": "Đuôi '-ieren' → không 'ge-': 'studiert'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "studiert"
                            ],
                            "translation": "Nữ sinh viên đã học đại học một năm ở Wien."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 23: Điền dạng Präteritum của 'sein': „Letzten Sommer ___ ich mit meiner Familie in Đà Nẵng.“",
                    "options": null,
                    "correct_answer": "war",
                    "explanation": "'ich' + Präteritum của 'sein' = 'war'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "war"
                            ],
                            "translation": "Mùa hè năm ngoái tôi đã ở Đà Nẵng cùng gia đình."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 24: Điền dạng Präteritum của 'sein': „Wo ___ du gestern Nachmittag, Linh? Ich habe dich nicht gesehen.“",
                    "options": null,
                    "correct_answer": "warst",
                    "explanation": "'du' + Präteritum của 'sein' = 'warst'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "warst"
                            ],
                            "translation": "Chiều qua bạn đã ở đâu vậy, Linh? Mình đã không nhìn thấy bạn."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 25: Điền dạng Präteritum của 'haben': „Die Kinder ___ gestern viel Spaß am Strand.“",
                    "options": null,
                    "correct_answer": "hatten",
                    "explanation": "'die Kinder' = 'sie' (số nhiều) + Präteritum của 'haben' = 'hatten'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "hatten"
                            ],
                            "translation": "Hôm qua bọn trẻ đã rất vui ở bãi biển."
                    }
            },
            {
                    "type": "dien_khuyet",
                    "question": "Câu 26: Điền Partizip II của 'wandern': „Ihr seid am Wochenende in den Bergen ___.“",
                    "options": null,
                    "correct_answer": "gewandert",
                    "explanation": "'wandern' có quy tắc: 'ge' + 'wander' + 't' = 'gewandert' (dùng 'sein' vì là di chuyển: 'ihr seid').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "gewandert"
                            ],
                            "translation": "Cuối tuần các bạn đã đi bộ đường dài trên núi."
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 27: Dịch sang tiếng Đức (kèm mạo từ số ít): \"cuộc hành trình bằng xe đạp\"",
                    "options": null,
                    "correct_answer": "die Radtour",
                    "explanation": "Cuộc hành trình bằng xe đạp là danh từ giống cái 'die Radtour' (số nhiều: 'die Radtouren').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "die Radtour",
                                    "Radtour"
                            ],
                            "translation": "cuộc hành trình bằng xe đạp"
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 28: Dịch sang tiếng Đức (kèm mạo từ số ít): \"phố cổ\"",
                    "options": null,
                    "correct_answer": "die Altstadt",
                    "explanation": "Phố cổ là 'die Altstadt' (số nhiều: 'die Altstädte').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "die Altstadt",
                                    "Altstadt"
                            ],
                            "translation": "phố cổ"
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 29: Dịch sang tiếng Đức (kèm mạo từ số ít): \"sách hướng dẫn du lịch\"",
                    "options": null,
                    "correct_answer": "der Reiseführer",
                    "explanation": "Sách hướng dẫn du lịch là 'der Reiseführer' (số nhiều: 'die Reiseführer').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "der Reiseführer",
                                    "Reiseführer",
                                    "der Reisefuehrer"
                            ],
                            "translation": "sách hướng dẫn du lịch"
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 30: Dịch sang tiếng Đức (kèm mạo từ số ít): \"điểm đến du lịch\"",
                    "options": null,
                    "correct_answer": "das Reiseziel",
                    "explanation": "'die Reise' + 'das Ziel' → giống của từ cuối: 'das Reiseziel' (số nhiều: 'die Reiseziele').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "das Reiseziel",
                                    "Reiseziel"
                            ],
                            "translation": "điểm đến du lịch"
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 31: Dịch sang tiếng Đức bằng Perfekt: \"Anh ấy đã đến nơi.\" (động từ 'ankommen')",
                    "options": null,
                    "correct_answer": "er ist angekommen",
                    "explanation": "'ankommen' là chuyển động → 'sein'; 'er' → 'ist'; Partizip II 'angekommen' → 'er ist angekommen'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "er ist angekommen",
                                    "Er ist angekommen."
                            ],
                            "translation": "Anh ấy đã đến nơi."
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 32: Dịch sang tiếng Đức bằng Perfekt: \"Chúng tôi đã cắm trại.\" (động từ 'zelten')",
                    "options": null,
                    "correct_answer": "wir haben gezeltet",
                    "explanation": "'zelten' dùng 'haben'; 'wir' → 'haben'; gốc 'zelt' đuôi '-t' → 'gezeltet' → 'wir haben gezeltet'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "wir haben gezeltet",
                                    "Wir haben gezeltet."
                            ],
                            "translation": "Chúng tôi đã cắm trại."
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 33: Dịch sang tiếng Đức (dạng số nhiều): \"những kỳ nghỉ\" (số nhiều của 'der Urlaub')",
                    "options": null,
                    "correct_answer": "die Urlaube",
                    "explanation": "Số nhiều của 'der Urlaub' là 'die Urlaube'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "die Urlaube",
                                    "Urlaube"
                            ],
                            "translation": "những kỳ nghỉ"
                    }
            },
            {
                    "type": "dich_nghia_vd",
                    "question": "Câu 34: Dịch sang tiếng Đức bằng Perfekt: \"Tôi đã thử món ăn.\" ('das Essen probieren')",
                    "options": null,
                    "correct_answer": "ich habe das Essen probiert",
                    "explanation": "'probieren' đuôi '-ieren' → không 'ge-': 'probiert'; 'ich' → 'habe' → 'ich habe das Essen probiert'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "ich habe das Essen probiert",
                                    "Ich habe das Essen probiert."
                            ],
                            "translation": "Tôi đã thử món ăn."
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 35: Dịch sang tiếng Việt: „das Reiseland“",
                    "options": null,
                    "correct_answer": "đất nước du lịch",
                    "explanation": "'die Reise' (chuyến du lịch) + 'das Land' (đất nước) = 'das Reiseland'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "đất nước du lịch",
                                    "quốc gia du lịch",
                                    "nước du lịch"
                            ],
                            "translation": "đất nước du lịch"
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 36: Dịch sang tiếng Việt: „der Bummel“",
                    "options": null,
                    "correct_answer": "cuộc đi dạo",
                    "explanation": "'der Bummel' là cuộc đi dạo phố, tản bộ ngắm cảnh (số nhiều: 'die Bummel').",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "cuộc đi dạo",
                                    "cuộc đi dạo phố",
                                    "sự đi dạo",
                                    "đi dạo"
                            ],
                            "translation": "cuộc đi dạo"
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 37: Dịch sang tiếng Việt: „die Besichtigung“",
                    "options": null,
                    "correct_answer": "sự tham quan",
                    "explanation": "'die Besichtigung' xuất phát từ động từ 'besichtigen' (tham quan); đuôi '-ung' luôn là 'die'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "sự tham quan",
                                    "buổi tham quan",
                                    "chuyến tham quan",
                                    "tham quan"
                            ],
                            "translation": "sự tham quan"
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 38: Dịch sang tiếng Việt: „Es war langweilig.“",
                    "options": null,
                    "correct_answer": "Nó chán.",
                    "explanation": "'es war' là Präteritum của 'sein' (\"nó đã là\"), 'langweilig' = chán, nhàm chán.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "Nó chán.",
                                    "Nó đã chán.",
                                    "Nó nhàm chán.",
                                    "Thật nhàm chán.",
                                    "Nó rất chán."
                            ],
                            "translation": "Nó chán."
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 39: Dịch sang tiếng Việt: „Ich habe Fotos gemacht.“",
                    "options": null,
                    "correct_answer": "Tôi đã chụp ảnh.",
                    "explanation": "'Fotos machen' = chụp ảnh; Perfekt 'ich habe … gemacht' = \"tôi đã …\".",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "Tôi đã chụp ảnh.",
                                    "Tôi đã chụp những bức ảnh.",
                                    "Tôi đã chụp nhiều ảnh."
                            ],
                            "translation": "Tôi đã chụp ảnh."
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 40: Dịch sang tiếng Việt: „Wir sind in den Alpen gewandert.“",
                    "options": null,
                    "correct_answer": "Chúng tôi đã đi bộ đường dài trên dãy Alps.",
                    "explanation": "'wandern' = đi bộ đường dài (dùng 'sein'); 'in den Alpen' = ở / trong dãy Alps.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "Chúng tôi đã đi bộ đường dài trên dãy Alps.",
                                    "Chúng tôi đã đi bộ đường dài ở dãy Alps.",
                                    "Chúng tôi đã đi bộ đường dài trong dãy Alps."
                            ],
                            "translation": "Chúng tôi đã đi bộ đường dài trên dãy Alps."
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 41: Dịch sang tiếng Việt: „Das Wetter war prima.“",
                    "options": null,
                    "correct_answer": "Thời tiết thật tuyệt.",
                    "explanation": "'das Wetter' (thời tiết) + 'war' (Präteritum của 'sein') + 'prima' (rất tốt, tuyệt).",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "Thời tiết thật tuyệt.",
                                    "Thời tiết đã rất tốt.",
                                    "Thời tiết rất tuyệt.",
                                    "Thời tiết rất tốt."
                            ],
                            "translation": "Thời tiết thật tuyệt."
                    }
            },
            {
                    "type": "dich_nghia_dv",
                    "question": "Câu 42: Dịch sang tiếng Việt: „Was ist passiert?“",
                    "options": null,
                    "correct_answer": "Chuyện gì đã xảy ra?",
                    "explanation": "'passieren' (xảy ra) dùng 'sein' → 'es ist passiert'; câu hỏi 'Was ist passiert?'.",
                    "exp_reward": 15,
                    "extra_data": {
                            "accepted_answers": [
                                    "Chuyện gì đã xảy ra?",
                                    "Có chuyện gì xảy ra vậy?",
                                    "Chuyện gì xảy ra vậy?",
                                    "Điều gì đã xảy ra?"
                            ],
                            "translation": "Chuyện gì đã xảy ra?"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 43: Nối các cặp tương ứng sau (Infinitiv – Partizip II, động từ có quy tắc):",
                    "options": null,
                    "correct_answer": "machen = gemacht || arbeiten = gearbeitet || studieren = studiert || bezahlen = bezahlt",
                    "explanation": "'machen' (nhóm 1: 'ge-t'), 'arbeiten' (nhóm 2: 'ge-et'), 'studieren' (nhóm 3: '-ieren', không 'ge-'), 'bezahlen' (nhóm 4: 'be-', không 'ge-').",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "machen",
                                            "right": "gemacht"
                                    },
                                    {
                                            "left": "arbeiten",
                                            "right": "gearbeitet"
                                    },
                                    {
                                            "left": "studieren",
                                            "right": "studiert"
                                    },
                                    {
                                            "left": "bezahlen",
                                            "right": "bezahlt"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 44: Nối các cặp tương ứng sau (Infinitiv – Partizip II, bất quy tắc dùng haben):",
                    "options": null,
                    "correct_answer": "essen = gegessen || trinken = getrunken || schreiben = geschrieben || sehen = gesehen",
                    "explanation": "Bốn động từ bất quy tắc có dạng 'ge- … -en' ('trinken' đổi 'i → u', 'schreiben' đổi 'ei → ie').",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "essen",
                                            "right": "gegessen"
                                    },
                                    {
                                            "left": "trinken",
                                            "right": "getrunken"
                                    },
                                    {
                                            "left": "schreiben",
                                            "right": "geschrieben"
                                    },
                                    {
                                            "left": "sehen",
                                            "right": "gesehen"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 45: Nối các cặp tương ứng sau (Infinitiv – Perfekt dùng sein):",
                    "options": null,
                    "correct_answer": "fahren = ist gefahren || fliegen = ist geflogen || bleiben = ist geblieben || laufen = ist gelaufen",
                    "explanation": "Cả bốn động từ đều chỉ chuyển động đổi vị trí hoặc 'bleiben' nên dùng 'sein'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "fahren",
                                            "right": "ist gefahren"
                                    },
                                    {
                                            "left": "fliegen",
                                            "right": "ist geflogen"
                                    },
                                    {
                                            "left": "bleiben",
                                            "right": "ist geblieben"
                                    },
                                    {
                                            "left": "laufen",
                                            "right": "ist gelaufen"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 46: Nối các cặp tương ứng sau (Động từ tách – Partizip II):",
                    "options": null,
                    "correct_answer": "einkaufen = eingekauft || anschauen = angeschaut || aufstehen = aufgestanden || mitnehmen = mitgenommen",
                    "explanation": "Động từ tách chèn 'ge' giữa tiền tố và gốc: 'ein' + 'ge' + 'kauft', 'an' + 'ge' + 'schaut', 'auf' + 'ge' + 'standen', 'mit' + 'ge' + 'nommen'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "einkaufen",
                                            "right": "eingekauft"
                                    },
                                    {
                                            "left": "anschauen",
                                            "right": "angeschaut"
                                    },
                                    {
                                            "left": "aufstehen",
                                            "right": "aufgestanden"
                                    },
                                    {
                                            "left": "mitnehmen",
                                            "right": "mitgenommen"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 47: Nối các cặp tương ứng sau (Quy tắc – Ví dụ):",
                    "options": null,
                    "correct_answer": "ge + gốc + t = spielen → gespielt || ge + gốc + et (gốc đuôi -t) = warten → gewartet || đuôi -ieren, không ge- = reservieren → reserviert || tiền tố không tách, không ge- = erleben → erlebt",
                    "explanation": "Bốn quy tắc đầu của Partizip II (nhóm 1, 2, 3, 4).",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "ge + gốc + t",
                                            "right": "spielen → gespielt"
                                    },
                                    {
                                            "left": "ge + gốc + et (gốc đuôi -t)",
                                            "right": "warten → gewartet"
                                    },
                                    {
                                            "left": "đuôi -ieren, không ge-",
                                            "right": "reservieren → reserviert"
                                    },
                                    {
                                            "left": "tiền tố không tách, không ge-",
                                            "right": "erleben → erlebt"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 48: Nối các cặp tương ứng sau (Câu hỏi về kỳ nghỉ – Câu trả lời phù hợp):",
                    "options": null,
                    "correct_answer": "Wo warst du im Urlaub? = Ich war auf der Insel Phú Quốc. || Wie war das Hotel? = Es war sauber und gemütlich. || Was hast du gemacht? = Ich habe viele Fotos gemacht. || Wie bist du gefahren? = Ich bin mit dem Zug gefahren.",
                    "explanation": "Câu hỏi 'Wo', 'Wie war', 'Was', 'Wie' phải được đáp bằng câu cùng loại thông tin (nơi chốn, tính chất, hành động, phương tiện).",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "Wo warst du im Urlaub?",
                                            "right": "Ich war auf der Insel Phú Quốc."
                                    },
                                    {
                                            "left": "Wie war das Hotel?",
                                            "right": "Es war sauber und gemütlich."
                                    },
                                    {
                                            "left": "Was hast du gemacht?",
                                            "right": "Ich habe viele Fotos gemacht."
                                    },
                                    {
                                            "left": "Wie bist du gefahren?",
                                            "right": "Ich bin mit dem Zug gefahren."
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 49: Nối các cặp tương ứng sau (Danh từ – Động từ đi cặp, Kollokation):",
                    "options": null,
                    "correct_answer": "ein Hotel = buchen || den Koffer = packen || ein Schloss = besichtigen || ein Picknick = machen",
                    "explanation": "'ein Hotel buchen' (đặt khách sạn), 'den Koffer packen' (đóng vali), 'ein Schloss besichtigen' (tham quan lâu đài), 'ein Picknick machen' (đi dã ngoại).",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "ein Hotel",
                                            "right": "buchen"
                                    },
                                    {
                                            "left": "den Koffer",
                                            "right": "packen"
                                    },
                                    {
                                            "left": "ein Schloss",
                                            "right": "besichtigen"
                                    },
                                    {
                                            "left": "ein Picknick",
                                            "right": "machen"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "noi_o",
                    "question": "Câu 50: Nối các cặp tương ứng sau (Ngôi – Dạng Präteritum):",
                    "options": null,
                    "correct_answer": "ich (sein) = war || du (sein) = warst || ihr (haben) = hattet || wir (haben) = hatten",
                    "explanation": "'ich war', 'du warst', 'ihr hattet', 'wir hatten'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "noi_o_pairs": [
                                    {
                                            "left": "ich (sein)",
                                            "right": "war"
                                    },
                                    {
                                            "left": "du (sein)",
                                            "right": "warst"
                                    },
                                    {
                                            "left": "ihr (haben)",
                                            "right": "hattet"
                                    },
                                    {
                                            "left": "wir (haben)",
                                            "right": "hatten"
                                    }
                            ],
                            "translation": "Nối các cặp hoàn chỉnh"
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 51: Điền 2 từ để hoàn thành câu: „Hôm qua tôi đã tham quan viện bảo tàng và chụp ảnh.“: 'Gestern [1] ich das Museum [2] und Fotos gemacht.'",
                    "options": null,
                    "correct_answer": "habe / besichtigt",
                    "explanation": "'ich' → 'habe'; 'besichtigen' (tiền tố 'be-') → 'besichtigt'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Gestern [1] ich das Museum [2] und Fotos gemacht.",
                            "slot1_accepted": [
                                    "habe"
                            ],
                            "slot2_accepted": [
                                    "besichtigt"
                            ],
                            "accepted_answers": [
                                    "habe / besichtigt",
                                    "habe besichtigt",
                                    "habe, besichtigt"
                            ],
                            "translation": "Điền 2 từ để hoàn thành câu: „Hôm qua tôi đã tham quan viện bảo tàng và chụp ảnh."
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 52: Điền 2 từ để hoàn thành câu: „Chúng tôi đã đi bằng tàu hỏa đến Hamburg.“: 'Wir [1] mit dem Zug nach Hamburg [2].'",
                    "options": null,
                    "correct_answer": "sind / gefahren",
                    "explanation": "'fahren' chuyển động → 'sein'; 'wir' → 'sind'; Partizip II 'gefahren'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Wir [1] mit dem Zug nach Hamburg [2].",
                            "slot1_accepted": [
                                    "sind"
                            ],
                            "slot2_accepted": [
                                    "gefahren"
                            ],
                            "accepted_answers": [
                                    "sind / gefahren",
                                    "sind gefahren",
                                    "sind, gefahren"
                            ],
                            "translation": "Điền 2 từ để hoàn thành câu: „Chúng tôi đã đi bằng tàu hỏa đến Hamburg."
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 53: Điền 2 từ để hoàn thành câu: „Linh đã ở lại Hội An hai tuần.“: 'Linh [1] zwei Wochen in Hội An [2].'",
                    "options": null,
                    "correct_answer": "ist / geblieben",
                    "explanation": "'bleiben' luôn dùng 'sein'; 'Linh' = 'sie' → 'ist'; Partizip II 'geblieben'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Linh [1] zwei Wochen in Hội An [2].",
                            "slot1_accepted": [
                                    "ist"
                            ],
                            "slot2_accepted": [
                                    "geblieben"
                            ],
                            "accepted_answers": [
                                    "ist / geblieben",
                                    "ist geblieben",
                                    "ist, geblieben"
                            ],
                            "translation": "Điền 2 từ để hoàn thành câu: „Linh đã ở lại Hội An hai tuần."
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 54: Điền 2 từ để hoàn thành câu hỏi: „Các bạn đã ngủ ngon chứ?“: '[1] ihr gut [2]?'",
                    "options": null,
                    "correct_answer": "habt / geschlafen",
                    "explanation": "Câu hỏi Ja/Nein bắt đầu bằng trợ động từ; 'ihr' → 'habt'; 'schlafen' → 'geschlafen'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "[1] ihr gut [2]?",
                            "slot1_accepted": [
                                    "habt"
                            ],
                            "slot2_accepted": [
                                    "geschlafen"
                            ],
                            "accepted_answers": [
                                    "habt / geschlafen",
                                    "habt geschlafen",
                                    "habt, geschlafen"
                            ],
                            "translation": "Điền 2 từ để hoàn thành câu hỏi: „Các bạn đã ngủ ngon chứ?"
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 55: Điền 2 Partizip II để hoàn thành câu: „Tôi đã đặt phòng và đã trả tiền.“: 'Ich habe das Zimmer [1] und [2].'",
                    "options": null,
                    "correct_answer": "gebucht / bezahlt",
                    "explanation": "'buchen' → 'gebucht'; 'bezahlen' (tiền tố 'be-') → 'bezahlt'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Ich habe das Zimmer [1] und [2].",
                            "slot1_accepted": [
                                    "gebucht"
                            ],
                            "slot2_accepted": [
                                    "bezahlt"
                            ],
                            "accepted_answers": [
                                    "gebucht / bezahlt",
                                    "gebucht bezahlt",
                                    "gebucht, bezahlt"
                            ],
                            "translation": "Điền 2 Partizip II để hoàn thành câu: „Tôi đã đặt phòng và đã trả tiền."
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 56: Điền 2 dạng Präteritum của 'sein' để hoàn thành câu: „Hôm qua thời tiết rất tốt, và chúng tôi đã ở bãi biển.“: 'Das Wetter [1] gestern sehr gut, und wir [2] am Strand.'",
                    "options": null,
                    "correct_answer": "war / waren",
                    "explanation": "'das Wetter' = 'es' → 'war'; 'wir' → 'waren'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Das Wetter [1] gestern sehr gut, und wir [2] am Strand.",
                            "slot1_accepted": [
                                    "war"
                            ],
                            "slot2_accepted": [
                                    "waren"
                            ],
                            "accepted_answers": [
                                    "war / waren",
                                    "war waren",
                                    "war, waren"
                            ],
                            "translation": "Điền 2 dạng Präteritum của 'sein' để hoàn thành câu: „Hôm qua thời tiết rất tốt, và chúng tôi đã ở bãi biển."
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 57: Điền 2 từ để hoàn thành câu: „Anna đã đóng vali của mình rồi sau đó đã đi đến nhà ga.“: 'Anna [1] ihren Koffer [2] und ist dann zum Bahnhof gegangen.'",
                    "options": null,
                    "correct_answer": "hat / gepackt",
                    "explanation": "'packen' có tân ngữ 'den Koffer' → 'haben'; 'Anna' = 'sie' → 'hat'; Partizip II 'gepackt'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Anna [1] ihren Koffer [2] und ist dann zum Bahnhof gegangen.",
                            "slot1_accepted": [
                                    "hat"
                            ],
                            "slot2_accepted": [
                                    "gepackt"
                            ],
                            "accepted_answers": [
                                    "hat / gepackt",
                                    "hat gepackt",
                                    "hat, gepackt"
                            ],
                            "translation": "Điền 2 từ để hoàn thành câu: „Anna đã đóng vali của mình rồi sau đó đã đi đến nhà ga."
                    }
            },
            {
                    "type": "dien_tao_cau",
                    "question": "Câu 58: Điền 2 từ để hoàn thành câu: „Họ đã gặp những người bạn mới và đã nói chuyện nhiều.“: 'Sie [1] neue Freunde [2] und viel gesprochen.'",
                    "options": null,
                    "correct_answer": "haben / getroffen",
                    "explanation": "'sie' (họ, số nhiều) → 'haben'; 'treffen' bất quy tắc → 'getroffen'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "display_frame": "Sie [1] neue Freunde [2] und viel gesprochen.",
                            "slot1_accepted": [
                                    "haben"
                            ],
                            "slot2_accepted": [
                                    "getroffen"
                            ],
                            "accepted_answers": [
                                    "haben / getroffen",
                                    "haben getroffen",
                                    "haben, getroffen"
                            ],
                            "translation": "Điền 2 từ để hoàn thành câu: „Họ đã gặp những người bạn mới và đã nói chuyện nhiều."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 59: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Meine Eltern sind letzte Woche nach Italien ___.'",
                    "options": null,
                    "correct_answer": "geflogen",
                    "explanation": "'fliegen → ist geflogen'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Meine Eltern sind letzte Woche nach Italien geflogen.",
                            "display_sentence": "Meine Eltern sind letzte Woche nach Italien ___.",
                            "hint_vi": "Bố mẹ tôi đã bay đến Ý vào tuần trước.",
                            "accepted_answers": [
                                    "geflogen"
                            ],
                            "translation": "Bố mẹ tôi đã bay đến Ý vào tuần trước."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 60: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Im Sommer haben wir zwei Nächte am See ___.'",
                    "options": null,
                    "correct_answer": "gezeltet",
                    "explanation": "Gốc 'zelt' kết thúc '-t' → 'gezeltet'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Im Sommer haben wir zwei Nächte am See gezeltet.",
                            "display_sentence": "Im Sommer haben wir zwei Nächte am See ___.",
                            "hint_vi": "Vào mùa hè chúng tôi đã cắm trại hai đêm bên hồ.",
                            "accepted_answers": [
                                    "gezeltet"
                            ],
                            "translation": "Vào mùa hè chúng tôi đã cắm trại hai đêm bên hồ."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 61: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Ich habe das Hotel im Internet ___.'",
                    "options": null,
                    "correct_answer": "gebucht",
                    "explanation": "'buchen → gebucht'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Ich habe das Hotel im Internet gebucht.",
                            "display_sentence": "Ich habe das Hotel im Internet ___.",
                            "hint_vi": "Tôi đã đặt khách sạn trên mạng.",
                            "accepted_answers": [
                                    "gebucht"
                            ],
                            "translation": "Tôi đã đặt khách sạn trên mạng."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 62: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Bus ist um neun Uhr ___.'",
                    "options": null,
                    "correct_answer": "abgefahren",
                    "explanation": "'abfahren' (tách) → 'ab' + 'ge' + 'fahren' = 'abgefahren', dùng 'sein'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Der Bus ist um neun Uhr abgefahren.",
                            "display_sentence": "Der Bus ist um neun Uhr ___.",
                            "hint_vi": "Chiếc xe buýt đã khởi hành lúc chín giờ.",
                            "accepted_answers": [
                                    "abgefahren"
                            ],
                            "translation": "Chiếc xe buýt đã khởi hành lúc chín giờ."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 63: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Wo ___ ihr im Sommer? Wir waren in den Alpen.'",
                    "options": null,
                    "correct_answer": "wart",
                    "explanation": "'ihr' + Präteritum của 'sein' = 'wart'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Wo wart ihr im Sommer? Wir waren in den Alpen.",
                            "display_sentence": "Wo ___ ihr im Sommer? Wir waren in den Alpen.",
                            "hint_vi": "Vào mùa hè các bạn đã ở đâu? Chúng tôi đã ở dãy Alps.",
                            "accepted_answers": [
                                    "wart"
                            ],
                            "translation": "Vào mùa hè các bạn đã ở đâu? Chúng tôi đã ở dãy Alps."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 64: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Am Abend haben wir die Nudelsuppe ___.'",
                    "options": null,
                    "correct_answer": "probiert",
                    "explanation": "Đuôi '-ieren' → không 'ge-': 'probiert'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Am Abend haben wir die Nudelsuppe probiert.",
                            "display_sentence": "Am Abend haben wir die Nudelsuppe ___.",
                            "hint_vi": "Buổi tối chúng tôi đã thử món súp mì.",
                            "accepted_answers": [
                                    "probiert"
                            ],
                            "translation": "Buổi tối chúng tôi đã thử món súp mì."
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 65: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Was ist denn ___? Mein Koffer ist nicht angekommen!'",
                    "options": null,
                    "correct_answer": "passiert",
                    "explanation": "'passieren' đuôi '-ieren' → 'passiert' (dùng 'sein': 'ist passiert').",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Was ist denn passiert? Mein Koffer ist nicht angekommen!",
                            "display_sentence": "Was ist denn ___? Mein Koffer ist nicht angekommen!",
                            "hint_vi": "Chuyện gì đã xảy ra vậy? Vali của tôi đã không đến nơi!",
                            "accepted_answers": [
                                    "passiert"
                            ],
                            "translation": "Chuyện gì đã xảy ra vậy? Vali của tôi đã không đến nơi!"
                    }
            },
            {
                    "type": "nghe_dien",
                    "question": "Câu 66: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Nach dem Frühstück haben wir den Reiseführer ___.'",
                    "options": null,
                    "correct_answer": "gelesen",
                    "explanation": "'lesen' bất quy tắc: 'gelesen'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "audio_text": "Nach dem Frühstück haben wir den Reiseführer gelesen.",
                            "display_sentence": "Nach dem Frühstück haben wir den Reiseführer ___.",
                            "hint_vi": "Sau bữa sáng chúng tôi đã đọc cuốn sách hướng dẫn du lịch.",
                            "accepted_answers": [
                                    "gelesen"
                            ],
                            "translation": "Sau bữa sáng chúng tôi đã đọc cuốn sách hướng dẫn du lịch."
                    }
            },
            {
                    "type": "dich_cau_vd",
                    "question": "Câu 67: Dịch câu sau sang tiếng Đức: \"Mùa hè năm ngoái tôi đã đi du lịch đến Berlin.\"",
                    "options": null,
                    "correct_answer": "Letzten Sommer bin ich nach Berlin gereist.",
                    "explanation": "'reisen' / 'fahren' đều là di chuyển → 'ich bin … gereist / gefahren'; trạng từ thời gian ở đầu câu thì đảo 'bin ich'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Letzten Sommer bin ich nach Berlin gereist."
                            ],
                            "translation": "Mùa hè năm ngoái tôi đã đi du lịch đến Berlin."
                    }
            },
            {
                    "type": "dich_cau_vd",
                    "question": "Câu 68: Dịch câu sau sang tiếng Đức: \"Gia đình tôi đã ở qua đêm trong một khách sạn nhỏ và đã ăn nhiều cá.\"",
                    "options": null,
                    "correct_answer": "Meine Familie hat in einem kleinen Hotel übernachtet und viel Fisch gegessen.",
                    "explanation": "'übernachten → übernachtet', 'essen → gegessen'; cả hai dùng 'haben' nên 'hat' chỉ cần xuất hiện một lần.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Meine Familie hat in einem kleinen Hotel übernachtet und viel Fisch gegessen."
                            ],
                            "translation": "Gia đình tôi đã ở qua đêm trong một khách sạn nhỏ và đã ăn nhiều cá."
                    }
            },
            {
                    "type": "dich_cau_vd",
                    "question": "Câu 69: Dịch câu hỏi sau sang tiếng Đức: \"Bạn đã làm gì vào cuối tuần, Tom?\"",
                    "options": null,
                    "correct_answer": "Was hast du am Wochenende gemacht, Tom?",
                    "explanation": "W-Frage: 'Was' + 'hast' (vị trí 2) + 'du' + … + 'gemacht' (cuối câu).",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Was hast du am Wochenende gemacht, Tom?"
                            ],
                            "translation": "Bạn đã làm gì vào cuối tuần, Tom?"
                    }
            },
            {
                    "type": "dich_cau_vd",
                    "question": "Câu 70: Dịch câu sau sang tiếng Đức: \"Hôm qua trời đã mưa cả ngày, nhưng buổi tối thì tuyệt.\"",
                    "options": null,
                    "correct_answer": "Gestern hat es den ganzen Tag geregnet, aber der Abend war toll.",
                    "explanation": "'regnen → hat geregnet' (ngôi 'es'); 'der Abend war toll' dùng Präteritum của 'sein'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Gestern hat es den ganzen Tag geregnet, aber der Abend war toll."
                            ],
                            "translation": "Hôm qua trời đã mưa cả ngày, nhưng buổi tối thì tuyệt."
                    }
            },
            {
                    "type": "dich_cau_vd",
                    "question": "Câu 71: Dịch câu sau sang tiếng Đức: \"Chúng tôi đã không ở lại bãi biển lâu.\"",
                    "options": null,
                    "correct_answer": "Wir sind nicht lange am Strand geblieben.",
                    "explanation": "'bleiben → sind … geblieben'; 'nicht' đứng trước 'lange'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Wir sind nicht lange am Strand geblieben."
                            ],
                            "translation": "Chúng tôi đã không ở lại bãi biển lâu."
                    }
            },
            {
                    "type": "dich_cau_vd",
                    "question": "Câu 72: Dịch câu sau sang tiếng Đức: \"Tối qua em gái tôi đã gọi điện cho tôi.\"",
                    "options": null,
                    "correct_answer": "Meine Schwester hat mich gestern Abend angerufen.",
                    "explanation": "'anrufen' (tách, bất quy tắc) → 'hat … angerufen'; 'mich' (tôi, Akkusativ).",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Meine Schwester hat mich gestern Abend angerufen."
                            ],
                            "translation": "Tối qua em gái tôi đã gọi điện cho tôi."
                    }
            },
            {
                    "type": "dich_cau_dv",
                    "question": "Câu 73: Dịch câu sau sang tiếng Việt: „Letzten Winter sind wir nach Österreich gefahren. Dort hat es viel geschneit.“",
                    "options": null,
                    "correct_answer": "Mùa đông năm ngoái chúng tôi đã đi Áo. Ở đó tuyết đã rơi nhiều.",
                    "explanation": "'sind … gefahren' (chuyển động); 'es hat geschneit' = tuyết đã rơi.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Mùa đông năm ngoái chúng tôi đã đi Áo. Ở đó tuyết đã rơi nhiều."
                            ],
                            "translation": "Mùa đông năm ngoái chúng tôi đã đi Áo. Ở đó tuyết đã rơi nhiều."
                    }
            },
            {
                    "type": "dich_cau_dv",
                    "question": "Câu 74: Dịch câu sau sang tiếng Việt: „Ich habe mein Handy im Hotel vergessen, und jetzt muss ich zurückfahren.“",
                    "options": null,
                    "correct_answer": "Tôi đã quên điện thoại trong khách sạn và bây giờ tôi phải quay lại.",
                    "explanation": "'vergessen → hat vergessen'; 'muss … zurückfahren' = phải quay lại.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Tôi đã quên điện thoại trong khách sạn và bây giờ tôi phải quay lại."
                            ],
                            "translation": "Tôi đã quên điện thoại trong khách sạn và bây giờ tôi phải quay lại."
                    }
            },
            {
                    "type": "dich_cau_dv",
                    "question": "Câu 75: Dịch câu sau sang tiếng Việt: „Wo wart ihr denn gestern? Wir haben euch angerufen, aber ihr habt nicht geantwortet.“",
                    "options": null,
                    "correct_answer": "Hôm qua các bạn đã ở đâu vậy? Chúng tôi đã gọi cho các bạn nhưng các bạn đã không trả lời.",
                    "explanation": "'wart' (Präteritum 'sein', 'ihr'); 'angerufen'; 'geantwortet' (gốc '-t' → '-et'), ở đây phủ định 'nicht geantwortet'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Hôm qua các bạn đã ở đâu vậy? Chúng tôi đã gọi cho các bạn nhưng các bạn đã không trả lời."
                            ],
                            "translation": "Hôm qua các bạn đã ở đâu vậy? Chúng tôi đã gọi cho các bạn nhưng các bạn đã không trả lời."
                    }
            },
            {
                    "type": "dich_cau_dv",
                    "question": "Câu 76: Dịch câu sau sang tiếng Việt: „Die Reise war lang, aber schön. Wir sind mit dem Schiff gefahren und haben viele Inseln gesehen.“",
                    "options": null,
                    "correct_answer": "Chuyến đi dài nhưng đẹp. Chúng tôi đã đi bằng tàu thủy và đã nhìn thấy nhiều hòn đảo.",
                    "explanation": "'war' (Präteritum 'sein'); 'sind … gefahren'; 'haben … gesehen'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Chuyến đi dài nhưng đẹp. Chúng tôi đã đi bằng tàu thủy và đã nhìn thấy nhiều hòn đảo."
                            ],
                            "translation": "Chuyến đi dài nhưng đẹp. Chúng tôi đã đi bằng tàu thủy và đã nhìn thấy nhiều hòn đảo."
                    }
            },
            {
                    "type": "dich_cau_dv",
                    "question": "Câu 77: Dịch câu sau sang tiếng Việt: „Mein Opa hat früher in einem Dorf in den Bergen gewohnt.“",
                    "options": null,
                    "correct_answer": "Ông tôi ngày trước đã sống trong một ngôi làng trên núi.",
                    "explanation": "'früher' = ngày trước; 'wohnen → hat gewohnt' (trạng thái tại chỗ → 'haben').",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Ông tôi ngày trước đã sống trong một ngôi làng trên núi."
                            ],
                            "translation": "Ông tôi ngày trước đã sống trong một ngôi làng trên núi."
                    }
            },
            {
                    "type": "dich_cau_dv",
                    "question": "Câu 78: Dịch đoạn hội thoại sau sang tiếng Việt: „Hast du schon den Koffer gepackt? — Nein, noch nicht. Ich habe zuerst die Fahrkarten gekauft.“",
                    "options": null,
                    "correct_answer": "Bạn đã đóng vali chưa? — Chưa, chưa đâu. Trước tiên tôi đã mua vé.",
                    "explanation": "'schon' = đã … rồi; 'noch nicht' = chưa; 'gepackt', 'gekauft' là Partizip II có quy tắc.",
                    "exp_reward": 25,
                    "extra_data": {
                            "accepted_answers": [
                                    "Bạn đã đóng vali chưa? — Chưa, chưa đâu. Trước tiên tôi đã mua vé."
                            ],
                            "translation": "Bạn đã đóng vali chưa? — Chưa, chưa đâu. Trước tiên tôi đã mua vé."
                    }
            },
            {
                    "type": "sap_xep_cau",
                    "question": "Câu 79: Sắp xếp các từ sau thành câu Perfekt hoàn chỉnh: [geschrieben, ich, Gestern, Postkarten, habe]",
                    "options": null,
                    "correct_answer": "Gestern habe ich Postkarten geschrieben.",
                    "explanation": "Có thể mở đầu bằng 'Gestern' (khi đó 'habe' ở vị trí 2, 'ich' đứng sau) hoặc bằng 'Ich'; 'geschrieben' luôn ở cuối.",
                    "exp_reward": 20,
                    "extra_data": {
                            "tokens": [
                                    "geschrieben",
                                    "ich",
                                    "Gestern",
                                    "Postkarten",
                                    "habe"
                            ],
                            "accepted_answers": [
                                    "Gestern habe ich Postkarten geschrieben.",
                                    "Ich habe gestern Postkarten geschrieben."
                            ],
                            "translation": "Hôm qua tôi đã viết bưu thiếp."
                    }
            },
            {
                    "type": "sap_xep_cau",
                    "question": "Câu 80: Sắp xếp các từ sau thành câu Perfekt hoàn chỉnh: [gefahren, nach Köln, Wir, am Wochenende, sind]",
                    "options": null,
                    "correct_answer": "Wir sind am Wochenende nach Köln gefahren.",
                    "explanation": "'sind' ở vị trí 2, 'gefahren' ở cuối câu; 'am Wochenende' có thể đứng đầu câu (đảo ngữ).",
                    "exp_reward": 20,
                    "extra_data": {
                            "tokens": [
                                    "gefahren",
                                    "nach Köln",
                                    "Wir",
                                    "am Wochenende",
                                    "sind"
                            ],
                            "accepted_answers": [
                                    "Wir sind am Wochenende nach Köln gefahren.",
                                    "Am Wochenende sind wir nach Köln gefahren."
                            ],
                            "translation": "Cuối tuần chúng tôi đã đi Köln."
                    }
            },
            {
                    "type": "sap_xep_cau",
                    "question": "Câu 81: Sắp xếp các từ sau thành câu Perfekt hoàn chỉnh: [gespielt, Die Kinder, im Meer, haben]",
                    "options": null,
                    "correct_answer": "Die Kinder haben im Meer gespielt.",
                    "explanation": "'haben' ở vị trí 2; 'gespielt' cuối câu.",
                    "exp_reward": 20,
                    "extra_data": {
                            "tokens": [
                                    "gespielt",
                                    "Die Kinder",
                                    "im Meer",
                                    "haben"
                            ],
                            "accepted_answers": [
                                    "Die Kinder haben im Meer gespielt.",
                                    "Im Meer haben die Kinder gespielt."
                            ],
                            "translation": "Bọn trẻ đã chơi dưới biển."
                    }
            },
            {
                    "type": "sap_xep_cau",
                    "question": "Câu 82: Sắp xếp các từ sau thành câu Perfekt hoàn chỉnh: [gegangen, nicht, Wir, ins Museum, sind]",
                    "options": null,
                    "correct_answer": "Wir sind nicht ins Museum gegangen.",
                    "explanation": "'nicht' đứng trước bổ ngữ chỉ hướng 'ins Museum'; 'gegangen' ở cuối câu.",
                    "exp_reward": 20,
                    "extra_data": {
                            "tokens": [
                                    "gegangen",
                                    "nicht",
                                    "Wir",
                                    "ins Museum",
                                    "sind"
                            ],
                            "accepted_answers": [
                                    "Wir sind nicht ins Museum gegangen."
                            ],
                            "translation": "Chúng tôi đã không đi vào viện bảo tàng."
                    }
            },
            {
                    "type": "sap_xep_cau",
                    "question": "Câu 83: Sắp xếp các từ sau thành câu Perfekt hoàn chỉnh: [gemacht, du, Hast, viele Fotos, im Urlaub]",
                    "options": null,
                    "correct_answer": "Hast du im Urlaub viele Fotos gemacht?",
                    "explanation": "Câu hỏi Ja/Nein bắt đầu bằng trợ động từ 'Hast', tiếp theo là 'du'; 'gemacht' cuối câu.",
                    "exp_reward": 20,
                    "extra_data": {
                            "tokens": [
                                    "gemacht",
                                    "du",
                                    "Hast",
                                    "viele Fotos",
                                    "im Urlaub"
                            ],
                            "accepted_answers": [
                                    "Hast du im Urlaub viele Fotos gemacht?",
                                    "Hast du viele Fotos im Urlaub gemacht?"
                            ],
                            "translation": "Bạn đã chụp nhiều ảnh trong kỳ nghỉ chứ?"
                    }
            },
            {
                    "type": "sap_xep_cau",
                    "question": "Câu 84: Sắp xếp các từ sau thành câu Perfekt hoàn chỉnh: [angekommen, Die Gäste, um zehn Uhr, sind]",
                    "options": null,
                    "correct_answer": "Die Gäste sind um zehn Uhr angekommen.",
                    "explanation": "'ankommen' dùng 'sein'; Partizip II 'angekommen' nằm cuối câu.",
                    "exp_reward": 20,
                    "extra_data": {
                            "tokens": [
                                    "angekommen",
                                    "Die Gäste",
                                    "um zehn Uhr",
                                    "sind"
                            ],
                            "accepted_answers": [
                                    "Die Gäste sind um zehn Uhr angekommen.",
                                    "Um zehn Uhr sind die Gäste angekommen."
                            ],
                            "translation": "Các vị khách đã đến nơi lúc mười giờ."
                    }
            },
            {
                    "type": "chon_haben_sein",
                    "question": "Câu 85: Xếp 4 động từ sau vào trợ động từ haben hoặc sein tương ứng (ngăn cách bởi dấu /): fahren (đi xe), machen (làm), bleiben (ở lại), essen (ăn)",
                    "options": null,
                    "correct_answer": "sein / haben / sein / haben",
                    "explanation": "'fahren' chuyển động; 'bleiben' là một trong ba động từ 'sein/bleiben/werden'; 'machen' và 'essen' có tân ngữ nên dùng 'haben'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "items": [
                                    {
                                            "verb": "fahren",
                                            "meaning_vi": "đi xe",
                                            "aux": "sein",
                                            "partizip": "ist gefahren"
                                    },
                                    {
                                            "verb": "machen",
                                            "meaning_vi": "làm",
                                            "aux": "haben",
                                            "partizip": "hat gemacht"
                                    },
                                    {
                                            "verb": "bleiben",
                                            "meaning_vi": "ở lại",
                                            "aux": "sein",
                                            "partizip": "ist geblieben"
                                    },
                                    {
                                            "verb": "essen",
                                            "meaning_vi": "ăn",
                                            "aux": "haben",
                                            "partizip": "hat gegessen"
                                    }
                            ],
                            "accepted_answers": [
                                    "sein / haben / sein / haben",
                                    "sein haben sein haben",
                                    "sein, haben, sein, haben"
                            ],
                            "translation": "Đáp án chuẩn: sein / haben / sein / haben"
                    }
            },
            {
                    "type": "chon_haben_sein",
                    "question": "Câu 86: Xếp 4 động từ sau vào trợ động từ haben hoặc sein tương ứng (ngăn cách bởi dấu /): einschlafen (ngủ thiếp đi), schlafen (ngủ), fliegen (bay), fotografieren (chụp ảnh)",
                    "options": null,
                    "correct_answer": "sein / haben / sein / haben",
                    "explanation": "'einschlafen' đổi trạng thái; 'schlafen' là trạng thái kéo dài; 'fliegen' chuyển động; 'fotografieren' có tân ngữ.",
                    "exp_reward": 20,
                    "extra_data": {
                            "items": [
                                    {
                                            "verb": "einschlafen",
                                            "meaning_vi": "ngủ thiếp đi",
                                            "aux": "sein",
                                            "partizip": "ist eingeschlafen"
                                    },
                                    {
                                            "verb": "schlafen",
                                            "meaning_vi": "ngủ",
                                            "aux": "haben",
                                            "partizip": "hat geschlafen"
                                    },
                                    {
                                            "verb": "fliegen",
                                            "meaning_vi": "bay",
                                            "aux": "sein",
                                            "partizip": "ist geflogen"
                                    },
                                    {
                                            "verb": "fotografieren",
                                            "meaning_vi": "chụp ảnh",
                                            "aux": "haben",
                                            "partizip": "hat fotografiert"
                                    }
                            ],
                            "accepted_answers": [
                                    "sein / haben / sein / haben",
                                    "sein haben sein haben",
                                    "sein, haben, sein, haben"
                            ],
                            "translation": "Đáp án chuẩn: sein / haben / sein / haben"
                    }
            },
            {
                    "type": "chon_haben_sein",
                    "question": "Câu 87: Xếp 4 động từ sau vào trợ động từ haben hoặc sein tương ứng (ngăn cách bởi dấu /): übernachten (qua đêm), wandern (đi bộ đường dài), aufwachen (thức dậy), besichtigen (tham quan)",
                    "options": null,
                    "correct_answer": "haben / sein / sein / haben",
                    "explanation": "'wandern' chuyển động; 'aufwachen' đổi trạng thái; 'übernachten' (tại chỗ) và 'besichtigen' (có tân ngữ) dùng 'haben'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "items": [
                                    {
                                            "verb": "übernachten",
                                            "meaning_vi": "qua đêm",
                                            "aux": "haben",
                                            "partizip": "hat übernachtet"
                                    },
                                    {
                                            "verb": "wandern",
                                            "meaning_vi": "đi bộ đường dài",
                                            "aux": "sein",
                                            "partizip": "ist gewandert"
                                    },
                                    {
                                            "verb": "aufwachen",
                                            "meaning_vi": "thức dậy",
                                            "aux": "sein",
                                            "partizip": "ist aufgewacht"
                                    },
                                    {
                                            "verb": "besichtigen",
                                            "meaning_vi": "tham quan",
                                            "aux": "haben",
                                            "partizip": "hat besichtigt"
                                    }
                            ],
                            "accepted_answers": [
                                    "haben / sein / sein / haben",
                                    "haben sein sein haben",
                                    "haben, sein, sein, haben"
                            ],
                            "translation": "Đáp án chuẩn: haben / sein / sein / haben"
                    }
            },
            {
                    "type": "chon_haben_sein",
                    "question": "Câu 88: Xếp 4 động từ sau vào trợ động từ haben hoặc sein tương ứng (ngăn cách bởi dấu /): passieren (xảy ra), bezahlen (trả tiền), kommen (đến), regnen (mưa)",
                    "options": null,
                    "correct_answer": "sein / haben / sein / haben",
                    "explanation": "'passieren' và 'kommen' dùng 'sein'; 'bezahlen' có tân ngữ; 'regnen' là động từ thời tiết dùng 'haben'.",
                    "exp_reward": 20,
                    "extra_data": {
                            "items": [
                                    {
                                            "verb": "passieren",
                                            "meaning_vi": "xảy ra",
                                            "aux": "sein",
                                            "partizip": "ist passiert"
                                    },
                                    {
                                            "verb": "bezahlen",
                                            "meaning_vi": "trả tiền",
                                            "aux": "haben",
                                            "partizip": "hat bezahlt"
                                    },
                                    {
                                            "verb": "kommen",
                                            "meaning_vi": "đến",
                                            "aux": "sein",
                                            "partizip": "ist gekommen"
                                    },
                                    {
                                            "verb": "regnen",
                                            "meaning_vi": "mưa",
                                            "aux": "haben",
                                            "partizip": "hat geregnet"
                                    }
                            ],
                            "accepted_answers": [
                                    "sein / haben / sein / haben",
                                    "sein haben sein haben",
                                    "sein, haben, sein, haben"
                            ],
                            "translation": "Đáp án chuẩn: sein / haben / sein / haben"
                    }
            },
            {
                    "type": "tim_loi_sai",
                    "question": "Câu 89: Tìm đúng 1 lỗi sai và gõ lại cả câu đúng: „Wir haben gestern nach Berlin gefahren.“",
                    "options": null,
                    "correct_answer": "Wir sind gestern nach Berlin gefahren.",
                    "explanation": "Lỗi trợ động từ: 'fahren' là chuyển động đổi vị trí nên phải dùng 'sind', không phải 'haben'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "wrong_sentence": "Wir haben gestern nach Berlin gefahren.",
                            "accepted_answers": [
                                    "Wir sind gestern nach Berlin gefahren.",
                                    "Gestern sind wir nach Berlin gefahren."
                            ],
                            "translation": "Hôm qua chúng tôi đã đi Berlin."
                    }
            },
            {
                    "type": "tim_loi_sai",
                    "question": "Câu 90: Tìm đúng 1 lỗi sai và gõ lại cả câu đúng: „Ich habe im Urlaub viele Fotos gemachen.“",
                    "options": null,
                    "correct_answer": "Ich habe im Urlaub viele Fotos gemacht.",
                    "explanation": "Lỗi Partizip II: động từ có quy tắc là 'ge' + gốc + 't' = 'gemacht', không phải 'gemachen'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "wrong_sentence": "Ich habe im Urlaub viele Fotos gemachen.",
                            "accepted_answers": [
                                    "Ich habe im Urlaub viele Fotos gemacht."
                            ],
                            "translation": "Tôi đã chụp nhiều ảnh trong kỳ nghỉ."
                    }
            },
            {
                    "type": "tim_loi_sai",
                    "question": "Câu 91: Tìm đúng 1 lỗi sai và gõ lại cả câu đúng: „Sie hat ein Picknick gemacht am Fluss.“",
                    "options": null,
                    "correct_answer": "Sie hat am Fluss ein Picknick gemacht.",
                    "explanation": "Lỗi vị trí động từ: 'gemacht' (Partizip II) phải đứng cuối câu, sau cả cụm 'am Fluss'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "wrong_sentence": "Sie hat ein Picknick gemacht am Fluss.",
                            "accepted_answers": [
                                    "Sie hat am Fluss ein Picknick gemacht.",
                                    "Sie hat ein Picknick am Fluss gemacht."
                            ],
                            "translation": "Cô ấy đã dã ngoại bên sông."
                    }
            },
            {
                    "type": "tim_loi_sai",
                    "question": "Câu 92: Tìm đúng 1 lỗi sai và gõ lại cả câu đúng: „Wir haben die Rechnung gebezahlt.“",
                    "options": null,
                    "correct_answer": "Wir haben die Rechnung bezahlt.",
                    "explanation": "Lỗi Partizip II: 'bezahlen' có tiền tố 'be-' không tách nên không có 'ge-' → 'bezahlt'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "wrong_sentence": "Wir haben die Rechnung gebezahlt.",
                            "accepted_answers": [
                                    "Wir haben die Rechnung bezahlt."
                            ],
                            "translation": "Chúng tôi đã trả hóa đơn."
                    }
            },
            {
                    "type": "viet_lai_perfekt",
                    "question": "Câu 93: Viết lại câu sau sang thì Perfekt: „Ich besuche meine Tante in Bremen.“",
                    "options": null,
                    "correct_answer": "Ich habe meine Tante in Bremen besucht.",
                    "explanation": "'besuchen' → 'haben' + 'besucht' (tiền tố 'be-', không 'ge-'), Partizip II đứng cuối câu.",
                    "exp_reward": 25,
                    "extra_data": {
                            "source_sentence": "Ich besuche meine Tante in Bremen.",
                            "accepted_answers": [
                                    "Ich habe meine Tante in Bremen besucht."
                            ],
                            "translation": "Tôi đã thăm dì của tôi ở Bremen."
                    }
            },
            {
                    "type": "viet_lai_perfekt",
                    "question": "Câu 94: Viết lại câu sau sang thì Perfekt: „Maria fährt mit dem Rad zum See.“",
                    "options": null,
                    "correct_answer": "Maria ist mit dem Rad zum See gefahren.",
                    "explanation": "'fahren' chuyển động → 'ist' + 'gefahren'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "source_sentence": "Maria fährt mit dem Rad zum See.",
                            "accepted_answers": [
                                    "Maria ist mit dem Rad zum See gefahren."
                            ],
                            "translation": "Maria đã đạp xe đến hồ."
                    }
            },
            {
                    "type": "viet_lai_perfekt",
                    "question": "Câu 95: Viết lại câu sau sang thì Perfekt: „Die Gäste steigen in Köln aus.“",
                    "options": null,
                    "correct_answer": "Die Gäste sind in Köln ausgestiegen.",
                    "explanation": "'aussteigen' (tách, chuyển động) → 'sind' + 'aus' + 'ge' + 'stiegen' = 'ausgestiegen'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "source_sentence": "Die Gäste steigen in Köln aus.",
                            "accepted_answers": [
                                    "Die Gäste sind in Köln ausgestiegen."
                            ],
                            "translation": "Các vị khách đã xuống xe ở Köln."
                    }
            },
            {
                    "type": "viet_lai_perfekt",
                    "question": "Câu 96: Viết lại câu sau sang thì Perfekt: „Ihr reserviert den Tisch und telefoniert mit dem Hotel.“",
                    "options": null,
                    "correct_answer": "Ihr habt den Tisch reserviert und mit dem Hotel telefoniert.",
                    "explanation": "Hai động từ đuôi '-ieren' → không 'ge-': 'reserviert', 'telefoniert'; 'ihr' → 'habt'.",
                    "exp_reward": 25,
                    "extra_data": {
                            "source_sentence": "Ihr reserviert den Tisch und telefoniert mit dem Hotel.",
                            "accepted_answers": [
                                    "Ihr habt den Tisch reserviert und mit dem Hotel telefoniert.",
                                    "Ihr habt den Tisch reserviert und habt mit dem Hotel telefoniert."
                            ],
                            "translation": "Các bạn đã đặt bàn và đã gọi điện cho khách sạn."
                    }
            },
            {
                    "type": "dung_sai",
                    "question": "Câu 97: Đọc đoạn văn và xác định mệnh đề sau là Richtig (Đúng) hay Falsch (Sai): „Familie Weber ist mit dem Auto nach Wien gefahren.“",
                    "options": [
                            "Richtig",
                            "Falsch"
                    ],
                    "correct_answer": "Falsch",
                    "explanation": "Trong đoạn văn: „Familie Weber hat … eine Radtour an der Donau gemacht.“ — họ đi bằng xe đạp ('Radtour'), không đi ô tô.",
                    "exp_reward": 15,
                    "extra_data": {
                            "reading_text": "Familie Weber hat im August eine Radtour an der Donau gemacht. Sie sind von Passau nach Wien gefahren. Das Wetter war meistens sonnig, aber in Linz hat es zwei Tage geregnet. Sie haben dort in einer Pension übernachtet und ein Museum besucht. In Wien haben sie das Rathaus fotografiert. Am Ende sind sie mit dem Zug nach Hause gefahren.",
                            "reading_translation_vi": "Gia đình Weber đã đi một chuyến đạp xe dọc sông Donau vào tháng Tám. Họ đã đi từ Passau đến Wien. Thời tiết phần lớn là nắng, nhưng ở Linz trời đã mưa hai ngày. Họ đã ngủ lại ở đó trong một nhà nghỉ và thăm một bảo tàng. Ở Wien họ đã chụp ảnh tòa thị chính. Cuối cùng họ đã đi tàu hỏa về nhà.",
                            "statement": "Familie Weber ist mit dem Auto nach Wien gefahren.",
                            "statement_vi": "Gia đình Weber đã đi Wien bằng ô tô.",
                            "translation": "Gia đình Weber đã đi Wien bằng ô tô."
                    }
            },
            {
                    "type": "dung_sai",
                    "question": "Câu 98: Đọc đoạn văn và xác định mệnh đề sau là Richtig (Đúng) hay Falsch (Sai): „In Linz hat es geregnet.“",
                    "options": [
                            "Richtig",
                            "Falsch"
                    ],
                    "correct_answer": "Richtig",
                    "explanation": "Đoạn văn viết „… aber in Linz hat es zwei Tage geregnet.“",
                    "exp_reward": 15,
                    "extra_data": {
                            "reading_text": "Familie Weber hat im August eine Radtour an der Donau gemacht. Sie sind von Passau nach Wien gefahren. Das Wetter war meistens sonnig, aber in Linz hat es zwei Tage geregnet. Sie haben dort in einer Pension übernachtet und ein Museum besucht. In Wien haben sie das Rathaus fotografiert. Am Ende sind sie mit dem Zug nach Hause gefahren.",
                            "reading_translation_vi": "Gia đình Weber đã đi một chuyến đạp xe dọc sông Donau vào tháng Tám. Họ đã đi từ Passau đến Wien. Thời tiết phần lớn là nắng, nhưng ở Linz trời đã mưa hai ngày. Họ đã ngủ lại ở đó trong một nhà nghỉ và thăm một bảo tàng. Ở Wien họ đã chụp ảnh tòa thị chính. Cuối cùng họ đã đi tàu hỏa về nhà.",
                            "statement": "In Linz hat es geregnet.",
                            "statement_vi": "Ở Linz trời đã mưa.",
                            "translation": "Ở Linz trời đã mưa."
                    }
            },
            {
                    "type": "dung_sai",
                    "question": "Câu 99: Đọc đoạn văn và xác định mệnh đề sau là Richtig (Đúng) hay Falsch (Sai): „Sie waren zwei Wochen in Barcelona.“",
                    "options": [
                            "Richtig",
                            "Falsch"
                    ],
                    "correct_answer": "Falsch",
                    "explanation": "Đoạn văn viết „Wir waren eine Woche in Barcelona.“ — chỉ một tuần.",
                    "exp_reward": 15,
                    "extra_data": {
                            "reading_text": "Lukas und Sophie waren letzten Sommer auf der Insel Rügen an der Ostsee. Sie haben zwei Wochen auf einem Campingplatz gezeltet. Sie sind jeden Tag im Meer geschwommen und haben am Strand Volleyball gespielt. Lukas hat viele Fotos vom Sonnenuntergang gemacht. Das Essen im Restaurant war sehr lecker, aber die Rechnung war teuer. Trotzdem hatten sie viel Spaß.",
                            "reading_translation_vi": "Lukas và Sophie đã ở trên đảo Rügen bên biển Baltic vào mùa hè năm ngoái. Họ đã cắm trại hai tuần trên một khu cắm trại. Họ đã bơi ở biển mỗi ngày và đã chơi bóng chuyền ở bãi biển. Lukas đã chụp nhiều ảnh hoàng hôn. Đồ ăn ở nhà hàng rất ngon, nhưng hóa đơn thì đắt. Dù vậy họ đã có rất nhiều niềm vui.",
                            "statement": "Sie waren zwei Wochen in Barcelona.",
                            "statement_vi": "Họ đã ở Barcelona hai tuần.",
                            "translation": "Họ đã ở Barcelona hai tuần."
                    }
            },
            {
                    "type": "dung_sai",
                    "question": "Câu 100: Đọc đoạn văn và xác định mệnh đề sau là Richtig (Đúng) hay Falsch (Sai): „Sie haben viel gegessen und getanzt.“",
                    "options": [
                            "Richtig",
                            "Falsch"
                    ],
                    "correct_answer": "Richtig",
                    "explanation": "Đoạn văn viết „Wir haben viel gegessen, getanzt und am Strand gelegen.“\n\n---",
                    "exp_reward": 15,
                    "extra_data": {
                            "reading_text": "Lukas und Sophie waren letzten Sommer auf der Insel Rügen an der Ostsee. Sie haben zwei Wochen auf einem Campingplatz gezeltet. Sie sind jeden Tag im Meer geschwommen und haben am Strand Volleyball gespielt. Lukas hat viele Fotos vom Sonnenuntergang gemacht. Das Essen im Restaurant war sehr lecker, aber die Rechnung war teuer. Trotzdem hatten sie viel Spaß.",
                            "reading_translation_vi": "Lukas và Sophie đã ở trên đảo Rügen bên biển Baltic vào mùa hè năm ngoái. Họ đã cắm trại hai tuần trên một khu cắm trại. Họ đã bơi ở biển mỗi ngày và đã chơi bóng chuyền ở bãi biển. Lukas đã chụp nhiều ảnh hoàng hôn. Đồ ăn ở nhà hàng rất ngon, nhưng hóa đơn thì đắt. Dù vậy họ đã có rất nhiều niềm vui.",
                            "statement": "Sie haben viel gegessen und getanzt.",
                            "statement_vi": "Họ đã ăn nhiều và đã nhảy.",
                            "translation": "Họ đã ăn nhiều và đã nhảy."
                    }
            }
    ]

    exercises_data = []
    for ex in exercises_raw:
        opts_str = json.dumps(ex["options"], ensure_ascii=False) if ex.get("options") else None
        extra_str = json.dumps(ex["extra_data"], ensure_ascii=False) if ex.get("extra_data") else None
        exercises_data.append((
            lesson_id,
            ex["type"],
            ex["question"],
            opts_str,
            ex["correct_answer"],
            ex["explanation"],
            ex["exp_reward"],
            extra_str
        ))

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises_data)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công Bài 9: 'Du lịch - Perfekt & Präteritum' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 14 dạng!")

if __name__ == "__main__":
    seed_lesson_9()
