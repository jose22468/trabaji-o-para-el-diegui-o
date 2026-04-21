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