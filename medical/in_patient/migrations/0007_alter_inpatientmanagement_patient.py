# Generated by Django 5.0 on 2023-12-17 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("in_patient", "0006_inpatientmanagement_bed_booked_date_and_more"),
        ("patient", "0012_nurse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inpatientmanagement",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="patient.patient"
            ),
        ),
    ]