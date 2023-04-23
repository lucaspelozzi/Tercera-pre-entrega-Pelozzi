
from django.urls import path
from uno import views
from django.shortcuts import render

app_name = 'uno'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('fecha/', views.fecha, name='fecha'),
    path('paginavacia/', views.paginavacia, name='paginavacia'),
    path('template2/', views.template2, name='template2'),
    path('crearanimal/', views.crearanimal, name='crearanimal'),
    path('render/', views.mirender, name='render'),
]