from django.shortcuts       import render, redirect, get_object_or_404
from django.contrib.auth    import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator  import Paginator
from django.http            import HttpResponse
from django.contrib         import messages
from django.db              import models
import csv
import openpyxl
from openpyxl.utils        import get_column_letter

from .models import CorrespondenciaEntrada, DocumentManager
from .forms  import EntradaForm, DocumentManagerForm

# Permiso para staff

def is_staff_user(user):
    return user.is_staff

# Login/logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}")
            return redirect(request.GET.get('next', 'correspondencia_app:dashboard'))
        messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'correspondencia_app/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect('correspondencia_app:login')

# Dashboard

@login_required
def dashboard(request):
    return render(request, 'correspondencia_app/dashboard.html')

# Listar Entradas

@login_required
def entrada_list(request):
    q = request.GET.get('q', '')
    qs = CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion')
    if q:
        qs = qs.filter(
            models.Q(asunto__icontains=q) |
            models.Q(remitente__icontains=q)
        )
    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'correspondencia_app/entrada_list.html', {
        'entradas': page_obj,
        'q': q,
    })

# Crear Entrada

@login_required
@user_passes_test(is_staff_user)
def entrada_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada creada correctamente")
            return redirect('correspondencia_app:entrada_list')
        messages.error(request, "Por favor corrige los errores en el formulario")
    else:
        form = EntradaForm()
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form, 'edit': False})

# Editar Entrada

@login_required
@user_passes_test(is_staff_user)
def entrada_edit(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, request.FILES, instance=entrada)
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada actualizada")
            return redirect('correspondencia_app:entrada_list')
        messages.error(request, "Por favor corrige los errores en el formulario")
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form, 'edit': True})

# Eliminar Entrada

@login_required
@user_passes_test(is_staff_user)
def entrada_delete(request, pk):
    entrada = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        messages.success(request, "Entrada eliminada")
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'entrada': entrada})

# Exportar CSV

@login_required
@user_passes_test(is_staff_user)
def export_entradas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="entradas.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','Número','Asunto','Fecha recepción','Remitente','Destinatario','Estado','Gestor'])
    for e in CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion'):
        writer.writerow([
            e.pk, e.numero_documento, e.asunto, e.fecha_recepcion,
            e.remitente, e.destinatario, e.estado,
            e.gestor.nombre if e.gestor else ''
        ])
    return response

# Exportar XLSX

@login_required
@user_passes_test(is_staff_user)
def export_entradas_xlsx(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Entradas'
    headers = ['ID','Número','Asunto','Fecha recepción','Remitente','Destinatario','Estado','Gestor']
    ws.append(headers)
    for e in CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion'):
        ws.append([
            e.pk,
            e.numero_documento,
            e.asunto,
            e.fecha_recepcion.strftime('%Y-%m-%d'),
            e.remitente,
            e.destinatario,
            e.estado,
            e.gestor.nombre if e.gestor else ''
        ])
    for i in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(i)].auto_size = True
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=entradas.xlsx'
    wb.save(response)
    return response

# Listar Gestores

@login_required
def document_manager_list(request):
    q = request.GET.get('q', '')
    qs = DocumentManager.objects.all().order_by('nombre')
    if q:
        qs = qs.filter(
            models.Q(nombre__icontains=q) |
            models.Q(email__icontains=q)
        )
    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'correspondencia_app/document_manager_list.html', {
        'gestores': page_obj,
        'q': q,
    })

# Crear Gestor

@login_required
@user_passes_test(is_staff_user)
def document_manager_create(request):
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Gestor creado correctamente")
            return redirect('correspondencia_app:document_manager_list')
        messages.error(request, "Por favor corrige los errores en el formulario")
    else:
        form = DocumentManagerForm()
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form, 'edit': False})

# Editar Gestor

@login_required
@user_passes_test(is_staff_user)
def document_manager_edit(request, pk):
    gestor = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        form = DocumentManagerForm(request.POST, request.FILES, instance=gestor)
        if form.is_valid():
            form.save()
            messages.success(request, "Gestor actualizado")
            return redirect('correspondencia_app:document_manager_list')
        messages.error(request, "Por favor corrige los errores en el formulario")
    else:
        form = DocumentManagerForm(instance=gestor)
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form, 'edit': True})

# Eliminar Gestor

@login_required
@user_passes_test(is_staff_user)
def document_manager_delete(request, pk):
    gestor = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        gestor.delete()
        messages.success(request, "Gestor eliminado")
        return redirect('correspondencia_app:document_manager_list')
    return render(request, 'correspondencia_app/document_manager_confirm_delete.html', {'gestor': gestor})

# Exportar Gestores CSV

@login_required
@user_passes_test(is_staff_user)
def export_gestores_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gestores.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID','Nombre','Email','Teléfono'])
    for g in DocumentManager.objects.all().order_by('nombre'):
        writer.writerow([g.pk, g.nombre, g.email, g.telefono])
    return response

# Exportar Gestores XLSX

@login_required
@user_passes_test(is_staff_user)
def export_gestores_xlsx(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Gestores'
    headers = ['ID','Nombre','Email','Teléfono']
    ws.append(headers)
    for g in DocumentManager.objects.all().order_by('nombre'):
        ws.append([g.pk, g.nombre, g.email, g.telefono])
    for i in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(i)].auto_size = True
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=gestores.xlsx'
    wb.save(response)
    return response