from django.contrib import admin
from .models import Categoria, Producto
from django.utils.html import format_html

admin.site.site_header = "SP Factory Admin"
admin.site.site_title = "SP Factory Admin"
admin.site.index_title = "Bienvenido al panel de administración de SP Factory"

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'precio_formateado', 'categoria', 'imagen_modificada')
    readonly_fields = ('imagen_modificada',)
    search_fields = ('nombre',)
    list_filter = ('marca', 'categoria')

    @admin.display(description='Precio')
    def precio_formateado(self, obj):
        return f"${obj.precio:,}".replace(',', '.')

    @admin.display(description='Imagen')
    def imagen_modificada(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:4px;">',
                obj.imagen.url
            )
        return '-'