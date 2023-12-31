# Generated by Django 5.0 on 2023-12-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("in_patient", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rooms",
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
                ("room_number", models.IntegerField()),
                ("bed_number_1", models.BooleanField(default=False)),
                ("bed_number_2", models.BooleanField(default=False)),
                (
                    "room_type",
                    models.CharField(
                        choices=[("Shared", "Shared"), ("Private", "Private")],
                        max_length=10,
                    ),
                ),
                ("is_available", models.BooleanField(default=True)),
            ],
        ),
    ]
