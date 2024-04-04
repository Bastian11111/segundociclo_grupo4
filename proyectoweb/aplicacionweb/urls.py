#CON ESTE SOLO VEMOS HOME

from django.urls import path #Lo primero que hacemos es importar el path
from .views import principal #Lo segundo es importar "home" por ahora solo este, aunque se pueden importar más vistas
from .views import recuperarcontra
from .views import registrarse
from .views import micuentatf
from .views import lugares
from .views import logros
from .views import iniciosesion
from .views import historia
from .views import forowiki
from .views import flora
from .views import enemigos
from .views import consumibles
from .views import construcciones
from .views import armas
from .views import animales

#LLAMA A LAS VISTAS UNA POR UNA (EN ESTE CASO LA PRIMERA))
urlpatterns = [
    path('', principal, name='Principal'), #La primera vista que se llama es home, lo vacio dice que es la vista principal, home es la vista que se llama y el otro home es un alias 
    path('recuperarcontra/', recuperarcontra, name='rcontra'),
    path('registrarse/', registrarse, name='registrarse'),
    path('micuentatf/', micuentatf, name='micuenta'),
    path('lugares/', lugares, name='lugares'),
    path('logros/', logros, name='logros'),
    path('iniciosesion/', iniciosesion, name='iniciosesion'),
    path('historia/', historia, name='historia'),
    path('forowiki/', forowiki, name='forowiki'),
    path('flora/', flora, name='flora'),
    path('enemigos/', enemigos, name='enemigos'),
    path('consumibles/', consumibles, name='consumibles'),
    path('construcciones/', construcciones, name='construcciones'),
    path('armas/', armas, name='armas'),
    path('animales/', animales, name='animales'),
    
    
]
