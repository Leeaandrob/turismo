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


def servico_edit(request,servico_id):

    servico = get_object_or_404(Destino,id=servico_id)
    if request.method == 'POST':
        return edit_servico(request,servico)
    else:
        return request_servico(request,servico)

def edit_servico(request,servico):
    '''
        @edit_funcao: View para alterar os dados de um funcao
    '''
    form = ServicoForm(request.POST,instance=servico)
    if form.is_valid():
        servico = form.save(commit=False)
        servico.save()
        return HttpResponseRedirect('/servicos/lista')
    else:
        return render(request,'servico_editar.html',{'form':form})

def request_servico(request,servico):
    '''
        @request_funcao: View para obter os dados de um determinado funcao
    '''
    form = ServicoForm(instance=servico)
    return render(request, 'servico_editar.html', {'form': form})