# Generated by Django 4.0.2 on 2022-04-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_question_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Subject',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
