# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:

        greaterNodes = []
        stack = []

        cur = head
        index = 0
        while cur:
            greaterNodes.append(0)
            while stack and stack[-1][1] < cur.val:
        
                i, v = stack.pop()
                greaterNodes[i] = cur.val
            stack.append([index, cur.val])
            cur = cur.next
            index += 1
        
        for i, v in stack:
            greaterNodes[i] = 0

        return greaterNodes

        