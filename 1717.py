class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            return self.maximumGain(s[::-1], y, x)
        
        def solve(s: str, a: str, b: str, x: int) -> int:
            stack = []
            res = 0
            for c in s:
                if not stack or c != b:
                    stack.append(c)
                elif stack[-1] == a:
                    stack.pop()
                    res += x
                else:
                    stack.append(c)
            return res, stack
    
        ab, stack = solve(s, 'a', 'b', x)
        ba, _ = solve(''.join(stack), 'b', 'a', y)
        return ab + ba
