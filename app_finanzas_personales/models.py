from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Habitacion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Artículo')
    precio_referencia = models.IntegerField()
    vida_util_referencia_meses = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['categoria', 'nombre']
        verbose_name_plural = 'Artículos'

class Compra(models.Model):
    ESTADO_CHOICES = [
        ('en_uso', 'En Uso'),
        ('desecho', 'Desecho'),
    ]
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    precio_compra = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    fecha_reemplazo = models.DateField(blank=True, null=True, verbose_name='Fecha de Reemplazo Forzado')
    fecha_baja = models.DateField(blank=True, null=True, verbose_name='Fecha de Baja')
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='en_uso')

    def __str__(self):
        return self.articulo.nombre
    
    class Meta:
        ordering = ['articulo', 'fecha_compra']
        verbose_name_plural = 'Compras'