#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from turismo.clientes.forms import ClienteForm
from turismo.clientes.models import Cliente

# Create your views here.

def cliente_create(request):
    return render(request,'cliente_novo.html')

def cliente_create(request):
    form = ClienteForm(request.POST)
    if not form.is_valid():
        return render(request, 'cliente_novo.html',{'form':form})
    obj = form.save()
    return HttpResponseRedirect("/clientes/lista/")

def cliente_lista(request):
    return render(request, 'cliente_lista.html',{'clientes':Cliente.objects.all()})

def cliente_edit(request):
    pass