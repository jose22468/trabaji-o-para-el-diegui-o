import sys

def resolver():
    # Leemos todas las líneas de la entrada estándar
    lineas = sys.stdin.read().splitlines()
    
    # Procesamos las líneas de dos en dos
    for i in range(0, len(lineas), 2):
        # Es posible que la última pareja esté incompleta si el archivo termina mal
        if i + 1 >= len(lineas):
            break
            
        a = lineas[i]
        b = lineas[i+1]
        
        resultado = []
        
        # Recorremos las letras del abecedario en orden
        for char_code in range(ord('a'), ord('z') + 1):
            letra = chr(char_code)
            
            # Contamos cuántas veces aparece la letra en cada cadena
            conteo_a = a.count(letra)
            conteo_b = b.count(letra)
            
            # El número de veces que incluimos la letra es el mínimo de ambos
            veces = min(conteo_a, conteo_b)
            
            # Añadimos la letra esa cantidad de veces a nuestra lista
            resultado.append(letra * veces)
        
        # Unimos todo en una sola cadena y la imprimimos
        print("".join(resultado))

if __name__ == "__main__":
    resolver()