# coding: utf-8

from django import forms
from turismo.grupos.models import Grupo,Roteiro
from django.core.exceptions import ValidationError
from django.forms.widgets import Select,CheckboxSelectMultiple

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        
        widgets = { 'clientes': forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),}

class RoteiroForm(forms.ModelForm):
	class Meta:
		model = Roteiro
		widgets = {
            'descricao': forms.Textarea(attrs={'cols': 200, 'rows': 5}),
        }