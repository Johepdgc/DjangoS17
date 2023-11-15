from django.db import models

# creamos nuestras 4 entidades segun diagrama.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=75)
    Edad = models.IntegerField()
    DUI = models.CharField(max_length=9)

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_del_area = models.CharField(max_length=150)
    Descripcion = models.CharField(max_length=255)

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=75)
    Edad = models.IntegerField()
    AreaId = models.ForeignKey(Area, on_delete=models.CASCADE)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    Fecha_venta = models.DateField()
    Monto = models.FloatField()
    ClienteId = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    EmpleadoId = models.ForeignKey(Empleado, on_delete=models.CASCADE)
