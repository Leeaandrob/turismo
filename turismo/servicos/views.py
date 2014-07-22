#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from turismo.servicos.forms import ServicoForm
from turismo.servicos.models import Servico

# Create your views here.

def servico_create(request):
    return render(request,'servico_novo.html')

def servico_create(request):
    form = ServicoForm(request.POST)
    if not form.is_valid():
        return render(request, 'servico_novo.html',{'form':form})
    obj = form.save()
    return HttpResponseRedirect("/servicos/lista/")

def servico_lista(request):
    return render(request, 'servico_lista.html',{'servicos':Servico.objects.all()})