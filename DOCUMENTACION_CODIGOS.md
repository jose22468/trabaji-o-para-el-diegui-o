# Documentación paso a paso de los códigos

Este documento explica, de forma práctica y ordenada, qué hace cada script del proyecto y cómo fluye su lógica.

---

## 1) `codigos de estructuras/semana 9/Punto A semana 9.py`

### Objetivo
Contar cuántas hojas **distintas** se recolectaron, donde cada hoja está representada por una cadena (por ejemplo, `especie color`).

### Paso a paso
1. Lee un entero `n`, que indica cuántas hojas se van a registrar.
2. Crea un `set` llamado `hojas_unicas`.
3. Repite `n` veces:
   - Lee una línea (`hoja`).
   - Agrega esa línea al `set`.
4. Imprime `len(hojas_unicas)`.

### Idea clave
Un `set` en Python elimina duplicados automáticamente.

### Complejidad aproximada
- Tiempo: O(n)
- Espacio: O(n) en el peor caso.

---

## 2) `codigos de estructuras/semana 9/Punto B semana 9.py`

### Objetivo
Para cada par de cadenas `(a, b)`, imprimir sus caracteres comunes en orden alfabético y con repeticiones mínimas (intersección de multiconjuntos).

### Paso a paso
1. Lee toda la entrada con `sys.stdin.read().splitlines()`.
2. Recorre las líneas de 2 en 2 (cada par es un caso de prueba).
3. Para cada letra de `'a'` a `'z'`:
   - Cuenta cuántas veces aparece en `a` y en `b`.
   - Toma el mínimo de ambos conteos.
   - Agrega esa letra repetida `mínimo` veces al resultado.
4. Une e imprime el resultado.
5. Si hay una línea sobrante sin pareja, se ignora para evitar error.

### Idea clave
La intersección por letra se obtiene con `min(conteo_a, conteo_b)`.

### Complejidad aproximada
- Tiempo por caso: O(26 * (|a| + |b|)) debido a `count` por letra.
- Espacio: O(|resultado|).

---

## 3) `codigos de estructuras/semana 9/Punto E semana 9.py`

### Objetivo
Determinar el ganador de un juego de puntajes acumulados cuando puede haber empates en puntaje final.

### Paso a paso
1. Lee `n` rondas.
2. En cada ronda:
   - Lee `nombre` y `puntos`.
   - Guarda la ronda en una lista `rondas`.
   - Actualiza `puntajes_finales[nombre]`.
3. Calcula `max_puntaje` (el mejor puntaje final).
4. Recorre nuevamente `rondas` acumulando en `puntajes_actuales`.
5. El primer jugador que cumpla ambas condiciones gana:
   - Su acumulado parcial ya es `>= max_puntaje`.
   - Su puntaje final total es exactamente `max_puntaje`.
6. Imprime su nombre y termina.

### Idea clave
Se hace en dos pasadas: una para conocer el máximo final y otra para desempatar por “quién llegó primero”.

### Complejidad aproximada
- Tiempo: O(n)
- Espacio: O(n) por almacenamiento de rondas y mapas.

---

## 4) `codigos de estructuras/semana 9/Punto I semana 9.py`

### Objetivo
Calcular la suma de grados de palíndromo de todos los prefijos de una cadena.

### Paso a paso
1. Lee la cadena `s`.
2. Crea `dp` donde `dp[i]` es el grado de palíndromo del prefijo de longitud `i`.
3. Inicializa variables de rolling hash:
   - `h1`: hash adelante
   - `h2`: hash “reverso” acumulado
   - `base`, `mod`, `pw`
4. Para cada posición `i` (1 a n):
   - Actualiza `h1` con el nuevo carácter.
   - Actualiza `h2` con potencia `pw`.
   - Si `h1 == h2`, considera el prefijo como palíndromo:
     - `dp[i] = dp[i // 2] + 1`
     - acumula en `total_suma`
   - Si no, `dp[i] = 0`.
5. Imprime `total_suma`.

### Idea clave
Si un prefijo es palíndromo, su grado depende recursivamente del grado de su mitad izquierda.

### Complejidad aproximada
- Tiempo: O(n)
- Espacio: O(n)

> Nota: con hashing existe posibilidad teórica de colisiones, aunque suele ser baja con buen módulo/base.

---

## 5) `codigos de estructuras/semana 10/punto C semana 10.py`

### Objetivo
Dado un grafo dirigido y varios nodos de inicio, reportar qué nodos no son alcanzables desde cada inicio.

### Paso a paso
1. Lee toda la entrada tokenizada (`split()`).
2. Mientras haya casos:
   - Lee `n` (nodos). Si `n == 0`, termina.
   - Inicializa lista de adyacencia `adj`.
3. Construye el grafo con el formato:
   - `u v1 v2 ... 0`
   - termina bloque con una línea que empieza en `0`.
4. Lee número de consultas `num_queries`.
5. Para cada nodo de inicio:
   - Ejecuta BFS usando una cola.
   - Marca visitados alcanzables.
   - Construye lista `inaccessible` con los no visitados.
   - Imprime cantidad y nodos inaccesibles.

### Idea clave
Aplicar búsqueda por anchura por consulta para identificar alcanzabilidad.

### Complejidad aproximada
- Por consulta: O(n + m)
- Total: O(q * (n + m))

---

## 6) `codigos de estructuras/semana 10/punto E semana 10.py`

### Objetivo
Simular caída de fichas de dominó en un grafo dirigido: si cae una, puede tumbar a otras conectadas.

### Paso a paso
1. Lee `num_test_cases`.
2. Por cada caso:
   - Lee `n` (nodos), `m` (aristas), `l` (empujones iniciales).
   - Construye adyacencia dirigida.
3. Marca qué fichas ya cayeron en `caidas`.
4. Carga una pila con los nodos empujados inicialmente.
5. Mientras la pila tenga elementos:
   - Saca un nodo `actual`.
   - Incrementa `total_caidas`.
   - Recorre sus vecinos y empuja los no caídos.
6. Imprime `total_caidas`.

### Idea clave
Es un DFS iterativo desde múltiples fuentes iniciales.

### Complejidad aproximada
- Tiempo: O(n + m) por caso (cada nodo/arista se procesa a lo sumo una vez útil).
- Espacio: O(n + m).

---

## 7) `codigos de estructuras/semana 10/punto F semana 10.py`

### Objetivo
Encontrar el camino más corto (en número de nodos/aristas) entre el nodo `1` y el nodo `n` en un grafo no dirigido.

### Paso a paso
1. Lee `n` y `m`.
2. Construye lista de adyacencia no dirigida.
3. Inicializa:
   - `dist` con `-1` (no visitado)
   - `parent` para reconstruir camino.
4. Ejecuta BFS desde el nodo `1`.
5. Si `dist[n] == -1`, imprime `IMPOSSIBLE`.
6. Si sí existe ruta:
   - Reconstruye el camino desde `n` usando `parent`.
   - Invierte la lista para obtener orden `1 -> n`.
   - Imprime longitud y secuencia del camino.

### Idea clave
BFS en grafo no ponderado garantiza camino mínimo en cantidad de pasos.

### Complejidad aproximada
- Tiempo: O(n + m)
- Espacio: O(n + m)

---

## 8) `codigos de estructuras/semana 10/punto G semana 10.py`

### Objetivo
Encontrar componentes conexas de un grafo no dirigido y proponer carreteras para conectar todo el país con el mínimo de nuevas conexiones.

### Paso a paso
1. Lee `n` y `m`.
2. Construye adyacencia no dirigida.
3. Recorre nodos del 1 al `n`:
   - Si un nodo no está visitado, inicia DFS iterativo desde él.
   - Guarda ese nodo como representante de una componente.
4. Si hay `c` componentes, se necesitan `c - 1` carreteras.
5. Imprime `k = len(representantes) - 1`.
6. Conecta representantes consecutivos:
   - `rep[0]-rep[1]`, `rep[1]-rep[2]`, etc.

### Idea clave
Conectar componentes en cadena usa exactamente el mínimo número de aristas nuevas.

### Complejidad aproximada
- Tiempo: O(n + m)
- Espacio: O(n + m)

---

## Recomendaciones generales para estudiar estos códigos

1. **Empieza por identificar el tipo de problema**: conteo, BFS, DFS, hashing, etc.
2. **Dibuja un caso pequeño** en papel antes de ejecutar mentalmente el código.
3. **Rastrea variables clave** (`visited`, `parent`, `dp`, acumuladores).
4. **Valida complejidad** para saber si escala al tamaño del problema.
5. **Prueba bordes**: entrada vacía, nodos aislados, empates, cadenas muy cortas.

