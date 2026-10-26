from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Producto

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})