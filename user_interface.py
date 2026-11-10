"""Interfaz de consola de la Reserva Natural Bahía Coralina."""

"""Interfaz de consola de la Reserva Natural Bahía Coralina (Alternativa B).

Lee lo que teclea la persona, llama a business_logic.py y muestra los resultados.
Para ejecutarlo:  python user_interface.py

Dos variables de entorno existen solo para poder verificar el programa con
casos automáticos; sin ellas el programa se comporta como siempre:
  FECHA_ACTUAL_PRUEBA=AAAA-MM-DD  usa esa fecha como "hoy" (requisito 9).
  ECO_ENTRADA=1                   repite en pantalla lo que se lee, para que la
                                  salida se vea como una sesión de terminal.
"""
import os
from datetime import date
from business_logic import (Reserva, leer_lineas, cantidad_texto, SATURACION,
                            MENSAJE_FIN_CALENDARIO)
MENU = """
===== Reserva Natural Bahía Coralina =====
1. Crear un sector
2. Registrar los visitantes del día siguiente
3. Simular días
4. Ver el informe de un sector
5. Ver el sector con el porcentaje de uso más alto y el más bajo
6. Cargar los sectores y los visitantes desde archivos
7. Salir"""
if __name__ == "__main__":
    main()

def leer(mensaje):
    """Muestra el mensaje y lee una línea. Con ECO_ENTRADA=1 la repite en pantalla."""
    texto = input(mensaje)
    if os.environ.get("ECO_ENTRADA") == "1":
        print(texto)
    return texto

def pedir_sector(reserva):
    """Lee el nombre de un sector y lo busca. Si no existe lo avisa y devuelve None."""
    nombre = leer("Nombre del sector: ")
    sector = reserva.buscar_sector(nombre)
    if sector is None:
        print("No hay un sector con ese nombre.")
    return sector

def opcion_crear_sector(reserva):
    nombre = leer("Nombre del sector: ")
    capacidad = leer("Capacidad de carga (visitantes por día): ")
    anio = leer("Año de inicio del registro: ")
    mes = leer("Mes de inicio del registro: ")
    dia = leer("Día de inicio del registro: ")
    sector, mensaje = reserva.crear_sector(nombre, capacidad, anio, mes, dia)
    if sector is None:
        print(mensaje)
    else:
        print(f"Sector creado: {sector.nombre} (capacidad de carga: "
              f"{cantidad_texto(sector.capacidad, 'visitante', 'visitantes')}, "
              f"inicio del registro: {sector.fecha_inicio}). "
              "Todavía no tiene días registrados.")

def main():
    reserva = Reserva()
    opcion = ""
    try:
        while opcion != "7":
            print(MENU)
            opcion = leer("Elija una opción: ").strip()
            if opcion == "1":
                opcion_crear_sector(reserva)
            elif opcion == "7":
                print("Hasta luego.")
            else:
                print("La opción no es válida.")
    except EOFError:
        print()
        print("Se terminó la entrada de datos. El programa termina.")


if __name__ == "__main__":
    main()
