class Solution {
        public int isPrefixOfWord(String sentence, String searchWord) {
            for (int i = 0, searchIndex = 0, searchSize = searchWord.length(), wordIndex = 1; 
                                        i < sentence.length(); ++i) {
                char c = sentence.charAt(i);
                if (c == ' ') {
                    ++wordIndex;
                    searchIndex = 0;
                }else if (searchIndex < searchSize) {
                    searchIndex = c == searchWord.charAt(searchIndex) ? ++searchIndex : searchSize + 1; 
                }
                if (searchIndex == searchSize) {
                    return wordIndex;
                }
            }
            return -1;
        }
}
