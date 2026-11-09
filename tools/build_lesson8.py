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
        ('Schule', 'die', 'die', 'die Schulen', 'eine Schule', 'keine Schule', 'trường học', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Schulen).', 'Die Kinder gehen jeden Morgen zur Schule.', 'Những đứa trẻ đi đến trường học mỗi buổi sáng.'),
        ('Brücke', 'die', 'die', 'die Brücken', 'eine Brücke', 'keine Brücke', 'cây cầu', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Brücken). Đi qua cầu: über die Brücke.', 'Paula und Alex laufen über die Schlossbrücke.', 'Paula và Alex đi bộ qua cầu Schlossbrücke.'),
        ('Bank', 'die', 'die', 'die Banken / die Bänke', 'eine Bank', 'keine Bank', 'ngân hàng / ghế băng dài', cat1, 'Phân biệt 2 nghĩa: Ngân hàng có số nhiều là die Banken; Ghế băng dài có số nhiều là die Bänke. Đi ngang qua: an der Bank vorbei.', 'Dann gehen Sie die erste Straße rechts, an der Bank vorbei.', 'Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.'),
        ('Post', 'die', 'die', 'nur Singular', 'eine Post', 'keine Post', 'bưu điện, ngành bưu chính', cat1, 'Danh từ giống cái (die), thường chỉ dùng ở số ít (nur Singular). Đi tới bưu điện: zur Post.', 'Rechts neben der Ampel sehen Sie die Post.', 'Ở bên phải cạnh đèn giao thông, Ngài sẽ nhìn thấy bưu điện.'),
        ('Straße', 'die', 'die', 'die Straßen', 'eine Straße', 'keine Straße', 'con đường, phố', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Straßen). Đi dọc theo con đường: die Straße entlang.', 'Gehen Sie bitte diese Straße entlang bis zur Kreuzung!', 'Xin Ngài hãy đi dọc theo con đường này cho đến ngã tư!'),
        ('Ampel', 'die', 'die', 'die Ampeln', 'eine Ampel', 'keine Ampel', 'đèn giao thông', cat1, 'Danh từ giống cái (die), số nhiều thêm -n (die Ampeln). Cho đến đèn giao thông: bis zur Ampel.', 'Gehen Sie geradeaus bis zur Ampel!', 'Ngài hãy đi thẳng cho đến đèn giao thông!'),
        ('Kreuzung', 'die', 'die', 'die Kreuzungen', 'eine Kreuzung', 'keine Kreuzung', 'ngã tư, giao lộ', cat1, 'Hậu tố -ung luôn mang giống cái (die), số nhiều thêm -en (die Kreuzungen). Cho đến ngã tư: bis zur Kreuzung.', 'An der zweiten Kreuzung biegen Sie bitte rechts ab!', 'Tại ngã tư thứ hai xin Ngài hãy rẽ phải!'),
        ('Disko', 'die', 'die', 'die Diskos', 'eine Disko', 'keine Disko', 'vũ trường, quán bar nhạc', cat1, 'Danh từ giống cái (die), số nhiều thêm -s (die Diskos). Đi vào vũ trường: in die Disko.', 'Am Abend gehen die Jugendlichen in die Disko.', 'Vào buổi tối các bạn thanh thiếu niên đi vào vũ trường.'),
        ('Schloss', 'das', 'das', 'die Schlösser', 'ein Schloss', 'kein Schloss', 'lâu đài, cung điện', cat1, 'Danh từ giống trung (das), số nhiều biến âm o -> ö và thêm -er (die Schlösser).', 'In Deutschland gibt es viele alte Schlösser.', 'Ở nước Đức có rất nhiều lâu đài cổ kính.'),
        ('Stadttor', 'das', 'das', 'die Stadttore', 'ein Stadttor', 'kein Stadttor', 'cổng thành', cat1, 'Danh từ ghép giống trung (die Stadt + das Tor), số nhiều: die Stadttore. Đi xuyên qua cổng: durch das Stadttor.', 'Die Touristen gehen durch das alte Stadttor.', 'Các du khách đi xuyên qua cổng thành cổ.'),
        ('Kino', 'das', 'das', 'die Kinos', 'ein Kino', 'kein Kino', 'rạp chiếu phim', cat1, 'Danh từ giống trung (das), số nhiều thêm -s (die Kinos). Đi vào rạp chiếu phim: ins Kino (in + das).', 'Heute Abend wollen wir noch einen Film im Kino sehen.', 'Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim.'),
        ('Krankenhaus', 'das', 'das', 'die Krankenhäuser', 'ein Krankenhaus', 'kein Krankenhaus', 'bệnh viện', cat1, 'Danh từ ghép giống trung (krank + das Haus), số nhiều: die Krankenhäuser.', 'Der Arzt arbeitet jeden Tag im Krankenhaus.', 'Bác sĩ làm việc mỗi ngày ở trong bệnh viện.'),
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
        ('Museumsinsel', 'die', 'die', 'nur Singular', 'eine Museumsinsel', 'keine Museumsinsel', 'Đảo Bảo tàng Berlin', cat2, 'Quần thể bảo tàng di sản UNESCO mang giống cái (vì die Insel - hòn đảo). Đi tới: zur Museumsinsel.', 'Auf der Museumsinsel liegen fünf weltberühmte Museen.', 'Trên Đảo Bảo tàng có năm viện bảo tàng nổi tiếng khắp thế giới.'),
        ('Alte Nationalgalerie', 'die', 'die', 'nur Singular', 'eine Alte Nationalgalerie', 'keine Alte Nationalgalerie', 'Khu triển lãm Quốc gia Cũ', cat2, 'Hậu tố -ie luôn mang giống cái (die). Đi vào trong: in die Alte Nationalgalerie.', 'Danach will ich in die Alte Nationalgalerie gehen.', 'Tiếp theo tôi muốn đi vào Khu triển lãm Quốc gia Cũ.'),
        ('Bundeskanzleramt', 'das', 'das', 'nur Singular', 'ein Bundeskanzleramt', 'kein Bundeskanzleramt', 'Phủ Thủ tướng Liên bang Đức', cat2, 'Trụ sở làm việc của Thủ tướng Đức mang giống trung (vì das Amt - cơ quan/phủ). Chạy xe ngang qua: am Bundeskanzleramt vorbei.', 'Sie fahren mit dem Bus am Bundeskanzleramt vorbei.', 'Họ đi xe buýt ngang qua Phủ Thủ tướng.'),
        ('Brandenburger Tor', 'das', 'das', 'nur Singular', 'ein Brandenburger Tor', 'kein Brandenburger Tor', 'Cổng thành Brandenburg', cat2, 'Biểu tượng lịch sử của Berlin và nước Đức mang giống trung (vì das Tor). Đi tới: zum Brandenburger Tor.', 'Paula und Alex gehen zum Brandenburger Tor und machen viele Fotos.', 'Paula và Alex đi đến Cổng Brandenburg và chụp nhiều bức ảnh.'),
        ('Schloss Bellevue', 'das', 'das', 'nur Singular', 'ein Schloss Bellevue', 'kein Schloss Bellevue', 'Cung điện Bellevue', cat2, 'Nơi làm việc của Tổng thống Đức mang giống trung (vì das Schloss).', 'Das Schloss Bellevue liegt direkt an der Spree in Berlin.', 'Cung điện Bellevue nằm ngay bên bờ sông Spree ở Berlin.'),
        ('Sony Center', 'das', 'das', 'nur Singular', 'ein Sony Center', 'kein Sony Center', 'Trung tâm phức hợp Sony', cat2, 'Trung tâm thương mại & rạp chiếu phim hiện đại mang giống trung (vì das Center).', 'Wir schauen uns das moderne Dach im Sony Center an.', 'Chúng tôi ngắm nhìn mái vòm hiện đại ở Trung tâm Sony.'),

        # 6 City orientation & Transport terms
        ('Stadtrundfahrt', 'die', 'die', 'die Stadtrundfahrten', 'eine Stadtrundfahrt', 'keine Stadtrundfahrt', 'chuyến tham quan thành phố', cat1, 'Danh từ ghép giống cái (die Stadt + die Fahrt), số nhiều: die Stadtrundfahrten.', 'Wir wollen heute eine Stadtrundfahrt in Berlin machen.', 'Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố ở Berlin.'),
        ('Fluss', 'der', 'der', 'die Flüsse', 'ein Fluss', 'kein Fluss', 'dòng sông', cat1, 'Danh từ giống đực (der), số nhiều biến âm u -> ü và thêm -e (die Flüsse).', 'Die Spree ist ein bekannter Fluss in Berlin.', 'Spree là một dòng sông nổi tiếng ở Berlin.'),
        ('Fußgänger', 'der', 'der', 'die Fußgänger', 'ein Fußgänger', 'kein Fußgänger', 'người đi bộ', cat1, 'Hậu tố -er chỉ người mang giống đực (der), giữ nguyên ở số nhiều (die Fußgänger).', 'An der Kreuzung müssen Fußgänger auf die Ampel achten.', 'Tại ngã tư người đi bộ phải chú ý đến đèn giao thông.'),
        ('Haltestelle', 'die', 'die', 'die Haltestellen', 'eine Haltestelle', 'keine Haltestelle', 'trạm dừng, điểm đỗ xe buýt / tàu', cat1, 'Danh từ ghép giống cái (die Stelle), số nhiều thêm -n (die Haltestellen).', 'Der Bus hält an der nächsten Haltestelle.', 'Chiếc xe buýt dừng lại ở trạm dừng tiếp theo.'),
        ('Ticket', 'das', 'das', 'die Tickets', 'ein Ticket', 'kein Ticket', 'vé (xe buýt, tàu hỏa, tham quan)', cat1, 'Từ vay mượn giống trung (das), số nhiều thêm -s (die Tickets).', 'Sie kauft ein Ticket für die Stadtrundfahrt.', 'Cô ấy mua một chiếc vé cho chuyến tham quan thành phố.'),
        ('Zentrum', 'das', 'das', 'die Zentren', 'ein Zentrum', 'kein Zentrum', 'trung tâm thành phố', cat1, 'Hậu tố -um đổi thành -en ở số nhiều: die Zentren. Giống trung (das). Đi tới trung tâm: ins Zentrum.', 'Die Museumsinsel liegt direkt im Zentrum von Berlin.', 'Đảo Bảo tàng nằm ngay tại trung tâm của Berlin.')
    ]

    vocab_list = []
    for w, art, gen, pl, ind, neg, m, cat, rule, ex, ex_vi in vocab_raw:
        vocab_list.append({
            "word": w,
            "article": art,
            "gender": gen,
            "plural": pl,
            "indefinite": ind,
            "negation": neg,
            "akkusativ": f"den / einen / keinen {w}" if art == "der" else (f"die / eine / keine {w}" if art == "die" else f"das / ein / kein {w}"),
            "meaning": m,
            "category": cat,
            "rule": rule,
            "example": ex,
            "example_vi": ex_vi
        })

    # 100 EXERCISES
    ex_list = []

    # -------------------------------------------------------------------------
    # NHÓM 1: TRẮC NGHIỆM (18 CÂU: Q1 -> Q18)
    # -------------------------------------------------------------------------
    mcqs = [
        (
            "Câu 1: Quan sát Sơ đồ chỉ đường e) bên trên và chọn câu lệnh tiếng Đức khớp chính xác với mũi tên:",
            ["Gehen Sie hier links.", "Gehen Sie die erste Straße links.", "Gehen Sie die zweite Straße links.", "Gehen Sie die zweite Straße rechts."],
            "Gehen Sie die zweite Straße links.",
            "Trên sơ đồ e), con đường chính có hai ngã rẽ bên trái, mũi tên đi thẳng bỏ qua ngã rẽ thứ nhất và quẹo vào ngã rẽ thứ hai bên tay trái -> 'Gehen Sie die zweite Straße links.'",
            {"visual_svg": "direction_card_e", "translation": "Ngài hãy rẽ trái ở con đường thứ hai."}
        ),
        (
            "Câu 2: Quan sát Sơ đồ chỉ đường b) bên trên: Mũi tên chỉ hành động đi ngang qua nhà thờ (die Kirche). Câu nào dưới đây đúng ngữ pháp 100%?",
            ["Gehen Sie an die Kirche vorbei.", "Gehen Sie an der Kirche vorbei.", "Gehen Sie durch die Kirche.", "Gehen Sie über der Kirche."],
            "Gehen Sie an der Kirche vorbei.",
            "Cấu trúc 'đi ngang qua bên cạnh một địa điểm' luôn dùng an + Dativ + vorbei. Vì die Kirche mang giống cái (Femininum), ở Dativ mạo từ die đổi thành der -> 'an der Kirche vorbei'.",
            {"visual_svg": "direction_card_b", "translation": "Ngài hãy đi ngang qua nhà thờ."}
        ),
        (
            "Câu 3: Quan sát Sơ đồ chỉ đường f) bên trên: Để chỉ đường 'Ngài hãy đi băng qua quảng trường (der Platz)', ta nói như thế nào?",
            ["Gehen Sie über dem Platz.", "Gehen Sie über den Platz.", "Gehen Sie an dem Platz vorbei.", "Gehen Sie bis zum Platz."],
            "Gehen Sie über den Platz.",
            "Đi băng qua một bề mặt không gian (Wohin? - có sự di chuyển) dùng giới từ über + Akkusativ. Danh từ giống đực der Platz sang Akkusativ đổi thành 'über den Platz'.",
            {"visual_svg": "direction_card_f", "translation": "Ngài hãy đi băng qua quảng trường."}
        ),
        (
            "Câu 4: Quan sát hai sơ đồ c) và d) bên trên: Vì cả 'die Ampel' (đèn giao thông) và 'die Kreuzung' (ngã tư) đều mang giống cái (Femininum), cụm giới từ 'đi cho đến...' nào dưới đây là đúng?",
            ["bis zu die Ampel / bis zu die Kreuzung", "bis zum Ampel / bis zum Kreuzung", "bis zur Ampel / bis zur Kreuzung", "bis an die Ampel / bis in die Kreuzung"],
            "bis zur Ampel / bis zur Kreuzung",
            "Giới từ kép 'bis zu' luôn đi với Cách 3 (Dativ). Với danh từ giống cái (die Ampel, die Kreuzung), zu + der viết tắt thành zur -> 'bis zur Ampel' và 'bis zur Kreuzung'.",
            {"visual_svg": "direction_card_c_and_d", "translation": "Đi cho đến đèn giao thông / Đi cho đến ngã tư."}
        ),
        (
            "Câu 5: Quan sát Sơ đồ i) bên trên: Chọn câu đúng ngữ pháp để diễn tả 'Ngài hãy đi dọc theo con đường Friedrich (die Friedrichstraße)':",
            ["Gehen Sie entlang der Friedrichstraße.", "Gehen Sie die Friedrichstraße entlang.", "Gehen Sie an der Friedrichstraße entlang vorbei.", "Gehen Sie durch die Friedrichstraße entlang."],
            "Gehen Sie die Friedrichstraße entlang.",
            "Khi dùng từ 'entlang' (dọc theo) đứng SAU danh từ, danh từ phía trước được chia ở Cách 4 (Akkusativ): 'Gehen Sie die Friedrichstraße entlang.'",
            {"visual_svg": "direction_card_i", "translation": "Ngài hãy đi dọc theo đường Friedrich."}
        ),
        (
            "Câu 6: Quan sát 2 hình minh họa đối chiếu bên trên và chọn cặp giới từ + mạo từ điền đúng vào câu: 'Zuerst gehen die Touristen ___ Stadttor (das Stadttor), und danach laufen sie ___ Brücke (die Brücke).'",
            ["über das / durch die", "durch das / über die", "durch dem / über der", "am / an der"],
            "durch das / über die",
            "Đi xuyên qua lòng cổng vòm dùng 'durch + Akkusativ' (durch das Stadttor); đi vượt qua mặt cầu dùng 'über + Akkusativ' (über die Brücke).",
            {"visual_svg": "spatial_contrast_tor_bruecke", "translation": "Đầu tiên các du khách đi xuyên qua cổng thành, và tiếp theo họ đi bộ qua cây cầu."}
        ),
        (
            "Câu 7: Hãy theo dõi lộ trình sau trên Bản đồ thành phố bên trên: 'Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei. Dann gehen Sie bis zur zweiten Kreuzung und dort links. Danach gehen Sie bis zur Ampel.' — Tòa nhà nằm ở bên tay phải (rechts) của bạn tại điểm cuối là gì?",
            ["das Kino", "die Bank", "die Post", "der Bahnhof"],
            "die Post",
            "Theo đúng hướng di chuyển từ dưới lên tới đèn giao thông (Ampel) trên bản đồ thành phố, phía bên tay phải (rechts) chính là 'die Post' (Bưu điện).",
            {"visual_svg": "city_grid_map_quiz_1", "translation": "Ở bên phải Ngài nhìn thấy bưu điện (die Post)."}
        ),
        (
            "Câu 8: Quan sát Lộ trình số 2 (màu xanh lá) trên bản đồ bên trên và chọn từ đúng điền vào chỗ trống: 'Zuerst gehen Sie geradeaus, bis zur ___ Kreuzung rechts. Dann gehen Sie geradeaus, ___ die Kreuzung. Links sehen Sie die Post.'",
            ["ersten / durch", "zweiten / über", "zweiten / an", "dritten / um"],
            "zweiten / über",
            "Đường màu xanh lá đi thẳng tới ngã tư thứ hai ('bis zur zweiten Kreuzung rechts'), sau đó đi thẳng băng qua ngã tư tiếp theo ('über die Kreuzung').",
            {"visual_svg": "city_grid_map_quiz_2", "translation": "Đầu tiên Ngài đi thẳng đến ngã tư thứ hai rẽ phải, sau đó đi thẳng băng qua ngã tư."}
        ),
        (
            "Câu 9: Dòng nào dưới đây liệt kê ĐÚNG 100% cả mạo từ số ít và dạng số nhiều của các danh từ địa điểm trong thành phố?",
            [
                "der Bahnhof (die Bahnhofen) / das Schloss (die Schlosse) / das Einkaufszentrum (die Einkaufszentrums)",
                "der Bahnhof (die Bahnhöfe) / das Schloss (die Schlösser) / das Einkaufszentrum (die Einkaufszentren)",
                "das Bahnhof (die Bahnhöfe) / der Schloss (die Schlösser) / die Einkaufszentrum (die Einkaufszentren)",
                "der Hafen (die Hafen) / der Markt (die Markte) / der Platz (die Platze)"
            ],
            "der Bahnhof (die Bahnhöfe) / das Schloss (die Schlösser) / das Einkaufszentrum (die Einkaufszentren)",
            "der Bahnhof -> die Bahnhöfe (thêm Umlaut + -e); das Schloss -> die Schlösser (thêm Umlaut + -er); das Einkaufszentrum -> die Einkaufszentren (đuôi -um đổi thành -en).",
            {"translation": "Nhà ga (các nhà ga) / Lâu đài (các lâu đài) / Trung tâm thương mại (các trung tâm thương mại)."}
        ),
        (
            "Câu 10: Phát biểu ngữ pháp nào dưới đây về danh từ 'die Bank' và 'die Post' là CHÍNH XÁC NHẤT?",
            [
                "Danh từ 'die Post' có dạng số nhiều thông dụng là 'die Posten', còn 'die Bank' không có số nhiều.",
                "Danh từ 'die Post' (bưu điện) chỉ dùng ở số ít (nur Singular), còn 'die Bank' có số nhiều là 'die Banken' (các ngân hàng) hoặc 'die Bänke' (các ghế băng dài).",
                "Cả 'die Post' và 'die Bank' đều mang giống trung (das).",
                "Danh từ 'der Flughafen' mang giống trung vì chỉ địa điểm lớn."
            ],
            "Danh từ 'die Post' (bưu điện) chỉ dùng ở số ít (nur Singular), còn 'die Bank' có số nhiều là 'die Banken' (các ngân hàng) hoặc 'die Bänke' (các ghế băng dài).",
            "'die Post' (bưu điện) là danh từ chỉ dùng ở số ít (nur Singular). 'die Bank' khi mang nghĩa ngân hàng có số nhiều là die Banken, còn khi mang nghĩa ghế băng dài có số nhiều là die Bänke.",
            {"translation": "die Post chỉ dùng ở số ít; die Bank có 2 dạng số nhiều: die Banken (ngân hàng) và die Bänke (ghế dài)."}
        ),
        (
            "Câu 11: Nhóm danh lam thắng cảnh Berlin nào dưới đây có cả 3 địa danh đều mang GIỐNG TRUNG (das)?",
            [
                "der Reichstag, der Berliner Dom, der Fernsehturm",
                "die Humboldt-Universität, die Staatsoper, die Museumsinsel",
                "das Bundeskanzleramt, das Brandenburger Tor, das Schloss Bellevue",
                "das Alexanderplatz, das Friedrichstraße, das Sony Center"
            ],
            "das Bundeskanzleramt, das Brandenburger Tor, das Schloss Bellevue",
            "Cả 3 địa danh này đều có danh từ gốc ở cuối mang giống trung: das Amt -> das Bundeskanzleramt, das Tor -> das Brandenburger Tor, das Schloss -> das Schloss Bellevue (và das Sony Center).",
            {"translation": "Phủ Thủ tướng Liên bang, Cổng Brandenburg, Cung điện Bellevue."}
        ),
        (
            "Câu 12: Chọn cặp mạo từ đúng cho 2 địa danh nổi tiếng ở Berlin: '1. ___ Fernsehturm steht am Alexanderplatz. — 2. ___ Museumsinsel liegt im Zentrum von Berlin.'",
            ["Das / Die", "Der / Die", "Der / Das", "Die / Der"],
            "Der / Die",
            "der Turm (ngọn tháp) -> 'der Fernsehturm' (giống đực); die Insel (hòn đảo) -> 'die Museumsinsel' (giống cái).",
            {"translation": "1. Tháp truyền hình nằm ở quảng trường Alexander. — 2. Đảo Bảo tàng nằm ở trung tâm Berlin."}
        ),
        (
            "Câu 13: Chọn phương án đúng điền vào câu phân biệt 'zum' vs 'in den': 'Paula und Alex gehen zuerst ___ Brandenburger Tor (das Tor) und machen Fotos. Am Nachmittag gehen sie ___ Berliner Dom (der Dom) und hören ein Konzert.'",
            ["ins / zum", "zum / in den", "in das / im", "zur / in der"],
            "zum / in den",
            "Đi tới khu vực Cổng Brandenburg để chụp ảnh bên ngoài dùng zu + dem = 'zum Brandenburger Tor'. Đi hẳn vào bên trong Nhà thờ lớn Berlin (der Dom) nghe hòa nhạc dùng in + Akkusativ = 'in den Berliner Dom'.",
            {"translation": "Paula và Alex đầu tiên đi đến Cổng Brandenburg chụp ảnh. Buổi chiều họ đi vào Nhà thờ lớn Berlin nghe hòa nhạc."}
        ),
        (
            "Câu 14: Chọn cặp từ đúng hoàn thành câu miêu tả chuyến tham quan Berlin: 'Die Touristen fahren mit dem Bus ___ Bundeskanzleramt (das Amt) vorbei und laufen dann ___ Schlossbrücke (die Brücke).'",
            ["ans / über der", "am / über die", "durch das / an der", "beim / durch die"],
            "am / über die",
            "Đi ngang qua das Bundeskanzleramt dùng an + dem ... vorbei = 'am Bundeskanzleramt vorbei'. Đi bộ qua cầu die Schlossbrücke (Wohin? + Akkusativ) dùng 'über die Schlossbrücke'.",
            {"translation": "Các du khách đi xe buýt ngang qua Phủ Thủ tướng và sau đó đi bộ qua cầu Schlossbrücke."}
        ),
        (
            "Câu 15: Chọn cặp dạng chia đúng của động từ khuyết thiếu 'wollen': 'Wir ___ heute eine Stadtrundfahrt in Berlin machen, und danach ___ ich in die Alte Nationalgalerie gehen.'",
            ["wollt / will", "wollen / will", "wollen / wolle", "will / wollen"],
            "wollen / will",
            "Với động từ khuyết thiếu wollen, ngôi wir chia là 'wollen', còn ngôi ich biến đổi nguyên âm o -> i và không có đuôi thành 'will'.",
            {"translation": "Hôm nay chúng tôi muốn đi tham quan thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia Cũ."}
        ),
        (
            "Câu 16: Chọn phương án đúng hoàn thành câu đối thoại: 'Was ___ ihr heute Nachmittag machen? — Maria und ich ___ auf der Friedrichstraße bummeln.'",
            ["wollt / wollen", "willst / wollen", "wollen / wollt", "wollt / will"],
            "wollt / wollen",
            "Ngôi ihr (các bạn) chia là 'wollt'. Chủ ngữ ghép 'Maria und ich' tương đương với ngôi wir (chúng tôi) nên chia là 'wollen'.",
            {"translation": "Chiều nay các bạn muốn làm gì? — Maria và tôi muốn đi dạo phố trên đường Friedrich."}
        ),
        (
            "Câu 17: Chọn câu có cách chia động từ khuyết thiếu ĐÚNG NGỮ PHÁP 100%:",
            [
                "Mein Bruder willt nächstes Jahr in Deutschland studieren.",
                "Am Wochenende musst meine Schwester im Krankenhaus arbeiten.",
                "Lukas kann sehr gut kochen und will in Berlin ein Restaurant aufmachen.",
                "Wir möchten heute Abend einen Film im Kino seht."
            ],
            "Lukas kann sehr gut kochen und will in Berlin ein Restaurant aufmachen.",
            "Ở ngôi thứ 3 số ít (Lukas = er), động từ können chia là 'kann' và wollen chia là 'will' (tuyệt đối không thêm -t), động từ chính kochen và aufmachen đứng nguyên mẫu ở cuối câu.",
            {"translation": "Lukas có thể nấu ăn rất giỏi và muốn mở một nhà hàng ở Berlin."}
        ),
        (
            "Câu 18: Một du khách đứng ở nhà ga và muốn hỏi đường đi đến Nhà hát Opera Quốc gia (die Staatsoper). Câu hỏi nào dưới đây là ĐÚNG NGỮ PHÁP?",
            [
                "Entschuldigung, wie komme ich zum Staatsoper?",
                "Entschuldigung, wie komme ich zur Staatsoper?",
                "Entschuldigung, wo geht es in der Staatsoper?",
                "Entschuldigung, ich suche der Staatsoper."
            ],
            "Entschuldigung, wie komme ich zur Staatsoper?",
            "Danh từ die Staatsoper mang giống cái (Femininum), nên khi đi với giới từ zu + Dativ phải dùng zu + der = 'zur Staatsoper' (hoặc nếu dùng in + Akkusativ thì là 'in die Staatsoper').",
            {"translation": "Xin lỗi, làm thế nào tôi đi đến được Nhà hát Opera Quốc gia?"}
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

    # -------------------------------------------------------------------------
    # NHÓM 2: ĐIỀN KHUYẾT (15 CÂU: Q19 -> Q33)
    # -------------------------------------------------------------------------
    fill_ins = [
        (
            "Câu 19: Quan sát Sơ đồ chỉ đường a) bên trên và điền từ chỉ hướng thích hợp vào chỗ trống: 'Gehen Sie zuerst 200 Meter ___!'",
            "geradeaus",
            ["geradeaus"],
            "Đi thẳng về phía trước trong tiếng Đức là 'geradeaus'.",
            {"visual_svg": "direction_card_a", "translation": "Ngài hãy đi thẳng 200 mét trước tiên!"}
        ),
        (
            "Câu 20: Quan sát Sơ đồ chỉ đường h) bên trên và điền từ chỉ hướng thích hợp vào chỗ trống: 'An der Ampel gehen Sie bitte hier ___, nicht links!'",
            "rechts",
            ["rechts"],
            "Đối lập với links (bên trái) là 'rechts' (bên phải).",
            {"visual_svg": "direction_card_h", "translation": "Tại đèn giao thông xin Ngài hãy rẽ phải ở đây, đừng rẽ trái!"}
        ),
        (
            "Câu 21: Quan sát Sơ đồ chỉ đường bên trên và điền từ còn thiếu để hoàn thành cấu trúc 'đi ngang qua': 'Gehen Sie an der Humboldt-Universität ___ und dann die erste Straße links.'",
            "vorbei",
            ["vorbei"],
            "Cấu trúc đi ngang qua một địa điểm là an + Dativ + 'vorbei'.",
            {"visual_svg": "spatial_diagram_vorbei", "translation": "Ngài hãy đi ngang qua trường Đại học Humboldt rồi rẽ vào đường thứ nhất bên trái."}
        ),
        (
            "Câu 22: Điền giới từ thu gọn (an + dem) thích hợp vào chỗ trống: 'Der Sightseeing-Bus fährt ___ Bundeskanzleramt und ___ Reichstag vorbei.' (Gợi ý: das Bundeskanzleramt, der Reichstag)",
            "am",
            ["am"],
            "Cả das Bundeskanzleramt (giống trung) và der Reichstag (giống đực) khi đi với an + Dativ + vorbei đều gộp an + dem thành 'am'.",
            {"translation": "Chiếc xe buýt tham quan chạy ngang qua Phủ Thủ tướng và tòa nhà Quốc hội."}
        ),
        (
            "Câu 23: Quan sát Sơ đồ k) bên trên và điền giới từ chỉ sự xuyên qua (+ Akkusativ) vào chỗ trống: 'Die Besucher gehen ___ das Brandenburger Tor.'",
            "durch",
            ["durch", "durchs"],
            "Đi xuyên qua lòng cánh cổng vòm dùng giới từ 'durch' + Cách 4 (Akkusativ).",
            {"visual_svg": "direction_card_k", "translation": "Những người khách tham quan đi xuyên qua Cổng Brandenburg."}
        ),
        (
            "Câu 24: Quan sát Sơ đồ l) bên trên và điền giới từ chỉ hành động đi vượt qua mặt cầu vào chỗ trống: 'Paula und Alex laufen ___ die Schlossbrücke.'",
            "über",
            ["über", "ueber"],
            "Đi qua cầu, qua đường, qua quảng trường dùng 'über + Akkusativ'.",
            {"visual_svg": "direction_card_l", "translation": "Paula và Alex đi bộ qua cầu Schlossbrücke."}
        ),
        (
            "Câu 25: Điền hậu tố giới từ chỉ đường 'dọc theo' đứng sau danh từ ở Akkusativ: 'Gehen Sie bitte den Fluss Spree ___ bis zur Museumsinsel!'",
            "entlang",
            ["entlang"],
            "Cấu trúc [Danh từ ở Akkusativ] + 'entlang' có nghĩa là đi dọc theo (den Fluss entlang, die Straße entlang).",
            {"translation": "Xin Ngài hãy đi dọc theo sông Spree cho đến Đảo Bảo tàng!"}
        ),
        (
            "Câu 26: Điền cụm từ thu gọn (zu + der) vào chỗ trống: 'Gehen Sie immer geradeaus bis ___ zweiten Kreuzung!' (Gợi ý: die Kreuzung)",
            "zur",
            ["zur"],
            "'bis zu' luôn đi với Cách 3 (Dativ). die Kreuzung mang giống cái nên zu + der viết tắt là 'zur' (bis zur zweiten Kreuzung).",
            {"translation": "Ngài cứ đi thẳng mãi cho đến ngã tư thứ hai!"}
        ),
        (
            "Câu 27: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'In den Sommerferien ___ mein Sohn allein nach Berlin reisen.'",
            "will",
            ["will"],
            "Chủ ngữ 'mein Sohn' là ngôi thứ 3 số ít (er), động từ wollen chia thành 'will'.",
            {"dynamic_modal_wollen": True, "translation": "Trong kỳ nghỉ hè, con trai tôi muốn đi du lịch một mình đến Berlin."}
        ),
        (
            "Câu 28: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'Wohin ___ du heute Abend mit deinen Freunden gehen, Sofia?'",
            "willst",
            ["willst"],
            "Ngôi thứ 2 số ít (du) của động từ wollen là 'willst'.",
            {"dynamic_modal_wollen": True, "translation": "Tối nay bạn muốn đi đâu cùng với những người bạn của mình thế, Sofia?"}
        ),
        (
            "Câu 29: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'Heute Abend ___ wir noch einen spannenden Film im Kino sehen.'",
            "wollen",
            ["wollen"],
            "Ngôi thứ nhất số nhiều (wir) của động từ wollen giữ nguyên là 'wollen'.",
            {"dynamic_modal_wollen": True, "translation": "Tối nay chúng tôi còn muốn xem một bộ phim hấp dẫn ở trong rạp chiếu phim."}
        ),
        (
            "Câu 30: Điền cụm giới từ + mạo từ (in + den) thích hợp vào chỗ trống: 'Am Nachmittag gehen die Touristen ___ Berliner Dom und hören ein Orgelkonzert.' (Gợi ý: der Berliner Dom)",
            "in den",
            ["in den"],
            "Đi vào bên trong tòa nhà (Wohin? + Akkusativ) với danh từ giống đực der Berliner Dom dùng 'in den'.",
            {"dynamic_berlin_route": True, "translation": "Vào buổi chiều các du khách đi vào trong Nhà thờ lớn Berlin và nghe một buổi hòa nhạc đàn đại phong cầm."}
        ),
        (
            "Câu 31: Điền cụm giới từ + mạo từ (in + die) thích hợp vào chỗ trống: 'Nach dem Abendessen gehen Paula und Alex ___ Disko ‚Von Euch‘.' (Gợi ý: die Disko)",
            "in die",
            ["in die"],
            "die Disko mang giống cái, đi vào trong vũ trường (Wohin? + Akkusativ) dùng 'in die Disko'.",
            {"translation": "Sau bữa tối, Paula và Alex đi vào vũ trường 'Von Euch'."}
        ),
        (
            "Câu 32: Điền giới từ thu gọn (zu + dem) thích hợp vào chỗ trống: 'Entschuldigung, wie komme ich am schnellsten ___ Hauptbahnhof?' (Gợi ý: der Hauptbahnhof)",
            "zum",
            ["zum"],
            "der Hauptbahnhof mang giống đực, đi sau zu + Dativ gộp zu + dem thành 'zum Hauptbahnhof'.",
            {"translation": "Xin lỗi, làm thế nào tôi đi đến được nhà ga trung tâm nhanh nhất?"}
        ),
        (
            "Câu 33: Điền dạng số nhiều đúng của danh từ 'das Schloss' (lâu đài, cung điện) vào chỗ trống: 'In Deutschland und Österreich gibt es viele alte ___.'",
            "Schlösser",
            ["Schlösser", "Schloesser"],
            "Danh từ giống trung das Schloss khi chuyển sang số nhiều phải thêm Umlaut o -> ö và đuôi -er thành 'die Schlösser'.",
            {"translation": "Ở Đức và Áo có rất nhiều lâu đài cổ."}
        )
    ]

    for q, ans, acc, exp, extra in fill_ins:
        extra_data = {
            "accepted_answers": acc,
            "translation": extra.get("translation", "")
        }
        if "visual_svg" in extra:
            extra_data["visual_svg"] = extra["visual_svg"]
        if "dynamic_modal_wollen" in extra:
            extra_data["dynamic_modal_wollen"] = True
        if "dynamic_berlin_route" in extra:
            extra_data["dynamic_berlin_route"] = True

        ex_list.append({
            "type": "dien_khuyet",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": extra_data
        })

    # -------------------------------------------------------------------------
    # NHÓM 3: DỊCH TỪ / CỤM TỪ V -> Đ (12 CÂU: Q34 -> Q45)
    # -------------------------------------------------------------------------
    trans_vd = [
        ("Câu 34: Dịch sang tiếng Đức (kèm mạo từ số ít): 'cảng biển'", "der Hafen", ["der Hafen", "Hafen"], "Cảng biển là danh từ giống đực der Hafen (số nhiều: die Häfen).", "cảng biển: der Hafen"),
        ("Câu 35: Dịch sang tiếng Đức (kèm mạo từ số ít): 'cây cầu'", "die Brücke", ["die Brücke", "die Bruecke", "Brücke", "Bruecke"], "Cây cầu là danh từ giống cái die Brücke (số nhiều: die Brücken).", "cây cầu: die Brücke"),
        ("Câu 36: Dịch sang tiếng Đức (kèm mạo từ số ít): 'lâu đài / cung điện'", "das Schloss", ["das Schloss", "Schloss"], "Lâu đài / cung điện là danh từ giống trung das Schloss (số nhiều: die Schlösser).", "lâu đài, cung điện: das Schloss"),
        ("Câu 37: Dịch sang tiếng Đức (kèm mạo từ số ít): 'trung tâm thương mại'", "das Einkaufszentrum", ["das Einkaufszentrum", "Einkaufszentrum"], "Trung tâm thương mại là danh từ giống trung das Einkaufszentrum (số nhiều: die Einkaufszentren).", "trung tâm thương mại: das Einkaufszentrum"),
        ("Câu 38: Dịch sang tiếng Đức (kèm mạo từ số ít): 'cổng thành'", "das Stadttor", ["das Stadttor", "Stadttor"], "Cổng thành là danh từ ghép giống trung das Stadttor (số nhiều: die Stadttore).", "cổng thành: das Stadttor"),
        ("Câu 39: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Tòa nhà Quốc hội Đức'", "der Reichstag", ["der Reichstag", "Reichstag"], "Tòa nhà Quốc hội ở Berlin là der Reichstag.", "Tòa nhà Quốc hội Đức: der Reichstag"),
        ("Câu 40: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Phủ Thủ tướng Đức'", "das Bundeskanzleramt", ["das Bundeskanzleramt", "Bundeskanzleramt"], "Phủ Thủ tướng Liên bang Đức là danh từ giống trung das Bundeskanzleramt.", "Phủ Thủ tướng Đức: das Bundeskanzleramt"),
        ("Câu 41: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Đảo Bảo tàng'", "die Museumsinsel", ["die Museumsinsel", "Museumsinsel"], "Đảo Bảo tàng ở Berlin là danh từ giống cái die Museumsinsel.", "Đảo Bảo tàng: die Museumsinsel"),
        ("Câu 42: Dịch địa danh Berlin sau sang tiếng Đức (kèm mạo từ): 'Tháp truyền hình'", "der Fernsehturm", ["der Fernsehturm", "Fernsehturm"], "Tháp truyền hình là danh từ giống đực der Fernsehturm.", "Tháp truyền hình: der Fernsehturm"),
        ("Câu 43: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi cho đến đèn giao thông'", "bis zur Ampel gehen", ["bis zur Ampel gehen", "bis zur Ampel", "Gehen Sie bis zur Ampel"], "Đèn giao thông là die Ampel -> 'cho đến đèn giao thông' là bis zur Ampel.", "đi cho đến đèn giao thông: bis zur Ampel gehen"),
        ("Câu 44: Dịch cụm chỉ đường sau sang tiếng Đức: 'đi ngang qua ngân hàng'", "an der Bank vorbei", ["an der Bank vorbei", "an der Bank vorbeigehen", "Gehen Sie an der Bank vorbei"], "Ngân hàng là die Bank -> cấu trúc an + Dativ + vorbei là an der Bank vorbei.", "đi ngang qua ngân hàng: an der Bank vorbei"),
        ("Câu 45: Dịch cụm từ chỉ hoạt động du lịch sau sang tiếng Đức: 'thực hiện một chuyến tham quan vòng quanh thành phố'", "eine Stadtrundfahrt machen", ["eine Stadtrundfahrt machen", "Stadtrundfahrt machen"], "Chuyến tham quan thành phố là die Stadtrundfahrt -> eine Stadtrundfahrt machen.", "thực hiện chuyến tham quan thành phố: eine Stadtrundfahrt machen")
    ]

    for q, ans, acc, exp, trans in trans_vd:
        ex_list.append({
            "type": "dich_nghia_vd",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "accepted_answers": acc,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 4: DỊCH TỪ / CỤM TỪ Đ -> V (12 CÂU: Q46 -> Q57)
    # -------------------------------------------------------------------------
    trans_dv = [
        ("Câu 46: Dịch sang tiếng Việt: 'die Staatsoper'", "nhà hát Opera quốc gia", ["nhà hát Opera quốc gia", "nhà hát nhạc kịch quốc gia", "nhà hát opera nhà nước", "nhà hát opera"], "die Staatsoper là Nhà hát Opera Quốc gia tại Berlin.", "die Staatsoper: nhà hát Opera quốc gia"),
        ("Câu 47: Dịch sang tiếng Việt: 'der Berliner Dom'", "nhà thờ lớn Berlin", ["nhà thờ lớn Berlin", "nhà thờ chính tòa Berlin", "thánh đường Berlin"], "der Berliner Dom là Nhà thờ lớn Berlin.", "der Berliner Dom: nhà thờ lớn Berlin"),
        ("Câu 48: Dịch sang tiếng Việt: 'die Alte Nationalgalerie'", "khu triển lãm quốc gia cũ", ["khu triển lãm quốc gia cũ", "khu trưng bày nghệ thuật quốc gia", "phòng triển lãm quốc gia cổ", "khu triển lãm quốc gia"], "die Alte Nationalgalerie là Khu triển lãm Quốc gia (Cũ) nằm trên Đảo Bảo tàng ở Berlin.", "die Alte Nationalgalerie: khu triển lãm quốc gia cũ"),
        ("Câu 49: Dịch sang tiếng Việt: 'das Schloss Bellevue'", "cung điện Bellevue", ["cung điện Bellevue", "lâu đài Bellevue"], "das Schloss Bellevue là Cung điện Bellevue (nơi làm việc chính thức của Tổng thống Đức ở Berlin).", "das Schloss Bellevue: cung điện Bellevue"),
        ("Câu 50: Dịch sang tiếng Việt: 'Gehen Sie die erste Straße rechts!'", "Ngài hãy rẽ phải ở con đường thứ nhất", ["Ngài hãy rẽ phải ở con đường thứ nhất", "Hãy đi con đường đầu tiên bên phải", "Rẽ phải ở đường đầu tiên", "Ngài hãy đi đường thứ nhất bên tay phải"], "die erste Straße rechts = rẽ phải ở con đường thứ nhất / đầu tiên.", "Gehen Sie die erste Straße rechts!: Ngài hãy rẽ phải ở con đường thứ nhất"),
        ("Câu 51: Dịch sang tiếng Việt: 'Gehen Sie bis zur zweiten Kreuzung und dort links!'", "Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái", ["Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái", "Ngài hãy đi tới ngã tư thứ hai thì rẽ trái", "Ngài hãy đi cho đến ngã tư thứ hai và rẽ trái ở đó", "Ngài hãy đi đến ngã tư thứ hai và rẽ trái ở đó", "Đi đến ngã tư thứ hai rồi rẽ trái", "Hãy đi tới ngã tư thứ hai bên trái", "Đi đến ngã tư thứ hai rẽ trái"], "bis zur zweiten Kreuzung und dort links = đi đến ngã tư thứ hai và rẽ trái ở đó (thì rẽ trái).", "Gehen Sie bis zur zweiten Kreuzung und dort links!: Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái"),
        ("Câu 52: Dịch sang tiếng Việt: 'Gehen Sie über den Platz und durch das Stadttor!'", "Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành", ["Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành", "Hãy đi qua quảng trường và đi xuyên qua cổng thành", "Đi qua quảng trường và xuyên qua cổng thành"], "über den Platz = băng qua quảng trường; durch das Stadttor = xuyên qua cổng thành.", "Gehen Sie über den Platz und durch das Stadttor!: Ngài hãy đi băng qua quảng trường và xuyên qua cổng thành"),
        ("Câu 53: Dịch sang tiếng Việt: 'auf der Friedrichstraße bummeln'", "đi dạo phố trên đường Friedrich", ["đi dạo phố trên đường Friedrich", "dạo chơi mua sắm trên phố Friedrich", "tản bộ trên đường Friedrich", "đi dạo trên đường Friedrich"], "Động từ bummeln có nghĩa là đi dạo phố, tản bộ ngắm cảnh/cửa hàng.", "auf der Friedrichstraße bummeln: đi dạo phố trên đường Friedrich"),
        ("Câu 54: Dịch sang tiếng Việt: 'Entschuldigung, wie komme ich ins Kino?'", "Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?", ["Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?", "Xin lỗi, tôi đi tới rạp chiếu phim bằng cách nào?", "Xin lỗi, đi đến rạp chiếu phim như thế nào?", "Xin lỗi làm sao tôi đến rạp chiếu phim?"], "Wie komme ich ins Kino? là câu hỏi đường lịch sự để đi tới rạp chiếu phim.", "Entschuldigung, wie komme ich ins Kino?: Xin lỗi, làm thế nào tôi đi đến được rạp chiếu phim?"),
        ("Câu 55: Dịch sang tiếng Việt: 'Zuerst — Dann — Danach — Anschließend'", "Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó", ["Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó", "Trước tiên, sau đó, tiếp theo, tiếp nối sau đó", "Đầu tiên, sau đó, tiếp đó, sau cùng", "Đầu tiên - Sau đó - Tiếp theo - Tiếp đó"], "Bộ 4 trạng từ liên kết trình tự hành động khi chỉ đường và kể lịch trình.", "Zuerst - Dann - Danach - Anschließend: Đầu tiên - Sau đó - Tiếp theo - Tiếp ngay sau đó"),
        ("Câu 56: Dịch sang tiếng Việt: 'mit dem Bus am Bundeskanzleramt vorbeifahren'", "đi xe buýt ngang qua Phủ Thủ tướng", ["đi xe buýt ngang qua Phủ Thủ tướng", "chạy xe buýt ngang qua Phủ Thủ tướng", "đi xe bus ngang qua Phủ Thủ tướng"], "mit dem Bus = bằng xe buýt; am Bundeskanzleramt vorbeifahren = đi/chạy xe ngang qua Phủ Thủ tướng.", "mit dem Bus am Bundeskanzleramt vorbeifahren: đi xe buýt ngang qua Phủ Thủ tướng"),
        ("Câu 57: Dịch sang tiếng Việt: 'die Straße entlanggehen'", "đi bộ dọc theo con đường", ["đi bộ dọc theo con đường", "đi dọc theo con đường", "đi dọc phố"], "die Straße entlanggehen = đi bộ dọc theo chiều dài con đường.", "die Straße entlanggehen: đi bộ dọc theo con đường")
    ]

    for q, ans, acc, exp, trans in trans_dv:
        ex_list.append({
            "type": "dich_nghia_dv",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "accepted_answers": acc,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 5: NỐI Ô (10 BÀI: Q58 -> Q67, MỖI BÀI 4 CẶP = 40 MỆNH ĐỀ)
    # LƯU Ý BẮT BUỘC: KHÔNG HIỆN TIẾNG VIỆT TRONG Ô CHỌN; DỊCH ĐỦ 4 CẶP; GIẢI THÍCH ĐỦ 4 CẶP!
    # -------------------------------------------------------------------------
    noi_o_sets = [
        # 58
        (
            "Câu 58: Nối Sơ đồ Chỉ đường (Cột Trái) với Khẩu lệnh tiếng Đức tương ứng (Cột Phải):",
            [
                {"left": "Symbol a (↑)", "right": "Gehen Sie geradeaus."},
                {"left": "Symbol h (↱)", "right": "Gehen Sie hier rechts."},
                {"left": "Symbol g (↰)", "right": "Gehen Sie hier links."},
                {"left": "Symbol i (〰️)", "right": "Gehen Sie die Straße entlang."}
            ],
            "1. Symbol a (↑): Ngài hãy đi thẳng. | 2. Symbol h (↱): Ngài hãy rẽ phải ở đây. | 3. Symbol g (↰): Ngài hãy rẽ trái ở đây. | 4. Symbol i (〰️): Ngài hãy đi dọc theo con đường.",
            "Phân tích 4 biểu tượng sơ đồ: 1. Symbol a chỉ mũi tên đi thẳng (geradeaus). 2. Symbol h quẹo phải ngay tại ngã rẽ hiện tại (hier rechts). 3. Symbol g quẹo trái ngay tại ngã rẽ hiện tại (hier links). 4. Symbol i uốn lượn chạy dọc theo chiều dài con đường (die Straße entlang)."
        ),
        # 59
        (
            "Câu 59: Nối Sơ đồ Chỉ đường (Cột Trái) với Khẩu lệnh tiếng Đức tương ứng (Cột Phải):",
            [
                {"left": "Symbol c (Ampel)", "right": "Gehen Sie bis zur Ampel."},
                {"left": "Symbol d (Kreuzung)", "right": "Gehen Sie bis zur Kreuzung."},
                {"left": "Symbol b (Kirche)", "right": "Gehen Sie an der Kirche vorbei."},
                {"left": "Symbol f (Platz)", "right": "Gehen Sie über den Platz."}
            ],
            "1. Symbol c (Ampel): Ngài hãy đi cho đến đèn giao thông. | 2. Symbol d (Kreuzung): Ngài hãy đi cho đến ngã tư. | 3. Symbol b (Kirche): Ngài hãy đi ngang qua nhà thờ. | 4. Symbol f (Platz): Ngài hãy đi băng qua quảng trường.",
            "Phân tích 4 biểu tượng sơ đồ: 1. Symbol c dừng lại trước cột đèn giao thông (bis zur Ampel). 2. Symbol d dừng lại trước ngã tư (bis zur Kreuzung). 3. Symbol b đi lướt ngang qua mặt nhà thờ (an der Kirche vorbei). 4. Symbol f đi băng xuyên qua quảng trường tròn (über den Platz)."
        ),
        # 60
        (
            "Câu 60: Nối Cặp Danh từ Địa điểm (Cột Trái) với Dạng Số nhiều tương ứng (Cột Phải):",
            [
                {"left": "der Bahnhof & der Flughafen", "right": "die Bahnhöfe & die Flughäfen"},
                {"left": "das Schloss & das Krankenhaus", "right": "die Schlösser & die Krankenhäuser"},
                {"left": "das Einkaufszentrum & das Museum", "right": "die Einkaufszentren & die Museen"},
                {"left": "die Post", "right": "nur Singular (kein Plural)"}
            ],
            "1. der Bahnhof & der Flughafen: các nhà ga & các sân bay. | 2. das Schloss & das Krankenhaus: các lâu đài & các bệnh viện. | 3. das Einkaufszentrum & das Museum: các trung tâm thương mại & các viện bảo tàng. | 4. die Post: bưu điện (chỉ dùng ở số ít).",
            "Quy tắc số nhiều danh từ địa điểm: 1. der Bahnhof/Flughafen biến âm a -> ä và thêm đuôi -e (die Bahnhöfe, die Flughäfen). 2. das Schloss/Krankenhaus thêm Umlaut và đuôi -er (die Schlösser, die Krankenhäuser). 3. das Einkaufszentrum/Museum có đuôi -um đổi thành -en (die Einkaufszentren, die Museen). 4. die Post chỉ dùng ở số ít (nur Singular)."
        ),
        # 61
        (
            "Câu 61: Nối Danh lam Thắng cảnh Berlin (Cột Trái) với Giống & Nhóm kiến trúc tương ứng (Cột Phải):",
            [
                {"left": "der Reichstag & der Fernsehturm", "right": "Maskulinum: das Parlament & der Turm"},
                {"left": "der Berliner Dom & der Alexanderplatz", "right": "Maskulinum: die Kirche & der Platz"},
                {"left": "die Humboldt-Universität & die Staatsoper", "right": "Femininum: die Universität & die Oper"},
                {"left": "die Museumsinsel & die Friedrichstraße", "right": "Femininum: die Insel & die Straße"}
            ],
            "1. der Reichstag & der Fernsehturm: Giống đực - Tòa nhà Quốc hội & Tháp truyền hình. | 2. der Berliner Dom & der Alexanderplatz: Giống đực - Nhà thờ lớn Berlin & Quảng trường Alexander. | 3. die Humboldt-Universität & die Staatsoper: Giống cái - Trường Đại học Humboldt & Nhà hát Opera Quốc gia. | 4. die Museumsinsel & die Friedrichstraße: Giống cái - Đảo Bảo tàng & Phố mua sắm Friedrich.",
            "Quy tắc giống danh lam thắng cảnh: 1. der Tag -> der Reichstag, der Turm -> der Fernsehturm (đều giống đực). 2. der Dom -> der Berliner Dom, der Platz -> der Alexanderplatz (đều giống đực). 3. Đuôi -tät -> die Humboldt-Universität, die Oper -> die Staatsoper (đều giống cái). 4. die Insel -> die Museumsinsel, die Straße -> die Friedrichstraße (đều giống cái)."
        ),
        # 62
        (
            "Câu 62: Nối Danh lam Thắng cảnh Berlin (Cột Trái) với Giống & Chức năng tương ứng (Cột Phải):",
            [
                {"left": "das Brandenburger Tor", "right": "Neutrum: das Tor im Zentrum"},
                {"left": "das Bundeskanzleramt", "right": "Neutrum: das moderne Regierungsamt"},
                {"left": "das Schloss Bellevue", "right": "Neutrum: das weiße Schloss an der Spree"},
                {"left": "die Alte Nationalgalerie", "right": "Femininum: die Galerie für Kunst"}
            ],
            "1. das Brandenburger Tor: Giống trung - Cổng thành ở trung tâm. | 2. das Bundeskanzleramt: Giống trung - Phủ Thủ tướng Liên bang. | 3. das Schloss Bellevue: Giống trung - Cung điện của Tổng thống Liên bang. | 4. die Alte Nationalgalerie: Giống cái - Khu triển lãm nghệ thuật.",
            "Quy tắc giống danh lam thắng cảnh: 1. das Tor -> das Brandenburger Tor (giống trung). 2. das Amt -> das Bundeskanzleramt (giống trung). 3. das Schloss -> das Schloss Bellevue (giống trung). 4. Hậu tố -ie luôn mang giống cái -> die Alte Nationalgalerie."
        ),
        # 63
        (
            "Câu 63: Nối Mẫu Câu Hỏi Đường (Cột Trái) với Cấu trúc Ngữ pháp tương ứng (Cột Phải):",
            [
                {"left": "Entschuldigung, ich suche ...", "right": "+ Akkusativ: den Bahnhof / das Kino"},
                {"left": "Entschuldigung, wo ist ...?", "right": "+ Nominativ: der Bahnhof / das Kino"},
                {"left": "Entschuldigung, wie komme ich ...?", "right": "+ zum Bahnhof / zur Post / ins Kino"},
                {"left": "Entschuldigung, wo geht es ...?", "right": "+ zum Reichstag / zur Museumsinsel / ins Zentrum"}
            ],
            "1. Entschuldigung, ich suche ...: Xin lỗi, tôi đang tìm + Cách 4 (Akkusativ). | 2. Entschuldigung, wo ist ...?: Xin lỗi, ở đâu vậy + Cách 1 (Nominativ). | 3. Entschuldigung, wie komme ich ...?: Làm thế nào tôi đến được + zum/zur/ins. | 4. Entschuldigung, wo geht es ...?: Đi lối nào để tới + zum/zur/ins.",
            "Cấu trúc câu hỏi đường: 1. suchen đòi hỏi tân ngữ Cách 4 Akkusativ. 2. sein (ist) đi với chủ ngữ Cách 1 Nominativ. 3. wie komme ich hỏi phương hướng tới địa điểm (zu + Dativ hoặc in + Akkusativ). 4. wo geht es hỏi lối đi tới địa điểm (zum/zur/ins)."
        ),
        # 64
        (
            "Câu 64: Nối Giới từ Không gian (Cột Trái) với Cách Ngữ pháp & Ví dụ tương ứng (Cột Phải):",
            [
                {"left": "an ... vorbei", "right": "Dativ: an der Bank vorbei / am Dom vorbei"},
                {"left": "durch ...", "right": "Akkusativ: durch das Tor / durch den Park"},
                {"left": "über ...", "right": "Akkusativ: über die Brücke / über den Platz"},
                {"left": "... entlang", "right": "Akkusativ: die Straße entlang / den Fluss entlang"}
            ],
            "1. an ... vorbei: đi ngang qua bên cạnh + Cách 3 (Dativ). | 2. durch ...: đi xuyên qua lòng + Cách 4 (Akkusativ). | 3. über ...: đi băng qua mặt + Cách 4 (Akkusativ). | 4. ... entlang: đi dọc theo chiều dài (đứng sau danh từ ở Cách 4 Akkusativ).",
            "Ngữ pháp giới từ chỉ đường: 1. an + Dativ + vorbei chỉ hành động đi ngang qua địa điểm. 2. durch luôn đi với Akkusativ chỉ việc đi xuyên qua. 3. über đi với Akkusativ khi có chuyển động băng qua bề mặt. 4. entlang đặt sau danh từ ở Akkusativ chỉ việc đi dọc theo chiều dài."
        ),
        # 65
        (
            "Câu 65: Nối Chủ ngữ (Cột Trái) với Dạng chia đúng của Modalverb 'wollen' (Cột Phải):",
            [
                {"left": "ich / er / sie / es (wollen)", "right": "will"},
                {"left": "du (wollen & müssen)", "right": "willst / musst"},
                {"left": "wir / sie / Sie (wollen & möchten)", "right": "wollen / möchten"},
                {"left": "ihr (wollen & können)", "right": "wollt / könnt"}
            ],
            "1. ich / er / sie / es (wollen): muốn (ngôi ich và er/sie/es bằng nhau: will). | 2. du (wollen & müssen): bạn muốn/phải (thêm đuôi -st: willst, musst). | 3. wir / sie / Sie (wollen & möchten): chúng tôi/họ/Ngài muốn (dạng nguyên mẫu: wollen, möchten). | 4. ihr (wollen & können): các bạn muốn/có thể (thêm đuôi -t: wollt, könnt).",
            "Quy tắc chia Modalverb: 1. Ngôi ich và er/sie/es luôn giống hệt nhau và không có đuôi -t (ich will, er will). 2. Ngôi du luôn có đuôi -st (du willst, du musst). 3. Ngôi wir và sie/Sie luôn giữ nguyên đuôi -en giống nguyên mẫu (wir wollen, sie möchten). 4. Ngôi ihr luôn có đuôi -t (ihr wollt, ihr könnt)."
        ),
        # 66
        (
            "Câu 66: Nối Vế đầu Chặng Khám Phá Berlin của Paula & Alex (Cột Trái) với Vế sau tương ứng (Cột Phải):",
            [
                {"left": "Sie gehen zum Brandenburger Tor", "right": "und machen dort viele Fotos."},
                {"left": "Sie fahren mit dem Bus am Bundeskanzleramt vorbei", "right": "und laufen über die Schlossbrücke."},
                {"left": "Am Nachmittag gehen sie in den Berliner Dom", "right": "und hören ein Orgelkonzert."},
                {"left": "Am Abend essen sie Pizza", "right": "und gehen danach in die Disko „Von Euch“."}
            ],
            "1. Họ đi đến Cổng Brandenburg: và chụp nhiều bức ảnh ở đó. | 2. Họ đi xe buýt ngang qua Phủ Thủ tướng: và đi bộ qua cầu Schlossbrücke. | 3. Vào buổi chiều họ đi vào Nhà thờ lớn Berlin: và nghe một buổi hòa nhạc đàn đại phong cầm. | 4. Vào buổi tối họ ăn pizza: và sau đó đi vào vũ trường 'Von Euch'.",
            "Theo bài đọc Berlin sehen: 1. Paula và Alex đến Cổng Brandenburg chụp ảnh bên ngoài cổng (zum Brandenburger Tor). 2. Đi xe buýt ngang qua Phủ Thủ tướng (am Bundeskanzleramt vorbei) và qua cầu (über die Schlossbrücke). 3. Buổi chiều vào bên trong Nhà thờ lớn Berlin (in den Berliner Dom) nghe hòa nhạc. 4. Buổi tối ăn pizza và đi vào vũ trường (in die Disko)."
        ),
        # 67
        (
            "Câu 67: Nối Trạng từ Trình tự Thời gian (Cột Trái) với Hành động Chỉ đường trên Bản đồ (Cột Phải):",
            [
                {"left": "Zuerst", "right": "gehen Sie geradeaus."},
                {"left": "Dann", "right": "gehen Sie die erste Straße rechts, an der Bank vorbei."},
                {"left": "Danach", "right": "gehen Sie bis zur zweiten Kreuzung und dort links, bis zur Ampel."},
                {"left": "Rechts", "right": "sehen Sie die Post."}
            ],
            "1. Zuerst: Đầu tiên Ngài đi thẳng. | 2. Dann: Sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng. | 3. Danach: Tiếp theo Ngài đi đến ngã tư thứ hai và rẽ trái ở đó, đi cho đến đèn giao thông. | 4. Rechts: Ở bên phải Ngài sẽ nhìn thấy bưu điện.",
            "Khung trình tự chỉ đường Lộ trình 1: 1. Zuerst mở đầu hành trình đi thẳng từ điểm xuất phát. 2. Dann chỉ bước tiếp theo rẽ phải qua ngân hàng. 3. Danach chỉ chặng kế tiếp đi đến ngã tư thứ hai rẽ trái ở đó và đến đèn giao thông. 4. Rechts chỉ vị trí đích đến của tòa nhà bưu điện nằm bên tay phải."
        )
    ]

    for q, pairs, trans, exp in noi_o_sets:
        # Xáo trộn cột phải
        clean_pairs = []
        for p in pairs:
            clean_pairs.append({"left": p["left"], "right": p["right"]})
        
        # correct_answer là chuỗi chuẩn
        corr_ans = " | ".join([f"{p['left']} = {p['right']}" for p in clean_pairs])
        ex_list.append({
            "type": "noi_o",
            "question": q,
            "options": None,
            "correct_answer": corr_ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "noi_o_pairs": clean_pairs,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 6: ĐIỀN TẠO CÂU KÈM BẢN ĐỒ / ĐOẠN VĂN (10 CÂU: Q68 -> Q77)
    # -------------------------------------------------------------------------
    create_sent = [
        (
            "Câu 68: Quan sát Bản đồ Lộ trình 1 bên trên và điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Dann gehen Sie die erste Straße [1], an der Bank [2].' (Gợi ý: 'Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.')",
            "rechts / vorbei",
            ["rechts / vorbei", "rechts/vorbei", "rechts, vorbei"],
            "Rẽ phải là 'rechts'; đi ngang qua ngân hàng là 'an der Bank vorbei'. Bạn cần điền đủ cả 2 từ ngăn cách bởi dấu /.",
            {"visual_svg": "city_grid_map_quiz_1", "translation": "Sau đó Ngài hãy rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."}
        ),
        (
            "Câu 69: Quan sát Bản đồ Lộ trình 2 bên trên và điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Zuerst gehen Sie geradeaus, bis [1] zweiten Kreuzung rechts. Dann gehen Sie [2] die Kreuzung.' (Gợi ý: 'Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai bên phải, sau đó đi băng qua ngã tư.')",
            "zur / über",
            ["zur / über", "zur/über", "zur / ueber", "zur/ueber"],
            "'Cho đến ngã tư thứ hai' là bis zur zweiten Kreuzung; 'băng qua ngã tư' là über die Kreuzung. Bạn cần điền đủ cả 2 từ ngăn cách bởi dấu /.",
            {"visual_svg": "city_grid_map_quiz_2", "translation": "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai bên phải, sau đó đi băng qua ngã tư."}
        ),
        (
            "Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Sie fahren mit dem Bus [1] Bundeskanzleramt vorbei und laufen [2] die Schlossbrücke.' (Gợi ý: 'Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.')",
            "am / über",
            ["am / über", "am/über", "am / ueber", "am/ueber"],
            "das Bundeskanzleramt đi với an + Dativ + vorbei là 'am Bundeskanzleramt vorbei'; đi bộ qua cầu die Schlossbrücke là 'über die Schlossbrücke'.",
            {"translation": "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."}
        ),
        (
            "Câu 71: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Geht zuerst [1] das Brandenburger Tor und dann die Straße [2]!' (Gợi ý: 'Đầu tiên các bạn hãy đi xuyên qua Cổng Brandenburg rồi đi dọc theo con đường.')",
            "durch / entlang",
            ["durch / entlang", "durch/entlang"],
            "Đi xuyên qua lòng cổng vòm là 'durch das Brandenburger Tor'; đi dọc theo con đường là 'die Straße entlang'.",
            {"translation": "Đầu tiên các bạn hãy đi xuyên qua Cổng Brandenburg rồi đi dọc theo con đường!"}
        ),
        (
            "Câu 72: Điền 2 dạng chia đúng của động từ 'wollen' vào các chỗ trống (ngăn cách bởi dấu /): 'Wir [1] noch eine Stadtrundfahrt machen, und danach [2] ich in die Nationalgalerie gehen.'",
            "wollen / will",
            ["wollen / will", "wollen/will"],
            "Ngôi wir chia là 'wollen', ngôi ich chia là 'will'.",
            {"translation": "Chúng mình còn muốn làm một chuyến tham quan thành phố, và sau đó mình muốn đi vào Khu triển lãm Quốc gia."}
        ),
        (
            "Câu 73: Điền 2 cụm từ thích hợp vào các chỗ trống (phân biệt 'zum' và 'in den', ngăn cách bởi dấu /): 'Am Vormittag gehen wir [1] Alexanderplatz, und am Nachmittag gehen wir [2] Berliner Dom.'",
            "zum / in den",
            ["zum / in den", "zum/in den"],
            "Đi đến quảng trường dùng 'zum Alexanderplatz' (zu + dem); đi vào bên trong lòng nhà thờ lớn dùng 'in den Berliner Dom' (in + Akkusativ).",
            {"translation": "Buổi sáng chúng tôi đi đến Quảng trường Alexander, và buổi chiều chúng tôi đi vào trong Nhà thờ lớn Berlin."}
        ),
        (
            "Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Anschließend [1] Maria und ich auf der Friedrichstraße [2].' (Gợi ý: 'wollen', 'đi dạo phố')",
            "wollen / bummeln",
            ["wollen / bummeln", "wollen/bummeln"],
            "Chủ ngữ 'Maria und ich' (wir) chia wollen ở vị trí số 2 là 'wollen', động từ nguyên mẫu 'bummeln' đứng cuối câu.",
            {"translation": "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."}
        ),
        (
            "Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Entschuldigung, ich [1] das Kino. Wie komme ich [2] Kino?' (Gợi ý: 'tìm kiếm', 'đến rạp')",
            "suche / ins",
            ["suche / ins", "suche/ins", "suche / zum", "suche/zum"],
            "'Tôi đang tìm' là ich suche; 'đến rạp chiếu phim' là ins Kino (in + das) hoặc zum Kino.",
            {"translation": "Xin lỗi, tôi đang tìm rạp chiếu phim. Làm thế nào tôi đi đến được rạp chiếu phim?"}
        ),
        (
            "Câu 76: Điền 2 động từ khuyết thiếu (müssen và wollen) chia theo ngôi 'ich' vào các chỗ trống (ngăn cách bởi dấu /): 'Am Wochenende [1] ich arbeiten, aber nächstes Jahr in Deutschland [2] ich studieren.'",
            "muss / will",
            ["muss / will", "muss/will"],
            "Ngôi ich của müssen là 'muss', của wollen là 'will'.",
            {"translation": "Vào cuối tuần tôi phải làm việc, nhưng sang năm ở Đức tôi muốn học đại học."}
        ),
        (
            "Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Gehen Sie bis zur [1]. Rechts [2] Sie die Post.' (Gợi ý: 'đèn giao thông', 'nhìn thấy')",
            "Ampel / sehen",
            ["Ampel / sehen", "Ampel/sehen"],
            "Đèn giao thông là 'die Ampel' (bis zur Ampel); nhìn thấy là 'sehen Sie'.",
            {"translation": "Ngài hãy đi cho đến đèn giao thông, ở bên phải Ngài sẽ nhìn thấy bưu điện."}
        )
    ]

    for q, ans, acc, exp, extra in create_sent:
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
            "exp_reward": 20,
            "extra_data": extra_data
        })

    # -------------------------------------------------------------------------
    # NHÓM 7: NGHE ĐIỀN TỪ (9 CÂU: Q78 -> Q86)
    # -------------------------------------------------------------------------
    listenings = [
        (
            "Câu 78: Nghe phát âm chuẩn de-DE và điền từ chỉ hướng còn thiếu vào chỗ trống:",
            "Zuerst gehen Sie geradeaus und dann die erste Straße rechts, an der Bank vorbei.",
            "Zuerst gehen Sie ___ und dann die erste Straße rechts, an der Bank vorbei.",
            "geradeaus",
            ["geradeaus"],
            "Đầu tiên Ngài đi thẳng và sau đó rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.",
            "Từ chỉ hướng 'đi thẳng' trong tiếng Đức là 'geradeaus'."
        ),
        (
            "Câu 79: Nghe phát âm chuẩn de-DE và điền danh từ còn thiếu vào chỗ trống:",
            "Gehen Sie bitte bis zur zweiten Kreuzung und dort links, danach bis zur Ampel.",
            "Gehen Sie bitte bis zur zweiten ___ und dort links, danach bis zur Ampel.",
            "Kreuzung",
            ["Kreuzung"],
            "Xin Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông.",
            "Danh từ 'die Kreuzung' có nghĩa là ngã tư, giao lộ (bis zur zweiten Kreuzung)."
        ),
        (
            "Câu 80: Nghe phát âm chuẩn de-DE và điền giới từ thu gọn còn thiếu vào chỗ trống:",
            "Paula und Alex gehen zum Brandenburger Tor und machen viele Fotos.",
            "Paula und Alex gehen ___ Brandenburger Tor und machen viele Fotos.",
            "zum",
            ["zum"],
            "Paula và Alex đi đến Cổng Brandenburg và chụp nhiều bức ảnh.",
            "zu + dem Brandenburger Tor viết tắt là 'zum Brandenburger Tor'."
        ),
        (
            "Câu 81: Nghe phát âm chuẩn de-DE và điền danh từ địa danh còn thiếu vào chỗ trống:",
            "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke.",
            "Sie fahren mit dem Bus am ___ vorbei und laufen über die Schlossbrücke.",
            "Bundeskanzleramt",
            ["Bundeskanzleramt"],
            "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.",
            "Phủ Thủ tướng Liên bang Đức là 'das Bundeskanzleramt' (am Bundeskanzleramt vorbei)."
        ),
        (
            "Câu 82: Nghe phát âm chuẩn de-DE và điền danh từ địa danh còn thiếu vào chỗ trống:",
            "Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert.",
            "Am Nachmittag gehen sie in den Berliner ___ und hören ein Konzert.",
            "Dom",
            ["Dom"],
            "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc.",
            "Nhà thờ lớn Berlin là 'der Berliner Dom' (in den Berliner Dom)."
        ),
        (
            "Câu 83: Nghe phát âm chuẩn de-DE và điền danh từ còn thiếu vào chỗ trống:",
            "Wir wollen heute eine Stadtrundfahrt in Berlin machen.",
            "Wir wollen heute eine ___ in Berlin machen.",
            "Stadtrundfahrt",
            ["Stadtrundfahrt"],
            "Hôm nay chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố ở Berlin.",
            "Danh từ 'die Stadtrundfahrt' có nghĩa là chuyến tham quan vòng quanh thành phố."
        ),
        (
            "Câu 84: Nghe phát âm chuẩn de-DE và điền động từ nguyên mẫu còn thiếu vào chỗ trống:",
            "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
            "Anschließend wollen Maria und ich auf der Friedrichstraße ___.",
            "bummeln",
            ["bummeln"],
            "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.",
            "Động từ nguyên mẫu 'bummeln' có nghĩa là đi dạo phố, tản bộ ngắm cảnh."
        ),
        (
            "Câu 85: Nghe phát âm chuẩn de-DE và điền danh từ còn thiếu vào chỗ trống:",
            "Gehen Sie bitte an der Kirche vorbei und dann über den Platz.",
            "Gehen Sie bitte an der ___ vorbei und dann über den Platz.",
            "Kirche",
            ["Kirche"],
            "Xin Ngài hãy đi ngang qua nhà thờ và sau đó đi băng qua quảng trường.",
            "Danh từ 'die Kirche' có nghĩa là nhà thờ (an der Kirche vorbei)."
        ),
        (
            "Câu 86: Nghe phát âm chuẩn de-DE và điền dạng chia của động từ 'wollen' vào chỗ trống:",
            "In Deutschland will mein Bruder an der Humboldt-Universität studieren.",
            "In Deutschland ___ mein Bruder an der Humboldt-Universität studieren.",
            "will",
            ["will"],
            "Ở Đức anh trai tôi muốn học đại học tại trường Đại học Humboldt.",
            "Động từ khuyết thiếu wollen chia ở ngôi thứ 3 số ít (mein Bruder) là 'will'."
        )
    ]

    for q, audio, disp, ans, acc, hint, exp in listenings:
        ex_list.append({
            "type": "nghe_dien",
            "question": q,
            "options": None,
            "correct_answer": ans,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "audio_text": audio,
                "display_sentence": disp,
                "hint_vi": hint,
                "accepted_answers": acc,
                "translation": hint
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 8: DỊCH CÂU V -> Đ (7 CÂU: Q87 -> Q93, ĐA ĐÁP ÁN LINH HOẠT)
    # -------------------------------------------------------------------------
    trans_sent_vd = [
        (
            "Câu 87: Dịch câu hỏi đường sau sang tiếng Đức: 'Xin lỗi, tôi đang tìm bưu điện. Làm thế nào tôi đi đến được bưu điện?'",
            "Entschuldigung, ich suche die Post. Wie komme ich zur Post?",
            [
                "Entschuldigung, ich suche die Post. Wie komme ich zur Post?",
                "Entschuldigung, ich suche die Post. Wo geht es zur Post?",
                "Entschuldigen Sie, ich suche die Post. Wie komme ich zur Post?",
                "Entschuldigung, ich suche die Post! Wie komme ich zur Post?",
                "Entschuldigen Sie bitte, ich suche die Post. Wie komme ich zur Post?"
            ],
            "die Post mang giống cái; sau ich suche (Akkusativ) là die Post, còn sau Wie komme ich ...? (zu + Dativ) là zur Post.",
            "Xin lỗi, tôi đang tìm bưu điện. Làm thế nào tôi đi đến được bưu điện?"
        ),
        (
            "Câu 88: Dịch câu chỉ đường sau sang tiếng Đức: 'Đầu tiên Ngài đi thẳng, sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng.'",
            "Zuerst gehen Sie geradeaus, dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
            [
                "Zuerst gehen Sie geradeaus, dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
                "Zuerst gehen Sie geradeaus. Dann gehen Sie die erste Straße rechts, an der Bank vorbei.",
                "Gehen Sie zuerst geradeaus und dann die erste Straße rechts, an der Bank vorbei.",
                "Zuerst gehen Sie geradeaus, dann die erste Straße rechts, an der Bank vorbei."
            ],
            "Zuerst gehen Sie geradeaus, die erste Straße rechts, và an der Bank vorbei (an + Dativ + vorbei).",
            "Đầu tiên Ngài đi thẳng, sau đó Ngài rẽ phải ở con đường thứ nhất, đi ngang qua ngân hàng."
        ),
        (
            "Câu 89: Dịch câu chỉ đường sau sang tiếng Đức: 'Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông.'",
            "Gehen Sie bis zur zweiten Kreuzung und dort links, danach gehen Sie bis zur Ampel.",
            [
                "Gehen Sie bis zur zweiten Kreuzung und dort links, danach gehen Sie bis zur Ampel.",
                "Gehen Sie bis zur zweiten Kreuzung und dort links und danach bis zur Ampel.",
                "Dann gehen Sie bis zur zweiten Kreuzung und dort links. Danach gehen Sie bis zur Ampel.",
                "Gehen Sie bitte bis zur zweiten Kreuzung und dort links und danach bis zur Ampel.",
                "Gehen Sie bitte bis zur zweiten Kreuzung und dort links, danach gehen Sie bis zur Ampel.",
                "Gehen Sie bis zur zweiten Kreuzung links, danach gehen Sie bis zur Ampel.",
                "Gehen Sie bis zur zweiten Kreuzung links und danach bis zur Ampel.",
                "Dann gehen Sie bis zur zweiten Kreuzung links. Danach gehen Sie bis zur Ampel."
            ],
            "Đi đến ngã tư thứ hai và rẽ trái ở đó: 'bis zur zweiten Kreuzung und dort links'; cho đến đèn giao thông: 'bis zur Ampel' (bis zu + der Dativ).",
            "Ngài hãy đi cho đến ngã tư thứ hai thì rẽ trái, tiếp theo đi cho đến đèn giao thông."
        ),
        (
            "Câu 90: Dịch câu sau sang tiếng Đức: 'Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke.'",
            "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke.",
            [
                "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und laufen über die Schlossbrücke.",
                "Sie fahren mit dem Bus am Bundeskanzleramt vorbei und gehen über die Schlossbrücke.",
                "Sie fahren mit dem Bus am Bundeskanzleramt vorbei, und laufen über die Schlossbrücke."
            ],
            "am Bundeskanzleramt vorbei (an + dem ... vorbei) và über die Schlossbrücke (über + Akkusativ).",
            "Họ đi xe buýt ngang qua Phủ Thủ tướng và đi bộ qua cầu Schlossbrücke."
        ),
        (
            "Câu 91: Dịch câu sau sang tiếng Đức: 'Chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia.'",
            "Wir wollen eine Stadtrundfahrt machen, und danach will ich in die Nationalgalerie gehen.",
            [
                "Wir wollen eine Stadtrundfahrt machen, und danach will ich in die Nationalgalerie gehen.",
                "Wir wollen noch eine Stadtrundfahrt machen. Danach will ich in die Nationalgalerie gehen.",
                "Wir wollen eine Stadtrundfahrt machen. Danach will ich in die Alte Nationalgalerie gehen.",
                "Wir wollen eine Stadtrundfahrt machen und danach will ich in die Alte Nationalgalerie gehen."
            ],
            "Wir wollen ... machen (ngôi wir) và Danach will ich ... gehen (ngôi ich đảo động từ lên vị trí số 2).",
            "Chúng tôi muốn thực hiện một chuyến tham quan vòng quanh thành phố, và sau đó tôi muốn đi vào Khu triển lãm Quốc gia."
        ),
        (
            "Câu 92: Dịch câu sau sang tiếng Đức: 'Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich.'",
            "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
            [
                "Anschließend wollen Maria und ich auf der Friedrichstraße bummeln.",
                "Danach wollen Maria und ich auf der Friedrichstraße bummeln.",
                "Maria und ich wollen anschließend auf der Friedrichstraße bummeln.",
                "Anschließend möchten Maria und ich auf der Friedrichstraße bummeln."
            ],
            "Anschließend đứng đầu câu đảo wollen lên vị trí số 2, động từ nguyên mẫu bummeln đứng ở cuối câu.",
            "Tiếp ngay sau đó Maria và tôi muốn đi dạo phố trên đường Friedrich."
        ),
        (
            "Câu 93: Dịch câu sau sang tiếng Đức: 'Ngài hãy đi xuyên qua Cổng Brandenburg và đi băng qua quảng trường.'",
            "Gehen Sie durch das Brandenburger Tor und über den Platz.",
            [
                "Gehen Sie durch das Brandenburger Tor und über den Platz.",
                "Gehen Sie durch das Brandenburger Tor und gehen Sie über den Platz.",
                "Bitte gehen Sie durch das Brandenburger Tor und über den Platz.",
                "Gehen Sie durch das Brandenburger Tor, und über den Platz."
            ],
            "durch das Brandenburger Tor (durch + Akkusativ) và über den Platz (über + Akkusativ).",
            "Ngài hãy đi xuyên qua Cổng Brandenburg và đi băng qua quảng trường."
        )
    ]

    for q, ans, acc, exp, trans in trans_sent_vd:
        ex_list.append({
            "type": "dich_cau_vd",
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

    # -------------------------------------------------------------------------
    # NHÓM 9: DỊCH CÂU Đ -> V (7 CÂU: Q94 -> Q100, ĐA ĐÁP ÁN LINH HOẠT)
    # -------------------------------------------------------------------------
    trans_sent_dv = [
        (
            "Câu 94: Dịch câu sau sang tiếng Việt: 'Zuerst gehen Sie geradeaus, bis zur zweiten Kreuzung rechts. Dann gehen Sie geradeaus, über die Kreuzung. Links sehen Sie die Post.'",
            "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện.",
            [
                "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện.",
                "Trước tiên hãy đi thẳng đến ngã tư thứ hai bên phải. Sau đó đi thẳng băng qua ngã tư. Bên trái bạn sẽ thấy bưu điện.",
                "Đầu tiên Ngài đi thẳng tới ngã tư thứ hai bên tay phải, sau đó đi thẳng qua ngã tư, bên trái Ngài thấy bưu điện.",
                "Đầu tiên bạn đi thẳng đến ngã tư thứ hai bên phải. Sau đó bạn đi thẳng qua ngã tư. Bên trái bạn sẽ thấy bưu điện."
            ],
            "Đây là toàn bộ câu miêu tả Lộ trình số 2 trên bản đồ chỉ đường tới Bưu điện (die Post).",
            "Đầu tiên Ngài đi thẳng cho đến ngã tư thứ hai thì rẽ phải. Sau đó Ngài đi thẳng, băng qua ngã tư. Ở bên trái Ngài sẽ nhìn thấy bưu điện."
        ),
        (
            "Câu 95: Dịch câu sau sang tiếng Việt: 'Paula und Alex kommen aus Madrid. Sie besuchen Freunde in Berlin und gehen zuerst zum Brandenburger Tor.'",
            "Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg.",
            [
                "Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg.",
                "Paula và Alex tới từ Madrid, họ đến thăm bạn bè tại Berlin và trước tiên đi tới Cổng Brandenburg.",
                "Paula và Alex đến từ Madrid. Họ đến thăm bạn bè ở Berlin và trước hết đi đến Cổng Brandenburg.",
                "Paula và Alex đến từ Madrid. Họ thăm bạn bè ở Berlin và đầu tiên đi tới Cổng Brandenburg."
            ],
            "besuchen Freunde = thăm bạn bè; gehen zum Brandenburger Tor = đi đến Cổng Brandenburg.",
            "Paula và Alex đến từ Madrid. Họ thăm những người bạn ở Berlin và đầu tiên đi đến Cổng Brandenburg."
        ),
        (
            "Câu 96: Dịch câu sau sang tiếng Việt: 'Am Nachmittag gehen sie in den Berliner Dom und hören ein Konzert. Am Abend gehen sie in die Disko.'",
            "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường.",
            [
                "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường.",
                "Buổi chiều họ vào trong Nhà thờ lớn Berlin nghe hòa nhạc, buổi tối họ đi tới quán bar vũ trường.",
                "Vào buổi chiều họ vào Nhà thờ lớn Berlin và nghe hòa nhạc. Vào buổi tối họ đi vào vũ trường.",
                "Buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe hòa nhạc. Buổi tối họ đi vũ trường."
            ],
            "in den Berliner Dom = vào trong Nhà thờ lớn Berlin; in die Disko = vào trong vũ trường.",
            "Vào buổi chiều họ đi vào Nhà thờ lớn Berlin và nghe một buổi hòa nhạc. Vào buổi tối họ đi vào vũ trường."
        ),
        (
            "Câu 97: Dịch câu sau sang tiếng Việt: 'Gehen Sie bitte an der Kirche vorbei, dann die Lạch-Tray-Straße entlang bis zur Ampel!'",
            "Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!",
            [
                "Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!",
                "Hãy đi ngang qua nhà thờ rồi đi dọc đường Lạch Tray tới chỗ đèn giao thông!",
                "Xin hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray đến đèn giao thông!",
                "Xin bạn hãy đi ngang qua nhà thờ, sau đó đi dọc đường Lạch Tray cho đến đèn giao thông!"
            ],
            "an der Kirche vorbei = đi ngang qua nhà thờ; die Lạch-Tray-Straße entlang = đi dọc theo đường Lạch Tray; bis zur Ampel = cho đến đèn giao thông.",
            "Xin Ngài hãy đi ngang qua nhà thờ, sau đó đi dọc theo đường Lạch Tray cho đến đèn giao thông!"
        ),
        (
            "Câu 98: Dịch câu sau sang tiếng Việt: 'Heute Abend wollen wir noch einen Film im Kino sehen, aber am Wochenende muss ich arbeiten.'",
            "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc.",
            [
                "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc.",
                "Tối nay chúng mình còn muốn xem phim ở rạp nhưng cuối tuần mình phải đi làm.",
                "Tối nay chúng tôi muốn xem một bộ phim trong rạp chiếu phim, nhưng cuối tuần tôi phải làm việc.",
                "Tối nay chúng tôi còn muốn xem một bộ phim ở rạp chiếu phim, nhưng cuối tuần tôi phải làm việc."
            ],
            "Kết hợp hai động từ khuyết thiếu: wollen (muốn - kế hoạch) và müssen (phải - nghĩa vụ công việc).",
            "Tối nay chúng tôi còn muốn xem một bộ phim ở trong rạp chiếu phim, nhưng vào cuối tuần tôi phải làm việc."
        ),
        (
            "Câu 99: Dịch câu sau sang tiếng Việt: 'Entschuldigung, wie komme ich zur Museumsinsel und zur Humboldt-Universität?'",
            "Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?",
            [
                "Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?",
                "Xin lỗi cho hỏi tôi đi tới Đảo Bảo tàng và Đại học Humboldt bằng cách nào?",
                "Xin lỗi, tôi đi đến Đảo Bảo tàng và trường Đại học Humboldt như thế nào?",
                "Xin lỗi, làm sao để tôi đi đến Đảo Bảo tàng và trường Đại học Humboldt?"
            ],
            "Cả die Museumsinsel và die Humboldt-Universität đều mang giống cái nên đi với zur (zu + der).",
            "Xin lỗi, làm thế nào tôi đi đến được Đảo Bảo tàng và trường Đại học Humboldt?"
        ),
        (
            "Câu 100: Dịch câu sau sang tiếng Việt: 'Die Touristen gehen durch das alte Stadttor, laufen über den Marktplatz und besichtigen das schöne Schloss.'",
            "Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ.",
            [
                "Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ.",
                "Những người khách du lịch đi qua cổng thành cũ, băng qua quảng trường chợ và tham quan lâu đài tuyệt đẹp.",
                "Các khách du lịch đi xuyên qua cổng thành cổ, đi bộ qua quảng trường chợ và tham quan lâu đài đẹp.",
                "Du khách đi xuyên qua cổng thành cổ, đi bộ qua quảng trường chợ và tham quan cung điện đẹp."
            ],
            "durch das alte Stadttor = xuyên qua cổng thành cổ; über den Marktplatz = băng qua quảng trường chợ; besichtigen das schöne Schloss = tham quan lâu đài/cung điện đẹp.",
            "Các du khách đi xuyên qua cổng thành cổ, đi bộ băng qua quảng trường chợ và tham quan cung điện đẹp đẽ."
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
            art,
            meaning,
            example_str
        ))

    cursor.executemany("""
        INSERT INTO vocabularies (lesson_id, german_word, article, vietnamese_meaning, example_sentence)
        VALUES (?, ?, ?, ?, ?);
    """, vocabularies)

    # =========================================================================
    # KHO 100 CÂU HỎI BÀI TẬP ĐỘC NHẤT BÀI 8 (9 NHÓM DẠNG CHUẨN)
    # =========================================================================
    raw_exercises = {json.dumps(ex_list, ensure_ascii=False, indent=8)}

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
    print("✅ Đã khởi tạo thành công Bài 8: 'Stadt - Hỏi đường / Chỉ đường - Động từ khuyết thiếu' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_8()
'''

    output_path = os.path.join(BASE_DIR, "lessons", "a1", "seed_a1_b8.py")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(lesson_script)
    print(f"Successfully generated {output_path}!")

if __name__ == "__main__":
    build_lesson_8_seed()
