from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor
from .forms import EntradaForm, SalidaForm, GestorForm

# --- Autenticación ---

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña inválidos'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')


# --- Dashboard ---

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# --- Entradas ---

@login_required
def entrada_list(request):
    entradas = EntradaCorrespondencia.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})


@login_required
def entrada_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})


@login_required
def entrada_update(request, pk):
    item = get_object_or_404(EntradaCorrespondencia, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm(instance=item)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})


@login_required
def entrada_delete(request, pk):
    item = get_object_or_404(EntradaCorrespondencia, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'item': item})


# --- Salidas ---

@login_required
def salida_list(request):
    salidas = SalidaCorrespondencia.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})


@login_required
def salida_create(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:salida_list')
    else:
        form = SalidaForm()
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})


@login_required
def salida_update(request, pk):
    item = get_object_or_404(SalidaCorrespondencia, pk=pk)
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:salida_list')
    else:
        form = SalidaForm(instance=item)
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})


@login_required
def salida_delete(request, pk):
    item = get_object_or_404(SalidaCorrespondencia, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('correspondencia_app:salida_list')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'item': item})


# --- Gestores ---

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
            return redirect('correspondencia_app:gestor_list')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})


@login_required
def gestor_update(request, pk):
    item = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        form = GestorForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:gestor_list')
    else:
        form = GestorForm(instance=item)
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})


@login_required
def gestor_delete(request, pk):
    item = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('correspondencia_app:gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'item': item})

def custom_logout(request):
    logout(request)
    return redirect('login')