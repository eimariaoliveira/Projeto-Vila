# Generated by Django 4.2.16 on 2024-11-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0021_alter_atividade_capacidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]