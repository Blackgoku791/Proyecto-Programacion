# 003 - Probar la simulacion y el informe sin depender del azar ni de la fecha

Creado por Luis, 13/11. Asignado a Sebastian. Hitos M2 y M3. Etiquetas: dificultad, diseno, verificacion.
Cerrado el 16/11 con: `dias_sin_registrar recibe hoy`.

## Que paso

Dos cosas. La simulacion daba numeros distintos cada vez, y el informe miraba la
 fecha del computador. Entonces las salidas esperadas cambiaban solas y las
pruebas se caian al otro dia.

## Como lo arreglamos

`simular_dias` recibe el generador como parametro; en el programa normal sigue
siendo `random.randint` y en las pruebas metemos uno que da siempre el mismo
numero. Para la fecha, `dias_sin_registrar(hoy)` recibe el dia y el caso 64 usa
`FECHA_ACTUAL_PRUEBA`. El caso 32 no compara texto, revisa que cada visitante
este entre 40 y 80 y que la cantidad de dias sea la pedida.

## Lo que hablamos

Luis: El caso 32 no puede comparar palabra por palabra porque randint cambia.
Mejor pasamos el generador y revisamos rangos.

Jose: Igual con el caso 64. Si el informe llama a date.today(), la salida
esperada envejece.

Sebastian: Bien, pero solo inyectamos en las pruebas. Al usuario le sigue
llegando azar y la fecha real, no vamos a cambiar el comportamiento del menu.
