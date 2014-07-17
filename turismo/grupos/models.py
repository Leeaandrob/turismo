#coding: utf-8
from django.db import models
from turismo.destinos.models import Destino
# Create your models here.

class Grupo(models.Model):
	name = models.CharField(max_length=100)
	destino = models.ForeignKey(Destino)
