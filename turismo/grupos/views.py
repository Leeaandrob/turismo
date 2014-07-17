#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from turismo.grupos.forms import GrupoForm
from turismo.grupos.models import Grupo
from turismo.destinos.models import Destino
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
