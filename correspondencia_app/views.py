from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Max
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import CorrespondenciaEntrada, DocumentManager
from .forms import EntradaForm, DocumentManagerForm

# Mixin para asegurar staff
class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

# -----------------------------------
# Login / Logout
# -----------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('correspondencia_app:dashboard')
        else:
            return render(request, 'correspondencia_app/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
    return render(request, 'correspondencia_app/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('correspondencia_app:login')

# -----------------------------------
# Dashboard con estadísticas
# -----------------------------------
@login_required
@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    total_entradas = CorrespondenciaEntrada.objects.count()
    total_gestores = DocumentManager.objects.count()
    return render(request, 'correspondencia_app/dashboard.html', {
        'total_entradas': total_entradas,
        'total_gestores': total_gestores,
    })

# -----------------------------------
# CRUD Entradas
# -----------------------------------
class EntradaListView(LoginRequiredMixin, ListView):
    model = CorrespondenciaEntrada
    template_name = 'correspondencia_app/entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 10
    ordering = ['-pk']

class EntradaCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = CorrespondenciaEntrada
    form_class = EntradaForm
    template_name = 'correspondencia_app/entrada_form.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')

    def form_valid(self, form):
        # Generar número automático
        max_num = CorrespondenciaEntrada.objects.aggregate(
            max_num=Max('numero_documento')
        )['max_num'] or 0
        form.instance.numero_documento = max_num + 1
        # Fecha automática
        form.instance.fecha_recepcion = timezone.now().date()
        return super().form_valid(form)

class EntradaUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = CorrespondenciaEntrada
    form_class = EntradaForm
    template_name = 'correspondencia_app/entrada_form.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')

class EntradaDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = CorrespondenciaEntrada
    template_name = 'correspondencia_app/entrada_confirm_delete.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')

# -----------------------------------
# CRUD Gestores (DocumentManager)
# -----------------------------------
class DocumentManagerListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    model = DocumentManager
    template_name = 'correspondencia_app/document_manager_list.html'
    context_object_name = 'gestores'
    paginate_by = 10
    ordering = ['-pk']

class DocumentManagerCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = DocumentManager
    form_class = DocumentManagerForm
    template_name = 'correspondencia_app/document_manager_form.html'
    success_url = reverse_lazy('correspondencia_app:document_manager_list')

class DocumentManagerUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = DocumentManager
    form_class = DocumentManagerForm
    template_name = 'correspondencia_app/document_manager_form.html'
    success_url = reverse_lazy('correspondencia_app:document_manager_list')

class DocumentManagerDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = DocumentManager
    template_name = 'correspondencia_app/document_manager_confirm_delete.html'
    success_url = reverse_lazy('correspondencia_app:document_manager_list')
