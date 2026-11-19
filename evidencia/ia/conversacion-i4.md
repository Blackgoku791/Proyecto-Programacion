# Incremento 4: el sector de mayor y el de menor uso

Esta parte salió de la conversación con Claude. El artifact completo está en
https://claude.ai/artifact/4QTAkEsfXs263JdqbGfBFf
y la copia local en `conversacion-completa.md`.

---

Actividad

	

Qué respondió la IA

	

Qué se aceptó o se corrigió, y por qué



Análisis

	

Solo cuentan los sectores con al menos un día registrado, y si dos empatan gana el que se creó primero.

	

Se aceptó.



Diseño

	

Sector.uso_mayor_que compara dos sectores multiplicando en cruz, solo con enteros, en vez de dividir.

	

Se aceptó. Con divisiones, dos porcentajes iguales podrían salir distintos por los decimales.



Codificación

	

Reserva.sectores_con_uso_extremo recorre los sectores una sola vez guardando mayor y menor, con comparaciones estrictas.

	

Se aceptó.



Verificación

	

El caso 55 usa dos sectores "gemelos" con el mismo porcentaje exacto, para defender la comparación en cruz.

	

Se aceptó.
