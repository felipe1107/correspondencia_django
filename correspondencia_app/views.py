from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# --------------------------------------
# ENTRADAS
# --------------------------------------

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
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def editar_entrada(request, pk):
    item = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm(instance=item)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
def eliminar_entrada(request, pk):
    item = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'item': item})

# --------------------------------------
# SALIDAS
# --------------------------------------

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
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def editar_salida(request, pk):
    item = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm(instance=item)
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
def eliminar_salida(request, pk):
    item = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'item': item})

# --------------------------------------
# GESTORES
# --------------------------------------

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
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def editar_gestor(request, pk):
    item = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        form = GestorForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorForm(instance=item)
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def eliminar_gestor(request, pk):
    item = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'item': item})
