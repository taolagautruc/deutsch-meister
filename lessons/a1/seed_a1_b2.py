import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_2():
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

    # Xóa dữ liệu cũ của Bài 2 nếu đã có để cập nhật sạch sẽ
    cursor.execute("DELETE FROM lessons WHERE level_id = ? AND title LIKE 'Bài 2%';", (a1_id,))

    lesson_title = 'Bài 2: "Sprache im Kurs - Động Từ và Giống (der, die, das & Mạo Từ)"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (6 HỌC PHẦN CHUẨN ĐẶC TẢ - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 2 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Bài Học Giống Danh Từ & Giao Tiếp Lớp Học (Bài 2)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 60 phút • ⚡ 650+ EXP
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Sprache im Kurs • Động Từ Lớp Học, Giống Danh Từ (der / die / das) & Mạo Từ
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Làm chủ khái niệm giống của danh từ tiếng Đức; nắm vững bảng quy tắc vàng nhận biết giống đực (<i>der</i>), giống cái (<i>die</i>), giống trung (<i>das</i>) theo hậu tố và nhóm nghĩa; ghi nhớ 18 danh từ đồ dùng lớp học cùng quy tắc tạo số nhiều; sử dụng thành thạo 3 cột mạo từ (Xác định <i>der/die/das</i>, Bất định <i>ein/eine</i>, Phủ định <i>kein/keine</i>); tự tin dùng 6 mẫu câu giao tiếp lớp học (<i>Wie heißt das auf Deutsch?, Können Sie das bitte wiederholen/buchstabieren/anschreiben?</i>).
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: KHÁI NIỆM MẠO TỪ, GIỐNG CỦA DANH TỪ & 4 CÁCH -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm">1</span>
                <h4 class="text-lg font-black text-slate-900">Khái niệm Mạo từ (Artikel), Giống của Danh từ & 4 Cách trong tiếng Đức</h4>
            </div>

            <div class="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-100 text-xs sm:text-sm text-indigo-950 space-y-2">
                <p class="font-bold text-indigo-900">📌 2 Nguyên tắc bất di bất dịch của Danh từ tiếng Đức (Nomen / Substantive):</p>
                <ol class="list-decimal list-inside space-y-1 text-slate-700 ml-1">
                    <li><b>Luôn luôn viết hoa chữ cái đầu tiên</b> dù đứng ở bất kỳ vị trí nào trong câu (ví dụ: <i>der Tisch, die Brille, das Buch</i>).</li>
                    <li>Mỗi danh từ đều mang một <b>giống ngữ pháp (Genus)</b> cố định, được thể hiện thông qua <b>Mạo từ (Artikel)</b> đứng trước nó.</li>
                </ol>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 pt-1">
                <div class="p-4 rounded-2xl bg-blue-50/80 border border-blue-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-lg bg-blue-600 text-white font-black text-xs">der (m)</span>
                    <h5 class="font-bold text-blue-950 text-sm">Maskulinum • Giống Đực</h5>
                    <p class="text-xs text-slate-600">Mạo từ xác định số ít: <b>der</b></p>
                    <p class="text-xs text-blue-800 font-semibold">Ví dụ: <i>der Tisch</i> (cái bàn), <i>der Kuli</i> (bút bi)</p>
                </div>
                <div class="p-4 rounded-2xl bg-rose-50/80 border border-rose-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-black text-xs">die (f)</span>
                    <h5 class="font-bold text-rose-950 text-sm">Femininum • Giống Cái</h5>
                    <p class="text-xs text-slate-600">Mạo từ xác định số ít: <b>die</b></p>
                    <p class="text-xs text-rose-800 font-semibold">Ví dụ: <i>die Brille</i> (kính mắt), <i>die Tasche</i> (túi)</p>
                </div>
                <div class="p-4 rounded-2xl bg-emerald-50/80 border border-emerald-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-black text-xs">das (n)</span>
                    <h5 class="font-bold text-emerald-950 text-sm">Neutrum • Giống Trung</h5>
                    <p class="text-xs text-slate-600">Mạo từ xác định số ít: <b>das</b></p>
                    <p class="text-xs text-emerald-800 font-semibold">Ví dụ: <i>das Buch</i> (quyển sách), <i>das Handy</i> (điện thoại)</p>
                </div>
                <div class="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 space-y-2">
                    <span class="px-2.5 py-1 rounded-lg bg-amber-600 text-white font-black text-xs">die (Pl.)</span>
                    <h5 class="font-bold text-amber-950 text-sm">Plural • Số Nhiều Chung</h5>
                    <p class="text-xs text-slate-600">Tất cả danh từ khi sang số nhiều (Cách 1) đều dùng chung mạo từ <b>die</b>.</p>
                    <p class="text-xs text-amber-800 font-semibold">Ví dụ: <i>die Tische, die Brillen, die Bücher</i></p>
                </div>
            </div>

            <!-- TỔNG QUAN 4 CÁCH -->
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-3">
                <h5 class="font-bold text-slate-800 text-sm flex items-center gap-2">
                    <span>🧭</span> Tổng quan 4 Cách (Kasus) trong tiếng Đức
                </h5>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                    <div class="p-3 rounded-xl bg-white border border-slate-200">
                        <span class="font-extrabold text-indigo-600">1. Nominativ (Cách 1 - Trọng tâm bài học):</span>
                        <p class="text-slate-600 mt-1">Chủ ngữ của câu hoặc danh từ đứng sau động từ <i>sein (Das ist...)</i>, <i>heißen</i>.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200">
                        <span class="font-extrabold text-indigo-600">2. Genitiv (Cách 2 - Sở hữu cách):</span>
                        <p class="text-slate-600 mt-1">Chỉ sự sở hữu (ở trình độ A1 thường dùng cấu trúc <b>von + Tên riêng</b>, ví dụ: <i>der Kuli von Anna</i>).</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200">
                        <span class="font-extrabold text-indigo-600">3. Dativ (Cách 3 - Tân ngữ gián tiếp):</span>
                        <p class="text-slate-600 mt-1">Chỉ đối tượng tiếp nhận hành động hoặc trạng thái vị trí tĩnh.</p>
                    </div>
                    <div class="p-3 rounded-xl bg-white border border-slate-200">
                        <span class="font-extrabold text-indigo-600">4. Akkusativ (Cách 4 - Tân ngữ trực tiếp):</span>
                        <p class="text-slate-600 mt-1">Chỉ đối tượng trực tiếp chịu tác động của ngoại động từ (ví dụ: <i>Ich habe einen Kuli</i>).</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: BÍ QUYẾT NHẬN DIỆN GIỐNG THEO ĐUÔI HẬU TỐ & NHÓM NGHĨA -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm">2</span>
                <h4 class="text-lg font-black text-slate-900">Bí quyết Nhận diện Giống của Danh từ (der / die / das) theo Hậu tố & Nhóm nghĩa</h4>
            </div>
            <p class="text-xs sm:text-sm text-slate-600">
                Đây là bảng quy tắc vàng giúp bạn nhận diện chính xác giống của hàng nghìn danh từ mà không cần học vẹt:
            </p>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                <!-- DER -->
                <div class="p-5 rounded-2xl bg-blue-50/50 border border-blue-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-3 py-1 rounded-lg bg-blue-600 text-white font-black text-xs">der (Maskulinum)</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <p class="font-bold text-blue-900">🔹 Hậu tố luôn mang giống đực:</p>
                        <ul class="list-disc list-inside text-slate-700 space-y-1">
                            <li><b>-ant</b>: <i>der Praktikant</i> (thực tập sinh)</li>
                            <li><b>-ent</b>: <i>der Student</i> (nam sinh viên)</li>
                            <li><b>-ich</b>: <i>der Teppich</i> (tấm thảm)</li>
                            <li><b>-ismus</b>: <i>der Tourismus, der Optimismus</i></li>
                            <li><b>-ist</b>: <i>der Polizist, der Journalist</i></li>
                            <li><b>-ast</b>: <i>der Kontrast, der Palast</i></li>
                            <li><b>-ling</b>: <i>der Zwilling, der Schmetterling</i></li>
                        </ul>
                        <p class="font-bold text-blue-900 pt-2">🔹 Nhóm ý nghĩa luôn mang giống đực:</p>
                        <ul class="list-disc list-inside text-slate-700 space-y-1">
                            <li>12 Tháng trong năm (<i>der Januar, der Juni...</i>)</li>
                            <li>7 Thứ trong tuần (<i>der Montag, der Sonntag...</i>)</li>
                            <li>4 Mùa (<i>der Sommer, der Winter, der Frühling, der Herbst</i>)</li>
                            <li>4 Hướng (<i>der Norden, der Süden, der Osten, der Westen</i>)</li>
                            <li>Thời tiết (<i>der Wind, der Regen, der Schnee, der Nebel</i>)</li>
                            <li>Nghề nghiệp nam giới (<i>der Koch, der Lehrer, der Arzt</i>)</li>
                        </ul>
                    </div>
                </div>

                <!-- DIE -->
                <div class="p-5 rounded-2xl bg-rose-50/50 border border-rose-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-3 py-1 rounded-lg bg-rose-600 text-white font-black text-xs">die (Femininum)</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <p class="font-bold text-rose-900">🔸 Hậu tố luôn mang giống cái (100%):</p>
                        <ul class="list-disc list-inside text-slate-700 space-y-1">
                            <li><b>-heit</b>: <i>die Krankheit, die Freiheit</i></li>
                            <li><b>-keit</b>: <i>die Möglichkeit, die Pünktlichkeit</i></li>
                            <li><b>-schaft</b>: <i>die Freundschaft, die Mannschaft</i></li>
                            <li><b>-ung</b>: <i>die Kleidung, die Wohnung, die Übung</i></li>
                            <li><b>-ie</b>: <i>die Allergie, die Energie</i></li>
                            <li><b>-anz / -enz</b>: <i>die Distanz, die Konferenz</i></li>
                            <li><b>-in</b>: <i>die Sekretärin, die Lehrerin, die Studentin</i></li>
                        </ul>
                        <p class="font-bold text-rose-900 pt-2">🔸 Nhóm ý nghĩa luôn mang giống cái:</p>
                        <ul class="list-disc list-inside text-slate-700 space-y-1">
                            <li>Đa số loài cây (<i>die Tanne, die Eiche</i>)</li>
                            <li>Đa số loài hoa (<i>die Rose, die Tulpe, die Orchidee</i>)</li>
                        </ul>
                    </div>
                </div>

                <!-- DAS -->
                <div class="p-5 rounded-2xl bg-emerald-50/50 border border-emerald-200 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="px-3 py-1 rounded-lg bg-emerald-600 text-white font-black text-xs">das (Neutrum)</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <p class="font-bold text-emerald-900">🟢 Hậu tố luôn mang giống trung:</p>
                        <ul class="list-disc list-inside text-slate-700 space-y-1">
                            <li><b>-ment</b>: <i>das Dokument, das Medikament</i></li>
                            <li class="text-rose-700 font-bold">⚠️ Ngoại lệ: <i>der Moment</i> (khoảnh khắc)!</li>
                            <li><b>-um</b>: <i>das Studium, das Museum, das Zentrum</i></li>
                            <li><b>-tum</b>: <i>das Präteritum, das Eigentum</i></li>
                            <li><b>-chen / -lein</b> (thu nhỏ 100%): <i>das Brötchen, das Mädchen</i></li>
                            <li><b>-ma / -em</b>: <i>das Thema, das Klima, das System</i></li>
                            <li><b>-nis</b>: <i>das Ergebnis, das Zeugnis</i></li>
                            <li class="text-rose-700 font-bold">⚠️ Ngoại lệ: <i>die Erlaubnis</i> (sự cho phép)!</li>
                        </ul>
                        <p class="font-bold text-emerald-900 pt-2">🟢 Nhóm cấu tạo luôn mang giống trung:</p>
                        <ul class="list-disc list-inside text-slate-700 space-y-1">
                            <li>Động từ nguyên mẫu viết hoa (<i>das Essen, das Lesen</i>)</li>
                            <li>Tính từ hóa danh từ (<i>das Gute, das Neue</i>)</li>
                            <li>Kim loại (<i>das Gold, das Silber, das Eisen</i>)</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: BẢNG 18 TỪ VỰNG ĐỒ DÙNG LỚP HỌC & SỐ NHIỀU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm">3</span>
                <h4 class="text-lg font-black text-slate-900">18 Từ vựng Đồ dùng Lớp học & Quy tắc Số nhiều (Plural)</h4>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 border-b border-slate-200 font-bold">
                            <th class="p-3">Giống</th>
                            <th class="p-3">Số ít (Singular)</th>
                            <th class="p-3">Số nhiều (Plural)</th>
                            <th class="p-3">Nghĩa tiếng Việt</th>
                            <th class="p-3">Quy tắc biến đổi số nhiều</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Tisch</td><td class="p-3 text-indigo-600 font-semibold">die Tische</td><td class="p-3">cái bàn</td><td class="p-3 text-slate-500">Thêm đuôi -e</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Stuhl</td><td class="p-3 text-indigo-600 font-semibold">die Stühle</td><td class="p-3">cái ghế</td><td class="p-3 text-slate-500">Biến âm u → ü + đuôi -e</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Füller</td><td class="p-3 text-indigo-600 font-semibold">die Füller</td><td class="p-3">bút máy / bút mực</td><td class="p-3 text-slate-500">Đuôi -er giữ nguyên dạng</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Kuli</td><td class="p-3 text-indigo-600 font-semibold">die Kulis</td><td class="p-3">bút bi</td><td class="p-3 text-slate-500">Thêm đuôi -s</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Bleistift</td><td class="p-3 text-indigo-600 font-semibold">die Bleistifte</td><td class="p-3">bút chì</td><td class="p-3 text-slate-500">Thêm đuôi -e</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Radiergummi</td><td class="p-3 text-indigo-600 font-semibold">die Radiergummis</td><td class="p-3">cục tẩy / gôm</td><td class="p-3 text-slate-500">Thêm đuôi -s</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-blue-600">der</td><td class="p-3 font-bold">der Becher</td><td class="p-3 text-indigo-600 font-semibold">die Becher</td><td class="p-3">cái cốc / ly</td><td class="p-3 text-slate-500">Đuôi -er giữ nguyên dạng</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-rose-600">die</td><td class="p-3 font-bold">die Tafel</td><td class="p-3 text-indigo-600 font-semibold">die Tafeln</td><td class="p-3">cái bảng đen</td><td class="p-3 text-slate-500">Đuôi -el thêm -n</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-rose-600">die</td><td class="p-3 font-bold">die Brille</td><td class="p-3 text-indigo-600 font-semibold">die Brillen</td><td class="p-3">cái kính mắt</td><td class="p-3 text-slate-500">Đuôi -e thêm -n</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-rose-600">die</td><td class="p-3 font-bold">die Tasche</td><td class="p-3 text-indigo-600 font-semibold">die Taschen</td><td class="p-3">túi xách / cặp sách</td><td class="p-3 text-slate-500">Đuôi -e thêm -n</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-rose-600">die</td><td class="p-3 font-bold">die Landkarte</td><td class="p-3 text-indigo-600 font-semibold">die Landkarten</td><td class="p-3">bản đồ</td><td class="p-3 text-slate-500">Lấy giống theo die Karte, thêm -n</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Papier</td><td class="p-3 text-indigo-600 font-semibold">die Papiere</td><td class="p-3">tờ giấy</td><td class="p-3 text-slate-500">Thêm đuôi -e</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Heft</td><td class="p-3 text-indigo-600 font-semibold">die Hefte</td><td class="p-3">quyển vở</td><td class="p-3 text-slate-500">Thêm đuôi -e</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Buch</td><td class="p-3 text-indigo-600 font-semibold">die Bücher</td><td class="p-3">quyển sách</td><td class="p-3 text-slate-500">Biến âm u → ü + đuôi -er</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Wörterbuch</td><td class="p-3 text-indigo-600 font-semibold">die Wörterbücher</td><td class="p-3">quyển từ điển</td><td class="p-3 text-slate-500">Ghép (Wörter + Buch) → số nhiều theo Buch</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Handy</td><td class="p-3 text-indigo-600 font-semibold">die Handys</td><td class="p-3">điện thoại di động</td><td class="p-3 text-slate-500">Từ mượn thêm đuôi -s</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Whiteboard</td><td class="p-3 text-indigo-600 font-semibold">die Whiteboards</td><td class="p-3">bảng trắng</td><td class="p-3 text-slate-500">Từ mượn thêm đuôi -s</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-bold text-emerald-600">das</td><td class="p-3 font-bold">das Brötchen</td><td class="p-3 text-indigo-600 font-semibold">die Brötchen</td><td class="p-3">bánh mì nhỏ</td><td class="p-3 text-slate-500">Đuôi -chen giữ nguyên dạng</td></tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- HỌC PHẦN 4: ĐỘNG TỪ & MẪU CÂU GIAO TIẾP LỚP HỌC -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm">4</span>
                <h4 class="text-lg font-black text-slate-900">Động từ & 6 Mẫu câu Giao tiếp trong Lớp học (Sprache im Kurs)</h4>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="p-4 rounded-2xl bg-indigo-50 border border-indigo-100 space-y-2">
                    <h5 class="font-bold text-indigo-950 text-sm">🔹 Các Động từ lớp học cốt lõi:</h5>
                    <ul class="text-xs text-slate-700 space-y-2">
                        <li><b>heißen</b> (gọi là / tên là): <i>Wie heißt das auf Deutsch?</i></li>
                        <li><b>verstehen</b> (hiểu): <i>Das verstehe ich nicht.</i> (Đảo tân ngữ lên đầu, động từ ở vị trí 2).</li>
                        <li><b>können</b> (khuyết thiếu - có thể): <i>Können Sie das bitte ...?</i> (Đẩy động từ chính về cuối câu ở dạng nguyên mẫu).</li>
                        <li><b>wiederholen</b> (nhắc lại): <i>Können Sie das bitte wiederholen?</i></li>
                        <li><b>buchstabieren</b> (đánh vần): <i>Können Sie das bitte buchstabieren?</i></li>
                        <li><b>anschreiben</b> (viết lên bảng): <i>Können Sie das bitte anschreiben?</i></li>
                    </ul>
                </div>

                <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 space-y-2">
                    <h5 class="font-bold text-amber-950 text-sm">🔹 6 Mẫu câu giao tiếp chuẩn:</h5>
                    <ol class="list-decimal list-inside text-xs text-slate-700 space-y-1.5 font-medium">
                        <li><b>Wie heißt das auf Deutsch?</b> → Cái này tiếng Đức gọi là gì?</li>
                        <li><b>Was ist das auf Deutsch?</b> → Cái này trong tiếng Đức là gì?</li>
                        <li><b>Entschuldigung, wie bitte?</b> → Xin lỗi, Ngài nói sao cơ ạ?</li>
                        <li><b>Das verstehe ich nicht. Können Sie das bitte wiederholen?</b> → Tôi không hiểu. Ngài lặp lại được không?</li>
                        <li><b>Das verstehe ich nicht. Können Sie das bitte buchstabieren?</b> → Tôi không hiểu. Ngài đánh vần giúp tôi?</li>
                        <li><b>Das verstehe ich không -> Das verstehe ich nicht. Können Sie das bitte anschreiben?</b> → Tôi không hiểu. Ngài viết lên bảng giúp tôi?</li>
                    </ol>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 5: BẢNG 3 CỘT MẠO TỪ Ở CÁCH 1 (NOMINATIV) -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm">5</span>
                <h4 class="text-lg font-black text-slate-900">Bảng 3 Cột Mạo từ: Xác định, Bất định & Phủ định với "kein/keine"</h4>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-indigo-900 text-white font-bold">
                            <th class="p-3">Giống</th>
                            <th class="p-3">Mạo từ Xác định (đã biết rõ)</th>
                            <th class="p-3">Mạo từ Bất định (một cái bất kỳ)</th>
                            <th class="p-3">Mạo từ Phủ định (không phải là...)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100">
                        <tr class="bg-blue-50/30">
                            <td class="p-3 font-bold text-blue-700">Maskulinum (m)</td>
                            <td class="p-3 font-bold"><b>der</b> Kuli</td>
                            <td class="p-3 font-bold text-emerald-700"><b>ein</b> Kuli</td>
                            <td class="p-3 font-bold text-rose-700"><b>kein</b> Kuli</td>
                        </tr>
                        <tr class="bg-rose-50/30">
                            <td class="p-3 font-bold text-rose-700">Femininum (f)</td>
                            <td class="p-3 font-bold"><b>die</b> Brille</td>
                            <td class="p-3 font-bold text-emerald-700"><b>eine</b> Brille</td>
                            <td class="p-3 font-bold text-rose-700"><b>keine</b> Brille</td>
                        </tr>
                        <tr class="bg-emerald-50/30">
                            <td class="p-3 font-bold text-emerald-700">Neutrum (n)</td>
                            <td class="p-3 font-bold"><b>das</b> Handy</td>
                            <td class="p-3 font-bold text-emerald-700"><b>ein</b> Handy</td>
                            <td class="p-3 font-bold text-rose-700"><b>kein</b> Handy</td>
                        </tr>
                        <tr class="bg-amber-50/30">
                            <td class="p-3 font-bold text-amber-700">Plural (Số nhiều)</td>
                            <td class="p-3 font-bold"><b>die</b> Bücher</td>
                            <td class="p-3 font-bold text-slate-400">— (Không có)</td>
                            <td class="p-3 font-bold text-rose-700"><b>keine</b> Bücher</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="p-4 rounded-2xl bg-amber-50/80 border border-amber-200 text-xs sm:text-sm text-slate-700 space-y-1.5">
                <p class="font-bold text-amber-900">💡 Mẹo ghi nhớ siêu nhanh:</p>
                <p>1. Giống đực (<i>der</i>) và giống trung (<i>das</i>) dùng chung mạo từ bất định: <b>ein</b>, phủ định: <b>kein</b>.</p>
                <p>2. Giống cái (<i>die</i>) và số nhiều (<i>Plural</i>) dùng chung đuôi <b>-e</b>: <b>eine / keine</b> (Lưu ý: Số nhiều không có <i>eine</i>, chỉ có <i>keine</i>!).</p>
                <p>3. Khi có cụm sở hữu <b>von + Tên riêng</b> (ví dụ: <i>von Anna, von David</i>), đồ vật đã được xác định cụ thể nên ta dùng lại mạo từ xác định <b>der/die/das</b>!</p>
            </div>
        </div>

        <!-- HỌC PHẦN 6: THỰC HÀNH HỎI ĐÁP ĐỒ VẬT & SỞ HỮU -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="flex items-center justify-center w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 font-black text-sm">6</span>
                <h4 class="text-lg font-black text-slate-900">Thực hành Hỏi - Đáp Đồ vật & Sở hữu (Ist das ein/eine ...?)</h4>
            </div>

            <div class="space-y-3 text-xs sm:text-sm">
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-indigo-900">1. Hỏi bút bi (der Kuli):</p>
                    <p class="text-slate-700">Hỏi: <i>Ist das <b>ein</b> Kuli?</i> (Đây có phải là cây bút bi không?)</p>
                    <p class="text-emerald-800">Đáp khẳng định: <i>Ja, das ist <b>der</b> Kuli <b>von Anna</b>.</i> (Đúng, đó là cây bút bi của Anna.)</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-indigo-900">2. Hỏi điện thoại (das Handy):</p>
                    <p class="text-slate-700">Hỏi: <i>Ist das <b>ein</b> Handy?</i> (Đây có phải là điện thoại không?)</p>
                    <p class="text-emerald-800">Đáp: <i>Ja, das ist <b>das</b> Handy <b>von David</b>.</i> (Đúng, đó là điện thoại của David.)</p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-indigo-900">3. Hỏi kính mắt và phủ định (die Brille):</p>
                    <p class="text-slate-700">Hỏi: <i>Ist das <b>eine</b> Brille?</i> (Đây có phải là kính mắt không?)</p>
                    <p class="text-rose-800">Đáp phủ định + đính chính: <i>Nein, das ist <b>keine</b> Brille. Das ist <b>eine</b> Landkarte.</i></p>
                </div>
                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                    <p class="font-bold text-indigo-900">4. Hỏi cái cốc và tờ giấy (der Becher & das Papier):</p>
                    <p class="text-slate-700">Hỏi: <i>Ist das <b>ein</b> Becher?</i> (Đây có phải là cái cốc không?)</p>
                    <p class="text-rose-800">Đáp: <i>Nein, das ist <b>kein</b> Becher. Das ist <b>ein</b> Papier.</i> (Không, đó không phải là cái cốc. Đó là một tờ giấy.)</p>
                </div>
            </div>
        </div>
    </div>
    """

    cursor.execute("""
        INSERT INTO lessons (level_id, title, grammar_content)
        VALUES (?, ?, ?);
    """, (a1_id, lesson_title, grammar_html))
    lesson_id = cursor.lastrowid

    # =========================================================================
    # NẠP TỪ VỰNG BÀI 2 (36 TỪ CHUẨN ĐỒ DÙNG LỚP HỌC, ĐỘNG TỪ & HẬU TỐ)
    # =========================================================================
    vocabularies = [
        # Đồ dùng lớp học (der)
        (lesson_id, "Tisch", "der", "cái bàn", "Ist das ein Tisch? – Ja, das ist der Tisch im Kursraum."),
        (lesson_id, "Stuhl", "der", "cái ghế", "Das ist kein Tisch, das ist ein Stuhl."),
        (lesson_id, "Füller", "der", "bút mực / bút máy", "Ist das ein Füller? – Ja, das ist der Füller von Marc."),
        (lesson_id, "Kuli", "der", "bút bi (Kugelschreiber)", "Ist das ein Kuli? – Ja, das ist der Kuli von Anna."),
        (lesson_id, "Bleistift", "der", "bút chì", "Ich habe keinen Kuli, aber ich habe einen Bleistift."),
        (lesson_id, "Radiergummi", "der", "cục tẩy / gôm", "Wie heißt das auf Deutsch? – Das ist ein Radiergummi."),
        (lesson_id, "Becher", "der", "cái cốc / cái ly (không quai)", "Ist das ein Becher? – Nein, das ist kein Becher."),

        # Đồ dùng lớp học (die)
        (lesson_id, "Tafel", "die", "cái bảng đen", "Die Lehrerin schreibt an die Tafel."),
        (lesson_id, "Brille", "die", "cái kính mắt", "Ist das eine Brille? – Nein, das ist keine Brille."),
        (lesson_id, "Tasche", "die", "túi xách / cặp sách", "Ja, das ist die Tasche von Anna."),
        (lesson_id, "Landkarte", "die", "bản đồ", "Das ist keine Brille, das ist eine Landkarte."),

        # Đồ dùng lớp học (das)
        (lesson_id, "Papier", "das", "tờ giấy", "Ist das ein Becher? – Nein, das ist ein Papier."),
        (lesson_id, "Heft", "das", "quyển vở", "Können Sie 'das Heft' bitte buchstabieren? – H - E - F - T."),
        (lesson_id, "Buch", "das", "quyển sách", "Ist das ein Buch? – Ja, das ist das Buch von Frau Schiller."),
        (lesson_id, "Wörterbuch", "das", "quyển từ điển", "Das ist kein Heft, das ist ein Wörterbuch."),
        (lesson_id, "Handy", "das", "điện thoại di động", "Ist das ein Handy? – Ja, das ist das Handy von David."),
        (lesson_id, "Whiteboard", "das", "bảng trắng", "Im Deutschkurs haben wir eine Tafel und ein Whiteboard."),
        (lesson_id, "Brötchen", "das", "bánh mì nhỏ", "Ich esse ein Brötchen und trinke einen Kaffee."),

        # Động từ lớp học
        (lesson_id, "verstehen", "Verb", "hiểu, nắm bắt được", "Das verstehe ich nicht. Können Sie das bitte erklären?"),
        (lesson_id, "wiederholen", "Verb", "lặp lại, nhắc lại", "Das verstehe ich nicht. Können Sie das bitte wiederholen?"),
        (lesson_id, "buchstabieren", "Verb", "đánh vần", "Das verstehe ich nicht. Können Sie das bitte buchstabieren?"),
        (lesson_id, "anschreiben", "Verb", "viết lên bảng", "Das verstehe ich không -> Das verstehe ich nicht. Können Sie das bitte anschreiben?"),
        (lesson_id, "können", "Modalverb", "có thể (nhờ vả / khả năng)", "Können Sie das bitte langsam wiederholen?"),
        (lesson_id, "heißen", "Verb", "tên là, gọi là", "Wie heißt das auf Deutsch?"),

        # Hậu tố nhận biết giống & ngoại lệ
        (lesson_id, "Praktikant", "der", "nam thực tập sinh (-ant)", "Er ist ein Praktikant bei der Post."),
        (lesson_id, "Student", "der", "nam sinh viên (-ent)", "David ist ein Student aus den USA."),
        (lesson_id, "Teppich", "der", "tấm thảm (-ich)", "Ist das ein Teppich? – Ja, der Teppich ist sehr schön."),
        (lesson_id, "Polizist", "der", "nam cảnh sát (-ist)", "Mein Freund arbeitet als Polizist in Berlin."),
        (lesson_id, "Krankheit", "die", "căn bệnh (-heit)", "Das ist keine schlimme Krankheit."),
        (lesson_id, "Möglichkeit", "die", "khả năng / cơ hội (-keit)", "Das ist eine gute Möglichkeit für uns."),
        (lesson_id, "Freundschaft", "die", "tình bạn (-schaft)", "Die Freundschaft von Anna und Sophie ist toll."),
        (lesson_id, "Kleidung", "die", "quần áo, trang phục (-ung)", "Die Kleidung aus Italien ist sehr modern."),
        (lesson_id, "Dokument", "das", "tài liệu (-ment)", "Ist das ein Dokument? – Ja, das ist das Dokument von Herr Nguyen."),
        (lesson_id, "Moment", "der", "khoảnh khắc, giây lát (NGOẠI LỆ -ment)", "Einen Moment, bitte! Ich schreibe das Wort an."),
        (lesson_id, "Ergebnis", "das", "kết quả (-nis)", "Das Ergebnis im Deutschkurs ist super."),
        (lesson_id, "Erlaubnis", "die", "sự cho phép (NGOẠI LỆ -nis)", "Hast du eine Erlaubnis von der Lehrerin?")
    ]

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # NẠP KHO 50 CÂU HỎI BÀI 2 (ĐỦ 7 DẠNG KỸ NĂNG: 10 + 10 + 8 + 6 + 5 + 4 + 7)
    # =========================================================================
    passage_doc = (
        "Frau Schiller: Guten Morgen zusammen! Was ist das auf Deutsch, Marc?\n"
        "Marc: Das ist ein Kuli.\n"
        "Frau Schiller: Sehr gut! Das ist der Kuli von Anna. Und Anna, ist das ein Heft?\n"
        "Anna: Nein, Frau Schiller, das ist kein Heft. Das ist ein Wörterbuch.\n"
        "David: Entschuldigung, wie bitte? Das verstehe ich nicht. Können Sie das bitte anschreiben?\n"
        "Frau Schiller: Ja, natürlich: W - Ö - R - T - E - R - B - U - C - H. Das ist ein Wörterbuch. "
        "Auf dem Tisch haben wir auch eine Landkarte und drei Stühle."
    )

    exercises = [
        # ---------------------------------------------------------------------
        # DẠNG 1: TRẮC NGHIỆM (trac_nghiem) - ĐÚNG 10 CÂU (Câu 1 -> 10)
        # ---------------------------------------------------------------------
        (
            lesson_id, "trac_nghiem",
            "Câu 1 [Quy tắc hậu tố]: Mọi danh từ có hậu tố '-ung' (như Kleidung, Wohnung, Übung) luôn mang giống gì?",
            json.dumps(["die (Femininum)", "der (Maskulinum)", "das (Neutrum)", "Tùy thuộc vào ngữ cảnh"]),
            "die (Femininum)",
            "Tất cả danh từ tận cùng bằng -ung đều mang giống cái (die) 100%.", 10, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 2 [Quy tắc hậu tố]: Các danh từ có đuôi '-heit', '-keit', '-schaft' (như Krankheit, Möglichkeit, Freundschaft) mang giống nào?",
            json.dumps(["die (Femininum)", "der (Maskulinum)", "das (Neutrum)", "Có thể là der hoặc das"]),
            "die (Femininum)",
            "Các đuôi -heit, -keit, -schaft luôn là dấu hiệu nhận biết 100% của giống cái (die).", 10, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 3 [Bẫy Ngoại Lệ Cực Kỳ Quan Trọng]: Đa số danh từ đuôi '-ment' mang giống trung (das), nhưng từ 'Moment' (khoảnh khắc) mang giống gì?",
            json.dumps(["der Moment (Giống đực)", "das Moment (Giống trung)", "die Moment (Giống cái)", "Không có mạo từ"]),
            "der Moment (Giống đực)",
            "⚠️ Bẫy ngoại lệ kinh điển: 'der Moment' là giống đực, dù kết thúc bằng -ment!", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 4 [Bẫy Ngoại Lệ Cực Kỳ Quan Trọng]: Đa số danh từ đuôi '-nis' mang giống trung (das Ergebnis), nhưng 'Erlaubnis' (sự cho phép) mang giống gì?",
            json.dumps(["die Erlaubnis (Giống cái)", "das Erlaubnis (Giống trung)", "der Erlaubnis (Giống đực)", "Cả der và das đều đúng"]),
            "die Erlaubnis (Giống cái)",
            "⚠️ Bẫy ngoại lệ kinh điển: 'die Erlaubnis' là giống cái, dù kết thúc bằng -nis!", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 5 [Hậu tố giảm nhẹ]: Danh từ có đuôi thu nhỏ / giảm nhẹ '-chen' (như Brötchen, Mädchen) luôn mang giống gì?",
            json.dumps(["das (Neutrum)", "die (Femininum)", "der (Maskulinum)", "Thay đổi theo giới tính"]),
            "das (Neutrum)",
            "Các danh từ có hậu tố giảm nhẹ -chen hoặc -lein luôn mang giống trung (das) 100%.", 10, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 6 [Nhóm ý nghĩa]: Tên các tháng trong năm (Januar, Mai, Juni) và các mùa (Sommer, Winter) mang giống nào?",
            json.dumps(["der (Maskulinum)", "die (Femininum)", "das (Neutrum)", "Không có mạo từ"]),
            "der (Maskulinum)",
            "Tháng, thứ trong tuần, các mùa và các hướng không gian luôn mang giống đực (der).", 10, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 7 [Danh từ ghép]: Danh từ ghép 'das Wörterbuch' (quyển từ điển) lấy giống theo thành phần nào?",
            json.dumps(["Từ đứng cuối cùng (das Buch)", "Từ đứng đầu tiên (die Wörter)", "Từ có số lượng âm tiết nhiều hơn", "Mặc định luôn là giống đực der"]),
            "Từ đứng cuối cùng (das Buch)",
            "Nguyên tắc danh từ ghép tiếng Đức: Giống và dạng số nhiều luôn được xác định bởi từ đứng cuối cùng (das Buch -> das Wörterbuch).", 10, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 8 [Ngữ pháp Mạo từ]: Mạo từ bất định (ein / eine) ở dạng số nhiều (Plural) là gì?",
            json.dumps(["Không có mạo từ bất định (Nullartikel)", "Dùng mạo từ 'eine'", "Dùng mạo từ 'einen'", "Dùng mạo từ 'einer'"]),
            "Không có mạo từ bất định (Nullartikel)",
            "Số nhiều không có mạo từ bất định! Chỉ nói 'Das sind Bücher', không bao giờ có 'eine Bücher'.", 15, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 9 [Giao tiếp lớp học]: Khi bạn không biết tên một đồ vật bằng tiếng Đức, bạn hỏi câu nào?",
            json.dumps(["Wie heißt das auf Deutsch?", "Wer bist du?", "Woher kommen Sie?", "Wie alt sind Sie?"]),
            "Wie heißt das auf Deutsch?",
            "'Wie heißt das auf Deutsch?' nghĩa là 'Cái này tiếng Đức gọi là gì?'.", 10, None
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 10 [Mạo từ phủ định]: Để phủ định danh từ số nhiều ở cách 1 (ví dụ: 'Das sind ___ Bücher'), ta dùng từ nào?",
            json.dumps(["keine", "kein", "nicht", "keinen"]),
            "keine",
            "Phủ định danh từ số nhiều ở Nominativ dùng 'keine' (Das sind keine Bücher).", 10, None
        ),

        # ---------------------------------------------------------------------
        # DẠNG 2: ĐIỀN KHUYẾT MẠO TỪ & ĐỘNG TỪ (dien_khuyet) - ĐÚNG 10 CÂU (Câu 11 -> 20)
        # ---------------------------------------------------------------------
        (
            lesson_id, "dien_khuyet",
            "Câu 11: Điền mạo từ bất định thích hợp: 'Ist das ___ Brille? – Ja, das ist eine Brille.'",
            None, "eine",
            "'die Brille' là giống cái nên mạo từ bất định là 'eine'.", 10, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 12: Điền mạo từ bất định thích hợp: 'Ist das ___ Kuli? – Ja, das ist ein Kuli.'",
            None, "ein",
            "'der Kuli' là giống đực nên mạo từ bất định là 'ein'.", 10, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 13: Điền mạo từ thích hợp: 'Das ist kein Tisch, das ist ___ Stuhl.'",
            None, "ein",
            "'der Stuhl' là giống đực nên dùng 'ein Stuhl'.", 10, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 14: Điền từ phủ định: 'Ist das eine Landkarte? – Nein, das ist ___ Landkarte.'",
            None, "keine",
            "'die Landkarte' là giống cái nên phủ định bằng 'keine'.", 10, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 15: Điền dạng chia của động từ 'verstehen': 'Das ___ ich nicht. Können Sie das bitte wiederholen?'",
            None, "verstehe",
            "Chủ ngữ là 'ich' nên động từ chia là 'verstehe'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 16: Điền động từ thích hợp: 'Können Sie das Wort bitte ___? – H - E - F - T.'",
            None, "buchstabieren",
            "Khi đánh vần từng chữ cái, ta dùng động từ 'buchstabieren' ở dạng nguyên mẫu cuối câu.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 17: Điền động từ thích hợp: 'Können Sie das Wort bitte an die Tafel ___?' (viết lên bảng)",
            None, "anschreiben",
            "Động từ 'anschreiben' (viết lên bảng) đứng ở cuối câu sau 'Können Sie...'.", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 18: Điền dạng số nhiều của 'der Stuhl': 'Im Kursraum gibt es einen Tisch und vier ___.'",
            None, "Stühle",
            "Số nhiều của 'der Stuhl' là 'die Stühle' (biến âm u -> ü và thêm -e).", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 19: Điền dạng số nhiều của 'das Buch': 'Auf dem Tisch liegen viele ___.'",
            None, "Bücher",
            "Số nhiều của 'das Buch' là 'die Bücher' (biến âm u -> ü và thêm -er).", 15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 20 [Mạo từ & Phủ định (Random)]: Hoàn thành câu trả lời phủ định: \"Ist das eine Tasche?\" → \"Nein, das ist ___ Tasche. Das ist ___ Bleistift.\" (Điền 2 từ mạo từ cách nhau bởi dấu phẩy):",
            None, "keine, ein",
            "'Tasche' mang giống die nên phủ định là 'keine'; 'Bleistift' mang giống der nên dùng 'ein'.", 20,
            json.dumps({"dynamic_article_quiz": True})
        ),

        # ---------------------------------------------------------------------
        # DẠNG 3: DỊCH 2 CHIỀU VIỆT ⇄ ĐỨC (dich) - ĐÚNG 8 CÂU (Câu 21 -> 28)
        # ---------------------------------------------------------------------
        (
            lesson_id, "dich",
            "Câu 21 [Dịch Đức → Việt]: Hãy dịch câu giao tiếp sau sang tiếng Việt: 'Wie heißt das auf Deutsch?'",
            None, "Cái này tiếng Đức gọi là gì? / Cái này gọi là gì trong tiếng Đức? / Cái này tiếng Đức là gì? / Trong tiếng Đức cái này gọi là gì? / Cái này đọc là gì trong tiếng Đức?",
            "'Wie heißt das auf Deutsch?' = Cái này tiếng Đức gọi là gì? (hoặc Trong tiếng Đức cái này tên là gì?).", 15, None
        ),
        (
            lesson_id, "dich",
            "Câu 22 [Dịch Đức → Việt]: Hãy dịch câu giao tiếp sau sang tiếng Việt: 'Das verstehe ich nicht. Können Sie das bitte wiederholen?'",
            None, "Tôi không hiểu điều đó. Ngài có thể vui lòng lặp lại được không? / Tôi không hiểu. Ngài có thể nhắc lại được không? / Tôi không hiểu, bạn có thể nhắc lại được không? / Tôi không hiểu điều này. Bạn có thể nhắc lại được không? / Tôi không hiểu. Ngài có thể lặp lại được không? / Tôi không hiểu, ngài có thể lặp lại được không?",
            "'Das verstehe ich nicht' = Tôi không hiểu điều đó; 'Können Sie das bitte wiederholen?' = Ngài có thể vui lòng nhắc lại được không?", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 23 [Dịch Đức → Việt]: Hãy dịch câu sau sang tiếng Việt: 'Das ist kein Heft, das ist ein Wörterbuch.'",
            None, "Đó không phải là quyển vở, đó là một quyển từ điển. / Đây không phải là quyển vở, đây là một quyển từ điển. / Đó không phải là vở, đó là từ điển. / Đó không phải quyển vở, đó là một cuốn từ điển. / Kia không phải quyển vở, kia là cuốn từ điển.",
            "'kein Heft' = không phải quyển vở; 'ein Wörterbuch' = một quyển từ điển.", 15, None
        ),
        (
            lesson_id, "dich",
            "Câu 24 [Dịch Đức → Việt]: Hãy dịch câu sau sang tiếng Việt: 'Ist das ein Handy? – Ja, das ist das Handy von David.'",
            None, "Đây có phải là điện thoại không? – Đúng, đó là điện thoại của David. / Đây là điện thoại phải không? – Vâng, đó là điện thoại của David. / Đây có phải là điện thoại không? – Vâng, đó là điện thoại của David. / Đây có phải điện thoại không? – Đúng, đó là điện thoại của David.",
            "'das Handy von David' = điện thoại của David.", 15, None
        ),
        (
            lesson_id, "dich",
            "Câu 25 [Dịch Việt → Đức]: Dịch câu lịch sự khi nghe không rõ sang tiếng Đức: 'Xin lỗi, Ngài nói sao cơ ạ?'",
            None, "Entschuldigung, wie bitte? / Wie bitte? / Entschuldigung, wie bitte / Entschuldigen Sie, wie bitte?",
            "'Entschuldigung, wie bitte?' là câu hỏi lịch sự khi chưa nghe rõ lời đối phương.", 15, None
        ),
        (
            lesson_id, "dich",
            "Câu 26 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Ngài có thể vui lòng đánh vần từ đó được không?'",
            None, "Können Sie das bitte buchstabieren? / Können Sie das Wort bitte buchstabieren? / Können Sie das bitte buchstabieren / Kannst du das bitte buchstabieren?",
            "Cấu trúc nhờ vả: 'Können Sie das bitte buchstabieren?'.", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 27 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Ngài có thể vui lòng viết từ đó lên bảng được không?'",
            None, "Können Sie das bitte anschreiben? / Können Sie das bitte an die Tafel schreiben? / Können Sie das bitte anschreiben / Kannst du das bitte anschreiben?",
            "'anschreiben' = viết lên bảng. Câu hỏi: 'Können Sie das bitte anschreiben?'.", 20, None
        ),
        (
            lesson_id, "dich",
            "Câu 28 [Dịch Việt → Đức]: Dịch câu sau sang tiếng Đức: 'Không, đó không phải là kính mắt. Đó là một tấm bản đồ.'",
            None, "Nein, das ist keine Brille. Das ist eine Landkarte. / Nein, das ist keine Brille, das ist eine Landkarte. / Nein, das ist keine Brille. Es ist eine Landkarte.",
            "'keine Brille' (phủ định die) và 'eine Landkarte' (bất định die).", 20, None
        ),

        # ---------------------------------------------------------------------
        # DẠNG 4: LUYỆN NGHE (nghe) - ĐÚNG 6 CÂU (Câu 29 -> 34)
        # ---------------------------------------------------------------------
        (
            lesson_id, "nghe",
            "Câu 29 [Luyện Nghe]: Nghe câu sau và điền cụm từ nghe được: 'Das ist ___ von Anna.'",
            None, "der Kuli",
            "Âm thanh phát: 'Das ist der Kuli von Anna.' → Cụm từ cần điền là 'der Kuli'.", 15,
            json.dumps({"audio_text": "Das ist der Kuli von Anna."})
        ),
        (
            lesson_id, "nghe",
            "Câu 30 [Luyện Nghe]: Nghe câu phủ định và điền cụm mạo từ + danh từ: 'Nein, das ist ___.'",
            None, "keine Brille",
            "Âm thanh phát: 'Nein, das ist keine Brille. Das ist eine Landkarte.' → Cần điền 'keine Brille'.", 15,
            json.dumps({"audio_text": "Nein, das ist keine Brille. Das ist eine Landkarte."})
        ),
        (
            lesson_id, "nghe",
            "Câu 31 [Luyện Nghe]: Nghe câu hỏi lớp học và chép lại hoàn chỉnh bằng tiếng Đức:",
            None, "Wie heißt das auf Deutsch? / Wie heißt das auf Deutsch",
            "Âm thanh phát câu hỏi: 'Wie heißt das auf Deutsch?'", 20,
            json.dumps({"audio_text": "Wie heißt das auf Deutsch?"})
        ),
        (
            lesson_id, "nghe",
            "Câu 32 [Luyện Nghe]: Nghe câu nhờ vả và điền động từ ở cuối câu: 'Können Sie das bitte ___?'",
            None, "wiederholen / bitte wiederholen",
            "Âm thanh phát: 'Können Sie das bitte wiederholen?' → Động từ là 'wiederholen'.", 15,
            json.dumps({"audio_text": "Können Sie das bitte wiederholen?"})
        ),
        (
            lesson_id, "nghe",
            "Câu 33 [Luyện Nghe số nhiều]: Nghe câu miêu tả phòng học và điền 2 danh từ số nhiều: 'Im Kursraum gibt es viele ___ und ___.' (cách nhau bởi dấu phẩy):",
            None, "Tische, Stühle / Tische und Stühle / Stühle, Tische",
            "Âm thanh phát: 'Im Kursraum gibt es viele Tische und Stühle.' → Điền 'Tische, Stühle'.", 20,
            json.dumps({"audio_text": "Im Kursraum gibt es viele Tische und Stühle."})
        ),
        (
            lesson_id, "nghe",
            "Câu 34 [Luyện Nghe sở hữu]: Nghe câu sau và điền cụm từ: 'Das ist ___ von Frau Schiller.'",
            None, "das Wörterbuch",
            "Âm thanh phát: 'Das ist das Wörterbuch von Frau Schiller.' → Điền 'das Wörterbuch'.", 15,
            json.dumps({"audio_text": "Das ist das Wörterbuch von Frau Schiller."})
        ),

        # ---------------------------------------------------------------------
        # DẠNG 5: SẮP XẾP TỪ THÀNH CÂU (sap_xep) - ĐÚNG 5 CÂU (Câu 35 -> 39)
        # ---------------------------------------------------------------------
        (
            lesson_id, "sap_xep",
            "Câu 35 [Sắp xếp từ thành câu]: Sắp xếp câu hỏi kinh điển trong lớp học: 'Cái này tiếng Đức gọi là gì?': [heißt / Deutsch / Wie / auf / das / ?]",
            None, "Wie heißt das auf Deutsch?",
            "Cấu trúc hỏi từ vựng trong tiếng Đức: Wie + heißt + das + auf Deutsch?", 20,
            json.dumps({"audio_text": "Wie heißt das auf Deutsch?", "translation": "Cái này tiếng Đức gọi là gì?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 36 [Sắp xếp từ thành câu]: Sắp xếp câu giao tiếp: 'Tôi không hiểu điều đó. Ngài nhắc lại được không?': [verstehe / Das / nicht / . / bitte / Können / wiederholen / das / Sie / ?]",
            None, "Das verstehe ich nicht. Können Sie das bitte wiederholen?",
            "Mệnh đề 1: Das verstehe ich không. Mệnh đề 2: Động từ khuyết thiếu Können đảo lên đầu câu hỏi Ja/Nein: Können Sie das bitte wiederholen?", 20,
            json.dumps({"audio_text": "Das verstehe ich nicht. Können Sie das bitte wiederholen?", "translation": "Tôi không hiểu điều đó. Ngài có thể vui lòng nhắc lại được không?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 37 [Sắp xếp từ thành câu]: Sắp xếp câu nhờ giáo viên đánh vần từ vựng: [Sie / buchstabieren / bitte / Können / das / ?]",
            None, "Können Sie das bitte buchstabieren?",
            "Câu hỏi lịch sự dùng động từ khuyết thiếu können: Können đứng vị trí 1, chủ ngữ Sie vị trí 2, bitte ở giữa, động từ buchstabieren nguyên thể ở cuối.", 20,
            json.dumps({"audio_text": "Können Sie das bitte buchstabieren?", "translation": "Ngài có thể vui lòng đánh vần từ đó được không?"}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 38 [Sắp xếp từ thành câu]: Sắp xếp câu phủ định mạo từ và khẳng định: [keine / Brille / Nein / das / ist / . / eine / Das / Landkarte / ist / .]",
            None, "Nein, das ist keine Brille. Das ist eine Landkarte.",
            "Nein, das ist keine Brille (die Brille dùng keine). Das ist eine Landkarte (die Landkarte dùng eine).", 20,
            json.dumps({"audio_text": "Nein, das ist keine Brille. Das ist eine Landkarte.", "translation": "Không, đó không phải là kính mắt. Đó là một tấm bản đồ."}, ensure_ascii=False)
        ),
        (
            lesson_id, "sap_xep",
            "Câu 39 [Sắp xếp từ thành câu]: Sắp xếp câu xác nhận sở hữu từ điển của bà Schiller: [das Wörterbuch / ist / Ja / Frau Schiller / von / das / .]",
            None, "Ja, das ist das Wörterbuch von Frau Schiller.",
            "Ja, das ist das Wörterbuch (giống trung das) von Frau Schiller (cụm sở hữu von + tên người).", 20,
            json.dumps({"audio_text": "Ja, das ist das Wörterbuch von Frau Schiller.", "translation": "Vâng, đó là cuốn từ điển của bà Schiller."}, ensure_ascii=False)
        ),

        # ---------------------------------------------------------------------
        # DẠNG 6: ĐỌC HIỂU TÌNH HUỐNG LỚP HỌC (doc) - ĐÚNG 4 CÂU (Câu 40 -> 43)
        # ---------------------------------------------------------------------
        (
            lesson_id, "doc",
            "Câu 40 [Đọc hiểu 1]: Dựa vào đoạn hội thoại lớp học, cây bút bi (Kuli) trên bàn là của ai?",
            json.dumps([
                "Của bạn Anna",
                "Của bạn Marc",
                "Của bạn David",
                "Của cô giáo Frau Schiller"
            ]),
            "Của bạn Anna",
            "Cô giáo Frau Schiller xác nhận: 'Sehr gut! Das ist der Kuli von Anna.'", 20,
            json.dumps({"passage": passage_doc})
        ),
        (
            lesson_id, "doc",
            "Câu 41 [Đọc hiểu 2]: Đồ vật mà cô giáo chỉ vào khi hỏi Anna thực chất là gì?",
            json.dumps([
                "Một quyển từ điển",
                "Một quyển vở",
                "Một chiếc kính mắt",
                "Một tờ giấy"
            ]),
            "Một quyển từ điển",
            "Anna trả lời: 'Nein, Frau Schiller, das ist kein Heft. Das ist ein Wörterbuch.'", 20,
            json.dumps({"passage": passage_doc})
        ),
        (
            lesson_id, "doc",
            "Câu 42 [Đọc hiểu 3]: Bạn David đã nhờ cô giáo làm điều gì khi không hiểu từ mới?",
            json.dumps([
                "Viết từ đó lên bảng",
                "Nói lại thật nhanh",
                "Cho bạn ấy mượn từ điển",
                "Đọc dịch sang tiếng Anh"
            ]),
            "Viết từ đó lên bảng",
            "David nói: 'Das verstehe ich không hiểu. Können Sie das bitte anschreiben?'", 20,
            json.dumps({"passage": passage_doc})
        ),
        (
            lesson_id, "doc",
            "Câu 43 [Đọc hiểu 4]: Trong lớp học, ngoài bàn và từ điển thì còn có những đồ vật gì nữa?",
            json.dumps([
                "Một tấm bản đồ và ba cái ghế",
                "Một chiếc điện thoại và hai quyển vở",
                "Bốn chiếc cốc và một cái bánh mì",
                "Không có thêm đồ vật nào"
            ]),
            "Một tấm bản đồ và ba cái ghế",
            "Cô giáo nói: 'Auf dem Tisch haben wir auch eine Landkarte und drei Stühle.'", 20,
            json.dumps({"passage": passage_doc})
        ),

        # ---------------------------------------------------------------------
        # DẠNG 7: VIẾT CÂU & SỐ NHIỀU (viet) - ĐÚNG 7 CÂU (Câu 44 -> 50)
        # ---------------------------------------------------------------------
        (
            lesson_id, "viet",
            "Câu 44 [Sắp xếp khung câu Satzklammer]: Sắp xếp các từ sau thành câu nhờ vả hoàn chỉnh: 'bitte / Sie / Können / das / wiederholen / ?'",
            None, "Können Sie das bitte wiederholen? / Können Sie das bitte wiederholen / Können Sie das wiederholen, bitte? / Können Sie das wiederholen bitte / Können Sie bitte das wiederholen? / Können Sie bitte wiederholen? / Können Sie wiederholen bitte? / Können Sie wiederholen bitte",
            "Cấu trúc khung câu: Động từ khuyết thiếu 'Können' ở đầu câu hỏi + Sie + das bitte + động từ nguyên mẫu 'wiederholen' ở cuối câu.", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 45 [Sắp xếp khung câu Satzklammer]: Sắp xếp các từ sau thành câu hoàn chỉnh: 'buchstabieren / bitte / das / Sie / Können / ?'",
            None, "Können Sie das bitte buchstabieren? / Können Sie das bitte buchstabieren / Können Sie das buchstabieren, bitte? / Können Sie das buchstabieren bitte / Können Sie bitte das buchstabieren? / Können Sie bitte buchstabieren? / Können Sie buchstabieren bitte? / Können Sie buchstabieren bitte",
            "Cấu trúc: Können + Sie + das bitte + buchstabieren?", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 46 [Chuyển đổi số nhiều]: Hãy viết dạng số nhiều (kèm mạo từ 'die') của danh từ 'das Buch':",
            None, "die Bücher / Bücher",
            "'das Buch' chuyển sang số nhiều là 'die Bücher' (biến âm u -> ü và thêm -er).", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 47 [Chuyển đổi số nhiều]: Hãy viết dạng số nhiều (kèm mạo từ 'die') của danh từ 'der Tisch':",
            None, "die Tische / Tische",
            "'der Tisch' chuyển sang số nhiều là 'die Tische' (thêm đuôi -e).", 25, None
        ),
        (
            lesson_id, "viet",
            "Câu 48 [Mạo từ Sở Hữu (Random)]: Hoàn thành câu xác nhận đồ vật của David: \"Ist das ___ Handy?\" → \"Ja, das ist ___ Handy von David.\" (Điền 2 từ mạo từ cách nhau bởi dấu phẩy):",
            None, "ein, das",
            "'Handy' mang giống das → Mạo từ bất định là 'ein' và mạo từ sở hữu là 'das Handy von David'.", 25,
            json.dumps({"dynamic_possessive_article": True})
        ),
        (
            lesson_id, "viet",
            "Câu 49 [Số Nhiều Danh Từ (Random)]: Hãy viết dạng số nhiều (kèm mạo từ 'die') của danh từ 'der Stuhl':",
            None, "die Stühle / Stühle",
            "'der Stuhl' khi chuyển sang số nhiều là 'die Stühle' (biến âm u -> ü và thêm -e).", 25,
            json.dumps({"dynamic_plural_quiz": True})
        ),
        (
            lesson_id, "viet",
            "Câu 50 [Mạo từ & Phủ định (Random)]: Hoàn thành câu trả lời phủ định: \"Ist das ein Becher?\" → \"Nein, das ist ___ Becher. Das ist ___ Papier.\" (Điền 2 từ mạo từ cách nhau bởi dấu phẩy):",
            None, "kein, ein",
            "'Becher' là giống đực der nên phủ định là 'kein'; 'Papier' là giống trung das nên dùng 'ein'.", 30,
            json.dumps({"dynamic_article_quiz": True})
        )
    ]

    import random
    shuffled_exercises = []
    for ex in exercises:
        ex_list = list(ex)
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
    print("✅ Đã khởi tạo thành công Bài 2: 'Sprache im Kurs - Động Từ và Giống (der, die, das & Mạo Từ)' với đầy đủ 6 Học phần Lý thuyết (Không link YouTube) + 36 Từ vựng + ĐÚNG 50 Bài tập (10+10+8+6+5+4+7) có Random Đổi đề!")

if __name__ == "__main__":
    seed_lesson_2()
