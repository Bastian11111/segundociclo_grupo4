from django.db import models

#Estas son importaciones que tenia el profesor en su codigo
from pyexpat import model


# Create your models here.
class Usuario(models.Model):
    emailUsuario = models.CharField(max_length=50, primary_key=True, verbose_name='Email')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    contraseñaUsuario = models.CharField(max_length=50, verbose_name='Contraseña')
    
    def __str__(self):
        return self.nameUsuario
    
    