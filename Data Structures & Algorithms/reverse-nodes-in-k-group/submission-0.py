# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node, k):
        prev = None
        cur = node
        while cur and k > 0:
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
            k -= 1
        return prev, cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kthGroup = prevGroup
            for i in range(k):
                kthGroup = kthGroup.next
                if not kthGroup:
                    return dummy.next
            nextGroup = kthGroup.next
            prev, cur = self.reverseList(prevGroup.next, k)

            tail = prevGroup.next 
            prevGroup.next = prev
            tail.next = nextGroup

            prevGroup = tail


