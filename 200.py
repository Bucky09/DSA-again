class Solution:
    def __init__(self):
        self.islands = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        def trace(r, c):
            if not(0 <= r < row) or not(0 <= c < col) or grid[r][c] in ('0', -1):
                return
            grid[r][c] = -1
            trace(r, c + 1), trace(r, c - 1), trace(r + 1, c), trace(r - 1, c)

        row, col = len(grid), len(grid[0])
        for rr in range(row):
            for cc in range(col):
                if grid[rr][cc] == '1':
                    trace(rr, cc)
                    self.islands += 1
        return self.islands        
