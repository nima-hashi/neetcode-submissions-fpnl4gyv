# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        def dfs(node, depth):
            if not node:
                return []

            if depth == len(res):
                res.append([])
            
            res[depth].append(node.val)

            if node.left:
                dfs(node.left, depth + 1)
            
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
            

        




        # if not root:
        #     return []
        
        # queue = deque([root])
        # res = []

        # while queue:
        #     qLen = len(queue)
        #     level = []
        #     for i in range(qLen):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     res.append(level)
        # return res

        