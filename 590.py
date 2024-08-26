class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)

            res.append(node.val)

        dfs(root)
        return res
