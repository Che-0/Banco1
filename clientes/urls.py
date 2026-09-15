from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ListaClientesView.as_view(), name='lista_clientes'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('<int:pk>/', views.DetalleClienteView.as_view(), name='detalle_cliente'),
    path('<int:pk>/editar/', views.EditarClienteView.as_view(), name='editar_cliente'),
    path('<int:pk>/eliminar/', views.EliminarClienteView.as_view(), name='eliminar_cliente'),
]