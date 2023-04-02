# Generated by Django 4.1.7 on 2023-03-28 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_remove_doctor_schedule_schedule_doctor'),
        ('patient', '0008_alter_patientrecord_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientrecord',
            name='appointment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patientrecord',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.doctor'),
        ),
    ]
