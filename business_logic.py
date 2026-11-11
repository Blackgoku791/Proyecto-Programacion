"""Lógica del negocio de la Reserva Natural Bahía Coralina."""

"""Lógica del negocio de la Reserva Natural Bahía Coralina (Alternativa B).

Este archivo no lee del teclado ni escribe en pantalla: solo guarda los datos
de los sectores y calcula los indicadores. Los mensajes de error que devuelven
sus métodos los muestra user_interface.py.
"""
import math
import random
from datetime import date, timedelta
BAJA = 0
MODERADA = 1
ALTA = 2
SATURACION = 3
MENSAJE_FIN_CALENDARIO = ("El registro de este sector ya llegó al último día "
                          "que permite el calendario.")

def convertir_entero(texto):
    """Convierte un texto en un número entero, o devuelve None si no lo es.

    Acepta espacios al principio y al final y un signo + o - delante. Solo
    acepta los dígitos del 0 al 9 (int() de Python aceptaría también guiones
    bajos o dígitos de otros alfabetos, y aquí no queremos eso).
    """
    texto = texto.strip()
    cuerpo = texto
    if len(texto) > 0 and texto[0] in "+-":
        cuerpo = texto[1:]
    if cuerpo == "":
        return None
    for caracter in cuerpo:
        if caracter not in "0123456789":
            return None
    return int(texto)

def crear_fecha(anio_texto, mes_texto, dia_texto):
    """Devuelve la fecha del calendario, o None si no es una fecha válida."""
    anio = convertir_entero(anio_texto)
    mes = convertir_entero(mes_texto)
    dia = convertir_entero(dia_texto)
    if anio is None or mes is None or dia is None:
        return None
    try:
        return date(anio, mes, dia)
    except (ValueError, OverflowError):
        return None

def cantidad_texto(cantidad, singular, plural):
    """Escribe una cantidad con su unidad: '1 día' o '3 días'."""
    if cantidad == 1:
        return f"{cantidad} {singular}"
    return f"{cantidad} {plural}"

class Sector:
def __init__(self, nombre, capacidad, fecha_inicio):
        self.nombre = nombre
        self.capacidad = capacidad
        self.fecha_inicio = fecha_inicio
        self.visitantes = []

def dias_registrados(self):
        return len(self.visitantes)

def fecha_del_dia(self, posicion):
        return self.fecha_inicio + timedelta(days=posicion)

class Reserva:
def __init__(self):
        self.sectores = []

def esta_vacia(self):
        return len(self.sectores) == 0

def buscar_sector(self, nombre):
        """Busca por nombre exacto (mayúsculas y tildes cuentan), sin espacios
        al principio ni al final. Devuelve el sector o None."""
        nombre = nombre.strip()
        for sector in self.sectores:
            if sector.nombre == nombre:
                return sector
        return None

def crear_sector(self, nombre, capacidad_texto, anio_texto, mes_texto, dia_texto):
        """Crea y guarda un sector. Devuelve (sector, None) o (None, mensaje).

        Revisa las condiciones en orden y se detiene en la primera que falla.
        """
        nombre = nombre.strip()
        if nombre == "":
            return None, "El nombre no puede estar vacío."
        if self.buscar_sector(nombre) is not None:
            return None, "Ya existe un sector con ese nombre."
        capacidad = convertir_entero(capacidad_texto)
        if capacidad is None:
            return None, "La capacidad de carga debe ser un número entero."
        if capacidad < 1:
            return None, "La capacidad de carga debe ser de al menos un visitante."
        fecha = crear_fecha(anio_texto, mes_texto, dia_texto)
        if fecha is None:
            return None, "La fecha no es válida."
        sector = Sector(nombre, capacidad, fecha)
        self.sectores.append(sector)
        return sector, None
