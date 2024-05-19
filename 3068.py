class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n, res, minD, cnt = len(nums), 0, inf, 0
        for num in nums:
            d = (num^k)-num
            if d > 0:
                cnt ^= 1
                if d < minD:
                    minD = d
                res += num^k
            else:
                if -d < minD:
                    minD = -d
                res += num
        if cnt:
            res -= minD
        return res
