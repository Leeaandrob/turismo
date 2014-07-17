# coding: utf-8

from django import forms
from turismo.grupos.models import Grupo
from django.core.exceptions import ValidationError

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo