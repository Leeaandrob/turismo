# coding: utf-8

from django import forms
from turismo.grupos.models import Grupo
from django.core.exceptions import ValidationError
from django.forms.widgets import Select,CheckboxSelectMultiple
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo

        widgets = { 'clientes': forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),}