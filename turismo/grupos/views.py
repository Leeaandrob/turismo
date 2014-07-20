#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from turismo.grupos.forms import GrupoForm
from turismo.grupos.models import Grupo
# Create your views here.

def grupo_create(request):
	return render(request,'grupo_novo.html')

def grupo_create(request):

	form = GrupoForm(request.POST)
	if not form.is_valid():
		return render(request, 'grupo_novo.html', {'form': form})
	obj = form.save()
	return HttpResponseRedirect("/grupos/lista/")

def grupo_lista(request):
	return render(request, 'grupo_lista.html',{'grupos':Grupo.objects.all()})



def grupo_edit(request,grupo_id):

    grupo = get_object_or_404(Grupo,id=grupo_id)
    if request.method == 'POST':
        return edit_grupo(request,grupo)
    else:
        return request_grupo(request,grupo)

def edit_grupo(request,grupo):
    '''
        @edit_funcao: View para alterar os dados de um funcao
    '''
    form = GrupoForm(request.POST,instance=grupo)
    if form.is_valid():
        grupo = form.save(commit=False)
        grupo.save()
        return HttpResponseRedirect('/grupos/lista')
    else:
        return render(request,'grupo_editar.html',{'form':form})

def request_grupo(request,grupo):
    '''
        @request_funcao: View para obter os dados de um determinado funcao
    '''
    form = GrupoForm(instance=grupo)
    return render(request, 'grupo_editar.html', {'form': form})