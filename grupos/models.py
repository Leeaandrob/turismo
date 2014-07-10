#coding: utf-8
from django.db import models

# Create your models here.

class Grupo(models.Model):
	name = models.CharField(max_length=100)
	destino = models.CharField(max_length=100)
	#destino = models.IntegerField()
