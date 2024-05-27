import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)+1):
            if i == len(nums[bisect.bisect_left(nums, i):]):
                return i
        
        return -1
