from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import EntradaForm, SalidaForm, GestorForm

# --- Autenticación ---
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'correspondencia_app/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'correspondencia_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# --- Dashboard ---
@login_required
def dashboard(request):
    entradas = CorrespondenciaEntrada.objects.count()
    salidas = CorrespondenciaSalida.objects.count()
    gestores = Gestor.objects.count()
    return render(request, 'correspondencia_app/dashboard.html', {
        'entradas_count': entradas,
        'salidas_count': salidas,
        'gestores_count': gestores,
    })

# --- Entradas ---
@login_required
def entrada_list(request):
    items = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'items': items})

@login_required
def entrada_create(request):
    form = EntradaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_update(request, pk):
    obj = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    form = EntradaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def entrada_delete(request, pk):
    obj = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'obj': obj})

# --- Salidas ---
@login_required
def salida_list(request):
    items = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'items': items})

@login_required
def salida_create(request):
    form = SalidaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_update(request, pk):
    obj = get_object_or_404(CorrespondenciaSalida, pk=pk)
    form = SalidaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def salida_delete(request, pk):
    obj = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'obj': obj})

# --- Gestores ---
@login_required
def gestor_list(request):
    items = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'items': items})

@login_required
def gestor_create(request):
    form = GestorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_update(request, pk):
    obj = get_object_or_404(Gestor, pk=pk)
    form = GestorForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_delete(request, pk):
    obj = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'obj': obj})
