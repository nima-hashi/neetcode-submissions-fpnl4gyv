# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, depth):
            if not node:
                return []

            if depth == len(res):
                res.append(node.val)

            if node.right:
                dfs(node.right, depth + 1)
            if node.left:
                dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res




        # if not root:
        #     return []
        
        # res = []
        # queue = deque([root])

        # while queue:
        #     qLen = len(queue)
        #     for i in range(qLen):
        #         node = queue.popleft()
        #         if i == qLen - 1:
        #             res.append(node.val)
                
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return res


        