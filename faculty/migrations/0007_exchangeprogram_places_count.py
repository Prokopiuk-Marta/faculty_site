from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0006_split_university_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="places_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
