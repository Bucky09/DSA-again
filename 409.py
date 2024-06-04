class Solution:
    def longestPalindrome(self, s: str) -> int:
        cmap = {}
        ans = 0
        for c in s:
            if c not in cmap:
                cmap[c] = 0
            cmap[c]+=1
        for key,val in cmap.items():
            if val%2==0:
                ans+=val
            else:
                ans+=(val-1)
        if ans < len(s):
            ans+=1
        return ans
