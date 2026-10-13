from django.db import migrations


def text_to_number(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        digits = ""
        for char in program.places:
            if char.isdigit():
                digits = digits + char

        if digits == "":
            program.places_count = 0
        else:
            program.places_count = int(digits)
        program.save(update_fields=["places_count"])


def number_to_text(apps, schema_editor):
    ExchangeProgram = apps.get_model("faculty", "ExchangeProgram")
    for program in ExchangeProgram.objects.all():
        program.places = str(program.places_count)
        program.save(update_fields=["places"])


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0007_exchangeprogram_places_count"),
    ]

    operations = [
        migrations.RunPython(text_to_number, reverse_code=number_to_text),
    ]
