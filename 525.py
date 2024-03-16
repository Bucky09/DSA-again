class Solution:
    def findMaxLength(self, A: List[int]) -> int:
        ans = 0
        c = 0
        C = [0] * (len(A) * 2 + 1)
        C[0] = 1
        for i, a in enumerate(A, 2):
            if a: c += 1
            else: c -= 1
            if C[c]:
                i -= C[c]
                if i > ans: ans = i
            else:
                C[c] = i
        return ans
