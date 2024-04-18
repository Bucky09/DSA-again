class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n, total = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total+=4
                    if i > 0 and grid[i-1][j] == 1: total-=2
                    if j > 0 and grid[i][j-1] == 1: total-=2
        return total
