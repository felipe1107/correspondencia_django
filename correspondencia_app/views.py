from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, DocumentManager
from .forms  import EntradaForm, DocumentManagerForm

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'correspondencia_app/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'correspondencia_app/login.html')

@login_required
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
def entrada_edit(request, pk):
    obj = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = EntradaForm(instance=obj)
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
            return redirect('document_manager_list')
    else:
        form = DocumentManagerForm()
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form})

@login_required
def document_manager_edit(request, pk):
    obj = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('document_manager_list')
    else:
        form = DocumentManagerForm(instance=obj)
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form})
