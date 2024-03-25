class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num = [0]*len(nums)
        res = []
        for n in nums:
            if num[n-1]==0:
                num[n-1]=n
            else:
                res.append(n)
        return res
