# Casos de verificación

Cada carpeta es un caso: `entrada.txt` es lo que se teclea, `salida_esperada.txt` es lo que debe mostrar el programa (o `comprobar.py`, cuando el resultado depende del azar) y `fecha.txt` es el día de hoy que se simula. Los archivos de datos están en `datos/`.

| Caso | Requisitos | Qué verifica |
|---|---|---|
| 01_menu_opciones_invalidas | 14 | Con opciones que no existen (8, dos, vacía, 0, 07) avisa y vuelve a mostrar el menú; los espacios alrededor de un 7 válido se ignoran. |
| 02_menu_salir_directo | 14 | La opción 7 termina el programa. |
| 03_menu_fin_de_entrada | 14 | Si se acaban los datos de entrada sin elegir salir, el programa termina con un aviso en vez de fallar. |
| 04_menu_vuelve_despues_de_cada_opcion | 14 | Después de crear, informar, ver extremos, registrar con sector inexistente y una opción inválida, el menú vuelve a mostrarse. |
| 10_crear_sector_ok | 1 | Con datos válidos crea el sector sin días registrados. |
| 11_crear_nombre_vacio | 1, 10 | Un nombre vacío o solo de espacios no crea el sector; un nombre con espacios alrededor se guarda sin ellos. |
| 12_crear_capacidad_no_entera | 1 | Capacidades que no son enteros (ochenta, 80.5, vacía, 8 0, 1e3, --5, +, -, 1_0 y dígitos de otros alfabetos) no crean el sector. |
| 13_crear_capacidad_menor_a_uno | 1 | Capacidades 0, -5 y -0 avisan que debe ser de al menos un visitante. |
| 14_crear_capacidad_valida | 1 | Capacidad 1 (límite), con espacios, con signo + y muy grande se aceptan. |
| 15_crear_fecha_invalida | 1 | Fechas que no existen o no son números enteros avisan que la fecha no es válida y no crean el sector. |
| 16_crear_fecha_borde_valida | 1 | Fechas límite válidas: 29 de febrero de un año bisiesto, 31 de diciembre de 9999, 1 de enero del año 1 y fechas con espacios. |
| 17_crear_orden_de_validacion | 1 | Cuando fallan varias condiciones se muestra solo el mensaje de la primera: nombre vacío, nombre repetido, capacidad no entera, capacidad menor a uno, fecha. |
| 18_crear_nombre_repetido_conserva_el_original | 1, 10 | Crear un sector con un nombre ya usado (también con espacios alrededor) avisa y el sector original conserva sus datos. |
| 19_nombres_que_difieren_en_mayusculas_o_tildes | 1, 10 | El nombre se compara tal como está escrito: playa brava y Playa Brava son sectores distintos, igual que Murciélago y Murcielago. |
| 20_registrar_sector_inexistente | 2, 10 | Con un nombre que no corresponde a un sector avisa y vuelve al menú sin leer visitantes. |
| 21_registrar_validacion_y_exito | 2, 4, 5 | Repite la lectura del mismo día mientras el dato no sea un entero de 0 a la capacidad; con 52 registra el día. |
| 22_registrar_limites_cero_y_capacidad | 2, 5, 6, 7 | 0 y la capacidad son visitantes válidos; el día siguiente avanza de a uno; 1 se escribe en singular. |
| 23_registrar_cambio_de_anio | 2, 9 | El día siguiente cruza de 2026-12-31 a 2027-01-01; un registro adelantado a hoy está al día. |
| 24_registrar_anios_bisiesto_y_no_bisiesto | 2 | Después del 28 de febrero sigue el 29 en 2028 (bisiesto) y el 1 de marzo en 2027. |
| 25_fin_del_calendario | 2, 3 | En el último día que admite el calendario (9999-12-31) ya no se puede registrar ni simular, y se avisa cuántos días caben. |
| 30_simular_sector_inexistente | 3, 10 | Con un sector inexistente avisa y vuelve al menú sin leer los demás datos. |
| 31_simular_con_minimo_igual_al_maximo | 3, 4, 7 | Con mínimo igual al máximo (40) los tres días simulados valen 40; 40 de 80 es exactamente 50 %, presión moderada. |
| 32_simular_numeros_al_azar_dentro_del_rango | 3 | Los días simulados se agregan después de los registrados, con visitantes dentro del rango y con el mínimo y el máximo incluidos (propiedades, porque el azar cambia en cada ejecución). |
| 33_simular_dias_invalidos | 3 | Días que no son enteros o menores que 1 avisan y no leen el mínimo ni el máximo; no se agrega ningún día. |
| 34_simular_minimo_invalido | 3 | Un mínimo no entero o fuera de 0 a la capacidad avisa y no lee el máximo. |
| 35_simular_maximo_invalido | 3 | Un máximo no entero o fuera de 0 a la capacidad avisa y no agrega días. |
| 36_simular_minimo_mayor_que_el_maximo | 3, 4 | Mínimo mayor que el máximo avisa; el máximo fuera de rango se avisa antes que la comparación; mínimo 0 y máximo 0 con 1 día se acepta. |
| 40_informe_playa_brava | 4, 5, 6, 7, 8, 9, 13 | Informe completo de Playa Brava con el ejemplo del documento (80.17 %, desviación 112.53, 3 días en saturación, racha de 2). |
| 41_informe_sendero_de_los_mangles | 4, 5, 6, 7, 8, 9 | Informe del Sendero de los Mangles: promedio 105.0, desviación 33.54, un día en cada nivel. |
| 42_informe_sector_sin_dias | 4 | Un sector sin días registrados muestra nombre, capacidad y el aviso, y nada más. |
| 43_informe_un_solo_dia_y_registro_al_dia | 4, 5, 6, 9 | Con un solo día la desviación es 0.0; con hoy el 2026-11-02 y último día 2026-11-01 el registro está al día. |
| 44_informe_empates_de_maximo_y_minimo | 6, 7, 8 | Con dos días empatados en el máximo (600) y en el mínimo (120) se muestran los primeros. |
| 45_informe_fronteras_de_los_niveles | 7 | Los visitantes 299, 300, 449, 450, 539 y 540 de un sector de 600 caen en baja, moderada, moderada, alta, alta y saturación. |
| 46_informe_racha_mas_larga_de_tres | 8 | Hay una racha de 2 días y otra de 3 días; gana la de 3 que empieza el 2026-11-04. |
| 47_informe_rachas_empatadas | 8 | Dos rachas de 2 días empatan; muestra la que empezó primero. |
| 48_informe_racha_que_abarca_todo_el_registro | 8 | Todos los días en saturación (el 90 % exacto cuenta): la racha es todo el registro. |
| 49_informe_sin_saturacion | 7, 8 | Sin ningún día en saturación el informe lo avisa; 50 % exacto es moderada y 89 % es alta. |
| 50_extremos_ejemplo_del_documento | 11 | Playa Brava (80.17 %) es el más alto y el Mirador del Faro (65.0 %) el más bajo; la Cueva sin días no cuenta. |
| 51_extremos_sin_sectores | 11 | Sin sectores avisa que ningún sector tiene días registrados. |
| 52_extremos_sectores_sin_dias | 11 | Con un sector sin días registrados avisa lo mismo. |
| 53_extremos_empate_gana_el_primero | 11 | Tres sectores con 50 % exacto: tanto el más alto como el más bajo son el primero creado. |
| 54_extremos_un_solo_sector_con_dias | 11 | Con un único sector con días, ese sector es a la vez el más alto y el más bajo. |
| 55_extremos_empate_exacto_que_los_decimales_romperian | 11 | Gemelo A (1 de 3) y Gemelo B (1, 2 y 2 de 5) tienen exactamente 33.33 %, pero con decimales el cálculo promedio/capacidad*100 da valores distintos; debe contar el primero. |
| 56_extremos_el_mayor_se_creo_despues | 11 | El sector de mayor uso (Alto, 90 %) se creó después del de menor uso (Bajo, 10 %). |
| 60_pendientes_un_solo_dia | 9 | Con hoy el 2026-11-07 y último día el 2026-11-05 falta registrar un solo día, el 2026-11-06. |
| 61_pendientes_registro_al_dia_justo | 9 | Con hoy el 2026-11-06 el último día registrado es el anterior a hoy: al día. |
| 62_pendientes_registro_adelantado | 9 | Con hoy el 2026-11-04 el registro llega más lejos que el día anterior a hoy: al día. |
| 63_pendientes_cruzando_el_anio | 9 | Con hoy el 2027-01-03 faltan 58 días, del 2026-11-06 al 2027-01-02. |
| 64_pendientes_ejemplo_del_documento | 9 | Con hoy el 2026-11-20 faltan 14 días del 2026-11-06 al 2026-11-19 (Playa Brava) y 15 en el Sendero de los Mangles. |
| 70_cargar_ejemplo_del_documento | 12, 13 | Carga el ejemplo completo del documento: 2 sectores con 5 líneas descartadas y 9 días con otras 5 descartadas, y comprueba los datos cargados. |
| 71_cargar_archivo_de_sectores_inexistente | 12 | Si el archivo de sectores no existe lo avisa, no carga nada y no lee la ruta del de visitantes. |
| 72_cargar_archivo_de_visitantes_inexistente | 13 | Si el archivo de visitantes no existe, los sectores ya cargados se quedan sin días registrados. |
| 73_cargar_con_sectores_creados_a_mano | 12 | Con un sector ya en el programa avisa que la carga solo se hace sin sectores y no lee ninguna ruta. |
| 74_cargar_dos_veces | 12, 13 | Una segunda carga se rechaza y los días no se agregan otra vez (Playa Brava sigue con 5 días). |
| 75_cargar_formato_flexible | 12, 13 | Acepta BOM, finales de línea de Windows, líneas vacías o solo con espacios, espacios alrededor de los campos y última línea sin salto de línea. |
| 76_cargar_sectores_causas_de_descarte | 12 | Cada causa de descarte de una línea de sectores, en el orden de las condiciones: campos, nombre vacío, nombre repetido (con espacios), capacidad no entera, capacidad menor a uno y fecha. |
| 77_cargar_visitantes_causas_de_descarte | 13 | Cada causa de descarte de una línea de visitantes: campos, sector inexistente (también por mayúsculas), no entero y fuera de rango; 0 y la capacidad se aceptan. |
| 78_cargar_archivo_que_no_es_utf8 | 12 | Un archivo de sectores guardado en Latin-1 se rechaza completo con un aviso. |
| 79_cargar_ruta_vacia_o_de_carpeta | 12 | Una ruta vacía no existe; una ruta que es una carpeta no se puede leer. En ambos casos no se carga nada. |
| 80_cargar_todo_invalido_permite_otra_carga | 12, 13 | Si ninguna línea crea un sector, el programa sigue sin sectores y permite una nueva carga. |
| 81_cargar_fin_del_calendario_y_singular | 12, 13 | Un día que ya no cabe en el calendario se descarta con su causa; con un sector y un día los avisos van en singular. |
| 82_cargar_archivos_vacios | 12, 13 | Un archivo sin ningún byte y uno con solo el encabezado cargan cero sectores y cero días. |
| 90_buscar_por_nombre_exacto | 10 | El nombre distingue mayúsculas y tildes y se compara sin espacios al principio ni al final; informe, registrar y simular lo buscan igual. |
