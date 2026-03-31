"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        # create hashmap --> {old:newcopy}
        oldToNew = {None:None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToNew[cur] = copy
            cur = cur.next

        # connecting rand pointers for copies
        cur = head
        while cur:
            oldToNew[cur].random = oldToNew[cur.random]
            oldToNew[cur].next = oldToNew[cur.next]
            cur = cur.next
        
        return oldToNew[head]

        