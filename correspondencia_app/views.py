from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

@login_required
def vista_principal(request):
    return render(request, 'inicio.html')

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def lista_entradas(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'entradas/lista_entradas.html', {'entradas': entradas})

@login_required
def lista_salidas(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'salidas/lista_salidas.html', {'salidas': salidas})

@login_required
def lista_gestores(request):
    gestores = Gestor.objects.all()
    return render(request, 'gestores/lista_gestores.html', {'gestores': gestores})
