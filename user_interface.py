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

def opcion_registrar_dia(reserva):
    sector = pedir_sector(reserva)
    if sector is None:
        return
    fecha = sector.fecha_siguiente()
    if fecha is None:
        print(MENSAJE_FIN_CALENDARIO)
        return
    print(f"El día que sigue en el registro es {fecha}.")
    visitantes = None
    while visitantes is None:
        texto = leer(f"Visitantes del día {fecha}: ")
        visitantes, mensaje = sector.validar_visitantes(texto)
        if visitantes is None:
            print(mensaje)
    sector.registrar_dia(visitantes)
    print(f"Se registró el día {fecha} con "
          f"{cantidad_texto(visitantes, 'visitante', 'visitantes')}.")

def opcion_simular_dias(reserva):
    sector = pedir_sector(reserva)
    if sector is None:
        return
    # Cada dato se revisa apenas se lee; si falla, se vuelve al menú sin leer los demás.
    dias, mensaje = sector.validar_dias_a_simular(leer("Número de días a simular: "))
    if dias is None:
        print(mensaje)
        return
    minimo, mensaje = sector.validar_visitantes(leer("Visitantes mínimos: "))
    if minimo is None:
        print(mensaje)
        return
    maximo, mensaje = sector.validar_visitantes(leer("Visitantes máximos: "))
    if maximo is None:
        print(mensaje)
        return
    mensaje = sector.validar_minimo_y_maximo(minimo, maximo)
    if mensaje is not None:
        print(mensaje)
        return
    sector.simular_dias(dias, minimo, maximo)
    print(f"Se simularon {cantidad_texto(dias, 'día', 'días')} "
          f"en el registro de {sector.nombre}.")

def mostrar_informe(sector, hoy):
    print(f"Informe del sector {sector.nombre}")
    print("Capacidad de carga: "
          f"{cantidad_texto(sector.capacidad, 'visitante', 'visitantes')}")
    if sector.dias_registrados() == 0:
        print("El sector no tiene días registrados.")
        return
    print(f"Días registrados: {sector.dias_registrados()}")
    print(f"Visitantes totales: {sector.visitantes_totales()}")
    print(f"Promedio de visitantes por día: {round(sector.promedio(), 2)}")
    print(f"Porcentaje de uso: {round(sector.porcentaje_uso(), 2)} %")
    print("Desviación estándar de los visitantes: "
          f"{round(sector.desviacion_estandar(), 2)}")
    print(f"Día con más visitantes: {sector.fecha_dia_con_mas_visitantes()}")
    print(f"Día con menos visitantes: {sector.fecha_dia_con_menos_visitantes()}")
    baja, moderada, alta, saturacion = sector.dias_por_nivel()
    print(f"Días en presión baja: {baja}")
    print(f"Días en presión moderada: {moderada}")
    print(f"Días en presión alta: {alta}")
    print(f"Días en saturación: {saturacion}")
    largo, inicio = sector.racha_mas_larga_en_saturacion()
    if largo == 0:
        print("Racha más larga en saturación: el sector no tuvo ningún día en saturación.")
    else:
        print("Racha más larga en saturación: "
              f"{cantidad_texto(largo, 'día', 'días')}, desde el {inicio}")
    print(f"Último día registrado: {sector.fecha_ultimo_dia()}")
    faltan, primero, ultimo = sector.dias_sin_registrar(hoy)
    if faltan == 0:
        print("El registro está al día.")
    elif faltan == 1:
        print(f"Días por registrar: 1, el {primero}")
    else:
        print(f"Días por registrar: {faltan}, del {primero} al {ultimo}")

def opcion_informe(reserva):
    sector = pedir_sector(reserva)
    if sector is not None:
        mostrar_informe(sector, obtener_fecha_actual())

def obtener_fecha_actual():
    """La fecha del computador, o la de FECHA_ACTUAL_PRUEBA si está definida."""
    texto = os.environ.get("FECHA_ACTUAL_PRUEBA")
    if texto:
        try:
            return date.fromisoformat(texto)
        except ValueError:
            pass
    return date.today()

def opcion_uso_extremo(reserva):
    mayor, menor = reserva.sectores_con_uso_extremo()
    if mayor is None:
        print("Ningún sector tiene días registrados.")
        return
    print("Sector con el porcentaje de uso más alto: "
          f"{mayor.nombre} ({round(mayor.porcentaje_uso(), 2)} %)")
    print("Sector con el porcentaje de uso más bajo: "
          f"{menor.nombre} ({round(menor.porcentaje_uso(), 2)} %)")

def mostrar_cargados(cantidad, singular, plural):
    if cantidad == 1:
        print(f"Se cargó 1 {singular}.")
    else:
        print(f"Se cargaron {cantidad} {plural}.")

def mostrar_descartes(descartes):
    for numero, causa in descartes:
        print(f"Línea {numero} descartada: {causa}")

def opcion_cargar_archivos(reserva):
    if not reserva.esta_vacia():
        print("La carga solo se hace con el programa sin sectores.")
        return
    ruta_sectores = leer("Ruta del archivo de sectores: ").strip()
    lineas, error = leer_lineas(ruta_sectores)
    if lineas is None:
        print(error)
        return
    cargados, descartes = reserva.cargar_sectores(lineas)
    mostrar_descartes(descartes)
    mostrar_cargados(cargados, "sector", "sectores")

    ruta_visitantes = leer("Ruta del archivo de visitantes: ").strip()
    lineas, error = leer_lineas(ruta_visitantes)
    if lineas is None:
        print(error)
        return
    cargados, descartes = reserva.cargar_visitantes(lineas)
    mostrar_descartes(descartes)
    mostrar_cargados(cargados, "día", "días")

def main():
    reserva = Reserva()
    opcion = ""
    try:
        while opcion != "7":
            print(MENU)
            opcion = leer("Elija una opción: ").strip()
            if opcion == "1":
                opcion_crear_sector(reserva)
            elif opcion == "2":
                opcion_registrar_dia(reserva)
            elif opcion == "3":
                opcion_simular_dias(reserva)
            elif opcion == "4":
                opcion_informe(reserva)
            elif opcion == "5":
                opcion_uso_extremo(reserva)
            elif opcion == "6":
                opcion_cargar_archivos(reserva)
            elif opcion == "7":
                print("Hasta luego.")
            else:
                print("La opción no es válida.")
    except EOFError:
        print()
        print("Se terminó la entrada de datos. El programa termina.")


if __name__ == "__main__":
    main()
