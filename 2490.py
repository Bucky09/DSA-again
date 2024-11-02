class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Loop through each word and check adjacent pairs
        for i in range(len(words)):
            # Check if the last character of the current word is equal to the first character of the next word
            if words[i][-1] != words[(i + 1) % len(words)][0]:
                return False
        
        # If all checks passed, the sentence is circular
        return True
