# Generated by Django 4.2.17 on 2024-12-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0027_alter_atividade_capacidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividade',
            old_name='categorias',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]
