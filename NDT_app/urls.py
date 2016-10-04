from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^quienes_somos/?$', views.quienes_somos, name='quienes_somos'),
    url(r'^contacto/?$', views.contacto, name='contacto'),
    url(r'^inicio/?$', views.inicio, name='inicio'),
    url(r'^productos/?$', views.productos, name='productos'),
    url(r'$', views.inicio, name='inicio'),

]