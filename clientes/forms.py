from django import forms
from .models import Cliente, CuentaBancaria

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombres', 'apellidos', 'tipo_documento', 'numero_documento',
            'fecha_nacimiento', 'telefono', 'email',
            'direccion', 'ciudad', 'departamento', 'estado'
        ]
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento': forms.Select(attrs={'class': 'form-select'}),
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'tipo_documento': 'Tipo de documento',
            'numero_documento': 'Número de documento',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
            'direccion': 'Dirección',
            'ciudad': 'Ciudad',
            'departamento': 'Departamento / Estado',
            'estado': 'Estado del cliente',
        }

class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = ['cliente', 'numero_cuenta', 'tipo_cuenta', 'saldo', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'numero_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_cuenta': forms.Select(attrs={'class': 'form-select'}),
            'saldo': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'cliente': 'Cliente',
            'numero_cuenta': 'Número de cuenta',
            'tipo_cuenta': 'Tipo de cuenta',
            'saldo': 'Saldo inicial',
            'estado': 'Estado de la cuenta',
        }