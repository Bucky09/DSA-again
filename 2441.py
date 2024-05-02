class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        c=-1
        for i in nums:
            i=i*-1
            if i in set(nums) and i>c:   c=i
        return c
