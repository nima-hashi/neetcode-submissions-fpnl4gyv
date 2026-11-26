# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right

        #BFS 
        # queue = deque([(p,q)])

        # while queue:
        #     for i in range(len(queue)):
        #         pNode, qNode = queue.popleft()
        #         if not pNode and not qNode:
        #             continue
        #         if not pNode or not qNode:
        #             return False
        #         if pNode.val != qNode.val:
        #             return False
                
        #         queue.append((pNode.left, qNode.left))
        #         queue.append((pNode.right, qNode.right))
        # return True
                

        #iterative dfs

        # stack = [(p, q)]
        # while stack:
        #     pNode, qNode = stack.pop()

        #     if not pNode and not qNode:
        #         continue
        #     if not pNode or not qNode:
        #         return False
        #     if pNode.val != qNode.val:
        #         return False
            
        #     stack.append((pNode.left, qNode.left))
        #     stack.append((pNode.right, qNode.right))

        # return True

        #dfs recursion sol 2

        # if not p and not q:
        #     return True
        
        # if p and q and p.val == q.val:
        #     left = self.isSameTree(p.left, q.left)
        #     right = self.isSameTree(p.right, q.right)
        #     return left and right
        
        # return False


        #dfs recursion sol 1

        # if not p and not q:
        #     return True

        # if (not p and q) or (not q and p) or (p and q and p.val != q.val):
        #     return False
        
        # left = self.isSameTree(p.left, q.left)
        # right = self.isSameTree(p.right, q.right)

        # return left and right
        