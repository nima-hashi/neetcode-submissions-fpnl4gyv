# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # dfs 

        if not root:
            return 0
        
        depth = 0
        stack = [(root, 1)]

        while stack:
            node, d = stack.pop()
            depth = max(depth, d)
            if node.right:
                stack.append((node.right, d + 1))
            if node.left:
                stack.append((node.left, d + 1))

        return depth
        

        #bfs

        # depth = 0

        # if not root:
        #     return depth
        
        # queue = deque([root])
        # while queue:
        #     queueLen = len(queue)
        #     for i in range(queueLen):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     depth += 1
        # return depth
                

        


        # if not root:
        #     return 0
        
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)
        # return 1 + max(left, right)
        