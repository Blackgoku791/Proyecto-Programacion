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
