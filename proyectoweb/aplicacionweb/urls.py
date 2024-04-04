#CON ESTE SOLO VEMOS HOME

from django.urls import path #Lo primero que hacemos es importar el path
from .views import home #Lo segundo es importar "home" por ahora solo este, aunque se pueden importar más vistas

#LLAMA A LAS VISTAS UNA POR UNA (EN ESTE CASO LA PRIMERA))
urlpatterns = [
    path('', home, name='home'), #La primera vista que se llama es home, lo vacio dice que es la vista principal, home es la vista que se llama y el otro home es un alias 
]
