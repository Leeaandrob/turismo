#coding: utf-8
from django.db import models

# Create your models here.

class Destino(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return unicode(self.name)