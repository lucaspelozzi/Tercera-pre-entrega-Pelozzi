
from django.urls import path
from uno import views


urlpatterns = [
    path('', views.paginavacia),
    path('iniciopagina/', views.iniciopagina),
    path('fecha/', views.fecha),
    path('saludo/<str:nombre>/<str:apellido>/', views.saludo),
    # path('template1/', views.template1),
    path('template2/', views.template2),
    path('crearanimal/', views.crearanimal),
]