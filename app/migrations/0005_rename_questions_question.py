# Generated by Django 4.0.2 on 2022-03-24 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_answer_questions_answer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
