from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Count

from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida
from .forms import GestorForm, EntradaForm, SalidaForm

# --- LOGIN ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('correspondencia_app:dashboard')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('correspondencia_app:dashboard')

    return render(request, 'correspondencia_app/login.html', {'form': form})

# --- LOGOUT ---
@login_required
def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')

# --- DASHBOARD ---
@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# --- GESTORES ---
@login_required
def gestor_list(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

@login_required
def gestor_create(request):
    form = GestorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('correspondencia_app:gestor_list')
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
def gestor_delete(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        return redirect('correspondencia_app:gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'gestor': gestor})

# --- ENTRADAS ---
@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion')
    query = request.GET.get("q")
    if query:
        entradas = entradas.filter(numero_documento__icontains=query)
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def entrada_create(request):
    form = EntradaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

# --- SALIDAS ---
@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all().order_by('-fecha_envio')
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def salida_create(request):
    form = SalidaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('correspondencia_app:salida_list')
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

# --- ESTADÍSTICA: Entradas por mes ---
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

    return JsonResponse({
        "labels": etiquetas,
        "data": cantidades,
    })
