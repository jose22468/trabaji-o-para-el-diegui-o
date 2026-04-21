import sys

def resolver():
    n = int(input())
    rondas = []
    puntajes_finales = {}

    # 1. Guardamos las rondas y calculamos el puntaje total de cada uno al final
    for _ in range(n):
        nombre, puntos = input().split()
        puntos = int(puntos)
        rondas.append((nombre, puntos))
        puntajes_finales[nombre] = puntajes_finales.get(nombre, 0) + puntos

    max_puntaje = max(puntajes_finales.values())

    puntajes_actuales = {}
    for nombre, puntos in rondas:
        puntajes_actuales[nombre] = puntajes_actuales.get(nombre, 0) + puntos
        
        if puntajes_actuales[nombre] >= max_puntaje and puntajes_finales[nombre] == max_puntaje:
            print(nombre)
            break

resolver()