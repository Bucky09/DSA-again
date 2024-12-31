class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        return solveRec(days, costs);
    }

    public int solveRec(int[] d, int[] c){
        int n = d.length;
        int[] dp = new int[n+1];
        Arrays.fill(dp, -1);
        return solve(0, n, d, c, dp);
    }
    public int solve(int i, int n, int[] d, int[] c, int[] dp){
        if(i >= n){
            return 0;
        }

        if (dp[i] != -1)
            return dp[i];

        int opt1 = c[0] + solve(i+1, n, d, c, dp);

        int ni = n;
        for(int q = i; q<n; q++){
            if(d[i]+7 <= d[q]){
                ni = q;
                break;
            }
        }
        int opt2 = c[1] + solve(ni, n, d, c, dp);

        ni = n;
        for(int q = i; q<n; q++){
            if(d[i]+30 <= d[q]){
                ni = q;
                break;
            }
        }
        int opt3 = c[2] + solve(ni, n, d, c, dp);

        int res = Math.min(opt1, Math.min(opt2, opt3));
        dp[i] = res;
        return res;
    }
}
