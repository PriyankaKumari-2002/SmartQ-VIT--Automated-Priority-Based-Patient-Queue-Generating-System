# Generated by Django 4.1.7 on 2023-03-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_alter_patienthistory_patient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrecord',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
