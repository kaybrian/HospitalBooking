# Generated by Django 3.1 on 2021-05-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_doctorprofile_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientprofile',
            name='Gender',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
