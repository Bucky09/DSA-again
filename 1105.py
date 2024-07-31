class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def solve(idx, currwidth, maxht):
            if idx == len(books):
                return 0
            
            op1, op2 = float("inf"), float("inf")
            if currwidth + books[idx][0] <= shelfWidth:
                op1 = solve(idx+1, books[idx][0] + currwidth, max(maxht, books[idx][1])) + max(maxht, books[idx][1]) - maxht
            
            op2 = solve(idx+1, books[idx][0], books[idx][1]) + books[idx][1]
            
            return min(op1, op2)
        
        return solve(0, 0, 0)
