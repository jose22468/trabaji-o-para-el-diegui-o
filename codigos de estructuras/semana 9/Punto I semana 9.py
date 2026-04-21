import sys

def resolver():
    # Leemos la cadena y eliminamos espacios en blanco
    s = sys.stdin.readline().strip()
    if not s:
        return

    n = len(s)
    # dp[i] guardará el grado de palíndromo del prefijo de longitud i
    dp = [0] * (n + 1)
    
    # Variables para el Rolling Hash
    h1 = 0  # Hash hacia adelante
    h2 = 0  # Hash hacia atrás
    base = 131  # Un número primo como base
    pw = 1      # Potencia de la base
    mod = 10**9 + 7  # Un módulo grande para evitar colisiones
    
    total_suma = 0
    
    for i in range(1, n + 1):
        char_val = ord(s[i-1])
        
        # Actualizamos hash hacia adelante: (h1 * base + nuevo_caracter)
        h1 = (h1 * base + char_val) % mod
        
        # Actualizamos hash hacia atrás: (h2 + nuevo_caracter * base^(i-1))
        h2 = (h2 + char_val * pw) % mod
        pw = (pw * base) % mod
        
        # Si los hashes coinciden, el prefijo es un palíndromo
        if h1 == h2:
            # El grado es: 1 + el grado de su mitad izquierda
            # La mitad izquierda de un prefijo de longitud i es i // 2
            dp[i] = dp[i // 2] + 1
            total_suma += dp[i]
        else:
            # No es palíndromo, su grado es 0
            dp[i] = 0
            
    print(total_suma)

if __name__ == "__main__":
    resolver()