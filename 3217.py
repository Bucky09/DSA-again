class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        nums_set = set(nums)

        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
