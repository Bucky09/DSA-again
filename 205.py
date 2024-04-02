class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapping = {}  # Dictionary to store character mappings from s to t
        visited = set()  # Set to keep track of characters already mapped
        
        for char_s, char_t in zip(s, t):
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                if char_t in visited:
                    return False
                mapping[char_s] = char_t
                visited.add(char_t)
        
        return True

