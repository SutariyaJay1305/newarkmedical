# Generated by Django 5.0 on 2023-12-16 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patient", "0011_alter_appointment_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="InPatientManagement",
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
                ("bed_number", models.IntegerField()),
                ("scheduled_surgery_room", models.IntegerField(blank=True, null=True)),
                ("scheduled_surgery_date", models.DateField(blank=True, null=True)),
                ("surgery_booked", models.BooleanField(default=False)),
                (
                    "assigned_doctor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.doctor",
                    ),
                ),
                (
                    "patient",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SurgerySchedule",
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
                ("scheduled_date", models.DateField()),
                (
                    "surgeon",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="patient.doctor"
                    ),
                ),
            ],
        ),
    ]