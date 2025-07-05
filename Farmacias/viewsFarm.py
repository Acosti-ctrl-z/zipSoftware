from django.shortcuts import render, redirect
from .models import Farmacia
from .forms import FarmaciaForm
from Laboratorios.models import Laboratorios
from Medicamentos.models import Medicamento

def registrar_farmacia(request):
    if request.method == 'POST':
        form = FarmaciaForm(request.POST)
        if form.is_valid():
            farmacia = form.save(commit=False)  # Guarda la farmacia sin ManyToMany
            farmacia.save()                     # Ahora sí tiene ID
            form.save_m2m()                     # Guarda la relación con laboratorios
            return redirect('home')  # O la vista que prefieras
    else:
        form = FarmaciaForm()
    
    return render(request, 'registro_farm.html', {'form': form})

def lista_farm(request):
    farmacias = Farmacia.objects.all()
    laboratorios=Laboratorios.objects.all()
    medicamentos=Medicamento.objects.all()
    return render(request, 'lista_farm.html', {'farmacias': farmacias, 'medicamentos':medicamentos,'laboratorios':laboratorios})