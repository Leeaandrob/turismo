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


def upload_picture(request):
    profile_pictures = django_settings.MEDIA_ROOT + '/profile_pictures/'
    if not os.path.exists(profile_pictures):
        os.makedirs(profile_pictures)
    f = request.FILES['picture']
    filename = profile_pictures + request.user.username + '_tmp.jpg'
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)    
    im = Image.open(filename)
    width, height = im.size
    if width > 350:
        new_width = 350
        new_height = (height * 350) / width
        new_size = new_width, new_height
        im.thumbnail(new_size, Image.ANTIALIAS)
        im.save(filename)
    return redirect('/colaboradores/?upload_picture=uploaded')

def save_uploaded_picture(request):
    try:
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        w = int(request.POST.get('w'))
        h = int(request.POST.get('h'))
        tmp_filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + request.user.username + '_tmp.jpg'
        filename = django_settings.MEDIA_ROOT + '/profile_pictures/' + request.user.username + '.jpg'
        im = Image.open(tmp_filename)
        cropped_im = im.crop((x, y, w+x, h+y))
        cropped_im.thumbnail((200, 200), Image.ANTIALIAS)
        cropped_im.save(filename)
        os.remove(tmp_filename)
    except Exception, e:
        pass
    return redirect('/colaboradores/')