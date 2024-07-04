class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head.next

        sum = 0
        while r:
            if r.val == 0:
                l = l.next
                l.val = sum
                sum = 0
            else:
                sum += r.val
            r = r.next
        
        l.next = None
        return head.next
