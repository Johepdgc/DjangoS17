from django.shortcuts import render
from .models import Cliente, Area, Empleado, Venta

# juntamos todas las tablas en una misma view con su respectiva template mencionando las entidades.
def all_lists(request):
    cliente = Cliente.objects.all()
    area = Area.objects.all()
    empleado = Empleado.objects.all()
    venta = Venta.objects.all()
    return render(request, 'all_lists.html', {'cliente': cliente, 'area': area, 'empleado': empleado, 'venta': venta})
