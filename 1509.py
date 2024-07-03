class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        smallest = heapq.nsmallest(4, nums)
        largest = heapq.nlargest(4, nums)
        
        return min(
            largest[0] - smallest[3],
            largest[1] - smallest[2],
            largest[2] - smallest[1],
            largest[3] - smallest[0]
        )
