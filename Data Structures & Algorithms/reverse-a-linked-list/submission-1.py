# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        upNext = None

        while curr:
            save = curr.next
            curr.next = upNext
            upNext = curr
            curr = save
        
        return upNext

        
        