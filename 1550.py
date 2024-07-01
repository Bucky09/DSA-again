class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(1, len(arr) - 1):
            if arr[i - 1] % 2 + arr[i] % 2 + arr[i + 1] % 2 == 3:
                return True
        return False
