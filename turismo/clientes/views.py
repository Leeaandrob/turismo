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

def cliente_edit(request,cliente_id):
    cliente = get_object_or_404(Cliente,id=cliente_id)
    if request.method == 'POST':
        return edit_grupo(request,cliente)
    else:
        return request_grupo(request,cliente)
def edit_grupo(request,cliente):
    form = ClienteForm(request.POST,instance=cliente)
    if form.is_valid():
        cliente = form.save(commit=False)
        cliente.save()
        return HttpResponseRedirect('/clientes/lista')
    else:
        return render(request,'cliente_editar.html',{'form':form})

def request_grupo(request,cliente):
    form = ClienteForm(instance=cliente)
    return render(request,'cliente_editar.html',{'form':form})