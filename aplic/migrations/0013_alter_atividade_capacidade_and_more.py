# Generated by Django 5.1.2 on 2024-10-09 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0012_alter_atividade_capacidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='responsavel',
            name='residentes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplic.residente'),
        ),
    ]
