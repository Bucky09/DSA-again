class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        stack = [(root, 0)]
        while stack:
            root, pos = stack.pop()
            if pos and not root.left and not root.right:
                total += root.val
            if root.left:
                stack.append((root.left, 1))
            if root.right:
                stack.append((root.right, 0))

        return total
