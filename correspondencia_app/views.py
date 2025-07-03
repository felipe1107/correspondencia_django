from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# Vistas de Correspondencia de Entrada
@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

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
def entrada_update(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_delete(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'entrada': entrada})

# Vistas de Correspondencia de Salida
@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

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
def salida_update(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm(instance=salida)
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_delete(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'salida': salida})

# Vistas de Gestores
@login_required
def gestor_list(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

@login_required
def gestor_create(request):
    if request.method == 'POST':
        form = GestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_update(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        form = GestorForm(request.POST, instance=gestor)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorForm(instance=gestor)
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_delete(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'gestor': gestor})
