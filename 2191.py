class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def mp(num):
            res = 0
            m = 1
            if num==0:
                return mapping[num]
            while(num):
                res = res+ mapping[num%10]*m
                num=num//10
                m*=10
            return res
        
        nums.sort(key = lambda x: mp(x))
        return nums
