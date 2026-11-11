import json
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_5():
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

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 5%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 19

    # Xóa dữ liệu cũ của Bài 5 nếu có để cập nhật sạch sẽ
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM lessons WHERE id = ?;", (lesson_id,))

    lesson_title = 'Bài 5: "Thời gian - Động từ tách - Haben in Präteritum (Termine)"'

    # =========================================================================
    # NỘI DUNG LÝ THUYẾT CHI TIẾT (6 HỌC PHẦN CHUẨN ĐẶC TẢ - KHÔNG LINK YOUTUBE)
    # =========================================================================
    grammar_html = """
    <div class="space-y-8 text-slate-700 leading-relaxed">
        <!-- BANNER TỔNG QUAN BÀI 5 DEUTSCHMEISTER -->
        <div class="p-6 sm:p-8 rounded-3xl bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white shadow-xl border border-slate-800 relative overflow-hidden">
            <div class="relative z-10 space-y-3">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/20 border border-indigo-400/30 text-indigo-300 text-xs font-bold">
                        🇩🇪 DeutschMeister A1 • Thời Gian • Động Từ Tách • Haben ở Quá Khứ (Bài 5)
                    </span>
                    <span class="text-xs text-amber-400 font-semibold flex items-center gap-1.5">
                        ⏱️ Thời lượng ước tính: 90 phút • ⚡ 900+ EXP
                    </span>
                </div>
                <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">
                    Thời Gian - Động Từ Tách - Haben in Präteritum (Termine)
                </h3>
                <p class="text-slate-300 text-xs sm:text-sm leading-relaxed max-w-4xl">
                    <b>Mục tiêu bài học:</b> Hệ thống toàn diện đơn vị thời gian, các thứ trong tuần (<i>der Montag → Sonntag</i>), 6 buổi trong ngày (<i>der Morgen → die Nacht</i>), 12 tháng và 4 mùa; làm chủ 2 cách đọc giờ (Chính thống 24h & Đời thường 12h với <i>vor / nach / Viertel / halb</i>); ghi nhớ ma trận giới từ thời gian (<i>um, am, im, in der, von...bis</i>); nắm vững quy tắc khung câu (<i>Satzklammer</i>) với <b>Động từ tách (Trennbare Verben)</b>; miêu tả lưu loát lịch trình một ngày (<i>Tagesabläufe</i>) với quy tắc đảo ngữ V2; và làm chủ thì quá khứ đơn (<b>Präteritum</b>) của động từ <i>haben (hatte, hattest, hatten...)</i> đối chiếu với <i>sein (war, waren...)</i>.
                </p>
            </div>
        </div>

        <!-- HỌC PHẦN 1: ĐƠN VỊ THỜI GIAN, CÁC THỨ, CÁC BUỔI TRONG NGÀY & 12 THÁNG -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-sm">1</span>
                <h4 class="text-lg font-bold text-slate-900">Đơn Vị Thời Gian, 7 Thứ Trong Tuần, 6 Buổi & 12 Tháng</h4>
            </div>

            <!-- Bảng 1.1: Đơn vị thời gian cơ bản -->
            <div class="space-y-3">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>⏱️</span> 1.1. Các Đơn Vị Thời Gian Cơ Bản (Zeiteinheiten)
                </h5>
                <p class="text-xs text-slate-600">
                    💡 <b>Mẹo nhớ giống:</b> Các đơn vị nhỏ (<i>die Sekunde, die Minute, die Stunde, die Woche</i>) mang giống cái <b>die</b>; <i>der Tag</i> và <i>der Monat</i> mang giống đực <b>der</b>; <i>das Wochenende</i> và <i>das Jahr</i> mang giống trung <b>das</b>.
                </p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Giống & Mạo từ</th>
                                <th class="p-3">Số Ít (Singular)</th>
                                <th class="p-3">Số Nhiều (Plural)</th>
                                <th class="p-3">Nghĩa Tiếng Việt</th>
                                <th class="p-3">Ví Dụ Chuẩn (Phát âm & Dịch nghĩa)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-rose-600">die (f)</td>
                                <td class="p-3 font-semibold">die Sekunde</td>
                                <td class="p-3">die Sekunden</td>
                                <td class="p-3">giây</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Eine Minute hat sechzig Sekunden.“<br><span class="text-xs text-slate-500">(Một phút có sáu mươi giây.)</span></span>
                                        <button onclick="speakGerman('Eine Minute hat sechzig Sekunden.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-rose-600">die (f)</td>
                                <td class="p-3 font-semibold">die Minute</td>
                                <td class="p-3">die Minuten</td>
                                <td class="p-3">phút</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Der Bus kommt in fünf Minuten.“<br><span class="text-xs text-slate-500">(Xe buýt sẽ đến trong năm phút nữa.)</span></span>
                                        <button onclick="speakGerman('Der Bus kommt in fünf Minuten.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-rose-600">die (f)</td>
                                <td class="p-3 font-semibold">die Stunde</td>
                                <td class="p-3">die Stunden</td>
                                <td class="p-3">tiếng, giờ đồng hồ (thời lượng)</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Heute arbeite ich acht Stunden.“<br><span class="text-xs text-slate-500">(Hôm nay tôi làm việc tám tiếng đồng hồ.)</span></span>
                                        <button onclick="speakGerman('Heute arbeite ich acht Stunden.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-blue-600">der (m)</td>
                                <td class="p-3 font-semibold">der Tag</td>
                                <td class="p-3">die Tage</td>
                                <td class="p-3">ngày</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Ein Tag hat vierundzwanzig Stunden.“<br><span class="text-xs text-slate-500">(Một ngày có hai mươi tư tiếng đồng hồ.)</span></span>
                                        <button onclick="speakGerman('Ein Tag hat vierundzwanzig Stunden.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-rose-600">die (f)</td>
                                <td class="p-3 font-semibold">die Woche</td>
                                <td class="p-3">die Wochen</td>
                                <td class="p-3">tuần</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Eine Woche hat sieben Tage.“<br><span class="text-xs text-slate-500">(Một tuần có bảy ngày.)</span></span>
                                        <button onclick="speakGerman('Eine Woche hat sieben Tage.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-emerald-600">das (n)</td>
                                <td class="p-3 font-semibold">das Wochenende</td>
                                <td class="p-3">die Wochenenden</td>
                                <td class="p-3">cuối tuần</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Am Wochenende arbeite ich nicht.“<br><span class="text-xs text-slate-500">(Vào cuối tuần tôi không làm việc.)</span></span>
                                        <button onclick="speakGerman('Am Wochenende arbeite ich nicht.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-blue-600">der (m)</td>
                                <td class="p-3 font-semibold">der Monat</td>
                                <td class="p-3">die Monate</td>
                                <td class="p-3">tháng</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Ein Monat hat dreißig Tage.“<br><span class="text-xs text-slate-500">(Một tháng có ba mươi ngày.)</span></span>
                                        <button onclick="speakGerman('Ein Monat hat dreißig Tage.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-bold text-emerald-600">das (n)</td>
                                <td class="p-3 font-semibold">das Jahr</td>
                                <td class="p-3">die Jahre</td>
                                <td class="p-3">năm</td>
                                <td class="p-3">
                                    <div class="flex items-center justify-between gap-2">
                                        <span>„Ein Jahr hat zwölf Monate.“<br><span class="text-xs text-slate-500">(Một năm có mười hai tháng.)</span></span>
                                        <button onclick="speakGerman('Ein Jahr hat zwölf Monate.')" class="p-1 rounded bg-slate-100 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="p-3 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-amber-900 space-y-1">
                    <p class="font-bold">⚠️ Phân biệt quan trọng giữa 'die Uhr' và 'die Stunde':</p>
                    <p>• <b>die Uhr:</b> Chỉ <i>mốc thời gian trên mặt đồng hồ</i> (VD: <i>Es ist 8 Uhr = Bây giờ là 8 giờ đúng</i>) hoặc cái đồng hồ đeo tay.</p>
                    <p>• <b>die Stunde:</b> Chỉ <i>thời lượng / khoảng thời gian kéo dài</i> (VD: <i>Der Kurs dauert zwei Stunden = Khóa học kéo dài 2 tiếng</i>).</p>
                </div>
            </div>

            <!-- Bảng 1.2: 7 Thứ trong tuần & 6 Buổi trong ngày -->
            <div class="space-y-3 pt-3 border-t border-slate-100">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>📅</span> 1.2. 7 Thứ Trong Tuần (Wochentage) & 6 Buổi Trong Ngày (Tageszeiten)
                </h5>
                <p class="text-xs text-slate-600">
                    💡 <b>Quy tắc vàng:</b> Cả <b>7 thứ trong tuần</b> và <b>5 buổi trong ngày</b> đều mang giống đực <b>der</b> và khi trả lời <i>"Khi nào? (Wann?)"</i> đều đi với giới từ <b>am</b> (<i>am Montag, am Morgen</i>...). Ngoại lệ duy nhất: <b>die Nacht</b> (ban đêm) mang giống cái nên bắt buộc dùng <b>in der Nacht</b>.
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                    <!-- 7 Thứ -->
                    <div class="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-2">
                        <span class="font-extrabold text-blue-900 block pb-1 border-b border-blue-200">7 Thứ Trong Tuần (am + Wochentag)</span>
                        <ul class="space-y-1.5 text-slate-800">
                            <li class="flex justify-between items-center">
                                <span><b>der Montag</b> → <span class="text-blue-700 font-bold">am Montag</span> (thứ Hai)</span>
                                <button onclick="speakGerman('am Montag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Dienstag</b> → <span class="text-blue-700 font-bold">am Dienstag</span> (thứ Ba)</span>
                                <button onclick="speakGerman('am Dienstag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Mittwoch</b> → <span class="text-blue-700 font-bold">am Mittwoch</span> (thứ Tư)</span>
                                <button onclick="speakGerman('am Mittwoch')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Donnerstag</b> → <span class="text-blue-700 font-bold">am Donnerstag</span> (thứ Năm)</span>
                                <button onclick="speakGerman('am Donnerstag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Freitag</b> → <span class="text-blue-700 font-bold">am Freitag</span> (thứ Sáu)</span>
                                <button onclick="speakGerman('am Freitag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Samstag</b> → <span class="text-blue-700 font-bold">am Samstag</span> (thứ Bảy)</span>
                                <button onclick="speakGerman('am Samstag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Sonntag</b> → <span class="text-blue-700 font-bold">am Sonntag</span> (Chủ nhật)</span>
                                <button onclick="speakGerman('am Sonntag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                        </ul>
                    </div>

                    <!-- 6 Buổi trong ngày -->
                    <div class="p-4 rounded-2xl bg-indigo-50/60 border border-indigo-200 space-y-2">
                        <span class="font-extrabold text-indigo-900 block pb-1 border-b border-indigo-200">6 Buổi Trong Ngày (Tageszeiten)</span>
                        <ul class="space-y-1.5 text-slate-800">
                            <li class="flex justify-between items-center">
                                <span><b>der Morgen</b> (06-10h) → <span class="text-indigo-700 font-bold">am Morgen</span> (sáng sớm)</span>
                                <button onclick="speakGerman('am Morgen')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Vormittag</b> (10-12h) → <span class="text-indigo-700 font-bold">am Vormittag</span> (sáng trước trưa)</span>
                                <button onclick="speakGerman('am Vormittag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Mittag</b> (12-14h) → <span class="text-indigo-700 font-bold">am Mittag</span> (buổi trưa)</span>
                                <button onclick="speakGerman('am Mittag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Nachmittag</b> (14-18h) → <span class="text-indigo-700 font-bold">am Nachmittag</span> (buổi chiều)</span>
                                <button onclick="speakGerman('am Nachmittag')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center">
                                <span><b>der Abend</b> (18-22h) → <span class="text-indigo-700 font-bold">am Abend</span> (buổi tối)</span>
                                <button onclick="speakGerman('am Abend')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                            <li class="flex justify-between items-center bg-rose-50 p-1.5 rounded-lg border border-rose-200 text-rose-900 font-semibold">
                                <span>⚠️ <b>die Nacht</b> (22-06h) → <span class="text-rose-700 font-black">in der Nacht</span> (ban đêm)</span>
                                <button onclick="speakGerman('in der Nacht')" class="p-1 text-xs cursor-pointer">🔊</button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Bảng 1.3: 12 Tháng & 4 Mùa -->
            <div class="space-y-3 pt-3 border-t border-slate-100">
                <h5 class="text-sm font-bold text-slate-800 flex items-center gap-2">
                    <span>🍂</span> 1.3. 12 Tháng Trong Năm (Monate) & 4 Mùa (Jahreszeiten)
                </h5>
                <p class="text-xs text-slate-600">
                    💡 <b>Quy tắc vàng:</b> Tất cả 12 tháng và 4 mùa đều mang giống đực <b>der</b> và đi với giới từ <b>im</b> (<i>im Januar, im Juli, im Sommer...</i>).
                </p>
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2 text-xs">
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Januar</b><br><span class="text-indigo-700 font-bold">im Januar</span> (Th. 1)</div>
                        <button onclick="speakGerman('im Januar')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Februar</b><br><span class="text-indigo-700 font-bold">im Februar</span> (Th. 2)</div>
                        <button onclick="speakGerman('im Februar')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der März</b><br><span class="text-indigo-700 font-bold">im März</span> (Th. 3)</div>
                        <button onclick="speakGerman('im März')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der April</b><br><span class="text-indigo-700 font-bold">im April</span> (Th. 4)</div>
                        <button onclick="speakGerman('im April')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Mai</b><br><span class="text-indigo-700 font-bold">im Mai</span> (Th. 5)</div>
                        <button onclick="speakGerman('im Mai')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Juni</b><br><span class="text-indigo-700 font-bold">im Juni</span> (Th. 6)</div>
                        <button onclick="speakGerman('im Juni')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Juli</b><br><span class="text-indigo-700 font-bold">im Juli</span> (Th. 7)</div>
                        <button onclick="speakGerman('im Juli')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der August</b><br><span class="text-indigo-700 font-bold">im August</span> (Th. 8)</div>
                        <button onclick="speakGerman('im August')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der September</b><br><span class="text-indigo-700 font-bold">im September</span> (Th. 9)</div>
                        <button onclick="speakGerman('im September')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Oktober</b><br><span class="text-indigo-700 font-bold">im Oktober</span> (Th. 10)</div>
                        <button onclick="speakGerman('im Oktober')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der November</b><br><span class="text-indigo-700 font-bold">im November</span> (Th. 11)</div>
                        <button onclick="speakGerman('im November')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex justify-between items-center">
                        <div><b>der Dezember</b><br><span class="text-indigo-700 font-bold">im Dezember</span> (Th. 12)</div>
                        <button onclick="speakGerman('im Dezember')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                </div>

                <!-- 4 Mùa -->
                <div class="p-3 rounded-2xl bg-emerald-50/70 border border-emerald-200 text-xs text-emerald-950 flex flex-wrap items-center justify-between gap-2">
                    <span class="font-bold">🌸 4 Mùa:</span>
                    <span><b>im Frühling</b> (mùa xuân)</span>
                    <span><b>im Sommer</b> (mùa hạ)</span>
                    <span><b>im Herbst</b> (mùa thu)</span>
                    <span><b>im Winter</b> (mùa đông)</span>
                    <button onclick="speakGerman('im Frühling, im Sommer, im Herbst, im Winter')" class="p-1 rounded bg-emerald-100 hover:bg-emerald-200 cursor-pointer">🔊 Nghe 4 mùa</button>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 2: HỆ THỐNG HÓA 2 CÁCH ĐỌC GIỜ -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold text-sm">2</span>
                <h4 class="text-lg font-bold text-slate-900">Hai Cách Đọc Giờ (Die Uhrzeit: Offiziell & Inoffiziell)</h4>
            </div>

            <!-- Câu hỏi giờ -->
            <div class="p-3.5 rounded-2xl bg-indigo-50/60 border border-indigo-200 text-xs sm:text-sm text-slate-800 space-y-1">
                <p class="font-bold text-indigo-900">Mẫu câu hỏi giờ thông dụng:</p>
                <div class="flex flex-wrap gap-4">
                    <div class="flex items-center gap-1.5">
                        <span>• <b>Wie spät ist es?</b> (Mấy giờ rồi?) → <i>Es ist...</i></span>
                        <button onclick="speakGerman('Wie spät ist es?')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <span>• <b>Wie viel Uhr ist es?</b> (Mấy giờ rồi?) → <i>Es ist...</i></span>
                        <button onclick="speakGerman('Wie viel Uhr ist es?')" class="p-1 cursor-pointer">🔊</button>
                    </div>
                </div>
            </div>

            <!-- So sánh 2 cách đọc -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs sm:text-sm">
                <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                    <span class="font-extrabold text-slate-900 block pb-1 border-b border-slate-200">Cách 1: Chính thống (Offiziell - Đài báo, sân bay)</span>
                    <p>• Dùng <b>Hệ 24 giờ</b> (0h → 24h).</p>
                    <p>• Bắt buộc có từ <b>„Uhr“</b> đứng giữa Giờ và Phút.</p>
                    <p class="font-bold text-indigo-700">Công thức: Giờ + Uhr + Phút</p>
                    <p class="italic text-slate-600">Ví dụ: 08:15 → <i>Es ist acht Uhr fünfzehn.</i></p>
                </div>

                <div class="p-4 rounded-2xl bg-amber-50/60 border border-amber-200 space-y-2">
                    <span class="font-extrabold text-amber-950 block pb-1 border-b border-amber-200">Cách 2: Đời thường (Inoffiziell - Giao tiếp hàng ngày)</span>
                    <p>• Dùng <b>Hệ 12 tiếng</b> (20h10 phải đổi thành 8h10 tối).</p>
                    <p>• <b>KHÔNG dùng từ „Uhr“</b> (trừ giờ chẵn như <i>acht Uhr</i>).</p>
                    <p>• <b>nach:</b> Giờ hơn (Phút + nach + Giờ)</p>
                    <p>• <b>vor:</b> Giờ kém (Phút kém + vor + Giờ kế tiếp)</p>
                    <p>• <b>Viertel nach:</b> Hơn 15 phút (Viertel nach + Giờ)</p>
                    <p>• <b>Viertel vor:</b> Kém 15 phút (Viertel vor + Giờ kế tiếp)</p>
                    <p class="font-bold text-amber-900">⚠️ Giờ rưỡi: halb + Giờ kế tiếp (Giờ + 1)</p>
                    <p class="italic text-slate-600">Ví dụ: 08:30 → <i>Es ist halb neun.</i> (Nửa tiếng nữa tới 9h)</p>
                </div>
            </div>

            <!-- Bảng 12 ví dụ chuyển đổi giờ -->
            <div class="space-y-2">
                <span class="text-xs font-bold text-slate-700">Bảng Ví Dụ Chuyển Đổi Giờ Thực Tế:</span>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-2.5">Giờ Số</th>
                                <th class="p-2.5">Chính Thống (Offiziell)</th>
                                <th class="p-2.5">Đời Thường (Inoffiziell)</th>
                                <th class="p-2.5">Giải Thích Quy Tắc</th>
                                <th class="p-2.5">Audio</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">08:15</td>
                                <td class="p-2.5">acht Uhr fünfzehn</td>
                                <td class="p-2.5 font-bold text-indigo-700">Viertel nach acht</td>
                                <td class="p-2.5 text-slate-600">Hơn 15' (1/4 giờ) qua mốc 8h</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist Viertel nach acht.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">09:30</td>
                                <td class="p-2.5">neun Uhr dreißig</td>
                                <td class="p-2.5 font-bold text-amber-700">halb zehn</td>
                                <td class="p-2.5 text-slate-600">Nửa tiếng nữa tới 10h (halb + 10)</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist halb zehn.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">09:05</td>
                                <td class="p-2.5">neun Uhr fünf</td>
                                <td class="p-2.5 font-bold text-indigo-700">fünf nach neun</td>
                                <td class="p-2.5 text-slate-600">9h hơn 5 phút (5 nach 9)</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist fünf nach neun.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">07:50</td>
                                <td class="p-2.5">sieben Uhr fünfzig</td>
                                <td class="p-2.5 font-bold text-rose-700">zehn vor acht</td>
                                <td class="p-2.5 text-slate-600">8h kém 10 phút (10 vor 8)</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist zehn vor acht.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">20:10</td>
                                <td class="p-2.5">zwanzig Uhr zehn</td>
                                <td class="p-2.5 font-bold text-indigo-700">zehn nach acht</td>
                                <td class="p-2.5 text-slate-600">20h10 đổi hệ 12h = 8h hơn 10'</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist zehn nach acht.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">03:15</td>
                                <td class="p-2.5">drei Uhr fünfzehn</td>
                                <td class="p-2.5 font-bold text-indigo-700">Viertel nach drei</td>
                                <td class="p-2.5 text-slate-600">3h hơn 15 phút</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist Viertel nach drei.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">05:45</td>
                                <td class="p-2.5">fünf Uhr fünfundvierzig</td>
                                <td class="p-2.5 font-bold text-rose-700">Viertel vor sechs</td>
                                <td class="p-2.5 text-slate-600">6h kém 15 phút (1/4 giờ)</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist Viertel vor sechs.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">08:30</td>
                                <td class="p-2.5">acht Uhr dreißig</td>
                                <td class="p-2.5 font-bold text-amber-700">halb neun</td>
                                <td class="p-2.5 text-slate-600">8h rưỡi = halb + 9</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist halb neun.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">09:10</td>
                                <td class="p-2.5">neun Uhr zehn</td>
                                <td class="p-2.5 font-bold text-indigo-700">zehn nach neun</td>
                                <td class="p-2.5 text-slate-600">9h hơn 10 phút</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist zehn nach neun.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">02:30</td>
                                <td class="p-2.5">zwei Uhr dreißig</td>
                                <td class="p-2.5 font-bold text-amber-700">halb drei</td>
                                <td class="p-2.5 text-slate-600">2h rưỡi = halb + 3</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist halb drei.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">05:50</td>
                                <td class="p-2.5">fünf Uhr fünfzig</td>
                                <td class="p-2.5 font-bold text-rose-700">zehn vor sechs</td>
                                <td class="p-2.5 text-slate-600">6h kém 10 phút</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist zehn vor sechs.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">06:05</td>
                                <td class="p-2.5">sechs Uhr fünf</td>
                                <td class="p-2.5 font-bold text-indigo-700">fünf nach sechs</td>
                                <td class="p-2.5 text-slate-600">6h hơn 5 phút</td>
                                <td class="p-2.5"><button onclick="speakGerman('Es ist fünf nach sechs.')" class="p-1 cursor-pointer">🔊</button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 3: MA TRẬN GIỚI TỪ THỜI GIAN -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-sm">3</span>
                <h4 class="text-lg font-bold text-slate-900">Ma Trận Giới Từ Chỉ Thời Gian (um, am, im, in der, von...bis)</h4>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                            <th class="p-3">Giới từ</th>
                            <th class="p-3">Đi cùng thành phần nào?</th>
                            <th class="p-3">Câu hỏi</th>
                            <th class="p-3">Ví Dụ Tiếng Đức (Audio)</th>
                            <th class="p-3">Dịch Nghĩa Tiếng Việt</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-800">
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-extrabold text-blue-700 text-base">um</td>
                            <td class="p-3 font-semibold">Giờ giấc cụ thể (Uhrzeit)</td>
                            <td class="p-3 text-slate-500">Um wie viel Uhr? / Wann?</td>
                            <td class="p-3">
                                <div class="flex items-center justify-between gap-2">
                                    <span>„Ich stehe <b>um</b> 8 Uhr auf.“</span>
                                    <button onclick="speakGerman('Ich stehe um acht Uhr auf.')" class="p-1 cursor-pointer">🔊</button>
                                </div>
                            </td>
                            <td class="p-3 text-slate-600">Tôi thức dậy <b>vào lúc</b> 8 giờ.</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-extrabold text-indigo-700 text-base">am<br><span class="text-[10px] text-slate-400 font-normal">(an + dem)</span></td>
                            <td class="p-3 font-semibold">• Thứ trong tuần (Montag - Sonntag)<br>• Buổi trong ngày (Morgen, Abend...)<br>• Cuối tuần (am Wochenende)</td>
                            <td class="p-3 text-slate-500">Wann? / An welchem Tag?</td>
                            <td class="p-3">
                                <div class="flex items-center justify-between gap-2">
                                    <span>„<b>Am</b> Sonntag stehe ich spät auf.“</span>
                                    <button onclick="speakGerman('Am Sonntag stehe ich spät auf.')" class="p-1 cursor-pointer">🔊</button>
                                </div>
                            </td>
                            <td class="p-3 text-slate-600"><b>Vào</b> Chủ nhật tôi dậy muộn.</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-extrabold text-emerald-700 text-base">im<br><span class="text-[10px] text-slate-400 font-normal">(in + dem)</span></td>
                            <td class="p-3 font-semibold">• 12 Tháng trong năm (Januar - Dezember)<br>• 4 Mùa (Frühling, Sommer, Herbst, Winter)</td>
                            <td class="p-3 text-slate-500">Wann? / In welchem Monat?</td>
                            <td class="p-3">
                                <div class="flex items-center justify-between gap-2">
                                    <span>„<b>Im</b> Juni fahren wir nach Berlin.“</span>
                                    <button onclick="speakGerman('Im Juni fahren wir nach Berlin.')" class="p-1 cursor-pointer">🔊</button>
                                </div>
                            </td>
                            <td class="p-3 text-slate-600"><b>Vào</b> tháng Sáu chúng tôi đi tới Berlin.</td>
                        </tr>
                        <tr class="hover:bg-slate-50 bg-rose-50/40">
                            <td class="p-3 font-extrabold text-rose-700 text-base">in der<br><span class="text-[10px] text-rose-500 font-normal">(Ngoại lệ!)</span></td>
                            <td class="p-3 font-semibold">Ban đêm (die Nacht mang giống cái)</td>
                            <td class="p-3 text-slate-500">Wann?</td>
                            <td class="p-3">
                                <div class="flex items-center justify-between gap-2">
                                    <span>„<b>In der</b> Nacht schlafe ich.“</span>
                                    <button onclick="speakGerman('In der Nacht schlafe ich.')" class="p-1 cursor-pointer">🔊</button>
                                </div>
                            </td>
                            <td class="p-3 text-slate-600"><b>Vào</b> ban đêm tôi ngủ.</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-extrabold text-purple-700 text-base">von...bis</td>
                            <td class="p-3 font-semibold">Khoảng thời gian (từ... đến...)</td>
                            <td class="p-3 text-slate-500">Von wann bis wann?</td>
                            <td class="p-3">
                                <div class="flex items-center justify-between gap-2">
                                    <span>„<b>Von</b> 8 <b>bis</b> 12 Uhr arbeite ich.“</span>
                                    <button onclick="speakGerman('Von acht bis zwölf Uhr arbeite ich.')" class="p-1 cursor-pointer">🔊</button>
                                </div>
                            </td>
                            <td class="p-3 text-slate-600"><b>Từ</b> 8 <b>đến</b> 12 giờ tôi làm việc.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- HỌC PHẦN 4: ĐỘNG TỪ TÁCH TRONG TIẾNG ĐỨC -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-5">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center font-bold text-sm">4</span>
                <h4 class="text-lg font-bold text-slate-900">Động Từ Tách (Trennbare Verben) & Khung Câu (Satzklammer)</h4>
            </div>

            <!-- Cấu tạo -->
            <div class="p-4 rounded-2xl bg-purple-50/60 border border-purple-200 text-xs sm:text-sm text-slate-800 space-y-2">
                <p class="font-bold text-purple-900">Cấu tạo của Động từ tách:</p>
                <p>Động từ tách gồm 2 phần: <b>Tiền tố tách (Präfix)</b> + <b>Động từ gốc (Verbstamm)</b>.</p>
                <p>• <b>machen</b> (làm) → <b>auf</b>machen (mở), <b>zu</b>machen (đóng), <b>an</b>machen (bật), <b>aus</b>machen (tắt).</p>
                <p>• Các tiền tố tách thông dụng: <i>auf-, aus-, an-, ein-, mit-, zu-, vor-, fern-, ab-, zurück-</i>.</p>
            </div>

            <!-- Quy tắc khung câu -->
            <div class="space-y-2">
                <span class="text-xs font-bold text-slate-800">Quy tắc Khung Câu (Satzklammer) trong câu đơn ở thì Hiện tại:</span>
                <p class="text-xs text-slate-600">
                    • <b>Động từ gốc:</b> Đứng ở <b>vị trí số 2 (V2)</b> trong câu trần thuật hoặc câu hỏi W-Frage (đứng vị trí số 1 trong Ja/Nein-Frage) và <b>chia theo ngôi của chủ ngữ</b>.<br>
                    • <b>Tiền tố tách:</b> Tách rời ra và <b>đẩy xuống đứng ở CUỐI CÙNG CỦA CÂU</b>.
                </p>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs sm:text-sm border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-3">Loại câu</th>
                                <th class="p-3">Vị trí 1</th>
                                <th class="p-3 text-center bg-indigo-50 text-indigo-900">Vị trí 2 (Động từ gốc chia theo ngôi)</th>
                                <th class="p-3">Thành phần giữa câu</th>
                                <th class="p-3 text-center bg-rose-50 text-rose-900">Cuối câu (Tiền tố tách)</th>
                                <th class="p-3">Dịch nghĩa</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-semibold">Trần thuật (Chủ ngữ đầu)</td>
                                <td class="p-3 font-bold">Ich</td>
                                <td class="p-3 text-center font-black text-indigo-700 bg-indigo-50/50">mache</td>
                                <td class="p-3">die Tür</td>
                                <td class="p-3 text-center font-black text-rose-700 bg-rose-50/50">auf.</td>
                                <td class="p-3 text-slate-600">Tôi mở cánh cửa ra.</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-semibold">Trần thuật (Đảo ngữ)</td>
                                <td class="p-3 font-bold">Am Sonntag</td>
                                <td class="p-3 text-center font-black text-indigo-700 bg-indigo-50/50">stehe</td>
                                <td class="p-3">ich um 8 Uhr</td>
                                <td class="p-3 text-center font-black text-rose-700 bg-rose-50/50">auf.</td>
                                <td class="p-3 text-slate-600">Vào Chủ nhật tôi thức dậy lúc 8 giờ.</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-semibold">Câu hỏi W-Frage</td>
                                <td class="p-3 font-bold">Wann</td>
                                <td class="p-3 text-center font-black text-indigo-700 bg-indigo-50/50">stehst</td>
                                <td class="p-3">du am Sonntag</td>
                                <td class="p-3 text-center font-black text-rose-700 bg-rose-50/50">auf?</td>
                                <td class="p-3 text-slate-600">Khi nào bạn thức dậy vào Chủ nhật?</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-semibold">Câu hỏi W-Frage</td>
                                <td class="p-3 font-bold">Wann</td>
                                <td class="p-3 text-center font-black text-indigo-700 bg-indigo-50/50">gehst</td>
                                <td class="p-3">du am Freitag</td>
                                <td class="p-3 text-center font-black text-rose-700 bg-rose-50/50">aus?</td>
                                <td class="p-3 text-slate-600">Khi nào bạn đi chơi vào thứ Sáu?</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-3 font-semibold">Câu hỏi Ja/Nein</td>
                                <td class="p-3 text-slate-400 italic">(Đảo V2 lên 1)</td>
                                <td class="p-3 text-center font-black text-indigo-700 bg-indigo-50/50">Machst</td>
                                <td class="p-3">du bitte das Fenster</td>
                                <td class="p-3 text-center font-black text-rose-700 bg-rose-50/50">zu?</td>
                                <td class="p-3 text-slate-600">Bạn làm ơn đóng cửa sổ lại nhé?</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bảng chia 6 động từ tách tiêu biểu -->
            <div class="space-y-2">
                <span class="text-xs font-bold text-slate-800">Bảng Chia Động Từ Tách Theo Ngôi:</span>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                                <th class="p-2.5">Ngôi</th>
                                <th class="p-2.5">aufmachen (mở)</th>
                                <th class="p-2.5">aufstehen (dậy)</th>
                                <th class="p-2.5">ausgehen (đi chơi)</th>
                                <th class="p-2.5">einkaufen (mua sắm)</th>
                                <th class="p-2.5">anrufen (gọi điện)</th>
                                <th class="p-2.5">fernsehen (xem tivi - biến âm e→ie)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-800">
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">ich</td>
                                <td class="p-2.5">mache ... auf</td>
                                <td class="p-2.5">stehe ... auf</td>
                                <td class="p-2.5">gehe ... aus</td>
                                <td class="p-2.5">kaufe ... ein</td>
                                <td class="p-2.5">rufe ... an</td>
                                <td class="p-2.5">sehe ... fern</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">du</td>
                                <td class="p-2.5">machst ... auf</td>
                                <td class="p-2.5">stehst ... auf</td>
                                <td class="p-2.5">gehst ... aus</td>
                                <td class="p-2.5">kaufst ... ein</td>
                                <td class="p-2.5">rufst ... an</td>
                                <td class="p-2.5 font-bold text-amber-700">siehst ... fern</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">er/sie/es</td>
                                <td class="p-2.5">macht ... auf</td>
                                <td class="p-2.5">steht ... auf</td>
                                <td class="p-2.5">geht ... aus</td>
                                <td class="p-2.5">kauft ... ein</td>
                                <td class="p-2.5">ruft ... an</td>
                                <td class="p-2.5 font-bold text-amber-700">sieht ... fern</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">wir</td>
                                <td class="p-2.5">machen ... auf</td>
                                <td class="p-2.5">stehen ... auf</td>
                                <td class="p-2.5">gehen ... aus</td>
                                <td class="p-2.5">kaufen ... ein</td>
                                <td class="p-2.5">rufen ... an</td>
                                <td class="p-2.5">sehen ... fern</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">ihr</td>
                                <td class="p-2.5">macht ... auf</td>
                                <td class="p-2.5">steht ... auf</td>
                                <td class="p-2.5">geht ... aus</td>
                                <td class="p-2.5">kauft ... ein</td>
                                <td class="p-2.5">ruft ... an</td>
                                <td class="p-2.5">seht ... fern</td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="p-2.5 font-bold">sie/Sie</td>
                                <td class="p-2.5">machen ... auf</td>
                                <td class="p-2.5">stehen ... auf</td>
                                <td class="p-2.5">gehen ... aus</td>
                                <td class="p-2.5">kaufen ... ein</td>
                                <td class="p-2.5">rufen ... an</td>
                                <td class="p-2.5">sehen ... fern</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 5: DIỄN BIẾN TRONG NGÀY & ĐẢO NGỮ V2 -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-4">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-sm">5</span>
                <h4 class="text-lg font-bold text-slate-900">Diễn Biến Trong Ngày (Tagesabläufe) & Đảo Ngữ Vị Trí Số 2 (Inversion)</h4>
            </div>

            <p class="text-xs sm:text-sm text-slate-600">
                Khi trạng ngữ chỉ thời gian (<i>Am Sonntag, Um 9 Uhr, Von 8 bis 12 Uhr</i>) đứng ở <b>vị trí số 1</b> để nhấn mạnh, thì <b>động từ chia theo ngôi bắt buộc vẫn đứng ở vị trí số 2</b>, và <b>chủ ngữ (ich, du, wir...) lùi sang vị trí số 3</b>.
            </p>

            <div class="space-y-3">
                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">1. Wann stehst du am Sonntag auf?</span> (Bạn thức dậy lúc nào vào Chủ nhật?)<br>
                        <span class="font-semibold text-slate-800">→ Am Sonntag stehe ich um 8 Uhr auf.</span> (Vào Chủ nhật tôi thức dậy lúc 8 giờ.)
                    </div>
                    <button onclick="speakGerman('Am Sonntag stehe ich um acht Uhr auf.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>

                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">2. Um wie viel Uhr frühstückst du?</span> (Bạn ăn sáng vào lúc mấy giờ?)<br>
                        <span class="font-semibold text-slate-800">→ Um 9 Uhr frühstücke ich.</span> (Vào lúc 9 giờ tôi ăn sáng.)
                    </div>
                    <button onclick="speakGerman('Um neun Uhr frühstücke ich.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>

                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">3. Wann machst du Mittagspause?</span> (Khi nào bạn nghỉ trưa?)<br>
                        <span class="font-semibold text-slate-800">→ Um 12 Uhr mache ich Mittagspause.</span> (Vào lúc 12 giờ tôi nghỉ trưa.)
                    </div>
                    <button onclick="speakGerman('Um zwölf Uhr mache ich Mittagspause.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>

                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">4. Von wann bis wann arbeitest du?</span> (Bạn làm việc từ mấy giờ đến mấy giờ?)<br>
                        <span class="font-semibold text-slate-800">→ Von 8 bis 12 Uhr arbeite ich.</span> (Từ 8 giờ đến 12 giờ tôi làm việc.)
                    </div>
                    <button onclick="speakGerman('Von acht bis zwölf Uhr arbeite ich.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>

                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">5. Wann gehst du am Freitag aus?</span> (Khi nào bạn đi chơi vào thứ Sáu?)<br>
                        <span class="font-semibold text-slate-800">→ Am Freitag um 20 Uhr gehe ich aus.</span> (Vào thứ Sáu lúc 20 giờ tôi đi chơi.)
                    </div>
                    <button onclick="speakGerman('Am Freitag um zwanzig Uhr gehe ich aus.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>

                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">6. Wann machst du Sport?</span> (Khi nào bạn tập thể thao?)<br>
                        <span class="font-semibold text-slate-800">→ Um 17 Uhr mache ich Sport.</span> (Vào lúc 17 giờ tôi tập thể thao.)
                    </div>
                    <button onclick="speakGerman('Um siebzehn Uhr mache ich Sport.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>

                <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs sm:text-sm">
                    <div>
                        <span class="font-bold text-indigo-700">7. Wann gehst du ins Bett?</span> (Khi nào bạn đi ngủ?)<br>
                        <span class="font-semibold text-slate-800">→ Um 22 Uhr gehe ich ins Bett.</span> (Vào lúc 22 giờ tôi đi ngủ.)
                    </div>
                    <button onclick="speakGerman('Um zweiundzwanzig Uhr gehe ich ins Bett.')" class="self-start sm:self-center p-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-700 text-xs cursor-pointer">🔊 Nghe</button>
                </div>
            </div>
        </div>

        <!-- HỌC PHẦN 6: ĐỘNG TỪ "HABEN" Ở THÌ QUÁ KHỨ ĐƠN & ĐỐI CHIẾU VỚI "SEIN" -->
        <div class="p-6 rounded-3xl bg-white border border-slate-200 shadow-sm space-y-6">
            <div class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-xl bg-rose-100 text-rose-700 flex items-center justify-center font-bold text-sm">6</span>
                <h4 class="text-lg font-bold text-slate-900">Động Từ "haben" ở Thì Quá Khứ Đơn (Präteritum) & Đối Chiếu Với "sein"</h4>
            </div>

            <p class="text-xs sm:text-sm text-slate-600">
                Ở Bài 3, bạn đã học quá khứ đơn của <b>sein</b> (<i>war / warst / waren / wart</i>). Sang Bài 5, chúng ta hoàn thiện động từ nền tảng thứ hai: quá khứ đơn của <b>haben</b> (<i>hatte, hattest, hatten, hattet</i>). Khi giao tiếp về quá khứ, người Đức luôn ưu tiên dùng thì <b>Präteritum</b> cho 2 động từ này vì sự ngắn gọn và tự nhiên.
            </p>

            <!-- Bảng chia đối chiếu sein vs haben -->
            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs sm:text-sm border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
                            <th class="p-3">Ngôi (Pronomen)</th>
                            <th class="p-3">Nghĩa tiếng Việt</th>
                            <th class="p-3">sein ở Hiện tại (Präsens)</th>
                            <th class="p-3 text-indigo-900 bg-indigo-50">sein ở Quá khứ (Präteritum: đã thì/là/ở)</th>
                            <th class="p-3">haben ở Hiện tại (Präsens)</th>
                            <th class="p-3 text-amber-900 bg-amber-50">haben ở Quá khứ (Präteritum: đã có)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-800">
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold">ich</td>
                            <td class="p-3 text-slate-500">tôi</td>
                            <td class="p-3">bin</td>
                            <td class="p-3 font-black text-indigo-700 bg-indigo-50/50">war</td>
                            <td class="p-3">habe</td>
                            <td class="p-3 font-black text-amber-700 bg-amber-50/50">hatte</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold">du</td>
                            <td class="p-3 text-slate-500">bạn</td>
                            <td class="p-3">bist</td>
                            <td class="p-3 font-black text-indigo-700 bg-indigo-50/50">warst</td>
                            <td class="p-3">hast</td>
                            <td class="p-3 font-black text-amber-700 bg-amber-50/50">hattest</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold">er/sie/es</td>
                            <td class="p-3 text-slate-500">anh ấy/cô ấy/nó</td>
                            <td class="p-3">ist</td>
                            <td class="p-3 font-black text-indigo-700 bg-indigo-50/50">war</td>
                            <td class="p-3">hat</td>
                            <td class="p-3 font-black text-amber-700 bg-amber-50/50">hatte</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold">wir</td>
                            <td class="p-3 text-slate-500">chúng tôi</td>
                            <td class="p-3">sind</td>
                            <td class="p-3 font-black text-indigo-700 bg-indigo-50/50">waren</td>
                            <td class="p-3">haben</td>
                            <td class="p-3 font-black text-amber-700 bg-amber-50/50">hatten</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold">ihr</td>
                            <td class="p-3 text-slate-500">các bạn</td>
                            <td class="p-3">seid</td>
                            <td class="p-3 font-black text-indigo-700 bg-indigo-50/50">wart</td>
                            <td class="p-3">habt</td>
                            <td class="p-3 font-black text-amber-700 bg-amber-50/50">hattet</td>
                        </tr>
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold">sie/Sie</td>
                            <td class="p-3 text-slate-500">họ / Ngài</td>
                            <td class="p-3">sind</td>
                            <td class="p-3 font-black text-indigo-700 bg-indigo-50/50">waren</td>
                            <td class="p-3">haben</td>
                            <td class="p-3 font-black text-amber-700 bg-amber-50/50">hatten</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="p-3 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-amber-900 space-y-1">
                <p class="font-bold">💡 Mẹo nhớ quan trọng của thì Präteritum:</p>
                <p>• Ngôi <b>ich</b> và ngôi <b>er/sie/es</b> luôn chia <b>giống hệt nhau</b>: <i>ich hatte = er hatte</i>; <i>ich war = er war</i>.</p>
                <p>• Ngôi <b>wir</b> và ngôi <b>sie/Sie</b> luôn chia <b>giống hệt nhau</b>: <i>wir hatten = sie hatten</i>; <i>wir waren = sie waren</i>.</p>
            </div>

            <!-- 4 Câu đối chiếu Gestern vs. Heute -->
            <div class="space-y-2 pt-2">
                <span class="text-xs font-bold text-slate-800">4 Mẫu Câu Đối Chiếu Quá Khứ (Gestern) vs. Hiện Tại (Heute):</span>
                <div class="space-y-2">
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs sm:text-sm flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <b>Gestern hatte ich keine Zeit,</b> aber heute habe ich viel Zeit.<br>
                            <span class="text-slate-500 text-xs">(Hôm qua tôi đã không có thời gian, nhưng hôm nay tôi có nhiều thời gian.)</span>
                        </div>
                        <button onclick="speakGerman('Gestern hatte ich keine Zeit, aber heute habe ich viel Zeit.')" class="self-start sm:self-center p-1 rounded bg-slate-200 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs sm:text-sm flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <b>Gestern hatten wir eine Panne,</b> aber heute haben wir keine Panne.<br>
                            <span class="text-slate-500 text-xs">(Hôm qua chúng tôi đã gặp một sự cố hỏng xe, nhưng hôm nay chúng tôi không gặp sự cố nào.)</span>
                        </div>
                        <button onclick="speakGerman('Gestern hatten wir eine Panne, aber heute haben wir keine Panne.')" class="self-start sm:self-center p-1 rounded bg-slate-200 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs sm:text-sm flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <b>Gestern hattest du kein Glück,</b> aber heute hast du viel Glück.<br>
                            <span class="text-slate-500 text-xs">(Hôm qua bạn đã không gặp may, nhưng hôm nay bạn có nhiều may mắn.)</span>
                        </div>
                        <button onclick="speakGerman('Gestern hattest du kein Glück, aber heute hast du viel Glück.')" class="self-start sm:self-center p-1 rounded bg-slate-200 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                    </div>
                    <div class="p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs sm:text-sm flex flex-col sm:flex-row sm:items-center justify-between gap-2">
                        <div>
                            <b>Gestern hatte er kein Geld,</b> aber heute hat er viel Geld.<br>
                            <span class="text-slate-500 text-xs">(Hôm qua anh ấy đã không có tiền, nhưng hôm nay anh ấy có nhiều tiền.)</span>
                        </div>
                        <button onclick="speakGerman('Gestern hatte er kein Geld, aber heute hat er viel Geld.')" class="self-start sm:self-center p-1 rounded bg-slate-200 hover:bg-indigo-100 text-xs cursor-pointer">🔊</button>
                    </div>
                </div>
            </div>

            <!-- Bức thư của Maria gửi Thomas -->
            <div class="p-5 rounded-3xl bg-indigo-50/70 border border-indigo-200 space-y-4">
                <div class="flex items-center justify-between flex-wrap gap-2">
                    <span class="font-extrabold text-indigo-950 text-sm sm:text-base">✉️ Bức Thư Của Maria Gửi Thomas (Phân Tích 7 Vị Trí Präteritum)</span>
                    <button onclick="speakGerman('Lieber Thomas, Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine Panne. Ich hatte kein Handy und kein Geld für den Bus. Und ein Rad hatten Joan und ich auch nicht. Joan hatte ein Handy, aber sie hatte deine Nummer nicht. Hattet ihr eine tolle Party? Liebe Grüße, Maria')" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs shadow-xs cursor-pointer">
                        🔊 Nghe toàn bộ bức thư (de-DE)
                    </button>
                </div>

                <div class="p-4 rounded-2xl bg-white border border-indigo-100 text-xs sm:text-sm text-slate-800 space-y-2 font-mono">
                    <p class="font-bold">Lieber Thomas,</p>
                    <p>Entschuldigung, wir <span class="bg-indigo-100 px-1.5 py-0.5 rounded font-black text-indigo-800">waren</span> (1) gestern Abend nicht bei der Party. Wir <span class="bg-amber-100 px-1.5 py-0.5 rounded font-black text-amber-800">hatten</span> (2) eine Panne. Ich <span class="bg-amber-100 px-1.5 py-0.5 rounded font-black text-amber-800">hatte</span> (3) kein Handy und kein Geld für den Bus. Und ein Rad <span class="bg-amber-100 px-1.5 py-0.5 rounded font-black text-amber-800">hatten</span> (4) Joan und ich auch nicht. Joan <span class="bg-amber-100 px-1.5 py-0.5 rounded font-black text-amber-800">hatte</span> (5) ein Handy, aber sie <span class="bg-amber-100 px-1.5 py-0.5 rounded font-black text-amber-800">hatte</span> (6) deine Nummer nicht. <span class="bg-amber-100 px-1.5 py-0.5 rounded font-black text-amber-800">Hattet</span> (7) ihr eine tolle Party?</p>
                    <p class="font-bold">Liebe Grüße<br>Maria</p>
                </div>

                <div class="p-4 rounded-2xl bg-white border border-indigo-100 text-xs space-y-2">
                    <span class="font-bold text-slate-900 block">📖 Dịch nghĩa toàn văn bức thư:</span>
                    <p class="text-slate-600 italic">
                        „Thomas thân mến, xin lỗi nhé, tối hôm qua chúng mình đã không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe. Mình đã không có điện thoại di động và cũng không có tiền đi xe buýt. Và một chiếc xe đạp thì Joan và mình cũng đã không có. Joan đã có một chiếc điện thoại di động, nhưng cô ấy lại không có số của bạn. Các bạn đã có một bữa tiệc tuyệt vời chứ? Thân mến, Maria“
                    </p>
                </div>

                <div class="space-y-1.5 text-xs text-slate-700">
                    <span class="font-bold text-slate-900 block">💡 Giải thích ngữ pháp 7 vị trí chia động từ:</span>
                    <p>1. <b>waren:</b> Chủ ngữ <i>wir</i>, chỉ trạng thái ở địa điểm tại bữa tiệc tối qua → dùng <i>sein</i> ở Präteritum là <i>waren</i>.</p>
                    <p>2. <b>hatten:</b> Chủ ngữ <i>wir</i>, đi với cụm danh từ <i>eine Panne</i> (gặp sự cố) → dùng <i>haben</i> ở Präteritum là <i>hatten</i>.</p>
                    <p>3. <b>hatte:</b> Chủ ngữ <i>Ich</i> → <i>hatte</i> (không có điện thoại, không có tiền).</p>
                    <p>4. <b>hatten:</b> Chủ ngữ là <i>Joan und ich</i> (= ngôi <i>wir</i>), tân ngữ <i>ein Rad</i> đảo lên đầu câu, động từ ở vị trí 2 chia theo <i>wir</i> là <i>hatten</i>.</p>
                    <p>5. <b>hatte:</b> Chủ ngữ <i>Joan</i> (= ngôi thứ 3 số ít <i>sie/cô ấy</i>) → <i>hatte</i>.</p>
                    <p>6. <b>hatte:</b> Chủ ngữ <i>sie</i> (cô ấy) → <i>hatte</i> (không có số điện thoại của bạn).</p>
                    <p>7. <b>Hattet:</b> Câu hỏi Ja/Nein đảo động từ lên đầu câu cho chủ ngữ <i>ihr</i> (các bạn) → <i>Hattet ihr eine tolle Party?</i></p>
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
    # DANH SÁCH 38 TỪ VỰNG CHUẨN A1 BÀI 5 (100% CÓ MẠO TỪ, SỐ NHIỀU, DỊCH NGHĨA & VÍ DỤ KHỚP)
    # =========================================================================
    vocabularies = [
        # --- 1. ĐƠN VỊ THỜI GIAN (8 từ) ---
        (lesson_id, "Sekunde", "die", "giây (Pl: die Sekunden)", "Eine Minute hat sechzig Sekunden. (Một phút có sáu mươi giây.)"),
        (lesson_id, "Minute", "die", "phút (Pl: die Minuten)", "Der Bus kommt in fünf Minuten. (Xe buýt sẽ đến trong năm phút nữa.)"),
        (lesson_id, "Stunde", "die", "giờ, tiếng đồng hồ (thời lượng; Pl: die Stunden)", "Heute arbeite ich acht Stunden. (Hôm nay tôi làm việc tám tiếng đồng hồ.)"),
        (lesson_id, "Tag", "der", "ngày (Pl: die Tage)", "Ein Tag hat vierundzwanzig Stunden. (Một ngày có hai mươi tư tiếng đồng hồ.)"),
        (lesson_id, "Woche", "die", "tuần (Pl: die Wochen)", "Eine Woche hat sieben Tage. (Một tuần có bảy ngày.)"),
        (lesson_id, "Wochenende", "das", "cuối tuần (Pl: die Wochenenden)", "Am Wochenende arbeite ich nicht. (Vào cuối tuần tôi không làm việc.)"),
        (lesson_id, "Monat", "der", "tháng (Pl: die Monate)", "Ein Monat hat dreißig oder einunddreißig Tage. (Một tháng có ba mươi hoặc ba mươi mốt ngày.)"),
        (lesson_id, "Jahr", "das", "năm (Pl: die Jahre)", "Ein Jahr hat zwölf Monate. (Một năm có mười hai tháng.)"),

        # --- 2. ĐỒNG HỒ & MỐC GIỜ (1 từ) ---
        (lesson_id, "Uhr", "die", "đồng hồ, giờ mốc (Pl: die Uhren)", "Es ist acht Uhr. (Bây giờ là tám giờ đúng.)"),

        # --- 3. 7 THỨ TRONG TUẦN (7 từ) ---
        (lesson_id, "Montag", "der", "thứ Hai (Pl: die Montage)", "Am Montag beginnt meine Arbeitswoche. (Vào thứ Hai tuần làm việc của tôi bắt đầu.)"),
        (lesson_id, "Dienstag", "der", "thứ Ba (Pl: die Dienstage)", "Am Dienstag habe ich einen Deutschkurs. (Vào thứ Ba tôi có một khóa học tiếng Đức.)"),
        (lesson_id, "Mittwoch", "der", "thứ Tư (Pl: die Mittwoche)", "Am Mittwoch mache ich um 17 Uhr Sport. (Vào thứ Tư tôi tập thể thao lúc 17 giờ.)"),
        (lesson_id, "Donnerstag", "der", "thứ Năm (Pl: die Donnerstage)", "Am Donnerstag kauft Anna im Supermarkt ein. (Vào thứ Năm Anna đi mua sắm ở siêu thị.)"),
        (lesson_id, "Freitag", "der", "thứ Sáu (Pl: die Freitage)", "Am Freitag um 20 Uhr gehe ich aus. (Vào thứ Sáu lúc 20 giờ tôi đi chơi.)"),
        (lesson_id, "Samstag", "der", "thứ Bảy (Pl: die Samstage)", "Am Samstag treffen wir unsere Freunde. (Vào thứ Bảy chúng tôi gặp gỡ bạn bè của mình.)"),
        (lesson_id, "Sonntag", "der", "Chủ nhật (Pl: die Sonntage)", "Am Sonntag stehe ich um 8 Uhr auf. (Vào Chủ nhật tôi thức dậy lúc 8 giờ.)"),

        # --- 4. 6 BUỔI TRONG NGÀY (6 từ) ---
        (lesson_id, "Morgen", "der", "buổi sáng sớm (06:00 - 10:00; Pl: die Morgen)", "Am Morgen trinke ich gern eine Tasse Kaffee. (Vào buổi sáng tôi thích uống một tách cà phê.)"),
        (lesson_id, "Vormittag", "der", "buổi sáng trước trưa (10:00 - 12:00; Pl: die Vormittage)", "Am Vormittag arbeite ich im Büro. (Vào buổi sáng trước trưa tôi làm việc ở văn phòng.)"),
        (lesson_id, "Mittag", "der", "buổi trưa (12:00 - 14:00; Pl: die Mittage)", "Am Mittag mache ich um 12 Uhr Mittagspause. (Vào buổi trưa tôi nghỉ trưa lúc 12 giờ.)"),
        (lesson_id, "Nachmittag", "der", "buổi chiều (14:00 - 18:00; Pl: die Nachmittage)", "Am Nachmittag trinken wir Tee und lesen ein Buch. (Vào buổi chiều chúng tôi uống trà và đọc một quyển sách.)"),
        (lesson_id, "Abend", "der", "buổi tối (18:00 - 22:00; Pl: die Abende)", "Am Abend sehe ich mit meiner Familie fern. (Vào buổi tối tôi xem tivi cùng gia đình mình.)"),
        (lesson_id, "Nacht", "die", "ban đêm (22:00 - 06:00; Pl: die Nächte)", "In der Nacht schlafe ich acht Stunden. (Vào ban đêm tôi ngủ tám tiếng đồng hồ.)"),

        # --- 5. 12 THÁNG TRONG NĂM (12 từ) ---
        (lesson_id, "Januar", "der", "tháng Một (Pl: kein Plural; ghi chú: Plural selten)", "Im Januar ist es in Deutschland sehr kalt. (Vào tháng Một trời ở Đức rất lạnh.)"),
        (lesson_id, "Februar", "der", "tháng Hai (Pl: kein Plural; ghi chú: Plural selten)", "Im Februar hat der Monat nur 28 oder 29 Tage. (Vào tháng Hai tháng chỉ có 28 hoặc 29 ngày.)"),
        (lesson_id, "März", "der", "tháng Ba (Pl: kein Plural; ghi chú: Plural selten)", "Im März beginnt der Frühling. (Vào tháng Ba mùa xuân bắt đầu.)"),
        (lesson_id, "April", "der", "tháng Tư (Pl: kein Plural; ghi chú: Plural selten)", "Mein Bruder hat im April Geburtstag. (Anh trai tôi có sinh nhật vào tháng Tư.)"),
        (lesson_id, "Mai", "der", "tháng Năm (Pl: kein Plural; ghi chú: Plural selten)", "Im Mai ist das Wetter in Berlin sehr schön. (Vào tháng Năm thời tiết ở Berlin rất đẹp.)"),
        (lesson_id, "Juni", "der", "tháng Sáu (Pl: kein Plural; ghi chú: Plural selten)", "Im Juni fahren wir nach Italien. (Vào tháng Sáu chúng tôi đi sang Ý.)"),
        (lesson_id, "Juli", "der", "tháng Bảy (Pl: kein Plural; ghi chú: Plural selten)", "Im Juli haben die Studenten Sommerferien. (Vào tháng Bảy các sinh viên có kỳ nghỉ hè.)"),
        (lesson_id, "August", "der", "tháng Tám (Pl: kein Plural; ghi chú: Plural selten)", "Im August ist es in Vietnam oft heiß. (Vào tháng Tám trời ở Việt Nam thường nóng.)"),
        (lesson_id, "September", "der", "tháng Chín (Pl: kein Plural; ghi chú: Plural selten)", "Im September beginnt mein Studium. (Vào tháng Chín việc học đại học của tôi bắt đầu.)"),
        (lesson_id, "Oktober", "der", "tháng Mười (Pl: kein Plural; ghi chú: Plural selten)", "Im Oktober ist der Herbst sehr schön. (Vào tháng Mười mùa thu rất đẹp.)"),
        (lesson_id, "November", "der", "tháng Mười Một (Pl: kein Plural; ghi chú: Plural selten)", "Im November arbeite ich viel. (Vào tháng Mười Một tôi làm việc nhiều.)"),
        (lesson_id, "Dezember", "der", "tháng Mười Hai (Pl: kein Plural; ghi chú: Plural selten)", "Im Dezember ist Weihnachten. (Vào tháng Mười Hai là lễ Giáng sinh.)"),

        # --- 6. TỪ VỰNG LỊCH TRÌNH & SỰ CỐ (4 từ) ---
        (lesson_id, "Termin", "der", "cuộc hẹn, lịch hẹn (Pl: die Termine)", "Ich habe einen Termin um zehn Uhr. (Tôi có một cuộc hẹn vào lúc 10 giờ.)"),
        (lesson_id, "Mittagspause", "die", "giờ nghỉ trưa (Pl: die Mittagspausen)", "Um zwölf Uhr mache ich Mittagspause. (Vào lúc 12 giờ tôi nghỉ trưa.)"),
        (lesson_id, "Panne", "die", "sự cố hỏng xe dọc đường (Pl: die Pannen)", "Wir hatten gestern eine Panne. (Hôm qua chúng tôi đã gặp một sự cố hỏng xe.)"),
        (lesson_id, "Zeit", "die", "thời gian (Pl: die Zeiten)", "Gestern hatte ich keine Zeit. (Hôm qua tôi đã không có thời gian.)")
    ]

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # TỪ ĐIỂN DỊCH NGHĨA TIẾNG VIỆT CHUẨN 100% CHO 50 BÀI TẬP BÀI 5
    # =========================================================================
    EXERCISE_TRANSLATIONS = {
        1: "Vào Chủ nhật anh ấy thức dậy vào lúc 8 giờ.",
        2: "2 giờ 30 phút (2 giờ rưỡi) đọc là 'halb drei'.",
        3: "5 giờ 50 phút (6 giờ kém 10 phút) đọc là 'zehn vor sechs'.",
        4: "Trời nóng quá. Chúng tôi mở cửa sổ ra.",
        5: "Vào ban đêm bọn trẻ ngủ tám tiếng đồng hồ.",
        6: "Các bạn làm việc từ lúc nào đến lúc nào? — Từ 8 giờ đến 12 giờ chúng tôi làm việc.",
        7: "Hôm qua bạn đã không gặp may, nhưng hôm nay bạn có nhiều may mắn.",
        8: "Các bạn đã có một bữa tiệc tuyệt vời chứ?",
        9: "Anh trai tôi có sinh nhật vào tháng Sáu.",
        10: "Khi nào bạn thức dậy vào Chủ nhật?",
        11: "Vào thứ Sáu lúc 20 giờ Lisa đi ra ngoài / đi chơi.",
        12: "Hôm qua anh ấy đã không có thời gian, nhưng hôm nay anh ấy có nhiều thời gian.",
        13: "Xin lỗi, tối qua chúng mình không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe.",
        14: "Joan đã có một chiếc điện thoại di động, nhưng cô ấy đã không có số của bạn.",
        15: "Bây giờ là 8 giờ 15 phút (Một phần tư giờ sau mốc 8 giờ).",
        16: "cuối tuần = das Wochenende",
        17: "thứ Tư = der Mittwoch",
        18: "thức dậy = aufstehen",
        19: "ăn sáng = frühstücken",
        20: "sự cố (hỏng xe) = die Panne",
        21: "từ thứ Hai đến thứ Sáu = von Montag bis Freitag",
        22: "der Nachmittag = buổi chiều (14:00 – 18:00)",
        23: "die Stunde = giờ, tiếng đồng hồ (thời lượng)",
        24: "aufmachen = mở ra (cửa, sách...)",
        25: "ausgehen = đi ra ngoài / đi chơi",
        26: "halb drei = 2 giờ rưỡi (2h30)",
        27: "Mittagspause machen = nghỉ trưa / nghỉ ăn trưa",
        28: "1. acht Uhr fünfzehn / Viertel nach acht: 8 giờ 15 phút (8 giờ hơn 15)\n2. neun Uhr zehn / zehn nach neun: 9 giờ 10 phút\n3. zwei Uhr dreißig / halb drei: 2 giờ 30 phút (2 rưỡi)\n4. fünf Uhr fünfzig / zehn vor sechs: 5 giờ 50 phút (6 giờ kém 10)",
        29: "1. um 8 Uhr: vào lúc 8 giờ\n2. am Sonntag / am Morgen: vào Chủ nhật / vào buổi sáng\n3. im Juni / im Sommer: vào tháng Sáu / vào mùa hè\n4. in der Nacht: vào ban đêm",
        30: "1. aufstehen (thức dậy) → um 7 Uhr morgens aus dem Bett (ra khỏi giường lúc 7 giờ sáng)\n2. frühstücken (ăn sáng) → Kaffee trinken und Brot essen (uống cà phê và ăn bánh mì)\n3. ausgehen (đi chơi / ra ngoài) → am Freitagabend mit Freunden feiern (tiệc tùng với bạn bè vào tối thứ Sáu)\n4. aufmachen (mở ra) → die Tür hoặc das Fenster öffnen (mở cửa ra vào hoặc cửa sổ)",
        31: "1. ich / er / sie / es hatte: tôi / anh ấy / cô ấy / nó đã có\n2. du hattest: bạn đã có\n3. wir / sie / Sie hatten: chúng tôi / họ / quý vị đã có\n4. ihr hattet: các bạn đã có",
        32: "1. der Morgen: buổi sáng sớm (06:00 – 10:00)\n2. der Vormittag: buổi sáng / trước giờ trưa (10:00 – 12:00)\n3. der Nachmittag: buổi chiều (14:00 – 18:00)\n4. die Nacht: ban đêm (22:00 – 06:00)",
        33: "1. Wann steht Thomas am Sonntag auf? → Am Sonntag steht er um 8 Uhr auf. (Chủ nhật Thomas thức dậy lúc mấy giờ? → Vào Chủ nhật anh ấy thức dậy lúc 8 giờ.)\n2. Um wie viel Uhr frühstückt ihr? → Um 9 Uhr frühstücken wir. (Các bạn ăn sáng lúc mấy giờ? → Lúc 9 giờ chúng tôi ăn sáng.)\n3. Von wann bis wann arbeiten die Kollegen? → Von 8 bis 17 Uhr arbeiten sie. (Các đồng nghiệp làm việc từ mấy giờ đến mấy giờ? → Họ làm việc từ 8 giờ đến 17 giờ.)\n4. Wann geht das Kind ins Bett? → Um 21 Uhr geht es ins Bett. (Khi nào đứa trẻ đi ngủ? → Lúc 21 giờ nó đi ngủ.)",
        34: "Vào Chủ nhật chúng tôi thức dậy vào lúc 8 giờ. (Am Sonntag stehen wir um 8 Uhr auf.)",
        35: "Anh ấy mở cánh cửa ra. (Er macht die Tür auf.)",
        36: "Hôm qua chúng tôi đã gặp một sự cố, nhưng hôm nay chúng tôi không gặp sự cố nào.",
        37: "Từ 8 giờ đến 12 giờ các bạn làm việc. (Von 8 bis 12 Uhr arbeitet ihr.)",
        38: "Khi nào các bạn đi chơi vào thứ Sáu? — Vào thứ Sáu lúc 20 giờ chúng tôi đi chơi.",
        39: "Vào Chủ nhật anh ấy thức dậy vào lúc 8 giờ.",
        40: "Vào lúc 9 giờ chúng tôi ăn sáng.",
        41: "Xin lỗi, tối qua chúng mình không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe.",
        42: "Hôm qua anh ấy đã không có tiền, nhưng hôm nay anh ấy có nhiều tiền.",
        43: "Vào Chủ nhật chúng tôi thức dậy lúc 8 giờ. (Am Sonntag stehen wir um 8 Uhr auf.)",
        44: "Từ 8 giờ đến 12 giờ anh ấy làm việc. (Von 8 bis 12 Uhr arbeitet er.)",
        45: "Hôm qua chúng tôi không có thời gian, nhưng hôm nay chúng tôi có nhiều thời gian.",
        46: "Vào thứ Sáu lúc 20 giờ họ đi chơi. (Am Freitag um 20 Uhr gehen sie aus.)",
        47: "Cô ấy mở cửa / Cô ấy mở cánh cửa ra. (Sie macht die Tür auf.)",
        48: "Vào lúc 12 giờ chúng tôi nghỉ trưa. (Um 12 Uhr machen wir Mittagspause.)",
        49: "Hôm qua chúng tôi đã gặp một sự cố, nhưng hôm nay chúng tôi không gặp sự cố nào.",
        50: "Vào lúc 22 giờ anh ấy đi ngủ. (Um 22 Uhr geht er ins Bett.)"
    }

    # =========================================================================
    # KHO 50 BÀI TẬP BÀI 5 CHUẨN 9 DẠNG THEO ĐÚNG ĐẶC TẢ KỸ THUẬT
    # =========================================================================
    exercises = [
        # --- DẠNG 1: TRẮC NGHIỆM (trac_nghiem - 8 Câu) ---
        (
            lesson_id, "trac_nghiem",
            "Câu 1: Chọn giới từ chỉ thời gian đúng điền vào câu: '___ Sonntag steht er ___ 8 Uhr auf.'",
            json.dumps(["Am / um", "Im / um", "Um / am", "Am / im"], ensure_ascii=False),
            "Am / um",
            "Thứ trong tuần ('Sonntag') đi với giới từ 'am'; giờ giấc cụ thể ('8 Uhr') đi với giới từ 'um'.",
            15, json.dumps({"dynamic_prep_quiz": True})
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 2: Cách đọc giờ đời thường (Inoffiziell) nào sau đây tương ứng với 08:15 (acht Uhr fünfzehn)?",
            json.dumps(["Viertel nach acht", "Viertel vor acht", "halb acht", "acht nach Viertel"], ensure_ascii=False),
            "Viertel nach acht",
            "Mốc 08:15 là 8 giờ hơn 15 phút. Trong cách nói đời thường, 15 phút là một phần tư tiếng ('Viertel'), đi qua mốc 8 giờ dùng 'nach' -> 'Viertel nach acht'.",
            15, json.dumps({"translation": "Mốc giờ 08:15: Viertel nach acht (8 giờ hơn 15 phút)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 3: Cách đọc giờ đời thường nào sau đây tương ứng với 14:30 (vierzehn Uhr dreißig / 2h30 chiều)?",
            json.dumps(["halb drei", "halb zwei", "Viertel nach zwei", "dreißig nach zwei"], ensure_ascii=False),
            "halb drei",
            "Trong cách nói giờ đời thường tiếng Đức, giờ rưỡi dùng công thức 'halb + giờ tiếp theo (giờ + 1)'. 2h30 tức là còn nửa tiếng nữa đến 3 giờ, do đó phải đọc là 'halb drei'.",
            15, json.dumps({"translation": "Mốc giờ 14:30 / 2h30: halb drei (2 giờ rưỡi)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 4: Chọn dạng đúng của động từ tách 'aufmachen' (mở) cho câu: 'Es ist heiß. Wir ___ das Fenster ___.'",
            json.dumps(["machen / auf", "aufmachen / —", "macht / auf", "auf / mache"], ensure_ascii=False),
            "machen / auf",
            "Với động từ tách 'aufmachen', trong câu đơn động từ gốc 'machen' đứng ở vị trí số 2 chia theo ngôi 'wir' là 'machen', còn tiền tố 'auf' tách ra đứng ở cuối câu.",
            15, json.dumps({"dynamic_trennbare_quiz": True})
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 5: Chọn giới từ đúng cho danh từ chỉ buổi 'die Nacht' (ban đêm): '___ Nacht schlafen die Kinder acht Stunden.'",
            json.dumps(["In der", "Am", "Im", "Um"], ensure_ascii=False),
            "In der",
            "Khác với các buổi khác mang giống đực (am Morgen, am Abend), riêng 'die Nacht' mang giống cái nên bắt buộc phải dùng cụm giới từ 'in der Nacht'.",
            15, json.dumps({"translation": "Vào ban đêm bọn trẻ ngủ 8 tiếng. (In der Nacht schlafen die Kinder acht Stunden.)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 6: Chọn từ để hỏi đúng cho câu trả lời 'Von 8 bis 12 Uhr arbeiten wir.': '___ arbeitet ihr?'",
            json.dumps(["Von wann bis wann", "Um wie viel Uhr", "Woher", "Wer"], ensure_ascii=False),
            "Von wann bis wann",
            "Để hỏi khoảng thời gian bắt đầu và kết thúc tương ứng với câu trả lời 'Von ... bis ...', ta dùng cụm từ để hỏi 'Von wann bis wann...?'. Câu hỏi chia theo ngôi 'ihr' (các bạn): 'Von wann bis wann arbeitet ihr?'.",
            15, json.dumps({"translation": "Các bạn làm việc từ mấy giờ đến mấy giờ? (Von wann bis wann arbeitet ihr?)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 7: Chọn dạng quá khứ đơn (Präteritum) đúng của động từ 'haben' cho chủ ngữ 'wir': 'Gestern Abend ___ wir leider keine Zeit.'",
            json.dumps(["hatten", "hatte", "hattet", "hattest"], ensure_ascii=False),
            "hatten",
            "Chủ ngữ là ngôi 'wir' (chúng tôi), động từ 'haben' ở thì quá khứ đơn (Präteritum) được chia là 'hatten'. Cả câu: 'Gestern Abend hatten wir leider keine Zeit.' (Tối hôm qua chúng tôi tiếc là không có thời gian).",
            15, json.dumps({"translation": "Tối hôm qua chúng tôi tiếc là không có thời gian. (Gestern Abend hatten wir leider keine Zeit.)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "trac_nghiem",
            "Câu 8: Đọc đoạn thư sau của Maria gửi Thomas:\n„Lieber Thomas, wie geht es dir? Letzte Woche hatte ich Geburtstag und eine tolle Feier. Wie war dein Wochenende mit deinen Freunden? ___ ihr auch eine tolle Party?\nLiebe Grüße, Maria“\n\nChọn dạng chia đúng của động từ 'haben' ở thì Präteritum đi với ngôi 'ihr' để điền vào chỗ trống cuối thư:",
            json.dumps(["Hattet", "Hattest", "Hatten", "Hatte"], ensure_ascii=False),
            "Hattet",
            "Chủ ngữ trong câu hỏi cuối thư là ngôi 'ihr' (các bạn). Động từ 'haben' ở thì quá khứ đơn (Präteritum) chia theo ngôi 'ihr' là 'hattet': 'Hattet ihr auch eine tolle Party?' (Các bạn cũng đã có một bữa tiệc tuyệt vời chứ?).",
            15, json.dumps({"translation": "Các bạn cũng đã có một bữa tiệc tuyệt vời chứ? (Hattet ihr auch một bữa tiệc tuyệt vời chứ?)"}, ensure_ascii=False)
        ),

        # --- DẠNG 2: ĐIỀN KHUYẾT (dien_khuyet - 7 Câu) ---
        (
            lesson_id, "dien_khuyet",
            "Câu 9: Điền giới từ chỉ thời gian thích hợp vào chỗ trống: 'Mein Bruder hat ___ Juni Geburtstag.'",
            None,
            "im / Im",
            "Tất cả 12 tháng trong năm (der Januar → der Dezember) đều đi với giới từ 'im'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 10: Điền tiền tố tách còn thiếu vào cuối câu: 'Wann stehst du am Sonntag ___?'",
            None,
            "auf",
            "Động từ 'thức dậy' là 'aufstehen', khi chia với 'du' thì gốc 'stehst' đứng ở vị trí số 2 và tiền tố 'auf' đứng ở cuối câu.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 11: Điền tiền tố tách còn thiếu vào cuối câu: 'Am Freitag um 20 Uhr geht Lisa ___.'",
            None,
            "aus",
            "Động từ 'đi chơi / đi ra ngoài' là 'ausgehen' (Lisa geht ... aus).",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 12: Điền dạng chia đúng của động từ 'haben' ở thì quá khứ đơn (Präteritum): 'Gestern ___ er keine Zeit, aber heute hat er viel Zeit.'",
            None,
            "hatte",
            "Ngôi 'er' của động từ 'haben' ở thì Präteritum là 'hatte'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 13: Điền dạng chia đúng của động từ 'haben' ở thì quá khứ đơn (Präteritum): 'Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir ___ eine Panne.'",
            None,
            "hatten",
            "Ngôi 'wir' của động từ 'haben' ở thì Präteritum là 'hatten'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 14: Điền dạng chia đúng của động từ 'haben' ở thì quá khứ đơn (Präteritum): 'Joan ___ ein Handy, aber sie hatte deine Nummer nicht.'",
            None,
            "hatte",
            "Chủ ngữ 'Joan' tương ứng với ngôi thứ 3 số ít (sie - cô ấy), nên 'haben' ở Präteritum chia là 'hatte'.",
            15, None
        ),
        (
            lesson_id, "dien_khuyet",
            "Câu 15: Điền từ chỉ giờ đời thường còn thiếu cho mốc 8h15: 'Es ist ___ nach acht.'",
            None,
            "Viertel / viertel",
            "15 phút bằng 1/4 giờ ('Viertel'), vì vậy 8h15 đọc là 'Viertel nach acht'.",
            15, None
        ),

        # --- DẠNG 3: DỊCH NGHĨA TỪ / CỤM TỪ VIỆT → ĐỨC (dich_nghia_vd - 6 Câu) ---
        (
            lesson_id, "dich_nghia_vd",
            "Câu 16: Dịch sang tiếng Đức: 'cuối tuần'",
            None,
            "das Wochenende / Wochenende / ein Wochenende",
            "'Cuối tuần' trong tiếng Đức là danh từ giống trung 'das Wochenende' (số nhiều: 'die Wochenenden').",
            20, None
        ),
        (
            lesson_id, "dich_nghia_vd",
            "Câu 17: Dịch sang tiếng Đức: 'thứ Tư'",
            None,
            "der Mittwoch / Mittwoch",
            "'Thứ Tư' trong tiếng Đức là 'der Mittwoch' (tất cả các thứ trong tuần đều mang giống đực 'der').",
            20, None
        ),
        (
            lesson_id, "dich_nghia_vd",
            "Câu 18: Dịch sang tiếng Đức (động từ nguyên mẫu): 'thức dậy'",
            None,
            "aufstehen",
            "'Thức dậy' là động từ tách 'aufstehen' (tiền tố 'auf-' + động từ gốc 'stehen').",
            20, None
        ),
        (
            lesson_id, "dich_nghia_vd",
            "Câu 19: Dịch sang tiếng Đức (động từ nguyên mẫu): 'ăn sáng'",
            None,
            "frühstücken / fruehstuecken",
            "'Ăn sáng' trong tiếng Đức là động từ không tách 'frühstücken'.",
            20, None
        ),
        (
            lesson_id, "dich_nghia_vd",
            "Câu 20: Dịch sang tiếng Đức: 'sự cố (hỏng xe)'",
            None,
            "die Panne / Panne / eine Panne",
            "'Sự cố / hỏng xe dọc đường' là danh từ giống cái 'die Panne' (Wir hatten eine Panne).",
            20, None
        ),
        (
            lesson_id, "dich_nghia_vd",
            "Câu 21: Dịch cụm giới từ thời gian sau sang tiếng Đức: 'từ thứ Hai đến thứ Sáu'",
            None,
            "von Montag bis Freitag",
            "Cấu trúc chỉ khoảng thời gian 'từ ... đến ...' là 'von ... bis ...' → 'von Montag bis Freitag'.",
            20, None
        ),

        # --- DẠNG 4: DỊCH NGHĨA TỪ / CỤM TỪ ĐỨC → VIỆT (dich_nghia_dv - 6 Câu) ---
        (
            lesson_id, "dich_nghia_dv",
            "Câu 22: Dịch sang tiếng Việt: „der Nachmittag“",
            None,
            "buổi chiều / chiều",
            "'der Nachmittag' là buổi chiều (khung giờ từ 14h đến 18h).",
            20, None
        ),
        (
            lesson_id, "dich_nghia_dv",
            "Câu 23: Dịch sang tiếng Việt: „die Stunde“",
            None,
            "giờ / tiếng / tiếng đồng hồ / giờ đồng hồ / một giờ / một tiếng",
            "'die Stunde' (số nhiều: 'die Stunden') có nghĩa là giờ / tiếng đồng hồ (chỉ khoảng thời gian).",
            20, None
        ),
        (
            lesson_id, "dich_nghia_dv",
            "Câu 24: Dịch sang tiếng Việt: „aufmachen“",
            None,
            "mở / mở ra / mở cửa",
            "Động từ tách 'aufmachen' ('auf-' + 'machen') có nghĩa là mở ra (như mở cửa, mở sách...).",
            20, None
        ),
        (
            lesson_id, "dich_nghia_dv",
            "Câu 25: Dịch sang tiếng Việt: „ausgehen“",
            None,
            "đi chơi / đi ra ngoài / ra ngoài / đi dạo phố / đi chơi tối",
            "Động từ tách 'ausgehen' ('aus-' + 'gehen') có nghĩa là đi ra ngoài / đi chơi.",
            20, None
        ),
        (
            lesson_id, "dich_nghia_dv",
            "Câu 26: Dịch cách nói giờ sau sang tiếng Việt: „halb drei“",
            None,
            "2 giờ rưỡi / hai giờ rưỡi / 2 giờ 30 / 2 giờ 30 phút / hai giờ ba mươi phút / 2h30",
            "'halb drei' (nửa tiếng trước mốc 3 giờ) có nghĩa là 2 giờ rưỡi (2h30).",
            20, None
        ),
        (
            lesson_id, "dich_nghia_dv",
            "Câu 27: Dịch cụm từ sau sang tiếng Việt: „Mittagspause machen“",
            None,
            "nghỉ trưa / làm giờ nghỉ trưa / nghỉ ăn trưa / giải lao buổi trưa",
            "'die Mittagspause' = giờ nghỉ trưa; 'Mittagspause machen' = nghỉ trưa.",
            20, None
        ),

        # --- DẠNG 5: NỐI Ô TỪ TRÁI QUA PHẢI (noi_o - 6 Bài, mỗi bài 4 cặp) ---
        (
            lesson_id, "noi_o",
            "Câu 28 (Bài nối ô 1): Nối giờ chính thống ở cột trái với cách nói giờ đời thường tương ứng ở cột phải:",
            None,
            "acht Uhr fünfzehn = Viertel nach acht | neun Uhr zehn = zehn nach neun | zwei Uhr dreißig = halb drei | fünf Uhr fünfzig = zehn vor sechs",
            "Quy tắc chuyển đổi giờ chính thống sang giờ đời thường: 1. 'Viertel nach + giờ' = hơn 15 phút (acht Uhr fünfzehn → Viertel nach acht). 2. 'phút + nach + giờ' = giờ hơn (neun Uhr zehn → zehn nach neun). 3. 'halb + (giờ hiện tại + 1)' = giờ rưỡi (zwei Uhr dreißig → 2h30 là nửa tiếng trước mốc 3h → halb drei). 4. 'phút còn thiếu + vor + giờ kế tiếp' = giờ kém (fünf Uhr fünfzig → còn 10 phút nữa tới 6h → zehn vor sechs).",
            25, json.dumps({
                "translation": "1. acht Uhr fünfzehn / Viertel nach acht: 8 giờ 15 phút (8 giờ hơn 15)\n2. neun Uhr zehn / zehn nach neun: 9 giờ 10 phút\n3. zwei Uhr dreißig / halb drei: 2 giờ 30 phút (2 rưỡi)\n4. fünf Uhr fünfzig / zehn vor sechs: 5 giờ 50 phút (6 giờ kém 10)",
                "noi_o_pairs": [
                    {"left": "acht Uhr fünfzehn", "right": "Viertel nach acht"},
                    {"left": "neun Uhr zehn", "right": "zehn nach neun"},
                    {"left": "zwei Uhr dreißig", "right": "halb drei"},
                    {"left": "fünf Uhr fünfzig", "right": "zehn vor sechs"}
                ]
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "noi_o",
            "Câu 29 (Bài nối ô 2): Nối giới từ thời gian ở cột trái với danh từ phù hợp ở cột phải:",
            None,
            "um = 8 Uhr | am = Sonntag / der Morgen | im = der Juni / der Sommer | in der = die Nacht",
            "Quy tắc sử dụng giới từ thời gian: 1. 'um' đi với mốc giờ giấc cụ thể ('um 8 Uhr'). 2. 'am' (an + dem) đi với các thứ trong tuần và các buổi trong ngày ('am Sonntag', 'am Morgen' - ngoại trừ ban đêm). 3. 'im' (in + dem) đi với các tháng và các mùa trong năm ('im Juni', 'im Sommer'). 4. Riêng 'die Nacht' là danh từ giống cái nên ở Dativ bắt buộc dùng cụm cố định 'in der Nacht' (vào ban đêm).",
            25, json.dumps({
                "translation": "1. um 8 Uhr: vào lúc 8 giờ\n2. am Sonntag / am Morgen: vào Chủ nhật / vào buổi sáng\n3. im Juni / im Sommer: vào tháng Sáu / vào mùa hè\n4. in der Nacht: vào ban đêm",
                "noi_o_pairs": [
                    {"left": "um", "right": "8 Uhr"},
                    {"left": "am", "right": "Sonntag / der Morgen"},
                    {"left": "im", "right": "der Juni / der Sommer"},
                    {"left": "in der", "right": "die Nacht"}
                ]
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "noi_o",
            "Câu 30 (Bài nối ô 3): Nối động từ ở cột trái với cụm hoạt động tiếng Đức tương ứng ở cột phải:",
            None,
            "aufstehen = um 7 Uhr morgens aus dem Bett | frühstücken = Kaffee trinken und Brot essen | ausgehen = am Freitagabend mit Freunden feiern | aufmachen = die Tür oder das Fenster öffnen",
            "Mối liên hệ từ vựng và động từ tách: 1. 'aufstehen' (thức dậy, rời giường) đồng nghĩa với việc ra khỏi giường lúc 7 giờ sáng ('aus dem Bett'). 2. 'frühstücken' (ăn sáng) là hoạt động uống cà phê và ăn bánh mì ('Kaffee trinken und Brot essen'). 3. Động từ tách 'ausgehen' (đi chơi, ra ngoài) khớp với việc đi tiệc tùng tối thứ Sáu với bạn bè ('mit Freunden feiern'). 4. Động từ tách 'aufmachen' (mở ra) đồng nghĩa trực tiếp với động từ 'öffnen' (mở cửa ra vào hoặc cửa sổ).",
            25, json.dumps({
                "translation": "1. aufstehen (thức dậy) → um 7 Uhr morgens aus dem Bett (ra khỏi giường lúc 7 giờ sáng)\n2. frühstücken (ăn sáng) → Kaffee trinken und Brot essen (uống cà phê và ăn bánh mì)\n3. ausgehen (đi chơi / ra ngoài) → am Freitagabend mit Freunden feiern (tiệc tùng với bạn bè vào tối thứ Sáu)\n4. aufmachen (mở ra) → die Tür hoặc das Fenster öffnen (mở cửa ra vào hoặc cửa sổ)",
                "noi_o_pairs": [
                    {"left": "aufstehen", "right": "um 7 Uhr morgens aus dem Bett"},
                    {"left": "frühstücken", "right": "Kaffee trinken und Brot essen"},
                    {"left": "ausgehen", "right": "am Freitagabend mit Freunden feiern"},
                    {"left": "aufmachen", "right": "die Tür oder das Fenster öffnen"}
                ]
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "noi_o",
            "Câu 31 (Bài nối ô 4): Nối đại từ nhân xưng ở cột trái với dạng chia đúng của động từ 'haben' ở thì quá khứ đơn (Präteritum) ở cột phải:",
            None,
            "ich / er / sie / es = hatte | du = hattest | wir / sie / Sie = hatten | ihr = hattet",
            "Quy tắc chia động từ 'haben' ở thì quá khứ đơn (Präteritum): Gốc động từ biến đổi thành 'hatt-'. Ngôi thứ nhất ('ich') và ngôi thứ ba số ít ('er/sie/es') luôn có dạng chia giống hệt nhau là 'hatte' (không thêm đuôi -t); ngôi 'du' thêm đuôi '-est' ('hattest'); ngôi 'ihr' thêm đuôi '-et' ('hattet'); các ngôi số nhiều 'wir/sie/Sie' thêm đuôi '-en' ('hatten').",
            25, json.dumps({
                "translation": "1. ich / er / sie / es hatte: tôi / anh ấy / cô ấy / nó đã có\n2. du hattest: bạn đã có\n3. wir / sie / Sie hatten: chúng tôi / họ / quý vị đã có\n4. ihr hattet: các bạn đã có",
                "noi_o_pairs": [
                    {"left": "ich / er / sie / es", "right": "hatte"},
                    {"left": "du", "right": "hattest"},
                    {"left": "wir / sie / Sie", "right": "hatten"},
                    {"left": "ihr", "right": "hattet"}
                ]
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "noi_o",
            "Câu 32 (Bài nối ô 5): Nối các buổi trong ngày ở cột trái với khung giờ tương ứng ở cột phải:",
            None,
            "der Morgen = 06:00 – 10:00 Uhr | der Vormittag = 10:00 – 12:00 Uhr | der Nachmittag = 14:00 – 18:00 Uhr | die Nacht = 22:00 – 06:00 Uhr",
            "Quy tắc về giống và giới từ chỉ các buổi trong ngày: Hầu hết các buổi trong ngày đều mang giống đực (der Morgen, der Vormittag, der Mittag, der Nachmittag, der Abend) và đi với giới từ 'am' (am Morgen, am Vormittag, am Nachmittag...). Ngoại lệ duy nhất là 'die Nacht' mang giống cái và bắt buộc đi với giới từ 'in der' ('in der Nacht').",
            25, json.dumps({
                "translation": "1. der Morgen: buổi sáng sớm (06:00 – 10:00)\n2. der Vormittag: buổi sáng / trước giờ trưa (10:00 – 12:00)\n3. der Nachmittag: buổi chiều (14:00 – 18:00)\n4. die Nacht: ban đêm (22:00 – 06:00)",
                "noi_o_pairs": [
                    {"left": "der Morgen", "right": "06:00 – 10:00 Uhr"},
                    {"left": "der Vormittag", "right": "10:00 – 12:00 Uhr"},
                    {"left": "der Nachmittag", "right": "14:00 – 18:00 Uhr"},
                    {"left": "die Nacht", "right": "22:00 – 06:00 Uhr"}
                ]
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "noi_o",
            "Câu 33 (Bài nối ô 6): Nối câu hỏi lịch trình (Tagesabläufe) ở cột trái với câu trả lời tương ứng ở cột phải:",
            None,
            "Wann steht Thomas am Sonntag auf? = Am Sonntag steht er um 8 Uhr auf. | Um wie viel Uhr frühstückt ihr? = Um 9 Uhr frühstücken wir. | Von wann bis wann arbeiten die Kollegen? = Von 8 bis 17 Uhr arbeiten sie. | Wann geht das Kind ins Bett? = Um 21 Uhr geht es ins Bett.",
            "Cách đối chiếu đại từ chủ ngữ và từ để hỏi để tìm câu trả lời đúng: 1. 'Thomas' (nam số ít) được thay thế bằng đại từ 'er' kết hợp động từ tách 'steht ... auf'; 2. Câu hỏi hỏi ngôi 'ihr' (các bạn) thì câu trả lời phải đáp bằng ngôi 'wir' (chúng tôi); 3. 'die Kollegen' (đồng nghiệp - số nhiều) được thay bằng đại từ 'sie' (họ) và câu hỏi 'Von wann bis wann' khớp với câu trả lời 'Von ... bis ...'; 4. 'das Kind' (đứa trẻ - giống trung) được thay thế tương ứng bằng đại từ 'es'.",
            25, json.dumps({
                "translation": "1. Wann steht Thomas am Sonntag auf? → Am Sonntag steht er um 8 Uhr auf. (Chủ nhật Thomas thức dậy lúc mấy giờ? → Vào Chủ nhật anh ấy thức dậy lúc 8 giờ.)\n2. Um wie viel Uhr frühstückt ihr? → Um 9 Uhr frühstücken wir. (Các bạn ăn sáng lúc mấy giờ? → Lúc 9 giờ chúng tôi ăn sáng.)\n3. Von wann bis wann arbeiten die Kollegen? → Von 8 bis 17 Uhr arbeiten sie. (Các đồng nghiệp làm việc từ mấy giờ đến mấy giờ? → Họ làm việc từ 8 giờ đến 17 giờ.)\n4. Wann geht das Kind ins Bett? → Um 21 Uhr geht es ins Bett. (Khi nào đứa trẻ đi ngủ? → Lúc 21 giờ nó đi ngủ.)",
                "noi_o_pairs": [
                    {"left": "Wann steht Thomas am Sonntag auf?", "right": "Am Sonntag steht er um 8 Uhr auf."},
                    {"left": "Um wie viel Uhr frühstückt ihr?", "right": "Um 9 Uhr frühstücken wir."},
                    {"left": "Von wann bis wann arbeiten die Kollegen?", "right": "Von 8 bis 17 Uhr arbeiten sie."},
                    {"left": "Wann geht das Kind ins Bett?", "right": "Um 21 Uhr geht es ins Bett."}
                ]
            }, ensure_ascii=False)
        ),

        # --- DẠNG 6: ĐIỀN VÀO CHỖ TRỐNG ĐỂ TẠO THÀNH CÂU (dien_tao_cau - 5 Câu) ---
        (
            lesson_id, "dien_tao_cau",
            "Câu 34: Điền 2 từ còn thiếu vào chỗ trống (cách nhau bởi dấu gạch chéo '/') để hoàn thành câu: 'Am Sonntag ___ wir um 8 Uhr ___.'",
            None,
            "stehen / auf / stehen auf / wachen / auf / wachen auf",
            "Khi 'Am Sonntag' đứng đầu câu, động từ gốc 'stehen' đứng ở vị trí số 2 (trước chủ ngữ 'wir'), còn tiền tố 'auf' đứng ở cuối câu (động từ tách 'aufstehen' / 'aufwachen').",
            20, json.dumps({"translation": "Vào Chủ nhật chúng tôi thức dậy vào lúc 8 giờ. (Am Sonntag stehen wir um 8 Uhr auf.)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "dien_tao_cau",
            "Câu 35: Điền 2 từ còn thiếu vào chỗ trống (cách nhau bởi dấu '/') để hoàn thành câu: 'Er ___ die Tür ___.'",
            None,
            "macht / auf / macht auf / macht / zu / macht zu / schließt / ab / schliesst / ab",
            "Động từ tách 'aufmachen' (mở) hoặc 'zumachen' (đóng) chia cho ngôi 'er': động từ gốc 'macht' đứng ở vị trí số 2 và tiền tố 'auf' (hoặc 'zu') đứng ở cuối câu.",
            20, json.dumps({"translation": "Anh ấy mở cánh cửa ra (Er macht die Tür auf) hoặc Anh ấy đóng cánh cửa lại (Er macht die Tür zu)."}, ensure_ascii=False)
        ),
        (
            lesson_id, "dien_tao_cau",
            "Câu 36: Điền 2 từ còn thiếu vào chỗ trống (cách nhau bởi dấu '/') để đối chiếu quá khứ – hiện tại: 'Gestern ___ wir eine Panne, aber heute ___ wir keine Panne.'",
            None,
            "hatten / haben",
            "Với chủ ngữ 'wir', ở mệnh đề quá khứ ('Gestern') ta dùng 'hatten' (Präteritum), còn ở mệnh đề hiện tại ('heute') ta dùng 'haben' (Präsens).",
            20, json.dumps({"translation": "Hôm qua chúng tôi bị hỏng xe, nhưng hôm nay chúng tôi không bị hỏng xe."}, ensure_ascii=False)
        ),
        (
            lesson_id, "dien_tao_cau",
            "Câu 37: Điền 2 từ còn thiếu vào chỗ trống (cách nhau bởi dấu '/') để tạo câu lịch trình: 'Von 8 ___ 12 Uhr ___ ihr.'",
            None,
            "bis / arbeitet",
            "Cấu trúc chỉ khoảng thời gian 'Von 8 bis 12 Uhr' đứng ở vị trí số 1, động từ 'arbeiten' chia theo ngôi 'ihr' là 'arbeitet' đứng ở vị trí số 2.",
            20, json.dumps({"translation": "Từ 8 giờ đến 12 giờ các bạn làm việc. (Von 8 bis 12 Uhr arbeitet ihr.)"}, ensure_ascii=False)
        ),
        (
            lesson_id, "dien_tao_cau",
            "Câu 38: Điền 2 từ còn thiếu vào chỗ trống (cách nhau bởi dấu '/') để hoàn thành cặp hỏi – đáp: 'Wann geht ihr am Freitag ___? — Am Freitag um 20 Uhr ___ wir aus.'",
            None,
            "aus / gehen",
            "Động từ tách 'ausgehen' tách tiền tố 'aus' xuống cuối câu hỏi (ngôi 'ihr' chia là 'geht'), và ở câu trả lời động từ gốc 'gehen' chia theo ngôi 'wir' đứng ở vị trí số 2.",
            20, json.dumps({"translation": "Khi nào các bạn đi chơi vào thứ Sáu? — Vào thứ Sáu lúc 20 giờ chúng tôi đi chơi."}, ensure_ascii=False)
        ),

        # --- DẠNG 7: NGHE GIỌNG BẢN XỨ DE-DE VÀ ĐIỀN TỪ (nghe_dien - 4 Câu) ---
        (
            lesson_id, "nghe_dien",
            "Câu 39 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Am Sonntag ___ er um acht Uhr auf.'",
            None,
            "steht",
            "Động từ gốc 'steht' chia theo ngôi 'er' đứng ở vị trí thứ 2 trong câu. Cả câu: 'Am Sonntag steht er um acht Uhr auf.' (Vào Chủ nhật anh ấy thức dậy vào lúc 8 giờ.)",
            20, json.dumps({
                "audio_text": "Am Sonntag steht er um acht Uhr auf.",
                "display_sentence": "Am Sonntag ___ er um acht Uhr auf.",
                "translation": "Vào Chủ nhật anh ấy thức dậy vào lúc 8 giờ."
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe_dien",
            "Câu 40 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Um neun Uhr ___ wir.'",
            None,
            "frühstücken / fruehstuecken",
            "Động từ không tách 'frühstücken' chia ở ngôi 'wir' là 'frühstücken'. Cả câu: 'Um neun Uhr frühstücken wir.' (Vào lúc 9 giờ chúng tôi ăn sáng.)",
            20, json.dumps({
                "audio_text": "Um neun Uhr frühstücken wir.",
                "display_sentence": "Um neun Uhr ___ wir.",
                "translation": "Vào lúc 9 giờ chúng tôi ăn sáng."
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe_dien",
            "Câu 41 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine ___.'",
            None,
            "Panne",
            "Danh từ 'die Panne' có nghĩa là sự cố hỏng xe dọc đường. Cả câu: 'Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine Panne.' (Xin lỗi, tối qua chúng mình không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe.)",
            20, json.dumps({
                "audio_text": "Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine Panne.",
                "display_sentence": "Entschuldigung, wir waren gestern Abend nicht bei der Party. Wir hatten eine ___.",
                "translation": "Xin lỗi, tối qua chúng mình không có mặt ở bữa tiệc. Chúng mình đã gặp một sự cố hỏng xe."
            }, ensure_ascii=False)
        ),
        (
            lesson_id, "nghe_dien",
            "Câu 42 [Luyện Nghe]: Nghe và điền từ còn thiếu vào chỗ trống: 'Gestern ___ er kein Geld, aber heute hat er viel Geld.'",
            None,
            "hatte",
            "Quá khứ đơn (Präteritum) của động từ 'haben' với ngôi 'er' là 'hatte'. Cả câu: 'Gestern hatte er kein Geld, aber heute hat er viel Geld.' (Hôm qua anh ấy đã không có tiền, nhưng hôm nay anh ấy có nhiều tiền.)",
            20, json.dumps({
                "audio_text": "Gestern hatte er kein Geld, aber heute hat er viel Geld.",
                "display_sentence": "Gestern ___ er kein Geld, aber heute hat er viel Geld.",
                "translation": "Hôm qua anh ấy đã không có tiền, nhưng hôm nay anh ấy có nhiều tiền."
            }, ensure_ascii=False)
        ),

        # --- DẠNG 8: DỊCH CÂU HOÀN CHỈNH VIỆT → ĐỨC (dich_cau_vd - 4 Câu) ---
        (
            lesson_id, "dich_cau_vd",
            "Câu 43: Dịch câu sau sang tiếng Đức: 'Vào Chủ nhật chúng tôi thức dậy lúc 8 giờ.'",
            None,
            "Am Sonntag stehen wir um 8 Uhr auf. / Am Sonntag stehen wir um acht Uhr auf. / Wir stehen am Sonntag um 8 Uhr auf. / Wir stehen am Sonntag um acht Uhr auf. / Um 8 Uhr stehen wir am Sonntag auf.",
            "Chấp nhận cả cách đưa trạng ngữ 'Am Sonntag' lên đầu câu (đảo ngữ 'stehen wir') hoặc để chủ ngữ 'Wir stehen' ở đầu câu, miễn động từ 'stehen' ở vị trí số 2 và tiền tố 'auf' ở cuối câu.",
            25, None
        ),
        (
            lesson_id, "dich_cau_vd",
            "Câu 44: Dịch câu sau sang tiếng Đức: 'Từ 8 giờ đến 12 giờ anh ấy làm việc.'",
            None,
            "Von 8 bis 12 Uhr arbeitet er. / Von acht bis zwölf Uhr arbeitet er. / Er arbeitet von 8 bis 12 Uhr. / Er arbeitet von acht bis十二 Uhr. / Er arbeitet von acht bis zwölf Uhr. / Von 8 Uhr bis 12 Uhr arbeitet er.",
            "Cấu trúc 'von ... bis ...' kết hợp với động từ 'arbeiten' chia cho ngôi 'er' là 'arbeitet'.",
            25, None
        ),
        (
            lesson_id, "dich_cau_vd",
            "Câu 45: Dịch câu sau sang tiếng Đức: 'Hôm qua chúng tôi không có thời gian, nhưng hôm nay chúng tôi có nhiều thời gian.'",
            None,
            "Gestern hatten wir keine Zeit, aber heute haben wir viel Zeit. / Wir hatten gestern keine Zeit, aber heute haben wir viel Zeit. / Gestern hatten wir keine Zeit, aber wir haben heute viel Zeit. / Wir hatten gestern keine Zeit, aber wir haben heute viel Zeit.",
            "Mệnh đề quá khứ với 'gestern' dùng 'hatten wir keine Zeit', mệnh đề hiện tại với 'heute' dùng 'haben wir viel Zeit'.",
            25, None
        ),
        (
            lesson_id, "dich_cau_vd",
            "Câu 46: Dịch câu sau sang tiếng Đức: 'Vào thứ Sáu lúc 20 giờ họ đi chơi.'",
            None,
            "Am Freitag um 20 Uhr gehen sie aus. / Am Freitag um zwanzig Uhr gehen sie aus. / Sie gehen am Freitag um 20 Uhr aus. / Sie gehen am Freitag um zwanzig Uhr aus. / Am Freitag gehen sie um 20 Uhr aus.",
            "Động từ tách 'ausgehen' chia cho ngôi 'sie' (họ): 'gehen' đứng ở vị trí số 2, tiền tố 'aus' tách ra đứng ở cuối câu.",
            25, None
        ),

        # --- DẠNG 9: DỊCH CÂU HOÀN CHỈNH ĐỨC → VIỆT (dich_cau_dv - 4 Câu) ---
        (
            lesson_id, "dich_cau_dv",
            "Câu 47: Dịch câu sau sang tiếng Việt: „Sie macht die Tür auf.“",
            None,
            "Cô ấy mở cửa / Cô ấy mở cánh cửa / Cô ấy mở cửa ra / Cô ấy mở cánh cửa ra / Bà ấy mở cửa / Bà ấy mở cánh cửa / Bà ấy mở cửa ra / Bà ấy mở cánh cửa ra",
            "'aufmachen' = mở ra; 'die Tür' = cánh cửa; 'Sie macht die Tür auf' = Cô ấy mở cánh cửa ra.",
            25, None
        ),
        (
            lesson_id, "dich_cau_dv",
            "Câu 48: Dịch câu sau sang tiếng Việt: „Um 12 Uhr machen wir Mittagspause.“",
            None,
            "Vào lúc 12 giờ chúng tôi nghỉ trưa / Lúc 12 giờ chúng tôi nghỉ trưa / 12 giờ chúng tôi nghỉ trưa / Chúng tôi nghỉ trưa vào lúc 12 giờ / Chúng tôi nghỉ trưa lúc 12 giờ / Chúng mình nghỉ trưa lúc 12 giờ / Vào lúc 12 giờ chúng mình nghỉ trưa / Lúc 12 giờ chúng mình nghỉ trưa / 12 giờ chúng mình nghỉ trưa / Chúng mình nghỉ trưa vào lúc 12 giờ",
            "'Um 12 Uhr' = vào lúc 12 giờ; 'Mittagspause machen' = nghỉ trưa.",
            25, None
        ),
        (
            lesson_id, "dich_cau_dv",
            "Câu 49: Dịch câu sau sang tiếng Việt: „Gestern hatten wir eine Panne, aber heute haben wir keine Panne.“",
            None,
            "Hôm qua chúng tôi đã gặp một sự cố, nhưng hôm nay chúng tôi không gặp sự cố nào / Hôm qua chúng tôi có một sự cố hỏng xe, nhưng hôm nay chúng tôi không có sự cố nào / Hôm qua chúng tôi bị hỏng xe, nhưng hôm nay chúng tôi không bị hỏng xe / Hôm qua chúng mình gặp sự cố, nhưng hôm nay chúng mình không gặp sự cố",
            "'eine Panne haben' = gặp sự cố (hỏng xe); 'hatten' là quá khứ đơn của 'haben' ở ngôi 'wir'.",
            25, None
        ),
        (
            lesson_id, "dich_cau_dv",
            "Câu 50: Dịch câu sau sang tiếng Việt: „Um 22 Uhr geht er ins Bett.“",
            None,
            "Vào lúc 22 giờ anh ấy đi ngủ / Lúc 22 giờ anh ấy đi ngủ / 22 giờ anh ấy đi ngủ / Anh ấy đi ngủ vào lúc 22 giờ / Anh ấy đi ngủ lúc 22 giờ / Vào lúc 10 giờ tối anh ấy đi ngủ / Lúc 22 giờ anh ấy lên giường đi ngủ / Anh ấy lên giường đi ngủ lúc 22 giờ / Anh ấy đi ngủ lúc 10 giờ tối",
            "'Um 22 Uhr' = vào lúc 22 giờ; 'ins Bett gehen' = lên giường / đi ngủ.",
            25, None
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
        trans_val = EXERCISE_TRANSLATIONS.get(q_num)
        if trans_val and not extra_d.get("translation"):
            extra_d["translation"] = trans_val
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
    print("✅ Đã khởi tạo thành công Bài 5: 'Thời gian - Động từ tách - Haben in Präteritum (Termine)' với đầy đủ 6 Học phần Lý thuyết (Không link YouTube) + 38 Từ vựng + ĐÚNG 50 Bài tập (8+7+6+6+6+5+4+4+4) chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_5()

