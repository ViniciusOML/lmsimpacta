# Generated by Django 2.1.7 on 2019-05-21 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0006_auto_20190520_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='semestre',
            new_name='semestres',
        ),
    ]