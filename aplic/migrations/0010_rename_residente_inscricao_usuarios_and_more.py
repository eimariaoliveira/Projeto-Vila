# Generated by Django 4.2.16 on 2024-11-26 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0009_alter_atividade_capacidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscricao',
            old_name='residente',
            new_name='usuarios',
        ),
        migrations.RenameField(
            model_name='responsavel',
            old_name='residentes',
            new_name='usuarios',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='administrador',
        ),
        migrations.RemoveField(
            model_name='endereco',
            name='responsavel',
        ),
        migrations.AddField(
            model_name='endereco',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='endereco', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atividade',
            name='capacidade',
            field=models.IntegerField(blank=True, help_text='', null=True, verbose_name='Capacidade'),
        ),
    ]
