# Generated by Django 3.2.16 on 2022-11-26 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0002_auto_20221126_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividade',
            old_name='tipo_atividade',
            new_name='tipos_atividade',
        ),
    ]
