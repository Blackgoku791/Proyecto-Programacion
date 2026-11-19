# Conversación con Claude (copia local del artifact)

Link original: https://claude.ai/artifact/4QTAkEsfXs263JdqbGfBFf

Esta es una copia del artifact donde Claude resumió la conversación continua que
se usó en los cinco incrementos. No es el JSON crudo de Claude: si después se
exporta el historial completo desde la aplicación, se guarda en esta misma carpeta.

---

Informe del uso de la inteligencia artificial generativa

19 de nov de 2026
 · 
@Jose



Resumen

Usamos un solo asistente, Claude de Anthropic, en una conversación continua de Claude Code. Le pedimos que escribiera el programa de la Alternativa B (business_logic.py y user_interface.py), el documento de análisis, los casos de verificación y el informe integral, y después que nos explicara el código para poder entenderlo.

La IA produjo casi todo el primer borrador de código y documentos; nosotros pedimos, leimos, ejecutamos las pruebas y decidimos qué quedaba. Este informe cuenta cada actividad del ciclo en los cinco incrementos, y dice con honestidad qué hizo la IA y qué hicimos nosotros. Las pruebas finales son 63 casos que se corren con verificar.py y que ejecutan el programa de verdad.

Incrementos 1 a 5

Usamos los mismos cinco incrementos del informe integral. Toda la conversación la llevó Jose, así que él es el integrante de cada interacción de abajo; los demás integrantes que usaron la IA por su cuenta deben agregar sus interacciones en la sección final. Casi todo se pidió en un solo encargo grande, y la IA lo fue resolviendo incremento por incremento. Por eso las tablas cuentan lo que la IA decidió en cada actividad y no una conversación distinta por incremento.

Incremento 1: el menú, crear un sector y buscarlo

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

Incremento 2: registrar días y simular días

Actividad

	

Qué respondió la IA

	

Qué se aceptó o se corrigió, y por qué



Análisis

	

Definió que el día que sigue es la fecha de inicio más tantos días como ya estén registrados.

	

Se aceptó: evita guardar una fecha por día.



Diseño

	

Sector.validar_visitantes devuelve (valor, mensaje) y lo reutilizan el registro, la simulación y la carga de archivos. simular_dias recibe el generador de números aleatorios como parámetro.

	

Se aceptó. Pasar el generador permite probar la simulación sin depender del azar.



Codificación

	

El registro repite la pregunta con un while hasta que el valor sea válido; la simulación usa randint(minimo, maximo), que incluye los dos extremos.

	

Se aceptó.



Verificación

	

El caso 32 revisa la simulación con un comprobar.py que mira rangos y cantidades, porque el resultado cambia en cada corrida.

	

Se aceptó; los demás casos comparan la salida palabra por palabra.

Incremento 3: el informe de un sector

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

Incremento 4: el sector de mayor y el de menor uso

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

Incremento 5: cargar desde archivos

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

Errores de la IA y cómo los detectamos

Los errores de abajo ocurrieron en la conversación. Los detectó la propia IA con sus pruebas, no nosotros; si el equipo encontró otros al leer o correr el código, hay que agregarlos aquí.

Error

	

Cómo se detectó

	

Qué se hizo



Los casos de verificación no detectaban un convertir_entero que aceptara 1_0 como entero.

	

Con una prueba de mutación: se dañó el código a propósito y se vio que ningún caso fallaba.

	

Se agregaron casos a las pruebas 12 y 21 y se repitió la prueba hasta que el daño sí fallara.



El generador de casos tenía restos de pruebas anteriores: un truco con [:-1], un bloque if False else y uno repetido en el caso 36.

	

Al releer el generador antes de entregar.

	

Se reescribió con una función registrar(nombre, fecha, errores, valido) y se quitó lo repetido.



Sumar un día a una fecha cercana al año 9999 podía fallar.

	

Al pensar en los límites del calendario para el incremento 5.

	

Se agregó el límite del 31 de diciembre de 9999 y el mensaje MENSAJE_FIN_CALENDARIO.



Una errata en el informe integral: "puestos a propuesta" en vez de "puestos a propósito".

	

Al releer el documento ya escrito.

	

Se corrigió.



Al leer los documentos del trabajo, la IA solo vio el CSS de las páginas HTML, porque la lectura se cortó.

	

El texto leído no tenía ningún requisito.

	

Extrajo el texto del cuerpo con un script y trabajó sobre ese texto.

Evidencias guardadas en el repositorio

Cada interacción de este informe se respalda con la exportación de la conversación donde ocurrió. La guardamos en la carpeta evidencia/ia/ del repositorio, con estos nombres:

Archivo

	

Qué respalda



evidencia/ia/conversacion-completa

	

Todos los incrementos: el encargo inicial, el código, el análisis, la explicación y el informe integral.



evidencia/ia/errores-detectados

	

Captura de la salida de verificar.py y de la prueba de mutación que mostró el error de 1_0.

Si un integrante usó la IA en otra conversación, su exportación va en la misma carpeta, con su nombre en el archivo.

Lo que el equipo debe completar antes de entregar

Este informe cuenta lo que pasó en la conversación que tenemos, y no puede saber lo que el equipo hizo fuera de ella.

Exportar la conversación desde la aplicación y guardarla en evidencia/ia/ con el nombre de la tabla de evidencias.

Agregar las interacciones de los otros integrantes que usaron la IA, con su nombre, qué pidieron y qué aceptaron o rechazaron.

Agregar los errores que el equipo encontró al leer o correr el código, si hubo alguno.

Revisar que en cada incremento quede escrito qué del código entendimos y modificamos nosotros, no solo lo que hizo la IA.

Poner la captura de python verificar.py con los 63 casos en verde en evidencia/ia/errores-detectados.
