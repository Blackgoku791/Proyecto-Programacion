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

def main():
    reserva = Reserva()
    opcion = ""
    try:
        while opcion != "7":
            print(MENU)
            opcion = leer("Elija una opción: ").strip()
            elif opcion == "7":
                print("Hasta luego.")
            else:
                print("La opción no es válida.")
    except EOFError:
        print()
        print("Se terminó la entrada de datos. El programa termina.")


if __name__ == "__main__":
    main()
