# Generated by Django 4.1.13 on 2024-03-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userdetails_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='certificate',
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='progress_Id',
            field=models.JSONField(default=dict),
        ),
    ]
