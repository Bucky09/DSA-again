class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left,cur,res=0,1,0
        for right in range(len(nums)):
            cur*=nums[right]
            while cur>=k:
                cur//=nums[left]
                left+=1
            res+=right-left+1
        return res
