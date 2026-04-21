# Leemos el número de hojas
n = int(input())

# Creamos un conjunto para guardar las combinaciones únicas
hojas_unicas = set()

for _ in range(n):
    # Leemos la línea que contiene "especie color"
    hoja = input()
    # La añadimos al conjunto
    hojas_unicas.add(hoja)

# El tamaño del conjunto será el número de hojas diferentes recogidas
print(len(hojas_unicas))