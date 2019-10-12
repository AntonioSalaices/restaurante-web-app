from django.db import models

# Create your models here.
class Mesa(models.Model):
    nombre = models.CharField(max_length=40)
    ubicacion= models.CharField(max_length=50)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Pedidos(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    mesa = models.IntegerField()
    orden = models.TextField(max_length=200, default="Orden:")
    total = models.FloatField()
    observacion = models.TextField()

    def __str__(self):
        return self.nombre_cliente + " , en la mesa" + str(self.mesa)
    

