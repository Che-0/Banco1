# Sistema Bancario - Documentación

## 1. Descripción del Proyecto

Sistema web de gestión bancaria desarrollado con Django. Permite la administración de usuarios, clientes, cuentas bancarias, transferencias, notificaciones y reportes.

## 2. Funcionalidades Principales

- Inicio de sesión con roles (Administrador, Empleado, Cliente)
- Administración de usuarios
- Registro y gestión de clientes
- Creación automática de cuentas bancarias
- Portal del cliente (consulta de saldo y movimientos)
- Transferencias entre cuentas
- Sistema de notificaciones
- Reportes (clientes y transferencias) + exportación a Excel
- Foto de perfil para clientes

## 3. Roles del Sistema

| Rol | Permisos |
|-----|----------|
| **Administrador** | Acceso total: usuarios, clientes, reportes, notificaciones |
| **Empleado** | Gestión de clientes y reportes |
| **Cliente** | Ver su cuenta, saldo, realizar transferencias y cambiar su foto |

## 4. Estructura de la Base de Datos

### User (accounts_user)
Cuenta de acceso al sistema. Contiene usuario, contraseña, rol y datos básicos.

### Cliente (clientes_cliente)
Registro de la persona en el banco. Puede estar vinculado a un User.

### CuentaBancaria (clientes_cuentabancaria)
Cuenta bancaria asociada a un Cliente. Contiene número de cuenta y saldo.

### Transferencia (clientes_transferencia)
Registro de movimientos entre cuentas.

### Notificacion (notificaciones_notificacion)
Mensajes internos del sistema para los usuarios.

## 5. Tecnologías Utilizadas

- Python / Django
- Bootstrap 5
- SQLite (desarrollo) / PostgreSQL (producción)
- openpyxl (exportación Excel)
- WhiteNoise + Gunicorn (despliegue)

## 6. Instalación Local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver