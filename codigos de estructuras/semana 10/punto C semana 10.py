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