# Generated by Django 2.1.7 on 2019-05-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0011_auto_20190520_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrizcurricular',
            name='semestres',
            field=models.IntegerField(default=4),
        ),
    ]
