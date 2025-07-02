from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Count

from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida
from .forms import GestorForm, EntradaForm, SalidaForm


@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')


# ---------------- GESTORES ----------------
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
def gestor_delete(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        return redirect('correspondencia_app:gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'gestor': gestor})


# ---------------- ENTRADAS ----------------
@login_required
def entrada_list(request):
    q = request.GET.get("q")
    entradas = CorrespondenciaEntrada.objects.all()
    if q:
        entradas = entradas.filter(numero_documento__icontains=q) | entradas.filter(asunto__icontains=q)
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


# ---------------- SALIDAS ----------------
@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
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


# ---------------- LOGIN / LOGOUT ----------------
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('password')
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'correspondencia_app/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')


# ---------------- GRÁFICAS ----------------
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
