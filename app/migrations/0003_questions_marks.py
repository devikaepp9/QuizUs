# Generated by Django 4.0.2 on 2022-03-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_answer_questions_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='marks',
            field=models.BigIntegerField(default=1, max_length=3),
        ),
    ]
