class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result
################################################
################################################

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result, i = 0, 0
        curr = 1
        while curr <= n:
            if i < len(nums) and nums[i] <= curr:
                curr += nums[i]
                i += 1
            else:
                curr += curr
                result += 1
        return result
