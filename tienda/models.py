from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=32)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    marca = models.CharField(max_length=32)
    precio = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_DEFAULT, default='Sin Categoría')

    def __str__(self):
        return self.nombre