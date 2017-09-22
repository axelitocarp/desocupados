from django.shortcuts import render
from .models import Persona
# Create your views here.


def lista(request):
    return render(request, 'lalista.html')

def lista_personas(request):
        persvar = Persona.objects.all()
        return render(request, 'lista_pers.html', {'persona' : persvar})
