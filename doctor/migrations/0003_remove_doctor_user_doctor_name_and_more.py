# Generated by Django 5.1.4 on 2024-12-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_availabletime_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='user',
        ),
        migrations.AddField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='available_time',
            field=models.ManyToManyField(null=True, to='doctor.availabletime'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='designation',
            field=models.ManyToManyField(null=True, to='doctor.designation'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(null=True, upload_to='doctor/images/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='meet_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ManyToManyField(null=True, to='doctor.specialization'),
        ),
    ]