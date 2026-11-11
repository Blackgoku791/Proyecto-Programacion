# 001 - Orden del mensaje al crear un sector con varios datos malos

Creado por Luis, 11/11. Asignado a Sebastian. Hito M1. Etiquetas: dificultad, validacion.
Cerrado el 11/11 con: `arreglo el orden de validacion en crear_sector`.

## Que paso

Probamos el ejemplo que trae el documento: capacidad 0 y fecha 31 de noviembre.
Nos respondia "La fecha no es valida" y debe responder la capacidad, porque esa
es la primera condicion que falla. Estabamos validando la fecha apenas la leiamos.

## Como lo arreglamos

Ahora leemos los cinco datos y despues revisamos en este orden: nombre, capacidad
entera, capacidad >= 1 y fecha. El caso 17 quedo para que no se nos vuelva a
meter el mismo error.

## Lo que hablamos

Jose: El problema es validar mientras se lee. Si el usuario escribe primero la
fecha, sale un mensaje; si la escribe de ultimo, sale otro. No puede depender de
eso.

Luis: Si, y el ejemplo del profe es justo al reves de como lo teniamos.

Sebastian: Listo, dejo crear_sector con el orden del documento y meto el caso 17.
