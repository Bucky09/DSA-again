class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [1, 2, 4]
        for i in range(3, n+1): 
            dp.append((dp[i-3] + dp[i-2] + dp[i-1]) % 1_000_000_007)
        ans = dp[n] 
        for i in range(n): 
            ans = (ans + dp[i] * dp[n-1-i]) % 1_000_000_007
        return ans
