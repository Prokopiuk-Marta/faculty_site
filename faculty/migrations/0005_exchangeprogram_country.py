from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faculty", "0004_add_exchange_programs"),
    ]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(db_index=True, default="", max_length=100),
        ),
    ]
