from django.db import models

# Create your models here.

class Recurso(models.Model):
    nome=models.CharField(max_length=64, verbose_name='Nome do recurso')
    descricao=models.CharField(max_length=254, verbose_name='Descrição')
    quantidade=models.IntegerField(max_length=4, verbose_name='Quantidade')
    