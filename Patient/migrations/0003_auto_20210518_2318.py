# Generated by Django 3.1 on 2021-05-18 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_patientsprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientsprofile',
            old_name='patient',
            new_name='patientname',
        ),
    ]