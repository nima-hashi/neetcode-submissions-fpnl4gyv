# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        leftPrev = dummy
        cur = dummy.next

        for i in range(left-1):
            leftPrev = leftPrev.next
            cur = cur.next
        
        prev = None
        for i in range(right-left+1):
            save = cur.next 
            cur.next = prev
            prev = cur
            cur = save
        
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next