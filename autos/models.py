from django.db import models

# Create your models here.
#    2.    Definir un modelo Auto con los siguientes campos:

#    •    marca (char, máx. 50 caracteres)

#    •    modelo (char, máx. 50 caracteres)

#    •    año (entero)

#    •    precio (decimal, 10,2)


class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"