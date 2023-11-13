from django.db import models

class Cliente(models.Model):
    dni = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dias_restantes = models.IntegerField()
    monto_ingresado = models.DecimalField(max_digits=10)
    