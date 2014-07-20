# coding: utf-8

from django import forms
from turismo.clientes.models import Cliente
from django.core.exceptions import ValidationError

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente