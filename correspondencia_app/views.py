from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, DocumentManager
from .forms  import EntradaForm, DocumentManagerForm

def login_view(request):
    # … tu lógica de login …
    pass

def logout_view(request):
    # … tu lógica de logout …
    pass

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# ——— Entradas ———

@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion')
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
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form, 'edit': False})

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
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form, 'edit': True})

@login_required
def entrada_delete(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'entrada': entrada})

# ——— Document Managers / Gestores ———

@login_required
def document_manager_list(request):
    gestores = DocumentManager.objects.all().order_by('nombre')
    return render(request, 'correspondencia_app/document_manager_list.html', {'gestores': gestores})

@login_required
def document_manager_create(request):
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:document_manager_list')
    else:
        form = DocumentManagerForm()
    return render(request, 'correspondencia_app/document_manager_form.html', {
        'form': form,
        'edit': False,
          })
@login_required
def document_manager_edit(request, pk):
    gestor = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST, request.FILES, instance=gestor)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:document_manager_list')
    else:
        form = DocumentManagerForm(instance=gestor)
    return render(request, 'correspondencia_app/document_manager_form.html', {
        'form': form,
        'edit': True,
    })
@login_required
def document_manager_delete(request, pk):
    gestor = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        return redirect('correspondencia_app:document_manager_list')
    return render(request, 'correspondencia_app/document_manager_confirm_delete.html', {'gestor': gestor})
