from django.urls import path
from .import views
urlpatterns = [
    path('motos', views.motos, name='motos'),
    path('crearmotos', views.crearmotos, name='crearmotos'),
    path('listamotos', views.listamotos, name='listamotos')
]
