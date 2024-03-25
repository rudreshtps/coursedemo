# Generated by Django 4.1.13 on 2024-03-19 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('StudentId', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('college_Id', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('whatsApp_No', models.IntegerField()),
                ('mob_No', models.IntegerField()),
                ('sem', models.CharField(max_length=3)),
                ('branch', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=3)),
                ('user_category', models.CharField(max_length=3)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('exp_date', models.DateField()),
                ('score', models.IntegerField()),
                ('progress_Id', models.CharField(max_length=30)),
            ],
        ),
    ]
