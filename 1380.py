class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minR = [min(i) for i in matrix]
        maxC = [i for i in range(len(matrix) - (len(matrix) - len(matrix[0])))]
        mid = []
        for i in range(len(matrix) - (len(matrix) - len(matrix[0]))):
            for ii in range(len(matrix)):
                mid.append(matrix[ii][i])
            maxC[i] = max(mid)
            mid.clear()
        for i in minR:
            if i in maxC: return [i]
        return []
