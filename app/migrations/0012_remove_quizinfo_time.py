# Generated by Django 4.0.2 on 2022-03-27 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_quizinfo_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizinfo',
            name='time',
        ),
    ]
