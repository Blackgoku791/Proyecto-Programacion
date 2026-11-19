"""Ejecuta todos los casos de verificación de la carpeta casos/.

Uso:  python verificar.py            (todos los casos)
      python verificar.py 40 55      (solo los casos cuyo nombre empieza por 40 o 55)

Cada caso se comprueba ejecutando user_interface.py de verdad, como lo haría una
persona: se le entrega entrada.txt por la entrada estándar y se compara lo que
imprime con salida_esperada.txt. Los casos que dependen del azar traen un
comprobar.py en lugar de salida_esperada.txt.
"""

import difflib
import os
import runpy
import subprocess
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
CARPETA_CASOS = os.path.join(RAIZ, "casos")


def leer(ruta):
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        return archivo.read()


def ejecutar_programa(entrada, fecha):
    """Corre user_interface.py con esa entrada y devuelve (salida, errores)."""
    entorno = dict(os.environ)
    entorno["ECO_ENTRADA"] = "1"
    entorno["PYTHONIOENCODING"] = "utf-8"
    entorno["PYTHONUTF8"] = "1"
    entorno.pop("FECHA_ACTUAL_PRUEBA", None)
    if fecha:
        entorno["FECHA_ACTUAL_PRUEBA"] = fecha
    resultado = subprocess.run([sys.executable, "user_interface.py"], input=entrada.encode("utf-8"),
                               capture_output=True, cwd=RAIZ, env=entorno, timeout=120)
    salida = resultado.stdout.decode("utf-8").replace("\r\n", "\n")
    return salida, resultado.stderr.decode("utf-8")


def verificar_caso(nombre):
    ruta = os.path.join(CARPETA_CASOS, nombre)
    entrada = leer(os.path.join(ruta, "entrada.txt"))
    fecha_archivo = os.path.join(ruta, "fecha.txt")
    fecha = leer(fecha_archivo).strip() if os.path.exists(fecha_archivo) else None
    salida, errores = ejecutar_programa(entrada, fecha)
    if errores.strip() != "":
        return "el programa falló:\n" + errores

    ruta_comprobar = os.path.join(ruta, "comprobar.py")
    if os.path.exists(ruta_comprobar):
        problema = runpy.run_path(ruta_comprobar)["comprobar"](salida)
        return problema

    esperada = leer(os.path.join(ruta, "salida_esperada.txt"))
    if salida == esperada:
        return None
    diferencias = difflib.unified_diff(esperada.splitlines(), salida.splitlines(),
                                       "esperada", "obtenida", lineterm="", n=2)
    return "la salida no coincide:\n" + "\n".join(diferencias)


def main():
    filtros = sys.argv[1:]
    nombres = sorted(n for n in os.listdir(CARPETA_CASOS)
                     if os.path.isdir(os.path.join(CARPETA_CASOS, n)) and n != "datos")
    if filtros:
        nombres = [n for n in nombres if any(n.startswith(f) for f in filtros)]
    fallidos = 0
    for nombre in nombres:
        problema = verificar_caso(nombre)
        if problema is None:
            print(f"OK       {nombre}")
        else:
            fallidos += 1
            print(f"FALLA    {nombre}")
            for linea in problema.splitlines():
                print("           " + linea)
    print()
    print(f"{len(nombres) - fallidos} de {len(nombres)} casos pasaron.")
    return 1 if fallidos else 0


if __name__ == "__main__":
    sys.exit(main())
