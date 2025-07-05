from django import forms

class NuevoLaboratorio(forms.Form):
    nombre = forms.CharField(label="ingrese nombre del laboratorio", max_length=200)
    direccion = forms.CharField(label="ingrese la direccion del laboratorio", max_length=200)