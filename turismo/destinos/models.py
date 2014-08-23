#coding: utf-8
from django.db import models
from imagekit.models import ImageSpecField
# Create your models here.

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    
    def __unicode__(self):
        return unicode(self.nome)