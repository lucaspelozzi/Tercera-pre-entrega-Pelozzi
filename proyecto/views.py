from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
def iniciopagina(request):
    return HttpResponse('<h1>Hola web</h1>')

def fecha(request):
    dt = datetime.now()
    dt_formato = dt.strftime("%A %d %B %Y %I:%M")
    return HttpResponse(f'<p>{dt_formato}</p>')

def saludo(request, nombre, apellido):
    return HttpResponse(f'<h1>Hola {nombre}{apellido}</h1>')

def template(request):
    
    archivo = open(r'C:\Users\KILLL\Desktop\Carpeta de CODER\Proyecto\templates\template.html', 'r')
    
    template = Template(archivo.read())
    
    archivo.close()
    
    contexto = Context()
    
    templaterenderizado = template.render(contexto)
    
    return HttpResponse(templaterenderizado)