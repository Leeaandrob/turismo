# coding: utf-8

from django import forms
from turismo.destinos.models import Destino
from django.core.exceptions import ValidationError

from django.contrib import admin


class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino

