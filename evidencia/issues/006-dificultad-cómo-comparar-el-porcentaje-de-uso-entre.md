# 006 - Como comparar el porcentaje de uso entre sectores

Creado por Jose, 17/11. Asignado a Luis. Hito M4. Etiquetas: dificultad, aritmetica.
Cerrado el 17/11 con: `comparo uso en multiplicacion cruzada`.

## Que paso

El caso 55 tiene dos sectores gemelos con el mismo uso exacto. Con division los
decimales los separaban y ganaba el equivocado. La regla dice que en empate
gana el que se creo primero.

## Como lo arreglamos

`uso_mayor_que` compara en multiplicacion cruzada, todo con enteros. Ademas
`sectores_con_uso_extremo` recorre en orden de creacion y usa `>` estricto.

## Lo que hablamos

Jose: El caso 55 me esta fallando y no entiendo por que si son iguales.

Luis: Es la division otra vez. Multiplicamos totales por la capacidad del otro
y comparamos enteros, igual que hicimos con los niveles.

Sebastian: Y como recorremos en orden, el primero gana el empate por construccion.
