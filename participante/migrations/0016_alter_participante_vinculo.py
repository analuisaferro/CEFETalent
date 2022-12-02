# Generated by Django 4.1.3 on 2022-12-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participante', '0015_participante_vinculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='vinculo',
            field=models.CharField(choices=[('i', 'Interno: Estudantes e funcionários'), ('e', 'Externo: Convidados e outros')], max_length=1, null=True, verbose_name='Vínculo institucional'),
        ),
    ]