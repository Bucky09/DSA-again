class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        cur_min = float("inf")
        cur_max = 0
        ans = 0
        index_min = 0
        index_max = 0
        l = 0

        for r in range(len(nums)):

            if nums[r] <= cur_min:
                cur_min = nums[r]
                index_min = r
                if cur_min < minK:
                    l = r + 1
                    cur_min = float("inf")
                    cur_max = 0
            if nums[r] >= cur_max:
                cur_max = nums[r]
                index_max = r
                if cur_max > maxK:
                    l = r + 1
                    cur_min = float("inf")
                    cur_max = 0
            if cur_min == minK and cur_max == maxK:
                ans += min(index_min, index_max) - l + 1

                
        return ans
            
