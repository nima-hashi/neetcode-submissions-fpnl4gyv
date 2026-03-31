# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # make slow point to elm before one that needs to be deleted
        slow = head
        fast = head

        for i in range(n + 1):
            if fast:
                fast = fast.next
            else:
                return head.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        # delete it

        slow.next = slow.next.next

        return head


        