# correspondencia_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, DocumentManager
from .forms import EntradaForm, DocumentManagerForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            messages.error(request, "Usuario o contraseña inválidos")
    return render(request, 'correspondencia_app/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# — Entradas —
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
def entrada_edit(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

# — Gestores / Document Managers —
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
            return redirect('correspondencia_app:lista_del_administrador_de_documentos')
    else:
        form = DocumentManagerForm()
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form})

@login_required
def document_manager_edit(request, pk):
    gestor = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST, instance=gestor)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:lista_del_administrador_de_documentos')
    else:
        form = DocumentManagerForm(instance=gestor)
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form})
