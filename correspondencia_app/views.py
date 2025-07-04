from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm, RegistroUsuarioForm

# Vista de inicio
def home(request):
    return redirect('login')

# LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('entrada_list')
    else:
        form = AuthenticationForm()
    return render(request, 'correspondencia_app/login.html', {'form': form})

# CERRAR SESIÓN
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

# REGISTRO USUARIO (opcional, puedes eliminarla si no se va a usar)
def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'correspondencia_app/registro_usuario.html', {'form': form})

# LISTA DE ENTRADAS
@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

# CREAR ENTRADA
@login_required
def crear_entrada(request):
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, 'correspondencia_app/crear_entrada.html', {'form': form})

# EDITAR ENTRADA
@login_required
def editar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/editar_entrada.html', {'form': form})

# ELIMINAR ENTRADA
@login_required
def eliminar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/eliminar_entrada.html', {'entrada': entrada})

# LISTA DE SALIDAS
@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

# CREAR SALIDA
@login_required
def crear_salida(request):
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm()
    return render(request, 'correspondencia_app/crear_salida.html', {'form': form})

# EDITAR SALIDA
@login_required
def editar_salida(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm(instance=salida)
    return render(request, 'correspondencia_app/editar_salida.html', {'form': form})

# ELIMINAR SALIDA
@login_required
def eliminar_salida(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/eliminar_salida.html', {'salida': salida})

# LISTA DE GESTORES
@login_required
def gestor_list(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

# CREAR GESTOR
@login_required
def crear_gestor(request):
    if request.method == 'POST':
        form = GestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/crear_gestor.html', {'form': form})

# EDITAR GESTOR
@login_required
def editar_gestor(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        form = GestorForm(request.POST, instance=gestor)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorForm(instance=gestor)
    return render(request, 'correspondencia_app/editar_gestor.html', {'form': form})

# ELIMINAR GESTOR
@login_required
def eliminar_gestor(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/eliminar_gestor.html', {'gestor': gestor})
