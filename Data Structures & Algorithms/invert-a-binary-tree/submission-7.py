# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        #bfs 
        if not root:
            return None
        
        queue = deque([root])
        while queue:
            qLen = len(queue)
            for i in range(qLen):
                node = queue.pop()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

        



        # iterative dfs

        # if not root:
        #     return None
        
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
            
        #     node.left, node.right = node.right, node.left
        
        # return root
    

        