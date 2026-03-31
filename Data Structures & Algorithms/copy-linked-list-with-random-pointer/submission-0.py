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
            return None
        
        # clone each node and set it after the original 
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        
        #  setting up random pointers for the cloned nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # seperate the clones from original

        old = head
        new = head.next

        new_head = new

        while old:
            old_next = old.next.next
            if old_next:
                new.next = old_next.next 
            else:
                new.next = None
            old.next = old_next
            old = old_next
            new = new.next
        
        return new_head

        


        