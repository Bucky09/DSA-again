class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        articulationPoints = 0
        adj = self.getAdj(grid)
        num, low = [0]*(m*n), [0]*(m*n)
        count, aps = 0, [0]*(m*n)

        def dfs(v, prev):
            nonlocal count

            childCount = 0
            count += 1
            num[v] = low[v] = count

            for u in adj[v]:
                if u == prev:
                    continue

                if num[u] == 0:
                    dfs(u, v)
                    low[v] = min(low[v], low[u])

                    if num[v] <= low[u]:
                        aps[v]= 1
                    childCount += 1
                else:
                    low[v] = min(low[v], num[u])

            return childCount

        connectedGroups = 0
        for i in range(m):
            for j in range(n):
                idx = self.getIdx(i, j, m, n)
                if grid[i][j] == 1 and num[idx] == 0:
                    connectedGroups += 1
                    aps[idx] = 1 if (dfs(idx, -1) >= 2) else 0


        if connectedGroups > 1:
            return 0

        if sum(aps) >= 1:
            return 1

        return min(count, 2)

    def getAdj(self, grid):
        m, n = len(grid), len(grid[0])
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        adj = defaultdict(list)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                idx = self.getIdx(i, j, m, n)

                for d in dir:
                    newX, newY = i+d[0], j+d[1]
                    if not self.isValid(newX, newY, m, n) or grid[newX][newY] == 0:
                        continue
                    
                    newIdx = self.getIdx(newX, newY, m, n)
                    adj[idx].append(newIdx)
        
        return adj


    def isValid(self, x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n

    def getIdx(self, x, y, m, n):
        return x*n+y
    
    [1,1,0,1,1]
    [1,1,1,1,1]
    [1,1,0,1,1]
    [1,1,0,1,1]
