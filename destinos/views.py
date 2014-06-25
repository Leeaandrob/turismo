#coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import DestinoForm
from .models import Destino
# Create your views here.

def destino_create(request):
	return render(request,'destino_novo.html')

def destino_create(request):
	'''
		@create_grupo: POST Usado para recebimento de dados e criação do usuario caso tudo esteja correto
	'''
	form = DestinoForm(request.POST)
	if not form.is_valid():
		return render(request, 'destino_novo.html',
			{'form': form})
	obj = form.save()
	return HttpResponseRedirect("/destinos/lista/")

def destino_lista(request):
	return render(request, 'destino_lista.html',{'destinos':Destino.objects.all()})

def destino_edit(request):
	"""destino = get_object_or_404(Destino,id=destino_id) """
	return render(request,'destino_editar.html')
