# Generated by Django 5.1.4 on 2024-12-08 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Review'},
        ),
    ]