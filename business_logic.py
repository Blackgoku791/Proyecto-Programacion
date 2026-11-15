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

def fecha_siguiente(self):
        """Fecha del día que sigue en el registro, o None si ya no cabe otro."""
        if self.dias_que_caben() <= 0:
            return None
        return self.fecha_del_dia(len(self.visitantes))

def validar_visitantes(self, texto):
        """Devuelve (visitantes, None) o (None, mensaje de error)."""
        visitantes = convertir_entero(texto)
        if visitantes is None:
            return None, "Los visitantes deben ser un número entero."
        if visitantes < 0 or visitantes > self.capacidad:
            return None, f"Los visitantes van de 0 a {self.capacidad}."
        return visitantes, None

def registrar_dia(self, visitantes):
        """Agrega un día ya validado al final del registro."""
        self.visitantes.append(visitantes)

def validar_dias_a_simular(self, texto):
        """Devuelve (dias, None) o (None, mensaje de error)."""
        dias = convertir_entero(texto)
        if dias is None:
            return None, "El número de días debe ser un número entero."
        if dias < 1:
            return None, "Se debe simular al menos un día."
        caben = self.dias_que_caben()
        if caben <= 0:
            return None, MENSAJE_FIN_CALENDARIO
        if dias > caben:
            return None, ("El calendario solo permite registrar "
                          f"{cantidad_texto(caben, 'día', 'días')} más en este sector.")
        return dias, None

def validar_minimo_y_maximo(self, minimo, maximo):
        """Devuelve un mensaje de error, o None si el mínimo no pasa del máximo."""
        if minimo > maximo:
            return "El mínimo no puede ser mayor que el máximo."
        return None

def simular_dias(self, dias, minimo, maximo, generador=random):
        """Agrega días con un número de visitantes al azar entre minimo y maximo."""
        for _ in range(dias):
            self.visitantes.append(generador.randint(minimo, maximo))

def dias_que_caben(self):
        """Cuántos días más se pueden registrar antes de salirse del calendario."""
        hasta_el_final = (date.max - self.fecha_inicio).days + 1
        return hasta_el_final - len(self.visitantes)

def visitantes_totales(self):
        total = 0
        for cantidad in self.visitantes:
            total = total + cantidad
        return total

def promedio(self):
        return self.visitantes_totales() / len(self.visitantes)

def porcentaje_uso(self):
        """Promedio entre capacidad por 100, calculado con una sola división."""
        return self.visitantes_totales() * 100 / (len(self.visitantes) * self.capacidad)

def desviacion_estandar(self):
        promedio = self.promedio()
        suma_cuadrados = 0
        for cantidad in self.visitantes:
            diferencia = cantidad - promedio
            suma_cuadrados = suma_cuadrados + diferencia ** 2
        return math.sqrt(suma_cuadrados / len(self.visitantes))

def fecha_dia_con_mas_visitantes(self):
        """Fecha del primer día con el máximo de visitantes."""
        posicion = 0
        for i in range(1, len(self.visitantes)):
            if self.visitantes[i] > self.visitantes[posicion]:
                posicion = i
        return self.fecha_del_dia(posicion)

def fecha_dia_con_menos_visitantes(self):
        """Fecha del primer día con el mínimo de visitantes."""
        posicion = 0
        for i in range(1, len(self.visitantes)):
            if self.visitantes[i] < self.visitantes[posicion]:
                posicion = i
        return self.fecha_del_dia(posicion)

def nivel_de_presion(self, visitantes):
        """Nivel de presión de un día, comparando con enteros (sin decimales)."""
        ocupado = visitantes * 100
        if ocupado >= 90 * self.capacidad:
            return SATURACION
        if ocupado >= 75 * self.capacidad:
            return ALTA
        if ocupado >= 50 * self.capacidad:
            return MODERADA
        return BAJA

def dias_por_nivel(self):
        """Lista de cuatro conteos, en el orden baja, moderada, alta, saturación."""
        conteos = [0, 0, 0, 0]
        for cantidad in self.visitantes:
            conteos[self.nivel_de_presion(cantidad)] += 1
        return conteos

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
