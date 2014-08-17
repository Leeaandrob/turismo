#coding: utf-8
from django.db import models
from turismo.destinos.models import Destino
from turismo.clientes.models import Cliente
from turismo.colaboradores.models import Colaborador
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
    colaboradores = models.ManyToManyField(Colaborador,verbose_name="Colaboradores", blank=True)

class Roteiro(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    grupo = models.ForeignKey(Grupo)

