# correspondencia_app/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def entrada_create(request):
    form = CorrespondenciaEntradaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_edit(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    form = CorrespondenciaEntradaForm(request.POST or None, request.FILES or None, instance=entrada)
    if form.is_valid():
        form.save()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def salida_create(request):
    form = CorrespondenciaSalidaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_edit(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    form = CorrespondenciaSalidaForm(request.POST or None, request.FILES or None, instance=salida)
    if form.is_valid():
        form.save()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def gestor_list(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

@login_required
def gestor_create(request):
    form = GestorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_edit(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    form = GestorForm(request.POST or None, instance=gestor)
    if form.is_valid():
        form.save()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})
