class Solution {
    public int nthUglyNumber(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 0;
        dp[1] = 1;

        int i2, i3, i5;
        i2 = i3 = i5 = 1;

        for (int i = 2; i <= n; i++) {
            int n2 = dp[i2] * 2;
            int n3 = dp[i3] * 3;
            int n5 = dp[i5] * 5;

            int toInsert = Math.min(n2, Math.min(n3, n5));
            dp[i] = toInsert;
            if (toInsert == n2)
                i2++;
            if (toInsert == n3)
                i3++;
            if (toInsert == n5)
                i5++;
        }
        return dp[n];

    }
}
