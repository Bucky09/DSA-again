class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = dict()
        seenq = set()
        j_cur = j_nex = 0
        for i, x in enumerate(nums):
            if x in seen.keys():
                seenq.remove(seen[x])
            seen[x] = i
            seenq.add(i)

            if len(seen) < k: 
                continue
            
            if len(seen) > k:
                del(seen[nums[j_nex]])
                seenq.remove(j_nex)
                j_cur = j_nex + 1
                j_nex = j_nex + 1
            
            while j_nex < i and j_nex not in seenq:
                j_nex += 1
            
            ans += j_nex - j_cur + 1
        return ans
