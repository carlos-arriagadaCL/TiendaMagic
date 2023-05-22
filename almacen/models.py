from django.db import models
from django.urls import reverse
from categoria.models import Categoria

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=2000, blank=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='photos/productos')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.categoria.slug, self.slug])

    def __str__(self):
        return self.nombre

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='tamaño', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('tamaño', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()
    class Meta:
        verbose_name = 'Variación'
        verbose_name_plural = 'Variaciones'

    def __str__(self):
        return self.variation_value