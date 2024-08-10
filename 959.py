class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if x != rootMapping[x]:
                return find(rootMapping[x])
            return x
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rootX < rootY:
                    rootMapping[rootY] = rootX
                else:
                    rootMapping[rootX] = rootY
                return True
            return False
        
        n = len(grid)
        result = 1
        rootMapping = [None for i in range(n+1)] * (n+1)
        for i in range(n+1):
            for j in range(n+1):
                id = i * (n+1) + j
                if i == 0 or i == n or j == 0 or j == n:
                    rootMapping[id] = 0
                else:
                    rootMapping[id] = id
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == ' ':
                    continue
                a = None
                b = None
                if grid[i][j] == '/':
                    a = i * (n+1) + (j+1)
                    b = (i+1) * (n+1) + j
                else: # '\\'
                    a = i * (n+1) + j
                    b = (i+1) * (n+1) + (j+1)
                if not union(a, b):
                    result += 1
            
        return result
