# Incremento 1: el menú, crear un sector y buscarlo

Esta parte salió de la conversación con Claude. El artifact completo está en
https://claude.ai/artifact/4QTAkEsfXs263JdqbGfBFf
y la copia local en `conversacion-completa.md`.

---

Actividad

	

Qué respondió la IA

	

Qué se aceptó o se corrigió, y por qué



Análisis

	

Leyó el documento del trabajo y propuso leer los cinco datos del sector antes de validar, porque el ejemplo con capacidad 0 y fecha 31 de noviembre solo avisa de la capacidad.

	

Se aceptó: coincide con el ejemplo del documento.



Diseño

	

Creó las clases Sector y Reserva; crear_sector devuelve (sector, mensaje) y revisa las condiciones en el orden del documento.

	

Se aceptó; no hubo cambios del equipo en la conversación.



Codificación

	

Escribió convertir_entero aceptando solo dígitos 0-9 con signo opcional, crear_fecha con datetime.date y el menú con while y elif.

	

Se aceptó. La IA dejó de usar int directo porque int("1_0") da 10 en Python y el documento no lo permite.



Verificación

	

Escribió los casos del incremento y los corrió con verificar.py.

	

La IA encontró que sus propios casos no detectaban un convertir_entero que aceptara 1_0; agregó casos a las pruebas 12 y 21 y volvió a correr todo.
