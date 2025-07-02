from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import TruncMonth

from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import EntradaForm, SalidaForm, GestorForm

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion')
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all().order_by('-fecha_envio')
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def gestor_list(request):
    gestores = Gestor.objects.all().order_by('nombre')
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

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
