class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the end of list2
        curr = list2
        while curr.next:
            curr = curr.next
        list2_end = curr
        
        # Find the nodes at positions a-1 and b+1 in list1
        prev_a = list1
        for _ in range(a - 1):
            prev_a = prev_a.next
        
        next_b = list1
        for _ in range(b + 1):
            next_b = next_b.next
        
        # Connect the parts of list1 with list2
        prev_a.next = list2
        list2_end.next = next_b
        
        return list1
