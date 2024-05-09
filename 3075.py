class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        children = sorted(happiness, reverse=True)

        if children[k-1] >= k-1:
            return sum(children[:k]) - ((0 + k-1) * k // 2)

        res = 0
        for i, h in enumerate(children[:k]):
            if h - i <= 0:
                break
            res += h - i
        return res
