# Generated by Django 5.0 on 2023-12-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patient", "0011_alter_appointment_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Nurse",
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
                ("name", models.CharField(max_length=100)),
                ("contact_number", models.CharField(max_length=20)),
                ("specialization", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("shift_time", models.TimeField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
