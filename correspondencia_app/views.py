# correspondencia_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Gestor, CorrespondenciaEntrada, CorrespondenciaSalida
from .forms import GestorForm, CorrespondenciaEntradaForm, CorrespondenciaSalidaForm

# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio")
        else:
            return render(request, "correspondencia_app/login.html", {"error": "Credenciales inválidas"})
    return render(request, "correspondencia_app/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

# INICIO
@login_required
def inicio(request):
    return render(request, "correspondencia_app/inicio.html")

# GESTORES
@login_required
def gestor_list(request):
    gestores = Gestor.objects.all()
    return render(request, "correspondencia_app/gestor_list.html", {"gestores": gestores})

@login_required
def gestor_create(request):
    if request.method == "POST":
        form = GestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestor_list")
    else:
        form = GestorForm()
    return render(request, "correspondencia_app/gestor_form.html", {"form": form})

@login_required
def gestor_delete(request, pk):
    gestor = get_object_or_404(Gestor, pk=pk)
    if request.method == "POST":
        gestor.delete()
        return redirect("gestor_list")
    return render(request, "correspondencia_app/gestor_confirm_delete.html", {"gestor": gestor})

# ENTRADAS
@login_required
def entrada_list(request):
    query = request.GET.get("q")
    if query:
        entradas = CorrespondenciaEntrada.objects.filter(asunto__icontains=query)
    else:
        entradas = CorrespondenciaEntrada.objects.all()
    return render(request, "correspondencia_app/entrada_list.html", {"entradas": entradas})

@login_required
def entrada_create(request):
    if request.method == "POST":
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("entrada_list")
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, "correspondencia_app/entrada_form.html", {"form": form})

# SALIDAS (Paso 2)
@login_required
def salida_list(request):
    query = request.GET.get("q")
    if query:
        salidas = CorrespondenciaSalida.objects.filter(asunto__icontains=query)
    else:
        salidas = CorrespondenciaSalida.objects.all()
    return render(request, "correspondencia_app/salida_list.html", {"salidas": salidas})

@login_required
def salida_create(request):
    if request.method == "POST":
        form = CorrespondenciaSalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("salida_list")
    else:
        form = CorrespondenciaSalidaForm()
    return render(request, "correspondencia_app/salida_form.html", {"form": form})

@login_required
def salida_update(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == "POST":
        form = CorrespondenciaSalidaForm(request.POST, request.FILES, instance=salida)
        if form.is_valid():
            form.save()
            return redirect("salida_list")
    else:
        form = CorrespondenciaSalidaForm(instance=salida)
    return render(request, "correspondencia_app/salida_form.html", {"form": form})

@login_required
def salida_delete(request, pk):
    salida = get_object_or_404(CorrespondenciaSalida, pk=pk)
    if request.method == "POST":
        salida.delete()
        return redirect("salida_list")
    return render(request, "correspondencia_app/salida_confirm_delete.html", {"salida": salida})
