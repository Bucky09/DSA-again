class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            twice_of_val = curr.val * 2
            if twice_of_val < 10:
                curr.val = twice_of_val
            elif prev:  # other than first node

                curr.val = twice_of_val % 10

                prev.val += 1
            else:  

                head = ListNode(1, curr)

                curr.val = twice_of_val % 10
            prev = curr
            curr = curr.next

        return head
