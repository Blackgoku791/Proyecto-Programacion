# Analisis - Alternativa B: Reserva Natural Bahia Coralina

Equipo: Jose Alcendra, Sebastian Turizo, Luis Pacheco.
Curso: Fundamentos de Programacion, Universidad del Magdalena.

Acá dejamos escritas las reglas que salieron del documento de la alternativa y
las decisiones que tomamos cuando algo no estaba claro. Este es el mismo analisis
que usamos para hacer los 63 casos de `casos/`.

## Acuerdos que vale la pena aclarar

- El nombre del sector se recorta con `strip()` y se compara tal cual. O sea que
  `playa brava` no encuentra a `Playa Brava` (caso 90).
- Para entero admitimos solo digitos, con signo opcional. `int("1_0")` de Python
  da 10 y eso no debe pasar (casos 12 y 21).
- Las fechas se validan con `date`; atras capturamos `ValueError` y
  `OverflowError` (caso 15).
- El dia que se registra siempre es el siguiente del ultimo que hay, sin saltos
  (casos 23 y 24).
- No se puede pasar del 9999-12-31.Si se llega ahi avisamos con
  `MENSAJE_FIN_CALENDARIO` (casos 25 y 81).

## Requisito 1 - crear sector

Entradas: nombre, capacidad, anio, mes y dia. Salida: el sector nuevo o el
mensaje de error.

Leemos los cinco datos antes de validar. Esto es importante porque en el ejemplo
del documento (capacidad 0 y 31 de noviembre) debe avisar la capacidad, no la
fecha (caso 17). El orden de las condiciones es: nombre no vacio y no repetido,
capacidad entera, capacidad >= 1 y fecha valida. Si el nombre ya existe no se
toca el sector original (caso 18).

## Requisito 2 - registrar visitantes

Se pide el nombre del sector y los visitantes del dia siguiente. Entre 0 y la
capacidad, los dos incluidos. Si el dato esta mal se vuelve a preguntar el mismo
dia (casos 21 y 22). Si el sector no existe, aviso y vuelta al menu (caso 20).

## Requisito 3 - simular dias

Nombre, cantidad de dias, minimo y maximo. Cada dato se valida apenas se lee.
Dias >= 1, minimo y maximo entre 0 y la capacidad, minimo <= maximo. Usamos
`randint`, que incluye los extremos. Para poder probar sin depender del azar le
pasamos el generador a `simular_dias` (caso 32).

## Requisito 4 - informe de un sector

Nombre y fecha actual (la fecha se puede inyectar en las pruebas). Mostramos
nombre, capacidad, dias, total de visitantes, promedio y porcentaje de uso con
`round(..., 2)`. Sin dias registrados solo sale el aviso (caso 42).
`promedio = totales / dias` y `porcentaje = promedio / capacidad * 100`.

## Requisito 5 - desviacion estandar

Raiz cuadrada de la media de los cuadrados de las diferencias con el promedio,
redondeada a dos decimales (casos 40, 41 y 43).

## Requisito 6 - dia de mas y de menos visitantes

Las fechas del maximo y del minimo. En empate gana el primero del registro;
por eso los recorridos usan `>` y `<` estrictos (caso 44).

## Requisito 7 - niveles de presion

Baja < 50%, moderada [50%, 75%), alta [75%, 90%) y saturacion >= 90%.
Comparamos `visitantes * 100` contra `50/75/90 * capacidad` para que un dia
justo en 90% no caiga en alta por decimales (caso 45). Se imprimen los cuatro
conteos, aunque sean cero.

## Requisito 8 - racha mas larga en saturacion

Longitud y fecha de inicio. En empate gana la que empezo primero. Si no hay
saturacion, se avisa (casos 46 a 49).

## Requisito 9 - dias sin registrar

El ultimo dia deberia ser el anterior a hoy. Si no, decimos cuantos faltan y el
rango. `dias_sin_registrar(hoy)` recibe la fecha para que el caso 64 no dependa
del dia en que corramos las pruebas.

## Requisito 10 - varios sectores

Busqueda exacta por nombre en orden de creacion o carga. Sin coincidencia, aviso
y vuelta al menu (casos 19 y 90).

## Requisito 11 - mayor y menor porcentaje de uso

Solo sectores con al menos un dia. Se compara sin redondear y en empate gana el
que se creo primero. `uso_mayor_que` multiplica en cruz con enteros porque
dividir rompia empates exactos (casos 53 y 55). Al mostrar si va redondeado a
dos decimales (caso 50).

## Requisito 12 - cargar sectores desde archivo

CSV UTF-8 con encabezado y cinco campos separados por `;`. Solo se permite con
el programa sin sectores. Las lineas vacias se saltan; una linea mala se
descarta con su numero y motivo y se sigue (casos 70, 73, 74, 76 y 82).

## Requisito 13 - cargar visitantes desde archivo

Igual, pero con dos campos. Se descarta por campos incorrectos, sector que no
existe, visitantes no enteros o fuera de rango, y fin del calendario.
`leer_lineas` usa `split("\n")` y separa los mensajes de archivo inexistente,
archivo no UTF-8 y otros errores (casos 71, 72, 77, 78, 79 y 81).

## Requisito 14 - menu

Siete opciones. Despues de cada una vuelve a salir el menu; una opcion que no
existe avisa. `7` termina y un `EOFError` tambien (casos 01 a 04).
