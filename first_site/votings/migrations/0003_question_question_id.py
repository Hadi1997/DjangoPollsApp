# Generated by Django 2.1.4 on 2018-12-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votings', '0002_auto_20181210_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_id',
            field=models.IntegerField(default=0),
        ),
    ]
