from django.db import models

#Estas son importaciones que tenia el profesor en su codigo
from pyexpat import model


# Create your models here.

#NOTA: Para las imagenes tuve que instalar "python -m pip install Pillow" para que funcionara

# CLASE PARA REGISTRAR CATEGORIAS: DIFERENCIA USUARIO DE ADMIN
# class Categoria(models.Model):
#     idCategoria = models.AutoField(primary_key=True)
#     nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre')
    
#     def __str__(self):
#         return self.nombreCategoria
    
# class Administrador(models.Model):
#     emailAdministrador = models.CharField(max_length=200, primary_key=True, verbose_name='Email')
#     nombreAdministrador = models.CharField(max_length=50, verbose_name='Nombre')
#     contraseñaAdministrador = models.CharField(max_length=50, verbose_name='Contraseña')
#     avatarAdministrador = models.ImageField(upload_to='administradores', null=True, blank=True)
#     categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='administradores')
    
#     def __str__(self):
#         return self.nombreAdministrador
# CLASE PARA REGISTRAR USUARIOS

class Usuario(models.Model):
    emailUsuario = models.CharField(max_length=200, primary_key=True, verbose_name='Email')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    contraseñaUsuario = models.CharField(max_length=50, verbose_name='Contraseña')
    avatarUsuario = models.ImageField(upload_to='usuarios', null=True, blank=True)
    
    # Cada vez que llamamos a categoria retornamos el nombre de la categoria
    def __str__(self):
        return self.get_code_name()
    
    #Este metodo es para que en el administrador se vea el email al inicio (tuvimos que agregar .get_code_name() al def de arriba)
    def get_code_name(self):
        return f"Email asociado: {self.emailUsuario}"
    

    