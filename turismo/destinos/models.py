#coding: utf-8
from django.db import models
from imagekit.models import ImageSpecField
from croppable.fields import CroppableImageField
from croppable.utils import get_crop_processor
# Create your models here.

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    