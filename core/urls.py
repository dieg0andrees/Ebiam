from django.urls import path
from django.conf.urls import handler400, handler403, handler404, handler500
from .views import *
from . import views
urlpatterns = [
    path('',index,name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('service/', listar_servicios, name="service"),
    path('account_locked/', account_locked, name="account_locked"),
    #path('listar_servicios/',listar_servicios, name="listar_servicios"),
]

#Asignar rutas de errores:
handler400 = views.error
handler403 = views.error
handler404 = views.error
handler500 = views.error