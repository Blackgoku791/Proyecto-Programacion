# Incremento 3: el informe de un sector

Esta parte salió de la conversación con Claude. El artifact completo está en
https://claude.ai/artifact/4QTAkEsfXs263JdqbGfBFf
y la copia local en `conversacion-completa.md`.

---

Actividad

	

Qué respondió la IA

	

Qué se aceptó o se corrigió, y por qué



Análisis

	

Pasó cada indicador del informe a una fórmula y decidió qué se redondea y cuándo.

	

Se aceptó.



Diseño

	

Cuatro constantes para los niveles de presión y dias_sin_registrar(hoy), que recibe la fecha de hoy como parámetro.

	

Se aceptó. Recibir "hoy" permite probar el informe con una fecha fija.



Codificación

	

Los niveles se calculan con enteros (visitantes * 100 contra 90 * capacidad, 75 * capacidad y 50 * capacidad); el redondeo a 2 decimales solo se hace al imprimir.

	

Se aceptó. Con decimales, un día justo en 90 % podía caer en el nivel equivocado.



Verificación

	

Casos en los bordes de cada nivel y con FECHA_ACTUAL_PRUEBA para fijar el día de hoy.

	

Se aceptó.
