class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1 for _ in range(n+1)]

        def dfs(n):
            if n==2 or n==1:
                return 1
            if n==0:
                return 0
            if dp[n] != -1:
                return dp[n]
            dp[n]=dfs(n-2)+dfs(n-1)+dfs(n-3)
            return dp[n]

        return dfs(n)
