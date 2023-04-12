from django.shortcuts import render

from django.shortcuts import render
from .models import MiModelo

def buscar(request):
    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        resultados = MiModelo.objects.filter(campo1__contains=busqueda)
        contexto = {'resultados': resultados}
        return render(request, 'mi_template.html', contexto)
    else:
        return render(request, 'buscar.html')