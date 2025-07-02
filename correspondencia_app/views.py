from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import CorrespondenciaEntrada, Gestor
from .forms import EntradaForm, GestorForm

# Vista de login
def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('password')
        user = authenticate(request, username=usuario, password=clave)
        if user:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            return render(request, 'correspondencia_app/login.html', {
                'error': 'Usuario o clave inválidos'
            })
    return render(request, 'correspondencia_app/login.html')

# Vista de logout
def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')

# Decorador para restringir a usuarios staff
def staff_required(view_func):
    return user_passes_test(lambda u: u.is_staff, login_url='correspondencia_app:login')(view_func)

# Vista del dashboard
@login_required
def dashboard(request):
    total_entradas = CorrespondenciaEntrada.objects.count()
    total_gestores = Gestor.objects.count()
    recientes = CorrespondenciaEntrada.objects.order_by('-pk')[:5]
    return render(request, 'correspondencia_app/dashboard.html', {
        'total_entradas': total_entradas,
        'total_gestores': total_gestores,
        'recientes': recientes,
    })

# Lista de entradas
@staff_required
def entrada_list(request):
    q = request.GET.get('q', '')
    qs = CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion')
    if q:
        qs = qs.filter(asunto__icontains=q)
    return render(request, 'correspondencia_app/entrada_list.html', {
        'entradas': qs,
        'q': q,
    })

# Crear nueva entrada
@staff_required
def entrada_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

# Editar entrada existente
@staff_required
def entrada_edit(request, pk):
    obj = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:entrada_list')
    else:
        form = EntradaForm(instance=obj)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form})

# Eliminar entrada
@staff_required
def entrada_delete(request, pk):
    obj = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'object': obj})

# Lista de gestores
@staff_required
def gestor_list(request):
    q = request.GET.get('q', '')
    qs = Gestor.objects.all().order_by('nombre')
    if q:
        qs = qs.filter(nombre__icontains=q)
    return render(request, 'correspondencia_app/gestor_list.html', {
        'gestores': qs,
        'q': q,
    })

# Crear nuevo gestor
@staff_required
def gestor_create(request):
    if request.method == 'POST':
        form = GestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:gestor_list')
    else:
        form = GestorForm()
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

# Editar gestor
@staff_required
def gestor_edit(request, pk):
    obj = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        form = GestorForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('correspondencia_app:gestor_list')
    else:
        form = GestorForm(instance=obj)
    return render(request, 'correspondencia_app/gestor_form.html', {'form': form})

# Eliminar gestor
@staff_required
def gestor_delete(request, pk):
    obj = get_object_or_404(Gestor, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('correspondencia_app:gestor_list')
    return render(request, 'correspondencia_app/gestor_confirm_delete.html', {'object': obj})
