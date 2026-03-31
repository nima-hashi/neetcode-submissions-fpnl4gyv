# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        return prev
    
    def findMid(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        
        # find mid point
        mid = self.findMid(head)

        # reverse 2nd half
        second = self.reverseList(mid.next)
        
        # end 1st half
        mid.next = None

        # merge first and second
        first = head

        while first and second:
            # save next pointers
            tmp1 = first.next
            tmp2 = second.next

            # reorder links
            first.next = second
            second.next = tmp1

            # move forward
            first = tmp1
            second = tmp2


