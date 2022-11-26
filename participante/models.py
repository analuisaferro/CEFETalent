from django.db import models

from organizacao.models import Recurso

# Create your models here.


class Participante(models.Model):
    def __str__(self):
        return '%s - %s' % (self.nome, self.matricula)

    class Meta:
        verbose_name_plural = "Participantes"
        verbose_name = "Participante"
        ordering = ['nome']

    nome = models.CharField(max_length=64, verbose_name='Nome Completo')
    matricula = models.CharField(
        max_length=13, verbose_name='Matrícula do Estudante', unique=True)
    email = models.CharField(max_length=254, verbose_name="Email", unique=True)
    celular = models.CharField(
        max_length=14, verbose_name='Número de celular')


class Tipo_Atividade(models.Model):
    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        verbose_name_plural = "Tipos de atividade"
        verbose_name = "Tipo de atividade"
        ordering = ['nome']

    nome = models.CharField(max_length=64, verbose_name='Tipo de atividade')


class Formato_Atividade(models.Model):
    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        verbose_name_plural = "Formatos de atividade"
        verbose_name = "Formato de atividade"
        ordering = ['nome']

    nome = models.CharField(max_length=64, verbose_name='Formato da atividade')


class Atividade(models.Model):

    def __str__(self):
        return '%s' % (self.titulo)

    class Meta:
        verbose_name_plural = "Atividades"
        verbose_name = "Atividade"
        ordering = ['titulo']

    titulo = models.CharField(
        max_length=64, verbose_name='Título da atividade', unique=True)
    descricao = models.TextField(
        max_length=512, verbose_name='Descrição da apresentação')
    duracao = models.IntegerField(
        verbose_name='Duração em minutos')
    tipos_atividade = models.ManyToManyField(Tipo_Atividade)
    formato_atividade = models.ForeignKey(
        Formato_Atividade, on_delete=models.PROTECT)
    recursos = models.ManyToManyField(Recurso)
    participantes = models.ManyToManyField(Participante)
