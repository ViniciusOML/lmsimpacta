# Generated by Django 2.1.7 on 2019-05-21 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0012_auto_20190520_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='semestres',
            field=models.IntegerField(default=4, verbose_name='Semestre'),
        ),
        migrations.AlterField(
            model_name='matrizcurricular',
            name='semestres',
            field=models.IntegerField(default=4, verbose_name='Semestre'),
        ),
    ]
