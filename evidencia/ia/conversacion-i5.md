# Incremento 5: cargar desde archivos

Esta parte salió de la conversación con Claude. El artifact completo está en
https://claude.ai/artifact/4QTAkEsfXs263JdqbGfBFf
y la copia local en `conversacion-completa.md`.

---

Actividad

	

Qué respondió la IA

	

Qué se aceptó o se corrigió, y por qué



Análisis

	

Separó las líneas que se saltan sin aviso (vacías) de las que se descartan con el mensaje "Línea N descartada: causa".

	

Se aceptó.



Diseño

	

leer_lineas devuelve (líneas, mensaje); cargar_sectores y cargar_visitantes devuelven (cuántos, descartes) y no imprimen nada.

	

Se aceptó. Dejar el print en la interfaz mantiene separada la lógica.



Codificación

	

Las líneas se parten con split("\n") y no con splitlines; se capturan por separado el archivo que no existe, el que no está en UTF-8 y los demás errores de lectura. Además, la IA agregó por su cuenta un límite: el registro no pasa del 31 de diciembre de 9999.

	

Se aceptó. El límite no estaba en el documento; lo puso la IA para que el programa no se caiga con OverflowError.



Verificación

	

Archivos de prueba en casos/datos/ con BOM, saltos de línea de Windows, Latin-1 y vacíos.

	

Se aceptó.
