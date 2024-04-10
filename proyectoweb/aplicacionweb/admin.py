from django.contrib import admin

#Se importa el modelo Usuario
from .models import Usuario 



# Register your models here.

#Esto es para que se pueda ver el modelo Usuario en el administrador de Django y este los pueda manipular
admin.site.register(Usuario)


