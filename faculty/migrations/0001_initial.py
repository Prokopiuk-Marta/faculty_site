import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("head", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name": "Кафедра",
                "verbose_name_plural": "Кафедри",
            },
        ),
        migrations.CreateModel(
            name="MainPage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("short_text", models.TextField()),
                ("about_text", models.TextField()),
                ("dean", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=300)),
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Головна сторінка",
                "verbose_name_plural": "Головна сторінка",
            },
        ),
        migrations.CreateModel(
            name="Program",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("code", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("coordinator_name", models.CharField(max_length=200)),
                ("coordinator_contact", models.CharField(max_length=200)),
                ("disciplines", models.TextField(blank=True)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="programs",
                        to="faculty.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "Спеціальність",
                "verbose_name_plural": "Спеціальності",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("position", models.CharField(max_length=200)),
                ("degree", models.CharField(blank=True, max_length=200)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teachers",
                        to="faculty.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "Викладач",
                "verbose_name_plural": "Викладачі",
            },
        ),
    ]
