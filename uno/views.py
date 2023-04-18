from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from uno.models import Animal

def paginavacia(request):
    return HttpResponse('<h1></h1>')

def iniciopagina(request):
    return HttpResponse('<h1>Hola web</h1>')

# version con Httpresponse

def fecha(request):
    dt = datetime.now()
    dtconformato = dt.strftime("%A %d %B %Y %I:%M")
    # datos = {'fecha': dtconformato}
    # template = loader.get_template(r'template.html')
    return HttpResponse(dtconformato)

def saludo(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre} {apellido}</h1>')

# def template1(request):
#     archivo = open(r'C:\Users\KILLL\Desktop\Carpeta de CODER\Proyecto\templates\template1.html', 'r')
#     template = template(archivo.read())
#     archivo.close()
#     contexto = Context()
#     templaterenderizado = template.render(contexto)
#     return HttpResponse(templaterenderizado)

def template2(request):
    datos = {
        'nombre': 'Lucas',
        'apellido': 'Pelozzi',
        'edad': 4,
        'anios' : [
            1889, 1982
        ]   
    }
    
    template = loader.get_template(r'template2.html')
    templaterenderizado = template.render(datos)
    return HttpResponse(templaterenderizado)

def crearanimal(request):
    animal = Animal(nombre='Tomi', edad=15)
    print(animal.nombre)
    print(animal.edad)
    animal.save()
    datos = {'animal': animal}
    template = loader.get_template(r'crearanimal.html')
    templaterenderizado = template.render(datos)
    return HttpResponse(templaterenderizado)