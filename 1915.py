class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dic = {chr(ord('a') + i) : (1 << i) for i in range(10)}
        diff = list(dic.values())
        masks = {h:0 for h in range(1 << 10)}
        mask = 0
        masks[0] += 1
        for c in word:
            mask ^= dic[c]
            masks[mask] += 1
        ans = 0
        for mask in masks:
            ans += (masks[mask] - 1) * (masks[mask])
            for m in diff:
                ans += masks[mask] * masks[mask ^ m]
        return ans // 2
