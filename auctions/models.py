from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Producto(models.Model):
    CATEGORIAS = [
        ('Mesas', 'Mesas'),
        ('Sillas', 'Sillas'),
        ('Cocina', 'Cocina'),
        ('Escritorios', 'Escritorios'),
        ('Otros', 'Otros')
    ]
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen_url = models.URLField(blank=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    categoria = models.CharField(blank=True, choices=CATEGORIAS, max_length=64)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo