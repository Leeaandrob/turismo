# coding: utf-8

from django import forms
from turismo.servicos.models import Servico
from django.core.exceptions import ValidationError

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico