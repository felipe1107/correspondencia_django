from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import EntradaForm, SalidaForm, GestorForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
    return render(request, 'correspondencia_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def entrada_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_update(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_delete(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'entrada': entrada})

@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def salida_create(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = SalidaForm()
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_update(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        form = SalidaForm(request.POST, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = SalidaForm(instance=salida)
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_delete(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'salida': salida})

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
