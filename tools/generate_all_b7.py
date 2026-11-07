import os
import sys
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tools.build_lesson7_seed import generate_seed_script

def build_full_seed_script():
    grammar_html = generate_seed_script()

    # 50 VOCABULARIES
    cat1 = 'Danh từ Nghề nghiệp Nam & Nữ (Berufe - Bài 7)'
    cat2 = 'Nơi làm việc & Hoạt động Công việc (Arbeitsorte & Alltag - Bài 7)'

    vocab_raw = [
        # 32 Berufe
        ('Programmierer', 'der', 'der', 'die Programmierer', 'ein Programmierer', 'kein Programmierer', 'nam lập trình viên', cat1, 'Danh từ giống đực (der Programmierer). Số nhiều giữ nguyên die Programmierer.', 'Paula Rausch arbeitet mit einem Programmierer im Büro zusammen.', 'Paula Rausch làm việc cùng một nam lập trình viên ở văn phòng.'),
        ('Programmiererin', 'die', 'die', 'die Programmiererinnen', 'eine Programmiererin', 'keine Programmiererin', 'nữ lập trình viên', cat1, 'Danh từ giống cái kết thúc bằng -in. Số nhiều gấp đôi -nn thành die Programmiererinnen.', 'Paula Rausch ist 35 Jahre alt und arbeitet als Programmiererin.', 'Paula Rausch 35 tuổi và làm nghề nữ lập trình viên.'),
        ('Taxifahrer', 'der', 'der', 'die Taxifahrer', 'ein Taxifahrer', 'kein Taxifahrer', 'nam tài xế taxi', cat1, 'Danh từ giống đực (der Taxifahrer). Nghề nghiệp nói sein + Taxifahrer hoặc arbeiten als Taxifahrer.', 'Mein Onkel arbeitet seit fünf Jahren als Taxifahrer in Hamburg.', 'Chú tôi làm nghề tài xế taxi ở Hamburg từ 5 năm nay.'),
        ('Taxifahrerin', 'die', 'die', 'die Taxifahrerinnen', 'eine Taxifahrerin', 'keine Taxifahrerin', 'nữ tài xế taxi', cat1, 'Danh từ giống cái. Số nhiều thêm -nen: die Taxifahrerinnen.', 'Frau Becker ist eine erfahrene Taxifahrerin in Berlin.', 'Bà Becker là một nữ tài xế taxi giàu kinh nghiệm ở Berlin.'),
        ('Krankenpfleger', 'der', 'der', 'die Krankenpfleger', 'ein Krankenpfleger', 'kein Krankenpfleger', 'nam điều dưỡng / y tá', cat1, 'Danh từ giống đực chỉ nam y tá, chăm sóc bệnh nhân trong bệnh viện.', 'Der Krankenpfleger hilft dem Arzt jeden Tag im Krankenhaus.', 'Người nam điều dưỡng giúp đỡ bác sĩ mỗi ngày ở bệnh viện.'),
        ('Krankenpflegerin', 'die', 'die', 'die Krankenpflegerinnen', 'eine Krankenpflegerin', 'keine Krankenpflegerin', 'nữ điều dưỡng / y tá', cat1, 'Danh từ giống cái chỉ nữ y tá (hoặc die Krankenschwester).', 'Meine Tante arbeitet als Krankenpflegerin auf der Station.', 'Dì tôi làm nghề nữ điều dưỡng ở khoa điều trị.'),
        ('Florist', 'der', 'der', 'die Floristen', 'ein Florist', 'kein Florist', 'nam nhân viên bán hoa / cắm hoa', cat1, 'Danh từ giống đực thuộc nhóm N-Deklination: số nhiều die Floristen.', 'Der Florist bindet wunderschöne Blumen für die Hochzeit.', 'Người nam thợ hoa bó những bông hoa tuyệt đẹp cho đám cưới.'),
        ('Floristin', 'die', 'die', 'die Floristinnen', 'eine Floristin', 'keine Floristin', 'nữ nhân viên bán hoa', cat1, 'Danh từ giống cái (die Floristin). Nơi làm việc im Blumengeschäft.', 'Die Floristin verkauft schöne Blumen im Blumengeschäft.', 'Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa.'),
        ('Verkäufer', 'der', 'der', 'die Verkäufer', 'ein Verkäufer', 'kein Verkäufer', 'nam nhân viên bán hàng', cat1, 'Danh từ giống đực. Bán hàng trong siêu thị hoặc cửa hàng.', 'Der Verkäufer berät die Kunden freundlich im Supermarkt.', 'Nam nhân viên bán hàng tư vấn khách hàng thân thiện ở siêu thị.'),
        ('Verkäuferin', 'die', 'die', 'die Verkäuferinnen', 'eine Verkäuferin', 'keine Verkäuferin', 'nữ nhân viên bán hàng', cat1, 'Danh từ giống cái (die Verkäuferin). Số nhiều die Verkäuferinnen.', 'Die Verkäuferin verkauft moderne Schuhe im Schuhgeschäft.', 'Nữ nhân viên bán hàng bán những đôi giày hiện đại ở trong cửa hàng giày.'),
        ('Mechatroniker', 'der', 'der', 'die Mechatroniker', 'ein Mechatroniker', 'kein Mechatroniker', 'nam thợ cơ khí ô tô', cat1, 'Thợ cơ khí điện tử ô tô (KFZ-Mechatroniker), làm việc in einer Werkstatt.', 'Der Mechatroniker repariert das Auto in einer Werkstatt.', 'Người thợ cơ khí sửa chiếc ô tô ở trong một xưởng sửa chữa.'),
        ('Mechatronikerin', 'die', 'die', 'die Mechatronikerinnen', 'eine Mechatronikerin', 'keine Mechatronikerin', 'nữ thợ cơ khí ô tô', cat1, 'Nữ thợ cơ khí ô tô (KFZ-Mechatronikerin).', 'Sie lernt fleißig und möchte Mechatronikerin werden.', 'Cô ấy học tập chăm chỉ và muốn trở thành nữ thợ cơ khí.'),
        ('Trainer', 'der', 'der', 'die Trainer', 'ein Trainer', 'kein Trainer', 'nam huấn luyện viên', cat1, 'Danh từ giống đực (der Trainer), làm việc im Fitnessstudio hoặc im Stadion.', 'Der Trainer leitet das Training im Fitnessstudio.', 'Huấn luyện viên phụ trách buổi tập ở phòng gym.'),
        ('Trainerin', 'die', 'die', 'die Trainerinnen', 'eine Trainerin', 'keine Trainerin', 'nữ huấn luyện viên', cat1, 'Danh từ giống cái (die Trainerin), số nhiều die Trainerinnen.', 'Unsere Trainerin hilft den Sportlern jeden Tag im Stadion.', 'Nữ huấn luyện viên của chúng tôi giúp đỡ các vận động viên mỗi ngày ở sân vận động.'),
        ('Lehrer', 'der', 'der', 'die Lehrer', 'ein Lehrer', 'kein Lehrer', 'nam giáo viên', cat1, 'Danh từ giống đực (der Lehrer). Cấu trúc Er ist Lehrer von Beruf không dùng mạo từ.', 'Frank Müller ist Lehrer von Beruf und hat jetzt Ferien.', 'Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ.'),
        ('Lehrerin', 'die', 'die', 'die Lehrerinnen', 'eine Lehrerin', 'keine Lehrerin', 'nữ giáo viên', cat1, 'Danh từ giống cái (die Lehrerin). Giảng dạy ở trường: an einer Schule unterrichten.', 'Die Lehrerin unterrichtet Schüler an einer Schule in Berlin.', 'Nữ giáo viên giảng dạy học sinh tại một trường học ở Berlin.'),
        ('Schüler', 'der', 'der', 'die Schüler', 'ein Schüler', 'kein Schüler', 'nam học sinh (phổ thông)', cat1, 'Danh từ giống đực (der Schüler), học sinh cấp 1 đến cấp 3.', 'Der Schüler lernt viele Fächer in der Schule.', 'Cậu học sinh học nhiều môn học ở trường.'),
        ('Schülerin', 'die', 'die', 'die Schülerinnen', 'eine Schülerin', 'keine Schülerin', 'nữ học sinh (phổ thông)', cat1, 'Danh từ giống cái (die Schülerin), số nhiều die Schülerinnen.', 'Anna ist eine fleißige Schülerin am Gymnasium.', 'Anna là một nữ học sinh chăm chỉ tại trường THPT (Gymnasium).'),
        ('Student', 'der', 'der', 'die Studenten', 'ein Student', 'kein Student', 'nam sinh viên (đại học)', cat1, 'Danh từ giống đực nhóm N-Deklination: der Student, des Studenten, die Studenten.', 'Der Student studiert Informatik an der Universität.', 'Nam sinh viên học ngành công nghệ thông tin tại trường đại học.'),
        ('Studentin', 'die', 'die', 'die Studentinnen', 'eine Studentin', 'keine Studentin', 'nữ sinh viên (đại học)', cat1, 'Danh từ giống cái (die Studentin). Học đại học: an der Universität studieren.', 'Die Studentin liest viele deutsche Fachbücher in der Bibliothek.', 'Nữ sinh viên đọc nhiều sách chuyên ngành tiếng Đức trong thư viện.'),
        ('Sekretär', 'der', 'der', 'die Sekretäre', 'ein Sekretär', 'kein Sekretär', 'nam thư ký', cat1, 'Danh từ giống đực (der Sekretär), số nhiều die Sekretäre.', 'Der Sekretär vereinbart wichtige Termine mit Kunden.', 'Nam thư ký sắp xếp các cuộc hẹn quan trọng với khách hàng.'),
        ('Sekretärin', 'die', 'die', 'die Sekretärinnen', 'eine Sekretärin', 'keine Sekretärin', 'nữ thư ký', cat1, 'Danh từ giống cái (die Sekretärin). Viết email và gọi điện: E-Mails schreiben und Kunden anrufen.', 'Die Sekretärin schreibt E-Mails und ruft Kunden im Büro an.', 'Nữ thư ký viết email và gọi điện cho khách hàng ở văn phòng.'),
        ('Friseur', 'der', 'der', 'die Friseure', 'ein Friseur', 'kein Friseur', 'nam thợ cắt tóc', cat1, 'Danh từ giống đực (der Friseur). Nơi làm việc im Friseursalon.', 'Der Friseur schneidet meinem Bruder im Friseursalon die Haare.', 'Người thợ làm tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc.'),
        ('Friseurin', 'die', 'die', 'die Friseurinnen', 'eine Friseurin', 'keine Friseurin', 'nữ thợ làm tóc', cat1, 'Danh từ giống cái (die Friseurin), số nhiều die Friseurinnen.', 'Die Friseurin macht eine sehr schöne moderne Frisur.', 'Nữ thợ làm tóc làm một kiểu tóc hiện đại rất đẹp.'),
        ('Kellner', 'der', 'der', 'die Kellner', 'ein Kellner', 'kein Kellner', 'nam nhân viên phục vụ bàn', cat1, 'Danh từ giống đực (der Kellner). Phục vụ thực khách im Restaurant.', 'Der Kellner bringt den Gästen das Essen im Restaurant.', 'Người bồi bàn mang thức ăn cho thực khách ở nhà hàng.'),
        ('Kellnerin', 'die', 'die', 'die Kellnerinnen', 'eine Kellnerin', 'keine Kellnerin', 'nữ nhân viên phục vụ bàn', cat1, 'Danh từ giống cái (die Kellnerin), số nhiều die Kellnerinnen.', 'Die Kellnerin bedient Gäste freundlich im Café.', 'Nữ phục vụ bàn phục vụ thực khách thân thiện ở quán cà phê.'),
        ('Koch', 'der', 'der', 'die Köche', 'ein Koch', 'kein Koch', 'nam đầu bếp', cat1, 'Danh từ giống đực đặc biệt: số nhiều đổi biến âm die Köche.', 'Der Koch bereitet köstliche Gerichte in der Küche zu.', 'Người đầu bếp chuẩn bị những món ăn ngon tuyệt trong nhà bếp.'),
        ('Köchin', 'die', 'die', 'die Köchinnen', 'eine Köchin', 'keine Köchin', 'nữ đầu bếp', cat1, 'Danh từ giống cái đặc biệt: thêm Umlaut ö và đuôi -in thành die Köchin.', 'Frau Bui ist eine talentierte Köchin in einem Restaurant.', 'Bà Bùi là một nữ đầu bếp tài năng trong một nhà hàng.'),
        ('Arzt', 'der', 'der', 'die Ärzte', 'ein Arzt', 'kein Arzt', 'nam bác sĩ', cat1, 'Danh từ giống đực đặc biệt: số nhiều thêm Umlaut die Ärzte.', 'Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus.', 'Bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện.'),
        ('Ärztin', 'die', 'die', 'die Ärztinnen', 'eine Ärztin', 'keine Ärztin', 'nữ bác sĩ', cat1, 'Danh từ giống cái đặc biệt: thêm Umlaut ä và đuôi -in thành die Ärztin.', 'Die Ärztin hilft kranken Menschen mit großer Geduld.', 'Nữ bác sĩ giúp đỡ những người bệnh bằng sự kiên nhẫn to lớn.'),
        ('Hausmann', 'der', 'der', 'die Hausmänner', 'ein Hausmann', 'kein Hausmann', 'người đàn ông nội trợ', cat1, 'Danh từ giống đực (der Hausmann), số nhiều die Hausmänner.', 'Mein Onkel ist Hausmann und kümmert sich um die Kinder.', 'Chú tôi là người nội trợ và chăm sóc con cái.'),
        ('Hausfrau', 'die', 'die', 'die Hausfrauen', 'eine Hausfrau', 'keine Hausfrau', 'người phụ nữ nội trợ', cat1, 'Danh từ giống cái chuyển từ gốc -mann sang -frau: die Hausfrau.', 'Meine Großmutter war viele Jahre Hausfrau und kochte gern.', 'Bà tôi đã làm nội trợ nhiều năm và rất thích nấu ăn.'),

        # 18 Arbeitsorte & Alltag
        ('Friseursalon', 'der', 'der', 'die Friseursalons', 'ein Friseursalon', 'kein Friseursalon', 'tiệm làm tóc, salon tóc', cat2, 'Danh từ giống đực (der Friseursalon). Trả lời Wo? dùng im Friseursalon (in + dem).', 'Der Friseur arbeitet jeden Tag im Friseursalon.', 'Người thợ làm tóc làm việc mỗi ngày ở trong tiệm làm tóc.'),
        ('Supermarkt', 'der', 'der', 'die Supermärkte', 'ein Supermarkt', 'kein Supermarkt', 'siêu thị', cat2, 'Danh từ giống đực (der Supermarkt). Trả lời Wo? dùng im Supermarkt.', 'Frau Lindner kauft frische Lebensmittel im Supermarkt ein.', 'Bà Lindner mua thực phẩm tươi ở trong siêu thị.'),
        ('Kindergarten', 'der', 'der', 'die Kindergärten', 'ein Kindergarten', 'kein Kindergarten', 'trường mẫu giáo, nhà trẻ', cat2, 'Danh từ giống đực. Di chuyển Wohin? -> in den Kindergarten; ở lại Wo? -> im Kindergarten.', 'Um 8.30 Uhr bringt Frank seine Tochter in den Kindergarten.', 'Lúc 8 giờ 30 phút Frank đưa con gái vào trường mẫu giáo.'),
        ('Schule', 'die', 'die', 'die Schulen', 'eine Schule', 'keine Schule', 'trường học (phổ thông)', cat2, 'Danh từ giống cái (die Schule). Trả lời Wo? dùng an einer Schule hoặc in der Schule.', 'Frau Weber unterrichtet viele Schüler an einer Schule in Berlin.', 'Bà Weber giảng dạy nhiều học sinh tại một trường học ở Berlin.'),
        ('Universität', 'die', 'die', 'die Universitäten', 'eine Universität', 'keine Universität', 'trường đại học', cat2, 'Danh từ giống cái đuôi -tät. Trả lời Wo? dùng an der Universität / an einer Hochschule.', 'Mein Bruder studiert Informatik an der Universität.', 'Anh trai tôi học ngành tin học tại trường đại học.'),
        ('Werkstatt', 'die', 'die', 'die Werkstätten', 'eine Werkstatt', 'keine Werkstatt', 'xưởng sửa chữa', cat2, 'Danh từ giống cái (die Werkstatt). Di chuyển Wohin? -> in die Werkstatt; ở tại Wo? -> in der Werkstatt.', 'Der KFZ-Mechatroniker repariert das Auto in einer Werkstatt.', 'Người thợ cơ khí ô tô sửa chiếc xe trong một xưởng sửa chữa.'),
        ('Baustelle', 'die', 'die', 'die Baustellen', 'eine Baustelle', 'keine Baustelle', 'công trường xây dựng', cat2, 'Danh từ giống cái (die Baustelle). Trả lời Wo? dùng auf der Baustelle / auf einer Baustelle.', 'Die Arbeiter tragen Helme auf der Baustelle.', 'Các công nhân đội mũ bảo hộ trên công trường xây dựng.'),
        ('Firma', 'die', 'die', 'die Firmen', 'eine Firma', 'keine Firma', 'công ty, doanh nghiệp', cat2, 'Danh từ giống cái (die Firma). Trả lời Wo? dùng in einer Firma hoặc bei einer IT-Firma.', 'Paula Rausch arbeitet als Programmiererin bei einer IT-Firma.', 'Paula Rausch làm nghề lập trình viên tại một công ty công nghệ thông tin.'),
        ('Krankenhaus', 'das', 'das', 'die Krankenhäuser', 'ein Krankenhaus', 'kein Krankenhaus', 'bệnh viện', cat2, 'Danh từ giống trung (das Krankenhaus). Trả lời Wo? dùng im Krankenhaus (in + dem).', 'Der Arzt untersucht die Patienten im Krankenhaus.', 'Bác sĩ khám cho các bệnh nhân ở trong bệnh viện.'),
        ('Restaurant', 'das', 'das', 'die Restaurants', 'ein Restaurant', 'kein Restaurant', 'nhà hàng', cat2, 'Danh từ giống trung gốc Pháp (das Restaurant). Trả lời Wo? dùng im Restaurant.', 'Die Köchin kocht leckere Spezialitäten im Restaurant.', 'Nữ đầu bếp nấu các món đặc sản ngon miệng ở trong nhà hàng.'),
        ('Blumengeschäft', 'das', 'das', 'die Blumengeschäfte', 'ein Blumengeschäft', 'kein Blumengeschäft', 'cửa hàng hoa tươi', cat2, 'Danh từ ghép giống trung (das Blumengeschäft). Trả lời Wo? dùng im Blumengeschäft.', 'Die Floristin verkauft bunte Rosen im Blumengeschäft.', 'Người nữ bán hoa bán hoa hồng nhiều màu sắc ở trong cửa hàng hoa.'),
        ('Schuhgeschäft', 'das', 'das', 'die Schuhgeschäfte', 'ein Schuhgeschäft', 'kein Schuhgeschäft', 'cửa hàng giày dép', cat2, 'Danh từ ghép giống trung (das Schuhgeschäft). Trả lời Wo? dùng im Schuhgeschäft.', 'Die Verkäuferin verkauft modische Schuhe im Schuhgeschäft.', 'Nữ nhân viên bán hàng bán giày thời trang ở trong cửa hàng giày.'),
        ('Sprachzentrum', 'das', 'das', 'die Sprachzentren', 'ein Sprachzentrum', 'kein Sprachzentrum', 'trung tâm ngoại ngữ', cat2, 'Danh từ giống trung đuôi -um đổi số nhiều sang -en: die Sprachzentren. Dùng im Sprachzentrum.', 'Wir lernen jeden Tag Deutsch im Sprachzentrum.', 'Chúng tôi học tiếng Đức mỗi ngày ở trong trung tâm ngoại ngữ.'),
        ('Bett', 'das', 'das', 'die Betten', 'ein Bett', 'kein Bett', 'chiếc giường ngủ', cat2, 'Danh từ giống trung (das Bett). Hướng di chuyển Wohin? -> ins Bett; Vị trí tĩnh Wo? -> im Bett.', 'Um neunzehn Uhr bringt Frank seine Tochter ins Bett.', 'Lúc 19 giờ Frank đưa con gái của mình lên giường đi ngủ.'),
        ('Fitnessstudio', 'das', 'das', 'die Fitnessstudios', 'ein Fitnessstudio', 'kein Fitnessstudio', 'phòng tập thể hình, gym', cat2, 'Danh từ giống trung (das Fitnessstudio). Trả lời Wo? dùng im Fitnessstudio.', 'Der Trainer trainiert fleißig Sportler im Fitnessstudio.', 'Huấn luyện viên rèn luyện chăm chỉ cho vận động viên ở phòng gym.'),
        ('Stadion', 'das', 'das', 'die Stadien', 'ein Stadion', 'kein Stadion', 'sân vận động', cat2, 'Danh từ giống trung (das Stadion), số nhiều die Stadien. Trả lời Wo? dùng im Stadion.', 'Am Wochenende spielen Fußballer im großen Stadion.', 'Vào cuối tuần các cầu thủ thi đấu ở trong sân vận động lớn.'),
        ('Computer', 'der', 'der', 'die Computer', 'ein Computer', 'kein Computer', 'máy vi tính', cat2, 'Danh từ giống đực (der Computer). Tân ngữ Akkusativ sau brauchen: einen Computer brauchen.', 'Bei ihrer Arbeit braucht Petra May einen schnellen Computer.', 'Trong công việc của mình, Petra May cần một chiếc máy tính nhanh.'),
        ('Patient', 'der', 'der', 'die Patienten', 'ein Patient', 'kein Patient', 'bệnh nhân', cat2, 'Danh từ giống đực N-Deklination (der Patient). Tân ngữ Akkusativ sau untersuchen: den Patienten untersuchen.', 'Der Arzt untersucht den kranken Patienten im Behandlungszimmer.', 'Bác sĩ khám cho bệnh nhân bị ốm ở trong phòng khám bệnh.')
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
    # -------------------------------------------------------------------------
    # NHÓM 1: TRẮC NGHIỆM (18 CÂU: Q1 -> Q18)
    # -------------------------------------------------------------------------
    mcqs = [
        (
            "Câu 1: Chọn phương án đúng hoàn thành câu giới thiệu nghề nghiệp: 'Herr Hoffmann arbeitet seit drei Jahren ___ Mechatroniker in München.'",
            ["wie ein", "als", "von", "für"],
            "als",
            "Khi dùng động từ 'arbeiten' để giới thiệu nghề nghiệp, tiếng Đức dùng cấu trúc 'arbeiten als + [Nghề nghiệp]' không có mạo từ (Herr Hoffmann arbeitet als Mechatroniker).",
            {"accepted_answers": ["als"], "translation": "Ông Hoffmann làm kỹ thuật viên cơ điện tử ở Munich được ba năm rồi."}
        ),
        (
            "Câu 2: Chọn câu đúng ngữ pháp tiếng Đức khi miêu tả nghề nghiệp có tính từ đi kèm:",
            ["Frau Schneider ist sehr fleißige Verkäuferin.", "Frau Schneider ist eine sehr fleißige Verkäuferin.", "Frau Schneider arbeitet als eine Verkäuferin.", "Frau Schneider ist einer fleißige Verkäuferin."],
            "Frau Schneider ist eine sehr fleißige Verkäuferin.",
            "Quy tắc nghề nghiệp: Bình thường nói tên nghề không dùng mạo từ (Sie ist Verkäuferin), nhưng khi có tính từ bổ nghĩa (sehr fleißige) thì BẮT BUỘC phải dùng mạo từ không xác định (eine sehr fleißige Verkäuferin).",
            {"accepted_answers": ["Frau Schneider ist eine sehr fleißige Verkäuferin."], "translation": "Bà Schneider là một nữ nhân viên bán hàng rất chăm chỉ."}
        ),
        (
            "Câu 3: Cặp danh từ nghề nghiệp Nam – Nữ nào dưới đây được viết ĐÚNG CHÍNH TẢ 100%?",
            ["der Hausmann -> die Hausmännerin / der Krankenpfleger -> die Krankenpfleger", "der Koch -> die Köcherin / der Arzt -> die Ärztinn", "der Koch -> die Köchin / der Arzt -> die Ärztin", "der Koch -> die Kochin / der Arzt -> die Arztin"],
            "der Koch -> die Köchin / der Arzt -> die Ärztin",
            "Hai danh từ der Koch và der Arzt khi chuyển sang giống cái (Femininum) vừa thêm hậu tố -in vừa phải thêm dấu Umlaut trên nguyên âm gốc: die Köchin và die Ärztin. Dạng die Kochin / die Arztin thiếu dấu Umlaut nên sai chính tả.",
            {"accepted_answers": ["der Koch -> die Köchin / der Arzt -> die Ärztin"], "translation": "Nam đầu bếp -> Nữ đầu bếp / Nam bác sĩ -> Nữ bác sĩ."}
        ),
        (
            "Câu 4: Chọn phương án đúng hoàn thành câu: 'Ein KFZ-Mechatroniker ___ Autos und arbeitet ___.'",
            ["verkauft / im Schuhgeschäft", "untersucht / im Krankenhaus", "repariert / in einer Werkstatt", "schneidet / im Friseursalon"],
            "repariert / in einer Werkstatt",
            "KFZ-Mechatroniker là kỹ thuật viên cơ điện tử ô tô; công việc là repariert Autos (sửa ô tô) và nơi làm việc (Wo? + Dativ) là in einer Werkstatt (die Werkstatt -> in einer Werkstatt).",
            {"accepted_answers": ["repariert / in einer Werkstatt"], "translation": "Một kỹ thuật viên cơ điện tử ô tô (KFZ-Mechatroniker) sửa chữa xe hơi và làm việc ở trong một xưởng sửa chữa.", "dynamic_profession_quiz": True}
        ),
        (
            "Câu 5: Chọn dạng chia đúng của động từ khuyết thiếu: 'Mein Kollege ist Programmierer von Beruf. Er ___ drei moderne Programmiersprachen fließend sprechen.'",
            ["könnt", "kannst", "kann", "können"],
            "kann",
            "Động từ können diễn tả khả năng/năng lực chuyên môn. Với ngôi er/sie/es, können chia là 'kann' (đổi nguyên âm ö -> a và không thêm đuôi -t).",
            {"accepted_answers": ["kann"], "translation": "Đồng nghiệp của tôi làm nghề lập trình viên. Anh ấy có thể nói trôi chảy ba ngôn ngữ lập trình hiện đại."}
        ),
        (
            "Câu 6: Chọn dạng chia đúng của động từ khuyết thiếu 'müssen': 'Paula Rausch arbeitet als Programmiererin. Jeden Morgen ___ sie schon um 6.15 Uhr aufstehen.'",
            ["müsst", "musst", "muss", "müssen"],
            "muss",
            "Với động từ khuyết thiếu müssen, ngôi ich và ngôi er/sie/es chia giống hệt nhau là muss (đổi ü -> u và không có đuôi -t).",
            {"accepted_answers": ["muss"], "translation": "Paula Rausch làm nghề lập trình viên. Mỗi buổi sáng cô ấy phải thức dậy lúc 6 giờ 15.", "dynamic_modalverb_schedule_quiz": True}
        ),
        (
            "Câu 7: Chọn phương án đúng diễn tả quy định an toàn lao động: 'Auf der Baustelle ___ die Arbeiter ohne Schutzhelm nicht arbeiten.'",
            ["dürft", "darf", "dürfen", "darfst"],
            "dürfen",
            "Chủ ngữ 'die Arbeiter' là danh từ số nhiều (họ - sie). Động từ dürfen chia theo ngôi số nhiều là 'dürfen'. Kết hợp với 'nicht' diễn tả điều cấm đoán tuyệt đối trên công trường.",
            {"accepted_answers": ["dürfen"], "translation": "Trên công trường xây dựng, các công nhân không được phép làm việc khi không đội mũ bảo hộ."}
        ),
        (
            "Câu 8: Chọn dạng chia đúng của 'wollen': 'Nach dem Abitur an der Schule ___ meine Schwester Medizin an der Universität studieren.'",
            ["willst", "wollt", "will", "wollen"],
            "will",
            "Động từ wollen diễn tả nguyện vọng, ý chí quyết tâm. Với chủ ngữ 'meine Schwester' (ngôi sie số ít), wollen đổi nguyên âm o -> i thành 'will' (ngôi ich và er/sie/es đều là will).",
            {"accepted_answers": ["will"], "translation": "Sau khi tốt nghiệp trung học phổ thông, em gái tôi muốn học ngành Y tại trường đại học."}
        ),
        (
            "Câu 9: Chọn dạng chia đúng của 'sollen': 'Der Arzt rät dem Patienten: „Herr Braun, Sie haben hohes Fieber. Sie ___ viel Tee trinken und im Bett bleiben.“'",
            ["sollt", "sollen", "soll", "sollst"],
            "sollen",
            "Động từ sollen dùng để truyền đạt lời khuyên hoặc yêu cầu từ người có thẩm quyền (như bác sĩ). Đi với ngôi lịch sự 'Sie' thì động từ giữ nguyên là 'sollen'.",
            {"accepted_answers": ["sollen"], "translation": "Bác sĩ khuyên bệnh nhân: „Thưa ông Braun, ông bị sốt cao. Ông nên uống nhiều trà và ở trên giường.“"}
        ),
        (
            "Câu 10: Chọn câu có cấu trúc khung câu (Satzklammer) đúng ngữ pháp tiếng Đức:",
            ["Im Restaurant muss der Kellner servieren das Essen schnell.", "Im Restaurant muss der Kellner den Gästen das Essen schnell servieren.", "Im Restaurant der Kellner muss servieren das Essen schnell.", "Im Restaurant muss servieren der Kellner schnell das Essen."],
            "Im Restaurant muss der Kellner den Gästen das Essen schnell servieren.",
            "Quy tắc Satzklammer (khung câu): Động từ khuyết thiếu (muss) đứng ở vị trí số 2, toàn bộ các tân ngữ và trạng từ đứng ở giữa, và động từ nguyên mẫu (servieren) bắt buộc phải đứng ở cuối câu cùng.",
            {"accepted_answers": ["Im Restaurant muss der Kellner den Gästen das Essen schnell servieren."], "translation": "Trong nhà hàng, người phục vụ phải nhanh chóng bưng thức ăn cho thực khách."}
        ),
        (
            "Câu 11: Chọn mạo từ đúng: 'Der Kellner bringt ___ frischen Kaffee an den Tisch.'",
            ["der", "dem", "den", "das"],
            "den",
            "Danh từ 'Kaffee' mang giống đực (der Kaffee). Làm tân ngữ trực tiếp chịu tác động của hành động 'bringen' nên chia ở Cách 4 (Akkusativ): mạo từ der chuyển thành den.",
            {"accepted_answers": ["den"], "translation": "Người phục vụ mang cà phê tươi đến bàn."}
        ),
        (
            "Câu 12: Chọn cặp mạo từ đúng: '1. Die Ärztin untersucht ___ kranken Mann. — 2. Die Krankenschwester hilft ___ kranken Mann.'",
            ["den / dem", "dem / den", "den / den", "dem / dem"],
            "den / dem",
            "Động từ untersuchen đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ: der Mann -> den Mann). Động từ helfen đòi hỏi tân ngữ ở Cách 3 (Dativ: der Mann -> dem Mann).",
            {"accepted_answers": ["den / dem"], "translation": "1. Nữ bác sĩ khám cho người đàn ông bị ốm. — 2. Nữ y tá giúp đỡ người đàn ông bị ốm.", "dynamic_akkdativ_kontrast_quiz": True}
        ),
        (
            "Câu 13: Chọn mạo từ đúng: 'Für seine tägliche Arbeit im Büro kauft der Sekretär ___ neuen Drucker.'",
            ["ein", "einen", "einem", "einer"],
            "einen",
            "Động từ kaufen đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ). Danh từ der Drucker là giống đực, nên mạo từ không xác định ein đổi sang Akkusativ là einen.",
            {"accepted_answers": ["einen"], "translation": "Cho công việc hằng ngày ở văn phòng, nam thư ký mua một chiếc máy in mới."}
        ),
        (
            "Câu 14: Chọn mạo từ phủ định đúng: 'Heute ist Sonntag und der Schüler hat schulfrei. Er braucht ___ Wecker.'",
            ["kein", "keinen", "keinem", "keine"],
            "keinen",
            "Động từ brauchen đi với Cách 4 (Akkusativ). Danh từ der Wecker mang giống đực, do đó mạo từ phủ định kein đổi thành keinen.",
            {"accepted_answers": ["keinen"], "translation": "Hôm nay là Chủ nhật và học sinh được nghỉ học. Cậu ấy không cần đồng hồ báo thức."}
        ),
        (
            "Câu 15: Chọn cặp giới từ đúng: 'Der Trainer kauft neue Bälle ___ sein Team und läuft niemals ___ seine Sportschuhe.'",
            ["für / ohne", "mit / für", "zu / von", "bei / mit"],
            "für / ohne",
            "Hai giới từ 'für' (dành cho) và 'ohne' (không có) thuộc nhóm FUDGE-BO luôn luôn đòi hỏi danh từ đi sau chia ở Cách 4 (Akkusativ): für sein Team, ohne seine Sportschuhe.",
            {"accepted_answers": ["für / ohne"], "translation": "Huấn luyện viên mua những quả bóng mới cho đội của mình và không bao giờ chạy mà không có giày thể thao."}
        ),
        (
            "Câu 16: Chọn dạng mạo từ sở hữu đúng: 'Der Taxifahrer holt ___ Wagen am Morgen aus der Garage.'",
            ["sein", "seinen", "seinem", "seiner"],
            "seinen",
            "Chủ ngữ là der Taxifahrer (ngôi er), gốc sở hữu là sein-. Danh từ der Wagen mang giống đực làm tân ngữ trực tiếp (Akkusativ) cho holt, nên mạo từ sở hữu đổi thành seinen.",
            {"accepted_answers": ["seinen"], "translation": "Người tài xế taxi lấy chiếc xe của mình ra khỏi gara vào buổi sáng."}
        ),
        (
            "Câu 17: Chọn phương án đúng ngữ pháp: 'Der Chef kauft ___ Sekretärin ___ neuen Computer.'",
            ["der / ein", "einer / dem", "die / einen", "der / einen"],
            "der / einen",
            "Trong câu có 2 tân ngữ: Người nhận lợi ích (Wem? cho nữ thư ký) chia ở Cách 3 (Dativ: die -> der Sekretärin); Vật được mua (Was? một chiếc máy tính mới) chia ở Cách 4 (Akkusativ: der -> einen neuen Computer).",
            {"accepted_answers": ["der / einen"], "translation": "Người sếp mua cho nữ thư ký một chiếc máy tính mới."}
        ),
        (
            "Câu 18: Chọn dạng mạo từ sở hữu đúng: 'Liebe Schüler, ihr müsst morgen ___ Lehrer fragen und ___ Hefte mitbringen!'",
            ["euer / eure", "euren / eure", "eurem / euren", "eurer / eure"],
            "euren / eure",
            "Động từ fragen (hỏi ai) và mitbringen (mang theo cái gì) đều đi với Cách 4 (Akkusativ). Chủ ngữ là ihr (các em) -> gốc euer. Trước der Lehrer (giống đực Akkusativ) đổi thành euren Lehrer; trước die Hefte (số nhiều Akkusativ) đổi thành eure Hefte.",
            {"accepted_answers": ["euren / eure"], "translation": "Các em học sinh thân mến, ngày mai các em phải hỏi thầy giáo của các em và mang theo vở của các em nhé!", "dynamic_possessivartikel_akkusativ_quiz": True}
        )
    ]

    for q, opts, corr, exp, extra in mcqs:
        ex_list.append({
            "type": "trac_nghiem",
            "question": q,
            "options": opts,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 15,
            "extra_data": extra
        })

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # NHÓM 2: ĐIỀN KHUYẾT (15 CÂU: Q19 -> Q33)
    # -------------------------------------------------------------------------
    fill_blanks = [
        ("Câu 19: Điền dạng chia đúng của động từ khuyết thiếu 'können' vào chỗ trống: 'Am Samstag haben wir frei. ___ ihr mit uns ins Restaurant kommen?'", ["Könnt", "könnt"], "Könnt", "Chủ ngữ là 'ihr' (các bạn). Động từ können chia cho ngôi ihr là könnt (giữ nguyên âm ö và thêm đuôi -t). Đứng đầu câu hỏi đảo ngữ nên viết hoa Könnt.", "Thứ Bảy chúng tôi được nghỉ. Các bạn có thể đi nhà hàng cùng chúng tôi không?"),
        ("Câu 20: Điền dạng chia đúng của động từ khuyết thiếu 'müssen' vào chỗ trống: 'Wie viele Stunden ___ du pro Tag im Büro arbeiten?'", ["musst"], "musst", "Chủ ngữ là 'du'. Động từ müssen đổi ü -> u và chia đuôi -st thành musst.", "Bạn phải làm việc bao nhiêu tiếng mỗi ngày ở văn phòng?"),
        ("Câu 21: Điền dạng chia đúng của động từ khuyết thiếu 'dürfen' vào chỗ trống: 'Hier ist eine gefährliche Baustelle. ___ Besucher das Gelände betreten?'", ["Dürfen", "dürfen"], "Dürfen", "Chủ ngữ 'Besucher' là danh từ số nhiều (những vị khách). Động từ dürfen giữ nguyên là Dürfen ở đầu câu hỏi.", "Đây là công trường nguy hiểm. Khách tham quan có được phép đi vào khu vực này không?"),
        ("Câu 22: Điền dạng chia đúng của động từ khuyết thiếu 'wollen' vào chỗ trống: 'Nächste Woche ___ wir einen schönen Ausflug mit der Familie machen.'", ["wollen"], "wollen", "Chủ ngữ là 'wir' (chúng tôi). Động từ wollen giữ nguyên dạng nguyên mẫu là wollen.", "Tuần tới chúng tôi muốn có một chuyến dã ngoại tuyệt đẹp cùng gia đình."),
        ("Câu 23: Điền mạo từ xác định thích hợp vào chỗ trống: 'Der Lehrer korrigiert ___ schwierigen Test der Schüler am Schreibtisch.'", ["den"], "den", "Danh từ 'der Test' mang giống đực. Làm tân ngữ trực tiếp cho động từ korrigieren nên đổi thành den.", "Thầy giáo chấm bài kiểm tra khó của học sinh tại bàn làm việc."),
        ("Câu 24: Điền mạo từ không xác định thích hợp vào chỗ trống: 'Im Blumengeschäft bestellt der Kunde ___ bunten Blumenstrauß.'", ["einen"], "einen", "Danh từ 'der Blumenstrauß' mang giống đực, làm tân ngữ trực tiếp cho bestellt nên mạo từ ein đổi thành einen.", "Ở cửa hàng hoa, người khách đặt một bó hoa rực rỡ sắc màu."),
        ("Câu 25: Điền mạo từ phủ định thích hợp vào chỗ trống: 'Heute scheint den ganzen Tag die Sonne, ich brauche ___ Regenschirm.'", ["keinen"], "keinen", "Động từ brauchen đi với Cách 4 (Akkusativ). Danh từ der Regenschirm là giống đực nên kein đổi thành keinen.", "Hôm nay trời nắng cả ngày, tôi không cần chiếc ô nào cả."),
        ("Câu 26: Điền mạo từ sở hữu của ngôi 'ich' (mein-) thích hợp vào chỗ trống: 'Vor der Konferenz rufe ich ___ Kollegen noch einmal an.'", ["meinen"], "meinen", "Động từ anrufen đòi hỏi tân ngữ Akkusativ. Chủ ngữ ich -> gốc mein-. Trước danh từ giống đực der Kollege đổi thành meinen.", "Trước hội nghị, tôi gọi điện cho người đồng nghiệp của mình một lần nữa."),
        ("Câu 27: Điền mạo từ thích hợp vào chỗ trống: 'Die Trainerin lobt ___ besten Sportler nach dem Spiel.'", ["ihren", "den"], "ihren", "Động từ loben (khen ngợi) đi với Cách 4 (Akkusativ). Danh từ der Sportler mang giống đực nên mạo từ sở hữu của cô ấy ihr- đổi thành ihren (hoặc mạo từ xác định den).", "Nữ huấn luyện viên khen ngợi vận động viên xuất sắc nhất của mình sau trận đấu."),
        ("Câu 28: Điền giới từ thích hợp vào chỗ trống: 'Der Koch kauft frische Zutaten ___ das Abendessen.'", ["für", "fuer"], "für", "Giới từ für luôn luôn đòi hỏi danh từ đi sau chia ở Cách 4 (Akkusativ): für das Abendessen (cho bữa tối).", "Người đầu bếp mua các nguyên liệu tươi ngon cho bữa tối."),
        ("Câu 29: Điền giới từ thích hợp vào chỗ trống: 'Der Student kann ___ sein Wörterbuch den Fachtext nicht verstehen.'", ["ohne"], "ohne", "Giới từ ohne mang nghĩa 'không có / thiếu' và luôn đi với Akkusativ (ohne sein Wörterbuch).", "Cậu sinh viên không thể hiểu được bài đọc chuyên ngành nếu thiếu cuốn từ điển."),
        ("Câu 30: Điền từ thích hợp vào chỗ trống: 'Der Kunde parkt den Wagen und geht in ___ Supermarkt.'", ["den", "einen"], "den", "Động từ gehen chỉ sự di chuyển (hướng đi Wohin?) đòi hỏi in + Akkusativ: in den Supermarkt.", "Người khách hàng đỗ xe và đi vào trong siêu thị."),
        ("Câu 31: Điền từ thích hợp vào chỗ trống: 'Nach dem langen Arbeitstag legt sich der Arzt müde ___ Bett.'", ["ins", "in das"], "ins", "Hành động nằm lên giường (di chuyển Wohin? + Akkusativ) với danh từ giống trung das Bett được rút gọn in + das = ins Bett.", "Sau một ngày làm việc dài, vị bác sĩ mệt mỏi ngả lưng lên giường."),
        ("Câu 32: Điền từ thích hợp vào chỗ trống: 'Die Mechatronikerin prüft die Bremsen des Autos in ___ Werkstatt.'", ["der"], "der", "Câu hỏi Wo? (vị trí tĩnh) đòi hỏi Cách 3 (Dativ). Danh từ die Werkstatt mang giống cái nên in + der = in der Werkstatt.", "Nữ thợ cơ khí kiểm tra phanh xe hơi ở trong xưởng sửa chữa."),
        ("Câu 33: Điền mạo từ thích hợp vào chỗ trống: 'Der erfahrene Krankenpfleger hilft ___ jungen Ärztin bei der Operation.'", ["der"], "der", "Động từ helfen luôn luôn đòi hỏi tân ngữ ở Cách 3 (Dativ). Danh từ die Ärztin (giống cái) chuyển mạo từ thành der Ärztin.", "Người nam điều dưỡng giàu kinh nghiệm giúp đỡ nữ bác sĩ trẻ trong ca phẫu thuật.")
    ]

    for q, ans, corr, exp, trans in fill_blanks:
        ex_list.append({
            "type": "dien_khuyet",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ans,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 3: DỊCH TỪ / CỤM TỪ VIỆT -> ĐỨC (12 CÂU: Q34 -> Q45)
    # -------------------------------------------------------------------------
    vd_phrases = [
        ("Câu 34: Dịch sang tiếng Đức (kèm mạo từ): 'nữ lập trình viên'", ["die Programmiererin", "Programmiererin"], "die Programmiererin", "Nam lập trình viên là der Programmierer -> Nữ lập trình viên thêm -in là die Programmiererin."),
        ("Câu 35: Dịch sang tiếng Đức (kèm mạo từ): 'thợ cơ khí ô tô (nam)'", ["der KFZ-Mechatroniker", "der Mechatroniker", "KFZ-Mechatroniker", "Mechatroniker"], "der KFZ-Mechatroniker", "Thợ cơ khí / kỹ thuật viên sửa chữa ô tô là der KFZ-Mechatroniker (hoặc der Mechatroniker)."),
        ("Câu 36: Dịch sang tiếng Đức (kèm mạo từ): 'nữ y tá / điều dưỡng'", ["die Krankenpflegerin", "die Krankenschwester", "Krankenpflegerin", "Krankenschwester"], "die Krankenpflegerin", "Nữ y tá / điều dưỡng trong tiếng Đức là die Krankenpflegerin hoặc die Krankenschwester."),
        ("Câu 37: Dịch sang tiếng Đức (kèm mạo từ): 'người bán hoa (nữ)'", ["die Floristin", "Floristin"], "die Floristin", "Nam bán hoa là der Florist -> Nữ bán hoa là die Floristin."),
        ("Câu 38: Dịch sang tiếng Đức (kèm mạo từ): 'tiệm làm tóc / salon tóc'", ["der Friseursalon", "Friseursalon"], "der Friseursalon", "Tiệm làm tóc là danh từ giống đực der Friseursalon (số nhiều: die Friseursalons)."),
        ("Câu 39: Dịch sang tiếng Đức (kèm mạo từ): 'xưởng sửa chữa'", ["die Werkstatt", "Werkstatt"], "die Werkstatt", "Xưởng sửa chữa là danh từ giống cái die Werkstatt (số nhiều: die Werkstätten)."),
        ("Câu 40: Dịch sang tiếng Đức (kèm mạo từ): 'công trường xây dựng'", ["die Baustelle", "Baustelle"], "die Baustelle", "Công trường xây dựng là danh từ giống cái die Baustelle (số nhiều: die Baustellen)."),
        ("Câu 41: Dịch sang tiếng Đức (kèm mạo từ): 'cửa hàng hoa'", ["das Blumengeschäft", "Blumengeschäft", "das Blumengeschaeft"], "das Blumengeschäft", "Cửa hàng hoa là danh từ ghép giống trung das Blumengeschäft (số nhiều: die Blumengeschäfte)."),
        ("Câu 42: Dịch sang tiếng Đức (kèm mạo từ): 'trung tâm ngoại ngữ'", ["das Sprachzentrum", "Sprachzentrum"], "das Sprachzentrum", "Trung tâm ngoại ngữ là danh từ giống trung das Sprachzentrum (số nhiều: die Sprachzentren)."),
        ("Câu 43: Dịch cụm hoạt động nghề nghiệp sau sang tiếng Đức: 'khám cho các bệnh nhân'", ["Patienten untersuchen", "die Patienten untersuchen", "untersucht Patienten"], "Patienten untersuchen", "Động từ 'khám bệnh' là untersuchen, bệnh nhân số nhiều là die Patienten -> Patienten untersuchen."),
        ("Câu 44: Dịch cụm hoạt động nghề nghiệp sau sang tiếng Đức: 'cắt tóc'", ["Haare schneiden", "die Haare schneiden", "schneidet Haare"], "Haare schneiden", "Danh từ 'tóc' (số nhiều) là die Haare, động từ 'cắt' là schneiden -> Haare schneiden."),
        ("Câu 45: Dịch câu hỏi nghề nghiệp sau sang tiếng Đức (dạng trang trọng 'Sie'): 'Ngài làm nghề gì?'", ["Was sind Sie von Beruf?", "Was machen Sie beruflich?", "Was ist Ihr Beruf?"], "Was sind Sie von Beruf?", "Cả 3 mẫu câu Was sind Sie von Beruf?, Was machen Sie beruflich? và Was ist Ihr Beruf? đều chuẩn xác 100%.")
    ]

    for q, ans, corr, exp in vd_phrases:
        ex_list.append({
            "type": "dich_nghia_vd",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ans,
                "translation": q.split("'")[1] if "'" in q else corr
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 4: DỊCH TỪ / CỤM TỪ ĐỨC -> VIỆT (12 CÂU: Q46 -> Q57)
    # -------------------------------------------------------------------------
    dv_phrases = [
        ("Câu 46: Dịch sang tiếng Việt: 'der Taxifahrer / die Taxifahrerin'", ["tài xế taxi", "người lái xe taxi", "nam tài xế taxi và nữ tài xế taxi", "lái xe taxi"], "tài xế taxi", "der Taxifahrer (nam) và die Taxifahrerin (nữ) có nghĩa là tài xế taxi."),
        ("Câu 47: Dịch sang tiếng Việt: 'der Hausmann / die Hausfrau'", ["người nội trợ", "nam nội trợ và nữ nội trợ", "đàn ông nội trợ và phụ nữ nội trợ", "nội trợ"], "người nội trợ", "der Hausmann (nam nội trợ) và die Hausfrau (nữ nội trợ)."),
        ("Câu 48: Dịch sang tiếng Việt: 'der Kellner / die Kellnerin'", ["nhân viên phục vụ bàn", "bồi bàn", "người phục vụ nhà hàng", "nam bồi bàn và nữ bồi bàn"], "nhân viên phục vụ bàn", "der Kellner / die Kellnerin là nhân viên phục vụ bàn (bồi bàn) trong nhà hàng hoặc quán cà phê."),
        ("Câu 49: Dịch sang tiếng Việt: 'der Sekretär / die Sekretärin'", ["thư ký", "nam thư ký và nữ thư ký", "người thư ký"], "thư ký", "der Sekretär / die Sekretärin có nghĩa là thư ký văn phòng."),
        ("Câu 50: Dịch sang tiếng Việt: 'Schüler an einer Schule unterrichten'", ["dạy học sinh ở một trường học", "giảng dạy học sinh tại một ngôi trường", "dạy học sinh tại một trường học"], "dạy học sinh ở một trường học", "unterrichten = giảng dạy; Schüler = học sinh; an einer Schule = tại một ngôi trường."),
        ("Câu 51: Dịch sang tiếng Việt: 'Computerprogramme schreiben'", ["viết chương trình máy tính", "viết các chương trình máy tính", "lập trình phần mềm máy tính"], "viết chương trình máy tính", "die Computerprogramme = các chương trình máy tính; schreiben = viết."),
        ("Câu 52: Dịch sang tiếng Việt: 'die Tochter vom Kindergarten abholen'", ["đón con gái từ trường mẫu giáo", "đón con gái từ nhà trẻ về", "đón cô con gái ở trường mầm non"], "đón con gái từ trường mẫu giáo", "abholen = đón; vom Kindergarten = từ trường mẫu giáo / nhà trẻ."),
        ("Câu 53: Dịch sang tiếng Việt: 'das Auto in die Werkstatt bringen'", ["mang ô tô vào xưởng sửa chữa", "đưa xe hơi đến xưởng sửa chữa", "đem ô tô vào xưởng"], "mang ô tô vào xưởng sửa chữa", "in die Werkstatt bringen (Wohin? + Akkusativ) = mang/đưa vào xưởng sửa chữa."),
        ("Câu 54: Dịch sang tiếng Việt: 'zum Fußballtraining gehen'", ["đi đến buổi tập bóng đá", "đi tập đá bóng", "đi tới buổi huấn luyện bóng đá"], "đi đến buổi tập bóng đá", "das Fußballtraining = buổi tập luyện bóng đá; zum Fußballtraining gehen = đi tập bóng đá."),
        ("Câu 55: Dịch sang tiếng Việt: 'Kunden im Büro anrufen'", ["gọi điện cho khách hàng ở trong văn phòng", "gọi điện thoại cho khách hàng tại văn phòng", "gọi cho khách hàng ở văn phòng"], "gọi điện cho khách hàng ở trong văn phòng", "die Kunden = khách hàng; anrufen = gọi điện thoại; im Büro = ở trong văn phòng."),
        ("Câu 56: Dịch sang tiếng Việt: 'müssen — können — möchten'", ["phải - có thể - muốn", "phải, có thể, muốn", "bắt buộc phải - có thể - muốn"], "phải - có thể - muốn", "Ba động từ khuyết thiếu trọng tâm: müssen (phải), können (có thể), möchten (muốn)."),
        ("Câu 57: Dịch sang tiếng Việt: 'im Schuhgeschäft Schuhe verkaufen'", ["bán giày ở trong cửa hàng giày", "bán giày dép tại tiệm giày", "bán giày trong tiệm giày"], "bán giày ở trong cửa hàng giày", "im Schuhgeschäft = ở trong cửa hàng giày dép; Schuhe verkaufen = bán giày.")
    ]

    for q, ans, corr, exp in dv_phrases:
        ex_list.append({
            "type": "dich_nghia_dv",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 15,
            "extra_data": {
                "accepted_answers": ans,
                "translation": corr
            }
        })

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (10 BÀI: Q58 -> Q67, mỗi bài 4 cặp)
    # -------------------------------------------------------------------------
    noi_o_data = [
        (
            "Câu 58: Nối Nghề nghiệp (Cột Trái) với Nhiệm vụ chuyên môn đặc trưng (Cột Phải):",
            [
                {"left": "Florist / Floristin", "right": "bindet Blumensträuße und verkauft Rosen im Blumengeschäft"},
                {"left": "KFZ-Mechatroniker / Mechatronikerin", "right": "repariert defekte Motoren und prüft Bremsen in der Werkstatt"},
                {"left": "Kellner / Kellnerin", "right": "serviert Getränke und bringt Speisen an den Tisch"},
                {"left": "Bauarbeiter / Bauarbeiterin", "right": "baut moderne Gebäude und trägt Schutzhelm auf der Baustelle"}
            ],
            "Nối nghề nghiệp với nhiệm vụ và nơi làm việc đặc trưng: 1. Florist/in (thợ hoa) làm việc tại Blumengeschäft, nhiệm vụ là cắm hoa (bindet Blumensträuße) và bán hoa (verkauft Rosen). 2. KFZ-Mechatroniker/in (kỹ thuật viên cơ điện tử ô tô) làm việc trong Werkstatt, nhiệm vụ là sửa động cơ (repariert Motoren) và kiểm tra phanh (prüft Bremsen). 3. Kellner/in (nhân viên phục vụ bàn) làm việc tại quán ăn/nhà hàng, nhiệm vụ là bưng đồ uống (serviert Getränke) và mang món ăn ra bàn (bringt Speisen an den Tisch). 4. Bauarbeiter/in (công nhân xây dựng) làm việc tại Baustelle, nhiệm vụ là xây nhà (baut Gebäude) và phải đội mũ bảo hộ lao động (trägt Schutzhelm).",
            "1. Thợ hoa: cắm/bó hoa và bán hoa hồng trong cửa hàng hoa. | 2. Kỹ thuật viên cơ điện tử ô tô: sửa chữa động cơ hỏng và kiểm tra phanh trong xưởng sửa chữa. | 3. Nhân viên phục vụ bàn: bưng đồ uống và mang món ăn đến bàn cho khách. | 4. Công nhân xây dựng: xây các tòa nhà hiện đại và đội mũ bảo hộ trên công trường."
        ),
        (
            "Câu 59: Nối Nghề nghiệp (Cột Trái) với Nơi làm việc chuẩn ngữ pháp (Cột Phải):",
            [
                {"left": "die Verkäuferin", "right": "im Supermarkt oder im Schuhgeschäft"},
                {"left": "der Koch", "right": "in der Restaurantküche am Herd"},
                {"left": "die Schülerin und der Lehrer", "right": "im Klassenzimmer am Gymnasium"},
                {"left": "die Trainerin und der Sportler", "right": "im großen Fußballstadion"}
            ],
            "Vị trí nơi làm việc (câu hỏi Wo? - Ở đâu?) đi với giới từ in + Cách 3 (Dativ): 1. die Verkäuferin bán hàng ở siêu thị/tiệm giày: der Supermarkt / das Schuhgeschäft là giống đực/trung nên in + dem rút gọn thành 'im Supermarkt / im Schuhgeschäft'. 2. der Koch nấu nướng trong bếp: die Restaurantküche là danh từ giống cái nên in + der chuyển thành 'in der Restaurantküche'. 3. die Schülerin & der Lehrer dạy và học ở trường: das Klassenzimmer là giống trung nên in + dem rút gọn thành 'im Klassenzimmer'. 4. die Trainerin & der Sportler tập luyện ở sân vận động: das Fußballstadion là giống trung nên in + dem rút gọn thành 'im großen Fußballstadion'.",
            "1. Nữ nhân viên bán hàng: ở trong siêu thị hoặc trong cửa hàng giày. | 2. Nam đầu bếp: ở trong gian bếp nhà hàng bên cạnh bếp nấu. | 3. Nữ học sinh và nam thầy giáo: ở trong phòng học tại trường trung học. | 4. Nữ huấn luyện viên và nam vận động viên: ở trong sân vận động bóng đá lớn."
        ),
        (
            "Câu 60: Nối Cụm động từ cố định (Cột Trái) với Thành phần đi kèm phù hợp ngữ pháp (Cột Phải):",
            [
                {"left": "arbeiten als", "right": "Mechatroniker bei einer Autofirma"},
                {"left": "telefonieren mit", "right": "dem Kunden im Büro"},
                {"left": "danken für", "right": "die große Hilfe der Kollegen"},
                {"left": "helfen bei", "right": "der schweren Arbeit am Computer"}
            ],
            "Quy tắc ngữ pháp của các cụm động từ đi kèm giới từ cố định: 1. 'arbeiten als' đi trực tiếp với tên nghề nghiệp mà không dùng mạo từ (không dùng ein/der): arbeiten als Mechatroniker. 2. 'telefonieren mit' luôn đòi hỏi Cách 3 (Dativ): danh từ giống đực der Kunde đổi thành 'mit dem Kunden'. 3. 'danken für' luôn đòi hỏi Cách 4 (Akkusativ): danh từ giống cái die Hilfe giữ nguyên mạo từ 'für die große Hilfe'. 4. 'helfen bei' luôn đòi hỏi Cách 3 (Dativ): danh từ giống cái die Arbeit đổi mạo từ thành 'bei der schweren Arbeit'.",
            "1. làm việc với tư cách là kỹ thuật viên cơ điện tử tại một công ty ô tô | 2. gọi điện thoại với khách hàng ở văn phòng | 3. cảm ơn vì sự giúp đỡ to lớn của các đồng nghiệp | 4. giúp đỡ trong công việc nặng nhọc bên máy vi tính."
        ),
        (
            "Câu 61: Nối Động từ khuyết thiếu (Cột Trái) với Tình huống thực tế sử dụng (Cột Phải):",
            [
                {"left": "müssen", "right": "Die Ampel ist rot, alle Autos stoppen hier."},
                {"left": "können", "right": "Er spricht fließend vier Fremdsprachen."},
                {"left": "nicht dürfen", "right": "Hier ist eine Baustelle, Betreten verboten!"},
                {"left": "wollen", "right": "Wir haben einen festen Plan für die Zukunft."}
            ],
            "Bản chất và ngữ cảnh sử dụng của 4 động từ khuyết thiếu: 1. 'müssen' diễn tả sự bắt buộc khách quan, luật lệ hoặc quy định bắt buộc phải tuân theo (đèn đỏ thì xe cộ bắt buộc phải dừng). 2. 'können' diễn tả năng lực, khả năng chuyên môn hoặc kỹ năng cá nhân (khả năng nói được 4 ngoại ngữ). 3. 'nicht dürfen' diễn tả sự cấm đoán tuyệt đối, liên quan đến an toàn lao động hoặc biển báo cấm (cấm người ngoài vào công trường nguy hiểm). 4. 'wollen' diễn tả ý chí quyết tâm mạnh mẽ, mong muốn chủ quan hoặc kế hoạch đã định sẵn cho tương lai.",
            "1. müssen: Đèn giao thông màu đỏ, tất cả ô tô phải dừng lại ở đây. | 2. können: Anh ấy có thể nói trôi chảy bốn thứ tiếng ngoại ngữ. | 3. nicht dürfen: Đây là công trường xây dựng, cấm vào (không được phép vào)! | 4. wollen: Chúng tôi có một kế hoạch kiên định cho tương lai (muốn / quyết tâm thực hiện)."
        ),
        (
            "Câu 62: Nối Chủ ngữ (Cột Trái) với Dạng chia đúng của Modalverb wollen & dürfen (Cột Phải):",
            [
                {"left": "ich / er / sie / es", "right": "will / darf"},
                {"left": "du", "right": "willst / darfst"},
                {"left": "ihr", "right": "wollt / dürft"},
                {"left": "wir / sie / Sie", "right": "wollen / dürfen"}
            ],
            "Quy tắc chia động từ khuyết thiếu wollen (muốn) và dürfen (được phép): 1. Ngôi 'ich' và ngôi số ít 'er/sie/es' luôn chia giống hệt nhau, đổi nguyên âm (o -> i, ü -> a) và hoàn toàn KHÔNG có đuôi động từ (-t): ich/er/sie/es will, darf. 2. Ngôi 'du' đổi nguyên âm và thêm đuôi -st theo quy tắc chia: du willst, darfst. 3. Ngôi 'ihr' giữ nguyên âm gốc của động từ (o, ü) và thêm đuôi -t: ihr wollt, dürft. 4. Ngôi số nhiều 'wir', 'sie' (họ) và ngôi lịch sự 'Sie' giữ nguyên dạng nguyên mẫu tận cùng đuôi -en: wir/sie/Sie wollen, dürfen.",
            "1. ich / er / sie / es: tôi / anh ấy / cô ấy / nó muốn / được phép | 2. du: bạn muốn / được phép | 3. ihr: các bạn muốn / được phép | 4. wir / sie / Sie: chúng tôi / họ / Ngài muốn / được phép."
        ),
        (
            "Câu 63: Nối Câu hỏi phỏng vấn công việc (Cột Trái) với Câu trả lời phù hợp ngữ cảnh (Cột Phải):",
            [
                {"left": "Was machen Sie beruflich, Herr Bauer?", "right": "Ich arbeite als Mechatroniker bei einer Autofirma."},
                {"left": "Wo arbeiten Sie jeden Tag?", "right": "In einer modernen Werkstatt am Stadtrand."},
                {"left": "Welche Aufgaben müssen Sie übernehmen?", "right": "Ich muss Fahrzeuge warten und Fehler diagnostizieren."},
                {"left": "Wie gefällt Ihnen die Arbeit?", "right": "Sehr gut, ich kann viele neue Technologien lernen."}
            ],
            "Đối chiếu ngữ cảnh câu hỏi và câu trả lời trong phỏng vấn nghề nghiệp: 1. 'Was machen Sie beruflich?' (hỏi nghề nghiệp) -> trả lời bằng cấu trúc chức danh nghề 'Ich arbeite als Mechatroniker...'. 2. 'Wo arbeiten Sie...?' (hỏi địa điểm làm việc) -> trả lời bằng cụm chỉ nơi chốn 'In einer modernen Werkstatt...'. 3. 'Welche Aufgaben müssen Sie übernehmen?' (hỏi nhiệm vụ công việc) -> trả lời bằng các hành động chuyên môn 'Ich muss Fahrzeuge warten und Fehler diagnostizieren'. 4. 'Wie gefällt Ihnen die Arbeit?' (hỏi cảm nhận/mức độ yêu thích) -> trả lời bằng đánh giá tích cực 'Sehr gut, ich kann viele neue Technologien lernen'.",
            "1. 'Thưa ông Bauer, ông làm nghề gì?' — 'Tôi làm kỹ thuật viên cơ điện tử tại một công ty ô tô.' | 2. 'Hằng ngày ông làm việc ở đâu?' — 'Trong một xưởng sửa chữa hiện đại ở ngoại ô thành phố.' | 3. 'Ông phải đảm nhận những nhiệm vụ nào?' — 'Tôi phải bảo dưỡng xe cộ và chẩn đoán lỗi hỏng.' | 4. 'Ông thấy công việc này thế nào?' — 'Rất tốt, tôi có thể học hỏi nhiều công nghệ mới.'"
        ),
        (
            "Câu 64: Nối Động từ (Cột Trái) với Cụm danh từ tân ngữ phù hợp ngữ pháp (Cột Phải):",
            [
                {"left": "untersuchen", "right": "den kranken Patienten im Behandlungszimmer"},
                {"left": "helfen", "right": "der älteren Dame beim Überqueren der Straße"},
                {"left": "anrufen", "right": "meinen besten Kollegen im Büro"},
                {"left": "gehören", "right": "dem neuen Trainer der Fußballmannschaft"}
            ],
            "Quy tắc đòi hỏi Cách (Kasus) của từng động từ: 1. 'untersuchen' (khám bệnh) đòi hỏi tân ngữ trực tiếp ở Cách 4 (Akkusativ): danh từ giống đực der Patient (danh từ N-Deklination) đổi thành 'den kranken Patienten'. 2. 'helfen' (giúp đỡ) luôn đòi hỏi tân ngữ ở Cách 3 (Dativ): danh từ giống cái die Dame đổi mạo từ thành 'der älteren Dame'. 3. 'anrufen' (gọi điện cho ai) đòi hỏi tân ngữ ở Cách 4 (Akkusativ): danh từ giống đực der Kollege (mein-) đổi thành 'meinen besten Kollegen'. 4. 'gehören' (thuộc về ai) luôn đòi hỏi tân ngữ ở Cách 3 (Dativ): danh từ giống đực der Trainer đổi mạo từ thành 'dem neuen Trainer'.",
            "1. untersuchen: khám cho bệnh nhân bị ốm ở trong phòng khám bệnh | 2. helfen: giúp đỡ bà cụ lớn tuổi khi băng qua đường | 3. anrufen: gọi điện thoại cho người đồng nghiệp thân nhất của tôi ở văn phòng | 4. gehören: thuộc về vị huấn luyện viên mới của đội bóng đá."
        ),
        (
            "Câu 65: Nối Câu hỏi về Địa điểm (Cột Trái) với Câu trả lời chuẩn ngữ pháp (Cột Phải):",
            [
                {"left": "Wohin fährt der Taxifahrer den Touristen?", "right": "Direkt an den Flughafen."},
                {"left": "Wo untersucht die Ärztin den Patienten?", "right": "Im Behandlungszimmer."},
                {"left": "Wohin geht die Lehrerin nach der Pause?", "right": "Zurück in das Klassenzimmer."},
                {"left": "Wo kocht der Koch das Mittagessen?", "right": "In der modernen Restaurantküche."}
            ],
            "Phân biệt câu hỏi hướng di chuyển (Wohin? + Akkusativ) và vị trí tại chỗ (Wo? + Dativ): 1. 'Wohin fährt der Taxifahrer...?' hỏi hướng di chuyển đến sân bay, đòi hỏi giới từ an + Akkusativ: danh từ giống đực der Flughafen đổi thành 'an den Flughafen'. 2. 'Wo untersucht die Ärztin...?' hỏi vị trí khám bệnh tại chỗ, đòi hỏi giới từ in + Dativ: danh từ giống trung das Behandlungszimmer đổi in + dem thành 'im Behandlungszimmer'. 3. 'Wohin geht die Lehrerin...?' hỏi hướng đi vào phòng học, đòi hỏi giới từ in + Akkusativ: danh từ giống trung das Klassenzimmer giữ nguyên 'in das Klassenzimmer'. 4. 'Wo kocht der Koch...?' hỏi vị trí nấu ăn tại chỗ, đòi hỏi giới từ in + Dativ: danh từ giống cái die Restaurantküche đổi in + der thành 'in der modernen Restaurantküche'.",
            "1. 'Tài xế taxi chở du khách đi đâu?' — 'Đi thẳng đến sân bay.' | 2. 'Nữ bác sĩ khám bệnh nhân ở đâu?' — 'Ở trong phòng khám bệnh.' | 3. 'Cô giáo đi đâu sau giờ giải lao?' — 'Quay trở lại trong phòng học.' | 4. 'Đầu bếp nấu bữa trưa ở đâu?' — 'Ở trong gian bếp nhà hàng hiện đại.'"
        ),
        (
            "Câu 66: Nối Hoạt động công việc (Cột Trái) với Dụng cụ cần thiết tương ứng (Cột Phải):",
            [
                {"left": "Der Mechatroniker muss Schrauben am Motor festziehen,", "right": "deshalb sucht er einen passenden Schraubenschlüssel."},
                {"left": "Die Ärztin muss die Körpertemperatur messen,", "right": "deshalb braucht sie ein genaues Fieberthermometer."},
                {"left": "Die Sekretärin muss den ganzen Tag E-Mails tippen,", "right": "deshalb kauft sie eine moderne Computertastatur."},
                {"left": "Der Lehrer bereitet den Unterricht für morgen vor,", "right": "deshalb sammelt er alle wichtigen Lehrbücher."}
            ],
            "Sự biến đổi của mạo từ theo 3 giống và số nhiều khi làm tân ngữ trực tiếp (Cách 4 - Akkusativ): 1. Giống đực (Maskulinum - der Schraubenschlüssel): Biến đổi mạo từ sang đuôi -en khi làm tân ngữ cho động từ suchen: 'einen passenden Schraubenschlüssel'. 2. Giống trung (Neutrum - das Fieberthermometer): Giữ nguyên mạo từ giống như Nominativ khi làm tân ngữ cho brauchen: 'ein genaues Fieberthermometer'. 3. Giống cái (Femininum - die Computertastatur): Giữ nguyên mạo từ đuôi -e khi làm tân ngữ cho kaufen: 'eine moderne Computertastatur'. 4. Số nhiều (Plural - die Lehrbücher): Giữ nguyên mạo từ số nhiều khi làm tân ngữ cho sammeln: 'alle wichtigen Lehrbücher'. Cả 4 câu đều gắn liền với hoạt động và dụng cụ chuyên môn của từng ngành nghề.",
            "1. Kỹ thuật viên cơ điện tử phải siết chặt ốc vít ở động cơ, vì vậy anh ấy tìm một chiếc cờ lê phù hợp. | 2. Nữ bác sĩ phải đo thân nhiệt, vì vậy cô ấy cần một chiếc nhiệt kế chính xác. | 3. Nữ thư ký phải gõ email cả ngày, vì vậy cô ấy mua một chiếc bàn phím máy tính hiện đại. | 4. Thầy giáo chuẩn bị bài giảng cho ngày mai, vì vậy thầy thu thập tất cả các sách giáo khoa quan trọng."
        ),
        (
            "Câu 67: Nối Tình huống ở vế đầu (Cột Trái) với Hoạt động dùng động từ khuyết thiếu phù hợp (Cột Phải):",
            [
                {"left": "Ich arbeite heute im Spätdienst,", "right": "deshalb kann ich am Morgen bis 9.00 Uhr schlafen."},
                {"left": "Mein Sohn ist heute leider krank,", "right": "deshalb darf er heute nicht in die Schule gehen."},
                {"left": "Habt ihr morgen frei,", "right": "oder müsst ihr um 8.00 Uhr in der Firma sein?"},
                {"left": "Frau Klein arbeitet als Sekretärin im Büro,", "right": "und sie kann sehr schnell E-Mails schreiben."}
            ],
            "Ghép nối dựa trên sự hòa hợp chủ ngữ và ngữ nghĩa của Modalverb: 1. Chủ ngữ 'Ich' tương ứng với cách chia 'kann ich' (làm ca muộn nên buổi sáng có thể ngủ dậy muộn). 2. Chủ ngữ 'Mein Sohn' (ngôi er) bị ốm tương ứng với sự cấm đoán 'darf er nicht' (bị ốm nên không được phép đến trường để tránh lây bệnh). 3. Câu hỏi với chủ ngữ 'ihr' đi liền với vế 'oder müsst ihr' (hỏi các bạn được nghỉ hay phải có mặt ở công ty lúc 8 giờ). 4. Chủ ngữ 'Frau Klein' (ngôi sie) làm thư ký tương ứng với năng lực chuyên môn 'sie kann sehr schnell E-Mails schreiben'.",
            "1. Hôm nay tôi làm ca muộn, vì vậy buổi sáng tôi có thể ngủ đến 9 giờ. | 2. Hôm nay con trai tôi không may bị ốm, vì vậy cháu không được phép đến trường. | 3. Ngày mai các bạn được nghỉ, hay các bạn phải có mặt ở công ty lúc 8 giờ? | 4. Bà Klein làm thư ký ở văn phòng, và bà ấy có thể gõ email rất nhanh."
        )
    ]

    for item in noi_o_data:
        if len(item) == 4:
            q, pairs, exp, trans = item
        else:
            q, pairs, exp = item
            trans = "Nối các cặp tương ứng giữa 2 cột."
        ex_list.append({
            "type": "noi_o",
            "question": q,
            "options": None,
            "correct_answer": "Hoàn thành nối ô",
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "noi_o_pairs": pairs,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # NHÓM 6: ĐIỀN TẠO CÂU (10 CÂU: Q68 -> Q77, điền 2 từ ngăn cách bởi dấu /)
    # -------------------------------------------------------------------------
    dien_tao_cau_data = [
        ("Câu 68: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Nachts [1] die Taxifahrer sehr vorsichtig [2].' (Gợi ý: 'Ban đêm các tài xế taxi phải lái xe rất cẩn thận.')", ["müssen / fahren", "müssen/fahren", "muessen / fahren", "muessen/fahren"], "müssen / fahren", "Nachts [1] die Taxifahrer sehr vorsichtig [2].", "Động từ khuyết thiếu müssen chia cho danh từ số nhiều die Taxifahrer là müssen ở vị trí số 2; động từ fahren ở dạng nguyên mẫu đứng cuối câu.", "Ban đêm các tài xế taxi phải lái xe rất cẩn thận."),
        ("Câu 69: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Kellner [1] das Essen nhanh an den Tisch [2].' (Gợi ý: 'Người bồi bàn có thể mang thức ăn nhanh đến bàn.')", ["kann / bringen", "kann/bringen"], "kann / bringen", "Der Kellner [1] das Essen schnell an den Tisch [2].", "Động từ können chia cho ngôi thứ ba số ít der Kellner là kann ở vị trí số 2; động từ bringen giữ nguyên mẫu ở cuối câu.", "Người bồi bàn có thể mang thức ăn nhanh đến bàn."),
        ("Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'In der Universitätsbibliothek [1] man nicht laut [2].' (Gợi ý: 'Trong thư viện trường đại học người ta không được phép nói to.')", ["darf / sprechen", "darf/sprechen"], "darf / sprechen", "In der Universitätsbibliothek [1] man nicht laut [2].", "Đại từ bất định man đi với dạng chia ngôi thứ 3 số ít: dürfen đổi thành darf; động từ sprechen nguyên mẫu đứng cuối câu.", "Trong thư viện trường đại học người ta không được phép nói to."),
        ("Câu 71: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Trainer [1] morgen ein wichtiges Fußballtraining [2].' (Gợi ý: 'Ngày mai huấn luyện viên muốn dẫn dắt một buổi tập bóng đá quan trọng.')", ["will / leiten", "will/leiten", "will / machen", "will/machen", "will / organisieren", "will/organisieren"], "will / leiten", "Der Trainer [1] morgen ein wichtiges Fußballtraining [2].", "Động từ wollen chia cho der Trainer (er) là will ở vị trí số 2; động từ nguyên mẫu leiten (hoặc organisieren/machen) đứng ở cuối câu.", "Ngày mai huấn luyện viên muốn dẫn dắt một buổi tập bóng đá quan trọng."),
        ("Câu 72: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Patient mit Fieber [1] täglich viel Wasser [2].' (Gợi ý: 'Người bệnh nhân bị sốt nên uống nhiều nước mỗi ngày.')", ["soll / trinken", "soll/trinken"], "soll / trinken", "Der Patient mit Fieber [1] täglich viel Wasser [2].", "Động từ sollen truyền đạt lời khuyên y tế, chia cho der Patient (er) là soll; động từ nguyên mẫu trinken đứng ở cuối câu.", "Người bệnh nhân bị sốt nên uống nhiều nước mỗi ngày."),
        ("Câu 73: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Heute Nachmittag [1] der Hausmann frische Lebensmittel [2].' (Gợi ý: 'Chiều nay người đàn ông nội trợ muốn mua thực phẩm tươi.')", ["möchte / einkaufen", "möchte/einkaufen", "moechte / einkaufen", "moechte/einkaufen", "möchte / kaufen", "möchte/kaufen"], "möchte / einkaufen", "Heute Nachmittag [1] der Hausmann frische Lebensmittel [2].", "Động từ möchten chia cho ngôi er (der Hausmann) là möchte; động từ tách einkaufen giữ nguyên mẫu viết liền ở cuối câu.", "Chiều nay người đàn ông nội trợ muốn mua thực phẩm tươi."),
        ("Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Die Floristin [1] wunderschöne Blumen an die Kunden [2].' (Gợi ý: 'Nữ thợ hoa phải giao những bông hoa tuyệt đẹp cho khách hàng.')", ["muss / liefern", "muss/liefern", "muss / verkaufen", "muss/verkaufen"], "muss / liefern", "Die Floristin [1] wunderschöne Blumen an die Kunden [2].", "Động từ müssen chia cho die Floristin (sie) là muss; động từ liefern (hoặc verkaufen) giữ nguyên mẫu ở cuối câu.", "Nữ thợ hoa phải giao những bông hoa tuyệt đẹp cho khách hàng."),
        ("Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Im Sprachzentrum [1] die Schüler fleißig Deutsch [2].' (Gợi ý: 'Ở trung tâm ngôn ngữ các học viên có thể học tiếng Đức chăm chỉ.')", ["können / lernen", "können/lernen", "koennen / lernen", "koennen/lernen"], "können / lernen", "Im Sprachzentrum [1] die Schüler fleißig Deutsch [2].", "Chủ ngữ die Schüler là số nhiều nên können giữ nguyên; động từ lernen đứng ở cuối câu.", "Ở trung tâm ngôn ngữ các học viên có thể học tiếng Đức chăm chỉ."),
        ("Câu 76: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Die Programmiererin [1] einen neuen Laptop für ihre Arbeit [2].' (Gợi ý: 'Nữ lập trình viên muốn mua một chiếc máy tính xách tay mới cho công việc.')", ["will / kaufen", "will/kaufen", "möchte / kaufen", "möchte/kaufen"], "will / kaufen", "Die Programmiererin [1] einen neuen Laptop für ihre Arbeit [2].", "Động từ wollen chia cho ngôi sie là will ở vị trí số 2; động từ kaufen đứng ở cuối câu.", "Nữ lập trình viên muốn mua một chiếc máy tính xách tay mới cho công việc."),
        ("Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Nach der langen Nachtschicht [1] der Krankenpfleger ruhig [2].' (Gợi ý: 'Sau ca trực đêm dài người nam điều dưỡng được phép ngủ yên tĩnh.')", ["darf / schlafen", "darf/schlafen", "kann / schlafen", "kann/schlafen"], "darf / schlafen", "Nach der langen Nachtschicht [1] der Krankenpfleger ruhig [2].", "Động từ dürfen chia cho der Krankenpfleger là darf ở vị trí 2; động từ schlafen giữ nguyên mẫu ở cuối câu.", "Sau ca trực đêm dài người nam điều dưỡng được phép ngủ yên tĩnh.")
    ]

    for q, ans, corr, dframe, exp, trans in dien_tao_cau_data:
        ex_list.append({
            "type": "dien_tao_cau",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "accepted_answers": ans,
                "display_frame": dframe,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # NHÓM 7: NGHE ĐIỀN (9 CÂU: Q78 -> Q86)
    # -------------------------------------------------------------------------
    nghe_dien_data = [
        (
            "Der Koch bereitet köstliche Gerichte in der Küche zu.",
            "Câu 78: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Koch bereitet köstliche Gerichte in der ___ zu.'",
            ["Küche", "Kueche", "küche", "kueche"],
            "Küche",
            "Người đầu bếp chuẩn bị các món ăn ngon trong nhà bếp.",
            "Danh từ chỉ nơi làm việc của đầu bếp là die Küche (in der Küche = trong nhà bếp)."
        ),
        (
            "Die Studentin besucht am Nachmittag eine Vorlesung an der Universität.",
            "Câu 79: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Studentin besucht am Nachmittag eine Vorlesung an der ___.'",
            ["Universität", "Universitaet", "universität", "universitaet", "Uni", "uni"],
            "Universität",
            "Nữ sinh viên tham dự một buổi giảng tại trường đại học vào buổi chiều.",
            "Nơi học tập của sinh viên đại học là die Universität (an der Universität = tại trường đại học)."
        ),
        (
            "Der Verkäufer berät die Kunden freundlich im Schuhgeschäft.",
            "Câu 80: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Verkäufer berät die Kunden freundlich im ___.'",
            ["Schuhgeschäft", "Schuhgeschaeft", "schuhgeschäft", "schuhgeschaeft"],
            "Schuhgeschäft",
            "Người bán hàng tư vấn khách hàng thân thiện ở trong cửa hàng giày.",
            "Cửa hàng bán giày dép là das Schuhgeschäft (im Schuhgeschäft)."
        ),
        (
            "Die Friseurin macht eine sehr schöne moderne Frisur im Friseursalon.",
            "Câu 81: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Friseurin macht eine sehr schöne moderne Frisur im ___.'",
            ["Friseursalon", "friseursalon"],
            "Friseursalon",
            "Nữ thợ làm tóc làm một kiểu tóc hiện đại rất đẹp trong tiệm làm tóc.",
            "Tiệm làm tóc là der Friseursalon (im Friseursalon)."
        ),
        (
            "Auf der Baustelle müssen alle Arbeiter einen Schutzhelm tragen.",
            "Câu 82: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Auf der ___ müssen alle Arbeiter einen Schutzhelm tragen.'",
            ["Baustelle", "baustelle"],
            "Baustelle",
            "Trên công trường tất cả công nhân phải đội mũ bảo hộ.",
            "Công trường xây dựng là die Baustelle (auf der Baustelle)."
        ),
        (
            "Der Trainer leitet das Training für die Mannschaft im Stadion.",
            "Câu 83: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Trainer leitet das Training für die Mannschaft im ___.'",
            ["Stadion", "stadion"],
            "Stadion",
            "Huấn luyện viên điều hành buổi tập cho đội bóng ở sân vận động.",
            "Sân vận động thể thao là das Stadion (im Stadion)."
        ),
        (
            "Der Sekretär schreibt wichtige E-Mails an seinem Computer.",
            "Câu 84: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Sekretär schreibt wichtige E-Mails an seinem ___.'",
            ["Computer", "computer"],
            "Computer",
            "Nam thư ký viết những email quan trọng trên máy tính của mình.",
            "Thiết bị văn phòng để gõ email là der Computer (am Computer / an seinem Computer)."
        ),
        (
            "Viele Ausländer lernen gemeinsam Deutsch im Sprachzentrum.",
            "Câu 85: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Viele Ausländer lernen gemeinsam Deutsch im ___.'",
            ["Sprachzentrum", "sprachzentrum"],
            "Sprachzentrum",
            "Nhiều người nước ngoài cùng nhau học tiếng Đức ở trung tâm ngoại ngữ.",
            "Trung tâm ngoại ngữ là das Sprachzentrum (im Sprachzentrum)."
        ),
        (
            "Die Krankenschwester misst die Temperatur für den Patienten.",
            "Câu 86: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Krankenschwester misst die Temperatur für den ___.'",
            ["Patienten", "Patient", "patienten", "patient"],
            "Patienten",
            "Nữ y tá đo nhiệt độ cho người bệnh nhân.",
            "Người bệnh nhân ở Cách 4 (Akkusativ N-Deklination) là den Patienten."
        )
    ]

    for audio, q, ans, corr, hint, exp in nghe_dien_data:
        ex_list.append({
            "type": "nghe_dien",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "audio_text": audio,
                "accepted_answers": ans,
                "hint_vi": hint,
                "translation": hint
            }
        })

    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    # NHÓM 8: DỊCH CÂU VIỆT -> ĐỨC (7 CÂU: Q87 -> Q93)
    # -------------------------------------------------------------------------
    vd_sentences = [
        (
            "Câu 87: Dịch câu sau sang tiếng Đức: 'Nam nhân viên bán hàng tư vấn khách hàng rất thân thiện trong siêu thị.'",
            [
                "Der Verkäufer berät die Kunden sehr freundlich im Supermarkt.",
                "Der Verkäufer berät im Supermarkt die Kunden rất freundlich.",
                "Im Supermarkt berät der Verkäufer die Kunden sehr freundlich.",
                "Der Verkaeufer beraet die Kunden sehr freundlich im Supermarkt.",
                "Der Verkäufer berät Kunden sehr freundlich im Supermarkt."
            ],
            "Der Verkäufer berät die Kunden sehr freundlich im Supermarkt.",
            "Nam nhân viên bán hàng là Der Verkäufer; động từ beraten biến âm a -> ä (berät) đi với Akkusativ (die Kunden); ở trong siêu thị là im Supermarkt.",
            "Nam nhân viên bán hàng tư vấn khách hàng rất thân thiện trong siêu thị."
        ),
        (
            "Câu 88: Dịch câu sau sang tiếng Đức: 'Nữ thợ làm tóc có thể tạo một kiểu tóc rất đẹp.'",
            [
                "Die Friseurin kann eine sehr schöne Frisur machen.",
                "Die Friseurin kann eine sehr schöne Frisur kreieren.",
                "Die Friseurin kann eine sehr schoene Frisur machen.",
                "Eine sehr schöne Frisur kann die Friseurin machen.",
                "Die Friseurin kann eine schöne Frisur machen."
            ],
            "Die Friseurin kann eine sehr schöne Frisur machen.",
            "Nữ thợ làm tóc là Die Friseurin; có thể là kann (Modalverb ở vị trí số 2); động từ nguyên mẫu machen đứng ở cuối câu.",
            "Nữ thợ làm tóc có thể tạo một kiểu tóc rất đẹp."
        ),
        (
            "Câu 89: Dịch câu sau sang tiếng Đức: 'Các học sinh phải nộp bài tập về nhà cho thầy giáo.'",
            [
                "Die Schüler müssen dem Lehrer die Hausaufgaben abgeben.",
                "Die Schüler müssen die Hausaufgaben dem Lehrer abgeben.",
                "Die Schueler muessen dem Lehrer die Hausaufgaben abgeben.",
                "Dem Lehrer müssen die Schüler die Hausaufgaben abgeben.",
                "Die Schüler müssen dem Lehrer ihre Hausaufgaben abgeben."
            ],
            "Die Schüler müssen dem Lehrer die Hausaufgaben abgeben.",
            "Chủ ngữ die Schüler số nhiều đi với müssen; thầy giáo là người nhận ở Dativ (dem Lehrer); bài tập về nhà là Akkusativ (die Hausaufgaben); abgeben đứng cuối câu.",
            "Các học sinh phải nộp bài tập về nhà cho thầy giáo."
        ),
        (
            "Câu 90: Dịch câu sau sang tiếng Đức: 'Ở trong bệnh viện, người ta không được phép hút thuốc lá.'",
            [
                "Im Krankenhaus darf man nicht rauchen.",
                "Man darf im Krankenhaus nicht rauchen.",
                "In dem Krankenhaus darf man nicht rauchen.",
                "Im Krankenhaus darf man keine Zigaretten rauchen."
            ],
            "Im Krankenhaus darf man nicht rauchen.",
            "Ở bệnh viện là Im Krankenhaus; đại từ man chia động từ darf ở vị trí 2; không được phép hút thuốc là darf ... nicht rauchen.",
            "Ở trong bệnh viện, người ta không được phép hút thuốc lá."
        ),
        (
            "Câu 91: Dịch câu sau sang tiếng Đức: 'Người phụ nữ nội trợ chuẩn bị bữa tối cho cả gia đình trong bếp.'",
            [
                "Die Hausfrau bereitet das Abendessen für die Familie in der Küche zu.",
                "In der Küche bereitet die Hausfrau das Abendessen für die Familie zu.",
                "Die Hausfrau bereitet in der Küche das Abendessen für die Familie zu.",
                "Die Hausfrau kocht das Abendessen für die Familie in der Küche.",
                "Die Hausfrau bereitet das Abendessen fuer die Familie in der Kueche zu."
            ],
            "Die Hausfrau bereitet das Abendessen für die Familie in der Küche zu.",
            "Người phụ nữ nội trợ là Die Hausfrau; chuẩn bị là zubereiten (động từ tách: bereitet ... zu); cho gia đình là für die Familie (Akkusativ); trong bếp là in der Küche (Dativ).",
            "Người phụ nữ nội trợ chuẩn bị bữa tối cho cả gia đình trong bếp."
        ),
        (
            "Câu 92: Dịch câu sau sang tiếng Đức: 'Vị huấn luyện viên giúp đỡ các cầu thủ trẻ trong sân vận động.'",
            [
                "Der Trainer hilft den jungen Spielern im Stadion.",
                "Im Stadion hilft der Trainer den jungen Spielern.",
                "Der Trainer hilft im Stadion den jungen Spielern.",
                "Der Trainer hilft jungen Spielern im Stadion."
            ],
            "Der Trainer hilft den jungen Spielern im Stadion.",
            "Huấn luyện viên là Der Trainer; động từ helfen biến âm e -> i thành hilft và bắt buộc đi với Dativ số nhiều (den jungen Spielern); trong sân vận động là im Stadion.",
            "Vị huấn luyện viên giúp đỡ các cầu thủ trẻ trong sân vận động."
        ),
        (
            "Câu 93: Dịch câu sau sang tiếng Đức: 'Nam thư ký gọi điện cho khách hàng vì một cuộc hẹn quan trọng.'",
            [
                "Der Sekretär ruft den Kunden für einen wichtigen Termin an.",
                "Für einen wichtigen Termin ruft der Sekretär den Kunden an.",
                "Der Sekretaer ruft den Kunden fuer einen wichtigen Termin an.",
                "Der Sekretär ruft für einen wichtigen Termin den Kunden an."
            ],
            "Der Sekretär ruft den Kunden für einen wichtigen Termin an.",
            "Nam thư ký là Der Sekretär; động từ anrufen là động từ tách (ruft ... an) đi với Akkusativ (den Kunden); vì một cuộc hẹn là für einen wichtigen Termin (Akkusativ).",
            "Nam thư ký gọi điện cho khách hàng vì một cuộc hẹn quan trọng."
        )
    ]

    for q, ans, corr, exp, trans in vd_sentences:
        ex_list.append({
            "type": "dich_cau_vd",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": {
                "accepted_answers": ans,
                "translation": trans
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 9: DỊCH CÂU ĐỨC -> VIỆT (7 CÂU: Q94 -> Q100)
    # -------------------------------------------------------------------------
    dv_sentences = [
        (
            "Câu 94: Dịch câu sau sang tiếng Việt: 'Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.'",
            [
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
            "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo",
            "muss ... abholen = phải đón; ihre Tochter = con gái của cô ấy; vom Kindergarten = từ trường mẫu giáo.",
            "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen."
        ),
        (
            "Câu 95: Dịch câu sau sang tiếng Việt: 'Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen.'",
            [
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
            "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
            "ist Lehrer von Beruf = làm nghề giáo viên; hat Ferien = có kỳ nghỉ; kann bis 7 Uhr schlafen = có thể ngủ đến 7 giờ.",
            "Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen."
        ),
        (
            "Câu 96: Dịch câu sau sang tiếng Việt: 'Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen.'",
            [
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
            "Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
            "wichtig für sie = quan trọng đối với cô ấy; muss ihre Kunden oft anrufen = thường xuyên phải gọi điện cho khách hàng của mình.",
            "Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen."
        ),
        (
            "Câu 97: Dịch câu sau sang tiếng Việt: 'Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining.'",
            [
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
            "Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá",
            "bringt sein Auto in die Werkstatt = mang ô tô vào xưởng sửa chữa (Akkusativ); geht zum Fußballtraining = đi đến buổi tập bóng đá (Dativ).",
            "Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining."
        ),
        (
            "Câu 98: Dịch câu sau sang tiếng Việt: 'Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität.'",
            [
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
            "Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học",
            "vormittags = vào buổi sáng; Schüler an einer Schule = học sinh tại một trường học; nachmittags = vào buổi chiều; Studenten an der Universität = sinh viên tại trường đại học.",
            "Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität."
        ),
        (
            "Câu 99: Dịch câu sau sang tiếng Việt: 'Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat.'",
            [
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
            "Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối",
            "kann ... fernsehen = có thể xem tivi; im Wohnzimmer = ở trong phòng khách; das Abendessen machen = làm bữa tối.",
            "Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat."
        ),
        (
            "Câu 100: Dịch câu sau sang tiếng Việt: 'Der Friseur schneidet meinem Bruder im Friseursalon die Haare.'",
            [
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
            "Người thợ cắt tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc",
            "Câu kết hợp cả Dativ và Akkusativ: meinem Bruder (Wem? -> Dativ: cho anh trai tôi), im Friseursalon (Wo? -> Dativ: ở trong tiệm làm tóc), die Haare (Was? -> Akkusativ: mái tóc).",
            "Der Friseur schneidet meinem Bruder im Friseursalon die Haare."
        )
    ]

    for q, ans, corr, exp, trans in dv_sentences:
        ex_list.append({
            "type": "dich_cau_dv",
            "question": q,
            "options": None,
            "correct_answer": corr,
            "explanation": exp,
            "exp_reward": 25,
            "extra_data": {
                "accepted_answers": ans,
                "translation": corr
            }
        })

    assert len(ex_list) == 100, f"Expected 100 exercises, got {len(ex_list)}"
    assert len(vocab_list) == 50, f"Expected 50 vocab, got {len(vocab_list)}"

    # Check deduplication
    q_texts = [ex["question"] for ex in ex_list]
    assert len(set(q_texts)) == 100, f"Duplicate questions found! {len(set(q_texts))} unique."

    print("✅ All 100 exercises and 50 vocabularies created and verified unique!")

    # Format into seed_a1_b7.py
    seed_code = f'''import json
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
    # DANH MỤC 50 TỪ VỰNG TRỌNG TÂM BÀI 7 (KHỚP 100% VỚI LEXIKON_DB.JS)
    # =========================================================================
    vocab_raw = {json.dumps(vocab_list, ensure_ascii=False, indent=8)}

    vocabularies = []
    for item in vocab_raw:
        meaning = f"{{item['meaning']}} (Pl: {{item['plural']}})" if item.get("plural") else item["meaning"]
        example_str = f"{{item['example']}} ({{item['example_vi']}})" if item.get("example_vi") else item["example"]
        vocabularies.append((
            lesson_id,
            f"{{item['article']}} {{item['word']}}",
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
    print("✅ Đã khởi tạo thành công Bài 7: 'Beruf - Modalverben - Artikelwörter in Akkusativ' với đầy đủ 5 Học phần Lý thuyết + 50 Từ vựng + ĐÚNG 100 Bài tập chuẩn 9 dạng!")

if __name__ == "__main__":
    seed_lesson_7()
'''

    out_path = os.path.join(BASE_DIR, "lessons", "a1", "seed_a1_b7.py")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(seed_code)
    print(f"Generated {out_path} successfully!")

if __name__ == "__main__":
    build_full_seed_script()
