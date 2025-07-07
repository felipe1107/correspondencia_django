from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# ----------------- ENTRADAS -----------------
@login_required
def entrada_list(request):
    items = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'items': items})

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
    return render(request, 'correspondencia_app/crear_entrada.html', {'form': form})

@login_required
def eliminar_entrada(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    entrada.delete()
    return redirect('entrada_list')

# ----------------- SALIDAS -----------------
@login_required
def salida_list(request):
    items = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'items': items})

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
    return render(request, 'correspondencia_app/crear_salida.html', {'form': form})

@login_required
def eliminar_salida(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    salida.delete()
    return redirect('salida_list')

# ----------------- GESTORES -----------------
@login_required
def gestor_list(request):
    items = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'items': items})

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
    return render(request, 'correspondencia_app/crear_gestor.html', {'form': form})

@login_required
def eliminar_gestor(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    gestor.delete()
    return redirect('gestor_list')

# ----------------- LOGOUT -----------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
