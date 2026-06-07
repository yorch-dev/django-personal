from math import exp, lgamma


def agentes_requeridos_acd(intensidad, tmo, servicio_requerido,
                           tiempo_objetivo, ocupacion_maxima
                           ):
    agentes = 0
    if intensidad > 0:
        min_agentes = 1
        agentes = min_agentes
        while (
            nivel_servicio(intensidad, agentes, tiempo_objetivo, tmo) < servicio_requerido
            or utilizacion(intensidad, agentes) > ocupacion_maxima
        ):
            agentes += 1
        while (
            nivel_servicio(intensidad, agentes - 0.1, tiempo_objetivo, tmo) >= servicio_requerido
            and utilizacion(intensidad, agentes - 0.1) <= ocupacion_maxima
        ):
            agentes -= 0.1
        return agentes
    else:
        return agentes


def nivel_servicio(intensidad, agentes, objetivo, tmo):
    try:
        nivel_servicio = 1 - (erlang_c(intensidad, agentes) * exp(-(agentes - intensidad) * objetivo / tmo))
        if intensidad == 0:
            nivel_servicio = 1
    except Exception:
        nivel_servicio = 0
    if nivel_servicio > 1:
        nivel_servicio = 1
    if nivel_servicio < 0:
        nivel_servicio = 0
    return nivel_servicio


def erlang_c(intensidad, agentes):
    try:
        erlang_c = (numerador(intensidad, agentes)) / ((numerador(intensidad, agentes)) + ((1 - utilizacion(intensidad, agentes)) * erlang_b(intensidad, agentes)))
    except Exception:
        erlang_c = 0
    if intensidad == 0:
        erlang_c = 0
    if erlang_c > 1:
        erlang_c = 1
    return erlang_c


def utilizacion(intensidad, agentes):
    try:
        utilizacion = intensidad / agentes
    except Exception:
        utilizacion = 0
    if utilizacion < 0:
        utilizacion = 0
    if utilizacion > 1:
        utilizacion = 1
    return utilizacion


def numerador(intensidad, agentes):
    return (intensidad ** agentes) / exp(gamma_ln(agentes + 1))


def erlang_b(intensidad, agentes):
    respuesta = 0
    for k in range(0, int(agentes)):
        respuesta += 1 * ((intensidad ** k) / exp(gamma_ln(k + 1)))
    return respuesta


def gamma_ln(n):
    return lgamma(n)
