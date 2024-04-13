class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        area = 0
        def histogram(arr):
            ans = 0
            stack = []
            for i,h in enumerate(arr):
                start = i
                while stack and stack[-1][1]>h:
                    index, height = stack.pop()
                    ans = max(ans, height*(i-index))
                    start = index
                stack.append((start, h))
            for i,h in stack:
                ans = max(ans, h*(len(arr)-i))
            return ans
        counter = [0]*len(matrix[0])
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '0':
                    counter[i] = 0
                else:
                    counter[i] += 1
            area = max(area, histogram(counter))
        return area
