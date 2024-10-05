/**
 * Sliding Window
 *
 * Time Complexity: O(S1 + (S2-S1)) = O(S2)
 *
 * Space Complexity: O(M) = O(26) = O(1)
 *
 * S1 = Length of input string s1. S2 = Length of input string s2. M = Range of
 * character set which is 26 in this case.
 */
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1 == null || s2 == null) {
            throw new IllegalArgumentException("Input string is null");
        }

        int l1 = s1.length();
        int l2 = s2.length();
        if (l1 == 0) {
            return true;
        }
        if (l2 < l1) {
            return false;
        }

        int[] countMap = new int[26];

        for (int i = 0; i < l1; i++) {
            // Adding Characters of S1 in the window
            countMap[s1.charAt(i) - 'a']++;
            // Removing Characters of S2 in the window
            countMap[s2.charAt(i) - 'a']--;
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            // Counting the characters which have count as zero.
            // Either these characters are not present in the window or appear same number
            // of times in the window.
            if (countMap[i] == 0) {
                count++;
            }
        }
        // If count is 26, all S1 characters appear same number of times in S2.
        if (count == 26) {
            return true;
        }

        for (int i = l1; i < l2; i++) {
            // Adding new character in the window.
            int r = s2.charAt(i) - 'a';
            countMap[r]--;
            if (countMap[r] == 0) {
                count++;
            } else if (countMap[r] == -1) {
                count--;
            }

            // Removing old character from the window.
            int l = s2.charAt(i - l1) - 'a';
            countMap[l]++;
            if (countMap[l] == 0) {
                count++;
            } else if (countMap[l] == 1) {
                count--;
            }

            if (count == 26) {
                return true;
            }
        }

        return false;
    }
}
