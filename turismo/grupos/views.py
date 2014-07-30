#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from turismo.grupos.forms import GrupoForm
from turismo.grupos.models import Grupo
from django.core.urlresolvers import reverse as r

from turismo.clientes.models import Cliente
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
    return render(request, 'grupo_editar.html',
        {'form':form,'grupo':grupo,
        'clientes_dentro':grupo.clientes.all(),
        'clientes_fora':Cliente.objects.all().exclude(id__in=grupo.clientes.all())})

def inserir_ao_grupo(request,grupo_id,cliente_id):
    cliente = get_object_or_404(Cliente,id=cliente_id)
    grupo = get_object_or_404(Grupo,id=grupo_id)
    grupo.clientes.add(cliente)
    return HttpResponseRedirect(r('grupos:grupo_edit', args=[grupo.id]))
    #return HttpResponseRedirect(r('grupos:pessoas_grupo', args=[grupo.id]))

def remover_do_grupo(request,grupo_id,cliente_id):
    cliente = get_object_or_404(Cliente,id=cliente_id)
    grupo = get_object_or_404(Grupo,id=grupo_id)
    grupo.clientes.remove(cliente)
    return HttpResponseRedirect(r('grupos:grupo_edit', args=[grupo.id]))
    #return HttpResponseRedirect(r('grupos:pessoas_grupo', args=[grupo.id]))



def add_grupo(request):
    if request.is_ajax() and request.POST :
        # do some stuff        
        grupo = Grupo.objects.get(id=request.POST['grupo_id'])
        cliente = Cliente.objects.get(id=request.POST['cliente_id'])
        grupo.clientes.add(cliente)
        form = GrupoForm(instance=grupo)
        return render(request, 'pessoas.html',
            {'form':form,'grupo':grupo,
            'clientes_dentro':grupo.clientes.all(),
            'clientes_fora':Cliente.objects.all().exclude(id__in=grupo.clientes.all())})
    else:
        raise Http404r('grupos:grupo_edit', args=[grupo.id])
def rm_grupo(request):
    if request.is_ajax() and request.POST :
        # do some stuff        
        grupo = Grupo.objects.get(id=request.POST['grupo_id'])
        cliente = Cliente.objects.get(id=request.POST['cliente_id'])
        grupo.clientes.remove(cliente)
        
        form = GrupoForm(instance=grupo)
        return render(request, 'pessoas.html',
            {'form':form,'grupo':grupo,
            'clientes_dentro':grupo.clientes.all(),
            'clientes_fora':Cliente.objects.all().exclude(id__in=grupo.clientes.all())})
    else:
        raise Http404




def clientes_grupo(request,grupo_id):
    grupo = get_object_or_404(Grupo,id=grupo_id)
    return render(request, 'pessoas.html',
        {'grupo':grupo,
        'clientes_dentro':grupo.clientes.all(),
        'clientes_fora':Cliente.objects.all().exclude(id__in=grupo.clientes.all())})