# Generated by Django 4.1.13 on 2024-03-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('courseId', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=500)),
            ],
        ),
    ]
