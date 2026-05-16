from django.contrib import admin
from django import forms
from django.db import models
from .models import Categoria, Habitacion, Articulo, Compra

admin.site.register(Categoria)
admin.site.register(Habitacion)

class NumberFormatAdminMixin(admin.ModelAdmin):
    formfield_overrides = {
        models.IntegerField: {'widget': forms.TextInput(attrs={'class': 'js-number-with-dots'})},
    }

    class Media:
        js = ('js/admin-number-format.js',)

class ArticuloAdmin(NumberFormatAdminMixin):
    list_display = ('nombre', 'precio_referencia_formateado', 'vida_util_referencia_meses', 'categoria', 'habitacion')
    
    def precio_referencia_formateado(self, obj):
        return f"{obj.precio_referencia:,}".replace(",", ".")
    precio_referencia_formateado.short_description = 'Precio Referencia'

class CompraAdmin(NumberFormatAdminMixin):
    pass

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Compra, CompraAdmin)
