from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'aplicacionweb/Animales.html') #El render lo que hace es renderizar la vista, el request es lo que se le envia a la vista, y el nombre de la vista que se va a renderizar