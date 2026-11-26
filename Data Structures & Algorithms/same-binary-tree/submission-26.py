# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #iterative dfs

        pStack = [p]
        qStack = [q]

        while pStack and qStack:

            node1 = pStack.pop()
            node2 = qStack.pop()
            
            if not node1 and not node2:
                continue
            
            if not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            pStack.append(node1.left)
            pStack.append(node1.right)
            
            qStack.append(node2.left)
            qStack.append(node2.right)
        
        return not pStack and not qStack
            






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
        