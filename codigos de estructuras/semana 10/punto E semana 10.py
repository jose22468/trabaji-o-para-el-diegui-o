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