# SP Factory

Aplicación web de catálogo para una tienda de componentes de computador, desarrollada con Django. Permite explorar productos, consultar sus detalles y administrar el catálogo desde el panel de administración.

## Funcionalidades

- Página principal con catálogo de productos e imágenes.
- Página de detalle con categoría, marca, precio y descripción.
- Administración de productos y categorías desde Django Admin.
- Búsqueda y filtros de productos en el panel de administración.
- Interfaz adaptable con Bootstrap 5.3 y estilos propios.

> El proyecto implementa un catálogo; no incluye carrito de compras ni procesamiento de pagos.

## Tecnologías

- Python 3.10 o superior
- Django 5.2
- SQLite
- Pillow para el manejo de imágenes
- Bootstrap 5.3 (cargado desde CDN)

Las dependencias de Python están fijadas en [`requirements.txt`](requirements.txt).

## Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <CARPETA_DEL_REPOSITORIO>
```

### 2. Crear y activar un entorno virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias y preparar la base de datos

```bash
python -m pip install -r requirements.txt
python manage.py migrate
```

### 4. Crear un usuario administrador

```bash
python manage.py createsuperuser
```

Sigue las indicaciones para definir el nombre de usuario y la contraseña.

### 5. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Abre <http://127.0.0.1:8000/> para ver la tienda y <http://127.0.0.1:8000/admin/> para administrar el catálogo. Desde el panel, crea primero las categorías y luego agrega productos. Las imágenes se pueden cargar al editar cada producto.

## Estructura del proyecto

```text
config/        Configuración y rutas principales de Django
tienda/        Modelos, vistas, administración y migraciones
templates/     Plantillas del catálogo y detalle de producto
static/        Estilos CSS
media/         Imágenes de productos
db.sqlite3     Base de datos SQLite local
manage.py      Herramienta de administración de Django
```

## Pruebas

Ejecuta las pruebas de la aplicación con:

```bash
python manage.py test
```

## Consideraciones para producción

La configuración incluida está preparada para desarrollo local. Antes de publicar el sitio, configura una clave secreta mediante variables de entorno, desactiva `DEBUG`, define `ALLOWED_HOSTS` para el dominio y sigue la [lista de verificación de despliegue de Django](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/). También debes configurar el servicio de archivos estáticos y de medios para el entorno de despliegue; el proyecto sirve las imágenes subidas localmente solo durante el desarrollo.
