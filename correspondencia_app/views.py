from django.shortcuts       import render, redirect, get_object_or_404
from django.contrib.auth    import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator  import Paginator
from django.http            import HttpResponse
from django.contrib         import messages
from django.db.models       import Count, Q
import csv
import openpyxl
from openpyxl.utils        import get_column_letter

from .models import CorrespondenciaEntrada, DocumentManager
from .forms  import EntradaForm, DocumentManagerForm

def is_staff_user(user):
    return user.is_staff

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            messages.success(request, f"Bienvenido, {user.username}")
            return redirect('correspondencia_app:dashboard_stats')
        messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'correspondencia_app/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión")
    return redirect('correspondencia_app:login')

@login_required
def dashboard_stats(request):
    by_gestor = (
        CorrespondenciaEntrada.objects
        .values('gestor__nombre')
        .annotate(total=Count('id'))
        .order_by('-total')
    )
    by_estado = (
        CorrespondenciaEntrada.objects
        .values('estado')
        .annotate(total=Count('id'))
        .order_by('-total')
    )
    return render(request, 'correspondencia_app/dashboard_stats.html', {
        'by_gestor': list(by_gestor),
        'by_estado': list(by_estado),
    })

@login_required
def entrada_list(request):
    q = request.GET.get('q', '')
    qs = CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion')
    if q:
        qs = qs.filter(Q(asunto__icontains=q) | Q(remitente__icontains=q))
    page = Paginator(qs, 10).get_page(request.GET.get('page'))
    return render(request, 'correspondencia_app/entrada_list.html', {'entradas': page, 'q': q})

@login_required
@user_passes_test(is_staff_user)
def entrada_create(request):
    form = EntradaForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada creada correctamente")
            return redirect('correspondencia_app:entrada_list')
        messages.error(request, "Corrige los errores")
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form, 'edit': False})

@login_required
@user_passes_test(is_staff_user)
def entrada_edit(request, pk):
    e = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    form = EntradaForm(request.POST or None, request.FILES or None, instance=e)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Entrada actualizada")
            return redirect('correspondencia_app:entrada_list')
        messages.error(request, "Corrige los errores")
    return render(request, 'correspondencia_app/entrada_form.html', {'form': form, 'edit': True})

@login_required
@user_passes_test(is_staff_user)
def entrada_delete(request, pk):
    e = get_object_or_404(CorrespondenciaEntrada, pk=pk)
    if request.method == 'POST':
        e.delete()
        messages.success(request, "Entrada eliminada")
        return redirect('correspondencia_app:entrada_list')
    return render(request, 'correspondencia_app/entrada_confirm_delete.html', {'entrada': e})

@login_required
@user_passes_test(is_staff_user)
def export_entradas_csv(request):
    resp = HttpResponse(content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename="entradas.csv"'
    w = csv.writer(resp)
    w.writerow(['ID','Número','Asunto','Fecha','Remitente','Destinatario','Estado','Gestor'])
    for e in CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion'):
        w.writerow([e.pk, e.numero_documento, e.asunto, e.fecha_recepcion,
                    e.remitente, e.destinatario, e.estado,
                    e.gestor.nombre if e.gestor else ''])
    return resp

@login_required
@user_passes_test(is_staff_user)
def export_entradas_xlsx(request):
    wb = openpyxl.Workbook()
    ws = wb.active; ws.title = 'Entradas'
    hdr = ['ID','Número','Asunto','Fecha','Remitente','Destinatario','Estado','Gestor']
    ws.append(hdr)
    for e in CorrespondenciaEntrada.objects.all().order_by('-fecha_recepcion'):
        ws.append([e.pk, e.numero_documento, e.asunto, e.fecha_recepcion.strftime('%Y-%m-%d'),
                   e.remitente, e.destinatario, e.estado,
                   e.gestor.nombre if e.gestor else ''])
    for i in range(1, len(hdr)+1):
        ws.column_dimensions[get_column_letter(i)].width = 20
    resp = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    resp['Content-Disposition'] = 'attachment; filename=entradas.xlsx'
    wb.save(resp)
    return resp

@login_required
def document_manager_list(request):
    q = request.GET.get('q', '')
    qs = DocumentManager.objects.all().order_by('nombre')
    if q:
        qs = qs.filter(Q(nombre__icontains=q) | Q(email__icontains=q))
    page = Paginator(qs, 10).get_page(request.GET.get('page'))
    return render(request, 'correspondencia_app/document_manager_list.html', {'gestores': page, 'q': q})

@login_required
@user_passes_test(is_staff_user)
def document_manager_create(request):
    form = DocumentManagerForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Gestor creado correctamente")
            return redirect('correspondencia_app:document_manager_list')
        messages.error(request, "Corrige los errores")
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form, 'edit': False})

@login_required
@user_passes_test(is_staff_user)
def document_manager_edit(request, pk):
    g = get_object_or_404(DocumentManager, pk=pk)
    form = DocumentManagerForm(request.POST or None, request.FILES or None, instance=g)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Gestor actualizado")
            return redirect('correspondencia_app:document_manager_list')
        messages.error(request, "Corrige los errores")
    return render(request, 'correspondencia_app/document_manager_form.html', {'form': form, 'edit': True})

@login_required
@user_passes_test(is_staff_user)
def document_manager_delete(request, pk):
    g = get_object_or_404(DocumentManager, pk=pk)
    if request.method == 'POST':
        g.delete()
        messages.success(request, "Gestor eliminado")
        return redirect('correspondencia_app:document_manager_list')
    return render(request, 'correspondencia_app/document_manager_confirm_delete.html', {'gestor': g})

@login_required
@user_passes_test(is_staff_user)
def export_gestores_csv(request):
    resp = HttpResponse(content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename="gestores.csv"'
    w = csv.writer(resp)
    w.writerow(['ID','Nombre','Email','Teléfono'])
    for g in DocumentManager.objects.all().order_by('nombre'):
        w.writerow([g.pk, g.nombre, g.email, g.telefono])
    return resp

@login_required
@user_passes_test(is_staff_user)
def export_gestores_xlsx(request):
    wb = openpyxl.Workbook()
    ws = wb.active; ws.title = 'Gestores'
    hdr = ['ID','Nombre','Email','Teléfono']
    ws.append(hdr)
    for g in DocumentManager.objects.all().order_by('nombre'):
        ws.append([g.pk, g.nombre, g.email, g.telefono])
    for i in range(1, len(hdr)+1):
        ws.column_dimensions[get_column_letter(i)].width = 20
    resp = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    resp['Content-Disposition'] = 'attachment; filename=gestores.xlsx'
    wb.save(resp)
    return resp
