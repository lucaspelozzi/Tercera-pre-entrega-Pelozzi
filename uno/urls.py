
from django.urls import path
from uno import views
from django.shortcuts import render

app_name = 'uno'

urlpatterns = [
    path('', views.inicio),
    path('paginavacia/', views.paginavacia),
    path('fecha/', views.fecha),
    path('saludo/<str:nombre>/<str:apellido>/', views.saludo),
    path('template1/', views.template1),
    path('template2/', views.template2),
    path('crearanimal/', views.crearanimal),
    path('render/', views.mirender),
]