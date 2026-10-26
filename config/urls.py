from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tienda.views import home, detalle_producto

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('producto/<int:id>/', detalle_producto, name='detalle_producto'),
]

# Esto es para trabajar de forma local.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)