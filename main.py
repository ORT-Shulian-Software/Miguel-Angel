# coding=utf-8


def asignar_bancas(votos, bancas, padron):
    """
    Asigna las bancas de acuerdo al sistema D'Hondt modificado.

    :param votos: List[int] - Lista de votos por agrupación.
    :param bancas: int - Número de bancas a repartir.
    :param padron: int - Total del padrón electoral.
    :return: List[int] - Lista de bancas asignadas a cada agrupación.
    """
    num_agrupaciones = len(votos)
    cocientes = []
    
    # Generar la tabla de cocientes
    for i in range(num_agrupaciones):
        cocientes.extend([(votos[i] / (j + 1), i) for j in range(bancas)])
    
    # Ordenar los cocientes en orden descendente
    cocientes.sort(reverse=True, key=lambda x: x[0])
    
    # Seleccionar los n máximos y contar cuántos corresponden a cada agrupación
    resultado = [0] * num_agrupaciones
    for _, index in cocientes[:bancas]:
        resultado[index] += 1
    
    return resultado
