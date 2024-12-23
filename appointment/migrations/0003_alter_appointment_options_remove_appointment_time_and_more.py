# Generated by Django 5.1.4 on 2024-12-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_alter_appointment_cancel'),
        ('doctor', '0006_alter_review_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name_plural': 'Appoinment'},
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.ManyToManyField(to='doctor.availabletime'),
        ),
    ]
