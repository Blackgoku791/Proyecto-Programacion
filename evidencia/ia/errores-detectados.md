# Errores detectados y comprobaciones

Lo que viene hasta la línea "Comprobación hecha hoy" es copia del artifact de
Claude: https://claude.ai/artifact/4QTAkEsfXs263JdqbGfBFf

---

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

---

## Comprobación hecha hoy

Volví a correr la prueba de mutación sobre una copia del repositorio: cambié
`convertir_entero` por un `return int(texto.strip())`, que sí acepta `"1_0"`.
Con los casos que hay ahora, la prueba falla en 12 casos, entre ellos el 12 y el
21:

    FALLA    12_crear_capacidad_no_entera
    FALLA    15_crear_fecha_invalida
    FALLA    17_crear_orden_de_validacion
    FALLA    21_registrar_validacion_y_exito
    FALLA    33_simular_dias_invalidos
    FALLA    34_simular_minimo_invalido
    FALLA    35_simular_maximo_invalido
    FALLA    70_cargar_ejemplo_del_documento
    FALLA    72_cargar_archivo_de_visitantes_inexistente
    FALLA    76_cargar_sectores_causas_de_descarte
    FALLA    77_cargar_visitantes_causas_de_descarte
    FALLA    80_cargar_todo_invalido_permite_otra_carga
    51 de 63 casos pasaron.

Eso confirma que los casos agregados sirven. Antes de agregarlos, el mismo daño
pasaba sin que fallara ninguna prueba, como cuenta el artifact.

Salida final del verificador, con el código correcto:

    $ python verificar.py
    ...
    63 de 63 casos pasaron.
