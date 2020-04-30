from django.shortcuts import render
from pet.models import Pet


def index(request):
    ListPets = Pet.objects.all()
    context = {
    'pets': ListPets

    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
