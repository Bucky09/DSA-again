class Solution {
    public int minBitFlips(int start, int goal) {
        int diff = start^goal;
        int cnt =0;
        int end = (int)(Math.log(diff)/Math.log(2));

        for(int i=0;i<end+1;i++){
            if((diff &(1<<i)) > 0)
            cnt++;
        }
        return cnt;
    }
}
