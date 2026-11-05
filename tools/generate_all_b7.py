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
        ('Mechatronikerin', 'die', 'die', 'die Mechatronikerinnen', 'eine Mechatronikerin', 'keine Mechatronikerin', 'nữ thợ cơ khí ô tô', cat1, 'Nữ thợ cơ khí ô tô (KFZ-Mechatronikerin).', 'Sie lernt fleißig und möchte eine Mechatronikerin werden.', 'Cô ấy học tập chăm chỉ và muốn trở thành một nữ thợ cơ khí.'),
        ('Trainer', 'der', 'der', 'die Trainer', 'ein Trainer', 'kein Trainer', 'nam huấn luyện viên', cat1, 'Danh từ giống đực (der Trainer), làm việc im Fitnessstudio hoặc im Stadion.', 'Der Trainer leitet das Training im Fitnessstudio.', 'Huấn luyện viên phụ trách buổi tập ở phòng gym.'),
        ('Trainerin', 'die', 'die', 'die Trainerinnen', 'eine Trainerin', 'keine Trainerin', 'nữ huấn luyện viên', cat1, 'Danh từ giống cái (die Trainerin), số nhiều die Trainerinnen.', 'Unsere Trainerin hilft den Sportlern jeden Tag im Stadion.', 'Nữ huấn luyện viên của chúng tôi giúp đỡ các vận động viên mỗi ngày ở sân vận động.'),
        ('Lehrer', 'der', 'der', 'die Lehrer', 'ein Lehrer', 'kein Lehrer', 'nam giáo viên', cat1, 'Danh từ giống đực (der Lehrer). Cấu trúc Er ist Lehrer von Beruf không dùng mạo từ.', 'Frank Müller ist Lehrer von Beruf und hat jetzt Ferien.', 'Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ.'),
        ('Lehrerin', 'die', 'die', 'die Lehrerinnen', 'eine Lehrerin', 'keine Lehrerin', 'nữ giáo viên', cat1, 'Danh từ giống cái (die Lehrerin). Giảng dạy ở trường: an einer Schule unterrichten.', 'Die Lehrerin unterrichtet Schüler an einer Schule in Berlin.', 'Nữ giáo viên giảng dạy học sinh tại một trường học ở Berlin.'),
        ('Schüler', 'der', 'der', 'die Schüler', 'ein Schüler', 'kein Schüler', 'nam học sinh (phổ thông)', cat1, 'Danh từ giống đực (der Schüler), học sinh cấp 1 đến cấp 3.', 'Der Schüler lernt viele Fächer in der Schule.', 'Cậu học sinh học nhiều môn học ở trường.'),
        ('Schülerin', 'die', 'die', 'die Schülerinnen', 'eine Schülerin', 'keine Schülerin', 'nữ học sinh (phổ thông)', cat1, 'Danh từ giống cái (die Schülerin), số nhiều die Schülerinnen.', 'Anna ist eine fleißige Schülerin am Gymnasium.', 'Anna là một nữ học sinh chăm chỉ tại trường chuyên.'),
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
        ('Patient', 'der', 'der', 'die Patienten', 'ein Patient', 'kein Patient', 'bệnh nhân', cat2, 'Danh từ giống đực N-Deklination (der Patient). Tân ngữ Akkusativ sau untersuchen: den Patienten untersuchen.', 'Der Arzt untersucht den kranken Patient im Behandlungszimmer.', 'Bác sĩ khám cho bệnh nhân bị ốm ở trong phòng khám bệnh.')
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
            "Câu 1: Chọn phương án đúng để hoàn thành cuộc hội thoại: 'Was machen Sie beruflich, Frau Lindner? — Ich arbeite ___ Programmiererin bei einer IT-Firma.'",
            ["wie eine", "als", "von", "für"],
            "als",
            "Khi dùng động từ 'arbeiten' để giới thiệu nghề nghiệp, tiếng Đức dùng giới từ 'als' + danh từ nghề nghiệp không có mạo từ (Ich arbeite als Programmiererin).",
            {"accepted_answers": ["als"], "translation": "Công việc chuyên môn của bà là gì, thưa bà Lindner? — Tôi làm nghề lập trình viên tại một công ty công nghệ thông tin."}
        ),
        (
            "Câu 2: Chọn câu đúng ngữ pháp tiếng Đức khi giới thiệu nghề nghiệp của anh trai:",
            ["Mein Bruder ist einen Lehrer von Beruf.", "Mein Bruder ist Lehrer von Beruf.", "Mein Bruder arbeitet von Beruf Lehrer.", "Mein Bruder ist der Lehrer beruflich."],
            "Mein Bruder ist Lehrer von Beruf.",
            "Với cấu trúc '[Chủ ngữ] + sein + [Nghề nghiệp] + von Beruf', danh từ chỉ nghề nghiệp đứng một mình không dùng mạo từ ein/einen.",
            {"accepted_answers": ["Mein Bruder ist Lehrer von Beruf."], "translation": "Anh trai tôi làm nghề giáo viên."}
        ),
        (
            "Câu 3: Cặp danh từ nghề nghiệp Nam – Nữ nào dưới đây được viết ĐÚNG CHÍNH TẢ 100%?",
            ["der Koch -> die Kochin / der Arzt -> die Arztin", "der Koch -> die Köchin / der Arzt -> die Ärztin", "der Koch -> die Köcherin / der Arzt -> die Ärztinn", "der Hausmann -> die Hausmännin / der Krankenpfleger -> die Krankenpfleger"],
            "der Koch -> die Köchin / der Arzt -> die Ärztin",
            "Hai danh từ der Koch và der Arzt khi chuyển sang giống cái (Femininum) vừa thêm hậu tố -in vừa phải thêm dấu Umlaut trên nguyên âm gốc: die Köchin và die Ärztin.",
            {"accepted_answers": ["der Koch -> die Köchin / der Arzt -> die Ärztin"], "translation": "Nam đầu bếp -> Nữ đầu bếp / Nam bác sĩ -> Nữ bác sĩ."}
        ),
        (
            "Câu 4: Chọn phương án đúng hoàn thành câu: 'Ein KFZ-Mechatroniker ___ Autos und arbeitet ___.'",
            ["verkauft / im Schuhgeschäft", "untersucht / im Krankenhaus", "repariert / in einer Werkstatt", "schneidet / im Friseursalon"],
            "repariert / in einer Werkstatt",
            "KFZ-Mechatroniker là thợ cơ khí ô tô; công việc là repariert Autos (sửa ô tô) và nơi làm việc (Wo? + Dativ) là in einer Werkstatt (die Werkstatt -> in einer Werkstatt).",
            {"accepted_answers": ["repariert / in einer Werkstatt"], "translation": "Một người thợ cơ khí ô tô sửa chữa xe hơi và làm việc ở trong một xưởng sửa chữa.", "dynamic_profession_quiz": True}
        ),
        (
            "Câu 5: Chọn giới từ và mạo từ đúng: 'Wo arbeitet deine Schwester? — Sie ist Floristin und arbeitet ___ Blumengeschäft neben dem Bahnhof.'",
            ["ins", "in der", "im", "auf dem"],
            "im",
            "Câu hỏi Wo? (làm việc ở đâu) đòi hỏi Cách 3 (Dativ). das Blumengeschäft mang giống trung nên in + dem viết tắt là im Blumengeschäft.",
            {"accepted_answers": ["im"], "translation": "Chị gái của bạn làm việc ở đâu? — Chị ấy là người bán hoa và làm việc ở trong cửa hàng hoa bên cạnh nhà ga."}
        ),
        (
            "Câu 6: Chọn dạng chia đúng của động từ khuyết thiếu 'müssen': 'Paula Rausch arbeitet als Programmiererin. Jeden Morgen ___ sie schon um 6.15 Uhr aufstehen.'",
            ["müsst", "musst", "muss", "müssen"],
            "muss",
            "Với động từ khuyết thiếu müssen, ngôi ich và ngôi er/sie/es chia giống hệt nhau là muss (đổi ü -> u và không có đuôi -t).",
            {"accepted_answers": ["muss"], "translation": "Paula Rausch làm nghề lập trình viên. Mỗi buổi sáng cô ấy đã phải thức dậy lúc 6 giờ 15 phút.", "dynamic_modalverb_schedule_quiz": True}
        ),
        (
            "Câu 7: Chọn phương án đúng: 'Kinder, heute habt ihr Ferien! ___ ihr bis 9 Uhr schlafen?'",
            ["Könnt", "Kannst", "Können", "Kannt"],
            "Könnt",
            "Chủ ngữ là ihr (các con/các bạn), động từ können giữ nguyên nguyên âm ö và chia đuôi -t thành könnt.",
            {"accepted_answers": ["Könnt"], "translation": "Các con ơi, hôm nay các con được nghỉ lễ! Các con có thể ngủ đến 9 giờ không?"}
        ),
        (
            "Câu 8: Chọn câu đúng trật tự từ ngữ pháp tiếng Đức:",
            ["Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholt.", "Um 16.30 Uhr holt Paula ihre Tochter vom Kindergarten müssen ab.", "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.", "Um 16.30 Uhr muss abholen Paula ihre Tochter vom Kindergarten."],
            "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen.",
            "Khi có động từ khuyết thiếu muss đứng ở vị trí số 2, động từ tách abholen không tách nữa mà giữ nguyên dạng nguyên mẫu (Infinitiv) đứng ở cuối câu.",
            {"accepted_answers": ["Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen."], "translation": "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo."}
        ),
        (
            "Câu 9: Chọn cặp từ đúng điền vào câu: 'Bei ihrer Arbeit braucht Petra ___ Computer und ___ großen Schreibtisch.'",
            ["ein / ein", "einen / einen", "einem / einem", "den / dem"],
            "einen / einen",
            "Động từ brauchen (cần cái gì) luôn đi với tân ngữ trực tiếp ở Cách 4 (Akkusativ). Cả der Computer và der Schreibtisch đều mang giống đực (Maskulinum), nên mạo từ ein đổi thành einen.",
            {"accepted_answers": ["einen / einen"], "translation": "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."}
        ),
        (
            "Câu 10: Chọn phương án đúng: 'Herr Weber arbeitet heute von zu Hause. Er braucht ___ Anzug, sondern nur ___ Laptop.'",
            ["kein / ein", "keinen / einen", "keinem / một", "keine / eine"],
            "keinen / einen",
            "Cả der Anzug và der Laptop đều là danh từ giống đực làm tân ngữ trực tiếp (Akkusativ) sau động từ braucht, nên chia là keinen Anzug và einen Laptop.",
            {"accepted_answers": ["keinen / einen"], "translation": "Hôm nay ông Weber làm việc tại nhà. Ông ấy không cần bộ vest nào cả mà chỉ cần một chiếc máy tính xách tay."}
        ),
        (
            "Câu 11: Chọn phương án đúng: 'Die Sekretärin muss heute Vormittag ___ Chef und ___ Kunden anrufen.'",
            ["ihren / ihre", "ihrem / ihren", "ihre / ihren", "ihr / ihre"],
            "ihren / ihre",
            "Động từ anrufen (gọi điện cho ai) đi với Cách 4 (Akkusativ). Với der Chef (giống đực), mạo từ sở hữu của cô ấy (ihr-) đổi thành ihren Chef; với die Kunden (số nhiều) ở Akkusativ thì giữ nguyên đuôi -e là ihre Kunden.",
            {"accepted_answers": ["ihren / ihre"], "translation": "Nữ thư ký sáng nay phải gọi điện cho ông sếp của cô ấy và các khách hàng của cô ấy."}
        ),
        (
            "Câu 12: Chọn cặp mạo từ đúng điền vào 2 câu sau: '1. Die Ärztin untersucht ___ kranken Mann. — 2. Die Krankenschwester hilft ___ kranken Mann.'",
            ["den / den", "dem / den", "den / dem", "der / dem"],
            "den / dem",
            "Động từ untersuchen (khám bệnh cho ai) đòi hỏi Cách 4 (Akkusativ) -> den kranken Mann. Ngược lại, động từ helfen (giúp đỡ ai) bắt buộc đi với Cách 3 (Dativ) -> dem kranken Mann.",
            {"accepted_answers": ["den / dem"], "translation": "1. Nữ bác sĩ khám cho người đàn ông bị ốm. — 2. Nữ y tá giúp đỡ người đàn ông bị ốm.", "dynamic_akkdativ_kontrast_quiz": True}
        ),
        (
            "Câu 13: Chọn phương án đúng hoàn thành câu: '___ seiner Arbeit im Krankenhaus hat der Arzt wenig Pause, aber die Arbeit ist sehr wichtig ___ seine Patienten.'",
            ["Für / bei", "Bei / für", "Mit / von", "Zu / ohne"],
            "Bei / für",
            "Cụm 'Trong công việc của mình' dùng Bei seiner Arbeit (bei + Dativ), còn 'quan trọng đối với ai' dùng wichtig für + Akkusativ (für seine Patienten).",
            {"accepted_answers": ["Bei / für"], "translation": "Trong công việc của mình ở bệnh viện, vị bác sĩ có ít thời gian nghỉ giải lao, nhưng công việc đó rất quan trọng đối với các bệnh nhân của ông ấy."}
        ),
        (
            "Câu 14: Chọn phương án đúng điền vào 2 chỗ trống: 'Um 8.30 Uhr bringt Frank seine Tochter ___ Kindergarten (Wohin?), und um 16.30 Uhr holt Paula die Tochter ___ Kindergarten (Woher?) ab.'",
            ["im / in den", "in den / vom", "zum / im", "in dem / von der"],
            "in den / vom",
            "Đưa vào trường mẫu giáo (bringen -> câu hỏi Wohin? + Akkusativ) với danh từ giống đực der Kindergarten là in den Kindergarten. Đón từ trường mẫu giáo về (abholen -> von + Dativ) là vom Kindergarten.",
            {"accepted_answers": ["in den / vom"], "translation": "Lúc 8 giờ 30 phút Frank đưa con gái vào trường mẫu giáo, và lúc 16 giờ 30 phút Paula đón con gái từ trường mẫu giáo về."}
        ),
        (
            "Câu 15: Chọn cặp từ đúng: 'Herr Müller bringt sein Auto ___ Werkstatt (Wohin?). Dort repariert der Mechatroniker das Auto ___ Werkstatt (Wo?).'",
            ["in die / in der", "in der / in die", "zur / in die", "in eine / in eine"],
            "in die / in der",
            "Danh từ die Werkstatt mang giống cái (Femininum). Khi di chuyển vào xưởng (Wohin? + Akkusativ) dùng in die Werkstatt; khi làm việc ở bên trong xưởng (Wo? + Dativ) dùng in der Werkstatt.",
            {"accepted_answers": ["in die / in der"], "translation": "Ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa. Ở đó người thợ cơ khí sửa chiếc ô tô ở trong xưởng."}
        ),
        (
            "Câu 16: Chọn phương án đúng: 'Um 19 Uhr bringt die Mutter ihren Sohn ___ Bett. Um 20 Uhr liegt er schon ___ Bett und schläft.'",
            ["im / ins", "ins / im", "in dem / in das", "ans / am"],
            "ins / im",
            "Đưa lên giường (bringen — di chuyển Wohin?) dùng in + das = ins Bett (Akkusativ). Nằm ngủ trên giường (liegen/schlafen — vị trí tĩnh Wo?) dùng in + dem = im Bett (Dativ).",
            {"accepted_answers": ["ins / im"], "translation": "Lúc 19 giờ người mẹ đưa con trai lên giường ngủ. Lúc 20 giờ cậu bé đã nằm trên giường và ngủ."}
        ),
        (
            "Câu 17: Chọn phương án đúng ngữ pháp: 'Der Chef kauft ___ Sekretärin (die Sekretärin) ___ neuen Computer (der Computer).'",
            ["die / einen", "der / einen", "der / một", "einer / den"],
            "der / einen",
            "Trong câu có 2 tân ngữ: Người nhận lợi ích (Wem? cho nữ thư ký) chia ở Cách 3 (Dativ) -> der Sekretärin; Vật được mua (Was? một chiếc máy tính mới) chia ở Cách 4 (Akkusativ) -> einen neuen Computer.",
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
    # NHÓM 2: ĐIỀN KHUYẾT (15 CÂU: Q19 -> Q33)
    # -------------------------------------------------------------------------
    fill_blanks = [
        ("Câu 19: Điền giới từ chỉ nghề nghiệp thích hợp vào chỗ trống: 'Mein Onkel arbeitet seit fünf Jahren ___ Taxifahrer in Hamburg.'", ["als"], "als", "Cụm arbeiten als + [Nghề nghiệp] dùng để nói làm nghề gì.", "Chú của tôi làm nghề tài xế taxi ở Hamburg từ 5 năm nay."),
        ("Câu 20: Điền danh từ nghề nghiệp dạng Nữ (Femininum) tương ứng với 'der Arzt' vào chỗ trống: 'Meine Tante arbeitet im Krankenhaus. Sie ist ___ von Beruf.'", ["Ärztin", "Aerztin"], "Ärztin", "der Arzt khi chuyển sang danh từ nghề nghiệp nữ phải thêm dấu Umlaut và đuôi -in thành Ärztin.", "Dì của tôi làm việc ở trong bệnh viện. Dì ấy làm nghề nữ bác sĩ."),
        ("Câu 21: Điền danh từ nghề nghiệp dạng Nữ (Femininum) tương ứng với 'der Koch' vào chỗ trống: 'Frau Bui kocht sehr gut in einem großen Restaurant. Sie arbeitet als ___.'", ["Köchin", "Koechin"], "Köchin", "der Koch chuyển sang giống cái thêm Umlaut o -> ö và -in thành Köchin.", "Bà Bùi nấu ăn rất ngon trong một nhà hàng lớn. Bà ấy làm nghề nữ đầu bếp."),
        ("Câu 22: Điền dạng chia đúng của động từ khuyết thiếu 'müssen' vào chỗ trống: 'Ich habe morgen eine Prüfung, deshalb ___ ich heute Abend viel lernen.'", ["muss"], "muss", "Ngôi thứ nhất số ít (ich) của động từ müssen là muss.", "Ngày mai tôi có một kỳ thi, vì vậy tối nay tôi phải học bài nhiều."),
        ("Câu 23: Điền dạng chia đúng của động từ khuyết thiếu 'müssen' vào chỗ trống: 'Wann ___ du morgen früh zur Arbeit fahren, Lukas?'", ["musst"], "musst", "Ngôi thứ hai số ít (du) của động từ müssen là musst.", "Sáng sớm mai bạn phải đi làm lúc mấy giờ thế, Lukas?"),
        ("Câu 24: Điền dạng chia đúng của động từ khuyết thiếu 'können' vào chỗ trống: 'Herr Müller hat heute Ferien. Er ___ bis 8 Uhr schlafen.'", ["kann"], "kann", "Ngôi thứ ba số ít (er) của động từ können là kann (không có đuôi -t).", "Ông Müller hôm nay có kỳ nghỉ. Ông ấy có thể ngủ đến 8 giờ."),
        ("Câu 25: Điền dạng chia đúng của động từ khuyết thiếu 'möchten' vào chỗ trống: 'Anna ist Schülerin, aber später ___ sie Medizin an der Universität studieren.'", ["möchte", "moechte"], "möchte", "Ngôi thứ ba số ít (sie - cô ấy) của möchten là möchte.", "Anna là học sinh, nhưng sau này cô ấy muốn học ngành Y ở trường đại học."),
        ("Câu 26: Điền dạng nguyên mẫu của động từ tách 'aufstehen' vào cuối câu có Modalverb: 'Am Sonntag müssen wir nicht früh ___.'", ["aufstehen"], "aufstehen", "Khi câu đã có động từ khuyết thiếu müssen ở vị trí số 2, động từ tách aufstehen giữ nguyên dạng nguyên mẫu viết liền ở cuối câu.", "Vào Chủ nhật chúng tôi không phải thức dậy sớm."),
        ("Câu 27: Điền mạo từ không xác định đúng ở Cách 4 (Akkusativ) vào chỗ trống: 'Für seine Arbeit im Büro braucht mein Bruder ___ schnellen Laptop.'", ["einen"], "einen", "Động từ brauchen đòi hỏi Cách 4 (Akkusativ). der Laptop mang giống đực nên ein đổi thành einen.", "Cho công việc của mình ở văn phòng, anh trai tôi cần một chiếc máy tính xách tay nhanh."),
        ("Câu 28: Điền mạo từ phủ định 'kein' đúng ở Cách 4 (Akkusativ) vào chỗ trống: 'Ich trinke meinen Tee bitte ohne Zucker, ich brauche ___ Löffel.'", ["keinen"], "keinen", "der Löffel mang giống đực, làm tân ngữ trực tiếp (Akkusativ) sau brauche, nên kein đổi thành keinen.", "Tôi uống trà không đường, tôi không cần cái thìa nào cả."),
        ("Câu 29: Điền mạo từ sở hữu của ngôi 'er' (sein-) đúng ở Cách 4 (Akkusativ) vào chỗ trống: 'Der Programmierer ruft ___ Chef im Büro an.'", ["seinen"], "seinen", "Động từ anrufen đi với Cách 4 (Akkusativ). der Chef mang giống đực nên gốc sở hữu sein- của er đổi thành seinen.", "Lập trình viên gọi điện cho ông sếp của anh ấy ở văn phòng."),
        ("Câu 30: Điền mạo từ xác định đúng (phân biệt Wohin? Akkusativ) vào chỗ trống: 'Jeden Morgen um 8 Uhr bringt Frau Rausch ihren Sohn in ___ Kindergarten.'", ["den"], "den", "Hành động đưa con đến trường mẫu giáo (bringen -> câu hỏi Wohin?) dùng Cách 4 (Akkusativ): der Kindergarten -> in den Kindergarten.", "Mỗi buổi sáng lúc 8 giờ bà Rausch đưa con trai mình vào trường mẫu giáo."),
        ("Câu 31: Điền giới từ thu gọn (in + das) chỉ hướng di chuyển Wohin? (Akkusativ) vào chỗ trống: 'Es ist schon 22 Uhr. Die Kinder müssen jetzt ___ Bett gehen.'", ["ins"], "ins", "Đi lên giường ngủ (Wohin? + Akkusativ) với danh từ giống trung das Bett dùng in + das gộp thành ins Bett.", "Đã 22 giờ rồi. Bọn trẻ bây giờ phải đi lên giường ngủ."),
        ("Câu 32: Điền mạo từ xác định đúng ở Cách 3 (Dativ) sau động từ 'helfen': 'Die Sekretärin hilft ___ neuen Praktikanten bei der Arbeit.'", ["dem"], "dem", "Động từ helfen luôn đi với Cách 3 (Dativ), nên der Praktikant chuyển thành dem neuen Praktikanten.", "Nữ thư ký giúp đỡ nam thực tập sinh mới trong công việc."),
        ("Câu 33: Điền dạng chia đúng của động từ 'unterrichten' theo chủ ngữ vào chỗ trống: 'Herr Müller ist Lehrer von Beruf und ___ Mathematik an einer Schule.'", ["unterrichtet"], "unterrichtet", "Động từ unterrichten có gốc kết thúc bằng -t (unterricht-), nên ở ngôi thứ 3 số ít (er) phải thêm -e- trước -t thành unterrichtet.", "Ông Müller làm nghề giáo viên và giảng dạy môn Toán tại một trường học.")
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
                "translation": q.split("'")[1] if "'" in q else corr
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 5: NỐI Ô TỪ TRÁI QUA PHẢI (10 BÀI: Q58 -> Q67, mỗi bài 4 cặp)
    # -------------------------------------------------------------------------
    noi_o_data = [
        (
            "Câu 58: Nối Nghề nghiệp với Hoạt động đặc trưng tương ứng:",
            [
                {"left": "der Lehrer / die Lehrerin", "right": "unterrichtet Schüler (giảng dạy học sinh)"},
                {"left": "der Arzt / die Ärztin", "right": "untersucht Patienten (khám cho bệnh nhân)"},
                {"left": "der KFZ-Mechatroniker", "right": "repariert Autos (sửa chữa xe ô tô)"},
                {"left": "der Programmierer", "right": "schreibt Computerprogramme (viết chương trình máy tính)"}
            ],
            "Nghề giáo viên giảng dạy học sinh, bác sĩ khám bệnh nhân, thợ cơ khí sửa ô tô, lập trình viên viết phần mềm."
        ),
        (
            "Câu 59: Nối Nghề nghiệp với Hoạt động đặc trưng tương ứng (Phần 2):",
            [
                {"left": "der Friseur / die Friseurin", "right": "schneidet Haare (cắt tóc)"},
                {"left": "der Verkäufer / die Verkäuferin", "right": "verkauft Schuhe (bán giày dép)"},
                {"left": "der Florist / die Floristin", "right": "verkauft Blumen (bán hoa tươi)"},
                {"left": "der Koch / die Köchin", "right": "kocht leckere Speisen (nấu những món ăn ngon)"}
            ],
            "Thợ làm tóc cắt tóc, nhân viên bán hàng bán giày dép, thợ hoa bán hoa, đầu bếp nấu món ăn ngon."
        ),
        (
            "Câu 60: Nối Nghề nghiệp với Nơi làm việc chuẩn ở Dativ:",
            [
                {"left": "der Lehrer", "right": "arbeitet an einer Schule / im Sprachzentrum"},
                {"left": "die Ärztin und der Krankenpfleger", "right": "arbeiten im Krankenhaus"},
                {"left": "der KFZ-Mechatroniker", "right": "arbeitet in einer Werkstatt"},
                {"left": "die Friseurin", "right": "arbeitet im Friseursalon"}
            ],
            "Giáo viên làm việc ở trường học/trung tâm ngoại ngữ, bác sĩ và y tá ở bệnh viện, thợ cơ khí ở xưởng, thợ tóc ở tiệm làm tóc."
        ),
        (
            "Câu 61: Nối Danh từ Nghề nghiệp Nam với Dạng Nữ đặc biệt:",
            [
                {"left": "der Arzt (nam bác sĩ)", "right": "die Ärztin (thêm Umlaut ä + -in)"},
                {"left": "der Koch (nam đầu bếp)", "right": "die Köchin (thêm Umlaut ö + -in)"},
                {"left": "der Hausmann (nam nội trợ)", "right": "die Hausfrau (đổi gốc sang -frau)"},
                {"left": "der Krankenpfleger (nam điều dưỡng)", "right": "die Krankenschwester / die Krankenpflegerin"}
            ],
            "Các trường hợp biến đổi đặc biệt sang giống cái: thêm Umlaut (Ärztin, Köchin), đổi gốc (Hausfrau), và danh xưng truyền thống (Krankenschwester)."
        ),
        (
            "Câu 62: Nối Chủ ngữ với Dạng chia của Động từ khuyết thiếu müssen và können:",
            [
                {"left": "ich / er / sie / es (với müssen)", "right": "muss (đổi ü -> u, không có đuôi)"},
                {"left": "ich / er / sie / es (với können)", "right": "kann (đổi ö -> a, không có đuôi)"},
                {"left": "du (với müssen & können)", "right": "musst / kannst (thêm đuôi -st)"},
                {"left": "ihr (với müssen & können)", "right": "müsst / könnt (giữ Umlaut, thêm đuôi -t)"}
            ],
            "Quy tắc chia Modalverben: ngôi 1 và 3 số ít đổi nguyên âm và không có đuôi; ngôi du thêm -st; ngôi ihr giữ nguyên âm gốc và thêm đuôi -t."
        ),
        (
            "Câu 63: Nối Câu hỏi Nghề nghiệp & Nơi làm việc với Câu trả lời chuẩn:",
            [
                {"left": "Was sind Sie von Beruf?", "right": "Ich bin Sekretärin von Beruf."},
                {"left": "Als was arbeitet dein Bruder?", "right": "Er arbeitet als Programmierer."},
                {"left": "Wo arbeitet Frau Wagner?", "right": "Sie arbeitet im Blumengeschäft."},
                {"left": "Was muss Petra im Büro machen?", "right": "Sie muss ihre Kunden anrufen."}
            ],
            "Cặp câu hỏi và câu trả lời hoàn chỉnh tương ứng về nghề nghiệp, nơi làm việc và nhiệm vụ công việc."
        ),
        (
            "Câu 64: Phân biệt Động từ đi với Cách 4 (Akkusativ) vs. Động từ đi với Cách 3 (Dativ):",
            [
                {"left": "brauchen (cần) & suchen (tìm)", "right": "luôn đi với Cách 4 (Akkusativ: einen Computer)"},
                {"left": "anrufen (gọi điện) & untersuchen (khám)", "right": "luôn đi với Cách 4 (Akkusativ: den Patienten)"},
                {"left": "helfen (giúp đỡ) & danken (cảm ơn)", "right": "luôn đi với Cách 3 (Dativ: dem Arzt)"},
                {"left": "gefallen (làm ai thích) & gehören (thuộc về)", "right": "luôn đi với Cách 3 (Dativ: meiner Mutter)"}
            ],
            "Động từ Akkusativ chỉ tân ngữ trực tiếp (cần, tìm, gọi, khám); Động từ Dativ quy định người nhận tác động (giúp đỡ, cảm ơn, thích, thuộc về)."
        ),
        (
            "Câu 65: Đối chiếu trực tiếp giữa Hướng di chuyển Wohin? (Akkusativ) và Vị trí tĩnh Wo? (Dativ):",
            [
                {"left": "in den Kindergarten bringen (Wohin?)", "right": "im Kindergarten spielen (Wo?)"},
                {"left": "in die Werkstatt fahren (Wohin?)", "right": "in der Werkstatt reparieren (Wo?)"},
                {"left": "ins Bett gehen (Wohin?)", "right": "im Bett schlafen (Wo?)"},
                {"left": "ins Büro kommen (Wohin?)", "right": "im Büro arbeiten (Wo?)"}
            ],
            "Wohin? (hướng di chuyển) dùng Akkusativ (in den Kindergarten, in die Werkstatt, ins Bett, ins Büro); Wo? (vị trí tĩnh) dùng Dativ (im Kindergarten, in der Werkstatt, im Bett, im Büro)."
        ),
        (
            "Câu 66: Biến đổi Từ hạn định từ Nominativ sang Akkusativ:",
            [
                {"left": "der Tisch / ein Computer (Maskulinum)", "right": "den Tisch / einen Computer (đổi sang đuôi -en)"},
                {"left": "die Tasche / meine Tochter (Femininum)", "right": "die Tasche / meine Tochter (giữ nguyên)"},
                {"left": "das Buch / kein Auto (Neutrum)", "right": "das Buch / kein Auto (giữ nguyên)"},
                {"left": "die Bücher / ihre Kunden (Plural)", "right": "die Bücher / ihre Kunden (giữ nguyên, không thêm -n)"}
            ],
            "Ở Cách 4 Akkusativ, chỉ duy nhất giống đực (der) biến đổi đuôi sang -en; giống cái, giống trung và số nhiều giữ nguyên dạng Nominativ."
        ),
        (
            "Câu 67: Nối Mốc thời gian với Hoạt động trong lịch trình của Paula Rausch & Frank Müller:",
            [
                {"left": "Paula: um 6.15 Uhr", "right": "muss sie aufstehen"},
                {"left": "Paula: um 16.30 Uhr", "right": "muss sie ihre Tochter vom Kindergarten abholen"},
                {"left": "Frank: bis 7.00 Uhr", "right": "kann er schlafen, weil er Ferien hat"},
                {"left": "Frank: um 12.30 Uhr", "right": "bringt er das Auto in die Werkstatt"}
            ],
            "Lịch trình hàng ngày thực tế của Paula Rausch và Frank Müller trong đoạn văn bài học."
        )
    ]

    for q, pairs, exp in noi_o_data:
        ex_list.append({
            "type": "noi_o",
            "question": q,
            "options": None,
            "correct_answer": "Hoàn thành nối ô",
            "explanation": exp,
            "exp_reward": 20,
            "extra_data": {
                "noi_o_pairs": pairs,
                "translation": "Nối các cặp tương ứng giữa 2 cột."
            }
        })

    # -------------------------------------------------------------------------
    # NHÓM 6: ĐIỀN TẠO CÂU (10 CÂU: Q68 -> Q77, điền 2 từ ngăn cách bởi dấu /)
    # -------------------------------------------------------------------------
    dien_tao_cau_data = [
        ("Câu 68: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Um 6.15 Uhr [1] Paula [2].' (Gợi ý: 'Lúc 6 giờ 15 phút Paula phải thức dậy.')", ["muss / aufstehen", "muss/aufstehen"], "muss / aufstehen", "Um 6.15 Uhr [1] Paula [2].", "Động từ khuyết thiếu müssen chia theo ngôi thứ 3 số ít (Paula) là muss đứng ở vị trí số 2; động từ tách aufstehen giữ nguyên mẫu viết liền ở cuối câu.", "Lúc 6 giờ 15 phút Paula phải thức dậy."),
        ("Câu 69: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Von 20 bis 22 Uhr [1] sie [2].' (Gợi ý: 'Từ 20 giờ đến 22 giờ cô ấy có thể xem tivi.')", ["kann / fernsehen", "kann/fernsehen"], "kann / fernsehen", "Von 20 bis 22 Uhr [1] sie [2].", "können chia cho ngôi sie (cô ấy) là kann ở vị trí số 2; động từ tách fernsehen giữ nguyên mẫu ở cuối câu.", "Từ 20 giờ đến 22 giờ cô ấy có thể xem tivi."),
        ("Câu 70: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Um 16.30 Uhr muss sie ihre Tochter [1] Kindergarten [2].' (Gợi ý: 'Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo.')", ["vom / abholen", "vom/abholen"], "vom / abholen", "Um 16.30 Uhr muss sie ihre Tochter [1] Kindergarten [2].", "Đón từ trường mẫu giáo dùng von + dem = vom Kindergarten; động từ abholen đứng nguyên mẫu ở cuối câu sau muss.", "Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo."),
        ("Câu 71: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Bei [1] Arbeit braucht Petra [2] Computer und einen großen Schreibtisch.' (Gợi ý: 'Trong công việc của mình, Petra cần một chiếc máy tính và một chiếc bàn làm việc lớn.')", ["ihrer / einen", "ihrer/einen"], "ihrer / einen", "Bei [1] Arbeit braucht Petra [2] Computer und einen großen Schreibtisch.", "Sau giới từ Bei là Cách 3 (Dativ) với die Arbeit (giống cái) -> Bei ihrer Arbeit. Sau động từ braucht là Cách 4 (Akkusativ) với der Computer (giống đực) -> einen Computer.", "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."),
        ("Câu 72: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Am Morgen bringt Frank die Tochter in [1] Kindergarten, und am Nachmittag spielt sie [2] Kindergarten.' (Gợi ý: 'Buổi sáng Frank đưa con gái vào trường mẫu giáo, và buổi chiều con bé chơi ở trong trường mẫu giáo.')", ["den / im", "den/im"], "den / im", "Am Morgen bringt Frank die Tochter in [1] Kindergarten, und am Nachmittag spielt sie [2] Kindergarten.", "Đưa vào trường mẫu giáo (Wohin? + Akkusativ) là in den Kindergarten; chơi ở trong trường mẫu giáo (Wo? + Dativ) là im Kindergarten.", "Buổi sáng Frank đưa con gái vào trường mẫu giáo, và buổi chiều con bé chơi ở trong trường mẫu giáo."),
        ("Câu 73: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Arzt untersucht [1] Patienten [2] Krankenhaus.' (Gợi ý: 'Vị bác sĩ khám cho người bệnh nhân ở trong bệnh viện.')", ["den / im", "den/im"], "den / im", "Der Arzt untersucht [1] Patienten [2] Krankenhaus.", "untersuchen đi với Akkusativ (den Patienten), còn nơi chốn tĩnh Wo? với das Krankenhaus đi với Dativ (im Krankenhaus).", "Vị bác sĩ khám cho người bệnh nhân ở trong bệnh viện."),
        ("Câu 74: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Meine Schwester arbeitet als [1] und [2] sehr gut kochen.' (Gợi ý: 'Chị gái của tôi làm nghề nữ đầu bếp và có thể nấu ăn rất giỏi.')", ["Köchin / kann", "Köchin/kann", "Koechin / kann", "Koechin/kann"], "Köchin / kann", "Meine Schwester arbeitet als [1] und [2] sehr gut kochen.", "Nữ đầu bếp là Köchin; động từ können chia cho meine Schwester (sie) là kann.", "Chị gái của tôi làm nghề nữ đầu bếp và có thể nấu ăn rất giỏi."),
        ("Câu 75: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Der Krankenpfleger gibt [1] Arzt [2] Kuli.' (Gợi ý: 'Người nam điều dưỡng đưa cho vị bác sĩ một chiếc bút bi.')", ["dem / einen", "dem/einen"], "dem / einen", "Der Krankenpfleger gibt [1] Arzt [2] Kuli.", "Người nhận (Wem? cho bác sĩ) chia ở Cách 3 (Dativ) -> dem Arzt; vật được đưa (Was? một chiếc bút bi) chia ở Cách 4 (Akkusativ) -> einen Kuli.", "Người nam điều dưỡng đưa cho vị bác sĩ một chiếc bút bi."),
        ("Câu 76: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): 'Um 12.30 Uhr [1] er das Auto in [2] Werkstatt.' (Gợi ý: 'Lúc 12 giờ 30 phút anh ấy mang chiếc ô tô vào xưởng sửa chữa.')", ["bringt / die", "bringt/die"], "bringt / die", "Um 12.30 Uhr [1] er das Auto in [2] Werkstatt.", "Động từ bringen chia ở ngôi er là bringt; mang vào xưởng (Wohin? + Akkusativ) với danh từ giống cái die Werkstatt là in die Werkstatt.", "Lúc 12 giờ 30 phút anh ấy mang chiếc ô tô vào xưởng sửa chữa."),
        ("Câu 77: Điền 2 từ còn thiếu vào các chỗ trống (ngăn cách bởi dấu /): '[1] ihr am Samstag [2] Büro arbeiten?' (Gợi ý: 'Các bạn có phải làm việc vào thứ Bảy ở trong văn phòng không?')", ["Müsst / im", "Müsst/im", "müsst / im", "müsst/im", "Muesst / im", "muesst / im"], "Müsst / im", "[1] ihr am Samstag [2] Büro arbeiten?", "Câu hỏi đảo động từ khuyết thiếu müssen với chủ ngữ ihr là Müsst ihr ...?; làm việc ở trong văn phòng (Wo? + Dativ) là im Büro.", "Các bạn có phải làm việc vào thứ Bảy ở trong văn phòng không?")
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
    # NHÓM 7: NGHE ĐIỀN (9 CÂU: Q78 -> Q86)
    # -------------------------------------------------------------------------
    nghe_dien_data = [
        ("Paula Rausch ist fünfunddreißig Jahre alt und arbeitet als Programmiererin.", "Câu 78: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Paula Rausch ist 35 Jahre alt und arbeitet als ___.'", ["Programmiererin"], "Programmiererin", "Paula Rausch 35 tuổi và làm nghề nữ lập trình viên.", "Danh từ chỉ nữ lập trình viên là die Programmiererin."),
        ("Der KFZ-Mechatroniker repariert Autos in einer Werkstatt.", "Câu 79: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der KFZ-Mechatroniker repariert Autos in einer ___.'", ["Werkstatt"], "Werkstatt", "Người thợ cơ khí ô tô sửa chữa xe hơi ở trong một xưởng sửa chữa.", "Danh từ die Werkstatt có nghĩa là xưởng sửa chữa (in einer Werkstatt)."),
        ("Der Arzt untersucht jeden Tag viele Patienten im Krankenhaus.", "Câu 80: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Der Arzt ___ jeden Tag viele Patienten im Krankenhaus.'", ["untersucht"], "untersucht", "Vị bác sĩ khám cho nhiều bệnh nhân mỗi ngày ở trong bệnh viện.", "Động từ untersuchen (khám bệnh) chia ở ngôi thứ 3 số ít (der Arzt) là untersucht."),
        ("Bei ihrer Arbeit braucht Petra einen schnellen Computer und einen großen Schreibtisch.", "Câu 81: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Bei ihrer Arbeit braucht Petra ___ schnellen Computer und einen großen Schreibtisch.'", ["einen"], "einen", "Trong công việc của mình, Petra cần một chiếc máy tính nhanh và một cái bàn làm việc lớn.", "Sau động từ braucht (Akkusativ), mạo từ không xác định của der Computer là einen."),
        ("Um sechzehn Uhr dreißig muss sie ihre Tochter vom Kindergarten abholen.", "Câu 82: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Um 16.30 Uhr muss sie ihre Tochter vom Kindergarten ___.'", ["abholen"], "abholen", "Lúc 16 giờ 30 phút cô ấy phải đón con gái của mình từ trường mẫu giáo.", "Động từ tách abholen đứng ở cuối câu ở dạng nguyên mẫu khi đi cùng muss."),
        ("Frank Müller ist Lehrer von Beruf und hat jetzt Ferien.", "Câu 83: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Frank Müller ist ___ von Beruf und hat jetzt Ferien.'", ["Lehrer"], "Lehrer", "Frank Müller làm nghề giáo viên và hiện đang có kỳ nghỉ.", "Danh từ chỉ nam giáo viên là der Lehrer (Er ist Lehrer von Beruf)."),
        ("Die Floristin verkauft schöne Blumen im Blumengeschäft.", "Câu 84: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Die Floristin verkauft schöne Blumen im ___.'", ["Blumengeschäft", "Blumengeschaeft"], "Blumengeschäft", "Người nữ bán hoa bán những bông hoa đẹp ở trong cửa hàng hoa.", "Danh từ das Blumengeschäft có nghĩa là cửa hàng hoa (im Blumengeschäft)."),
        ("Sie muss ihre Kunden im Büro oft anrufen.", "Câu 85: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Sie muss ihre ___ im Büro oft anrufen.'", ["Kunden"], "Kunden", "Cô ấy thường xuyên phải gọi điện cho các khách hàng của mình ở trong văn phòng.", "Danh từ số nhiều die Kunden có nghĩa là những khách hàng."),
        ("Um neunzehn Uhr bringt der Vater seine Tochter ins Bett.", "Câu 86: Nghe phát âm tiếng Đức và điền từ còn thiếu vào chỗ trống: 'Um 19 Uhr bringt der Vater seine Tochter ___ Bett.'", ["ins"], "ins", "Lúc 19 giờ người bố đưa con gái của mình lên giường đi ngủ.", "Cụm ins Bett bringen (in + das Bett — Wohin? Akkusativ) có nghĩa là đưa lên giường đi ngủ.")
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
    # NHÓM 8: DỊCH CÂU VIỆT -> ĐỨC (7 CÂU: Q87 -> Q93)
    # -------------------------------------------------------------------------
    vd_sentences = [
        (
            "Câu 87: Dịch câu sau sang tiếng Đức: 'Bạn làm nghề gì? — Tôi làm nghề lập trình viên.'",
            ["Was bist du von Beruf? Ich arbeite als Programmierer.", "Was bist du von Beruf? Ich bin Programmierer.", "Was bist du von Beruf? Ich bin Programmierer von Beruf.", "Was machst du beruflich? Ich arbeite als Programmierer.", "Was machst du beruflich? Ich bin Programmiererin.", "Was machst du beruflich? Ich bin Programmierer."],
            "Was bist du von Beruf? Ich arbeite als Programmierer.",
            "Hỏi nghề nghiệp thân mật dùng Was bist du von Beruf? hoặc Was machst du beruflich?; trả lời dùng Ich bin Programmierer hoặc Ich arbeite als Programmierer.",
            "Bạn làm nghề gì? — Tôi làm nghề lập trình viên."
        ),
        (
            "Câu 88: Dịch câu sau sang tiếng Đức: 'Lúc 7 giờ 15 phút cô ấy phải đi bằng xe buýt đến chỗ làm.'",
            ["Um 7.15 Uhr muss sie mit dem Bus zur Arbeit fahren.", "Um Viertel nach sieben muss sie mit dem Bus zur Arbeit fahren.", "Sie muss um 7.15 Uhr mit dem Bus zur Arbeit fahren.", "Um sieben Uhr fünfzehn muss sie mit dem Bus zur Arbeit fahren."],
            "Um 7.15 Uhr muss sie mit dem Bus zur Arbeit fahren.",
            "Động từ khuyết thiếu muss đứng ở vị trí số 2, động từ chính fahren đứng nguyên mẫu ở cuối câu; phương tiện mit dem Bus và đích đến zur Arbeit đều chia ở Dativ.",
            "Lúc 7 giờ 15 phút cô ấy phải đi bằng xe buýt đến chỗ làm."
        ),
        (
            "Câu 89: Dịch câu sau sang tiếng Đức: 'Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn.'",
            ["Bei ihrer Arbeit braucht Petra einen Computer und einen großen Schreibtisch.", "Petra braucht bei ihrer Arbeit einen Computer und einen großen Schreibtisch.", "Für ihre Arbeit braucht Petra einen Computer und einen großen Schreibtisch."],
            "Bei ihrer Arbeit braucht Petra einen Computer und einen großen Schreibtisch.",
            "Bei ihrer Arbeit chia ở Dativ; sau động từ braucht thì cả der Computer và der Schreibtisch đều chia ở Akkusativ (einen Computer und einen großen Schreibtisch).",
            "Trong công việc của mình, Petra cần một chiếc máy tính và một cái bàn làm việc lớn."
        ),
        (
            "Câu 90: Dịch câu sau sang tiếng Đức: 'Người thợ cơ khí sửa chữa ô tô ở trong một xưởng sửa chữa.'",
            ["Der Mechatroniker repariert Autos in einer Werkstatt.", "Der KFZ-Mechatroniker repariert Autos in einer Werkstatt.", "Der Mechatroniker repariert das Auto in einer Werkstatt.", "In einer Werkstatt repariert der KFZ-Mechatroniker Autos."],
            "Der Mechatroniker repariert Autos in einer Werkstatt.",
            "Tân ngữ trực tiếp Autos ở Akkusativ, còn nơi làm việc tĩnh in einer Werkstatt chia ở Dativ.",
            "Người thợ cơ khí sửa chữa ô tô ở trong một xưởng sửa chữa."
        ),
        (
            "Câu 91: Dịch câu sau sang tiếng Đức: 'Lúc 8 giờ 30 phút anh ấy phải đưa con gái vào trường mẫu giáo.'",
            ["Um 8.30 Uhr muss er die Tochter in den Kindergarten bringen.", "Um halb neun muss er die Tochter in den Kindergarten bringen.", "Um 8.30 Uhr muss er seine Tochter in den Kindergarten bringen.", "Er muss um 8.30 Uhr seine Tochter in den Kindergarten bringen."],
            "Um 8.30 Uhr muss er die Tochter in den Kindergarten bringen.",
            "Đưa con gái vào trường mẫu giáo (bringen -> di chuyển Wohin?) dùng Cách 4 (Akkusativ): in den Kindergarten.",
            "Lúc 8 giờ 30 phút anh ấy phải đưa con gái vào trường mẫu giáo."
        ),
        (
            "Câu 92: Dịch câu sau sang tiếng Đức: 'Nữ bác sĩ khám cho các bệnh nhân ở trong bệnh viện.'",
            ["Die Ärztin untersucht Patienten im Krankenhaus.", "Die Ärztin untersucht die Patienten im Krankenhaus.", "Im Krankenhaus untersucht die Ärztin Patienten."],
            "Die Ärztin untersucht Patienten im Krankenhaus.",
            "Nữ bác sĩ là Die Ärztin; khám cho bệnh nhân là untersucht Patienten (Akkusativ); ở trong bệnh viện là im Krankenhaus (Dativ).",
            "Nữ bác sĩ khám cho các bệnh nhân ở trong bệnh viện."
        ),
        (
            "Câu 93: Dịch câu sau sang tiếng Đức: 'Người điều dưỡng giúp đỡ vị bác sĩ mỗi ngày.'",
            ["Der Krankenpfleger hilft dem Arzt jeden Tag.", "Jeden Tag hilft der Krankenpfleger dem Arzt.", "Die Krankenschwester hilft dem Arzt jeden Tag.", "Die Krankenpflegerin hilft dem Arzt jeden Tag."],
            "Der Krankenpfleger hilft dem Arzt jeden Tag.",
            "Động từ helfen biến âm e -> i thành hilft và bắt buộc đi với Cách 3 (Dativ): der Arzt -> dem Arzt.",
            "Người điều dưỡng giúp đỡ vị bác sĩ mỗi ngày."
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
            ["Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo", "Vào lúc 16h30 Paula phải đón con gái từ nhà trẻ về", "Lúc 4 giờ rưỡi chiều Paula phải đón con gái của cô ấy từ trường mầm non", "Lúc 16 giờ 30 Paula phải đón con gái từ trường mẫu giáo", "Lúc 16h30 phút Paula phải đón con gái từ trường mẫu giáo"],
            "Lúc 16 giờ 30 phút Paula phải đón con gái của mình từ trường mẫu giáo",
            "muss ... abholen = phải đón; ihre Tochter = con gái của cô ấy; vom Kindergarten = từ trường mẫu giáo.",
            "Um 16.30 Uhr muss Paula ihre Tochter vom Kindergarten abholen."
        ),
        (
            "Câu 95: Dịch câu sau sang tiếng Việt: 'Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen.'",
            ["Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ", "Nghề của Frank Müller là giáo viên nhưng hôm nay anh ấy được nghỉ lễ và có thể ngủ tới 7 giờ", "Frank Müller là giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ đến 7 giờ", "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ nên có thể ngủ tới 7 giờ"],
            "Frank Müller làm nghề giáo viên nhưng hôm nay anh ấy có kỳ nghỉ và có thể ngủ đến 7 giờ",
            "ist Lehrer von Beruf = làm nghề giáo viên; hat Ferien = có kỳ nghỉ; kann bis 7 Uhr schlafen = có thể ngủ đến 7 giờ.",
            "Frank Müller ist Lehrer von Beruf, aber heute hat er Ferien und kann bis 7 Uhr schlafen."
        ),
        (
            "Câu 96: Dịch câu sau sang tiếng Việt: 'Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen.'",
            ["Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình", "Điện thoại rất quan trọng với cô ấy bởi vì cô ấy phải gọi điện cho khách hàng của mình thường xuyên", "Cái điện thoại rất quan trọng đối với cô ấy vì cô ấy thường phải gọi cho khách hàng", "Chiếc điện thoại rất quan trọng với cô ấy vì cô ấy phải thường xuyên gọi điện cho khách hàng"],
            "Chiếc điện thoại rất quan trọng đối với cô ấy vì cô ấy thường xuyên phải gọi điện cho các khách hàng của mình",
            "wichtig für sie = quan trọng đối với cô ấy; muss ihre Kunden oft anrufen = thường xuyên phải gọi điện cho khách hàng của mình.",
            "Das Telefon ist sehr wichtig für sie, denn sie muss ihre Kunden oft anrufen."
        ),
        (
            "Câu 97: Dịch câu sau sang tiếng Việt: 'Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining.'",
            ["Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá", "Buổi chiều ông Müller đưa xe hơi vào xưởng sửa chữa và sau đó đi tập đá bóng", "Vào buổi chiều anh Müller đem ô tô tới xưởng sửa xe rồi đi tập bóng đá", "Buổi chiều ông Müller mang ô tô vào xưởng sửa chữa rồi đi đến buổi tập bóng đá"],
            "Vào buổi chiều ông Müller mang chiếc ô tô của mình vào xưởng sửa chữa rồi sau đó đi đến buổi tập bóng đá",
            "bringt sein Auto in die Werkstatt = mang ô tô vào xưởng sửa chữa (Akkusativ); geht zum Fußballtraining = đi đến buổi tập bóng đá (Dativ).",
            "Am Nachmittag bringt Herr Müller sein Auto in die Werkstatt und geht dann zum Fußballtraining."
        ),
        (
            "Câu 98: Dịch câu sau sang tiếng Việt: 'Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität.'",
            ["Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học", "Nữ giáo viên dạy học sinh ở một ngôi trường vào buổi sáng và dạy sinh viên tại trường đại học vào buổi chiều", "Buổi sáng cô giáo giảng dạy học sinh ở trường phổ thông và buổi chiều dạy sinh viên ở trường đại học", "Nữ giáo viên buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học"],
            "Cô giáo buổi sáng dạy học sinh tại một trường học và buổi chiều dạy sinh viên ở trường đại học",
            "vormittags = vào buổi sáng; Schüler an einer Schule = học sinh tại một trường học; nachmittags = vào buổi chiều; Studenten an der Universität = sinh viên tại trường đại học.",
            "Die Lehrerin unterrichtet vormittags Schüler an einer Schule und nachmittags Studenten an der Universität."
        ),
        (
            "Câu 99: Dịch câu sau sang tiếng Việt: 'Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat.'",
            ["Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối", "Từ 8 giờ đến 10 giờ tối Paula có thể xem truyền hình trong phòng khách sau khi làm xong bữa tối", "Từ 20 giờ đến 22 giờ Paula có thể xem tivi trong phòng khách sau khi nấu bữa tối", "Từ 20 đến 22 giờ Paula có thể xem tivi ở phòng khách sau khi làm bữa tối"],
            "Từ 20 đến 22 giờ Paula có thể xem tivi ở trong phòng khách sau khi cô ấy đã làm bữa tối",
            "kann ... fernsehen = có thể xem tivi; im Wohnzimmer = ở trong phòng khách; das Abendessen machen = làm bữa tối.",
            "Von 20 bis 22 Uhr kann Paula im Wohnzimmer fernsehen, nachdem sie das Abendessen gemacht hat."
        ),
        (
            "Câu 100: Dịch câu sau sang tiếng Việt: 'Der Friseur schneidet meinem Bruder im Friseursalon die Haare.'",
            ["Người thợ cắt tóc cắt tóc cho anh trai tôi ở trong tiệm làm tóc", "Thợ làm tóc cắt tóc cho anh trai của tôi tại tiệm cắt tóc", "Người thợ làm tóc đang cắt tóc cho anh tôi ở trong salon tóc", "Thợ cắt tóc cắt tóc cho anh trai tôi trong tiệm làm tóc"],
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
                "translation": trans
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
        vocabularies.append((
            lesson_id,
            f"{{item['article']}} {{item['word']}}",
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
