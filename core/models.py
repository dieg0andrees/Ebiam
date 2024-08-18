from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    imagen_principal = models.ImageField(upload_to='servicios_imagen/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='servicios_imagen_adicionales/')

    def __str__(self):
        return f'Imagen de {self.servicio.nombre}'
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.CharField(max_length=12)
    correo = models.EmailField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.nombre