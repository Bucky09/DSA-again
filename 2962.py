class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = ans = cntr = 0
        maxel = max(nums)
        for r in range(len(nums)):
            ans += r - l 
            if nums[r] == maxel:
                cntr += 1
            if cntr < k:
                continue
            
            while nums[l] != maxel:
                l += 1
            l += 1
            cntr -= 1
        
        ans += r - l + 1

        return len(nums) * (len(nums) + 1) // 2 - ans
