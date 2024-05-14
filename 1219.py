class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        def isStartingPoint(i, j):
            directions = [(i+1, j), (i,j+1), (i-1,j), (i,j-1)]
            direction = 0
            for (row_idx, col_idx) in directions:
                if row_idx<m and col_idx<n and grid[row_idx][col_idx]!=0:
                    direction += 1
            return direction <= 2
        def dfs(r,c,visited):
            res=0
            for x,y in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=x<m and 0<=y<n and grid[x][y]!=0 and (x,y) not in visited:
                    res=max(res,grid[x][y]+dfs(x,y,visited|{(x,y)}))
            return res
        maximum=0
        for i in range(m):
            for j in range(n):
                if isStartingPoint(i,j):
                    maximum=max(maximum,grid[i][j]+dfs(i,j,{(i,j)}))
        
        return maximum
