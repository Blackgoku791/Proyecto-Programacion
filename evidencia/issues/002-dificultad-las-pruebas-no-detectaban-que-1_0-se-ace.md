# 002 - Las pruebas no detectaban que 1_0 se aceptara como entero

Creado por Luis, 12/11. Asignado a Sebastian. Hito M2. Etiquetas: dificultad, verificacion.
Cerrado el 12/11 con: `convertir_entero solo acepta digitos`.

## Que paso

`int("1_0")` en Python da 10. El documento dice que solo se permiten digitos.
Para ver si nuestros casos servian, cambie la funcion a proposito a `int(texto)`
y... no fallo ninguna prueba. O sea que nuestras pruebas no probaban nada de eso.

## Como lo arreglamos

convertir_entero ahora recorre el texto y solo deja pasar 0-9 con signo opcional.
Agregue `1_0` en los casos 12 y 21. Volvi a dañar la funcion a proposito y esta
vez si fallo.

## Lo que hablamos

Sebastian: Puse el int(texto) malo a proposito y las 63 pruebas quedaron verdes.
Eso no puede estar bien.

Luis: El caso limite no venia en el documento, lo tuvimos que inventar nosotros.

Jose: Agregalo tu a los casos 12 y 21 y lo volvemos a intentar. Si no falla,
entonces el caso no sirve.
