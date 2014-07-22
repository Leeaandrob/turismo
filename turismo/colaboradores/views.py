#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from turismo.colaboradores.forms import ColaboradorForm
from turismo.colaboradores.models import Colaborador

# Create your views here.

def colaborador_create(request):
    return render(request,'colaborador_novo.html')

def colaborador_create(request):
    form = ColaboradorForm(request.POST)
    if not form.is_valid():
        return render(request, 'colaborador_novo.html',{'form':form})
    obj = form.save()
    return HttpResponseRedirect("/colaboradores/lista/")

def colaborador_lista(request):
    return render(request, 'colaborador_lista.html',{'colaboradores':Colaborador.objects.all()})