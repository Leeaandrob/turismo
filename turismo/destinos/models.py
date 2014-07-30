#coding: utf-8
from django.db import models
from imagekit.models import ImageSpecField
from croppable.fields import CroppableImageField
from croppable.utils import get_crop_processor
# Create your models here.

class Destino(models.Model):
    nome = models.CharField(max_length=100)
    #my_image = CroppableImageField(invalidate_on_save=['my_image_cropped'], upload_to='my_image_folder', blank=True)
    #my_image_cropped = ImageSpecField(get_crop_processor(image_field='my_image'))
    
    def __unicode__(self):
        return unicode(self.nome)