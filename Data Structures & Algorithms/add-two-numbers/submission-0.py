# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedaList(l):

        prev = None
        cur = l

        while cur:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        remainder = 0

        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + remainder
            remainder = total // 10
            cur.next = ListNode(total % 10)
    
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        
        if remainder:
            cur.next = ListNode(remainder)
        
        return dummy.next






        