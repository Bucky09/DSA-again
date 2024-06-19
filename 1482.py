class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(x):
            total = 0
            currcount = 0
            for b in bloomDay:
                if x>=b:
                    currcount += 1
                else:
                    total += currcount // k
                    if total >= m:
                        return True
                    currcount = 0
            total += currcount // k
            return total >= m

        if m*k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left)//2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left
