from django.contrib import admin
from .models import *
# Register your models here.

class ImagenServicioInline(admin.TabularInline):
    model = ImagenServicio
    extra = 1

class ServicioAdmin(admin.ModelAdmin):
    inlines = [ImagenServicioInline]  # Incluye las imágenes adicionales en el formulario del servicio

admin.site.register(Servicio, ServicioAdmin)

admin.site.register(Contacto)