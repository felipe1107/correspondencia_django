from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, GestorCorrespondencia
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorCorrespondenciaForm

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def gestor_list(request):
    gestores = GestorCorrespondencia.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

@login_required
def entrada_create(request):
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def salida_create(request):
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm()
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def gestor_create(request):
    if request.method == 'POST':
        form = GestorCorrespondenciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorCorrespondenciaForm()
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})
