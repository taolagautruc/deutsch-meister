# -*- coding: utf-8 -*-
import os
import sys
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tools.generate_all_b8 import build_full_lesson8_seed_script as get_grammar_html

def build_lesson_8_seed():
    grammar_html = get_grammar_html()

    cat1 = 'Địa điểm trong Thành phố & Giao thông Chỉ đường (In der Stadt & Wegbeschreibung - Bài 8)'
    cat2 = 'Danh lam Thắng cảnh tại Thủ đô Berlin (Sehenswürdigkeiten in Berlin - Bài 8)'

    # 50 VOCABULARIES
    vocab_raw = [
        # 30 In der Stadt & Transport
        ('Bahnhof', 'der', 'der', 'die Bahnhöfe', 'ein Bahnhof', 'kein Bahnhof', 'nhà ga tàu hỏa', cat1, 'Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm đuôi -e (die Bahnhöfe).', 'Entschuldigung, wie komme ich zum Bahnhof?', 'Xin lỗi, làm thế nào tôi đi đến được nhà ga?'),
        ('Hauptbahnhof', 'der', 'der', 'die Hauptbahnhöfe', 'ein Hauptbahnhof', 'kein Hauptbahnhof', 'nhà ga trung tâm', cat1, 'Danh từ ghép với der Bahnhof (Haupt + Bahnhof), số nhiều: die Hauptbahnhöfe.', 'Der Zug nach München fährt vom Hauptbahnhof ab.', 'Chuyến tàu đi München khởi hành từ nhà ga trung tâm.'),
        ('Hafen', 'der', 'der', 'die Häfen', 'ein Hafen', 'kein Hafen', 'cảng biển', cat1, 'Danh từ giống đực (der), số nhiều biến âm a -> ä (die Häfen).', 'In Hamburg besichtigen wir den großen Hafen.', 'Ở Hamburg chúng tôi tham quan cảng biển lớn.'),
        ('Flughafen', 'der', 'der', 'die Flughäfen', 'ein Flughafen', 'kein Flughafen', 'sân bay', cat1, 'Danh từ ghép (Flug + der Hafen), số nhiều: die Flughäfen.', 'Der Taxifahrer fährt schnell zum Flughafen.', 'Người tài xế taxi lái xe nhanh đến sân bay.'),
        ('Markt', 'der', 'der', 'die Märkte', 'ein Markt', 'kein Markt', 'chợ, khu chợ', cat1, 'Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm đuôi -e (die Märkte).', 'Am Samstag kaufe ich frisches Obst auf dem Markt.', 'Vào thứ Bảy tôi mua hoa quả tươi ở chợ.'),
        ('Supermarkt', 'der', 'der', 'die Supermärkte', 'ein Supermarkt', 'kein Supermarkt', 'siêu thị', cat1, 'Danh từ ghép (Super + der Markt), số nhiều: die Supermärkte.', 'Er geht nach der Arbeit in den Supermarkt einkaufen.', 'Anh ấy đi vào siêu thị mua sắm sau giờ làm việc.'),
        ('Platz', 'der', 'der', 'die Plätze', 'ein Platz', 'kein Platz', 'quảng trường, chỗ', cat1, 'Danh từ giống đực (der), số nhiều biến âm a -> ä và thêm -e (die Plätze). Băng qua quảng trường: über den Platz.', 'Gehen Sie geradeaus über den Platz!', 'Ngài hãy đi thẳng băng qua quảng trường!'),
        ('Park', 'der', 'der', 'die Parks', 'ein Park', 'kein Park', 'công viên', cat1, 'Danh từ giống đực (der), số nhiều thêm -s (die Parks). Đi xuyên qua công viên: durch den Park.', 'Am Nachmittag spazieren wir gern durch den Park.', 'Vào buổi chiều chúng tôi thích đi dạo xuyên qua công viên.'),
        ('Zoo', 'der', 'der', 'die Zoos', 'ein Zoo', 'kein Zoo', 'vườn bách thú, sở thú', cat1, 'Danh từ giống đực vay mượn, số nhiều thêm -s (die Zoos).', 'Am Wochenende besuchen viele Familien den Zoo.', 'Vào cuối tuần nhiều gia đình đi tham quan sở thú.'),
        ('Turm', 'der', 'der', 'die Türme', 'ein Turm', 'kein Turm', 'tòa tháp, ngọn tháp', cat1, 'Danh từ giống đực (der), số nhiều biến âm u -> ü và thêm -e (die Türme).', 'Von diesem Turm hat man eine schöne Aussicht.', 'Từ ngọn tháp này người ta có một tầm nhìn rất đẹp.'),
        ('Dom', 'der', 'der', 'die Dome', 'ein Dom', 'kein Dom', 'nhà thờ lớn, thánh đường', cat1, 'Danh từ giống đực (der), số nhiều thêm đuôi -e (die Dome).', 'Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.', 'Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc.'),
        ('Stadt', 'die', 'die', 'die Städte', 'eine Stadt', 'keine Stadt', 'thành phố', cat1, 'Danh từ giống cái (die), số nhiều biến âm a -> ä và thêm -e (die Städte).', 'Berlin ist eine sehr interessante Stadt.', 'Berlin là một thành phố rất thú vị.'),
        ('Kirche', 'die', 'die', 'die Kirchen', 'eine Kirche', 'keine Kirche', 'nhà thờ', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Kirchen). Đi ngang qua nhà thờ: an der Kirche vorbei.', 'Gehen Sie an der Kirche vorbei und dann links!', 'Ngài hãy đi ngang qua nhà thờ rồi sau đó rẽ trái!'),
        ('Schule', 'die', 'die', 'die Schulen', 'eine Schule', 'keine Schule', 'trường học', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Schulen).', 'Die Kinder gehen jeden Morgen zur Schule.', 'Bọn trẻ đi đến trường vào mỗi buổi sáng.'),
        ('Brücke', 'die', 'die', 'die Brücken', 'eine Brücke', 'keine Brücke', 'cây cầu', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Brücken). Đi qua cầu: über die Brücke.', 'Wir laufen über die Brücke zum Museum.', 'Chúng tôi đi bộ qua cây cầu đến viện bảo tàng.'),
        ('Bank', 'die', 'die', 'die Banken', 'eine Bank', 'keine Bank', 'ngân hàng (tài chính)', cat1, 'Phân biệt 2 nghĩa: Ngân hàng tiền số nhiều là die Banken; ghế băng dài số nhiều là die Bänke.', 'Vor der Reise muss ich noch zur Bank gehen.', 'Trước chuyến đi tôi còn phải ra ngân hàng.'),
        ('Post', 'die', 'die', 'nur Singular', 'eine Post', 'keine Post', 'bưu điện, ngành bưu chính', cat1, 'Danh từ giống cái chỉ dùng ở số ít (nur Singular). Khi muốn đếm nhiều bưu cục cụ thể dùng das Postamt -> die Postämter.', 'Ich bringe diesen Brief schnell zur Post.', 'Tôi mang lá thư này nhanh ra bưu điện.'),
        ('Straße', 'die', 'die', 'die Straßen', 'eine Straße', 'keine Straße', 'con đường, con phố', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Straßen). Đi dọc phố: die Straße entlang.', 'In dieser Straße gibt es viele kleine Cafés.', 'Trên con phố này có rất nhiều quán cà phê nhỏ.'),
        ('Ampel', 'die', 'die', 'die Ampeln', 'eine Ampel', 'keine Ampel', 'đèn giao thông', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Ampeln). Cho đến đèn giao thông: bis zur Ampel.', 'An der Ampel biegen Sie bitte rechts ab!', 'Tại đèn giao thông xin Ngài hãy rẽ phải!'),
        ('Kreuzung', 'die', 'die', 'die Kreuzungen', 'eine Kreuzung', 'keine Kreuzung', 'ngã tư, giao lộ', cat1, 'Hậu tố -ung luôn là giống cái (die), số nhiều: die Kreuzungen. Băng qua ngã tư: über die Kreuzung.', 'An der nächsten Kreuzung fahren wir geradeaus.', 'Tại ngã tư tiếp theo chúng ta đi thẳng.'),
        ('Disko', 'die', 'die', 'die Diskos', 'eine Disko', 'keine Disko', 'vũ trường, quán bar nhảy', cat1, 'Danh từ giống cái (die), số nhiều thêm -s (die Diskos). Vào vũ trường: in die Disko.', 'Am Freitagabend gehen die Jugendlichen in die Disko.', 'Vào tối thứ Sáu các bạn trẻ đi vào vũ trường.'),
        ('Schloss', 'das', 'das', 'die Schlösser', 'ein Schloss', 'kein Schloss', 'lâu đài, cung điện', cat1, 'Danh từ giống trung (das), số nhiều biến âm o -> ö và thêm -er (die Schlösser).', 'Das alte Schloss liegt direkt am Fluss.', 'Tòa lâu đài cổ nằm ngay bên cạnh dòng sông.'),
        ('Stadttor', 'das', 'das', 'die Stadttore', 'ein Stadttor', 'kein Stadttor', 'cổng thành', cat1, 'Danh từ ghép giống trung (die Stadt + das Tor), số nhiều: die Stadttore. Đi xuyên qua cổng: durch das Stadttor.', 'Die Touristen gehen durch das historische Stadttor.', 'Các du khách đi xuyên qua cổng thành lịch sử.'),
        ('Kino', 'das', 'das', 'die Kinos', 'ein Kino', 'kein Kino', 'rạp chiếu phim', cat1, 'Danh từ giống trung (das), số nhiều thêm -s (die Kinos). Đi vào rạp: ins Kino (in das Kino).', 'Heute Abend gehen wir zusammen ins Kino.', 'Tối nay chúng tôi cùng nhau đi xem phim ở rạp.'),
        ('Krankenhaus', 'das', 'das', 'die Krankenhäuser', 'ein Krankenhaus', 'kein Krankenhaus', 'bệnh viện', cat1, 'Danh từ ghép giống trung (der Kranke + das Haus), số nhiều: die Krankenhäuser. Đi ngang qua: am Krankenhaus vorbei.', 'Der Arzt arbeitet jeden Tag im Krankenhaus.', 'Bác sĩ làm việc mỗi ngày ở trong bệnh viện.'),
        ('Einkaufszentrum', 'das', 'das', 'die Einkaufszentren', 'ein Einkaufszentrum', 'kein Einkaufszentrum', 'trung tâm thương mại', cat1, 'Đuôi -um đổi thành -en ở số nhiều: die Einkaufszentren. Giống trung (das).', 'Am Samstag gehen viele Leute ins Einkaufszentrum.', 'Vào thứ Bảy nhiều người đi vào trung tâm thương mại.'),
        ('Hotel', 'das', 'das', 'die Hotels', 'ein Hotel', 'kein Hotel', 'khách sạn', cat1, 'Danh từ giống trung (das), số nhiều thêm -s (die Hotels).', 'Die Touristen übernachten in einem modernen Hotel.', 'Các du khách nghỉ qua đêm trong một khách sạn hiện đại.'),
        ('Museum', 'das', 'das', 'die Museen', 'ein Museum', 'kein Museum', 'viện bảo tàng', cat1, 'Đuôi -um đổi thành -en ở số nhiều: die Museen. Giống trung (das).', 'Morgen wollen wir das historische Museum besuchen.', 'Ngày mai chúng tôi muốn đi tham quan viện bảo tàng lịch sử.'),
        ('Rathaus', 'das', 'das', 'die Rathäuser', 'ein Rathaus', 'kein Rathaus', 'tòa thị chính', cat1, 'Danh từ ghép giống trung (der Rat + das Haus), số nhiều: die Rathäuser.', 'Vor dem Rathaus gibt es einen schönen Marktplatz.', 'Ở phía trước tòa thị chính có một quảng trường chợ đẹp.'),
        ('Theater', 'das', 'das', 'die Theater', 'ein Theater', 'kein Theater', 'nhà hát kịch', cat1, 'Danh từ giống trung (das), giữ nguyên dạng ở số nhiều (die Theater).', 'Am Wochenende gehen wir ins Theater.', 'Vào cuối tuần chúng tôi đi xem kịch ở nhà hát.'),

        # 14 Sehenswürdigkeiten Berlin
        ('Reichstag', 'der', 'der', 'die Reichstage', 'ein Reichstag', 'kein Reichstag', 'Tòa nhà Quốc hội Đức', cat2, 'Danh lam thắng cảnh Berlin giống đực (vì der Tag). Đi tới: zum Reichstag.', 'Die Touristen stehen vor dem Reichstag und fotografieren die Glaskuppel.', 'Các du khách đứng trước Tòa nhà Quốc hội và chụp ảnh mái vòm kính.'),
        ('Alexanderplatz', 'der', 'der', 'nur Singular', 'ein Alexanderplatz', 'kein Alexanderplatz', 'Quảng trường Alexander', cat2, 'Quảng trường nổi tiếng ở Berlin mang giống đực (vì der Platz). Đi tới: zum Alexanderplatz.', 'Wir treffen uns heute Nachmittag am Alexanderplatz.', 'Chúng ta hẹn gặp nhau vào chiều nay ở Quảng trường Alexander.'),
        ('Potsdamer Platz', 'der', 'der', 'nur Singular', 'ein Potsdamer Platz', 'kein Potsdamer Platz', 'Quảng trường Potsdam', cat2, 'Quảng trường hiện đại tại Berlin mang giống đực (vì der Platz).', 'Am Potsdamer Platz gibt es viele moderne Hochhäuser und Kinos.', 'Ở Quảng trường Potsdam có rất nhiều tòa nhà cao tầng hiện đại và rạp chiếu phim.'),
        ('Berliner Dom', 'der', 'der', 'nur Singular', 'ein Berliner Dom', 'kein Berliner Dom', 'Nhà thờ lớn Berlin', cat2, 'Thánh đường lớn ở Berlin mang giống đực (vì der Dom). Đi vào trong: in den Berliner Dom.', 'Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.', 'Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc.'),
        ('Fernsehturm', 'der', 'der', 'die Fernsehtürme', 'ein Fernsehturm', 'kein Fernsehturm', 'Tháp truyền hình Berlin', cat2, 'Tòa tháp cao nhất nước Đức tại Berlin mang giống đực (vì der Turm).', 'Der Fernsehturm ist das höchste Bauwerk in ganz Deutschland.', 'Tháp truyền hình là công trình kiến trúc cao nhất trên toàn nước Đức.'),
        ('Humboldt-Universität', 'die', 'die', 'die Humboldt-Universitäten', 'eine Humboldt-Universität', 'keine Humboldt-Universität', 'Trường Đại học Humboldt', cat2, 'Hậu tố -tät luôn mang giống cái (die). Đi tới: zur Humboldt-Universität.', 'In Deutschland will mein Bruder an der Humboldt-Universität studieren.', 'Ở Đức anh trai tôi muốn học đại học tại trường Đại học Humboldt.'),
        ('Staatsoper', 'die', 'die', 'die Staatsopern', 'eine Staatsoper', 'keine Staatsoper', 'Nhà hát Opera Quốc gia Berlin', cat2, 'Danh lam thắng cảnh mang giống cái (vì die Oper). Đi tới: zur Staatsoper.', 'Heute Abend besuchen wir eine berühmte Oper in der Staatsoper.', 'Tối nay chúng tôi đi xem một vở nhạc kịch nổi tiếng ở Nhà hát Opera Quốc gia.'),
        ('Friedrichstraße', 'die', 'die', 'nur Singular', 'eine Friedrichstraße', 'keine Friedrichstraße', 'Phố mua sắm Friedrich', cat2, 'Con phố thương mại sầm uất tại Berlin mang giống cái (vì die Straße). Đi dọc phố: die Friedrichstraße entlang.', 'Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.', 'Tiếp sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.'),
        ('Museumsinsel', 'die', 'die', 'nur Singular', 'eine Museumsinsel', 'keine Museumsinsel', 'Đảo Bảo tàng Berlin', cat2, 'Quần thể viện bảo tàng nổi tiếng thế giới mang giống cái (vì die Insel - hòn đảo).', 'Auf der Museumsinsel besichtigen wir berühmte Kunstwerke.', 'Trên Đảo Bảo tàng chúng tôi tham quan các tác phẩm nghệ thuật nổi tiếng.'),
        ('Alte Nationalgalerie', 'die', 'die', 'die Alten Nationalgalerien', 'eine Alte Nationalgalerie', 'keine Alte Nationalgalerie', 'Khu triển lãm Quốc gia Cũ', cat2, 'Hậu tố -ie luôn mang giống cái (die Galerie). Đi vào: in die Alte Nationalgalerie.', 'Danach will ich in die Alte Nationalgalerie gehen.', 'Sau đó tôi muốn đi vào Khu triển lãm Quốc gia Cũ.'),
        ('Bundeskanzleramt', 'das', 'das', 'die Bundeskanzlerämter', 'ein Bundeskanzleramt', 'kein Bundeskanzleramt', 'Phủ Thủ tướng Liên bang', cat2, 'Danh lam thắng cảnh mang giống trung (vì das Amt - cơ quan).', 'Sie fahren mit dem Bus am Bundeskanzleramt vorbei.', 'Họ đi xe buýt ngang qua Phủ Thủ tướng Liên bang.'),
        ('Brandenburger Tor', 'das', 'das', 'nur Singular', 'ein Brandenburger Tor', 'kein Brandenburger Tor', 'Cổng thành Brandenburg', cat2, 'Biểu tượng lịch sử nước Đức mang giống trung (vì das Tor). Đi tới: zum Brandenburger Tor.', 'Sie gehen zum Brandenburger Tor und machen viele Fotos.', 'Họ đi đến Cổng Brandenburg và chụp nhiều bức ảnh.'),
        ('Schloss Bellevue', 'das', 'das', 'nur Singular', 'ein Schloss Bellevue', 'kein Schloss Bellevue', 'Cung điện Bellevue', cat2, 'Dinh thự Tổng thống Đức mang giống trung (vì das Schloss).', 'Das Schloss Bellevue liegt mitten im Tiergarten an der Spree.', 'Cung điện Bellevue nằm giữa công viên Tiergarten bên bờ sông Spree.'),
        ('Sony Center', 'das', 'das', 'nur Singular', 'ein Sony Center', 'kein Sony Center', 'Trung tâm phức hợp Sony Center', cat2, 'Khu phức hợp hiện đại tại Potsdamer Platz mang giống trung (vì das Center).', 'Im Sony Center gibt es viele Restaurants, Kinos und Geschäfte.', 'Trong Sony Center có rất nhiều nhà hàng, rạp chiếu phim và cửa hàng.'),

        # 6 Direction & Action
        ('geradeaus', '', '', None, None, None, 'đi thẳng', cat1, 'Trạng từ chỉ hướng: geradeaus gehen (đi thẳng).', 'Gehen Sie bitte 200 Meter geradeaus!', 'Xin Ngài hãy đi thẳng 200 mét!'),
        ('vorbei', '', '', None, None, None, 'ngang qua', cat1, 'Giới từ phối hợp: an + Dativ + vorbei (đi ngang qua bên cạnh tòa nhà).', 'Er geht an der Bank vorbei.', 'Anh ấy đi ngang qua ngân hàng.'),
        ('entlang', '', '', None, None, None, 'dọc theo', cat1, 'Đứng SAU danh từ ở Akkusativ: die Straße entlang (dọc theo con đường).', 'Laufen Sie den Fluss entlang!', 'Ngài hãy đi dọc theo con sông!'),
        ('über', '', '', None, None, None, 'băng qua, vượt qua trên mặt', cat1, 'Giới từ đi với Akkusativ khi có chuyển động: über die Brücke (qua cầu), über den Platz (qua quảng trường).', 'Wir gehen über die Brücke.', 'Chúng tôi đi qua cây cầu.'),
        ('durch', '', '', None, None, None, 'xuyên qua', cat1, 'Giới từ luôn đi với Akkusativ: durch das Tor (qua cổng), durch den Park (qua công viên).', 'Die Touristen gehen durch das Tor.', 'Các du khách đi xuyên qua cánh cổng.'),
        ('bummeln', '', '', None, None, None, 'đi dạo phố, tản bộ ngắm cảnh', cat1, 'Động từ thường đi với auf / durch: auf der Straße bummeln.', 'Am Nachmittag wollen wir im Zentrum bummeln.', 'Buổi chiều chúng tôi muốn đi dạo phố ở trung tâm.')
    ]

    vocab_list = []
    for item in vocab_raw:
        word, article, gender, plural, indef, neg, meaning, category, notes, ex_de, ex_vi = item
        vocab_list.append({
            "word": word,
            "article": article if article else None,
            "gender": gender if gender else None,
            "plural": plural,
            "indefinite": indef,
            "negation": neg,
            "akkusativ": (("den " if article == 'der' else ("die " if article == 'die' else ("das " if article == 'das' else ""))) + word).strip() if article else word,
            "meaning": meaning,
            "category": category,
            "notes": notes,
            "example": ex_de,
            "example_vi": ex_vi
        })

    ex_list = []

    # =========================================================================
    # NHÓM 1: TRẮC NGHIỆM THỰC CHIẾN BẢN ĐỒ & TỪ VỰNG (18 CÂU: Q1 -> Q18)
    # =========================================================================
    mcqs = [
        # --- CÂU 1 (Tourist, START → Kino) ---
        (
            """Câu 1: Một du khách đứng ở điểm START và hỏi đường. Hãy đọc lời chỉ đường, đối chiếu với bản đồ và chọn nơi du khách đang tìm.
„Gehen Sie zuerst geradeaus über die erste Kreuzung! An der zweiten Kreuzung biegen Sie rechts ab. Gehen Sie dann am Krankenhaus vorbei bis zur Ampel. Direkt hinter der Ampel liegt das Gebäude links.“""",
            [
                "Das Schloss",
                "Das Kino",
                "Die Post",
                "Der Bahnhof"
            ],
            "Das Kino",
            "Từ START đi thẳng qua ngã tư 1 → ngã tư 2 rẽ phải (vào Behrenstr.) → đi qua Krankenhaus ('am Krankenhaus vorbei') tới Ampel ('bis zur Ampel') → ngay sau Ampel, bên trái là Kino.",
            {
                "visual_svg": "map_route_finder_1",
                "translation": "Đầu tiên bạn hãy đi thẳng qua ngã tư thứ nhất! Ở ngã tư thứ hai bạn hãy rẽ phải. Sau đó bạn đi qua bệnh viện cho đến đèn giao thông. Ngay phía sau đèn giao thông là tòa nhà ở bên trái."
            }
        ),

        # --- CÂU 2 (Jonas, đường xanh → Einkaufszentrum) ---
        (
            "Câu 2: Bạn của bạn là Jonas muốn đến Einkaufszentrum. Lời chỉ đường nào khớp chính xác với lộ trình màu xanh trên bản đồ?",
            [
                "Geh geradeaus und nimm die zweite Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                "Geh geradeaus und nimm die dritte Straße rechts. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                "Geh geradeaus und nimm die dritte Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
                "Geh geradeaus und nimm die dritte Straße links. Geh durch den Park und dann über die Brücke. Das Einkaufszentrum liegt rechts."
            ],
            "Geh geradeaus und nimm die dritte Straße links. Geh über die Brücke und dann durch den Park. Das Einkaufszentrum liegt rechts.",
            "Thứ tự trên bản đồ là đi thẳng → ngã tư thứ 3 rẽ trái → qua cầu ('über die Brücke') → xuyên công viên ('durch den Park') → Einkaufszentrum bên phải. Câu 'nimm die zweite Straße links' sai vì ngã rẽ thực tế là đường thứ ba. Câu 'dritte Straße rechts' sai vì đường rẽ sang bên trái. Câu 'durch den Park und dann über die Brücke' sai thứ tự vì trên lộ trình bạn đi qua cầu trước rồi mới đi xuyên qua công viên.",
            {
                "visual_svg": "map_route_line_2",
                "translation": "Bạn hãy đi thẳng và đi vào con đường thứ ba bên trái. Hãy đi qua cầu và sau đó đi xuyên qua công viên. Trung tâm thương mại nằm ở bên phải."
            }
        ),

        # --- CÂU 3 (3 hình 1→2→3) ---
        (
            "Câu 3: Chọn chuỗi câu tiếng Đức mô tả đúng ba hình (1 → 2 → 3) và hoàn toàn đúng ngữ pháp.",
            [
                "Zuerst gehen wir an die Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                "Zuerst gehen wir am Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                "Zuerst gehen wir an der Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
                "Zuerst gehen wir durch das Stadttor, dann an der Staatsoper vorbei und danach den Fluss entlang."
            ],
            "Zuerst gehen wir an der Staatsoper vorbei, dann durch das Stadttor und danach den Fluss entlang.",
            "(1) die Staatsoper (giống cái) → 'an der Staatsoper vorbei' (an + Dativ). (2) das Stadttor (giống trung) → 'durch das Stadttor' (durch + Akkusativ). (3) der Fluss (giống đực) → 'den Fluss entlang' (entlang đặt sau danh từ + Akkusativ). Thứ tự khớp hình 1 → 2 → 3. Đáp án 'Zuerst gehen wir durch das Stadttor, dann an der Staatsoper vorbei und danach den Fluss entlang' tuy đúng ngữ pháp nhưng sai thứ tự so với các hình (hình 1 là Staatsoper, hình 2 là Stadttor).",
            {
                "visual_svg": "quiz_spatial_3_steps",
                "translation": "Đầu tiên chúng ta đi ngang qua Nhà hát Opera, sau đó đi xuyên qua cổng thành và tiếp theo đi dọc theo dòng sông."
            }
        ),

        # --- CÂU 4 (câu hỏi SAI ngữ pháp) ---
        (
            "Câu 4: Một bà cụ hỏi bạn đường trên phố ở Berlin. Câu hỏi nào dưới đây SAI ngữ pháp?",
            [
                "Entschuldigung, wo finde ich das Bundeskanzleramt?",
                "Entschuldigung, wie komme ich zum Museumsinsel?",
                "Entschuldigung, wo ist hier eine Bank?",
                "Entschuldigung, wo geht es hier zum Hauptbahnhof?"
            ],
            "Entschuldigung, wie komme ich zum Museumsinsel?",
            "die Museumsinsel là danh từ giống cái (vì die Insel) → khi hỏi đường dùng cấu trúc zu + Dativ, zu + der biến thành 'zur Museumsinsel', không thể dùng 'zum' (câu đúng phải là: 'Entschuldigung, wie komme ich zur Museumsinsel?'). Câu hỏi 'wo geht es hier zum Hauptbahnhof?' là đúng ngữ pháp vì der Hauptbahnhof là danh từ giống đực → zu + dem = zum.",
            {
                "translation": "Xin lỗi, làm thế nào tôi đến được Đảo Bảo tàng?"
            }
        ),

        # --- CÂU 5 (Clara và Tim → Rathaus) ---
        (
            """Câu 5: Bạn chỉ đường cho Clara và Tim trên bản đồ. Chọn đáp án điền đúng vào các chỗ trống.
„Clara und Tim suchen das historische Rathaus. Du erklärst ihnen den Weg: ‚Geht zuerst ___ Humboldt-Universität und ___ Berliner Dom vorbei, dann geradeaus bis ___ Ampel und über ___ Marktplatz!‘“""",
            [
                "an der / am / zum / den",
                "an der / am / zur / dem",
                "an der / am / zur / den",
                "am / an der / zur / den"
            ],
            "an der / am / zur / den",
            "die Humboldt-Universität (giống cái) → 'an der Humboldt-Universität vorbei' (an + Dativ); der Berliner Dom (giống đực) → 'am Berliner Dom vorbei' (an + dem = am); die Ampel (giống cái) → 'bis zur Ampel' (zu + der = zur); der Marktplatz (giống đực) đi với 'über + Akkusativ' khi chỉ hướng di chuyển → 'über den Marktplatz'.",
            {
                "visual_svg": "map_route_line_3",
                "translation": "Clara và Tim đang tìm tòa thị chính lịch sử. Bạn giải thích đường đi cho họ: 'Đầu tiên các bạn hãy đi qua Đại học Humboldt và đi qua Nhà thờ lớn Berlin, sau đó đi thẳng cho đến đèn giao thông và đi băng qua quảng trường chợ!'"
            }
        ),

        # --- CÂU 6 (cùng mạo từ) ---
        (
            "Câu 6: Hàng nào có cả 4 danh từ cùng một mạo từ xác định ở số ít?",
            [
                "Staatsoper – Brücke – Stadttor – Friedrichstraße",
                "Schloss – Einkaufszentrum – Bank – Bundeskanzleramt",
                "Reichstag – Hafen – Fernsehturm – Potsdamer Platz",
                "Bahnhof – Markt – Museumsinsel – Zoo"
            ],
            "Reichstag – Hafen – Fernsehturm – Potsdamer Platz",
            "Hàng 'Reichstag – Hafen – Fernsehturm – Potsdamer Platz' đều là danh từ giống đực mang mạo từ 'der' (der Reichstag, der Hafen, der Fernsehturm, der Potsdamer Platz). Hàng có Staatsoper lẫn 'das Stadttor' (còn lại là die). Hàng có Schloss lẫn 'die Bank' (còn lại là das). Hàng có Bahnhof lẫn 'die Museumsinsel' (còn lại là der).",
            {
                "translation": "Tòa nhà Quốc hội – cảng – tháp truyền hình – Quảng trường Potsdam."
            }
        ),

        # --- CÂU 7 (số nhiều) ---
        (
            "Câu 7: Câu nào dưới đây mô tả một đại đô thị châu Âu và dùng ĐÚNG tất cả các dạng số nhiều?",
            [
                "In dieser Metropole gibt es drei Flughäfe, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks.",
                "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks.",
                "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentrums und viele grüne Parks.",
                "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parken."
            ],
            "In dieser Metropole gibt es drei Flughäfen, vier alte Schlösser, zwei große Einkaufszentren und viele grüne Parks.",
            "der Flughafen → die Flughäfen (chỉ biến âm a → ä, không thêm đuôi vì Flughafen đã kết thúc bằng -en); das Schloss → die Schlösser (biến âm + đuôi -er); das Einkaufszentrum → die Einkaufszentren (đuôi -um đổi thành -en); der Park → die Parks (từ vay mượn nước ngoài, số nhiều thêm -s).",
            {
                "translation": "Ở đại đô thị này có ba sân bay, bốn lâu đài cổ, hai trung tâm thương mại lớn và nhiều công viên xanh mát."
            }
        ),
        # --- CÂU 8 (Banken / Bänken) ---
        (
            """Câu 8: Chọn đáp án điền đúng vào hai chỗ trống.
‚In der Innenstadt arbeiten viele Menschen in den internationalen ___, und im Stadtpark sitzen die Rentner gern auf den sonnigen ___.‘""",
            [
                "Banken / Banken",
                "Banken / Bänken",
                "Bänken / Bänken",
                "Banken / Bänke"
            ],
            "Banken / Bänken",
            "Cùng một từ 'die Bank' nhưng hai nghĩa có hai số nhiều khác nhau: ngân hàng → 'die Banken'; ghế băng → 'die Bänke' (có Umlaut). Sau 'in den' và 'auf den' (Dativ số nhiều) danh từ phải có đuôi -n: 'in den Banken' (đã có sẵn -n), 'auf den Bänken'. Đáp án 'Banken' cho ghế băng thiếu Umlaut; 'Bänken' cho ngân hàng dùng sai dạng; 'Bänke' thiếu đuôi -n ở Dativ số nhiều.",
            {"translation": "Ở khu trung tâm thành phố, nhiều người làm việc trong các ngân hàng quốc tế, còn trong công viên thành phố, những người về hưu thích ngồi trên những chiếc ghế băng đầy nắng."}
        ),
        # --- CÂU 9 (Staatsoper / Alexanderplatz) ---
        (
            """Câu 9: Chọn đáp án điền đúng vào ba chỗ trống.
Am Samstagabend möchten meine Cousine und ich ___ Staatsoper gehen, denn dann singt ein berühmter Tenor ___ Staatsoper. Davor fahren wir noch kurz ___ Alexanderplatz.""",
            [
                "in die / in der / zum",
                "in der / in der / zum",
                "in die / in die / zum",
                "in die / in der / zur"
            ],
            "in die / in der / zum",
            "Động từ 'gehen' chỉ hướng di chuyển vào trong (Wohin?) với 'die Staatsoper' đi với in + Akkusativ → 'in die Staatsoper'; 'singen' chỉ hành động diễn ra tại chỗ (Wo?) đi với in + Dativ → 'in der Staatsoper'; 'der Alexanderplatz' đi với zu + Dativ → 'zu + dem = zum'. Các đáp án có 'in der' sau 'gehen' hoặc 'in die' sau 'singt' sai vì nhầm hướng di chuyển với vị trí; 'zur' sai vì Alexanderplatz là danh từ giống đực.",
            {"translation": "Tối thứ Bảy, em họ (hoặc chị họ) của tôi và tôi muốn đi vào Nhà hát Opera Quốc gia, vì lúc đó một giọng nam cao nổi tiếng sẽ hát trong nhà hát. Trước đó chúng tôi còn ghé nhanh tới Quảng trường Alexander."}
        ),
        # --- CÂU 10 (Reiseleiter Spree / Brücke / Tunnel) ---
        (
            """Câu 10: Một hướng dẫn viên du lịch nói với đoàn khách. Chọn đáp án điền đúng vào ba chỗ trống.
‚Wir spazieren jetzt zuerst die Spree ___, gehen dann ___ die alte Holzbrücke und laufen schließlich ___ den dunklen Tunnel zum Schloss.‘""",
            [
                "vorbei / über / in",
                "über / durch / entlang",
                "entlang / über / durch",
                "durch / entlang / über"
            ],
            "entlang / über / durch",
            "Đi dọc theo dòng sông Spree (đặt sau danh từ) dùng 'entlang' ('die Spree entlang'); đi vượt qua trên mặt cầu dùng 'über' ('über die alte Holzbrücke'); đi xuyên qua lòng đường hầm tối ('der Tunnel') dùng 'durch' ('durch den dunklen Tunnel'). Các đáp án khác sai vì dùng nhầm giới từ hoặc đảo lộn thứ tự không khớp với từng chặng di chuyển.",
            {"translation": "Hướng dẫn viên du lịch nói với các vị khách: 'Bây giờ đầu tiên chúng ta đi dạo dọc theo sông Spree, sau đó đi qua cây cầu gỗ cổ và cuối cùng đi bộ xuyên qua đường hầm tối để tới cung điện.'"}
        ),
        # --- CÂU 11 (Familie Schneider) ---
        (
            """Câu 11: Một gia đình đang du lịch ở München. Chọn đáp án điền đúng vào ba chỗ trống.
Familie Schneider ist neu in München. Herr Schneider ___ unbedingt das Deutsche Museum besichtigen, aber seine Kinder sind müde und ___ không mehr weit laufen. Deshalb ___ alle jetzt ein Taxi zum Hotel nehmen.""".replace("không", "nicht"),
            [
                "will / können / müssen",
                "wollen / können / müssen",
                "will / kann / müssen",
                "will / können / muss"
            ],
            "will / können / müssen",
            "Chủ ngữ 'Herr Schneider' (ngôi er số ít) → 'will'; 'seine Kinder' (ngôi sie số nhiều) → 'können'; 'alle' (đại từ làm chủ ngữ số nhiều) → 'müssen'. Các đáp án khác sai vì chia động từ không khớp chủ ngữ: 'wollen' với 'Herr Schneider', 'kann' với 'seine Kinder', 'muss' với 'alle'.",
            {"translation": "Gia đình Schneider mới đến München. Ông Schneider nhất định muốn tham quan Bảo tàng Đức, nhưng các con của ông đã mỏi chân và không thể đi bộ xa thêm nữa. Vì vậy bây giờ tất cả họ phải bắt một chiếc taxi về khách sạn."}
        ),
        # --- CÂU 12 (Chỉ đường Theater - bản đồ lỗi hướng) ---
        (
            "Câu 12: Một người qua đường chỉ đường tới Theater cho bạn, dựa theo bản đồ. Trong câu nào người đó nói SAI hướng so với lộ trình vẽ trên bản đồ?",
            [
                "Gehen Sie zuerst geradeaus über die erste Kreuzung.",
                "An der zweiten Kreuzung biegen Sie links ab.",
                "Danach gehen Sie an der Kirche vorbei, die links von Ihnen liegt.",
                "Dann biegen Sie noch einmal rechts ab, und das Theater liegt direkt vor Ihnen."
            ],
            "Danach gehen Sie an der Kirche vorbei, die links von Ihnen liegt.",
            "Trên bản đồ, đường đi thẳng qua ngã tư thứ nhất, rẽ trái ở ngã tư thứ hai rồi đi dọc theo đường ngang. Nhà thờ (Kirche) nằm phía trên đường, tức bên PHẢI người đi ('rechts'), nhưng câu này lại nói 'links'. Ba câu còn lại khớp với lộ trình.",
            {
                "visual_svg": "map_error_check_1",
                "translation": "Một người qua đường chỉ đường tới Theater cho bạn, dựa theo bản đồ. Trong câu nào người đó nói SAI hướng so với lộ trình vẽ trên bản đồ? — Người qua đường nói sai hướng của nhà thờ."
            }
        ),
        # --- CÂU 13 (Hỏi đường Hauptbahnhof / Kirche) ---
        (
            """Câu 13: Du khách hỏi đường ở trung tâm thành phố. Chọn đáp án điền đúng vào ba chỗ trống.
‚Entschuldigung, wir suchen ___ neuen Hauptbahnhof.‘ — ‚Gehen Sie einfach an ___ alten Kirche vorbei, dann steht ___ Hauptbahnhof direkt vor Ihnen!‘""",
            [
                "den / der / der",
                "dem / der / der",
                "den / die / der",
                "den / der / den"
            ],
            "den / der / der",
            "1. Động từ 'suchen' đòi hỏi tân ngữ trực tiếp ở Akkusativ; 'der Hauptbahnhof' (giống đực) đổi thành 'den neuen Hauptbahnhof'. 2. Cụm giới từ 'an … vorbei' luôn đi với Dativ; 'die Kirche' (giống cái) đổi thành 'an der alten Kirche vorbei'. 3. Trong mệnh đề 'dann steht ___ Hauptbahnhof', danh từ làm chủ ngữ ở Nominativ nên giữ nguyên mạo từ 'der Hauptbahnhof'. Các đáp án khác sai vì: 'dem' sai vì sau 'suchen' cần Akkusativ; 'die' sai vì 'an … vorbei' cần Dativ; 'den' ở chỗ thứ ba sai vì chủ ngữ của 'steht' ở Nominativ.",
            {"translation": "'Xin lỗi, chúng tôi đang tìm nhà ga trung tâm mới.' — 'Quý vị cứ đi ngang qua nhà thờ cổ, sau đó nhà ga trung tâm sẽ nằm ngay trước mặt quý vị!'"}
        ),
        # --- CÂU 14 (Taxi ở Wien) ---
        (
            """Câu 14: Một hành khách và một tài xế taxi ở Viên trò chuyện. Chọn đáp án điền đúng vào hai chỗ trống.
Taxifahrer: Muss ich hier schon abbiegen?
Fahrgast: Nein, fahren Sie bitte erst die ___ Straße links und halten Sie dann an der ___ Ampel vor dem Theater!""",
            [
                "dritten / zweiten",
                "dritte / zweiten",
                "dritte / zweite",
                "dritter / zweiten"
            ],
            "dritte / zweiten",
            "Số thứ tự đứng sau 'die' (giống cái ở Akkusativ) nhận đuôi -e ('die dritte Straße'); đứng sau 'an der' (giống cái ở Dativ) nhận đuôi -en ('an der zweiten Ampel'). Đáp án 'dritten' sai vì Akkusativ giống cái nhận đuôi -e; 'zweite' sai vì Dativ giống cái phải nhận đuôi -en; 'dritter' sai vì đây không phải biến cách mạnh không có mạo từ.",
            {"translation": "Tài xế taxi: 'Tôi phải rẽ ngay ở đây à?' — Hành khách: 'Không, trước tiên xin hãy đi vào con đường thứ ba bên trái, rồi dừng lại ở đèn giao thông thứ hai trước nhà hát!'"}
        ),
        # --- CÂU 15 (Trật tự từ) ---
        (
            "Câu 15: Chọn câu có trật tự từ đúng duy nhất.",
            [
                "Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder Eis essen.",
                "Zuerst wir wollen den großen Hafen besichtigen, und danach möchten die Kinder Eis essen.",
                "Zuerst wollen wir den großen Hafen besichtigen, und danach die Kinder möchten Eis essen.",
                "Zuerst wollen besichtigen wir den großen Hafen, und danach möchten die Kinder Eis essen."
            ],
            "Zuerst wollen wir den großen Hafen besichtigen, und danach möchten die Kinder Eis essen.",
            "Khi trạng từ thời gian ('Zuerst', 'danach') đứng đầu câu hoặc đầu mệnh đề, động từ đã chia ('wollen', 'möchten') phải đứng ngay sau nó, còn động từ nguyên mẫu ('besichtigen', 'essen') đứng ở cuối câu. Liên từ 'und' kết nối hai mệnh đề độc lập mà không thay đổi trật tự từ. Các đáp án sai vì: câu thứ hai đặt 'wir' trước động từ; câu thứ ba đặt 'die Kinder' trước động từ ở mệnh đề sau 'und'; câu thứ tư đặt 'besichtigen' sai chỗ, phải ở cuối mệnh đề.",
            {"translation": "Đầu tiên chúng tôi muốn tham quan cảng lớn, và sau đó bọn trẻ muốn ăn kem."}
        ),
        # --- CÂU 16 (Đi Schloss Sanssouci) ---
        (
            """Câu 16: Ông bà của bạn cần đi từ khách sạn tới cung điện Sanssouci vào ngày mai. Chọn đáp án điền đúng vào bốn chỗ trống.
Wie kommen deine Großeltern morgen vom Hotel zum Schloss Sanssouci? — Sie fahren zuerst mit ___ S-Bahn bis ___ Hauptbahnhof und nehmen dort ___ Bus direkt ___ Schloss.""",
            [
                "die / zum / den / zum",
                "der / zur / den / zum",
                "der / zum / den / zum",
                "der / zum / dem / zum"
            ],
            "der / zum / den / zum",
            "1. 'mit' luôn đi với Dativ: 'die S-Bahn' → 'mit der S-Bahn'. 2. 'bis zu' đi với Dativ: 'der Hauptbahnhof' → 'bis zum Hauptbahnhof'. 3. 'nehmen' cần tân ngữ Akkusativ: 'der Bus' → 'nehmen den Bus'. 4. 'zu + Dativ': 'das Schloss' → 'zum Schloss'. Các đáp án khác sai vì: 'die' sau 'mit' sai do 'mit' luôn đi với Dativ; 'zur Hauptbahnhof' sai vì der Hauptbahnhof giống đực; 'dem Bus' sai vì 'nehmen' cần Akkusativ.",
            {"translation": "Ông bà của bạn ngày mai đi từ khách sạn đến Cung điện Sanssouci bằng cách nào? — Đầu tiên ông bà đi bằng tàu điện S-Bahn cho đến nhà ga trung tâm và ở đó bắt xe buýt đi thẳng tới cung điện."}
        ),
        # --- CÂU 17 (Tài xế hỏi đường đi sân bay) ---
        (
            "Câu 17: Một tài xế ô tô hỏi bạn cách đi ra sân bay. Chọn câu trả lời vừa hợp logic vừa đúng ngữ pháp.",
            [
                "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!",
                "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Hauptbahnhof!",
                "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach die zweite Ampel rechts zum Flughafen!",
                "Gehen Sie zu Fuß diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!"
            ],
            "Fahren Sie diese Hauptstraße entlang, dann über die große Brücke und nach der zweiten Ampel rechts zum Flughafen!",
            "Tài xế đang điều khiển ô tô nên dùng động từ 'Fahren Sie...', đi dọc đường chính ('diese Hauptstraße entlang'), qua trên cây cầu ('über die große Brücke'), sau đèn giao thông thứ hai ('nach der zweiten Ampel' vì nach + Dativ) và đích đến đúng câu hỏi là sân bay ('zum Flughafen'). Các câu còn lại sai vì: một câu chỉ nhầm đích đến là nhà ga trung tâm; một câu sai ngữ pháp 'nach die zweite Ampel'; một câu sai logic thực tế vì bảo người đang lái xe hãy đi bộ ('Gehen Sie zu Fuß').",
            {"translation": "Một tài xế ô tô hỏi bạn cách đi ra sân bay. Câu trả lời nào vừa hợp logic thực tế vừa đúng ngữ pháp?"}
        ),
        # --- CÂU 18 (Bảng thông tin nhà ga / Friedrichsbrücke) ---
        (
            """Câu 18: Đọc bảng thông tin tại nhà ga rồi trả lời câu hỏi.
‚Vom Hauptbahnhof erreichen Sie die Museumsinsel in 15 Minuten zu Fuß: Gehen Sie durch den Bahnhofspark, über die Friedrichsbrücke und an der Staatsoper vorbei.‘
Khách tham quan phải làm gì trên quãng đường này?""",
            [
                "Sie müssen vor der Brücke links zum großen Flughafen abbiegen.",
                "Sie müssen einen Park durchqueren und eine Brücke überqueren.",
                "Sie müssen mit dem Linienbus direkt in die Staatsoper hineingehen.",
                "Sie dürfen den schönen Bahnhofspark auf keinen Fall betreten."
            ],
            "Sie müssen einen Park durchqueren und eine Brücke überqueren.",
            "'durch den Bahnhofspark gehen' tương đương với 'einen Park durchqueren' (đi xuyên qua công viên); 'über die Friedrichsbrücke gehen' tương đương với 'eine Brücke überqueren' (băng qua cầu). Các đáp án khác sai vì bảng thông tin không hề yêu cầu rẽ trái ra sân bay, không bảo đi xe buýt vào nhà hát, và cũng không cấm khách bước vào công viên.",
            {"translation": "Đọc bảng thông tin tại nhà ga: 'Từ nhà ga trung tâm, quý vị đi bộ 15 phút là tới Đảo Bảo tàng: Hãy đi xuyên qua công viên nhà ga, đi qua cầu Friedrichs và đi ngang qua Nhà hát Opera Quốc gia.' — Khách tham quan phải làm gì trên quãng đường này?"}
        )
    ]

    for q, opts, ans, exp, extra in mcqs:
        extra_data = {
            "accepted_answers": [ans],
            "translation": extra.get("translation", "")
        }
        if "visual_svg" in extra:
            extra_data["visual_svg"] = extra["visual_svg"]
        ex_list.append({
            "type": "trac_nghiem",
            "question": q,
            "options": opts,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": extra_data
        })

    # =========================================================================
    # NHÓM 2: ĐIỀN KHUYẾT CHUYÊN SÂU (15 CÂU: Q19 -> Q33)
    # =========================================================================
    fill_ins = [
        (
            "Câu 19: „Entschuldigung, wie komme ich zum Krankenhaus?“ — „Gehen Sie zuerst geradeaus an ___ Bank vorbei und biegen Sie dann links ab!“",
            "der",
            ["der"],
            "Danh từ Bank mang giống cái ('die Bank'). Trong cấu trúc 'an + Dativ + vorbei', mạo từ die đổi thành 'der' ('an der Bank vorbei').",
            {"visual_svg": "map_fill_1", "translation": "Xin lỗi, làm thế nào tôi đi đến được bệnh viện? — Đầu tiên Ngài hãy đi thẳng ngang qua ngân hàng rồi sau đó rẽ trái!"}
        ),
        (
            "Câu 20: „Fährt dieser Bus zum Kunstmuseum?“ — „Ja, er fährt direkt ___ alten Schloss vorbei und hält dann vor dem Museum.“",
            "am",
            ["am", "an dem"],
            "Danh từ Schloss mang giống trung ('das Schloss'). Đi với cấu trúc 'an + Dativ + vorbei', an + dem gộp thành 'am' ('am alten Schloss vorbei').",
            {"visual_svg": "map_fill_2", "translation": "Chuyến xe buýt này có chạy tới bảo tàng nghệ thuật không? — Có, nó chạy ngang qua ngay cung điện cổ rồi dừng trước bảo tàng."}
        ),
        (
            "Câu 21: „Um zur Museumsinsel zu kommen, müsst ihr zuerst ___ die große Brücke laufen.“",
            "über",
            ["über", "ueber"],
            "Đi vượt qua / băng qua mặt cầu ('die Brücke') dùng giới từ 'über' (+ Akkusativ).",
            {"visual_svg": "quiz_icon_bridge", "translation": "Để đi đến được Đảo Bảo tàng, đầu tiên các bạn phải đi bộ qua cây cầu lớn."}
        ),
        (
            "Câu 22: „Wenn du in die Altstadt willst, musst du zu Fuß ___ das historische Stadttor gehen.“",
            "durch",
            ["durch", "durchs"],
            "Đi xuyên qua lòng cổng thành ('das Stadttor') dùng giới từ 'durch' (+ Akkusativ).",
            {"visual_svg": "quiz_icon_gate", "translation": "Nếu bạn muốn vào khu phố cổ, bạn phải đi bộ xuyên qua cổng thành lịch sử."}
        ),
        (
            "Câu 23: „Gehen Sie einfach diese breite Straße ___! Nach etwa dreihundert Metern sehen Sie links den Zoo.“",
            "entlang",
            ["entlang"],
            "Từ chỉ hướng đi dọc theo đứng sau danh từ ở Akkusativ ('diese breite Straße') là 'entlang'.",
            {"visual_svg": "quiz_icon_along", "translation": "Ngài cứ đi dọc theo con đường rộng này! Sau khoảng ba trăm mét Ngài sẽ nhìn thấy sở thú ở bên trái."}
        ),
        (
            "Câu 24: „Fahren Sie mit dem Fahrrad immer geradeaus bis ___ dritten Kreuzung und biegen Sie dort rechts ab!“",
            "zur",
            ["zur", "zu der"],
            "Danh từ Kreuzung mang giống cái ('die Kreuzung'). Sau giới từ kép 'bis zu + Dativ', zu + der viết tắt thành 'zur' ('bis zur dritten Kreuzung').",
            {"translation": "Ngài cứ đạp xe thẳng mãi cho đến ngã tư thứ ba và rẽ phải ở đó!"}
        ),
        (
            "Câu 25: „Wie weit fährt die Straßenbahn Linie 4?“ — „Sie fährt vom Rathaus durch das Zentrum bis ___ Hafen.“",
            "zum",
            ["zum", "zu dem"],
            "Danh từ Hafen (cảng biển) mang giống đực ('der Hafen'). Sau 'bis zu + Dativ', zu + dem viết tắt thành 'zum' ('bis zum Hafen').",
            {"translation": "Tuyến tàu điện mặt đất số 4 chạy bao xa? — Nó chạy từ tòa thị chính xuyên qua trung tâm cho đến cảng biển."}
        ),
        (
            "Câu 26: „Es regnet stark! Komm, wir gehen schnell ___ Einkaufszentrum dort drüben und trinken einen heißen Kakao!“",
            "ins",
            ["ins", "in das"],
            "Danh từ Einkaufszentrum mang giống trung ('das Einkaufszentrum'). Đi bước vào bên trong ('Wohin?' + Akkusativ) dùng in + das = 'ins'.",
            {"translation": "Trời mưa to quá! Nào, chúng mình đi nhanh vào trong trung tâm thương mại ở đằng kia và uống một cốc ca cao nóng đi!"}
        ),
        (
            "Câu 27: „Meine Tante interessiert sich sehr für Kunst, deshalb geht sie heute Nachmittag ___ Alte Nationalgalerie.“",
            "in die",
            ["in die"],
            "'Alte Nationalgalerie' mang giống cái ('die'). Đi vào bên trong ('Wohin?' + Akkusativ) dùng 'in die'.",
            {"translation": "Cô của tôi rất quan tâm đến nghệ thuật, vì vậy chiều nay cô ấy đi vào Khu triển lãm Quốc gia Cũ."}
        ),
        (
            "Câu 28: „Das Wetter ist heute wunderbar. Gehen wir am Nachmittag mit den Kindern ___ großen Stadtpark oder lieber in den Zoo?“",
            "in den",
            ["in den"],
            "Danh từ Stadtpark ('der Park') mang giống đực. Khi chỉ hướng đi vào ('Wohin?' + Akkusativ), der đổi thành den -> 'in den'.",
            {"translation": "Thời tiết hôm nay tuyệt đẹp. Chiều nay chúng ta đi cùng bọn trẻ vào công viên lớn của thành phố hay đi vào sở thú hơn?"}
        ),
        (
            "Câu 29: „Mein Onkel fotografiert sehr gern. In Berlin ___ er unbedingt auf den Fernsehturm fahren und die Stadt von oben fotografieren.“",
            "will",
            ["will"],
            "Chủ ngữ 'er' ('mein Onkel') là ngôi thứ 3 số ít; động từ khuyết thiếu wollen biến âm o -> i và không có đuôi thành 'will'.",
            {"translation": "Chú của tôi rất thích chụp ảnh. Ở Berlin chú ấy nhất định muốn đi lên Tháp truyền hình và chụp ảnh thành phố từ trên cao."}
        ),
        (
            "Câu 30: „Hallo Leon, hallo Mia! Ihr seid schon am Alexanderplatz. Was ___ ihr denn danach noch in der Innenstadt unternehmen?“",
            "wollt",
            ["wollt"],
            "Với chủ ngữ ngôi thứ 2 số nhiều 'ihr' (các bạn), động từ wollen chia thành 'wollt'.",
            {"translation": "Chào Leon, chào Mia! Hai bạn đã ở Quảng trường Alexander rồi. Thế sau đó hai bạn còn muốn làm gì ở khu trung tâm thành phố nữa?"}
        ),
        (
            "Câu 31: „Geh einfach über die kleine Brücke und dann 100 Meter geradeaus! Direkt auf der linken Seite ___ du schon die gelbe Post.“",
            "siehst",
            ["siehst"],
            "Động từ sehen (nhìn thấy) là động từ mạnh biến âm e -> ie ở ngôi du ('du siehst') và er/sie/es ('er sieht'). Vì chỉ đường cho bạn ở ngôi du, đáp án đúng là 'siehst'.",
            {"translation": "Cậu cứ đi qua cây cầu nhỏ rồi đi thẳng 100 mét! Ngay ở phía bên tay trái cậu sẽ nhìn thấy bưu điện màu vàng."}
        ),
        (
            "Câu 32: „Nimm am besten die Buslinie 100! Dieser Bus ___ am Reichstag, am Brandenburger Tor und am Schloss Bellevue vorbei.“",
            "fährt",
            ["fährt", "faehrt"],
            "Chủ ngữ 'Dieser Bus' là ngôi thứ 3 số ít (er). Động từ tách vorbeifahren tách tiền tố vorbei xuống cuối câu, phần gốc fahren biến âm a -> ä thành 'fährt'.",
            {"translation": "Tốt nhất bạn hãy đi tuyến xe buýt số 100! Chuyến xe buýt này chạy ngang qua Tòa nhà Quốc hội, Cổng Brandenburg và Cung điện Bellevue."}
        ),
        (
            "Câu 33: „Das Wetter in Berlin ist sonnig. Nach dem Mittagessen wollen meine Schwester und ich zwei Stunden auf dem Kurfürstendamm ___.“",
            "bummeln",
            ["bummeln"],
            "Sau động từ khuyết thiếu wollen, động từ chính đứng ở cuối câu ở dạng nguyên mẫu: 'bummeln' (đi dạo phố, tản bộ ngắm cảnh/mua sắm).",
            {"translation": "Thời tiết ở Berlin nắng đẹp. Sau bữa trưa, chị gái tôi và tôi muốn đi dạo phố hai tiếng đồng hồ trên đại lộ Kurfürstendamm."}
        )
    ]

    for q, ans, acc, exp, extra in fill_ins:
        extra_data = {
            "accepted_answers": acc,
            "translation": extra.get("translation", "")
        }
        if "visual_svg" in extra:
            extra_data["visual_svg"] = extra["visual_svg"]
        ex_list.append({
            "type": "dien_khuyet",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": extra_data
        })

    # =========================================================================
    # NHÓM 3: DỊCH CỤM TỪ VIỆT -> ĐỨC (12 CÂU: Q34 -> Q45)
    # =========================================================================
    trans_vocab_vd = [
        (
            "Câu 34: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'nhà ga trung tâm'",
            "der Hauptbahnhof",
            ["der Hauptbahnhof"],
            "Nhà ga trung tâm là danh từ giống đực der Hauptbahnhof (vì der Bahnhof).",
            "nhà ga trung tâm: der Hauptbahnhof"
        ),
        (
            "Câu 35: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'sân bay'",
            "der Flughafen",
            ["der Flughafen"],
            "Sân bay là danh từ ghép giống đực der Flughafen (số nhiều: die Flughäfen).",
            "sân bay: der Flughafen"
        ),
        (
            "Câu 36: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'ngã tư / giao lộ'",
            "die Kreuzung",
            ["die Kreuzung"],
            "Ngã tư / giao lộ là danh từ giống cái die Kreuzung (đuôi -ung luôn mang mạo từ die).",
            "ngã tư / giao lộ: die Kreuzung"
        ),
        (
            "Câu 37: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định ở số ít): 'đèn giao thông'",
            "die Ampel",
            ["die Ampel"],
            "Đèn giao thông là danh từ giống cái die Ampel (số nhiều: die Ampeln).",
            "đèn giao thông: die Ampel"
        ),
        (
            "Câu 38: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định): 'Nhà thờ lớn Berlin'",
            "der Berliner Dom",
            ["der Berliner Dom"],
            "Nhà thờ lớn Berlin là danh từ giống đực der Berliner Dom.",
            "Nhà thờ lớn Berlin: der Berliner Dom"
        ),
        (
            "Câu 39: Dịch sang tiếng Đức (bắt buộc kèm mạo từ xác định): 'Cổng thành Brandenburg'",
            "das Brandenburger Tor",
            ["das Brandenburger Tor"],
            "Cổng Brandenburg mang giống trung das Brandenburger Tor (vì das Tor).",
            "Cổng thành Brandenburg: das Brandenburger Tor"
        ),
        (
            "Câu 40: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi ngang qua bệnh viện'",
            "am Krankenhaus vorbei",
            ["am Krankenhaus vorbei", "am Krankenhaus vorbeigehen", "an dem Krankenhaus vorbei", "Gehen Sie am Krankenhaus vorbei"],
            "Bệnh viện là das Krankenhaus (giống trung). Khi đi với cấu trúc an + Dativ + vorbei, an + dem gộp thành 'am Krankenhaus vorbei'.",
            "đi ngang qua bệnh viện: am Krankenhaus vorbei"
        ),
        (
            "Câu 41: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi ngang qua trường đại học'",
            "an der Universität vorbei",
            ["an der Universität vorbei", "an der Universitaet vorbei", "an der Universität vorbeigehen", "Gehen Sie an der Universität vorbei"],
            "Trường đại học là die Universität (giống cái). Đi với an + Dativ + vorbei đổi die thành der: 'an der Universität vorbei'.",
            "đi ngang qua trường đại học: an der Universität vorbei"
        ),
        (
            "Câu 42: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi xuyên qua công viên'",
            "durch den Park",
            ["durch den Park", "durch den Park gehen", "durch den Park laufen", "Gehen Sie durch den Park"],
            "Công viên là der Park (giống đực). Đi xuyên qua dùng durch + Akkusativ -> 'durch den Park'.",
            "đi xuyên qua công viên: durch den Park"
        ),
        (
            "Câu 43: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi băng qua ngã tư'",
            "über die Kreuzung",
            ["über die Kreuzung", "ueber die Kreuzung", "über die Kreuzung gehen", "Gehen Sie über die Kreuzung"],
            "Ngã tư là die Kreuzung (giống cái). Đi băng qua dùng über + Akkusativ -> 'über die Kreuzung'.",
            "đi băng qua ngã tư: über die Kreuzung"
        ),
        (
            "Câu 44: Dịch cụm chỉ đường sau sang tiếng Đức (dùng ngôi trang trọng Sie): 'Ngài hãy rẽ trái ở con đường thứ ba!'",
            "Gehen Sie die dritte Straße links!",
            [
                "Gehen Sie die dritte Straße links!",
                "Gehen Sie die dritte Straße links",
                "Gehen Sie die 3. Straße links!",
                "Gehen Sie die 3. Straße links",
                "Fahren Sie die dritte Straße links!",
                "Fahren Sie die dritte Straße links",
                "Biegen Sie die dritte Straße links ab!",
                "Biegen Sie die dritte Straße links ab"
            ],
            "Con đường thứ ba bên trái là 'die dritte Straße links'.",
            "Ngài hãy rẽ trái ở con đường thứ ba: Gehen Sie die dritte Straße links!"
        ),
        (
            "Câu 45: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi cho đến nhà ga'",
            "bis zum Bahnhof",
            ["bis zum Bahnhof", "bis zum Bahnhof gehen", "Gehen Sie bis zum Bahnhof"],
            "Nhà ga là der Bahnhof (giống đực). Đi cho đến nhà ga dùng bis zu + Dativ -> 'bis zum Bahnhof'.",
            "đi cho đến nhà ga: bis zum Bahnhof"
        )
    ]

    for q, ans, acc, exp, trans in trans_vocab_vd:
        ex_list.append({
            "type": "dich_nghia_vd",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": {
                "accepted_answers": acc,
                "translation": trans
            }
        })

    # =========================================================================
    # NHÓM 4: DỊCH CỤM TỪ ĐỨC -> VIỆT (12 CÂU: Q46 -> Q57)
    # =========================================================================
    trans_vocab_dv = [
        (
            "Câu 46: Dịch sang tiếng Việt: „die Bahnhöfe und die Flughäfen“",
            "các nhà ga và các sân bay",
            ["các nhà ga và các sân bay", "những nhà ga và những sân bay", "nhà ga và sân bay", "các nhà ga và sân bay"],
            "Dạng số nhiều của der Bahnhof (die Bahnhöfe) và der Flughafen (die Flughäfen).",
            "die Bahnhöfe und die Flughäfen = các nhà ga và các sân bay"
        ),
        (
            "Câu 47: Dịch sang tiếng Việt: „die alten Schlösser und die modernen Einkaufszentren“",
            "những lâu đài cổ và những trung tâm thương mại hiện đại",
            ["những lâu đài cổ và những trung tâm thương mại hiện đại", "các lâu đài cổ và các trung tâm thương mại hiện đại", "các cung điện cổ và các trung tâm thương mại hiện đại", "những lâu đài cổ và trung tâm thương mại hiện đại"],
            "die Schlösser = những lâu đài/cung điện; die Einkaufszentren = những trung tâm thương mại.",
            "die alten Schlösser und die modernen Einkaufszentren = những lâu đài cổ và những trung tâm thương mại hiện đại"
        ),
        (
            "Câu 48: Dịch sang tiếng Việt: „am Supermarkt und an der Post vorbeigehen“",
            "đi ngang qua siêu thị và bưu điện",
            ["đi ngang qua siêu thị và bưu điện", "đi bộ ngang qua siêu thị và bưu điện", "đi ngang qua siêu thị và qua bưu điện"],
            "Cấu trúc an + Dativ + vorbeigehen với der Supermarkt (am) và die Post (an der).",
            "am Supermarkt und an der Post vorbeigehen = đi ngang qua siêu thị và bưu điện"
        ),
        (
            "Câu 49: Dịch sang tiếng Việt: „durch das mittelalterliche Stadttor laufen“",
            "đi bộ xuyên qua cổng thành thời trung cổ",
            ["đi bộ xuyên qua cổng thành thời trung cổ", "chạy xuyên qua cổng thành trung cổ", "đi xuyên qua cổng thành cổ", "đi xuyên qua cổng thành thời trung cổ", "chạy qua cổng thành thời trung cổ"],
            "durch das Stadttor = xuyên qua cổng thành.",
            "durch das mittelalterliche Stadttor laufen = đi bộ xuyên qua cổng thành thời trung cổ"
        ),
        (
            "Câu 50: Dịch sang tiếng Việt: „den malerischen Fluss entlangspazieren“",
            "đi dạo dọc theo dòng sông thơ mộng",
            ["đi dạo dọc theo dòng sông thơ mộng", "tản bộ dọc theo con sông đẹp như tranh", "đi dạo dọc bờ sông thơ mộng", "tản bộ dọc theo dòng sông thơ mộng", "đi dạo dọc theo con sông thơ mộng"],
            "den Fluss entlangspazieren = đi dạo dọc theo con sông.",
            "den malerischen Fluss entlangspazieren = đi dạo dọc theo dòng sông thơ mộng"
        ),
        (
            "Câu 51: Dịch sang tiếng Việt: „bis zur dritten Ampel geradeaus fahren“",
            "lái xe đi thẳng cho đến đèn giao thông thứ ba",
            ["lái xe đi thẳng cho đến đèn giao thông thứ ba", "chạy thẳng tới cột đèn giao thông thứ ba", "đi xe thẳng đến đèn giao thông thứ 3", "chạy thẳng cho đến đèn giao thông thứ ba", "đi thẳng cho đến đèn giao thông thứ ba"],
            "bis zur dritten Ampel = cho đến đèn giao thông thứ ba.",
            "bis zur dritten Ampel geradeaus fahren = lái xe đi thẳng cho đến đèn giao thông thứ ba"
        ),
        (
            "Câu 52: Dịch sang tiếng Việt: „über die breite Brücke in die Neustadt gehen“",
            "đi qua cây cầu rộng để vào khu phố mới",
            ["đi qua cây cầu rộng để vào khu phố mới", "đi bộ qua cây cầu rộng vào khu đô thị mới", "đi qua cây cầu rộng vào khu phố mới", "băng qua cây cầu rộng vào khu phố mới"],
            "über die breite Brücke = qua cây cầu rộng; in die Neustadt = vào khu phố mới.",
            "über die breite Brücke in die Neustadt gehen = đi qua cây cầu rộng để vào khu phố mới"
        ),
        (
            "Câu 53: Dịch sang tiếng Việt: „eine zweistündige Stadtrundfahrt mit dem Doppeldeckerbus machen“",
            "thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng",
            ["thực hiện một chuyến tham quan vòng quanh thành phố kéo dài hai tiếng bằng xe buýt hai tầng", "đi tham quan thành phố 2 tiếng bằng xe buýt 2 tầng", "đi tham quan vòng quanh thành phố 2 tiếng bằng xe buýt hai tầng", "thực hiện chuyến tham quan thành phố hai tiếng bằng xe buýt hai tầng"],
            "eine Stadtrundfahrt machen = thực hiện chuyến tham quan vòng quanh thành phố; der Doppeldeckerbus = xe buýt 2 tầng.",
            "eine zweistündige Stadtrundfahrt mit dem Doppeldeckerbus machen = thực hiện chuyến tham quan vòng quanh thành phố 2 tiếng bằng xe buýt 2 tầng"
        ),
        (
            "Câu 54: Dịch sang tiếng Việt: „an der nächsten Kreuzung links abbiegen“",
            "rẽ trái ở ngã tư tiếp theo",
            ["rẽ trái ở ngã tư tiếp theo", "quẹo trái tại giao lộ kế tiếp", "rẽ trái ở ngã tư kế tiếp", "quẹo trái ở ngã tư tiếp theo"],
            "an der nächsten Kreuzung = tại ngã tư tiếp theo; links abbiegen = rẽ trái.",
            "an der nächsten Kreuzung links abbiegen = rẽ trái ở ngã tư tiếp theo"
        ),
        (
            "Câu 55: Dịch sang tiếng Việt: „den Fernsehturm am Alexanderplatz besichtigen wollen“",
            "muốn tham quan Tháp truyền hình ở quảng trường Alexander",
            ["muốn tham quan Tháp truyền hình ở quảng trường Alexander", "muốn đi xem Tháp truyền hình tại quảng trường Alexander", "muốn tham quan tháp truyền hình ở quảng trường Alexander"],
            "besichtigen = tham quan; wollen = muốn.",
            "den Fernsehturm am Alexanderplatz besichtigen wollen = muốn tham quan Tháp truyền hình ở quảng trường Alexander"
        ),
        (
            "Câu 56: Dịch sang tiếng Việt: „Entschuldigen Sie bitte, wo geht es hier zum Reichstag?“",
            "Xin lỗi Ngài, ở đây đi lối nào để tới Tòa nhà Quốc hội vậy?",
            ["Xin lỗi Ngài, ở đây đi lối nào để tới Tòa nhà Quốc hội vậy?", "Cho tôi xin lỗi, đường nào đi đến Tòa nhà Quốc hội thế ạ?", "Xin lỗi, đi đến Tòa nhà Quốc hội theo hướng nào?", "Xin lỗi, đi lối nào để tới Tòa nhà Quốc hội?"],
            "Câu hỏi đường lịch sự với 'Wo geht es hier zum ...?'.",
            "Entschuldigen Sie bitte, wo geht es hier zum Reichstag? = Xin lỗi Ngài, ở đây đi lối nào để tới Tòa nhà Quốc hội vậy?"
        ),
        (
            "Câu 57: Dịch sang tiếng Việt: „Gegenüber vom Bahnhof sehen Sie das große Hotel.“",
            "Đối diện với nhà ga Ngài sẽ nhìn thấy khách sạn lớn.",
            ["Đối diện với nhà ga Ngài sẽ nhìn thấy khách sạn lớn.", "Ở phía đối diện nhà ga bạn sẽ thấy khách sạn lớn.", "Đối diện với nhà ga bạn sẽ nhìn thấy khách sạn lớn.", "Ở phía đối diện nhà ga Ngài sẽ nhìn thấy khách sạn lớn."],
            "gegenüber von + Dativ = đối diện với...",
            "Gegenüber vom Bahnhof sehen Sie das große Hotel. = Đối diện với nhà ga Ngài sẽ nhìn thấy khách sạn lớn."
        )
    ]

    for q, ans, acc, exp, trans in trans_vocab_dv:
        ex_list.append({
            "type": "dich_nghia_dv",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": {
                "accepted_answers": acc,
                "translation": trans
            }
        })

    # =========================================================================
    # NHÓM 5: NỐI Ô TƯ DUY NGỮ PHÁP & ĐỊNH HƯỚNG (10 BÀI: Q58 -> Q67)
    # (Đảm bảo: Cả 10 bài không có tiếng Việt trong ô chọn trái/phải!)
    # =========================================================================
    match_exercises = [
        # 58
        (
            "Câu 58: Nối Tình huống của Khách du lịch (Cột Trái) với Câu Hỏi Đường phù hợp (Cột Phải):",
            [
                {"left": "Du suchst ein Medikament und fragst nach dem Ort (Wo? + Nominativ)", "right": "Entschuldigung, wo ist hier eine Apotheke?"},
                {"left": "Du stehst auf der Straße und suchst direkt den Ort (suchen + Akkusativ)", "right": "Entschuldigung, ich suche den Hauptbahnhof."},
                {"left": "Du möchtest den Weg zu einer Sehenswürdigkeit wissen (zu + Dativ)", "right": "Entschuldigung, wie komme ich zum Brandenburger Tor?"},
                {"left": "Du möchtest in ein Gebäude hineingehen (in + Akkusativ)", "right": "Entschuldigung, wo geht es hier ins Stadtmuseum?"}
            ],
            "1. Bạn tìm thuốc và hỏi địa điểm (Wo? + Nominativ): Xin lỗi, ở đây có hiệu thuốc nào không? | 2. Bạn đứng trên đường và tìm thẳng địa điểm (suchen + Akkusativ): Xin lỗi, tôi đang tìm nhà ga trung tâm. | 3. Bạn muốn biết đường tới danh thắng (zu + Dativ): Xin lỗi, làm thế nào tôi đến được Cổng Brandenburg? | 4. Bạn muốn bước vào trong tòa nhà (in + Akkusativ): Xin lỗi, đi lối nào để vào trong bảo tàng thành phố?",
            "Phân tích 4 mẫu câu hỏi đường: 1. Động từ 'sein' (wo ist) đòi hỏi Nominativ. 2. Động từ 'suchen' đòi hỏi tân ngữ Akkusativ (den Hauptbahnhof). 3. 'wie komme ich' đi với zu + Dativ (zum Brandenburger Tor). 4. 'wo geht es' đi với in + Akkusativ khi vào trong tòa nhà (ins Stadtmuseum)."
        ),
        # 59
        (
            "Câu 59: Nối Động từ Chỉ đường (Cột Trái) với Cụm Giới từ Không gian tương ứng (Cột Phải):",
            [
                {"left": "Bitte gehen Sie an ...", "right": "der alten Kirche und am Rathaus vorbei!"},
                {"left": "Bitte laufen Sie durch ...", "right": "den grünen Stadtpark und das große Stadttor!"},
                {"left": "Bitte fahren Sie über ...", "right": "die neue Brücke und den Marktplatz!"},
                {"left": "Bitte spazieren Sie ...", "right": "die Friedrichstraße und den Kanal entlang!"}
            ],
            "1. Xin Ngài hãy đi ngang qua: nhà thờ cổ và tòa thị chính! | 2. Xin Ngài hãy đi bộ xuyên qua: công viên thành phố xanh tươi và cổng thành lớn! | 3. Xin Ngài hãy lái xe băng qua: cây cầu mới và quảng trường chợ! | 4. Xin Ngài hãy đi dạo: dọc theo phố Friedrich và con kênh!",
            "Quy tắc giới từ không gian: 1. an + Dativ + vorbei (an der alten Kirche, am Rathaus vorbei). 2. durch + Akkusativ (durch den Stadtpark, durch das Stadttor). 3. über + Akkusativ (über die Brücke, über den Marktplatz). 4. Danh từ ở Akkusativ + entlang (die Friedrichstraße entlang, den Kanal entlang)."
        ),
        # 60
        (
            "Câu 60: Nối Cặp Địa điểm (Cột Trái) với Cụm 'bis zu' tương ứng (Cột Phải):",
            [
                {"left": "der Flughafen & der Hafen", "right": "Fahren Sie geradeaus bis zum Flughafen / bis zum Hafen!"},
                {"left": "die Kreuzung & die Ampel", "right": "Gehen Sie geradeaus bis zur Kreuzung / bis zur Ampel!"},
                {"left": "das Stadttor & das Einkaufszentrum", "right": "Laufen Sie geradeaus bis zum Stadttor / bis zum Einkaufszentrum!"},
                {"left": "die zweite Straße & die Staatsoper", "right": "Gehen Sie geradeaus bis zur zweiten Straße / bis zur Staatsoper!"}
            ],
            "1. Sân bay & cảng biển (Maskulinum): Hãy lái xe đi thẳng cho đến sân bay / cho đến cảng biển! | 2. Ngã tư & đèn giao thông (Femininum): Hãy đi thẳng cho đến ngã tư / cho đến đèn giao thông! | 3. Cổng thành & trung tâm thương mại (Neutrum): Hãy đi bộ thẳng cho đến cổng thành / cho đến trung tâm thương mại! | 4. Con đường thứ hai & Nhà hát Opera (Femininum): Hãy đi thẳng cho đến con đường thứ hai / cho đến Nhà hát Opera!",
            "Cấu trúc 'bis zu + Dativ': 1. Danh từ giống đực (der): zu + dem = 'zum' (zum Flughafen, zum Hafen). 2. Danh từ giống cái (die): zu + der = 'zur' (zur Kreuzung, zur Ampel). 3. Danh từ giống trung (das): zu + dem = 'zum' (zum Stadttor, zum Einkaufszentrum). 4. Danh từ giống cái đi kèm số thứ tự hoặc tên riêng: zu + der = 'zur' (zur zweiten Straße, zur Staatsoper)."
        ),
        # 61
        (
            "Câu 61: Nối Nhóm Địa danh (Cột Trái) với Cấu trúc 'in + Akkusativ/Dativ' tương ứng (Cột Phải):",
            [
                {"left": "Berliner Dom, Zoo, Supermarkt (Maskulinum)", "right": "Wir gehen am Nachmittag in den Berliner Dom / in den Zoo."},
                {"left": "Disko, Staatsoper, Nationalgalerie (Femininum)", "right": "Wir gehen heute Abend in die Disko / in die Staatsoper."},
                {"left": "Kino, Einkaufszentrum, Theater (Neutrum)", "right": "Wir gehen am Wochenende ins Kino / ins Einkaufszentrum."},
                {"left": "Konzert, Film (Wo? -> Dativ)", "right": "Wir hören ein Konzert im Berliner Dom / sehen einen Film im Kino."}
            ],
            "1. Nhà thờ lớn, sở thú, siêu thị (Giống đực - Akkusativ): Buổi chiều chúng tôi đi vào Nhà thờ lớn Berlin / vào sở thú. | 2. Vũ trường, Nhà hát Opera, Khu triển lãm (Giống cái - Akkusativ): Tối nay chúng tôi đi vào vũ trường / vào Nhà hát Opera. | 3. Rạp phim, trung tâm thương mại, nhà hát kịch (Giống trung - Akkusativ): Cuối tuần chúng tôi đi vào rạp chiếu phim / vào trung tâm thương mại. | 4. Nghe hòa nhạc, xem phim (Vị trí tĩnh Wo? -> Dativ): Chúng tôi nghe hòa nhạc ở trong Nhà thờ lớn / xem phim ở trong rạp.",
            "Quy tắc giới từ 'in': 1. Di chuyển vào trong (Wohin? + Akkusativ): giống đực dùng 'in den' (in den Berliner Dom, in den Zoo). 2. Giống cái dùng 'in die' (in die Disko, in die Staatsoper). 3. Giống trung dùng 'in das' = 'ins' (ins Kino, ins Einkaufszentrum). 4. Vị trí tĩnh diễn ra sự việc (Wo? + Dativ): giống đực/trung dùng 'in dem' = 'im' (im Berliner Dom, im Kino)."
        ),
        # 62
        (
            "Câu 62: Nối Đối tượng Giao tiếp (Cột Trái) với Lời Chỉ đường phù hợp (Cột Phải):",
            [
                {"left": "Höfliche Anrede an eine ältere Dame (Sie)", "right": "Gehen Sie bitte die erste Straße rechts und dann bis zur Ampel!"},
                {"left": "Wegbeschreibung für den besten Freund (du)", "right": "Geh bitte die erste Straße rechts und lauf dann über den Platz!"},
                {"left": "Wegbeschreibung für zwei Mitschüler (ihr)", "right": "Geht bitte die erste Straße rechts und fahrt dann mit dem Bus!"},
                {"left": "Vorschlag für die ganze Gruppe (wir)", "right": "Gehen wir zuerst durch den Park und danach ins Restaurant!"}
            ],
            "1. Lời nói lịch sự với một quý bà lớn tuổi (ngôi Sie): Xin Ngài hãy đi con đường thứ nhất bên phải và sau đó đi cho đến đèn giao thông! | 2. Chỉ đường cho bạn thân nhất (ngôi du): Cậu hãy đi con đường thứ nhất bên phải và sau đó chạy băng qua quảng trường! | 3. Chỉ đường cho hai người bạn cùng lớp (ngôi ihr): Các bạn hãy đi con đường thứ nhất bên phải và sau đó đi bằng xe buýt! | 4. Đề xuất cho cả nhóm bạn bè (ngôi wir): Đầu tiên chúng ta hãy đi xuyên qua công viên và sau đó vào quán cà phê!",
            "Các ngôi giao tiếp trong câu chỉ đường: 1. Ngôi lịch sự 'Sie': đảo động từ lên đầu kèm đại từ 'Gehen Sie...'. 2. Ngôi thân mật số ít 'du': dùng thể mệnh lệnh bỏ đuôi -st và bỏ đại từ 'Geh... / Lauf...'. 3. Ngôi thân mật số nhiều 'ihr': dùng thể mệnh lệnh giữ đuôi -t và bỏ đại từ 'Geht... / Fahrt...'. 4. Lời rủ rê nhóm 'wir': đảo động từ lên trước 'Gehen wir...'."
        ),
        # 63
        (
            "Câu 63: Nối Chủ ngữ (Cột Trái) với Câu Động từ Khuyết thiếu tương ứng (Cột Phải):",
            [
                {"left": "Meine Cousine Lena (3. Person Singular)", "right": "will nächstes Jahr an der Humboldt-Universität Medizin studieren."},
                {"left": "Mein Bruder und ich (1. Person Plural)", "right": "wollen morgen Vormittag eine Schifffahrt auf der Spree machen."},
                {"left": "Du (2. Person Singular)", "right": "musst an der dritten Kreuzung links abbiegen und vor der Bank halten."},
                {"left": "Ihr (2. Person Plural)", "right": "könnt vom Alexanderplatz zu Fuß bis zur Museumsinsel gehen."}
            ],
            "1. Chị họ Lena của tôi (Ngôi thứ 3 số ít): muốn học ngành y tại Đại học Humboldt vào năm tới. | 2. Anh trai tôi và tôi (Ngôi thứ nhất số nhiều wir): muốn đi du thuyền trên sông Spree vào sáng mai. | 3. Bạn (Ngôi thứ 2 số ít du): phải rẽ trái ở ngã tư thứ ba và dừng lại trước ngân hàng. | 4. Các bạn (Ngôi thứ 2 số nhiều ihr): có thể đi bộ từ Quảng trường Alexander cho đến Đảo Bảo tàng.",
            "Chia Modalverben theo các ngôi: 1. Ngôi thứ 3 số ít (sie = Lena) của wollen chia là 'will'. 2. Chủ ngữ ghép 'Mein Bruder und ich' = wir chia wollen là 'wollen'. 3. Ngôi du chia müssen là 'musst'. 4. Ngôi ihr chia können là 'könnt'."
        ),
        # 64
        (
            "Câu 64: Nối Danh từ Địa điểm Số Ít (Cột Trái) với Dạng Số Nhiều tương ứng (Cột Phải):",
            [
                {"left": "der Bahnhof / der Hafen / der Markt", "right": "die Bahnhöfe / die Häfen / die Märkte"},
                {"left": "das Schloss / das Krankenhaus / das Rathaus", "right": "die Schlösser / die Krankenhäuser / die Rathäuser"},
                {"left": "das Einkaufszentrum / das Museum", "right": "die Einkaufszentren / die Museen"},
                {"left": "die Brücke / die Kreuzung / die Ampel", "right": "die Brücken / die Kreuzungen / die Ampeln"}
            ],
            "1. Nhà ga / cảng biển / khu chợ: các nhà ga / các cảng biển / các khu chợ. | 2. Lâu đài / bệnh viện / tòa thị chính: các lâu đài / các bệnh viện / các tòa thị chính. | 3. Trung tâm thương mại / viện bảo tàng: các trung tâm thương mại / các viện bảo tàng. | 4. Cây cầu / ngã tư / đèn giao thông: những cây cầu / những ngã tư / những cột đèn giao thông.",
            "Quy tắc chuyển số nhiều danh từ địa điểm: 1. Danh từ giống đực thêm Umlaut và đuôi -e (Bahnhöfe, Häfen, Märkte). 2. Danh từ giống trung tận cùng bằng Haus/Schloss thêm Umlaut và đuôi -er (Schlösser, Krankenhäuser, Rathäuser). 3. Danh từ gốc Latin đuôi -um đổi thành -en (Einkaufszentren, Museen). 4. Danh từ giống cái thêm đuôi -n/-en (Brücken, Kreuzungen, Ampeln)."
        ),
        # 65
        (
            "Câu 65: Nối Danh lam Thắng cảnh Berlin (Cột Trái) với Hoạt động thực tế phù hợp (Cột Phải):",
            [
                {"left": "Auf dem Fernsehturm am Alexanderplatz", "right": "kann man ganz Berlin von oben sehen."},
                {"left": "Auf der Museumsinsel und in der Alten Nationalgalerie", "right": "wollen die Touristen berühmte Kunstwerke besichtigen."},
                {"left": "Auf der langen Friedrichstraße", "right": "möchten viele Besucher am Nachmittag bummeln und einkaufen."},
                {"left": "Vor dem Brandenburger Tor und dem Reichstag", "right": "machen die Reisegruppen immer viele Erinnerungsfotos."}
            ],
            "1. Trên Tháp truyền hình ở Quảng trường Alexander: người ta có thể nhìn thấy toàn cảnh Berlin từ trên cao. | 2. Trên Đảo Bảo tàng và trong Khu triển lãm Quốc gia Cũ: các du khách muốn tham quan các tác phẩm nghệ thuật nổi tiếng. | 3. Trên phố mua sắm Friedrich dài: nhiều khách tham quan muốn đi dạo và mua sắm vào buổi chiều. | 4. Phía trước Cổng Brandenburg và Tòa nhà Quốc hội: các đoàn du lịch luôn chụp rất nhiều bức ảnh kỷ niệm.",
            "Hoạt động gắn liền với địa danh Berlin: 1. Fernsehturm cao 368m là nơi ngắm toàn cảnh thành phố (von oben sehen). 2. Museumsinsel và Alte Nationalgalerie là trung tâm nghệ thuật và bảo tàng (Kunstwerke besichtigen). 3. Friedrichstraße là phố thương mại mua sắm sầm uất (bummeln und einkaufen). 4. Brandenburger Tor và Reichstag là biểu tượng lịch sử để chụp ảnh kỷ niệm (Erinnerungsfotos machen)."
        ),
        # 66
        (
            "Câu 66: Nối Trình tự Chỉ đường (Cột Trái) với Mệnh đề Di chuyển tương ứng (Cột Phải):",
            [
                {"left": "Erster Schritt (Zuerst)", "right": "gehen Sie vom Bahnhofsvorplatz geradeaus die Kaiserstraße entlang."},
                {"left": "Zweiter Schritt (Dann)", "right": "biegen Sie an der zweiten Kreuzung vor der Bank links ab."},
                {"left": "Dritter Schritt (Danach)", "right": "laufen Sie über die kleine Brücke und am Stadtpark vorbei."},
                {"left": "Letzter Schritt (Zum Schluss)", "right": "sehen Sie direkt rechts nach der Ampel Ihr Hotel."}
            ],
            "1. Bước thứ nhất (Đầu tiên): Ngài hãy đi từ quảng trường trước nhà ga đi thẳng dọc theo phố Kaiser. | 2. Bước thứ hai (Sau đó): Ngài hãy rẽ trái ở ngã tư thứ hai phía trước ngân hàng. | 3. Bước thứ ba (Tiếp theo): Ngài hãy đi bộ qua cây cầu nhỏ và đi ngang qua công viên thành phố. | 4. Bước cuối cùng (Cuối cùng): Ngài sẽ nhìn thấy khách sạn của mình ở ngay bên phải sau cột đèn giao thông.",
            "Trình tự logic của bài chỉ đường: 1. Bắt đầu bằng 'Zuerst' xuất phát từ điểm ban đầu. 2. Tiếp diễn bằng 'Dann' với hành động rẽ hướng. 3. Kết nối bằng 'Danach' vượt qua các chướng ngại vật/cột mốc. 4. Kết thúc bằng 'Zum Schluss' xác định tòa nhà đích đến."
        ),
        # 67
        (
            "Câu 67: Nối Câu hỏi Phương hướng (Cột Trái) với Câu trả lời đúng Ngữ pháp (Cột Phải):",
            [
                {"left": "Wo wartet dein Freund auf dich? (Dativ)", "right": "Er steht direkt vor dem Kino / an der zweiten Ampel."},
                {"left": "Wohin läufst du so schnell? (Akkusativ)", "right": "Ich laufe schnell in das Kino / über die Straße."},
                {"left": "Wo fährt der Sightseeing-Bus entlang? (Dativ)", "right": "Er fährt am Schloss Bellevue und an der Universität vorbei."},
                {"left": "Wohin fährt der Sightseeing-Bus jetzt? (Akkusativ)", "right": "Er fährt jetzt durch das Stadttor auf den großen Platz."}
            ],
            "1. Bạn của bạn đang đợi bạn ở đâu? (Vị trí tĩnh - Dativ): Anh ấy đang đứng ngay trước rạp chiếu phim / ở cột đèn giao thông thứ hai. | 2. Bạn đang chạy nhanh đi đâu thế? (Hướng di chuyển - Akkusativ): Tôi đang chạy nhanh vào trong rạp chiếu phim / qua bên kia đường. | 3. Chiếc xe buýt tham quan chạy dọc theo đâu? (Đi ngang qua - Dativ): Nó chạy ngang qua Cung điện Bellevue và trường Đại học. | 4. Bây giờ chiếc xe buýt tham quan chạy đi đâu? (Xuyên qua hướng tới - Akkusativ): Bây giờ nó chạy xuyên qua cổng thành đi ra quảng trường lớn.",
            "Phân biệt Wo? (Dativ) và Wohin? (Akkusativ): 1. Câu hỏi 'Wo?' hỏi vị trí đứng tĩnh đòi hỏi Dativ (vor dem Kino, an der Ampel). 2. Câu hỏi 'Wohin?' hỏi hướng đích chuyển động đòi hỏi Akkusativ (in das Kino, über die Straße). 3. Hành động đi ngang qua địa điểm dùng an + Dativ + vorbei. 4. Hành động đi xuyên qua và tiến vào không gian mới dùng durch + Akkusativ."
        )
    ]

    for q, pairs, trans, exp in match_exercises:
        corr_ans = " | ".join([f"{p['left']} = {p['right']}" for p in pairs])
        ex_list.append({
            "type": "noi_o",
            "question": q,
            "options": None,
            "correct_answer": corr_ans,
            "explanation": exp,
            "exp_reward": 30,
            "extra_data": {
                "noi_o_pairs": pairs,
                "translation": trans
            }
        })

    # =========================================================================
    # NHÓM 6: ĐIỀN VÀO CHỖ TRỐNG TẠO CÂU (10 CÂU: Q68 -> Q77)
    # =========================================================================
    create_sentences = [
        (
            "Câu 68: Hoàn thành lời chỉ đường cho người bạn thân (du) khớp với lộ trình trên bản đồ bằng cách điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Lauf zuerst [1] den Park und geh dann an [2] Kirche vorbei bis zum Bahnhof!'",
            "durch / der",
            ["durch / der", "durch/der"],
            "Đi xuyên qua 'der Park' dùng 'durch' ('durch den Park'). Đi ngang qua 'die Kirche' dùng 'an + Dativ + vorbei' -> 'an der Kirche vorbei'.",
            {"visual_svg": "map_build_1", "translation": "Đầu tiên cậu hãy chạy xuyên qua công viên và sau đó đi ngang qua nhà thờ cho đến nhà ga!"}
        ),
        (
            "Câu 69: Hoàn thành lời chỉ đường lịch sự cho vị khách du lịch khớp với bản đồ bằng cách điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Gehen Sie zuerst [1] die Brücke und dann die Goethestraße [2] bis zur Post!'",
            "über / entlang",
            ["über / entlang", "über/entlang", "ueber / entlang", "ueber/entlang"],
            "Đi vượt qua mặt cầu dùng 'über' ('über die Brücke'); đi dọc theo con đường đặt 'entlang' ở sau danh từ ('die Goethestraße entlang').",
            {"visual_svg": "map_build_2", "translation": "Đầu tiên Ngài hãy đi qua cây cầu và sau đó đi dọc theo đường Goethe cho đến bưu điện!"}
        ),
        (
            "Câu 70: Hoàn thành câu kể về lịch trình ngày Chủ nhật của gia đình bằng cách điền 2 cụm từ vào các chỗ trống (ngăn cách bởi dấu /): 'Am Sonntagvormittag fahren wir zuerst [1] Flughafen, um Oma abzuholen, und am Nachmittag gehen wir zusammen [2] Zoo.'",
            "zum / in den",
            ["zum / in den", "zum/in den", "zum / zum", "zum/zum"],
            "'der Flughafen' sau 'zu + Dativ' là 'zum Flughafen'; đi vào bên trong sở thú ('der Zoo') dùng 'in den Zoo'.",
            {"translation": "Sáng Chủ nhật đầu tiên chúng tôi lái xe ra sân bay để đón bà, và buổi chiều chúng tôi cùng nhau đi vào sở thú."}
        ),
        (
            "Câu 71: Hoàn thành lời hướng dẫn của tài xế xe buýt bằng cách điền 2 từ vào các chỗ trống (ngăn cách bởi dấu /): 'Sie müssen hier aussteigen, dann [1] großen Supermarkt vorbeigehen und geradeaus bis [2] zweiten Ampel laufen.'",
            "am / zur",
            ["am / zur", "am/zur", "an dem / zur", "an dem/zur", "am / zu der", "am/zu der"],
            "'der Supermarkt' đi với 'an + Dativ + vorbei' là 'am großen Supermarkt vorbei'; 'die Ampel' đi với 'bis zu + Dativ' là 'bis zur zweiten Ampel'.",
            {"translation": "Ngài phải xuống xe ở đây, sau đó đi ngang qua siêu thị lớn và đi bộ thẳng cho đến đèn giao thông thứ hai."}
        ),
        (
            "Câu 72: Hoàn thành câu với dạng chia đúng của động từ khuyết thiếu 'wollen' vào các chỗ trống (ngăn cách bởi dấu /): 'Mein Freund Lukas [1] heute unbedingt das Bundeskanzleramt fotografieren, aber wir [2] lieber zuerst auf der Museumsinsel spazieren gehen.'",
            "will / wollen",
            ["will / wollen", "will/wollen"],
            "Ngôi thứ 3 số ít ('Lukas' = 'er') chia là 'will'; ngôi thứ nhất số nhiều ('wir') chia là 'wollen'.",
            {"translation": "Người bạn Lukas của tôi hôm nay nhất định muốn chụp ảnh Phủ Thủ tướng, nhưng chúng tôi lại muốn đi dạo trên Đảo Bảo tàng trước hơn."}
        ),
        (
            "Câu 73: Hoàn thành câu hướng dẫn giao thông với dạng chia đúng của 'müssen' vào chỗ trống [1] và 'können' vào chỗ trống [2] (ngăn cách bởi dấu /): 'Vor der Baustelle [1] ihr leider rechts abbiegen, aber danach [2] ihr wieder geradeaus bis zum Hafen fahren.'",
            "müsst / könnt",
            ["müsst / könnt", "müsst/könnt", "muesst / koennt", "muesst/koennt"],
            "Với chủ ngữ 'ihr' (các bạn), 'müssen' chia là 'müsst' và 'können' chia là 'könnt'.",
            {"translation": "Trước công trường rất tiếc các bạn phải rẽ phải, nhưng sau đó các bạn có thể lại chạy thẳng cho đến cảng biển."}
        ),
        (
            "Câu 74: Hoàn thành câu với cụm giới từ 'in' kèm mạo từ thích hợp vào các chỗ trống (ngăn cách bởi dấu /): 'Wohin gehst du? — Ich gehe jetzt [1] Staatsoper, weil meine Freundin heute Abend [2] Staatsoper Geige spielt.'",
            "in die / in der",
            ["in die / in der", "in die/in der"],
            "Ô 1 trả lời cho 'Wohin?' (di chuyển vào trong) -> in + Akkusativ = 'in die Staatsoper'. Ô 2 trả lời cho 'Wo?' (chơi đàn ở đâu - vị trí tĩnh) -> in + Dativ = 'in der Staatsoper'.",
            {"translation": "Bạn đang đi đâu thế? — Bây giờ tôi đi vào Nhà hát Opera Quốc gia, bởi vì tối nay bạn gái tôi chơi đàn vĩ cầm ở trong Nhà hát Opera Quốc gia."}
        ),
        (
            "Câu 75: Hoàn thành câu với dạng rút gọn đúng của giới từ 'in' vào các chỗ trống (ngăn cách bởi dấu /): 'Mein kleiner Bruder muss leider [1] Krankenhaus gebracht werden, aber unser Nachbar arbeitet als Arzt [2] Krankenhaus.'",
            "ins / im",
            ["ins / im", "ins/im", "in das / in dem", "in das/in dem"],
            "Đưa vào bệnh viện ('Wohin?' + Akkusativ) với 'das Krankenhaus' dùng 'ins' (in das). Làm việc ở trong bệnh viện ('Wo?' + Dativ) dùng 'im' (in dem).",
            {"translation": "Em trai nhỏ của tôi rất tiếc phải được đưa vào bệnh viện, nhưng người hàng xóm của chúng tôi làm bác sĩ ở trong bệnh viện đó."}
        ),
        (
            "Câu 76: Hoàn thành đoạn hội thoại hỏi đường ngắn trên phố bằng cách điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Entschuldigung, ich suche [1] alten Marktplatz. Wie komme ich am besten [2] Marktplatz?'",
            "den / zum",
            ["den / zum", "den/zum", "den / zu dem", "den/zu dem"],
            "'der Marktplatz' (giống đực) đứng sau động từ 'suchen' (Akkusativ) dùng mạo từ 'den' ('den alten Marktplatz'); đứng sau 'Wie komme ich ...?' (zu + Dativ) dùng 'zum' ('zum Marktplatz').",
            {"translation": "Xin lỗi, tôi đang tìm quảng trường chợ cổ. Làm thế nào tôi đi đến được quảng trường chợ một cách tốt nhất?"}
        ),
        (
            "Câu 77: Hoàn thành câu chỉ đường với dạng đúng của số thứ tự 'erste' (1.) vào chỗ trống [1] và 'zweite' (2.) vào chỗ trống [2] (ngăn cách bởi dấu /): 'Nehmen Sie bitte die [1] Straße rechts und biegen Sie dann an der [2] Kreuzung wieder links ab!'",
            "erste / zweiten",
            ["erste / zweiten", "erste/zweiten"],
            "Sau 'die' ở Akkusativ giống cái dùng 'erste' ('die erste Straße'); sau 'an der' ở Dativ giống cái bắt buộc thêm đuôi -n thành 'zweiten' ('an der zweiten Kreuzung').",
            {"translation": "Xin Ngài hãy đi con đường thứ nhất bên phải và sau đó tại ngã tư thứ hai lại rẽ trái!"}
        )
    ]

    for q, ans, acc, exp, extra in create_sentences:
        extra_data = {
            "accepted_answers": acc,
            "translation": extra.get("translation", "")
        }
        if "visual_svg" in extra:
            extra_data["visual_svg"] = extra["visual_svg"]
        ex_list.append({
            "type": "dien_tao_cau",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": extra_data
        })

    # =========================================================================
    # NHÓM 7: NGHE VÀ ĐIỀN TỪ (9 CÂU: Q78 -> Q86)
    # =========================================================================
    listen_exercises = [
        (
            "Câu 78: „Entschuldigung, wie komme ich vom Hauptbahnhof am schnellsten zum ___?“",
            "Flughafen",
            ["Flughafen"],
            "Entschuldigung, wie komme ich vom Hauptbahnhof am schnellsten zum Flughafen?",
            "Danh từ ghép der Flughafen có nghĩa là sân bay.",
            "Xin lỗi, làm thế nào tôi đi từ nhà ga trung tâm ra sân bay nhanh nhất?"
        ),
        (
            "Câu 79: „Gehen Sie zuerst über die lange ___ und dann dreihundert Meter den Fluss entlang.“",
            "Brücke",
            ["Brücke", "Bruecke"],
            "Gehen Sie zuerst über die lange Brücke und dann dreihundert Meter den Fluss entlang.",
            "Danh từ die Brücke có nghĩa là cây cầu.",
            "Đầu tiên Ngài hãy đi qua cây cầu dài và sau đó đi dọc theo con sông ba trăm mét."
        ),
        (
            "Câu 80: „Der Sightseeing-Bus fährt am historischen Rathaus und an der ___ vorbei.“",
            "Staatsoper",
            ["Staatsoper"],
            "Der Sightseeing-Bus fährt am historischen Rathaus und an der Staatsoper vorbei.",
            "die Staatsoper là Nhà hát Opera Quốc gia.",
            "Chiếc xe buýt tham quan chạy ngang qua tòa thị chính lịch sử và Nhà hát Opera Quốc gia."
        ),
        (
            "Câu 81: „An der dritten ___ vor dem Krankenhaus musst du links abbiegen.“",
            "Kreuzung",
            ["Kreuzung"],
            "An der dritten Kreuzung vor dem Krankenhaus musst du links abbiegen.",
            "die Kreuzung là ngã tư / giao lộ.",
            "Tại ngã tư thứ ba trước bệnh viện, bạn phải rẽ trái."
        ),
        (
            "Câu 82: „Meine Großeltern ___ morgen Nachmittag das schöne Schloss Bellevue besichtigen.“",
            "wollen",
            ["wollen"],
            "Meine Großeltern wollen morgen Nachmittag das schöne Schloss Bellevue besichtigen.",
            "Động từ khuyết thiếu wollen chia với chủ ngữ số nhiều Meine Großeltern (sie).",
            "Ông bà của tôi muốn tham quan Cung điện Bellevue tuyệt đẹp vào chiều mai."
        ),
        (
            "Câu 83: „Laufen Sie einfach ___ das alte Stadttor, dann stehen Sie direkt auf dem Marktplatz.“",
            "durch",
            ["durch"],
            "Laufen Sie einfach durch das alte Stadttor, dann stehen Sie direkt auf dem Marktplatz.",
            "Giới từ durch (+ Akkusativ) diễn tả sự đi xuyên qua lòng cổng thành.",
            "Ngài cứ đi bộ xuyên qua cổng thành cổ, sau đó Ngài sẽ đứng ngay trên quảng trường chợ."
        ),
        (
            "Câu 84: „Am Samstag möchten wir im neuen ___ Kleider kaufen und danach ins Kino gehen.“",
            "Einkaufszentrum",
            ["Einkaufszentrum"],
            "Am Samstag möchten wir im neuen Einkaufszentrum Kleider kaufen und danach ins Kino gehen.",
            "das Einkaufszentrum là trung tâm thương mại.",
            "Vào thứ Bảy chúng tôi muốn mua quần áo ở trong trung tâm thương mại mới và sau đó đi vào rạp chiếu phim."
        ),
        (
            "Câu 85: „Fahren Sie bitte immer ___ bis zur zweiten Ampel vor der Universität!“",
            "geradeaus",
            ["geradeaus"],
            "Fahren Sie bitte immer geradeaus bis zur zweiten Ampel vor der Universität!",
            "Trạng từ chỉ hướng geradeaus có nghĩa là đi thẳng.",
            "Xin Ngài cứ lái xe đi thẳng mãi cho đến đèn giao thông thứ hai trước trường đại học!"
        ),
        (
            "Câu 86: „Nach der ___ will mein Cousin noch eine Stunde am Hafen bummeln.“",
            "Stadtrundfahrt",
            ["Stadtrundfahrt"],
            "Nach der Stadtrundfahrt will mein Cousin noch eine Stunde am Hafen bummeln.",
            "die Stadtrundfahrt là chuyến tham quan vòng quanh thành phố.",
            "Sau chuyến tham quan vòng quanh thành phố, anh họ tôi còn muốn đi dạo một tiếng ở cảng biển."
        )
    ]

    for q, ans, acc, audio_t, exp, trans in listen_exercises:
        ex_list.append({
            "type": "nghe_dien",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": {
                "accepted_answers": acc,
                "audio_text": audio_t,
                "translation": trans
            }
        })

    # =========================================================================
    # NHÓM 8: DỊCH CÂU HOÀN CHỈNH VIỆT -> ĐỨC (7 CÂU: Q87 -> Q93)
    # =========================================================================
    trans_sent_vd = [
        (
            "Câu 87: Dịch câu chỉ đường sau sang tiếng Đức (dùng ngôi trang trọng Sie): 'Đầu tiên Ngài hãy đi thẳng qua cây cầu, sau đó đi ngang qua bệnh viện cho đến đèn giao thông thứ hai!'",
            "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!",
            [
                "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!",
                "Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel",
                "Zuerst gehen Sie geradeaus über die Brücke, danach gehen Sie am Krankenhaus vorbei bis zur zweiten Ampel.",
                "Zuerst gehen Sie geradeaus über die Brücke, danach gehen Sie am Krankenhaus vorbei bis zur zweiten Ampel",
                "Gehen Sie zuerst über die Brücke geradeaus und dann am Krankenhaus vorbei bis zur zweiten Ampel!",
                "Gehen Sie zuerst über die Brücke geradeaus und dann am Krankenhaus vorbei bis zur zweiten Ampel!"
            ],
            "Qua cầu: 'über die Brücke' (Akkusativ); đi ngang qua bệnh viện ('das Krankenhaus'): 'am Krankenhaus vorbei' (Dativ); cho đến đèn giao thông thứ hai ('die Ampel'): 'bis zur zweiten Ampel' (Dativ).",
            "Đầu tiên Ngài hãy đi thẳng qua cây cầu, sau đó đi ngang qua bệnh viện cho đến đèn giao thông thứ hai: Gehen Sie zuerst geradeaus über die Brücke, dann am Krankenhaus vorbei bis zur zweiten Ampel!"
        ),
        (
            "Câu 88: Dịch câu chỉ đường cho bạn thân sau sang tiếng Đức (dùng ngôi du): 'Cậu hãy đi xuyên qua công viên, đi dọc theo con sông và rẽ trái ở ngã tư thứ nhất!'",
            "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!",
            [
                "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!",
                "Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab",
                "Geh durch den Park, geh den Fluss entlang und geh die erste Straße links!",
                "Geh durch den Park, geh den Fluss entlang und geh die erste Straße links",
                "Lauf durch den Park, den Fluss entlang und an der ersten Kreuzung links!",
                "Lauf durch den Park, den Fluss entlang und an der ersten Kreuzung links"
            ],
            "Ngôi du mệnh lệnh: 'Geh / Lauf'; xuyên qua công viên: 'durch den Park'; dọc theo con sông: 'den Fluss entlang'; ở ngã tư thứ nhất bên trái: 'an der ersten Kreuzung links'.",
            "Cậu hãy đi xuyên qua công viên, đi dọc theo con sông và rẽ trái ở ngã tư thứ nhất: Geh durch den Park, lauf den Fluss entlang und bieg an der ersten Kreuzung links ab!"
        ),
        (
            "Câu 89: Dịch câu hỏi đường sau sang tiếng Đức: 'Xin lỗi, chúng tôi đang tìm Đảo Bảo tàng. Làm thế nào chúng tôi đi bộ đến được Đảo Bảo tàng?'",
            "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?",
            [
                "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?",
                "Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel",
                "Entschuldigung, wir suchen die Museumsinsel. Wie gehen wir zur Museumsinsel?",
                "Entschuldigung, wir suchen die Museumsinsel. Wie gehen wir zur Museumsinsel",
                "Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir zur Museumsinsel?",
                "Entschuldigen Sie, wir suchen die Museumsinsel. Wie kommen wir zur Museumsinsel"
            ],
            "'die Museumsinsel' mang giống cái (die): sau 'suchen' (Akkusativ) là 'die Museumsinsel', sau 'Wie kommen wir ...?' (zu + Dativ) là 'zur Museumsinsel'.",
            "Xin lỗi, chúng tôi đang tìm Đảo Bảo tàng. Làm thế nào chúng tôi đi bộ đến được Đảo Bảo tàng? = Entschuldigung, wir suchen die Museumsinsel. Wie kommen wir zu Fuß zur Museumsinsel?"
        ),
        (
            "Câu 90: Dịch câu sau sang tiếng Đức (dùng ngôi ihr): 'Các bạn hãy đi ngang qua nhà thờ cổ và băng qua quảng trường chợ, ở bên phải các bạn sẽ nhìn thấy tòa thị chính.'",
            "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.",
            [
                "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.",
                "Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus",
                "Geht an der alten Kirche vorbei und lauft über den Marktplatz! Rechts seht ihr das Rathaus.",
                "Geht an der alten Kirche vorbei und lauft über den Marktplatz! Rechts seht ihr das Rathaus",
                "Lauft an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus.",
                "Lauft an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus"
            ],
            "Mệnh lệnh ngôi ihr: 'Geht / Lauft'; ngang qua nhà thờ cổ: 'an der alten Kirche vorbei'; băng qua quảng trường chợ: 'über den Marktplatz'; các bạn nhìn thấy: 'seht ihr'.",
            "Các bạn hãy đi ngang qua nhà thờ cổ và băng qua quảng trường chợ, ở bên phải các bạn sẽ nhìn thấy tòa thị chính = Geht an der alten Kirche vorbei und über den Marktplatz, rechts seht ihr das Rathaus."
        ),
        (
            "Câu 91: Dịch câu sau sang tiếng Đức: 'Buổi sáng chú của tôi muốn tham quan Tòa nhà Quốc hội, và buổi chiều chúng tôi muốn đi dạo phố ở trung tâm thương mại.'",
            "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln.",
            [
                "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln.",
                "Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln",
                "Am Morgen will mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln.",
                "Am Morgen will mein Onkel den Reichstag besichtigen, und am Nachmittag möchten wir im Einkaufszentrum bummeln",
                "Vormittags möchte mein Onkel den Reichstag besichtigen, und nachmittags wollen wir im Einkaufszentrum bummeln.",
                "Vormittags möchte mein Onkel den Reichstag besichtigen, und nachmittags wollen wir im Einkaufszentrum bummeln"
            ],
            "'mein Onkel' (er) -> 'will ... besichtigen'; 'der Reichstag' ở Akkusativ là 'den Reichstag'; ở trong trung tâm thương mại (Wo? + Dativ) là 'im Einkaufszentrum'.",
            "Buổi sáng chú của tôi muốn tham quan Tòa nhà Quốc hội, và buổi chiều chúng tôi muốn đi dạo phố ở trung tâm thương mại = Am Vormittag will mein Onkel den Reichstag besichtigen, und am Nachmittag wollen wir im Einkaufszentrum bummeln."
        ),
        (
            "Câu 92: Dịch câu sau sang tiếng Đức: 'Đầu tiên các du khách đi xe buýt đến Cổng Brandenburg, và buổi tối họ đi vào trong Nhà hát Opera Quốc gia.'",
            "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper.",
            [
                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper.",
                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper",
                "Die Touristen fahren zuerst mit dem Bus zum Brandenburger Tor, und abends gehen sie in die Staatsoper.",
                "Die Touristen fahren zuerst mit dem Bus zum Brandenburger Tor, und abends gehen sie in die Staatsoper",
                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor und gehen am Abend in die Staatsoper.",
                "Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor und gehen am Abend in die Staatsoper"
            ],
            "Đi bằng xe buýt: 'mit dem Bus'; đến Cổng Brandenburg: 'zum Brandenburger Tor' (zu + dem); đi vào trong Nhà hát Opera Quốc gia: 'in die Staatsoper' (in + Akkusativ).",
            "Đầu tiên các du khách đi xe buýt đến Cổng Brandenburg, và buổi tối họ đi vào trong Nhà hát Opera Quốc gia = Zuerst fahren die Touristen mit dem Bus zum Brandenburger Tor, und am Abend gehen sie in die Staatsoper."
        ),
        (
            "Câu 93: Dịch câu sau sang tiếng Đức: 'Để đến được cảng biển, bạn phải đi xuyên qua cổng thành và đi ngang qua ngân hàng lớn.'",
            "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen.",
            [
                "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen.",
                "Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen",
                "Du musst durch das Stadttor gehen und an der großen Bank vorbeigehen, um zum Hafen zu kommen.",
                "Du musst durch das Stadttor gehen und an der großen Bank vorbeigehen, um zum Hafen zu kommen",
                "Wenn du zum Hafen willst, musst du durch das Stadttor und an der großen Bank vorbeigehen.",
                "Wenn du zum Hafen willst, musst du durch das Stadttor und an der großen Bank vorbeigehen"
            ],
            "Đến cảng biển: 'zum Hafen'; xuyên qua cổng thành: 'durch das Stadttor'; ngang qua ngân hàng lớn: 'an der großen Bank vorbei'.",
            "Để đến được cảng biển, bạn phải đi xuyên qua cổng thành và đi ngang qua ngân hàng lớn = Um zum Hafen zu kommen, musst du durch das Stadttor und an der großen Bank vorbeigehen."
        )
    ]

    for q, ans, acc, exp, trans in trans_sent_vd:
        ex_list.append({
            "type": "dich_cau_vd",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 30,
            "extra_data": {
                "accepted_answers": acc,
                "translation": trans
            }
        })

    # =========================================================================
    # NHÓM 9: DỊCH CÂU HOÀN CHỈNH ĐỨC -> VIỆT (7 CÂU: Q94 -> Q100)
    # =========================================================================
    trans_sent_dv = [
        (
            "Câu 94: Dịch câu chỉ đường sau sang tiếng Việt: „Gehen Sie vom Bahnhof aus zuerst dreihundert Meter geradeaus, dann an der Hauptpost vorbei und an der zweiten Ampel rechts!“",
            "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!",
            [
                "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!",
                "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai",
                "Từ phía nhà ga trước tiên bạn đi thẳng 300 mét, rồi đi qua bưu điện chính và tại đèn giao thông thứ hai thì rẽ phải!",
                "Từ phía nhà ga trước tiên bạn đi thẳng 300 mét, rồi đi qua bưu điện chính và tại đèn giao thông thứ hai thì rẽ phải",
                "Từ nhà ga đầu tiên bạn đi thẳng 300m, sau đó đi qua bưu điện chính và rẽ phải ở đèn giao thông thứ 2!",
                "Từ nhà ga đầu tiên bạn đi thẳng 300m, sau đó đi qua bưu điện chính và rẽ phải ở đèn giao thông thứ 2"
            ],
            "'vom Bahnhof aus' = từ nhà ga; 'an der Hauptpost vorbei' = ngang qua bưu điện chính; 'an der zweiten Ampel rechts' = rẽ phải ở đèn giao thông thứ hai.",
            "Từ nhà ga, đầu tiên Ngài hãy đi thẳng ba trăm mét, sau đó đi ngang qua bưu điện trung tâm và rẽ phải ở đèn giao thông thứ hai!"
        ),
        (
            "Câu 95: Dịch câu sau sang tiếng Việt: „Wenn ihr zum alten Schloss wollt, müsst ihr zuerst durch den Stadtpark laufen und danach die steinerne Brücke überqueren.“",
            "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá.",
            [
                "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá.",
                "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá",
                "Nếu các cậu muốn tới cung điện cổ thì trước tiên phải chạy xuyên qua công viên thành phố rồi đi qua cây cầu bằng đá.",
                "Nếu các cậu muốn tới cung điện cổ thì trước tiên phải chạy xuyên qua công viên thành phố rồi đi qua cây cầu bằng đá",
                "Nếu các bạn muốn đến lâu đài cổ, các bạn phải đi xuyên qua công viên thành phố và sau đó đi qua cây cầu đá.",
                "Nếu các bạn muốn đến lâu đài cổ, các bạn phải đi xuyên qua công viên thành phố và sau đó đi qua cây cầu đá"
            ],
            "'durch den Stadtpark laufen' = đi bộ/chạy xuyên qua công viên thành phố; 'die steinerne Brücke überqueren' = băng qua cây cầu đá.",
            "Nếu các bạn muốn đến lâu đài cổ, đầu tiên các bạn phải đi bộ xuyên qua công viên thành phố và tiếp theo băng qua cây cầu đá."
        ),
        (
            "Câu 96: Dịch câu sau sang tiếng Việt: „Der Bus Linie 200 fährt am Alexanderplatz, am Berliner Dom und an der Humboldt-Universität vorbei bis zum Zoologischen Garten.“",
            "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú.",
            [
                "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú.",
                "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú",
                "Xe buýt tuyến 200 đi ngang qua quảng trường Alexander, Nhà thờ lớn Berlin và trường Đại học Humboldt tới tận Sở thú.",
                "Xe buýt tuyến 200 đi ngang qua quảng trường Alexander, Nhà thờ lớn Berlin và trường Đại học Humboldt tới tận Sở thú",
                "Tuyến xe buýt 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt đến tận Vườn bách thú.",
                "Tuyến xe buýt 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt đến tận Vườn bách thú"
            ],
            "Cấu trúc 'an + Dativ + vorbeifahren' với cả danh từ giống đực ('am') và giống cái ('an der').",
            "Tuyến xe buýt số 200 chạy ngang qua Quảng trường Alexander, Nhà thờ lớn Berlin và Đại học Humboldt cho đến Vườn bách thú."
        ),
        (
            "Câu 97: Dịch câu sau sang tiếng Việt: „Entschuldigen Sie bitte, können Sie mir auf dem Stadtplan zeigen, wie ich zu Fuß zum Bundeskanzleramt komme?“",
            "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?",
            [
                "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?",
                "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không",
                "Cho tôi xin lỗi, bạn có thể chỉ giúp tôi trên bản đồ thành phố đường đi bộ tới Phủ Thủ tướng được không?",
                "Cho tôi xin lỗi, bạn có thể chỉ giúp tôi trên bản đồ thành phố đường đi bộ tới Phủ Thủ tướng được không",
                "Xin lỗi, bạn có thể chỉ cho tôi trên bản đồ làm thế nào tôi đi bộ đến Phủ Thủ tướng được không?",
                "Xin lỗi, bạn có thể chỉ cho tôi trên bản đồ làm thế nào tôi đi bộ đến Phủ Thủ tướng được không"
            ],
            "'auf dem Stadtplan zeigen' = chỉ trên bản đồ thành phố; 'zu Fuß zum Bundeskanzleramt kommen' = đi bộ đến Phủ Thủ tướng.",
            "Xin lỗi Ngài, Ngài có thể chỉ cho tôi trên bản đồ thành phố làm thế nào tôi đi bộ đến được Phủ Thủ tướng không?"
        ),
        (
            "Câu 98: Dịch câu sau sang tiếng Việt: „Spaziert einfach zwanzig Minuten das Flussufer entlang, dann seht ihr auf der linken Seite die berühmte Museumsinsel!“",
            "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!",
            [
                "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!",
                "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái",
                "Các cậu hãy tản bộ dọc bờ sông 20 phút rồi sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái!",
                "Các cậu hãy tản bộ dọc bờ sông 20 phút rồi sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái",
                "Các bạn cứ đi dạo 20 phút dọc bờ sông, sau đó các bạn sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái!",
                "Các bạn cứ đi dạo 20 phút dọc bờ sông, sau đó các bạn sẽ thấy Đảo Bảo tàng nổi tiếng ở bên trái"
            ],
            "'das Flussufer entlang' = dọc theo bờ sông; 'auf der linken Seite' = ở phía bên tay trái.",
            "Các bạn cứ đi dạo dọc theo bờ sông hai mươi phút, sau đó các bạn sẽ nhìn thấy Đảo Bảo tàng nổi tiếng ở phía bên tay trái!"
        ),
        (
            "Câu 99: Dịch câu sau sang tiếng Việt: „Am Vormittag wollen die Studenten in die Alte Nationalgalerie gehen, aber am Abend möchten sie lieber einen Film im Kino sehen.“",
            "Vào buổi sáng các sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn.",
            [
                "Vào buổi sáng các sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn.",
                "Vào buổi sáng các sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn",
                "Buổi sáng những người sinh viên muốn vào Khu triển lãm Quốc gia Cũ, nhưng buổi tối họ muốn xem phim trong rạp hơn.",
                "Buổi sáng những người sinh viên muốn vào Khu triển lãm Quốc gia Cũ, nhưng buổi tối họ muốn xem phim trong rạp hơn",
                "Buổi sáng sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng buổi tối họ thích xem một bộ phim trong rạp chiếu phim hơn.",
                "Buổi sáng sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng buổi tối họ thích xem một bộ phim trong rạp chiếu phim hơn"
            ],
            "Đối chiếu 'in die Alte Nationalgalerie gehen' (Wohin? + Akkusativ) và 'im Kino sehen' (Wo? + Dativ).",
            "Vào buổi sáng các sinh viên muốn đi vào Khu triển lãm Quốc gia Cũ, nhưng vào buổi tối họ lại thích xem một bộ phim ở trong rạp chiếu phim hơn."
        ),
        (
            "Câu 100: Dịch câu sau sang tiếng Việt: „Biegen Sie bitte vor dem großen Einkaufszentrum links ab, fahren Sie durch den kurzen Tunnel und halten Sie direkt neben der Bank!“",
            "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!",
            [
                "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!",
                "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng",
                "Hãy quẹo trái ở phía trước trung tâm mua sắm lớn, chạy xuyên qua hầm ngắn và đỗ ngay cạnh ngân hàng!",
                "Hãy quẹo trái ở phía trước trung tâm mua sắm lớn, chạy xuyên qua hầm ngắn và đỗ ngay cạnh ngân hàng",
                "Xin bạn hãy rẽ trái trước trung tâm thương mại lớn, lái xe qua đường hầm ngắn và dừng ngay bên cạnh ngân hàng!",
                "Xin bạn hãy rẽ trái trước trung tâm thương mại lớn, lái xe qua đường hầm ngắn và dừng ngay bên cạnh ngân hàng"
            ],
            "'vor dem großen Einkaufszentrum' = trước trung tâm thương mại lớn; 'durch den kurzen Tunnel' = xuyên qua đường hầm ngắn; 'neben der Bank' = bên cạnh ngân hàng.",
            "Xin Ngài hãy rẽ trái trước trung tâm thương mại lớn, lái xe xuyên qua đường hầm ngắn và dừng lại ngay bên cạnh ngân hàng!"
        )
    ]

    for q, ans, acc, exp, trans in trans_sent_dv:
        ex_list.append({
            "type": "dich_cau_dv",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": {
                "accepted_answers": acc,
                "translation": trans
            }
        })

    print(f"Total exercises created: {len(ex_list)}")
    assert len(ex_list) == 100, f"Expected 100 exercises, got {len(ex_list)}"

    # Generate lessons/a1/seed_a1_b8.py content
    lesson_script = f'''import json
import os
import sys

true = True
false = False
null = None

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from database import get_connection

def seed_lesson_8():
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

    cursor.execute("SELECT id FROM lessons WHERE level_id = ? AND title LIKE 'Bài 8%';", (a1_id,))
    existing_lesson = cursor.fetchone()
    lesson_id = existing_lesson["id"] if existing_lesson else 22

    # Xóa dữ liệu cũ của Bài 8 nếu có để cập nhật sạch sẽ (Bảo toàn tuyệt đối Bài 1 -> Bài 7)
    cursor.execute("DELETE FROM vocabularies WHERE lesson_id = ?;", (lesson_id,))
    cursor.execute("DELETE FROM exercises WHERE lesson_id = ?;", (lesson_id,))

    lesson_title = 'Bài 8: "Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu (Thành phố Berlin - Định hướng Bản đồ & Modalverben)"'

    grammar_html = """{grammar_html}"""

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
    # DANH MỤC 50 TỪ VỰNG TRỌNG TÂM BÀI 8 (KHỚP 100% VỚI LEXIKON_DB.JS)
    # =========================================================================
    vocab_raw = {json.dumps(vocab_list, ensure_ascii=False, indent=8)}

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

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # 100 BÀI TẬP ĐỘC NHẤT BÀI 8 (CHUẨN 9 DẠNG BÀI - ZERO BUG & KHÔNG LỘ GỢI Ý)
    # =========================================================================
    exercises_raw = {json.dumps(ex_list, ensure_ascii=False, indent=8)}

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
    print("✅ Đã khởi tạo thành công Bài 8: 'Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng (Zero Spoilers)!")

if __name__ == "__main__":
    seed_lesson_8()
'''

    output_path = os.path.join(BASE_DIR, "lessons", "a1", "seed_a1_b8.py")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(lesson_script)

    print(f"Successfully generated {output_path}!")

if __name__ == "__main__":
    build_lesson_8_seed()
