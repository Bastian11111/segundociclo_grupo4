from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'aplicacionweb/menuprincipal_wiki.html') #El render lo que hace es renderizar la vista, el request es lo que se le envia a la vista, y el nombre de la vista que se va a renderizar

def recuperarcontra(request):
    return render(request, 'aplicacionweb/recuperarcontra.html')

def registrarse(request):
    return render(request, 'aplicacionweb/registrase_wiki.html')

def micuentatf(request):
    return render(request, 'aplicacionweb/micuentatf.html')

def lugares(request):
    return render(request, 'aplicacionweb/lugarestf.html')

def logros(request):
    return render(request, 'aplicacionweb/logros.html')

def iniciosesion(request):
    return render(request, 'aplicacionweb/inicio_sesion_wiki.html')

def historia(request):
    return render(request, 'aplicacionweb/historia.html')

def forowiki(request):
    return render(request, 'aplicacionweb/forowiki.html')

def flora(request):
    return render(request, 'aplicacionweb/flora.html')

def enemigos(request):
    return render(request, 'aplicacionweb/enemigos.html')

def consumibles(request):
    return render(request, 'aplicacionweb/consumibles.html')

def construcciones(request):
    return render(request, 'aplicacionweb/construcciones.html')

def armas(request):
    return render(request, 'aplicacionweb/armas.html')

def animales(request):
    return render(request, 'aplicacionweb/animales.html')




