class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        k = sum(nums)
        ones = sum(nums[-k:])
        max_fill = ones
        for i in range(len(nums)):
            ones += nums[i]-nums[i-k]
            if ones > max_fill:
                max_fill = ones
        return k - max_fill
