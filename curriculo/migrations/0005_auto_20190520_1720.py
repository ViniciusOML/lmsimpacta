# Generated by Django 2.1.7 on 2019-05-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0004_auto_20190520_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='semestre',
            field=models.IntegerField(default=4),
        ),
    ]