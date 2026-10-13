from django.db import migrations


def split_university(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        text = program.university
        name = text
        country = ""

        if "(" in text:
            parts = text.split("(")
            name = parts[0]
            country = parts[1].replace(")", "")
        elif " - " in text:
            parts = text.split(" - ")
            name = parts[0]
            country = parts[1]
        elif "," in text:
            parts = text.split(",")
            name = parts[0]
            country = parts[1]

        program.university = name.strip()
        program.country = country.strip()
        program.save(update_fields=["university", "country"])


def join_university(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        if program.country != "":
            program.university = program.university + ", " + program.country
            program.save(update_fields=["university"])


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0005_exchangeprogram_country"),
    ]

    operations = [
        migrations.RunPython(split_university, reverse_code=join_university),
    ]
