from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import CorrespondenciaEntrada, Gestor
from .forms import EntradaForm, GestorForm

def staff_required(user):
    return user.is_active and user.is_staff

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return staff_required(self.request.user)

@login_required
def dashboard(request):
    # Aquí tus estadísticas (total entradas, total gestores, etc.)
    total_entradas = CorrespondenciaEntrada.objects.count()
    total_gestores = Gestor.objects.count()
    return render(request, 'correspondencia_app/dashboard.html', {
        'total_entradas': total_entradas,
        'total_gestores': total_gestores,
    })

# --- Entradas ---
class EntradaListView(LoginRequiredMixin, ListView):
    model = CorrespondenciaEntrada
    template_name = 'correspondencia_app/entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = super().get_queryset().select_related('gestor').order_by('-pk')
        if q:
            qs = qs.filter(asunto__icontains=q)
        return qs

class EntradaCreateView(StaffRequiredMixin, CreateView):
    model = CorrespondenciaEntrada
    form_class = EntradaForm
    template_name = 'correspondencia_app/entrada_form.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')

class EntradaUpdateView(StaffRequiredMixin, UpdateView):
    model = CorrespondenciaEntrada
    form_class = EntradaForm
    template_name = 'correspondencia_app/entrada_form.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')

class EntradaDeleteView(StaffRequiredMixin, DeleteView):
    model = CorrespondenciaEntrada
    template_name = 'correspondencia_app/entrada_confirm_delete.html'
    success_url = reverse_lazy('correspondencia_app:entrada_list')

# --- Gestores ---
class GestorListView(LoginRequiredMixin, ListView):
    model = Gestor
    template_name = 'correspondencia_app/gestor_list.html'
    context_object_name = 'gestores'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = super().get_queryset().order_by('nombre')
        if q:
            qs = qs.filter(nombre__icontains=q)
        return qs

class GestorCreateView(StaffRequiredMixin, CreateView):
    model = Gestor
    form_class = GestorForm
    template_name = 'correspondencia_app/gestor_form.html'
    success_url = reverse_lazy('correspondencia_app:gestor_list')

class GestorUpdateView(StaffRequiredMixin, UpdateView):
    model = Gestor
    form_class = GestorForm
    template_name = 'correspondencia_app/gestor_form.html'
    success_url = reverse_lazy('correspondencia_app:gestor_list')

class GestorDeleteView(StaffRequiredMixin, DeleteView):
    model = Gestor
    template_name = 'correspondencia_app/gestor_confirm_delete.html'
    success_url = reverse_lazy('correspondencia_app:gestor_list')
