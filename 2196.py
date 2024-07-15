# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        childs = set()
        for pv, cp, is_left in descriptions:
            parent = tree.setdefault(pv, TreeNode(val=pv)) 
            child = tree.setdefault(cp, TreeNode(val=cp)) 
            childs.add(cp)

            if is_left == 0:
                parent.right = child
            else:
                parent.left = child
        
        for node_val, node in tree.items():
            if node_val not in childs:
                return node

        return None
