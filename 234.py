class Solution:
    def isPalindrome(self, head) -> bool:
        forward = []
        current_node = head
        while current_node:
            forward.append(current_node.val)
            current_node = current_node.next

        backward = []
        
        def backwards(node):
            if node:
                backwards(node.next)
                backward.append(node.val)
        backwards(head)
        if backward == forward:
            return True
        else:
            return False
        
