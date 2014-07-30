#coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from turismo.destinos.forms import DestinoForm
from turismo.destinos.models import Destino
# Create your views here.

#def destino_create(request):
#	return render(request,'destino_novo.html')

def destino_create(request):
	form = DestinoForm(request.POST)
	if not form.is_valid():
		return render(request, 'destino_novo.html',{'form': form})
	obj = form.save()
	return HttpResponseRedirect("/destinos/lista/")

def destino_lista(request):
	return render(request, 'destino_lista.html',{'destinos':Destino.objects.all()})


def destino_edit(request,destino_id):

    destino = get_object_or_404(Destino,id=destino_id)
    if request.method == 'POST':
        return edit_destino(request,destino)
    else:
        return request_destino(request,destino)

def edit_destino(request,destino):
    '''
        @edit_funcao: View para alterar os dados de um funcao
    '''
    form = DestinoForm(request.POST,instance=destino)
    if form.is_valid():
        destino = form.save(commit=False)
        destino.save()
        return HttpResponseRedirect('/destinos/lista')
    else:
        return render(request,'destino_editar.html',{'form':form})

def request_destino(request,destino):
    '''
        @request_funcao: View para obter os dados de um determinado funcao
    '''
    form = DestinoForm(instance=destino)
    return render(request, 'destino_editar.html', {'form': form})




	

