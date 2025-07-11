from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import EntradaCorrespondencia, SalidaCorrespondencia, Gestor
from .forms import EntradaForm, SalidaForm, GestorForm
from django.db.models import Q

# Roles
def es_administrador(user):
    return user.groups.filter(name='Administrador').exists()

def es_editor(user):
    return user.groups.filter(name='Editor').exists()

def es_visualizador(user):
    return user.groups.filter(name='Visualizador').exists()

# Autenticación
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            return render(request, 'correspondencia_app/login.html', {'error': 'Usuario o contraseña inválidos'})
    return render(request, 'correspondencia_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')

# Dashboard
@login_required
def dashboard(request):
    total_entradas = EntradaCorrespondencia.objects.count()
    total_salidas = SalidaCorrespondencia.objects.count()
    total_gestores = Gestor.objects.count()
    ultimas_entradas = EntradaCorrespondencia.objects.order_by('-fecha_recepcion')[:5]
    ultimas_salidas = SalidaCorrespondencia.objects.order_by('-fecha_envio')[:5]
    context = {
        'total_entradas': total_entradas,
        'total_salidas': total_salidas,
        'total_gestores': total_gestores,
        'ultimas_entradas': ultimas_entradas,
        'ultimas_salidas': ultimas_salidas,
    }
    return render(request, 'correspondencia_app/dashboard.html', context)

# Entradas
@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u) or es_visualizador(u))
def entrada_list(request):
    query = request.GET.get("q")
    if query:
        entradas = EntradaCorrespondencia.objects.filter(
            Q(numero_documento__icontains=query) |
            Q(remitente__icontains=query) |
            Q(destinatario__icontains=query) |
            Q(asunto__icontains=query) |
            Q(departamento_destino__icontains=query) |
            Q(estado__icontains=query)
        )
    else:
        entradas = EntradaCorrespondencia.objects.all()
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': entradas})

@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u))
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
@user_passes_test(lambda u: es_administrador(u) or es_editor(u))
def entrada_edit(request, pk):
    entrada = get_object_or_404(EntradaCorrespondencia, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: es_administrador(u))
def entrada_delete(request, pk):
    item = get_object_or_404(EntradaCorrespondencia, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'item': item})

# Salidas
@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u) or es_visualizador(u))
def salida_list(request):
    salidas = SalidaCorrespondencia.objects.all()
    return render(request, 'correspondencia_app/salida_list.html', {'salidas': salidas})

@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u))
def salida_create(request):
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:salida_list')
    else:
        form = SalidaForm()
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u))
def salida_edit(request, pk):
    salida = get_object_or_404(SalidaCorrespondencia, pk=pk)
    if request.method == 'POST':
        form = SalidaForm(request.POST, request.FILES, instance=salida)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:salida_list')
    else:
        form = SalidaForm(instance=salida)
    return render(request, 'correspondencia_app/salida_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: es_administrador(u))
def salida_delete(request, pk):
    item = get_object_or_404(SalidaCorrespondencia, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('correspondencia_app:salida_list')
    return render(request, 'correspondencia_app/salida_confirm_delete.html', {'item': item})

# Gestores
@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u) or es_visualizador(u))
def gestor_list(request):
    query = request.GET.get("q")
    if query:
        gestores = Gestor.objects.filter(
            Q(nombre__icontains=query) | Q(departamento__icontains=query)
        )
    else:
        gestores = Gestor.objects.all()
    return render(request, 'correspondencia_app/gestor_list.html', {'gestores': gestores})

@login_required
@user_passes_test(lambda u: es_administrador(u) or es_editor(u))
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
@user_passes_test(lambda u: es_administrador(u) or es_editor(u))
def gestor_update(request, pk):
    item = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        form = GestorForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:gestor_list')
    else:
        form = GestorForm(instance=item)
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

@login_required
@user_passes_test(lambda u: es_administrador(u))
def gestor_delete(request, pk):
    item = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('correspondencia_app:gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'item': item})

# Página de inicio
def index(request):
    return render(request, 'correspondencia_app/inicio.html')
