# Miguel Ángel

Miguel Ángel Pichetto es uno de los dirigentes mas longevos del congreso de la nación. Paso por ambas cámaras (diputados y senadores) y pasó por los principales partidos del país: Fue jefe del senado durante el kirchnerismo, fue candidato a vicepresidente de Mauricio Macri, y ahora es uno de los principales armadores en diputados del gobierno de la libertad avanza. Completo. Conoce las cámaras mejor que su casa, y es un doctor honoris causa en rosca.

Pero uno no llega a diputado por magia. Es elegido. Democráticamente. Pero no es como los presidentes: se votan en conjunto, por lista. ¿Como se hace esto?

## Parte 1

Las bancas de diputados se asignan proporcionalmente en base a los votos que obtuvo cada lista en la elección. Pero muchas veces no se pueden dividir bien, y sería muy conflictivo si no hay una forma unívoca de asignación. Existen algoritmos de asignación proporcional, y particular, en argentina se usa una modificación del sistema D'Hondt.

**Todavía no busquen como es**. Lo vamos a ver más adelante. Solo tienen que saber que para repartir las bancas, necesita esencialmente 3 cosas:
- Los votos por agrupación
- Las bancas a repartir
- El total del padrón (este número no es solamente la suma de votos, cuenta también quienes no fueron a votar, los votos en blanco y los anulados)

La idea es construir tests para esta función hipotética, `bancas_por_agrupación`. Toma 3 parámetros: Los votos por agrupación, que van a ser `list[int]`,las bancas y el padrón, ambos enteros. La función retorna una lista de bancas por agrupación (`list[int]`) en el mismo orden para la lista de votos.

Por ejemplo, en 2023, San Juan renovaba 3 bancas de diputados. De un total de 607413 electores, LA LIBERTAD AVANZA obtuvo 145782 votos, UNION POR LA PATRIA 145188 votos y JUNTOS POR EL CAMBIO 107908 votos. Recibieron una banca cada uno. Es decir, de nuestra función hipotética *bancas_por_agrupación*, debería ocurrir que `bancas_por_agrupación([145782,145188,107908],3,607413)` debería devolver `[1,1,1]`.

Piensen un conjunto de tests para esta función, y escribanlos para `pytest en el archivo *test_bancas.py*. **Todavía no tienen que hacer la función**, por lo tanto, los tests deberían fallar. Pueden usar resultados de elecciones anteriores como referencia. Pueden ver datos de elecciones anteriores en: https://resultados.mininterior.gob.ar/. Para ver votos y bancas del 2023, pueden ver: https://www.pagina12.com.ar/601412-resultados-elecciones-2023-mapas-interactivos-con-los-datos-.

## Parte 2

Ahora si, completar la función `bancas_por_agrupación` en *main.py*. Pueden ver como es el algoritmo en los siguientes links:
- https://chequeado.com/el-explicador/como-funciona-el-sistema-dhondt-conoce-como-se-cuentan-los-votos-y-se-reparten-las-bancas-del-congreso-nacional/
- https://buenosaires.gob.ar/sites/default/files/media/document/2021/11/03/cf6fa751bd98e12d862873d24f0417820d5d6f5c.pdf
- https://es.wikipedia.org/wiki/Sistema_D%27Hondt

Obviamente, corran los tests que hicieron para ver si está bien.

Habiendo hecho el programa, ¿Cambiarían los tests que hicieron?