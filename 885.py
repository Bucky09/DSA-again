class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        ans = []
        i, j = rStart, cStart
        di, dj = 0, 1
        n = 0
        while len(ans) < rows * cols:
            for k in range(n // 2 + 1):
                if 0 <= i < rows and 0 <= j < cols:
                    ans.append([i, j])
                i, j = i + di, j + dj
            di, dj = dj, -di
            n += 1
        
        return ans
