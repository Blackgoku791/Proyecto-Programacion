import re


def _informe(salida, nombre):
    inicio = salida.index("Informe del sector " + nombre)
    resto = salida[inicio:]
    fin = resto.find("\n=====")
    return resto if fin == -1 else resto[:fin]


def _numero(texto, etiqueta):
    return int(re.search(etiqueta + r": (\d+)", texto).group(1))


def comprobar(salida):
    azar = _informe(salida, "Azar")
    if _numero(azar, "Días registrados") != 3:
        return "Azar debería tener 3 días registrados"
    total = _numero(azar, "Visitantes totales")
    if not 52 + 2 * 40 <= total <= 52 + 2 * 80:
        return f"Los dos días simulados de Azar deben sumar entre 80 y 160 (total {total})"
    if "Último día registrado: 2026-11-03" not in azar:
        return "Los días simulados deben agregarse a continuación del registrado"
    moneda = _informe(salida, "Moneda")
    baja = _numero(moneda, "Días en presión baja")
    saturacion = _numero(moneda, "Días en saturación")
    if _numero(moneda, "Días registrados") != 200 or baja + saturacion != 200:
        return "Con capacidad 1 y rango 0 a 1 todos los días deben quedar en baja o en saturación"
    if baja == 0 or saturacion == 0:
        return "En 200 días con rango 0 a 1 deben aparecer los dos extremos (mínimo y máximo incluidos)"
    return None
