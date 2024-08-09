class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(r, c):
            # Check if all numbers are distinct and in range [1, 9]
            nums = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r + i][c + j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)
            
            # Calculate the expected magic sum (sum of first row)
            magic_sum = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            
            # Check rows, columns, and diagonals
            for i in range(3):
                if (grid[r + i][c] + grid[r + i][c + 1] + grid[r + i][c + 2] != magic_sum or
                    grid[r][c + i] + grid[r + 1][c + i] + grid[r + 2][c + i] != magic_sum):
                    return False
            
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != magic_sum or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != magic_sum):
                return False
            
            return True
        
        row, col = len(grid), len(grid[0])
        count = 0
        
        # Iterate through all possible top-left corners of 3x3 subgrids
        for r in range(row - 2):
            for c in range(col - 2):
                if isMagicSquare(r, c):
                    count += 1
        
        return count
