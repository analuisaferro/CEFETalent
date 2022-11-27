from django.db import models

# Create your models here.

class Recurso(models.Model):
    def __str__(self):
        return '%s' % (self.nome)

    class Meta:
        verbose_name_plural = "Recursos"
        verbose_name = "Recurso"
        ordering = ['nome']

    nome=models.CharField(max_length=64, verbose_name='Nome do recurso')
    descricao=models.TextField(max_length=254, verbose_name='Descrição', blank=True, null=True)
    quantidade=models.IntegerField(verbose_name='Quantidade')
    