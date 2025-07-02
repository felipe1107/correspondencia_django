# correspondencia_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida
from .forms import GestorForm, EntradaForm, SalidaForm
from django.db.models import Q

# Vista Login
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'correspondencia_app/login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'correspondencia_app/login.html')

# Vista Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Vista Principal
@login_required
def inicio(request):
    return render(request, 'correspondencia_app/inicio.html')

# GESTORES
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
            return redirect('gestor_lista')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_delete(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        return redirect('gestor_lista')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'gestor': gestor})

# ENTRADAS
@login_required
def entrada_list(request):
    query = request.GET.get('q')
    entradas = CorrespondenciaEntrada.objects.all()
    if query:
        entradas = entradas.filter(
            Q(numero_documento__icontains=query) |
            Q(asunto__icontains=query) |
            Q(gestor__nombre__icontains=query)
        )
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def entrada_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entrada_lista')
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_delete(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada_lista')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'entrada': entrada})

# SALIDAS
@login_required
def salida_list(request):
    query = request.GET.get('q')
    salidas = CorrespondenciaSalida.objects.all()
    if query:
        salidas = salidas.filter(
            Q(numero_documento__icontains=query) |
            Q(asunto__icontains=query) |
            Q(destinatario__icontains=query)
        )
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def salida_create(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salida_lista')
    else:
        form = SalidaForm()
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_delete(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida_lista')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'salida': salida})
