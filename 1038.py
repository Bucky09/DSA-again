class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        su = 0
        def rec(curr:TreeNode):
            nonlocal su
            if curr.right:
                rec(curr.right)
            su += curr.val
            curr.val = su
            if curr.left:
                rec(curr.left)
        rec(root)
        return root
