public int prefixCount(String[] words, String pref) {
    int ans = 0;
    for(String w: words) 
        ans += (w.indexOf(pref) == 0) ? 1 : 0;
    return ans;
}
