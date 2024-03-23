class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst=[]
        start=head
        while(start!=None):
            lst.append(start)
            start=start.next
        length=len(lst)
        low=1
        high=length-1
        start=head
        while(low<=high):
            
            start.next=lst[high]
            high-=1
            start=start.next
            start.next=lst[low]
            start=start.next
            low+=1
        start.next=None
