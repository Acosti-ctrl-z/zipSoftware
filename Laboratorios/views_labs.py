from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NuevoLaboratorio
from.models import Laboratorios

# Create your views here.
def labs(request):
    laboratorio= Laboratorios.objects.all()
    return render(request, 'labs.html', {
        'laboratorio': laboratorio
    })

def crear_labs(request):
    if request.method == 'GET':
        return render(request, 'crear_labs.html', {
                'form': NuevoLaboratorio()
            })
    else:
            Laboratorios.objects.create(nombre=request.POST['nombre'], direccion=request.POST['direccion'])
            return redirect('/labs/')
    