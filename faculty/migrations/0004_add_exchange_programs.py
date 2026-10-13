from django.db import migrations

ADD_PROGRAMS_SQL = """
INSERT INTO faculty_exchangeprogram (university, languages, places, deadline, description)
VALUES
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
 'Найбільший університет Польщі. Студенти факультету можуть провести семестр на факультетах біології, хімії або фізики.'),
('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
 'Один з найстаріших університетів Європи (заснований у 1425 році) з сильними програмами з біоінженерії та хімії.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
 'Найстаріший університет Литви. Для студентів-природничників є курси англійською з біохімії та екології.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
 'Ягеллонський університет у Кракові, один з найстаріших у Центральній Європі. Обмін доступний для студентів-біологів і хіміків.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
 'Провідний університет Естонії з сильною школою екології та молекулярної біології. Більшість курсів для обміну викладаються англійською.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
 'Університет у Брно з великим кампусом природничих наук. Підходить студентам, які цікавляться біохімією та екологією.');
"""

DELETE_PROGRAMS_SQL = """
DELETE FROM faculty_exchangeprogram
WHERE university LIKE 'Uniwersytet Warszawski%'
   OR university LIKE 'KU Leuven%'
   OR university LIKE 'Vilnius University%'
   OR university LIKE 'Uniwersytet Jagielloński%'
   OR university LIKE 'University of Tartu%'
   OR university LIKE 'Masaryk University%';
"""


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0003_exchangeprogram"),
    ]

    operations = [
        migrations.RunSQL(ADD_PROGRAMS_SQL, reverse_sql=DELETE_PROGRAMS_SQL),
    ]
