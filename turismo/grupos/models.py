#coding: utf-8
from django.db import models
from turismo.destinos.models import Destino
from turismo.clientes.models import Cliente
# Create your models here.


SITUACAO = (
        ('A', 'Em Aberto'),
        ('B', 'Concluído'),
        ('C', 'Cancelado'),
        )

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    destino = models.ForeignKey(Destino)
    partida = models.CharField(max_length=10)
    chegada = models.CharField(max_length=10)
    numpessoas = models.CharField(max_length=3)
    situacao = models.CharField(max_length=1,choices=SITUACAO)
    clientes = models.ManyToManyField(Cliente,verbose_name="Pessoas Listadas", blank=True)

