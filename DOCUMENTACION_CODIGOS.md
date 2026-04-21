# Documentación línea por línea de todos los códigos

Esta guía explica **qué hace cada línea** de cada script del repositorio.
# Documentación paso a paso de los códigos

Este documento explica, de forma práctica y ordenada, qué hace cada script del proyecto y cómo fluye su lógica.

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

