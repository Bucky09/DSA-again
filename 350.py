class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = []
        for num in nums1:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num in nums2:
            if num in hashmap and hashmap[num] > 0:
                res.append(num)
                hashmap[num] -= 1
        return res
