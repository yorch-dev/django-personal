from django.shortcuts import render
from .utilidades.erlangc import agentes_requeridos_acd, nivel_servicio


def erlangc(request):
    campos_requeridos = (
        'llamadas',
        'tmo',
        'servicio_requerido',
        'tiempo_objetivo',
        'ocupacion_maxima',
    )

    if request.method == 'GET' and all(campo in request.GET for campo in campos_requeridos):
        parametros = request.GET
        llamadas = float(parametros.get('llamadas', 0))
        tmo = float(parametros.get('tmo', 0))
        servicio_requerido = float(parametros.get('servicio_requerido', 0)) / 100
        tiempo_objetivo = float(parametros.get('tiempo_objetivo', 0))
        ocupacion_maxima = float(parametros.get('ocupacion_maxima', 80)) / 100
        intensidad = llamadas * tmo / 60 / 30
        agentes = agentes_requeridos_acd(
            intensidad,
            tmo,
            servicio_requerido,
            tiempo_objetivo,
            ocupacion_maxima,
        )
        servicio = nivel_servicio(intensidad, agentes, tiempo_objetivo, tmo)
        resultados = f'Agentes requeridos: {agentes:.2f}, Nivel de servicio estimado: {servicio:.2%}'
        context = {
            'llamadas': parametros.get('llamadas', ''),
            'tmo': parametros.get('tmo', ''),
            'servicio_requerido': parametros.get('servicio_requerido', ''),
            'tiempo_objetivo': parametros.get('tiempo_objetivo', ''),
            'ocupacion_maxima': parametros.get('ocupacion_maxima', ''),
            'resultados': resultados,
        }
    else:
        context = {}

    return render(request, 'app_lab/erlangc.html', context)
