from django.db import models

# Create your models here.

#USUARIOS PARA LOGIN
class Usuarios (models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Edad = models.IntegerField
    Correo = models.EmailField
    Contra = models.CharField(max_length=20)


