# Generated by Django 3.1 on 2021-05-18 23:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Patient', '0003_auto_20210518_2318'),
        ('Doctors', '0002_auto_20210515_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(blank=True, max_length=450, null=True)),
                ('Diagonis', models.CharField(max_length=50)),
                ('billing', models.PositiveIntegerField(blank=True, null=True)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ManyToManyField(related_name='prescrip', to='Patient.Patientsprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MedicialRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Name', models.CharField(blank=True, max_length=450, null=True)),
                ('Description', models.CharField(max_length=50)),
                ('Attachment', models.FileField(blank=True, null=True, upload_to='files')),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ManyToManyField(related_name='records', to='Patient.Patientsprofile')),
            ],
        ),
    ]