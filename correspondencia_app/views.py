from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CorrespondenciaEntrada, CorrespondenciaSalida, Gestor
from .forms import CorrespondenciaEntradaForm, CorrespondenciaSalidaForm, GestorForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

class CustomLoginView(LoginView):
    template_name = 'correspondencia_app/login.html'

@login_required
def entrada_list(request):
    entradas = CorrespondenciaEntrada.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
def crear_entrada(request):
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm()
    return render(request, 'correspondencia_app/crear_entrada.html', {'form': form})

@login_required
def editar_entrada(request, entrada_id):
    entrada = get_object_or_404(CorrespondenciaEntrada, id=entrada_id)
    if request.method == 'POST':
        form = CorrespondenciaEntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('entrada_list')
    else:
        form = CorrespondenciaEntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/editar_entrada.html', {'form': form, 'entrada': entrada})

@login_required
def eliminar_entrada(request, entrada_id):
    entrada = get_object_or_404(CorrespondenciaEntrada, id=entrada_id)
    if request.method == 'POST':
        entrada.delete()
        return redirect('entrada_list')
    return render(request, 'correspondencia_app/eliminar_entrada.html', {'entrada': entrada})

@login_required
def salida_list(request):
    salidas = CorrespondenciaSalida.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
def crear_salida(request):
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm()
    return render(request, 'correspondencia_app/crear_salida.html', {'form': form})

@login_required
def editar_salida(request, salida_id):
    salida = get_object_or_404(CorrespondenciaSalida, id=salida_id)
    if request.method == 'POST':
        form = CorrespondenciaSalidaForm(request.POST, request.FILES, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('salida_list')
    else:
        form = CorrespondenciaSalidaForm(instance=salida)
    return render(request, 'correspondencia_app/editar_salida.html', {'form': form, 'salida': salida})

@login_required
def eliminar_salida(request, salida_id):
    salida = get_object_or_404(CorrespondenciaSalida, id=salida_id)
    if request.method == 'POST':
        salida.delete()
        return redirect('salida_list')
    return render(request, 'correspondencia_app/eliminar_salida.html', {'salida': salida})

@login_required
def gestor_list(request):
    gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

@login_required
def crear_gestor(request):
    if request.method == 'POST':
        form = GestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestor_list')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/crear_gestor.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
# VISTA: Listado de usuarios registrados (solo superusuarios pueden ver esto)
@login_required
def lista_usuarios(request):
    if not request.user.is_superuser:
        return redirect('entrada_list')
    usuarios = User.objects.all()
    return render(request, 'correspondencia_app/usuario_list.html', {'usuarios': usuarios})


# VISTA: Eliminar usuario (solo superusuarios)
@login_required
def eliminar_usuario(request, pk):
    if not request.user.is_superuser:
        return redirect('entrada_list')
    usuario = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'correspondencia_app/usuario_confirm_delete.html', {'usuario': usuario})
