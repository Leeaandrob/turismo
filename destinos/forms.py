# coding: utf-8

from django import forms
from destinos.models import Destino
from django.core.exceptions import ValidationError

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino