# Generated by Django 2.1.7 on 2019-05-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0009_curso_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='semestres',
            new_name='semestre1',
        ),
        migrations.RenameField(
            model_name='matrizcurricular',
            old_name='semestre',
            new_name='semestres',
        ),
        migrations.AddField(
            model_name='curso',
            name='semestre2',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='curso',
            name='semestre3',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='curso',
            name='semestre4',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descricao',
            field=models.TextField(blank=True, max_length=255, verbose_name='Descrição'),
        ),
    ]
