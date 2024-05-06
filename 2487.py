class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the list
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Initialize a dummy node to hold the result
        dummy_head = ListNode(-1)
        temp_prev, curr = dummy_head, prev
        # Traverse the reversed list, keeping nodes greater or equal to previous
        while curr:
            if curr.val >= temp_prev.val:
                temp_prev.next = curr
                temp_prev = curr
                curr = curr.next
            else:
                curr = curr.next
        temp_prev.next = None
        
        # Reverse the result list again
        new_prev = None
        curr = dummy_head.next
        while curr:
            curr.next, new_prev, curr = new_prev, curr, curr.next

        return new_prev
