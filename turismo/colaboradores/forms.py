# coding: utf-8

from django import forms
from turismo.colaboradores.models import Colaborador
from django.core.exceptions import ValidationError

class ColaboradorForm(forms.ModelForm):
    class Meta:
        model = Colaborador
        widgets = { 'servicos': forms.CheckboxSelectMultiple(attrs={'class':'form-inline'}),}