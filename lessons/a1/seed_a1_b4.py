import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_4():
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
        return
    a1_id = level_a1["id"]

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 4%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 18

    # Xóa dữ liệu cũ của Bài 4 để cập nhật sạch sẽ
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM lessons WHERE id = ?;", (lesson_id,))

    lesson_title = 'Bài 4: "Menschen und Häuser - Nhà Ở, Cách 1 Nominativ / Cách 4 Akkusativ & Mạo Từ Sở Hữu"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (7 HỌC PHẦN CHUẨN ĐẶC TẢ - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 4 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Ngữ Pháp Cốt Lõi: Nominativ & Akkusativ • Mạo Từ Sở Hữu (Bài 4)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 85 phút • ⚡ 850+ EXP
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Menschen und Häuser • Nhà Ở, Cách 1 (Nominativ) vs. Cách 4 (Akkusativ) & Mạo Từ Sở Hữu
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Làm chủ toàn diện danh từ không gian sống (nhà ở, các phòng <i>-zimmer</i>, đồ nội thất và 9 cặp tính từ đối lập); thấu hiểu bản chất ngữ pháp của <b>Cách 1 (Nominativ - Chủ ngữ)</b> và <b>Cách 4 (Akkusativ - Tân ngữ trực tiếp)</b>; nắm vững <i>Quy luật Vàng</i>: 90% mạo từ giữ nguyên, chỉ duy nhất giống đực (<b>der</b>) đổi sang đuôi <b>-en</b> (<i>den, einen, keinen</i>); làm chủ hệ thống <b>Mạo từ sở hữu (Possessivartikel)</b> theo 9 ngôi nhân xưng và quy tắc lược bỏ chữ <i>e</i> của ngôi <i>ihr → eure / euren</i>; giải mã ngữ pháp bức thư kinh điển của Julia gửi Claudia và tự tin miêu tả trọn vẹn ngôi nhà của bạn.
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: TỪ VỰNG CHỦ ĐỀ NHÀ Ở & CÁC PHÒNG (MENSCHEN UND HÄUSER) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Từ Vựng Chủ Đề Nhà Ở & Các Phòng Trong Nhà</h4>
            </div>

            <p class="text-xs sm:text-sm text-slate-600">
                Trong tiếng Đức, mọi không gian sống đều được phân chia theo 3 giống (<b>der</b> - Đực, <b>die</b> - Cái, <b>das</b> - Trung). Dưới đây là bảng phân loại chuẩn xác kèm dạng số nhiều:
            </p>

            <!-- Bảng phân loại danh từ theo 3 giống -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs sm:text-sm">
                <!-- Giống Đực (der) -->
                <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-2.5">
                    <div class="flex items-center justify-between border-b border-blue-200 pb-2">
                        <span class="font-extrabold text-blue-800">🔵 Giống Đực (der)</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-blue-200/60 text-blue-900">Maskulinum</span>
                    </div>
                    <ul class="space-y-2 text-slate-800">
                        <li class="flex items-start justify-between gap-1">
                            <div><b>der Garten</b> <span class="text-slate-500 text-xs">(Pl: die Gärten)</span><br><span class="text-xs text-slate-600">Khu vườn (biến âm a→ä)</span></div>
                            <button onclick="speakGerman('der Garten')" class="p-1 rounded bg-blue-100 hover:bg-blue-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>der Balkon</b> <span class="text-slate-500 text-xs">(Pl: die Balkone)</span><br><span class="text-xs text-slate-600">Ban công</span></div>
                            <button onclick="speakGerman('der Balkon')" class="p-1 rounded bg-blue-100 hover:bg-blue-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>der Flur</b> <span class="text-slate-500 text-xs">(Pl: die Flure)</span><br><span class="text-xs text-slate-600">Hành lang</span></div>
                            <button onclick="speakGerman('der Flur')" class="p-1 rounded bg-blue-100 hover:bg-blue-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>der Keller</b> <span class="text-slate-500 text-xs">(Pl: die Keller)</span><br><span class="text-xs text-slate-600">Tầng hầm (đuôi -er giữ nguyên)</span></div>
                            <button onclick="speakGerman('der Keller')" class="p-1 rounded bg-blue-100 hover:bg-blue-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>der Stock</b> <span class="text-slate-500 text-xs">(Pl: die Stöcke; hoặc das Stockwerk, Pl: die Stockwerke)</span><br><span class="text-xs text-slate-600">Tầng lầu (ở Đức: das Erdgeschoss = tầng trệt, nên der 1. Stock = lầu 1 / tầng 2)</span></div>
                            <button onclick="speakGerman('der Stock')" class="p-1 rounded bg-blue-100 hover:bg-blue-200 text-xs cursor-pointer">🔊</button>
                        </li>
                    </ul>
                </div>

                <!-- Giống Cái (die) -->
                <div class="p-4 rounded-2xl bg-rose-50/60 border border-rose-200 space-y-2.5">
                    <div class="flex items-center justify-between border-b border-rose-200 pb-2">
                        <span class="font-extrabold text-rose-800">🔴 Giống Cái (die)</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-rose-200/60 text-rose-900">Femininum</span>
                    </div>
                    <ul class="space-y-2 text-slate-800">
                        <li class="flex items-start justify-between gap-1">
                            <div><b>die Wohnung</b> <span class="text-slate-500 text-xs">(Pl: die Wohnungen)</span><br><span class="text-xs text-slate-600">Căn hộ (hậu tố -ung luôn là die)</span></div>
                            <button onclick="speakGerman('die Wohnung')" class="p-1 rounded bg-rose-100 hover:bg-rose-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>die Küche</b> <span class="text-slate-500 text-xs">(Pl: die Küchen)</span><br><span class="text-xs text-slate-600">Phòng bếp / Nhà bếp</span></div>
                            <button onclick="speakGerman('die Küche')" class="p-1 rounded bg-rose-100 hover:bg-rose-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>die Garage</b> <span class="text-slate-500 text-xs">(Pl: die Garagen)</span><br><span class="text-xs text-slate-600">Ga-ra ô tô</span></div>
                            <button onclick="speakGerman('die Garage')" class="p-1 rounded bg-rose-100 hover:bg-rose-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>die Terrasse</b> <span class="text-slate-500 text-xs">(Pl: die Terrassen)</span><br><span class="text-xs text-slate-600">Hiên nhà / Sân hiên</span></div>
                            <button onclick="speakGerman('die Terrasse')" class="p-1 rounded bg-rose-100 hover:bg-rose-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>die Toilette</b> <span class="text-slate-500 text-xs">(Pl: die Toiletten)</span><br><span class="text-xs text-slate-600">Nhà vệ sinh</span></div>
                            <button onclick="speakGerman('die Toilette')" class="p-1 rounded bg-rose-100 hover:bg-rose-200 text-xs cursor-pointer">🔊</button>
                        </li>
                    </ul>
                </div>

                <!-- Giống Trung (das) -->
                <div class="p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200 space-y-2.5">
                    <div class="flex items-center justify-between border-b border-emerald-200 pb-2">
                        <span class="font-extrabold text-emerald-800">🟢 Giống Trung (das)</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-emerald-200/60 text-emerald-900">Neutrum</span>
                    </div>
                    <ul class="space-y-2 text-slate-800">
                        <li class="flex items-start justify-between gap-1">
                            <div><b>das Haus</b> <span class="text-slate-500 text-xs">(Pl: die Häuser)</span><br><span class="text-xs text-slate-600">Ngôi nhà (biến âm au→äu + er)</span></div>
                            <button onclick="speakGerman('das Haus')" class="p-1 rounded bg-emerald-100 hover:bg-emerald-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>das Zimmer</b> <span class="text-slate-500 text-xs">(Pl: die Zimmer)</span><br><span class="text-xs text-slate-600">Căn phòng (số nhiều giữ nguyên)</span></div>
                            <button onclick="speakGerman('das Zimmer')" class="p-1 rounded bg-emerald-100 hover:bg-emerald-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>das Fenster</b> <span class="text-slate-500 text-xs">(Pl: die Fenster)</span><br><span class="text-xs text-slate-600">Cửa sổ (số nhiều giữ nguyên)</span></div>
                            <button onclick="speakGerman('das Fenster')" class="p-1 rounded bg-emerald-100 hover:bg-emerald-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>das Wohnheim</b> <span class="text-slate-500 text-xs">(Pl: die Wohnheime)</span><br><span class="text-xs text-slate-600">Ký túc xá (das Heim)</span></div>
                            <button onclick="speakGerman('das Wohnheim')" class="p-1 rounded bg-emerald-100 hover:bg-emerald-200 text-xs cursor-pointer">🔊</button>
                        </li>
                        <li class="flex items-start justify-between gap-1">
                            <div><b>das Bad</b> <span class="text-slate-500 text-xs">(Pl: die Bäder)</span><br><span class="text-xs text-slate-600">Phòng tắm (cũng: bồn tắm, việc tắm; = das Badezimmer)</span></div>
                            <button onclick="speakGerman('das Bad')" class="p-1 rounded bg-emerald-100 hover:bg-emerald-200 text-xs cursor-pointer">🔊</button>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Quy tắc danh từ ghép với -zimmer -->
            <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 text-xs sm:text-sm space-y-2">
                <div class="flex items-center gap-2 text-amber-900 font-extrabold">
                    <span>💡 Quy tắc Vàng về Danh từ Ghép (Komposita mit "-zimmer"):</span>
                </div>
                <p class="text-slate-700">
                    Vì từ gốc đứng cuối cùng là <b>das Zimmer</b> (căn phòng - giống trung, số nhiều <b>die Zimmer</b> giữ nguyên), nên <b>TẤT CẢ các phòng ghép với đuôi -zimmer đều mang giống trung (das)</b> và <b>dạng số nhiều luôn giữ nguyên không thêm đuôi</b>:
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2 pt-1 font-mono text-xs">
                    <div class="p-2 bg-white rounded-lg border border-amber-200/80"><b>das Wohnzimmer</b>: Phòng khách</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200/80"><b>das Badezimmer</b>: Phòng tắm</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200/80"><b>das Schlafzimmer</b>: Phòng ngủ</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200/80"><b>das Esszimmer</b>: Phòng ăn</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200/80"><b>das Arbeitszimmer</b>: Phòng làm việc</div>
                    <div class="p-2 bg-white rounded-lg border border-amber-200/80"><b>das Kinderzimmer</b>: Phòng trẻ em</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: HỆ THỐNG 4 CÁCH & SO SÁNH NOMINATIV (CÁCH 1) VS. AKKUSATIV (CÁCH 4) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Hệ Thống 4 Cách Trong Tiếng Đức & Trọng Tâm Nominativ vs. Akkusativ</h4>
            </div>

            <!-- Bảng 4 cách -->
            <div class="overflow-x-auto rounded-2xl border border-slate-200 shadow-xs">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 text-slate-800 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3">Ký hiệu</th>
                            <th class="p-3">Tên tiếng Đức</th>
                            <th class="p-3">Tên tiếng Việt</th>
                            <th class="p-3">Chức năng cốt lõi</th>
                            <th class="p-3">Câu hỏi nhận diện</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="bg-indigo-50/40">
                            <td class="p-3 font-black text-indigo-700">C1</td>
                            <td class="p-3 font-bold">Nominativ</td>
                            <td class="p-3">Chủ ngữ cách</td>
                            <td class="p-3">Chủ ngữ thực hiện hành động; đứng sau động từ nối <b>sein</b> (bin, ist, sind...)</td>
                            <td class="p-3 font-mono text-indigo-600">Wer? (Ai?) / Was? (Cái gì?)</td>
                        </tr>
                        <tr class="text-slate-500">
                            <td class="p-3 font-semibold">C2</td>
                            <td class="p-3 font-medium">Genitiv</td>
                            <td class="p-3">Sở hữu cách</td>
                            <td class="p-3">Biểu thị quyền sở hữu (ở A1 thường dùng cấu trúc <i>von + Dativ</i>)</td>
                            <td class="p-3 font-mono">Wessen? (Của ai?)</td>
                        </tr>
                        <tr class="text-slate-500">
                            <td class="p-3 font-semibold">C3</td>
                            <td class="p-3 font-medium">Dativ</td>
                            <td class="p-3">Tân ngữ gián tiếp</td>
                            <td class="p-3">Người/vật nhận tác động gián tiếp; đứng sau giới từ luôn đi với Dativ (<i>mit, aus, bei, zu...</i>)</td>
                            <td class="p-3 font-mono">Wem? (Cho ai?)<br><span class="text-[11px] text-slate-500 font-sans italic block pt-0.5">(Ghi chú: Giới từ 2 chiều in, an, auf... + Dativ khi hỏi vị trí tĩnh "Wo? - Ở đâu?")</span></td>
                        </tr>
                        <tr class="bg-rose-50/40">
                            <td class="p-3 font-black text-rose-700">C4</td>
                            <td class="p-3 font-bold">Akkusativ</td>
                            <td class="p-3">Tân ngữ trực tiếp</td>
                            <td class="p-3">Chịu tác động trực tiếp của ngoại động từ (<b>haben, finden, brauchen, suchen, kaufen, sehen, es gibt...</b>)</td>
                            <td class="p-3 font-mono text-rose-600">Wen? (Ai?) / Was? (Cái gì?)<br><span class="text-[11px] text-slate-500 font-sans italic block pt-0.5">(Ghi chú: Giới từ 2 chiều + Akkusativ khi hỏi hướng chuyển động "Wohin? - Đi đâu?")</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- QUY LUẬT VÀNG KHI CHUYỂN C1 -> C4 -->
            <div class="p-5 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50 border-2 border-amber-300 space-y-3">
                <div class="flex items-center gap-2 text-amber-900 font-black text-sm sm:text-base">
                    <span>🔥 QUY LUẬT VÀNG KHI CHUYỂN TỪ NOMINATIV SANG AKKUSATIV:</span>
                </div>
                <div class="text-xs sm:text-sm text-slate-800 space-y-1.5 leading-relaxed">
                    <p>• <b>Chỉ duy nhất Giống Đực (der) bị biến đổi mạo từ sang đuôi <u>-en</u>:</b></p>
                    <div class="pl-4 font-mono font-bold space-y-0.5 text-rose-700 text-xs sm:text-sm">
                        <div>der → <span class="bg-rose-100 px-1.5 py-0.5 rounded text-rose-900">den</span> (Mạo từ xác định)</div>
                        <div>ein → <span class="bg-rose-100 px-1.5 py-0.5 rounded text-rose-900">einen</span> (Mạo từ bất định)</div>
                        <div>kein → <span class="bg-rose-100 px-1.5 py-0.5 rounded text-rose-900">keinen</span> (Mạo từ phủ định)</div>
                        <div>mein / dein / sein... → <span class="bg-rose-100 px-1.5 py-0.5 rounded text-rose-900">meinen / deinen / seinen...</span> (Mạo từ sở hữu)</div>
                    </div>
                    <p class="pt-1.5">• <b>Tất cả các giống còn lại: Giống Cái (die), Giống Trung (das) và Số Nhiều (die Pl.) GIỮ NGUYÊN 100% NHƯ Ở NOMINATIV!</b></p>
                </div>
            </div>

            <!-- BẢNG MA TRẬN ĐỐI CHIẾU 3 LOẠI MẠO TỪ -->
            <div class="space-y-4 pt-2">
                <h5 class="text-sm font-extrabold text-slate-800 uppercase tracking-wider">Bảng Ma Trận Đối Chiếu Chi Tiết 3 Loại Mạo Từ:</h5>
                <div class="overflow-x-auto rounded-2xl border border-slate-200">
                    <table class="w-full text-left text-xs sm:text-sm">
                        <thead class="bg-slate-100 text-slate-800 font-bold border-b border-slate-200">
                            <tr>
                                <th class="p-3">Giống / Số</th>
                                <th class="p-3">Nominativ (Cách 1)</th>
                                <th class="p-3 text-center">→</th>
                                <th class="p-3">Akkusativ (Cách 4)</th>
                                <th class="p-3">Ví dụ thực tế đối chiếu</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            <tr class="bg-blue-50/30">
                                <td class="p-3 font-bold text-blue-800">🔵 Giống Đực (der)</td>
                                <td class="p-3 font-mono"><b>der</b> / <b>ein</b> / <b>kein</b> Garten</td>
                                <td class="p-3 text-center text-rose-600 font-bold">→</td>
                                <td class="p-3 font-mono font-bold text-rose-700 bg-rose-50/50"><b>den</b> / <b>einen</b> / <b>keinen</b> Garten</td>
                                <td class="p-3 text-xs"><i>Der Garten ist groß. → Ich finde <b>den Garten</b> schön.</i></td>
                            </tr>
                            <tr class="bg-rose-50/30">
                                <td class="p-3 font-bold text-rose-800">🔴 Giống Cái (die)</td>
                                <td class="p-3 font-mono"><b>die</b> / <b>eine</b> / <b>keine</b> Küche</td>
                                <td class="p-3 text-center text-slate-400 font-bold">→</td>
                                <td class="p-3 font-mono font-bold text-slate-700"><b>die</b> / <b>eine</b> / <b>keine</b> Küche <span class="text-slate-400 text-xs font-normal">(giữ nguyên)</span></td>
                                <td class="p-3 text-xs"><i>Die Küche ist neu. → Ich finde <b>die Küche</b> zu klein.</i></td>
                            </tr>
                            <tr class="bg-emerald-50/30">
                                <td class="p-3 font-bold text-emerald-800">🟢 Giống Trung (das)</td>
                                <td class="p-3 font-mono"><b>das</b> / <b>ein</b> / <b>kein</b> Haus</td>
                                <td class="p-3 text-center text-slate-400 font-bold">→</td>
                                <td class="p-3 font-mono font-bold text-slate-700"><b>das</b> / <b>ein</b> / <b>kein</b> Haus <span class="text-slate-400 text-xs font-normal">(giữ nguyên)</span></td>
                                <td class="p-3 text-xs"><i>Das Haus ist alt. → Wir haben <b>ein Haus</b>.</i></td>
                            </tr>
                            <tr class="bg-purple-50/30">
                                <td class="p-3 font-bold text-purple-800">🟣 Số Nhiều (die Pl.)</td>
                                <td class="p-3 font-mono"><b>die</b> / <b>—</b> / <b>keine</b> Zimmer</td>
                                <td class="p-3 text-center text-slate-400 font-bold">→</td>
                                <td class="p-3 font-mono font-bold text-slate-700"><b>die</b> / <b>—</b> / <b>keine</b> Zimmer <span class="text-slate-400 text-xs font-normal">(giữ nguyên)</span></td>
                                <td class="p-3 text-xs"><i>Hier gibt es <b>keine Toiletten</b>.</i></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: PHÂN TÍCH BỨC THƯ CỦA JULIA GỬI CLAUDIA (THEO SÁT BẢNG VIẾT) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Giải Mã Ngữ Pháp Bức Thư Của Julia Gửi Claudia</h4>
            </div>

            <!-- Khung bức thư nguyên văn -->
            <div class="p-5 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-3 font-serif">
                <div class="text-amber-900 font-bold text-sm uppercase tracking-wider font-sans">✉️ Bức Thư Nguyên Văn (Văn Bản Chuẩn Trên Bảng):</div>
                <div class="text-slate-800 text-sm sm:text-base leading-relaxed pl-2 border-l-4 border-amber-400">
                    <p><i>Liebe Claudia,</i></p>
                    <p class="pt-1.5">
                        <i>wir haben <b>ein</b> Haus. Unser Haus ist sehr alt und hat 5 Zimmer. Oben gibt es <b>einen</b> Balkon. Das Wohnzimmer ist groß, aber ich finde <b>die</b> Küche <b>zu klein</b>. Das Haus hat <b>einen</b> Flur. Er ist lang und dunkel. Wir haben auch <b>einen</b> Garten. Ich finde <b>den</b> Garten sehr schön.</i>
                    </p>
                    <p class="pt-2"><i>Viele Grüße<br>Julia</i></p>
                </div>
                <div class="text-xs text-slate-600 font-sans pt-1 border-t border-amber-200/60">
                    <b>Dịch nghĩa:</b> <i>"Claudia thân mến, chúng mình có một ngôi nhà. Ngôi nhà của chúng mình rất cũ và có 5 phòng. Ở phía trên có một ban công. Phòng khách thì rộng, nhưng mình thấy nhà bếp quá nhỏ. Ngôi nhà có một hành lang. Nó dài và tối. Chúng mình cũng có một khu vườn. Mình thấy khu vườn đó rất đẹp. Thân ái, Julia"</i>
                </div>
            </div>

            <!-- 5 Điểm ngữ pháp đắt giá -->
            <div class="space-y-3 text-xs sm:text-sm">
                <h5 class="font-extrabold text-slate-800">5 Điểm Ngữ Pháp Cốt Lõi Được Rút Ra Từ Bức Thư:</h5>
                <ol class="space-y-2 list-decimal list-inside text-slate-700 leading-relaxed">
                    <li>
                        <b>Chuyển đổi từ lần 1 (bất định) sang lần 2 (xác định / sở hữu):</b><br>
                        <span class="pl-5 text-slate-600 block">Câu trước: <i>"wir haben <b>ein</b> Haus"</i> (nhắc lần đầu sau haben → mạo từ bất định <i>ein</i>). Câu ngay sau: <i>"<b>Unser Haus</b> ist..."</i> (ngôi nhà đã xác định, thuộc sở hữu của ngôi <i>wir</i> và đứng làm chủ ngữ của câu → dùng mạo từ sở hữu <i>Unser</i>).</span>
                    </li>
                    <li>
                        <b>Cấu trúc "es gibt + Akkusativ" (Có / Tồn tại cái gì):</b><br>
                        <span class="pl-5 text-slate-600 block"><i>"Oben gibt es <b>einen</b> Balkon."</i> → <b>oben</b> là trạng từ chỉ nơi chốn (phía trên / tầng trên, trái nghĩa với <b>unten</b>). Vì <i>der Balkon</i> là giống đực, đứng sau <i>es gibt</i> bắt buộc đổi <i>ein → <b>einen Balkon</b></i>.</span>
                    </li>
                    <li>
                        <b>Cấu trúc đánh giá "finden + Akkusativ + Tính từ":</b><br>
                        <span class="pl-5 text-slate-600 block"><i>"...aber ich finde <b>die</b> Küche <b>zu klein</b>."</i> → Căn bếp là giống cái xác định (<i>die Küche</i>), giữ nguyên ở Akkusativ. Phó từ <b>zu + tính từ</b> (<i>zu klein, zu teuer, zu laut</i>) mang sắc thái phàn nàn: "quá mức mong muốn".</span>
                    </li>
                    <li>
                        <b>Đại từ nhân xưng thay thế danh từ theo giống (Er / Sie / Es):</b><br>
                        <span class="pl-5 text-slate-600 block"><i>"Das Haus hat <b>einen Flur</b>. <b>Er</b> ist lang und dunkel."</i> → Đại từ <b>Er</b> ở câu sau thay thế trực tiếp cho danh từ giống đực <i>der Flur</i> (trong tiếng Đức: <i>der → Er, die → Sie, das → Es</i>).</span>
                    </li>
                    <li>
                        <b>Sự biến đổi kinh điển: "einen Garten" (lần 1) → "den Garten" (lần 2):</b><br>
                        <span class="pl-5 text-slate-600 block">Lần 1: <i>"Wir haben auch <b>einen</b> Garten"</i> (mới giới thiệu sau haben → bất định <i>einen</i>). Lần 2: <i>"Ich finde <b>den</b> Garten sehr schön"</i> (khu vườn đã xác định sau finden → xác định <i>den</i>).</span>
                    </li>
                </ol>
            </div>
        </div>

        <!-- HỌC PHẦN 4: HỆ THỐNG MẠO TỪ SỞ HỮU (POSSESSIVARTIKEL) THEO 9 NGÔI & 4 GIỐNG -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-teal-100 text-teal-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Bảng Ma Trận Toàn Diện: Mạo Từ Sở Hữu Theo 9 Ngôi Nhân Xưng</h4>
            </div>

            <p class="text-xs sm:text-sm text-slate-600">
                Để chia mạo từ sở hữu, người học thực hiện 2 bước: <b>(1) Chọn gốc sở hữu</b> theo người sở hữu; <b>(2) Gắn đuôi</b> theo Giống, Số và Cách của danh từ đứng ngay sau nó (giống hệt cách gắn đuôi của từ phủ định <i>kein-</i>).
            </p>

            <!-- BẢNG MA TRẬN 9 NGÔI Ở NOMINATIV (CÁCH 1) -->
            <div class="overflow-x-auto rounded-2xl border border-slate-200 shadow-xs">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 text-slate-800 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3">Ngôi nhân xưng</th>
                            <th class="p-3">Gốc sở hữu</th>
                            <th class="p-3">Giống Đực (der)</th>
                            <th class="p-3">Giống Trung (das)</th>
                            <th class="p-3 text-rose-700">Giống Cái (die) (+e)</th>
                            <th class="p-3 text-purple-700">Số Nhiều (Pl.) (+e)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr>
                            <td class="p-3 font-bold">ich (tôi)</td>
                            <td class="p-3 font-mono text-indigo-600">mein-</td>
                            <td class="p-3">mein Garten</td>
                            <td class="p-3">mein Haus</td>
                            <td class="p-3 font-bold text-rose-700">meine Wohnung</td>
                            <td class="p-3 font-bold text-purple-700">meine Kinder</td>
                        </tr>
                        <tr class="bg-slate-50/50">
                            <td class="p-3 font-bold">du (bạn)</td>
                            <td class="p-3 font-mono text-indigo-600">dein-</td>
                            <td class="p-3">dein Garten</td>
                            <td class="p-3">dein Haus</td>
                            <td class="p-3 font-bold text-rose-700">deine Wohnung</td>
                            <td class="p-3 font-bold text-purple-700">deine Kinder</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold">er / es (anh ấy / nó)</td>
                            <td class="p-3 font-mono text-indigo-600">sein-</td>
                            <td class="p-3">sein Garten</td>
                            <td class="p-3">sein Haus</td>
                            <td class="p-3 font-bold text-rose-700">seine Wohnung</td>
                            <td class="p-3 font-bold text-purple-700">seine Kinder</td>
                        </tr>
                        <tr class="bg-slate-50/50">
                            <td class="p-3 font-bold">sie (cô ấy)</td>
                            <td class="p-3 font-mono text-indigo-600">ihr-</td>
                            <td class="p-3">ihr Garten</td>
                            <td class="p-3">ihr Haus</td>
                            <td class="p-3 font-bold text-rose-700">ihre Wohnung</td>
                            <td class="p-3 font-bold text-purple-700">ihre Kinder</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold">wir (chúng tôi)</td>
                            <td class="p-3 font-mono text-indigo-600">unser-</td>
                            <td class="p-3">unser Garten</td>
                            <td class="p-3">unser Haus</td>
                            <td class="p-3 font-bold text-rose-700">unsere Wohnung</td>
                            <td class="p-3 font-bold text-purple-700">unsere Kinder</td>
                        </tr>
                        <tr class="bg-amber-50/60">
                            <td class="p-3 font-bold text-amber-900">ihr (các bạn) ⚠️</td>
                            <td class="p-3 font-mono text-amber-700 font-bold">euer-</td>
                            <td class="p-3 font-mono">euer Garten</td>
                            <td class="p-3 font-mono">euer Haus</td>
                            <td class="p-3 font-mono font-bold text-rose-700 bg-amber-100/60">eure Wohnung (bỏ e)</td>
                            <td class="p-3 font-mono font-bold text-purple-700 bg-amber-100/60">eure Kinder (bỏ e)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold">sie (họ)</td>
                            <td class="p-3 font-mono text-indigo-600">ihr-</td>
                            <td class="p-3">ihr Garten</td>
                            <td class="p-3">ihr Haus</td>
                            <td class="p-3 font-bold text-rose-700">ihre Wohnung</td>
                            <td class="p-3 font-bold text-purple-700">ihre Kinder</td>
                        </tr>
                        <tr class="bg-indigo-50/40">
                            <td class="p-3 font-bold text-indigo-900">Sie (Ngài / Các Ngài) ⭐</td>
                            <td class="p-3 font-mono font-bold text-indigo-700">Ihr- (VIẾT HOA)</td>
                            <td class="p-3 font-mono">Ihr Garten</td>
                            <td class="p-3 font-mono">Ihr Haus</td>
                            <td class="p-3 font-mono font-bold text-rose-700">Ihre Wohnung</td>
                            <td class="p-3 font-mono font-bold text-purple-700">Ihre Kinder</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- LƯU Ý ĐẶC BIỆT KHI SANG AKKUSATIV -->
            <div class="p-4 rounded-2xl bg-rose-50 border border-rose-200 text-xs sm:text-sm space-y-2">
                <span class="font-extrabold text-rose-900 block">🚨 Khi Đứng Ở Tân Ngữ Akkusativ (Sau haben, finden, suchen, brauchen, kaufen...):</span>
                <p class="text-slate-800">
                    Chỉ duy nhất cột <b>Giống Đực (der)</b> thêm đuôi <b>-en</b>: <i>meinen Garten, deinen Garten, seinen Garten, ihren Garten, unseren Garten, <b>euren Garten (bỏ e)</b>, Ihren Garten</i>. Các cột Giống Trung, Giống Cái và Số Nhiều giữ nguyên 100% như bảng Nominativ trên!
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 5: TỪ VỰNG ĐỒ NỘI THẤT & 9 CẶP TÍNH TỪ ĐỐI LẬP (MÖBEL & ADJEKTIVE) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-orange-100 text-orange-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Đồ Nội Thất (Möbel) & 9 Cặp Tính Từ Đối Lập (Gegenteile)</h4>
            </div>

            <!-- Bảng Đồ Nội Thất -->
            <div class="overflow-x-auto rounded-2xl border border-slate-200 shadow-xs">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 text-slate-800 font-bold border-b border-slate-200">
                        <tr>
                            <th class="p-3">Giống</th>
                            <th class="p-3">Danh từ Nominativ</th>
                            <th class="p-3">Số nhiều (Plural)</th>
                            <th class="p-3">Dạng Akkusativ (sau haben / finden...)</th>
                            <th class="p-3">Nghĩa tiếng Việt</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Schrank</td>
                            <td class="p-3 text-slate-500">die Schränke</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Schrank / den Schrank</td>
                            <td class="p-3">Tủ quần áo / Tủ đồ</td>
                        </tr>
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Kühlschrank</td>
                            <td class="p-3 text-slate-500">die Kühlschränke</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Kühlschrank / den Kühlschrank</td>
                            <td class="p-3">Tủ lạnh (kühl + Schrank)</td>
                        </tr>
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Tisch</td>
                            <td class="p-3 text-slate-500">die Tische</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Tisch / den Tisch</td>
                            <td class="p-3">Cái bàn (Schreibtisch: bàn học)</td>
                        </tr>
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Stuhl</td>
                            <td class="p-3 text-slate-500">die Stühle</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Stuhl / den Stuhl</td>
                            <td class="p-3">Cái ghế (biến âm u→ü + e)</td>
                        </tr>
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Fernseher</td>
                            <td class="p-3 text-slate-500">die Fernseher</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Fernseher / den Fernseher</td>
                            <td class="p-3">Chiếc tivi</td>
                        </tr>
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Teppich</td>
                            <td class="p-3 text-slate-500">die Teppiche</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Teppich / den Teppich</td>
                            <td class="p-3">Tấm thảm (đuôi -ich là der)</td>
                        </tr>
                        <tr class="bg-blue-50/20">
                            <td class="p-3 font-bold text-blue-700">🔵 Đực</td>
                            <td class="p-3 font-bold">der Spiegel</td>
                            <td class="p-3 text-slate-500">die Spiegel</td>
                            <td class="p-3 font-mono font-bold text-rose-700">einen Spiegel / den Spiegel</td>
                            <td class="p-3">Cái gương</td>
                        </tr>
                        <tr class="bg-rose-50/20">
                            <td class="p-3 font-bold text-rose-700">🔴 Cái</td>
                            <td class="p-3 font-bold">die Lampe</td>
                            <td class="p-3 text-slate-500">die Lampen</td>
                            <td class="p-3 font-mono font-bold text-slate-700">eine Lampe</td>
                            <td class="p-3">Cây đèn</td>
                        </tr>
                        <tr class="bg-rose-50/20">
                            <td class="p-3 font-bold text-rose-700">🔴 Cái</td>
                            <td class="p-3 font-bold">die Spüle</td>
                            <td class="p-3 text-slate-500">die Spülen</td>
                            <td class="p-3 font-mono font-bold text-slate-700">eine Spüle</td>
                            <td class="p-3">Bồn rửa bát</td>
                        </tr>
                        <tr class="bg-emerald-50/20">
                            <td class="p-3 font-bold text-emerald-700">🟢 Trung</td>
                            <td class="p-3 font-bold">das Bett</td>
                            <td class="p-3 text-slate-500">die Betten</td>
                            <td class="p-3 font-mono font-bold text-slate-700">ein Bett</td>
                            <td class="p-3">Chiếc giường</td>
                        </tr>
                        <tr class="bg-emerald-50/20">
                            <td class="p-3 font-bold text-emerald-700">🟢 Trung</td>
                            <td class="p-3 font-bold">das Regal / Bücherregal</td>
                            <td class="p-3 text-slate-500">die Regale / die Bücherregale</td>
                            <td class="p-3 font-mono font-bold text-slate-700">ein Regal / ein Bücherregal</td>
                            <td class="p-3">Cái giá / Kệ sách</td>
                        </tr>
                        <tr class="bg-emerald-50/20">
                            <td class="p-3 font-bold text-emerald-700">🟢 Trung</td>
                            <td class="p-3 font-bold">das Sofa</td>
                            <td class="p-3 text-slate-500">die Sofas</td>
                            <td class="p-3 font-mono font-bold text-slate-700">ein Sofa</td>
                            <td class="p-3">Ghế sofa</td>
                        </tr>
                        <tr class="bg-purple-50/20">
                            <td class="p-3 font-bold text-purple-700">🟣 Số nhiều</td>
                            <td class="p-3 font-bold">die Möbel</td>
                            <td class="p-3 text-slate-500">die Möbel (Pl.)</td>
                            <td class="p-3 font-mono font-bold text-slate-700">Möbel / die Möbel</td>
                            <td class="p-3">Đồ nội thất (luôn dùng số nhiều)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Bảng 9 cặp tính từ đối lập -->
            <div class="space-y-3 pt-2">
                <h5 class="text-sm font-extrabold text-slate-800 uppercase tracking-wider">9 Cặp Tính Từ Đối Lập Miêu Tả Nhà Cửa (Gegenteile):</h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-xs sm:text-sm">
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>hell</b> (sáng) >< <b>dunkel</b> (tối)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>groß</b> (lớn/rộng) >< <b>klein</b> (nhỏ/hẹp)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>ruhig</b> (yên tĩnh - phòng/nhà) / <b>leise</b> (nhỏ tiếng) >< <b>laut</b> (ồn ào / to tiếng)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>lang</b> (dài) >< <b>kurz</b> (ngắn)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>neu</b> (mới) >< <b>alt</b> (cũ/cổ)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>billig / günstig</b> (rẻ) >< <b>teuer</b> (đắt)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>schön</b> (đẹp) >< <b>hässlich</b> (xấu)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>modern</b> (hiện đại) >< <b>altmodisch</b> (lỗi thời / kiểu cũ)</div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200"><b>gemütlich</b> (ấm cúng) >< <b>ungemütlich</b> (không ấm cúng / bất tiện)</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 6: BÀI DỊCH MẪU MIÊU TẢ NGÔI NHÀ CỦA TÔI (THEO SÁT BẢNG VIẾT) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">6</span>
                <h4 class="text-lg font-bold text-slate-900">Bài Dịch Mẫu Miêu Tả Ngôi Nhà Của Tôi (5 Câu Cốt Lõi Trên Bảng)</h4>
            </div>

            <p class="text-xs sm:text-sm text-slate-600">
                Đây là bài tập dịch tổng hợp toàn bộ các kỹ năng ngữ pháp của Bài 4 (kết hợp mạo từ sở hữu, động từ <i>sein + tính từ</i>, và ngoại động từ <i>haben + Akkusativ</i>):
            </p>

            <div class="space-y-3 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900">Câu 1: "Tôi có một ngôi nhà. Ngôi nhà của tôi có 4 phòng và 1 phòng bếp: 1 phòng khách, 2 phòng ngủ, 1 phòng làm việc và 1 phòng bếp."</div>
                    <div class="font-mono text-indigo-700 font-bold">→ Ich habe ein Haus. Mein Haus hat vier Zimmer und eine Küche: ein Wohnzimmer, zwei Schlafzimmer, ein Arbeitszimmer und eine Küche.</div>
                    <div class="text-xs text-slate-500">Phân tích: das Haus đứng sau habe (Akkusativ) → ein Haus; làm chủ ngữ (Nominativ) → Mein Haus; die Küche (giống cái) tách riêng với 4 phòng ở (Zimmer) → vier Zimmer und eine Küche.</div>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900">Câu 2: "Phòng khách của tôi thì sáng và hiện đại. Nó có 1 Tivi và 1 giá sách."</div>
                    <div class="font-mono text-indigo-700 font-bold">→ Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher und ein Bücherregal.</div>
                    <div class="text-xs text-slate-500">Phân tích: Đại từ 'Es' thay cho das Wohnzimmer; der Fernseher (giống đực) sau hat đổi thành 'einen Fernseher'; das Bücherregal giữ nguyên 'ein'.</div>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900">Câu 3: "Phòng ngủ của tôi thì ấm cúng và có 1 giường."</div>
                    <div class="font-mono text-indigo-700 font-bold">→ Mein Schlafzimmer ist gemütlich und hat ein Bett.</div>
                    <div class="text-xs text-slate-500">Phân tích: das Schlafzimmer → Mein; das Bett (giống trung) đứng sau hat → ein Bett.</div>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900">Câu 4: "Phòng làm việc của tôi thì nhỏ nhưng sáng. Nó có 1 bàn và 1 ghế."</div>
                    <div class="font-mono text-indigo-700 font-bold">→ Mein Arbeitszimmer ist klein, aber hell. Es hat einen Tisch und einen Stuhl.</div>
                    <div class="text-xs text-slate-500">Phân tích: Liên từ aber nối 2 tính từ trái nghĩa; Cả der Tisch và der Stuhl đều là giống đực nên sau hat đổi thành 'einen Tisch und einen Stuhl'.</div>
                </div>

                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                    <div class="font-bold text-slate-900">Câu 5: "Phòng bếp của tôi thì nhỏ và đẹp."</div>
                    <div class="font-mono text-indigo-700 font-bold">→ Meine Küche ist klein und schön.</div>
                    <div class="text-xs text-slate-500">Phân tích: die Küche là giống cái (die) nên mạo từ sở hữu làm chủ ngữ bắt buộc phải có đuôi -e: Meine Küche.</div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 7: TỔNG KẾT & MẸO GHI NHỚ PHẢN XẠ NHANH A1 -->
        <div class="p-6 rounded-3xl bg-indigo-50/60 border border-indigo-200 shadow-sm space-y-4 text-xs sm:text-sm">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-200 text-indigo-800 flex items-center justify-center font-bold text-sm">7</span>
                <h4 class="text-lg font-bold text-indigo-950">Mẹo Ghi Nhớ Nhanh & Tránh 4 Cạm Bẫy Phổ Biến</h4>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-slate-700">
                <div class="p-4 rounded-2xl bg-white border border-indigo-100 space-y-2">
                    <b class="text-indigo-900">1. Động từ "sein" KHÔNG BAO GIỜ đi với Akkusativ:</b>
                    <p class="text-xs">Sau <i>ist / sind / war / waren</i> luôn là Nominativ: <i>"Das ist <b>ein</b> Garten"</i> (chứ không bao giờ là <i>einen</i>).</p>
                </div>
                <div class="p-4 rounded-2xl bg-white border border-indigo-100 space-y-2">
                    <b class="text-indigo-900">2. Cấu trúc "es gibt" LUÔN LUÔN đòi hỏi Akkusativ:</b>
                    <p class="text-xs">Dù dịch là "có", sau <i>es gibt</i> giống đực luôn là <b>einen / keinen / den</b>: <i>"Oben gibt es <b>einen</b> Balkon"</i>.</p>
                </div>
                <div class="p-4 rounded-2xl bg-white border border-indigo-100 space-y-2">
                    <b class="text-indigo-900">3. Ngôi "ihr" khi thêm đuôi phải rụng chữ "e" ở giữa:</b>
                    <p class="text-xs">Không viết <i>euere / eueren</i> mà phải viết là <b>eure</b> và <b>euren</b>.</p>
                </div>
                <div class="p-4 rounded-2xl bg-white border border-indigo-100 space-y-2">
                    <b class="text-indigo-900">4. Tính từ đứng sau "sein" & "finden" giữ nguyên không chia đuôi:</b>
                    <p class="text-xs"><i>"Ich finde den Garten <b>schön</b>"</i>, <i>"Die Küche ist <b>klein</b>"</i> (không thêm đuôi -e hay -en ở cuối tính từ).</p>
                </div>
            </div>
        </div>
    </div>
    """

    cursor.execute("""
        INSERT INTO lessons (id, level_id, title, grammar_content)
        VALUES (?, ?, ?, ?);
    """, (lesson_id, a1_id, lesson_title, grammar_html))

    # =========================================================================
    # DANH SÁCH TỪ VỰNG BÀI 4 (48 TỪ VỰNG CHUẨN ĐẶC TẢ)
    # =========================================================================
    vocabularies = [
        (lesson_id, "Garten", "der", "khu vườn (Pl: die Gärten)", "Wir haben einen Garten. Ich finde den Garten sehr schön. (Chúng tôi có một khu vườn. Tôi thấy khu vườn rất đẹp.)"),
        (lesson_id, "Balkon", "der", "ban công (Pl: die Balkone)", "Oben gibt es einen Balkon. (Ở phía trên có một ban công.)"),
        (lesson_id, "Flur", "der", "hành lang (Pl: die Flure)", "Das Haus hat einen Flur. Er ist lang und dunkel. (Ngôi nhà có một hành lang. Nó dài và tối.)"),
        (lesson_id, "Keller", "der", "tầng hầm (Pl: die Keller)", "Die Wohnung hat einen Keller. (Căn hộ có một tầng hầm.)"),
        (lesson_id, "Stock", "der", "tầng lầu (Pl: die Stöcke; hoặc das Stockwerk, Pl: die Stockwerke; der erste Stock = lầu 1 / tầng 2)", "Die Wohnung liegt im ersten Stock. (Căn hộ nằm ở lầu 1 / tầng 2.)"),
        (lesson_id, "Wohnung", "die", "căn hộ (Pl: die Wohnungen)", "Wir suchen eine Wohnung in Berlin. (Chúng tôi đang tìm một căn hộ ở Berlin.)"),
        (lesson_id, "Küche", "die", "phòng bếp (Pl: die Küchen)", "Ich finde die Küche zu klein. (Tôi thấy căn bếp quá nhỏ.)"),
        (lesson_id, "Garage", "die", "nhà để xe / ga-ra (Pl: die Garagen)", "Das Haus hat eine Garage. (Ngôi nhà có một nhà để xe.)"),
        (lesson_id, "Terrasse", "die", "sân hiên / hiên nhà (Pl: die Terrassen)", "Wir sitzen auf der Terrasse. (Chúng tôi ngồi trên sân hiên.)"),
        (lesson_id, "Toilette", "die", "nhà vệ sinh (Pl: die Toiletten)", "Hier gibt es keine Toiletten. (Ở đây không có nhà vệ sinh nào.)"),
        (lesson_id, "Haus", "das", "ngôi nhà (Pl: die Häuser)", "Wir haben ein Haus. Unser Haus ist sehr alt. (Chúng tôi có một ngôi nhà. Ngôi nhà của chúng tôi rất cũ.)"),
        (lesson_id, "Zimmer", "das", "căn phòng (Pl: die Zimmer)", "Unser Haus hat 5 Zimmer. (Ngôi nhà của chúng tôi có 5 phòng.)"),
        (lesson_id, "Wohnzimmer", "das", "phòng khách (Pl: die Wohnzimmer)", "Mein Wohnzimmer ist hell und modern. (Phòng khách của tôi sáng sủa và hiện đại.)"),
        (lesson_id, "Schlafzimmer", "das", "phòng ngủ (Pl: die Schlafzimmer)", "Mein Schlafzimmer ist sehr gemütlich. (Phòng ngủ của tôi rất ấm cúng.)"),
        (lesson_id, "Badezimmer", "das", "phòng tắm (Pl: die Badezimmer)", "Das Badezimmer hat ein Fenster. (Phòng tắm có một cửa sổ.)"),
        (lesson_id, "Arbeitszimmer", "das", "phòng làm việc (Pl: die Arbeitszimmer)", "Mein Arbeitszimmer ist klein, aber hell. (Phòng làm việc của tôi nhỏ nhưng sáng sủa.)"),
        (lesson_id, "Esszimmer", "das", "phòng ăn (Pl: die Esszimmer)", "Wir essen im Esszimmer. (Chúng tôi ăn cơm trong phòng ăn.)"),
        (lesson_id, "Kinderzimmer", "das", "phòng trẻ em (Pl: die Kinderzimmer)", "Das Kinderzimmer ist groß. (Phòng trẻ em rộng.)"),
        (lesson_id, "Fenster", "das", "cửa sổ (Pl: die Fenster)", "Das Zimmer hat kein Fenster. (Căn phòng không có cửa sổ.)"),
        (lesson_id, "Wohnheim", "das", "ký túc xá (Pl: die Wohnheime)", "David wohnt im Studentenwohnheim. (David sống trong ký túc xá sinh viên.)"),
        (lesson_id, "Bad", "das", "phòng tắm (cũng: bồn tắm, việc tắm; = das Badezimmer; Pl: die Bäder)", "Im Bad gibt es einen Spiegel. (Trong phòng tắm có một cái gương.)"),
        (lesson_id, "Schrank", "der", "cái tủ (Pl: die Schränke)", "Er kauft einen Schrank. (Anh ấy mua một chiếc tủ.)"),
        (lesson_id, "Kühlschrank", "der", "tủ lạnh (Pl: die Kühlschränke)", "Die Küche hat einen Kühlschrank. (Phòng bếp có một chiếc tủ lạnh.)"),
        (lesson_id, "Tisch", "der", "cái bàn (Pl: die Tische)", "Ich brauche einen Tisch. (Tôi cần một cái bàn.)"),
        (lesson_id, "Stuhl", "der", "cái ghế (Pl: die Stühle)", "Das Arbeitszimmer hat einen Tisch und einen Stuhl. (Phòng làm việc có một cái bàn và một cái ghế.)"),
        (lesson_id, "Teppich", "der", "tấm thảm (Pl: die Teppiche)", "Das Wohnzimmer hat einen Teppich. (Phòng khách có một tấm thảm.)"),
        (lesson_id, "Spiegel", "der", "cái gương (Pl: die Spiegel)", "Im Bad gibt es einen Spiegel. (Trong phòng tắm có một cái gương.)"),
        (lesson_id, "Fernseher", "der", "chiếc tivi (Pl: die Fernseher)", "Das Wohnzimmer hat einen Fernseher. (Phòng khách có một chiếc tivi.)"),
        (lesson_id, "Lampe", "die", "cây đèn (Pl: die Lampen)", "Ich kaufe eine Lampe. (Tôi mua một cây đèn.)"),
        (lesson_id, "Spüle", "die", "bồn rửa bát (Pl: die Spülen)", "Die Küche hat một bồn rửa bát/eine Spüle... (Phòng bếp có một bồn rửa bát.)") if False else (lesson_id, "Spüle", "die", "bồn rửa bát (Pl: die Spülen)", "Die Küche hat eine Spüle. (Phòng bếp có một bồn rửa bát.)"),
        (lesson_id, "Bett", "das", "chiếc giường (Pl: die Betten)", "Mein Schlafzimmer hat ein Bett. (Phòng ngủ của tôi có một chiếc giường.)"),
        (lesson_id, "Regal", "das", "cái kệ / giá (Pl: die Regale)", "Wir haben ein Regal. (Chúng tôi có một cái kệ.)"),
        (lesson_id, "Bücherregal", "das", "kệ sách / giá sách (Pl: die Bücherregale)", "Das Wohnzimmer hat ein Bücherregal. (Phòng khách có một chiếc kệ sách.)"),
        (lesson_id, "Sofa", "das", "ghế sofa (Pl: die Sofas)", "Ich finde das Sofa ein bisschen altmodisch. (Tôi thấy chiếc ghế sofa hơi lỗi thời một chút.)"),
        (lesson_id, "Möbel", "die (Pl.)", "đồ nội thất (luôn dùng số nhiều: die Möbel)", "Die Möbel sind neu. (Đồ nội thất thì mới.)"),
        (lesson_id, "hell", "Adj.", "sáng sủa", "Mein Arbeitszimmer ist hell. (Phòng làm việc của tôi sáng sủa.)"),
        (lesson_id, "dunkel", "Adj.", "tối tăm", "Der Flur ist dunkel. (Hành lang thì tối tăm.)"),
        (lesson_id, "groß", "Adj.", "to, lớn, rộng", "Das Wohnzimmer ist groß. (Phòng khách thì rộng lớn.)"),
        (lesson_id, "klein", "Adj.", "nhỏ, hẹp", "Die Küche ist zu klein. (Căn bếp thì quá nhỏ.)"),
        (lesson_id, "ruhig", "Adj.", "yên tĩnh, thanh bình", "Mein Zimmer ist sehr ruhig. (Phòng của tôi rất yên tĩnh.)"),
        (lesson_id, "laut", "Adj.", "ồn ào, ầm ĩ", "Die Straße ist sehr laut. (Con đường thì rất ồn ào.)"),
        (lesson_id, "lang", "Adj.", "dài", "Der Flur ist lang und dunkel. (Hành lang thì dài và tối.)"),
        (lesson_id, "kurz", "Adj.", "ngắn", "Der Weg ist kurz. (Quãng đường thì ngắn.)"),
        (lesson_id, "neu", "Adj.", "mới", "Die Möbel sind neu. (Đồ nội thất thì mới.)"),
        (lesson_id, "alt", "Adj.", "cũ, lâu năm, già", "Unser Haus ist sehr alt. (Ngôi nhà của chúng tôi rất cũ.)"),
        (lesson_id, "billig", "Adj.", "rẻ", "Das Zimmer hier ist billig. (Căn phòng ở đây thì rẻ.)"),
        (lesson_id, "teuer", "Adj.", "đắt đỏ", "Die Wohnung ist teuer. (Căn hộ thì đắt đỏ.)"),
        (lesson_id, "schön", "Adj.", "đẹp", "Ich finde den Garten schön. (Tôi thấy khu vườn đẹp.)"),
        (lesson_id, "hässlich", "Adj.", "xấu xí", "Der alte Schrank ist hässlich. (Chiếc tủ cũ thì xấu xí.)"),
        (lesson_id, "modern", "Adj.", "hiện đại", "Das Wohnzimmer ist modern. (Phòng khách thì hiện đại.)"),
        (lesson_id, "altmodisch", "Adj.", "lỗi thời, kiểu cũ", "Ich finde das Sofa ein bisschen altmodisch. (Tôi thấy chiếc ghế sofa hơi lỗi thời một chút.)"),
        (lesson_id, "gemütlich", "Adj.", "ấm cúng, thoải mái", "Mein Schlafzimmer ist gemütlich. (Phòng ngủ của tôi thì ấm cúng.)"),
        (lesson_id, "ungemütlich", "Adj.", "không ấm cúng, bất tiện", "Der Flur ist dunkel und ungemütlich. (Hành lang tối và không ấm cúng.)")
    ]

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # KHO 50 BÀI TẬP BÀI 4 (12 Trắc nghiệm + 12 Điền khuyết + 8 Dịch + 5 Nghe + 4 Nói + 4 Đọc + 5 Viết)
    # =========================================================================
    passage_b4_julia = (
        "Bức thư của Julia gửi các bạn (Brief von Julia):\n"
        "Liebe Freunde,\n"
        "unser Haus ist sehr alt und hat 5 Zimmer.\n"
        "Oben gibt es einen Balkon.\n"
        "Aber ich finde die Küche zu klein.\n"
        "Das Haus hat einen Flur. Er ist lang und dunkel.\n"
        "Viele Grüße,\n"
        "Julia"
    )


    EXERCISE_TRANSLATIONS = {
    "1": "Chúng tôi có một ngôi nhà. (Wir haben ein Haus.)",
    "2": "Ở phía trên có một ban công. (Oben gibt es einen Balkon.)",
    "3": "Tôi thấy khu vườn rất đẹp. (Ich finde den Garten sehr schön.)",
    "4": "Phòng khách thì rộng, nhưng tôi thấy nhà bếp quá nhỏ. (Das Wohnzimmer ist groß, aber ich finde die Küche zu klein.)",
    "5": "Ngôi nhà có một hành lang. Nó dài và tối. (Das Haus hat einen Flur. Er ist lang und dunkel.)",
    "6": "Kia có phải là túi xách của bạn không, Anna? (Ist das deine Tasche, Anna?)",
    "7": "Kia có phải là ô tô của Ngài không, ông Müller? (Ist das Ihr Auto, Herr Müller?)",
    "8": "Kia có phải là con của các bạn không, Maria và Lukas? (Sind das eure Kinder, Maria und Lukas?)",
    "9": "Kia có phải là sách của bạn không, Tina? – Không, đó là sách của cô ấy. (Ist das dein Buch, Tina? – Nein, das ist ihr Buch.)",
    "10": "Tất cả các phòng có đuôi '-zimmer' (Wohnzimmer, Schlafzimmer...) đều mang giống trung (das).",
    "11": "Từ trái nghĩa của 'hell' (sáng sủa) là 'dunkel' (tối tăm).",
    "12": "Chúng tôi có một khu vườn. (Wir haben einen Garten.)",
    "13": "Ở phía trên có một ban công. (Oben gibt es einen Balkon.)",
    "14": "Ngôi nhà có một hành lang. (Das Haus hat einen Flur.)",
    "15": "Chúng tôi cũng có một khu vườn. Tôi thấy khu vườn rất đẹp. (Wir haben auch einen Garten. Ich finde den Garten sehr schön.)",
    "16": "Phòng khách thì rộng, nhưng tôi thấy nhà bếp quá nhỏ. (Das Wohnzimmer ist groß, aber ich finde die Küche zu klein.)",
    "17": "Đó có phải là một tầng hầm không? – Không, căn hộ không có tầng hầm. (Ist das ein Keller? – Nein, die Wohnung hat keinen Keller.)",
    "18": "Đây là căn hộ của chúng tôi. (Das ist unsere Wohnung.)",
    "19": "Chúng tôi đến thăm khu vườn của các bạn. (Wir besuchen euren Garten.)",
    "20": "Đó là ngôi nhà của anh ấy. (Das ist sein Haus.)",
    "21": "Cô ấy đang tìm chìa khóa của mình. (Sie sucht ihren Schlüssel.)",
    "22": "Hôm qua chúng tôi không có thời gian. (Gestern hatten wir keine Zeit.)",
    "23": "Đó là phòng của tôi. (Das ist mein Zimmer.)",
    "24": "Căn phòng làm việc không tối tăm, mà nó sáng sủa.",
    "25": "Tôi có một ngôi nhà. Ngôi nhà của tôi có 5 phòng. (Ich habe ein Haus. Mein Haus hat 5 Zimmer.)",
    "26": "Phòng khách của tôi thì sáng và hiện đại. (Mein Wohnzimmer ist hell und modern.)",
    "27": "Nó có 1 Tivi và 1 giá sách. (Es hat einen Fernseher und ein Bücherregal.)",
    "28": "Phòng ngủ của tôi thì ấm cúng và có 1 giường. (Mein Schlafzimmer ist gemütlich und hat ein Bett.)",
    "29": "Phòng làm việc của tôi thì nhỏ nhưng sáng. Nó có 1 bàn và 1 ghế. (Mein Arbeitszimmer ist klein, aber hell. Es hat einen Tisch und einen Stuhl.)",
    "30": "Phòng bếp của tôi thì nhỏ và đẹp. (Meine Küche ist klein und schön.)",
    "31": "Chúng mình cũng có một khu vườn. Mình thấy khu vườn rất đẹp. (Wir haben auch einen Garten. Ich finde den Garten sehr schön.)",
    "32": "Phòng khách của tôi thì sáng và hiện đại. (Mein Wohnzimmer ist hell und modern.)",
    "33": "Ở phía trên có một ban công. (Oben gibt es einen Balkon.)",
    "34": "Tôi thấy khu vườn rất đẹp. (Ich finde den Garten rất đẹp / sehr schön.)",
    "35": "Ngôi nhà có một hành lang. (Das Haus hat einen Flur.)",
    "36": "Kia có phải các con của các bạn không, Maria và Lukas? (Sind das eure Kinder, Maria und Lukas?)",
    "37": "Phòng khách của tôi sáng sủa và hiện đại. (Mein Wohnzimmer ist hell und modern.)",
    "38": "Phòng khách của tôi sáng và hiện đại. Nó có một chiếc TV và một giá sách. (Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher und ein Bücherregal.)",
    "39": "Đó có phải con của các bạn không, Maria và Lukas? (Sind das eure Kinder, Maria und Lukas?)",
    "40": "Ngôi nhà có một hành lang. Nó dài và tối. (Das Haus hat einen Flur. Er ist lang und dunkel.)",
    "41": "Chúng tôi cũng có một khu vườn. Tôi thấy khu vườn rất đẹp. (Wir haben auch einen Garten. Ich finde den Garten sehr schön.)",
    "42": "Bức thư của Julia gửi các bạn:\nCác bạn thân mến,\nNgôi nhà của chúng mình rất cổ kính và có 5 phòng.\nỞ phía trên có một ban công.\nNhưng mình thấy nhà bếp quá nhỏ.\nNgôi nhà có một hành lang. Nó dài và tối.\nThân ái,\nJulia",
    "43": "Bức thư của Julia gửi các bạn:\nCác bạn thân mến,\nNgôi nhà của chúng mình rất cổ kính và có 5 phòng.\nỞ phía trên có một ban công.\nNhưng mình thấy nhà bếp quá nhỏ.\nNgôi nhà có một hành lang. Nó dài và tối.\nThân ái,\nJulia",
    "44": "Bức thư của Julia gửi các bạn:\nCác bạn thân mến,\nNgôi nhà của chúng mình rất cổ kính và có 5 phòng.\nỞ phía trên có một ban công.\nNhưng mình thấy nhà bếp quá nhỏ.\nNgôi nhà có một hành lang. Nó dài và tối.\nThân ái,\nJulia",
    "45": "Bức thư của Julia gửi các bạn:\nCác bạn thân mến,\nNgôi nhà của chúng mình rất cổ kính và có 5 phòng.\nỞ phía trên có một ban công.\nNhưng mình thấy nhà bếp quá nhỏ.\nNgôi nhà có một hành lang. Nó dài và tối.\nThân ái,\nJulia",
    "46": "Chúng tôi có một khu vườn. (Wir haben einen Garten.)",
    "47": "Đó là cuốn sách của cô ấy. (Das ist ihr Buch.)",
    "48": "Đó là chiếc tủ của anh ấy. (Das ist sein Schrank.)",
    "49": "Chúng tôi không có tivi. (Wir haben keinen Fernseher.)",
    "50": "Ngôi nhà có một hành lang. Nó dài và tối. (Das Haus hat einen Flur. Er ist lang und dunkel.)"
}

    exercises = [
        # --- DẠNG 1: TRẮC NGHIỆM NGỮ PHÁP & TỪ VỰNG (12 CÂU) ---
        (
            lesson_id, "trac_nghiem",
            "Câu 1: Chọn mạo từ thích hợp cho câu sau: 'Wir haben ___ Haus.'",
            json.dumps(["ein", "einen", "eine", "den"]),
            "ein",
            "'das Haus' là danh từ giống trung (das), đứng sau 'haben' ở Akkusativ vẫn giữ nguyên là 'ein'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 2: Chọn mạo từ đúng: 'Oben gibt es ___ Balkon.'",
            json.dumps(["einen", "ein", "eine", "der"]),
            "einen",
            "Cấu trúc 'es gibt' luôn đòi hỏi tân ngữ Akkusativ. 'der Balkon' (giống đực) đổi 'ein' thành 'einen Balkon'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 3: Chọn mạo từ thích hợp: 'Ich finde ___ Garten sehr schön.'",
            json.dumps(["den", "der", "die", "das"]),
            "den",
            "Động từ 'finden' đòi hỏi Akkusativ. Khu vườn đã được xác định và mang giống đực (der) nên đổi thành 'den Garten'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 4: Chọn mạo từ đúng: 'Das Wohnzimmer ist groß, aber ich finde ___ Küche zu klein.'",
            json.dumps(["die", "den", "der", "das"]),
            "die",
            "'die Küche' mang giống cái (die), khi đứng sau động từ 'finden' (Akkusativ) vẫn giữ nguyên là 'die Küche'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 5: Chọn đại từ nhân xưng thay thế thích hợp: 'Das Haus hat einen Flur. ___ ist lang und dunkel.'",
            json.dumps(["Er", "Es", "Sie", "Ihn"]),
            "Er",
            "'der Flur' mang giống đực (der). Khi làm chủ ngữ ở câu sau (Nominativ), danh từ giống đực được thay bằng đại từ 'Er'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 6: Điền mạo từ sở hữu đúng: 'Ist das ___ Tasche, Anna?' (Anna là bạn bè thân mật)",
            json.dumps(["deine", "dein", "deinen", "ihre"]),
            "deine",
            "'die Tasche' mang giống cái (die). Chủ sở hữu là bạn (du) → gốc 'dein' + đuôi '-e' thành 'deine Tasche'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 7: Điền mạo từ sở hữu lịch sự: 'Ist das ___ Auto, Herr Müller?'",
            json.dumps(["Ihr", "Ihre", "Ihren", "dein"]),
            "Ihr",
            "Xưng hô trang trọng với Herr Müller dùng ngôi 'Sie' → gốc sở hữu 'Ihr' (viết hoa). 'das Auto' giống trung nên không thêm đuôi: 'Ihr Auto'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 8: Điền mạo từ sở hữu: 'Sind das ___ Kinder, Maria und Lukas?' (nói chuyện với 2 bạn)",
            json.dumps(["eure", "euer", "euren", "unsere"]),
            "eure",
            "Nói với Maria und Lukas là ngôi 'ihr' (các bạn) → gốc 'euer'. 'die Kinder' là số nhiều → thêm '-e' và lược bỏ 'e' ở giữa: 'eure Kinder'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 9: Điền mạo từ sở hữu: 'Ist das dein Buch, Tina? – Nein, das ist das Buch von Lena. Es ist ___ Buch.'",
            json.dumps(["ihr", "sein", "ihre", "seine"]),
            "ihr",
            "Quyển sách của Lena (nữ = sie/cô ấy) → gốc sở hữu là 'ihr'. 'das Buch' mang giống trung nên không thêm đuôi → 'ihr Buch'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 10: Tất cả các phòng có đuôi '-zimmer' (Wohnzimmer, Schlafzimmer, Badezimmer...) mang giống gì?",
            json.dumps(["das (Giống trung)", "der (Giống đực)", "die (Giống cái)", "die (Số nhiều)"]),
            "das (Giống trung)",
            "Theo quy tắc từ ghép (Komposita), từ đứng cuối là 'das Zimmer' (giống trung) nên tất cả các phòng '-zimmer' đều mang giống 'das'.",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 11: Từ trái nghĩa (Gegenteil) của tính từ 'hell' (sáng sủa) là gì?",
            json.dumps(["dunkel", "laut", "klein", "teuer"]),
            "dunkel",
            "'hell' (sáng sủa) trái nghĩa với 'dunkel' (tối tăm).",
            15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 12 [Dynamic Phân biệt Nominativ / Akkusativ]: Chọn mạo từ đúng nhất cho câu sau:",
            json.dumps(["einen", "ein", "eine", "den"]),
            "einen",
            "Kiểm tra động từ (sein vs. haben/es gibt/finden) và giống của danh từ để chia mạo từ chính xác.",
            15,
            json.dumps({"dynamic_nom_akk_quiz": True})
        ),

        # --- DẠNG 2: ĐIỀN KHUYẾT NGỮ PHÁP CHUYÊN SÂU (12 CÂU) ---
        (
            lesson_id, "dien_khuyet",
            "Câu 13: Hoàn thành câu trong thư Julia: 'Oben gibt es ___ Balkon.' (Điền mạo từ bất định)",
            None,
            "einen",
            "der Balkon (giống đực) sau 'gibt es' (Akkusativ) đổi 'ein' thành 'einen'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 14: Hoàn thành câu trong thư Julia: 'Das Haus hat ___ Flur.' (Điền mạo từ bất định)",
            None,
            "einen",
            "der Flur (giống đực) sau 'hat' (Akkusativ) đổi 'ein' thành 'einen'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 15: Hoàn thành câu trong thư Julia: 'Wir haben auch einen Garten. Ich finde ___ Garten sehr schön.' (Điền mạo từ xác định)",
            None,
            "den",
            "der Garten đã được nhắc ở câu trước (đã xác định) và đứng sau 'finde' (Akkusativ) nên đổi thành 'den Garten'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 16: Điền từ thích hợp vào câu: 'Das Wohnzimmer ist groß, aber ich finde die Küche ___ klein.' (Phó từ mang ý 'quá mức')",
            None,
            "zu",
            "Phó từ 'zu' đi kèm tính từ mang nghĩa phàn nàn 'quá...': zu klein (quá nhỏ).",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 17: Hoàn thành câu hỏi phủ định: 'Ist das ein Keller?' → 'Nein, die Wohnung hat ___ Keller.' (Điền từ phủ định)",
            None,
            "keinen",
            "der Keller (giống đực) đứng sau 'hat' ở Akkusativ nên từ phủ định đổi 'kein' thành 'keinen'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 18: Điền mạo từ sở hữu của 'wir' trước danh từ giống cái: 'Das ist ___ Wohnung.' (Căn hộ của chúng tôi)",
            None,
            "unsere",
            "Người sở hữu 'wir' → gốc 'unser'. 'die Wohnung' mang giống cái nên thêm '-e' thành 'unsere Wohnung'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 19: Điền mạo từ sở hữu của ngôi 'ihr' (các bạn) trước danh từ giống đực ở Akkusativ: 'Wir besuchen ___ Garten.' (khu vườn của các bạn)",
            None,
            "euren",
            "Gốc 'euer' khi thêm đuôi '-en' ở Akkusativ sẽ lược bỏ 'e' ở giữa: 'euer + en' → 'euren'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 20: Điền mạo từ sở hữu của 'er' trước danh từ giống trung: 'Das ist ___ Haus.' (Ngôi nhà của anh ấy)",
            None,
            "sein",
            "Người sở hữu là 'er' (anh ấy) → gốc 'sein'. 'das Haus' mang giống trung nên giữ nguyên: 'sein Haus'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 21: Điền mạo từ sở hữu của 'sie' (cô ấy) trước danh từ giống đực ở Akkusativ: 'Sie sucht ___ Schlüssel.' (Chìa khóa của cô ấy - der Schlüssel)",
            None,
            "ihren",
            "Cô ấy ('sie') → gốc 'ihr'. 'der Schlüssel' (giống đực) sau 'sucht' (Akkusativ) thêm đuôi '-en' → 'ihren Schlüssel'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 22: Điền dạng quá khứ của động từ 'haben' ở ngôi 'wir': 'Gestern ___ wir keine Zeit.' (Hôm qua chúng tôi không có thời gian)",
            None,
            "hatten",
            "Thì quá khứ Präteritum của 'haben' ở ngôi 'wir' là 'hatten'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 23 [Dynamic Sở Hữu 9 Ngôi]: Hãy chia mạo từ sở hữu thích hợp cho câu sau:",
            None,
            "meine",
            "Xác định người sở hữu (ich, du, er, sie, wir, ihr, Sie) và giống/cách của danh từ để chia đuôi chính xác.",
            15,
            json.dumps({"dynamic_possessiv_quiz": True})
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 24 [Dynamic Tính Từ Đối Lập]: Điền tính từ trái nghĩa thích hợp vào chỗ trống:",
            None,
            "dunkel",
            "Ghi nhớ các cặp tính từ đối lập miêu tả nhà cửa: hell/dunkel, groß/klein, ruhig/laut, neu/alt, billig/teuer, schön/hässlich.",
            15,
            json.dumps({"dynamic_adjective_antonym_quiz": True})
        ),

        # --- DẠNG 3: DỊCH 2 CHIỀU VIỆT ⇄ ĐỨC (8 CÂU) ---
        (
            lesson_id, "dich",
            "Câu 25: Dịch câu sau sang tiếng Đức: 'Tôi có một ngôi nhà. Ngôi nhà của tôi có 5 phòng.'",
            None,
            "Ich habe ein Haus. Mein Haus hat 5 Zimmer. / Ich habe ein Haus. Mein Haus hat fünf Zimmer. / Ich besitze ein Haus. Mein Haus hat 5 Zimmer.",
            "das Haus đứng sau habe (Akkusativ) → ein Haus; làm chủ ngữ (Nominativ) → Mein Haus. Số nhiều của Zimmer giữ nguyên.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 26: Dịch câu sau sang tiếng Đức: 'Phòng khách của tôi thì sáng và hiện đại.'",
            None,
            "Mein Wohnzimmer ist hell und modern. / Mein Wohnzimmer ist modern und hell.",
            "das Wohnzimmer (giống trung) → Mein Wohnzimmer. Tính từ sau 'ist' giữ nguyên không chia đuôi.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 27: Dịch câu sau sang tiếng Đức: 'Nó có 1 Tivi và 1 giá sách.' (Nó = thay thế cho das Wohnzimmer)",
            None,
            "Es hat einen Fernseher und ein Bücherregal. / Es hat ein Bücherregal und einen Fernseher. / Es hat einen Fernseher und ein Regal.",
            "Đại từ 'Es' thay cho das Wohnzimmer; der Fernseher (giống đực) sau hat đổi thành 'einen Fernseher'; das Bücherregal giữ nguyên 'ein'.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 28: Dịch câu sau sang tiếng Đức: 'Phòng ngủ của tôi thì ấm cúng và có 1 giường.'",
            None,
            "Mein Schlafzimmer ist gemütlich und hat ein Bett. / Mein Schlafzimmer ist gemütlich und hat 1 Bett.",
            "das Schlafzimmer → Mein Schlafzimmer; das Bett (giống trung) sau hat → ein Bett.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 29: Dịch câu sau sang tiếng Đức: 'Phòng làm việc của tôi thì nhỏ nhưng sáng. Nó có 1 bàn và 1 ghế.'",
            None,
            "Mein Arbeitszimmer ist klein, aber hell. Es hat einen Tisch und einen Stuhl. / Mein Arbeitszimmer ist klein, aber hell. Es hat einen Stuhl und einen Tisch. / Mein Arbeitszimmer ist klein aber hell. Es hat einen Tisch und einen Stuhl.",
            "Liên từ aber nối 2 tính từ tương phản; der Tisch và der Stuhl đều là giống đực nên đổi thành 'einen Tisch und einen Stuhl'.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 30: Dịch câu sau sang tiếng Đức: 'Phòng bếp của tôi thì nhỏ và đẹp.'",
            None,
            "Meine Küche ist klein und schön. / Meine Küche ist schön und klein.",
            "die Küche (giống cái) nên mạo từ sở hữu phải có đuôi -e: Meine Küche.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 31: Dịch câu sau sang tiếng Việt: 'Wir haben auch einen Garten. Ich finde den Garten sehr schön.'",
            None,
            "Chúng mình cũng có một khu vườn. Mình thấy khu vườn rất đẹp. / Chúng tôi cũng có một khu vườn. Tôi thấy khu vườn rất đẹp. / Chúng ta cũng có một khu vườn. Tôi thấy khu vườn rất đẹp. / Chúng mình cũng có một cái vườn. Mình thấy vườn rất đẹp.",
            "Bản dịch câu kết trong thư của Julia gửi Claudia.",
            20, None
        ),
        (
            lesson_id, "dich",
            "Câu 32 [Dynamic Dịch Câu Miêu Tả Nhà & Nội Thất]: Hãy dịch câu sau sang tiếng Đức chuẩn xác:",
            None,
            "Mein Wohnzimmer ist hell und modern. / Mein Wohnzimmer ist modern und hell.",
            "Vận dụng chính xác mạo từ sở hữu (Mein/Meine), đại từ thay thế (Er/Sie/Es) và Akkusativ giống đực (einen Tisch, einen Stuhl, einen Fernseher).",
            20,
            json.dumps({"dynamic_house_translation_quiz": True})
        ),

        # --- DẠNG 4: LUYỆN NGHE 1.0X & 0.65X (5 CÂU) ---
        (
            lesson_id, "nghe",
            "Câu 33 [Luyện Nghe]: Nghe và điền mạo từ còn thiếu trong câu: 'Oben gibt es ___ Balkon.'",
            None,
            "einen",
            "Âm thanh phát câu: 'Oben gibt es einen Balkon.' (Ở phía trên có một ban công.) → Điền mạo từ Akkusativ 'einen'.",
            20,
            json.dumps({"audio_text": "Oben gibt es einen Balkon.", "translation": "Ở phía trên có một ban công."}, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe",
            "Câu 34 [Luyện Nghe]: Nghe và điền từ còn thiếu: 'Ich finde den Garten sehr ___.'",
            None,
            "schön",
            "Âm thanh phát câu: 'Ich finde den Garten sehr schön.' (Tôi thấy khu vườn rất đẹp.) → Tính từ còn thiếu là 'schön'.",
            20,
            json.dumps({"audio_text": "Ich finde den Garten sehr schön.", "translation": "Tôi thấy khu vườn rất đẹp."}, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe",
            "Câu 35 [Luyện Nghe]: Nghe và điền danh từ: 'Das Haus hat einen ___.'",
            None,
            "Flur",
            "Âm thanh phát câu: 'Das Haus hat einen Flur.' (Ngôi nhà có một hành lang.) → Danh từ còn thiếu là 'Flur'.",
            20,
            json.dumps({"audio_text": "Das Haus hat einen Flur.", "translation": "Ngôi nhà có một hành lang."}, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe",
            "Câu 36 [Luyện Nghe]: Nghe và điền mạo từ sở hữu: 'Sind das ___ Kinder, Maria und Lukas?'",
            None,
            "eure",
            "Âm thanh phát câu: 'Sind das eure Kinder, Maria und Lukas?' (Kia có phải các con của các bạn không, Maria và Lukas?) → Mạo từ sở hữu số nhiều là 'eure'.",
            20,
            json.dumps({"audio_text": "Sind das eure Kinder, Maria und Lukas?", "translation": "Kia có phải các con của các bạn không, Maria và Lukas?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe",
            "Câu 37 [Luyện Nghe]: Nghe và viết lại câu miêu tả: 'Mein Wohnzimmer ist hell und modern.'",
            None,
            "Mein Wohnzimmer ist hell und modern. / Mein Wohnzimmer ist modern und hell.",
            "Âm thanh phát câu: 'Mein Wohnzimmer ist hell und modern.' (Phòng khách của tôi sáng sủa và hiện đại.)",
            20,
            json.dumps({"audio_text": "Mein Wohnzimmer ist hell und modern.", "translation": "Phòng khách của tôi sáng sủa và hiện đại."}, ensure_ascii=False)
        ),

        # --- DẠNG 5: SẮP XẾP TỪ THÀNH CÂU (sap_xep) - ĐÚNG 4 CÂU (Câu 38 -> 41) ---
        (
            lesson_id, "sap_xep",
            "Câu 38 [Sắp xếp từ thành câu]: Sắp xếp các từ sau thành 2 câu miêu tả phòng khách và đồ đạc: [hell und modern / ist / Mein Wohnzimmer / . / einen Fernseher / Es / hat / und / ein Bücherregal / .]",
            None,
            "Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher und ein Bücherregal.",
            "Câu 1: Mein Wohnzimmer ist hell und modern. Câu 2: Động từ haben đi với Akkusativ: einen Fernseher (der Fernseher) và ein Bücherregal (das Bücherregal).",
            20,
            json.dumps({"audio_text": "Mein Wohnzimmer ist hell und modern. Es hat einen Fernseher und ein Bücherregal.", "translation": "Phòng khách của tôi sáng và hiện đại. Nó có một chiếc TV và một giá sách."}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 39 [Sắp xếp từ thành câu]: Sắp xếp câu hỏi xác nhận mạo từ sở hữu số nhiều: [eure / Sind / Kinder / das / , / Maria und Lukas / ?]",
            None,
            "Sind das eure Kinder, Maria und Lukas?",
            "Động từ Sind đảo lên đầu câu hỏi Ja/Nein. Đại từ sở hữu ngôi ihr ở dạng số nhiều (die Kinder) là eure.",
            20,
            json.dumps({"audio_text": "Sind das eure Kinder, Maria und Lukas?", "translation": "Đó có phải con của các bạn không, Maria và Lukas?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 40 [Sắp xếp từ thành câu]: Sắp xếp câu miêu tả hành lang sử dụng đại từ thay thế Er: [einen Flur / hat / Das Haus / . / ist / Er / lang und dunkel / .]",
            None,
            "Das Haus hat einen Flur. Er ist lang und dunkel.",
            "Câu 1: Động từ hat đòi hỏi Akkusativ -> einen Flur (der Flur). Câu 2: Đại từ Er thay thế cho danh từ giống đực der Flur.",
            20,
            json.dumps({"audio_text": "Das Haus hat einen Flur. Er ist lang und dunkel.", "translation": "Ngôi nhà có một hành lang. Nó dài và tối."}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 41 [Sắp xếp từ thành câu]: Sắp xếp câu miêu tả có khu vườn và cảm nghĩ: [einen Garten / Wir / auch / haben / . / den Garten / sehr schön / finde / Ich / .]",
            None,
            "Wir haben auch einen Garten. Ich finde den Garten sehr schön.",
            "Câu 1: haben đòi hỏi Akkusativ -> einen Garten. Câu 2: finden đòi hỏi Akkusativ -> den Garten sehr schön.",
            20,
            json.dumps({"audio_text": "Wir haben auch einen Garten. Ich finde den Garten sehr schön.", "translation": "Chúng tôi cũng có một khu vườn. Tôi thấy khu vườn rất đẹp."}, ensure_ascii=False)
        ),
        # --- DẠNG 6: ĐỌC HIỂU BỨC THƯ CỦA JULIA (4 CÂU) ---
        (
            lesson_id, "doc",
            "Câu 42 [Đọc hiểu Thư Julia]: Dựa vào bức thư của Julia, ngôi nhà của Julia có bao nhiêu phòng (Zimmer)? (Điền con số)",
            None,
            "5 / fünf / 5 Zimmer / fünf Zimmer",
            "Trong thư Julia viết: 'Unser Haus ist sehr alt und hat 5 Zimmer.' → Đáp án là 5 phòng.",
            20, json.dumps({"passage": passage_b4_julia}, ensure_ascii=False)
        ),
        (
            lesson_id, "doc",
            "Câu 43 [Đọc hiểu Thư Julia]: Ở phía trên (Oben) của ngôi nhà có cái gì? (Điền tiếng Đức kèm mạo từ: 'einen ...')",
            None,
            "einen Balkon / Balkon / ein Balkon / der Balkon",
            "Trong thư viết: 'Oben gibt es einen Balkon.'",
            20, json.dumps({"passage": passage_b4_julia}, ensure_ascii=False)
        ),
        (
            lesson_id, "doc",
            "Câu 44 [Đọc hiểu Thư Julia]: Julia cảm thấy nhà bếp (die Küche) như thế nào? (Điền cụm 2 từ tiếng Đức)",
            None,
            "zu klein / quá nhỏ / sie ist zu klein / nhỏ quá",
            "Julia viết: '...aber ich finde die Küche zu klein.'",
            20, json.dumps({"passage": passage_b4_julia}, ensure_ascii=False)
        ),
        (
            lesson_id, "doc",
            "Câu 45 [Đọc hiểu Thư Julia]: Hành lang (der Flur) của ngôi nhà được miêu tả bằng 2 tính từ nào? (Điền dạng '... und ...')",
            None,
            "lang und dunkel / dunkel und lang / dài và tối / tối và dài",
            "Julia viết: 'Das Haus hat einen Flur. Er ist lang und dunkel.'",
            20, json.dumps({"passage": passage_b4_julia}, ensure_ascii=False)
        ),

        # --- DẠNG 7: VIẾT LẠI CÂU & BIẾN ĐỔI NGỮ PHÁP (5 CÂU) ---
        (
            lesson_id, "viet",
            "Câu 46: Viết lại câu sau sang câu có động từ 'haben' ở Akkusativ: 'Das ist ein Garten.' → 'Wir haben ___.'",
            None,
            "einen Garten / den Garten / Garten",
            "Chuyển từ Nominativ 'ein Garten' sang Akkusativ sau 'haben': 'Wir haben einen Garten.'",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 47: Viết lại câu sau dùng mạo từ sở hữu thay thế cụm 'von Lena': 'Das ist das Buch von Lena.' → 'Das ist ___ Buch.'",
            None,
            "ihr",
            "Lena là nữ (sie/cô ấy) → dùng gốc 'ihr'. das Buch là giống trung nên không thêm đuôi: 'ihr Buch'.",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 48: Viết lại câu sau dùng mạo từ sở hữu thay thế cụm 'von Peter': 'Das ist der Schrank von Peter.' → 'Das ist ___ Schrank.'",
            None,
            "sein",
            "Peter là nam (er/anh ấy) → dùng gốc 'sein'. der Schrank ở Nominativ nên giữ nguyên: 'sein Schrank'.",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 49: Viết lại câu sau sang dạng phủ định với 'kein-': 'Wir haben einen Fernseher.' → 'Wir haben ___ Fernseher.'",
            None,
            "keinen",
            "der Fernseher đứng sau 'haben' ở Akkusativ nên từ phủ định là 'keinen Fernseher'.",
            25, None
        ),
        (
            lesson_id, "viet",
            "Câu 50 [Dynamic Thay Thế Đại Từ Nhân Xưng (Er/Sie/Es)]: Điền đại từ nhân xưng thích hợp:",
            None,
            "Er",
            "Đại từ nhân xưng thay thế danh từ làm chủ ngữ: der → Er, die → Sie, das → Es.",
            25,
            json.dumps({"dynamic_pronoun_replacement_quiz": True})
        )
    ]

    import random
    shuffled_exercises = []
    for idx, ex in enumerate(exercises):
        ex_list = list(ex)
        q_num = idx + 1
        extra_d = {}
        if ex_list[7]:
            try:
                extra_d = json.loads(ex_list[7]) if isinstance(ex_list[7], str) else dict(ex_list[7])
            except Exception:
                extra_d = {}
        trans_val = EXERCISE_TRANSLATIONS.get(str(q_num)) or EXERCISE_TRANSLATIONS.get(q_num)
        if trans_val and not extra_d.get("translation"):
            extra_d["translation"] = trans_val
            # trans applied
        ex_list[7] = json.dumps(extra_d, ensure_ascii=False) if extra_d else None
        if ex_list[1] == "trac_nghiem" and ex_list[3]:
            try:
                opts = json.loads(ex_list[3])
                if isinstance(opts, list) and len(opts) > 1:
                    random.shuffle(opts)
                    ex_list[3] = json.dumps(opts, ensure_ascii=False)
            except Exception:
                pass
        shuffled_exercises.append(tuple(ex_list))
    exercises = shuffled_exercises

    cursor.executemany("""
        INSERT INTO exercises (lesson_id, exercise_type, question, options_json, correct_answer, explanation, exp_reward, extra_data)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    """, exercises)

    conn.commit()
    conn.close()
    print("✅ Đã khởi tạo thành công Bài 4: 'Menschen und Häuser' với đầy đủ 7 Học phần Lý thuyết (Không link YouTube) + 48 Từ vựng + ĐÚNG 50 Bài tập (12+12+8+5+4+4+5) có 5 Bộ Random Đổi đề!")

if __name__ == "__main__":
    seed_lesson_4()
