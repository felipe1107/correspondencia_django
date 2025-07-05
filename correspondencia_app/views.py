from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import EntradaForm, SalidaForm
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor, Usuario

# -------------------- AUTENTICACIÓN --------------------

def login_view(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def inicio(request):
    return render(request, 'dashboard.html')


# -------------------- USUARIOS --------------------
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'correspondencia_app/usuario_list.html', {'usuarios': usuarios})


# -------------------- ENTRADAS --------------------
@login_required
def lista_entradas(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/lista_entradas.html', {'entradas': entradas})

@login_required
def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/crear_entrada.html', {'form': form})

@login_required
def editar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/crear_entrada.html', {'form': form})

@login_required
def eliminar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('lista_entradas')
    return render(request, 'correspondencia_app/eliminar_entrada.html', {'entrada': entrada})


# -------------------- SALIDAS --------------------
@login_required
def lista_salidas(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/lista_salidas.html', {'salidas': salidas})

@login_required
def crear_salida(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_salidas')
    else:
        form = SalidaForm()
    return render(request, 'correspondencia_app/crear_salida.html', {'form': form})

@login_required
def editar_salida(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('lista_salidas')
    else:
        form = SalidaForm(instance=salida)
    return render(request, 'correspondencia_app/crear_salida.html', {'form': form})

@login_required
def eliminar_salida(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        salida.delete()
        return redirect('lista_salidas')
    return render(request, 'correspondencia_app/eliminar_salida.html', {'salida': salida})


# -------------------- GESTORES --------------------
@login_required
def lista_gestores(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/lista_gestores.html', {'gestores': gestores})
