class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diffs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        return longestSubAtMostK(diffs, maxCost)

def longestSubAtMostK(nums, k):
    l = 0
    cur = 0
    for num in nums:
        cur += num
        if cur > k:
            cur -= nums[l]
            l += 1
    return len(nums) - l
