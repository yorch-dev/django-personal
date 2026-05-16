from django.shortcuts import render
from .models import Categoria, Habitacion, Articulo, Compra
from dateutil.relativedelta import relativedelta

def index(request):
    return render(request, 'app_finanzas_personales/index_finanzas_personales.html')

# quiero mostrar un resumen de las compras realizadas, agrupadas por categoría y habitación, con el total gastado en cada una
def resumen_compras(request):
    # Obtener todas las compras con su información relacionada
    compras = Compra.objects.select_related('articulo__categoria', 'articulo__habitacion').all()
    resumen = []
    
    for compra in compras:
        # Calcular fecha aproximada de reemplazo
        fecha_reemplazo_aprox = None
        if compra.fecha_compra and compra.articulo.vida_util_referencia_meses:
            fecha_reemplazo_aprox = compra.fecha_compra + relativedelta(months=compra.articulo.vida_util_referencia_meses)
        
        resumen.append({
            'categoria': compra.articulo.categoria.nombre,
            'habitacion': compra.articulo.habitacion.nombre,
            'articulo': compra.articulo.nombre,
            'fecha_compra': compra.fecha_compra,
            'precio_compra': f"{compra.precio_compra:,}".replace(",", "."),
            'fecha_reemplazo_aprox': fecha_reemplazo_aprox,
        })
    
    # Calcular costo mensual por artículo (como "arriendo")
    articulos = Articulo.objects.all()
    costo_mensual_articulos = []
    total_mensual = 0
    
    for articulo in articulos:
        if articulo.vida_util_referencia_meses > 0:
            costo_mensual = articulo.precio_referencia / articulo.vida_util_referencia_meses
            total_mensual += costo_mensual
            costo_mensual_articulos.append({
                'nombre': articulo.nombre,
                'categoria': articulo.categoria.nombre,
                'habitacion': articulo.habitacion.nombre,
                'precio_referencia': f"{articulo.precio_referencia:,}".replace(",", "."),
                'vida_util_meses': articulo.vida_util_referencia_meses,
                'costo_mensual': f"{costo_mensual:,.0f}".replace(",", "."),
            })
    
    total_mensual_formateado = f"{total_mensual:,.0f}".replace(",", ".")
    
    return render(request, 'app_finanzas_personales/resumen_compras.html', {
        'resumen': resumen,
        'costo_mensual_articulos': costo_mensual_articulos,
        'total_mensual': total_mensual_formateado,
    })