# coding=utf-8
from main import asignar_bancas

def test_distribucion_equilibrada():
    assert asignar_bancas([1000, 1000, 1000], 3, 5000) == [1, 1, 1]

def test_gran_diferencia_padron_votos():
    assert asignar_bancas([100, 200, 300], 2, 10000) == [0, 1, 1]

def test_votos_minimos():
    assert asignar_bancas([1, 1000, 2000], 3, 3001) == [0, 1, 2]

def test_umbral():
    assert asignar_bancas([1001, 1000, 999], 3, 3000) == [1, 1, 1]

def test_distribucion_desigual():
    assert asignar_bancas([2000, 1500, 1000], 3, 5000) == [2, 1, 0]

def test_partido_dominante():
    assert asignar_bancas([5000, 1000, 500], 3, 7000) == [3, 0, 0]

def test_caso_real_san_juan_2023():
    assert asignar_bancas([145782, 145188, 107908], 3, 607413) == [1, 1, 1]

def test_votos_nulos_y_en_blanco():
    assert asignar_bancas([1000, 1000, 1000], 3, 5000) == [1, 1, 1]

def test_pocas_bancas_muchos_partidos():
    assert asignar_bancas([300, 200, 100, 50], 2, 1000) == [1, 1, 0, 0]

