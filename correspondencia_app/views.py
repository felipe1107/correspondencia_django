from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import EntradaForm, SalidaForm, GestorForm

@login_required
def inicio(request):
    return render(request, 'dashboard.html')

# ENTRADAS
@login_required
def lista_entradas(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'entradas/lista_entradas.html', {'entradas': entradas})

# SALIDAS
@login_required
def lista_salidas(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'salidas/lista_salidas.html', {'salidas': salidas})

# GESTORES
@login_required
def lista_gestores(request):
    gestores = Gestor.objects.all()
    return render(request, 'gestores/lista_gestores.html', {'gestores': gestores})
