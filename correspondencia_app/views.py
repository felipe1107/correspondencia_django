from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import CorrespondenciaEntrada, DocumentManager
from .forms import EntradaForm, DocumentManagerForm

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            error = "Usuario o contraseña incorrectos"
    return render(request, 'correspondencia_app/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')

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
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def document_manager_list(request):
    gestores = DocumentManager.objects.all()
    return render(request, 'correspondencia_app/document_manager_list.html', {'gestores': gestores})

@login_required
def document_manager_create(request):
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:document_manager_list')
    else:
        form = DocumentManagerForm()
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form})
