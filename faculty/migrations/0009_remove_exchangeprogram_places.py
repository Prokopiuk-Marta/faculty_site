from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("faculty", "0008_convert_places_to_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exchangeprogram",
            name="places",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.RemoveField(
            model_name="exchangeprogram",
            name="places",
        ),
    ]
