# Generated by Django 5.1.2 on 2024-10-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_alter_atividade_capacidade_alter_responsavel_celular_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsavel',
            name='administador',
        ),
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]
