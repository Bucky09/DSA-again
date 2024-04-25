class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        lenghts = [0]*26
        a = ord('a')
        for c in s:
            o = ord(c) - a
            lenghts[o] = max(lenghts[max(0,o-k):min(26,o+k+1)]) + 1
        return max(lenghts)
