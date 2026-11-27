# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #result = []
        # stack = []
        # cur = root
        # n = 0

        # while stack or cur:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     n += 1
        #     if n == k:
        #         return cur.val
        #     #result.append(cur.val)
        #     cur = cur.right
        


        cnt = k
        res = root.val

        def dfs(node):

            nonlocal cnt, res

            if not node:
                return 
        
            dfs(node.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res
        