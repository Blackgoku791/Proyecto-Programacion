# 007 - Leer archivos: saltos de linea, BOM y codificacion

Creado por Sebastian, 18/11. Asignado a Jose. Hito M5. Etiquetas: dificultad, archivos.
Cerrado el 19/11 con: `leer_lineas ya distingue los errores`.

## Que paso

`splitlines()` cortaba en caracteres que no son saltos de linea del archivo.
Ademas un archivo exportado del Excel traia BOM y el primer sector salia con un
nombre raro, y uno en Latin-1 directamente reventaba sin mensaje.

## Como lo arreglamos

Cambiamos a `split("\n")` y dejamos que `strip()` limpie el retorno de carro del
CRLF. Separamos los mensajes: archivo que no existe, archivo que no es UTF-8 y
demas errores de lectura. Los archivos de prueba estan en `casos/datos/`.

## Lo que hablamos

Sebastian: El Excel nos metio un BOM y el primer nombre salia mal.

Jose: Con split("\n") y strip() se arregla lo del BOM y lo del CRLF.

Luis: Y separa los tres mensajes de error, que antes todo caia en el mismo.
El caso 78 defiende lo de Latin-1.
