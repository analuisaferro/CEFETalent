from django.db import models

from organizacao.models import Recurso

# Create your models here.

class Participante(models.Model):
    nome=models.CharField(max_length=64, verbose_name='Nome Completo')
    matricula=models.CharField(max_length=13, verbose_name='Matrícula do Estudante')
    email=models.CharField(max_length=254, verbose_name="Email", blank=True)
    celular=models.CharField(max_length=14, verbose_name='Número de celular', blank=True)
    

class Atividade(models.Model):
    titulo=models.CharField(max_length=64, verbose_name='Título da atividade')
    descricao=models.TextField(max_length=512, verbose_name='Descrição da apresentação')
    duracao=models.IntegerField(max_length=4, verbose_name='Duração em minutos')
    recursos=models.ManyToManyField(Recurso, on_delete=models.PROTECT)
    participantes=models.ManyToManyField(Participante, on_delete=models.PROTECT)

class Tipo_Atividade(models.Model):
    nome=models.CharField(max_length=64, verbose_name='Tipo de atividade')

class Formato_Atividade(models.Model):
    nome=models.CharField(max_length=64, verbose_name='Formato da atividade')