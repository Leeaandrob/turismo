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

def colaborador_edit(request,colaborador_id):
    colaborador = get_object_or_404(Colaborador,id=colaborador_id)
    if request.method == 'POST':
        return edit_colaborador(request,colaborador)
    else:
        return request_grupo(request,cliente)
def edit_colaborador(request,colaborador):
    form = ColaboradorForm(request.POST,instance=colaborador)
    if form.is_valid():
        colaborador = form.save(commit=False)
        colaborador.save()
        return HttpResponseRedirect('/colaboradores/lista')
    else:
        return render(request,'colaborador_editar.html',{'form':form})

def request_colaborador(request,colaborador):
    form = ColaboradorForm(instance=colaborador)
    return render(request,'colaborador_editar.html',{'form':form})