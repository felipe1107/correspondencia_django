from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm

@login_required
def vista_principal(request):
    return render(request, 'inicio.html')

@login_required
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'correspondencia_app/lista_usuarios.html', {'usuarios': usuarios})

@login_required
def lista_entradas(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/lista_entradas.html', {'entradas': entradas})

@login_required
def lista_salidas(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/lista_salidas.html', {'salidas': salidas})

@login_required
def lista_gestores(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/lista_gestores.html', {'gestores': gestores})

@login_required
def crear_entrada(request):
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, 'correspondencia_app/formulario_entrada.html', {'form': form})

@login_required
def editar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = CorrespondenciaEntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/formulario_entrada.html', {'form': form})
@login_required
def eliminar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('lista_entradas')
    return render(request, 'correspondencia_app/confirmar_eliminar_entrada.html', {'entrada': entrada})
