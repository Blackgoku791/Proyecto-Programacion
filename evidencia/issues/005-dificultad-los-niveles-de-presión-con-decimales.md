# 005 - Los niveles de presion con decimales

Creado por Luis, 15/11. Asignado a Luis. Hito M3. Etiquetas: dificultad, aritmetica.
Cerrado el 15/11 con: `niveles con comparacion de enteros`.

## Que paso

Con capacidad 600 y 540 visitantes la division daba 89.99999 y caia en alta.
Segun el documento 540 es saturacion, porque es justo el 90%.

## Como lo arreglamos

Comparamos `visitantes * 100` contra `90 * capacidad`, `75 * capacidad` y
`50 * capacidad`. El `round` a dos decimales solo quedo al imprimir el informe
(caso 45).

## Lo que hablamos

Luis: El calculo con decimales me dio 89.9999 y me clasifico mal el dia.

Jose: Es lo mismo de siempre, no comparemos float. Multiplicamos en cruz.

Sebastian: Si, y dejamos el redondeo solo en la salida, no sea que cambie la
clasificacion.
