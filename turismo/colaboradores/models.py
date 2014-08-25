#coding: utf-8
from django.db import models
from turismo.destinos.models import Destino
from turismo.servicos.models import Servico
# Create your models here.

PESSOA = (
        ('J', 'Pessoa Jurídica'),
        ('F', 'Física'),
        )

class Colaborador(models.Model):
	nome = models.CharField(max_length=100)
	destino = models.ForeignKey(Destino)
	telefone = models.CharField(max_length=15)
	telefone2 = models.CharField(max_length=15,blank=True)
	email = models.CharField(max_length=30,blank=True)
	site = models.CharField(max_length=30,blank=True)
	servicos = models.ManyToManyField(Servico,verbose_name="Serviços")
	observacao = models.CharField(max_length=100,blank=True)
	def __unicode__(self):
	    return unicode(self.nome)