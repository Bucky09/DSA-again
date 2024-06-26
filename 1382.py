class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        allNodes = []
        def inorder(node):
            if node:
                inorder(node.left)
                allNodes.append(node)
                inorder(node.right)
        inorder(root)
        def buildBst(l, r):
            if l > r: 
                return None
            mid = l + (r-l)//2
            root = allNodes[mid]
            root.left = buildBst(l, mid -1)
            root.right = buildBst(mid+1, r)
            return root
        return buildBst(0, len(allNodes)-1)
