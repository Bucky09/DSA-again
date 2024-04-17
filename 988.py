class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []

        def dfs(node, ds):
            if not node:
                return
            ds.append(chr(97+node.val))
            
            if not node.left and not node.right:
                ans.append("".join(ds[::-1]))
                ds.pop()
                return
            dfs(node.left, ds)
            dfs(node.right, ds)
            ds.pop()
                

        dfs(root, [])
        ans.sort()
        return ans[0]
