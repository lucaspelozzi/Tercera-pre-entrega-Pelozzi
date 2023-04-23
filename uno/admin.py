from django.contrib import admin
from uno.models import Animal, Persona

# Register your models here.

# admin.site.register(Animal)
# admin.site.register(Persona)

admin.site.register((Animal,Persona))