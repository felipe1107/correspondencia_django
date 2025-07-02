from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models.functions import TruncMonth
from django.db.models import Count
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

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

    return JsonResponse({
        "labels": etiquetas,
        "data": cantidades,
    })

@login_required
def lista_entradas(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/lista_entradas.html', {'entradas': entradas})

@login_required
def crear_entrada(request):
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:lista_entradas')
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, 'correspondencia_app/crear_entrada.html', {'form': form})

@login_required
def lista_salidas(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/lista_salidas.html', {'salidas': salidas})

@login_required
def crear_salida(request):
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:lista_salidas')
    else:
        form = CorrespondenciaSalidaForm()
    return render(request, 'correspondencia_app/crear_salida.html', {'form': form})

@login_required
def lista_gestores(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/lista_gestores.html', {'gestores': gestores})

@login_required
def crear_gestor(request):
    if request.method == 'POST':
        form = GestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:lista_gestores')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/crear_gestor.html', {'form': form})
