from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Cliente, CuentaBancaria
from .forms import ClienteForm, CuentaBancariaForm
from accounts.models import User
from notificaciones.models import Notificacion

def es_admin_o_empleado(user):
    return user.is_authenticated and (user.es_admin or user.es_empleado or user.is_superuser)

# ========== Listado de clientes ==========
class ListaClientesView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Cliente
    template_name = 'clientes/lista_clientes.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def test_func(self):
        return es_admin_o_empleado(self.request.user)

    def get_queryset(self):
        queryset = Cliente.objects.select_related('usuario', 'creado_por').all()
        # Filtro simple por búsqueda
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                models.Q(nombres__icontains=q) |
                models.Q(apellidos__icontains=q) |
                models.Q(numero_documento__icontains=q)
            )
        return queryset

# Necesitas importar models para el Q
from django.db import models

# ========== Crear cliente ==========
@login_required
@user_passes_test(es_admin_o_empleado)
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.creado_por = request.user
            cliente.save()

            # Crear notificación automática
            Notificacion.objects.create(
                destinatario=request.user,
                titulo="Cliente registrado",
                mensaje=f"Se registró correctamente al cliente {cliente.nombre_completo}.",
                tipo=Notificacion.Tipo.EXITO
            )

            messages.success(request, f"Cliente {cliente.nombre_completo} registrado correctamente.")
            return redirect('clientes:lista_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/form_cliente.html', {
    'form': form,
    'titulo': 'Registrar Cliente'
    })

# ========== Detalle de cliente ==========
class DetalleClienteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Cliente
    template_name = 'clientes/detalle_cliente.html'
    context_object_name = 'cliente'

    def test_func(self):
        return es_admin_o_empleado(self.request.user)

# ========== Editar cliente ==========
class EditarClienteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form_cliente.html'
    success_url = reverse_lazy('clientes:lista_clientes')

    def test_func(self):
        return es_admin_o_empleado(self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Cliente actualizado correctamente.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        return context

# ========== Eliminar cliente ==========
class EliminarClienteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/eliminar_cliente.html'
    success_url = reverse_lazy('clientes:lista_clientes')
    context_object_name = 'cliente'

    def test_func(self):
        return es_admin_o_empleado(self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Cliente eliminado correctamente.")
        return super().delete(request, *args, **kwargs)