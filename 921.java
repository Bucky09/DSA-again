class Solution {
    public int minAddToMakeValid(String s) {
        int unmatchedOpenBrackets = 0, unmatchedCloseBrackets = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                ++unmatchedOpenBrackets;
            }else if (unmatchedOpenBrackets > 0) {
                --unmatchedOpenBrackets;
            }else {
                ++unmatchedCloseBrackets;
            }
        }
        return unmatchedOpenBrackets + unmatchedCloseBrackets;
    }
}
