from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from uno.models import Animal
from django.shortcuts import render


def paginavacia(request):
    return render(request, r'uno/paginavacia.html')

def inicio(request):
    # return HttpResponse('<h1>Inicio</h1>')
    # datos = {'nombre': 'Lucas', 'apellido':'Pelozzi', 'fecha_nacimiento': '1982'}
    return render(request, r'uno/index.html')

# version con Httpresponse

def fecha(request):
    dt = datetime.now()
    dtconformato = dt.strftime("%A %d %B %Y %I:%M")
    # datos = {'fecha': dtconformato}
    # template = loader.get_template(r'template.html')
    return HttpResponse(dtconformato)

def saludo(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre} {apellido}</h1>')

def template2(request):
    datos = {
        'nombre': 'Lucas',
        'apellido': 'Pelozzi',
        'edad': 4,
        'anios' : [
            1889, 1982
        ]   
    }
    
    template = loader.get_template(r'uno/template2.html')
    templaterenderizado = template.render(datos)
    return HttpResponse(templaterenderizado)

def crearanimal(request):
    animal = Animal(nombre='Kity', edad=17)
    print(animal.nombre)
    print(animal.edad)
    animal.save()
    datos = {'animal': animal}
    template = loader.get_template(r'uno/crearanimal.html')
    templaterenderizado = template.render(datos)
    return HttpResponse(templaterenderizado)

def mirender(request):
    datos = {'nombre': 'Lucas', 'apellido':'Pelozzi', 'fecha_nacimiento': '1982'}
    # template = loader.get_template(r'mirender.html')
    # templaterenderizado = template.render(datos)
    # return HttpResponse(templaterenderizado)

    return render(request, r'uno/render.html', datos)
    