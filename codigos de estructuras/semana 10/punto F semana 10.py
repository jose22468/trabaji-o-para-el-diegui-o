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
    