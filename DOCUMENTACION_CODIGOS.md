# Documentación línea por línea de todos los códigos

Esta guía explica **qué hace cada línea** de cada script del repositorio.

---

## 1) `codigos de estructuras/semana 9/Punto A semana 9.py`

### Explicación línea por línea
- **Línea 1**: Comentario que indica que se leerá la cantidad de hojas.
- **Línea 2**: `n = int(input())` lee un número entero desde entrada estándar.
- **Línea 4**: Comentario que anuncia la creación de un conjunto.
- **Línea 5**: `hojas_unicas = set()` crea un `set` vacío para evitar duplicados.
- **Línea 7**: `for _ in range(n):` repite el bloque exactamente `n` veces.
- **Línea 8**: Comentario descriptivo de la entrada esperada (`especie color`).
- **Línea 9**: `hoja = input()` lee una línea completa con los datos de una hoja.
- **Línea 10**: Comentario que indica la inserción al conjunto.
- **Línea 11**: `hojas_unicas.add(hoja)` agrega la hoja; si ya existe, no se duplica.
- **Línea 13**: Comentario que explica la salida final.
- **Línea 14**: `print(len(hojas_unicas))` imprime cuántas hojas distintas hubo.

### Cómo se construyó el código (paso a paso)
1. Se definió primero la entrada principal: cantidad de registros (`n`).
2. Se eligió `set` para resolver duplicados de manera automática.
3. Se diseñó un ciclo simple para leer cada registro.
4. Se cerró con una salida única: tamaño del conjunto.

---

## 2) `codigos de estructuras/semana 9/Punto B semana 9.py`

### Explicación línea por línea
- **Línea 1**: `import sys` para usar lectura rápida por `stdin`.
- **Línea 3**: Se declara la función `resolver()` que contiene toda la lógica.
- **Línea 4**: Comentario sobre leer toda la entrada.
- **Línea 5**: `lineas = sys.stdin.read().splitlines()` toma todas las líneas en una lista.
- **Línea 7**: Comentario: se procesan de dos en dos.
- **Línea 8**: `for i in range(0, len(lineas), 2):` avanza de 2 en 2 para tomar pares.
- **Línea 9**: Comentario sobre posible par incompleto.
- **Línea 10**: Verifica si falta la segunda línea del par.
- **Línea 11**: `break` corta si el par está incompleto.
- **Línea 13**: `a = lineas[i]` primera cadena.
- **Línea 14**: `b = lineas[i+1]` segunda cadena.
- **Línea 16**: `resultado = []` acumulará fragmentos de salida.
- **Línea 18**: Comentario: recorrer alfabeto en orden.
- **Línea 19**: Bucle de códigos ASCII de `'a'` a `'z'`.
- **Línea 20**: Convierte código ASCII a carácter con `chr`.
- **Línea 22**: Comentario de conteo por cadena.
- **Línea 23**: Cuenta apariciones de la letra en `a`.
- **Línea 24**: Cuenta apariciones de la letra en `b`.
- **Línea 26**: Comentario: usar mínimo común.
- **Línea 27**: `veces = min(conteo_a, conteo_b)` define cuántas letras comunes hay.
- **Línea 29**: Comentario: agregar la letra repetida.
- **Línea 30**: `resultado.append(letra * veces)` añade el bloque de caracteres.
- **Línea 32**: Comentario de unión final.
- **Línea 33**: `print("".join(resultado))` imprime intersección ordenada.
- **Línea 35**: Guarda de ejecución directa del archivo.
- **Línea 36**: Llama `resolver()` si se ejecuta como script principal.

### Cómo se construyó el código (paso a paso)
1. Se aisló la solución en una función.
2. Se planteó lectura total para manejar múltiples casos.
3. Se definió un patrón de procesamiento en pares de líneas.
4. Se recorrió el alfabeto para garantizar orden.
5. Se aplicó intersección por frecuencia con `min`.

---

## 3) `codigos de estructuras/semana 9/Punto E semana 9.py`

### Explicación línea por línea
- **Línea 1**: `import sys` (en este script no es esencial, pero está presente).
- **Línea 3**: Se define `resolver()`.
- **Línea 4**: `n = int(input())` lee número de rondas.
- **Línea 5**: `rondas = []` almacenará (jugador, puntos) en orden temporal.
- **Línea 6**: `puntajes_finales = {}` guardará total final por jugador.
- **Línea 8**: Comentario de la primera fase.
- **Línea 9**: Bucle de lectura de `n` rondas.
- **Línea 10**: `nombre, puntos = input().split()` toma datos de cada ronda.
- **Línea 11**: Convierte `puntos` a entero.
- **Línea 12**: Guarda la ronda en la lista.
- **Línea 13**: Acumula total final por jugador (`get(..., 0)` evita clave inexistente).
- **Línea 15**: Obtiene el mayor puntaje final alcanzado.
- **Línea 17**: `puntajes_actuales = {}` llevará acumulado en orden de rondas.
- **Línea 18**: Recorre nuevamente las rondas, ahora para desempatar por tiempo.
- **Línea 19**: Actualiza el acumulado parcial de cada jugador.
- **Línea 21**: Condición doble: (a) alcanza/supera máximo durante la secuencia y (b) su final real es máximo.
- **Línea 22**: Imprime ganador correcto.
- **Línea 23**: `break` para terminar al primer jugador válido.
- **Línea 25**: Ejecuta `resolver()` directamente.

### Cómo se construyó el código (paso a paso)
1. Se detectó que hay dos criterios: máximo final y orden de llegada.
2. Se decidió guardar todas las rondas para una segunda pasada.
3. Primera pasada: calcular totales finales.
4. Segunda pasada: encontrar quién cumplió primero la condición de ganador.

---

## 4) `codigos de estructuras/semana 9/Punto I semana 9.py`

### Explicación línea por línea
- **Línea 1**: Importa `sys` para lectura de `stdin`.
- **Línea 3**: Define la función principal `resolver()`.
- **Línea 4**: Comentario: leer cadena.
- **Línea 5**: `s = sys.stdin.readline().strip()` lee una línea y quita espacios extremos.
- **Línea 6**: Si la cadena queda vacía, se valida.
- **Línea 7**: `return` termina sin imprimir.
- **Línea 9**: `n = len(s)` longitud de la cadena.
- **Línea 10**: Comentario sobre `dp`.
- **Línea 11**: `dp = [0] * (n + 1)` crea arreglo de grados por prefijo.
- **Línea 13**: Comentario de variables para rolling hash.
- **Línea 14**: `h1 = 0` hash acumulado izquierda→derecha.
- **Línea 15**: `h2 = 0` hash acumulado “invertido”.
- **Línea 16**: `base = 131` base de hash polinomial.
- **Línea 17**: `pw = 1` potencia actual de la base.
- **Línea 18**: `mod = 10**9 + 7` módulo primo grande.
- **Línea 20**: `total_suma = 0` acumulador final de grados.
- **Línea 22**: Recorre prefijos de tamaño 1 a `n`.
- **Línea 23**: Convierte carácter actual a valor entero (`ord`).
- **Línea 25**: Comentario actualización hash directo.
- **Línea 26**: Actualiza `h1 = (h1*base + char_val) % mod`.
- **Línea 28**: Comentario actualización hash inverso incremental.
- **Línea 29**: Actualiza `h2 = (h2 + char_val*pw) % mod`.
- **Línea 30**: Actualiza potencia `pw = (pw*base) % mod`.
- **Línea 32**: Si hashes coinciden, se asume prefijo palíndromo.
- **Línea 33**: Inicia rama de prefijo palíndromo.
- **Línea 34-35**: Comentarios sobre fórmula del grado por mitad.
- **Línea 36**: `dp[i] = dp[i // 2] + 1` calcula grado recursivo.
- **Línea 37**: Suma ese grado al total.
- **Línea 38**: Rama del caso no palíndromo.
- **Línea 39**: Comentario.
- **Línea 40**: `dp[i] = 0`.
- **Línea 42**: Imprime suma total de grados.
- **Línea 44**: Guarda de ejecución principal.
- **Línea 45**: Llama a `resolver()`.

### Cómo se construyó el código (paso a paso)
1. Se definió la estructura `dp` para grados de prefijo.
2. Se eligió rolling hash para detectar palíndromos rápido.
3. Se actualizan hashes por cada nuevo carácter.
4. Se aplica fórmula de grado usando mitad izquierda.
5. Se acumula y reporta la suma global.

---

## 5) `codigos de estructuras/semana 10/punto C semana 10.py`

### Explicación línea por línea
- **Línea 1**: Importa `sys`.
- **Línea 3**: Define `resolver_grafos()`.
- **Línea 4-5**: Comentario sobre lectura completa por tokens.
- **Línea 6**: `input_data = sys.stdin.read().split()` lee todo separado por espacios/saltos.
- **Línea 7**: Si no hay datos, valida vacío.
- **Línea 8**: Termina función.
- **Línea 10**: `idx = 0` puntero para recorrer tokens.
- **Línea 11**: Bucle principal de casos.
- **Línea 12**: Lee `n` (nodos).
- **Línea 13**: Avanza puntero.
- **Línea 15**: Si `n == 0`, fin de entrada.
- **Línea 16**: `break`.
- **Línea 18**: Crea adyacencias vacías para nodos `1..n`.
- **Línea 21**: Inicio de lectura de bloques de aristas.
- **Línea 22**: Lee nodo origen `u`.
- **Línea 23**: Avanza puntero.
- **Línea 24**: Si `u == 0`, termina bloque de aristas.
- **Línea 25**: `break` del bloque externo.
- **Línea 27**: Bucle interno para destinos de `u`.
- **Línea 28**: Lee destino `v`.
- **Línea 29**: Avanza puntero.
- **Línea 30**: Si `v == 0`, termina lista de destinos de ese `u`.
- **Línea 31**: `break`.
- **Línea 32**: Agrega arista dirigida `u -> v`.
- **Línea 34**: Lee número de consultas.
- **Línea 35**: Avanza puntero.
- **Línea 37**: Itera por cada consulta.
- **Línea 38**: Lee nodo de inicio.
- **Línea 39**: Avanza puntero.
- **Línea 41**: Inicializa vector de visitados.
- **Línea 42**: Cola inicial con `start_node`.
- **Línea 44**: BFS/recorrido mientras haya cola.
- **Línea 45**: Saca primer elemento con `pop(0)`.
- **Línea 46**: Recorre vecinos del nodo actual.
- **Línea 47**: Si vecino no visitado.
- **Línea 48**: Marca visitado.
- **Línea 49**: Lo agrega a cola.
- **Línea 51**: Genera lista de no alcanzables.
- **Línea 53**: Prepara salida: cantidad + nodos.
- **Línea 54**: Imprime en una línea.
- **Línea 56**: Guarda de ejecución principal.
- **Línea 57**: Ejecuta `resolver_grafos()`.

### Cómo se construyó el código (paso a paso)
1. Se planteó parser con puntero para formato de entrada irregular.
2. Se construyó adyacencia dirigida por bloques.
3. Para cada consulta, se corrió un recorrido desde el nodo inicial.
4. Se listaron nodos no visitados como resultado pedido.

---

## 6) `codigos de estructuras/semana 10/punto E semana 10.py`

### Explicación línea por línea
- **Línea 1**: Importa `sys`.
- **Línea 3**: Define `resolver_dominos()`.
- **Línea 4**: Lee entrada completa en tokens.
- **Línea 5**: Si no hay entrada, valida.
- **Línea 6**: Retorna.
- **Línea 8**: Inicializa puntero `idx`.
- **Línea 9**: Lee cantidad de casos.
- **Línea 10**: Avanza puntero.
- **Línea 12**: Itera por cada caso de prueba.
- **Línea 13**: Lee `n` (dominos).
- **Línea 14**: Lee `m` (relaciones).
- **Línea 15**: Lee `l` (empujones iniciales).
- **Línea 16**: Avanza puntero tras leer cabecera.
- **Línea 18**: Crea lista de adyacencia de tamaño `n+1`.
- **Línea 20**: Recorre `m` aristas.
- **Línea 21**: Lee origen `x`.
- **Línea 22**: Lee destino `y`.
- **Línea 23**: Guarda arista `x -> y`.
- **Línea 24**: Avanza puntero 2 posiciones.
- **Línea 26**: `caidas` marca qué fichas ya cayeron.
- **Línea 27**: `stack` para DFS iterativo.
- **Línea 29**: Recorre los `l` empujones iniciales.
- **Línea 30**: Lee ficha inicial `z`.
- **Línea 31**: Avanza puntero.
- **Línea 32**: Si no cayó antes.
- **Línea 33**: Marca como caída.
- **Línea 34**: Inserta en pila.
- **Línea 36**: Inicializa contador final.
- **Línea 37**: Mientras haya nodos pendientes en pila.
- **Línea 38**: Extrae un nodo actual.
- **Línea 39**: Cuenta esa caída.
- **Línea 41**: Recorre vecinos alcanzables desde `actual`.
- **Línea 42**: Si vecino aún no cayó.
- **Línea 43**: Lo marca como caído.
- **Línea 44**: Lo apila para seguir propagación.
- **Línea 46**: Imprime total de caídas.
- **Línea 48**: Guarda principal.
- **Línea 49**: Ejecuta función.

### Cómo se construyó el código (paso a paso)
1. Se configuró lectura de múltiples casos.
2. Se modeló el efecto dominó como grafo dirigido.
3. Se cargaron fuentes iniciales de caída.
4. Se propagó con DFS iterativo hasta agotar alcanzables.

---

## 7) `codigos de estructuras/semana 10/punto F semana 10.py`

### Explicación línea por línea
- **Línea 1**: Importa `sys`.
- **Línea 2**: Importa `deque` para cola eficiente.
- **Línea 4**: Define `resolver_red()`.
- **Línea 5**: Lee toda la entrada en tokens (`input` local como lista).
- **Línea 6**: Si no hay datos, valida.
- **Línea 7**: Retorna.
- **Línea 9**: Lee `n` (nodos).
- **Línea 10**: Lee `m` (aristas).
- **Línea 12**: Crea adyacencia no dirigida.
- **Línea 13**: `ptr = 2` apunta al primer par de arista.
- **Línea 14**: Repite por cada arista.
- **Línea 15**: Lee `u`.
- **Línea 16**: Lee `v`.
- **Línea 17**: Agrega `v` a vecinos de `u`.
- **Línea 18**: Agrega `u` a vecinos de `v`.
- **Línea 19**: Avanza puntero.
- **Línea 21**: Inicializa padres para reconstrucción.
- **Línea 22**: Inicializa distancias con `-1` (no visitado).
- **Línea 24**: Cola BFS inicial con nodo `1`.
- **Línea 25**: Distancia de inicio se fija en 1.
- **Línea 27**: Bucle BFS.
- **Línea 28**: Extrae nodo frontal.
- **Línea 30**: Si llegó a destino `n`, puede cortar.
- **Línea 31**: `break`.
- **Línea 33**: Recorre vecinos.
- **Línea 34**: Si vecino no visitado.
- **Línea 35**: Asigna distancia `dist[u] + 1`.
- **Línea 36**: Guarda padre para ruta.
- **Línea 37**: Encola vecino.
- **Línea 39**: Si destino quedó sin visitar.
- **Línea 40**: Imprime `IMPOSSIBLE`.
- **Línea 41**: Si sí se alcanzó destino.
- **Línea 42**: Inicializa lista del camino.
- **Línea 43**: Comienza en `actual = n`.
- **Línea 44**: Retrocede por padres hasta `0`.
- **Línea 45**: Añade nodo actual a la ruta.
- **Línea 46**: Salta a su padre.
- **Línea 48**: Invierte la lista para orden correcto.
- **Línea 50**: Imprime longitud del camino.
- **Línea 51**: Imprime secuencia de nodos.
- **Línea 53**: Guarda principal.
- **Línea 54**: Llama función.

### Cómo se construyó el código (paso a paso)
1. Se modeló red como grafo no dirigido.
2. Se usó BFS para garantizar camino más corto.
3. Se guardó el padre de cada nodo visitado.
4. Se reconstruyó la ruta final desde `n` hacia `1`.

---

## 8) `codigos de estructuras/semana 10/punto G semana 10.py`

### Explicación línea por línea
- **Línea 1**: Importa `sys`.
- **Línea 3**: Ajusta límite de recursión (aunque aquí se usa DFS iterativo).
- **Línea 5**: Define `resolver_carreteras()`.
- **Línea 6**: Lee toda la entrada por tokens.
- **Línea 7**: Si no hay datos, valida.
- **Línea 8**: Retorna.
- **Línea 10**: Lee `n` (ciudades/nodos).
- **Línea 11**: Lee `m` (carreteras existentes).
- **Línea 13**: Crea adyacencia para grafo no dirigido.
- **Línea 14**: Inicializa puntero `idx = 2`.
- **Línea 15**: Itera por cada arista.
- **Línea 16**: Lee `u`.
- **Línea 17**: Lee `v`.
- **Línea 18**: Agrega `v` como vecino de `u`.
- **Línea 19**: Agrega `u` como vecino de `v`.
- **Línea 20**: Avanza puntero.
- **Línea 22**: `visitados` para control de componentes.
- **Línea 23**: `representantes` guardará un nodo por componente.
- **Línea 25**: Recorre nodos `1..n`.
- **Línea 26**: Si nodo `i` no fue visitado, inicia nueva componente.
- **Línea 27**: Guarda `i` como representante.
- **Línea 28**: Inicializa pila DFS con `i`.
- **Línea 29**: Marca `i` visitado.
- **Línea 30**: DFS iterativo mientras haya pila.
- **Línea 31**: Saca un nodo `u`.
- **Línea 32**: Recorre vecinos.
- **Línea 33**: Si vecino no visitado.
- **Línea 34**: Lo marca visitado.
- **Línea 35**: Lo apila.
- **Línea 37**: `k = len(representantes) - 1` carreteras nuevas mínimas.
- **Línea 38**: Imprime `k`.
- **Línea 40**: Recorre pares consecutivos de representantes.
- **Línea 41**: Imprime conexión entre componente `i` e `i+1`.
- **Línea 43**: Guarda principal.
- **Línea 44**: Ejecuta la función.

### Cómo se construyó el código (paso a paso)
1. Se identificó que el problema requiere contar componentes conexas.
2. Se aplicó DFS iterativo para descubrir cada componente.
3. Se guardó un representante por componente.
4. Se conectaron representantes consecutivos para usar el mínimo de nuevas aristas.

---

## Resumen final
- El repositorio tiene 8 scripts enfocados en estructuras/grafos y manipulación de cadenas.
- En todos los casos, la estrategia fue:
  1) leer entrada,
  2) modelar estructura de datos,
  3) recorrer/procesar,
  4) imprimir el resultado exacto pedido.


---

## Anexo: códigos completos

### `codigos de estructuras/semana 9/Punto A semana 9.py`

```python
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
```

### `codigos de estructuras/semana 9/Punto B semana 9.py`

```python
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
```

### `codigos de estructuras/semana 9/Punto E semana 9.py`

```python
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
```

### `codigos de estructuras/semana 9/Punto I semana 9.py`

```python
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
```

### `codigos de estructuras/semana 10/punto C semana 10.py`

```python
import sys

def resolver_grafos():
    # Leemos toda la entrada de golpe. split() maneja saltos de línea 
    # y múltiples espacios perfectamente para este tipo de problemas.
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        
        if n == 0:
            break 

        adj = {i: [] for i in range(1, n + 1)}
        
       
        while True:
            u = int(input_data[idx])
            idx += 1
            if u == 0:
                break 
            
            while True:
                v = int(input_data[idx])
                idx += 1
                if v == 0:
                    break
                adj[u].append(v)
                
        num_queries = int(input_data[idx])
        idx += 1
        
        for _ in range(num_queries):
            start_node = int(input_data[idx])
            idx += 1
            
            visited = [False] * (n + 1)
            queue = [start_node]
            
            while queue:
                curr = queue.pop(0)
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        
            inaccessible = [i for i in range(1, n + 1) if not visited[i]]
            
            output = [len(inaccessible)] + inaccessible
            print(" ".join(map(str, output)))

if __name__ == '__main__':
    resolver_grafos()
```

### `codigos de estructuras/semana 10/punto E semana 10.py`

```python
import sys

def resolver_dominos():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    num_test_cases = int(input_data[idx])
    idx += 1
    
    for _ in range(num_test_cases):
        n = int(input_data[idx]) 
        m = int(input_data[idx+1]) 
        l = int(input_data[idx+2]) 
        idx += 3
        
        adj = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            x = int(input_data[idx])
            y = int(input_data[idx+1])
            adj[x].append(y)
            idx += 2
            
        caidas = [False] * (n + 1)
        stack = []
        
        for _ in range(l):
            z = int(input_data[idx])
            idx += 1
            if not caidas[z]:
                caidas[z] = True
                stack.append(z)
                
        total_caidas = 0
        while stack:
            actual = stack.pop()
            total_caidas += 1 
            
            for vecino in adj[actual]:
                if not caidas[vecino]:
                    caidas[vecino] = True
                    stack.append(vecino)
                    
        print(total_caidas)

if __name__ == '__main__':
    resolver_dominos()
```

### `codigos de estructuras/semana 10/punto F semana 10.py`

```python
import sys
from collections import deque

def resolver_red():
    input = sys.stdin.read().split()
    if not input:
        return
        
    n = int(input[0])
    m = int(input[1])
    
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input[ptr])
        v = int(input[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
        
    parent = [0] * (n + 1)
    dist = [-1] * (n + 1)
    
    queue = deque([1])
    dist[1] = 1
    
    while queue:
        u = queue.popleft()
        
        if u == n: 
            break
            
        for v in adj[u]:
            if dist[v] == -1: 
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)
                
    if dist[n] == -1:
        print("IMPOSSIBLE")
    else:
        camino = []
        actual = n
        while actual != 0:
            camino.append(actual)
            actual = parent[actual]
            
        camino.reverse()
        
        print(len(camino))
        print(*(camino))

if __name__ == '__main__':
    resolver_red()
```

### `codigos de estructuras/semana 10/punto G semana 10.py`

```python
import sys

sys.setrecursionlimit(200000)

def resolver_carreteras():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    visitados = [False] * (n + 1)
    representantes = [] 

    for i in range(1, n + 1):
        if not visitados[i]:
            representantes.append(i)
            stack = [i]
            visitados[i] = True
            while stack:
                u = stack.pop()
                for vecino in adj[u]:
                    if not visitados[vecino]:
                        visitados[vecino] = True
                        stack.append(vecino)
    
    k = len(representantes) - 1
    print(k)
    
    for i in range(k):
        print(f"{representantes[i]} {representantes[i+1]}")

if __name__ == '__main__':
    resolver_carreteras()
```

