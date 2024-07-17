# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        
        def helper(x):
            if not x:
                return None
            x.left = helper(x.left)
            x.right = helper(x.right)
            if x.val in to_delete:
                if x.left:
                    ans.append(x.left)
                if x.right:
                    ans.append(x.right)
                return None
            return x
        root = helper(root)
        if root:
            ans.append(root)
        return ans
