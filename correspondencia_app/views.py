from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Count
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm

@login_required
def dashboard(request):
    total_entradas = CorrespondenciaEntrada.objects.count()
    total_salidas = CorrespondenciaSalida.objects.count()
    total_gestores = Gestor.objects.count()
    return render(request, 'correspondencia_app/dashboard.html', {
        'total_entradas': total_entradas,
        'total_salidas': total_salidas,
        'total_gestores': total_gestores,
    })

# --- ENTRADAS ---
@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def entrada_create(request):
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

# --- SALIDAS ---
@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def salida_create(request):
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:salida_list')
    else:
        form = CorrespondenciaSalidaForm()
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

# --- GESTORES ---
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

# --- GRÁFICAS ---
@login_required
def entradas_por_mes(request):
    datos = (
        CorrespondenciaEntrada.objects
        .annotate(mes=TruncMonth("fecha_recepcion"))
        .values("mes")
        .annotate(total=Count("id"))
        .order_by("mes")
    )
    etiquetas = [dato["mes"].strftime("%B") for dato in datos]
    cantidades = [dato["total"] for dato in datos]
    return JsonResponse({"labels": etiquetas, "data": cantidades})

@login_required
def salidas_por_mes(request):
    datos = (
        CorrespondenciaSalida.objects
        .annotate(mes=TruncMonth("fecha_envio"))
        .values("mes")
        .annotate(total=Count("id"))
        .order_by("mes")
    )
    etiquetas = [dato["mes"].strftime("%B") for dato in datos]
    cantidades = [dato["total"] for dato in datos]
    return JsonResponse({"labels": etiquetas, "data": cantidades})

# --- LOGOUT ---
@login_required
def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')
