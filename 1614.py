class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        stack = []
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                depth = max(depth, len(stack))
                stack.pop()
        return depth
