from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Entrada, Salida, Gestor
from .forms import EntradaForm, SalidaForm
from django.contrib import messages

@login_required
def inicio(request):
    return render(request, 'dashboard.html')

@login_required
def lista_gestores(request):
    gestores = Gestor.objects.all()
    return render(request, 'gestores/lista_gestores.html', {'gestores': gestores})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def lista_entradas(request):
    entradas = Entrada.objects.all()
    return render(request, 'entradas/lista_entradas.html', {'entradas': entradas})

@login_required
def nueva_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = EntradaForm()
    return render(request, 'entradas/nueva_entrada.html', {'form': form})

@login_required
def eliminar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    entrada.delete()
    return redirect('lista_entradas')
