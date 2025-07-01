from django.shortcuts           import render, redirect, get_object_or_404
from django.contrib.auth        import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic       import ListView, CreateView, UpdateView, DeleteView
from django.urls                import reverse_lazy
from django.contrib             import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator      import Paginator
from django.http                import HttpResponse
from django.db.models           import Count, Q
import csv, openpyxl
from openpyxl.utils             import get_column_letter

from .models  import CorrespondenciaEntrada, DocumentManager
from .forms   import EntradaForm, DocumentManagerForm

# Mixins
def staff_required(user):
    return user.is_staff

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para esa acción.")
        return redirect('correspondencia_app:dashboard_stats')

# Authentication
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

# Dashboard
def dashboard_stats(request):
    by_gestor = (CorrespondenciaEntrada.objects
                 .values('gestor__nombre')
                 .annotate(total=Count('pk'))
                 .order_by('-total'))
    by_estado = (CorrespondenciaEntrada.objects
                 .values('estado')
                 .annotate(total=Count('pk'))
                 .order_by('-total'))
    return render(request, 'correspondencia_app/dashboard_stats.html', {
        'by_gestor': list(by_gestor), 'by_estado': list(by_estado)
    })

# Entradas CBV (sin cambios)
class EntradaListView(LoginRequiredMixin, ListView):
    model = CorrespondenciaEntrada
    template_name = 'correspondencia_app/entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 10
    ordering = ['-fecha_recepcion']
    def get_queryset(self):
        qs = super().get_queryset()
        q  = self.request.GET.get('q','')
        if q:
            qs = qs.filter(Q(asunto__icontains=q) | Q(remitente__icontains=q))
        return qs
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q','')
        return ctx

class EntradaCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = CorrespondenciaEntrada
    form_class = EntradaForm
    template_name = 'correspondencia_app/entrada_form.html'
    success_url  = reverse_lazy('correspondencia_app:entrada_list')
    def form_valid(self, form):
        messages.success(self.request, "Entrada creada correctamente.")
        return super().form_valid(form)

class EntradaUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = CorrespondenciaEntrada
    form_class = EntradaForm
    template_name = 'correspondencia_app/entrada_form.html'
    success_url  = reverse_lazy('correspondencia_app:entrada_list')
    def form_valid(self, form):
        messages.success(self.request, "Entrada actualizada correctamente.")
        return super().form_valid(form)

class EntradaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = CorrespondenciaEntrada
    template_name = 'correspondencia_app/entrada_confirm_delete.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Entrada eliminada correctamente.")
        return super().delete(request, *args, **kwargs)

# Gestores CBV
class GestorListView(LoginRequiredMixin, ListView):
    model = DocumentManager
    template_name = 'correspondencia_app/document_manager_list.html'
    context_object_name = 'gestores'
    paginate_by = 10
    ordering = ['nombre']
    def get_queryset(self):
        qs = super().get_queryset()
        q  = self.request.GET.get('q','')
        if q:
            qs = qs.filter(Q(nombre__icontains=q) | Q(email__icontains=q))
        return qs
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q','')
        return ctx

class GestorCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = DocumentManager
    form_class = DocumentManagerForm
    template_name = 'correspondencia_app/document_manager_form.html'
    success_url  = reverse_lazy('correspondencia_app:document_manager_list')
    def form_valid(self, form):
        messages.success(self.request, "Gestor creado correctamente.")
        return super().form_valid(form)

class GestorUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = DocumentManager
    form_class = DocumentManagerForm
    template_name = 'correspondencia_app/document_manager_form.html'
    success_url  = reverse_lazy('correspondencia_app:document_manager_list')
    def form_valid(self, form):
        messages.success(self.request, "Gestor actualizado correctamente.")
        return super().form_valid(form)

class GestorDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = DocumentManager
    template_name = 'correspondencia_app/document_manager_confirm_delete.html'
    success_url = reverse_lazy('correspondencia_app:document_manager_list')
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Gestor eliminado correctamente.")
        return super().delete(request, *args, **kwargs)