class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return 
        if depth==1:
            return TreeNode(val, root, None)
        q= deque()
        q.append(root)
        currlevel=1

        while q:
            if currlevel==depth-1:
                break
            
            currlen= len(q)
            for i in range(currlen):

                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            currlevel+=1
        
        for node in q:
            curr_left= node.left
            node.left= TreeNode(val,curr_left, None)

            curr_right= node.right
            node.right= TreeNode(val, None, curr_right)
        
        return root
