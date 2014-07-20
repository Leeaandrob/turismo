#coding: utf-8
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=10)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    orgao = models.CharField(max_length=20)
    endereco = models.CharField(max_length=30)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    tel01 = models.CharField(max_length=10)
    tel02 = models.CharField(max_length=10)
    email = models.EmailField(max_length=25)