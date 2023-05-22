from django.db import models
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=255, blank=True)
    imagen = models.ImageField(upload_to='photos/categoria', blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.nombre