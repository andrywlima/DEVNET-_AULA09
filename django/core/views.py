from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Objeto


def index(request):
    objetos = Objeto.objects.all()

    context = {
        'objetos': objetos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def objeto(request, pk):
    # obj = Objeto.objects.get(id=pk)
    obj = get_object_or_404(Objeto, id=pk)
    context = {
        'objeto': obj
    }
    return render(request, 'objeto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def erro500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
