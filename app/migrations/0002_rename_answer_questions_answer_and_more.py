# Generated by Django 4.0.2 on 2022-03-12 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='answer',
            new_name='Answer',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='quiznameques',
            new_name='Quiz_Name',
        ),
    ]