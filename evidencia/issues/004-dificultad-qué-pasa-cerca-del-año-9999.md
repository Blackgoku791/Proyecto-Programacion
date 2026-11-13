# 004 - Que pasa cerca del ano 9999

Creado por Sebastian, 13/11. Asignado a Sebastian. Hito M2. Etiquetas: dificultad, caso-limite.
Cerrado el 13/11 con: `limite del calendario, ya no se cae`.

## Que paso

Hice un sector que empezaba el 31/12/9999 y al registrar el dia siguiente el
programa se cayo con OverflowError. El documento no dice nada de ese borde.

## Como lo arreglamos

Se agregaron `dias_que_caben` y `MENSAJE_FIN_CALENDARIO`. Registrar, simular y
cargar archivos avisan en vez de caerse (casos 25 y 81).

## Lo que hablamos

Sebastian: Encontre el error al probar justo ese dia. Se caea en vez de avisar.

Luis: Como el documento no lo contempla, podiamos decidir nosotros. Yo diria
que es un limite del calendario y ya.

Jose: Que avise, pero que no se detenga todo. Si cargando un archivo aparece un
dia de mas, se descarta esa linea y se sigue con las demas.
