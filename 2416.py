class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        for w in words:
            node = trie
            for c in (w):
                if c not in node: node[c] = {}
                node = node[c]
                node['$'] = 1 if '$' not in node else node['$']+1
        #print(trie)
        for i in range(len(words)):
            ans = 0
            node = trie
            for c in words[i]:
                node = node[c]
                ans += node['$']
            words[i] = ans
        return words        
