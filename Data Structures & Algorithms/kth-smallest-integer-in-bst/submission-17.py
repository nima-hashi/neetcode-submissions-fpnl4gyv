# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cur = root
        cnt = 0
        while cur:
            if not cur.left:
                cnt += 1
                if cnt == k:
                    return cur.val
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    cnt += 1
                    if cnt == k:
                        return cur.val
                    cur = cur.right
        return -1







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
        


        # cnt = k
        # res = 0

        # def dfs(node):

        #     nonlocal cnt, res

        #     if not node:
        #         return 
        
        #     dfs(node.left)
        #     if cnt == 0:
        #         return
        #     cnt -= 1
        #     if cnt == 0:
        #         res = node.val
        #         return
        #     dfs(node.right)
        
        # dfs(root)
        # return res
        